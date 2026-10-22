"""Understanding Evaluator: A/B rollout tests of whether a user can recognize a policy.

A test shows two rollouts from the same initial state: one of the explained
(target) policy and one of a different policy for the same task. The user picks
which one is the explained policy.

Tests are built offline into a *test bank* before any participant takes part,
from rollouts alone, so the questions cannot depend on any explanation
(no leakage from the explanation generator). The bank stores *pair tests*:
two policies on one initial state. Either policy can be the target, so one
pair test serves both of them.

Selection rules, aimed at non-trivial tests:

- Same outcome: both rollouts solve the task, or both fail
  (``require_same_outcome``), so "which one succeeded" is not a shortcut.
- Distinguishable: the two state trajectories must differ by at least
  ``min_divergence``. Identical behaviour cannot be told apart.
- Graded difficulty: each test's divergence is ranked against the other tests
  in its environment. A lower percentile means more similar rollouts, so the
  test is harder. That bin is logged with every answer, so later analysis can
  control for test difficulty.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import logging
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
from numpy.typing import NDArray

from robocode.explanations.policy_provider import (
    PolicyProvider,
    PolicyRecord,
    Rollout,
    RolloutEngine,
)
from robocode.utils.episode import save_video

logger = logging.getLogger(__name__)

DIFFICULTY_BINS = ("hard", "medium", "easy")  # low -> high divergence percentile


@dataclass
class PairTest:
    """Two policies' rollouts from one initial state, with rendered videos."""

    test_id: str
    env_name: str
    policy_ids: tuple[str, str]
    seed: int
    object_count: int | None
    videos: dict[str, str]  # policy_id -> video path relative to the bank dir
    divergence: float
    divergence_percentile: float = 0.0  # within env; set when the bank is built
    difficulty: str = "medium"
    stats: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> dict[str, Any]:
        """JSON-serializable form."""
        data = asdict(self)
        data["policy_ids"] = list(self.policy_ids)
        return data

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> PairTest:
        """Inverse of :meth:`to_json`."""
        data = dict(data)
        data["policy_ids"] = tuple(data["policy_ids"])
        return cls(**data)


@dataclass(frozen=True)
class ABPresentation:
    """One A/B question as shown to a participant."""

    test_id: str
    target_policy_id: str
    distractor_policy_id: str
    labels: dict[str, str]  # "A"/"B" -> policy_id
    videos: dict[str, str]  # "A"/"B" -> video path relative to the bank dir

    @property
    def correct_label(self) -> str:
        """The label whose rollout is the target policy."""
        return next(k for k, v in self.labels.items() if v == self.target_policy_id)

    def is_correct(self, answer: str) -> bool:
        """Score an answer ("A" or "B")."""
        if answer not in self.labels:
            raise ValueError(
                f"Answer must be one of {sorted(self.labels)}, got {answer!r}"
            )
        return answer == self.correct_label


def present(
    test: PairTest, target_policy_id: str, target_first: bool
) -> ABPresentation:
    """Make an A/B question with the target shown first (A) or second (B)."""
    if target_policy_id not in test.policy_ids:
        raise ValueError(f"{target_policy_id} is not part of test {test.test_id}")
    distractor = next(p for p in test.policy_ids if p != target_policy_id)
    order = (
        [target_policy_id, distractor]
        if target_first
        else [distractor, target_policy_id]
    )
    labels = dict(zip("AB", order))
    return ABPresentation(
        test_id=test.test_id,
        target_policy_id=target_policy_id,
        distractor_policy_id=distractor,
        labels=labels,
        videos={k: test.videos[v] for k, v in labels.items()},
    )


def describe_test(test: PairTest, target_policy_id: str) -> str:
    """A short behavioural summary of a test, for profile updates.

    Describes only the observable rollouts (no policy code, no explanation), so a
    learner can relate an error to the situation it occurred in.
    """
    distractor = next(p for p in test.policy_ids if p != target_policy_id)
    per = test.stats.get("per_policy", {})

    def one(pid: str) -> str:
        s = per.get(pid, {})
        order = s.get("object_change_order") or []
        moved = ", ".join(o for o in order[:4]) or "n/a"
        status = "solved" if s.get("solved") else "did not solve"
        return (
            f"{s.get('num_steps', '?')} steps, {status}, objects first changed: {moved}"
        )

    return (
        f"Difficulty {test.difficulty} (divergence percentile "
        f"{test.divergence_percentile:.2f} within {test.env_name}). "
        f"Explained policy: {one(target_policy_id)}. "
        f"Other policy: {one(distractor)}."
    )


