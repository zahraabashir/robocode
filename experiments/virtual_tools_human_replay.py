"""Replay the recorded human placements through VirtualToolsEnv; compare outcomes.

A fidelity check of the Virtual Tools environment: every placement human participants
made (``third-party/tool-games/data/*/humans``) is replayed as one step from the
level's initial scene, and the env's outcome (accepted? success?) is compared with
the recorded one. Humans could only make placements the game accepted, so a human
placement the env rejects is a disagreement too. The human data is used only here,
never by agents.

Level names in the data differ from the level files in five places: four Validation
levels are renamed, and ``Original/Launch_A.json`` and ``Launch_B.json`` carry each
other's names. ``DATA_TO_LEVEL`` maps them. Three data levels (FridgeMagnet, Towers_A,
Towers_B) have no level file and are skipped.

Usage::

    python experiments/virtual_tools_human_replay.py [--max-per-level N] [--workers 8]
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import random
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any

import numpy as np

from robocode.environments.tool_games import TOOL_GAMES_ROOT
from robocode.environments.virtual_tools_env import VirtualToolsEnv

_DATA = TOOL_GAMES_ROOT / "data"
_HUMAN_FILES = {
    "Original": _DATA / "original_levels" / "humans" / "FullGameSuccessData.csv",
    "Validation": _DATA / "cv_levels" / "humans" / "FullGameSuccessDataCV.csv",
}
_RENAMED = {
    "Launch_A": "Launch_B",
    "Launch_B": "Launch_A",
    "BasicAlt": "Basic_v2",
    "FallingAlt": "Falling_v2",
    "TableAlt": "Table_v2",
    "DoubleLaunch": "Launch_v2",
}
_ENVS: dict[str, VirtualToolsEnv] = {}


def level_for(folder: str, trial: str) -> str:
    """The level file name (``Folder/Name``) for a level name in the human data."""
    return f"{folder}/{_RENAMED.get(trial, trial)}"


def _replay(task: tuple[str, int, float, float]) -> tuple[bool, bool]:
    """(accepted, success) of one placement from the level's initial scene."""
    level, tool, x, y = task
    if level not in _ENVS:
        _ENVS[level] = VirtualToolsEnv(levels=[level])
    env = _ENVS[level]
    env.reset(seed=0, options={"object_count": 0})
    _, _, _, _, info = env.step(np.array([tool, x, y], dtype=np.float64))
    return bool(info["accepted"]), bool(info["success"])


def _load_tasks(max_per_level: int | None, seed: int) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    rows_by_level: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for folder, path in _HUMAN_FILES.items():
        for row in csv.DictReader(path.open(encoding="utf-8")):
            level = level_for(folder, row["Trial"])
            level_file = TOOL_GAMES_ROOT / "environment" / "Trials" / f"{level}.json"
            if not level_file.is_file():
                continue
            tool_names = json.loads(level_file.read_text(encoding="utf-8"))["toolNames"]
            rows_by_level[level].append(
                {
                    "level": level,
                    "tool": tool_names.index(row["Tool"]),
                    "x": float(row["PosX"]),
                    "y": float(row["PosY"]),
                    "human_success": row["SuccessPlace"] == "True",
                }
            )
    tasks: list[dict[str, Any]] = []
    for level in sorted(rows_by_level):
        rows = rows_by_level[level]
        if max_per_level is not None:
            successes = [r for r in rows if r["human_success"]]
            failures = [r for r in rows if not r["human_success"]]
            rows = rng.sample(successes, min(max_per_level, len(successes)))
            rows += rng.sample(failures, min(max_per_level, len(failures)))
        tasks.extend(rows)
    return tasks


def main() -> None:
    """Replay, then print a per-level agreement table and the totals."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument(
        "--max-per-level",
        type=int,
        default=None,
        help="Sample at most N successes and N failures per level (default: all).",
    )
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--json-out", type=Path, default=None)
    args = parser.parse_args()

    tasks = _load_tasks(args.max_per_level, args.seed)
    with ProcessPoolExecutor(args.workers) as pool:
        outcomes = list(
            pool.map(
                _replay,
                [(t["level"], t["tool"], t["x"], t["y"]) for t in tasks],
                chunksize=16,
            )
        )

    table: dict[str, collections.Counter[str]] = collections.defaultdict(
        collections.Counter
    )
    for task, (accepted, success) in zip(tasks, outcomes):
        human = "human_success" if task["human_success"] else "human_failure"
        if not accepted:
            verdict = "rejected"
        elif success == task["human_success"]:
            verdict = "agree"
        else:
            verdict = "disagree"
        table[task["level"]][f"{human}:{verdict}"] += 1
    totals: collections.Counter[str] = collections.Counter()
    print(
        f"{'level':24s} {'human success: agree/disagree/rejected':>40s}"
        f" {'human failure: agree/disagree/rejected':>40s}"
    )
    for level in sorted(table):
        counts = table[level]
        totals.update(counts)
        cells = [
            "/".join(str(counts[f"{h}:{v}"]) for v in ("agree", "disagree", "rejected"))
            for h in ("human_success", "human_failure")
        ]
        print(f"{level:24s} {cells[0]:>40s} {cells[1]:>40s}")
    agree = totals["human_success:agree"] + totals["human_failure:agree"]
    rejected = totals["human_success:rejected"] + totals["human_failure:rejected"]
    print(
        f"\n{agree}/{len(tasks)} placements agree ({agree / len(tasks):.1%}); "
        f"human successes the env fails: {totals['human_success:disagree']}, "
        f"human failures the env solves: {totals['human_failure:disagree']}, "
        f"rejected: {rejected}"
    )
    if args.json_out is not None:
        args.json_out.write_text(
            json.dumps({"num_placements": len(tasks), "by_level": table}, indent=2),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
