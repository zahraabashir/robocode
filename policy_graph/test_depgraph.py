"""Graph properties behind the review findings, checked on the graph itself (not via a verdict).

    uv run --with pytest python -m pytest agent_runs/tools/policy_graph/test_depgraph.py
"""

import itertools
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from depgraph import build_graph  # noqa: E402

_ids = itertools.count()


def graph(tmp_path: Path, files, entry=None):
    d = tmp_path / f"g{next(_ids)}"
    if isinstance(files, str):
        files = {"m.py": files}
    for name, src in files.items():
        p = d / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(textwrap.dedent(src))
    return build_graph([d / e for e in (entry or [next(iter(files))])])


def node(g, kind, name=None, line=None, scope_end=None):
    hits = [n for n in g.nodes if n.kind == kind and (name is None or n.name == name)
            and (line is None or n.line == line) and (scope_end is None or n.scope.endswith(scope_end))]
    assert len(hits) == 1, hits
    return hits[0]


def lines_of(g, scope_end):
    return {n.line for n in g.nodes if n.scope.endswith(scope_end) and n.kind in ("def", "call", "op")}


# ---------------------------------------------------------------- finding 6: field identity

def test_same_named_classes_in_different_modules_have_separate_fields(tmp_path):
    g = graph(tmp_path, {"a.py": "class Policy:\n    def get_action(self, o):\n        return self.plan[0]\n",
                         "b.py": "class Policy:\n    def make(self, o):\n        self.plan = [o]\n"},
              ["a.py", "b.py"])
    fields = {n.name for n in g.nodes if n.kind == "field"}
    assert {"a.Policy.plan", "b.Policy.plan"} <= fields
    sl = g.backward_slice([g.functions["a.Policy.get_action"].return_node])
    assert not any(n.scope.startswith("b.") for n in sl)


def test_subclasses_share_the_root_class_field(tmp_path):
    g = graph(tmp_path, """
        class Base:
            def reset(self, o):
                self.goal = o
        class P(Base):
            def get_action(self, o):
                return self.goal
    """)
    sl = g.backward_slice([g.functions["m.P.get_action"].return_node])
    assert any(n.label() == "field:m.Base.goal" for n in sl) and any(n.label() == "param:reset.o" for n in sl)


# ---------------------------------------------------------------- finding 5: constants

def test_constant_requires_every_write_to_agree(tmp_path):
    g = graph(tmp_path, """
        class P:
            enabled = True
            depth = 0
            def __init__(self):
                self.mode = "react"
                self.margin = 0.1
                self.margin = 0.2
            def disable(self):
                self.enabled = False
    """)
    assert g.constant_fields == {"m.P.depth": 0, "m.P.mode": "react"}
    assert "m.P.enabled" in g.written_fields


def test_writes_through_other_objects_and_setattr(tmp_path):
    g = graph(tmp_path, """
        class P:
            def __init__(self):
                self.enabled = False
                self.k = 3
        p = P()
        p.enabled = True
    """)
    assert g.constant_fields == {"m.P.k": 3}
    g = graph(tmp_path, """
        class P:
            def __init__(self, name, value):
                self.enabled = False
                setattr(self, name, value)
    """)
    assert g.constant_fields == {}
    g = graph(tmp_path, """
        class P:
            def __init__(self):
                self.flag = True
                self.on = 1
    """)
    assert g.constant_fields["m.P.flag"] is True and g.constant_fields["m.P.on"] == 1


# ---------------------------------------------------------------- finding 7: termination and reachability

def test_nothing_after_unconditional_exits_is_analysed(tmp_path):
    g = graph(tmp_path, """
        def f(obs):
            return 0
            x = obs + 1
            return x
        def g2(obs):
            while False:
                y = obs + 2
            for _ in range(3):
                break
                z = obs + 3
            if obs:
                raise ValueError
                w = obs + 4
            return 1
    """)
    assert lines_of(g, ".f") == {3}  # only `return 0`
    assert not {7, 10, 13} & lines_of(g, ".g2")
    assert any(t == "while False" and part == "body" for _, _, t, part in g.pruned)


