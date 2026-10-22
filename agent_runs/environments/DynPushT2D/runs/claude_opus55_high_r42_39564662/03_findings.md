# DynPushT2D · Claude Opus 5.5 High · replicate 42

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: active two-push prediction

[approach.py](evidence/final/approach.py) separates navigation and pushing into queued segments (`_build`, 282–318). Navigation searches a visibility graph using Dijkstra. `_eval` (144–236) repeatedly calls a contact model, [tmodel.py](evidence/final/tmodel.py), to predict how a candidate push moves the block. `_plan` (238–280) evaluates a second push from the predicted endpoint of a first push. That second outcome can change the first choice: this is explicit look-ahead before execution.

`LOOKAHEAD=16` controls how many first-push candidates receive this extra evaluation; it does not mean sixteen pushes deep. Two-push evaluation is conditional on the fine-positioning flag and accumulated planning time being below 25 seconds. When disabled, the controller still predicts the result of a single push segment. Execution observes the real block and can replan.

## F001 — Successful tests are followed by deeper planning

[E0347](01_timeline.md#E0347): the agent reports all 400 cases solved and proposes improving step efficiency → [C005](02_code_changes.md#C005): add two-push look-ahead → [E0365](01_timeline.md#E0365): report lower mean steps.

- **Observed:** the C005 policy diff passes the predicted block and robot endpoint into another `_eval` call. This is a verified algorithmic addition, beyond a message claiming to plan ahead.
- **Interpretation:** development shifts from solving cases toward choosing more efficient actions after reported success.
- **Alternative/limit:** the message's performance comparison is not an independently reproduced result. Search width and other changes also evolve later. The runtime cutoff does not prove that the coding agent itself follows an optimal computation budget.
- **Next check:** hold the harness, cases and candidate set fixed; compare depth one versus two, recording first-action disagreements, steps and planning time.
- **Status:** active predictive mechanism and edit supported; performance benefit and resource-rational explanation remain hypotheses.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