def trajectory_divergence(
    a: NDArray[np.float64], b: NDArray[np.float64], num_points: int = 64
) -> float:
    """How different two state trajectories are, scale-free and length-agnostic.

    Both are resampled to ``num_points`` over normalized time; each feature is
    scaled by its pooled standard deviation (constant features are dropped); the
    result is the mean over time of the RMS per-feature difference.
    """
    if a.shape[1] != b.shape[1]:
        raise ValueError("trajectories must have the same feature dimension")
    ra, rb = _resample(a, num_points), _resample(b, num_points)
    pooled = np.concatenate([a, b])
    std = pooled.std(axis=0)
    keep = std > 1e-9
    if not keep.any():
        return 0.0
    diff = (ra[:, keep] - rb[:, keep]) / std[keep]
    return float(np.sqrt((diff**2).mean(axis=1)).mean())


def _resample(traj: NDArray[np.float64], num_points: int) -> NDArray[np.float64]:
    src = np.linspace(0.0, 1.0, len(traj))
    dst = np.linspace(0.0, 1.0, num_points)
    return np.stack(
        [np.interp(dst, src, traj[:, j]) for j in range(traj.shape[1])], axis=1
    )


def _rollout_stats(r: Rollout) -> dict[str, Any]:
    return {
        "solved": r.solved,
        "num_steps": r.num_steps,
        "object_change_order": r.object_change_order,
        "error": r.error,
    }


@dataclass
class TestBankConfig:
    """How to sample and filter A/B tests."""

    __test__ = False  # not a pytest test class

    seeds: list[int]
    object_counts: list[int | None] = field(default_factory=lambda: [None])
    max_steps: int = 400
    require_same_outcome: bool = True
    require_solved: bool = False
    min_divergence: float = 0.05
    tests_per_pair: int = 2
    frame_stride: int = 2
    fps: int = 15


class TestBank:
    """A stored set of pair tests, indexed by policy."""

    __test__ = False  # not a pytest test class

    def __init__(self, root: str | Path, tests: list[PairTest]) -> None:
        self.root = Path(root)
        self.tests = {t.test_id: t for t in tests}

    @classmethod
    def load(cls, root: str | Path) -> TestBank:
        """Load a bank written by :meth:`save`."""
        root = Path(root)
        lines = (root / "tests.jsonl").read_text().splitlines()
        return cls(
            root, [PairTest.from_json(json.loads(l)) for l in lines if l.strip()]
        )

    def save(self, build_info: dict[str, Any] | None = None) -> None:
        """Write ``tests.jsonl`` (and optional build provenance) under the root."""
        self.root.mkdir(parents=True, exist_ok=True)
        with open(self.root / "tests.jsonl", "w", encoding="utf-8") as f:
            for test in self.tests.values():
                f.write(json.dumps(test.to_json()) + "\n")
        if build_info is not None:
            (self.root / "build_info.json").write_text(json.dumps(build_info, indent=2))

    def tests_for(self, policy_id: str) -> list[PairTest]:
        """All tests in which ``policy_id`` appears, sorted by id."""
        return sorted(
            (t for t in self.tests.values() if policy_id in t.policy_ids),
            key=lambda t: t.test_id,
        )

    def policy_ids(self) -> list[str]:
        """Policies that have at least one test."""
        return sorted({p for t in self.tests.values() for p in t.policy_ids})


