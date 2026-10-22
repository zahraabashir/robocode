"""Dependency graph of Python source code: what every value is computed from.

General purpose (no assumptions about robots or policies) and standard library only.
Given files or directories, it builds a flow-sensitive, inter-procedural program
dependence graph:

- Nodes are value sites: a variable at the line where it is assigned (``def``), a
  function parameter (``param``) or return value (``return``), an object attribute
  that persists between calls (``field``, e.g. ``self.plan``), a module global
  (``global``), each call site (``call``), and each ``+``/``-`` (``op``) so that the
  two operands of an additive update stay apart (see ``ops``).
- Edges say "computed from": ``data`` (read in the expression), ``control`` (read in
  an enclosing ``if``/``while`` test or ``for`` iterable, or in a test whose earlier
  ``return``/``break``/``continue``/``raise`` decides whether a statement runs),
  ``arg`` (call argument -> callee parameter), ``ret`` (callee return -> call site),
  ``field_write`` (assignment -> persistent attribute), ``base`` (old value kept by an
  in-place update such as ``x[i] = v`` or ``x.append(v)``), and ``iter`` (iterable ->
  the loop, comprehension or callback variable bound to each of its elements).
- Copies: the subset of edges along which a value passes *unchanged* (assignment,
  indexing, unpacking, returning, argument binding, conversions such as ``int`` or
  ``np.array``), as opposed to being computed from (``a + b``, ``f(a)``). Kept in
  ``copies``.

Flow sensitivity: each assignment is its own node and reaching definitions are
propagated through branches and loops (to a fixpoint), so a reused name does not
merge unrelated values. Statements after an unconditional ``return``/``raise``/
``break``/``continue`` and bodies of loops or branches whose test is a constant false
(including attributes that only ever hold one literal) are not analysed at all.

Inter-procedural: calls to functions defined in the analysed code link arguments to
parameters and returns to call sites (context-insensitive). Function values are
tracked: lambdas and nested functions are analysed as functions, a variable or
attribute holding a function resolves to it (``planner = plan; planner(x)``), and
known higher-order library functions bind their callbacks (``min/max/sorted(key=f)``,
``map``, ``filter``, ``scipy.optimize`` objectives). Calls into libraries become
``call`` nodes named by their imported qualified name (e.g.
``scipy.sparse.csgraph.dijkstra``); each call site records how it was resolved, so
unresolved code is visible rather than silently treated as absent.

Persistent attributes share one ``field`` node per attribute and class family, named
by the fully qualified root class (``field:pkg.mod.Policy.plan``), so unrelated classes
with the same short name never share state.

Known approximations: no type inference (calls on arbitrary objects are recorded by
method name, or resolved by a method name unique among the classes of the modules the
caller imports), no alias analysis of mutable objects, containers are tracked as whole
values (except tuples unpacked from a tuple literal or a function that always returns
one), closures see the variables reaching their definition, and exceptions are
approximated (a handler may start from the state before or after the ``try`` body).

Usage::

    from depgraph import build_graph
    g = build_graph(["path/to/approach.py"])      # modules it imports are followed
    print(g.summary())
"""

from __future__ import annotations

import ast
import builtins
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Iterator

EDGE_KINDS = ("data", "control", "arg", "ret", "field_write", "base", "iter")
DATA_KINDS = ("data", "arg", "ret", "field_write", "base", "iter")  # value flow, without control

# In-place mutators: x.m(args) changes x, so x gets a new (weak) definition.
MUTATING_METHODS = frozenset({
    "append", "appendleft", "extend", "extendleft", "insert", "add", "update", "pop",
    "popleft", "popitem", "remove", "discard", "clear", "sort", "reverse", "setdefault",
    "fill", "put", "put_nowait", "push", "resize", "itemset",
})
# Calls whose result is their first argument's value, converted or copied.
COPY_CALLS = frozenset({"int", "float", "list", "tuple", "copy.copy", "copy.deepcopy", "numpy.array",
                        "numpy.asarray", "numpy.float32", "numpy.float64", "numpy.copy", "method:copy"})
# Method calls whose result is (part of) their receiver: ``d.get(k)``, ``x.reshape(...)``.
RECEIVER_PART_CALLS = frozenset({"method:get", "method:item", "method:tolist", "method:astype", "method:reshape",
                                 "method:flatten", "method:ravel", "method:squeeze", "method:values", "method:keys",
                                 "method:items", "method:view"})
# Calls whose result is one of their arguments (or one of its elements).
SELECTING_CALLS = frozenset({"min", "max", "sorted", "reversed", "heapq.nsmallest", "heapq.nlargest"})
# Library functions that mutate their first argument.
FIRST_ARG_MUTATORS = frozenset({
    "heapq.heappush", "heapq.heappop", "heapq.heapify", "heapq.heapreplace",
    "heapq.heappushpop", "random.shuffle", "numpy.random.shuffle", "numpy.copyto",
    "numpy.put", "numpy.place", "numpy.fill_diagonal",
})
# Library functions that call a function argument. ``key=`` callbacks receive elements of
# the iterable arguments; ``map``/``filter`` callbacks receive elements of the iterables;
# optimiser objectives receive candidate values of the decision variable (from ``x0``).
KEY_CALLBACK_CALLS = frozenset({"min", "max", "sorted", "method:sort", "heapq.nsmallest", "heapq.nlargest"})
ELEMENT_CALLBACK_CALLS = frozenset({"map", "filter"})
OPTIMISERS = frozenset({
    "scipy.optimize.minimize", "scipy.optimize.minimize_scalar", "scipy.optimize.least_squares",
    "scipy.optimize.differential_evolution", "scipy.optimize.dual_annealing", "scipy.optimize.basinhopping",
    "scipy.optimize.shgo", "scipy.optimize.brute", "scipy.optimize.direct", "scipy.optimize.fmin",
    "scipy.optimize.fmin_powell", "scipy.optimize.fmin_cg", "scipy.optimize.fmin_bfgs",
    "scipy.optimize.fmin_l_bfgs_b", "scipy.optimize.fmin_tnc", "scipy.optimize.fmin_slsqp",
})

BUILTIN_NAMES = frozenset(dir(builtins))
_STDLIB_FALLBACK = {"abc", "argparse", "array", "ast", "bisect", "collections", "contextlib", "copy",
                    "dataclasses", "datetime", "enum", "functools", "heapq", "inspect", "io", "itertools",
                    "json", "logging", "math", "operator", "os", "pathlib", "pickle", "queue", "random", "re",
                    "statistics", "string", "sys", "time", "typing", "warnings", "weakref"}
STDLIB_MODULES = frozenset(getattr(sys, "stdlib_module_names", ()) or _STDLIB_FALLBACK)
# Third-party packages treated as libraries (their calls are named, not reported as
# missing project code). Extend per corpus with ``build_graph(..., libraries=...)``.
KNOWN_LIBRARIES = frozenset({
    "numpy", "scipy", "networkx", "torch", "jax", "jaxlib", "tensorflow", "keras", "sklearn", "pandas",
    "matplotlib", "cv2", "PIL", "skimage", "shapely", "trimesh", "open3d", "numba", "einops", "tqdm", "yaml",
    "omegaconf", "hydra", "gym", "gymnasium", "pybullet", "pybullet_planning", "mujoco", "pymunk", "pygame",
    "Box2D", "ompl", "pydrake", "ortools", "cvxpy", "pulp", "casadi", "pyomo", "gurobipy", "transforms3d",
    "pytransform3d", "spatialmath", "roboticstoolbox", "kinder", "prpl_utils", "relational_structs",
    "robocode",
})


@dataclass(frozen=True)
class Node:
    """A value site in the program."""

    kind: str  # def | param | return | field | global | call | op
    name: str  # variable, attribute or callee name; "+"/"-"/"+="/"-=" for op
    scope: str = ""  # qualified name of the enclosing function ("" for field/global)
    file: str = ""
    line: int = 0
    col: int = 0
    detail: str = ""  # e.g. "[idx]" for an element update, ".weak" for in-place updates

    def label(self) -> str:
        """Short human-readable form, e.g. ``move@150`` or ``field:pkg.Policy.plan``."""
        if self.kind in ("field", "global"):
            return f"{self.kind}:{self.name}"
        if self.kind == "param":
            return f"param:{self.scope.rsplit('.', 1)[-1]}.{self.name}"
        if self.kind == "return":
            return f"{self.name}:{self.scope}"
        if self.kind == "call":
            return f"call:{self.name}@{self.line}"
        if self.kind == "op":
            return f"op{self.name}@{self.line}"
        return f"{self.name}{self.detail}@{self.line}"


@dataclass
class OpInfo:
    """An additive operation ``left + right`` / ``left - right`` (or ``left += right``)."""

    symbol: str
    text: str = ""
    sequence: bool = False  # an operand is a list/tuple/string literal: concatenation, not arithmetic
    left: set[Node] = field(default_factory=set)  # what each operand is computed from
    right: set[Node] = field(default_factory=set)
    left_copy: set[Node] = field(default_factory=set)  # values each operand *is* (passed unchanged)
    right_copy: set[Node] = field(default_factory=set)


@dataclass
class CallSite:
    """One call expression."""

    node: Node
    callee: str | None  # project function qualname, if resolved (the first, if several)
    external: str | None  # library / unresolved name otherwise
    function: str  # caller qualname
    ast_node: ast.Call
    loop_depth: int
    by_name: bool = False  # callee resolved only by its (unique) method name
    callees: tuple[str, ...] = ()  # every project function the call may run
    # project | builtin | library | method (unknown receiver) | dynamic | unresolved-name | unresolved-import
    resolution: str = ""
    arg_deps: list[set[Node]] = field(default_factory=list)
    kw_deps: dict[str, set[Node]] = field(default_factory=dict)
    recv_deps: set[Node] = field(default_factory=set)
    callbacks: dict[str, tuple[str, ...]] = field(default_factory=dict)  # role (key/map/objective) -> functions


@dataclass
class BestUpdate:
    """``if c < best: best = c; choice = a``: a comparison and the assignments in its branch."""

    line: int
    col: int
    end_line: int
    var: str  # the running best: compared and reassigned
    chosen: list[str]  # the other variables assigned in that branch (the winners)
    stmts: list[tuple[int, int]]  # (line, col) of the assignments in that branch


@dataclass
class Frontier:
    """A search loop shape: a worklist that is popped and refilled, or a layered expansion."""

    kind: str  # worklist | layered | relaxation
    container: str  # the frontier (worklist), the layer iterated over (layered) or the cost table (relaxation)
    line: int
    pops: list[ast.Call] = field(default_factory=list)
    pushes: list[ast.Call] = field(default_factory=list)
    closed: list[str] = field(default_factory=list)  # visited / cost / parent tables (worklist); predecessors (relaxation)
    next_layer: str = ""  # container filled from each element's successors (layered)
    inner: tuple[int, int] = (0, 0)  # lines of the loop over the current layer (layered)
    writes: list[tuple[int, int]] = field(default_factory=list)  # (line, col) of the cost-table stores (relaxation)
    value_roots: list[str] = field(default_factory=list)  # variables the stored candidate costs come from


@dataclass
class LoopInfo:
    """A for/while loop, with the selection and search shapes found in it."""

    function: str
    kind: str
    line: int
    end_line: int
    best_updates: list[BestUpdate] = field(default_factory=list)
    frontiers: list[Frontier] = field(default_factory=list)


