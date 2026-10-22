# DynPushT2D · GPT-6 Astra (high) · replicate 24

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). The complete final controller and imported local runtime helpers were read; cited trace events and changes were checked. This is not exhaustive manual annotation.

## Controller: analytic contact choice with geometry-triggered execution modes

[approach.py](evidence/final/approach.py) uses **Dijkstra search** over a visibility graph for navigation (`navigate`, 54–86). The contact-selection calculation (123–154) predicts local translation/rotation response from contact geometry, inertia and normal/tangential force components, then optimizes the pushing direction for predicted progress.

This is an explicit local model, but not a sequence of simulated pushes. Navigation search and a local pushing prediction should be labeled separately.

**Phase-label caution:** this run retains contact/history memory, but it does not use the same persistent move/push phase machine as replicate 424. `self.pushing` is reset each call; current geometry determines whether to navigate or push, and the flag records the chosen mode. “Navigation/pushing modes” is more accurate than assuming an identical phase architecture across both runs.

## F001 — Change the predicted action, then discover parameter interactions

[C019](02_code_changes.md#C019) adds analytic tangential pushing-direction selection → [E0085](01_timeline.md#E0085) reports benefits of angled pushes → [E0094](01_timeline.md#E0094) says a lower orientation weight helped an earlier controller but slowed this angled-push version, so the old weight is retained.

- **Observed:** the contact-response calculation is present in the saved diff and final controller. The message explicitly describes a parameter preference changing with the algorithm version.
- **Interpretation:** development choices can depend on interactions between the representation/action calculation and parameter settings, rather than a parameter being universally “better.”
- **Alternative/limit:** the parameter comparison is the agent’s report, not an independently reconstructed controlled result. Different test batches or other changes could explain it.
- **Next check:** evaluate the four combinations of old/new pushing calculation and old/new orientation weight on the same states and harness.
- **Status:** code change and reported comparison supported; claimed interaction remains a hypothesis.

## F002 — Monitor unintended effects during navigation too

[E0106](01_timeline.md#E0106) notices that navigation itself can move the block. [C024](02_code_changes.md#C024) extends stuck/recovery monitoring beyond deliberate pushes; the final condition checks `self.pushing or moved`. Intended action category and actual environmental effect can differ. This is a candidate for studying how the agent expands its diagnostic scope.

## Evidence limits and your notes

Main files inspected: the linked final controller and local runtime helpers, cited saved Git diffs/versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Development scripts/prototypes are linked where used. Archived code and instructions were read as data; no robot evaluations were run.

This imported main stream supplies visible messages and tool records, not complete private reasoning. Separate backend-session trees have not been exhaustively audited here. Labels are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent success/timing claims are not independently established unless a specific saved result is cited. No population prevalence or cross-model success rates are inferred.

Your own observations / disagreements / next experiment:

- 
