"""Tests for profiles, condition filtering, memory isolation and the LLM updater."""

import json

import pytest

from robocode.explanations.mock_llm import MockLLMClient
from robocode.explanations.user_model import (
    CONDITIONS,
    LLMProfileUpdater,
    UserMemoryStore,
    empty_profile,
    get_condition,
    observation_for_update,
    parse_json_object,
    validate_profile,
)
from robocode.utils.llm import LLMResponse


def _full_obs(
    rnd: int = 0, text: str = "It was too long; around 150 words would be better."
) -> dict:
    return {
        "round": rnd,
        "env_name": "ToyEnv",
        "explanation": "Some explanation " * 100,
        "explanation_words": 200,
        "understanding": {
            "correct": False,
            "difficulty": "hard",
            "test_summary": "...",
        },
        "preference": {"rating": 2, "text": text},
    }


def test_condition_filter_hides_unused_signals() -> None:
    """Each condition's updater sees only its signals."""
    full = _full_obs()
    u_only = observation_for_update(full, get_condition("understanding_only"))
    assert "understanding" in u_only and "preference" not in u_only
    both = observation_for_update(full, get_condition("understanding_preference"))
    assert both["preference"]["text"] == full["preference"]["text"]
    none = observation_for_update(full, get_condition("no_learning"))
    assert "understanding" not in none and "preference" not in none
    # Filtering copies, so an updater cannot mutate the logged record.
    both["understanding"]["correct"] = True
    assert full["understanding"]["correct"] is False


def test_unknown_condition() -> None:
    """Typos in condition names fail loudly."""
    with pytest.raises(ValueError):
        get_condition("understanding+preference")


def test_understanding_only_prompt_never_contains_feedback() -> None:
    """The preference text and rating cannot reach the understanding-only updater."""
    llm = MockLLMClient()
    updater = LLMProfileUpdater(llm)
    cond = CONDITIONS["understanding_only"]
    secret = "PLEASE-USE-BULLETS-xyz"
    updater.update(
        empty_profile(), observation_for_update(_full_obs(text=secret), cond), cond
    )
    assert secret not in llm.prompts[-1]
    assert '"rating"' not in llm.prompts[-1]
    assert "do not observe the person's ratings" in llm.prompts[-1]


def test_mock_updater_accumulates_evidence_and_confidence() -> None:
    """Repeated consistent feedback raises confidence; one round stays low."""
    updater = LLMProfileUpdater(MockLLMClient())
    cond = CONDITIONS["understanding_preference"]
    profile = empty_profile()
    confidences = []
    for rnd in range(3):
        profile, meta = updater.update(
            profile, observation_for_update(_full_obs(rnd), cond), cond
        )
        assert meta["error"] is None
        length = next(i for i in profile["preferences"] if i["id"] == "length")
        confidences.append(length["confidence"])
    assert confidences == ["low", "medium", "high"]
    assert length["evidence"] == [0, 1, 2]
    assert "150 words" in profile["guidance"]
    assert profile["version"] == 3 and profile["updated_after_round"] == 2


class _BrokenLLM:
    def complete(self, messages):  # pylint: disable=unused-argument
        """Return text with no JSON in it."""
        return LLMResponse(text="Sorry, I cannot do that.")


def test_unparseable_update_keeps_previous_profile() -> None:
    """A bad LLM reply is logged as an error and does not corrupt memory."""
    before = empty_profile()
    before["guidance"] = "keep me"
    cond = CONDITIONS["understanding_preference"]
    after, meta = LLMProfileUpdater(_BrokenLLM()).update(
        before, observation_for_update(_full_obs(), cond), cond
    )
    assert after == before and after is not before
    assert meta["error"]


def test_validate_profile_coerces_schema() -> None:
    """Malformed items are dropped and unknown confidences become low."""
    raw = parse_json_object(
        "```json\n"
        + json.dumps(
            {
                "summary": "s",
                "preferences": [
                    {
                        "claim": "Likes short",
                        "confidence": "very high",
                        "evidence": [1, "x"],
                    },
                    3,
                ],
                "understood": [],
                "struggles": [],
                "open_questions": ["Is format important?"],
            }
        )
        + "\n```"
    )
    out = validate_profile(raw, fallback={"guidance": "old"})
    assert out["preferences"] == [
        {
            "id": "likes-short",
            "claim": "Likes short",
            "evidence": [1],
            "confidence": "low",
        }
    ]
    assert out["guidance"] == "old"
    assert out["open_questions"] == ["Is format important?"]


def test_memory_isolated_by_user_and_condition(tmp_path) -> None:
    """Writing one (user, condition) never changes another's profile."""
    store = UserMemoryStore(tmp_path)
    profile = empty_profile()
    profile.update(version=1, guidance="u1 likes bullets")
    store.save("u1", "understanding_preference", profile)
    assert (
        store.load("u1", "understanding_preference")["guidance"] == "u1 likes bullets"
    )
    assert store.load("u2", "understanding_preference") == empty_profile()
    assert store.load("u1", "understanding_only") == empty_profile()
    assert (
        tmp_path / "understanding_preference" / "u1" / "versions" / "v001.json"
    ).exists()


def test_memory_rejects_path_traversal(tmp_path) -> None:
    """User ids cannot escape the memory root."""
    with pytest.raises(ValueError):
        UserMemoryStore(tmp_path).path_for("../other", "no_learning")
