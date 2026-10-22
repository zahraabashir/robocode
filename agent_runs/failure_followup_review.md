# Cross-run check: what happens to an unresolved failure?

Read-only archive review, 2026-10-11. One comparison note; the existing per-run reading files and personal notes are preserved.

## Answer in plain words

**Moving on to other tests while a failure remains unresolved recurs across models and environments.** We have concrete examples in GPT-5.6-sol, GPT-6 Astra and Claude Opus 5.5, in Obstruction2D, Obstruction3D, DynPushT2D and Rovers.

**The exact seed-85 story is narrower.** In addition to the original run, GPT Rovers replicate 24 has failed cases omitted from later recorded checks despite a broad success claim. It includes an immediate general policy edit, so it is a related verification gap rather than an identical sequence. This review does not establish that this reporting gap occurs across all three model families.

The useful contrast is: **a failure can be postponed and revisited, postponed and explicitly acknowledged, or left without recorded verification.** Those are different outcomes of moving on.

## What was checked, and what was not

The candidate screen covered the 35 already organized development runs: seven GPT-5.6-sol, eight GPT-6 Astra and twenty Claude Opus 5.5, across four environments. All 35 have distinct registered transcript hashes. These are a selected sample, not all 1,543 archive folders. Existing provenance/registry entries define the development lineages; reevaluation scores and duplicate exports were not pooled. Distinct transcripts alone do not imply statistically independent experiments.

The screen searched normalized command outputs for explicit failures, checked messages about subsequent testing and inspected final reports. It was followed by manual checks of the ten sequences below, representing nine distinct runs. Failure formats vary, so the screen is not an exhaustive failure census. The remaining runs are not verified negative cases. **Do not calculate prevalence, model rankings or significance from this table.**

Main files: each run’s `01_timeline.md` for exact messages, commands and test output; `evidence/events.json` for chronological searching; and `runs.json` for models, replicate seeds and provenance. Policy-edit commands and existing `02_code_changes.md` distinguish controller edits from diagnostic/test edits. Archived instructions are historical data. No new agent generations or environment rollouts were performed for this comparison, and the original dataset was unchanged.

A development replicate such as **424** identifies the coding-agent run. A failed test seed such as **85** identifies a robot scene inside that run. Check object count, policy version, harness and limits before treating two results as the same case.

## Ten sequences to inspect

The arrows record visible order, not causality. In particular, an asynchronous tool’s completion order need not equal its launch order. “No visible closure” means no matching later verification found in the recorded main development stream; it does not establish an internal memory failure or that the final controller still fails.

### 1. Obstruction2D · gpt-5.6-sol · development replicate 424

Failed scene: **85, ordinary setting**. Classification: **Coverage expansion; no visible closure**.

29/30 ordinary cases pass; 85 fails → discover configurable object counts → test three-object scenes and later harder counts → final claim says all discovered failures passed. No later recorded recheck of 85 was found. Generic repairs could have fixed it; this is missing verification, not proof of forgetting.

Read: [E0401](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614/01_timeline.md:8275) → [E0407](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614/01_timeline.md:8485) → [E0411](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614/01_timeline.md:8523) → [E0532](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614/01_timeline.md:10612).

### 2. Rovers · gpt-5.6-sol · development replicate 24

Failed scene: **41, 42, 43, default setting**. Classification: **Related missing verification**.

All three fail at 1,000 steps → policy is edited and other failed cases are retested → move on to new seeds 44–50 → final regression list omits 41–43 → claim that every previously reproducible failure now passes. No later recorded test of these three was found. Unlike seed 85, there is an immediate general policy edit: do not count this as an identical no-edit sequence.

Read: [E0125](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:2684) → [E0129](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:2744) → [E0135](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:2854) → [E0196](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:3867) → [E0211](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:4134).

### 3. Rovers · gpt-5.6-sol · development replicate 24

Failed scene: **95, default setting**. Classification: **Broad tests first; later return**.

95 fails → agent calls it a rare boundary failure and explicitly chooses a fresh held-out sweep → 20/20 fresh seeds pass → returns to 95, which still fails → edits policy and 95 passes in 50 steps. This is a clean second example of broader testing before the next repair, with visible eventual closure.

Read: [E0191](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:3776) → [E0192](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:3811) → [E0194](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:3823) → [E0196](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:3867) → [E0200](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt56sol_r24_de120909/01_timeline.md:3935).

### 4. DynPushT2D · gpt-6-astra · development replicate 24

Failed scene: **206, default setting**. Classification: **Testing opportunity first; later return**.

