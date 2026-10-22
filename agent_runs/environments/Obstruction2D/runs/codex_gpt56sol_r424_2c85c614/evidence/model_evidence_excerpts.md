# Selected readable evidence about prediction and planning

Eight preserved rollout files; counts are records, not unique thoughts. Forked sessions can repeat inherited history. Encrypted payloads omitted. Selected helper messages are proposals, not proof of execution or main-agent adoption.

## E1: archived helper agent

Source: `/Users/zahra.bashir/.cache/robocode-results-viewer/1sNuRoRxMxh7_VDE93hWn_ZNHBd74Uzt2/runs/Blackbox/Codex GPT5.6 Sol/kinematic2d/obstruction2d_generalized__agentic__none__blackbox__strict__codex_gpt56sol__timeout_60s__99b3a73f/2026-09-08_22-07-59/replicate_424/sandbox/.agent_sessions/codex/2026/09/08/rollout-2026-09-08T22-08-33-01a082a2-f8b8-7c61-a29b-46574d0345ee.jsonl`; original line 40.

Recommended controller is a feedback-driven finite-state machine using top-down grasps:

- Choose a feasible horizontal slot on the target surface, minimizing movable obstruction conflicts and rejecting static conflicts.
- Clear only conflicting obstructions, topmost first.
- Face the gripper downward, grasp each rectangle from above, verify attachment by observed object motion, lift above all geometry, move sideways, and release beyond the platform.
- Replan after every release.
- Grasp and carry the target without rotating it, center it in the chosen slot, lower its bottom to the surface top, release, and withdraw.
- Retry failed grasps with progressively deeper contact and small lateral offsets.

Likely end-effector reach is:

```python
base_radius + arm_joint * arm_length + gripper_width / 2
```

with `arm_joint` normalized; the alternate interpretation is direct extension `base_radius + arm_joint + ...`, so this should be confirmed empirically.

I sent the parent agent the full geometry, slot-selection, parking, grasp-verification, and recovery details.

## E2: archived helper agent

Source: `/Users/zahra.bashir/.cache/robocode-results-viewer/1sNuRoRxMxh7_VDE93hWn_ZNHBd74Uzt2/runs/Blackbox/Codex GPT5.6 Sol/kinematic2d/obstruction2d_generalized__agentic__none__blackbox__strict__codex_gpt56sol__timeout_60s__99b3a73f/2026-09-08_22-07-59/replicate_424/sandbox/.agent_sessions/codex/2026/09/08/rollout-2026-09-08T23-02-20-01a082d4-33c4-7a02-8922-e54dc085f63f.jsonl`; original line 79.

Recommended minimal fix: order the temporary target and all blockers by descending world-space top edge, not blocker height with the crowded target forcibly first.

```python
def top_y(o):
    th = state.get(o, "theta")
    w = state.get(o, "width")
    h = state.get(o, "height")
    return state.get(o, "y") + 0.5 * (
        abs(math.sin(th)) * w + abs(math.cos(th)) * h
    )

tasks = obstacles + ([target] if crowded else [])
tasks.sort(key=top_y, reverse=True)
self.todo = [o.name for o in tasks] + [target_name]
```

This directly addresses the likely seed 18 mechanism: while attempting the lower target, the descending vacuum contacts a taller overlapping blocker. The controller only monitors the intended object, so it carries and drops the wrong object before retrying.

A secondary safeguard can identify whichever movable object actually rises during `lift` and adopt it as the current task. Preserve the final-target invariant when doing so: if the accidentally attached object is the target, insert the displaced blocker after the temporary target and increment `final_index`; never swap a blocker into the final target slot.

## E3: archived helper agent

Source: `/Users/zahra.bashir/.cache/robocode-results-viewer/1sNuRoRxMxh7_VDE93hWn_ZNHBd74Uzt2/runs/Blackbox/Codex GPT5.6 Sol/kinematic2d/obstruction2d_generalized__agentic__none__blackbox__strict__codex_gpt56sol__timeout_60s__99b3a73f/2026-09-08_22-07-59/replicate_424/sandbox/.agent_sessions/codex/2026/09/08/rollout-2026-09-08T23-02-29-01a082d4-56bf-7120-9d77-c12d3440135f.jsonl`; original line 74.

