"""NumPy indexing, updates, aliasing and precision, checked against ordinary Python.

The indexing forms are reduced from the 10 corpus crashes (unhashable slice or
array keys); fixtures are new code, not the policies themselves.
"""

# Fixture source preserves layout; test names describe the cases.
# pylint: disable=missing-function-docstring,line-too-long

import textwrap

import pytest

from policy_graph.runtime import RuntimeSession
from policy_graph.runtime.test_runtime import trace

np = pytest.importorskip("numpy")

CORPUS_INDEXING = {
    "slice_window_copy": """
        out = np.zeros_like(A); a, b = 1, -1
        out[1:3, 0:2] = A[1 - a:3 - a, 0 - b:2 - b]
        return out.tolist()""",
    "fancy_index_pair": """
        idx = np.asarray(np.arange(12).reshape(3, 4)); fi = np.array([0, 2, 1]); fj = np.array([1, 3, 0])
        ok = fi > 0
        return idx[fi[ok], fj[ok]].tolist()""",
    "broadcast_new_axes": """
        seg = A[:, 0]; free = A[:, 1] > 2
        same = (seg[:, None] == seg[None, :]) & free[:, None] & free[None, :]
        return same.tolist()""",
    "where_with_mask_axis": """
        alive = A[:, 0] > 3
        return np.where(alive[:, None], A * 2, A).tolist()""",
    "column_arithmetic": """
        return (np.abs(A[:, 0] - obs) - 0.5).tolist()""",
    "three_axis_broadcast": """
        boxes = np.column_stack((A[:, :2], A[:, 2:3]))
        d = np.abs(A[:, None, :2] - boxes[None, :, :2]) - boxes[None, :, 2:]
        return d.shape, float(d.sum())""",
    "column_stack_negated": """
        return np.column_stack((-A[:, 1], A[:, 0])).tolist()""",
    "column_update_from_itself": """
        T = A.copy(); s, c, c0 = 0.5, 0.25, A[:, 0]
        T[:, 1] = -s * c0 + c * T[:, 1]
        return T.tolist()""",
    "comprehension_of_views": """
        J = [A.reshape(3, 3, 1)[:, :, 0], A]
        return [M[:2, :2].copy().tolist() for M in J]""",
    "inplace_column_add": """
        a = np.zeros(4); B = np.eye(4); i = 2
        a += B[:, i] * obs
        a[3] = -1.0
        return a.tolist()""",
}


@pytest.mark.parametrize("name", sorted(CORPUS_INDEXING))
def test_corpus_indexing_forms_preserve_results(tmp_path, name):
    result, _ = trace(
        tmp_path,
        # As in the corpus, the array has been passed to a NumPy call first
        # (before the fix this gave it a heap entry, where tuple keys crashed).
        "import numpy as np\ndef get_action(obs):\n"
        "    A = np.asarray(np.arange(9.0).reshape(3, 3) * obs)\n"
        + textwrap.indent(textwrap.dedent(CORPUS_INDEXING[name]).strip(), "    ")
        + "\n",
        [("get_action", (2.0,))],
    )
    assert result["incomplete"] is None
    assert result["verdict"] == "no_planning_observed"
    assert result["unknown_count"] == 0


def depends_on_observation(session, index=-1, phase=None):
    """Whether action ``index`` depends on the observation of ``phase``."""
    graph = session.recorder.graph
    action = session.recorder.actions[index]
    phase = phase or graph.events[action].phase
    observations = {
        e.id for e in graph.events if e.kind == "observation" and e.phase == phase
    }
    return bool(observations & graph.backward_slice([action]))


VIEWS = """
import numpy as np
class GeneratedApproach:
    def reset(self, obs):
        self.grid = np.zeros((2, 3))
    def get_action(self, obs):
        {body}
        return float(self.grid.sum())
"""


@pytest.mark.parametrize(
    "body,depends",
    [
        ("view = self.grid[:, :2]\n        view[0, 1] = obs", True),
        ("self.grid[0].T[1:] += obs", True),
        ("alias = self.grid\n        alias *= 0\n        alias += obs", True),
        ("np.add(self.grid, obs, out=self.grid)", True),
        ("self.grid.reshape(-1).fill(obs)", True),
        ("np.copyto(self.grid[1], obs)", True),
        ("copy = self.grid[[0, 1]]\n        copy[0, 0] = obs", False),
        ("copy = self.grid.copy()\n        copy += obs", False),
        (
            "mask = self.grid > -1\n        self.grid[mask] = 1.0\n        unused = obs",
            False,
        ),
    ],
)
def test_views_aliases_and_writes_reach_later_reads(tmp_path, body, depends):
    _, session = trace(
        tmp_path,
        VIEWS.format(body=body),
        [("reset", (0.0,)), ("get_action", (3.0,)), ("get_action", (4.0,))],
    )
    assert depends_on_observation(session) is depends


