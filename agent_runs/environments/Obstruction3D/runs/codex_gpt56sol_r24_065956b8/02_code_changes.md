# Obstruction3D · gpt-5.6-sol · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `6051cff` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `25581ec` | Add safe baseline object-centric policy | approach.py | [E0009](01_timeline.md#E0009) |
| [C003](#C003) · `e34a8b1` | Add robot dynamics probe script | probe_dynamics.py | No matched commit command/output |
| [C004](#C004) · `db57f3d` | Add focused grasp mechanics probe | probe_grasp.py | No matched commit command/output |
| [C005](#C005) · `bda251a` | Extend probe with random grasp search | probe_grasp.py | No matched commit command/output |
| [C006](#C006) · `dfb0363` | Extend probes for object state and gripper controls | probe_dynamics.py | No matched commit command/output |
| [C007](#C007) · `0aa23e6` | Add targeted grasp semantics probe | probe_grasp.py | No matched commit command/output |
| [C008](#C008) · `f54406c` | Restore concurrent grasp probe after shared-file race | probe_grasp.py | No matched commit command/output |
| [C009](#C009) · `4aef2dd` | Probe pitch-joint grid for target grasp | probe_grasp.py | No matched commit command/output |
| [C010](#C010) · `77f8416` | Add first Kinova geometry-driven pick-place controller | approach.py, ik_probe.py, inspect_env.py, probe_instances.py, quick_probe.py, scan_grasp.py | [E0054](01_timeline.md#E0054) |
| [C011](#C011) · `8a5f258` | Probe Kinova arm mount offset for grasping | probe_mount_offset.py | No matched commit command/output |
| [C012](#C012) · `e76da11` | Expand grasp search across wrist pitch | probe_grasp.py | No matched commit command/output |
| [C013](#C013) · `0fb74a1` | Add live multi-seed policy test harness | probe_mount_offset.py, test_approach.py | [E0060](01_timeline.md#E0060) |
| [C014](#C014) · `e58258a` | Measure end-effector effects via attached target | probe_attached_effects.py | No matched commit command/output |
| [C015](#C015) · `ce292be` | Add instance geometry and targeted grasp probes | probe_instances.py | No matched commit command/output |
| [C016](#C016) · `520ecd3` | Reproduce grasp and test direct carried placement | probe_grasp.py | No matched commit command/output |
| [C017](#C017) · `df38b42` | Handle variable obstructions with feedback-corrected placements | approach.py | [E0064](01_timeline.md#E0064) |
| [C018](#C018) · `af7f318` | Probe gripper release while moving | probe_instances.py | No matched commit command/output |
| [C019](#C019) · `0777df1` | Use collision-robust fingertip grasp offset | approach.py | [E0068](01_timeline.md#E0068) |
| [C020](#C020) · `ccc4f71` | Measure carried-object response near grasp pose | probe_grasp.py | No matched commit command/output |
| [C021](#C021) · `fd657ac` | Probe supported-object release at pickup pose | probe_instances.py | No matched commit command/output |
| [C022](#C022) · `42aa406` | Fix carried-object perturbation probe | probe_grasp.py | No matched commit command/output |
| [C023](#C023) · `997a264` | Test lifted transport before target release | probe_grasp.py | No matched commit command/output |
| [C024](#C024) · `7fc6982` | Preserve tool orientation through placement IK probe | probe_instances.py | No matched commit command/output |
| [C025](#C025) · `8574b11` | Preserve grasp orientation and lower objects onto support | approach.py | [E0077](01_timeline.md#E0077) |
| [C026](#C026) · `9a12aef` | Use Cartesian descent waypoints in placement probe | probe_instances.py | No matched commit command/output |
| [C027](#C027) · `a651114` | Use safe vertical lift and staged Cartesian descent | approach.py | [E0081](01_timeline.md#E0081) |
| [C028](#C028) · `499d0e3` | Generalize discovered grasp with base alignment | probe_grasp.py | No matched commit command/output |
| [C029](#C029) · `a573a7f` | Refine supported descent with close vertical waypoints | approach.py | [E0087](01_timeline.md#E0087) |
| [C030](#C030) · `2906ab9` | Handle full target y range in grasp sequence | probe_grasp.py | No matched commit command/output |
| [C031](#C031) · `ab7b166` | Calibrate supported release height | approach.py | [E0093](01_timeline.md#E0093) |
| [C032](#C032) · `55de0b2` | Interpolate a far-reach target grasp anchor | probe_grasp.py | No matched commit command/output |
| [C033](#C033) · `20d3842` | Approach pickups through collision-safe Cartesian waypoints | approach.py | [E0101](01_timeline.md#E0101) |
| [C034](#C034) · `f314793` | Test calibrated grasp on named obstructions | probe_grasp.py | No matched commit command/output |
| [C035](#C035) · `500304a` | Improve dense-obstruction ordering lift and retraction | approach.py | [E0111](01_timeline.md#E0111) |
| [C036](#C036) · `c9b0cbf` | Add calibrated target grasp and obstruction recovery | approach.py | [E0119](01_timeline.md#E0119) |
| [C037](#C037) · `98f2ea5` | Reposition mobile base for reliable picks and transfers | approach.py | [E0125](01_timeline.md#E0125) |
| [C038](#C038) · `9c8397b` | Defer collision-blocked obstruction grasps | approach.py | [E0131](01_timeline.md#E0131) |
| [C039](#C039) · `3e03d41` | Grasp obstructions near their collision-free top edge | approach.py | [E0137](01_timeline.md#E0137) |
| [C040](#C040) · `d7e9429` | Tune elevated obstruction pinch height | approach.py | [E0143](01_timeline.md#E0143) |
| [C041](#C041) · `db6fc03` | Use calibrated base-translated grasp for every block | approach.py | [E0151](01_timeline.md#E0151) |
| [C042](#C042) · `9fa169b` | Add pinned-count stress validation runner | validate_pinned.py | No matched commit command/output |
| [C043](#C043) · `7e72b0a` | Separate safe base translation from grasp posture motion | approach.py, validate_30_0.out, validate_31_1.out, validate_32_3.out, validate_33_5.out | [E0169](01_timeline.md#E0169) |
| [C044](#C044) · `bcaa08b` | Lift crowded blocks with collision-safe increments | approach.py, validate_30_0.out, validate_31_1.out, validate_32_3.out, validate_33_5.out | [E0177](01_timeline.md#E0177) |
| [C045](#C045) · `febba60` | Sidestep dense neighbors while lifting obstructions | approach.py | [E0183](01_timeline.md#E0183) |
| [C046](#C046) · `d0c15d2` | Adapt grasp height and rotate through blocked candidates | approach.py | [E0197](01_timeline.md#E0197) |
| [C047](#C047) · `3aadb3b` | Recover from collision-stalled grasp postures | approach.py | [E0207](01_timeline.md#E0207) |
| [C048](#C048) · `8482e50` | Distribute parked obstructions across both table ends | approach.py | [E0215](01_timeline.md#E0215) |
| [C049](#C049) · `b782c30` | Use arm-reachable obstruction parking columns | approach.py | [E0221](01_timeline.md#E0221) |
| [C050](#C050) · `0765ea9` | Fallback to IK for size-sensitive obstruction grasps | approach.py | [E0239](01_timeline.md#E0239) |
| [C051](#C051) · `da141eb` | Center the fallback IK pinch on small blocks | approach.py | [E0245](01_timeline.md#E0245) |
| [C052](#C052) · `b81f1b8` | Run IK fallback from calibrated pedestal origin | approach.py | [E0249](01_timeline.md#E0249) |
| [C053](#C053) · `5aaa70f` | Use stable obstruction order with deferred retries | approach.py | [E0255](01_timeline.md#E0255) |
| [C054](#C054) · `0403801` | Route stalled calibrated grasps through IK fallback | approach.py | [E0261](01_timeline.md#E0261) |
| [C055](#C055) · `0a0929b` | Keep all parking slots opposite the target region | approach.py | [E0267](01_timeline.md#E0267) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `6051cff63c4ab8e505a1389b5f516b5890442e20`; parents: none (initial snapshot). Recorded author date: 2026-09-09T15:16:47+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_6051cff.diff)

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
index 0000000..98c1f5d
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1,129 @@
           1 +{
           2 +  "host": "127.0.0.1",
           3 +  "port": 45091,
           4 +  "token": "d22ee82bdd5a0a64e200b647ebf9f5b0",
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
### C002 · Add safe baseline object-centric policy

Commit `25581ec185ed66f817fa983d15a083866b0ef4e3`; parents: 6051cff63c4ab8e505a1389b5f516b5890442e20. Recorded author date: 2026-09-09T15:17:23+02:00.

File roles (automatic): policy.

- [E0009](01_timeline.md#E0009): commit hash in recorded output.
[Controller after this commit](evidence/versions/C002_25581ec_approach.py) · [Exact all-file diff](evidence/diffs/C002_25581ec.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..1faa0cb
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,16 @@
           1 +"""Policy for the Obstruction3D black-box manipulation task."""
           2 +
           3 +import numpy as np
           4 +
           5 +
           6 +class GeneratedApproach:
           7 +    def __init__(self, action_space, observation_space, primitives):
           8 +        self.action_space = action_space
           9 +        self.observation_space = observation_space
          10 +
          11 +    def reset(self, state, info):
          12 +        pass
          13 +
          14 +    def get_action(self, state):
          15 +        # Safe baseline; replaced as dynamics are identified.
          16 +        return np.zeros(self.action_space.shape, dtype=np.float32)
```

</details>

<a id="C003"></a>
### C003 · Add robot dynamics probe script

Commit `e34a8b1f55f13c4a773dafa44c7fbdf38da02ec5`; parents: 25581ec185ed66f817fa983d15a083866b0ef4e3. Recorded author date: 2026-09-09T15:18:15+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C003_e34a8b1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dynamics.py b/probe_dynamics.py
new file mode 100644
index 0000000..00100ef
--- /dev/null
+++ b/probe_dynamics.py
@@ -0,0 +1,70 @@
           1 +"""Small black-box probes for Obstruction3DEnv dynamics."""
           2 +
           3 +import numpy as np
           4 +
           5 +from env_client import make_env
           6 +
           7 +
           8 +ROBOT_FEATURES = (
           9 +    "pos_base_x", "pos_base_y", "pos_base_rot",
          10 +    "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7",
          11 +    "finger_state", "grasp_active",
          12 +    "grasp_tf_x", "grasp_tf_y", "grasp_tf_z",
          13 +    "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw",
          14 +)
          15 +
          16 +
          17 +def robot_values(state):
          18 +    robot = state.get_object_from_name("robot")
          19 +    return np.array([state.get(robot, f) for f in ROBOT_FEATURES], dtype=float)
          20 +
          21 +
          22 +def main():
          23 +    env = make_env()
          24 +    state, info = env.reset(seed=0)
          25 +    print("names", state.get_object_names())
          26 +    for name in state.get_object_names():
          27 +        obj = state.get_object_from_name(name)
          28 +        print("object", name, "type", getattr(obj, "type", None), "repr", repr(obj))
          29 +    print("robot baseline", dict(zip(ROBOT_FEATURES, robot_values(state))))
          30 +    env.close()
          31 +
          32 +    # Independent one-step effects from exactly the same initial state.
          33 +    for action_i in range(11):
          34 +        env = make_env()
          35 +        before, _ = env.reset(seed=0)
          36 +        b = robot_values(before)
          37 +        action = np.zeros(11, dtype=np.float32)
          38 +        action[action_i] = 0.2 if action_i < 10 else 1.0
          39 +        after, reward, terminated, truncated, _ = env.step(action)
          40 +        a = robot_values(after)
          41 +        changed = {
          42 +            feature: round(float(delta), 7)
          43 +            for feature, delta in zip(ROBOT_FEATURES, a - b)
          44 +            if abs(delta) > 1e-7
          45 +        }
          46 +        print("one_step", action_i, "changed", changed,
          47 +              "reward/done", reward, terminated, truncated)
          48 +        env.close()
          49 +
          50 +    # Cumulative response and any action clipping / rate effects.
          51 +    for action_i in range(10):
          52 +        env = make_env()
          53 +        state, _ = env.reset(seed=0)
          54 +        b = robot_values(state)
          55 +        action = np.zeros(11, dtype=np.float32)
          56 +        action[action_i] = 0.2
          57 +        for _ in range(5):
          58 +            state, _, _, _, _ = env.step(action)
          59 +        delta = robot_values(state) - b
          60 +        changed = {
          61 +            feature: round(float(d), 6)
          62 +            for feature, d in zip(ROBOT_FEATURES, delta)
          63 +            if abs(d) > 1e-7
          64 +        }
          65 +        print("five_step", action_i, changed)
          66 +        env.close()
          67 +
          68 +
          69 +if __name__ == "__main__":
          70 +    main()
```

</details>

<a id="C004"></a>
### C004 · Add focused grasp mechanics probe

Commit `db57f3dd7d49257bcf0e27ae95102bf745baaf71`; parents: e34a8b1f55f13c4a773dafa44c7fbdf38da02ec5. Recorded author date: 2026-09-09T15:18:17+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C004_db57f3d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
new file mode 100644
index 0000000..8817979
--- /dev/null
+++ b/probe_grasp.py
@@ -0,0 +1,46 @@
           1 +"""Focused black-box probes for Obstruction3D grasp mechanics."""
           2 +
           3 +import numpy as np
           4 +
           5 +from env_client import make_env
           6 +
           7 +
           8 +def read(state, obj, names):
           9 +    return {name: float(state.get(obj, name)) for name in names}
          10 +
          11 +
          12 +def snapshot(state):
          13 +    out = {}
          14 +    for name in state.get_object_names():
          15 +        obj = state.get_object_from_name(name)
          16 +        try:
          17 +            out[name] = read(state, obj, ["pose_x", "pose_y", "pose_z", "grasp_active"])
          18 +        except Exception:
          19 +            out[name] = read(state, obj, [
          20 +                "pos_base_x", "pos_base_y", "pos_base_rot",
          21 +                "joint_1", "joint_2", "joint_3", "joint_4", "joint_5",
          22 +                "joint_6", "joint_7", "finger_state", "grasp_active",
          23 +                "grasp_tf_x", "grasp_tf_y", "grasp_tf_z",
          24 +            ])
          25 +    return out
          26 +
          27 +
          28 +def main():
          29 +    env = make_env()
          30 +    state, info = env.reset(seed=0)
          31 +    print("max_steps", env.max_steps, "info", info)
          32 +    print(snapshot(state))
          33 +    for label, action in [
          34 +        ("close", [0] * 10 + [-1]),
          35 +        ("open", [0] * 10 + [1]),
          36 +        ("all_joint_plus", [0, 0, 0] + [0.2] * 7 + [0]),
          37 +        ("all_joint_minus", [0, 0, 0] + [-0.2] * 7 + [0]),
          38 +        ("base_plus", [0.2, 0.2, 0.2] + [0] * 8),
          39 +    ]:
          40 +        state, reward, term, trunc, info = env.step(np.asarray(action, dtype=np.float32))
          41 +        print(label, reward, term, trunc, info, snapshot(state))
          42 +    env.close()
          43 +
          44 +
          45 +if __name__ == "__main__":
          46 +    main()
```

</details>

<a id="C005"></a>
### C005 · Extend probe with random grasp search

Commit `bda251a1073395f7f591f6e9936599672cbe9a8e`; parents: db57f3dd7d49257bcf0e27ae95102bf745baaf71. Recorded author date: 2026-09-09T15:19:15+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C005_bda251a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index 8817979..4ce49dd 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -42,5 +42,41 @@ def main():
   42     42      env.close()
   43     43  
   44     44  
          45 +def random_search(seed=0, steps=1000):
          46 +    """Look for any attachment while broadly random-walking configuration."""
          47 +    rng = np.random.default_rng(seed + 991)
          48 +    env = make_env()
          49 +    state, _ = env.reset(seed=seed)
          50 +    initial = snapshot(state)
          51 +    print("seed", seed, "objects", initial)
          52 +    last_positions = {k: (v.get("pose_x"), v.get("pose_y"), v.get("pose_z"))
          53 +                      for k, v in initial.items() if "pose_x" in v}
          54 +    for t in range(steps):
          55 +        action = np.zeros(11, dtype=np.float32)
          56 +        # Persistent random motion explores configurations better than white noise.
          57 +        action[:10] = rng.choice([-0.2, 0.0, 0.2], size=10, p=[0.3, 0.4, 0.3])
          58 +        action[10] = -1.0
          59 +        state, reward, term, trunc, info = env.step(action)
          60 +        snap = snapshot(state)
          61 +        moved = []
          62 +        for k, old in last_positions.items():
          63 +            new = tuple(snap[k].get(x) for x in ("pose_x", "pose_y", "pose_z"))
          64 +            if max(abs(a - b) for a, b in zip(old, new)) > 1e-5:
          65 +                moved.append((k, old, new))
          66 +            last_positions[k] = new
          67 +        if moved or snap["robot"]["grasp_active"]:
          68 +            print("EVENT", t, "a", action.tolist(), "moved", moved,
          69 +                  "robot", snap["robot"])
          70 +        if snap["robot"]["grasp_active"] or term or trunc:
          71 +            print("END", t, reward, term, trunc, snap)
          72 +            break
          73 +    env.close()
          74 +
          75 +
   45     76  if __name__ == "__main__":
   46        -    main()
          77 +    import argparse
          78 +    parser = argparse.ArgumentParser()
          79 +    parser.add_argument("--random", action="store_true")
          80 +    parser.add_argument("--seed", type=int, default=0)
          81 +    args = parser.parse_args()
          82 +    random_search(args.seed) if args.random else main()
```

</details>

<a id="C006"></a>
### C006 · Extend probes for object state and gripper controls

Commit `dfb0363511696cbcf9356c5fd8a6d455ab426006`; parents: bda251a1073395f7f591f6e9936599672cbe9a8e. Recorded author date: 2026-09-09T15:21:50+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C006_dfb0363.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dynamics.py b/probe_dynamics.py
index 00100ef..0930c4e 100644
--- a/probe_dynamics.py
+++ b/probe_dynamics.py
@@ -27,6 +27,13 @@ def main():
   27     27          obj = state.get_object_from_name(name)
   28     28          print("object", name, "type", getattr(obj, "type", None), "repr", repr(obj))
   29     29      print("robot baseline", dict(zip(ROBOT_FEATURES, robot_values(state))))
          30 +    cuboid_features = (
          31 +        "pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw",
          32 +        "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z",
          33 +    )
          34 +    for name in sorted(n for n in state.get_object_names() if n != "robot"):
          35 +        obj = state.get_object_from_name(name)
          36 +        print("cuboid", name, {f: state.get(obj, f) for f in cuboid_features})
   30     37      env.close()
   31     38  
   32     39      # Independent one-step effects from exactly the same initial state.
@@ -47,6 +54,31 @@ def main():
   47     54                "reward/done", reward, terminated, truncated)
   48     55          env.close()
   49     56  
          57 +    env = make_env()
          58 +    for label, action_i, magnitude in (
          59 +        ("base_x_negative", 0, -0.2),
          60 +        ("base_y_negative", 1, -0.2),
          61 +        ("base_rot_negative", 2, -0.2),
          62 +        ("close", 10, -1.0),
          63 +    ):
          64 +        before, _ = env.reset(seed=0)
          65 +        b = robot_values(before)
          66 +        action = np.zeros(11, dtype=np.float32)
          67 +        action[action_i] = magnitude
          68 +        after, reward, terminated, truncated, _ = env.step(action)
          69 +        a = robot_values(after)
          70 +        changed = {
          71 +            feature: round(float(delta), 7)
          72 +            for feature, delta in zip(ROBOT_FEATURES, a - b)
          73 +            if abs(delta) > 1e-7
          74 +        }
          75 +        print(label, changed, "robot", dict(zip(ROBOT_FEATURES, a)))
          76 +        for name in sorted(n for n in after.get_object_names() if n != "robot"):
          77 +            obj = after.get_object_from_name(name)
          78 +            if after.get(obj, "grasp_active"):
          79 +                print("grasped", name)
          80 +    env.close()
          81 +
   50     82      # Cumulative response and any action clipping / rate effects.
   51     83      for action_i in range(10):
   52     84          env = make_env()
```

</details>

<a id="C007"></a>
### C007 · Add targeted grasp semantics probe

Commit `0aa23e659ca50d86cd08a97e61fd13e4a5acd99e`; parents: dfb0363511696cbcf9356c5fd8a6d455ab426006. Recorded author date: 2026-09-09T15:23:10+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C007_0aa23e6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index 4ce49dd..d7156c5 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -1,82 +1,45 @@
    1        -"""Focused black-box probes for Obstruction3D grasp mechanics."""
           1 +"""Try simple base-alignment grasps and report attachment-transform semantics."""
    2      2  
    3      3  import numpy as np
    4      4  
    5      5  from env_client import make_env
    6      6  
    7      7  
    8        -def read(state, obj, names):
    9        -    return {name: float(state.get(obj, name)) for name in names}
   10        -
   11        -
   12        -def snapshot(state):
   13        -    out = {}
   14        -    for name in state.get_object_names():
   15        -        obj = state.get_object_from_name(name)
   16        -        try:
   17        -            out[name] = read(state, obj, ["pose_x", "pose_y", "pose_z", "grasp_active"])
   18        -        except Exception:
   19        -            out[name] = read(state, obj, [
   20        -                "pos_base_x", "pos_base_y", "pos_base_rot",
   21        -                "joint_1", "joint_2", "joint_3", "joint_4", "joint_5",
   22        -                "joint_6", "joint_7", "finger_state", "grasp_active",
   23        -                "grasp_tf_x", "grasp_tf_y", "grasp_tf_z",
   24        -            ])
   25        -    return out
           8 +def value(state, name, feature):
           9 +    return state.get(state.get_object_from_name(name), feature)
   26     10  
   27     11  
   28     12  def main():
          13 +    # The nominal arm extends along world +x; test y alignment plus small x/joint offsets.
          14 +    candidates = []
          15 +    for dx in (0.0, -0.05, -0.1, -0.2):
          16 +        for j2 in (0.0, -0.1, 0.1, -0.2, 0.2):
          17 +            for j4 in (0.0, -0.1, 0.1):
          18 +                candidates.append((dx, j2, j4))
   29     19      env = make_env()
   30        -    state, info = env.reset(seed=0)
   31        -    print("max_steps", env.max_steps, "info", info)
   32        -    print(snapshot(state))
   33        -    for label, action in [
   34        -        ("close", [0] * 10 + [-1]),
   35        -        ("open", [0] * 10 + [1]),
   36        -        ("all_joint_plus", [0, 0, 0] + [0.2] * 7 + [0]),
   37        -        ("all_joint_minus", [0, 0, 0] + [-0.2] * 7 + [0]),
   38        -        ("base_plus", [0.2, 0.2, 0.2] + [0] * 8),
   39        -    ]:
   40        -        state, reward, term, trunc, info = env.step(np.asarray(action, dtype=np.float32))
   41        -        print(label, reward, term, trunc, info, snapshot(state))
   42        -    env.close()
   43        -
   44        -
   45        -def random_search(seed=0, steps=1000):
   46        -    """Look for any attachment while broadly random-walking configuration."""
   47        -    rng = np.random.default_rng(seed + 991)
   48        -    env = make_env()
   49        -    state, _ = env.reset(seed=seed)
   50        -    initial = snapshot(state)
   51        -    print("seed", seed, "objects", initial)
   52        -    last_positions = {k: (v.get("pose_x"), v.get("pose_y"), v.get("pose_z"))
   53        -                      for k, v in initial.items() if "pose_x" in v}
   54        -    for t in range(steps):
   55        -        action = np.zeros(11, dtype=np.float32)
   56        -        # Persistent random motion explores configurations better than white noise.
   57        -        action[:10] = rng.choice([-0.2, 0.0, 0.2], size=10, p=[0.3, 0.4, 0.3])
   58        -        action[10] = -1.0
   59        -        state, reward, term, trunc, info = env.step(action)
   60        -        snap = snapshot(state)
   61        -        moved = []
   62        -        for k, old in last_positions.items():
   63        -            new = tuple(snap[k].get(x) for x in ("pose_x", "pose_y", "pose_z"))
   64        -            if max(abs(a - b) for a, b in zip(old, new)) > 1e-5:
   65        -                moved.append((k, old, new))
   66        -            last_positions[k] = new
   67        -        if moved or snap["robot"]["grasp_active"]:
   68        -            print("EVENT", t, "a", action.tolist(), "moved", moved,
   69        -                  "robot", snap["robot"])
   70        -        if snap["robot"]["grasp_active"] or term or trunc:
   71        -            print("END", t, reward, term, trunc, snap)
          20 +    for dx, j2, j4 in candidates:
          21 +        state, _ = env.reset(seed=0)
          22 +        target_y = value(state, "target_block", "pose_y")
          23 +        move = np.zeros(11, dtype=np.float32)
          24 +        move[0], move[1], move[4], move[6] = dx, target_y, j2, j4
          25 +        state, _, _, _, _ = env.step(move)
          26 +        close = np.zeros(11, dtype=np.float32)
          27 +        close[10] = -1.0
          28 +        state, _, _, _, _ = env.step(close)
          29 +        active = value(state, "robot", "grasp_active")
          30 +        if active:
          31 +            robot = state.get_object_from_name("robot")
          32 +            tf = [state.get(robot, "grasp_tf_" + c) for c in "xyz"]
          33 +            quat = [state.get(robot, "grasp_tf_q" + c) for c in "xyzw"]
          34 +            held = [n for n in state.get_object_names()
          35 +                    if n != "robot" and value(state, n, "grasp_active")]
          36 +            print("SUCCESS", dx, j2, j4, "held", held, "tf", tf, quat,
          37 +                  "finger", state.get(robot, "finger_state"))
   72     38              break
          39 +    else:
          40 +        print("no grasp in", len(candidates), "candidates")
   73     41      env.close()
   74     42  
   75     43  
   76     44  if __name__ == "__main__":
   77        -    import argparse
   78        -    parser = argparse.ArgumentParser()
   79        -    parser.add_argument("--random", action="store_true")
   80        -    parser.add_argument("--seed", type=int, default=0)
   81        -    args = parser.parse_args()
   82        -    random_search(args.seed) if args.random else main()
          45 +    main()
```

</details>

<a id="C008"></a>
### C008 · Restore concurrent grasp probe after shared-file race

Commit `f54406c63cd7de034766d1032e649394cb7c5088`; parents: 0aa23e659ca50d86cd08a97e61fd13e4a5acd99e. Recorded author date: 2026-09-09T15:25:08+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C008_f54406c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index d7156c5..4ce49dd 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -1,45 +1,82 @@
    1        -"""Try simple base-alignment grasps and report attachment-transform semantics."""
           1 +"""Focused black-box probes for Obstruction3D grasp mechanics."""
    2      2  
    3      3  import numpy as np
    4      4  
    5      5  from env_client import make_env
    6      6  
    7      7  
    8        -def value(state, name, feature):
    9        -    return state.get(state.get_object_from_name(name), feature)
           8 +def read(state, obj, names):
           9 +    return {name: float(state.get(obj, name)) for name in names}
          10 +
          11 +
          12 +def snapshot(state):
          13 +    out = {}
          14 +    for name in state.get_object_names():
          15 +        obj = state.get_object_from_name(name)
          16 +        try:
          17 +            out[name] = read(state, obj, ["pose_x", "pose_y", "pose_z", "grasp_active"])
          18 +        except Exception:
          19 +            out[name] = read(state, obj, [
          20 +                "pos_base_x", "pos_base_y", "pos_base_rot",
          21 +                "joint_1", "joint_2", "joint_3", "joint_4", "joint_5",
          22 +                "joint_6", "joint_7", "finger_state", "grasp_active",
          23 +                "grasp_tf_x", "grasp_tf_y", "grasp_tf_z",
          24 +            ])
          25 +    return out
   10     26  
   11     27  
   12     28  def main():
   13        -    # The nominal arm extends along world +x; test y alignment plus small x/joint offsets.
   14        -    candidates = []
   15        -    for dx in (0.0, -0.05, -0.1, -0.2):
   16        -        for j2 in (0.0, -0.1, 0.1, -0.2, 0.2):
   17        -            for j4 in (0.0, -0.1, 0.1):
   18        -                candidates.append((dx, j2, j4))
   19     29      env = make_env()
   20        -    for dx, j2, j4 in candidates:
   21        -        state, _ = env.reset(seed=0)
   22        -        target_y = value(state, "target_block", "pose_y")
   23        -        move = np.zeros(11, dtype=np.float32)
   24        -        move[0], move[1], move[4], move[6] = dx, target_y, j2, j4
   25        -        state, _, _, _, _ = env.step(move)
   26        -        close = np.zeros(11, dtype=np.float32)
   27        -        close[10] = -1.0
   28        -        state, _, _, _, _ = env.step(close)
   29        -        active = value(state, "robot", "grasp_active")
   30        -        if active:
   31        -            robot = state.get_object_from_name("robot")
   32        -            tf = [state.get(robot, "grasp_tf_" + c) for c in "xyz"]
   33        -            quat = [state.get(robot, "grasp_tf_q" + c) for c in "xyzw"]
   34        -            held = [n for n in state.get_object_names()
   35        -                    if n != "robot" and value(state, n, "grasp_active")]
   36        -            print("SUCCESS", dx, j2, j4, "held", held, "tf", tf, quat,
   37        -                  "finger", state.get(robot, "finger_state"))
          30 +    state, info = env.reset(seed=0)
          31 +    print("max_steps", env.max_steps, "info", info)
          32 +    print(snapshot(state))
          33 +    for label, action in [
          34 +        ("close", [0] * 10 + [-1]),
          35 +        ("open", [0] * 10 + [1]),
          36 +        ("all_joint_plus", [0, 0, 0] + [0.2] * 7 + [0]),
          37 +        ("all_joint_minus", [0, 0, 0] + [-0.2] * 7 + [0]),
          38 +        ("base_plus", [0.2, 0.2, 0.2] + [0] * 8),
          39 +    ]:
          40 +        state, reward, term, trunc, info = env.step(np.asarray(action, dtype=np.float32))
          41 +        print(label, reward, term, trunc, info, snapshot(state))
          42 +    env.close()
          43 +
          44 +
          45 +def random_search(seed=0, steps=1000):
          46 +    """Look for any attachment while broadly random-walking configuration."""
          47 +    rng = np.random.default_rng(seed + 991)
          48 +    env = make_env()
          49 +    state, _ = env.reset(seed=seed)
          50 +    initial = snapshot(state)
          51 +    print("seed", seed, "objects", initial)
          52 +    last_positions = {k: (v.get("pose_x"), v.get("pose_y"), v.get("pose_z"))
          53 +                      for k, v in initial.items() if "pose_x" in v}
          54 +    for t in range(steps):
          55 +        action = np.zeros(11, dtype=np.float32)
          56 +        # Persistent random motion explores configurations better than white noise.
          57 +        action[:10] = rng.choice([-0.2, 0.0, 0.2], size=10, p=[0.3, 0.4, 0.3])
          58 +        action[10] = -1.0
          59 +        state, reward, term, trunc, info = env.step(action)
          60 +        snap = snapshot(state)
          61 +        moved = []
          62 +        for k, old in last_positions.items():
          63 +            new = tuple(snap[k].get(x) for x in ("pose_x", "pose_y", "pose_z"))
          64 +            if max(abs(a - b) for a, b in zip(old, new)) > 1e-5:
          65 +                moved.append((k, old, new))
          66 +            last_positions[k] = new
          67 +        if moved or snap["robot"]["grasp_active"]:
          68 +            print("EVENT", t, "a", action.tolist(), "moved", moved,
          69 +                  "robot", snap["robot"])
          70 +        if snap["robot"]["grasp_active"] or term or trunc:
          71 +            print("END", t, reward, term, trunc, snap)
   38     72              break
   39        -    else:
   40        -        print("no grasp in", len(candidates), "candidates")
   41     73      env.close()
   42     74  
   43     75  
   44     76  if __name__ == "__main__":
   45        -    main()
          77 +    import argparse
          78 +    parser = argparse.ArgumentParser()
          79 +    parser.add_argument("--random", action="store_true")
          80 +    parser.add_argument("--seed", type=int, default=0)
          81 +    args = parser.parse_args()
          82 +    random_search(args.seed) if args.random else main()
```

</details>

<a id="C009"></a>
### C009 · Probe pitch-joint grid for target grasp

Commit `4aef2ddb4a673f7a424142a52d1aaaf197f776e8`; parents: f54406c63cd7de034766d1032e649394cb7c5088. Recorded author date: 2026-09-09T15:26:26+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C009_4aef2dd.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index 4ce49dd..0b868ce 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -73,10 +73,50 @@ def random_search(seed=0, steps=1000):
   73     73      env.close()
   74     74  
   75     75  
          76 +def joint_grid(seed=0):
          77 +    """Sweep the main pitch joints with the base y-aligned to the target."""
          78 +    env = make_env()
          79 +    state, _ = env.reset(seed=seed)
          80 +    snap = snapshot(state)
          81 +    target_y = snap["target_block"]["pose_y"]
          82 +    action = np.zeros(11, dtype=np.float32)
          83 +    action[1] = np.clip(target_y - snap["robot"]["pos_base_y"], -0.2, 0.2)
          84 +    state, *_ = env.step(action)
          85 +    base_j2 = snapshot(state)["robot"]["joint_2"]
          86 +    base_j4 = snapshot(state)["robot"]["joint_4"]
          87 +    old_xyz = tuple(snapshot(state)["target_block"]["pose_" + c] for c in "xyz")
          88 +    j2s = [base_j2 + 0.2 * k for k in range(-6, 7)]
          89 +    j4s = [base_j4 + 0.2 * k for k in range(-6, 7)]
          90 +    for row, wanted_j2 in enumerate(j2s):
          91 +        for wanted_j4 in (j4s if row % 2 == 0 else list(reversed(j4s))):
          92 +            now = snapshot(state)["robot"]
          93 +            action = np.zeros(11, dtype=np.float32)
          94 +            action[4] = np.clip(wanted_j2 - now["joint_2"], -0.2, 0.2)
          95 +            action[6] = np.clip(wanted_j4 - now["joint_4"], -0.2, 0.2)
          96 +            action[10] = 1.0
          97 +            state, *_ = env.step(action)
          98 +            close = np.zeros(11, dtype=np.float32)
          99 +            close[10] = -1.0
         100 +            state, reward, term, trunc, _ = env.step(close)
         101 +            ss = snapshot(state)
         102 +            xyz = tuple(ss["target_block"]["pose_" + c] for c in "xyz")
         103 +            moved = max(abs(a - b) for a, b in zip(xyz, old_xyz))
         104 +            if moved > 1e-6 or ss["robot"]["grasp_active"]:
         105 +                print("EVENT", wanted_j2, wanted_j4, "xyz", xyz, "moved", moved,
         106 +                      "robot", ss["robot"], "done", term, trunc)
         107 +            old_xyz = xyz
         108 +            if ss["robot"]["grasp_active"] or term or trunc:
         109 +                env.close()
         110 +                return
         111 +    print("grid found no grasp")
         112 +    env.close()
         113 +
         114 +
   76    115  if __name__ == "__main__":
   77    116      import argparse
   78    117      parser = argparse.ArgumentParser()
   79    118      parser.add_argument("--random", action="store_true")
         119 +    parser.add_argument("--grid", action="store_true")
   80    120      parser.add_argument("--seed", type=int, default=0)
   81    121      args = parser.parse_args()
   82        -    random_search(args.seed) if args.random else main()
         122 +    joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main())
```

</details>

<a id="C010"></a>
### C010 · Add first Kinova geometry-driven pick-place controller

Commit `77f8416630f39a82874b45dbeb3605763f5e64d7`; parents: 4aef2ddb4a673f7a424142a52d1aaaf197f776e8. Recorded author date: 2026-09-09T15:26:56+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0054](01_timeline.md#E0054): commit hash in recorded output.
[Controller after this commit](evidence/versions/C010_77f8416_approach.py) · [Exact all-file diff](evidence/diffs/C010_77f8416.diff)

[Previous saved controller snapshot](evidence/versions/C002_25581ec_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1faa0cb..a3110a6 100644
--- a/approach.py
+++ b/approach.py
@@ -1,16 +1,84 @@
    1        -"""Policy for the Obstruction3D black-box manipulation task."""
           1 +"""Geometry-driven policy for the Obstruction3D manipulation task."""
    2      2  
    3      3  import numpy as np
           4 +from scipy.optimize import least_squares
           5 +from scipy.spatial.transform import Rotation
           6 +
           7 +_ORIGINS = (
           8 +    ((0, 0, .15643), (np.pi, 0, 0)),
           9 +    ((0, .005375, -.12838), (np.pi / 2, 0, 0)),
          10 +    ((0, -.21038, -.006375), (-np.pi / 2, 0, 0)),
          11 +    ((0, .006375, -.21038), (np.pi / 2, 0, 0)),
          12 +    ((0, -.20843, -.006375), (-np.pi / 2, 0, 0)),
          13 +    ((0, .00017505, -.10593), (np.pi / 2, 0, 0)),
          14 +    ((0, -.10593, -.00017505), (-np.pi / 2, 0, 0)),
          15 +)
          16 +_HOME = np.array((0, -.35, -np.pi, -2.5, 0, -.87, np.pi / 2))
          17 +
          18 +
          19 +def _fk(q):
          20 +    t = np.eye(4)
          21 +    for angle, (xyz, rpy) in zip(q, _ORIGINS):
          22 +        a = np.eye(4)
          23 +        a[:3, :3] = Rotation.from_euler("xyz", rpy).as_matrix()
          24 +        a[:3, 3] = xyz
          25 +        z = np.eye(4)
          26 +        z[:3, :3] = Rotation.from_euler("z", angle).as_matrix()
          27 +        t = t @ a @ z
          28 +    a = np.eye(4)
          29 +    a[:3, :3] = Rotation.from_euler("x", np.pi).as_matrix()
          30 +    a[:3, 3] = (0, 0, -.061525)
          31 +    return t @ a
    4     32  
    5     33  
    6     34  class GeneratedApproach:
    7     35      def __init__(self, action_space, observation_space, primitives):
    8     36          self.action_space = action_space
    9        -        self.observation_space = observation_space
          37 +
          38 +    @staticmethod
          39 +    def _get(state, name, feature):
          40 +        return float(state.get(state.get_object_from_name(name), feature))
          41 +
          42 +    def _solve(self, xyz, seed=None):
          43 +        start = _HOME if seed is None else seed
          44 +        base = np.array((self.base_x, self.base_y, 0.0))
          45 +        def residual(q):
          46 +            t = _fk(q)
          47 +            grasp = base + t[:3, 3] + .12 * t[:3, 2]
          48 +            return np.r_[8 * (grasp - xyz), 1.5 * t[:2, 2], .03 * (q - _HOME)]
          49 +        return least_squares(residual, start, max_nfev=180).x
   10     50  
   11     51      def reset(self, state, info):
   12        -        pass
          52 +        self.step = 0
          53 +        self.base_x = self._get(state, "robot", "pos_base_x")
          54 +        self.base_y = self._get(state, "robot", "pos_base_y")
          55 +        block = np.array([self._get(state, "target_block", f"pose_{c}") for c in "xyz"])
          56 +        region = np.array([self._get(state, "target_region", f"pose_{c}") for c in "xyz"])
          57 +        self.pick_q = self._solve(block)
          58 +        self.lift_q = self._solve(block + (0, 0, .18), self.pick_q)
          59 +        self.place_q = self._solve(region + (0, 0, .08), self.lift_q)
          60 +        self.drop_q = self._solve(region + (0, 0, .03), self.place_q)
   13     61  
   14     62      def get_action(self, state):
   15        -        # Safe baseline; replaced as dynamics are identified.
   16        -        return np.zeros(self.action_space.shape, dtype=np.float32)
          63 +        self.step += 1
          64 +        robot = state.get_object_from_name("robot")
          65 +        q = np.array([float(state.get(robot, f"joint_{i}")) for i in range(1, 8)])
          66 +        grasped = float(state.get(robot, "grasp_active")) > .5
          67 +        if self.step <= 18:
          68 +            goal, grip = self.pick_q, 1.0
          69 +        elif self.step <= 21:
          70 +            goal, grip = self.pick_q, -1.0
          71 +        elif self.step <= 35:
          72 +            goal, grip = self.lift_q, 0.0
          73 +        elif self.step <= 51:
          74 +            goal, grip = self.place_q, 0.0
          75 +        elif self.step <= 60:
          76 +            goal, grip = self.drop_q, 0.0
          77 +        else:
          78 +            goal, grip = self.drop_q, 1.0
          79 +        if 22 <= self.step <= 35 and not grasped:
          80 +            goal, grip = self.pick_q, -1.0
          81 +        action = np.zeros(self.action_space.shape, dtype=np.float32)
          82 +        action[3:10] = np.clip(goal - q, -.2, .2)
          83 +        action[10] = grip
          84 +        return action
diff --git a/ik_probe.py b/ik_probe.py
new file mode 100644
index 0000000..7019d65
--- /dev/null
+++ b/ik_probe.py
@@ -0,0 +1,33 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +from scipy.optimize import least_squares
           4 +from scipy.spatial.transform import Rotation
           5 +
           6 +ORIGINS=[([0,0,.15643],[np.pi,0,0]),([0,.005375,-.12838],[np.pi/2,0,0]),([0,-.21038,-.006375],[-np.pi/2,0,0]),([0,.006375,-.21038],[np.pi/2,0,0]),([0,-.20843,-.006375],[-np.pi/2,0,0]),([0,.00017505,-.10593],[np.pi/2,0,0]),([0,-.10593,-.00017505],[-np.pi/2,0,0])]
           7 +Q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
           8 +def fk(q):
           9 + T=np.eye(4)
          10 + for qi,(xyz,rpy) in zip(q,ORIGINS):
          11 +  A=np.eye(4);A[:3,:3]=Rotation.from_euler('xyz',rpy).as_matrix();A[:3,3]=xyz
          12 +  Z=np.eye(4);Z[:3,:3]=Rotation.from_euler('z',qi).as_matrix();T=T@A@Z
          13 + A=np.eye(4);A[:3,:3]=Rotation.from_euler('x',np.pi).as_matrix();A[:3,3]=[0,0,-.061525]
          14 + return T@A
          15 +def ik(xyz,off):
          16 + def fun(q):
          17 +  T=fk(q); grasp=T[:3,3]+off*T[:3,2]
          18 +  return np.r_[5*(grasp-xyz), T[:2,2], .15*(q-Q0)]
          19 + return least_squares(fun,Q0,max_nfev=300).x
          20 +def val(s,n,f): return float(s.get(s.get_object_from_name(n),f))
          21 +
          22 +for off in [.04,.08,.12,.16]:
          23 + e=make_env();s,_=e.reset(seed=0);xyz=np.array([val(s,'target_block',f) for f in ['pose_x','pose_y','pose_z']])
          24 + q=ik(xyz-np.array([-.12,0,0]),off) # base frame target
          25 + print('OFF',off,'q',q,'fk',fk(q)[:3,3], 'gp',fk(q)[:3,3]+off*fk(q)[:3,2])
          26 + for k in range(40):
          27 +  rob=s.get_object_from_name('robot'); cur=np.array([float(s.get(rob,'joint_'+str(i))) for i in range(1,8)])
          28 +  a=np.zeros(11,np.float32);a[3:10]=np.clip(q-cur,-.2,.2);a[10]=1
          29 +  s,r,t,tr,info=e.step(a)
          30 +  if np.max(np.abs(q-cur))<.01:break
          31 + a=np.zeros(11,np.float32);a[10]=-1;s,r,t,tr,info=e.step(a)
          32 + print(' grasp',val(s,'robot','grasp_active'),val(s,'target_block','grasp_active'),'obj',[val(s,'target_block',f) for f in ['pose_x','pose_y','pose_z']], 'tf',[val(s,'robot',f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']])
          33 + e.close()
diff --git a/inspect_env.py b/inspect_env.py
new file mode 100644
index 0000000..ddcb3b8
--- /dev/null
+++ b/inspect_env.py
@@ -0,0 +1,26 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def vals(s, o):
           5 +    feats = ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z',
           6 +             'object_type','grasp_active','pos_base_x','pos_base_y','pos_base_rot',
           7 +             'joint_1','joint_2','joint_3','joint_4','joint_5','joint_6','joint_7',
           8 +             'finger_state','grasp_tf_x','grasp_tf_y','grasp_tf_z']
           9 +    out={}
          10 +    for f in feats:
          11 +        try: out[f]=float(s.get(o,f))
          12 +        except Exception: pass
          13 +    return out
          14 +
          15 +e=make_env(); s,info=e.reset(seed=0)
          16 +print('info', info, 'max', e.max_steps, 'names', s.get_object_names())
          17 +for n in s.get_object_names(): print(n, vals(s,s.get_object_from_name(n)))
          18 +for ix in range(11):
          19 +    e2=make_env(); q,_=e2.reset(seed=0); a=np.zeros(11,np.float32); a[ix]=e2.action_space.high[ix]
          20 +    q,r,t,tr,inf=e2.step(a)
          21 +    rob=q.get_object_from_name('robot')
          22 +    print('ACT',ix,'rtt',r,t,tr,'robot',vals(q,rob))
          23 +    for n in q.get_object_names():
          24 +        if n!='robot': print(' ',n,vals(q,q.get_object_from_name(n)))
          25 +    e2.close()
          26 +e.close()
diff --git a/probe_instances.py b/probe_instances.py
new file mode 100644
index 0000000..2fc05ef
--- /dev/null
+++ b/probe_instances.py
@@ -0,0 +1,150 @@
           1 +"""Exploration-only probes for Obstruction3DEnv."""
           2 +import argparse
           3 +import json
           4 +import numpy as np
           5 +
           6 +from env_client import make_env
           7 +
           8 +
           9 +def snapshot(state):
          10 +    rows = {}
          11 +    for name in state.get_object_names():
          12 +        obj = state.get_object_from_name(name)
          13 +        vals = {}
          14 +        for feat in (
          15 +            "pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw",
          16 +            "half_extent_x", "half_extent_y", "half_extent_z", "grasp_active", "object_type",
          17 +            "pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3",
          18 +            "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_tf_x",
          19 +            "grasp_tf_y", "grasp_tf_z",
          20 +        ):
          21 +            try:
          22 +                vals[feat] = float(state.get(obj, feat))
          23 +            except Exception:
          24 +                pass
          25 +        rows[name] = vals
          26 +    return rows
          27 +
          28 +
          29 +def resets(n):
          30 +    env = make_env()
          31 +    records = []
          32 +    try:
          33 +        for seed in range(n):
          34 +            s, info = env.reset(seed=seed)
          35 +            rows = snapshot(s)
          36 +            rec = {"seed": seed, "names": list(rows), "info": info}
          37 +            for name, vals in rows.items():
          38 +                rec[name] = vals
          39 +            records.append(rec)
          40 +    finally:
          41 +        env.close()
          42 +    print(json.dumps(records, separators=(",", ":")))
          43 +
          44 +
          45 +def effects(seed, index, value, steps):
          46 +    env = make_env()
          47 +    try:
          48 +        s, info = env.reset(seed=seed)
          49 +        print("initial", json.dumps(snapshot(s), separators=(",", ":")))
          50 +        action = np.zeros(env.action_space.shape, dtype=np.float32)
          51 +        action[index] = value
          52 +        for t in range(steps):
          53 +            s, reward, term, trunc, info = env.step(action)
          54 +            print(t + 1, reward, term, trunc, json.dumps(snapshot(s), separators=(",", ":")))
          55 +            if term or trunc:
          56 +                break
          57 +    finally:
          58 +        env.close()
          59 +
          60 +
          61 +def effect_all(seed):
          62 +    for idx in range(11):
          63 +        env = make_env()
          64 +        try:
          65 +            s0, _ = env.reset(seed=seed)
          66 +            b = snapshot(s0)
          67 +            action = np.zeros(11, dtype=np.float32)
          68 +            action[idx] = 1.0 if idx == 10 else 0.2
          69 +            s1, reward, term, trunc, info = env.step(action)
          70 +            a = snapshot(s1)
          71 +            changed = {}
          72 +            for name in a:
          73 +                d = {k: round(v - b[name].get(k, v), 6) for k, v in a[name].items()
          74 +                     if isinstance(v, float) and abs(v - b[name].get(k, v)) > 1e-6}
          75 +                if d:
          76 +                    changed[name] = d
          77 +            print(idx, changed)
          78 +        finally:
          79 +            env.close()
          80 +
          81 +
          82 +def target_scan(seed, limit):
          83 +    """Coordinate sweeps around the tabletop-ready home posture."""
          84 +    env = make_env()
          85 +    try:
          86 +        s, _ = env.reset(seed=seed)
          87 +        target = snapshot(s)["target_block"]
          88 +        # Align the mobile base laterally with the target first.
          89 +        a = np.zeros(11, dtype=np.float32)
          90 +        a[1] = np.clip(target["pose_y"], -0.2, 0.2)
          91 +        a[10] = 1.0
          92 +        s, *_ = env.step(a)
          93 +        names = [n for n in s.get_object_names() if n != "robot"]
          94 +        home = np.array([0., -.35, -np.pi, -2.5, 0., -.87, np.pi / 2])
          95 +        # Most vertical tabletop motion is generated by shoulder/elbow/wrist pitch.
          96 +        candidates = []
          97 +        for bx in (-.12, -.22, -.32, -.42):
          98 +            for q2 in (-1.15, -.95, -.75, -.55, -.35, -.15, .05, .25):
          99 +                for q4 in (-3.1, -2.9, -2.7, -2.5, -2.3, -2.1, -1.9):
         100 +                    for q6 in (-1.47, -1.27, -1.07, -.87, -.67, -.47, -.27):
         101 +                        q = home.copy(); q[1] = q2; q[3] = q4; q[5] = q6
         102 +                        candidates.append((bx, q))
         103 +        # Nearby configurations first.
         104 +        candidates.sort(key=lambda z: abs(z[0] + .12) + np.sum(abs(z[1] - home)))
         105 +        t = 1
         106 +        for ci, (bx, q) in enumerate(candidates):
         107 +            robot = snapshot(s)["robot"]
         108 +            cur = np.array([robot[f"joint_{i}"] for i in range(1, 8)])
         109 +            # Move toward candidate, gripper open. Each delta is already legal.
         110 +            while max(abs(q - cur).max(), abs(bx - robot["pos_base_x"])) > .02:
         111 +                a = np.zeros(11, dtype=np.float32)
         112 +                a[0] = np.clip(bx - robot["pos_base_x"], -.2, .2)
         113 +                a[3:10] = np.clip(q - cur, -.2, .2)
         114 +                a[10] = 1.
         115 +                s, _, term, trunc, _ = env.step(a); t += 1
         116 +                robot = snapshot(s)["robot"]
         117 +                cur = np.array([robot[f"joint_{i}"] for i in range(1, 8)])
         118 +                if t >= limit or term or trunc: return print("LIMIT", t)
         119 +            a = np.zeros(11, dtype=np.float32); a[10] = -1.
         120 +            s, _, term, trunc, _ = env.step(a); t += 1
         121 +            snap = snapshot(s)
         122 +            moved = [n for n in names if snap[n]["grasp_active"] > .5]
         123 +            if snap["robot"]["grasp_active"] > .5 or moved:
         124 +                print("GRASP", "t", t, "candidate", ci, "bx", bx, "q", q.tolist(),
         125 +                      "held", moved, "robot", snap["robot"], "objects", {n:snap[n] for n in moved})
         126 +                return
         127 +            if t >= limit or term or trunc: return print("LIMIT", t)
         128 +        print("NO_GRASP", t)
         129 +    finally:
         130 +        env.close()
         131 +
         132 +
         133 +if __name__ == "__main__":
         134 +    p = argparse.ArgumentParser()
         135 +    p.add_argument("mode", choices=("resets", "effects", "effect_all", "target_scan"))
         136 +    p.add_argument("--n", type=int, default=20)
         137 +    p.add_argument("--seed", type=int, default=0)
         138 +    p.add_argument("--index", type=int, default=0)
         139 +    p.add_argument("--value", type=float, default=0.2)
         140 +    p.add_argument("--steps", type=int, default=1)
         141 +    p.add_argument("--limit", type=int, default=280)
         142 +    a = p.parse_args()
         143 +    if a.mode == "resets":
         144 +        resets(a.n)
         145 +    elif a.mode == "effects":
         146 +        effects(a.seed, a.index, a.value, a.steps)
         147 +    elif a.mode == "effect_all":
         148 +        effect_all(a.seed)
         149 +    else:
         150 +        target_scan(a.seed, a.limit)
diff --git a/quick_probe.py b/quick_probe.py
new file mode 100644
index 0000000..8651278
--- /dev/null
+++ b/quick_probe.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def get(s,n,f): return float(s.get(s.get_object_from_name(n),f))
           5 +def snap(s):
           6 +    names=sorted(s.get_object_names())
           7 +    rob=[get(s,'robot',f) for f in ['pos_base_x','pos_base_y','pos_base_rot','joint_1','joint_2','joint_3','joint_4','joint_5','joint_6','joint_7','finger_state','grasp_active','grasp_tf_x','grasp_tf_y','grasp_tf_z']]
           8 +    objs={n:[get(s,n,f) for f in ['pose_x','pose_y','pose_z','grasp_active']] for n in names if n!='robot'}
           9 +    return rob,objs
          10 +
          11 +e=make_env(); s,_=e.reset(seed=0); print('start',snap(s))
          12 +seq=[]
          13 +a=np.zeros(11,np.float32); a[10]=-1; seq.append(a)
          14 +for idx in range(10):
          15 +    a=np.zeros(11,np.float32); a[idx]=.2; seq.append(a)
          16 +for k,a in enumerate(seq):
          17 +    s,r,t,tr,i=e.step(a); print(k, snap(s), r,t,tr)
          18 +e.close()
diff --git a/scan_grasp.py b/scan_grasp.py
new file mode 100644
index 0000000..ef8ac0c
--- /dev/null
+++ b/scan_grasp.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def v(s,n,f): return float(s.get(s.get_object_from_name(n),f))
           5 +e=make_env();s,_=e.reset(seed=0)
           6 +tx=v(s,'target_block','pose_x');ty=v(s,'target_block','pose_y')
           7 +print('target',tx,ty,v(s,'target_block','pose_z'))
           8 +for bx in [-.12,-.22,-.32,-.42,-.52,-.62]:
           9 + for yo in [0,-.04,.04]:
          10 +  # absolute positioning by observed robot state
          11 +  for grip in [1,-1]:
          12 +   r=s.get_object_from_name('robot');cx=float(s.get(r,'pos_base_x'));cy=float(s.get(r,'pos_base_y'))
          13 +   a=np.zeros(11,np.float32);a[0]=np.clip(bx-cx,-.2,.2);a[1]=np.clip(ty+yo-cy,-.2,.2);a[10]=grip
          14 +   s,re,te,tr,info=e.step(a)
          15 +  print(bx,yo,'robot',v(s,'robot','pos_base_x'),v(s,'robot','pos_base_y'),'grasp',v(s,'robot','grasp_active'),v(s,'target_block','grasp_active'),[v(s,'robot',f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']])
          16 +  if v(s,'robot','grasp_active')>0: raise SystemExit
          17 +e.close()
```

</details>

<a id="C011"></a>
### C011 · Probe Kinova arm mount offset for grasping

Commit `8a5f258a055292fa672b5f732d15640c25cf7aaa`; parents: 77f8416630f39a82874b45dbeb3605763f5e64d7. Recorded author date: 2026-09-09T15:27:14+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C011_8a5f258.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_mount_offset.py b/probe_mount_offset.py
new file mode 100644
index 0000000..897ffb5
--- /dev/null
+++ b/probe_mount_offset.py
@@ -0,0 +1,70 @@
           1 +"""Probe the suspected 0.12 m arm mount offset using Kinova FK/IK."""
           2 +
           3 +import numpy as np
           4 +from scipy.optimize import least_squares
           5 +from scipy.spatial.transform import Rotation
           6 +from env_client import make_env
           7 +
           8 +ORIGINS = [
           9 +    ([0, 0, .15643], [np.pi, 0, 0]), ([0, .005375, -.12838], [np.pi / 2, 0, 0]),
          10 +    ([0, -.21038, -.006375], [-np.pi / 2, 0, 0]), ([0, .006375, -.21038], [np.pi / 2, 0, 0]),
          11 +    ([0, -.20843, -.006375], [-np.pi / 2, 0, 0]), ([0, .00017505, -.10593], [np.pi / 2, 0, 0]),
          12 +    ([0, -.10593, -.00017505], [-np.pi / 2, 0, 0]),
          13 +]
          14 +Q0 = np.array([0, -.35, -np.pi, -2.5, 0, -.87, np.pi / 2])
          15 +
          16 +
          17 +def fk(q):
          18 +    transform = np.eye(4)
          19 +    for qi, (xyz, rpy) in zip(q, ORIGINS):
          20 +        fixed = np.eye(4)
          21 +        fixed[:3, :3] = Rotation.from_euler("xyz", rpy).as_matrix()
          22 +        fixed[:3, 3] = xyz
          23 +        joint = np.eye(4)
          24 +        joint[:3, :3] = Rotation.from_euler("z", qi).as_matrix()
          25 +        transform = transform @ fixed @ joint
          26 +    tool = np.eye(4)
          27 +    tool[:3, :3] = Rotation.from_euler("x", np.pi).as_matrix()
          28 +    tool[:3, 3] = [0, 0, -.061525]
          29 +    return transform @ tool
          30 +
          31 +
          32 +def get(state, obj, feature):
          33 +    return float(state.get(state.get_object_from_name(obj), feature))
          34 +
          35 +
          36 +def main():
          37 +    env = make_env()
          38 +    for mount_x in (0.12, 0.10, 0.14):
          39 +        for height in (.10, .125, .15):
          40 +            for offset in (.04, .08, .12):
          41 +                state, _ = env.reset(seed=0)
          42 +                target = np.array([get(state, "target_block", "pose_" + axis) for axis in "xyz"])
          43 +                target[2] = height
          44 +                desired = target - np.array([-0.12 + mount_x, 0, 0])
          45 +                def residual(q):
          46 +                    pose = fk(q)
          47 +                    grasp = pose[:3, 3] + offset * pose[:3, 2]
          48 +                    return np.r_[8 * (grasp - desired), pose[:2, 2], .08 * (q - Q0)]
          49 +                q = least_squares(residual, Q0, max_nfev=250).x
          50 +                for _ in range(20):
          51 +                    robot = state.get_object_from_name("robot")
          52 +                    cur = np.array([state.get(robot, "joint_" + str(i)) for i in range(1, 8)])
          53 +                    action = np.zeros(11, np.float32)
          54 +                    action[3:10] = np.clip(q - cur, -.2, .2)
          55 +                    action[10] = 1
          56 +                    state, _, _, _, _ = env.step(action)
          57 +                    if np.max(np.abs(q - cur)) < .01:
          58 +                        break
          59 +                action = np.zeros(11, np.float32); action[10] = -1
          60 +                state, _, _, _, _ = env.step(action)
          61 +                if get(state, "robot", "grasp_active"):
          62 +                    print("SUCCESS", mount_x, height, offset, q,
          63 +                          [get(state, "robot", "grasp_tf_" + a) for a in "xyz"])
          64 +                    env.close(); return
          65 +                print("miss", mount_x, height, offset)
          66 +    env.close()
          67 +
          68 +
          69 +if __name__ == "__main__":
          70 +    main()
```

</details>

<a id="C012"></a>
### C012 · Expand grasp search across wrist pitch

Commit `e76da11496feb2d7071d341feaf572b8bbd7b025`; parents: 8a5f258a055292fa672b5f732d15640c25cf7aaa. Recorded author date: 2026-09-09T15:27:30+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C012_e76da11.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index 0b868ce..eafaf57 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -112,11 +112,60 @@ def joint_grid(seed=0):
  112    112      env.close()
  113    113  
  114    114  
         115 +def triple_grid(seed=0):
         116 +    """Sweep shoulder, elbow, and wrist pitch at target-aligned base y."""
         117 +    env = make_env()
         118 +    state, _ = env.reset(seed=seed)
         119 +    initial = snapshot(state)
         120 +    action = np.zeros(11, dtype=np.float32)
         121 +    action[1] = np.clip(initial["target_block"]["pose_y"], -0.2, 0.2)
         122 +    state, *_ = env.step(action)
         123 +    home = snapshot(state)["robot"]
         124 +    vals2 = [home["joint_2"] + 0.2 * k for k in range(-6, 7)]
         125 +    vals4 = [home["joint_4"] + 0.2 * k for k in range(-6, 7)]
         126 +    vals6 = [home["joint_6"] + 0.2 * k for k in range(-6, 7)]
         127 +    # First walk to the low corner (joint deltas are capped at 0.2).
         128 +    for _ in range(6):
         129 +        action = np.zeros(11, dtype=np.float32)
         130 +        action[[4, 6, 8]] = -0.2
         131 +        action[10] = -1.0
         132 +        state, *_ = env.step(action)
         133 +    for i, wanted2 in enumerate(vals2):
         134 +        order4 = vals4 if i % 2 == 0 else list(reversed(vals4))
         135 +        for j, wanted4 in enumerate(order4):
         136 +            order6 = vals6 if (i + j) % 2 == 0 else list(reversed(vals6))
         137 +            for wanted6 in order6:
         138 +                now = snapshot(state)["robot"]
         139 +                action = np.zeros(11, dtype=np.float32)
         140 +                action[4] = np.clip(wanted2 - now["joint_2"], -0.2, 0.2)
         141 +                action[6] = np.clip(wanted4 - now["joint_4"], -0.2, 0.2)
         142 +                action[8] = np.clip(wanted6 - now["joint_6"], -0.2, 0.2)
         143 +                action[10] = -1.0
         144 +                state, reward, term, trunc, _ = env.step(action)
         145 +                ss = snapshot(state)
         146 +                moved = []
         147 +                for name, old in initial.items():
         148 +                    if "pose_x" not in old:
         149 +                        continue
         150 +                    d = max(abs(ss[name]["pose_" + c] - old["pose_" + c]) for c in "xyz")
         151 +                    if d > 1e-5:
         152 +                        moved.append((name, d, tuple(ss[name]["pose_" + c] for c in "xyz")))
         153 +                if moved or ss["robot"]["grasp_active"]:
         154 +                    print("TRIPLE EVENT", wanted2, wanted4, wanted6,
         155 +                          "moved", moved, "robot", ss["robot"], "done", term, trunc)
         156 +                if ss["robot"]["grasp_active"] or term or trunc:
         157 +                    env.close()
         158 +                    return
         159 +    print("triple grid found no grasp")
         160 +    env.close()
         161 +
         162 +
  115    163  if __name__ == "__main__":
  116    164      import argparse
  117    165      parser = argparse.ArgumentParser()
  118    166      parser.add_argument("--random", action="store_true")
  119    167      parser.add_argument("--grid", action="store_true")
         168 +    parser.add_argument("--triple", action="store_true")
  120    169      parser.add_argument("--seed", type=int, default=0)
  121    170      args = parser.parse_args()
  122        -    joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main())
         171 +    triple_grid(args.seed) if args.triple else (joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main()))
```

</details>

<a id="C013"></a>
### C013 · Add live multi-seed policy test harness

Commit `0fb74a1907410f358b66b4ec4bb01515c2d8bbfe`; parents: e76da11496feb2d7071d341feaf572b8bbd7b025. Recorded author date: 2026-09-09T15:27:31+02:00.

File roles (automatic): diagnostic/test.

- [E0060](01_timeline.md#E0060): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C013_0fb74a1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_mount_offset.py b/probe_mount_offset.py
index 897ffb5..bb443ca 100644
--- a/probe_mount_offset.py
+++ b/probe_mount_offset.py
@@ -60,7 +60,11 @@ def main():
   60     60                  state, _, _, _, _ = env.step(action)
   61     61                  if get(state, "robot", "grasp_active"):
   62     62                      print("SUCCESS", mount_x, height, offset, q,
   63        -                          [get(state, "robot", "grasp_tf_" + a) for a in "xyz"])
          63 +                          "held", [name for name in state.get_object_names()
          64 +                                   if name != "robot" and get(state, name, "grasp_active")],
          65 +                          "tf", [get(state, "robot", "grasp_tf_" + a) for a in "xyz"],
          66 +                          [get(state, "robot", "grasp_tf_q" + a) for a in "xyzw"],
          67 +                          "finger", get(state, "robot", "finger_state"))
   64     68                      env.close(); return
   65     69                  print("miss", mount_x, height, offset)
   66     70      env.close()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..58e87b6
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +
           4 +def run(seed, count=None, limit=200):
           5 +    env = make_env()
           6 +    options = {} if count is None else {"object_count": count}
           7 +    state, info = env.reset(seed=seed, options=options)
           8 +    policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
           9 +    policy.reset(state, info)
          10 +    for step in range(limit):
          11 +        state, reward, terminated, truncated, info = env.step(policy.get_action(state))
          12 +        if terminated or truncated:
          13 +            env.close(); return terminated, step + 1
          14 +    env.close(); return False, limit
          15 +
          16 +if __name__ == "__main__":
          17 +    for seed in range(5):
          18 +        print(seed, run(seed))
```

</details>

<a id="C014"></a>
### C014 · Measure end-effector effects via attached target

Commit `e58258a782c18fd38632ea3c7c7301f0a30d0938`; parents: 0fb74a1907410f358b66b4ec4bb01515c2d8bbfe. Recorded author date: 2026-09-09T15:28:45+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C014_e58258a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_attached_effects.py b/probe_attached_effects.py
new file mode 100644
index 0000000..1598ac6
--- /dev/null
+++ b/probe_attached_effects.py
@@ -0,0 +1,48 @@
           1 +"""Use a held target as an observable proxy for end-effector motion."""
           2 +
           3 +import numpy as np
           4 +from env_client import make_env
           5 +
           6 +
           7 +Q_GRASP = np.array([
           8 +    -.40352596, .61178776, -3.23371948, -2.0778396,
           9 +    .1132004, -.45664564, 1.57079633,
          10 +])
          11 +
          12 +
          13 +def get(state, obj, feature):
          14 +    return float(state.get(state.get_object_from_name(obj), feature))
          15 +
          16 +
          17 +def object_pose(state):
          18 +    return np.array([get(state, "target_block", "pose_" + f)
          19 +                     for f in ("x", "y", "z", "qx", "qy", "qz", "qw")])
          20 +
          21 +
          22 +def main():
          23 +    env = make_env()
          24 +    state, _ = env.reset(seed=0)
          25 +    for _ in range(20):
          26 +        robot = state.get_object_from_name("robot")
          27 +        current = np.array([state.get(robot, "joint_" + str(i)) for i in range(1, 8)])
          28 +        action = np.zeros(11, np.float32)
          29 +        action[3:10] = np.clip(Q_GRASP - current, -.2, .2)
          30 +        action[10] = 1
          31 +        state, _, _, _, _ = env.step(action)
          32 +        if np.max(np.abs(Q_GRASP - current)) < .01:
          33 +            break
          34 +    action = np.zeros(11, np.float32); action[10] = -1
          35 +    state, _, _, _, _ = env.step(action)
          36 +    print("attached", get(state, "robot", "grasp_active"), object_pose(state))
          37 +    for index in range(10):
          38 +        before = object_pose(state)
          39 +        action = np.zeros(11, np.float32); action[index] = .05
          40 +        state, _, _, _, _ = env.step(action)
          41 +        print("action", index, "object_delta", object_pose(state) - before)
          42 +        action[index] = -.05
          43 +        state, _, _, _, _ = env.step(action)
          44 +    env.close()
          45 +
          46 +
          47 +if __name__ == "__main__":
          48 +    main()
```

</details>

<a id="C015"></a>
### C015 · Add instance geometry and targeted grasp probes

Commit `ce292be521470aa8c68c1bf114ea0ecdfb1dd141`; parents: e58258a782c18fd38632ea3c7c7301f0a30d0938. Recorded author date: 2026-09-09T15:30:48+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C015_ce292be.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_instances.py b/probe_instances.py
index 2fc05ef..69744c6 100644
--- a/probe_instances.py
+++ b/probe_instances.py
@@ -2,10 +2,36 @@
    2      2  import argparse
    3      3  import json
    4      4  import numpy as np
           5 +from scipy.optimize import least_squares
           6 +from scipy.spatial.transform import Rotation
    5      7  
    6      8  from env_client import make_env
    7      9  
    8     10  
          11 +ORIGINS = [([0, 0, .15643], [np.pi, 0, 0]), ([0, .005375, -.12838], [np.pi/2, 0, 0]),
          12 +           ([0, -.21038, -.006375], [-np.pi/2, 0, 0]), ([0, .006375, -.21038], [np.pi/2, 0, 0]),
          13 +           ([0, -.20843, -.006375], [-np.pi/2, 0, 0]), ([0, .00017505, -.10593], [np.pi/2, 0, 0]),
          14 +           ([0, -.10593, -.00017505], [-np.pi/2, 0, 0])]
          15 +QHOME = np.array([0, -.35, -np.pi, -2.5, 0, -.87, np.pi/2])
          16 +
          17 +
          18 +def fk(q):
          19 +    t = np.eye(4)
          20 +    for qi, (xyz, rpy) in zip(q, ORIGINS):
          21 +        a = np.eye(4); a[:3, :3] = Rotation.from_euler("xyz", rpy).as_matrix(); a[:3, 3] = xyz
          22 +        z = np.eye(4); z[:3, :3] = Rotation.from_euler("z", qi).as_matrix()
          23 +        t = t @ a @ z
          24 +    a = np.eye(4); a[:3, :3] = Rotation.from_euler("x", np.pi).as_matrix(); a[:3, 3] = [0, 0, -.061525]
          25 +    return t @ a
          26 +
          27 +
          28 +def ik(xyz, off=.12):
          29 +    def fun(q):
          30 +        t = fk(q); grasp = t[:3, 3] + off * t[:3, 2]
          31 +        return np.r_[5 * (grasp - xyz), t[:2, 2], .15 * (q - QHOME)]
          32 +    return least_squares(fun, QHOME, max_nfev=300).x
          33 +
          34 +
    9     35  def snapshot(state):
   10     36      rows = {}
   11     37      for name in state.get_object_names():
@@ -130,9 +156,56 @@ def target_scan(seed, limit):
  130    156          env.close()
  131    157  
  132    158  
         159 +def full_place(seed):
         160 +    env = make_env()
         161 +    try:
         162 +        s, info = env.reset(seed=seed)
         163 +        start = snapshot(s)
         164 +        if any(n.startswith("obstruction") for n in start):
         165 +            print("WARNING obstructions present")
         166 +        def drive(q, grip):
         167 +            nonlocal s
         168 +            for _ in range(30):
         169 +                rob = snapshot(s)["robot"]
         170 +                cur = np.array([rob[f"joint_{i}"] for i in range(1, 8)])
         171 +                a = np.zeros(11, np.float32); a[3:10] = np.clip(q-cur, -.2, .2); a[10] = grip
         172 +                s, r, term, trunc, inf = env.step(a)
         173 +                if abs(q-cur).max() < .01 or term or trunc:
         174 +                    return r, term, trunc
         175 +            return r, term, trunc
         176 +        target = start["target_block"]
         177 +        qpick = ik(np.array([target[f"pose_{k}"] for k in "xyz"]), off=.16)
         178 +        drive(qpick, 1.)
         179 +        a = np.zeros(11, np.float32); a[10] = -1.; s, r, term, trunc, _ = env.step(a)
         180 +        print("PICK", snapshot(s)["robot"], qpick.tolist())
         181 +        region = start["target_region"]
         182 +        # Lift vertically before translating so the held block clears the table.
         183 +        qlift = ik(np.array([target["pose_x"], target["pose_y"], .30]), off=.16)
         184 +        print("LIFT", drive(qlift, -1.), snapshot(s)["target_block"])
         185 +        if seed == 111:
         186 +            for gi in range(12):
         187 +                a = np.zeros(11, np.float32); a[10] = 1.
         188 +                s, r, term, trunc, _ = env.step(a)
         189 +                print("OPEN", gi, snapshot(s)["robot"]["finger_state"], snapshot(s)["robot"]["grasp_active"], snapshot(s)["target_block"]["grasp_active"])
         190 +            return
         191 +        qabove = ik(np.array([region["pose_x"], region["pose_y"], .30]), off=.16)
         192 +        print("ABOVE", drive(qabove, -1.), snapshot(s)["target_block"])
         193 +        xyz = np.array([region["pose_x"], region["pose_y"],
         194 +                        region["pose_z"] + region["half_extent_z"] + target["half_extent_z"]])
         195 +        qplace = ik(xyz, off=.16)
         196 +        print("MOVE", drive(qplace, -1.), "target", snapshot(s)["target_block"], "q", qplace.tolist())
         197 +        a = np.zeros(11, np.float32); a[10] = 1.
         198 +        for _ in range(8):
         199 +            s, r, term, trunc, _ = env.step(a)
         200 +            if term or not snapshot(s)["robot"]["grasp_active"]: break
         201 +        print("DROP", r, term, trunc, "target", snapshot(s)["target_block"], "robot", snapshot(s)["robot"])
         202 +    finally:
         203 +        env.close()
         204 +
         205 +
  133    206  if __name__ == "__main__":
  134    207      p = argparse.ArgumentParser()
  135        -    p.add_argument("mode", choices=("resets", "effects", "effect_all", "target_scan"))
         208 +    p.add_argument("mode", choices=("resets", "effects", "effect_all", "target_scan", "full_place"))
  136    209      p.add_argument("--n", type=int, default=20)
  137    210      p.add_argument("--seed", type=int, default=0)
  138    211      p.add_argument("--index", type=int, default=0)
@@ -146,5 +219,7 @@ if __name__ == "__main__":
  146    219          effects(a.seed, a.index, a.value, a.steps)
  147    220      elif a.mode == "effect_all":
  148    221          effect_all(a.seed)
  149        -    else:
         222 +    elif a.mode == "target_scan":
  150    223          target_scan(a.seed, a.limit)
         224 +    else:
         225 +        full_place(a.seed)
```

</details>

<a id="C016"></a>
### C016 · Reproduce grasp and test direct carried placement

Commit `520ecd3ddd9e8a2714abf8bee8ffcb8c43b90193`; parents: ce292be521470aa8c68c1bf114ea0ecdfb1dd141. Recorded author date: 2026-09-09T15:30:52+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C016_520ecd3.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index eafaf57..d36c5aa 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -160,12 +160,56 @@ def triple_grid(seed=0):
  160    160      env.close()
  161    161  
  162    162  
         163 +def exact_sequence(seed=0):
         164 +    """Reproduce the discovered grasp, translate it, and test release."""
         165 +    env = make_env()
         166 +    state, _ = env.reset(seed=seed)
         167 +    ss = snapshot(state)
         168 +    block0 = tuple(ss["target_block"]["pose_" + c] for c in "xyz")
         169 +    region = tuple(ss["target_region"]["pose_" + c] for c in "xyz")
         170 +    print("INITIAL block", block0, "region", region)
         171 +    # Exact relative sequence from home: y-align and open while moving to the
         172 +    # successful q2/q4/q6 configuration, respecting +/-0.2 action limits.
         173 +    actions = []
         174 +    for k in range(3):
         175 +        a = np.zeros(11, dtype=np.float32)
         176 +        if k == 0:
         177 +            a[1] = np.clip(block0[1] - ss["robot"]["pos_base_y"], -0.2, 0.2)
         178 +        a[4] = 0.2
         179 +        a[6] = 0.2 if k == 0 else 0.0
         180 +        a[8] = 0.2 if k < 2 else 0.0
         181 +        a[10] = 1.0
         182 +        actions.append(("pose_open", a))
         183 +    close = np.zeros(11, dtype=np.float32)
         184 +    close[10] = -1.0
         185 +    actions.append(("close", close))
         186 +    carry = np.zeros(11, dtype=np.float32)
         187 +    carry[0] = np.clip(region[0] - block0[0], -0.2, 0.2)
         188 +    carry[1] = np.clip(region[1] - block0[1], -0.2, 0.2)
         189 +    actions.append(("carry", carry))
         190 +    release = np.zeros(11, dtype=np.float32)
         191 +    release[10] = 1.0
         192 +    actions.append(("release", release))
         193 +    for k, (label, action) in enumerate(actions, 1):
         194 +        state, reward, term, trunc, _ = env.step(action)
         195 +        ss = snapshot(state)
         196 +        held = [name for name, data in ss.items()
         197 +                if name != "robot" and data.get("grasp_active", 0) > 0.5]
         198 +        print(k, label, "a", action.tolist(), "robot", ss["robot"],
         199 +              "block", ss["target_block"], "held", held,
         200 +              "reward/done", reward, term, trunc)
         201 +        if term or trunc:
         202 +            break
         203 +    env.close()
         204 +
         205 +
  163    206  if __name__ == "__main__":
  164    207      import argparse
  165    208      parser = argparse.ArgumentParser()
  166    209      parser.add_argument("--random", action="store_true")
  167    210      parser.add_argument("--grid", action="store_true")
  168    211      parser.add_argument("--triple", action="store_true")
         212 +    parser.add_argument("--exact", action="store_true")
  169    213      parser.add_argument("--seed", type=int, default=0)
  170    214      args = parser.parse_args()
  171        -    triple_grid(args.seed) if args.triple else (joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main()))
         215 +    exact_sequence(args.seed) if args.exact else (triple_grid(args.seed) if args.triple else (joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main())))
```

</details>

<a id="C017"></a>
### C017 · Handle variable obstructions with feedback-corrected placements

Commit `df38b42d6399ebf28c6fe73693c7c5d9b1276d75`; parents: 520ecd3ddd9e8a2714abf8bee8ffcb8c43b90193. Recorded author date: 2026-09-09T15:30:58+02:00.

File roles (automatic): policy.

- [E0064](01_timeline.md#E0064): commit hash in recorded output.
[Controller after this commit](evidence/versions/C017_df38b42_approach.py) · [Exact all-file diff](evidence/diffs/C017_df38b42.diff)

[Previous saved controller snapshot](evidence/versions/C010_77f8416_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a3110a6..a7bfa4d 100644
--- a/approach.py
+++ b/approach.py
@@ -41,44 +41,144 @@ class GeneratedApproach:
   41     41  
   42     42      def _solve(self, xyz, seed=None):
   43     43          start = _HOME if seed is None else seed
   44        -        base = np.array((self.base_x, self.base_y, 0.0))
          44 +        # The reported x=-.12 is the mobile-base bound; the arm pedestal is
          45 +        # mounted +.12 from it.  Hence the initial arm frame is world origin.
          46 +        base = np.array((self.base_x + .12, self.base_y, 0.0))
   45     47          def residual(q):
   46     48              t = _fk(q)
   47     49              grasp = base + t[:3, 3] + .12 * t[:3, 2]
   48        -            return np.r_[8 * (grasp - xyz), 1.5 * t[:2, 2], .03 * (q - _HOME)]
          50 +            return np.r_[10 * (grasp - xyz), 1.5 * t[:2, 2], .02 * (q - start)]
   49     51          return least_squares(residual, start, max_nfev=180).x
   50     52  
          53 +    def _xyz(self, state, name):
          54 +        return np.array([self._get(state, name, f"pose_{c}") for c in "xyz"])
          55 +
          56 +    def _robot_q(self, state):
          57 +        robot = state.get_object_from_name("robot")
          58 +        return np.array([float(state.get(robot, f"joint_{i}")) for i in range(1, 8)])
          59 +
          60 +    def _held(self, state):
          61 +        for name in state.get_object_names():
          62 +            if name != "robot":
          63 +                try:
          64 +                    if self._get(state, name, "grasp_active") > .5:
          65 +                        return name
          66 +                except (KeyError, ValueError):
          67 +                    pass
          68 +        return None
          69 +
          70 +    def _blocking(self, state, name):
          71 +        if not name.startswith("obstruction"):
          72 +            return False
          73 +        rx, ry = self._xyz(state, "target_region")[:2]
          74 +        ox, oy = self._xyz(state, name)[:2]
          75 +        rhx = self._get(state, "target_region", "half_extent_x")
          76 +        rhy = self._get(state, "target_region", "half_extent_y")
          77 +        ohx = self._get(state, name, "half_extent_x")
          78 +        ohy = self._get(state, name, "half_extent_y")
          79 +        return abs(ox-rx) < rhx+ohx+.006 and abs(oy-ry) < rhy+ohy+.006
          80 +
          81 +    def _choose_task(self, state):
          82 +        blockers = sorted(n for n in state.get_object_names() if self._blocking(state, n))
          83 +        if blockers:
          84 +            self.object = blockers[0]
          85 +            # Use rows opposite the goal. Staggering x prevents a pile even
          86 +            # when many independently sampled obstructions must be cleared.
          87 +            ry = self._xyz(state, "target_region")[1]
          88 +            i = self.park_count
          89 +            self.park_count += 1
          90 +            self.destination = np.array((.13 + .06*(i % 6), -.34 if ry >= 0 else .34,
          91 +                                         .075 + self._get(state, self.object, "half_extent_z")))
          92 +            return
          93 +        self.object = "target_block"
          94 +        reg = self._xyz(state, "target_region")
          95 +        z = reg[2] + self._get(state, "target_region", "half_extent_z")
          96 +        z += self._get(state, "target_block", "half_extent_z") + .006
          97 +        self.destination = np.array((reg[0], reg[1], z))
          98 +
          99 +    def _set_goal_for_object_delta(self, state, desired_object_xyz):
         100 +        q = self._robot_q(state)
         101 +        t = _fk(q)
         102 +        model_grasp = np.array((self.base_x + .12, self.base_y, 0.0)) + t[:3, 3] + .12*t[:3, 2]
         103 +        desired_grasp = model_grasp + desired_object_xyz - self._xyz(state, self._held(state))
         104 +        self.goal_q = self._solve(desired_grasp, q)
         105 +
         106 +    def _act_to(self, q, goal, grip=0.0):
         107 +        action = np.zeros(self.action_space.shape, dtype=np.float32)
         108 +        action[3:10] = np.clip(goal - q, -.2, .2)
         109 +        action[10] = grip
         110 +        return action
         111 +
   51    112      def reset(self, state, info):
   52    113          self.step = 0
         114 +        self.phase = "choose"
         115 +        self.phase_steps = 0
         116 +        self.park_count = 0
   53    117          self.base_x = self._get(state, "robot", "pos_base_x")
   54    118          self.base_y = self._get(state, "robot", "pos_base_y")
   55        -        block = np.array([self._get(state, "target_block", f"pose_{c}") for c in "xyz"])
   56        -        region = np.array([self._get(state, "target_region", f"pose_{c}") for c in "xyz"])
   57        -        self.pick_q = self._solve(block)
   58        -        self.lift_q = self._solve(block + (0, 0, .18), self.pick_q)
   59        -        self.place_q = self._solve(region + (0, 0, .08), self.lift_q)
   60        -        self.drop_q = self._solve(region + (0, 0, .03), self.place_q)
   61    119  
   62    120      def get_action(self, state):
   63    121          self.step += 1
   64        -        robot = state.get_object_from_name("robot")
   65        -        q = np.array([float(state.get(robot, f"joint_{i}")) for i in range(1, 8)])
   66        -        grasped = float(state.get(robot, "grasp_active")) > .5
   67        -        if self.step <= 18:
   68        -            goal, grip = self.pick_q, 1.0
   69        -        elif self.step <= 21:
   70        -            goal, grip = self.pick_q, -1.0
   71        -        elif self.step <= 35:
   72        -            goal, grip = self.lift_q, 0.0
   73        -        elif self.step <= 51:
   74        -            goal, grip = self.place_q, 0.0
   75        -        elif self.step <= 60:
   76        -            goal, grip = self.drop_q, 0.0
   77        -        else:
   78        -            goal, grip = self.drop_q, 1.0
   79        -        if 22 <= self.step <= 35 and not grasped:
   80        -            goal, grip = self.pick_q, -1.0
   81        -        action = np.zeros(self.action_space.shape, dtype=np.float32)
   82        -        action[3:10] = np.clip(goal - q, -.2, .2)
   83        -        action[10] = grip
   84        -        return action
         122 +        self.phase_steps += 1
         123 +        q = self._robot_q(state)
         124 +        held = self._held(state)
         125 +
         126 +        if self.phase == "choose":
         127 +            self._choose_task(state)
         128 +            self.goal_q = self._solve(self._xyz(state, self.object), q)
         129 +            self.phase, self.phase_steps = "pick", 0
         130 +
         131 +        if self.phase == "pick":
         132 +            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 35:
         133 +                self.phase, self.phase_steps = "close", 0
         134 +            else:
         135 +                return self._act_to(q, self.goal_q, 1.0)
         136 +
         137 +        if self.phase == "close":
         138 +            if held is not None:
         139 +                self.object = held  # handle a neighboring obstruction gracefully
         140 +                self.phase, self.phase_steps = "lift", 0
         141 +            elif self.phase_steps > 5:
         142 +                # Re-read its pose in case the open gripper nudged it.
         143 +                self.goal_q = self._solve(self._xyz(state, self.object), q)
         144 +                self.phase, self.phase_steps = "pick", 0
         145 +                return self._act_to(q, self.goal_q, 1.0)
         146 +            else:
         147 +                return self._act_to(q, q, -1.0)
         148 +
         149 +        if self.phase == "lift":
         150 +            # At table height a simultaneous Cartesian move may be rejected by
         151 +            # collision checking. Joint 4 positive is a reliable vertical escape.
         152 +            if self.phase_steps <= 4:
         153 +                action = self._act_to(q, q)
         154 +                action[6] = .18
         155 +                return action
         156 +            hover = self.destination.copy()
         157 +            hover[2] = max(.27, self.destination[2] + .16)
         158 +            self._set_goal_for_object_delta(state, hover)
         159 +            self.phase, self.phase_steps = "transfer", 0
         160 +
         161 +        if self.phase == "transfer":
         162 +            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 40:
         163 +                # Feedback from the grasped object's observed pose cancels the
         164 +                # unknown attachment transform and yields precise placement.
         165 +                self._set_goal_for_object_delta(state, self.destination)
         166 +                self.phase, self.phase_steps = "lower", 0
         167 +            else:
         168 +                return self._act_to(q, self.goal_q)
         169 +
         170 +        if self.phase == "lower":
         171 +            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 35:
         172 +                self.phase, self.phase_steps = "release", 0
         173 +            else:
         174 +                return self._act_to(q, self.goal_q)
         175 +
         176 +        if self.phase == "release":
         177 +            if held is None and self.phase_steps > 1:
         178 +                if self.object == "target_block":
         179 +                    # Keep open and let physics settle/termination register.
         180 +                    return self._act_to(q, q, 1.0)
         181 +                self.phase, self.phase_steps = "choose", 0
         182 +            return self._act_to(q, q, 1.0)
         183 +
         184 +        return self._act_to(q, q, 1.0)
```

</details>

<a id="C018"></a>
### C018 · Probe gripper release while moving

Commit `af7f31899e9a66053690275249d4c5775792f4fe`; parents: df38b42d6399ebf28c6fe73693c7c5d9b1276d75. Recorded author date: 2026-09-09T15:31:19+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C018_af7f318.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_instances.py b/probe_instances.py
index 69744c6..a5fa577 100644
--- a/probe_instances.py
+++ b/probe_instances.py
@@ -184,7 +184,7 @@ def full_place(seed):
  184    184          print("LIFT", drive(qlift, -1.), snapshot(s)["target_block"])
  185    185          if seed == 111:
  186    186              for gi in range(12):
  187        -                a = np.zeros(11, np.float32); a[10] = 1.
         187 +                a = np.zeros(11, np.float32); a[3] = .05; a[10] = 1.
  188    188                  s, r, term, trunc, _ = env.step(a)
  189    189                  print("OPEN", gi, snapshot(s)["robot"]["finger_state"], snapshot(s)["robot"]["grasp_active"], snapshot(s)["target_block"]["grasp_active"])
  190    190              return
```

</details>

<a id="C019"></a>
### C019 · Use collision-robust fingertip grasp offset

Commit `0777df176bc6b3b56680c75dbaa9f356ef928334`; parents: af7f31899e9a66053690275249d4c5775792f4fe. Recorded author date: 2026-09-09T15:31:24+02:00.

File roles (automatic): policy.

- [E0068](01_timeline.md#E0068): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_0777df1_approach.py) · [Exact all-file diff](evidence/diffs/C019_0777df1.diff)

[Previous saved controller snapshot](evidence/versions/C017_df38b42_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a7bfa4d..7160f34 100644
--- a/approach.py
+++ b/approach.py
@@ -46,7 +46,7 @@ class GeneratedApproach:
   46     46          base = np.array((self.base_x + .12, self.base_y, 0.0))
   47     47          def residual(q):
   48     48              t = _fk(q)
   49        -            grasp = base + t[:3, 3] + .12 * t[:3, 2]
          49 +            grasp = base + t[:3, 3] + .16 * t[:3, 2]
   50     50              return np.r_[10 * (grasp - xyz), 1.5 * t[:2, 2], .02 * (q - start)]
   51     51          return least_squares(residual, start, max_nfev=180).x
   52     52  
@@ -99,7 +99,7 @@ class GeneratedApproach:
   99     99      def _set_goal_for_object_delta(self, state, desired_object_xyz):
  100    100          q = self._robot_q(state)
  101    101          t = _fk(q)
  102        -        model_grasp = np.array((self.base_x + .12, self.base_y, 0.0)) + t[:3, 3] + .12*t[:3, 2]
         102 +        model_grasp = np.array((self.base_x + .12, self.base_y, 0.0)) + t[:3, 3] + .16*t[:3, 2]
  103    103          desired_grasp = model_grasp + desired_object_xyz - self._xyz(state, self._held(state))
  104    104          self.goal_q = self._solve(desired_grasp, q)
  105    105  
```

</details>

<a id="C020"></a>
### C020 · Measure carried-object response near grasp pose

Commit `ccc4f712dd87d1d3987d4957d0d9026a6cf12364`; parents: 0777df176bc6b3b56680c75dbaa9f356ef928334. Recorded author date: 2026-09-09T15:31:33+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C020_ccc4f71.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index d36c5aa..6e07967 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -203,6 +203,42 @@ def exact_sequence(seed=0):
  203    203      env.close()
  204    204  
  205    205  
         206 +def perturb_grasp(seed=0):
         207 +    """Measure one-step carried-object deltas about the successful grasp."""
         208 +    for index in range(10):
         209 +        for amount in (-0.1, 0.1):
         210 +            env = make_env()
         211 +            state, _ = env.reset(seed=seed)
         212 +            ss = snapshot(state)
         213 +            block0 = tuple(ss["target_block"]["pose_" + c] for c in "xyz")
         214 +            # Reach exact successful pose in three bounded moves.
         215 +            for k in range(3):
         216 +                a = np.zeros(11, dtype=np.float32)
         217 +                if k == 0:
         218 +                    a[1] = np.clip(block0[1], -0.2, 0.2)
         219 +                a[4] = 0.2
         220 +                a[6] = 0.2 if k == 0 else 0.0
         221 +                a[8] = 0.2 if k < 2 else 0.0
         222 +                state, *_ = env.step(a)
         223 +            a = np.zeros(11, dtype=np.float32)
         224 +            a[10] = -1.0
         225 +            state, *_ = env.step(a)
         226 +            before = snapshot(state)
         227 +            a = np.zeros(11, dtype=np.float32)
         228 +            a[index] = amount
         229 +            state, reward, term, trunc, _ = env.step(a)
         230 +            after = snapshot(state)
         231 +            delta = tuple(after["target_block"]["pose_" + c] -
         232 +                          before["target_block"]["pose_" + c] for c in "xyz")
         233 +            robot_delta = after["robot"].get(
         234 +                ["pos_base_x", "pos_base_y", "pos_base_rot"] +
         235 +                ["joint_" + str(i) for i in range(1, 8)][max(0, index - 3)], 0)
         236 +            print("PERTURB", index, amount, "delta", delta,
         237 +                  "still_held", after["robot"]["grasp_active"],
         238 +                  "robot", after["robot"], "done", term, trunc)
         239 +            env.close()
         240 +
         241 +
  206    242  if __name__ == "__main__":
  207    243      import argparse
  208    244      parser = argparse.ArgumentParser()
@@ -210,6 +246,7 @@ if __name__ == "__main__":
  210    246      parser.add_argument("--grid", action="store_true")
  211    247      parser.add_argument("--triple", action="store_true")
  212    248      parser.add_argument("--exact", action="store_true")
         249 +    parser.add_argument("--perturb", action="store_true")
  213    250      parser.add_argument("--seed", type=int, default=0)
  214    251      args = parser.parse_args()
  215        -    exact_sequence(args.seed) if args.exact else (triple_grid(args.seed) if args.triple else (joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main())))
         252 +    perturb_grasp(args.seed) if args.perturb else (exact_sequence(args.seed) if args.exact else (triple_grid(args.seed) if args.triple else (joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main()))))
```

</details>

<a id="C021"></a>
### C021 · Probe supported-object release at pickup pose

Commit `fd657accdc1f99ff724791429e470e9c1ab95e92`; parents: ccc4f712dd87d1d3987d4957d0d9026a6cf12364. Recorded author date: 2026-09-09T15:31:43+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C021_fd657ac.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_instances.py b/probe_instances.py
index a5fa577..9f7f5d8 100644
--- a/probe_instances.py
+++ b/probe_instances.py
@@ -178,6 +178,12 @@ def full_place(seed):
  178    178          drive(qpick, 1.)
  179    179          a = np.zeros(11, np.float32); a[10] = -1.; s, r, term, trunc, _ = env.step(a)
  180    180          print("PICK", snapshot(s)["robot"], qpick.tolist())
         181 +        if seed == 112:
         182 +            for gi in range(3):
         183 +                a = np.zeros(11, np.float32); a[10] = 1.
         184 +                s, r, term, trunc, _ = env.step(a)
         185 +                print("OPEN_AT_PICK", gi, snapshot(s)["robot"], snapshot(s)["target_block"])
         186 +            return
  181    187          region = start["target_region"]
  182    188          # Lift vertically before translating so the held block clears the table.
  183    189          qlift = ik(np.array([target["pose_x"], target["pose_y"], .30]), off=.16)
```

</details>

<a id="C022"></a>
### C022 · Fix carried-object perturbation probe

Commit `42aa406676be888b8eadc05f73c4363e438f38ce`; parents: fd657accdc1f99ff724791429e470e9c1ab95e92. Recorded author date: 2026-09-09T15:31:44+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C022_42aa406.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index 6e07967..fdd70a4 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -230,9 +230,6 @@ def perturb_grasp(seed=0):
  230    230              after = snapshot(state)
  231    231              delta = tuple(after["target_block"]["pose_" + c] -
  232    232                            before["target_block"]["pose_" + c] for c in "xyz")
  233        -            robot_delta = after["robot"].get(
  234        -                ["pos_base_x", "pos_base_y", "pos_base_rot"] +
  235        -                ["joint_" + str(i) for i in range(1, 8)][max(0, index - 3)], 0)
  236    233              print("PERTURB", index, amount, "delta", delta,
  237    234                    "still_held", after["robot"]["grasp_active"],
  238    235                    "robot", after["robot"], "done", term, trunc)
```

</details>

<a id="C023"></a>
### C023 · Test lifted transport before target release

Commit `997a264c0ac2d36766f615d9c889cada7634a37b`; parents: 42aa406676be888b8eadc05f73c4363e438f38ce. Recorded author date: 2026-09-09T15:32:41+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C023_997a264.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index fdd70a4..6f645d5 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -183,10 +183,18 @@ def exact_sequence(seed=0):
  183    183      close = np.zeros(11, dtype=np.float32)
  184    184      close[10] = -1.0
  185    185      actions.append(("close", close))
         186 +    for _ in range(4):
         187 +        lift = np.zeros(11, dtype=np.float32)
         188 +        lift[4] = -0.1
         189 +        actions.append(("lift_q2", lift))
  186    190      carry = np.zeros(11, dtype=np.float32)
  187    191      carry[0] = np.clip(region[0] - block0[0], -0.2, 0.2)
  188    192      carry[1] = np.clip(region[1] - block0[1], -0.2, 0.2)
  189    193      actions.append(("carry", carry))
         194 +    for _ in range(4):
         195 +        lower = np.zeros(11, dtype=np.float32)
         196 +        lower[4] = 0.1
         197 +        actions.append(("lower_q2", lower))
  190    198      release = np.zeros(11, dtype=np.float32)
  191    199      release[10] = 1.0
  192    200      actions.append(("release", release))
```

</details>

<a id="C024"></a>
### C024 · Preserve tool orientation through placement IK probe

Commit `7fc6982858ef50f740ea6071c22bbf3bef643979`; parents: 997a264c0ac2d36766f615d9c889cada7634a37b. Recorded author date: 2026-09-09T15:32:49+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C024_7fc6982.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_instances.py b/probe_instances.py
index 9f7f5d8..299dd8f 100644
--- a/probe_instances.py
+++ b/probe_instances.py
@@ -32,6 +32,14 @@ def ik(xyz, off=.12):
   32     32      return least_squares(fun, QHOME, max_nfev=300).x
   33     33  
   34     34  
          35 +def ik_fixed(xyz, seed, rotation, off=.16):
          36 +    def fun(q):
          37 +        t = fk(q); grasp = t[:3, 3] + off * t[:3, 2]
          38 +        dr = Rotation.from_matrix(rotation.T @ t[:3, :3]).as_rotvec()
          39 +        return np.r_[8 * (grasp - xyz), 2 * dr, .02 * (q - seed)]
          40 +    return least_squares(fun, seed, max_nfev=500).x
          41 +
          42 +
   35     43  def snapshot(state):
   36     44      rows = {}
   37     45      for name in state.get_object_names():
@@ -186,7 +194,8 @@ def full_place(seed):
  186    194              return
  187    195          region = start["target_region"]
  188    196          # Lift vertically before translating so the held block clears the table.
  189        -        qlift = ik(np.array([target["pose_x"], target["pose_y"], .30]), off=.16)
         197 +        rot = fk(qpick)[:3, :3]
         198 +        qlift = ik_fixed(np.array([target["pose_x"], target["pose_y"], .30]), qpick, rot)
  190    199          print("LIFT", drive(qlift, -1.), snapshot(s)["target_block"])
  191    200          if seed == 111:
  192    201              for gi in range(12):
@@ -194,11 +203,11 @@ def full_place(seed):
  194    203                  s, r, term, trunc, _ = env.step(a)
  195    204                  print("OPEN", gi, snapshot(s)["robot"]["finger_state"], snapshot(s)["robot"]["grasp_active"], snapshot(s)["target_block"]["grasp_active"])
  196    205              return
  197        -        qabove = ik(np.array([region["pose_x"], region["pose_y"], .30]), off=.16)
         206 +        qabove = ik_fixed(np.array([region["pose_x"], region["pose_y"], .30]), qlift, rot)
  198    207          print("ABOVE", drive(qabove, -1.), snapshot(s)["target_block"])
  199    208          xyz = np.array([region["pose_x"], region["pose_y"],
  200    209                          region["pose_z"] + region["half_extent_z"] + target["half_extent_z"]])
  201        -        qplace = ik(xyz, off=.16)
         210 +        qplace = ik_fixed(xyz, qabove, rot)
  202    211          print("MOVE", drive(qplace, -1.), "target", snapshot(s)["target_block"], "q", qplace.tolist())
  203    212          a = np.zeros(11, np.float32); a[10] = 1.
  204    213          for _ in range(8):
```

</details>

<a id="C025"></a>
### C025 · Preserve grasp orientation and lower objects onto support

Commit `8574b1169a0a2f47c4a10ffdf0ec8eb8264833d6`; parents: 7fc6982858ef50f740ea6071c22bbf3bef643979. Recorded author date: 2026-09-09T15:33:04+02:00.

File roles (automatic): policy.

- [E0077](01_timeline.md#E0077): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_8574b11_approach.py) · [Exact all-file diff](evidence/diffs/C025_8574b11.diff)

[Previous saved controller snapshot](evidence/versions/C019_0777df1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7160f34..f0621b2 100644
--- a/approach.py
+++ b/approach.py
@@ -47,7 +47,11 @@ class GeneratedApproach:
   47     47          def residual(q):
   48     48              t = _fk(q)
   49     49              grasp = base + t[:3, 3] + .16 * t[:3, 2]
   50        -            return np.r_[10 * (grasp - xyz), 1.5 * t[:2, 2], .02 * (q - start)]
          50 +            if self.carry_rotation is None:
          51 +                orientation = t[:2, 2]
          52 +            else:
          53 +                orientation = Rotation.from_matrix(self.carry_rotation.T @ t[:3, :3]).as_rotvec()
          54 +            return np.r_[10 * (grasp - xyz), 1.8 * orientation, .02 * (q - start)]
   51     55          return least_squares(residual, start, max_nfev=180).x
   52     56  
   53     57      def _xyz(self, state, name):
@@ -93,7 +97,9 @@ class GeneratedApproach:
   93     97          self.object = "target_block"
   94     98          reg = self._xyz(state, "target_region")
   95     99          z = reg[2] + self._get(state, "target_region", "half_extent_z")
   96        -        z += self._get(state, "target_block", "half_extent_z") + .006
         100 +        # A tiny penetration request lets collision resolution establish support;
         101 +        # airborne objects intentionally cannot be released by this environment.
         102 +        z += self._get(state, "target_block", "half_extent_z") - .002
   97    103          self.destination = np.array((reg[0], reg[1], z))
   98    104  
   99    105      def _set_goal_for_object_delta(self, state, desired_object_xyz):
@@ -114,6 +120,7 @@ class GeneratedApproach:
  114    120          self.phase = "choose"
  115    121          self.phase_steps = 0
  116    122          self.park_count = 0
         123 +        self.carry_rotation = None
  117    124          self.base_x = self._get(state, "robot", "pos_base_x")
  118    125          self.base_y = self._get(state, "robot", "pos_base_y")
  119    126  
@@ -137,6 +144,7 @@ class GeneratedApproach:
  137    144          if self.phase == "close":
  138    145              if held is not None:
  139    146                  self.object = held  # handle a neighboring obstruction gracefully
         147 +                self.carry_rotation = _fk(q)[:3, :3].copy()
  140    148                  self.phase, self.phase_steps = "lift", 0
  141    149              elif self.phase_steps > 5:
  142    150                  # Re-read its pose in case the open gripper nudged it.
@@ -179,6 +187,7 @@ class GeneratedApproach:
  179    187                      # Keep open and let physics settle/termination register.
  180    188                      return self._act_to(q, q, 1.0)
  181    189                  self.phase, self.phase_steps = "choose", 0
         190 +                self.carry_rotation = None
  182    191              return self._act_to(q, q, 1.0)
  183    192  
  184    193          return self._act_to(q, q, 1.0)
```

</details>

<a id="C026"></a>
### C026 · Use Cartesian descent waypoints in placement probe

Commit `9a12aef4ac81b5a75bfe1279ae6ef85e1b0cf394`; parents: 8574b1169a0a2f47c4a10ffdf0ec8eb8264833d6. Recorded author date: 2026-09-09T15:33:23+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C026_9a12aef.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_instances.py b/probe_instances.py
index 299dd8f..dcd8810 100644
--- a/probe_instances.py
+++ b/probe_instances.py
@@ -205,10 +205,11 @@ def full_place(seed):
  205    205              return
  206    206          qabove = ik_fixed(np.array([region["pose_x"], region["pose_y"], .30]), qlift, rot)
  207    207          print("ABOVE", drive(qabove, -1.), snapshot(s)["target_block"])
  208        -        xyz = np.array([region["pose_x"], region["pose_y"],
  209        -                        region["pose_z"] + region["half_extent_z"] + target["half_extent_z"]])
  210        -        qplace = ik_fixed(xyz, qabove, rot)
  211        -        print("MOVE", drive(qplace, -1.), "target", snapshot(s)["target_block"], "q", qplace.tolist())
         208 +        qplace = qabove
         209 +        for zlevel in (.25, .20, .16, .135, .115, .110):
         210 +            xyz = np.array([region["pose_x"], region["pose_y"], zlevel])
         211 +            qplace = ik_fixed(xyz, qplace, rot)
         212 +            print("DESCEND", zlevel, drive(qplace, -1.), snapshot(s)["target_block"])
  212    213          a = np.zeros(11, np.float32); a[10] = 1.
  213    214          for _ in range(8):
  214    215              s, r, term, trunc, _ = env.step(a)
```

</details>

<a id="C027"></a>
### C027 · Use safe vertical lift and staged Cartesian descent

Commit `a65111406d3284d5927d831804d04317c3426f78`; parents: 9a12aef4ac81b5a75bfe1279ae6ef85e1b0cf394. Recorded author date: 2026-09-09T15:33:37+02:00.

File roles (automatic): policy.

- [E0081](01_timeline.md#E0081): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C027_a651114_approach.py) · [Exact all-file diff](evidence/diffs/C027_a651114.diff)

[Previous saved controller snapshot](evidence/versions/C025_8574b11_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f0621b2..179c3a3 100644
--- a/approach.py
+++ b/approach.py
@@ -159,7 +159,7 @@ class GeneratedApproach:
  159    159              # collision checking. Joint 4 positive is a reliable vertical escape.
  160    160              if self.phase_steps <= 4:
  161    161                  action = self._act_to(q, q)
  162        -                action[6] = .18
         162 +                action[4] = -.12
  163    163                  return action
  164    164              hover = self.destination.copy()
  165    165              hover[2] = max(.27, self.destination[2] + .16)
@@ -168,16 +168,27 @@ class GeneratedApproach:
  168    168  
  169    169          if self.phase == "transfer":
  170    170              if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 40:
  171        -                # Feedback from the grasped object's observed pose cancels the
  172        -                # unknown attachment transform and yields precise placement.
  173        -                self._set_goal_for_object_delta(state, self.destination)
         171 +                # Short Cartesian-like descent segments avoid a joint-space
         172 +                # interpolation arc that can sweep the object into the table.
         173 +                self.descent_z = [self.destination[2]+d for d in (.10, .055, .025, 0)]
         174 +                self.descent_index = 0
         175 +                waypoint = self.destination.copy()
         176 +                waypoint[2] = self.descent_z[0]
         177 +                self._set_goal_for_object_delta(state, waypoint)
  174    178                  self.phase, self.phase_steps = "lower", 0
  175    179              else:
  176    180                  return self._act_to(q, self.goal_q)
  177    181  
  178    182          if self.phase == "lower":
  179    183              if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 35:
  180        -                self.phase, self.phase_steps = "release", 0
         184 +                self.descent_index += 1
         185 +                if self.descent_index >= len(self.descent_z):
         186 +                    self.phase, self.phase_steps = "release", 0
         187 +                else:
         188 +                    waypoint = self.destination.copy()
         189 +                    waypoint[2] = self.descent_z[self.descent_index]
         190 +                    self._set_goal_for_object_delta(state, waypoint)
         191 +                    self.phase_steps = 0
  181    192              else:
  182    193                  return self._act_to(q, self.goal_q)
  183    194  
```

</details>

<a id="C028"></a>
### C028 · Generalize discovered grasp with base alignment

Commit `499d0e3bad736b7220a7660f14e67b9cec36176a`; parents: a65111406d3284d5927d831804d04317c3426f78. Recorded author date: 2026-09-09T15:33:57+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C028_499d0e3.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index 6f645d5..20ea575 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -174,6 +174,7 @@ def exact_sequence(seed=0):
  174    174      for k in range(3):
  175    175          a = np.zeros(11, dtype=np.float32)
  176    176          if k == 0:
         177 +            a[0] = np.clip(block0[0] - 0.33598166704177856, -0.2, 0.0)
  177    178              a[1] = np.clip(block0[1] - ss["robot"]["pos_base_y"], -0.2, 0.2)
  178    179          a[4] = 0.2
  179    180          a[6] = 0.2 if k == 0 else 0.0
```

</details>

<a id="C029"></a>
### C029 · Refine supported descent with close vertical waypoints

Commit `a573a7f500497cfe07e7af232a38f16a31e85218`; parents: 499d0e3bad736b7220a7660f14e67b9cec36176a. Recorded author date: 2026-09-09T15:34:18+02:00.

File roles (automatic): policy.

- [E0087](01_timeline.md#E0087): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C029_a573a7f_approach.py) · [Exact all-file diff](evidence/diffs/C029_a573a7f.diff)

[Previous saved controller snapshot](evidence/versions/C027_a651114_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 179c3a3..39ec4dd 100644
--- a/approach.py
+++ b/approach.py
@@ -170,7 +170,7 @@ class GeneratedApproach:
  170    170              if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 40:
  171    171                  # Short Cartesian-like descent segments avoid a joint-space
  172    172                  # interpolation arc that can sweep the object into the table.
  173        -                self.descent_z = [self.destination[2]+d for d in (.10, .055, .025, 0)]
         173 +                self.descent_z = [self.destination[2]+d for d in (.142, .092, .052, .027, .007, 0)]
  174    174                  self.descent_index = 0
  175    175                  waypoint = self.destination.copy()
  176    176                  waypoint[2] = self.descent_z[0]
@@ -189,6 +189,7 @@ class GeneratedApproach:
  189    189                      waypoint[2] = self.descent_z[self.descent_index]
  190    190                      self._set_goal_for_object_delta(state, waypoint)
  191    191                      self.phase_steps = 0
         192 +                    return self._act_to(q, self.goal_q)
  192    193              else:
  193    194                  return self._act_to(q, self.goal_q)
  194    195  
```

</details>

<a id="C030"></a>
### C030 · Handle full target y range in grasp sequence

Commit `2906ab9b59a4f0d046f250ab6e442d91ba1a2cb4`; parents: a573a7f500497cfe07e7af232a38f16a31e85218. Recorded author date: 2026-09-09T15:34:20+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C030_2906ab9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index 20ea575..12a0094 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -173,9 +173,12 @@ def exact_sequence(seed=0):
  173    173      actions = []
  174    174      for k in range(3):
  175    175          a = np.zeros(11, dtype=np.float32)
         176 +        # Predicted current values are enough while constructing this fixed
         177 +        # sequence: x needs at most one move, y may need two bounded moves.
  176    178          if k == 0:
  177    179              a[0] = np.clip(block0[0] - 0.33598166704177856, -0.2, 0.0)
  178        -            a[1] = np.clip(block0[1] - ss["robot"]["pos_base_y"], -0.2, 0.2)
         180 +        if k < 2:
         181 +            a[1] = np.clip(block0[1] - (0.0 if k == 0 else np.clip(block0[1], -0.2, 0.2)), -0.2, 0.2)
  179    182          a[4] = 0.2
  180    183          a[6] = 0.2 if k == 0 else 0.0
  181    184          a[8] = 0.2 if k < 2 else 0.0
```

</details>

<a id="C031"></a>
### C031 · Calibrate supported release height

Commit `ab7b16606f7270242e6d9efbeaf6db113d9a4991`; parents: 2906ab9b59a4f0d046f250ab6e442d91ba1a2cb4. Recorded author date: 2026-09-09T15:35:07+02:00.

File roles (automatic): policy.

- [E0093](01_timeline.md#E0093): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C031_ab7b166_approach.py) · [Exact all-file diff](evidence/diffs/C031_ab7b166.diff)

[Previous saved controller snapshot](evidence/versions/C029_a573a7f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 39ec4dd..4b89bd0 100644
--- a/approach.py
+++ b/approach.py
@@ -92,14 +92,14 @@ class GeneratedApproach:
   92     92              i = self.park_count
   93     93              self.park_count += 1
   94     94              self.destination = np.array((.13 + .06*(i % 6), -.34 if ry >= 0 else .34,
   95        -                                         .075 + self._get(state, self.object, "half_extent_z")))
          95 +                                         .078 + self._get(state, self.object, "half_extent_z")))
   96     96              return
   97     97          self.object = "target_block"
   98     98          reg = self._xyz(state, "target_region")
   99     99          z = reg[2] + self._get(state, "target_region", "half_extent_z")
  100        -        # A tiny penetration request lets collision resolution establish support;
  101        -        # airborne objects intentionally cannot be released by this environment.
  102        -        z += self._get(state, "target_block", "half_extent_z") - .002
         100 +        # Contact is recognized a few millimeters above the analytical surface.
         101 +        # Airborne objects intentionally cannot be released by this environment.
         102 +        z += self._get(state, "target_block", "half_extent_z") + .003
  103    103          self.destination = np.array((reg[0], reg[1], z))
  104    104  
  105    105      def _set_goal_for_object_delta(self, state, desired_object_xyz):
```

</details>

<a id="C032"></a>
### C032 · Interpolate a far-reach target grasp anchor

Commit `55de0b26bdf1f6a2977edd04e5ea7297f139bc8e`; parents: ab7b16606f7270242e6d9efbeaf6db113d9a4991. Recorded author date: 2026-09-09T15:37:12+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C032_55de0b2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index 12a0094..bc59631 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -184,6 +184,15 @@ def exact_sequence(seed=0):
  184    184          a[8] = 0.2 if k < 2 else 0.0
  185    185          a[10] = 1.0
  186    186          actions.append(("pose_open", a))
         187 +    far_extra = np.clip(
         188 +        (block0[0] - 0.33598166704177856) /
         189 +        (0.4644085764884949 - 0.33598166704177856) * 0.2,
         190 +        0.0, 0.2)
         191 +    if far_extra > 1e-6:
         192 +        a = np.zeros(11, dtype=np.float32)
         193 +        a[[4, 6, 8]] = far_extra
         194 +        a[10] = 1.0
         195 +        actions.append(("far_reach", a))
  187    196      close = np.zeros(11, dtype=np.float32)
  188    197      close[10] = -1.0
  189    198      actions.append(("close", close))
```

</details>

<a id="C033"></a>
### C033 · Approach pickups through collision-safe Cartesian waypoints

Commit `20d3842de52e070d9eea27c0b54ceab5a2b1d452`; parents: 55de0b26bdf1f6a2977edd04e5ea7297f139bc8e. Recorded author date: 2026-09-09T15:37:56+02:00.

File roles (automatic): policy.

- [E0101](01_timeline.md#E0101): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C033_20d3842_approach.py) · [Exact all-file diff](evidence/diffs/C033_20d3842.diff)

[Previous saved controller snapshot](evidence/versions/C031_ab7b166_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4b89bd0..b9d5ddd 100644
--- a/approach.py
+++ b/approach.py
@@ -132,12 +132,32 @@ class GeneratedApproach:
  132    132  
  133    133          if self.phase == "choose":
  134    134              self._choose_task(state)
  135        -            self.goal_q = self._solve(self._xyz(state, self.object), q)
  136        -            self.phase, self.phase_steps = "pick", 0
         135 +            self.carry_rotation = None
         136 +            self.pick_xyz = self._xyz(state, self.object)
         137 +            self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
         138 +            self.phase, self.phase_steps = "prepick", 0
         139 +
         140 +        if self.phase == "prepick":
         141 +            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 40:
         142 +                self.carry_rotation = _fk(q)[:3, :3].copy()
         143 +                self.pick_z = [self.pick_xyz[2]+d for d in (.10, .05, 0)]
         144 +                self.pick_index = 0
         145 +                waypoint = self.pick_xyz.copy(); waypoint[2] = self.pick_z[0]
         146 +                self.goal_q = self._solve(waypoint, q)
         147 +                self.phase, self.phase_steps = "pick", 0
         148 +            else:
         149 +                return self._act_to(q, self.goal_q, 1.0)
  137    150  
  138    151          if self.phase == "pick":
  139        -            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 35:
  140        -                self.phase, self.phase_steps = "close", 0
         152 +            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 30:
         153 +                self.pick_index += 1
         154 +                if self.pick_index >= len(self.pick_z):
         155 +                    self.phase, self.phase_steps = "close", 0
         156 +                else:
         157 +                    waypoint = self.pick_xyz.copy(); waypoint[2] = self.pick_z[self.pick_index]
         158 +                    self.goal_q = self._solve(waypoint, q)
         159 +                    self.phase_steps = 0
         160 +                    return self._act_to(q, self.goal_q, 1.0)
  141    161              else:
  142    162                  return self._act_to(q, self.goal_q, 1.0)
  143    163  
@@ -147,9 +167,11 @@ class GeneratedApproach:
  147    167                  self.carry_rotation = _fk(q)[:3, :3].copy()
  148    168                  self.phase, self.phase_steps = "lift", 0
  149    169              elif self.phase_steps > 5:
  150        -                # Re-read its pose in case the open gripper nudged it.
  151        -                self.goal_q = self._solve(self._xyz(state, self.object), q)
  152        -                self.phase, self.phase_steps = "pick", 0
         170 +                # Retry through a collision-safe overhead approach.
         171 +                self.carry_rotation = None
         172 +                self.pick_xyz = self._xyz(state, self.object)
         173 +                self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
         174 +                self.phase, self.phase_steps = "prepick", 0
  153    175                  return self._act_to(q, self.goal_q, 1.0)
  154    176              else:
  155    177                  return self._act_to(q, q, -1.0)
```

</details>

<a id="C034"></a>
### C034 · Test calibrated grasp on named obstructions

Commit `f3147931d189137eade450c2c319aca579ff3edd`; parents: 20d3842de52e070d9eea27c0b54ceab5a2b1d452. Recorded author date: 2026-09-09T15:38:17+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C034_f314793.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
index bc59631..df5e6f9 100644
--- a/probe_grasp.py
+++ b/probe_grasp.py
@@ -257,6 +257,33 @@ def perturb_grasp(seed=0):
  257    257              env.close()
  258    258  
  259    259  
         260 +def grasp_named(seed=0, name="obstruction0"):
         261 +    """Try the calibrated table-height grasp on an arbitrary cuboid."""
         262 +    env = make_env()
         263 +    state, _ = env.reset(seed=seed)
         264 +    ss = snapshot(state)
         265 +    xyz = tuple(ss[name]["pose_" + c] for c in "xyz")
         266 +    desired_bx = xyz[0] - 0.45598166435956955
         267 +    for k in range(3):
         268 +        now = snapshot(state)["robot"]
         269 +        a = np.zeros(11, dtype=np.float32)
         270 +        a[0] = np.clip(desired_bx - now["pos_base_x"], -0.2, 0.0)
         271 +        a[1] = np.clip(xyz[1] - now["pos_base_y"], -0.2, 0.2)
         272 +        a[4] = 0.2
         273 +        a[6] = 0.2 if k == 0 else 0.0
         274 +        a[8] = 0.2 if k < 2 else 0.0
         275 +        a[10] = 1.0
         276 +        state, *_ = env.step(a)
         277 +    a = np.zeros(11, dtype=np.float32)
         278 +    a[10] = -1.0
         279 +    state, reward, term, trunc, _ = env.step(a)
         280 +    ss = snapshot(state)
         281 +    print("NAMED", seed, name, "xyz", xyz, "robot", ss["robot"],
         282 +          "held", [n for n, d in ss.items() if n != "robot" and d.get("grasp_active", 0) > .5],
         283 +          "done", reward, term, trunc)
         284 +    env.close()
         285 +
         286 +
  260    287  if __name__ == "__main__":
  261    288      import argparse
  262    289      parser = argparse.ArgumentParser()
@@ -265,6 +292,8 @@ if __name__ == "__main__":
  265    292      parser.add_argument("--triple", action="store_true")
  266    293      parser.add_argument("--exact", action="store_true")
  267    294      parser.add_argument("--perturb", action="store_true")
         295 +    parser.add_argument("--object", default="obstruction0")
         296 +    parser.add_argument("--named", action="store_true")
  268    297      parser.add_argument("--seed", type=int, default=0)
  269    298      args = parser.parse_args()
  270        -    perturb_grasp(args.seed) if args.perturb else (exact_sequence(args.seed) if args.exact else (triple_grid(args.seed) if args.triple else (joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main()))))
         299 +    grasp_named(args.seed, args.object) if args.named else (perturb_grasp(args.seed) if args.perturb else (exact_sequence(args.seed) if args.exact else (triple_grid(args.seed) if args.triple else (joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main())))))
```

</details>

<a id="C035"></a>
### C035 · Improve dense-obstruction ordering lift and retraction

Commit `500304afc15501543b36cdc775c95cdb912469a8`; parents: f3147931d189137eade450c2c319aca579ff3edd. Recorded author date: 2026-09-09T15:41:43+02:00.

File roles (automatic): policy.

- [E0111](01_timeline.md#E0111): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C035_500304a_approach.py) · [Exact all-file diff](evidence/diffs/C035_500304a.diff)

[Previous saved controller snapshot](evidence/versions/C033_20d3842_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b9d5ddd..37a107b 100644
--- a/approach.py
+++ b/approach.py
@@ -83,7 +83,8 @@ class GeneratedApproach:
   83     83          return abs(ox-rx) < rhx+ohx+.006 and abs(oy-ry) < rhy+ohy+.006
   84     84  
   85     85      def _choose_task(self, state):
   86        -        blockers = sorted(n for n in state.get_object_names() if self._blocking(state, n))
          86 +        blockers = sorted((n for n in state.get_object_names() if self._blocking(state, n)),
          87 +                          key=lambda n: -self._xyz(state, n)[2])
   87     88          if blockers:
   88     89              self.object = blockers[0]
   89     90              # Use rows opposite the goal. Staggering x prevents a pile even
@@ -165,6 +166,7 @@ class GeneratedApproach:
  165    166              if held is not None:
  166    167                  self.object = held  # handle a neighboring obstruction gracefully
  167    168                  self.carry_rotation = _fk(q)[:3, :3].copy()
         169 +                self.lift_start_z = self._xyz(state, held)[2]
  168    170                  self.phase, self.phase_steps = "lift", 0
  169    171              elif self.phase_steps > 5:
  170    172                  # Retry through a collision-safe overhead approach.
@@ -179,10 +181,18 @@ class GeneratedApproach:
  179    181          if self.phase == "lift":
  180    182              # At table height a simultaneous Cartesian move may be rejected by
  181    183              # collision checking. Joint 4 positive is a reliable vertical escape.
  182        -            if self.phase_steps <= 4:
         184 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 4:
  183    185                  action = self._act_to(q, q)
  184    186                  action[4] = -.12
  185    187                  return action
         188 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 9:
         189 +                action = self._act_to(q, q)
         190 +                action[6] = .10
         191 +                return action
         192 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 15:
         193 +                action = self._act_to(q, q)
         194 +                action[4], action[6] = -.06, .06
         195 +                return action
  186    196              hover = self.destination.copy()
  187    197              hover[2] = max(.27, self.destination[2] + .16)
  188    198              self._set_goal_for_object_delta(state, hover)
@@ -220,8 +230,15 @@ class GeneratedApproach:
  220    230                  if self.object == "target_block":
  221    231                      # Keep open and let physics settle/termination register.
  222    232                      return self._act_to(q, q, 1.0)
  223        -                self.phase, self.phase_steps = "choose", 0
         233 +                self.phase, self.phase_steps = "retract", 0
  224    234                  self.carry_rotation = None
  225    235              return self._act_to(q, q, 1.0)
  226    236  
         237 +        if self.phase == "retract":
         238 +            if self.phase_steps <= 5:
         239 +                action = self._act_to(q, q, 1.0)
         240 +                action[4] = -.12
         241 +                return action
         242 +            self.phase, self.phase_steps = "choose", 0
         243 +
  227    244          return self._act_to(q, q, 1.0)
```

</details>

<a id="C036"></a>
### C036 · Add calibrated target grasp and obstruction recovery

Commit `c9b0cbf619e9ec8dd586667b57f222af9f2801d6`; parents: 500304afc15501543b36cdc775c95cdb912469a8. Recorded author date: 2026-09-09T15:44:56+02:00.

File roles (automatic): policy.

- [E0119](01_timeline.md#E0119): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C036_c9b0cbf_approach.py) · [Exact all-file diff](evidence/diffs/C036_c9b0cbf.diff)

[Previous saved controller snapshot](evidence/versions/C035_500304a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 37a107b..fd8015e 100644
--- a/approach.py
+++ b/approach.py
@@ -84,7 +84,7 @@ class GeneratedApproach:
   84     84  
   85     85      def _choose_task(self, state):
   86     86          blockers = sorted((n for n in state.get_object_names() if self._blocking(state, n)),
   87        -                          key=lambda n: -self._xyz(state, n)[2])
          87 +                          key=lambda n: (n in self.deferred, -self._xyz(state, n)[2]))
   88     88          if blockers:
   89     89              self.object = blockers[0]
   90     90              # Use rows opposite the goal. Staggering x prevents a pile even
@@ -121,6 +121,7 @@ class GeneratedApproach:
  121    121          self.phase = "choose"
  122    122          self.phase_steps = 0
  123    123          self.park_count = 0
         124 +        self.deferred = set()
  124    125          self.carry_rotation = None
  125    126          self.base_x = self._get(state, "robot", "pos_base_x")
  126    127          self.base_y = self._get(state, "robot", "pos_base_y")
@@ -130,11 +131,42 @@ class GeneratedApproach:
  130    131          self.phase_steps += 1
  131    132          q = self._robot_q(state)
  132    133          held = self._held(state)
         134 +        self.base_x = self._get(state, "robot", "pos_base_x")
         135 +        self.base_y = self._get(state, "robot", "pos_base_y")
  133    136  
  134    137          if self.phase == "choose":
  135    138              self._choose_task(state)
  136    139              self.carry_rotation = None
  137    140              self.pick_xyz = self._xyz(state, self.object)
         141 +            if self.object == "target_block":
         142 +                u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
         143 +                self.anchor_q = np.array((0, .25+.2*u, -np.pi, -2.30+.2*u,
         144 +                                          0, -.47+.2*u, np.pi/2))
         145 +                self.anchor_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
         146 +                self.anchor_by = self.pick_xyz[1]
         147 +                self.goal_q = _HOME.copy()
         148 +                self.phase, self.phase_steps = "target_home", 0
         149 +            else:
         150 +                self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
         151 +                self.phase, self.phase_steps = "prepick", 0
         152 +
         153 +        if self.phase == "target_home":
         154 +            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 25:
         155 +                self.goal_q = self.anchor_q
         156 +                self.phase, self.phase_steps = "target_anchor", 0
         157 +            else:
         158 +                return self._act_to(q, self.goal_q, 1.0)
         159 +
         160 +        if self.phase == "target_anchor":
         161 +            bxerr, byerr = self.anchor_bx-self.base_x, self.anchor_by-self.base_y
         162 +            if np.max(np.abs(self.goal_q-q)) < .012 and max(abs(bxerr),abs(byerr)) < .005:
         163 +                self.phase, self.phase_steps = "close", 0
         164 +            else:
         165 +                action = self._act_to(q, self.goal_q, 1.0)
         166 +                action[0], action[1] = np.clip(bxerr, -.2, .2), np.clip(byerr, -.2, .2)
         167 +                return action
         168 +
         169 +        if self.phase == "choose":
  138    170              self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
  139    171              self.phase, self.phase_steps = "prepick", 0
  140    172  
@@ -172,8 +204,12 @@ class GeneratedApproach:
  172    204                  # Retry through a collision-safe overhead approach.
  173    205                  self.carry_rotation = None
  174    206                  self.pick_xyz = self._xyz(state, self.object)
  175        -                self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
  176        -                self.phase, self.phase_steps = "prepick", 0
         207 +                if self.object == "target_block":
         208 +                    self.goal_q = _HOME.copy()
         209 +                    self.phase, self.phase_steps = "target_home", 0
         210 +                else:
         211 +                    self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
         212 +                    self.phase, self.phase_steps = "prepick", 0
  177    213                  return self._act_to(q, self.goal_q, 1.0)
  178    214              else:
  179    215                  return self._act_to(q, q, -1.0)
@@ -193,6 +229,10 @@ class GeneratedApproach:
  193    229                  action = self._act_to(q, q)
  194    230                  action[4], action[6] = -.06, .06
  195    231                  return action
         232 +            if self._xyz(state, held)[2] < self.lift_start_z + .06:
         233 +                self.deferred.add(self.object)
         234 +                self.phase, self.phase_steps = "release", 0
         235 +                return self._act_to(q, q, 1.0)
  196    236              hover = self.destination.copy()
  197    237              hover[2] = max(.27, self.destination[2] + .16)
  198    238              self._set_goal_for_object_delta(state, hover)
@@ -230,6 +270,7 @@ class GeneratedApproach:
  230    270                  if self.object == "target_block":
  231    271                      # Keep open and let physics settle/termination register.
  232    272                      return self._act_to(q, q, 1.0)
         273 +                self.deferred.discard(self.object)
  233    274                  self.phase, self.phase_steps = "retract", 0
  234    275                  self.carry_rotation = None
  235    276              return self._act_to(q, q, 1.0)
@@ -239,6 +280,13 @@ class GeneratedApproach:
  239    280                  action = self._act_to(q, q, 1.0)
  240    281                  action[4] = -.12
  241    282                  return action
  242        -            self.phase, self.phase_steps = "choose", 0
         283 +            self.goal_q = _HOME.copy()
         284 +            self.phase, self.phase_steps = "home", 0
         285 +
         286 +        if self.phase == "home":
         287 +            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 30:
         288 +                self.phase, self.phase_steps = "choose", 0
         289 +            else:
         290 +                return self._act_to(q, self.goal_q, 1.0)
  243    291  
  244    292          return self._act_to(q, q, 1.0)
```

</details>

<a id="C037"></a>
### C037 · Reposition mobile base for reliable picks and transfers

Commit `98f2ea54a127f040b35040be8c273d44b8f0d458`; parents: c9b0cbf619e9ec8dd586667b57f222af9f2801d6. Recorded author date: 2026-09-09T15:47:57+02:00.

File roles (automatic): policy.

- [E0125](01_timeline.md#E0125): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C037_98f2ea5_approach.py) · [Exact all-file diff](evidence/diffs/C037_98f2ea5.diff)

[Previous saved controller snapshot](evidence/versions/C036_c9b0cbf_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fd8015e..c7b90c4 100644
--- a/approach.py
+++ b/approach.py
@@ -90,10 +90,14 @@ class GeneratedApproach:
   90     90              # Use rows opposite the goal. Staggering x prevents a pile even
   91     91              # when many independently sampled obstructions must be cleared.
   92     92              ry = self._xyz(state, "target_region")[1]
   93        -            i = self.park_count
   94        -            self.park_count += 1
   95        -            self.destination = np.array((.13 + .06*(i % 6), -.34 if ry >= 0 else .34,
   96        -                                         .078 + self._get(state, self.object, "half_extent_z")))
          93 +            if self.object not in self.park_spots:
          94 +                i = len(self.park_spots)
          95 +                side = -.34 if ry >= 0 else .34
          96 +                px = .13 + .12*(i % 4)
          97 +                py = side - np.sign(side)*.07*(i // 4)
          98 +                self.park_spots[self.object] = (px, py)
          99 +            px, py = self.park_spots[self.object]
         100 +            self.destination = np.array((px, py, .078 + self._get(state, self.object, "half_extent_z")))
   97    101              return
   98    102          self.object = "target_block"
   99    103          reg = self._xyz(state, "target_region")
@@ -121,7 +125,9 @@ class GeneratedApproach:
  121    125          self.phase = "choose"
  122    126          self.phase_steps = 0
  123    127          self.park_count = 0
         128 +        self.park_spots = {}
  124    129          self.deferred = set()
         130 +        self.abandoning = False
  125    131          self.carry_rotation = None
  126    132          self.base_x = self._get(state, "robot", "pos_base_x")
  127    133          self.base_y = self._get(state, "robot", "pos_base_y")
@@ -147,8 +153,21 @@ class GeneratedApproach:
  147    153                  self.goal_q = _HOME.copy()
  148    154                  self.phase, self.phase_steps = "target_home", 0
  149    155              else:
         156 +                self.goal_q = _HOME.copy()
         157 +                self.pick_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
         158 +                self.pick_by = self.pick_xyz[1]
         159 +                self.phase, self.phase_steps = "prepick_base", 0
         160 +
         161 +        if self.phase == "prepick_base":
         162 +            bxerr, byerr = self.pick_bx-self.base_x, self.pick_by-self.base_y
         163 +            if (np.max(np.abs(self.goal_q-q)) < .012 and
         164 +                    max(abs(bxerr), abs(byerr)) < .005) or self.phase_steps > 30:
  150    165                  self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
  151    166                  self.phase, self.phase_steps = "prepick", 0
         167 +            else:
         168 +                action = self._act_to(q, self.goal_q, 1.0)
         169 +                action[0], action[1] = np.clip(bxerr, -.2, .2), np.clip(byerr, -.2, .2)
         170 +                return action
  152    171  
  153    172          if self.phase == "target_home":
  154    173              if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 25:
@@ -199,6 +218,7 @@ class GeneratedApproach:
  199    218                  self.object = held  # handle a neighboring obstruction gracefully
  200    219                  self.carry_rotation = _fk(q)[:3, :3].copy()
  201    220                  self.lift_start_z = self._xyz(state, held)[2]
         221 +                self.abandoning = False
  202    222                  self.phase, self.phase_steps = "lift", 0
  203    223              elif self.phase_steps > 5:
  204    224                  # Retry through a collision-safe overhead approach.
@@ -208,8 +228,8 @@ class GeneratedApproach:
  208    228                      self.goal_q = _HOME.copy()
  209    229                      self.phase, self.phase_steps = "target_home", 0
  210    230                  else:
  211        -                    self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
  212        -                    self.phase, self.phase_steps = "prepick", 0
         231 +                    self.goal_q = _HOME.copy()
         232 +                    self.phase, self.phase_steps = "prepick_base", 0
  213    233                  return self._act_to(q, self.goal_q, 1.0)
  214    234              else:
  215    235                  return self._act_to(q, q, -1.0)
@@ -231,12 +251,24 @@ class GeneratedApproach:
  231    251                  return action
  232    252              if self._xyz(state, held)[2] < self.lift_start_z + .06:
  233    253                  self.deferred.add(self.object)
         254 +                self.abandoning = True
  234    255                  self.phase, self.phase_steps = "release", 0
  235    256                  return self._act_to(q, q, 1.0)
  236        -            hover = self.destination.copy()
  237        -            hover[2] = max(.27, self.destination[2] + .16)
  238        -            self._set_goal_for_object_delta(state, hover)
  239        -            self.phase, self.phase_steps = "transfer", 0
         257 +            self.transport_bx = self.destination[0]-.4559817 if self.destination[0] <= .3359817 else -.12
         258 +            self.transport_by = self.destination[1]
         259 +            self.phase, self.phase_steps = "base_transfer", 0
         260 +
         261 +        if self.phase == "base_transfer":
         262 +            bxerr, byerr = self.transport_bx-self.base_x, self.transport_by-self.base_y
         263 +            if max(abs(bxerr), abs(byerr)) < .005 or self.phase_steps > 20:
         264 +                hover = self.destination.copy()
         265 +                hover[2] = max(.27, self.destination[2] + .16)
         266 +                self._set_goal_for_object_delta(state, hover)
         267 +                self.phase, self.phase_steps = "transfer", 0
         268 +            else:
         269 +                action = self._act_to(q, q)
         270 +                action[0], action[1] = np.clip(bxerr, -.2, .2), np.clip(byerr, -.2, .2)
         271 +                return action
  240    272  
  241    273          if self.phase == "transfer":
  242    274              if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 40:
@@ -270,7 +302,8 @@ class GeneratedApproach:
  270    302                  if self.object == "target_block":
  271    303                      # Keep open and let physics settle/termination register.
  272    304                      return self._act_to(q, q, 1.0)
  273        -                self.deferred.discard(self.object)
         305 +                if not self.abandoning:
         306 +                    self.deferred.discard(self.object)
  274    307                  self.phase, self.phase_steps = "retract", 0
  275    308                  self.carry_rotation = None
  276    309              return self._act_to(q, q, 1.0)
```

</details>

<a id="C038"></a>
### C038 · Defer collision-blocked obstruction grasps

Commit `9c8397b4a97a9d7dd65b2386f15e52f20ca217f6`; parents: 98f2ea54a127f040b35040be8c273d44b8f0d458. Recorded author date: 2026-09-09T15:49:35+02:00.

File roles (automatic): policy.

- [E0131](01_timeline.md#E0131): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C038_9c8397b_approach.py) · [Exact all-file diff](evidence/diffs/C038_9c8397b.diff)

[Previous saved controller snapshot](evidence/versions/C037_98f2ea5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c7b90c4..ef94456 100644
--- a/approach.py
+++ b/approach.py
@@ -228,8 +228,10 @@ class GeneratedApproach:
  228    228                      self.goal_q = _HOME.copy()
  229    229                      self.phase, self.phase_steps = "target_home", 0
  230    230                  else:
  231        -                    self.goal_q = _HOME.copy()
  232        -                    self.phase, self.phase_steps = "prepick_base", 0
         231 +                    # In a dense cluster, try a neighbor first; removing either
         232 +                    # one often makes the original vertical grasp collision-free.
         233 +                    self.deferred.add(self.object)
         234 +                    self.phase, self.phase_steps = "retract", 0
  233    235                  return self._act_to(q, self.goal_q, 1.0)
  234    236              else:
  235    237                  return self._act_to(q, q, -1.0)
```

</details>

<a id="C039"></a>
### C039 · Grasp obstructions near their collision-free top edge

Commit `3e03d41dcd2715e8dea4e40294bd377548732929`; parents: 9c8397b4a97a9d7dd65b2386f15e52f20ca217f6. Recorded author date: 2026-09-09T15:50:57+02:00.

File roles (automatic): policy.

- [E0137](01_timeline.md#E0137): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C039_3e03d41_approach.py) · [Exact all-file diff](evidence/diffs/C039_3e03d41.diff)

[Previous saved controller snapshot](evidence/versions/C038_9c8397b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ef94456..ded4325 100644
--- a/approach.py
+++ b/approach.py
@@ -144,6 +144,10 @@ class GeneratedApproach:
  144    144              self._choose_task(state)
  145    145              self.carry_rotation = None
  146    146              self.pick_xyz = self._xyz(state, self.object)
         147 +            if self.object.startswith("obstruction"):
         148 +                # Pinch near the top: center-height grasps can put fingertips
         149 +                # into the target plate or an immediately adjacent blocker.
         150 +                self.pick_xyz[2] += .8*self._get(state, self.object, "half_extent_z")
  147    151              if self.object == "target_block":
  148    152                  u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
  149    153                  self.anchor_q = np.array((0, .25+.2*u, -np.pi, -2.30+.2*u,
@@ -224,6 +228,8 @@ class GeneratedApproach:
  224    228                  # Retry through a collision-safe overhead approach.
  225    229                  self.carry_rotation = None
  226    230                  self.pick_xyz = self._xyz(state, self.object)
         231 +                if self.object.startswith("obstruction"):
         232 +                    self.pick_xyz[2] += .8*self._get(state, self.object, "half_extent_z")
  227    233                  if self.object == "target_block":
  228    234                      self.goal_q = _HOME.copy()
  229    235                      self.phase, self.phase_steps = "target_home", 0
```

</details>

<a id="C040"></a>
### C040 · Tune elevated obstruction pinch height

Commit `d7e942929cd546c174e12c71ed3992f96980e3f8`; parents: 3e03d41dcd2715e8dea4e40294bd377548732929. Recorded author date: 2026-09-09T15:51:59+02:00.

File roles (automatic): policy.

- [E0143](01_timeline.md#E0143): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C040_d7e9429_approach.py) · [Exact all-file diff](evidence/diffs/C040_d7e9429.diff)

[Previous saved controller snapshot](evidence/versions/C039_3e03d41_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ded4325..fc34ca8 100644
--- a/approach.py
+++ b/approach.py
@@ -147,7 +147,7 @@ class GeneratedApproach:
  147    147              if self.object.startswith("obstruction"):
  148    148                  # Pinch near the top: center-height grasps can put fingertips
  149    149                  # into the target plate or an immediately adjacent blocker.
  150        -                self.pick_xyz[2] += .8*self._get(state, self.object, "half_extent_z")
         150 +                self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
  151    151              if self.object == "target_block":
  152    152                  u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
  153    153                  self.anchor_q = np.array((0, .25+.2*u, -np.pi, -2.30+.2*u,
@@ -229,7 +229,7 @@ class GeneratedApproach:
  229    229                  self.carry_rotation = None
  230    230                  self.pick_xyz = self._xyz(state, self.object)
  231    231                  if self.object.startswith("obstruction"):
  232        -                    self.pick_xyz[2] += .8*self._get(state, self.object, "half_extent_z")
         232 +                    self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
  233    233                  if self.object == "target_block":
  234    234                      self.goal_q = _HOME.copy()
  235    235                      self.phase, self.phase_steps = "target_home", 0
```

</details>

<a id="C041"></a>
### C041 · Use calibrated base-translated grasp for every block

Commit `db6fc0322dc8496412aec20c6a61941565674caf`; parents: d7e942929cd546c174e12c71ed3992f96980e3f8. Recorded author date: 2026-09-09T15:53:41+02:00.

File roles (automatic): policy.

- [E0151](01_timeline.md#E0151): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C041_db6fc03_approach.py) · [Exact all-file diff](evidence/diffs/C041_db6fc03.diff)

[Previous saved controller snapshot](evidence/versions/C040_d7e9429_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fc34ca8..0fcc1bc 100644
--- a/approach.py
+++ b/approach.py
@@ -148,19 +148,16 @@ class GeneratedApproach:
  148    148                  # Pinch near the top: center-height grasps can put fingertips
  149    149                  # into the target plate or an immediately adjacent blocker.
  150    150                  self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
  151        -            if self.object == "target_block":
  152        -                u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
  153        -                self.anchor_q = np.array((0, .25+.2*u, -np.pi, -2.30+.2*u,
  154        -                                          0, -.47+.2*u, np.pi/2))
  155        -                self.anchor_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
  156        -                self.anchor_by = self.pick_xyz[1]
  157        -                self.goal_q = _HOME.copy()
  158        -                self.phase, self.phase_steps = "target_home", 0
  159        -            else:
  160        -                self.goal_q = _HOME.copy()
  161        -                self.pick_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
  162        -                self.pick_by = self.pick_xyz[1]
  163        -                self.phase, self.phase_steps = "prepick_base", 0
         151 +            # A calibrated vertical grasp pose plus base translation is more
         152 +            # collision-robust than interpolating through a low joint-space IK
         153 +            # path. It works for both target-sized and small obstruction blocks.
         154 +            u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
         155 +            self.anchor_q = np.array((0, .25+.2*u, -np.pi, -2.30+.2*u,
         156 +                                      0, -.47+.2*u, np.pi/2))
         157 +            self.anchor_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
         158 +            self.anchor_by = self.pick_xyz[1]
         159 +            self.goal_q = _HOME.copy()
         160 +            self.phase, self.phase_steps = "target_home", 0
  164    161  
  165    162          if self.phase == "prepick_base":
  166    163              bxerr, byerr = self.pick_bx-self.base_x, self.pick_by-self.base_y
@@ -230,14 +227,10 @@ class GeneratedApproach:
  230    227                  self.pick_xyz = self._xyz(state, self.object)
  231    228                  if self.object.startswith("obstruction"):
  232    229                      self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
  233        -                if self.object == "target_block":
  234        -                    self.goal_q = _HOME.copy()
  235        -                    self.phase, self.phase_steps = "target_home", 0
  236        -                else:
  237        -                    # In a dense cluster, try a neighbor first; removing either
  238        -                    # one often makes the original vertical grasp collision-free.
         230 +                if self.object != "target_block":
  239    231                      self.deferred.add(self.object)
  240        -                    self.phase, self.phase_steps = "retract", 0
         232 +                self.goal_q = _HOME.copy()
         233 +                self.phase, self.phase_steps = "target_home", 0
  241    234                  return self._act_to(q, self.goal_q, 1.0)
  242    235              else:
  243    236                  return self._act_to(q, q, -1.0)
```

</details>

<a id="C042"></a>
### C042 · Add pinned-count stress validation runner

Commit `9fa169b0da75bc9c3f2bc03f90f353fe07c8c438`; parents: db6fc0322dc8496412aec20c6a61941565674caf. Recorded author date: 2026-09-09T15:55:07+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C042_9fa169b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/validate_pinned.py b/validate_pinned.py
new file mode 100644
index 0000000..7120bd2
--- /dev/null
+++ b/validate_pinned.py
@@ -0,0 +1,44 @@
           1 +"""Run one pinned obstruction-count case; intended for parallel shell use."""
           2 +import argparse
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +p = argparse.ArgumentParser()
           7 +p.add_argument("seed", type=int)
           8 +p.add_argument("count", type=int)
           9 +p.add_argument("--limit", type=int, default=800)
          10 +a = p.parse_args()
          11 +
          12 +env = make_env()
          13 +state, info = env.reset(seed=a.seed, options={"object_count": a.count})
          14 +policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
          15 +policy.reset(state, info)
          16 +last_phase = getattr(policy, "phase", None)
          17 +changes = []
          18 +for step in range(a.limit):
          19 +    state, reward, terminated, truncated, info = env.step(policy.get_action(state))
          20 +    phase = getattr(policy, "phase", None)
          21 +    if phase != last_phase:
          22 +        changes.append((step + 1, last_phase, phase, getattr(policy, "object", None)))
          23 +        last_phase = phase
          24 +    if terminated or truncated:
          25 +        break
          26 +held = None
          27 +for name in state.get_object_names():
          28 +    if name == "robot":
          29 +        continue
          30 +    try:
          31 +        if float(state.get(state.get_object_from_name(name), "grasp_active")) > .5:
          32 +            held = name
          33 +    except Exception:
          34 +        pass
          35 +def pos(name):
          36 +    o = state.get_object_from_name(name)
          37 +    return tuple(round(float(state.get(o, "pose_" + c)), 4) for c in "xyz")
          38 +print({"seed": a.seed, "count": a.count, "steps": step + 1,
          39 +       "terminated": terminated, "truncated": truncated,
          40 +       "phase": getattr(policy, "phase", None), "phase_steps": getattr(policy, "phase_steps", None),
          41 +       "object": getattr(policy, "object", None), "held": held,
          42 +       "target": pos("target_block"), "region": pos("target_region"),
          43 +       "transitions": changes[-15:]})
          44 +env.close()
```

</details>

<a id="C043"></a>
### C043 · Separate safe base translation from grasp posture motion

Commit `7e72b0a8105213aea17d7fd5ec26f3a50ab7d050`; parents: 9fa169b0da75bc9c3f2bc03f90f353fe07c8c438. Recorded author date: 2026-09-09T16:00:28+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0169](01_timeline.md#E0169): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C043_7e72b0a_approach.py) · [Exact all-file diff](evidence/diffs/C043_7e72b0a.diff)

[Previous saved controller snapshot](evidence/versions/C041_db6fc03_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0fcc1bc..9379956 100644
--- a/approach.py
+++ b/approach.py
@@ -179,11 +179,17 @@ class GeneratedApproach:
  179    179  
  180    180          if self.phase == "target_anchor":
  181    181              bxerr, byerr = self.anchor_bx-self.base_x, self.anchor_by-self.base_y
  182        -            if np.max(np.abs(self.goal_q-q)) < .012 and max(abs(bxerr),abs(byerr)) < .005:
         182 +            base_error = max(abs(bxerr), abs(byerr))
         183 +            if np.max(np.abs(self.goal_q-q)) < .012 and base_error < .005:
  183    184                  self.phase, self.phase_steps = "close", 0
         185 +            elif base_error >= .005:
         186 +                # Translate with the arm fully retracted. Combining these with
         187 +                # low-arm joint deltas can make collision rejection atomic.
         188 +                action = self._act_to(q, q, 1.0)
         189 +                action[0], action[1] = np.clip(bxerr, -.2, .2), np.clip(byerr, -.2, .2)
         190 +                return action
  184    191              else:
  185    192                  action = self._act_to(q, self.goal_q, 1.0)
  186        -                action[0], action[1] = np.clip(bxerr, -.2, .2), np.clip(byerr, -.2, .2)
  187    193                  return action
  188    194  
  189    195          if self.phase == "choose":
diff --git a/validate_30_0.out b/validate_30_0.out
new file mode 100644
index 0000000..41fe3fe
--- /dev/null
+++ b/validate_30_0.out
@@ -0,0 +1 @@
           1 +{'seed': 30, 'count': 0, 'steps': 21, 'terminated': True, 'truncated': False, 'phase': 'release', 'phase_steps': 0, 'object': 'target_block', 'held': None, 'target': (0.332, 0.2076, 0.113), 'region': (0.332, 0.2076, 0.08), 'transitions': [(1, 'choose', 'target_anchor', 'target_block'), (4, 'target_anchor', 'close', 'target_block'), (5, 'close', 'lift', 'target_block'), (8, 'lift', 'base_transfer', 'target_block'), (11, 'base_transfer', 'transfer', 'target_block'), (15, 'transfer', 'lower', 'target_block'), (21, 'lower', 'release', 'target_block')]}
diff --git a/validate_31_1.out b/validate_31_1.out
new file mode 100644
index 0000000..ad88c34
--- /dev/null
+++ b/validate_31_1.out
@@ -0,0 +1 @@
           1 +{'seed': 31, 'count': 1, 'steps': 51, 'terminated': True, 'truncated': False, 'phase': 'release', 'phase_steps': 0, 'object': 'target_block', 'held': None, 'target': (0.2916, 0.1341, 0.113), 'region': (0.2916, 0.1341, 0.08), 'transitions': [(5, 'close', 'lift', 'obstruction0'), (8, 'lift', 'base_transfer', 'obstruction0'), (11, 'base_transfer', 'transfer', 'obstruction0'), (14, 'transfer', 'lower', 'obstruction0'), (20, 'lower', 'release', 'obstruction0'), (22, 'release', 'retract', 'obstruction0'), (28, 'retract', 'home', 'obstruction0'), (31, 'home', 'choose', 'obstruction0'), (32, 'choose', 'target_anchor', 'target_block'), (35, 'target_anchor', 'close', 'target_block'), (36, 'close', 'lift', 'target_block'), (39, 'lift', 'base_transfer', 'target_block'), (41, 'base_transfer', 'transfer', 'target_block'), (45, 'transfer', 'lower', 'target_block'), (51, 'lower', 'release', 'target_block')]}
diff --git a/validate_32_3.out b/validate_32_3.out
new file mode 100644
index 0000000..f967291
--- /dev/null
+++ b/validate_32_3.out
@@ -0,0 +1 @@
           1 +{'seed': 32, 'count': 3, 'steps': 800, 'terminated': False, 'truncated': False, 'phase': 'target_anchor', 'phase_steps': 0, 'object': 'obstruction0', 'held': None, 'target': (0.4682, 0.1269, 0.1), 'region': (0.238, 0.1354, 0.08), 'transitions': [(743, 'target_anchor', 'close', 'obstruction0'), (749, 'close', 'target_home', 'obstruction0'), (752, 'target_home', 'target_anchor', 'obstruction0'), (755, 'target_anchor', 'close', 'obstruction0'), (761, 'close', 'target_home', 'obstruction0'), (764, 'target_home', 'target_anchor', 'obstruction0'), (767, 'target_anchor', 'close', 'obstruction0'), (773, 'close', 'target_home', 'obstruction0'), (776, 'target_home', 'target_anchor', 'obstruction0'), (779, 'target_anchor', 'close', 'obstruction0'), (785, 'close', 'target_home', 'obstruction0'), (788, 'target_home', 'target_anchor', 'obstruction0'), (791, 'target_anchor', 'close', 'obstruction0'), (797, 'close', 'target_home', 'obstruction0'), (800, 'target_home', 'target_anchor', 'obstruction0')]}
diff --git a/validate_33_5.out b/validate_33_5.out
new file mode 100644
index 0000000..3bc9da0
--- /dev/null
+++ b/validate_33_5.out
@@ -0,0 +1 @@
           1 +{'seed': 33, 'count': 5, 'steps': 800, 'terminated': False, 'truncated': False, 'phase': 'close', 'phase_steps': 4, 'object': 'obstruction2', 'held': None, 'target': (0.3889, 0.0319, 0.1), 'region': (0.2181, 0.0644, 0.08), 'transitions': [(742, 'close', 'target_home', 'obstruction2'), (745, 'target_home', 'target_anchor', 'obstruction2'), (748, 'target_anchor', 'close', 'obstruction2'), (754, 'close', 'target_home', 'obstruction2'), (757, 'target_home', 'target_anchor', 'obstruction2'), (760, 'target_anchor', 'close', 'obstruction2'), (766, 'close', 'target_home', 'obstruction2'), (769, 'target_home', 'target_anchor', 'obstruction2'), (772, 'target_anchor', 'close', 'obstruction2'), (778, 'close', 'target_home', 'obstruction2'), (781, 'target_home', 'target_anchor', 'obstruction2'), (784, 'target_anchor', 'close', 'obstruction2'), (790, 'close', 'target_home', 'obstruction2'), (793, 'target_home', 'target_anchor', 'obstruction2'), (796, 'target_anchor', 'close', 'obstruction2')]}
```

</details>

<a id="C044"></a>
### C044 · Lift crowded blocks with collision-safe increments

Commit `bcaa08b06a61d688afc26c9a073d4b10df8c2f64`; parents: 7e72b0a8105213aea17d7fd5ec26f3a50ab7d050. Recorded author date: 2026-09-09T16:01:58+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0177](01_timeline.md#E0177): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C044_bcaa08b_approach.py) · [Exact all-file diff](evidence/diffs/C044_bcaa08b.diff)

[Previous saved controller snapshot](evidence/versions/C043_7e72b0a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9379956..7f9de6b 100644
--- a/approach.py
+++ b/approach.py
@@ -244,17 +244,17 @@ class GeneratedApproach:
  244    244          if self.phase == "lift":
  245    245              # At table height a simultaneous Cartesian move may be rejected by
  246    246              # collision checking. Joint 4 positive is a reliable vertical escape.
  247        -            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 4:
         247 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 10:
  248    248                  action = self._act_to(q, q)
  249        -                action[4] = -.12
         249 +                action[4] = -.05
  250    250                  return action
  251        -            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 9:
         251 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 18:
  252    252                  action = self._act_to(q, q)
  253        -                action[6] = .10
         253 +                action[6] = .04
  254    254                  return action
  255        -            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 15:
         255 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 25:
  256    256                  action = self._act_to(q, q)
  257        -                action[4], action[6] = -.06, .06
         257 +                action[4], action[6] = -.03, .03
  258    258                  return action
  259    259              if self._xyz(state, held)[2] < self.lift_start_z + .06:
  260    260                  self.deferred.add(self.object)
diff --git a/validate_30_0.out b/validate_30_0.out
deleted file mode 100644
index 41fe3fe..0000000
--- a/validate_30_0.out
+++ /dev/null
@@ -1 +0,0 @@
    1        -{'seed': 30, 'count': 0, 'steps': 21, 'terminated': True, 'truncated': False, 'phase': 'release', 'phase_steps': 0, 'object': 'target_block', 'held': None, 'target': (0.332, 0.2076, 0.113), 'region': (0.332, 0.2076, 0.08), 'transitions': [(1, 'choose', 'target_anchor', 'target_block'), (4, 'target_anchor', 'close', 'target_block'), (5, 'close', 'lift', 'target_block'), (8, 'lift', 'base_transfer', 'target_block'), (11, 'base_transfer', 'transfer', 'target_block'), (15, 'transfer', 'lower', 'target_block'), (21, 'lower', 'release', 'target_block')]}
diff --git a/validate_31_1.out b/validate_31_1.out
deleted file mode 100644
index ad88c34..0000000
--- a/validate_31_1.out
+++ /dev/null
@@ -1 +0,0 @@
    1        -{'seed': 31, 'count': 1, 'steps': 51, 'terminated': True, 'truncated': False, 'phase': 'release', 'phase_steps': 0, 'object': 'target_block', 'held': None, 'target': (0.2916, 0.1341, 0.113), 'region': (0.2916, 0.1341, 0.08), 'transitions': [(5, 'close', 'lift', 'obstruction0'), (8, 'lift', 'base_transfer', 'obstruction0'), (11, 'base_transfer', 'transfer', 'obstruction0'), (14, 'transfer', 'lower', 'obstruction0'), (20, 'lower', 'release', 'obstruction0'), (22, 'release', 'retract', 'obstruction0'), (28, 'retract', 'home', 'obstruction0'), (31, 'home', 'choose', 'obstruction0'), (32, 'choose', 'target_anchor', 'target_block'), (35, 'target_anchor', 'close', 'target_block'), (36, 'close', 'lift', 'target_block'), (39, 'lift', 'base_transfer', 'target_block'), (41, 'base_transfer', 'transfer', 'target_block'), (45, 'transfer', 'lower', 'target_block'), (51, 'lower', 'release', 'target_block')]}
diff --git a/validate_32_3.out b/validate_32_3.out
deleted file mode 100644
index f967291..0000000
--- a/validate_32_3.out
+++ /dev/null
@@ -1 +0,0 @@
    1        -{'seed': 32, 'count': 3, 'steps': 800, 'terminated': False, 'truncated': False, 'phase': 'target_anchor', 'phase_steps': 0, 'object': 'obstruction0', 'held': None, 'target': (0.4682, 0.1269, 0.1), 'region': (0.238, 0.1354, 0.08), 'transitions': [(743, 'target_anchor', 'close', 'obstruction0'), (749, 'close', 'target_home', 'obstruction0'), (752, 'target_home', 'target_anchor', 'obstruction0'), (755, 'target_anchor', 'close', 'obstruction0'), (761, 'close', 'target_home', 'obstruction0'), (764, 'target_home', 'target_anchor', 'obstruction0'), (767, 'target_anchor', 'close', 'obstruction0'), (773, 'close', 'target_home', 'obstruction0'), (776, 'target_home', 'target_anchor', 'obstruction0'), (779, 'target_anchor', 'close', 'obstruction0'), (785, 'close', 'target_home', 'obstruction0'), (788, 'target_home', 'target_anchor', 'obstruction0'), (791, 'target_anchor', 'close', 'obstruction0'), (797, 'close', 'target_home', 'obstruction0'), (800, 'target_home', 'target_anchor', 'obstruction0')]}
diff --git a/validate_33_5.out b/validate_33_5.out
deleted file mode 100644
index 3bc9da0..0000000
--- a/validate_33_5.out
+++ /dev/null
@@ -1 +0,0 @@
    1        -{'seed': 33, 'count': 5, 'steps': 800, 'terminated': False, 'truncated': False, 'phase': 'close', 'phase_steps': 4, 'object': 'obstruction2', 'held': None, 'target': (0.3889, 0.0319, 0.1), 'region': (0.2181, 0.0644, 0.08), 'transitions': [(742, 'close', 'target_home', 'obstruction2'), (745, 'target_home', 'target_anchor', 'obstruction2'), (748, 'target_anchor', 'close', 'obstruction2'), (754, 'close', 'target_home', 'obstruction2'), (757, 'target_home', 'target_anchor', 'obstruction2'), (760, 'target_anchor', 'close', 'obstruction2'), (766, 'close', 'target_home', 'obstruction2'), (769, 'target_home', 'target_anchor', 'obstruction2'), (772, 'target_anchor', 'close', 'obstruction2'), (778, 'close', 'target_home', 'obstruction2'), (781, 'target_home', 'target_anchor', 'obstruction2'), (784, 'target_anchor', 'close', 'obstruction2'), (790, 'close', 'target_home', 'obstruction2'), (793, 'target_home', 'target_anchor', 'obstruction2'), (796, 'target_anchor', 'close', 'obstruction2')]}
```

</details>

<a id="C045"></a>
### C045 · Sidestep dense neighbors while lifting obstructions

Commit `febba60ecca9c79d420641ba86e09c2e16f30e31`; parents: bcaa08b06a61d688afc26c9a073d4b10df8c2f64. Recorded author date: 2026-09-09T16:02:54+02:00.

File roles (automatic): policy.

- [E0183](01_timeline.md#E0183): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C045_febba60_approach.py) · [Exact all-file diff](evidence/diffs/C045_febba60.diff)

[Previous saved controller snapshot](evidence/versions/C044_bcaa08b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7f9de6b..92b2e69 100644
--- a/approach.py
+++ b/approach.py
@@ -244,15 +244,20 @@ class GeneratedApproach:
  244    244          if self.phase == "lift":
  245    245              # At table height a simultaneous Cartesian move may be rejected by
  246    246              # collision checking. Joint 4 positive is a reliable vertical escape.
  247        -            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 10:
         247 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 14:
  248    248                  action = self._act_to(q, q)
  249        -                action[4] = -.05
         249 +                if self.phase_steps % 2 == 0:
         250 +                    action[4] = -.05
         251 +                else:
         252 +                    region_y = self._xyz(state, "target_region")[1]
         253 +                    away = np.sign(self._xyz(state, held)[1] - region_y)
         254 +                    action[5] = -.04 * (away if away != 0 else 1)
  250    255                  return action
  251        -            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 18:
         256 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 22:
  252    257                  action = self._act_to(q, q)
  253    258                  action[6] = .04
  254    259                  return action
  255        -            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 25:
         260 +            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 29:
  256    261                  action = self._act_to(q, q)
  257    262                  action[4], action[6] = -.03, .03
  258    263                  return action
```

</details>

<a id="C046"></a>
### C046 · Adapt grasp height and rotate through blocked candidates

Commit `d0c15d2f29448bca8bd90d9e43217642a304e1f3`; parents: febba60ecca9c79d420641ba86e09c2e16f30e31. Recorded author date: 2026-09-09T16:07:49+02:00.

File roles (automatic): policy.

- [E0197](01_timeline.md#E0197): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C046_d0c15d2_approach.py) · [Exact all-file diff](evidence/diffs/C046_d0c15d2.diff)

[Previous saved controller snapshot](evidence/versions/C045_febba60_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 92b2e69..73169d5 100644
--- a/approach.py
+++ b/approach.py
@@ -152,9 +152,14 @@ class GeneratedApproach:
  152    152              # collision-robust than interpolating through a low joint-space IK
  153    153              # path. It works for both target-sized and small obstruction blocks.
  154    154              u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
         155 +            center_z = self._xyz(state, self.object)[2]
         156 +            height_q = (.1-center_z)/.3445
  155    157              self.anchor_q = np.array((0, .25+.2*u, -np.pi, -2.30+.2*u,
  156    158                                        0, -.47+.2*u, np.pi/2))
         159 +            self.anchor_q[1] += height_q
  157    160              self.anchor_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
         161 +            if self.pick_xyz[0] <= .3359817:
         162 +                self.anchor_bx += .1625*height_q
  158    163              self.anchor_by = self.pick_xyz[1]
  159    164              self.goal_q = _HOME.copy()
  160    165              self.phase, self.phase_steps = "target_home", 0
@@ -235,8 +240,10 @@ class GeneratedApproach:
  235    240                      self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
  236    241                  if self.object != "target_block":
  237    242                      self.deferred.add(self.object)
  238        -                self.goal_q = _HOME.copy()
  239        -                self.phase, self.phase_steps = "target_home", 0
         243 +                    self.phase, self.phase_steps = "retract", 0
         244 +                else:
         245 +                    self.goal_q = _HOME.copy()
         246 +                    self.phase, self.phase_steps = "target_home", 0
  240    247                  return self._act_to(q, self.goal_q, 1.0)
  241    248              else:
  242    249                  return self._act_to(q, q, -1.0)
```

</details>

<a id="C047"></a>
### C047 · Recover from collision-stalled grasp postures

Commit `3aadb3bad5b52211406b5b45f317fb6977582d33`; parents: d0c15d2f29448bca8bd90d9e43217642a304e1f3. Recorded author date: 2026-09-09T16:11:51+02:00.

File roles (automatic): policy.

- [E0207](01_timeline.md#E0207): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C047_3aadb3b_approach.py) · [Exact all-file diff](evidence/diffs/C047_3aadb3b.diff)

[Previous saved controller snapshot](evidence/versions/C046_d0c15d2_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 73169d5..91328d9 100644
--- a/approach.py
+++ b/approach.py
@@ -185,6 +185,16 @@ class GeneratedApproach:
  185    185          if self.phase == "target_anchor":
  186    186              bxerr, byerr = self.anchor_bx-self.base_x, self.anchor_by-self.base_y
  187    187              base_error = max(abs(bxerr), abs(byerr))
         188 +            if self.phase_steps > 20:
         189 +                if self.object.startswith("obstruction"):
         190 +                    self.deferred.add(self.object)
         191 +                    self.phase, self.phase_steps = "retract", 0
         192 +                    return self._act_to(q, q, 1.0)
         193 +                self.carry_rotation = None
         194 +                self.pick_xyz = self._xyz(state, self.object)
         195 +                self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
         196 +                self.phase, self.phase_steps = "prepick", 0
         197 +                return self._act_to(q, self.goal_q, 1.0)
  188    198              if np.max(np.abs(self.goal_q-q)) < .012 and base_error < .005:
  189    199                  self.phase, self.phase_steps = "close", 0
  190    200              elif base_error >= .005:
```

</details>

<a id="C048"></a>
### C048 · Distribute parked obstructions across both table ends

Commit `8482e501a27290a25cfd75b0886fde251eb510fe`; parents: 3aadb3bad5b52211406b5b45f317fb6977582d33. Recorded author date: 2026-09-09T16:13:34+02:00.

File roles (automatic): policy.

- [E0215](01_timeline.md#E0215): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C048_8482e50_approach.py) · [Exact all-file diff](evidence/diffs/C048_8482e50.diff)

[Previous saved controller snapshot](evidence/versions/C047_3aadb3b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 91328d9..6cd3f38 100644
--- a/approach.py
+++ b/approach.py
@@ -93,8 +93,10 @@ class GeneratedApproach:
   93     93              if self.object not in self.park_spots:
   94     94                  i = len(self.park_spots)
   95     95                  side = -.34 if ry >= 0 else .34
          96 +                if i % 2:
          97 +                    side = -side
   96     98                  px = .13 + .12*(i % 4)
   97        -                py = side - np.sign(side)*.07*(i // 4)
          99 +                py = side - np.sign(side)*.07*(i // 8)
   98    100                  self.park_spots[self.object] = (px, py)
   99    101              px, py = self.park_spots[self.object]
  100    102              self.destination = np.array((px, py, .078 + self._get(state, self.object, "half_extent_z")))
```

</details>

<a id="C049"></a>
### C049 · Use arm-reachable obstruction parking columns

Commit `b782c302a1ffe6f854ca3781bb5b99265491da24`; parents: 8482e501a27290a25cfd75b0886fde251eb510fe. Recorded author date: 2026-09-09T16:14:15+02:00.

File roles (automatic): policy.

- [E0221](01_timeline.md#E0221): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C049_b782c30_approach.py) · [Exact all-file diff](evidence/diffs/C049_b782c30.diff)

[Previous saved controller snapshot](evidence/versions/C048_8482e50_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6cd3f38..f8e968d 100644
--- a/approach.py
+++ b/approach.py
@@ -95,7 +95,9 @@ class GeneratedApproach:
   95     95                  side = -.34 if ry >= 0 else .34
   96     96                  if i % 2:
   97     97                      side = -side
   98        -                px = .13 + .12*(i % 4)
          98 +                # Mid/far-x parking is reachable with a near-vertical arm; the
          99 +                # near-left corner can force the wrist through the tabletop.
         100 +                px = (.25, .25, .40, .40, .13, .13)[i % 6]
   99    101                  py = side - np.sign(side)*.07*(i // 8)
  100    102                  self.park_spots[self.object] = (px, py)
  101    103              px, py = self.park_spots[self.object]
```

</details>

<a id="C050"></a>
### C050 · Fallback to IK for size-sensitive obstruction grasps

Commit `0765ea91ddc3c3538ac0e4de39dbdd78d1808a6f`; parents: b782c302a1ffe6f854ca3781bb5b99265491da24. Recorded author date: 2026-09-09T16:19:14+02:00.

File roles (automatic): policy.

- [E0239](01_timeline.md#E0239): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C050_0765ea9_approach.py) · [Exact all-file diff](evidence/diffs/C050_0765ea9.diff)

[Previous saved controller snapshot](evidence/versions/C049_b782c30_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f8e968d..c04e3a5 100644
--- a/approach.py
+++ b/approach.py
@@ -131,6 +131,8 @@ class GeneratedApproach:
  131    131          self.park_count = 0
  132    132          self.park_spots = {}
  133    133          self.deferred = set()
         134 +        self.generic_objects = set()
         135 +        self.using_generic = False
  134    136          self.abandoning = False
  135    137          self.carry_rotation = None
  136    138          self.base_x = self._get(state, "robot", "pos_base_x")
@@ -148,6 +150,13 @@ class GeneratedApproach:
  148    150              self._choose_task(state)
  149    151              self.carry_rotation = None
  150    152              self.pick_xyz = self._xyz(state, self.object)
         153 +            self.using_generic = self.object in self.generic_objects
         154 +            if self.using_generic:
         155 +                self.generic_objects.discard(self.object)
         156 +                self.goal_q = _HOME.copy()
         157 +                self.pick_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
         158 +                self.pick_by = self.pick_xyz[1]
         159 +                self.phase, self.phase_steps = "prepick_base", 0
  151    160              if self.object.startswith("obstruction"):
  152    161                  # Pinch near the top: center-height grasps can put fingertips
  153    162                  # into the target plate or an immediately adjacent blocker.
@@ -155,7 +164,10 @@ class GeneratedApproach:
  155    164              # A calibrated vertical grasp pose plus base translation is more
  156    165              # collision-robust than interpolating through a low joint-space IK
  157    166              # path. It works for both target-sized and small obstruction blocks.
  158        -            u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
         167 +            if not self.using_generic:
         168 +                u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
         169 +            else:
         170 +                u = 0.0
  159    171              center_z = self._xyz(state, self.object)[2]
  160    172              height_q = (.1-center_z)/.3445
  161    173              self.anchor_q = np.array((0, .25+.2*u, -np.pi, -2.30+.2*u,
@@ -165,8 +177,9 @@ class GeneratedApproach:
  165    177              if self.pick_xyz[0] <= .3359817:
  166    178                  self.anchor_bx += .1625*height_q
  167    179              self.anchor_by = self.pick_xyz[1]
  168        -            self.goal_q = _HOME.copy()
  169        -            self.phase, self.phase_steps = "target_home", 0
         180 +            if not self.using_generic:
         181 +                self.goal_q = _HOME.copy()
         182 +                self.phase, self.phase_steps = "target_home", 0
  170    183  
  171    184          if self.phase == "prepick_base":
  172    185              bxerr, byerr = self.pick_bx-self.base_x, self.pick_by-self.base_y
@@ -253,7 +266,10 @@ class GeneratedApproach:
  253    266                  if self.object.startswith("obstruction"):
  254    267                      self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
  255    268                  if self.object != "target_block":
  256        -                    self.deferred.add(self.object)
         269 +                    if self.using_generic:
         270 +                        self.deferred.add(self.object)
         271 +                    else:
         272 +                        self.generic_objects.add(self.object)
  257    273                      self.phase, self.phase_steps = "retract", 0
  258    274                  else:
  259    275                      self.goal_q = _HOME.copy()
```

</details>

<a id="C051"></a>
### C051 · Center the fallback IK pinch on small blocks

Commit `da141eba1271fac60dc53a2d69a74115c280c3d6`; parents: 0765ea91ddc3c3538ac0e4de39dbdd78d1808a6f. Recorded author date: 2026-09-09T16:20:41+02:00.

File roles (automatic): policy.

- [E0245](01_timeline.md#E0245): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C051_da141eb_approach.py) · [Exact all-file diff](evidence/diffs/C051_da141eb.diff)

[Previous saved controller snapshot](evidence/versions/C050_0765ea9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c04e3a5..341a170 100644
--- a/approach.py
+++ b/approach.py
@@ -157,7 +157,7 @@ class GeneratedApproach:
  157    157                  self.pick_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
  158    158                  self.pick_by = self.pick_xyz[1]
  159    159                  self.phase, self.phase_steps = "prepick_base", 0
  160        -            if self.object.startswith("obstruction"):
         160 +            if self.object.startswith("obstruction") and not self.using_generic:
  161    161                  # Pinch near the top: center-height grasps can put fingertips
  162    162                  # into the target plate or an immediately adjacent blocker.
  163    163                  self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
```

</details>

<a id="C052"></a>
### C052 · Run IK fallback from calibrated pedestal origin

Commit `b81f1b88f3a003864a226b80221eb5ab9b9b5743`; parents: da141eba1271fac60dc53a2d69a74115c280c3d6. Recorded author date: 2026-09-09T16:21:29+02:00.

File roles (automatic): policy.

- [E0249](01_timeline.md#E0249): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C052_b81f1b8_approach.py) · [Exact all-file diff](evidence/diffs/C052_b81f1b8.diff)

[Previous saved controller snapshot](evidence/versions/C051_da141eb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 341a170..8ef43da 100644
--- a/approach.py
+++ b/approach.py
@@ -154,8 +154,8 @@ class GeneratedApproach:
  154    154              if self.using_generic:
  155    155                  self.generic_objects.discard(self.object)
  156    156                  self.goal_q = _HOME.copy()
  157        -                self.pick_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
  158        -                self.pick_by = self.pick_xyz[1]
         157 +                self.pick_bx = -.12
         158 +                self.pick_by = 0.0
  159    159                  self.phase, self.phase_steps = "prepick_base", 0
  160    160              if self.object.startswith("obstruction") and not self.using_generic:
  161    161                  # Pinch near the top: center-height grasps can put fingertips
```

</details>

<a id="C053"></a>
### C053 · Use stable obstruction order with deferred retries

Commit `5aaa70f6a2d6e54277d5605033cfcef42fe84f5e`; parents: b81f1b88f3a003864a226b80221eb5ab9b9b5743. Recorded author date: 2026-09-09T16:22:57+02:00.

File roles (automatic): policy.

- [E0255](01_timeline.md#E0255): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C053_5aaa70f_approach.py) · [Exact all-file diff](evidence/diffs/C053_5aaa70f.diff)

[Previous saved controller snapshot](evidence/versions/C052_b81f1b8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8ef43da..25daa61 100644
--- a/approach.py
+++ b/approach.py
@@ -84,7 +84,7 @@ class GeneratedApproach:
   84     84  
   85     85      def _choose_task(self, state):
   86     86          blockers = sorted((n for n in state.get_object_names() if self._blocking(state, n)),
   87        -                          key=lambda n: (n in self.deferred, -self._xyz(state, n)[2]))
          87 +                          key=lambda n: (n in self.deferred, n))
   88     88          if blockers:
   89     89              self.object = blockers[0]
   90     90              # Use rows opposite the goal. Staggering x prevents a pile even
```

</details>

<a id="C054"></a>
### C054 · Route stalled calibrated grasps through IK fallback

Commit `040380111b9d22d55f8d897a3e44b41fa2eb0761`; parents: 5aaa70f6a2d6e54277d5605033cfcef42fe84f5e. Recorded author date: 2026-09-09T16:24:17+02:00.

File roles (automatic): policy.

- [E0261](01_timeline.md#E0261): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C054_0403801_approach.py) · [Exact all-file diff](evidence/diffs/C054_0403801.diff)

[Previous saved controller snapshot](evidence/versions/C053_5aaa70f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 25daa61..5ba7558 100644
--- a/approach.py
+++ b/approach.py
@@ -204,7 +204,7 @@ class GeneratedApproach:
  204    204              base_error = max(abs(bxerr), abs(byerr))
  205    205              if self.phase_steps > 20:
  206    206                  if self.object.startswith("obstruction"):
  207        -                    self.deferred.add(self.object)
         207 +                    self.generic_objects.add(self.object)
  208    208                      self.phase, self.phase_steps = "retract", 0
  209    209                      return self._act_to(q, q, 1.0)
  210    210                  self.carry_rotation = None
```

</details>

<a id="C055"></a>
### C055 · Keep all parking slots opposite the target region

Commit `0a0929bd08672e78d0dc386c36a6df12902d3375`; parents: 040380111b9d22d55f8d897a3e44b41fa2eb0761. Recorded author date: 2026-09-09T16:25:22+02:00.

File roles (automatic): policy.

- [E0267](01_timeline.md#E0267): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C055_0a0929b_approach.py) · [Exact all-file diff](evidence/diffs/C055_0a0929b.diff)

[Previous saved controller snapshot](evidence/versions/C054_0403801_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5ba7558..d72873a 100644
--- a/approach.py
+++ b/approach.py
@@ -93,12 +93,10 @@ class GeneratedApproach:
   93     93              if self.object not in self.park_spots:
   94     94                  i = len(self.park_spots)
   95     95                  side = -.34 if ry >= 0 else .34
   96        -                if i % 2:
   97        -                    side = -side
   98     96                  # Mid/far-x parking is reachable with a near-vertical arm; the
   99     97                  # near-left corner can force the wrist through the tabletop.
  100        -                px = (.25, .25, .40, .40, .13, .13)[i % 6]
  101        -                py = side - np.sign(side)*.07*(i // 8)
          98 +                px = (.25, .40, .13, .47)[i % 4]
          99 +                py = side - np.sign(side)*.07*(i // 4)
  102    100                  self.park_spots[self.object] = (px, py)
  103    101              px, py = self.park_spots[self.object]
  104    102              self.destination = np.array((px, py, .078 + self._get(state, self.object, "half_extent_z")))
```

</details>

