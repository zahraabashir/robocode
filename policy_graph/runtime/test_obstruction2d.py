"""Reference-oracle regression tests, kept separate from general recognition."""

# Fixtures execute the original source intentionally; test names describe cases.
# pylint: disable=exec-used,missing-function-docstring

import ast
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from policy_graph.runtime import RuntimeConfig, RuntimeSession, TraceLimit
from policy_graph.runtime.__main__ import main
from policy_graph.runtime.episode_config import load_episode_spec
from policy_graph.runtime.reference.obstruction2d import (
    Obstruction2DAdapter,
    Obstruction2DReferenceSession,
    movement_steps,
)

SOURCE = (Path(__file__).parent / "fixtures/obstruction2d_polyline.py.txt").read_text()


@pytest.fixture(name="policy_path")
def policy_path_fixture(tmp_path):
    path = tmp_path / "approach.py"
    path.write_text(SOURCE)
    return path


def constructor():
    np = pytest.importorskip("numpy")
    return (SimpleNamespace(low=np.full(5, -1.0), high=np.full(5, 1.0)), None, {})


def test_source_contract_is_not_name_recognition():
    assert Obstruction2DAdapter.matches(SOURCE)
    assert Obstruction2DAdapter.matches(ast.unparse(ast.parse(SOURCE)))
    assert Obstruction2DAdapter.matches(SOURCE + "\n# a comment\n")
    assert not Obstruction2DAdapter.matches(SOURCE.replace("return p\n", "return []\n"))
    assert not Obstruction2DAdapter.matches(
        SOURCE.replace("SPEED = 0.05", "SPEED = 0.5")
    )
    assert not Obstruction2DAdapter.matches("class GeneratedApproach: pass")
    assert not Obstruction2DAdapter.matches("not valid Python !")


def test_sampling_parameter_is_checked():
    assert Obstruction2DAdapter.matches(SOURCE.replace("L / 0.003", "L / 0.006"))
    assert not Obstruction2DAdapter.matches(SOURCE.replace("L / 0.003", "L / 0.0"))
    assert not Obstruction2DAdapter.matches(SOURCE.replace("L / 0.003", "L / -0.003"))


def test_nominal_horizon_counts_movements_and_arm_motion():
    # Four grid moves, each exactly one nominal action at SPEED=.05.
    path = [(0, 0), (0, 0.05), (0.05, 0.05), (0.1, 0.05), (0.1, 0)]
    assert movement_steps(path) == 4
    assert movement_steps([(0, 0, 0.1), (0.05, 0, 0.4)]) == 3
    assert movement_steps([(0, 0), (0, 0)]) == 0


def run_path_search(path, *, blocked=False):
    with Obstruction2DReferenceSession(path) as session:
        session.load(constructor_args=constructor())
        session.policy.robot = {"r": 0.05, "gh": 0.02, "gw": 0.02, "arm_max": 0.2}
        obstacles = (
            [{"name": "wall", "x": 0, "y": 0, "w": 2, "h": 2}] if blocked else []
        )
        chosen = session.call(
            "_plan_path",
            (0.3, 0.5, 0.2),
            (0.7, 0.5, 0.2),
            obstacles,
            None,
            state_args=(),
            action=False,
        )
    return chosen, session.report()


def test_denser_collision_sampling_changes_work_not_horizon(policy_path):
    coarse_path, coarse = run_path_search(policy_path)
    policy_path.write_text(SOURCE.replace("L / 0.003", "L / 0.0015"))
    fine_path, fine = run_path_search(policy_path)
    assert fine_path == coarse_path
    a, b = coarse["planning_events"][0], fine["planning_events"][0]
    assert a["selected_path_horizon"] == b["selected_path_horizon"] == 8
    assert a["max_candidate_horizon"] == b["max_candidate_horizon"]
    assert (
        a["counts"]["candidate_paths_scored"] == b["counts"]["candidate_paths_scored"]
    )
    assert b["counts"]["collision_sample_rows"] > a["counts"]["collision_sample_rows"]
    assert not a["action_relevant"] and not coarse["actions"]
    assert coarse["status"] == "not_evaluated"


def test_fallback_path_is_not_marked_collision_validated(policy_path):
    path, result = run_path_search(policy_path, blocked=True)
    search = result["planning_events"][0]
    assert search["selection"] == "unchecked_fallback"
    assert not search["selected_path_validated"]
    assert search["selected_path_horizon"] == movement_steps(path)
    assert result["geometric_planning"]["performed"]["unchecked_fallback_paths"] == 1


