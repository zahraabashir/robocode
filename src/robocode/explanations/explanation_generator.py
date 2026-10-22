"""Explanation Generator: an LLM explains one policy, optionally for one user.

All conditions use the same prompt template. The only difference is whether a
learned user profile is inserted, so differences between conditions come from
the interaction history rather than from a different explainer. The generator
never sees the understanding test, the distractor policy or other policies.
"""

from __future__ import annotations

import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from typing import Any

from robocode.explanations.policy_provider import PolicyRecord
from robocode.utils.llm import LLMClient

EXPLAIN_TEMPLATE = """\
You are explaining a robot control policy to a person. The policy is a Python \
program that a coding agent wrote to solve the task described below. The \
program is frozen: it is run as-is on new instances of the task.

Your goal is to help this person understand how the policy actually works, \
including its decision-making logic, well enough to recognize its behaviour and \
anticipate what it would do in a new situation.

- Be faithful to the code. Describe what this program does, not what a good \
policy for the task would do. If something is unclear from the code, say so \
rather than guessing.
- The person will not see the code.
- You choose the content, structure, length and level of detail.
{profile_section}
<task_description>
{task_description}
</task_description>

<policy_code>
{policy_code}
</policy_code>

Write only the explanation, in Markdown."""

PROFILE_SECTION = """
We have explained other policies to this person before. What we have learned \
about them is summarized in the profile below. Use it to decide how to explain \
this policy to them. Entries with low confidence are tentative, and a profile \
can be wrong, so do not drop information this person needs in order to \
understand the policy. Do not mention the profile.

<user_profile>
{profile_json}
</user_profile>
"""


@dataclass
class Explanation:
    """A generated explanation and its provenance."""

    text: str
    policy_id: str
    used_profile: bool
    profile_version: int | None
    prompt_sha1: str
    latency_s: float
    cost_usd: float | None
    model: dict[str, Any] = field(default_factory=dict)

    @property
    def word_count(self) -> int:
        """Words, ignoring Markdown-only tokens such as "-" or "##"."""
        return count_words(self.text)

    @property
    def char_count(self) -> int:
        """Characters."""
        return len(self.text)

    @property
    def structure(self) -> dict[str, int]:
        """Simple structural features, for analysis."""
        lines = self.text.splitlines()
        return {
            "headings": sum(1 for l in lines if re.match(r"^\s*#{1,6}\s", l)),
            "bullets": sum(1 for l in lines if re.match(r"^\s*([-*+]|\d+\.)\s", l)),
            "code_spans": self.text.count("`") // 2,
            "paragraphs": len(
                [p for p in re.split(r"\n\s*\n", self.text) if p.strip()]
            ),
        }


class ExplanationGenerator:
    """Builds the explanation prompt and calls the LLM."""

    def __init__(
        self,
        llm: LLMClient,
        model_info: dict[str, Any] | None = None,
        max_code_chars: int = 80_000,
        max_task_chars: int = 20_000,
    ) -> None:
        self._llm = llm
        self._model_info = dict(model_info or {})
        self._max_code_chars = max_code_chars
        self._max_task_chars = max_task_chars

    def build_prompt(self, policy: PolicyRecord, profile: dict[str, Any] | None) -> str:
        """The exact prompt text for one policy and (optional) profile."""
        profile_section = ""
        if profile is not None:
            profile_section = PROFILE_SECTION.format(
                profile_json=json.dumps(profile_for_prompt(profile), indent=2)
            )
        return EXPLAIN_TEMPLATE.format(
            profile_section=profile_section,
            task_description=_clip(policy.task_description(), self._max_task_chars),
            policy_code=_clip(policy.source(), self._max_code_chars),
        )

    def generate(
        self, policy: PolicyRecord, profile: dict[str, Any] | None
    ) -> Explanation:
        """Explain ``policy``; ``profile=None`` means no user-specific knowledge."""
        prompt = self.build_prompt(policy, profile)
        start = time.monotonic()
        response = self._llm.complete([{"role": "user", "content": prompt}])
        return Explanation(
            text=response.text.strip(),
            policy_id=policy.policy_id,
            used_profile=profile is not None,
            profile_version=None if profile is None else profile.get("version"),
            prompt_sha1=hashlib.sha1(prompt.encode()).hexdigest(),
            latency_s=time.monotonic() - start,
            cost_usd=response.cost_usd,
            model=self._model_info,
        )


def count_words(text: str) -> int:
    """Whitespace-delimited tokens that contain a letter or digit."""
    return sum(1 for token in text.split() if re.search(r"\w", token))


def profile_for_prompt(profile: dict[str, Any]) -> dict[str, Any]:
    """The profile without bookkeeping fields the explainer does not need."""
    return {
        k: v for k, v in profile.items() if k not in ("version", "updated_after_round")
    }


def _clip(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n\n[... truncated {len(text) - limit} characters ...]"
