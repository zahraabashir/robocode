"""Shadow provenance for real Python values used by instrumented source.

Values in policy variables are ordinary Python objects. ``Value`` objects are
transient instrumentation operands; native/library calls never receive them.
"""

# Methods implement the AST instrumentation protocol rather than a public API.
# Exact builtin types are intentional: subclasses can override their semantics.
# pylint: disable=missing-function-docstring,unidiomatic-typecheck

from __future__ import annotations

import functools
import inspect
import operator
import sys
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any

from policy_graph.reactivity import PLANNERS

from .config import RuntimeConfig
from .graph import ExecutionGraph, Site
from .semantics import candidate_horizon, candidate_key


@dataclass(slots=True)
class Value:
    """A temporary shadow operand; never exposed to the traced policy."""

    value: Any
    ref: int
    depth: int | None = None
    candidate: bool = False
    context: tuple[int, ...] = ()
    receiver: Value | None = None
    attribute: str | None = None


def replace(v, **c):
    """``dataclasses.replace`` for Value, without its per-call field reflection."""
    return Value(
        c["value"] if "value" in c else v.value,
        c["ref"] if "ref" in c else v.ref,
        c["depth"] if "depth" in c else v.depth,
        c["candidate"] if "candidate" in c else v.candidate,
        c["context"] if "context" in c else v.context,
        c["receiver"] if "receiver" in c else v.receiver,
        c["attribute"] if "attribute" in c else v.attribute,
    )


@dataclass
class Heap:
    """Versioned provenance for one retained object identity."""

    value: Any  # Retain identity for this bounded trace; id reuse must not alias.
    whole: int
    structure: int
    items: dict = field(default_factory=dict)
    attrs: dict = field(default_factory=dict)


@dataclass
class Frame:
    """Lexical bindings and active dependencies of a Python invocation."""

    parent: Frame | None
    invocation: int
    bindings: dict = field(default_factory=dict)
    local_names: set = field(default_factory=set)
    global_names: set = field(default_factory=set)
    nonlocal_names: set = field(default_factory=set)
    controls: list = field(default_factory=list)
    uncertainty: list = field(default_factory=list)
    exit_controls: list = field(default_factory=list)
    returned: Value | None = None

    def owner(self, name):
        if name in self.global_names:
            f = self
            while f.parent is not None:
                f = f.parent
            return f
        if name in self.nonlocal_names and self.parent is not None:
            return self.parent.lookup_frame(name)
        return self

    def lookup_frame(self, name):
        if name in self.bindings or name in self.local_names or self.parent is None:
            return self.owner(name)
        return self.parent.lookup_frame(name)


BINOPS = {
    name: getattr(operator, op)
    for name, op in {
        "Add": "add",
        "Sub": "sub",
        "Mult": "mul",
        "Div": "truediv",
        "FloorDiv": "floordiv",
        "Mod": "mod",
        "Pow": "pow",
        "MatMult": "matmul",
        "LShift": "lshift",
        "RShift": "rshift",
        "BitOr": "or_",
        "BitAnd": "and_",
        "BitXor": "xor",
    }.items()
}
CMPOPS = {
    "Lt": operator.lt,
    "LtE": operator.le,
    "Gt": operator.gt,
    "GtE": operator.ge,
    "Eq": operator.eq,
    "NotEq": operator.ne,
    "Is": operator.is_,
    "IsNot": operator.is_not,
    "In": lambda a, b: a in b,
    "NotIn": lambda a, b: a not in b,
}
UNARY = {
    "USub": operator.neg,
    "UAdd": operator.pos,
    "Not": operator.not_,
    "Invert": operator.invert,
}
SCALARS = (int, float, complex, bool, str, bytes, type(None))
# Python's in-place operators, e.g. ``|=`` is operator.ior (not "ior_").
INPLACE = {
    name: getattr(operator, "i" + fn.__name__.rstrip("_"), fn)
    for name, fn in BINOPS.items()
}
# Longer control lists are summarized by one event with the same dependencies.
CONTROL_LIMIT = 8

# NumPy is optional; its values only exist if the traced program imported it.
NUMPY_EXCLUDED = ("numpy.random", "numpy.testing", "numpy.ctypeslib", "numpy.f2py")
NUMPY_IO = {
    "save",
    "savez",
    "savez_compressed",
    "savetxt",
    "load",
    "loadtxt",
    "genfromtxt",
    "fromfile",
    "fromregex",
    "memmap",
    "tofile",
    "dump",
    "dumps",
}
NUMPY_INPLACE_FUNCTIONS = {
    "copyto",
    "put",
    "place",
    "putmask",
    "fill_diagonal",
    "put_along_axis",
}
NUMPY_INPLACE_METHODS = {
    "fill",
    "sort",
    "partition",
    "resize",
    "put",
    "itemset",
    "setfield",
    "setflags",
    "__setitem__",
}
# Representation changes that keep a value's prediction depth (like int/float).
NUMPY_CONVERSIONS = {
    "array",
    "asarray",
    "asanyarray",
    "ascontiguousarray",
    "copy",
    "astype",
    "reshape",
    "ravel",
    "flatten",
    "squeeze",
    "atleast_1d",
    "item",
    "float64",
    "float32",
    "int64",
    "int32",
}


def _numpy():
    return sys.modules.get("numpy")


def _numpy_value(value, np):
    """An exact NumPy array or scalar type, whose operators run no user code."""
    kind = type(value)
    if kind is np.ndarray:
        return not value.dtype.hasobject
    return (
        isinstance(value, np.generic)
        and kind.__module__ == "numpy"
        and not isinstance(value, np.object_)
    )


def _plain_key(key, depth=0):
    """Hashable without invoking user __hash__/__eq__ (unlike slices pre-3.12)."""
    if type(key) in (str, int, float, bool):
        return True
    return (
        type(key) is tuple and depth < 4 and all(_plain_key(k, depth + 1) for k in key)
    )


