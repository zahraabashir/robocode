# Inspection protocol — version 4

Use one stable home for each development run. Read what the agent said and did before interpreting why. Keep the experiment archive unchanged.

## The three documents

1. **01_timeline.md — what happened?** A chronological table of messages, edits, commands, tests, coordination and session boundaries. Exact messages are printed below; commands and outputs are expandable. A shell call can contain several actions, so it can have multiple tags.
2. **02_code_changes.md — what changed?** Every saved commit in HEAD ancestry, original titles, linked timeline events, all affected files, and exact diffs with OLD/NEW line numbers. Policy snapshots provide context. Test-harness edits are included, not treated as controller edits.
3. **03_findings.md — what might it mean?** Human-owned findings and notes. Separate observed evidence, interpretation, alternatives and next checks. New research questions go here rather than into new folders.

`evidence/` is supporting material, not another reading assignment. It contains the task/config, raw transcript, final code, historical diffs and policy versions, a Git bundle, source hashes, and editable annotations. Historical instructions are stored as text data, not active AGENTS.md files.

## Start with one sequence

Read a message or test result → record your expectation of the next action → inspect the next events → open the corresponding diff → read the actual subsequent test output → write a finding only if something is worth investigating.

Do not start by reading every file in `evidence/`. For Obstruction2D, start with the linked examples in its findings document. Search the timeline for “Message,” “diagnostic/test edit,” “commit attempt,” or “test/probe candidate” to navigate.

## Identifiers and units

- **Run:** one generation/development lineage, not an episode, commit, or resumed turn. The manifest records exact source path, model, settings and hashes. Folder suffixes use the first eight characters of the transcript hash; the full hash is authoritative.
- **E0401:** original `stream.jsonl` line 401. Claude can append B01/B02 for individual content blocks on the same line. IDs intentionally have gaps. A completed tool item is shown once; its start line is retained to expose overlap. Unfinished items and unexpected record types remain visible. The exact raw stream retains every record.
- **C001:** first commit in the saved HEAD ancestry. Commit SHA, parents and recorded date are retained. A commit with only diagnostics still gets an ID. Git order is not necessarily the order in which asynchronous tools completed.
- **R01–R51:** older Obstruction2D policy-revision aliases preserved in the change guide. They do not count every commit; R01 is not the first-ever program.
- **F001:** a human finding within one run. A finding can link several events/commits and need not describe a repair.
- **Test condition:** seed + object-count setting + policy version + harness version + relevant limits. A seed by itself is insufficient.

Arrows mean “followed by.” They do not imply that the first event caused the next decision. When an event both commits and tests, preserve the command's order instead of inventing separate timestamps.

## Annotation rules

Automatic tags locate candidate evidence. They are not validated behavioral labels. A filename containing “test” is a clue, not proof of what the command did. A message preview is shortened; the exact message below is authoritative. Process exit zero does not mean every robot episode passed. Result previews quote available report lines without pooling batches.

Treat a commit title, code comment, or agent explanation as a claim to check against implementation and output. Link a commit to a transcript using its printed hash where available; a title appearing in a commit command is a weaker association and is marked as such. A current final file does not reconstruct an uncommitted intermediate edit. The change guide contains all tracked-file changes; missing intermediate content must stay unknown.

The generator does not automatically label every change “retained,” “reverted,” or “successful.” Identical controller hashes identify exact revisits; partial reversals and behavioral effects require inspection. A later test is not necessarily an isolated test of one change. Several parameters, the harness, or the tested cases may change together.

For each finding use:

- **Observed:** exact event/commit references and the narrow factual statement.
- **Interpretation:** a possible explanation, separated from observation.
- **Alternative:** another explanation or an important evidence gap.
- **Next check:** evidence or an intervention that would distinguish them.
- **Status:** open, supported observation, contradicted hypothesis, or uncertain interpretation.

Working behavioral categories include diagnosis, policy revision, diagnostic/test revision, coverage expansion, rollback, rewrite, validation, and stopping. These are descriptive categories, **not formal ACT*ONOMY labels**. A later taxonomy annotation should record the paper version, label definition, unit, evidence and reviewer separately.

## Controller mechanisms and coding-agent decisions are separate

Use code to assess persistent phase state, anticipatory constraints, one-step prediction, multi-step geometric search, dynamics rollout, and task-sequence search. Trace the output of any purported planner to returned actions. A function called “plan” is insufficient. Geometry assumptions can be inaccurate and still constitute a model used in search.

Use the development trace to assess explanations, chosen experiments, edits, reversals and stopping. A controller containing A* does not establish the coding agent's private internal reasoning. Real-environment testing during development is not a dynamics model inside the final controller. A feedback rule is not automatically model-free reinforcement learning. Phase structure and explicit planning can coexist. Record the kind of structure: a fixed phase machine, a queue of planned action segments, or a search-generated operator sequence. Do not assign an identical “phase-based” label merely because a program performs several task activities. “Look-ahead” can mean waypoint advancement, a future-pose clearance check, or a multi-action search; identify the actual computation and its influence on actions.

## Coverage, identity and uncertainty