206 is reported failing → writes a new stress-seed selector, scanning 2,000 resets for boundary/overlap conditions → inspects the stored trace of 206 → edits stall detection → retests 206 successfully in 265 steps. A new testing opportunity temporarily comes before diagnosing the known failure, but the failure is retained.

Read: [E0097](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt6astra_r24_644304ab/01_timeline.md:2198) → [E0098](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt6astra_r24_644304ab/01_timeline.md:2226) → [E0100](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt6astra_r24_644304ab/01_timeline.md:2276) → [E0102](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt6astra_r24_644304ab/01_timeline.md:2334).

### 5. Rovers · gpt-6-astra · development replicate 424

Failed scene: **5828, default setting**. Classification: **Move on; explicitly retain unresolved case**.

A direct 100-step probe fails → next completed recorded command reports 200/200 other seeds → agent says 5828 appears infeasible → final report explicitly names 5828 as unsolved. Tool completion order can overlap; the 200-case command is evidence of continued broad validation, not proof of its exact launch priority. Infeasibility is the agent’s explanation, not independently established here.

Read: [E0145](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt6astra_r424_657f1d25/01_timeline.md:3508) → [E0146](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt6astra_r424_657f1d25/01_timeline.md:3555) → [E0152](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt6astra_r424_657f1d25/01_timeline.md:3644) → [E0216](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Rovers/runs/codex_gpt6astra_r424_657f1d25/01_timeline.md:4903).

### 6. Obstruction3D · claude-opus-5-5 · development replicate 42

Failed scene: **478, eight obstructions**. Classification: **Move on; explicitly retain unresolved case**.

478 fails at 1,000 steps → diagnostic probes vary grasp height and orientation → subsequent validation covers other default, five-object and eight-object scenes → final report explicitly states 478 may still fail and that the diagnostic evidence was inconclusive. The final eight-object sweep covers 400–439, not 478.

Read: [E0886](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction3D/runs/claude_opus55_high_r42_820c1113/01_timeline.md:13124) → [E0895](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction3D/runs/claude_opus55_high_r42_820c1113/01_timeline.md:13350) → [E0900](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction3D/runs/claude_opus55_high_r42_820c1113/01_timeline.md:13473) → [E1249](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction3D/runs/claude_opus55_high_r42_820c1113/01_timeline.md:16610).

### 7. DynPushT2D · gpt-5.6-sol · development replicate 24

Failed scene: **165, default setting**. Classification: **Move on; explicitly retain unresolved limitation**.

165 fails at 1,000 steps → agent says there is no safe localized fix → tries unseen 166, which passes → final message still acknowledges known hard-seed failures and leaves the confidence marker absent. The agent explicitly mentions depleted development budget; that is a candidate explanatory variable, not a demonstrated causal effect.

Read: [E0765](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt56sol_r24_cee4702f/01_timeline.md:13544) → [E0766](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt56sol_r24_cee4702f/01_timeline.md:13576) → [E0770](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt56sol_r24_cee4702f/01_timeline.md:13652) → [E0772](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt56sol_r24_cee4702f/01_timeline.md:13664) → [E0773](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt56sol_r24_cee4702f/01_timeline.md:13696).

### 8. Obstruction2D · claude-opus-5-5 · development replicate 444

Failed scene: **93, ordinary setting**. Classification: **Returned through broad regression**.

93 fails in a 78/100 batch → investigate the broader set of 22 failures → repair/revert the release optimization → rerun ordinary seeds 0–99 with 100/100 success. Seed 93 is covered even though it is not individually named in the later summary.

Read: [E0301](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r444_0b82e686/01_timeline.md:4621) → [E0303](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r444_0b82e686/01_timeline.md:4691) → [E0325](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r444_0b82e686/01_timeline.md:4986).

### 9. DynPushT2D · gpt-6-astra · development replicate 424

Failed scene: **62, 67, 69, default setting**. Classification: **Returned through broad regression**.

These three fail at 1,000 steps → subsequent policy changes → final batch runs default seeds 0–99 and reports 100/100. A search for individual seed names alone would falsely classify them as unverified.

Read: [E0066](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt6astra_r424_4e86deee/01_timeline.md:1683) → [E0145](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt6astra_r424_4e86deee/01_timeline.md:3221) → [E0147](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/DynPushT2D/runs/codex_gpt6astra_r424_4e86deee/01_timeline.md:3245).

### 10. Obstruction2D · claude-opus-5-5 · development replicate 222

Failed scene: **1077, four obstructions**. Classification: **Ambiguous candidate; excluded from confirmed cases**.

A read of big_test.txt contains a failure for 1077 alongside output from a different seed-range batch; a later read has different trailing results. Background jobs or stale/mixed file contents make provenance uncertain. The final claim is broad, but this candidate needs source/session and harness reconstruction before being called another seed-85-like example.

