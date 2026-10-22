# Obstruction3D · Claude Opus 5.5 High · replicate 424

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). These are analyst notes to inspect, not an exhaustive hand-labeling of the run. Reviewed the complete final controller and its imported local runtime helpers; checked the cited code changes and trace events. No controller was executed.

## Controller: staged manipulation with a kinematic model

[approach.py](evidence/final/approach.py) creates a queue of approach, descend, close, lift, transfer, open and retreat operations (`_plan_pick_place`, 153–173; `_step`, 260–401). Object selection and parking use geometric scores and failure history (`_plan`, 190–231; `_free_spot`, 67–84).

The controller uses an explicit robot model: [kin.py](evidence/final/kin.py) maps joints to tool pose with `fk` and solves target poses with `ik`. The executor precomputes joint waypoints from Cartesian targets. This supports **model-based kinematic computation**, but does not establish task-level search over alternative complete removal sequences. I did not find such sequence search or contact-dynamics rollouts in the final controller and its imported `kin.py`.

## F001 — Choose a grasp with the later placement in mind

[C017](02_code_changes.md#C017) adds a placement pose to the grasp-scoring calculation. In final `_grasp_yaw` (116–143), a candidate's score uses finger clearance both at pickup and at the proposed placement. `_plan_pick_place` passes the target placement pose into it.

Simple sequence: **consider a grasp angle → predict clearance at the future placement → choose an angle using both checks → execute the staged motion**.

- **Observed:** the future-pose constraint affects the selected grasp before execution.
- **Interpretation:** anticipatory geometric reasoning inside the written controller.
- **Alternative/limit:** this is a limited endpoint check, not simulation of alternative complete task sequences. The agent's private reasoning is not visible.
- **Next check:** find a scene where pickup-only scoring and pickup-plus-placement scoring select different grasps, then compare outcomes under the same policy otherwise.
- **Status:** implementation supported; behavioral effect not independently replayed.

## F002 — Repairing a model is different from changing a stage

[E0078](01_timeline.md#E0078) reports that collision observations disagree with the assumed gripper position and proposes visual inspection. [C003](02_code_changes.md#C003) changes calibrated kinematics and grasp/place transformations, alongside execution changes. Read this as a model-revision candidate, not an isolated experiment: several pieces changed together. The later final kinematic model is used at runtime, not solely in development tests.

## Evidence limits and your notes

The main files used here are `evidence/final/approach.py` (and linked runtime helpers), the cited saved Git diffs/versions, `evidence/stream.jsonl`, and `evidence/config.yaml`. Messages, tools and code support these observations; they do not expose complete private reasoning. All thinking blocks in this run’s imported stream have empty readable text; see [stream coverage](evidence/stream_coverage.json). Separate backend session trees have not been exhaustively audited here.

Labels here are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent statements about success, timing or model accuracy remain claims unless a specific saved output is cited. No cross-model success rates or prevalence estimates are aggregated.

Your own observations / disagreements / next experiment:

- 
