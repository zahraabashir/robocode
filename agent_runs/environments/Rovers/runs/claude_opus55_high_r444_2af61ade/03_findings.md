# Rovers · Claude Opus 5.5 High · replicate 444

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: task-order search followed by spatial and temporal refinement

[approach.py](evidence/final/approach.py) uses `_rover_tables_h.dfs` (400–431) to compare task orders with predicted task/calibration state. `_plan` (434–562) assigns tasks between the two rovers and compares candidate schedules. `_refine` and `_realize` (564 onward) refine the chosen sequence on a finer spatial grid and use a predicted other-rover trajectory for transmission timing. A computation-time flag can skip expensive refinement.

The executor follows the computed operations and motion. Calling this simply phase-based would miss the search that determines those stages and their timing.

## F001 — A richer timing model breaks an assumption in plan extraction

[E0664](01_timeline.md#E0664): discuss transmissions blocked by the moving other rover → [C009](02_code_changes.md#C009): add timed transmission handling → [E0760](01_timeline.md#E0760): diagnose waiting that the old backtracking rule cannot represent → [C011](02_code_changes.md#C011): repair backtracking → [E0804](01_timeline.md#E0804): report 120/120 with no replans.

- **Observed:** C011 carries timed transmission information through the planner and relaxes a predecessor-time comparison so waiting can be represented, while retaining the timing check for the operation. The diff supports a representation repair at the interface between planning and execution.
- **Interpretation:** better prediction requires changes beyond the model itself: the plan extractor must be able to express the new schedules.
- **Alternative/limit:** the result is an agent report, not a new validation here. Other fixes in the same period may affect success. The new model's accuracy has not been established by this reading.
- **Next check:** construct saved-state cases that require waiting; compare the predicted schedule, extracted actions and actual transmission time before/after the repair.
- **Status:** timing/backtracking change supported; robustness and performance effects remain to test.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
