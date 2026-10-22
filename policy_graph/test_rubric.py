"""Classification tests derived from the planning rubric (see reactivity.py), not from earlier outputs.

    uv run --with pytest python -m pytest agent_runs/tools/policy_graph/test_rubric.py

Expected verdicts: "planning", "reactive" (non-planning, supported) or "needs_review"
(non-planning label, but something unresolved could change it).

1. REVIEW_CASES: the 34 checks from the code review, with the label the rubric requires.
2. RUBRIC_CASES: independent policies for each rubric rule.
3. INVARIANT_PAIRS: behaviour-preserving rewrites that must not change the verdict.
4. Review status: unresolved code yields "needs_review", and configuration resolves it.
"""

import itertools
import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from depgraph import build_graph  # noqa: E402
from reactivity import EntrypointError, PolicyConfig, analyze, classify, find_decision_function  # noqa: E402

_ids = itertools.count()


def run(tmp_path: Path, files, entry=None, decision=None, config=None):
    """Write the source(s) to a fresh folder and classify. ``files`` is code or {path: code}."""
    d = tmp_path / f"case{next(_ids)}"
    if isinstance(files, str):
        files = {"policy.py": files}
    for name, src in files.items():
        p = d / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(textwrap.dedent(src))
    entry = entry or [next(iter(files))]
    return analyze([d / e for e in entry], decision, config)


# --------------------------------------------------------------------------- 1. review regression cases

ONE_STEP = "costs = [(obs + a)**2 for a in actions]"
REVIEW_CASES = {
    "reactive_control": ("""
        class Policy:
            def get_action(self, obs):
                return 1 if obs > 0 else 0
        """, "reactive"),
    "route_search": ("""
        import networkx as nx
        class Policy:
            def get_action(self, obs):
                path = nx.shortest_path(obs.graph, obs.position, obs.goal)
                return path[1]
        """, "planning"),
    "trajectory_optimizer": ("""
        from scipy.optimize import minimize
        class Policy:
            def get_action(self, obs):
                result = minimize(lambda actions: sum((obs + sum(actions[:i+1]))**2 for i in range(3)), [0, 0, 0])
                return result.x[0]
        """, "planning"),
    "reactive_logits": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                logits = [2 * obs[0] - obs[1], obs[1]]
                return np.argmax(logits)
        """, "reactive"),
    "one_step_direct": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                actions = [-1, 1]
                costs = [(obs + a)**2 for a in actions]
                return np.argmin(costs)
        """, "planning"),
    "one_step_encoded": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                actions = [-1, 1]
                costs = [(obs + a)**2 for a in actions]
                return 2 * np.argmin(costs) - 1
        """, "planning"),
    "one_step_identity": ("""
        import numpy as np
        def identity(x):
            return x
        class Policy:
            def get_action(self, obs):
                costs = [(obs + a)**2 for a in [-1, 1]]
                return identity(np.argmin(costs))
        """, "planning"),
    "one_step_key_lambda": ("""
        class Policy:
            def get_action(self, obs):
                return min([-1, 1], key=lambda a: (obs + a)**2)
        """, "planning"),
    "one_step_key_function": ("""
        class Policy:
            def get_action(self, obs):
                def score(a):
                    return (obs + a)**2
                return min([-1, 1], key=score)
        """, "planning"),
    "one_step_field_state": ("""
        import numpy as np
        class Policy:
            def observe(self, obs):
                self.obs = obs
            def get_action(self):
                costs = [(self.obs + a)**2 for a in [-1, 1]]
                return np.argmin(costs)
        """, "planning"),
    "index_nested": ("""
        class Policy:
            def get_action(self, obs):
                actions = [-1, 1]
                costs = [(obs + a)**2 for a in actions]
                return actions[costs.index(min(costs))]
        """, "planning"),
    "index_split": ("""
        class Policy:
            def get_action(self, obs):
                actions = [-1, 1]
                costs = [(obs + a)**2 for a in actions]
                best = min(costs)
                return actions[costs.index(best)]
        """, "planning"),
    "unreachable_after_return": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                return 0
                return np.argmin([(obs + a)**2 for a in [-1, 1]])
        """, "reactive"),
    "unreachable_while_false": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                while False:
                    return np.argmin([(obs + a)**2 for a in [-1, 1]])
                return 0
        """, "reactive"),
    "class_default_pruning": ("""
        import numpy as np
        class Policy:
            enabled = True
            def disable(self):
                self.enabled = False
            def get_action(self, obs):
                if self.enabled:
                    return np.argmin([(obs + a)**2 for a in [-1, 1]])
                return 0
        """, "planning"),
    "same_file_setting": ("""
        import numpy as np
        class Policy:
            def __init__(self):
                self.enabled = False
            def get_action(self, obs):
                if self.enabled:
                    return np.argmin([(obs + a)**2 for a in [-1, 1]])
                return 0
        p = Policy()
        p.enabled = True
        """, "planning"),
    "annotated_copy": ("""
        def clone(obs: dict) -> dict:
            return obs.copy()
        class Policy:
            def get_action(self, obs):
                return max(clone(obs)['left'], clone(obs)['right']) + 1
        """, "reactive"),
    "unannotated_copy": ("""
        def clone(obs):
            return obs.copy()
        class Policy:
            def get_action(self, obs):
                return max(clone(obs)['left'], clone(obs)['right']) + 1
        """, "reactive"),
    "composed_arithmetic": ("""
        def normalize(v):
            return v / 10
        class Policy:
            def get_action(self, obs):
                x = normalize(obs)
                y = normalize(x + 1)
                return max(y, obs) + 1
        """, "reactive"),
    "recursive_arithmetic": ("""
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        class Policy:
            def get_action(self, obs):
                return max(factorial(obs), obs) + 1
        """, "reactive"),
    "best_so_far": ("""
        class Policy:
            def get_action(self, obs):
                best = float('inf')
                action = 0
                for a in [-1, 1]:
                    cost = (obs + a)**2
                    if cost < best:
                        best = cost
                        action = a
                return action
        """, "planning"),
    "best_so_far_annotated": ("""
        class Policy:
            def get_action(self, obs):
                best = float('inf')
                action = 0
                for a in [-1, 1]:
                    cost = (obs + a)**2
                    if cost < best:
                        best: float = cost
                        action: int = a
                return action
        """, "planning"),
    "top_level_autodiscovery": ("""
        def get_action(obs):
            return 1 if obs > 0 else 0
        """, "reactive"),
    "indirect_callback": ("""
        def plan(obs):
            return min([-1, 1], key=lambda a: (obs + a)**2)
        class Policy:
            def get_action(self, obs):
                planner = plan
                return planner(obs)
        """, "planning"),
    "script_constant": ("""
        class Policy:
            def get_action(self, obs):
                return [0, 1, 0][obs]
        """, "reactive"),
    "discarded_plan": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                unused = np.argmin([(obs+a)**2 for a in [-1,1]])
                return 0
        """, "reactive"),
    "zero_horizon_enumeration": ("""
        import itertools
        class Policy:
            def get_action(self, obs):
                pairs = itertools.product(obs, repeat=2)
                largest = max(pairs, key=lambda p: p[0] + p[1])
                return largest[0] + largest[1]
        """, "reactive"),
    "branch_only_prediction": ("""
        def step(state: dict, a) -> dict:
            return {'x': state['x'] + a}
        class Policy:
            def get_action(self, obs):
                best = -1
                action = 0
                for a in [-1, 1]:
                    predicted = step(obs, a)
                    if predicted['x'] == 0:
                        score = 10
                    else:
                        score = 0
                    if score > best:
                        best = score
                        action = a
                return action * 2
        """, "planning"),
    "target_loop_false_choice": ("""
        class Policy:
            def get_action(self, obs):
                best = float('inf')
                action = 0
                for x in [-1, 1]:
                    distance = abs(obs - x)
                    if distance < best:
                        best = distance
                        target = x
                    action = 1 if target > obs else -1
                return action
        """, "reactive"),
    "nested_if_mutator": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                out = [0]
                if np.argmin([(obs+a)**2 for a in [-1,1]]):
                    out.append(1)
                return out[-1]
        """, "planning"),
}

MULTI_A = """
class Policy:
    def __init__(self):
        self.plan = [0]
    def get_action(self, obs):
        return self.plan[0]
