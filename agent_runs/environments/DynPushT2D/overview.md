# DynPushT2D — run index

[All environments](../../README.md) · [Shared protocol](../../protocol.md)

A circular pusher moves a T-shaped block to a target position and orientation through contact.

The earlier **GPT** reviews found stages, A* navigation and geometric pushing rules, without multi-step contact-dynamics rollouts in the final code. All five **Claude** cases contain predictive pushing calculations, but their depth and use differ: 24, 42 and 424 use two-push rollouts; 222 uses approximate maneuver look-ahead that can switch on/off after stalls; 444 keeps contact-model rollouts but disables the optional second push. These are findings about selected code, not a model-wide ranking.

| Run | Model / configured effort | Review status | Reading files |
| --- | --- | --- | --- |
| Replicate 24 | Codex GPT-5.6-sol / medium | Prior manual review | [Timeline](runs/codex_gpt56sol_r24_cee4702f/01_timeline.md) · [Changes](runs/codex_gpt56sol_r24_cee4702f/02_code_changes.md) · [Findings / notes](runs/codex_gpt56sol_r24_cee4702f/03_findings.md) |
| Replicate 424 | Codex GPT-5.6-sol / medium | Prior manual review | [Timeline](runs/codex_gpt56sol_r424_7e89c88a/01_timeline.md) · [Changes](runs/codex_gpt56sol_r424_7e89c88a/02_code_changes.md) · [Findings / notes](runs/codex_gpt56sol_r424_7e89c88a/03_findings.md) |
| Replicate 24 | Claude Opus 5.5 / high | Initial controller + selected trace review | [Timeline](runs/claude_opus55_high_r24_55605190/01_timeline.md) · [Changes](runs/claude_opus55_high_r24_55605190/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r24_55605190/03_findings.md) |
| Replicate 42 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r42_39564662/01_timeline.md) · [Changes](runs/claude_opus55_high_r42_39564662/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r42_39564662/03_findings.md) |
| Replicate 222 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r222_2702c656/01_timeline.md) · [Changes](runs/claude_opus55_high_r222_2702c656/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r222_2702c656/03_findings.md) |
| Replicate 424 | Claude Opus 5.5 / high | Initial controller + selected trace review | [Timeline](runs/claude_opus55_high_r424_2a46a52d/01_timeline.md) · [Changes](runs/claude_opus55_high_r424_2a46a52d/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r424_2a46a52d/03_findings.md) |
| Replicate 444 | Claude Opus 5.5 / high | Targeted controller + selected trace review | [Timeline](runs/claude_opus55_high_r444_2bf26d60/01_timeline.md) · [Changes](runs/claude_opus55_high_r444_2bf26d60/02_code_changes.md) · [Findings / notes](runs/claude_opus55_high_r444_2bf26d60/03_findings.md) |
| Replicate 24 | Codex GPT-6 Astra / high | Initial controller + selected trace review | [Timeline](runs/codex_gpt6astra_r24_644304ab/01_timeline.md) · [Changes](runs/codex_gpt6astra_r24_644304ab/02_code_changes.md) · [Findings / notes](runs/codex_gpt6astra_r24_644304ab/03_findings.md) |
| Replicate 424 | Codex GPT-6 Astra / high | Initial controller + selected trace review | [Timeline](runs/codex_gpt6astra_r424_4e86deee/01_timeline.md) · [Changes](runs/codex_gpt6astra_r424_4e86deee/02_code_changes.md) · [Findings / notes](runs/codex_gpt6astra_r424_4e86deee/03_findings.md) |

## Claude: what to inspect first