@dataclass
class FunctionInfo:
    """A function, method or lambda defined in the analysed code."""

    qualname: str
    module: str
    file: str
    node: ast.FunctionDef | ast.AsyncFunctionDef | ast.Lambda
    cls: str | None
    params: list[str]
    is_method: bool
    param_nodes: dict[str, Node] = field(default_factory=dict)
    return_node: Node | None = None
    nested: dict[str, str] = field(default_factory=dict)  # local name -> nested qualname
    parent: str | None = None  # enclosing function, for nested functions and lambdas
    captured_writes: dict[str, set[Node]] = field(default_factory=dict)  # closure vars it modifies
    imports: dict[str, str] = field(default_factory=dict)  # imports made inside the function
    global_names: set[str] = field(default_factory=set)
    call_sites: dict[Node, CallSite] = field(default_factory=dict)
    loops: dict[int, LoopInfo] = field(default_factory=dict)  # keyed by line
    is_lambda: bool = False
    free_names: frozenset | None = None


@dataclass
class ClassInfo:
    """A class defined in the analysed code."""

    qualname: str
    module: str
    node: ast.ClassDef
    bases: list[str] = field(default_factory=list)  # resolved project base qualnames
    methods: dict[str, str] = field(default_factory=dict)  # name -> function qualname


@dataclass
class ModuleInfo:
    """One analysed source file."""

    name: str
    file: str
    tree: ast.Module
    imports: dict[str, str] = field(default_factory=dict)  # local alias -> qualified name
    functions: dict[str, str] = field(default_factory=dict)  # top-level name -> qualname
    classes: dict[str, str] = field(default_factory=dict)
    globals: set[str] = field(default_factory=set)
    is_package: bool = False


