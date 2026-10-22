# Obstruction3D · Claude Opus 5.5 High · replicate 222

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: predicted trajectories can merge execution stages

[approach.py](evidence/final/approach.py) contains forward/inverse kinematics. `_jplan_to` (737–789) tries base positions and arm configurations, can reject a choice that makes a later goal unreachable, and uses `_path_ok` (791–803) to check clearance along interpolated joint motion. These are explicit geometric predictions before execution, not a full search over removal orders in the inspected task selector.

The executor normally queues travel and descent separately. With **`MERGE=True`**, `_merge` (805–833) attempts a combined joint movement. If it cannot find a suitable path it falls back to separate stages; a rejected joint move can temporarily disable merging. Thus the apparent phase boundaries are conditional, not an invariant plan template.

## F001 — Introduce joint-space planning, then combine previously separate stages

[C015](02_code_changes.md#C015): add joint-space travel → [C018](02_code_changes.md#C018): expand base-position candidates → [C020](02_code_changes.md#C020): enable merged travel/descent and its fallback → [E1706](01_timeline.md#E1706): the final message describes the combined motion.

- **Observed:** the C020 diff adds the lazy/combined execution route and temporary disabling after a rejected move. The final call path reaches `_merge` from `get_action` (580–588).
- **Interpretation:** development changes the boundaries between subtasks, rather than only tuning actions within fixed phases. A model is used to decide when two stages can share one trajectory.
- **Alternative/limit:** an active flag establishes availability, not how often the branch ran or succeeded in saved evaluation episodes. Simultaneous planning changes could explain any reported efficiency gain.
- **Next check:** record merge attempts, acceptance and rejection on identical cases with merging enabled/disabled; compare collision rejection and steps while holding the planner fixed.
- **Status:** mechanism and structural edit supported; execution frequency and benefit unmeasured here.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
