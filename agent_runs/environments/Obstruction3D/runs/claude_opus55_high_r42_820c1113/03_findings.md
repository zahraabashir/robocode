# Obstruction3D · Claude Opus 5.5 High · replicate 42

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: kinematic motion with local counterfactual checks

[kin.py](evidence/final/kin.py) supplies forward kinematics and numerical inverse kinematics. [approach.py](evidence/final/approach.py) uses pickup, grasp, placement and release phases (446–561), with waypoint tracking constrained by joint movement limits.

`_plan_next` (142–242) can temporarily remove one obstruction from a geometric check to estimate whether doing so clears a grasp. This is a local hypothetical-state calculation. It differs from simulating complete alternative object-removal sequences; that broader search was not found in the inspected task-selection function.

## F001 — Add a future-travel term, then remove it

[E1164](01_timeline.md#E1164): propose accounting for pickup → parking → target travel → [C018](02_code_changes.md#C018): add the term → [E1189](01_timeline.md#E1189): report worse mean steps and decide to revert → [C019](02_code_changes.md#C019): remove it.

- **Observed:** the C019 diff removes the `W_TRAVEL` calculation that includes travel from a proposed parking spot toward the target. It also restores earlier clearance weights and current-object travel scoring. Kinematic control remains active.
- **Interpretation:** a more anticipatory scoring rule is considered and rejected in the visible development sequence.
- **Alternative/limit:** the agent reports 24.4 versus 23.6 mean steps, but this is not a new independent measurement. Because several scoring terms change, it does not show that anticipation itself hurts performance.
- **Next check:** change only the future-travel term on identical episodes, preserving clearance weights; compare placement choices, success and steps.
- **Status:** addition and removal supported; the causal explanation is uncertain.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
