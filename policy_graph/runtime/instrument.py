"""Compile instrumentation in memory; policy variables retain their real types."""

# AST dispatch methods mirror Recorder's private instrumentation protocol.
# pylint: disable=missing-function-docstring

from __future__ import annotations

import ast
import hashlib
import re

from .graph import Site

_LINE_END = re.compile(r"\r\n|\r|\n")


class _Segments:
    """``ast.get_source_segment`` without re-splitting the source for every node."""

    def __init__(self, source):
        self.lines, start = [], 0
        for match in _LINE_END.finditer(source):
            self.lines.append(source[start : match.end()])
            start = match.end()
        if start < len(source):
            self.lines.append(source[start:])
        self.encoded = {}

    def line(self, index):
        if index not in self.encoded:
            self.encoded[index] = self.lines[index].encode()
        return self.encoded[index]

    def __call__(self, node, limit=160):
        try:
            first, last = node.lineno - 1, node.end_lineno - 1
            start, end = node.col_offset, node.end_col_offset
        except AttributeError:
            return ""
        if first < 0 or last >= len(self.lines) or end is None or last < first:
            return ""
        if first == last:
            return self.line(first)[start:end].decode(errors="replace")[:limit]
        parts = [self.line(first)[start:].decode(errors="replace")]
        for index in range(first + 1, last):
            if sum(map(len, parts)) >= limit:
                break
            parts.append(self.lines[index])
        else:
            parts.append(self.line(last)[:end].decode(errors="replace"))
        return "".join(parts)[:limit]


def _exit_kind(node):
    if isinstance(
        node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)
    ):
        return 0
    if isinstance(node, (ast.Return, ast.Raise)):
        return 2
    if isinstance(node, (ast.Break, ast.Continue)):
        return 1
    return max((_exit_kind(child) for child in ast.iter_child_nodes(node)), default=0)


