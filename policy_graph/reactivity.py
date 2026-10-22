"""Does a policy plan? Explicit rules on its dependency graph (rubric ``RUBRIC_VERSION``).

Categories
----------
A policy is **planning** when a reachable part of it that influences the returned action

1. searches for or constructs a task plan, route, motion plan or control trajectory
   with a planning procedure, or
2. evaluates hypothetical consequences of candidate actions or plans and uses those
   consequences to choose what to do (a horizon of one step is enough).

Otherwise it is **reactive**, the name kept for the non-planning category. It covers
rule-based controllers, fixed scripts (predefined action sequences), and action
rankings that predict nothing (an argmax over logits, learned action scores or
present-state heuristics). A scripted policy that calls a planner for its actions is
planning.

The label is a static reading of the analysed code under its analysed configuration:
"planning" means a supported planning computation is reachable and influences the
action, not that it runs on every call.

What counts as evidence (each must influence the action: it lies in the backward slice
of the decision function's return value, with unreachable code already removed)
--------------------------------------------------------------------------------
planner-call      a call to a contracted planner (``PLANNERS``: shortest-path and routing
                  libraries, OMPL, ...) or a planner named in ``PolicyConfig.planners``.
                  The planner may return its already-selected route or plan.
graph-search      a hand-written search loop: a worklist that is popped and refilled with
                  successors of the popped element and consults a visited/cost/parent
                  table (BFS, Dijkstra, A*), or a layered expansion in which each element
                  of the current layer adds successors to the next layer.
tree-search       recursion that branches over alternatives (in a loop or comprehension,
                  or at two or more call sites) and selects among the results (min, max,
                  best-so-far, or a test on a recursive result, as in backtracking).
ordering-search   a choice among the orderings produced by ``itertools.permutations``
                  (exhaustive task-order search).
lookahead         a choice among candidates (argmin/argmax/argsort, min/max/sorted, an
                  index of the min/max, a best-so-far loop, or an optimiser's objective)
                  whose scores depend on a hypothetical outcome of a candidate:
                  - an additive update of a state-like value by a candidate,
                    ``obs + a``, ``pos + dt * v``, ``s += a`` (also inside helpers and
                    across multi-step rollouts), or
                  - a call to a transition model named in ``PolicyConfig.transition_models``.
                  When the only predictions are arithmetic, the chosen candidate must
                  become the action through a state-independent encoding (``actions[i]``,
                  ``2 * i - 1``, a lookup table, an identity helper): this separates
                  choosing an *action* by its predicted outcome from choosing a *target*
                  by distance and then steering towards it (``np.sign(t - pos)``).
transition-model  a configured transition model whose prediction influences the action.

Recursion, iteration, enumeration (``itertools.product``), numerical optimisation,
copying, matching input/output types and function composition are not evidence on
their own; they are reported as notes when they were considered and rejected.

Analysis status
---------------
Independently of the label, ``status`` is ``supported`` or ``needs_review``. A reactive
result needs review when something the analysis could not see could change it: an
unresolved import used by the action, an unresolved callback at a choice, candidates
scored by an opaque call, a generic solver, an unresolved call named like a planner, a
dynamic call or ambiguous method that could reach planning code, or an entrypoint found
only by a generic name. ``Report.planning`` is then ``None`` and ``Report.verdict`` is
``"needs_review"``, so an unknown result never reads as a confident "reactive".

State: the decision function's parameters (except ``self``) plus *observation fields*,
attributes assigned from the parameters of the policy's non-constructor methods
(e.g. ``observe(self, obs): self.obs = obs``). Both can be set in ``PolicyConfig``.
"""

from __future__ import annotations

import ast
import json
import re
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path

from depgraph import (DATA_KINDS, EDGE_KINDS, MUTATING_METHODS, OPTIMISERS, CallSite, DependencyGraph, Node,
                      _field_owner, _walk, build_graph)

RUBRIC_VERSION = "planning-rubric-2 (2026-10-20)"
RULE_PLAN = "constructs a plan, route or trajectory with a planning procedure"
RULE_LOOKAHEAD = "evaluates hypothetical consequences of candidates and chooses by them"

STRONG_DECISION_NAMES = ("get_action", "act", "select_action", "choose_action", "compute_action", "policy")
GENERIC_DECISION_NAMES = ("step", "predict", "__call__")  # also used for non-policy code: needs review
DECISION_NAMES = STRONG_DECISION_NAMES + GENERIC_DECISION_NAMES
CONSTRUCTORS = ("__init__", "__new__", "__post_init__")

# Planner contracts: library calls that search for and return a route, path, plan or
# cost-to-go table. Exact names, or prefixes ending in ".".
PLANNERS = {
    **{f"networkx.{n}": "shortest-path search" for n in (
        "shortest_path", "shortest_path_length", "astar_path", "astar_path_length", "dijkstra_path",
        "dijkstra_path_length", "bidirectional_dijkstra", "bidirectional_shortest_path", "bellman_ford_path",
        "bellman_ford_path_length", "single_source_dijkstra", "single_source_dijkstra_path",
        "single_source_dijkstra_path_length", "multi_source_dijkstra", "multi_source_dijkstra_path",
        "single_source_shortest_path", "single_source_shortest_path_length", "all_shortest_paths",
        "all_pairs_shortest_path", "all_pairs_shortest_path_length", "all_pairs_dijkstra_path",
        "all_pairs_dijkstra_path_length", "shortest_simple_paths", "floyd_warshall", "floyd_warshall_numpy",
        "johnson")},
    "networkx.algorithms.approximation.traveling_salesman_problem": "task-order (TSP) planner",
    "networkx.approximation.traveling_salesman_problem": "task-order (TSP) planner",
    **{f"scipy.sparse.csgraph.{n}": "shortest-path search" for n in (
        "dijkstra", "shortest_path", "bellman_ford", "johnson", "floyd_warshall", "yen",
        "breadth_first_order", "depth_first_order", "breadth_first_tree", "depth_first_tree")},
    "skimage.graph.route_through_array": "minimum-cost route search",
    "skimage.graph.MCP": "minimum-cost route search",
    "skimage.graph.MCP_Geometric": "minimum-cost route search",
    "ortools.constraint_solver.pywrapcp.RoutingModel": "vehicle-routing planner",
    "ompl.": "motion planner (OMPL)",
    "pybullet_planning.plan_joint_motion": "motion planner", "pybullet_planning.plan_motion": "motion planner",
    "pybullet_planning.plan_base_motion": "motion planner", "pybullet_planning.birrt": "motion planner",
    "pybullet_planning.rrt_connect": "motion planner", "pybullet_planning.rrt": "motion planner",
    "pybullet_planning.prm": "motion planner", "pybullet_planning.lazy_prm": "motion planner",
    "pydrake.planning.": "motion / trajectory planner (Drake)",
}
# Solvers whose role (planning or not) depends on the model they are given: review.
GENERIC_SOLVERS = ("cvxpy.", "pulp.", "casadi.", "pyomo.", "gurobipy.", "ortools.sat.", "ortools.linear_solver.",
                   "scipy.optimize.linprog", "scipy.optimize.milp", "pydrake.solvers.")
