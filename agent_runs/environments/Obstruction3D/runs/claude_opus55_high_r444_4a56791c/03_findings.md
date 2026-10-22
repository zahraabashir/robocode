# Obstruction3D · Claude Opus 5.5 High · replicate 444

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: kinematic plan comparison; “lookahead” also names waypoint advancement

[kin.py](evidence/final/kin.py) provides kinematics. In [approach.py](evidence/final/approach.py), `_plan_pick` and `_plan_place` (359–512) try alternative orientations, construct reachable motion plans and compare costs. Task selection follows grasp dependencies with a bounded frontier (`_pick_target`, 278–329). The executor runs queued movement, base, gripper and check operations.

`_lookahead` (565–593) advances to a farther queued joint waypoint when the joint movement budget permits. That function is not a branching search over future object-removal actions. Nevertheless, the earlier alternative-plan construction and kinematic checks are predictive. Naming alone would obscure these two distinct computations.

## F001 — A difficult case leads to using another part of the action space

[E1127](01_timeline.md#E1127): report expensive computation in a many-obstruction case → [C023](02_code_changes.md#C023): accelerate kinematics/early exit → [E1155](01_timeline.md#E1155): report a 980-step case → [E1165](01_timeline.md#E1165): diagnose arm reach near its mount → [C024](02_code_changes.md#C024): add base repositioning in the alternative controller → [C025](02_code_changes.md#C025): promote the controller; base actions remain in the final file.

- **Observed:** C024 adds a `base_for` calculation and base movement to pickup/placement plans. This changes how the controller can make an arm target reachable, beyond changing an inverse-kinematics tolerance.
- **Interpretation:** a reachability diagnosis leads to expanding the effective action repertoire.
- **Alternative/limit:** this sequence does not isolate whether the speed optimization caused the bad case. The diagnosis and subsequent reported recovery are agent claims; several implementation changes intervene.
- **Next check:** hold the arm solver fixed, compare the same near-mount states with/without base repositioning, and measure reachability, steps and computation.
- **Status:** expansion of control actions supported; causal chain remains a hypothesis.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