"""
MULTI_B = """
import itertools
class Policy:
    def make_plan(self, obs):
        self.plan = min(itertools.permutations(obs), key=lambda p: sum(p))
"""
PKG = {"pkg/__init__.py": "\n",
       "pkg/planner.py": "def choose(obs):\n    return min([-1,1],key=lambda a:(obs+a)**2)\n",
       "pkg/policy.py": "from .planner import choose\nclass Policy:\n    def get_action(self,obs):\n        return choose(obs)\n"}
REVIEW_MULTI = {
    "same_name_class_alone": ({"multi/a.py": MULTI_A}, ["multi/a.py"], "a.Policy.get_action", "reactive"),
    "same_name_class_with_unrelated_module": ({"multi/a.py": MULTI_A, "multi/b.py": MULTI_B},
                                              ["multi/a.py", "multi/b.py"], "a.Policy.get_action", "reactive"),
    "relative_import_single_file": (PKG, ["pkg/policy.py"], "policy.Policy.get_action", "planning"),
    "relative_import_directory": (PKG, ["pkg"], "policy.Policy.get_action", "planning"),
}


@pytest.mark.parametrize("name", sorted(REVIEW_CASES))
def test_review_case(tmp_path, name):
    src, expected = REVIEW_CASES[name]
    r = run(tmp_path, src)
    assert r.verdict == expected, r.text()


@pytest.mark.parametrize("name", sorted(REVIEW_MULTI))
def test_review_multi_file_case(tmp_path, name):
    files, entry, decision, expected = REVIEW_MULTI[name]
    r = run(tmp_path, files, entry, decision)
    assert r.verdict == expected, r.text()


def test_review_evidence_is_specific(tmp_path):
    """The evidence names the rule and the prediction, not a generic pattern."""
    r = run(tmp_path, REVIEW_CASES["branch_only_prediction"][0])
    (e,) = r.evidence
    assert e.kind == "lookahead" and "state['x'] + a" in e.what and e.rule.startswith("evaluates")
    assert [s[0] for s in e.sites] == ["prediction", "choice", "action"]
    r = run(tmp_path, REVIEW_CASES["route_search"][0])
    assert [e.kind for e in r.evidence] == ["planner-call"] and "path" in r.evidence[0].influence
    r = run(tmp_path, REVIEW_CASES["discarded_plan"][0])
    assert any(n.kind == "not-action-relevant" for n in r.notes), r.text()
    r = run(tmp_path, REVIEW_CASES["unreachable_while_false"][0])
    assert any("while False" in p[2] for p in r.pruned)


# --------------------------------------------------------------------------- 2. independent rubric cases

RUBRIC_CASES = {
    # -- non-planning: rules, fixed scripts, rankings that predict nothing (rule 3, 5)
    "timed_script": ("""
        SCRIPT = [(0.1, 0.0), (0.1, 0.0), (0.0, 0.2), (-0.1, 0.0)]
        class Policy:
            def reset(self, obs):
                self.t = 0
            def get_action(self, obs):
                a = SCRIPT[self.t % len(SCRIPT)]
                self.t += 1
                return a
        """, "reactive"),
    "linear_action_scores": ("""
        import numpy as np
        class Policy:
            def __init__(self, W, b):
                self.W, self.b = W, b
            def get_action(self, obs):
                scores = [self.W[a] @ obs + self.b[a] for a in range(3)]
                return int(np.argmax(scores))
        """, "reactive"),
    "learned_q_network": ("""
        import numpy as np
        class Policy:
            def __init__(self, net):
                self.net = net
            def get_action(self, obs):
                return int(np.argmax(self.net(obs)))
        """, "reactive"),
    "present_state_heuristic_ranking": ("""
        import numpy as np
        MOVES = [np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1])]
        class Policy:
            def get_action(self, obs):
                direction = obs["goal"] - obs["pos"]
                return max(MOVES, key=lambda m: float(np.dot(m, direction)))
        """, "reactive"),
    # -- one-step look-ahead (rule 2)
    "predicted_move_ranking": ("""
        import numpy as np
        MOVES = [np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1])]
        class Policy:
            def get_action(self, obs):
                return min(MOVES, key=lambda m: float(np.linalg.norm(obs["pos"] + m - obs["goal"])))
        """, "planning"),
    "velocity_model_helper": ("""
        class Policy:
            dt = 0.1
            def predict_x(self, x, v, a):
                v2 = v + self.dt * a
                return x + self.dt * v2
            def get_action(self, obs):
                best, best_a = None, 0.0
                for a in (-1.0, 0.0, 1.0):
                    err = abs(self.predict_x(obs["x"], obs["v"], a) - obs["target"])
                    if best is None or err < best:
                        best, best_a = err, a
                return best_a
        """, "planning"),
    "continuous_one_step_optimisation": ("""
        from scipy.optimize import minimize_scalar
        class Policy:
            def get_action(self, obs):
                res = minimize_scalar(lambda u: (obs["x"] + 0.1 * u - obs["goal"]) ** 2 + 0.01 * u * u,
                                      bounds=(-1, 1), method="bounded")
                return res.x
        """, "planning"),
    "observation_stored_by_update": ("""
        class Policy:
            def update(self, obs):
                self.pos = obs["pos"]
                self.goal = obs["goal"]
            def act(self):
                return min((-1, 0, 1), key=lambda a: abs(self.goal - (self.pos + a)))
        """, "planning"),
    "observation_stored_rule": ("""
        class Policy:
            def update(self, obs):
                self.pos = obs["pos"]
                self.goal = obs["goal"]
            def act(self):
                return 1 if self.goal > self.pos else -1
        """, "reactive"),
    # -- multi-step rollout and task search (rules 1, 2)
    "shooting_mpc": ("""
        import numpy as np
        class Policy:
            def __init__(self):
                self.rng = np.random.default_rng(0)
            def dynamics(self, s, a):
                return s + 0.1 * a
            def get_action(self, obs):
                plans = [self.rng.uniform(-1, 1, size=5) for _ in range(32)]
                best_cost, best_plan = float("inf"), None
                for plan in plans:
                    s, cost = obs, 0.0
                    for a in plan:
                        s = self.dynamics(s, a)
                        cost += float(abs(s))
                    if cost < best_cost:
                        best_cost, best_plan = cost, plan
                return best_plan[0]
        """, "planning"),
    "task_bfs": ("""
        from collections import deque
        class Policy:
            def successors(self, state):
                done, pos = state
                return [(done | {t}, t) for t in self.tasks if t not in done]
            def get_action(self, obs):
                start = (frozenset(), obs["pos"])
                parent = {start: None}
                queue = deque([start])
                goal = None
                while queue:
                    state = queue.popleft()
                    if len(state[0]) == len(self.tasks):
                        goal = state
                        break
                    for nxt in self.successors(state):
                        if nxt not in parent:
                            parent[nxt] = state
                            queue.append(nxt)
                step = goal
                while parent.get(step) is not None and parent[parent[step]] is not None:
                    step = parent[step]
                return step[1] if step else None
        """, "planning"),
    "layered_reachability": ("""
        class Policy:
            def neighbours(self, cell):
                x, y = cell
                return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            def get_action(self, obs):
                layers = [{obs["start"]}]
                for t in range(20):
                    new = set()
                    for cell in layers[-1]:
                        for nb in self.neighbours(cell):
                            if nb not in obs["walls"]:
                                new.add(nb)
                    layers.append(new)
                    if obs["goal"] in new:
                        break
                return len(layers)
        """, "planning"),
    "tree_walk_without_selection": ("""
        class Policy:
            def total(self, node):
                return node["w"] + sum(self.total(c) for c in node["children"])
            def get_action(self, obs):
                return 1 if self.total(obs["tree"]) > 3 else 0
        """, "reactive"),
    # -- route / motion planning and trajectories (rules 1, 4, 7)
    "dijkstra_with_controller": ("""
        import numpy as np
        from scipy.sparse.csgraph import dijkstra
        class Policy:
            def reset(self, obs):
                self.graph = obs["graph"]
                self.points = obs["points"]
            def get_action(self, obs):
                start, goal = obs["node"], obs["goal_node"]
                dist, pred = dijkstra(self.graph, indices=start, return_predecessors=True)
                nxt = goal
                while pred[nxt] != start and pred[nxt] >= 0:
                    nxt = pred[nxt]
                return np.clip(self.points[nxt] - obs["pos"], -0.2, 0.2)
        """, "planning"),
    "hand_written_astar_cached": ("""
        import heapq
        import numpy as np
        class Policy:
            def plan(self, start, goal, blocked):
                frontier = [(0.0, start)]
                cost, parent = {start: 0.0}, {start: None}
                while frontier:
                    _, cur = heapq.heappop(frontier)
                    if cur == goal:
                        break
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nxt = (cur[0] + dx, cur[1] + dy)
                        if nxt in blocked:
                            continue
                        c = cost[cur] + 1.0
                        if c < cost.get(nxt, float("inf")):
                            cost[nxt], parent[nxt] = c, cur
                            heapq.heappush(frontier, (c + abs(goal[0] - nxt[0]) + abs(goal[1] - nxt[1]), nxt))
                path, node = [], goal
                while node is not None and node in parent:
                    path.append(node)
                    node = parent[node]
                return path[::-1]
            def get_action(self, obs):
                if not getattr(self, "waypoints", None):
                    self.waypoints = self.plan(obs["cell"], obs["goal"], obs["blocked"])
                target = np.array(self.waypoints[1] if len(self.waypoints) > 1 else obs["goal"])
                return np.clip(target - np.array(obs["cell"]), -1, 1)
        """, "planning"),
    "astar_in_bounded_for_loop": ("""
        import heapq
        class Policy:
            def astar(self, start, goal, blocked):
                openq, cost, parent = [(0, start)], {start: 0}, {}
                end = None
                for _ in range(10000):
                    if not openq:
                        break
                    g, k = heapq.heappop(openq)
                    if k == goal:
                        end = k
                        break
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nk = (k[0] + dx, k[1] + dy)
                        if nk in blocked:
                            continue
                        if g + 1 < cost.get(nk, 10 ** 9):
                            cost[nk], parent[nk] = g + 1, k
                            heapq.heappush(openq, (g + 1, nk))
                path = []
                while end is not None and end != start:
                    path.append(end)
                    end = parent[end]
                return path[::-1]
            def get_action(self, obs):
                if not getattr(self, "path", None):
                    self.path = self.astar(obs["cell"], obs["goal"], obs["blocked"])
                wp = self.path[0] if self.path else obs["cell"]
                return (wp[0] - obs["cell"][0], wp[1] - obs["cell"][1])
        """, "planning"),
    "vectorised_dp_route": ("""
        import numpy as np
        class Policy:
            def dp(self, free, j0, j1):
                n, m = free.shape
                costs, backs = [np.where(np.arange(m) == j0, 0.0, 1e9)], []
                for i in range(1, n):
                    prev = costs[-1]
                    new = np.full(m, 1e9)
                    parent = np.full(m, -1)
                    for d in (-1, 0, 1):
                        src = np.arange(max(0, -d), min(m, m - d))
                        dst = src + d
                        cand = prev[src] + 1.0
                        better = free[i, dst] & (cand < new[dst])
                        new[dst[better]] = cand[better]
                        parent[dst[better]] = src[better]
                    costs.append(new)
                    backs.append(parent)
                j, path = j1, [j1]
                for parent in reversed(backs):
                    j = int(parent[j])
                    path.append(j)
                return path[::-1]
            def get_action(self, obs):
                path = self.dp(obs["free"], obs["row"], obs["goal_row"])
                return np.sign(path[1] - obs["row"])
        """, "planning"),
    "bellman_ford_dict": ("""
        class Policy:
            def get_action(self, obs):
                dist, prev = {obs["start"]: 0.0}, {}
                for _ in range(len(obs["nodes"])):
                    for u, v, w in obs["edges"]:
                        if u in dist and dist[u] + w < dist.get(v, float("inf")):
                            dist[v] = dist[u] + w
                            prev[v] = u
                node = obs["goal"]
                while prev.get(node) != obs["start"]:
                    node = prev[node]
                return node
        """, "planning"),
    "grouped_argmin_is_not_relaxation": ("""
        class Policy:
            def get_action(self, obs):
                best, arg = {}, {}
                for i, o in enumerate(obs["objects"]):
                    k, s = o["kind"], abs(o["x"] - obs["x"])
                    if s < best.get(k, float("inf")):
                        best[k] = s
                        arg[k] = i
                return 1 if arg.get("rock", 0) > 2 else -1
        """, "reactive"),
    "generator_policy_with_route": ("""
        import networkx as nx
        class Policy:
            def _plan(self):
                path = nx.shortest_path(self.obs["graph"], self.obs["pos"], self.obs["goal"])
                for node in path[1:]:
                    yield ("move", node)
                yield ("stop", None)
            def get_action(self, obs):
                self.obs = obs
                if getattr(self, "gen", None) is None:
                    self.gen = self._plan()
                return next(self.gen)
        """, "planning"),
    "generator_script": ("""
        class Policy:
            def _script(self):
                for a in ("open", "lift", "close"):
                    yield a
            def get_action(self, obs):
                if getattr(self, "gen", None) is None:
                    self.gen = self._script()
                return next(self.gen, "noop")
        """, "reactive"),
    "generate_and_test_paths": ("""
        class Policy:
            def free(self, path, obstacles):
                for i in range(len(path) - 1):
                    (x0, y0), (x1, y1) = path[i], path[i + 1]
                    for k in range(11):
                        x, y = x0 + (x1 - x0) * k / 10, y0 + (y1 - y0) * k / 10
                        if any(abs(x - ox) < r and abs(y - oy) < r for ox, oy, r in obstacles):
                            return False
                return True
            def plan(self, a, b, obstacles):
                cands = [[a, b]]
                for h in (0.2, 0.4, 0.6, 0.8):
                    cands.append([a, (a[0], h), (b[0], h), b])
                ranked = sorted(cands, key=len)
                for p in ranked:
                    if self.free(p, obstacles):
                        return p
                return [a, b]
            def get_action(self, obs):
                path = self.plan(obs["pos"], obs["goal"], obs["obstacles"])
                return (path[1][0] - obs["pos"][0], path[1][1] - obs["pos"][1])
        """, "planning"),
    "first_free_object_is_not_generate_and_test": ("""
        class Policy:
            def is_free(self, o, objs):
                return not any(abs(o["x"] - q["x"]) < 0.1 for q in objs if q is not o)
            def pick(self, obs):
                for o in sorted(obs["objects"], key=lambda o: abs(o["x"] - obs["x"])):
                    if self.is_free(o, obs["objects"]):
                        return o
                return obs["objects"][0]
            def get_action(self, obs):
                return 1 if self.pick(obs)["x"] > obs["x"] else -1
        """, "reactive"),
    "controller_simulation_scores_targets": ("""
        class Policy:
            def simulate(self, y, y_goal, heights):
                steps = 0
                for h in heights:
                    dy = max(-0.1, min(0.1, max(y_goal, h) - y))
                    y += dy
                    steps += 1 + abs(dy)
                return steps
            def get_action(self, obs):
                best, spot = None, None
                for x in obs["spots"]:
                    cost = self.simulate(obs["y"], x, obs["heights"])
                    if best is None or cost < best:
                        best, spot = cost, x
                return max(-0.1, min(0.1, spot - obs["y"]))
        """, "planning"),
    "ik_per_candidate_is_not_a_rollout": ("""
        class Policy:
            def ik(self, q, target):
                for _ in range(50):
                    q = q + 0.5 * (target - q)
                return q
            def get_action(self, obs):
                best, choice = None, None
                for g in obs["grasps"]:
                    q = self.ik(obs["q"], g)
                    err = abs(q - g)
                    if best is None or err < best:
                        best, choice = err, q
                return choice - obs["q"]
        """, "reactive"),
    "ompl_motion_planner": ("""
        from ompl import base as ob
        from ompl import geometric as og
        class Policy:
            def get_action(self, obs):
                space = ob.RealVectorStateSpace(2)
                setup = og.SimpleSetup(space)
                setup.setStartAndGoalStates(obs["start"], obs["goal"])
                setup.solve(1.0)
                return setup.getSolutionPath().getState(1)
        """, "planning"),
    "planner_result_returned_directly": ("""
        import networkx as nx
        class Policy:
            def get_action(self, obs):
                return nx.astar_path(obs["graph"], obs["pos"], obs["goal"])
        """, "planning"),
    "route_planned_at_reset_and_followed": ("""
        import networkx as nx
        class Policy:
            def reset(self, obs):
                self.route = nx.dijkstra_path(obs["graph"], obs["pos"], obs["goal"])
                self.i = 0
            def get_action(self, obs):
                if self.i + 1 < len(self.route) and obs["pos"] == self.route[self.i + 1]:
                    self.i += 1
                nxt = self.route[min(self.i + 1, len(self.route) - 1)]
                return (nxt[0] - obs["pos"][0], nxt[1] - obs["pos"][1])
        """, "planning"),
    "discarded_route": ("""
        import networkx as nx
        class Policy:
            def __init__(self):
                self.log = []
            def get_action(self, obs):
                path = nx.shortest_path(obs["graph"], obs["pos"], obs["goal"])
                self.log.append(len(path))
                return 1 if obs["x"] > 0 else -1
        """, "reactive"),
    # -- scripts that invoke a planner (rule 5)
    "script_with_planner_phase": ("""
        import networkx as nx
        SCRIPT = ["open", "open", "close"]
        class Policy:
            def reset(self, obs):
                self.phase, self.t = "navigate", 0
            def get_action(self, obs):
                if self.phase == "navigate":
                    if obs["pos"] == obs["goal"]:
                        self.phase = "script"
                    else:
                        path = nx.astar_path(obs["graph"], obs["pos"], obs["goal"])
                        return ("move", path[1])
                cmd = SCRIPT[min(self.t, len(SCRIPT) - 1)]
                self.t += 1
                return (cmd, None)
        """, "planning"),
    "script_with_planner_switched_off": ("""
        import networkx as nx
        class Policy:
            def __init__(self):
                self.use_planner = False
            def get_action(self, obs):
                if self.use_planner:
                    return nx.astar_path(obs["graph"], obs["pos"], obs["goal"])[1]
                return obs["scripted"][obs["t"]]
        """, "reactive"),
    # -- ordinary computation that is not planning (rule 6)
    "deepcopy_and_compare": ("""
        import copy
        class State:
            def __init__(self, x):
                self.x = x
            def clone(self):
                return copy.deepcopy(self)
        class Policy:
            def get_action(self, obs):
                s = State(obs).clone()
                s.x = s.x * 2
                return max(s.x, obs) - 1
        """, "reactive"),
    "iterated_preprocessing": ("""
        import math
        def wrap(a):
            return (a + math.pi) % (2 * math.pi) - math.pi
        class Policy:
            def get_action(self, obs):
                e = wrap(wrap(obs["heading"]) - obs["target"])
                return max(-1.0, min(1.0, 2.0 * e))
        """, "reactive"),
    # -- unreachable code and settings (rules 8, 10)
    "after_break": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                for _ in range(1):
                    break
                    return int(np.argmin([(obs + a) ** 2 for a in (-1, 1)]))
                return 0
        """, "reactive"),
    "after_raise": ("""
        import numpy as np
        class Policy:
            def get_action(self, obs):
                if obs is None:
                    raise ValueError("no observation")
                    return int(np.argmin([(obs + a) ** 2 for a in (-1, 1)]))
                return 0
        """, "reactive"),
    "setting_with_one_value": ("""
        import numpy as np
        class Policy:
            def __init__(self):
                self.mode = "react"
            def get_action(self, obs):
                if self.mode == "plan":
                    return int(np.argmin([(obs + a) ** 2 for a in (-1, 1)]))
                return 0
        """, "reactive"),
    "setting_changed_by_a_method": ("""
        import numpy as np
        class Policy:
            def __init__(self):
                self.mode = "react"
            def enable_planning(self):
                self.mode = "plan"
            def get_action(self, obs):
                if self.mode == "plan":
                    return int(np.argmin([(obs + a) ** 2 for a in (-1, 1)]))
                return 0
        """, "planning"),
    "setting_changed_by_setattr": ("""
        import numpy as np
        class Policy:
            def __init__(self, **cfg):
                self.mode = "react"
                for k, v in cfg.items():
                    setattr(self, k, v)
            def get_action(self, obs):
                if self.mode == "plan":
                    return int(np.argmin([(obs + a) ** 2 for a in (-1, 1)]))
                return 0
        """, "planning"),
    # -- conditional rewards and conditional mutations (review finding 9)
    "collision_pruned_lookahead": ("""
        class Policy:
            def get_action(self, obs):
                best, choice = None, 0
                for a in (-1, 0, 1):
                    nxt = obs["x"] + a
                    if nxt in obs["obstacles"]:
                        continue
                    reward = 10 if nxt == obs["goal"] else -abs(obs["goal"] - nxt)
                    if best is None or reward > best:
                        best, choice = reward, a
                return choice
        """, "planning"),
    "conditional_mutation_without_prediction": ("""
        class Policy:
            def get_action(self, obs):
                keep = []
                for a in (-1, 1):
                    if a * obs["x"] < 0:
                        keep.append(a)
                return keep[0] if keep else 0
        """, "reactive"),
}


