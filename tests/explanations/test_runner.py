"""End-to-end session tests with the mock LLM and simulated participants."""

import json
from pathlib import Path

import pytest

from robocode.explanations.explanation_generator import (
    ExplanationGenerator,
    count_words,
)
from robocode.explanations.feedback import PreferenceFeedback, collect_feedback
from robocode.explanations.logger import read_jsonl
from robocode.explanations.mock_llm import MockLLMClient
from robocode.explanations.policy_provider import policy_from_path
from robocode.explanations.runner import build_schedule, run_simulated_session
from robocode.explanations.simulated_user import PERSONAS, SimulatedParticipant
from robocode.explanations.study import StudyContext, public_model_info

REQUIRED_FIELDS = {
    "user_id",
    "round",
    "env_name",
    "policy_id",
    "explanation",
    "test",
    "answer",
    "cumulative_accuracy",
    "feedback",
    "profile_before",
    "profile_after",
    "condition",
}


def _run(
    ctx: StudyContext, user: str, condition: str, persona: str = "concise_algorithmic"
):
    participant = SimulatedParticipant(PERSONAS[persona], seed=3)
    session = ctx.make_session(user, condition, participant.info())
    return run_simulated_session(session, participant, ctx.bank)


def test_schedule_is_paired_across_conditions_and_never_repeats(
    ctx: StudyContext,
) -> None:
    """Conditions see the same policies/tests; policies are held out within a user."""
    records = {c: _run(ctx, "u1", c) for c in ctx.cfg.conditions}
    keys = {
        c: [
            (r["policy_id"], r["test"]["test_id"], r["test"]["correct_label"])
            for r in recs
        ]
        for c, recs in records.items()
    }
    assert len({tuple(v) for v in keys.values()}) == 1
    policies = [k[0] for k in keys["no_learning"]]
    assert len(policies) == len(set(policies)) == ctx.cfg.num_rounds
    other = build_schedule(ctx.bank, 7, "u2", 5)
    assert [p.policy_id for p in other] != policies or [
        p.target_first for p in other
    ] != [k[2] == "A" for k in keys["no_learning"]]


def test_schedule_balances_difficulty(ctx: StudyContext) -> None:
    """Each block of three rounds has one test of each difficulty when available."""
    plans = build_schedule(ctx.bank, 7, "balance", 6)
    assert sorted(p.difficulty for p in plans[:3]) == ["easy", "hard", "medium"]
    assert sorted(p.difficulty for p in plans[3:]) == ["easy", "hard", "medium"]
    assert [
        p.is_eval_round for p in build_schedule(ctx.bank, 7, "x", 5, num_eval_rounds=2)
    ] == [False, False, False, True, True]
    with pytest.raises(ValueError):
        build_schedule(ctx.bank, 7, "x", 99)


def test_log_records_have_required_fields(ctx: StudyContext) -> None:
    """Every round is logged with everything needed for analysis."""
    _run(ctx, "u1", "understanding_preference")
    rows = read_jsonl(ctx.logger.study_dir / "rounds.jsonl")
    assert len(rows) == ctx.cfg.num_rounds
    for i, row in enumerate(rows):
        assert REQUIRED_FIELDS <= set(row)
        assert row["round"] == i
        text = row["explanation"]["text"]
        assert row["explanation"]["word_count"] == count_words(text)
        assert row["answer"]["correct"] == (
            row["answer"]["label"] == row["test"]["correct_label"]
        )
        assert row["test"]["labels"][row["test"]["correct_label"]] == row["policy_id"]
        assert row["explanation"]["model"] == {"provider": "mock"}
        assert 1 <= row["feedback"]["rating"] <= 5
    # The profile chain is consistent: each round starts from the last result.
    for prev, cur in zip(rows, rows[1:]):
        assert cur["profile_before"] == prev["profile_after"]
    acc = sum(r["answer"]["correct"] for r in rows) / len(rows)
    assert rows[-1]["cumulative_accuracy"] == pytest.approx(acc)
    events = [e["event"] for e in read_jsonl(ctx.logger.study_dir / "events.jsonl")]
    assert (
        events[0] == "session_start"
        and events.count("round_start") == ctx.cfg.num_rounds
    )


def test_no_learning_never_uses_or_writes_profile(ctx: StudyContext) -> None:
    """The baseline explains without user knowledge and stores no memory."""
    rows = _run(ctx, "u1", "no_learning")
    assert not any(r["explanation"]["used_profile"] for r in rows)
    assert not any(r["profile_update"]["performed"] for r in rows)
    assert not (ctx.memory.root / "no_learning").exists()


def test_adaptive_conditions_condition_explanations_after_round_one(
    ctx: StudyContext,
) -> None:
    """Round 0 has no prior knowledge; later rounds use the learned profile."""
    rows = _run(ctx, "u1", "understanding_preference")
    assert [r["explanation"]["used_profile"] for r in rows] == [False] + [True] * (
        len(rows) - 1
    )
    assert rows[0]["profile_update"]["visible_signals"] == [
        "env_name",
        "explanation",
        "explanation_words",
        "preference",
        "round",
        "understanding",
    ]
    u_only = _run(ctx, "u1", "understanding_only")
    assert "preference" not in u_only[0]["profile_update"]["visible_signals"]


