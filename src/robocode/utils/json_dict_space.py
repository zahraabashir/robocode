"""A gymnasium space for observations that are plain dicts of JSON values."""

from __future__ import annotations

import json
from typing import Any

from gymnasium.spaces import Space


class JSONDictSpace(Space[dict[str, Any]]):
    """Observations that are dicts of JSON values (str, number, bool, None, list, dict).

    For environments whose observation fits neither a fixed-length vector nor an
    object-centric state, such as a level description with polygons of varying size
    plus a history of attempts. Such a dict crosses the black-box wire unchanged:
    ``robocode.utils.env_server.encode`` passes dicts, lists and scalars through, and
    the sandbox's ``env_client`` decodes them back to the same values. So a program sees
    the same dict while it is developed in the sandbox and when it is scored on the host.

    ``description`` is a short summary of the layout, sent to the sandbox in
    ``env_spaces.json``; the environment description documents the layout in full.
    """

    def __init__(self, description: str) -> None:
        super().__init__(shape=None, dtype=None)
        self.description = description

    def contains(self, x: Any) -> bool:
        """True for a string-keyed dict that is JSON-serializable without NaN."""
        if not isinstance(x, dict):
            return False
        try:
            json.dumps(x, allow_nan=False)
        except (TypeError, ValueError):
            return False
        return True

    def sample(self, mask: Any | None = None, probability: Any | None = None) -> Any:
        """Not supported: a valid observation depends on the environment's rules."""
        raise NotImplementedError("JSONDictSpace cannot sample observations")

    @property
    def is_np_flattenable(self) -> bool:
        """A JSON dict has no fixed numpy layout."""
        return False

    def __repr__(self) -> str:
        return "JSONDictSpace()"

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, JSONDictSpace) and other.description == self.description
        )

    def __hash__(self) -> int:
        return hash(("JSONDictSpace", self.description))
