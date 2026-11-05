"""Score observed planning decisions and retain references to cached events.

Dependency queries use forward passes over the append-only event list instead of
one backward traversal per decision or action. Parents always precede children,
so each event's set of relevant ancestors is the union of its parents' sets,
stored as an integer bitset over the (few) events a query actually asks about.
"""

from dataclasses import asdict

from .semantics import semantic_profile

VERSION = "runtime-planning-5"
DECISIONS = ("choice", "condition", "planner", "call-return")
ID_LIMIT = 100  # Per-action unknown IDs listed; the count is always complete.
COMPARISON, CALL_RETURN, CHOICE, OPAQUE = 1, 2, 4, 8
UNCHECKED = (
    "Baseline action-slice rules were not applied: the static slice does not "
    "contain this choice"
)
FLAGS = {"comparison": COMPARISON, "call-return": CALL_RETURN, "choice": CHOICE}
BYTE_BITS = [tuple(i for i in range(8) if b >> i & 1) for b in range(256)]


class _Reach:
    """For every event, which members of ``interesting`` it transitively depends on.

    ``exact`` skips edges recorded as conservative whole-value approximations.
    ``roots`` maps an event to the parents whose union is queried at that event
    (``backward_slice(roots)`` excludes the event itself); ``keep`` retains the
    event's own set. Other sets are released once their last child is processed.
    """

    def __init__(
        self, graph, interesting, *, roots=None, keep=(), exact=False, flags=False
    ):
        # pylint: disable=too-many-locals
        events = graph.events
        self.ids = sorted(interesting)
        self.position = position = {e: i for i, e in enumerate(self.ids)}
        roots, keep = roots or {}, set(keep)
        parents = [graph.parents(e, exact=exact) for e in events]
        consumers = [
            set(ps) | set(roots.get(i, ())) if i in roots else ps
            for i, ps in enumerate(parents)
        ]
        remaining = [0] * len(events)
        for refs in consumers:
            for p in refs:
                remaining[p] += 1
        bits = [0] * len(events)
        # Kind flags (comparison, call-return, choice, opaque) in each slice.
        self.flags = marks = [0] * len(events) if flags else None
        self.at = at = {}  # Union over an event's declared roots.
        self.kept = kept = {}
        for event in events:
            i = event.id
            b = 1 << position[i] if i in position else 0
            ps = parents[i]
            for p in ps:
                bp = bits[p]
                if bp:
                    b |= bp
            bits[i] = b
            if marks is not None:
                f = OPAQUE if event.kind == "opaque" else FLAGS.get(event.kind, 0)
                for p in ps:
                    f |= marks[p]
                marks[i] = f
            if i in roots:
                rb = rf = 0
                for r in roots[i]:
                    rb |= bits[r]
                    if marks is not None:
                        rf |= marks[r]
                at[i] = (rb, rf)
            if i in keep:
                kept[i] = b
            for p in consumers[i]:
                remaining[p] -= 1
                if not remaining[p]:
                    bits[p] = 0
            if not remaining[i]:
                bits[i] = 0

    def mask(self, members):
        """Bitset of the given interesting event IDs."""
        out = 0
        for e in members:
            if e in self.position:
                out |= 1 << self.position[e]
        return out

    def decode(self, bits, limit=None):
        """Event IDs in a bitset, ascending; at most ``limit`` of them."""
        out = []
        if bits.bit_count() <= 64:  # Sparse: extract the lowest bit repeatedly.
            while bits and (limit is None or len(out) < limit):
                low = bits & -bits
                out.append(self.ids[low.bit_length() - 1])
                bits ^= low
            return out
        data = bits.to_bytes((bits.bit_length() + 7) // 8, "little")
        for index, byte in enumerate(data):
            if byte:
                for offset in BYTE_BITS[byte]:
                    out.append(self.ids[index * 8 + offset])
                if limit is not None and len(out) >= limit:
                    return out[:limit]
        return out


def _group(key, groups, event, recognition):
    return groups.setdefault(
        key,
        {
            "id": event.id,
            "selectors": [],
            "bits": 0,
            "exact_bits": 0,
            "score_roots": set(),
            "phase": event.phase,
            "kind": event.kind,
            "site": event.site,
            "recognition": recognition,
        },
    )


def report(recorder, metadata=None, *, include_graph=False):
    """Summarize observed planning work and its relation to returned actions."""
    # pylint: disable=too-many-locals,too-many-branches,too-many-statements
    g = recorder.graph
    events = g.events
    recognition = recorder.recognition
    imprecise_ids = [e.id for e in events if e.detail.get("imprecise_parents")]
    transitions = [e.id for e in events if e.kind == "transition"]
    assessments = [e.id for e in events if e.kind == "assessment"]
    sites = recognition.witness_kinds() if recognition is not None else {}
    witnesses = {
        e.id
        for e in events
        if e.kind in sites.get((e.site.file, e.site.line), ())
        and not e.detail.get("contract_internal")
    }
    candidates = [
        e
        for e in events
        if e.kind in DECISIONS and not e.detail.get("contract_internal")
    ]
    roots = {e.id: e.detail.get("score_roots", e.data) for e in candidates}
    models = [
        i for i in transitions if events[i].detail.get("basis") == "declared model"
    ]
    reach = _Reach(
        g,
        set(transitions) | set(assessments) | witnesses,
        roots=roots,
        keep=models,
        flags=True,
    )
    exact = (
        _Reach(
            g, set(transitions) | set(assessments), roots=roots, keep=models, exact=True
        )
        if imprecise_ids
        else reach
    )
    transition_mask = reach.mask(transitions)
    assessment_mask = reach.mask(assessments)
    exact_transition_mask = exact.mask(transitions)
    # One mask per required (candidate, role): a match is a few bitwise ANDs.
    by_site = {}
    for i in witnesses:
        e = events[i]
        by_site.setdefault((e.site.file, e.site.line, e.kind), []).append(i)
    role_masks = (
        [
            [
                (
                    role,
                    reach.mask(
                        [
                            i
                            for kind in kinds
                            for i in by_site.get((file, line, kind), ())
                        ]
                    ),
                )
                for role, file, line, kinds in roles
            ]
            for roles in recognition.roles
        ]
        if recognition is not None
        else []
    )

    groups = {}
    for event in candidates:
        deps, flags = reach.at[event.id]
        found = None
        candidates = (
            recognition.applicable_evidence(event) if recognition is not None else ()
        )
        if candidates:
            # Witnesses are executed events in this decision's slice, or itself.
            bits = deps | (reach.mask([event.id]) if event.id in witnesses else 0)
            checked = event.kind != "condition" or flags & (COMPARISON | CALL_RETURN)
            for index in candidates:
                masks = role_masks[index]
                if masks and checked and all(bits & m for _, m in masks):
                    found = (index, bits)  # Witness IDs are decoded once, below.
                    break
        has_transitions = bool(deps & transition_mask)
        has_assessments = bool(deps & assessment_mask)
        if event.kind == "call-return":
            if found is None or flags & CHOICE:
                continue
        if event.kind == "condition":
            if (
                not found
                and not has_assessments
                and (not has_transitions or not flags & COMPARISON)
            ):
                continue
            key = (
                event.invocation,
                event.site.file,
                event.site.line,
                event.site.column,
            )
        else:
            key = event.id
        if (
            not found
            and not has_transitions
            and not has_assessments
            and event.kind != "planner"
        ):
            continue
        group = _group(key, groups, event, found)
        if found:
            group["recognition"] = found
        group["selectors"].append(event.id)
        group["bits"] |= deps & (transition_mask | assessment_mask)
        group["exact_bits"] |= exact.at[event.id][0] if exact is not reach else deps
        group["score_roots"].update(roots[event.id])

    # Which planning selectors, model transitions and unknowns each action uses.
    selectors = {s for group in groups.values() for s in group["selectors"]}
    opaque = [e.id for e in events if e.kind == "opaque"]
    action_roots = {a: (a,) for a in recorder.actions}
    used_by = _Reach(g, selectors | set(models) | set(opaque), roots=action_roots)
    exact_used_by = (
        _Reach(g, selectors | set(models), roots=action_roots, exact=True)
        if imprecise_ids
        else used_by
    )
    selector_mask = used_by.mask(selectors | set(models))
    opaque_mask = used_by.mask(opaque)
    relevant_bits = exact_relevant_bits = 0
    for action in recorder.actions:
        relevant_bits |= used_by.at[action][0]
        exact_relevant_bits |= exact_used_by.at[action][0]
    relevant = set(used_by.decode(relevant_bits & selector_mask))
    exact_relevant = (
        set(exact_used_by.decode(exact_relevant_bits))
        if exact_used_by is not used_by
        else relevant
    )

    for group in groups.values():
        if group.get("recognition"):
            index, bits = group["recognition"]
            role_ids = {}
            for role, mask in role_masks[index]:
                role_ids.setdefault(role, []).extend(reach.decode(bits & mask))
            group["recognition"] = recognition.describe(index, role_ids)
    covered = 0
    for group in groups.values():
        covered |= group["bits"]
    covered_ids = set(reach.decode(covered & transition_mask))
    for i in models:
        if i in relevant and i not in covered_ids:
            event = events[i]
            group = _group(("direct-model", event.phase), groups, event, None)
            group["kind"] = "model"
            group["selectors"].append(i)
            group["bits"] |= reach.kept[i] & transition_mask
            group["exact_bits"] |= (
                exact.kept[i] if exact is not reach else reach.kept[i]
            )

    planning = []
    for group in groups.values():
        ids = set(reach.decode(group["bits"] & transition_mask))
        exact_ids = (
            set(exact.decode(group["exact_bits"] & exact_transition_mask))
            if exact is not reach
            else ids
        )
        assessed = reach.decode(group["bits"] & assessment_mask)
        units = {events[i].detail.get("unit", "model steps") for i in ids}
        reasons = []
        if group["kind"] == "planner":
            reasons.append("Opaque planner has no transition-count contract")
        if any(reach.flags[s] & OPAQUE for s in group["selectors"]):
            reasons.append("Unsupported dependencies reach this planning event")
        if ids != exact_ids:
            reasons.append("Whole-array dependencies may include unrelated transitions")
        if len(units) > 1:
            reasons.append("Transitions use different abstraction units")
        if g.incomplete:
            reasons.append(g.incomplete)
        structural_only = bool(group.get("recognition")) and (
            group["recognition"]["rule"] != "lookahead" or not ids
        )
        unmeasured = reasons or structural_only or (assessed and not ids)
        is_exact = bool(set(group["selectors"]) & exact_relevant)
        if (
            is_exact
            and not ids
            and not assessed
            and (group.get("recognition") or {}).get("action_slice_rules")
            == "unchecked"
        ):
            # Only the baseline rule supports this decision, and its target-choice
            # rejection was never evaluated: relevance is unresolved, not claimed.
            is_exact = False
            reasons.append(UNCHECKED)
        planning.append(
            {
                "id": group["id"],
                "recognition": group.get("recognition"),
                "phase": group["phase"],
                "kind": group["kind"],
                "site": asdict(group["site"]),
                "selector_ids": group["selectors"],
                "transition_ids": sorted(ids),
                "assessment_ids": sorted(assessed),
                "score_root_ids": sorted(group["score_roots"]),
                "action_relevant": is_exact,
                "possibly_action_relevant": not is_exact
                and bool(set(group["selectors"]) & relevant),
                "depth": (
                    None
                    if unmeasured
                    else max((events[i].depth or 0 for i in ids), default=0)
                ),
                "work": None if unmeasured else len(ids),
                "unit": next(iter(units)) if len(units) == 1 else None,
                "status": "unknown" if reasons else "observed",
                "reasons": reasons,
            }
        )
    by_selector = {s: p for p in planning for s in p["selector_ids"]}
    order = {id(p): k for k, p in enumerate(planning)}
    action_reports = []
    for index, action in enumerate(recorder.actions):
        bits = used_by.at[action][0]
        exact_bits = exact_used_by.at[action][0]
        mine = set(used_by.decode(bits & selector_mask)) & set(by_selector)
        exact_mine = (
            set(exact_used_by.decode(exact_bits)) & mine
            if exact_used_by is not used_by
            else mine
        )
        events_ = sorted(
            {id(by_selector[s]): by_selector[s] for s in mine}.values(),
            key=lambda p: order[id(p)],
        )
        certain = [p for p in events_ if not exact_mine.isdisjoint(p["selector_ids"])]
        certain_ids = {id(p) for p in certain}  # Identity: dict equality is deep.
        possible = [p for p in events_ if id(p) not in certain_ids]
        unknown_count = (bits & opaque_mask).bit_count()
        unknown = used_by.decode(bits & opaque_mask, ID_LIMIT)
        action_units = {p["unit"] for p in certain if p["unit"] is not None}
        invalid = bool(
            unknown_count
            or g.incomplete
            or possible
            or len(action_units) > 1
            or any(p["depth"] is None for p in certain)
        )
        updates = set().union(*(set(p["transition_ids"]) for p in certain))
        phase = events[action].phase
        new = {i for i in updates if events[i].phase == phase}
        action_reports.append(
            {
                "index": index,
                "return_event": action,
                "phase": phase,
                "planning_event_ids": [p["id"] for p in certain],
                "possible_planning_event_ids": [p["id"] for p in possible],
                "planning_depth": (
                    None if invalid else max((p["depth"] for p in certain), default=0)
                ),
                "new_planning_work": None if invalid else len(new),
                "inherited_planning_event_ids": [
                    p["id"] for p in certain if p["phase"] != phase
                ],
                "status": (
                    "partial"
                    if invalid
                    and not unknown_count
                    and not g.incomplete
                    and not possible
                    and len(action_units) <= 1
                    and certain
                    and all(p["status"] == "observed" for p in certain)
                    else "unknown" if invalid else "observed"
                ),
                "unknown_event_ids": unknown,
                "unknown_event_count": unknown_count,
            }
        )
    used = [p for p in planning if p["action_relevant"]]
    possible = [p for p in planning if p["possibly_action_relevant"]]
    unchecked = [p for p in possible if UNCHECKED in p["reasons"]]
    unchecked_ids = {id(p) for p in unchecked}
    unknown_bits = relevant_bits & opaque_mask
    unknown_count = unknown_bits.bit_count()
    unknown = used_by.decode(unknown_bits)
    units = {p["unit"] for p in used if p["unit"] is not None}
    invalid = bool(
        unknown
        or g.incomplete
        or possible
        or len(units) > 1
        or not recorder.actions
        or any(p["depth"] is None for p in used)
    )
    updates = set().union(*(set(p["transition_ids"]) for p in used))
    performed = set().union(*(set(p["transition_ids"]) for p in planning))
    uncertain_phases = {
        e.phase
        for e in events
        if e.kind == "opaque" and not e.detail.get("contract_internal")
    } | {p["phase"] for p in planning if p["work"] is None}
    calls = []
    for call in recorder.calls:
        phase = call["phase"]
        phase_updates = {i for i in performed if events[i].phase == phase}
        calls.append(
            {
                **call,
                "planning_event_ids": [
                    p["id"] for p in planning if p["phase"] == phase
                ],
                "performed_planning_work": (
                    None
                    if g.incomplete or phase in uncertain_phases
                    else len(phase_updates)
                ),
                "observed_planning_work": len(phase_updates),
            }
        )
    union = g.backward_slice(recorder.actions) if imprecise_ids else set()
    reasons = {}
    for i in unknown:
        reason = events[i].detail["reason"]
        reasons[reason] = reasons.get(reason, 0) + 1
    result = {
        "version": VERSION,
        "basis": (
            "Observed executions; conditional on transition contracts "
            "and assessment contracts, arithmetic and baseline structural heuristics"
        ),
        "verdict": (
            "planning_observed"
            if used
            else ("needs_review" if invalid else "no_planning_observed")
        ),
        "status": (
            "partial"
            if invalid
            and not unknown
            and not g.incomplete
            and not possible
            and len(units) <= 1
            and used
            and all(p["status"] == "observed" for p in used)
            else "unknown" if invalid else "observed"
        ),
        "planning_depth": (
            None if invalid else max((p["depth"] for p in used), default=0)
        ),
        "planning_work": None if invalid else len(updates),
        "performed_planning_work": (
            None if g.incomplete or uncertain_phases else len(performed)
        ),
        "planning_event_count": len(used),
        "possibly_relevant_planning_event_count": len(possible),
        "units": sorted(units),
        "support_scope": (
            "Arithmetic lookahead, declared models, assessments and planner calls; "
            "and executed baseline structural search patterns"
        ),
        "planning_calls_per_action": (
            len({p["phase"] for p in used}) / len(recorder.actions)
            if recorder.actions
            else None
        ),
        "planning_events": planning,
        "actions": action_reports,
        "calls": calls,
        "executed_prediction_updates": len(transitions),
        "unknowns": [
            {
                "event": i,
                "reason": events[i].detail["reason"],
                "site": asdict(events[i].site),
            }
            for i in unknown
        ],
        "unknown_count": unknown_count,
        "unknown_reasons": dict(sorted(reasons.items(), key=lambda kv: -kv[1])),
        "precision": {
            "basis": (
                "NumPy arrays have no element provenance; partial reads record the "
                "whole array and are flagged. Exact relevance avoids those edges."
            ),
            "imprecise_events": len(imprecise_ids),
            "imprecise_events_in_action_slices": len(union & set(imprecise_ids)),
            "possibly_relevant_planning_event_ids": [
                p["id"] for p in possible if id(p) not in unchecked_ids
            ],
            "affects_scores": any(id(p) not in unchecked_ids for p in possible)
            or any(
                "Whole-array dependencies may include unrelated transitions"
                in p["reasons"]
                for p in used
            ),
        },
        "unchecked_rule_planning_event_ids": [p["id"] for p in unchecked],
        "incomplete": g.incomplete,
        "recognition_coverage": {
            "static_candidates": (
                len(recognition.evidence) if recognition is not None else 0
            ),
            "error": recognition.error if recognition is not None else None,
            "rejected_by_action_slice_rules": (
                recognition.rejected if recognition is not None else []
            ),
        },
        "source_hashes": recorder.source_hashes,
        "config": asdict(recorder.config),
        "metadata": metadata or {},
        "event_count": len(events),
    }
    if include_graph:
        result["graph"] = g.to_dict()
    result["semantic_profile"] = semantic_profile(g, planning, action_reports)
    if not recorder.actions and not g.incomplete:
        result["status"] = result["verdict"] = "not_evaluated"
    return result
