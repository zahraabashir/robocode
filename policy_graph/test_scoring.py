"""Numerical examples and conservative failure cases, independent of corpus hand labels."""
import json
import textwrap

import pytest

from policy_graph.reactivity import PolicyConfig, analyze


def report(tmp_path, source, **kwargs):
    path = tmp_path / "policy.py"
    path.write_text(textwrap.dedent(source))
    return analyze([path], **kwargs)


def assert_scores(r, depth, work):
    assert (r.planning_depth, r.planning_work) == (depth, work), r.text()
    data = json.loads(json.dumps(r.to_dict()))
    assert (data["planning_depth"], data["planning_work"]) == (depth, work)
    assert data["scores"]["planning_depth"]["status"] == ("unknown" if depth is None else "exact")


@pytest.mark.parametrize("body", ["return -obs", "return min([-1, 1], key=lambda a: abs(a - 5))"])
def test_reactive_zero(tmp_path, body):
    r = report(tmp_path, "def get_action(obs):\n    " + body)
    assert r.verdict == "reactive"
    assert_scores(r, 0, 0)


@pytest.mark.parametrize("encoding", ["i", "2 * i - 1", "ACTIONS[i]", "int(i)"])
def test_action_encoding_does_not_add_depth_or_work(tmp_path, encoding):
    r = report(tmp_path, f"""
        import numpy as np
        ACTIONS = [-2, -1, 1, 2]
        def get_action(obs):
            costs = [(obs + a)**2 for a in ACTIONS]
            i = np.argmin(costs)
            return {encoding}
    """)
    assert r.verdict == "planning"
    assert_scores(r, 1, 4)


@pytest.mark.parametrize("horizon,candidates", [(1, 4), (5, 4), (9, 2)])
def test_rollout_depth_vs_work(tmp_path, horizon, candidates):
    r = report(tmp_path, f"""
        class Policy:
            def model(self, state, action):
                return state + action
            def get_action(self, obs):
                costs = {{}}
                for a in range({candidates}):
                    s = obs
                    for t in range({horizon}):
                        s = self.model(s, a)
                    costs[a] = abs(s)
                return min(costs, key=costs.get)
    """)
    assert r.verdict == "planning"
    assert_scores(r, horizon, horizon * candidates)


def test_lambda_key(tmp_path):
    r = report(tmp_path, """
        def get_action(obs):
            return min([-1, 1], key=lambda a: abs(obs + a))
    """)
    assert_scores(r, 1, 2)


def test_named_key_with_closure(tmp_path):
    r = report(tmp_path, """
        def get_action(obs):
            def score(a):
                return abs(obs + a)
            return min([-1, 1], key=score)
    """)
    assert_scores(r, 1, 2)


def test_shared_prefix_counted_once(tmp_path):
    r = report(tmp_path, """
        import numpy as np
        def get_action(obs):
            costs = []
            for a in [-1, 1]:
                s = obs + a
                for b in [-1, 1]:
                    future = s + b
                    costs.append(abs(future))
            return int(np.argmin(costs))
    """)
    assert r.verdict == "planning"
    assert_scores(r, 2, 6)  # 2 shared first steps + 4 second steps


def test_best_so_far_branch_only_selects(tmp_path):
    r = report(tmp_path, """
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
    """)
    assert_scores(r, 5, 10)


@pytest.mark.parametrize("source,reason", [
    ("""
        def get_action(obs, actions):
            return min(actions, key=lambda a: abs(obs + a))
    """, "count"),
    ("""
        def get_action(obs, horizon):
            best, choice = 1e9, 0
            for a in [-1, 1]:
                s = obs
                for t in range(horizon):
                    s += a
                if abs(s) < best:
                    best, choice = abs(s), a
            return choice
    """, "runtime"),
    ("""
        def get_action(obs):
            if obs > 0:
                return min([-1, 1], key=lambda a: abs(obs + a))
            return 0
    """, "branch"),
    ("""
        import networkx as nx
        def get_action(obs):
            return nx.shortest_path(obs['graph'], obs['start'], obs['goal'])[1]
    """, "planner-call"),
    ("""
        import networkx as nx
        class Policy:
            def reset(self, obs):
                self.plan = nx.shortest_path(obs['graph'], obs['start'], obs['goal'])
            def get_action(self, obs):
                return self.plan[1]
    """, "outside"),
    ("""
        import numpy as np
        def get_action(obs):
            costs = [(obs+a)**2 for a in range(1000000000)]
            return int(np.argmin(costs))
    """, "budget"),
])
def test_unknown_is_not_zero(tmp_path, source, reason):
    r = report(tmp_path, source)
    assert r.verdict == "planning"
    assert_scores(r, None, None)
    assert reason.lower() in r.scores.reason.lower()


def test_unresolved_has_no_numerical_claim(tmp_path):
    r = report(tmp_path, """
        from absent_policy_module import choose
        def get_action(obs):
            return choose(obs)
    """)
    assert r.verdict == "needs_review"
    assert_scores(r, None, None)


