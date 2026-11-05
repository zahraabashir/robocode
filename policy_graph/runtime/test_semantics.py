"""General role contracts, independent breadth/work, and honest unknowns."""

# pylint: disable=missing-function-docstring

from dataclasses import asdict

import pytest

from policy_graph.runtime import AssessmentContract, RuntimeConfig, RuntimeSession
from policy_graph.runtime.semantics import candidate_key
from policy_graph.runtime.test_runtime import trace

ROUTE_CHECK = """
def feasible(route, blocked):
    for node in route:
        if node in blocked:
            return False
    return True
"""


def route_config(**kwargs):
    return RuntimeConfig(
        assessments={
            "feasible": AssessmentContract(
                horizon="sequence_edges",
                horizon_unit="graph edges",
                model_free=True,
            )
        },
        **kwargs,
    )


def test_one_route_has_roles_breadth_one_and_separate_horizon(tmp_path):
    result, _ = trace(
        tmp_path,
        ROUTE_CHECK + """
def get_action(obs):
    route = ["S", "B", "G"]
    return "B" if feasible(route, obs) else "WAIT"
""",
        calls=[("get_action", (["A"],))],
        config=route_config(),
    )
    assert result["verdict"] == "planning_observed"
    assert result["status"] == "partial"
    assert result["planning_depth"] is None
    episode = result["semantic_profile"]["episodes"][0]
    assert episode["role_chain_present"]
    assert all(episode["roles"].values())
    assert episode["interpretation_basis"] == ["declared assessment"]
    assert episode["measurements"]["breadth"]["value"] == 1
    assert episode["measurements"]["candidate_evaluations"]["value"] == 1
    horizon = episode["measurements"]["max_assessed_horizon"]
    assert (horizon["value"], horizon["unit"]) == (2, "graph edges")
    assert episode["measurements"]["model_depth"]["status"] == "not_applicable"


def test_repeated_route_checks_increase_work_not_breadth_and_keep_failures(tmp_path):
    result, _ = trace(
        tmp_path,
        ROUTE_CHECK + """
def get_action(obs):
    routes = [["S", "A", "G"], ["S", "A", "G"], ["S", "B", "C", "G"]]
    for route in routes:
        if feasible(route, obs):
            return route[1]
    return "WAIT"
""",
        calls=[("get_action", (["A", "B"],))],
        config=route_config(),
    )
    episode = result["semantic_profile"]["episodes"][0]
    assert episode["action_relevant"]
    assert episode["measurements"]["breadth"]["value"] == 2
    assert episode["measurements"]["candidate_evaluations"]["value"] == 3
    assert episode["measurements"]["max_assessed_horizon"]["value"] == 3


def test_unused_assessment_and_unexecuted_code_do_not_establish_decision(tmp_path):
    result, _ = trace(
        tmp_path,
        ROUTE_CHECK + """
def get_action(obs):
    unused = feasible(["S", "B", "G"], obs)
    if False:
        return "B" if feasible(["S", "B", "G"], obs) else "WAIT"
    return "WAIT"
""",
        calls=[("get_action", ([],))],
        config=route_config(),
    )
    assert result["semantic_profile"]["episodes"] == []
    assert result["verdict"] == "no_planning_observed"


def test_scalar_forms_have_same_breadth_and_heuristic_is_labeled(tmp_path):
    sources = [
        "def get_action(obs):\n"
        "    return min([-1, 0, 1], key=lambda a: abs(obs+a-10))\n",
        """
def get_action(obs):
    best = None
    chosen = 0
    for a in [-1, 0, 1]:
        score = abs(obs + a - 10)
        if best is None or score < best:
            best, chosen = score, a
    return chosen
""",
    ]
    for source in sources:
        result, _ = trace(tmp_path, source)
        episode = result["semantic_profile"]["episodes"][0]
        assert episode["role_chain_present"]
        assert episode["measurements"]["breadth"]["value"] == 3
        assert "arithmetic assumption" in episode["interpretation_basis"]


def test_duplicate_action_evaluation_is_work_not_new_alternative(tmp_path):
    result, _ = trace(
        tmp_path,
        """
def get_action(obs):
    return min([-1, -1, 1], key=lambda a: abs(obs + a - 10))
""",
    )
    metrics = result["semantic_profile"]["episodes"][0]["measurements"]
    assert metrics["breadth"]["value"] == 2
    assert metrics["candidate_evaluations"]["value"] == 3
    assert metrics["transition_work"]["value"] == 3


def test_candidate_identity_never_invokes_custom_methods():
    class Dangerous:
        """Unknown candidate representation with observable comparison hooks."""

        def __repr__(self):
            raise AssertionError("must not inspect arbitrary objects")

        def __eq__(self, other):
            raise AssertionError("must not compare arbitrary objects")

    assert candidate_key(Dangerous()) is None
    assert candidate_key(float("nan")) is None
    assert candidate_key(-0.0) == candidate_key(0.0)
    assert candidate_key(["S", "G"]) == candidate_key(["S", "G"])
    assert candidate_key(["S", "G"]) != candidate_key(("S", "G"))
    cyclic = []
    cyclic.append(cyclic)
    assert candidate_key(cyclic) is None


