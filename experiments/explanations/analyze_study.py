"""Analyze an explanation study's ``rounds.jsonl``.

Writes ``<study_dir>/analysis/``:

- ``rounds.csv``: one flat row per round (the table behind every figure).
- ``by_condition_round.csv``: accuracy, rating and length per condition and round.
- ``trends.csv``: per-condition linear trends over rounds. Accuracy is adjusted for
  test difficulty (the divergence percentile) so that easier questions are not
  mistaken for learning. CIs come from a bootstrap over users.
- ``trends.png``: accuracy, rating and explanation length by round (small multiples).
- ``report.md``: the tables above, accuracy by difficulty, and for every adaptive
  user, what the profile said before each round and how the explanation changed.

    python experiments/explanations/analyze_study.py outputs/explanations/demo_mock
"""

import argparse
import json
import re
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # pylint: disable=wrong-import-position
import numpy as np  # pylint: disable=wrong-import-position
import pandas as pd  # pylint: disable=wrong-import-position

from robocode.explanations.explanation_generator import (  # pylint: disable=wrong-import-position
    profile_for_prompt,
)
from robocode.explanations.logger import (  # pylint: disable=wrong-import-position
    read_jsonl,
)

# Categorical slots 1-3 of the reference palette (validated all-pairs, light mode).
CONDITION_COLORS = {
    "no_learning": "#2a78d6",
    "understanding_only": "#eb6834",
    "understanding_preference": "#1baf7a",
}
SURFACE = "#fcfcfb"
TEXT_PRIMARY = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e4e3df"


def markdown_table(df: pd.DataFrame, index: bool = True) -> str:
    """A GitHub Markdown table (avoids an extra dependency on tabulate)."""
    if index:
        df = df.reset_index()
    header = [str(c) for c in df.columns]
    rows = [
        [f"{v:.3f}" if isinstance(v, float) else str(v) for v in row]
        for row in df.itertuples(index=False)
    ]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    return "\n".join(lines + ["| " + " | ".join(r) + " |" for r in rows])


def flatten(records: list[dict[str, Any]]) -> pd.DataFrame:
    """One row per round with the fields used in analysis."""
    rows = []
    for r in records:
        rows.append(
            {
                "user_id": r["user_id"],
                "condition": r["condition"],
                "round": r["round"],
                "is_eval_round": r["is_eval_round"],
                "persona": r.get("participant", {}).get("persona"),
                "env_name": r["env_name"],
                "policy_id": r["policy_id"],
                "words": r["explanation"]["word_count"],
                "bullets": r["explanation"]["structure"]["bullets"],
                "used_profile": r["explanation"]["used_profile"],
                "test_id": r["test"]["test_id"],
                "difficulty": r["test"]["difficulty"],
                "divergence_percentile": r["test"]["divergence_percentile"],
                "correct": int(bool(r["answer"]["correct"])),
                "rating": r["feedback"]["rating"],
                "feedback_text": r["feedback"]["text"],
                "profile_version_after": r["profile_after"].get("version", 0),
                "update_error": (r.get("profile_update") or {}).get("error"),
            }
        )
    return pd.DataFrame(rows)


