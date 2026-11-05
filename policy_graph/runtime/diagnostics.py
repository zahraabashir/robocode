"""Stage-separated timing, memory and ordinary/traced behavior parity for one policy.

python -m policy_graph.runtime.diagnostics approach.py --out DIR

Two child processes run with identical settings (saved configuration, seed,
step limit, object count and primitives):

1. ``ordinary``: the unmodified policy under RoboCode's episode driver;
2. ``traced``: static recognition and instrumentation compile, then the
   instrumented episode and graph recording, then report generation (backward
   slicing, recognition matching and scoring) and JSON serialization.

Each stage has its own wall-clock budget, so an overrun is attributed to the
stage that caused it. Per-step action and observation fingerprints are compared.
For time-dependent policies tracing overhead can legitimately change behavior;
the source is checked for clock use and the result is reported, not hidden.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pickle
import re
import resource
import signal
import subprocess
import sys
import time
from pathlib import Path

CLOCK = re.compile(
    r"\b(import time|from time import|time\.(time|perf_counter|monotonic|process_time)"
    r"|datetime\.now|perf_counter\(|monotonic\()"
)


_clock = time.perf_counter  # Stage timing always uses the real clock.


def virtual_clock(step=1e-3):
    """Diagnostic only: identical deterministic clocks in both processes.

    Each call advances by ``step`` seconds, so wall-clock budgets depend on the
    number of clock reads, not on tracing overhead. Policies are not modified.
    """
    state = [0.0]

    def now():
        state[0] += step
        return state[0]

    for name in ("time", "perf_counter", "monotonic"):
        setattr(time, name, now)


class StageBudget(BaseException):
    """Raised by SIGALRM; a BaseException so policy ``except Exception`` ignores it."""


def _alarm(_signum, _frame):
    raise StageBudget()


def _rss_mb():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return round(peak / (1e6 if sys.platform == "darwin" else 1e3), 1)


def fingerprint(value):
    """Order- and dtype-sensitive digest of an action/observation, or None."""
    try:
        import numpy as np  # pylint: disable=import-outside-toplevel

        if isinstance(value, np.ndarray):
            payload = (
                str(value.dtype).encode()
                + str(value.shape).encode()
                + np.ascontiguousarray(value).tobytes()
            )
        else:
            payload = pickle.dumps(value, protocol=4)
    except Exception:  # pylint: disable=broad-exception-caught
        try:
            payload = repr(value).encode()
        except Exception:  # pylint: disable=broad-exception-caught
            return None
    return hashlib.sha256(payload).hexdigest()[:16]


CONSUMED = ("opaque", "transition", "choice", "assessment", "structural-candidate")


def attribute_events(path, recognition, graph):
    """Events per function, and how many could be summarized without losing
    anything the analysis uses.

    A function is *candidate-free* when no static candidate site (any role of a
    kept recognition candidate, or a choice call) lies in it or in a function it
    can call. Its events are *removable* only if they also include no event kind
    the analysis consumes (unknowns, transitions, choices, assessments, search
    markers). This bounds what summarizing helper calls could save.
    """
    # pylint: disable=import-outside-toplevel
    from policy_graph.depgraph import build_graph

    static = build_graph([str(path)])
    sites = {(f, line) for e in recognition.evidence for _, f, line in e.sites}
    sites |= {(f, line) for f, line, _ in recognition.choice_calls}
    spans = {
        q: (fn.file, fn.node.lineno, getattr(fn.node, "end_lineno", fn.node.lineno))
        for q, fn in static.functions.items()
    }

    def has_site(q):
        file, start, end = spans[q]
        return any(f == file and start <= line <= end for f, line in sites)

    free = {
        q: not any(has_site(c) for c in static.reachable_functions(q) if c in spans)
        for q in spans
    }
    counts = collections.defaultdict(collections.Counter)
    for event in graph.events:
        counts[(event.site.file, event.site.function)][
            "consumed" if event.kind in CONSUMED else "plain"
        ] += 1
    rows = []
    for (file, scope), c in counts.items():
        names = [
            q
            for q, span in spans.items()
            if span[0] == file and (q == scope or q.endswith("." + scope))
        ]
        rows.append(
            {
                "function": scope,
                "file": Path(file).name,
                "events": c["plain"] + c["consumed"],
                "consumed_events": c["consumed"],
                "candidate_free": bool(names) and free[min(names, key=len)],
            }
        )
    rows.sort(key=lambda r: -r["events"])
    total = sum(r["events"] for r in rows) or 1
    return {
        "candidate_free_share": round(
            sum(r["events"] for r in rows if r["candidate_free"]) / total, 3
        ),
        "removable_share": round(
            sum(
                r["events"]
                for r in rows
                if r["candidate_free"] and not r["consumed_events"]
            )
            / total,
            3,
        ),
        "top_functions": rows[:10],
    }


def time_dependence(path):
    """Clock use in the policy or its sibling modules (static text check)."""
    hits = []
    for file in sorted(Path(path).resolve().parent.glob("*.py")):
        text = file.read_text(encoding="utf-8", errors="replace")
        for number, line in enumerate(text.splitlines(), 1):
            if CLOCK.search(line):
                hits.append(f"{file.name}:{number}: {line.strip()[:100]}")
    return hits


class _Stage:
    """Time one stage under its own budget and record peak RSS afterwards."""

    def __init__(self, record, name, budget):
        self.record, self.name, self.budget = record, name, budget
        self.start = 0.0

    def __enter__(self):
        self.start = _clock()
        signal.setitimer(signal.ITIMER_REAL, self.budget)
        return self

    def __exit__(self, exc_type, exc, tb):
        signal.setitimer(signal.ITIMER_REAL, 0)
        entry = {
            "seconds": round(_clock() - self.start, 3),
            "peak_rss_mb": _rss_mb(),
            "outcome": "completed",
        }
        if exc_type is StageBudget:
            entry["outcome"] = f"exceeded {self.budget:g}s stage budget"
        elif exc is not None:
            entry["outcome"] = f"{exc_type.__name__}: {str(exc)[:300]}"
        self.record["stages"][self.name] = entry
        return exc is not None  # Later stages still report what they can.


def _episode(*, seed, max_steps, count, spec, policy_for, record):
    """RoboCode's run_episode with the same adapter in both modes."""
    # pylint: disable=import-outside-toplevel
    from robocode.approaches.base_approach import BaseApproach
    from robocode.utils.episode import run_episode

    env = spec.make_env()
    try:
        primitives = spec.make_primitives(env)
        call = policy_for(env, primitives)

        class Adapter(BaseApproach):  # pylint: disable=abstract-method
            """Identical driver; only ``call`` differs between modes."""

            def reset(self, state, info):
                super().reset(state, info)
                call("reset", state, info)

            def _get_action(self):
                action = call("get_action", self._last_state)
                record["actions"].append(fingerprint(action))
                return action

            def update(self, state, reward, done, info):
                super().update(state, reward, done, info)
                record["observations"].append(fingerprint(state))
                call("update", state, reward, done, info)

        adapter = Adapter(env.action_space, env.observation_space, seed, primitives)
        metrics, _, _ = run_episode(env, adapter, seed, max_steps, count=count)
        record["metrics"] = {
            k: metrics[k] for k in ("num_steps", "total_reward", "solved")
        }
    finally:
        env.close()