def test_while_true_exits_only_through_break(tmp_path):
    g = graph(tmp_path, """
        def f(obs):
            while True:
                if obs:
                    break
            a = obs + 1
            while True:
                pass
            b = obs + 2
            return a
    """)
    assert 6 in lines_of(g, ".f") and 9 not in lines_of(g, ".f")


def test_early_exit_adds_control_dependence(tmp_path):
    g = graph(tmp_path, """
        def f(obs, flag):
            if flag:
                return 0
            y = obs + 1
            for a in obs:
                if a < 0:
                    continue
                z = a * 2
            return y
    """)
    y = node(g, "def", "y")
    assert {u.label() for u, ks in g.preds[y].items() if "control" in ks} == {"param:f.flag"}
    z = node(g, "def", "z")
    a_defs = {u for u, ks in g.preds[z].items() if "control" in ks and u.name == "a"}
    assert a_defs, dict(g.preds[z])


# ---------------------------------------------------------------- finding 9: control dependence of mutations

def test_conditional_mutation_depends_on_its_condition(tmp_path):
    g = graph(tmp_path, """
        def f(obs, cond):
            out = [0]
            if cond > obs:
                out.append(1)
            return out[-1]
    """)
    weak = node(g, "def", "out", line=5)
    ctrl = {u.label() for u, ks in g.preds[weak].items() if "control" in ks}
    assert {"param:f.cond", "param:f.obs"} <= ctrl
    assert any(n.label() == "param:f.cond" for n in g.backward_slice([g.functions["m.f"].return_node]))


def test_branch_selected_value_depends_on_predicate(tmp_path):
    g = graph(tmp_path, """
        def f(pred):
            if pred == 0:
                score = 10
            else:
                score = 0
            return score
    """)
    for d in (n for n in g.nodes if n.name == "score"):
        assert any("control" in ks and u.label() == "param:f.pred" for u, ks in g.preds[d].items())


# ---------------------------------------------------------------- finding 3: copies across calls

def test_argument_binding_and_identity_helpers_copy(tmp_path):
    g = graph(tmp_path, """
        def identity(x):
            return x
        def f(obs):
            v = obs
            return identity(identity(v))
    """)
    v = node(g, "def", "v")
    x = node(g, "param", "x")
    assert (v, x) in g.copies
    ret = g.functions["m.f"].return_node
    assert v in g.copy_ancestors([ret])


def test_unpacked_tuple_elements_stay_apart(tmp_path):
    g = graph(tmp_path, """
        def pick(obs):
            return ("go", min(obs))
        def f(obs):
            name, target = pick(obs)
            return name
    """)
    sl = g.backward_slice([g.functions["m.f"].return_node])
    assert not any(n.kind == "call" and n.name == "min" for n in sl)


# ---------------------------------------------------------------- finding 4: function values and callbacks

def test_callable_alias_and_nested_function_resolve(tmp_path):
    g = graph(tmp_path, """
        def plan(obs):
            return obs
        def f(obs):
            planner = plan
            other = planner
            def helper(a):
                return a + obs
            return other(obs) + helper(1)
    """)
    assert {"m.plan", "m.f.helper"} <= g.call_graph["m.f"]
    assert all(cs.resolution == "project" for cs in g.functions["m.f"].call_sites.values())


def test_key_callback_receives_the_alternatives(tmp_path):
    g = graph(tmp_path, """
        def f(obs, xs):
            def score(a):
                return (obs + a) ** 2
            best = min(xs, key=score)
            also = min(xs, key=lambda b: (obs + b) ** 2)
            return best, also
    """)
    for q in ("m.f.score", next(q for q in g.functions if "<lambda" in q)):
        p = g.functions[q].param_nodes[g.functions[q].params[0]]
        assert any("iter" in ks and u.label() == "param:f.xs" for u, ks in g.preds[p].items()), q
        assert p in g.iter_vars
        mins = [n for n in g.nodes if n.kind == "call" and n.name == "min"]
        assert any(g.functions[q].return_node in g.preds[m] for m in mins)


def test_function_stored_in_a_field_resolves(tmp_path):
    g = graph(tmp_path, """
        class P:
            def get_action(self, obs):
                return self.scorer(obs)
            def __init__(self):
                self.scorer = self._score
            def _score(self, obs):
                return obs * 2
    """)
    assert "m.P._score" in g.call_graph["m.P.get_action"]


