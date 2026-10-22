# Agent development logs — start here

**One environment → one development run → three reading documents.** Everything below uses the same organization. The original experiment archive is unchanged.

There are now **35 organized runs: seven Codex GPT-5.6-sol (medium effort), twenty Claude Opus 5.5 (high effort), and eight Codex GPT-6 Astra (high effort)**. Exact model names and effort settings come from saved configurations.

| Environment | GPT-5.6 seeds | Claude seeds | Astra seeds | Reading index |
| --- | --- | --- | --- | --- |
| Obstruction2D | 424 | 24, 42, 222, 424, 444 | 424, 24 | [Compare runs](environments/Obstruction2D/overview.md) |
| Obstruction3D | 424, 24 | 24, 42, 222, 424, 444 | 424, 24 | [Compare runs](environments/Obstruction3D/overview.md) |
| DynPushT2D | 424, 24 | 24, 42, 222, 424, 444 | 424, 24 | [Compare runs](environments/DynPushT2D/overview.md) |
| Rovers | 424, 24 | 24, 42, 222, 424, 444 | 424, 24 | [Compare runs](environments/Rovers/overview.md) |

These are development-run replicate seeds, not robot episode IDs. Claude now has **five seeds per environment**, adding 13 runs on 2026-10-11. Astra Obstruction2D 24 now has a Claude counterpart; GPT-5.6 still has only 424 there. The other models have not been expanded to five seeds.

## Investigating versus expanding tests

[Six-run failure-response frequencies](failure_response_frequency.md): completed failure batches in Obstruction2D and DynPushT2D, across GPT-5.6, Astra and Claude, all development replicate 424. Includes counts, a comparison plot and every included feedback → action sequence. Read this for frequencies; the earlier cross-run note contains selected examples.

[Cross-run failure follow-up check](failure_followup_review.md): a candidate screen of all 35 organized runs, with ten manually checked sequences in nine runs. Moving on while a failure remains unresolved recurs; returning, acknowledging it, and lacking later verification are kept separate. This is not a prevalence estimate.

The [Obstruction2D GPT-5.6-sol 424 feasibility study](environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614/03_findings.md#full-run-feasibility) now covers all 73 main-stream command batches containing completed policy-test results, including successful tests. It includes the full decision ledger, a descriptive plot, eight matched local policy replays, and a proposed experiment on whether a testing-capability reminder changes the response to an unresolved failure. This is one dependent development trajectory, not a cross-run causal result. The existing three-file reading structure is unchanged.

## Start with one Astra example

[Rovers 24 findings](environments/Rovers/runs/codex_gpt6astra_r24_10c7bc43/03_findings.md): try task-planning alternatives → compare → keep the simpler scheduler, while a repair from that investigation enters the retained controller. The final program alone would hide those alternatives.

[DynPushT2D 424 findings](environments/DynPushT2D/runs/codex_gpt6astra_r424_4e86deee/03_findings.md): an explicit local contact-response model chooses pushes, but no multi-push rollout was found. This helps separate “uses a model” from “looks several actions ahead.”


## Start with one Claude example

New: [DynPushT2D 444](environments/DynPushT2D/runs/claude_opus55_high_r444_2bf26d60/03_findings.md) tries deeper planning, disables it, and later reconsiders it. [Obstruction3D 222](environments/Obstruction3D/runs/claude_opus55_high_r222_f6aa665e/03_findings.md) combines previously separate motion stages after predicting a feasible joint trajectory.

[DynPushT2D 24 findings](environments/DynPushT2D/runs/claude_opus55_high_r24_55605190/03_findings.md) is a compact example of explicit two-push look-ahead, with a saved comparison of search widths. Its execution still separates navigation and pushing.

For a strategy replacement, read [Rovers 24 findings](environments/Rovers/runs/claude_opus55_high_r24_1cd6a7a5/03_findings.md): develop a second planner alongside the first → compare → adopt it while preserving the old code.

The familiar GPT [Obstruction2D 424 findings](environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614/03_findings.md) still contain seed 18, R37/R39 and the testing-expansion example. These are not additional runs.

## What to open in any run

- **01_timeline.md:** exact messages, actions and outputs in recorded order; helper actors are identified where present in the source stream.
- **02_code_changes.md:** every saved commit, original title, affected files, timeline links and expandable diffs with before/after line numbers.
- **03_findings.md:** evidence-backed interpretations, limitations and space for your notes. Existing notes are preserved by the extraction tool.
- **evidence/:** source copies, final code and helpers, saved versions, diffs, hashes and recoverable Git history. Open through the reading documents when needed.

[The shared protocol](protocol.md) explains identifiers, evidence standards and how to read one sequence. E0401 means raw stream line 401; Claude may add B01/B02 for separate blocks on one line. C IDs count saved commits; old GPT Obstruction2D R aliases remain available.

## Current inspection coverage

All twenty Claude runs have evidence-linked initial notes: the earlier seven have initial controller reviews, and the thirteen additions have **targeted planner/execution reviews and selected development-sequence checks**. Eight Astra runs retain their initial reviews. This is not exhaustive manual trace annotation or a complete code audit for the thirteen additions. Four GPT runs retain prior manual findings; three remain unreviewed.

The Claude cases show that staged execution can coexist with substantial planning. Obstruction2D varies from motion prediction to alternative task plans; DynPushT2D varies in predictive model and active search depth; all five Rovers cases contain task search. Obstruction3D uses kinematic models and can merge motion stages after checking a predicted trajectory. “Phases” therefore needs a more precise label: fixed task stages, planned action segments, and search-generated operator sequences should remain distinguishable.

The Astra cases add further distinctions: obstruction tasks use staged geometric/kinematic control; pushing uses local contact-response predictions; Rovers 424 retains task-order search, while Rovers 24 retains greedy task selection. Fixed phase machines, geometry-triggered modes and computed task schedules remain separate descriptions.

Task descriptions and checked experiment settings match within the documented same-replicate pairs. The thirteen added Claude runs match their existing Claude reference configuration except replicate seed and experiment identifier; the evaluation seed is unchanged. Additional seeds do not imply matching coverage in GPT/Astra. Effort settings differ (Claude and Astra high, GPT-5.6 medium), as do dates; software/backend equivalence is not established. No cross-model success rates or prevalence estimates are calculated. All thinking blocks in the twenty imported Claude streams have empty readable text; Astra main streams provide visible messages/tools without complete private reasoning; these notes use visible messages, tools, code and tests. Formal ACT*ONOMY labeling has not been performed.

## Preservation and maintenance

[Migration record](migration/README.md) · [Verification report](migration/verification.json) · [Run registry and matching settings](runs.json)

The backup retains all 577 pre-migration files. Their former locations have since been removed; this structure does not depend on those locations. Original backend-session/media trees remain in the source archive and are not exhaustively duplicated here.

Write research notes in **03_findings.md**. For a clearer timeline title, edit **evidence/annotations.json** and rebuild that run. Generated documents are protected against silently overwriting manual edits. Routine reading needs no commands.
