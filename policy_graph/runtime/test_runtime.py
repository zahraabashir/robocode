"""Behavioral fixtures, checked against ordinary Python and hand-counted updates."""

# Test names describe each fixture; source strings deliberately preserve layout.
# pylint: disable=missing-function-docstring,line-too-long,exec-used

import json
import sys
import textwrap

import pytest

from policy_graph.runtime import (
    RuntimeConfig,
    RuntimeSession,
    TraceLimit,
    TransitionContract,
    trace_episode,
)


def trace(
    tmp_path,
    source,
    calls=None,
    *,
    config=None,
    class_name=None,
    constructor_kwargs=None,
):
    path = tmp_path / "approach.py"
    path.write_text(textwrap.dedent(source))
    normal = {"__name__": "fixture"}
    exec(compile(path.read_text(), str(path), "exec"), normal)
    selected = class_name or (
        "GeneratedApproach" if "GeneratedApproach" in normal else None
    )
    normal_policy = normal[selected](**(constructor_kwargs or {})) if selected else None
    expected, actual = [], []
    with RuntimeSession(path, config) as session:
        session.load(class_name=class_name, constructor_kwargs=constructor_kwargs)
        for name, args in calls or [("get_action", (3,))]:
            fn = (
                getattr(normal_policy, name)
                if normal_policy is not None
                else normal[name]
            )
            expected.append(fn(*args))
            actual.append(session.call(name, *args))
    assert actual == expected
    result = session.report(include_graph=True)
    json.dumps(result)
    assert all(
        parent < event.id
        for event in session.recorder.graph.events
        for parent in event.data + event.control
    )
    return result, session


@pytest.mark.parametrize(
    "body",
    [
        "return -obs",
        "if False:\n    return min([-1, 1], key=lambda a: abs(obs + a))\nreturn 0",
        "enabled = False\nif enabled:\n    return min([-1, 1], key=lambda a: abs(obs + a))\nreturn 0",
        "if obs > 0:\n    if obs < 0:\n        return min([-1, 1], key=lambda a: abs(obs + a))\nreturn 0",
        "action = 0\nfor _ in range(0):\n    action = min([-1, 1], key=lambda a: abs(obs + a))\nreturn action",
        "return 0\nreturn min([-1, 1], key=lambda a: abs(obs + a))",
    ],
)
def test_unexecuted_and_reactive(tmp_path, body):
    result, _ = trace(
        tmp_path, "def get_action(obs):\n" + textwrap.indent(body, "    ")
    )
    assert (result["planning_depth"], result["planning_work"]) == (0, 0)
    assert result["executed_prediction_updates"] == 0


def test_runtime_branches(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            if obs > 0:
                return min([-1, 1], key=lambda a: abs(obs + a))
            return 0
    """,
        [("get_action", (3,)), ("get_action", (-3,))],
    )
    assert [a["planning_depth"] for a in result["actions"]] == [1, 0]
    assert result["planning_work"] == 2


@pytest.mark.parametrize("horizon,candidates", [(1, 4), (5, 4), (9, 2)])
def test_rollouts(tmp_path, horizon, candidates):
    result, _ = trace(
        tmp_path,
        f"""
        def model(state, action):
            return state + action
        def get_action(obs):
            costs = {{}}
            for a in range({candidates}):
                s = obs
                for t in range({horizon}):
                    s = model(s, a)
                costs[a] = abs(s)
            return min(costs, key=costs.get)
    """,
    )
    assert (result["planning_depth"], result["planning_work"]) == (
        horizon,
        horizon * candidates,
    )


def test_shared_prefix(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            costs = []
            for a in [-1, 1]:
                s = obs + a
                for b in [-1, 1]:
                    future = s + b
                    costs.append(abs(future))
            return min(range(len(costs)), key=costs.__getitem__)
    """,
    )
    assert (result["planning_depth"], result["planning_work"]) == (2, 6)


