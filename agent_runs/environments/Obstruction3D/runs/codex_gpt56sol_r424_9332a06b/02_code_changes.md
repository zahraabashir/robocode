# Obstruction3D · gpt-5.6-sol · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `18c2edd` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `ebd3a35` | Add valid variable-state policy scaffold | approach.py, probe_dynamics_agent.py, probe_geometry_states.out, probe_geometry_states.py | [E0015](01_timeline.md#E0015) |
| [C003](#C003) · `c6dd787` | Aim mobile base laterally at target and probe grasp | approach.py, probe_geometry_states.out, probe_geometry_summary.py | [E0023](01_timeline.md#E0023) |
| [C004](#C004) · `a375a2d` | Add calibrated planar reach probe for target grasp | approach.py, probe_geometry_clearance.py, probe_geometry_heights.py, probe_grasp_agent.py | [E0039](01_timeline.md#E0039) |
| [C005](#C005) · `62c46a7` | Probe extended high arm configuration | approach.py, probe_random_grasp_agent.py | [E0050](01_timeline.md#E0050) |
| [C006](#C006) · `1a6664c` | Add feedback Cartesian pick-and-place controller | approach.py, scan_grasp.py, scan_low.py, test_pick_formula.py | [E0078](01_timeline.md#E0078) |
| [C007](#C007) · `6749ed7` | Add end-to-end policy test harness | test_approach.py | [E0082](01_timeline.md#E0082) |
| [C008](#C008) · `82abb4c` | Use calibrated grasp pose for precise final descent | approach.py | [E0086](01_timeline.md#E0086) |
| [C009](#C009) · `550e473` | Lower held block onto region before opening gripper | approach.py, probe_held_jacobian.py | [E0098](01_timeline.md#E0098) |
| [C010](#C010) · `eb9b61a` | Open and retract gripper to complete release | approach.py | [E0112](01_timeline.md#E0112) |
| [C011](#C011) · `4bd8c34` | Drop from aligned clearance height to avoid gripper wedging | approach.py | [E0118](01_timeline.md#E0118) |
| [C012](#C012) · `8a08dc8` | Preserve grasp orientation during Cartesian feedback | approach.py | [E0128](01_timeline.md#E0128) |
| [C013](#C013) · `fbe1b5d` | Fix virtual-control calibration dimension | approach.py | [E0132](01_timeline.md#E0132) |
| [C014](#C014) · `a53d8a0` | Add orientation feedback to Cartesian transport | approach.py | [E0136](01_timeline.md#E0136) |
| [C015](#C015) · `ebc80c8` | Use backward mobile-base motion in Cartesian transport | approach.py | [E0140](01_timeline.md#E0140) |
| [C016](#C016) · `a514ca1` | Handle release before waypoint indexing | approach.py | [E0144](01_timeline.md#E0144) |
| [C017](#C017) · `450886c` | Bring block into support contact before release | approach.py | [E0148](01_timeline.md#E0148) |
| [C018](#C018) · `053d040` | Push gently into support while opening gripper | approach.py | [E0152](01_timeline.md#E0152) |
| [C019](#C019) · `4353e5d` | Align above region before contact push | approach.py | [E0156](01_timeline.md#E0156) |
| [C020](#C020) · `ed4f6af` | Clear overlapping obstructions before placing target | approach.py, test_many.py | [E0170](01_timeline.md#E0170) |
| [C021](#C021) · `9fb91c9` | Add folded-arm grasp family for small obstructions | approach.py, scan_obstacle.py | [E0178](01_timeline.md#E0178) |
| [C022](#C022) · `e4f189b` | Broaden close-range pickup search | approach.py | [E0184](01_timeline.md#E0184) |
| [C023](#C023) · `5a4aa86` | Clear taller accessible obstructions first | approach.py | [E0188](01_timeline.md#E0188) |
| [C024](#C024) · `34b761a` | Reject accidental grasps of non-target objects | approach.py | [E0192](01_timeline.md#E0192) |
| [C025](#C025) · `8461ed9` | Sustain release push until support contact | approach.py | [E0198](01_timeline.md#E0198) |
| [C026](#C026) · `65422b5` | Prefer a higher target grasp to preserve finger clearance | approach.py | [E0208](01_timeline.md#E0208) |
| [C027](#C027) · `9cdd288` | Orient fingers along narrow target-region axis | approach.py | [E0216](01_timeline.md#E0216) |
| [C028](#C028) · `a2ea09b` | Restore reliable target grasp orientation | approach.py | [E0220](01_timeline.md#E0220) |
| [C029](#C029) · `c4098f6` | Reserve forward base travel for distant placements | approach.py | [E0226](01_timeline.md#E0226) |
| [C030](#C030) · `9789cc6` | Use rotated long-settle grasp for wide target regions | approach.py, scan_rotated_pick.py | [E0236](01_timeline.md#E0236) |
| [C031](#C031) · `2039c44` | Keep obstruction pickup search within episode budget | approach.py | [E0240](01_timeline.md#E0240) |
| [C032](#C032) · `9d7f832` | Favor reliable upright pickup over wedging-prone rotated grasp | approach.py | [E0244](01_timeline.md#E0244) |
| [C033](#C033) · `5a9a4bf` | Close only after converging to each pickup pose | approach.py | [E0250](01_timeline.md#E0250) |
| [C034](#C034) · `b8d29f9` | Restore base position before standard pickup | approach.py | [E0254](01_timeline.md#E0254) |
| [C035](#C035) · `f888c69` | Retract arm between object transfers | approach.py | [E0260](01_timeline.md#E0260) |
| [C036](#C036) · `2ec4ab1` | Relax off-region obstruction drop positioning | approach.py | [E0268](01_timeline.md#E0268) |
| [C037](#C037) · `3bd39dd` | Use target block as raised obstruction staging surface | approach.py | [E0272](01_timeline.md#E0272) |
| [C038](#C038) · `27238e8` | Restore edge staging for cleared obstructions | approach.py | [E0276](01_timeline.md#E0276) |
| [C039](#C039) · `3d29556` | Lift opening fingers to release without surface wedging | approach.py | [E0284](01_timeline.md#E0284) |
| [C040](#C040) · `d717a30` | Fall back to timed closure at contact-limited pickup poses | approach.py | [E0288](01_timeline.md#E0288) |
| [C041](#C041) · `d3f57a9` | Seat obstructions while lifting target-release fingers | approach.py | [E0292](01_timeline.md#E0292) |
| [C042](#C042) · `4ba933a` | Require precise supported obstruction placement before opening | approach.py | [E0296](01_timeline.md#E0296) |
| [C043](#C043) · `eeeee4e` | Use stable supported release for every object | approach.py | [E0300](01_timeline.md#E0300) |
| [C044](#C044) · `cc5d12e` | Clarify supported-release controller intent | approach.py | [E0307](01_timeline.md#E0307) |
| [C045](#C045) · `0d781c9` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C046](#C046) · `555ce10` | Relax orientation during high-clearance transport | approach.py, release_probe_agent.py | [E0324](01_timeline.md#E0324) |
| [C047](#C047) · `d6eb33d` | Lower transfer clearance to expand forward workspace | approach.py | [E0328](01_timeline.md#E0328) |
| [C048](#C048) · `edbafe9` | Recover from missed releases and dropped objects | approach.py | [E0332](01_timeline.md#E0332) |
| [C049](#C049) · `d2d86c6` | Probe open-only final target release | release_probe_openonly.py | No matched commit command/output |
| [C050](#C050) · `eba01de` | Advance pickup search once per accidental grasp | approach.py | [E0336](01_timeline.md#E0336) |
| [C051](#C051) · `a3db0e0` | Open target gripper without post-seat motion | approach.py | [E0342](01_timeline.md#E0342) |
| [C052](#C052) · `c3d9c67` | Discard obstructions beyond table edge for reliable release | approach.py | [E0358](01_timeline.md#E0358) |
| [C053](#C053) · `5601899` | Remove harmful reserve move and restore supported blocker staging | approach.py | [E0362](01_timeline.md#E0362) |
| [C054](#C054) · `d2a7e27` | Pre-retract base for long forward target transfers | approach.py | [E0366](01_timeline.md#E0366) |
| [C055](#C055) · `d982ec7` | Require firmer target support before opening | approach.py | [E0372](01_timeline.md#E0372) |
| [C056](#C056) · `0340a29` | Retry blocked target opening with delayed support push | approach.py | [E0376](01_timeline.md#E0376) |
| [C057](#C057) · `b6a1b28` | Lift jammed target gripper while preserving placement XY | approach.py | [E0380](01_timeline.md#E0380) |
| [C058](#C058) · `838fa46` | Add seed one jammed-release diagnostics | release_probe_seed1.py | No matched commit command/output |
| [C059](#C059) · `b2df7a7` | Avoid non-releasable centered grasp on long-forward transfers | approach.py | [E0398](01_timeline.md#E0398) |
| [C060](#C060) · `8a952ca` | Keep final target stationary while opening | approach.py, probe_forward_grasps.py | [E0410](01_timeline.md#E0410) |
| [C061](#C061) · `ccf2a77` | Add reliable far-obstruction grasp postures | approach.py, scan_far_obstacle.py | [E0425](01_timeline.md#E0425) |
| [C062](#C062) · `0b6c2ee` | Improve policy trajectory diagnostics | test_approach.py | [E0443](01_timeline.md#E0443) |
| [C063](#C063) · `6d12d39` | Keep obstruction drops within reachable edge workspace | approach.py | [E0447](01_timeline.md#E0447) |
| [C064](#C064) · `e7485e1` | Log gripper clearance in trajectory tests | test_approach.py | [E0455](01_timeline.md#E0455) |
| [C065](#C065) · `7d82379` | Release obstructions without clamping against table | approach.py | [E0460](01_timeline.md#E0460) |
| [C066](#C066) · `e8d5bde` | Parameterize far-obstruction grasp scan | scan_far_obstacle.py | [E0470](01_timeline.md#E0470) |
| [C067](#C067) · `0b2615c` | Release discarded obstructions above finger collision height | approach.py | [E0477](01_timeline.md#E0477) |
| [C068](#C068) · `a2d14ec` | Prefer releasable centered grasps at medium reach | approach.py | [E0481](01_timeline.md#E0481) |
| [C069](#C069) · `39f586e` | Use shallow medium-range obstruction grasp | approach.py | [E0485](01_timeline.md#E0485) |
| [C070](#C070) · `6d9f07a` | Probe rotated obstruction grasp alternatives | scan_rotated_pick.py | [E0494](01_timeline.md#E0494) |
| [C071](#C071) · `4a9f065` | Narrow rotated grasp probe to observed pickup pose | scan_rotated_pick.py | [E0495](01_timeline.md#E0495) |
| [C072](#C072) · `7b43eee` | Rotate medium obstruction grasps across narrow face | approach.py | [E0500](01_timeline.md#E0500) |
| [C073](#C073) · `ba027a9` | Keep obstruction releases clear of table boundary | approach.py | [E0504](01_timeline.md#E0504) |
| [C074](#C074) · `8a838b0` | Try folded grasps first for troublesome medium obstructions | approach.py | [E0510](01_timeline.md#E0510) |
| [C075](#C075) · `4a5cb77` | Restore best validated release and grasp policy | approach.py | [E0518](01_timeline.md#E0518) |
| [C076](#C076) · `e5c379b` | Parameterize variable-count policy regression test | test_many.py | [E0529](01_timeline.md#E0529) |
| [C077](#C077) · `956a7b2` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C078](#C078) · `8c5f400` | Report exact variable-count failure task | test_many.py | [E0549](01_timeline.md#E0549) |
| [C079](#C079) · `f675793` | Extend dense grasp search to medium obstructions | approach.py | [E0554](01_timeline.md#E0554) |
| [C080](#C080) · `07955a9` | Trace grasp candidates in variable-count tests | test_many.py | [E0560](01_timeline.md#E0560) |
| [C081](#C081) · `11efccb` | Compress alternating obstruction staging positions | approach.py | [E0565](01_timeline.md#E0565) |
| [C082](#C082) · `1e36eb6` | Cap obstruction staging at reachable x | approach.py | [E0569](01_timeline.md#E0569) |
| [C083](#C083) · `fd1d640` | Separate later obstruction drops into inner edge lanes | approach.py | [E0575](01_timeline.md#E0575) |
| [C084](#C084) · `1920e24` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C085](#C085) · `0bfd8c6` | Use extended grasp family for far target blocks | approach.py | [E0596](01_timeline.md#E0596) |
| [C086](#C086) · `8300fa7` | Advance base for extreme far-side pickups | approach.py | [E0600](01_timeline.md#E0600) |
| [C087](#C087) · `dc79774` | Prefer releasable alternate grasp for far targets | approach.py | [E0607](01_timeline.md#E0607) |
| [C088](#C088) · `acc380b` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C089](#C089) · `a80ce48` | Pulse jammed obstruction gripper before reopening | approach.py | [E0625](01_timeline.md#E0625) |
| [C090](#C090) · `eb3e8d4` | Remove ineffective gripper pulse recovery | approach.py | [E0630](01_timeline.md#E0630) |
| [C091](#C091) · `cdccafc` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C092](#C092) · `8b2a688` | Move first obstruction drop into reachable descent band | approach.py | [E0651](01_timeline.md#E0651) |
| [C093](#C093) · `7da7347` | Center first staging goal across mirrored control branch | approach.py | [E0658](01_timeline.md#E0658) |
| [C094](#C094) · `8007f16` | initial sandbox setup | AGENTS.md | No matched commit command/output |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `18c2edd0413dc4d4b642e199c201eb5e55b05a2e`; parents: none (initial snapshot). Recorded author date: 2026-09-09T15:17:17+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_18c2edd.diff)

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
index 0000000..76dfa5b
--- /dev/null
+++ b/AGENTS.md
@@ -0,0 +1,13 @@
           1 +You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
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
index 0000000..e4cb807
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1,129 @@
           1 +{
           2 +  "host": "127.0.0.1",
           3 +  "port": 39323,
           4 +  "token": "0f691b6c59b3a39f498dad5dbdb6aaa7",
           5 +  "observation_space": {
           6 +    "type": "ObjectCentric",
           7 +    "types": [
           8 +      {
           9 +        "name": "Kinematic3DCuboid",
          10 +        "parent": null,
          11 +        "features": [
          12 +          "pose_x",
          13 +          "pose_y",
          14 +          "pose_z",
          15 +          "pose_qx",
          16 +          "pose_qy",
          17 +          "pose_qz",
          18 +          "pose_qw",
          19 +          "grasp_active",
          20 +          "object_type",
          21 +          "half_extent_x",
          22 +          "half_extent_y",
          23 +          "half_extent_z"
          24 +        ]
          25 +      },
          26 +      {
          27 +        "name": "Kinematic3DFixture",
          28 +        "parent": null,
          29 +        "features": [
          30 +          "pose_x",
          31 +          "pose_y",
          32 +          "pose_z",
          33 +          "pose_qx",
          34 +          "pose_qy",
          35 +          "pose_qz",
          36 +          "pose_qw"
          37 +        ]
          38 +      },
          39 +      {
          40 +        "name": "Kinematic3DPoint",
          41 +        "parent": null,
          42 +        "features": [
          43 +          "x",
          44 +          "y",
          45 +          "z"
          46 +        ]
          47 +      },
          48 +      {
          49 +        "name": "Kinematic3DRobot",
          50 +        "parent": null,
          51 +        "features": [
          52 +          "pos_base_x",
          53 +          "pos_base_y",
          54 +          "pos_base_rot",
          55 +          "joint_1",
          56 +          "joint_2",
          57 +          "joint_3",
          58 +          "joint_4",
          59 +          "joint_5",
          60 +          "joint_6",
          61 +          "joint_7",
          62 +          "finger_state",
          63 +          "grasp_active",
          64 +          "grasp_tf_x",
          65 +          "grasp_tf_y",
          66 +          "grasp_tf_z",
          67 +          "grasp_tf_qx",
          68 +          "grasp_tf_qy",
          69 +          "grasp_tf_qz",
          70 +          "grasp_tf_qw"
          71 +        ]
          72 +      },
          73 +      {
          74 +        "name": "Kinematic3DTriangle",
          75 +        "parent": null,
          76 +        "features": [
          77 +          "pose_x",
          78 +          "pose_y",
          79 +          "pose_z",
          80 +          "pose_qx",
          81 +          "pose_qy",
          82 +          "pose_qz",
          83 +          "pose_qw",
          84 +          "grasp_active",
          85 +          "triangle_type",
          86 +          "side_a",
          87 +          "side_b",
          88 +          "depth"
          89 +        ]
          90 +      }
          91 +    ]
          92 +  },
          93 +  "action_space": {
          94 +    "type": "Box",
          95 +    "shape": [
          96 +      11
          97 +    ],
          98 +    "low": [
          99 +      -0.20000000298023224,
         100 +      -0.20000000298023224,
         101 +      -0.20000000298023224,
         102 +      -0.20000000298023224,
         103 +      -0.20000000298023224,
         104 +      -0.20000000298023224,
         105 +      -0.20000000298023224,
         106 +      -0.20000000298023224,
         107 +      -0.20000000298023224,
         108 +      -0.20000000298023224,
         109 +      -1.0
         110 +    ],
         111 +    "high": [
         112 +      0.20000000298023224,
         113 +      0.20000000298023224,
         114 +      0.20000000298023224,
         115 +      0.20000000298023224,
         116 +      0.20000000298023224,
         117 +      0.20000000298023224,
         118 +      0.20000000298023224,
         119 +      0.20000000298023224,
         120 +      0.20000000298023224,
         121 +      0.20000000298023224,
         122 +      1.0
         123 +    ],
         124 +    "dtype": "float32"
         125 +  },
         126 +  "max_steps": 1000,
         127 +  "primitives": [],
         128 +  "strict": true
         129 +}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Add valid variable-state policy scaffold

Commit `ebd3a35c1fa70994658921ff3f3235bed29d38c2`; parents: 18c2edd0413dc4d4b642e199c201eb5e55b05a2e. Recorded author date: 2026-09-09T15:18:33+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0015](01_timeline.md#E0015): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_ebd3a35_approach.py) · [Exact all-file diff](evidence/diffs/C002_ebd3a35.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..a6a5e08
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,18 @@
           1 +"""Reactive policy for the variable-count Obstruction3D task."""
           2 +
           3 +import numpy as np
           4 +
           5 +
           6 +class GeneratedApproach:
           7 +    def __init__(self, action_space, observation_space, primitives):
           8 +        self.action_space = action_space
           9 +        self.observation_space = observation_space
          10 +        self.t = 0
          11 +
          12 +    def reset(self, state, info):
          13 +        self.t = 0
          14 +
          15 +    def get_action(self, state):
          16 +        self.t += 1
          17 +        # Safe valid placeholder while the manipulation controller is calibrated.
          18 +        return np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
diff --git a/probe_dynamics_agent.py b/probe_dynamics_agent.py
new file mode 100644
index 0000000..2aee73a
--- /dev/null
+++ b/probe_dynamics_agent.py
@@ -0,0 +1,45 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +
           4 +
           5 +def vals(s, name):
           6 +    o = s.get_object_from_name(name)
           7 +    out = {}
           8 +    for f in [
           9 +        "pos_base_x", "pos_base_y", "pos_base_rot",
          10 +        "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7",
          11 +        "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z",
          12 +        "pose_x", "pose_y", "pose_z", "grasp_active", "half_extent_x", "half_extent_y", "half_extent_z",
          13 +    ]:
          14 +        try:
          15 +            out[f] = float(s.get(o, f))
          16 +        except Exception:
          17 +            pass
          18 +    return out
          19 +
          20 +
          21 +def diff(a, b):
          22 +    return {k: round(b[k] - v, 6) for k, v in a.items() if k in b and abs(b[k] - v) > 1e-8}
          23 +
          24 +
          25 +env = make_env()
          26 +print("spaces", env.action_space.shape, env.action_space.low, env.action_space.high, "max", env.max_steps)
          27 +for seed in [0, 1, 2]:
          28 +    s, info = env.reset(seed=seed)
          29 +    print("RESET", seed, s.get_object_names(), info)
          30 +    for n in s.get_object_names():
          31 +        print(n, vals(s, n))
          32 +env.close()
          33 +
          34 +for idx in range(11):
          35 +    for mag in [-1.0, 1.0]:
          36 +        env = make_env()
          37 +        s, _ = env.reset(seed=0)
          38 +        before = {n: vals(s, n) for n in s.get_object_names()}
          39 +        a = np.zeros(11, dtype=np.float32); a[idx] = mag
          40 +        s, r, term, trunc, info = env.step(a)
          41 +        after = {n: vals(s, n) for n in s.get_object_names()}
          42 +        print("ACT", idx, mag, "rtt", r, term, trunc, "robot", diff(before["robot"], after["robot"]))
          43 +        moved = {n: diff(before[n], after[n]) for n in before if n != "robot"}
          44 +        print(" moved", {k:v for k,v in moved.items() if v})
          45 +        env.close()
diff --git a/probe_geometry_states.out b/probe_geometry_states.out
new file mode 100644
index 0000000..e69de29
diff --git a/probe_geometry_states.py b/probe_geometry_states.py
new file mode 100644
index 0000000..14a964d
--- /dev/null
+++ b/probe_geometry_states.py
@@ -0,0 +1,27 @@
           1 +from env_client import make_env
           2 +
           3 +
           4 +def dump(seed, object_count=None):
           5 +    env = make_env()
           6 +    kwargs = {"seed": seed}
           7 +    if object_count is not None:
           8 +        # reset may or may not expose this option; keep ordinary seeded resets primary.
           9 +        kwargs["options"] = {"object_count": object_count}
          10 +    try:
          11 +        state, info = env.reset(**kwargs)
          12 +        print("SEED", seed, "COUNT_ARG", object_count, "MAX", env.max_steps,
          13 +              "ASHAPE", env.action_space.shape,
          14 +              "LOW", env.action_space.low.tolist(), "HIGH", env.action_space.high.tolist(),
          15 +              "INFO", info)
          16 +        for name in state.get_object_names():
          17 +            obj = state.get_object_from_name(name)
          18 +            feats = env.observation_space.type_features[obj.type]
          19 +            vals = {f: float(state.get(obj, f)) for f in feats}
          20 +            print(name, obj.type.name, vals)
          21 +    finally:
          22 +        env.close()
          23 +
          24 +
          25 +if __name__ == "__main__":
          26 +    for s in range(12):
          27 +        dump(s)
```

</details>

<a id="C003"></a>
### C003 · Aim mobile base laterally at target and probe grasp

Commit `c6dd7870bf44af9d7a0280926d8552e48ddfed5f`; parents: ebd3a35c1fa70994658921ff3f3235bed29d38c2. Recorded author date: 2026-09-09T15:19:56+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0023](01_timeline.md#E0023): commit hash in recorded output.
[Controller after this commit](evidence/versions/C003_c6dd787_approach.py) · [Exact all-file diff](evidence/diffs/C003_c6dd787.diff)

[Previous saved controller snapshot](evidence/versions/C002_ebd3a35_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a6a5e08..94a75b2 100644
--- a/approach.py
+++ b/approach.py
@@ -11,8 +11,17 @@ class GeneratedApproach:
   11     11  
   12     12      def reset(self, state, info):
   13     13          self.t = 0
          14 +        self.target_y = self._v(state, "target_block", "pose_y")
          15 +
          16 +    @staticmethod
          17 +    def _v(state, name, feature):
          18 +        return state.get(state.get_object_from_name(name), feature)
   14     19  
   15     20      def get_action(self, state):
   16     21          self.t += 1
   17        -        # Safe valid placeholder while the manipulation controller is calibrated.
   18        -        return np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
          22 +        a = np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
          23 +        robot_y = self._v(state, "robot", "pos_base_y")
          24 +        a[1] = np.clip(self.target_y - robot_y, -0.2, 0.2)
          25 +        if self.t >= 3:
          26 +            a[10] = -1.0
          27 +        return a
diff --git a/probe_geometry_states.out b/probe_geometry_states.out
index e69de29..e6aef9e 100644
--- a/probe_geometry_states.out
+++ b/probe_geometry_states.out
@@ -0,0 +1,67 @@
           1 +SEED 0 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 2}
           2 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
           3 +target_region Kinematic3DCuboid {'pose_x': 0.14442715048789978, 'pose_y': 0.23301441967487335, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.03910885006189346, 'half_extent_y': 0.028093600645661354, 'half_extent_z': 0.004999999888241291}
           4 +obstruction1 Kinematic3DCuboid {'pose_x': 0.10313927382230759, 'pose_y': 0.20900817215442657, 'pose_z': 0.10099423676729202, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.018631789833307266, 'half_extent_y': 0.015414612367749214, 'half_extent_z': 0.0159942377358675}
           5 +target_block Kinematic3DCuboid {'pose_x': 0.33598166704177856, 'pose_y': 0.17328143119812012, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.03128708153963089, 'half_extent_y': 0.022474881261587143, 'half_extent_z': 0.02500000037252903}
           6 +obstruction0 Kinematic3DCuboid {'pose_x': 0.1034325584769249, 'pose_y': 0.24800321459770203, 'pose_z': 0.09505476802587509, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.019350724294781685, 'half_extent_y': 0.01815853640437126, 'half_extent_z': 0.010054769925773144}
           7 +SEED 1 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 1}
           8 +target_block Kinematic3DCuboid {'pose_x': 0.13774842023849487, 'pose_y': 0.18313223123550415, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.02828371897339821, 'half_extent_y': 0.038811128586530685, 'half_extent_z': 0.02500000037252903}
           9 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          10 +target_region Kinematic3DCuboid {'pose_x': 0.44773608446121216, 'pose_y': -0.132277250289917, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.035354647785425186, 'half_extent_y': 0.04851391166448593, 'half_extent_z': 0.004999999888241291}
          11 +obstruction0 Kinematic3DCuboid {'pose_x': 0.419426292181015, 'pose_y': -0.14254437386989594, 'pose_z': 0.10106389969587326, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.013297317549586296, 'half_extent_y': 0.017884286120533943, 'half_extent_z': 0.01606389693915844}
          12 +SEED 2 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 2}
          13 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          14 +target_region Kinematic3DCuboid {'pose_x': 0.15949532389640808, 'pose_y': 0.0742836520075798, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.027848364785313606, 'half_extent_y': 0.02895473502576351, 'half_extent_z': 0.004999999888241291}
          15 +obstruction1 Kinematic3DCuboid {'pose_x': 0.14757776260375977, 'pose_y': 0.10241974890232086, 'pose_z': 0.10283249616622925, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.019674358889460564, 'half_extent_y': 0.016830647364258766, 'half_extent_z': 0.017832497134804726}
          16 +target_block Kinematic3DCuboid {'pose_x': 0.18906673789024353, 'pose_y': -0.33527371287345886, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.022278690710663795, 'half_extent_y': 0.02316378802061081, 'half_extent_z': 0.02500000037252903}
          17 +obstruction0 Kinematic3DCuboid {'pose_x': 0.17032761871814728, 'pose_y': 0.06920900195837021, 'pose_z': 0.09800124168395996, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.016574330627918243, 'half_extent_y': 0.015622656792402267, 'half_extent_z': 0.013001245446503162}
          18 +SEED 3 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 2}
          19 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          20 +target_region Kinematic3DCuboid {'pose_x': 0.3291561007499695, 'pose_y': -0.3026953637599945, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.022569475695490837, 'half_extent_y': 0.027104314416646957, 'half_extent_z': 0.004999999888241291}
          21 +obstruction1 Kinematic3DCuboid {'pose_x': 0.3195573091506958, 'pose_y': -0.27949976921081543, 'pose_z': 0.11446920782327652, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.012927207164466381, 'half_extent_y': 0.01001490093767643, 'half_extent_z': 0.0294692050665617}
          22 +target_block Kinematic3DCuboid {'pose_x': 0.15941956639289856, 'pose_y': -0.0823003500699997, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.01805558055639267, 'half_extent_y': 0.021683452650904655, 'half_extent_z': 0.02500000037252903}
          23 +obstruction0 Kinematic3DCuboid {'pose_x': 0.21985502541065216, 'pose_y': 0.11412347853183746, 'pose_z': 0.09975675493478775, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.014306279830634594, 'half_extent_y': 0.015867985785007477, 'half_extent_z': 0.02475675567984581}
          24 +SEED 4 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 2}
          25 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          26 +target_region Kinematic3DCuboid {'pose_x': 0.17281867563724518, 'pose_y': 0.07829679548740387, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.048291683197021484, 'half_extent_y': 0.035339824855327606, 'half_extent_z': 0.004999999888241291}
          27 +obstruction1 Kinematic3DCuboid {'pose_x': 0.17259173095226288, 'pose_y': 0.07778430730104446, 'pose_z': 0.0985538512468338, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.019689328968524933, 'half_extent_y': 0.019290264695882797, 'half_extent_z': 0.013553851284086704}
          28 +target_block Kinematic3DCuboid {'pose_x': 0.3974335789680481, 'pose_y': -0.241974338889122, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.03863334655761719, 'half_extent_y': 0.028271861374378204, 'half_extent_z': 0.02500000037252903}
          29 +obstruction0 Kinematic3DCuboid {'pose_x': 0.20295670628547668, 'pose_y': 0.1171213760972023, 'pose_z': 0.10454306751489639, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.015439414419233799, 'half_extent_y': 0.019022149965167046, 'half_extent_z': 0.01954307034611702}
          30 +SEED 5 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 2}
          31 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          32 +target_region Kinematic3DCuboid {'pose_x': 0.23323433101177216, 'pose_y': -0.3173888027667999, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.04415008798241615, 'half_extent_y': 0.04423822462558746, 'half_extent_z': 0.004999999888241291}
          33 +obstruction1 Kinematic3DCuboid {'pose_x': 0.19244296848773956, 'pose_y': -0.3001417815685272, 'pose_z': 0.10042903572320938, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.010608026757836342, 'half_extent_y': 0.015555961057543755, 'half_extent_z': 0.015429032035171986}
          34 +target_block Kinematic3DCuboid {'pose_x': 0.4644085764884949, 'pose_y': 0.11111042648553848, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.03532006964087486, 'half_extent_y': 0.03539057821035385, 'half_extent_z': 0.02500000037252903}
          35 +obstruction0 Kinematic3DCuboid {'pose_x': 0.2229616791009903, 'pose_y': -0.3180749714374542, 'pose_z': 0.1129535511136055, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.014349475502967834, 'half_extent_y': 0.019741861149668694, 'half_extent_z': 0.027953552082180977}
          36 +SEED 6 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 1}
          37 +target_block Kinematic3DCuboid {'pose_x': 0.35964807868003845, 'pose_y': -0.12778636813163757, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.028915943577885628, 'half_extent_y': 0.024238500744104385, 'half_extent_z': 0.02500000037252903}
          38 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          39 +target_region Kinematic3DCuboid {'pose_x': 0.25887131690979004, 'pose_y': 0.3604186475276947, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.0361449308693409, 'half_extent_y': 0.030298126861453056, 'half_extent_z': 0.004999999888241291}
          40 +obstruction0 Kinematic3DCuboid {'pose_x': 0.29616957902908325, 'pose_y': 0.3819534182548523, 'pose_z': 0.11200382560491562, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.011229723691940308, 'half_extent_y': 0.010517292656004429, 'half_extent_z': 0.027003826573491096}
          41 +SEED 7 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 2}
          42 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          43 +target_region Kinematic3DCuboid {'pose_x': 0.21138089895248413, 'pose_y': -0.14111600816249847, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.03875286504626274, 'half_extent_y': 0.046916414052248, 'half_extent_z': 0.004999999888241291}
          44 +obstruction1 Kinematic3DCuboid {'pose_x': 0.19748550653457642, 'pose_y': -0.2596478760242462, 'pose_z': 0.097443588078022, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.019955003634095192, 'half_extent_y': 0.017926618456840515, 'half_extent_z': 0.022443585097789764}
          45 +target_block Kinematic3DCuboid {'pose_x': 0.13278193771839142, 'pose_y': 0.23286931216716766, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.031002290546894073, 'half_extent_y': 0.03753313049674034, 'half_extent_z': 0.02500000037252903}
          46 +obstruction0 Kinematic3DCuboid {'pose_x': 0.20672087371349335, 'pose_y': -0.14065960049629211, 'pose_z': 0.1005685105919838, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.014679349958896637, 'half_extent_y': 0.013030324131250381, 'half_extent_z': 0.015568512491881847}
          47 +SEED 8 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 2}
          48 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          49 +target_region Kinematic3DCuboid {'pose_x': 0.39821675419807434, 'pose_y': 0.25920993089675903, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.029809167608618736, 'half_extent_y': 0.049618303775787354, 'half_extent_z': 0.004999999888241291}
          50 +obstruction1 Kinematic3DCuboid {'pose_x': 0.42532429099082947, 'pose_y': 0.22171513736248016, 'pose_z': 0.1070854440331459, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.012559205293655396, 'half_extent_y': 0.01590902917087078, 'half_extent_z': 0.022085445001721382}
          51 +target_block Kinematic3DCuboid {'pose_x': 0.278115451335907, 'pose_y': -0.09169850498437881, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.02384733408689499, 'half_extent_y': 0.039694644510746, 'half_extent_z': 0.02500000037252903}
          52 +obstruction0 Kinematic3DCuboid {'pose_x': 0.37770166993141174, 'pose_y': 0.2923009693622589, 'pose_z': 0.10014290362596512, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.01478965487331152, 'half_extent_y': 0.01241352129727602, 'half_extent_z': 0.015142904594540596}
          53 +SEED 9 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 1}
          54 +target_block Kinematic3DCuboid {'pose_x': 0.4175705015659332, 'pose_y': 0.315448522567749, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.036885980516672134, 'half_extent_y': 0.022883612662553787, 'half_extent_z': 0.02500000037252903}
          55 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          56 +target_region Kinematic3DCuboid {'pose_x': 0.3854208290576935, 'pose_y': 0.16049827635288239, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.04610747471451759, 'half_extent_y': 0.02860451675951481, 'half_extent_z': 0.004999999888241291}
          57 +obstruction0 Kinematic3DCuboid {'pose_x': 0.4182850122451782, 'pose_y': 0.19173592329025269, 'pose_z': 0.09630308300256729, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.014372480101883411, 'half_extent_y': 0.01484944298863411, 'half_extent_z': 0.011303083971142769}
          58 +SEED 10 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 2}
          59 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          60 +target_region Kinematic3DCuboid {'pose_x': 0.1938587725162506, 'pose_y': 0.009571950882673264, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.048680052161216736, 'half_extent_y': 0.026230454444885254, 'half_extent_z': 0.004999999888241291}
          61 +obstruction1 Kinematic3DCuboid {'pose_x': 0.19671772420406342, 'pose_y': 0.2702596187591553, 'pose_z': 0.08778702467679977, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.011449947021901608, 'half_extent_y': 0.017455801367759705, 'half_extent_z': 0.012787028215825558}
          62 +target_block Kinematic3DCuboid {'pose_x': 0.3608908951282501, 'pose_y': 0.2590554654598236, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.03894403949379921, 'half_extent_y': 0.020984362810850143, 'half_extent_z': 0.02500000037252903}
          63 +obstruction0 Kinematic3DCuboid {'pose_x': 0.22099873423576355, 'pose_y': 0.02971748821437359, 'pose_z': 0.10176430642604828, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.019569259136915207, 'half_extent_y': 0.018253328278660774, 'half_extent_z': 0.016764305531978607}
          64 +SEED 11 COUNT_ARG None MAX 1000 ASHAPE (11,) LOW [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0] HIGH [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0] INFO {'object_count': 0}
          65 +target_block Kinematic3DCuboid {'pose_x': 0.3441009819507599, 'pose_y': -0.09747365862131119, 'pose_z': 0.10000000149011612, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.019085684791207314, 'half_extent_y': 0.027982668951153755, 'half_extent_z': 0.02500000037252903}
          66 +robot Kinematic3DRobot {'pos_base_x': -0.11999999731779099, 'pos_base_y': 0.0, 'pos_base_rot': 0.0, 'joint_1': 0.0, 'joint_2': -0.3499999940395355, 'joint_3': -3.1415927410125732, 'joint_4': -2.5, 'joint_5': 0.0, 'joint_6': -0.8700000047683716, 'joint_7': 1.5707963705062866, 'finger_state': 0.0, 'grasp_active': 0.0, 'grasp_tf_x': 0.0, 'grasp_tf_y': 0.0, 'grasp_tf_z': 0.0, 'grasp_tf_qx': 0.0, 'grasp_tf_qy': 0.0, 'grasp_tf_qz': 0.0, 'grasp_tf_qw': 0.0}
          67 +target_region Kinematic3DCuboid {'pose_x': 0.13396383821964264, 'pose_y': -0.2570292055606842, 'pose_z': 0.07999999821186066, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0, 'grasp_active': 0.0, 'object_type': -1.0, 'half_extent_x': 0.023857105523347855, 'half_extent_y': 0.034978337585926056, 'half_extent_z': 0.004999999888241291}
diff --git a/probe_geometry_summary.py b/probe_geometry_summary.py
new file mode 100644
index 0000000..e9b08c4
--- /dev/null
+++ b/probe_geometry_summary.py
@@ -0,0 +1,54 @@
           1 +from collections import Counter
           2 +from env_client import make_env
           3 +
           4 +
           5 +def xyzhe(state, name):
           6 +    o = state.get_object_from_name(name)
           7 +    fs = ["pose_x", "pose_y", "pose_z", "half_extent_x", "half_extent_y", "half_extent_z"]
           8 +    return [float(state.get(o, f)) for f in fs]
           9 +
          10 +
          11 +def rng_update(ranges, key, vals):
          12 +    if key not in ranges:
          13 +        ranges[key] = [[x, x] for x in vals]
          14 +    for r, x in zip(ranges[key], vals):
          15 +        r[0] = min(r[0], x)
          16 +        r[1] = max(r[1], x)
          17 +
          18 +
          19 +env = make_env()
          20 +counts = Counter()
          21 +ranges = {}
          22 +on_region = 0
          23 +off_region = 0
          24 +overlaps = []
          25 +for seed in range(100):
          26 +    state, info = env.reset(seed=seed)
          27 +    names = state.get_object_names()
          28 +    obs = sorted(n for n in names if n.startswith("obstruction"))
          29 +    counts[len(obs)] += 1
          30 +    reg = xyzhe(state, "target_region")
          31 +    block = xyzhe(state, "target_block")
          32 +    rng_update(ranges, "region", reg)
          33 +    rng_update(ranges, "block", block)
          34 +    for name in obs:
          35 +        v = xyzhe(state, name)
          36 +        rng_update(ranges, "obstruction", v)
          37 +        dx, dy = abs(v[0]-reg[0]), abs(v[1]-reg[1])
          38 +        hit = dx < v[3]+reg[3] and dy < v[4]+reg[4]
          39 +        if hit: on_region += 1
          40 +        else: off_region += 1
          41 +        overlaps.append((dx, dy, dx-(v[3]+reg[3]), dy-(v[4]+reg[4])))
          42 +print("counts", counts)
          43 +print("ranges [x,y,z,hx,hy,hz]", ranges)
          44 +print("obstruction overlaps/off", on_region, off_region)
          45 +print("separation delta extrema", [[min(v[i] for v in overlaps), max(v[i] for v in overlaps)] for i in range(4)])
          46 +
          47 +for count in [0, 1, 2, 3, 5, 10]:
          48 +    try:
          49 +        state, info = env.reset(seed=123, options={"object_count": count})
          50 +        actual = sum(n.startswith("obstruction") for n in state.get_object_names())
          51 +        print("forced", count, "actual", actual, "info", info)
          52 +    except Exception as e:
          53 +        print("forced", count, "ERR", repr(e))
          54 +env.close()
```

</details>

<a id="C004"></a>
### C004 · Add calibrated planar reach probe for target grasp

Commit `a375a2d78bc2122bf9b546ac17af78bca2a08ca2`; parents: c6dd7870bf44af9d7a0280926d8552e48ddfed5f. Recorded author date: 2026-09-09T15:22:17+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0039](01_timeline.md#E0039): commit hash in recorded output.
[Controller after this commit](evidence/versions/C004_a375a2d_approach.py) · [Exact all-file diff](evidence/diffs/C004_a375a2d.diff)

[Previous saved controller snapshot](evidence/versions/C003_c6dd787_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 94a75b2..fdfc4e2 100644
--- a/approach.py
+++ b/approach.py
@@ -12,6 +12,8 @@ class GeneratedApproach:
   12     12      def reset(self, state, info):
   13     13          self.t = 0
   14     14          self.target_y = self._v(state, "target_block", "pose_y")
          15 +        self.target_q = np.array([0.0, 0.177, -np.pi, -2.267, 0.0, -0.673,
          16 +                                  np.pi / 2])
   15     17  
   16     18      @staticmethod
   17     19      def _v(state, name, feature):
@@ -21,7 +23,10 @@ class GeneratedApproach:
   21     23          self.t += 1
   22     24          a = np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
   23     25          robot_y = self._v(state, "robot", "pos_base_y")
   24        -        a[1] = np.clip(self.target_y - robot_y, -0.2, 0.2)
   25        -        if self.t >= 3:
          26 +        a[1] = np.clip(self.target_y - 0.00135 - robot_y, -0.2, 0.2)
          27 +        robot = state.get_object_from_name("robot")
          28 +        joints = np.array([state.get(robot, "joint_%d" % j) for j in range(1, 8)])
          29 +        a[3:10] = np.clip(self.target_q - joints, -0.2, 0.2)
          30 +        if self.t >= 6:
   26     31              a[10] = -1.0
   27     32          return a
diff --git a/probe_geometry_clearance.py b/probe_geometry_clearance.py
new file mode 100644
index 0000000..865498b
--- /dev/null
+++ b/probe_geometry_clearance.py
@@ -0,0 +1,35 @@
           1 +from collections import Counter
           2 +from env_client import make_env
           3 +
           4 +
           5 +def box(s, n):
           6 +    o = s.get_object_from_name(n)
           7 +    return tuple(float(s.get(o, f)) for f in
           8 +                 ("pose_x", "pose_y", "half_extent_x", "half_extent_y"))
           9 +
          10 +
          11 +def signed_axis_gaps(a, b):
          12 +    return abs(a[0]-b[0])-a[2]-b[2], abs(a[1]-b[1])-a[3]-b[3]
          13 +
          14 +
          15 +env = make_env()
          16 +ncounts = Counter()
          17 +br = []
          18 +bo = []
          19 +rratios = []
          20 +for seed in range(300):
          21 +    s, info = env.reset(seed=1000+seed)
          22 +    reg, blk = box(s, "target_region"), box(s, "target_block")
          23 +    ncounts[info["object_count"]] += 1
          24 +    br.append(signed_axis_gaps(reg, blk))
          25 +    rratios.append((blk[2]/reg[2], blk[3]/reg[3]))
          26 +    for n in s.get_object_names():
          27 +        if n.startswith("obstruction"):
          28 +            bo.append(signed_axis_gaps(blk, box(s, n)))
          29 +print("counts", ncounts)
          30 +print("block/region axis gap minima", min(x[0] for x in br), min(x[1] for x in br))
          31 +print("block/region overlap both", sum(x < 0 and y < 0 for x, y in br))
          32 +print("block/obstruction axis gap minima", min(x[0] for x in bo), min(x[1] for x in bo))
          33 +print("block/obstruction overlap both", sum(x < 0 and y < 0 for x, y in bo))
          34 +print("extent ratios", min(x for x,y in rratios), max(x for x,y in rratios), min(y for x,y in rratios), max(y for x,y in rratios))
          35 +env.close()
diff --git a/probe_geometry_heights.py b/probe_geometry_heights.py
new file mode 100644
index 0000000..adca344
--- /dev/null
+++ b/probe_geometry_heights.py
@@ -0,0 +1,23 @@
           1 +from collections import Counter
           2 +from env_client import make_env
           3 +
           4 +env = make_env()
           5 +c = Counter()
           6 +samples = []
           7 +for seed in range(300):
           8 +    s, _ = env.reset(seed=seed)
           9 +    for n in s.get_object_names():
          10 +        if not n.startswith("obstruction"):
          11 +            continue
          12 +        o = s.get_object_from_name(n)
          13 +        bottom = float(s.get(o, "pose_z") - s.get(o, "half_extent_z"))
          14 +        r = s.get_object_from_name("target_region")
          15 +        dx = abs(float(s.get(o,"pose_x") - s.get(r,"pose_x")))
          16 +        dy = abs(float(s.get(o,"pose_y") - s.get(r,"pose_y")))
          17 +        kind = round(bottom, 3)
          18 +        c[kind] += 1
          19 +        if len(samples) < 10 and kind == .075:
          20 +            samples.append((seed,n,bottom,dx,dy))
          21 +print(c)
          22 +print("table samples", samples)
          23 +env.close()
diff --git a/probe_grasp_agent.py b/probe_grasp_agent.py
new file mode 100644
index 0000000..8589ddc
--- /dev/null
+++ b/probe_grasp_agent.py
@@ -0,0 +1,35 @@
           1 +import itertools
           2 +import numpy as np
           3 +from env_client import make_env
           4 +
           5 +
           6 +def v(s, n, f): return float(s.get(s.get_object_from_name(n), f))
           7 +
           8 +
           9 +patterns = [
          10 +    (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0),
          11 +    (0, 1, 0), (0, -1, 0), (1, 0, 1), (-1, 0, -1),
          12 +    (1, 1, 1), (-1, -1, -1), (1, -1, 1), (-1, 1, -1),
          13 +]
          14 +for pat in patterns:
          15 +    env = make_env(); s, _ = env.reset(seed=0)
          16 +    ty = v(s, "target_block", "pose_y")
          17 +    base = (v(s,"target_block","pose_x"), ty, v(s,"target_block","pose_z"))
          18 +    # align laterally
          19 +    a=np.zeros(11,np.float32); a[1]=np.clip(ty-v(s,"robot","pos_base_y"),-.2,.2)
          20 +    s,*_=env.step(a)
          21 +    found = None; maxmove=0
          22 +    for t in range(120):
          23 +        a=np.zeros(11,np.float32)
          24 +        # Oscillate every 20 steps to scan rather than pin at limit.
          25 +        sg = 1 if (t//20)%2==0 else -1
          26 +        a[4]=.12*pat[0]*sg; a[6]=.12*pat[1]*sg; a[8]=.12*pat[2]*sg; a[10]=-1
          27 +        s,r,te,tr,info=env.step(a)
          28 +        xyz=(v(s,"target_block","pose_x"),v(s,"target_block","pose_y"),v(s,"target_block","pose_z"))
          29 +        maxmove=max(maxmove, sum((xyz[i]-base[i])**2 for i in range(3))**.5)
          30 +        if v(s,"robot","grasp_active") or v(s,"target_block","grasp_active"):
          31 +            found=(t,xyz,[v(s,"robot",f"joint_{i}") for i in range(1,8)],
          32 +                   [v(s,"robot",f"grasp_tf_{c}") for c in "xyz"])
          33 +            break
          34 +    print("PAT",pat,"found",found,"maxmove",round(maxmove,5),"final joints",[round(v(s,"robot",f"joint_{i}"),3) for i in range(1,8)])
          35 +    env.close()
```

</details>

<a id="C005"></a>
### C005 · Probe extended high arm configuration

Commit `62c46a797d1e58f14f995e34f07220b05a4eef94`; parents: a375a2d78bc2122bf9b546ac17af78bca2a08ca2. Recorded author date: 2026-09-09T15:23:19+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0050](01_timeline.md#E0050): commit hash in recorded output.
[Controller after this commit](evidence/versions/C005_62c46a7_approach.py) · [Exact all-file diff](evidence/diffs/C005_62c46a7.diff)

[Previous saved controller snapshot](evidence/versions/C004_a375a2d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fdfc4e2..3140a0e 100644
--- a/approach.py
+++ b/approach.py
@@ -12,7 +12,7 @@ class GeneratedApproach:
   12     12      def reset(self, state, info):
   13     13          self.t = 0
   14     14          self.target_y = self._v(state, "target_block", "pose_y")
   15        -        self.target_q = np.array([0.0, 0.177, -np.pi, -2.267, 0.0, -0.673,
          15 +        self.target_q = np.array([0.0, 0.8, -np.pi, -1.5, 0.0, -0.5,
   16     16                                    np.pi / 2])
   17     17  
   18     18      @staticmethod
@@ -27,6 +27,6 @@ class GeneratedApproach:
   27     27          robot = state.get_object_from_name("robot")
   28     28          joints = np.array([state.get(robot, "joint_%d" % j) for j in range(1, 8)])
   29     29          a[3:10] = np.clip(self.target_q - joints, -0.2, 0.2)
   30        -        if self.t >= 6:
   31        -            a[10] = -1.0
          30 +        # Keep open during this reach calibration.
          31 +        a[10] = 1.0
   32     32          return a
diff --git a/probe_random_grasp_agent.py b/probe_random_grasp_agent.py
new file mode 100644
index 0000000..7f892cc
--- /dev/null
+++ b/probe_random_grasp_agent.py
@@ -0,0 +1,31 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +
           4 +def v(s,n,f): return float(s.get(s.get_object_from_name(n),f))
           5 +
           6 +rng=np.random.default_rng(123)
           7 +for seed in range(4):
           8 +    env=make_env(); s,info=env.reset(seed=seed)
           9 +    names=list(s.get_object_names()); movable=[n for n in names if n!="robot" and n!="target_region"]
          10 +    init={n:np.array([v(s,n,"pose_x"),v(s,n,"pose_y"),v(s,n,"pose_z")]) for n in movable}
          11 +    tb="target_block"
          12 +    best=[]
          13 +    for t in range(700):
          14 +        a=np.zeros(11,np.float32)
          15 +        # Track target y with base. Keep x fixed because forward base is blocked.
          16 +        a[1]=np.clip(v(s,tb,"pose_y")-v(s,"robot","pos_base_y"),-.2,.2)
          17 +        # Correlated random walk, emphasizing pitch joints, periodic re-randomization.
          18 +        if t%12==0:
          19 +            u=rng.choice([-1.,0.,1.],size=7,p=[.4,.2,.4])*.18
          20 +        a[3:10]=u
          21 +        a[10]=-1
          22 +        s,r,te,tr,ii=env.step(a)
          23 +        moved=max(np.linalg.norm(np.array([v(s,n,"pose_x"),v(s,n,"pose_y"),v(s,n,"pose_z")])-init[n]) for n in movable)
          24 +        if moved>.002 and (not best or moved>best[-1][0]+.005):
          25 +            best.append((moved,t,[round(v(s,"robot",f"joint_{i}"),3) for i in range(1,8)]))
          26 +        held=[n for n in movable if v(s,n,"grasp_active")>.5]
          27 +        if v(s,"robot","grasp_active")>.5 or held:
          28 +            print("GRASP seed",seed,"t",t,"held",held,"j",[round(v(s,"robot",f"joint_{i}"),5) for i in range(1,8)],"base",v(s,"robot","pos_base_x"),v(s,"robot","pos_base_y"),"tf",[v(s,"robot",f"grasp_tf_{c}") for c in "xyz"])
          29 +            break
          30 +    else: print("NONE seed",seed,"bestmove",best[-5:])
          31 +    env.close()
```

</details>

<a id="C006"></a>
### C006 · Add feedback Cartesian pick-and-place controller

Commit `1a6664c6136702c8c1c8eb65020feb2f5cfa50ef`; parents: 62c46a797d1e58f14f995e34f07220b05a4eef94. Recorded author date: 2026-09-09T15:34:24+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0078](01_timeline.md#E0078): commit hash in recorded output.
[Controller after this commit](evidence/versions/C006_1a6664c_approach.py) · [Exact all-file diff](evidence/diffs/C006_1a6664c.diff)

[Previous saved controller snapshot](evidence/versions/C005_62c46a7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3140a0e..3ce5345 100644
--- a/approach.py
+++ b/approach.py
@@ -1,32 +1,62 @@
    1        -"""Reactive policy for the variable-count Obstruction3D task."""
    2        -
           1 +"""Feedback manipulation policy for Obstruction3D."""
    3      2  import numpy as np
    4      3  
    5        -
    6      4  class GeneratedApproach:
    7        -    def __init__(self, action_space, observation_space, primitives):
    8        -        self.action_space = action_space
    9        -        self.observation_space = observation_space
   10        -        self.t = 0
   11        -
   12        -    def reset(self, state, info):
   13        -        self.t = 0
   14        -        self.target_y = self._v(state, "target_block", "pose_y")
   15        -        self.target_q = np.array([0.0, 0.8, -np.pi, -1.5, 0.0, -0.5,
   16        -                                  np.pi / 2])
   17        -
           5 +    def __init__(self, action_space, observation_space, primitives): self.action_space=action_space
   18      6      @staticmethod
   19        -    def _v(state, name, feature):
   20        -        return state.get(state.get_object_from_name(name), feature)
   21        -
   22        -    def get_action(self, state):
   23        -        self.t += 1
   24        -        a = np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
   25        -        robot_y = self._v(state, "robot", "pos_base_y")
   26        -        a[1] = np.clip(self.target_y - 0.00135 - robot_y, -0.2, 0.2)
   27        -        robot = state.get_object_from_name("robot")
   28        -        joints = np.array([state.get(robot, "joint_%d" % j) for j in range(1, 8)])
   29        -        a[3:10] = np.clip(self.target_q - joints, -0.2, 0.2)
   30        -        # Keep open during this reach calibration.
   31        -        a[10] = 1.0
           7 +    def _v(s,n,f): return s.get(s.get_object_from_name(n),f)
           8 +    def _xyz(self,s,n): return np.array([self._v(s,n,"pose_"+c) for c in "xyz"])
           9 +    def reset(self,state,info):
          10 +        self.region=self._xyz(state,"target_region"); self.object_name="target_block"
          11 +        self.mode="pick"; self.pick_i=self.pick_t=0; self.controls=[1,4,6,8]
          12 +        self.J=np.zeros((3,4)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
          13 +        self.last_delta=0.; self.move_count=0; self.waypoint=0
          14 +        x=self._v(state,self.object_name,"pose_x")
          15 +        if x<.23: base=(.18,-2.50,-.75)
          16 +        else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
          17 +        self.pick_poses=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
          18 +                         (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10)]
          19 +    def _held(self,s): return self._v(s,"robot","grasp_active")>.5
          20 +    def _start_calibration(self,s):
          21 +        self.mode="calibrate"; self.cal_i=0; self.cal_sign=1
          22 +        self.last_pos=self._xyz(s,self.object_name); self.last_delta=0.
          23 +    def get_action(self,state):
          24 +        a=np.zeros(self.action_space.shape,dtype=self.action_space.dtype)
          25 +        if self._held(state) and self.mode=="pick": self._start_calibration(state)
          26 +        if self.mode=="pick":
          27 +            x,y,z=self._xyz(state,self.object_name); q2,q4,q6=self.pick_poses[self.pick_i]
          28 +            target=np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]); rob=state.get_object_from_name("robot")
          29 +            cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
          30 +            a[1]=np.clip(y-.00135-self._v(state,"robot","pos_base_y"),-.2,.2)
          31 +            a[3:10]=np.clip(target-cur,-.2,.2); a[10]=1. if self.pick_t<7 else -1.
          32 +            self.pick_t+=1
          33 +            if self.pick_t>=12:
          34 +                self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
          35 +            return a
          36 +        pos=self._xyz(state,self.object_name)
          37 +        if self.mode=="calibrate" and self.last_delta:
          38 +            col=(pos-self.last_pos)/self.last_delta
          39 +            if self.cal_sign<0:
          40 +                self.J[:,self.cal_i]=.5*(self.J[:,self.cal_i]+col); self.cal_i+=1; self.cal_sign=1
          41 +            else: self.J[:,self.cal_i]=col; self.cal_sign=-1
          42 +            self.last_delta=0.
          43 +        if self.mode=="calibrate":
          44 +            if self.cal_i>=len(self.controls): self.mode="move"; self.move_count=0
          45 +            else:
          46 +                d=.04*self.cal_sign; a[self.controls[self.cal_i]]=d; a[10]=-1.
          47 +                self.last_pos=pos; self.last_delta=d; return a
          48 +        goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
          49 +               np.array([self.region[0],self.region[1],.115])]
          50 +        goal=goals[self.waypoint]; err=goal-pos; tol=.012 if self.waypoint<2 else .004
          51 +        if np.linalg.norm(err)<tol:
          52 +            self.waypoint+=1
          53 +            if self.waypoint>=3: self.mode="release"
          54 +            else: self._start_calibration(state)
          55 +            a[10]=-1.; return a
          56 +        if self.mode=="release": a[10]=1.; return a
          57 +        JJ=self.J@self.J.T+1e-5*np.eye(3)
          58 +        u=self.J.T@np.linalg.solve(JJ,np.clip(err,-.06,.06)); u=np.clip(u,-.12,.12)
          59 +        for k,idx in enumerate(self.controls): a[idx]=u[k]
          60 +        a[10]=-1.; self.move_count+=1
          61 +        if self.move_count>=7: self._start_calibration(state)
   32     62          return a
diff --git a/scan_grasp.py b/scan_grasp.py
new file mode 100644
index 0000000..3803eac
--- /dev/null
+++ b/scan_grasp.py
@@ -0,0 +1,27 @@
           1 +import concurrent.futures
           2 +import itertools
           3 +import numpy as np
           4 +from env_client import make_env
           5 +
           6 +def v(s,n,f): return s.get(s.get_object_from_name(n),f)
           7 +
           8 +def trial(cfg):
           9 +    q2,q4,q6=cfg
          10 +    e=make_env(); s,_=e.reset(seed=0)
          11 +    target=np.array([0,q2,-np.pi,q4,0,q6,np.pi/2])
          12 +    for t in range(12):
          13 +        r=s.get_object_from_name('robot')
          14 +        cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)])
          15 +        a=np.zeros(11,np.float32)
          16 +        a[1]=np.clip(v(s,'target_block','pose_y')-.00135-v(s,'robot','pos_base_y'),-.2,.2)
          17 +        a[3:10]=np.clip(target-cur,-.2,.2)
          18 +        if t>=7:a[10]=-1
          19 +        s,_,_,_,_=e.step(a)
          20 +        if v(s,'robot','grasp_active')>.5:
          21 +            e.close(); return cfg,True
          22 +    e.close(); return cfg,False
          23 +
          24 +configs=list(itertools.product([.25,.35,.45,.55,.65],[-2.2,-2.0,-1.8],[-1.2,-1.0,-.8,-.6,-.4]))
          25 +with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
          26 +    for cfg,ok in ex.map(trial,configs):
          27 +        if ok: print('SUCCESS',cfg,flush=True)
diff --git a/scan_low.py b/scan_low.py
new file mode 100644
index 0000000..2ad7585
--- /dev/null
+++ b/scan_low.py
@@ -0,0 +1,15 @@
           1 +import concurrent.futures,itertools,numpy as np
           2 +from env_client import make_env
           3 +def v(s,n,f):return s.get(s.get_object_from_name(n),f)
           4 +def trial(c):
           5 + e=make_env();s,_=e.reset(seed=1);tar=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2]);y=v(s,'target_block','pose_y')
           6 + for t in range(12):
           7 +  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
           8 +  a[1]=np.clip(y-.00135-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2);a[10]=-1 if t>=7 else 1
           9 +  s,*_=e.step(a)
          10 +  if v(s,'robot','grasp_active')>.5:e.close();return c,True
          11 + e.close();return c,False
          12 +cs=list(itertools.product([.12,.18,.24,.30],[-2.5,-2.4,-2.3,-2.2],[-.9,-.75,-.6,-.45]))
          13 +with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
          14 + for c,o in ex.map(trial,cs):
          15 +  if o:print('SUCCESS',c,flush=True)
diff --git a/test_pick_formula.py b/test_pick_formula.py
new file mode 100644
index 0000000..ba8d2fa
--- /dev/null
+++ b/test_pick_formula.py
@@ -0,0 +1,21 @@
           1 +import concurrent.futures
           2 +import numpy as np
           3 +from env_client import make_env
           4 +
           5 +def v(s,n,f): return s.get(s.get_object_from_name(n),f)
           6 +def trial(seed):
           7 + e=make_env();s,_=e.reset(seed=seed); x=v(s,'target_block','pose_x'); y=v(s,'target_block','pose_y')
           8 + # Empirical planar reach interpolation.
           9 + q2=.35+2.0*(x-.336); q4=-2.2+1.5*(x-.336); q6=-.6+.8*(x-.336)
          10 + tar=np.array([0,q2,-np.pi,q4,0,q6,np.pi/2])
          11 + ok=False
          12 + for t in range(12):
          13 +  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)])
          14 +  a=np.zeros(11,np.float32);a[1]=np.clip(y-.00135-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2)
          15 +  if t>=7:a[10]=-1
          16 +  s,*_=e.step(a)
          17 +  if v(s,'robot','grasp_active')>.5:ok=True;break
          18 + e.close();return seed,round(x,3),np.round(tar[[1,3,5]],3).tolist(),ok
          19 +
          20 +with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
          21 + for z in ex.map(trial,range(20)):print(z,flush=True)
```

</details>

<a id="C007"></a>
### C007 · Add end-to-end policy test harness

Commit `6749ed7523aeff1f2c6c431e63cda154046c4715`; parents: 1a6664c6136702c8c1c8eb65020feb2f5cfa50ef. Recorded author date: 2026-09-09T15:34:39+02:00.

File roles (automatic): diagnostic/test.

- [E0082](01_timeline.md#E0082): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C007_6749ed7.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..cef8420
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys
           4 +for seed in map(int,sys.argv[1:] or [11]):
           5 + e=make_env();s,i=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
           6 + for t in range(e.max_steps):
           7 +  s,r,d,tr,i=e.step(p.get_action(s))
           8 +  if t%25==0:
           9 +   rob=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
          10 +   print(seed,t,p.mode,p.waypoint,'held',s.get(rob,'grasp_active'),'b',[round(s.get(b,'pose_'+c),3) for c in 'xyz'])
          11 +  if d or tr: break
          12 + print('RESULT',seed,t+1,d,tr,p.mode)
          13 + e.close()
```

</details>

<a id="C008"></a>
### C008 · Use calibrated grasp pose for precise final descent

Commit `82abb4ce7df4ba2d538b5095e8c3aa77b086e18b`; parents: 6749ed7523aeff1f2c6c431e63cda154046c4715. Recorded author date: 2026-09-09T15:35:38+02:00.

File roles (automatic): policy.

- [E0086](01_timeline.md#E0086): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_82abb4c_approach.py) · [Exact all-file diff](evidence/diffs/C008_82abb4c.diff)

[Previous saved controller snapshot](evidence/versions/C006_1a6664c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3ce5345..ee8c4e1 100644
--- a/approach.py
+++ b/approach.py
@@ -16,6 +16,10 @@ class GeneratedApproach:
   16     16          else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
   17     17          self.pick_poses=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
   18     18                           (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10)]
          19 +        rx=self.region[0]
          20 +        if rx<.23: self.lower_pose=(.18,-2.50,-.75)
          21 +        else: self.lower_pose=(.35+2*(rx-.336),-2.20+1.5*(rx-.336),-.60+.8*(rx-.336))
          22 +        self.lower_t=0
   19     23      def _held(self,s): return self._v(s,"robot","grasp_active")>.5
   20     24      def _start_calibration(self,s):
   21     25          self.mode="calibrate"; self.cal_i=0; self.cal_sign=1
@@ -34,6 +38,14 @@ class GeneratedApproach:
   34     38                  self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
   35     39              return a
   36     40          pos=self._xyz(state,self.object_name)
          41 +        if self.mode=="lower":
          42 +            q2,q4,q6=self.lower_pose; target=np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2])
          43 +            rob=state.get_object_from_name("robot")
          44 +            cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
          45 +            a[1]=np.clip(self.region[1]-.00135-self._v(state,"robot","pos_base_y"),-.12,.12)
          46 +            a[3:10]=np.clip(target-cur,-.10,.10); a[10]=-1.; self.lower_t+=1
          47 +            if self.lower_t>=15: self.mode="release"
          48 +            return a
   37     49          if self.mode=="calibrate" and self.last_delta:
   38     50              col=(pos-self.last_pos)/self.last_delta
   39     51              if self.cal_sign<0:
@@ -50,7 +62,7 @@ class GeneratedApproach:
   50     62          goal=goals[self.waypoint]; err=goal-pos; tol=.012 if self.waypoint<2 else .004
   51     63          if np.linalg.norm(err)<tol:
   52     64              self.waypoint+=1
   53        -            if self.waypoint>=3: self.mode="release"
          65 +            if self.waypoint>=2: self.mode="lower"; self.lower_t=0
   54     66              else: self._start_calibration(state)
   55     67              a[10]=-1.; return a
   56     68          if self.mode=="release": a[10]=1.; return a
```

</details>

<a id="C009"></a>
### C009 · Lower held block onto region before opening gripper

Commit `550e473b9d76de16b070743de67a49c4ed6370fb`; parents: 82abb4ce7df4ba2d538b5095e8c3aa77b086e18b. Recorded author date: 2026-09-09T15:36:44+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0098](01_timeline.md#E0098): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_550e473_approach.py) · [Exact all-file diff](evidence/diffs/C009_550e473.diff)

[Previous saved controller snapshot](evidence/versions/C008_82abb4c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ee8c4e1..552a8eb 100644
--- a/approach.py
+++ b/approach.py
@@ -19,6 +19,10 @@ class GeneratedApproach:
   19     19          rx=self.region[0]
   20     20          if rx<.23: self.lower_pose=(.18,-2.50,-.75)
   21     21          else: self.lower_pose=(.35+2*(rx-.336),-2.20+1.5*(rx-.336),-.60+.8*(rx-.336))
          22 +        # With an object in the fingers the nominal pickup pose leaves its bottom
          23 +        # about 2 cm high; this coupled correction lowers without shifting x.
          24 +        self.lower_pose=(self.lower_pose[0]+.10,self.lower_pose[1]-.027,
          25 +                         self.lower_pose[2]+.10)
   22     26          self.lower_t=0
   23     27      def _held(self,s): return self._v(s,"robot","grasp_active")>.5
   24     28      def _start_calibration(self,s):
diff --git a/probe_held_jacobian.py b/probe_held_jacobian.py
new file mode 100644
index 0000000..290b9e9
--- /dev/null
+++ b/probe_held_jacobian.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import numpy as np
           4 +def xyz(s):
           5 + o=s.get_object_from_name('target_block');return np.array([s.get(o,'pose_'+c) for c in 'xyz'])
           6 +e=make_env();s,i=e.reset(seed=11);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
           7 +for t in range(100):
           8 + s,*_=e.step(p.get_action(s))
           9 + if p.mode=='release':break
          10 +print('at',t,xyz(s))
          11 +for idx in [4,6,8]:
          12 + for d in [.04,-.04]:
          13 +  old=xyz(s);a=np.zeros(11,np.float32);a[idx]=d;a[10]=-1;s,*_=e.step(a)
          14 +  print(idx,d,xyz(s)-old)
          15 +e.close()
```

</details>

<a id="C010"></a>
### C010 · Open and retract gripper to complete release

Commit `eb9b61a2ac2c5f13d872cad50697cf6dcb721812`; parents: 550e473b9d76de16b070743de67a49c4ed6370fb. Recorded author date: 2026-09-09T15:39:37+02:00.

File roles (automatic): policy.

- [E0112](01_timeline.md#E0112): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_eb9b61a_approach.py) · [Exact all-file diff](evidence/diffs/C010_eb9b61a.diff)

[Previous saved controller snapshot](evidence/versions/C009_550e473_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 552a8eb..971f8c3 100644
--- a/approach.py
+++ b/approach.py
@@ -24,6 +24,7 @@ class GeneratedApproach:
   24     24          self.lower_pose=(self.lower_pose[0]+.10,self.lower_pose[1]-.027,
   25     25                           self.lower_pose[2]+.10)
   26     26          self.lower_t=0
          27 +        self.release_t=0
   27     28      def _held(self,s): return self._v(s,"robot","grasp_active")>.5
   28     29      def _start_calibration(self,s):
   29     30          self.mode="calibrate"; self.cal_i=0; self.cal_sign=1
@@ -48,7 +49,7 @@ class GeneratedApproach:
   48     49              cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
   49     50              a[1]=np.clip(self.region[1]-.00135-self._v(state,"robot","pos_base_y"),-.12,.12)
   50     51              a[3:10]=np.clip(target-cur,-.10,.10); a[10]=-1.; self.lower_t+=1
   51        -            if self.lower_t>=15: self.mode="release"
          52 +            if self.lower_t>=15: self.mode="release"; self.release_t=0
   52     53              return a
   53     54          if self.mode=="calibrate" and self.last_delta:
   54     55              col=(pos-self.last_pos)/self.last_delta
@@ -69,7 +70,12 @@ class GeneratedApproach:
   69     70              if self.waypoint>=2: self.mode="lower"; self.lower_t=0
   70     71              else: self._start_calibration(state)
   71     72              a[10]=-1.; return a
   72        -        if self.mode=="release": a[10]=1.; return a
          73 +        if self.mode=="release":
          74 +            # Open, then retract the hand so contact cannot keep the grasp latched.
          75 +            a[10]=1.
          76 +            if self.release_t<6: a[4]=-.08
          77 +            self.release_t+=1
          78 +            return a
   73     79          JJ=self.J@self.J.T+1e-5*np.eye(3)
   74     80          u=self.J.T@np.linalg.solve(JJ,np.clip(err,-.06,.06)); u=np.clip(u,-.12,.12)
   75     81          for k,idx in enumerate(self.controls): a[idx]=u[k]
```

</details>

<a id="C011"></a>
### C011 · Drop from aligned clearance height to avoid gripper wedging

Commit `4bd8c34888fd47acc646c616f718dbffc7d6227b`; parents: eb9b61a2ac2c5f13d872cad50697cf6dcb721812. Recorded author date: 2026-09-09T15:40:42+02:00.

File roles (automatic): policy.

- [E0118](01_timeline.md#E0118): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_4bd8c34_approach.py) · [Exact all-file diff](evidence/diffs/C011_4bd8c34.diff)

[Previous saved controller snapshot](evidence/versions/C010_eb9b61a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 971f8c3..e397a4d 100644
--- a/approach.py
+++ b/approach.py
@@ -67,13 +67,15 @@ class GeneratedApproach:
   67     67          goal=goals[self.waypoint]; err=goal-pos; tol=.012 if self.waypoint<2 else .004
   68     68          if np.linalg.norm(err)<tol:
   69     69              self.waypoint+=1
   70        -            if self.waypoint>=2: self.mode="lower"; self.lower_t=0
          70 +            # Dropping from the clear waypoint avoids wedging the fingers against
          71 +            # the tabletop; gravity preserves the accurately controlled x/y.
          72 +            if self.waypoint>=2: self.mode="release"; self.release_t=0
   71     73              else: self._start_calibration(state)
   72     74              a[10]=-1.; return a
   73     75          if self.mode=="release":
   74     76              # Open, then retract the hand so contact cannot keep the grasp latched.
   75     77              a[10]=1.
   76        -            if self.release_t<6: a[4]=-.08
          78 +            if 2 <= self.release_t < 8: a[4]=-.08
   77     79              self.release_t+=1
   78     80              return a
   79     81          JJ=self.J@self.J.T+1e-5*np.eye(3)
```

</details>

<a id="C012"></a>
### C012 · Preserve grasp orientation during Cartesian feedback

Commit `8a08dc82fa6b3d4be26c7b68595d011e93f3283b`; parents: 4bd8c34888fd47acc646c616f718dbffc7d6227b. Recorded author date: 2026-09-09T15:43:00+02:00.

File roles (automatic): policy.

- [E0128](01_timeline.md#E0128): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_8a08dc8_approach.py) · [Exact all-file diff](evidence/diffs/C012_8a08dc8.diff)

[Previous saved controller snapshot](evidence/versions/C011_4bd8c34_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e397a4d..19aee16 100644
--- a/approach.py
+++ b/approach.py
@@ -8,8 +8,12 @@ class GeneratedApproach:
    8      8      def _xyz(self,s,n): return np.array([self._v(s,n,"pose_"+c) for c in "xyz"])
    9      9      def reset(self,state,info):
   10     10          self.region=self._xyz(state,"target_region"); self.object_name="target_block"
   11        -        self.mode="pick"; self.pick_i=self.pick_t=0; self.controls=[1,4,6,8]
   12        -        self.J=np.zeros((3,4)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
          11 +        self.mode="pick"; self.pick_i=self.pick_t=0
          12 +        # Virtual controls: lateral base, and two planar motions that preserve
          13 +        # q2+q4+q6 (therefore preserving the block's upright orientation).
          14 +        self.B=np.zeros((11,3)); self.B[1,0]=1.; self.B[4,1]=1.; self.B[8,1]=-1.
          15 +        self.B[6,2]=1.; self.B[8,2]=-1.
          16 +        self.J=np.zeros((3,3)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
   13     17          self.last_delta=0.; self.move_count=0; self.waypoint=0
   14     18          x=self._v(state,self.object_name,"pose_x")
   15     19          if x<.23: base=(.18,-2.50,-.75)
@@ -60,7 +64,7 @@ class GeneratedApproach:
   60     64          if self.mode=="calibrate":
   61     65              if self.cal_i>=len(self.controls): self.mode="move"; self.move_count=0
   62     66              else:
   63        -                d=.04*self.cal_sign; a[self.controls[self.cal_i]]=d; a[10]=-1.
          67 +                d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
   64     68                  self.last_pos=pos; self.last_delta=d; return a
   65     69          goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
   66     70                 np.array([self.region[0],self.region[1],.115])]
@@ -69,18 +73,17 @@ class GeneratedApproach:
   69     73              self.waypoint+=1
   70     74              # Dropping from the clear waypoint avoids wedging the fingers against
   71     75              # the tabletop; gravity preserves the accurately controlled x/y.
   72        -            if self.waypoint>=2: self.mode="release"; self.release_t=0
          76 +            if self.waypoint>=3: self.mode="release"; self.release_t=0
   73     77              else: self._start_calibration(state)
   74     78              a[10]=-1.; return a
   75     79          if self.mode=="release":
   76     80              # Open, then retract the hand so contact cannot keep the grasp latched.
   77     81              a[10]=1.
   78        -            if 2 <= self.release_t < 8: a[4]=-.08
   79     82              self.release_t+=1
   80     83              return a
   81     84          JJ=self.J@self.J.T+1e-5*np.eye(3)
   82     85          u=self.J.T@np.linalg.solve(JJ,np.clip(err,-.06,.06)); u=np.clip(u,-.12,.12)
   83        -        for k,idx in enumerate(self.controls): a[idx]=u[k]
          86 +        a += self.B@u
   84     87          a[10]=-1.; self.move_count+=1
   85     88          if self.move_count>=7: self._start_calibration(state)
   86     89          return a
```

</details>

<a id="C013"></a>
### C013 · Fix virtual-control calibration dimension

Commit `fbe1b5d263ae81383fc57680bc8e522fd9fbc695`; parents: 8a08dc82fa6b3d4be26c7b68595d011e93f3283b. Recorded author date: 2026-09-09T15:43:14+02:00.

File roles (automatic): policy.

- [E0132](01_timeline.md#E0132): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_fbe1b5d_approach.py) · [Exact all-file diff](evidence/diffs/C013_fbe1b5d.diff)

[Previous saved controller snapshot](evidence/versions/C012_8a08dc8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 19aee16..f6dc902 100644
--- a/approach.py
+++ b/approach.py
@@ -62,7 +62,7 @@ class GeneratedApproach:
   62     62              else: self.J[:,self.cal_i]=col; self.cal_sign=-1
   63     63              self.last_delta=0.
   64     64          if self.mode=="calibrate":
   65        -            if self.cal_i>=len(self.controls): self.mode="move"; self.move_count=0
          65 +            if self.cal_i>=3: self.mode="move"; self.move_count=0
   66     66              else:
   67     67                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
   68     68                  self.last_pos=pos; self.last_delta=d; return a
```

</details>

<a id="C014"></a>
### C014 · Add orientation feedback to Cartesian transport

Commit `a53d8a0b7e0a335a93d774a67f37205d6febff00`; parents: fbe1b5d263ae81383fc57680bc8e522fd9fbc695. Recorded author date: 2026-09-09T15:44:09+02:00.

File roles (automatic): policy.

- [E0136](01_timeline.md#E0136): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_a53d8a0_approach.py) · [Exact all-file diff](evidence/diffs/C014_a53d8a0.diff)

[Previous saved controller snapshot](evidence/versions/C013_fbe1b5d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f6dc902..5ef88b8 100644
--- a/approach.py
+++ b/approach.py
@@ -9,11 +9,9 @@ class GeneratedApproach:
    9      9      def reset(self,state,info):
   10     10          self.region=self._xyz(state,"target_region"); self.object_name="target_block"
   11     11          self.mode="pick"; self.pick_i=self.pick_t=0
   12        -        # Virtual controls: lateral base, and two planar motions that preserve
   13        -        # q2+q4+q6 (therefore preserving the block's upright orientation).
   14        -        self.B=np.zeros((11,3)); self.B[1,0]=1.; self.B[4,1]=1.; self.B[8,1]=-1.
   15        -        self.B[6,2]=1.; self.B[8,2]=-1.
   16        -        self.J=np.zeros((3,3)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
          12 +        self.B=np.zeros((11,4)); self.B[1,0]=1.; self.B[4,1]=1.
          13 +        self.B[6,2]=1.; self.B[8,3]=1.
          14 +        self.J=np.zeros((6,4)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
   17     15          self.last_delta=0.; self.move_count=0; self.waypoint=0
   18     16          x=self._v(state,self.object_name,"pose_x")
   19     17          if x<.23: base=(.18,-2.50,-.75)
@@ -30,9 +28,12 @@ class GeneratedApproach:
   30     28          self.lower_t=0
   31     29          self.release_t=0
   32     30      def _held(self,s): return self._v(s,"robot","grasp_active")>.5
          31 +    def _feat(self,s):
          32 +        o=self.object_name
          33 +        return np.r_[self._xyz(s,o), .18*np.array([self._v(s,o,"pose_q"+c) for c in "xyz"])]
   33     34      def _start_calibration(self,s):
   34     35          self.mode="calibrate"; self.cal_i=0; self.cal_sign=1
   35        -        self.last_pos=self._xyz(s,self.object_name); self.last_delta=0.
          36 +        self.last_pos=self._feat(s); self.last_delta=0.
   36     37      def get_action(self,state):
   37     38          a=np.zeros(self.action_space.shape,dtype=self.action_space.dtype)
   38     39          if self._held(state) and self.mode=="pick": self._start_calibration(state)
@@ -46,7 +47,7 @@ class GeneratedApproach:
   46     47              if self.pick_t>=12:
   47     48                  self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
   48     49              return a
   49        -        pos=self._xyz(state,self.object_name)
          50 +        pos=self._xyz(state,self.object_name); feat=self._feat(state)
   50     51          if self.mode=="lower":
   51     52              q2,q4,q6=self.lower_pose; target=np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2])
   52     53              rob=state.get_object_from_name("robot")
@@ -56,20 +57,22 @@ class GeneratedApproach:
   56     57              if self.lower_t>=15: self.mode="release"; self.release_t=0
   57     58              return a
   58     59          if self.mode=="calibrate" and self.last_delta:
   59        -            col=(pos-self.last_pos)/self.last_delta
          60 +            col=(feat-self.last_pos)/self.last_delta
   60     61              if self.cal_sign<0:
   61     62                  self.J[:,self.cal_i]=.5*(self.J[:,self.cal_i]+col); self.cal_i+=1; self.cal_sign=1
   62     63              else: self.J[:,self.cal_i]=col; self.cal_sign=-1
   63     64              self.last_delta=0.
   64     65          if self.mode=="calibrate":
   65        -            if self.cal_i>=3: self.mode="move"; self.move_count=0
          66 +            if self.cal_i>=4: self.mode="move"; self.move_count=0
   66     67              else:
   67     68                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
   68        -                self.last_pos=pos; self.last_delta=d; return a
          69 +                self.last_pos=feat; self.last_delta=d; return a
   69     70          goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
   70     71                 np.array([self.region[0],self.region[1],.115])]
   71        -        goal=goals[self.waypoint]; err=goal-pos; tol=.012 if self.waypoint<2 else .004
   72        -        if np.linalg.norm(err)<tol:
          72 +        goal=goals[self.waypoint]; poserr=goal-pos
          73 +        err=np.r_[poserr, -feat[3:]]
          74 +        tol=.012 if self.waypoint<2 else .004
          75 +        if np.linalg.norm(poserr)<tol and np.linalg.norm(feat[3:])<.025:
   73     76              self.waypoint+=1
   74     77              # Dropping from the clear waypoint avoids wedging the fingers against
   75     78              # the tabletop; gravity preserves the accurately controlled x/y.
@@ -81,8 +84,8 @@ class GeneratedApproach:
   81     84              a[10]=1.
   82     85              self.release_t+=1
   83     86              return a
   84        -        JJ=self.J@self.J.T+1e-5*np.eye(3)
   85        -        u=self.J.T@np.linalg.solve(JJ,np.clip(err,-.06,.06)); u=np.clip(u,-.12,.12)
          87 +        u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(4),self.J.T@np.clip(err,-.06,.06))
          88 +        u=np.clip(u,-.10,.10)
   86     89          a += self.B@u
   87     90          a[10]=-1.; self.move_count+=1
   88     91          if self.move_count>=7: self._start_calibration(state)
```

</details>

<a id="C015"></a>
### C015 · Use backward mobile-base motion in Cartesian transport

Commit `ebc80c8f5e3f277e7281169a745169dccafdc651`; parents: a53d8a0b7e0a335a93d774a67f37205d6febff00. Recorded author date: 2026-09-09T15:45:05+02:00.

File roles (automatic): policy.

- [E0140](01_timeline.md#E0140): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_ebc80c8_approach.py) · [Exact all-file diff](evidence/diffs/C015_ebc80c8.diff)

[Previous saved controller snapshot](evidence/versions/C014_a53d8a0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5ef88b8..93052a9 100644
--- a/approach.py
+++ b/approach.py
@@ -9,9 +9,9 @@ class GeneratedApproach:
    9      9      def reset(self,state,info):
   10     10          self.region=self._xyz(state,"target_region"); self.object_name="target_block"
   11     11          self.mode="pick"; self.pick_i=self.pick_t=0
   12        -        self.B=np.zeros((11,4)); self.B[1,0]=1.; self.B[4,1]=1.
   13        -        self.B[6,2]=1.; self.B[8,3]=1.
   14        -        self.J=np.zeros((6,4)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
          12 +        self.B=np.zeros((11,5)); self.B[0,0]=1.; self.B[1,1]=1.; self.B[4,2]=1.
          13 +        self.B[6,3]=1.; self.B[8,4]=1.
          14 +        self.J=np.zeros((6,5)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
   15     15          self.last_delta=0.; self.move_count=0; self.waypoint=0
   16     16          x=self._v(state,self.object_name,"pose_x")
   17     17          if x<.23: base=(.18,-2.50,-.75)
@@ -63,7 +63,7 @@ class GeneratedApproach:
   63     63              else: self.J[:,self.cal_i]=col; self.cal_sign=-1
   64     64              self.last_delta=0.
   65     65          if self.mode=="calibrate":
   66        -            if self.cal_i>=4: self.mode="move"; self.move_count=0
          66 +            if self.cal_i>=5: self.mode="move"; self.move_count=0
   67     67              else:
   68     68                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
   69     69                  self.last_pos=feat; self.last_delta=d; return a
@@ -84,7 +84,7 @@ class GeneratedApproach:
   84     84              a[10]=1.
   85     85              self.release_t+=1
   86     86              return a
   87        -        u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(4),self.J.T@np.clip(err,-.06,.06))
          87 +        u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(err,-.06,.06))
   88     88          u=np.clip(u,-.10,.10)
   89     89          a += self.B@u
   90     90          a[10]=-1.; self.move_count+=1
```

</details>

<a id="C016"></a>
### C016 · Handle release before waypoint indexing

Commit `a514ca1a90d4e45d145a9fa061c881df72d6672f`; parents: ebc80c8f5e3f277e7281169a745169dccafdc651. Recorded author date: 2026-09-09T15:45:27+02:00.

File roles (automatic): policy.

- [E0144](01_timeline.md#E0144): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_a514ca1_approach.py) · [Exact all-file diff](evidence/diffs/C016_a514ca1.diff)

[Previous saved controller snapshot](evidence/versions/C015_ebc80c8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 93052a9..e47f188 100644
--- a/approach.py
+++ b/approach.py
@@ -67,6 +67,8 @@ class GeneratedApproach:
   67     67              else:
   68     68                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
   69     69                  self.last_pos=feat; self.last_delta=d; return a
          70 +        if self.mode=="release":
          71 +            a[10]=1.; self.release_t+=1; return a
   70     72          goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
   71     73                 np.array([self.region[0],self.region[1],.115])]
   72     74          goal=goals[self.waypoint]; poserr=goal-pos
@@ -79,11 +81,6 @@ class GeneratedApproach:
   79     81              if self.waypoint>=3: self.mode="release"; self.release_t=0
   80     82              else: self._start_calibration(state)
   81     83              a[10]=-1.; return a
   82        -        if self.mode=="release":
   83        -            # Open, then retract the hand so contact cannot keep the grasp latched.
   84        -            a[10]=1.
   85        -            self.release_t+=1
   86        -            return a
   87     84          u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(err,-.06,.06))
   88     85          u=np.clip(u,-.10,.10)
   89     86          a += self.B@u
```

</details>

<a id="C017"></a>
### C017 · Bring block into support contact before release

Commit `450886c47d3964f9b062dce6d244b52157406c38`; parents: a514ca1a90d4e45d145a9fa061c881df72d6672f. Recorded author date: 2026-09-09T15:45:46+02:00.

File roles (automatic): policy.

- [E0148](01_timeline.md#E0148): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_450886c_approach.py) · [Exact all-file diff](evidence/diffs/C017_450886c.diff)

[Previous saved controller snapshot](evidence/versions/C016_a514ca1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e47f188..84f0bf2 100644
--- a/approach.py
+++ b/approach.py
@@ -70,7 +70,7 @@ class GeneratedApproach:
   70     70          if self.mode=="release":
   71     71              a[10]=1.; self.release_t+=1; return a
   72     72          goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
   73        -               np.array([self.region[0],self.region[1],.115])]
          73 +               np.array([self.region[0],self.region[1],.108])]
   74     74          goal=goals[self.waypoint]; poserr=goal-pos
   75     75          err=np.r_[poserr, -feat[3:]]
   76     76          tol=.012 if self.waypoint<2 else .004
```

</details>

<a id="C018"></a>
### C018 · Push gently into support while opening gripper

Commit `053d040fe0a758215025046a1bfc5f9585056e9f`; parents: 450886c47d3964f9b062dce6d244b52157406c38. Recorded author date: 2026-09-09T15:46:30+02:00.

File roles (automatic): policy.

- [E0152](01_timeline.md#E0152): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_053d040_approach.py) · [Exact all-file diff](evidence/diffs/C018_053d040.diff)

[Previous saved controller snapshot](evidence/versions/C017_450886c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 84f0bf2..3ef4b4a 100644
--- a/approach.py
+++ b/approach.py
@@ -68,13 +68,21 @@ class GeneratedApproach:
   68     68                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
   69     69                  self.last_pos=feat; self.last_delta=d; return a
   70     70          if self.mode=="release":
          71 +            if self.release_t<12:
          72 +                g=np.array([self.region[0],self.region[1],.105])
          73 +                er=np.r_[g-pos,-feat[3:]]
          74 +                u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
          75 +                a += self.B@np.clip(u,-.035,.035)
   71     76              a[10]=1.; self.release_t+=1; return a
   72     77          goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
   73        -               np.array([self.region[0],self.region[1],.108])]
          78 +               np.array([self.region[0],self.region[1],.110])]
   74     79          goal=goals[self.waypoint]; poserr=goal-pos
   75     80          err=np.r_[poserr, -feat[3:]]
   76     81          tol=.012 if self.waypoint<2 else .004
   77        -        if np.linalg.norm(poserr)<tol and np.linalg.norm(feat[3:])<.025:
          82 +        arrived=(np.linalg.norm(poserr)<tol)
          83 +        if self.waypoint==2:
          84 +            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<.117)
          85 +        if arrived and np.linalg.norm(feat[3:])<.025:
   78     86              self.waypoint+=1
   79     87              # Dropping from the clear waypoint avoids wedging the fingers against
   80     88              # the tabletop; gravity preserves the accurately controlled x/y.
```

</details>

<a id="C019"></a>
### C019 · Align above region before contact push

Commit `4353e5d2a6405c7e9763d7067e14a0de2bd4562c`; parents: 053d040fe0a758215025046a1bfc5f9585056e9f. Recorded author date: 2026-09-09T15:47:04+02:00.

File roles (automatic): policy.

- [E0156](01_timeline.md#E0156): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_4353e5d_approach.py) · [Exact all-file diff](evidence/diffs/C019_4353e5d.diff)

[Previous saved controller snapshot](evidence/versions/C018_053d040_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3ef4b4a..efe7f22 100644
--- a/approach.py
+++ b/approach.py
@@ -75,7 +75,7 @@ class GeneratedApproach:
   75     75                  a += self.B@np.clip(u,-.035,.035)
   76     76              a[10]=1.; self.release_t+=1; return a
   77     77          goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
   78        -               np.array([self.region[0],self.region[1],.110])]
          78 +               np.array([self.region[0],self.region[1],.115])]
   79     79          goal=goals[self.waypoint]; poserr=goal-pos
   80     80          err=np.r_[poserr, -feat[3:]]
   81     81          tol=.012 if self.waypoint<2 else .004
```

</details>

<a id="C020"></a>
### C020 · Clear overlapping obstructions before placing target

Commit `ed4f6af71cb03ccf59baff16fb9ef4f344ad6ea9`; parents: 4353e5d2a6405c7e9763d7067e14a0de2bd4562c. Recorded author date: 2026-09-09T15:51:49+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0170](01_timeline.md#E0170): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_ed4f6af_approach.py) · [Exact all-file diff](evidence/diffs/C020_ed4f6af.diff)

[Previous saved controller snapshot](evidence/versions/C019_4353e5d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index efe7f22..b4e43c2 100644
--- a/approach.py
+++ b/approach.py
@@ -13,20 +13,29 @@ class GeneratedApproach:
   13     13          self.B[6,3]=1.; self.B[8,4]=1.
   14     14          self.J=np.zeros((6,5)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
   15     15          self.last_delta=0.; self.move_count=0; self.waypoint=0
   16        -        x=self._v(state,self.object_name,"pose_x")
          16 +        rx,ry,_=self.region; rhx=self._v(state,"target_region","half_extent_x"); rhy=self._v(state,"target_region","half_extent_y")
          17 +        blockers=[]
          18 +        for n in state.get_object_names():
          19 +            if not n.startswith("obstruction"): continue
          20 +            x,y,_=self._xyz(state,n); hx=self._v(state,n,"half_extent_x"); hy=self._v(state,n,"half_extent_y")
          21 +            if abs(x-rx)<hx+rhx and abs(y-ry)<hy+rhy: blockers.append(n)
          22 +        blockers.sort()
          23 +        self.tasks=blockers+["target_block"]; self.task_i=0
          24 +        self._setup(state,self.tasks[0])
          25 +
          26 +    def _setup(self,state,name):
          27 +        self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
          28 +        self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
          29 +        x=self._v(state,name,"pose_x")
   17     30          if x<.23: base=(.18,-2.50,-.75)
   18     31          else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
   19     32          self.pick_poses=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
   20        -                         (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10)]
   21        -        rx=self.region[0]
   22        -        if rx<.23: self.lower_pose=(.18,-2.50,-.75)
   23        -        else: self.lower_pose=(.35+2*(rx-.336),-2.20+1.5*(rx-.336),-.60+.8*(rx-.336))
   24        -        # With an object in the fingers the nominal pickup pose leaves its bottom
   25        -        # about 2 cm high; this coupled correction lowers without shifting x.
   26        -        self.lower_pose=(self.lower_pose[0]+.10,self.lower_pose[1]-.027,
   27        -                         self.lower_pose[2]+.10)
   28        -        self.lower_t=0
   29        -        self.release_t=0
          33 +                         (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
          34 +                         (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
          35 +        if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
          36 +        else:
          37 +            k=self.task_i; self.dest=np.array([.16+.07*(k%4), -.36 if k%2==0 else .36])
          38 +            self.rest_z=.075+self._v(state,name,"half_extent_z")
   30     39      def _held(self,s): return self._v(s,"robot","grasp_active")>.5
   31     40      def _feat(self,s):
   32     41          o=self.object_name
@@ -36,6 +45,10 @@ class GeneratedApproach:
   36     45          self.last_pos=self._feat(s); self.last_delta=0.
   37     46      def get_action(self,state):
   38     47          a=np.zeros(self.action_space.shape,dtype=self.action_space.dtype)
          48 +        if self.mode=="release" and not self._held(state):
          49 +            self.task_i+=1
          50 +            if self.task_i<len(self.tasks): self._setup(state,self.tasks[self.task_i])
          51 +            else: return a
   39     52          if self._held(state) and self.mode=="pick": self._start_calibration(state)
   40     53          if self.mode=="pick":
   41     54              x,y,z=self._xyz(state,self.object_name); q2,q4,q6=self.pick_poses[self.pick_i]
@@ -48,14 +61,6 @@ class GeneratedApproach:
   48     61                  self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
   49     62              return a
   50     63          pos=self._xyz(state,self.object_name); feat=self._feat(state)
   51        -        if self.mode=="lower":
   52        -            q2,q4,q6=self.lower_pose; target=np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2])
   53        -            rob=state.get_object_from_name("robot")
   54        -            cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
   55        -            a[1]=np.clip(self.region[1]-.00135-self._v(state,"robot","pos_base_y"),-.12,.12)
   56        -            a[3:10]=np.clip(target-cur,-.10,.10); a[10]=-1.; self.lower_t+=1
   57        -            if self.lower_t>=15: self.mode="release"; self.release_t=0
   58        -            return a
   59     64          if self.mode=="calibrate" and self.last_delta:
   60     65              col=(feat-self.last_pos)/self.last_delta
   61     66              if self.cal_sign<0:
@@ -69,19 +74,19 @@ class GeneratedApproach:
   69     74                  self.last_pos=feat; self.last_delta=d; return a
   70     75          if self.mode=="release":
   71     76              if self.release_t<12:
   72        -                g=np.array([self.region[0],self.region[1],.105])
          77 +                g=np.array([self.dest[0],self.dest[1],self.rest_z-.005])
   73     78                  er=np.r_[g-pos,-feat[3:]]
   74     79                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
   75     80                  a += self.B@np.clip(u,-.035,.035)
   76     81              a[10]=1.; self.release_t+=1; return a
   77        -        goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
   78        -               np.array([self.region[0],self.region[1],.115])]
          82 +        goals=[np.array([pos[0],pos[1],.24]),np.array([self.dest[0],self.dest[1],.24]),
          83 +               np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
   79     84          goal=goals[self.waypoint]; poserr=goal-pos
   80     85          err=np.r_[poserr, -feat[3:]]
   81     86          tol=.012 if self.waypoint<2 else .004
   82     87          arrived=(np.linalg.norm(poserr)<tol)
   83     88          if self.waypoint==2:
   84        -            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<.117)
          89 +            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
   85     90          if arrived and np.linalg.norm(feat[3:])<.025:
   86     91              self.waypoint+=1
   87     92              # Dropping from the clear waypoint avoids wedging the fingers against
diff --git a/test_many.py b/test_many.py
new file mode 100644
index 0000000..434c107
--- /dev/null
+++ b/test_many.py
@@ -0,0 +1,11 @@
           1 +import concurrent.futures
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +def run(seed,count=0):
           5 + e=make_env();s,i=e.reset(seed=seed,options={'object_count':count});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
           6 + for t in range(350):
           7 +  s,_,d,tr,_=e.step(p.get_action(s))
           8 +  if d or tr:break
           9 + e.close();return seed,t+1,d,p.mode
          10 +with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
          11 + for x in ex.map(run,range(20)):print(x,flush=True)
```

</details>

<a id="C021"></a>
### C021 · Add folded-arm grasp family for small obstructions

Commit `9fb91c91e4b7405dc80fc5de0667ef9e22b2c26e`; parents: ed4f6af71cb03ccf59baff16fb9ef4f344ad6ea9. Recorded author date: 2026-09-09T15:55:42+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0178](01_timeline.md#E0178): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_9fb91c9_approach.py) · [Exact all-file diff](evidence/diffs/C021_9fb91c9.diff)

[Previous saved controller snapshot](evidence/versions/C020_ed4f6af_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b4e43c2..5cf6406 100644
--- a/approach.py
+++ b/approach.py
@@ -29,9 +29,18 @@ class GeneratedApproach:
   29     29          x=self._v(state,name,"pose_x")
   30     30          if x<.23: base=(.18,-2.50,-.75)
   31     31          else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
   32        -        self.pick_poses=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
   33        -                         (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
   34        -                         (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
          32 +        triples=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
          33 +                 (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
          34 +                 (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
          35 +        self.pick_poses=[]
          36 +        for q2,q4,q6 in triples:
          37 +            self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,None))
          38 +        if name!="target_block":
          39 +            # A second, highly folded grasp family reaches the tiny obstructions.
          40 +            q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
          41 +            bx=min(-.12,-.12+x-.219855)
          42 +            for d in [0.,-.12,.12]:
          43 +                qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
   35     44          if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
   36     45          else:
   37     46              k=self.task_i; self.dest=np.array([.16+.07*(k%4), -.36 if k%2==0 else .36])
@@ -51,10 +60,11 @@ class GeneratedApproach:
   51     60              else: return a
   52     61          if self._held(state) and self.mode=="pick": self._start_calibration(state)
   53     62          if self.mode=="pick":
   54        -            x,y,z=self._xyz(state,self.object_name); q2,q4,q6=self.pick_poses[self.pick_i]
   55        -            target=np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]); rob=state.get_object_from_name("robot")
          63 +            x,y,z=self._xyz(state,self.object_name); target,yoff,bx=self.pick_poses[self.pick_i]
          64 +            rob=state.get_object_from_name("robot")
   56     65              cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
   57        -            a[1]=np.clip(y-.00135-self._v(state,"robot","pos_base_y"),-.2,.2)
          66 +            a[1]=np.clip(y-yoff-self._v(state,"robot","pos_base_y"),-.2,.2)
          67 +            if bx is not None: a[0]=np.clip(bx-self._v(state,"robot","pos_base_x"),-.2,.2)
   58     68              a[3:10]=np.clip(target-cur,-.2,.2); a[10]=1. if self.pick_t<7 else -1.
   59     69              self.pick_t+=1
   60     70              if self.pick_t>=12:
diff --git a/scan_obstacle.py b/scan_obstacle.py
new file mode 100644
index 0000000..b6177ad
--- /dev/null
+++ b/scan_obstacle.py
@@ -0,0 +1,15 @@
           1 +import concurrent.futures,itertools,numpy as np
           2 +from env_client import make_env
           3 +def v(s,n,f):return s.get(s.get_object_from_name(n),f)
           4 +def trial(c):
           5 + e=make_env();s,_=e.reset(seed=0);name='obstruction0';tar=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2]);y=v(s,name,'pose_y')
           6 + for t in range(12):
           7 +  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
           8 +  a[1]=np.clip(y-.00135-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2);a[10]=1 if t<7 else -1
           9 +  s,*_=e.step(a)
          10 +  if v(s,'robot','grasp_active')>.5:e.close();return c,True
          11 + e.close();return c,False
          12 +cs=list(itertools.product([.05,.12,.19,.26,.33],[-2.55,-2.4,-2.25,-2.1],[-1.05,-.85,-.65,-.45]))
          13 +with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
          14 + for c,o in ex.map(trial,cs):
          15 +  if o:print('SUCCESS',c,flush=True)
```

</details>

<a id="C022"></a>
### C022 · Broaden close-range pickup search

Commit `e4f189bd9b04e002176ee6497423e368df03b16b`; parents: 9fb91c91e4b7405dc80fc5de0667ef9e22b2c26e. Recorded author date: 2026-09-09T15:57:32+02:00.

File roles (automatic): policy.

- [E0184](01_timeline.md#E0184): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_e4f189b_approach.py) · [Exact all-file diff](evidence/diffs/C022_e4f189b.diff)

[Previous saved controller snapshot](evidence/versions/C021_9fb91c9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5cf6406..60a06a9 100644
--- a/approach.py
+++ b/approach.py
@@ -32,6 +32,10 @@ class GeneratedApproach:
   32     32          triples=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
   33     33                   (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
   34     34                   (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
          35 +        if x<.23:
          36 +            for q2 in (.10,.20,.30,.40):
          37 +                for q4 in (-2.50,-2.35,-2.20):
          38 +                    for q6 in (-.90,-.75,-.60): triples.append((q2,q4,q6))
   35     39          self.pick_poses=[]
   36     40          for q2,q4,q6 in triples:
   37     41              self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,None))
```

</details>

<a id="C023"></a>
### C023 · Clear taller accessible obstructions first

Commit `5a4aa86957fdcc0b87511929bf1322346fd9fe0b`; parents: e4f189bd9b04e002176ee6497423e368df03b16b. Recorded author date: 2026-09-09T15:57:53+02:00.

File roles (automatic): policy.

- [E0188](01_timeline.md#E0188): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C023_5a4aa86_approach.py) · [Exact all-file diff](evidence/diffs/C023_5a4aa86.diff)

[Previous saved controller snapshot](evidence/versions/C022_e4f189b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 60a06a9..afddff0 100644
--- a/approach.py
+++ b/approach.py
@@ -19,7 +19,7 @@ class GeneratedApproach:
   19     19              if not n.startswith("obstruction"): continue
   20     20              x,y,_=self._xyz(state,n); hx=self._v(state,n,"half_extent_x"); hy=self._v(state,n,"half_extent_y")
   21     21              if abs(x-rx)<hx+rhx and abs(y-ry)<hy+rhy: blockers.append(n)
   22        -        blockers.sort()
          22 +        blockers.sort(key=lambda n:self._v(state,n,"pose_z")+self._v(state,n,"half_extent_z"),reverse=True)
   23     23          self.tasks=blockers+["target_block"]; self.task_i=0
   24     24          self._setup(state,self.tasks[0])
   25     25  
```

</details>

<a id="C024"></a>
### C024 · Reject accidental grasps of non-target objects

Commit `34b761aa992f618019661e8bead624ae6f394004`; parents: 5a4aa86957fdcc0b87511929bf1322346fd9fe0b. Recorded author date: 2026-09-09T15:58:30+02:00.

File roles (automatic): policy.

- [E0192](01_timeline.md#E0192): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C024_34b761a_approach.py) · [Exact all-file diff](evidence/diffs/C024_34b761a.diff)

[Previous saved controller snapshot](evidence/versions/C023_5a4aa86_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index afddff0..dfb5e1f 100644
--- a/approach.py
+++ b/approach.py
@@ -49,7 +49,7 @@ class GeneratedApproach:
   49     49          else:
   50     50              k=self.task_i; self.dest=np.array([.16+.07*(k%4), -.36 if k%2==0 else .36])
   51     51              self.rest_z=.075+self._v(state,name,"half_extent_z")
   52        -    def _held(self,s): return self._v(s,"robot","grasp_active")>.5
          52 +    def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   53     53      def _feat(self,s):
   54     54          o=self.object_name
   55     55          return np.r_[self._xyz(s,o), .18*np.array([self._v(s,o,"pose_q"+c) for c in "xyz"])]
@@ -58,6 +58,8 @@ class GeneratedApproach:
   58     58          self.last_pos=self._feat(s); self.last_delta=0.
   59     59      def get_action(self,state):
   60     60          a=np.zeros(self.action_space.shape,dtype=self.action_space.dtype)
          61 +        if self.mode=="pick" and self._v(state,"robot","grasp_active")>.5 and not self._held(state):
          62 +            a[10]=1.; self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); return a
   61     63          if self.mode=="release" and not self._held(state):
   62     64              self.task_i+=1
   63     65              if self.task_i<len(self.tasks): self._setup(state,self.tasks[self.task_i])
```

</details>

<a id="C025"></a>
### C025 · Sustain release push until support contact

Commit `8461ed94202e58abd9f5baf6128d01b8aa0fb2c8`; parents: 34b761aa992f618019661e8bead624ae6f394004. Recorded author date: 2026-09-09T15:59:19+02:00.

File roles (automatic): policy.

- [E0198](01_timeline.md#E0198): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_8461ed9_approach.py) · [Exact all-file diff](evidence/diffs/C025_8461ed9.diff)

[Previous saved controller snapshot](evidence/versions/C024_34b761a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index dfb5e1f..1b94f4f 100644
--- a/approach.py
+++ b/approach.py
@@ -89,11 +89,11 @@ class GeneratedApproach:
   89     89                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
   90     90                  self.last_pos=feat; self.last_delta=d; return a
   91     91          if self.mode=="release":
   92        -            if self.release_t<12:
          92 +            if self.release_t<60:
   93     93                  g=np.array([self.dest[0],self.dest[1],self.rest_z-.005])
   94     94                  er=np.r_[g-pos,-feat[3:]]
   95     95                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
   96        -                a += self.B@np.clip(u,-.035,.035)
          96 +                a += self.B@np.clip(u,-.05,.05)
   97     97              a[10]=1.; self.release_t+=1; return a
   98     98          goals=[np.array([pos[0],pos[1],.24]),np.array([self.dest[0],self.dest[1],.24]),
   99     99                 np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
```

</details>

<a id="C026"></a>
### C026 · Prefer a higher target grasp to preserve finger clearance

Commit `65422b5c2639babe70139e17ab946b2021aabe8a`; parents: 8461ed94202e58abd9f5baf6128d01b8aa0fb2c8. Recorded author date: 2026-09-09T16:01:13+02:00.

File roles (automatic): policy.

- [E0208](01_timeline.md#E0208): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C026_65422b5_approach.py) · [Exact all-file diff](evidence/diffs/C026_65422b5.diff)

[Previous saved controller snapshot](evidence/versions/C025_8461ed9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1b94f4f..9b2cd70 100644
--- a/approach.py
+++ b/approach.py
@@ -29,7 +29,7 @@ class GeneratedApproach:
   29     29          x=self._v(state,name,"pose_x")
   30     30          if x<.23: base=(.18,-2.50,-.75)
   31     31          else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
   32        -        triples=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
          32 +        triples=[(base[0]-.10,base[1],base[2]),base,(base[0]+.08,base[1],base[2]),
   33     33                   (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
   34     34                   (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
   35     35          if x<.23:
```

</details>

<a id="C027"></a>
### C027 · Orient fingers along narrow target-region axis

Commit `9cdd2881f7bf0114386336622c9791b57f1465f2`; parents: 65422b5c2639babe70139e17ab946b2021aabe8a. Recorded author date: 2026-09-09T16:03:20+02:00.

File roles (automatic): policy.

- [E0216](01_timeline.md#E0216): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C027_9cdd288_approach.py) · [Exact all-file diff](evidence/diffs/C027_9cdd288.diff)

[Previous saved controller snapshot](evidence/versions/C026_65422b5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9b2cd70..daacd31 100644
--- a/approach.py
+++ b/approach.py
@@ -14,6 +14,7 @@ class GeneratedApproach:
   14     14          self.J=np.zeros((6,5)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
   15     15          self.last_delta=0.; self.move_count=0; self.waypoint=0
   16     16          rx,ry,_=self.region; rhx=self._v(state,"target_region","half_extent_x"); rhy=self._v(state,"target_region","half_extent_y")
          17 +        self.region_hx,self.region_hy=rhx,rhy
   17     18          blockers=[]
   18     19          for n in state.get_object_names():
   19     20              if not n.startswith("obstruction"): continue
@@ -39,6 +40,8 @@ class GeneratedApproach:
   39     40          self.pick_poses=[]
   40     41          for q2,q4,q6 in triples:
   41     42              self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,None))
          43 +        if name=="target_block" and self.region_hx>self.region_hy:
          44 +            for item in self.pick_poses: item[0][6]+=np.pi/2
   42     45          if name!="target_block":
   43     46              # A second, highly folded grasp family reaches the tiny obstructions.
   44     47              q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
```

</details>

<a id="C028"></a>
### C028 · Restore reliable target grasp orientation

Commit `a2ea09b4ead6338919499f3df91b1a185daaa45b`; parents: 9cdd2881f7bf0114386336622c9791b57f1465f2. Recorded author date: 2026-09-09T16:03:46+02:00.

File roles (automatic): policy.

- [E0220](01_timeline.md#E0220): commit hash in recorded output.
[Controller after this commit](evidence/versions/C028_a2ea09b_approach.py) · [Exact all-file diff](evidence/diffs/C028_a2ea09b.diff)

[Previous saved controller snapshot](evidence/versions/C027_9cdd288_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index daacd31..47cc3e0 100644
--- a/approach.py
+++ b/approach.py
@@ -40,8 +40,6 @@ class GeneratedApproach:
   40     40          self.pick_poses=[]
   41     41          for q2,q4,q6 in triples:
   42     42              self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,None))
   43        -        if name=="target_block" and self.region_hx>self.region_hy:
   44        -            for item in self.pick_poses: item[0][6]+=np.pi/2
   45     43          if name!="target_block":
   46     44              # A second, highly folded grasp family reaches the tiny obstructions.
   47     45              q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
```

</details>

<a id="C029"></a>
### C029 · Reserve forward base travel for distant placements

Commit `c4098f65b8e60352d8917e9c169cf8a3f7c41a25`; parents: a2ea09b4ead6338919499f3df91b1a185daaa45b. Recorded author date: 2026-09-09T16:05:59+02:00.

File roles (automatic): policy.

- [E0226](01_timeline.md#E0226): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C029_c4098f6_approach.py) · [Exact all-file diff](evidence/diffs/C029_c4098f6.diff)

[Previous saved controller snapshot](evidence/versions/C028_a2ea09b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 47cc3e0..c534514 100644
--- a/approach.py
+++ b/approach.py
@@ -27,7 +27,7 @@ class GeneratedApproach:
   27     27      def _setup(self,state,name):
   28     28          self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
   29     29          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
   30        -        x=self._v(state,name,"pose_x")
          30 +        x=self._v(state,name,"pose_x"); self.start_x=x
   31     31          if x<.23: base=(.18,-2.50,-.75)
   32     32          else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
   33     33          triples=[(base[0]-.10,base[1],base[2]),base,(base[0]+.08,base[1],base[2]),
@@ -61,6 +61,8 @@ class GeneratedApproach:
   61     61          a=np.zeros(self.action_space.shape,dtype=self.action_space.dtype)
   62     62          if self.mode=="pick" and self._v(state,"robot","grasp_active")>.5 and not self._held(state):
   63     63              a[10]=1.; self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); return a
          64 +        if self.mode=="reserve":
          65 +            a[0]=-.20; a[10]=-1.; self._start_calibration(state); return a
   64     66          if self.mode=="release" and not self._held(state):
   65     67              self.task_i+=1
   66     68              if self.task_i<len(self.tasks): self._setup(state,self.tasks[self.task_i])
@@ -109,6 +111,7 @@ class GeneratedApproach:
  109    111              # Dropping from the clear waypoint avoids wedging the fingers against
  110    112              # the tabletop; gravity preserves the accurately controlled x/y.
  111    113              if self.waypoint>=3: self.mode="release"; self.release_t=0
         114 +            elif self.waypoint==1 and self.dest[0]>self.start_x+.03: self.mode="reserve"
  112    115              else: self._start_calibration(state)
  113    116              a[10]=-1.; return a
  114    117          u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(err,-.06,.06))
```

</details>

<a id="C030"></a>
### C030 · Use rotated long-settle grasp for wide target regions

Commit `9789cc63ddd6839d1b8688b00b314147bce837f3`; parents: c4098f65b8e60352d8917e9c169cf8a3f7c41a25. Recorded author date: 2026-09-09T16:08:51+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0236](01_timeline.md#E0236): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C030_9789cc6_approach.py) · [Exact all-file diff](evidence/diffs/C030_9789cc6.diff)

[Previous saved controller snapshot](evidence/versions/C029_c4098f6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c534514..fedc5c4 100644
--- a/approach.py
+++ b/approach.py
@@ -40,6 +40,8 @@ class GeneratedApproach:
   40     40          self.pick_poses=[]
   41     41          for q2,q4,q6 in triples:
   42     42              self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,None))
          43 +        if name=="target_block" and self.region_hx>.027:
          44 +            for item in self.pick_poses: item[0][6]+=np.pi/2
   43     45          if name!="target_block":
   44     46              # A second, highly folded grasp family reaches the tiny obstructions.
   45     47              q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
@@ -74,9 +76,9 @@ class GeneratedApproach:
   74     76              cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
   75     77              a[1]=np.clip(y-yoff-self._v(state,"robot","pos_base_y"),-.2,.2)
   76     78              if bx is not None: a[0]=np.clip(bx-self._v(state,"robot","pos_base_x"),-.2,.2)
   77        -            a[3:10]=np.clip(target-cur,-.2,.2); a[10]=1. if self.pick_t<7 else -1.
          79 +            a[3:10]=np.clip(target-cur,-.2,.2); a[10]=1. if self.pick_t<14 else -1.
   78     80              self.pick_t+=1
   79        -            if self.pick_t>=12:
          81 +            if self.pick_t>=20:
   80     82                  self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
   81     83              return a
   82     84          pos=self._xyz(state,self.object_name); feat=self._feat(state)
diff --git a/scan_rotated_pick.py b/scan_rotated_pick.py
new file mode 100644
index 0000000..df963ae
--- /dev/null
+++ b/scan_rotated_pick.py
@@ -0,0 +1,13 @@
           1 +import concurrent.futures,numpy as np
           2 +from env_client import make_env
           3 +def v(s,n,f):return s.get(s.get_object_from_name(n),f)
           4 +def run(off):
           5 + e=make_env();s,_=e.reset(seed=0,options={'object_count':0});x=v(s,'target_block','pose_x');y=v(s,'target_block','pose_y')
           6 + tar=np.array([0,.25,-np.pi,-2.2,0,-.6,np.pi])
           7 + for t in range(15):
           8 +  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
           9 +  a[1]=np.clip(y+off-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
          10 +  if v(s,'target_block','grasp_active')>.5:e.close();return off,True
          11 + e.close();return off,False
          12 +with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex:
          13 + print(list(ex.map(run,np.linspace(-.08,.08,9))))
```

</details>

<a id="C031"></a>
### C031 · Keep obstruction pickup search within episode budget

Commit `2039c44027e96ccf62ad9ec17edf5629ed07bd0f`; parents: 9789cc63ddd6839d1b8688b00b314147bce837f3. Recorded author date: 2026-09-09T16:09:17+02:00.

File roles (automatic): policy.

- [E0240](01_timeline.md#E0240): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C031_2039c44_approach.py) · [Exact all-file diff](evidence/diffs/C031_2039c44.diff)

[Previous saved controller snapshot](evidence/versions/C030_9789cc6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fedc5c4..ee7eda0 100644
--- a/approach.py
+++ b/approach.py
@@ -26,6 +26,7 @@ class GeneratedApproach:
   26     26  
   27     27      def _setup(self,state,name):
   28     28          self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
          29 +        self.pick_period=20 if name=="target_block" else 12
   29     30          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
   30     31          x=self._v(state,name,"pose_x"); self.start_x=x
   31     32          if x<.23: base=(.18,-2.50,-.75)
@@ -76,9 +77,9 @@ class GeneratedApproach:
   76     77              cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
   77     78              a[1]=np.clip(y-yoff-self._v(state,"robot","pos_base_y"),-.2,.2)
   78     79              if bx is not None: a[0]=np.clip(bx-self._v(state,"robot","pos_base_x"),-.2,.2)
   79        -            a[3:10]=np.clip(target-cur,-.2,.2); a[10]=1. if self.pick_t<14 else -1.
          80 +            a[3:10]=np.clip(target-cur,-.2,.2); a[10]=1. if self.pick_t<self.pick_period-6 else -1.
   80     81              self.pick_t+=1
   81        -            if self.pick_t>=20:
          82 +            if self.pick_t>=self.pick_period:
   82     83                  self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
   83     84              return a
   84     85          pos=self._xyz(state,self.object_name); feat=self._feat(state)
```

</details>

<a id="C032"></a>
### C032 · Favor reliable upright pickup over wedging-prone rotated grasp

Commit `9d7f832cb991a794ce44753e0cd4553da691cd1a`; parents: 2039c44027e96ccf62ad9ec17edf5629ed07bd0f. Recorded author date: 2026-09-09T16:09:44+02:00.

File roles (automatic): policy.

- [E0244](01_timeline.md#E0244): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C032_9d7f832_approach.py) · [Exact all-file diff](evidence/diffs/C032_9d7f832.diff)

[Previous saved controller snapshot](evidence/versions/C031_2039c44_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ee7eda0..7a126e8 100644
--- a/approach.py
+++ b/approach.py
@@ -26,7 +26,7 @@ class GeneratedApproach:
   26     26  
   27     27      def _setup(self,state,name):
   28     28          self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
   29        -        self.pick_period=20 if name=="target_block" else 12
          29 +        self.pick_period=12
   30     30          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
   31     31          x=self._v(state,name,"pose_x"); self.start_x=x
   32     32          if x<.23: base=(.18,-2.50,-.75)
@@ -41,8 +41,6 @@ class GeneratedApproach:
   41     41          self.pick_poses=[]
   42     42          for q2,q4,q6 in triples:
   43     43              self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,None))
   44        -        if name=="target_block" and self.region_hx>.027:
   45        -            for item in self.pick_poses: item[0][6]+=np.pi/2
   46     44          if name!="target_block":
   47     45              # A second, highly folded grasp family reaches the tiny obstructions.
   48     46              q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
```

</details>

<a id="C033"></a>
### C033 · Close only after converging to each pickup pose

Commit `5a9a4bff0a20f1154fb8c19fe6ecee60d9136f80`; parents: 9d7f832cb991a794ce44753e0cd4553da691cd1a. Recorded author date: 2026-09-09T16:11:01+02:00.

File roles (automatic): policy.

- [E0250](01_timeline.md#E0250): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C033_5a9a4bf_approach.py) · [Exact all-file diff](evidence/diffs/C033_5a9a4bf.diff)

[Previous saved controller snapshot](evidence/versions/C032_9d7f832_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7a126e8..b5e85a9 100644
--- a/approach.py
+++ b/approach.py
@@ -26,7 +26,6 @@ class GeneratedApproach:
   26     26  
   27     27      def _setup(self,state,name):
   28     28          self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
   29        -        self.pick_period=12
   30     29          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
   31     30          x=self._v(state,name,"pose_x"); self.start_x=x
   32     31          if x<.23: base=(.18,-2.50,-.75)
@@ -75,9 +74,12 @@ class GeneratedApproach:
   75     74              cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
   76     75              a[1]=np.clip(y-yoff-self._v(state,"robot","pos_base_y"),-.2,.2)
   77     76              if bx is not None: a[0]=np.clip(bx-self._v(state,"robot","pos_base_x"),-.2,.2)
   78        -            a[3:10]=np.clip(target-cur,-.2,.2); a[10]=1. if self.pick_t<self.pick_period-6 else -1.
   79        -            self.pick_t+=1
   80        -            if self.pick_t>=self.pick_period:
          77 +            a[3:10]=np.clip(target-cur,-.2,.2)
          78 +            err=max(np.max(np.abs(target-cur)),abs(y-yoff-self._v(state,"robot","pos_base_y")))
          79 +            if bx is not None: err=max(err,abs(bx-self._v(state,"robot","pos_base_x")))
          80 +            if err<.035: a[10]=-1.; self.pick_t+=1
          81 +            else: a[10]=1.; self.pick_t=0
          82 +            if self.pick_t>=5:
   81     83                  self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
   82     84              return a
   83     85          pos=self._xyz(state,self.object_name); feat=self._feat(state)
```

</details>

<a id="C034"></a>
### C034 · Restore base position before standard pickup

Commit `b8d29f98e0cd0893215b3ca71ea23c8352baf216`; parents: 5a9a4bff0a20f1154fb8c19fe6ecee60d9136f80. Recorded author date: 2026-09-09T16:11:30+02:00.

File roles (automatic): policy.

- [E0254](01_timeline.md#E0254): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C034_b8d29f9_approach.py) · [Exact all-file diff](evidence/diffs/C034_b8d29f9.diff)

[Previous saved controller snapshot](evidence/versions/C033_5a9a4bf_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b5e85a9..58bf545 100644
--- a/approach.py
+++ b/approach.py
@@ -39,7 +39,7 @@ class GeneratedApproach:
   39     39                      for q6 in (-.90,-.75,-.60): triples.append((q2,q4,q6))
   40     40          self.pick_poses=[]
   41     41          for q2,q4,q6 in triples:
   42        -            self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,None))
          42 +            self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,-.12))
   43     43          if name!="target_block":
   44     44              # A second, highly folded grasp family reaches the tiny obstructions.
   45     45              q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
```

</details>

<a id="C035"></a>
### C035 · Retract arm between object transfers

Commit `f888c69e8f588f710ebd81994d39b9aa3b8fb4a4`; parents: b8d29f98e0cd0893215b3ca71ea23c8352baf216. Recorded author date: 2026-09-09T16:13:04+02:00.

File roles (automatic): policy.

- [E0260](01_timeline.md#E0260): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C035_f888c69_approach.py) · [Exact all-file diff](evidence/diffs/C035_f888c69.diff)

[Previous saved controller snapshot](evidence/versions/C034_b8d29f9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 58bf545..281b88b 100644
--- a/approach.py
+++ b/approach.py
@@ -26,6 +26,7 @@ class GeneratedApproach:
   26     26  
   27     27      def _setup(self,state,name):
   28     28          self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
          29 +        self.resetting=self.task_i>0
   29     30          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
   30     31          x=self._v(state,name,"pose_x"); self.start_x=x
   31     32          if x<.23: base=(.18,-2.50,-.75)
@@ -63,6 +64,13 @@ class GeneratedApproach:
   63     64              a[10]=1.; self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); return a
   64     65          if self.mode=="reserve":
   65     66              a[0]=-.20; a[10]=-1.; self._start_calibration(state); return a
          67 +        if self.mode=="pick" and self.resetting:
          68 +            safe=np.array([0.,-.35,-np.pi,-2.50,0.,-.87,np.pi/2])
          69 +            rob=state.get_object_from_name("robot")
          70 +            cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
          71 +            a[3:10]=np.clip(safe-cur,-.2,.2); a[10]=1.
          72 +            if np.max(np.abs(safe-cur))<.03: self.resetting=False
          73 +            return a
   66     74          if self.mode=="release" and not self._held(state):
   67     75              self.task_i+=1
   68     76              if self.task_i<len(self.tasks): self._setup(state,self.tasks[self.task_i])
```

</details>

<a id="C036"></a>
### C036 · Relax off-region obstruction drop positioning

Commit `2ec4ab1be767809b5ec610bab93146091c817cf4`; parents: f888c69e8f588f710ebd81994d39b9aa3b8fb4a4. Recorded author date: 2026-09-09T16:14:14+02:00.

File roles (automatic): policy.

- [E0268](01_timeline.md#E0268): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C036_2ec4ab1_approach.py) · [Exact all-file diff](evidence/diffs/C036_2ec4ab1.diff)

[Previous saved controller snapshot](evidence/versions/C035_f888c69_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 281b88b..9528c35 100644
--- a/approach.py
+++ b/approach.py
@@ -104,7 +104,8 @@ class GeneratedApproach:
  104    104                  self.last_pos=feat; self.last_delta=d; return a
  105    105          if self.mode=="release":
  106    106              if self.release_t<60:
  107        -                g=np.array([self.dest[0],self.dest[1],self.rest_z-.005])
         107 +                gx=self.release_x if self.object_name!="target_block" else self.dest[0]
         108 +                g=np.array([gx,self.dest[1],self.rest_z-.005])
  108    109                  er=np.r_[g-pos,-feat[3:]]
  109    110                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  110    111                  a += self.B@np.clip(u,-.05,.05)
@@ -117,11 +118,13 @@ class GeneratedApproach:
  117    118          arrived=(np.linalg.norm(poserr)<tol)
  118    119          if self.waypoint==2:
  119    120              arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
         121 +            if self.object_name!="target_block":
         122 +                arrived=(abs(poserr[1])<.025 and pos[2]<self.rest_z+.035)
  120    123          if arrived and np.linalg.norm(feat[3:])<.025:
  121    124              self.waypoint+=1
  122    125              # Dropping from the clear waypoint avoids wedging the fingers against
  123    126              # the tabletop; gravity preserves the accurately controlled x/y.
  124        -            if self.waypoint>=3: self.mode="release"; self.release_t=0
         127 +            if self.waypoint>=3: self.mode="release"; self.release_t=0; self.release_x=pos[0]
  125    128              elif self.waypoint==1 and self.dest[0]>self.start_x+.03: self.mode="reserve"
  126    129              else: self._start_calibration(state)
  127    130              a[10]=-1.; return a
```

</details>

<a id="C037"></a>
### C037 · Use target block as raised obstruction staging surface

Commit `3bd39dd955979619383d5c9ca3bb045ae3c12085`; parents: 2ec4ab1be767809b5ec610bab93146091c817cf4. Recorded author date: 2026-09-09T16:14:51+02:00.

File roles (automatic): policy.

- [E0272](01_timeline.md#E0272): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C037_3bd39dd_approach.py) · [Exact all-file diff](evidence/diffs/C037_3bd39dd.diff)

[Previous saved controller snapshot](evidence/versions/C036_2ec4ab1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9528c35..bff4c46 100644
--- a/approach.py
+++ b/approach.py
@@ -49,8 +49,9 @@ class GeneratedApproach:
   49     49                  qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
   50     50          if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
   51     51          else:
   52        -            k=self.task_i; self.dest=np.array([.16+.07*(k%4), -.36 if k%2==0 else .36])
   53        -            self.rest_z=.075+self._v(state,name,"half_extent_z")
          52 +            # The target block is a raised, guaranteed-clear temporary shelf.
          53 +            self.dest=self._xyz(state,"target_block")[:2]
          54 +            self.rest_z=.125+self._v(state,name,"half_extent_z")
   54     55      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   55     56      def _feat(self,s):
   56     57          o=self.object_name
```

</details>

<a id="C038"></a>
### C038 · Restore edge staging for cleared obstructions

Commit `27238e8368e0ac758a3626c0a26669f35f0ce24d`; parents: 3bd39dd955979619383d5c9ca3bb045ae3c12085. Recorded author date: 2026-09-09T16:15:11+02:00.

File roles (automatic): policy.

- [E0276](01_timeline.md#E0276): commit hash in recorded output.
[Controller after this commit](evidence/versions/C038_27238e8_approach.py) · [Exact all-file diff](evidence/diffs/C038_27238e8.diff)

[Previous saved controller snapshot](evidence/versions/C037_3bd39dd_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C036](#C036). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bff4c46..9528c35 100644
--- a/approach.py
+++ b/approach.py
@@ -49,9 +49,8 @@ class GeneratedApproach:
   49     49                  qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
   50     50          if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
   51     51          else:
   52        -            # The target block is a raised, guaranteed-clear temporary shelf.
   53        -            self.dest=self._xyz(state,"target_block")[:2]
   54        -            self.rest_z=.125+self._v(state,name,"half_extent_z")
          52 +            k=self.task_i; self.dest=np.array([.16+.07*(k%4), -.36 if k%2==0 else .36])
          53 +            self.rest_z=.075+self._v(state,name,"half_extent_z")
   55     54      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   56     55      def _feat(self,s):
   57     56          o=self.object_name
```

</details>

<a id="C039"></a>
### C039 · Lift opening fingers to release without surface wedging

Commit `3d29556c4b8c90901fe53d36297c8a8b64fcaa70`; parents: 27238e8368e0ac758a3626c0a26669f35f0ce24d. Recorded author date: 2026-09-09T16:16:30+02:00.

File roles (automatic): policy.

- [E0284](01_timeline.md#E0284): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C039_3d29556_approach.py) · [Exact all-file diff](evidence/diffs/C039_3d29556.diff)

[Previous saved controller snapshot](evidence/versions/C038_27238e8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9528c35..dec98f2 100644
--- a/approach.py
+++ b/approach.py
@@ -103,9 +103,10 @@ class GeneratedApproach:
  103    103                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  104    104                  self.last_pos=feat; self.last_delta=d; return a
  105    105          if self.mode=="release":
  106        -            if self.release_t<60:
  107        -                gx=self.release_x if self.object_name!="target_block" else self.dest[0]
  108        -                g=np.array([gx,self.dest[1],self.rest_z-.005])
         106 +            if self.release_t<30:
         107 +                # Lift the opening fingers away from the support; otherwise their
         108 +                # tips can be pinched between a wide region and the held block.
         109 +                g=np.array([self.release_x,self.dest[1],max(.20,pos[2]+.025)])
  109    110                  er=np.r_[g-pos,-feat[3:]]
  110    111                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  111    112                  a += self.B@np.clip(u,-.05,.05)
```

</details>

<a id="C040"></a>
### C040 · Fall back to timed closure at contact-limited pickup poses

Commit `d717a3080d6b8f7e5d6d72573c26d0c791992f03`; parents: 3d29556c4b8c90901fe53d36297c8a8b64fcaa70. Recorded author date: 2026-09-09T16:17:02+02:00.

File roles (automatic): policy.

- [E0288](01_timeline.md#E0288): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C040_d717a30_approach.py) · [Exact all-file diff](evidence/diffs/C040_d717a30.diff)

[Previous saved controller snapshot](evidence/versions/C039_3d29556_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index dec98f2..aa5b342 100644
--- a/approach.py
+++ b/approach.py
@@ -26,6 +26,7 @@ class GeneratedApproach:
   26     26  
   27     27      def _setup(self,state,name):
   28     28          self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
          29 +        self.approach_t=0
   29     30          self.resetting=self.task_i>0
   30     31          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
   31     32          x=self._v(state,name,"pose_x"); self.start_x=x
@@ -85,10 +86,12 @@ class GeneratedApproach:
   85     86              a[3:10]=np.clip(target-cur,-.2,.2)
   86     87              err=max(np.max(np.abs(target-cur)),abs(y-yoff-self._v(state,"robot","pos_base_y")))
   87     88              if bx is not None: err=max(err,abs(bx-self._v(state,"robot","pos_base_x")))
   88        -            if err<.035: a[10]=-1.; self.pick_t+=1
          89 +            self.approach_t+=1
          90 +            if err<.035 or self.approach_t>=12: a[10]=-1.; self.pick_t+=1
   89     91              else: a[10]=1.; self.pick_t=0
   90        -            if self.pick_t>=5:
          92 +            if self.pick_t>=5 or self.approach_t>=18:
   91     93                  self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
          94 +                self.approach_t=0
   92     95              return a
   93     96          pos=self._xyz(state,self.object_name); feat=self._feat(state)
   94     97          if self.mode=="calibrate" and self.last_delta:
```

</details>

<a id="C041"></a>
### C041 · Seat obstructions while lifting target-release fingers

Commit `d3f57a9c600846386542b0604cd873a5cb6c99f5`; parents: d717a3080d6b8f7e5d6d72573c26d0c791992f03. Recorded author date: 2026-09-09T16:17:27+02:00.

File roles (automatic): policy.

- [E0292](01_timeline.md#E0292): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C041_d3f57a9_approach.py) · [Exact all-file diff](evidence/diffs/C041_d3f57a9.diff)

[Previous saved controller snapshot](evidence/versions/C040_d717a30_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index aa5b342..913b162 100644
--- a/approach.py
+++ b/approach.py
@@ -107,9 +107,10 @@ class GeneratedApproach:
  107    107                  self.last_pos=feat; self.last_delta=d; return a
  108    108          if self.mode=="release":
  109    109              if self.release_t<30:
  110        -                # Lift the opening fingers away from the support; otherwise their
  111        -                # tips can be pinched between a wide region and the held block.
  112        -                g=np.array([self.release_x,self.dest[1],max(.20,pos[2]+.025)])
         110 +                if self.object_name=="target_block":
         111 +                    g=np.array([self.release_x,self.dest[1],max(.20,pos[2]+.025)])
         112 +                else:
         113 +                    g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
  113    114                  er=np.r_[g-pos,-feat[3:]]
  114    115                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  115    116                  a += self.B@np.clip(u,-.05,.05)
```

</details>

<a id="C042"></a>
### C042 · Require precise supported obstruction placement before opening

Commit `4ba933a590795080d445ac7a60c821ac929c7433`; parents: d3f57a9c600846386542b0604cd873a5cb6c99f5. Recorded author date: 2026-09-09T16:17:47+02:00.

File roles (automatic): policy.

- [E0296](01_timeline.md#E0296): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C042_4ba933a_approach.py) · [Exact all-file diff](evidence/diffs/C042_4ba933a.diff)

[Previous saved controller snapshot](evidence/versions/C041_d3f57a9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 913b162..78120fd 100644
--- a/approach.py
+++ b/approach.py
@@ -106,7 +106,8 @@ class GeneratedApproach:
  106    106                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  107    107                  self.last_pos=feat; self.last_delta=d; return a
  108    108          if self.mode=="release":
  109        -            if self.release_t<30:
         109 +            limit=30 if self.object_name=="target_block" else 60
         110 +            if self.release_t<limit:
  110    111                  if self.object_name=="target_block":
  111    112                      g=np.array([self.release_x,self.dest[1],max(.20,pos[2]+.025)])
  112    113                  else:
@@ -123,8 +124,6 @@ class GeneratedApproach:
  123    124          arrived=(np.linalg.norm(poserr)<tol)
  124    125          if self.waypoint==2:
  125    126              arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
  126        -            if self.object_name!="target_block":
  127        -                arrived=(abs(poserr[1])<.025 and pos[2]<self.rest_z+.035)
  128    127          if arrived and np.linalg.norm(feat[3:])<.025:
  129    128              self.waypoint+=1
  130    129              # Dropping from the clear waypoint avoids wedging the fingers against
```

</details>

<a id="C043"></a>
### C043 · Use stable supported release for every object

Commit `eeeee4e05135e85f98c3bf1b9ae5c3215ebe9184`; parents: 4ba933a590795080d445ac7a60c821ac929c7433. Recorded author date: 2026-09-09T16:18:12+02:00.

File roles (automatic): policy.

- [E0300](01_timeline.md#E0300): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C043_eeeee4e_approach.py) · [Exact all-file diff](evidence/diffs/C043_eeeee4e.diff)

[Previous saved controller snapshot](evidence/versions/C042_4ba933a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 78120fd..eead167 100644
--- a/approach.py
+++ b/approach.py
@@ -106,12 +106,8 @@ class GeneratedApproach:
  106    106                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  107    107                  self.last_pos=feat; self.last_delta=d; return a
  108    108          if self.mode=="release":
  109        -            limit=30 if self.object_name=="target_block" else 60
  110        -            if self.release_t<limit:
  111        -                if self.object_name=="target_block":
  112        -                    g=np.array([self.release_x,self.dest[1],max(.20,pos[2]+.025)])
  113        -                else:
  114        -                    g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
         109 +            if self.release_t<60:
         110 +                g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
  115    111                  er=np.r_[g-pos,-feat[3:]]
  116    112                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  117    113                  a += self.B@np.clip(u,-.05,.05)
```

</details>

<a id="C044"></a>
### C044 · Clarify supported-release controller intent

Commit `cc5d12e55ac3e5de8b2101edea8b5082cb4046e6`; parents: eeeee4e05135e85f98c3bf1b9ae5c3215ebe9184. Recorded author date: 2026-09-09T16:18:53+02:00.

File roles (automatic): policy.

- [E0307](01_timeline.md#E0307): commit hash in recorded output.
[Controller after this commit](evidence/versions/C044_cc5d12e_approach.py) · [Exact all-file diff](evidence/diffs/C044_cc5d12e.diff)

[Previous saved controller snapshot](evidence/versions/C043_eeeee4e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index eead167..726c57f 100644
--- a/approach.py
+++ b/approach.py
@@ -122,8 +122,7 @@ class GeneratedApproach:
  122    122              arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
  123    123          if arrived and np.linalg.norm(feat[3:])<.025:
  124    124              self.waypoint+=1
  125        -            # Dropping from the clear waypoint avoids wedging the fingers against
  126        -            # the tabletop; gravity preserves the accurately controlled x/y.
         125 +            # The last waypoint seats the object before opening the fingers.
  127    126              if self.waypoint>=3: self.mode="release"; self.release_t=0; self.release_x=pos[0]
  128    127              elif self.waypoint==1 and self.dest[0]>self.start_x+.03: self.mode="reserve"
  129    128              else: self._start_calibration(state)
```

</details>

<a id="C045"></a>
### C045 · initial sandbox setup

Commit `0d781c93af9840a351b79f09dd7b67faad6ff377`; parents: cc5d12e55ac3e5de8b2101edea8b5082cb4046e6. Recorded author date: 2026-09-09T16:19:07+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C045_0d781c9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 76dfa5b..85d005e 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $20.00. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $12.01. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C046"></a>
### C046 · Relax orientation during high-clearance transport

Commit `555ce1083962455fd6189f980a1e247a40b33b4b`; parents: 0d781c93af9840a351b79f09dd7b67faad6ff377. Recorded author date: 2026-09-09T16:20:29+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0324](01_timeline.md#E0324): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C046_555ce10_approach.py) · [Exact all-file diff](evidence/diffs/C046_555ce10.diff)

[Previous saved controller snapshot](evidence/versions/C044_cc5d12e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 726c57f..40fb667 100644
--- a/approach.py
+++ b/approach.py
@@ -116,6 +116,10 @@ class GeneratedApproach:
  116    116                 np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
  117    117          goal=goals[self.waypoint]; poserr=goal-pos
  118    118          err=np.r_[poserr, -feat[3:]]
         119 +        if self.waypoint==1:
         120 +            # At clearance height, temporarily exploit all redundant arm motion;
         121 +            # upright orientation is restored during the final descent.
         122 +            err[3:]=0.
  119    123          tol=.012 if self.waypoint<2 else .004
  120    124          arrived=(np.linalg.norm(poserr)<tol)
  121    125          if self.waypoint==2:
diff --git a/release_probe_agent.py b/release_probe_agent.py
new file mode 100644
index 0000000..3d0de9e
--- /dev/null
+++ b/release_probe_agent.py
@@ -0,0 +1,33 @@
           1 +"""Focused logging of final target release on deterministic seeds."""
           2 +import sys
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +
           7 +for seed in map(int, sys.argv[1:] or [0, 11]):
           8 +    env = make_env()
           9 +    state, info = env.reset(seed=seed)
          10 +    policy = GeneratedApproach(env.action_space, env.observation_space, {})
          11 +    policy.reset(state, info)
          12 +    prior = None
          13 +    for step in range(env.max_steps):
          14 +        action = policy.get_action(state)
          15 +        mode = policy.mode
          16 +        state, reward, done, trunc, info = env.step(action)
          17 +        if mode == "release" and policy.object_name == "target_block":
          18 +            robot = state.get_object_from_name("robot")
          19 +            block = state.get_object_from_name("target_block")
          20 +            vals = (
          21 +                step, policy.release_t, float(action[10]),
          22 +                state.get(robot, "finger_state"), state.get(robot, "grasp_active"),
          23 +                state.get(block, "grasp_active"), state.get(block, "pose_x"),
          24 +                state.get(block, "pose_y"), state.get(block, "pose_z"),
          25 +            )
          26 +            sig = tuple(round(float(x), 5) for x in vals[3:])
          27 +            if policy.release_t <= 8 or sig != prior or policy.release_t % 10 == 0:
          28 +                print(seed, *[round(float(x), 5) for x in vals])
          29 +            prior = sig
          30 +        if done or trunc:
          31 +            print("RESULT", seed, step + 1, done, trunc, policy.mode)
          32 +            break
          33 +    env.close()
```

</details>

<a id="C047"></a>
### C047 · Lower transfer clearance to expand forward workspace

Commit `d6eb33d728e388f2e9cd7781d7e7c6a2f2032138`; parents: 555ce1083962455fd6189f980a1e247a40b33b4b. Recorded author date: 2026-09-09T16:21:16+02:00.

File roles (automatic): policy.

- [E0328](01_timeline.md#E0328): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C047_d6eb33d_approach.py) · [Exact all-file diff](evidence/diffs/C047_d6eb33d.diff)

[Previous saved controller snapshot](evidence/versions/C046_555ce10_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 40fb667..6affe18 100644
--- a/approach.py
+++ b/approach.py
@@ -112,7 +112,8 @@ class GeneratedApproach:
  112    112                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  113    113                  a += self.B@np.clip(u,-.05,.05)
  114    114              a[10]=1.; self.release_t+=1; return a
  115        -        goals=[np.array([pos[0],pos[1],.24]),np.array([self.dest[0],self.dest[1],.24]),
         115 +        clearance=.19
         116 +        goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
  116    117                 np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
  117    118          goal=goals[self.waypoint]; poserr=goal-pos
  118    119          err=np.r_[poserr, -feat[3:]]
```

</details>

<a id="C048"></a>
### C048 · Recover from missed releases and dropped objects

Commit `edbafe94318183b79b508a4af9ed3874e913bc16`; parents: d6eb33d728e388f2e9cd7781d7e7c6a2f2032138. Recorded author date: 2026-09-09T16:22:34+02:00.

File roles (automatic): policy.

- [E0332](01_timeline.md#E0332): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C048_edbafe9_approach.py) · [Exact all-file diff](evidence/diffs/C048_edbafe9.diff)

[Previous saved controller snapshot](evidence/versions/C047_d6eb33d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6affe18..ad8b073 100644
--- a/approach.py
+++ b/approach.py
@@ -28,6 +28,7 @@ class GeneratedApproach:
   28     28          self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
   29     29          self.approach_t=0
   30     30          self.resetting=self.task_i>0
          31 +        self.reset_t=0
   31     32          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
   32     33          x=self._v(state,name,"pose_x"); self.start_x=x
   33     34          if x<.23: base=(.18,-2.50,-.75)
@@ -70,12 +71,21 @@ class GeneratedApproach:
   70     71              rob=state.get_object_from_name("robot")
   71     72              cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
   72     73              a[3:10]=np.clip(safe-cur,-.2,.2); a[10]=1.
   73        -            if np.max(np.abs(safe-cur))<.03: self.resetting=False
          74 +            self.reset_t+=1
          75 +            if np.max(np.abs(safe-cur))<.03 or self.reset_t>=25: self.resetting=False
   74     76              return a
   75     77          if self.mode=="release" and not self._held(state):
   76        -            self.task_i+=1
   77        -            if self.task_i<len(self.tasks): self._setup(state,self.tasks[self.task_i])
   78        -            else: return a
          78 +            if self.object_name=="target_block":
          79 +                # A callback after release means the drop missed the strict goal;
          80 +                # retry from the observed block pose rather than idling forever.
          81 +                self._setup(state,"target_block")
          82 +            else:
          83 +                self.task_i+=1
          84 +                if self.task_i<len(self.tasks): self._setup(state,self.tasks[self.task_i])
          85 +                else: return a
          86 +        if self.mode not in ("pick","release") and not self._held(state):
          87 +            # Recover if contact is lost during a transfer.
          88 +            self._setup(state,self.object_name)
   79     89          if self._held(state) and self.mode=="pick": self._start_calibration(state)
   80     90          if self.mode=="pick":
   81     91              x,y,z=self._xyz(state,self.object_name); target,yoff,bx=self.pick_poses[self.pick_i]
```

</details>

<a id="C049"></a>
### C049 · Probe open-only final target release

Commit `d2d86c60703a2f803575f891bc4c56040dd776f9`; parents: edbafe94318183b79b508a4af9ed3874e913bc16. Recorded author date: 2026-09-09T16:22:52+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C049_d2d86c6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/release_probe_openonly.py b/release_probe_openonly.py
new file mode 100644
index 0000000..7e7cb27
--- /dev/null
+++ b/release_probe_openonly.py
@@ -0,0 +1,24 @@
           1 +"""Test whether an unwedged target releases with gripper motion alone."""
           2 +import sys
           3 +import numpy as np
           4 +from env_client import make_env
           5 +from approach import GeneratedApproach
           6 +
           7 +
           8 +for seed in map(int, sys.argv[1:] or [0]):
           9 +    env = make_env()
          10 +    state, info = env.reset(seed=seed)
          11 +    policy = GeneratedApproach(env.action_space, env.observation_space, {})
          12 +    policy.reset(state, info)
          13 +    for step in range(env.max_steps):
          14 +        action = policy.get_action(state)
          15 +        if policy.mode == "release" and policy.object_name == "target_block":
          16 +            action = np.zeros(env.action_space.shape, dtype=env.action_space.dtype)
          17 +            action[10] = 1.0
          18 +        state, reward, done, trunc, info = env.step(action)
          19 +        if done or trunc:
          20 +            block = state.get_object_from_name("target_block")
          21 +            print(seed, step + 1, done, trunc,
          22 +                  [round(state.get(block, "pose_" + c), 5) for c in "xyz"])
          23 +            break
          24 +    env.close()
```

</details>

<a id="C050"></a>
### C050 · Advance pickup search once per accidental grasp

Commit `eba01de236cc7b4eb10a45be6594fba9aafdf24e`; parents: d2d86c60703a2f803575f891bc4c56040dd776f9. Recorded author date: 2026-09-09T16:23:01+02:00.

File roles (automatic): policy.

- [E0336](01_timeline.md#E0336): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C050_eba01de_approach.py) · [Exact all-file diff](evidence/diffs/C050_eba01de.diff)

[Previous saved controller snapshot](evidence/versions/C048_edbafe9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ad8b073..8c965d0 100644
--- a/approach.py
+++ b/approach.py
@@ -27,6 +27,7 @@ class GeneratedApproach:
   27     27      def _setup(self,state,name):
   28     28          self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
   29     29          self.approach_t=0
          30 +        self.opening_wrong=False
   30     31          self.resetting=self.task_i>0
   31     32          self.reset_t=0
   32     33          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
@@ -62,8 +63,12 @@ class GeneratedApproach:
   62     63          self.last_pos=self._feat(s); self.last_delta=0.
   63     64      def get_action(self,state):
   64     65          a=np.zeros(self.action_space.shape,dtype=self.action_space.dtype)
          66 +        if self.mode=="pick" and self.opening_wrong:
          67 +            if self._v(state,"robot","grasp_active")>.5: a[10]=1.; return a
          68 +            self.opening_wrong=False
   65     69          if self.mode=="pick" and self._v(state,"robot","grasp_active")>.5 and not self._held(state):
   66        -            a[10]=1.; self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); return a
          70 +            self.opening_wrong=True; a[10]=1.; self.pick_t=0; self.approach_t=0
          71 +            self.pick_i=(self.pick_i+1)%len(self.pick_poses); return a
   67     72          if self.mode=="reserve":
   68     73              a[0]=-.20; a[10]=-1.; self._start_calibration(state); return a
   69     74          if self.mode=="pick" and self.resetting:
```

</details>

<a id="C051"></a>
### C051 · Open target gripper without post-seat motion

Commit `a3db0e0c776e049092f60c63fa835e79713eaeb6`; parents: eba01de236cc7b4eb10a45be6594fba9aafdf24e. Recorded author date: 2026-09-09T16:24:15+02:00.

File roles (automatic): policy.

- [E0342](01_timeline.md#E0342): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C051_a3db0e0_approach.py) · [Exact all-file diff](evidence/diffs/C051_a3db0e0.diff)

[Previous saved controller snapshot](evidence/versions/C050_eba01de_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8c965d0..e14cae7 100644
--- a/approach.py
+++ b/approach.py
@@ -121,7 +121,7 @@ class GeneratedApproach:
  121    121                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  122    122                  self.last_pos=feat; self.last_delta=d; return a
  123    123          if self.mode=="release":
  124        -            if self.release_t<60:
         124 +            if self.object_name!="target_block" and self.release_t<60:
  125    125                  g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
  126    126                  er=np.r_[g-pos,-feat[3:]]
  127    127                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
```

</details>

<a id="C052"></a>
### C052 · Discard obstructions beyond table edge for reliable release

Commit `c3d9c6704b819f31d90555a5868a270089acdc3f`; parents: a3db0e0c776e049092f60c63fa835e79713eaeb6. Recorded author date: 2026-09-09T16:28:37+02:00.

File roles (automatic): policy.

- [E0358](01_timeline.md#E0358): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C052_c3d9c67_approach.py) · [Exact all-file diff](evidence/diffs/C052_c3d9c67.diff)

[Previous saved controller snapshot](evidence/versions/C051_a3db0e0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e14cae7..c4bd8a1 100644
--- a/approach.py
+++ b/approach.py
@@ -52,8 +52,10 @@ class GeneratedApproach:
   52     52                  qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
   53     53          if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
   54     54          else:
   55        -            k=self.task_i; self.dest=np.array([.16+.07*(k%4), -.36 if k%2==0 else .36])
   56        -            self.rest_z=.075+self._v(state,name,"half_extent_z")
          55 +            # Carry blockers beyond a side edge and release in free space. This
          56 +            # avoids trapping the fingers between a small block and the table.
          57 +            k=self.task_i; self.dest=np.array([x,-.50 if k%2==0 else .50])
          58 +            self.rest_z=.18
   57     59      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   58     60      def _feat(self,s):
   59     61          o=self.object_name
@@ -121,11 +123,6 @@ class GeneratedApproach:
  121    123                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  122    124                  self.last_pos=feat; self.last_delta=d; return a
  123    125          if self.mode=="release":
  124        -            if self.object_name!="target_block" and self.release_t<60:
  125        -                g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
  126        -                er=np.r_[g-pos,-feat[3:]]
  127        -                u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  128        -                a += self.B@np.clip(u,-.05,.05)
  129    126              a[10]=1.; self.release_t+=1; return a
  130    127          clearance=.19
  131    128          goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
```

</details>

<a id="C053"></a>
### C053 · Remove harmful reserve move and restore supported blocker staging

Commit `56018998022a4418ee0236e8f36ec22e7081259f`; parents: c3d9c6704b819f31d90555a5868a270089acdc3f. Recorded author date: 2026-09-09T16:29:14+02:00.

File roles (automatic): policy.

- [E0362](01_timeline.md#E0362): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C053_5601899_approach.py) · [Exact all-file diff](evidence/diffs/C053_5601899.diff)

[Previous saved controller snapshot](evidence/versions/C052_c3d9c67_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c4bd8a1..16200b2 100644
--- a/approach.py
+++ b/approach.py
@@ -52,10 +52,8 @@ class GeneratedApproach:
   52     52                  qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
   53     53          if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
   54     54          else:
   55        -            # Carry blockers beyond a side edge and release in free space. This
   56        -            # avoids trapping the fingers between a small block and the table.
   57        -            k=self.task_i; self.dest=np.array([x,-.50 if k%2==0 else .50])
   58        -            self.rest_z=.18
          55 +            k=self.task_i; self.dest=np.array([.16+.07*(k%4),-.36 if k%2==0 else .36])
          56 +            self.rest_z=.075+self._v(state,name,"half_extent_z")
   59     57      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   60     58      def _feat(self,s):
   61     59          o=self.object_name
@@ -123,6 +121,11 @@ class GeneratedApproach:
  123    121                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  124    122                  self.last_pos=feat; self.last_delta=d; return a
  125    123          if self.mode=="release":
         124 +            if self.object_name!="target_block" and self.release_t<60:
         125 +                g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
         126 +                er=np.r_[g-pos,-feat[3:]]
         127 +                u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
         128 +                a += self.B@np.clip(u,-.05,.05)
  126    129              a[10]=1.; self.release_t+=1; return a
  127    130          clearance=.19
  128    131          goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
@@ -141,7 +144,6 @@ class GeneratedApproach:
  141    144              self.waypoint+=1
  142    145              # The last waypoint seats the object before opening the fingers.
  143    146              if self.waypoint>=3: self.mode="release"; self.release_t=0; self.release_x=pos[0]
  144        -            elif self.waypoint==1 and self.dest[0]>self.start_x+.03: self.mode="reserve"
  145    147              else: self._start_calibration(state)
  146    148              a[10]=-1.; return a
  147    149          u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(err,-.06,.06))
```

</details>

<a id="C054"></a>
### C054 · Pre-retract base for long forward target transfers

Commit `d2a7e274d863df5d66b021b3c1acbfe8b742229f`; parents: 56018998022a4418ee0236e8f36ec22e7081259f. Recorded author date: 2026-09-09T16:30:08+02:00.

File roles (automatic): policy.

- [E0366](01_timeline.md#E0366): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C054_d2a7e27_approach.py) · [Exact all-file diff](evidence/diffs/C054_d2a7e27.diff)

[Previous saved controller snapshot](evidence/versions/C053_5601899_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 16200b2..5152117 100644
--- a/approach.py
+++ b/approach.py
@@ -32,18 +32,24 @@ class GeneratedApproach:
   32     32          self.reset_t=0
   33     33          self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
   34     34          x=self._v(state,name,"pose_x"); self.start_x=x
   35        -        if x<.23: base=(.18,-2.50,-.75)
   36        -        else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
          35 +        pick_bx=-.12
          36 +        model_x=x
          37 +        if name=="target_block" and self.region[0]>x+.15:
          38 +            # Pick with the base retracted and the arm extended.  The stored base
          39 +            # travel then supplies forward workspace during transport.
          40 +            pick_bx=-.30; model_x=x+.18
          41 +        if model_x<.23: base=(.18,-2.50,-.75)
          42 +        else: base=(.35+2*(model_x-.336),-2.20+1.5*(model_x-.336),-.60+.8*(model_x-.336))
   37     43          triples=[(base[0]-.10,base[1],base[2]),base,(base[0]+.08,base[1],base[2]),
   38     44                   (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
   39     45                   (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
   40        -        if x<.23:
          46 +        if model_x<.23:
   41     47              for q2 in (.10,.20,.30,.40):
   42     48                  for q4 in (-2.50,-2.35,-2.20):
   43     49                      for q6 in (-.90,-.75,-.60): triples.append((q2,q4,q6))
   44     50          self.pick_poses=[]
   45     51          for q2,q4,q6 in triples:
   46        -            self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,-.12))
          52 +            self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,pick_bx))
   47     53          if name!="target_block":
   48     54              # A second, highly folded grasp family reaches the tiny obstructions.
   49     55              q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
```

</details>

<a id="C055"></a>
### C055 · Require firmer target support before opening

Commit `d982ec7aaf1a6d4d470ab1ea5bfaf0900bb0aa7e`; parents: d2a7e274d863df5d66b021b3c1acbfe8b742229f. Recorded author date: 2026-09-09T16:31:03+02:00.

File roles (automatic): policy.

- [E0372](01_timeline.md#E0372): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C055_d982ec7_approach.py) · [Exact all-file diff](evidence/diffs/C055_d982ec7.diff)

[Previous saved controller snapshot](evidence/versions/C054_d2a7e27_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5152117..1fcef12 100644
--- a/approach.py
+++ b/approach.py
@@ -145,7 +145,8 @@ class GeneratedApproach:
  145    145          tol=.012 if self.waypoint<2 else .004
  146    146          arrived=(np.linalg.norm(poserr)<tol)
  147    147          if self.waypoint==2:
  148        -            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
         148 +            zmargin=.0048 if self.object_name=="target_block" else .012
         149 +            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+zmargin)
  149    150          if arrived and np.linalg.norm(feat[3:])<.025:
  150    151              self.waypoint+=1
  151    152              # The last waypoint seats the object before opening the fingers.
```

</details>

<a id="C056"></a>
### C056 · Retry blocked target opening with delayed support push

Commit `0340a295f867a07f228caadb6893d0a762deaf6a`; parents: d982ec7aaf1a6d4d470ab1ea5bfaf0900bb0aa7e. Recorded author date: 2026-09-09T16:31:52+02:00.

File roles (automatic): policy.

- [E0376](01_timeline.md#E0376): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C056_0340a29_approach.py) · [Exact all-file diff](evidence/diffs/C056_0340a29.diff)

[Previous saved controller snapshot](evidence/versions/C055_d982ec7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1fcef12..20cac2c 100644
--- a/approach.py
+++ b/approach.py
@@ -127,7 +127,8 @@ class GeneratedApproach:
  127    127                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  128    128                  self.last_pos=feat; self.last_delta=d; return a
  129    129          if self.mode=="release":
  130        -            if self.object_name!="target_block" and self.release_t<60:
         130 +            needs_push=(self.object_name!="target_block" or self.release_t>=2)
         131 +            if needs_push and self.release_t<60:
  131    132                  g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
  132    133                  er=np.r_[g-pos,-feat[3:]]
  133    134                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
@@ -145,8 +146,7 @@ class GeneratedApproach:
  145    146          tol=.012 if self.waypoint<2 else .004
  146    147          arrived=(np.linalg.norm(poserr)<tol)
  147    148          if self.waypoint==2:
  148        -            zmargin=.0048 if self.object_name=="target_block" else .012
  149        -            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+zmargin)
         149 +            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
  150    150          if arrived and np.linalg.norm(feat[3:])<.025:
  151    151              self.waypoint+=1
  152    152              # The last waypoint seats the object before opening the fingers.
```

</details>

<a id="C057"></a>
### C057 · Lift jammed target gripper while preserving placement XY

Commit `b6a1b28b3a41c141d3b4e054c0705e765bd8ae3f`; parents: 0340a295f867a07f228caadb6893d0a762deaf6a. Recorded author date: 2026-09-09T16:32:37+02:00.

File roles (automatic): policy.

- [E0380](01_timeline.md#E0380): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C057_b6a1b28_approach.py) · [Exact all-file diff](evidence/diffs/C057_b6a1b28.diff)

[Previous saved controller snapshot](evidence/versions/C056_0340a29_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 20cac2c..f6208e8 100644
--- a/approach.py
+++ b/approach.py
@@ -129,7 +129,8 @@ class GeneratedApproach:
  129    129          if self.mode=="release":
  130    130              needs_push=(self.object_name!="target_block" or self.release_t>=2)
  131    131              if needs_push and self.release_t<60:
  132        -                g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
         132 +                gz=self.rest_z-.005 if self.object_name!="target_block" else self.release_z+.04
         133 +                g=np.array([self.release_x,self.dest[1],gz])
  133    134                  er=np.r_[g-pos,-feat[3:]]
  134    135                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  135    136                  a += self.B@np.clip(u,-.05,.05)
@@ -150,7 +151,8 @@ class GeneratedApproach:
  150    151          if arrived and np.linalg.norm(feat[3:])<.025:
  151    152              self.waypoint+=1
  152    153              # The last waypoint seats the object before opening the fingers.
  153        -            if self.waypoint>=3: self.mode="release"; self.release_t=0; self.release_x=pos[0]
         154 +            if self.waypoint>=3:
         155 +                self.mode="release"; self.release_t=0; self.release_x=pos[0]; self.release_z=pos[2]
  154    156              else: self._start_calibration(state)
  155    157              a[10]=-1.; return a
  156    158          u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(err,-.06,.06))
```

</details>

<a id="C058"></a>
### C058 · Add seed one jammed-release diagnostics

Commit `838fa4638cbb97067e2b33c167b15b0ba0d86b96`; parents: b6a1b28b3a41c141d3b4e054c0705e765bd8ae3f. Recorded author date: 2026-09-09T16:35:20+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C058_838fa46.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/release_probe_seed1.py b/release_probe_seed1.py
new file mode 100644
index 0000000..c6f021b
--- /dev/null
+++ b/release_probe_seed1.py
@@ -0,0 +1,32 @@
           1 +"""Concise diagnostics for seed 1 with no obstructions."""
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +env = make_env()
           7 +s, info = env.reset(seed=1, options={"object_count": 0})
           8 +p = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +p.reset(s, info)
          10 +was_held = False
          11 +for t in range(env.max_steps):
          12 +    a = p.get_action(s)
          13 +    old_mode = p.mode
          14 +    s, _, done, trunc, _ = env.step(a)
          15 +    rob = s.get_object_from_name("robot")
          16 +    blk = s.get_object_from_name("target_block")
          17 +    held = s.get(blk, "grasp_active") > .5
          18 +    if held and not was_held:
          19 +        print("GRASP", t, "candidate", p.pick_i,
          20 +              "finger", s.get(rob, "finger_state"),
          21 +              "tf", [round(s.get(rob, "grasp_tf_" + c), 5) for c in "xyz"],
          22 +              "qtf", [round(s.get(rob, "grasp_tf_q" + c), 5) for c in "xyzw"])
          23 +    if old_mode == "release" and (p.release_t <= 8 or p.release_t % 10 == 0):
          24 +        print("RELEASE", t, p.release_t, "finger", round(s.get(rob,"finger_state"),4),
          25 +              "rheld", s.get(rob,"grasp_active"), "bheld", s.get(blk,"grasp_active"),
          26 +              "xyz", [round(s.get(blk, "pose_" + c), 5) for c in "xyz"],
          27 +              "a", [round(float(x), 3) for x in a])
          28 +    was_held = held
          29 +    if done or trunc:
          30 +        print("RESULT", t + 1, done, trunc)
          31 +        break
          32 +env.close()
```

</details>

<a id="C059"></a>
### C059 · Avoid non-releasable centered grasp on long-forward transfers

Commit `b2df7a78506dacdcfe8ae21c4c4ce32e6d1b5ced`; parents: 838fa4638cbb97067e2b33c167b15b0ba0d86b96. Recorded author date: 2026-09-09T16:36:26+02:00.

File roles (automatic): policy.

- [E0398](01_timeline.md#E0398): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C059_b2df7a7_approach.py) · [Exact all-file diff](evidence/diffs/C059_b2df7a7.diff)

[Previous saved controller snapshot](evidence/versions/C057_b6a1b28_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f6208e8..fb8e528 100644
--- a/approach.py
+++ b/approach.py
@@ -34,7 +34,8 @@ class GeneratedApproach:
   34     34          x=self._v(state,name,"pose_x"); self.start_x=x
   35     35          pick_bx=-.12
   36     36          model_x=x
   37        -        if name=="target_block" and self.region[0]>x+.15:
          37 +        forward_retracted=(name=="target_block" and self.region[0]>x+.15)
          38 +        if forward_retracted:
   38     39              # Pick with the base retracted and the arm extended.  The stored base
   39     40              # travel then supplies forward workspace during transport.
   40     41              pick_bx=-.30; model_x=x+.18
@@ -43,6 +44,10 @@ class GeneratedApproach:
   43     44          triples=[(base[0]-.10,base[1],base[2]),base,(base[0]+.08,base[1],base[2]),
   44     45                   (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
   45     46                   (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
          47 +        if forward_retracted:
          48 +            # The centered pose closes to finger_state ~= .1 on this branch and
          49 +            # cannot reopen. Use offset grasps with useful finger clearance.
          50 +            triples=[triples[2],triples[3],triples[4],triples[5],triples[6],triples[0]]
   46     51          if model_x<.23:
   47     52              for q2 in (.10,.20,.30,.40):
   48     53                  for q4 in (-2.50,-2.35,-2.20):
```

</details>

<a id="C060"></a>
### C060 · Keep final target stationary while opening

Commit `8a952ca020b8b2202c56cbe57cdd56b4cb80aba6`; parents: b2df7a78506dacdcfe8ae21c4c4ce32e6d1b5ced. Recorded author date: 2026-09-09T16:39:35+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0410](01_timeline.md#E0410): commit hash in recorded output.
[Controller after this commit](evidence/versions/C060_8a952ca_approach.py) · [Exact all-file diff](evidence/diffs/C060_8a952ca.diff)

[Previous saved controller snapshot](evidence/versions/C059_b2df7a7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fb8e528..2c35972 100644
--- a/approach.py
+++ b/approach.py
@@ -132,10 +132,8 @@ class GeneratedApproach:
  132    132                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  133    133                  self.last_pos=feat; self.last_delta=d; return a
  134    134          if self.mode=="release":
  135        -            needs_push=(self.object_name!="target_block" or self.release_t>=2)
  136        -            if needs_push and self.release_t<60:
  137        -                gz=self.rest_z-.005 if self.object_name!="target_block" else self.release_z+.04
  138        -                g=np.array([self.release_x,self.dest[1],gz])
         135 +            if self.object_name!="target_block" and self.release_t<60:
         136 +                g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
  139    137                  er=np.r_[g-pos,-feat[3:]]
  140    138                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  141    139                  a += self.B@np.clip(u,-.05,.05)
diff --git a/probe_forward_grasps.py b/probe_forward_grasps.py
new file mode 100644
index 0000000..b3bbb87
--- /dev/null
+++ b/probe_forward_grasps.py
@@ -0,0 +1,16 @@
           1 +import concurrent.futures,numpy as np
           2 +from env_client import make_env
           3 +base=(.314,-2.227,-.614)
           4 +triples=[(base[0]+d2,base[1]+d4,base[2]+d6) for d2,d4,d6 in
           5 +         [(0,0,0),(-.1,0,0),(.08,0,0),(0,-.1,-.1),(0,.1,.1),(0,0,-.18),(0,0,.18),(.15,-.15,0),(-.15,.15,0)]]
           6 +def run(c):
           7 + e=make_env();s,_=e.reset(seed=1,options={'object_count':0});q=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2])
           8 + def v(n,f):return s.get(s.get_object_from_name(n),f)
           9 + for t in range(25):
          10 +  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
          11 +  a[0]=np.clip(-.3-v('robot','pos_base_x'),-.2,.2);a[1]=np.clip(v('target_block','pose_y')-.00135-v('robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(q-cur,-.2,.2);a[10]=1 if t<16 else -1;s,*_=e.step(a)
          12 +  if v('target_block','grasp_active')>.5:
          13 +   out=(c,t,round(v('robot','finger_state'),3),round(v('robot','grasp_tf_z'),3));e.close();return out
          14 + e.close();return (c,None,None,None)
          15 +with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex:
          16 + for x in ex.map(run,triples):print(x,flush=True)
```

</details>

<a id="C061"></a>
### C061 · Add reliable far-obstruction grasp postures

Commit `ccf2a77c8fbbc357c5d9b73d153cb593ed61b9a1`; parents: 8a952ca020b8b2202c56cbe57cdd56b4cb80aba6. Recorded author date: 2026-09-09T16:43:41+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0425](01_timeline.md#E0425): commit hash in recorded output.
[Controller after this commit](evidence/versions/C061_ccf2a77_approach.py) · [Exact all-file diff](evidence/diffs/C061_ccf2a77.diff)

[Previous saved controller snapshot](evidence/versions/C060_8a952ca_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2c35972..c58ff5a 100644
--- a/approach.py
+++ b/approach.py
@@ -44,6 +44,11 @@ class GeneratedApproach:
   44     44          triples=[(base[0]-.10,base[1],base[2]),base,(base[0]+.08,base[1],base[2]),
   45     45                   (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
   46     46                   (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
          47 +        if name!="target_block" and model_x>.38:
          48 +            # Far-side obstructions need a more extended elbow.  These poses
          49 +            # retain enough finger clearance to release after transport.
          50 +            triples=[(.50,-2.05,-.40),(.50,-1.90,-.80),
          51 +                     (.60,-2.05,-.40),(.60,-1.90,-.80)]+triples
   47     52          if forward_retracted:
   48     53              # The centered pose closes to finger_state ~= .1 on this branch and
   49     54              # cannot reopen. Use offset grasps with useful finger clearance.
diff --git a/scan_far_obstacle.py b/scan_far_obstacle.py
new file mode 100644
index 0000000..c9967c7
--- /dev/null
+++ b/scan_far_obstacle.py
@@ -0,0 +1,14 @@
           1 +import concurrent.futures,itertools,numpy as np
           2 +from env_client import make_env
           3 +def run(c):
           4 + e=make_env();s,_=e.reset(seed=8);name='obstruction1';q=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2])
           5 + def v(n,f):return s.get(s.get_object_from_name(n),f)
           6 + for t in range(16):
           7 +  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
           8 +  a[1]=np.clip(v(name,'pose_y')-.00135-v('robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(q-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
           9 +  if v(name,'grasp_active')>.5:out=(c,t,v('robot','finger_state'));e.close();return out
          10 + e.close();return(c,None,None)
          11 +cs=list(itertools.product([.4,.5,.6,.7],[-2.2,-2.05,-1.9],[-.8,-.6,-.4]))
          12 +with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
          13 + for x in ex.map(run,cs):
          14 +  if x[1] is not None:print(x,flush=True)
```

</details>

<a id="C062"></a>
### C062 · Improve policy trajectory diagnostics

Commit `0b6c2ee1a5b316766df5558a6195069a21d6514a`; parents: ccf2a77c8fbbc357c5d9b73d153cb593ed61b9a1. Recorded author date: 2026-09-09T16:45:46+02:00.

File roles (automatic): diagnostic/test.

- [E0443](01_timeline.md#E0443): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C062_0b6c2ee.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index cef8420..f5e7ad2 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -7,7 +7,10 @@ for seed in map(int,sys.argv[1:] or [11]):
    7      7    s,r,d,tr,i=e.step(p.get_action(s))
    8      8    if t%25==0:
    9      9     rob=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
   10        -   print(seed,t,p.mode,p.waypoint,'held',s.get(rob,'grasp_active'),'b',[round(s.get(b,'pose_'+c),3) for c in 'xyz'])
          10 +   cur=s.get_object_from_name(p.object_name)
          11 +   print(seed,t,p.object_name,p.mode,p.waypoint,'held',s.get(rob,'grasp_active'),
          12 +         'obj',[round(s.get(cur,'pose_'+c),3) for c in 'xyz'],
          13 +         'b',[round(s.get(b,'pose_'+c),3) for c in 'xyz'])
   11     14    if d or tr: break
   12     15   print('RESULT',seed,t+1,d,tr,p.mode)
   13     16   e.close()
```

</details>

<a id="C063"></a>
### C063 · Keep obstruction drops within reachable edge workspace

Commit `6d12d39d2401f2e739cb66dccc30ff907610dbba`; parents: 0b6c2ee1a5b316766df5558a6195069a21d6514a. Recorded author date: 2026-09-09T16:46:42+02:00.

File roles (automatic): policy.

- [E0447](01_timeline.md#E0447): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C063_6d12d39_approach.py) · [Exact all-file diff](evidence/diffs/C063_6d12d39.diff)

[Previous saved controller snapshot](evidence/versions/C061_ccf2a77_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c58ff5a..7d419a1 100644
--- a/approach.py
+++ b/approach.py
@@ -68,7 +68,9 @@ class GeneratedApproach:
   68     68                  qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
   69     69          if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
   70     70          else:
   71        -            k=self.task_i; self.dest=np.array([.16+.07*(k%4),-.36 if k%2==0 else .36])
          71 +            # Keep edge drops inside the arm's well-conditioned x workspace;
          72 +            # wider spacing can leave a short-arm grasp unable to descend.
          73 +            k=self.task_i; self.dest=np.array([.16+.03*(k%4),-.36 if k%2==0 else .36])
   72     74              self.rest_z=.075+self._v(state,name,"half_extent_z")
   73     75      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   74     76      def _feat(self,s):
```

</details>

<a id="C064"></a>
### C064 · Log gripper clearance in trajectory tests

Commit `e7485e159aae3f3d49fda479a6fdae31818824e1`; parents: 6d12d39d2401f2e739cb66dccc30ff907610dbba. Recorded author date: 2026-09-09T16:47:34+02:00.

File roles (automatic): diagnostic/test.

- [E0455](01_timeline.md#E0455): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C064_e7485e1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index f5e7ad2..3b30628 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -9,6 +9,7 @@ for seed in map(int,sys.argv[1:] or [11]):
    9      9     rob=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
   10     10     cur=s.get_object_from_name(p.object_name)
   11     11     print(seed,t,p.object_name,p.mode,p.waypoint,'held',s.get(rob,'grasp_active'),
          12 +         'finger',round(s.get(rob,'finger_state'),3),
   12     13           'obj',[round(s.get(cur,'pose_'+c),3) for c in 'xyz'],
   13     14           'b',[round(s.get(b,'pose_'+c),3) for c in 'xyz'])
   14     15    if d or tr: break
```

</details>

<a id="C065"></a>
### C065 · Release obstructions without clamping against table

Commit `7d82379f3ecf6c1ec217b55048108878ebe40582`; parents: e7485e159aae3f3d49fda479a6fdae31818824e1. Recorded author date: 2026-09-09T16:48:09+02:00.

File roles (automatic): policy.

- [E0460](01_timeline.md#E0460): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C065_7d82379_approach.py) · [Exact all-file diff](evidence/diffs/C065_7d82379.diff)

[Previous saved controller snapshot](evidence/versions/C063_6d12d39_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7d419a1..3cf27cc 100644
--- a/approach.py
+++ b/approach.py
@@ -139,11 +139,9 @@ class GeneratedApproach:
  139    139                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  140    140                  self.last_pos=feat; self.last_delta=d; return a
  141    141          if self.mode=="release":
  142        -            if self.object_name!="target_block" and self.release_t<60:
  143        -                g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
  144        -                er=np.r_[g-pos,-feat[3:]]
  145        -                u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  146        -                a += self.B@np.clip(u,-.05,.05)
         142 +            # The last waypoint is already a supported drop.  Moving the wrist
         143 +            # down while opening can clamp a cuboid against the table and stop
         144 +            # the fingers entirely, so release without Cartesian motion.
  147    145              a[10]=1.; self.release_t+=1; return a
  148    146          clearance=.19
  149    147          goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
```

</details>

<a id="C066"></a>
### C066 · Parameterize far-obstruction grasp scan

Commit `e8d5bde8b1ab11e3c7702925270e30219f637446`; parents: 7d82379f3ecf6c1ec217b55048108878ebe40582. Recorded author date: 2026-09-09T16:48:54+02:00.

File roles (automatic): diagnostic/test.

- [E0470](01_timeline.md#E0470): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C066_e8d5bde.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/scan_far_obstacle.py b/scan_far_obstacle.py
index c9967c7..1e3245c 100644
--- a/scan_far_obstacle.py
+++ b/scan_far_obstacle.py
@@ -1,11 +1,13 @@
    1        -import concurrent.futures,itertools,numpy as np
           1 +import concurrent.futures,itertools,numpy as np,sys
    2      2  from env_client import make_env
           3 +seed=int(sys.argv[1]) if len(sys.argv)>1 else 8
           4 +name=sys.argv[2] if len(sys.argv)>2 else 'obstruction1'
    3      5  def run(c):
    4        - e=make_env();s,_=e.reset(seed=8);name='obstruction1';q=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2])
           6 + e=make_env();s,_=e.reset(seed=seed);q=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2])
    5      7   def v(n,f):return s.get(s.get_object_from_name(n),f)
    6      8   for t in range(16):
    7      9    r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
    8        -  a[1]=np.clip(v(name,'pose_y')-.00135-v('robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(q-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
          10 +  a[0]=np.clip(-.12-v('robot','pos_base_x'),-.2,.2);a[1]=np.clip(v(name,'pose_y')-.00135-v('robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(q-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
    9     11    if v(name,'grasp_active')>.5:out=(c,t,v('robot','finger_state'));e.close();return out
   10     12   e.close();return(c,None,None)
   11     13  cs=list(itertools.product([.4,.5,.6,.7],[-2.2,-2.05,-1.9],[-.8,-.6,-.4]))
```

</details>

<a id="C067"></a>
### C067 · Release discarded obstructions above finger collision height

Commit `0b2615cc077edc6a1c3f04f68430e3d7e8c06d40`; parents: e8d5bde8b1ab11e3c7702925270e30219f637446. Recorded author date: 2026-09-09T16:51:30+02:00.

File roles (automatic): policy.

- [E0477](01_timeline.md#E0477): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C067_0b2615c_approach.py) · [Exact all-file diff](evidence/diffs/C067_0b2615c.diff)

[Previous saved controller snapshot](evidence/versions/C065_7d82379_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3cf27cc..f1393bf 100644
--- a/approach.py
+++ b/approach.py
@@ -144,8 +144,9 @@ class GeneratedApproach:
  144    144              # the fingers entirely, so release without Cartesian motion.
  145    145              a[10]=1.; self.release_t+=1; return a
  146    146          clearance=.19
         147 +        drop_z=self.rest_z+.005 if self.object_name=="target_block" else self.rest_z+.04
  147    148          goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
  148        -               np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
         149 +               np.array([self.dest[0],self.dest[1],drop_z])]
  149    150          goal=goals[self.waypoint]; poserr=goal-pos
  150    151          err=np.r_[poserr, -feat[3:]]
  151    152          if self.waypoint==1:
@@ -155,7 +156,10 @@ class GeneratedApproach:
  155    156          tol=.012 if self.waypoint<2 else .004
  156    157          arrived=(np.linalg.norm(poserr)<tol)
  157    158          if self.waypoint==2:
  158        -            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
         159 +            if self.object_name=="target_block":
         160 +                arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
         161 +            else:
         162 +                arrived=np.linalg.norm(poserr)<.006
  159    163          if arrived and np.linalg.norm(feat[3:])<.025:
  160    164              self.waypoint+=1
  161    165              # The last waypoint seats the object before opening the fingers.
```

</details>

<a id="C068"></a>
### C068 · Prefer releasable centered grasps at medium reach

Commit `a2d14ec43ac915e0c02a844aeaee25accc2c590e`; parents: 0b2615cc077edc6a1c3f04f68430e3d7e8c06d40. Recorded author date: 2026-09-09T16:51:54+02:00.

File roles (automatic): policy.

- [E0481](01_timeline.md#E0481): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C068_a2d14ec_approach.py) · [Exact all-file diff](evidence/diffs/C068_a2d14ec.diff)

[Previous saved controller snapshot](evidence/versions/C067_0b2615c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f1393bf..c07940a 100644
--- a/approach.py
+++ b/approach.py
@@ -49,6 +49,11 @@ class GeneratedApproach:
   49     49              # retain enough finger clearance to release after transport.
   50     50              triples=[(.50,-2.05,-.40),(.50,-1.90,-.80),
   51     51                       (.60,-2.05,-.40),(.60,-1.90,-.80)]+triples
          52 +        elif name!="target_block" and model_x>.25:
          53 +            # The lower-shoulder variant can pinch medium-distance blocks so
          54 +            # deeply that the fingers cannot reopen; prefer the centered pose.
          55 +            triples=[triples[1],triples[2],triples[3],triples[4],
          56 +                     triples[5],triples[6],triples[0]]
   52     57          if forward_retracted:
   53     58              # The centered pose closes to finger_state ~= .1 on this branch and
   54     59              # cannot reopen. Use offset grasps with useful finger clearance.
```

</details>

<a id="C069"></a>
### C069 · Use shallow medium-range obstruction grasp

Commit `39f586ede7f3aebbbe8f3365749148c036eb8c6f`; parents: a2d14ec43ac915e0c02a844aeaee25accc2c590e. Recorded author date: 2026-09-09T16:52:17+02:00.

File roles (automatic): policy.

- [E0485](01_timeline.md#E0485): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C069_39f586e_approach.py) · [Exact all-file diff](evidence/diffs/C069_39f586e.diff)

[Previous saved controller snapshot](evidence/versions/C068_a2d14ec_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c07940a..cc09e53 100644
--- a/approach.py
+++ b/approach.py
@@ -52,8 +52,8 @@ class GeneratedApproach:
   52     52          elif name!="target_block" and model_x>.25:
   53     53              # The lower-shoulder variant can pinch medium-distance blocks so
   54     54              # deeply that the fingers cannot reopen; prefer the centered pose.
   55        -            triples=[triples[1],triples[2],triples[3],triples[4],
   56        -                     triples[5],triples[6],triples[0]]
          55 +            triples=[triples[2],triples[3],triples[4],triples[5],
          56 +                     triples[6],triples[1],triples[0]]
   57     57          if forward_retracted:
   58     58              # The centered pose closes to finger_state ~= .1 on this branch and
   59     59              # cannot reopen. Use offset grasps with useful finger clearance.
```

</details>

<a id="C070"></a>
### C070 · Probe rotated obstruction grasp alternatives

Commit `6d9f07ab58886c3421e24e691a565733cb5971c6`; parents: 39f586ede7f3aebbbe8f3365749148c036eb8c6f. Recorded author date: 2026-09-09T16:53:14+02:00.

File roles (automatic): diagnostic/test.

- [E0494](01_timeline.md#E0494): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C070_6d9f07a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/scan_rotated_pick.py b/scan_rotated_pick.py
index df963ae..200d13f 100644
--- a/scan_rotated_pick.py
+++ b/scan_rotated_pick.py
@@ -1,13 +1,18 @@
    1        -import concurrent.futures,numpy as np
           1 +import concurrent.futures,numpy as np,sys,itertools
    2      2  from env_client import make_env
    3      3  def v(s,n,f):return s.get(s.get_object_from_name(n),f)
    4        -def run(off):
    5        - e=make_env();s,_=e.reset(seed=0,options={'object_count':0});x=v(s,'target_block','pose_x');y=v(s,'target_block','pose_y')
    6        - tar=np.array([0,.25,-np.pi,-2.2,0,-.6,np.pi])
           4 +seed=int(sys.argv[1]) if len(sys.argv)>1 else 3
           5 +name=sys.argv[2] if len(sys.argv)>2 else 'obstruction1'
           6 +def run(spec):
           7 + off,q7=spec;e=make_env();s,_=e.reset(seed=seed);y=v(s,name,'pose_y')
           8 + tar=np.array([0,.32,-np.pi,-2.22,0,-.61,q7])
    7      9   for t in range(15):
    8     10    r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
    9        -  a[1]=np.clip(y+off-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
   10        -  if v(s,'target_block','grasp_active')>.5:e.close();return off,True
   11        - e.close();return off,False
   12        -with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex:
   13        - print(list(ex.map(run,np.linspace(-.08,.08,9))))
          11 +  a[0]=np.clip(-.12-v(s,'robot','pos_base_x'),-.2,.2);a[1]=np.clip(y+off-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
          12 +  if v(s,name,'grasp_active')>.5:
          13 +   out=(round(off,3),round(q7,3),round(v(s,'robot','finger_state'),3));e.close();return out
          14 + e.close();return None
          15 +specs=list(itertools.product(np.linspace(-.08,.08,9),[0.,np.pi/2,np.pi]))
          16 +with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
          17 + for out in ex.map(run,specs):
          18 +  if out:print(out,flush=True)
```

</details>

<a id="C071"></a>
### C071 · Narrow rotated grasp probe to observed pickup pose

Commit `4a9f065f457488266e9eab48b77e4341c52228c4`; parents: 6d9f07ab58886c3421e24e691a565733cb5971c6. Recorded author date: 2026-09-09T16:55:33+02:00.

File roles (automatic): diagnostic/test.

- [E0495](01_timeline.md#E0495): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C071_4a9f065.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/scan_rotated_pick.py b/scan_rotated_pick.py
index 200d13f..e404e2d 100644
--- a/scan_rotated_pick.py
+++ b/scan_rotated_pick.py
@@ -5,14 +5,14 @@ seed=int(sys.argv[1]) if len(sys.argv)>1 else 3
    5      5  name=sys.argv[2] if len(sys.argv)>2 else 'obstruction1'
    6      6  def run(spec):
    7      7   off,q7=spec;e=make_env();s,_=e.reset(seed=seed);y=v(s,name,'pose_y')
    8        - tar=np.array([0,.32,-np.pi,-2.22,0,-.61,q7])
           8 + tar=np.array([0,.40,-np.pi,-2.22,0,-.61,q7])
    9      9   for t in range(15):
   10     10    r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
   11     11    a[0]=np.clip(-.12-v(s,'robot','pos_base_x'),-.2,.2);a[1]=np.clip(y+off-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
   12     12    if v(s,name,'grasp_active')>.5:
   13     13     out=(round(off,3),round(q7,3),round(v(s,'robot','finger_state'),3));e.close();return out
   14     14   e.close();return None
   15        -specs=list(itertools.product(np.linspace(-.08,.08,9),[0.,np.pi/2,np.pi]))
   16        -with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
          15 +specs=[(.00135,q7) for q7 in (0.,np.pi/2,np.pi)]
          16 +with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
   17     17   for out in ex.map(run,specs):
   18     18    if out:print(out,flush=True)
```

</details>

<a id="C072"></a>
### C072 · Rotate medium obstruction grasps across narrow face

Commit `7b43eeefa6ab445114038a451a844b04947860d5`; parents: 4a9f065f457488266e9eab48b77e4341c52228c4. Recorded author date: 2026-09-09T16:57:45+02:00.

File roles (automatic): policy.

- [E0500](01_timeline.md#E0500): commit hash in recorded output.
[Controller after this commit](evidence/versions/C072_7b43eee_approach.py) · [Exact all-file diff](evidence/diffs/C072_7b43eee.diff)

[Previous saved controller snapshot](evidence/versions/C069_39f586e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cc09e53..b445f05 100644
--- a/approach.py
+++ b/approach.py
@@ -63,6 +63,12 @@ class GeneratedApproach:
   63     63                  for q4 in (-2.50,-2.35,-2.20):
   64     64                      for q6 in (-.90,-.75,-.60): triples.append((q2,q4,q6))
   65     65          self.pick_poses=[]
          66 +        if name!="target_block" and .25<model_x<=.38:
          67 +            # Turn the fingers across the narrow face of rectangular blocks.
          68 +            # Besides being easier to acquire, this avoids over-deep grasps
          69 +            # whose finger mechanism cannot reopen after transport.
          70 +            q2,q4,q6=base[0]+.08,base[1],base[2]
          71 +            self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,0.]),.00135,pick_bx))
   66     72          for q2,q4,q6 in triples:
   67     73              self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,pick_bx))
   68     74          if name!="target_block":
```

</details>

<a id="C073"></a>
### C073 · Keep obstruction releases clear of table boundary

Commit `ba027a9d78d0e503338912b42aa69202356e76a5`; parents: 7b43eeefa6ab445114038a451a844b04947860d5. Recorded author date: 2026-09-09T16:58:49+02:00.

File roles (automatic): policy.

- [E0504](01_timeline.md#E0504): commit hash in recorded output.
[Controller after this commit](evidence/versions/C073_ba027a9_approach.py) · [Exact all-file diff](evidence/diffs/C073_ba027a9.diff)

[Previous saved controller snapshot](evidence/versions/C072_7b43eee_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b445f05..a0ea313 100644
--- a/approach.py
+++ b/approach.py
@@ -81,7 +81,7 @@ class GeneratedApproach:
   81     81          else:
   82     82              # Keep edge drops inside the arm's well-conditioned x workspace;
   83     83              # wider spacing can leave a short-arm grasp unable to descend.
   84        -            k=self.task_i; self.dest=np.array([.16+.03*(k%4),-.36 if k%2==0 else .36])
          84 +            k=self.task_i; self.dest=np.array([.16+.03*(k%4),-.30 if k%2==0 else .30])
   85     85              self.rest_z=.075+self._v(state,name,"half_extent_z")
   86     86      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   87     87      def _feat(self,s):
```

</details>

<a id="C074"></a>
### C074 · Try folded grasps first for troublesome medium obstructions

Commit `8a838b0359c2055d1cfe0646511215ee2444b8eb`; parents: ba027a9d78d0e503338912b42aa69202356e76a5. Recorded author date: 2026-09-09T17:00:10+02:00.

File roles (automatic): policy.

- [E0510](01_timeline.md#E0510): commit hash in recorded output.
[Controller after this commit](evidence/versions/C074_8a838b0_approach.py) · [Exact all-file diff](evidence/diffs/C074_8a838b0.diff)

[Previous saved controller snapshot](evidence/versions/C073_ba027a9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a0ea313..99ced55 100644
--- a/approach.py
+++ b/approach.py
@@ -75,8 +75,11 @@ class GeneratedApproach:
   75     75              # A second, highly folded grasp family reaches the tiny obstructions.
   76     76              q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
   77     77              bx=min(-.12,-.12+x-.219855)
          78 +            folded=[]
   78     79              for d in [0.,-.12,.12]:
   79        -                qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
          80 +                qq=q.copy(); qq[5]+=d; folded.append((qq,.196424,bx))
          81 +            if .25<model_x<=.38: self.pick_poses=folded+self.pick_poses
          82 +            else: self.pick_poses.extend(folded)
   80     83          if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
   81     84          else:
   82     85              # Keep edge drops inside the arm's well-conditioned x workspace;
```

</details>

<a id="C075"></a>
### C075 · Restore best validated release and grasp policy

Commit `4a5cb77376ce810fddabb502e427065cecf9d16d`; parents: 8a838b0359c2055d1cfe0646511215ee2444b8eb. Recorded author date: 2026-09-09T17:03:12+02:00.

File roles (automatic): policy.

- [E0518](01_timeline.md#E0518): commit hash in recorded output.
[Controller after this commit](evidence/versions/C075_4a5cb77_approach.py) · [Exact all-file diff](evidence/diffs/C075_4a5cb77.diff)

[Previous saved controller snapshot](evidence/versions/C074_8a838b0_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C063](#C063). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 99ced55..7d419a1 100644
--- a/approach.py
+++ b/approach.py
@@ -49,11 +49,6 @@ class GeneratedApproach:
   49     49              # retain enough finger clearance to release after transport.
   50     50              triples=[(.50,-2.05,-.40),(.50,-1.90,-.80),
   51     51                       (.60,-2.05,-.40),(.60,-1.90,-.80)]+triples
   52        -        elif name!="target_block" and model_x>.25:
   53        -            # The lower-shoulder variant can pinch medium-distance blocks so
   54        -            # deeply that the fingers cannot reopen; prefer the centered pose.
   55        -            triples=[triples[2],triples[3],triples[4],triples[5],
   56        -                     triples[6],triples[1],triples[0]]
   57     52          if forward_retracted:
   58     53              # The centered pose closes to finger_state ~= .1 on this branch and
   59     54              # cannot reopen. Use offset grasps with useful finger clearance.
@@ -63,28 +58,19 @@ class GeneratedApproach:
   63     58                  for q4 in (-2.50,-2.35,-2.20):
   64     59                      for q6 in (-.90,-.75,-.60): triples.append((q2,q4,q6))
   65     60          self.pick_poses=[]
   66        -        if name!="target_block" and .25<model_x<=.38:
   67        -            # Turn the fingers across the narrow face of rectangular blocks.
   68        -            # Besides being easier to acquire, this avoids over-deep grasps
   69        -            # whose finger mechanism cannot reopen after transport.
   70        -            q2,q4,q6=base[0]+.08,base[1],base[2]
   71        -            self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,0.]),.00135,pick_bx))
   72     61          for q2,q4,q6 in triples:
   73     62              self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,pick_bx))
   74     63          if name!="target_block":
   75     64              # A second, highly folded grasp family reaches the tiny obstructions.
   76     65              q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
   77     66              bx=min(-.12,-.12+x-.219855)
   78        -            folded=[]
   79     67              for d in [0.,-.12,.12]:
   80        -                qq=q.copy(); qq[5]+=d; folded.append((qq,.196424,bx))
   81        -            if .25<model_x<=.38: self.pick_poses=folded+self.pick_poses
   82        -            else: self.pick_poses.extend(folded)
          68 +                qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
   83     69          if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
   84     70          else:
   85     71              # Keep edge drops inside the arm's well-conditioned x workspace;
   86     72              # wider spacing can leave a short-arm grasp unable to descend.
   87        -            k=self.task_i; self.dest=np.array([.16+.03*(k%4),-.30 if k%2==0 else .30])
          73 +            k=self.task_i; self.dest=np.array([.16+.03*(k%4),-.36 if k%2==0 else .36])
   88     74              self.rest_z=.075+self._v(state,name,"half_extent_z")
   89     75      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   90     76      def _feat(self,s):
@@ -153,14 +139,15 @@ class GeneratedApproach:
  153    139                  d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
  154    140                  self.last_pos=feat; self.last_delta=d; return a
  155    141          if self.mode=="release":
  156        -            # The last waypoint is already a supported drop.  Moving the wrist
  157        -            # down while opening can clamp a cuboid against the table and stop
  158        -            # the fingers entirely, so release without Cartesian motion.
         142 +            if self.object_name!="target_block" and self.release_t<60:
         143 +                g=np.array([self.release_x,self.dest[1],self.rest_z-.005])
         144 +                er=np.r_[g-pos,-feat[3:]]
         145 +                u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
         146 +                a += self.B@np.clip(u,-.05,.05)
  159    147              a[10]=1.; self.release_t+=1; return a
  160    148          clearance=.19
  161        -        drop_z=self.rest_z+.005 if self.object_name=="target_block" else self.rest_z+.04
  162    149          goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
  163        -               np.array([self.dest[0],self.dest[1],drop_z])]
         150 +               np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
  164    151          goal=goals[self.waypoint]; poserr=goal-pos
  165    152          err=np.r_[poserr, -feat[3:]]
  166    153          if self.waypoint==1:
@@ -170,10 +157,7 @@ class GeneratedApproach:
  170    157          tol=.012 if self.waypoint<2 else .004
  171    158          arrived=(np.linalg.norm(poserr)<tol)
  172    159          if self.waypoint==2:
  173        -            if self.object_name=="target_block":
  174        -                arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
  175        -            else:
  176        -                arrived=np.linalg.norm(poserr)<.006
         160 +            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
  177    161          if arrived and np.linalg.norm(feat[3:])<.025:
  178    162              self.waypoint+=1
  179    163              # The last waypoint seats the object before opening the fingers.
```

</details>

<a id="C076"></a>
### C076 · Parameterize variable-count policy regression test

Commit `e5c379b807310d3d219ad69cb5576112bc8c006d`; parents: 4a5cb77376ce810fddabb502e427065cecf9d16d. Recorded author date: 2026-09-09T17:03:50+02:00.

File roles (automatic): diagnostic/test.

- [E0529](01_timeline.md#E0529): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C076_e5c379b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_many.py b/test_many.py
index 434c107..1547b8e 100644
--- a/test_many.py
+++ b/test_many.py
@@ -1,11 +1,13 @@
    1        -import concurrent.futures
           1 +import concurrent.futures,sys
    2      2  from env_client import make_env
    3      3  from approach import GeneratedApproach
    4        -def run(seed,count=0):
           4 +count=int(sys.argv[1]) if len(sys.argv)>1 else 0
           5 +seeds=list(map(int,sys.argv[2:])) if len(sys.argv)>2 else list(range(20))
           6 +def run(seed):
    5      7   e=make_env();s,i=e.reset(seed=seed,options={'object_count':count});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
    6        - for t in range(350):
           8 + for t in range(e.max_steps):
    7      9    s,_,d,tr,_=e.step(p.get_action(s))
    8     10    if d or tr:break
    9     11   e.close();return seed,t+1,d,p.mode
   10        -with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
   11        - for x in ex.map(run,range(20)):print(x,flush=True)
          12 +with concurrent.futures.ThreadPoolExecutor(max_workers=min(4,len(seeds))) as ex:
          13 + for x in ex.map(run,seeds):print('COUNT',count,*x,flush=True)
```

</details>

<a id="C077"></a>
### C077 · initial sandbox setup

Commit `956a7b2f260e6a09a46a124d82d0c29307d09012`; parents: e5c379b807310d3d219ad69cb5576112bc8c006d. Recorded author date: 2026-09-09T17:09:17+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C077_956a7b2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 85d005e..86a320d 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $12.01. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $3.21. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C078"></a>
### C078 · Report exact variable-count failure task

Commit `8c5f40026756aed0208c5f5b333cc9f559e1c8b1`; parents: 956a7b2f260e6a09a46a124d82d0c29307d09012. Recorded author date: 2026-09-09T17:09:58+02:00.

File roles (automatic): diagnostic/test.

- [E0549](01_timeline.md#E0549): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C078_8c5f400.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_many.py b/test_many.py
index 1547b8e..3f02a2a 100644
--- a/test_many.py
+++ b/test_many.py
@@ -8,6 +8,9 @@ def run(seed):
    8      8   for t in range(e.max_steps):
    9      9    s,_,d,tr,_=e.step(p.get_action(s))
   10     10    if d or tr:break
   11        - e.close();return seed,t+1,d,p.mode
          11 + cur=s.get_object_from_name(p.object_name)
          12 + detail=(p.object_name,p.task_i,p.pick_i,len(p.pick_poses),
          13 +         tuple(round(s.get(cur,'pose_'+c),3) for c in 'xyz'))
          14 + e.close();return seed,t+1,d,p.mode,detail
   12     15  with concurrent.futures.ThreadPoolExecutor(max_workers=min(4,len(seeds))) as ex:
   13     16   for x in ex.map(run,seeds):print('COUNT',count,*x,flush=True)
```

</details>

<a id="C079"></a>
### C079 · Extend dense grasp search to medium obstructions

Commit `f6757931a8f64123129dedac26d9908acda54288`; parents: 8c5f40026756aed0208c5f5b333cc9f559e1c8b1. Recorded author date: 2026-09-09T17:13:39+02:00.

File roles (automatic): policy.

- [E0554](01_timeline.md#E0554): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C079_f675793_approach.py) · [Exact all-file diff](evidence/diffs/C079_f675793.diff)

[Previous saved controller snapshot](evidence/versions/C075_4a5cb77_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7d419a1..4e3f492 100644
--- a/approach.py
+++ b/approach.py
@@ -53,7 +53,9 @@ class GeneratedApproach:
   53     53              # The centered pose closes to finger_state ~= .1 on this branch and
   54     54              # cannot reopen. Use offset grasps with useful finger clearance.
   55     55              triples=[triples[2],triples[3],triples[4],triples[5],triples[6],triples[0]]
   56        -        if model_x<.23:
          56 +        if model_x<.23 or (name!="target_block" and model_x<.30):
          57 +            # Small blocks are less tolerant of the analytic reach estimate;
          58 +            # retain a bounded dense grid through the medium-distance band.
   57     59              for q2 in (.10,.20,.30,.40):
   58     60                  for q4 in (-2.50,-2.35,-2.20):
   59     61                      for q6 in (-.90,-.75,-.60): triples.append((q2,q4,q6))
```

</details>

<a id="C080"></a>
### C080 · Trace grasp candidates in variable-count tests

Commit `07955a9854b205855c2abdadb8d696d09f92d28f`; parents: f6757931a8f64123129dedac26d9908acda54288. Recorded author date: 2026-09-09T17:15:24+02:00.

File roles (automatic): diagnostic/test.

- [E0560](01_timeline.md#E0560): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C080_07955a9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_many.py b/test_many.py
index 3f02a2a..9504495 100644
--- a/test_many.py
+++ b/test_many.py
@@ -5,7 +5,12 @@ count=int(sys.argv[1]) if len(sys.argv)>1 else 0
    5      5  seeds=list(map(int,sys.argv[2:])) if len(sys.argv)>2 else list(range(20))
    6      6  def run(seed):
    7      7   e=make_env();s,i=e.reset(seed=seed,options={'object_count':count});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
           8 + prior_task=-1
    8      9   for t in range(e.max_steps):
          10 +  if p.task_i!=prior_task:
          11 +   print('ENTER',seed,t,p.task_i,p.object_name,flush=True);prior_task=p.task_i
          12 +  if p.mode=='pick' and p._held(s):
          13 +   print('GRASP',seed,t,p.task_i,p.object_name,p.pick_i,flush=True)
    9     14    s,_,d,tr,_=e.step(p.get_action(s))
   10     15    if d or tr:break
   11     16   cur=s.get_object_from_name(p.object_name)
```

</details>

<a id="C081"></a>
### C081 · Compress alternating obstruction staging positions

Commit `11efccb320021b212e60b55f736d396189bbaff1`; parents: 07955a9854b205855c2abdadb8d696d09f92d28f. Recorded author date: 2026-09-09T17:16:17+02:00.

File roles (automatic): policy.

- [E0565](01_timeline.md#E0565): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C081_11efccb_approach.py) · [Exact all-file diff](evidence/diffs/C081_11efccb.diff)

[Previous saved controller snapshot](evidence/versions/C079_f675793_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4e3f492..1c56a38 100644
--- a/approach.py
+++ b/approach.py
@@ -72,7 +72,10 @@ class GeneratedApproach:
   72     72          else:
   73     73              # Keep edge drops inside the arm's well-conditioned x workspace;
   74     74              # wider spacing can leave a short-arm grasp unable to descend.
   75        -            k=self.task_i; self.dest=np.array([.16+.03*(k%4),-.36 if k%2==0 else .36])
          75 +            k=self.task_i
          76 +            # Advance each side independently, keeping the early drops in the
          77 +            # arm's reliable x band while still avoiding pile-up.
          78 +            self.dest=np.array([.16+.03*((k+1)//2),-.36 if k%2==0 else .36])
   76     79              self.rest_z=.075+self._v(state,name,"half_extent_z")
   77     80      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   78     81      def _feat(self,s):
```

</details>

<a id="C082"></a>
### C082 · Cap obstruction staging at reachable x

Commit `1e36eb6b4040fcf73c55f0a786e7db7a96adc941`; parents: 11efccb320021b212e60b55f736d396189bbaff1. Recorded author date: 2026-09-09T17:17:01+02:00.

File roles (automatic): policy.

- [E0569](01_timeline.md#E0569): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C082_1e36eb6_approach.py) · [Exact all-file diff](evidence/diffs/C082_1e36eb6.diff)

[Previous saved controller snapshot](evidence/versions/C081_11efccb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1c56a38..55e6e74 100644
--- a/approach.py
+++ b/approach.py
@@ -73,9 +73,9 @@ class GeneratedApproach:
   73     73              # Keep edge drops inside the arm's well-conditioned x workspace;
   74     74              # wider spacing can leave a short-arm grasp unable to descend.
   75     75              k=self.task_i
   76        -            # Advance each side independently, keeping the early drops in the
   77        -            # arm's reliable x band while still avoiding pile-up.
   78        -            self.dest=np.array([.16+.03*((k+1)//2),-.36 if k%2==0 else .36])
          76 +            # Keep edge drops distinct without extending beyond the arm's
          77 +            # reliable descent band.
          78 +            self.dest=np.array([min(.22,.16+.03*k),-.36 if k%2==0 else .36])
   79     79              self.rest_z=.075+self._v(state,name,"half_extent_z")
   80     80      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   81     81      def _feat(self,s):
```

</details>

<a id="C083"></a>
### C083 · Separate later obstruction drops into inner edge lanes

Commit `fd1d6401a3b2231dd32653b78acfb2cb13ca67f1`; parents: 1e36eb6b4040fcf73c55f0a786e7db7a96adc941. Recorded author date: 2026-09-09T17:17:52+02:00.

File roles (automatic): policy.

- [E0575](01_timeline.md#E0575): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C083_fd1d640_approach.py) · [Exact all-file diff](evidence/diffs/C083_fd1d640.diff)

[Previous saved controller snapshot](evidence/versions/C082_1e36eb6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 55e6e74..2d485cf 100644
--- a/approach.py
+++ b/approach.py
@@ -75,7 +75,8 @@ class GeneratedApproach:
   75     75              k=self.task_i
   76     76              # Keep edge drops distinct without extending beyond the arm's
   77     77              # reliable descent band.
   78        -            self.dest=np.array([min(.22,.16+.03*k),-.36 if k%2==0 else .36])
          78 +            lane=.36-.06*((k//2)%2)
          79 +            self.dest=np.array([min(.22,.16+.03*k),-lane if k%2==0 else lane])
   79     80              self.rest_z=.075+self._v(state,name,"half_extent_z")
   80     81      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   81     82      def _feat(self,s):
```

</details>

<a id="C084"></a>
### C084 · initial sandbox setup

Commit `1920e24899415dfedb577c3d83f0cba7786044c2`; parents: fd1d6401a3b2231dd32653b78acfb2cb13ca67f1. Recorded author date: 2026-09-09T17:19:08+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C084_1920e24.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 86a320d..6b9812e 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $3.21. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $2.26. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C085"></a>
### C085 · Use extended grasp family for far target blocks

Commit `0bfd8c61bbbaee1f3f12d861ac50a2f02b77bc1f`; parents: 1920e24899415dfedb577c3d83f0cba7786044c2. Recorded author date: 2026-09-09T17:20:11+02:00.

File roles (automatic): policy.

- [E0596](01_timeline.md#E0596): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C085_0bfd8c6_approach.py) · [Exact all-file diff](evidence/diffs/C085_0bfd8c6.diff)

[Previous saved controller snapshot](evidence/versions/C083_fd1d640_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2d485cf..8b6d4f5 100644
--- a/approach.py
+++ b/approach.py
@@ -44,8 +44,8 @@ class GeneratedApproach:
   44     44          triples=[(base[0]-.10,base[1],base[2]),base,(base[0]+.08,base[1],base[2]),
   45     45                   (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
   46     46                   (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
   47        -        if name!="target_block" and model_x>.38:
   48        -            # Far-side obstructions need a more extended elbow.  These poses
          47 +        if model_x>.38:
          48 +            # Far-side cuboids need a more extended elbow.  These poses
   49     49              # retain enough finger clearance to release after transport.
   50     50              triples=[(.50,-2.05,-.40),(.50,-1.90,-.80),
   51     51                       (.60,-2.05,-.40),(.60,-1.90,-.80)]+triples
```

</details>

<a id="C086"></a>
### C086 · Advance base for extreme far-side pickups

Commit `8300fa7dfaa0cad356faced4e4e67eb927ffeae9`; parents: 0bfd8c61bbbaee1f3f12d861ac50a2f02b77bc1f. Recorded author date: 2026-09-09T17:20:49+02:00.

File roles (automatic): policy.

- [E0600](01_timeline.md#E0600): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C086_8300fa7_approach.py) · [Exact all-file diff](evidence/diffs/C086_8300fa7.diff)

[Previous saved controller snapshot](evidence/versions/C085_0bfd8c6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8b6d4f5..b47903e 100644
--- a/approach.py
+++ b/approach.py
@@ -34,6 +34,7 @@ class GeneratedApproach:
   34     34          x=self._v(state,name,"pose_x"); self.start_x=x
   35     35          pick_bx=-.12
   36     36          model_x=x
          37 +        if x>.44: pick_bx=-.08
   37     38          forward_retracted=(name=="target_block" and self.region[0]>x+.15)
   38     39          if forward_retracted:
   39     40              # Pick with the base retracted and the arm extended.  The stored base
```

</details>

<a id="C087"></a>
### C087 · Prefer releasable alternate grasp for far targets

Commit `dc79774203ad2f9902f82283e3d8177e72ea10ce`; parents: 8300fa7dfaa0cad356faced4e4e67eb927ffeae9. Recorded author date: 2026-09-09T17:21:37+02:00.

File roles (automatic): policy.

- [E0607](01_timeline.md#E0607): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C087_dc79774_approach.py) · [Exact all-file diff](evidence/diffs/C087_dc79774.diff)

[Previous saved controller snapshot](evidence/versions/C086_8300fa7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b47903e..f0e6663 100644
--- a/approach.py
+++ b/approach.py
@@ -48,8 +48,10 @@ class GeneratedApproach:
   48     48          if model_x>.38:
   49     49              # Far-side cuboids need a more extended elbow.  These poses
   50     50              # retain enough finger clearance to release after transport.
   51        -            triples=[(.50,-2.05,-.40),(.50,-1.90,-.80),
   52        -                     (.60,-2.05,-.40),(.60,-1.90,-.80)]+triples
          51 +            far=[(.50,-2.05,-.40),(.50,-1.90,-.80),
          52 +                 (.60,-2.05,-.40),(.60,-1.90,-.80)]
          53 +            if name=="target_block": far=[far[1],far[3],far[2],far[0]]
          54 +            triples=far+triples
   53     55          if forward_retracted:
   54     56              # The centered pose closes to finger_state ~= .1 on this branch and
   55     57              # cannot reopen. Use offset grasps with useful finger clearance.
```

</details>

<a id="C088"></a>
### C088 · initial sandbox setup

Commit `acc380b1f83f7ac893942cb0076b1ece54ef511b`; parents: dc79774203ad2f9902f82283e3d8177e72ea10ce. Recorded author date: 2026-09-09T17:22:36+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C088_acc380b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 6b9812e..3c5a54f 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $2.26. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.69. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C089"></a>
### C089 · Pulse jammed obstruction gripper before reopening

Commit `a80ce48a1a244b5a1a2fac25c6195f3cadc0310d`; parents: acc380b1f83f7ac893942cb0076b1ece54ef511b. Recorded author date: 2026-09-09T17:23:24+02:00.

File roles (automatic): policy.

- [E0625](01_timeline.md#E0625): commit hash in recorded output.
[Controller after this commit](evidence/versions/C089_a80ce48_approach.py) · [Exact all-file diff](evidence/diffs/C089_a80ce48.diff)

[Previous saved controller snapshot](evidence/versions/C087_dc79774_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f0e6663..20abbfe 100644
--- a/approach.py
+++ b/approach.py
@@ -153,7 +153,12 @@ class GeneratedApproach:
  153    153                  er=np.r_[g-pos,-feat[3:]]
  154    154                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  155    155                  a += self.B@np.clip(u,-.05,.05)
  156        -            a[10]=1.; self.release_t+=1; return a
         156 +            # If an obstruction remains latched, a short re-close/open cycle
         157 +            # can break static finger contact. Ordinary releases finish before
         158 +            # this recovery ever activates.
         159 +            pulse=(self.object_name!="target_block" and self.release_t>=20
         160 +                   and self.release_t%30<3)
         161 +            a[10]=-1. if pulse else 1.; self.release_t+=1; return a
  157    162          clearance=.19
  158    163          goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
  159    164                 np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
```

</details>

<a id="C090"></a>
### C090 · Remove ineffective gripper pulse recovery

Commit `eb3e8d46791d57e4a83f0298ebe826692deb3864`; parents: a80ce48a1a244b5a1a2fac25c6195f3cadc0310d. Recorded author date: 2026-09-09T17:24:17+02:00.

File roles (automatic): policy.

- [E0630](01_timeline.md#E0630): commit hash in recorded output.
[Controller after this commit](evidence/versions/C090_eb3e8d4_approach.py) · [Exact all-file diff](evidence/diffs/C090_eb3e8d4.diff)

[Previous saved controller snapshot](evidence/versions/C089_a80ce48_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C087](#C087). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 20abbfe..f0e6663 100644
--- a/approach.py
+++ b/approach.py
@@ -153,12 +153,7 @@ class GeneratedApproach:
  153    153                  er=np.r_[g-pos,-feat[3:]]
  154    154                  u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
  155    155                  a += self.B@np.clip(u,-.05,.05)
  156        -            # If an obstruction remains latched, a short re-close/open cycle
  157        -            # can break static finger contact. Ordinary releases finish before
  158        -            # this recovery ever activates.
  159        -            pulse=(self.object_name!="target_block" and self.release_t>=20
  160        -                   and self.release_t%30<3)
  161        -            a[10]=-1. if pulse else 1.; self.release_t+=1; return a
         156 +            a[10]=1.; self.release_t+=1; return a
  162    157          clearance=.19
  163    158          goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
  164    159                 np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
```

</details>

<a id="C091"></a>
### C091 · initial sandbox setup

Commit `cdccafcd29310fb5ca1d465ef99888fde48963f3`; parents: eb3e8d46791d57e4a83f0298ebe826692deb3864. Recorded author date: 2026-09-09T17:25:16+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C091_cdccafc.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 3c5a54f..d842239 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.69. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.23. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C092"></a>
### C092 · Move first obstruction drop into reachable descent band

Commit `8b2a6883f256d16399f899de526480717ad0d665`; parents: cdccafcd29310fb5ca1d465ef99888fde48963f3. Recorded author date: 2026-09-09T17:27:32+02:00.

File roles (automatic): policy.

- [E0651](01_timeline.md#E0651): commit hash in recorded output.
[Controller after this commit](evidence/versions/C092_8b2a688_approach.py) · [Exact all-file diff](evidence/diffs/C092_8b2a688.diff)

[Previous saved controller snapshot](evidence/versions/C090_eb3e8d4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f0e6663..76c2aa2 100644
--- a/approach.py
+++ b/approach.py
@@ -79,7 +79,8 @@ class GeneratedApproach:
   79     79              # Keep edge drops distinct without extending beyond the arm's
   80     80              # reliable descent band.
   81     81              lane=.36-.06*((k//2)%2)
   82        -            self.dest=np.array([min(.22,.16+.03*k),-lane if k%2==0 else lane])
          82 +            stage_x=.18 if k==0 else (.19 if k==1 else .22)
          83 +            self.dest=np.array([stage_x,-lane if k%2==0 else lane])
   83     84              self.rest_z=.075+self._v(state,name,"half_extent_z")
   84     85      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
   85     86      def _feat(self,s):
```

</details>

<a id="C093"></a>
### C093 · Center first staging goal across mirrored control branch

Commit `7da7347e4f5e0d0607fd3c4e586e4a0493dd1bbb`; parents: 8b2a6883f256d16399f899de526480717ad0d665. Recorded author date: 2026-09-09T17:29:19+02:00.

File roles (automatic): policy.

- [E0658](01_timeline.md#E0658): commit hash in recorded output.
[Controller after this commit](evidence/versions/C093_7da7347_approach.py) · [Exact all-file diff](evidence/diffs/C093_7da7347.diff)

[Previous saved controller snapshot](evidence/versions/C092_8b2a688_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 76c2aa2..b97fcc9 100644
--- a/approach.py
+++ b/approach.py
@@ -79,7 +79,7 @@ class GeneratedApproach:
   79     79              # Keep edge drops distinct without extending beyond the arm's
   80     80              # reliable descent band.
   81     81              lane=.36-.06*((k//2)%2)
   82        -            stage_x=.18 if k==0 else (.19 if k==1 else .22)
          82 +            stage_x=.17 if k==0 else (.19 if k==1 else .22)
   83     83              self.dest=np.array([stage_x,-lane if k%2==0 else lane])
   84     84              self.rest_z=.075+self._v(state,name,"half_extent_z")
   85     85      def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
```

</details>

<a id="C094"></a>
### C094 · initial sandbox setup

Commit `8007f16d23da006a9f0946d0671c8f39ab8ea786`; parents: 7da7347e4f5e0d0607fd3c4e586e4a0493dd1bbb. Recorded author date: 2026-09-09T17:29:28+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C094_8007f16.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index d842239..cc99805 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $1.23. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $0.60. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