def test_array_state_carries_dependencies_across_calls(tmp_path):
    result, session = trace(
        tmp_path,
        """
        import numpy as np
        class GeneratedApproach:
            def reset(self, obs):
                self.plan = np.zeros(3)
            def get_action(self, obs):
                if obs > 0:
                    self.plan[1] = obs
                if obs > 5:
                    self.plan[0] = 1.0
                return float(self.plan[1])
    """,
        [("reset", (0.0,)), ("get_action", (2.0,)), ("get_action", (-1.0,))],
    )
    assert result["incomplete"] is None
    # The second action reads a value written by the first call.
    assert depends_on_observation(session, -1, "get_action:0")
    graph = session.recorder.graph
    scope = graph.backward_slice([session.recorder.actions[-1]])
    untaken = [
        e.id
        for e in graph.events
        if e.kind == "condition"
        and e.phase == "get_action:1"
        and "obs > 5" in e.site.text
    ]
    # An untaken write still decides which contents survive.
    assert untaken and set(untaken) <= scope


def test_native_exceptions_and_truth_values_are_preserved(tmp_path):
    for expression, error in [
        ("np.arange(3)[5]", IndexError),
        ("np.ones(2) + np.ones(3)", ValueError),
        ("1 if np.ones(2) > 0 else 0", ValueError),
        ("[1, 2][0, 1]", TypeError),
        ("{}[(slice(1),)]", TypeError),
    ]:
        path = tmp_path / "policy.py"
        path.write_text(
            f"import numpy as np\ndef get_action(obs):\n    return {expression}\n"
        )
        with RuntimeSession(path) as session:
            session.load()
            with pytest.raises(error):
                session.call("get_action", 1)


def test_inplace_operators_keep_aliases(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        import numpy as np
        def get_action(obs):
            s = {1}; t = s; s |= {obs}
            m = np.zeros(2, dtype=bool); n = m; m |= np.array([True, False])
            k = np.ones(2, dtype=int); j = k; k &= 0
            return sorted(t), n.tolist(), j.tolist()
    """,
    )
    assert result["incomplete"] is None


def test_partial_read_makes_relevance_possible_not_exact(tmp_path):
    source = """
        import numpy as np
        def get_action(obs):
            best = min([-1, 1], key=lambda a: abs(obs + a))
            values = np.array([obs * 2.0, best])
            return {read}
    """
    unrelated, _ = trace(tmp_path, source.format(read="float(values[0])"))
    assert unrelated["verdict"] == "needs_review"
    assert unrelated["planning_event_count"] == 0
    assert unrelated["possibly_relevant_planning_event_count"] == 1
    assert unrelated["precision"]["affects_scores"]
    assert unrelated["planning_depth"] is None
    assert unrelated["actions"][0]["possible_planning_event_ids"]
    whole, _ = trace(tmp_path, source.format(read="float(values.sum())"))
    assert whole["verdict"] == "planning_observed"
    assert (whole["planning_depth"], whole["planning_work"]) == (1, 2)


def test_whole_array_counts_are_unknown_when_they_could_overcount(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        import numpy as np
        def get_action(obs):
            near = [(obs + a) ** 2 for a in [-1, 1]]
            far = [(obs + b) ** 2 for b in [10, 20]]
            costs = np.array(near + far)
            return int(np.argmin(costs[:2]))
    """,
    )
    assert result["verdict"] == "planning_observed"
    event = next(p for p in result["planning_events"] if p["action_relevant"])
    assert (
        "Whole-array dependencies may include unrelated transitions" in event["reasons"]
    )
    # Four transitions are reachable through the whole array; two are relevant.
    assert len(event["transition_ids"]) == 4
    assert (event["depth"], event["work"], result["planning_work"]) == (
        None,
        None,
        None,
    )


def test_numpy_additive_pattern_is_unknown_not_a_transition(tmp_path):
    source = """
        import numpy as np
        def get_action(obs):
            state = {state}
            return min([-1.0, 1.0], key=lambda a: abs(state + a))
    """
    python, _ = trace(tmp_path, source.format(state="float(obs)"))
    assert (python["planning_depth"], python["planning_work"]) == (1, 2)
    numpy_typed, _ = trace(tmp_path, source.format(state="np.float64(obs)"))
    # The baseline look-ahead rule may still label it; it is never "no planning"
    # and no transition counts are claimed.
    assert numpy_typed["verdict"] != "no_planning_observed"
    assert numpy_typed["status"] == "unknown"
    assert numpy_typed["planning_depth"] is None
    assert numpy_typed["executed_prediction_updates"] == 0
    assert any("additive-transition" in r for r in numpy_typed["unknown_reasons"])


