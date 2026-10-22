# Rovers — run index

[All environments](../../README.md) · [Shared protocol](../../protocol.md)

Two rovers collect samples, take photographs, transmit findings, empty stores and return home. This is a PDDLStream-based environment included alongside KinDER tasks.

**GPT 424** combines programmed phases with A* navigation; GPT 24 still awaits manual classification. All five **Claude** cases contain explicit task-level search, using different state representations and approximations. Their task sequences are computed, rather than simply following a fixed list of activity phases. Some also predict other-rover motion or combine operations with travel.

| Run | Model / configured effort | Review status | Reading files |
| --- | --- | --- | --- |
| Replicate 24 | Codex GPT-5.6-sol / medium | Manual review pending | [Timeline](runs/codex_gpt56sol_r24_de120909/01_timeline.md) · [Changes](runs/codex_gpt56sol_r24_de120909/02_code_changes.md) · [Findings / notes](runs/codex_gpt56sol_r24_de120909/03_findings.md) |
| Replicate 424 | Codex GPT-5.6-sol / medium | Prior manual review | [Timeline](runs/codex_gpt56sol_r424_0dc2ee42/01_timeline.md) · [Changes](runs/codex_gpt56sol_r424_0dc2ee42/02_code_changes.md) · [Findings / notes](runs/codex_gpt56sol_r424_0dc2ee42/03_findings.md) |
| Replicate 24 | Claude Opus 5.5 / high | Initial controller + selected trace review | [Timeline](runs/claude_opus55_high_r24_1cd6a7a5/01_timeline.md) · [Changes](runs/claude_opus55_high_r24_1cd6a7a5/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r24_1cd6a7a5/03_findings.md) |
| Replicate 42 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r42_181ed19d/01_timeline.md) · [Changes](runs/claude_opus55_high_r42_181ed19d/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r42_181ed19d/03_findings.md) |
| Replicate 222 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r222_c6c9dc31/01_timeline.md) · [Changes](runs/claude_opus55_high_r222_c6c9dc31/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r222_c6c9dc31/03_findings.md) |
| Replicate 424 | Claude Opus 5.5 / high | Initial controller + selected trace review | [Timeline](runs/claude_opus55_high_r424_4c49acd0/01_timeline.md) · [Changes](runs/claude_opus55_high_r424_4c49acd0/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r424_4c49acd0/03_findings.md) |
| Replicate 444 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r444_2af61ade/01_timeline.md) · [Changes](runs/claude_opus55_high_r444_2af61ade/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r444_2af61ade/03_findings.md) |
| Replicate 24 | Codex GPT-6 Astra / high | Initial controller + selected trace review | [Timeline](runs/codex_gpt6astra_r24_10c7bc43/01_timeline.md) · [Changes](runs/codex_gpt6astra_r24_10c7bc43/02_code_changes.md) · [Findings / notes](runs/codex_gpt6astra_r24_10c7bc43/03_findings.md) |
| Replicate 424 | Codex GPT-6 Astra / high | Initial controller + selected trace review | [Timeline](runs/codex_gpt6astra_r424_657f1d25/01_timeline.md) · [Changes](runs/codex_gpt6astra_r424_657f1d25/02_code_changes.md) · [Findings / notes](runs/codex_gpt6astra_r424_657f1d25/03_findings.md) |

## Claude: what to inspect first

| Run | Execution structure | Prediction / search found | Development sequence |
| --- | --- | --- | --- |
| [Claude 24](runs/claude_opus55_high_r24_1cd6a7a5/03_findings.md) | Search-generated operator sequence and plan pointer | Time-expanded BFS with discrete task state and geometry | Build alternative → compare → adopt; old controller preserved |
| [Claude 42](runs/claude_opus55_high_r42_181ed19d/03_findings.md) | Computed task order; movement and operations can overlap | Task-order/assignment search, Dijkstra fields, predicted operation validity | C011: finish a task while traveling toward the next |
| [Claude 222](runs/claude_opus55_high_r222_c6c9dc31/03_findings.md) | Search-generated position/operation sequence | Task-subset and spatial dynamic programming with calibration state | C018: exact rollback of costly camera-heading planner |
| [Claude 424](runs/claude_opus55_high_r424_4c49acd0/03_findings.md) | Computed task order; stage-indexed execution | Subset dynamic programming, transition-model rollouts, predicted other-rover motion | C003: add simulator; C011: revise model and executor |
| [Claude 444](runs/claude_opus55_high_r444_2af61ade/03_findings.md) | Computed schedule with temporal/spatial refinement | Task-order DFS, assignment search and predicted transmission timing | C009–C011: timed prediction requires backtracking that supports waiting |

## Astra: what to inspect first

| Run | Execution structure | Prediction / search found | Development sequence |
| --- | --- | --- | --- |
| Astra 424 | Computed task schedule, current-task state and opportunistic operations | Task-tour/assignment search plus Dijkstra navigation | C019: integrate task planner; C032: correct where failed-send evidence applies |
| Astra 24 | Greedy task choice each observation; opportunistic operations | Dijkstra navigation; final controller does not retain a task-tour planner | Build two planning alternatives → compare → retain simpler scheduler; transfer a repair |

Replicate 24 is especially useful for your development-trace question: the final policy hides task-planning approaches tried and not adopted. Its saved comparisons do not establish that every alternative was worse; see the findings for the small numerical differences and remaining uncertainty. Neither Astra controller should automatically receive the same fixed-phase label as an explicit sequential phase machine.

Open each run’s findings for exact functions, line ranges, commit links and messages. The earlier Claude/Astra notes describe their initial controller reviews; the 2026-10-11 Claude additions have targeted reviews of planner/execution functions, active flags and selected diffs/messages. Neither is exhaustive developmental annotation. No new robot evaluations were run.

Matching covers environment, replicate, task text, strict blackbox, no primitives, $20 generation budget and saved evaluation settings. Model effort, dates and potentially backend/software details differ; this is not a model-only causal comparison. A replicate is a development run, not an episode.

## Claude five-seed coverage

Seeds **24, 42, 222, 424 and 444** are distinct archived development runs of **claude-opus-5-5, high effort**. Fresh configurations match the existing Claude 424 reference except replicate seed and experiment identifier; the evaluation seed and task text are unchanged. These are not five independent draws of an evaluation benchmark. The added seeds extend within-Claude inspection; same-seed coverage for the other models is incomplete. See [selection and identity rules](../../protocol.md#coverage-identity-and-uncertainty).
