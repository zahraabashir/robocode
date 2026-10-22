# Migration record — updated 2026-10-11

[Start here](../README.md) · [Protocol](../protocol.md) · [Verification](verification.json)

The initial migration consolidated seven Codex development runs: four with prior manual findings and three unreviewed. A subsequent addition imported seven matching Claude Opus 5.5 High runs into the same structure, with initial controller reviews and selected trace checks. A third addition imported eight GPT-6 Astra High runs (replicates 424 and 24 in each of the four environments). A fourth addition on 2026-10-11 imported thirteen more Claude runs, bringing Claude to five seeds (24, 42, 222, 424, 444) per environment and the live registry to 35 runs. These additions have targeted controller/selected-sequence notes, not complete controller audits. Astra Obstruction2D 24 now has a same-replicate Claude counterpart; its coverage note was updated, while its scientific findings and the other existing findings were preserved. No archived code was executed; the older pilot inventories below remain historical snapshots.

## Preservation

[previous_analysis_2026-10-10.zip](previous_analysis_2026-10-10.zip) contains the exact 577 pre-migration files from the old analysis locations, excluding Finder metadata and Python bytecode caches. [legacy_inventory.json](legacy_inventory.json) records every original relative path, byte count and SHA-256. Extracting the backup recovers the old organization and original notes/scripts. The original project proposal is also available as [a readable copy](original_project_proposal.md).

The new run folders contain raw main transcripts, config/task descriptions, final Python files, saved policy snapshots, all-file commit diffs and complete saved-ref Git bundles. Instructions are historical text only. The old archive itself remains in its original location and has not been modified. Backend session trees and development render/video directories are not exhaustively copied into the new inspection folders; they remain in the original experiment archive, with its path in each manifest. Selected prior helper excerpts are preserved for Obstruction2D.

Prior selection, model/config matching and identity checks are retained in sample_manifest.json, identity_audit.json, inventory.json and comparison.json here. These are dated prior records, not a fresh full-dataset deduplication result. The new runs.json registry identifies the actual imported runs.

## Former locations preserved in the backup

These are the old items whose files are preserved in the backup. They are not required by the new reading documents or the new build tool:

- `agent_runs/obstruction2d_seed18/`
- `agent_runs/five_repair_sequences/`
- `agent_runs/run_424_sequence_map/`
- `agent_runs/diverse_environments_pilot/`
- `agent_runs/build_run_424_map.py`
- `agent_runs/prepare_five_repair_sequences.py`
- `agent_runs/minimal_project_proposal.md`

**Keep** `agent_runs/README.md`, `protocol.md`, `runs.json`, `environments/`, `tools/`, and `migration/`. The former locations listed above have since been removed; their 577 saved files remain recoverable from the verified backup. The current verification report checks that the live structure has no reading dependencies on those locations.

## Reproducibility

The new generator reads `runs.json`, each run's `evidence/annotations.json`, and the original archive. It does not import the old extraction scripts or depend on old folders. It preserves existing findings and refuses to overwrite manually changed generated documents.

Astra wrapper-export provenance is retained where available. Plain-text Codex launcher records are preserved without shifting raw-line event IDs. The Astra addition includes initial controller reviews and selected trace checks, not exhaustive annotation.

The verifier checks preserved file hashes, source copies, raw-event coverage, Git history and snapshots, internal document links, model identities, and absence of links to old reading folders. It restores each Git bundle into a temporary bare repository to check recoverability; it never runs a controller or checks out archived instructions.

The Claude expansion checked full fresh configurations against the existing Claude reference in each environment; differences are restricted to replicate seed and experiment identifier. All selected transcript hashes and recorded sessions were checked for reuse. Original outdated, rerun and reevaluation batches were not added. This is a selected-cohort identity check, not a fresh archive-wide deduplication. The historical pilot inventories remain unchanged.