class Recorder:
    """Execute instrumented operations on real values and record their evidence."""

    def __init__(self, config=None):
        self.config = config or RuntimeConfig()
        self.graph = ExecutionGraph(self.config.max_events)
        self.sites: list[Site] = []
        self.phase = "load"
        self.frame = Frame(None, 0)
        self.next_invocation = 1
        self.heap: dict[int, Heap] = {}
        self.iterators: dict[int, tuple] = {}
        self.defaults: dict[tuple[int, str], Value] = {}
        self.requests: list[dict] = []
        self.suppressed_transitions = 0
        self.actions: list[int] = []
        self.calls: list[dict] = []
        self.source_hashes: dict[str, str] = {}
        self.structural_sites: dict[tuple[str, int], str] = {}
        self.recognition = None
        self.generators = {}
        # One dependency-free event per constant site; uses add their own controls.
        self.literals: dict[int, int] = {}
        self.contract_cache: dict[str, tuple] = {}
        # Latest content version of each mutated/observed NumPy memory buffer,
        # keyed by the root of the ``.base`` chain so views and aliases share it.
        self.buffers: dict[int, tuple[Any, int]] = {}
        self.versions: dict[tuple, int] = {}
        # Tests can audit that innermost controls preserve the full closure.
        self.full_controls: dict[int, tuple[int, ...]] | None = None
        self.harness_site = self.site(Site("<harness>", 0, 0, "<harness>"))

    def site(self, site):
        self.sites.append(site)
        return len(self.sites) - 1

    def controls(self):
        """The innermost entry of each control list.

        Every entry is recorded while all entries below it are active, so the
        innermost one's transitive controls include the rest: referencing it
        alone yields exactly the same backward slices.
        """
        f = self.frame
        return (*f.controls[-1:], *f.exit_controls[-1:], *f.uncertainty[-1:])

    def event(self, kind, site, parents=(), *, controls=(), depth=None, **detail):
        if self.suppressed_transitions:
            detail["contract_internal"] = True
        ref = self.graph.add(
            kind,
            self.sites[site],
            self.phase,
            self.frame.invocation,
            parents,
            (*self.controls(), *controls),
            depth,
            **detail,
        )
        if self.full_controls is not None:
            f = self.frame
            self.full_controls[ref] = (
                *f.controls,
                *f.exit_controls,
                *f.uncertainty,
                *controls,
            )
        return ref

    def _covered(self, value):
        """A copy of ``value`` here would add no dependency: skip recording it."""
        event = self.graph.events[value.ref]
        return all(c in event.control for c in self.controls())

    def make(
        self,
        kind,
        site,
        value,
        operands=(),
        *,
        depth=None,
        candidate=False,
        context=(),
        **detail,
    ):
        ref = self.event(kind, site, [v.ref for v in operands], depth=depth, **detail)
        return Value(
            value,
            ref,
            depth,
            candidate,
            tuple(dict.fromkeys((*context, *self.frame.controls[-1:]))),
        )

    def literal(self, site, value):
        # A constant has no dependencies; whatever consumes it records the
        # controls under which it was evaluated, so one event per site suffices.
        ref = self.literals.get(site)
        if ref is None:
            ref = self.graph.add("literal", self.sites[site], self.phase, 0)
            self.literals[site] = ref
        return Value(value, ref, context=tuple(self.frame.controls[-1:]))

    def _summarize(self, site, controls):
        """Replace a control list by one event with identical transitive controls."""
        ref = self.graph.add(
            "control-summary",
            self.sites[site],
            self.phase,
            self.frame.invocation,
            (),
            controls,
        )
        controls[:] = [ref]

    def external(self, value, *, state=False, name="input"):
        result = self.make(
            "observation" if state else "input",
            self.harness_site,
            value,
            depth=0 if state else None,
            name=name,
        )
        if state and type(value) not in SCALARS:
            # A fresh real observation starts a new prediction origin even when
            # the environment reuses the same mutable observation object.
            np = _numpy()
            if np is not None and type(value) is np.ndarray:
                self._set_buffer(value, result.ref)
            else:
                self.heap[id(value)] = Heap(value, result.ref, result.ref)
        return result

    @staticmethod
    def _root(array):
        """The object owning an array's memory; views/aliases share this root."""
        root = array
        while getattr(root, "base", None) is not None:
            root = root.base
        return getattr(root, "obj", root) if type(root) is memoryview else root

    def _set_buffer(self, array, ref):
        root = self._root(array)
        self.buffers[id(root)] = (root, ref)  # Retaining root prevents id reuse.

    def _array_update(
        self, site, target, operands=(), parents=(), kind="array-write", **detail
    ):
        """Record a write through any view; later reads of every alias depend on it."""
        ref = self.event(
            kind,
            site,
            (
                self._whole(target).ref,
                *(self._whole(v).ref for v in operands),
                *parents,
            ),
            **detail,
        )
        self._set_buffer(target.value, ref)
        return ref

    def _copy(self, kind, site, value, *extra, **detail):
        ref = self.event(
            kind,
            site,
            (value.ref, *(v.ref for v in extra)),
            depth=value.depth,
            **detail,
        )
        return replace(
            value,
            ref=ref,
            context=tuple(dict.fromkeys((*value.context, *self.frame.controls[-1:]))),
        )

    def _version(self, parents):
        """A content summary; identical parent sets reuse the earlier event.

        It has no controls of its own: its consumer records those.
        """
        parents = tuple(parents)
        ref = self.versions.get(parents)
        if ref is None:
            ref = self.graph.add(
                "object-version", self.sites[self.harness_site], self.phase, 0, parents
            )
            self.versions[parents] = ref
        return ref

    def _whole(self, value, seen=None):
        np = _numpy()
        if np is not None and type(value.value) is np.ndarray:
            root = self._root(value.value)
            buffer = self.buffers.get(id(root))
            if buffer is None or buffer[0] is not root or buffer[1] == value.ref:
                return value
            return replace(
                value,
                ref=self._version((value.ref, buffer[1], *value.context)),
            )
        seen = set() if seen is None else seen
        if id(value.value) in seen:
            return value
        seen.add(id(value.value))
        heap = self.heap.get(id(value.value))
        if heap is None:
            return value
        if type(value.value) in (list, tuple, dict):
            keys = (
                list(value.value)
                if type(value.value) is dict
                else range(len(value.value))
            )
            parents = [heap.structure, *value.context]
            for key in keys:
                parents.append(
                    self._whole(heap.items[key], seen).ref
                    if key in heap.items
                    else heap.whole
                )
        else:
            parents = (value.ref, heap.whole, *value.context)
        return replace(value, ref=self._version(parents))

    def read(self, site, name, actual):
        owner = self.frame.lookup_frame(name)
        old = owner.bindings.get(name)
        if old is None or old.value is not actual:
            old = self.make("external-name", site, actual, name=name)
            owner.bindings[name] = old
        # No event: the consumer of this value records the current controls.
        return replace(
            old,
            context=tuple(dict.fromkeys((*old.context, *self.frame.controls[-1:]))),
        )

    def bind(self, site, name, value):
        result = (
            replace(
                value,
                context=tuple(
                    dict.fromkeys((*value.context, *self.frame.controls[-1:]))
                ),
            )
            if self._covered(value)
            else self._copy("write", site, value)
        )
        self.frame.owner(name).bindings[name] = result
        return value.value

    def _heap(self, value, site):
        heap = self.heap.get(id(value.value))
        if heap is None:
            structure = self.event("object-identity", site, value.context)
            heap = Heap(value.value, value.ref, structure)
            self.heap[id(value.value)] = heap
        return heap

    def container(self, site, kind, items):
        if kind == "dict":
            actual = {k.value: v.value for k, v in items}
            operands = [v for pair in items for v in pair]
            refs = {k.value: v for k, v in items}
        else:
            actual = {"list": list, "tuple": tuple, "set": set}[kind](
                v.value for v in items
            )
            operands = items
            refs = dict(enumerate(items)) if kind != "set" else {}
        result = self.make("container", site, actual, operands)
        heap = self._heap(result, site)
        heap.items = refs
        if kind == "dict":
            heap.structure = self.event(
                "dictionary-keys", site, [k.ref for k, _ in items]
            )
        return result

    def index(self, site, items):
        # Array indices contribute their current contents (in-place updates).
        return self.make(
            "index",
            site,
            tuple(v.value for v in items),
            [self._whole(v) for v in items],
        )

    def get_attr(self, site, base, name):
        actual = getattr(base.value, name)  # Evaluate a descriptor once.
        heap = self.heap.get(id(base.value))
        saved = heap.attrs.get(name) if heap else None
        if saved is not None and saved.value is actual:
            result = self._copy("attribute-read", site, saved)
        elif inspect.ismethod(actual) or (
            inspect.isbuiltin(actual)
            and getattr(actual, "__self__", None) is base.value
        ):
            ref = self.event("method-read", site, base.context)
            result = Value(actual, ref, context=base.context)
        else:
            result = self.make(
                "attribute-read",
                site,
                actual,
                [self._whole(base)],
                depth=base.depth,
                candidate=base.candidate,
                context=base.context,
            )
            # Properties execute outside an instrumented call boundary.
            descriptor = inspect.getattr_static(type(base.value), name, None)
            if isinstance(descriptor, property):
                result = self.opaque(
                    site, actual, [base], "Property dependency is not supported"
                )
        return replace(result, receiver=base, attribute=name)

    def set_attr(self, site, base, name, value):
        setattr(base.value, name, value.value)
        heap = self._heap(base, site)
        saved = self._copy("attribute-write", site, value, base)
        heap.attrs[name] = saved
        heap.whole = self.event("object-mutation", site, (heap.whole, saved.ref))

    def subscript(self, site, base, key):
        actual = base.value[key.value]
        heap = self.heap.get(id(base.value))
        k = key.value
        if type(base.value) in (list, tuple) and isinstance(k, int) and k < 0:
            k += len(base.value)
        if heap is not None and _plain_key(k) and k in heap.items:
            saved = heap.items[k]
            ref = self.event(
                "item-read",
                site,
                (saved.ref, key.ref, heap.structure, *base.context),
                depth=saved.depth,
            )
            return Value(
                actual,
                ref,
                saved.depth,
                saved.candidate,
                tuple(
                    dict.fromkeys(
                        (*saved.context, *base.context, *self.frame.controls[-1:])
                    )
                ),
            )
        if (
            heap is not None
            and isinstance(k, slice)
            and type(base.value) in (list, tuple)
        ):
            indices = list(range(len(base.value)))[k]
            items = [self.subscript(site, base, self.literal(site, i)) for i in indices]
            return self.container(
                site, "list" if type(base.value) is list else "tuple", items
            )
        np = _numpy()
        if np is not None and type(base.value) is np.ndarray:
            return self._array_read(site, base, key, actual, np)
        return self.make(
            "item-read",
            site,
            actual,
            [self._whole(base), key],
            depth=base.depth,
            candidate=base.candidate,
            context=base.context,
        )

    def _array_read(self, site, base, key, actual, np):
        """Indexing records the whole array, flagged when it selects a part.

        NumPy arrays have no element provenance: a basic, advanced or boolean
        index result depends on all elements of the base, plus the exact index.
        """
        whole = self._whole(base)
        index = self._whole(key) if type(key.value) is np.ndarray else key
        partial = base.value.size > 1 and not (
            type(actual) is np.ndarray and actual.size == base.value.size
        )
        ref = self.event(
            "item-read",
            site,
            (whole.ref, index.ref),
            depth=base.depth,
            array="index",
            **({"imprecise_parents": (whole.ref,)} if partial else {}),
        )
        return Value(
            actual,
            ref,
            base.depth,
            base.candidate,
            tuple(dict.fromkeys((*base.context, *self.frame.controls[-1:]))),
        )

    def set_item(self, site, base, key, value):
        new_key = type(base.value) is dict and key.value not in base.value
        base.value[key.value] = value.value
        np = _numpy()
        if np is not None and type(base.value) is np.ndarray:
            # Writes through a view also update its root buffer and other aliases.
            index = self._whole(key) if type(key.value) is np.ndarray else key
            self._array_update(site, base, [index, value])
            return
        heap = self._heap(base, site)
        if new_key:
            heap.structure = self.event(
                "structure-write", site, (heap.structure, key.ref)
            )
        if type(base.value) in (list, dict) and not isinstance(key.value, slice):
            k = key.value
            if type(base.value) is list and k < 0:
                k += len(base.value)
            heap.items[k] = self._copy("item-write", site, value, key)
            heap.whole = self.event(
                "object-mutation", site, (heap.whole, heap.items[k].ref)
            )
        else:
            self._unknown_mutation(
                site, base, "Unsupported indexed mutation", [key, value]
            )

    def _additive_pattern(self, op, left, right):
        """The structural pattern of the scalar arithmetic-transition heuristic."""
        state, candidate = (left, right) if left.depth is not None else (right, left)
        return (
            self.config.arithmetic_transitions
            and not self.suppressed_transitions
            and op in ("Add", "Sub")
            and state.depth is not None
            and candidate.depth is None
            and candidate.candidate
            and (state is left or op == "Add")
        )

    def _numpy_binary(self, site, op, left, right, inplace, np):
        """Elementwise/broadcast/matrix arithmetic with whole-value dependencies.

        This adds no planning interpretation. Arrays carry no per-element
        candidate marks, so a state-derived value shifted by a candidate or by
        any multi-element array (possibly a batch of candidate actions) is
        recorded as unknown, never as transitions and never as "no planning".
        """
        fn = INPLACE[op] if inplace else BINOPS[op]
        result = fn(left.value, right.value)
        operands = [self._whole(left), self._whole(right)]
        state = left if left.depth is not None else right
        other = right if state is left else left
        numeric = all(
            type(v.value) in (int, float)
            or (_numpy_value(v.value, np) and v.value.dtype.kind in "iuf")
            for v in (left, right)
        )
        marked = replace(other, candidate=True)
        batch = (
            type(other.value) is np.ndarray
            and other.value.size > 1
            and self._additive_pattern(
                op, *((left, marked) if state is left else (marked, right))
            )
        )
        if numeric and (self._additive_pattern(op, left, right) or batch):
            out = self.make(
                "opaque",
                site,
                result,
                operands,
                reason=(
                    "NumPy arithmetic matches the additive-transition pattern "
                    "(a candidate or a possible batch of candidates); it is not "
                    "interpreted as model transitions"
                ),
            )
        else:
            shifted = (
                numeric
                and op in ("Add", "Sub")
                and state.depth is not None
                and (left if state is right else right).depth is None
                and (state is left or op == "Add")
            )
            out = self.make(
                "operation",
                site,
                result,
                operands,
                depth=state.depth if shifted else None,
                candidate=left.candidate or right.candidate,
                operation=op,
                array=True,
            )
        if inplace and type(left.value) is np.ndarray and result is left.value:
            self._set_buffer(left.value, out.ref)
        return out

    def binary(self, site, op, left, right, inplace=False):
        np = _numpy()
        if (
            np is not None
            and any(_numpy_value(v.value, np) for v in (left, right))
            and all(self._ordinary(v.value) for v in (left, right))
        ):
            return self._numpy_binary(site, op, left, right, inplace, np)
        sequence_items = None
        if (
            type(left.value) in (list, tuple)
            and op == "Add"
            and type(right.value) is type(left.value)
        ):
            sequence_items = [*self.elements(site, left), *self.elements(site, right)]
        fn = INPLACE[op] if inplace else BINOPS[op]
        result = fn(left.value, right.value)
        state, candidate = (left, right) if left.depth is not None else (right, left)
        arithmetic = (
            self.config.arithmetic_transitions
            and not self.suppressed_transitions
            and op in ("Add", "Sub")
            and state.depth is not None
            and candidate.depth is None
            and candidate.candidate
            and (state is left or op == "Add")
            and type(left.value) in (int, float)
            and type(right.value) in (int, float)
        )
        if arithmetic:
            return self.make(
                "transition",
                site,
                result,
                [left, right],
                depth=state.depth + 1,
                state_parent=state.ref,
                unit="model steps",
                basis="arithmetic assumption",
                candidate_key=candidate_key(candidate.value),
            )
        if (
            type(left.value) in (list, tuple)
            and op == "Add"
            and type(right.value) is type(left.value)
        ):
            out = self.make("operation", site, result, [left, right])
            h = self._heap(out, site)
            h.items = dict(enumerate(sequence_items))
            h.whole = out.ref
            return out
        shifted_depth = (
            state.depth
            if (
                op in ("Add", "Sub")
                and state.depth is not None
                and candidate.depth is None
                and (state is left or op == "Add")
                and type(left.value) in (int, float)
                and type(right.value) in (int, float)
            )
            else None
        )
        out = self.make(
            "operation",
            site,
            result,
            [left, right],
            depth=shifted_depth,
            candidate=left.candidate or right.candidate,
            operation=op,
        )
        if (
            inplace
            and type(left.value) not in SCALARS
            and type(left.value) is not tuple
        ):
            self._unknown_mutation(
                site, left, "Unsupported in-place operation", [right]
            )
        if type(left.value) not in SCALARS or type(right.value) not in SCALARS:
            out = self.opaque(
                site,
                result,
                [out],
                "Non-scalar arithmetic requires a dependency/transition adapter",
            )
        return out

    def unary(self, site, op, operand):
        if not self._ordinary(operand.value):
            return self._opaque_call(
                site,
                lambda: UNARY[op](operand.value),
                [operand],
                "Custom unary operator requires an adapter",
            )
        result = UNARY[op](operand.value)
        return self.make(
            "operation",
            site,
            result,
            [self._whole(operand)],
            candidate=operand.candidate,
            operation=op,
        )

    def compare(self, site, op, left, right):
        if op not in ("Is", "IsNot") and not all(
            self._ordinary(v.value) for v in (left, right)
        ):
            return self._opaque_call(
                site,
                lambda: CMPOPS[op](left.value, right.value),
                [left, right],
                "Custom comparison requires an adapter",
            )
        value = CMPOPS[op](left.value, right.value)
        return self.make(
            "comparison",
            site,
            value,
            [self._whole(left), self._whole(right)],
            comparison=op,
        )

    def compare_chain(self, site, left, operators, thunks):
        comparisons = []
        for index, (op, thunk) in enumerate(zip(operators, thunks)):
            right = thunk()
            result = self.compare(site, op, left, right)
            comparisons.append(result)
            if index < len(operators) - 1 and not result.value:
                break
            left = right
        if len(comparisons) == 1:
            return comparisons[0]
        return self._copy("comparison-chain", site, comparisons[-1], *comparisons[:-1])

    def truth(self, site, value):
        self.event("test", site, [value.ref])
        return bool(value.value)

    def slice_value(self, site, start, stop, step):
        return self.make(
            "slice",
            site,
            slice(start.value, stop.value, step.value),
            [start, stop, step],
        )

    def boolean(self, site, op, thunks):
        values = []
        for index, thunk in enumerate(thunks):
            value = thunk()
            values.append(value)
            if index < len(thunks) - 1 and (
                (op == "And" and not value.value) or (op == "Or" and value.value)
            ):
                break
        return self._copy("boolean", site, values[-1], *values[:-1])

    def conditional(self, site, condition, yes, no):
        with self.branch(site, condition, (), False) as taken:
            # Record the selection while the test still controls it; the value
            # is consumed after this context ends.
            return self._copy("conditional", site, yes() if taken else no())

    @contextmanager
    def branch(self, site, condition, writes, exits=False, heap_writes=()):
        test = self.event("condition", site, [condition.ref])
        taken = bool(condition.value)
        control_count = len(self.frame.controls)
        before = {
            name: self.frame.lookup_frame(name).bindings.get(name) for name in writes
        }
        self.frame.controls.append(test)
        try:
            yield taken
        finally:
            del self.frame.controls[control_count:]
            # A non-taken assignment can determine which old definition survives.
            # Names rebound in the taken arm were written under this test already.
            for name in writes:
                owner = self.frame.lookup_frame(name)
                current = owner.bindings.get(name)
                if current is not None and current is before[name]:
                    ref = self.event(
                        "branch-join", site, (current.ref, test), depth=current.depth
                    )
                    owner.bindings[name] = replace(
                        current, ref=ref, context=(*current.context, test)
                    )
            self._heap_join(site, heap_writes, test)
            if exits:
                self.frame.controls.append(test)
            if exits == 2:
                # A rejected return/raise still determines whether later code
                # executes, including after a surrounding loop has finished.
                exits_ = self.frame.exit_controls
                exits_.append(test)
                if len(exits_) > CONTROL_LIMIT or (
                    len(exits_) > 1 and exits_[-2] > test
                ):
                    # An enclosing test exits after an inner one was appended, so
                    # it does not cover it: keep the innermost entry complete.
                    self._summarize(site, exits_)

    def _resolve_path(self, path):
        if path[0] == "name":
            return self.frame.lookup_frame(path[1]).bindings.get(path[1])
        base = self._resolve_path(path[1])
        heap = self.heap.get(id(base.value)) if base else None
        return heap.attrs.get(path[2]) if heap else None

    def _heap_join(self, site, specs, test):
        np = _numpy()
        joined = set()
        for kind, path, key in specs:
            base = self._resolve_path(path)
            if base is not None and np is not None and type(base.value) is np.ndarray:
                # An untaken array write still decides which contents survive.
                if kind != "attr" and id(base.value) not in joined:
                    joined.add(id(base.value))
                    self._array_update(site, base, parents=(test,), kind="memory-join")
                continue
            if kind == "whole":
                continue  # Computed keys of Python containers: unchanged behavior.
            heap = self.heap.get(id(base.value)) if base else None
            if heap is None:
                continue
            if kind == "structure":
                heap.structure = self.event(
                    "structure-join", site, (heap.structure, test)
                )
                continue
            if kind == "item":
                if key[0] == "constant":
                    key = key[1]
                else:
                    value = self.frame.lookup_frame(key[1]).bindings.get(key[1])
                    if value is None:
                        continue
                    key = value.value
                if type(base.value) is list and isinstance(key, int) and key < 0:
                    key += len(base.value)
                table = heap.items
            else:
                table = heap.attrs
            try:
                current = table.get(key)
            except TypeError:
                continue
            if current is not None:
                ref = self.event(
                    "memory-join", site, (current.ref, test), depth=current.depth
                )
                table[key] = replace(current, ref=ref, context=(*current.context, test))
                heap.whole = self.event("object-mutation", site, (heap.whole, ref))

    def _join_names(self, site, writes, test):
        for name in writes:
            owner = self.frame.lookup_frame(name)
            value = owner.bindings.get(name)
            if value is not None:
                ref = self.event(
                    "loop-join", site, (value.ref, test), depth=value.depth
                )
                owner.bindings[name] = replace(
                    value, ref=ref, context=(*value.context, test)
                )

    def _structural_hint(self, site):
        source = self.sites[site]
        hint = self.structural_sites.get((source.file, source.line))
        if hint:
            return self.event("structural-candidate", site, rule=hint)

        return None

    @contextmanager
    def for_loop(self, site, iterable, writes, heap_writes=()):
        marker = self.event("loop", site, [iterable.ref])
        count = len(self.frame.controls)
        self.frame.controls.append(marker)

        def values():
            for value in self.iterate(site, iterable):
                carried = self.frame.controls[count + 1 :]
                if len(carried) > CONTROL_LIMIT:
                    # Exits/hints of earlier iterations still control this one.
                    self._summarize(site, carried)
                    self.frame.controls[count + 1 :] = carried
                hint = self._structural_hint(site)
                if hint is not None:
                    self.frame.controls.append(hint)
                yield value

        try:
            yield values()
        finally:
            del self.frame.controls[count:]
            self._join_names(site, writes, marker)
            self._heap_join(site, heap_writes, marker)

    @contextmanager
    def while_loop(self, site, test, writes, heap_writes=()):
        count = len(self.frame.controls)
        last = None

        def iterations():
            nonlocal last
            while True:
                del self.frame.controls[count:]
                value = test()
                last = self.event("loop-test", site, [value.ref])
                if not value.value:
                    break
                self.frame.controls.append(last)
                hint = self._structural_hint(site)
                if hint is not None:
                    self.frame.controls.append(hint)
                yield None

        iterator = iterations()
        try:
            yield iterator
        finally:
            iterator.close()
            del self.frame.controls[count:]
            if last is not None:
                self._join_names(site, writes, last)
                self._heap_join(site, heap_writes, last)

    def elements(self, site, iterable):
        if id(iterable.value) in self.generators:
            metadata = self.generators[id(iterable.value)]
            for _ in iterable.value:
                yield metadata[1]
            return
        if id(iterable.value) in self.iterators:
            _, source, start = self.iterators[id(iterable.value)]
            for actual in iterable.value:
                index, _ = actual
                value = self.subscript(site, source, self.literal(site, index - start))
                pair = self.container(site, "tuple", [self.literal(site, index), value])
                # The policy receives the actual tuple emitted by enumerate.
                heap = self.heap.pop(id(pair.value))
                pair.value = heap.value = actual
                self.heap[id(actual)] = heap
                yield pair
        elif type(iterable.value) in (list, tuple, range, str, bytes):
            for i, actual in enumerate(iterable.value):
                yield self.subscript(site, iterable, self.literal(site, i))
        elif (np := _numpy()) is not None and type(iterable.value) is np.ndarray:
            whole = self._whole(iterable)
            # Rows/elements carry whole-array provenance (flagged when partial).
            detail = (
                {"imprecise_parents": (whole.ref,)} if len(iterable.value) > 1 else {}
            )
            for actual in iterable.value:
                ref = self.event(
                    "item-read",
                    site,
                    (whole.ref,),
                    depth=iterable.depth,
                    array="iteration",
                    **detail,
                )
                yield Value(
                    actual, ref, iterable.depth, iterable.candidate, iterable.context
                )
        elif type(iterable.value) is dict:
            heap = self.heap.get(id(iterable.value))
            for key in iterable.value:
                ref = self.event(
                    "dictionary-key",
                    site,
                    (heap.structure if heap else iterable.ref, *iterable.context),
                )
                yield Value(key, ref, context=iterable.context)
        else:
            for value in iterable.value:
                yield self.opaque(
                    site,
                    value,
                    [iterable],
                    "Iterator element provenance is unsupported",
                )

    def iterate(self, site, iterable):
        for value in self.elements(site, iterable):
            value = self._copy("iteration", site, value)
            # Observed state elements are not independent candidate actions.
            value.candidate = value.candidate or (
                value.depth is None and iterable.depth is None
            )
            yield value

    def comp_iter(self, site, iterable, names):
        for value in self.iterate(site, iterable):
            self.bind_target(site, names, value)
            yield value.value

    def bind_target(self, site, target, value):
        if isinstance(target, str):
            return self.bind(site, target, value)
        iterator = iter(self.elements(site, value))
        parts = []
        for _ in target:
            try:
                parts.append(next(iterator))
            except StopIteration as exc:
                raise ValueError("Not enough values to unpack") from exc
        sentinel = object()
        if next(iterator, sentinel) is not sentinel:
            raise ValueError("Too many values to unpack")
        return tuple(
            self.bind_target(site, name, part) for name, part in zip(target, parts)
        )

    def comprehension(self, site, kind, thunk):
        old = self.frame
        self.frame = Frame(old, old.invocation, controls=list(old.controls))
        try:
            if kind == "generator":
                source = thunk()  # Python evaluates the outer iterable now.
                frame = self.frame
                metadata = [None, None]

                def generate():
                    while True:
                        caller = self.frame
                        self.frame = frame
                        try:
                            try:
                                value = next(source)
                            except StopIteration:
                                return
                            metadata[1] = value
                        finally:
                            self.frame = caller
                        yield value.value

                actual = generate()
                metadata[0] = actual  # Keep identity alive for this session.
                self.generators[id(actual)] = metadata
                return self.make("generator", site, actual)
            return self.container(site, kind, thunk())
        finally:
            self.frame = old

    def return_value(self, site, value):
        self.frame.returned = self._copy("return", site, self._whole(value))
        return value.value

    def function(self, site, local_names=(), global_names=(), nonlocal_names=()):
        parent = self.frame

        def decorate(fn):
            signature = inspect.signature(fn)
            defaults = {
                name: self.defaults.pop((site, name))
                for name in signature.parameters
                if (site, name) in self.defaults
            }

            @functools.wraps(fn)
            def wrapped(*args, **kwargs):
                old = self.frame
                request = (
                    self.requests[-1]
                    if self.requests and self.requests[-1]["target"] is wrapped
                    else None
                )
                bound = signature.bind(*args, **kwargs)
                bound.apply_defaults()
                if request:
                    metadata = signature.bind(*request["args"], **request["kwargs"])
                    known = metadata.arguments
                else:
                    known = {}
                frame = Frame(
                    parent,
                    self.next_invocation,
                    local_names=set(local_names),
                    global_names=set(global_names),
                    nonlocal_names=set(nonlocal_names),
                    controls=list(old.controls),
                    uncertainty=list(old.uncertainty),
                )
                self.next_invocation += 1
                self.frame = frame
                try:
                    for name, actual in bound.arguments.items():
                        value = known.get(name, defaults.get(name))
                        if not isinstance(value, Value):
                            value = self.make("parameter-default", site, actual)
                        frame.bindings[name] = (
                            value
                            if self._covered(value)
                            else self._copy("parameter", site, value)
                        )
                    actual = fn(*args, **kwargs)
                    # Without an instrumented return (implicit None, or a return
                    # inside an unsupported statement), the value depends on this
                    # frame's controls and uncertainty: never a shared constant.
                    result = frame.returned or self.make(
                        "implicit-return", site, actual
                    )
                    if request is not None:
                        request["result"] = result
                    return actual
                finally:
                    self.frame = old

            wrapped.__policy_graph_instrumented__ = True
            return wrapped

        return decorate

    def default_value(self, site, name, value):
        self.defaults[(site, name)] = value
        return value.value

    def opaque(self, site, value, operands, reason):
        return self.make(
            "opaque", site, value, [self._whole(v) for v in operands], reason=reason
        )

    def _ordinary(self, actual, seen=None):
        if type(actual) in SCALARS or type(actual) is range:
            return True
        if type(actual) not in (list, tuple, dict, set, frozenset):
            np = _numpy()
            return np is not None and _numpy_value(actual, np)
        seen = set() if seen is None else seen
        if id(actual) in seen:
            return True
        seen.add(id(actual))
        items = list(actual) + list(actual.values()) if type(actual) is dict else actual
        return all(self._ordinary(v, seen) for v in items)

    def _opaque_call(self, site, invoke, operands, reason):
        marker = self.event(
            "opaque", site, [self._whole(v).ref for v in operands], reason=reason
        )
        count = len(self.frame.uncertainty)
        self.frame.uncertainty.append(marker)
        try:
            actual = invoke()
        finally:
            del self.frame.uncertainty[count:]
        out = self.opaque(site, actual, operands, reason)
        np = _numpy()
        for value in operands:
            if (
                type(value.value) not in SCALARS
                and not inspect.isroutine(value.value)
                and not (np is not None and isinstance(value.value, np.generic))
            ):
                self._unknown_mutation(
                    site, value, f"Possible mutation: {reason}", [out]
                )
        return out

    def unsupported(self, site, reason):
        ref = self.event("opaque", site, reason=reason)
        self.frame.uncertainty.append(ref)
        if len(self.frame.uncertainty) > CONTROL_LIMIT:
            self._summarize(site, self.frame.uncertainty)

    def unknown_writes(self, site, specs):
        """After an unsupported statement: its possible writes are unknown."""
        seen = set()
        for _, path, _ in specs:
            base = self._resolve_path(path)
            if base is not None and id(base.value) not in seen:
                seen.add(id(base.value))
                if type(base.value) not in SCALARS:
                    self._unknown_mutation(
                        site, base, "Possible mutation in unsupported statement"
                    )

    def _unknown_mutation(self, site, base, reason, operands=()):
        np = _numpy()
        if np is not None and type(base.value) is np.ndarray:
            self._array_update(site, base, operands, kind="opaque", reason=reason)
            return
        heap = self._heap(base, site)
        ref = self.event(
            "opaque", site, (heap.whole, *(v.ref for v in operands)), reason=reason
        )
        heap.whole = heap.structure = ref
        heap.items.clear()
        heap.attrs.clear()

    def _name(self, fn):
        module = getattr(fn, "__module__", "") or ""
        name = getattr(fn, "__qualname__", getattr(fn, "__name__", ""))
        return f"{module}.{name}".strip(".")

    def _matches(self, name, pattern):
        return (
            name.startswith(pattern)
            if pattern.endswith(".")
            else name == pattern or name.endswith("." + pattern)
        )

    def _invoke(self, site, function, args, kwargs):
        fn = function.value
        target = getattr(fn, "__func__", fn)
        if getattr(target, "__policy_graph_instrumented__", False):
            metadata = list(args)
            if inspect.ismethod(fn):
                receiver = function.receiver
                if receiver is None or receiver.value is not fn.__self__:
                    # e.g. a classmethod bound to the class, read from an instance.
                    receiver = self.external(fn.__self__, name="receiver")
                metadata.insert(0, receiver)
            request = {"target": target, "args": metadata, "kwargs": kwargs}
            self.requests.append(request)
            try:
                actual = fn(
                    *(v.value for v in args), **{k: v.value for k, v in kwargs.items()}
                )
            finally:
                self.requests.pop()
            result = request.get("result")
            if result is None:
                return self.opaque(
                    site,
                    actual,
                    args,
                    "Instrumented function returned without provenance",
                )
        else:
            result = self._native(site, function, args, kwargs)
        result = replace(result, context=(*result.context, function.ref))
        return self._copy(
            "call-return",
            site,
            result,
            function,
            instrumented_callee=bool(
                getattr(target, "__policy_graph_instrumented__", False)
            ),
        )

    def _contracts(self, name):
        """Assessment, transition contract and planner status of a callee name."""
        if name not in self.contract_cache:
            self.contract_cache[name] = (
                next(
                    (
                        v
                        for k, v in self.config.assessments.items()
                        if self._matches(name, k)
                    ),
                    None,
                ),
                next(
                    (
                        v
                        for k, v in self.config.transition_models.items()
                        if self._matches(name, k)
                    ),
                    None,
                ),
                any(self._matches(name, p) for p in (*PLANNERS, *self.config.planners)),
            )
        return self.contract_cache[name]

    def call(self, site, function, args, kwargs):
        name = self._name(function.value)
        assessment, contract, planner = self._contracts(name)
        if assessment is not None and not self.suppressed_transitions:
            return self._assess(site, function, args, kwargs, assessment, name)
        if contract is not None and not self.suppressed_transitions:
            self.suppressed_transitions += 1
            try:
                result = self._invoke(site, function, args, kwargs)
            finally:
                self.suppressed_transitions -= 1

            def argument(key):
                if isinstance(key, int):
                    if key < len(args):
                        return args[key]
                    parameters = list(inspect.signature(function.value).parameters)
                    return kwargs[parameters[key]]
                if key in kwargs:
                    return kwargs[key]
                return (
                    inspect.signature(function.value)
                    .bind(*args, **kwargs)
                    .arguments[key]
                )

            state, action = argument(contract.state_arg), argument(contract.action_arg)
            predicted = (
                result
                if contract.output_index is None
                else self.subscript(
                    site, result, self.literal(site, contract.output_index)
                )
            )
            # The declared contract defines the call boundary; its internal arithmetic
            # and opaque implementation are not independently counted.
            out = self.make(
                "transition",
                site,
                predicted.value,
                [state, action],
                depth=(state.depth or 0) + 1,
                state_parent=state.ref,
                unit=contract.unit,
                duration=contract.duration,
                basis="declared model",
                model=name,
                candidate_key=candidate_key(action.value),
            )
            if contract.output_index is None:
                return out
            heap = self._heap(result, site)
            heap.items[contract.output_index] = out
            heap.whole = self.event("model-result", site, (out.ref,))
            return replace(result, ref=heap.whole)
        if planner:
            result = self._invoke(site, function, args, kwargs)
            out = self.make(
                "planner",
                site,
                result.value,
                args + list(kwargs.values()),
                planner=name,
            )
            out.context = (*result.context, out.ref)
            return out
        return self._invoke(site, function, args, kwargs)

    def _assess(self, site, function, args, kwargs, contract, name):
        key = contract.candidate_arg
        if isinstance(key, int) and key < len(args):
            candidate = args[key]
        else:
            parameters = list(inspect.signature(function.value).parameters)
            key = parameters[key] if isinstance(key, int) else key
            bound = inspect.signature(function.value).bind(*args, **kwargs)
            if key not in bound.arguments:
                raise ValueError("Assessment candidate must be supplied explicitly")
            candidate = bound.arguments[key]
        # Snapshot dependencies before invocation. The declared pure boundary
        # replaces internal tracing; its body still executes exactly once.
        operands = [self._whole(v) for v in args + list(kwargs.values())]
        identity = candidate_key(candidate.value)
        horizon = candidate_horizon(candidate.value, contract)
        hypothesis = self.make(
            "hypothesis",
            site,
            candidate.value,
            [self._whole(candidate)],
            basis="declared assessment",
            category=contract.category,
            candidate_kind=contract.candidate_kind,
            candidate_key=identity,
        )
        self.suppressed_transitions += 1
        try:
            target = getattr(function.value, "__func__", function.value)
            if getattr(target, "__policy_graph_instrumented__", False):
                result = self._invoke(site, function, args, kwargs)
                actual = result.value
            else:
                actual = function.value(
                    *(v.value for v in args), **{k: v.value for k, v in kwargs.items()}
                )
        finally:
            self.suppressed_transitions -= 1
        return self.make(
            "assessment",
            site,
            actual,
            [hypothesis, *operands],
            hypothesis_id=hypothesis.ref,
            basis="declared assessment",
            category=contract.category,
            candidate_kind=contract.candidate_kind,
            candidate_key=identity,
            horizon=horizon,
            horizon_unit=contract.horizon_unit,
            model_free=contract.model_free,
            assessor=name,
        )

    def choose(self, site, fn, args, kwargs):
        if (
            not args
            or set(kwargs) - {"key", "default"}
            or (len(args) > 1 and "default" in kwargs)
        ):
            # Let Python produce its usual error before invoking any callbacks.
            return self._unsupported_form(site, fn, args, kwargs)
        key = kwargs.get("key")
        candidates = self.elements(site, args[0]) if len(args) == 1 else iter(args)
        values, scores, identities = [], [], []
        best = 0
        for candidate in candidates:
            identities.append(candidate_key(candidate.value))
            candidate = replace(candidate, candidate=candidate.depth is None)
            score = (
                self.call(site, key, [candidate], {})
                if key and key.value is not None
                else candidate
            )
            values.append(candidate)
            scores.append(self._whole(score))
            if len(scores) == 1 or (
                score.value < scores[best].value
                if fn is min
                else score.value > scores[best].value
            ):
                best = len(scores) - 1
        if not scores:
            if "default" in kwargs:
                return kwargs["default"]
            raise ValueError(f"{fn.__name__}() arg is an empty sequence")
        chosen = values[best]
        ref = self.event(
            "choice",
            site,
            [v.ref for v in (*scores, chosen)],
            depth=chosen.depth,
            score_roots=[s.ref for s in scores],
            candidates=len(values),
            candidate_keys=identities,
            selected=best,
        )
        return replace(chosen, ref=ref, context=(*chosen.context, ref))

    def _native(self, site, function, args, kwargs):
        fn = function.value
        receiver = function.receiver
        raw = [v.value for v in args]
        kw = {k: v.value for k, v in kwargs.items()}
        if fn is min or fn is max:
            return self.choose(site, fn, args, kwargs)
        if fn is list or fn is tuple:
            if len(args) > 1 or kwargs:
                return self._unsupported_form(site, fn, args, kwargs)
            items = list(self.elements(site, args[0])) if args else []
            return self.container(site, "list" if fn is list else "tuple", items)
        if (
            fn is dict
            and len(args) <= 1
            and not kwargs
            and (not args or type(args[0].value) is dict)
        ):
            items = (
                []
                if not args
                else [
                    (k, self.subscript(site, args[0], k))
                    for k in self.elements(site, args[0])
                ]
            )
            return self.container(site, "dict", items)
        if fn is sorted:
            if len(args) != 1 or set(kwargs) - {"key", "reverse"}:
                return self._unsupported_form(site, fn, args, kwargs)
            base = args[0]
            items = list(self.elements(site, base))
            key = kwargs.get("key")
            scores = []
            identities = []

            def score(index):
                value = items[index]
                identities.append(candidate_key(value.value))
                value = replace(value, candidate=value.depth is None)
                out = (
                    self.call(site, key, [value], {})
                    if key and key.value is not None
                    else value
                )
                scores.append(self._whole(out))
                return out.value

            order = sorted(
                range(len(items)), key=score, reverse=kw.get("reverse", False)
            )
            choice = self.event(
                "choice",
                site,
                [v.ref for v in scores],
                score_roots=[v.ref for v in scores],
                candidates=len(items),
                candidate_keys=identities,
            )
            out = self.container(
                site,
                "list",
                [replace(items[i], context=(*items[i].context, choice)) for i in order],
            )
            out.context = (*out.context, choice)
            return out
        if receiver is not None and type(receiver.value) in (list, dict):
            result = self._container_method(site, function, args, kwargs)
            if result is not None:
                return result
        np = _numpy()
        if np is not None:
            result = self._numpy_call(site, function, args, kwargs, np)
            if result is not None:
                return result
        if (
            fn is enumerate
            and args
            and (
                type(args[0].value) in (list, tuple, range, str, bytes)
                or (np is not None and type(args[0].value) is np.ndarray)
            )
        ):
            start = raw[1] if len(raw) > 1 else kw.get("start", 0)
            actual = fn(*raw, **kw)
            self.iterators[id(actual)] = (actual, args[0], start)
            return self.make("enumerate", site, actual, args)
        if any(
            fn is native
            for native in (
                abs,
                len,
                range,
                int,
                float,
                bool,
                str,
                round,
                pow,
                sum,
                all,
                any,
            )
        ):
            if not all(self._ordinary(v.value) for v in args + list(kwargs.values())):
                return self._opaque_call(
                    site,
                    lambda: fn(*raw, **kw),
                    args + list(kwargs.values()),
                    "Builtin on unsupported value requires an adapter",
                )
            actual = fn(*raw, **kw)
            operands = [self._whole(v) for v in args] + list(kwargs.values())
            if fn is len and id(args[0].value) in self.heap:
                base = args[0]
                ref = self.event(
                    "length", site, (self.heap[id(base.value)].structure, *base.context)
                )
                return Value(actual, ref)
            preserve = (fn is int or fn is float) and args
            return self.make(
                "builtin",
                site,
                actual,
                operands,
                depth=args[0].depth if preserve else None,
                candidate=any(v.candidate for v in args),
                builtin=self._name(fn),
            )
        if (
            inspect.isclass(fn)
            and type(fn) is type
            and fn.__new__ is object.__new__
            and (
                fn.__init__ is object.__init__
                or getattr(fn.__init__, "__policy_graph_instrumented__", False)
            )
        ):
            actual = fn(*raw, **kw)
            return self.make("construction", site, actual, args + list(kwargs.values()))
        name = self._name(fn)
        if name.startswith("math.") or any(
            self._matches(name, p) for p in self.config.pure_functions
        ):
            # A declared-pure method also reads its receiver.
            bound = receiver is not None and getattr(fn, "__self__", None) is (
                receiver.value
            )
            return self.make(
                "declared-pure",
                site,
                fn(*raw, **kw),
                [self._whole(v) for v in ([receiver] if bound else []) + args]
                + list(kwargs.values()),
            )
        operands = ([receiver] if receiver else []) + args + list(kwargs.values())
        return self._opaque_call(
            site,
            lambda: fn(*raw, **kw),
            operands,
            f"Opaque call: {name or type(fn).__name__}",
        )

    @staticmethod
    def _numpy_name(fn, np):
        """Qualified name of a NumPy function, ufunc (method) or array method."""
        if isinstance(fn, np.ufunc):
            return f"numpy.{fn.__name__}"
        owner = getattr(fn, "__self__", None)
        if isinstance(owner, np.ufunc):
            return f"numpy.{owner.__name__}.{fn.__name__}"
        if owner is not None and _numpy_value(owner, np):
            return f"numpy.ndarray.{fn.__name__}"
        module = getattr(fn, "__module__", None) or ""
        if module == "numpy" or module.startswith("numpy."):
            return f"{module}.{getattr(fn, '__name__', '')}"
        return None

    def _numpy_operand(self, value, np, depth=0):
        """Arguments NumPy can consume without executing traced or user code."""
        if type(value) in SCALARS or value is Ellipsis or type(value) in (range, slice):
            return True
        if _numpy_value(value, np) or isinstance(value, (np.dtype, np.ufunc)):
            return True
        if inspect.isclass(value):
            return value.__module__ in ("builtins", "numpy")
        if type(value) in (list, tuple) and depth < 6:
            return all(self._numpy_operand(v, np, depth + 1) for v in value)
        if type(value) is dict and depth < 6:
            return all(self._numpy_operand(v, np, depth + 1) for v in value.values())
        return False

    def _numpy_call(self, site, function, args, kwargs, np):
        """Pure NumPy operations get whole-value dependencies; writes update buffers.

        Random generators, I/O, callbacks and object arrays remain opaque. Output
        arrays (``out=``, in-place functions/methods, ufunc.at) are mutations.
        """
        fn = function.value
        name = self._numpy_name(fn, np)
        if name is None or name.startswith(NUMPY_EXCLUDED):
            return None
        short = name.rsplit(".", 1)[-1]
        receiver = None
        if name.startswith("numpy.ndarray."):
            receiver = function.receiver
            if receiver is None or receiver.value is not fn.__self__:
                return None  # A bound method without its array's provenance.
        if short in NUMPY_IO:
            return None
        values = ([receiver] if receiver else []) + args + list(kwargs.values())
        if not all(self._numpy_operand(v.value, np) for v in values):
            return None
        actual = fn(*(v.value for v in args), **{k: v.value for k, v in kwargs.items()})
        operands = [self._whole(v) for v in values]
        targets = []
        if receiver is not None and short in NUMPY_INPLACE_METHODS:
            targets.append(receiver)
        elif (
            receiver is None
            and args
            and (
                short in NUMPY_INPLACE_FUNCTIONS
                or (
                    isinstance(getattr(fn, "__self__", None), np.ufunc)
                    and short == "at"
                )
            )
        ):
            targets.append(args[0])
        if isinstance(fn, np.ufunc):
            targets.extend(args[fn.nin :])  # Positional outputs.
        if "out" in kwargs:
            out = kwargs["out"]
            targets.extend(
                [out]
                if type(out.value) is np.ndarray
                else list(self.elements(site, out)) if type(out.value) is tuple else []
            )
        # An argument returned as the result may be an output parameter.
        targets.extend(
            v for v in args if v.value is actual and type(actual) is np.ndarray
        )
        detail = {"numpy": name}
        if receiver is not None and (short == "tolist" or (short == "item" and args)):
            # Separately addressable parts carry whole-array provenance.
            if receiver.value.size > 1:
                detail["imprecise_parents"] = (operands[0].ref,)
        depth = values[0].depth if values and short in NUMPY_CONVERSIONS else None
        ref = self.event(
            "array-operation", site, [v.ref for v in operands], depth=depth, **detail
        )
        written = {}
        for target in targets:
            if type(target.value) is np.ndarray and id(target.value) not in written:
                written[id(target.value)] = self._array_update(
                    site, target, parents=(ref,), kind="array-write", numpy=name
                )
        if type(actual) is np.ndarray and id(actual) in written:
            ref = written[id(actual)]
        return Value(
            actual,
            ref,
            depth,
            any(v.candidate for v in values),
            tuple(self.frame.controls[-1:]),
        )

    def _unsupported_form(self, site, fn, args, kwargs, skip=0):
        """Argument forms Python normally rejects; run natively for its error.

        Should one be accepted, its result and possible mutations are unknown.
        ``skip`` leading operands (a bound receiver) are not passed again.
        """
        return self._opaque_call(
            site,
            lambda: fn(
                *(v.value for v in args[skip:]),
                **{k: v.value for k, v in kwargs.items()},
            ),
            [*args, *kwargs.values()],
            "Unsupported argument form",
        )

    def _container_method(self, site, function, args, kwargs):
        base, name = function.receiver, function.attribute
        arity = {
            "__getitem__": (1, 1),
            "get": (1, 2),
            "append": (1, 1),
            "extend": (1, 1),
            "pop": (1, 2) if type(base.value) is dict else (0, 1),
            "copy": (0, 0),
            "clear": (0, 0),
        }
        if name in arity:
            low, high = arity[name]
            if kwargs or not low <= len(args) <= high:
                return self._unsupported_form(
                    site, function.value, [base, *args], kwargs, skip=1
                )
        heap = self._heap(base, site)
        if name == "__getitem__":
            return self.subscript(site, base, args[0])
        if type(base.value) is dict and name == "get":
            key = args[0]
            if key.value in base.value:
                return self.subscript(site, base, key)
            return self._copy(
                "dict-default",
                site,
                args[1] if len(args) > 1 else self.literal(site, None),
                key,
                Value(base.value, heap.structure),
            )
        if type(base.value) is list and name == "append":
            i = len(base.value)
            base.value.append(args[0].value)
            heap.items[i] = self._copy("append", site, args[0])
            heap.whole = self.event(
                "object-mutation", site, (heap.whole, heap.items[i].ref)
            )
            heap.structure = self.event("structure-write", site, (heap.structure,))
            return self.literal(site, None)
        if type(base.value) is list and name == "extend":
            values = self.elements(site, args[0])
            if args[0].value is base.value:
                values = list(values)
            for value in values:
                append = replace(function, attribute="append", value=base.value.append)
                self._container_method(site, append, [value], {})
            return self.literal(site, None)
        if name == "pop":
            key = args[0] if args else self.literal(site, -1)
            if type(base.value) is dict and key.value not in base.value:
                if len(args) > 1:
                    return self._copy(
                        "pop-default",
                        site,
                        args[1],
                        key,
                        Value(base.value, heap.structure),
                    )
                raise KeyError(key.value)
            value = self.subscript(site, base, key)
            base.value.pop(key.value)
            if type(base.value) is list:
                k = key.value if key.value >= 0 else key.value + len(base.value) + 1
                heap.items = {
                    i if i < k else i - 1: v for i, v in heap.items.items() if i != k
                }
            else:
                heap.items.pop(key.value, None)
            heap.structure = self.event(
                "structure-write", site, (heap.structure, key.ref)
            )
            heap.whole = self.event(
                "object-mutation",
                site,
                (heap.structure, *(v.ref for v in heap.items.values())),
            )
            return value
        if name == "copy":
            if type(base.value) is list:
                return self.container(site, "list", list(self.elements(site, base)))
            return self.container(
                site,
                "dict",
                [(k, self.subscript(site, base, k)) for k in self.elements(site, base)],
            )
        if name == "clear":
            base.value.clear()
            heap.items.clear()
            heap.structure = heap.whole = self.event("clear", site)
            return self.literal(site, None)
        return None
