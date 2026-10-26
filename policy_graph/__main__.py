"""Command line: dependency graph and planning-or-reactive verdict for Python policies.

    python policy_graph path/to/approach.py [more files or dirs]
        [--decision get_action] [--config config.json] [--dot slice.dot] [--json report.json]

Modules that the given files import (absolute or relative) are analysed too. The
verdict is ``planning``, ``reactive`` (non-planning), or ``needs_review`` (reactive
label, but something unresolved could change it); see reactivity.py.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from policy_graph.depgraph import build_graph  # noqa: E402
from policy_graph.reactivity import EntrypointError, PolicyConfig, classify, discover_entrypoint  # noqa: E402


def main() -> None:
    """Print the verdict; optionally write the action slice as DOT and the report as JSON."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", help="Python files or directories")
    parser.add_argument("--decision", help="function/method that returns the action (default: auto)")
    parser.add_argument("--config", type=Path, help="PolicyConfig as JSON (state, planners, transition models, ...)")
    parser.add_argument("--dot", type=Path, help="write the action's backward slice as Graphviz DOT")
    parser.add_argument("--json", type=Path, help="write the report as JSON")
    args = parser.parse_args()

    config = PolicyConfig.from_json(args.config) if args.config else PolicyConfig()
    g = build_graph(args.paths, libraries=config.libraries)
    try:
        decision, _ = discover_entrypoint(g, args.decision or config.decision)
    except EntrypointError as e:
        sys.exit(f"error: {e}")
    report = classify(g, decision, config)
    print(g.summary())
    print(report.text())
    if args.dot:
        sink = g.functions[decision].return_node
        args.dot.write_text(g.to_dot(g.backward_slice([sink]) | {sink}))
        print(f"wrote {args.dot}")
    if args.json:
        args.json.write_text(json.dumps(report.to_dict(), indent=2, default=str))
        print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
