"""Tests for A/B presentation, scoring, divergence and difficulty."""

import numpy as np
import pytest

from robocode.explanations.understanding import (
    PairTest,
    TestBank,
    _assign_difficulty,
    _spread,
    describe_test,
    present,
    trajectory_divergence,
)


def _pair() -> PairTest:
    return PairTest(
        test_id="t",
        env_name="E",
        policy_ids=("E/p", "E/q"),
        seed=1,
        object_count=2,
        videos={"E/p": "p.gif", "E/q": "q.gif"},
        divergence=0.3,
        stats={
            "per_policy": {
                "E/p": {
                    "solved": True,
                    "num_steps": 30,
                    "object_change_order": ["robot", "obstruction1"],
                },
                "E/q": {
                    "solved": True,
                    "num_steps": 50,
                    "object_change_order": ["robot", "obstruction0"],
                },
            }
        },
    )


@pytest.mark.parametrize("target", ["E/p", "E/q"])
@pytest.mark.parametrize("target_first", [True, False])
def test_presentation_answer_correctness(target: str, target_first: bool) -> None:
    """The correct label always points at the target's video, in either order."""
    pres = present(_pair(), target, target_first)
    assert pres.correct_label == ("A" if target_first else "B")
    assert pres.labels[pres.correct_label] == target
    assert pres.videos[pres.correct_label] == f"{target.split('/')[1]}.gif"
    wrong = "B" if pres.correct_label == "A" else "A"
    assert pres.is_correct(pres.correct_label) and not pres.is_correct(wrong)
    assert pres.distractor_policy_id != target
    with pytest.raises(ValueError):
        pres.is_correct("C")


def test_present_rejects_unrelated_target() -> None:
    """A test can only be shown for one of its two policies."""
    with pytest.raises(ValueError):
        present(_pair(), "E/other", True)


def test_divergence_properties() -> None:
    """Zero for identical, symmetric, larger for more different behaviour."""
    rng = np.random.default_rng(0)
    a = np.cumsum(rng.normal(size=(40, 3)), axis=0)
    b = a + np.array([0.0, 2.0, 0.0])
    c = a + np.array([0.0, 6.0, 0.0])
    assert trajectory_divergence(a, a) == pytest.approx(0.0)
    assert trajectory_divergence(a, b) == pytest.approx(trajectory_divergence(b, a))
    assert trajectory_divergence(a, c) > trajectory_divergence(a, b)
    # Different lengths are compared on normalized time.
    assert trajectory_divergence(a, a[::2]) < 0.2
    const = np.ones((10, 2))
    assert trajectory_divergence(const, const) == 0.0


def test_difficulty_bins_by_percentile() -> None:
    """Most similar rollouts are hard, most different are easy."""
    tests = [_pair() for _ in range(6)]
    for t, d in zip(tests, [0.9, 0.1, 0.5, 0.3, 0.7, 0.2]):
        t.divergence = d
    _assign_difficulty(tests)
    assert [t.difficulty for t in tests] == [
        "easy",
        "hard",
        "medium",
        "medium",
        "easy",
        "hard",
    ]
    assert (
        min(t.divergence_percentile for t in tests) > 0
        and max(t.divergence_percentile for t in tests) < 1
    )


def test_spread_picks_range_of_difficulties() -> None:
    """Selected tests span the divergence range rather than only the easiest."""
    candidates = [(d, i) for i, d in enumerate([0.1, 0.9, 0.5, 0.3, 0.7])]
    assert [c[0] for c in _spread(candidates, 2)] == [0.1, 0.9]
    assert len(_spread(candidates[:1], 3)) == 1


def test_describe_test_mentions_both_rollouts_not_ids() -> None:
    """The summary given to updaters describes behaviour, not policy identities."""
    text = describe_test(_pair(), "E/p")
    assert "30 steps" in text and "50 steps" in text
    assert "E/q" not in text


def test_bank_round_trip(tmp_path) -> None:
    """Saved banks load back identically and index tests by policy."""
    bank = TestBank(tmp_path, [_pair()])
    bank.save({"note": "x"})
    loaded = TestBank.load(tmp_path)
    assert loaded.tests["t"] == _pair()
    assert [t.test_id for t in loaded.tests_for("E/q")] == ["t"]
    assert loaded.policy_ids() == ["E/p", "E/q"]
