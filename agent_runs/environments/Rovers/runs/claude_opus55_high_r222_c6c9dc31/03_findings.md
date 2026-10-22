# Rovers · Claude Opus 5.5 High · replicate 222

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: task-state dynamic programming, not a fixed phase template

[approach.py](evidence/final/approach.py) searches over completed-task subsets, the last task and spatial grid states (`_plan_inner`, `_assign`, `_propagate`, 150–465). Calibration is represented in the planning calculation. Plans are extracted into position/operation sequences (`_extract`, 515–597), then executed using a plan pointer and checked outcomes (600–697). Planning also refines transmission assumptions using the other rover's predicted trajectory.

This is explicit task and spatial look-ahead. The operation sequence is computed, even though execution has a current plan position. The final controller does not retain the experimental camera-heading planner described below.

## F001 — A more elaborate planner is saved, but the earlier policy is restored

[C016](02_code_changes.md#C016): add camera-heading planning → [C017](02_code_changes.md#C017): repair it → [E1210](01_timeline.md#E1210): report a smaller-than-expected gain → [C018](02_code_changes.md#C018): revert, citing about 0.045 steps gained at twice the planning time → [E1466](01_timeline.md#E1466): explain keeping the simpler option.

- **Observed:** the saved `approach.py` snapshot at C018 is byte-identical to C015, before the camera-heading addition. The experimental controller is preserved separately. This verifies a rollback, rather than relying only on the commit title.
- **Interpretation:** the agent weighs a small reported quality gain against a larger reported computation cost.
- **Alternative/limit:** the quoted tradeoff is the agent's report, not an independently reproduced estimate. Noise, a limited test set or remaining defects could also explain the decision. It is a candidate resource-allocation case, not proof of optimal resource rationality.
- **Next check:** compare both preserved versions on identical held-out cases with per-instance planning times and uncertainty in the step difference.
- **Status:** exact rollback and stated rationale supported; optimality and general benefit uncertain.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
