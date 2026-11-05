"""Baseline recognition must be witnessed in the observed execution."""

# Fixture source preserves layout; test names describe the cases.
# pylint: disable=missing-function-docstring,line-too-long

from pathlib import Path

import pytest

from policy_graph.reactivity import analyze
from policy_graph.runtime import RuntimeSession, trace_episode
from policy_graph.runtime.episode_config import load_episode_spec
from policy_graph.runtime.recognition import Recognition
from policy_graph.runtime.test_runtime import trace

GRAPH = """
def search(obs):
    todo = [0]
    parent = {0: None}
    while todo:
        node = todo.pop(0)
        if node == obs:
            return node
        for successor in (node + 1,):
            if successor not in parent and successor <= obs:
                parent[successor] = node
                todo.append(successor)
    return -1
"""

ROUTES = """
def clear(path, blocked):
    for node in path:
        if node in blocked:
            return False
    return True

def search(obs):
    routes = [[0, 1, 3], [0, 2, 3]]
    for path in sorted(routes, key=len):
        if clear(path, obs):
            return path
    return [0, 0]
"""

TREE = """
def search(state, depth):
    if depth == 0:
        return abs(state)
    return min([search(state - 1, depth - 1), search(state + 1, depth - 1)])
"""


def recognized(result, rule):
    return [
        p
        for p in result["planning_events"]
        if (p.get("recognition") or {}).get("rule") == rule
    ]


def test_worklist_search(tmp_path):
    result, _ = trace(
        tmp_path, GRAPH + "\ndef get_action(obs):\n    return search(obs)\n"
    )
    assert result["verdict"] == "planning_observed"
    assert recognized(result, "graph-search")
    assert result["planning_depth"] is None


def test_ranked_route_search(tmp_path):
    result, _ = trace(
        tmp_path,
        ROUTES + "\ndef get_action(obs):\n    return search(obs)[1]\n",
        [("get_action", ([1],))],
    )
    assert recognized(result, "generate-and-test")
    assert result["verdict"] == "planning_observed"


def test_recursive_search(tmp_path):
    result, _ = trace(
        tmp_path, TREE + "\ndef get_action(obs):\n    return search(obs, 2)\n"
    )
    assert recognized(result, "tree-search")


def test_recursive_base_case_is_not_search(tmp_path):
    result, _ = trace(
        tmp_path, TREE + "\ndef get_action(obs):\n    return search(obs, 0)\n"
    )
    assert not result["planning_events"]


def test_unexecuted_search(tmp_path):
    result, _ = trace(
        tmp_path,
        GRAPH
        + "\ndef get_action(obs):\n    if obs < 0:\n        return search(obs)\n    return 0\n",
    )
    assert not result["planning_events"]
    assert result["verdict"] == "no_planning_observed"


def test_discarded_search(tmp_path):
    result, _ = trace(
        tmp_path, GRAPH + "\ndef get_action(obs):\n    search(obs)\n    return 0\n"
    )
    assert recognized(result, "graph-search")
    assert not any(p["action_relevant"] for p in result["planning_events"])
    assert result["verdict"] == "no_planning_observed"


def test_ordering_search(tmp_path):
    result, _ = trace(
        tmp_path,
        """
import itertools
def get_action(obs):
    return min(itertools.permutations([1, 2, 3]), key=lambda p: abs(p[0] - obs))[0]
""",
    )
    assert recognized(result, "ordering-search")
    assert result["planning_depth"] is None


def test_cached_structural_search(tmp_path):
    result, _ = trace(
        tmp_path,
        ROUTES + """
class GeneratedApproach:
    def reset(self, obs):
        self.path = search(obs)
    def get_action(self, obs):
        return self.path[1]
""",
        [("reset", ([1],)), ("get_action", (0,)), ("get_action", (0,))],
    )
    assert recognized(result, "generate-and-test")
    assert all(a["inherited_planning_event_ids"] for a in result["actions"])


def test_empty_frontier(tmp_path):
    source = GRAPH.replace("todo = [0]", "todo = []")
    result, _ = trace(
        tmp_path, source + "\ndef get_action(obs):\n    return search(obs)\n"
    )
    assert not recognized(result, "graph-search")


def test_enumeration_without_assessment(tmp_path):
    result, _ = trace(
        tmp_path,
        """
import itertools
def get_action(obs):
    orders = list(itertools.permutations([1, 2, 3]))
    return orders[0][0]
""",
    )
    assert not result["planning_events"]


def test_generator_is_lazy_and_keeps_outer_iterable(tmp_path):
    result, _ = trace(
        tmp_path,
        """
def get_action(obs):
    options = [-1, 0, 1]
    evaluated = ((abs(obs + a - 10), a) for a in options)
    options = [100]
    return min(evaluated)[1]
""",
    )
    assert result["planning_work"] == 3
    assert result["planning_depth"] == 1
    unused, _ = trace(
        tmp_path,
        """
def get_action(obs):
    unused = ((abs(obs + a - 10), a) for a in [-1, 0, 1])
    return 0
""",
    )
    assert unused["executed_prediction_updates"] == 0
    assert not unused["planning_events"]


