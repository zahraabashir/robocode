# Obstruction2D · Claude Opus 5.5 High · replicate 24

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: geometric path planning with heuristic task order

[approach.py](evidence/final/approach.py) uses a persistent generator to execute pickup and placement legs. Its task order remains a nearest-object heuristic in the inspected `_plan` (753–813), while motion uses explicit search: `USE_ARM_DP=True` (48) enables a dynamic program over horizontal position, height and arm extension. `_move` (495–500) calls `_dp_path3` to obtain a path through predicted free configurations.

Two flags must be kept separate. The geometric motion planner is active; **`COST3=False`** disables using that more expensive planner merely to score candidate placements (`_path_cost`, 310–329). Thus the program uses a model where it builds motion, but a cheaper estimate in this placement-ranking calculation. This is not evidence of a full search over object-removal orders.

## F001 — Keep a planner for motion, stop using it as a cost estimator

[C010](02_code_changes.md#C010): add arm-extension dynamic programming → [E0497](01_timeline.md#E0497): report improvement → [E0543](01_timeline.md#E0543): say the richer cost estimate brings no gain and is slower → [C012](02_code_changes.md#C012): gate that estimator with `COST3=False`.

- **Observed:** the C012 diff changes the cost-estimation route while leaving arm-extension path planning active. This is selective use of a model, not a wholesale removal of planning.
- **Interpretation:** the agent chooses different computational detail for two parts of the controller.
- **Alternative/limit:** the message is a performance claim, and other scoring changes can affect placement choices. A disabled feature alone does not establish resource rationality.
- **Next check:** compare the two scoring options with identical layouts and candidate placements; measure selected placement, predicted versus actual travel, and computation time.
- **Status:** selective use is supported by active flags and call sites; the quality/time tradeoff remains to test.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