Most likely cause: blockers enter `carry` as soon as `oy >= 0.30`, too low to clear adjacent clustered rectangles. Horizontal motion is rejected, and after three stalls the policy intentionally releases the blocker in place.

Focused probes:

1. Trace seed 18 at phase changes: active object, robot/object positions, commanded `dx`, actual deltas, vacuum, and all obstacle bounds.
2. Compare blocker lift thresholds `0.30`, `0.40`, and `0.50`. Success only at higher values confirms insufficient clearance.
3. At the first stalled carry pose, try `dx=±0.005` with vacuum on. One working direction indicates directional trapping; neither indicates inadequate lift.
4. Raise by `0.01` repeatedly and retry tiny horizontal steps to measure the minimum escape height.
5. Check whether `ox-rx` remains constant during a clear vertical step. If not, the controller’s latched `attached` flag is a false positive.

I sent these probes and the likely failure mechanism to the parent agent.

## E4: main coding agent

Source: `/Users/zahra.bashir/Desktop/phd/robocode/actonomoy/run_424_sequence_map/evidence/stream.jsonl`; original line 155.

The core manipulation path is working—objects are lifted, parked, and the block reaches the geometrically correct surface pose—but the live termination check is exposing a subtle contact/containment discrepancy. I’m using a rendered rollout now to distinguish a visual placement offset from a state-machine timing issue.

## E5: main coding agent

Source: `/Users/zahra.bashir/Desktop/phd/robocode/actonomoy/run_424_sequence_map/evidence/stream.jsonl`; original line 338.

The focused trace revealed a concrete state-estimation bug: when a floating object is pushed downward during a retry and then re-lifted, attachment verification compares against its old elevated position and incorrectly declares failure. I’m correcting verification to track the lowest observed pickup height, which directly targets the rare clustered failures without changing nominal trajectories.

## E6: main coding agent

Source: `/Users/zahra.bashir/Desktop/phd/robocode/actonomoy/run_424_sequence_map/evidence/stream.jsonl`; original line 374.

Two fresh failures expose complementary edge cases: one near-height blocker should defer to temporarily moving the target, and one parking slot overlaps an obstacle that has not yet been processed. I’m widening the near-height ordering tolerance and rejecting parking columns that interfere with future pickup objects.

## E7: main coding agent

Source: `/Users/zahra.bashir/Desktop/phd/robocode/actonomoy/run_424_sequence_map/evidence/stream.jsonl`; original line 383.

A repeated seed-18 check caught an overcorrection: the wider height tolerance moved the target before a genuinely overlapping taller blocker. I’m refining the rule so any physically overlapping higher object always goes first, while the tolerance only governs separated near-height neighbors.

## E8: main coding agent

Source: `/Users/zahra.bashir/Desktop/phd/robocode/actonomoy/run_424_sequence_map/evidence/stream.jsonl`; original line 392.

Seed 59 reveals the last structural parking issue: when two blockers must move in the same direction, the nearer one was parked first in the inner slot, blocking the later object’s route. I’m prioritizing outermost surface-clear slots first; existing future-pickup and footprint constraints remain in place.

## E9: main coding agent

Source: `/Users/zahra.bashir/Desktop/phd/robocode/actonomoy/run_424_sequence_map/evidence/stream.jsonl`; original line 454.

Seed 93 has no physically adequate second ground-level slot: both side clearances are too tight after the first blocker is parked. The robust fallback is vertical stacking at the already-safe outer column, carrying the later blocker above the first instead of accepting a goal-adjacent slot.

## E10: main coding agent

Source: `/Users/zahra.bashir/Desktop/phd/robocode/actonomoy/run_424_sequence_map/evidence/stream.jsonl`; original line 514.

Seed 53’s failure is caused by a useful side effect: moving the first overlapping blocker also sweeps the second blocker safely away, but the controller still insists on grasping it at its new wall-adjacent pose. I’m adding a live relevance check so already-cleared blockers are skipped instead of retried.
