"""Compare groups of runs that differ in one setting (e.g. legacy vs neutral prompt).

Every run of a group is one replicate seed of the same agent on the same environment;
groups differ in the setting under study. The script reads each run's
``results.json`` (with its ``.hydra`` config and ``sandbox`` git history) and,
optionally, ``test_history.py`` output folders holding re-runs of every policy
checkpoint, and writes to ``--out``:

``final_solve_rate.png``
    The final policy's solve rate per run (one dot per seed, a tick at the group
    mean), on all evaluation counts, the counts seen in development, and the counts
    never seen. A group evaluated with a longer per-episode policy-time limit than
    ``--view-timeout`` also gets a view that counts episodes over that limit as failed
    (exact, from each episode's recorded policy time).
``solve_by_count.png``
    Solve rate per object count: group mean (thick) and each seed (thin).
``checkpoints.png``
    The re-run solve rate of every checkpoint, by checkpoint number and by minutes
    into development (the policy in force at each moment, until the agent stopped).
``development.png``
    Development cost, time, agent turns, checkpoints and output tokens per run.
``eval_compute.png``
    Policy seconds per episode and steps per solved episode, by object count.
``failures.png``
    Unsolved episodes by reason (ran out of policy time, ran out of steps, other).
``summary.md`` and ``comparison.json``
    The numbers behind the figures, per run and per group.

Usage:

    python experiments/compare_prompt_styles.py \
        --group legacy <run dirs...> --group neutral <run dirs...> \
        [--history <test_history.py out dirs...>] --out <dir> [--view-timeout 60]

Run dirs are searched for ``results.json`` files that have a ``.hydra`` folder next
to them, so a sweep folder brings in all its replicates. History folders are matched
to runs by commit, so they can be listed in any order.
"""

from __future__ import annotations

import argparse
import importlib
import json
import subprocess
import sys
from collections import defaultdict
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import yaml

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
from experiments import test_history  # pylint: disable=wrong-import-position

plt.switch_backend("Agg")

# Categorical slots in fixed order (validated light-mode palette); groups take them in
# the order given on the command line.
SERIES = (
    "#2a78d6",
    "#eb6834",
    "#1baf7a",
    "#eda100",
    "#e87ba4",
    "#008300",
    "#6250d6",
    "#e34948",
)
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#8a8985"
GRID = "#e4e3df"
SHADE = "#f0efeb"
SURFACE = "#fcfcfb"
SETUP_COMMIT = "initial sandbox setup"
REASONS = ("ran out of policy time", "ran out of steps", "other")

plt.rcParams.update(
    {
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "axes.edgecolor": GRID,
        "axes.labelcolor": INK_2,
        "axes.titlecolor": INK,
        "axes.titlelocation": "left",
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.6,
        "xtick.color": INK_2,
        "ytick.color": INK_2,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "text.color": INK,
        "legend.frameon": False,
        "legend.fontsize": 8,
        "font.size": 9,
    }
)


@dataclass
class Run:
    """One replicate: its results, config, and policy checkpoints."""

    group: str
    path: Path
    results: dict[str, Any]
    config: dict[str, Any]
    environment: str
    checkpoints: list[dict] = field(default_factory=list)
    dev_start: float | None = None
    # checkpoint sha -> re-run rows (test_history.py replay files)
    replays: dict[str, list[dict]] = field(default_factory=dict)
    history_dir: Path | None = None

    @property
    def seed(self) -> int:
        """The replicate seed."""
        return int(self.results.get("replicate_seed", self.config.get("seed", -1)))

    @property
    def episodes(self) -> list[dict]:
        """Per-episode evaluation records of the final policy."""
        return list(self.results.get("per_episode", []))

    @property
    def timeout(self) -> float | None:
        """Per-episode policy-time limit of the evaluation, in seconds."""
        value = self.config.get("eval_timeout")
        return float(value) if value is not None else None

    @property
    def design_counts(self) -> list[int]:
        """Object counts the agent could use during development."""
        regimes = self.results.get("count_regimes") or {}
        return [int(c) for c in (regimes.get("design") or {}).get("counts", [])]

    @property
    def dev_end(self) -> float | None:
        """When development ended (start plus the recorded development time)."""
        wall = self.results.get("gen_wall_time_s")
        if self.dev_start is None or wall is None:
            return None
        return self.dev_start + float(wall)


