"""Fixtures: a tiny synthetic policy archive, test bank and study context."""

from pathlib import Path

import pytest
import yaml
from omegaconf import OmegaConf

from robocode.explanations.logger import ExperimentLogger
from robocode.explanations.policy_provider import PolicyProvider
from robocode.explanations.study import StudyContext
from robocode.explanations.understanding import PairTest, TestBank
from robocode.explanations.user_model import UserMemoryStore

POLICY_TEMPLATE = '''"""Policy {i}: clear obstructions with a {algo} planner."""
import heapq

THRESHOLD = 0.{i}


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.plan = []

    def _make_plan(self, state):
        """Search for an order of obstructions to clear."""
        return []

    def _choose_grasp(self, state):
        """Pick the grasp offset that keeps the gripper clear of neighbouring objects."""
        return 0.0

    def _free_spot(self, state):
        """Find a free location on the floor to drop an obstruction, away from the target."""
        return 0.0

    def _path(self, a, b):
        """Plan a collision-free path between two poses with a plateau at safe height."""
        return [a, b]

    def _carry(self, state):
        """Move the held object along the planned path and release it at the goal."""
        return None

    def get_action(self, state):
        # replan whenever the current plan runs out or the scene has changed
        # obstructions are cleared in order of their overlap with the target surface
        # the block is placed last, centred on the target surface with a small gap
        # if a grasp fails the policy retries with a different grasp offset
        return None
'''

NUM_POLICIES = 6
ENV = "ToyEnv"


@pytest.fixture(name="archive")
def fixture_archive(tmp_path: Path) -> Path:
    """An agent_runs-style directory with NUM_POLICIES toy policies."""
    root = tmp_path / "archive"
    for i in range(NUM_POLICIES):
        evidence = root / "environments" / ENV / "runs" / f"run{i}" / "evidence"
        (evidence / "final").mkdir(parents=True)
        (evidence / "final" / "approach.py").write_text(
            POLICY_TEMPLATE.format(i=i, algo="best-first" if i % 2 else "greedy")
        )
        (evidence / "config.yaml").write_text(
            yaml.safe_dump(
                {
                    "environment": {"_target_": "toy.Env"},
                    "max_steps": 50,
                    "replicate_seed": i,
                }
            )
        )
        (evidence / "task.md").write_text("# ToyEnv\n\nPlace the block on the target.")
    return root


@pytest.fixture(name="bank")
def fixture_bank(tmp_path: Path) -> TestBank:
    """Pair tests over adjacent toy policies, spanning all difficulty bins."""
    ids = [f"{ENV}/run{i}" for i in range(NUM_POLICIES)]
    tests = []
    difficulties = ["hard", "medium", "easy"]
    for i in range(NUM_POLICIES):
        for k, j in enumerate([(i + 1) % NUM_POLICIES, (i + 2) % NUM_POLICIES]):
            diff = difficulties[(i + k) % 3]
            pct = {"hard": 0.15, "medium": 0.5, "easy": 0.85}[diff]
            tests.append(
                PairTest(
                    test_id=f"t{i}_{j}",
                    env_name=ENV,
                    policy_ids=(ids[i], ids[j]),
                    seed=100 + i,
                    object_count=None,
                    videos={ids[i]: f"videos/{i}.gif", ids[j]: f"videos/{j}.gif"},
                    divergence=pct,
                    divergence_percentile=pct,
                    difficulty=diff,
                    stats={"per_policy": {}},
                )
            )
    root = tmp_path / "bank"
    for i in range(NUM_POLICIES):
        (root / "videos").mkdir(parents=True, exist_ok=True)
        (root / "videos" / f"{i}.gif").write_bytes(b"GIF89a")
    bank = TestBank(root, tests)
    bank.save()
    return bank


@pytest.fixture(name="ctx")
def fixture_ctx(tmp_path: Path, archive: Path, bank: TestBank) -> StudyContext:
    """A mock-LLM study over the toy archive."""
    cfg = OmegaConf.create(
        {
            "study_id": "test_study",
            "study_seed": 7,
            "output_dir": str(tmp_path / "study"),
            "policy_root": str(archive),
            "envs": [ENV],
            "test_bank_dir": str(bank.root),
            "num_rounds": 5,
            "num_eval_rounds": 2,
            "balance_difficulty": True,
            "conditions": [
                "no_learning",
                "understanding_only",
                "understanding_preference",
            ],
            "explainer_llm": {"provider": "mock"},
            "updater_llm": {
                "provider": "mock",
                "api_key_env": "X",
                "auth_token": "secret",
            },
            "ui": {"show_explanation_during_test": False, "reveal_correctness": False},
        }
    )
    study_dir = Path(cfg.output_dir)
    return StudyContext(
        cfg=cfg,
        provider=PolicyProvider(archive),
        bank=TestBank.load(bank.root),
        memory=UserMemoryStore(study_dir / "memory"),
        logger=ExperimentLogger(study_dir),
    )