def test_best_so_far_including_rejected_candidate(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            best, choice = 1e9, 0
            for a in [-1, 1]:
                s = obs
                for t in range(5):
                    s += a
                cost = abs(s)
                if cost < best:
                    best, choice = cost, a
            return choice
    """,
    )
    assert (result["planning_depth"], result["planning_work"]) == (5, 10)


def test_overwritten_result(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            action = min([-1, 1], key=lambda a: abs(obs + a))
            action = 0
            return action
    """,
    )
    assert (result["planning_depth"], result["planning_work"]) == (0, 0)
    assert result["executed_prediction_updates"] == 2
    assert not result["planning_events"][0]["action_relevant"]
    assert result["performed_planning_work"] == 2
    assert result["calls"][-1]["performed_planning_work"] == 2


def test_cached_plan(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        class GeneratedApproach:
            def __init__(self):
                self.plan = []
            def reset(self, state, info):
                candidates = [[-1, -1, -1], [1, 1, 1]]
                def score(plan):
                    predicted = state
                    for action in plan:
                        predicted += action
                    return abs(predicted)
                self.plan = list(min(candidates, key=score))
            def get_action(self, state):
                return self.plan.pop(0)
    """,
        [
            ("reset", (3, {})),
            ("get_action", (3,)),
            ("get_action", (2,)),
            ("get_action", (1,)),
        ],
    )
    assert (result["planning_depth"], result["planning_work"]) == (3, 6)
    assert [a["new_planning_work"] for a in result["actions"]] == [0, 0, 0]
    ids = [a["planning_event_ids"] for a in result["actions"]]
    assert ids[0] and ids[0] == ids[1] == ids[2]


def test_alias_and_overwrite_item(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            xs = [min([-1, 1], key=lambda a: abs(obs + a))]
            alias = xs
            alias[0] = 0
            return xs[0]
    """,
    )
    assert result["planning_work"] == 0


def test_unselected_container_element(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            xs = [min([-1, 1], key=lambda a: abs(obs + a)), 0]
            return xs[1]
    """,
    )
    assert result["planning_work"] == 0


def test_comprehension_and_lambda(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            a = 99
            costs = [abs(obs + a) for a in [-1, 1]]
            winner = min(range(len(costs)), key=lambda i: costs[i])
            return [-1, 1][winner] + a - 99
    """,
    )
    assert (result["planning_depth"], result["planning_work"]) == (1, 2)


def test_call_context_not_merged(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def choose(obs, enabled):
            if enabled:
                return min([-1, 1], key=lambda a: abs(obs + a))
            return 0
        def get_action(obs):
            discarded = choose(obs, True)
            return choose(obs, False)
    """,
    )
    assert result["planning_work"] == 0
    assert result["executed_prediction_updates"] == 2


def test_declared_model_non_additive_and_no_double_count(tmp_path):
    config = RuntimeConfig(transition_models={"model": TransitionContract()})
    result, _ = trace(
        tmp_path,
        """
        def model(s, a):
            return s * 2 + a
        def get_action(obs):
            def score(a):
                s = obs
                for _ in range(3):
                    s = model(s, a)
                return abs(s)
            return min([-1, 1], key=score)
    """,
        config=config,
    )
    assert (result["planning_depth"], result["planning_work"]) == (3, 6)


def test_model_tuple_output(tmp_path):
    config = RuntimeConfig(
        transition_models={"model": TransitionContract(output_index=0)}
    )
    result, _ = trace(
        tmp_path,
        """
        def model(s, a):
            return (s * 2 + a, False)
        def get_action(obs):
            def score(a):
                s, done = model(obs, a)
                s, done = model(s, a)
                return abs(s)
            return min([-1, 1], key=score)
    """,
        config=config,
    )
    assert (result["planning_depth"], result["planning_work"]) == (2, 4)


def test_opaque_call_unknown(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        import hashlib
        def get_action(obs):
            return hashlib.sha256(str(obs).encode()).digest()[0]
    """,
    )
    assert result["status"] == "unknown"
    assert result["planning_depth"] is None


