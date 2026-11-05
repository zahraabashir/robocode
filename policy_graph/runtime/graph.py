"""Execution-instance dependencies. No policy values are serialized here."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field


@dataclass(frozen=True)
class Site:
    """A location in the original, unmodified policy source."""

    file: str
    line: int
    column: int
    function: str
    text: str = ""


@dataclass(slots=True)
class Event:
    """One executed operation, linked only to preceding dependency events.

    ``detail["imprecise_parents"]`` lists data parents whose recorded dependency
    is a conservative whole-value approximation (for example an array element read
    recorded as depending on the whole array). Exact traversals skip those edges.
    """

    id: int
    kind: str
    site: Site
    phase: str
    invocation: int
    data: tuple[int, ...] = ()
    control: tuple[int, ...] = ()
    depth: int | None = None
    detail: dict = field(default_factory=dict)


# Shared by events without details. Event details are never mutated after creation.
EMPTY: dict = {}


def _ids(refs):
    """Sorted, de-duplicated dependency IDs (most events have zero or one)."""
    if len(refs) == 1:
        return () if refs[0] is None else (refs[0],)
    return tuple(sorted({i for i in refs if i is not None})) if refs else ()


class TraceLimit(RuntimeError):
    """The trace is incomplete; do not turn the prefix into a complete score."""


class ExecutionGraph:
    """Append-only dependency DAG shared by all calls in a session."""

    def __init__(self, max_events: int = 200_000):
        self.events: list[Event] = []
        self.max_events = max_events
        self.incomplete: str | None = None

    def add(
        self, kind, site, phase, invocation, data=(), control=(), depth=None, **detail
    ):
        """Append a valid event or stop with an explicitly incomplete trace."""
        event_id = len(self.events)
        if event_id >= self.max_events:
            self.incomplete = f"Trace limit of {self.max_events} events reached"
            raise TraceLimit(self.incomplete)
        data, control = _ids(tuple(data)), _ids(tuple(control))
        if (data and (data[0] < 0 or data[-1] >= event_id)) or (
            control and (control[0] < 0 or control[-1] >= event_id)
        ):
            raise ValueError("Dependencies must refer to earlier execution events")
        self.events.append(
            Event(
                event_id,
                kind,
                site,
                phase,
                invocation,
                data,
                control,
                depth,
                detail or EMPTY,
            )
        )
        return event_id

    def parents(self, event, *, control=True, exact=False):
        """Dependency IDs of one event; ``exact`` omits whole-value approximations."""
        data = event.data
        if exact:
            imprecise = event.detail.get("imprecise_parents")
            if imprecise:
                data = tuple(i for i in data if i not in imprecise)
        return data + event.control if control else data

    def backward_slice(self, roots, *, control=True, exact=False):
        """Collect transitive dependencies of the selected event IDs."""
        seen = set()
        stack = list(roots)
        events = self.events
        while stack:
            event_id = stack.pop()
            if event_id in seen:
                continue
            seen.add(event_id)
            event = events[event_id]
            if exact and event.detail.get("imprecise_parents"):
                stack.extend(self.parents(event, control=control, exact=True))
                continue
            stack.extend(event.data)
            if control:
                stack.extend(event.control)
        return seen

    def to_dict(self):
        """Serialize graph metadata without retaining arbitrary policy values."""
        return {
            "events": [asdict(e) for e in self.events],
            "incomplete": self.incomplete,
        }

    def to_dot(self, roots=None):
        """Export the whole graph or a slice in Graphviz DOT format."""
        ids = (
            self.backward_slice(roots)
            if roots is not None
            else set(range(len(self.events)))
        )
        lines = ["digraph execution {", '  rankdir="LR";']
        for i in sorted(ids):
            e = self.events[i]
            label = f"{i}: {e.kind}\\n{e.site.function}:{e.site.line} [{e.phase}]"
            lines.append(f"  n{i} [label={json.dumps(label)}];")
            imprecise = e.detail.get("imprecise_parents") or ()
            for source in e.data:
                if source in ids:
                    label = "data (whole)" if source in imprecise else "data"
                    style = ", style=dotted" if source in imprecise else ""
                    lines.append(f'  n{source} -> n{i} [label="{label}"{style}];')
            for source in e.control:
                if source in ids:
                    lines.append(
                        f'  n{source} -> n{i} [label="control", style=dashed];'
                    )
        return "\n".join(lines + ["}"]) + "\n"