# Morphological dilation applied repeatedly to its own output grows a reached set by one
# step per iteration: a grid wavefront (brushfire / BFS) that computes arrival times.
WAVEFRONT_OPS = {"scipy.ndimage.maximum_filter", "scipy.ndimage.minimum_filter", "scipy.ndimage.binary_dilation",
                 "scipy.ndimage.grey_dilation", "scipy.ndimage.grey_erosion", "skimage.morphology.dilation",
                 "skimage.morphology.binary_dilation", "cv2.dilate"}
RANKERS = {"sorted", "numpy.argsort", "method:argsort", "method:sort", "heapq.nsmallest", "heapq.nlargest"}
ENUMERATORS = {"itertools.permutations": "orderings", "itertools.product": "combinations",
               "itertools.combinations": "subsets", "itertools.combinations_with_replacement": "multisets"}
SELECTION_APIS = {"numpy.argmin", "numpy.argmax", "numpy.argsort", "numpy.nanargmin", "numpy.nanargmax",
                  "numpy.lexsort", "heapq.nsmallest", "heapq.nlargest", "method:argmin", "method:argmax",
                  "method:argsort"}
KEYED_SELECTION = {"min", "max", "sorted", "method:sort"}  # see _compares_alternatives
EXTREMES = {"min", "max", "numpy.min", "numpy.max", "numpy.amin", "numpy.amax", "numpy.nanmin", "numpy.nanmax",
            "method:min", "method:max"}
OPAQUE = ("method", "dynamic", "unresolved-name", "unresolved-import")
# Method names on unknown receivers that read or reshape data rather than compute a model.
ACCESSOR_METHODS = MUTATING_METHODS | frozenset({
    "get", "items", "keys", "values", "copy", "tolist", "astype", "reshape", "flatten", "ravel", "squeeze",
    "transpose", "sum", "mean", "std", "max", "min", "prod", "dot", "cross", "norm", "clip", "round", "abs",
    "any", "all", "item", "index", "count", "append", "extend", "pop", "add", "update", "setdefault", "sort",
    "argmin", "argmax", "argsort", "cumsum", "split", "strip", "lower", "upper", "format", "join", "startswith",
    "endswith", "replace", "encode", "decode", "view", "numpy", "detach", "cpu", "float", "int", "long",
    "tobytes", "fill", "nonzero", "diagonal", "trace", "conj", "real", "imag", "as_matrix", "as_quat",
    "as_euler", "as_rotvec", "inv", "apply", "contains", "intersects", "distance", "buffer",
})
# Name tokens (split on "_" and case changes) that suggest an unresolved call plans.
PLANNER_TOKENS = ("plan", "search", "solve", "astar", "dijkstra", "shortest", "bfs", "dfs", "rrt", "prm", "rollout",
                  "simulat", "lookahead", "mpc", "optimi", "trajopt")


def _planner_like(name: str) -> bool:
    tokens = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name).lower().split("_")
    return any(t.startswith(PLANNER_TOKENS) or t.endswith("plan") for t in tokens if t)
NO_ITER = tuple(k for k in DATA_KINDS if k != "iter")


@dataclass
class PolicyConfig:
    """Per-corpus settings. Everything is optional; the defaults follow the module docstring."""

    decision: str | None = None  # qualified (or suffix) name of the function returning the action
    state_params: tuple[str, ...] | None = None  # decision parameters that carry the state (default: all)
    state_fields: tuple[str, ...] | None = None  # attributes holding observations (default: inferred)
    planners: dict[str, str] = field(default_factory=dict)  # extra planner contracts: name or "prefix." -> what
    transition_models: tuple[str, ...] = ()  # calls that predict the next state (qualified names or method names)
    reactive_scorers: tuple[str, ...] = ()  # opaque calls declared non-predictive (e.g. a learned Q-network)
    libraries: tuple[str, ...] = ()  # extra top-level packages that are libraries, not missing project code

    @classmethod
    def from_json(cls, path: str | Path) -> "PolicyConfig":
        data = json.loads(Path(path).read_text())
        for k in ("state_params", "state_fields", "transition_models", "reactive_scorers", "libraries"):
            if data.get(k) is not None:
                data[k] = tuple(data[k])
        return cls(**data)


@dataclass
class Evidence:
    """One planning computation that influences the action, located in the source."""

    kind: str  # planner-call | graph-search | tree-search | ordering-search | generate-and-test | lookahead | transition-model
    what: str
    function: str
    file: str
    line: int
    rule: str = ""  # the rubric rule it satisfies
    influence: str = ""  # how it reaches the action (a dependence path)
    sites: list[tuple[str, str, int]] = field(default_factory=list)  # (role, file, line)
    assumptions: list[str] = field(default_factory=list)
    nodes: tuple = field(default=(), repr=False, compare=False)
    winners: tuple = field(default=(), repr=False, compare=False)

    def __str__(self) -> str:
        return f"{self.what}  ({Path(self.file).name}:{self.line}, in {self.function.split('.', 1)[-1]})"

    def to_dict(self) -> dict:
        return {"kind": self.kind, "rule": self.rule, "what": self.what, "function": self.function,
                "file": self.file, "line": self.line, "influence": self.influence,
                "sites": [list(s) for s in self.sites], "assumptions": list(self.assumptions)}


@dataclass
class Issue:
    """Something the analysis could not resolve, or a candidate it considered and rejected."""

    kind: str
    what: str
    file: str = ""
    line: int = 0
    function: str = ""

    def __str__(self) -> str:
        where = f"  ({Path(self.file).name}:{self.line})" if self.file else ""
        return f"[{self.kind}] {self.what}{where}"

    def to_dict(self) -> dict:
        return {"kind": self.kind, "what": self.what, "file": self.file, "line": self.line, "function": self.function}


@dataclass
class Report:
    """Label, analysis status and evidence for one decision function.

    ``label`` is binary (planning / reactive). ``status`` says whether the label is
    supported or needs review. ``planning`` (kept for compatibility) is True, False, or
    None when the reactive label needs review; ``verdict`` is then ``"needs_review"``.
    """

    decision: str
    planning: bool | None
    evidence: list[Evidence]  # what makes it planning (empty if reactive)
    pruned: list[tuple[str, int, str, str]] = field(default_factory=list)
    status: str = "supported"  # supported | needs_review
    review_reasons: list[Issue] = field(default_factory=list)  # material unknowns (only when reactive)
    notes: list[Issue] = field(default_factory=list)  # rejected candidates, non-material unknowns
    entrypoint: str = "explicit"  # explicit | name | generic name
    coverage: dict = field(default_factory=dict)
    rubric_version: str = RUBRIC_VERSION

    @property
    def label(self) -> str:
        return "planning" if self.evidence else "reactive"

    @property
    def verdict(self) -> str:
        return self.label if self.status == "supported" else "needs_review"

    def text(self) -> str:
        lines = [f"decision function: {self.decision}  (entrypoint: {self.entrypoint})",
                 f"verdict: {self.verdict}  (label: {self.label}; status: {self.status}; rubric: {self.rubric_version})"]
        if self.evidence:
            lines.append("because:")
            for e in sorted(self.evidence, key=lambda e: (e.file, e.line)):
                lines.append(f"  [{e.kind}] {e}")
                if e.influence:
                    lines.append(f"      reaches the action: {e.influence}")
                for a in e.assumptions:
                    lines.append(f"      assumes: {a}")
        if self.review_reasons:
            lines.append("needs review because:")
            lines += [f"  {i}" for i in self.review_reasons]
        if self.notes:
            lines.append("notes:")
            lines += [f"  {i}" for i in self.notes]
        if self.pruned:
            lines.append("skipped because a constant setting makes them unreachable:")
            lines += [f"  {Path(f).name}:{ln}  {t}  -> {b} never runs" for f, ln, t, b in self.pruned]
        return "\n".join(lines)

    def to_dict(self) -> dict:
        return {"decision": self.decision, "verdict": self.verdict, "label": self.label, "status": self.status,
                "planning": self.planning, "entrypoint": self.entrypoint, "rubric_version": self.rubric_version,
                "evidence": [e.to_dict() for e in self.evidence],
                "review_reasons": [i.to_dict() for i in self.review_reasons],
                "notes": [i.to_dict() for i in self.notes],
                "pruned": [list(p) for p in self.pruned], "coverage": self.coverage}


