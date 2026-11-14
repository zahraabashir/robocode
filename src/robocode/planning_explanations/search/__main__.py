"""Run the search-explanations analyzer on class-based policies (KinDER)."""

import argparse
from pathlib import Path

from .policy_cli import add_policy_arguments, run_policy_suite
from .policy_fixtures import KINDER_POLICY, POLICY_FIXTURES
from .policy_runner import UnsupportedProgram


def main(argv=None) -> int:
    """Discover, persist the bank, then validate and export inspectable evidence."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", choices=("policy",), default="policy")
    sources = parser.add_mutually_exclusive_group()
    sources.add_argument(
        "--fixture",
        choices=("all", *sorted(set(POLICY_FIXTURES) | {KINDER_POLICY})),
        default="all",
    )
    sources.add_argument(
        "--source",
        type=Path,
        help="Trusted Python policy: a file defining a GeneratedApproach class",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/search-policy-benchmark"),
    )
    parser.add_argument("--max-candidates", type=int, help="Default: 6000")
    parser.add_argument("--max-bindings", type=int, default=64)
    parser.add_argument("--mapping-depth", type=int, default=2)
    parser.add_argument(
        "--max-selectors",
        type=int,
        help="Value paths inventoried per checkpoint. Default: 1024",
    )
    parser.add_argument(
        "--frozen", type=Path, help="Validate an existing bank; skip discovery"
    )
    add_policy_arguments(parser)
    args = parser.parse_args(argv)
    if args.frozen and not args.source and args.fixture == "all":
        parser.error("--frozen requires --source or a single --fixture")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    return run_policy_suite(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (UnsupportedProgram, ValueError, RuntimeError, AssertionError) as error:
        raise SystemExit(
            f"Unresolved experiment: {error}. No planning score assigned."
        ) from error