def test_condition_and_user_memories_are_isolated(ctx: StudyContext) -> None:
    """Profiles differ by (user, condition) and never mix."""
    _run(ctx, "u1", "understanding_preference", "concise_algorithmic")
    _run(ctx, "u2", "understanding_preference", "detail_oriented")
    _run(ctx, "u1", "understanding_only", "concise_algorithmic")
    p_u1 = ctx.memory.load("u1", "understanding_preference")
    p_u2 = ctx.memory.load("u2", "understanding_preference")
    p_u1_only = ctx.memory.load("u1", "understanding_only")
    assert p_u1["preferences"] and p_u2["preferences"]
    assert p_u1["guidance"] != p_u2["guidance"]
    assert p_u1_only["preferences"] == []  # no preference signal in this condition


def test_preference_learning_adapts_explanations_to_persona(ctx: StudyContext) -> None:
    """With the mock LLM, a concise persona's explanations get shorter and use
    bullets."""
    rows = _run(ctx, "u1", "understanding_preference", "concise_algorithmic")
    assert rows[-1]["explanation"]["word_count"] < rows[0]["explanation"]["word_count"]
    assert rows[-1]["explanation"]["structure"]["bullets"] >= 3
    detail = _run(ctx, "u2", "understanding_preference", "detail_oriented")
    # The toy policies are short, so the mock explainer cannot write much more;
    # check the learned preference and that it did not get shorter.
    assert "more detailed" in detail[-1]["profile_before"]["guidance"]
    assert (
        detail[-1]["explanation"]["word_count"]
        >= detail[0]["explanation"]["word_count"]
    )


def test_session_state_machine_guards(ctx: StudyContext) -> None:
    """Out-of-order or repeated submissions are rejected."""
    session = ctx.make_session("u1", "understanding_preference")
    with pytest.raises(RuntimeError):
        session.submit_answer("A")
    state = session.start_round()
    assert session.start_round() is state  # idempotent: one explanation per round
    with pytest.raises(RuntimeError):
        session.submit_feedback(PreferenceFeedback(3))
    session.submit_answer("A")
    with pytest.raises(RuntimeError):
        session.submit_answer("B")
    session.submit_feedback(PreferenceFeedback(3))
    assert session.round_index == 1


def test_resume_continues_after_restart(ctx: StudyContext) -> None:
    """A new session object for the same user picks up at the next round."""
    first = ctx.make_session("u1", "understanding_preference")
    for _ in range(2):
        first.start_round()
        first.submit_answer("A")
        first.submit_feedback(PreferenceFeedback(4, "keep this style"))
    resumed = ctx.make_session("u1", "understanding_preference")
    assert resumed.round_index == 2
    assert resumed.profile["version"] == 2
    assert resumed.start_round().plan == first.schedule[2]


def test_feedback_validation() -> None:
    """Ratings must be integers 1-5; text is trimmed."""
    assert collect_feedback("4", "  shorter please ") == PreferenceFeedback(
        4, "shorter please"
    )
    for bad in ("0", "6", "x", None):
        with pytest.raises(ValueError):
            collect_feedback(bad)


def test_model_info_strips_secrets(ctx: StudyContext) -> None:
    """Credentials never reach the logs; the name of the key variable does."""
    info = public_model_info(ctx.cfg.updater_llm)
    assert info == {"provider": "mock", "api_key_env": "X"}
    assert "secret" not in json.dumps(info)


def test_config_rejects_key_in_api_key_env(ctx: StudyContext) -> None:
    """A pasted key is refused before the config is logged."""
    cfg = ctx.cfg.copy()
    cfg.updater_llm.api_key_env = "sk-proj-abc123-NOT-A-NAME"
    with pytest.raises(ValueError, match="must name an environment variable"):
        StudyContext.from_config(cfg)
    assert not (Path(cfg.output_dir) / "config.json").exists()


def test_config_rejects_too_many_rounds(ctx: StudyContext) -> None:
    """Startup fails clearly when the pool cannot fill the schedule."""
    cfg = ctx.cfg.copy()
    cfg.updater_llm.api_key_env = "X"
    cfg.num_rounds = 99
    with pytest.raises(ValueError, match="num_rounds=99"):
        StudyContext.from_config(cfg)


def test_learned_profile_reused_without_learning(ctx: StudyContext, tmp_path) -> None:
    """A saved profile conditions a new explanation of any approach.py, read-only."""
    _run(ctx, "u1", "understanding_preference", "concise_algorithmic")
    profile_path = (
        ctx.memory.path_for("u1", "understanding_preference") / "profile.json"
    )
    before = profile_path.read_text()
    profile = json.loads(before)
    approach = ctx.provider.list_policies()[0].approach_path
    copy = tmp_path / "my_policy.py"
    copy.write_text(approach.read_text())
    policy = policy_from_path(copy)
    generator = ExplanationGenerator(MockLLMClient())
    personal = generator.generate(policy, profile)
    plain = generator.generate(policy, None)
    assert personal.used_profile and not plain.used_profile
    assert personal.structure["bullets"] > plain.structure["bullets"]
    assert profile_path.read_text() == before  # nothing was learned or written