@dataclass
class Series:
    """One line or dot column in a figure: a group, or a view of one."""

    label: str
    color: str
    runs: list[Run]
    solved: Callable[[dict], bool]
    hollow: bool = False


# -------------------------------------------------------------------------- loading


def _git(sandbox: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(sandbox), *args],
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _environment(job: Path, config: dict, results: dict) -> str:
    overrides = job / ".hydra" / "overrides.yaml"
    if overrides.exists():
        for item in yaml.safe_load(overrides.read_text()) or []:
            key, _, value = str(item).partition("=")
            if key == "environment":
                return value
    experiment = str(results.get("experiment_id") or config.get("experiment_id") or "")
    return experiment.split("__", 1)[0] or "unknown"


def _dev_start(sandbox: Path, first_checkpoint: float | None) -> float | None:
    """The sandbox setup commit just before the agent's first checkpoint."""
    rows = []
    for line in _git(sandbox, "log", "--reverse", "--format=%ct%x09%s").splitlines():
        when, _, subject = line.partition("\t")
        rows.append((float(when), subject))
    if not rows:
        return None
    setup = [
        t
        for t, s in rows
        if s == SETUP_COMMIT and (first_checkpoint is None or t <= first_checkpoint)
    ]
    return max(setup) if setup else rows[0][0]


def load_runs(groups: list[list[str]]) -> list[Run]:
    """Every run under each group's folders, oldest group first."""
    runs: list[Run] = []
    seen: set[Path] = set()
    for name, *dirs in groups:
        found = 0
        for folder in dirs:
            for results_path in sorted(Path(folder).rglob("results.json")):
                job = results_path.parent.resolve()
                config_path = job / ".hydra" / "config.yaml"
                if job in seen or not config_path.exists():
                    continue
                seen.add(job)
                config = yaml.safe_load(config_path.read_text())
                results = json.loads(results_path.read_text())
                run = Run(
                    group=name,
                    path=job,
                    results=results,
                    config=config,
                    environment=_environment(job, config, results),
                )
                sandbox = job / "sandbox"
                if (sandbox / ".git").exists():
                    run.checkpoints = test_history.versions(sandbox)
                    first = run.checkpoints[0]["time"] if run.checkpoints else None
                    run.dev_start = _dev_start(sandbox, first)
                runs.append(run)
                found += 1
        if not found:
            raise SystemExit(
                f"group {name!r}: no results.json with .hydra under {dirs}"
            )
    environments = {r.environment for r in runs}
    if len(environments) > 1:
        raise SystemExit(f"runs span several environments: {sorted(environments)}")
    order = [g[0] for g in groups]
    return sorted(runs, key=lambda r: (order.index(r.group), r.seed))


def attach_histories(runs: list[Run], folders: Sequence[Path]) -> list[str]:
    """Attach each test_history.py folder's re-runs to the run they came from."""
    problems = []
    for folder in folders:
        versions_path = folder / "versions.json"
        if not versions_path.exists():
            problems.append(f"{folder}: no versions.json (run extract first)")
            continue
        shas = {v["sha"] for v in json.loads(versions_path.read_text())}
        overlap = [(len(shas & {c["sha"] for c in r.checkpoints}), r) for r in runs]
        best, run = max(overlap, key=lambda pair: pair[0], default=(0, None))
        if run is None or not best:
            problems.append(f"{folder}: matches no run's commits")
            continue
        suite_path = folder / "suite.json"
        scenes = (
            [(e["seed"], e["count"]) for e in json.loads(suite_path.read_text())]
            if suite_path.exists()
            else None
        )
        replays: dict[str, list[dict]] = defaultdict(list)
        for path in sorted((folder / "replay").glob("v*.json")):
            try:
                row = json.loads(path.read_text())
            except (OSError, ValueError):
                continue
            results = row.get("results") or []
            if not results or row.get("sha") not in shas:
                continue
            if scenes and [(e["seed"], e["count"]) for e in results] != scenes:
                continue
            replays[row["sha"]].append(row)
        run.replays = dict(replays)
        run.history_dir = folder
    return problems


