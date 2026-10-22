# DynPushT2D · GPT-6 Astra (high) · replicate 424

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). The complete final controller and imported local runtime helpers were read; cited trace events and changes were checked. This is not exhaustive manual annotation.

## Controller: local contact prediction, route search and move/push phases

[approach.py](evidence/final/approach.py) uses a visibility graph and **Dijkstra search** for the robot’s path around the block (`path`, 31–54). `rate` (63–109) constructs a local contact-response matrix relating pushing force to translation/rotation, selects a force under friction and near-wall constraints, and scores predicted progress. `choose` (110–124) ranks contacts and checks navigation access.

Execution retains move/push state, observes the block again, and periodically reconsiders contacts (`get_action`, 128–162). This is a model-based local pushing calculation combined with search for robot navigation. **No sequence of simulated future block poses or multi-push rollout was found.** It differs from both a purely geometric pushing rule and Claude’s two-push look-ahead.

## F001 — Improve the constraints on a local prediction

[C013](02_code_changes.md#C013) introduces friction-constrained force selection → [C023](02_code_changes.md#C023) adds near-wall corner constraints and contact-centering changes → [E0104](01_timeline.md#E0104) explains a rare seed-608 wall trap and reports its repair.

- **Observed:** the C023 diff restricts force choices using predicted corner motion near walls. Final `rate` retains the calculation. The message ties the change to an observed trap.
- **Interpretation:** the response improves the feasibility assumptions of an existing local model rather than increasing its planning horizon.
- **Alternative/limit:** C023 changes contact centering and scoring as well, so a later improvement does not isolate the wall constraint. Local response estimates need not be accurate dynamics models to influence action choice.
- **Next check:** replay identical states with wall constraints enabled/disabled, compare predicted and observed motion, and keep contact centering fixed.
- **Status:** explicit local prediction supported; accuracy and isolated repair effect open.

## Evidence limits and your notes

Main files inspected: the linked final controller and local runtime helpers, cited saved Git diffs/versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Development scripts/prototypes are linked where used. Archived code and instructions were read as data; no robot evaluations were run.

This imported main stream supplies visible messages and tool records, not complete private reasoning. Separate backend-session trees have not been exhaustively audited here. Labels are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent success/timing claims are not independently established unless a specific saved result is cited. No population prevalence or cross-model success rates are inferred.

Your own observations / disagreements / next experiment:

- 
