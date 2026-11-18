"""Tests for virtual_tools_env.py (needs node.js, PyExecJS, and the tool-games
submodule; skipped otherwise)."""

# The availability checks must run before the env import, which needs all three.
# pylint: disable=wrong-import-position

import importlib.util
import json
import shutil
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import numpy as np
import pytest

_ROOT = Path(__file__).resolve().parents[2]
if importlib.util.find_spec("execjs") is None:
    pytest.skip("PyExecJS not installed", allow_module_level=True)
if shutil.which("node") is None:
    pytest.skip("node.js not on PATH", allow_module_level=True)
if not (_ROOT / "third-party" / "tool-games" / "environment").is_dir():
    pytest.skip("tool-games submodule not checked out", allow_module_level=True)

from hydra.utils import instantiate  # noqa: E402
from omegaconf import OmegaConf  # noqa: E402

from robocode.environments.variable_count import VariableCountEnv  # noqa: E402
from robocode.environments.virtual_tools_env import VirtualToolsEnv  # noqa: E402
from robocode.utils.env_client import BlackboxEnv  # noqa: E402
from robocode.utils.env_server import (  # noqa: E402
    decode,
    encode,
    env_server_running,
    serialize_space,
)

_CONFIG = OmegaConf.to_container(
    OmegaConf.load(_ROOT / "experiments/conf/environment/virtual_tools.yaml")
)
assert isinstance(_CONFIG, dict)
_CATAPULT = 2  # index of Original/Catapult in the config's level order
_VALIDATION = 18  # first held-out level
# A recorded human success on Catapult (tool obj2 = index 1), and a human failure.
_SOLVE = np.array([1.0, 409.0, 541.0], dtype=np.float64)
_MISS = np.array([1.0, 439.0, 158.0], dtype=np.float64)
_INSIDE_WALL = np.array([0.0, 5.0, 5.0], dtype=np.float64)


@pytest.fixture(scope="module", name="env")
def _env() -> Iterator[VirtualToolsEnv]:
    env = instantiate(_CONFIG)
    yield env
    env.close()


def _small_env(**kwargs: Any) -> VirtualToolsEnv:
    return VirtualToolsEnv(
        levels=["Original/Basic", "Original/Catapult", "Validation/Trap"],
        dev_levels=["Original/Basic", "Original/Catapult"],
        **kwargs,
    )


def test_config_levels_and_count_contract(env: VirtualToolsEnv) -> None:
    """All 28 levels load; the 18 Original ones are the development levels."""
    assert isinstance(env, VariableCountEnv)
    assert env.eval_counts == list(range(28))
    assert env.design_counts == list(range(18))
    assert env.levels[_CATAPULT] == "Original/Catapult"
    assert env.levels[_VALIDATION].startswith("Validation/")
    assert env.max_steps_for_count(0) == 30
    assert serialize_space(env.observation_space)["type"] == "JSONDict"
    # float64 so the sandbox client's dtype cast cannot move a placement.
    assert env.action_space.dtype == np.float64


def test_level_numbers_are_numbers(env: VirtualToolsEnv) -> None:
    """Physical values are numbers in every level, including Falling_v2, whose
    file stores some as text."""
    for index in env.eval_counts:
        world = env.reset(seed=0, options={"object_count": index})[0]["world"]
        entries = [*world["objects"].values(), world.get("defaults"), world["gcond"]]
        for entry in entries:
            for key in ("density", "friction", "elasticity", "duration"):
                if isinstance(entry, dict) and key in entry:
                    assert isinstance(entry[key], (int, float)), (index, key)


def test_known_solution_solves_in_one_attempt(env: VirtualToolsEnv) -> None:
    """A recorded human success solves the level and costs one attempt."""
    obs, info = env.reset(seed=0, options={"object_count": _CATAPULT})
    assert info == {}
    assert obs["attempts_used"] == 0 and obs["history"] == []
    obs, reward, terminated, truncated, info = env.step(_SOLVE)
    assert (reward, terminated, truncated) == (-1.0, True, False)
    assert info == {"accepted": True, "success": True}
    last = obs["history"][-1]
    assert last["success"] and last["sim_time"] < 20.0
    assert obs["solved"] and obs["attempts_used"] == 1
    with pytest.raises(RuntimeError):
        env.step(_SOLVE)


def test_failed_attempt_records_paths(env: VirtualToolsEnv) -> None:
    """A failure costs an attempt and records every moving object's path."""
    env.reset(seed=0, options={"object_count": _CATAPULT})
    obs, reward, terminated, truncated, _ = env.step(_MISS)
    assert (reward, terminated, truncated) == (-1.0, False, False)
    last = obs["history"][-1]
    assert last["accepted"] and not last["success"]
    assert last["sim_time"] == pytest.approx(20.0)
    assert {"Ball", "PLACED"} <= set(last["paths"])
    ball = last["paths"]["Ball"]
    assert len(ball["pos"]) == len(ball["rot"]) == 201  # every 0.1 s for 20 s


def test_rejected_placements_use_no_attempt(env: VirtualToolsEnv) -> None:
    """Overlapping and out-of-world placements are rejected without an attempt."""
    env.reset(seed=0, options={"object_count": _CATAPULT})
    for action in ([0.0, 5.0, 5.0], [1.0, 700.0, 300.0]):
        obs, reward, terminated, truncated, info = env.step(np.asarray(action))
        assert (reward, terminated, truncated) == (0.0, False, False)
        assert info == {"accepted": False, "success": False}
        assert obs["history"][-1] == {
            "tool": int(action[0]),
            "position": action[1:],
            "accepted": False,
        }
    assert obs["attempts_used"] == 0 and obs["rejected_placements"] == 2
    assert env.observation_space.contains(obs)