def step_limit_of(run: Run) -> Callable[[int | None], int | None]:
    """The evaluation step limit per object count (built from the run's env)."""
    default = run.config.get("max_steps")
    env = None
    env_config_path = run.path / "env_config.json"
    if env_config_path.exists():
        env_config = json.loads(env_config_path.read_text())
        module, name = env_config.pop("_target_").rsplit(".", 1)
        try:
            env = getattr(importlib.import_module(module), name)(**env_config)
        except Exception as error:  # pylint: disable=broad-exception-caught
            print(f"could not build the env for step limits: {error}")

    def limit(count: int | None) -> int | None:
        if count is not None:
            # A per-count limit we cannot compute is unknown, not the global one.
            if env is None or not hasattr(env, "max_steps_for_count"):
                return None
            return int(env.max_steps_for_count(count))
        return int(default) if default else None

    return limit


# -------------------------------------------------------------------------- numbers


def failure_reason(
    episode: dict, timeout: float | None, step_limit: Callable[[int | None], int | None]
) -> str | None:
    """Why an episode was unsolved (None if solved).

    The harness scores a policy-time overrun as unsolved with zero steps.
    """
    if episode.get("solved"):
        return None
    steps = episode.get("num_steps") or 0
    used = episode.get("policy_time_s") or 0.0
    if steps == 0 and timeout and used >= 0.9 * timeout:
        return REASONS[0]
    limit = step_limit(episode.get("object_count"))
    if limit and steps >= limit:
        return REASONS[1]
    return REASONS[2]


def rate(episodes: list[dict], solved: Callable[[dict], bool]) -> float | None:
    """Fraction of episodes ``solved`` accepts (None for no episodes)."""
    return sum(map(solved, episodes)) / len(episodes) if episodes else None


def checkpoint_rate(rows: list[dict]) -> float | None:
    """Mean solve rate over a checkpoint's re-runs."""
    rates = [
        sum(r["solved"] for r in row["results"]) / len(row["results"]) for row in rows
    ]
    return float(np.mean(rates)) if rates else None


def _spread(values: Sequence[float | None], digits: int = 2) -> str:
    kept = [v for v in values if v is not None]
    if not kept:
        return "—"
    mean = float(np.mean(kept))
    if len(kept) == 1:
        return f"{mean:.{digits}f}"
    return f"{mean:.{digits}f} ({min(kept):.{digits}f}–{max(kept):.{digits}f})"


def make_series(runs: list[Run], groups: list[str], view: float) -> list[Series]:
    """Each group, plus a stricter-time-limit view of groups evaluated longer."""
    out = []
    for slot, group in enumerate(groups):
        members = [r for r in runs if r.group == group]
        color = SERIES[slot]
        out.append(Series(group, color, members, lambda e: bool(e.get("solved"))))
        longer = all((r.timeout or 0) > view for r in members)
        timed = all("policy_time_s" in e for r in members for e in r.episodes)
        if longer and timed:
            out.append(
                Series(
                    f"{group}, policy time over {view:g} s counted as failed",
                    color,
                    members,
                    lambda e: bool(e.get("solved")) and e["policy_time_s"] <= view,
                    hollow=True,
                )
            )
    return out


# -------------------------------------------------------------------------- figures


def _dots(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    ax,
    x: float,
    values: list[float],
    series: Series,
    width: float,
    label: bool,
    digits: int = 2,
) -> None:
    """One column: a dot per seed and a tick at the mean, labelled."""
    if not values:
        return
    jitter = np.linspace(-width / 4, width / 4, len(values)) if len(values) > 1 else [0]
    ax.scatter(
        [x + j for j in jitter],
        values,
        s=26,
        facecolors=SURFACE if series.hollow else series.color,
        edgecolors=series.color,
        linewidths=1.4,
        zorder=3,
        label=series.label if label else None,
    )
    mean = float(np.mean(values))
    ax.hlines(mean, x - width / 2, x + width / 2, color=series.color, linewidth=2)
    ax.annotate(
        f"{mean:.{digits}f}",
        (x + width / 2, mean),
        xytext=(3, 0),
        textcoords="offset points",
        va="center",
        fontsize=7.5,
        color=INK_2,
    )


