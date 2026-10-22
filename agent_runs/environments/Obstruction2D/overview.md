# Obstruction2D — run index

[All environments](../../README.md) · [Shared protocol](../../protocol.md)

Pick up and place a target block on a surface, moving obstructing blocks as needed.

The earlier **GPT 424** review found phases, greedy placement and constraints for later pickups. The five **Claude** cases vary: 24 and 42 use geometric path planning, 222 rolls out a motion estimate for scoring, and 424 and 444 compare task sequences. Staged execution and explicit planning can coexist at different levels. The seed-18 and five-repair examples belong to GPT 424, not to an additional development run.

| Run | Model / configured effort | Review status | Reading files |
| --- | --- | --- | --- |
| Replicate 424 | Codex GPT-5.6-sol / medium | Prior manual review | [Timeline](runs/codex_gpt56sol_r424_2c85c614/01_timeline.md) · [Changes](runs/codex_gpt56sol_r424_2c85c614/02_code_changes.md) · [Findings / notes](runs/codex_gpt56sol_r424_2c85c614/03_findings.md) |
| Replicate 24 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r24_f8729873/01_timeline.md) · [Changes](runs/claude_opus55_high_r24_f8729873/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r24_f8729873/03_findings.md) |
| Replicate 42 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r42_820cc0f3/01_timeline.md) · [Changes](runs/claude_opus55_high_r42_820cc0f3/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r42_820cc0f3/03_findings.md) |
| Replicate 222 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r222_c7b08ad0/01_timeline.md) · [Changes](runs/claude_opus55_high_r222_c7b08ad0/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r222_c7b08ad0/03_findings.md) |
| Replicate 424 | Claude Opus 5.5 / high | Initial controller + selected trace review | [Timeline](runs/claude_opus55_high_r424_b71e4671/01_timeline.md) · [Changes](runs/claude_opus55_high_r424_b71e4671/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r424_b71e4671/03_findings.md) |
| Replicate 444 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r444_0b82e686/01_timeline.md) · [Changes](runs/claude_opus55_high_r444_0b82e686/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r444_0b82e686/03_findings.md) |
| Replicate 24 | Codex GPT-6 Astra / high | Initial controller + selected trace review | [Timeline](runs/codex_gpt6astra_r24_29375d55/01_timeline.md) · [Changes](runs/codex_gpt6astra_r24_29375d55/02_code_changes.md) · [Findings / notes](runs/codex_gpt6astra_r24_29375d55/03_findings.md) |
| Replicate 424 | Codex GPT-6 Astra / high | Initial controller + selected trace review | [Timeline](runs/codex_gpt6astra_r424_51fd524e/01_timeline.md) · [Changes](runs/codex_gpt6astra_r424_51fd524e/02_code_changes.md) · [Findings / notes](runs/codex_gpt6astra_r424_51fd524e/03_findings.md) |

## Claude: what to inspect first

| Run | Execution structure | Prediction / search found | Development sequence |
| --- | --- | --- | --- |
| [Claude 24](runs/claude_opus55_high_r24_f8729873/03_findings.md) | Generator-based pickup/placement legs | Dynamic programming over position, height and arm extension; heuristic task order | C012: keep motion planning, disable its expensive placement-cost use |
| [Claude 42](runs/claude_opus55_high_r42_820cc0f3/03_findings.md) | Queued movement/grasp/carry operations | Geometric candidate path search; local dependencies and future-pickup costs | C018: represent jointly grasped objects as a carried group |
| [Claude 222](runs/claude_opus55_high_r222_c7b08ad0/03_findings.md) | Explicit manipulation phases | Iterative motion rollout for placement scoring; heuristic dependency-guided task selection | C007: replace a cost formula with a movement rollout |
| [Claude 424](runs/claude_opus55_high_r424_b71e4671/03_findings.md) | Planned pick/drop/place legs | Removal orders, parking choices, simulated controller execution | C010: use simulation to rank plans |
| [Claude 444](runs/claude_opus55_high_r444_0b82e686/03_findings.md) | Manipulation modes driven by a selected task plan | Compare removal orders and target staging using hypothetical object states | C011: choose whether moving the target first helps |

## Astra: what to inspect first

| Run | Execution structure | Prediction / search found | Development sequence |
| --- | --- | --- | --- |
| Astra 424 | Explicit manipulation phases | Geometric grasp/placement checks; reserves future pickup space; no full task rollout found | C032: reserve clearance for a later pickup |
| Astra 24 | Explicit manipulation phases | Grasp-dependency traversal and future-configuration checks; no full task rollout found | C012: replace taller-blocker rule with grasp dependencies |

These Astra controllers resemble the earlier GPT-5.6 example in using staged heuristics and anticipation without the alternative-task-plan rollouts found in Claude 424 and 444. This is a within-sample observation, not an estimate of model tendencies.

**Coverage:** Claude has five development seeds here; Astra has 24 and 424, while GPT-5.6 has only 424. Astra 24 now has a Claude 24 counterpart with matching task text and checked evaluation settings. There is still no three-model replicate-24 comparison for this environment.

Open each run’s findings for exact functions, line ranges, commit links and messages. The earlier Claude/Astra notes describe their initial controller reviews; the 2026-10-11 Claude additions have targeted reviews of planner/execution functions, active flags and selected diffs/messages. Neither is exhaustive developmental annotation. No new robot evaluations were run.

For the paired runs, matching covers environment, replicate, task text, strict blackbox, no primitives, $20 generation budget and saved evaluation settings. Model effort, dates and potentially backend/software details differ; this is not a model-only causal comparison. A replicate is a development run, not an episode.

## Claude five-seed coverage

Seeds **24, 42, 222, 424 and 444** are distinct archived development runs of **claude-opus-5-5, high effort**. Fresh configurations match the existing Claude 424 reference except replicate seed and experiment identifier; the evaluation seed and task text are unchanged. These are not five independent draws of an evaluation benchmark. The added seeds extend within-Claude inspection; same-seed coverage for the other models is incomplete. See [selection and identity rules](../../protocol.md#coverage-identity-and-uncertainty).