class EntrypointError(ValueError):
    """No decision function, or several equally plausible ones."""

    def __init__(self, message: str, candidates: list[str]) -> None:
        super().__init__(message)
        self.candidates = candidates


def _is_stub(node: ast.AST) -> bool:
    body = [s for s in getattr(node, "body", []) if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant))]
    return all(isinstance(s, ast.Pass) or (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant))
               or (isinstance(s, ast.Raise) and "NotImplementedError" in ast.unparse(s)) for s in body)


def discover_entrypoint(g: DependencyGraph, name: str | None = None) -> tuple[str, str]:
    """(qualname, basis) of the function that returns the action.

    ``basis`` is ``explicit`` (given ``name``), ``name`` (a policy-specific name such as
    ``get_action``), or ``generic name`` (``step``/``predict``/``__call__``, which also
    name non-policy code: the report then needs review). Methods and top-level functions
    are both considered; several candidates with the first matching name raise
    ``EntrypointError`` instead of picking one.
    """
    funcs = {q: f for q, f in g.functions.items() if not f.is_lambda and f.parent is None}
    if name:
        hits = [q for q in funcs if q == name or q.endswith("." + name)]
        if len(hits) != 1:
            raise EntrypointError(f"decision function {name!r} matches {hits or 'nothing'}", hits)
        basis = "explicit"
    else:
        hits = []
        for candidate in DECISION_NAMES:
            hits = [q for q, f in funcs.items() if f.node.name == candidate and not _is_stub(f.node)]
            if hits:
                break
        if not hits:
            raise EntrypointError(f"no decision function found; pass one of {sorted(funcs)}", sorted(funcs))
        if len(hits) > 1:
            raise EntrypointError(f"ambiguous decision function: {sorted(hits)}; pass one with --decision",
                                  sorted(hits))
        basis = "generic name" if g.functions[hits[0]].node.name in GENERIC_DECISION_NAMES else "name"
    g.entrypoint_basis[hits[0]] = basis
    return hits[0], basis


def find_decision_function(g: DependencyGraph, name: str | None = None) -> str:
    """The method/function that returns the action (see ``discover_entrypoint``)."""
    return discover_entrypoint(g, name)[0]


def analyze(paths: list[str | Path], decision: str | None = None, config: PolicyConfig | None = None) -> Report:
    """Build the graph for ``paths`` and classify the decision function."""
    config = config or PolicyConfig()
    g = build_graph(paths, libraries=config.libraries)
    q, _ = discover_entrypoint(g, decision or config.decision)
    return classify(g, q, config)


def classify(g: DependencyGraph, decision: str, config: PolicyConfig | None = None) -> Report:
    return _Classifier(g, decision, config or PolicyConfig()).run()


@dataclass
class _Choice:
    """A selection among alternatives: what selects, what it selects (winners), and its scores."""

    what: str
    function: str
    file: str
    line: int
    site: Node | None
    winners: set[Node]
    scores: set[Node]
    optimiser: bool = False
    clamp: bool = False  # min/max of a few separate values rather than over a collection


def _compares_alternatives(call: ast.Call) -> bool:
    """Built-in min/max/sorted used to pick among alternatives, not to clamp.

    Counts: a key= function, a single collection (``min(costs)``, a comprehension), or
    two or more computed values. Not: ``max(0, x)``-style clamping with a literal.
    """
    if any(k.arg == "key" for k in call.keywords):
        return True
    args = call.args
    if len(args) == 1:
        return not isinstance(args[0], ast.Constant)
    return len(args) >= 2 and not any(isinstance(a, ast.Constant) or
                                      (isinstance(a, ast.UnaryOp) and isinstance(a.operand, ast.Constant))
                                      for a in args)


def _calls_in_iteration(fn_node: ast.AST) -> set[int]:
    """ids of calls inside a loop or comprehension of the function's own body."""
    out: set[int] = set()

    def visit(n: ast.AST, inside: bool) -> None:
        for child in ast.iter_child_nodes(n):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
                continue
            here = inside or isinstance(n, (ast.For, ast.AsyncFor, ast.While, ast.ListComp, ast.SetComp,
                                            ast.GeneratorExp, ast.DictComp))
            if isinstance(child, ast.Call) and here:
                out.add(id(child))
            visit(child, here)
    visit(fn_node, False)
    return out