class Instrumenter:
    """Rewrite supported syntax and mark the rest as opaque without rewriting it."""

    def __init__(self, recorder, file, source):
        self.recorder, self.file, self.source = recorder, file, source
        self.scope = "<module>"
        self.serial = 0
        self.segment = _Segments(source)
        digest = hashlib.sha256(source.encode()).hexdigest()[:12]
        self.name = f"_pg_runtime_{digest}"
        while self.name in source:
            self.name += "_"

    def temp(self):
        self.serial += 1
        return f"{self.name}_{self.serial}"

    def site(self, node):
        return ast.Constant(
            self.recorder.site(
                Site(
                    self.file,
                    getattr(node, "lineno", 0),
                    getattr(node, "col_offset", 0),
                    self.scope,
                    self.segment(node),
                )
            )
        )

    def rt(self, method, *args, **kwargs):
        return ast.Call(
            ast.Attribute(ast.Name(self.name, ast.Load()), method, ast.Load()),
            list(args),
            [ast.keyword(k, v) for k, v in kwargs.items()],
        )

    def thunk(self, expression):
        return ast.Lambda(
            ast.arguments(
                posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]
            ),
            expression,
        )

    def const(self, node, value):
        return self.rt("literal", self.site(node), ast.Constant(value))

    def expr(self, node):
        if node is None:
            return self.const(ast.Constant(None), None)
        site = self.site(node)
        if isinstance(node, ast.Constant):
            out = self.rt("literal", site, node)
        elif isinstance(node, ast.Name):
            out = self.rt("read", site, ast.Constant(node.id), node)
        elif isinstance(node, ast.Attribute):
            out = self.rt(
                "get_attr", site, self.expr(node.value), ast.Constant(node.attr)
            )
        elif isinstance(node, ast.Subscript):
            out = self.rt(
                "subscript", site, self.expr(node.value), self.key(node.slice)
            )
        elif isinstance(node, ast.Slice):
            out = self.rt(
                "slice_value",
                site,
                self.expr(node.lower),
                self.expr(node.upper),
                self.expr(node.step),
            )
        elif isinstance(node, ast.BinOp):
            out = self.rt(
                "binary",
                site,
                ast.Constant(type(node.op).__name__),
                self.expr(node.left),
                self.expr(node.right),
            )
        elif isinstance(node, ast.UnaryOp):
            out = self.rt(
                "unary",
                site,
                ast.Constant(type(node.op).__name__),
                self.expr(node.operand),
            )
        elif isinstance(node, ast.Compare):
            # Thunks preserve short-circuiting and evaluate intermediate operands once.
            out = self.rt(
                "compare_chain",
                site,
                self.expr(node.left),
                ast.List(
                    [ast.Constant(type(op).__name__) for op in node.ops], ast.Load()
                ),
                ast.List(
                    [self.thunk(self.expr(v)) for v in node.comparators], ast.Load()
                ),
            )
        elif isinstance(node, ast.BoolOp):
            out = self.rt(
                "boolean",
                site,
                ast.Constant(type(node.op).__name__),
                ast.List([self.thunk(self.expr(v)) for v in node.values], ast.Load()),
            )
        elif isinstance(node, ast.IfExp):
            out = self.rt(
                "conditional",
                site,
                self.expr(node.test),
                self.thunk(self.expr(node.body)),
                self.thunk(self.expr(node.orelse)),
            )
        elif isinstance(node, (ast.List, ast.Tuple, ast.Set)) and not any(
            isinstance(v, ast.Starred) for v in node.elts
        ):
            out = self.rt(
                "container",
                site,
                ast.Constant(type(node).__name__.lower()),
                ast.List([self.expr(v) for v in node.elts], ast.Load()),
            )
        elif isinstance(node, ast.Dict) and all(k is not None for k in node.keys):
            out = self.rt(
                "container",
                site,
                ast.Constant("dict"),
                ast.List(
                    [
                        ast.Tuple([self.expr(k), self.expr(v)], ast.Load())
                        for k, v in zip(node.keys, node.values)
                    ],
                    ast.Load(),
                ),
            )
        elif (
            isinstance(node, ast.Call)
            and not any(isinstance(a, ast.Starred) for a in node.args)
            and all(k.arg is not None for k in node.keywords)
        ):
            out = self.rt(
                "call",
                site,
                self.expr(node.func),
                ast.List([self.expr(a) for a in node.args], ast.Load()),
                ast.Dict(
                    [ast.Constant(k.arg) for k in node.keywords],
                    [self.expr(k.value) for k in node.keywords],
                ),
            )
        elif (
            isinstance(node, ast.Lambda)
            and not node.args.vararg
            and not node.args.kwarg
        ):
            self.defaults(node.args, site)
            body = self.rt("return_value", site, self.expr(node.body))
            fn = ast.Lambda(node.args, body)
            decorated = ast.Call(self.rt("function", site), [fn], [])
            out = self.rt("literal", site, decorated)
        elif isinstance(
            node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
        ) and all(not g.is_async for g in node.generators):
            try:
                generators = [
                    ast.comprehension(
                        g.target,
                        self.rt(
                            "comp_iter",
                            self.site(g),
                            self.expr(g.iter),
                            self.target_literal(g.target),
                        ),
                        [
                            self.rt("truth", self.site(test), self.expr(test))
                            for test in g.ifs
                        ],
                        0,
                    )
                    for g in node.generators
                ]
                if isinstance(node, ast.DictComp):
                    inner = ast.ListComp(
                        ast.Tuple(
                            [self.expr(node.key), self.expr(node.value)], ast.Load()
                        ),
                        generators,
                    )
                    kind = "dict"
                elif isinstance(node, ast.GeneratorExp):
                    inner = ast.GeneratorExp(self.expr(node.elt), generators)
                    kind = "generator"
                else:
                    inner = ast.ListComp(self.expr(node.elt), generators)
                    kind = "list" if isinstance(node, ast.ListComp) else "set"
                out = self.rt(
                    "comprehension", site, ast.Constant(kind), self.thunk(inner)
                )
            except ValueError:
                out = self.opaque_expr(node, site)
        else:
            out = self.opaque_expr(node, site)
        return ast.copy_location(out, node)

    def key(self, node):
        """An index tuple ``a[i, j]`` is only a key: no element provenance needed."""
        if isinstance(node, ast.Tuple) and not any(
            isinstance(e, ast.Starred) for e in node.elts
        ):
            return ast.copy_location(
                self.rt(
                    "index",
                    self.site(node),
                    ast.List([self.expr(e) for e in node.elts], ast.Load()),
                ),
                node,
            )
        return self.expr(node)

    def opaque_expr(self, node, site):
        return self.rt(
            "opaque",
            site,
            node,
            ast.List([], ast.Load()),
            ast.Constant(f"Unsupported expression: {type(node).__name__}"),
        )

    def target_literal(self, target):
        if isinstance(target, ast.Name):
            return ast.Constant(target.id)
        if isinstance(target, (ast.Tuple, ast.List)):
            return ast.Tuple([self.target_literal(t) for t in target.elts], ast.Load())
        raise ValueError("Unsupported binding target")

    def assign(self, node, target, value):
        site = self.site(node)
        if isinstance(target, ast.Name):
            return [
                ast.Assign(
                    [target], self.rt("bind", site, ast.Constant(target.id), value)
                )
            ]
        if isinstance(target, ast.Attribute):
            return [
                ast.Expr(
                    self.rt(
                        "set_attr",
                        site,
                        self.expr(target.value),
                        ast.Constant(target.attr),
                        value,
                    )
                )
            ]
        if isinstance(target, ast.Subscript):
            return [
                ast.Expr(
                    self.rt(
                        "set_item",
                        site,
                        self.expr(target.value),
                        self.key(target.slice),
                        value,
                    )
                )
            ]
        if isinstance(target, (ast.Tuple, ast.List)):
            literal = self.target_literal(target)
            return [ast.Assign([target], self.rt("bind_target", site, literal, value))]
        raise ValueError("Unsupported assignment target")

    def parallel(self, node, targets):
        """``a, b = x, y`` binds from temporaries: Python evaluates the whole
        right side first and the intermediate tuple is never observable."""
        value = node.value
        if not (
            len(targets) == 1
            and isinstance(targets[0], (ast.Tuple, ast.List))
            and isinstance(value, (ast.Tuple, ast.List))
            and len(targets[0].elts) == len(value.elts)
            and all(isinstance(t, ast.Name) for t in targets[0].elts)
            and not any(isinstance(v, ast.Starred) for v in value.elts)
        ):
            return None
        temps = [self.temp() for _ in value.elts]
        return [
            *(
                ast.Assign([ast.Name(t, ast.Store())], self.expr(v))
                for t, v in zip(temps, value.elts)
            ),
            *(
                a
                for t, target in zip(temps, targets[0].elts)
                for a in self.assign(node, target, ast.Name(t, ast.Load()))
            ),
        ]

    def writes(self, statements):
        names = set()

        def visit(node):
            if isinstance(
                node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)
            ):
                return
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                names.add(node.id)
            for child in ast.iter_child_nodes(node):
                visit(child)

        for stmt in statements:
            visit(stmt)
        return ast.Tuple([ast.Constant(n) for n in sorted(names)], ast.Load())

    def scoped_nodes(self, statements):
        for node in statements:
            yield node
            if not isinstance(
                node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)
            ):
                yield from self.scoped_nodes(ast.iter_child_nodes(node))

    def defaults(self, args, site):
        positional = args.posonlyargs + args.args
        args.defaults = [
            self.rt("default_value", site, ast.Constant(arg.arg), self.expr(value))
            for arg, value in zip(
                positional[len(positional) - len(args.defaults) :], args.defaults
            )
        ]
        args.kw_defaults = [
            (
                self.rt("default_value", site, ast.Constant(arg.arg), self.expr(value))
                if value is not None
                else None
            )
            for arg, value in zip(args.kwonlyargs, args.kw_defaults)
        ]

    def heap_writes(self, statements):
        """Resolve only shadow-memory paths; never evaluate an untaken target."""

        def path(node):
            if isinstance(node, ast.Name):
                return ("name", node.id)
            if isinstance(node, ast.Attribute):
                parent = path(node.value)
                return ("attr", parent, node.attr) if parent else None
            return None

        specs = []
        for node in self.scoped_nodes(statements):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr
                in {
                    "append",
                    "extend",
                    "pop",
                    "clear",
                    "insert",
                    "remove",
                    "reverse",
                    "sort",
                    "update",
                    "setdefault",
                    "__setitem__",
                    # NumPy in-place array methods.
                    "fill",
                    "partition",
                    "put",
                    "resize",
                    "itemset",
                }
            ):
                base = path(node.func.value)
                if base:
                    specs.append(("structure", base, None))
            if isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Store):
                base = path(node.value)
                if base:
                    specs.append(("attr", base, node.attr))
            if isinstance(node, ast.Subscript) and isinstance(node.ctx, ast.Store):
                base = path(node.value)
                key = (
                    ("constant", node.slice.value)
                    if isinstance(node.slice, ast.Constant)
                    else (
                        ("name", node.slice.id)
                        if isinstance(node.slice, ast.Name)
                        else None
                    )
                )
                if base and key:
                    specs.append(("item", base, key))
                elif base:
                    # Computed keys (slices, tuples, arrays): join the whole value.
                    specs.append(("whole", base, None))
        return ast.parse(repr(specs), mode="eval").body

    def block(self, statements):
        out = []
        for node in statements:
            for new in self.stmt(node):
                out.append(ast.copy_location(new, node))
        return out

    def stmt(self, node):
        site = self.site(node)
        if isinstance(node, ast.Expr):
            if isinstance(node.value, ast.Constant) and isinstance(
                node.value.value, str
            ):
                return [node]  # Preserve docstrings.
            return [ast.Expr(self.expr(node.value))]
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            if node.value is None:
                return [node]
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            parallel = self.parallel(node, targets)
            if parallel is not None:
                return parallel
            temp = self.temp()
            try:
                assigns = [
                    a
                    for t in targets
                    for a in self.assign(node, t, ast.Name(temp, ast.Load()))
                ]
            except ValueError:
                return self.unsupported_stmt(node)
            return [
                ast.Assign([ast.Name(temp, ast.Store())], self.expr(node.value)),
                *assigns,
            ]
        if isinstance(node, ast.AugAssign):
            # Attribute/subscript receivers must not be evaluated a second time.
            prefix = []
            if isinstance(node.target, ast.Name):
                old = self.expr(
                    ast.copy_location(ast.Name(node.target.id, ast.Load()), node.target)
                )
                result = self.rt(
                    "binary",
                    site,
                    ast.Constant(type(node.op).__name__),
                    old,
                    self.expr(node.value),
                    inplace=ast.Constant(True),
                )
                return self.assign(node, node.target, result)
            if isinstance(node.target, (ast.Attribute, ast.Subscript)):
                base = self.temp()
                prefix.append(
                    ast.Assign(
                        [ast.Name(base, ast.Store())], self.expr(node.target.value)
                    )
                )
                b = ast.Name(base, ast.Load())
                if isinstance(node.target, ast.Attribute):
                    key = ast.Constant(node.target.attr)
                    get, put = "get_attr", "set_attr"
                else:
                    tempkey = self.temp()
                    prefix.append(
                        ast.Assign(
                            [ast.Name(tempkey, ast.Store())],
                            self.key(node.target.slice),
                        )
                    )
                    key = ast.Name(tempkey, ast.Load())
                    get, put = "subscript", "set_item"
                result = self.rt(
                    "binary",
                    site,
                    ast.Constant(type(node.op).__name__),
                    self.rt(get, site, b, key),
                    self.expr(node.value),
                    inplace=ast.Constant(True),
                )
                return [*prefix, ast.Expr(self.rt(put, site, b, key, result))]
            return self.unsupported_stmt(node)
        if isinstance(node, ast.Return):
            return [ast.Return(self.rt("return_value", site, self.expr(node.value)))]
        if isinstance(node, ast.If):
            condition = self.temp()
            exits = max((_exit_kind(s) for s in node.body + node.orelse), default=0)
            context = self.rt(
                "branch",
                site,
                self.expr(node.test),
                self.writes(node.body + node.orelse),
                ast.Constant(exits),
                self.heap_writes(node.body + node.orelse),
            )
            return [
                ast.With(
                    [ast.withitem(context, ast.Name(condition, ast.Store()))],
                    [
                        ast.If(
                            ast.Name(condition, ast.Load()),
                            self.block(node.body),
                            self.block(node.orelse),
                        )
                    ],
                )
            ]
        if isinstance(node, ast.For):
            temp = self.temp()
            iterator = self.temp()
            try:
                binding = self.assign(node, node.target, ast.Name(temp, ast.Load()))
            except ValueError:
                return self.unsupported_stmt(node)
            body = [*binding, *self.block(node.body)]
            loop = ast.For(
                ast.Name(temp, ast.Store()),
                ast.Name(iterator, ast.Load()),
                body,
                self.block(node.orelse),
            )
            context = self.rt(
                "for_loop",
                site,
                self.expr(node.iter),
                self.writes(node.body),
                self.heap_writes(node.body),
            )
            return [
                ast.With(
                    [ast.withitem(context, ast.Name(iterator, ast.Store()))], [loop]
                )
            ]
        if isinstance(node, ast.While):
            iterator, item = self.temp(), self.temp()
            loop = ast.For(
                ast.Name(item, ast.Store()),
                ast.Name(iterator, ast.Load()),
                self.block(node.body),
                self.block(node.orelse),
            )
            context = self.rt(
                "while_loop",
                site,
                self.thunk(self.expr(node.test)),
                self.writes(node.body),
                self.heap_writes(node.body),
            )
            return [
                ast.With(
                    [ast.withitem(context, ast.Name(iterator, ast.Store()))], [loop]
                )
            ]
        if isinstance(node, ast.FunctionDef):
            old = self.scope
            self.scope = node.name if old == "<module>" else old + "." + node.name
            # staticmethod/classmethod only change binding; the original decorator
            # expression stays outermost. Other decorators keep the body opaque.
            binding = len(node.decorator_list) == 1 and (
                isinstance(node.decorator_list[0], ast.Name)
                and node.decorator_list[0].id in ("staticmethod", "classmethod")
            )
            unsupported = (
                (node.decorator_list and not binding)
                or node.args.vararg
                or node.args.kwarg
                or any(
                    isinstance(n, (ast.Yield, ast.YieldFrom, ast.Await))
                    for n in self.scoped_nodes(node.body)
                )
            )
            if unsupported:
                # Keep original function semantics; invocation is recorded as opaque.
                self.scope = old
                return [node]
            locals_ = self.writes(node.body)
            globals_ = ast.Tuple(
                [
                    ast.Constant(name)
                    for n in self.scoped_nodes(node.body)
                    if isinstance(n, ast.Global)
                    for name in n.names
                ],
                ast.Load(),
            )
            nonlocals_ = ast.Tuple(
                [
                    ast.Constant(name)
                    for n in ast.walk(node)
                    if isinstance(n, ast.Nonlocal)
                    for name in n.names
                ],
                ast.Load(),
            )
            self.defaults(node.args, site)
            node.body = self.block(node.body)
            node.decorator_list = [
                *node.decorator_list,
                self.rt("function", site, locals_, globals_, nonlocals_),
            ]
            self.scope = old
            return [node]
        if isinstance(node, ast.ClassDef):
            old = self.scope
            self.scope = node.name if old == "<module>" else old + "." + node.name
            body = []
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    body.extend(self.stmt(item))
                else:
                    # Class namespace execution has no shadow frame yet. Literal
                    # declarations are safe; other statements must remain unknown.
                    try:
                        if isinstance(item, (ast.Assign, ast.AnnAssign, ast.Expr)):
                            if item.value is not None:
                                ast.literal_eval(item.value)
                        elif not isinstance(
                            item, (ast.Pass, ast.Import, ast.ImportFrom)
                        ):
                            raise ValueError
                    except (ValueError, TypeError):
                        body.extend(self.unsupported_stmt(item))
                    else:
                        body.append(item)
            node.body = body
            self.scope = old
            return [node]
        if isinstance(node, ast.Raise):
            # Exceptions keep their native type and traceback; opaque handlers below
            # explicitly invalidate affected scores.
            return [node]
        if isinstance(
            node,
            (
                ast.Pass,
                ast.Break,
                ast.Continue,
                ast.Global,
                ast.Nonlocal,
                ast.Import,
                ast.ImportFrom,
            ),
        ):
            return [node]
        if isinstance(node, ast.Assert):
            return [ast.Assert(self.rt("truth", site, self.expr(node.test)), node.msg)]
        return self.unsupported_stmt(node)

    def unsupported_stmt(self, node):
        site = self.site(node)
        marker = ast.Expr(
            self.rt(
                "unsupported",
                site,
                ast.Constant(f"Unsupported statement: {type(node).__name__}"),
            )
        )
        specs = self.heap_writes([node])
        if specs.elts:
            # The body runs natively. On any exit, objects it may have written
            # through a name/attribute path get unknown contents for later reads.
            node = ast.Try(
                body=[node],
                handlers=[],
                orelse=[],
                finalbody=[ast.Expr(self.rt("unknown_writes", site, specs))],
            )
        return [marker, node]

    def compile(self):
        tree = ast.parse(self.source, self.file)
        tree.body = self.block(tree.body)
        return compile(ast.fix_missing_locations(tree), self.file, "exec")


def compile_source(recorder, path, source):
    recorder.source_hashes[str(path)] = hashlib.sha256(source.encode()).hexdigest()
    instrumenter = Instrumenter(recorder, str(path), source)
    return instrumenter.compile(), instrumenter.name