def build_test_bank(
    provider: PolicyProvider,
    engine: RolloutEngine,
    cfg: TestBankConfig,
    out_dir: str | Path,
    policy_ids: list[str] | None = None,
) -> TestBank:
    """Roll out every policy on every candidate state and keep good pair tests."""
    out_dir = Path(out_dir)
    policies = [
        p
        for p in provider.list_policies()
        if policy_ids is None or p.policy_id in policy_ids
    ]
    groups: dict[str, list[PolicyRecord]] = {}
    for p in policies:
        groups.setdefault(p.env_key, []).append(p)

    selected: list[PairTest] = []
    for group in groups.values():
        env_tests: list[PairTest] = []
        states = list(itertools.product(cfg.seeds, cfg.object_counts))
        rollouts: dict[tuple[str, int, int | None], Rollout] = {}
        for policy in group:
            for seed, count in states:
                rollouts[(policy.policy_id, seed, count)] = engine.rollout(
                    policy, seed, count, max_steps=cfg.max_steps
                )
            logger.info("Rolled out %s on %d states", policy.policy_id, len(states))
        for p1, p2 in itertools.combinations(group, 2):
            candidates = []
            for seed, count in states:
                r1 = rollouts[(p1.policy_id, seed, count)]
                r2 = rollouts[(p2.policy_id, seed, count)]
                if not _qualifies(r1, r2, cfg):
                    continue
                div = trajectory_divergence(r1.trajectory, r2.trajectory)
                if div >= cfg.min_divergence:
                    candidates.append((div, seed, count, r1, r2))
            for div, seed, count, r1, r2 in _spread(candidates, cfg.tests_per_pair):
                env_tests.append(_make_test(p1, p2, seed, count, div, r1, r2))
        _assign_difficulty(env_tests)
        selected.extend(env_tests)
        logger.info("%s: %d pair tests", group[0].env_name, len(env_tests))

    by_id = {p.policy_id: p for p in policies}
    for test in selected:
        for pid in test.policy_ids:
            path = out_dir / test.videos[pid]
            if path.exists():  # the same rollout can appear in several pair tests
                continue
            rollout = engine.rollout(
                by_id[pid],
                test.seed,
                test.object_count,
                max_steps=cfg.max_steps,
                render=True,
                frame_stride=cfg.frame_stride,
            )
            path.parent.mkdir(parents=True, exist_ok=True)
            save_video(rollout.frames, path, fps=cfg.fps)
    bank = TestBank(out_dir, selected)
    bank.save(
        build_info={
            "config": asdict(cfg),
            "policy_ids": [p.policy_id for p in policies],
        }
    )
    return bank


def _qualifies(r1: Rollout, r2: Rollout, cfg: TestBankConfig) -> bool:
    if r1.error or r2.error:
        return False
    if cfg.require_same_outcome and r1.solved != r2.solved:
        return False
    if cfg.require_solved and not (r1.solved and r2.solved):
        return False
    return True


def _spread(candidates: list[Any], k: int) -> list[Any]:
    """Up to ``k`` candidates evenly spaced in divergence rank (distinct seeds)."""
    candidates = sorted(candidates, key=lambda c: c[0])
    if len(candidates) <= k:
        return candidates
    idx = np.unique(np.linspace(0, len(candidates) - 1, k).round().astype(int))
    return [candidates[i] for i in idx]


def _make_test(
    p1: PolicyRecord,
    p2: PolicyRecord,
    seed: int,
    count: int | None,
    div: float,
    r1: Rollout,
    r2: Rollout,
) -> PairTest:
    key = f"{p1.policy_id}|{p2.policy_id}|{seed}|{count}"
    test_id = f"{p1.env_name}-{hashlib.sha1(key.encode()).hexdigest()[:10]}"
    videos = {
        p.policy_id: f"videos/{p.env_name}/{p.run_name}_seed{seed}_count{count}.gif"
        for p in (p1, p2)
    }
    return PairTest(
        test_id=test_id,
        env_name=p1.env_name,
        policy_ids=(p1.policy_id, p2.policy_id),
        seed=seed,
        object_count=count,
        videos=videos,
        divergence=div,
        stats={
            "per_policy": {
                p1.policy_id: _rollout_stats(r1),
                p2.policy_id: _rollout_stats(r2),
            },
            "both_solved": r1.solved and r2.solved,
            "change_order_differs": r1.object_change_order != r2.object_change_order,
            "step_ratio": max(r1.num_steps, r2.num_steps)
            / max(1, min(r1.num_steps, r2.num_steps)),
        },
    )


def _assign_difficulty(tests: list[PairTest]) -> None:
    """Percentile-rank divergence within one environment and bin into thirds."""
    if not tests:
        return
    order = np.argsort([t.divergence for t in tests], kind="stable")
    n = len(tests)
    for rank, i in enumerate(order):
        pct = (rank + 0.5) / n
        tests[i].divergence_percentile = pct
        tests[i].difficulty = DIFFICULTY_BINS[min(2, int(pct * 3))]