def test_opaque_planner_unknown_depth(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def search(s):
            return [s, s + 1]
        def get_action(obs):
            return search(obs)[1]
    """,
        config=RuntimeConfig(planners=("search",)),
    )
    assert result["verdict"] == "planning_observed"
    assert result["planning_depth"] is None


def test_short_circuit_preserves_calls(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def explode():
            raise ValueError('must not run')
        def get_action(obs):
            if False and explode():
                return 7
            return 1 if 0 < obs < 10 else explode()
    """,
    )
    assert result["planning_work"] == 0


def test_trace_budget_incomplete(tmp_path):
    p = tmp_path / "policy.py"
    p.write_text(
        "def get_action(obs):\n    return min([-1,1], key=lambda a: abs(obs+a))\n"
    )
    session = RuntimeSession(p, RuntimeConfig(max_events=10))
    with pytest.raises(TraceLimit), session:
        session.load()
        session.call("get_action", 3)
    assert session.report()["planning_depth"] is None


def test_sibling_import_and_cleanup(tmp_path):
    (tmp_path / "helper.py").write_text("def score(s, a):\n    return abs(s+a)\n")
    path = tmp_path / "approach.py"
    path.write_text(
        "from helper import score\ndef get_action(obs):\n    return min([-1,1], key=lambda a: score(obs,a))\n"
    )
    previous = sys.modules.get("helper")
    with RuntimeSession(path) as session:
        session.load()
        assert session.call("get_action", 3) == -1
    assert sys.modules.get("helper") is previous
    assert len(session.report()["source_hashes"]) == 2
    assert session.report()["planning_work"] == 2


def test_dot_slice(tmp_path):
    _, session = trace(
        tmp_path,
        "def get_action(obs):\n    return min([-1,1], key=lambda a: abs(obs+a))\n",
    )
    dot = session.recorder.graph.to_dot(session.recorder.actions)
    assert "digraph execution" in dot and "transition" in dot and "action" in dot


def test_non_taken_indexed_assignment_and_alias(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            out = [0]
            alias = out
            for a in [-1, 1]:
                future = obs + a
                if future < 0:
                    alias[0] = a
            return out[0]
    """,
    )
    assert (result["planning_depth"], result["planning_work"]) == (1, 2)


def test_while_break_continue_and_else(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            costs = {}
            for a in [-1, 1]:
                s = obs
                i = 0
                while i < 4:
                    i += 1
                    if i == 2:
                        continue
                    s += a
                else:
                    costs[a] = abs(s)
            return min(costs, key=costs.get)
    """,
    )
    assert (result["planning_depth"], result["planning_work"]) == (3, 6)


def test_list_iteration_observes_appends(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            xs = [0]
            for i, x in enumerate(xs):
                if i < 3:
                    xs.append(x + 1)
            return len(xs)
    """,
    )
    assert result["planning_work"] == 0


def test_sort_callback_observes_native_list_sort_semantics(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            xs = [3, 1, 2]
            seen = []
            def key(x):
                seen.append(len(xs))
                return x
            xs.sort(key=key)
            return seen
    """,
    )
    assert result["status"] == "unknown"


def test_fresh_observation_resets_depth(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        class GeneratedApproach:
            def get_action(self, obs):
                return min([-1,1], key=lambda a: abs(obs + a))
    """,
        [("get_action", (3,)), ("get_action", (2,))],
    )
    assert [a["planning_depth"] for a in result["actions"]] == [1, 1]
    assert result["planning_work"] == 4


def test_no_action_is_not_evaluated(tmp_path):
    path = tmp_path / "policy.py"
    path.write_text(
        "class GeneratedApproach:\n    def get_action(self, obs):\n        return obs\n"
    )
    with RuntimeSession(path) as session:
        session.load()
    assert session.report()["verdict"] == "not_evaluated"
    assert session.report()["planning_depth"] is None


@pytest.mark.parametrize("mutation", ["xs += xs", "xs.extend(xs)"])
def test_self_extending_list_preserves_execution(tmp_path, mutation):
    result, _ = trace(
        tmp_path,
        f"""
        def get_action(obs):
            xs = [-1, 1]
            {mutation}
            return xs
    """,
    )
    assert result["planning_depth"] == 0


def test_overwritten_nested_container_and_length(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            xs = [min([-1,1], key=lambda a: abs(obs+a))]
            outer = [xs]
            xs[0] = 0
            return outer, len(xs)
    """,
    )
    assert result["executed_prediction_updates"] == 2
    assert result["planning_work"] == 0


