# Obstruction3D — run index

[All environments](../../README.md) · [Shared protocol](../../protocol.md)

Move obstructing objects and place a target using a seven-joint arm in a 3D scene.

All five inspected **Claude** controllers use kinematic models, with different predictive checks and execution structures. Replicate 222 can merge travel and descent after checking a combined trajectory; 444 compares short motion plans and can reposition the base. Do not infer full removal-order search from these geometric predictions. Both **GPT** controllers still await manual classification: pending does not mean no planning.

| Run | Model / configured effort | Review status | Reading files |
| --- | --- | --- | --- |
| Replicate 24 | Codex GPT-5.6-sol / medium | Manual review pending | [Timeline](runs/codex_gpt56sol_r24_065956b8/01_timeline.md) · [Changes](runs/codex_gpt56sol_r24_065956b8/02_code_changes.md) · [Findings / notes](runs/codex_gpt56sol_r24_065956b8/03_findings.md) |
| Replicate 424 | Codex GPT-5.6-sol / medium | Manual review pending | [Timeline](runs/codex_gpt56sol_r424_9332a06b/01_timeline.md) · [Changes](runs/codex_gpt56sol_r424_9332a06b/02_code_changes.md) · [Findings / notes](runs/codex_gpt56sol_r424_9332a06b/03_findings.md) |
| Replicate 24 | Claude Opus 5.5 / high | Initial controller + selected trace review | [Timeline](runs/claude_opus55_high_r24_024d0ca5/01_timeline.md) · [Changes](runs/claude_opus55_high_r24_024d0ca5/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r24_024d0ca5/03_findings.md) |
| Replicate 42 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r42_820c1113/01_timeline.md) · [Changes](runs/claude_opus55_high_r42_820c1113/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r42_820c1113/03_findings.md) |
| Replicate 222 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r222_f6aa665e/01_timeline.md) · [Changes](runs/claude_opus55_high_r222_f6aa665e/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r222_f6aa665e/03_findings.md) |
| Replicate 424 | Claude Opus 5.5 / high | Initial controller + selected trace review | [Timeline](runs/claude_opus55_high_r424_3f9182d7/01_timeline.md) · [Changes](runs/claude_opus55_high_r424_3f9182d7/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r424_3f9182d7/03_findings.md) |
| Replicate 444 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r444_4a56791c/01_timeline.md) · [Changes](runs/claude_opus55_high_r444_4a56791c/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r444_4a56791c/03_findings.md) |
| Replicate 24 | Codex GPT-6 Astra / high | Initial controller + selected trace review | [Timeline](runs/codex_gpt6astra_r24_512c8dbf/01_timeline.md) · [Changes](runs/codex_gpt6astra_r24_512c8dbf/02_code_changes.md) · [Findings / notes](runs/codex_gpt6astra_r24_512c8dbf/03_findings.md) |
| Replicate 424 | Codex GPT-6 Astra / high | Initial controller + selected trace review | [Timeline](runs/codex_gpt6astra_r424_cf2d0159/01_timeline.md) · [Changes](runs/codex_gpt6astra_r424_cf2d0159/02_code_changes.md) · [Findings / notes](runs/codex_gpt6astra_r424_cf2d0159/03_findings.md) |

## Claude: what to inspect first

| Run | Execution structure | Prediction / search found | Development sequence |
| --- | --- | --- | --- |
| [Claude 24](runs/claude_opus55_high_r24_024d0ca5/03_findings.md) | Explicit grasp/place phases | Kinematic paths and sampled shortcut clearance; task choice remains heuristic | Rewrite → controller repair → tester defect discovered |
| [Claude 42](runs/claude_opus55_high_r42_820c1113/03_findings.md) | Pickup/grasp/placement/release phases | Kinematics and a local hypothetical blocker-removal check | C018–C019: add then remove a future-travel cost term |
| [Claude 222](runs/claude_opus55_high_r222_f6aa665e/03_findings.md) | Queued operations; travel/descent can merge | Kinematic candidate trajectories, sampled clearance, future-goal reachability | C020: predict a combined movement; retain staged fallback |
| [Claude 424](runs/claude_opus55_high_r424_3f9182d7/03_findings.md) | Queued approach/grasp/transfer/release operations | Kinematics and endpoint clearance; no complete task-sequence rollout found | C017: grasp choice checks later placement |
| [Claude 444](runs/claude_opus55_high_r444_4a56791c/03_findings.md) | Movement/base/gripper/check queue | Kinematic short-plan comparison; bounded grasp dependencies | C024–C025: add base repositioning and retain it |

## Astra: what to inspect first

| Run | Execution structure | Prediction / search found | Development sequence |
| --- | --- | --- | --- |
| Astra 424 | Manipulation phases and recovery | Calibrated forward kinematics, numerical inverse kinematics, local clearance scoring | Fit a model from measured transforms → integrate it into control |
| Astra 24 | Manipulation phases and recovery | Forward kinematics and closed-form inverse kinematics; geometric destination checks | Iterative IK → closed form; release trap → regrasp and relocate |

Both use explicit models at runtime, but no multi-action task rollout was found in their final controllers. Having a kinematic model is different from searching a sequence of object removals.

Open each run’s findings for exact functions, line ranges, commit links and messages. The earlier Claude/Astra notes describe their initial controller reviews; the 2026-10-11 Claude additions have targeted reviews of planner/execution functions, active flags and selected diffs/messages. Neither is exhaustive developmental annotation. No new robot evaluations were run.

Matching covers environment, replicate, task text, strict blackbox, no primitives, $20 generation budget and saved evaluation settings. Model effort, dates and potentially backend/software details differ; this is not a model-only causal comparison. A replicate is a development run, not an episode.

## Claude five-seed coverage

Seeds **24, 42, 222, 424 and 444** are distinct archived development runs of **claude-opus-5-5, high effort**. Fresh configurations match the existing Claude 424 reference except replicate seed and experiment identifier; the evaluation seed and task text are unchanged. These are not five independent draws of an evaluation benchmark. The added seeds extend within-Claude inspection; same-seed coverage for the other models is incomplete. See [selection and identity rules](../../protocol.md#coverage-identity-and-uncertainty).