def plot_final(series: list[Series], out: Path) -> None:
    """Final solve rate on all, seen, and never-seen counts."""
    design = set(series[0].runs[0].design_counts)
    counts = sorted(
        {e["object_count"] for s in series for r in s.runs for e in r.episodes}
    )
    seen = [c for c in counts if c in design]
    unseen = [c for c in counts if c not in design]
    columns = [("all counts", counts)]
    if seen and unseen:
        columns += [
            (f"seen in development\n(counts {', '.join(map(str, seen))})", seen),
            (f"never seen\n(counts {', '.join(map(str, unseen))})", unseen),
        ]
    fig, ax = plt.subplots(figsize=(9, 4.6))
    width = 0.8 / len(series)
    lowest = 1.0
    for col, (_, chosen) in enumerate(columns):
        for slot, s in enumerate(series):
            values = []
            for run in s.runs:
                value = rate(
                    [e for e in run.episodes if e["object_count"] in chosen], s.solved
                )
                if value is not None:
                    values.append(value)
            lowest = min([lowest, *values])
            x = col - 0.4 + width * (slot + 0.5)
            _dots(ax, x, values, s, width * 0.7, label=col == 0)
    ax.set_xticks(range(len(columns)), [c[0] for c in columns])
    ax.grid(axis="x", visible=False)
    ax.set_ylim(max(0.0, lowest - 0.08), 1.02)
    ax.set_ylabel("solve rate of the final policy")
    seeds = ", ".join(f"{s.label}: {len(s.runs)}" for s in series if not s.hollow)
    ax.set_title(
        f"Final policy on the evaluation suite (one dot per seed; runs {seeds})"
    )
    ax.legend(loc="lower left")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_by_count(series: list[Series], out: Path) -> None:
    """Solve rate per object count: mean and per-seed lines."""
    fig, ax = plt.subplots(figsize=(8, 4.6))
    design = series[0].runs[0].design_counts
    counts = sorted(
        {e["object_count"] for s in series for r in s.runs for e in r.episodes}
    )
    unseen = [c for c in counts if c not in design]
    if design and unseen:
        edge = (max(design) + min(unseen)) / 2
        ax.axvspan(min(counts) - 1, edge, color=SHADE, zorder=0, linewidth=0)
        ax.text(min(counts) - 0.6, 0.03, "seen in development", color=MUTED, fontsize=8)
    for s in series:
        per_seed = []
        for run in s.runs:
            rates = []
            for c in counts:
                value = rate(
                    [e for e in run.episodes if e["object_count"] == c], s.solved
                )
                rates.append(np.nan if value is None else value)
            per_seed.append(rates)
            if not s.hollow:
                ax.plot(counts, rates, color=s.color, linewidth=0.8, alpha=0.35)
        mean = np.nanmean(np.array(per_seed, dtype=float), axis=0)
        ax.plot(
            counts,
            mean,
            color=s.color,
            linewidth=2,
            linestyle="--" if s.hollow else "-",
            marker="o",
            markersize=5,
            markerfacecolor=SURFACE if s.hollow else s.color,
            label=f"{s.label} (mean of {len(s.runs)} seeds)",
        )
    ax.set_xlim(min(counts) - 1, max(counts) + 1)
    ax.set_xticks(counts)
    ax.set_ylim(-0.02, 1.02)
    ax.set_xlabel("object count")
    ax.set_ylabel("solve rate")
    ax.set_title("Solve rate by object count (thin lines: single seeds)")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_checkpoints(runs: list[Run], groups: list[str], out: Path) -> bool:
    """Re-run solve rate per checkpoint, by number and by development minute."""
    if not any(r.replays for r in runs):
        return False
    fig, (ax_n, ax_t) = plt.subplots(1, 2, figsize=(12, 4.6), sharey=True)
    for run in runs:
        color = SERIES[groups.index(run.group)]
        points = [
            (c["index"], c["time"], checkpoint_rate(run.replays.get(c["sha"], [])))
            for c in run.checkpoints
        ]
        index = [p[0] for p in points]
        rates = [np.nan if p[2] is None else p[2] for p in points]
        ax_n.plot(index, rates, color=color, linewidth=1.2, marker="o", markersize=4)
        if index and not np.isnan(rates[-1]):
            ax_n.annotate(
                f"{run.seed}",
                (index[-1], rates[-1]),
                xytext=(4, 0),
                textcoords="offset points",
                va="center",
                fontsize=7,
                color=INK_2,
            )
        if run.dev_start is None:
            continue
        minutes = [(p[1] - run.dev_start) / 60 for p in points]
        end = run.dev_end
        if end is not None and minutes:
            last = max(minutes[-1], (end - run.dev_start) / 60)
            ax_t.step(
                [*minutes, last],
                [*rates, rates[-1]],
                where="post",
                color=color,
                linewidth=1.2,
            )
            ax_t.plot([last], [rates[-1]], marker="|", markersize=9, color=color)
    for slot, group in enumerate(groups):
        members = [r for r in runs if r.group == group]
        replayed = sum(
            1 for r in members for c in r.checkpoints if r.replays.get(c["sha"])
        )
        total = sum(len(r.checkpoints) for r in members)
        ax_n.plot(
            [],
            [],
            color=SERIES[slot],
            linewidth=1.2,
            label=f"{group} ({replayed}/{total} checkpoints re-run)",
        )
    ax_n.set_xlabel("checkpoint (commit that changed the policy)")
    ax_n.set_ylabel("solve rate when re-run on the evaluation suite")
    ax_n.set_ylim(-0.02, 1.02)
    ax_n.set_title("By checkpoint (labels: replicate seed)")
    ax_n.legend(loc="lower right")
    ax_t.set_xlabel("minutes into development (| = agent stopped)")
    ax_t.set_title("Policy in force over development time")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return True


