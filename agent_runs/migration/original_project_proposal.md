# One development decision in KiNDER

Proposal date: 2026-10-03. Status: proposed; no new policy replay or ACT*ONOMY annotation has been performed.

## Question

Can a small ACT*ONOMY annotation, checked against a code change and its test feedback, characterize how a coding agent revised one robot-policy decision rule?

## Smallest unit

One failure–diagnostic probe–edit–retest sequence. One coding-agent run, one environment, one episode seed, two adjacent saved policy versions. The first deliverable is an inspectable case study, not a dataset-wide statistical result.

- Agent: Codex GPT-5.6 Sol, strict blackbox, development replicate 424.
- Task: Obstruction2D, episode seed 18 (two obstructions).
- Before: `c1c4586`.
- After: `e97a537`.
- Transcript window: `stream.jsonl` lines 338–349; extend only if a reference cannot be understood locally.
- The replicate seed identifies the development run; seed 18 identifies the policy test instance.

## Verified starting evidence

A fresh read of the archive on 2026-10-03 confirmed that the policy diff changes one block in reset(): before, a crowded target is placed ahead of the obstruction list; after, the target (when crowded) and obstructions are sorted by a computed top-edge-height key, descending. Final target placement remains the last task.

Transcript line 342 records the before version failing seed 18 at 1,000 steps. Line 344 records a diagnostic rollout with controller phase and object positions. Line 348 records the after version succeeding in 436 steps. These are historical observations, not newly reproduced results. They do not establish that every benefit follows from correct physical interpretation of the sorting key, nor do they reveal a complete internal reasoning process.

## First session: an archive-only micro-study

1. Extract the two approach.py versions, their diff, and the short transcript window into an isolated case folder. Preserve original paths, hashes, line numbers, and tool-call IDs. Do not execute historical shell commands.
2. Read the diff by hand. State the implemented before/after rule in one sentence each.
3. Annotate only observable coding-agent actions in the window using the pinned ACT*ONOMY codebook. Start at action/subaction level; use a leaf only when justified. Each label needs an exact evidence span, actor/source, and confidence or ambiguity note. Tool output is feedback available to the agent; it is not itself evidence that the agent reflected or evaluated.
4. Make a small timeline: event, ACT*ONOMY label, code consequence, observed result. Distinguish proposed changes from executed edits and reported success from tool-recorded success. Leave unobserved deliberation unknown.
5. Write a short conclusion identifying what is supported about the development decision, and what remains unsupported about its motivation or causal effect.

Suggested effort: one focused sitting of roughly 1–2 hours, excluding environment setup. Human review of this one case is the core research work; no batch annotation or new model calls are required.

## Smallest replay experiment

Once the historical environment version can be matched, run exactly two policy rollouts: before and after, both on seed 18 under the same 1,000-step limit and timeout. Save and compare the initial observations; seed equality alone is insufficient across environment versions. Record initial task order, objects grasped/moved, controller phases, solved status, and steps. Use copied policies and write all output outside the archive.

Prediction: the revisions produce different task orders, and the later order reproduces the archived success where the earlier one fails. Because the inspected policy diff is restricted to ordering, matched deterministic replays would provide a local intervention test. If outcomes differ from the archive, investigate version/state/nondeterminism before interpreting the policy effect. Two rollouts are a reproduction check, not a success-rate estimate.

## Deliverable and stopping rule

Produce one small evidence packet and a one-page finding. A reader must be able to trace every label and mechanism claim to a quoted event or code diff. The pilot succeeds methodologically even if some labels remain ambiguous or replay fails to reproduce; those are findings to document. Stop after this case. Do not add agents, tasks, more seeds, world-model classification, or the full archive until the annotation and evidence rules are understandable and useful.

## Source location

Archive run:
`/Users/zahra.bashir/.cache/robocode-results-viewer/1sNuRoRxMxh7_VDE93hWn_ZNHBd74Uzt2/runs/Blackbox/Codex GPT5.6 Sol/kinematic2d/obstruction2d_generalized__agentic__none__blackbox__strict__codex_gpt56sol__timeout_60s__99b3a73f/2026-09-08_22-07-59/replicate_424`

Primary files: `stream.jsonl`, `sandbox/.git` (read-only git show/diff), `sandbox/test_approach.py` at the relevant revisions, and `.hydra/config.yaml`. Final aggregate results.json is context, not the outcome of this historical two-version comparison.

Taxonomy paper: [How to Interpret Agent Behavior](https://arxiv.org/html/2605.13625v1). Previously identified upstream revision to use for codebook pinning: `0527a10dbd7363d80dce56a8b558f34946d2ddfd` in [gaojie058/Act-onomy](https://github.com/gaojie058/Act-onomy). Codebook availability must be verified before assigning labels.
