"""Policy Provider: frozen generated policies and their rollouts.

Policies come from the agent_runs archive, laid out as
``<root>/environments/<Env>/runs/<run>/evidence/`` with ``final/approach.py``
(the frozen ``GeneratedApproach``), ``config.yaml`` (the experiment config the
policy was synthesized under), ``task.md`` (the task description the coding
agent saw) and ``results.json`` (its scored evaluation).

Environments are rebuilt from each run's saved Hydra config, and policies are
loaded with :func:`robocode.utils.episode.load_generated_approach`, so rollouts
here match the scored evaluation's environment and loading path.
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import yaml
from hydra.utils import instantiate
from numpy.typing import NDArray
from omegaconf import OmegaConf

from robocode.utils.episode import load_generated_approach

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PolicyRecord:
    """One frozen generated policy and the task it was written for."""

    policy_id: str  # "<Env>/<run>"
    env_name: str
    run_name: str
    approach_path: Path
    evidence_dir: Path
    environment_cfg: dict[str, Any]
    max_steps: int
    metadata: dict[str, Any] = field(default_factory=dict)
    task_path: Path | None = None  # overrides evidence_dir / "task.md"

    def source(self) -> str:
        """The policy's program text."""
        return self.approach_path.read_text(encoding="utf-8")

    def task_description(self) -> str:
        """The task description the coding agent was given (may be empty)."""
        path = self.task_path or self.evidence_dir / "task.md"
        return path.read_text(encoding="utf-8") if path.exists() else ""

    @property
    def env_key(self) -> str:
        """Identifies the environment config; policies sharing it are comparable."""
        return json.dumps(self.environment_cfg, sort_keys=True)


class PolicyProvider:
    """Indexes the policies under an agent_runs-style archive root."""

    def __init__(
        self,
        root: str | Path,
        envs: list[str] | None = None,
        exclude: list[str] | None = None,
    ) -> None:
        self._root = Path(root)
        self._policies: dict[str, PolicyRecord] = {}
        excluded = set(exclude or [])
        env_root = self._root / "environments"
        for env_dir in sorted(p for p in env_root.iterdir() if p.is_dir()):
            if envs is not None and env_dir.name not in envs:
                continue
            for run_dir in sorted(
                p for p in (env_dir / "runs").iterdir() if p.is_dir()
            ):
                record = _load_record(env_dir.name, run_dir)
                if record is not None and record.policy_id not in excluded:
                    self._policies[record.policy_id] = record
        if not self._policies:
            raise ValueError(f"No policies found under {env_root}")

    def list_policies(self) -> list[PolicyRecord]:
        """All indexed policies, sorted by id."""
        return [self._policies[k] for k in sorted(self._policies)]

    def get(self, policy_id: str) -> PolicyRecord:
        """Look up a policy by id."""
        return self._policies[policy_id]

    def same_env(self, policy: PolicyRecord) -> list[PolicyRecord]:
        """Other policies written for the same environment config."""
        return [
            p
            for p in self.list_policies()
            if p.env_key == policy.env_key and p.policy_id != policy.policy_id
        ]


def policy_from_path(
    approach_path: str | Path, task_path: str | Path | None = None
) -> PolicyRecord:
    """A policy from any ``approach.py``, for explaining it outside a study.

    In the agent_runs layout (``.../evidence/final/approach.py``) the task
    description is found automatically; otherwise pass ``task_path`` (or the
    explanation is written from the code alone).
    """
    approach_path = Path(approach_path)
    if not approach_path.is_file():
        raise FileNotFoundError(approach_path)
    in_archive = approach_path.parent.name == "final"
    evidence = approach_path.parent.parent if in_archive else approach_path.parent
    run_name = evidence.parent.name if in_archive else approach_path.stem
    return PolicyRecord(
        policy_id=str(approach_path),
        env_name="",
        run_name=run_name,
        approach_path=approach_path,
        evidence_dir=evidence,
        environment_cfg={},
        max_steps=0,
        task_path=Path(task_path) if task_path is not None else None,
    )


def _load_record(env_name: str, run_dir: Path) -> PolicyRecord | None:
    evidence = run_dir / "evidence"
    approach = evidence / "final" / "approach.py"
    config_path = evidence / "config.yaml"
    if not approach.exists() or not config_path.exists():
        logger.warning("Skipping %s: missing approach.py or config.yaml", run_dir)
        return None
    cfg = yaml.safe_load(config_path.read_text())
    backend = (cfg.get("approach") or {}).get("backend") or {}
    metadata: dict[str, Any] = {
        "agent_backend": backend.get("backend"),
        "agent_model": backend.get("model"),
        "agent_effort": backend.get("effort") or backend.get("reasoning_effort"),
        "replicate_seed": cfg.get("replicate_seed"),
        "experiment_id": cfg.get("experiment_id"),
        "approach_lines": len(approach.read_text().splitlines()),
    }
    results_path = evidence / "results.json"
    if results_path.exists():
        results = json.loads(results_path.read_text())
        metadata["solve_rate"] = results.get("solve_rate")
        metadata["mean_eval_steps"] = results.get("mean_eval_steps")
    return PolicyRecord(
        policy_id=f"{env_name}/{run_dir.name}",
        env_name=env_name,
        run_name=run_dir.name,
        approach_path=approach,
        evidence_dir=evidence,
        environment_cfg=cfg["environment"],
        max_steps=int(cfg.get("max_steps", 1000)),
        metadata=metadata,
    )


