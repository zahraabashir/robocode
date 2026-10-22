# DynPushT2D 424 — findings and your notes

[Timeline](01_timeline.md) · [All commits and changed lines](02_code_changes.md) · [Final controller](evidence/final/approach.py)

**Prior manual analysis migrated for review.** No new rollouts or private-reasoning claims were added during reorganization. Your notes in this file are preserved when the timeline is rebuilt.

## Start here

- **F001 — Architectural rewrite:** [E0043](01_timeline.md#E0043) → [E0045](01_timeline.md#E0045) → [E0047](01_timeline.md#E0047) → [E0049](01_timeline.md#E0049). Read the explanation, deletion/addition, and actual diff together.
- **F002 — Planning and feedback coexist:** compare the A* routine with the rotation/translation stop conditions in the final code. The route search holds the current block pose fixed.
- **F003 — Anticipating wall interference:** inspect centerward prepositioning before rotation; it is a clearance rule, not a search over contact trajectories.

<a id="controller-details"></a>
## Controller and development evidence


Manual annotation for review, 2026-10-09. **Phase rules + explicit geometric A* + analytic contact heuristics + feedback.** No multi-step push-dynamics rollout or search over alternative manipulation sequences was found in the complete final program.

## Implemented mechanisms

All line numbers below refer to the copied final [approach.py](evidence/final/approach.py), whose SHA-256 matches the archive manifest and saved HEAD. The final policy imports only `heapq`, `math`, and NumPy; it does not invoke a simulator or another generated controller module.

| Mechanism | Evidence and interpretation |
| --- | --- |
| Phase decomposition | Lines 22–37 initialize persistent state; 180–222 choose a manipulation; 232–302 execute `nav`, `rot1`, `rot2`, `translate`, and `retreat`. This is executable phase state across calls. |
| Geometric model | Lines 45–55 transform the robot point into the block frame and test two expanded rectangles plus arena limits. These are controller assumptions about geometry. |
| Explicit look-ahead | Lines 57–122 expand alternative grid positions, reject blocked successors, accumulate path costs, prioritize by cost plus distance heuristic, and reconstruct waypoints. Actual code uses eight neighbors on a 0.10 grid, despite the stale “4-neighbour” docstring. |
| Connection to actions | `get_action` → `_begin_decision` → `_start_nav` → `_plan`; route following at 237–257 returns actions toward waypoints. The second rotation contact also calls `_start_nav` at 270. Thus search is on the policy's action path, not an unused helper. |
| Contact selection | Lines 148–170 calculate a centroid for the assumed T geometry and test seven candidate push directions. Each is scored for geometric accessibility and alignment with desired translation. There is no predicted future block trajectory for those candidates. |
| Anticipatory manipulation rule | Lines 190–195 move a block away from a wall before trying to rotate it. This encodes a clearance assumption about the later rotation, without searching rotation trajectories. |
| Feedback | Lines 274–300 stop strokes using observed angular change, observed translation, or step caps. Paired rotation contacts are scripted, not selected by comparing simulated multi-push outcomes. |

The model searched by A* is **possible pusher positions around a currently stationary T**, not the evolving robot–block contact system. Even imperfect geometry is still a model used in search; classification does not certify its accuracy or collision-free physical execution. The comments' “force” variables ultimately become robot displacement actions.

Fallbacks matter: `_plan` returns a direct goal if no free goal/search result is found (78–79, 104–105). Navigation also abandons a route after a stall (251–256). Therefore not every returned movement is backed by a successfully found route. Final branch frequencies were not measured.

## Development evidence

[Policy history](evidence/commits.json) contains 11 commits touching the controller. `_plan` first appears in the fifth, `2fc7f82`. The previous [ab58679 controller](evidence/versions/C016_ab58679_approach.py) uses geometric orbit/stage/push rules without a graph search. The [replacement diff](02_code_changes.md#C018) adds the collision model, A*, explicit rotation pair, and centroid-based contact choice.

[Transcript L43](01_timeline.md#E0043) supplies the readable explanation: probes changed the agent's interpretation of the reported block coordinates. L45 deletes the file, L47 adds it, and L49 records the replacement commit (207 insertions, 51 deletions). L51 records a test of the replacement. [L55](01_timeline.md#E0055) shows runtime `nav`, `rot1`, `rot2`, `translate`, and `retreat` phases; these support historical execution of the architecture, not a complete final-policy branch audit. Several subsequent fixes remain necessary, so the rewrite should not be described as immediately solving all tasks.

Compact sequence:

> orbit/stage/push heuristic → probes and revised geometry interpretation → substantial rewrite with A* and contact rules → tests expose remaining navigation/angle problems → refine contact accessibility, routing, stall recovery, and wall clearance.

## Scope and classification

Supported: phase decomposition, geometric multi-step look-ahead, geometric/mechanics-informed contact choice, feedback. Not found in inspected final code: learned value/reward policy, dynamics rollouts of candidate pushes, task-sequence search. “Model-free RL” is not an appropriate name for hand-written feedback rules merely because those rules lack dynamics rollouts.

Read the final controller in full, the main readable messages, and relevant historical changes/outputs. All saved policy versions and diffs were exported, but not every development helper/backend session was audited. This is not an ACT*ONOMY transcript annotation or an inference about private reasoning. No environment code or archived commands were executed. See [evidence manifest](evidence/manifest.json) and the [two-run comparison](../../overview.md).

## Your inspection notes

### Next finding — working title

- Sequence/event IDs:
- Observed evidence:
- Interpretation:
- Alternative explanation:
- Next check:
- Status:
