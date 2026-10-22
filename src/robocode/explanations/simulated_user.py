"""Simulated participants with hidden preferences, for testing the loop offline.

This is a toy model for checking that the pipeline runs and that the learning loop *can*
pick up user-specific signals. It does not watch the videos and is not evidence about
real people. Understanding is a noisy function of explanation length (attention) and
coverage of decision logic, scaled by how distinguishable the two rollouts are.
Satisfaction depends on how well the explanation's length, structure and focus match the
persona's hidden tastes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from robocode.explanations.explanation_generator import Explanation
from robocode.explanations.feedback import PreferenceFeedback
from robocode.explanations.understanding import ABPresentation, PairTest

DECISION_WORDS = (
    "if",
    "when",
    "unless",
    "otherwise",
    "choose",
    "chooses",
    "select",
    "first",
    "then",
    "order",
    "plan",
    "search",
    "replan",
    "fallback",
    "priority",
    "until",
)


@dataclass(frozen=True)
class Persona:
    """Hidden preferences of a simulated participant."""

    name: str
    preferred_words: tuple[int, int] = (150, 300)
    attention_words: int = 400  # comprehension drops beyond this length
    wants_bullets: bool | None = None  # None = indifferent
    focus_terms: tuple[str, ...] = ()  # terms whose presence pleases them
    focus_phrase: str = ""  # how they would phrase that wish in feedback
    dislike_terms: tuple[str, ...] = ()
    skill: float = 0.8  # max probability above chance of answering correctly
    comments: bool = True  # whether they write free-text feedback


PERSONAS: dict[str, Persona] = {
    "concise_algorithmic": Persona(
        name="concise_algorithmic",
        preferred_words=(80, 180),
        attention_words=250,
        wants_bullets=True,
        focus_terms=("search", "plan", "algorithm"),
        focus_phrase="the main planning algorithm and its key decisions",
        dislike_terms=("pixel", "constant"),
    ),
    "detail_oriented": Persona(
        name="detail_oriented",
        preferred_words=(400, 800),
        attention_words=900,
        wants_bullets=False,
        focus_terms=("threshold", "margin", "step", "example"),
        focus_phrase="concrete numbers, thresholds and a worked example",
    ),
    "quiet_rater": Persona(
        name="quiet_rater",
        preferred_words=(150, 300),
        attention_words=400,
        comments=False,
    ),
}


@dataclass
class SimulatedParticipant:
    """Answers tests and gives feedback according to a :class:`Persona`."""

    persona: Persona
    seed: int = 0
    _rng: np.random.Generator = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._rng = np.random.default_rng(self.seed)

    def info(self) -> dict[str, Any]:
        """Logged with each round, so analysis can compare learned vs.

        true tastes.
        """
        return {"simulated": True, "persona": self.persona.name, "seed": self.seed}

    def p_correct(self, explanation: Explanation, test: PairTest) -> float:
        """Probability of identifying the target rollout."""
        words = max(1, explanation.word_count)
        attention = min(1.0, self.persona.attention_words / words)
        tokens = re.findall(r"[a-z]+", explanation.text.lower())
        coverage = min(1.0, sum(t in DECISION_WORDS for t in tokens) / 12)
        info = min(1.0, words / 60)  # a one-liner conveys little
        discriminability = 0.4 + 0.6 * test.divergence_percentile
        return (
            0.5
            + 0.5 * self.persona.skill * attention * coverage * info * discriminability
        )

    def answer(
        self, explanation: Explanation, presentation: ABPresentation, test: PairTest
    ) -> str:
        """Pick "A" or "B"."""
        correct = self._rng.random() < self.p_correct(explanation, test)
        wrong = next(k for k in presentation.labels if k != presentation.correct_label)
        return presentation.correct_label if correct else wrong

    def feedback(self, explanation: Explanation) -> PreferenceFeedback:
        """Rate 1-5 and say the most important thing to change."""
        p = self.persona
        text = explanation.text.lower()
        words = explanation.word_count
        lo, hi = p.preferred_words
        complaints: list[tuple[float, str]] = []
        score = 4.0
        if words > hi:
            penalty = min(2.0, (words - hi) / hi * 2)
            score -= penalty
            complaints.append(
                (penalty, f"It was too long; around {hi} words would be better.")
            )
        elif words < lo:
            penalty = min(2.0, (lo - words) / lo * 2)
            score -= penalty
            complaints.append((penalty, "It was too brief; I wanted more detail."))
        bullets = explanation.structure["bullets"]
        if p.wants_bullets is True and bullets < 3:
            score -= 0.7
            complaints.append((0.7, "Please use bullet points instead of paragraphs."))
        elif p.wants_bullets is False and bullets > 6:
            score -= 0.7
            complaints.append(
                (0.7, "Fewer bullet lists please, prose reads better for me.")
            )
        if p.focus_terms:
            hits = sum(term in text for term in p.focus_terms)
            if hits == 0:
                score -= 1.0
                complaints.append((1.0, f"I prefer focusing on {p.focus_phrase}."))
            else:
                score += 0.5 * min(2, hits)
        if any(term in text for term in p.dislike_terms):
            score -= 0.5
            complaints.append((0.5, "Skip low-level implementation constants."))
        score += float(self._rng.normal(0, 0.3))
        rating = int(np.clip(round(score), 1, 5))
        comment = ""
        if p.comments and complaints:
            comment = max(complaints)[1]
        elif p.comments and rating >= 4:
            comment = "This was good, keep this style."
        return PreferenceFeedback(rating=rating, text=comment)
