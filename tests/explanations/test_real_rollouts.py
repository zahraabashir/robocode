"""Integration test: build a tiny test bank from real agent_runs policies.

Skipped when the agent_runs archive is not present (it is not tracked in git).
"""

from pathlib import Path

import pytest

from robocode.explanations.policy_provider import PolicyProvider, RolloutEngine
from robocode.explanations.understanding import TestBankConfig, build_test_bank

ARCHIVE = Path(__file__).resolve().parents[2] / "agent_runs"

pytestmark = pytest.mark.skipif(
    not (ARCHIVE / "environments").exists(), reason="agent_runs archive not present"
)


def test_rollouts_and_bank_from_real_policies(tmp_path: Path) -> None:
    """Two Obstruction2D policies, three seeds: rollouts run and tests qualify."""
    provider = PolicyProvider(ARCHIVE, envs=["Obstruction2D"])
    policies = provider.list_policies()[:2]
    assert all(p.metadata["approach_lines"] > 50 for p in policies)
    assert provider.same_env(policies[0])  # comparable policies exist

    engine = RolloutEngine()
    rollout = engine.rollout(
        policies[0], seed=101, max_steps=200, render=True, frame_stride=5
    )
    assert rollout.error is None and rollout.num_steps > 0
    assert rollout.trajectory.shape[0] == rollout.num_steps + 1
    assert "robot" in rollout.object_change_order
    assert rollout.frames and rollout.frames[0].ndim == 3

    cfg = TestBankConfig(
        seeds=[101, 102, 103], max_steps=200, tests_per_pair=2, frame_stride=5
    )
    bank = build_test_bank(
        provider, engine, cfg, tmp_path / "bank", [p.policy_id for p in policies]
    )
    for test in bank.tests.values():
        per = test.stats["per_policy"]
        assert (
            len({s["solved"] for s in per.values()}) == 1
        )  # same outcome: no trivial tests
        assert test.divergence >= cfg.min_divergence
        for video in test.videos.values():
            assert (bank.root / video).stat().st_size > 0
    assert (tmp_path / "bank" / "tests.jsonl").exists()
