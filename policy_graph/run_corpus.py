"""Re-classify the final policy of every run listed in all_runs_verdicts.json and rewrite it.

    python -m policy_graph.run_corpus [--out all_runs_verdicts.json]

Each run's ``evidence/final/approach.py`` is analysed (with the modules it imports).
The run list and hand labels are kept; verdict, status, evidence and scores are replaced.
Hand labels are copied as annotations, never used to compute labels or scores.
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from policy_graph.reactivity import analyze  # noqa: E402

RUNS = HERE.parent / "agent_runs" / "environments"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=HERE / "all_runs_verdicts.json")
    args = parser.parse_args()
    runs = json.loads((HERE / "all_runs_verdicts.json").read_text())
    out = []
    for r in runs:
        path = RUNS / r["env"] / "runs" / r["run"] / "evidence" / "final" / "approach.py"
        rep = analyze([path])
        out.append({"run": r["run"], "env": r["env"], "name": r["name"], "hand_label": r["hand_label"],
                    "verdict": rep.verdict, "label": rep.label, "status": rep.status,
                    "planning_depth": rep.planning_depth, "planning_work": rep.planning_work,
                    "scores": rep.scores.to_dict(),
                    "evidence": [f"[{e.kind}] {e}" for e in rep.evidence],
                    "review_reasons": [str(i) for i in rep.review_reasons]})
        depth = rep.planning_depth if rep.planning_depth is not None else "unknown"
        work = rep.planning_work if rep.planning_work is not None else "unknown"
        print(f"{r['env']:14s} {r['name']:12s} {r['hand_label'][:24]:24s} {rep.verdict}  depth={depth} work={work}")
    args.out.write_text(json.dumps(out, indent=1) + "\n")
    print(dict(Counter(o["verdict"] for o in out)), f"-> {args.out}")


if __name__ == "__main__":
    main()