@dataclass
class Rollout:
    """One episode of one policy from one initial state."""

    policy_id: str
    seed: int
    object_count: int | None
    solved: bool
    num_steps: int
    trajectory: NDArray[np.float64]  # (T+1, D) state features over time
    object_names: list[str]  # names for object-centric states, else []
    object_change_order: list[str]  # objects in the order they first change
    frames: list[NDArray[np.uint8]] = field(default_factory=list, repr=False)
    error: str | None = None


class RolloutEngine:
    """Runs policies on seeded initial states, caching one env per config."""

    def __init__(self, wall_time_limit_s: float = 60.0) -> None:
        self._envs: dict[str, Any] = {}
        self._wall_time_limit_s = wall_time_limit_s

    def env_for(self, policy: PolicyRecord) -> Any:
        """The (cached) environment instance for a policy's config."""
        if policy.env_key not in self._envs:
            self._envs[policy.env_key] = instantiate(
                OmegaConf.create(policy.environment_cfg)
            )
        return self._envs[policy.env_key]

    def rollout(
        self,
        policy: PolicyRecord,
        seed: int,
        object_count: int | None = None,
        max_steps: int | None = None,
        render: bool = False,
        frame_stride: int = 1,
    ) -> Rollout:
        """Run one episode.

        Policy exceptions are recorded, not raised.
        """
        env = self.env_for(policy)
        max_steps = max_steps or policy.max_steps
        approach = load_generated_approach(
            policy.approach_path, env.action_space, env.observation_space, {}
        )
        options = {"object_count": object_count} if object_count is not None else None
        obs, info = env.reset(seed=seed, options=options)
        names = _object_names(obs)
        states = [_featurize(obs, names)]
        frames: list[NDArray[np.uint8]] = []
        if render:
            frames.append(_render(env))
        solved = False
        error = None
        steps = 0
        start = time.monotonic()
        try:
            approach.reset(obs, info)
            for steps in range(1, max_steps + 1):
                obs, _, terminated, truncated, info = env.step(approach.get_action(obs))
                states.append(_featurize(obs, names))
                if render and (steps % frame_stride == 0 or terminated or truncated):
                    frames.append(_render(env))
                if terminated or truncated:
                    solved = bool(terminated)
                    break
                if time.monotonic() - start > self._wall_time_limit_s:
                    error = "wall_time_limit"
                    break
        except Exception as exc:  # pylint: disable=broad-exception-caught
            error = f"{type(exc).__name__}: {exc}"
            logger.warning(
                "Rollout of %s seed %d failed: %s", policy.policy_id, seed, error
            )
        trajectory = np.asarray(states, dtype=np.float64)
        return Rollout(
            policy_id=policy.policy_id,
            seed=seed,
            object_count=info.get("object_count", object_count),
            solved=solved,
            num_steps=steps,
            trajectory=trajectory,
            object_names=names,
            object_change_order=_change_order(obs, names, trajectory),
            frames=frames,
            error=error,
        )


def _object_names(obs: Any) -> list[str]:
    if hasattr(obs, "get_object_names"):
        return sorted(obs.get_object_names())
    return []


def _featurize(obs: Any, names: list[str]) -> NDArray[np.float64]:
    """A flat numeric vector of the full state, in a fixed object order."""
    if names:
        objs = [obs.get_object_from_name(n) for n in names]
        return np.asarray(obs.vec(objs), dtype=np.float64).ravel()
    return np.asarray(obs, dtype=np.float64).ravel()


def _change_order(
    obs: Any, names: list[str], trajectory: NDArray[np.float64], tol: float = 1e-4
) -> list[str]:
    """Objects sorted by the step at which their features first change.

    A coarse, environment-agnostic "decision signature": e.g. which obstruction a policy
    moves first. Empty for flat-vector states, which have no objects.
    """
    if not names:
        return []
    widths = [len(obs[obs.get_object_from_name(n)]) for n in names]
    first: dict[str, int] = {}
    offset = 0
    for name, width in zip(names, widths):
        block = trajectory[:, offset : offset + width]
        offset += width
        moved = np.nonzero(np.abs(block - block[0]).max(axis=1) > tol)[0]
        if len(moved):
            first[name] = int(moved[0])
    return sorted(first, key=lambda n: (first[n], n))


def _render(env: Any) -> NDArray[np.uint8]:
    frame = env.render()
    return np.asarray(frame, dtype=np.uint8)
