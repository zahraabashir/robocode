# Obstruction2D · Claude Opus 5.5 High · replicate 424

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). These are analyst notes to inspect, not an exhaustive hand-labeling of the run. Reviewed the complete final controller and its imported local runtime helpers; checked the cited code changes and trace events. No controller was executed.

## Controller: phases plus explicit plan comparison

**This Claude controller goes beyond the heuristic controller in the earlier GPT example.** It constructs and compares alternative obstruction-removal plans before executing one.

In [approach.py](evidence/final/approach.py), `_plan` (188–218) enumerates ordered subsets of obstructions. `_plan_subset` (244–323) branches over parking locations and updates a copied geometric scene (`ncur`) for subsequent choices. `_finish` adds the final target pickup and placement. `_sim_plan` (220–242) repeatedly calls the controller on predicted robot/arm positions, adds the predicted movement to those positions, and estimates execution length. This simulated length helps select the plan.

Execution still has stages: `self.legs` contains `pick`, `drop`, and `place`, and `self.leg` advances in `get_action` (382–458). The order and positions are outputs of planning. Thus phase structure and explicit look-ahead coexist.

**Limit:** this is a simplified geometric/kinematic model with assumed pickup/drop effects, candidate pruning and time limits. It is not a full simulator of every environment effect, and no optimality or model-accuracy claim is established here.

## F001 — Add simulated execution after already obtaining a working plan

[Message E0476](01_timeline.md#E0476) says the next improvement will compare candidate plans by simulated controller cost → [C010](02_code_changes.md#C010) adds candidate branching and `_sim_leg` → [E0487](01_timeline.md#E0487) reports an improvement and proposes wider candidate sets. In the final code this has become `_sim_plan`.

- **Observed:** the added simulation is actually used to choose a plan; it is not only mentioned in text. Earlier [C004](02_code_changes.md#C004) already introduced plan construction, so C010 is not the first planning code.
- **Interpretation:** development changes how plans are evaluated, while retaining a staged execution interface.
- **Alternative/limit:** the performance statements are agent reports; the code change alone does not isolate a causal improvement.
- **Next check:** compare C009/C010 under an identical harness, and inspect cases where simulation changes the chosen removal order or parking positions.
- **Status:** implementation change supported; benefit not independently reproduced.

## F002 — Search breadth responds to time concerns

[E0649](01_timeline.md#E0649) proposes wider search → [E0682](01_timeline.md#E0682) flags a 42-second test → [E0697](01_timeline.md#E0697) attributes much of it to concurrent testing, but still adds a safeguard. [C015](02_code_changes.md#C015) and [C016](02_code_changes.md#C016) add time guards. Final `_plan` and `_plan_subset` reduce search effort after elapsed-time thresholds; these are conditional, soft guards, not a guaranteed hard deadline.

This motivates a question about distinguishing controller compute costs from test-harness contention. It is not by itself evidence of optimal resource allocation.

## Evidence limits and your notes

The main files used here are `evidence/final/approach.py` (and linked runtime helpers), the cited saved Git diffs/versions, `evidence/stream.jsonl`, and `evidence/config.yaml`. Messages, tools and code support these observations; they do not expose complete private reasoning. All thinking blocks in this run’s imported stream have empty readable text; see [stream coverage](evidence/stream_coverage.json). Separate backend session trees have not been exhaustively audited here.

Labels here are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent statements about success, timing or model accuracy remain claims unless a specific saved output is cited. No cross-model success rates or prevalence estimates are aggregated.

Your own observations / disagreements / next experiment:

- 