@pytest.mark.parametrize("name", sorted(RUBRIC_CASES))
def test_rubric_case(tmp_path, name):
    src, expected = RUBRIC_CASES[name]
    r = run(tmp_path, src)
    assert r.verdict == expected, r.text()
    assert bool(r.evidence) is (expected == "planning")
    assert all(e.rule and e.influence for e in r.evidence), r.text()


def test_ranking_and_lookahead_differ_only_by_prediction(tmp_path):
    """Same candidate moves, same choice: only the predicted outcome makes it planning (rule 3)."""
    plain = run(tmp_path, RUBRIC_CASES["present_state_heuristic_ranking"][0])
    predicted = run(tmp_path, RUBRIC_CASES["predicted_move_ranking"][0])
    assert (plain.verdict, predicted.verdict) == ("reactive", "planning")
    assert any(n.kind == "ranking" for n in plain.notes), plain.text()


def test_target_choice_is_explained(tmp_path):
    r = run(tmp_path, REVIEW_CASES["target_loop_false_choice"][0])
    assert any(n.kind == "target-choice" for n in r.notes), r.text()


def test_rejected_patterns_are_notes_not_evidence(tmp_path):
    r = run(tmp_path, REVIEW_CASES["zero_horizon_enumeration"][0])
    assert any(n.kind == "enumeration" for n in r.notes), r.text()
    r = run(tmp_path, RUBRIC_CASES["tree_walk_without_selection"][0])
    assert any(n.kind == "recursion" for n in r.notes), r.text()
    r = run(tmp_path, REVIEW_CASES["recursive_arithmetic"][0])
    assert any(n.kind == "recursion" for n in r.notes), r.text()


