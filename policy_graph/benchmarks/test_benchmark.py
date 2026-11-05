"""Validate benchmark labels and measurement plumbing, not known semantic errors."""

# Test names describe the assertion; ordinary source fixtures are intentional.
# pylint: disable=missing-function-docstring

import json
import sys
from dataclasses import replace

import pytest

from policy_graph.benchmarks.__main__ import main
from policy_graph.benchmarks.cases import CASES, CATEGORIES, validate_cases
from policy_graph.benchmarks.evaluate import (
    assess,
    classify,
    evaluate,
    evaluate_case,
    ordinary_outputs,
    track_config,
)

BY_ID = {case.id: case for case in CASES}


def test_labels_cover_categories_and_equivalence_groups():
    validate_cases()
    assert {tag for case in CASES for tag in case.categories} == set(CATEGORIES)
    for group in {case.equivalence_group for case in CASES} - {None}:
        members = [case for case in CASES if case.equivalence_group == group]
        assert len(members) > 1
        gold = members[0]
        for case in members:
            assert (case.performed, case.action_relevant, case.metrics) == (
                gold.performed,
                gold.action_relevant,
                gold.metrics,
            )
            assert case.returns == gold.returns
    # Explicitly agreed boundary cases must stay positive in the benchmark.
    assert BY_ID["one_step_min"].performed
    assert BY_ID["single_route_validation"].performed


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.id)
def test_ordinary_fixture_matches_authored_outputs(case):
    for requirement in case.requirements:
        pytest.importorskip(requirement)
    assert ordinary_outputs(case) == list(case.returns)


def test_duplicate_ids_and_unexplained_positive_labels_are_rejected():
    with pytest.raises(ValueError, match="Duplicate"):
        validate_cases((CASES[0], CASES[0]))
    with pytest.raises(ValueError, match="Missing planning semantics"):
        validate_cases((replace(CASES[0], performed=True),))


@pytest.mark.parametrize("expected", (False, True))
def test_unknown_is_never_a_negative_or_a_pass(expected):
    assert classify(expected, None) == "abstention"
    case = replace(CASES[0], performed=expected, action_relevant=expected)
    checks = assess(case, None, execution_ok=False)
    assert checks["performed"]["outcome"] == "abstention"
    assert checks["action_relevant"]["outcome"] == "abstention"


def test_partial_trace_does_not_turn_prefix_into_complete_metrics():
    checks = assess(
        BY_ID["one_step_min"], {"incomplete": "trace limit"}, execution_ok=True
    )
    assert checks["action_relevant"]["observed"] is None
    assert all(metric["outcome"] == "unmeasured" for metric in checks["metrics"])


def test_equal_numbers_with_incompatible_depth_units_are_wrong():
    report = {
        "verdict": "planning_observed",
        "planning_events": [1],
        "planning_depth": 1,
        "planning_work": 3,
        "units": ["seconds"],
    }
    checks = assess(BY_ID["one_step_min"], report, execution_ok=True)
    assert checks["metrics"][0]["outcome"] == "incorrect"
    assert checks["metrics"][1]["outcome"] == "correct"


def test_shared_contract_is_global_and_not_keyed_to_cases():
    assert not track_config("automatic", 1000).transition_models
    assert set(track_config("shared_contracts", 1000).transition_models) == {
        "world_model.step"
    }
    with pytest.raises(ValueError, match="Unknown track"):
        track_config("reference", 1000)


def test_supported_measurements_and_cached_work_match_independent_labels():
    for identifier, track in (
        ("one_step_min", "automatic"),
        ("shared_model_rollout", "shared_contracts"),
        ("cached_plan", "automatic"),
        ("discarded_search", "automatic"),
        ("shared_single_route", "shared_contracts"),
        ("shared_failed_routes", "shared_contracts"),
        ("shared_placement", "shared_contracts"),
        ("shared_unused_check", "shared_contracts"),
    ):
        previous = sys.modules.get("world_model")
        result = evaluate_case(BY_ID[identifier], track)
        assert result["meets_expectations"], result
        assert not result["reference_measurements_used"]
        assert sys.modules.get("world_model") is previous


def test_missing_dependency_remains_a_gap_in_denominator():
    case = replace(CASES[0], requirements=("_missing_planning_benchmark_dependency_",))
    result = evaluate((case,))
    assert result["summary"]["cases"] == 1
    assert result["summary"]["missing_dependencies"] == 1
    assert result["summary"]["meets_expectations"] == 0
    assert result["summary"]["action_relevant"]["abstention"] == 1


def test_behavior_mismatch_invalidates_semantic_claims():
    case = replace(BY_ID["one_step_min"], returns=(999,))
    result = evaluate_case(case)
    assert not result["behavior_preserved"]
    assert not result["meets_expectations"]
    assert result["checks"]["action_relevant"]["outcome"] == "abstention"


def test_failed_execution_is_visible_and_does_not_drop_case():
    case = replace(
        CASES[0],
        source="def get_action(obs):\n    raise ValueError('fixture failure')\n",
    )
    result = evaluate((case,))
    assert result["summary"]["execution_errors"] == 1
    assert result["results"][0]["error"].startswith("Ordinary execution: ValueError")
    assert result["summary"]["cases"] == 1


@pytest.mark.parametrize("strict", (False, True))
def test_cli_records_trace_limit_and_strict_mode_returns_failure(
    tmp_path, monkeypatch, strict
):
    output = tmp_path / "results.json"
    argv = [
        "benchmark",
        "--case",
        "one_step_min",
        "--max-events",
        "1",
        "--json",
        str(output),
    ]
    if strict:
        argv.append("--strict")
    monkeypatch.setattr(sys, "argv", argv)
    if strict:
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 1
    else:
        main()
    result = json.loads(output.read_text(encoding="utf-8"))
    assert result["summary"]["execution_errors"] == 1
    assert result["summary"]["action_relevant"]["abstention"] == 1
    assert result["summary"]["meets_expectations"] == 0
