# Planning-approach table — all 35 runs

Draft v2, 2026-10-16. One row per development run. Labels come from reading the first substantive and final `approach.py` plus the commits where a label changed; every row was then re-verified against code, diffs and timeline events. Quotes are exact agent messages (E-IDs refer to each run's `01_timeline.md`). Labels are descriptive working labels, **not formal ACT\*ONOMY annotations**.

## Labels

**Task planner** — how the policy decides what to do next.
- **Fixed** — order not driven by the current scene: hard-coded phases, list/name order, or a sort done once at reset.
- **Greedy** — re-scores candidates against the current scene and picks the best *next* task (pairing two rovers to one task each still counts as Greedy).
- **Search** — plans an ordering of *several* tasks ahead (BFS, DP over subsets, DFS over orders, multi-push look-ahead), and that plan drives the returned action.

**Motion planner** — how the robot gets there.
- **Reactive** — per-step local rule (steering, feedback), no path search.
- **Scripted** — fixed motion recipe with computed offsets (lift → over → descend).
- **Geometric** — search over alternative paths (A\*, Dijkstra, grid BFS, candidate-path or base-pose search with collision checks). A single straight-line collision check is *not* Geometric; it is noted as "+ checked shortcut".
- **Model-based** — multi-step rollout of a predicted dynamics model to choose actions.

**Structure** — every final policy has separate task and motion layers (several *first* versions are purely Reactive).
- **Link** — what the task layer knows about motion: `none` · `after-fail` (re-chooses after a motion/grasp failure) · `grasp` (grasp feasibility checked before choosing) · `path` (path cost/feasibility or simulated execution before choosing) · `joint` (one search over task order and motion together). "from Cxxx" marks links added mid-run.
- **TAMP?** (provisional rule) — **TAMP** if the link includes `path` or `joint`; otherwise **TAMP-like**.

**Process columns**
- *First* — first substantive policy (placeholder/zero-action stubs skipped).
- *Tried, not adopted* — an approach with a **different** label built and tested but not kept. Same-label variants are noted in parentheses.
- *Switches* — commits where the main `approach.py` changed label.
- *Stated reason* — the agent's visible reason. Messages that only *report* a change after the commit are marked "(after)".
- *Decided by* — how each switch / rejection was decided:
  - **side-by-side** — same seeds, only this change differs (n given)
  - **before/after** — many seeds, but sequential, against an old saved run, or bundled with other changes
  - **debugging one case** — change came from tracing 1–2 failing seeds
  - **no visible test** — committed without any test that could compare
  - **initial design** — present from the first version

Models: **Claude** = Claude Opus 5.5 (high) · **Astra** = GPT-6 Astra (high) · **GPT-5.6** = GPT-5.6-sol (medium).

---

## Rovers

| Run | TAMP? | Link | Task | Motion | First | Tried, not adopted | Switches | Stated reason | Decided by |
|---|---|---|---|---|---|---|---|---|---|
| [Claude 24](environments/Rovers/runs/claude_opus55_high_r24_1cd6a7a5/03_findings.md) | TAMP | joint + replan | Search | Geometric | C002: Search / Geometric | — | none (C013 replaced the subset-DP planner with a time-expanded joint BFS built C008–C012; same labels) | E0943 "Seeds 0–47 now average 21.52 steps against 22.08 for approach.py, with no failures." | initial design; C013 rewrite: before/after (n=48, saved baseline E0850, bundled with C009–C012) |
| [Claude 42](environments/Rovers/runs/claude_opus55_high_r42_181ed19d/03_findings.md) | TAMP | joint (no task replan) | Search | Geometric | C002: Search / Geometric | — | none | none for architecture (E0772 "Plan estimates match actual totals (1356 vs 1361)") | initial design |
| [Claude 222](environments/Rovers/runs/claude_opus55_high_r222_c6c9dc31/03_findings.md) | TAMP | joint + replan | Search | Geometric | C002: Search / Geometric | — (camera-heading DP C016/C017, reverted C018; same label) | none | E1466 "The working version gained only 0.045 steps and roughly doubled planning time, so I dropped it." (same-label tweak; time from batch max only) | initial design; heading revert: before/after (n=400, saved baseline E0981 vs E1208) |
| [Claude 424](environments/Rovers/runs/claude_opus55_high_r424_4c49acd0/03_findings.md) | TAMP | joint + simulated rollouts | Search | Geometric | C002: Search / Geometric | — (topk, grid, heading variants; same label) | none (C003 simulator ranking, C008 layered DP; same labels) | C003: E0609 "adding an internal simulator so the planner can score candidate plans by simulated step count" | initial design; C003: debugging one case (seed 10, E0551/E0553) |
| [Claude 444](environments/Rovers/runs/claude_opus55_high_r444_2af61ade/03_findings.md) | TAMP | joint + replan | Search | Geometric | C006: Search / Geometric | — (mixed headings C019, reverted C020; same label) | none | none for architecture; E1019 "Mixed headings didn't help (and doubled planning time)" is a same-label tweak | initial design; heading revert: side-by-side (n=120, E0988 vs E1014; time claim untested) |
| [Astra 24](environments/Rovers/runs/codex_gpt6astra_r24_10c7bc43/03_findings.md) | TAMP | path (route cost in score) | **Greedy** | Geometric | C007: Greedy / Geometric | **Search** C036 (26.47 vs 26.60 steps, E0132), C038 (26.83 vs 26.60, n=30, E0141) | none | E0145 "The simpler scheduler performed best overall, so it remains in `approach.py`." | initial design; Search rejection: before/after (n=30, baseline read from saved results, not re-run) |
| [Astra 424](environments/Rovers/runs/codex_gpt6astra_r424_657f1d25/03_findings.md) | TAMP | path + after-fail | **Search** (greedy fallback) | Geometric | C004: Greedy / Geometric | — | **C019 Greedy → Search**; C022 re-assignment on route failure | E0072 "testing whether assigning complete task sequences… reduces completion time"; same seeds after commit: 99/100, 25.22 on successes vs greedy 100/100, 26.41 (E0109/E0110/E0114) | C019: no visible test at commit (E0091), then side-by-side (n=100, `--no-plan` flag); C022: debugging one case (seed 89) |
| [GPT-5.6 24](environments/Rovers/runs/codex_gpt56sol_r24_de120909/03_findings.md) | TAMP-like | none (Euclidean) | Fixed | Geometric (A\*) | C002: Fixed / Geometric | — | none | none for architecture | initial design |
| [GPT-5.6 424](environments/Rovers/runs/codex_gpt56sol_r424_0dc2ee42/03_findings.md) | TAMP-like | none | Fixed | Geometric (A\*) | C012: Fixed / Geometric | — (Chebyshev A\* C041, reverted C042; same label) | none | E0265 "Chebyshev A* made actual continuous routes worse, so I kept the empirically shorter Euclidean planner" | initial design; A\* revert: debugging (3 seeds, bundled) |

## Obstruction2D

| Run | TAMP? | Link | Task | Motion | First | Tried, not adopted | Switches | Stated reason | Decided by |
|---|---|---|---|---|---|---|---|---|---|
| [Claude 24](environments/Obstruction2D/runs/claude_opus55_high_r24_f8729873/03_findings.md) | TAMP | path (parking spots ranked by DP path cost) + grasp + after-fail | Greedy | Geometric (DP grid; C006 template kept as fallback) | C002: Greedy / Scripted | — (tallest-first → nearest-first order C008, n=40; 3D cost estimator C012, disabled: same labels) | **C007 Scripted → Geometric** (C006 only picks the lowest collision-free height for two fixed shapes — borderline, kept as Scripted) | E0258 (after C007) "Small improvement (59 → 57.6), but seeds 1 and 11 got worse."; E0543 "No gain from 3D cost estimates and far slower — disabling it." (same-label) | C007: debugging (seed 3, E0246) → before/after (n=12, same seeds, bundled); 3D cost rejection: side-by-side (n=40, E0541) |
| [Claude 42](environments/Obstruction2D/runs/claude_opus55_high_r42_820cc0f3/03_findings.md) | TAMP-like | grasp (C003) + after-fail (C007) | Greedy | Geometric (cheapest collision-free candidate polyline) | C002: Greedy / Scripted | — | **C004 Scripted → Geometric** | none before; E0148 (after C004+C005) "Now 43 steps avg on default seeds (was 64)" | debugging one case (seed 15, E0129/E0132); later before/after (n=200, bundled with C005, old C003 baseline) |
| [Claude 222](environments/Obstruction2D/runs/claude_opus55_high_r222_c7b08ad0/03_findings.md) | TAMP | path (simulated controller, from C005–C007) + grasp (from C010) + after-fail | Greedy | Reactive (clearance steering) | C002: Greedy / Reactive | — | none | none visible | initial design |
| [Claude 424](environments/Obstruction2D/runs/claude_opus55_high_r424_b71e4671/03_findings.md) | TAMP | path (cost estimate from C004; simulated controller from C010) | **Search** | Reactive (clearance steering) | C002: Greedy / Scripted | — | **C004 Greedy → Search + Scripted → Reactive** (one commit) | none before C004; E0227 (after) "Big step-count win (35 vs 116 mean) but 11 failures" — different seed sets, 29/40 solved; C010: E0476 "pick the cheapest by simulating the controller offline" | C004: no visible test; C010: debugging one case (seed 0, E0487) |
| [Claude 444](environments/Obstruction2D/runs/claude_opus55_high_r444_0b82e686/03_findings.md) | TAMP | path (analytic step-cost rollout: drop spots C009, whole order C011) + grasp (C006) | **Search** | Reactive (clearance steering) | C002: Greedy / Scripted | — | **C004 Scripted → Reactive; C011 Greedy → Search** | C004: none before (E0098 after, 1 seed: "Seed 0 now takes 50 steps instead of about 104"); C011: E0369 "The overhead is in obstruction handling…" | C004: debugging (seeds 31/74/21) → before/after (n=100, bundled); C011: debugging (seeds 5/12) → before/after (n=100, 33.0 → 32.3, bundled with staging) |
| [Astra 24](environments/Obstruction2D/runs/codex_gpt6astra_r24_29375d55/03_findings.md) | TAMP-like | grasp (from C005) | Greedy | Scripted | C003: Greedy / Scripted | — | none | none for labels (E0082 describes the C012 dependency fix, same label) | initial design |
| [Astra 424](environments/Obstruction2D/runs/codex_gpt6astra_r424_51fd524e/03_findings.md) | TAMP-like | grasp (from C024) | Greedy | Scripted | C011: Greedy / Scripted | — | none | none for labels (E0120 = C032 storage refinement) | initial design |
| [GPT-5.6 424](environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614/03_findings.md) | TAMP-like | after-fail (weak) | Fixed | Scripted | C002: Fixed / Reactive (never evaluated) | — (push-with-base idea probed only; high-carry variant rolled back C031, same label) | **C004 Reactive → Scripted** (task Fixed throughout) | E0035 (before) "vacuum lifting works reliably on the purple target block, but not on the red obstructions. I'm switching the controller design accordingly…" | C004: debugging one case (probes; committed after 1 seed, 0/1, E0079) |

## Obstruction3D

| Run | TAMP? | Link | Task | Motion | First | Tried, not adopted | Switches | Stated reason | Decided by |
|---|---|---|---|---|---|---|---|---|---|
| [Claude 24](environments/Obstruction3D/runs/claude_opus55_high_r24_024d0ca5/03_findings.md) | TAMP-like | grasp + after-fail | Greedy | Scripted (+ checked corner-cut C016; whole-body IK) | C003: Fixed / Scripted | — | **C013 Fixed → Greedy** (bundled with grasp-height candidates) | E0598 "most failures get stuck in to_grasp"; E0634 (after) "Seed 12 now succeeds" | debugging one case (seed 12, E0598–E0632); then 5/7 on earlier failures, no side-by-side |
| [Claude 42](environments/Obstruction3D/runs/claude_opus55_high_r42_820c1113/03_findings.md) | TAMP-like | grasp + after-fail | Greedy | Scripted (+ clearance-checked diagonal routing C014) | C003: Greedy / Scripted | — (travel-weighted parking C018, reverted C019: 24.4 vs 23.6, E1189; same label) | none | E1249 "If a gripper is blocked by a neighbour, that neighbour is moved first." | initial design |
| [Claude 222](environments/Obstruction3D/runs/claude_opus55_high_r222_f6aa665e/03_findings.md) | TAMP-like | grasp + after-fail | Greedy | Scripted (+ checked joint-space shortcut C015; base-pose search C018) | C003: Greedy / Scripted | — | none (C015/C018/C020 motion additions) | E1706 "long moves take 1–3 steps instead of 4–9" (describes C020) | initial design; C015: before/after (n=40, 34.575 → 34.325); C018: debugging (seed 2) → before/after (n=40, 33.5 → 25.9) |
| [Claude 424](environments/Obstruction3D/runs/claude_opus55_high_r424_3f9182d7/03_findings.md) | TAMP-like | grasp + after-fail | Greedy | Scripted | C002: Fixed / Scripted | — (accessibility score + aligned grasps + grasp depth C010–C012, reverted C013; same label) | **C003 Fixed → Greedy** (tallest first) | C013 revert: E0648 "Worse: 10/16 with 4 obstructions, and compute is up to 31 s."; C016 failure penalty: E0802 | C003: no visible test; C010–C012: debugging (seed 0) → before/after (16 seeds, bundled: 14/16 → 10/16); C016: debugging one case (seed 15) |
| [Claude 444](environments/Obstruction3D/runs/claude_opus55_high_r444_4a56791c/03_findings.md) | TAMP-like | grasp + after-fail | Greedy | Scripted | C003: Greedy / Scripted | — | none | none for labels (E1165 explains the C024 base move) | initial design |
| [Astra 24](environments/Obstruction3D/runs/codex_gpt6astra_r24_512c8dbf/03_findings.md) | TAMP-like | after-fail | Fixed | Scripted | C018: Fixed / Scripted (target only; obstruction height sort from C026) | — | none (C042 adds postponement) | E0162 "postpones a surrounded block and clears accessible neighbors first" | initial design; C042: debugging one case (20-obstruction seed 1) |
| [Astra 424](environments/Obstruction3D/runs/codex_gpt6astra_r424_cf2d0159/03_findings.md) | TAMP-like | after-fail | Fixed | Scripted | C007: Fixed / Scripted (target only; obstruction height sort from C031) | — | none (C052 adds postponement) | C052 title "Postpone enclosed obstructions until surrounding blocks are cleared"; E0157 "an enclosed obstruction requiring alternate grasp points or ordering" | initial design; C052: debugging one case (seed 8), no test of C052 itself |
| [GPT-5.6 24](environments/Obstruction3D/runs/codex_gpt56sol_r24_065956b8/03_findings.md) | TAMP-like | after-fail | Fixed (name order + defer on failure) | Scripted | C010: Fixed / Scripted | — (height-order sort key C035–C052, back to name C053; same label) | none | none in messages; C053 title "Use stable obstruction order with deferred retries"; test right after C053 failed seeds 0 and 5 (E0255) | initial design; C035/C053: debugging, no comparison |
| [GPT-5.6 424](environments/Obstruction3D/runs/codex_gpt56sol_r424_9332a06b/03_findings.md) | TAMP-like | none | Fixed | Scripted (+ Jacobian servo) | C006: Fixed / Scripted (target only; name sort C020 → height sort C023) | — | none | E0301 "clear them in height order" | initial design; C023: debugging (seeds 3/0) |

## DynPushT2D

Task = which push (contact, direction, length); motion = navigating to the contact and executing the push.

| Run | TAMP? | Link | Task | Motion | First | Tried, not adopted | Switches | Stated reason | Decided by |
|---|---|---|---|---|---|---|---|---|---|
| [Claude 24](environments/DynPushT2D/runs/claude_opus55_high_r24_55605190/03_findings.md) | TAMP | path | **Search** (2-push, top-8; off after 25 s) | Model-based + Geometric | C002: Greedy / Model-based + Geometric | — (LOOK=14, same label) | **C013 Greedy → Search** | no message; E0502 (before C013): look-ahead 0/4/8 → 159.1/145.9/143.0 steps, 96/96 each | side-by-side (n=96, only look-ahead varied) |
| [Claude 42](environments/DynPushT2D/runs/claude_opus55_high_r42_39564662/03_findings.md) | TAMP | path | **Search** (2-push, top-16; off after 25 s) | Model-based + Geometric | C002: Greedy / Model-based + Geometric | — | **C005 Greedy → Search** | E0347 "The approach is robust, so next I'll work on step efficiency"; E0365 "Lookahead cuts the average from about 128 to 117 steps" | side-by-side (n=100, look-ahead 0 vs 8, E0363) |
| [Claude 222](environments/DynPushT2D/runs/claude_opus55_high_r222_2702c656/03_findings.md) | TAMP | path + after-fail | **Search** (2-push C021; rotation look-ahead C023; stall guard flips it off/on C025) | Geometric + Reactive (analytic push model, no rollout) | C002: Greedy / Geometric + Reactive | — | **C021 Greedy → Search** | E0652 "Compute is negligible… That leaves room for more planning, so I'm re-profiling where the steps go."; first lost (E0669 "186.5 steps against 167.4 without it"), seed-1010 fix C022, then won 158.9 vs 167.4 (E0687) | side-by-side (n=80) — lost, debugging one case (seed 1010), side-by-side again (n=80) won |
| [Claude 424](environments/DynPushT2D/runs/claude_opus55_high_r424_2a46a52d/03_findings.md) | TAMP | path (soft, from C006) | **Search** (2-push, top-15; shrinks after 20 s, off after 30 s) | Model-based + Geometric | C002: Greedy / Model-based + Geometric (A\*) | — (look-ahead width 30, same label) | **C005 Greedy → Search** | E0257 "The two-push lookahead cuts the average from 139 to 127 steps" | side-by-side (n=60, look-ahead on vs off, E0255) |
| [Claude 444](environments/DynPushT2D/runs/claude_opus55_high_r444_2bf26d60/03_findings.md) | TAMP | path (from C012) + after-fail (from C018) | **Greedy** | Model-based + Geometric | C002: Greedy / Model-based + Geometric | **Search** C010 (58/60, 177.7 vs 147.7 steps, max 42.7 s, E0512); retested E0544, E0777 | C010 Greedy → Search, **C011 back to Greedy** | E0514 "Lookahead hurts (and is slow); disabling it (M=0)."; E0779 "Lookahead still doesn't help; leaving M=0." | side-by-side (n=60, E0512); retests before/after (n=60) |
| [Astra 24](environments/DynPushT2D/runs/codex_gpt6astra_r24_644304ab/03_findings.md) | TAMP-like | after-fail (weak, from C017) | Greedy | Geometric + Reactive (one-step model) | C002: Reactive | — | **C006 Reactive → Greedy / Geometric** | E0025 (after) "The policy now selects a surface point to push and routes the robot around the block."; before: E0019 "feedback control looks promising" | no visible test (probe-driven; 0/3 before, 0/5 after) |
| [Astra 424](environments/DynPushT2D/runs/codex_gpt6astra_r424_4e86deee/03_findings.md) | TAMP | path (route exists, from C016) + after-fail | Greedy | Geometric + Reactive (one-step model) | C005: Reactive (never run) | — | **C008 Reactive → Greedy / Geometric**; C016 adds route-existence filter | C008: E0024 "I'm using that geometry to choose contact points and route the robot around the block."; C016: E0061 "unreachable contacts behind wall-bound blocks" | C008: no visible test (0/5 after); C016: debugging failing seeds (9/160) |
| [GPT-5.6 24](environments/DynPushT2D/runs/codex_gpt56sol_r24_cee4702f/03_findings.md) | TAMP-like | none | Fixed | Geometric (A\*) + Scripted | C002: Reactive | — | **C013 Reactive → Fixed / Scripted; C023 → Geometric** | E0018 (leaving the baseline) "The naïve center-push baseline translates poorly… so I'm switching to contact-aware manipulation." | C013: no visible test (0/5 before and after); C023: debugging one case (seed 0) |
| [GPT-5.6 424](environments/DynPushT2D/runs/codex_gpt56sol_r424_7e89c88a/03_findings.md) | TAMP-like | none | Fixed | Geometric (A\*) + Scripted | C002: Reactive | — | **C018 Reactive → Fixed / Geometric + Scripted** (one commit) | E0043 "I'm replacing the heuristic with an explicit controller that rotates using symmetric push pairs, translates through calculated zero-torque contact lines, and routes around the actual T geometry." | no visible test (probe-driven; 1/5 after) |

---

## Summary

**Final task planner (35 runs)**

| | Fixed | Greedy | Search |
|---|---:|---:|---:|
| Rovers | 2 (GPT-5.6) | 1 (Astra) | 6 (Claude ×5, Astra) |
| Obstruction2D | 1 (GPT-5.6) | 5 (Claude ×3, Astra ×2) | 2 (Claude) |
| Obstruction3D | 4 (GPT-5.6 ×2, Astra ×2) | 5 (Claude ×5) | 0 |
| DynPushT2D | 2 (GPT-5.6) | 3 (Claude, Astra ×2) | 4 (Claude) |
| **Total** | **9** | **14** | **12** |

**How task-level decisions were made** (switches and rejected alternatives that change the task label)

| Decision | Run | Decided by |
|---|---|---|
| Greedy → Search | DynPush Claude 24, 42, 424 | side-by-side (n = 96, 100, 60) |
| Greedy → Search | DynPush Claude 222 | side-by-side (n=80), lost → debugged → won |
| Search rejected | DynPush Claude 444 | side-by-side (n=60) |
| Search rejected | Rovers Astra 24 | before/after (n=30, saved baseline) |
| Greedy → Search | Rovers Astra 424 | no visible test at commit; side-by-side afterwards (n=100) |
| Greedy → Search | Obstruction2D Claude 444 | debugging → before/after (n=100, bundled) |
| Greedy → Search | Obstruction2D Claude 424 | no visible test |
| Fixed → Greedy | Obstruction3D Claude 24 | debugging one case |
| Fixed → Greedy | Obstruction3D Claude 424 | no visible test |
| Reactive → staged policy | DynPush Astra 24, Astra 424, GPT-5.6 24, GPT-5.6 424 | no visible test |

**Patterns worth following up**
1. **Model family predicts task planner more than seed does.** GPT-5.6 is Fixed in every run (7/7); Claude is Greedy or Search (20/20), with Search in 12/20; Astra is mostly Greedy.
2. **Search depends on the environment.** Search appears in Rovers (6/9) and DynPushT2D (4/9) but never in Obstruction3D.
3. **Claude starts with Search in Rovers but adds it later elsewhere.** All five Claude Rovers runs search from the first version (initial design). In DynPushT2D and Obstruction2D, Claude adds Search after the policy already works, to cut steps (e.g. E0347 "The approach is robust, so next I'll work on step efficiency").
4. **Controlled comparisons happen when the alternative is a switchable flag.** Every side-by-side task decision is a look-ahead built as a parameter (LOOK, M, `--no-plan`) that can be set to 0. Rewrites and structural changes (Reactive → staged, Fixed → Greedy) are committed with no visible test or after debugging one seed.
5. **A-vs-B pairs (same model, same task, different outcome):**
   - **Rovers Astra 24 vs 424.** Both start Greedy and build Search. In 24 the gain was ~0.1 steps (noise) → rejected; in 424 it was ~1.2 steps on successful episodes → kept. Consistent with both following their evidence, though 424 committed before comparing.
   - **DynPush Claude 444 vs 222.** Look-ahead initially lost in both. 444 retested twice and dropped it; 222 traced the loss to one seed, fixed it, and look-ahead then won.
6. **Compute is cited, but rarely tested.** "doubled planning time" (Rovers Claude 222, 444) and "compute is up to 31 s" (Obstruction3D Claude 424) concern same-label tweaks, and none has a side-by-side timing measurement. The clearest compute-related task decision is DynPush Claude 444: "Lookahead hurts (and is slow)" — max 42.7 s vs 12.7 s per episode, alongside worse step counts. Several Search policies also cap look-ahead by elapsed time (DynPush Claude 24, 42, 424).
7. **Stated reasons are often written after the fact.** Several "reasons" are messages that report a result after the commit (e.g. Obstruction2D Claude 424 E0227, GPT-5.6 424 E0084). For the "why" question, only messages *before* a commit should count as reasons.

## Open decisions

1. **TAMP rule.** Provisional: TAMP needs path-level motion information before choosing (`path` or `joint`). Under this rule all of Obstruction3D is TAMP-like (grasp checks + retry after failure), and Rovers Astra 24 is TAMP because its greedy score uses Dijkstra route cost. If grasp-feasibility checks should count, most Claude Obstruction rows flip to TAMP. Sub-question: Obstruction2D Claude 24 and 222 rank *parking/placement spots* by path or rollout cost — counted as `path` here; if choosing a spot is not a task-level decision, both flip back to TAMP-like.
2. **Fixed vs Greedy for sorts.** Sorted once at reset or by name → Fixed; re-scored against the current scene at each choice → Greedy. GPT-5.6 Rovers 24 (fixed priority categories, nearest item inside) is borderline.
3. **Motion labels that fit poorly.** Claude Obstruction2D "clearance steering" (one-step, but looks ahead and is simulated for scoring); Astra DynPush one-step analytic contact model (no rollout); GPT-5.6 Obstruction3D Jacobian servo on fixed waypoints; Claude Obstruction2D 42 candidate-path search (a parameterized family of paths, not a map).
4. **Runtime-conditional search.** Several DynPush Search policies shrink or disable look-ahead after 20–30 s or after stalls; the label describes the default mode.

## Evidence limits

Labels come from parallel code/transcript reviews plus a second verification pass of every row (reviewers' cited E/C IDs were not all re-opened by hand). Claude thinking blocks are empty; reasons come only from visible messages. Some commits (e.g. Rovers Astra 24 C026/C027/C029) have no matching main-stream command. Seeds per model are unequal (Claude 5, Astra 2, GPT-5.6 1–2 per environment), and effort settings differ, so model comparisons are descriptive only.