@pytest.mark.parametrize(
    "expression,reason",
    [
        ("float(np.random.default_rng(0).normal())", "Opaque call"),
        ("float(np.vectorize(lambda x: x + 1)(np.ones(2)).sum())", "Opaque call"),
        ("len(np.array([1, 2], dtype=object) + 1)", "Non-scalar arithmetic"),
    ],
)
def test_unsupported_numpy_stays_opaque(tmp_path, expression, reason):
    path = tmp_path / "policy.py"
    path.write_text(
        f"import numpy as np\ndef get_action(obs):\n    return {expression}\n"
    )
    with RuntimeSession(path) as session:
        session.load()
        session.call("get_action", 1)
    result = session.report()
    assert result["status"] == "unknown"
    assert any(reason in r for r in result["unknown_reasons"])


def test_iteration_and_unpacking_of_arrays_are_flagged(tmp_path):
    result, session = trace(
        tmp_path,
        """
        import numpy as np
        def get_action(obs):
            rows = np.arange(6.0).reshape(3, 2) * obs
            total = 0.0
            for x, y in rows:
                total += float(x) - float(y)
            first = [float(v) for v in rows[0]][0]
            return total + first + sum(rows.tolist()[1])
    """,
    )
    assert result["incomplete"] is None and result["unknown_count"] == 0
    flagged = [
        e for e in session.recorder.graph.events if e.detail.get("imprecise_parents")
    ]
    assert {e.detail.get("array") or e.detail.get("numpy") for e in flagged} >= {
        "iteration",
        "numpy.ndarray.tolist",
    }


def test_binding_decorators_are_traced(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        class GeneratedApproach:
            scale = 2
            @staticmethod
            def part(s, k):
                return s[k]
            @classmethod
            def scaled(cls, x):
                return x * cls.scale
            def get_action(self, obs):
                return min([-1, 1], key=lambda a: abs(self.part(obs, 0) + a)) + self.scaled(1)
    """,
        [("get_action", ([3],))],
    )
    assert result["unknown_count"] == 0
    assert (result["planning_depth"], result["planning_work"]) == (1, 2)


AUDITED = [
    """
    def get_action(obs):
        if obs > 0:
            if obs < 0:
                return 1
        for i in range(4):
            if i == obs:
                continue
            if i > 2:
                break
            while obs > 10:
                obs -= 1
                if obs == 12:
                    return 2
        return [x for x in range(3) if x != obs][0]
    """,
    """
    import numpy as np
    def get_action(obs):
        a = np.zeros(3)
        for i in range(3):
            if i == 1:
                a[i] = obs
            elif i == 7:
                return -1
        b, c = a[0], a[1]
        return float(b + c) if obs else 0.0
    """,
]


@pytest.mark.parametrize("source", AUDITED)
def test_innermost_controls_preserve_full_closures(tmp_path, source):
    """Events reference only the innermost entry of each control list."""
    path = tmp_path / "approach.py"
    path.write_text(textwrap.dedent(source))
    with RuntimeSession(path) as session:
        session.recorder.full_controls = {}
        session.load()
        for obs in (3, -2, 0):
            session.call("get_action", obs)
    graph, full = session.recorder.graph, session.recorder.full_controls
    closures = [0] * len(graph.events)
    reduced = [0] * len(graph.events)
    for event in graph.events:
        f = r = 1 << event.id
        for parent in event.data:
            f |= closures[parent]
            r |= reduced[parent]
        for parent in full.get(event.id, event.control):
            f |= closures[parent]
        for parent in event.control:
            r |= reduced[parent]
        closures[event.id], reduced[event.id] = f, r
    assert closures == reduced
    assert max(len(e.control) for e in graph.events) <= 4


def test_batched_candidates_abstain_instead_of_no_planning(tmp_path):
    """An array of candidate moves has no candidate marks; never claim absence."""
    result, _ = trace(
        tmp_path,
        """
        import numpy as np
        def get_action(obs):
            moves = np.array([-1, 0, 1])
            costs = np.abs(obs + moves - 10)
            return int(moves[np.argmin(costs)])
    """,
        [("get_action", (7,))],
    )
    assert result["verdict"] == "needs_review"
    assert result["planning_depth"] is None
    # A vector offset that is not added to state-derived values stays precise.
    result, _ = trace(
        tmp_path,
        """
        import numpy as np
        def get_action(obs):
            offset = np.array([0.5, -0.5])
            return (np.zeros(2) + offset).tolist()
    """,
        [("get_action", (7,))],
    )
    assert result["verdict"] == "no_planning_observed"


def test_shared_empty_event_detail_is_never_mutated(tmp_path):
    from policy_graph.runtime.graph import (  # pylint: disable=import-outside-toplevel
        EMPTY,
    )

    trace(
        tmp_path,
        """
        import numpy as np
        def helper(x):
            return x * 2
        def get_action(obs):
            return float((np.eye(3) * helper(obs))[0, 0])
    """,
    )
    assert not EMPTY
