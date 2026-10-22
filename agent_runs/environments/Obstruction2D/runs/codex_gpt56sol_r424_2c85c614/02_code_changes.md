# Obstruction2D · gpt-5.6-sol · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `b8db573` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `b59ebec` | Add initial reactive grasp-and-place baseline | approach.py, probe_env.py | [E0011](01_timeline.md#E0011) |
| [C003](#C003) · `b9dd552` | Add live multi-seed policy test harness | test_approach.py | [E0020](01_timeline.md#E0020) |
| [C004 / R01](#C004) · `670d6a3` | Implement feedback FSM for clearing and target placement | approach.py, test_approach.py | [E0079](01_timeline.md#E0079) |
| [C005 / R02](#C005) · `55d3dab` | Use reset pose as reachable safe travel height | approach.py | [E0094](01_timeline.md#E0094) |
| [C006 / R03](#C006) · `98c6f07` | Park all movable objects tallest-first before final placement | approach.py | [E0106](01_timeline.md#E0106) |
| [C007 / R04](#C007) · `6d93a7d` | Exclude static surface and park cleared objects vertically | approach.py | [E0112](01_timeline.md#E0112) |
| [C008 / R05](#C008) · `e727013` | Keep vacuum off during horizontal transit | approach.py | [E0118](01_timeline.md#E0118) |
| [C009 / R06](#C009) · `5a9cda5` | Park cleared objects low enough for later regrasp | approach.py | [E0124](01_timeline.md#E0124) |
| [C010 / R07](#C010) · `f214f7d` | Park obstructions laterally away from target surface | approach.py | [E0130](01_timeline.md#E0130) |
| [C011 / R08](#C011) · `dd0457e` | Only pre-park target when it blocks obstacle access | approach.py | [E0144](01_timeline.md#E0144) |
| [C012 / R09](#C012) · `3f73fd4` | Fix moving-goal bug in obstruction carry phase | approach.py | [E0150](01_timeline.md#E0150) |
| [C013 / R10](#C013) · `735b56a` | Use lower carry height to match successful placement trajectory | approach.py | [E0177](01_timeline.md#E0177) |
| [C014 / R11](#C014) · `b15ba76` | Bias final placement slightly inside successful support region | approach.py | [E0181](01_timeline.md#E0181) |
| [C015 / R12](#C015) · `af4477f` | Use fine vertical steps so vacuum reaches contact | approach.py | [E0193](01_timeline.md#E0193) |
| [C016 / R13](#C016) · `9c6bdf4` | Avoid overshooting ceiling during retreat | approach.py | [E0201](01_timeline.md#E0201) |
| [C017 / R14](#C017) · `4f80855` | Park blockers away from target and handle travel bounds | approach.py | [E0207](01_timeline.md#E0207) |
| [C018 / R15](#C018) · `2d184c4` | Vertically separate parked blockers and recover at walls | approach.py | [E0213](01_timeline.md#E0213) |
| [C019 / R16](#C019) · `0c006f7` | Park blockers far outside surface at low clearance height | approach.py | [E0221](01_timeline.md#E0221) |
| [C020 / R17](#C020) · `adf84ae` | Add edge grasps and compensate carried-object offset | approach.py | [E0229](01_timeline.md#E0229) |
| [C021 / R18](#C021) · `b7ccec6` | Allocate geometry-scored parking slots for blockers | approach.py | [E0236](01_timeline.md#E0236) |
| [C022 / R19](#C022) · `0f0c2ee` | Reserve a remote slot for temporarily parked target | approach.py | [E0242](01_timeline.md#E0242) |
| [C023 / R20](#C023) · `71c469c` | Lift final target above all parked blockers | approach.py | [E0248](01_timeline.md#E0248) |
| [C024 / R21](#C024) · `2185ba3` | Keep parking slots away from side-wall dead zones | approach.py | [E0254](01_timeline.md#E0254) |
| [C025 / R22](#C025) · `8e66f4e` | Cap verification lift at reachable ceiling | approach.py | [E0260](01_timeline.md#E0260) |
| [C026 / R23](#C026) · `3098aab` | Raise temporary target and maximize final carry clearance | approach.py | [E0271](01_timeline.md#E0271) |
| [C027 / R24](#C027) · `5075837` | Park crowded target outward and lower cleared blockers | approach.py | [E0277](01_timeline.md#E0277) |
| [C028 / R25](#C028) · `0605fd3` | Route blockers outward without crossing the surface cluster | approach.py | [E0283](01_timeline.md#E0283) |
| [C029 / R26](#C029) · `f064af0` | Carry blockers high then lower them into parking slots | approach.py | [E0289](01_timeline.md#E0289) |
| [C030 / R27](#C030) · `a4cb1db` | Accept maximum reachable blocker carry height | approach.py | [E0293](01_timeline.md#E0293) |
| [C031 / R28](#C031) · `13fcd58` | Restore reliable low blocker parking behavior | approach.py | [E0297](01_timeline.md#E0297) |
| [C032 / R29](#C032) · `04141a4` | Choose globally clear parking slots over directional routing | approach.py | [E0301](01_timeline.md#E0301) |
| [C033 / R30](#C033) · `3f93ca0` | Use globally safest temporary target slot | approach.py | [E0307](01_timeline.md#E0307) |
| [C034 / R31](#C034) · `990576d` | Use denser nonoverlapping parking allocation | approach.py | [E0317](01_timeline.md#E0317) |
| [C035 / R32](#C035) · `a11bd5f` | Restore validated parking clearance margin | approach.py | [E0321](01_timeline.md#E0321) |
| [C036](#C036) · `539f180` | initial sandbox setup | AGENTS.md | No matched commit command/output |
| [C037 / R33](#C037) · `c1c4586` | Verify grasp against lowest observed object height | approach.py | [E0342](01_timeline.md#E0342) |
| [C038 / R34](#C038) · `e97a537` | Clear crowded objects from highest top edge downward | approach.py | [E0348](01_timeline.md#E0348) |
| [C039 / R35](#C039) · `c9b3655` | Keep parked blockers clear of final target sweep | approach.py | [E0358](01_timeline.md#E0358) |
| [C040 / R36](#C040) · `4d36a38` | Move crowded target after only materially taller blockers | approach.py | [E0366](01_timeline.md#E0366) |
| [C041 / R37](#C041) · `be6feb6` | Protect future pickups when assigning parking slots | approach.py | [E0378](01_timeline.md#E0378) |
| [C042 / R38](#C042) · `616a82f` | Prioritize physically overlapping taller blockers | approach.py | [E0387](01_timeline.md#E0387) |
| [C043 / R39](#C043) · `dafcc2f` | Allocate outer parking slots before inner ones | approach.py | [E0396](01_timeline.md#E0396) |
| [C044](#C044) · `678059d` | Add pinned object-count regression support | test_approach.py | [E0411](01_timeline.md#E0411) |
| [C045 / R40](#C045) · `0e14ec7` | Choose least-conflicting fallback parking slots | approach.py | [E0417](01_timeline.md#E0417) |
| [C046 / R41](#C046) · `f87f63f` | Increase clearance around future pickup columns | approach.py | [E0423](01_timeline.md#E0423) |
| [C047 / R42](#C047) · `6fc104f` | Only relocate objects blocking the final placement footprint | approach.py | [E0437](01_timeline.md#E0437) |
| [C048 / R43](#C048) · `c91cb8e` | Include blockers near the placement sweep envelope | approach.py | [E0441](01_timeline.md#E0441) |
| [C049 / R44](#C049) · `bb1c5eb` | Increase clearance from the final lowering corridor | approach.py | [E0447](01_timeline.md#E0447) |
| [C050 / R45](#C050) · `20d09c8` | Stack blockers when no safe horizontal slot exists | approach.py | [E0458](01_timeline.md#E0458) |
| [C051 / R46](#C051) · `5210b1a` | Stack only outside target transit corridor | approach.py | [E0464](01_timeline.md#E0464) |
| [C052 / R47](#C052) · `4868fc2` | Shorten recovery lift after failed grasps | approach.py | [E0475](01_timeline.md#E0475) |
| [C053 / R48](#C053) · `7cfa55b` | Add tolerance to failed-grasp recovery height | approach.py | [E0481](01_timeline.md#E0481) |
| [C054 / R49](#C054) · `af3dcdd` | Recover when verification lift is collision-blocked | approach.py | [E0489](01_timeline.md#E0489) |
| [C055 / R50](#C055) · `05d0971` | Add boundary columns for dense blocker parking | approach.py | [E0500](01_timeline.md#E0500) |
| [C056 / R51](#C056) · `4897e46` | Skip blockers already displaced from the goal | approach.py | [E0518](01_timeline.md#E0518) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `b8db573e6da12982e76953169b0a4634a230d0d6`; parents: none (initial snapshot). Recorded author date: 2026-09-08T22:08:02+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_b8db573.diff)

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
index 0000000..414b193
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1,168 @@
           1 +{
           2 +  "host": "127.0.0.1",
           3 +  "port": 37571,
           4 +  "token": "9fe72bf4d5f1e075c4bd1f12720e58ae",
           5 +  "observation_space": {
           6 +    "type": "ObjectCentric",
           7 +    "types": [
           8 +      {
           9 +        "name": "crv_robot",
          10 +        "parent": null,
          11 +        "features": [
          12 +          "x",
          13 +          "y",
          14 +          "theta",
          15 +          "base_radius",
          16 +          "arm_joint",
          17 +          "arm_length",
          18 +          "vacuum",
          19 +          "gripper_height",
          20 +          "gripper_width"
          21 +        ]
          22 +      },
          23 +      {
          24 +        "name": "kinematic2d",
          25 +        "parent": null,
          26 +        "features": [
          27 +          "x",
          28 +          "y",
          29 +          "theta",
          30 +          "static",
          31 +          "color_r",
          32 +          "color_g",
          33 +          "color_b",
          34 +          "z_order"
          35 +        ]
          36 +      },
          37 +      {
          38 +        "name": "circle",
          39 +        "parent": "kinematic2d",
          40 +        "features": [
          41 +          "x",
          42 +          "y",
          43 +          "theta",
          44 +          "static",
          45 +          "color_r",
          46 +          "color_g",
          47 +          "color_b",
          48 +          "z_order",
          49 +          "radius"
          50 +        ]
          51 +      },
          52 +      {
          53 +        "name": "double_rectangle",
          54 +        "parent": "kinematic2d",
          55 +        "features": [
          56 +          "x",
          57 +          "y",
          58 +          "theta",
          59 +          "static",
          60 +          "color_r",
          61 +          "color_g",
          62 +          "color_b",
          63 +          "z_order",
          64 +          "width",
          65 +          "height",
          66 +          "x1",
          67 +          "y1",
          68 +          "theta1",
          69 +          "width1",
          70 +          "height1",
          71 +          "z_order1",
          72 +          "color_r1",
          73 +          "color_g1",
          74 +          "color_b1"
          75 +        ]
          76 +      },
          77 +      {
          78 +        "name": "lobject",
          79 +        "parent": "kinematic2d",
          80 +        "features": [
          81 +          "x",
          82 +          "y",
          83 +          "theta",
          84 +          "static",
          85 +          "color_r",
          86 +          "color_g",
          87 +          "color_b",
          88 +          "z_order",
          89 +          "width",
          90 +          "length_side1",
          91 +          "length_side2"
          92 +        ]
          93 +      },
          94 +      {
          95 +        "name": "rectangle",
          96 +        "parent": "kinematic2d",
          97 +        "features": [
          98 +          "x",
          99 +          "y",
         100 +          "theta",
         101 +          "static",
         102 +          "color_r",
         103 +          "color_g",
         104 +          "color_b",
         105 +          "z_order",
         106 +          "width",
         107 +          "height"
         108 +        ]
         109 +      },
         110 +      {
         111 +        "name": "target_block",
         112 +        "parent": "rectangle",
         113 +        "features": [
         114 +          "x",
         115 +          "y",
         116 +          "theta",
         117 +          "static",
         118 +          "color_r",
         119 +          "color_g",
         120 +          "color_b",
         121 +          "z_order",
         122 +          "width",
         123 +          "height"
         124 +        ]
         125 +      },
         126 +      {
         127 +        "name": "target_surface",
         128 +        "parent": "rectangle",
         129 +        "features": [
         130 +          "x",
         131 +          "y",
         132 +          "theta",
         133 +          "static",
         134 +          "color_r",
         135 +          "color_g",
         136 +          "color_b",
         137 +          "z_order",
         138 +          "width",
         139 +          "height"
         140 +        ]
         141 +      }
         142 +    ]
         143 +  },
         144 +  "action_space": {
         145 +    "type": "Box",
         146 +    "shape": [
         147 +      5
         148 +    ],
         149 +    "low": [
         150 +      -0.05000000074505806,
         151 +      -0.05000000074505806,
         152 +      -0.19634954631328583,
         153 +      -0.10000000149011612,
         154 +      0.0
         155 +    ],
         156 +    "high": [
         157 +      0.05000000074505806,
         158 +      0.05000000074505806,
         159 +      0.19634954631328583,
         160 +      0.10000000149011612,
         161 +      1.0
         162 +    ],
         163 +    "dtype": "float32"
         164 +  },
         165 +  "max_steps": 1000,
         166 +  "primitives": [],
         167 +  "strict": true
         168 +}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Add initial reactive grasp-and-place baseline

Commit `b59ebec9e85d78c52f923b67a60ca56446903236`; parents: b8db573e6da12982e76953169b0a4634a230d0d6. Recorded author date: 2026-09-08T22:09:18+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0011](01_timeline.md#E0011): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_b59ebec_approach.py) · [Exact all-file diff](evidence/diffs/C002_b59ebec.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..a8e421c
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,43 @@
           1 +"""Reactive policy for Obstruction2DEnv."""
           2 +
           3 +import math
           4 +import numpy as np
           5 +
           6 +
           7 +class GeneratedApproach:
           8 +    def __init__(self, action_space, observation_space, primitives):
           9 +        self.action_space = action_space
          10 +        self.types = {t.name: t for t in observation_space.types}
          11 +        self.phase = "approach"
          12 +
          13 +    def reset(self, state, info):
          14 +        self.phase = "approach"
          15 +
          16 +    def _one(self, state, type_name):
          17 +        return state.get_objects(self.types[type_name])[0]
          18 +
          19 +    def get_action(self, state):
          20 +        robot = self._one(state, "crv_robot")
          21 +        block = self._one(state, "target_block")
          22 +        surface = self._one(state, "target_surface")
          23 +        rx, ry = state.get(robot, "x"), state.get(robot, "y")
          24 +        theta = state.get(robot, "theta")
          25 +        arm = state.get(robot, "arm_joint")
          26 +        vacuum = state.get(robot, "vacuum")
          27 +        bx, by = state.get(block, "x"), state.get(block, "y")
          28 +        sx, sy = state.get(surface, "x"), state.get(surface, "y")
          29 +
          30 +        # First baseline: approach/grasp the block, then translate it to the surface.
          31 +        carrying = vacuum > 0.5 and math.hypot(bx - sx, by - sy) > 0.03
          32 +        tx, ty = (sx, sy) if carrying else (bx, by)
          33 +        desired = math.atan2(ty - ry, tx - rx)
          34 +        err = (desired - theta + math.pi) % (2 * math.pi) - math.pi
          35 +        dist = math.hypot(tx - rx, ty - ry)
          36 +        target_arm = max(0.0, dist - 0.02)
          37 +        action = np.zeros(5, dtype=np.float32)
          38 +        if abs(err) > 0.05:
          39 +            action[2] = np.clip(err, -0.196, 0.196)
          40 +        else:
          41 +            action[3] = np.clip(target_arm - arm, -0.1, 0.1)
          42 +        action[4] = 1.0
          43 +        return np.clip(action, self.action_space.low, self.action_space.high).astype(np.float32)
diff --git a/probe_env.py b/probe_env.py
new file mode 100644
index 0000000..85a00b6
--- /dev/null
+++ b/probe_env.py
@@ -0,0 +1,29 @@
           1 +"""Small black-box probes; never imported by approach.py."""
           2 +
           3 +import argparse
           4 +import numpy as np
           5 +from env_client import make_env
           6 +
           7 +
           8 +def dump(state):
           9 +    for name in sorted(state.get_object_names()):
          10 +        obj = state.get_object_from_name(name)
          11 +        fs = state.type_features[obj.type]
          12 +        vals = [state.get(obj, f) for f in fs]
          13 +        print(name, obj.type.name, dict(zip(fs, np.round(vals, 4))))
          14 +
          15 +
          16 +if __name__ == "__main__":
          17 +    ap = argparse.ArgumentParser()
          18 +    ap.add_argument("--seed", type=int, default=0)
          19 +    ap.add_argument("--steps", type=int, default=0)
          20 +    args = ap.parse_args()
          21 +    env = make_env()
          22 +    obs, info = env.reset(seed=args.seed)
          23 +    print("max_steps", env.max_steps, "info", info)
          24 +    dump(obs)
          25 +    for i in range(args.steps):
          26 +        obs, rew, term, trunc, info = env.step(np.array([0, 0, 0, 0, 1], np.float32))
          27 +        print("step", i + 1, rew, term, trunc)
          28 +        dump(obs)
          29 +    env.close()
```

</details>

<a id="C003"></a>
### C003 · Add live multi-seed policy test harness

Commit `b9dd5522cc174a68908dfdd892bf66edb8ef52ae`; parents: b59ebec9e85d78c52f923b67a60ca56446903236. Recorded author date: 2026-09-08T22:10:02+02:00.

File roles (automatic): diagnostic/test.

- [E0020](01_timeline.md#E0020): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C003_b9dd552.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..813912b
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,43 @@
           1 +"""Evaluate the current policy against fresh live instances."""
           2 +
           3 +import argparse
           4 +import time
           5 +from collections import Counter
           6 +from env_client import make_env
           7 +from approach import GeneratedApproach
           8 +
           9 +
          10 +def run(seed, verbose=False):
          11 +    env = make_env()
          12 +    state, info = env.reset(seed=seed)
          13 +    approach = GeneratedApproach(env.action_space, env.observation_space, {})
          14 +    approach.reset(state, info)
          15 +    t0 = time.monotonic()
          16 +    term = trunc = False
          17 +    steps = 0
          18 +    try:
          19 +        while not (term or trunc):
          20 +            action = approach.get_action(state)
          21 +            state, reward, term, trunc, info = env.step(action)
          22 +            steps += 1
          23 +            if verbose and (steps < 10 or steps % 25 == 0 or term):
          24 +                r = state.get_objects(env.observation_space.get_type("crv_robot"))[0]
          25 +                b = state.get_objects(env.observation_space.get_type("target_block"))[0]
          26 +                print(steps, action.round(3), "r", round(state.get(r,"x"),3), round(state.get(r,"y"),3), round(state.get(r,"theta"),3), round(state.get(r,"arm_joint"),3), round(state.get(r,"vacuum"),1), "b", round(state.get(b,"x"),3), round(state.get(b,"y"),3))
          27 +    finally:
          28 +        env.close()
          29 +    return term, steps, info.get("object_count"), time.monotonic() - t0
          30 +
          31 +
          32 +if __name__ == "__main__":
          33 +    ap = argparse.ArgumentParser()
          34 +    ap.add_argument("--start", type=int, default=0)
          35 +    ap.add_argument("--n", type=int, default=10)
          36 +    ap.add_argument("--verbose", action="store_true")
          37 +    args = ap.parse_args()
          38 +    results = []
          39 +    for seed in range(args.start, args.start + args.n):
          40 +        result = run(seed, args.verbose)
          41 +        results.append(result)
          42 +        print(seed, result)
          43 +    print("success", sum(r[0] for r in results), "/", len(results), "by_count", Counter((r[2], r[0]) for r in results))
```

</details>

<a id="C004"></a>
<a id="R01"></a>
### C004 · Implement feedback FSM for clearing and target placement

Commit `670d6a3f67570639f5110b2d2c6590347bc3fe13`; parents: b9dd5522cc174a68908dfdd892bf66edb8ef52ae. Recorded author date: 2026-09-08T22:22:47+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0079](01_timeline.md#E0079): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Baseline stalls; explore manipulation → replace it with a controller that tracks movement phases and retries.

- Early controller redesign after an interrupted baseline test and extensive probes. The test harness also changes: the new harness enforces env.max_steps. It contains two recorded policy edit events (L75 and L77) before one commit; the intermediate pre-commit source is not reconstructed.

Prior mapped context: [E0012](01_timeline.md#E0012), [E0020](01_timeline.md#E0020), [E0022](01_timeline.md#E0022), [E0024](01_timeline.md#E0024), [E0026](01_timeline.md#E0026), [E0034](01_timeline.md#E0034), [E0035](01_timeline.md#E0035), [E0055](01_timeline.md#E0055), [E0066](01_timeline.md#E0066), [E0071](01_timeline.md#E0071), [E0073](01_timeline.md#E0073), [E0075](01_timeline.md#E0075), [E0077](01_timeline.md#E0077), [E0079](01_timeline.md#E0079).

Prior mapped post-edit test reports: [E0079](01_timeline.md#E0079), [E0088](01_timeline.md#E0088). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C004_670d6a3_approach.py) · [Exact all-file diff](evidence/diffs/C004_670d6a3.diff)

[Previous saved controller snapshot](evidence/versions/C002_b59ebec_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a8e421c..9d7d605 100644
--- a/approach.py
+++ b/approach.py
@@ -1,5 +1,4 @@
    1        -"""Reactive policy for Obstruction2DEnv."""
    2        -
           1 +"""Feedback controller for variable-count Obstruction2D."""
    3      2  import math
    4      3  import numpy as np
    5      4  
@@ -8,36 +7,111 @@ class GeneratedApproach:
    8      7      def __init__(self, action_space, observation_space, primitives):
    9      8          self.action_space = action_space
   10      9          self.types = {t.name: t for t in observation_space.types}
   11        -        self.phase = "approach"
   12     10  
   13     11      def reset(self, state, info):
   14        -        self.phase = "approach"
          12 +        rects = state.get_objects(self.types["rectangle"])
          13 +        self.todo = [o.name for o in rects if o.type.name == "rectangle"]
          14 +        self.todo.sort(key=lambda n: state.get(state.get_object_from_name(n), "height"))
          15 +        self.todo.append(state.get_objects(self.types["target_block"])[0].name)
          16 +        xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
          17 +        self.park_base = max(xs) + 0.45
          18 +        self.index, self.phase, self.retry = 0, "orient", 0
          19 +        self.stalled, self.last_robot_y = 0, None
          20 +        self.pick_y, self.attached, self.release_wait = 0.0, False, 0
          21 +
          22 +    @staticmethod
          23 +    def _clip(v, limit):
          24 +        return max(-limit, min(limit, v))
   15     25  
   16        -    def _one(self, state, type_name):
   17        -        return state.get_objects(self.types[type_name])[0]
          26 +    def _action(self, dx=0.0, dy=0.0, dtheta=0.0, darm=0.0, vac=0.0):
          27 +        a = np.array([dx, dy, dtheta, darm, vac], dtype=np.float32)
          28 +        return np.clip(a, self.action_space.low, self.action_space.high).astype(np.float32)
   18     29  
   19     30      def get_action(self, state):
   20        -        robot = self._one(state, "crv_robot")
   21        -        block = self._one(state, "target_block")
   22        -        surface = self._one(state, "target_surface")
          31 +        robot = state.get_objects(self.types["crv_robot"])[0]
          32 +        surface = state.get_objects(self.types["target_surface"])[0]
   23     33          rx, ry = state.get(robot, "x"), state.get(robot, "y")
   24     34          theta = state.get(robot, "theta")
   25        -        arm = state.get(robot, "arm_joint")
   26        -        vacuum = state.get(robot, "vacuum")
   27        -        bx, by = state.get(block, "x"), state.get(block, "y")
   28        -        sx, sy = state.get(surface, "x"), state.get(surface, "y")
          35 +        if self.index >= len(self.todo):
          36 +            return self._action()
          37 +        obj = state.get_object_from_name(self.todo[self.index])
          38 +        is_target = obj.type.name == "target_block"
          39 +        ox, oy = state.get(obj, "x"), state.get(obj, "y")
          40 +        width = state.get(obj, "width")
   29     41  
   30        -        # First baseline: approach/grasp the block, then translate it to the surface.
   31        -        carrying = vacuum > 0.5 and math.hypot(bx - sx, by - sy) > 0.03
   32        -        tx, ty = (sx, sy) if carrying else (bx, by)
   33        -        desired = math.atan2(ty - ry, tx - rx)
   34        -        err = (desired - theta + math.pi) % (2 * math.pi) - math.pi
   35        -        dist = math.hypot(tx - rx, ty - ry)
   36        -        target_arm = max(0.0, dist - 0.02)
   37        -        action = np.zeros(5, dtype=np.float32)
   38        -        if abs(err) > 0.05:
   39        -            action[2] = np.clip(err, -0.196, 0.196)
   40        -        else:
   41        -            action[3] = np.clip(target_arm - arm, -0.1, 0.1)
   42        -        action[4] = 1.0
   43        -        return np.clip(action, self.action_space.low, self.action_space.high).astype(np.float32)
          42 +        if self.phase == "orient":
          43 +            err = (-math.pi / 2 - theta + math.pi) % (2 * math.pi) - math.pi
          44 +            if abs(err) < 0.025:
          45 +                self.phase = "rise"
          46 +            else:
          47 +                return self._action(dtheta=self._clip(err, 0.196))
          48 +        if self.phase == "rise":
          49 +            if ry >= 0.88:
          50 +                self.phase = "align"
          51 +            else:
          52 +                return self._action(dy=min(0.05, 0.9 - ry))
          53 +        if self.phase == "align":
          54 +            offsets = (0.0, -0.22, 0.22, -0.38, 0.38)
          55 +            tx = ox + offsets[min(self.retry, 4)] * width
          56 +            if abs(tx - rx) < 0.004:
          57 +                self.phase, self.stalled = "descend", 0
          58 +                self.last_robot_y, self.pick_y = ry, oy
          59 +            else:
          60 +                return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
          61 +        if self.phase == "descend":
          62 +            if self.last_robot_y is not None and abs(ry - self.last_robot_y) < 0.001:
          63 +                self.stalled += 1
          64 +            else:
          65 +                self.stalled = 0
          66 +            self.last_robot_y = ry
          67 +            if self.stalled >= 2 or ry < 0.18:
          68 +                self.phase = "lift"
          69 +            else:
          70 +                return self._action(dy=-0.05, vac=1.0)
          71 +        if self.phase == "lift":
          72 +            if oy > self.pick_y + 0.015:
          73 +                self.attached = True
          74 +            if ry < 0.79:
          75 +                return self._action(dy=0.05, vac=1.0)
          76 +            if not self.attached:
          77 +                self.retry += 1
          78 +                if self.retry < 5:
          79 +                    self.phase = "align"
          80 +                    return self._action()
          81 +                if not is_target:
          82 +                    self.index += 1
          83 +                    self.retry = 0
          84 +                    self.phase = "rise"
          85 +                    return self._action()
          86 +                self.retry, self.phase = 0, "align"
          87 +                return self._action()
          88 +            self.phase = "carry"
          89 +        if self.phase == "carry":
          90 +            tx = state.get(surface, "x") if is_target else self.park_base + 0.24 * self.index
          91 +            if abs(tx - rx) > 0.004:
          92 +                return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
          93 +            self.phase = "lower" if is_target else "release"
          94 +            self.stalled, self.last_robot_y = 0, ry
          95 +        if self.phase == "lower":
          96 +            if abs(ry - self.last_robot_y) < 0.001:
          97 +                self.stalled += 1
          98 +            else:
          99 +                self.stalled = 0
         100 +            self.last_robot_y = ry
         101 +            if self.stalled >= 3:
         102 +                self.phase = "release"
         103 +            else:
         104 +                return self._action(dy=-0.05, vac=1.0)
         105 +        if self.phase == "release":
         106 +            self.release_wait += 1
         107 +            if self.release_wait < 2:
         108 +                return self._action()
         109 +            self.phase = "retreat"
         110 +        if self.phase == "retreat":
         111 +            if ry < 0.89:
         112 +                return self._action(dy=0.05)
         113 +            self.index += 1
         114 +            self.retry, self.attached, self.release_wait = 0, False, 0
         115 +            self.phase = "align" if self.index < len(self.todo) else "done"
         116 +            return self._action()
         117 +        return self._action()
diff --git a/test_approach.py b/test_approach.py
index 813912b..3d70199 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -16,7 +16,7 @@ def run(seed, verbose=False):
   16     16      term = trunc = False
   17     17      steps = 0
   18     18      try:
   19        -        while not (term or trunc):
          19 +        while not (term or trunc) and steps < env.max_steps:
   20     20              action = approach.get_action(state)
   21     21              state, reward, term, trunc, info = env.step(action)
   22     22              steps += 1
```

</details>

<a id="C005"></a>
<a id="R02"></a>
### C005 · Use reset pose as reachable safe travel height

Commit `55d3dab50b9384cb12ec258ecb24aa218841153b`; parents: 670d6a3f67570639f5110b2d2c6590347bc3fe13. Recorded author date: 2026-09-08T22:25:07+02:00.

File roles (automatic): policy.

- [E0094](01_timeline.md#E0094): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Robot stays in the rise phase → use its initial height as the reachable travel height.


Prior mapped context: [E0079](01_timeline.md#E0079), [E0084](01_timeline.md#E0084), [E0088](01_timeline.md#E0088), [E0090](01_timeline.md#E0090), [E0092](01_timeline.md#E0092), [E0094](01_timeline.md#E0094).

Prior mapped post-edit test reports: [E0094](01_timeline.md#E0094), [E0099](01_timeline.md#E0099). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C005_55d3dab_approach.py) · [Exact all-file diff](evidence/diffs/C005_55d3dab.diff)

[Previous saved controller snapshot](evidence/versions/C004_670d6a3_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9d7d605..53de72b 100644
--- a/approach.py
+++ b/approach.py
@@ -15,6 +15,8 @@ class GeneratedApproach:
   15     15          self.todo.append(state.get_objects(self.types["target_block"])[0].name)
   16     16          xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
   17     17          self.park_base = max(xs) + 0.45
          18 +        robot = state.get_objects(self.types["crv_robot"])[0]
          19 +        self.safe_y = state.get(robot, "y")
   18     20          self.index, self.phase, self.retry = 0, "orient", 0
   19     21          self.stalled, self.last_robot_y = 0, None
   20     22          self.pick_y, self.attached, self.release_wait = 0.0, False, 0
@@ -46,10 +48,10 @@ class GeneratedApproach:
   46     48              else:
   47     49                  return self._action(dtheta=self._clip(err, 0.196))
   48     50          if self.phase == "rise":
   49        -            if ry >= 0.88:
          51 +            if ry >= self.safe_y - 0.004:
   50     52                  self.phase = "align"
   51     53              else:
   52        -                return self._action(dy=min(0.05, 0.9 - ry))
          54 +                return self._action(dy=min(0.05, self.safe_y - ry))
   53     55          if self.phase == "align":
   54     56              offsets = (0.0, -0.22, 0.22, -0.38, 0.38)
   55     57              tx = ox + offsets[min(self.retry, 4)] * width
@@ -108,7 +110,7 @@ class GeneratedApproach:
  108    110                  return self._action()
  109    111              self.phase = "retreat"
  110    112          if self.phase == "retreat":
  111        -            if ry < 0.89:
         113 +            if ry < self.safe_y - 0.004:
  112    114                  return self._action(dy=0.05)
  113    115              self.index += 1
  114    116              self.retry, self.attached, self.release_wait = 0, False, 0
```

</details>

<a id="C006"></a>
<a id="R03"></a>
### C006 · Park all movable objects tallest-first before final placement

Commit `98c6f0752efb322c7bcf1f6f351d8d1d9f09ef37`; parents: 55d3dab50b9384cb12ec258ecb24aa218841153b. Recorded author date: 2026-09-08T22:26:54+02:00.

File roles (automatic): policy.

- [E0106](01_timeline.md#E0106): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Multi-object cases still fail → reorder rectangles tallest first and include an initial target-clearing pass.


Prior mapped context: [E0094](01_timeline.md#E0094), [E0099](01_timeline.md#E0099), [E0102](01_timeline.md#E0102), [E0104](01_timeline.md#E0104), [E0106](01_timeline.md#E0106).

Prior mapped post-edit test reports: [E0106](01_timeline.md#E0106). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C006_98c6f07_approach.py) · [Exact all-file diff](evidence/diffs/C006_98c6f07.diff)

[Previous saved controller snapshot](evidence/versions/C005_55d3dab_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 53de72b..6611f2e 100644
--- a/approach.py
+++ b/approach.py
@@ -10,9 +10,13 @@ class GeneratedApproach:
   10     10  
   11     11      def reset(self, state, info):
   12     12          rects = state.get_objects(self.types["rectangle"])
   13        -        self.todo = [o.name for o in rects if o.type.name == "rectangle"]
   14        -        self.todo.sort(key=lambda n: state.get(state.get_object_from_name(n), "height"))
   15        -        self.todo.append(state.get_objects(self.types["target_block"])[0].name)
          13 +        # Park every movable rectangle, tallest first.  Including the target in
          14 +        # this clearing pass matters when it physically shields a shorter object.
          15 +        self.todo = [o.name for o in rects]
          16 +        self.todo.sort(key=lambda n: -state.get(state.get_object_from_name(n), "height"))
          17 +        target_name = state.get_objects(self.types["target_block"])[0].name
          18 +        self.todo.append(target_name)  # retrieve it last for the actual placement
          19 +        self.final_index = len(self.todo) - 1
   16     20          xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
   17     21          self.park_base = max(xs) + 0.45
   18     22          robot = state.get_objects(self.types["crv_robot"])[0]
@@ -37,7 +41,7 @@ class GeneratedApproach:
   37     41          if self.index >= len(self.todo):
   38     42              return self._action()
   39     43          obj = state.get_object_from_name(self.todo[self.index])
   40        -        is_target = obj.type.name == "target_block"
          44 +        is_target = self.index == self.final_index
   41     45          ox, oy = state.get(obj, "x"), state.get(obj, "y")
   42     46          width = state.get(obj, "width")
   43     47  
```

</details>

<a id="C007"></a>
<a id="R04"></a>
### C007 · Exclude static surface and park cleared objects vertically

Commit `6d93a7d48faa104e1329e4bfaefa94efecba66e8`; parents: 98c6f0752efb322c7bcf1f6f351d8d1d9f09ef37. Recorded author date: 2026-09-08T22:27:43+02:00.

File roles (automatic): policy.

- [E0112](01_timeline.md#E0112): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Printed task list includes the static surface and motion stalls → filter static objects and park vertically in place.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0106](01_timeline.md#E0106), [E0108](01_timeline.md#E0108), [E0110](01_timeline.md#E0110), [E0112](01_timeline.md#E0112).

Prior mapped post-edit test reports: [E0112](01_timeline.md#E0112). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C007_6d93a7d_approach.py) · [Exact all-file diff](evidence/diffs/C007_6d93a7d.diff)

[Previous saved controller snapshot](evidence/versions/C006_98c6f07_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6611f2e..7e46a61 100644
--- a/approach.py
+++ b/approach.py
@@ -12,7 +12,7 @@ class GeneratedApproach:
   12     12          rects = state.get_objects(self.types["rectangle"])
   13     13          # Park every movable rectangle, tallest first.  Including the target in
   14     14          # this clearing pass matters when it physically shields a shorter object.
   15        -        self.todo = [o.name for o in rects]
          15 +        self.todo = [o.name for o in rects if state.get(o, "static") < 0.5]
   16     16          self.todo.sort(key=lambda n: -state.get(state.get_object_from_name(n), "height"))
   17     17          target_name = state.get_objects(self.types["target_block"])[0].name
   18     18          self.todo.append(target_name)  # retrieve it last for the actual placement
@@ -93,7 +93,8 @@ class GeneratedApproach:
   93     93                  return self._action()
   94     94              self.phase = "carry"
   95     95          if self.phase == "carry":
   96        -            tx = state.get(surface, "x") if is_target else self.park_base + 0.24 * self.index
          96 +            # Parking vertically in place avoids unknown horizontal world bounds.
          97 +            tx = state.get(surface, "x") if is_target else ox
   97     98              if abs(tx - rx) > 0.004:
   98     99                  return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
   99    100              self.phase = "lower" if is_target else "release"
```

</details>

<a id="C008"></a>
<a id="R05"></a>
### C008 · Keep vacuum off during horizontal transit

Commit `e727013d4d32a19467cdd4c7261b1df1a117e9c0`; parents: 6d93a7d48faa104e1329e4bfaefa94efecba66e8. Recorded author date: 2026-09-08T22:28:29+02:00.

File roles (automatic): policy.

- [E0118](01_timeline.md#E0118): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Target moves while the robot travels toward another object → turn vacuum off during horizontal alignment.


Prior mapped context: [E0112](01_timeline.md#E0112), [E0114](01_timeline.md#E0114), [E0116](01_timeline.md#E0116), [E0118](01_timeline.md#E0118).

Prior mapped post-edit test reports: [E0118](01_timeline.md#E0118). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C008_e727013_approach.py) · [Exact all-file diff](evidence/diffs/C008_e727013.diff)

[Previous saved controller snapshot](evidence/versions/C007_6d93a7d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7e46a61..29d42fb 100644
--- a/approach.py
+++ b/approach.py
@@ -63,7 +63,9 @@ class GeneratedApproach:
   63     63                  self.phase, self.stalled = "descend", 0
   64     64                  self.last_robot_y, self.pick_y = ry, oy
   65     65              else:
   66        -                return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
          66 +                # Keep suction off in transit: a previously parked object may
          67 +                # touch the gripper as it passes underneath.
          68 +                return self._action(dx=self._clip(tx - rx, 0.05), vac=0.0)
   67     69          if self.phase == "descend":
   68     70              if self.last_robot_y is not None and abs(ry - self.last_robot_y) < 0.001:
   69     71                  self.stalled += 1
```

</details>

<a id="C009"></a>
<a id="R06"></a>
### C009 · Park cleared objects low enough for later regrasp

Commit `5a9cda57e55c37dceaa8c7ddd7ec4813ed4b1916`; parents: e727013d4d32a19467cdd4c7261b1df1a117e9c0. Recorded author date: 2026-09-08T22:29:11+02:00.

File roles (automatic): policy.

- [E0124](01_timeline.md#E0124): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Objects remain high and the target cannot be regrasped → stop preliminary lifts at a lower parking height.


Prior mapped context: [E0118](01_timeline.md#E0118), [E0120](01_timeline.md#E0120), [E0122](01_timeline.md#E0122), [E0124](01_timeline.md#E0124).

Prior mapped post-edit test reports: [E0124](01_timeline.md#E0124). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C009_5a9cda5_approach.py) · [Exact all-file diff](evidence/diffs/C009_5a9cda5.diff)

[Previous saved controller snapshot](evidence/versions/C008_e727013_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 29d42fb..86b23ab 100644
--- a/approach.py
+++ b/approach.py
@@ -79,7 +79,10 @@ class GeneratedApproach:
   79     79          if self.phase == "lift":
   80     80              if oy > self.pick_y + 0.015:
   81     81                  self.attached = True
   82        -            if ry < 0.79:
          82 +            # A modest vertical park is enough to clear the ground while still
          83 +            # leaving room above it for a later verified re-grasp.
          84 +            parked_high_enough = (not is_target and self.attached and oy >= 0.35)
          85 +            if ry < 0.79 and not parked_high_enough:
   83     86                  return self._action(dy=0.05, vac=1.0)
   84     87              if not self.attached:
   85     88                  self.retry += 1
```

</details>

<a id="C010"></a>
<a id="R07"></a>
### C010 · Park obstructions laterally away from target surface

Commit `f214f7da0b2fc28156025e7d0c4e852164646ce7`; parents: 5a9cda57e55c37dceaa8c7ddd7ec4813ed4b1916. Recorded author date: 2026-09-08T22:30:02+02:00.

File roles (automatic): policy.

- [E0130](01_timeline.md#E0130): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Controller finishes but placement fails → move obstructions laterally away from the surface.


Prior mapped context: [E0124](01_timeline.md#E0124), [E0126](01_timeline.md#E0126), [E0128](01_timeline.md#E0128), [E0130](01_timeline.md#E0130).

Prior mapped post-edit test reports: [E0130](01_timeline.md#E0130), [E0132](01_timeline.md#E0132). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C010_f214f7d_approach.py) · [Exact all-file diff](evidence/diffs/C010_f214f7d.diff)

[Previous saved controller snapshot](evidence/versions/C009_5a9cda5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 86b23ab..0db84ac 100644
--- a/approach.py
+++ b/approach.py
@@ -98,8 +98,16 @@ class GeneratedApproach:
   98     98                  return self._action()
   99     99              self.phase = "carry"
  100    100          if self.phase == "carry":
  101        -            # Parking vertically in place avoids unknown horizontal world bounds.
  102        -            tx = state.get(surface, "x") if is_target else ox
         101 +            if is_target:
         102 +                tx = state.get(surface, "x")
         103 +            elif obj.type.name == "target_block":
         104 +                tx = ox
         105 +            else:
         106 +                sx = state.get(surface, "x")
         107 +                direction = 1.0 if ox >= sx else -1.0
         108 +                tx = ox + direction * (0.25 + 0.08 * self.index)
         109 +                # Empirically the circular base center is constrained here.
         110 +                tx = max(0.11, min(1.39, tx))
  103    111              if abs(tx - rx) > 0.004:
  104    112                  return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
  105    113              self.phase = "lower" if is_target else "release"
```

</details>

<a id="C011"></a>
<a id="R08"></a>
### C011 · Only pre-park target when it blocks obstacle access

Commit `dd0457e1ab7a6650cc3d3d9588c689fae71ca45b`; parents: f214f7da0b2fc28156025e7d0c4e852164646ce7. Recorded author date: 2026-09-08T22:32:29+02:00.

File roles (automatic): policy.

- [E0144](01_timeline.md#E0144): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Broader tests mostly fail → temporarily move the target only when the geometry is crowded.


Prior mapped context: [E0132](01_timeline.md#E0132), [E0136](01_timeline.md#E0136), [E0138](01_timeline.md#E0138), [E0140](01_timeline.md#E0140), [E0142](01_timeline.md#E0142), [E0144](01_timeline.md#E0144).

Prior mapped post-edit test reports: [E0144](01_timeline.md#E0144). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C011_dd0457e_approach.py) · [Exact all-file diff](evidence/diffs/C011_dd0457e.diff)

[Previous saved controller snapshot](evidence/versions/C010_f214f7d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0db84ac..eabaca3 100644
--- a/approach.py
+++ b/approach.py
@@ -10,11 +10,15 @@ class GeneratedApproach:
   10     10  
   11     11      def reset(self, state, info):
   12     12          rects = state.get_objects(self.types["rectangle"])
   13        -        # Park every movable rectangle, tallest first.  Including the target in
   14        -        # this clearing pass matters when it physically shields a shorter object.
   15        -        self.todo = [o.name for o in rects if state.get(o, "static") < 0.5]
   16        -        self.todo.sort(key=lambda n: -state.get(state.get_object_from_name(n), "height"))
   17     13          target_name = state.get_objects(self.types["target_block"])[0].name
          14 +        target = state.get_object_from_name(target_name)
          15 +        obstacles = [o for o in rects if o.type.name == "rectangle" and state.get(o, "static") < 0.5]
          16 +        obstacles.sort(key=lambda o: -state.get(o, "height"))
          17 +        # Temporarily lift the target only when it crowds an obstacle's access.
          18 +        tx, tw = state.get(target, "x"), state.get(target, "width")
          19 +        crowded = any(abs(tx - state.get(o, "x")) <
          20 +                      0.5 * (tw + state.get(o, "width")) + 0.14 for o in obstacles)
          21 +        self.todo = ([target_name] if crowded else []) + [o.name for o in obstacles]
   18     22          self.todo.append(target_name)  # retrieve it last for the actual placement
   19     23          self.final_index = len(self.todo) - 1
   20     24          xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
```

</details>

<a id="C012"></a>
<a id="R09"></a>
### C012 · Fix moving-goal bug in obstruction carry phase

Commit `3f73fd4d1be28fdc416adf4ded51401d96f74aae`; parents: dd0457e1ab7a6650cc3d3d9588c689fae71ca45b. Recorded author date: 2026-09-08T22:33:21+02:00.

File roles (automatic): policy.

- [E0150](01_timeline.md#E0150): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Failure persists with a moving obstruction destination → calculate that destination from the initial object position.


Prior mapped context: [E0144](01_timeline.md#E0144), [E0146](01_timeline.md#E0146), [E0148](01_timeline.md#E0148), [E0150](01_timeline.md#E0150).

Prior mapped post-edit test reports: [E0150](01_timeline.md#E0150), [E0163](01_timeline.md#E0163). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C012_3f73fd4_approach.py) · [Exact all-file diff](evidence/diffs/C012_3f73fd4.diff)

[Previous saved controller snapshot](evidence/versions/C011_dd0457e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index eabaca3..3db40ed 100644
--- a/approach.py
+++ b/approach.py
@@ -22,6 +22,8 @@ class GeneratedApproach:
   22     22          self.todo.append(target_name)  # retrieve it last for the actual placement
   23     23          self.final_index = len(self.todo) - 1
   24     24          xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
          25 +        self.initial_x = {n: state.get(state.get_object_from_name(n), "x")
          26 +                          for n in state.get_object_names()}
   25     27          self.park_base = max(xs) + 0.45
   26     28          robot = state.get_objects(self.types["crv_robot"])[0]
   27     29          self.safe_y = state.get(robot, "y")
@@ -108,8 +110,9 @@ class GeneratedApproach:
  108    110                  tx = ox
  109    111              else:
  110    112                  sx = state.get(surface, "x")
  111        -                direction = 1.0 if ox >= sx else -1.0
  112        -                tx = ox + direction * (0.25 + 0.08 * self.index)
         113 +                origin_x = self.initial_x[obj.name]
         114 +                direction = 1.0 if origin_x >= sx else -1.0
         115 +                tx = origin_x + direction * (0.25 + 0.08 * self.index)
  113    116                  # Empirically the circular base center is constrained here.
  114    117                  tx = max(0.11, min(1.39, tx))
  115    118              if abs(tx - rx) > 0.004:
```

</details>

<a id="C013"></a>
<a id="R10"></a>
### C013 · Use lower carry height to match successful placement trajectory

Commit `735b56a0e4dd843040001a7b0a134945b773f4c3`; parents: 3f73fd4d1be28fdc416adf4ded51401d96f74aae. Recorded author date: 2026-09-08T22:37:34+02:00.

File roles (automatic): policy.

- [E0177](01_timeline.md#E0177): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Program placement fails despite a successful hand-scripted placement probe → lower the carry-height threshold.


Prior mapped context: [E0150](01_timeline.md#E0150), [E0152](01_timeline.md#E0152), [E0154](01_timeline.md#E0154), [E0155](01_timeline.md#E0155), [E0157](01_timeline.md#E0157), [E0163](01_timeline.md#E0163), [E0165](01_timeline.md#E0165), [E0167](01_timeline.md#E0167), [E0169](01_timeline.md#E0169), [E0171](01_timeline.md#E0171), [E0173](01_timeline.md#E0173), [E0175](01_timeline.md#E0175), [E0177](01_timeline.md#E0177).

Prior mapped post-edit test reports: [E0177](01_timeline.md#E0177). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C013_735b56a_approach.py) · [Exact all-file diff](evidence/diffs/C013_735b56a.diff)

[Previous saved controller snapshot](evidence/versions/C012_3f73fd4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3db40ed..ad4f3c6 100644
--- a/approach.py
+++ b/approach.py
@@ -88,7 +88,7 @@ class GeneratedApproach:
   88     88              # A modest vertical park is enough to clear the ground while still
   89     89              # leaving room above it for a later verified re-grasp.
   90     90              parked_high_enough = (not is_target and self.attached and oy >= 0.35)
   91        -            if ry < 0.79 and not parked_high_enough:
          91 +            if ry < 0.74 and not parked_high_enough:
   92     92                  return self._action(dy=0.05, vac=1.0)
   93     93              if not self.attached:
   94     94                  self.retry += 1
```

</details>

<a id="C014"></a>
<a id="R11"></a>
### C014 · Bias final placement slightly inside successful support region

Commit `b15ba765819745483cd25351bc231630e3c5f39b`; parents: 735b56a0e4dd843040001a7b0a134945b773f4c3. Recorded author date: 2026-09-08T22:38:02+02:00.

File roles (automatic): policy.

- [E0181](01_timeline.md#E0181): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Lower carry height does not solve seed 1 → add a small horizontal offset to final placement.


Prior mapped context: [E0177](01_timeline.md#E0177), [E0179](01_timeline.md#E0179), [E0181](01_timeline.md#E0181).

Prior mapped post-edit test reports: [E0181](01_timeline.md#E0181), [E0183](01_timeline.md#E0183). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C014_b15ba76_approach.py) · [Exact all-file diff](evidence/diffs/C014_b15ba76.diff)

[Previous saved controller snapshot](evidence/versions/C013_735b56a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ad4f3c6..3c76b6b 100644
--- a/approach.py
+++ b/approach.py
@@ -105,7 +105,7 @@ class GeneratedApproach:
  105    105              self.phase = "carry"
  106    106          if self.phase == "carry":
  107    107              if is_target:
  108        -                tx = state.get(surface, "x")
         108 +                tx = state.get(surface, "x") + 0.008
  109    109              elif obj.type.name == "target_block":
  110    110                  tx = ox
  111    111              else:
```

</details>

<a id="C015"></a>
<a id="R12"></a>
### C015 · Use fine vertical steps so vacuum reaches contact

Commit `af4477f6256966431e7a90dc3f715263ad6b6895`; parents: b15ba765819745483cd25351bc231630e3c5f39b. Recorded author date: 2026-09-08T22:39:24+02:00.

File roles (automatic): policy.

- [E0193](01_timeline.md#E0193): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Several grasp cases fail; a fine-step probe lifts them → reduce downward steps from 0.05 to 0.01.


Prior mapped context: [E0183](01_timeline.md#E0183), [E0185](01_timeline.md#E0185), [E0187](01_timeline.md#E0187), [E0189](01_timeline.md#E0189), [E0191](01_timeline.md#E0191), [E0193](01_timeline.md#E0193).

Prior mapped post-edit test reports: [E0193](01_timeline.md#E0193). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C015_af4477f_approach.py) · [Exact all-file diff](evidence/diffs/C015_af4477f.diff)

[Previous saved controller snapshot](evidence/versions/C014_b15ba76_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3c76b6b..ceb03a5 100644
--- a/approach.py
+++ b/approach.py
@@ -81,7 +81,9 @@ class GeneratedApproach:
   81     81              if self.stalled >= 2 or ry < 0.18:
   82     82                  self.phase = "lift"
   83     83              else:
   84        -                return self._action(dy=-0.05, vac=1.0)
          84 +                # Fine approach is essential: collision resolution rejects an
          85 +                # overshooting move wholesale, leaving the vacuum just off-contact.
          86 +                return self._action(dy=-0.01, vac=1.0)
   85     87          if self.phase == "lift":
   86     88              if oy > self.pick_y + 0.015:
   87     89                  self.attached = True
@@ -128,7 +130,7 @@ class GeneratedApproach:
  128    130              if self.stalled >= 3:
  129    131                  self.phase = "release"
  130    132              else:
  131        -                return self._action(dy=-0.05, vac=1.0)
         133 +                return self._action(dy=-0.01, vac=1.0)
  132    134          if self.phase == "release":
  133    135              self.release_wait += 1
  134    136              if self.release_wait < 2:
```

</details>

<a id="C016"></a>
<a id="R13"></a>
### C016 · Avoid overshooting ceiling during retreat

Commit `9c6bdf4aadd4fb0898c37109aaacae340556bc9d`; parents: af4477f6256966431e7a90dc3f715263ad6b6895. Recorded author date: 2026-09-08T22:40:21+02:00.

File roles (automatic): policy.

- [E0201](01_timeline.md#E0201): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Robot stalls in retreat below its requested height → cap the upward step at the remaining height.


Prior mapped context: [E0193](01_timeline.md#E0193), [E0195](01_timeline.md#E0195), [E0197](01_timeline.md#E0197), [E0199](01_timeline.md#E0199), [E0201](01_timeline.md#E0201).

Prior mapped post-edit test reports: [E0201](01_timeline.md#E0201). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C016_9c6bdf4_approach.py) · [Exact all-file diff](evidence/diffs/C016_9c6bdf4.diff)

[Previous saved controller snapshot](evidence/versions/C015_af4477f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ceb03a5..81cc7e9 100644
--- a/approach.py
+++ b/approach.py
@@ -138,7 +138,7 @@ class GeneratedApproach:
  138    138              self.phase = "retreat"
  139    139          if self.phase == "retreat":
  140    140              if ry < self.safe_y - 0.004:
  141        -                return self._action(dy=0.05)
         141 +                return self._action(dy=min(0.05, self.safe_y - ry))
  142    142              self.index += 1
  143    143              self.retry, self.attached, self.release_wait = 0, False, 0
  144    144              self.phase = "align" if self.index < len(self.todo) else "done"
```

</details>

<a id="C017"></a>
<a id="R14"></a>
### C017 · Park blockers away from target and handle travel bounds

Commit `4f80855d9224b4217f437fe0af644a140c1f0ee2`; parents: 9c6bdf4aadd4fb0898c37109aaacae340556bc9d. Recorded author date: 2026-09-08T22:41:31+02:00.

File roles (automatic): policy.

- [E0207](01_timeline.md#E0207): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Target access and boundary cases remain → change parking direction and detect stalled horizontal carrying.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0201](01_timeline.md#E0201), [E0203](01_timeline.md#E0203), [E0205](01_timeline.md#E0205), [E0207](01_timeline.md#E0207).

Prior mapped post-edit test reports: [E0207](01_timeline.md#E0207). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C017_4f80855_approach.py) · [Exact all-file diff](evidence/diffs/C017_4f80855.diff)

[Previous saved controller snapshot](evidence/versions/C016_9c6bdf4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 81cc7e9..d2beb3c 100644
--- a/approach.py
+++ b/approach.py
@@ -29,6 +29,7 @@ class GeneratedApproach:
   29     29          self.safe_y = state.get(robot, "y")
   30     30          self.index, self.phase, self.retry = 0, "orient", 0
   31     31          self.stalled, self.last_robot_y = 0, None
          32 +        self.last_robot_x = None
   32     33          self.pick_y, self.attached, self.release_wait = 0.0, False, 0
   33     34  
   34     35      @staticmethod
@@ -105,21 +106,30 @@ class GeneratedApproach:
  105    106                  self.retry, self.phase = 0, "align"
  106    107                  return self._action()
  107    108              self.phase = "carry"
         109 +            self.stalled, self.last_robot_x = 0, rx
  108    110          if self.phase == "carry":
  109    111              if is_target:
  110    112                  tx = state.get(surface, "x") + 0.008
  111    113              elif obj.type.name == "target_block":
  112    114                  tx = ox
  113    115              else:
  114        -                sx = state.get(surface, "x")
  115    116                  origin_x = self.initial_x[obj.name]
  116        -                direction = 1.0 if origin_x >= sx else -1.0
  117        -                tx = origin_x + direction * (0.25 + 0.08 * self.index)
  118        -                # Empirically the circular base center is constrained here.
  119        -                tx = max(0.11, min(1.39, tx))
         117 +                target_name = state.get_objects(self.types["target_block"])[0].name
         118 +                target_x = self.initial_x[target_name]
         119 +                direction = 1.0 if origin_x >= target_x else -1.0
         120 +                tx = origin_x + direction * (0.25 + 0.12 * self.index)
  120    121              if abs(tx - rx) > 0.004:
  121        -                return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
  122        -            self.phase = "lower" if is_target else "release"
         122 +                if self.last_robot_x is not None and abs(rx - self.last_robot_x) < 0.001:
         123 +                    self.stalled += 1
         124 +                else:
         125 +                    self.stalled = 0
         126 +                self.last_robot_x = rx
         127 +                if self.stalled >= 3 and not is_target:
         128 +                    self.phase = "release"
         129 +                else:
         130 +                    return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
         131 +            else:
         132 +                self.phase = "lower" if is_target else "release"
  123    133              self.stalled, self.last_robot_y = 0, ry
  124    134          if self.phase == "lower":
  125    135              if abs(ry - self.last_robot_y) < 0.001:
```

</details>

<a id="C018"></a>
<a id="R15"></a>
### C018 · Vertically separate parked blockers and recover at walls

Commit `2d184c4bbc2637d77149742952c1c642ee1ec79f`; parents: 4f80855d9224b4217f437fe0af644a140c1f0ee2. Recorded author date: 2026-09-08T22:42:36+02:00.

File roles (automatic): policy.

- [E0213](01_timeline.md#E0213): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Failures remain after new parking rule → vary parking heights and add stalled-alignment recovery.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0207](01_timeline.md#E0207), [E0209](01_timeline.md#E0209), [E0211](01_timeline.md#E0211), [E0213](01_timeline.md#E0213).

Prior mapped post-edit test reports: [E0213](01_timeline.md#E0213). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C018_2d184c4_approach.py) · [Exact all-file diff](evidence/diffs/C018_2d184c4.diff)

[Previous saved controller snapshot](evidence/versions/C017_4f80855_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d2beb3c..06e44f9 100644
--- a/approach.py
+++ b/approach.py
@@ -70,6 +70,14 @@ class GeneratedApproach:
   70     70                  self.phase, self.stalled = "descend", 0
   71     71                  self.last_robot_y, self.pick_y = ry, oy
   72     72              else:
          73 +                if self.last_robot_x is not None and abs(rx - self.last_robot_x) < 0.001:
          74 +                    self.stalled += 1
          75 +                else:
          76 +                    self.stalled = 0
          77 +                self.last_robot_x = rx
          78 +                if self.stalled >= 3:
          79 +                    self.retry = min(4, self.retry + 1)
          80 +                    self.stalled = 0
   73     81                  # Keep suction off in transit: a previously parked object may
   74     82                  # touch the gripper as it passes underneath.
   75     83                  return self._action(dx=self._clip(tx - rx, 0.05), vac=0.0)
@@ -90,7 +98,8 @@ class GeneratedApproach:
   90     98                  self.attached = True
   91     99              # A modest vertical park is enough to clear the ground while still
   92    100              # leaving room above it for a later verified re-grasp.
   93        -            parked_high_enough = (not is_target and self.attached and oy >= 0.35)
         101 +            park_y = 0.35 if obj.type.name == "target_block" else max(0.38, 0.55 - 0.10 * self.index)
         102 +            parked_high_enough = (not is_target and self.attached and oy >= park_y)
   94    103              if ry < 0.74 and not parked_high_enough:
   95    104                  return self._action(dy=0.05, vac=1.0)
   96    105              if not self.attached:
@@ -151,6 +160,7 @@ class GeneratedApproach:
  151    160                  return self._action(dy=min(0.05, self.safe_y - ry))
  152    161              self.index += 1
  153    162              self.retry, self.attached, self.release_wait = 0, False, 0
         163 +            self.last_robot_x = None
  154    164              self.phase = "align" if self.index < len(self.todo) else "done"
  155    165              return self._action()
  156    166          return self._action()
```

</details>

<a id="C019"></a>
<a id="R16"></a>
### C019 · Park blockers far outside surface at low clearance height

Commit `0c006f7a4edc8218bdfe1b95ba5a08070d037461`; parents: 2d184c4bbc2637d77149742952c1c642ee1ec79f. Recorded author date: 2026-09-08T22:44:30+02:00.

File roles (automatic): policy.

- [E0221](01_timeline.md#E0221): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Objects still obstruct target movement → return to lower parking and move blockers farther away from the surface.


Prior mapped context: [E0213](01_timeline.md#E0213), [E0215](01_timeline.md#E0215), [E0217](01_timeline.md#E0217), [E0219](01_timeline.md#E0219), [E0221](01_timeline.md#E0221).

Prior mapped post-edit test reports: [E0221](01_timeline.md#E0221), [E0223](01_timeline.md#E0223). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C019_0c006f7_approach.py) · [Exact all-file diff](evidence/diffs/C019_0c006f7.diff)

[Previous saved controller snapshot](evidence/versions/C018_2d184c4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 06e44f9..ebb8e97 100644
--- a/approach.py
+++ b/approach.py
@@ -98,7 +98,7 @@ class GeneratedApproach:
   98     98                  self.attached = True
   99     99              # A modest vertical park is enough to clear the ground while still
  100    100              # leaving room above it for a later verified re-grasp.
  101        -            park_y = 0.35 if obj.type.name == "target_block" else max(0.38, 0.55 - 0.10 * self.index)
         101 +            park_y = 0.35
  102    102              parked_high_enough = (not is_target and self.attached and oy >= park_y)
  103    103              if ry < 0.74 and not parked_high_enough:
  104    104                  return self._action(dy=0.05, vac=1.0)
@@ -123,10 +123,9 @@ class GeneratedApproach:
  123    123                  tx = ox
  124    124              else:
  125    125                  origin_x = self.initial_x[obj.name]
  126        -                target_name = state.get_objects(self.types["target_block"])[0].name
  127        -                target_x = self.initial_x[target_name]
  128        -                direction = 1.0 if origin_x >= target_x else -1.0
  129        -                tx = origin_x + direction * (0.25 + 0.12 * self.index)
         126 +                surface_x = state.get(surface, "x")
         127 +                direction = 1.0 if origin_x >= surface_x else -1.0
         128 +                tx = origin_x + direction * (0.45 + 0.12 * self.index)
  130    129              if abs(tx - rx) > 0.004:
  131    130                  if self.last_robot_x is not None and abs(rx - self.last_robot_x) < 0.001:
  132    131                      self.stalled += 1
```

</details>

<a id="C020"></a>
<a id="R17"></a>
### C020 · Add edge grasps and compensate carried-object offset

Commit `adf84aecab53f3d90cca1baf8247a94fa7adcbb5`; parents: 0c006f7a4edc8218bdfe1b95ba5a08070d037461. Recorded author date: 2026-09-08T22:46:18+02:00.

File roles (automatic): policy.

- [E0229](01_timeline.md#E0229): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Several target pickups remain blocked → expand grasp offsets and compensate for the object-to-gripper offset.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0221](01_timeline.md#E0221), [E0223](01_timeline.md#E0223), [E0225](01_timeline.md#E0225), [E0227](01_timeline.md#E0227), [E0229](01_timeline.md#E0229).

Prior mapped post-edit test reports: [E0229](01_timeline.md#E0229). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C020_adf84ae_approach.py) · [Exact all-file diff](evidence/diffs/C020_adf84ae.diff)

[Previous saved controller snapshot](evidence/versions/C019_0c006f7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ebb8e97..6cdca02 100644
--- a/approach.py
+++ b/approach.py
@@ -31,6 +31,7 @@ class GeneratedApproach:
   31     31          self.stalled, self.last_robot_y = 0, None
   32     32          self.last_robot_x = None
   33     33          self.pick_y, self.attached, self.release_wait = 0.0, False, 0
          34 +        self.grasp_dx = 0.0
   34     35  
   35     36      @staticmethod
   36     37      def _clip(v, limit):
@@ -64,8 +65,8 @@ class GeneratedApproach:
   64     65              else:
   65     66                  return self._action(dy=min(0.05, self.safe_y - ry))
   66     67          if self.phase == "align":
   67        -            offsets = (0.0, -0.22, 0.22, -0.38, 0.38)
   68        -            tx = ox + offsets[min(self.retry, 4)] * width
          68 +            offsets = (0.0, -0.22, 0.22, -0.45, 0.45, -0.70, 0.70, -0.90, 0.90)
          69 +            tx = ox + offsets[min(self.retry, len(offsets) - 1)] * width
   69     70              if abs(tx - rx) < 0.004:
   70     71                  self.phase, self.stalled = "descend", 0
   71     72                  self.last_robot_y, self.pick_y = ry, oy
@@ -76,7 +77,7 @@ class GeneratedApproach:
   76     77                      self.stalled = 0
   77     78                  self.last_robot_x = rx
   78     79                  if self.stalled >= 3:
   79        -                    self.retry = min(4, self.retry + 1)
          80 +                    self.retry = min(len(offsets) - 1, self.retry + 1)
   80     81                      self.stalled = 0
   81     82                  # Keep suction off in transit: a previously parked object may
   82     83                  # touch the gripper as it passes underneath.
@@ -95,6 +96,8 @@ class GeneratedApproach:
   95     96                  return self._action(dy=-0.01, vac=1.0)
   96     97          if self.phase == "lift":
   97     98              if oy > self.pick_y + 0.015:
          99 +                if not self.attached:
         100 +                    self.grasp_dx = ox - rx
   98    101                  self.attached = True
   99    102              # A modest vertical park is enough to clear the ground while still
  100    103              # leaving room above it for a later verified re-grasp.
@@ -104,7 +107,7 @@ class GeneratedApproach:
  104    107                  return self._action(dy=0.05, vac=1.0)
  105    108              if not self.attached:
  106    109                  self.retry += 1
  107        -                if self.retry < 5:
         110 +                if self.retry < 9:
  108    111                      self.phase = "align"
  109    112                      return self._action()
  110    113                  if not is_target:
@@ -118,14 +121,15 @@ class GeneratedApproach:
  118    121              self.stalled, self.last_robot_x = 0, rx
  119    122          if self.phase == "carry":
  120    123              if is_target:
  121        -                tx = state.get(surface, "x") + 0.008
         124 +                desired_obj_x = state.get(surface, "x") + 0.008
  122    125              elif obj.type.name == "target_block":
  123        -                tx = ox
         126 +                desired_obj_x = self.initial_x[obj.name]
  124    127              else:
  125    128                  origin_x = self.initial_x[obj.name]
  126    129                  surface_x = state.get(surface, "x")
  127    130                  direction = 1.0 if origin_x >= surface_x else -1.0
  128        -                tx = origin_x + direction * (0.45 + 0.12 * self.index)
         131 +                desired_obj_x = origin_x + direction * (0.45 + 0.12 * self.index)
         132 +            tx = desired_obj_x - self.grasp_dx
  129    133              if abs(tx - rx) > 0.004:
  130    134                  if self.last_robot_x is not None and abs(rx - self.last_robot_x) < 0.001:
  131    135                      self.stalled += 1
```

</details>

<a id="C021"></a>
<a id="R18"></a>
### C021 · Allocate geometry-scored parking slots for blockers

Commit `b7ccec6239e077058e6424854f81fe21a464a3ec`; parents: adf84aecab53f3d90cca1baf8247a94fa7adcbb5. Recorded author date: 2026-09-08T22:48:03+02:00.

File roles (automatic): policy.

- [E0236](01_timeline.md#E0236): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Multi-obstacle parking failures persist → rank candidate parking positions by geometric clearance.


Prior mapped context: [E0229](01_timeline.md#E0229), [E0231](01_timeline.md#E0231), [E0232](01_timeline.md#E0232), [E0234](01_timeline.md#E0234), [E0236](01_timeline.md#E0236).

Prior mapped post-edit test reports: [E0236](01_timeline.md#E0236). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C021_b7ccec6_approach.py) · [Exact all-file diff](evidence/diffs/C021_b7ccec6.diff)

[Previous saved controller snapshot](evidence/versions/C020_adf84ae_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6cdca02..d1d1bce 100644
--- a/approach.py
+++ b/approach.py
@@ -20,6 +20,22 @@ class GeneratedApproach:
   20     20                        0.5 * (tw + state.get(o, "width")) + 0.14 for o in obstacles)
   21     21          self.todo = ([target_name] if crowded else []) + [o.name for o in obstacles]
   22     22          self.todo.append(target_name)  # retrieve it last for the actual placement
          23 +        surface = state.get_objects(self.types["target_surface"])[0]
          24 +        sx, sw = state.get(surface, "x"), state.get(surface, "width")
          25 +        # Greedily reserve floor-clear parking columns, preferring positions far
          26 +        # from both the pickup and goal.  The grid is count-independent.
          27 +        candidates = [0.14 + 0.10 * k for k in range(14)]
          28 +        candidates.sort(key=lambda x: min(abs(x - tx) - tw / 2,
          29 +                                           abs(x - sx) - sw / 2), reverse=True)
          30 +        self.parking = {}
          31 +        used = []
          32 +        for o in obstacles:
          33 +            ow = state.get(o, "width")
          34 +            valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.04
          35 +                                                  for px, pw in used)]
          36 +            px = valid[0] if valid else candidates[len(used) % len(candidates)]
          37 +            self.parking[o.name] = px
          38 +            used.append((px, ow))
   23     39          self.final_index = len(self.todo) - 1
   24     40          xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
   25     41          self.initial_x = {n: state.get(state.get_object_from_name(n), "x")
@@ -125,10 +141,7 @@ class GeneratedApproach:
  125    141              elif obj.type.name == "target_block":
  126    142                  desired_obj_x = self.initial_x[obj.name]
  127    143              else:
  128        -                origin_x = self.initial_x[obj.name]
  129        -                surface_x = state.get(surface, "x")
  130        -                direction = 1.0 if origin_x >= surface_x else -1.0
  131        -                desired_obj_x = origin_x + direction * (0.45 + 0.12 * self.index)
         144 +                desired_obj_x = self.parking[obj.name]
  132    145              tx = desired_obj_x - self.grasp_dx
  133    146              if abs(tx - rx) > 0.004:
  134    147                  if self.last_robot_x is not None and abs(rx - self.last_robot_x) < 0.001:
```

</details>

<a id="C022"></a>
<a id="R19"></a>
### C022 · Reserve a remote slot for temporarily parked target

Commit `0f0c2eeeb0cb14ed5a0b116fa12a266aee349f56`; parents: b7ccec6239e077058e6424854f81fe21a464a3ec. Recorded author date: 2026-09-08T22:49:07+02:00.

File roles (automatic): policy.

- [E0242](01_timeline.md#E0242): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Three regression cases still fail → reserve a remote parking position for the temporarily moved target.


Prior mapped context: [E0236](01_timeline.md#E0236), [E0238](01_timeline.md#E0238), [E0240](01_timeline.md#E0240), [E0242](01_timeline.md#E0242).

Prior mapped post-edit test reports: [E0242](01_timeline.md#E0242). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C022_0f0c2ee_approach.py) · [Exact all-file diff](evidence/diffs/C022_0f0c2ee.diff)

[Previous saved controller snapshot](evidence/versions/C021_b7ccec6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d1d1bce..46bc284 100644
--- a/approach.py
+++ b/approach.py
@@ -29,6 +29,10 @@ class GeneratedApproach:
   29     29                                             abs(x - sx) - sw / 2), reverse=True)
   30     30          self.parking = {}
   31     31          used = []
          32 +        self.target_park = tx
          33 +        if crowded:
          34 +            self.target_park = candidates[0]
          35 +            used.append((self.target_park, tw))
   32     36          for o in obstacles:
   33     37              ow = state.get(o, "width")
   34     38              valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.04
@@ -139,7 +143,7 @@ class GeneratedApproach:
  139    143              if is_target:
  140    144                  desired_obj_x = state.get(surface, "x") + 0.008
  141    145              elif obj.type.name == "target_block":
  142        -                desired_obj_x = self.initial_x[obj.name]
         146 +                desired_obj_x = self.target_park
  143    147              else:
  144    148                  desired_obj_x = self.parking[obj.name]
  145    149              tx = desired_obj_x - self.grasp_dx
```

</details>

<a id="C023"></a>
<a id="R20"></a>
### C023 · Lift final target above all parked blockers

Commit `71c469c4e314a5b175e8c23b683914de11a519e1`; parents: 0f0c2eeeb0cb14ed5a0b116fa12a266aee349f56. Recorded author date: 2026-09-08T22:49:55+02:00.

File roles (automatic): policy.

- [E0248](01_timeline.md#E0248): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 3 stalls while carrying the final target → increase final target carry height.


Prior mapped context: [E0242](01_timeline.md#E0242), [E0244](01_timeline.md#E0244), [E0246](01_timeline.md#E0246), [E0248](01_timeline.md#E0248).

Prior mapped post-edit test reports: [E0248](01_timeline.md#E0248). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C023_71c469c_approach.py) · [Exact all-file diff](evidence/diffs/C023_71c469c.diff)

[Previous saved controller snapshot](evidence/versions/C022_0f0c2ee_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 46bc284..acb24ec 100644
--- a/approach.py
+++ b/approach.py
@@ -123,7 +123,8 @@ class GeneratedApproach:
  123    123              # leaving room above it for a later verified re-grasp.
  124    124              park_y = 0.35
  125    125              parked_high_enough = (not is_target and self.attached and oy >= park_y)
  126        -            if ry < 0.74 and not parked_high_enough:
         126 +            lift_limit = self.safe_y - 0.025 if is_target else 0.74
         127 +            if ry < lift_limit and not parked_high_enough:
  127    128                  return self._action(dy=0.05, vac=1.0)
  128    129              if not self.attached:
  129    130                  self.retry += 1
```

</details>

<a id="C024"></a>
<a id="R21"></a>
### C024 · Keep parking slots away from side-wall dead zones

Commit `2185ba3df73338fd65ddcaabaa8b2a357185bd32`; parents: 71c469c4e314a5b175e8c23b683914de11a519e1. Recorded author date: 2026-09-08T22:50:43+02:00.

File roles (automatic): policy.

- [E0254](01_timeline.md#E0254): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 5 fails after earlier fixes → move candidate parking positions away from side walls.


Prior mapped context: [E0248](01_timeline.md#E0248), [E0250](01_timeline.md#E0250), [E0252](01_timeline.md#E0252), [E0254](01_timeline.md#E0254).

Prior mapped post-edit test reports: [E0254](01_timeline.md#E0254). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C024_2185ba3_approach.py) · [Exact all-file diff](evidence/diffs/C024_2185ba3.diff)

[Previous saved controller snapshot](evidence/versions/C023_71c469c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index acb24ec..275c805 100644
--- a/approach.py
+++ b/approach.py
@@ -24,7 +24,8 @@ class GeneratedApproach:
   24     24          sx, sw = state.get(surface, "x"), state.get(surface, "width")
   25     25          # Greedily reserve floor-clear parking columns, preferring positions far
   26     26          # from both the pickup and goal.  The grid is count-independent.
   27        -        candidates = [0.14 + 0.10 * k for k in range(14)]
          27 +        # Keep parking poses one base radius away from both side walls.
          28 +        candidates = [0.20 + 0.10 * k for k in range(12)]
   28     29          candidates.sort(key=lambda x: min(abs(x - tx) - tw / 2,
   29     30                                             abs(x - sx) - sw / 2), reverse=True)
   30     31          self.parking = {}
```

</details>

<a id="C025"></a>
<a id="R22"></a>
### C025 · Cap verification lift at reachable ceiling

Commit `8e66f4e20a889c54882353ae942873737a9c3ce5`; parents: 2185ba3df73338fd65ddcaabaa8b2a357185bd32. Recorded author date: 2026-09-08T22:51:32+02:00.

File roles (automatic): policy.

- [E0260](01_timeline.md#E0260): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 5 still stalls in lift → cap upward movement at the reachable ceiling.


Prior mapped context: [E0254](01_timeline.md#E0254), [E0256](01_timeline.md#E0256), [E0258](01_timeline.md#E0258), [E0260](01_timeline.md#E0260).

Prior mapped post-edit test reports: [E0260](01_timeline.md#E0260), [E0263](01_timeline.md#E0263). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C025_8e66f4e_approach.py) · [Exact all-file diff](evidence/diffs/C025_8e66f4e.diff)

[Previous saved controller snapshot](evidence/versions/C024_2185ba3_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 275c805..22a1384 100644
--- a/approach.py
+++ b/approach.py
@@ -126,7 +126,7 @@ class GeneratedApproach:
  126    126              parked_high_enough = (not is_target and self.attached and oy >= park_y)
  127    127              lift_limit = self.safe_y - 0.025 if is_target else 0.74
  128    128              if ry < lift_limit and not parked_high_enough:
  129        -                return self._action(dy=0.05, vac=1.0)
         129 +                return self._action(dy=min(0.05, self.safe_y - ry), vac=1.0)
  130    130              if not self.attached:
  131    131                  self.retry += 1
  132    132                  if self.retry < 9:
```

</details>

<a id="C026"></a>
<a id="R23"></a>
### C026 · Raise temporary target and maximize final carry clearance

Commit `3098aabc1d599cbc0c86bdff512bbb9059d0ffd9`; parents: 8e66f4e20a889c54882353ae942873737a9c3ce5. Recorded author date: 2026-09-08T22:53:12+02:00.

File roles (automatic): policy.

- [E0271](01_timeline.md#E0271): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** A broader sweep finds seeds 18 and 22 failing → raise temporary target parking and final carry height.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0261](01_timeline.md#E0261), [E0263](01_timeline.md#E0263), [E0265](01_timeline.md#E0265), [E0267](01_timeline.md#E0267), [E0269](01_timeline.md#E0269), [E0271](01_timeline.md#E0271).

Prior mapped post-edit test reports: [E0271](01_timeline.md#E0271). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C026_3098aab_approach.py) · [Exact all-file diff](evidence/diffs/C026_3098aab.diff)

[Previous saved controller snapshot](evidence/versions/C025_8e66f4e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 22a1384..4f7031b 100644
--- a/approach.py
+++ b/approach.py
@@ -122,9 +122,9 @@ class GeneratedApproach:
  122    122                  self.attached = True
  123    123              # A modest vertical park is enough to clear the ground while still
  124    124              # leaving room above it for a later verified re-grasp.
  125        -            park_y = 0.35
         125 +            park_y = 0.45 if (obj.type.name == "target_block" and not is_target) else 0.35
  126    126              parked_high_enough = (not is_target and self.attached and oy >= park_y)
  127        -            lift_limit = self.safe_y - 0.025 if is_target else 0.74
         127 +            lift_limit = self.safe_y if is_target else 0.74
  128    128              if ry < lift_limit and not parked_high_enough:
  129    129                  return self._action(dy=min(0.05, self.safe_y - ry), vac=1.0)
  130    130              if not self.attached:
```

</details>

<a id="C027"></a>
<a id="R24"></a>
### C027 · Park crowded target outward and lower cleared blockers

Commit `5075837dadc53f2b9aa222d14fab65556d3e1d3b`; parents: 3098aabc1d599cbc0c86bdff512bbb9059d0ffd9. Recorded author date: 2026-09-08T22:54:00+02:00.

File roles (automatic): policy.

- [E0277](01_timeline.md#E0277): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Both targeted cases still fail → choose an outward target slot and lower blocker parking.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0271](01_timeline.md#E0271), [E0273](01_timeline.md#E0273), [E0275](01_timeline.md#E0275), [E0277](01_timeline.md#E0277).

Prior mapped post-edit test reports: [E0277](01_timeline.md#E0277). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C027_5075837_approach.py) · [Exact all-file diff](evidence/diffs/C027_5075837.diff)

[Previous saved controller snapshot](evidence/versions/C026_3098aab_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4f7031b..b29244e 100644
--- a/approach.py
+++ b/approach.py
@@ -32,7 +32,8 @@ class GeneratedApproach:
   32     32          used = []
   33     33          self.target_park = tx
   34     34          if crowded:
   35        -            self.target_park = candidates[0]
          35 +            outward = [x for x in candidates if (x - sx) * (tx - sx) > 0]
          36 +            self.target_park = max(outward, key=lambda x: abs(x - sx)) if outward else candidates[0]
   36     37              used.append((self.target_park, tw))
   37     38          for o in obstacles:
   38     39              ow = state.get(o, "width")
@@ -122,7 +123,7 @@ class GeneratedApproach:
  122    123                  self.attached = True
  123    124              # A modest vertical park is enough to clear the ground while still
  124    125              # leaving room above it for a later verified re-grasp.
  125        -            park_y = 0.45 if (obj.type.name == "target_block" and not is_target) else 0.35
         126 +            park_y = 0.45 if (obj.type.name == "target_block" and not is_target) else 0.30
  126    127              parked_high_enough = (not is_target and self.attached and oy >= park_y)
  127    128              lift_limit = self.safe_y if is_target else 0.74
  128    129              if ry < lift_limit and not parked_high_enough:
```

</details>

<a id="C028"></a>
<a id="R25"></a>
### C028 · Route blockers outward without crossing the surface cluster

Commit `0605fd3f07cdfae354f87870e72be0d05cfb4d0f`; parents: 5075837dadc53f2b9aa222d14fab65556d3e1d3b. Recorded author date: 2026-09-08T22:54:44+02:00.

File roles (automatic): policy.

- [E0283](01_timeline.md#E0283): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 18 remains unresolved → restrict blocker parking to the same side of the surface.


Prior mapped context: [E0277](01_timeline.md#E0277), [E0279](01_timeline.md#E0279), [E0281](01_timeline.md#E0281), [E0283](01_timeline.md#E0283).

Prior mapped post-edit test reports: [E0283](01_timeline.md#E0283). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C028_0605fd3_approach.py) · [Exact all-file diff](evidence/diffs/C028_0605fd3.diff)

[Previous saved controller snapshot](evidence/versions/C027_5075837_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b29244e..796dfcd 100644
--- a/approach.py
+++ b/approach.py
@@ -37,8 +37,10 @@ class GeneratedApproach:
   37     37              used.append((self.target_park, tw))
   38     38          for o in obstacles:
   39     39              ow = state.get(o, "width")
   40        -            valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.04
   41        -                                                  for px, pw in used)]
          40 +            origin = state.get(o, "x")
          41 +            same_side = [x for x in candidates if (x - sx) * (origin - sx) >= 0]
          42 +            valid = [x for x in same_side if all(abs(x - px) > (ow + pw) / 2 + 0.04
          43 +                                                 for px, pw in used)]
   42     44              px = valid[0] if valid else candidates[len(used) % len(candidates)]
   43     45              self.parking[o.name] = px
   44     46              used.append((px, ow))
```

</details>

<a id="C029"></a>
<a id="R26"></a>
### C029 · Carry blockers high then lower them into parking slots

Commit `f064af00582ce75b9fd14ff90c2d56e519faf1f5`; parents: 0605fd3f07cdfae354f87870e72be0d05cfb4d0f. Recorded author date: 2026-09-08T22:55:32+02:00.

File roles (automatic): policy.

- [E0289](01_timeline.md#E0289): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 18 remains unresolved → carry blockers higher and add a separate lowering phase.


Prior mapped context: [E0283](01_timeline.md#E0283), [E0285](01_timeline.md#E0285), [E0287](01_timeline.md#E0287), [E0289](01_timeline.md#E0289).

Prior mapped post-edit test reports: [E0289](01_timeline.md#E0289). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C029_f064af0_approach.py) · [Exact all-file diff](evidence/diffs/C029_f064af0.diff)

[Previous saved controller snapshot](evidence/versions/C028_0605fd3_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 796dfcd..49fd42d 100644
--- a/approach.py
+++ b/approach.py
@@ -125,7 +125,7 @@ class GeneratedApproach:
  125    125                  self.attached = True
  126    126              # A modest vertical park is enough to clear the ground while still
  127    127              # leaving room above it for a later verified re-grasp.
  128        -            park_y = 0.45 if (obj.type.name == "target_block" and not is_target) else 0.30
         128 +            park_y = 0.45 if obj.type.name == "target_block" else 0.50
  129    129              parked_high_enough = (not is_target and self.attached and oy >= park_y)
  130    130              lift_limit = self.safe_y if is_target else 0.74
  131    131              if ry < lift_limit and not parked_high_enough:
@@ -163,8 +163,12 @@ class GeneratedApproach:
  163    163                  else:
  164    164                      return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
  165    165              else:
  166        -                self.phase = "lower" if is_target else "release"
         166 +                self.phase = "lower" if is_target else "park_lower"
  167    167              self.stalled, self.last_robot_y = 0, ry
         168 +        if self.phase == "park_lower":
         169 +            if oy > 0.305:
         170 +                return self._action(dy=-0.01, vac=1.0)
         171 +            self.phase = "release"
  168    172          if self.phase == "lower":
  169    173              if abs(ry - self.last_robot_y) < 0.001:
  170    174                  self.stalled += 1
```

</details>

<a id="C030"></a>
<a id="R27"></a>
### C030 · Accept maximum reachable blocker carry height

Commit `a4cb1dbb0987bec72cb037f5bffc942ae4fc26f3`; parents: f064af00582ce75b9fd14ff90c2d56e519faf1f5. Recorded author date: 2026-09-08T22:56:16+02:00.

File roles (automatic): policy.

- [E0293](01_timeline.md#E0293): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 18 and six baseline cases fail → allow a blocker lift to finish at the reachable ceiling.


Prior mapped context: [E0289](01_timeline.md#E0289), [E0291](01_timeline.md#E0291), [E0293](01_timeline.md#E0293).

Prior mapped post-edit test reports: [E0293](01_timeline.md#E0293). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C030_a4cb1db_approach.py) · [Exact all-file diff](evidence/diffs/C030_a4cb1db.diff)

[Previous saved controller snapshot](evidence/versions/C029_f064af0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 49fd42d..098fcbb 100644
--- a/approach.py
+++ b/approach.py
@@ -126,7 +126,8 @@ class GeneratedApproach:
  126    126              # A modest vertical park is enough to clear the ground while still
  127    127              # leaving room above it for a later verified re-grasp.
  128    128              park_y = 0.45 if obj.type.name == "target_block" else 0.50
  129        -            parked_high_enough = (not is_target and self.attached and oy >= park_y)
         129 +            parked_high_enough = (not is_target and self.attached and
         130 +                                  (oy >= park_y or ry >= self.safe_y - 0.004))
  130    131              lift_limit = self.safe_y if is_target else 0.74
  131    132              if ry < lift_limit and not parked_high_enough:
  132    133                  return self._action(dy=min(0.05, self.safe_y - ry), vac=1.0)
```

</details>

<a id="C031"></a>
<a id="R28"></a>
### C031 · Restore reliable low blocker parking behavior

Commit `13fcd5838c87608d9c30898ed7dd2f6bfa8a00b7`; parents: a4cb1dbb0987bec72cb037f5bffc942ae4fc26f3. Recorded author date: 2026-09-08T22:57:02+02:00.

File roles (automatic): policy.

- [E0297](01_timeline.md#E0297): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** The broad failures persist → undo the high-carry/lowering changes and restore low parking.

- Restores part of an earlier rule. A partial reversal is not necessarily a full Git revert or an exact return to an earlier complete program.

Prior mapped context: [E0293](01_timeline.md#E0293), [E0295](01_timeline.md#E0295), [E0297](01_timeline.md#E0297).

Prior mapped post-edit test reports: [E0297](01_timeline.md#E0297). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C031_13fcd58_approach.py) · [Exact all-file diff](evidence/diffs/C031_13fcd58.diff)

[Previous saved controller snapshot](evidence/versions/C030_a4cb1db_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C028](#C028). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 098fcbb..796dfcd 100644
--- a/approach.py
+++ b/approach.py
@@ -125,9 +125,8 @@ class GeneratedApproach:
  125    125                  self.attached = True
  126    126              # A modest vertical park is enough to clear the ground while still
  127    127              # leaving room above it for a later verified re-grasp.
  128        -            park_y = 0.45 if obj.type.name == "target_block" else 0.50
  129        -            parked_high_enough = (not is_target and self.attached and
  130        -                                  (oy >= park_y or ry >= self.safe_y - 0.004))
         128 +            park_y = 0.45 if (obj.type.name == "target_block" and not is_target) else 0.30
         129 +            parked_high_enough = (not is_target and self.attached and oy >= park_y)
  131    130              lift_limit = self.safe_y if is_target else 0.74
  132    131              if ry < lift_limit and not parked_high_enough:
  133    132                  return self._action(dy=min(0.05, self.safe_y - ry), vac=1.0)
@@ -164,12 +163,8 @@ class GeneratedApproach:
  164    163                  else:
  165    164                      return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
  166    165              else:
  167        -                self.phase = "lower" if is_target else "park_lower"
         166 +                self.phase = "lower" if is_target else "release"
  168    167              self.stalled, self.last_robot_y = 0, ry
  169        -        if self.phase == "park_lower":
  170        -            if oy > 0.305:
  171        -                return self._action(dy=-0.01, vac=1.0)
  172        -            self.phase = "release"
  173    168          if self.phase == "lower":
  174    169              if abs(ry - self.last_robot_y) < 0.001:
  175    170                  self.stalled += 1
```

</details>

<a id="C032"></a>
<a id="R29"></a>
### C032 · Choose globally clear parking slots over directional routing

Commit `04141a4c7d2ec421315e0c41837ad01b8093653e`; parents: 13fcd5838c87608d9c30898ed7dd2f6bfa8a00b7. Recorded author date: 2026-09-08T22:57:35+02:00.

File roles (automatic): policy.

- [E0301](01_timeline.md#E0301): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Three baseline failures remain → remove the same-side parking restriction.

- Restores part of an earlier rule. A partial reversal is not necessarily a full Git revert or an exact return to an earlier complete program.

Prior mapped context: [E0297](01_timeline.md#E0297), [E0299](01_timeline.md#E0299), [E0301](01_timeline.md#E0301).

Prior mapped post-edit test reports: [E0301](01_timeline.md#E0301). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C032_04141a4_approach.py) · [Exact all-file diff](evidence/diffs/C032_04141a4.diff)

[Previous saved controller snapshot](evidence/versions/C031_13fcd58_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C027](#C027). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 796dfcd..b29244e 100644
--- a/approach.py
+++ b/approach.py
@@ -37,10 +37,8 @@ class GeneratedApproach:
   37     37              used.append((self.target_park, tw))
   38     38          for o in obstacles:
   39     39              ow = state.get(o, "width")
   40        -            origin = state.get(o, "x")
   41        -            same_side = [x for x in candidates if (x - sx) * (origin - sx) >= 0]
   42        -            valid = [x for x in same_side if all(abs(x - px) > (ow + pw) / 2 + 0.04
   43        -                                                 for px, pw in used)]
          40 +            valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.04
          41 +                                                  for px, pw in used)]
   44     42              px = valid[0] if valid else candidates[len(used) % len(candidates)]
   45     43              self.parking[o.name] = px
   46     44              used.append((px, ow))
```

</details>

<a id="C033"></a>
<a id="R30"></a>
### C033 · Use globally safest temporary target slot

Commit `3f93ca0c4cd0d1c46cd0f0da2fc46554cfc0b38d`; parents: 04141a4c7d2ec421315e0c41837ad01b8093653e. Recorded author date: 2026-09-08T22:58:24+02:00.

File roles (automatic): policy.

- [E0307](01_timeline.md#E0307): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 10 remains unresolved → remove the outward-only target parking rule.

- Restores part of an earlier rule. A partial reversal is not necessarily a full Git revert or an exact return to an earlier complete program.

Prior mapped context: [E0301](01_timeline.md#E0301), [E0303](01_timeline.md#E0303), [E0305](01_timeline.md#E0305), [E0307](01_timeline.md#E0307).

Prior mapped post-edit test reports: [E0307](01_timeline.md#E0307), [E0311](01_timeline.md#E0311). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C033_3f93ca0_approach.py) · [Exact all-file diff](evidence/diffs/C033_3f93ca0.diff)

[Previous saved controller snapshot](evidence/versions/C032_04141a4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b29244e..ba7b5f6 100644
--- a/approach.py
+++ b/approach.py
@@ -32,8 +32,7 @@ class GeneratedApproach:
   32     32          used = []
   33     33          self.target_park = tx
   34     34          if crowded:
   35        -            outward = [x for x in candidates if (x - sx) * (tx - sx) > 0]
   36        -            self.target_park = max(outward, key=lambda x: abs(x - sx)) if outward else candidates[0]
          35 +            self.target_park = candidates[0]
   37     36              used.append((self.target_park, tw))
   38     37          for o in obstacles:
   39     38              ow = state.get(o, "width")
```

</details>

<a id="C034"></a>
<a id="R31"></a>
### C034 · Use denser nonoverlapping parking allocation

Commit `990576d616dd3fe0c0742b7ac88631919d3b82a1`; parents: 3f93ca0c4cd0d1c46cd0f0da2fc46554cfc0b38d. Recorded author date: 2026-09-08T23:00:33+02:00.

File roles (automatic): policy.

- [E0317](01_timeline.md#E0317): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Several clustered cases fail → reduce the spacing margin between parked objects.


Prior mapped context: [E0307](01_timeline.md#E0307), [E0311](01_timeline.md#E0311), [E0313](01_timeline.md#E0313), [E0315](01_timeline.md#E0315), [E0317](01_timeline.md#E0317).

Prior mapped post-edit test reports: [E0317](01_timeline.md#E0317). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C034_990576d_approach.py) · [Exact all-file diff](evidence/diffs/C034_990576d.diff)

[Previous saved controller snapshot](evidence/versions/C033_3f93ca0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ba7b5f6..359d509 100644
--- a/approach.py
+++ b/approach.py
@@ -36,7 +36,7 @@ class GeneratedApproach:
   36     36              used.append((self.target_park, tw))
   37     37          for o in obstacles:
   38     38              ow = state.get(o, "width")
   39        -            valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.04
          39 +            valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.015
   40     40                                                    for px, pw in used)]
   41     41              px = valid[0] if valid else candidates[len(used) % len(candidates)]
   42     42              self.parking[o.name] = px
```

</details>

<a id="C035"></a>
<a id="R32"></a>
### C035 · Restore validated parking clearance margin

Commit `a11bd5f9b411df31efdc63d9afbec4404369f0ff`; parents: 990576d616dd3fe0c0742b7ac88631919d3b82a1. Recorded author date: 2026-09-08T23:01:02+02:00.

File roles (automatic): policy.

- [E0321](01_timeline.md#E0321): commit hash in recorded output.

**Prior analyst description (carried forward, not independently relabeled):** Smaller spacing leaves all four targeted cases failing → restore the earlier spacing margin → compile and hand off without a fresh rollout report in that turn.

- No fresh rollout result is recorded after this revision before that turn ends at L328. L321 runs compilation. A later resumed turn probes the unchanged policy at L335 (included with R33); this is not a claim that the policy was never executed again. Later agent summaries are not a replacement for a missing same-turn retest.
- Restores part of an earlier rule. A partial reversal is not necessarily a full Git revert or an exact return to an earlier complete program.

Prior mapped context: [E0317](01_timeline.md#E0317), [E0319](01_timeline.md#E0319), [E0321](01_timeline.md#E0321).

Prior mapped post-edit test reports: none mapped. These are not isolated causal tests.

[Controller after this commit](evidence/versions/C035_a11bd5f_approach.py) · [Exact all-file diff](evidence/diffs/C035_a11bd5f.diff)

[Previous saved controller snapshot](evidence/versions/C034_990576d_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C033](#C033). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 359d509..ba7b5f6 100644
--- a/approach.py
+++ b/approach.py
@@ -36,7 +36,7 @@ class GeneratedApproach:
   36     36              used.append((self.target_park, tw))
   37     37          for o in obstacles:
   38     38              ow = state.get(o, "width")
   39        -            valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.015
          39 +            valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.04
   40     40                                                    for px, pw in used)]
   41     41              px = valid[0] if valid else candidates[len(used) % len(candidates)]
   42     42              self.parking[o.name] = px
```

</details>

<a id="C036"></a>
### C036 · initial sandbox setup

Commit `539f180b5e0bda7f31f3c416d407e89b1703d98c`; parents: a11bd5f9b411df31efdc63d9afbec4404369f0ff. Recorded author date: 2026-09-08T23:01:50+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C036_539f180.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/AGENTS.md b/AGENTS.md
index 76dfa5b..5dbfa8c 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,6 @@
    1      1  You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
    2      2  
    3        -Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $20.00. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $13.04. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
    4      4  
    5      5  Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
    6      6  
```

</details>

<a id="C037"></a>
<a id="R33"></a>
### C037 · Verify grasp against lowest observed object height

Commit `c1c4586e18d6eb769aa82ec18799d7a6a5bd5dab`; parents: 539f180b5e0bda7f31f3c416d407e89b1703d98c. Recorded author date: 2026-09-08T23:03:26+02:00.

File roles (automatic): policy.

- [E0342](01_timeline.md#E0342): commit hash in recorded output.

**Prior analyst description (carried forward, not independently relabeled):** Resume work on seed 18; inspect pickup heights → verify a lift against the lowest observed object height.

- This crosses a turn boundary. Actual Git parent 539f180 only changes archived AGENTS.md; the preceding policy-changing commit is a11bd5f. These historical instructions remain data.

Prior mapped context: [E0317](01_timeline.md#E0317), [E0324](01_timeline.md#E0324), [E0327](01_timeline.md#E0327), [E0331](01_timeline.md#E0331), [E0335](01_timeline.md#E0335), [E0338](01_timeline.md#E0338), [E0340](01_timeline.md#E0340), [E0342](01_timeline.md#E0342).

Prior mapped post-edit test reports: [E0342](01_timeline.md#E0342). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C037_c1c4586_approach.py) · [Exact all-file diff](evidence/diffs/C037_c1c4586.diff)

[Previous saved controller snapshot](evidence/versions/C035_a11bd5f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ba7b5f6..ef555ac 100644
--- a/approach.py
+++ b/approach.py
@@ -104,6 +104,10 @@ class GeneratedApproach:
  104    104                  # touch the gripper as it passes underneath.
  105    105                  return self._action(dx=self._clip(tx - rx, 0.05), vac=0.0)
  106    106          if self.phase == "descend":
         107 +            # A neighboring floating object can be pushed downward before the
         108 +            # vacuum acquires it.  Verify lift relative to the lowest observed
         109 +            # height, not merely its height at the start of the approach.
         110 +            self.pick_y = min(self.pick_y, oy)
  107    111              if self.last_robot_y is not None and abs(ry - self.last_robot_y) < 0.001:
  108    112                  self.stalled += 1
  109    113              else:
```

</details>

<a id="C038"></a>
<a id="R34"></a>
### C038 · Clear crowded objects from highest top edge downward

Commit `e97a5378cb34a8df18769cdf4c4b15f5bf5e674d`; parents: c1c4586e18d6eb769aa82ec18799d7a6a5bd5dab. Recorded author date: 2026-09-08T23:04:36+02:00.

File roles (automatic): policy.

- [E0348](01_timeline.md#E0348): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 18 still fails and the controller reaches done → sort the initial task list by computed top height.


Prior mapped context: [E0342](01_timeline.md#E0342), [E0344](01_timeline.md#E0344), [E0346](01_timeline.md#E0346), [E0348](01_timeline.md#E0348).

Prior mapped post-edit test reports: [E0348](01_timeline.md#E0348), [E0351](01_timeline.md#E0351). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C038_e97a537_approach.py) · [Exact all-file diff](evidence/diffs/C038_e97a537.diff)

[Previous saved controller snapshot](evidence/versions/C037_c1c4586_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ef555ac..2f8b395 100644
--- a/approach.py
+++ b/approach.py
@@ -18,7 +18,16 @@ class GeneratedApproach:
   18     18          tx, tw = state.get(target, "x"), state.get(target, "width")
   19     19          crowded = any(abs(tx - state.get(o, "x")) <
   20     20                        0.5 * (tw + state.get(o, "width")) + 0.14 for o in obstacles)
   21        -        self.todo = ([target_name] if crowded else []) + [o.name for o in obstacles]
          21 +        tasks = list(obstacles)
          22 +        if crowded:
          23 +            tasks.append(target)
          24 +        def top_y(o):
          25 +            angle = state.get(o, "theta")
          26 +            vertical_half = 0.5 * (abs(math.sin(angle)) * state.get(o, "width") +
          27 +                                   abs(math.cos(angle)) * state.get(o, "height"))
          28 +            return state.get(o, "y") + vertical_half
          29 +        tasks.sort(key=top_y, reverse=True)
          30 +        self.todo = [o.name for o in tasks]
   22     31          self.todo.append(target_name)  # retrieve it last for the actual placement
   23     32          surface = state.get_objects(self.types["target_surface"])[0]
   24     33          sx, sw = state.get(surface, "x"), state.get(surface, "width")
```

</details>

<a id="C039"></a>
<a id="R35"></a>
### C039 · Keep parked blockers clear of final target sweep

Commit `c9b3655e06a45822107bdbf0b1953ba730e77ef1`; parents: e97a5378cb34a8df18769cdf4c4b15f5bf5e674d. Recorded author date: 2026-09-08T23:06:22+02:00.

File roles (automatic): policy.

- [E0358](01_timeline.md#E0358): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seeds 39 and 45 fail → add destination clearance and enlarge separation between parked objects.


Prior mapped context: [E0349](01_timeline.md#E0349), [E0351](01_timeline.md#E0351), [E0353](01_timeline.md#E0353), [E0354](01_timeline.md#E0354), [E0356](01_timeline.md#E0356), [E0358](01_timeline.md#E0358).

Prior mapped post-edit test reports: [E0358](01_timeline.md#E0358). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C039_c9b3655_approach.py) · [Exact all-file diff](evidence/diffs/C039_c9b3655.diff)

[Previous saved controller snapshot](evidence/versions/C038_e97a537_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2f8b395..14a32d6 100644
--- a/approach.py
+++ b/approach.py
@@ -45,8 +45,11 @@ class GeneratedApproach:
   45     45              used.append((self.target_park, tw))
   46     46          for o in obstacles:
   47     47              ow = state.get(o, "width")
   48        -            valid = [x for x in candidates if all(abs(x - px) > (ow + pw) / 2 + 0.04
   49        -                                                  for px, pw in used)]
          48 +            goal_clearance = sw / 2 + tw / 2 + ow / 2 + 0.03
          49 +            valid = [x for x in candidates
          50 +                     if abs(x - sx) > goal_clearance
          51 +                     and all(abs(x - px) > (ow + pw) / 2 + 0.12
          52 +                             for px, pw in used)]
   50     53              px = valid[0] if valid else candidates[len(used) % len(candidates)]
   51     54              self.parking[o.name] = px
   52     55              used.append((px, ow))
```

</details>

<a id="C040"></a>
<a id="R36"></a>
### C040 · Move crowded target after only materially taller blockers

Commit `4d36a38a1864f8754cb3d3ed0c0bf114e1588e37`; parents: c9b3655e06a45822107bdbf0b1953ba730e77ef1. Recorded author date: 2026-09-08T23:07:35+02:00.

File roles (automatic): policy.

- [E0366](01_timeline.md#E0366): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 3 becomes a regression → insert the target earlier when blocker heights are close.


Prior mapped context: [E0358](01_timeline.md#E0358), [E0360](01_timeline.md#E0360), [E0362](01_timeline.md#E0362), [E0364](01_timeline.md#E0364), [E0366](01_timeline.md#E0366).

Prior mapped post-edit test reports: [E0366](01_timeline.md#E0366), [E0370](01_timeline.md#E0370). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C040_4d36a38_approach.py) · [Exact all-file diff](evidence/diffs/C040_4d36a38.diff)

[Previous saved controller snapshot](evidence/versions/C039_c9b3655_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 14a32d6..3266302 100644
--- a/approach.py
+++ b/approach.py
@@ -18,15 +18,18 @@ class GeneratedApproach:
   18     18          tx, tw = state.get(target, "x"), state.get(target, "width")
   19     19          crowded = any(abs(tx - state.get(o, "x")) <
   20     20                        0.5 * (tw + state.get(o, "width")) + 0.14 for o in obstacles)
   21        -        tasks = list(obstacles)
   22        -        if crowded:
   23        -            tasks.append(target)
   24     21          def top_y(o):
   25     22              angle = state.get(o, "theta")
   26     23              vertical_half = 0.5 * (abs(math.sin(angle)) * state.get(o, "width") +
   27     24                                     abs(math.cos(angle)) * state.get(o, "height"))
   28     25              return state.get(o, "y") + vertical_half
   29        -        tasks.sort(key=top_y, reverse=True)
          26 +        tasks = sorted(obstacles, key=top_y, reverse=True)
          27 +        if crowded:
          28 +            target_top = top_y(target)
          29 +            # Clear meaningfully taller neighbors first, then move the target
          30 +            # before near-tied lower objects can obstruct its pickup corridor.
          31 +            insert_at = sum(top_y(o) > target_top + 0.015 for o in tasks)
          32 +            tasks.insert(insert_at, target)
   30     33          self.todo = [o.name for o in tasks]
   31     34          self.todo.append(target_name)  # retrieve it last for the actual placement
   32     35          surface = state.get_objects(self.types["target_surface"])[0]
```

</details>

<a id="C041"></a>
<a id="R37"></a>
### C041 · Protect future pickups when assigning parking slots

Commit `be6feb60cb8cb0981cde9814194135d920128e75`; parents: 4d36a38a1864f8754cb3d3ed0c0bf114e1588e37. Recorded author date: 2026-09-08T23:09:56+02:00.

File roles (automatic): policy.

- [E0378](01_timeline.md#E0378): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seeds 15 and 26 fail → widen the height tolerance AND reject parking slots near future pickups.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0367](01_timeline.md#E0367), [E0370](01_timeline.md#E0370), [E0373](01_timeline.md#E0373), [E0374](01_timeline.md#E0374), [E0376](01_timeline.md#E0376), [E0378](01_timeline.md#E0378).

Prior mapped post-edit test reports: [E0378](01_timeline.md#E0378), [E0380](01_timeline.md#E0380). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C041_be6feb6_approach.py) · [Exact all-file diff](evidence/diffs/C041_be6feb6.diff)

[Previous saved controller snapshot](evidence/versions/C040_4d36a38_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3266302..6ba4bfc 100644
--- a/approach.py
+++ b/approach.py
@@ -28,7 +28,7 @@ class GeneratedApproach:
   28     28              target_top = top_y(target)
   29     29              # Clear meaningfully taller neighbors first, then move the target
   30     30              # before near-tied lower objects can obstruct its pickup corridor.
   31        -            insert_at = sum(top_y(o) > target_top + 0.015 for o in tasks)
          31 +            insert_at = sum(top_y(o) > target_top + 0.035 for o in tasks)
   32     32              tasks.insert(insert_at, target)
   33     33          self.todo = [o.name for o in tasks]
   34     34          self.todo.append(target_name)  # retrieve it last for the actual placement
@@ -42,6 +42,10 @@ class GeneratedApproach:
   42     42                                             abs(x - sx) - sw / 2), reverse=True)
   43     43          self.parking = {}
   44     44          used = []
          45 +        first_rank = {}
          46 +        for rank, name in enumerate(self.todo):
          47 +            if name not in first_rank:
          48 +                first_rank[name] = rank
   45     49          self.target_park = tx
   46     50          if crowded:
   47     51              self.target_park = candidates[0]
@@ -49,8 +53,12 @@ class GeneratedApproach:
   49     53          for o in obstacles:
   50     54              ow = state.get(o, "width")
   51     55              goal_clearance = sw / 2 + tw / 2 + ow / 2 + 0.03
          56 +            future = [q for q in obstacles + [target]
          57 +                      if q.name != o.name and first_rank.get(q.name, 10**9) > first_rank[o.name]]
   52     58              valid = [x for x in candidates
   53     59                       if abs(x - sx) > goal_clearance
          60 +                     and all(abs(x - state.get(q, "x")) >
          61 +                             (ow + state.get(q, "width")) / 2 + 0.08 for q in future)
   54     62                       and all(abs(x - px) > (ow + pw) / 2 + 0.12
   55     63                               for px, pw in used)]
   56     64              px = valid[0] if valid else candidates[len(used) % len(candidates)]
```

</details>

<a id="C042"></a>
<a id="R38"></a>
### C042 · Prioritize physically overlapping taller blockers

Commit `616a82f41c95f8f631d9813da952c4d62c8e5a85`; parents: be6feb60cb8cb0981cde9814194135d920128e75. Recorded author date: 2026-09-08T23:11:34+02:00.

File roles (automatic): policy.

- [E0387](01_timeline.md#E0387): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 18 breaks again → include geometric overlap in the target-ordering criterion.


Prior mapped context: [E0380](01_timeline.md#E0380), [E0382](01_timeline.md#E0382), [E0383](01_timeline.md#E0383), [E0385](01_timeline.md#E0385), [E0387](01_timeline.md#E0387).

Prior mapped post-edit test reports: [E0387](01_timeline.md#E0387), [E0389](01_timeline.md#E0389). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C042_616a82f_approach.py) · [Exact all-file diff](evidence/diffs/C042_616a82f.diff)

[Previous saved controller snapshot](evidence/versions/C041_be6feb6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6ba4bfc..31cc0e1 100644
--- a/approach.py
+++ b/approach.py
@@ -26,9 +26,18 @@ class GeneratedApproach:
   26     26          tasks = sorted(obstacles, key=top_y, reverse=True)
   27     27          if crowded:
   28     28              target_top = top_y(target)
          29 +            target_angle = state.get(target, "theta")
          30 +            target_hx = 0.5 * (abs(math.cos(target_angle)) * tw +
          31 +                               abs(math.sin(target_angle)) * state.get(target, "height"))
          32 +            def must_precede_target(o):
          33 +                angle = state.get(o, "theta")
          34 +                hx = 0.5 * (abs(math.cos(angle)) * state.get(o, "width") +
          35 +                            abs(math.sin(angle)) * state.get(o, "height"))
          36 +                overlaps = abs(state.get(o, "x") - tx) < hx + target_hx + 0.005
          37 +                return top_y(o) > target_top + 0.035 or (overlaps and top_y(o) > target_top)
   29     38              # Clear meaningfully taller neighbors first, then move the target
   30     39              # before near-tied lower objects can obstruct its pickup corridor.
   31        -            insert_at = sum(top_y(o) > target_top + 0.035 for o in tasks)
          40 +            insert_at = sum(must_precede_target(o) for o in tasks)
   32     41              tasks.insert(insert_at, target)
   33     42          self.todo = [o.name for o in tasks]
   34     43          self.todo.append(target_name)  # retrieve it last for the actual placement
```

</details>

<a id="C043"></a>
<a id="R39"></a>
### C043 · Allocate outer parking slots before inner ones

Commit `dafcc2f32a2e25cb17d3c23d03a74a4c163e5fd3`; parents: 616a82f41c95f8f631d9813da952c4d62c8e5a85. Recorded author date: 2026-09-08T23:13:25+02:00.

File roles (automatic): policy.

- [E0396](01_timeline.md#E0396): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 59 fails → allocate farther-from-surface parking positions before inner positions.


Prior mapped context: [E0389](01_timeline.md#E0389), [E0391](01_timeline.md#E0391), [E0392](01_timeline.md#E0392), [E0394](01_timeline.md#E0394), [E0396](01_timeline.md#E0396).

Prior mapped post-edit test reports: [E0396](01_timeline.md#E0396), [E0401](01_timeline.md#E0401), [E0411](01_timeline.md#E0411). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C043_dafcc2f_approach.py) · [Exact all-file diff](evidence/diffs/C043_dafcc2f.diff)

[Previous saved controller snapshot](evidence/versions/C042_616a82f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 31cc0e1..dfac8aa 100644
--- a/approach.py
+++ b/approach.py
@@ -47,8 +47,9 @@ class GeneratedApproach:
   47     47          # from both the pickup and goal.  The grid is count-independent.
   48     48          # Keep parking poses one base radius away from both side walls.
   49     49          candidates = [0.20 + 0.10 * k for k in range(12)]
   50        -        candidates.sort(key=lambda x: min(abs(x - tx) - tw / 2,
   51        -                                           abs(x - sx) - sw / 2), reverse=True)
          50 +        # Allocate outermost slots first so a later blocker never has to pass
          51 +        # through an earlier parked one on the way out of the goal region.
          52 +        candidates.sort(key=lambda x: (abs(x - sx), abs(x - tx)), reverse=True)
   52     53          self.parking = {}
   53     54          used = []
   54     55          first_rank = {}
```

</details>

<a id="C044"></a>
### C044 · Add pinned object-count regression support

Commit `678059d4ec84d6608cd7d10084be4b9f6efe8e0e`; parents: dafcc2f32a2e25cb17d3c23d03a74a4c163e5fd3. Recorded author date: 2026-09-08T23:15:14+02:00.

File roles (automatic): diagnostic/test.

- [E0411](01_timeline.md#E0411): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C044_678059d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index 3d70199..e9e6b94 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -7,9 +7,10 @@ from env_client import make_env
    7      7  from approach import GeneratedApproach
    8      8  
    9      9  
   10        -def run(seed, verbose=False):
          10 +def run(seed, verbose=False, object_count=None):
   11     11      env = make_env()
   12        -    state, info = env.reset(seed=seed)
          12 +    options = {"object_count": object_count} if object_count is not None else None
          13 +    state, info = env.reset(seed=seed, options=options)
   13     14      approach = GeneratedApproach(env.action_space, env.observation_space, {})
   14     15      approach.reset(state, info)
   15     16      t0 = time.monotonic()
@@ -34,10 +35,11 @@ if __name__ == "__main__":
   34     35      ap.add_argument("--start", type=int, default=0)
   35     36      ap.add_argument("--n", type=int, default=10)
   36     37      ap.add_argument("--verbose", action="store_true")
          38 +    ap.add_argument("--count", type=int, default=None)
   37     39      args = ap.parse_args()
   38     40      results = []
   39     41      for seed in range(args.start, args.start + args.n):
   40        -        result = run(seed, args.verbose)
          42 +        result = run(seed, args.verbose, args.count)
   41     43          results.append(result)
   42     44          print(seed, result)
   43     45      print("success", sum(r[0] for r in results), "/", len(results), "by_count", Counter((r[2], r[0]) for r in results))
```

</details>

<a id="C045"></a>
<a id="R40"></a>
### C045 · Choose least-conflicting fallback parking slots

Commit `0e14ec7609b468597927230059f43346654fbc6d`; parents: 678059d4ec84d6608cd7d10084be4b9f6efe8e0e. Recorded author date: 2026-09-08T23:16:33+02:00.

File roles (automatic): policy.

- [E0417](01_timeline.md#E0417): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Pinned count-3 tests fail on seeds 1 and 3 → densify the parking grid and score fallback constraint violations.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0407](01_timeline.md#E0407), [E0411](01_timeline.md#E0411), [E0413](01_timeline.md#E0413), [E0415](01_timeline.md#E0415), [E0417](01_timeline.md#E0417).

Prior mapped post-edit test reports: [E0417](01_timeline.md#E0417). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C045_0e14ec7_approach.py) · [Exact all-file diff](evidence/diffs/C045_0e14ec7.diff)

[Previous saved controller snapshot](evidence/versions/C043_dafcc2f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index dfac8aa..8953f95 100644
--- a/approach.py
+++ b/approach.py
@@ -46,7 +46,7 @@ class GeneratedApproach:
   46     46          # Greedily reserve floor-clear parking columns, preferring positions far
   47     47          # from both the pickup and goal.  The grid is count-independent.
   48     48          # Keep parking poses one base radius away from both side walls.
   49        -        candidates = [0.20 + 0.10 * k for k in range(12)]
          49 +        candidates = [0.20 + 0.05 * k for k in range(23)]
   50     50          # Allocate outermost slots first so a later blocker never has to pass
   51     51          # through an earlier parked one on the way out of the goal region.
   52     52          candidates.sort(key=lambda x: (abs(x - sx), abs(x - tx)), reverse=True)
@@ -71,7 +71,20 @@ class GeneratedApproach:
   71     71                               (ow + state.get(q, "width")) / 2 + 0.08 for q in future)
   72     72                       and all(abs(x - px) > (ow + pw) / 2 + 0.12
   73     73                               for px, pw in used)]
   74        -            px = valid[0] if valid else candidates[len(used) % len(candidates)]
          74 +            if valid:
          75 +                px = valid[0]
          76 +            else:
          77 +                # If strict margins cannot all fit, choose the least-violating
          78 +                # slot instead of blindly reusing an occupied column.
          79 +                def slot_slack(x):
          80 +                    margins = [abs(x - sx) - goal_clearance]
          81 +                    margins += [abs(x - state.get(q, "x")) -
          82 +                                ((ow + state.get(q, "width")) / 2 + 0.08)
          83 +                                for q in future]
          84 +                    margins += [abs(x - qx) - ((ow + qw) / 2 + 0.12)
          85 +                                for qx, qw in used]
          86 +                    return min(margins)
          87 +                px = max(candidates, key=slot_slack)
   75     88              self.parking[o.name] = px
   76     89              used.append((px, ow))
   77     90          self.final_index = len(self.todo) - 1
```

</details>

<a id="C046"></a>
<a id="R41"></a>
### C046 · Increase clearance around future pickup columns

Commit `f87f63f3649fbf63ac884fb1b9fe168478b2930c`; parents: 0e14ec7609b468597927230059f43346654fbc6d. Recorded author date: 2026-09-08T23:17:21+02:00.

File roles (automatic): policy.

- [E0423](01_timeline.md#E0423): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Count-3 seed 4 now fails → increase clearance around future pickup locations.


Prior mapped context: [E0417](01_timeline.md#E0417), [E0419](01_timeline.md#E0419), [E0421](01_timeline.md#E0421), [E0423](01_timeline.md#E0423).

Prior mapped post-edit test reports: [E0423](01_timeline.md#E0423), [E0426](01_timeline.md#E0426). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C046_f87f63f_approach.py) · [Exact all-file diff](evidence/diffs/C046_f87f63f.diff)

[Previous saved controller snapshot](evidence/versions/C045_0e14ec7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8953f95..c88fb43 100644
--- a/approach.py
+++ b/approach.py
@@ -68,7 +68,7 @@ class GeneratedApproach:
   68     68              valid = [x for x in candidates
   69     69                       if abs(x - sx) > goal_clearance
   70     70                       and all(abs(x - state.get(q, "x")) >
   71        -                             (ow + state.get(q, "width")) / 2 + 0.08 for q in future)
          71 +                             (ow + state.get(q, "width")) / 2 + 0.14 for q in future)
   72     72                       and all(abs(x - px) > (ow + pw) / 2 + 0.12
   73     73                               for px, pw in used)]
   74     74              if valid:
@@ -79,7 +79,7 @@ class GeneratedApproach:
   79     79                  def slot_slack(x):
   80     80                      margins = [abs(x - sx) - goal_clearance]
   81     81                      margins += [abs(x - state.get(q, "x")) -
   82        -                                ((ow + state.get(q, "width")) / 2 + 0.08)
          82 +                                ((ow + state.get(q, "width")) / 2 + 0.14)
   83     83                                  for q in future]
   84     84                      margins += [abs(x - qx) - ((ow + qw) / 2 + 0.12)
   85     85                                  for qx, qw in used]
```

</details>

<a id="C047"></a>
<a id="R42"></a>
### C047 · Only relocate objects blocking the final placement footprint

Commit `6fc104f41b4160e0015842e8f62e768b6b985c9e`; parents: f87f63f3649fbf63ac884fb1b9fe168478b2930c. Recorded author date: 2026-09-08T23:19:39+02:00.

File roles (automatic): policy.

- [E0437](01_timeline.md#E0437): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Count-4 testing fails on four of five seeds → only relocate objects near the final placement footprint.

- L426 also reports a count-5 environment reset error. That is not evidence of robot-policy failure at count 5.

Prior mapped context: [E0424](01_timeline.md#E0424), [E0426](01_timeline.md#E0426), [E0428](01_timeline.md#E0428), [E0430](01_timeline.md#E0430), [E0432](01_timeline.md#E0432), [E0433](01_timeline.md#E0433), [E0435](01_timeline.md#E0435), [E0437](01_timeline.md#E0437).

Prior mapped post-edit test reports: [E0437](01_timeline.md#E0437). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C047_6fc104f_approach.py) · [Exact all-file diff](evidence/diffs/C047_6fc104f.diff)

[Previous saved controller snapshot](evidence/versions/C046_f87f63f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c88fb43..945dc26 100644
--- a/approach.py
+++ b/approach.py
@@ -12,10 +12,22 @@ class GeneratedApproach:
   12     12          rects = state.get_objects(self.types["rectangle"])
   13     13          target_name = state.get_objects(self.types["target_block"])[0].name
   14     14          target = state.get_object_from_name(target_name)
   15        -        obstacles = [o for o in rects if o.type.name == "rectangle" and state.get(o, "static") < 0.5]
          15 +        surface = state.get_objects(self.types["target_surface"])[0]
          16 +        sx, sw = state.get(surface, "x"), state.get(surface, "width")
          17 +        tx, tw = state.get(target, "x"), state.get(target, "width")
          18 +        target_angle = state.get(target, "theta")
          19 +        target_hx = 0.5 * (abs(math.cos(target_angle)) * tw +
          20 +                           abs(math.sin(target_angle)) * state.get(target, "height"))
          21 +        all_obstacles = [o for o in rects
          22 +                         if o.type.name == "rectangle" and state.get(o, "static") < 0.5]
          23 +        def blocks_goal(o):
          24 +            angle = state.get(o, "theta")
          25 +            hx = 0.5 * (abs(math.cos(angle)) * state.get(o, "width") +
          26 +                        abs(math.sin(angle)) * state.get(o, "height"))
          27 +            return abs(state.get(o, "x") - sx) < target_hx + hx + 0.025
          28 +        obstacles = [o for o in all_obstacles if blocks_goal(o)]
   16     29          obstacles.sort(key=lambda o: -state.get(o, "height"))
   17     30          # Temporarily lift the target only when it crowds an obstacle's access.
   18        -        tx, tw = state.get(target, "x"), state.get(target, "width")
   19     31          crowded = any(abs(tx - state.get(o, "x")) <
   20     32                        0.5 * (tw + state.get(o, "width")) + 0.14 for o in obstacles)
   21     33          def top_y(o):
@@ -26,9 +38,6 @@ class GeneratedApproach:
   26     38          tasks = sorted(obstacles, key=top_y, reverse=True)
   27     39          if crowded:
   28     40              target_top = top_y(target)
   29        -            target_angle = state.get(target, "theta")
   30        -            target_hx = 0.5 * (abs(math.cos(target_angle)) * tw +
   31        -                               abs(math.sin(target_angle)) * state.get(target, "height"))
   32     41              def must_precede_target(o):
   33     42                  angle = state.get(o, "theta")
   34     43                  hx = 0.5 * (abs(math.cos(angle)) * state.get(o, "width") +
@@ -41,8 +50,6 @@ class GeneratedApproach:
   41     50              tasks.insert(insert_at, target)
   42     51          self.todo = [o.name for o in tasks]
   43     52          self.todo.append(target_name)  # retrieve it last for the actual placement
   44        -        surface = state.get_objects(self.types["target_surface"])[0]
   45        -        sx, sw = state.get(surface, "x"), state.get(surface, "width")
   46     53          # Greedily reserve floor-clear parking columns, preferring positions far
   47     54          # from both the pickup and goal.  The grid is count-independent.
   48     55          # Keep parking poses one base radius away from both side walls.
```

</details>

<a id="C048"></a>
<a id="R43"></a>
### C048 · Include blockers near the placement sweep envelope

Commit `c91cb8e9be2aec3700f91693fbc5d99f41f6e2a3`; parents: 6fc104f41b4160e0015842e8f62e768b6b985c9e. Recorded author date: 2026-09-08T23:20:26+02:00.

File roles (automatic): policy.

- [E0441](01_timeline.md#E0441): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Filtering leaves baseline seed 6 and count-4 cases failing → widen the footprint used to select blockers.


Prior mapped context: [E0437](01_timeline.md#E0437), [E0439](01_timeline.md#E0439), [E0441](01_timeline.md#E0441).

Prior mapped post-edit test reports: [E0441](01_timeline.md#E0441). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C048_c91cb8e_approach.py) · [Exact all-file diff](evidence/diffs/C048_c91cb8e.diff)

[Previous saved controller snapshot](evidence/versions/C047_6fc104f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 945dc26..8d3b6a3 100644
--- a/approach.py
+++ b/approach.py
@@ -24,7 +24,9 @@ class GeneratedApproach:
   24     24              angle = state.get(o, "theta")
   25     25              hx = 0.5 * (abs(math.cos(angle)) * state.get(o, "width") +
   26     26                          abs(math.sin(angle)) * state.get(o, "height"))
   27        -            return abs(state.get(o, "x") - sx) < target_hx + hx + 0.025
          27 +            # Include near-edge objects because the gripper/base sweep has a
          28 +            # wider collision envelope than the block footprint itself.
          29 +            return abs(state.get(o, "x") - sx) < target_hx + hx + 0.12
   28     30          obstacles = [o for o in all_obstacles if blocks_goal(o)]
   29     31          obstacles.sort(key=lambda o: -state.get(o, "height"))
   30     32          # Temporarily lift the target only when it crowds an obstacle's access.
```

</details>

<a id="C049"></a>
<a id="R44"></a>
### C049 · Increase clearance from the final lowering corridor

Commit `bb1c5eb0368c5961989b6f2880180b9c46a128b5`; parents: c91cb8e9be2aec3700f91693fbc5d99f41f6e2a3. Recorded author date: 2026-09-08T23:21:04+02:00.

File roles (automatic): policy.

- [E0447](01_timeline.md#E0447): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Count-4 seed 1 still fails → enlarge the clearance around the final lowering location.


Prior mapped context: [E0441](01_timeline.md#E0441), [E0443](01_timeline.md#E0443), [E0445](01_timeline.md#E0445), [E0447](01_timeline.md#E0447).

Prior mapped post-edit test reports: [E0447](01_timeline.md#E0447), [E0451](01_timeline.md#E0451). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C049_bb1c5eb_approach.py) · [Exact all-file diff](evidence/diffs/C049_bb1c5eb.diff)

[Previous saved controller snapshot](evidence/versions/C048_c91cb8e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8d3b6a3..82b4498 100644
--- a/approach.py
+++ b/approach.py
@@ -71,7 +71,7 @@ class GeneratedApproach:
   71     71              used.append((self.target_park, tw))
   72     72          for o in obstacles:
   73     73              ow = state.get(o, "width")
   74        -            goal_clearance = sw / 2 + tw / 2 + ow / 2 + 0.03
          74 +            goal_clearance = sw / 2 + tw / 2 + ow / 2 + 0.10
   75     75              future = [q for q in obstacles + [target]
   76     76                        if q.name != o.name and first_rank.get(q.name, 10**9) > first_rank[o.name]]
   77     77              valid = [x for x in candidates
```

</details>

<a id="C050"></a>
<a id="R45"></a>
### C050 · Stack blockers when no safe horizontal slot exists

Commit `20d09c8656cf55177f2c3f77b7de178305af944c`; parents: bb1c5eb0368c5961989b6f2880180b9c46a128b5. Recorded author date: 2026-09-08T23:23:36+02:00.

File roles (automatic): policy.

- [E0458](01_timeline.md#E0458): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 93 fails with crowded horizontal parking → add a vertical stacking fallback.


Prior mapped context: [E0451](01_timeline.md#E0451), [E0453](01_timeline.md#E0453), [E0454](01_timeline.md#E0454), [E0456](01_timeline.md#E0456), [E0458](01_timeline.md#E0458).

Prior mapped post-edit test reports: [E0458](01_timeline.md#E0458). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C050_20d09c8_approach.py) · [Exact all-file diff](evidence/diffs/C050_20d09c8.diff)

[Previous saved controller snapshot](evidence/versions/C049_bb1c5eb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 82b4498..b38adba 100644
--- a/approach.py
+++ b/approach.py
@@ -60,6 +60,7 @@ class GeneratedApproach:
   60     60          # through an earlier parked one on the way out of the goal region.
   61     61          candidates.sort(key=lambda x: (abs(x - sx), abs(x - tx)), reverse=True)
   62     62          self.parking = {}
          63 +        self.parking_y = {}
   63     64          used = []
   64     65          first_rank = {}
   65     66          for rank, name in enumerate(self.todo):
@@ -68,7 +69,7 @@ class GeneratedApproach:
   68     69          self.target_park = tx
   69     70          if crowded:
   70     71              self.target_park = candidates[0]
   71        -            used.append((self.target_park, tw))
          72 +            used.append((self.target_park, tw, target_name))
   72     73          for o in obstacles:
   73     74              ow = state.get(o, "width")
   74     75              goal_clearance = sw / 2 + tw / 2 + ow / 2 + 0.10
@@ -79,7 +80,8 @@ class GeneratedApproach:
   79     80                       and all(abs(x - state.get(q, "x")) >
   80     81                               (ow + state.get(q, "width")) / 2 + 0.14 for q in future)
   81     82                       and all(abs(x - px) > (ow + pw) / 2 + 0.12
   82        -                             for px, pw in used)]
          83 +                             for px, pw, _ in used)]
          84 +            park_y = 0.30
   83     85              if valid:
   84     86                  px = valid[0]
   85     87              else:
@@ -91,11 +93,19 @@ class GeneratedApproach:
   91     93                                  ((ow + state.get(q, "width")) / 2 + 0.14)
   92     94                                  for q in future]
   93     95                      margins += [abs(x - qx) - ((ow + qw) / 2 + 0.12)
   94        -                                for qx, qw in used]
          96 +                                for qx, qw, _ in used]
   95     97                      return min(margins)
   96        -                px = max(candidates, key=slot_slack)
          98 +                blocker_slots = [(qx, name) for qx, _, name in used if name != target_name]
          99 +                if blocker_slots:
         100 +                    px, _ = max(blocker_slots, key=lambda item: abs(item[0] - sx))
         101 +                    level = sum(abs(qx - px) < 0.01 for qx, _, name in used
         102 +                                if name != target_name)
         103 +                    park_y = 0.30 + 0.20 * level
         104 +                else:
         105 +                    px = max(candidates, key=slot_slack)
   97    106              self.parking[o.name] = px
   98        -            used.append((px, ow))
         107 +            self.parking_y[o.name] = park_y
         108 +            used.append((px, ow, o.name))
   99    109          self.final_index = len(self.todo) - 1
  100    110          xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
  101    111          self.initial_x = {n: state.get(state.get_object_from_name(n), "x")
@@ -181,7 +191,8 @@ class GeneratedApproach:
  181    191                  self.attached = True
  182    192              # A modest vertical park is enough to clear the ground while still
  183    193              # leaving room above it for a later verified re-grasp.
  184        -            park_y = 0.45 if (obj.type.name == "target_block" and not is_target) else 0.30
         194 +            park_y = (0.45 if obj.type.name == "target_block"
         195 +                      else self.parking_y.get(obj.name, 0.30))
  185    196              parked_high_enough = (not is_target and self.attached and oy >= park_y)
  186    197              lift_limit = self.safe_y if is_target else 0.74
  187    198              if ry < lift_limit and not parked_high_enough:
```

</details>

<a id="C051"></a>
<a id="R46"></a>
### C051 · Stack only outside target transit corridor

Commit `5210b1a6485b9c8c862638b37ae5f2b56dff06fe`; parents: 20d09c8656cf55177f2c3f77b7de178305af944c. Recorded author date: 2026-09-08T23:25:02+02:00.

File roles (automatic): policy.

- [E0464](01_timeline.md#E0464): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Stacking fixes seed 93 but breaks count-4 cases → restrict stacking to outer columns and small blocker sets.

- Multiple code decisions change together. Outcome attribution to an individual component requires further checking.

Prior mapped context: [E0458](01_timeline.md#E0458), [E0460](01_timeline.md#E0460), [E0462](01_timeline.md#E0462), [E0464](01_timeline.md#E0464).

Prior mapped post-edit test reports: [E0464](01_timeline.md#E0464), [E0469](01_timeline.md#E0469). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C051_5210b1a_approach.py) · [Exact all-file diff](evidence/diffs/C051_5210b1a.diff)

[Previous saved controller snapshot](evidence/versions/C050_20d09c8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b38adba..cdcf5c9 100644
--- a/approach.py
+++ b/approach.py
@@ -96,8 +96,10 @@ class GeneratedApproach:
   96     96                                  for qx, qw, _ in used]
   97     97                      return min(margins)
   98     98                  blocker_slots = [(qx, name) for qx, _, name in used if name != target_name]
   99        -                if blocker_slots:
  100        -                    px, _ = max(blocker_slots, key=lambda item: abs(item[0] - sx))
          99 +                stack_slots = [item for item in blocker_slots
         100 +                               if not min(tx, sx) - 0.10 < item[0] < max(tx, sx) + 0.10]
         101 +                if len(obstacles) <= 2 and stack_slots:
         102 +                    px, _ = max(stack_slots, key=lambda item: abs(item[0] - sx))
  101    103                      level = sum(abs(qx - px) < 0.01 for qx, _, name in used
  102    104                                  if name != target_name)
  103    105                      park_y = 0.30 + 0.20 * level
```

</details>

<a id="C052"></a>
<a id="R47"></a>
### C052 · Shorten recovery lift after failed grasps

Commit `4868fc2a012627cd4879d4579300529e3b15d8dd`; parents: 5210b1a6485b9c8c862638b37ae5f2b56dff06fe. Recorded author date: 2026-09-08T23:27:21+02:00.

File roles (automatic): policy.

- [E0475](01_timeline.md#E0475): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** New count-4 failures appear → shorten the verification/recovery lift when no attachment is detected.


Prior mapped context: [E0465](01_timeline.md#E0465), [E0469](01_timeline.md#E0469), [E0471](01_timeline.md#E0471), [E0473](01_timeline.md#E0473), [E0475](01_timeline.md#E0475).

Prior mapped post-edit test reports: [E0475](01_timeline.md#E0475). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C052_4868fc2_approach.py) · [Exact all-file diff](evidence/diffs/C052_4868fc2.diff)

[Previous saved controller snapshot](evidence/versions/C051_5210b1a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cdcf5c9..b96faf3 100644
--- a/approach.py
+++ b/approach.py
@@ -182,6 +182,7 @@ class GeneratedApproach:
  182    182              self.last_robot_y = ry
  183    183              if self.stalled >= 2 or ry < 0.18:
  184    184                  self.phase = "lift"
         185 +                self.contact_robot_y = ry
  185    186              else:
  186    187                  # Fine approach is essential: collision resolution rejects an
  187    188                  # overshooting move wholesale, leaving the vacuum just off-contact.
@@ -196,7 +197,10 @@ class GeneratedApproach:
  196    197              park_y = (0.45 if obj.type.name == "target_block"
  197    198                        else self.parking_y.get(obj.name, 0.30))
  198    199              parked_high_enough = (not is_target and self.attached and oy >= park_y)
  199        -            lift_limit = self.safe_y if is_target else 0.74
         200 +            if not self.attached:
         201 +                lift_limit = min(0.74, self.contact_robot_y + 0.15)
         202 +            else:
         203 +                lift_limit = self.safe_y if is_target else 0.74
  200    204              if ry < lift_limit and not parked_high_enough:
  201    205                  return self._action(dy=min(0.05, self.safe_y - ry), vac=1.0)
  202    206              if not self.attached:
```

</details>

<a id="C053"></a>
<a id="R48"></a>
### C053 · Add tolerance to failed-grasp recovery height

Commit `7cfa55b4e6f9afeae4855f47dde1f5c2462a57a5`; parents: 4868fc2a012627cd4879d4579300529e3b15d8dd. Recorded author date: 2026-09-08T23:28:12+02:00.

File roles (automatic): policy.

- [E0481](01_timeline.md#E0481): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Count-4 seed 5 still fails → add a tolerance to the lift-height stopping condition.


Prior mapped context: [E0475](01_timeline.md#E0475), [E0477](01_timeline.md#E0477), [E0479](01_timeline.md#E0479), [E0481](01_timeline.md#E0481).

Prior mapped post-edit test reports: [E0481](01_timeline.md#E0481). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C053_7cfa55b_approach.py) · [Exact all-file diff](evidence/diffs/C053_7cfa55b.diff)

[Previous saved controller snapshot](evidence/versions/C052_4868fc2_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b96faf3..46a8f2a 100644
--- a/approach.py
+++ b/approach.py
@@ -201,7 +201,7 @@ class GeneratedApproach:
  201    201                  lift_limit = min(0.74, self.contact_robot_y + 0.15)
  202    202              else:
  203    203                  lift_limit = self.safe_y if is_target else 0.74
  204        -            if ry < lift_limit and not parked_high_enough:
         204 +            if ry < lift_limit - 0.004 and not parked_high_enough:
  205    205                  return self._action(dy=min(0.05, self.safe_y - ry), vac=1.0)
  206    206              if not self.attached:
  207    207                  self.retry += 1
```

</details>

<a id="C054"></a>
<a id="R49"></a>
### C054 · Recover when verification lift is collision-blocked

Commit `af3dcdd680dad5766ccec9c50f3e6ae84ec4255b`; parents: 7cfa55b4e6f9afeae4855f47dde1f5c2462a57a5. Recorded author date: 2026-09-08T23:29:11+02:00.

File roles (automatic): policy.

- [E0489](01_timeline.md#E0489): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 5 remains stuck in lift → detect vertical stalls and enter recovery.


Prior mapped context: [E0481](01_timeline.md#E0481), [E0483](01_timeline.md#E0483), [E0485](01_timeline.md#E0485), [E0487](01_timeline.md#E0487), [E0489](01_timeline.md#E0489).

Prior mapped post-edit test reports: [E0489](01_timeline.md#E0489), [E0491](01_timeline.md#E0491), [E0493](01_timeline.md#E0493). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C054_af3dcdd_approach.py) · [Exact all-file diff](evidence/diffs/C054_af3dcdd.diff)

[Previous saved controller snapshot](evidence/versions/C053_7cfa55b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 46a8f2a..4881cfd 100644
--- a/approach.py
+++ b/approach.py
@@ -183,11 +183,18 @@ class GeneratedApproach:
  183    183              if self.stalled >= 2 or ry < 0.18:
  184    184                  self.phase = "lift"
  185    185                  self.contact_robot_y = ry
         186 +                self.stalled = 0
         187 +                self.last_robot_y = ry
  186    188              else:
  187    189                  # Fine approach is essential: collision resolution rejects an
  188    190                  # overshooting move wholesale, leaving the vacuum just off-contact.
  189    191                  return self._action(dy=-0.01, vac=1.0)
  190    192          if self.phase == "lift":
         193 +            if abs(ry - self.last_robot_y) < 0.001:
         194 +                self.stalled += 1
         195 +            else:
         196 +                self.stalled = 0
         197 +            self.last_robot_y = ry
  191    198              if oy > self.pick_y + 0.015:
  192    199                  if not self.attached:
  193    200                      self.grasp_dx = ox - rx
@@ -201,7 +208,7 @@ class GeneratedApproach:
  201    208                  lift_limit = min(0.74, self.contact_robot_y + 0.15)
  202    209              else:
  203    210                  lift_limit = self.safe_y if is_target else 0.74
  204        -            if ry < lift_limit - 0.004 and not parked_high_enough:
         211 +            if ry < lift_limit - 0.004 and not parked_high_enough and self.stalled < 2:
  205    212                  return self._action(dy=min(0.05, self.safe_y - ry), vac=1.0)
  206    213              if not self.attached:
  207    214                  self.retry += 1
```

</details>

<a id="C055"></a>
<a id="R50"></a>
### C055 · Add boundary columns for dense blocker parking

Commit `05d09719879202800efd5443054cddd535fa8165`; parents: af3dcdd680dad5766ccec9c50f3e6ae84ec4255b. Recorded author date: 2026-09-08T23:30:57+02:00.

File roles (automatic): policy.

- [E0500](01_timeline.md#E0500): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Count-4 seed 7 remains unresolved → add parking candidates near both boundaries.


Prior mapped context: [E0493](01_timeline.md#E0493), [E0495](01_timeline.md#E0495), [E0496](01_timeline.md#E0496), [E0498](01_timeline.md#E0498), [E0500](01_timeline.md#E0500).

Prior mapped post-edit test reports: [E0500](01_timeline.md#E0500), [E0502](01_timeline.md#E0502), [E0509](01_timeline.md#E0509), [E0511](01_timeline.md#E0511). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C055_05d0971_approach.py) · [Exact all-file diff](evidence/diffs/C055_05d0971.diff)

[Previous saved controller snapshot](evidence/versions/C054_af3dcdd_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4881cfd..0167393 100644
--- a/approach.py
+++ b/approach.py
@@ -55,7 +55,7 @@ class GeneratedApproach:
   55     55          # Greedily reserve floor-clear parking columns, preferring positions far
   56     56          # from both the pickup and goal.  The grid is count-independent.
   57     57          # Keep parking poses one base radius away from both side walls.
   58        -        candidates = [0.20 + 0.05 * k for k in range(23)]
          58 +        candidates = [0.12] + [0.20 + 0.05 * k for k in range(23)] + [1.38, 1.46]
   59     59          # Allocate outermost slots first so a later blocker never has to pass
   60     60          # through an earlier parked one on the way out of the goal region.
   61     61          candidates.sort(key=lambda x: (abs(x - sx), abs(x - tx)), reverse=True)
```

</details>

<a id="C056"></a>
<a id="R51"></a>
### C056 · Skip blockers already displaced from the goal

Commit `4897e46269b5d9f885dd2a13e79b864e96a206f2`; parents: 05d09719879202800efd5443054cddd535fa8165. Recorded author date: 2026-09-08T23:34:19+02:00.

File roles (automatic): policy.

- [E0518](01_timeline.md#E0518): commit title in command; output may not confirm creation.

**Prior analyst description (carried forward, not independently relabeled):** Seed 53 fails after another object has displaced a blocker → recheck relevance and skip blockers already clear of the destination.

- Post-edit context includes final validation and stopping. L528 attempts a confidence-marker commit but returns nothing to commit; it is not a saved new policy revision.

Prior mapped context: [E0507](01_timeline.md#E0507), [E0511](01_timeline.md#E0511), [E0513](01_timeline.md#E0513), [E0514](01_timeline.md#E0514), [E0516](01_timeline.md#E0516), [E0518](01_timeline.md#E0518).

Prior mapped post-edit test reports: [E0518](01_timeline.md#E0518), [E0523](01_timeline.md#E0523). These are not isolated causal tests.

[Controller after this commit](evidence/versions/C056_4897e46_approach.py) · [Exact all-file diff](evidence/diffs/C056_4897e46.diff)

[Previous saved controller snapshot](evidence/versions/C055_05d0971_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0167393..0d50efd 100644
--- a/approach.py
+++ b/approach.py
@@ -141,6 +141,21 @@ class GeneratedApproach:
  141    141          ox, oy = state.get(obj, "x"), state.get(obj, "y")
  142    142          width = state.get(obj, "width")
  143    143  
         144 +        if not is_target and obj.type.name == "rectangle" and self.phase in ("rise", "align"):
         145 +            angle = state.get(obj, "theta")
         146 +            obstacle_hx = 0.5 * (abs(math.cos(angle)) * width +
         147 +                                 abs(math.sin(angle)) * state.get(obj, "height"))
         148 +            target = state.get_objects(self.types["target_block"])[0]
         149 +            target_angle = state.get(target, "theta")
         150 +            target_hx = 0.5 * (abs(math.cos(target_angle)) * state.get(target, "width") +
         151 +                               abs(math.sin(target_angle)) * state.get(target, "height"))
         152 +            if abs(ox - state.get(surface, "x")) >= obstacle_hx + target_hx + 0.12:
         153 +                self.index += 1
         154 +                self.retry, self.attached = 0, False
         155 +                self.phase = "rise"
         156 +                self.last_robot_x = None
         157 +                return self._action()
         158 +
  144    159          if self.phase == "orient":
  145    160              err = (-math.pi / 2 - theta + math.pi) % (2 * math.pi) - math.pi
  146    161              if abs(err) < 0.025:
```

</details>

