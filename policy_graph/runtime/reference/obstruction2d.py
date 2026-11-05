"""Policy-specific reference measurements, excluded from general recognition.

This is deliberately a source-checked adapter, not recognition by method name.
NumPy and observation APIs execute normally. Only declared search boundaries and
waypoint reads are observed; the graph is a plan-level association graph, not a
complete variable-level slice. Only explicit reference sessions use this adapter.
"""

from __future__ import annotations

import ast
import functools
import hashlib
import math
from collections import Counter
from dataclasses import asdict

from ..graph import Site
from ..runner import RuntimeSession

AST_SHA256 = "2ab0f47f7aee14b26164226bffa02996b081d6742f5a7928c65b5b82818239a5"
ADAPTER_ID = "obstruction2d-polyline-v1"
COUNTS = (
    "candidate_paths_scored",
    "candidate_paths_checked",
    "prefilter_paths_checked",
    "collision_calls",
    "collision_sample_rows",
)
LIMITATION = (
    "Measures geometric path search only. Model-transition depth/work and other "
    "heuristic searches are not measured. Action associations are conservative "
    "at the selected/inspected plan level, not a complete dynamic slice."
)


def movement_steps(path, speed=0.05, arm_speed=0.1):
    """Policy's nominal movement cost; excludes grasp, retries and dynamics."""
    total = 0
    for a, b in zip(path, path[1:]):
        distance = max(abs(a[0] - b[0]) / speed, abs(a[1] - b[1]) / speed)
        if len(a) > 2 and len(b) > 2:
            distance = max(distance, abs(a[2] - b[2]) / arm_speed)
        total += math.ceil(distance - 1e-6)
    return total


def _contract_tree(source):
    tree = ast.parse(source)
    # Collision sample spacing is a resolution parameter, not a horizon unit.
    # Permit a different positive literal here, but verify every other AST node.
    for cls in tree.body:
        if isinstance(cls, ast.ClassDef) and cls.name == "GeneratedApproach":
            for method in cls.body:
                if isinstance(method, ast.FunctionDef) and method.name == "_path_free":
                    for node in ast.walk(method):
                        if (
                            isinstance(node, ast.BinOp)
                            and isinstance(node.op, ast.Div)
                            and isinstance(node.left, ast.Name)
                            and node.left.id == "L"
                            and isinstance(node.right, ast.Constant)
                            and type(node.right.value) in (int, float)
                            and math.isfinite(node.right.value)
                            and node.right.value > 0
                        ):
                            node.right.value = 0.003
    return tree