| Run | Execution structure | Prediction / search found | Development sequence |
| --- | --- | --- | --- |
| [Claude 24](runs/claude_opus55_high_r24_55605190/03_findings.md) | Labeled nav/push segments | Multi-step push simulation and a second-push rollout | C013: adopt LOOK=8 after a recorded width comparison |
| [Claude 42](runs/claude_opus55_high_r42_39564662/03_findings.md) | Navigation and push segments | Contact-model rollouts plus a second-push evaluation | C005: deeper planning after reported success |
| [Claude 222](runs/claude_opus55_high_r222_2702c656/03_findings.md) | Plan/approach/push phases | Approximate rotation/translation endpoint models; two-maneuver scoring | C025: toggle look-ahead after stalls |
| [Claude 424](runs/claude_opus55_high_r424_2a46a52d/03_findings.md) | Navigation then push segments | Multi-step push simulation and a second-push rollout | C005: increase planning depth; later trade off breadth/time |
| [Claude 444](runs/claude_opus55_high_r444_2bf26d60/03_findings.md) | Plan/navigation/push modes | Multi-step contact-model rollout; second-push branch disabled by M=0 | C010–C011: try deeper search, then disable it; later reconsider |

## Astra: what to inspect first

| Run | Execution structure | Prediction / search found | Development sequence |
| --- | --- | --- | --- |
| Astra 424 | Persistent move/push phases | Dijkstra navigation; analytic local contact response with friction/wall constraints | C023: constrain predicted pushes near walls |
| Astra 24 | Geometry-triggered navigation/pushing modes; contact memory | Dijkstra navigation; analytic normal/tangential contact response | C019: angled-push calculation; C024: monitor unintended navigation contact |

Astra gives a useful middle case: both programs explicitly predict local pushing response, but neither final controller rolls out a multi-push sequence. Keep this separate from the GPT-5.6 heuristic pushing rules and the different active/disabled look-ahead mechanisms in the five Claude cases. Also distinguish a persistent phase machine from a mode selected afresh using current geometry.

Open each run’s findings for exact functions, line ranges, commit links and messages. The earlier Claude/Astra notes describe their initial controller reviews; the 2026-10-11 Claude additions have targeted reviews of planner/execution functions, active flags and selected diffs/messages. Neither is exhaustive developmental annotation. No new robot evaluations were run.

Matching covers environment, replicate, task text, strict blackbox, no primitives, $20 generation budget and saved evaluation settings. Model effort, dates and potentially backend/software details differ; this is not a model-only causal comparison. A replicate is a development run, not an episode.

## Earlier GPT-only comparison

| Question | Replicate 424 | Replicate 24 |
| --- | --- | --- |
| Persistent phases | Supported | Supported |
| Multi-step geometric route search | A* | A* |
| Contact choice | Calculated centroid/contact rays and paired rotation strokes | Estimated center of mass and contact-side selection |
| Feedback | Observed rotation/displacement; stall checks | Observed drift; adaptive contact offset; stale-route checks |
| Multi-step contact-dynamics rollout | Not found in final code | Not found in final code |
| Task-level search over push sequences | Not found in final code | Not found in final code |

The useful distinction is what gets predicted. Both search possible pusher routes around a block whose pose is held fixed during search; neither final policy compares simulated future block trajectories from alternative multi-push plans. Feedback and mechanics-informed rules are not automatically model-free reinforcement learning.

Development examples: 424 substantially rewrites its early controller; 24 adds diagnostic logging before a stale-route repair and later reverts a restriction on a near-goal shortcut. Read their findings documents for exact event and commit links. These cases motivate a hypothesis about separate methods for navigation and manipulation; they do not establish prevalence across agents.

## Claude five-seed coverage

Seeds **24, 42, 222, 424 and 444** are distinct archived development runs of **claude-opus-5-5, high effort**. Fresh configurations match the existing Claude 424 reference except replicate seed and experiment identifier; the evaluation seed and task text are unchanged. These are not five independent draws of an evaluation benchmark. The added seeds extend within-Claude inspection; same-seed coverage for the other models is incomplete. See [selection and identity rules](../../protocol.md#coverage-identity-and-uncertainty).
