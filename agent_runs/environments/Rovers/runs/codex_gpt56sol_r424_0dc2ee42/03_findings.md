# Rovers 424 — findings and your notes

[Timeline](01_timeline.md) · [All commits and changed lines](02_code_changes.md) · [Final controller](evidence/final/approach.py)

**Prior manual analysis migrated for review.** No new rollouts or private-reasoning claims were added during reorganization. Your notes in this file are preserved when the timeline is rebuilt.

## Start here

- **Phases plus route planning:** [early message E0010](01_timeline.md#E0010) → [executed planner probe E0080](01_timeline.md#E0080).
- **Check a suspicious observation before editing:** [E0237](01_timeline.md#E0237) → [E0239](01_timeline.md#E0239).
- **Try an optimization, then partially revert:** [E0250](01_timeline.md#E0250) → [E0254](01_timeline.md#E0254) → [E0258](01_timeline.md#E0258).

## Findings to revisit


Scope: one archived run, not both selected Rovers replicates. Sources are the copied main transcript, saved policy diffs, and final controller. No new evaluations were run. Arrow sequences describe recorded order, not proof of hidden causation.

## What generalizes from Obstruction2D?

Phase decomposition appears in both inspected controllers. Absence of explicit multi-step search does not: Rovers 424 includes A*-style navigation in its first saved policy and final policy. This is a concrete counterexample to an all-environments claim, not an estimate of prevalence. Its task-level sample/images/send/drop/home sequence remains programmed rather than searched.

## 1. A planned route can fail because execution changes its direction

**Compute a route judged clear by the model → encounter collisions → diagnose motion deviating from the planned segment → preserve the segment direction in the action command.**

At [L54](01_timeline.md#E0054), the agent attributes an important navigation failure to separately clipping x and y movement. The [6a2200f diff](02_code_changes.md#C021) replaces independent clipping with one scale factor. As a mathematical illustration, a requested vector (0.4, 0.1) independently clipped to 0.2 becomes (0.2, 0.1), which changes direction; shared scaling produces (0.2, 0.05), which preserves direction. These illustrative numbers are not an archived action.

Interesting question: when predictions fail, does the agent change the world model, the planned route, or the mechanism that executes the route? Here the visible diagnosis and edit target execution. The correction does not prove the geometry model itself is universally accurate.

## 2. It turns a troublesome parameter tradeoff into a conditional strategy

**Large obstacle clearance blocks narrow routes → smaller clearance risks collisions → search with the larger margin first → retry with a smaller margin only if no route is found.**

[L87](01_timeline.md#E0087) states the tradeoff. [bc97ce1](02_code_changes.md#C026) introduces a two-margin planner, initially using 0.20 and 0.185. The final [approach.py](evidence/final/approach.py), lines 127–131, uses 0.21 and 0.195 after further tuning.

This is a structural change from choosing one global margin to conditioning the margin on a search result. No probability of model correctness or expected utility is computed, so it should not automatically be called Bayesian or resource-rational planning.

Interesting question: when does the agent replace a single tuned rule with a conditional fallback?

## 3. It abandons an apparently better search objective after testing

**Reason that diagonal and axial motion each cost one action → change grid costs and heuristic → test → restore the earlier geometric search costs.**

[L250](01_timeline.md#E0250) announces the optimization. [4e995ed](02_code_changes.md#C041) changes diagonal cost from 1.414 to 1 and switches to a Chebyshev heuristic; it also adds sampling on arrival. [0d4421d](02_code_changes.md#C042) reverses only the search-cost change, preserving arrival sampling. The three matched ordinary seeds at [L254](01_timeline.md#E0254) versus [L258](01_timeline.md#E0258) finish in 65/56/31 versus 64/54/31 steps; all pass. [L265](01_timeline.md#E0265) describes keeping the empirically shorter planner.

The observed difference is small and from three cases. It does not show that the restored objective is generally better or isolate why smoothing and continuous execution change route efficiency. It does show selective rollback rather than wholesale rejection of both changes.

Interesting question: what evidence makes the agent abandon an appealing model-based optimization, and which parts does it preserve?

## 4. It investigates conflicting evidence before editing the policy

**Many numerical tests pass → visualization appears suspicious → rerun the same seed and object count numerically → observe success.**

[L228](01_timeline.md#E0228) renders seed 42 with four objectives. At [L237](01_timeline.md#E0237), the agent explicitly says it will treat the suspicious visual case as a failure until checked. [L239](01_timeline.md#E0239) runs pinned counts 1–4 for seed 42; the four-objective case succeeds in 58 steps. No policy edit occurs between L237 and this check. At [L250](01_timeline.md#E0250), the agent attributes the visual concern to frames covering only an early part of the trajectory.

Supported: an exact-case numerical check before editing, and a successful rerun. The explanation about the visualization is the agent's recorded attribution; this analysis has not independently reconstructed the removed rendered frames.

Interesting question: does the agent distinguish a policy failure from incomplete or misleading observations, and how does it choose the follow-up measurement?

## Additional controller behavior worth testing

If both clearance-based searches fail, the final `_plan` returns the goal directly. The robot can therefore attempt direct movement even when the model found no route. This is an implemented fallback, not evidence that it occurred in any particular final evaluation. Measuring its actual use would require an instrumented replay. It is another reason to describe this controller as a combination of planning and fallback rules.

## A research question that spans both environments

**When observed behavior disagrees with expectations, what does the coding agent revise: its model of the environment, its plan, its execution code, or its way of gathering evidence?**

The four sequences above offer candidate examples, not exhaustive labels or causal results. The initial implementation of A* means this run is especially useful for comparing model/plan/execution failures with Obstruction2D's predominantly heuristic repairs.

<a id="controller-details"></a>
## Controller and development evidence


Status: first manual annotation for review, 2026-10-09. This is a fresh strict-blackbox development run according to saved provenance. Final policy commit `0d4421d`; the archived working policy matches it. All 404 lines of the final policy were read, its internal calls traced, the initial policy and relevant diffs inspected, and main-transcript evidence checked. No new environment rollout was run.

## Task in plain language

Two rovers must collect a stone analysis and a soil analysis, photograph every objective, transmit all required information, empty their stores, and return home. Sampling requires proximity and an empty store; each image requires calibration; transmission requires visibility of the lander. Obstacles constrain driving and visibility. This creates dependencies between actions, not just a single movement goal. See [task.md](evidence/task.md).

## Finding: phases and explicit look-ahead coexist

The final code has per-rover persistent phases:

**sample → images → send → drop → home**

These are actual stored phase values, initialized at line 88 and read/changed in `get_action` from line 310 onward. Each phase can span many calls. The sample phase can itself drop a sample; the image phase alternates calibration and imaging according to observed state. Transitions use completion flags rather than a single predetermined timer. The two rovers each carry their own phase.

Inside those phases, motion is selected through:

**get_action → _move → _plan → _plan_with_margin → cached route → next motion command**

`_move` is called for sampling (330), imaging (348), transmission (377), and returning home (399). It plans when the destination changes, no route remains, or the rover is stuck (188–201).

### Why the planner is explicit look-ahead

Read [approach.py](evidence/final/approach.py), lines 127–186. The code implements an A*-style search:

1. Convert current and goal positions to a grid with **0.05 m** spacing. The comment still says 0.1 m; the numeric assignment is authoritative.
2. Start a priority queue and record accumulated path cost and predecessors.
3. Generate up to eight neighboring positions from each expanded position.
4. Reject hypothetical positions using `_blocked`.
5. Prioritize candidates by accumulated cost plus estimated remaining distance.
6. Reconstruct the multi-step route and shorten it using straight-line clearance checks.
7. Follow the resulting waypoints through `_move`.

These candidate positions are computed before the rover executes them. This is stronger evidence of explicit multi-step look-ahead than Obstruction2D's future-pickup clearance rule.

The model is an approximate 2D navigation model: obstacle rectangles expanded by safety margins, arena bounds, a hard-coded central divider, an approximated lander footprint, and the other rover's current position. It is not a full physics simulator or joint prediction of the two rovers' future behavior. It does not search the space of sample/calibrate/image/send/drop task sequences. Those task phases are programmed explicitly.

Additional one-step prediction: lines 333–335 calculate `current_position + commanded_movement` and issue SAMPLE on the same step if the predicted position is close enough. This assumes the commanded motion occurs; collision rejection can invalidate that prediction.

### Evidence that this is used, not just a named function

- The call chain above connects the planner output directly to returned motion commands.
- [Transcript L80](01_timeline.md#E0080) records calls to `_plan` for three cases where `_line_free` is false. The printed results are two-waypoint routes, not just the destination. These routes are computed after reset, without stepping the environment inside the probe. Thus historical planner execution is directly visible in development.
- [L93](01_timeline.md#E0093) and [L95](01_timeline.md#E0095) compare routes under different clearance margins.
- [L271](01_timeline.md#E0271) records the final code finishing four pinned-count tests with both phase values `home`. This shows final controller execution, but is not per-call instrumentation proving which final episodes expanded the A* branch versus taking the straight-line shortcut.

Only standard `heapq`, `math`, and NumPy are imported. The search loop and collision checks are implemented inside the generated policy, not a call to an imported planning library. The A* algorithm is conventional; generated implementation does not imply invention.

## Development evidence

The first saved policy, [0f846f8.py](evidence/versions/C012_0f846f8_approach.py), already has phases and A*. [L10](01_timeline.md#E0010) announces grid-based navigation before the policy is written; L14 records the file addition and L16 the first test. The initial test fails at 1,000 steps. A planner's existence therefore does not imply an immediately correct controller.

The subsequent sequence is:

**write phase controller with grid search → encounter collisions → change geometry/clearance assumptions → fix path following → vary clearance and grid resolution → add fallback planning → repair sample and visibility handling → try a different path-cost metric → restore the earlier cost metric → validate.**

Three useful development episodes:

1. **Planned route versus executed motion.** [L54](01_timeline.md#E0054) says separately clipping x and y caused motion to deviate from the planned segment. The [6a2200f diff](02_code_changes.md#C021) replaces separate clipping with a shared scale factor, preserving direction. This is an implementation mismatch between plan and execution, not absence of planning.
2. **Model conservatism versus reachability.** [L87](01_timeline.md#E0087) explains that a large clearance can close a feasible narrow passage, while smaller clearance may graze obstacles. The final planner tries margin 0.21 first and 0.195 second. This is choosing among model approximations using observed behavior.
3. **Search objective versus actual outcome.** [L250](01_timeline.md#E0250) proposes unit-cost diagonal moves with a Chebyshev heuristic. [4e995ed](02_code_changes.md#C041) implements that and sampling on arrival. [0d4421d](02_code_changes.md#C042) restores the earlier geometric costs while retaining arrival sampling. The same three ordinary seeds in L254 versus L258 take 65/56/31 versus 64/54/31 steps; both versions solve all three. This is a small observed efficiency difference, not a population-level result. [L265](01_timeline.md#E0265) states why the agent kept the older cost metric.

## Limits of the model

- Task/operator sequences are fixed by phases, not searched.
- The other rover is treated as a current obstacle, not a future moving trajectory.
- If both searches fail, `_plan` returns the goal directly (line 131), bypassing a guaranteed clear route. Some actions therefore need not follow a successful search result.
- Search uses approximate geometric tests, shortcuts, and an approximate goal threshold. This analysis does not establish path optimality or collision-free execution.
- The readable transcript contains explanations; this case has not received a backend-session reasoning audit. No hidden internal reasoning claim is made.

## Annotation for review

| Feature | Assessment | Evidence |
| --- | --- | --- |
| Persistent phase decomposition | Supported | Final lines 88, 310–402; observed final phases at L271 |
| Explicit multi-step geometric look-ahead | Supported | Search at 133–186; action call path; executed development probes L80/93/95 |
| One-step action consequence prediction | Supported | Final lines 333–335 |
| Full dynamics rollout | Not found in complete final policy | Geometry and kinematic neighbor positions only |
| Search over task/operator sequences | Not found in complete final policy | Explicit sample/images/send/drop/home branches |
| Planner implementation | Implemented in generated file | Imports and search loop; present in initial saved policy |

This is one run. It challenges an either/or classification between phases and planning, and demonstrates look-ahead somewhere outside Obstruction2D. It does not yet show how consistently either mechanism occurs across tasks.

Source paths and SHA-256 hashes are in [evidence_manifest.json](evidence/manifest.json). Full policy history is in [policy_history.json](evidence/commits.json); the original-format stream and readable completed-event transcript are included. Historical commands and instructions are data only.

## Your inspection notes

### Next finding — working title

- Sequence/event IDs:
- Observed evidence:
- Interpretation:
- Alternative explanation:
- Next check:
- Status:
