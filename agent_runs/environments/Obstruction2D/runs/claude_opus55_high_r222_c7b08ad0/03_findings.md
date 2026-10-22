# Obstruction2D · Claude Opus 5.5 High · replicate 222

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: a motion rollout inside heuristic task selection

[approach.py](evidence/final/approach.py) uses `plan/to_grasp/grasp/lift/carry/release` phases (446–549). Task selection (351–414) chooses nearby blockers and recursively follows grasp dependencies, with a depth bound. It does not perform a full permutation search in this inspected section.

However, `_est` (217–251) explicitly advances a predicted robot position through a clearance profile, for up to 200 iterations, to estimate travel steps. `_drop_spot` (272–340) uses these estimates for approach, carry and later pickup/delivery, including a hypothetical profile after parking an object. This is model-based prediction in the scoring calculation, even though task ordering remains heuristic.

## F001 — Replace a cost formula with a rollout of movement

[C006](02_code_changes.md#C006): use estimated step costs for placement → [C007](02_code_changes.md#C007), linked to [E0192](01_timeline.md#E0192): replace the simpler `_est` formula with a loop that advances predicted position.

- **Observed:** the policy diff provides the strongest evidence here: it replaces a height/distance formula with an iterative movement estimate. It also changes candidate spacing and a height limit. There is no need to invent an accompanying verbal explanation.
- **Interpretation:** development makes placement ranking more closely reflect how the motion controller would travel.
- **Alternative/limit:** an approximate rollout can still rank candidates poorly. Any observed improvement could also come from the candidate-grid changes in the same commit.
- **Next check:** keep the candidate grid fixed, compare both estimators on the same states, and check estimated versus realized travel and chosen placements.
- **Status:** algorithmic change supported by implementation; motivation and performance effect remain uncertain.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
