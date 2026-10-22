# DynPushT2D · Claude Opus 5.5 High · replicate 424

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). These are analyst notes to inspect, not an exhaustive hand-labeling of the run. Reviewed the complete final controller and its imported local runtime helpers; checked the cited code changes and trace events. No controller was executed.

## Controller: model-based pushing with two-push look-ahead

**Unlike the earlier GPT DynPushT2D examples, this controller predicts future block motion when choosing pushes.** In [approach.py](evidence/final/approach.py), `Model.step` / `_step1` (69–121) update a predicted block position and angle. `_rollout` (209–300) repeatedly applies that model to alternative contact points, directions, step sizes and curvatures, for up to `KMAX=30` modeled steps.

`_plan_push` (302–333) takes promising first pushes, starts another rollout from each predicted resulting block/pusher state, and uses the second push's predicted cost to choose the first. This is bounded two-push look-ahead, not merely executing a push and reacting afterward.

The selected plan becomes **navigate to contact → push → observe/replan** in `_get_action` (483–535). Feedback and fallback rules coexist with the model.

Navigation uses grid **Dijkstra** in [navgrid.py](evidence/final/navgrid.py), reached through `_navigate` → `_gridpath`. An `_astar` function remains in `approach.py`, but it is not called by this final navigation path. The introductory comment still says A*: this is a concrete reason to check call paths rather than label from comments.

## F001 — One-push rollouts become two-push look-ahead

[E0248](01_timeline.md#E0248) announces a two-stage planner → [C005](02_code_changes.md#C005) adds the second rollout and uses its score to select the first action sequence → [E0257](01_timeline.md#E0257) reports better average steps and proposes tuning the look-ahead width.

- **Observed:** the diff supports an increase in planning depth, not the first appearance of a model; the earlier version already predicted one push.
- **Interpretation:** an agent can refine the horizon of an existing model-based controller while keeping its execution stages.
- **Alternative/limit:** the model is approximate; these notes do not independently establish prediction accuracy or performance gain.
- **Next check:** compare look-ahead enabled/disabled at fixed candidate sets and compute budget, including episodes where they choose different first pushes.
- **Status:** mechanism supported by final code, commit and trace.

## F002 — Retain a cheaper search setting

[E0427](01_timeline.md#E0427) says wider search saves about three steps but roughly doubles worst-case time, and retains safer defaults. In final `_get_action`, accumulated controller time above 20 seconds reduces search width; above 30 seconds disables second-stage search; above 50 seconds prevents new planning. This is an explicit compute/solution-quality tradeoff in text and code, not proof of optimal resource rationality. Branch usage has not been measured.

## Evidence limits and your notes

The main files used here are `evidence/final/approach.py` (and linked runtime helpers), the cited saved Git diffs/versions, `evidence/stream.jsonl`, and `evidence/config.yaml`. Messages, tools and code support these observations; they do not expose complete private reasoning. All thinking blocks in this run’s imported stream have empty readable text; see [stream coverage](evidence/stream_coverage.json). Separate backend session trees have not been exhaustively audited here.

Labels here are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent statements about success, timing or model accuracy remain claims unless a specific saved output is cited. No cross-model success rates or prevalence estimates are aggregated.

Your own observations / disagreements / next experiment:

- 
