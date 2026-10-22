"""Experiment Runner: schedules and runs multi-round explanation sessions.

A :class:`StudySession` is one participant in one condition. It is a small
state machine (explanation -> test -> feedback -> next round), so the same
object drives both the simulated loop (:func:`run_simulated_session`) and the
web interface.

The round schedule (policy, test, A/B order, difficulty) depends only on
``(study seed, user_id)``, not on the condition. A simulated persona run under
all three conditions therefore sees identical policies and questions, and
condition differences come only from adaptation. Policies are not repeated
within a session, so every explanation and test is for a policy the system has
not explained to this user before (held out from the profile).
"""

from __future__ import annotations

import copy
import hashlib
import time
from dataclasses import asdict, dataclass, field
from typing import Any, Protocol

import numpy as np

from robocode.explanations.explanation_generator import (
    Explanation,
    ExplanationGenerator,
)
from robocode.explanations.feedback import PreferenceFeedback
from robocode.explanations.logger import ExperimentLogger
from robocode.explanations.policy_provider import PolicyProvider
from robocode.explanations.understanding import (
    DIFFICULTY_BINS,
    ABPresentation,
    PairTest,
    TestBank,
    describe_test,
    present,
)
from robocode.explanations.user_model import (
    Condition,
    ProfileUpdater,
    UserMemoryStore,
    observation_for_update,
)

AB_QUESTION = "Which rollout shows the policy that was just explained to you?"


@dataclass(frozen=True)
class RoundPlan:
    """What a participant sees in one round, fixed before the session starts."""

    round_index: int
    policy_id: str
    test_id: str
    target_first: bool
    difficulty: str
    is_eval_round: bool


def schedule_seed(study_seed: int, user_id: str) -> int:
    """A per-user seed that does not depend on the condition."""
    digest = hashlib.sha256(f"{study_seed}:{user_id}".encode()).hexdigest()
    return int(digest[:12], 16)


def build_schedule(
    bank: TestBank,
    study_seed: int,
    user_id: str,
    num_rounds: int,
    policy_ids: list[str] | None = None,
    num_eval_rounds: int = 0,
    balance_difficulty: bool = True,
) -> list[RoundPlan]:
    """Sample a non-repeating policy sequence and one test per round.

    With ``balance_difficulty``, difficulty bins are assigned to rounds in
    shuffled blocks (one of each bin per block), so test difficulty does not
    drift across rounds and change in accuracy over rounds is not just an
    artifact of easier questions. The last ``num_eval_rounds`` rounds are flagged
    for held-out evaluation.
    """
    rng = np.random.default_rng(schedule_seed(study_seed, user_id))
    pool = sorted(set(bank.policy_ids()) & set(policy_ids or bank.policy_ids()))
    if num_rounds > len(pool):
        raise ValueError(
            f"num_rounds={num_rounds} exceeds {len(pool)} testable policies"
        )
    order = [pool[i] for i in rng.permutation(len(pool))[:num_rounds]]
    bins: list[str] = []
    while len(bins) < num_rounds:
        bins.extend(DIFFICULTY_BINS[i] for i in rng.permutation(len(DIFFICULTY_BINS)))
    plans = []
    for r, policy_id in enumerate(order):
        tests = bank.tests_for(policy_id)
        if balance_difficulty:
            tests = _closest_difficulty(tests, bins[r])
        test = tests[int(rng.integers(len(tests)))]
        plans.append(
            RoundPlan(
                round_index=r,
                policy_id=policy_id,
                test_id=test.test_id,
                target_first=bool(rng.integers(2)),
                difficulty=test.difficulty,
                is_eval_round=r >= num_rounds - num_eval_rounds,
            )
        )
    return plans


def _closest_difficulty(tests: list[PairTest], wanted: str) -> list[PairTest]:
    rank = DIFFICULTY_BINS.index(wanted)
    best = min(abs(DIFFICULTY_BINS.index(t.difficulty) - rank) for t in tests)
    return [t for t in tests if abs(DIFFICULTY_BINS.index(t.difficulty) - rank) == best]