class Obstruction2DAdapter:
    """Observe actual search calls without tracing their numerical internals."""

    def __init__(self, recorder, path, source):
        self.recorder, self.path, self.source = recorder, str(path), source
        self.name = "_pg_obstruction2d_adapter"
        while self.name in source:
            self.name += "_"
        self.searches = []
        self.builders = []
        self.waypoints = {}
        self.selected = set()
        self.inputs = []
        self.counts = Counter()
        self.call_counts = {}
        self.sites = {}

    @staticmethod
    def matches(source):
        """Accept only reviewed code (formatting/comments need not match)."""
        try:
            tree = _contract_tree(source)
        except (SyntaxError, ValueError, OverflowError):
            return False
        digest = hashlib.sha256(ast.dump(tree, include_attributes=False).encode())
        return digest.hexdigest() == AST_SHA256

    @staticmethod
    def contract():
        """Expose assumptions and coverage in every report using the adapter."""
        return {
            "id": ADAPTER_ID,
            "matched_ast_sha256": AST_SHA256,
            "coverage": "path search, collision sample counts, cached plan association",
            "horizon_unit": "estimated movement steps per path",
            "horizon_basis": "sum ceil(max(|dx|/.05, |dy|/.05, |darm|/.1) - 1e-6)",
            "horizon_excludes": (
                "grasp/release delays, retries, collisions and replanning"
            ),
            "limitations": LIMITATION,
        }

    def compile(self):
        """Inject observers without rewriting numerical or control operations."""
        tree = ast.parse(self.source)
        tracked = {
            "_nsteps",
            "_collides",
            "_path_free",
            "_plan_path",
            "_make_plan",
            "_replan_carry",
        }
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                self.sites[node.name] = self.recorder.site(
                    Site(self.path, node.lineno, node.col_offset, node.name)
                )
                if node.name in tracked:
                    decorator = ast.Call(
                        ast.Attribute(
                            ast.Name(self.name, ast.Load()), "observe", ast.Load()
                        ),
                        [ast.Constant(node.name)],
                        [],
                    )
                    node.decorator_list.append(decorator)
                if node.name == "get_action":
                    for stmt in ast.walk(node):
                        if (
                            isinstance(stmt, ast.Assign)
                            and len(stmt.targets) == 1
                            and isinstance(stmt.targets[0], ast.Name)
                            and stmt.targets[0].id == "wp"
                        ):
                            stmt.value = ast.copy_location(
                                ast.Call(
                                    ast.Attribute(
                                        ast.Name(self.name, ast.Load()),
                                        "waypoint",
                                        ast.Load(),
                                    ),
                                    [stmt.value],
                                    [],
                                ),
                                stmt.value,
                            )
        self.recorder.source_hashes[self.path] = hashlib.sha256(
            self.source.encode()
        ).hexdigest()
        return compile(ast.fix_missing_locations(tree), self.path, "exec"), {
            self.name: self
        }

    def _increment(self, key, amount=1):
        self.counts[key] += amount
        if self.searches:
            self.searches[-1]["counts"][key] += amount

    def observe(self, name):
        """Decorate one verified semantic boundary; values remain ordinary Python."""

        def decorate(fn):
            @functools.wraps(fn)
            def wrapped(*args, **kwargs):
                if name == "_plan_path":
                    return self._search(fn, args, kwargs)
                if name in ("_make_plan", "_replan_carry"):
                    return self._build(fn, args, kwargs)
                if name == "_collides":
                    pts = args[1] if len(args) > 1 else kwargs["pts"]
                    self._increment("collision_calls")
                    self._increment("collision_sample_rows", len(pts))
                if name == "_path_free" and self.searches:
                    path = args[1] if len(args) > 1 else kwargs["path"]
                    key = (
                        "candidate_paths_checked"
                        if id(path) in self.searches[-1]["scores"]
                        else "prefilter_paths_checked"
                    )
                    self._increment(key)
                result = fn(*args, **kwargs)
                if name == "_nsteps" and self.searches:
                    path = args[0] if args else kwargs["path"]
                    self._increment("candidate_paths_scored")
                    # Keep rejected candidates' identities until the search returns.
                    self.searches[-1]["scores"][id(path)] = (path, result)
                return result

            return wrapped

        return decorate

    def _search(self, fn, args, kwargs):
        search = {"counts": Counter(), "scores": {}}
        self.searches.append(search)
        try:
            path = fn(*args, **kwargs)
        finally:
            self.searches.pop()
        scores = search["scores"]
        horizons = [int(pair[1]) for pair in scores.values()]
        selected = scores.get(id(path))
        detail = {
            "adapter": ADAPTER_ID,
            "counts": {key: search["counts"][key] for key in COUNTS},
            "max_candidate_horizon": max(horizons, default=None),
            "selected_path_horizon": (
                int(selected[1]) if selected else movement_steps(path)
            ),
            "selected_path_segments": len(path) - 1,
            "selected_path_validated": selected is not None,
            "selection": "checked_candidate" if selected else "unchecked_fallback",
            "horizon_unit": "estimated movement steps per path",
        }
        event = self.recorder.event(
            "geometric-search", self.sites["_plan_path"], self.inputs, **detail
        )
        if self.builders:
            self.builders[-1].append(event)
        return path

    def _build(self, fn, args, kwargs):
        children = []
        self.builders.append(children)
        try:
            plan = fn(*args, **kwargs)
        finally:
            self.builders.pop()
        if plan:
            event = self.recorder.event(
                "plan-build",
                self.sites[fn.__name__],
                [*self.inputs, *children],
                association="whole plan; constituent paths conservatively grouped",
            )
            for waypoint in plan:
                self.waypoints[id(waypoint)] = (waypoint, event)
        return plan

    def waypoint(self, value):
        """Associate a controller's inspected waypoint with its original plan."""
        saved = self.waypoints.get(id(value))
        if saved is not None and saved[0] is value:
            self.selected.add(saved[1])
        return value

    def call(self, fn, args, kwargs, *, state_args, action):
        """Run a lifecycle call, retaining cached-plan links and performed counts."""
        r = self.recorder
        self.selected = set()
        self.counts = Counter()
        r.frame.invocation = r.next_invocation
        r.next_invocation += 1
        self.inputs = [
            r.external(value, state=key in state_args, name=f"{fn.__name__}.{key}").ref
            for key, value in [*enumerate(args), *kwargs.items()]
        ]
        if fn.__name__ == "reset":
            self.waypoints.clear()
        try:
            result = fn(*args, **kwargs)
            returned = r.event(
                "semantic-call",
                self.sites.get(fn.__name__, r.harness_site),
                [*self.inputs, *sorted(self.selected)],
                adapter=ADAPTER_ID,
            )
            if action:
                r.actions.append(r.event("action", r.harness_site, [returned]))
            return result
        finally:
            self.call_counts[r.phase] = {key: self.counts[key] for key in COUNTS}
            # No retaining every discarded waypoint for the rest of an episode.
            owner = getattr(fn, "__self__", None)
            retained = {id(w) for w in getattr(owner, "plan", [])}
            self.waypoints = {
                key: value for key, value in self.waypoints.items() if key in retained
            }

    def summarize(self, result):
        """Add separately typed geometric metrics; never invent rollout depth."""
        g = self.recorder.graph
        searches = [e for e in g.events if e.kind == "geometric-search"]
        used = g.backward_slice(self.recorder.actions)
        relevant = [e for e in searches if e.id in used]
        complete = not g.incomplete

        def measurements(events):
            return {
                "path_searches": len(events),
                **{key: sum(e.detail["counts"][key] for e in events) for key in COUNTS},
                "max_selected_path_horizon": max(
                    (e.detail["selected_path_horizon"] for e in events), default=None
                ),
                "max_candidate_path_horizon": max(
                    (
                        e.detail["max_candidate_horizon"]
                        for e in events
                        if e.detail["max_candidate_horizon"] is not None
                    ),
                    default=None,
                ),
                "unchecked_fallback_paths": sum(
                    not e.detail["selected_path_validated"] for e in events
                ),
            }

        for action in result["actions"]:
            scope = g.backward_slice([action["return_event"]])
            events = [e for e in searches if e.id in scope]
            action.update(
                planning_depth=None,
                new_planning_work=None,
                status="partial" if complete else "unknown",
                planning_event_ids=[e.id for e in events],
                inherited_planning_event_ids=[
                    e.id for e in events if e.phase != action["phase"]
                ],
                geometric_planning={
                    "associated": measurements(events),
                    "new": measurements(
                        [e for e in events if e.phase == action["phase"]]
                    ),
                    "complete": complete,
                },
            )
        for call in result["calls"]:
            call["performed_planning_work"] = None
            call["planning_event_ids"] = [
                e.id for e in searches if e.phase == call["phase"]
            ]
            call["geometric_work"] = self.call_counts.get(
                call["phase"], {key: 0 for key in COUNTS}
            )
        totals = {key: sum(c[key] for c in self.call_counts.values()) for key in COUNTS}
        result.update(
            status=(
                ("partial" if complete else "unknown")
                if result["actions"] or g.incomplete
                else "not_evaluated"
            ),
            verdict=(
                "planning_observed"
                if relevant
                else (
                    "needs_review"
                    if result["actions"] or g.incomplete
                    else "not_evaluated"
                )
            ),
            planning_depth=None,
            planning_work=None,
            performed_planning_work=None,
            planning_event_count=len(relevant),
            units=[],
            basis="Observed semantic boundaries of a source-verified geometric policy",
            support_scope=LIMITATION,
            planning_calls_per_action=(
                len({e.phase for e in relevant}) / len(result["actions"])
                if result["actions"]
                else None
            ),
            planning_events=[
                {
                    "id": e.id,
                    "kind": e.kind,
                    "phase": e.phase,
                    "site": asdict(e.site),
                    "action_relevant": e.id in used,
                    "status": "observed" if complete else "incomplete",
                    "depth": None,
                    "work": None,
                    "transition_ids": [],
                    "selector_ids": [e.id],
                    "unit": None,
                    "reasons": [LIMITATION],
                    **e.detail,
                }
                for e in searches
            ],
            geometric_planning={
                "status": "observed" if complete else "incomplete",
                "horizon_unit": "estimated movement steps per path",
                "action_relevance_basis": (
                    "selected/inspected cached plan "
                    "(conservative plan-level association)"
                ),
                "performed": measurements(searches),
                "action_relevant": measurements(relevant),
                "all_collision_and_search_counts": totals,
                "counts_are_prefix_only": not complete,
            },
        )


class Obstruction2DReferenceSession(RuntimeSession):
    """Opt-in measurement oracle; never used by the normal CLI or benchmark.

    Results describe this reviewed policy, not automatic recognition accuracy.
    """

    def source_transform(self, source, path):
        if (
            self.recorder.config.transition_models
            or self.recorder.config.assessments
            or self.recorder.config.planners
            or self.recorder.config.pure_functions
        ):
            raise ValueError(
                "Reference measurements cannot be mixed with generic contracts"
            )
        if not Obstruction2DAdapter.matches(source):
            raise ValueError(
                "Source does not match the reviewed Obstruction2D reference"
            )
        self.semantic_adapter = Obstruction2DAdapter(self.recorder, path, source)
        self.metadata["semantic_adapter"] = self.semantic_adapter.contract()
        self.metadata["measurement_role"] = "policy_specific_reference"
        return self.semantic_adapter.compile()
