"""Human-specified task semantics and expected labels, never supplied to tracing.

These are development fixtures, not a held-out estimate of generalization. The
description and labels specify the meaning of otherwise ambiguous computations.
"""

from __future__ import annotations

from dataclasses import dataclass
from textwrap import dedent
from typing import Any

VERSION = "planning-benchmark-0.2"
CATEGORIES = (
    "action_effect",
    "configuration_route",
    "task_constraints",
    "contingency_information",
)

# One shared model API for the contract track, independent of fixture identity.
WORLD_MODEL = '''"""One action changes a scalar world state by s_next = 2*s + a."""
def step(state, action):
    return state * 2 + action

def route_clear(route, blocked):
    """Pure assessment of one proposed route against blocked graph nodes."""
    for node in route:
        if node in blocked:
            return False
    return True

def placement_cost(slot, occupied):
    """Pure assessment of a proposed placement: occupancy and distance to slot 3."""
    return 1000 if slot in occupied else abs(slot - 3)
'''


@dataclass(frozen=True)
class Call:
    """A lifecycle invocation; arguments are copied independently for each run."""

    method: str = "get_action"
    args: tuple = ()
    state_args: tuple = (0,)
    action: bool | None = None


@dataclass(frozen=True)
class Metric:
    """An exact expected quantity in an existing report field, with its unit."""

    path: str
    value: int
    unit: str


@dataclass(frozen=True)
class Case:
    """One execution scenario with semantic ground truth independent of the scorer."""

    id: str
    description: str
    source: str
    calls: tuple[Call, ...]
    returns: tuple[Any, ...]
    performed: bool
    action_relevant: bool
    categories: tuple[str, ...] = ()
    evidence: tuple[str, str, str] = ("", "", "")
    metrics: tuple[Metric, ...] = ()
    equivalence_group: str | None = None
    requirements: tuple[str, ...] = ()
    notes: str = ""


def _case(
    identifier: str,
    description: str,
    source: str,
    args: tuple,
    returned: Any,
    *,
    planning: bool = True,
    **kwargs: Any,
) -> Case:
    return Case(
        identifier,
        description,
        dedent(source).lstrip(),
        (Call(args=tuple(args)),),
        (returned,),
        planning,
        planning,
        **kwargs,
    )


ONE_STEP_METRICS = (
    Metric("planning_depth", 1, "model steps"),
    Metric("planning_work", 3, "transition evaluations"),
    Metric(
        "semantic_profile.episodes.0.measurements.breadth.value",
        3,
        "distinct candidates",
    ),
)
EFFECT_EVIDENCE = (
    "Three possible movements in a scalar world where next position equals "
    "position + movement.",
    "Evaluate each predicted position's distance to target 10.",
    "Return the movement whose predicted outcome is nearest the target.",
)
ROUTE_EVIDENCE = (
    "Proposed node sequences are future routes through a graph; "
    "listed edges are traversable.",
    "Reject routes through observed blocked nodes and compare lengths "
    "of feasible routes.",
    "Return the next node on the chosen route as the movement action.",
)