def test_configured_model_does_not_imply_one_time_step(tmp_path):
    r = report(tmp_path, """
        import simulator
        def get_action(obs):
            return min([-1, 1], key=lambda a: abs(simulator.predict(obs, a)))
    """, config=PolicyConfig(transition_models=("simulator.predict",), libraries=("simulator",)))
    assert r.verdict == "planning"
    assert_scores(r, None, None)


def test_discarded_predictions_do_not_count(tmp_path):
    r = report(tmp_path, """
        def get_action(obs):
            unused = [obs + a for a in [-3, -2, -1, 0, 1, 2, 3]]
            return min([-1, 1], key=lambda a: abs(obs + a))
    """)
    assert_scores(r, 1, 2)


def test_zero_loop_does_not_manufacture_positive_score(tmp_path):
    r = report(tmp_path, """
        import numpy as np
        def get_action(obs):
            costs = [(obs+a)**2 for a in range(0)]
            return int(np.argmin(costs))
    """)
    # Classifier can still find a syntactic witness; the scorer cannot validate a choice.
    assert r.verdict == "planning"
    assert_scores(r, None, None)


def test_reverse_operands_and_score_arithmetic(tmp_path):
    r = report(tmp_path, """
        def get_action(obs):
            return min([-1, 1], key=lambda a: abs(100 - (a + obs)) * 20)
    """)
    assert_scores(r, 1, 2)


def test_mutated_alias_cannot_give_a_false_fixed_count(tmp_path):
    r = report(tmp_path, """
        def get_action(obs):
            actions = [-1, 1]
            alias = actions
            alias.append(2)
            return min(actions, key=lambda a: abs(obs + a))
    """)
    assert r.verdict == "planning"
    assert_scores(r, None, None)


def test_lazy_filtered_candidates_cannot_give_a_false_fixed_count(tmp_path):
    r = report(tmp_path, """
        def get_action(obs):
            return min((a for a in [-1, 1] if obs > a), key=lambda a: abs(obs + a))
    """)
    assert_scores(r, None, None)


def test_shared_helper_with_discarded_call_is_not_overcounted(tmp_path):
    r = report(tmp_path, """
        class Policy:
            def predict(self, s, a):
                return s + a
            def get_action(self, obs):
                unused = [self.predict(obs, a) for a in [-3, -2, -1, 0, 1, 2, 3]]
                return min([-1, 1], key=lambda a: abs(self.predict(obs, a)))
    """)
    assert r.verdict == "planning"
    # Context-insensitive helper provenance is insufficient to claim an exact two.
    assert_scores(r, None, None)


def test_unresolved_alongside_planning_does_not_change_verdict(tmp_path):
    r = report(tmp_path, """
        from absent_policy_module import adjust
        def get_action(obs):
            action = min([-1, 1], key=lambda a: abs(obs + a))
            return adjust(action)
    """)
    assert r.verdict == "planning"
    assert_scores(r, None, None)


def test_corpus_scores_are_independent_of_hand_labels(tmp_path, monkeypatch, capsys):
    import policy_graph.run_corpus as corpus
    manifest = [{"run": "r1", "env": "test", "name": "example", "hand_label": "deliberately unverified"}]
    (tmp_path / "all_runs_verdicts.json").write_text(json.dumps(manifest))
    policy = tmp_path / "test/runs/r1/evidence/final/approach.py"
    policy.parent.mkdir(parents=True)
    policy.write_text("def get_action(obs):\n    return min([-1, 1], key=lambda a: abs(obs+a))\n")
    out = tmp_path / "scores.json"
    monkeypatch.setattr(corpus, "HERE", tmp_path)
    monkeypatch.setattr(corpus, "RUNS", tmp_path)
    monkeypatch.setattr("sys.argv", ["run_corpus", "--out", str(out)])
    corpus.main()
    row = json.loads(out.read_text())[0]
    assert (row["planning_depth"], row["planning_work"]) == (1, 2)
    assert row["hand_label"] == "deliberately unverified"
    assert row["scores"]["planning_work"]["unit"] == "hypothetical update evaluations"
    assert json.loads((tmp_path / "all_runs_verdicts.json").read_text()) == manifest
    assert "depth=1 work=2" in capsys.readouterr().out


def test_nested_helper_uses_local_horizon_not_shadowed_global(tmp_path):
    r = report(tmp_path, """
        HORIZON = 2
        def get_action(obs):
            HORIZON = 5
            def score(a):
                s = obs
                for _ in range(HORIZON):
                    s = s + a
                return abs(s)
            return min([-1, 1], key=score)
    """)
    assert_scores(r, 5, 10)


def test_return_branch_encoding_keeps_scores(tmp_path):
    r = report(tmp_path, """
        import numpy as np
        def get_action(obs):
            costs = [(obs + a)**2 for a in [-1, 1]]
            i = int(np.argmin(costs))
            if i == 0:
                return -1
            else:
                return 1
    """)
    assert_scores(r, 1, 2)