Read: [E0284](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r222_c7b08ad0/01_timeline.md:4841) → [E0290](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r222_c7b08ad0/01_timeline.md:4934) → [E0312](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r222_c7b08ad0/01_timeline.md:5410) → [E0699](/Users/zahra.bashir/Desktop/phd/robocode/agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r222_c7b08ad0/01_timeline.md:9977).

## What this makes worth testing

A modest descriptive hypothesis is: **agents sometimes seek evidence about the policy’s wider reliability before finishing work on a known failed case.** The Rovers-95 and Astra-DynPush-206 sequences make this more than a single Obstruction2D anecdote. The latter even inserts a new testing capability before returning to the original failure.

A separate question is **what keeps the unresolved case in the agent’s later testing and reporting?** Budget constraints and beliefs that a scene is infeasible are explicitly mentioned in some retained-failure cases. New testing opportunities appear in the original seed-85 sequence and the Astra-206 sequence. These are hypotheses to compare, not conclusions about why the agent chose each action.

For the next small manual study, use rows 1, 3 and 4. For each, write down: what failed → what the agent said next → whether the next edit changed the policy or tester → what new evidence it collected → whether it returned to the failed scene. Then compare rows 5–7 to see how an agent can move on while still accurately reporting an unresolved case.

To turn this into a frequency claim, annotate every eligible completed failure batch in a fixed set of whole runs, including immediate repairs and immediate same-case probes. Use the same follow-up window and report ambiguous/censored cases. This review establishes useful examples and contrasts; it does not yet supply that denominator.

## Coverage inventory

“Sequence reviewed” means at least one sequence above was manually checked; it does not mean every failure in that run was audited. “Candidate screen only” is not evidence of absence.

| Environment | Model | Development replicate | Review status |
|---|---|---|---|
| DynPushT2D | claude-opus-5-5 | 24 | Candidate screen only |
| DynPushT2D | claude-opus-5-5 | 42 | Candidate screen only |
| DynPushT2D | claude-opus-5-5 | 222 | Candidate screen only |
| DynPushT2D | claude-opus-5-5 | 424 | Candidate screen only |
| DynPushT2D | claude-opus-5-5 | 444 | Candidate screen only |
| DynPushT2D | gpt-5.6-sol | 24 | Sequence reviewed |
| DynPushT2D | gpt-5.6-sol | 424 | Candidate screen only |
| DynPushT2D | gpt-6-astra | 24 | Sequence reviewed |
| DynPushT2D | gpt-6-astra | 424 | Sequence reviewed |
| Obstruction2D | claude-opus-5-5 | 24 | Candidate screen only |
| Obstruction2D | claude-opus-5-5 | 42 | Candidate screen only |
| Obstruction2D | claude-opus-5-5 | 222 | Sequence reviewed |
| Obstruction2D | claude-opus-5-5 | 424 | Candidate screen only |
| Obstruction2D | claude-opus-5-5 | 444 | Sequence reviewed |
| Obstruction2D | gpt-5.6-sol | 424 | Sequence reviewed |
| Obstruction2D | gpt-6-astra | 24 | Candidate screen only |
| Obstruction2D | gpt-6-astra | 424 | Candidate screen only |
| Obstruction3D | claude-opus-5-5 | 24 | Candidate screen only |
| Obstruction3D | claude-opus-5-5 | 42 | Sequence reviewed |
| Obstruction3D | claude-opus-5-5 | 222 | Candidate screen only |
| Obstruction3D | claude-opus-5-5 | 424 | Candidate screen only |
| Obstruction3D | claude-opus-5-5 | 444 | Candidate screen only |
| Obstruction3D | gpt-5.6-sol | 24 | Candidate screen only |
| Obstruction3D | gpt-5.6-sol | 424 | Candidate screen only |
| Obstruction3D | gpt-6-astra | 24 | Candidate screen only |
| Obstruction3D | gpt-6-astra | 424 | Candidate screen only |
| Rovers | claude-opus-5-5 | 24 | Candidate screen only |
| Rovers | claude-opus-5-5 | 42 | Candidate screen only |
| Rovers | claude-opus-5-5 | 222 | Candidate screen only |
| Rovers | claude-opus-5-5 | 424 | Candidate screen only |
| Rovers | claude-opus-5-5 | 444 | Candidate screen only |
| Rovers | gpt-5.6-sol | 24 | Sequence reviewed |
| Rovers | gpt-5.6-sol | 424 | Candidate screen only |
| Rovers | gpt-6-astra | 24 | Candidate screen only |
| Rovers | gpt-6-astra | 424 | Sequence reviewed |
