"""Explicit semantic contracts for operations that a trace cannot interpret."""

from __future__ import annotations

from dataclasses import dataclass, field

CATEGORIES = (
    "action_effect",
    "configuration_route",
    "task_constraints",
    "contingency_information",
)


@dataclass(frozen=True)
class AssessmentContract:
    """A pure function assesses one prospective candidate and returns a score/bool.

    This declares meaning, not correctness of the checker or the resulting plan.
    The function must depend only on its arguments and must not mutate them.
    Horizon extraction is optional and only applies to plain lists/tuples.
    model_free=True additionally declares no model transitions inside the API;
    otherwise hidden model depth/work remain unknown, not inapplicable.
    """

    candidate_arg: int | str = 0
    category: str = "configuration_route"
    candidate_kind: str = "route"
    horizon: str | None = None
    horizon_unit: str | None = None
    model_free: bool = False

    def __post_init__(self):
        if self.category not in CATEGORIES or not self.candidate_kind:
            raise ValueError(
                "Assessment contracts need a known category and candidate kind"
            )
        if self.horizon not in (None, "sequence_edges", "sequence_items"):
            raise ValueError("Unsupported horizon extractor")
        if bool(self.horizon) != bool(self.horizon_unit):
            raise ValueError(
                "A horizon extractor and its unit must be supplied together"
            )
        if isinstance(self.candidate_arg, int) and self.candidate_arg < 0:
            raise ValueError("candidate_arg must be non-negative")


@dataclass(frozen=True)
class TransitionContract:
    """One call predicts one successor; argument names use the original signature.

    Integer arguments count bound-method arguments without ``self``. output_index
    identifies a next-state component of a tuple result, such as (state, done).
    The whole call is counted once, even when its Python body is instrumented.
    """

    state_arg: int | str = 0
    action_arg: int | str = 1
    output_index: int | None = None
    unit: str = "model steps"
    duration: float | None = None


@dataclass
class RuntimeConfig:
    """Recognition assumptions and the trace size limit for one session."""

    transition_models: dict[str, TransitionContract] = field(default_factory=dict)
    assessments: dict[str, AssessmentContract] = field(default_factory=dict)
    planners: tuple[str, ...] = ()
    pure_functions: tuple[str, ...] = ()
    arithmetic_transitions: bool = True
    max_events: int = 200_000

    @classmethod
    def from_dict(cls, data):
        """Construct contracts and immutable name lists from JSON-compatible data."""
        data = dict(data)
        # Read older saved configs without re-enabling policy-specific dispatch.
        if data.pop("semantic_adapters", False):
            raise ValueError(
                "Automatic policy-specific adapters have been removed. "
                "Use the explicit runtime.reference API for reference measurements."
            )
        data["transition_models"] = {
            name: TransitionContract(**contract)
            for name, contract in data.get("transition_models", {}).items()
        }
        data["assessments"] = {
            name: AssessmentContract(**contract)
            for name, contract in data.get("assessments", {}).items()
        }
        for key in ("planners", "pure_functions"):
            if key in data:
                data[key] = tuple(data[key])
        return cls(**data)