@dataclass
class RoundState:
    """In-progress data for the current round."""

    plan: RoundPlan
    explanation: Explanation
    presentation: ABPresentation
    profile_before: dict[str, Any]
    started_at: float
    answer: str | None = None
    correct: bool | None = None
    answered_at: float | None = None
    test_shown_at: float | None = None
    extra: dict[str, Any] = field(default_factory=dict)


class StudySession:
    """One participant, one condition, a fixed schedule of rounds."""

    def __init__(
        self,
        *,
        study_id: str,
        user_id: str,
        condition: Condition,
        schedule: list[RoundPlan],
        provider: PolicyProvider,
        bank: TestBank,
        generator: ExplanationGenerator,
        updater: ProfileUpdater | None,
        memory: UserMemoryStore,
        logger: ExperimentLogger,
        participant_info: dict[str, Any] | None = None,
    ) -> None:
        if condition.adapt and updater is None:
            raise ValueError(
                f"Condition {condition.name} adapts but no updater was given"
            )
        self.study_id = study_id
        self.user_id = user_id
        self.condition = condition
        self.schedule = schedule
        self._provider = provider
        self._bank = bank
        self._generator = generator
        self._updater = updater
        self._memory = memory
        self._logger = logger
        self._participant_info = dict(participant_info or {})
        self._num_correct = 0
        self.round_index = 0
        self.current: RoundState | None = None
        self._logger.log_event(
            "session_start",
            study_id=study_id,
            user_id=user_id,
            condition=condition.name,
            schedule=[asdict(p) for p in schedule],
        )

    def resume(self, completed: list[dict[str, Any]]) -> None:
        """Skip rounds already logged for this user and condition (after a restart).

        The profile is persisted after each round, so only the round counter and running
        accuracy need restoring. A round interrupted mid-way is restarted.
        """
        planned = [p.policy_id for p in self.schedule[: len(completed)]]
        if [r["policy_id"] for r in completed] != planned:
            raise RuntimeError(
                f"Logged rounds for {self.user_id} do not match the schedule"
            )
        self.round_index = len(completed)
        self._num_correct = sum(bool(r["answer"]["correct"]) for r in completed)

    @property
    def done(self) -> bool:
        """Whether every scheduled round has been completed."""
        return self.round_index >= len(self.schedule)

    @property
    def profile(self) -> dict[str, Any]:
        """This user's current profile in this condition."""
        return self._memory.load(self.user_id, self.condition.name)

    def start_round(self) -> RoundState:
        """Generate the explanation for the next round (idempotent per round)."""
        if self.done:
            raise RuntimeError("Session is complete")
        if self.current is not None:
            return self.current
        plan = self.schedule[self.round_index]
        policy = self._provider.get(plan.policy_id)
        profile = self.profile
        conditioned = self.condition.adapt and profile.get("version", 0) > 0
        explanation = self._generator.generate(policy, profile if conditioned else None)
        self.current = RoundState(
            plan=plan,
            explanation=explanation,
            presentation=present(
                self._bank.tests[plan.test_id], plan.policy_id, plan.target_first
            ),
            profile_before=copy.deepcopy(profile),
            started_at=time.time(),
        )
        self._logger.log_event(
            "round_start",
            user_id=self.user_id,
            condition=self.condition.name,
            round=plan.round_index,
            policy_id=plan.policy_id,
        )
        return self.current

    def mark_test_shown(self) -> None:
        """Record when the participant finished reading and opened the test."""
        state = self._require_state()
        if state.test_shown_at is None:
            state.test_shown_at = time.time()

    def submit_answer(self, label: str) -> bool:
        """Score the A/B answer.

        It cannot be changed once submitted.
        """
        state = self._require_state()
        if state.answer is not None:
            raise RuntimeError("Answer already submitted for this round")
        state.correct = state.presentation.is_correct(label)
        state.answer = label
        state.answered_at = time.time()
        return state.correct

    def submit_feedback(self, feedback: PreferenceFeedback) -> dict[str, Any]:
        """Finish the round: update the profile (per condition), log, advance."""
        state = self._require_state()
        if state.answer is None or state.correct is None:
            raise RuntimeError("Submit the A/B answer before feedback")
        self._num_correct += int(state.correct)
        test = self._bank.tests[state.plan.test_id]
        full_obs = {
            "round": state.plan.round_index,
            "env_name": test.env_name,
            "explanation": state.explanation.text,
            "explanation_words": state.explanation.word_count,
            "understanding": {
                "correct": state.correct,
                "difficulty": test.difficulty,
                "test_summary": describe_test(test, state.plan.policy_id),
            },
            "preference": feedback.to_json(),
        }
        update_meta: dict[str, Any] = {"performed": False}
        profile_after = state.profile_before
        if self.condition.adapt:
            assert self._updater is not None
            visible = observation_for_update(full_obs, self.condition)
            profile_after, meta = self._updater.update(
                state.profile_before, visible, self.condition
            )
            self._memory.save(self.user_id, self.condition.name, profile_after)
            update_meta = {
                "performed": True,
                "visible_signals": sorted(visible),
                **meta,
            }
        record = self._round_record(state, test, feedback, profile_after, update_meta)
        self._logger.log_round(record)
        self.round_index += 1
        self.current = None
        return record

    def _round_record(
        self,
        state: RoundState,
        test: PairTest,
        feedback: PreferenceFeedback,
        profile_after: dict[str, Any],
        update_meta: dict[str, Any],
    ) -> dict[str, Any]:
        expl = state.explanation
        pres = state.presentation
        n_done = self.round_index + 1
        policy = self._provider.get(state.plan.policy_id)
        return {
            "study_id": self.study_id,
            "user_id": self.user_id,
            "condition": self.condition.name,
            "round": state.plan.round_index,
            "is_eval_round": state.plan.is_eval_round,
            "participant": self._participant_info,
            "env_name": policy.env_name,
            "policy_id": policy.policy_id,
            "policy_metadata": policy.metadata,
            "explanation": {
                "text": expl.text,
                "word_count": expl.word_count,
                "char_count": expl.char_count,
                "structure": expl.structure,
                "used_profile": expl.used_profile,
                "profile_version": expl.profile_version,
                "prompt_sha1": expl.prompt_sha1,
                "latency_s": expl.latency_s,
                "cost_usd": expl.cost_usd,
                "model": expl.model,
            },
            "test": {
                "test_id": test.test_id,
                "question": AB_QUESTION,
                "target_policy_id": pres.target_policy_id,
                "distractor_policy_id": pres.distractor_policy_id,
                "labels": pres.labels,
                "videos": pres.videos,
                "seed": test.seed,
                "object_count": test.object_count,
                "difficulty": test.difficulty,
                "divergence": test.divergence,
                "divergence_percentile": test.divergence_percentile,
                "stats": test.stats,
                "correct_label": pres.correct_label,
            },
            "answer": {
                "label": state.answer,
                "correct": state.correct,
                "reading_time_s": _dt(state.started_at, state.test_shown_at),
                "answer_time_s": _dt(
                    state.test_shown_at or state.started_at, state.answered_at
                ),
            },
            "cumulative_accuracy": self._num_correct / n_done,
            "feedback": feedback.to_json(),
            "profile_before": state.profile_before,
            "profile_after": profile_after,
            "profile_update": update_meta,
            "completed_at": time.time(),
        }

    def _require_state(self) -> RoundState:
        if self.current is None:
            raise RuntimeError("No round in progress; call start_round() first")
        return self.current


def _dt(start: float | None, end: float | None) -> float | None:
    return None if start is None or end is None else end - start


class Participant(Protocol):
    """Anything that can take part in a session without a UI (e.g. a simulator)."""

    def answer(
        self, explanation: Explanation, presentation: ABPresentation, test: PairTest
    ) -> str:
        """Return "A" or "B"."""

    def feedback(self, explanation: Explanation) -> PreferenceFeedback:
        """Return a satisfaction rating and optional comment."""


def run_simulated_session(
    session: StudySession, participant: Participant, bank: TestBank
) -> list[dict[str, Any]]:
    """Drive a session to completion with a non-interactive participant."""
    records = []
    while not session.done:
        state = session.start_round()
        session.mark_test_shown()
        test = bank.tests[state.plan.test_id]
        session.submit_answer(
            participant.answer(state.explanation, state.presentation, test)
        )
        records.append(session.submit_feedback(participant.feedback(state.explanation)))
    return records
