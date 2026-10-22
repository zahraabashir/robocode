# Rovers · Claude Opus 5.5 High · replicate 24

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). These are analyst notes to inspect, not an exhaustive hand-labeling of the run. Reviewed the complete final controller and its imported local runtime helpers; checked the cited code changes and trace events. No controller was executed.

## Controller: search constructs the action sequence

[approach.py](evidence/final/approach.py) uses time-expanded breadth-first search over **grid position + completed-task bits + calibration + storage + sending status**. `RoverBFS.transitions` (183–204) defines predicted operation effects; `run` (213–262) expands reachable states over time, and `extract` (264–309) reconstructs a sequence. `reset` (318–382) compares how to divide requirements between the two rovers and refines plans using the other rover's predicted route.

`_rover_action` (561–622) executes the saved sequence, checks observed outcomes, retries or replans, and makes runtime heading/sending adjustments. Search and feedback coexist. This is model-based symbolic/geometric planning; it is not a contact-dynamics simulator.

**Phase-label caution:** the code has explicit task/operator state and a persistent plan pointer, but not the same fixed “finish sampling, then start imaging” phase template. The search can interleave operations. Keep this distinct from a manually programmed phase machine when testing whether phase decomposition generalizes.

## F001 — Develop a replacement alongside a working controller

[E0858](01_timeline.md#E0858): “I'll write the new planner as `approach2.py` and keep `approach.py` as the working fallback until the new one beats it.” → [C008](02_code_changes.md#C008) adds the alternative planner → [E0873](01_timeline.md#E0873) reports a comparison → [E0952](01_timeline.md#E0952) copies the old controller to `approach_v1.py`, adopts `approach2.py` and runs another batch → [C013](02_code_changes.md#C013) preserves the adoption in Git.

- **Observed:** the core planner is replaced, while the previous controller remains available. The final [approach_v1.py](evidence/final/approach_v1.py) is byte-identical to the last saved controller before adoption (C007; C008–C012 changed the alternative/support files).
- **Interpretation:** this is a parallel alternative followed by promotion, rather than immediately throwing away the working policy.
- **Alternative/limit:** the new planner reuses task knowledge and some supporting logic; this is not a claim that it starts from zero. Reported performance differences still need controlled replication.
- **Next check:** compare both saved versions on identical cases; inspect what evidence the agent used as its criterion for switching.
- **Status:** replacement/preservation sequence supported by exact message, command, diff and file bytes.

## F002 — Predicted interference between rovers

`send_mask_t` (144–153) uses the other rover's predicted position at a future time to constrain sending. Plan refinement installs `other_traj` and reruns search. This is prospective coordination inside the controller. Heading/execution corrections remain outside parts of the search state, so the planner does not model every execution detail.

## Evidence limits and your notes

The main files used here are `evidence/final/approach.py` (and linked runtime helpers), the cited saved Git diffs/versions, `evidence/stream.jsonl`, and `evidence/config.yaml`. Messages, tools and code support these observations; they do not expose complete private reasoning. All thinking blocks in this run’s imported stream have empty readable text; see [stream coverage](evidence/stream_coverage.json). Separate backend session trees have not been exhaustively audited here.

Labels here are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent statements about success, timing or model accuracy remain claims unless a specific saved output is cited. No cross-model success rates or prevalence estimates are aggregated.

Your own observations / disagreements / next experiment:

- 
