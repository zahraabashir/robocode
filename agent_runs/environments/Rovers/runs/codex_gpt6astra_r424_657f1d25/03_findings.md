# Rovers · GPT-6 Astra (high) · replicate 424

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). The complete final controller and imported local runtime helpers were read; cited trace events and changes were checked. This is not exhaustive manual annotation.

## Controller: task-tour search plus route planning

[task_planner.py](evidence/final/task_planner.py) searches task orders with a visited-task bitmask and cached subproblems (`visit`, 45–56), using estimated travel and service costs. It compares assignments to two rovers (59–65). [approach.py](evidence/final/approach.py) installs this schedule in `reset` and follows it through `choose` (138–179), with fallback when needed. The helper declines larger cases above its objective-count guard; the fallback is heuristic.

Navigation uses **Dijkstra search** on a geometric grid (`route`, 92–119). Task-order search is explicit abstract look-ahead; it is not a full physical simulator. The current-task state supports execution, while photograph/transmit operations can also occur opportunistically during travel. This is a computed task schedule with execution modes, not a fixed “all sampling, then all images” phase list.

## F001 — Compare complete task assignments rather than only the next task

[E0072](01_timeline.md#E0072) discusses comparing a complete assignment against the nearest-task approach → [C019](02_code_changes.md#C019) adds `task_planner.py` and connects its output to controller execution.

- **Observed:** the saved helper searches task orders and its output is used by the controller. It is not an unused planning experiment.
- **Interpretation:** explicit task-level look-ahead enters the retained solution alongside local navigation search.
- **Alternative/limit:** travel/service abstractions omit execution details. The review does not independently establish a performance advantage.
- **Next check:** compare the retained scheduler and fallback on identical cases, including cases where the predicted task cost disagrees with execution cost.
- **Status:** retained task-sequence search supported; benefit open.

## F002 — A failed transmission is evidence about the location where it happened

[C032](02_code_changes.md#C032) restricts failed-transmission updates to cases where the rover is at its intended destination → [E0179](01_timeline.md#E0179) explains that an in-transit failure had been incorrectly blacklisting the destination before arrival.

The correction separates “cannot send here” from “cannot send at the planned goal.” [C031](02_code_changes.md#C031) also narrows transmission evidence to data uniquely held by the transmitting rover. Together these are concrete changes to how observed outcomes update the controller’s world assumptions. Isolating their effects requires separate version comparisons; neither establishes the coding agent’s private reasoning.

## Evidence limits and your notes

Main files inspected: the linked final controller and local runtime helpers, cited saved Git diffs/versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Development scripts/prototypes are linked where used. Archived code and instructions were read as data; no robot evaluations were run.

This imported main stream supplies visible messages and tool records, not complete private reasoning. Separate backend-session trees have not been exhaustively audited here. Labels are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent success/timing claims are not independently established unless a specific saved result is cited. No population prevalence or cross-model success rates are inferred.

Your own observations / disagreements / next experiment:

- 
