# DynPushT2D · gpt-5.6-sol · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `3a55000` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `64e2807` | Add baseline behind-object pushing policy and test harness | approach.py, probe_strategy.py, test_approach.py | [E0009](01_timeline.md#E0009) |
| [C003](#C003) · `30211d8` | add isolated reset and contact probing script | explore_geometry.py | No matched commit command/output |
| [C004](#C004) · `7cc31b7` | Respect robot Euclidean displacement limit | approach.py, probe_dynamics.py | [E0017](01_timeline.md#E0017) |
| [C005](#C005) · `937d66d` | Keep dynamics probes inside strict action norm | probe_dynamics.py | No matched commit command/output |
| [C006](#C006) · `0676090` | add isolated heuristic T-block strategy experiments | candidate_strategy.py, test_candidate_strategy.py | No matched commit command/output |
| [C007](#C007) · `0d015e9` | print failing candidate actions for strict harness debugging | test_candidate_strategy.py | No matched commit command/output |
| [C008](#C008) · `aec5753` | Report local-frame contact coordinates in dynamics probe | probe_dynamics.py | No matched commit command/output |
| [C009](#C009) · `139de84` | respect hidden radial action displacement limit | candidate_strategy.py | No matched commit command/output |
| [C010](#C010) · `587c5c3` | Use persistent staged contact for center pushes | approach.py, explore_geometry.py | [E0030](01_timeline.md#E0030) |
| [C011](#C011) · `6c18834` | log candidate trajectories for controller diagnosis | test_candidate_strategy.py | No matched commit command/output |
| [C012](#C012) · `a7d8ac7` | Probe tangential rotation control after contact | probe_dynamics.py | No matched commit command/output |
| [C013](#C013) · `8d291ba` | Add stem-tip rotation strokes and COM-aligned translation | approach.py | [E0034](01_timeline.md#E0034) |
| [C014](#C014) · `ac1accf` | shorten rotation bursts and handle arena-edge setup paths | candidate_strategy.py | No matched commit command/output |
| [C015](#C015) · `f6f942e` | Add concise mode trajectory diagnostics | test_approach.py | [E0038](01_timeline.md#E0038) |
| [C016](#C016) · `7c95c0c` | Interleave pose correction and keep staging targets reachable | approach.py, candidate_strategy.py | [E0042](01_timeline.md#E0042) |
| [C017](#C017) · `00a4150` | Select accessible T endpoint for rotation contacts | approach.py | [E0046](01_timeline.md#E0046) |
| [C018](#C018) · `149554c` | avoid accidental contact during polar staging | candidate_strategy.py | No matched commit command/output |
| [C019](#C019) · `f1d882c` | stage low-impulse rotation strokes directly at contact | candidate_strategy.py | No matched commit command/output |
| [C020](#C020) · `5f07c86` | Replace controller with bounded stem rotation and COM translation strokes | approach.py | [E0057](01_timeline.md#E0057) |
| [C021](#C021) · `2bd31ab` | Route translation setup around T geometry and clamp arena targets | approach.py | [E0061](01_timeline.md#E0061) |
| [C022](#C022) · `88b437b` | Allow translation strokes to reach the asymmetric outline | approach.py | [E0065](01_timeline.md#E0065) |
| [C023](#C023) · `3db79a0` | Add fast geometry-aware A-star contact navigation | approach.py | [E0069](01_timeline.md#E0069) |
| [C024](#C024) · `e1fedce` | Trace contact-navigation state transitions | test_approach.py | [E0073](01_timeline.md#E0073) |
| [C025](#C025) · `3bdeac4` | Increase trajectory sampling around navigation collisions | test_approach.py | [E0077](01_timeline.md#E0077) |
| [C026](#C026) · `d523a1c` | Abort and replan stale routes on accidental contact | approach.py | [E0081](01_timeline.md#E0081) |
| [C027](#C027) · `a91a6fd` | Maintain stable COM contact for efficient translation | approach.py | [E0085](01_timeline.md#E0085) |
| [C028](#C028) · `9e7ff36` | Release at target and correct angle wrap branch | approach.py | [E0092](01_timeline.md#E0092) |
| [C029](#C029) · `5bc8cf8` | Adapt rotation lever near boundaries and prevent diagonal corner cuts | approach.py | [E0100](01_timeline.md#E0100) |
| [C030](#C030) · `f6a9314` | Adapt translation contact line to cancel observed torque | approach.py | [E0106](01_timeline.md#E0106) |
| [C031](#C031) · `ba6c6b8` | Permit translation-first recovery near arena boundaries | approach.py | [E0112](01_timeline.md#E0112) |
| [C032](#C032) · `5cd4926` | Accelerate rotation strokes away from boundaries | approach.py | [E0118](01_timeline.md#E0118) |
| [C033](#C033) · `7c3e208` | Tune online torque cancellation and final orientation precision | approach.py | [E0124](01_timeline.md#E0124) |
| [C034](#C034) · `c03b231` | Restore stable conservative torque adaptation | approach.py | [E0128](01_timeline.md#E0128) |
| [C035](#C035) · `8091315` | Preserve contact room with earlier boundary recovery | approach.py | [E0134](01_timeline.md#E0134) |
| [C036](#C036) · `08cf5b1` | Use longer efficient rotation strokes in open space | approach.py | [E0142](01_timeline.md#E0142) |
| [C037](#C037) · `e070c50` | Balance open-space rotation speed and stability | approach.py | [E0146](01_timeline.md#E0146) |
| [C038](#C038) · `ea59351` | Favor reliable bounded rotation strokes across poses | approach.py | [E0152](01_timeline.md#E0152) |
| [C039](#C039) · `34dd135` | Adapt rotation stroke length in edge approach zones | approach.py | [E0158](01_timeline.md#E0158) |
| [C040](#C040) · `de55505` | Interleave recovery translation when rotation drifts away from goal | approach.py | [E0166](01_timeline.md#E0166) |
| [C041](#C041) · `afe60d7` | Prioritize final orientation once position is close | approach.py | [E0170](01_timeline.md#E0170) |
| [C042](#C042) · `c3d1145` | Clear forced translation after reaching positional target | approach.py | [E0176](01_timeline.md#E0176) |
| [C043](#C043) · `869a6eb` | Accelerate long-distance COM pushes while retaining precision | approach.py | [E0182](01_timeline.md#E0182) |
| [C044](#C044) · `451cb27` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C045](#C045) · `860fb75` | Learn contact offset from short torque-limited pushes | approach.py | [E0206](01_timeline.md#E0206) |
| [C046](#C046) · `3cdb148` | Limit short-stroke torque learning to final alignment | approach.py | [E0222](01_timeline.md#E0222) |
| [C047](#C047) · `88325fb` | Extend recovery pushes to amortize contact navigation | approach.py | [E0232](01_timeline.md#E0232) |
| [C048](#C048) · `fb12fbd` | Carry boundary recovery through a meaningful translation stroke | approach.py | [E0238](01_timeline.md#E0238) |
| [C049](#C049) · `c768c44` | Retreat straight backward to prevent destructive recontact | approach.py | [E0247](01_timeline.md#E0247) |
| [C050](#C050) · `c083d05` | Use cap-end torque when distal stem contact is crowded | approach.py | [E0263](01_timeline.md#E0263) |
| [C051](#C051) · `5edfcb4` | Restrict cap torque to favorable CCW wall cases | approach.py | [E0271](01_timeline.md#E0271) |
| [C052](#C052) · `b8dfac8` | Persist effective cap contact after CCW wall activation | approach.py | [E0277](01_timeline.md#E0277) |
| [C053](#C053) · `63c97a2` | Reuse activated cap contact for bidirectional corrections | approach.py | [E0283](01_timeline.md#E0283) |
| [C054](#C054) · `b3e226e` | Activate cap torque for CCW rotations near horizontal walls | approach.py | [E0291](01_timeline.md#E0291) |
| [C055](#C055) · `d1c4230` | Accelerate large residual rotations in open space | approach.py | [E0297](01_timeline.md#E0297) |
| [C056](#C056) · `39a5bcb` | Restore conservative rotation activation after held-out failures | approach.py | [E0305](01_timeline.md#E0305) |
| [C057](#C057) · `4abcf8e` | Choose rotation contact that also advances toward goal | approach.py | [E0314](01_timeline.md#E0314) |
| [C058](#C058) · `dc01eb9` | Switch torque contacts only for meaningful position progress | approach.py | [E0324](01_timeline.md#E0324) |
| [C059](#C059) · `7c40b65` | Tune rotation contact progress threshold | approach.py | [E0330](01_timeline.md#E0330) |
| [C060](#C060) · `e57d51f` | Restore best validated contact selection threshold | approach.py | [E0336](01_timeline.md#E0336) |
| [C061](#C061) · `ab1562e` | Increase final translation speed within safe release margin | approach.py | [E0342](01_timeline.md#E0342) |
| [C062](#C062) · `3db2f59` | Keep forced recovery displacement bounded | approach.py | [E0364](01_timeline.md#E0364) |
| [C063](#C063) · `8bd11df` | Amortize bounded recovery contact over useful distance | approach.py | [E0370](01_timeline.md#E0370) |
| [C064](#C064) · `c5ab694` | Use longer goal-directed recovery strokes | approach.py | [E0376](01_timeline.md#E0376) |
| [C065](#C065) · `47f8a11` | Use transformed T footprint for boundary recovery | approach.py | [E0382](01_timeline.md#E0382) |
| [C066](#C066) · `09d0ca9` | Restore validated center-based recovery thresholds | approach.py | [E0388](01_timeline.md#E0388) |
| [C067](#C067) · `3d77208` | Shorten straight retreat after contact separation | approach.py | [E0398](01_timeline.md#E0398) |
| [C068](#C068) · `98e64bb` | Use direct final contact setup near positional goal | approach.py | [E0404](01_timeline.md#E0404) |
| [C069](#C069) · `b7bbb82` | Continue useful incidental contact during translation setup | approach.py | [E0417](01_timeline.md#E0417) |
| [C070](#C070) · `4574f1b` | Limit incidental-contact continuation to final approach | approach.py | [E0423](01_timeline.md#E0423) |
| [C071](#C071) · `1edc02f` | Tighten opportunistic final-contact continuation | approach.py | [E0429](01_timeline.md#E0429) |
| [C072](#C072) · `c6a707e` | Remove unsafe incidental-contact continuation | approach.py | [E0435](01_timeline.md#E0435) |
| [C073](#C073) · `f76f178` | Use direct rotation setup at final position | approach.py | [E0447](01_timeline.md#E0447) |
| [C074](#C074) · `f20ffb6` | Restore planned final rotation approach | approach.py | [E0453](01_timeline.md#E0453) |
| [C075](#C075) · `1c7f100` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C076](#C076) · `1c8a0e6` | Align planned and runtime translation staging targets | approach.py | [E0468](01_timeline.md#E0468) |
| [C077](#C077) · `77f29bd` | Reverse immediately when translation stroke expires | approach.py | [E0476](01_timeline.md#E0476) |
| [C078](#C078) · `4063195` | Restore validated final stroke follow-through | approach.py | [E0482](01_timeline.md#E0482) |
| [C079](#C079) · `de2487e` | Begin rotation retreat without an extra torque step | approach.py | [E0488](01_timeline.md#E0488) |
| [C080](#C080) · `6aeb0f9` | Keep empirically validated rotation follow-through | approach.py | [E0494](01_timeline.md#E0494) |
| [C081](#C081) · `6923450` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C082](#C082) · `6766818` | Tighten direct final-contact shortcut | approach.py | [E0514](01_timeline.md#E0514) |
| [C083](#C083) · `4c017c7` | Restore validated final-contact distance | approach.py | [E0520](01_timeline.md#E0520) |
| [C084](#C084) · `5a4bc81` | Reduce unnecessary near-tolerance rotation cycles | approach.py | [E0524](01_timeline.md#E0524) |
| [C085](#C085) · `6bfc26e` | Restore conservative orientation correction threshold | approach.py | [E0530](01_timeline.md#E0530) |
| [C086](#C086) · `3891024` | Keep nontrivial obstacle routes during final approach | approach.py | [E0539](01_timeline.md#E0539) |
| [C087](#C087) · `37b79db` | Retain higher-scoring direct final approach | approach.py | [E0545](01_timeline.md#E0545) |
| [C088](#C088) · `97642a0` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C089](#C089) · `e848b3a` | Test direct late-stage rotation setup | approach.py | [E0569](01_timeline.md#E0569) |
| [C090](#C090) · `498959a` | Restore safe planned rotation setup | approach.py | [E0575](01_timeline.md#E0575) |
| [C091](#C091) · `6732cff` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C092](#C092) · `e206af9` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C093](#C093) · `d99bdea` | Test faster long-distance translation strokes | approach.py | [E0607](01_timeline.md#E0607) |
| [C094](#C094) · `90333d0` | Restore stable long-distance translation speed | approach.py | [E0615](01_timeline.md#E0615) |
| [C095](#C095) · `548345d` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C096](#C096) · `f6c33d6` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C097](#C097) · `3414e23` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C098](#C098) · `a54cb35` | Try slightly earlier direct final approach | approach.py | [E0663](01_timeline.md#E0663) |
| [C099](#C099) · `27c77f7` | Restore validated direct approach cutoff | approach.py | [E0670](01_timeline.md#E0670) |
| [C100](#C100) · `b123779` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C101](#C101) · `8d393fa` | Avoid marginal rotation cycles near episode horizon | approach.py | [E0687](01_timeline.md#E0687) |
| [C102](#C102) · `636532f` | Restore strict rotation threshold after horizon test | approach.py | [E0694](01_timeline.md#E0694) |
| [C103](#C103) · `98f39c0` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C104](#C104) · `2e6c143` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C105](#C105) · `93c6674` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C106](#C106) · `dbadd61` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C107](#C107) · `9d5823d` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C108](#C108) · `0f71f90` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C109](#C109) · `e2c1747` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C110](#C110) · `362deb8` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C111](#C111) · `47dea9d` | initial sandbox setup | AGENTS.md | No matched commit command/output |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `3a55000d50a578e4d66458a315fe18d7c656e83f`; parents: none (initial snapshot). Recorded author date: 2026-09-09T08:23:32+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_3a55000.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/.gitignore b/.gitignore
new file mode 100644
index 0000000..7963cd5
--- /dev/null
+++ b/.gitignore
@@ -0,0 +1,13 @@
           1 +__pycache__/
           2 +*.pyc
           3 +*.png
           4 +*.gif
           5 +*.jpg
           6 +*.jpeg
           7 +*.mp4
           8 +agent_log.txt
           9 +.mcp/
          10 +.agent_sessions/
          11 +.agent_home/
          12 +.agent_prompts/
          13 +mcp_renders/
diff --git a/AGENTS.md b/AGENTS.md
new file mode 100644
index 0000000..b034ec3
--- /dev/null
+++ b/AGENTS.md
@@ -0,0 +1,13 @@
           1 +You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
           2 +
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $20.00. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           4 +
           5 +Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
           6 +
           7 +All files you create MUST use relative paths so they stay in the current working directory (/sandbox). Never write files using absolute paths.
           8 +
           9 +CONTEXT MANAGEMENT: your context window is limited and you MUST protect it aggressively: (1) When running Bash commands, pipe output through `head` or `tail` to limit verbosity if possible. (2) Keep your thinking brief, do not write long reasoning traces. (3) Keep your main conversation focused on writing and testing code, not on reading source or reasoning at length.
          10 +
          11 +The Python interpreter is at /opt/robocode-strict/bin/python
          12 +Run test scripts with:
          13 +    /opt/robocode-strict/bin/python test_approach.py
diff --git a/env_client.py b/env_client.py
new file mode 100644
index 0000000..6923c9f
--- /dev/null
+++ b/env_client.py
@@ -0,0 +1,735 @@
           1 +"""Client for the black-box environment server.
           2 +
           3 +This file is copied into the agent sandbox. Import it in test and
           4 +exploration scripts to interact with the environment without access to its
           5 +source code::
           6 +
           7 +    from env_client import make_env
           8 +
           9 +    env = make_env()
          10 +    obs, info = env.reset(seed=0)
          11 +    obs, reward, terminated, truncated, info = env.step(action)
          12 +    state = env.get_state()
          13 +    env.set_state(state)
          14 +    primitives = env.make_primitives()  # same dict the eval harness passes
          15 +    env.close()
          16 +
          17 +Each call to ``make_env()`` creates a fresh, independent environment
          18 +instance on the server, so parallel test scripts are safe.
          19 +
          20 +The list above is the legacy blackbox interface. When ``env_spaces.json`` has
          21 +``"strict": true``, only reset, step, rendering, close, and generic space metadata
          22 +are supported; the host server rejects every other helper command independently.
          23 +
          24 +NOTE: ``approach.py`` must NOT import this module. It is evaluated by a
          25 +separate harness that calls it directly with real observations; this client
          26 +is only for test and exploration scripts.
          27 +
          28 +This module must stay importable with only the standard library and numpy.
          29 +"""
          30 +
          31 +from __future__ import annotations
          32 +
          33 +import importlib
          34 +import json
          35 +import socket
          36 +import sys
          37 +from pathlib import Path
          38 +from typing import Any
          39 +
          40 +import numpy as np
          41 +
          42 +_METADATA_PATH = Path(__file__).resolve().parent / "env_spaces.json"
          43 +_NDARRAY_TAG = "__ndarray__"
          44 +_HANDLE_TAG = "__handle__"
          45 +_MODULE_TAG = "__module__"
          46 +_SET_TAG = "__set__"
          47 +_OCS_TAG = "__ocs__"
          48 +
          49 +
          50 +# ---------------------------------------------------------------------------
          51 +# Local ObjectCentricState mirror
          52 +#
          53 +# A variable-count env hands the program an ObjectCentricState. This sandbox module
          54 +# must stay importable with only the standard library and numpy, so rather than import
          55 +# relational_structs it reconstructs a faithful local mirror from the self-contained
          56 +# codec payload (which embeds the type hierarchy). The mirror implements the subset of
          57 +# the ObjectCentricState API a generated program uses, with the same semantics -- most
          58 +# importantly `is_instance` over the ancestor chain and `get(obj, feature)` by name --
          59 +# so a program tested here behaves as it will at eval against the real state.
          60 +# ---------------------------------------------------------------------------
          61 +
          62 +
          63 +class _Type:
          64 +    """A local mirror of relational_structs.Type (name + optional parent)."""
          65 +
          66 +    def __init__(self, name: str, parent: "_Type | None" = None) -> None:
          67 +        self.name = name
          68 +        self.parent = parent
          69 +
          70 +    def get_ancestors(self) -> set["_Type"]:
          71 +        """Return this type and all of its ancestors (parents, grandparents, ...)."""
          72 +        ancestors: set[_Type] = set()
          73 +        cur: _Type | None = self
          74 +        while cur is not None:
          75 +            ancestors.add(cur)
          76 +            cur = cur.parent
          77 +        return ancestors
          78 +
          79 +    def __eq__(self, other: Any) -> bool:
          80 +        return isinstance(other, _Type) and other.name == self.name
          81 +
          82 +    def __hash__(self) -> int:
          83 +        return hash(self.name)
          84 +
          85 +    def __repr__(self) -> str:
          86 +        return f"Type({self.name})"
          87 +
          88 +
          89 +class _Object:
          90 +    """A local mirror of relational_structs.Object (name + type)."""
          91 +
          92 +    def __init__(self, name: str, typ: _Type) -> None:
          93 +        self.name = name
          94 +        self.type = typ
          95 +
          96 +    def is_instance(self, typ: _Type) -> bool:
          97 +        """True if this object's type is *typ* or a descendant of it."""
          98 +        return typ in self.type.get_ancestors()
          99 +
         100 +    def __eq__(self, other: Any) -> bool:
         101 +        return isinstance(other, _Object) and other.name == self.name
         102 +
         103 +    def __hash__(self) -> int:
         104 +        return hash(self.name)
         105 +
         106 +    def __repr__(self) -> str:
         107 +        return f"{self.name}:{self.type.name}"
         108 +
         109 +
         110 +class _ObjectCentricState:
         111 +    """A local mirror of relational_structs.ObjectCentricState.
         112 +
         113 +    Holds ``{Object: feature ndarray}`` as ``data`` plus ``{Type: [feature names]}`` as
         114 +    ``type_features`` (both public, matching the real state) and exposes the read/write
         115 +    API a program uses. Iteration yields the objects, sorted by name for determinism.
         116 +    """
         117 +
         118 +    def __init__(
         119 +        self,
         120 +        data: dict[_Object, np.ndarray],
         121 +        type_features: dict[_Type, list[str]],
         122 +    ) -> None:
         123 +        self.data = data
         124 +        self.type_features = type_features
         125 +
         126 +    def __iter__(self) -> Any:
         127 +        return iter(sorted(self.data, key=lambda o: o.name))
         128 +
         129 +    def get_object_names(self) -> set[str]:
         130 +        """The set of object names in this state."""
         131 +        return {o.name for o in self.data}
         132 +
         133 +    def get_object_from_name(self, name: str) -> _Object:
         134 +        """The object with the given name."""
         135 +        for obj in self.data:
         136 +            if obj.name == name:
         137 +                return obj
         138 +        raise ValueError(f"No object named {name!r}")
         139 +
         140 +    def get_objects(self, typ: _Type) -> list[_Object]:
         141 +        """Objects that are instances of *typ* (its subtypes included), by name."""
         142 +        return sorted(
         143 +            (o for o in self.data if o.is_instance(typ)), key=lambda o: o.name
         144 +        )
         145 +
         146 +    def _feature_index(self, obj: _Object, feature: str) -> int:
         147 +        return self.type_features[obj.type].index(feature)
         148 +
         149 +    def get(self, obj: _Object, feature: str) -> float:
         150 +        """Read a named feature of an object."""
         151 +        return float(self.data[obj][self._feature_index(obj, feature)])
         152 +
         153 +    def set(self, obj: _Object, feature: str, value: float) -> None:
         154 +        """Write a named feature of an object in place."""
         155 +        self.data[obj][self._feature_index(obj, feature)] = value
         156 +
         157 +    def vec(self, objects: Any) -> np.ndarray:
         158 +        """Concatenate the feature vectors of the given objects."""
         159 +        return (
         160 +            np.concatenate([self.data[o] for o in objects]) if objects else np.array([])
         161 +        )
         162 +
         163 +    def copy(self) -> "_ObjectCentricState":
         164 +        """A deep copy of this state."""
         165 +        return _ObjectCentricState(
         166 +            {o: arr.copy() for o, arr in self.data.items()},
         167 +            {t: list(f) for t, f in self.type_features.items()},
         168 +        )
         169 +
         170 +    def allclose(self, other: "_ObjectCentricState") -> bool:
         171 +        """True if *other* has the same objects with numerically-close features."""
         172 +        if self.get_object_names() != other.get_object_names():
         173 +            return False
         174 +        return all(
         175 +            np.allclose(self.data[o], other.data[other.get_object_from_name(o.name)])
         176 +            for o in self.data
         177 +        )
         178 +
         179 +
         180 +def _build_local_types(
         181 +    types_payload: list[dict[str, Any]],
         182 +) -> tuple[dict[str, _Type], dict[_Type, list[str]]]:
         183 +    """Rebuild local {name: _Type} and {_Type: [features]} (parents-first payload)."""
         184 +    type_by_name: dict[str, _Type] = {}
         185 +    type_features: dict[_Type, list[str]] = {}
         186 +    for entry in types_payload:
         187 +        parent = type_by_name[entry["parent"]] if entry["parent"] is not None else None
         188 +        typ = _Type(entry["name"], parent)
         189 +        type_by_name[entry["name"]] = typ
         190 +        type_features[typ] = list(entry["features"])
         191 +    return type_by_name, type_features
         192 +
         193 +
         194 +def _ocs_from_payload(payload: dict[str, Any]) -> _ObjectCentricState:
         195 +    """Reconstruct a local ObjectCentricState from a self-contained codec payload."""
         196 +    type_by_name, type_features = _build_local_types(payload["types"])
         197 +    data: dict[_Object, np.ndarray] = {}
         198 +    for entry in payload["objects"]:
         199 +        obj = _Object(entry["name"], type_by_name[entry["type"]])
         200 +        data[obj] = np.array(entry["features"], dtype=np.float32)
         201 +    return _ObjectCentricState(data, type_features)
         202 +
         203 +
         204 +def _ocs_to_payload(state: _ObjectCentricState) -> dict[str, Any]:
         205 +    """Encode a local ObjectCentricState back to the self-contained codec payload."""
         206 +
         207 +    def depth(t: _Type) -> int:
         208 +        n, p = 0, t.parent
         209 +        while p is not None:
         210 +            n, p = n + 1, p.parent
         211 +        return n
         212 +
         213 +    types = sorted(state.type_features, key=lambda t: (depth(t), t.name))
         214 +    return {
         215 +        "types": [
         216 +            {
         217 +                "name": t.name,
         218 +                "parent": t.parent.name if t.parent is not None else None,
         219 +                "features": list(state.type_features[t]),
         220 +            }
         221 +            for t in types
         222 +        ],
         223 +        "objects": [
         224 +            {
         225 +                "name": o.name,
         226 +                "type": o.type.name,
         227 +                "features": [float(v) for v in state.data[o]],
         228 +            }
         229 +            for o in sorted(state.data, key=lambda o: o.name)
         230 +        ],
         231 +    }
         232 +
         233 +
         234 +def _encode(obj: Any) -> Any:
         235 +    """Encode values as tagged JSON (mirrors robocode.utils.env_server)."""
         236 +    if isinstance(obj, _ObjectCentricState):
         237 +        return {_OCS_TAG: _ocs_to_payload(obj)}
         238 +    if isinstance(obj, np.generic):
         239 +        return obj.item()
         240 +    if isinstance(obj, np.ndarray):
         241 +        return {_NDARRAY_TAG: obj.tolist(), "dtype": str(obj.dtype)}
         242 +    if isinstance(obj, dict):
         243 +        return {key: _encode(value) for key, value in obj.items()}
         244 +    if isinstance(obj, (list, tuple)):
         245 +        return [_encode(value) for value in obj]
         246 +    return obj
         247 +
         248 +
         249 +def _decode(obj: Any) -> Any:
         250 +    """Decode tagged JSON (mirrors robocode.utils.env_server)."""
         251 +    if isinstance(obj, dict):
         252 +        if _OCS_TAG in obj:
         253 +            return _ocs_from_payload(obj[_OCS_TAG])
         254 +        if _NDARRAY_TAG in obj:
         255 +            return np.array(obj[_NDARRAY_TAG], dtype=np.dtype(obj["dtype"]))
         256 +        return {key: _decode(value) for key, value in obj.items()}
         257 +    if isinstance(obj, list):
         258 +        return [_decode(value) for value in obj]
         259 +    return obj
         260 +
         261 +
         262 +def _encode_ref(obj: Any) -> Any:
         263 +    """Encode args/targets for the remote-object proxy commands.
         264 +
         265 +    Same as ``_encode`` but ``_RemoteHandle`` objects serialize to their
         266 +    ``{"__handle__": id}`` token so the host resolves them from its registry.
         267 +    Used only by devectorize/vectorize/getattr/call requests.
         268 +    """
         269 +    if isinstance(obj, _RemoteHandle):
         270 +        return {_HANDLE_TAG: obj._handle_id}  # pylint: disable=protected-access
         271 +    if isinstance(obj, _ObjectCentricState):
         272 +        return {_OCS_TAG: _ocs_to_payload(obj)}
         273 +    if isinstance(obj, np.generic):
         274 +        return obj.item()
         275 +    if isinstance(obj, np.ndarray):
         276 +        return {_NDARRAY_TAG: obj.tolist(), "dtype": str(obj.dtype)}
         277 +    if isinstance(obj, dict):
         278 +        return {key: _encode_ref(value) for key, value in obj.items()}
         279 +    if isinstance(obj, (list, tuple)):
         280 +        return [_encode_ref(value) for value in obj]
         281 +    if isinstance(obj, (set, frozenset)):
         282 +        return {_SET_TAG: [_encode_ref(value) for value in obj]}
         283 +    return obj
         284 +
         285 +
         286 +class SpaceInfo:
         287 +    """Metadata for a Box space: shape, low, high, dtype, and sample()."""
         288 +
         289 +    def __init__(self, spec: dict[str, Any]) -> None:
         290 +        if spec["type"] != "Box":
         291 +            raise TypeError(
         292 +                f"Unsupported space type {spec['type']!r}; extend SpaceInfo "
         293 +                "alongside the server's serialize_space"
         294 +            )
         295 +        self.shape: tuple[int, ...] = tuple(spec["shape"])
         296 +        self.dtype: np.dtype[Any] = np.dtype(spec["dtype"])
         297 +        self.low: np.ndarray = np.array(spec["low"], dtype=self.dtype)
         298 +        self.high: np.ndarray = np.array(spec["high"], dtype=self.dtype)
         299 +
         300 +    def sample(self, rng: np.random.Generator | None = None) -> np.ndarray:
         301 +        """Sample uniformly between low and high."""
         302 +        if rng is None:
         303 +            rng = np.random.default_rng()
         304 +        return rng.uniform(self.low, self.high).astype(self.dtype)
         305 +
         306 +
         307 +class _RemoteHandle:
         308 +    """A reference to a host-side object, used over the env server.
         309 +
         310 +    Attribute access and calls are proxied to the host: ``handle.method(...)``
         311 +    issues a ``getattr`` (returning another handle for the bound method) then a
         312 +    ``call``. Returned values are decoded the same way as any response, so a
         313 +    scalar/ndarray comes back inline and another object comes back as a nested
         314 +    ``_RemoteHandle``. Private/dunder attributes are refused client-side, both
         315 +    to avoid surprise round-trips and to mirror the host security guard.
         316 +    """
         317 +
         318 +    def __init__(self, client: "BlackboxEnv", handle_id: str) -> None:
         319 +        # Use object.__setattr__-free plain assignment; __getattr__ only fires
         320 +        # for names not found normally, and these two are set here.
         321 +        self._client = client
         322 +        self._handle_id = handle_id
         323 +
         324 +    def __getattr__(self, name: str) -> Any:
         325 +        if name.startswith("_"):
         326 +            raise AttributeError(
         327 +                f"refusing private/dunder attribute access on remote handle: "
         328 +                f"{name!r}"
         329 +            )
         330 +        response = self._client._request(  # pylint: disable=protected-access
         331 +            {
         332 +                "cmd": "getattr",
         333 +                "target": {_HANDLE_TAG: self._handle_id},
         334 +                "name": name,
         335 +            }
         336 +        )
         337 +        return self._client._decode_ref(  # pylint: disable=protected-access
         338 +            response["result"]
         339 +        )
         340 +
         341 +    def __call__(self, *args: Any, **kwargs: Any) -> Any:
         342 +        response = self._client._request(  # pylint: disable=protected-access
         343 +            {
         344 +                "cmd": "call",
         345 +                "target": {_HANDLE_TAG: self._handle_id},
         346 +                "args": _encode_ref(list(args)),
         347 +                "kwargs": _encode_ref(kwargs),
         348 +            }
         349 +        )
         350 +        return self._client._decode_ref(  # pylint: disable=protected-access
         351 +            response["result"]
         352 +        )
         353 +
         354 +
         355 +class _RemoteModule:
         356 +    """A reference to a whitelisted host module (e.g. crv_motion_planning).
         357 +
         358 +    Attribute access proxies a ``getattr`` against the ``{"__module__": name}``
         359 +    target, so ``module.plan_crv_actions`` returns a callable handle the agent
         360 +    can invoke. Mirrors how a remote-module primitive is used at eval time,
         361 +    where ``primitives['crv_motion_planning']`` is the real module.
         362 +    """
         363 +
         364 +    def __init__(self, client: "BlackboxEnv", short_name: str) -> None:
         365 +        self._client = client
         366 +        self._short_name = short_name
         367 +
         368 +    def __getattr__(self, name: str) -> Any:
         369 +        if name.startswith("_"):
         370 +            raise AttributeError(
         371 +                f"refusing private/dunder attribute access on remote module: "
         372 +                f"{name!r}"
         373 +            )
         374 +        response = self._client._request(  # pylint: disable=protected-access
         375 +            {
         376 +                "cmd": "getattr",
         377 +                "target": {_MODULE_TAG: self._short_name},
         378 +                "name": name,
         379 +            }
         380 +        )
         381 +        return self._client._decode_ref(  # pylint: disable=protected-access
         382 +            response["result"]
         383 +        )
         384 +
         385 +
         386 +class _BlackboxObservationSpace(SpaceInfo):
         387 +    """Box-space metadata plus client-backed devectorize/vectorize.
         388 +
         389 +    Stands in for the eval-time ``ObjectCentricBoxSpace``: it keeps the
         390 +    shape/low/high/dtype/sample() of a plain ``SpaceInfo`` and adds
         391 +    ``devectorize(obs)`` / ``vectorize(ocs)`` that proxy to the host. The agent
         392 +    writes ``observation_space.devectorize(obs)`` exactly as it would at eval.
         393 +    """
         394 +
         395 +    def __init__(self, spec: dict[str, Any], client: "BlackboxEnv") -> None:
         396 +        super().__init__(spec)
         397 +        self._client = client
         398 +
         399 +    def devectorize(self, obs: Any) -> Any:
         400 +        """Return an object-centric view of *obs* as a remote handle."""
         401 +        return self._client.devectorize(obs)
         402 +
         403 +    def vectorize(self, state: Any) -> np.ndarray:
         404 +        """Return the flat observation vector for an object-centric state."""
         405 +        return self._client.vectorize(state)
         406 +
         407 +
         408 +class _ObjectCentricObservationSpace:
         409 +    """Client-side view of a variable-count env's ObjectCentricStateSpace.
         410 +
         411 +    The observation is already an object-centric state (reconstructed locally from the
         412 +    wire), so this space has no fixed shape/vector: it exposes the domain ``types`` and
         413 +    ``type_features`` the program needs to enumerate objects, matching the eval-time
         414 +    ``observation_space.types``. There is no ``devectorize`` -- the state is not a
         415 +    vector.
         416 +    """
         417 +
         418 +    def __init__(self, spec: dict[str, Any]) -> None:
         419 +        self._type_by_name, self._type_features = _build_local_types(spec["types"])
         420 +
         421 +    @property
         422 +    def types(self) -> set[_Type]:
         423 +        """The domain object types (matches the eval-time observation_space.types)."""
         424 +        return set(self._type_features)
         425 +
         426 +    @property
         427 +    def type_features(self) -> dict[_Type, list[str]]:
         428 +        """Feature names for each type."""
         429 +        return {t: list(f) for t, f in self._type_features.items()}
         430 +
         431 +    def get_type(self, name: str) -> _Type:
         432 +        """The domain type with the given name (e.g. ``"rectangle"``)."""
         433 +        return self._type_by_name[name]
         434 +
         435 +
         436 +class BlackboxEnv:
         437 +    """A live environment instance, accessed over the wire."""
         438 +
         439 +    def __init__(self, meta: dict[str, Any], sandbox_root: Any = None) -> None:
         440 +        obs_spec = meta["observation_space"]
         441 +        self._strict = bool(meta.get("strict", False))
         442 +        # A variable-count env sends object-centric states, reconstructed locally; a
         443 +        # fixed-count env sends Box vectors as before.
         444 +        self._object_centric = obs_spec.get("type") == "ObjectCentric"
         445 +        if self._object_centric:
         446 +            self.observation_space: Any = _ObjectCentricObservationSpace(obs_spec)
         447 +        elif self._strict:
         448 +            # Strict blackbox exposes only generic array metadata. In particular,
         449 +            # do not attach the host-backed devectorize/vectorize helpers that make
         450 +            # the legacy blackbox convenient but confound the isolation ablation.
         451 +            self.observation_space = SpaceInfo(obs_spec)
         452 +        else:
         453 +            self.observation_space = _BlackboxObservationSpace(obs_spec, self)
         454 +        self.action_space = SpaceInfo(meta["action_space"])
         455 +        self.max_steps: int | None = meta["max_steps"]
         456 +        # How make_primitives rebuilds the eval-time primitives dict (see
         457 +        # robocode.primitives.blackbox_primitive_manifest). Empty when the
         458 +        # run configures no primitives.
         459 +        self._primitive_manifest: list[dict[str, Any]] = meta.get("primitives", [])
         460 +        # Where render_policy looks for approach.py and make_primitives imports
         461 +        # generic primitive sources; the sandbox dir in real runs (set by
         462 +        # make_env), the current dir for ad-hoc construction.
         463 +        self._sandbox_root = (
         464 +            Path(sandbox_root) if sandbox_root is not None else Path.cwd()
         465 +        )
         466 +        self._token: str = meta["token"]
         467 +        self._sock = socket.create_connection((meta["host"], meta["port"]))
         468 +        self._file = self._sock.makefile("rwb")
         469 +
         470 +    def _request(self, payload: dict[str, Any]) -> dict[str, Any]:
         471 +        payload["token"] = self._token
         472 +        self._file.write(json.dumps(payload).encode("utf-8") + b"\n")
         473 +        self._file.flush()
         474 +        line = self._file.readline()
         475 +        if not line:
         476 +            raise RuntimeError("Connection to the environment server was closed")
         477 +        response = json.loads(line)
         478 +        if "error" in response:
         479 +            raise RuntimeError(f"Environment server error: {response['error']}")
         480 +        return _decode(response)
         481 +
         482 +    def _decode_ref(self, obj: Any) -> Any:
         483 +        """Decode a remote-command result, mapping handles to _RemoteHandle.
         484 +
         485 +        ``_request`` already ran ``_decode`` over the response (so ndarrays are
         486 +        arrays), but it leaves ``{"__handle__": id}`` dicts intact since it does
         487 +        not know the handle tag. Here we turn those into ``_RemoteHandle``
         488 +        objects and recurse through the remaining containers.
         489 +        """
         490 +        if isinstance(obj, dict):
         491 +            if _HANDLE_TAG in obj:
         492 +                return _RemoteHandle(self, obj[_HANDLE_TAG])
         493 +            if _SET_TAG in obj:
         494 +                return {self._decode_ref(value) for value in obj[_SET_TAG]}
         495 +            return {key: self._decode_ref(value) for key, value in obj.items()}
         496 +        if isinstance(obj, list):
         497 +            return [self._decode_ref(value) for value in obj]
         498 +        return obj
         499 +
         500 +    def devectorize(self, obs: Any) -> _RemoteHandle:
         501 +        """Return an object-centric view of *obs* (a remote ObjectCentricState).
         502 +
         503 +        Proxies ``observation_space.devectorize`` to the host. The returned
         504 +        handle exposes the public ObjectCentricState API (``get_object_names``,
         505 +        ``get_object_from_name``, ``get_objects``, ``get``, ``set``, ``copy``,
         506 +        ...) over the wire. Pass it straight to the CRV planners from
         507 +        ``make_primitives``.
         508 +        """
         509 +        response = self._request(
         510 +            {"cmd": "devectorize", "obs": _encode(np.asarray(obs))}
         511 +        )
         512 +        return self._decode_ref(response["result"])
         513 +
         514 +    def vectorize(self, state: Any) -> np.ndarray:
         515 +        """Return the flat observation vector for an object-centric state handle."""
         516 +        response = self._request({"cmd": "vectorize", "state": _encode_ref(state)})
         517 +        return self._decode_ref(response["result"])
         518 +
         519 +    def reset(
         520 +        self, seed: int | None = None, options: dict[str, Any] | None = None
         521 +    ) -> tuple[np.ndarray, dict[str, Any]]:
         522 +        """Reset the environment; returns (obs, info)."""
         523 +        response = self._request({"cmd": "reset", "seed": seed, "options": options})
         524 +        return response["obs"], response["info"]
         525 +
         526 +    def step(self, action: Any) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
         527 +        """Step the environment; returns (obs, reward, terminated, truncated, info)."""
         528 +        action = np.asarray(action, dtype=self.action_space.dtype)
         529 +        response = self._request({"cmd": "step", "action": _encode(action)})
         530 +        return (
         531 +            response["obs"],
         532 +            response["reward"],
         533 +            response["terminated"],
         534 +            response["truncated"],
         535 +            response["info"],
         536 +        )
         537 +
         538 +    def get_state(self) -> Any:
         539 +        """Return a snapshot of the full environment state.
         540 +
         541 +        A Box vector for a fixed-count env; a local ObjectCentricState for a
         542 +        variable-count env (reconstructed by ``_decode``).
         543 +        """
         544 +        return self._request({"cmd": "get_state"})["state"]
         545 +
         546 +    def _encode_state(self, state: Any) -> Any:
         547 +        """Encode a state for the wire: an object-centric state or a Box vector."""
         548 +        if isinstance(state, _ObjectCentricState):
         549 +            return _encode(state)
         550 +        return _encode(np.asarray(state))
         551 +
         552 +    def render_state(
         553 +        self,
         554 +        seed: int = 42,
         555 +        state: Any = None,
         556 +        label: str = "",
         557 +        object_count: int | None = None,
         558 +    ) -> str:
         559 +        """Render a state on the host; returns a PNG path inside the sandbox.
         560 +
         561 +        Either pass ``seed`` to render the initial state after a reset (with
         562 +        ``object_count`` to pin a variable-count env's object count), or ``state`` (a
         563 +        flat list of floats, as from ``get_state().tolist()``) to render an arbitrary
         564 +        state. The path is relative to the sandbox dir.
         565 +        """
         566 +        if isinstance(state, _ObjectCentricState):
         567 +            state = _encode(state)  # tagged object-centric payload, decoded host-side
         568 +        elif isinstance(state, np.ndarray):
         569 +            state = state.tolist()
         570 +        return self._request(
         571 +            {
         572 +                "cmd": "render_state",
         573 +                "seed": seed,
         574 +                "state": state,
         575 +                "label": label,
         576 +                "object_count": object_count,
         577 +            }
         578 +        )["path"]
         579 +
         580 +    def render_policy(
         581 +        self,
         582 +        seed: int = 42,
         583 +        max_steps: int = 1000,
         584 +        max_frames: int = 100,
         585 +        approach_path: Any = None,
         586 +        object_count: int | None = None,
         587 +    ) -> list[str]:
         588 +        """Run an episode of approach.py here and render the visited states.
         589 +
         590 +        The policy runs in this process: only ``get_action`` (which needs the
         591 +        observation alone) executes locally, while each visited state is
         592 +        rendered on the host via ``render_state``. No approach code runs on the
         593 +        host, so a black-box agent cannot reach the env source through rendering.
         594 +        ``object_count`` pins a variable-count env's object count on the rollout reset.
         595 +        Returns the PNG paths (relative to the sandbox dir).
         596 +        """
         597 +        path = (
         598 +            Path(approach_path)
         599 +            if approach_path is not None
         600 +            else self._sandbox_root / "approach.py"
         601 +        )
         602 +        approach = _load_generated_approach(
         603 +            path, self.action_space, self.observation_space, self.make_primitives()
         604 +        )
         605 +        options = {"object_count": object_count} if object_count is not None else None
         606 +        obs, info = self.reset(seed=seed, options=options)
         607 +        approach.reset(obs, info)
         608 +        # Strict mode deliberately withholds raw state snapshots. Its observations
         609 +        # are nevertheless renderable, so use them to visualize a policy without
         610 +        # opening the get_state channel to agent scripts.
         611 +        states = [obs if self._strict else self.get_state()]
         612 +        for _ in range(max_steps):
         613 +            obs, reward, terminated, truncated, info = self.step(
         614 +                approach.get_action(obs)
         615 +            )
         616 +            if hasattr(approach, "update"):
         617 +                approach.update(obs, reward, terminated or truncated, info)
         618 +            states.append(obs if self._strict else self.get_state())
         619 +            if terminated or truncated:
         620 +                break
         621 +        return [
         622 +            self.render_state(state=state, label=f"policy_seed{seed}_{i:04d}")
         623 +            for i, state in enumerate(states[:max_frames])
         624 +        ]
         625 +
         626 +    def set_state(self, state: Any) -> None:
         627 +        """Restore a state snapshot previously returned by get_state()."""
         628 +        self._request({"cmd": "set_state", "state": self._encode_state(state)})
         629 +
         630 +    def check_action_collision(self, state: Any, action: Any) -> bool:
         631 +        """Return True if taking *action* in *state* causes a collision.
         632 +
         633 +        Runs the env-dependent collision primitive on the host (the sandbox
         634 +        lacks the env source), against this connection's env. Mirrors the
         635 +        eval-time ``primitives['check_action_collision']`` callable, so test
         636 +        scripts that get it from ``make_primitives`` call it the same way.
         637 +        """
         638 +        response = self._request(
         639 +            {
         640 +                "cmd": "check_action_collision",
         641 +                "state": self._encode_state(state),
         642 +                "action": _encode(np.asarray(action, dtype=self.action_space.dtype)),
         643 +            }
         644 +        )
         645 +        return response["collision"]
         646 +
         647 +    def make_primitives(self) -> dict[str, Any]:
         648 +        """Build the eval-time primitives dict for this black-box env.
         649 +
         650 +        Black-box counterpart of ``robocode.primitives.build_primitives``:
         651 +        env-dependent primitives proxy to the host, while generic ones are
         652 +        imported from their copies under ``primitives/`` in the sandbox. Use
         653 +        it in test scripts so they exercise exactly the primitives the harness
         654 +        passes to ``GeneratedApproach`` at evaluation time::
         655 +
         656 +            from env_client import make_env
         657 +
         658 +            env = make_env()
         659 +            primitives = env.make_primitives()
         660 +        """
         661 +        sandbox_dir = str(self._sandbox_root.resolve())
         662 +        if sandbox_dir not in sys.path:
         663 +            sys.path.insert(0, sandbox_dir)
         664 +        primitives: dict[str, Any] = {}
         665 +        for spec in self._primitive_manifest:
         666 +            if spec["kind"] == "host_proxy":
         667 +                primitives[spec["name"]] = getattr(self, spec["name"])
         668 +            elif spec["kind"] == "remote_module":
         669 +                # The module source is withheld from the sandbox; reach it on
         670 +                # the host via a remote-module proxy (e.g. crv_motion_planning).
         671 +                primitives[spec["name"]] = _RemoteModule(self, spec["module"])
         672 +            else:
         673 +                module = importlib.import_module(f"primitives.{spec['module']}")
         674 +                primitives[spec["name"]] = (
         675 +                    module if spec["attr"] is None else getattr(module, spec["attr"])
         676 +                )
         677 +        return primitives
         678 +
         679 +    def close(self) -> None:
         680 +        """Close the connection (and the server-side environment)."""
         681 +        try:
         682 +            self._file.write(
         683 +                json.dumps({"cmd": "close", "token": self._token}).encode("utf-8")
         684 +                + b"\n"
         685 +            )
         686 +            self._file.flush()
         687 +        finally:
         688 +            # makefile() wraps a dup of the socket; close it too so the buffered
         689 +            # file object does not leak (ResourceWarning) when close() runs.
         690 +            self._file.close()
         691 +            self._sock.close()
         692 +
         693 +    def __enter__(self) -> "BlackboxEnv":
         694 +        return self
         695 +
         696 +    def __exit__(self, *exc_info: Any) -> None:
         697 +        self.close()
         698 +
         699 +
         700 +def _load_generated_approach(
         701 +    path: Path, action_space: Any, observation_space: Any, primitives: dict[str, Any]
         702 +) -> Any:
         703 +    """Exec ``approach.py`` and instantiate its ``GeneratedApproach``.
         704 +
         705 +    Mirrors ``robocode.utils.episode.load_generated_approach``; duplicated here
         706 +    (like the codec above) because this module must stay importable with only
         707 +    the standard library and numpy, since it is copied standalone into the
         708 +    sandbox. Used only by ``render_policy`` for visual debugging.
         709 +    """
         710 +    sandbox_dir = str(path.resolve().parent)
         711 +    added = sandbox_dir not in sys.path
         712 +    if added:
         713 +        sys.path.insert(0, sandbox_dir)
         714 +    try:
         715 +        namespace: dict[str, Any] = {"__file__": str(path)}
         716 +        exec(  # pylint: disable=exec-used
         717 +            compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace
         718 +        )
         719 +    finally:
         720 +        if added:
         721 +            sys.path.remove(sandbox_dir)
         722 +    return namespace["GeneratedApproach"](
         723 +        action_space, observation_space, primitives=primitives
         724 +    )
         725 +
         726 +
         727 +def make_env(metadata_path: Any = None) -> BlackboxEnv:
         728 +    """Connect to the environment server; returns a fresh env instance.
         729 +
         730 +    *metadata_path* defaults to ``env_spaces.json`` next to this module
         731 +    (the agent's sandbox copy); the MCP server passes an explicit path.
         732 +    """
         733 +    path = Path(metadata_path) if metadata_path is not None else _METADATA_PATH
         734 +    meta = json.loads(path.read_text(encoding="utf-8"))
         735 +    return BlackboxEnv(meta, sandbox_root=path.parent)
diff --git a/env_spaces.json b/env_spaces.json
new file mode 100644
index 0000000..c4d5769
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1,124 @@
           1 +{
           2 +  "host": "127.0.0.1",
           3 +  "port": 43217,
           4 +  "token": "f565f752bc17ad7b55f4fd335c3d1f47",
           5 +  "observation_space": {
           6 +    "type": "Box",
           7 +    "shape": [
           8 +      45
           9 +    ],
          10 +    "low": [
          11 +      -Infinity,
          12 +      -Infinity,
          13 +      -Infinity,
          14 +      -Infinity,
          15 +      -Infinity,
          16 +      -Infinity,
          17 +      -Infinity,
          18 +      -Infinity,
          19 +      -Infinity,
          20 +      -Infinity,
          21 +      -Infinity,
          22 +      -Infinity,
          23 +      -Infinity,
          24 +      -Infinity,
          25 +      -Infinity,
          26 +      -Infinity,
          27 +      -Infinity,
          28 +      -Infinity,
          29 +      -Infinity,
          30 +      -Infinity,
          31 +      -Infinity,
          32 +      -Infinity,
          33 +      -Infinity,
          34 +      -Infinity,
          35 +      -Infinity,
          36 +      -Infinity,
          37 +      -Infinity,
          38 +      -Infinity,
          39 +      -Infinity,
          40 +      -Infinity,
          41 +      -Infinity,
          42 +      -Infinity,
          43 +      -Infinity,
          44 +      -Infinity,
          45 +      -Infinity,
          46 +      -Infinity,
          47 +      -Infinity,
          48 +      -Infinity,
          49 +      -Infinity,
          50 +      -Infinity,
          51 +      -Infinity,
          52 +      -Infinity,
          53 +      -Infinity,
          54 +      -Infinity,
          55 +      -Infinity
          56 +    ],
          57 +    "high": [
          58 +      Infinity,
          59 +      Infinity,
          60 +      Infinity,
          61 +      Infinity,
          62 +      Infinity,
          63 +      Infinity,
          64 +      Infinity,
          65 +      Infinity,
          66 +      Infinity,
          67 +      Infinity,
          68 +      Infinity,
          69 +      Infinity,
          70 +      Infinity,
          71 +      Infinity,
          72 +      Infinity,
          73 +      Infinity,
          74 +      Infinity,
          75 +      Infinity,
          76 +      Infinity,
          77 +      Infinity,
          78 +      Infinity,
          79 +      Infinity,
          80 +      Infinity,
          81 +      Infinity,
          82 +      Infinity,
          83 +      Infinity,
          84 +      Infinity,
          85 +      Infinity,
          86 +      Infinity,
          87 +      Infinity,
          88 +      Infinity,
          89 +      Infinity,
          90 +      Infinity,
          91 +      Infinity,
          92 +      Infinity,
          93 +      Infinity,
          94 +      Infinity,
          95 +      Infinity,
          96 +      Infinity,
          97 +      Infinity,
          98 +      Infinity,
          99 +      Infinity,
         100 +      Infinity,
         101 +      Infinity,
         102 +      Infinity
         103 +    ],
         104 +    "dtype": "float64"
         105 +  },
         106 +  "action_space": {
         107 +    "type": "Box",
         108 +    "shape": [
         109 +      2
         110 +    ],
         111 +    "low": [
         112 +      -0.05,
         113 +      -0.05
         114 +    ],
         115 +    "high": [
         116 +      0.05,
         117 +      0.05
         118 +    ],
         119 +    "dtype": "float64"
         120 +  },
         121 +  "max_steps": 1000,
         122 +  "primitives": [],
         123 +  "strict": true
         124 +}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Add baseline behind-object pushing policy and test harness

Commit `64e280702248a44d6781c642956d3ab514583499`; parents: 3a55000d50a578e4d66458a315fe18d7c656e83f. Recorded author date: 2026-09-09T08:24:52+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0009](01_timeline.md#E0009): commit hash in recorded output.
[Controller after this commit](evidence/versions/C002_64e2807_approach.py) · [Exact all-file diff](evidence/diffs/C002_64e2807.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..e72d96e
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,30 @@
           1 +import math
           2 +import numpy as np
           3 +
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.low = np.asarray(action_space.low, dtype=float)
           8 +        self.high = np.asarray(action_space.high, dtype=float)
           9 +        self.reset(None, None)
          10 +
          11 +    def reset(self, state, info):
          12 +        self.step = 0
          13 +
          14 +    def get_action(self, state):
          15 +        s = np.asarray(state, dtype=float)
          16 +        obj = s[0:2]
          17 +        robot = s[16:18]
          18 +        goal = s[29:31]
          19 +        delta = goal - obj
          20 +        dist = float(np.linalg.norm(delta))
          21 +        if dist > 1e-9:
          22 +            direction = delta / dist
          23 +        else:
          24 +            direction = np.array([1.0, 0.0])
          25 +        # First get behind the object, then push through its centre.
          26 +        stand = obj - direction * 0.16
          27 +        target = stand if np.linalg.norm(robot - stand) > 0.055 else obj + direction * 0.10
          28 +        action = np.clip(target - robot, self.low, self.high)
          29 +        self.step += 1
          30 +        return action.astype(float)
diff --git a/probe_strategy.py b/probe_strategy.py
new file mode 100644
index 0000000..0e2735c
--- /dev/null
+++ b/probe_strategy.py
@@ -0,0 +1,16 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +
           5 +def main():
           6 +    for seed in range(10):
           7 +        env = make_env()
           8 +        obs, _ = env.reset(seed=seed)
           9 +        print(seed, "block", np.round(obs[0:3], 3), "robot", np.round(obs[16:18], 3),
          10 +              "goal", np.round(obs[29:32], 3), "dims", np.round(obs[12:15], 3),
          11 +              "r", round(float(obs[28]), 3))
          12 +        env.close()
          13 +
          14 +
          15 +if __name__ == "__main__":
          16 +    main()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..4956428
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,28 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +
           7 +def run(seed, verbose=False):
           8 +    env = make_env()
           9 +    obs, info = env.reset(seed=seed)
          10 +    policy = GeneratedApproach(env.action_space, env.observation_space, {})
          11 +    policy.reset(obs, info)
          12 +    initial = obs.copy()
          13 +    for step in range(env.max_steps):
          14 +        obs, reward, term, trunc, info = env.step(policy.get_action(obs))
          15 +        if term or trunc:
          16 +            break
          17 +    env.close()
          18 +    pe = np.linalg.norm(obs[:2] - obs[29:31])
          19 +    ae = abs((obs[2] - obs[31] + np.pi) % (2*np.pi) - np.pi)
          20 +    print(seed, term, step + 1, 'err', round(float(pe), 3), round(float(ae), 3),
          21 +          'init', np.round(initial[[0,1,2,16,17,29,30,31]], 3))
          22 +    return term, step + 1
          23 +
          24 +
          25 +if __name__ == '__main__':
          26 +    seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
          27 +    results = [run(s) for s in seeds]
          28 +    print('success', sum(x[0] for x in results), '/', len(results))
```

</details>

<a id="C003"></a>
### C003 · add isolated reset and contact probing script

Commit `30211d83199d26a08cf3f97f809e0dc0ca355265`; parents: 64e280702248a44d6781c642956d3ab514583499. Recorded author date: 2026-09-09T08:25:28+02:00.

File roles (automatic): support code (role needs review).

[Exact all-file diff](evidence/diffs/C003_30211d8.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/explore_geometry.py b/explore_geometry.py
new file mode 100644
index 0000000..c19a815
--- /dev/null
+++ b/explore_geometry.py
@@ -0,0 +1,74 @@
           1 +"""Small black-box probes for DynPushT2D reset and contact dynamics."""
           2 +import argparse
           3 +import math
           4 +
           5 +import numpy as np
           6 +
           7 +from env_client import make_env
           8 +
           9 +
          10 +def resets(count):
          11 +    env = make_env()
          12 +    try:
          13 +        for seed in range(count):
          14 +            s, _ = env.reset(seed=seed)
          15 +            print(
          16 +                seed,
          17 +                "block", np.round(s[[0, 1, 2]], 4).tolist(),
          18 +                "robot", np.round(s[[16, 17]], 4).tolist(),
          19 +                "goal", np.round(s[[29, 30, 31]], 4).tolist(),
          20 +                "dims", np.round(s[[12, 13, 14, 28]], 4).tolist(),
          21 +            )
          22 +    finally:
          23 +        env.close()
          24 +
          25 +
          26 +def drive_to(env, state, target, max_steps=100):
          27 +    """Move robot toward a world point, stopping once close."""
          28 +    for _ in range(max_steps):
          29 +        delta = np.asarray(target) - state[16:18]
          30 +        if np.linalg.norm(delta) < 0.006:
          31 +            break
          32 +        action = np.clip(delta, -0.05, 0.05)
          33 +        state, _, done, trunc, _ = env.step(action)
          34 +        if done or trunc:
          35 +            break
          36 +    return state
          37 +
          38 +
          39 +def contact(seed, offset, push, push_steps=8):
          40 +    env = make_env()
          41 +    try:
          42 +        s, _ = env.reset(seed=seed)
          43 +        start = s.copy()
          44 +        target = s[0:2] + np.asarray(offset)
          45 +        s = drive_to(env, s, target)
          46 +        pre = s.copy()
          47 +        rows = []
          48 +        for k in range(push_steps):
          49 +            s, _, done, trunc, _ = env.step(np.asarray(push, dtype=float))
          50 +            rows.append((k + 1, *(s[0:3] - start[0:3]), *s[0:3], *s[16:18]))
          51 +            if done or trunc:
          52 +                break
          53 +        print("seed", seed, "offset", offset, "push", push)
          54 +        print("start", np.round(start[[0, 1, 2, 16, 17]], 4).tolist())
          55 +        print("pre", np.round(pre[[0, 1, 2, 16, 17]], 4).tolist())
          56 +        for row in rows:
          57 +            print(np.round(row, 5).tolist())
          58 +    finally:
          59 +        env.close()
          60 +
          61 +
          62 +if __name__ == "__main__":
          63 +    parser = argparse.ArgumentParser()
          64 +    parser.add_argument("mode", choices=("resets", "contact"))
          65 +    parser.add_argument("--count", type=int, default=20)
          66 +    parser.add_argument("--seed", type=int, default=0)
          67 +    parser.add_argument("--offset", nargs=2, type=float, default=(-0.15, 0))
          68 +    parser.add_argument("--push", nargs=2, type=float, default=(0.05, 0))
          69 +    parser.add_argument("--steps", type=int, default=8)
          70 +    args = parser.parse_args()
          71 +    if args.mode == "resets":
          72 +        resets(args.count)
          73 +    else:
          74 +        contact(args.seed, args.offset, args.push, args.steps)
```

</details>

<a id="C004"></a>
### C004 · Respect robot Euclidean displacement limit

Commit `7cc31b73668228286bb7d18041a7e8908fde80f1`; parents: 30211d83199d26a08cf3f97f809e0dc0ca355265. Recorded author date: 2026-09-09T08:25:29+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0017](01_timeline.md#E0017): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_7cc31b7_approach.py) · [Exact all-file diff](evidence/diffs/C004_7cc31b7.diff)

[Previous saved controller snapshot](evidence/versions/C002_64e2807_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e72d96e..4dad70d 100644
--- a/approach.py
+++ b/approach.py
@@ -26,5 +26,9 @@ class GeneratedApproach:
   26     26          stand = obj - direction * 0.16
   27     27          target = stand if np.linalg.norm(robot - stand) > 0.055 else obj + direction * 0.10
   28     28          action = np.clip(target - robot, self.low, self.high)
          29 +        # The robot has a Euclidean displacement cap in addition to Box bounds.
          30 +        norm = float(np.linalg.norm(action))
          31 +        if norm > 0.049:
          32 +            action *= 0.049 / norm
   29     33          self.step += 1
   30     34          return action.astype(float)
diff --git a/probe_dynamics.py b/probe_dynamics.py
new file mode 100644
index 0000000..90980b3
--- /dev/null
+++ b/probe_dynamics.py
@@ -0,0 +1,168 @@
           1 +"""Small empirical probe for DynPushT2D dynamics (never imported by approach.py)."""
           2 +
           3 +import math
           4 +
           5 +import numpy as np
           6 +
           7 +from env_client import make_env
           8 +
           9 +
          10 +def angle_wrap(x):
          11 +    return (x + math.pi) % (2.0 * math.pi) - math.pi
          12 +
          13 +
          14 +def reset_summary(seed):
          15 +    env = make_env()
          16 +    obs, _ = env.reset(seed=seed)
          17 +    print(
          18 +        "RESET",
          19 +        seed,
          20 +        "block",
          21 +        np.round(obs[[0, 1, 2]], 5).tolist(),
          22 +        "robot",
          23 +        np.round(obs[[16, 17]], 5).tolist(),
          24 +        "goal",
          25 +        np.round(obs[[29, 30, 31]], 5).tolist(),
          26 +        "dims",
          27 +        np.round(obs[[12, 13, 14, 28]], 5).tolist(),
          28 +        "max_steps",
          29 +        env.max_steps,
          30 +    )
          31 +    env.close()
          32 +
          33 +
          34 +def free_motion(seed):
          35 +    """Move directly away from the block to avoid an accidental collision."""
          36 +    env = make_env()
          37 +    obs, _ = env.reset(seed=seed)
          38 +    start = obs.copy()
          39 +    away = obs[16:18] - obs[0:2]
          40 +    axis = int(np.argmax(np.abs(away)))
          41 +    act = np.zeros(2, dtype=np.float32)
          42 +    act[axis] = 0.03 * (1.0 if away[axis] >= 0 else -1.0)
          43 +    rows = []
          44 +    for _ in range(3):
          45 +        obs, _, _, _, _ = env.step(act)
          46 +        rows.append((obs[16:18].copy(), obs[19:21].copy(), obs[0:2].copy()))
          47 +    robot_d = [r[0] - start[16:18] for r in rows]
          48 +    block_d = [r[2] - start[0:2] for r in rows]
          49 +    print(
          50 +        "FREE",
          51 +        seed,
          52 +        "action",
          53 +        act.tolist(),
          54 +        "robot_delta",
          55 +        np.round(robot_d, 6).tolist(),
          56 +        "reported_v",
          57 +        np.round([r[1] for r in rows], 6).tolist(),
          58 +        "block_delta",
          59 +        np.round(block_d, 7).tolist(),
          60 +    )
          61 +    env.close()
          62 +
          63 +
          64 +def ram_center(seed):
          65 +    """Drive toward the block center and measure first contact and sustained push."""
          66 +    env = make_env()
          67 +    obs, _ = env.reset(seed=seed)
          68 +    initial = obs.copy()
          69 +    first_contact = None
          70 +    samples = []
          71 +    terminated_at = None
          72 +    for step in range(1, 121):
          73 +        vec = obs[0:2] - obs[16:18]
          74 +        norm = float(np.linalg.norm(vec))
          75 +        act = 0.05 * vec / max(norm, 1e-9)
          76 +        obs, reward, term, trunc, _ = env.step(act.astype(np.float32))
          77 +        bdisp = float(np.linalg.norm(obs[0:2] - initial[0:2]))
          78 +        if first_contact is None and bdisp > 1e-5:
          79 +            first_contact = (
          80 +                step,
          81 +                norm,
          82 +                obs[16:18].copy(),
          83 +                obs[0:2].copy(),
          84 +                obs[3:6].copy(),
          85 +            )
          86 +        if first_contact is not None and step in {
          87 +            first_contact[0],
          88 +            first_contact[0] + 1,
          89 +            first_contact[0] + 5,
          90 +            first_contact[0] + 15,
          91 +        }:
          92 +            samples.append(
          93 +                (
          94 +                    step,
          95 +                    obs[0:2] - initial[0:2],
          96 +                    angle_wrap(float(obs[2] - initial[2])),
          97 +                    obs[16:18].copy(),
          98 +                )
          99 +            )
         100 +        if term or trunc:
         101 +            terminated_at = (step, term, trunc, reward)
         102 +            break
         103 +    fc = None
         104 +    if first_contact:
         105 +        fc = (
         106 +            first_contact[0],
         107 +            round(first_contact[1], 5),
         108 +            np.round(first_contact[2], 5).tolist(),
         109 +            np.round(first_contact[3], 5).tolist(),
         110 +            np.round(first_contact[4], 5).tolist(),
         111 +        )
         112 +    pretty_samples = [
         113 +        (s, np.round(d, 5).tolist(), round(a, 5), np.round(r, 5).tolist())
         114 +        for s, d, a, r in samples
         115 +    ]
         116 +    print("RAM", seed, "first", fc, "samples", pretty_samples, "stop", terminated_at)
         117 +    env.close()
         118 +
         119 +
         120 +def coast_after_push(seed):
         121 +    """Reach contact, issue one push, then zeros to expose inertia/damping."""
         122 +    env = make_env()
         123 +    obs, _ = env.reset(seed=seed)
         124 +    initial = obs.copy()
         125 +    contacted = False
         126 +    push_action = None
         127 +    for _ in range(100):
         128 +        vec = obs[0:2] - obs[16:18]
         129 +        act = 0.05 * vec / max(float(np.linalg.norm(vec)), 1e-9)
         130 +        obs, _, term, trunc, _ = env.step(act.astype(np.float32))
         131 +        if np.linalg.norm(obs[0:2] - initial[0:2]) > 1e-5:
         132 +            contacted = True
         133 +            push_action = act.copy()
         134 +            break
         135 +        if term or trunc:
         136 +            break
         137 +    rows = []
         138 +    if contacted:
         139 +        for k in range(8):
         140 +            obs, _, term, trunc, _ = env.step(np.zeros(2, dtype=np.float32))
         141 +            rows.append((k + 1, obs[0:2].copy(), obs[3:6].copy(), obs[16:18].copy()))
         142 +            if term or trunc:
         143 +                break
         144 +    print(
         145 +        "COAST",
         146 +        seed,
         147 +        "contacted",
         148 +        contacted,
         149 +        "last_action",
         150 +        None if push_action is None else np.round(push_action, 5).tolist(),
         151 +        "rows",
         152 +        [
         153 +            (k, np.round(p, 5).tolist(), np.round(v, 5).tolist(), np.round(r, 5).tolist())
         154 +            for k, p, v, r in rows
         155 +        ],
         156 +    )
         157 +    env.close()
         158 +
         159 +
         160 +if __name__ == "__main__":
         161 +    env = make_env()
         162 +    print("SPACES", env.observation_space.shape, env.action_space.low, env.action_space.high)
         163 +    env.close()
         164 +    for probe_seed in range(4):
         165 +        reset_summary(probe_seed)
         166 +        free_motion(probe_seed)
         167 +        ram_center(probe_seed)
         168 +    coast_after_push(0)
```

</details>

<a id="C005"></a>
### C005 · Keep dynamics probes inside strict action norm

Commit `937d66d0ab7a87bcda9b8aac36a7be1d8eb09f19`; parents: 7cc31b73668228286bb7d18041a7e8908fde80f1. Recorded author date: 2026-09-09T08:26:02+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C005_937d66d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dynamics.py b/probe_dynamics.py
index 90980b3..2140a5a 100644
--- a/probe_dynamics.py
+++ b/probe_dynamics.py
@@ -72,7 +72,8 @@ def ram_center(seed):
   72     72      for step in range(1, 121):
   73     73          vec = obs[0:2] - obs[16:18]
   74     74          norm = float(np.linalg.norm(vec))
   75        -        act = 0.05 * vec / max(norm, 1e-9)
          75 +        # Stay just inside the server's strict Euclidean-norm action bound.
          76 +        act = 0.049 * vec / max(norm, 1e-9)
   76     77          obs, reward, term, trunc, _ = env.step(act.astype(np.float32))
   77     78          bdisp = float(np.linalg.norm(obs[0:2] - initial[0:2]))
   78     79          if first_contact is None and bdisp > 1e-5:
@@ -126,7 +127,7 @@ def coast_after_push(seed):
  126    127      push_action = None
  127    128      for _ in range(100):
  128    129          vec = obs[0:2] - obs[16:18]
  129        -        act = 0.05 * vec / max(float(np.linalg.norm(vec)), 1e-9)
         130 +        act = 0.049 * vec / max(float(np.linalg.norm(vec)), 1e-9)
  130    131          obs, _, term, trunc, _ = env.step(act.astype(np.float32))
  131    132          if np.linalg.norm(obs[0:2] - initial[0:2]) > 1e-5:
  132    133              contacted = True
```

</details>

<a id="C006"></a>
### C006 · add isolated heuristic T-block strategy experiments

Commit `06760904bcfd29387e1062b9f9da5b09918ef1bd`; parents: 937d66d0ab7a87bcda9b8aac36a7be1d8eb09f19. Recorded author date: 2026-09-09T08:26:36+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

[Exact all-file diff](evidence/diffs/C006_0676090.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/candidate_strategy.py b/candidate_strategy.py
new file mode 100644
index 0000000..cc1fffa
--- /dev/null
+++ b/candidate_strategy.py
@@ -0,0 +1,125 @@
           1 +"""Experimental policy for DynPushT2D, kept separate from the submitted approach."""
           2 +import math
           3 +import numpy as np
           4 +
           5 +
           6 +def wrap_angle(x):
           7 +    return (x + math.pi) % (2.0 * math.pi) - math.pi
           8 +
           9 +
          10 +class CandidateStrategy:
          11 +    def __init__(self, action_space, observation_space, primitives):
          12 +        self.low = np.asarray(action_space.low, dtype=float)
          13 +        self.high = np.asarray(action_space.high, dtype=float)
          14 +        self.phase = "select"
          15 +        self.mode = None
          16 +        self.side = 1.0
          17 +        self.ticks = 0
          18 +
          19 +    def reset(self, state, info):
          20 +        self.phase = "select"
          21 +        self.mode = None
          22 +        self.side = 1.0
          23 +        self.ticks = 0
          24 +
          25 +    @staticmethod
          26 +    def _unit(v):
          27 +        n = float(np.linalg.norm(v))
          28 +        return v / n if n > 1e-9 else np.zeros(2)
          29 +
          30 +    def _move(self, robot, target, gain=1.0):
          31 +        return np.clip((target - robot) * gain, self.low, self.high)
          32 +
          33 +    def _select(self, s):
          34 +        c = s[0:2]
          35 +        goal = s[29:31]
          36 +        ae = wrap_angle(float(s[31] - s[2]))
          37 +        pe = float(np.linalg.norm(goal - c))
          38 +        # Pose accuracy requires repeatedly correcting the orientation disturbed by
          39 +        # translation.  Angle gets priority except very close to its tolerance.
          40 +        if abs(ae) > 0.10:
          41 +            self.mode = "rotate"
          42 +            self.side = 1.0 if ae >= 0 else -1.0
          43 +        elif pe > 0.022:
          44 +            self.mode = "translate"
          45 +        else:
          46 +            self.mode = "rotate"
          47 +            self.side = 1.0 if ae >= 0 else -1.0
          48 +        self.phase = "retreat"
          49 +        self.ticks = 0
          50 +
          51 +    def _geometry(self, s):
          52 +        c = np.asarray(s[0:2], dtype=float)
          53 +        robot = np.asarray(s[16:18], dtype=float)
          54 +        if self.mode == "translate":
          55 +            force = self._unit(np.asarray(s[29:31]) - c)
          56 +            # Contact somewhere on the rear-facing support surface.
          57 +            contact = c - force * 0.52
          58 +            setup = c - force * 0.83
          59 +        else:
          60 +            th = float(s[2])
          61 +            ex = np.array([math.cos(th), math.sin(th)])
          62 +            ey = np.array([-math.sin(th), math.cos(th)])
          63 +            # Push tangentially on the positive local-x end. side is torque sign.
          64 +            contact = c + ex * (0.40 * float(s[13]))
          65 +            force = ey * self.side
          66 +            setup = contact - force * 0.30
          67 +        return c, robot, contact, setup, force
          68 +
          69 +    def get_action(self, state):
          70 +        s = np.asarray(state, dtype=float)
          71 +        self.ticks += 1
          72 +        if self.phase == "select":
          73 +            self._select(s)
          74 +        c, robot, contact, setup, force = self._geometry(s)
          75 +
          76 +        # Use a collision-free polar repositioning maneuver around the object.
          77 +        ray = self._unit(setup - c)
          78 +        radius = 0.88
          79 +        rvec = robot - c
          80 +        rdist = float(np.linalg.norm(rvec))
          81 +        rang = math.atan2(rvec[1], rvec[0])
          82 +        tang = math.atan2(ray[1], ray[0])
          83 +        adiff = wrap_angle(tang - rang)
          84 +
          85 +        if self.phase == "retreat":
          86 +            if rdist >= radius - 0.04:
          87 +                self.phase = "orbit"
          88 +            else:
          89 +                outward = self._unit(rvec)
          90 +                if np.linalg.norm(outward) < 0.5:
          91 +                    outward = ray
          92 +                return self._move(robot, c + outward * radius)
          93 +
          94 +        if self.phase == "orbit":
          95 +            if abs(adiff) < 0.10:
          96 +                self.phase = "approach"
          97 +            else:
          98 +                # A look-ahead point gives smooth travel around the clearance circle.
          99 +                stepang = rang + max(-0.35, min(0.35, adiff))
         100 +                waypoint = c + radius * np.array([math.cos(stepang), math.sin(stepang)])
         101 +                return self._move(robot, waypoint)
         102 +
         103 +        if self.phase == "approach":
         104 +            if np.linalg.norm(robot - setup) < 0.055:
         105 +                self.phase = "push"
         106 +                self.ticks = 0
         107 +            else:
         108 +                return self._move(robot, setup)
         109 +
         110 +        if self.phase == "push":
         111 +            ae = wrap_angle(float(s[31] - s[2]))
         112 +            pe = float(np.linalg.norm(s[29:31] - c))
         113 +            done = ((self.mode == "rotate" and (abs(ae) < 0.065 or self.ticks > 55)) or
         114 +                    (self.mode == "translate" and (pe < 0.020 or abs(ae) > 0.16 or self.ticks > 90)))
         115 +            if done:
         116 +                self.phase = "select"
         117 +            # Aim through the selected contact, then continue in the desired force direction.
         118 +            aim = contact + force * 0.35
         119 +            return self._move(robot, aim)
         120 +
         121 +        return np.zeros(2)
         122 +
         123 +
         124 +# Allows the same test harness shape as approach.py.
         125 +GeneratedApproach = CandidateStrategy
diff --git a/test_candidate_strategy.py b/test_candidate_strategy.py
new file mode 100644
index 0000000..458b497
--- /dev/null
+++ b/test_candidate_strategy.py
@@ -0,0 +1,32 @@
           1 +from env_client import make_env
           2 +from candidate_strategy import CandidateStrategy
           3 +import numpy as np
           4 +import sys
           5 +
           6 +
           7 +def run(seed, verbose=False):
           8 +    env = make_env()
           9 +    obs, info = env.reset(seed=seed)
          10 +    policy = CandidateStrategy(env.action_space, env.observation_space, env.make_primitives())
          11 +    policy.reset(obs, info)
          12 +    initial = obs.copy()
          13 +    for step in range(env.max_steps):
          14 +        obs, reward, term, trunc, info = env.step(policy.get_action(obs))
          15 +        if verbose and (step % 100 == 99 or term or trunc):
          16 +            ae = (obs[31] - obs[2] + np.pi) % (2*np.pi) - np.pi
          17 +            print(seed, step + 1, policy.mode, policy.phase, "poserr", round(float(np.linalg.norm(obs[29:31]-obs[0:2])), 3), "angerr", round(float(ae), 3))
          18 +        if term or trunc:
          19 +            break
          20 +    env.close()
          21 +    ae = (obs[31] - obs[2] + np.pi) % (2*np.pi) - np.pi
          22 +    return term, step + 1, float(np.linalg.norm(obs[29:31]-obs[0:2])), abs(float(ae)), initial, obs
          23 +
          24 +
          25 +if __name__ == "__main__":
          26 +    seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
          27 +    results = []
          28 +    for seed in seeds:
          29 +        result = run(seed, verbose=True)
          30 +        results.append(result)
          31 +        print("RESULT", seed, result[:4])
          32 +    print("SUMMARY", sum(r[0] for r in results), "/", len(results), "mean_steps", np.mean([r[1] for r in results]))
```

</details>

<a id="C007"></a>
### C007 · print failing candidate actions for strict harness debugging

Commit `0d015e9834c02f991666c36eb49445093a8faf27`; parents: 06760904bcfd29387e1062b9f9da5b09918ef1bd. Recorded author date: 2026-09-09T08:26:49+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C007_0d015e9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_candidate_strategy.py b/test_candidate_strategy.py
index 458b497..439d104 100644
--- a/test_candidate_strategy.py
+++ b/test_candidate_strategy.py
@@ -11,7 +11,12 @@ def run(seed, verbose=False):
   11     11      policy.reset(obs, info)
   12     12      initial = obs.copy()
   13     13      for step in range(env.max_steps):
   14        -        obs, reward, term, trunc, info = env.step(policy.get_action(obs))
          14 +        action = policy.get_action(obs)
          15 +        try:
          16 +            obs, reward, term, trunc, info = env.step(action)
          17 +        except Exception:
          18 +            print("BAD ACTION", seed, step, action, action.dtype, policy.mode, policy.phase)
          19 +            raise
   15     20          if verbose and (step % 100 == 99 or term or trunc):
   16     21              ae = (obs[31] - obs[2] + np.pi) % (2*np.pi) - np.pi
   17     22              print(seed, step + 1, policy.mode, policy.phase, "poserr", round(float(np.linalg.norm(obs[29:31]-obs[0:2])), 3), "angerr", round(float(ae), 3))
```

</details>

<a id="C008"></a>
### C008 · Report local-frame contact coordinates in dynamics probe

Commit `aec5753c685e074fc609de5686c7b36264c28278`; parents: 0d015e9834c02f991666c36eb49445093a8faf27. Recorded author date: 2026-09-09T08:27:03+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C008_aec5753.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dynamics.py b/probe_dynamics.py
index 2140a5a..3c8404b 100644
--- a/probe_dynamics.py
+++ b/probe_dynamics.py
@@ -83,6 +83,7 @@ def ram_center(seed):
   83     83                  obs[16:18].copy(),
   84     84                  obs[0:2].copy(),
   85     85                  obs[3:6].copy(),
          86 +                float(obs[2]),
   86     87              )
   87     88          if first_contact is not None and step in {
   88     89              first_contact[0],
@@ -103,12 +104,19 @@ def ram_center(seed):
  103    104              break
  104    105      fc = None
  105    106      if first_contact:
         107 +        contact_delta = first_contact[2] - first_contact[3]
         108 +        c, s = math.cos(first_contact[5]), math.sin(first_contact[5])
         109 +        local_contact = np.array(
         110 +            [c * contact_delta[0] + s * contact_delta[1],
         111 +             -s * contact_delta[0] + c * contact_delta[1]]
         112 +        )
  106    113          fc = (
  107    114              first_contact[0],
  108    115              round(first_contact[1], 5),
  109    116              np.round(first_contact[2], 5).tolist(),
  110    117              np.round(first_contact[3], 5).tolist(),
  111    118              np.round(first_contact[4], 5).tolist(),
         119 +            np.round(local_contact, 5).tolist(),
  112    120          )
  113    121      pretty_samples = [
  114    122          (s, np.round(d, 5).tolist(), round(a, 5), np.round(r, 5).tolist())
```

</details>

<a id="C009"></a>
### C009 · respect hidden radial action displacement limit

Commit `139de8447713be3b13375f5c869d3a7f7f60509f`; parents: aec5753c685e074fc609de5686c7b36264c28278. Recorded author date: 2026-09-09T08:27:05+02:00.

File roles (automatic): support code (role needs review).

[Exact all-file diff](evidence/diffs/C009_139de84.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/candidate_strategy.py b/candidate_strategy.py
index cc1fffa..ba2bb5c 100644
--- a/candidate_strategy.py
+++ b/candidate_strategy.py
@@ -28,7 +28,13 @@ class CandidateStrategy:
   28     28          return v / n if n > 1e-9 else np.zeros(2)
   29     29  
   30     30      def _move(self, robot, target, gain=1.0):
   31        -        return np.clip((target - robot) * gain, self.low, self.high)
          31 +        # The server also enforces a Euclidean displacement cap despite the Box
          32 +        # metadata being per-axis, so diagonal commands must be normalized.
          33 +        action = np.clip((target - robot) * gain, self.low, self.high)
          34 +        norm = float(np.linalg.norm(action))
          35 +        if norm > 0.049:
          36 +            action *= 0.049 / norm
          37 +        return action
   32     38  
   33     39      def _select(self, s):
   34     40          c = s[0:2]
```

</details>

<a id="C010"></a>
### C010 · Use persistent staged contact for center pushes

Commit `587c5c3909f4d50fddeec7b4929fccff2c9e7e6c`; parents: 139de8447713be3b13375f5c869d3a7f7f60509f. Recorded author date: 2026-09-09T08:27:13+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0030](01_timeline.md#E0030): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_587c5c3_approach.py) · [Exact all-file diff](evidence/diffs/C010_587c5c3.diff)

[Previous saved controller snapshot](evidence/versions/C004_7cc31b7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4dad70d..61c2bea 100644
--- a/approach.py
+++ b/approach.py
@@ -10,6 +10,8 @@ class GeneratedApproach:
   10     10  
   11     11      def reset(self, state, info):
   12     12          self.step = 0
          13 +        self.mode = "approach"
          14 +        self.push_dir = None
   13     15  
   14     16      def get_action(self, state):
   15     17          s = np.asarray(state, dtype=float)
@@ -22,9 +24,21 @@ class GeneratedApproach:
   22     24              direction = delta / dist
   23     25          else:
   24     26              direction = np.array([1.0, 0.0])
   25        -        # First get behind the object, then push through its centre.
   26        -        stand = obj - direction * 0.16
   27        -        target = stand if np.linalg.norm(robot - stand) > 0.055 else obj + direction * 0.10
          27 +        if self.push_dir is None:
          28 +            self.push_dir = direction.copy()
          29 +        if self.mode == "approach":
          30 +            self.push_dir = direction.copy()
          31 +            # Outside the T's roughly 0.6 radius bounding box.
          32 +            stand = obj - self.push_dir * 0.78
          33 +            target = stand
          34 +            if np.linalg.norm(robot - stand) < 0.045:
          35 +                self.mode = "push"
          36 +        else:
          37 +            # Aim through the centre and keep contact rather than oscillating
          38 +            # between the moving staging point and the object.
          39 +            target = obj + self.push_dir * 0.25
          40 +            if np.dot(delta, self.push_dir) < -0.04:
          41 +                self.mode = "approach"
   28     42          action = np.clip(target - robot, self.low, self.high)
   29     43          # The robot has a Euclidean displacement cap in addition to Box bounds.
   30     44          norm = float(np.linalg.norm(action))
diff --git a/explore_geometry.py b/explore_geometry.py
index c19a815..5cb88ca 100644
--- a/explore_geometry.py
+++ b/explore_geometry.py
@@ -29,7 +29,9 @@ def drive_to(env, state, target, max_steps=100):
   29     29          delta = np.asarray(target) - state[16:18]
   30     30          if np.linalg.norm(delta) < 0.006:
   31     31              break
   32        -        action = np.clip(delta, -0.05, 0.05)
          32 +        # The server additionally enforces a Euclidean speed cap near 0.05.
          33 +        norm = np.linalg.norm(delta)
          34 +        action = delta * min(1.0, 0.049 / max(norm, 1e-12))
   33     35          state, _, done, trunc, _ = env.step(action)
   34     36          if done or trunc:
   35     37              break
```

</details>

<a id="C011"></a>
### C011 · log candidate trajectories for controller diagnosis

Commit `6c1883497288a803121dba460f2f55f5b473f03d`; parents: 587c5c3909f4d50fddeec7b4929fccff2c9e7e6c. Recorded author date: 2026-09-09T08:27:30+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C011_6c18834.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_candidate_strategy.py b/test_candidate_strategy.py
index 439d104..24f8711 100644
--- a/test_candidate_strategy.py
+++ b/test_candidate_strategy.py
@@ -19,7 +19,9 @@ def run(seed, verbose=False):
   19     19              raise
   20     20          if verbose and (step % 100 == 99 or term or trunc):
   21     21              ae = (obs[31] - obs[2] + np.pi) % (2*np.pi) - np.pi
   22        -            print(seed, step + 1, policy.mode, policy.phase, "poserr", round(float(np.linalg.norm(obs[29:31]-obs[0:2])), 3), "angerr", round(float(ae), 3))
          22 +            print(seed, step + 1, policy.mode, policy.phase, "block", np.round(obs[0:3], 2),
          23 +                  "robot", np.round(obs[16:18], 2), "poserr", round(float(np.linalg.norm(obs[29:31]-obs[0:2])), 3),
          24 +                  "angerr", round(float(ae), 3))
   23     25          if term or trunc:
   24     26              break
   25     27      env.close()
```

</details>

<a id="C012"></a>
### C012 · Probe tangential rotation control after contact

Commit `a7d8ac7b6c499449ab3abd823e6c1ceb5680cab1`; parents: 6c1883497288a803121dba460f2f55f5b473f03d. Recorded author date: 2026-09-09T08:27:55+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C012_a7d8ac7.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dynamics.py b/probe_dynamics.py
index 3c8404b..93810ab 100644
--- a/probe_dynamics.py
+++ b/probe_dynamics.py
@@ -166,6 +166,41 @@ def coast_after_push(seed):
  166    166      env.close()
  167    167  
  168    168  
         169 +def tangent_at_contact(seed, tangent_sign):
         170 +    """Reach first contact, then combine inward and tangential robot motion."""
         171 +    env = make_env()
         172 +    obs, _ = env.reset(seed=seed)
         173 +    initial = obs.copy()
         174 +    contact_state = None
         175 +    for _ in range(100):
         176 +        vec = obs[0:2] - obs[16:18]
         177 +        act = 0.049 * vec / max(float(np.linalg.norm(vec)), 1e-9)
         178 +        obs, _, term, trunc, _ = env.step(act.astype(np.float32))
         179 +        if np.linalg.norm(obs[0:2] - initial[0:2]) > 1e-5:
         180 +            contact_state = obs.copy()
         181 +            break
         182 +        if term or trunc:
         183 +            break
         184 +    if contact_state is not None:
         185 +        for _ in range(10):
         186 +            inward = obs[0:2] - obs[16:18]
         187 +            inward /= max(float(np.linalg.norm(inward)), 1e-9)
         188 +            tangent = tangent_sign * np.array([-inward[1], inward[0]])
         189 +            act = 0.034 * inward + 0.034 * tangent
         190 +            obs, _, term, trunc, _ = env.step(act.astype(np.float32))
         191 +            if term or trunc:
         192 +                break
         193 +        result = (
         194 +            np.round(obs[0:2] - contact_state[0:2], 5).tolist(),
         195 +            round(angle_wrap(float(obs[2] - contact_state[2])), 5),
         196 +            np.round(obs[16:18] - contact_state[16:18], 5).tolist(),
         197 +        )
         198 +    else:
         199 +        result = None
         200 +    print("TANGENT", seed, tangent_sign, result)
         201 +    env.close()
         202 +
         203 +
  169    204  if __name__ == "__main__":
  170    205      env = make_env()
  171    206      print("SPACES", env.observation_space.shape, env.action_space.low, env.action_space.high)
@@ -175,3 +210,6 @@ if __name__ == "__main__":
  175    210          free_motion(probe_seed)
  176    211          ram_center(probe_seed)
  177    212      coast_after_push(0)
         213 +    for probe_seed in (0, 1):
         214 +        tangent_at_contact(probe_seed, -1)
         215 +        tangent_at_contact(probe_seed, 1)
```

</details>

<a id="C013"></a>
### C013 · Add stem-tip rotation strokes and COM-aligned translation

Commit `8d291ba744be2fae3afbfcc7de9a8b3da144e560`; parents: a7d8ac7b6c499449ab3abd823e6c1ceb5680cab1. Recorded author date: 2026-09-09T08:28:07+02:00.

File roles (automatic): policy.

- [E0034](01_timeline.md#E0034): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_8d291ba_approach.py) · [Exact all-file diff](evidence/diffs/C013_8d291ba.diff)

[Previous saved controller snapshot](evidence/versions/C010_587c5c3_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 61c2bea..b54f1d2 100644
--- a/approach.py
+++ b/approach.py
@@ -10,33 +10,59 @@ class GeneratedApproach:
   10     10  
   11     11      def reset(self, state, info):
   12     12          self.step = 0
   13        -        self.mode = "approach"
          13 +        self.mode = "rotate_approach"
   14     14          self.push_dir = None
          15 +        self.stroke_theta = 0.0
   15     16  
   16     17      def get_action(self, state):
   17     18          s = np.asarray(state, dtype=float)
   18     19          obj = s[0:2]
   19     20          robot = s[16:18]
   20     21          goal = s[29:31]
          22 +        theta = float(s[2])
          23 +        goal_theta = float(s[31])
          24 +        angle_error = (goal_theta - theta + math.pi) % (2.0 * math.pi) - math.pi
   21     25          delta = goal - obj
   22     26          dist = float(np.linalg.norm(delta))
   23     27          if dist > 1e-9:
   24     28              direction = delta / dist
   25     29          else:
   26     30              direction = np.array([1.0, 0.0])
   27        -        if self.push_dir is None:
          31 +        width, lh, lv = map(float, s[12:15])
          32 +        c, sn = math.cos(theta), math.sin(theta)
          33 +        # Stem runs along local -y.  Its tip gives a large moment arm.
          34 +        stem_dir = np.array([sn, -c])
          35 +        tip = obj + stem_dir * (lv - width * 0.5)
          36 +        turn = 1.0 if angle_error > 0.0 else -1.0
          37 +        tangent = np.array([-stem_dir[1], stem_dir[0]]) * turn
          38 +
          39 +        if self.mode.startswith("rotate") and abs(angle_error) < 0.075:
          40 +            self.mode = "approach"
   28     41              self.push_dir = direction.copy()
   29        -        if self.mode == "approach":
          42 +
          43 +        if self.mode == "rotate_approach":
          44 +            target = tip - tangent * 0.24
          45 +            if np.linalg.norm(robot - target) < 0.045:
          46 +                self.mode = "rotate_push"
          47 +                self.stroke_theta = theta
          48 +        elif self.mode == "rotate_push":
          49 +            target = tip + tangent * 0.35
          50 +            turned = abs((theta - self.stroke_theta + math.pi) % (2*math.pi) - math.pi)
          51 +            if turned > 0.25 or np.linalg.norm(robot - tip) > 0.55:
          52 +                self.mode = "rotate_approach"
          53 +        elif self.mode == "approach":
   30     54              self.push_dir = direction.copy()
   31        -            # Outside the T's roughly 0.6 radius bounding box.
   32        -            stand = obj - self.push_dir * 0.78
          55 +            # Approximate COM is down the stem; pushing through it reduces spin.
          56 +            com = obj + stem_dir * (0.22 * lv)
          57 +            stand = com - self.push_dir * 1.05
   33     58              target = stand
   34     59              if np.linalg.norm(robot - stand) < 0.045:
   35     60                  self.mode = "push"
   36     61          else:
   37     62              # Aim through the centre and keep contact rather than oscillating
   38     63              # between the moving staging point and the object.
   39        -            target = obj + self.push_dir * 0.25
          64 +            com = obj + stem_dir * (0.22 * lv)
          65 +            target = com + self.push_dir * 0.30
   40     66              if np.dot(delta, self.push_dir) < -0.04:
   41     67                  self.mode = "approach"
   42     68          action = np.clip(target - robot, self.low, self.high)
```

</details>

<a id="C014"></a>
### C014 · shorten rotation bursts and handle arena-edge setup paths

Commit `ac1accf0c2087cfad250299b612753824fcc06dd`; parents: 8d291ba744be2fae3afbfcc7de9a8b3da144e560. Recorded author date: 2026-09-09T08:28:13+02:00.

File roles (automatic): support code (role needs review).

[Exact all-file diff](evidence/diffs/C014_ac1accf.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/candidate_strategy.py b/candidate_strategy.py
index ba2bb5c..b32a766 100644
--- a/candidate_strategy.py
+++ b/candidate_strategy.py
@@ -61,7 +61,7 @@ class CandidateStrategy:
   61     61              force = self._unit(np.asarray(s[29:31]) - c)
   62     62              # Contact somewhere on the rear-facing support surface.
   63     63              contact = c - force * 0.52
   64        -            setup = c - force * 0.83
          64 +            setup = c - force * 0.64
   65     65          else:
   66     66              th = float(s[2])
   67     67              ex = np.array([math.cos(th), math.sin(th)])
@@ -81,7 +81,7 @@ class CandidateStrategy:
   81     81  
   82     82          # Use a collision-free polar repositioning maneuver around the object.
   83     83          ray = self._unit(setup - c)
   84        -        radius = 0.88
          84 +        radius = 0.70
   85     85          rvec = robot - c
   86     86          rdist = float(np.linalg.norm(rvec))
   87     87          rang = math.atan2(rvec[1], rvec[0])
@@ -104,6 +104,7 @@ class CandidateStrategy:
  104    104                  # A look-ahead point gives smooth travel around the clearance circle.
  105    105                  stepang = rang + max(-0.35, min(0.35, adiff))
  106    106                  waypoint = c + radius * np.array([math.cos(stepang), math.sin(stepang)])
         107 +                waypoint = np.clip(waypoint, 0.12, 4.88)
  107    108                  return self._move(robot, waypoint)
  108    109  
  109    110          if self.phase == "approach":
@@ -116,7 +117,7 @@ class CandidateStrategy:
  116    117          if self.phase == "push":
  117    118              ae = wrap_angle(float(s[31] - s[2]))
  118    119              pe = float(np.linalg.norm(s[29:31] - c))
  119        -            done = ((self.mode == "rotate" and (abs(ae) < 0.065 or self.ticks > 55)) or
         120 +            done = ((self.mode == "rotate" and (abs(ae) < 0.065 or self.ticks > 7)) or
  120    121                      (self.mode == "translate" and (pe < 0.020 or abs(ae) > 0.16 or self.ticks > 90)))
  121    122              if done:
  122    123                  self.phase = "select"
```

</details>

<a id="C015"></a>
### C015 · Add concise mode trajectory diagnostics

Commit `f6f942e9838001d28a22b025c5f28cba68f32d5e`; parents: ac1accf0c2087cfad250299b612753824fcc06dd. Recorded author date: 2026-09-09T08:28:29+02:00.

File roles (automatic): diagnostic/test.

- [E0038](01_timeline.md#E0038): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C015_f6f942e.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index 4956428..9521ace 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -12,6 +12,9 @@ def run(seed, verbose=False):
   12     12      initial = obs.copy()
   13     13      for step in range(env.max_steps):
   14     14          obs, reward, term, trunc, info = env.step(policy.get_action(obs))
          15 +        if verbose and step % 50 == 0:
          16 +            print(' ', step, policy.mode, 'pose', np.round(obs[:3], 3),
          17 +                  'robot', np.round(obs[16:18], 3))
   15     18          if term or trunc:
   16     19              break
   17     20      env.close()
@@ -24,5 +27,5 @@ def run(seed, verbose=False):
   24     27  
   25     28  if __name__ == '__main__':
   26     29      seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
   27        -    results = [run(s) for s in seeds]
          30 +    results = [run(s, verbose=len(seeds) == 1) for s in seeds]
   28     31      print('success', sum(x[0] for x in results), '/', len(results))
```

</details>

<a id="C016"></a>
### C016 · Interleave pose correction and keep staging targets reachable

Commit `7c95c0c0ee9cb8fe918b697886c7b9a37f6694b5`; parents: f6f942e9838001d28a22b025c5f28cba68f32d5e. Recorded author date: 2026-09-09T08:29:06+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0042](01_timeline.md#E0042): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_7c95c0c_approach.py) · [Exact all-file diff](evidence/diffs/C016_7c95c0c.diff)

[Previous saved controller snapshot](evidence/versions/C013_8d291ba_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b54f1d2..c42469d 100644
--- a/approach.py
+++ b/approach.py
@@ -36,9 +36,11 @@ class GeneratedApproach:
   36     36          turn = 1.0 if angle_error > 0.0 else -1.0
   37     37          tangent = np.array([-stem_dir[1], stem_dir[0]]) * turn
   38     38  
   39        -        if self.mode.startswith("rotate") and abs(angle_error) < 0.075:
          39 +        if self.mode.startswith("rotate") and abs(angle_error) < 0.065:
   40     40              self.mode = "approach"
   41     41              self.push_dir = direction.copy()
          42 +        elif not self.mode.startswith("rotate") and abs(angle_error) > 0.16:
          43 +            self.mode = "rotate_approach"
   42     44  
   43     45          if self.mode == "rotate_approach":
   44     46              target = tip - tangent * 0.24
@@ -54,7 +56,8 @@ class GeneratedApproach:
   54     56              self.push_dir = direction.copy()
   55     57              # Approximate COM is down the stem; pushing through it reduces spin.
   56     58              com = obj + stem_dir * (0.22 * lv)
   57        -            stand = com - self.push_dir * 1.05
          59 +            stand = com - self.push_dir * 0.78
          60 +            stand = np.clip(stand, 0.13, 4.87)
   58     61              target = stand
   59     62              if np.linalg.norm(robot - stand) < 0.045:
   60     63                  self.mode = "push"
diff --git a/candidate_strategy.py b/candidate_strategy.py
index b32a766..209d428 100644
--- a/candidate_strategy.py
+++ b/candidate_strategy.py
@@ -27,13 +27,13 @@ class CandidateStrategy:
   27     27          n = float(np.linalg.norm(v))
   28     28          return v / n if n > 1e-9 else np.zeros(2)
   29     29  
   30        -    def _move(self, robot, target, gain=1.0):
          30 +    def _move(self, robot, target, gain=1.0, maxnorm=0.049):
   31     31          # The server also enforces a Euclidean displacement cap despite the Box
   32     32          # metadata being per-axis, so diagonal commands must be normalized.
   33     33          action = np.clip((target - robot) * gain, self.low, self.high)
   34     34          norm = float(np.linalg.norm(action))
   35        -        if norm > 0.049:
   36        -            action *= 0.049 / norm
          35 +        if norm > maxnorm:
          36 +            action *= maxnorm / norm
   37     37          return action
   38     38  
   39     39      def _select(self, s):
@@ -117,13 +117,16 @@ class CandidateStrategy:
  117    117          if self.phase == "push":
  118    118              ae = wrap_angle(float(s[31] - s[2]))
  119    119              pe = float(np.linalg.norm(s[29:31] - c))
  120        -            done = ((self.mode == "rotate" and (abs(ae) < 0.065 or self.ticks > 7)) or
  121        -                    (self.mode == "translate" and (pe < 0.020 or abs(ae) > 0.16 or self.ticks > 90)))
         120 +            omega = float(s[5])
         121 +            done = ((self.mode == "rotate" and
         122 +                     (abs(ae) < 0.075 or omega * self.side > 0.12 or self.ticks > 4)) or
         123 +                    (self.mode == "translate" and
         124 +                     (pe < 0.020 or abs(ae) > 0.14 or self.ticks > 35)))
  122    125              if done:
  123    126                  self.phase = "select"
  124    127              # Aim through the selected contact, then continue in the desired force direction.
  125    128              aim = contact + force * 0.35
  126        -            return self._move(robot, aim)
         129 +            return self._move(robot, aim, maxnorm=(0.006 if self.mode == "rotate" else 0.010))
  127    130  
  128    131          return np.zeros(2)
  129    132  
```

</details>

<a id="C017"></a>
### C017 · Select accessible T endpoint for rotation contacts

Commit `00a41508709fa172f306183bfa5a2323d9015c6c`; parents: 7c95c0c0ee9cb8fe918b697886c7b9a37f6694b5. Recorded author date: 2026-09-09T08:29:43+02:00.

File roles (automatic): policy.

- [E0046](01_timeline.md#E0046): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_00a4150_approach.py) · [Exact all-file diff](evidence/diffs/C017_00a4150.diff)

[Previous saved controller snapshot](evidence/versions/C016_7c95c0c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c42469d..62434d5 100644
--- a/approach.py
+++ b/approach.py
@@ -13,6 +13,7 @@ class GeneratedApproach:
   13     13          self.mode = "rotate_approach"
   14     14          self.push_dir = None
   15     15          self.stroke_theta = 0.0
          16 +        self.lever_local = None
   16     17  
   17     18      def get_action(self, state):
   18     19          s = np.asarray(state, dtype=float)
@@ -30,17 +31,34 @@ class GeneratedApproach:
   30     31              direction = np.array([1.0, 0.0])
   31     32          width, lh, lv = map(float, s[12:15])
   32     33          c, sn = math.cos(theta), math.sin(theta)
   33        -        # Stem runs along local -y.  Its tip gives a large moment arm.
          34 +        # Stem runs along local -y.  Use whichever of its tip or the two cap
          35 +        # ends offers an accessible tangential rotation contact.
   34     36          stem_dir = np.array([sn, -c])
   35        -        tip = obj + stem_dir * (lv - width * 0.5)
   36     37          turn = 1.0 if angle_error > 0.0 else -1.0
   37        -        tangent = np.array([-stem_dir[1], stem_dir[0]]) * turn
          38 +
          39 +        if self.mode == "rotate_approach" and self.lever_local is None:
          40 +            local_options = [np.array([0.0, -(lv - width * 0.5)]),
          41 +                             np.array([lh * 0.5 - width * 0.5, 0.0]),
          42 +                             np.array([-lh * 0.5 + width * 0.5, 0.0])]
          43 +            def clearance(local):
          44 +                r = np.array([c*local[0] - sn*local[1],
          45 +                              sn*local[0] + c*local[1]])
          46 +                f = np.array([-r[1], r[0]]) * turn / np.linalg.norm(r)
          47 +                stage = obj + r - f * 0.24
          48 +                return min(stage[0] - 0.11, 4.89 - stage[0],
          49 +                           stage[1] - 0.11, 4.89 - stage[1])
          50 +            self.lever_local = max(local_options, key=clearance)
          51 +        local = self.lever_local if self.lever_local is not None else np.array([0.0, -lv])
          52 +        lever = np.array([c*local[0] - sn*local[1], sn*local[0] + c*local[1]])
          53 +        tip = obj + lever
          54 +        tangent = np.array([-lever[1], lever[0]]) * turn / np.linalg.norm(lever)
   38     55  
   39     56          if self.mode.startswith("rotate") and abs(angle_error) < 0.065:
   40     57              self.mode = "approach"
   41     58              self.push_dir = direction.copy()
   42     59          elif not self.mode.startswith("rotate") and abs(angle_error) > 0.16:
   43     60              self.mode = "rotate_approach"
          61 +            self.lever_local = None
   44     62  
   45     63          if self.mode == "rotate_approach":
   46     64              target = tip - tangent * 0.24
@@ -52,6 +70,7 @@ class GeneratedApproach:
   52     70              turned = abs((theta - self.stroke_theta + math.pi) % (2*math.pi) - math.pi)
   53     71              if turned > 0.25 or np.linalg.norm(robot - tip) > 0.55:
   54     72                  self.mode = "rotate_approach"
          73 +                self.lever_local = None
   55     74          elif self.mode == "approach":
   56     75              self.push_dir = direction.copy()
   57     76              # Approximate COM is down the stem; pushing through it reduces spin.
```

</details>

<a id="C018"></a>
### C018 · avoid accidental contact during polar staging

Commit `149554c75e0f3d79234d27728ec51dc81e0a10fa`; parents: 00a41508709fa172f306183bfa5a2323d9015c6c. Recorded author date: 2026-09-09T08:30:14+02:00.

File roles (automatic): support code (role needs review).

[Exact all-file diff](evidence/diffs/C018_149554c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/candidate_strategy.py b/candidate_strategy.py
index 209d428..81cadcb 100644
--- a/candidate_strategy.py
+++ b/candidate_strategy.py
@@ -81,7 +81,9 @@ class CandidateStrategy:
   81     81  
   82     82          # Use a collision-free polar repositioning maneuver around the object.
   83     83          ray = self._unit(setup - c)
   84        -        radius = 0.70
          84 +        # The T's longest corner is about 0.7 from its reference point; less
          85 +        # clearance makes the robot accidentally shove it while repositioning.
          86 +        radius = 0.88
   85     87          rvec = robot - c
   86     88          rdist = float(np.linalg.norm(rvec))
   87     89          rang = math.atan2(rvec[1], rvec[0])
@@ -102,8 +104,13 @@ class CandidateStrategy:
  102    104                  self.phase = "approach"
  103    105              else:
  104    106                  # A look-ahead point gives smooth travel around the clearance circle.
  105        -                stepang = rang + max(-0.35, min(0.35, adiff))
         107 +                direction = 1.0 if adiff > 0 else -1.0
         108 +                stepang = rang + direction * min(0.25, abs(adiff))
  106    109                  waypoint = c + radius * np.array([math.cos(stepang), math.sin(stepang)])
         110 +                # If the short arc runs into a wall, take the long way around.
         111 +                if np.any(waypoint < 0.12) or np.any(waypoint > 4.88):
         112 +                    stepang = rang - direction * 0.25
         113 +                    waypoint = c + radius * np.array([math.cos(stepang), math.sin(stepang)])
  107    114                  waypoint = np.clip(waypoint, 0.12, 4.88)
  108    115                  return self._move(robot, waypoint)
  109    116  
```

</details>

<a id="C019"></a>
### C019 · stage low-impulse rotation strokes directly at contact

Commit `f1d882cbb01e9c61ccdc8a4c239b01793eccb3d1`; parents: 149554c75e0f3d79234d27728ec51dc81e0a10fa. Recorded author date: 2026-09-09T08:30:57+02:00.

File roles (automatic): support code (role needs review).

[Exact all-file diff](evidence/diffs/C019_f1d882c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/candidate_strategy.py b/candidate_strategy.py
index 81cadcb..f47c503 100644
--- a/candidate_strategy.py
+++ b/candidate_strategy.py
@@ -69,7 +69,9 @@ class CandidateStrategy:
   69     69              # Push tangentially on the positive local-x end. side is torque sign.
   70     70              contact = c + ex * (0.40 * float(s[13]))
   71     71              force = ey * self.side
   72        -            setup = contact - force * 0.30
          72 +            # Robot-center staging point: one radius plus a small margin behind
          73 +            # the intended material contact point.
          74 +            setup = contact - force * 0.12
   73     75          return c, robot, contact, setup, force
   74     76  
   75     77      def get_action(self, state):
@@ -126,13 +128,13 @@ class CandidateStrategy:
  126    128              pe = float(np.linalg.norm(s[29:31] - c))
  127    129              omega = float(s[5])
  128    130              done = ((self.mode == "rotate" and
  129        -                     (abs(ae) < 0.075 or omega * self.side > 0.12 or self.ticks > 4)) or
         131 +                     (abs(ae) < 0.075 or omega * self.side > 0.12 or self.ticks > 8)) or
  130    132                      (self.mode == "translate" and
  131    133                       (pe < 0.020 or abs(ae) > 0.14 or self.ticks > 35)))
  132    134              if done:
  133    135                  self.phase = "select"
  134    136              # Aim through the selected contact, then continue in the desired force direction.
  135        -            aim = contact + force * 0.35
         137 +            aim = contact + force * 0.10
  136    138              return self._move(robot, aim, maxnorm=(0.006 if self.mode == "rotate" else 0.010))
  137    139  
  138    140          return np.zeros(2)
```

</details>

<a id="C020"></a>
### C020 · Replace controller with bounded stem rotation and COM translation strokes

Commit `5f07c8605dfc9d58e6491c47557bd53d1b9fedb6`; parents: f1d882cbb01e9c61ccdc8a4c239b01793eccb3d1. Recorded author date: 2026-09-09T08:33:48+02:00.

File roles (automatic): policy.

- [E0057](01_timeline.md#E0057): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_5f07c86_approach.py) · [Exact all-file diff](evidence/diffs/C020_5f07c86.diff)

[Previous saved controller snapshot](evidence/versions/C017_00a4150_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 62434d5..d169e4b 100644
--- a/approach.py
+++ b/approach.py
@@ -3,94 +3,103 @@ import numpy as np
    3      3  
    4      4  
    5      5  class GeneratedApproach:
           6 +    """Closed-loop contact controller for the asymmetric T pusher."""
    6      7      def __init__(self, action_space, observation_space, primitives):
    7      8          self.low = np.asarray(action_space.low, dtype=float)
    8      9          self.high = np.asarray(action_space.high, dtype=float)
    9     10          self.reset(None, None)
   10     11  
   11     12      def reset(self, state, info):
   12        -        self.step = 0
   13        -        self.mode = "rotate_approach"
   14        -        self.push_dir = None
   15        -        self.stroke_theta = 0.0
   16        -        self.lever_local = None
          13 +        self.mode = "choose"
          14 +        self.count = 0
          15 +        self.turn_sign = 1.0
          16 +        self.push_dir = np.array([1.0, 0.0])
          17 +        self.start_pose = np.zeros(3)
          18 +
          19 +    @staticmethod
          20 +    def _angle(x):
          21 +        return (x + math.pi) % (2.0 * math.pi) - math.pi
          22 +
          23 +    @staticmethod
          24 +    def _world(local, theta):
          25 +        c, sn = math.cos(theta), math.sin(theta)
          26 +        return np.array([c*local[0] - sn*local[1], sn*local[0] + c*local[1]])
          27 +
          28 +    def _safe(self, delta, speed=0.049):
          29 +        a = np.asarray(delta, dtype=float)
          30 +        n = float(np.linalg.norm(a))
          31 +        if n > speed:
          32 +            a *= speed / n
          33 +        return np.clip(a, self.low, self.high).astype(float)
   17     34  
   18     35      def get_action(self, state):
   19     36          s = np.asarray(state, dtype=float)
   20        -        obj = s[0:2]
   21        -        robot = s[16:18]
   22        -        goal = s[29:31]
   23        -        theta = float(s[2])
   24        -        goal_theta = float(s[31])
   25        -        angle_error = (goal_theta - theta + math.pi) % (2.0 * math.pi) - math.pi
   26        -        delta = goal - obj
   27        -        dist = float(np.linalg.norm(delta))
   28        -        if dist > 1e-9:
   29        -            direction = delta / dist
   30        -        else:
   31        -            direction = np.array([1.0, 0.0])
          37 +        obj, robot, goal = s[0:2], s[16:18], s[29:31]
          38 +        theta, goal_theta = float(s[2]), float(s[31])
   32     39          width, lh, lv = map(float, s[12:15])
   33        -        c, sn = math.cos(theta), math.sin(theta)
   34        -        # Stem runs along local -y.  Use whichever of its tip or the two cap
   35        -        # ends offers an accessible tangential rotation contact.
   36        -        stem_dir = np.array([sn, -c])
   37        -        turn = 1.0 if angle_error > 0.0 else -1.0
          40 +        ae = self._angle(goal_theta - theta)
          41 +        dp = goal - obj
          42 +        pd = float(np.linalg.norm(dp))
   38     43  
   39        -        if self.mode == "rotate_approach" and self.lever_local is None:
   40        -            local_options = [np.array([0.0, -(lv - width * 0.5)]),
   41        -                             np.array([lh * 0.5 - width * 0.5, 0.0]),
   42        -                             np.array([-lh * 0.5 + width * 0.5, 0.0])]
   43        -            def clearance(local):
   44        -                r = np.array([c*local[0] - sn*local[1],
   45        -                              sn*local[0] + c*local[1]])
   46        -                f = np.array([-r[1], r[0]]) * turn / np.linalg.norm(r)
   47        -                stage = obj + r - f * 0.24
   48        -                return min(stage[0] - 0.11, 4.89 - stage[0],
   49        -                           stage[1] - 0.11, 4.89 - stage[1])
   50        -            self.lever_local = max(local_options, key=clearance)
   51        -        local = self.lever_local if self.lever_local is not None else np.array([0.0, -lv])
   52        -        lever = np.array([c*local[0] - sn*local[1], sn*local[0] + c*local[1]])
   53        -        tip = obj + lever
   54        -        tangent = np.array([-lever[1], lever[0]]) * turn / np.linalg.norm(lever)
          44 +        if self.mode == "choose":
          45 +            if abs(ae) > 0.075:
          46 +                self.turn_sign = 1.0 if ae > 0.0 else -1.0
          47 +                self.mode = "rot_far"
          48 +            elif pd > 0.018:
          49 +                self.push_dir = dp / max(pd, 1e-9)
          50 +                self.mode = "move_far"
          51 +            else:
          52 +                return np.zeros(2, dtype=float)
          53 +            self.count = 0
          54 +            self.start_pose = np.array([obj[0], obj[1], theta])
   55     55  
   56        -        if self.mode.startswith("rotate") and abs(angle_error) < 0.065:
   57        -            self.mode = "approach"
   58        -            self.push_dir = direction.copy()
   59        -        elif not self.mode.startswith("rotate") and abs(angle_error) > 0.16:
   60        -            self.mode = "rotate_approach"
   61        -            self.lever_local = None
          56 +        if self.mode.startswith("rot"):
          57 +            # Distal-stem side contact is a reliable long rotation lever.
          58 +            side = -self.turn_sign
          59 +            far_local = np.array([side * (width * 0.5 + 0.34), -0.72 * lv])
          60 +            contact_local = np.array([side * (width * 0.5 + 0.115), -0.72 * lv])
          61 +            far = obj + self._world(far_local, theta)
          62 +            contact = obj + self._world(contact_local, theta)
          63 +            force = self._world(np.array([self.turn_sign, 0.0]), theta)
          64 +            if self.mode == "rot_far":
          65 +                if np.linalg.norm(robot - far) < 0.035:
          66 +                    self.mode = "rot_contact"
          67 +                return self._safe(far - robot)
          68 +            if self.mode == "rot_contact":
          69 +                if np.linalg.norm(robot - contact) < 0.018:
          70 +                    self.mode = "rot_push"
          71 +                    self.count = 0
          72 +                    self.start_pose = np.array([obj[0], obj[1], theta])
          73 +                return self._safe(contact - robot, 0.025)
          74 +            if self.mode == "rot_push":
          75 +                self.count += 1
          76 +                current_ae = self._angle(goal_theta - theta)
          77 +                turned = abs(self._angle(theta - self.start_pose[2]))
          78 +                if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
          79 +                        or turned > 0.16 or self.count >= 10):
          80 +                    self.mode = "rot_retreat"
          81 +                return self._safe(force, 0.016)
          82 +            if np.linalg.norm(robot - far) < 0.04:
          83 +                self.mode = "choose"
          84 +            return self._safe(far - robot, 0.035)
   62     85  
   63        -        if self.mode == "rotate_approach":
   64        -            target = tip - tangent * 0.24
   65        -            if np.linalg.norm(robot - target) < 0.045:
   66        -                self.mode = "rotate_push"
   67        -                self.stroke_theta = theta
   68        -        elif self.mode == "rotate_push":
   69        -            target = tip + tangent * 0.35
   70        -            turned = abs((theta - self.stroke_theta + math.pi) % (2*math.pi) - math.pi)
   71        -            if turned > 0.25 or np.linalg.norm(robot - tip) > 0.55:
   72        -                self.mode = "rotate_approach"
   73        -                self.lever_local = None
   74        -        elif self.mode == "approach":
   75        -            self.push_dir = direction.copy()
   76        -            # Approximate COM is down the stem; pushing through it reduces spin.
   77        -            com = obj + stem_dir * (0.22 * lv)
   78        -            stand = com - self.push_dir * 0.78
   79        -            stand = np.clip(stand, 0.13, 4.87)
   80        -            target = stand
   81        -            if np.linalg.norm(robot - stand) < 0.045:
   82        -                self.mode = "push"
   83        -        else:
   84        -            # Aim through the centre and keep contact rather than oscillating
   85        -            # between the moving staging point and the object.
   86        -            com = obj + stem_dir * (0.22 * lv)
   87        -            target = com + self.push_dir * 0.30
   88        -            if np.dot(delta, self.push_dir) < -0.04:
   89        -                self.mode = "approach"
   90        -        action = np.clip(target - robot, self.low, self.high)
   91        -        # The robot has a Euclidean displacement cap in addition to Box bounds.
   92        -        norm = float(np.linalg.norm(action))
   93        -        if norm > 0.049:
   94        -            action *= 0.049 / norm
   95        -        self.step += 1
   96        -        return action.astype(float)
          86 +        # The effective COM lies down the stem from the reported junction.
          87 +        com = obj + self._world(np.array([0.0, -0.36 * lv]), theta)
          88 +        far = com - self.push_dir * 0.82
          89 +        if self.mode == "move_far":
          90 +            if np.linalg.norm(robot - far) < 0.035:
          91 +                self.mode = "move_push"
          92 +                self.count = 0
          93 +                self.start_pose = np.array([obj[0], obj[1], theta])
          94 +            return self._safe(far - robot)
          95 +        if self.mode == "move_push":
          96 +            self.count += 1
          97 +            moved = float(np.linalg.norm(obj - self.start_pose[:2]))
          98 +            now_ae = abs(self._angle(goal_theta - theta))
          99 +            if moved > 0.14 or self.count >= 18 or now_ae > 0.13:
         100 +                self.mode = "move_retreat"
         101 +            speed = 0.012 if pd < 0.12 else 0.025
         102 +            return self._safe((com + self.push_dir * 0.20) - robot, speed)
         103 +        if np.linalg.norm(robot - far) < 0.04:
         104 +            self.mode = "choose"
         105 +        return self._safe(far - robot, 0.035)
```

</details>

<a id="C021"></a>
### C021 · Route translation setup around T geometry and clamp arena targets

Commit `2bd31ab3280068205dcdbd8afcb97852c1e39939`; parents: 5f07c8605dfc9d58e6491c47557bd53d1b9fedb6. Recorded author date: 2026-09-09T08:35:11+02:00.

File roles (automatic): policy.

- [E0061](01_timeline.md#E0061): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_2bd31ab_approach.py) · [Exact all-file diff](evidence/diffs/C021_2bd31ab.diff)

[Previous saved controller snapshot](evidence/versions/C020_5f07c86_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d169e4b..4aeab0d 100644
--- a/approach.py
+++ b/approach.py
@@ -15,6 +15,7 @@ class GeneratedApproach:
   15     15          self.turn_sign = 1.0
   16     16          self.push_dir = np.array([1.0, 0.0])
   17     17          self.start_pose = np.zeros(3)
          18 +        self.nav = []
   18     19  
   19     20      @staticmethod
   20     21      def _angle(x):
@@ -48,6 +49,23 @@ class GeneratedApproach:
   48     49              elif pd > 0.018:
   49     50                  self.push_dir = dp / max(pd, 1e-9)
   50     51                  self.mode = "move_far"
          52 +                # Route around the cap instead of crossing the T when moving
          53 +                # from a rotation contact to the translation staging side.
          54 +                c, sn = math.cos(theta), math.sin(theta)
          55 +                rel = robot - obj
          56 +                local_robot = np.array([c*rel[0] + sn*rel[1],
          57 +                                        -sn*rel[0] + c*rel[1]])
          58 +                com0 = obj + self._world(np.array([0.0, -0.36*lv]), theta)
          59 +                far0 = np.clip(com0 - self.push_dir*0.82, 0.105, 4.895)
          60 +                frel = far0 - obj
          61 +                far_local = np.array([c*frel[0] + sn*frel[1],
          62 +                                      -sn*frel[0] + c*frel[1]])
          63 +                side0 = 1.0 if local_robot[0] >= 0 else -1.0
          64 +                self.nav = [obj + self._world(np.array([side0*0.76,
          65 +                            min(0.30, max(-0.72*lv, local_robot[1]))]), theta),
          66 +                            obj + self._world(np.array([side0*0.76, 0.30]), theta),
          67 +                            obj + self._world(np.array([far_local[0], 0.30]), theta)]
          68 +                self.nav = [np.clip(p, 0.105, 4.895) for p in self.nav]
   51     69              else:
   52     70                  return np.zeros(2, dtype=float)
   53     71              self.count = 0
@@ -85,8 +103,12 @@ class GeneratedApproach:
   85    103  
   86    104          # The effective COM lies down the stem from the reported junction.
   87    105          com = obj + self._world(np.array([0.0, -0.36 * lv]), theta)
   88        -        far = com - self.push_dir * 0.82
         106 +        far = np.clip(com - self.push_dir * 0.82, 0.105, 4.895)
   89    107          if self.mode == "move_far":
         108 +            while self.nav and np.linalg.norm(robot - self.nav[0]) < 0.045:
         109 +                self.nav.pop(0)
         110 +            if self.nav:
         111 +                return self._safe(self.nav[0] - robot)
   90    112              if np.linalg.norm(robot - far) < 0.035:
   91    113                  self.mode = "move_push"
   92    114                  self.count = 0
```

</details>

<a id="C022"></a>
### C022 · Allow translation strokes to reach the asymmetric outline

Commit `88b437b8fa1488f66f5e2da2efe76c59e3b85397`; parents: 2bd31ab3280068205dcdbd8afcb97852c1e39939. Recorded author date: 2026-09-09T08:35:39+02:00.

File roles (automatic): policy.

- [E0065](01_timeline.md#E0065): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_88b437b_approach.py) · [Exact all-file diff](evidence/diffs/C022_88b437b.diff)

[Previous saved controller snapshot](evidence/versions/C021_2bd31ab_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4aeab0d..c9bccf5 100644
--- a/approach.py
+++ b/approach.py
@@ -118,7 +118,9 @@ class GeneratedApproach:
  118    118              self.count += 1
  119    119              moved = float(np.linalg.norm(obj - self.start_pose[:2]))
  120    120              now_ae = abs(self._angle(goal_theta - theta))
  121        -            if moved > 0.14 or self.count >= 18 or now_ae > 0.13:
         121 +            # Much of the stroke is free travel from the guaranteed-clear
         122 +            # staging radius to the actual outline (especially at the stem).
         123 +            if moved > 0.14 or self.count >= 48 or now_ae > 0.13:
  122    124                  self.mode = "move_retreat"
  123    125              speed = 0.012 if pd < 0.12 else 0.025
  124    126              return self._safe((com + self.push_dir * 0.20) - robot, speed)
```

</details>

<a id="C023"></a>
### C023 · Add fast geometry-aware A-star contact navigation

Commit `3db79a00542e31f7b39a2a78a7f8a90b77b95350`; parents: 88b437b8fa1488f66f5e2da2efe76c59e3b85397. Recorded author date: 2026-09-09T08:37:20+02:00.

File roles (automatic): policy.

- [E0069](01_timeline.md#E0069): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C023_3db79a0_approach.py) · [Exact all-file diff](evidence/diffs/C023_3db79a0.diff)

[Previous saved controller snapshot](evidence/versions/C022_88b437b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c9bccf5..a4329c8 100644
--- a/approach.py
+++ b/approach.py
@@ -1,4 +1,5 @@
    1      1  import math
           2 +import heapq
    2      3  import numpy as np
    3      4  
    4      5  
@@ -33,6 +34,62 @@ class GeneratedApproach:
   33     34              a *= speed / n
   34     35          return np.clip(a, self.low, self.high).astype(float)
   35     36  
          37 +    def _plan(self, start, target, obj, theta, width, lh, lv):
          38 +        """Small A* route for the robot centre around the expanded T."""
          39 +        lo, hi, res = 0.11, 4.89, 0.12
          40 +        n = int((hi-lo)/res) + 1
          41 +        c, sn = math.cos(theta), math.sin(theta)
          42 +        margin = 0.105
          43 +        def blocked(ix, iy):
          44 +            p = np.array([lo + ix*res, lo + iy*res]) - obj
          45 +            x, y = c*p[0] + sn*p[1], -sn*p[0] + c*p[1]
          46 +            bar = abs(x) < lh*0.5+margin and abs(y) < width*0.5+margin
          47 +            stem = abs(x) < width*0.5+margin and -lv-margin < y < width*0.5+margin
          48 +            return bar or stem
          49 +        def node(p):
          50 +            return (max(0, min(n-1, int(round((p[0]-lo)/res)))),
          51 +                    max(0, min(n-1, int(round((p[1]-lo)/res)))))
          52 +        st, gl = node(start), node(np.clip(target, lo, hi))
          53 +        # Pick a nearby free goal lattice point.
          54 +        if blocked(*gl):
          55 +            choices = [(i, j) for i in range(max(0,gl[0]-2),min(n,gl[0]+3))
          56 +                       for j in range(max(0,gl[1]-2),min(n,gl[1]+3)) if not blocked(i,j)]
          57 +            if choices:
          58 +                gl = min(choices, key=lambda q:(q[0]-gl[0])**2+(q[1]-gl[1])**2)
          59 +        heap = [(0.0, st)]
          60 +        cost, parent = {st: 0.0}, {}
          61 +        moves = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
          62 +        while heap:
          63 +            _, cur = heapq.heappop(heap)
          64 +            if cur == gl:
          65 +                break
          66 +            for dx, dy in moves:
          67 +                q = (cur[0]+dx, cur[1]+dy)
          68 +                if not (0 <= q[0] < n and 0 <= q[1] < n) or (q != st and blocked(*q)):
          69 +                    continue
          70 +                nc = cost[cur] + math.hypot(dx,dy)
          71 +                if nc < cost.get(q, 1e30):
          72 +                    cost[q], parent[q] = nc, cur
          73 +                    h = math.hypot(q[0]-gl[0],q[1]-gl[1])
          74 +                    heapq.heappush(heap, (nc+h, q))
          75 +        if gl not in cost:
          76 +            return []
          77 +        path, q = [], gl
          78 +        while q != st:
          79 +            path.append(np.array([lo+q[0]*res, lo+q[1]*res]))
          80 +            q = parent[q]
          81 +        path.reverse()
          82 +        # Retain only turning points to reduce jitter.
          83 +        compact = []
          84 +        last_dir = None
          85 +        for i, p in enumerate(path):
          86 +            d = None if i+1 == len(path) else tuple(np.sign(path[i+1]-p))
          87 +            if i == 0 or d != last_dir:
          88 +                compact.append(p)
          89 +            last_dir = d
          90 +        compact.append(np.clip(target, lo, hi))
          91 +        return compact
          92 +
   36     93      def get_action(self, state):
   37     94          s = np.asarray(state, dtype=float)
   38     95          obj, robot, goal = s[0:2], s[16:18], s[29:31]
@@ -46,26 +103,15 @@ class GeneratedApproach:
   46    103              if abs(ae) > 0.075:
   47    104                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
   48    105                  self.mode = "rot_far"
         106 +                side = -self.turn_sign
         107 +                far0 = obj + self._world(np.array([side*(width*.5+.34), -.72*lv]), theta)
         108 +                self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
   49    109              elif pd > 0.018:
   50    110                  self.push_dir = dp / max(pd, 1e-9)
   51    111                  self.mode = "move_far"
   52        -                # Route around the cap instead of crossing the T when moving
   53        -                # from a rotation contact to the translation staging side.
   54        -                c, sn = math.cos(theta), math.sin(theta)
   55        -                rel = robot - obj
   56        -                local_robot = np.array([c*rel[0] + sn*rel[1],
   57        -                                        -sn*rel[0] + c*rel[1]])
   58    112                  com0 = obj + self._world(np.array([0.0, -0.36*lv]), theta)
   59    113                  far0 = np.clip(com0 - self.push_dir*0.82, 0.105, 4.895)
   60        -                frel = far0 - obj
   61        -                far_local = np.array([c*frel[0] + sn*frel[1],
   62        -                                      -sn*frel[0] + c*frel[1]])
   63        -                side0 = 1.0 if local_robot[0] >= 0 else -1.0
   64        -                self.nav = [obj + self._world(np.array([side0*0.76,
   65        -                            min(0.30, max(-0.72*lv, local_robot[1]))]), theta),
   66        -                            obj + self._world(np.array([side0*0.76, 0.30]), theta),
   67        -                            obj + self._world(np.array([far_local[0], 0.30]), theta)]
   68        -                self.nav = [np.clip(p, 0.105, 4.895) for p in self.nav]
         114 +                self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
   69    115              else:
   70    116                  return np.zeros(2, dtype=float)
   71    117              self.count = 0
@@ -80,6 +126,10 @@ class GeneratedApproach:
   80    126              contact = obj + self._world(contact_local, theta)
   81    127              force = self._world(np.array([self.turn_sign, 0.0]), theta)
   82    128              if self.mode == "rot_far":
         129 +                while self.nav and np.linalg.norm(robot-self.nav[0]) < 0.05:
         130 +                    self.nav.pop(0)
         131 +                if self.nav:
         132 +                    return self._safe(self.nav[0]-robot)
   83    133                  if np.linalg.norm(robot - far) < 0.035:
   84    134                      self.mode = "rot_contact"
   85    135                  return self._safe(far - robot)
```

</details>

<a id="C024"></a>
### C024 · Trace contact-navigation state transitions

Commit `e1fedceb6ff8e7e658465114f1be5fccfeceb600`; parents: 3db79a00542e31f7b39a2a78a7f8a90b77b95350. Recorded author date: 2026-09-09T08:37:42+02:00.

File roles (automatic): diagnostic/test.

- [E0073](01_timeline.md#E0073): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C024_e1fedce.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index 9521ace..40f9978 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -10,8 +10,13 @@ def run(seed, verbose=False):
   10     10      policy = GeneratedApproach(env.action_space, env.observation_space, {})
   11     11      policy.reset(obs, info)
   12     12      initial = obs.copy()
          13 +    old_mode = policy.mode
   13     14      for step in range(env.max_steps):
   14     15          obs, reward, term, trunc, info = env.step(policy.get_action(obs))
          16 +        if verbose and policy.mode != old_mode:
          17 +            print(' transition', step, old_mode, '->', policy.mode,
          18 +                  'nav', [np.round(x, 2).tolist() for x in policy.nav])
          19 +            old_mode = policy.mode
   15     20          if verbose and step % 50 == 0:
   16     21              print(' ', step, policy.mode, 'pose', np.round(obs[:3], 3),
   17     22                    'robot', np.round(obs[16:18], 3))
```

</details>

<a id="C025"></a>
### C025 · Increase trajectory sampling around navigation collisions

Commit `3bdeac403a24413c21af61a6dfc5d7869ab4a5cf`; parents: e1fedceb6ff8e7e658465114f1be5fccfeceb600. Recorded author date: 2026-09-09T08:38:05+02:00.

File roles (automatic): diagnostic/test.

- [E0077](01_timeline.md#E0077): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C025_3bdeac4.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index 40f9978..1fcf0a6 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -17,7 +17,7 @@ def run(seed, verbose=False):
   17     17              print(' transition', step, old_mode, '->', policy.mode,
   18     18                    'nav', [np.round(x, 2).tolist() for x in policy.nav])
   19     19              old_mode = policy.mode
   20        -        if verbose and step % 50 == 0:
          20 +        if verbose and step % 10 == 0:
   21     21              print(' ', step, policy.mode, 'pose', np.round(obs[:3], 3),
   22     22                    'robot', np.round(obs[16:18], 3))
   23     23          if term or trunc:
```

</details>

<a id="C026"></a>
### C026 · Abort and replan stale routes on accidental contact

Commit `d523a1c726f1cd73d257b8bed7242a5a6587fa50`; parents: 3bdeac403a24413c21af61a6dfc5d7869ab4a5cf. Recorded author date: 2026-09-09T08:38:30+02:00.

File roles (automatic): policy.

- [E0081](01_timeline.md#E0081): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C026_d523a1c_approach.py) · [Exact all-file diff](evidence/diffs/C026_d523a1c.diff)

[Previous saved controller snapshot](evidence/versions/C023_3db79a0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a4329c8..e71cbd1 100644
--- a/approach.py
+++ b/approach.py
@@ -39,7 +39,7 @@ class GeneratedApproach:
   39     39          lo, hi, res = 0.11, 4.89, 0.12
   40     40          n = int((hi-lo)/res) + 1
   41     41          c, sn = math.cos(theta), math.sin(theta)
   42        -        margin = 0.105
          42 +        margin = 0.145
   43     43          def blocked(ix, iy):
   44     44              p = np.array([lo + ix*res, lo + iy*res]) - obj
   45     45              x, y = c*p[0] + sn*p[1], -sn*p[0] + c*p[1]
@@ -126,6 +126,11 @@ class GeneratedApproach:
  126    126              contact = obj + self._world(contact_local, theta)
  127    127              force = self._world(np.array([self.turn_sign, 0.0]), theta)
  128    128              if self.mode == "rot_far":
         129 +                disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
         130 +                             abs(self._angle(theta-self.start_pose[2])) > 0.018)
         131 +                if disturbed:
         132 +                    self.mode, self.nav = "choose", []
         133 +                    return self._safe(robot-obj, 0.035)
  129    134                  while self.nav and np.linalg.norm(robot-self.nav[0]) < 0.05:
  130    135                      self.nav.pop(0)
  131    136                  if self.nav:
@@ -155,6 +160,11 @@ class GeneratedApproach:
  155    160          com = obj + self._world(np.array([0.0, -0.36 * lv]), theta)
  156    161          far = np.clip(com - self.push_dir * 0.82, 0.105, 4.895)
  157    162          if self.mode == "move_far":
         163 +            disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
         164 +                         abs(self._angle(theta-self.start_pose[2])) > 0.018)
         165 +            if disturbed:
         166 +                self.mode, self.nav = "choose", []
         167 +                return self._safe(robot-obj, 0.035)
  158    168              while self.nav and np.linalg.norm(robot - self.nav[0]) < 0.045:
  159    169                  self.nav.pop(0)
  160    170              if self.nav:
```

</details>

<a id="C027"></a>
### C027 · Maintain stable COM contact for efficient translation

Commit `a91a6fd310bd36f6dfe70cc9d0502f8993f9d301`; parents: d523a1c726f1cd73d257b8bed7242a5a6587fa50. Recorded author date: 2026-09-09T08:39:01+02:00.

File roles (automatic): policy.

- [E0085](01_timeline.md#E0085): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C027_a91a6fd_approach.py) · [Exact all-file diff](evidence/diffs/C027_a91a6fd.diff)

[Previous saved controller snapshot](evidence/versions/C026_d523a1c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e71cbd1..42bb90e 100644
--- a/approach.py
+++ b/approach.py
@@ -100,7 +100,7 @@ class GeneratedApproach:
  100    100          pd = float(np.linalg.norm(dp))
  101    101  
  102    102          if self.mode == "choose":
  103        -            if abs(ae) > 0.075:
         103 +            if abs(ae) > 0.11:
  104    104                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  105    105                  self.mode = "rot_far"
  106    106                  side = -self.turn_sign
@@ -178,9 +178,13 @@ class GeneratedApproach:
  178    178              self.count += 1
  179    179              moved = float(np.linalg.norm(obj - self.start_pose[:2]))
  180    180              now_ae = abs(self._angle(goal_theta - theta))
  181        -            # Much of the stroke is free travel from the guaranteed-clear
  182        -            # staging radius to the actual outline (especially at the stem).
  183        -            if moved > 0.14 or self.count >= 48 or now_ae > 0.13:
         181 +            # Once contact is established, keep following through in short
         182 +            # closed-loop segments instead of paying to reacquire every time.
         183 +            if moved > 0.14 and now_ae < 0.11 and pd > 0.05:
         184 +                self.start_pose = np.array([obj[0], obj[1], theta])
         185 +                self.push_dir = dp / max(pd, 1e-9)
         186 +                self.count = 0
         187 +            elif self.count >= 60 or now_ae > 0.13:
  184    188                  self.mode = "move_retreat"
  185    189              speed = 0.012 if pd < 0.12 else 0.025
  186    190              return self._safe((com + self.push_dir * 0.20) - robot, speed)
```

</details>

<a id="C028"></a>
### C028 · Release at target and correct angle wrap branch

Commit `9e7ff36b0cca333943ec1dbcbfa8008e8f077af6`; parents: a91a6fd310bd36f6dfe70cc9d0502f8993f9d301. Recorded author date: 2026-09-09T08:40:29+02:00.

File roles (automatic): policy.

- [E0092](01_timeline.md#E0092): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C028_9e7ff36_approach.py) · [Exact all-file diff](evidence/diffs/C028_9e7ff36.diff)

[Previous saved controller snapshot](evidence/versions/C027_a91a6fd_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 42bb90e..db6f690 100644
--- a/approach.py
+++ b/approach.py
@@ -100,7 +100,8 @@ class GeneratedApproach:
  100    100          pd = float(np.linalg.norm(dp))
  101    101  
  102    102          if self.mode == "choose":
  103        -            if abs(ae) > 0.11:
         103 +            branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
         104 +            if abs(ae) > 0.11 or branch_mismatch:
  104    105                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  105    106                  self.mode = "rot_far"
  106    107                  side = -self.turn_sign
@@ -178,6 +179,11 @@ class GeneratedApproach:
  178    179              self.count += 1
  179    180              moved = float(np.linalg.norm(obj - self.start_pose[:2]))
  180    181              now_ae = abs(self._angle(goal_theta - theta))
         182 +            # Release immediately upon arrival or after crossing the goal;
         183 +            # another inward step can overshoot substantially under contact.
         184 +            if pd < 0.022 or np.dot(dp, self.push_dir) < 0.0:
         185 +                self.mode = "move_retreat"
         186 +                return self._safe(-self.push_dir, 0.018)
  181    187              # Once contact is established, keep following through in short
  182    188              # closed-loop segments instead of paying to reacquire every time.
  183    189              if moved > 0.14 and now_ae < 0.11 and pd > 0.05:
```

</details>

<a id="C029"></a>
### C029 · Adapt rotation lever near boundaries and prevent diagonal corner cuts

Commit `5bc8cf8e74eb517fa7f8d5a6a1d48e3edb595ba7`; parents: 9e7ff36b0cca333943ec1dbcbfa8008e8f077af6. Recorded author date: 2026-09-09T08:41:58+02:00.

File roles (automatic): policy.

- [E0100](01_timeline.md#E0100): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C029_5bc8cf8_approach.py) · [Exact all-file diff](evidence/diffs/C029_5bc8cf8.diff)

[Previous saved controller snapshot](evidence/versions/C028_9e7ff36_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index db6f690..6c9d036 100644
--- a/approach.py
+++ b/approach.py
@@ -17,6 +17,7 @@ class GeneratedApproach:
   17     17          self.push_dir = np.array([1.0, 0.0])
   18     18          self.start_pose = np.zeros(3)
   19     19          self.nav = []
          20 +        self.rot_y = -0.7
   20     21  
   21     22      @staticmethod
   22     23      def _angle(x):
@@ -67,6 +68,8 @@ class GeneratedApproach:
   67     68                  q = (cur[0]+dx, cur[1]+dy)
   68     69                  if not (0 <= q[0] < n and 0 <= q[1] < n) or (q != st and blocked(*q)):
   69     70                      continue
          71 +                if dx and dy and (blocked(cur[0]+dx, cur[1]) or blocked(cur[0], cur[1]+dy)):
          72 +                    continue
   70     73                  nc = cost[cur] + math.hypot(dx,dy)
   71     74                  if nc < cost.get(q, 1e30):
   72     75                      cost[q], parent[q] = nc, cur
@@ -101,11 +104,21 @@ class GeneratedApproach:
  101    104  
  102    105          if self.mode == "choose":
  103    106              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  104        -            if abs(ae) > 0.11 or branch_mismatch:
         107 +            boundary_recover = min(obj) < 0.72 or max(obj) > 4.28
         108 +            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover:
  105    109                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  106    110                  self.mode = "rot_far"
  107    111                  side = -self.turn_sign
  108        -                far0 = obj + self._world(np.array([side*(width*.5+.34), -.72*lv]), theta)
         112 +                # Move the lever up the stem when the distal contact would
         113 +                # crowd a robot boundary.
         114 +                def lever_clear(frac):
         115 +                    pts = [np.array([side*(width*.5+.34), -frac*lv]),
         116 +                           np.array([side*(width*.5+.115), -frac*lv])]
         117 +                    world = [obj+self._world(p,theta) for p in pts]
         118 +                    return min(min(q[0]-.105,4.895-q[0],q[1]-.105,4.895-q[1]) for q in world)
         119 +                frac = max((0.80, 0.68, 0.56), key=lever_clear)
         120 +                self.rot_y = -frac*lv
         121 +                far0 = obj + self._world(np.array([side*(width*.5+.34), self.rot_y]), theta)
  109    122                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  110    123              elif pd > 0.018:
  111    124                  self.push_dir = dp / max(pd, 1e-9)
@@ -121,8 +134,8 @@ class GeneratedApproach:
  121    134          if self.mode.startswith("rot"):
  122    135              # Distal-stem side contact is a reliable long rotation lever.
  123    136              side = -self.turn_sign
  124        -            far_local = np.array([side * (width * 0.5 + 0.34), -0.72 * lv])
  125        -            contact_local = np.array([side * (width * 0.5 + 0.115), -0.72 * lv])
         137 +            far_local = np.array([side * (width * 0.5 + 0.34), self.rot_y])
         138 +            contact_local = np.array([side * (width * 0.5 + 0.115), self.rot_y])
  126    139              far = obj + self._world(far_local, theta)
  127    140              contact = obj + self._world(contact_local, theta)
  128    141              force = self._world(np.array([self.turn_sign, 0.0]), theta)
@@ -150,7 +163,7 @@ class GeneratedApproach:
  150    163                  current_ae = self._angle(goal_theta - theta)
  151    164                  turned = abs(self._angle(theta - self.start_pose[2]))
  152    165                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  153        -                        or turned > 0.16 or self.count >= 10):
         166 +                        or turned > 0.12 or self.count >= 8):
  154    167                      self.mode = "rot_retreat"
  155    168                  return self._safe(force, 0.016)
  156    169              if np.linalg.norm(robot - far) < 0.04:
```

</details>

<a id="C030"></a>
### C030 · Adapt translation contact line to cancel observed torque

Commit `f6a93145912731742207c66269ccb593958e32d5`; parents: 5bc8cf8e74eb517fa7f8d5a6a1d48e3edb595ba7. Recorded author date: 2026-09-09T08:42:57+02:00.

File roles (automatic): policy.

- [E0106](01_timeline.md#E0106): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C030_f6a9314_approach.py) · [Exact all-file diff](evidence/diffs/C030_f6a9314.diff)

[Previous saved controller snapshot](evidence/versions/C029_5bc8cf8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6c9d036..87f8f60 100644
--- a/approach.py
+++ b/approach.py
@@ -18,6 +18,7 @@ class GeneratedApproach:
   18     18          self.start_pose = np.zeros(3)
   19     19          self.nav = []
   20     20          self.rot_y = -0.7
          21 +        self.line_offset = 0.0
   21     22  
   22     23      @staticmethod
   23     24      def _angle(x):
@@ -124,6 +125,7 @@ class GeneratedApproach:
  124    125                  self.push_dir = dp / max(pd, 1e-9)
  125    126                  self.mode = "move_far"
  126    127                  com0 = obj + self._world(np.array([0.0, -0.36*lv]), theta)
         128 +                com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  127    129                  far0 = np.clip(com0 - self.push_dir*0.82, 0.105, 4.895)
  128    130                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  129    131              else:
@@ -172,6 +174,7 @@ class GeneratedApproach:
  172    174  
  173    175          # The effective COM lies down the stem from the reported junction.
  174    176          com = obj + self._world(np.array([0.0, -0.36 * lv]), theta)
         177 +        com = com + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  175    178          far = np.clip(com - self.push_dir * 0.82, 0.105, 4.895)
  176    179          if self.mode == "move_far":
  177    180              disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
@@ -199,7 +202,9 @@ class GeneratedApproach:
  199    202                  return self._safe(-self.push_dir, 0.018)
  200    203              # Once contact is established, keep following through in short
  201    204              # closed-loop segments instead of paying to reacquire every time.
  202        -            if moved > 0.14 and now_ae < 0.11 and pd > 0.05:
         205 +            if moved > 0.11 and now_ae < 0.14 and pd > 0.05:
         206 +                dtheta = self._angle(theta-self.start_pose[2])
         207 +                self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  203    208                  self.start_pose = np.array([obj[0], obj[1], theta])
  204    209                  self.push_dir = dp / max(pd, 1e-9)
  205    210                  self.count = 0
```

</details>

<a id="C031"></a>
### C031 · Permit translation-first recovery near arena boundaries

Commit `ba6c6b83af99bcbe596ba94aa89bc618a2ab99f5`; parents: f6a93145912731742207c66269ccb593958e32d5. Recorded author date: 2026-09-09T08:43:53+02:00.

File roles (automatic): policy.

- [E0112](01_timeline.md#E0112): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C031_ba6c6b8_approach.py) · [Exact all-file diff](evidence/diffs/C031_ba6c6b8.diff)

[Previous saved controller snapshot](evidence/versions/C030_f6a9314_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 87f8f60..6b011b7 100644
--- a/approach.py
+++ b/approach.py
@@ -202,13 +202,14 @@ class GeneratedApproach:
  202    202                  return self._safe(-self.push_dir, 0.018)
  203    203              # Once contact is established, keep following through in short
  204    204              # closed-loop segments instead of paying to reacquire every time.
  205        -            if moved > 0.11 and now_ae < 0.14 and pd > 0.05:
         205 +            near_boundary = min(obj) < 0.78 or max(obj) > 4.22
         206 +            if moved > 0.11 and (now_ae < 0.14 or near_boundary) and pd > 0.05:
  206    207                  dtheta = self._angle(theta-self.start_pose[2])
  207    208                  self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  208    209                  self.start_pose = np.array([obj[0], obj[1], theta])
  209    210                  self.push_dir = dp / max(pd, 1e-9)
  210    211                  self.count = 0
  211        -            elif self.count >= 60 or now_ae > 0.13:
         212 +            elif self.count >= 60 or (now_ae > 0.13 and not near_boundary):
  212    213                  self.mode = "move_retreat"
  213    214              speed = 0.012 if pd < 0.12 else 0.025
  214    215              return self._safe((com + self.push_dir * 0.20) - robot, speed)
```

</details>

<a id="C032"></a>
### C032 · Accelerate rotation strokes away from boundaries

Commit `5cd4926a0960646e84c8990b1c066d98cd62d2e1`; parents: ba6c6b83af99bcbe596ba94aa89bc618a2ab99f5. Recorded author date: 2026-09-09T08:44:48+02:00.

File roles (automatic): policy.

- [E0118](01_timeline.md#E0118): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C032_5cd4926_approach.py) · [Exact all-file diff](evidence/diffs/C032_5cd4926.diff)

[Previous saved controller snapshot](evidence/versions/C031_ba6c6b8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6b011b7..2311190 100644
--- a/approach.py
+++ b/approach.py
@@ -165,9 +165,10 @@ class GeneratedApproach:
  165    165                  current_ae = self._angle(goal_theta - theta)
  166    166                  turned = abs(self._angle(theta - self.start_pose[2]))
  167    167                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  168        -                        or turned > 0.12 or self.count >= 8):
         168 +                        or turned > 0.18 or self.count >= 9):
  169    169                      self.mode = "rot_retreat"
  170        -                return self._safe(force, 0.016)
         170 +                speed = 0.014 if min(obj) < 0.8 or max(obj) > 4.2 else 0.022
         171 +                return self._safe(force, speed)
  171    172              if np.linalg.norm(robot - far) < 0.04:
  172    173                  self.mode = "choose"
  173    174              return self._safe(far - robot, 0.035)
```

</details>

<a id="C033"></a>
### C033 · Tune online torque cancellation and final orientation precision

Commit `7c3e2087fb02f92e63a19ca3b6a749cbd9f17880`; parents: 5cd4926a0960646e84c8990b1c066d98cd62d2e1. Recorded author date: 2026-09-09T08:45:43+02:00.

File roles (automatic): policy.

- [E0124](01_timeline.md#E0124): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C033_7c3e208_approach.py) · [Exact all-file diff](evidence/diffs/C033_7c3e208.diff)

[Previous saved controller snapshot](evidence/versions/C032_5cd4926_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2311190..6a315a5 100644
--- a/approach.py
+++ b/approach.py
@@ -105,8 +105,9 @@ class GeneratedApproach:
  105    105  
  106    106          if self.mode == "choose":
  107    107              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
         108 +            turn_threshold = 0.06 if pd < 0.18 else 0.11
  108    109              boundary_recover = min(obj) < 0.72 or max(obj) > 4.28
  109        -            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover:
         110 +            if (abs(ae) > turn_threshold or branch_mismatch) and not boundary_recover:
  110    111                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  111    112                  self.mode = "rot_far"
  112    113                  side = -self.turn_sign
@@ -204,13 +205,13 @@ class GeneratedApproach:
  204    205              # Once contact is established, keep following through in short
  205    206              # closed-loop segments instead of paying to reacquire every time.
  206    207              near_boundary = min(obj) < 0.78 or max(obj) > 4.22
  207        -            if moved > 0.11 and (now_ae < 0.14 or near_boundary) and pd > 0.05:
         208 +            if moved > 0.08 and (now_ae < 0.16 or near_boundary) and pd > 0.05:
  208    209                  dtheta = self._angle(theta-self.start_pose[2])
  209        -                self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
         210 +                self.line_offset = float(np.clip(self.line_offset + 1.2*dtheta, -0.28, 0.28))
  210    211                  self.start_pose = np.array([obj[0], obj[1], theta])
  211    212                  self.push_dir = dp / max(pd, 1e-9)
  212    213                  self.count = 0
  213        -            elif self.count >= 60 or (now_ae > 0.13 and not near_boundary):
         214 +            elif self.count >= 60 or (now_ae > 0.155 and not near_boundary):
  214    215                  self.mode = "move_retreat"
  215    216              speed = 0.012 if pd < 0.12 else 0.025
  216    217              return self._safe((com + self.push_dir * 0.20) - robot, speed)
```

</details>

<a id="C034"></a>
### C034 · Restore stable conservative torque adaptation

Commit `c03b231cf2f2bbab84b02a71dade607cfa7b27b2`; parents: 7c3e2087fb02f92e63a19ca3b6a749cbd9f17880. Recorded author date: 2026-09-09T08:46:15+02:00.

File roles (automatic): policy.

- [E0128](01_timeline.md#E0128): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C034_c03b231_approach.py) · [Exact all-file diff](evidence/diffs/C034_c03b231.diff)

[Previous saved controller snapshot](evidence/versions/C033_7c3e208_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C032](#C032). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6a315a5..2311190 100644
--- a/approach.py
+++ b/approach.py
@@ -105,9 +105,8 @@ class GeneratedApproach:
  105    105  
  106    106          if self.mode == "choose":
  107    107              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  108        -            turn_threshold = 0.06 if pd < 0.18 else 0.11
  109    108              boundary_recover = min(obj) < 0.72 or max(obj) > 4.28
  110        -            if (abs(ae) > turn_threshold or branch_mismatch) and not boundary_recover:
         109 +            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover:
  111    110                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  112    111                  self.mode = "rot_far"
  113    112                  side = -self.turn_sign
@@ -205,13 +204,13 @@ class GeneratedApproach:
  205    204              # Once contact is established, keep following through in short
  206    205              # closed-loop segments instead of paying to reacquire every time.
  207    206              near_boundary = min(obj) < 0.78 or max(obj) > 4.22
  208        -            if moved > 0.08 and (now_ae < 0.16 or near_boundary) and pd > 0.05:
         207 +            if moved > 0.11 and (now_ae < 0.14 or near_boundary) and pd > 0.05:
  209    208                  dtheta = self._angle(theta-self.start_pose[2])
  210        -                self.line_offset = float(np.clip(self.line_offset + 1.2*dtheta, -0.28, 0.28))
         209 +                self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  211    210                  self.start_pose = np.array([obj[0], obj[1], theta])
  212    211                  self.push_dir = dp / max(pd, 1e-9)
  213    212                  self.count = 0
  214        -            elif self.count >= 60 or (now_ae > 0.155 and not near_boundary):
         213 +            elif self.count >= 60 or (now_ae > 0.13 and not near_boundary):
  215    214                  self.mode = "move_retreat"
  216    215              speed = 0.012 if pd < 0.12 else 0.025
  217    216              return self._safe((com + self.push_dir * 0.20) - robot, speed)
```

</details>

<a id="C035"></a>
### C035 · Preserve contact room with earlier boundary recovery

Commit `8091315c4168dab5667a681955828ada2091c6a2`; parents: c03b231cf2f2bbab84b02a71dade607cfa7b27b2. Recorded author date: 2026-09-09T08:46:59+02:00.

File roles (automatic): policy.

- [E0134](01_timeline.md#E0134): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C035_8091315_approach.py) · [Exact all-file diff](evidence/diffs/C035_8091315.diff)

[Previous saved controller snapshot](evidence/versions/C034_c03b231_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2311190..252f3b9 100644
--- a/approach.py
+++ b/approach.py
@@ -105,7 +105,7 @@ class GeneratedApproach:
  105    105  
  106    106          if self.mode == "choose":
  107    107              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  108        -            boundary_recover = min(obj) < 0.72 or max(obj) > 4.28
         108 +            boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
  109    109              if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover:
  110    110                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  111    111                  self.mode = "rot_far"
@@ -176,7 +176,7 @@ class GeneratedApproach:
  176    176          # The effective COM lies down the stem from the reported junction.
  177    177          com = obj + self._world(np.array([0.0, -0.36 * lv]), theta)
  178    178          com = com + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  179        -        far = np.clip(com - self.push_dir * 0.82, 0.105, 4.895)
         179 +        far = np.clip(com - self.push_dir * 0.76, 0.105, 4.895)
  180    180          if self.mode == "move_far":
  181    181              disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
  182    182                           abs(self._angle(theta-self.start_pose[2])) > 0.018)
@@ -203,7 +203,7 @@ class GeneratedApproach:
  203    203                  return self._safe(-self.push_dir, 0.018)
  204    204              # Once contact is established, keep following through in short
  205    205              # closed-loop segments instead of paying to reacquire every time.
  206        -            near_boundary = min(obj) < 0.78 or max(obj) > 4.22
         206 +            near_boundary = min(obj) < 0.96 or max(obj) > 4.04
  207    207              if moved > 0.11 and (now_ae < 0.14 or near_boundary) and pd > 0.05:
  208    208                  dtheta = self._angle(theta-self.start_pose[2])
  209    209                  self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
```

</details>

<a id="C036"></a>
### C036 · Use longer efficient rotation strokes in open space

Commit `08cf5b12c689540ee3c6e6a7e76e0f17e75a3e1f`; parents: 8091315c4168dab5667a681955828ada2091c6a2. Recorded author date: 2026-09-09T08:48:21+02:00.

File roles (automatic): policy.

- [E0142](01_timeline.md#E0142): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C036_08cf5b1_approach.py) · [Exact all-file diff](evidence/diffs/C036_08cf5b1.diff)

[Previous saved controller snapshot](evidence/versions/C035_8091315_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 252f3b9..9a1723c 100644
--- a/approach.py
+++ b/approach.py
@@ -164,10 +164,13 @@ class GeneratedApproach:
  164    164                  self.count += 1
  165    165                  current_ae = self._angle(goal_theta - theta)
  166    166                  turned = abs(self._angle(theta - self.start_pose[2]))
         167 +                crowded = min(obj) < 0.95 or max(obj) > 4.05
         168 +                turn_limit = 0.12 if crowded else 0.28
         169 +                count_limit = 8 if crowded else 14
  167    170                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  168        -                        or turned > 0.18 or self.count >= 9):
         171 +                        or turned > turn_limit or self.count >= count_limit):
  169    172                      self.mode = "rot_retreat"
  170        -                speed = 0.014 if min(obj) < 0.8 or max(obj) > 4.2 else 0.022
         173 +                speed = 0.014 if crowded else 0.022
  171    174                  return self._safe(force, speed)
  172    175              if np.linalg.norm(robot - far) < 0.04:
  173    176                  self.mode = "choose"
```

</details>

<a id="C037"></a>
### C037 · Balance open-space rotation speed and stability

Commit `e070c507b45db2f9d15ad664eff5039c59d338c2`; parents: 08cf5b12c689540ee3c6e6a7e76e0f17e75a3e1f. Recorded author date: 2026-09-09T08:48:43+02:00.

File roles (automatic): policy.

- [E0146](01_timeline.md#E0146): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C037_e070c50_approach.py) · [Exact all-file diff](evidence/diffs/C037_e070c50.diff)

[Previous saved controller snapshot](evidence/versions/C036_08cf5b1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9a1723c..7481095 100644
--- a/approach.py
+++ b/approach.py
@@ -165,8 +165,8 @@ class GeneratedApproach:
  165    165                  current_ae = self._angle(goal_theta - theta)
  166    166                  turned = abs(self._angle(theta - self.start_pose[2]))
  167    167                  crowded = min(obj) < 0.95 or max(obj) > 4.05
  168        -                turn_limit = 0.12 if crowded else 0.28
  169        -                count_limit = 8 if crowded else 14
         168 +                turn_limit = 0.12 if crowded else 0.22
         169 +                count_limit = 8 if crowded else 11
  170    170                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  171    171                          or turned > turn_limit or self.count >= count_limit):
  172    172                      self.mode = "rot_retreat"
```

</details>

<a id="C038"></a>
### C038 · Favor reliable bounded rotation strokes across poses

Commit `ea5935166af01a57a9d705ac397650e989deec7e`; parents: e070c507b45db2f9d15ad664eff5039c59d338c2. Recorded author date: 2026-09-09T08:49:27+02:00.

File roles (automatic): policy.

- [E0152](01_timeline.md#E0152): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C038_ea59351_approach.py) · [Exact all-file diff](evidence/diffs/C038_ea59351.diff)

[Previous saved controller snapshot](evidence/versions/C037_e070c50_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7481095..b227ad8 100644
--- a/approach.py
+++ b/approach.py
@@ -165,8 +165,8 @@ class GeneratedApproach:
  165    165                  current_ae = self._angle(goal_theta - theta)
  166    166                  turned = abs(self._angle(theta - self.start_pose[2]))
  167    167                  crowded = min(obj) < 0.95 or max(obj) > 4.05
  168        -                turn_limit = 0.12 if crowded else 0.22
  169        -                count_limit = 8 if crowded else 11
         168 +                turn_limit = 0.12 if crowded else 0.18
         169 +                count_limit = 8 if crowded else 9
  170    170                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  171    171                          or turned > turn_limit or self.count >= count_limit):
  172    172                      self.mode = "rot_retreat"
```

</details>

<a id="C039"></a>
### C039 · Adapt rotation stroke length in edge approach zones

Commit `34dd135bddc230f5ed750b2a2f55c27b8d8c9887`; parents: ea5935166af01a57a9d705ac397650e989deec7e. Recorded author date: 2026-09-09T08:50:13+02:00.

File roles (automatic): policy.

- [E0158](01_timeline.md#E0158): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C039_34dd135_approach.py) · [Exact all-file diff](evidence/diffs/C039_34dd135.diff)

[Previous saved controller snapshot](evidence/versions/C038_ea59351_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b227ad8..4785b3e 100644
--- a/approach.py
+++ b/approach.py
@@ -165,8 +165,9 @@ class GeneratedApproach:
  165    165                  current_ae = self._angle(goal_theta - theta)
  166    166                  turned = abs(self._angle(theta - self.start_pose[2]))
  167    167                  crowded = min(obj) < 0.95 or max(obj) > 4.05
  168        -                turn_limit = 0.12 if crowded else 0.18
  169        -                count_limit = 8 if crowded else 9
         168 +                edge_zone = min(obj) < 1.20 or max(obj) > 3.80
         169 +                turn_limit = 0.12 if crowded else (0.22 if edge_zone else 0.18)
         170 +                count_limit = 8 if crowded else (11 if edge_zone else 9)
  170    171                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  171    172                          or turned > turn_limit or self.count >= count_limit):
  172    173                      self.mode = "rot_retreat"
```

</details>

<a id="C040"></a>
### C040 · Interleave recovery translation when rotation drifts away from goal

Commit `de55505f1bb9ad41a0516e8ba093db63ddb0bf0c`; parents: 34dd135bddc230f5ed750b2a2f55c27b8d8c9887. Recorded author date: 2026-09-09T08:51:38+02:00.

File roles (automatic): policy.

- [E0166](01_timeline.md#E0166): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C040_de55505_approach.py) · [Exact all-file diff](evidence/diffs/C040_de55505.diff)

[Previous saved controller snapshot](evidence/versions/C039_34dd135_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4785b3e..f303591 100644
--- a/approach.py
+++ b/approach.py
@@ -19,6 +19,8 @@ class GeneratedApproach:
   19     19          self.nav = []
   20     20          self.rot_y = -0.7
   21     21          self.line_offset = 0.0
          22 +        self.force_move = False
          23 +        self.start_pd = 0.0
   22     24  
   23     25      @staticmethod
   24     26      def _angle(x):
@@ -106,7 +108,7 @@ class GeneratedApproach:
  106    108          if self.mode == "choose":
  107    109              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  108    110              boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
  109        -            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover:
         111 +            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover and not self.force_move:
  110    112                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  111    113                  self.mode = "rot_far"
  112    114                  side = -self.turn_sign
@@ -159,6 +161,7 @@ class GeneratedApproach:
  159    161                      self.mode = "rot_push"
  160    162                      self.count = 0
  161    163                      self.start_pose = np.array([obj[0], obj[1], theta])
         164 +                    self.start_pd = pd
  162    165                  return self._safe(contact - robot, 0.025)
  163    166              if self.mode == "rot_push":
  164    167                  self.count += 1
@@ -174,6 +177,8 @@ class GeneratedApproach:
  174    177                  speed = 0.014 if crowded else 0.022
  175    178                  return self._safe(force, speed)
  176    179              if np.linalg.norm(robot - far) < 0.04:
         180 +                if pd > self.start_pd + 0.18:
         181 +                    self.force_move = True
  177    182                  self.mode = "choose"
  178    183              return self._safe(far - robot, 0.035)
  179    184  
@@ -208,13 +213,17 @@ class GeneratedApproach:
  208    213              # Once contact is established, keep following through in short
  209    214              # closed-loop segments instead of paying to reacquire every time.
  210    215              near_boundary = min(obj) < 0.96 or max(obj) > 4.04
  211        -            if moved > 0.11 and (now_ae < 0.14 or near_boundary) and pd > 0.05:
         216 +            if self.force_move and moved > 0.18:
         217 +                self.force_move = False
         218 +                self.mode = "move_retreat"
         219 +                return self._safe(-self.push_dir, 0.018)
         220 +            if moved > 0.11 and (now_ae < 0.14 or near_boundary or self.force_move) and pd > 0.05:
  212    221                  dtheta = self._angle(theta-self.start_pose[2])
  213    222                  self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  214    223                  self.start_pose = np.array([obj[0], obj[1], theta])
  215    224                  self.push_dir = dp / max(pd, 1e-9)
  216    225                  self.count = 0
  217        -            elif self.count >= 60 or (now_ae > 0.13 and not near_boundary):
         226 +            elif self.count >= 60 or (now_ae > 0.13 and not near_boundary and not self.force_move):
  218    227                  self.mode = "move_retreat"
  219    228              speed = 0.012 if pd < 0.12 else 0.025
  220    229              return self._safe((com + self.push_dir * 0.20) - robot, speed)
```

</details>

<a id="C041"></a>
### C041 · Prioritize final orientation once position is close

Commit `afe60d7c47239d2ec2b302d26056c1beee3f274c`; parents: de55505f1bb9ad41a0516e8ba093db63ddb0bf0c. Recorded author date: 2026-09-09T08:51:57+02:00.

File roles (automatic): policy.

- [E0170](01_timeline.md#E0170): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C041_afe60d7_approach.py) · [Exact all-file diff](evidence/diffs/C041_afe60d7.diff)

[Previous saved controller snapshot](evidence/versions/C040_de55505_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f303591..6fe2cf5 100644
--- a/approach.py
+++ b/approach.py
@@ -177,7 +177,7 @@ class GeneratedApproach:
  177    177                  speed = 0.014 if crowded else 0.022
  178    178                  return self._safe(force, speed)
  179    179              if np.linalg.norm(robot - far) < 0.04:
  180        -                if pd > self.start_pd + 0.18:
         180 +                if pd > 0.30 and pd > self.start_pd + 0.18:
  181    181                      self.force_move = True
  182    182                  self.mode = "choose"
  183    183              return self._safe(far - robot, 0.035)
```

</details>

<a id="C042"></a>
### C042 · Clear forced translation after reaching positional target

Commit `c3d1145345e09786e849c26383afa36ceee733f4`; parents: afe60d7c47239d2ec2b302d26056c1beee3f274c. Recorded author date: 2026-09-09T08:52:21+02:00.

File roles (automatic): policy.

- [E0176](01_timeline.md#E0176): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C042_c3d1145_approach.py) · [Exact all-file diff](evidence/diffs/C042_c3d1145.diff)

[Previous saved controller snapshot](evidence/versions/C041_afe60d7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6fe2cf5..4266e22 100644
--- a/approach.py
+++ b/approach.py
@@ -208,6 +208,7 @@ class GeneratedApproach:
  208    208              # Release immediately upon arrival or after crossing the goal;
  209    209              # another inward step can overshoot substantially under contact.
  210    210              if pd < 0.022 or np.dot(dp, self.push_dir) < 0.0:
         211 +                self.force_move = False
  211    212                  self.mode = "move_retreat"
  212    213                  return self._safe(-self.push_dir, 0.018)
  213    214              # Once contact is established, keep following through in short
```

</details>

<a id="C043"></a>
### C043 · Accelerate long-distance COM pushes while retaining precision

Commit `869a6eb6407952aceee654855f31558d895fd475`; parents: c3d1145345e09786e849c26383afa36ceee733f4. Recorded author date: 2026-09-09T08:53:07+02:00.

File roles (automatic): policy.

- [E0182](01_timeline.md#E0182): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C043_869a6eb_approach.py) · [Exact all-file diff](evidence/diffs/C043_869a6eb.diff)

[Previous saved controller snapshot](evidence/versions/C042_c3d1145_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4266e22..9ab8cef 100644
--- a/approach.py
+++ b/approach.py
@@ -226,7 +226,7 @@ class GeneratedApproach:
  226    226                  self.count = 0
  227    227              elif self.count >= 60 or (now_ae > 0.13 and not near_boundary and not self.force_move):
  228    228                  self.mode = "move_retreat"
  229        -            speed = 0.012 if pd < 0.12 else 0.025
         229 +            speed = 0.012 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
  230    230              return self._safe((com + self.push_dir * 0.20) - robot, speed)
  231    231          if np.linalg.norm(robot - far) < 0.04:
  232    232              self.mode = "choose"
```

</details>

<a id="C044"></a>
### C044 · initial sandbox setup

Commit `451cb27a227cb39a2c657075c7d060311c9e5d2a`; parents: 869a6eb6407952aceee654855f31558d895fd475. Recorded author date: 2026-09-09T08:54:54+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C044_451cb27.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index b034ec3..410a176 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $20.00. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $15.71. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C045"></a>
### C045 · Learn contact offset from short torque-limited pushes

Commit `860fb75a1e66158dce0d4cf5a67e19907d728eae`; parents: 451cb27a227cb39a2c657075c7d060311c9e5d2a. Recorded author date: 2026-09-09T08:56:06+02:00.

File roles (automatic): policy.

- [E0206](01_timeline.md#E0206): commit hash in recorded output.
[Controller after this commit](evidence/versions/C045_860fb75_approach.py) · [Exact all-file diff](evidence/diffs/C045_860fb75.diff)

[Previous saved controller snapshot](evidence/versions/C043_869a6eb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9ab8cef..ce5fbcb 100644
--- a/approach.py
+++ b/approach.py
@@ -225,6 +225,9 @@ class GeneratedApproach:
  225    225                  self.push_dir = dp / max(pd, 1e-9)
  226    226                  self.count = 0
  227    227              elif self.count >= 60 or (now_ae > 0.13 and not near_boundary and not self.force_move):
         228 +                if moved > 0.02:
         229 +                    dtheta = self._angle(theta-self.start_pose[2])
         230 +                    self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  228    231                  self.mode = "move_retreat"
  229    232              speed = 0.012 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
  230    233              return self._safe((com + self.push_dir * 0.20) - robot, speed)
```

</details>

<a id="C046"></a>
### C046 · Limit short-stroke torque learning to final alignment

Commit `3cdb148b6d48e3853a81f2906e48512bb1736272`; parents: 860fb75a1e66158dce0d4cf5a67e19907d728eae. Recorded author date: 2026-09-09T08:58:51+02:00.

File roles (automatic): policy.

- [E0222](01_timeline.md#E0222): commit hash in recorded output.
[Controller after this commit](evidence/versions/C046_3cdb148_approach.py) · [Exact all-file diff](evidence/diffs/C046_3cdb148.diff)

[Previous saved controller snapshot](evidence/versions/C045_860fb75_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ce5fbcb..7ca4411 100644
--- a/approach.py
+++ b/approach.py
@@ -225,7 +225,7 @@ class GeneratedApproach:
  225    225                  self.push_dir = dp / max(pd, 1e-9)
  226    226                  self.count = 0
  227    227              elif self.count >= 60 or (now_ae > 0.13 and not near_boundary and not self.force_move):
  228        -                if moved > 0.02:
         228 +                if moved > 0.02 and pd < 0.30:
  229    229                      dtheta = self._angle(theta-self.start_pose[2])
  230    230                      self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  231    231                  self.mode = "move_retreat"
```

</details>

<a id="C047"></a>
### C047 · Extend recovery pushes to amortize contact navigation

Commit `88325fb1673b4ad3e4f85ee9e0a82b51e480e1bf`; parents: 3cdb148b6d48e3853a81f2906e48512bb1736272. Recorded author date: 2026-09-09T08:59:46+02:00.

File roles (automatic): policy.

- [E0232](01_timeline.md#E0232): commit hash in recorded output.
[Controller after this commit](evidence/versions/C047_88325fb_approach.py) · [Exact all-file diff](evidence/diffs/C047_88325fb.diff)

[Previous saved controller snapshot](evidence/versions/C046_3cdb148_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7ca4411..c66a49e 100644
--- a/approach.py
+++ b/approach.py
@@ -214,7 +214,7 @@ class GeneratedApproach:
  214    214              # Once contact is established, keep following through in short
  215    215              # closed-loop segments instead of paying to reacquire every time.
  216    216              near_boundary = min(obj) < 0.96 or max(obj) > 4.04
  217        -            if self.force_move and moved > 0.18:
         217 +            if self.force_move and moved > 0.42:
  218    218                  self.force_move = False
  219    219                  self.mode = "move_retreat"
  220    220                  return self._safe(-self.push_dir, 0.018)
```

</details>

<a id="C048"></a>
### C048 · Carry boundary recovery through a meaningful translation stroke

Commit `fb12fbd266014bf0a11c60334d24794654675f9e`; parents: 88325fb1673b4ad3e4f85ee9e0a82b51e480e1bf. Recorded author date: 2026-09-09T09:00:15+02:00.

File roles (automatic): policy.

- [E0238](01_timeline.md#E0238): commit hash in recorded output.
[Controller after this commit](evidence/versions/C048_fb12fbd_approach.py) · [Exact all-file diff](evidence/diffs/C048_fb12fbd.diff)

[Previous saved controller snapshot](evidence/versions/C047_88325fb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c66a49e..87c0c51 100644
--- a/approach.py
+++ b/approach.py
@@ -124,6 +124,7 @@ class GeneratedApproach:
  124    124                  far0 = obj + self._world(np.array([side*(width*.5+.34), self.rot_y]), theta)
  125    125                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  126    126              elif pd > 0.018:
         127 +                self.force_move = self.force_move or boundary_recover
  127    128                  self.push_dir = dp / max(pd, 1e-9)
  128    129                  self.mode = "move_far"
  129    130                  com0 = obj + self._world(np.array([0.0, -0.36*lv]), theta)
```

</details>

<a id="C049"></a>
### C049 · Retreat straight backward to prevent destructive recontact

Commit `c768c44bfa5f13d2a257ea0fca5f1a3c4b1dada8`; parents: fb12fbd266014bf0a11c60334d24794654675f9e. Recorded author date: 2026-09-09T09:01:07+02:00.

File roles (automatic): policy.

- [E0247](01_timeline.md#E0247): commit hash in recorded output.
[Controller after this commit](evidence/versions/C049_c768c44_approach.py) · [Exact all-file diff](evidence/diffs/C049_c768c44.diff)

[Previous saved controller snapshot](evidence/versions/C048_fb12fbd_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 87c0c51..1292f04 100644
--- a/approach.py
+++ b/approach.py
@@ -21,6 +21,7 @@ class GeneratedApproach:
   21     21          self.line_offset = 0.0
   22     22          self.force_move = False
   23     23          self.start_pd = 0.0
          24 +        self.retreat_count = 0
   24     25  
   25     26      @staticmethod
   26     27      def _angle(x):
@@ -124,7 +125,6 @@ class GeneratedApproach:
  124    125                  far0 = obj + self._world(np.array([side*(width*.5+.34), self.rot_y]), theta)
  125    126                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  126    127              elif pd > 0.018:
  127        -                self.force_move = self.force_move or boundary_recover
  128    128                  self.push_dir = dp / max(pd, 1e-9)
  129    129                  self.mode = "move_far"
  130    130                  com0 = obj + self._world(np.array([0.0, -0.36*lv]), theta)
@@ -211,13 +211,15 @@ class GeneratedApproach:
  211    211              if pd < 0.022 or np.dot(dp, self.push_dir) < 0.0:
  212    212                  self.force_move = False
  213    213                  self.mode = "move_retreat"
         214 +                self.retreat_count = 0
  214    215                  return self._safe(-self.push_dir, 0.018)
  215    216              # Once contact is established, keep following through in short
  216    217              # closed-loop segments instead of paying to reacquire every time.
  217    218              near_boundary = min(obj) < 0.96 or max(obj) > 4.04
  218        -            if self.force_move and moved > 0.42:
         219 +            if self.force_move and moved > 0.18:
  219    220                  self.force_move = False
  220    221                  self.mode = "move_retreat"
         222 +                self.retreat_count = 0
  221    223                  return self._safe(-self.push_dir, 0.018)
  222    224              if moved > 0.11 and (now_ae < 0.14 or near_boundary or self.force_move) and pd > 0.05:
  223    225                  dtheta = self._angle(theta-self.start_pose[2])
@@ -230,8 +232,12 @@ class GeneratedApproach:
  230    232                      dtheta = self._angle(theta-self.start_pose[2])
  231    233                      self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  232    234                  self.mode = "move_retreat"
         235 +                self.retreat_count = 0
  233    236              speed = 0.012 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
  234    237              return self._safe((com + self.push_dir * 0.20) - robot, speed)
  235        -        if np.linalg.norm(robot - far) < 0.04:
         238 +        # Break contact along the exact reverse push direction. Recomputing a
         239 +        # COM-relative far point after the T rotates can route through the T.
         240 +        self.retreat_count += 1
         241 +        if self.retreat_count >= 12:
  236    242              self.mode = "choose"
  237        -        return self._safe(far - robot, 0.035)
         243 +        return self._safe(-self.push_dir, 0.035)
```

</details>

<a id="C050"></a>
### C050 · Use cap-end torque when distal stem contact is crowded

Commit `c083d05863968ac12cb0efdcea6e089f8c523d95`; parents: c768c44bfa5f13d2a257ea0fca5f1a3c4b1dada8. Recorded author date: 2026-09-09T09:03:35+02:00.

File roles (automatic): policy.

- [E0263](01_timeline.md#E0263): commit hash in recorded output.
[Controller after this commit](evidence/versions/C050_c083d05_approach.py) · [Exact all-file diff](evidence/diffs/C050_c083d05.diff)

[Previous saved controller snapshot](evidence/versions/C049_c768c44_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1292f04..c01e080 100644
--- a/approach.py
+++ b/approach.py
@@ -18,6 +18,7 @@ class GeneratedApproach:
   18     18          self.start_pose = np.zeros(3)
   19     19          self.nav = []
   20     20          self.rot_y = -0.7
          21 +        self.rot_cap = False
   21     22          self.line_offset = 0.0
   22     23          self.force_move = False
   23     24          self.start_pd = 0.0
@@ -121,8 +122,13 @@ class GeneratedApproach:
  121    122                      world = [obj+self._world(p,theta) for p in pts]
  122    123                      return min(min(q[0]-.105,4.895-q[0],q[1]-.105,4.895-q[1]) for q in world)
  123    124                  frac = max((0.80, 0.68, 0.56), key=lever_clear)
         125 +                self.rot_cap = frac < 0.60
  124    126                  self.rot_y = -frac*lv
  125        -                far0 = obj + self._world(np.array([side*(width*.5+.34), self.rot_y]), theta)
         127 +                if self.rot_cap:
         128 +                    far_local0 = np.array([self.turn_sign*(lh*.5+.34), 0.0])
         129 +                else:
         130 +                    far_local0 = np.array([side*(width*.5+.34), self.rot_y])
         131 +                far0 = obj + self._world(far_local0, theta)
  126    132                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  127    133              elif pd > 0.018:
  128    134                  self.push_dir = dp / max(pd, 1e-9)
@@ -139,11 +145,17 @@ class GeneratedApproach:
  139    145          if self.mode.startswith("rot"):
  140    146              # Distal-stem side contact is a reliable long rotation lever.
  141    147              side = -self.turn_sign
  142        -            far_local = np.array([side * (width * 0.5 + 0.34), self.rot_y])
  143        -            contact_local = np.array([side * (width * 0.5 + 0.115), self.rot_y])
         148 +            if self.rot_cap:
         149 +                far_local = np.array([self.turn_sign*(lh*.5+.34), 0.0])
         150 +                contact_local = np.array([self.turn_sign*(lh*.5+.115), 0.0])
         151 +                local_force = np.array([-self.turn_sign, 0.0])
         152 +            else:
         153 +                far_local = np.array([side * (width * 0.5 + 0.34), self.rot_y])
         154 +                contact_local = np.array([side * (width * 0.5 + 0.115), self.rot_y])
         155 +                local_force = np.array([self.turn_sign, 0.0])
  144    156              far = obj + self._world(far_local, theta)
  145    157              contact = obj + self._world(contact_local, theta)
  146        -            force = self._world(np.array([self.turn_sign, 0.0]), theta)
         158 +            force = self._world(local_force, theta)
  147    159              if self.mode == "rot_far":
  148    160                  disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
  149    161                               abs(self._angle(theta-self.start_pose[2])) > 0.018)
```

</details>

<a id="C051"></a>
### C051 · Restrict cap torque to favorable CCW wall cases

Commit `5edfcb4e1919cd7bd8c4031e3c90283c525c196c`; parents: c083d05863968ac12cb0efdcea6e089f8c523d95. Recorded author date: 2026-09-09T09:04:36+02:00.

File roles (automatic): policy.

- [E0271](01_timeline.md#E0271): commit hash in recorded output.
[Controller after this commit](evidence/versions/C051_5edfcb4_approach.py) · [Exact all-file diff](evidence/diffs/C051_5edfcb4.diff)

[Previous saved controller snapshot](evidence/versions/C050_c083d05_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c01e080..ead97e3 100644
--- a/approach.py
+++ b/approach.py
@@ -122,7 +122,8 @@ class GeneratedApproach:
  122    122                      world = [obj+self._world(p,theta) for p in pts]
  123    123                      return min(min(q[0]-.105,4.895-q[0],q[1]-.105,4.895-q[1]) for q in world)
  124    124                  frac = max((0.80, 0.68, 0.56), key=lever_clear)
  125        -                self.rot_cap = frac < 0.60
         125 +                self.rot_cap = (frac < 0.60 and self.turn_sign > 0.0 and
         126 +                                (obj[1] < 1.30 or obj[1] > 3.70))
  126    127                  self.rot_y = -frac*lv
  127    128                  if self.rot_cap:
  128    129                      far_local0 = np.array([self.turn_sign*(lh*.5+.34), 0.0])
```

</details>

<a id="C052"></a>
### C052 · Persist effective cap contact after CCW wall activation

Commit `b8dfac8c28cff4db0dae9b3f94978427ac4ea099`; parents: 5edfcb4e1919cd7bd8c4031e3c90283c525c196c. Recorded author date: 2026-09-09T09:05:13+02:00.

File roles (automatic): policy.

- [E0277](01_timeline.md#E0277): commit hash in recorded output.
[Controller after this commit](evidence/versions/C052_b8dfac8_approach.py) · [Exact all-file diff](evidence/diffs/C052_b8dfac8.diff)

[Previous saved controller snapshot](evidence/versions/C051_5edfcb4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ead97e3..b5395b9 100644
--- a/approach.py
+++ b/approach.py
@@ -19,6 +19,7 @@ class GeneratedApproach:
   19     19          self.nav = []
   20     20          self.rot_y = -0.7
   21     21          self.rot_cap = False
          22 +        self.cap_preferred = False
   22     23          self.line_offset = 0.0
   23     24          self.force_move = False
   24     25          self.start_pd = 0.0
@@ -122,8 +123,10 @@ class GeneratedApproach:
  122    123                      world = [obj+self._world(p,theta) for p in pts]
  123    124                      return min(min(q[0]-.105,4.895-q[0],q[1]-.105,4.895-q[1]) for q in world)
  124    125                  frac = max((0.80, 0.68, 0.56), key=lever_clear)
  125        -                self.rot_cap = (frac < 0.60 and self.turn_sign > 0.0 and
  126        -                                (obj[1] < 1.30 or obj[1] > 3.70))
         126 +                if (frac < 0.60 and self.turn_sign > 0.0 and
         127 +                        (obj[1] < 1.30 or obj[1] > 3.70)):
         128 +                    self.cap_preferred = True
         129 +                self.rot_cap = self.cap_preferred and self.turn_sign > 0.0
  127    130                  self.rot_y = -frac*lv
  128    131                  if self.rot_cap:
  129    132                      far_local0 = np.array([self.turn_sign*(lh*.5+.34), 0.0])
```

</details>

<a id="C053"></a>
### C053 · Reuse activated cap contact for bidirectional corrections

Commit `63c97a2fa48e0b388c9e341d768b372ee7f58bab`; parents: b8dfac8c28cff4db0dae9b3f94978427ac4ea099. Recorded author date: 2026-09-09T09:05:46+02:00.

File roles (automatic): policy.

- [E0283](01_timeline.md#E0283): commit hash in recorded output.
[Controller after this commit](evidence/versions/C053_63c97a2_approach.py) · [Exact all-file diff](evidence/diffs/C053_63c97a2.diff)

[Previous saved controller snapshot](evidence/versions/C052_b8dfac8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b5395b9..6b13d6a 100644
--- a/approach.py
+++ b/approach.py
@@ -126,7 +126,7 @@ class GeneratedApproach:
  126    126                  if (frac < 0.60 and self.turn_sign > 0.0 and
  127    127                          (obj[1] < 1.30 or obj[1] > 3.70)):
  128    128                      self.cap_preferred = True
  129        -                self.rot_cap = self.cap_preferred and self.turn_sign > 0.0
         129 +                self.rot_cap = self.cap_preferred
  130    130                  self.rot_y = -frac*lv
  131    131                  if self.rot_cap:
  132    132                      far_local0 = np.array([self.turn_sign*(lh*.5+.34), 0.0])
```

</details>

<a id="C054"></a>
### C054 · Activate cap torque for CCW rotations near horizontal walls

Commit `b3e226e49b8647a9827c985233b18917857fbf9b`; parents: 63c97a2fa48e0b388c9e341d768b372ee7f58bab. Recorded author date: 2026-09-09T09:06:42+02:00.

File roles (automatic): policy.

- [E0291](01_timeline.md#E0291): commit hash in recorded output.
[Controller after this commit](evidence/versions/C054_b3e226e_approach.py) · [Exact all-file diff](evidence/diffs/C054_b3e226e.diff)

[Previous saved controller snapshot](evidence/versions/C053_63c97a2_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6b13d6a..a10eb09 100644
--- a/approach.py
+++ b/approach.py
@@ -123,7 +123,7 @@ class GeneratedApproach:
  123    123                      world = [obj+self._world(p,theta) for p in pts]
  124    124                      return min(min(q[0]-.105,4.895-q[0],q[1]-.105,4.895-q[1]) for q in world)
  125    125                  frac = max((0.80, 0.68, 0.56), key=lever_clear)
  126        -                if (frac < 0.60 and self.turn_sign > 0.0 and
         126 +                if (self.turn_sign > 0.0 and
  127    127                          (obj[1] < 1.30 or obj[1] > 3.70)):
  128    128                      self.cap_preferred = True
  129    129                  self.rot_cap = self.cap_preferred
```

</details>

<a id="C055"></a>
### C055 · Accelerate large residual rotations in open space

Commit `d1c4230591e884aa938f0bbcd15b5b687d32f00d`; parents: b3e226e49b8647a9827c985233b18917857fbf9b. Recorded author date: 2026-09-09T09:07:13+02:00.

File roles (automatic): policy.

- [E0297](01_timeline.md#E0297): commit hash in recorded output.
[Controller after this commit](evidence/versions/C055_d1c4230_approach.py) · [Exact all-file diff](evidence/diffs/C055_d1c4230.diff)

[Previous saved controller snapshot](evidence/versions/C054_b3e226e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a10eb09..3928c80 100644
--- a/approach.py
+++ b/approach.py
@@ -191,7 +191,7 @@ class GeneratedApproach:
  191    191                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  192    192                          or turned > turn_limit or self.count >= count_limit):
  193    193                      self.mode = "rot_retreat"
  194        -                speed = 0.014 if crowded else 0.022
         194 +                speed = 0.014 if crowded else (0.028 if abs(current_ae) > 1.0 else 0.022)
  195    195                  return self._safe(force, speed)
  196    196              if np.linalg.norm(robot - far) < 0.04:
  197    197                  if pd > 0.30 and pd > self.start_pd + 0.18:
```

</details>

<a id="C056"></a>
### C056 · Restore conservative rotation activation after held-out failures

Commit `39a5bcbf6ede4a5d69a9f75f2d8acd1d63e64ba6`; parents: d1c4230591e884aa938f0bbcd15b5b687d32f00d. Recorded author date: 2026-09-09T09:08:26+02:00.

File roles (automatic): policy.

- [E0305](01_timeline.md#E0305): commit hash in recorded output.
[Controller after this commit](evidence/versions/C056_39a5bcb_approach.py) · [Exact all-file diff](evidence/diffs/C056_39a5bcb.diff)

[Previous saved controller snapshot](evidence/versions/C055_d1c4230_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C053](#C053). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3928c80..6b13d6a 100644
--- a/approach.py
+++ b/approach.py
@@ -123,7 +123,7 @@ class GeneratedApproach:
  123    123                      world = [obj+self._world(p,theta) for p in pts]
  124    124                      return min(min(q[0]-.105,4.895-q[0],q[1]-.105,4.895-q[1]) for q in world)
  125    125                  frac = max((0.80, 0.68, 0.56), key=lever_clear)
  126        -                if (self.turn_sign > 0.0 and
         126 +                if (frac < 0.60 and self.turn_sign > 0.0 and
  127    127                          (obj[1] < 1.30 or obj[1] > 3.70)):
  128    128                      self.cap_preferred = True
  129    129                  self.rot_cap = self.cap_preferred
@@ -191,7 +191,7 @@ class GeneratedApproach:
  191    191                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  192    192                          or turned > turn_limit or self.count >= count_limit):
  193    193                      self.mode = "rot_retreat"
  194        -                speed = 0.014 if crowded else (0.028 if abs(current_ae) > 1.0 else 0.022)
         194 +                speed = 0.014 if crowded else 0.022
  195    195                  return self._safe(force, speed)
  196    196              if np.linalg.norm(robot - far) < 0.04:
  197    197                  if pd > 0.30 and pd > self.start_pd + 0.18:
```

</details>

<a id="C057"></a>
### C057 · Choose rotation contact that also advances toward goal

Commit `4abcf8efb909152855bcb7b8400013a7e0c4c572`; parents: 39a5bcbf6ede4a5d69a9f75f2d8acd1d63e64ba6. Recorded author date: 2026-09-09T09:09:26+02:00.

File roles (automatic): policy.

- [E0314](01_timeline.md#E0314): commit hash in recorded output.
[Controller after this commit](evidence/versions/C057_4abcf8e_approach.py) · [Exact all-file diff](evidence/diffs/C057_4abcf8e.diff)

[Previous saved controller snapshot](evidence/versions/C056_39a5bcb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6b13d6a..c429300 100644
--- a/approach.py
+++ b/approach.py
@@ -126,7 +126,12 @@ class GeneratedApproach:
  126    126                  if (frac < 0.60 and self.turn_sign > 0.0 and
  127    127                          (obj[1] < 1.30 or obj[1] > 3.70)):
  128    128                      self.cap_preferred = True
  129        -                self.rot_cap = self.cap_preferred
         129 +                stem_force_world = self._world(np.array([self.turn_sign, 0.0]), theta)
         130 +                # Stem-side and cap-end contacts create the same torque with
         131 +                # opposite linear components. Prefer the one that also moves
         132 +                # toward the goal instead of later undoing rotation drift.
         133 +                helps_position = float(np.dot(stem_force_world, dp)) >= 0.0
         134 +                self.rot_cap = self.cap_preferred or not helps_position
  130    135                  self.rot_y = -frac*lv
  131    136                  if self.rot_cap:
  132    137                      far_local0 = np.array([self.turn_sign*(lh*.5+.34), 0.0])
```

</details>

<a id="C058"></a>
### C058 · Switch torque contacts only for meaningful position progress

Commit `dc01eb936305e953e6410973e5e0eb92dbc99381`; parents: 4abcf8efb909152855bcb7b8400013a7e0c4c572. Recorded author date: 2026-09-09T09:10:53+02:00.

File roles (automatic): policy.

- [E0324](01_timeline.md#E0324): commit hash in recorded output.
[Controller after this commit](evidence/versions/C058_dc01eb9_approach.py) · [Exact all-file diff](evidence/diffs/C058_dc01eb9.diff)

[Previous saved controller snapshot](evidence/versions/C057_4abcf8e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c429300..b2925be 100644
--- a/approach.py
+++ b/approach.py
@@ -130,7 +130,7 @@ class GeneratedApproach:
  130    130                  # Stem-side and cap-end contacts create the same torque with
  131    131                  # opposite linear components. Prefer the one that also moves
  132    132                  # toward the goal instead of later undoing rotation drift.
  133        -                helps_position = float(np.dot(stem_force_world, dp)) >= 0.0
         133 +                helps_position = float(np.dot(stem_force_world, dp)) >= -0.20*pd
  134    134                  self.rot_cap = self.cap_preferred or not helps_position
  135    135                  self.rot_y = -frac*lv
  136    136                  if self.rot_cap:
```

</details>

<a id="C059"></a>
### C059 · Tune rotation contact progress threshold

Commit `7c40b651904a9bd63888e5930d720b612dbbd13f`; parents: dc01eb936305e953e6410973e5e0eb92dbc99381. Recorded author date: 2026-09-09T09:11:25+02:00.

File roles (automatic): policy.

- [E0330](01_timeline.md#E0330): commit hash in recorded output.
[Controller after this commit](evidence/versions/C059_7c40b65_approach.py) · [Exact all-file diff](evidence/diffs/C059_7c40b65.diff)

[Previous saved controller snapshot](evidence/versions/C058_dc01eb9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b2925be..748faac 100644
--- a/approach.py
+++ b/approach.py
@@ -130,7 +130,7 @@ class GeneratedApproach:
  130    130                  # Stem-side and cap-end contacts create the same torque with
  131    131                  # opposite linear components. Prefer the one that also moves
  132    132                  # toward the goal instead of later undoing rotation drift.
  133        -                helps_position = float(np.dot(stem_force_world, dp)) >= -0.20*pd
         133 +                helps_position = float(np.dot(stem_force_world, dp)) >= -0.10*pd
  134    134                  self.rot_cap = self.cap_preferred or not helps_position
  135    135                  self.rot_y = -frac*lv
  136    136                  if self.rot_cap:
```

</details>

<a id="C060"></a>
### C060 · Restore best validated contact selection threshold

Commit `e57d51fef9a6ee197610699685013df6bbb61fd9`; parents: 7c40b651904a9bd63888e5930d720b612dbbd13f. Recorded author date: 2026-09-09T09:11:48+02:00.

File roles (automatic): policy.

- [E0336](01_timeline.md#E0336): commit hash in recorded output.
[Controller after this commit](evidence/versions/C060_e57d51f_approach.py) · [Exact all-file diff](evidence/diffs/C060_e57d51f.diff)

[Previous saved controller snapshot](evidence/versions/C059_7c40b65_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C058](#C058). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 748faac..b2925be 100644
--- a/approach.py
+++ b/approach.py
@@ -130,7 +130,7 @@ class GeneratedApproach:
  130    130                  # Stem-side and cap-end contacts create the same torque with
  131    131                  # opposite linear components. Prefer the one that also moves
  132    132                  # toward the goal instead of later undoing rotation drift.
  133        -                helps_position = float(np.dot(stem_force_world, dp)) >= -0.10*pd
         133 +                helps_position = float(np.dot(stem_force_world, dp)) >= -0.20*pd
  134    134                  self.rot_cap = self.cap_preferred or not helps_position
  135    135                  self.rot_y = -frac*lv
  136    136                  if self.rot_cap:
```

</details>

<a id="C061"></a>
### C061 · Increase final translation speed within safe release margin

Commit `ab1562e92357e2214afdc2df4cfc4b3a105b39bd`; parents: e57d51fef9a6ee197610699685013df6bbb61fd9. Recorded author date: 2026-09-09T09:12:26+02:00.

File roles (automatic): policy.

- [E0342](01_timeline.md#E0342): commit hash in recorded output.
[Controller after this commit](evidence/versions/C061_ab1562e_approach.py) · [Exact all-file diff](evidence/diffs/C061_ab1562e.diff)

[Previous saved controller snapshot](evidence/versions/C060_e57d51f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b2925be..2bad0aa 100644
--- a/approach.py
+++ b/approach.py
@@ -254,7 +254,7 @@ class GeneratedApproach:
  254    254                      self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  255    255                  self.mode = "move_retreat"
  256    256                  self.retreat_count = 0
  257        -            speed = 0.012 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
         257 +            speed = 0.016 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
  258    258              return self._safe((com + self.push_dir * 0.20) - robot, speed)
  259    259          # Break contact along the exact reverse push direction. Recomputing a
  260    260          # COM-relative far point after the T rotates can route through the T.
```

</details>

<a id="C062"></a>
### C062 · Keep forced recovery displacement bounded

Commit `3db2f59ad5697179ba73d6345578e9eee4d4212a`; parents: ab1562e92357e2214afdc2df4cfc4b3a105b39bd. Recorded author date: 2026-09-09T09:15:00+02:00.

File roles (automatic): policy.

- [E0364](01_timeline.md#E0364): commit hash in recorded output.
[Controller after this commit](evidence/versions/C062_3db2f59_approach.py) · [Exact all-file diff](evidence/diffs/C062_3db2f59.diff)

[Previous saved controller snapshot](evidence/versions/C061_ab1562e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2bad0aa..2150053 100644
--- a/approach.py
+++ b/approach.py
@@ -242,7 +242,8 @@ class GeneratedApproach:
  242    242                  self.mode = "move_retreat"
  243    243                  self.retreat_count = 0
  244    244                  return self._safe(-self.push_dir, 0.018)
  245        -            if moved > 0.11 and (now_ae < 0.14 or near_boundary or self.force_move) and pd > 0.05:
         245 +            if (not self.force_move and moved > 0.11 and
         246 +                    (now_ae < 0.14 or near_boundary) and pd > 0.05):
  246    247                  dtheta = self._angle(theta-self.start_pose[2])
  247    248                  self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  248    249                  self.start_pose = np.array([obj[0], obj[1], theta])
```

</details>

<a id="C063"></a>
### C063 · Amortize bounded recovery contact over useful distance

Commit `8bd11dfef76a056c4d5dbb87497bbec6a95faab2`; parents: 3db2f59ad5697179ba73d6345578e9eee4d4212a. Recorded author date: 2026-09-09T09:15:43+02:00.

File roles (automatic): policy.

- [E0370](01_timeline.md#E0370): commit hash in recorded output.
[Controller after this commit](evidence/versions/C063_8bd11df_approach.py) · [Exact all-file diff](evidence/diffs/C063_8bd11df.diff)

[Previous saved controller snapshot](evidence/versions/C062_3db2f59_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2150053..bce4c7f 100644
--- a/approach.py
+++ b/approach.py
@@ -237,7 +237,7 @@ class GeneratedApproach:
  237    237              # Once contact is established, keep following through in short
  238    238              # closed-loop segments instead of paying to reacquire every time.
  239    239              near_boundary = min(obj) < 0.96 or max(obj) > 4.04
  240        -            if self.force_move and moved > 0.18:
         240 +            if self.force_move and moved > 0.34:
  241    241                  self.force_move = False
  242    242                  self.mode = "move_retreat"
  243    243                  self.retreat_count = 0
```

</details>

<a id="C064"></a>
### C064 · Use longer goal-directed recovery strokes

Commit `c5ab694aa1b9a802cc64d3b8c6b1d33986d3d12a`; parents: 8bd11dfef76a056c4d5dbb87497bbec6a95faab2. Recorded author date: 2026-09-09T09:16:14+02:00.

File roles (automatic): policy.

- [E0376](01_timeline.md#E0376): commit hash in recorded output.
[Controller after this commit](evidence/versions/C064_c5ab694_approach.py) · [Exact all-file diff](evidence/diffs/C064_c5ab694.diff)

[Previous saved controller snapshot](evidence/versions/C063_8bd11df_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bce4c7f..3d51f31 100644
--- a/approach.py
+++ b/approach.py
@@ -237,7 +237,7 @@ class GeneratedApproach:
  237    237              # Once contact is established, keep following through in short
  238    238              # closed-loop segments instead of paying to reacquire every time.
  239    239              near_boundary = min(obj) < 0.96 or max(obj) > 4.04
  240        -            if self.force_move and moved > 0.34:
         240 +            if self.force_move and moved > 0.55:
  241    241                  self.force_move = False
  242    242                  self.mode = "move_retreat"
  243    243                  self.retreat_count = 0
```

</details>

<a id="C065"></a>
### C065 · Use transformed T footprint for boundary recovery

Commit `47f8a11905c53f94b442187454849ef3dce742a5`; parents: c5ab694aa1b9a802cc64d3b8c6b1d33986d3d12a. Recorded author date: 2026-09-09T09:17:09+02:00.

File roles (automatic): policy.

- [E0382](01_timeline.md#E0382): commit hash in recorded output.
[Controller after this commit](evidence/versions/C065_47f8a11_approach.py) · [Exact all-file diff](evidence/diffs/C065_47f8a11.diff)

[Previous saved controller snapshot](evidence/versions/C064_c5ab694_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3d51f31..49acfd4 100644
--- a/approach.py
+++ b/approach.py
@@ -107,10 +107,17 @@ class GeneratedApproach:
  107    107          ae = self._angle(goal_theta - theta)
  108    108          dp = goal - obj
  109    109          pd = float(np.linalg.norm(dp))
         110 +        local_outline = [(-lh*.5, -width*.5), (lh*.5, -width*.5),
         111 +                         (-lh*.5, width*.5), (lh*.5, width*.5),
         112 +                         (-width*.5, -lv), (width*.5, -lv)]
         113 +        outline = np.array([obj + self._world(np.array(p), theta)
         114 +                            for p in local_outline])
         115 +        footprint_crowded = (float(np.min(outline)) < 0.42 or
         116 +                             float(np.max(outline)) > 4.58)
  110    117  
  111    118          if self.mode == "choose":
  112    119              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  113        -            boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
         120 +            boundary_recover = footprint_crowded
  114    121              if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover and not self.force_move:
  115    122                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  116    123                  self.mode = "rot_far"
@@ -189,7 +196,7 @@ class GeneratedApproach:
  189    196                  self.count += 1
  190    197                  current_ae = self._angle(goal_theta - theta)
  191    198                  turned = abs(self._angle(theta - self.start_pose[2]))
  192        -                crowded = min(obj) < 0.95 or max(obj) > 4.05
         199 +                crowded = footprint_crowded
  193    200                  edge_zone = min(obj) < 1.20 or max(obj) > 3.80
  194    201                  turn_limit = 0.12 if crowded else (0.22 if edge_zone else 0.18)
  195    202                  count_limit = 8 if crowded else (11 if edge_zone else 9)
@@ -236,7 +243,7 @@ class GeneratedApproach:
  236    243                  return self._safe(-self.push_dir, 0.018)
  237    244              # Once contact is established, keep following through in short
  238    245              # closed-loop segments instead of paying to reacquire every time.
  239        -            near_boundary = min(obj) < 0.96 or max(obj) > 4.04
         246 +            near_boundary = footprint_crowded
  240    247              if self.force_move and moved > 0.55:
  241    248                  self.force_move = False
  242    249                  self.mode = "move_retreat"
```

</details>

<a id="C066"></a>
### C066 · Restore validated center-based recovery thresholds

Commit `09d0ca9db6096dfb15174a4f123cbdfd2d56a057`; parents: 47f8a11905c53f94b442187454849ef3dce742a5. Recorded author date: 2026-09-09T09:17:57+02:00.

File roles (automatic): policy.

- [E0388](01_timeline.md#E0388): commit hash in recorded output.
[Controller after this commit](evidence/versions/C066_09d0ca9_approach.py) · [Exact all-file diff](evidence/diffs/C066_09d0ca9.diff)

[Previous saved controller snapshot](evidence/versions/C065_47f8a11_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C064](#C064). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 49acfd4..3d51f31 100644
--- a/approach.py
+++ b/approach.py
@@ -107,17 +107,10 @@ class GeneratedApproach:
  107    107          ae = self._angle(goal_theta - theta)
  108    108          dp = goal - obj
  109    109          pd = float(np.linalg.norm(dp))
  110        -        local_outline = [(-lh*.5, -width*.5), (lh*.5, -width*.5),
  111        -                         (-lh*.5, width*.5), (lh*.5, width*.5),
  112        -                         (-width*.5, -lv), (width*.5, -lv)]
  113        -        outline = np.array([obj + self._world(np.array(p), theta)
  114        -                            for p in local_outline])
  115        -        footprint_crowded = (float(np.min(outline)) < 0.42 or
  116        -                             float(np.max(outline)) > 4.58)
  117    110  
  118    111          if self.mode == "choose":
  119    112              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  120        -            boundary_recover = footprint_crowded
         113 +            boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
  121    114              if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover and not self.force_move:
  122    115                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  123    116                  self.mode = "rot_far"
@@ -196,7 +189,7 @@ class GeneratedApproach:
  196    189                  self.count += 1
  197    190                  current_ae = self._angle(goal_theta - theta)
  198    191                  turned = abs(self._angle(theta - self.start_pose[2]))
  199        -                crowded = footprint_crowded
         192 +                crowded = min(obj) < 0.95 or max(obj) > 4.05
  200    193                  edge_zone = min(obj) < 1.20 or max(obj) > 3.80
  201    194                  turn_limit = 0.12 if crowded else (0.22 if edge_zone else 0.18)
  202    195                  count_limit = 8 if crowded else (11 if edge_zone else 9)
@@ -243,7 +236,7 @@ class GeneratedApproach:
  243    236                  return self._safe(-self.push_dir, 0.018)
  244    237              # Once contact is established, keep following through in short
  245    238              # closed-loop segments instead of paying to reacquire every time.
  246        -            near_boundary = footprint_crowded
         239 +            near_boundary = min(obj) < 0.96 or max(obj) > 4.04
  247    240              if self.force_move and moved > 0.55:
  248    241                  self.force_move = False
  249    242                  self.mode = "move_retreat"
```

</details>

<a id="C067"></a>
### C067 · Shorten straight retreat after contact separation

Commit `3d77208780cf2c0b6927bed7e2f9ee491144cb5f`; parents: 09d0ca9db6096dfb15174a4f123cbdfd2d56a057. Recorded author date: 2026-09-09T09:18:58+02:00.

File roles (automatic): policy.

- [E0398](01_timeline.md#E0398): commit hash in recorded output.
[Controller after this commit](evidence/versions/C067_3d77208_approach.py) · [Exact all-file diff](evidence/diffs/C067_3d77208.diff)

[Previous saved controller snapshot](evidence/versions/C066_09d0ca9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3d51f31..c0d2f35 100644
--- a/approach.py
+++ b/approach.py
@@ -260,6 +260,6 @@ class GeneratedApproach:
  260    260          # Break contact along the exact reverse push direction. Recomputing a
  261    261          # COM-relative far point after the T rotates can route through the T.
  262    262          self.retreat_count += 1
  263        -        if self.retreat_count >= 12:
         263 +        if self.retreat_count >= 8:
  264    264              self.mode = "choose"
  265    265          return self._safe(-self.push_dir, 0.035)
```

</details>

<a id="C068"></a>
### C068 · Use direct final contact setup near positional goal

Commit `98e64bb8cc1696c92919bdc3618bf2c14d160e1b`; parents: 3d77208780cf2c0b6927bed7e2f9ee491144cb5f. Recorded author date: 2026-09-09T09:19:41+02:00.

File roles (automatic): policy.

- [E0404](01_timeline.md#E0404): commit hash in recorded output.
[Controller after this commit](evidence/versions/C068_98e64bb_approach.py) · [Exact all-file diff](evidence/diffs/C068_98e64bb.diff)

[Previous saved controller snapshot](evidence/versions/C067_3d77208_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c0d2f35..dfe391d 100644
--- a/approach.py
+++ b/approach.py
@@ -146,6 +146,8 @@ class GeneratedApproach:
  146    146                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  147    147                  far0 = np.clip(com0 - self.push_dir*0.82, 0.105, 4.895)
  148    148                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
         149 +                if pd < 0.15:
         150 +                    self.nav = []
  149    151              else:
  150    152                  return np.zeros(2, dtype=float)
  151    153              self.count = 0
```

</details>

<a id="C069"></a>
### C069 · Continue useful incidental contact during translation setup

Commit `b7bbb822f69212ac36bbeccf9e7f237a3edc8d37`; parents: 98e64bb8cc1696c92919bdc3618bf2c14d160e1b. Recorded author date: 2026-09-09T09:21:05+02:00.

File roles (automatic): policy.

- [E0417](01_timeline.md#E0417): commit hash in recorded output.
[Controller after this commit](evidence/versions/C069_b7bbb82_approach.py) · [Exact all-file diff](evidence/diffs/C069_b7bbb82.diff)

[Previous saved controller snapshot](evidence/versions/C068_98e64bb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index dfe391d..4f58a52 100644
--- a/approach.py
+++ b/approach.py
@@ -142,6 +142,7 @@ class GeneratedApproach:
  142    142              elif pd > 0.018:
  143    143                  self.push_dir = dp / max(pd, 1e-9)
  144    144                  self.mode = "move_far"
         145 +                self.start_pd = pd
  145    146                  com0 = obj + self._world(np.array([0.0, -0.36*lv]), theta)
  146    147                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  147    148                  far0 = np.clip(com0 - self.push_dir*0.82, 0.105, 4.895)
@@ -214,6 +215,11 @@ class GeneratedApproach:
  214    215              disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
  215    216                           abs(self._angle(theta-self.start_pose[2])) > 0.018)
  216    217              if disturbed:
         218 +                if pd < self.start_pd - 0.002 and abs(ae) < 0.16:
         219 +                    self.mode, self.nav = "move_push", []
         220 +                    self.count = 0
         221 +                    self.start_pose = np.array([obj[0], obj[1], theta])
         222 +                    return self._safe((com + self.push_dir*0.20)-robot, 0.024)
  217    223                  self.mode, self.nav = "choose", []
  218    224                  return self._safe(robot-obj, 0.035)
  219    225              while self.nav and np.linalg.norm(robot - self.nav[0]) < 0.045:
```

</details>

<a id="C070"></a>
### C070 · Limit incidental-contact continuation to final approach

Commit `4574f1b7af9ad0c34f8ed29726d1301f6de88917`; parents: b7bbb822f69212ac36bbeccf9e7f237a3edc8d37. Recorded author date: 2026-09-09T09:21:36+02:00.

File roles (automatic): policy.

- [E0423](01_timeline.md#E0423): commit hash in recorded output.
[Controller after this commit](evidence/versions/C070_4574f1b_approach.py) · [Exact all-file diff](evidence/diffs/C070_4574f1b.diff)

[Previous saved controller snapshot](evidence/versions/C069_b7bbb82_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4f58a52..e44242d 100644
--- a/approach.py
+++ b/approach.py
@@ -215,7 +215,7 @@ class GeneratedApproach:
  215    215              disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
  216    216                           abs(self._angle(theta-self.start_pose[2])) > 0.018)
  217    217              if disturbed:
  218        -                if pd < self.start_pd - 0.002 and abs(ae) < 0.16:
         218 +                if pd < 0.60 and pd < self.start_pd - 0.002 and abs(ae) < 0.16:
  219    219                      self.mode, self.nav = "move_push", []
  220    220                      self.count = 0
  221    221                      self.start_pose = np.array([obj[0], obj[1], theta])
```

</details>

<a id="C071"></a>
### C071 · Tighten opportunistic final-contact continuation

Commit `1edc02f2726e33284c0d7c5adc202c02fb643d8d`; parents: 4574f1b7af9ad0c34f8ed29726d1301f6de88917. Recorded author date: 2026-09-09T09:22:06+02:00.

File roles (automatic): policy.

- [E0429](01_timeline.md#E0429): commit hash in recorded output.
[Controller after this commit](evidence/versions/C071_1edc02f_approach.py) · [Exact all-file diff](evidence/diffs/C071_1edc02f.diff)

[Previous saved controller snapshot](evidence/versions/C070_4574f1b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e44242d..0cde859 100644
--- a/approach.py
+++ b/approach.py
@@ -215,7 +215,7 @@ class GeneratedApproach:
  215    215              disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
  216    216                           abs(self._angle(theta-self.start_pose[2])) > 0.018)
  217    217              if disturbed:
  218        -                if pd < 0.60 and pd < self.start_pd - 0.002 and abs(ae) < 0.16:
         218 +                if pd < 0.45 and pd < self.start_pd - 0.002 and abs(ae) < 0.16:
  219    219                      self.mode, self.nav = "move_push", []
  220    220                      self.count = 0
  221    221                      self.start_pose = np.array([obj[0], obj[1], theta])
```

</details>

<a id="C072"></a>
### C072 · Remove unsafe incidental-contact continuation

Commit `c6a707e93f3919e40ab6c9dc8897f64299fe0c64`; parents: 1edc02f2726e33284c0d7c5adc202c02fb643d8d. Recorded author date: 2026-09-09T09:22:42+02:00.

File roles (automatic): policy.

- [E0435](01_timeline.md#E0435): commit hash in recorded output.
[Controller after this commit](evidence/versions/C072_c6a707e_approach.py) · [Exact all-file diff](evidence/diffs/C072_c6a707e.diff)

[Previous saved controller snapshot](evidence/versions/C071_1edc02f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0cde859..faca0a6 100644
--- a/approach.py
+++ b/approach.py
@@ -215,11 +215,6 @@ class GeneratedApproach:
  215    215              disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
  216    216                           abs(self._angle(theta-self.start_pose[2])) > 0.018)
  217    217              if disturbed:
  218        -                if pd < 0.45 and pd < self.start_pd - 0.002 and abs(ae) < 0.16:
  219        -                    self.mode, self.nav = "move_push", []
  220        -                    self.count = 0
  221        -                    self.start_pose = np.array([obj[0], obj[1], theta])
  222        -                    return self._safe((com + self.push_dir*0.20)-robot, 0.024)
  223    218                  self.mode, self.nav = "choose", []
  224    219                  return self._safe(robot-obj, 0.035)
  225    220              while self.nav and np.linalg.norm(robot - self.nav[0]) < 0.045:
```

</details>

<a id="C073"></a>
### C073 · Use direct rotation setup at final position

Commit `f76f1781b9d028e5ba33d8d23f238bcd341494c2`; parents: c6a707e93f3919e40ab6c9dc8897f64299fe0c64. Recorded author date: 2026-09-09T09:23:53+02:00.

File roles (automatic): policy.

- [E0447](01_timeline.md#E0447): commit hash in recorded output.
[Controller after this commit](evidence/versions/C073_f76f178_approach.py) · [Exact all-file diff](evidence/diffs/C073_f76f178.diff)

[Previous saved controller snapshot](evidence/versions/C072_c6a707e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index faca0a6..be65f67 100644
--- a/approach.py
+++ b/approach.py
@@ -139,6 +139,8 @@ class GeneratedApproach:
  139    139                      far_local0 = np.array([side*(width*.5+.34), self.rot_y])
  140    140                  far0 = obj + self._world(far_local0, theta)
  141    141                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
         142 +                if pd < 0.05:
         143 +                    self.nav = []
  142    144              elif pd > 0.018:
  143    145                  self.push_dir = dp / max(pd, 1e-9)
  144    146                  self.mode = "move_far"
```

</details>

<a id="C074"></a>
### C074 · Restore planned final rotation approach

Commit `f20ffb6312668550c1e2cf2e7f32f3ef7f036f1b`; parents: f76f1781b9d028e5ba33d8d23f238bcd341494c2. Recorded author date: 2026-09-09T09:24:19+02:00.

File roles (automatic): policy.

- [E0453](01_timeline.md#E0453): commit hash in recorded output.
[Controller after this commit](evidence/versions/C074_f20ffb6_approach.py) · [Exact all-file diff](evidence/diffs/C074_f20ffb6.diff)

[Previous saved controller snapshot](evidence/versions/C073_f76f178_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C072](#C072). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index be65f67..faca0a6 100644
--- a/approach.py
+++ b/approach.py
@@ -139,8 +139,6 @@ class GeneratedApproach:
  139    139                      far_local0 = np.array([side*(width*.5+.34), self.rot_y])
  140    140                  far0 = obj + self._world(far_local0, theta)
  141    141                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  142        -                if pd < 0.05:
  143        -                    self.nav = []
  144    142              elif pd > 0.018:
  145    143                  self.push_dir = dp / max(pd, 1e-9)
  146    144                  self.mode = "move_far"
```

</details>

<a id="C075"></a>
### C075 · initial sandbox setup

Commit `1c7f1008a670dbfd03570a2aca017b1c05e7c025`; parents: f20ffb6312668550c1e2cf2e7f32f3ef7f036f1b. Recorded author date: 2026-09-09T09:24:44+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C075_1c7f100.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 410a176..4b9f4bf 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $15.71. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $7.57. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C076"></a>
### C076 · Align planned and runtime translation staging targets

Commit `1c8a0e6b6f9517ff059688b5c58c108dfbaabc36`; parents: 1c7f1008a670dbfd03570a2aca017b1c05e7c025. Recorded author date: 2026-09-09T09:25:27+02:00.

File roles (automatic): policy.

- [E0468](01_timeline.md#E0468): commit hash in recorded output.
[Controller after this commit](evidence/versions/C076_1c8a0e6_approach.py) · [Exact all-file diff](evidence/diffs/C076_1c8a0e6.diff)

[Previous saved controller snapshot](evidence/versions/C074_f20ffb6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index faca0a6..846f21e 100644
--- a/approach.py
+++ b/approach.py
@@ -145,7 +145,7 @@ class GeneratedApproach:
  145    145                  self.start_pd = pd
  146    146                  com0 = obj + self._world(np.array([0.0, -0.36*lv]), theta)
  147    147                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  148        -                far0 = np.clip(com0 - self.push_dir*0.82, 0.105, 4.895)
         148 +                far0 = np.clip(com0 - self.push_dir*0.76, 0.105, 4.895)
  149    149                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  150    150                  if pd < 0.15:
  151    151                      self.nav = []
```

</details>

<a id="C077"></a>
### C077 · Reverse immediately when translation stroke expires

Commit `77f29bd95fea7291457ef0126cdf07930c4de354`; parents: 1c8a0e6b6f9517ff059688b5c58c108dfbaabc36. Recorded author date: 2026-09-09T09:26:38+02:00.

File roles (automatic): policy.

- [E0476](01_timeline.md#E0476): commit hash in recorded output.
[Controller after this commit](evidence/versions/C077_77f29bd_approach.py) · [Exact all-file diff](evidence/diffs/C077_77f29bd.diff)

[Previous saved controller snapshot](evidence/versions/C076_1c8a0e6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 846f21e..67aa406 100644
--- a/approach.py
+++ b/approach.py
@@ -258,6 +258,7 @@ class GeneratedApproach:
  258    258                      self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
  259    259                  self.mode = "move_retreat"
  260    260                  self.retreat_count = 0
         261 +                return self._safe(-self.push_dir, 0.018)
  261    262              speed = 0.016 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
  262    263              return self._safe((com + self.push_dir * 0.20) - robot, speed)
  263    264          # Break contact along the exact reverse push direction. Recomputing a
```

</details>

<a id="C078"></a>
### C078 · Restore validated final stroke follow-through

Commit `4063195103a988b29324549a425e2b6901e9bca5`; parents: 77f29bd95fea7291457ef0126cdf07930c4de354. Recorded author date: 2026-09-09T09:27:08+02:00.

File roles (automatic): policy.

- [E0482](01_timeline.md#E0482): commit hash in recorded output.
[Controller after this commit](evidence/versions/C078_4063195_approach.py) · [Exact all-file diff](evidence/diffs/C078_4063195.diff)

[Previous saved controller snapshot](evidence/versions/C077_77f29bd_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 67aa406..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -236,7 +236,6 @@ class GeneratedApproach:
  236    236                  self.force_move = False
  237    237                  self.mode = "move_retreat"
  238    238                  self.retreat_count = 0
  239        -                return self._safe(-self.push_dir, 0.018)
  240    239              # Once contact is established, keep following through in short
  241    240              # closed-loop segments instead of paying to reacquire every time.
  242    241              near_boundary = min(obj) < 0.96 or max(obj) > 4.04
```

</details>

<a id="C079"></a>
### C079 · Begin rotation retreat without an extra torque step

Commit `de2487e5d3c89130ce3f53d91e4125851f3c6d7f`; parents: 4063195103a988b29324549a425e2b6901e9bca5. Recorded author date: 2026-09-09T09:27:58+02:00.

File roles (automatic): policy.

- [E0488](01_timeline.md#E0488): commit hash in recorded output.
[Controller after this commit](evidence/versions/C079_de2487e_approach.py) · [Exact all-file diff](evidence/diffs/C079_de2487e.diff)

[Previous saved controller snapshot](evidence/versions/C078_4063195_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b72fad0..76bdd56 100644
--- a/approach.py
+++ b/approach.py
@@ -199,6 +199,7 @@ class GeneratedApproach:
  199    199                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  200    200                          or turned > turn_limit or self.count >= count_limit):
  201    201                      self.mode = "rot_retreat"
         202 +                    return self._safe(far - robot, 0.035)
  202    203                  speed = 0.014 if crowded else 0.022
  203    204                  return self._safe(force, speed)
  204    205              if np.linalg.norm(robot - far) < 0.04:
```

</details>

<a id="C080"></a>
### C080 · Keep empirically validated rotation follow-through

Commit `6aeb0f9cdd1f7f56371c7c9610b886bc356e6f52`; parents: de2487e5d3c89130ce3f53d91e4125851f3c6d7f. Recorded author date: 2026-09-09T09:28:26+02:00.

File roles (automatic): policy.

- [E0494](01_timeline.md#E0494): commit hash in recorded output.
[Controller after this commit](evidence/versions/C080_6aeb0f9_approach.py) · [Exact all-file diff](evidence/diffs/C080_6aeb0f9.diff)

[Previous saved controller snapshot](evidence/versions/C079_de2487e_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C078](#C078). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 76bdd56..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -199,7 +199,6 @@ class GeneratedApproach:
  199    199                  if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
  200    200                          or turned > turn_limit or self.count >= count_limit):
  201    201                      self.mode = "rot_retreat"
  202        -                    return self._safe(far - robot, 0.035)
  203    202                  speed = 0.014 if crowded else 0.022
  204    203                  return self._safe(force, speed)
  205    204              if np.linalg.norm(robot - far) < 0.04:
```

</details>

<a id="C081"></a>
### C081 · initial sandbox setup

Commit `6923450058217280acd3f03fce2807f2675eeb23`; parents: 6aeb0f9cdd1f7f56371c7c9610b886bc356e6f52. Recorded author date: 2026-09-09T09:29:32+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C081_6923450.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 4b9f4bf..91ef92d 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $7.57. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $6.03. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C082"></a>
### C082 · Tighten direct final-contact shortcut

Commit `676681812668a84c9c7d05ad1ad6132864b4ff5e`; parents: 6923450058217280acd3f03fce2807f2675eeb23. Recorded author date: 2026-09-09T09:30:15+02:00.

File roles (automatic): policy.

- [E0514](01_timeline.md#E0514): commit hash in recorded output.
[Controller after this commit](evidence/versions/C082_6766818_approach.py) · [Exact all-file diff](evidence/diffs/C082_6766818.diff)

[Previous saved controller snapshot](evidence/versions/C080_6aeb0f9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b72fad0..45b3695 100644
--- a/approach.py
+++ b/approach.py
@@ -147,7 +147,7 @@ class GeneratedApproach:
  147    147                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  148    148                  far0 = np.clip(com0 - self.push_dir*0.76, 0.105, 4.895)
  149    149                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  150        -                if pd < 0.15:
         150 +                if pd < 0.08:
  151    151                      self.nav = []
  152    152              else:
  153    153                  return np.zeros(2, dtype=float)
```

</details>

<a id="C083"></a>
### C083 · Restore validated final-contact distance

Commit `4c017c70403d6888a1e6a47880fe38583187678a`; parents: 676681812668a84c9c7d05ad1ad6132864b4ff5e. Recorded author date: 2026-09-09T09:30:53+02:00.

File roles (automatic): policy.

- [E0520](01_timeline.md#E0520): commit hash in recorded output.
[Controller after this commit](evidence/versions/C083_4c017c7_approach.py) · [Exact all-file diff](evidence/diffs/C083_4c017c7.diff)

[Previous saved controller snapshot](evidence/versions/C082_6766818_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C078](#C078), [C080](#C080). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 45b3695..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -147,7 +147,7 @@ class GeneratedApproach:
  147    147                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  148    148                  far0 = np.clip(com0 - self.push_dir*0.76, 0.105, 4.895)
  149    149                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  150        -                if pd < 0.08:
         150 +                if pd < 0.15:
  151    151                      self.nav = []
  152    152              else:
  153    153                  return np.zeros(2, dtype=float)
```

</details>

<a id="C084"></a>
### C084 · Reduce unnecessary near-tolerance rotation cycles

Commit `5a4bc815b96c515d6a66d86b5dfbcd959f759b03`; parents: 4c017c70403d6888a1e6a47880fe38583187678a. Recorded author date: 2026-09-09T09:31:03+02:00.

File roles (automatic): policy.

- [E0524](01_timeline.md#E0524): commit hash in recorded output.
[Controller after this commit](evidence/versions/C084_5a4bc81_approach.py) · [Exact all-file diff](evidence/diffs/C084_5a4bc81.diff)

[Previous saved controller snapshot](evidence/versions/C083_4c017c7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b72fad0..9497113 100644
--- a/approach.py
+++ b/approach.py
@@ -111,7 +111,7 @@ class GeneratedApproach:
  111    111          if self.mode == "choose":
  112    112              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  113    113              boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
  114        -            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover and not self.force_move:
         114 +            if (abs(ae) > 0.12 or branch_mismatch) and not boundary_recover and not self.force_move:
  115    115                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  116    116                  self.mode = "rot_far"
  117    117                  side = -self.turn_sign
```

</details>

<a id="C085"></a>
### C085 · Restore conservative orientation correction threshold

Commit `6bfc26e0f56d461a6afe0148b2286916e6eb2559`; parents: 5a4bc815b96c515d6a66d86b5dfbcd959f759b03. Recorded author date: 2026-09-09T09:31:42+02:00.

File roles (automatic): policy.

- [E0530](01_timeline.md#E0530): commit hash in recorded output.
[Controller after this commit](evidence/versions/C085_6bfc26e_approach.py) · [Exact all-file diff](evidence/diffs/C085_6bfc26e.diff)

[Previous saved controller snapshot](evidence/versions/C084_5a4bc81_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C078](#C078), [C080](#C080), [C083](#C083). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9497113..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -111,7 +111,7 @@ class GeneratedApproach:
  111    111          if self.mode == "choose":
  112    112              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  113    113              boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
  114        -            if (abs(ae) > 0.12 or branch_mismatch) and not boundary_recover and not self.force_move:
         114 +            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover and not self.force_move:
  115    115                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  116    116                  self.mode = "rot_far"
  117    117                  side = -self.turn_sign
```

</details>

<a id="C086"></a>
### C086 · Keep nontrivial obstacle routes during final approach

Commit `389102449ee3ebe52abbd04c8d0f81f4307461c2`; parents: 6bfc26e0f56d461a6afe0148b2286916e6eb2559. Recorded author date: 2026-09-09T09:33:00+02:00.

File roles (automatic): policy.

- [E0539](01_timeline.md#E0539): commit hash in recorded output.
[Controller after this commit](evidence/versions/C086_3891024_approach.py) · [Exact all-file diff](evidence/diffs/C086_3891024.diff)

[Previous saved controller snapshot](evidence/versions/C085_6bfc26e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b72fad0..e5c2404 100644
--- a/approach.py
+++ b/approach.py
@@ -147,7 +147,7 @@ class GeneratedApproach:
  147    147                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  148    148                  far0 = np.clip(com0 - self.push_dir*0.76, 0.105, 4.895)
  149    149                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  150        -                if pd < 0.15:
         150 +                if pd < 0.15 and len(self.nav) <= 2:
  151    151                      self.nav = []
  152    152              else:
  153    153                  return np.zeros(2, dtype=float)
```

</details>

<a id="C087"></a>
### C087 · Retain higher-scoring direct final approach

Commit `37b79db24804ffdaba5beab5fb9f81ebd500add7`; parents: 389102449ee3ebe52abbd04c8d0f81f4307461c2. Recorded author date: 2026-09-09T09:33:32+02:00.

File roles (automatic): policy.

- [E0545](01_timeline.md#E0545): commit hash in recorded output.
[Controller after this commit](evidence/versions/C087_37b79db_approach.py) · [Exact all-file diff](evidence/diffs/C087_37b79db.diff)

[Previous saved controller snapshot](evidence/versions/C086_3891024_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C078](#C078), [C080](#C080), [C083](#C083), [C085](#C085). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e5c2404..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -147,7 +147,7 @@ class GeneratedApproach:
  147    147                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  148    148                  far0 = np.clip(com0 - self.push_dir*0.76, 0.105, 4.895)
  149    149                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  150        -                if pd < 0.15 and len(self.nav) <= 2:
         150 +                if pd < 0.15:
  151    151                      self.nav = []
  152    152              else:
  153    153                  return np.zeros(2, dtype=float)
```

</details>

<a id="C088"></a>
### C088 · initial sandbox setup

Commit `97642a09b90c407db509adc6ad7ab6d7e3be486d`; parents: 37b79db24804ffdaba5beab5fb9f81ebd500add7. Recorded author date: 2026-09-09T09:34:26+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C088_97642a0.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 91ef92d..5e77746 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $6.03. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $4.43. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C089"></a>
### C089 · Test direct late-stage rotation setup

Commit `e848b3aeae9df192b4c0e096c3ef9f1f31ef3544`; parents: 97642a09b90c407db509adc6ad7ab6d7e3be486d. Recorded author date: 2026-09-09T09:36:25+02:00.

File roles (automatic): policy.

- [E0569](01_timeline.md#E0569): commit hash in recorded output.
[Controller after this commit](evidence/versions/C089_e848b3a_approach.py) · [Exact all-file diff](evidence/diffs/C089_e848b3a.diff)

[Previous saved controller snapshot](evidence/versions/C087_37b79db_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b72fad0..e48398a 100644
--- a/approach.py
+++ b/approach.py
@@ -139,6 +139,8 @@ class GeneratedApproach:
  139    139                      far_local0 = np.array([side*(width*.5+.34), self.rot_y])
  140    140                  far0 = obj + self._world(far_local0, theta)
  141    141                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
         142 +                if pd < 0.20:
         143 +                    self.nav = []
  142    144              elif pd > 0.018:
  143    145                  self.push_dir = dp / max(pd, 1e-9)
  144    146                  self.mode = "move_far"
```

</details>

<a id="C090"></a>
### C090 · Restore safe planned rotation setup

Commit `498959a5cf61bf0412d8101f89268bc419edad03`; parents: e848b3aeae9df192b4c0e096c3ef9f1f31ef3544. Recorded author date: 2026-09-09T09:36:58+02:00.

File roles (automatic): policy.

- [E0575](01_timeline.md#E0575): commit hash in recorded output.
[Controller after this commit](evidence/versions/C090_498959a_approach.py) · [Exact all-file diff](evidence/diffs/C090_498959a.diff)

[Previous saved controller snapshot](evidence/versions/C089_e848b3a_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C078](#C078), [C080](#C080), [C083](#C083), [C085](#C085), [C087](#C087). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e48398a..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -139,8 +139,6 @@ class GeneratedApproach:
  139    139                      far_local0 = np.array([side*(width*.5+.34), self.rot_y])
  140    140                  far0 = obj + self._world(far_local0, theta)
  141    141                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  142        -                if pd < 0.20:
  143        -                    self.nav = []
  144    142              elif pd > 0.018:
  145    143                  self.push_dir = dp / max(pd, 1e-9)
  146    144                  self.mode = "move_far"
```

</details>

<a id="C091"></a>
### C091 · initial sandbox setup

Commit `6732cff03f01cca1077cea7a4433c71406c4c633`; parents: 498959a5cf61bf0412d8101f89268bc419edad03. Recorded author date: 2026-09-09T09:37:50+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C091_6732cff.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 5e77746..4ecc59a 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $4.43. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $3.34. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C092"></a>
### C092 · initial sandbox setup

Commit `e206af941b25c1ab1530cc71e9a3f68255482c96`; parents: 6732cff03f01cca1077cea7a4433c71406c4c633. Recorded author date: 2026-09-09T09:39:05+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C092_e206af9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 4ecc59a..cad61f3 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $3.34. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $2.93. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C093"></a>
### C093 · Test faster long-distance translation strokes

Commit `d99bdea0d3f5d0b082e4cbdef2476a9d52862262`; parents: e206af941b25c1ab1530cc71e9a3f68255482c96. Recorded author date: 2026-09-09T09:39:59+02:00.

File roles (automatic): policy.

- [E0607](01_timeline.md#E0607): commit hash in recorded output.
[Controller after this commit](evidence/versions/C093_d99bdea_approach.py) · [Exact all-file diff](evidence/diffs/C093_d99bdea.diff)

[Previous saved controller snapshot](evidence/versions/C090_498959a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b72fad0..2b2f35e 100644
--- a/approach.py
+++ b/approach.py
@@ -258,7 +258,7 @@ class GeneratedApproach:
  258    258                  self.mode = "move_retreat"
  259    259                  self.retreat_count = 0
  260    260                  return self._safe(-self.push_dir, 0.018)
  261        -            speed = 0.016 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
         261 +            speed = 0.016 if pd < 0.12 else (0.038 if pd > 0.55 else 0.024)
  262    262              return self._safe((com + self.push_dir * 0.20) - robot, speed)
  263    263          # Break contact along the exact reverse push direction. Recomputing a
  264    264          # COM-relative far point after the T rotates can route through the T.
```

</details>

<a id="C094"></a>
### C094 · Restore stable long-distance translation speed

Commit `90333d013b517d768f8ca1cc70adc67b640397b8`; parents: d99bdea0d3f5d0b082e4cbdef2476a9d52862262. Recorded author date: 2026-09-09T09:40:50+02:00.

File roles (automatic): policy.

- [E0615](01_timeline.md#E0615): commit hash in recorded output.
[Controller after this commit](evidence/versions/C094_90333d0_approach.py) · [Exact all-file diff](evidence/diffs/C094_90333d0.diff)

[Previous saved controller snapshot](evidence/versions/C093_d99bdea_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C078](#C078), [C080](#C080), [C083](#C083), [C085](#C085), [C087](#C087), [C090](#C090). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2b2f35e..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -258,7 +258,7 @@ class GeneratedApproach:
  258    258                  self.mode = "move_retreat"
  259    259                  self.retreat_count = 0
  260    260                  return self._safe(-self.push_dir, 0.018)
  261        -            speed = 0.016 if pd < 0.12 else (0.038 if pd > 0.55 else 0.024)
         261 +            speed = 0.016 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
  262    262              return self._safe((com + self.push_dir * 0.20) - robot, speed)
  263    263          # Break contact along the exact reverse push direction. Recomputing a
  264    264          # COM-relative far point after the T rotates can route through the T.
```

</details>

<a id="C095"></a>
### C095 · initial sandbox setup

Commit `548345d5bd1f80739a3f6b22f28b7fce940c6571`; parents: 90333d013b517d768f8ca1cc70adc67b640397b8. Recorded author date: 2026-09-09T09:41:26+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C095_548345d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index cad61f3..9452637 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $2.93. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $2.18. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C096"></a>
### C096 · initial sandbox setup

Commit `f6c33d6681a8c5ca9f490fd46e4d41490d245705`; parents: 548345d5bd1f80739a3f6b22f28b7fce940c6571. Recorded author date: 2026-09-09T09:42:52+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C096_f6c33d6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 9452637..2403dee 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $2.18. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.87. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C097"></a>
### C097 · initial sandbox setup

Commit `3414e2337e9fad27b4553c398fab99fe3db6faa0`; parents: f6c33d6681a8c5ca9f490fd46e4d41490d245705. Recorded author date: 2026-09-09T09:44:24+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C097_3414e23.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 2403dee..8c751dc 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.87. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.70. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C098"></a>
### C098 · Try slightly earlier direct final approach

Commit `a54cb35202a19b7687c4c62d6ea267338e454311`; parents: 3414e2337e9fad27b4553c398fab99fe3db6faa0. Recorded author date: 2026-09-09T09:44:56+02:00.

File roles (automatic): policy.

- [E0663](01_timeline.md#E0663): commit hash in recorded output.
[Controller after this commit](evidence/versions/C098_a54cb35_approach.py) · [Exact all-file diff](evidence/diffs/C098_a54cb35.diff)

[Previous saved controller snapshot](evidence/versions/C094_90333d0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b72fad0..0ec8578 100644
--- a/approach.py
+++ b/approach.py
@@ -147,7 +147,7 @@ class GeneratedApproach:
  147    147                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  148    148                  far0 = np.clip(com0 - self.push_dir*0.76, 0.105, 4.895)
  149    149                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  150        -                if pd < 0.15:
         150 +                if pd < 0.18:
  151    151                      self.nav = []
  152    152              else:
  153    153                  return np.zeros(2, dtype=float)
```

</details>

<a id="C099"></a>
### C099 · Restore validated direct approach cutoff

Commit `27c77f7441b23c8aed60f52f35aabf0b9c5b5e52`; parents: a54cb35202a19b7687c4c62d6ea267338e454311. Recorded author date: 2026-09-09T09:45:15+02:00.

File roles (automatic): policy.

- [E0670](01_timeline.md#E0670): commit hash in recorded output.
[Controller after this commit](evidence/versions/C099_27c77f7_approach.py) · [Exact all-file diff](evidence/diffs/C099_27c77f7.diff)

[Previous saved controller snapshot](evidence/versions/C098_a54cb35_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C078](#C078), [C080](#C080), [C083](#C083), [C085](#C085), [C087](#C087), [C090](#C090), [C094](#C094). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0ec8578..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -147,7 +147,7 @@ class GeneratedApproach:
  147    147                  com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
  148    148                  far0 = np.clip(com0 - self.push_dir*0.76, 0.105, 4.895)
  149    149                  self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
  150        -                if pd < 0.18:
         150 +                if pd < 0.15:
  151    151                      self.nav = []
  152    152              else:
  153    153                  return np.zeros(2, dtype=float)
```

</details>

<a id="C100"></a>
### C100 · initial sandbox setup

Commit `b1237798fdff6bc525235402407f1978b14e67c7`; parents: 27c77f7441b23c8aed60f52f35aabf0b9c5b5e52. Recorded author date: 2026-09-09T09:45:21+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C100_b123779.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 8c751dc..fa5db8f 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.70. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.57. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C101"></a>
### C101 · Avoid marginal rotation cycles near episode horizon

Commit `8d393fab872a58905d18f6be091023eb043d0e9b`; parents: b1237798fdff6bc525235402407f1978b14e67c7. Recorded author date: 2026-09-09T09:46:33+02:00.

File roles (automatic): policy.

- [E0687](01_timeline.md#E0687): commit hash in recorded output.
[Controller after this commit](evidence/versions/C101_8d393fa_approach.py) · [Exact all-file diff](evidence/diffs/C101_8d393fa.diff)

[Previous saved controller snapshot](evidence/versions/C099_27c77f7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b72fad0..9c77e58 100644
--- a/approach.py
+++ b/approach.py
@@ -24,6 +24,7 @@ class GeneratedApproach:
   24     24          self.force_move = False
   25     25          self.start_pd = 0.0
   26     26          self.retreat_count = 0
          27 +        self.steps = 0
   27     28  
   28     29      @staticmethod
   29     30      def _angle(x):
@@ -100,6 +101,7 @@ class GeneratedApproach:
  100    101          return compact
  101    102  
  102    103      def get_action(self, state):
         104 +        self.steps += 1
  103    105          s = np.asarray(state, dtype=float)
  104    106          obj, robot, goal = s[0:2], s[16:18], s[29:31]
  105    107          theta, goal_theta = float(s[2]), float(s[31])
@@ -111,7 +113,8 @@ class GeneratedApproach:
  111    113          if self.mode == "choose":
  112    114              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  113    115              boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
  114        -            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover and not self.force_move:
         116 +            turn_threshold = 0.135 if self.steps > 850 else 0.11
         117 +            if (abs(ae) > turn_threshold or branch_mismatch) and not boundary_recover and not self.force_move:
  115    118                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  116    119                  self.mode = "rot_far"
  117    120                  side = -self.turn_sign
```

</details>

<a id="C102"></a>
### C102 · Restore strict rotation threshold after horizon test

Commit `636532f067ca4e498ff0270c6264adf0da2ebc56`; parents: 8d393fab872a58905d18f6be091023eb043d0e9b. Recorded author date: 2026-09-09T09:46:57+02:00.

File roles (automatic): policy.

- [E0694](01_timeline.md#E0694): commit hash in recorded output.
[Controller after this commit](evidence/versions/C102_636532f_approach.py) · [Exact all-file diff](evidence/diffs/C102_636532f.diff)

[Previous saved controller snapshot](evidence/versions/C101_8d393fa_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C078](#C078), [C080](#C080), [C083](#C083), [C085](#C085), [C087](#C087), [C090](#C090), [C094](#C094), [C099](#C099). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9c77e58..b72fad0 100644
--- a/approach.py
+++ b/approach.py
@@ -24,7 +24,6 @@ class GeneratedApproach:
   24     24          self.force_move = False
   25     25          self.start_pd = 0.0
   26     26          self.retreat_count = 0
   27        -        self.steps = 0
   28     27  
   29     28      @staticmethod
   30     29      def _angle(x):
@@ -101,7 +100,6 @@ class GeneratedApproach:
  101    100          return compact
  102    101  
  103    102      def get_action(self, state):
  104        -        self.steps += 1
  105    103          s = np.asarray(state, dtype=float)
  106    104          obj, robot, goal = s[0:2], s[16:18], s[29:31]
  107    105          theta, goal_theta = float(s[2]), float(s[31])
@@ -113,8 +111,7 @@ class GeneratedApproach:
  113    111          if self.mode == "choose":
  114    112              branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
  115    113              boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
  116        -            turn_threshold = 0.135 if self.steps > 850 else 0.11
  117        -            if (abs(ae) > turn_threshold or branch_mismatch) and not boundary_recover and not self.force_move:
         114 +            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover and not self.force_move:
  118    115                  self.turn_sign = 1.0 if ae > 0.0 else -1.0
  119    116                  self.mode = "rot_far"
  120    117                  side = -self.turn_sign
```

</details>

<a id="C103"></a>
### C103 · initial sandbox setup

Commit `98f39c080cf09842957cadb474478c1c6484399d`; parents: 636532f067ca4e498ff0270c6264adf0da2ebc56. Recorded author date: 2026-09-09T09:47:03+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C103_98f39c0.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index fa5db8f..c4404f4 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.57. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.36. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C104"></a>
### C104 · initial sandbox setup

Commit `2e6c1435aea66c93b69acebf9287d8b6fdc3316d`; parents: 98f39c080cf09842957cadb474478c1c6484399d. Recorded author date: 2026-09-09T09:48:06+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C104_2e6c143.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index c4404f4..97c4394 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.36. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.24. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C105"></a>
### C105 · initial sandbox setup

Commit `93c667493203a26bb0a71cc75f227e20505cc265`; parents: 2e6c1435aea66c93b69acebf9287d8b6fdc3316d. Recorded author date: 2026-09-09T09:49:01+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C105_93c6674.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 97c4394..834c771 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.24. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.10. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C106"></a>
### C106 · initial sandbox setup

Commit `dbadd615237b51fdda645851287f467f79912b1e`; parents: 93c667493203a26bb0a71cc75f227e20505cc265. Recorded author date: 2026-09-09T09:49:35+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C106_dbadd61.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 834c771..0a1c19c 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.10. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.03. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C107"></a>
### C107 · initial sandbox setup

Commit `9d5823d4676feb0893a726a3323b452e6247c8b6`; parents: dbadd615237b51fdda645851287f467f79912b1e. Recorded author date: 2026-09-09T09:50:12+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C107_9d5823d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 0a1c19c..770d0ca 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.03. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.95. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C108"></a>
### C108 · initial sandbox setup

Commit `0f71f90121f2d57194000494ba69236aa7768777`; parents: 9d5823d4676feb0893a726a3323b452e6247c8b6. Recorded author date: 2026-09-09T09:50:53+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C108_0f71f90.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 770d0ca..4b90f24 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.95. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.83. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C109"></a>
### C109 · initial sandbox setup

Commit `e2c17471031a6b8cbc2622843797ebc16a185cfa`; parents: 0f71f90121f2d57194000494ba69236aa7768777. Recorded author date: 2026-09-09T09:51:26+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C109_e2c1747.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 4b90f24..3fbdced 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.83. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.75. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C110"></a>
### C110 · initial sandbox setup

Commit `362deb8cdce6f9c1fab43a01cf91aff2eabc6d40`; parents: e2c17471031a6b8cbc2622843797ebc16a185cfa. Recorded author date: 2026-09-09T09:51:54+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C110_362deb8.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 3fbdced..8c91e22 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.75. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.66. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C111"></a>
### C111 · initial sandbox setup

Commit `47dea9d34800e0ab5751c3e0a5b8bf2438d4d7ea`; parents: 362deb8cdce6f9c1fab43a01cf91aff2eabc6d40. Recorded author date: 2026-09-09T09:52:24+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C111_47dea9d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 8c91e22..612e57e 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.66. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.58. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