class DependencyGraph:
    """Nodes, typed edges and the program structure they were extracted from."""

    def __init__(self) -> None:
        self.preds: dict[Node, dict[Node, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.succs: dict[Node, dict[Node, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.nodes: set[Node] = set()
        self.modules: dict[str, ModuleInfo] = {}
        self.functions: dict[str, FunctionInfo] = {}
        self.classes: dict[str, ClassInfo] = {}
        self.call_graph: dict[str, set[str]] = defaultdict(set)
        self.call_sites: dict[Node, CallSite] = {}  # every call, including module-level ones
        self.constant_fields: dict[str, object] = {}  # "pkg.mod.Class.attr" -> its only possible literal
        self.written_fields: set[str] = set()  # "pkg.mod.Class.attr" assigned anywhere in the family
        self.pruned: list[tuple[str, int, str, str]] = []  # (file, line, test, part skipped)
        self.copies: set[tuple[Node, Node]] = set()  # (src, dst): dst holds src's value (or part of it) unchanged
        self.ops: dict[Node, OpInfo] = {}
        self.fnvals: dict[Node, set[str]] = defaultdict(set)  # value site -> functions it may hold
        self.iter_vars: set[Node] = set()  # loop / comprehension / callback variables bound to elements
        self.decision_vars: set[Node] = set()  # optimiser objective parameters (the decision variable)
        self.test_deps: dict[tuple[str, int, int], set[Node]] = defaultdict(set)  # (scope, line, col) of an if
        self.ordering_tests: set[tuple[str, int, int]] = set()  # ifs comparing two computed values with < > <= >=
        self.sequence_defs: set[Node] = set()  # variables initialised with a list/tuple (built up, not simulated)
        self.scope_defs: dict[str, set[Node]] = defaultdict(set)
        self.unresolved_imports: list[tuple[str, str, int]] = []  # (module, importing file, line)
        self.unresolved_callbacks: dict[Node, str] = {}  # call -> callback expression we could not resolve
        self.parse_errors: list[tuple[str, str]] = []
        self.module_alias: dict[str, str] = {}  # dotted name used in an import -> analysed module name
        self.module_deps: dict[str, set[str]] = defaultdict(set)
        self.libraries: frozenset[str] = STDLIB_MODULES | KNOWN_LIBRARIES
        self.entrypoint_basis: dict[str, str] = {}  # decision qualname -> how it was found
        self._copy_index: tuple[int, dict, dict] | None = None

    def add_edge(self, src: Node, dst: Node, kind: str) -> None:
        """Record that ``dst`` is computed from ``src``."""
        self.nodes.add(src)
        self.nodes.add(dst)
        self.preds[dst][src].add(kind)
        self.succs[src][dst].add(kind)

    def backward_slice(self, start: Iterable[Node], kinds: Iterable[str] = EDGE_KINDS) -> set[Node]:
        """Every node that the start nodes are (transitively) computed from."""
        return self._reach(start, kinds, self.preds)

    def forward_slice(self, start: Iterable[Node], kinds: Iterable[str] = EDGE_KINDS) -> set[Node]:
        """Every node (transitively) computed from the start nodes."""
        return self._reach(start, kinds, self.succs)

    @staticmethod
    def _reach(start: Iterable[Node], kinds: Iterable[str], adj) -> set[Node]:
        allowed = set(kinds)
        seen: set[Node] = set()
        stack = list(start)
        while stack:
            v = stack.pop()
            for u, ks in adj.get(v, {}).items():
                if u not in seen and ks & allowed:
                    seen.add(u)
                    stack.append(u)
        return seen

    def _copy_maps(self) -> tuple[dict, dict]:
        if self._copy_index is None or self._copy_index[0] != len(self.copies):
            preds, succs = defaultdict(set), defaultdict(set)
            for s, d in self.copies:
                preds[d].add(s)
                succs[s].add(d)
            self._copy_index = (len(self.copies), preds, succs)
        return self._copy_index[1], self._copy_index[2]

    def copy_ancestors(self, start: Iterable[Node]) -> set[Node]:
        """Values that reach the start nodes unchanged (through copies only)."""
        preds = self._copy_maps()[0]
        seen: set[Node] = set()
        stack = list(start)
        while stack:
            for u in preds.get(stack.pop(), ()):
                if u not in seen:
                    seen.add(u)
                    stack.append(u)
        return seen

    def copy_successors(self) -> dict[Node, set[Node]]:
        return self._copy_maps()[1]

    def reachable_functions(self, root: str) -> set[str]:
        """Functions callable from ``root`` (including itself)."""
        seen, stack = {root}, [root]
        while stack:
            for callee in self.call_graph.get(stack.pop(), ()):
                if callee not in seen:
                    seen.add(callee)
                    stack.append(callee)
        return seen

    def recursive_functions(self) -> set[str]:
        """Functions on a call-graph cycle (direct or mutual recursion)."""
        out = set()
        for f in self.functions:
            stack, seen = list(self.call_graph.get(f, ())), set()
            while stack:
                g = stack.pop()
                if g == f:
                    out.add(f)
                    break
                if g not in seen:
                    seen.add(g)
                    stack.extend(self.call_graph.get(g, ()))
        return out

    def import_closure(self, module: str) -> set[str]:
        """The module and every analysed module it imports, directly or indirectly."""
        seen, stack = {module}, [module]
        while stack:
            for m in self.module_deps.get(stack.pop(), ()):
                if m not in seen:
                    seen.add(m)
                    stack.append(m)
        return seen

    def resolution_of(self, external: str) -> str:
        """How a call that is not a project function was resolved (see ``CallSite.resolution``)."""
        if external in ("<dynamic>", "<call>"):
            return "dynamic"
        if external.startswith("method:"):
            return "method"
        if "." not in external:
            return "builtin" if external in BUILTIN_NAMES else "unresolved-name"
        mod = _owning_module(self, external)
        if mod is not None:  # inside an analysed package: a missing submodule, or an unknown name
            head = f"{mod}.{external[len(mod) + 1:].split('.')[0]}"
            known = head in self.classes or head in self.functions
            return "unresolved-import" if "." in external[len(mod) + 1:] and not known else "unresolved-name"
        return "library" if external.split(".")[0] in self.libraries else "unresolved-import"

    def summary(self) -> str:
        """Counts, for a quick check."""
        n_edges = sum(len(d) for d in self.preds.values())
        kinds = defaultdict(int)
        for n in self.nodes:
            kinds[n.kind] += 1
        return (f"{len(self.modules)} modules, {len(self.functions)} functions, "
                f"{len(self.nodes)} nodes ({dict(kinds)}), {n_edges} edges")

    def to_dot(self, nodes: Iterable[Node] | None = None) -> str:
        """Graphviz DOT text for the whole graph or a subset (e.g. a slice)."""
        keep = set(nodes) if nodes is not None else self.nodes
        ids = {n: f"n{i}" for i, n in enumerate(sorted(keep, key=lambda n: (n.scope, n.line, n.label())))}
        shape = {"field": "box", "global": "box", "call": "ellipse", "param": "invhouse", "return": "house",
                 "op": "circle"}
        lines = ["digraph deps {", "  rankdir=LR; node [fontsize=10];"]
        for n, i in ids.items():
            lines.append(f'  {i} [label="{n.label()}", shape={shape.get(n.kind, "plaintext")}];')
        for dst in keep:
            for src, ks in self.preds.get(dst, {}).items():
                if src in keep:
                    style = "dashed" if ks == {"control"} else "solid"
                    lines.append(f'  {ids[src]} -> {ids[dst]} [style={style}, label="{",".join(sorted(ks))}"];')
        lines.append("}")
        return "\n".join(lines)


# --------------------------------------------------------------------------- loading


def _import_root(f: Path) -> Path:
    """The directory a file is imported from: above every enclosing package."""
    d = f.parent
    while (d / "__init__.py").is_file() and d.parent != d:
        d = d.parent
    return d


def _common_dir(paths: list[Path]) -> Path:
    common = paths[0]
    for p in paths[1:]:
        while not p.is_relative_to(common):
            common = common.parent
    return common


def _module_name(path: Path, root: Path) -> str:
    rel = path.relative_to(root).with_suffix("")
    parts = list(rel.parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts) or path.stem


def _parse(f: Path) -> ast.Module | None:
    try:
        return ast.parse(f.read_text(encoding="utf-8"), str(f))
    except (SyntaxError, UnicodeDecodeError, ValueError):
        return None


def _collect(paths: Iterable[str | Path], follow_imports: bool, libraries: frozenset[str]):
    """Files to analyse, plus the imports that could not be resolved to files.

    Imports are resolved like Python does for a script or package: absolute imports
    from the importing file's directory or its package root, relative imports from the
    package of the importing file. Packages on the way (``__init__.py``) are included.
    """
    files: list[Path] = []
    for p in map(Path, paths):
        files.extend(sorted(p.rglob("*.py")) if p.is_dir() else [p])
    files = list(dict.fromkeys(f.resolve() for f in files))
    if not files:
        raise ValueError("no Python files found")
    aliases: dict[str, Path] = {}  # dotted import name -> file
    unresolved: list[tuple[str, str, int]] = []
    seen, queue = set(files), list(files)

    def add(c: Path, import_name: str | None = None) -> None:
        c = c.resolve()
        if import_name:
            aliases.setdefault(import_name, c)
        if c not in seen:
            seen.add(c)
            files.append(c)
            queue.append(c)

    def absolute(name: str, f: Path, names: list[str], line: int) -> None:
        parts = name.split(".")
        for base in dict.fromkeys((f.parent, _import_root(f))):
            target = base.joinpath(*parts)
            if target.with_suffix(".py").is_file():
                add(target.with_suffix(".py"), name)
            elif (target / "__init__.py").is_file():
                add(target / "__init__.py", name)
                for n in names:  # `from pkg import sub` may import a submodule
                    if (target / f"{n}.py").is_file():
                        add(target / f"{n}.py", f"{name}.{n}")
            else:
                continue
            for i in range(1, len(parts)):  # parent packages run first
                if base.joinpath(*parts[:i], "__init__.py").is_file():
                    add(base.joinpath(*parts[:i], "__init__.py"), ".".join(parts[:i]))
            return
        if parts[0] not in libraries:
            unresolved.append((name, str(f), line))

    def relative(node: ast.ImportFrom, f: Path) -> None:
        base = f.parent
        for _ in range(node.level - 1):
            base = base.parent
        parts = node.module.split(".") if node.module else []
        target = base.joinpath(*parts)
        found = False
        if (base / "__init__.py").is_file():
            add(base / "__init__.py")
        if parts and target.with_suffix(".py").is_file():
            add(target.with_suffix(".py"))
            found = True
        elif (target / "__init__.py").is_file():
            add(target / "__init__.py")
            found = True
        for a in node.names:
            if (target / f"{a.name}.py").is_file():
                add(target / f"{a.name}.py")
                found = True
        if not found:
            unresolved.append(("." * node.level + (node.module or ""), str(f), node.lineno))

    while follow_imports and queue:
        f = queue.pop(0)
        tree = _parse(f)
        if tree is None:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names:
                    absolute(a.name, f, [], node.lineno)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    relative(node, f)
                elif node.module:
                    absolute(node.module, f, [a.name for a in node.names], node.lineno)
    root = _common_dir([_import_root(f) for f in files])
    return root, files, aliases, unresolved


def build_graph(paths: Iterable[str | Path], follow_imports: bool = True,
                libraries: Iterable[str] = ()) -> DependencyGraph:
    """Parse the given files/directories and build their dependency graph.

    ``libraries`` adds top-level package names whose imports are libraries (named calls)
    rather than missing project code.
    """
    g = DependencyGraph()
    g.libraries = g.libraries | frozenset(libraries)
    given = [Path(p).resolve() for p in paths]
    root, files, aliases, g.unresolved_imports = _collect(paths, follow_imports, g.libraries)
    for f in files:
        tree = _parse(f)
        if tree is None:
            if f in given or any(f.is_relative_to(p) for p in given if p.is_dir()):
                raise SyntaxError(f"cannot parse {f}")
            g.parse_errors.append((str(f), "syntax error"))
            continue
        name = _module_name(f, root)
        g.modules[name] = ModuleInfo(name, str(f), tree, is_package=f.name == "__init__.py")
    by_file = {Path(m.file): m.name for m in g.modules.values()}
    g.module_alias = {imp: by_file[f] for imp, f in aliases.items() if f in by_file and by_file[f] != imp}
    for mod in g.modules.values():
        _index_module(g, mod)
    for mod in g.modules.values():
        _resolve_bases(g, mod)
    writes = _field_write_summaries(g)
    g.constant_fields, g.written_fields = _constant_fields(g)
    analyzer = _Analyzer(g, writes)
    for _ in range(4):  # function values found late (e.g. a callback stored in a field) need another pass
        before = {k: frozenset(v) for k, v in g.fnvals.items() if v}
        analyzer.new_pass()
        for mod in g.modules.values():
            analyzer.analyze_module(mod)
        for fn in list(g.functions.values()):
            if fn.parent is None and not fn.is_lambda:  # nested functions are analysed inside their parent
                analyzer.analyze_function(fn)
        if {k: frozenset(v) for k, v in g.fnvals.items() if v} == before:
            break
    g.pruned = list(dict.fromkeys(g.pruned))
    return g


def _alias(g: DependencyGraph, dotted: str) -> str:
    """Rewrite a dotted import name to the analysed module name it was resolved to."""
    parts = dotted.split(".")
    for i in range(len(parts), 0, -1):
        head = ".".join(parts[:i])
        if head in g.module_alias:
            return ".".join([g.module_alias[head], *parts[i:]])
    return dotted


def _import_bindings(g: DependencyGraph, mod: ModuleInfo, node: ast.Import | ast.ImportFrom) -> dict[str, str]:
    """Local name -> qualified name for one import statement."""
    out = {}
    if isinstance(node, ast.Import):
        for a in node.names:
            if a.asname:
                out[a.asname] = _alias(g, a.name)
            else:
                head = a.name.split(".")[0]
                out[head] = _alias(g, head)
        return out
    if node.level:
        pkg = mod.name.split(".") if mod.is_package else mod.name.split(".")[:-1]
        pkg = pkg[: len(pkg) - (node.level - 1)] if node.level > 1 else pkg
        base = ".".join([*pkg, *(node.module.split(".") if node.module else [])])
    else:
        base = _alias(g, node.module or "")
    for a in node.names:
        out[a.asname or a.name] = f"{base}.{a.name}" if base else a.name
    return out


def _owning_module(g: DependencyGraph, qualified: str) -> str | None:
    parts = qualified.split(".")
    for i in range(len(parts), 0, -1):
        if ".".join(parts[:i]) in g.modules:
            return ".".join(parts[:i])
    return None


def _index_module(g: DependencyGraph, mod: ModuleInfo) -> None:
    for node in mod.tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod.imports.update(_import_bindings(g, mod, node))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            q = f"{mod.name}.{node.name}"
            mod.functions[node.name] = q
            g.functions[q] = _function_info(q, mod, node, None)
        elif isinstance(node, ast.ClassDef):
            cq = f"{mod.name}.{node.name}"
            mod.classes[node.name] = cq
            ci = ClassInfo(cq, mod.name, node)
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    fq = f"{cq}.{item.name}"
                    ci.methods[item.name] = fq
                    g.functions[fq] = _function_info(fq, mod, item, cq)
            g.classes[cq] = ci
        elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in targets:
                for n in ast.walk(t):
                    if isinstance(n, ast.Name):
                        mod.globals.add(n.id)
    for node in ast.walk(mod.tree):  # every import, including those inside functions
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for q in _import_bindings(g, mod, node).values():
                parts = q.split(".")
                for i in range(1, len(parts) + 1):
                    if ".".join(parts[:i]) in g.modules and ".".join(parts[:i]) != mod.name:
                        g.module_deps[mod.name].add(".".join(parts[:i]))


def _function_info(q: str, mod: ModuleInfo, node, cls: str | None) -> FunctionInfo:
    args = node.args
    params = [a.arg for a in (*args.posonlyargs, *args.args)]
    if args.vararg:
        params.append(args.vararg.arg)
    params += [a.arg for a in args.kwonlyargs]
    if args.kwarg:
        params.append(args.kwarg.arg)
    decos = {d.id for d in getattr(node, "decorator_list", ()) if isinstance(d, ast.Name)}
    is_method = cls is not None and "staticmethod" not in decos and bool(params)
    return FunctionInfo(q, mod.name, mod.file, node, cls, params, is_method, is_lambda=isinstance(node, ast.Lambda))


def _resolve_bases(g: DependencyGraph, mod: ModuleInfo) -> None:
    for cq in mod.classes.values():
        ci = g.classes[cq]
        for b in ci.node.bases:
            name = _dotted(b)
            if name is None:
                continue
            q = _resolve_name(g, mod, name)
            if q in g.classes:
                ci.bases.append(q)


def _dotted(expr: ast.expr) -> str | None:
    parts = []
    while isinstance(expr, ast.Attribute):
        parts.append(expr.attr)
        expr = expr.value
    if isinstance(expr, ast.Name):
        parts.append(expr.id)
        return ".".join(reversed(parts))
    return None


def _root_dotted(expr: ast.expr) -> str | None:
    """`best[0]` -> 'best', `self.best[i] - 1e-9` -> 'self.best' (first operand of arithmetic)."""
    while isinstance(expr, (ast.Subscript, ast.BinOp, ast.UnaryOp)):
        expr = expr.value if isinstance(expr, ast.Subscript) else (expr.left if isinstance(expr, ast.BinOp) else expr.operand)
    return _dotted(expr)


def _resolve_name(g: DependencyGraph, mod: ModuleInfo, dotted: str) -> str:
    """Qualified name of a dotted reference as seen from ``mod``."""
    head, _, rest = dotted.partition(".")
    if head in mod.functions:
        base = mod.functions[head]
    elif head in mod.classes:
        base = mod.classes[head]
    elif head in mod.imports:
        base = mod.imports[head]
    else:
        base = head
    return f"{base}.{rest}" if rest else base


def _mro(g: DependencyGraph, cq: str) -> list[str]:
    out, stack = [], [cq]
    while stack:
        c = stack.pop(0)
        if c in out or c not in g.classes:
            continue
        out.append(c)
        stack.extend(g.classes[c].bases)
    return out


def _resolve_method(g: DependencyGraph, cq: str | None, name: str) -> str | None:
    if cq is None:
        return None
    for c in _mro(g, cq):
        if name in g.classes[c].methods:
            return g.classes[c].methods[name]
    return None


def _field_owner(g: DependencyGraph, cq: str) -> str:
    """Root project ancestor (fully qualified): one field node per attribute and class family."""
    while g.classes.get(cq) and g.classes[cq].bases:
        cq = g.classes[cq].bases[0]
    return cq


def _field_write_summaries(g: DependencyGraph) -> dict[str, set[str]]:
    """Attributes of ``self`` each method may write, including via self-method calls."""
    direct: dict[str, set[str]] = defaultdict(set)
    calls: dict[str, set[str]] = defaultdict(set)
    for q, fn in g.functions.items():
        if not fn.is_method:
            continue
        me = fn.params[0]
        for n in ast.walk(fn.node):
            targets = []
            if isinstance(n, ast.Assign):
                targets = n.targets
            elif isinstance(n, (ast.AugAssign, ast.AnnAssign)):
                targets = [n.target]
            elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
                if n.func.attr in MUTATING_METHODS:
                    targets = [n.func.value]
                if isinstance(n.func.value, ast.Name) and n.func.value.id == me:
                    callee = _resolve_method(g, fn.cls, n.func.attr)
                    if callee:
                        calls[q].add(callee)
            for t in targets:
                for leaf in _flatten_targets(t):
                    root = _attr_root(leaf, me)
                    if root:
                        direct[q].add(root)
    out = {}
    for q in g.functions:
        seen, stack, acc = {q}, [q], set()
        while stack:
            f = stack.pop()
            acc |= direct.get(f, set())
            for c in calls.get(f, ()):
                if c not in seen:
                    seen.add(c)
                    stack.append(c)
        out[q] = acc
    return out


_NONCONST = ("<nonconst>",)


def _literal(e: ast.expr | None):
    """(type, value) of a literal, so that True and 1 stay different; _NONCONST otherwise."""
    if isinstance(e, ast.Constant):
        return (type(e.value).__name__, e.value)
    if isinstance(e, ast.UnaryOp) and isinstance(e.op, ast.USub) and isinstance(e.operand, ast.Constant) \
            and isinstance(e.operand.value, (int, float)):
        return (type(e.operand.value).__name__, -e.operand.value)
    return _NONCONST


def _store_targets(n: ast.AST) -> tuple[list[ast.expr], ast.expr | None, bool]:
    """(targets, assigned value, whether the value replaces the target) for statements that store."""
    if isinstance(n, ast.Assign):
        return n.targets, n.value, True
    if isinstance(n, ast.AnnAssign):
        return [n.target], n.value, n.value is not None
    if isinstance(n, ast.AugAssign):
        return [n.target], None, False
    if isinstance(n, (ast.For, ast.AsyncFor)):
        return [n.target], None, False
    if isinstance(n, (ast.With, ast.AsyncWith)):
        return [i.optional_vars for i in n.items if i.optional_vars is not None], None, False
    if isinstance(n, ast.NamedExpr):
        return [n.target], None, False
    return [], None, False


def _constant_fields(g: DependencyGraph) -> tuple[dict[str, object], set[str]]:
    """Attributes whose every visible write stores the same literal, and all written attributes.

    Counted writes: class-body defaults, every assignment to ``self.attr`` in any method of
    the class family (constructor or not), in-place updates, and any assignment to an
    attribute of the same name on another object anywhere in the analysed code (without
    types, ``p.enabled = True`` may target the class). ``setattr`` with a computed name or
    writes through ``__dict__``/``vars`` make nothing constant.
    """
    values: dict[str, set] = defaultdict(set)
    elsewhere: set[str] = set()  # attribute names written on objects other than self
    dynamic = False

    def scan(tree: ast.AST, me: str | None, owner: str | None) -> None:
        nonlocal dynamic
        for n in ast.walk(tree):
            targets, value, replaces = _store_targets(n)
            if isinstance(n, ast.Call):
                fname = _dotted(n.func) or ""
                if fname == "setattr" and len(n.args) >= 2:
                    if isinstance(n.args[1], ast.Constant) and isinstance(n.args[1].value, str):
                        elsewhere.add(n.args[1].value)
                    else:
                        dynamic = True
                elif fname in ("vars", "object.__setattr__"):
                    dynamic = True
                elif isinstance(n.func, ast.Attribute) and n.func.attr in MUTATING_METHODS:
                    targets, value, replaces = [n.func.value], None, False
            for t in targets:
                for leaf in _flatten_targets(t):
                    root = _attr_root(leaf, me) if me else None
                    if root is not None and owner:
                        direct = replaces and isinstance(leaf, ast.Attribute)
                        values[f"{owner}.{root}"].add(_literal(value) if direct else _NONCONST)
                    for a in ast.walk(leaf):
                        if isinstance(a, ast.Attribute) and isinstance(a.ctx, ast.Store) and a.attr != root:
                            if a.attr == "__dict__":
                                dynamic = True
                            elsewhere.add(a.attr)
                        elif isinstance(a, ast.Attribute) and a.attr == "__dict__":
                            dynamic = True

    for cq, ci in g.classes.items():
        owner = _field_owner(g, cq)
        for st in ci.node.body:
            targets, value, replaces = _store_targets(st)
            for t in targets:
                for leaf in _flatten_targets(t):
                    if isinstance(leaf, ast.Name):
                        values[f"{owner}.{leaf.id}"].add(_literal(value) if replaces else _NONCONST)
    for fn in g.functions.values():  # module-level functions and methods; nested ones are inside them
        me = fn.params[0] if fn.is_method else None
        scan(fn.node, me, _field_owner(g, fn.cls) if fn.is_method else None)
    for mod in g.modules.values():
        for st in mod.tree.body:
            if not isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                scan(st, None, None)
    written = set(values)
    if dynamic:
        return {}, written
    consts = {k: next(iter(v))[1] for k, v in values.items()
              if len(v) == 1 and _NONCONST not in v and k.rsplit(".", 1)[-1] not in elsewhere}
    return consts, written


def _flatten_targets(t: ast.expr) -> Iterator[ast.expr]:
    if isinstance(t, (ast.Tuple, ast.List)):
        for e in t.elts:
            yield from _flatten_targets(e)
    elif isinstance(t, ast.Starred):
        yield from _flatten_targets(t.value)
    else:
        yield t


def _attr_root(t: ast.expr, me: str) -> str | None:
    """For self.a / self.a[i] / self.a.b[...] return 'a'."""
    while isinstance(t, (ast.Subscript, ast.Attribute)):
        if isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name) and t.value.id == me:
            return t.attr
        t = t.value
    return None


def _walk(stmts: Iterable[ast.AST], into_loops: bool) -> Iterator[ast.AST]:
    """Nodes under the statements, not entering nested functions, lambdas or classes (or loops)."""
    stack = list(stmts)[::-1]
    while stack:
        n = stack.pop()
        yield n
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
            continue
        if not into_loops and isinstance(n, (ast.For, ast.AsyncFor, ast.While)):
            continue
        stack.extend(list(ast.iter_child_nodes(n))[::-1])


def _iter_container(e: ast.expr) -> str | None:
    """The container a loop iterates over: ``xs``, ``xs.items()``, ``list(xs)``, ``enumerate(xs)``."""
    if isinstance(e, ast.Call):
        if isinstance(e.func, ast.Attribute) and e.func.attr in ("items", "keys", "values", "copy"):
            return _iter_container(e.func.value)
        if isinstance(e.func, ast.Name) and e.func.id in ("list", "sorted", "tuple", "set", "enumerate",
                                                          "reversed", "iter") and e.args:
            return _iter_container(e.args[0])
        return None
    return _root_dotted(e)


def _written_containers(stmts: Iterable[ast.AST]) -> set[str]:
    """Containers updated in place: ``c[k] = v``, ``c[k] |= v``, ``c.add(v)``, ``c.append(v)``."""
    out = set()
    for n in _walk(stmts, True):
        if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            for t in (n.targets if isinstance(n, ast.Assign) else [n.target]):
                for leaf in _flatten_targets(t):
                    if isinstance(leaf, ast.Subscript):
                        out.add(_root_dotted(leaf))
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and n.func.attr in ("add", "append", "appendleft", "extend", "update", "setdefault", "put"):
            out.add(_dotted(n.func.value))
    return out - {None}


# --------------------------------------------------------------------------- analysis

Env = dict[str, set[Node]]
_MISSING = object()


def _element_return(fn: FunctionInfo, i: int) -> Node:
    """Element ``i`` of the tuple a function returns (when every return is an n-tuple)."""
    return Node("return", f"return[{i}]", fn.qualname, fn.file, fn.node.lineno)


def _tuple_alternatives(e: ast.expr | None) -> list[list[ast.expr]] | None:
    """The tuple literals an expression can evaluate to: ``(a, b)`` or ``(a, b) if c else (d, e)``."""
    if isinstance(e, ast.Tuple) and not any(isinstance(x, ast.Starred) for x in e.elts):
        return [e.elts]
    if isinstance(e, ast.IfExp):
        body, orelse = _tuple_alternatives(e.body), _tuple_alternatives(e.orelse)
        if body and orelse:
            return body + orelse
    return None


def _tuple_return_arity(fn_node: ast.AST) -> int | None:
    """n if every ``return`` in the function's own body returns an n-tuple literal."""
    if isinstance(fn_node, ast.Lambda):
        alts = _tuple_alternatives(fn_node.body)
        return len(alts[0]) if alts and len({len(a) for a in alts}) == 1 else None
    arities = set()
    stack = list(fn_node.body)
    while stack:
        n = stack.pop()
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
            continue
        if isinstance(n, ast.Return):
            alts = _tuple_alternatives(n.value)
            arities.update({len(a) for a in alts} if alts else {None})
        stack.extend(ast.iter_child_nodes(n))
    return arities.pop() if len(arities) == 1 else None


class _LoopCtx:
    """Environments leaving the innermost loop body early."""

    def __init__(self) -> None:
        self.breaks: list[Env] = []
        self.continues: list[Env] = []


class _Analyzer:
    """Walks function bodies, maintaining reaching definitions, and adds edges.

    An environment of ``None`` means "unreachable": nothing after an unconditional
    ``return``/``raise``/``break``/``continue`` is analysed.
    """

    def __init__(self, g: DependencyGraph, field_writes: dict[str, set[str]]) -> None:
        self.g = g
        self.field_writes = field_writes
        self.fn: FunctionInfo | None = None
        self.mod: ModuleInfo | None = None
        self.scope = ""
        self.loop_stack: list[LoopInfo] = []
        self.loop_ctx: list[_LoopCtx] = []
        self.ctrl: frozenset = frozenset()  # control context of the statement being analysed
        self._copies: dict[int, set[Node]] = {}  # id(expression) -> nodes whose value it passes on unchanged
        self._deps: dict[int, set[Node]] = {}  # id(expression) -> nodes it is computed from
        self._fnrefs: set[int] = set()  # id(expression) of expressions that name a function (not call it)
        self._analyzed: dict[str, object] = {}
        self.me: str | None = None  # name of self in a method

    def new_pass(self) -> None:
        self._analyzed = {}

    # ---- entry points
    def analyze_module(self, mod: ModuleInfo) -> None:
        self.mod, self.fn, self.me = mod, None, None
        self.scope = f"{mod.name}.<module>"
        self.loop_stack, self.loop_ctx, self.ctrl = [], [], frozenset()
        body = [s for s in mod.tree.body if not isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
        env = self.block(body, {}, frozenset()) or {}
        for name, defs in env.items():
            if name in mod.globals:
                for d in defs:
                    self.g.add_edge(d, self.global_node(mod, name), "data")
                    if self.g.fnvals.get(d):
                        self.g.fnvals[self.global_node(mod, name)] |= self.g.fnvals[d]
        for c in (n for n in mod.tree.body if isinstance(n, ast.ClassDef)):  # class-level attributes
            cq = mod.classes[c.name]
            cenv = self.block([s for s in c.body if isinstance(s, (ast.Assign, ast.AnnAssign))], {}, frozenset()) or {}
            for name, defs in cenv.items():
                for d in defs:
                    self.g.add_edge(d, self.field_node(cq, name), "field_write")
                    self.g.copies.add((d, self.field_node(cq, name)))

    def analyze_function(self, fn: FunctionInfo, closure: Env | None = None, me: str | None = None) -> None:
        key = self._closure_key(fn, closure)
        if self._analyzed.get(fn.qualname, _MISSING) == key:
            return
        self._analyzed[fn.qualname] = key
        prev = (self.fn, self.mod, self.scope, self.me, self.loop_stack, self.loop_ctx, self.ctrl)
        self.fn, self.mod, self.scope = fn, self.g.modules[fn.module], fn.qualname
        self.me = fn.params[0] if fn.is_method else me
        self.loop_stack, self.loop_ctx, self.ctrl = [], [], frozenset()
        try:
            if not fn.is_lambda:
                fn.global_names = {n for s in ast.walk(fn.node) if isinstance(s, (ast.Global, ast.Nonlocal))
                                   for n in s.names}
                for st in ast.walk(fn.node):  # `import x` inside a function (or a nested one)
                    if isinstance(st, (ast.Import, ast.ImportFrom)):
                        fn.imports.update(_import_bindings(self.g, self.mod, st))
            fn.return_node = Node("return", "return", fn.qualname, fn.file, fn.node.lineno)
            self.g.nodes.add(fn.return_node)
            env: Env = dict(closure or {})
            for p in fn.params:
                pn = Node("param", p, fn.qualname, fn.file, fn.node.lineno)
                fn.param_nodes[p] = pn
                self.g.nodes.add(pn)
                env[p] = {pn}
            # defaults are evaluated in the enclosing scope; ignore
            if fn.is_lambda:
                self.link(self.expr(fn.node.body, env), fn.return_node, copies=self.copied(fn.node.body))
            else:
                self.block(fn.node.body, env, frozenset())
            if closure and not fn.is_lambda:  # in-place changes to captured variables are visible to the encloser
                for n in self.g.scope_defs.get(fn.qualname, ()):
                    if n.name in closure and n.name not in fn.params and n.detail:
                        fn.captured_writes.setdefault(n.name, set()).add(n)
        finally:
            self.fn, self.mod, self.scope, self.me, self.loop_stack, self.loop_ctx, self.ctrl = prev

    def _closure_key(self, fn: FunctionInfo, closure: Env | None):
        if not closure:
            return None
        if fn.free_names is None:
            fn.free_names = frozenset(n.id for n in ast.walk(fn.node) if isinstance(n, ast.Name))
        return frozenset((k, frozenset(closure[k])) for k in fn.free_names if k in closure)

    # ---- node helpers
    def field_node(self, cq: str, attr: str) -> Node:
        return Node("field", f"{_field_owner(self.g, cq)}.{attr}")

    def global_node(self, mod: ModuleInfo, name: str) -> Node:
        return Node("global", f"{mod.name}.{name}")

    def return_of(self, q: str) -> Node:
        info = self.g.functions[q]
        return Node("return", "return", q, info.file, info.node.lineno)

    def new_def(self, name: str, at: ast.AST, detail: str = "") -> Node:
        n = Node("def", name, self.scope, self.mod.file if self.mod else "", getattr(at, "lineno", 0),
                 getattr(at, "col_offset", 0), detail)
        self.g.nodes.add(n)
        self.g.scope_defs[self.scope].add(n)
        return n

    def op_node(self, at: ast.AST, symbol: str, left: set[Node], right: set[Node],
                left_copy: set[Node], right_copy: set[Node], operands: tuple = ()) -> Node:
        n = Node("op", symbol, self.scope, self.mod.file if self.mod else "", at.lineno, at.col_offset)
        self.g.nodes.add(n)
        self.link(left, n)
        self.link(right, n)
        info = self.g.ops.get(n)
        if info is None:
            seq = (ast.List, ast.Tuple, ast.ListComp, ast.JoinedStr, ast.Set, ast.SetComp, ast.GeneratorExp)
            info = self.g.ops[n] = OpInfo(symbol, ast.unparse(at)[:80], sequence=any(
                isinstance(x, seq) or (isinstance(x, ast.Constant) and isinstance(x.value, (str, bytes)))
                for x in operands))
        info.left |= left
        info.right |= right
        info.left_copy |= left_copy
        info.right_copy |= right_copy
        return n

    def link(self, srcs: Iterable[Node], dst: Node, kind: str = "data", copies: Iterable[Node] = ()) -> None:
        srcs = list(srcs)
        for s in srcs:
            self.g.add_edge(s, dst, kind)
        for s in (srcs if kind in ("base", "field_write") else copies):
            self.g.copies.add((s, dst))

    def copied(self, e: ast.expr | None) -> set[Node]:
        """Nodes whose value ``e`` passes on unchanged (``e`` must have gone through ``expr``)."""
        return set(self._copies.get(id(e), ())) if e is not None else set()

    def deps_of(self, e: ast.expr | None) -> set[Node]:
        """Nodes ``e`` was computed from (``e`` must have gone through ``expr``)."""
        return set(self._deps.get(id(e), ())) if e is not None else set()

    def add_fnvals(self, n: Node, targets: Iterable[str]) -> None:
        self.g.fnvals[n] |= set(targets)

    def fnvals_of(self, nodes: Iterable[Node]) -> set[str]:
        out: set[str] = set()
        for n in nodes:
            out |= self.g.fnvals.get(n, set())
        return out

    def fallback(self, key: str) -> set[Node]:
        """Value of a name that has no local definition reaching here."""
        if key.startswith("self.") and self.fn and self.fn.cls:
            return {self.field_node(self.fn.cls, key[5:])}
        if self.mod and (key in self.mod.globals or (self.fn and key in self.fn.global_names)):
            return {self.global_node(self.mod, key)}
        return set()

    def lookup(self, env: Env, key: str) -> set[Node]:
        return set(env[key]) if key in env else self.fallback(key)

    def merge(self, *envs: Env | None) -> Env | None:
        live = [e for e in envs if e is not None]
        if not live:
            return None
        keys = set().union(*live)
        return {k: set().union(*(e[k] if k in e else self.fallback(k) for e in live)) for k in keys}

    # ---- names that denote functions
    def local_import(self, name: str) -> str | None:
        f = self.fn
        while f is not None:
            if name in f.imports:
                return f.imports[name]
            f = self.g.functions.get(f.parent) if f.parent else None
        return None

    def function_named(self, name: str) -> str | None:
        """Project function a bare name refers to (nested, enclosing, imported or module-level)."""
        f = self.fn
        while f is not None:
            if name in f.nested:
                return f.nested[name]
            if getattr(f.node, "name", None) == name and f.parent is not None:
                return f.qualname
            f = self.g.functions.get(f.parent) if f.parent else None
        imported = self.local_import(name)
        if imported is not None:
            return imported if imported in self.g.functions else None
        if self.mod is None:
            return None
        q = _resolve_name(self.g, self.mod, name)
        return q if q in self.g.functions else None

    def project_function(self, dotted: str) -> str | None:
        """``module.function`` or ``Class.method`` reached through an import or a class name."""
        if self.mod is None:
            return None
        head, _, rest = dotted.partition(".")
        imported = self.local_import(head)
        q = f"{imported}.{rest}" if imported and rest else (_resolve_name(self.g, self.mod, dotted))
        if q in self.g.functions:
            return q
        cls_q, _, meth = q.rpartition(".")
        if cls_q in self.g.classes:
            return _resolve_method(self.g, cls_q, meth)
        return None

    def method_ref(self, attr: str) -> str | None:
        """``self.m`` used as a value names the method, unless ``m`` is also a stored attribute."""
        if not (self.fn and self.fn.cls):
            return None
        if f"{_field_owner(self.g, self.fn.cls)}.{attr}" in self.g.written_fields:
            return None
        return _resolve_method(self.g, self.fn.cls, attr)

    def lambda_function(self, e: ast.Lambda, env: Env) -> str:
        """Register a lambda as a function (once) and analyse it with the variables it closes over."""
        q = f"{self.scope}.<lambda:{e.lineno}:{e.col_offset}>"
        info = self.g.functions.get(q)
        if info is None:
            info = _function_info(q, self.mod, e, None)
            info.cls = self.fn.cls if self.fn else None
            info.parent = self.fn.qualname if self.fn else None
            self.g.functions[q] = info
        self.analyze_function(info, closure=env, me=self.me)
        return q

    def fn_targets(self, e: ast.expr | None, env: Env) -> set[str]:
        """Project functions an expression evaluates to (empty if it is not a known function)."""
        if e is None:
            return set()
        if isinstance(e, ast.Lambda):
            return {self.lambda_function(e, env)}
        if isinstance(e, ast.Name):
            if e.id in env:
                return self.fnvals_of(env[e.id])
            q = self.function_named(e.id)
            if q:
                return {q}
            if self.mod and e.id in self.mod.globals:
                return self.fnvals_of({self.global_node(self.mod, e.id)})
            return set()
        if isinstance(e, ast.Attribute):
            if self.me is not None and isinstance(e.value, ast.Name) and e.value.id == self.me:
                key = f"self.{e.attr}"
                held = self.fnvals_of(self.lookup(env, key))
                if held:
                    return held
                m = _resolve_method(self.g, self.fn.cls if self.fn else None, e.attr)
                return {m} if m else set()
            dotted = _dotted(e)
            if dotted is not None and dotted.split(".")[0] not in env:
                q = self.project_function(dotted)
                return {q} if q else set()
            return set()
        if isinstance(e, ast.Call):
            name = _dotted(e.func)
            if name and e.args and self.qualify(name) == "functools.partial":
                return self.fn_targets(e.args[0], env)
        return set()

    def qualify(self, dotted: str) -> str:
        """Imported qualified name of a dotted reference (``hq.heappop`` -> ``heapq.heappop``)."""
        head, _, rest = dotted.partition(".")
        imported = self.local_import(head)
        if imported is not None:
            return f"{imported}.{rest}" if rest else imported
        return _resolve_name(self.g, self.mod, dotted) if self.mod else dotted

    # ---- expressions
    def expr(self, e: ast.expr | None, env: Env) -> set[Node]:
        """Definitions the value of ``e`` depends on (adds call nodes/edges as needed)."""
        deps = self._expr(e, env)
        if e is not None:
            self._deps[id(e)] = deps
            self._copies[id(e)] = self._copied_parts(e, deps)
        return deps

    def _copied_parts(self, e: ast.expr, deps: set[Node]) -> set[Node]:
        c = self.copied
        if id(e) in self._fnrefs:  # a function used as a value: not a copy of its result
            return set()
        if isinstance(e, (ast.Name, ast.NamedExpr)):
            return set(deps)
        if isinstance(e, ast.Attribute):
            if self.me is not None and isinstance(e.value, ast.Name) and e.value.id == self.me:
                return set(deps)
            return c(e.value)
        if isinstance(e, ast.Subscript):  # the element, picked by the index
            return c(e.value) | c(e.slice)
        if isinstance(e, (ast.Tuple, ast.List, ast.Set)):
            return set().union(*(c(x) for x in e.elts))
        if isinstance(e, ast.Dict):
            return set().union(*(c(x) for x in e.values))
        if isinstance(e, ast.Starred):
            return c(e.value)
        if isinstance(e, ast.IfExp):
            return c(e.body) | c(e.orelse)
        if isinstance(e, (ast.ListComp, ast.SetComp, ast.GeneratorExp)):
            return c(e.elt)
        if isinstance(e, ast.Call):  # the call's result (its own copy edges say where it comes from)
            return set(deps)
        if isinstance(e, ast.BinOp) and isinstance(e.op, (ast.Add, ast.Sub)):
            return set(deps)  # the op node is the value
        return set()  # other arithmetic, comparisons, ...: a new value

    def _expr(self, e: ast.expr | None, env: Env) -> set[Node]:
        if e is None or isinstance(e, ast.Constant):
            return set()
        if isinstance(e, ast.Name):
            if self.me is not None and e.id == self.me:
                return set()
            if e.id in env:
                return set(env[e.id])
            fb = self.fallback(e.id)
            if fb:
                return fb
            q = self.function_named(e.id)
            if q:  # a function used as a value: what it computes, when called
                self._fnrefs.add(id(e))
                return {self.return_of(q)}
            return set()
        if isinstance(e, ast.Attribute):
            if self.me is not None and isinstance(e.value, ast.Name) and e.value.id == self.me:
                key = f"self.{e.attr}"
                if key not in env:
                    m = self.method_ref(e.attr)
                    if m:
                        self._fnrefs.add(id(e))
                        return {self.return_of(m)}
                return self.lookup(env, key)
            dotted = _dotted(e)
            if dotted is not None and dotted.split(".")[0] not in env:
                q = self.project_function(dotted)
                if q:
                    self._fnrefs.add(id(e))
                    return {self.return_of(q)}
            return self.expr(e.value, env)
        if isinstance(e, ast.Subscript):
            return self.expr(e.value, env) | self.expr(e.slice, env)
        if isinstance(e, ast.Call):
            return self.call(e, env)
        if isinstance(e, ast.NamedExpr):
            deps = self.expr(e.value, env)
            d = self.new_def(e.target.id, e)
            self.link(deps, d, copies=self.copied(e.value))
            self.link(self.ctrl, d, "control")
            env[e.target.id] = {d}
            return {d}
        if isinstance(e, (ast.Yield, ast.YieldFrom)):  # a generator produces what it yields
            deps = self.expr(e.value, env)
            if self.fn is not None and self.fn.return_node is not None:
                yd = self.new_def("<yield>", e)
                self.link(deps, yd, copies=self.copied(e.value) if isinstance(e, ast.Yield) else ())
                self.link(self.ctrl, yd, "control")
                self.link({yd}, self.fn.return_node, copies={yd} if isinstance(e, ast.Yield) else ())
            return set()  # the value sent back into the generator is unknown
        if isinstance(e, ast.Lambda):
            q = self.lambda_function(e, env)
            self._fnrefs.add(id(e))
            return {self.return_of(q)}
        if isinstance(e, ast.BinOp) and isinstance(e.op, (ast.Add, ast.Sub)):
            left, right = self.expr(e.left, env), self.expr(e.right, env)
            return {self.op_node(e, "+" if isinstance(e.op, ast.Add) else "-", left, right,
                                 self.copied(e.left), self.copied(e.right), (e.left, e.right))}
        if isinstance(e, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
            inner, deps = dict(env), set()
            for gen in e.generators:
                it = self.expr(gen.iter, inner)
                deps |= it
                for leaf in _flatten_targets(gen.target):
                    if isinstance(leaf, ast.Name):  # the element variable: its own node
                        d = self.new_def(leaf.id, leaf)
                        self.link(it, d, "iter", copies=self.copied(gen.iter))
                        self.g.iter_vars.add(d)
                        inner[leaf.id] = {d}
                for cond in gen.ifs:
                    deps |= self.expr(cond, inner)
            if isinstance(e, ast.DictComp):
                return deps | self.expr(e.key, inner) | self.expr(e.value, inner)
            return deps | self.expr(e.elt, inner)
        out: set[Node] = set()
        for child in ast.iter_child_nodes(e):
            if isinstance(child, ast.expr):
                out |= self.expr(child, env)
            elif isinstance(child, ast.keyword):
                out |= self.expr(child.value, env)
        return out

    def unique_method(self, name: str) -> str | None:
        """The project method with this name, if exactly one class defines it among the
        modules the current module imports (directly or not), itself included."""
        if name.startswith("__"):
            return None
        mods = self.g.import_closure(self.mod.name) if self.mod else set()
        hits = [ci.methods[name] for ci in self.g.classes.values() if name in ci.methods and ci.module in mods]
        return hits[0] if len(hits) == 1 else None

    def resolve_callee(self, func: ast.expr, env: Env) -> tuple[list[str], str | None, set[Node], bool]:
        """(project qualnames, external name, receiver deps, resolved-by-name) for a call target."""
        assert self.mod is not None
        dotted0 = _dotted(func)
        if dotted0 is not None:
            head, _, rest = dotted0.partition(".")
            imported = self.local_import(head) if head not in env else None
            if imported is not None:
                q = f"{imported}.{rest}" if rest else imported
                if q in self.g.functions:
                    return [q], None, set(), False
                m = self.project_function(dotted0)
                if m:
                    return [m], None, set(), False
                return [], q, set(), False
        if isinstance(func, ast.Name):
            if func.id in env:  # a variable: resolved if it holds known functions
                held = self.fnvals_of(env[func.id])
                if held:
                    return sorted(held), None, set(), False
                return [], func.id, set(env[func.id]), False
            q = self.function_named(func.id)
            if q:
                return [q], None, set(), False
            q = _resolve_name(self.g, self.mod, func.id)
            if q in self.g.classes:
                init = _resolve_method(self.g, q, "__init__")
                return ([init] if init else []), (None if init else q), set(), False
            if func.id in self.mod.globals:
                held = self.fnvals_of({self.global_node(self.mod, func.id)})
                if held:
                    return sorted(held), None, set(), False
            return [], q, set(), False
        if isinstance(func, ast.Attribute):
            if self.me is not None and isinstance(func.value, ast.Name) and func.value.id == self.me:
                m = _resolve_method(self.g, self.fn.cls if self.fn else None, func.attr)
                if m:
                    return [m], None, set(), False
                key = f"self.{func.attr}"
                held_nodes = self.lookup(env, key)
                held = self.fnvals_of(held_nodes)
                if held:  # an attribute holding a function (e.g. a callback set in __init__)
                    return sorted(held), None, set(), False
                return [], f"method:{func.attr}", held_nodes, False
            dotted = _dotted(func)
            if dotted is not None:
                head = dotted.split(".")[0]
                if head not in env and (head in self.mod.imports or head in self.mod.classes or head in self.mod.functions):
                    m = self.project_function(dotted)
                    if m:
                        return [m], None, set(), False
                    return [], _resolve_name(self.g, self.mod, dotted), set(), False
            recv = self.expr(func.value, env)
            m = self.unique_method(func.attr)
            if m:
                return [m], None, recv, True
            return [], f"method:{func.attr}", recv, False
        return [], "<dynamic>", self.expr(func, env), False

    def call(self, c: ast.Call, env: Env) -> set[Node]:
        callees, external, recv, by_name = self.resolve_callee(c.func, env)
        name = callees[0] if callees else (external or "<call>")
        cn = Node("call", name, self.scope, self.mod.file if self.mod else "", c.lineno, c.col_offset)
        self.g.nodes.add(cn)
        self.link(recv, cn)
        arg_exprs = [a.value if isinstance(a, ast.Starred) else a for a in c.args]
        arg_deps = [self.expr(a, env) for a in arg_exprs]
        kw_deps: dict[str, set[Node]] = {}
        for k in c.keywords:
            kw_deps[k.arg or "**"] = kw_deps.get(k.arg or "**", set()) | self.expr(k.value, env)
        for d in arg_deps:
            self.link(d, cn)
        for d in kw_deps.values():
            self.link(d, cn)
        if external in COPY_CALLS and c.args:
            self.link((), cn, copies=self.copied(c.args[0]))
        elif (external in COPY_CALLS or external in RECEIVER_PART_CALLS) and recv:  # x.copy(), d.get(k)
            self.link((), cn, copies=recv)
        elif external in SELECTING_CALLS:  # the result is one of the alternatives
            sources = arg_exprs[1:2] if external.startswith("heapq.") else arg_exprs
            self.link((), cn, copies=set().union(*(self.copied(a) for a in sources)) if sources else ())
        callbacks = self.bind_callbacks(c, cn, external if not callees else None, arg_exprs, env)
        site = CallSite(cn, callees[0] if callees else None, None if callees else external, self.scope, c,
                        len(self.loop_stack), by_name, tuple(callees),
                        "project" if callees else self.g.resolution_of(external or "<call>"),
                        arg_deps, kw_deps, set(recv), callbacks)
        self.g.call_sites[cn] = site
        if self.fn is not None:
            self.fn.call_sites[cn] = site
        for callee in callees:
            info = self.g.functions[callee]
            self.g.call_graph[self.scope].add(callee)
            for nm, defs in info.captured_writes.items():  # nested function mutated our variable
                env[nm] = self.lookup(env, nm) | defs
            params = info.params[1:] if info.is_method else info.params
            for p, d, a in zip(params, arg_deps, arg_exprs):
                self.bind_param(info, p, d, a, env)
            for k in c.keywords:
                if k.arg in info.params:
                    self.bind_param(info, k.arg, self.deps_of(k.value), k.value, env)
            ret = self.return_of(callee)
            self.g.add_edge(ret, cn, "ret")
            self.g.copies.add((ret, cn))
            # calls on self may write persistent attributes: later reads see the field
            if self.me is not None and isinstance(c.func, ast.Attribute) and isinstance(c.func.value, ast.Name) \
                    and c.func.value.id == self.me:
                for attr in self.field_writes.get(callee, ()):
                    key = f"self.{attr}"
                    env[key] = self.lookup(env, key) | self.fallback(key)
        # in-place mutation of the receiver or first argument
        target = None
        if isinstance(c.func, ast.Attribute) and c.func.attr in MUTATING_METHODS:
            target = c.func.value
        elif external in FIRST_ARG_MUTATORS and c.args:
            target = c.args[0]
        if target is not None:
            kept = {cn} | set().union(*(self.copied(a) for a in arg_exprs))
            self.weak_update(target, {cn} | set().union(*arg_deps, *kw_deps.values()), env, self.ctrl, c, kept)
        return {cn}

    def bind_param(self, info: FunctionInfo, p: str, deps: set[Node], arg: ast.expr, env: Env) -> None:
        """An argument becomes the callee's parameter unchanged (and carries any function it holds)."""
        pn = Node("param", p, info.qualname, info.file, info.node.lineno)
        self.link(deps, pn, "arg", copies=self.copied(arg))
        targets = self.fn_targets(arg, env)
        if targets:
            self.add_fnvals(pn, targets)

    def bind_callbacks(self, c: ast.Call, cn: Node, external: str | None, arg_exprs: list[ast.expr],
                       env: Env) -> dict[str, tuple[str, ...]]:
        """Summaries of library functions that call a function argument (see KEY_CALLBACK_CALLS etc.)."""
        if external is None:
            return {}
        kws = {k.arg: k.value for k in c.keywords if k.arg}
        specs: list[tuple[str, ast.expr, list[ast.expr]]] = []
        if external in KEY_CALLBACK_CALLS and "key" in kws:
            if external.startswith("heapq."):
                sources = arg_exprs[1:2]
            elif external == "method:sort":
                sources = [c.func.value]
            else:
                sources = arg_exprs
            specs.append(("key", kws["key"], sources))
        elif external in ELEMENT_CALLBACK_CALLS and arg_exprs:
            specs.append(("map", arg_exprs[0], arg_exprs[1:]))
        elif external in OPTIMISERS:
            fun = arg_exprs[0] if arg_exprs else kws.get("fun", kws.get("func"))
            x0 = arg_exprs[1] if len(arg_exprs) > 1 else kws.get("x0")
            if fun is not None:
                specs.append(("objective", fun, [x0] if x0 is not None else []))
        out: dict[str, tuple[str, ...]] = {}
        for role, fexpr, sources in specs:
            if role == "key" and isinstance(fexpr, ast.Attribute) and fexpr.attr in ("get", "__getitem__"):
                out[role] = ()  # key=table.get: a lookup; the table is already a dependence of the call
                continue
            targets = self.fn_targets(fexpr, env)
            if not targets:
                if not self._library_callable(fexpr, env):
                    self.g.unresolved_callbacks[cn] = ast.unparse(fexpr)[:60]
                continue
            out[role] = tuple(sorted(targets))
            for q in targets:
                info = self.g.functions[q]
                params = info.params[1:] if info.is_method else info.params
                self.g.call_graph[self.scope].add(q)
                self.g.add_edge(self.return_of(q), cn, "data")  # the result depends on what the callback returns
                if not params:
                    continue
                pairs = list(zip(params, sources)) if external == "map" else [(params[0], s) for s in sources]
                for p, src in pairs:
                    pn = Node("param", p, info.qualname, info.file, info.node.lineno)
                    self.link(self.deps_of(src), pn, "iter", copies=self.copied(src))
                if role == "objective":
                    self.g.decision_vars.add(Node("param", params[0], info.qualname, info.file, info.node.lineno))
                    extra = kws.get("args")
                    if isinstance(extra, ast.Tuple):
                        for p, elt in zip(params[1:], extra.elts):
                            pn = Node("param", p, info.qualname, info.file, info.node.lineno)
                            self.link(self.deps_of(elt), pn, "arg", copies=self.copied(elt))
                else:
                    for p, _ in pairs:
                        self.g.iter_vars.add(Node("param", p, info.qualname, info.file, info.node.lineno))
        return out

    def _library_callable(self, e: ast.expr, env: Env) -> bool:
        """``len``, ``np.abs``, ``operator.itemgetter(1)``: a callable from a builtin or library."""
        if isinstance(e, ast.Call):
            e = e.func
        name = _dotted(e)
        if name is None or name.split(".")[0] in env:
            return False
        q = self.qualify(name)
        return q in BUILTIN_NAMES or self.g.resolution_of(q) == "library"

    # ---- assignment
    def assign(self, t: ast.expr, deps: set[Node], env: Env, ctrl: frozenset, at: ast.AST,
               copies: set[Node] | dict[int, tuple[set[Node], set[Node]]] = frozenset(), kind: str = "data",
               fnvals: set[str] = frozenset()) -> list[Node]:
        """Bind targets; ``copies`` may give (deps, copies) per unpacked leaf. Returns the new defs."""
        per_leaf = copies if isinstance(copies, dict) else None
        made = []
        for leaf in _flatten_targets(t):
            leaf_deps, leaf_copies = deps, copies
            if per_leaf is not None:
                leaf_deps, leaf_copies = per_leaf.get(id(leaf), (deps, set()))
            if isinstance(leaf, ast.Name):
                d = self.new_def(leaf.id, at)
                self.link(leaf_deps, d, kind, copies=leaf_copies)
                self.link(ctrl, d, "control")
                env[leaf.id] = {d}
                made.append(d)
                if fnvals:
                    self.add_fnvals(d, fnvals)
                if self.mod and (self.fn is None and leaf.id in self.mod.globals or self.fn and leaf.id in self.fn.global_names):
                    self.g.add_edge(d, self.global_node(self.mod, leaf.id), "data")
                    if fnvals:
                        self.add_fnvals(self.global_node(self.mod, leaf.id), fnvals)
            elif isinstance(leaf, ast.Attribute) and self.me is not None and isinstance(leaf.value, ast.Name) \
                    and leaf.value.id == self.me:
                key = f"self.{leaf.attr}"
                d = self.new_def(key, at)
                self.link(leaf_deps, d, kind, copies=leaf_copies)
                self.link(ctrl, d, "control")
                env[key] = {d}
                made.append(d)
                if self.fn and self.fn.cls:
                    fnode = self.field_node(self.fn.cls, leaf.attr)
                    self.g.add_edge(d, fnode, "field_write")
                    self.g.copies.add((d, fnode))
                    if fnvals:
                        self.add_fnvals(d, fnvals)
                        self.add_fnvals(fnode, fnvals)
            else:  # x[i] = v, x.a = v, self.a[i] = v: in-place update of the root
                extra = self.expr(leaf.slice, env) if isinstance(leaf, ast.Subscript) else set()
                self.weak_update(leaf, leaf_deps | extra, env, ctrl, at, leaf_copies)
        return made

    def unpacked_parts(self, t: ast.expr, value: ast.expr) -> set[Node] | dict[int, tuple[set[Node], set[Node]]]:
        """Copies for ``a, b = value``, element by element when the elements are known: a tuple
        literal, or a call to a function whose every return is a tuple of that length. Then each
        target depends only on its own element."""
        if not isinstance(t, (ast.Tuple, ast.List)) or any(isinstance(x, ast.Starred) for x in t.elts):
            return self.copied(value)
        n = len(t.elts)
        if isinstance(value, (ast.Tuple, ast.List)) and len(value.elts) == n:
            parts = [(self.deps_of(x), self.copied(x)) for x in value.elts]
        else:
            call = value if isinstance(value, ast.Call) else None
            cs = next((cs for cs in self.fn.call_sites.values() if cs.ast_node is call), None) if call and self.fn else None
            info = self.g.functions.get(cs.callee) if cs and cs.callee and len(cs.callees) == 1 else None
            if info is None or _tuple_return_arity(info.node) != n:
                return self.copied(value)
            parts = [({_element_return(info, i)}, {_element_return(info, i)}) for i in range(n)]
        out: dict[int, tuple[set[Node], set[Node]]] = {}
        for sub, part in zip(t.elts, parts):
            for leaf in _flatten_targets(sub):
                out[id(leaf)] = part
        return out

    def weak_update(self, target: ast.expr, deps: set[Node], env: Env, ctrl: frozenset, at: ast.AST,
                    copies: set[Node] = frozenset()) -> None:
        """target is changed in place: new definition of its root that keeps the old value."""
        detail = f"[{ast.unparse(target.slice)}]" if isinstance(target, ast.Subscript) else ".weak"
        t = target
        while isinstance(t, (ast.Subscript, ast.Attribute)):
            if self.me is not None and isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name) and t.value.id == self.me:
                key = f"self.{t.attr}"
                d = self.new_def(key, at, detail)
                self.link(self.lookup(env, key), d, "base")
                self.link(deps, d, copies=copies)
                self.link(ctrl, d, "control")
                env[key] = {d}
                if self.fn and self.fn.cls:
                    fnode = self.field_node(self.fn.cls, t.attr)
                    self.g.add_edge(d, fnode, "field_write")
                    self.g.copies.add((d, fnode))
                return
            t = t.value
        if isinstance(t, ast.Name) and not (self.me is not None and t.id == self.me):
            d = self.new_def(t.id, at, detail)
            self.link(self.lookup(env, t.id), d, "base")
            self.link(deps, d, copies=copies)
            self.link(ctrl, d, "control")
            env[t.id] = {d}

    def const_value(self, e: ast.expr):
        """Literal value of e if statically known (constants and constant fields)."""
        if isinstance(e, ast.Constant):
            return e.value
        if self.me is not None and isinstance(e, ast.Attribute) and isinstance(e.value, ast.Name) \
                and e.value.id == self.me and self.fn and self.fn.cls:
            key = f"{_field_owner(self.g, self.fn.cls)}.{e.attr}"
            if key in self.g.constant_fields:
                return self.g.constant_fields[key]
        raise LookupError

    def eval_test(self, test: ast.expr):
        """True/False if a branch condition is decided by constants, else None."""
        import operator
        ops = {ast.Gt: operator.gt, ast.GtE: operator.ge, ast.Lt: operator.lt, ast.LtE: operator.le,
               ast.Eq: operator.eq, ast.NotEq: operator.ne, ast.Is: operator.is_, ast.IsNot: operator.is_not}
        try:
            if isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not):
                v = self.eval_test(test.operand)
                return None if v is None else not v
            if isinstance(test, ast.BoolOp):
                vals = [self.eval_test(v) for v in test.values]
                if isinstance(test.op, ast.And):
                    return False if False in vals else (True if all(v is True for v in vals) else None)
                return True if True in vals else (False if all(v is False for v in vals) else None)
            if isinstance(test, ast.Compare) and len(test.ops) == 1 and type(test.ops[0]) in ops:
                return bool(ops[type(test.ops[0])](self.const_value(test.left), self.const_value(test.comparators[0])))
            return bool(self.const_value(test))
        except (LookupError, TypeError):
            return None

    # ---- statements
    def block(self, stmts: list[ast.stmt], env: Env | None, ctrl: frozenset) -> Env | None:
        for s in stmts:
            if env is None:  # unreachable: nothing after an unconditional exit runs
                break
            env, ctrl = self.stmt(s, env, ctrl)
        return env

    def stmt(self, s: ast.stmt, env: Env, ctrl: frozenset) -> tuple[Env | None, frozenset]:
        """Analyse one statement. Returns the environment after it (None: does not complete)
        and the control context for the statements that follow it in the same block."""
        env = {k: set(v) for k, v in env.items()}
        self.ctrl = ctrl
        after = ctrl
        file = self.mod.file if self.mod else ""
        if isinstance(s, ast.Assign):
            deps = self.expr(s.value, env)
            fnv = self.fn_targets(s.value, env) if isinstance(s.value, (ast.Name, ast.Attribute, ast.Lambda, ast.Call)) else set()
            seq = isinstance(s.value, (ast.List, ast.Tuple, ast.ListComp)) or (
                isinstance(s.value, ast.Call) and _dotted(s.value.func) in ("list", "tuple"))
            for t in s.targets:
                made = self.assign(t, deps, env, ctrl, s, self.unpacked_parts(t, s.value), fnvals=fnv)
                if seq and isinstance(t, ast.Name):
                    self.g.sequence_defs.update(made)
        elif isinstance(s, ast.AnnAssign):
            if s.value is not None:
                fnv = self.fn_targets(s.value, env) if isinstance(s.value, (ast.Name, ast.Attribute, ast.Lambda)) else set()
                self.assign(s.target, self.expr(s.value, env), env, ctrl, s, self.copied(s.value), fnvals=fnv)
        elif isinstance(s, ast.AugAssign):
            vdeps = self.expr(s.value, env)
            tdeps = self.expr(s.target, env)
            if isinstance(s.op, (ast.Add, ast.Sub)):
                deps = {self.op_node(s, "+=" if isinstance(s.op, ast.Add) else "-=", tdeps, vdeps,
                                     self.copied(s.target), self.copied(s.value), (s.value,))}
                copies = set(deps)
            else:
                deps, copies = vdeps | tdeps, set()
            if isinstance(s.target, ast.Name) or (isinstance(s.target, ast.Attribute) and self.me is not None
                                                  and isinstance(s.target.value, ast.Name) and s.target.value.id == self.me):
                self.assign(s.target, deps, env, ctrl, s, copies)
            else:
                self.weak_update(s.target, deps, env, ctrl, s, copies)
        elif isinstance(s, ast.Expr):
            self.expr(s.value, env)
        elif isinstance(s, ast.If):
            decided = self.eval_test(s.test)
            if decided is False:
                self.g.pruned.append((file, s.lineno, f"if {ast.unparse(s.test)}", "body"))
                return self.block(s.orelse, env, ctrl), ctrl
            if decided is True:
                if s.orelse:
                    self.g.pruned.append((file, s.lineno, f"if {ast.unparse(s.test)}", "else"))
                return self.block(s.body, env, ctrl), ctrl
            tdeps = self.expr(s.test, env)
            self.g.test_deps[(self.scope, s.lineno, s.col_offset)] |= tdeps
            if any(isinstance(x, ast.Compare) and all(isinstance(o, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)) for o in x.ops)
                   and not any(_literal(v) is not _NONCONST for v in [x.left, *x.comparators]) for x in ast.walk(s.test)):
                self.g.ordering_tests.add((self.scope, s.lineno, s.col_offset))
            c = ctrl | tdeps
            body = self.block(s.body, {k: set(v) for k, v in env.items()}, c)
            orelse = self.block(s.orelse, env, c)
            env = self.merge(body, orelse)
            if (body is None) != (orelse is None):  # one branch exits early: what follows depends on the test
                after = c
        elif isinstance(s, (ast.For, ast.AsyncFor, ast.While)):
            env = self.loop(s, env, ctrl)
        elif isinstance(s, (ast.With, ast.AsyncWith)):
            for item in s.items:
                deps = self.expr(item.context_expr, env)
                if item.optional_vars is not None:
                    self.assign(item.optional_vars, deps, env, ctrl, s, self.copied(item.context_expr))
            env = self.block(s.body, env, ctrl)
        elif isinstance(s, ast.Try) or type(s).__name__ == "TryStar":
            after_body = self.block(s.body, {k: set(v) for k, v in env.items()}, ctrl)
            start = self.merge(env, after_body)  # an exception may leave the body before or after any statement
            branches = [self.block(s.orelse, after_body, ctrl) if after_body is not None else None]
            for h in s.handlers:
                henv = {k: set(v) for k, v in start.items()}
                if h.name:
                    henv[h.name] = set()
                branches.append(self.block(h.body, henv, ctrl))
            merged = self.merge(*branches)
            if s.finalbody:
                fin = self.block(s.finalbody, merged if merged is not None else start, ctrl)
                env = fin if merged is not None else None
            else:
                env = merged
        elif type(s).__name__ == "Match":  # Python >= 3.10
            c = ctrl | self.expr(s.subject, env)
            cases = []
            for case in s.cases:
                cenv = {k: set(v) for k, v in env.items()}
                if case.guard is not None:
                    self.expr(case.guard, cenv)
                cases.append(self.block(case.body, cenv, c))
            env = self.merge(env, *cases)
        elif isinstance(s, ast.Return):
            if self.fn is not None and self.fn.return_node is not None:
                rd = self.new_def("<return>", s)  # this return statement; the function's return merges them
                self.link(self.expr(s.value, env), rd, copies=self.copied(s.value))
                self.link(ctrl, rd, "control")
                self.link({rd}, self.fn.return_node, copies={rd})
                for elts in _tuple_alternatives(s.value) or ():  # element-wise, for callers that unpack it
                    for i, elt in enumerate(elts):
                        er = _element_return(self.fn, i)
                        self.link(self.deps_of(elt), er, copies=self.copied(elt))
                        self.link(ctrl, er, "control")
            else:
                self.expr(s.value, env)
            env = None
        elif isinstance(s, ast.Raise):
            self.expr(s.exc, env)
            self.expr(s.cause, env)
            env = None
        elif isinstance(s, ast.Break):
            if self.loop_ctx:
                self.loop_ctx[-1].breaks.append(env)
            env = None
        elif isinstance(s, ast.Continue):
            if self.loop_ctx:
                self.loop_ctx[-1].continues.append(env)
            env = None
        elif isinstance(s, ast.Assert):
            decided = self.eval_test(s.test)
            self.expr(s.test, env)
            if decided is False:
                env = None
        elif isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef)) and self.fn is not None:
            q = f"{self.fn.qualname}.{s.name}"
            info = self.g.functions.get(q)
            if info is None:
                info = _function_info(q, self.mod, s, None)
                info.cls = self.fn.cls  # closures over self see the same attributes
                info.parent = self.fn.qualname
                self.g.functions[q] = info
            self.fn.nested[s.name] = q
            self.analyze_function(info, closure=env, me=self.me)
            d = self.new_def(s.name, s)  # the name now holds the function
            self.g.add_edge(self.return_of(q), d, "data")
            self.add_fnvals(d, {q})
            env[s.name] = {d}
        self.ctrl = ctrl
        return env, after

    def loop(self, s, env: Env, ctrl: frozenset) -> Env | None:
        is_while = isinstance(s, ast.While)
        decided = self.eval_test(s.test) if is_while else None
        if decided is False:  # `while False:` / a constant setting: the body never runs
            self.g.pruned.append((self.mod.file if self.mod else "", s.lineno, f"while {ast.unparse(s.test)}", "body"))
            return self.block(s.orelse, env, ctrl)
        info = self.fn.loops.get(s.lineno) if self.fn is not None else None
        if info is None:
            info = LoopInfo(self.scope, "while" if is_while else "for", s.lineno, getattr(s, "end_lineno", s.lineno))
            self._scan_loop(s, info)
            if self.fn is not None:
                self.fn.loops[s.lineno] = info
        self.loop_stack.append(info)
        breaks: list[Env] = []
        cur = env
        try:
            for _ in range(12):
                ctx = _LoopCtx()
                self.loop_ctx.append(ctx)
                try:
                    e = {k: set(v) for k, v in cur.items()}
                    self.ctrl = ctrl
                    if is_while:
                        c = ctrl if decided is True else ctrl | self.expr(s.test, e)
                    else:
                        it = self.expr(s.iter, e)
                        made = self.assign(s.target, it, e, ctrl, s, self.copied(s.iter), kind="iter")
                        self.g.iter_vars.update(made)
                        c = ctrl | it
                    end = self.block(s.body, e, c)
                finally:
                    self.loop_ctx.pop()
                breaks = ctx.breaks
                new = self.merge(env, end, *ctx.continues)
                if new == cur:
                    break
                cur = new
        finally:
            self.loop_stack.pop()
        normal = None if decided is True else cur  # leaving because the test failed / the iterable ran out
        after = self.block(s.orelse, normal, ctrl) if normal is not None else None
        return self.merge(after, *breaks)

    def _scan_loop(self, s, info: LoopInfo) -> None:
        """Best-so-far updates (``if c < best: best = c; choice = a``) and search loop shapes."""
        for n in _walk(s.body, into_loops=False):
            if not isinstance(n, ast.If):
                continue
            # any ordering comparison in the condition, e.g. `best is None or c < best[0]`
            compares = [c for c in ast.walk(n.test) if isinstance(c, ast.Compare)
                        and all(isinstance(o, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)) for o in c.ops)]
            compared = {_root_dotted(x) for c in compares for x in [c.left, *c.comparators]} - {None}
            assigns = []
            for st in _walk(n.body, into_loops=False):
                if isinstance(st, ast.Assign):
                    targets = st.targets
                elif isinstance(st, ast.AnnAssign) and st.value is not None:
                    targets = [st.target]
                else:
                    continue
                for t in targets:
                    for leaf in _flatten_targets(t):
                        if _dotted(leaf):
                            assigns.append((_dotted(leaf), st.lineno, st.col_offset))
            hit = compared & {a[0] for a in assigns}
            if hit:
                var = sorted(hit)[0]
                info.best_updates.append(BestUpdate(n.lineno, n.col_offset, getattr(n, "end_lineno", n.lineno), var,
                                                    sorted({a[0] for a in assigns} - {var}),
                                                    [(a[1], a[2]) for a in assigns]))
        # worklist (in `while q:` or a bounded `for _ in range(n):` loop): pop an element, push its successors,
        # and remember visited ones
        # The pop belongs to this loop's own body (a loop that merely contains a search loop is not one);
        # successors may be pushed from an inner loop over neighbours.
        pops: dict[str, list[ast.Call]] = defaultdict(list)
        pushes: dict[str, list[ast.Call]] = defaultdict(list)
        own = {id(n) for n in _walk(s.body, into_loops=False)}
        for n in _walk(s.body, into_loops=True):
            if not isinstance(n, ast.Call):
                continue
            q = self.qualify(_dotted(n.func)) if _dotted(n.func) else ""
            if q in ("heapq.heappop", "heapq.heappushpop", "heapq.heapreplace") and n.args and id(n) in own:
                pops[_root_dotted(n.args[0])].append(n)
            if q in ("heapq.heappush", "heapq.heappushpop", "heapq.heapreplace") and n.args:
                pushes[_root_dotted(n.args[0])].append(n)
            if isinstance(n.func, ast.Attribute):
                cont = _dotted(n.func.value)
                if n.func.attr in ("pop", "popleft") and id(n) in own:
                    pops[cont].append(n)
                if n.func.attr in ("append", "appendleft", "extend", "add", "put"):
                    pushes[cont].append(n)
        for frontier in sorted(set(pops) & set(pushes) - {None}):
            closed = self._closed_tables(s, frontier)
            if closed:
                info.frontiers.append(Frontier("worklist", frontier, s.lineno, pops[frontier], pushes[frontier],
                                               closed))
        self._scan_relaxation(s, info)
        for inner in _walk(s.body, into_loops=True):  # layered: expand every element of the current layer
            if not isinstance(inner, (ast.For, ast.AsyncFor)):
                continue
            layer = _iter_container(inner.iter)
            if not layer:
                continue
            branching = set()  # containers filled inside an iteration over each element's successors
            for sub in _walk(inner.body, into_loops=True):
                if isinstance(sub, (ast.For, ast.AsyncFor)):
                    branching |= _written_containers(sub.body)
                elif isinstance(sub, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
                    branching |= _written_containers([sub])
            for nxt in sorted(branching - {layer}):
                info.frontiers.append(Frontier("layered", layer, s.lineno, next_layer=nxt,
                                               inner=(inner.lineno, getattr(inner, "end_lineno", inner.lineno))))

    @staticmethod
    def _scan_relaxation(s, info: LoopInfo) -> None:
        """Relaxation: a cost-table entry is replaced where a candidate compares smaller, and a
        predecessor table is written with the same keys (``if c < cost[k]: cost[k] = c; parent[k] = u``,
        or vectorised with a mask). The classifier checks that candidates come from earlier costs."""
        own = list(_walk(s.body, into_loops=False))
        stores = []  # (table, names in the index, (line, col), root of the stored value)
        for st in own:
            if not isinstance(st, ast.Assign) or len(st.targets) != 1:
                continue
            t, v = st.targets[0], st.value
            pairs = list(zip(t.elts, v.elts)) if isinstance(t, (ast.Tuple, ast.List)) and \
                isinstance(v, (ast.Tuple, ast.List)) and len(t.elts) == len(v.elts) else [(t, v)]
            for leaf, val in pairs:
                if isinstance(leaf, ast.Subscript) and _root_dotted(leaf):
                    keys = {x.id for x in ast.walk(leaf.slice) if isinstance(x, ast.Name)}
                    stores.append((_root_dotted(leaf), keys, (st.lineno, st.col_offset), _root_dotted(val)))
        compared = set()
        for c in own:
            if isinstance(c, ast.Compare) and all(isinstance(o, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)) for o in c.ops):
                for x in [c.left, *c.comparators]:
                    if isinstance(x, ast.Subscript):
                        compared.add(_root_dotted(x))
                    elif isinstance(x, ast.Call) and isinstance(x.func, ast.Attribute) and x.func.attr == "get":
                        compared.add(_dotted(x.func.value))
        for table in sorted({st[0] for st in stores} & compared - {None}):
            mine = [st for st in stores if st[0] == table]
            keys = set().union(*(st[1] for st in mine))
            preds = sorted({st[0] for st in stores if st[0] != table and st[1] & keys})
            roots = sorted({st[3] for st in mine if st[3]})
            if keys and preds and roots:
                info.frontiers.append(Frontier("relaxation", table, s.lineno, closed=preds,
                                               writes=[st[2] for st in mine], value_roots=roots))

    @staticmethod
    def _closed_tables(s: ast.While | ast.For, frontier: str) -> list[str]:
        """Tables written in the loop and consulted in one of its tests (visited / cost / parent)."""
        written = _written_containers(s.body)
        tested: set[str] = set()
        tests = [s.test] if isinstance(s, ast.While) else []
        tests += [n.test for n in _walk(s.body, True) if isinstance(n, (ast.If, ast.While, ast.IfExp))]
        tests += [c for n in _walk(s.body, True) if isinstance(n, ast.comprehension) for c in n.ifs]
        for t in tests:
            for x in ast.walk(t):
                if isinstance(x, ast.Compare) and any(isinstance(o, (ast.In, ast.NotIn)) for o in x.ops):
                    tested |= {_root_dotted(c) for c in x.comparators}
                elif isinstance(x, ast.Subscript):
                    tested.add(_root_dotted(x))
                elif isinstance(x, ast.Call) and isinstance(x.func, ast.Attribute) and x.func.attr in ("get", "__contains__"):
                    tested.add(_dotted(x.func.value))
        return sorted((written & tested) - {frontier, None})
