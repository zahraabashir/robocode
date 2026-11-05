"""Explicit role evidence and typed measurements above the execution graph.

Contracts declare prospective meaning; automatic arithmetic remains a heuristic.
No policy names, source fingerprints, or benchmark identities are inspected here.
"""

from __future__ import annotations

import hashlib
import json
import math


def candidate_key(value):
    """Fingerprint bounded plain values without invoking user equality/repr hooks.

    Type-sensitive structural equality is an operational identity convention,
    not a claim that two representations describe different world behaviors.
    Arbitrary objects, cycles, huge values and NaNs produce unknown identity.
    """
    budget = [256]

    def freeze(item, depth):
        budget[0] -= 1
        if budget[0] < 0 or depth > 8:
            raise ValueError
        kind = type(item)
        if kind in (type(None), bool, int, float, str):
            if kind is float and not math.isfinite(item):
                raise ValueError
            if kind is float and item == 0.0:
                item = 0.0  # Signed zeros denote the same scalar candidate.
            if kind is str and len(item) > 4096:
                raise ValueError
            if kind is int and item.bit_length() > 1024:
                raise ValueError
            return (kind.__name__, item)
        if kind in (list, tuple):
            if len(item) > budget[0]:
                raise ValueError
            return (kind.__name__, [freeze(v, depth + 1) for v in item])
        raise ValueError

    try:
        payload = json.dumps(freeze(value, 0), separators=(",", ":"))
    except ValueError:
        return None
    return hashlib.sha256(payload.encode()).hexdigest()


def candidate_horizon(value, contract):
    """Measure only the explicitly declared sequence extent, never rollout depth."""
    if contract.horizon is None or type(value) not in (list, tuple):
        return None
    return max(0, len(value) - (contract.horizon == "sequence_edges"))


def _metric(value, unit, *, invalid=False, basis=None, missing="unknown"):
    return {
        "value": None if invalid else value,
        "unit": unit,
        "status": (
            "unknown" if invalid else ("measured" if value is not None else missing)
        ),
        "basis": basis,
    }


