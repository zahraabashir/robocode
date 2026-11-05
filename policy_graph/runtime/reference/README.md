# Obstruction2D reference measurement

This is a policy-specific reference, excluded from the automatic runtime and the
planning benchmark. It validates geometric measurements for one reviewed policy;
it is not evidence of general recognition of route planning or NumPy operations.
The original adapter is retained here to preserve useful measurement evidence.

Select it explicitly through the Python API, from the repository root:

```python
from pathlib import Path
from policy_graph.runtime.episode_config import load_episode_spec
from policy_graph.runtime.reference.obstruction2d import Obstruction2DReferenceSession

path = Path(
    "agent_runs/environments/Obstruction2D/runs/"
    "claude_opus55_high_r42_820cc0f3/evidence/final/approach.py"
)
spec = load_episode_spec(path)
env = spec.make_env()
try:
    session = Obstruction2DReferenceSession(path).run_episode(
        env, seed=0, count=2, max_steps=spec.max_steps,
        primitives=spec.make_primitives(env),
    )
    report = session.report()
finally:
    env.close()
```

The report records `metadata.measurement_role = "policy_specific_reference"`.
It can be serialized as JSON, and `session.recorder.graph.to_dot()` exports its
graph. No normal CLI option automatically selects this reference.

This run finishes successfully in **41 actions**, with **135 graph events**,
**6 path searches**, and **5,399 candidate paths scored**. The longest selected
route takes **11 estimated movement actions**; the maximum scored candidate
horizon is **31 estimated movement steps**. These measurements describe this
seed and object count, not all possible executions of the policy.

The adapter executes NumPy operations, object-observation reads, and generators
normally. It records a summary for each completed `_plan_path` call, connects it
to the constructed plan, and links controller waypoint reads to that plan across
calls. It does not emit an event for every arithmetic operation or collision
sample. The event limit still applies to the compact graph.

The report's `geometric_planning` fields keep different units separate:

- `performed`: counts and horizon summaries for completed path searches, including
  searches not associated with a returned action.
- `action_relevant`: the same measurements for unique search events associated
  with plans inspected by the controller. Each search is counted once even when
  many actions reuse it. This association conservatively groups an entire plan's
  constituent paths; it is not a complete variable-level dependency slice.
- `candidate_paths_scored`: actual candidate cost evaluations. This is breadth/work,
  not the number of unique future states or simulated transitions.
- `candidate_paths_checked` and `prefilter_paths_checked`: full candidate checks
  and the preliminary plateau checks, respectively.
- `collision_sample_rows`: rows supplied to collision checks; repeated samples
  count again. Increasing collision resolution increases this work, not horizon.
- `max_selected_path_horizon` / `max_candidate_path_horizon`: the maximum cost of
  a returned path / scored candidate, using the policy's `_nsteps` formula. Each
  segment costs `ceil(max(abs(dx)/.05, abs(dy)/.05, abs(darm)/.1) - 1e-6)`.
  This estimates nominal movement actions, excluding grasp/release delays,
  retries, collisions and replanning. It is neither a simulated-state depth nor
  the total remaining horizon of a multi-path pick-and-place plan.
  Read the selected-path value as `longest selected route: N estimated movement
  actions`; the JSON field name is retained for compatibility.
- `all_collision_and_search_counts`: actual counts across lifecycle calls,
  including collision checks performed outside `_plan_path`. These can exceed
  the counts in the path-search summaries.

Each search reports whether the returned path passed the policy's collision
checker. Its unchecked fallback is explicitly labeled; sampled checks are not a
proof of continuous collision freedom. Per-action `geometric_planning.new` contains
newly computed associated searches; `associated` also includes cached searches.
Per-call `geometric_work` records work performed, including discarded searches.
Cached horizon values describe the original path, not its remaining suffix.

Overall status is **`partial`**: geometric measurements are available, while the
generic `planning_depth` and `planning_work` remain `null`. This adapter does not
measure all other heuristics or provide general NumPy provenance. On failure,
status becomes `unknown`, geometric status becomes `incomplete`, and any retained
measurements are explicitly prefix-only.

The reference checks the entire reviewed AST, including constants, imports, and
controller logic. Whitespace/comments and a positive collision sample spacing
literal may vary. Other changes raise an error; they do not silently select a
different interpretation. Reference measurements cannot be mixed with explicit
model, planner, or pure-function contracts. The frozen source in `../fixtures/`
allows regression tests without the local archive. Reference tests compare its
actions with ordinary execution on multiple seeds.