# --------------------------------------------------------------------------- 3. invariance under rewrites

LOOKAHEAD_BASE = """
import numpy as np
ACTIONS = [-1, 1]
class Policy:
    def get_action(self, obs):
        costs = [(obs + a) ** 2 for a in ACTIONS]
        {body}
"""
ENCODINGS = {
    "index": "return int(np.argmin(costs))",
    "affine": "return 2 * int(np.argmin(costs)) - 1",
    "table": "return ACTIONS[int(np.argmin(costs))]",
    "dict": 'return {0: "left", 1: "right"}[int(np.argmin(costs))]',
    "one_hot": "return np.eye(2)[int(np.argmin(costs))]",
    "branch": 'i = int(np.argmin(costs))\n        if i == 0:\n            return "left"\n        return "right"',
    "method_helper": "return self.encode(int(np.argmin(costs)))\n    def encode(self, i):\n        return ACTIONS[i]",
}

INVARIANT_PAIRS = {
    "lambda_vs_named_key": (REVIEW_CASES["one_step_key_lambda"][0], REVIEW_CASES["one_step_key_function"][0]),
    "lambda_vs_method_key": ("""
        class Policy:
            def get_action(self, obs):
                return min((-1, 0, 1), key=lambda a: abs(self.goal - (obs + a)))
        """, """
        class Policy:
            def get_action(self, obs):
                self.obs = obs
                return min((-1, 0, 1), key=self.score)
            def score(self, a):
                return abs(self.goal - (self.obs + a))
        """),
    "direct_vs_identity": (REVIEW_CASES["one_step_direct"][0], REVIEW_CASES["one_step_identity"][0]),
    "direct_vs_method_identity": (REVIEW_CASES["one_step_direct"][0], """
        import numpy as np
        class Policy:
            def same(self, x):
                return x
            def get_action(self, obs):
                costs = [(obs + a)**2 for a in [-1, 1]]
                return self.same(self.same(np.argmin(costs)))
        """),
    "nested_vs_split_index": (REVIEW_CASES["index_nested"][0], REVIEW_CASES["index_split"][0]),
    "nested_vs_split_argmin": (REVIEW_CASES["one_step_direct"][0], """
        import numpy as np
        class Policy:
            def get_action(self, obs):
                actions = [-1, 1]
                costs = [(obs + a)**2 for a in actions]
                arr = np.array(costs)
                i = np.argmin(arr)
                choice = i
                return choice
        """),
    "plain_vs_annotated_best_so_far": (REVIEW_CASES["best_so_far"][0], REVIEW_CASES["best_so_far_annotated"][0]),
    "plain_vs_annotated_lists": (REVIEW_CASES["one_step_direct"][0], """
        import numpy as np
        class Policy:
            def get_action(self, obs):
                actions: list[int] = [-1, 1]
                costs: list[float] = [(obs + a)**2 for a in actions]
                best: int = np.argmin(costs)
                return best
        """),
    "alias_vs_direct_call": (REVIEW_CASES["indirect_callback"][0], """
        def plan(obs):
            return min([-1, 1], key=lambda a: (obs + a)**2)
        class Policy:
            def get_action(self, obs):
                return plan(obs)
        """),
    "callback_field_vs_direct_method": ("""
        class Policy:
            def __init__(self):
                self.scorer = self.predicted_cost
            def predicted_cost(self, a):
                return abs(self.goal - (self.x + a))
            def get_action(self, obs):
                self.x = obs
                return min((-1, 1), key=self.scorer)
        """, """
        class Policy:
            def predicted_cost(self, a):
                return abs(self.goal - (self.x + a))
            def get_action(self, obs):
                self.x = obs
                return min((-1, 1), key=self.predicted_cost)
        """),
    "renamed_class": (REVIEW_CASES["best_so_far"][0],
                      REVIEW_CASES["best_so_far"][0].replace("class Policy", "class Controller")),
}
for _name, _body in ENCODINGS.items():
    if _name != "index":
        INVARIANT_PAIRS[f"encoding_index_vs_{_name}"] = (LOOKAHEAD_BASE.format(body=ENCODINGS["index"]),
                                                         LOOKAHEAD_BASE.format(body=_body))


