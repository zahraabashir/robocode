# DynPushT2D · Claude Opus 5.5 High · replicate 444

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: dynamics rollouts remain active; a second push does not

[model_v.py](evidence/final/model_v.py) implements an approximate contact/dynamics model. In [approach.py](evidence/final/approach.py), `eval_pushes` (259–333) predicts up to 40 actions for candidate pushes and scores their predicted outcomes. `plan_push` (335–366) selects among them. Dijkstra navigation and `plan/nav/push` modes connect these predictions to returned actions; feedback and periodic replanning remain active.

The distinction is in line 166: **`self.M = 0`** disables the optional second-push branch at line 343. The final controller still performs multi-step prediction within a push. It would be wrong either to label it as having no look-ahead or to count its unused two-push branch as active planning.

## F001 — Deeper planning is tried, disabled, and reconsidered

[E0498](01_timeline.md#E0498): propose two-level planning → [C010](02_code_changes.md#C010): add it → [E0514](01_timeline.md#E0514): report worse results and more computation → [C011](02_code_changes.md#C011): change `M` from 8 to 0 → [E0539](01_timeline.md#E0539): consider retrying after other improvements → [E0779](01_timeline.md#E0779): again prefer `M=0`.

- **Observed:** the C011 diff disables the second-push search; the final default preserves that decision. The source keeps the optional branch, so the final file alone does not explain this trajectory.
- **Interpretation:** the agent revisits a previously rejected idea after changing the surrounding controller, then retains the shallower option.
- **Alternative/limit:** the reported time/quality tradeoff is evidence of the stated rationale, not proof of an optimal choice or a controlled comparison. Model error, candidate pruning and test variation may matter.
- **Next check:** compare `M=0` and positive values on identical saved states and budgets; separate model prediction error from search cost.
- **Status:** adoption, disabling and reconsideration supported; causal explanation open.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
