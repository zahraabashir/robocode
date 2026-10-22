# Rovers · Claude Opus 5.5 High · replicate 42

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: computed task orders and predictive operations while traveling

[approach.py](evidence/final/approach.py) enumerates task orders in `_rover_costs` and assignments in `_make_plan` (280–358). Navigation costs come from Dijkstra distance fields (`field_from`, 138–149). The task sequence is computed by search, not a fixed list of activity phases.

`_target` and `_lookahead` (589–708) connect a current operation to the next task. `_lookahead` predicts whether operations will be valid at upcoming positions while the rover starts traveling toward the next task—for example, calibration at one predicted position followed by imaging at the next. The executor (710–780) can combine movement with the predicted-valid operation. Transmission checks also use predicted other-rover positions.

## F001 — Reduce idle operation steps by overlapping tasks and movement

[E0779](01_timeline.md#E0779): inspect nonmoving steps of the rover that determines completion time → [C011](02_code_changes.md#C011): add predictive operation/travel overlap → [E0795](01_timeline.md#E0795): report a small improvement.

- **Observed:** C011 adds `_lookahead` and connects its operation choice to returned actions. This is not merely renaming phases: the controller predicts whether it can finish one task while moving toward another.
- **Interpretation:** development changes the scheduling relationship between task completion and travel.
- **Alternative/limit:** the reported gain is not independently reproduced, and an approximate validity model may fail in some geometries. Computed task order itself can also change total time.
- **Next check:** keep the task plan fixed and compare overlap enabled/disabled on the same instances; inspect predicted and actual validity for each combined action.
- **Status:** predictive overlap mechanism supported; general performance effect open.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
