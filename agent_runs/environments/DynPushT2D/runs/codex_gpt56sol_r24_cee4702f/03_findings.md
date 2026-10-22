# DynPushT2D 24 — findings and your notes

[Timeline](01_timeline.md) · [All commits and changed lines](02_code_changes.md) · [Final controller](evidence/final/approach.py)

**Prior manual analysis migrated for review.** No new rollouts or private-reasoning claims were added during reorganization. Your notes in this file are preserved when the timeline is rebuilt.

## Start here

- **F001 — Add observation before repair:** [E0069](01_timeline.md#E0069) → [E0073](01_timeline.md#E0073) → [E0077](01_timeline.md#E0077) → [E0081](01_timeline.md#E0081).
- **F002 — Online contact adjustment:** [E0106](01_timeline.md#E0106) and the corresponding diff; observed angular drift updates the contact offset.
- **F003 — Anticipating unwanted drift:** [E0310](01_timeline.md#E0310) → [E0314](01_timeline.md#E0314).
- **F004 — Remove a planning safeguard after testing:** [E0535](01_timeline.md#E0535) → [E0539](01_timeline.md#E0539) → [E0541](01_timeline.md#E0541) → [E0545](01_timeline.md#E0545).

<a id="controller-details"></a>
## Controller and development evidence


Manual annotation for review, 2026-10-09. **Phase rules + explicit geometric A* + mechanics-informed contact choice + feedback with an adaptive contact offset.** No multi-step prediction of candidate push sequences was found in the complete final controller.

## Implemented mechanisms

All line numbers refer to the copied final [approach.py](evidence/final/approach.py), verified against the saved policy and HEAD hashes. Only `math`, `heapq`, and NumPy are imported; development files such as `candidate_strategy.py` are not imported by this final policy.

| Mechanism | Evidence and interpretation |
| --- | --- |
| Phase decomposition | Lines 13–26 reset persistent phase/feedback state. Lines 110–155 choose rotation or translation; 157–268 implement approach, contact, push, and retreat phases. |
| Geometric model and search | Lines 44–99 construct an expanded two-rectangle T approximation on a 0.12 grid. Eight-neighbor successors, collision checks, accumulated costs, a Euclidean heuristic, and parent reconstruction implement A* directly. The block pose stays fixed within the search. |
| Connection to actions | `get_action` calls `_plan` at 140 and 149; `rot_far` consumes waypoints at 177–180 and `move_far` at 220–223. |
| Predictive contact heuristic | Lines 130–140 select a stem-side or cap-end contact using the presumed direction of translation accompanying rotation. The dot product checks whether the push direction helps positional error; it does not compute a predicted next block pose. |
| Feedback-based replanning | Lines 172–176 and 215–219 compare the observed block pose with the pose at plan creation. If it changed enough, abandon the route and choose again. |
| Adaptive contact rule | Lines 249–250 and 256–257 update `line_offset` using observed angular change. This shifts the assumed translation contact line (211–212). The offset resets each episode (23). It is an online correction rule, not a learned transition predictor or value function. |
| Explicit planner bypass | Lines 149–151 calculate a translation-approach route and then erase it if positional error is below 0.15. Direct approach follows once the waypoint list is empty. |

The final controller combines model-based navigation with reactive and adaptive manipulation. A* uses a geometric approximation; it does not simulate contact physics. Evaluating three lever fractions for current boundary clearance (120–125) is candidate scoring, not multi-step planning.

Search can fail and return an empty route (84–85); subsequent control approaches the contact staging point directly. The final target is appended after grid search without checking that exact continuous target against the obstacle model (98). Thus route search does not guarantee physically collision-free control. Runtime frequencies of these branches were not measured.

## Development sequences

**Introducing and diagnosing planning:** short contact strokes replace an earlier endpoint strategy ([L51](01_timeline.md#E0051), commit `5f07c86`) → A* replaces a hand-set detour ([diff 3db79a0](02_code_changes.md#C023), [L69](01_timeline.md#E0069)) → test still fails → add transition/waypoint logging ([L73](01_timeline.md#E0073)) → increase pose sampling ([L77](01_timeline.md#E0077)) → enlarge clearance and abort stale routes ([L81](01_timeline.md#E0081), [diff d523a1c](02_code_changes.md#C026)).

L73 prints multi-waypoint routes actually produced during execution. L77 records a changing block pose while still approaching. This directly supports the distinction between a static geometric planner and a contact-sensitive physical task. The repair changes both clearance and replanning, so its effects cannot be attributed to either change alone from this sequence.

**Adding online correction:** [commit f6a9314](02_code_changes.md#C030), recorded/tested at [L106](01_timeline.md#E0106), adds a contact offset updated from measured angular change. The final code retains this mechanism. “Observe rotation → adjust where to push next” is supported; “simulate future rotation before choosing a push” is not.

**Anticipating unwanted drift:** [L310](01_timeline.md#E0310) proposes choosing between contacts that rotate in the same direction but translate differently → [commit 4abcf8e](02_code_changes.md#C057) adds the directional rule → final lines 130–135 retain it. This is a mechanics-informed anticipation rule, even without quantitative dynamics simulation.

**Adding then removing a planning safeguard:** [L535](01_timeline.md#E0535) says the final-approach shortcut discarded an 11-waypoint route → [3891024](02_code_changes.md#C086) restricts bypass to routes with at most two waypoints → [L541](01_timeline.md#E0541) reports 6/10 in a selected test batch → [37b79db](02_code_changes.md#C087), recorded at L545, restores the broader shortcut. The commit title claims a higher score; this fragment alone does not provide a matched evaluation proving superiority. Final lines 149–151 confirm the broader shortcut survived later revisions.

## Scope

The archive contains 77 commits affecting `approach.py`, including reverts, and 774 main-stream lines. `_plan` first appears in the tenth saved policy commit. These are one development run with resumed turns, not 77 independent runs or necessarily 77 repairs. Final HEAD includes a later commit beyond the last policy-changing commit; the final policy hash still matches the saved working file and latest policy version.

Final code was read in full; main messages, selected diagnostic outputs, and relevant historical diffs were inspected. All policy versions/diffs were exported. Development helpers and backend/subagent reasoning were not comprehensively audited. No fresh performance comparison or simulator execution was performed. These are mechanism annotations, not completed ACT*ONOMY transcript labels. See [evidence manifest](evidence/manifest.json) and the [two-run comparison](../../overview.md).

## Your inspection notes

### Next finding — working title

- Sequence/event IDs:
- Observed evidence:
- Interpretation:
- Alternative explanation:
- Next check:
- Status:
