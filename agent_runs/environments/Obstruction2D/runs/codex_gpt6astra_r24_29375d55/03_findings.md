# Obstruction2D · GPT-6 Astra (high) · replicate 24

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). The complete final controller and imported local runtime helpers were read; cited trace events and changes were checked. This is not exhaustive manual annotation.

## Controller: stages plus grasp-dependency reasoning

[approach.py](evidence/final/approach.py) has explicit manipulation phases (`get_action`, 179–226). `select` (83–177) scores destination/grasp choices and traverses **grasp blockers**: it tracks visited objects, gathers dependencies across possible grasps, and uses an access-cost heuristic to choose which obstruction to handle next (108–133).

Parking candidates are also checked against future pickup and placement configurations. This is more than a fixed removal list, but it is not a search over full alternative removal-and-parking trajectories. The code combines dependency-guided selection, geometric anticipation and feedback. No forward dynamics rollout was found in the final controller.

**Pairing note (coverage updated 2026-10-11):** [Claude replicate 24](../claude_opus55_high_r24_f8729873/03_findings.md) is now included, with matching task text and checked environment/evaluation settings. GPT-5.6 still has only replicate 424 here, so this is not a same-replicate three-model comparison. The findings below are unchanged from the initial review.

## F001 — Replace a height rule with a grasp-dependency rule

[C012](02_code_changes.md#C012) changes blocker selection → [E0082](01_timeline.md#E0082) explains that a shorter neighbor had to be removed before the chosen obstruction could be grasped alone.

- **Observed:** the diff replaces a restriction to taller blockers with a visited set, dependency collection and an access-cost choice. The message reports the motivating case and subsequent success.
- **Interpretation:** the representation of “what must move first” becomes sensitive to grasp geometry rather than height alone. This is a useful small unit for studying how a failure changes the controller’s task decomposition.
- **Alternative/limit:** the traversal still makes heuristic choices; it does not evaluate the eventual cost of all possible removal orders. The message and diff do not establish private internal reasoning or isolate the performance effect.
- **Next check:** find scenes where height order and grasp-dependency order disagree, then compare C011/C012 with the same harness and object counts.
- **Status:** algorithmic change supported; generality and causal benefit open.

## Evidence limits and your notes

Main files inspected: the linked final controller and local runtime helpers, cited saved Git diffs/versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Development scripts/prototypes are linked where used. Archived code and instructions were read as data; no robot evaluations were run.

This imported main stream supplies visible messages and tool records, not complete private reasoning. Separate backend-session trees have not been exhaustively audited here. Labels are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent success/timing claims are not independently established unless a specific saved result is cited. No population prevalence or cross-model success rates are inferred.

Your own observations / disagreements / next experiment:

- 
