# Obstruction3D · GPT-6 Astra (high) · replicate 424

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). The complete final controller and imported local runtime helpers were read; cited trace events and changes were checked. This is not exhaustive manual annotation.

## Controller: calibrated kinematics inside a phase machine

[approach.py](evidence/final/approach.py) imports [kinematics_fit.py](evidence/final/kinematics_fit.py). The helper maps joint values to tool pose; `ik` (approach lines 6–14) numerically solves for joint values using this model. `reset` builds an obstruction order, while `get_action` (69–209) executes manipulation stages with retry/recovery rules.

When a lift is blocked, the controller scores a small set of lateral displacements for clearance (87–109). These are local geometric alternatives, not a rollout of a complete removal sequence. An explicit runtime kinematic model is present; multi-step task/trajectory search was not found.

## F001 — Use measured transforms to improve a model, then use it for control

[E0048](01_timeline.md#E0048) proposes using a successful grasp’s reported transform for calibration → [C023](02_code_changes.md#C023) saves a fitting script → [C025](02_code_changes.md#C025) saves the calibrated helper → [C029](02_code_changes.md#C029) connects it to the staged controller.

- **Observed:** [fit_fk.py](evidence/final/fit_fk.py) reads joint/base/object/grasp-transform samples and fits positional corrections using linear least squares. The runtime helper contains correction constants, and the final inverse-kinematics function calls it. [E0065](01_timeline.md#E0065) reports a pickup using the calibrated controller.
- **Interpretation:** the development process includes model calibration, not only changing action rules after failure. The resulting model is used at test time to choose joint commands.
- **Alternative/limit:** the fitting script and runtime integration are directly visible; this review did not independently recompute the fit or establish its accuracy. Some intermediate commits have no confidently matched main-stream event, so their exact conversational origin remains unspecified.
- **Next check:** recover the committed sample data and fitted version, measure pose prediction error on held-out configurations, and compare the controller with/without the corrections.
- **Status:** model-fitting and runtime-use sequence supported; accuracy and benefit unverified here.

## Evidence limits and your notes

Main files inspected: the linked final controller and local runtime helpers, cited saved Git diffs/versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Development scripts/prototypes are linked where used. Archived code and instructions were read as data; no robot evaluations were run.

This imported main stream supplies visible messages and tool records, not complete private reasoning. Separate backend-session trees have not been exhaustively audited here. Labels are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent success/timing claims are not independently established unless a specific saved result is cited. No population prevalence or cross-model success rates are inferred.

Your own observations / disagreements / next experiment:

- 
