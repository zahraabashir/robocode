# Obstruction3D · Claude Opus 5.5 High · replicate 24

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). These are analyst notes to inspect, not an exhaustive hand-labeling of the run. Reviewed the complete final controller and its imported local runtime helpers; checked the cited code changes and trace events. No controller was executed.

## Controller: explicit stages, model-based geometry, local path checks

[approach.py](evidence/final/approach.py) maintains phases including `to_grasp`, `close`, `to_place`, `open` and `done` (`_policy`, 433–520). Task selection is a rule that prioritizes graspable objects and can insert a blocking object into the pending tasks (`_select_task`, 206–235).

[kin.py](evidence/final/kin.py) supplies a forward/inverse kinematic model, including the mobile base. `_set_path` (302–346) builds joint waypoints. `_safe_move` (385–407) predicts tool positions at four points along a proposed joint-space shortcut and checks clearance. `_track` uses that check before cutting a corner.

**The word “look-ahead” needs care here:** `self.look` also controls how far along an existing path the controller advances in one action. It does not denote search depth over alternative task sequences. The final controller uses local geometric prediction; I did not find a rollout search over complete alternative removal plans in this file and its imported `kin.py`.

## F001 — An apparent controller failure turns out partly to be a tester failure

[Rewrite C008](02_code_changes.md#C008) → [E0365](01_timeline.md#E0365): agent reports the rewrite failing → [E0371](01_timeline.md#E0371): diagnoses path-pointer handling → [E0405](01_timeline.md#E0405): runs an older controller to compare grasp poses → [E0407](01_timeline.md#E0407): identifies clipping in the debug script that prevents gripper closing → [E0411](01_timeline.md#E0411): rewrites the tester to call `get_action`; its saved output ends with `DONE 41`.

[C009](02_code_changes.md#C009) also fixes path truncation and gripper handling. **Do not attribute the whole improvement to the tester alone.**

- **Observed:** the agent revisits whether its measurement procedure is causing the failure, using an older controller as a diagnostic comparison.
- **Interpretation:** failure attribution can move between policy, environment model and test harness.
- **Alternative/limit:** real controller defects and a tester defect coexist here; successive interventions are confounded.
- **Next check:** reconstruct the old/new controller × old/new tester comparison to separate their effects.
- **Status:** diagnostic sequence supported by messages, commands, diff and saved output; no fresh replay.

## F002 — Rewrite followed by repairs to execution bookkeeping

[C008](02_code_changes.md#C008) substantially replaces path construction/tracking and geometric scoring. [C009](02_code_changes.md#C009) truncates consumed path entries; [C010](02_code_changes.md#C010) prevents skipping Cartesian corners. This is a useful short sequence for studying how a new representation introduces new bookkeeping failures. It is a substantial revision, not evidence that every previous component was discarded.

## Evidence limits and your notes

The main files used here are `evidence/final/approach.py` (and linked runtime helpers), the cited saved Git diffs/versions, `evidence/stream.jsonl`, and `evidence/config.yaml`. Messages, tools and code support these observations; they do not expose complete private reasoning. All thinking blocks in this run’s imported stream have empty readable text; see [stream coverage](evidence/stream_coverage.json). Separate backend session trees have not been exhaustively audited here.

Labels here are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent statements about success, timing or model accuracy remain claims unless a specific saved output is cited. No cross-model success rates or prevalence estimates are aggregated.

Your own observations / disagreements / next experiment:

- 
