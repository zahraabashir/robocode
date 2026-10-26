"""Tests: the extractor's core properties and reactive/planning verdicts on small policies.

    pytest agent_runs/tools/policy_graph/test_policy_graph.py
"""

import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from policy_graph.depgraph import build_graph  # noqa: E402
from policy_graph.is_reactive import as_module  # noqa: E402
from policy_graph.reactivity import classify, find_decision_function  # noqa: E402


def write(tmp_path: Path, name: str, src: str) -> Path:
    path = tmp_path / name
    path.write_text(textwrap.dedent(src))
    return path


def verdict(tmp_path: Path, src: str, extra: dict[str, str] | None = None):
    path = write(tmp_path, "policy.py", src)
    for name, text in (extra or {}).items():
        write(tmp_path, name, text)
    g = build_graph([path])
    return classify(g, find_decision_function(g))


CASES = sorted((Path(__file__).resolve().parent / "cases").glob("*.py"))


def expected_label(path: Path) -> str:
    """The ``# expect: reactive`` / ``# expect: planning`` line at the top of a case."""
    for line in path.read_text().splitlines():
        if line.startswith("# expect:"):
            return line.split(":", 1)[1].strip()
    pytest.skip(f"{path.name} has no '# expect: reactive|planning' line")


@pytest.mark.parametrize("path", CASES, ids=[c.stem for c in CASES])
def test_case_files(path, tmp_path):
    """Each file in cases/ states its expected verdict in a comment."""
    expected = expected_label(path)
    src = path.read_text()
    module = as_module(src)
    if module != src:  # a bare method: wrap it in a class first
        path = tmp_path / path.name
        path.write_text(module)
    g = build_graph([path])
    r = classify(g, find_decision_function(g))
    assert r.verdict == expected, r.text()


def kinds(report):
    return {e.kind for e in report.evidence}


# ------------------------------------------------------------------ extractor


def test_flow_sensitive_reuse_of_a_name(tmp_path):
    """Two assignments to the same name are different nodes."""
    path = write(tmp_path, "m.py", """
        def f(a, b):
            x = a
            y = x
            x = b
            return x
    """)
    g = build_graph([path])
    sl = g.backward_slice([g.functions["m.f"].return_node])
    names = {n.label() for n in sl}
    assert "param:f.b" in names and "param:f.a" not in names


def test_loop_carried_dependence(tmp_path):
    """A value updated in a loop depends on its own earlier value."""
    path = write(tmp_path, "m.py", """
        def f(xs):
            total = 0
            for x in xs:
                total = total + x
            return total
    """)
    g = build_graph([path])
    loop_def = next(n for n in g.nodes if n.name == "total" and n.line == 5)
    assert loop_def in g.backward_slice([loop_def])


def test_interprocedural_and_fields(tmp_path):
    """Arguments reach callee parameters; a helper's attribute write reaches the reader."""
    path = write(tmp_path, "m.py", """
        class P:
            def reset(self, obs):
                self.goal = self.pick(obs)
            def pick(self, obs):
                return obs * 2
            def get_action(self, obs):
                return self.goal
    """)
    g = build_graph([path])
    sl = g.backward_slice([g.functions["m.P.get_action"].return_node])
    labels = {n.label() for n in sl}
    assert {"field:m.P.goal", "param:reset.obs", "param:pick.obs"} <= labels  # fields are fully qualified


def test_follows_local_imports(tmp_path):
    write(tmp_path, "helper.py", "def double(v):\n    return 2 * v\n")
    path = write(tmp_path, "m.py", "from helper import double\n\ndef f(a):\n    return double(a)\n")
    g = build_graph([path])
    assert "helper" in g.modules
    assert any(n.label() == "param:double.v" for n in g.backward_slice([g.functions["m.f"].return_node]))


def test_constant_branch_is_pruned(tmp_path):
    path = write(tmp_path, "m.py", """
        class P:
            def __init__(self):
                self.depth = 0
            def get_action(self, obs):
                a = obs
                if self.depth > 0:
                    a = self.think(obs)
                return a
            def think(self, obs):
                return obs
    """)
    g = build_graph([path])
    assert g.pruned and g.pruned[0][3] == "body"
    assert "m.P.think" not in g.call_graph.get("m.P.get_action", set())


