"""Builds a study from a config file: the glue shared by every entry point.

Configs are YAML read with OmegaConf, with ``key=value`` command-line overrides
(see ``experiments/explanations/conf/``). LLM settings reuse the completion
configs in ``experiments/conf/approach/completion/``: ``provider`` is one of
``cli`` / ``anthropic`` / ``openai_compatible`` (see :mod:`robocode.utils.llm`)
or ``mock`` for :class:`~robocode.explanations.mock_llm.MockLLMClient`.
API keys are read from the environment variable named by ``api_key_env``,
never from the config.

Each session gets its own LLM clients, so a client-side conversation cache
(as in the Claude CLI client) cannot carry anything from one user or condition
to another.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from omegaconf import DictConfig, OmegaConf

from robocode.explanations.explanation_generator import ExplanationGenerator
from robocode.explanations.logger import ExperimentLogger, read_jsonl
from robocode.explanations.mock_llm import MockLLMClient
from robocode.explanations.policy_provider import PolicyProvider
from robocode.explanations.runner import StudySession, build_schedule
from robocode.explanations.understanding import TestBank, TestBankConfig
from robocode.explanations.user_model import (
    CONDITIONS,
    LLMProfileUpdater,
    UserMemoryStore,
    get_condition,
)
from robocode.utils.llm import LLMClient, create_llm_client

_SECRET_KEYS = ("api_key", "auth_token", "token", "secret")


def load_config(path: str | Path, overrides: list[str] | None = None) -> DictConfig:
    """Load a study YAML and apply dotlist overrides (``a.b=value``)."""
    cfg = OmegaConf.load(path)
    if overrides:
        cfg = OmegaConf.merge(cfg, OmegaConf.from_dotlist(overrides))
    assert isinstance(cfg, DictConfig)
    return cfg


def make_llm(cfg: DictConfig) -> LLMClient:
    """A completion client for one role, or the offline mock."""
    if cfg["provider"] == "mock":
        return MockLLMClient()
    return create_llm_client(cfg)


def public_model_info(cfg: DictConfig) -> dict[str, Any]:
    """The LLM config as logged: everything but credential values."""
    data = OmegaConf.to_container(cfg, resolve=True)
    assert isinstance(data, dict)
    return {
        str(k): v
        for k, v in data.items()
        if not any(s in str(k) for s in _SECRET_KEYS) or str(k) == "api_key_env"
    }


def check_llm_config(cfg: DictConfig) -> None:
    """Reject LLM settings that would put a credential in the config or logs.

    ``api_key_env`` must be the *name* of an environment variable (e.g.
    ``OPENAI_API_KEY``), not the key itself.
    """
    for role in ("explainer_llm", "updater_llm"):
        name = cfg[role].get("api_key_env", "")
        if name and not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", str(name)):
            raise ValueError(
                f"{role}.api_key_env must name an environment variable (e.g. "
                "OPENAI_API_KEY), but its value looks like a key. Remove the key from "
                "the config, run `export OPENAI_API_KEY=...` in your shell, and set "
                f"{role}.api_key_env: OPENAI_API_KEY."
            )


def test_bank_config(cfg: DictConfig) -> TestBankConfig:
    """The ``test_bank`` section as a :class:`TestBankConfig`."""
    data = OmegaConf.to_container(cfg.test_bank, resolve=True)
    assert isinstance(data, dict)
    return TestBankConfig(**{str(k): v for k, v in data.items()})


def assign_condition(study_seed: int, user_id: str, conditions: list[str]) -> str:
    """Deterministic between-subjects assignment for human participants."""
    digest = hashlib.sha256(f"condition:{study_seed}:{user_id}".encode()).hexdigest()
    return conditions[int(digest, 16) % len(conditions)]


@dataclass
class StudyContext:
    """Components shared by all sessions of one study."""

    cfg: DictConfig
    provider: PolicyProvider
    bank: TestBank
    memory: UserMemoryStore
    logger: ExperimentLogger

    @classmethod
    def from_config(cls, cfg: DictConfig) -> StudyContext:
        """Load policies and the test bank, and prepare output directories.

        Validates the config before anything is written to disk.
        """
        check_llm_config(cfg)
        study_dir = Path(cfg.output_dir)
        provider = PolicyProvider(
            cfg.policy_root, envs=list(cfg.envs) if cfg.get("envs") else None
        )
        bank = TestBank.load(cfg.test_bank_dir)
        testable = [p for p in provider.list_policies() if bank.tests_for(p.policy_id)]
        if int(cfg.num_rounds) > len(testable):
            raise ValueError(
                f"num_rounds={cfg.num_rounds} but envs={list(cfg.get('envs') or [])} "
                f"have only {len(testable)} policies with A/B tests. Lower num_rounds "
                "or add environments (policies never repeat within a participant)."
            )
        logger = ExperimentLogger(study_dir)
        resolved = OmegaConf.to_container(cfg, resolve=True)
        assert isinstance(resolved, dict)
        logger.write_config({str(k): v for k, v in resolved.items()})
        return cls(
            cfg=cfg,
            provider=provider,
            bank=bank,
            memory=UserMemoryStore(study_dir / "memory"),
            logger=logger,
        )

    def policy_pool(self) -> list[str]:
        """Policies that may be explained: in the configured envs and in the bank."""
        return [
            p.policy_id
            for p in self.provider.list_policies()
            if self.bank.tests_for(p.policy_id)
        ]

    def make_session(
        self,
        user_id: str,
        condition_name: str,
        participant_info: dict[str, Any] | None = None,
    ) -> StudySession:
        """A new (or resumed) session for one user in one condition."""
        cfg = self.cfg
        condition = get_condition(condition_name)
        schedule = build_schedule(
            self.bank,
            study_seed=int(cfg.study_seed),
            user_id=user_id,
            num_rounds=int(cfg.num_rounds),
            policy_ids=self.policy_pool(),
            num_eval_rounds=int(cfg.get("num_eval_rounds", 0)),
            balance_difficulty=bool(cfg.get("balance_difficulty", True)),
        )
        generator = ExplanationGenerator(
            make_llm(cfg.explainer_llm),
            model_info=public_model_info(cfg.explainer_llm),
            max_code_chars=int(cfg.get("max_code_chars", 80_000)),
        )
        updater = None
        if condition.adapt:
            updater = LLMProfileUpdater(
                make_llm(cfg.updater_llm), model_info=public_model_info(cfg.updater_llm)
            )
        session = StudySession(
            study_id=str(cfg.study_id),
            user_id=user_id,
            condition=condition,
            schedule=schedule,
            provider=self.provider,
            bank=self.bank,
            generator=generator,
            updater=updater,
            memory=self.memory,
            logger=self.logger,
            participant_info=participant_info,
        )
        session.resume(self.completed_rounds(user_id, condition_name))
        return session

    def completed_rounds(
        self, user_id: str, condition_name: str
    ) -> list[dict[str, Any]]:
        """Logged rounds for one (user, condition), for resuming after a restart."""
        path = self.logger.study_dir / "rounds.jsonl"
        if not path.exists():
            return []
        return [
            r
            for r in read_jsonl(path)
            if r["user_id"] == user_id and r["condition"] == condition_name
        ]


def all_conditions() -> list[str]:
    """Every defined condition name."""
    return list(CONDITIONS)
