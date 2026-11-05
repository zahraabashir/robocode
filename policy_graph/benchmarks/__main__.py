"""Run the planning-definition benchmark independently of implementation tests."""

import argparse
import json
from pathlib import Path

from .cases import CASES
from .evaluate import TRACKS, evaluate


def main():
    """Print semantic errors and abstentions, optionally saving their evidence."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--track", choices=(*TRACKS, "both"), default="automatic")
    parser.add_argument(
        "--case",
        action="append",
        dest="cases",
        help="Case ID; repeat to select several",
    )
    parser.add_argument(
        "--list", action="store_true", help="List cases without executing them"
    )
    parser.add_argument(
        "--json", type=Path, help="Save labels, measurements, and discrepancy details"
    )
    parser.add_argument("--max-events", type=int, default=200_000)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 for any gap, including unknowns or missing dependencies",
    )
    args = parser.parse_args()
    if args.max_events <= 0:
        parser.error("--max-events must be positive")
    requested = set(args.cases or ())
    unknown = requested - {case.id for case in CASES}
    if unknown:
        parser.error(f"Unknown case IDs: {', '.join(sorted(unknown))}")
    cases = [case for case in CASES if not requested or case.id in requested]
    if args.list:
        for case in cases:
            print(f"{case.id}: {case.description}")
        return
    tracks = TRACKS if args.track == "both" else (args.track,)
    result = evaluate(cases, tracks=tracks, max_events=args.max_events)
    if args.json:
        args.json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for track, summary in result["by_track"].items():
        print(
            f"{track}: {summary['meets_expectations']}/{summary['cases']} "
            f"meet all current expectations; "
            f"{summary['behavior_preserved']}/{summary['cases']} "
            f"preserve expected behavior"
        )
        print(
            f"  labels only: {summary['both_labels_correct']}/{summary['cases']} "
            "have both performed and action-relevant labels correct"
        )
        for role in ("performed", "action_relevant"):
            counts = summary[role]
            print(
                f"  {role}: {counts['false_positive']} false positives; "
                f"{counts['false_negative']} false negatives; "
                f"{counts['abstention']} unknown"
            )
    for record in result["results"]:
        if not record["meets_expectations"]:
            checks = record["checks"]
            print(
                f"  GAP {record['track']}/{record['id']}: "
                f"performed={checks['performed']['outcome']}; "
                f"action_relevant={checks['action_relevant']['outcome']}"
            )
            for metric in checks["metrics"]:
                if metric["outcome"] != "correct":
                    print(
                        f"    {metric['path']}: {metric['outcome']}; "
                        f"expected {metric['value']} {metric['unit']}, "
                        f"observed {metric['observed']}"
                    )
            if record["error"]:
                print(f"    {record['error']}")
            if record["requirements_missing"]:
                missing = ", ".join(record["requirements_missing"])
                print(f"    Missing dependencies: {missing}")
    if (
        args.strict
        and result["summary"]["meets_expectations"] != result["summary"]["cases"]
    ):
        parser.exit(1)


if __name__ == "__main__":
    main()  # type: ignore[no-untyped-call]