@pytest.mark.parametrize("name", sorted(INVARIANT_PAIRS))
def test_invariant_pair(tmp_path, name):
    a, b = INVARIANT_PAIRS[name]
    ra, rb = run(tmp_path, a), run(tmp_path, b)
    assert ra.verdict == rb.verdict == "planning", ra.text() + "\n---\n" + rb.text()
    assert {e.kind for e in ra.evidence} == {e.kind for e in rb.evidence}


UNRELATED = """
import itertools
import networkx as nx
class Policy:
    def __init__(self):
        self.plan = None
        self.enabled = True
    def make_plan(self, obs):
        self.plan = min(itertools.permutations(obs), key=sum)
        return nx.shortest_path(obs, 0, 1)
"""


@pytest.mark.parametrize("base", ["best_so_far", "script_constant", "reactive_control"])
def test_unrelated_same_named_class_changes_nothing(tmp_path, base):
    src, expected = REVIEW_CASES[base]
    alone = run(tmp_path, {"a.py": src})
    together = run(tmp_path, {"a.py": src, "other.py": UNRELATED}, ["a.py", "other.py"], "a.Policy.get_action")
    assert alone.verdict == together.verdict == expected, together.text()
    assert [str(e) for e in alone.evidence] == [str(e) for e in together.evidence]