def test_nested_mutation_contributes_to_return(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            xs = [0]
            outer = [xs]
            xs[0] = min([-1,1], key=lambda a: abs(obs+a))
            return outer
    """,
    )
    assert result["planning_work"] == 2


def test_fixed_container_length_excludes_values(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            xs = [min([-1,1], key=lambda a: abs(obs+a))]
            return len(xs)
    """,
    )
    assert result["planning_work"] == 0


def test_non_taken_append_controls_length(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            xs = []
            for a in [-1,1]:
                future = obs + a
                if future < 0:
                    xs.append(a)
            return len(xs)
    """,
    )
    assert (result["planning_depth"], result["planning_work"]) == (1, 2)


def test_generator_unpack_is_consumed_once(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            x, y = (v for v in [obs, 2])
            return x + y
    """,
    )
    assert result["status"] == "observed"
    assert result["verdict"] == "no_planning_observed"


def test_selected_callable_contributes_to_result(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def negative():
            return [-1]
        def positive():
            return [1]
        def get_action(obs):
            a = min([-1,1], key=lambda a: abs(obs+a))
            fn = negative if a < 0 else positive
            return fn()[0]
    """,
    )
    assert result["planning_work"] == 2


def test_cached_function_default_retains_planning(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        class GeneratedApproach:
            def reset(self, obs):
                self.action = lambda chosen=min([-1,1], key=lambda a: abs(obs+a)): chosen
            def get_action(self, obs):
                return self.action()
    """,
        [("reset", (3,)), ("get_action", (3,)), ("get_action", (2,))],
    )
    assert (result["planning_depth"], result["planning_work"]) == (1, 2)
    assert all(a["new_planning_work"] == 0 for a in result["actions"])
    assert [
        c["performed_planning_work"]
        for c in result["calls"]
        if c["phase"].startswith("get_action:")
    ] == [0, 0]


