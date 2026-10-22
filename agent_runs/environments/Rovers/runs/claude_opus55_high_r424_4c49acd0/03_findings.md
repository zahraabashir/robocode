# Rovers · Claude Opus 5.5 High · replicate 424

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). These are analyst notes to inspect, not an exhaustive hand-labeling of the run. Reviewed the complete final controller and its imported local runtime helpers; checked the cited code changes and trace events. No controller was executed.

## Controller: task-order search, a transition model, and staged execution

[approach.py](evidence/final/approach.py) uses a Held–Karp-style subset dynamic program (`_held_karp`, 365–441) to compare task orders. `_plan` (443–480) combines assignments across the two rovers, then scores top candidate pairs using simulated execution. `_model_step` (519–577) predicts movement and discrete effects such as calibration, imaging, sampling, sending and dropping; `_simulate` (579–587) repeatedly applies the policy to those predicted states.

Execution uses cost-to-go fields indexed by task stage, calibration, store status and sending status (`_layer_fields`, 804–851; `_rover_action`, 853–923). The task order is computed, rather than one universal hardcoded sequence. Geometric navigation uses grid distance propagation. This is explicit model-based task planning, beyond route search alone.

The controller also predicts the other rover's trajectory to choose a sending location/time (`_predict_other`, 687–710; `_final_send_target`, 712–747). It does not merely wait for an observed blockage and react.

## F001 — The agent builds a model to evaluate candidate plans

[E0609](01_timeline.md#E0609) announces an internal simulator while probes are still running → [C003](02_code_changes.md#C003) adds `_model_step`, `_simulate` and simulation-based plan selection → [E0616](01_timeline.md#E0616) reports comparing simulated and real step counts.

- **Observed:** simulated trajectories actually rank candidate plans in the controller.
- **Interpretation:** an executable world model is developed and used both in diagnostic comparisons and at controller runtime.
- **Alternative/limit:** matching aggregate step counts is weaker than validating state-by-state transitions; the model is an approximation.
- **Next check:** compare predicted/observed state transitions, especially where two candidate plans have similar cost.
- **Status:** runtime use supported; reported model accuracy not independently reproduced.

## F002 — Repair the predicted world and the controller together

[E1008](01_timeline.md#E1008) reports real/simulated discrepancies for two seeds → [E1065](01_timeline.md#E1065) waits for an image-selection probe → [E1294](01_timeline.md#E1294) proposes distinguishing objectives in range from objectives considered visible → [C011](02_code_changes.md#C011) changes the task-region computation, simulated image effect and executor → [E1320](01_timeline.md#E1320) reports improved agreement.

This is a model-mismatch investigation, not simply a policy constant adjustment. Because model and executor change together, the later reported improvement does not isolate which component caused it. A useful follow-up is a crossed old/new model × old/new executor comparison.

## Evidence limits and your notes

The main files used here are `evidence/final/approach.py` (and linked runtime helpers), the cited saved Git diffs/versions, `evidence/stream.jsonl`, and `evidence/config.yaml`. Messages, tools and code support these observations; they do not expose complete private reasoning. All thinking blocks in this run’s imported stream have empty readable text; see [stream coverage](evidence/stream_coverage.json). Separate backend session trees have not been exhaustively audited here.

Labels here are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent statements about success, timing or model accuracy remain claims unless a specific saved output is cited. No cross-model success rates or prevalence estimates are aggregated.

Your own observations / disagreements / next experiment:

- 