class _Classifier:
    def __init__(self, g: DependencyGraph, decision: str, cfg: PolicyConfig) -> None:
        self.g, self.cfg, self.decision = g, cfg, decision
        self.fn = g.functions[decision]
        self.sink = self.fn.return_node
        self.slice = g.backward_slice([self.sink]) | {self.sink}
        self.by_scope: dict[str, list[Node]] = defaultdict(list)
        for n in g.nodes:
            self.by_scope[n.scope].append(n)
        self.state = self._state_sources()
        self.S = g.forward_slice(self.state, DATA_KINDS) | self.state  # computed from the state
        self.SL = self._state_like()  # *is* the state (or a state updated additively)
        self.cands = g.iter_vars | g.decision_vars
        self.C = g.forward_slice(self.cands, DATA_KINDS) | self.cands  # computed from some loop/callback variable
        self._without: dict[Node, set[Node]] = {}
        self._sources: dict[Node, set[Node]] = {}
        self.H = {o for o in g.ops if self._hypothetical(o)}  # hypothetical outcomes of candidates
        self.roll_sources: dict[Node, set[str]] = {}  # rollout -> functions whose candidates drive it
        self.H_roll = self._rollouts()  # closed-loop simulations: state update -> accumulated time/cost
        accs = set().union(set(), *self.H_roll.values())
        self.H_fwd = g.forward_slice(self.H | accs) | self.H | accs  # everything that depends on one
        self.notes: list[Issue] = []
        self.review: list[Issue] = []

    # ------------------------------------------------------------------ state
    def _state_sources(self) -> set[Node]:
        fn, g, cfg = self.fn, self.g, self.cfg
        params = [p for p in fn.params if not (fn.is_method and p == fn.params[0])]
        if cfg.state_params is not None:
            params = [p for p in params if p in cfg.state_params]
        out = {fn.param_nodes[p] for p in params if p in fn.param_nodes}
        if fn.cls:
            owner = _field_owner(g, fn.cls)
            if cfg.state_fields is not None:
                out |= {Node("field", f"{owner}.{a}") for a in cfg.state_fields}
            else:  # observation fields: assigned from what non-constructor methods receive
                received = set()
                for f in g.functions.values():
                    if f.cls and not f.is_lambda and f.parent is None and _field_owner(g, f.cls) == owner \
                            and f.node.name not in CONSTRUCTORS:
                        received |= {pn for p, pn in f.param_nodes.items() if not (f.is_method and p == f.params[0])}
                out |= {n for n in g.forward_slice(received, NO_ITER)
                        if n.kind == "field" and n.name.startswith(owner + ".")}
        return out

    def _state_like(self) -> set[Node]:
        """Values that are the state itself, a copy or part of it, or the state shifted by ``+``/``-``.
        Elements drawn from a state collection by iteration (``for o in obs["objects"]``) are
        candidates, not the state."""
        users: dict[Node, set[Node]] = defaultdict(set)
        for o, info in self.g.ops.items():
            for n in info.left_copy:
                users[n].add(o)
            if info.symbol.startswith("+"):
                for n in info.right_copy:
                    users[n].add(o)
        succ = self.g.copy_successors()
        seen, stack = set(self.state), list(self.state)
        while stack:
            u = stack.pop()
            nxt = {v for v in succ.get(u, set()) if "iter" not in self.g.preds[v].get(u, ())}
            for v in nxt | users.get(u, set()):
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return seen

    def _state_without(self, x: Node) -> set[Node]:
        """What depends on the state when candidate variable ``x`` is taken away (its elements may
        themselves come from the state, as in ``for a in obs["legal_actions"]``)."""
        if x not in self._without:
            seen, stack = set(self.state) - {x}, [s for s in self.state if s != x]
            while stack:
                for u, ks in self.g.succs.get(stack.pop(), {}).items():
                    if u not in seen and u != x and ks & set(DATA_KINDS):
                        seen.add(u)
                        stack.append(u)
            self._without[x] = seen
        return self._without[x]

    def _pure_candidate(self, nodes, depth: int = 0) -> bool:
        """Some node is computed from a candidate variable and, apart from that candidate, not from
        the state (looking through parameters, whose taint may come from other call sites)."""
        for n in nodes:
            if n.kind == "field" or n.name.startswith("self.") or n not in self.C:
                continue  # persistent attributes are never the alternative under evaluation
            if n not in self._sources:
                self._sources[n] = (self.g.backward_slice([n], DATA_KINDS) | {n}) & self.cands
            if any(n not in self._state_without(x) for x in self._sources[n]):
                return True
            if n.kind == "param" and depth < 4:
                srcs = {u for u, ks in self.g.preds.get(n, {}).items() if ks & {"arg", "iter"}}
                if self._pure_candidate(srcs, depth + 1):
                    return True
        return False

    def _rollouts(self) -> dict[Node, set[Node]]:
        """Closed-loop simulations: inside a loop, a state-like variable is updated additively by a step
        that depends on a candidate from outside the loop (``y += dy`` with ``dy`` toward a candidate
        target), and the loop accumulates time or cost that depends on it (``steps += ...``). Returns
        update -> accumulators. A solver iterating to a converged value accumulates nothing."""
        g, out = self.g, {}
        succ = g.copy_successors()
        seq, changed = set(g.sequence_defs), True  # lists being built up, followed through `plan += ...`
        while changed:
            changed = False
            for o, info in g.ops.items():
                if info.sequence or (info.left_copy | info.right_copy) & seq:
                    new = {d for d in succ.get(o, ()) if d.kind == "def"} - seq
                    seq |= new
                    changed |= bool(new)

        def self_update(o: Node) -> bool:
            """`y += dy` / `y = y + dy` in a loop, where the next iteration's left operand is this
            result (the variable carries its own value), and the variable is not a list being built."""
            info = g.ops[o]
            mine = {d for d in succ.get(o, ()) if d.kind == "def"}
            return bool(info.left_copy & mine) and not (info.left_copy | mine) & seq

        def loops_of(o: Node) -> set[tuple[int, int]]:
            f = g.functions[o.scope]
            return {(lp.line, lp.end_line) for lp in f.loops.values() if lp.line <= o.line <= lp.end_line}

        updates = [o for o, info in g.ops.items() if not info.sequence and o.scope in g.functions and self_update(o)]
        for o in updates:
            info = g.ops[o]
            if o in self.H or not info.left_copy & self.SL or not loops_of(o):
                continue
            own = {v for v in self.cands if v.scope == o.scope and v.line in {lo for lo, _ in loops_of(o)}}
            srcs = (g.backward_slice(info.right, DATA_KINDS) | info.right) & self.cands
            if not srcs - own:  # stepped by the loop's own counter, not toward an outer candidate
                continue
            after = self._within([o], o.scope, EDGE_KINDS)
            accs = {a for a in updates if a != o and a.scope == o.scope and a in after
                    and g.ops[a].symbol.startswith("+") and loops_of(a) & loops_of(o)}
            if accs:
                out[o] = accs
                self.roll_sources[o] = {x.scope for x in srcs - own if o.scope in g.reachable_functions(x.scope)}
        return out

    def _hypothetical(self, o: Node) -> bool:
        """``state ± candidate``: one operand is state-like, the other comes from a candidate only."""
        info = self.g.ops[o]
        if info.sequence:
            return False
        return (bool(info.left_copy & self.SL) and self._pure_candidate(info.right)) or \
               (bool(info.right_copy & self.SL) and self._pure_candidate(info.left))

    # ------------------------------------------------------------------ helpers
    def _site(self, n: Node) -> CallSite | None:
        return self.g.call_sites.get(n)

    def _matches(self, name: str, table) -> str | None:
        """Description if a call name is in a contract table (exact or prefix ending in '.')."""
        for k in table:
            if name == k or (k.endswith(".") and name.startswith(k)):
                return table[k] if isinstance(table, dict) else k
        return None

    def _named(self, name: str, names) -> bool:
        short = name.split(":")[-1].split(".")[-1]
        return any(name == n or name.endswith("." + n) or short == n for n in names)

    def _callback_returns(self, cs: CallSite, role: str) -> set[Node]:
        return {self.g.functions[q].return_node for q in cs.callbacks.get(role, ())
                if self.g.functions[q].return_node is not None}

    def _index_of_extreme(self, cs: CallSite) -> bool:
        """``xs.index(min(xs))``, also with the extreme computed earlier (``m = min(xs); xs.index(m)``)."""
        call = cs.ast_node
        if len(call.args) != 1 or not cs.arg_deps:
            return False
        a = call.args[0]
        if isinstance(a, ast.Call) and isinstance(a.func, ast.Name) and a.func.id in ("min", "max"):
            return True
        recv = self.g.copy_ancestors(cs.recv_deps) | cs.recv_deps
        for n in self.g.copy_ancestors(cs.arg_deps[0]) | cs.arg_deps[0]:
            s = self._site(n) if n.kind == "call" and n.name in EXTREMES else None
            if s and (set().union(set(), *s.arg_deps) | s.recv_deps) & recv:
                return True
        return False

    def _within(self, start, q: str, kinds=DATA_KINDS) -> set[Node]:
        """Forward data slice that may enter callees but never leaves function ``q`` through its own
        return or re-enters it through its parameters (a loop's cycle must close inside the loop)."""
        f = self.g.functions[q]
        stop = {f.return_node, *f.param_nodes.values()} | {n for n in self.by_scope[q] if n.kind == "return"}
        seen: set[Node] = set()
        stack = list(start)
        while stack:
            for u, ks in self.g.succs.get(stack.pop(), {}).items():
                if u not in seen and u not in stop and ks & set(kinds):
                    seen.add(u)
                    stack.append(u)
        return seen

    def _relaxes_from_itself(self, fr, q: str) -> bool:
        """The stored candidate costs are computed from earlier entries of the same cost table
        (directly, ``cost[u] + w``, or through earlier layers, ``prev = costs[-1]``)."""
        if fr.container in fr.value_roots:
            return True
        f = self.g.functions[q]
        stop = set(f.param_nodes.values())
        start = [n for n in self.g.scope_defs.get(q, ()) if n.name in fr.value_roots]
        seen, stack = set(start), list(start)
        while stack:
            v = stack.pop()
            if v.name == fr.container or v.name == f"self.{fr.container}":
                return True
            for u, ks in self.g.preds.get(v, {}).items():
                if u not in seen and u not in stop and ks & set(DATA_KINDS) and u.scope == q:
                    seen.add(u)
                    stack.append(u)
        return False

    def _nearest_prediction(self, scores: set[Node], candidates: set[Node]) -> Node | None:
        """The prediction closest to a choice's scores (through value flow, then any dependence)."""
        for kinds in (set(DATA_KINDS), set(EDGE_KINDS)):
            seen, q = set(scores), deque(scores)
            while q:
                v = q.popleft()
                if v in candidates:
                    return v
                for u, ks in self.g.preds.get(v, {}).items():
                    if u not in seen and ks & kinds:
                        seen.add(u)
                        q.append(u)
        return None

    def _influence(self, start, goals: set[Node] | None = None, within: set[Node] | None = None) -> str:
        """Shortest dependence path from the evidence to the action (or to ``goals``), as labels."""
        goals, within = goals or {self.sink}, within or self.slice
        start = [s for s in start if s in within]
        prev: dict[Node, tuple[Node, set[str]]] = {}
        seen, q, end = set(start), deque(start), None
        while q:
            v = q.popleft()
            if v in goals:
                end = v
                break
            for u, ks in self.g.succs.get(v, {}).items():
                if u in within and u not in seen:
                    seen.add(u)
                    prev[u] = (v, ks)
                    q.append(u)
        if end is None:
            return ""
        path, kinds, v = [end], set(), end
        while v in prev:
            v, ks = prev[v]
            kinds |= ks
            path.append(v)
        path.reverse()
        labels = [n.label() for n in path]
        if len(labels) > 7:
            labels = labels[:3] + ["..."] + labels[-3:]
        return " -> ".join(labels) + f"  [{', '.join(sorted(kinds))}]"

    # ------------------------------------------------------------------ choices
    def _choices(self, region: set[Node]) -> list[_Choice]:
        g, out = self.g, []
        for n in region:
            if n.kind != "call" or (cs := self._site(n)) is None:
                continue
            name, scores, optimiser = n.name, None, False
            if name in SELECTION_APIS:
                if name.startswith("method:"):
                    scores = set(cs.recv_deps)
                elif name.startswith("heapq."):
                    scores = set(cs.arg_deps[1]) if len(cs.arg_deps) > 1 else set()
                else:
                    scores = set(cs.arg_deps[0]) if cs.arg_deps else set()
                scores |= self._callback_returns(cs, "key")
            elif name in KEYED_SELECTION and (cs.callees == () and _compares_alternatives(cs.ast_node)):
                if "key" in cs.kw_deps:
                    scores = self._callback_returns(cs, "key") or set(cs.kw_deps["key"])
                else:
                    scores = set().union(set(), *cs.arg_deps)
            elif name == "method:index" and self._index_of_extreme(cs):
                scores = set(cs.recv_deps)
            elif name in OPTIMISERS:
                scores, optimiser = self._callback_returns(cs, "objective"), True
            if scores is None:
                continue
            label = name.replace("method:", ".")
            clamp = name in ("min", "max") and len(cs.ast_node.args) >= 2 and "key" not in cs.kw_deps
            out.append(_Choice(label, n.scope, n.file, n.line, n, {n}, scores, optimiser, clamp))
        scopes = {n.scope for n in region}
        for q in scopes:
            f = g.functions.get(q)
            if f is None:
                continue
            defs = g.scope_defs.get(q, set())
            for loop in f.loops.values():
                for bu in loop.best_updates:
                    at = set(bu.stmts)
                    mine = [d for d in defs if (d.line, d.col) in at]
                    chosen = {d for d in mine if d.name in bu.chosen}
                    winners = chosen | {d for d in mine if d.name == bu.var}  # the best may hold the winner
                    if not winners & region:
                        continue
                    scores = set(g.test_deps.get((q, bu.line, bu.col), set()))
                    out.append(_Choice(f"best-so-far loop over {bu.var}", q, f.file, bu.line, None, winners, scores))
        return out

    def _predictions(self, ch: _Choice) -> tuple[list[Node], list[Node], list[Node]]:
        """(arithmetic hypothetical outcomes, transition-model calls, closed-loop rollouts) that the
        choice's scores depend on. A rollout counts when its accumulated time/cost reaches the scores."""
        if not ch.scores & self.H_fwd and not self.cfg.transition_models:
            return [], [], []
        ssl = self.g.backward_slice(ch.scores) | ch.scores
        ops = sorted(ssl & self.H, key=lambda n: (n.file, n.line))
        models = sorted((n for n in ssl if n.kind == "call" and self.cfg.transition_models
                         and self._named(n.name, self.cfg.transition_models)), key=lambda n: (n.file, n.line))
        rolls = []
        if self.H_roll and ssl & set(self.H_roll):
            data = self.g.backward_slice(ch.scores, DATA_KINDS) | ch.scores
            loops = {o: [(lp.line, lp.end_line) for lp in self.g.functions[o.scope].loops.values()
                         if lp.line <= o.line <= lp.end_line] for o in self.H_roll}
            rolls = sorted((o for o, accs in self.H_roll.items() if accs & data  # not a choice inside the rollout
                            and not (ch.function == o.scope and any(lo <= ch.line <= hi for lo, hi in loops[o]))
                            and ch.function in self.roll_sources[o]  # the choice's candidates drive the rollout
                            and not ch.clamp),  # max(a, b) of two values is not a choice among candidates
                           key=lambda n: (n.file, n.line))
        return ops, models, rolls

    def _encodes(self, winners: set[Node]) -> bool:
        """The action is the winner under a state-independent transformation: nothing on the way
        from the winner to the returned value combines it with a state-derived value."""
        g = self.g
        winners = (set(winners) & self.slice) or set(winners)  # the values the action is computed from
        P = (g.forward_slice(winners) & self.slice) | set(winners)
        for v in P - winners:
            if v.kind == "param":  # binding, not computing (other call sites do not combine)
                continue
            cs = self._site(v) if v.kind == "call" else None
            inner = cs is not None and cs.resolution == "project"  # its body is checked through its return
            for u, ks in g.preds.get(v, {}).items():
                if u in P or not ks & {"data", "ret", "iter"} or (u, v) in g.copies or (inner and "ret" not in ks):
                    continue
                if u in self.S:
                    return False
        return True

    # ------------------------------------------------------------------ evidence
    def _planner_calls(self, region: set[Node]) -> list[Evidence]:
        table = {**PLANNERS, **self.cfg.planners}
        out = []
        for n in sorted((n for n in region if n.kind == "call"), key=lambda n: (n.file, n.line)):
            what = self._matches(n.name, table)
            if what:
                out.append(Evidence("planner-call", f"{n.name} ({what})", n.scope, n.file, n.line, RULE_PLAN,
                                    nodes=(n,), sites=[("planner", n.file, n.line)],
                                    assumptions=[f"contract: {n.name} searches for and returns a {what.split(' (')[0]}"
                                                 " result"]))
        return out

    def _transition_calls(self, region: set[Node]) -> list[Evidence]:
        if not self.cfg.transition_models:
            return []
        return [Evidence("transition-model", f"{n.name} (configured transition model) predicts outcomes used for "
                         "the action", n.scope, n.file, n.line, RULE_LOOKAHEAD, nodes=(n,),
                         sites=[("prediction", n.file, n.line)],
                         assumptions=["configured: this call predicts the next state"])
                for n in region if n.kind == "call" and self._named(n.name, self.cfg.transition_models)]

    def _graph_searches(self, region: set[Node]) -> list[Evidence]:
        g, out = self.g, []
        ast_calls = {id(cs.ast_node): cs.node for cs in g.call_sites.values()}
        for f in g.functions.values():
            for loop in f.loops.values():
                if not loop.frontiers:
                    continue
                inside = {n for n in self.by_scope[f.qualname] if loop.line <= n.line <= loop.end_line}
                if not inside & region:
                    continue
                for fr in loop.frontiers:
                    if fr.kind == "worklist":
                        pops = {ast_calls[id(c)] for c in fr.pops if id(c) in ast_calls}
                        pushes = {ast_calls[id(c)] for c in fr.pushes if id(c) in ast_calls}
                        if not self._within(pops, f.qualname) & pushes:
                            continue
                        what = (f"graph search: worklist `{fr.container}` is popped and refilled with successors of "
                                f"the popped element, with visited/cost table {', '.join(f'`{c}`' for c in fr.closed)}")
                    elif fr.kind == "relaxation":
                        if any(lp.line <= loop.line <= lp.end_line and lp is not loop
                               and any(x.kind != "relaxation" for x in lp.frontiers) for lp in f.loops.values()):
                            continue  # the relaxation step of a worklist search already reported
                        if not self._relaxes_from_itself(fr, f.qualname):
                            continue
                        what = (f"graph search: entries of cost table `{fr.container}` are relaxed with candidates "
                                f"computed from earlier costs, recording predecessors in "
                                f"{', '.join(f'`{c}`' for c in fr.closed)} (shortest-path dynamic programming)")
                    else:
                        lo, hi = fr.inner
                        nxt = {n for n in inside if n.kind == "def" and n.name == fr.next_layer and lo <= n.line <= hi}
                        cur = {n for n in inside if n.kind == "def" and n.name == fr.container and not lo <= n.line <= hi}
                        if not nxt or not self._within(nxt, f.qualname) & cur:
                            continue
                        what = (f"graph search: each element of layer `{fr.container}` adds its successors to "
                                f"`{fr.next_layer}`, which becomes the next layer")
                    out.append(Evidence("graph-search", what, f.qualname, f.file, loop.line, RULE_PLAN,
                                        nodes=tuple(inside & region), sites=[("search loop", f.file, loop.line)],
                                        assumptions=["the loop is read as a search over states or locations "
                                                     "(a perception flood fill would look the same)"]))
                    break
        for n in sorted((n for n in region if n.kind == "call" and n.name in WAVEFRONT_OPS), key=lambda n: n.line):
            if n.scope in g.functions and n in self._within([n], n.scope):  # dilated again on a later iteration
                out.append(Evidence("graph-search", f"wavefront expansion: {n.name.split('.')[-1]} is applied "
                                    "repeatedly to the set it has reached (grid BFS / arrival times)", n.scope, n.file,
                                    n.line, RULE_PLAN, nodes=(n,), sites=[("expansion", n.file, n.line)],
                                    assumptions=["repeated dilation of a reached set is read as a wavefront "
                                                 "search (iterated smoothing would look the same)"]))
        return out

    def _tree_searches(self, region: set[Node], choices: list[_Choice]) -> list[Evidence]:
        g, out = self.g, []
        rec = g.recursive_functions()
        for q in sorted(rec):
            f = g.functions[q]
            inside = set(self.by_scope[q])
            if not inside & region:
                continue
            sites = [cs for cs in f.call_sites.values()
                     if any(c in rec and q in g.reachable_functions(c) for c in cs.callees)]
            if not sites:
                continue
            looped = _calls_in_iteration(f.node)
            if len(sites) < 2 and not any(id(cs.ast_node) in looped for cs in sites):
                self._note(region, "recursion", f"{q.split('.')[-1]} recurses on one branch only (no search over "
                           "alternatives)", f.file, sites[0].node.line, q)
                continue
            rec_nodes = {cs.node for cs in sites}
            reach = g.reachable_functions(q)  # the selection may sit in a helper the recursion calls
            alts = g.forward_slice({v for v in g.iter_vars if v.scope == q}, DATA_KINDS)
            results = g.forward_slice(rec_nodes, DATA_KINDS) | rec_nodes
            selected = any(ch.function in reach and (g.backward_slice(ch.scores) | ch.scores) & (rec_nodes | alts)
                           for ch in choices)
            tested = any(deps & results for (sc, _, _), deps in g.test_deps.items() if sc == q) or \
                any(deps & alts for key, deps in g.test_deps.items() if key[0] in reach and key in g.ordering_tests)
            if not (selected or tested):
                self._note(region, "recursion", f"{q.split('.')[-1]} branches recursively but never compares "
                           "the branches' results", f.file, sites[0].node.line, q)
                continue
            how = "selects among the results" if selected else "compares the results of its branches"
            out.append(Evidence("tree-search", f"tree search: {q.split('.')[-1]} recurses over alternatives and {how}",
                                q, f.file, sites[0].node.line, RULE_PLAN, nodes=tuple(inside & region),
                                sites=[("recursive call", f.file, cs.node.line) for cs in sites[:3]]))
        return out

    def _generate_and_test(self, region: set[Node]) -> list[Evidence]:
        """Candidates ranked by cost are tried in order and the first that passes a feasibility check
        is returned, where the check walks along the candidate (a plan: ``for i in range(len(path) - 1)``)."""
        g, out = self.g, []
        for q, f in g.functions.items():
            if f.is_lambda or not set(self.by_scope[q]) & region:
                continue
            for s in _walk(f.node.body, into_loops=True):
                if not isinstance(s, (ast.For, ast.AsyncFor)):
                    continue
                lv = {v for v in g.iter_vars if v.scope == q and v.line == s.lineno}
                src = {u for v in lv for u, ks in g.preds.get(v, {}).items() if "iter" in ks}
                ranked = [n for n in g.backward_slice(src, DATA_KINDS) | src
                          if n.kind == "call" and n.scope == q and n.name in RANKERS]
                if not lv or not ranked:
                    continue
                cand = self._within(lv, q) | lv
                for n in _walk(s.body, into_loops=False):
                    if not isinstance(n, ast.If):
                        continue
                    rets = [r for r in _walk(n.body, into_loops=False) if isinstance(r, ast.Return) and r.value]
                    tdeps = g.test_deps.get((q, n.lineno, n.col_offset), set())
                    checks = [c for c in tdeps if c.kind == "call" and (cs := self._site(c)) and cs.callees
                              and set().union(set(), *cs.arg_deps) & cand and set().union(set(), *cs.arg_deps) & self.S
                              and self._walks_along(cs, cand)]
                    returned = {d for d in g.scope_defs.get(q, ()) if d.name == "<return>"
                                and any(d.line == r.lineno for r in rets)} & cand & region
                    if checks and returned:
                        c = checks[0]
                        out.append(Evidence("generate-and-test", f"generate-and-test: candidates ranked by "
                                            f"{ranked[0].name.replace('method:', '.')} are tried in order and the first "
                                            f"that passes {c.name.rsplit('.', 1)[-1]} is returned", q, f.file,
                                            s.lineno, RULE_PLAN, nodes=tuple(returned), winners=tuple(returned),
                                            sites=[("ranking", ranked[0].file, ranked[0].line),
                                                   ("feasibility check", c.file, c.line)],
                                            assumptions=[f"{c.name.rsplit('.', 1)[-1]} checks a candidate plan by "
                                                         "walking along it"]))
                        break
        return out

    def _walks_along(self, cs: CallSite, cand: set[Node]) -> bool:
        """The checking function (or one it calls) iterates over the elements of the argument that
        receives the candidate (a path's waypoints or segments), not over other inputs."""
        for callee in cs.callees:
            info = self.g.functions[callee]
            params = info.params[1:] if info.is_method else info.params
            got = {info.param_nodes[p] for p, d in zip(params, cs.arg_deps) if p in info.param_nodes and d & cand}
            succ, base, stack = self.g.copy_successors(), set(got), list(got)
            while stack:  # the candidate itself, passed on unchanged
                for v in succ.get(stack.pop(), ()):
                    if v not in base:
                        base.add(v)
                        stack.append(v)
            lens = {n for n, cs2 in self.g.call_sites.items() if n.name == "len" and set().union(set(), *cs2.arg_deps) & base}
            reach = base | self.g.forward_slice(lens, DATA_KINDS) | lens  # ... or range(len(candidate))
            for fq in self.g.reachable_functions(callee):
                for v in self.g.iter_vars:
                    if v.scope == fq and any("iter" in ks and u in reach for u, ks in self.g.preds.get(v, {}).items()):
                        return True
        return False

    def _ordering_searches(self, choices: list[_Choice]) -> list[Evidence]:
        out = []
        for ch in choices:
            if not ch.winners & self.slice:
                continue
            anc = self.g.copy_ancestors(ch.winners) | ch.winners
            perms = sorted((n for n in anc if n.kind == "call" and n.name == "itertools.permutations"),
                           key=lambda n: n.line)
            if perms:
                p = perms[0]
                out.append(Evidence("ordering-search", f"task-order search: {ch.what} selects one of the orderings "
                                    "enumerated by itertools.permutations", ch.function, ch.file, ch.line, RULE_PLAN,
                                    nodes=(p, *ch.winners), winners=tuple(ch.winners),
                                    sites=[("orderings", p.file, p.line), ("choice", ch.file, ch.line)],
                                    assumptions=["exhaustive search over orderings counts as task planning; "
                                                 "how orderings are scored is not judged"]))
        return out

    def _lookaheads(self, choices: list[_Choice], region: set[Node], record: bool) -> list[Evidence]:
        out = []
        rejected: list[_Choice] = []
        for ch in choices:
            if not ch.winners & region:
                continue
            ops, models, rolls = self._predictions(ch)
            if not ops and not models and not rolls:
                if record:
                    self._unpredicted_choice(ch)
                continue
            if not models and not rolls and region is self.slice and not self._encodes(ch.winners):
                rejected.append(ch)
                continue
            strong = models or rolls  # predictions that need no action-encoding check
            pred = self._nearest_prediction(ch.scores, set(strong or ops)) or (strong or ops)[0]
            text = pred.name if models else self.g.ops[pred].text
            rollout = bool(rolls) or (bool(ops) and pred in self.g.forward_slice([pred], DATA_KINDS))
            kind = "multi-step rollout" if rollout else "look-ahead"
            what = (f"{'optimisation' if ch.optimiser else kind}: candidates are scored by the predicted outcome "
                    f"`{text}` and chosen by {ch.what}")
            if models:
                assumptions = [f"configured transition model: {pred.name}"]
            elif rolls:
                accs = ", ".join(sorted({f"`{self.g.ops[a].text}`" for a in self.H_roll[pred]})[:2])
                assumptions = [f"`{text}` steps a simulated state toward the candidate inside a loop that "
                               f"accumulates {accs} (a closed-loop rollout); the chosen candidate may be a target"]
            else:
                assumptions = [f"`{text}` is read as the state after applying a candidate (additive transition)",
                               "the chosen candidate becomes the action through a state-independent encoding"]
            to_choice = self._influence([pred], set(ch.scores), self.g.backward_slice(ch.scores) | ch.scores)
            out.append(Evidence("lookahead", what, ch.function, ch.file, ch.line, RULE_LOOKAHEAD,
                                influence=f"prediction to scores: {to_choice}; chosen value to action: " if to_choice
                                else "",
                                nodes=tuple(ch.winners), winners=tuple(ch.winners),
                                sites=[("prediction", pred.file, pred.line), ("choice", ch.file, ch.line),
                                       ("action", self.sink.file, self.sink.line)],
                                assumptions=assumptions))
        if record:
            used = set().union(set(), *(self.g.backward_slice(e.winners) for e in out))
            for ch in rejected:
                if not ch.winners & used:
                    self.notes.append(Issue("target-choice", f"{ch.what} ranks candidates by a predicted relation to "
                                            "the state, but the action is then computed from the chosen candidate and "
                                            "the current state (choosing a target, not an action)",
                                            ch.file, ch.line, ch.function))
        return out

    def _unpredicted_choice(self, ch: _Choice) -> None:
        """A choice that reaches the action without predicted outcomes: note it, and ask for review
        when its scores come from an opaque call that receives both a candidate and the state."""
        ssl = self.g.backward_slice(ch.scores) | ch.scores
        for n in sorted((n for n in ssl if n.kind == "call"), key=lambda n: n.line):
            cs = self._site(n)
            if cs is None or cs.resolution not in OPAQUE or self._named(n.name, self.cfg.reactive_scorers):
                continue
            short = n.name.split(":")[-1].split(".")[-1]
            if short in ACCESSOR_METHODS or short.startswith(("get", "is_", "has_", "_get")):
                continue
            inputs = set().union(cs.recv_deps, *cs.arg_deps, *cs.kw_deps.values())
            if inputs & self.C and inputs & self.S:
                self.review.append(Issue("opaque-scorer", f"{ch.what} scores candidates with `{n.name}`, which is "
                                         "not analysed and receives both a candidate and the state; it may be a "
                                         "transition model (configure transition_models or reactive_scorers)",
                                         n.file, n.line, n.scope))
                return
        what = "the optimiser's objective predicts no outcome of the decision variable (static solve)" \
            if ch.optimiser else "candidates are ranked without a recognised predicted outcome (action ranking only)"
        via = sorted({n.name.rsplit(".", 1)[-1] for n in ssl if n.kind == "call" and (cs := self._site(n))
                      and cs.resolution == "project" and set().union(set(), *cs.arg_deps) & self.C
                      and set().union(set(), *cs.arg_deps) & self.S})
        if via:
            what += (f"; scored through {', '.join(via[:3])}, which receive the candidate and the state "
                     "(configure transition_models if one predicts outcomes)")
        self.notes.append(Issue("ranking", f"{ch.what}: {what}", ch.file, ch.line, ch.function))

    def _note(self, region: set[Node], kind: str, what: str, file: str, line: int, function: str) -> None:
        if region is self.slice:
            self.notes.append(Issue(kind, what, file, line, function))

    def _evidence(self, region: set[Node], record: bool) -> list[Evidence]:
        choices = self._choices(region)
        all_choices = choices if region is self.all_nodes else self._choices(self.all_nodes)
        ev = (self._planner_calls(region) + self._transition_calls(region) + self._graph_searches(region)
              + self._tree_searches(region, all_choices) + self._ordering_searches(choices)
              + self._generate_and_test(region)
              + self._lookaheads(choices, region, record))
        seen, out = set(), []
        for e in ev:
            key = (e.kind, e.what, e.file, e.line)
            if key not in seen:
                seen.add(key)
                out.append(e)
        return out

    # ------------------------------------------------------------------ review
    def _review(self, global_sites: list[Evidence]) -> None:
        g = self.g
        calls = sorted((n for n in self.slice if n.kind == "call"), key=lambda n: (n.file, n.line))
        reachable = g.reachable_functions(self.decision)
        planning_fns = {e.function for e in global_sites}
        for n in calls:
            cs = self._site(n)
            if cs is None:
                continue
            short = n.name.split(":")[-1].split(".")[-1]
            if cs.resolution == "unresolved-import":
                self.review.append(Issue("unresolved-import", f"`{n.name}` comes from a module that was not found; "
                                         "its code was not analysed", n.file, n.line, n.scope))
            elif cs.resolution == "library" and self._matches(n.name, {k: k for k in GENERIC_SOLVERS}):
                self.review.append(Issue("solver-role", f"`{n.name}` is a general solver; whether it plans depends "
                                         "on the model it is given", n.file, n.line, n.scope))
            elif cs.resolution in OPAQUE and _planner_like(short) and \
                    not self._named(n.name, self.cfg.reactive_scorers):
                self.review.append(Issue("planner-like-call", f"`{n.name}` is not resolved and is named like a "
                                         "planner", n.file, n.line, n.scope))
            elif cs.resolution in ("dynamic", "unresolved-name") and planning_fns - reachable:
                self.review.append(Issue("dynamic-call", f"the target of `{ast.unparse(cs.ast_node.func)[:50]}` is not "
                                         f"known statically; planning code elsewhere ({', '.join(sorted(planning_fns - reachable))[:120]}) "
                                         "could be what it calls", n.file, n.line, n.scope))
            elif cs.resolution == "method":
                owners = [ci.methods[short] for ci in g.classes.values() if short in ci.methods]
                planners = [o for o in owners if g.reachable_functions(o) & planning_fns]
                if planners:
                    self.review.append(Issue("ambiguous-method", f"`.{short}()` is called on an object of unknown "
                                             f"type and could be {', '.join(planners)}, which plans",
                                             n.file, n.line, n.scope))
        for n, text in g.unresolved_callbacks.items():
            if n in self.slice:
                self.review.append(Issue("unresolved-callback", f"the function passed to `{n.name}` (`{text}`) could "
                                         "not be resolved", n.file, n.line, n.scope))
        if g.entrypoint_basis.get(self.decision) == "generic name":
            self.review.append(Issue("entrypoint", f"the decision function was found by the generic name "
                                     f"`{self.fn.node.name}`; confirm it returns the policy's action",
                                     self.fn.file, self.fn.node.lineno, self.decision))
        for file, msg in g.parse_errors:
            self.review.append(Issue("parse-error", f"an imported module could not be parsed ({msg}) and was skipped",
                                     file))

    # ------------------------------------------------------------------ run
    def run(self) -> Report:
        g = self.g
        self.all_nodes = set(g.nodes)
        evidence = self._evidence(self.slice, record=True)
        global_sites = self._evidence(self.all_nodes, record=False)
        relevant = {(e.kind, e.file, e.line) for e in evidence}
        for e in global_sites:
            if (e.kind, e.file, e.line) not in relevant and not set(e.nodes) & self.slice:
                self.notes.append(Issue("not-action-relevant", f"{e.kind} at {Path(e.file).name}:{e.line} does not "
                                        "influence the returned action (discarded, unreachable from it, or unrelated)",
                                        e.file, e.line, e.function))
        for n in sorted((n for n in self.slice if n.kind == "call" and n.name in ENUMERATORS), key=lambda n: n.line):
            if not any(e.kind == "ordering-search" and n in e.nodes for e in evidence):
                self.notes.append(Issue("enumeration", f"{n.name} enumerates {ENUMERATORS[n.name]}, but no evaluation "
                                        "of their consequences selects one: enumeration alone is not planning",
                                        n.file, n.line, n.scope))
        for e in evidence:
            e.influence += self._influence(e.winners or e.nodes)
        planned_in = {e.function for e in evidence}  # choices that are part of a search already reported
        self.notes = [i for i in self.notes if not (i.kind in ("ranking", "target-choice") and i.function in planned_in)]
        self._review(global_sites)
        review = _dedupe_issues(self.review)
        if evidence:
            self.notes += [Issue(i.kind, f"{i.what} (does not affect the planning label)", i.file, i.line, i.function)
                           for i in review]
            review = []
        status = "needs_review" if review else "supported"
        planning = True if evidence else (None if review else False)
        return Report(decision=self.decision, planning=planning, evidence=evidence, pruned=list(g.pruned),
                      status=status, review_reasons=review, notes=_group_issues(self.notes),
                      entrypoint=g.entrypoint_basis.get(self.decision, "explicit"), coverage=self._coverage())

    def _coverage(self) -> dict:
        g = self.g
        counts: dict[str, int] = defaultdict(int)
        for n in self.slice:
            if n.kind == "call" and (cs := self._site(n)) is not None:
                counts[cs.resolution] += 1
        return {"modules": sorted(g.modules), "unresolved_imports": [list(u) for u in g.unresolved_imports],
                "parse_errors": [list(p) for p in g.parse_errors], "action_slice_calls": dict(sorted(counts.items())),
                "state_sources": sorted(n.label() for n in self.state)}


def _group_issues(issues: list[Issue]) -> list[Issue]:
    """One issue per (kind, text), located at its first occurrence, with a count of the others."""
    groups: dict[tuple[str, str], list[Issue]] = {}
    for i in _dedupe_issues(issues):
        groups.setdefault((i.kind, i.what), []).append(i)
    out = []
    for (kind, what), items in groups.items():
        items.sort(key=lambda i: (i.file, i.line))
        first = items[0]
        extra = f" (and {len(items) - 1} more: lines {', '.join(str(i.line) for i in items[1:6])}" \
                f"{', ...' if len(items) > 6 else ''})" if len(items) > 1 else ""
        out.append(Issue(kind, what + extra, first.file, first.line, first.function))
    return out


def _dedupe_issues(issues: list[Issue]) -> list[Issue]:
    seen, out = set(), []
    for i in issues:
        key = (i.kind, i.what, i.file, i.line)
        if key not in seen:
            seen.add(key)
            out.append(i)
    return out