def test_contracts_round_trip_and_reject_untyped_horizons():
    cfg = route_config()
    assert RuntimeConfig.from_dict(asdict(cfg)) == cfg
    with pytest.raises(ValueError, match="together"):
        AssessmentContract(horizon="sequence_edges")
    with pytest.raises(ValueError, match="category"):
        AssessmentContract(category="unknown")


def test_limit_invalidates_semantic_measurements(tmp_path):
    path = tmp_path / "policy.py"
    path.write_text(
        "def get_action(obs):\n    return min([-1,1],key=lambda a: obs+a)\n"
    )
    session = RuntimeSession(path)
    with session:
        session.load()
        session.call("get_action", 3)
    session.recorder.graph.incomplete = "Stopped before episode finished"
    profile = session.report()["semantic_profile"]
    assert profile["declared_assessment_work"]["performed"] is None
    assert all(
        m["value"] is None
        for p in profile["episodes"]
        for m in p["measurements"].values()
    )


def test_cached_route_keeps_origin_and_does_not_repeat_work(tmp_path):
    result, _ = trace(
        tmp_path,
        ROUTE_CHECK + """
class GeneratedApproach:
    def reset(self, obs):
        route = ["S", "B", "G"]
        self.plan = ["B", "G"] if feasible(route, obs) else ["WAIT", "WAIT"]
    def get_action(self, obs):
        return self.plan.pop(0)
""",
        calls=[("reset", ([],)), ("get_action", ([],)), ("get_action", ([],))],
        config=route_config(),
    )
    profile = result["semantic_profile"]
    assert profile["declared_assessment_work"]["performed"] == 1
    assert profile["declared_assessment_work"]["action_relevant"] == 1
    assert profile["episodes"][0]["action_indices"] == [0, 1]
    assert [a["new_assessment_work"] for a in profile["actions"]] == [0, 0]
    assert (
        profile["actions"][0]["associated_assessment_ids"]
        == profile["actions"][1]["associated_assessment_ids"]
    )


def test_native_pure_assessor_preserves_candidates_and_keyword_binding(tmp_path):
    cfg = RuntimeConfig(
        assessments={
            "math.dist": AssessmentContract(candidate_kind="placement", candidate_arg=0)
        }
    )
    result, _ = trace(
        tmp_path,
        """
import math
def get_action(obs):
    candidates = [[0.0, 0.0], [2.0, 0.0]]
    chosen = min(candidates, key=lambda p: math.dist(p, obs))
    return chosen[0]
""",
        calls=[("get_action", ([1.9, 0.0],))],
        config=cfg,
    )
    assert not result["unknowns"]
    assert (
        result["semantic_profile"]["episodes"][0]["measurements"]["breadth"]["value"]
        == 2
    )
    cfg.assessments = {"feasible": AssessmentContract(candidate_arg="route")}
    result, _ = trace(
        tmp_path,
        ROUTE_CHECK + """
def get_action(obs):
    return "B" if feasible(blocked=obs, route=["S", "B", "G"]) else "WAIT"
""",
        calls=[("get_action", ([],))],
        config=cfg,
    )
    assert result["verdict"] == "planning_observed"


def test_discarded_decision_counts_performed_but_not_action_work(tmp_path):
    result, _ = trace(
        tmp_path,
        ROUTE_CHECK + """
def get_action(obs):
    discarded = "B" if feasible(["S", "B", "G"], obs) else "WAIT"
    return "STAY"
""",
        calls=[("get_action", ([],))],
        config=route_config(),
    )
    work = result["semantic_profile"]["declared_assessment_work"]
    assert (work["performed"], work["action_relevant"]) == (1, 0)


def test_return_guard_survives_while_loop_without_leaking_from_nested_function(
    tmp_path,
):
    result, _ = trace(
        tmp_path,
        ROUTE_CHECK + """
def get_action(obs):
    i = 0
    while i < 2:
        if feasible(["S", "B", "G"], obs):
            return "B"
        i += 1
    return "WAIT"
""",
        calls=[("get_action", (["B"],))],
        config=route_config(),
    )
    assert result["planning_events"][0]["action_relevant"]
    result, _ = trace(
        tmp_path,
        ROUTE_CHECK + """
def get_action(obs):
    for i in range(2):
        if feasible(["S", "B", "G"], obs):
            def helper():
                return "B"
    return "WAIT"
""",
        calls=[("get_action", ([],))],
        config=route_config(),
    )
    assert not any(p["action_relevant"] for p in result["planning_events"])


def test_assessment_contract_does_not_hide_unmeasured_model_depth(tmp_path):
    result, _ = trace(
        tmp_path,
        """
def evaluate(action, obs):
    for _ in range(3):
        obs = obs * 2 + action
    return abs(obs - 10)
def get_action(obs):
    return min([-1, 1], key=lambda action: evaluate(action, obs))
""",
        config=RuntimeConfig(
            assessments={
                "evaluate": AssessmentContract(
                    candidate_kind="action", category="action_effect"
                )
            }
        ),
    )
    metrics = result["semantic_profile"]["episodes"][0]["measurements"]
    assert metrics["model_depth"]["value"] is None
    assert metrics["model_depth"]["status"] == "unknown"
    assert metrics["transition_work"]["status"] == "unknown"
    assert metrics["candidate_evaluations"]["value"] == 2
