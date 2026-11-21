"""Tests for the neutral (fact-only) strict-blackbox prompt and its protocol."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import numpy as np
import pytest
from gymnasium.spaces import Box
from omegaconf import DictConfig

from robocode import prompts
from robocode.approaches.agentic_approach import AgenticApproach
from robocode.approaches.agentic_per_instance_approach import (
    AgenticPerInstanceApproach,
)
from robocode.environments.kinder_geom2d_env import KinderGeom2DEnv
from robocode.environments.variable_object_count_env import VariableObjectCountEnv
from robocode.utils import rate_limit
from robocode.utils.backends import DEFAULT_BACKEND_CFG
from robocode.utils.backends.agent_files import build_agents_md, build_claude_md
from robocode.utils.backends.codex import CodexBackend
from robocode.utils.env_client import BlackboxEnv
from robocode.utils.env_server import (
    decode,
    encode,
    env_server_running,
    serialize_space,
)
from robocode.utils.env_server_runtime import _dispatch, _HandleRegistry, _StepLimit
from robocode.utils.sandbox import SandboxConfig

_OBSTRUCTION2D = "kinder.envs.kinematic2d.obstruction2d:Obstruction2DEnv"

# Phrases that steer the agent; none may appear in a neutral prompt.
_STEERING = (
    "optimal",
    "expert",
    "seconds",
    "wall-clock",
    "budget",
    "efficiently",
    "exhaustive",
    "slow planners",
    "computed plan",
    "interrupted",
    "test scripts",
    "test_approach",
    "Plan subagent",
    "delegate",
    "thinking",
    "never assume a fixed object count",
    "any number of objects",
    "env.max_steps",
    "IMPORTANT",
    "CRITICAL",
    "VARIABLE",
)


def _assert_no_steering(text: str) -> None:
    for phrase in _STEERING:
        assert phrase not in text, phrase


# ---------------------------------------------------------------------------
# Prompt text
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("backend_name", ["claude", "codex", "opencode"])
def test_neutral_system_prompt_states_goal_and_commit_rule_only(
    backend_name: str,
) -> None:
    """Goal, scoring rule, files, and the verbatim commit rule; nothing else."""
    system = prompts.build_neutral_system_prompt(backend_name=backend_name)
    assert system.startswith(prompts.NEUTRAL_GOAL)
    assert "`terminated=True` within the episode's step limit" in system
    assert "may differ from the ones you see during development" in system
    assert (
        "a general solution that works across different instances of this "
        "environment, not only the instances you try" in system
    )
    version_control = prompts._VERSION_CONTROL  # pylint: disable=protected-access
    assert version_control.strip() in system
    _assert_no_steering(system)
    assert "subagent" not in system.lower()


@pytest.mark.parametrize("object_centric", [True, False])
def test_neutral_task_prompt_keeps_isolation_facts(object_centric: bool) -> None:
    """The no-libraries note and import allowlist stay verbatim; advice is gone."""
    task = prompts.build_neutral_task_prompt(
        python_executable="/opt/py",
        object_centric=object_centric,
        mcp_tools=("render_state", "render_policy"),
    )
    # pylint: disable=protected-access
    assert prompts._STRICT_BB_NOTE.strip() in task
    assert prompts._STRICT_BB_IMPORT_RULE.strip() in task
    assert prompts._STRICT_BB_HELPERS in task
    assert prompts._AGENTIC_CLASS_CODE in task
    # pylint: enable=protected-access
    assert "max_steps" not in task  # no step-limit number is given
    assert "Run Python with `/opt/py`." in task
    assert "mcp__robocode-tools__render_state" in task
    assert "not from inside subagents" in task
    _assert_no_steering(task)
    assert "\n\n\n" not in task


def test_neutral_task_prompt_object_centric_vs_vector() -> None:
    """Object-centric runs document the typed-object API; vector runs do not."""
    oc = prompts.build_neutral_task_prompt(python_executable="py", object_centric=True)
    vec = prompts.build_neutral_task_prompt(
        python_executable="py", object_centric=False
    )
    assert "ObjectCentricState" in oc
    assert "number of objects varies between episodes" in oc
    assert "ObjectCentricState" not in vec
    assert "fixed-length numpy arrays" in vec
    assert "MCP" not in oc  # no tools configured


def test_neutral_task_prompt_inlines_description() -> None:
    """An env description is inlined right after the opener."""
    task = prompts.build_neutral_task_prompt(
        python_executable="py", object_centric=True, env_description="Push the box.\n"
    )
    assert "The environment is described below.\n\nPush the box.\n\n" in task


def test_neutral_task_prompt_drops_generalization_advice_from_card() -> None:
    """A variable-count card keeps its task facts but loses its Generalization
    section."""
    env = _obstruction_env()
    try:
        card = env.env_description_blackbox
    finally:
        env.close()
    assert "## Generalization" in card  # the legacy prompt still inlines it
    task = prompts.build_neutral_task_prompt(
        python_executable="py", object_centric=True, env_description=card
    )
    assert "## Generalization" not in task
    assert "in principle unbounded" not in task
    assert "Do not assume a fixed object count" not in task
    for kept in ("## Observation", "## Action Space", "## Reward"):
        assert kept in task


def test_legacy_prompts_keep_their_advice() -> None:
    """The refactor that shares fragments leaves the legacy text in place."""
    assert "(e.g., a computed plan)" in prompts.AGENTIC_CLASS_INTERFACE
    assert prompts.SYSTEM_FILE_DISCIPLINE.startswith("IMPORTANT: You MUST write ALL")
    version_control = prompts._VERSION_CONTROL  # pylint: disable=protected-access
    assert prompts.SYSTEM_FILE_DISCIPLINE.endswith(version_control)
    legacy = prompts.blackbox_interaction_spec(strict=True)
    assert "`env.max_steps` is the episode step limit used at evaluation time." in (
        legacy
    )


def test_neutral_agent_files_state_only_paths_and_interpreter() -> None:
    """Sandbox CLAUDE.md/AGENTS.md drop context-management advice."""
    for build in (build_claude_md, build_agents_md):
        neutral = build("/opt/py", (), neutral=True)
        assert "relative paths" in neutral
        assert "The Python interpreter is at /opt/py" in neutral
        assert "CONTEXT MANAGEMENT" not in neutral
        assert "test_approach.py" not in neutral
        assert "CONTEXT MANAGEMENT" in build("/opt/py", ())


def test_neutral_resume_prompts_only_say_what_happened() -> None:
    """Error-recovery messages carry no brevity or finishing advice."""
    neutral = SandboxConfig(sandbox_dir=Path("."), neutral_prompt=True)
    legacy = SandboxConfig(sandbox_dir=Path("."))
    for kind in ("output_token", "context", "api_error"):
        # pylint: disable=protected-access
        text = rate_limit._resume_prompt(kind, neutral)
        assert text.endswith("Continue the task.")
        assert "concise" not in text and "finish" not in text
        assert rate_limit._resume_prompt(kind, legacy) != text


# ---------------------------------------------------------------------------
# Approach configuration
# ---------------------------------------------------------------------------


def _strict_args(**overrides: Any) -> dict[str, Any]:
    space = Box(-1.0, 1.0, (2,), dtype=np.float32)
    args: dict[str, Any] = {
        "action_space": space,
        "observation_space": space,
        "seed": 0,
        "primitives": {},
        "backend": DEFAULT_BACKEND_CFG,
        "container_backend": "docker",
        "blackbox": True,
        "blackbox_strict": True,
        "env_cfg": '{"_target_": "unused.ForValidation"}',
        "mcp_tools": (),
        "max_steps": 1000,
        "eval_timeout": 600.0,
        "prompt_style": "neutral",
    }
    args.update(overrides)
    return args


def test_neutral_approach_builds_neutral_prompts() -> None:
    """prompt_style=neutral swaps both prompts and enables the reset-info limit."""
    approach = AgenticApproach(**_strict_args())
    prompt, system, init_files = (
        approach._build_agentic_prompts()  # pylint: disable=protected-access
    )
    assert system == prompts.build_neutral_system_prompt(backend_name="claude")
    assert prompt.startswith("You are writing an approach for an environment")
    _assert_no_steering(prompt + system)
    assert set(init_files) == {"env_client.py"}


def test_legacy_approach_is_unchanged_by_default() -> None:
    """Without prompt_style the legacy prompts and eval info are used."""
    approach = AgenticApproach(**_strict_args(prompt_style="legacy"))
    _, system, _ = approach._build_agentic_prompts()  # pylint: disable=protected-access
    assert "slow planners" in system


@pytest.mark.parametrize(
    "overrides,message",
    [
        ({"prompt_style": "vanilla"}, "prompt_style must be one of"),
        ({"blackbox_strict": False}, "strict blackbox only"),
        ({"max_steps": None}, "requires max_steps"),
    ],
)
def test_neutral_approach_rejects_unsupported_setups(
    overrides: dict[str, Any], message: str
) -> None:
    """Neutral is defined only for strict-blackbox generalized runs."""
    with pytest.raises(ValueError, match=message):
        AgenticApproach(**_strict_args(**overrides))


def test_neutral_rejects_per_instance_runs() -> None:
    """Per-instance runs keep their budget-stewardship prompt."""
    with pytest.raises(ValueError, match="generalized runs only"):
        AgenticPerInstanceApproach(**_strict_args())


def test_neutral_warns_about_a_short_eval_cutoff(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """A cutoff under the safety cap would be an unstated runtime budget."""
    AgenticApproach(**_strict_args(eval_timeout=60.0))
    assert "safety cap" in caplog.text


# ---------------------------------------------------------------------------
# Step limit: development server and evaluation loop
# ---------------------------------------------------------------------------


def _obstruction_env() -> VariableObjectCountEnv:
    return VariableObjectCountEnv(
        constant_object_env_path=_OBSTRUCTION2D,
        count_kwarg="num_obstructions",
        count_object_prefix="obstruction",
        design_counts=[0, 1],
        eval_counts=[0, 1, 2],
        bilevel_env_name="obstruction2d",
        base_steps=2,
        steps_per_object=1,
    )


def test_server_step_limit_follows_object_count(tmp_path: Path) -> None:
    """A variable-count episode is truncated at max_steps_for_count, silently."""
    env = _obstruction_env()
    registry = _HandleRegistry()
    limit = _StepLimit(fallback=1000)
    try:
        reset = _dispatch(
            env,
            {"cmd": "reset", "seed": 0, "options": {"object_count": 2}},
            tmp_path,
            registry,
            strict=True,
            step_limit=limit,
        )
        assert "max_steps" not in decode(reset["info"])
        assert env.max_steps_for_count(2) == 4
        action = encode(np.zeros_like(env.action_space.sample()))
        truncated = [
            _dispatch(
                env,
                {"cmd": "step", "action": action},
                tmp_path,
                registry,
                strict=True,
                step_limit=limit,
            )["truncated"]
            for _ in range(4)
        ]
        assert truncated == [False, False, False, True]
    finally:
        env.close()


def test_server_without_step_limit_is_unchanged(tmp_path: Path) -> None:
    """Legacy servers add no info key and never truncate on their own."""
    env = _obstruction_env()
    try:
        reset = _dispatch(env, {"cmd": "reset", "seed": 0}, tmp_path, _HandleRegistry())
        assert "max_steps" not in decode(reset["info"])
    finally:
        env.close()


def test_env_server_subprocess_enforces_fallback_limit(tmp_path: Path) -> None:
    """--step-limit reaches the server process; fixed-count envs use its value."""
    env_cfg = {
        "_target_": "robocode.environments.kinder_geom2d_env.KinderGeom2DEnv",
        "env_id": "kinder/Motion2D-p0-v0",
    }
    direct = KinderGeom2DEnv("kinder/Motion2D-p0-v0")
    sandbox_dir = tmp_path / "sandbox"
    sandbox_dir.mkdir()
    try:
        with env_server_running(json.dumps(env_cfg), sandbox_dir, step_limit=3) as (
            port,
            token,
        ):
            meta = {
                "host": "127.0.0.1",
                "port": port,
                "token": token,
                "observation_space": serialize_space(direct.observation_space),
                "action_space": serialize_space(direct.action_space),
                "max_steps": None,
            }
            with BlackboxEnv(meta) as client:
                _, info = client.reset(seed=0)
                assert "max_steps" not in info
                action = np.zeros_like(direct.action_space.sample())
                flags = [client.step(action)[3] for _ in range(3)]
                assert flags == [False, False, True]
                assert client.max_steps is None
    finally:
        direct.close()


# ---------------------------------------------------------------------------
# Codex: silent budget, no continuation after a voluntary stop
# ---------------------------------------------------------------------------


def _codex(tmp_path: Path, **config: Any) -> tuple[CodexBackend, SandboxConfig, Path]:
    backend = CodexBackend(
        DictConfig(
            {
                "input_usd_per_mtok": 4,
                "cached_input_usd_per_mtok": 0.4,
                "output_usd_per_mtok": 20,
            }
        )
    )
    sandbox = SandboxConfig(
        sandbox_dir=tmp_path,
        max_budget_usd=20,
        system_prompt="SYSTEM",
        prompt="TASK",
        neutral_prompt=True,
        **config,
    )
    backend.build_cli_cmd(sandbox)
    return backend, sandbox, tmp_path / ".agent_sessions/codex"


def _record(output_tokens: int) -> str:
    return (
        json.dumps(
            {
                "type": "token_usage_record",
                "payload": {
                    "response_id": "root",
                    "usage": {
                        "input_tokens": 0,
                        "cached_input_tokens": 0,
                        "output_tokens": output_tokens,
                    },
                },
            }
        )
        + "\n"
    )


def test_neutral_codex_writes_no_budget_text_or_status(tmp_path: Path) -> None:
    """AGENTS.md is the system prompt plus sandbox facts; no budget file appears."""
    backend, sandbox, sessions = _codex(tmp_path)
    backend.setup_sandbox_files(sandbox, docker_python="/opt/py")
    agents = (tmp_path / "AGENTS.md").read_text()
    assert agents.startswith("SYSTEM\n\n")
    assert "budget" not in agents.lower()
    assert "solution_confident" not in agents
    backend._write_budget_status(5.0)  # pylint: disable=protected-access
    assert not (sessions / "budget_status.json").exists()


def test_neutral_codex_resume_sends_the_plain_prompt(tmp_path: Path) -> None:
    """Error-recovery resumes carry no remaining-budget message."""
    backend, _, _ = _codex(tmp_path)
    resumed = SandboxConfig(
        sandbox_dir=tmp_path,
        max_budget_usd=12,
        prompt="Continue the task.",
        resume_previous_session=True,
        neutral_prompt=True,
    )
    assert backend.stdin_text(resumed) == "Continue the task."


def test_neutral_codex_voluntary_stop_is_final(tmp_path: Path) -> None:
    """Stopping early without a confidence marker is not resumed."""
    backend, _, sessions = _codex(tmp_path)
    (sessions / "root.jsonl").write_text(_record(100_000))  # $2 of $20 spent
    proc = MagicMock(spec=subprocess.Popen)
    proc.stdout = iter(())
    proc.stderr = MagicMock()
    proc.stderr.read.return_value = ""
    proc.returncode = 0
    result = backend.parse_stream(proc)
    assert not result.unconfirmed_solution
    assert not result.is_error