def test_generator_suspension_does_not_change_bindings(tmp_path):
    result, _ = trace(
        tmp_path,
        """
def get_action(obs):
    a = 50
    values = (a + obs for a in [1, 2, 3])
    first = next(values)
    rest = list(values)
    return [first, rest, a]
""",
    )
    assert result["incomplete"] is None


def test_baseline_numpy_reducer_label_with_supported_counts(tmp_path):
    # np.argmin is a whole-value reduction (exact here), so the two scalar
    # transitions are counted; it used to be opaque and the counts unknown.
    # test_numpy covers partial reads, where counts must remain unknown.
    result, _ = trace(
        tmp_path,
        """
import numpy as np
def get_action(obs):
    costs = [(obs + a)**2 for a in [-1, 1]]
    return int(np.argmin(costs))
""",
    )
    assert result["verdict"] == "planning_observed"
    assert recognized(result, "lookahead")
    assert (result["planning_depth"], result["planning_work"]) == (1, 2)


TARGET = """
class GeneratedApproach:
    def reset(self, obs):
        self.targets = [obs - 2.0, obs + 3.0]

    def get_action(self, obs):
        best = min(self.targets, key=lambda t: abs(obs + t))
        return {returned}
"""


def test_target_choice_is_rejected_as_in_the_static_slice(tmp_path):
    """The chosen candidate reaches the action combined with the current state
    (tracking error), so the baseline's _encodes rule rejects the look-ahead."""
    result, session = trace(
        tmp_path,
        TARGET.format(returned="best - obs"),
        [("reset", (1.0,)), ("get_action", (1.5,))],
    )
    assert result["verdict"] == "no_planning_observed"
    assert not recognized(result, "lookahead")
    rejected = session.recorder.recognition.rejected
    assert [r["rule"] for r in rejected] == ["lookahead"]
    assert "_encodes" in rejected[0]["reason"]
    static = analyze([session.path])
    assert static.planning is False
    assert any(n.kind == "target-choice" for n in static.notes)


def test_encoded_choice_and_discarded_choice_keep_recognition(tmp_path):
    result, _ = trace(
        tmp_path,
        TARGET.format(returned="best"),
        [("reset", (1.0,)), ("get_action", (1.5,))],
    )
    assert result["verdict"] == "planning_observed"
    assert recognized(result, "lookahead")
    # Discarded work is still performed planning, not rejected by slice rules.
    result, _ = trace(
        tmp_path,
        TARGET.format(returned="0.0"),
        [("reset", (1.0,)), ("get_action", (1.5,))],
    )
    assert result["verdict"] == "no_planning_observed"
    assert recognized(result, "lookahead")
    assert not any(p["action_relevant"] for p in result["planning_events"])


CORPUS_POLICY = (
    Path(__file__).resolve().parents[2]
    / "agent_runs/environments/Obstruction3D/runs/codex_gpt56sol_r424_9332a06b"
    / "evidence/final/approach.py"
)


@pytest.mark.skipif(not CORPUS_POLICY.is_file(), reason="corpus not available")
def test_corpus_tracking_error_policy_is_not_planning():
    """The reported false positive: ``target - cur`` tracking error (line 130)."""
    pytest.importorskip("kinder")
    recognition = Recognition(CORPUS_POLICY)
    assert not recognition.evidence
    assert {(r["rule"], r["line"]) for r in recognition.rejected} >= {
        ("lookahead", 130)
    }
    spec = load_episode_spec(CORPUS_POLICY)
    env = spec.make_env()
    try:
        session = trace_episode(
            CORPUS_POLICY,
            env,
            seed=0,
            max_steps=40,
            primitives=spec.make_primitives(env),
        )
    finally:
        env.close()
    result = session.report()
    assert result["incomplete"] is None and len(result["actions"]) == 40
    assert result["verdict"] != "planning_observed"
    assert not result["planning_events"]


def test_unchecked_lookahead_cannot_alone_establish_relevance(tmp_path):
    """Outside the static action slice the target-choice rule was never applied:
    the decision counts as performed, but its relevance is unresolved."""
    path = tmp_path / "approach.py"
    path.write_text(TARGET.format(returned="best"))
    with RuntimeSession(path) as session:
        recognition = session.recorder.recognition
        recognition.unchecked = {id(e) for e in recognition.evidence}
        session.load()
        session.call("reset", 1.0)
        session.call("get_action", 1.5)
    result = session.report()
    assert result["verdict"] == "needs_review"
    assert result["planning_events"] and result["unchecked_rule_planning_event_ids"]
    assert not any(p["action_relevant"] for p in result["planning_events"])
    assert not result["precision"]["affects_scores"]


CLAMP_POLICY = (
    Path(__file__).resolve().parents[2]
    / "agent_runs/environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614"
    / "evidence/final/approach.py"
)


@pytest.mark.skipif(not CLAMP_POLICY.is_file(), reason="corpus not available")
def test_reset_classifier_does_not_judge_decision_time_code():
    """``_clip(tx - rx, 0.05)`` (tracking error) runs only from get_action; the
    reset classifier's reading of it as a look-ahead is not used."""
    recognition = Recognition(CLAMP_POLICY)
    assert not [e for e in recognition.evidence if e.kind == "lookahead"]
    assert any(
        r["line"] == 126 and "not executed by" in r["reason"]
        for r in recognition.rejected
    )