def test_unrelated_module_with_same_field_and_setting(tmp_path):
    """Writes to `self.plan` / `self.enabled` in another module's Policy are not ours."""
    a = """
        import numpy as np
        class Policy:
            def __init__(self):
                self.plan = [0]
                self.enabled = False
            def get_action(self, obs):
                if self.enabled:
                    return int(np.argmin([(obs + a) ** 2 for a in (-1, 1)]))
                return self.plan[0]
    """
    alone = run(tmp_path, {"a.py": a})
    together = run(tmp_path, {"a.py": a, "b.py": UNRELATED}, ["a.py", "b.py"], "a.Policy.get_action")
    # b.Policy's own `self.enabled = True` and `self.plan = ...` belong to another class family.
    assert alone.verdict == together.verdict == "reactive", together.text()
    assert alone.pruned and together.pruned
    # A write through another object (no types: it might be ours) does make the setting non-constant.
    p = run(tmp_path, {"a.py": a, "c.py": "from a import Policy\np = Policy()\np.enabled = True\n"},
            ["a.py", "c.py"], "a.Policy.get_action")
    assert p.verdict == "planning", p.text()


def test_package_entry_file_vs_directory(tmp_path):
    files = {"pkg/__init__.py": "from .policy import Policy\n",
             "pkg/model.py": "def step(s, a):\n    return s + a\n",
             "pkg/search.py": ("from .model import step\n"
                               "def best(s, goal):\n"
                               "    return min((-1, 0, 1), key=lambda a: abs(goal - step(s, a)))\n"),
             "pkg/policy.py": ("from .search import best\n"
                               "class Policy:\n"
                               "    def get_action(self, obs):\n"
                               "        return best(obs['x'], obs['goal'])\n")}
    entry = run(tmp_path, files, ["pkg/policy.py"])
    whole = run(tmp_path, files, ["pkg"], "policy.Policy.get_action")
    assert entry.verdict == whole.verdict == "planning", entry.text()
    assert entry.evidence[0].what == whole.evidence[0].what