def semantic_profile(graph, planning, actions):
    """Attach inspectable role bindings; do not turn heuristic meaning into fact."""
    episodes = []
    # Indexes instead of rescanning every action's ID list per planning event.
    indices = {}
    for action in actions:
        for i in action["planning_event_ids"]:
            indices.setdefault(i, []).append(action["index"])
    assessed = {p["id"]: p.get("assessment_ids", []) for p in planning}
    for p in planning:
        transitions = [graph.events[i] for i in p["transition_ids"]]
        assessments = [graph.events[i] for i in p.get("assessment_ids", [])]
        selectors = [graph.events[i] for i in p["selector_ids"]]
        hypotheses = sorted(
            {e.detail["hypothesis_id"] for e in assessments}
            | {e.id for e in transitions}
        )
        basis = sorted(
            {e.detail.get("basis", "unspecified") for e in transitions}
            | {e.detail["basis"] for e in assessments}
        )
        recognition = p.get("recognition")
        if recognition:
            basis.append(recognition["basis"] + ": " + recognition["rule"])
        if p["kind"] == "planner":
            basis.append("declared/known planner; internal roles unavailable")
        assessment_ids = p.get("assessment_ids", []) or p.get("score_root_ids", [])
        if recognition and not hypotheses:
            hypotheses = recognition["witness_ids"]
        complete_roles = bool(hypotheses and assessment_ids and p["kind"] != "model")
        categories = sorted(
            {e.detail["category"] for e in assessments}
            | ({"action_effect"} if transitions else set())
        )
        keys = []
        candidate_kind = None
        evaluations = None
        if assessments:
            kinds = {e.detail["candidate_kind"] for e in assessments}
            candidate_kind = next(iter(kinds)) if len(kinds) == 1 else "mixed"
            keys = [e.detail["candidate_key"] for e in assessments]
            evaluations = len(assessments)
            if len(kinds) > 1:
                keys = []
        elif all(e.kind == "choice" for e in selectors):
            candidate_kind = "selection inputs (assumed prospective)"
            keys = [
                key for e in selectors for key in e.detail.get("candidate_keys", [])
            ]
            evaluations = sum(e.detail.get("candidates", 0) for e in selectors)
        elif transitions:
            candidate_kind = "first-step actions (assumed prospective)"
            keys = [e.detail.get("candidate_key") for e in transitions if e.depth == 1]
        breadth = len(set(keys)) if keys and all(k is not None for k in keys) else None
        invalid = bool(graph.incomplete or p["reasons"])
        model_free = bool(assessments) and all(
            e.detail.get("model_free", False) for e in assessments
        )
        horizon_units = {
            e.detail["horizon_unit"]
            for e in assessments
            if e.detail.get("horizon_unit") is not None
        }
        horizons = [e.detail.get("horizon") for e in assessments]
        horizon = (
            max(horizons)
            if len(horizon_units) == 1
            and horizons
            and all(h is not None for h in horizons)
            else None
        )
        episodes.append(
            {
                "planning_event_id": p["id"],
                "structural_evidence": recognition,
                "phase": p["phase"],
                "categories": categories,
                "interpretation_basis": basis,
                "role_basis": {
                    "hypothesis": basis,
                    "assessment": (
                        "declared API semantics"
                        if assessments
                        else "inferred from score/comparison dependencies"
                    ),
                    "decision": "inferred from value selection or control flow",
                },
                "roles": {
                    "hypothesis": hypotheses,
                    "assessment": sorted(set(assessment_ids)),
                    "decision": p["selector_ids"] if p["kind"] != "model" else [],
                },
                "role_chain_present": complete_roles,
                "action_indices": indices.get(p["id"], []),
                "action_relevant": p["action_relevant"],
                "candidate_kind": candidate_kind,
                "measurements": {
                    "model_depth": _metric(
                        p["depth"],
                        p["unit"] or "model steps",
                        invalid=invalid,
                        missing=(
                            "not_applicable"
                            if model_free and not transitions
                            else "unknown"
                        ),
                    ),
                    "transition_work": _metric(
                        (
                            len(transitions)
                            if transitions and p["work"] is not None
                            else None
                        ),
                        "transition evaluations",
                        invalid=invalid,
                        missing="not_applicable" if model_free else "unknown",
                    ),
                    "breadth": _metric(
                        breadth,
                        "distinct candidates",
                        invalid=invalid,
                        basis=(
                            "type-sensitive structural identity "
                            "within this decision group"
                        ),
                    ),
                    "candidate_evaluations": _metric(
                        evaluations, "candidate evaluations", invalid=invalid
                    ),
                    "max_assessed_horizon": _metric(
                        horizon,
                        next(iter(horizon_units)) if len(horizon_units) == 1 else None,
                        invalid=invalid,
                        missing="not_applicable" if not horizon_units else "unknown",
                    ),
                },
            }
        )
    performed_ids = {i for p in planning for i in p.get("assessment_ids", [])}
    relevant_ids = {
        i for p in planning if p["action_relevant"] for i in p.get("assessment_ids", [])
    }
    return {
        "version": "planning-semantics-1",
        "episodes": episodes,
        "interpretation_is_conditional": True,
        "scope": (
            "Recognized events only; " "this is not proof of complete semantic coverage"
        ),
        "declared_assessment_work": {
            "performed": None if graph.incomplete else len(performed_ids),
            "action_relevant": None if graph.incomplete else len(relevant_ids),
            "unit": "assessment evaluations in recognized decisions",
        },
        "actions": [
            {
                "index": action["index"],
                "associated_assessment_ids": sorted(
                    {
                        i
                        for p in action["planning_event_ids"]
                        for i in assessed.get(p, [])
                    }
                ),
                "new_assessment_work": (
                    None
                    if graph.incomplete
                    else len(
                        {
                            i
                            for p in action["planning_event_ids"]
                            for i in assessed.get(p, [])
                            if graph.events[i].phase == action["phase"]
                        }
                    )
                ),
            }
            for action in actions
        ],
    }
