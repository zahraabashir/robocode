# DynPushT2D · Claude Opus 5.5 High · replicate 222

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **targeted controller review and selected development sequence** (2026-10-11). The full run is organized for your inspection; this initial note does not label every decision.

## Controller: approximate maneuver planning with a phase machine

[approach.py](evidence/final/approach.py) uses `plan → approach → push` phases (507–614) and Dijkstra navigation (442–487). The author defines rotation and translation maneuvers in Python; these are not supplied environment primitives. `choose` (231–329) predicts rotation endpoints, checks intermediate wall positions, and can score the following translation. `pick_trans_la` (379–421) predicts a translated block pose and estimates a second translation plus travel cost.

This is explicit look-ahead with an approximate maneuver model. It differs from stepping a detailed contact simulator through every action. Both look-ahead flags start enabled, but repeated lack of progress can toggle them (`_get_action`, 516–517). Therefore, an implementation can contain planning and sometimes choose actions without its deeper planner.

## F001 — Add planning, then make its use reversible during execution

[E0652](01_timeline.md#E0652): consider spending more computation on planning → [C021](02_code_changes.md#C021): add two-step translation look-ahead → [E0669](01_timeline.md#E0669): report worse mean steps → later [E0743](01_timeline.md#E0743): report five failures in a larger sweep → [C025](02_code_changes.md#C025): add the stall-triggered switch.

- **Observed:** the saved C025 diff adds code that switches `lookahead` and `rot_la` after repeated stalls. This is a runtime strategy change in the generated controller, not a new coding-agent intervention at each stall.
- **Interpretation:** a richer planner is treated as fallible; feedback can change which planner is used.
- **Alternative/limit:** intervening changes and different test batches prevent attributing the later reported success to this switch alone. A toggle might escape a loop through changed actions without selecting a more accurate model.
- **Next check:** replay the same stalled states with flags fixed on, fixed off, and adaptive; measure action differences and recovery, holding all other fixes constant.
- **Status:** predictive code and switching rule supported; explanation of recovery uncertain.

## Evidence limits and your notes

Main sources: the linked final controller/helper files, cited saved Git diffs and policy versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Review scope is targeted planner/execution functions, active flags and selected development sequences; it is **not a complete audit of every helper or every trace event**. No archived code was executed.

All thinking blocks in this imported main stream have empty readable text; see [coverage](evidence/stream_coverage.json). Separate backend-session trees have not been exhaustively audited. These observations concern visible messages and implemented computations, not private reasoning. Labels are descriptive, **not formal ACT*ONOMY annotations**. Reported test success or speed is not an independent evaluation unless a specific output and matched test conditions are checked.

Your observations / disagreements / next experiment:

- 
