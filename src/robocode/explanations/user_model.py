"""User Model / Memory: a persistent, inspectable profile per user and condition.

The profile is a small JSON document that an LLM rewrites after every round.
It has no fixed preference categories: every learned item is a free-text claim
with the rounds that support it and a confidence level, so one can trace what
was learned and from which interactions.

Which signals the updater may use is decided by the :class:`Condition`.
:func:`observation_for_update` removes the unused signals *before* the updater
sees the round, so a condition cannot leak signals it should not use.
Memories are stored under ``<root>/<condition>/<user_id>/``, so users and
conditions never share a profile.

To replace this learner (e.g. with a contextual bandit), implement
:class:`ProfileUpdater` and keep the same observation format.
"""

from __future__ import annotations

import copy
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from robocode.utils.llm import LLMClient

PROFILE_LIST_KEYS = ("preferences", "understood", "struggles", "open_questions")
CONFIDENCE_LEVELS = ("low", "medium", "high")


def empty_profile() -> dict[str, Any]:
    """The profile before any interaction."""
    return {
        "version": 0,
        "updated_after_round": None,
        "summary": "No interactions yet; nothing is known about this person.",
        # Each item: {"id": slug, "claim": str, "evidence": [round, ...],
        #             "confidence": "low" | "medium" | "high"}
        "preferences": [],  # how they like explanations
        "understood": [],  # concepts/policy aspects they appear to grasp
        "struggles": [],  # concepts/aspects they appear to miss
        "open_questions": [],  # uncertainties worth resolving; free text
        "guidance": "",  # short advice to the explainer for the next policy
    }


@dataclass(frozen=True)
class Condition:
    """An experimental condition: which signals adaptation may use."""

    name: str
    adapt: bool  # whether a profile is learned and given to the explainer
    use_understanding: bool
    use_preference: bool


CONDITIONS: dict[str, Condition] = {
    "no_learning": Condition(
        "no_learning", adapt=False, use_understanding=False, use_preference=False
    ),
    "understanding_only": Condition(
        "understanding_only", adapt=True, use_understanding=True, use_preference=False
    ),
    "understanding_preference": Condition(
        "understanding_preference",
        adapt=True,
        use_understanding=True,
        use_preference=True,
    ),
}


def get_condition(name: str) -> Condition:
    """Look up a condition by name."""
    if name not in CONDITIONS:
        raise ValueError(
            f"Unknown condition {name!r}; expected one of {sorted(CONDITIONS)}"
        )
    return CONDITIONS[name]


def observation_for_update(
    full: dict[str, Any], condition: Condition
) -> dict[str, Any]:
    """The part of a round record a condition's updater is allowed to see.

    ``full`` has keys ``round``, ``env_name``, ``explanation`` (text),
    ``explanation_words``, ``understanding`` (``correct``, ``difficulty``,
    ``test_summary``) and ``preference`` (``rating``, ``text``).
    """
    obs = {
        "round": full["round"],
        "env_name": full["env_name"],
        "explanation": full["explanation"],
        "explanation_words": full["explanation_words"],
    }
    if condition.use_understanding:
        obs["understanding"] = copy.deepcopy(full["understanding"])
    if condition.use_preference:
        obs["preference"] = copy.deepcopy(full["preference"])
    return obs