The 35 organized records comprise seven Codex GPT-5.6-sol selections, twenty Claude Opus 5.5 High runs, and eight Codex GPT-6 Astra High runs. Claude has replicate seeds 24, 42, 222, 424 and 444 in each of the four environments. Four GPT runs have prior manual analysis; three await inspection. The earlier seven Claude and eight Astra runs have initial controller reviews; the thirteen Claude additions have targeted planner/execution, active-flag and selected development-sequence reviews. Read each finding's scope: no exhaustive developmental labeling or complete code audit is claimed for the additions. This is a purposive selection, not a population estimate. Astra Obstruction2D 24 now has a Claude counterpart, but no selected GPT-5.6 counterpart. The seed-18 packet and five-repair packet are excerpts of GPT Obstruction2D replicate 424, not additional runs.

The prior pilot's selection and identity audit are retained under `migration/`. Selected main transcript hashes are distinct and final policies match saved HEADs. This does not claim complete dataset deduplication. Before adding or aggregating a record, check original/rerun/outdated condition, `load_dir`, provenance, thread IDs, transcript reuse and generation lineage. A reevaluation can supply new outcomes without being a new generation. Identical code alone does not prove duplicate generation.

Codex timelines include recorded delegation calls but do not merge separate helper-session trees. Claude streams contain inline helper events; their timelines preserve those events and identify the parent tool/actor. Do not compare raw timeline row counts across providers as equal decision units. Selected Obstruction2D helper excerpts and its prior reasoning-availability audit are preserved as separate evidence. Backend reasoning coverage must be stated per run; missing/encrypted content is not reconstructed. Unknown and unreviewed cases are not negative labels.

Both Codex and Claude stream adapters are supported and verified. Claude requests/results are matched by session ID and tool-use ID, not proximity. Events are positioned at response lines, with request lines preserved to expose overlap. The turn/session column counts Claude session initializations, not model inference turns. Background launches are not finished experiments, and a tool result without a recorded exit code is not assigned exit zero. Empty thinking and routine progress remain in the raw stream, with an exhaustive block/record coverage ledger. All thinking blocks in these twenty Claude streams have empty readable text; this does not assert the content of every separate backend-session file.

The Claude selections are original Blackbox runs with `load_dir: null`, not Outdated or CodeX rerun batches. The original seven are paired by environment and replicate with an existing GPT selection; the thirteen additions extend within-Claude coverage. The original pairs have matching task-description bytes and checked environment/evaluation settings, including strict blackbox, no primitives, $20 generation budget, 100 evaluation tasks, max 1000 steps, 60-second evaluation timeout, and evaluation seed. Configured effort differs: Claude high versus GPT medium. Dates and potentially software/backend details differ. Unique transcripts and sessions within the selection do not replace archive-wide lineage deduplication. Pair settings and hashes are recorded in `runs.json` and rechecked by the verifier.

The thirteen Claude additions (2026-10-11) were checked against fresh source configurations, not folder labels. Within each environment, their complete saved configurations match Claude 424 except `replicate_seed` and, where present, `experiment_id`; all use evaluation seed 792075 and identical task text. Some seed-42 folder experiment identifiers differ from their actual configuration identifier, so the configuration is authoritative. Exactly five matching Claude seeds were identified per selected environment. All 35 selected main transcript hashes are distinct; the 34 registered session IDs are also distinct. The earlier GPT Obstruction2D 424 record has no registered session ID, so its identity check relies on transcript/code history and the retained prior audit. Final policies match saved HEADs. These checks exclude duplicate selected exports and reevaluations with `load_dir`, but do not establish full archive-wide independence. The shared evaluation seed means five generation replicates do not supply five independent evaluation benchmarks. No outcomes are pooled here.

The eight Astra selections are original strict Blackbox generations with `load_dir: null`; outdated batches, reruns and reevaluations were excluded from this addition. Seven match an existing GPT-5.6 environment/replicate, task text and checked settings. The eighth, Obstruction2D 24, initially used GPT Obstruction2D 424 only as a task/settings reference. Since the Claude expansion it uses Claude Obstruction2D 24 as its same-replicate task/settings reference, including evaluation seed; backend and container details still differ. Astra uses high reasoning effort. The registry preserves original export provenance for six wrapper exports; corresponding provenance/manifest files are copied into evidence. Identity checks distinguish the selected transcripts and thread IDs, not every generation in the full archive.

Some Codex exports begin with a plain-text launcher line. The importer preserves this as a non-JSON record with its original line number instead of discarding it or shifting subsequent E IDs. Completed items retain start lines; unfinished items remain visible. The eight Astra main streams do not expose complete private reasoning; their separate backend-session trees have not been exhaustively audited. Readable agent messages remain useful evidence but do not establish private deliberation.

## Editing and rebuilding

Write your own research notes in **03_findings.md**. Edit **evidence/annotations.json** to change a timeline title or add a structured commit description. Those descriptions should be clearly attributed to the analyst. Do not change copied source files to make them fit an interpretation.

`tools/build_inspection.py` generates the first two documents and evidence from `runs.json`. It preserves existing findings and refuses to overwrite a generated document that has been manually changed since its last build. There is no need to rerun the generator just to take notes.

```bash
python3 agent_runs/tools/build_inspection.py --run obstruction2d_generalized_replicate_424
python3 agent_runs/tools/verify_inspection.py
```

These tools read the archive and write only the analysis folder. They do not run saved commands, policies, simulators or instructions. A verified backup of all 577 pre-migration files is in `migration/previous_analysis_2026-10-10.zip`; the former reading locations have since been removed. The new reading documents do not depend on them.