# ------------------------------------------------------------------ verdicts

RULES = """
class Policy:
    def get_action(self, obs):
        if obs["x"] > 0.5:
            return -1.0
        return 1.0 if obs["y"] > 0 else 0.0
"""

PHASES = """
class Policy:
    def reset(self, obs):
        self.phase = 0
    def get_action(self, obs):
        if self.phase == 0 and obs["near"]:
            self.phase = 1
        return 0.1 if self.phase == 0 else -0.1
"""

GREEDY = """
import numpy as np
class Policy:
    def get_action(self, obs):
        costs = [np.hypot(t[0] - obs["x"], t[1] - obs["y"]) for t in obs["targets"]]
        t = obs["targets"][int(np.argmin(costs))]
        return np.clip([t[0] - obs["x"], t[1] - obs["y"]], -1, 1)
"""

GREEDY_LOOP = """
class Policy:
    def get_action(self, obs):
        best, choice = 1e9, None
        for t in obs["targets"]:
            cost = abs(t - obs["pos"])
            if cost < best:
                best = cost
                choice = t
        return 0.1 * (choice - obs["pos"])
"""

BFS = """
from collections import deque
class Policy:
    def get_action(self, obs):
        frontier, seen = deque([obs["start"]]), {obs["start"]: None}
        while frontier:
            cur = frontier.popleft()
            for nxt in obs["graph"][cur]:
                if nxt not in seen:
                    seen[nxt] = cur
                    frontier.append(nxt)
        return seen
"""

ROLLOUT = """
class Policy:
    def model(self, state, action):
        return state + action
    def get_action(self, obs):
        best, choice = 1e9, None
        for a in (-1, 0, 1):
            s = obs
            for _ in range(5):
                s = self.model(s, a)
            if abs(s) < best:
                best, choice = abs(s), a
        return choice
"""

SUCCESSOR = """
class Block:
    def __init__(self, p):
        self.p = p
    def moved(self, d):
        return Block(self.p + d)
class Policy:
    def get_action(self, obs):
        b = Block(obs)
        options = [(abs(b.moved(d).p), d) for d in (-1, 1)]
        return min(options, key=lambda o: o[0])[1]
"""

STORED_PLAN = """
import itertools
class Policy:
    def reset(self, obs):
        self.plan = list(min(itertools.permutations(obs["tasks"]), key=lambda o: sum(o)))
    def get_action(self, obs):
        if obs["done"]:
            self.plan.pop(0)
        return self.plan[0]
"""


@pytest.mark.parametrize("src, planning", [
    (RULES, False),
    (PHASES, False),  # remembering a phase is memory, not planning
    (GREEDY, False),  # nearest target chosen, then the action computed from it
    (GREEDY_LOOP, False),
    (BFS, True),  # route search counts (rubric rule 1: task and motion planning both count)
    (ROLLOUT, True),
    (SUCCESSOR, True),
    (STORED_PLAN, True),  # search at reset whose result the step follows
])
def test_verdicts(tmp_path, src, planning):
    r = verdict(tmp_path, src)
    assert r.planning is planning, r.text()
    assert bool(r.evidence) is planning


def test_evidence_kinds(tmp_path):
    rollout = verdict(tmp_path, ROLLOUT)
    assert any(e.kind == "lookahead" and "multi-step rollout" in e.what for e in rollout.evidence), rollout.text()
    assert kinds(verdict(tmp_path, SUCCESSOR)) == {"lookahead"}  # the successor *predicts*, it is not proof alone
    assert kinds(verdict(tmp_path, STORED_PLAN)) == {"ordering-search"}
    assert kinds(verdict(tmp_path, BFS)) == {"graph-search"}


def test_one_step_lookahead_returns_the_chosen_action(tmp_path):
    r = verdict(tmp_path, """
        class Policy:
            def get_action(self, obs):
                return min((-1, 0, 1), key=lambda a: abs(self.goal - (obs + a)))
    """)
    assert r.planning and kinds(r) == {"lookahead"}, r.text()


