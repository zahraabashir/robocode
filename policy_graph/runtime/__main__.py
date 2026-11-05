"""Trace a RoboCode policy in its environment, or run a manual test scenario.

python -m policy_graph.runtime approach.py --env small_maze --seed 0
"""

import argparse
import hashlib
import json
from pathlib import Path

from .config import RuntimeConfig
from .episode_config import load_episode_spec
from .runner import RuntimeSession


def _positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return number


def _run_scenario(session, path):
    scenario_text = path.read_text(encoding="utf-8")
    scenario = json.loads(scenario_text)
    session.metadata.update(
        {
            "mode": "scenario",
            "scenario": str(path.resolve()),
            "scenario_sha256": hashlib.sha256(scenario_text.encode()).hexdigest(),
        }
    )
    with session:
        session.load(
            class_name=scenario.get("class_name"),
            constructor_args=scenario.get("constructor_args", ()),
            constructor_kwargs=scenario.get("constructor_kwargs", {}),
        )
        for call in scenario.get("calls", []):
            session.call(
                call.get("method", "get_action"),
                *call.get("args", []),
                state_args=call.get("state_args", (0,)),
                action=call.get("action"),
                **call.get("kwargs", {}),
            )


def main():
    """Run an episode or explicit scenario and persist its evidence."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--scenario", type=Path, help="Optional manual call sequence as JSON"
    )
    mode.add_argument(
        "--env", help="RoboCode environment name, e.g. small_maze or motion2d_easy"
    )
    mode.add_argument(
        "--run-config",
        type=Path,
        help=(
            "Saved run config.yaml (otherwise discover nearby "
            ".hydra/config.yaml or evidence/config.yaml)"
        ),
    )
    parser.add_argument("--seed", type=int, help="Episode reset seed (default: 0)")
    parser.add_argument(
        "--max-steps",
        type=_positive,
        help="Episode step limit (saved run value or 1000)",
    )
    parser.add_argument(
        "--object-count",
        type=_positive,
        help="Pin the count for a variable-count environment",
    )
    parser.add_argument(
        "--primitives",
        nargs="*",
        help="Primitive names (saved run list or none); an empty list disables them",
    )
    parser.add_argument(
        "--config", type=Path, help="RuntimeConfig and model contracts as JSON"
    )
    parser.add_argument("--json", type=Path, help="Write a machine-readable report")
    parser.add_argument(
        "--dot", type=Path, help="Write the union of action dependency slices"
    )
    parser.add_argument("--include-graph", action="store_true")
    args = parser.parse_args()
    if args.scenario and any(
        value is not None
        for value in (args.seed, args.max_steps, args.object_count, args.primitives)
    ):
        parser.error(
            "--seed, --max-steps, --object-count and --primitives are episode options; "
            "omit --scenario"
        )
    if args.seed is not None and args.seed < 0:
        parser.error("--seed must be non-negative")
    config = (
        RuntimeConfig.from_dict(json.loads(args.config.read_text()))
        if args.config
        else RuntimeConfig()
    )
    session = RuntimeSession(args.path, config)
    error = None
    try:
        if args.scenario:
            _run_scenario(session, args.scenario)
        else:
            spec = load_episode_spec(
                args.path,
                env=args.env,
                run_config=args.run_config,
                max_steps=args.max_steps,
                primitives=args.primitives,
            )
            session.metadata.update(spec.metadata)
            env = spec.make_env()
            try:
                session.run_episode(
                    env,
                    seed=args.seed if args.seed is not None else 0,
                    max_steps=spec.max_steps,
                    count=args.object_count,
                    primitives=spec.make_primitives(env),
                )
            finally:
                env.close()
    except Exception as exc:  # pylint: disable=broad-exception-caught
        # Persist incomplete evidence for review, then fail.
        error = f"{type(exc).__name__}: {exc}"
        session.recorder.graph.incomplete = error
    result = session.report(include_graph=args.include_graph)
    if args.json:
        args.json.write_text(json.dumps(result, indent=2) + "\n")
    if args.dot:
        args.dot.write_text(session.recorder.graph.to_dot(session.recorder.actions))
    print(f"{result['verdict']} ({result['status']})")
    geometric = result.get("geometric_planning")
    if geometric:
        measured = geometric["performed"]
        totals = geometric["all_collision_and_search_counts"]
        print("model-transition depth/work: not measured by geometric adapter")
        print(
            f"path searches: {measured['path_searches']}; "
            f"candidate paths scored: {totals['candidate_paths_scored']}; "
            f"candidate paths checked: {totals['candidate_paths_checked']}"
        )
        print(
            "longest selected route: "
            f"{measured['max_selected_path_horizon']} estimated movement actions; "
            "max candidate-path horizon: "
            f"{measured['max_candidate_path_horizon']} estimated movement steps"
        )
        print(f"collision sample rows: {totals['collision_sample_rows']}")
        if geometric["counts_are_prefix_only"]:
            print(
                "incomplete trace: geometric measurements cover the recorded prefix only"
            )
    else:
        print(
            f"planning depth: {result['planning_depth']}; "
            f"planning work: {result['planning_work']}"
        )
    print(
        f"{len(result['actions'])} actions; "
        f"{result['planning_event_count']} action-relevant planning events"
    )
    if error:
        parser.exit(1, error + "\n")


if __name__ == "__main__":
    # The recorder protocol handles arbitrary Python values and is dynamically typed.
    main()  # type: ignore[no-untyped-call]
