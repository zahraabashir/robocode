"""CLI episodes use live observations, retain failures, and reuse saved settings."""

# Test names describe the cases; Gym methods retain their required signatures.
# pylint: disable=missing-function-docstring,unused-argument

import json
import sys
from pathlib import Path

import pytest

from policy_graph.runtime.__main__ import main
from policy_graph.runtime.episode_config import EpisodeSpec, load_episode_spec

EXAMPLES = Path(__file__).parent / "examples"


@pytest.fixture(name="episode")
def episode_fixture(tmp_path, monkeypatch):
    gym = pytest.importorskip("gymnasium")
    pytest.importorskip("omegaconf")
    pytest.importorskip("imageio")

    class LineEnv(gym.Env):
        """A live environment whose observation changes after each action."""

        action_space = gym.spaces.Discrete(3, start=-1)
        observation_space = gym.spaces.Discrete(10)
        state = 3
        seed_used = None
        options_used = None
        closed = False

        def reset(self, *, seed=None, options=None):
            self.seed_used, self.options_used = seed, options
            self.state = 3
            return self.state, {}

        def step(self, action):
            self.state += action
            return self.state, 0.0, self.state == 0, False, {}

        def close(self):
            self.closed = True

    env = LineEnv()
    monkeypatch.setattr(EpisodeSpec, "make_env", lambda self: env)
    policy = tmp_path / "approach.py"
    policy.write_text((EXAMPLES / "cached_plan.py").read_text(encoding="utf-8"))
    return env, policy


def invoke(monkeypatch, policy, output, *options):
    monkeypatch.setattr(
        sys, "argv", ["runtime", str(policy), "--json", str(output), *options]
    )
    main()
    return json.loads(output.read_text())


def test_episode_cli_without_scenario(tmp_path, monkeypatch, episode):
    env, policy = episode
    result = invoke(
        monkeypatch,
        policy,
        tmp_path / "report.json",
        "--env",
        "small_maze",
        "--seed",
        "17",
        "--max-steps",
        "10",
    )
    assert env.closed and env.seed_used == 17 and env.state == 0
    assert len(result["actions"]) == 3
    assert result["metadata"]["episode_metrics"]["solved"]
    assert result["metadata"]["mode"] == "episode"
    assert (result["planning_depth"], result["planning_work"]) == (3, 6)


@pytest.mark.parametrize("layout", ["hydra", "archive", "explicit"])
def test_cli_reuses_saved_run_config(tmp_path, monkeypatch, episode, layout):
    env, original = episode
    if layout == "archive":
        policy = tmp_path / "evidence/final/approach.py"
        config = tmp_path / "evidence/config.yaml"
    else:
        policy = tmp_path / "run/sandbox/approach.py"
        config = tmp_path / (
            "run/.hydra/config.yaml" if layout == "hydra" else "saved.yaml"
        )
    policy.parent.mkdir(parents=True)
    policy.write_text(original.read_text())
    config.parent.mkdir(parents=True, exist_ok=True)
    config.write_text("""environment:
  _target_: robocode.environments.maze_env.MazeEnv
max_steps: 1
primitives: []
""")
    options = ["--run-config", str(config)] if layout == "explicit" else []
    result = invoke(monkeypatch, policy, tmp_path / "report.json", *options)
    assert env.closed and env.seed_used == 0 and env.state == 2
    assert len(result["actions"]) == 1
    assert result["metadata"]["max_steps"] == 1
    assert result["metadata"]["episode_config"] == str(config.resolve())


def test_episode_overrides_saved_limits_and_primitives(tmp_path):
    pytest.importorskip("omegaconf")
    config = tmp_path / "run.yaml"
    config.write_text("""environment:
  _target_: robocode.environments.maze_env.MazeEnv
  min_height: ${size}
size: 3
max_steps: 100
primitives: [BiRRT]
approach:
  blackbox: true
""")
    spec = load_episode_spec(
        tmp_path / "approach.py", run_config=config, max_steps=2, primitives=[]
    )
    assert spec.max_steps == 2 and not spec.primitive_names and spec.blackbox
    assert spec.environment["min_height"] == 3


def test_cli_scenario_still_works(tmp_path, monkeypatch):
    result = invoke(
        monkeypatch,
        EXAMPLES / "cached_plan.py",
        tmp_path / "report.json",
        "--scenario",
        str(EXAMPLES / "cached_plan.json"),
    )
    assert result["metadata"]["mode"] == "scenario"
    assert (result["planning_depth"], result["planning_work"]) == (3, 6)


def test_cli_policy_failure_preserves_partial_trace_and_closes_env(
    tmp_path, monkeypatch, episode
):
    env, policy = episode
    policy.write_text("""class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        pass
    def reset(self, state, info):
        pass
    def get_action(self, state):
        if state < 3:
            raise ValueError('fixture failure')
        return -1
""")
    output = tmp_path / "report.json"
    with pytest.raises(SystemExit) as exc:
        invoke(monkeypatch, policy, output, "--env", "small_maze")
    result = json.loads(output.read_text())
    assert exc.value.code == 1 and env.closed
    assert len(result["actions"]) == 1
    assert result["status"] == "unknown" and result["planning_depth"] is None
    assert "fixture failure" in result["incomplete"]
    assert result["metadata"]["mode"] == "episode"


def test_cli_missing_environment_explains_needed_option(tmp_path, monkeypatch, capsys):
    pytest.importorskip("omegaconf")
    policy = tmp_path / "approach.py"
    policy.write_text("class GeneratedApproach: pass\n")
    with pytest.raises(SystemExit) as exc:
        invoke(monkeypatch, policy, tmp_path / "report.json")
    assert exc.value.code == 1
    assert "Specify --env NAME" in capsys.readouterr().err
    assert json.loads((tmp_path / "report.json").read_text())["status"] == "unknown"


@pytest.mark.parametrize(
    "options",
    [
        ["--env", "small_maze", "--scenario", "calls.json"],
        ["--scenario", "calls.json", "--seed", "2"],
        ["--env", "small_maze", "--max-steps", "0"],
    ],
)
def test_cli_rejects_conflicting_or_invalid_options(tmp_path, monkeypatch, options):
    with pytest.raises(SystemExit) as exc:
        invoke(
            monkeypatch, tmp_path / "approach.py", tmp_path / "report.json", *options
        )
    assert exc.value.code == 2