def test_non_finite_action_is_an_error(env: VirtualToolsEnv) -> None:
    """A NaN action is a program bug: it raises and changes nothing."""
    env.reset(seed=0, options={"object_count": _CATAPULT})
    with pytest.raises(ValueError, match="finite"):
        env.step(np.array([1.0, float("nan"), 100.0]))
    assert env.get_state()["history"] == []


def test_truncation_budgets() -> None:
    """The episode truncates when attempts or rejected placements run out."""
    env = _small_env(max_attempts=2, max_rejected_placements=2)
    env.reset(seed=0, options={"object_count": 1})
    assert env.step(_MISS)[3] is False
    assert env.step(_MISS)[3] is True
    env.reset(seed=0, options={"object_count": 1})
    assert env.step(_INSIDE_WALL)[3] is False
    assert env.step(_INSIDE_WALL)[3] is True


def test_synthesis_restriction_hides_held_out_levels() -> None:
    """After restrict_to_synthesis, held-out levels refuse to load."""
    env = _small_env()
    env.reset(seed=0, options={"object_count": 2})  # allowed before restricting
    env.restrict_to_synthesis()
    with pytest.raises(ValueError, match="held out"):
        env.reset(seed=0, options={"object_count": 2})
    for seed in range(6):
        env.reset(seed=seed)
        assert env.current_count in env.design_counts
    unrestricted = _small_env(hold_out_from_synthesis=False)
    unrestricted.restrict_to_synthesis()
    unrestricted.reset(seed=0, options={"object_count": 2})


def test_state_roundtrip_is_deterministic(env: VirtualToolsEnv) -> None:
    """A restored state steps exactly like the original; states survive the wire."""
    env.reset(seed=0, options={"object_count": _CATAPULT})
    env.step(_INSIDE_WALL)
    state = env.get_state()
    assert decode(json.loads(json.dumps(encode(state)))) == state
    first = env.step(_MISS)[0]
    other = _small_env()
    other.set_state(state)
    second = other.step(_MISS)[0]
    assert first == second


def test_render(env: VirtualToolsEnv) -> None:
    """Rendering returns an RGB frame before and after a placement."""
    env.reset(seed=0, options={"object_count": _CATAPULT})
    before: Any = env.render()
    env.step(_MISS)
    after: Any = env.render()
    for frame in (before, after):
        assert isinstance(frame, np.ndarray)
        assert frame.dtype == np.uint8 and frame.shape[2] == 3
    assert not np.array_equal(before, after)


def test_description_states_the_split(env: VirtualToolsEnv) -> None:
    """The description tells the agent which levels it can load and what is held out."""
    text = env.env_description_blackbox
    assert "development levels are indices 0-17." in text
    assert "10 more levels" in text
    for name in env.levels:  # no level names leak into the agent-facing text
        assert name.split("/")[1] not in text


def test_prompt_note_is_added_only_when_set(env: VirtualToolsEnv) -> None:
    """A prompt note adds one paragraph after the levels; the default adds none."""
    note = "Note that the levels are   just examples."
    noted = _small_env(prompt_note=note).env_description_blackbox
    plain = _small_env().env_description_blackbox
    assert "Note that the levels are just examples." in noted
    assert noted.replace("Note that the levels are just examples.\n\n", "") == plain
    assert "just examples" not in env.env_description_blackbox


def test_strict_server_roundtrip(tmp_path: Path, env: VirtualToolsEnv) -> None:
    """Through a strict env server: dict observations, hold-out, and rendering."""
    sandbox_dir = tmp_path / "sandbox"
    sandbox_dir.mkdir()
    (sandbox_dir / "approach.py").write_text(
        "class GeneratedApproach:\n"
        "    def __init__(self, action_space, observation_space, primitives):\n"
        "        pass\n"
        "    def reset(self, state, info):\n"
        "        pass\n"
        "    def get_action(self, state):\n"
        "        return [1.0, 409.0, 541.0]\n"
    )
    with env_server_running(json.dumps(_CONFIG), sandbox_dir, strict=True) as (
        port,
        token,
    ):
        meta = {
            "host": "127.0.0.1",
            "port": port,
            "token": token,
            "observation_space": serialize_space(env.observation_space),
            "action_space": serialize_space(env.action_space),
            "max_steps": 30,
            "strict": True,
        }
        with BlackboxEnv(meta, sandbox_root=sandbox_dir) as client:
            obs, _ = client.reset(seed=0, options={"object_count": _CATAPULT})
            direct, _ = env.reset(seed=0, options={"object_count": _CATAPULT})
            assert obs == direct
            obs, reward, terminated, _, info = client.step(_MISS)
            assert obs == env.step(_MISS)[0]
            assert reward == -1.0 and not terminated and info["accepted"]
            with pytest.raises(RuntimeError, match="held out"):
                client.reset(seed=0, options={"object_count": _VALIDATION})
            with pytest.raises(RuntimeError, match="strict"):
                client.get_state()
            path = client.render_state(state=obs, label="after_miss")
            assert (sandbox_dir / path).exists()
            frames = client.render_policy(seed=0, object_count=_CATAPULT)
            assert len(frames) == 2  # the reset and the one solving step
            assert all((sandbox_dir / p).exists() for p in frames)