def test_unpacked_tuple_keeps_elements_apart(tmp_path):
    """``name, target = pick()``: the action uses the name, not the chosen target."""
    r = verdict(tmp_path, """
        class Policy:
            def pick(self, obs):
                if obs["done"]:
                    return ("stop", None)
                return ("go", min(obs["targets"], key=lambda t: abs(t - obs["pos"])))
            def get_action(self, obs):
                name, target = self.pick(obs)
                return {"go": 1.0, "stop": 0.0}[name]
    """)
    assert not r.planning, r.text()


def test_recursion_search(tmp_path):
    r = verdict(tmp_path, """
        class Policy:
            def search(self, state, depth):
                if depth == 0:
                    return 0
                return max(self.search(state + a, depth - 1) for a in (-1, 1))
            def get_action(self, obs):
                return self.search(obs, 3)
    """)
    assert r.planning and "tree-search" in kinds(r), r.text()


def test_dead_lookahead_is_not_evidence(tmp_path):
    """Look-ahead disabled by a constant (like M = 0) is reported as pruned, not as planning."""
    r = verdict(tmp_path, """
        class Policy:
            def __init__(self):
                self.M = 0
            def model(self, s, a):
                return s + a
            def get_action(self, obs):
                best = -1 if obs > 0 else 1
                if self.M > 0:
                    s = obs
                    for _ in range(3):
                        s = self.model(s, best)
                    best = s
                return best
    """)
    assert not r.planning, r.text()
    assert r.pruned


def test_replanning_only_when_needed(tmp_path):
    r = verdict(tmp_path, """
        import itertools
        class Policy:
            def reset(self, obs):
                self.plan = []
            def get_action(self, obs):
                if not self.plan:
                    self.plan = list(min(itertools.permutations(obs["tasks"]), key=sum))
                return self.plan.pop(0)
    """)
    assert r.planning, r.text()


def test_nested_recursive_search_is_found(tmp_path):
    """A recursive helper defined inside another function (as in task_planner.visit)."""
    r = verdict(tmp_path, """
        class Policy:
            def reset(self, obs):
                best = {}
                def visit(at, done, cost):
                    best[done] = min(best.get(done, 1e9), cost)
                    for k in obs["tasks"]:
                        if k not in done:
                            visit(k, done | {k}, cost + abs(k - at))
                visit(0, frozenset(), 0)
                self.plan = best
            def get_action(self, obs):
                return self.plan
    """)
    assert r.planning and "tree-search" in kinds(r), r.text()


def test_lookup_reused_after_arithmetic_is_not_self_composition(tmp_path):
    """index -> position -> next position -> index again is not predicting from a prediction."""
    r = verdict(tmp_path, """
        import numpy as np
        class Policy:
            def nearest(self, p):
                return int(np.argmin(np.abs(self.points - p)))
            def reset(self, obs):
                self.points = np.arange(10.0)
            def get_action(self, obs):
                i = self.nearest(obs)
                q = np.clip(self.points[i] + 1, 0, 9)
                return self.nearest(q)
    """)
    assert r.planning is False, r.text()  # reusing a lookup helper is not prediction


def test_iterative_solver_is_not_planning(tmp_path):
    """An IK-style fixed-point iteration converges to one answer; nothing is compared."""
    r = verdict(tmp_path, """
        class Policy:
            def step(self, q, target):
                return q + 0.5 * (target - q)
            def get_action(self, obs):
                q = obs["joints"]
                for _ in range(20):
                    q = self.step(q, obs["target"])
                return q
    """)
    assert not r.planning, r.text()


def test_function_local_import(tmp_path):
    """`import itertools` inside a method still resolves (as in Obstruction2D Claude 444)."""
    r = verdict(tmp_path, """
        class Policy:
            def get_action(self, obs):
                import itertools
                orders = list(itertools.permutations(obs["tasks"]))
                best = None
                for order in orders:
                    c = sum(order)
                    if best is None or c < best[0]:
                        best = (c, order)
                return best[1]
    """)
    assert r.planning and "ordering-search" in kinds(r), r.text()