def _ols(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    design = np.column_stack([np.ones(len(x)), x])
    coef, *_ = np.linalg.lstsq(design, y, rcond=None)
    return coef


def trends(df: pd.DataFrame, n_boot: int = 1000, seed: int = 0) -> pd.DataFrame:
    """Per-condition slope over rounds, with a user-level bootstrap 95% CI.

    accuracy ~ round + divergence_percentile (linear probability model); rating ~ round;
    words ~ round.
    """
    rng = np.random.default_rng(seed)
    specs = {
        "accuracy_per_round (difficulty-adjusted)": (
            "correct",
            ["round", "divergence_percentile"],
        ),
        "rating_per_round": ("rating", ["round"]),
        "words_per_round": ("words", ["round"]),
    }
    out = []
    for cond, cdf in df.groupby("condition"):
        users = cdf["user_id"].unique()
        by_user = dict(list(cdf.groupby("user_id")))
        for name, (y, xs) in specs.items():
            est = _ols(cdf[xs].to_numpy(float), cdf[y].to_numpy(float))[1]
            boots = []
            for _ in range(n_boot):
                sample = pd.concat([by_user[u] for u in rng.choice(users, len(users))])
                boots.append(
                    _ols(sample[xs].to_numpy(float), sample[y].to_numpy(float))[1]
                )
            lo, hi = (
                np.percentile(boots, [2.5, 97.5])
                if len(users) > 1
                else (np.nan, np.nan)
            )
            out.append(
                {
                    "condition": cond,
                    "measure": name,
                    "slope": est,
                    "ci_low": lo,
                    "ci_high": hi,
                    "n_users": len(users),
                    "n_rounds": len(cdf),
                }
            )
    return pd.DataFrame(out)


def _label_line_ends(ax: Any, table: pd.DataFrame, col: str) -> None:
    """Direct-label each condition's last point, spreading labels that collide."""
    ends = []
    for cond in CONDITION_COLORS:
        sub = table[table["condition"] == cond]
        if not sub.empty:
            ends.append((float(sub.iloc[-1][col]), float(sub.iloc[-1]["round"]), cond))
    ends.sort()
    lo, hi = ax.get_ylim()
    gap = (hi - lo) * 0.07
    placed: list[float] = []
    for y, x, cond in ends:
        label_y = max(y, placed[-1] + gap) if placed else y
        placed.append(label_y)
        ax.annotate(
            cond.replace("_", " "),
            (x, y),
            xytext=(x + 0.15, label_y),
            textcoords="data",
            fontsize=7,
            color=TEXT_SECONDARY,
            va="center",
            annotation_clip=False,
        )


def plot_trends(table: pd.DataFrame, path: Path) -> None:
    """Accuracy, rating and length by round: three panels, one axis each."""
    panels = [
        ("accuracy", "A/B accuracy"),
        ("rating", "Mean satisfaction (1-5)"),
        ("words", "Explanation length (words)"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(14.5, 4), facecolor=SURFACE)
    limits = {"accuracy": (0, 1.05), "rating": (1, 5.2)}
    for ax, (col, title) in zip(axes, panels):
        ax.set_facecolor(SURFACE)
        for cond, color in CONDITION_COLORS.items():
            sub = table[table["condition"] == cond]
            if sub.empty:
                continue
            ax.plot(
                sub["round"],
                sub[col],
                color=color,
                linewidth=2,
                marker="o",
                markersize=5,
                markeredgecolor=SURFACE,
                markeredgewidth=2,
                label=cond,
            )
        if col in limits:
            ax.set_ylim(*limits[col])
        _label_line_ends(ax, table, col)
        ax.set_title(title, fontsize=10, color=TEXT_PRIMARY, loc="left")
        ax.set_xlabel("Round", fontsize=9, color=TEXT_SECONDARY)
        ax.grid(axis="y", color=GRID, linewidth=0.8)
        ax.tick_params(colors=TEXT_SECONDARY, labelsize=8)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(GRID)
    axes[0].legend(
        frameon=False, fontsize=8, loc="lower left", labelcolor=TEXT_SECONDARY
    )
    fig.tight_layout()
    fig.savefig(path, dpi=150, facecolor=SURFACE)
    plt.close(fig)


def profile_trace(records: list[dict[str, Any]]) -> str:
    """For each adaptive (user, condition): profile guidance -> explanation ->
    outcome."""
    lines: list[str] = []
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for r in records:
        groups.setdefault((r["user_id"], r["condition"]), []).append(r)
    for (user, cond), recs in sorted(groups.items()):
        if cond == "no_learning":
            continue
        persona = recs[0].get("participant", {}).get("persona")
        lines.append(
            f"### {user} / {cond}"
            + (f" (hidden persona: {persona})" if persona else "")
        )
        lines.append("")
        lines.append(
            "| round | guidance used for this explanation | words | bullets | correct "
            "| rating | feedback |"
        )
        lines.append("|---|---|---|---|---|---|---|")
        for r in sorted(recs, key=lambda r: r["round"]):
            guidance = (
                r["profile_before"].get("guidance", "")
                if r["explanation"]["used_profile"]
                else "(no profile)"
            )
            cells = [
                str(r["round"]),
                guidance or "(empty)",
                str(r["explanation"]["word_count"]),
                str(r["explanation"]["structure"]["bullets"]),
                str(r["answer"]["correct"]),
                str(r["feedback"]["rating"]),
                r["feedback"]["text"] or "",
            ]
            lines.append(
                "| "
                + " | ".join(c.replace("|", "/").replace("\n", " ") for c in cells)
                + " |"
            )
        final = max(recs, key=lambda r: r["round"])["profile_after"]
        lines.append("")
        lines.append("Final profile (preferences / struggles):")
        lines.append("")
        for key in ("preferences", "understood", "struggles"):
            for item in final.get(key, []):
                if isinstance(item, dict):
                    lines.append(
                        f"- *{key}* [{item['confidence']}, rounds "
                        f"{item['evidence']}]: {item['claim']}"
                    )
        for q in final.get("open_questions", []):
            lines.append(
                f"- *open question*: {q if isinstance(q, str) else json.dumps(q)}"
            )
        lines.append("")
    return "\n".join(lines)


def _fence(text: str, lang: str = "") -> str:
    """A code fence longer than any backtick run inside ``text``."""
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    ticks = "`" * max(3, longest + 1)
    return f"{ticks}{lang}\n{text}\n{ticks}"


def _item_changes(before: dict[str, Any], after: dict[str, Any]) -> list[str]:
    """Profile items added, removed or revised, matched by id within each list."""
    changes = []
    for key in ("preferences", "understood", "struggles", "open_questions"):
        old = {i.get("id"): i for i in before.get(key, []) if isinstance(i, dict)}
        new = {i.get("id"): i for i in after.get(key, []) if isinstance(i, dict)}
        for item_id in new.keys() - old.keys():
            n = new[item_id]
            changes.append(
                f"+ {key}/{item_id} [{n.get('confidence')}]: {n.get('claim')}"
            )
        for item_id in old.keys() - new.keys():
            changes.append(f"- {key}/{item_id} (removed)")
        for item_id in new.keys() & old.keys():
            o, n = old[item_id], new[item_id]
            if o.get("confidence") != n.get("confidence"):
                changes.append(
                    f"~ {key}/{item_id}: confidence {o.get('confidence')} -> "
                    f"{n.get('confidence')}"
                )
            if o.get("claim") != n.get("claim"):
                changes.append(f"~ {key}/{item_id}: claim -> {n.get('claim')}")
    return changes


def write_traces(records: list[dict[str, Any]], out_dir: Path) -> list[Path]:
    """One Markdown file per (condition, user) for reading the rounds by hand.

    For each round: the exact profile injected into the explanation prompt (as
    :func:`profile_for_prompt` renders it), the explanation it produced, the test,
    the feedback, and what the profile update changed.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for r in records:
        groups.setdefault((r["condition"], r["user_id"]), []).append(r)
    paths = []
    for (cond, user), recs in sorted(groups.items()):
        lines = [f"# Trace: participant {user}, condition {cond}", ""]
        for r in sorted(recs, key=lambda r: r["round"]):
            expl, test, ans = r["explanation"], r["test"], r["answer"]
            lines += [f"## Round {r['round'] + 1}: {r['policy_id']}", ""]
            if expl["used_profile"]:
                injected = profile_for_prompt(r["profile_before"])
                lines += [
                    f"**Profile injected:** version {expl['profile_version']} "
                    f"(written after round {r['round']}).",
                    "",
                    "**Guidance injected:**",
                    "",
                    "> " + (injected.get("guidance") or "(empty)"),
                    "",
                    "<details><summary>Full profile as injected</summary>",
                    "",
                    _fence(json.dumps(injected, indent=2), "json"),
                    "",
                    "</details>",
                    "",
                ]
            else:
                lines += ["**Profile injected:** none.", ""]
            lines += [
                f"**Explanation** ({expl['word_count']} words):",
                "",
                _fence(expl["text"], "markdown"),
                "",
                f"**Test:** {test['difficulty']}; target {test['target_policy_id']} vs. "
                f"distractor {test['distractor_policy_id']}; correct answer "
                f"{test['correct_label']}, answered {ans['label']} -> "
                f"{'correct' if ans['correct'] else 'incorrect'}.",
                "",
                f"**Feedback:** rating {r['feedback']['rating']}; comment: "
                f"{r['feedback']['text'] or '(none)'}",
                "",
            ]
            update = r.get("profile_update") or {}
            if update.get("performed"):
                changes = _item_changes(r["profile_before"], r["profile_after"])
                lines += [
                    f"**Profile update** (updater saw: "
                    f"{', '.join(update.get('visible_signals', []))}; "
                    f"error: {update.get('error')}):",
                    "",
                    _fence("\n".join(changes) or "(no item changes)"),
                    "",
                    "New guidance: "
                    + (r["profile_after"].get("guidance") or "(empty)"),
                    "",
                ]
            else:
                lines += ["**Profile update:** none (no-learning condition).", ""]
        path = out_dir / f"{cond}__{user}.md"
        path.write_text("\n".join(lines))
        paths.append(path)
    return paths


def main() -> None:
    """Write tables, figure and report for one study directory."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study_dir", type=Path)
    args = parser.parse_args()
    records = read_jsonl(args.study_dir / "rounds.jsonl")
    out = args.study_dir / "analysis"
    out.mkdir(exist_ok=True)
    df = flatten(records)
    df.to_csv(out / "rounds.csv", index=False)

    table = (
        df.groupby(["condition", "round"])
        .agg(
            accuracy=("correct", "mean"),
            rating=("rating", "mean"),
            words=("words", "mean"),
            difficulty_pct=("divergence_percentile", "mean"),
            n=("correct", "size"),
        )
        .reset_index()
    )
    table.to_csv(out / "by_condition_round.csv", index=False)
    trend = trends(df)
    trend.to_csv(out / "trends.csv", index=False)
    plot_trends(table, out / "trends.png")

    phase = df.assign(
        phase=np.where(df["is_eval_round"], "eval (held-out, last rounds)", "learning")
    )
    by_phase = phase.groupby(["condition", "phase"]).agg(
        accuracy=("correct", "mean"),
        rating=("rating", "mean"),
        words=("words", "mean"),
        n=("correct", "size"),
    )
    by_diff = df.pivot_table(
        index="condition", columns="difficulty", values="correct", aggfunc="mean"
    )
    report = [
        f"# Explanation study analysis: {args.study_dir.name}",
        "",
        f"{len(df)} rounds, {df['user_id'].nunique()} users, conditions: "
        f"{', '.join(sorted(df['condition'].unique()))}.",
        f"Profile-update parse errors: {int(df['update_error'].notna().sum())}.",
        "",
        "A/B accuracy is only a proxy for understanding (chance = 0.5). With few "
        "users these numbers "
        "describe this run, not a population.",
        "",
        "## Learning vs. held-out evaluation rounds",
        "",
        markdown_table(by_phase),
        "",
        "## Trends over rounds (slope per round; bootstrap 95% CI over users)",
        "",
        markdown_table(trend, index=False),
        "",
        "## Accuracy by test difficulty",
        "",
        "Difficulty is fixed by the test bank (divergence percentile within env); the "
        "schedule balances it "
        "across rounds, so mean difficulty per round should be flat (see "
        "by_condition_round.csv).",
        "",
        markdown_table(by_diff),
        "",
        "![trends](trends.png)",
        "",
        "## What was learned, and how it shaped the next explanation",
        "",
        profile_trace(records),
    ]
    (out / "report.md").write_text("\n".join(report))
    traces = write_traces(records, out / "traces")
    print(by_phase.round(3).to_string())
    print()
    print(trend.round(4).to_string(index=False))
    print(f"\nWrote {out}/report.md, trends.png and CSV tables")
    print(f"Per-participant traces ({len(traces)}) in {out}/traces/")


if __name__ == "__main__":
    main()