# --------------------------------------------------------------------------- 4. analysis status

OPAQUE_SCORER = """
import numpy as np
class Policy:
    def __init__(self, model):
        self.model = model
    def get_action(self, obs):
        scores = [self.model.evaluate(obs, a) for a in (-1, 0, 1)]
        return int(np.argmax(scores)) - 1
"""

REVIEW_STATUS_CASES = {
    "missing_module": ({"policy.py": """
        from planner_lib import compute_path
        class Policy:
            def get_action(self, obs):
                return compute_path(obs)[0]
        """}, "unresolved-import"),
    "missing_relative_module": ({"pkg/__init__.py": "", "pkg/policy.py": """
        from .gone import plan
        class Policy:
            def get_action(self, obs):
                return plan(obs)
        """}, "unresolved-import"),
    "unresolved_key_callback": ({"policy.py": """
        class Policy:
            def __init__(self, scorer):
                self.scorer = scorer
            def get_action(self, obs):
                return min((-1, 0, 1), key=self.scorer)
        """}, "unresolved-callback"),
    "opaque_candidate_scorer": ({"policy.py": OPAQUE_SCORER}, "opaque-scorer"),
    "generic_solver": ({"policy.py": """
        import cvxpy as cp
        class Policy:
            def get_action(self, obs):
                u = cp.Variable(2)
                prob = cp.Problem(cp.Minimize(cp.sum_squares(u - obs["ref"])))
                prob.solve()
                return u.value
        """}, "solver-role"),
    "external_planner_object": ({"policy.py": """
        class Policy:
            def __init__(self, planner):
                self.planner = planner
            def get_action(self, obs):
                return self.planner.plan(obs)[0]
        """}, "planner-like-call"),
    "dynamic_dispatch": ({"policy.py": """
        import networkx as nx
        class Policy:
            def __init__(self, mode):
                self.mode = mode
            def _plan(self, obs):
                return nx.shortest_path(obs["graph"], obs["pos"], obs["goal"])[1]
            def _react(self, obs):
                return obs["default"]
            def get_action(self, obs):
                return getattr(self, "_" + self.mode)(obs)
        """}, "dynamic-call"),
    "generic_entrypoint_name": ({"policy.py": """
        class Controller:
            def step(self, obs):
                return 1 if obs > 0 else -1
        """}, "entrypoint"),
}


