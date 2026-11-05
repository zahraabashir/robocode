"""Rerun the saved 35-policy runtime evaluation under its original protocol.

python -m policy_graph.runtime.corpus --out policy_graph/runtime/results/NAME

Policies, names and saved static labels come from an earlier ``summary.json``.
Each policy runs the ordinary CLI in its own process (seed 0, saved environment
configuration and step limit, environment-default object count, default
contracts) with the given event limit and process timeout, ``--workers`` at a
time. ``--diagnostics`` additionally runs the stage-separated diagnostics
harness, written to ``diagnostics/`` and summarized separately.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PREVIOUS = Path(__file__).resolve().parent / "results/corpus35-seed0-v4/summary.json"


def _run_cli(record, out, timeout, max_events, contracts=None):
    report = out / f"{record['run']}.json"
    command = [
        sys.executable,
        "-m",
        "policy_graph.runtime",
        record["policy"],
        "--seed",
        "0",
        "--json",
        str(report),
    ]
    config = None
    if max_events != 200_000 or contracts:
        # Non-default limits and contracts are an explicit config, never implied.
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, dir=out
        ) as handle:
            json.dump({**(contracts or {}), "max_events": max_events}, handle)
            config = Path(handle.name)
        command += ["--config", str(config)]
    started = time.perf_counter()
    try:
        process = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        timed_out, code, log = (
            False,
            process.returncode,
            process.stdout + process.stderr,
        )
    except subprocess.TimeoutExpired as exc:
        timed_out, code = True, None
        log = (exc.stdout or b"").decode(errors="replace") + (exc.stderr or b"").decode(
            errors="replace"
        )
    elapsed = time.perf_counter() - started
    if config is not None:
        config.unlink(missing_ok=True)
    (out / f"{record['run']}.log").write_text(log)
    data = (
        json.loads(report.read_text()) if report.is_file() and not timed_out else None
    )
    if timed_out:
        report.unlink(missing_ok=True)
    metrics = (data or {}).get("metadata", {}).get("episode_metrics")
    actions = data["actions"] if data else []
    return {
        **{
            k: record[k] for k in ("run", "env", "name", "hand_label", "static_verdict")
        },
        "policy": record["policy"],
        "source_sha256": hashlib.sha256(
            Path(record["policy"]).read_bytes()
        ).hexdigest(),
        "command": command,
        "elapsed_seconds": round(elapsed, 2),
        "exit_code": code,
        "timeout": timed_out,
        "report": str(report) if data else None,
        "completed_episode": bool(data)
        and not data["incomplete"]
        and metrics is not None,
        "verdict": data["verdict"] if data else None,
        "status": data["status"] if data else None,
        "incomplete": data["incomplete"] if data else None,
        "actions": len(actions) if data else None,
        "planning_events": data["planning_event_count"] if data else None,
        "possibly_relevant_planning_events": (
            data.get("possibly_relevant_planning_event_count") if data else None
        ),
        "planning_depth": data["planning_depth"] if data else None,
        "planning_work": data["planning_work"] if data else None,
        "performed_planning_work": data["performed_planning_work"] if data else None,
        "unknown_count": data.get("unknown_count") if data else None,
        "unknown_reasons": (
            dict(list(data.get("unknown_reasons", {}).items())[:5]) if data else None
        ),
        "precision": data.get("precision") if data else None,
        "recognized_rules": (
            sorted(
                {
                    p["recognition"]["rule"]
                    for p in data["planning_events"]
                    if p.get("recognition")
                }
            )
            if data
            else None
        ),
        "recognition_error": (data["recognition_coverage"]["error"] if data else None),
        "event_count": data["event_count"] if data else None,
        "episode_metrics": metrics,
    }


def _run_diagnostics(record, out, budget, max_events):
    target = out / "diagnostics"
    command = [
        sys.executable,
        "-m",
        "policy_graph.runtime.diagnostics",
        record["policy"],
        "--out",
        str(target),
        "--name",
        record["run"],
        "--stage-budget",
        str(budget),
        "--max-events",
        str(max_events),
    ]
    subprocess.run(
        command, cwd=ROOT, capture_output=True, timeout=8 * budget + 120, check=False
    )
    path = target / f"{record['run']}.json"
    return json.loads(path.read_text()) if path.is_file() else None


def classify(row):
    """One outcome per policy; unknowns and failures are never 'no planning'."""
    if row["timeout"]:
        return "timeout"
    incomplete = row["incomplete"] or ""
    if "Trace limit" in incomplete:
        return "event_limit"
    if incomplete:
        return "error"
    if not row["completed_episode"]:
        return "no_report" if row["report"] is None else "error"
    return "completed"


def main():
    """Run the protocol, then write summary.json (and diagnostics if requested)."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--records", type=Path, default=PREVIOUS)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--max-events", type=int, default=200_000)
    parser.add_argument("--diagnostics", action="store_true")
    parser.add_argument("--stage-budget", type=float, default=60.0)
    parser.add_argument("--only", nargs="*", help="Run names to include")
    parser.add_argument(
        "--contracts",
        type=Path,
        help="RuntimeConfig JSON of declared contracts (an explicit assumption track)",
    )
    parser.add_argument(
        "--hash-seed",
        type=int,
        help="PYTHONHASHSEED for every child process (default: not fixed, as in v4)",
    )
    parser.add_argument(
        "--diagnostics-only",
        action="store_true",
        help="Skip the protocol run; write only diagnostics/",
    )
    args = parser.parse_args()
    if args.hash_seed is not None:
        # The static analyzer's set iteration order can change its candidates.
        os.environ["PYTHONHASHSEED"] = str(args.hash_seed)
    records = json.loads(args.records.read_text())["records"]
    contracts = (
        json.loads(args.contracts.read_text(encoding="utf-8"))
        if args.contracts
        else None
    )
    if args.only:
        records = [r for r in records if r["run"] in args.only]
    args.out.mkdir(parents=True, exist_ok=True)
    if args.diagnostics_only:
        args.diagnostics, records_run = True, False
    else:
        records_run = True
    rows = []
    with ThreadPoolExecutor(args.workers) as pool:
        if records_run:
            rows = list(
                pool.map(
                    lambda r: _run_cli(
                        r, args.out, args.timeout, args.max_events, contracts
                    ),
                    records,
                )
            )
    for row in rows:
        row["outcome"] = classify(row)
    versions = {
        json.loads(Path(r["report"]).read_text(encoding="utf-8"))["version"]
        for r in rows
        if r["report"]
    }
    summary = {
        "runtime_version": sorted(versions),
        "protocol": {
            "seed": 0,
            "episode_limit": "saved max_steps",
            "object_count": "environment default sampling",
            "max_events": args.max_events,
            "timeout_seconds": args.timeout,
            "workers": args.workers,
            "python_hash_seed": args.hash_seed,
            "contracts": (
                {"file": str(args.contracts), **contracts}
                if contracts
                else "defaults only"
            ),
        },
        "records": rows,
    }
    if records_run:
        (args.out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    if args.diagnostics:
        with ThreadPoolExecutor(args.workers) as pool:
            diagnostics = list(
                pool.map(
                    lambda r: _run_diagnostics(
                        r, args.out, args.stage_budget, args.max_events
                    ),
                    records,
                )
            )
        (args.out / "diagnostics/summary.json").write_text(
            json.dumps(
                [
                    {"run": r["run"], **(d or {"error": "no diagnostics record"})}
                    for r, d in zip(records, diagnostics)
                ],
                indent=2,
            )
            + "\n"
        )
    counts = {}
    for row in rows:
        counts[row["outcome"]] = counts.get(row["outcome"], 0) + 1
    print(json.dumps(counts))


if __name__ == "__main__":
    main()  # type: ignore[no-untyped-call]