def test_nested_global_declaration_does_not_affect_outer_parameter(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        def get_action(obs):
            def unused():
                global obs
                return 0
            return min([-1,1], key=lambda a: abs(obs+a))
    """,
    )
    assert result["planning_work"] == 2


def test_computed_class_body_requires_review(tmp_path):
    result, _ = trace(
        tmp_path,
        """
        class GeneratedApproach:
            plan = min([1,2], key=lambda a: abs(3+a))
            def get_action(self, obs):
                return self.plan
    """,
    )
    assert result["status"] == "unknown"


@pytest.mark.parametrize("expression", ["-value", "value < 3"])
def test_custom_operator_requires_review(tmp_path, expression):
    result, _ = trace(
        tmp_path,
        f"""
        class Value:
            def __neg__(self):
                return -1
            def __lt__(self, other):
                return True
        def get_action(obs):
            value = Value()
            return {expression}
    """,
    )
    assert result["status"] == "unknown"


@pytest.mark.parametrize(
    "expression",
    [
        "list([1], [2])",
        "tuple([1], bad=True)",
        "sorted([2,1], bad=True)",
        "[].append(1, 2)",
        "{}.pop()",
        "{1:2}.get(1, 2, 3)",
    ],
)
def test_adapter_preserves_argument_errors(tmp_path, expression):
    path = tmp_path / "policy.py"
    path.write_text(f"def get_action(obs):\n    return {expression}\n")
    with pytest.raises(TypeError):
        eval(expression)
    with RuntimeSession(path) as session:
        session.load()
        with pytest.raises(TypeError):
            session.call("get_action", 3)
    assert session.report()["status"] == "unknown"


def test_nested_session_rejected_without_changing_import_hooks(tmp_path):
    path = tmp_path / "policy.py"
    path.write_text("def get_action(obs):\n    return 0\n")
    before = list(sys.meta_path)
    with RuntimeSession(path) as session:
        with pytest.raises(RuntimeError, match="another session"):
            with RuntimeSession(path):
                pass
        session.load()
        assert session.call("get_action", 3) == 0
    assert sys.meta_path == before
    assert session.report()["config"]["arithmetic_transitions"] is True


def test_real_robocode_lifecycle(tmp_path):
    gym = pytest.importorskip("gymnasium")
    pytest.importorskip("imageio")

    class LineEnv(gym.Env):
        """Minimal deterministic environment for the real episode adapter."""

        action_space = gym.spaces.Discrete(3, start=-1)
        observation_space = gym.spaces.Discrete(10)
        state = 3

        def reset(self, *, seed=None, options=None):  # pylint: disable=unused-argument
            self.state = 3
            return self.state, {}

        def step(self, action):
            self.state += action
            return self.state, 0.0, self.state == 0, False, {}

    path = tmp_path / "approach.py"
    path.write_text(textwrap.dedent("""
        class GeneratedApproach:
            def __init__(self, action_space, observation_space, primitives):
                self.plan = []
            def reset(self, state, info):
                def score(plan):
                    predicted = state
                    for a in plan:
                        predicted += a
                    return abs(predicted)
                self.plan = list(min([[-1,-1,-1], [1,1,1]], key=score))
            def get_action(self, state):
                return self.plan.pop(0)
            def update(self, state, reward, done, info):
                self.last = state
    """))
    session = trace_episode(path, LineEnv(), seed=7, max_steps=10)
    result = session.report()
    assert result["metadata"]["episode_metrics"]["solved"] is True
    assert (result["planning_depth"], result["planning_work"]) == (3, 6)
    assert len(result["actions"]) == 3
    assert len([c for c in result["calls"] if c["phase"].startswith("update:")]) == 3


@pytest.mark.parametrize(
    "body",
    [
        "try:\n        return min([-1, 1], key=lambda a: abs(obs + a))\n    except ValueError:\n        return 0",
        'with memoryview(b"x"):\n        return min([-1, 1], key=lambda a: abs(obs + a))',
    ],
)
def test_return_inside_unsupported_statement_is_unknown(tmp_path, body):
    """The value comes from uninstrumented code; it must not look like a constant."""
    result, _ = trace(tmp_path, "def get_action(obs):\n    " + body + "\n")
    assert result["verdict"] == "needs_review"
    assert result["status"] == "unknown"
    assert any("Unsupported statement" in u["reason"] for u in result["unknowns"])


def test_implicit_none_return_depends_on_controls(tmp_path):
    _, session = trace(
        tmp_path,
        """
        def choose(obs):
            if obs > 0:
                return 1
        def get_action(obs):
            return choose(obs)
    """,
        [("get_action", (-3,))],
    )
    graph = session.recorder.graph
    scope = graph.backward_slice(session.recorder.actions)
    assert any(e.kind == "condition" for e in map(graph.events.__getitem__, scope))


def test_writes_inside_unsupported_statement_are_unknown_later(tmp_path):
    """A plan cached by a try body is not a dependency-free constant later."""
    result, _ = trace(
        tmp_path,
        """
        class GeneratedApproach:
            def reset(self, obs):
                try:
                    self.plan = min([-1, 1], key=lambda a: abs(obs + a))
                except ValueError:
                    self.plan = 0
            def get_action(self, obs):
                return self.plan
    """,
        [("reset", (3,)), ("get_action", (3,))],
    )
    assert result["verdict"] == "needs_review"
    assert any(
        "Possible mutation in unsupported statement" in u["reason"]
        for u in result["unknowns"]
    )


def test_declared_pure_method_depends_on_its_receiver(tmp_path):
    from fractions import Fraction  # pylint: disable=import-outside-toplevel

    path = tmp_path / "approach.py"
    path.write_text("def get_action(obs):\n    return obs.limit_denominator(10)\n")
    config = RuntimeConfig(pure_functions=("fractions.Fraction.limit_denominator",))
    with RuntimeSession(path, config) as session:
        session.load()
        session.call("get_action", Fraction(1, 3))
    graph = session.recorder.graph
    scope = graph.backward_slice(session.recorder.actions)
    assert any(graph.events[i].kind == "observation" for i in scope)
    assert session.report()["unknown_count"] == 0
