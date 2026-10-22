# Rovers · GPT-6 Astra (high) · replicate 24

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). The complete final controller and imported local runtime helpers were read; cited trace events and changes were checked. This is not exhaustive manual annotation.

## Controller: route search with a greedy task scheduler

[approach.py](evidence/final/approach.py) builds a geometric grid and uses **Dijkstra search** to route each rover. It chooses a task using current route cost with sample/send preferences (103–121), and can perform useful operations while moving (156–162). Failed movement, imaging and sending update spatial masks (82–95).

The final controller has no retained multi-task tour planner and no equivalent persistent global task-phase machine. Tasks are selected again from the current observation. This is a useful counterexample to an overly broad “every agent writes fixed phases” hypothesis. It still has a spatial model and navigation search; “model-free controller” would be inaccurate.

## F001 — Try more elaborate planners, then keep the simpler scheduler

[C036](02_code_changes.md#C036) adds [tour_candidate.py](evidence/final/tour_candidate.py), which uses subset dynamic programming to allocate tasks → [C038](02_code_changes.md#C038) adds [ordered_candidate.py](evidence/final/ordered_candidate.py), which also reconstructs and follows task stages → [E0141](01_timeline.md#E0141) prints a comparison → [E0145](01_timeline.md#E0145) says the simpler scheduler is retained. Final `approach.py` does not import either candidate; [C039](02_code_changes.md#C039) adds explanations rather than adopting their planning code.

- **Observed:** development includes task-planning alternatives that the final controller alone would not reveal.
- **Interpretation:** building an explicit planner does not guarantee retaining it. This is a useful decision point for studying selection criteria.
- **Alternative/limit:** the evidence does not establish that every planner was worse. [E0132](01_timeline.md#E0132) prints tour mean steps **26.47** versus baseline **26.60**, while E0141 prints ordered **26.83** versus baseline **26.60**. These are saved small-batch outputs, not new evaluations or statistically established differences. The full criterion behind “best overall” is not specified in the visible message. Harness/version equivalence needs further audit.
- **Next check:** recover the exact compared versions and conditions; compare success, steps, runtime and failure modes on identical cases. Check whether stability or computation cost can explain retention without assuming those were the agent’s unstated reasons.
- **Status:** prototype/comparison/non-adoption sequence supported; rationale and superiority unresolved.

## F002 — A discarded planning branch can still contribute a repair

[E0130](01_timeline.md#E0130) edits both `approach.py` and `tour_candidate.py` after a calibration/imaging retry problem; [C037](02_code_changes.md#C037) preserves both edits. Failed calibration now affects all relevant image-viewpoint candidates, and image acquisition is checked using an observed image-count change. [E0134](01_timeline.md#E0134) describes the retry-loop diagnosis. The planning alternative is not adopted, but diagnostic work during its evaluation changes the retained controller.

## Evidence limits and your notes

Main files inspected: the linked final controller and local runtime helpers, cited saved Git diffs/versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Development scripts/prototypes are linked where used. Archived code and instructions were read as data; no robot evaluations were run.

This imported main stream supplies visible messages and tool records, not complete private reasoning. Separate backend-session trees have not been exhaustively audited here. Labels are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent success/timing claims are not independently established unless a specific saved result is cited. No population prevalence or cross-model success rates are inferred.

Your own observations / disagreements / next experiment:

- 