@pytest.mark.parametrize("seed,count", [(0, 2), (1, 0), (2, 4)])
def test_live_episode_matches_original_actions_and_reuses_cache(
    policy_path, seed, count
):
    np = pytest.importorskip("numpy")
    pytest.importorskip("kinder")
    pytest.importorskip("hydra")
    spec = load_episode_spec(policy_path, env="obstruction2d_generalized")
    env = spec.make_env()
    original = {}
    exec(compile(SOURCE, str(policy_path), "exec"), original)
    plain = original["GeneratedApproach"](env.action_space, env.observation_space, {})
    try:
        state, info = env.reset(seed=seed, options={"object_count": count})
        plain.reset(state, info)
        with Obstruction2DReferenceSession(
            policy_path, RuntimeConfig(max_events=1000)
        ) as session:
            session.load(constructor_args=(env.action_space, env.observation_space, {}))
            session.call("reset", state, info)
            for _ in range(80):
                expected = plain.get_action(state)
                actual = session.call("get_action", state)
                np.testing.assert_array_equal(actual, expected)
                assert actual.dtype == expected.dtype
                assert session.policy.plan == plain.plan
                state, _, terminated, truncated, _ = env.step(actual)
                if terminated or truncated:
                    break
        result = session.report(include_graph=True)
    finally:
        env.close()
    json.dumps(result)
    assert result["incomplete"] is None and result["event_count"] < 1000
    assert result["verdict"] == "planning_observed"
    assert result["status"] == "partial"
    assert result["planning_depth"] is None  # Geometry is not rollout depth.
    assert result["geometric_planning"]["performed"]["candidate_paths_scored"] > 0
    first = result["actions"][0]
    second = result["actions"][1]
    assert first["geometric_planning"]["new"]["candidate_paths_scored"] > 0
    assert second["geometric_planning"]["new"]["candidate_paths_scored"] == 0
    assert second["inherited_planning_event_ids"] == first["planning_event_ids"]
    measured = result["geometric_planning"]["performed"]
    assert measured["candidate_paths_scored"] == sum(
        e["counts"]["candidate_paths_scored"] for e in result["planning_events"]
    )
    assert (
        sum(
            a["geometric_planning"]["associated"]["candidate_paths_scored"]
            for a in result["actions"]
        )
        > measured["candidate_paths_scored"]
    )
    assert all(
        p < e.id for e in session.recorder.graph.events for p in e.data + e.control
    )


def test_reset_does_not_reuse_old_plan_provenance(policy_path):
    pytest.importorskip("kinder")
    pytest.importorskip("hydra")
    env = load_episode_spec(policy_path, env="obstruction2d_generalized").make_env()
    try:
        state, info = env.reset(seed=0, options={"object_count": 2})
        with Obstruction2DReferenceSession(policy_path) as session:
            session.load(constructor_args=(env.action_space, env.observation_space, {}))
            for _ in range(2):
                session.call("reset", state, info)
                session.call("get_action", state)
        actions = session.report()["actions"]
        assert not set(actions[0]["planning_event_ids"]) & set(
            actions[1]["planning_event_ids"]
        )
        assert not actions[1]["inherited_planning_event_ids"]
    finally:
        env.close()


def test_adapter_remains_subject_to_event_limit(policy_path):
    pytest.importorskip("kinder")
    pytest.importorskip("hydra")
    env = load_episode_spec(policy_path, env="obstruction2d_generalized").make_env()
    session = Obstruction2DReferenceSession(policy_path, RuntimeConfig(max_events=5))
    try:
        with pytest.raises(TraceLimit):
            session.run_episode(env, seed=0, count=2, max_steps=2)
    finally:
        env.close()
    result = session.report()
    assert result["incomplete"] and result["status"] == "unknown"
    assert result["geometric_planning"]["counts_are_prefix_only"]


@pytest.mark.parametrize(
    "config",
    [
        RuntimeConfig(),
        RuntimeConfig(planners=("_plan_path",)),
    ],
)
def test_generic_tracing_can_be_requested(policy_path, config):
    with RuntimeSession(policy_path, config) as session:
        session.load(constructor_args=constructor())
        assert session.semantic_adapter is None
        assert "semantic_adapter" not in session.metadata


def test_cli_never_auto_selects_reference_adapter(tmp_path, monkeypatch, capsys):
    pytest.importorskip("kinder")
    pytest.importorskip("hydra")
    policy = tmp_path / "evidence/final/approach.py"
    policy.parent.mkdir(parents=True)
    policy.write_text(SOURCE)
    env_yaml = (
        Path(__file__).parents[2]
        / "experiments/conf/environment/obstruction2d_generalized.yaml"
    )
    import_yaml = "\n".join("  " + line for line in env_yaml.read_text().splitlines())
    (policy.parent.parent / "config.yaml").write_text(
        "environment:\n" + import_yaml + "\nmax_steps: 3\nprimitives: []\n"
    )
    output = tmp_path / "report.json"
    dot = tmp_path / "report.dot"
    config = tmp_path / "runtime.json"
    config.write_text('{"max_events": 1000}')
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "runtime",
            str(policy),
            "--seed",
            "0",
            "--object-count",
            "2",
            "--json",
            str(output),
            "--dot",
            str(dot),
            "--config",
            str(config),
        ],
    )
    exit_code = 0
    try:
        main()
    except SystemExit as exc:
        exit_code = exc.code
    result = json.loads(output.read_text())
    if exit_code:
        assert exit_code == 1
        assert "TraceLimit" in result["incomplete"]
    assert "semantic_adapter" not in result["metadata"]
    assert "geometric_planning" not in result
    assert "geometric-search" not in dot.read_text()
    stdout = capsys.readouterr().out
    assert "path searches:" not in stdout


def test_old_configs_cannot_restore_automatic_reference_dispatch():
    assert RuntimeConfig.from_dict({"semantic_adapters": False}) == RuntimeConfig()
    with pytest.raises(ValueError, match="removed"):
        RuntimeConfig.from_dict({"semantic_adapters": True})


def test_explicit_reference_refuses_unreviewed_source_and_mixed_contracts(policy_path):
    reference = Obstruction2DReferenceSession(policy_path)
    with pytest.raises(ValueError, match="does not match"):
        reference.source_transform("class GeneratedApproach: pass", policy_path)
    configured = Obstruction2DReferenceSession(
        policy_path, RuntimeConfig(planners=("some_planner",))
    )
    with pytest.raises(ValueError, match="cannot be mixed"):
        configured.source_transform(SOURCE, policy_path)