def test_unresolved_callback_is_recorded(tmp_path):
    g = graph(tmp_path, """
        def f(xs, scorer):
            return min(xs, key=scorer)
    """)
    assert list(g.unresolved_callbacks.values()) == ["scorer"]


def test_optimiser_objective_parameter_is_the_decision_variable(tmp_path):
    g = graph(tmp_path, """
        from scipy.optimize import minimize
        def f(obs):
            return minimize(lambda u: (obs + u) ** 2, [0.0]).x
    """)
    (dv,) = g.decision_vars
    assert dv.kind == "param" and dv.name == "u"


# ---------------------------------------------------------------- finding 11: imports and coverage

def test_relative_imports_use_package_context(tmp_path):
    files = {"pkg/__init__.py": "", "pkg/sub/__init__.py": "",
             "pkg/planner.py": "def choose(o):\n    return o\n",
             "pkg/sub/policy.py": ("from ..planner import choose\nfrom . import missing\nimport numpy\n"
                                   "import not_installed_anywhere\n"
                                   "def get_action(o):\n    return choose(o)\n")}
    g = graph(tmp_path, files, ["pkg/sub/policy.py"])
    assert {"pkg", "pkg.planner", "pkg.sub", "pkg.sub.policy"} <= set(g.modules)
    assert "pkg.planner.choose" in g.call_graph["pkg.sub.policy.get_action"]
    unresolved = {u[0] for u in g.unresolved_imports}
    assert ".missing" not in unresolved  # `from . import missing`: the package exists, the name may be in it
    assert "not_installed_anywhere" in unresolved and "numpy" not in unresolved


def test_missing_relative_module_and_call_resolution(tmp_path):
    files = {"pkg/__init__.py": "", "pkg/policy.py": ("from .gone import plan\nimport helperlib\n"
                                                      "def get_action(o):\n    return plan(o) + helperlib.f(o)\n")}
    g = graph(tmp_path, files, ["pkg/policy.py"])
    assert ".gone" in {u[0] for u in g.unresolved_imports}
    res = {cs.external: cs.resolution for cs in g.call_sites.values()}
    assert res["helperlib.f"] == "unresolved-import"
    assert res["pkg.gone.plan"] == "unresolved-import"  # a missing submodule of an analysed package


def test_method_resolution_by_name_stays_within_imported_modules(tmp_path):
    files = {"a.py": "def get_action(obj):\n    return obj.plan_route()\n",
             "b.py": "class Planner:\n    def plan_route(self):\n        return 1\n"}
    g = graph(tmp_path, files, ["a.py", "b.py"])
    (cs,) = g.functions["a.get_action"].call_sites.values()
    assert cs.resolution == "method" and cs.callee is None
    files["a.py"] = "import b\ndef get_action(obj):\n    return obj.plan_route()\n"
    g = graph(tmp_path, files, ["a.py", "b.py"])
    (cs,) = g.functions["a.get_action"].call_sites.values()
    assert cs.callee == "b.Planner.plan_route" and cs.by_name


# ---------------------------------------------------------------- additive operations and iteration

def test_additive_operations_keep_their_operands(tmp_path):
    g = graph(tmp_path, """
        def f(obs, acts):
            return [(obs + a) ** 2 for a in acts]
    """)
    (op,) = g.ops
    info = g.ops[op]
    assert {n.label() for n in info.left_copy} == {"param:f.obs"}
    (a,) = info.right
    assert a in g.iter_vars and any("iter" in ks for ks in g.preds[a].values())


def test_generator_yields_reach_the_consumer(tmp_path):
    g = graph(tmp_path, """
        def route(obs):
            return [obs + 1, obs + 2]
        class P:
            def _plan(self, obs):
                for wp in route(obs):
                    yield wp
                yield from self._tail(obs)
            def _tail(self, obs):
                yield obs * 0
            def get_action(self, obs):
                if not hasattr(self, "gen"):
                    self.gen = self._plan(obs)
                return next(self.gen)
    """)
    sl = g.backward_slice([g.functions["m.P.get_action"].return_node])
    assert {"m.route", "m.P._tail"} <= {n.scope for n in sl if n.kind == "return"}