BASE_CASES = (
    _case(
        "current_correction",
        "Calibrate a current clearance measurement and apply a reactive threshold.",
        """
        def get_action(obs):
            corrected = obs + 0.1
            return 0 if corrected < 0.2 else 1
    """,
        (0.4,),
        1,
        planning=False,
        notes="The addition estimates present clearance, not a future action outcome.",
    ),
    _case(
        "calibration_alternatives",
        "Estimate current clearance under three calibration offsets; "
        "no prospective behavior is assessed.",
        """
        def get_action(obs):
            current_clearances = [obs + offset for offset in (-0.1, 0.0, 0.1)]
            conservative_clearance = min(current_clearances)
            return 0 if conservative_clearance < 0.2 else 1
    """,
        (0.4,),
        1,
        planning=False,
        notes=(
            "Negative control for confusing alternative current-state estimates "
            "with alternative future actions."
        ),
    ),
    _case(
        "unused_prediction",
        "Predict possible movements but do not assess them or use them in a decision.",
        """
        def get_action(obs):
            future_positions = [obs + move for move in (-1, 0, 1)]
            return 0
    """,
        (7,),
        0,
        planning=False,
    ),
    _case(
        "unexecuted_branch",
        "The only planning branch is not executed for the supplied observation.",
        """
        def get_action(obs):
            if obs < 0:
                return min((-1, 0, 1), key=lambda move: abs(obs + move - 10))
            return 0
    """,
        (7,),
        0,
        planning=False,
    ),
    _case(
        "one_step_min",
        "One-step action selection using a scalar comprehension callback.",
        """
        def get_action(obs):
            return min((-1, 0, 1), key=lambda move: abs(obs + move - 10))
    """,
        (7,),
        1,
        categories=("action_effect",),
        evidence=EFFECT_EVIDENCE,
        metrics=ONE_STEP_METRICS,
        equivalence_group="one_step",
    ),
    _case(
        "one_step_loop",
        "The same one-step decision expressed as a best-so-far loop.",
        """
        def get_action(obs):
            best = None
            chosen = 0
            for move in (-1, 0, 1):
                future = obs + move
                cost = abs(future - 10)
                if best is None or cost < best:
                    best = cost
                    chosen = move
            return chosen
    """,
        (7,),
        1,
        categories=("action_effect",),
        evidence=EFFECT_EVIDENCE,
        metrics=ONE_STEP_METRICS,
        equivalence_group="one_step",
    ),
    _case(
        "one_step_helper",
        "The same decision with renamed variables and a helper function.",
        """
        def assess(x, u):
            return abs(x + u - 10)
        def get_action(observation):
            return min((-1, 0, 1), key=lambda u: assess(observation, u))
    """,
        (7,),
        1,
        categories=("action_effect",),
        evidence=EFFECT_EVIDENCE,
        metrics=ONE_STEP_METRICS,
        equivalence_group="one_step",
    ),
    _case(
        "one_step_numpy",
        "The same three evaluations computed in a NumPy batch.",
        """
        import numpy as np
        def get_action(obs):
            moves = np.array([-1, 0, 1])
            future_positions = obs + moves
            costs = np.abs(future_positions - 10)
            return int(moves[np.argmin(costs)])
    """,
        (7,),
        1,
        categories=("action_effect",),
        evidence=EFFECT_EVIDENCE,
        metrics=ONE_STEP_METRICS,
        equivalence_group="one_step",
        requirements=("numpy",),
    ),
    _case(
        "one_step_generator",
        "The same decision evaluated through a generator expression.",
        """
        def get_action(obs):
            evaluated = ((abs(obs + move - 10), move) for move in (-1, 0, 1))
            return min(evaluated)[1]
    """,
        (7,),
        1,
        categories=("action_effect",),
        evidence=EFFECT_EVIDENCE,
        metrics=ONE_STEP_METRICS,
        equivalence_group="one_step",
    ),
    _case(
        "shared_model_rollout",
        "Three successor steps for each of three actions, using the shared model API.",
        """
        import world_model
        def get_action(obs):
            def evaluate(action):
                state = obs
                for _ in range(3):
                    state = world_model.step(state, action)
                return abs(state - 10)
            return min((-1, 0, 1), key=evaluate)
    """,
        (2,),
        -1,
        categories=("action_effect",),
        evidence=(
            "Three constant-action sequences, each of length three, "
            "under s_next = 2*s + a.",
            "Predict the terminal state and compare distance to target 10.",
            "Return the first action of the best sequence.",
        ),
        metrics=(
            Metric("planning_depth", 3, "model steps"),
            Metric("planning_work", 9, "transition evaluations"),
        ),
    ),
    _case(
        "route_selection",
        "Choose the shortest feasible route around observed blocked nodes.",
        """
        def clear(route, blocked):
            for node in route:
                if node in blocked:
                    return False
            return True
        def get_action(obs):
            routes = [["S", "A", "G"], ["S", "B", "C", "G"]]
            feasible = [route for route in routes if clear(route, obs)]
            chosen = min(feasible, key=len)
            return chosen[1]
    """,
        (["A"],),
        "B",
        categories=("configuration_route",),
        evidence=ROUTE_EVIDENCE,
        equivalence_group="route_choice",
        notes=(
            "Selected route has three graph edges; "
            "no dynamics rollout depth is asserted."
        ),
    ),
    _case(
        "route_selection_loop",
        "The same route choice, with feasibility and selection implemented in loops.",
        """
        def get_action(obs):
            routes = [["S", "A", "G"], ["S", "B", "C", "G"]]
            best = None
            for route in routes:
                blocked = False
                for node in route:
                    if node in obs:
                        blocked = True
                        break
                if not blocked and (best is None or len(route) < len(best)):
                    best = route
            return best[1]
    """,
        (["A"],),
        "B",
        categories=("configuration_route",),
        evidence=ROUTE_EVIDENCE,
        equivalence_group="route_choice",
    ),
    _case(
        "single_route_validation",
        "Validate one proposed route before committing to its first movement.",
        """
        def get_action(obs):
            route = ["S", "B", "G"]
            for node in route:
                if node in obs:
                    return "WAIT"
            return route[1]
    """,
        (["A"],),
        "B",
        categories=("configuration_route",),
        evidence=(
            "One proposed future route S-B-G.",
            "Check every route node against known obstructions.",
            "Choose to follow the route or wait based on its feasibility.",
        ),
    ),
    _case(
        "failed_route_search",
        "All proposed routes are infeasible; "
        "the failed search determines a wait action.",
        """
        def get_action(obs):
            routes = [["S", "A", "G"], ["S", "B", "G"]]
            for route in routes:
                feasible = True
                for node in route:
                    if node in obs:
                        feasible = False
                        break
                if feasible:
                    return route[1]
            return "WAIT"
    """,
        (["A", "B"],),
        "WAIT",
        categories=("configuration_route",),
        evidence=(
            "Two candidate future routes.",
            "Both are tested and rejected by obstruction constraints.",
            "The lack of a feasible route causes the wait action.",
        ),
    ),
    _case(
        "placement_choice",
        "Choose an intended box placement in an unoccupied slot near slot 3.",
        """
        def get_action(obs):
            placements = [1, 2, 3, 4]
            feasible = [p for p in placements if p not in obs]
            return min(feasible, key=lambda p: abs(p - 3))
    """,
        ([3],),
        2,
        categories=("configuration_route",),
        evidence=(
            "Each candidate slot is a prospective box placement, "
            "not an observed box location.",
            "Check occupancy and distance to desired placement 3.",
            "Return the selected slot as the place-box command.",
        ),
    ),
    Case(
        "discarded_search",
        "A planning computation runs, but its selected action is discarded.",
        dedent("""
        def get_action(obs):
            discarded = min((-1, 0, 1), key=lambda move: abs(obs + move - 10))
            return 0
    """).lstrip(),
        (Call(args=(7,)),),
        (0,),
        True,
        False,
        ("action_effect",),
        EFFECT_EVIDENCE,
        metrics=(
            Metric("planning_work", 0, "action-relevant transition evaluations"),
            Metric("performed_planning_work", 3, "transition evaluations"),
        ),
    ),
    Case(
        "cached_plan",
        "Compute a three-movement plan during reset "
        "and reuse it for three returned actions.",
        dedent("""
        class GeneratedApproach:
            def reset(self, obs, info):
                def evaluate(move):
                    future = obs
                    for _ in range(3):
                        future = future + move
                    return abs(future - 10)
                chosen = min((-1, 0, 1), key=evaluate)
                self.plan = [chosen, chosen, chosen]
            def get_action(self, obs):
                return self.plan.pop(0)
    """).lstrip(),
        (Call("reset", (2, {})), Call(args=(2,)), Call(args=(3,)), Call(args=(4,))),
        (None, 1, 1, 1),
        True,
        True,
        ("action_effect",),
        (
            "Three alternative constant-movement sequences of length three.",
            "Evaluate terminal distance to target 10 during reset.",
            "Store the chosen sequence and return its elements on later calls.",
        ),
        metrics=(
            Metric("planning_depth", 3, "model steps"),
            Metric("planning_work", 9, "transition evaluations"),
            Metric("actions.0.new_planning_work", 0, "transition evaluations"),
            Metric("actions.1.new_planning_work", 0, "transition evaluations"),
            Metric("actions.2.new_planning_work", 0, "transition evaluations"),
        ),
    ),
    Case(
        "hardcoded_sequence",
        "Execute a fixed sequence without constructing or assessing it "
        "during this trace.",
        dedent("""
        class GeneratedApproach:
            def reset(self, obs, info):
                self.moves = [1, 1, -1]
            def get_action(self, obs):
                return self.moves.pop(0)
    """).lstrip(),
        (Call("reset", (2, {})), Call(args=(2,)), Call(args=(3,)), Call(args=(4,))),
        (None, 1, 1, -1),
        False,
        False,
        notes=(
            "No claim is made about how a human or external process "
            "originally chose this sequence."
        ),
    ),
    _case(
        "task_order",
        "Find a task ordering that satisfies clearing-before-grasping prerequisites.",
        """
        def get_action(obs):
            orders = [["grasp", "clear"], ["clear", "grasp"]]
            for order in orders:
                accessible = obs
                feasible = True
                for task in order:
                    if task == "clear":
                        accessible = True
                    elif not accessible:
                        feasible = False
                        break
                if feasible:
                    return order[0]
            return "WAIT"
    """,
        (False,),
        "clear",
        categories=("task_constraints", "action_effect"),
        evidence=(
            "Two hypothetical orderings of clear and grasp tasks.",
            "Propagate the symbolic accessible condition and test grasp prerequisites.",
            "Choose the first task in a feasible ordering.",
        ),
    ),
    _case(
        "contingent_choice",
        "Compare a risky action's possible outcomes with a safe alternative.",
        """
        def get_action(obs):
            probability = obs
            risky_outcomes = [(probability, 10.0), (1.0 - probability, -20.0)]
            expected_risky = 0.0
            for chance, reward in risky_outcomes:
                expected_risky += chance * reward
            safe_reward = 2.0
            return "RISKY" if expected_risky > safe_reward else "SAFE"
    """,
        (0.5,),
        "SAFE",
        categories=("contingency_information", "action_effect"),
        evidence=(
            "A risky action with success/failure outcomes, compared with a safe action.",
            "Assess expected reward under the supplied success probability.",
            "Choose the action with higher assessed expected reward.",
        ),
    ),
    _case(
        "information_choice",
        "Compare inspecting before acting with acting immediately under uncertainty.",
        """
        def get_action(obs):
            probability_left = obs
            reward = 10.0
            inspection_cost = 1.0
            immediate = max(probability_left, 1.0 - probability_left) * reward
            inspect_then_choose = reward - inspection_cost
            if inspect_then_choose > immediate:
                return "INSPECT"
            return "LEFT" if probability_left >= 0.5 else "RIGHT"
    """,
        (0.5,),
        "INSPECT",
        categories=("contingency_information",),
        evidence=(
            "Inspect-then-act and act-now strategies for a hidden left/right target.",
            "Compare expected success reward; perfect inspection costs one unit.",
            "Select information gathering when it improves expected utility.",
        ),
        notes=(
            "A two-decision strategy is assessed analytically; "
            "no explicit dynamics-step depth is asserted."
        ),
    ),
)


