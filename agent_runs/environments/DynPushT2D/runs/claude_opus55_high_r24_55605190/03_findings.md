# DynPushT2D · Claude Opus 5.5 High · replicate 24

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). These are analyst notes to inspect, not an exhaustive hand-labeling of the run. Reviewed the complete final controller and its imported local runtime helpers; checked the cited code changes and trace events. No controller was executed.

## Controller: simulated pushing and bounded two-push look-ahead

In [approach.py](evidence/final/approach.py), `plan_push` (217–385) propagates predicted center-of-mass position and angle for candidate contacts and push directions using a quasi-static contact approximation. Its loop (313–342) checks predicted wall/friction constraints and scores predicted outcomes.

For up to `LOOK=8` first-push candidates, it creates a predicted state `s2` and calls `plan_push(s2, 0)` (369–382). The score of the predicted second push can change the selected first push. This is explicit look-ahead before acting.

`build_actions` (388–410) produces labeled `nav` and `push` segments. `_get_action` executes them, observes the actual state and can replan after ten push actions. Navigation uses Dijkstra-style search over a visibility graph (`nav_path`, 135–178), with accumulated path cost and no A* heuristic. Thus staged execution, search, an approximate model and feedback coexist.

## F001 — A directly inspectable planning-depth comparison

[E0476](01_timeline.md#E0476) times the existing single-push planner → [E0502](01_timeline.md#E0502) adds a predicted second push and runs three settings → [C013](02_code_changes.md#C013) sets `LOOK=8`.

The saved E0502 output reports, on its sweep:

| Look-ahead width | Reported mean steps | Reported solved |
| --- | --- | --- |
| 0 | 159.07 | 96/96 |
| 4 | 145.92 | 96/96 |
| 8 | 142.96 | 96/96 |

These are **development-test outputs**, not independent evaluation results or newly reproduced measurements. Inspect the exact command and sweep harness before treating the comparison as controlled.

- **Interpretation:** this is a small candidate experiment for whether predicting a second push improves the first choice.
- **Alternative/limit:** pruning, runtime and other settings can affect the comparison; no uncertainty estimate is supplied here.
- **Next check:** hold the controller/harness fixed, compare per-seed results and record first-action disagreements and planner time.
- **Status:** code mechanism and saved comparison supported; causal performance claim remains to test.

## F002 — A controller changes its own planning effort

Final `_get_action` disables two-push look-ahead after 25 seconds of accumulated planning time and stops periodic mid-push replanning after 40 seconds. It can also tighten its success margins when its model predicts success but the environment continues. These are explicit adaptation rules in the generated program. They do not establish what private reasoning the coding agent used, or whether those branches ran during evaluation.

## Evidence limits and your notes

The main files used here are `evidence/final/approach.py` (and linked runtime helpers), the cited saved Git diffs/versions, `evidence/stream.jsonl`, and `evidence/config.yaml`. Messages, tools and code support these observations; they do not expose complete private reasoning. All thinking blocks in this run’s imported stream have empty readable text; see [stream coverage](evidence/stream_coverage.json). Separate backend session trees have not been exhaustively audited here.

Labels here are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent statements about success, timing or model accuracy remain claims unless a specific saved output is cited. No cross-model success rates or prevalence estimates are aggregated.

Your own observations / disagreements / next experiment:

- 