def run_ordinary(args, record):
    """Stage 1: the unmodified policy (no instrumentation, no recognition)."""
    # pylint: disable=import-outside-toplevel
    from robocode.utils.episode import load_generated_approach

    from .episode_config import load_episode_spec

    spec = load_episode_spec(args.path)
    record["max_steps"] = spec.max_steps

    def policy_for(env, primitives):
        policy = load_generated_approach(
            args.path, env.action_space, env.observation_space, primitives
        )

        def call(name, *values):
            if name == "update" and not hasattr(policy, "update"):
                return None
            return getattr(policy, name)(*values)

        return call

    with _Stage(record, "ordinary_execution", args.stage_budget):
        _episode(
            seed=args.seed,
            max_steps=spec.max_steps,
            count=args.object_count,
            spec=spec,
            policy_for=policy_for,
            record=record,
        )


def run_traced(args, record):
    """Stages 2-4 in one process; each has its own budget."""
    # pylint: disable=import-outside-toplevel
    from robocode.utils.episode import load_generated_approach

    from .config import RuntimeConfig
    from .episode_config import load_episode_spec
    from .instrument import compile_source
    from .recognition import Recognition
    from .recorder import Recorder
    from .runner import RuntimeSession

    spec = load_episode_spec(args.path)
    record["max_steps"] = spec.max_steps
    config = RuntimeConfig(max_events=args.max_events)
    source = Path(args.path).read_text(encoding="utf-8")
    with _Stage(record, "recognition_and_instrumentation", args.stage_budget):
        started = _clock()
        recognition = Recognition(args.path)
        record["recognition"] = {
            "seconds": round(_clock() - started, 3),
            "candidates": len(recognition.evidence),
            "rejected_by_slice_rules": len(getattr(recognition, "rejected", [])),
            "error": recognition.error,
        }
        started = _clock()
        compile_source(Recorder(config), args.path, source)
        record["instrumentation_compile_seconds"] = round(_clock() - started, 3)
    session = RuntimeSession(args.path, config)
    # Reuse stage 2's recognition so stage 3 measures execution and recording only.
    session.recorder.recognition = recognition
    session.recorder.structural_sites = recognition.loop_sites()
    session._structural_hints = lambda: None  # pylint: disable=protected-access
    calls = collections.Counter()

    def policy_for(env, primitives):
        session.metadata.update(spec.metadata)
        session.__enter__()  # pylint: disable=unnecessary-dunder-call
        with session.phase("load-and-construction"):
            session.policy = load_generated_approach(
                args.path,
                env.action_space,
                env.observation_space,
                primitives,
                source_transform=session.source_transform,
            )

        def call(name, *values):
            if name == "update" and not hasattr(session.policy, "update"):
                return None
            calls[name] += 1
            return session.call(name, *values)

        return call

    with _Stage(record, "traced_execution", args.stage_budget):
        try:
            _episode(
                seed=args.seed,
                max_steps=spec.max_steps,
                count=args.object_count,
                spec=spec,
                policy_for=policy_for,
                record=record,
            )
        except BaseException as exc:
            session.recorder.graph.incomplete = (
                session.recorder.graph.incomplete or f"{type(exc).__name__}: {exc}"
            )
            raise
        finally:
            if session.finder is not None and session.finder in sys.meta_path:
                session.__exit__(None, None, None)
    graph = session.recorder.graph
    record["trace"] = {
        "events": len(graph.events),
        "max_events": args.max_events,
        "incomplete": graph.incomplete,
        "calls": dict(calls),
        "returned_actions": len(session.recorder.actions),
        "last_phase": graph.events[-1].phase if graph.events else None,
        "event_kinds": dict(
            collections.Counter(e.kind for e in graph.events).most_common(12)
        ),
        "mean_control_dependencies": (
            round(sum(len(e.control) for e in graph.events) / len(graph.events), 2)
            if graph.events
            else 0
        ),
        "opaque_reasons": dict(
            collections.Counter(
                e.detail.get("reason", "")[:90]
                for e in graph.events
                if e.kind == "opaque"
            ).most_common(8)
        ),
        "imprecise_events": sum(
            bool(e.detail.get("imprecise_parents")) for e in graph.events
        ),
        "attribution": attribute_events(args.path, recognition, graph),
    }
    report = None
    with _Stage(record, "report_generation", args.stage_budget):
        report = session.report()
        started = _clock()
        text = json.dumps(report)
        record["report_json_seconds"] = round(_clock() - started, 3)
        record["report_json_bytes"] = len(text)
    if report is not None:
        record["report"] = {
            k: report.get(k)
            for k in (
                "version",
                "verdict",
                "status",
                "planning_depth",
                "planning_work",
                "performed_planning_work",
                "planning_event_count",
                "possibly_relevant_planning_event_count",
                "unknown_count",
                "incomplete",
            )
        }
        record["report"]["precision"] = report.get("precision")


