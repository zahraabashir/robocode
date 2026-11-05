"""Compare independent semantic labels with the current runtime recognizer."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path

from policy_graph.runtime import (
    AssessmentContract,
    RuntimeConfig,
    RuntimeSession,
    TransitionContract,
)

from .cases import CASES, VERSION, WORLD_MODEL, validate_cases

TRACKS = ("automatic", "shared_contracts")
SHARED_CONTRACTS = {"world_model.step": TransitionContract()}
SHARED_ASSESSMENTS = {
    "world_model.route_clear": AssessmentContract(
        horizon="sequence_edges",
        horizon_unit="graph edges",
        model_free=True,
    ),
    "world_model.placement_cost": AssessmentContract(
        candidate_kind="placement", model_free=True
    ),
}


def track_config(track, max_events):
    """Only track-level API semantics are supplied; no per-case recognition rules."""
    if track not in TRACKS:
        raise ValueError(f"Unknown track: {track}")
    return RuntimeConfig(
        max_events=max_events,
        transition_models=(
            SHARED_CONTRACTS.copy() if track == "shared_contracts" else {}
        ),
        assessments=SHARED_ASSESSMENTS.copy() if track == "shared_contracts" else {},
    )


def _ordinary(path, calls):
    # Fixtures are trusted, finite benchmark programs, not user-uploaded code.
    # Install just the documented shared API for this ordinary execution.
    spec = importlib.util.spec_from_file_location(
        "world_model", path.parent / "world_model.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    previous = sys.modules.get("world_model")
    sys.modules["world_model"] = module
    try:
        spec.loader.exec_module(module)
        namespace = {"__file__": str(path), "__name__": "_benchmark_ordinary"}
        exec(  # pylint: disable=exec-used
            compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace
        )
        policy = (
            namespace["GeneratedApproach"]()
            if "GeneratedApproach" in namespace
            else None
        )
        result = []
        for call in calls:
            fn = (
                getattr(policy, call.method)
                if policy is not None
                else namespace[call.method]
            )
            result.append(copy.deepcopy(fn(*copy.deepcopy(call.args))))
        return result
    finally:
        if previous is None:
            sys.modules.pop("world_model", None)
        else:
            sys.modules["world_model"] = previous


def ordinary_outputs(case):
    """Execute a fixture without instrumentation to validate its expected behavior."""
    with tempfile.TemporaryDirectory(prefix="planning-benchmark-plain-") as directory:
        path = _write_fixture(directory, case)
        return _ordinary(path, case.calls)


def _write_fixture(directory, case):
    path = Path(directory) / "approach.py"
    path.write_text(case.source, encoding="utf-8")
    (path.parent / "world_model.py").write_text(WORLD_MODEL, encoding="utf-8")
    return path


def classify(expected, observed):
    """Unknown is an abstention, never a negative prediction or a passing result."""
    if observed is None:
        return "abstention"
    if expected:
        return "true_positive" if observed else "false_negative"
    return "false_positive" if observed else "true_negative"


def _field(report, path):
    value = report
    for part in path.split("."):
        try:
            value = value[int(part)] if isinstance(value, list) else value[part]
        except (KeyError, IndexError, TypeError, ValueError):
            return None
    return value


def assess(case, report, *, execution_ok):
    """Evaluate predictions, not implementation-specific event IDs or names."""
    relevant = performed = None
    complete = execution_ok and report is not None and not report.get("incomplete")
    if complete:
        if report["verdict"] == "planning_observed":
            relevant = True
        elif report["verdict"] == "no_planning_observed":
            relevant = False
        if report["planning_events"]:
            performed = True
        elif report["performed_planning_work"] is not None:
            performed = report["performed_planning_work"] > 0
    metrics = []
    for metric in case.metrics:
        observed = _field(report, metric.path) if complete else None
        correct_unit = (
            (
                metric.path != "planning_depth"
                or observed == 0
                or metric.unit in report.get("units", [])
            )
            if complete
            else False
        )
        if (
            complete
            and metric.path.startswith("semantic_profile.")
            and metric.path.endswith(".value")
        ):
            correct_unit = _field(report, metric.path[:-5] + "unit") == metric.unit
        metrics.append(
            {
                **asdict(metric),
                "observed": observed,
                "outcome": (
                    "unmeasured"
                    if observed is None
                    else (
                        "correct"
                        if observed == metric.value and correct_unit
                        else "incorrect"
                    )
                ),
            }
        )
    return {
        "performed": {
            "expected": case.performed,
            "observed": performed,
            "outcome": classify(case.performed, performed),
        },
        "action_relevant": {
            "expected": case.action_relevant,
            "observed": relevant,
            "outcome": classify(case.action_relevant, relevant),
        },
        "metrics": metrics,
    }


def evaluate_case(case, track="automatic", *, max_events=200_000):
    """Trace one scenario and retain both behavior fidelity and semantic errors."""
    missing = [
        name for name in case.requirements if importlib.util.find_spec(name) is None
    ]
    record = {
        "id": case.id,
        "track": track,
        "description": case.description,
        "categories": list(case.categories),
        "evidence": list(case.evidence),
        "notes": case.notes,
        "calls": [asdict(call) for call in case.calls],
        "source_sha256": hashlib.sha256(case.source.encode()).hexdigest(),
        "equivalence_group": case.equivalence_group,
        "expected_returns": list(case.returns),
        "requirements_missing": missing,
        "reference_measurements_used": False,
    }
    report = None
    error = None
    ordinary = actual = None
    if not missing:
        with tempfile.TemporaryDirectory(prefix="planning-benchmark-") as directory:
            path = _write_fixture(directory, case)
            try:
                ordinary = _ordinary(path, case.calls)
            except Exception as exc:  # pylint: disable=broad-exception-caught
                error = f"Ordinary execution: {type(exc).__name__}: {exc}"
            if error is None:
                session = RuntimeSession(path, track_config(track, max_events))
                actual = []
                try:
                    with session:
                        session.load()
                        for call in case.calls:
                            actual.append(
                                copy.deepcopy(
                                    session.call(
                                        call.method,
                                        *copy.deepcopy(call.args),
                                        state_args=call.state_args,
                                        action=call.action,
                                    )
                                )
                            )
                except Exception as exc:  # pylint: disable=broad-exception-caught
                    error = f"Traced execution: {type(exc).__name__}: {exc}"
                report = session.report()
                if session.semantic_adapter is not None:
                    raise AssertionError(
                        "Policy-specific references cannot enter the benchmark"
                    )
    behavior_ok = (
        ordinary == list(case.returns)
        and actual == ordinary
        and error is None
        and not missing
    )
    checks = assess(case, report, execution_ok=behavior_ok)
    passed = (
        behavior_ok
        and all(
            checks[key]["outcome"] in ("true_positive", "true_negative")
            for key in ("performed", "action_relevant")
        )
        and all(m["outcome"] == "correct" for m in checks["metrics"])
    )
    record.update(
        ordinary_returns=ordinary,
        traced_returns=actual,
        behavior_preserved=bool(behavior_ok),
        error=error,
        checks=checks,
        requirements_satisfied=not missing,
        meets_expectations=bool(passed),
        runtime=(
            None
            if report is None
            else {
                key: report[key]
                for key in (
                    "version",
                    "verdict",
                    "status",
                    "planning_depth",
                    "planning_work",
                    "performed_planning_work",
                    "event_count",
                    "incomplete",
                    "config",
                    "units",
                    "semantic_profile",
                )
            }
        ),
        unknown_reasons=(
            sorted({u["reason"] for u in report["unknowns"]}) if report else []
        ),
    )
    return record


def _summary(records):
    out = {
        "cases": len(records),
        "behavior_preserved": sum(r["behavior_preserved"] for r in records),
        "meets_expectations": sum(r["meets_expectations"] for r in records),
        "both_labels_correct": sum(
            r["behavior_preserved"]
            and all(
                r["checks"][role]["outcome"] in ("true_positive", "true_negative")
                for role in ("performed", "action_relevant")
            )
            for r in records
        ),
        "missing_dependencies": sum(bool(r["requirements_missing"]) for r in records),
        "execution_errors": sum(r["error"] is not None for r in records),
    }
    for key in ("performed", "action_relevant"):
        counts = Counter(r["checks"][key]["outcome"] for r in records)
        out[key] = {
            name: counts[name]
            for name in (
                "true_positive",
                "true_negative",
                "false_positive",
                "false_negative",
                "abstention",
            )
        }
    counts = Counter(m["outcome"] for r in records for m in r["checks"]["metrics"])
    out["metrics"] = {
        key: counts[key] for key in ("correct", "incorrect", "unmeasured")
    }
    families = defaultdict(Counter)
    for record in records:
        for metric in record["checks"]["metrics"]:
            families[metric["path"]][metric["outcome"]] += 1
    out["metrics_by_field"] = {
        path: {key: counts[key] for key in ("correct", "incorrect", "unmeasured")}
        for path, counts in sorted(families.items())
    }
    return out


def _equivalence(records):
    groups = defaultdict(list)
    for record in records:
        if record["equivalence_group"]:
            groups[(record["track"], record["equivalence_group"])].append(record)
    results = []
    for (track, name), members in groups.items():
        signatures = {
            (
                r["checks"]["performed"]["observed"],
                r["checks"]["action_relevant"]["observed"],
                tuple(m["observed"] for m in r["checks"]["metrics"]),
            )
            for r in members
        }
        results.append(
            {
                "track": track,
                "group": name,
                "cases": [r["id"] for r in members],
                "comparable": len(members) > 1,
                "consistent": len(signatures) == 1 if len(members) > 1 else None,
                "all_correct": all(r["meets_expectations"] for r in members),
            }
        )
    return results


def evaluate(cases=CASES, *, tracks=("automatic",), max_events=200_000):
    """Report all gaps; the benchmark does not train or patch the recognizer."""
    validate_cases(cases)
    if max_events <= 0 or not tracks or set(tracks) - set(TRACKS):
        raise ValueError("Choose valid tracks and a positive event limit")
    records = [
        evaluate_case(case, track, max_events=max_events)
        for track in tracks
        for case in cases
    ]
    runtime_root = Path(__file__).resolve().parent.parent / "runtime"
    return {
        "version": VERSION,
        "split": "development",
        "scope": (
            "Observed fixture executions; " "labels are not supplied to the recognizer"
        ),
        "shared_api_sha256": hashlib.sha256(WORLD_MODEL.encode()).hexdigest(),
        "runtime_source_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(runtime_root.glob("*.py"))
            if not path.name.startswith("test_")
        },
        "shared_contracts": {
            name: asdict(contract) for name, contract in SHARED_CONTRACTS.items()
        },
        "shared_assessment_contracts": {
            name: asdict(contract) for name, contract in SHARED_ASSESSMENTS.items()
        },
        "summary": _summary(records),
        "by_track": {
            track: _summary([r for r in records if r["track"] == track])
            for track in tracks
        },
        "by_track_and_category": {
            track: {
                category: _summary(
                    [
                        r
                        for r in records
                        if r["track"] == track and category in r["categories"]
                    ]
                )
                for category in sorted({c for r in records for c in r["categories"]})
            }
            for track in tracks
        },
        "equivalence_groups": _equivalence(records),
        "results": records,
    }
