"""`--suite policy`: the analyzer on class-based policies with state across calls."""

import argparse
import json
from pathlib import Path

from .policy_discovery import (
    PolicyLimits,
    discover_policy,
    load_policy_bank,
    validate_policy,
)
from .policy_domains import DEVELOPMENT, VALIDATION, DiscWorld, KinderDomain
from .policy_fixtures import GROUND_TRUTH, KINDER_POLICY, POLICY_FIXTURES, kinder_source
from .policy_report import (
    at_least,
    finding_text,
    rate_text,
    save_policy_report,
    save_unresolved,
    searches_text,
    share_range,
    spread_text,
    write_json,
)
from .policy_runner import PolicyProgram, UnsupportedProgram

FAILURES = (
    UnsupportedProgram,
    ValueError,
    RuntimeError,
    AssertionError,
    SyntaxError,
    KeyError,
    TypeError,
    IndexError,
    NameError,
    ArithmeticError,
)


def policy_sources(args: argparse.Namespace) -> dict[str, tuple[str, str]]:
    """Name -> (source, domain kind); KinDER for the real and custom policies."""
    if args.source:
        return {args.source.stem: (args.source.read_text(encoding="utf-8"), "kinder")}
    every = {name: (source, "disc") for name, source in POLICY_FIXTURES.items()}
    every[KINDER_POLICY] = (kinder_source(), "kinder")
    return every if args.fixture == "all" else {args.fixture: every[args.fixture]}


def policy_limits(args: argparse.Namespace) -> PolicyLimits:
    """Suite defaults unless a flag overrides them."""
    defaults = PolicyLimits()
    return PolicyLimits(
        candidates=args.max_candidates or defaults.candidates,
        bindings=args.max_bindings,
        mapping_depth=args.mapping_depth,
        selectors=args.max_selectors or defaults.selectors,
        edits_per_run=args.edits_per_run,
        probed_runs=args.probed_runs,
    )


def _bounded(row: dict, key: str, mean: bool = True, partial: bool = False):
    """A summary value, or "≥" its lower bound when the value is withheld."""
    value = row.get(f"mean_{key}" if mean else key)
    return at_least(value, row.get(f"lower_bound_{key}"), partial)


def run_policy_suite(args: argparse.Namespace) -> int:
    """Discover, persist each bank, validate, and write one report per policy."""
    limits = policy_limits(args)
    config = (
        json.loads(args.env_config.read_text(encoding="utf-8"))
        if args.env_config
        else None
    )
    kinder = None
    summaries, failed = [], False
    for name, (source, kind) in policy_sources(args).items():
        directory = args.output_dir / name
        try:
            if kind == "kinder":
                kinder = kinder or KinderDomain(config)
            domain = kinder if kind == "kinder" else DiscWorld()
            program = PolicyProgram(source)
            bank = (
                load_policy_bank(args.frozen)
                if args.frozen
                else discover_policy(program, domain, DEVELOPMENT, VALIDATION, limits)
            )
            # Persist the bank BEFORE any validation episode is executed.
            bank.save(directory / "frozen.json")
            validation = validate_policy(program, domain, bank)
            summary = save_policy_report(
                directory,
                name,
                program,
                bank,
                validation,
                None if args.source else GROUND_TRUTH[name],
            )
        except FAILURES as exc:
            summary = save_unresolved(directory, name, source, exc)
            failed = True
        summaries.append(summary)
        rate = rate_text(
            summary.get("mean_planning_rate"),
            summary.get("lower_bound_planning_rate"),
        )
        score = at_least(
            summary.get("mean_prev_planning_score"),
            summary.get("lower_bound_prev_planning_score"),
        )
        print(
            f'{name}: {finding_text(summary["finding"])}; '
            f"planning rate={rate}, "
            "squares per searching decision (median; mean)="
            f'{spread_text(summary.get("squares_per_decision"), extremes=False)}, '
            f"prev_planning_score={score}, "
            "followed-plan share="
            f'{summary.get("mean_followed_plan_share")}'
            f' (max {summary.get("mean_followed_plan_share_max")})'
        )
    write_summaries(args.output_dir, summaries)
    return 1 if failed else 0


def write_summaries(output_dir: Path, summaries: list[dict]) -> None:
    """summary.json and summary.md for every analyzed policy."""
    write_json(output_dir / "summary.json", summaries)
    rows = [
        "# Search explanations of stateful policies",
        "",
        "A decision is one policy call. A searching decision has at least one search "
        "that got beyond its start square; a stuck search never left it. Planning "
        "rate (searching decisions / calls), stuck searches and prev_planning_score "
        "are means over each policy's frozen validation episodes; per-decision values "
        "pool every searching decision. Squares are each policy's own grid cells; "
        "floor (m²) compares policies. prev_planning_score is the method's per-call "
        "score, planning rate x mean squares per searching decision. The "
        "followed-plan share is the fraction of action calls whose command followed "
        "a cached plan with a complete search-to-action witness; its max adds calls "
        "whose plan evidence is unresolved.",
        "",
        "| Policy | Known fixture label | Finding | Solved | Planning rate | "
        "Stuck searches (per episode) | "
        "Squares per searching decision: median; mean (min–max) | "
        "Floor per searching decision (m²): median; mean | "
        "Searches per searching decision: mean (max) | "
        "prev_planning_score (derived) | Search-guided actions |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in summaries:
        cells = [
            f'[{row["fixture"]}]({row["fixture"]}/report.html)',
            row.get("fixture_ground_truth"),
            finding_text(row["finding"]),
            row.get("solved"),
            rate_text(
                row.get("mean_planning_rate"), row.get("lower_bound_planning_rate")
            ),
            row.get("mean_stuck_searches"),
            spread_text(row.get("squares_per_decision")),
            spread_text(row.get("floor_per_decision"), 2, False),
            searches_text(row.get("searches_per_decision")),
            _bounded(row, "prev_planning_score"),
            share_range(
                row.get("mean_followed_plan_share"),
                row.get("mean_followed_plan_share_max"),
            ),
        ]
        rows.append(
            "| " + " | ".join("—" if c is None else str(c) for c in cells) + " |"
        )
    rows += [
        "",
        "≥ marks a lower bound. For effort, the total counts only runs the analyzer "
        "could read; the other runs are unknown (never zero) and can only add to it. "
        "For attributed effort, it also marks runs with no complete action witness, "
        "which is not zero planning. — marks a value with no bound. "
        "A share range's max counts plans "
        "whose search provenance is unresolved; it is the most the evidence allows, "
        "not an estimate. Cross-call credit requires a search "
        "edit to predict the stored plan and later action, with mediation controls.",
    ]
    (output_dir / "summary.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f'Reports: {output_dir.resolve() / "summary.md"}')


def add_policy_arguments(parser: argparse.ArgumentParser) -> None:
    """Flags used only by the policy suite."""
    parser.add_argument(
        "--env-config",
        type=Path,
        help="KinDER env config JSON for --suite policy --source (default: the "
        "stored ClutteredRetrieval2D config)",
    )
    parser.add_argument(
        "--edits-per-run",
        type=int,
        default=5,
        help="Policy suite: paired edits per run",
    )
    parser.add_argument(
        "--probed-runs",
        type=int,
        default=8,
        help="Policy suite: runs probed per part per episode",
    )