def parity(ordinary, traced):
    """Compare per-step fingerprints; a truncated trace is compared as a prefix."""
    a, b = ordinary.get("actions", []), traced.get("actions", [])
    oa, ob = ordinary.get("observations", []), traced.get("observations", [])
    steps = min(len(a), len(b))
    first = next((i for i in range(steps) if a[i] != b[i]), None)
    obs_steps = min(len(oa), len(ob))
    first_obs = next((i for i in range(obs_steps) if oa[i] != ob[i]), None)
    complete = (
        "metrics" in ordinary
        and "metrics" in traced
        and ordinary["stages"]["ordinary_execution"]["outcome"] == "completed"
        and traced["stages"].get("traced_execution", {}).get("outcome") == "completed"
    )
    return {
        "compared_actions": steps,
        "ordinary_actions": len(a),
        "traced_actions": len(b),
        "first_action_mismatch": first,
        "first_observation_mismatch": first_obs,
        "metrics_equal": (
            ordinary["metrics"] == traced["metrics"] if complete else None
        ),
        "status": (
            "not_compared"
            if steps == 0
            else (
                "mismatch"
                if first is not None or first_obs is not None
                else ("equal" if complete else "equal_prefix")
            )
        ),
    }


def main():
    """Run both child processes for one policy and write a combined record."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--object-count", type=int)
    parser.add_argument("--max-events", type=int, default=200_000)
    parser.add_argument("--stage-budget", type=float, default=60.0)
    parser.add_argument("--mode", choices=("both", "ordinary", "traced"))
    parser.add_argument("--name")
    parser.add_argument(
        "--virtual-clock",
        type=float,
        nargs="?",
        const=1e-3,
        metavar="STEP",
        help="Diagnostic: time.time/perf_counter/monotonic advance STEP seconds "
        "per call in both modes (default 0.001)",
    )
    args = parser.parse_args()
    args.path = args.path.resolve()
    name = args.name or args.path.parent.parent.parent.name
    if args.mode in ("ordinary", "traced"):
        signal.signal(signal.SIGALRM, _alarm)
        if args.virtual_clock:
            virtual_clock(args.virtual_clock)
        record = {
            "mode": args.mode,
            "stages": {},
            "actions": [],
            "observations": [],
            "process_start_rss_mb": _rss_mb(),
        }
        (run_ordinary if args.mode == "ordinary" else run_traced)(args, record)
        args.out.write_text(json.dumps(record) + "\n")
        return
    args.out.mkdir(parents=True, exist_ok=True)
    results = {}
    for mode in ("ordinary", "traced"):
        target = args.out / f"{name}.{mode}.json"
        command = [
            sys.executable,
            "-m",
            "policy_graph.runtime.diagnostics",
            str(args.path),
            "--out",
            str(target),
            "--mode",
            mode,
            "--seed",
            str(args.seed),
            "--max-events",
            str(args.max_events),
            "--stage-budget",
            str(args.stage_budget),
            *(["--object-count", str(args.object_count)] if args.object_count else []),
            *(
                ["--virtual-clock", str(args.virtual_clock)]
                if args.virtual_clock
                else []
            ),
        ]
        started = _clock()
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=4 * args.stage_budget + 60,
            check=False,
        )
        record = (
            json.loads(target.read_text())
            if target.is_file()
            else {"stages": {}, "error": process.stderr[-2000:]}
        )
        record["process_seconds"] = round(_clock() - started, 2)
        record["exit_code"] = process.returncode
        results[mode] = record
        target.unlink(missing_ok=True)
    combined = {
        "policy": str(args.path),
        "source_sha256": hashlib.sha256(args.path.read_bytes()).hexdigest(),
        "seed": args.seed,
        "max_events": args.max_events,
        "stage_budget_seconds": args.stage_budget,
        "clock_use": time_dependence(args.path),
        "virtual_clock": args.virtual_clock,
        "ordinary": {
            k: v
            for k, v in results["ordinary"].items()
            if k not in ("actions", "observations")
        },
        "traced": {
            k: v
            for k, v in results["traced"].items()
            if k not in ("actions", "observations")
        },
        "parity": parity(results["ordinary"], results["traced"]),
    }
    (args.out / f"{name}.json").write_text(json.dumps(combined, indent=2) + "\n")
    print(json.dumps({"policy": name, "parity": combined["parity"]["status"]}))


if __name__ == "__main__":
    main()  # type: ignore[no-untyped-call]
