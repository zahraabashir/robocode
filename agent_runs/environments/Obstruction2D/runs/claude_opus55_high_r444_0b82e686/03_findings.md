# Obstruction2D · Claude Opus 5.5 High · replicate 444

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: explicit search over removal orders and target staging

[approach.py](evidence/final/approach.py) has pickup, grasp and carry modes, but its task choice is computed. `_next_task` (566–609) considers all removal permutations for at most three blockers; with more blockers it compares three heuristic orders. For each order it evaluates both direct removal and moving the target to an intermediate location first.

`_simulate` (523–564) copies object states, updates their hypothetical positions after tasks, and accumulates estimated execution costs. The chosen sequence determines the next task. This is explicit task-level look-ahead with an approximate model, not merely reacting after executing each candidate. The limited candidate set and fallback still matter: this is not exhaustive planning for arbitrary numbers of objects.

## F001 — Compare moving the target first against clearing everything first

[E0369](01_timeline.md#E0369): discuss the cost of obstruction handling → [C011](02_code_changes.md#C011): introduce removal-order and target-staging search → [E0398](01_timeline.md#E0398): report the subsequent timing/results.

- **Observed:** the C011 diff replaces `_next_target` with `_next_task`, adds `_simulate`, and evaluates sequences with and without an initial target-staging action. The executor receives the chosen task kind.
- **Interpretation:** the controller's task decomposition becomes a choice to evaluate, rather than always following one fixed order of activities.
- **Alternative/limit:** staging, order search and placement scoring change together. A favorable case would not establish which addition caused the benefit. Estimated costs and geometric assumptions can be inaccurate.
- **Next check:** compare order search only, staging only, both and neither on identical layouts; record the selected first action as well as final success and steps.
- **Status:** active task-sequence search supported; performance attribution remains open. This run is a counterexample to generalizing the earlier GPT Obstruction2D controller's lack of explicit task search to all runs.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