@pytest.mark.parametrize("name", sorted(REVIEW_STATUS_CASES))
def test_unresolved_code_needs_review(tmp_path, name):
    files, kind = REVIEW_STATUS_CASES[name]
    r = run(tmp_path, files, [max(files, key=lambda f: f.endswith("policy.py"))])
    assert r.verdict == "needs_review" and r.status == "needs_review", r.text()
    assert r.label == "reactive" and r.planning is None  # binary label kept; never a confident False
    assert kind in {i.kind for i in r.review_reasons}, r.text()


def test_supplying_the_missing_module_resolves_review(tmp_path):
    files = dict(REVIEW_STATUS_CASES["missing_module"][0])
    files["planner_lib.py"] = """
        import networkx as nx
        def compute_path(obs):
            return nx.shortest_path(obs["graph"], obs["pos"], obs["goal"])[1:]
    """
    r = run(tmp_path, files)
    assert r.verdict == "planning" and r.status == "supported", r.text()


def test_configuration_resolves_opaque_scorer(tmp_path):
    as_model = run(tmp_path, OPAQUE_SCORER, config=PolicyConfig(transition_models=("evaluate",)))
    assert as_model.verdict == "planning" and as_model.evidence[0].kind in ("lookahead", "transition-model")
    as_scorer = run(tmp_path, OPAQUE_SCORER, config=PolicyConfig(reactive_scorers=("evaluate",)))
    assert as_scorer.verdict == "reactive" and as_scorer.status == "supported", as_scorer.text()


def test_configured_planner_and_state_fields(tmp_path):
    src = """
        from kin import plan_reach
        class Policy:
            def get_action(self, obs):
                return plan_reach(obs)[0]
    """
    files = {"policy.py": src, "kin.py": "def plan_reach(obs):\n    return [obs]\n"}
    assert run(tmp_path, files).verdict == "reactive"
    configured = run(tmp_path, files, config=PolicyConfig(planners={"kin.plan_reach": "motion planner"}))
    assert configured.verdict == "planning" and configured.evidence[0].kind == "planner-call"
    field_src = """
        class Policy:
            def tick(self, sensor):
                self.reading = sensor
            def get_action(self):
                return min((-1, 1), key=lambda a: abs(self.reading + a))
    """
    assert run(tmp_path, field_src).verdict == "planning"
    assert run(tmp_path, field_src, config=PolicyConfig(state_fields=())).verdict == "reactive"


def test_known_callables_and_names_do_not_need_review(tmp_path):
    r = run(tmp_path, """
        import operator
        class Policy:
            def __init__(self, solver):
                self.solver = solver
            def get_action(self, obs):
                order = sorted(obs["items"], key=operator.itemgetter(1))
                widths = list(map(float, obs["w"]))
                first = min(order, key=len)
                return self.solver.resolve(first, widths)
    """)
    assert r.verdict == "reactive" and r.status == "supported", r.text()
    r = run(tmp_path, """
        class Policy:
            def get_action(self, obs):
                return self.agent.replanRoute(obs)
    """)
    assert r.verdict == "needs_review" and r.review_reasons[0].kind == "planner-like-call", r.text()


def test_planning_with_unknowns_stays_supported(tmp_path):
    """Unresolved code cannot remove supported planning evidence; it becomes a note."""
    r = run(tmp_path, """
        import networkx as nx
        from missing_lib import smooth
        class Policy:
            def get_action(self, obs):
                path = nx.shortest_path(obs["graph"], obs["pos"], obs["goal"])
                return smooth(path)[1]
    """)
    assert r.verdict == "planning" and r.status == "supported" and r.planning is True
    assert any(n.kind == "unresolved-import" for n in r.notes), r.text()


def test_report_schema(tmp_path):
    r = run(tmp_path, REVIEW_CASES["route_search"][0])
    d = r.to_dict()
    assert {"verdict", "label", "status", "planning", "evidence", "review_reasons", "notes", "rubric_version",
            "entrypoint", "coverage", "pruned"} <= set(d)
    assert d["evidence"][0]["rule"] and d["evidence"][0]["sites"] and d["coverage"]["modules"]


# --------------------------------------------------------------------------- entrypoints

def test_entrypoint_discovery(tmp_path):
    def graph(src):
        d = tmp_path / f"e{next(_ids)}"
        d.mkdir()
        (d / "m.py").write_text(textwrap.dedent(src))
        return build_graph([d / "m.py"])

    assert find_decision_function(graph("def get_action(obs):\n    return 0\n")) == "m.get_action"
    two = graph("class A:\n    def get_action(self, o):\n        return 0\n"
                "class B:\n    def get_action(self, o):\n        return 1\n")
    with pytest.raises(EntrypointError) as err:
        find_decision_function(two)
    assert sorted(err.value.candidates) == ["m.A.get_action", "m.B.get_action"]
    assert find_decision_function(two, "B.get_action") == "m.B.get_action"
    stub = graph("class Base:\n    def get_action(self, o):\n        raise NotImplementedError\n"
                 "class P(Base):\n    def get_action(self, o):\n        return 1\n")
    assert find_decision_function(stub) == "m.P.get_action"
    # a policy-specific name wins over a generic one; only a generic name needs review
    g = graph("class P:\n    def step(self, o):\n        return 0\n    def act(self, o):\n        return 1\n")
    assert find_decision_function(g) == "m.P.act"
    r = classify(g, "m.P.act")
    assert r.entrypoint == "name" and r.status == "supported"
