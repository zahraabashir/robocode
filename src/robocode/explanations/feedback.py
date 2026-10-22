"""Feedback Collector: preference ratings and free-text feedback.

Preference is collected in every condition, including ones that do not learn
from it. Whether it is *used* is decided by the condition in
:mod:`robocode.explanations.user_model`.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

RATING_QUESTION = (
    "How satisfied were you with this explanation? "
    "(1 = very unsatisfied, 5 = very satisfied)"
)
TEXT_QUESTION = "What would you change about the explanation? (optional)"
MAX_TEXT_CHARS = 4000


@dataclass(frozen=True)
class PreferenceFeedback:
    """One participant's preference response to one explanation."""

    rating: int
    text: str = ""

    def to_json(self) -> dict[str, Any]:
        """JSON-serializable form."""
        return asdict(self)


def collect_feedback(rating: Any, text: str | None = "") -> PreferenceFeedback:
    """Validate and normalize raw form/console input."""
    try:
        value = int(rating)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Rating must be an integer 1-5, got {rating!r}") from exc
    if not 1 <= value <= 5:
        raise ValueError(f"Rating must be between 1 and 5, got {value}")
    return PreferenceFeedback(rating=value, text=(text or "").strip()[:MAX_TEXT_CHARS])
