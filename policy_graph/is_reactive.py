"""One-word answer: planning, reactive, or needs_review.

    python policy_graph/is_reactive.py my_policy.py
    pbpaste | python policy_graph/is_reactive.py      # code from the clipboard

``needs_review`` means no planning was found but something unresolved (a missing
module, an opaque scorer, ...) could change that; it is never printed as "reactive".
The code can be a whole file or a single method: a ``def get_action(self, ...)``
with no class around it is wrapped in one. Add ``--why`` to see the evidence.
"""

import argparse
import ast
import sys
import tempfile
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from policy_graph.depgraph import build_graph  # noqa: E402
from policy_graph.reactivity import EntrypointError, classify, find_decision_function  # noqa: E402


def as_module(src: str) -> str:
    """Wrap top-level methods (functions whose first parameter is ``self``) in a class."""
    src = textwrap.dedent(src)
    tree = ast.parse(src)
    methods = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
               and n.args.args and n.args.args[0].arg == "self"]
    if not methods or any(isinstance(n, ast.ClassDef) for n in tree.body):
        return src
    lines = src.splitlines()
    def text(n):
        start = min([n.lineno, *(d.lineno for d in getattr(n, "decorator_list", []))])
        return "\n".join(lines[start - 1:n.end_lineno])
    top = [text(n) for n in tree.body if n not in methods]  # imports etc. stay at module level
    body = [textwrap.indent(text(n), "    ") for n in methods]
    return "\n".join(top + ["class Policy:"] + body) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file", nargs="?", help="Python file (default: read the code from stdin)")
    parser.add_argument("--decision", help="function that returns the action (default: get_action, act, ...)")
    parser.add_argument("--why", action="store_true", help="also print the evidence")
    args = parser.parse_args()
    src = Path(args.file).read_text() if args.file else sys.stdin.read()
    if args.file and as_module(src) == src:
        g = build_graph([args.file])  # in place, so modules it imports from its folder are found
    else:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "policy.py"
            path.write_text(as_module(src))
            g = build_graph([path])
    try:
        report = classify(g, find_decision_function(g, args.decision))
    except EntrypointError as e:
        sys.exit(f"error: {e}")
    print(report.verdict)
    if args.why:
        print(report.text())


if __name__ == "__main__":
    main()
