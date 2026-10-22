# Obstruction2D · GPT-6 Astra (high) · replicate 424

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). The complete final controller and imported local runtime helpers were read; cited trace events and changes were checked. This is not exhaustive manual annotation.

## Controller: programmed phases with future-clearance constraints

[approach.py](evidence/final/approach.py) uses explicit phases: select → above → down → lift → carry → place → retreat (`get_action`, 122–178). Selection scores possible target placements and chooses a blocking object; it does not search complete removal sequences. `grasp_position` (36–60) and `placement_collisions` (62–78) check geometric configurations, including the gripper, arm and base.

`storage` (80–120) reserves space for **both a later target pickup and final placement**. This is explicit anticipation in a geometric model, even without a multi-action rollout. The most precise description is a staged heuristic controller with predictive clearance checks. Calling it model-free would hide those checks; calling it a full task planner would overstate them.

## F001 — An empty parking location can still obstruct the future

[E0120](01_timeline.md#E0120) reports that a moved obstruction blocked the target’s later pickup near a wall → [C032](02_code_changes.md#C032) preserves a storage rule that reserves the target pickup footprint as well as its destination.

- **Observed:** the message reports both the failure and a correction. The diff adds `pickup_left`/`pickup_right` and filters floor and stacked parking candidates. The final `storage` function retains the constraint.
- **Interpretation:** a failure leads to a rule about a future action, rather than just the current placement. This is similar to the earlier GPT-5.6 Obstruction2D example, but belongs to a separate development run.
- **Alternative/limit:** this is a hand-coded geometric exclusion, not evidence that the coding agent internally simulated a complete plan. The message is retrospective; its position is not the exact edit time. Its success claims are not a fresh verification.
- **Next check:** replay the versions before/after C032 on matched scenes, record where objects are parked, and isolate whether pickup clearance explains the difference.
- **Status:** implementation and reported diagnosis supported; causal performance effect untested here.

## Evidence limits and your notes

Main files inspected: the linked final controller and local runtime helpers, cited saved Git diffs/versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Development scripts/prototypes are linked where used. Archived code and instructions were read as data; no robot evaluations were run.

This imported main stream supplies visible messages and tool records, not complete private reasoning. Separate backend-session trees have not been exhaustively audited here. Labels are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent success/timing claims are not independently established unless a specific saved result is cited. No population prevalence or cross-model success rates are inferred.

Your own observations / disagreements / next experiment:

- 
