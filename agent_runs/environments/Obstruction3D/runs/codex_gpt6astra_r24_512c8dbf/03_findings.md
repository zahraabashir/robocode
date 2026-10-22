# Obstruction3D · GPT-6 Astra (high) · replicate 24

[Timeline](01_timeline.md) · [Code changes](02_code_changes.md) · [Environment comparison](../../overview.md)

Status: **initial controller review and selected development sequences** (2026-10-10). The complete final controller and imported local runtime helpers were read; cited trace events and changes were checked. This is not exhaustive manual annotation.

## Controller: explicit kinematics, staged manipulation and recovery

[kin.py](evidence/final/kin.py) defines forward kinematics (5–11) and closed-form inverse kinematics (13–22). [approach.py](evidence/final/approach.py) uses them to execute above → align → grasp → lift → carry → lower → release stages. Object order, destination selection and postponement are heuristic; no multi-action state rollout was found.

[C032](02_code_changes.md#C032) replaces iterative inverse kinematics with a trigonometric solution; [E0099](01_timeline.md#E0099) describes this change. The model remains explicit even though finding a joint configuration no longer requires iterative numerical search. A faster implementation is plausible, but this review does not supply an isolated timing comparison.

## F001 — Undo a completed placement when the empty gripper cannot escape

[E0179](01_timeline.md#E0179) reports a post-release trap and proposes an escape test → [C046](02_code_changes.md#C046) adds regrasp-and-relocate recovery → [E0185](01_timeline.md#E0185) reports that the experiment worked → [C047](02_code_changes.md#C047) remembers problematic placements across attempts.

- **Observed:** final approach lines 97–106 detect the post-release problem, regrasp the object, insert it into the task list again, and mark a bad placement site. `choose_destination` uses bad-site memory.
- **Interpretation:** placing the object is not sufficient for completing the subtask; the robot must also be able to leave. The controller revises a locally completed action after seeing a downstream consequence.
- **Alternative/limit:** this is feedback recovery, not evidence of advance simulation of the escape trajectory. Several recovery details develop across commits; later success cannot automatically be credited to one line.
- **Next check:** compare pre/post-recovery versions on the saved trap and new scenes; distinguish regrasp success, escape success and full-task success.
- **Status:** recovery mechanism and development sequence supported; generalization open.

## Evidence limits and your notes

Main files inspected: the linked final controller and local runtime helpers, cited saved Git diffs/versions, [raw transcript](evidence/stream.jsonl), and [configuration](evidence/config.yaml). Development scripts/prototypes are linked where used. Archived code and instructions were read as data; no robot evaluations were run.

This imported main stream supplies visible messages and tool records, not complete private reasoning. Separate backend-session trees have not been exhaustively audited here. Labels are descriptive mechanism judgments, **not formal ACT*ONOMY annotations**. Agent success/timing claims are not independently established unless a specific saved result is cited. No population prevalence or cross-model success rates are inferred.

Your own observations / disagreements / next experiment:

- 