class ProfileUpdater(Protocol):
    """Anything that turns (profile, observation) into a new profile."""

    def update(
        self, profile: dict[str, Any], observation: dict[str, Any], condition: Condition
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """Return ``(new_profile, update_metadata)``."""


UPDATE_TEMPLATE = """\
You maintain a profile of one person. The profile is used to tailor \
explanations of robot control policies to this person. Each round, a different \
policy (a program written by a coding agent) was explained to them. Below are \
the previous profile and what happened in the latest round. Return the \
updated profile.

What you can observe in this study: {signals}.
{signal_notes}
Rules:
- Record only what the evidence supports. One round is weak evidence: a claim \
supported by a single round has confidence "low". Raise confidence only when \
several rounds agree; lower or remove claims that later rounds contradict.
- Each list item is {{"id": short-slug, "claim": text, "evidence": [round \
numbers], "confidence": "low"|"medium"|"high"}}. Keep ids stable when you \
revise a claim, and add the new round to its evidence.
- Describe this person, not the specific policy or task, unless the evidence \
is only about that task (then say so).
- Do not assume more detail is always better. Only infer preferences about \
length, structure, focus or style from evidence.
- Use "open_questions" for what is still uncertain about how to explain things \
to this person.
- "guidance" is advice to whoever explains the next policy, under 120 words. \
"summary" is at most 3 sentences.
- At most 8 items per list. Merge overlapping items.

<previous_profile>
{profile_json}
</previous_profile>

<round_observation>
{observation_json}
</round_observation>

Return only a JSON object with exactly these keys: "summary", "preferences", \
"understood", "struggles", "open_questions", "guidance"."""

UNDERSTANDING_NOTE = (
    "- Understanding is measured by an A/B test: the person watched two rollouts "
    "from the same start state, one of the explained policy and one of a different "
    "policy, and picked which was the explained one. Chance is 50%, so a single "
    "answer is noisy, and the test summary gives its difficulty. Getting it right "
    "does not mean they liked the explanation.\n"
)
PREFERENCE_NOTE = (
    "- Preference is a 1-5 satisfaction rating and an optional comment. Liking an "
    "explanation does not mean it was effective, and a comment about one "
    "explanation may not generalize.\n"
)


class LLMProfileUpdater:
    """Rewrites the profile with an LLM; keeps the old profile if parsing fails."""

    def __init__(
        self, llm: LLMClient, model_info: dict[str, Any] | None = None
    ) -> None:
        self._llm = llm
        self.model_info = dict(model_info or {})

    def build_prompt(
        self, profile: dict[str, Any], observation: dict[str, Any], condition: Condition
    ) -> str:
        """The exact update prompt."""
        signals = ["the explanation they were given"]
        notes = ""
        if condition.use_understanding:
            signals.append("whether they passed an understanding test")
            notes += UNDERSTANDING_NOTE
        if condition.use_preference:
            signals.append("their satisfaction rating and comments")
            notes += PREFERENCE_NOTE
        else:
            notes += "- You do not observe the person's ratings or comments.\n"
        visible = {
            k: v
            for k, v in profile.items()
            if k not in ("version", "updated_after_round")
        }
        return UPDATE_TEMPLATE.format(
            signals="; ".join(signals),
            signal_notes=notes,
            profile_json=json.dumps(visible, indent=2),
            observation_json=json.dumps(observation, indent=2),
        )

    def update(
        self, profile: dict[str, Any], observation: dict[str, Any], condition: Condition
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """Ask the LLM for a new profile given the visible observation."""
        prompt = self.build_prompt(profile, observation, condition)
        start = time.monotonic()
        response = self._llm.complete([{"role": "user", "content": prompt}])
        meta: dict[str, Any] = {
            "latency_s": time.monotonic() - start,
            "cost_usd": response.cost_usd,
            "model": self.model_info,
            "raw_response": response.text,
            "error": None,
        }
        try:
            new = validate_profile(parse_json_object(response.text), fallback=profile)
        except ValueError as exc:
            meta["error"] = str(exc)
            return copy.deepcopy(profile), meta
        new["version"] = profile.get("version", 0) + 1
        new["updated_after_round"] = observation["round"]
        return new, meta


def parse_json_object(text: str) -> dict[str, Any]:
    """Parse the first JSON object in an LLM reply (tolerates code fences)."""
    fenced = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.DOTALL)
    candidate = (
        fenced.group(1) if fenced else text[text.find("{") : text.rfind("}") + 1]
    )
    try:
        data = json.loads(candidate)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Profile update is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Profile update is not a JSON object")
    return data


def validate_profile(data: dict[str, Any], fallback: dict[str, Any]) -> dict[str, Any]:
    """Coerce an updater's output to the profile schema.

    Missing keys are copied from ``fallback``; malformed list items are dropped;
    unknown confidence levels become "low".
    """
    out = empty_profile()
    for key in ("summary", "guidance"):
        value = data.get(key, fallback.get(key, ""))
        out[key] = value if isinstance(value, str) else json.dumps(value)
    for key in PROFILE_LIST_KEYS:
        items = data.get(key, fallback.get(key, []))
        if not isinstance(items, list):
            raise ValueError(f"Profile field {key!r} must be a list")
        out[key] = [_clean_item(i) for i in items if _clean_item(i) is not None][:8]
    return out


def _clean_item(item: Any) -> Any:
    if isinstance(item, str):
        return item  # open_questions may be plain strings
    if not isinstance(item, dict) or not isinstance(item.get("claim"), str):
        return None
    confidence = item.get("confidence", "low")
    evidence = item.get("evidence", [])
    return {
        "id": str(item.get("id") or _slug(item["claim"])),
        "claim": item["claim"],
        "evidence": (
            [e for e in evidence if isinstance(e, int)]
            if isinstance(evidence, list)
            else []
        ),
        "confidence": confidence if confidence in CONFIDENCE_LEVELS else "low",
    }


def _slug(text: str) -> str:
    return "-".join(re.findall(r"[a-z0-9]+", text.lower())[:5]) or "item"


class UserMemoryStore:
    """Profiles on disk, isolated by condition and user.

    ``<root>/<condition>/<user_id>/profile.json`` holds the current profile and
    ``versions/vNNN.json`` every past version.
    """

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)

    def path_for(self, user_id: str, condition: str) -> Path:
        """Directory for one (user, condition) memory."""
        for part in (user_id, condition):
            if not re.fullmatch(r"[A-Za-z0-9_.-]+", part) or part in (".", ".."):
                raise ValueError(f"Unsafe identifier for a memory path: {part!r}")
        return self.root / condition / user_id

    def load(self, user_id: str, condition: str) -> dict[str, Any]:
        """The current profile (empty if this user has none in this condition)."""
        path = self.path_for(user_id, condition) / "profile.json"
        if not path.exists():
            return empty_profile()
        profile: dict[str, Any] = json.loads(path.read_text())
        return profile

    def save(self, user_id: str, condition: str, profile: dict[str, Any]) -> None:
        """Write the current profile and keep a numbered copy."""
        directory = self.path_for(user_id, condition)
        (directory / "versions").mkdir(parents=True, exist_ok=True)
        text = json.dumps(profile, indent=2)
        (directory / "profile.json").write_text(text)
        (directory / "versions" / f"v{profile.get('version', 0):03d}.json").write_text(
            text
        )
