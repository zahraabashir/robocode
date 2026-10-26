"""Conservative, static counts of recognised hypothetical state updates.

This module never imports or executes a policy. The small AST interpreter carries
only constants, collection shapes and hypothetical depths. Unsupported execution
shapes yield unknown scores; classification remains the responsibility of reactivity.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass

VERSION = "planning-scores-1"
DEPTH_DESCRIPTION = "How far ahead does this policy reason?"
WORK_DESCRIPTION = "How much hypothetical exploration does this policy perform?"
SCOPE = "Recognised action-relevant hypothetical updates in one decision invocation."


@dataclass
class PlanningScores:
    depth: int | None = None
    work: int | None = None
    reason: str = "Scores have not been computed."
    sites: tuple = ()

    def to_dict(self):
        return {
            "version": VERSION,
            "scope": SCOPE,
            "basis": "static; conditional on the classifier's transition assumptions; not a runtime measurement",
            "planning_depth": {"value": self.depth, "status": "exact" if self.depth is not None else "unknown",
                               "unit": "successive hypothetical updates", "description": DEPTH_DESCRIPTION},
            "planning_work": {"value": self.work, "status": "exact" if self.work is not None else "unknown",
                              "unit": "hypothetical update evaluations", "description": WORK_DESCRIPTION},
            "reason": self.reason,
            "sites": [{"file": n.file, "line": n.line, "function": n.scope} for n in self.sites],
        }

    def text(self):
        depth = "unknown" if self.depth is None else str(self.depth)
        work = "unknown" if self.work is None else str(self.work)
        return [f"planning depth: {depth}  ({DEPTH_DESCRIPTION})",
                f"planning work: {work}  ({WORK_DESCRIPTION})", f"  score basis: {self.reason}"]


class _Unknown(Exception):
    pass


_MISSING = object()


@dataclass(frozen=True)
class _Value:
    depth: int | None = 0
    constant: object = _MISSING
    items: tuple | None = None


def _combine(values):
    values = list(values)
    return _Value(None if any(v.depth is None for v in values) else max((v.depth for v in values), default=0))


def _join(a, b):
    if a == b:
        return a
    return _Value(a.depth if a.depth == b.depth else None)


def quantify(classifier, evidence, review):
    """Use the existing verdict/evidence; never supply input to classification."""
    if review:
        return PlanningScores(reason="Unresolved action-relevant code prevents a complete count.")
    if not evidence:
        return PlanningScores(0, 0, "No action-relevant planning recognised under the current rubric.")
    g = classifier.g
    reachable = g.reachable_functions(classifier.decision)
    if any(e.function not in reachable for e in evidence):
        return PlanningScores(reason="Planning is cached or computed outside the decision call; its generation cost is unknown.")
    unsupported = sorted({e.kind for e in evidence} - {"lookahead"})
    if unsupported:
        return PlanningScores(reason="No static update-count contract for: " + ", ".join(unsupported) + ".")
    winners = set().union(*(set(e.winners) for e in evidence))
    events = set()
    for ch in classifier._choices(classifier.slice):
        if ch.winners & winners:
            ops, models, rolls = classifier._predictions(ch)
            if models:
                return PlanningScores(reason="A configured model has no declared single-step counting contract.")
            events.update(ops + rolls)
    sites = tuple(sorted(events, key=lambda n: (n.file, n.line, n.col)))
    if not events:
        return PlanningScores(reason="No countable hypothetical updates could be isolated.")
    if any(n.scope not in reachable for n in events):
        return PlanningScores(reason="A hypothetical update is outside the resolved decision call tree.", sites=sites)
    state_sides = {
        n: "left" if n in classifier.H_roll or
        (g.ops[n].left_copy & classifier.SL and classifier._pure_candidate(g.ops[n].right)) else "right"
        for n in events
    }
    counter = _Counter(g, events, classifier.slice, state_sides)
    try:
        counter.function(classifier.decision, [], {})
        if counter.seen != events or counter.work == 0:
            raise _Unknown("Not all recognised prediction sites could be counted in the decision call.")
        return PlanningScores(counter.depth, counter.work,
                              "Fixed, fully traversed hypothetical updates; repeated evaluations count again. "
                              "Action conversion and score arithmetic add no steps.", sites)
    except (_Unknown, RecursionError) as exc:
        return PlanningScores(reason=str(exc) or "Static scoring recursion limit reached.", sites=sites)


class _Counter:
    LIMIT = 10000  # bounded analysis, independent of policy runtime

    def __init__(self, graph, events, action_slice, state_sides):
        self.g = graph
        self.action_slice = action_slice
        self.state_sides = state_sides
        self.events = {(n.scope, n.line, n.col): n for n in events}
        self.calls = {(cs.function, cs.ast_node.lineno, cs.ast_node.col_offset): cs
                      for cs in graph.call_sites.values()}
        self.seen = set()
        self.depth = self.work = self.visits = 0
        self.stack = []

    def tick(self):
        self.visits += 1
        if self.visits > self.LIMIT:
            raise _Unknown("Static counting budget exceeded; no partial total is reported.")

    def update(self, node, scope, left, right):
        event = self.events.get((scope, node.lineno, node.col_offset))
        if event is not None:
            value = left if self.state_sides[event] == "left" else right
            if value.depth is None:
                raise _Unknown("The input depth of a hypothetical update depends on an unresolved branch.")
            value = _Value(value.depth + 1)
            self.work += 1
            self.depth = max(self.depth, value.depth)
            self.seen.add(event)
            return value
        return _combine([left, right])

    def function(self, scope, args, kwargs, closure=None):
        self.tick()
        if scope in self.stack:
            raise _Unknown("Recursive planning needs a runtime or bounded-search count.")
        f = self.g.functions[scope]
        if getattr(f.node, "decorator_list", ()):
            raise _Unknown("Decorated helper execution cannot be counted statically.")
        if isinstance(f.node, ast.AsyncFunctionDef) or f.node.args.vararg or f.node.args.kwarg or f.node.args.kwonlyargs:
            raise _Unknown("Async or variadic helper execution is not supported by static scoring.")
        env = {}
        # Literal module constants only; no policy code is executed during analysis.
        for stmt in self.g.modules[f.module].tree.body:
            if isinstance(stmt, (ast.Assign, ast.AnnAssign)):
                targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
                if all(isinstance(t, ast.Name) for t in targets):
                    value = self.literal(stmt.value, env)
                    for target in targets:
                        env[target.id] = value
        if f.parent and closure:
            env.update(closure)
        defaults = [None] * (len(f.params) - len(f.node.args.defaults)) + list(f.node.args.defaults)
        for i, name in enumerate(f.params):
            env[name] = args[i] if i < len(args) else kwargs.get(name, self.literal(defaults[i], env))
        self.stack.append(scope)
        try:
            if isinstance(f.node, ast.Lambda):
                return self.expr(f.node.body, env, scope)
            returned, value = self.block(f.node.body, env, scope)
            return value if returned else _Value()
        finally:
            self.stack.pop()

    def literal(self, node, env):
        if isinstance(node, ast.Constant):
            return _Value(constant=node.value)
        if isinstance(node, ast.Name):
            return env.get(node.id, _Value())
        if isinstance(node, (ast.List, ast.Tuple)):
            return _Value(items=tuple(self.literal(x, env) for x in node.elts))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            v = self.literal(node.operand, env)
            if type(v.constant) is int:
                return _Value(constant=-v.constant if isinstance(node.op, ast.USub) else v.constant)
        return _Value()

    def assign(self, target, value, env):
        if isinstance(target, ast.Name):
            env[target.id] = value
        elif isinstance(target, (ast.Tuple, ast.List)):
            for i, item in enumerate(target.elts):
                self.assign(item, value.items[i] if value.items and i < len(value.items) else _Value(value.depth), env)
        elif isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name):
            # Containers used to collect scores lose their precise shape, but keep provenance.
            name = target.value.id
            env[name] = _combine([env.get(name, _Value()), value])
        else:
            raise _Unknown("Mutable fields or aliased state writes need a separate counting model.")

    def block(self, body, env, scope):
        for stmt in body:
            self.tick()
            if isinstance(stmt, ast.Return):
                return True, self.expr(stmt.value, env, scope)
            if isinstance(stmt, (ast.Assign, ast.AnnAssign)):
                value = self.expr(stmt.value, env, scope)
                for target in stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]:
                    self.assign(target, value, env)
            elif isinstance(stmt, ast.AugAssign):
                left, right = self.expr(stmt.target, env, scope), self.expr(stmt.value, env, scope)
                self.assign(stmt.target, self.update(stmt, scope, left, right), env)
            elif isinstance(stmt, ast.Expr):
                self.expr(stmt.value, env, scope)
            elif isinstance(stmt, ast.For):
                values = self.expr(stmt.iter, env, scope).items
                if values is None:
                    raise _Unknown("A loop's iteration count depends on runtime data.")
                for value in values:
                    self.assign(stmt.target, value, env)
                    returned, result = self.block(stmt.body, env, scope)
                    if returned:
                        return True, result
                returned, result = self.block(stmt.orelse, env, scope)
                if returned:
                    return True, result
            elif isinstance(stmt, ast.If):
                test = self.expr(stmt.test, env, scope)
                if test.constant is not _MISSING:
                    returned, result = self.block(stmt.body if test.constant else stmt.orelse, env, scope)
                    if returned:
                        return True, result
                else:
                    before = (self.work, self.depth, self.seen.copy())
                    left, right = dict(env), dict(env)
                    lr, lv = self.block(stmt.body, left, scope)
                    lcounts = (self.work, self.depth, self.seen.copy())
                    self.work, self.depth, self.seen = before
                    rr, rv = self.block(stmt.orelse, right, scope)
                    if (self.work, self.depth, self.seen) != lcounts or lr != rr:
                        raise _Unknown("Planning amount or early exit depends on a runtime branch.")
                    if lr:
                        return True, _join(lv, rv)
                    env.update({k: _join(left.get(k, _Value()), right.get(k, _Value())) for k in left.keys() | right.keys()})
            elif isinstance(stmt, (ast.FunctionDef, ast.Import, ast.ImportFrom, ast.Pass)):
                continue
            else:
                raise _Unknown(f"Static scoring does not resolve {type(stmt).__name__} execution.")
        return False, _Value()

    def expr(self, node, env, scope):
        self.tick()
        if node is None:
            return _Value()
        if isinstance(node, (ast.Constant, ast.Name)):
            return self.literal(node, env)
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            values = tuple(self.expr(x, env, scope) for x in node.elts)
            if isinstance(node, ast.Set):
                raise _Unknown("Set iteration cardinality is not supported by static scoring.")
            return _Value(_combine(values).depth, items=values)
        if isinstance(node, ast.Dict):
            return _combine(self.expr(x, env, scope) for x in [*node.keys, *node.values] if x is not None)
        if isinstance(node, ast.Attribute):
            return _Value(self.expr(node.value, env, scope).depth)
        if isinstance(node, ast.Subscript):
            value = self.expr(node.value, env, scope)
            index = self.expr(node.slice, env, scope)
            if value.items is not None and type(index.constant) is int:
                try:
                    return value.items[index.constant]
                except IndexError:
                    raise _Unknown("A static collection index is out of range.") from None
            if value.items is not None and len({v.depth for v in value.items}) > 1:
                return _Value(None)
            return _Value(value.depth)
        if isinstance(node, ast.BinOp):
            left, right = self.expr(node.left, env, scope), self.expr(node.right, env, scope)
            value = self.update(node, scope, left, right)
            if value.depth == 0 and type(left.constant) is int and type(right.constant) is int:
                a, b = left.constant, right.constant
                if isinstance(node.op, ast.Add):
                    return _Value(constant=a + b)
                if isinstance(node.op, ast.Sub):
                    return _Value(constant=a - b)
                if isinstance(node.op, ast.Mult) and abs(a) < self.LIMIT and abs(b) < self.LIMIT:
                    return _Value(constant=a * b)
            return value
        if isinstance(node, ast.UnaryOp):
            value = self.expr(node.operand, env, scope)
            if type(value.constant) is int and isinstance(node.op, (ast.USub, ast.UAdd)):
                return _Value(constant=-value.constant if isinstance(node.op, ast.USub) else value.constant)
            return _Value(value.depth)
        if isinstance(node, ast.Compare):
            self.expr(node.left, env, scope)
            for x in node.comparators:
                self.expr(x, env, scope)
            return _Value()
        if isinstance(node, ast.Lambda):
            return _Value()
        if isinstance(node, (ast.ListComp, ast.GeneratorExp)):
            if isinstance(node, ast.GeneratorExp):
                raise _Unknown("Lazy generator consumption is not counted statically; use an eager comprehension for fixed counts.")
            values = []
            def visit(i, local):
                if i == len(node.generators):
                    values.append(self.expr(node.elt, local, scope))
                    return
                gen = node.generators[i]
                if gen.ifs or gen.is_async:
                    raise _Unknown("Filtered or async candidate counts depend on execution.")
                items = self.expr(gen.iter, local, scope).items
                if items is None:
                    raise _Unknown("Candidate count depends on runtime data.")
                for value in items:
                    self.assign(gen.target, value, local)
                    visit(i + 1, dict(local))
            visit(0, dict(env))
            return _Value(_combine(values).depth, items=tuple(values))
        if isinstance(node, ast.Call):
            return self.call(node, env, scope)
        raise _Unknown(f"Static scoring does not resolve {type(node).__name__} expressions.")

    def call(self, node, env, scope):
        cs = self.calls.get((scope, node.lineno, node.col_offset))
        if any(isinstance(a, ast.Starred) for a in node.args) or any(k.arg is None for k in node.keywords):
            raise _Unknown("Expanded call arguments are not supported by static scoring.")
        args = [self.expr(a, env, scope) for a in node.args]
        kwargs = {k.arg: self.expr(k.value, env, scope) for k in node.keywords}
        if cs and len(cs.callees) == 1:
            if cs.node not in self.action_slice:
                # Shared helper bodies are context-insensitive in the graph. A separate
                # discarded call must not multiply the action-relevant computation.
                if any(n.scope in self.g.reachable_functions(cs.callees[0]) for n in self.events.values()):
                    raise _Unknown("A prediction helper is shared with a discarded call; context-specific counts are unresolved.")
            callee = self.g.functions[cs.callees[0]]
            if callee.is_method and isinstance(node.func, ast.Attribute) and callee.params[:1] == ["self"]:
                args = [self.expr(node.func.value, env, scope)] + args
            return self.function(cs.callees[0], args, kwargs, env)
        if cs and cs.callees:
            raise _Unknown("The helper call has multiple possible targets.")
        name = cs.external if cs else None
        if name == "range":
            if not 1 <= len(args) <= 3 or any(type(v.constant) is not int for v in args):
                raise _Unknown("A range bound depends on runtime data.")
            try:
                values = range(*(v.constant for v in args))
                if len(values) > self.LIMIT:
                    raise _Unknown("Static counting budget exceeded by a loop bound.")
                return _Value(items=tuple(_Value(constant=v) for v in values))
            except (ValueError, OverflowError):
                raise _Unknown("A range bound is invalid or too large.") from None
        if name == "len" and len(args) == 1 and args[0].items is not None:
            return _Value(constant=len(args[0].items))
        if name in {"min", "max", "sorted"} and "key" in kwargs:
            callbacks = cs.callbacks.get("key", ()) if cs else ()
            if callbacks:
                if len(callbacks) != 1 or not args or args[0].items is None:
                    raise _Unknown("The key callback's evaluation count is unknown.")
                for item in args[0].items:
                    callback = self.g.functions[callbacks[0]]
                    params = [_Value(), item] if callback.is_method else [item]
                    self.function(callbacks[0], params, {}, env)
        if cs and cs.callbacks and not (name in {"min", "max", "sorted"} and "key" in kwargs):
            raise _Unknown("This callback's invocation count is not supported by static scoring.")
        if isinstance(node.func, ast.Attribute):
            receiver = self.expr(node.func.value, env, scope)
            if node.func.attr == "append" and isinstance(node.func.value, ast.Name) and len(args) == 1:
                if len(self.stack) > 1 or any(v is receiver for k, v in env.items() if k != node.func.value.id):
                    raise _Unknown("Aliased or helper-mutated collections need a separate counting model.")
                env[node.func.value.id] = _Value(_combine([receiver, args[0]]).depth,
                                                items=receiver.items + (args[0],) if receiver.items is not None else None)
                return _Value()
            if node.func.attr in {"extend", "pop", "clear", "remove", "insert", "update", "sort", "reverse"}:
                raise _Unknown("Mutable collection operations need a separate counting model.")
            args.append(receiver)
        # Arithmetic/scoring/encoding calls do not themselves add model steps.
        return _combine([*args, *kwargs.values()])