DEV_METRICS: tuple[tuple[str, Callable[[Run], float | None]], ...] = (
    ("development cost ($)", lambda r: r.results.get("agent_cost_usd")),
    (
        "development time (min)",
        lambda r: (
            r.results["gen_wall_time_s"] / 60
            if r.results.get("gen_wall_time_s") is not None
            else None
        ),
    ),
    ("agent turns", lambda r: r.results.get("gen_num_turns")),
    (
        "policy checkpoints",
        lambda r: float(len(r.checkpoints)) if r.checkpoints else None,
    ),
    (
        "output tokens (thousands)",
        lambda r: (
            r.results["gen_output_tokens"] / 1000
            if r.results.get("gen_output_tokens") is not None
            else None
        ),
    ),
)


def plot_development(series: list[Series], out: Path) -> None:
    """Development effort per run, one panel per measure."""
    groups = [s for s in series if not s.hollow]
    fig, axes = plt.subplots(1, len(DEV_METRICS), figsize=(3 * len(DEV_METRICS), 3.6))
    width = 0.8 / len(groups)
    for ax, (name, measure) in zip(axes, DEV_METRICS):
        top = 0.0
        for slot, s in enumerate(groups):
            values = [v for v in (measure(r) for r in s.runs) if v is not None]
            top = max([top, *values])
            _dots(
                ax, -0.4 + width * (slot + 0.5), values, s, width * 0.7, False, digits=1
            )
        ax.set_xticks(
            [-0.4 + width * (i + 0.5) for i in range(len(groups))],
            [s.label for s in groups],
        )
        ax.grid(axis="x", visible=False)
        ax.set_ylim(0, top * 1.12 or 1)
        ax.set_title(name, fontsize=9)
    fig.suptitle("Development (one dot per seed, tick at the mean)", x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_compute(series: list[Series], out: Path) -> None:
    """Policy seconds per episode and steps per solved episode, by count."""
    groups = [s for s in series if not s.hollow]
    fig, (ax_time, ax_steps) = plt.subplots(1, 2, figsize=(12, 4.4))
    limits = sorted({r.timeout for s in groups for r in s.runs if r.timeout})
    for s in groups:
        by_count: dict[int, list[dict]] = defaultdict(list)
        for run in s.runs:
            for e in run.episodes:
                by_count[e["object_count"]].append(e)
        counts = sorted(by_count)
        times = [[e.get("policy_time_s", np.nan) for e in by_count[c]] for c in counts]
        med = [float(np.nanmedian(t)) for t in times]
        low = [float(np.nanpercentile(t, 25)) for t in times]
        high = [float(np.nanpercentile(t, 75)) for t in times]
        ax_time.fill_between(counts, low, high, color=s.color, alpha=0.15, linewidth=0)
        ax_time.plot(
            counts,
            med,
            color=s.color,
            linewidth=2,
            marker="o",
            markersize=5,
            label=f"{s.label} (median, band 25–75%)",
        )
        steps = [
            [e["num_steps"] for e in by_count[c] if e.get("solved")] for c in counts
        ]
        ax_steps.plot(
            counts,
            [float(np.median(v)) if v else np.nan for v in steps],
            color=s.color,
            linewidth=2,
            marker="o",
            markersize=5,
            label=f"{s.label} (median)",
        )
    for limit in limits:
        users = sorted({s.label for s in groups for r in s.runs if r.timeout == limit})
        ax_time.axhline(limit, color=MUTED, linewidth=0.9, linestyle=":")
        ax_time.text(
            0.5,
            limit * 1.08,
            f"{limit:g} s limit ({', '.join(users)})",
            color=MUTED,
            fontsize=7.5,
        )
    ax_time.set_yscale("log")
    ax_time.set_xlabel("object count")
    ax_time.set_ylabel("policy seconds per episode (log)")
    ax_time.set_title("Time the policy spends deciding, per episode")
    ax_time.legend(loc="lower right")
    ax_steps.set_xlabel("object count")
    ax_steps.set_ylabel("steps")
    ax_steps.set_title("Steps per solved episode")
    ax_steps.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def failure_table(
    series: list[Series], step_limit: Callable[[int | None], int | None]
) -> dict[str, dict[str, dict[int, int]]]:
    """Group -> reason -> object count -> unsolved episodes (summed over seeds)."""
    table: dict[str, dict[str, dict[int, int]]] = {}
    for s in series:
        if s.hollow:
            continue
        cells: dict[str, dict[int, int]] = {r: defaultdict(int) for r in REASONS}
        for run in s.runs:
            for e in run.episodes:
                reason = failure_reason(e, run.timeout, step_limit)
                if reason:
                    cells[reason][e["object_count"]] += 1
        table[s.label] = {r: dict(v) for r, v in cells.items()}
    return table


def plot_failures(
    series: list[Series], table: dict[str, dict[str, dict[int, int]]], out: Path
) -> None:
    """Unsolved episodes per count, one panel per reason."""
    groups = [s for s in series if not s.hollow]
    counts = sorted(
        {e["object_count"] for s in groups for r in s.runs for e in r.episodes}
    )
    # Reasons no episode had stay in summary.md only.
    reasons = [r for r in REASONS if any(table[s.label][r] for s in groups)] or [
        REASONS[0]
    ]
    fig, axes = plt.subplots(
        1,
        len(reasons),
        figsize=(4.4 * len(reasons) + 0.6, 3.8),
        sharey=True,
        squeeze=False,
    )
    width = 0.8 / len(groups)
    for ax, reason in zip(axes[0], reasons):
        for slot, s in enumerate(groups):
            values = [table[s.label][reason].get(c, 0) for c in counts]
            ax.bar(
                [i - 0.4 + width * (slot + 0.5) for i in range(len(counts))],
                values,
                width=width,
                color=s.color,
                edgecolor=SURFACE,
                linewidth=1,
                label=f"{s.label} ({sum(values)} total)",
            )
        ax.set_xticks(range(len(counts)), [str(c) for c in counts])
        ax.grid(axis="x", visible=False)
        ax.set_xlabel("object count")
        ax.set_title(reason)
        ax.legend(loc="upper left")
    axes[0][0].set_ylabel("unsolved episodes (all seeds)")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


# -------------------------------------------------------------------------- summary


def run_row(run: Run, series: list[Series]) -> dict[str, Any]:
    """The numbers for one run."""
    design = set(run.design_counts)
    eps = run.episodes
    row: dict[str, Any] = {
        "group": run.group,
        "seed": run.seed,
        "path": str(run.path),
        "eval_timeout_s": run.timeout,
        "solve_rate": rate(eps, lambda e: bool(e.get("solved"))),
        "seen_solve_rate": rate(
            [e for e in eps if e["object_count"] in design],
            lambda e: bool(e.get("solved")),
        ),
        "unseen_solve_rate": rate(
            [e for e in eps if e["object_count"] not in design],
            lambda e: bool(e.get("solved")),
        ),
    }
    for s in series:
        if s.hollow and run in s.runs:
            row["solve_rate_stricter_view"] = rate(eps, s.solved)
    for name, measure in DEV_METRICS:
        row[name] = measure(run)
    rates = [
        (c["index"], c["time"], checkpoint_rate(run.replays.get(c["sha"], [])))
        for c in run.checkpoints
    ]
    replayed = [(i, t, r) for i, t, r in rates if r is not None]
    first = next(((i, t, r) for i, t, r in replayed if r > 0), None)
    timeouts = sorted(
        {row_.get("timeout") for rows in run.replays.values() for row_ in rows},
        key=lambda v: (v is None, v or 0),
    )
    row["checkpoints"] = {
        "history_dir": str(run.history_dir) if run.history_dir else None,
        "replayed": len(replayed),
        "total": len(run.checkpoints),
        "rerun_timeout_s": [t for t in timeouts if t is not None] or None,
        "rates": {f"v{i:02d}": r for i, _, r in replayed},
        "first_solving": (
            {
                "checkpoint": first[0],
                "minute": (first[1] - run.dev_start) / 60 if run.dev_start else None,
                "rate": first[2],
            }
            if first
            else None
        ),
        "best": max((r for _, _, r in replayed), default=None),
        "final": (
            replayed[-1][2] if replayed and replayed[-1][0] == len(rates) else None
        ),
    }
    return row


def write_summary(
    runs: list[Run],
    series: list[Series],
    table: dict[str, dict[str, dict[int, int]]],
    problems: list[str],
    figures: list[str],
    out: Path,
) -> None:
    """summary.md and comparison.json."""
    rows = [run_row(r, series) for r in runs]
    groups = [s.label for s in series if not s.hollow]
    views = {s.label: s for s in series if s.hollow}
    lines = [
        f"# Comparison on {runs[0].environment}",
        "",
        "Groups: "
        + "; ".join(
            f"**{g}** ({len([r for r in runs if r.group == g])} runs, seeds "
            + ", ".join(str(r.seed) for r in runs if r.group == g)
            + ")"
            for g in groups
        ),
        "",
        "## Final policy, group mean (min–max over seeds)",
        "",
        "| | " + " | ".join(groups) + " |",
        "|---|" + "---|" * len(groups),
    ]

    def group_line(label: str, key: str, digits: int = 2) -> str:
        cells = [
            _spread([r[key] for r in rows if r["group"] == g], digits) for g in groups
        ]
        return f"| {label} | " + " | ".join(cells) + " |"

    lines += [
        group_line("solve rate, all counts", "solve_rate"),
        group_line("seen in development", "seen_solve_rate"),
        group_line("never seen", "unseen_solve_rate"),
    ]
    for label, view in views.items():
        cells = [
            (
                _spread(
                    [r.get("solve_rate_stricter_view") for r in rows if r["group"] == g]
                )
                if g == view.runs[0].group
                else "—"
            )
            for g in groups
        ]
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    lines.append(
        "| evaluation policy-time limit (s) | "
        + " | ".join(
            ", ".join(
                sorted({f"{r.timeout:g}" for r in runs if r.group == g and r.timeout})
            )
            for g in groups
        )
        + " |"
    )
    for name, _ in DEV_METRICS:
        lines.append(group_line(name, name, 1))
    lines += ["", "## Unsolved episodes by reason (all seeds)", ""]
    lines += ["| reason | " + " | ".join(groups) + " |", "|---|" + "---|" * len(groups)]
    for reason in REASONS:
        lines.append(
            f"| {reason} | "
            + " | ".join(str(sum(table[g][reason].values())) for g in groups)
            + " |"
        )
    lines += [
        "",
        "## Per run",
        "",
        "| group | seed | solve | seen | never seen | cost $ | dev min | turns "
        "| checkpoints | re-run | first solving checkpoint | best | final |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    def fmt(value: Any, digits: int = 2) -> str:
        return "—" if value is None else f"{value:.{digits}f}"

    for r in rows:
        ck = r["checkpoints"]
        first = ck["first_solving"]
        first_text = (
            f"v{first['checkpoint']:02d}"
            + (f" at {first['minute']:.0f} min" if first["minute"] is not None else "")
            + f" ({first['rate']:.2f})"
            if first
            else "—"
        )
        rerun = f"{ck['replayed']}/{ck['total']}"
        if ck["rerun_timeout_s"]:
            rerun += " @ " + ", ".join(f"{t:g}" for t in ck["rerun_timeout_s"]) + " s"
        lines.append(
            f"| {r['group']} | {r['seed']} | {fmt(r['solve_rate'])} "
            f"| {fmt(r['seen_solve_rate'])} | {fmt(r['unseen_solve_rate'])} "
            f"| {fmt(r['development cost ($)'])} "
            f"| {fmt(r['development time (min)'], 1)} "
            f"| {fmt(r['agent turns'], 0)} | {ck['total']} | {rerun} | {first_text} "
            f"| {fmt(ck['best'])} | {fmt(ck['final'])} |"
        )
    lines += [
        "",
        "## Notes",
        "",
        "- Solve rates are over every scheduled evaluation episode; an episode that "
        "ran out of policy time counts as unsolved.",
        "- A stricter-limit view counts a solved episode as failed when its recorded "
        "policy time exceeded the limit. The policies in that group were not told about "
        "a limit, so this is the same policy judged by the other group's rule, not what "
        "an agent told about that limit would have written.",
        "- Ran out of policy time: the harness stopped the episode at the evaluation "
        "limit. Ran out of steps: the episode reached the step limit for its object "
        "count without finishing.",
        "- Checkpoint rates are re-runs by `experiments/test_history.py replay` on the "
        "run's own evaluation suite (mean over repeats). `@ N s` is the re-run cutoff "
        "where the replay files record it.",
        "- Development time runs from the sandbox setup commit to the agent's stop.",
        "- Few seeds per group: compare the per-seed spread before reading a "
        "difference between means as an effect.",
    ]
    if problems:
        lines += ["", "## Warnings", ""] + [f"- {p}" for p in problems]
    lines += ["", "## Figures", ""] + [f"- `{f}`" for f in figures]
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "comparison.json").write_text(
        json.dumps({"runs": rows, "failures": table}, indent=1, default=str),
        encoding="utf-8",
    )


def main() -> None:
    """Command-line entry."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument(
        "--group",
        nargs="+",
        action="append",
        required=True,
        metavar=("NAME", "DIR"),
        help="a group name followed by run folders (repeat for each group)",
    )
    parser.add_argument(
        "--history",
        nargs="*",
        type=Path,
        default=[],
        help="test_history.py output folders (matched to runs by commit)",
    )
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--view-timeout",
        type=float,
        default=60.0,
        help="also judge groups evaluated with a longer limit by this one",
    )
    args = parser.parse_args()
    if any(len(g) < 2 for g in args.group):
        parser.error("each --group needs a name and at least one folder")
    groups = [g[0] for g in args.group]
    if len(set(groups)) != len(groups) or len(groups) > len(SERIES):
        parser.error(f"group names must be unique, at most {len(SERIES)} groups")

    runs = load_runs(args.group)
    problems = attach_histories(runs, args.history)
    suites = {
        (r.results.get("eval_seed"), r.results.get("num_eval_tasks")) for r in runs
    }
    sizes = {
        len(row["results"])
        for run in runs
        for rows_ in run.replays.values()
        for row in rows_
    }
    if len(sizes) > 1:
        problems.append(
            f"checkpoint re-runs use different numbers of episodes: {sorted(sizes)}"
        )
    if len(suites) > 1:
        problems.append(
            f"runs were evaluated on different suites: {sorted(suites, key=str)}"
        )
    series = make_series(runs, groups, args.view_timeout)
    table = failure_table(series, step_limit_of(runs[0]))

    args.out.mkdir(parents=True, exist_ok=True)
    plot_final(series, args.out / "final_solve_rate.png")
    plot_by_count(series, args.out / "solve_by_count.png")
    plot_development(series, args.out / "development.png")
    plot_compute(series, args.out / "eval_compute.png")
    plot_failures(series, table, args.out / "failures.png")
    figures = [
        "final_solve_rate.png",
        "solve_by_count.png",
        "development.png",
        "eval_compute.png",
        "failures.png",
    ]
    if plot_checkpoints(runs, groups, args.out / "checkpoints.png"):
        figures.insert(2, "checkpoints.png")
    write_summary(runs, series, table, problems, figures, args.out)
    for problem in problems:
        print(f"note: {problem}")
    print(f"{len(runs)} runs -> {args.out}/summary.md and {len(figures)} figures")


if __name__ == "__main__":
    main()