CONTRACT_CASES = (
    _case(
        "shared_single_route",
        "Validate one route using a shared checking API.",
        """
        import world_model
        def get_action(obs):
            route = ["S", "B", "G"]
            return "B" if world_model.route_clear(route, obs) else "WAIT"
    """,
        (["A"],),
        "B",
        categories=("configuration_route",),
        evidence=(
            "One proposed future route S-B-G.",
            "The shared route_clear API checks the route against blocked nodes.",
            "Its result chooses whether to move or wait.",
        ),
        metrics=(
            Metric(
                "semantic_profile.episodes.0.measurements.breadth.value",
                1,
                "distinct candidates",
            ),
            Metric(
                "semantic_profile.episodes.0.measurements.candidate_evaluations.value",
                1,
                "candidate evaluations",
            ),
            Metric(
                "semantic_profile.episodes.0.measurements.max_assessed_horizon.value",
                2,
                "graph edges",
            ),
        ),
    ),
    _case(
        "shared_failed_routes",
        "Repeated failed route checks: two distinct routes, three evaluations.",
        """
        import world_model
        def get_action(obs):
            routes = [["S", "A", "G"], ["S", "A", "G"], ["S", "B", "C", "G"]]
            for route in routes:
                if world_model.route_clear(route, obs):
                    return route[1]
            return "WAIT"
    """,
        (["A", "B"],),
        "WAIT",
        categories=("configuration_route",),
        evidence=(
            "Two distinct proposed routes, with the first assessed twice.",
            "The shared checking API rejects all candidates.",
            "Because no route passed, return WAIT.",
        ),
        metrics=(
            Metric(
                "semantic_profile.episodes.0.measurements.breadth.value",
                2,
                "distinct candidates",
            ),
            Metric(
                "semantic_profile.episodes.0.measurements.candidate_evaluations.value",
                3,
                "candidate evaluations",
            ),
            Metric(
                "semantic_profile.episodes.0.measurements.max_assessed_horizon.value",
                3,
                "graph edges",
            ),
        ),
    ),
    _case(
        "shared_placement",
        "Rank prospective placements using the shared cost API.",
        """
        import world_model
        def get_action(obs):
            return min([1, 2, 3, 4],
                       key=lambda slot: world_model.placement_cost(slot, obs))
    """,
        ([3],),
        2,
        categories=("configuration_route",),
        evidence=(
            "Four possible placements of a box.",
            "Evaluate occupancy and distance to slot 3.",
            "Select the lowest-cost placement.",
        ),
        metrics=(
            Metric(
                "semantic_profile.episodes.0.measurements.breadth.value",
                4,
                "distinct candidates",
            ),
            Metric(
                "semantic_profile.episodes.0.measurements.candidate_evaluations.value",
                4,
                "candidate evaluations",
            ),
        ),
    ),
    _case(
        "shared_unused_check",
        "Check a proposed route but never use the result in a decision.",
        """
        import world_model
        def get_action(obs):
            unused = world_model.route_clear(["S", "B", "G"], obs)
            return "WAIT"
    """,
        (["A"],),
        "WAIT",
        planning=False,
        notes=(
            "Hypothesis and assessment alone are not "
            "a complete deliberative decision."
        ),
    ),
)

CASES = BASE_CASES + CONTRACT_CASES


def validate_cases(cases=CASES):
    """Reject malformed benchmark labels, independently of analyzer predictions."""
    ids = set()
    for case in cases:
        if case.id in ids:
            raise ValueError(f"Duplicate case ID: {case.id}")
        ids.add(case.id)
        if len(case.calls) != len(case.returns) or not case.calls:
            raise ValueError(f"Invalid call/return sequence: {case.id}")
        if case.performed and (not case.categories or not all(case.evidence)):
            raise ValueError(f"Missing planning semantics: {case.id}")
        if case.action_relevant and not case.performed:
            raise ValueError(
                f"Action relevance without recorded planning origin: {case.id}"
            )
        if set(case.categories) - set(CATEGORIES):
            raise ValueError(f"Unknown category: {case.id}")
        compile(case.source, case.id, "exec")
