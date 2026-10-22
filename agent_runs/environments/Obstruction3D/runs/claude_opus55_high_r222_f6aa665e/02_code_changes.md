# Obstruction3D · claude-opus-5-5 · replicate 222: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `0dcc59c` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `96e9dc5` | Exploration: FK (Kinova Gen3 URDF), IK, probes; base at world origin; grasp works | dbg/approach.py, dbg/kin.py, grid_0.txt, grid_1.5708.txt, kin.py, m1.txt, m2.txt, m3.txt, probe0.py, probe1.py, probe_base_1.py, probe_base_10.py, probe_base_2.py, probe_base_3.py… | [E0221](01_timeline.md#E0221) |
| [C003](#C003) · `c071470` | First full approach: clear obstructions then place block | approach.py, probe_base_11.py, probe_base_12.py, probe_base_13.py, probe_base_fk.py, probe_place.py, probe_tab_ik.py, probe_tab_info.py, test_approach.py | [E0365](01_timeline.md#E0365) |
| [C004](#C004) · `1afb5b9` | joint limits fix, bigger cartesian step | approach.py, dbg_run.py, probe_base_14.py, probe_base_15.py, probe_base_16.py, probe_tab_desc.py, probe_tab_ref.py, probe_tab_run.sh, probe_tab_y0_s0.txt, probe_tab_y0_s0.txt.tmp,… | [E0451](01_timeline.md#E0451) |
| [C005](#C005) · `daa4226` | grasp height rule (fingertip &gt;= support+0.017), grasp verification and retry | approach.py, g9b.txt, ga.txt, gb.txt, gc.txt, probe_g9.py, probe_tab_ik2.py, probe_tab_ref.out, probe_tab_ref.py, probe_tab_ref2.out | [E0481](01_timeline.md#E0481) |
| [C006](#C006) · `da7468c` | wip | dbg2.py, oc_check.py, probe_basefk.py, res_40_240.txt, test_approach.py | [E0595](01_timeline.md#E0595) |
| [C007](#C007) · `1bb36b8` | Rewrite: base-aware IK, base repositioning, grasp candidates incl. diagonal, stall detection, held-object replanning | approach.py, dbg_run.py | [E0605](01_timeline.md#E0605) |
| [C008](#C008) · `36264e4` | tests: object_count option | res_a.txt, res_oc4.txt | [E0658](01_timeline.md#E0658) |
| [C009](#C009) · `2e2235a` | adaptive step scale on rejection; finer steps near objects | approach.py, dbg_run.py, probe_lift.py | [E0672](01_timeline.md#E0672) |
| [C010](#C010) · `308b062` | timing in tests | res_b.txt, res_oc6.txt, test_approach.py | [E0741](01_timeline.md#E0741) |
| [C011](#C011) · `d17592f` | Escape moves in cycling directions on generic rejection (fixes endless lift loop) | approach.py, d15.txt, res_oc8.txt | [E0786](01_timeline.md#E0786) |
| [C012](#C012) · `8e94aa7` | Exact-on-line stepping with joint-cap shrink, bigger steps, lower safe height, drop spots near path | approach.py, probe_succ.py, res_a.txt, res_oc3.txt, res_oc5.txt, res_oc8.txt, res_t.txt | [E0989](01_timeline.md#E0989) |
| [C013](#C013) · `2c03cfc` | Corridor-based safe height, drop retreat segment | approach.py, probe_dz.py, res_t.txt | [E1042](01_timeline.md#E1042) |
| [C014](#C014) · `f623846` | Base-assisted y travel when arm is extended (ASSIST_MINX=0.2) | approach.py, res_t.txt, res_t2.txt, res_t8.txt | [E1114](01_timeline.md#E1114) |
| [C015](#C015) · `d7ac6b8` | Joint-space travel when interpolated path clears local obstacles | approach.py, res_t.txt | [E1165](01_timeline.md#E1165) |
| [C016](#C016) · `b3f709d` | Per-call compute time guard | approach.py, res_t2.txt, res_t8.txt | [E1231](01_timeline.md#E1231) |
| [C017](#C017) · `fcd604e` | STEP_LOW 0.08 | approach.py, res_t.txt, res_t5.txt | [E1245](01_timeline.md#E1245) |
| [C018](#C018) · `f688947` | Travel via joint+base interpolation with base-translation/rotation candidates (mean 25.9 steps) | approach.py, dbg_steps.py, probe_rot.py, res_t.txt, tally.py | [E1329](01_timeline.md#E1329) |
| [C019](#C019) · `c698440` | Faster FK/IK (vectorized Jacobian, early exit) | approach.py, p.out, prof1.py, prof2.py, res_t.txt | [E1362](01_timeline.md#E1362) |
| [C020](#C020) · `a6b2537` | Lazy merge of travel+descend into one joint move | approach.py, probe_rej.py, res_base.txt, res_t.txt, res_t2.txt, res_t4.txt, res_t8.txt | [E1457](01_timeline.md#E1457), [E1459](01_timeline.md#E1459) |
| [C021](#C021) · `e0f7863` | Lower floor/safe clearances (mean ~24 steps default) | approach.py | [E1551](01_timeline.md#E1551) |
| [C022](#C022) · `9f44174` | Close gripper when grasp descent is blocked but fingers already straddle object | approach.py | [E1668](01_timeline.md#E1668) |
| [C023](#C023) · `3506b1e` | Add validation results and debug scripts | d104.txt, d112.txt, dev/approach.py, dev/dbg_run.py, dev/env_client.py, dev/env_spaces.json, dev/res_t.txt, dev/res_t5.txt, dev/tally.py, dev/test_approach.py, probe_f.py, res_f8.… | [E1705](01_timeline.md#E1705) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `0dcc59c0958dcb148036dd5564eae8daca38b2db`; parents: none (initial snapshot). Recorded author date: 2026-09-30T20:32:19+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_0dcc59c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/.claude/settings.json b/.claude/settings.json
new file mode 100644
index 0000000..8199f99
--- /dev/null
+++ b/.claude/settings.json
@@ -0,0 +1,15 @@
           1 +{
           2 +  "hooks": {
           3 +    "PreToolUse": [
           4 +      {
           5 +        "matcher": "Write|Edit",
           6 +        "hooks": [
           7 +          {
           8 +            "type": "command",
           9 +            "command": "python3 .claude/validate_sandbox.py"
          10 +          }
          11 +        ]
          12 +      }
          13 +    ]
          14 +  }
          15 +}
diff --git a/.claude/validate_sandbox.py b/.claude/validate_sandbox.py
new file mode 100644
index 0000000..2a5285b
--- /dev/null
+++ b/.claude/validate_sandbox.py
@@ -0,0 +1,31 @@
           1 +#!/usr/bin/env python3
           2 +import json
           3 +import os
           4 +import sys
           5 +
           6 +data = json.load(sys.stdin)
           7 +tool_name = data.get("tool_name", "")
           8 +tool_input = data.get("tool_input", {})
           9 +
          10 +if tool_name not in ("Write", "Edit"):
          11 +    sys.exit(0)
          12 +
          13 +file_path = tool_input.get("file_path", "")
          14 +if not file_path:
          15 +    sys.exit(0)
          16 +
          17 +sandbox = os.path.realpath(os.getcwd())
          18 +resolved = os.path.realpath(file_path)
          19 +
          20 +if resolved == sandbox or resolved.startswith(sandbox + os.sep):
          21 +    sys.exit(0)
          22 +
          23 +json.dump({
          24 +    "hookSpecificOutput": {
          25 +        "hookEventName": "PreToolUse",
          26 +        "permissionDecision": "deny",
          27 +        "permissionDecisionReason": (
          28 +            f"Blocked: {file_path} resolves outside the sandbox directory"
          29 +        ),
          30 +    }
          31 +}, sys.stdout)
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
diff --git a/CLAUDE.md b/CLAUDE.md
new file mode 100644
index 0000000..e0d707c
--- /dev/null
+++ b/CLAUDE.md
@@ -0,0 +1,7 @@
           1 +All files you create MUST use relative paths so they stay in the current working directory (/sandbox). Never write files using absolute paths.
           2 +
           3 +CONTEXT MANAGEMENT: your context window is limited and you MUST protect it aggressively: (1) Delegate ALL source code reading, exploration, and deep reasoning to subagents: have them return only concise summaries and actionable suggestions. (2) Never read large files directly; spawn a subagent to read and summarize them. (3) When running Bash commands, pipe output through `head` or `tail` to limit verbosity if possible. (4) Keep your thinking brief, do not write long reasoning traces. If you need to reason deeply about a design decision, delegate that to a subagent and have it return the conclusion. (5) Keep your main conversation focused on writing and testing code, not on reading source or reasoning at length.
           4 +
           5 +The Python interpreter is at /opt/robocode-strict/bin/python
           6 +Run test scripts with:
           7 +    /opt/robocode-strict/bin/python test_approach.py
diff --git a/env_client.py b/env_client.py
new file mode 100644
index 0000000..108c884
--- /dev/null
+++ b/env_client.py
@@ -0,0 +1,737 @@
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
          86 +        # Match relational_structs.Type's dataclass repr, including name quoting.
          87 +        # Policies must see the same strings during synthesis and evaluation.
          88 +        return f"Type(name={self.name!r})"
          89 +
          90 +
          91 +class _Object:
          92 +    """A local mirror of relational_structs.Object (name + type)."""
          93 +
          94 +    def __init__(self, name: str, typ: _Type) -> None:
          95 +        self.name = name
          96 +        self.type = typ
          97 +
          98 +    def is_instance(self, typ: _Type) -> bool:
          99 +        """True if this object's type is *typ* or a descendant of it."""
         100 +        return typ in self.type.get_ancestors()
         101 +
         102 +    def __eq__(self, other: Any) -> bool:
         103 +        return isinstance(other, _Object) and other.name == self.name
         104 +
         105 +    def __hash__(self) -> int:
         106 +        return hash(self.name)
         107 +
         108 +    def __repr__(self) -> str:
         109 +        return f"{self.name}:{self.type.name}"
         110 +
         111 +
         112 +class _ObjectCentricState:
         113 +    """A local mirror of relational_structs.ObjectCentricState.
         114 +
         115 +    Holds ``{Object: feature ndarray}`` as ``data`` plus ``{Type: [feature names]}`` as
         116 +    ``type_features`` (both public, matching the real state) and exposes the read/write
         117 +    API a program uses. Iteration yields the objects, sorted by name for determinism.
         118 +    """
         119 +
         120 +    def __init__(
         121 +        self,
         122 +        data: dict[_Object, np.ndarray],
         123 +        type_features: dict[_Type, list[str]],
         124 +    ) -> None:
         125 +        self.data = data
         126 +        self.type_features = type_features
         127 +
         128 +    def __iter__(self) -> Any:
         129 +        return iter(sorted(self.data, key=lambda o: o.name))
         130 +
         131 +    def get_object_names(self) -> set[str]:
         132 +        """The set of object names in this state."""
         133 +        return {o.name for o in self.data}
         134 +
         135 +    def get_object_from_name(self, name: str) -> _Object:
         136 +        """The object with the given name."""
         137 +        for obj in self.data:
         138 +            if obj.name == name:
         139 +                return obj
         140 +        raise ValueError(f"No object named {name!r}")
         141 +
         142 +    def get_objects(self, typ: _Type) -> list[_Object]:
         143 +        """Objects that are instances of *typ* (its subtypes included), by name."""
         144 +        return sorted(
         145 +            (o for o in self.data if o.is_instance(typ)), key=lambda o: o.name
         146 +        )
         147 +
         148 +    def _feature_index(self, obj: _Object, feature: str) -> int:
         149 +        return self.type_features[obj.type].index(feature)
         150 +
         151 +    def get(self, obj: _Object, feature: str) -> float:
         152 +        """Read a named feature of an object."""
         153 +        return float(self.data[obj][self._feature_index(obj, feature)])
         154 +
         155 +    def set(self, obj: _Object, feature: str, value: float) -> None:
         156 +        """Write a named feature of an object in place."""
         157 +        self.data[obj][self._feature_index(obj, feature)] = value
         158 +
         159 +    def vec(self, objects: Any) -> np.ndarray:
         160 +        """Concatenate the feature vectors of the given objects."""
         161 +        return (
         162 +            np.concatenate([self.data[o] for o in objects]) if objects else np.array([])
         163 +        )
         164 +
         165 +    def copy(self) -> "_ObjectCentricState":
         166 +        """A deep copy of this state."""
         167 +        return _ObjectCentricState(
         168 +            {o: arr.copy() for o, arr in self.data.items()},
         169 +            {t: list(f) for t, f in self.type_features.items()},
         170 +        )
         171 +
         172 +    def allclose(self, other: "_ObjectCentricState") -> bool:
         173 +        """True if *other* has the same objects with numerically-close features."""
         174 +        if self.get_object_names() != other.get_object_names():
         175 +            return False
         176 +        return all(
         177 +            np.allclose(self.data[o], other.data[other.get_object_from_name(o.name)])
         178 +            for o in self.data
         179 +        )
         180 +
         181 +
         182 +def _build_local_types(
         183 +    types_payload: list[dict[str, Any]],
         184 +) -> tuple[dict[str, _Type], dict[_Type, list[str]]]:
         185 +    """Rebuild local {name: _Type} and {_Type: [features]} (parents-first payload)."""
         186 +    type_by_name: dict[str, _Type] = {}
         187 +    type_features: dict[_Type, list[str]] = {}
         188 +    for entry in types_payload:
         189 +        parent = type_by_name[entry["parent"]] if entry["parent"] is not None else None
         190 +        typ = _Type(entry["name"], parent)
         191 +        type_by_name[entry["name"]] = typ
         192 +        type_features[typ] = list(entry["features"])
         193 +    return type_by_name, type_features
         194 +
         195 +
         196 +def _ocs_from_payload(payload: dict[str, Any]) -> _ObjectCentricState:
         197 +    """Reconstruct a local ObjectCentricState from a self-contained codec payload."""
         198 +    type_by_name, type_features = _build_local_types(payload["types"])
         199 +    data: dict[_Object, np.ndarray] = {}
         200 +    for entry in payload["objects"]:
         201 +        obj = _Object(entry["name"], type_by_name[entry["type"]])
         202 +        data[obj] = np.array(entry["features"], dtype=np.float32)
         203 +    return _ObjectCentricState(data, type_features)
         204 +
         205 +
         206 +def _ocs_to_payload(state: _ObjectCentricState) -> dict[str, Any]:
         207 +    """Encode a local ObjectCentricState back to the self-contained codec payload."""
         208 +
         209 +    def depth(t: _Type) -> int:
         210 +        n, p = 0, t.parent
         211 +        while p is not None:
         212 +            n, p = n + 1, p.parent
         213 +        return n
         214 +
         215 +    types = sorted(state.type_features, key=lambda t: (depth(t), t.name))
         216 +    return {
         217 +        "types": [
         218 +            {
         219 +                "name": t.name,
         220 +                "parent": t.parent.name if t.parent is not None else None,
         221 +                "features": list(state.type_features[t]),
         222 +            }
         223 +            for t in types
         224 +        ],
         225 +        "objects": [
         226 +            {
         227 +                "name": o.name,
         228 +                "type": o.type.name,
         229 +                "features": [float(v) for v in state.data[o]],
         230 +            }
         231 +            for o in sorted(state.data, key=lambda o: o.name)
         232 +        ],
         233 +    }
         234 +
         235 +
         236 +def _encode(obj: Any) -> Any:
         237 +    """Encode values as tagged JSON (mirrors robocode.utils.env_server)."""
         238 +    if isinstance(obj, _ObjectCentricState):
         239 +        return {_OCS_TAG: _ocs_to_payload(obj)}
         240 +    if isinstance(obj, np.generic):
         241 +        return obj.item()
         242 +    if isinstance(obj, np.ndarray):
         243 +        return {_NDARRAY_TAG: obj.tolist(), "dtype": str(obj.dtype)}
         244 +    if isinstance(obj, dict):
         245 +        return {key: _encode(value) for key, value in obj.items()}
         246 +    if isinstance(obj, (list, tuple)):
         247 +        return [_encode(value) for value in obj]
         248 +    return obj
         249 +
         250 +
         251 +def _decode(obj: Any) -> Any:
         252 +    """Decode tagged JSON (mirrors robocode.utils.env_server)."""
         253 +    if isinstance(obj, dict):
         254 +        if _OCS_TAG in obj:
         255 +            return _ocs_from_payload(obj[_OCS_TAG])
         256 +        if _NDARRAY_TAG in obj:
         257 +            return np.array(obj[_NDARRAY_TAG], dtype=np.dtype(obj["dtype"]))
         258 +        return {key: _decode(value) for key, value in obj.items()}
         259 +    if isinstance(obj, list):
         260 +        return [_decode(value) for value in obj]
         261 +    return obj
         262 +
         263 +
         264 +def _encode_ref(obj: Any) -> Any:
         265 +    """Encode args/targets for the remote-object proxy commands.
         266 +
         267 +    Same as ``_encode`` but ``_RemoteHandle`` objects serialize to their
         268 +    ``{"__handle__": id}`` token so the host resolves them from its registry.
         269 +    Used only by devectorize/vectorize/getattr/call requests.
         270 +    """
         271 +    if isinstance(obj, _RemoteHandle):
         272 +        return {_HANDLE_TAG: obj._handle_id}  # pylint: disable=protected-access
         273 +    if isinstance(obj, _ObjectCentricState):
         274 +        return {_OCS_TAG: _ocs_to_payload(obj)}
         275 +    if isinstance(obj, np.generic):
         276 +        return obj.item()
         277 +    if isinstance(obj, np.ndarray):
         278 +        return {_NDARRAY_TAG: obj.tolist(), "dtype": str(obj.dtype)}
         279 +    if isinstance(obj, dict):
         280 +        return {key: _encode_ref(value) for key, value in obj.items()}
         281 +    if isinstance(obj, (list, tuple)):
         282 +        return [_encode_ref(value) for value in obj]
         283 +    if isinstance(obj, (set, frozenset)):
         284 +        return {_SET_TAG: [_encode_ref(value) for value in obj]}
         285 +    return obj
         286 +
         287 +
         288 +class SpaceInfo:
         289 +    """Metadata for a Box space: shape, low, high, dtype, and sample()."""
         290 +
         291 +    def __init__(self, spec: dict[str, Any]) -> None:
         292 +        if spec["type"] != "Box":
         293 +            raise TypeError(
         294 +                f"Unsupported space type {spec['type']!r}; extend SpaceInfo "
         295 +                "alongside the server's serialize_space"
         296 +            )
         297 +        self.shape: tuple[int, ...] = tuple(spec["shape"])
         298 +        self.dtype: np.dtype[Any] = np.dtype(spec["dtype"])
         299 +        self.low: np.ndarray = np.array(spec["low"], dtype=self.dtype)
         300 +        self.high: np.ndarray = np.array(spec["high"], dtype=self.dtype)
         301 +
         302 +    def sample(self, rng: np.random.Generator | None = None) -> np.ndarray:
         303 +        """Sample uniformly between low and high."""
         304 +        if rng is None:
         305 +            rng = np.random.default_rng()
         306 +        return rng.uniform(self.low, self.high).astype(self.dtype)
         307 +
         308 +
         309 +class _RemoteHandle:
         310 +    """A reference to a host-side object, used over the env server.
         311 +
         312 +    Attribute access and calls are proxied to the host: ``handle.method(...)``
         313 +    issues a ``getattr`` (returning another handle for the bound method) then a
         314 +    ``call``. Returned values are decoded the same way as any response, so a
         315 +    scalar/ndarray comes back inline and another object comes back as a nested
         316 +    ``_RemoteHandle``. Private/dunder attributes are refused client-side, both
         317 +    to avoid surprise round-trips and to mirror the host security guard.
         318 +    """
         319 +
         320 +    def __init__(self, client: "BlackboxEnv", handle_id: str) -> None:
         321 +        # Use object.__setattr__-free plain assignment; __getattr__ only fires
         322 +        # for names not found normally, and these two are set here.
         323 +        self._client = client
         324 +        self._handle_id = handle_id
         325 +
         326 +    def __getattr__(self, name: str) -> Any:
         327 +        if name.startswith("_"):
         328 +            raise AttributeError(
         329 +                f"refusing private/dunder attribute access on remote handle: "
         330 +                f"{name!r}"
         331 +            )
         332 +        response = self._client._request(  # pylint: disable=protected-access
         333 +            {
         334 +                "cmd": "getattr",
         335 +                "target": {_HANDLE_TAG: self._handle_id},
         336 +                "name": name,
         337 +            }
         338 +        )
         339 +        return self._client._decode_ref(  # pylint: disable=protected-access
         340 +            response["result"]
         341 +        )
         342 +
         343 +    def __call__(self, *args: Any, **kwargs: Any) -> Any:
         344 +        response = self._client._request(  # pylint: disable=protected-access
         345 +            {
         346 +                "cmd": "call",
         347 +                "target": {_HANDLE_TAG: self._handle_id},
         348 +                "args": _encode_ref(list(args)),
         349 +                "kwargs": _encode_ref(kwargs),
         350 +            }
         351 +        )
         352 +        return self._client._decode_ref(  # pylint: disable=protected-access
         353 +            response["result"]
         354 +        )
         355 +
         356 +
         357 +class _RemoteModule:
         358 +    """A reference to a whitelisted host module (e.g. crv_motion_planning).
         359 +
         360 +    Attribute access proxies a ``getattr`` against the ``{"__module__": name}``
         361 +    target, so ``module.plan_crv_actions`` returns a callable handle the agent
         362 +    can invoke. Mirrors how a remote-module primitive is used at eval time,
         363 +    where ``primitives['crv_motion_planning']`` is the real module.
         364 +    """
         365 +
         366 +    def __init__(self, client: "BlackboxEnv", short_name: str) -> None:
         367 +        self._client = client
         368 +        self._short_name = short_name
         369 +
         370 +    def __getattr__(self, name: str) -> Any:
         371 +        if name.startswith("_"):
         372 +            raise AttributeError(
         373 +                f"refusing private/dunder attribute access on remote module: "
         374 +                f"{name!r}"
         375 +            )
         376 +        response = self._client._request(  # pylint: disable=protected-access
         377 +            {
         378 +                "cmd": "getattr",
         379 +                "target": {_MODULE_TAG: self._short_name},
         380 +                "name": name,
         381 +            }
         382 +        )
         383 +        return self._client._decode_ref(  # pylint: disable=protected-access
         384 +            response["result"]
         385 +        )
         386 +
         387 +
         388 +class _BlackboxObservationSpace(SpaceInfo):
         389 +    """Box-space metadata plus client-backed devectorize/vectorize.
         390 +
         391 +    Stands in for the eval-time ``ObjectCentricBoxSpace``: it keeps the
         392 +    shape/low/high/dtype/sample() of a plain ``SpaceInfo`` and adds
         393 +    ``devectorize(obs)`` / ``vectorize(ocs)`` that proxy to the host. The agent
         394 +    writes ``observation_space.devectorize(obs)`` exactly as it would at eval.
         395 +    """
         396 +
         397 +    def __init__(self, spec: dict[str, Any], client: "BlackboxEnv") -> None:
         398 +        super().__init__(spec)
         399 +        self._client = client
         400 +
         401 +    def devectorize(self, obs: Any) -> Any:
         402 +        """Return an object-centric view of *obs* as a remote handle."""
         403 +        return self._client.devectorize(obs)
         404 +
         405 +    def vectorize(self, state: Any) -> np.ndarray:
         406 +        """Return the flat observation vector for an object-centric state."""
         407 +        return self._client.vectorize(state)
         408 +
         409 +
         410 +class _ObjectCentricObservationSpace:
         411 +    """Client-side view of a variable-count env's ObjectCentricStateSpace.
         412 +
         413 +    The observation is already an object-centric state (reconstructed locally from the
         414 +    wire), so this space has no fixed shape/vector: it exposes the domain ``types`` and
         415 +    ``type_features`` the program needs to enumerate objects, matching the eval-time
         416 +    ``observation_space.types``. There is no ``devectorize`` -- the state is not a
         417 +    vector.
         418 +    """
         419 +
         420 +    def __init__(self, spec: dict[str, Any]) -> None:
         421 +        self._type_by_name, self._type_features = _build_local_types(spec["types"])
         422 +
         423 +    @property
         424 +    def types(self) -> set[_Type]:
         425 +        """The domain object types (matches the eval-time observation_space.types)."""
         426 +        return set(self._type_features)
         427 +
         428 +    @property
         429 +    def type_features(self) -> dict[_Type, list[str]]:
         430 +        """Feature names for each type."""
         431 +        return {t: list(f) for t, f in self._type_features.items()}
         432 +
         433 +    def get_type(self, name: str) -> _Type:
         434 +        """The domain type with the given name (e.g. ``"rectangle"``)."""
         435 +        return self._type_by_name[name]
         436 +
         437 +
         438 +class BlackboxEnv:
         439 +    """A live environment instance, accessed over the wire."""
         440 +
         441 +    def __init__(self, meta: dict[str, Any], sandbox_root: Any = None) -> None:
         442 +        obs_spec = meta["observation_space"]
         443 +        self._strict = bool(meta.get("strict", False))
         444 +        # A variable-count env sends object-centric states, reconstructed locally; a
         445 +        # fixed-count env sends Box vectors as before.
         446 +        self._object_centric = obs_spec.get("type") == "ObjectCentric"
         447 +        if self._object_centric:
         448 +            self.observation_space: Any = _ObjectCentricObservationSpace(obs_spec)
         449 +        elif self._strict:
         450 +            # Strict blackbox exposes only generic array metadata. In particular,
         451 +            # do not attach the host-backed devectorize/vectorize helpers that make
         452 +            # the legacy blackbox convenient but confound the isolation ablation.
         453 +            self.observation_space = SpaceInfo(obs_spec)
         454 +        else:
         455 +            self.observation_space = _BlackboxObservationSpace(obs_spec, self)
         456 +        self.action_space = SpaceInfo(meta["action_space"])
         457 +        self.max_steps: int | None = meta["max_steps"]
         458 +        # How make_primitives rebuilds the eval-time primitives dict (see
         459 +        # robocode.primitives.blackbox_primitive_manifest). Empty when the
         460 +        # run configures no primitives.
         461 +        self._primitive_manifest: list[dict[str, Any]] = meta.get("primitives", [])
         462 +        # Where render_policy looks for approach.py and make_primitives imports
         463 +        # generic primitive sources; the sandbox dir in real runs (set by
         464 +        # make_env), the current dir for ad-hoc construction.
         465 +        self._sandbox_root = (
         466 +            Path(sandbox_root) if sandbox_root is not None else Path.cwd()
         467 +        )
         468 +        self._token: str = meta["token"]
         469 +        self._sock = socket.create_connection((meta["host"], meta["port"]))
         470 +        self._file = self._sock.makefile("rwb")
         471 +
         472 +    def _request(self, payload: dict[str, Any]) -> dict[str, Any]:
         473 +        payload["token"] = self._token
         474 +        self._file.write(json.dumps(payload).encode("utf-8") + b"\n")
         475 +        self._file.flush()
         476 +        line = self._file.readline()
         477 +        if not line:
         478 +            raise RuntimeError("Connection to the environment server was closed")
         479 +        response = json.loads(line)
         480 +        if "error" in response:
         481 +            raise RuntimeError(f"Environment server error: {response['error']}")
         482 +        return _decode(response)
         483 +
         484 +    def _decode_ref(self, obj: Any) -> Any:
         485 +        """Decode a remote-command result, mapping handles to _RemoteHandle.
         486 +
         487 +        ``_request`` already ran ``_decode`` over the response (so ndarrays are
         488 +        arrays), but it leaves ``{"__handle__": id}`` dicts intact since it does
         489 +        not know the handle tag. Here we turn those into ``_RemoteHandle``
         490 +        objects and recurse through the remaining containers.
         491 +        """
         492 +        if isinstance(obj, dict):
         493 +            if _HANDLE_TAG in obj:
         494 +                return _RemoteHandle(self, obj[_HANDLE_TAG])
         495 +            if _SET_TAG in obj:
         496 +                return {self._decode_ref(value) for value in obj[_SET_TAG]}
         497 +            return {key: self._decode_ref(value) for key, value in obj.items()}
         498 +        if isinstance(obj, list):
         499 +            return [self._decode_ref(value) for value in obj]
         500 +        return obj
         501 +
         502 +    def devectorize(self, obs: Any) -> _RemoteHandle:
         503 +        """Return an object-centric view of *obs* (a remote ObjectCentricState).
         504 +
         505 +        Proxies ``observation_space.devectorize`` to the host. The returned
         506 +        handle exposes the public ObjectCentricState API (``get_object_names``,
         507 +        ``get_object_from_name``, ``get_objects``, ``get``, ``set``, ``copy``,
         508 +        ...) over the wire. Pass it straight to the CRV planners from
         509 +        ``make_primitives``.
         510 +        """
         511 +        response = self._request(
         512 +            {"cmd": "devectorize", "obs": _encode(np.asarray(obs))}
         513 +        )
         514 +        return self._decode_ref(response["result"])
         515 +
         516 +    def vectorize(self, state: Any) -> np.ndarray:
         517 +        """Return the flat observation vector for an object-centric state handle."""
         518 +        response = self._request({"cmd": "vectorize", "state": _encode_ref(state)})
         519 +        return self._decode_ref(response["result"])
         520 +
         521 +    def reset(
         522 +        self, seed: int | None = None, options: dict[str, Any] | None = None
         523 +    ) -> tuple[np.ndarray, dict[str, Any]]:
         524 +        """Reset the environment; returns (obs, info)."""
         525 +        response = self._request({"cmd": "reset", "seed": seed, "options": options})
         526 +        return response["obs"], response["info"]
         527 +
         528 +    def step(self, action: Any) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
         529 +        """Step the environment; returns (obs, reward, terminated, truncated, info)."""
         530 +        action = np.asarray(action, dtype=self.action_space.dtype)
         531 +        response = self._request({"cmd": "step", "action": _encode(action)})
         532 +        return (
         533 +            response["obs"],
         534 +            response["reward"],
         535 +            response["terminated"],
         536 +            response["truncated"],
         537 +            response["info"],
         538 +        )
         539 +
         540 +    def get_state(self) -> Any:
         541 +        """Return a snapshot of the full environment state.
         542 +
         543 +        A Box vector for a fixed-count env; a local ObjectCentricState for a
         544 +        variable-count env (reconstructed by ``_decode``).
         545 +        """
         546 +        return self._request({"cmd": "get_state"})["state"]
         547 +
         548 +    def _encode_state(self, state: Any) -> Any:
         549 +        """Encode a state for the wire: an object-centric state or a Box vector."""
         550 +        if isinstance(state, _ObjectCentricState):
         551 +            return _encode(state)
         552 +        return _encode(np.asarray(state))
         553 +
         554 +    def render_state(
         555 +        self,
         556 +        seed: int = 42,
         557 +        state: Any = None,
         558 +        label: str = "",
         559 +        object_count: int | None = None,
         560 +    ) -> str:
         561 +        """Render a state on the host; returns a PNG path inside the sandbox.
         562 +
         563 +        Either pass ``seed`` to render the initial state after a reset (with
         564 +        ``object_count`` to pin a variable-count env's object count), or ``state`` (a
         565 +        flat list of floats, as from ``get_state().tolist()``) to render an arbitrary
         566 +        state. The path is relative to the sandbox dir.
         567 +        """
         568 +        if isinstance(state, _ObjectCentricState):
         569 +            state = _encode(state)  # tagged object-centric payload, decoded host-side
         570 +        elif isinstance(state, np.ndarray):
         571 +            state = state.tolist()
         572 +        return self._request(
         573 +            {
         574 +                "cmd": "render_state",
         575 +                "seed": seed,
         576 +                "state": state,
         577 +                "label": label,
         578 +                "object_count": object_count,
         579 +            }
         580 +        )["path"]
         581 +
         582 +    def render_policy(
         583 +        self,
         584 +        seed: int = 42,
         585 +        max_steps: int = 1000,
         586 +        max_frames: int = 100,
         587 +        approach_path: Any = None,
         588 +        object_count: int | None = None,
         589 +    ) -> list[str]:
         590 +        """Run an episode of approach.py here and render the visited states.
         591 +
         592 +        The policy runs in this process: only ``get_action`` (which needs the
         593 +        observation alone) executes locally, while each visited state is
         594 +        rendered on the host via ``render_state``. No approach code runs on the
         595 +        host, so a black-box agent cannot reach the env source through rendering.
         596 +        ``object_count`` pins a variable-count env's object count on the rollout reset.
         597 +        Returns the PNG paths (relative to the sandbox dir).
         598 +        """
         599 +        path = (
         600 +            Path(approach_path)
         601 +            if approach_path is not None
         602 +            else self._sandbox_root / "approach.py"
         603 +        )
         604 +        approach = _load_generated_approach(
         605 +            path, self.action_space, self.observation_space, self.make_primitives()
         606 +        )
         607 +        options = {"object_count": object_count} if object_count is not None else None
         608 +        obs, info = self.reset(seed=seed, options=options)
         609 +        approach.reset(obs, info)
         610 +        # Strict mode deliberately withholds raw state snapshots. Its observations
         611 +        # are nevertheless renderable, so use them to visualize a policy without
         612 +        # opening the get_state channel to agent scripts.
         613 +        states = [obs if self._strict else self.get_state()]
         614 +        for _ in range(max_steps):
         615 +            obs, reward, terminated, truncated, info = self.step(
         616 +                approach.get_action(obs)
         617 +            )
         618 +            if hasattr(approach, "update"):
         619 +                approach.update(obs, reward, terminated or truncated, info)
         620 +            states.append(obs if self._strict else self.get_state())
         621 +            if terminated or truncated:
         622 +                break
         623 +        return [
         624 +            self.render_state(state=state, label=f"policy_seed{seed}_{i:04d}")
         625 +            for i, state in enumerate(states[:max_frames])
         626 +        ]
         627 +
         628 +    def set_state(self, state: Any) -> None:
         629 +        """Restore a state snapshot previously returned by get_state()."""
         630 +        self._request({"cmd": "set_state", "state": self._encode_state(state)})
         631 +
         632 +    def check_action_collision(self, state: Any, action: Any) -> bool:
         633 +        """Return True if taking *action* in *state* causes a collision.
         634 +
         635 +        Runs the env-dependent collision primitive on the host (the sandbox
         636 +        lacks the env source), against this connection's env. Mirrors the
         637 +        eval-time ``primitives['check_action_collision']`` callable, so test
         638 +        scripts that get it from ``make_primitives`` call it the same way.
         639 +        """
         640 +        response = self._request(
         641 +            {
         642 +                "cmd": "check_action_collision",
         643 +                "state": self._encode_state(state),
         644 +                "action": _encode(np.asarray(action, dtype=self.action_space.dtype)),
         645 +            }
         646 +        )
         647 +        return response["collision"]
         648 +
         649 +    def make_primitives(self) -> dict[str, Any]:
         650 +        """Build the eval-time primitives dict for this black-box env.
         651 +
         652 +        Black-box counterpart of ``robocode.primitives.build_primitives``:
         653 +        env-dependent primitives proxy to the host, while generic ones are
         654 +        imported from their copies under ``primitives/`` in the sandbox. Use
         655 +        it in test scripts so they exercise exactly the primitives the harness
         656 +        passes to ``GeneratedApproach`` at evaluation time::
         657 +
         658 +            from env_client import make_env
         659 +
         660 +            env = make_env()
         661 +            primitives = env.make_primitives()
         662 +        """
         663 +        sandbox_dir = str(self._sandbox_root.resolve())
         664 +        if sandbox_dir not in sys.path:
         665 +            sys.path.insert(0, sandbox_dir)
         666 +        primitives: dict[str, Any] = {}
         667 +        for spec in self._primitive_manifest:
         668 +            if spec["kind"] == "host_proxy":
         669 +                primitives[spec["name"]] = getattr(self, spec["name"])
         670 +            elif spec["kind"] == "remote_module":
         671 +                # The module source is withheld from the sandbox; reach it on
         672 +                # the host via a remote-module proxy (e.g. crv_motion_planning).
         673 +                primitives[spec["name"]] = _RemoteModule(self, spec["module"])
         674 +            else:
         675 +                module = importlib.import_module(f"primitives.{spec['module']}")
         676 +                primitives[spec["name"]] = (
         677 +                    module if spec["attr"] is None else getattr(module, spec["attr"])
         678 +                )
         679 +        return primitives
         680 +
         681 +    def close(self) -> None:
         682 +        """Close the connection (and the server-side environment)."""
         683 +        try:
         684 +            self._file.write(
         685 +                json.dumps({"cmd": "close", "token": self._token}).encode("utf-8")
         686 +                + b"\n"
         687 +            )
         688 +            self._file.flush()
         689 +        finally:
         690 +            # makefile() wraps a dup of the socket; close it too so the buffered
         691 +            # file object does not leak (ResourceWarning) when close() runs.
         692 +            self._file.close()
         693 +            self._sock.close()
         694 +
         695 +    def __enter__(self) -> "BlackboxEnv":
         696 +        return self
         697 +
         698 +    def __exit__(self, *exc_info: Any) -> None:
         699 +        self.close()
         700 +
         701 +
         702 +def _load_generated_approach(
         703 +    path: Path, action_space: Any, observation_space: Any, primitives: dict[str, Any]
         704 +) -> Any:
         705 +    """Exec ``approach.py`` and instantiate its ``GeneratedApproach``.
         706 +
         707 +    Mirrors ``robocode.utils.episode.load_generated_approach``; duplicated here
         708 +    (like the codec above) because this module must stay importable with only
         709 +    the standard library and numpy, since it is copied standalone into the
         710 +    sandbox. Used only by ``render_policy`` for visual debugging.
         711 +    """
         712 +    sandbox_dir = str(path.resolve().parent)
         713 +    added = sandbox_dir not in sys.path
         714 +    if added:
         715 +        sys.path.insert(0, sandbox_dir)
         716 +    try:
         717 +        namespace: dict[str, Any] = {"__file__": str(path)}
         718 +        exec(  # pylint: disable=exec-used
         719 +            compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace
         720 +        )
         721 +    finally:
         722 +        if added:
         723 +            sys.path.remove(sandbox_dir)
         724 +    return namespace["GeneratedApproach"](
         725 +        action_space, observation_space, primitives=primitives
         726 +    )
         727 +
         728 +
         729 +def make_env(metadata_path: Any = None) -> BlackboxEnv:
         730 +    """Connect to the environment server; returns a fresh env instance.
         731 +
         732 +    *metadata_path* defaults to ``env_spaces.json`` next to this module
         733 +    (the agent's sandbox copy); the MCP server passes an explicit path.
         734 +    """
         735 +    path = Path(metadata_path) if metadata_path is not None else _METADATA_PATH
         736 +    meta = json.loads(path.read_text(encoding="utf-8"))
         737 +    return BlackboxEnv(meta, sandbox_root=path.parent)
diff --git a/env_spaces.json b/env_spaces.json
new file mode 100644
index 0000000..1d4e8d4
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "a55f540c5f383484c0efbffe8d1ca4c1", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Exploration: FK (Kinova Gen3 URDF), IK, probes; base at world origin; grasp works

Commit `96e9dc5de2ad8aa774bfeaf251e0c73d04046bac`; parents: 0dcc59c0958dcb148036dd5564eae8daca38b2db. Recorded author date: 2026-09-30T20:43:30+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0221](01_timeline.md#E0221): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C002_96e9dc5.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/dbg/approach.py b/dbg/approach.py
new file mode 100644
index 0000000..7d7e6a2
--- /dev/null
+++ b/dbg/approach.py
@@ -0,0 +1,21 @@
           1 +import numpy as np
           2 +from kin import ik, down_R
           3 +class GeneratedApproach:
           4 +    def __init__(self, action_space, observation_space, primitives): pass
           5 +    def reset(self, state, info):
           6 +        self.t=0
           7 +        R=state.get_object_from_name("robot"); B=state.get_object_from_name("target_block")
           8 +        self.R=R
           9 +        q=np.array([state.get(R,f'joint_{i}') for i in range(1,8)])
          10 +        bx,by=state.get(B,'pose_x'),state.get(B,'pose_y')
          11 +        self.wps=[]
          12 +        for z in [0.4,0.33,0.255]:
          13 +            q,_=ik(q,np.array([bx,by,z]),down_R(0),(-0.12,0,0)); self.wps.append(q)
          14 +    def get_action(self, state):
          15 +        self.t+=1
          16 +        q=np.array([state.get(self.R,f'joint_{i}') for i in range(1,8)])
          17 +        a=np.zeros(11,np.float32)
          18 +        while self.wps and np.max(np.abs(self.wps[0]-q))<1e-4: self.wps.pop(0)
          19 +        if self.wps: a[3:10]=np.clip(self.wps[0]-q,-.2,.2)
          20 +        else: a[10]=-1
          21 +        return a
diff --git a/dbg/kin.py b/dbg/kin.py
new file mode 100644
index 0000000..19ed11b
--- /dev/null
+++ b/dbg/kin.py
@@ -0,0 +1,80 @@
           1 +import numpy as np
           2 +
           3 +def rpy_mat(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def tf(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = rpy_mat(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +def rotz(q):
          13 +    c, s = np.cos(q), np.sin(q)
          14 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          15 +
          16 +PI = np.pi
          17 +JOINTS = [
          18 +    tf([0, 0, 0.15643], [PI, 0, 0]),
          19 +    tf([0, 0.005375, -0.12838], [PI/2, 0, 0]),
          20 +    tf([0, -0.21038, -0.006375], [-PI/2, 0, 0]),
          21 +    tf([0, 0.006375, -0.21038], [PI/2, 0, 0]),
          22 +    tf([0, -0.20843, -0.006375], [-PI/2, 0, 0]),
          23 +    tf([0, 0.00017505, -0.10593], [PI/2, 0, 0]),
          24 +    tf([0, -0.10593, -0.00017505], [-PI/2, 0, 0]),
          25 +]
          26 +EE = tf([0, 0, -0.061525], [PI, 0, 0])
          27 +
          28 +def fk_all(q, base=(0, 0, 0), base_z=0.0, tool=0.0):
          29 +    T = np.eye(4)
          30 +    T[:3, :3] = rpy_mat(0, 0, base[2]); T[:3, 3] = [base[0], base[1], base_z]
          31 +    frames = [T.copy()]
          32 +    for i in range(7):
          33 +        T = T @ JOINTS[i] @ rotz(q[i])
          34 +        frames.append(T.copy())
          35 +    T = T @ EE
          36 +    frames.append(T.copy())
          37 +    Tt = T.copy(); Tt[:3, 3] = T[:3, 3] + T[:3, 2] * tool
          38 +    frames.append(Tt)
          39 +    return frames
          40 +
          41 +def ee_pose(q, base, base_z=0.0, tool=0.0):
          42 +    return fk_all(q, base, base_z, tool)[-1]
          43 +
          44 +def pose_err(T, pos, R):
          45 +    ep = pos - T[:3, 3]
          46 +    Re = R @ T[:3, :3].T
          47 +    # axis-angle of Re
          48 +    ang = np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]]) * 0.5
          49 +    return np.concatenate([ep, ang])
          50 +
          51 +def down_R(yaw):
          52 +    # z axis pointing down, x axis along yaw
          53 +    c, s = np.cos(yaw), np.sin(yaw)
          54 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          55 +    return np.stack([x, y, z], axis=1)
          56 +
          57 +def ik(q0, pos, R, base, base_z=0.0, tool=0.0, iters=200, wrot=0.3, tol=1e-4):
          58 +    q = np.array(q0, dtype=float)
          59 +    W = np.array([1, 1, 1, wrot, wrot, wrot])
          60 +    for it in range(iters):
          61 +        T = ee_pose(q, base, base_z, tool)
          62 +        e = pose_err(T, pos, R) * W
          63 +        if np.linalg.norm(e) < tol:
          64 +            break
          65 +        J = np.zeros((6, 7)); h = 1e-6
          66 +        for i in range(7):
          67 +            dq = q.copy(); dq[i] += h
          68 +            J[:, i] = (pose_err(ee_pose(dq, base, base_z, tool), pos, R) * W - e) / -h
          69 +        lam = 1e-3
          70 +        step = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
          71 +        n = np.linalg.norm(step)
          72 +        if n > 0.3: step *= 0.3 / n
          73 +        q += step
          74 +    return q, np.linalg.norm(e)
          75 +
          76 +from scipy.spatial.transform import Rotation as _Rot
          77 +def pose_err(T, pos, R):
          78 +    ep = pos - T[:3, 3]
          79 +    ang = _Rot.from_matrix(R @ T[:3, :3].T).as_rotvec()
          80 +    return np.concatenate([ep, ang])
diff --git a/grid_0.txt b/grid_0.txt
new file mode 100644
index 0000000..ca53324
--- /dev/null
+++ b/grid_0.txt
@@ -0,0 +1,12 @@
           1 +yaw 0.0 center 0.27 0.173 step 0.02
           2 ++0.370 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           3 ++0.350 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           4 ++0.330 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           5 ++0.310 0.230 0.230 0.230 0.230 0.260 0.260 0.260 0.230 0.230 0.230 0.230
           6 ++0.290 0.230 0.230 0.230 0.230 0.280 0.280 0.280 0.230 0.230 0.230 0.230
           7 ++0.270 0.230 0.230 0.230 0.230 0.280 0.280 0.280 0.230 0.230 0.230 0.230
           8 ++0.250 0.230 0.230 0.230 0.230 0.280 0.280 0.280 0.230 0.230 0.230 0.230
           9 ++0.230 0.230 0.230 0.230 0.230 0.280 0.280 0.280 0.230 0.230 0.230 0.230
          10 ++0.210 0.230 0.230 0.230 0.230 0.235 0.235 0.235 0.230 0.230 0.230 0.230
          11 ++0.190 0.230 0.230 0.230 0.230 0.280 0.280 0.280 0.230 0.230 0.230 0.230
          12 ++0.170 0.230 0.230 0.230 0.230 0.280 0.280 0.280 0.230 0.230 0.230 0.230
diff --git a/grid_1.5708.txt b/grid_1.5708.txt
new file mode 100644
index 0000000..2650025
--- /dev/null
+++ b/grid_1.5708.txt
@@ -0,0 +1,12 @@
           1 +yaw 1.5708 center 0.27 0.173 step 0.02
           2 ++0.370 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           3 ++0.350 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           4 ++0.330 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           5 ++0.310 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           6 ++0.290 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           7 ++0.270 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           8 ++0.250 0.230 0.270 0.280 0.280 0.240 0.230 0.240 0.280 0.280 0.270 0.230
           9 ++0.230 0.230 0.270 0.280 0.280 0.240 0.230 0.240 0.280 0.280 0.270 0.230
          10 ++0.210 0.230 0.270 0.280 0.280 0.240 0.230 0.240 0.280 0.280 0.270 0.230
          11 ++0.190 0.230 0.270 0.280 0.280 0.240 0.230 0.240 0.280 0.280 0.270 0.230
          12 ++0.170 0.230 0.230 0.240 0.240 0.235 0.230 0.235 0.240 0.240 0.230 0.230
diff --git a/kin.py b/kin.py
new file mode 100644
index 0000000..19ed11b
--- /dev/null
+++ b/kin.py
@@ -0,0 +1,80 @@
           1 +import numpy as np
           2 +
           3 +def rpy_mat(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def tf(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = rpy_mat(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +def rotz(q):
          13 +    c, s = np.cos(q), np.sin(q)
          14 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          15 +
          16 +PI = np.pi
          17 +JOINTS = [
          18 +    tf([0, 0, 0.15643], [PI, 0, 0]),
          19 +    tf([0, 0.005375, -0.12838], [PI/2, 0, 0]),
          20 +    tf([0, -0.21038, -0.006375], [-PI/2, 0, 0]),
          21 +    tf([0, 0.006375, -0.21038], [PI/2, 0, 0]),
          22 +    tf([0, -0.20843, -0.006375], [-PI/2, 0, 0]),
          23 +    tf([0, 0.00017505, -0.10593], [PI/2, 0, 0]),
          24 +    tf([0, -0.10593, -0.00017505], [-PI/2, 0, 0]),
          25 +]
          26 +EE = tf([0, 0, -0.061525], [PI, 0, 0])
          27 +
          28 +def fk_all(q, base=(0, 0, 0), base_z=0.0, tool=0.0):
          29 +    T = np.eye(4)
          30 +    T[:3, :3] = rpy_mat(0, 0, base[2]); T[:3, 3] = [base[0], base[1], base_z]
          31 +    frames = [T.copy()]
          32 +    for i in range(7):
          33 +        T = T @ JOINTS[i] @ rotz(q[i])
          34 +        frames.append(T.copy())
          35 +    T = T @ EE
          36 +    frames.append(T.copy())
          37 +    Tt = T.copy(); Tt[:3, 3] = T[:3, 3] + T[:3, 2] * tool
          38 +    frames.append(Tt)
          39 +    return frames
          40 +
          41 +def ee_pose(q, base, base_z=0.0, tool=0.0):
          42 +    return fk_all(q, base, base_z, tool)[-1]
          43 +
          44 +def pose_err(T, pos, R):
          45 +    ep = pos - T[:3, 3]
          46 +    Re = R @ T[:3, :3].T
          47 +    # axis-angle of Re
          48 +    ang = np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]]) * 0.5
          49 +    return np.concatenate([ep, ang])
          50 +
          51 +def down_R(yaw):
          52 +    # z axis pointing down, x axis along yaw
          53 +    c, s = np.cos(yaw), np.sin(yaw)
          54 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          55 +    return np.stack([x, y, z], axis=1)
          56 +
          57 +def ik(q0, pos, R, base, base_z=0.0, tool=0.0, iters=200, wrot=0.3, tol=1e-4):
          58 +    q = np.array(q0, dtype=float)
          59 +    W = np.array([1, 1, 1, wrot, wrot, wrot])
          60 +    for it in range(iters):
          61 +        T = ee_pose(q, base, base_z, tool)
          62 +        e = pose_err(T, pos, R) * W
          63 +        if np.linalg.norm(e) < tol:
          64 +            break
          65 +        J = np.zeros((6, 7)); h = 1e-6
          66 +        for i in range(7):
          67 +            dq = q.copy(); dq[i] += h
          68 +            J[:, i] = (pose_err(ee_pose(dq, base, base_z, tool), pos, R) * W - e) / -h
          69 +        lam = 1e-3
          70 +        step = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
          71 +        n = np.linalg.norm(step)
          72 +        if n > 0.3: step *= 0.3 / n
          73 +        q += step
          74 +    return q, np.linalg.norm(e)
          75 +
          76 +from scipy.spatial.transform import Rotation as _Rot
          77 +def pose_err(T, pos, R):
          78 +    ep = pos - T[:3, 3]
          79 +    ang = _Rot.from_matrix(R @ T[:3, :3].T).as_rotvec()
          80 +    return np.concatenate([ep, ang])
diff --git a/m1.txt b/m1.txt
new file mode 100644
index 0000000..5ed9af9
--- /dev/null
+++ b/m1.txt
@@ -0,0 +1,14 @@
           1 +y -0.12 0.22499999999999992
           2 +y -0.1 0.22499999999999992
           3 +y -0.08 0.22499999999999992
           4 +y -0.06 0.22499999999999992
           5 +y -0.04 0.22499999999999992
           6 +y -0.02 0.27499999999999997
           7 +y 0.0 0.27499999999999997
           8 +y 0.02 0.27499999999999997
           9 +y 0.04 0.22499999999999992
          10 +y 0.06 0.22499999999999992
          11 +y 0.08 0.22499999999999992
          12 +y 0.1 0.22499999999999992
          13 +y 0.12 0.22499999999999992
          14 +21.0484561920166
diff --git a/m2.txt b/m2.txt
new file mode 100644
index 0000000..4552f1e
--- /dev/null
+++ b/m2.txt
@@ -0,0 +1,14 @@
           1 +x -0.12 0.23499999999999993
           2 +x -0.1 0.22499999999999992
           3 +x -0.08 0.22499999999999992
           4 +x -0.06 0.22499999999999992
           5 +x -0.04 0.22499999999999992
           6 +x -0.02 0.22499999999999992
           7 +x 0.0 0.22499999999999992
           8 +x 0.02 0.22499999999999992
           9 +x 0.04 0.22499999999999992
          10 +x 0.06 0.22499999999999992
          11 +x 0.08 0.22499999999999992
          12 +x 0.1 0.22499999999999992
          13 +x 0.12 0.22499999999999992
          14 +19.209277629852295
diff --git a/m3.txt b/m3.txt
new file mode 100644
index 0000000..2f426fc
--- /dev/null
+++ b/m3.txt
@@ -0,0 +1,14 @@
           1 +y -0.12 0.22499999999999992
           2 +y -0.1 0.22499999999999992
           3 +y -0.08 0.22499999999999992
           4 +y -0.06 0.22499999999999992
           5 +y -0.04 0.23499999999999993
           6 +y -0.02 0.23499999999999993
           7 +y 0.0 0.23499999999999993
           8 +y 0.02 0.23499999999999993
           9 +y 0.04 0.22499999999999992
          10 +y 0.06 0.22499999999999992
          11 +y 0.08 0.22499999999999992
          12 +y 0.1 0.22499999999999992
          13 +y 0.12 0.22499999999999992
          14 +23.501456022262573
diff --git a/probe0.py b/probe0.py
new file mode 100644
index 0000000..a101ae8
--- /dev/null
+++ b/probe0.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def dump(obs):
           5 +    for o in sorted(obs.data, key=lambda o:o.name):
           6 +        f = obs.type_features[o.type]
           7 +        print(o.name, {k: round(float(v),4) for k,v in zip(f, obs.data[o])})
           8 +for seed in [0,1,2]:
           9 +    obs, info = env.reset(seed=seed)
          10 +    print("seed",seed); dump(obs)
          11 +env.close()
diff --git a/probe1.py b/probe1.py
new file mode 100644
index 0000000..e0d12c3
--- /dev/null
+++ b/probe1.py
@@ -0,0 +1,24 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +R = obs.get_object_from_name("robot")
           6 +F = obs.type_features[R.type]
           7 +def rv(o): return np.round(o.data[R],4)
           8 +print(F)
           9 +print(rv(obs))
          10 +a = np.zeros(11, dtype=np.float32)
          11 +a[3]=0.1; a[4]=0.3
          12 +obs,r,te,tr,_ = env.step(a); print("j1+.1 j2+.3(clipped?)", rv(obs), r)
          13 +a = np.zeros(11, dtype=np.float32); a[0]=0.1; a[2]=0.1
          14 +obs,r,te,tr,_ = env.step(a); print("base", rv(obs))
          15 +a = np.zeros(11, dtype=np.float32); a[10]=-1
          16 +obs,r,te,tr,_ = env.step(a); print("close", rv(obs))
          17 +a = np.zeros(11, dtype=np.float32); a[10]=1
          18 +obs,r,te,tr,_ = env.step(a); print("open", rv(obs))
          19 +a = np.zeros(11, dtype=np.float32); a[4]=0.2
          20 +for i in range(15):
          21 +    obs,r,te,tr,_ = env.step(a)
          22 +    print(i, rv(obs)[:10])
          23 +print(env.max_steps)
          24 +env.close()
diff --git a/probe_base_1.py b/probe_base_1.py
new file mode 100644
index 0000000..2b442ab
--- /dev/null
+++ b/probe_base_1.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def rob(obs):
           5 +    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
           6 +def A(**kw):
           7 +    a = np.zeros(11, dtype=np.float32)
           8 +    for k,v in kw.items(): a[int(k[1:])] = v
           9 +    return a
          10 +tests = [("x+.1",A(i0=.1)),("x-.1",A(i0=-.1)),("y+.1",A(i1=.1)),("y-.1",A(i1=-.1)),("rot+.1",A(i2=.1)),("rot-.1",A(i2=-.1)),
          11 +         ("x+.01",A(i0=.01)),("x-.05",A(i0=-.05)),("y+.05",A(i1=.05)),("rot.05",A(i2=.05)),("x-.1y.1rot.1",A(i0=-.1,i1=.1,i2=.1)),
          12 +         ("x+.5 clip?",A(i0=.5)),("x-.5",A(i0=-.5))]
          13 +for name,a in tests:
          14 +    obs,_ = env.reset(seed=1)
          15 +    s0 = rob(obs)
          16 +    obs,*_ = env.step(a); s1 = rob(obs)
          17 +    obs,*_ = env.step(a); s2 = rob(obs)
          18 +    print(name, "d1", np.round(s1-s0,5)[:3], "d2", np.round(s2-s1,5)[:3], "other", np.abs(s2-s0)[3:].max().round(5))
          19 +env.close()
diff --git a/probe_base_10.py b/probe_base_10.py
new file mode 100644
index 0000000..ac5afbc
--- /dev/null
+++ b/probe_base_10.py
@@ -0,0 +1,31 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def A(**kw):
           5 +    a = np.zeros(11, dtype=np.float32)
           6 +    for k,v in kw.items(): a[int(k[1:])] = v
           7 +    return a
           8 +def objs(obs): return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name!="robot"}
           9 +# j2 limit off-table
          10 +obs,_=env.reset(seed=1); R=obs.get_object_from_name("robot")
          11 +for _ in range(10): obs,*_=env.step(A(i1=.2))
          12 +for _ in range(50):
          13 +    j=obs.get(R,"joint_2"); obs,*_=env.step(A(i4=.05))
          14 +    if abs(obs.get(R,"joint_2")-j)<1e-6: break
          15 +print("off-table (y=2) j2 stops at", obs.get(R,"joint_2"))
          16 +rng=np.random.default_rng(1)
          17 +tot=rej=0; moves=[]
          18 +for seed in range(5):
          19 +    obs,_=env.reset(seed=seed); o0=objs(obs)
          20 +    obs,*_=env.step(A(i0=.05))
          21 +    for t in range(400):
          22 +        a=np.zeros(11,np.float32); a[3:10]=rng.uniform(-.2,.2,7); a[10]=1
          23 +        a[4]+=0.03  # bias downward
          24 +        s=np.array(obs.data[R][:10]); obs,*_=env.step(a); tot+=1
          25 +        if np.allclose(np.array(obs.data[R][:10]),s): rej+=1
          26 +        o=objs(obs)
          27 +        for k in o0:
          28 +            if np.abs(o[k]-o0[k]).max()>1e-6: moves.append((seed,t,k,np.round(o[k]-o0[k],3)))
          29 +        o0=o
          30 +print("steps",tot,"rejected",rej,"object moves",len(moves)); print(moves[:10])
          31 +env.close()
diff --git a/probe_base_2.py b/probe_base_2.py
new file mode 100644
index 0000000..c4e188c
--- /dev/null
+++ b/probe_base_2.py
@@ -0,0 +1,39 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def rob(obs):
           5 +    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
           6 +def A(**kw):
           7 +    a = np.zeros(11, dtype=np.float32)
           8 +    for k,v in kw.items(): a[int(k[1:])] = v
           9 +    return a
          10 +for seed in [0,1]:
          11 +    obs,_ = env.reset(seed=seed); s=rob(obs)
          12 +    for i in range(30):
          13 +        obs,*_ = env.step(A(i0=.01)); n=rob(obs)
          14 +        if np.allclose(n,s): print("seed",seed,"x+ stops at base_x",n[0]); break
          15 +        s=n
          16 +    # exactness
          17 +    obs,_=env.reset(seed=seed); s0=rob(obs)
          18 +    obs,*_=env.step(A(i1=0.0123456,i2=-0.0333,i3=0.0777)); s1=rob(obs)
          19 +    print("exact diff", (s1-s0)[:4]-np.array([0,0.0123456,-0.0333,0.0777],dtype=np.float32))
          20 +# rejection whole action: x+.1 (rejected) combined with y+.1 and j1+.1
          21 +for name,a in [("x+.1 & y+.1",A(i0=.1,i1=.1)),("x+.1 & j1+.1",A(i0=.1,i3=.1)),("x+.1 & rot.1",A(i0=.1,i2=.1))]:
          22 +    obs,_=env.reset(seed=1); s0=rob(obs); obs,*_=env.step(a); print(name, np.round(rob(obs)-s0,4))
          23 +# base x limit when moving away / y wide range
          24 +obs,_=env.reset(seed=1); s=rob(obs)
          25 +for i in range(60):
          26 +    obs,*_=env.step(A(i0=-.2)); n=rob(obs)
          27 +    if np.allclose(n,s): break
          28 +    s=n
          29 +print("x- stops at", n[0], "after", i)
          30 +obs,_=env.reset(seed=1); s=rob(obs)
          31 +for i in range(60):
          32 +    obs,*_=env.step(A(i1=.2)); n=rob(obs)
          33 +    if np.allclose(n,s): break
          34 +    s=n
          35 +print("y+ stops at", n[1], "after", i)
          36 +obs,_=env.reset(seed=1); 
          37 +for i in range(40): obs,*_=env.step(A(i2=.2))
          38 +print("rot after 40*0.2 =", rob(obs)[2], "(8.0 raw)")
          39 +env.close()
diff --git a/probe_base_3.py b/probe_base_3.py
new file mode 100644
index 0000000..ae5027c
--- /dev/null
+++ b/probe_base_3.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def rob(obs):
           5 +    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
           6 +def A(**kw):
           7 +    a = np.zeros(11, dtype=np.float32)
           8 +    for k,v in kw.items(): a[int(k[1:])] = v
           9 +    return a
          10 +def push(seed, idx, d, n=80, pre=()):
          11 +    obs,_=env.reset(seed=seed)
          12 +    for p in pre: obs,*_=env.step(p)
          13 +    s=rob(obs); k=0
          14 +    for i in range(n):
          15 +        obs,*_=env.step(A(**{f"i{idx}":d})); m=rob(obs)
          16 +        if np.allclose(m,s): break
          17 +        s=m; k+=1
          18 +    return s, k
          19 +# x+ at y=2 (off table?)
          20 +s,k=push(1,0,.01,pre=[A(i1=.2)]*10); print("x+ at y=2 stops at x",s[0],k)
          21 +s,k=push(1,0,.01,pre=[A(i2=.2)]*16); print("x+ at rot=pi stops at x",s[0],k)
          22 +for j in range(1,8):
          23 +    idx=2+j
          24 +    for d in (.2,-.2):
          25 +        s,k=push(1,idx,d,n=40)
          26 +        # find fine limit with 0.01
          27 +        obs,_=env.reset(seed=1)
          28 +        s2,k2=None,None
          29 +        print(f"j{j} d{d:+}: stops at {s[idx]:.4f} after {k} steps")
          30 +env.close()
diff --git a/probe_base_4.py b/probe_base_4.py
new file mode 100644
index 0000000..3db101a
--- /dev/null
+++ b/probe_base_4.py
@@ -0,0 +1,42 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def rob(obs):
           5 +    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
           6 +def objs(obs):
           7 +    return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name not in ("robot",)}
           8 +def A(**kw):
           9 +    a = np.zeros(11, dtype=np.float32)
          10 +    for k,v in kw.items(): a[int(k[1:])] = v
          11 +    return a
          12 +obs,_=env.reset(seed=1)
          13 +for _ in range(3): obs,*_=env.step(A(i4=.2))
          14 +s0=rob(obs); print("j2 now",s0[4])
          15 +obs,*_=env.step(A(i4=.2,i3=.1)); print("j2+.2(rej)&j1+.1:",np.round(rob(obs)-s0,4))
          16 +obs,_=env.reset(seed=1); s0=rob(obs)
          17 +obs,*_=env.step(A(i3=.7)); print("j1 +0.7 ->",np.round(rob(obs)-s0,4)[3])
          18 +obs,_=env.reset(seed=1); s0=rob(obs)
          19 +obs,*_=env.step(A(i6=-.1)); print("j4 -0.1 ->",np.round(rob(obs)-s0,4)[6])
          20 +obs,*_=env.step(A(i6=-.1)); print("j4 another -0.1 ->",np.round(rob(obs)-s0,4)[6])
          21 +# fine j2 limit via 0.01
          22 +obs,_=env.reset(seed=1); s=rob(obs)
          23 +for i in range(200):
          24 +    obs,*_=env.step(A(i4=.01)); m=rob(obs)
          25 +    if np.allclose(m,s): break
          26 +    s=m
          27 +print("j2 fine stop", s[4])
          28 +# random exploration for object movement
          29 +rng=np.random.default_rng(0)
          30 +moved=0; tot=0
          31 +for seed in range(4):
          32 +    obs,_=env.reset(seed=seed); o0=objs(obs)
          33 +    for t in range(300):
          34 +        a=rng.uniform(-.2,.2,11).astype(np.float32); a[10]=1.0
          35 +        a[0]=abs(a[0])*0.3 if t<100 else a[0]*0.3
          36 +        obs,*_=env.step(a); tot+=1
          37 +        o=objs(obs)
          38 +        for k in o0:
          39 +            if np.abs(o[k]-o0[k]).max()>1e-6:
          40 +                moved+=1; print("seed",seed,"t",t,k,"moved",np.round(o[k]-o0[k],4)); o0=o; break
          41 +print("moves",moved,"of steps",tot)
          42 +env.close()
diff --git a/probe_base_5.py b/probe_base_5.py
new file mode 100644
index 0000000..3afbf5b
--- /dev/null
+++ b/probe_base_5.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def rob(obs):
           5 +    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
           6 +def objs(obs):
           7 +    return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name!="robot"}
           8 +def A(**kw):
           9 +    a = np.zeros(11, dtype=np.float32)
          10 +    for k,v in kw.items(): a[int(k[1:])] = v
          11 +    return a
          12 +obs,_=env.reset(seed=1)
          13 +for _ in range(5): obs,*_=env.step(A(i4=.2))
          14 +s0=rob(obs); print("j2 now",s0[4])
          15 +obs,*_=env.step(A(i4=.2,i3=.1)); print("j2+.2(rej)&j1+.1:",np.round(rob(obs)-s0,4))
          16 +obs,*_=env.step(A(i4=.01,i3=.1)); print("j2+.01&j1+.1:",np.round(rob(obs)-s0,4))
          17 +# sweeps: for each seed, lower arm, then sweep j1 and base y, record rejections + object moves
          18 +for seed in range(6):
          19 +    obs,_=env.reset(seed=seed); o0=objs(obs)
          20 +    for _ in range(5): obs,*_=env.step(A(i4=.2))
          21 +    rej=0; mv=set()
          22 +    seq=[A(i3=.05)]*40+[A(i3=-.05)]*80+[A(i1=.05)]*20+[A(i1=-.05)]*40+[A(i0=.02)]*10+[A(i3=.05)]*80
          23 +    for a in seq:
          24 +        s=rob(obs); obs,*_=env.step(a)
          25 +        if np.allclose(rob(obs),s): rej+=1
          26 +        o=objs(obs)
          27 +        for k in o0:
          28 +            if np.abs(o[k]-o0[k]).max()>1e-6: mv.add(k)
          29 +    print("seed",seed,"rejected",rej,"/",len(seq),"moved objs",mv, "final j1",round(rob(obs)[3],2))
          30 +env.close()
diff --git a/probe_base_6.py b/probe_base_6.py
new file mode 100644
index 0000000..7764ed8
--- /dev/null
+++ b/probe_base_6.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +import numpy as np, json
           3 +env = make_env()
           4 +def A(**kw):
           5 +    a = np.zeros(11, dtype=np.float32)
           6 +    for k,v in kw.items(): a[int(k[1:])] = v
           7 +    return a
           8 +obs,_=env.reset(seed=1)
           9 +for _ in range(5): obs,*_=env.step(A(i4=.2))
          10 +for _ in range(3): obs,*_=env.step(A(i4=.02))
          11 +print(type(obs), [m for m in dir(obs) if not m.startswith('_')][:30])
          12 +env.close()
diff --git a/probe_base_7.py b/probe_base_7.py
new file mode 100644
index 0000000..a2ad2da
--- /dev/null
+++ b/probe_base_7.py
@@ -0,0 +1,35 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def A(**kw):
           5 +    a = np.zeros(11, dtype=np.float32)
           6 +    for k,v in kw.items(): a[int(k[1:])] = v
           7 +    return a
           8 +obs,_=env.reset(seed=1)
           9 +for _ in range(5): obs,*_=env.step(A(i4=.2))
          10 +for _ in range(6): obs,*_=env.step(A(i4=.01))
          11 +st=env.get_state(); print(type(st))
          12 +R=st.get_object_from_name("robot"); print("j2",st.get(R,"joint_2"))
          13 +res=[]
          14 +for ob in ["obstruction0","target_block"]:
          15 +  for x in np.arange(0.0,0.8,0.1):
          16 +    for y in np.arange(-0.6,0.61,0.2):
          17 +        s=st.copy(); O=s.get_object_from_name(ob)
          18 +        s.set(O,"pose_x",x); s.set(O,"pose_y",y)
          19 +        # move other objects far away
          20 +        for n in s.get_object_names():
          21 +            if n not in ("robot",ob,"target_region"):
          22 +                o2=s.get_object_from_name(n); s.set(o2,"pose_y",5.0)
          23 +        env.set_state(s)
          24 +        o=env.get_state(); p0=np.array([o.get(O,"pose_x"),o.get(O,"pose_y"),o.get(O,"pose_z")])
          25 +        rej=0
          26 +        for k in range(126):
          27 +            o=env.get_state(); jr=o.get(R,"joint_1")
          28 +            obs,*_=env.step(A(i3=.05))
          29 +            if abs(obs.get(R,"joint_1")-jr)<1e-6: rej+=1; break
          30 +        p1=np.array([obs.get(O,"pose_x"),obs.get(O,"pose_y"),obs.get(O,"pose_z")])
          31 +        mv=np.abs(p1-p0).max()
          32 +        if rej or mv>1e-6: res.append((ob,round(x,2),round(y,2),rej,round(mv,4),round(obs.get(R,"joint_1"),2)))
          33 +for r in res: print(r)
          34 +print("n events",len(res))
          35 +env.close()
diff --git a/probe_base_8.py b/probe_base_8.py
new file mode 100644
index 0000000..f7dff9e
--- /dev/null
+++ b/probe_base_8.py
@@ -0,0 +1,16 @@
           1 +from env_client import make_env
           2 +import numpy as np, json
           3 +env = make_env()
           4 +def A(**kw):
           5 +    a = np.zeros(11, dtype=np.float32)
           6 +    for k,v in kw.items(): a[int(k[1:])] = v
           7 +    return a
           8 +obs,_=env.reset(seed=1)
           9 +for _ in range(5): obs,*_=env.step(A(i4=.2))
          10 +for _ in range(6): obs,*_=env.step(A(i4=.01))
          11 +print([o.name for o in obs.data])
          12 +try: v=env.observation_space.vectorize(obs); print("vec ok")
          13 +except Exception as e: v=obs.vec(list(obs.data)); print("fallback",e)
          14 +json.dump([float(x) for x in v], open("probe_base_vec.json","w"))
          15 +print(len(v))
          16 +env.close()
diff --git a/probe_base_9.py b/probe_base_9.py
new file mode 100644
index 0000000..8f912ee
--- /dev/null
+++ b/probe_base_9.py
@@ -0,0 +1,29 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def A(**kw):
           5 +    a = np.zeros(11, dtype=np.float32)
           6 +    for k,v in kw.items(): a[int(k[1:])] = v
           7 +    return a
           8 +def objs(obs): return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name!="robot"}
           9 +R=None
          10 +events=[]
          11 +for seed in [1,2]:
          12 +  for bx in [-0.07,-0.2,-0.35]:
          13 +    for by in [-0.3,0.0,0.3]:
          14 +      for j2 in [0.3,0.5,0.7]:
          15 +        obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot")
          16 +        steps=[A(i0=bx+0.12)] if abs(bx+0.12)>1e-9 else []
          17 +        for a in steps+[A(i1=by)]: obs,*_=env.step(a)
          18 +        n=int(round((j2+0.35)/0.1))
          19 +        for _ in range(n): obs,*_=env.step(A(i4=.1))
          20 +        o0=objs(obs); jj=obs.get(R,"joint_2")
          21 +        rej=0
          22 +        for d in [0.1]*32+[-0.1]*64:
          23 +            j=obs.get(R,"joint_1"); obs,*_=env.step(A(i3=d))
          24 +            if abs(obs.get(R,"joint_1")-j)<1e-6: rej+=1
          25 +        o=objs(obs); mv={k:np.round(o[k]-o0[k],3) for k in o0 if np.abs(o[k]-o0[k]).max()>1e-6}
          26 +        if rej or mv: events.append((seed,bx,by,round(jj,2),rej,mv))
          27 +for e in events: print(e)
          28 +print(len(events))
          29 +env.close()
diff --git a/probe_base_vec.json b/probe_base_vec.json
new file mode 100644
index 0000000..5b10326
--- /dev/null
+++ b/probe_base_vec.json
@@ -0,0 +1 @@
           1 +[0.419426292181015, -0.14254437386989594, 0.10106389969587326, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, 0.013297317549586296, 0.017884286120533943, 0.01606389693915844, -0.11999999731779099, 0.0, 0.0, 0.0, 0.7100000381469727, -3.1415927410125732, -2.5, 0.0, -0.8700000047683716, 1.5707963705062866, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.13774842023849487, 0.18313223123550415, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, 0.02828371897339821, 0.038811128586530685, 0.02500000037252903, 0.44773608446121216, -0.132277250289917, 0.07999999821186066, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, 0.035354647785425186, 0.04851391166448593, 0.004999999888241291]
\ No newline at end of file
diff --git a/probe_grasp.py b/probe_grasp.py
new file mode 100644
index 0000000..b323201
--- /dev/null
+++ b/probe_grasp.py
@@ -0,0 +1,41 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +env = make_env()
           5 +obs, info = env.reset(seed=0)
           6 +R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
           7 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           8 +def goto(obs, qt, grip=0.0, maxn=40):
           9 +    for _ in range(maxn):
          10 +        q = q_of(obs)
          11 +        d = qt - q
          12 +        if np.max(np.abs(d)) < 1e-4: break
          13 +        d = np.clip(d, -0.2, 0.2)
          14 +        a = np.zeros(11, np.float32); a[3:10] = d; a[10] = grip
          15 +        obs2, r, te, tr, _ = env.step(a)
          16 +        if np.allclose(q_of(obs2), q): return obs2, False
          17 +        obs = obs2
          18 +    return obs, True
          19 +yaw = float(sys.argv[1]) if len(sys.argv)>1 else 0.0
          20 +bx, by = obs.get(B,'pose_x'), obs.get(B,'pose_y')
          21 +base = (-0.12,0,0)
          22 +q = q_of(obs)
          23 +for z in [0.45,0.40,0.36,0.34,0.32,0.30,0.29,0.28,0.27,0.26,0.25,0.24,0.235,0.23,0.225,0.22,0.215,0.21,0.205,0.20]:
          24 +    qt, e = ik(q, np.array([bx,by,z]), down_R(yaw), base)
          25 +    obs, ok = goto(obs, qt)
          26 +    q = q_of(obs)
          27 +    print(z, ok, round(e,5), np.round(obs.data[B][:3],4))
          28 +    if not ok: break
          29 +# close
          30 +a = np.zeros(11, np.float32); a[10] = -1
          31 +for k in range(3):
          32 +    obs,_,_,_,_ = env.step(a); print('close', k, np.round(obs.data[R][10:12],3))
          33 +print("after close robot", np.round(obs.data[R][10:],4), "block", np.round(obs.data[B],4))
          34 +T = ee_pose(q_of(obs), base)
          35 +print("EE", np.round(T,4))
          36 +# lift
          37 +qt,e = ik(q_of(obs), T[:3,3]+[0,0,0.1], T[:3,:3], base)
          38 +obs, ok = goto(obs, qt)
          39 +print("lift", ok, np.round(obs.data[B][:7],4), np.round(obs.data[R][10:],4))
          40 +T = ee_pose(q_of(obs), base); print("EE", np.round(T[:3,3],4))
          41 +env.close()
diff --git a/probe_grasp2.py b/probe_grasp2.py
new file mode 100644
index 0000000..155b42b
--- /dev/null
+++ b/probe_grasp2.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +env = make_env()
           5 +R=None
           6 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           7 +def goto(obs, qt, grip=0.0, maxn=40):
           8 +    for _ in range(maxn):
           9 +        q = q_of(obs); d = qt - q
          10 +        if np.max(np.abs(d)) < 1e-4: break
          11 +        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2); a[10] = grip
          12 +        obs2, r, te, tr, info = env.step(a)
          13 +        if np.allclose(q_of(obs2), q): return obs2, False
          14 +        obs = obs2
          15 +    return obs, True
          16 +base=(-0.12,0,0)
          17 +yaw=float(sys.argv[1])
          18 +for zc in [0.235,0.245,0.255,0.265,0.28]:
          19 +    obs, info = env.reset(seed=0)
          20 +    R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
          21 +    bx, by = obs.get(B,'pose_x'), obs.get(B,'pose_y')
          22 +    q=q_of(obs)
          23 +    for z in [0.4,0.33,zc]:
          24 +        qt,e = ik(q, np.array([bx,by,z]), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs)
          25 +    res=[]
          26 +    for g in [-1,-1,-1]:
          27 +        a=np.zeros(11,np.float32); a[10]=g
          28 +        obs,r,te,tr,info=env.step(a); res.append(tuple(np.round(obs.data[R][10:12],3)))
          29 +    print(zc, ok, res, info)
          30 +env.close()
diff --git a/probe_grasp3.py b/probe_grasp3.py
new file mode 100644
index 0000000..dcc0ce6
--- /dev/null
+++ b/probe_grasp3.py
@@ -0,0 +1,32 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +env = make_env()
           5 +R=None
           6 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           7 +def goto(obs, qt, grip=0.0, maxn=40):
           8 +    for _ in range(maxn):
           9 +        q = q_of(obs); d = qt - q
          10 +        if np.max(np.abs(d)) < 1e-4: break
          11 +        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2); a[10] = grip
          12 +        obs2, r, te, tr, info = env.step(a)
          13 +        if np.allclose(q_of(obs2), q): return obs2, False
          14 +        obs = obs2
          15 +    return obs, True
          16 +base=(0,0,0)
          17 +yaw=float(sys.argv[1]); zc=float(sys.argv[2])
          18 +obs, info = env.reset(seed=0)
          19 +R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
          20 +bx, by = obs.get(B,'pose_x'), obs.get(B,'pose_y')
          21 +q=q_of(obs)
          22 +for z in [0.4,0.33,zc]:
          23 +    qt,e = ik(q, np.array([bx,by,z]), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs)
          24 +print("reached", ok)
          25 +a=np.zeros(11,np.float32); a[10]=-1
          26 +obs,r,te,tr,info=env.step(a); print("close", np.round(obs.data[R][10:],4))
          27 +T=ee_pose(q,base); print("EE", np.round(T,4))
          28 +print("block", np.round(obs.data[B][:8],4))
          29 +qt,e=ik(q,T[:3,3]+[0,0,0.1],T[:3,:3],base); obs,ok=goto(obs,qt)
          30 +print("lift", ok, np.round(obs.data[B][:8],4))
          31 +T2=ee_pose(q_of(obs),base); print("EE2", np.round(T2[:3,3],4))
          32 +env.close()
diff --git a/probe_grid.py b/probe_grid.py
new file mode 100644
index 0000000..381ae47
--- /dev/null
+++ b/probe_grid.py
@@ -0,0 +1,39 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys, time, json
           4 +env = make_env()
           5 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); cx=float(sys.argv[3]); cy=float(sys.argv[4]); step=float(sys.argv[5]); n=int(sys.argv[6])
           6 +obs, info = env.reset(seed=seed)
           7 +R = obs.get_object_from_name("robot")
           8 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           9 +def goto(obs, qt, maxn=40):
          10 +    for _ in range(maxn):
          11 +        q = q_of(obs); d = qt - q
          12 +        if np.max(np.abs(d)) < 1e-4: break
          13 +        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2)
          14 +        obs2, r, te, tr, _ = env.step(a)
          15 +        if np.allclose(q_of(obs2), q): return obs2, False
          16 +        obs = obs2
          17 +    return obs, True
          18 +base=(-0.12,0,0)
          19 +q=q_of(obs)
          20 +qhome,_=ik(q,np.array([cx,cy,0.36]),down_R(yaw),base)
          21 +obs,ok=goto(obs,qhome); q=q_of(obs)
          22 +out={}
          23 +for i in range(-n,n+1):
          24 +  for j in range(-n,n+1):
          25 +    x,y=cx+i*step, cy+j*step
          26 +    qa,_=ik(qhome,np.array([x,y,0.34]),down_R(yaw),base); obs,ok=goto(obs,qa); q=q_of(obs)
          27 +    stop=None
          28 +    for z in np.arange(0.33,0.22,-0.005):
          29 +        qt,_=ik(q,np.array([x,y,z]),down_R(yaw),base); obs,ok=goto(obs,qt); q=q_of(obs)
          30 +        if not ok: stop=round(z+0.005,3); break
          31 +    out[(i,j)]=stop
          32 +    for zz in np.arange(ee_pose(q,base)[2,3],0.345,0.02):
          33 +        qt,_=ik(q,np.array([x,y,zz]),down_R(yaw),base); obs,ok=goto(obs,qt); q=q_of(obs)
          34 +    obs,ok=goto(obs,qhome); q=q_of(obs)
          35 +# print map: rows = x (i), cols = y (j)
          36 +print("yaw",yaw,"center",cx,cy,"step",step)
          37 +for i in range(n,-n-1,-1):
          38 +    print("%+.3f "%(cx+i*step)+" ".join("  -  " if out[(i,j)] is None else "%.3f"%out[(i,j)] for j in range(-n,n+1)))
          39 +env.close()
diff --git a/probe_grip3.py b/probe_grip3.py
new file mode 100644
index 0000000..bca2e3c
--- /dev/null
+++ b/probe_grip3.py
@@ -0,0 +1,10 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=3)
           5 +R = obs.get_object_from_name("robot")
           6 +for g in [1,1,-1,-1,-0.7,-1,1,0,-1]:
           7 +    a=np.zeros(11,np.float32); a[10]=g; a[3]=0.01
           8 +    obs,r,te,tr,info=env.step(a); print(g, np.round(obs.data[R][3:12],3))
           9 +print(env.action_space.low, env.action_space.high)
          10 +env.close()
diff --git a/probe_map.py b/probe_map.py
new file mode 100644
index 0000000..c24c94c
--- /dev/null
+++ b/probe_map.py
@@ -0,0 +1,34 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys, time
           4 +env = make_env()
           5 +obs, info = env.reset(seed=0)
           6 +R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
           7 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           8 +def goto(obs, qt, maxn=40):
           9 +    for _ in range(maxn):
          10 +        q = q_of(obs); d = qt - q
          11 +        if np.max(np.abs(d)) < 1e-4: break
          12 +        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2)
          13 +        obs2, r, te, tr, _ = env.step(a)
          14 +        if np.allclose(q_of(obs2), q): return obs2, False
          15 +        obs = obs2
          16 +    return obs, True
          17 +base=(-0.12,0,0)
          18 +bx,by=obs.get(B,'pose_x'),obs.get(B,'pose_y')
          19 +q=q_of(obs); t=time.time()
          20 +axis=sys.argv[1]; bx+=float(sys.argv[2]); by+=float(sys.argv[3])
          21 +for d in np.arange(-0.12,0.121,0.02):
          22 +    x,y = (bx+d,by) if axis=='x' else (bx,by+d)
          23 +    cur=ee_pose(q,base)[:3,3]
          24 +    for zz in np.arange(cur[2],0.34,0.02):
          25 +        qt,_=ik(q,np.array([cur[0],cur[1],zz]),down_R(0),base); obs,ok=goto(obs,qt); q=q_of(obs)
          26 +    qt,_=ik(q,np.array([x,y,0.34]),down_R(0),base); obs,ok=goto(obs,qt); q=q_of(obs)
          27 +    if not ok: print('move fail')
          28 +    stop=None
          29 +    for z in np.arange(0.32,0.22,-0.005):
          30 +        qt,_=ik(q,np.array([x,y,z]),down_R(0),base); obs,ok=goto(obs,qt); q=q_of(obs)
          31 +        if not ok: stop=z; break
          32 +    print(axis, round(d,3), stop)
          33 +print(time.time()-t)
          34 +env.close()
diff --git a/probe_table.py b/probe_table.py
new file mode 100644
index 0000000..8847d4f
--- /dev/null
+++ b/probe_table.py
@@ -0,0 +1,24 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +env = make_env()
           5 +obs, info = env.reset(seed=0)
           6 +R = obs.get_object_from_name("robot")
           7 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           8 +def goto(obs, qt, grip=0.0, maxn=40):
           9 +    for _ in range(maxn):
          10 +        q = q_of(obs); d = qt - q
          11 +        if np.max(np.abs(d)) < 1e-4: break
          12 +        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2); a[10] = grip
          13 +        obs2, r, te, tr, _ = env.step(a)
          14 +        if np.allclose(q_of(obs2), q): return obs2, False
          15 +        obs = obs2
          16 +    return obs, True
          17 +base=(-0.12,0,0); q=q_of(obs)
          18 +x,y = float(sys.argv[1]), float(sys.argv[2])
          19 +for z in np.arange(0.40,0.10,-0.005):
          20 +    qt,e = ik(q, np.array([x,y,z]), down_R(0), base)
          21 +    obs, ok = goto(obs, qt); q=q_of(obs)
          22 +    if not ok or e>1e-3: print("stop at", round(z,3), ok, e); break
          23 +print("EE z", ee_pose(q,base)[2,3])
          24 +env.close()
```

</details>

<a id="C003"></a>
### C003 · First full approach: clear obstructions then place block

Commit `c07147037442a45ce9df9f7ff70d39f39b52203b`; parents: 96e9dc5de2ad8aa774bfeaf251e0c73d04046bac. Recorded author date: 2026-09-30T20:45:35+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0365](01_timeline.md#E0365): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_c071470_approach.py) · [Exact all-file diff](evidence/diffs/C003_c071470.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..744534b
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,378 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place the
           2 +target block on it.  Uses an internal FK/IK model of the Kinova Gen3 (arm base at the
           3 +world origin, verified empirically) and Cartesian straight-line motions."""
           4 +import numpy as np
           5 +
           6 +PI = np.pi
           7 +
           8 +# ----------------------------------------------------------------------------- kinematics
           9 +def _rpy(r, p, y):
          10 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
          11 +    return np.array([[cy * cp, cy * sp * sr - sy * cr, cy * sp * cr + sy * sr],
          12 +                     [sy * cp, sy * sp * sr + cy * cr, sy * sp * cr - cy * sr],
          13 +                     [-sp, cp * sr, cp * cr]])
          14 +
          15 +
          16 +def _tf(xyz, rpy):
          17 +    T = np.eye(4)
          18 +    T[:3, :3] = _rpy(*rpy)
          19 +    T[:3, 3] = xyz
          20 +    return T
          21 +
          22 +
          23 +_JOINTS = [
          24 +    _tf([0, 0, 0.15643], [PI, 0, 0]),
          25 +    _tf([0, 0.005375, -0.12838], [PI / 2, 0, 0]),
          26 +    _tf([0, -0.21038, -0.006375], [-PI / 2, 0, 0]),
          27 +    _tf([0, 0.006375, -0.21038], [PI / 2, 0, 0]),
          28 +    _tf([0, -0.20843, -0.006375], [-PI / 2, 0, 0]),
          29 +    _tf([0, 0.00017505, -0.10593], [PI / 2, 0, 0]),
          30 +    _tf([0, -0.10593, -0.00017505], [-PI / 2, 0, 0]),
          31 +]
          32 +_EE = _tf([0, 0, -0.061525], [PI, 0, 0])
          33 +FINGER = 0.155          # EE frame -> fingertip distance (along tool z)
          34 +FINGER_OFF = 0.05       # finger centre offset from tool axis along closing direction
          35 +
          36 +# joint limits (Kinova Gen3); None = continuous
          37 +_LIM = [None, (-2.24, 2.24), None, (-2.57, 2.57), None, (-2.09, 2.09), None]
          38 +
          39 +
          40 +def fk(q):
          41 +    T = np.eye(4)
          42 +    zs, ps = [], []
          43 +    for i in range(7):
          44 +        T = T @ _JOINTS[i]
          45 +        zs.append(T[:3, 2].copy())
          46 +        ps.append(T[:3, 3].copy())
          47 +        c, s = np.cos(q[i]), np.sin(q[i])
          48 +        Rz = np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1.0]])
          49 +        T = T @ Rz
          50 +    T = T @ _EE
          51 +    return T, zs, ps
          52 +
          53 +
          54 +def down_R(yaw):
          55 +    c, s = np.cos(yaw), np.sin(yaw)
          56 +    x = np.array([c, s, 0.0])
          57 +    z = np.array([0, 0, -1.0])
          58 +    y = np.cross(z, x)
          59 +    return np.stack([x, y, z], axis=1)
          60 +
          61 +
          62 +def _rotvec(Rm):
          63 +    cos = (np.trace(Rm) - 1) / 2
          64 +    cos = min(1.0, max(-1.0, cos))
          65 +    ang = np.arccos(cos)
          66 +    v = np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]])
          67 +    if ang < 1e-6:
          68 +        return v * 0.5
          69 +    if ang > PI - 1e-4:
          70 +        # 180 deg: axis from diagonal
          71 +        M = (Rm + np.eye(3)) / 2
          72 +        k = np.argmax(np.diag(M))
          73 +        ax = M[:, k] / np.sqrt(max(M[k, k], 1e-12))
          74 +        return ax * ang
          75 +    return v * ang / (2 * np.sin(ang))
          76 +
          77 +
          78 +def ik(q0, pos, Rt, iters=100, tol=1e-5):
          79 +    q = np.array(q0, dtype=float)
          80 +    err = 1e9
          81 +    for _ in range(iters):
          82 +        T, zs, ps = fk(q)
          83 +        ep = pos - T[:3, 3]
          84 +        er = _rotvec(Rt @ T[:3, :3].T)
          85 +        e = np.concatenate([ep, 0.3 * er])
          86 +        err = np.linalg.norm(e)
          87 +        if err < tol:
          88 +            break
          89 +        J = np.zeros((6, 7))
          90 +        pe = T[:3, 3]
          91 +        for i in range(7):
          92 +            J[:3, i] = np.cross(zs[i], pe - ps[i])
          93 +            J[3:, i] = 0.3 * zs[i]
          94 +        lam = 1e-4
          95 +        dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
          96 +        n = np.max(np.abs(dq))
          97 +        if n > 0.4:
          98 +            dq *= 0.4 / n
          99 +        q += dq
         100 +        for i, lim in enumerate(_LIM):
         101 +            if lim is not None:
         102 +                q[i] = min(lim[1], max(lim[0], q[i]))
         103 +    return q, err
         104 +
         105 +
         106 +def wrap(a):
         107 +    return (a + PI) % (2 * PI) - PI
         108 +
         109 +
         110 +# ----------------------------------------------------------------------------- approach
         111 +class GeneratedApproach:
         112 +    def __init__(self, action_space, observation_space, primitives):
         113 +        self.action_space = action_space
         114 +        self.observation_space = observation_space
         115 +
         116 +    # ---------------------------------------------------------------- state helpers
         117 +    def _robot(self, state):
         118 +        for n in state.get_object_names():
         119 +            if n == "robot":
         120 +                return state.get_object_from_name(n)
         121 +        return None
         122 +
         123 +    def _q(self, state):
         124 +        r = self._robot(state)
         125 +        return np.array([state.get(r, "joint_%d" % i) for i in range(1, 8)])
         126 +
         127 +    def _boxes(self, state):
         128 +        out = {}
         129 +        for n in state.get_object_names():
         130 +            if n == "robot":
         131 +                continue
         132 +            o = state.get_object_from_name(n)
         133 +            try:
         134 +                out[n] = dict(
         135 +                    x=state.get(o, "pose_x"), y=state.get(o, "pose_y"), z=state.get(o, "pose_z"),
         136 +                    hx=state.get(o, "half_extent_x"), hy=state.get(o, "half_extent_y"),
         137 +                    hz=state.get(o, "half_extent_z"), g=state.get(o, "grasp_active"))
         138 +            except Exception:
         139 +                pass
         140 +        return out
         141 +
         142 +    # ---------------------------------------------------------------- episode
         143 +    def reset(self, state, info):
         144 +        self.segs = []          # queue of segments
         145 +        self.cur = None
         146 +        self.last_q = None
         147 +        self.last_cmd = None
         148 +        self.stuck = 0
         149 +        self.held = None
         150 +        self.moved = set()
         151 +        self.fail = {}
         152 +        self.placed_spots = []
         153 +        self.yaw = 0.0
         154 +        self.done_flag = False
         155 +
         156 +    # ---------------------------------------------------------------- geometry
         157 +    def _region(self, boxes):
         158 +        return boxes.get("target_region")
         159 +
         160 +    def _blocking(self, boxes):
         161 +        reg = self._region(boxes)
         162 +        res = []
         163 +        for n, b in boxes.items():
         164 +            if n in ("target_region", "target_block"):
         165 +                continue
         166 +            if abs(b["x"] - reg["x"]) < b["hx"] + reg["hx"] + 0.003 and \
         167 +               abs(b["y"] - reg["y"]) < b["hy"] + reg["hy"] + 0.003 and \
         168 +               b["z"] - b["hz"] < reg["z"] + reg["hz"] + 0.08:
         169 +                res.append(n)
         170 +        return res
         171 +
         172 +    def _grasp_clear(self, boxes, name, yaw):
         173 +        """clearance of finger boxes from other objects for a top-down grasp"""
         174 +        b = boxes[name]
         175 +        ax = np.array([np.cos(yaw), np.sin(yaw)])
         176 +        best = 1e9
         177 +        for sgn in (-1, 1):
         178 +            f = np.array([b["x"], b["y"]]) + sgn * FINGER_OFF * ax
         179 +            for n, o in boxes.items():
         180 +                if n == name or n == "target_region":
         181 +                    continue
         182 +                dx = abs(f[0] - o["x"]) - o["hx"]
         183 +                dy = abs(f[1] - o["y"]) - o["hy"]
         184 +                d = max(dx, dy)
         185 +                best = min(best, d)
         186 +        return best
         187 +
         188 +    def _choose_yaw(self, boxes, name, q):
         189 +        b = boxes[name]
         190 +        cands = []
         191 +        for yaw in (0.0, PI / 2):
         192 +            width = 2 * (b["hx"] if yaw == 0.0 else b["hy"])
         193 +            if width > 0.082:
         194 +                continue
         195 +            clr = self._grasp_clear(boxes, name, yaw)
         196 +            cands.append((min(clr, 0.03) - 0.2 * width, yaw))
         197 +        if not cands:
         198 +            return None
         199 +        cands.sort(reverse=True)
         200 +        yaw = cands[0][1]
         201 +        k = self.fail.get(name, 0)
         202 +        if k % 2 == 1 and len(cands) > 1:
         203 +            yaw = cands[1][1]
         204 +        return self._best_equiv_yaw(yaw, q)
         205 +
         206 +    def _best_equiv_yaw(self, yaw, q):
         207 +        # yaw and yaw+pi are equivalent grasps; pick the one nearer the current tool yaw
         208 +        T, _, _ = fk(q)
         209 +        cur = np.arctan2(T[1, 0], T[0, 0])
         210 +        opts = [yaw, wrap(yaw + PI)]
         211 +        return min(opts, key=lambda a: abs(wrap(a - cur)))
         212 +
         213 +    def _safe_z(self, boxes, held_hz=0.0, held_off=0.0):
         214 +        top = 0.1
         215 +        for n, b in boxes.items():
         216 +            if b["g"] > 0.5:
         217 +                continue
         218 +            top = max(top, b["z"] + b["hz"])
         219 +        return max(0.34, top + 0.03 + held_hz + held_off + FINGER)
         220 +
         221 +    def _drop_spot(self, boxes, name):
         222 +        reg = self._region(boxes)
         223 +        b = boxes[name]
         224 +        best, bs = None, -1e9
         225 +        for x in np.arange(0.15, 0.46, 0.025):
         226 +            for y in np.arange(-0.3, 0.31, 0.025):
         227 +                clr = 1e9
         228 +                for n, o in boxes.items():
         229 +                    if n == name:
         230 +                        continue
         231 +                    m = 0.05 if n != "target_region" else 0.03
         232 +                    dx = abs(x - o["x"]) - o["hx"] - b["hx"] - m
         233 +                    dy = abs(y - o["y"]) - o["hy"] - b["hy"] - m
         234 +                    clr = min(clr, max(dx, dy))
         235 +                for (px, py) in self.placed_spots:
         236 +                    clr = min(clr, max(abs(x - px), abs(y - py)) - 0.08)
         237 +                dist = np.hypot(x - b["x"], y - b["y"])
         238 +                score = min(clr, 0.04) * 10 - dist
         239 +                if score > bs:
         240 +                    bs, best = score, (x, y)
         241 +        return best
         242 +
         243 +    # ---------------------------------------------------------------- planning
         244 +    def _plan_pick_place(self, state, name, place_xy, place_bottom, final_yaw=None):
         245 +        boxes = self._boxes(state)
         246 +        q = self._q(state)
         247 +        b = boxes[name]
         248 +        yaw = self._choose_yaw(boxes, name, q)
         249 +        if yaw is None:
         250 +            yaw = self._best_equiv_yaw(0.0, q)
         251 +        T, _, _ = fk(q)
         252 +        safe0 = self._safe_z(boxes)
         253 +        # fingertip at object centre (but not below support+5mm)
         254 +        tip = max(b["z"], b["z"] - b["hz"] + 0.012)
         255 +        grasp_z = tip + FINGER
         256 +        off = grasp_z - b["z"]          # EE z - object centre z while held
         257 +        safe1 = max(self._safe_z(boxes, b["hz"], 0.0) , b["hz"] + off + 0.03 + 0.15)
         258 +        safe1 = max(safe1, self._safe_z({k: v for k, v in boxes.items() if k != name}) + b["hz"])
         259 +        segs = []
         260 +        segs.append(("move", np.array([T[0, 3], T[1, 3], max(T[2, 3], safe0)]), None))
         261 +        segs.append(("move", np.array([b["x"], b["y"], max(safe0, safe1)]), yaw))
         262 +        segs.append(("move", np.array([b["x"], b["y"], grasp_z]), yaw, "grasp_descend", name))
         263 +        segs.append(("grip", -1.0, name))
         264 +        segs.append(("move", np.array([b["x"], b["y"], safe1]), yaw))
         265 +        pyaw = yaw if final_yaw is None else final_yaw
         266 +        place_z = place_bottom + b["hz"] + off
         267 +        segs.append(("move", np.array([place_xy[0], place_xy[1], safe1]), pyaw))
         268 +        segs.append(("move", np.array([place_xy[0], place_xy[1], place_z]), pyaw, "place_descend"))
         269 +        segs.append(("grip", 1.0, None))
         270 +        segs.append(("move", np.array([place_xy[0], place_xy[1], max(safe1, place_z + 0.05)]), pyaw))
         271 +        return segs
         272 +
         273 +    def _replan(self, state):
         274 +        boxes = self._boxes(state)
         275 +        reg = self._region(boxes)
         276 +        blk = self._blocking(boxes)
         277 +        blk = [n for n in blk if self.fail.get(n, 0) < 6]
         278 +        if blk:
         279 +            # most accessible first: highest grasp clearance
         280 +            q = self._q(state)
         281 +            blk.sort(key=lambda n: -max(self._grasp_clear(boxes, n, 0.0),
         282 +                                         self._grasp_clear(boxes, n, PI / 2)))
         283 +            name = blk[0]
         284 +            spot = self._drop_spot(boxes, name)
         285 +            self.placed_spots.append(spot)
         286 +            b = boxes[name]
         287 +            bottom = 0.075 + 0.002
         288 +            return self._plan_pick_place(state, name, spot, bottom)
         289 +        # place target block
         290 +        tb = boxes["target_block"]
         291 +        return self._plan_pick_place(state, "target_block", (reg["x"], reg["y"]),
         292 +                                     reg["z"] + reg["hz"] + 0.0005)
         293 +
         294 +    # ---------------------------------------------------------------- control
         295 +    def get_action(self, state):
         296 +        q = self._q(state)
         297 +        act = np.zeros(11, dtype=np.float32)
         298 +        # detect rejected motion
         299 +        rejected = False
         300 +        if self.last_cmd is not None and self.last_q is not None:
         301 +            if np.max(np.abs(self.last_cmd)) > 1e-6 and np.max(np.abs(q - self.last_q)) < 1e-7:
         302 +                rejected = True
         303 +        self.last_q = q.copy()
         304 +        self.last_cmd = None
         305 +
         306 +        if rejected and self.cur is not None and self.cur[0] == "move":
         307 +            self._handle_reject(state)
         308 +
         309 +        for _ in range(20):
         310 +            if self.cur is None:
         311 +                if not self.segs:
         312 +                    self.segs = self._replan(state)
         313 +                self.cur = self.segs.pop(0)
         314 +                self.stuck = 0
         315 +            seg = self.cur
         316 +            if seg[0] == "grip":
         317 +                act[10] = seg[1]
         318 +                self.cur = None
         319 +                self.last_cmd = np.zeros(7)
         320 +                return act
         321 +            # move segment
         322 +            goal, yaw = seg[1], seg[2]
         323 +            T, _, _ = fk(q)
         324 +            if yaw is None:
         325 +                Rt = T[:3, :3]
         326 +                Rt = down_R(np.arctan2(T[1, 0], T[0, 0])) if abs(T[2, 2] + 1) < 0.2 else Rt
         327 +            else:
         328 +                Rt = down_R(yaw)
         329 +            p = T[:3, 3]
         330 +            d = goal - p
         331 +            rerr = np.linalg.norm(_rotvec(Rt @ T[:3, :3].T))
         332 +            if np.linalg.norm(d) < 5e-4 and rerr < 2e-3:
         333 +                self.cur = None
         334 +                continue
         335 +            # intermediate cartesian target
         336 +            step = 0.04
         337 +            nd = np.linalg.norm(d)
         338 +            tgt = goal if nd < step else p + d * step / nd
         339 +            qt, err = ik(q, tgt, Rt)
         340 +            dq = qt - q
         341 +            m = np.max(np.abs(dq))
         342 +            if m > 0.2:
         343 +                dq *= 0.2 / m
         344 +            if m < 1e-6:
         345 +                self.cur = None
         346 +                continue
         347 +            act[3:10] = dq.astype(np.float32)
         348 +            self.last_cmd = dq
         349 +            return act
         350 +        return act
         351 +
         352 +    def _handle_reject(self, state):
         353 +        seg = self.cur
         354 +        tag = seg[3] if len(seg) > 3 else None
         355 +        self.stuck += 1
         356 +        if tag == "place_descend":
         357 +            # contact: just release here
         358 +            self.cur = None
         359 +            return
         360 +        if tag == "grasp_descend":
         361 +            # can't reach grasp pose: grasp at current height if fingertips reach object, else retry
         362 +            name = seg[4]
         363 +            boxes = self._boxes(state)
         364 +            b = boxes[name]
         365 +            T, _, _ = fk(self._q(state))
         366 +            tip = T[2, 3] - FINGER
         367 +            if tip < b["z"] + b["hz"] - 0.006:
         368 +                self.cur = None
         369 +                return
         370 +            self.fail[name] = self.fail.get(name, 0) + 1
         371 +            T, _, _ = fk(self._q(state))
         372 +            self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.08]), None)]
         373 +            self.cur = None
         374 +            return
         375 +        # generic: go up a bit, then replan
         376 +        T, _, _ = fk(self._q(state))
         377 +        self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.03]), None)]
         378 +        self.cur = None
diff --git a/probe_base_11.py b/probe_base_11.py
new file mode 100644
index 0000000..ff321d0
--- /dev/null
+++ b/probe_base_11.py
@@ -0,0 +1,49 @@
           1 +from env_client import make_env
           2 +from probe_base_fk import fk
           3 +import numpy as np
           4 +def ik(p, q, tool=0.12, it=300):
           5 +    q=np.array(q,float)
           6 +    for _ in range(it):
           7 +        def err(q):
           8 +            T=fk(q,tool); return np.concatenate([T[:3,3]-p, 0.3*(T[:3,2]-np.array([0,0,-1]))])
           9 +        e=err(q)
          10 +        if np.linalg.norm(e)<1e-5: break
          11 +        J=np.zeros((6,7))
          12 +        for i in range(7):
          13 +            dq=np.zeros(7); dq[i]=1e-5; J[:,i]=(err(q+dq)-e)/1e-5
          14 +        q=q-J.T@np.linalg.solve(J@J.T+1e-4*np.eye(6),e)
          15 +    return q, np.linalg.norm(e)
          16 +env=make_env()
          17 +def goto(obs,R,qt):
          18 +    """move joints to qt in steps<=0.1; return (obs, rejected_flag)"""
          19 +    for _ in range(200):
          20 +        q=np.array([obs.get(R,f"joint_{i}") for i in range(1,8)])
          21 +        d=np.clip(qt-q,-0.1,0.1)
          22 +        if np.abs(d).max()<1e-6: return obs,False
          23 +        a=np.zeros(11,np.float32); a[3:10]=d; a[10]=1
          24 +        obs,*_=env.step(a)
          25 +        q2=np.array([obs.get(R,f"joint_{i}") for i in range(1,8)])
          26 +        if np.allclose(q2,q): return obs,True
          27 +    return obs,False
          28 +def objs(obs): return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name!="robot"}
          29 +for seed in [1,0,2]:
          30 +    obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot")
          31 +    base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
          32 +    TB=obs.get_object_from_name("target_block")
          33 +    tb=np.array([obs.get(TB,"pose_x"),obs.get(TB,"pose_y")])
          34 +    for label,xy in [("above block",tb),("empty spot",tb+np.array([0,0.15 if tb[1]<0 else -0.15]))]:
          35 +        obs,_=env.reset(seed=seed); o0=objs(obs)
          36 +        rel=xy-base
          37 +        qh=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2])
          38 +        obs,rj=goto(obs,R,qh)
          39 +        q=qh; last=None
          40 +        for zr in np.arange(0.40,-0.6,-0.01):
          41 +            qt,err=ik(np.array([rel[0],rel[1],zr]),q)
          42 +            if err>1e-3: print("ik fail",zr); break
          43 +            obs,rj=goto(obs,R,qt); q=qt
          44 +            if rj: break
          45 +            last=zr
          46 +        o=objs(obs)
          47 +        mv={k:np.round(o[k]-o0[k],3) for k in o0 if np.abs(o[k]-o0[k]).max()>1e-6}
          48 +        print(f"seed{seed} {label} xy={np.round(xy,3)}: lowest ok z_rel={last}, rejected={rj}, moved={mv}")
          49 +env.close()
diff --git a/probe_base_12.py b/probe_base_12.py
new file mode 100644
index 0000000..2a151b6
--- /dev/null
+++ b/probe_base_12.py
@@ -0,0 +1,17 @@
           1 +import numpy as np, sys
           2 +sys.argv=['x']
           3 +exec(open('probe_base_11.py').read().split("for seed in")[0])
           4 +for seed in [1,0]:
           5 +    obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot"); o0=objs(obs)
           6 +    base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
           7 +    TB=obs.get_object_from_name("target_block"); tb=np.array([obs.get(TB,"pose_x"),obs.get(TB,"pose_y")])
           8 +    rel=tb-base; q=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2]); obs,_=goto(obs,R,q)
           9 +    for zr in np.arange(0.40,0.105,-0.01):
          10 +        q,_=ik(np.array([rel[0],rel[1],zr]),q); obs,rj=goto(obs,R,q)
          11 +    # scan xy offsets at this height for grasp
          12 +    a=np.zeros(11,np.float32); a[10]=-1
          13 +    obs,*_=env.step(a); print("seed",seed,"close at block: finger",obs.get(R,"finger_state"),"grasp",obs.get(R,"grasp_active"), "TB grasp",obs.get(TB,"grasp_active"))
          14 +    for zr in np.arange(0.11,0.3,0.02):
          15 +        q,_=ik(np.array([rel[0],rel[1],zr]),q); obs,rj=goto(obs,R,q)
          16 +    o=objs(obs); print(" after lift moved:",{k:np.round(o[k]-o0[k],3) for k in o0 if np.abs(o[k]-o0[k]).max()>1e-6})
          17 +env.close()
diff --git a/probe_base_13.py b/probe_base_13.py
new file mode 100644
index 0000000..fb11a0d
--- /dev/null
+++ b/probe_base_13.py
@@ -0,0 +1,7 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env(); obs,_=env.reset(seed=1); R=obs.get_object_from_name("robot")
           4 +for g in [-1,-1,-1,1,1,0,-0.3,-0.6]:
           5 +    a=np.zeros(11,np.float32); a[10]=g; obs,r,te,tr,info=env.step(a)
           6 +    print(g, obs.get(R,"finger_state"), obs.get(R,"grasp_active"), r, te, info)
           7 +env.close()
diff --git a/probe_base_fk.py b/probe_base_fk.py
new file mode 100644
index 0000000..312a7e7
--- /dev/null
+++ b/probe_base_fk.py
@@ -0,0 +1,16 @@
           1 +import numpy as np
           2 +D=[(np.pi/2,-(0.1564+0.1284),0),(np.pi/2,-(0.0054+0.0064),np.pi),(np.pi/2,-(0.2104+0.2104),np.pi),
           3 +   (np.pi/2,-(0.0064+0.0064),np.pi),(np.pi/2,-(0.2084+0.1059),np.pi),(np.pi/2,0,np.pi),(np.pi,-(0.1059+0.0615),np.pi)]
           4 +def dh(al,d,th):
           5 +    ca,sa,ct,st=np.cos(al),np.sin(al),np.cos(th),np.sin(th)
           6 +    return np.array([[ct,-st*ca,st*sa,0],[st,ct*ca,-ct*sa,0],[0,sa,ca,d],[0,0,0,1]])
           7 +def fk(q,tool=0.0):
           8 +    T=dh(np.pi,0,0)
           9 +    for (al,d,off),qi in zip(D,q): T=T@dh(al,d,qi+off)
          10 +    T=T@np.array([[1,0,0,0],[0,1,0,0],[0,0,1,tool],[0,0,0,1]])
          11 +    return T
          12 +if __name__=="__main__":
          13 +    q0=[0,-0.35,-np.pi,-2.5,0,-0.87,np.pi/2]
          14 +    for j2 in [-0.35,0.0,0.35,0.7]:
          15 +        q=list(q0); q[1]=j2; T=fk(q,0.12); print(j2, np.round(T[:3,3],3), "zaxis",np.round(T[:3,2],2))
          16 +    print("home",np.round(fk([0,0.26,np.pi,-2.27,0,0.96,np.pi/2],0.12)[:3,3],3))
diff --git a/probe_place.py b/probe_place.py
new file mode 100644
index 0000000..d5bcb52
--- /dev/null
+++ b/probe_place.py
@@ -0,0 +1,38 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +env = make_env()
           5 +R=None
           6 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           7 +def goto(obs, qt, grip=0.0, maxn=40):
           8 +    for _ in range(maxn):
           9 +        q = q_of(obs); d = qt - q
          10 +        if np.max(np.abs(d)) < 1e-4: break
          11 +        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2); a[10] = grip
          12 +        obs2, r, te, tr, info = env.step(a)
          13 +        if np.allclose(q_of(obs2), q): return obs2, False
          14 +        obs = obs2
          15 +    return obs, True
          16 +base=(0,0,0); yaw=1.5708
          17 +obs, info = env.reset(seed=0)
          18 +R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
          19 +bx, by = obs.get(B,'pose_x'), obs.get(B,'pose_y')
          20 +q=q_of(obs)
          21 +for z in [0.4,0.33,0.255]:
          22 +    qt,e = ik(q, np.array([bx,by,z]), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs)
          23 +a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a)
          24 +tx,ty=0.3,-0.1
          25 +for p in [(bx,by,0.35),(tx,ty,0.35),(tx,ty,0.30),(tx,ty,0.27),(tx,ty,0.26)]:
          26 +    qt,e = ik(q, np.array(p), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs); print(p, ok, np.round(obs.data[B][:3],4))
          27 +for z in np.arange(0.26,0.24,-0.001):
          28 +    qt,e = ik(q, np.array([tx,ty,z]), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs)
          29 +    if not ok: print("stop", z, np.round(obs.data[B][:3],4)); break
          30 +a=np.zeros(11,np.float32); a[10]=1; obs,r,te,*_=env.step(a); print("open", np.round(obs.data[R][10:12],3), np.round(obs.data[B][:3],4), r, te)
          31 +qt,e = ik(q, np.array([tx,ty,0.35]), down_R(yaw), base); obs,ok=goto(obs,qt); print("up", ok, np.round(obs.data[B][:3],4))
          32 +# regrasp and release in the air
          33 +qt,e = ik(q_of(obs), np.array([tx,ty,ee_pose(q,base)[2,3]]), down_R(yaw), base); obs,ok=goto(obs,qt)
          34 +a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a); print("regrasp", obs.data[R][11])
          35 +q=q_of(obs); qt,e = ik(q, np.array([tx,ty,0.33]), down_R(yaw), base); obs,ok=goto(obs,qt)
          36 +a=np.zeros(11,np.float32); a[10]=1; obs,*_=env.step(a); print("release air", np.round(obs.data[B][:3],4))
          37 +obs,*_=env.step(np.zeros(11,np.float32)); print("next", np.round(obs.data[B][:3],4))
          38 +env.close()
diff --git a/probe_tab_ik.py b/probe_tab_ik.py
new file mode 100644
index 0000000..28cc961
--- /dev/null
+++ b/probe_tab_ik.py
@@ -0,0 +1,16 @@
           1 +from kin import *
           2 +import numpy as np
           3 +q0=np.array([0,0.26,3.14,-2.27,0,0.96,1.57])  # generic seed
           4 +xs=np.round(np.arange(-0.3,0.95,0.05),3); ys=np.round(np.arange(-0.8,0.85,0.05),3)
           5 +for yaw in [0,np.pi/2]:
           6 +  for z in [0.23,0.40]:
           7 +    print("yaw",round(yaw,2),"z",z,"  cols y from",ys[0],"to",ys[-1])
           8 +    for x in xs[::-1]:
           9 +        row=""
          10 +        for y in ys:
          11 +            best=9
          12 +            for s in [q0, np.array([0,0.5,0,1.8,0,1.0,0]), np.array([np.arctan2(y,x),0.3,3.14,-2.0,0,0.9,1.57])]:
          13 +                q,e=ik(s,np.array([x,y,z]),down_R(yaw),(0,0,0)); best=min(best,e)
          14 +                if best<1e-3: break
          15 +            row+="#" if best<1e-3 else "."
          16 +        print("%+.2f "%x+row)
diff --git a/probe_tab_info.py b/probe_tab_info.py
new file mode 100644
index 0000000..3e972d5
--- /dev/null
+++ b/probe_tab_info.py
@@ -0,0 +1,20 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np
           4 +env = make_env()
           5 +for seed in [0,1,2]:
           6 +    obs, info = env.reset(seed=seed)
           7 +    for o in obs:
           8 +        pass
           9 +    print(type(obs))
          10 +    try:
          11 +        names=[o.name for o in obs]
          12 +    except Exception as e: names=None; print(e)
          13 +    print(names)
          14 +    for n in names or []:
          15 +        o=obs.get_object_from_name(n)
          16 +        f=[k for k in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z'] ]
          17 +        try: print(n,[round(float(obs.get(o,k)),3) for k in f])
          18 +        except Exception as e: print(n,e)
          19 +st=env.get_state(); print(type(st), str(st)[:300])
          20 +env.close()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..33858d2
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,24 @@
           1 +import sys, time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +def run(seed, verbose=False):
           5 +    env = make_env()
           6 +    obs, info = env.reset(seed=seed)
           7 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           8 +    t = time.time(); ap.reset(obs, info)
           9 +    ret = 0; steps = 0; term = False
          10 +    for steps in range(1, env.max_steps + 1):
          11 +        a = ap.get_action(obs)
          12 +        obs, r, term, trunc, info = env.step(a)
          13 +        ret += r
          14 +        if term or trunc: break
          15 +    dt = time.time() - t
          16 +    env.close()
          17 +    return seed, info.get('object_count'), term, steps, round(dt, 1)
          18 +if __name__ == "__main__":
          19 +    from concurrent.futures import ThreadPoolExecutor
          20 +    seeds = list(range(int(sys.argv[1]), int(sys.argv[2])))
          21 +    with ThreadPoolExecutor(8) as ex:
          22 +        res = list(ex.map(run, seeds))
          23 +    for r in res: print(r)
          24 +    print("success", sum(r[2] for r in res), "/", len(res), "mean steps", np.mean([r[3] for r in res]))
```

</details>

<a id="C004"></a>
### C004 · joint limits fix, bigger cartesian step

Commit `1afb5b99782877bdaf42d2220295db45314a0a6e`; parents: c07147037442a45ce9df9f7ff70d39f39b52203b. Recorded author date: 2026-09-30T20:55:50+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0451](01_timeline.md#E0451): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_1afb5b9_approach.py) · [Exact all-file diff](evidence/diffs/C004_1afb5b9.diff)

[Previous saved controller snapshot](evidence/versions/C003_c071470_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 744534b..d91a176 100644
--- a/approach.py
+++ b/approach.py
@@ -34,7 +34,7 @@ FINGER = 0.155          # EE frame -> fingertip distance (along tool z)
   34     34  FINGER_OFF = 0.05       # finger centre offset from tool axis along closing direction
   35     35  
   36     36  # joint limits (Kinova Gen3); None = continuous
   37        -_LIM = [None, (-2.24, 2.24), None, (-2.57, 2.57), None, (-2.09, 2.09), None]
          37 +_LIM = [None, (-2.38, 2.38), None, (-2.63, 2.63), None, (-2.2, 2.2), None]
   38     38  
   39     39  
   40     40  def fk(q):
@@ -333,7 +333,7 @@ class GeneratedApproach:
  333    333                  self.cur = None
  334    334                  continue
  335    335              # intermediate cartesian target
  336        -            step = 0.04
         336 +            step = 0.08
  337    337              nd = np.linalg.norm(d)
  338    338              tgt = goal if nd < step else p + d * step / nd
  339    339              qt, err = ik(q, tgt, Rt)
diff --git a/dbg_run.py b/dbg_run.py
new file mode 100644
index 0000000..bbc2a19
--- /dev/null
+++ b/dbg_run.py
@@ -0,0 +1,20 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach, fk
           4 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 1000
           5 +env = make_env(); obs, info = env.reset(seed=seed)
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +bx = ap._boxes(obs)
           8 +for n,b in sorted(bx.items()): print(n, {k: round(v,3) for k,v in b.items()})
           9 +lastseg=None
          10 +for t in range(N):
          11 +    a = ap.get_action(obs)
          12 +    seg = ap.cur
          13 +    key = None if seg is None else (seg[0], tuple(np.round(seg[1],3)) if seg[0]=='move' else seg[1], seg[2] if seg[0]=='move' and seg[2] is None else (round(seg[2],2) if seg[0]=='move' else seg[2]), seg[3] if len(seg)>3 else '')
          14 +    obs, r, term, trunc, info = env.step(a)
          15 +    q = ap._q(obs); T,_,_ = fk(q)
          16 +    rob = ap._robot(obs)
          17 +    if key != lastseg or np.allclose(q, ap.last_q):
          18 +        print(t, key, "ee", np.round(T[:3,3],3), "grasp", obs.get(rob,'grasp_active'), "REJ" if np.allclose(q, ap.last_q) and np.any(a[3:10]!=0) else "")
          19 +        lastseg = key
          20 +    if term: print("DONE", t); break
diff --git a/probe_base_14.py b/probe_base_14.py
new file mode 100644
index 0000000..2b6f65a
--- /dev/null
+++ b/probe_base_14.py
@@ -0,0 +1,23 @@
           1 +import numpy as np
           2 +exec(open('probe_base_11.py').read().split("for seed in")[0])
           3 +for seed in [1]:
           4 +    obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot"); o0=objs(obs)
           5 +    base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
           6 +    TB=obs.get_object_from_name("target_block"); tb=np.array([obs.get(TB,"pose_x"),obs.get(TB,"pose_y")])
           7 +    rel=tb-base; q=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2]); obs,_=goto(obs,R,q)
           8 +    z=0.125
           9 +    for zr in np.arange(0.40,z,-0.01):
          10 +        q,_=ik(np.array([rel[0]-0.12,rel[1],zr]),q); obs,rj=goto(obs,R,q)
          11 +    rejs=[];grasps=[]
          12 +    for dy in np.arange(-0.1,0.101,0.025):
          13 +        for dx in np.arange(-0.12,0.121,0.01):
          14 +            q,_=ik(np.array([rel[0]+dx,rel[1]+dy,z]),q); obs,rj=goto(obs,R,q)
          15 +            if rj: rejs.append((round(dx,3),round(dy,3)))
          16 +            a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a)
          17 +            if obs.get(R,"grasp_active")>0.5 or obs.get(R,"finger_state")!=0: grasps.append((round(dx,3),round(dy,3),obs.get(R,"finger_state")))
          18 +            a[10]=1; obs,*_=env.step(a)
          19 +        q,_=ik(np.array([rel[0]-0.12,rel[1]+dy+0.025,z+0.1]),q); obs,_=goto(obs,R,q)
          20 +    o=objs(obs)
          21 +    print("rejections",len(rejs),rejs[:20]); print("grasps",grasps[:10])
          22 +    print("moved:",{k:np.round(o[k]-o0[k],3) for k in o0 if np.abs(o[k]-o0[k]).max()>1e-6})
          23 +env.close()
diff --git a/probe_base_15.py b/probe_base_15.py
new file mode 100644
index 0000000..ef36f7b
--- /dev/null
+++ b/probe_base_15.py
@@ -0,0 +1,16 @@
           1 +import numpy as np
           2 +exec(open('probe_base_11.py').read().split("for seed in")[0])
           3 +seed=1
           4 +obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot")
           5 +base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
           6 +TB=obs.get_object_from_name("target_block"); tb0=np.array(obs.data[TB][:7],float)
           7 +rel=tb0[:2]-base; q=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2]); obs,rj=goto(obs,R,q); print("home rej",rj)
           8 +for zr in np.arange(0.40,0.125,-0.01):
           9 +    q,_=ik(np.array([rel[0]-0.12,rel[1],zr]),q); obs,rj=goto(obs,R,q)
          10 +    if rj: print("rej descending",zr)
          11 +for dx in np.arange(-0.12,0.121,0.01):
          12 +    q,_=ik(np.array([rel[0]+dx,rel[1],0.125]),q); obs,rj=goto(obs,R,q)
          13 +    tb=np.array(obs.data[TB][:7],float)
          14 +    print(f"dx={dx:+.2f} rej={rj} tb_delta={np.round(tb-tb0,4)} fs={obs.get(R,'finger_state'):.3f}")
          15 +    if rj: break
          16 +env.close()
diff --git a/probe_base_16.py b/probe_base_16.py
new file mode 100644
index 0000000..4ef389d
--- /dev/null
+++ b/probe_base_16.py
@@ -0,0 +1,19 @@
           1 +import numpy as np
           2 +exec(open('probe_base_11.py').read().split("for seed in")[0])
           3 +def run(seed,dy,z):
           4 +    obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot")
           5 +    base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
           6 +    TB=obs.get_object_from_name("target_block"); tb0=np.array(obs.data[TB][:7],float)
           7 +    rel=tb0[:2]-base+np.array([0,dy]); q=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2]); obs,rj=goto(obs,R,q)
           8 +    for zr in np.arange(0.40,z,-0.01):
           9 +        q,_=ik(np.array([rel[0]-0.12,rel[1],zr]),q); obs,rj=goto(obs,R,q)
          10 +        if rj: return f"rej descending {zr:.2f}"
          11 +    for dx in np.arange(-0.12,0.121,0.01):
          12 +        q,_=ik(np.array([rel[0]+dx,rel[1],z]),q); obs,rj=goto(obs,R,q)
          13 +        tb=np.array(obs.data[TB][:7],float)
          14 +        if rj or np.abs(tb-tb0).max()>1e-6: return f"stop dx={dx:+.2f} rej={rj} tb_delta={np.round(tb-tb0,4)}"
          15 +    return "passed through all dx"
          16 +for z in [0.13,0.15,0.17,0.2]:
          17 +    for dy in [0.0,-0.12]:
          18 +        print(f"z={z} dy={dy}:",run(1,dy,z))
          19 +env.close()
diff --git a/probe_tab_desc.py b/probe_tab_desc.py
new file mode 100644
index 0000000..b54e8aa
--- /dev/null
+++ b/probe_tab_desc.py
@@ -0,0 +1,55 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); x=float(sys.argv[3])
           5 +ys=np.round(np.arange(-0.6,0.6001,0.05),3)
           6 +if len(sys.argv)>4: ys=np.round(np.arange(float(sys.argv[4]),float(sys.argv[5])+1e-6,float(sys.argv[6])),3)
           7 +env = make_env()
           8 +B=(0,0,0); Rd=down_R(yaw)
           9 +def reset():
          10 +    o,_=env.reset(seed=seed); return o
          11 +obs=reset(); R=obs.get_object_from_name("robot")
          12 +objs=[]
          13 +for n in ['target_block','target_region','obstruction0','obstruction1','obstruction2','obstruction3']:
          14 +    try:
          15 +        o=obs.get_object_from_name(n); objs.append((obs.get(o,'pose_x'),obs.get(o,'pose_y')))
          16 +    except Exception: pass
          17 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
          18 +def goto(obs, qt, maxn=40):
          19 +    for _ in range(maxn):
          20 +        q=q_of(obs); d=qt-q
          21 +        if np.max(np.abs(d))<1e-4: break
          22 +        a=np.zeros(11,np.float32); a[3:10]=np.clip(d,-.2,.2)
          23 +        obs2,r,te,tr,_=env.step(a)
          24 +        if np.allclose(q_of(obs2),q): return obs2,False
          25 +        obs=obs2
          26 +    return obs,True
          27 +def moveto(obs,p):
          28 +    q=q_of(obs); qt,e=ik(q,np.array(p),Rd,B)
          29 +    if e>1e-3: return obs,False,e
          30 +    obs,ok=goto(obs,qt); return obs,ok,e
          31 +res=[]
          32 +for y in ys:
          33 +    if any(np.hypot(x-ox,y-oy)<0.09 for ox,oy in objs): res.append('O'); continue
          34 +    q=q_of(obs)
          35 +    _,e1=ik(q,np.array([x,y,0.36]),Rd,B); _,e2=ik(q,np.array([x,y,0.23]),Rd,B)
          36 +    if e1>1e-3 and e2>1e-3: res.append('N'); continue
          37 +    # up then across
          38 +    p=ee_pose(q,B)[:3,3]
          39 +    obs,ok,_=moveto(obs,[p[0],p[1],0.36])
          40 +    good=True
          41 +    for t in np.linspace(0,1,6)[1:]:
          42 +        obs,ok,e=moveto(obs,[p[0]+t*(x-p[0]),p[1]+t*(y-p[1]),0.36])
          43 +        if not ok: good=False; break
          44 +    if not good:
          45 +        obs=reset(); obs,ok,e=moveto(obs,[x,y,0.36])
          46 +        if not ok: res.append('T'); obs=reset(); continue
          47 +    stop=None; last=0.36
          48 +    for z in np.round(np.arange(0.35,0.0999,-0.01),3):
          49 +        obs,ok,e=moveto(obs,[x,y,z])
          50 +        if e>1e-3: stop='n%d'%round(z*100); break
          51 +        if not ok: stop='%d'%round(z*100); break
          52 +    res.append(stop if stop else 'F')
          53 +    for z in np.arange(ee_pose(q_of(obs),B)[2,3],0.37,0.02): obs,ok,e=moveto(obs,[x,y,min(z,0.36)])
          54 +print("%+.3f "%x+" ".join("%4s"%r for r in res), flush=True)
          55 +env.close()
diff --git a/probe_tab_ref.py b/probe_tab_ref.py
new file mode 100644
index 0000000..3dae27f
--- /dev/null
+++ b/probe_tab_ref.py
@@ -0,0 +1,55 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); x=float(sys.argv[3])
           5 +ys=np.round(np.arange(-0.6,0.6001,0.05),3); ZMIN=0.0999
           6 +if len(sys.argv)>4: ys=np.round(np.arange(float(sys.argv[4]),float(sys.argv[5])+1e-6,float(sys.argv[6])),3)
           7 +env = make_env()
           8 +B=(0,0,0); Rd=down_R(yaw)
           9 +def reset():
          10 +    o,_=env.reset(seed=seed); return o
          11 +obs=reset(); R=obs.get_object_from_name("robot")
          12 +objs=[]
          13 +for n in ['target_block','target_region','obstruction0','obstruction1','obstruction2','obstruction3']:
          14 +    try:
          15 +        o=obs.get_object_from_name(n); objs.append((obs.get(o,'pose_x'),obs.get(o,'pose_y')))
          16 +    except Exception: pass
          17 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
          18 +def goto(obs, qt, maxn=40):
          19 +    for _ in range(maxn):
          20 +        q=q_of(obs); d=qt-q
          21 +        if np.max(np.abs(d))<1e-4: break
          22 +        a=np.zeros(11,np.float32); a[3:10]=np.clip(d,-.2,.2)
          23 +        obs2,r,te,tr,_=env.step(a)
          24 +        if np.allclose(q_of(obs2),q): return obs2,False
          25 +        obs=obs2
          26 +    return obs,True
          27 +def moveto(obs,p):
          28 +    q=q_of(obs); qt,e=ik(q,np.array(p),Rd,B)
          29 +    if e>1e-3: return obs,False,e
          30 +    obs,ok=goto(obs,qt); return obs,ok,e
          31 +res=[]
          32 +for y in ys:
          33 +    if any(np.hypot(x-ox,y-oy)<0.09 for ox,oy in objs): res.append('O'); continue
          34 +    q=q_of(obs)
          35 +    _,e1=ik(q,np.array([x,y,0.36]),Rd,B); _,e2=ik(q,np.array([x,y,0.23]),Rd,B)
          36 +    if e1>1e-3 and e2>1e-3: res.append('N'); continue
          37 +    # up then across
          38 +    p=ee_pose(q,B)[:3,3]
          39 +    obs,ok,_=moveto(obs,[p[0],p[1],0.36])
          40 +    good=True
          41 +    for t in np.linspace(0,1,6)[1:]:
          42 +        obs,ok,e=moveto(obs,[p[0]+t*(x-p[0]),p[1]+t*(y-p[1]),0.36])
          43 +        if not ok: good=False; break
          44 +    if not good:
          45 +        obs=reset(); obs,ok,e=moveto(obs,[x,y,0.36])
          46 +        if not ok: res.append('T'); obs=reset(); continue
          47 +    stop=None; last=0.36
          48 +    for z in np.round(np.arange(0.35,ZMIN,-0.01),3):
          49 +        obs,ok,e=moveto(obs,[x,y,z])
          50 +        if e>1e-3: stop='n%d'%round(z*100); break
          51 +        if not ok: stop='%d'%round(z*100); break
          52 +    res.append(stop if stop else 'F')
          53 +    for z in np.arange(ee_pose(q_of(obs),B)[2,3],0.37,0.02): obs,ok,e=moveto(obs,[x,y,min(z,0.36)])
          54 +print("%+.3f "%x+" ".join("%4s"%r for r in res), flush=True)
          55 +env.close()
diff --git a/probe_tab_run.sh b/probe_tab_run.sh
new file mode 100644
index 0000000..c88e338
--- /dev/null
+++ b/probe_tab_run.sh
@@ -0,0 +1,5 @@
           1 +yaw=$1; seed=$2; out=$3
           2 +for x in $(seq -0.10 0.05 0.70); do
           3 +  /opt/robocode-strict/bin/python probe_tab_desc.py $seed $yaw $x >> $out.tmp 2>&1 &
           4 +done; wait
           5 +sort -r -n -k1 $out.tmp > $out
diff --git a/probe_tab_y0_s0.txt b/probe_tab_y0_s0.txt
new file mode 100644
index 0000000..08092a2
--- /dev/null
+++ b/probe_tab_y0_s0.txt
@@ -0,0 +1,101 @@
           1 +Traceback (most recent call last):
           2 +Traceback (most recent call last):
           3 +Traceback (most recent call last):
           4 +Traceback (most recent call last):
           5 +Traceback (most recent call last):
           6 +Traceback (most recent call last):
           7 +Traceback (most recent call last):
           8 +RuntimeError: Connection to the environment server was closed
           9 +RuntimeError: Connection to the environment server was closed
          10 +RuntimeError: Connection to the environment server was closed
          11 +RuntimeError: Connection to the environment server was closed
          12 +RuntimeError: Connection to the environment server was closed
          13 +RuntimeError: Connection to the environment server was closed
          14 +RuntimeError: Connection to the environment server was closed
          15 ++0.650    N    N    N    N    N    N    T    T    F    F    F    F    F    F    F    F    F    T    T    N    N    N    N    N    N
          16 ++0.600    N    N    N    N    T    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    T    N    N    N    N
          17 ++0.500    N    N    T    F   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   11    T    N    N
          18 ++0.350    F    F    F    F   22   22   22   22   22   22   22   22   22   22    O    O    O    O   22   22   22   11    F    F    F
          19 ++0.200    F    F    F    F   22   22   22   22   22   22   22   22   22   22   22   22    O    O    O   22   22   11    F    F    F
          20 ++0.150    F    F    F    F   22   22   22   22   22   22   22   24   25   23   22    O    O    O    O   22   22   11    F    F    F
          21 ++0.050    F    F    F    F   22   22   22   22   22   25   29    T    T    T    T    O    O    O    O   22   22    F    F    F    F
          22 ++0.000    F    F    F    F    F    F    F    F    F   26   29    T    T    T    T   24    F    F    F    F    F    F    F    F    F
          23 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          24 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          25 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          26 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          27 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          28 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          29 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          30 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          31 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          32 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          33 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          34 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          35 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          36 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          37 +  File "/sandbox/env_client.py", line 525, in reset
          38 +  File "/sandbox/env_client.py", line 525, in reset
          39 +  File "/sandbox/env_client.py", line 525, in reset
          40 +  File "/sandbox/env_client.py", line 525, in reset
          41 +  File "/sandbox/env_client.py", line 525, in reset
          42 +  File "/sandbox/env_client.py", line 525, in reset
          43 +  File "/sandbox/env_client.py", line 525, in reset
          44 +  File "/sandbox/env_client.py", line 478, in _request
          45 +  File "/sandbox/env_client.py", line 478, in _request
          46 +  File "/sandbox/env_client.py", line 478, in _request
          47 +  File "/sandbox/env_client.py", line 478, in _request
          48 +  File "/sandbox/env_client.py", line 478, in _request
          49 +  File "/sandbox/env_client.py", line 478, in _request
          50 +  File "/sandbox/env_client.py", line 478, in _request
          51 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          52 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          53 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          54 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          55 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          56 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          57 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          58 +    raise RuntimeError("Connection to the environment server was closed")
          59 +    raise RuntimeError("Connection to the environment server was closed")
          60 +    raise RuntimeError("Connection to the environment server was closed")
          61 +    raise RuntimeError("Connection to the environment server was closed")
          62 +    raise RuntimeError("Connection to the environment server was closed")
          63 +    raise RuntimeError("Connection to the environment server was closed")
          64 +    raise RuntimeError("Connection to the environment server was closed")
          65 +    obs=reset(); R=obs.get_object_from_name("robot")
          66 +    obs=reset(); R=obs.get_object_from_name("robot")
          67 +    obs=reset(); R=obs.get_object_from_name("robot")
          68 +    obs=reset(); R=obs.get_object_from_name("robot")
          69 +    obs=reset(); R=obs.get_object_from_name("robot")
          70 +    obs=reset(); R=obs.get_object_from_name("robot")
          71 +    obs=reset(); R=obs.get_object_from_name("robot")
          72 +    o,_=env.reset(seed=seed); return o
          73 +    o,_=env.reset(seed=seed); return o
          74 +    o,_=env.reset(seed=seed); return o
          75 +    o,_=env.reset(seed=seed); return o
          76 +    o,_=env.reset(seed=seed); return o
          77 +    o,_=env.reset(seed=seed); return o
          78 +    o,_=env.reset(seed=seed); return o
          79 +        ^^^^^^^^^^^^^^^^^^^^
          80 +        ^^^^^^^^^^^^^^^^^^^^
          81 +        ^^^^^^^^^^^^^^^^^^^^
          82 +        ^^^^^^^^^^^^^^^^^^^^
          83 +        ^^^^^^^^^^^^^^^^^^^^
          84 +        ^^^^^^^^^^^^^^^^^^^^
          85 +        ^^^^^^^^^^^^^^^^^^^^
          86 +        ^^^^^^^
          87 +        ^^^^^^^
          88 +        ^^^^^^^
          89 +        ^^^^^^^
          90 +        ^^^^^^^
          91 +        ^^^^^^^
          92 +        ^^^^^^^
          93 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          94 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          95 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          96 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          97 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          98 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          99 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         100 +-0.050    F    F    F    F    F    F    F    F    F   25   29    T    T    T    T   23    F    F    F    F    F    F    F    F    F
         101 +-0.100    F    F    F    F    F    F    F    F    F   22   27    T    T    T    T   20   19    F    F    F    F    F    F    F    F
diff --git a/probe_tab_y0_s0.txt.tmp b/probe_tab_y0_s0.txt.tmp
new file mode 100644
index 0000000..61edf27
--- /dev/null
+++ b/probe_tab_y0_s0.txt.tmp
@@ -0,0 +1,101 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
           3 +    obs=reset(); R=obs.get_object_from_name("robot")
           4 +        ^^^^^^^
           5 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
           6 +    o,_=env.reset(seed=seed); return o
           7 +        ^^^^^^^^^^^^^^^^^^^^
           8 +  File "/sandbox/env_client.py", line 525, in reset
           9 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          10 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          11 +  File "/sandbox/env_client.py", line 478, in _request
          12 +    raise RuntimeError("Connection to the environment server was closed")
          13 +RuntimeError: Connection to the environment server was closed
          14 +Traceback (most recent call last):
          15 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          16 +    obs=reset(); R=obs.get_object_from_name("robot")
          17 +        ^^^^^^^
          18 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          19 +    o,_=env.reset(seed=seed); return o
          20 +        ^^^^^^^^^^^^^^^^^^^^
          21 +  File "/sandbox/env_client.py", line 525, in reset
          22 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          23 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          24 +  File "/sandbox/env_client.py", line 478, in _request
          25 +    raise RuntimeError("Connection to the environment server was closed")
          26 +RuntimeError: Connection to the environment server was closed
          27 +Traceback (most recent call last):
          28 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          29 +    obs=reset(); R=obs.get_object_from_name("robot")
          30 +        ^^^^^^^
          31 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          32 +    o,_=env.reset(seed=seed); return o
          33 +        ^^^^^^^^^^^^^^^^^^^^
          34 +  File "/sandbox/env_client.py", line 525, in reset
          35 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          36 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          37 +  File "/sandbox/env_client.py", line 478, in _request
          38 +    raise RuntimeError("Connection to the environment server was closed")
          39 +RuntimeError: Connection to the environment server was closed
          40 +Traceback (most recent call last):
          41 +Traceback (most recent call last):
          42 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          43 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          44 +    obs=reset(); R=obs.get_object_from_name("robot")
          45 +    obs=reset(); R=obs.get_object_from_name("robot")
          46 +        ^^^^^^^
          47 +        ^^^^^^^
          48 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          49 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          50 +    o,_=env.reset(seed=seed); return o
          51 +    o,_=env.reset(seed=seed); return o
          52 +        ^^^^^^^^^^^^^^^^^^^^
          53 +        ^^^^^^^^^^^^^^^^^^^^
          54 +  File "/sandbox/env_client.py", line 525, in reset
          55 +  File "/sandbox/env_client.py", line 525, in reset
          56 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          57 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          58 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          59 +  File "/sandbox/env_client.py", line 478, in _request
          60 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          61 +  File "/sandbox/env_client.py", line 478, in _request
          62 +    raise RuntimeError("Connection to the environment server was closed")
          63 +RuntimeError: Connection to the environment server was closed
          64 +    raise RuntimeError("Connection to the environment server was closed")
          65 +RuntimeError: Connection to the environment server was closed
          66 +Traceback (most recent call last):
          67 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          68 +    obs=reset(); R=obs.get_object_from_name("robot")
          69 +        ^^^^^^^
          70 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          71 +    o,_=env.reset(seed=seed); return o
          72 +        ^^^^^^^^^^^^^^^^^^^^
          73 +  File "/sandbox/env_client.py", line 525, in reset
          74 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          75 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          76 +  File "/sandbox/env_client.py", line 478, in _request
          77 +    raise RuntimeError("Connection to the environment server was closed")
          78 +RuntimeError: Connection to the environment server was closed
          79 +Traceback (most recent call last):
          80 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          81 +    obs=reset(); R=obs.get_object_from_name("robot")
          82 +        ^^^^^^^
          83 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          84 +    o,_=env.reset(seed=seed); return o
          85 +        ^^^^^^^^^^^^^^^^^^^^
          86 +  File "/sandbox/env_client.py", line 525, in reset
          87 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          88 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          89 +  File "/sandbox/env_client.py", line 478, in _request
          90 +    raise RuntimeError("Connection to the environment server was closed")
          91 +RuntimeError: Connection to the environment server was closed
          92 ++0.650    N    N    N    N    N    N    T    T    F    F    F    F    F    F    F    F    F    T    T    N    N    N    N    N    N
          93 ++0.500    N    N    T    F   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   11    T    N    N
          94 ++0.050    F    F    F    F   22   22   22   22   22   25   29    T    T    T    T    O    O    O    O   22   22    F    F    F    F
          95 ++0.600    N    N    N    N    T    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    T    N    N    N    N
          96 ++0.200    F    F    F    F   22   22   22   22   22   22   22   22   22   22   22   22    O    O    O   22   22   11    F    F    F
          97 ++0.350    F    F    F    F   22   22   22   22   22   22   22   22   22   22    O    O    O    O   22   22   22   11    F    F    F
          98 ++0.150    F    F    F    F   22   22   22   22   22   22   22   24   25   23   22    O    O    O    O   22   22   11    F    F    F
          99 ++0.000    F    F    F    F    F    F    F    F    F   26   29    T    T    T    T   24    F    F    F    F    F    F    F    F    F
         100 +-0.100    F    F    F    F    F    F    F    F    F   22   27    T    T    T    T   20   19    F    F    F    F    F    F    F    F
         101 +-0.050    F    F    F    F    F    F    F    F    F   25   29    T    T    T    T   23    F    F    F    F    F    F    F    F    F
diff --git a/probe_tab_y0_s1.txt b/probe_tab_y0_s1.txt
new file mode 100644
index 0000000..21a242e
--- /dev/null
+++ b/probe_tab_y0_s1.txt
@@ -0,0 +1,125 @@
           1 +Traceback (most recent call last):
           2 +Traceback (most recent call last):
           3 +Traceback (most recent call last):
           4 +Traceback (most recent call last):
           5 +Traceback (most recent call last):
           6 +Traceback (most recent call last):
           7 +Traceback (most recent call last):
           8 +Traceback (most recent call last):
           9 +Traceback (most recent call last):
          10 +RuntimeError: Connection to the environment server was closed
          11 +RuntimeError: Connection to the environment server was closed
          12 +RuntimeError: Connection to the environment server was closed
          13 +RuntimeError: Connection to the environment server was closed
          14 +RuntimeError: Connection to the environment server was closed
          15 +RuntimeError: Connection to the environment server was closed
          16 +RuntimeError: Connection to the environment server was closed
          17 +RuntimeError: Connection to the environment server was closed
          18 +RuntimeError: Connection to the environment server was closed
          19 ++0.600    N    N    N    N    T    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    T    N    N    N    N
          20 ++0.400    T    F    F    F   22   22   22   22    O    O    O   22   22   22   22   22   22   22   22   22   22   11    F    F    T
          21 ++0.350    F    F    F    F   22   22   22   22   22    O    O   22   22   22   22   22   22   22   22   22   22   11    F    F    F
          22 ++0.300    F    F    F    F   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   11    F    F    F
          23 ++0.200    F    F    F    F   22   22   22   22   22   22   22   22   22   22   22    O    O   22   22   22   22   11    F    F    F
          24 ++0.100    F    F    F    F   22   22   22   22   22   22   26    T    T    T   25    O    O    O   22   22   22   11    F    F    F
          25 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          26 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          27 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          28 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          29 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          30 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          31 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          32 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          33 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          34 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          35 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          36 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          37 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          38 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          39 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          40 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          41 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          42 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          43 +  File "/sandbox/env_client.py", line 525, in reset
          44 +  File "/sandbox/env_client.py", line 525, in reset
          45 +  File "/sandbox/env_client.py", line 525, in reset
          46 +  File "/sandbox/env_client.py", line 525, in reset
          47 +  File "/sandbox/env_client.py", line 525, in reset
          48 +  File "/sandbox/env_client.py", line 525, in reset
          49 +  File "/sandbox/env_client.py", line 525, in reset
          50 +  File "/sandbox/env_client.py", line 525, in reset
          51 +  File "/sandbox/env_client.py", line 525, in reset
          52 +  File "/sandbox/env_client.py", line 478, in _request
          53 +  File "/sandbox/env_client.py", line 478, in _request
          54 +  File "/sandbox/env_client.py", line 478, in _request
          55 +  File "/sandbox/env_client.py", line 478, in _request
          56 +  File "/sandbox/env_client.py", line 478, in _request
          57 +  File "/sandbox/env_client.py", line 478, in _request
          58 +  File "/sandbox/env_client.py", line 478, in _request
          59 +  File "/sandbox/env_client.py", line 478, in _request
          60 +  File "/sandbox/env_client.py", line 478, in _request
          61 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          62 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          63 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          64 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          65 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          66 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          67 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          68 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          69 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          70 +    raise RuntimeError("Connection to the environment server was closed")
          71 +    raise RuntimeError("Connection to the environment server was closed")
          72 +    raise RuntimeError("Connection to the environment server was closed")
          73 +    raise RuntimeError("Connection to the environment server was closed")
          74 +    raise RuntimeError("Connection to the environment server was closed")
          75 +    raise RuntimeError("Connection to the environment server was closed")
          76 +    raise RuntimeError("Connection to the environment server was closed")
          77 +    raise RuntimeError("Connection to the environment server was closed")
          78 +    raise RuntimeError("Connection to the environment server was closed")
          79 +    obs=reset(); R=obs.get_object_from_name("robot")
          80 +    obs=reset(); R=obs.get_object_from_name("robot")
          81 +    obs=reset(); R=obs.get_object_from_name("robot")
          82 +    obs=reset(); R=obs.get_object_from_name("robot")
          83 +    obs=reset(); R=obs.get_object_from_name("robot")
          84 +    obs=reset(); R=obs.get_object_from_name("robot")
          85 +    obs=reset(); R=obs.get_object_from_name("robot")
          86 +    obs=reset(); R=obs.get_object_from_name("robot")
          87 +    obs=reset(); R=obs.get_object_from_name("robot")
          88 +    o,_=env.reset(seed=seed); return o
          89 +    o,_=env.reset(seed=seed); return o
          90 +    o,_=env.reset(seed=seed); return o
          91 +    o,_=env.reset(seed=seed); return o
          92 +    o,_=env.reset(seed=seed); return o
          93 +    o,_=env.reset(seed=seed); return o
          94 +    o,_=env.reset(seed=seed); return o
          95 +    o,_=env.reset(seed=seed); return o
          96 +    o,_=env.reset(seed=seed); return o
          97 +        ^^^^^^^^^^^^^^^^^^^^
          98 +        ^^^^^^^^^^^^^^^^^^^^
          99 +        ^^^^^^^^^^^^^^^^^^^^
         100 +        ^^^^^^^^^^^^^^^^^^^^
         101 +        ^^^^^^^^^^^^^^^^^^^^
         102 +        ^^^^^^^^^^^^^^^^^^^^
         103 +        ^^^^^^^^^^^^^^^^^^^^
         104 +        ^^^^^^^^^^^^^^^^^^^^
         105 +        ^^^^^^^^^^^^^^^^^^^^
         106 +        ^^^^^^^
         107 +        ^^^^^^^
         108 +        ^^^^^^^
         109 +        ^^^^^^^
         110 +        ^^^^^^^
         111 +        ^^^^^^^
         112 +        ^^^^^^^
         113 +        ^^^^^^^
         114 +        ^^^^^^^
         115 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         116 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         117 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         118 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         119 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         120 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         121 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         122 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         123 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         124 +-0.050    F    F    F    F    F    F    F    F    F   25   29    T    T    T    T   23    F    F    F    F    F    F    F    F    F
         125 +-0.100    F    F    F    F    F    F    F    F    F   22   27    T    T    T    T   20   19    F    F    F    F    F    F    F    F
diff --git a/probe_tab_y0_s1.txt.tmp b/probe_tab_y0_s1.txt.tmp
new file mode 100644
index 0000000..6e3ae9a
--- /dev/null
+++ b/probe_tab_y0_s1.txt.tmp
@@ -0,0 +1,125 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
           3 +    obs=reset(); R=obs.get_object_from_name("robot")
           4 +        ^^^^^^^
           5 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
           6 +    o,_=env.reset(seed=seed); return o
           7 +        ^^^^^^^^^^^^^^^^^^^^
           8 +  File "/sandbox/env_client.py", line 525, in reset
           9 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          10 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          11 +  File "/sandbox/env_client.py", line 478, in _request
          12 +    raise RuntimeError("Connection to the environment server was closed")
          13 +RuntimeError: Connection to the environment server was closed
          14 +Traceback (most recent call last):
          15 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          16 +    obs=reset(); R=obs.get_object_from_name("robot")
          17 +        ^^^^^^^
          18 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          19 +    o,_=env.reset(seed=seed); return o
          20 +        ^^^^^^^^^^^^^^^^^^^^
          21 +  File "/sandbox/env_client.py", line 525, in reset
          22 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          23 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          24 +  File "/sandbox/env_client.py", line 478, in _request
          25 +    raise RuntimeError("Connection to the environment server was closed")
          26 +RuntimeError: Connection to the environment server was closed
          27 +Traceback (most recent call last):
          28 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          29 +    obs=reset(); R=obs.get_object_from_name("robot")
          30 +        ^^^^^^^
          31 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          32 +    o,_=env.reset(seed=seed); return o
          33 +        ^^^^^^^^^^^^^^^^^^^^
          34 +  File "/sandbox/env_client.py", line 525, in reset
          35 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          36 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          37 +  File "/sandbox/env_client.py", line 478, in _request
          38 +    raise RuntimeError("Connection to the environment server was closed")
          39 +RuntimeError: Connection to the environment server was closed
          40 +Traceback (most recent call last):
          41 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          42 +    obs=reset(); R=obs.get_object_from_name("robot")
          43 +        ^^^^^^^
          44 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          45 +    o,_=env.reset(seed=seed); return o
          46 +        ^^^^^^^^^^^^^^^^^^^^
          47 +  File "/sandbox/env_client.py", line 525, in reset
          48 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          49 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          50 +  File "/sandbox/env_client.py", line 478, in _request
          51 +    raise RuntimeError("Connection to the environment server was closed")
          52 +RuntimeError: Connection to the environment server was closed
          53 +Traceback (most recent call last):
          54 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          55 +Traceback (most recent call last):
          56 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          57 +Traceback (most recent call last):
          58 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          59 +    obs=reset(); R=obs.get_object_from_name("robot")
          60 +        ^^^^^^^
          61 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          62 +    o,_=env.reset(seed=seed); return o
          63 +    obs=reset(); R=obs.get_object_from_name("robot")
          64 +    obs=reset(); R=obs.get_object_from_name("robot")
          65 +        ^^^^^^^^^^^^^^^^^^^^
          66 +  File "/sandbox/env_client.py", line 525, in reset
          67 +        ^^^^^^^
          68 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          69 +        ^^^^^^^
          70 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          71 +    o,_=env.reset(seed=seed); return o
          72 +    o,_=env.reset(seed=seed); return o
          73 +        ^^^^^^^^^^^^^^^^^^^^
          74 +  File "/sandbox/env_client.py", line 525, in reset
          75 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          76 +        ^^^^^^^^^^^^^^^^^^^^
          77 +  File "/sandbox/env_client.py", line 525, in reset
          78 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          79 +  File "/sandbox/env_client.py", line 478, in _request
          80 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          81 +    raise RuntimeError("Connection to the environment server was closed")
          82 +RuntimeError: Connection to the environment server was closed
          83 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          84 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          85 +  File "/sandbox/env_client.py", line 478, in _request
          86 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          87 +  File "/sandbox/env_client.py", line 478, in _request
          88 +    raise RuntimeError("Connection to the environment server was closed")
          89 +RuntimeError: Connection to the environment server was closed
          90 +    raise RuntimeError("Connection to the environment server was closed")
          91 +RuntimeError: Connection to the environment server was closed
          92 +Traceback (most recent call last):
          93 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          94 +    obs=reset(); R=obs.get_object_from_name("robot")
          95 +        ^^^^^^^
          96 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          97 +    o,_=env.reset(seed=seed); return o
          98 +        ^^^^^^^^^^^^^^^^^^^^
          99 +  File "/sandbox/env_client.py", line 525, in reset
         100 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
         101 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         102 +  File "/sandbox/env_client.py", line 478, in _request
         103 +    raise RuntimeError("Connection to the environment server was closed")
         104 +RuntimeError: Connection to the environment server was closed
         105 +Traceback (most recent call last):
         106 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
         107 +    obs=reset(); R=obs.get_object_from_name("robot")
         108 +        ^^^^^^^
         109 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
         110 +    o,_=env.reset(seed=seed); return o
         111 +        ^^^^^^^^^^^^^^^^^^^^
         112 +  File "/sandbox/env_client.py", line 525, in reset
         113 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
         114 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         115 +  File "/sandbox/env_client.py", line 478, in _request
         116 +    raise RuntimeError("Connection to the environment server was closed")
         117 +RuntimeError: Connection to the environment server was closed
         118 ++0.400    T    F    F    F   22   22   22   22    O    O    O   22   22   22   22   22   22   22   22   22   22   11    F    F    T
         119 ++0.100    F    F    F    F   22   22   22   22   22   22   26    T    T    T   25    O    O    O   22   22   22   11    F    F    F
         120 ++0.350    F    F    F    F   22   22   22   22   22    O    O   22   22   22   22   22   22   22   22   22   22   11    F    F    F
         121 ++0.200    F    F    F    F   22   22   22   22   22   22   22   22   22   22   22    O    O   22   22   22   22   11    F    F    F
         122 ++0.600    N    N    N    N    T    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    T    N    N    N    N
         123 ++0.300    F    F    F    F   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   11    F    F    F
         124 +-0.050    F    F    F    F    F    F    F    F    F   25   29    T    T    T    T   23    F    F    F    F    F    F    F    F    F
         125 +-0.100    F    F    F    F    F    F    F    F    F   22   27    T    T    T    T   20   19    F    F    F    F    F    F    F    F
diff --git a/probe_tab_y90_s0.txt b/probe_tab_y90_s0.txt
new file mode 100644
index 0000000..85e7b9e
--- /dev/null
+++ b/probe_tab_y90_s0.txt
@@ -0,0 +1,41 @@
           1 +Traceback (most recent call last):
           2 +Traceback (most recent call last):
           3 +RuntimeError: Connection to the environment server was closed
           4 +RuntimeError: Connection to the environment server was closed
           5 ++0.700    N    N    N    N    N    N    N    N    N    T    T    T    T    T    T    T    N    N    N    N    N    N    N    N    N
           6 ++0.650    N    N    N    N    N    N    T    T    F    F    F    F    F    F    F    F    F    T    T    N    N    N    N    N    N
           7 ++0.550    N    N    N    T    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    T    N    N    N
           8 ++0.500    N    N    T   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22    T    N    N
           9 ++0.450    N    T    F   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22    F    T    N
          10 ++0.400    T    F    F   22   22   22   22   22   22   22   22   22   22   22   22    O    O   22   22   22   22   22    F    F    T
          11 ++0.350    F    F    F   22   22   22   22   22   22   22   22   22   22   22    O    O    O    O   22   22   22   22    F    F    F
          12 ++0.300    F    F    F   22   22   22   22   22   22   22   22   22   22   22    O    O    O    O   22   22   22   22    F    F    F
          13 ++0.250    F    F    F   22   22   22   22   22   22   22   22   22   22   22   22    O   22   22   22   22   22   22    F    F    F
          14 ++0.200    F    F    F   22   22   22   22   22   22   22   22   22   22   22   22   22    O    O    O   22   22   22    F    F    F
          15 ++0.150    F    F    F   22   22   22   22   22   22   22   22   25   26   24   22    O    O    O    O   22   22   22    F    F    F
          16 ++0.100    F    F    F   22   22   22   22   22   22   22   27   29   29   28   25    O    O    O    O   22   22   22    F    F    F
          17 ++0.050    F    F    F    F   11   11   11   11   14   25    T    T    T    T    T    O    O    O    O   11   11    F    F    F    F
          18 ++0.000    F    F    F    F    F    F    F    F   17   26    T    T    T    T    T   24    F    F    F    F    F    F    F    F    F
          19 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          20 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          21 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          22 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          23 +  File "/sandbox/env_client.py", line 525, in reset
          24 +  File "/sandbox/env_client.py", line 525, in reset
          25 +  File "/sandbox/env_client.py", line 478, in _request
          26 +  File "/sandbox/env_client.py", line 478, in _request
          27 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          28 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          29 +    raise RuntimeError("Connection to the environment server was closed")
          30 +    raise RuntimeError("Connection to the environment server was closed")
          31 +    obs=reset(); R=obs.get_object_from_name("robot")
          32 +    obs=reset(); R=obs.get_object_from_name("robot")
          33 +    o,_=env.reset(seed=seed); return o
          34 +    o,_=env.reset(seed=seed); return o
          35 +        ^^^^^^^^^^^^^^^^^^^^
          36 +        ^^^^^^^^^^^^^^^^^^^^
          37 +        ^^^^^^^
          38 +        ^^^^^^^
          39 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          40 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          41 +-0.100    F    F    F    F    F    F    F    F    F   22   27   29   34    T   25   19    F    F    F    F    F    F    F    F    F
diff --git a/probe_tab_y90_s0.txt.tmp b/probe_tab_y90_s0.txt.tmp
new file mode 100644
index 0000000..80ed792
--- /dev/null
+++ b/probe_tab_y90_s0.txt.tmp
@@ -0,0 +1,41 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
           3 +    obs=reset(); R=obs.get_object_from_name("robot")
           4 +        ^^^^^^^
           5 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
           6 +    o,_=env.reset(seed=seed); return o
           7 +        ^^^^^^^^^^^^^^^^^^^^
           8 +  File "/sandbox/env_client.py", line 525, in reset
           9 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          10 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          11 +  File "/sandbox/env_client.py", line 478, in _request
          12 +    raise RuntimeError("Connection to the environment server was closed")
          13 +RuntimeError: Connection to the environment server was closed
          14 +Traceback (most recent call last):
          15 +  File "/sandbox/probe_tab_desc.py", line 11, in <module>
          16 +    obs=reset(); R=obs.get_object_from_name("robot")
          17 +        ^^^^^^^
          18 +  File "/sandbox/probe_tab_desc.py", line 10, in reset
          19 +    o,_=env.reset(seed=seed); return o
          20 +        ^^^^^^^^^^^^^^^^^^^^
          21 +  File "/sandbox/env_client.py", line 525, in reset
          22 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          23 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          24 +  File "/sandbox/env_client.py", line 478, in _request
          25 +    raise RuntimeError("Connection to the environment server was closed")
          26 +RuntimeError: Connection to the environment server was closed
          27 ++0.700    N    N    N    N    N    N    N    N    N    T    T    T    T    T    T    T    N    N    N    N    N    N    N    N    N
          28 ++0.650    N    N    N    N    N    N    T    T    F    F    F    F    F    F    F    F    F    T    T    N    N    N    N    N    N
          29 ++0.500    N    N    T   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22    T    N    N
          30 ++0.450    N    T    F   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22   22    F    T    N
          31 ++0.400    T    F    F   22   22   22   22   22   22   22   22   22   22   22   22    O    O   22   22   22   22   22    F    F    T
          32 ++0.100    F    F    F   22   22   22   22   22   22   22   27   29   29   28   25    O    O    O    O   22   22   22    F    F    F
          33 ++0.300    F    F    F   22   22   22   22   22   22   22   22   22   22   22    O    O    O    O   22   22   22   22    F    F    F
          34 ++0.200    F    F    F   22   22   22   22   22   22   22   22   22   22   22   22   22    O    O    O   22   22   22    F    F    F
          35 ++0.150    F    F    F   22   22   22   22   22   22   22   22   25   26   24   22    O    O    O    O   22   22   22    F    F    F
          36 ++0.350    F    F    F   22   22   22   22   22   22   22   22   22   22   22    O    O    O    O   22   22   22   22    F    F    F
          37 ++0.250    F    F    F   22   22   22   22   22   22   22   22   22   22   22   22    O   22   22   22   22   22   22    F    F    F
          38 ++0.050    F    F    F    F   11   11   11   11   14   25    T    T    T    T    T    O    O    O    O   11   11    F    F    F    F
          39 ++0.550    N    N    N    T    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    F    T    N    N    N
          40 ++0.000    F    F    F    F    F    F    F    F   17   26    T    T    T    T    T   24    F    F    F    F    F    F    F    F    F
          41 +-0.100    F    F    F    F    F    F    F    F    F   22   27   29   34    T   25   19    F    F    F    F    F    F    F    F    F
diff --git a/prof.py b/prof.py
new file mode 100644
index 0000000..7e1bc30
--- /dev/null
+++ b/prof.py
@@ -0,0 +1,11 @@
           1 +import time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env(); obs, info = env.reset(seed=7)
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           6 +ta=te=0
           7 +for i in range(60):
           8 +    t=time.time(); a=ap.get_action(obs); ta+=time.time()-t
           9 +    t=time.time(); obs,r,term,tr,info=env.step(a); te+=time.time()-t
          10 +    if term: break
          11 +print(i, "approach", ta, "env", te)
```

</details>

<a id="C005"></a>
### C005 · grasp height rule (fingertip >= support+0.017), grasp verification and retry

Commit `daa4226b42c072ae3f08ab2bc01d042d5c01e9e6`; parents: 1afb5b99782877bdaf42d2220295db45314a0a6e. Recorded author date: 2026-09-30T21:05:54+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0481](01_timeline.md#E0481): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_daa4226_approach.py) · [Exact all-file diff](evidence/diffs/C005_daa4226.diff)

[Previous saved controller snapshot](evidence/versions/C004_1afb5b9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d91a176..f7f0c1d 100644
--- a/approach.py
+++ b/approach.py
@@ -152,6 +152,7 @@ class GeneratedApproach:
  152    152          self.placed_spots = []
  153    153          self.yaw = 0.0
  154    154          self.done_flag = False
         155 +        self.pending_check = None
  155    156  
  156    157      # ---------------------------------------------------------------- geometry
  157    158      def _region(self, boxes):
@@ -251,7 +252,10 @@ class GeneratedApproach:
  251    252          T, _, _ = fk(q)
  252    253          safe0 = self._safe_z(boxes)
  253    254          # fingertip at object centre (but not below support+5mm)
  254        -        tip = max(b["z"], b["z"] - b["hz"] + 0.012)
         255 +        k = self.fail.get(name, 0)
         256 +        tip = max(b["z"], b["z"] - b["hz"] + 0.017)
         257 +        tip = tip + [0.0, 0.003, -0.002, 0.006, 0.0, 0.003][k % 6]
         258 +        tip = min(tip, b["z"] + b["hz"] - 0.001)
  255    259          grasp_z = tip + FINGER
  256    260          off = grasp_z - b["z"]          # EE z - object centre z while held
  257    261          safe1 = max(self._safe_z(boxes, b["hz"], 0.0) , b["hz"] + off + 0.03 + 0.15)
@@ -303,6 +307,15 @@ class GeneratedApproach:
  303    307          self.last_q = q.copy()
  304    308          self.last_cmd = None
  305    309  
         310 +        if self.pending_check is not None:
         311 +            name = self.pending_check
         312 +            self.pending_check = None
         313 +            r = self._robot(state)
         314 +            if state.get(r, "grasp_active") < 0.5:
         315 +                self.fail[name] = self.fail.get(name, 0) + 1
         316 +                T, _, _ = fk(q)
         317 +                self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.05]), None)]
         318 +                self.cur = None
  306    319          if rejected and self.cur is not None and self.cur[0] == "move":
  307    320              self._handle_reject(state)
  308    321  
@@ -316,6 +329,7 @@ class GeneratedApproach:
  316    329              if seg[0] == "grip":
  317    330                  act[10] = seg[1]
  318    331                  self.cur = None
         332 +                self.pending_check = seg[2] if seg[1] < 0 else None
  319    333                  self.last_cmd = np.zeros(7)
  320    334                  return act
  321    335              # move segment
diff --git a/g9b.txt b/g9b.txt
new file mode 100644
index 0000000..ab022c1
--- /dev/null
+++ b/g9b.txt
@@ -0,0 +1,6 @@
           1 +-0.008 0.0 reached True grasp 0.0 finger 0.0 [0. 0. 0.]
           2 +-0.004 0.0 reached True grasp 0.0 finger 0.0 [0. 0. 0.]
           3 +0.0 0.0 reached True grasp 0.0 finger 0.0 [0. 0. 0.]
           4 +0.004 0.0 reached True grasp 1.0 finger 0.56 [0.00e+00 1.00e-04 3.38e-02]
           5 +0.008 0.0 reached True grasp 1.0 finger 0.56 [0.00e+00 1.00e-04 3.78e-02]
           6 +0.012 0.0 reached True grasp 1.0 finger 0.56 [0.00e+00 1.00e-04 4.18e-02]
diff --git a/ga.txt b/ga.txt
new file mode 100644
index 0000000..09d781b
--- /dev/null
+++ b/ga.txt
@@ -0,0 +1,9 @@
           1 +-0.02 0.0 reached False grasp 0.0 finger 0.0 [0. 0. 0.]
           2 +-0.012 0.0 reached True grasp 0.0 finger 0.0 [0. 0. 0.]
           3 +-0.006 0.0 reached True grasp 1.0 finger 0.6 [0.00e+00 1.00e-04 2.38e-02]
           4 +0.0 0.0 reached True grasp 1.0 finger 0.6 [0.00e+00 1.00e-04 2.98e-02]
           5 +0.004 0.0 reached True grasp 1.0 finger 0.6 [0.00e+00 1.00e-04 3.38e-02]
           6 +0.01 0.0 reached True grasp 1.0 finger 0.6 [0.00e+00 1.00e-04 3.98e-02]
           7 +0.016 0.0 reached True grasp 1.0 finger 0.6 [0.00e+00 1.00e-04 4.58e-02]
           8 +0.022 0.0 reached True grasp 1.0 finger 0.6 [0.00e+00 1.00e-04 5.18e-02]
           9 +0.03 0.0 reached True grasp 0.0 finger 0.0 [0. 0. 0.]
diff --git a/gb.txt b/gb.txt
new file mode 100644
index 0000000..3f38b40
--- /dev/null
+++ b/gb.txt
@@ -0,0 +1,9 @@
           1 +-0.02 0.0 reached False grasp 0.0 finger 0.0 [0. 0. 0.]
           2 +-0.012 0.0 reached False grasp 0.0 finger 0.0 [0. 0. 0.]
           3 +-0.006 0.0 reached False grasp 0.0 finger 0.0 [0. 0. 0.]
           4 +0.0 0.0 reached False grasp 0.0 finger 0.0 [0. 0. 0.]
           5 +0.004 0.0 reached False grasp 0.0 finger 0.0 [0. 0. 0.]
           6 +0.01 0.0 reached True grasp 1.0 finger 0.42 [0.00e+00 1.00e-04 3.98e-02]
           7 +0.016 0.0 reached True grasp 1.0 finger 0.42 [0.00e+00 1.00e-04 4.58e-02]
           8 +0.022 0.0 reached True grasp 1.0 finger 0.42 [0.00e+00 1.00e-04 5.18e-02]
           9 +0.03 0.0 reached True grasp 1.0 finger 0.42 [0.00e+00 1.00e-04 5.98e-02]
diff --git a/gc.txt b/gc.txt
new file mode 100644
index 0000000..ae9d073
--- /dev/null
+++ b/gc.txt
@@ -0,0 +1,6 @@
           1 +0.001 0.0 reached True grasp 0.0 finger 0.0 [0. 0. 0.]
           2 +0.002 0.0 reached True grasp 1.0 finger 0.56 [0.00e+00 1.00e-04 3.18e-02]
           3 +0.003 0.0 reached True grasp 1.0 finger 0.56 [0.00e+00 1.00e-04 3.28e-02]
           4 +0.014 0.0 reached True grasp 1.0 finger 0.56 [0.00e+00 1.00e-04 4.38e-02]
           5 +0.018 0.0 reached True grasp 0.0 finger 0.0 [0. 0. 0.]
           6 +0.022 0.0 reached True grasp 0.0 finger 0.0 [0. 0. 0.]
diff --git a/probe_g9.py b/probe_g9.py
new file mode 100644
index 0000000..4247317
--- /dev/null
+++ b/probe_g9.py
@@ -0,0 +1,26 @@
           1 +from env_client import make_env
           2 +from approach import ik, fk, down_R
           3 +import numpy as np, sys
           4 +seed=int(sys.argv[1]); name=sys.argv[2]; yaw=float(sys.argv[3])
           5 +env = make_env()
           6 +def q_of(o,R): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           7 +def goto(obs, R, qt, maxn=40):
           8 +    for _ in range(maxn):
           9 +        q = q_of(obs,R); d = qt - q
          10 +        if np.max(np.abs(d)) < 1e-4: break
          11 +        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2)
          12 +        obs2, *_ = env.step(a)
          13 +        if np.allclose(q_of(obs2,R), q): return obs2, False
          14 +        obs = obs2
          15 +    return obs, True
          16 +for dtip in [float(v) for v in sys.argv[4].split(",")]:
          17 +  for dx in [0.0]:
          18 +    obs, info = env.reset(seed=seed)
          19 +    R = obs.get_object_from_name("robot"); B = obs.get_object_from_name(name)
          20 +    bx, by, bz = obs.get(B,'pose_x'), obs.get(B,'pose_y'), obs.get(B,'pose_z')
          21 +    q=q_of(obs,R)
          22 +    for z in [0.36, bz+0.155+dtip]:
          23 +        qt,e = ik(q, np.array([bx+dx,by,z]), down_R(yaw)); obs,ok=goto(obs,R,qt); q=q_of(obs,R)
          24 +    a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a)
          25 +    print(dtip, dx, "reached", ok, "grasp", obs.get(R,'grasp_active'), "finger", round(obs.get(R,'finger_state'),3), np.round(obs.data[R][12:15],4))
          26 +env.close()
diff --git a/probe_tab_ik2.py b/probe_tab_ik2.py
new file mode 100644
index 0000000..6d0c9a5
--- /dev/null
+++ b/probe_tab_ik2.py
@@ -0,0 +1,12 @@
           1 +from kin import *
           2 +import numpy as np
           3 +q0=np.array([0,0.26,3.14,-2.27,0,0.96,1.57])
           4 +pts=[(0.51,0.41),(0.51,-0.41),(0.09,0.41),(0.09,-0.41),(0.55,0),(0.6,0.3),(0.3,0),(0.12,0.0)]
           5 +for yaw in [0,np.pi/2]:
           6 +  for z in [0.23,0.40]:
           7 +    r=[]
           8 +    for x,y in pts:
           9 +        s=np.array([np.arctan2(y,x),0.3,3.14,-2.0,0,0.9,1.57])
          10 +        e=min(ik(s,np.array([x,y,z]),down_R(yaw),(0,0,0))[1], ik(q0,np.array([x,y,z]),down_R(yaw),(0,0,0))[1])
          11 +        r.append("%.0e"%e)
          12 +    print(round(yaw,2),z,r,flush=True)
diff --git a/probe_tab_ref.out b/probe_tab_ref.out
new file mode 100644
index 0000000..e4c7e05
--- /dev/null
+++ b/probe_tab_ref.out
@@ -0,0 +1,12 @@
           1 +y 0.0 yaw 0.0 [(0.6, '-17')]
           2 +x 0.3 yaw 0.0 [(0.55, '-18')]
           3 +y 0.3 yaw 0.0 [(-0.02, 'F'), (-0.01, 'F'), (0.0, 'F'), (0.01, 'F'), (0.02, 'F'), (0.03, 'O'), (0.04, 'O'), (0.05, 'O'), (0.06, 'O'), (0.07, 'O'), (0.08, 'O'), (0.09, 'O'), (0.1, 'O')]
           4 +y 0.3 yaw 1.5708 [(-0.02, 'F'), (-0.01, 'F'), (0.0, 'F'), (0.01, 'F'), (0.02, 'F'), (0.03, 'O'), (0.04, 'O'), (0.05, 'O'), (0.06, 'O'), (0.07, 'O'), (0.08, 'O'), (0.09, 'O'), (0.1, 'O')]
           5 +y -0.2 yaw 0.0 [(0.45, '22'), (0.46, '22'), (0.47, '22'), (0.48, '22'), (0.49, '22'), (0.5, '22'), (0.51, '22'), (0.52, '22'), (0.53, '22'), (0.54, '22'), (0.55, '22'), (0.56, '21'), (0.57, '19'), (0.58, 'F')]
           6 +x 0.3 yaw 1.5708 [(-0.5, 'F'), (-0.49, 'F'), (-0.48, 'F'), (-0.47, '19'), (-0.46, '21'), (-0.45, '22'), (-0.44, '22'), (-0.43, '22'), (-0.42, '22'), (-0.41, '22'), (-0.4, '22'), (-0.39, '22'), (-0.38, '22'), (-0.37, '22'), (-0.36, '22')]
           7 +x 0.3 yaw 1.5708 [(0.36, '22'), (0.37, '22'), (0.38, '22'), (0.39, '22'), (0.4, '22'), (0.41, '22'), (0.42, '22'), (0.43, '22'), (0.44, '22'), (0.45, '22'), (0.46, '21'), (0.47, '19'), (0.48, 'F'), (0.49, 'F'), (0.5, 'F')]
           8 +y -0.2 yaw 1.5708 [(0.45, '22'), (0.46, '22'), (0.47, '22'), (0.48, '22'), (0.49, '22'), (0.5, '22'), (0.51, '22'), (0.52, '15'), (0.53, '12'), (0.54, 'F'), (0.55, 'F'), (0.56, 'F'), (0.57, 'F'), (0.58, 'F')]
           9 +x 0.3 yaw 0.0 [(0.36, '22'), (0.37, '22'), (0.38, '22'), (0.39, '22'), (0.4, '22'), (0.41, '22'), (0.42, '15'), (0.43, '12'), (0.44, '11'), (0.45, '11'), (0.46, '11'), (0.47, 'F'), (0.48, 'F'), (0.49, 'F'), (0.5, 'F')]
          10 +x 0.3 yaw 0.0 [(-0.5, 'F'), (-0.49, 'F'), (-0.48, 'F'), (-0.47, 'F'), (-0.46, 'F'), (-0.45, 'F'), (-0.44, 'F'), (-0.43, '12'), (-0.42, '15'), (-0.41, '22'), (-0.4, '22'), (-0.39, '22'), (-0.38, '22'), (-0.37, '22'), (-0.36, '22')]
          11 +y -0.25 yaw 0.0 [(-0.02, 'F'), (-0.01, 'F'), (0.0, 'F'), (0.01, 'F'), (0.02, 'F'), (0.03, '18'), (0.04, '21'), (0.05, '22'), (0.06, '22'), (0.07, '22'), (0.08, '22'), (0.09, '22'), (0.1, '22')]
          12 +y -0.25 yaw 1.5708 [(-0.02, 'F'), (-0.01, 'F'), (0.0, 'F'), (0.01, 'F'), (0.02, 'F'), (0.03, 'F'), (0.04, '11'), (0.05, '11'), (0.06, '11'), (0.07, '12'), (0.08, '15'), (0.09, '22'), (0.1, '22')]
diff --git a/probe_tab_ref.py b/probe_tab_ref.py
index 3dae27f..32aad83 100644
--- a/probe_tab_ref.py
+++ b/probe_tab_ref.py
@@ -1,11 +1,12 @@
    1      1  from env_client import make_env
    2      2  from kin import *
    3      3  import numpy as np, sys
    4        -seed=int(sys.argv[1]); yaw=float(sys.argv[2]); x=float(sys.argv[3])
           4 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); mode=sys.argv[3]; fixed=float(sys.argv[4])
    5      5  ys=np.round(np.arange(-0.6,0.6001,0.05),3); ZMIN=0.0999
    6        -if len(sys.argv)>4: ys=np.round(np.arange(float(sys.argv[4]),float(sys.argv[5])+1e-6,float(sys.argv[6])),3)
           6 +ys=np.round(np.arange(float(sys.argv[5]),float(sys.argv[6])+1e-6,float(sys.argv[7])),3)
           7 +if len(sys.argv)>8: ZMIN=float(sys.argv[8])
    7      8  env = make_env()
    8        -B=(0,0,0); Rd=down_R(yaw)
           9 +import os; NOSKIP=os.environ.get("NOSKIP"); B=(0,0,0); Rd=down_R(yaw)
    9     10  def reset():
   10     11      o,_=env.reset(seed=seed); return o
   11     12  obs=reset(); R=obs.get_object_from_name("robot")
@@ -29,8 +30,9 @@ def moveto(obs,p):
   29     30      if e>1e-3: return obs,False,e
   30     31      obs,ok=goto(obs,qt); return obs,ok,e
   31     32  res=[]
   32        -for y in ys:
   33        -    if any(np.hypot(x-ox,y-oy)<0.09 for ox,oy in objs): res.append('O'); continue
          33 +for v in ys:
          34 +    x,y=(fixed,v) if mode=='x' else (v,fixed)
          35 +    if not NOSKIP and any(np.hypot(x-ox,y-oy)<0.09 for ox,oy in objs): res.append('O'); continue
   34     36      q=q_of(obs)
   35     37      _,e1=ik(q,np.array([x,y,0.36]),Rd,B); _,e2=ik(q,np.array([x,y,0.23]),Rd,B)
   36     38      if e1>1e-3 and e2>1e-3: res.append('N'); continue
@@ -51,5 +53,5 @@ for y in ys:
   51     53          if not ok: stop='%d'%round(z*100); break
   52     54      res.append(stop if stop else 'F')
   53     55      for z in np.arange(ee_pose(q_of(obs),B)[2,3],0.37,0.02): obs,ok,e=moveto(obs,[x,y,min(z,0.36)])
   54        -print("%+.3f "%x+" ".join("%4s"%r for r in res), flush=True)
          56 +print(mode,fixed,"yaw",yaw,list(zip(ys.tolist(),res)), flush=True)
   55     57  env.close()
diff --git a/probe_tab_ref2.out b/probe_tab_ref2.out
new file mode 100644
index 0000000..ed2125d
--- /dev/null
+++ b/probe_tab_ref2.out
@@ -0,0 +1,4 @@
           1 +x 0.336 yaw 1.5708 [(0.1, '27'), (0.11, '27'), (0.12, '27'), (0.13, '27'), (0.14, '27'), (0.15, '27'), (0.16, 'F'), (0.17, 'F'), (0.18, 'F'), (0.19, 'F'), (0.2, '27'), (0.21, '27'), (0.22, '27'), (0.23, '27'), (0.24, '27'), (0.25, '27')]
           2 +x 0.336 yaw 0.0 [(0.1, 'F'), (0.11, 'F'), (0.12, 'F'), (0.13, 'F'), (0.14, 'F'), (0.15, 'F'), (0.16, 'F'), (0.17, 'F'), (0.18, 'F'), (0.19, 'F'), (0.2, 'F'), (0.21, 'F'), (0.22, 'F'), (0.23, 'F'), (0.24, 'F'), (0.25, 'F')]
           3 +y 0.173 yaw 0.0 [(0.24, '25'), (0.25, '27'), (0.26, '27'), (0.27, '27'), (0.28, '27'), (0.29, '27'), (0.3, '27'), (0.31, '27'), (0.32, '27'), (0.33, 'F'), (0.34, 'F'), (0.35, '27'), (0.36, '27'), (0.37, '27'), (0.38, '27'), (0.39, '27'), (0.4, '27'), (0.41, '27'), (0.42, '27'), (0.43, '25')]
           4 +y 0.173 yaw 1.5708 [(0.24, 'F'), (0.25, 'F'), (0.26, 'F'), (0.27, 'F'), (0.28, 'F'), (0.29, 'F'), (0.3, 'F'), (0.31, 'F'), (0.32, 'F'), (0.33, 'F'), (0.34, 'F'), (0.35, 'F'), (0.36, 'F'), (0.37, 'F'), (0.38, 'F'), (0.39, 'F'), (0.4, 'F'), (0.41, 'F'), (0.42, 'F'), (0.43, 'F')]
```

</details>

<a id="C006"></a>
### C006 · wip

Commit `da7468c031192b7a13dd1c99654bff17d65faf62`; parents: daa4226b42c072ae3f08ab2bc01d042d5c01e9e6. Recorded author date: 2026-09-30T21:35:24+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0595](01_timeline.md#E0595): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C006_da7468c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..677db19
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,11 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach, fk
           4 +seed=int(sys.argv[1]); N=int(sys.argv[2]); t0=int(sys.argv[3])
           5 +env = make_env(); obs, info = env.reset(seed=seed)
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +for t in range(N):
           8 +    a = ap.get_action(obs)
           9 +    obs, r, term, trunc, info = env.step(a)
          10 +    q = ap._q(obs); T,_,_ = fk(q)
          11 +    if t>=t0: print(t, np.round(T[:3,3],3), np.round(q,2), np.round(a[3:10],3))
diff --git a/oc_check.py b/oc_check.py
new file mode 100644
index 0000000..79f87a1
--- /dev/null
+++ b/oc_check.py
@@ -0,0 +1,4 @@
           1 +from env_client import make_env
           2 +env=make_env()
           3 +for n in [3,4,6,8]:
           4 +    obs,info=env.reset(seed=1,options={'object_count':n}); print(n, info, sorted(obs.get_object_names()))
diff --git a/probe_basefk.py b/probe_basefk.py
new file mode 100644
index 0000000..1ca81ff
--- /dev/null
+++ b/probe_basefk.py
@@ -0,0 +1,35 @@
           1 +from env_client import make_env
           2 +from approach import ik, fk, down_R
           3 +import numpy as np, sys
           4 +env = make_env()
           5 +dbx, dby, drot = [float(v) for v in sys.argv[1:4]]; hyp = sys.argv[4]
           6 +obs, info = env.reset(seed=0)
           7 +R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
           8 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           9 +# move base away first: -x then y/rot
          10 +for i in range(20):
          11 +    rem = np.array([dbx - (obs.get(R,'pos_base_x')+0.12), dby - obs.get(R,'pos_base_y'), drot - obs.get(R,'pos_base_rot')])
          12 +    if np.max(np.abs(rem))<1e-6: break
          13 +    a=np.zeros(11,np.float32); a[0:3]=np.clip(rem,-.2,.2); obs,*_=env.step(a)
          14 +bxw,byw,rot = obs.get(R,'pos_base_x'),obs.get(R,'pos_base_y'),obs.get(R,'pos_base_rot')
          15 +print("base", bxw, byw, rot)
          16 +if hyp=='A': mount=np.array([bxw+0.12*np.cos(rot), byw+0.12*np.sin(rot)])
          17 +else: mount=np.array([bxw+0.12, byw])
          18 +c,s=np.cos(rot),np.sin(rot); Rz=np.array([[c,-s,0],[s,c,0],[0,0,1]])
          19 +def to_local(p): 
          20 +    d=np.array(p)-np.array([mount[0],mount[1],0]); return Rz.T@d
          21 +bx,by=obs.get(B,'pose_x'),obs.get(B,'pose_y')
          22 +q=q_of(obs)
          23 +def goto(obs, qt, maxn=40):
          24 +    for _ in range(maxn):
          25 +        q = q_of(obs); d = qt - q
          26 +        if np.max(np.abs(d)) < 1e-4: break
          27 +        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2)
          28 +        obs2, *_ = env.step(a)
          29 +        if np.allclose(q_of(obs2), q): return obs2, False
          30 +        obs = obs2
          31 +    return obs, True
          32 +for z in [0.36,0.30,0.265]:
          33 +    p=to_local([bx,by,z]); Rl=Rz.T@down_R(np.pi/2)
          34 +    qt,e=ik(q,p,Rl); obs,ok=goto(obs,qt); q=q_of(obs); print(z, ok, e)
          35 +a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a); print("grasp", obs.get(R,'grasp_active'))
diff --git a/res_40_240.txt b/res_40_240.txt
new file mode 100644
index 0000000..a64f8e2
--- /dev/null
+++ b/res_40_240.txt
@@ -0,0 +1,201 @@
           1 +(40, 1, False, 1000, 290.6)
           2 +(41, 1, True, 44, 44.5)
           3 +(42, 0, True, 21, 23.6)
           4 +(43, 1, True, 40, 34.7)
           5 +(44, 2, True, 44, 42.7)
           6 +(45, 2, True, 55, 59.8)
           7 +(46, 1, True, 41, 33.4)
           8 +(47, 0, True, 20, 11.7)
           9 +(48, 0, True, 19, 12.2)
          10 +(49, 0, True, 23, 20.2)
          11 +(50, 2, True, 61, 48.2)
          12 +(51, 1, True, 40, 26.7)
          13 +(52, 2, False, 1000, 286.0)
          14 +(53, 2, True, 71, 49.9)
          15 +(54, 0, True, 23, 13.0)
          16 +(55, 2, True, 85, 57.4)
          17 +(56, 1, True, 32, 17.1)
          18 +(57, 0, True, 19, 10.6)
          19 +(58, 1, True, 33, 26.7)
          20 +(59, 2, True, 81, 58.1)
          21 +(60, 0, True, 20, 9.3)
          22 +(61, 1, True, 41, 21.8)
          23 +(62, 1, True, 40, 23.4)
          24 +(63, 1, True, 42, 24.1)
          25 +(64, 1, True, 45, 25.9)
          26 +(65, 0, True, 37, 26.0)
          27 +(66, 2, True, 60, 37.6)
          28 +(67, 2, True, 63, 38.4)
          29 +(68, 1, True, 23, 17.2)
          30 +(69, 0, True, 18, 10.8)
          31 +(70, 1, True, 45, 26.1)
          32 +(71, 2, True, 69, 49.5)
          33 +(72, 2, True, 63, 40.3)
          34 +(73, 2, True, 58, 32.3)
          35 +(74, 0, True, 20, 12.5)
          36 +(75, 1, True, 41, 25.1)
          37 +(76, 1, True, 49, 35.5)
          38 +(77, 0, True, 20, 6.0)
          39 +(78, 2, True, 47, 31.5)
          40 +(79, 0, True, 19, 12.3)
          41 +(80, 2, True, 60, 42.5)
          42 +(81, 0, True, 20, 10.0)
          43 +(82, 2, True, 61, 35.6)
          44 +(83, 2, True, 34, 18.8)
          45 +(84, 1, True, 41, 17.3)
          46 +(85, 2, True, 63, 37.2)
          47 +(86, 2, True, 54, 34.6)
          48 +(87, 1, True, 46, 31.5)
          49 +(88, 1, True, 44, 31.4)
          50 +(89, 2, True, 261, 149.1)
          51 +(90, 1, True, 33, 19.9)
          52 +(91, 2, True, 48, 32.1)
          53 +(92, 1, True, 33, 18.0)
          54 +(93, 2, True, 61, 42.5)
          55 +(94, 0, True, 26, 12.6)
          56 +(95, 1, True, 41, 22.7)
          57 +(96, 2, True, 68, 60.3)
          58 +(97, 0, True, 22, 14.8)
          59 +(98, 1, True, 42, 28.8)
          60 +(99, 2, True, 55, 33.7)
          61 +(100, 2, True, 61, 56.2)
          62 +(101, 0, True, 16, 8.4)
          63 +(102, 1, True, 35, 30.1)
          64 +(103, 1, True, 45, 46.5)
          65 +(104, 2, False, 1000, 794.8)
          66 +(105, 0, True, 22, 27.2)
          67 +(106, 1, True, 24, 38.5)
          68 +(107, 0, True, 22, 23.1)
          69 +(108, 0, True, 24, 26.1)
          70 +(109, 1, True, 38, 45.2)
          71 +(110, 1, True, 54, 68.7)
          72 +(111, 1, True, 36, 39.3)
          73 +(112, 0, True, 26, 25.5)
          74 +(113, 0, True, 26, 33.4)
          75 +(114, 0, True, 15, 8.6)
          76 +(115, 1, True, 37, 45.4)
          77 +(116, 0, True, 23, 27.7)
          78 +(117, 0, True, 16, 20.3)
          79 +(118, 1, True, 41, 51.5)
          80 +(119, 1, True, 44, 51.6)
          81 +(120, 0, True, 15, 15.3)
          82 +(121, 0, True, 17, 17.0)
          83 +(122, 2, True, 72, 72.3)
          84 +(123, 0, True, 18, 16.7)
          85 +(124, 2, True, 39, 35.1)
          86 +(125, 1, True, 57, 47.0)
          87 +(126, 0, True, 27, 20.9)
          88 +(127, 1, True, 24, 20.7)
          89 +(128, 2, True, 72, 65.7)
          90 +(129, 1, True, 37, 27.3)
          91 +(130, 2, False, 1000, 251.9)
          92 +(131, 1, True, 43, 38.0)
          93 +(132, 2, True, 52, 42.9)
          94 +(133, 1, True, 44, 41.0)
          95 +(134, 2, True, 60, 53.3)
          96 +(135, 1, True, 36, 27.8)
          97 +(136, 2, True, 40, 35.8)
          98 +(137, 1, True, 44, 42.0)
          99 +(138, 1, True, 45, 36.3)
         100 +(139, 1, True, 53, 47.4)
         101 +(140, 1, True, 40, 31.2)
         102 +(141, 1, True, 43, 37.7)
         103 +(142, 0, True, 30, 20.7)
         104 +(143, 2, True, 63, 71.7)
         105 +(144, 0, True, 24, 24.3)
         106 +(145, 1, True, 41, 48.6)
         107 +(146, 2, True, 42, 50.7)
         108 +(147, 0, True, 17, 22.2)
         109 +(148, 0, True, 16, 25.1)
         110 +(149, 0, True, 24, 30.0)
         111 +(150, 1, True, 31, 29.2)
         112 +(151, 2, True, 40, 32.4)
         113 +(152, 2, True, 50, 43.2)
         114 +(153, 2, True, 56, 44.5)
         115 +(154, 0, True, 19, 11.5)
         116 +(155, 0, True, 24, 20.0)
         117 +(156, 2, True, 133, 74.5)
         118 +(157, 0, True, 24, 15.0)
         119 +(158, 1, True, 33, 19.3)
         120 +(159, 2, True, 52, 37.5)
         121 +(160, 0, True, 32, 21.7)
         122 +(161, 2, True, 39, 24.9)
         123 +(162, 1, True, 47, 32.0)
         124 +(163, 1, True, 33, 22.3)
         125 +(164, 1, True, 39, 29.8)
         126 +(165, 1, True, 42, 28.9)
         127 +(166, 2, True, 79, 51.8)
         128 +(167, 2, True, 53, 35.8)
         129 +(168, 1, True, 141, 52.4)
         130 +(169, 2, True, 62, 42.0)
         131 +(170, 2, True, 71, 53.4)
         132 +(171, 2, True, 63, 43.3)
         133 +(172, 1, True, 41, 22.8)
         134 +(173, 2, True, 71, 51.3)
         135 +(174, 1, True, 44, 33.9)
         136 +(175, 2, True, 56, 42.8)
         137 +(176, 0, True, 22, 14.9)
         138 +(177, 2, True, 56, 45.4)
         139 +(178, 1, True, 45, 27.4)
         140 +(179, 2, True, 70, 47.9)
         141 +(180, 0, True, 28, 20.8)
         142 +(181, 2, True, 61, 56.1)
         143 +(182, 2, True, 65, 56.5)
         144 +(183, 2, True, 45, 40.5)
         145 +(184, 1, True, 41, 32.4)
         146 +(185, 0, True, 29, 15.3)
         147 +(186, 0, True, 22, 7.6)
         148 +(187, 1, True, 24, 29.0)
         149 +(188, 1, True, 38, 40.1)
         150 +(189, 1, True, 49, 52.8)
         151 +(190, 0, True, 21, 22.8)
         152 +(191, 0, True, 16, 15.2)
         153 +(192, 2, True, 42, 45.5)
         154 +(193, 1, True, 56, 54.1)
         155 +(194, 2, True, 162, 83.6)
         156 +(195, 0, True, 20, 14.1)
         157 +(196, 0, True, 19, 14.4)
         158 +(197, 2, True, 51, 46.4)
         159 +(198, 1, True, 43, 42.8)
         160 +(199, 1, True, 53, 51.7)
         161 +(200, 0, True, 24, 16.4)
         162 +(201, 0, True, 15, 6.7)
         163 +(202, 0, True, 23, 24.8)
         164 +(203, 0, True, 16, 11.8)
         165 +(204, 2, True, 74, 72.9)
         166 +(205, 1, True, 35, 29.9)
         167 +(206, 1, True, 39, 33.1)
         168 +(207, 0, True, 27, 18.0)
         169 +(208, 2, True, 35, 33.0)
         170 +(209, 2, False, 1000, 227.7)
         171 +(210, 0, True, 18, 10.1)
         172 +(211, 0, True, 17, 16.5)
         173 +(212, 0, True, 19, 15.9)
         174 +(213, 0, True, 28, 20.6)
         175 +(214, 0, True, 30, 24.3)
         176 +(215, 2, True, 58, 42.1)
         177 +(216, 2, True, 40, 30.9)
         178 +(217, 2, True, 58, 43.3)
         179 +(218, 1, True, 43, 32.3)
         180 +(219, 0, True, 20, 9.4)
         181 +(220, 2, True, 62, 41.0)
         182 +(221, 1, True, 33, 22.6)
         183 +(222, 1, True, 38, 23.9)
         184 +(223, 1, True, 42, 27.2)
         185 +(224, 2, True, 54, 33.7)
         186 +(225, 2, True, 64, 52.5)
         187 +(226, 2, True, 57, 40.2)
         188 +(227, 1, True, 40, 24.8)
         189 +(228, 1, True, 39, 23.6)
         190 +(229, 1, True, 38, 32.6)
         191 +(230, 1, True, 38, 31.2)
         192 +(231, 0, True, 28, 26.4)
         193 +(232, 1, True, 54, 40.9)
         194 +(233, 0, False, 1000, 84.6)
         195 +(234, 1, True, 53, 35.0)
         196 +(235, 2, True, 45, 32.1)
         197 +(236, 1, True, 35, 20.3)
         198 +(237, 2, True, 61, 25.8)
         199 +(238, 1, True, 25, 11.3)
         200 +(239, 2, True, 48, 13.1)
         201 +success 194 / 200 mean steps 71.755
diff --git a/test_approach.py b/test_approach.py
index 33858d2..76f32da 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -1,9 +1,10 @@
    1      1  import sys, time, numpy as np
    2      2  from env_client import make_env
    3      3  from approach import GeneratedApproach
           4 +OC=None
    4      5  def run(seed, verbose=False):
    5      6      env = make_env()
    6        -    obs, info = env.reset(seed=seed)
           7 +    obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
    7      8      ap = GeneratedApproach(env.action_space, env.observation_space, {})
    8      9      t = time.time(); ap.reset(obs, info)
    9     10      ret = 0; steps = 0; term = False
@@ -18,6 +19,7 @@ def run(seed, verbose=False):
   18     19  if __name__ == "__main__":
   19     20      from concurrent.futures import ThreadPoolExecutor
   20     21      seeds = list(range(int(sys.argv[1]), int(sys.argv[2])))
          22 +    if len(sys.argv) > 3: OC = int(sys.argv[3])
   21     23      with ThreadPoolExecutor(8) as ex:
   22     24          res = list(ex.map(run, seeds))
   23     25      for r in res: print(r)
```

</details>

<a id="C007"></a>
### C007 · Rewrite: base-aware IK, base repositioning, grasp candidates incl. diagonal, stall detection, held-object replanning

Commit `1bb36b841fad1bb916712238ed5918d008a803b0`; parents: da7468c031192b7a13dd1c99654bff17d65faf62. Recorded author date: 2026-09-30T21:36:34+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0605](01_timeline.md#E0605): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_1bb36b8_approach.py) · [Exact all-file diff](evidence/diffs/C007_1bb36b8.diff)

[Previous saved controller snapshot](evidence/versions/C005_daa4226_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f7f0c1d..8744db5 100644
--- a/approach.py
+++ b/approach.py
@@ -108,6 +108,17 @@ def wrap(a):
  108    108  
  109    109  
  110    110  # ----------------------------------------------------------------------------- approach
         111 +TABLE_TOP = 0.075
         112 +MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
         113 +TABLE_X = (0.10, 0.50)
         114 +TABLE_Y = (-0.40, 0.40)
         115 +MAX_OPEN = 0.078            # max object width between the fingers
         116 +
         117 +
         118 +def _yaw_of(Rm):
         119 +    return np.arctan2(Rm[1, 0], Rm[0, 0])
         120 +
         121 +
  111    122  class GeneratedApproach:
  112    123      def __init__(self, action_space, observation_space, primitives):
  113    124          self.action_space = action_space
@@ -115,15 +126,17 @@ class GeneratedApproach:
  115    126  
  116    127      # ---------------------------------------------------------------- state helpers
  117    128      def _robot(self, state):
  118        -        for n in state.get_object_names():
  119        -            if n == "robot":
  120        -                return state.get_object_from_name(n)
  121        -        return None
         129 +        return state.get_object_from_name("robot")
  122    130  
  123    131      def _q(self, state):
  124    132          r = self._robot(state)
  125    133          return np.array([state.get(r, "joint_%d" % i) for i in range(1, 8)])
  126    134  
         135 +    def _base(self, state):
         136 +        r = self._robot(state)
         137 +        return np.array([state.get(r, "pos_base_x"), state.get(r, "pos_base_y"),
         138 +                         state.get(r, "pos_base_rot")])
         139 +
  127    140      def _boxes(self, state):
  128    141          out = {}
  129    142          for n in state.get_object_names():
@@ -134,259 +147,443 @@ class GeneratedApproach:
  134    147                  out[n] = dict(
  135    148                      x=state.get(o, "pose_x"), y=state.get(o, "pose_y"), z=state.get(o, "pose_z"),
  136    149                      hx=state.get(o, "half_extent_x"), hy=state.get(o, "half_extent_y"),
  137        -                    hz=state.get(o, "half_extent_z"), g=state.get(o, "grasp_active"))
         150 +                    hz=state.get(o, "half_extent_z"), g=state.get(o, "grasp_active"),
         151 +                    yaw=2 * np.arctan2(state.get(o, "pose_qz"), state.get(o, "pose_qw")))
  138    152              except Exception:
  139    153                  pass
  140    154          return out
  141    155  
         156 +    # ---------------------------------------------------------------- frames
         157 +    @staticmethod
         158 +    def _mount(base):
         159 +        c, s = np.cos(base[2]), np.sin(base[2])
         160 +        M = np.eye(4)
         161 +        M[:3, :3] = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
         162 +        M[0, 3] = base[0] + MOUNT_OFF * c
         163 +        M[1, 3] = base[1] + MOUNT_OFF * s
         164 +        return M
         165 +
         166 +    def _ee_world(self, q, base):
         167 +        T, _, _ = fk(q)
         168 +        return self._mount(base) @ T
         169 +
         170 +    def _ik_world(self, q0, pos, Rw, base, iters=100):
         171 +        M = self._mount(base)
         172 +        pa = M[:3, :3].T @ (np.asarray(pos) - M[:3, 3])
         173 +        Ra = M[:3, :3].T @ Rw
         174 +        return ik(q0, pa, Ra, iters=iters)
         175 +
         176 +    def _feasible(self, base, pos, yaw, seeds):
         177 +        """IK feasibility of a top-down pose from a few seeds; returns q or None."""
         178 +        Rw = down_R(yaw)
         179 +        for s in seeds:
         180 +            q, e = self._ik_world(s, pos, Rw, base, iters=150)
         181 +            if e < 1e-4:
         182 +                return q
         183 +        return None
         184 +
  142    185      # ---------------------------------------------------------------- episode
  143    186      def reset(self, state, info):
  144        -        self.segs = []          # queue of segments
         187 +        self.segs = []
  145    188          self.cur = None
  146    189          self.last_q = None
  147        -        self.last_cmd = None
  148        -        self.stuck = 0
  149        -        self.held = None
  150        -        self.moved = set()
  151        -        self.fail = {}
         190 +        self.last_base = None
         191 +        self.last_cmd = False
         192 +        self.fail = {}              # candidate key -> failures
         193 +        self.obj_fail = {}
  152    194          self.placed_spots = []
  153        -        self.yaw = 0.0
  154        -        self.done_flag = False
  155    195          self.pending_check = None
         196 +        self.best_d = None
         197 +        self.stall = 0
         198 +        self.q_home = self._q(state)
         199 +        self.nsteps = 0
         200 +        # a nominal top-down configuration used as an extra IK seed
         201 +        b = self._base(state)
         202 +        qn, e = self._ik_world(self.q_home, [0.30, 0.0, 0.33], down_R(0.0), b, iters=200)
         203 +        self.q_nom = qn
  156    204  
  157    205      # ---------------------------------------------------------------- geometry
  158        -    def _region(self, boxes):
  159        -        return boxes.get("target_region")
  160        -
  161    206      def _blocking(self, boxes):
  162        -        reg = self._region(boxes)
         207 +        reg = boxes["target_region"]
  163    208          res = []
  164    209          for n, b in boxes.items():
  165        -            if n in ("target_region", "target_block"):
         210 +            if n in ("target_region", "target_block") or b["g"] > 0.5:
  166    211                  continue
  167        -            if abs(b["x"] - reg["x"]) < b["hx"] + reg["hx"] + 0.003 and \
  168        -               abs(b["y"] - reg["y"]) < b["hy"] + reg["hy"] + 0.003 and \
         212 +            ex, ey = self._extent_xy(b)
         213 +            if abs(b["x"] - reg["x"]) < ex + reg["hx"] + 0.004 and \
         214 +               abs(b["y"] - reg["y"]) < ey + reg["hy"] + 0.004 and \
  169    215                 b["z"] - b["hz"] < reg["z"] + reg["hz"] + 0.08:
  170    216                  res.append(n)
  171    217          return res
  172    218  
  173        -    def _grasp_clear(self, boxes, name, yaw):
  174        -        """clearance of finger boxes from other objects for a top-down grasp"""
         219 +    @staticmethod
         220 +    def _extent_xy(b):
         221 +        c, s = abs(np.cos(b["yaw"])), abs(np.sin(b["yaw"]))
         222 +        return b["hx"] * c + b["hy"] * s, b["hx"] * s + b["hy"] * c
         223 +
         224 +    @staticmethod
         225 +    def _width_along(b, yaw):
         226 +        a = yaw - b["yaw"]
         227 +        c, s = abs(np.cos(a)), abs(np.sin(a))
         228 +        return 2 * (b["hx"] * c + b["hy"] * s), 2 * (b["hx"] * s + b["hy"] * c)
         229 +
         230 +    def _grasp_clear(self, boxes, name, yaw, tip):
         231 +        """Approximate clearance of the finger volumes (open + closing sweep) and the
         232 +        palm from other objects for a top-down grasp."""
  175    233          b = boxes[name]
  176        -        ax = np.array([np.cos(yaw), np.sin(yaw)])
  177        -        best = 1e9
  178        -        for sgn in (-1, 1):
  179        -            f = np.array([b["x"], b["y"]]) + sgn * FINGER_OFF * ax
  180        -            for n, o in boxes.items():
  181        -                if n == name or n == "target_region":
  182        -                    continue
  183        -                dx = abs(f[0] - o["x"]) - o["hx"]
  184        -                dy = abs(f[1] - o["y"]) - o["hy"]
  185        -                d = max(dx, dy)
  186        -                best = min(best, d)
         234 +        wu, wv = self._width_along(b, yaw)
         235 +        u = np.array([np.cos(yaw), np.sin(yaw)])
         236 +        v = np.array([-u[1], u[0]])
         237 +        c0 = np.array([b["x"], b["y"]])
         238 +        best = 1.0
         239 +        for n, o in boxes.items():
         240 +            if n == name or o["g"] > 0.5:
         241 +                continue
         242 +            otop = o["z"] + o["hz"]
         243 +            if n == "target_region":
         244 +                continue
         245 +            # z-overlap with finger volume (tip-0.015 .. tip+0.045) and palm (above)
         246 +            if otop < tip - 0.016:
         247 +                continue
         248 +            ex, ey = self._extent_xy(o)
         249 +            # sample the object's footprint corners/edges in gripper frame
         250 +            pts = []
         251 +            for fx in (-1, -0.5, 0, 0.5, 1):
         252 +                for fy in (-1, -0.5, 0, 0.5, 1):
         253 +                    pts.append([o["x"] + fx * ex, o["y"] + fy * ey])
         254 +            pts = np.array(pts) - c0
         255 +            pu = np.abs(pts @ u)
         256 +            pv = np.abs(pts @ v)
         257 +            # finger band: u in [wu/2, 0.068], |v| < 0.014
         258 +            du = np.maximum(wu / 2 - pu, pu - 0.068)
         259 +            dv = pv - 0.014
         260 +            d_f = np.min(np.maximum(du, dv))
         261 +            # palm: |u| < 0.07, |v| < 0.035, z > tip + 0.045
         262 +            if otop > tip + 0.040:
         263 +                d_p = np.min(np.maximum(pu - 0.07, pv - 0.035))
         264 +                d_f = min(d_f, d_p)
         265 +            best = min(best, d_f)
  187    266          return best
  188    267  
  189        -    def _choose_yaw(self, boxes, name, q):
         268 +    def _grasp_candidates(self, boxes, name):
  190    269          b = boxes[name]
         270 +        support = b["z"] - b["hz"]
         271 +        top = b["z"] + b["hz"]
         272 +        tip0 = min(max(b["z"], support + 0.017), top - 0.001)
         273 +        tips = [tip0, min(tip0 + 0.004, top - 0.001), top - 0.002]
  191    274          cands = []
  192        -        for yaw in (0.0, PI / 2):
  193        -            width = 2 * (b["hx"] if yaw == 0.0 else b["hy"])
  194        -            if width > 0.082:
         275 +        for yaw in (b["yaw"], b["yaw"] + PI / 2, b["yaw"] + PI / 4, b["yaw"] - PI / 4):
         276 +            yaw = wrap(yaw)
         277 +            wu, wv = self._width_along(b, yaw)
         278 +            if wu > MAX_OPEN:
  195    279                  continue
  196        -            clr = self._grasp_clear(boxes, name, yaw)
  197        -            cands.append((min(clr, 0.03) - 0.2 * width, yaw))
  198        -        if not cands:
  199        -            return None
  200        -        cands.sort(reverse=True)
  201        -        yaw = cands[0][1]
  202        -        k = self.fail.get(name, 0)
  203        -        if k % 2 == 1 and len(cands) > 1:
  204        -            yaw = cands[1][1]
  205        -        return self._best_equiv_yaw(yaw, q)
  206        -
  207        -    def _best_equiv_yaw(self, yaw, q):
  208        -        # yaw and yaw+pi are equivalent grasps; pick the one nearer the current tool yaw
  209        -        T, _, _ = fk(q)
  210        -        cur = np.arctan2(T[1, 0], T[0, 0])
  211        -        opts = [yaw, wrap(yaw + PI)]
  212        -        return min(opts, key=lambda a: abs(wrap(a - cur)))
  213        -
  214        -    def _safe_z(self, boxes, held_hz=0.0, held_off=0.0):
  215        -        top = 0.1
         280 +            for ti, tip in enumerate(tips):
         281 +                if tip < support + 0.0125:
         282 +                    continue
         283 +                key = (name, round(yaw, 3), round(tip, 4))
         284 +                if self.fail.get(key, 0) > 0:
         285 +                    continue
         286 +                clr = self._grasp_clear(boxes, name, yaw, tip)
         287 +                diag = 0 if abs(wrap(2 * (yaw - b["yaw"]))) < 0.1 else 1
         288 +                score = min(clr, 0.02) - 0.004 * diag - 0.003 * ti - 0.1 * wu * (clr > 0.005)
         289 +                cands.append((score, yaw, tip, key, clr))
         290 +        cands.sort(key=lambda c: -c[0])
         291 +        return cands
         292 +
         293 +    def _safe_z(self, boxes, exclude=None, held_below=0.0):
         294 +        top = TABLE_TOP + 0.03
  216    295          for n, b in boxes.items():
  217        -            if b["g"] > 0.5:
         296 +            if b["g"] > 0.5 or n == exclude:
  218    297                  continue
  219    298              top = max(top, b["z"] + b["hz"])
  220        -        return max(0.34, top + 0.03 + held_hz + held_off + FINGER)
         299 +        return max(0.33, top + 0.025 + held_below + FINGER)
  221    300  
  222        -    def _drop_spot(self, boxes, name):
  223        -        reg = self._region(boxes)
         301 +    def _drop_spot(self, boxes, name, base, seeds, safe):
         302 +        reg = boxes["target_region"]
  224    303          b = boxes[name]
  225        -        best, bs = None, -1e9
  226        -        for x in np.arange(0.15, 0.46, 0.025):
  227        -            for y in np.arange(-0.3, 0.31, 0.025):
  228        -                clr = 1e9
         304 +        bex, bey = self._extent_xy(b)
         305 +        cands = []
         306 +        for x in np.arange(TABLE_X[0] + 0.06, TABLE_X[1] - 0.03, 0.025):
         307 +            for y in np.arange(TABLE_Y[0] + 0.05, TABLE_Y[1] - 0.049, 0.025):
         308 +                if x < 0.2 and abs(y) < 0.14:
         309 +                    continue
         310 +                clr = 1.0
  229    311                  for n, o in boxes.items():
  230    312                      if n == name:
  231    313                          continue
  232        -                    m = 0.05 if n != "target_region" else 0.03
  233        -                    dx = abs(x - o["x"]) - o["hx"] - b["hx"] - m
  234        -                    dy = abs(y - o["y"]) - o["hy"] - b["hy"] - m
         314 +                    ex, ey = self._extent_xy(o)
         315 +                    m = 0.06 if n != "target_region" else 0.03
         316 +                    if n == "target_block":
         317 +                        m = 0.075
         318 +                    dx = abs(x - o["x"]) - ex - bex - m
         319 +                    dy = abs(y - o["y"]) - ey - bey - m
  235    320                      clr = min(clr, max(dx, dy))
  236    321                  for (px, py) in self.placed_spots:
  237        -                    clr = min(clr, max(abs(x - px), abs(y - py)) - 0.08)
         322 +                    clr = min(clr, max(abs(x - px), abs(y - py)) - 0.07)
  238    323                  dist = np.hypot(x - b["x"], y - b["y"])
  239        -                score = min(clr, 0.04) * 10 - dist
  240        -                if score > bs:
  241        -                    bs, best = score, (x, y)
  242        -        return best
         324 +                cands.append((min(clr, 0.03) * 10 - dist, x, y))
         325 +        cands.sort(key=lambda c: -c[0])
         326 +        for sc, x, y in cands[:25]:
         327 +            if self._feasible(base, [x, y, safe], 0.0, seeds) is not None:
         328 +                return (x, y)
         329 +        return (cands[0][1], cands[0][2])
         330 +
         331 +    # ---------------------------------------------------------------- base selection
         332 +    def _choose_base(self, base, poses, seeds):
         333 +        """Return a base pose from which all (pos, yaw) poses are IK-feasible, preferring
         334 +        the current base.  Returns (base, ok)."""
         335 +        def ok(bb):
         336 +            ss = list(seeds)
         337 +            for pos, yaw in poses:
         338 +                q = self._feasible(bb, pos, yaw, ss)
         339 +                if q is None:
         340 +                    return False
         341 +                ss = [q] + ss
         342 +            return True
         343 +        if ok(base):
         344 +            return base, True
         345 +        cx = np.mean([p[0][0] for p in poses])
         346 +        cy = np.mean([p[0][1] for p in poses])
         347 +        cands = []
         348 +        for dx in (0.0, -0.05, -0.1, -0.15, -0.2, -0.25, 0.05):
         349 +            for dy in (0.0, -0.1, 0.1, -0.2, 0.2):
         350 +                bx = min(base[0] + dx, -0.08)
         351 +                by = base[1] + dy
         352 +                # prefer reach distance ~0.35-0.45 from mount
         353 +                mx = bx + MOUNT_OFF
         354 +                r = np.hypot(cx - mx, cy - by)
         355 +                cost = abs(dx) + abs(dy) + 0.5 * abs(r - 0.4)
         356 +                cands.append((cost, np.array([bx, by, 0.0])))
         357 +        cands.sort(key=lambda c: c[0])
         358 +        for cost, bb in cands:
         359 +            if ok(bb):
         360 +                return bb, True
         361 +        return base, False
  243    362  
  244    363      # ---------------------------------------------------------------- planning
  245        -    def _plan_pick_place(self, state, name, place_xy, place_bottom, final_yaw=None):
  246        -        boxes = self._boxes(state)
         364 +    def _plan_pick(self, state, boxes, name, cand):
         365 +        """Segments to pick object `name` with candidate (yaw, tip)."""
  247    366          q = self._q(state)
         367 +        base = self._base(state)
  248    368          b = boxes[name]
  249        -        yaw = self._choose_yaw(boxes, name, q)
  250        -        if yaw is None:
  251        -            yaw = self._best_equiv_yaw(0.0, q)
  252        -        T, _, _ = fk(q)
  253        -        safe0 = self._safe_z(boxes)
  254        -        # fingertip at object centre (but not below support+5mm)
  255        -        k = self.fail.get(name, 0)
  256        -        tip = max(b["z"], b["z"] - b["hz"] + 0.017)
  257        -        tip = tip + [0.0, 0.003, -0.002, 0.006, 0.0, 0.003][k % 6]
  258        -        tip = min(tip, b["z"] + b["hz"] - 0.001)
         369 +        yaw, tip = cand
         370 +        seeds = [q, self.q_nom, self.q_home]
         371 +        safe = self._safe_z(boxes)
  259    372          grasp_z = tip + FINGER
  260        -        off = grasp_z - b["z"]          # EE z - object centre z while held
  261        -        safe1 = max(self._safe_z(boxes, b["hz"], 0.0) , b["hz"] + off + 0.03 + 0.15)
  262        -        safe1 = max(safe1, self._safe_z({k: v for k, v in boxes.items() if k != name}) + b["hz"])
         373 +        above = np.array([b["x"], b["y"], safe])
         374 +        gpos = np.array([b["x"], b["y"], grasp_z])
         375 +        # choose equivalent yaw (yaw or yaw+pi) closest to current tool yaw
         376 +        Tw = self._ee_world(q, base)
         377 +        cur_yaw = _yaw_of(Tw[:3, :3])
         378 +        opts = sorted([yaw, wrap(yaw + PI)], key=lambda a: abs(wrap(a - cur_yaw)))
         379 +        for y in opts:
         380 +            nb, ok = self._choose_base(base, [(above, y), (gpos, y)], seeds)
         381 +            if ok:
         382 +                yaw = y
         383 +                break
  263    384          segs = []
  264        -        segs.append(("move", np.array([T[0, 3], T[1, 3], max(T[2, 3], safe0)]), None))
  265        -        segs.append(("move", np.array([b["x"], b["y"], max(safe0, safe1)]), yaw))
  266        -        segs.append(("move", np.array([b["x"], b["y"], grasp_z]), yaw, "grasp_descend", name))
         385 +        segs.append(("move", np.array([Tw[0, 3], Tw[1, 3], max(Tw[2, 3], safe)]), None, "lift"))
         386 +        if np.max(np.abs(nb - base)) > 1e-6:
         387 +            segs.append(("base", nb))
         388 +        segs.append(("move", above, yaw, "travel"))
         389 +        segs.append(("move", gpos, yaw, "grasp_descend", name))
  267    390          segs.append(("grip", -1.0, name))
  268        -        segs.append(("move", np.array([b["x"], b["y"], safe1]), yaw))
  269        -        pyaw = yaw if final_yaw is None else final_yaw
  270        -        place_z = place_bottom + b["hz"] + off
  271        -        segs.append(("move", np.array([place_xy[0], place_xy[1], safe1]), pyaw))
  272        -        segs.append(("move", np.array([place_xy[0], place_xy[1], place_z]), pyaw, "place_descend"))
         391 +        return segs
         392 +
         393 +    def _plan_place(self, state, boxes, name, place_xy, bottom):
         394 +        """Segments to place currently-held object `name` with its bottom at `bottom`."""
         395 +        q = self._q(state)
         396 +        base = self._base(state)
         397 +        b = boxes[name]
         398 +        Tw = self._ee_world(q, base)
         399 +        yaw = _yaw_of(Tw[:3, :3])
         400 +        off = Tw[2, 3] - b["z"]                 # EE z - object centre z
         401 +        # xy offset of object centre relative to EE (in world, keep yaw constant)
         402 +        dxy = np.array([b["x"] - Tw[0, 3], b["y"] - Tw[1, 3]])
         403 +        seeds = [q, self.q_nom, self.q_home]
         404 +        safe = max(self._safe_z(boxes, exclude=name, held_below=b["hz"] + off - FINGER),
         405 +                   Tw[2, 3])
         406 +        safe = max(safe, bottom + b["hz"] + off + 0.03)
         407 +        ex = np.array([place_xy[0] - dxy[0], place_xy[1] - dxy[1]])
         408 +        pz = bottom + b["hz"] + off
         409 +        above = np.array([ex[0], ex[1], safe])
         410 +        ppos = np.array([ex[0], ex[1], pz])
         411 +        nb, ok = self._choose_base(base, [(above, yaw), (ppos, yaw)], seeds)
         412 +        segs = []
         413 +        segs.append(("move", np.array([Tw[0, 3], Tw[1, 3], safe]), yaw, "lift"))
         414 +        if np.max(np.abs(nb - base)) > 1e-6:
         415 +            segs.append(("base", nb))
         416 +        segs.append(("move", above, yaw, "travel"))
         417 +        segs.append(("move", ppos, yaw, "place_descend"))
  273    418          segs.append(("grip", 1.0, None))
  274        -        segs.append(("move", np.array([place_xy[0], place_xy[1], max(safe1, place_z + 0.05)]), pyaw))
         419 +        segs.append(("move", np.array([ex[0], ex[1], pz + 0.06]), yaw, "retreat"))
  275    420          return segs
  276    421  
         422 +    def _held(self, boxes):
         423 +        for n, b in boxes.items():
         424 +            if b["g"] > 0.5:
         425 +                return n
         426 +        return None
         427 +
  277    428      def _replan(self, state):
  278    429          boxes = self._boxes(state)
  279        -        reg = self._region(boxes)
  280        -        blk = self._blocking(boxes)
  281        -        blk = [n for n in blk if self.fail.get(n, 0) < 6]
  282        -        if blk:
  283        -            # most accessible first: highest grasp clearance
  284        -            q = self._q(state)
  285        -            blk.sort(key=lambda n: -max(self._grasp_clear(boxes, n, 0.0),
  286        -                                         self._grasp_clear(boxes, n, PI / 2)))
  287        -            name = blk[0]
  288        -            spot = self._drop_spot(boxes, name)
         430 +        reg = boxes["target_region"]
         431 +        held = self._held(boxes)
         432 +        r = self._robot(state)
         433 +        if held is None and state.get(r, "grasp_active") > 0.5:
         434 +            held = None
         435 +        if held is not None:
         436 +            if held == "target_block" and not self._blocking(boxes):
         437 +                return self._plan_place(state, boxes, held, (reg["x"], reg["y"]),
         438 +                                        reg["z"] + reg["hz"] + 0.0005)
         439 +            if held == "target_block":
         440 +                # should not happen often: park the block somewhere free
         441 +                base = self._base(state)
         442 +                seeds = [self._q(state), self.q_nom, self.q_home]
         443 +                spot = self._drop_spot(boxes, held, base, seeds, self._safe_z(boxes))
         444 +                return self._plan_place(state, boxes, held, spot, TABLE_TOP + 0.001)
         445 +            base = self._base(state)
         446 +            seeds = [self._q(state), self.q_nom, self.q_home]
         447 +            spot = self._drop_spot(boxes, held, base, seeds, self._safe_z(boxes))
  289    448              self.placed_spots.append(spot)
  290        -            b = boxes[name]
  291        -            bottom = 0.075 + 0.002
  292        -            return self._plan_pick_place(state, name, spot, bottom)
  293        -        # place target block
  294        -        tb = boxes["target_block"]
  295        -        return self._plan_pick_place(state, "target_block", (reg["x"], reg["y"]),
  296        -                                     reg["z"] + reg["hz"] + 0.0005)
         449 +            return self._plan_place(state, boxes, held, spot, TABLE_TOP + 0.0015)
         450 +        blk = self._blocking(boxes)
         451 +        targets = blk if blk else ["target_block"]
         452 +        best = None
         453 +        for n in targets:
         454 +            cands = self._grasp_candidates(boxes, n)
         455 +            if cands:
         456 +                c = cands[0]
         457 +                if best is None or c[0] > best[0][0]:
         458 +                    best = (c, n)
         459 +        if best is None:
         460 +            # everything failed once: reset failure memory and retry
         461 +            self.fail = {}
         462 +            for n in targets:
         463 +                cands = self._grasp_candidates(boxes, n)
         464 +                if cands:
         465 +                    best = (cands[0], n)
         466 +                    break
         467 +        if best is None:
         468 +            T = self._ee_world(self._q(state), self._base(state))
         469 +            return [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.02]), None, "lift")]
         470 +        c, n = best
         471 +        self.cur_key = c[3]
         472 +        return self._plan_pick(state, boxes, n, (c[1], c[2]))
  297    473  
  298    474      # ---------------------------------------------------------------- control
  299    475      def get_action(self, state):
         476 +        self.nsteps += 1
  300    477          q = self._q(state)
         478 +        base = self._base(state)
  301    479          act = np.zeros(11, dtype=np.float32)
  302        -        # detect rejected motion
  303    480          rejected = False
  304        -        if self.last_cmd is not None and self.last_q is not None:
  305        -            if np.max(np.abs(self.last_cmd)) > 1e-6 and np.max(np.abs(q - self.last_q)) < 1e-7:
         481 +        if self.last_cmd and self.last_q is not None:
         482 +            if np.max(np.abs(q - self.last_q)) < 1e-7 and \
         483 +               np.max(np.abs(base - self.last_base)) < 1e-7:
  306    484                  rejected = True
  307    485          self.last_q = q.copy()
  308        -        self.last_cmd = None
         486 +        self.last_base = base.copy()
         487 +        self.last_cmd = False
  309    488  
  310    489          if self.pending_check is not None:
  311    490              name = self.pending_check
  312    491              self.pending_check = None
  313    492              r = self._robot(state)
  314    493              if state.get(r, "grasp_active") < 0.5:
  315        -                self.fail[name] = self.fail.get(name, 0) + 1
  316        -                T, _, _ = fk(q)
  317        -                self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.05]), None)]
         494 +                key = getattr(self, "cur_key", None)
         495 +                if key is not None:
         496 +                    self.fail[key] = self.fail.get(key, 0) + 1
         497 +                self.segs = []
  318    498                  self.cur = None
  319        -        if rejected and self.cur is not None and self.cur[0] == "move":
         499 +
         500 +        if rejected and self.cur is not None and self.cur[0] in ("move", "base"):
  320    501              self._handle_reject(state)
  321    502  
  322        -        for _ in range(20):
         503 +        for _ in range(30):
  323    504              if self.cur is None:
  324    505                  if not self.segs:
  325    506                      self.segs = self._replan(state)
  326    507                  self.cur = self.segs.pop(0)
  327        -                self.stuck = 0
         508 +                self.best_d = None
         509 +                self.stall = 0
  328    510              seg = self.cur
  329    511              if seg[0] == "grip":
  330    512                  act[10] = seg[1]
  331    513                  self.cur = None
  332    514                  self.pending_check = seg[2] if seg[1] < 0 else None
  333        -                self.last_cmd = np.zeros(7)
  334    515                  return act
  335        -            # move segment
         516 +            if seg[0] == "base":
         517 +                d = seg[1] - base
         518 +                d[2] = wrap(d[2])
         519 +                if np.max(np.abs(d)) < 1e-6:
         520 +                    self.cur = None
         521 +                    continue
         522 +                act[0:3] = np.clip(d, -0.2, 0.2)
         523 +                self.last_cmd = True
         524 +                return act
  336    525              goal, yaw = seg[1], seg[2]
  337        -            T, _, _ = fk(q)
         526 +            Tw = self._ee_world(q, base)
  338    527              if yaw is None:
  339        -                Rt = T[:3, :3]
  340        -                Rt = down_R(np.arctan2(T[1, 0], T[0, 0])) if abs(T[2, 2] + 1) < 0.2 else Rt
         528 +                Rt = down_R(_yaw_of(Tw[:3, :3])) if Tw[2, 2] < -0.8 else Tw[:3, :3]
  341    529              else:
  342    530                  Rt = down_R(yaw)
  343        -            p = T[:3, 3]
         531 +            p = Tw[:3, 3]
  344    532              d = goal - p
  345        -            rerr = np.linalg.norm(_rotvec(Rt @ T[:3, :3].T))
  346        -            if np.linalg.norm(d) < 5e-4 and rerr < 2e-3:
         533 +            nd = np.linalg.norm(d)
         534 +            rerr = np.linalg.norm(_rotvec(Rt @ Tw[:3, :3].T))
         535 +            if nd < 5e-4 and rerr < 2e-3:
  347    536                  self.cur = None
  348    537                  continue
  349        -            # intermediate cartesian target
         538 +            # stall detection
         539 +            prog = nd + 0.1 * rerr
         540 +            if self.best_d is None or prog < self.best_d - 2e-4:
         541 +                self.best_d = prog
         542 +                self.stall = 0
         543 +            else:
         544 +                self.stall += 1
         545 +                if self.stall >= 4:
         546 +                    if nd < 3e-3 and rerr < 2e-2:
         547 +                        self.cur = None
         548 +                        continue
         549 +                    self._handle_reject(state)
         550 +                    continue
  350    551              step = 0.08
  351        -            nd = np.linalg.norm(d)
  352    552              tgt = goal if nd < step else p + d * step / nd
  353        -            qt, err = ik(q, tgt, Rt)
         553 +            qt, err = self._ik_world(q, tgt, Rt, base)
  354    554              dq = qt - q
  355    555              m = np.max(np.abs(dq))
  356    556              if m > 0.2:
  357    557                  dq *= 0.2 / m
  358        -            if m < 1e-6:
  359        -                self.cur = None
         558 +            if m < 1e-7:
         559 +                self.stall += 1
  360    560                  continue
  361    561              act[3:10] = dq.astype(np.float32)
  362        -            self.last_cmd = dq
         562 +            self.last_cmd = True
  363    563              return act
  364    564          return act
  365    565  
  366    566      def _handle_reject(self, state):
  367    567          seg = self.cur
  368        -        tag = seg[3] if len(seg) > 3 else None
  369        -        self.stuck += 1
         568 +        tag = seg[3] if (seg[0] == "move" and len(seg) > 3) else None
         569 +        q = self._q(state)
         570 +        base = self._base(state)
         571 +        T = self._ee_world(q, base)
  370    572          if tag == "place_descend":
  371        -            # contact: just release here
         573 +            # contact: release here (object is resting on something)
  372    574              self.cur = None
  373    575              return
  374    576          if tag == "grasp_descend":
  375        -            # can't reach grasp pose: grasp at current height if fingertips reach object, else retry
  376        -            name = seg[4]
  377        -            boxes = self._boxes(state)
  378        -            b = boxes[name]
  379        -            T, _, _ = fk(self._q(state))
  380        -            tip = T[2, 3] - FINGER
  381        -            if tip < b["z"] + b["hz"] - 0.006:
  382        -                self.cur = None
  383        -                return
  384        -            self.fail[name] = self.fail.get(name, 0) + 1
  385        -            T, _, _ = fk(self._q(state))
  386        -            self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.08]), None)]
         577 +            key = getattr(self, "cur_key", None)
         578 +            if key is not None:
         579 +                self.fail[key] = self.fail.get(key, 0) + 1
         580 +            self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.06]), None, "lift")]
         581 +            self.cur = None
         582 +            return
         583 +        if seg[0] == "base":
         584 +            self.segs = []
  387    585              self.cur = None
  388    586              return
  389    587          # generic: go up a bit, then replan
  390        -        T, _, _ = fk(self._q(state))
  391        -        self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.03]), None)]
         588 +        self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.04]), None, "lift")]
  392    589          self.cur = None
diff --git a/dbg_run.py b/dbg_run.py
index bbc2a19..659869e 100644
--- a/dbg_run.py
+++ b/dbg_run.py
@@ -1,6 +1,7 @@
    1      1  import sys, numpy as np
    2      2  from env_client import make_env
    3      3  from approach import GeneratedApproach, fk
           4 +import approach as AP
    4      5  seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 1000
    5      6  env = make_env(); obs, info = env.reset(seed=seed)
    6      7  ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
@@ -10,9 +11,9 @@ lastseg=None
   10     11  for t in range(N):
   11     12      a = ap.get_action(obs)
   12     13      seg = ap.cur
   13        -    key = None if seg is None else (seg[0], tuple(np.round(seg[1],3)) if seg[0]=='move' else seg[1], seg[2] if seg[0]=='move' and seg[2] is None else (round(seg[2],2) if seg[0]=='move' else seg[2]), seg[3] if len(seg)>3 else '')
          14 +    key = None if seg is None else tuple((tuple(np.round(v,3)) if isinstance(v,np.ndarray) else (round(v,2) if isinstance(v,float) else v)) for v in seg)
   14     15      obs, r, term, trunc, info = env.step(a)
   15        -    q = ap._q(obs); T,_,_ = fk(q)
          16 +    q = ap._q(obs); T = ap._ee_world(q, ap._base(obs))
   16     17      rob = ap._robot(obs)
   17     18      if key != lastseg or np.allclose(q, ap.last_q):
   18     19          print(t, key, "ee", np.round(T[:3,3],3), "grasp", obs.get(rob,'grasp_active'), "REJ" if np.allclose(q, ap.last_q) and np.any(a[3:10]!=0) else "")
```

</details>

<a id="C008"></a>
### C008 · tests: object_count option

Commit `36264e4a78bdaba568d450c368168376990a2309`; parents: 1bb36b841fad1bb916712238ed5918d008a803b0. Recorded author date: 2026-09-30T21:51:13+02:00.

File roles (automatic): setup/other.

- [E0658](01_timeline.md#E0658): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C008_36264e4.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res_a.txt b/res_a.txt
new file mode 100644
index 0000000..37c6321
--- /dev/null
+++ b/res_a.txt
@@ -0,0 +1,101 @@
           1 +(0, 2, True, 54, 32.9)
           2 +(1, 1, True, 47, 24.6)
           3 +(2, 2, True, 61, 44.9)
           4 +(3, 2, True, 43, 27.8)
           5 +(4, 2, True, 57, 36.6)
           6 +(5, 2, True, 59, 45.6)
           7 +(6, 1, True, 41, 18.3)
           8 +(7, 2, True, 52, 29.3)
           9 +(8, 2, True, 53, 47.4)
          10 +(9, 1, True, 34, 26.4)
          11 +(10, 2, True, 38, 33.4)
          12 +(11, 0, True, 24, 19.0)
          13 +(12, 1, True, 44, 37.8)
          14 +(13, 2, True, 58, 46.7)
          15 +(14, 0, True, 17, 11.9)
          16 +(15, 2, True, 39, 25.8)
          17 +(16, 1, True, 33, 21.8)
          18 +(17, 2, True, 57, 46.0)
          19 +(18, 2, True, 40, 30.9)
          20 +(19, 1, True, 43, 32.6)
          21 +(20, 2, True, 62, 54.0)
          22 +(21, 0, True, 32, 26.1)
          23 +(22, 2, True, 38, 32.4)
          24 +(23, 0, True, 30, 29.4)
          25 +(24, 1, True, 27, 27.1)
          26 +(25, 1, True, 49, 44.7)
          27 +(26, 2, True, 42, 45.8)
          28 +(27, 0, True, 37, 29.1)
          29 +(28, 1, True, 54, 50.8)
          30 +(29, 2, True, 23, 19.9)
          31 +(30, 0, True, 31, 27.2)
          32 +(31, 1, True, 56, 55.3)
          33 +(32, 2, True, 50, 48.5)
          34 +(33, 2, True, 52, 57.6)
          35 +(34, 0, True, 22, 19.2)
          36 +(35, 0, True, 25, 21.4)
          37 +(36, 1, True, 35, 25.7)
          38 +(37, 0, True, 25, 19.2)
          39 +(38, 0, True, 23, 24.5)
          40 +(39, 2, True, 60, 65.9)
          41 +(40, 1, True, 90, 56.5)
          42 +(41, 1, True, 33, 28.7)
          43 +(42, 0, True, 23, 16.3)
          44 +(43, 1, True, 38, 22.5)
          45 +(44, 2, True, 39, 34.7)
          46 +(45, 2, True, 49, 39.4)
          47 +(46, 1, True, 31, 21.6)
          48 +(47, 0, True, 17, 12.1)
          49 +(48, 0, True, 19, 16.4)
          50 +(49, 0, True, 21, 25.0)
          51 +(50, 2, True, 58, 51.8)
          52 +(51, 1, True, 34, 27.6)
          53 +(52, 2, True, 60, 59.1)
          54 +(53, 2, True, 56, 47.3)
          55 +(54, 0, True, 22, 20.2)
          56 +(55, 2, True, 60, 59.1)
          57 +(56, 1, True, 36, 25.0)
          58 +(57, 0, True, 21, 13.2)
          59 +(58, 1, True, 34, 35.6)
          60 +(59, 2, True, 72, 65.3)
          61 +(60, 0, True, 20, 18.4)
          62 +(61, 1, True, 42, 33.8)
          63 +(62, 1, True, 37, 29.2)
          64 +(63, 1, True, 40, 32.7)
          65 +(64, 1, True, 38, 28.3)
          66 +(65, 0, True, 35, 30.5)
          67 +(66, 2, True, 50, 42.8)
          68 +(67, 2, True, 53, 49.6)
          69 +(68, 1, True, 22, 22.1)
          70 +(69, 0, True, 21, 14.6)
          71 +(70, 1, True, 47, 41.5)
          72 +(71, 2, True, 64, 54.1)
          73 +(72, 2, True, 62, 56.2)
          74 +(73, 2, True, 44, 36.5)
          75 +(74, 0, True, 18, 12.6)
          76 +(75, 1, True, 30, 18.6)
          77 +(76, 1, True, 52, 43.4)
          78 +(77, 0, True, 25, 16.3)
          79 +(78, 2, True, 38, 31.4)
          80 +(79, 0, True, 17, 11.9)
          81 +(80, 2, True, 51, 37.0)
          82 +(81, 0, True, 27, 21.5)
          83 +(82, 2, True, 56, 42.4)
          84 +(83, 2, True, 38, 29.5)
          85 +(84, 1, True, 36, 24.9)
          86 +(85, 2, True, 48, 36.8)
          87 +(86, 2, True, 51, 40.0)
          88 +(87, 1, True, 46, 39.6)
          89 +(88, 1, True, 41, 26.8)
          90 +(89, 2, True, 52, 54.3)
          91 +(90, 1, True, 34, 27.0)
          92 +(91, 2, True, 42, 37.7)
          93 +(92, 1, True, 37, 35.0)
          94 +(93, 2, True, 55, 39.2)
          95 +(94, 0, True, 25, 23.4)
          96 +(95, 1, True, 43, 27.1)
          97 +(96, 2, True, 60, 29.8)
          98 +(97, 0, True, 28, 18.0)
          99 +(98, 1, True, 49, 13.1)
         100 +(99, 2, True, 48, 9.4)
         101 +success 100 / 100 mean steps 41.02
diff --git a/res_oc4.txt b/res_oc4.txt
new file mode 100644
index 0000000..c737bc6
--- /dev/null
+++ b/res_oc4.txt
@@ -0,0 +1,31 @@
           1 +(0, 4, True, 81, 44.6)
           2 +(1, 4, True, 70, 52.0)
           3 +(2, 4, True, 77, 55.5)
           4 +(3, 4, True, 58, 33.4)
           5 +(4, 4, False, 1000, 241.2)
           6 +(5, 4, True, 97, 58.5)
           7 +(6, 4, True, 90, 57.6)
           8 +(7, 4, True, 93, 62.2)
           9 +(8, 4, True, 89, 58.0)
          10 +(9, 4, True, 83, 59.1)
          11 +(10, 4, True, 79, 60.2)
          12 +(11, 4, True, 86, 63.4)
          13 +(12, 4, True, 113, 81.9)
          14 +(13, 4, True, 90, 59.5)
          15 +(14, 4, True, 48, 22.4)
          16 +(15, 4, True, 87, 65.0)
          17 +(16, 4, True, 50, 35.4)
          18 +(17, 4, True, 75, 51.0)
          19 +(18, 4, True, 54, 34.8)
          20 +(19, 4, True, 90, 57.5)
          21 +(20, 4, True, 79, 52.5)
          22 +(21, 4, True, 79, 53.9)
          23 +(22, 4, True, 53, 31.3)
          24 +(23, 4, True, 104, 59.5)
          25 +(24, 4, True, 73, 41.0)
          26 +(25, 4, True, 60, 35.1)
          27 +(26, 4, True, 71, 30.7)
          28 +(27, 4, True, 86, 29.8)
          29 +(28, 4, True, 88, 27.7)
          30 +(29, 4, True, 59, 16.9)
          31 +success 29 / 30 mean steps 108.73333333333333
```

</details>

<a id="C009"></a>
### C009 · adaptive step scale on rejection; finer steps near objects

Commit `2e2235a14f09be87db9d1e5afe9073add038773b`; parents: 36264e4a78bdaba568d450c368168376990a2309. Recorded author date: 2026-09-30T21:52:06+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0672](01_timeline.md#E0672): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_2e2235a_approach.py) · [Exact all-file diff](evidence/diffs/C009_2e2235a.diff)

[Previous saved controller snapshot](evidence/versions/C007_1bb36b8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8744db5..744426d 100644
--- a/approach.py
+++ b/approach.py
@@ -197,6 +197,8 @@ class GeneratedApproach:
  197    197          self.stall = 0
  198    198          self.q_home = self._q(state)
  199    199          self.nsteps = 0
         200 +        self.scale = 1.0
         201 +        self.max_top = 0.15
  200    202          # a nominal top-down configuration used as an extra IK seed
  201    203          b = self._base(state)
  202    204          qn, e = self._ik_world(self.q_home, [0.30, 0.0, 0.33], down_R(0.0), b, iters=200)
@@ -474,6 +476,8 @@ class GeneratedApproach:
  474    476      # ---------------------------------------------------------------- control
  475    477      def get_action(self, state):
  476    478          self.nsteps += 1
         479 +        boxes0 = self._boxes(state)
         480 +        self.max_top = max([b["z"] + b["hz"] for n, b in boxes0.items() if b["g"] < 0.5] + [0.1])
  477    481          q = self._q(state)
  478    482          base = self._base(state)
  479    483          act = np.zeros(11, dtype=np.float32)
@@ -497,8 +501,15 @@ class GeneratedApproach:
  497    501                  self.segs = []
  498    502                  self.cur = None
  499    503  
         504 +        if rejected:
         505 +            self.scale = max(self.scale * 0.35, 0.01)
         506 +        elif self.last_q is not None:
         507 +            self.scale = min(1.0, self.scale * 1.5)
  500    508          if rejected and self.cur is not None and self.cur[0] in ("move", "base"):
  501        -            self._handle_reject(state)
         509 +            if self.scale > 0.02 and self.cur[0] == "move":
         510 +                pass            # retry the same segment with a smaller step
         511 +            else:
         512 +                self._handle_reject(state)
  502    513  
  503    514          for _ in range(30):
  504    515              if self.cur is None:
@@ -549,12 +560,17 @@ class GeneratedApproach:
  549    560                      self._handle_reject(state)
  550    561                      continue
  551    562              step = 0.08
         563 +            low = p[2] - FINGER < self.max_top + 0.03
         564 +            if low and seg[3] in ("lift", "grasp_descend", "place_descend", "retreat"):
         565 +                step = 0.03
         566 +            step *= self.scale
  552    567              tgt = goal if nd < step else p + d * step / nd
  553    568              qt, err = self._ik_world(q, tgt, Rt, base)
  554    569              dq = qt - q
  555    570              m = np.max(np.abs(dq))
  556        -            if m > 0.2:
  557        -                dq *= 0.2 / m
         571 +            lim = 0.2 * max(self.scale, 0.05)
         572 +            if m > lim:
         573 +                dq *= lim / m
  558    574              if m < 1e-7:
  559    575                  self.stall += 1
  560    576                  continue
diff --git a/dbg_run.py b/dbg_run.py
index 659869e..d434e54 100644
--- a/dbg_run.py
+++ b/dbg_run.py
@@ -2,8 +2,8 @@ import sys, numpy as np
    2      2  from env_client import make_env
    3      3  from approach import GeneratedApproach, fk
    4      4  import approach as AP
    5        -seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 1000
    6        -env = make_env(); obs, info = env.reset(seed=seed)
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 1000; OC=int(sys.argv[3]) if len(sys.argv)>3 else None
           6 +env = make_env(); obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None))
    7      7  ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    8      8  bx = ap._boxes(obs)
    9      9  for n,b in sorted(bx.items()): print(n, {k: round(v,3) for k,v in b.items()})
diff --git a/probe_lift.py b/probe_lift.py
new file mode 100644
index 0000000..74329a9
--- /dev/null
+++ b/probe_lift.py
@@ -0,0 +1,18 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach, down_R
           4 +env = make_env(); obs, info = env.reset(seed=4, options={"object_count":4})
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           6 +for t in range(34):
           7 +    a = ap.get_action(obs); obs,*_ = env.step(a)
           8 +bx = ap._boxes(obs)
           9 +for n in ['obstruction0','obstruction1','obstruction2']: print(n, {k: round(v,4) for k,v in bx[n].items()})
          10 +R=ap._robot(obs); print("finger", obs.get(R,'finger_state'), np.round(obs.data[R][11:],4))
          11 +q=ap._q(obs); base=ap._base(obs); T=ap._ee_world(q,base); print("EE", np.round(T[:3,3],4))
          12 +for d in [(0,0,0.002),(0,0.003,0),(0,0.003,0.002),(0.003,0,0),(-0.003,0,0),(0,-0.003,0)]:
          13 +    qt,e=ap._ik_world(q, T[:3,3]+np.array(d), T[:3,:3], base)
          14 +    a=np.zeros(11,np.float32); a[3:10]=qt-q; o2,*_=env.step(a)
          15 +    moved = not np.allclose(ap._q(o2), q)
          16 +    print(d, "moved", moved)
          17 +    if moved:
          18 +        a[3:10]=q-qt; o2,*_=env.step(a)
```

</details>

<a id="C010"></a>
### C010 · timing in tests

Commit `308b0623268b5a12e87722dccd656d6e188534be`; parents: 2e2235a14f09be87db9d1e5afe9073add038773b. Recorded author date: 2026-09-30T22:10:14+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0741](01_timeline.md#E0741): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C010_308b062.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res_b.txt b/res_b.txt
new file mode 100644
index 0000000..f16138e
--- /dev/null
+++ b/res_b.txt
@@ -0,0 +1,81 @@
           1 +(100, 2, True, 58, 45.5)
           2 +(101, 0, True, 23, 21.0)
           3 +(102, 1, True, 37, 40.4)
           4 +(103, 1, True, 39, 37.4)
           5 +(104, 2, True, 62, 58.9)
           6 +(105, 0, True, 22, 19.9)
           7 +(106, 1, True, 23, 18.8)
           8 +(107, 0, True, 23, 18.0)
           9 +(108, 0, True, 27, 25.7)
          10 +(109, 1, True, 42, 39.8)
          11 +(110, 1, True, 55, 58.1)
          12 +(111, 1, True, 37, 28.0)
          13 +(112, 0, True, 26, 16.6)
          14 +(113, 0, True, 27, 28.5)
          15 +(114, 0, True, 20, 24.6)
          16 +(115, 1, True, 47, 46.9)
          17 +(116, 0, True, 20, 23.7)
          18 +(117, 0, True, 22, 24.0)
          19 +(118, 1, True, 45, 42.2)
          20 +(119, 1, True, 50, 44.2)
          21 +(120, 0, True, 23, 17.9)
          22 +(121, 0, True, 22, 14.2)
          23 +(122, 2, True, 70, 60.9)
          24 +(123, 0, True, 25, 19.8)
          25 +(124, 2, True, 40, 33.1)
          26 +(125, 1, True, 53, 40.0)
          27 +(126, 0, True, 26, 20.1)
          28 +(127, 1, True, 23, 22.1)
          29 +(128, 2, True, 69, 57.9)
          30 +(129, 1, True, 42, 25.4)
          31 +(130, 2, True, 56, 33.4)
          32 +(131, 1, True, 53, 40.0)
          33 +(132, 2, True, 53, 29.9)
          34 +(133, 1, True, 46, 25.8)
          35 +(134, 2, True, 66, 51.1)
          36 +(135, 1, True, 44, 32.4)
          37 +(136, 2, True, 47, 35.0)
          38 +(137, 1, True, 40, 28.3)
          39 +(138, 1, True, 47, 36.4)
          40 +(139, 1, True, 48, 36.6)
          41 +(140, 1, True, 45, 36.3)
          42 +(141, 1, True, 40, 24.7)
          43 +(142, 0, True, 28, 30.3)
          44 +(143, 2, True, 64, 57.5)
          45 +(144, 0, True, 27, 28.7)
          46 +(145, 1, True, 37, 28.4)
          47 +(146, 2, True, 38, 37.8)
          48 +(147, 0, True, 15, 13.5)
          49 +(148, 0, True, 24, 18.3)
          50 +(149, 0, True, 23, 16.3)
          51 +(150, 1, True, 31, 24.6)
          52 +(151, 2, True, 48, 46.0)
          53 +(152, 2, True, 54, 43.3)
          54 +(153, 2, True, 56, 53.4)
          55 +(154, 0, True, 20, 17.1)
          56 +(155, 0, True, 24, 21.4)
          57 +(156, 2, True, 67, 63.7)
          58 +(157, 0, True, 23, 17.1)
          59 +(158, 1, True, 41, 36.5)
          60 +(159, 2, True, 57, 48.5)
          61 +(160, 0, True, 31, 33.0)
          62 +(161, 2, True, 51, 48.6)
          63 +(162, 1, True, 46, 40.6)
          64 +(163, 1, True, 41, 33.1)
          65 +(164, 1, True, 43, 37.2)
          66 +(165, 1, True, 39, 27.9)
          67 +(166, 2, True, 75, 61.6)
          68 +(167, 2, True, 58, 43.6)
          69 +(168, 1, True, 39, 27.2)
          70 +(169, 2, True, 61, 42.1)
          71 +(170, 2, True, 61, 45.3)
          72 +(171, 2, True, 62, 49.4)
          73 +(172, 1, True, 43, 29.3)
          74 +(173, 2, True, 56, 40.4)
          75 +(174, 1, True, 53, 32.9)
          76 +(175, 2, True, 46, 25.9)
          77 +(176, 0, True, 28, 14.3)
          78 +(177, 2, True, 60, 20.2)
          79 +(178, 1, True, 45, 12.6)
          80 +(179, 2, True, 62, 13.8)
          81 +success 80 / 80 mean steps 42.0
diff --git a/res_oc6.txt b/res_oc6.txt
new file mode 100644
index 0000000..3472a3b
--- /dev/null
+++ b/res_oc6.txt
@@ -0,0 +1,41 @@
           1 +(0, 6, True, 108, 68.0, 0.59, 0.038)
           2 +(1, 6, True, 123, 87.8, 0.75, 0.047)
           3 +(2, 6, True, 86, 50.5, 0.94, 0.542)
           4 +(3, 6, True, 78, 36.0, 0.51, 0.051)
           5 +(4, 6, True, 139, 88.1, 0.81, 0.063)
           6 +(5, 6, True, 148, 112.0, 1.02, 0.072)
           7 +(6, 6, True, 123, 70.9, 0.74, 0.056)
           8 +(7, 6, True, 140, 90.2, 0.9, 0.056)
           9 +(8, 6, True, 127, 85.8, 0.79, 0.063)
          10 +(9, 6, True, 119, 69.7, 0.68, 0.047)
          11 +(10, 6, True, 98, 61.3, 0.51, 0.059)
          12 +(11, 6, True, 112, 71.1, 0.68, 0.065)
          13 +(12, 6, True, 156, 112.2, 0.98, 0.061)
          14 +(13, 6, True, 167, 119.4, 0.99, 0.113)
          15 +(14, 6, True, 71, 41.2, 0.47, 0.062)
          16 +(15, 6, True, 131, 85.6, 1.45, 0.456)
          17 +(16, 6, True, 81, 50.7, 0.55, 0.063)
          18 +(17, 6, True, 75, 44.5, 0.46, 0.072)
          19 +(18, 6, True, 100, 68.1, 0.67, 0.053)
          20 +(19, 6, True, 690, 238.8, 3.25, 0.072)
          21 +(20, 6, True, 97, 65.8, 0.7, 0.062)
          22 +(21, 6, True, 104, 71.4, 1.8, 1.127)
          23 +(22, 6, True, 96, 55.3, 0.71, 0.097)
          24 +(23, 6, True, 129, 88.7, 0.84, 0.063)
          25 +(24, 6, True, 106, 67.6, 0.72, 0.048)
          26 +(25, 6, True, 68, 39.5, 0.41, 0.039)
          27 +(26, 6, True, 83, 49.2, 0.53, 0.039)
          28 +(27, 6, True, 93, 62.5, 0.64, 0.061)
          29 +(28, 6, True, 128, 95.1, 0.88, 0.068)
          30 +(29, 6, True, 89, 58.1, 0.48, 0.032)
          31 +(30, 6, True, 70, 41.1, 0.32, 0.036)
          32 +(31, 6, True, 101, 60.4, 0.62, 0.062)
          33 +(32, 6, True, 87, 47.7, 0.45, 0.045)
          34 +(33, 6, True, 136, 72.1, 0.72, 0.047)
          35 +(34, 6, True, 99, 56.0, 0.62, 0.072)
          36 +(35, 6, True, 79, 46.3, 0.42, 0.037)
          37 +(36, 6, True, 101, 46.8, 0.5, 0.04)
          38 +(37, 6, True, 118, 40.9, 0.71, 0.063)
          39 +(38, 6, True, 261, 41.5, 1.21, 0.052)
          40 +(39, 6, True, 688, 46.7, 2.28, 0.063)
          41 +success 40 / 40 mean steps 140.125
diff --git a/test_approach.py b/test_approach.py
index 76f32da..3f00c83 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -7,15 +7,16 @@ def run(seed, verbose=False):
    7      7      obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
    8      8      ap = GeneratedApproach(env.action_space, env.observation_space, {})
    9      9      t = time.time(); ap.reset(obs, info)
   10        -    ret = 0; steps = 0; term = False
          10 +    ret = 0; steps = 0; term = False; tot_a = 0.0; max_a = 0.0
   11     11      for steps in range(1, env.max_steps + 1):
   12        -        a = ap.get_action(obs)
          12 +        t1 = time.time(); a = ap.get_action(obs); ta = time.time() - t1
          13 +        tot_a += ta; max_a = max(max_a, ta)
   13     14          obs, r, term, trunc, info = env.step(a)
   14     15          ret += r
   15     16          if term or trunc: break
   16     17      dt = time.time() - t
   17     18      env.close()
   18        -    return seed, info.get('object_count'), term, steps, round(dt, 1)
          19 +    return seed, info.get('object_count'), term, steps, round(dt, 1), round(tot_a, 2), round(max_a, 3)
   19     20  if __name__ == "__main__":
   20     21      from concurrent.futures import ThreadPoolExecutor
   21     22      seeds = list(range(int(sys.argv[1]), int(sys.argv[2])))
```

</details>

<a id="C011"></a>
### C011 · Escape moves in cycling directions on generic rejection (fixes endless lift loop)

Commit `d17592f5b1c9d652a9d321308638fe97e04f5220`; parents: 308b0623268b5a12e87722dccd656d6e188534be. Recorded author date: 2026-09-30T22:17:04+02:00.

File roles (automatic): policy, setup/other.

- [E0786](01_timeline.md#E0786): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_d17592f_approach.py) · [Exact all-file diff](evidence/diffs/C011_d17592f.diff)

[Previous saved controller snapshot](evidence/versions/C009_2e2235a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 744426d..ec67c6c 100644
--- a/approach.py
+++ b/approach.py
@@ -199,6 +199,7 @@ class GeneratedApproach:
  199    199          self.nsteps = 0
  200    200          self.scale = 1.0
  201    201          self.max_top = 0.15
         202 +        self.esc = 0
  202    203          # a nominal top-down configuration used as an extra IK seed
  203    204          b = self._base(state)
  204    205          qn, e = self._ik_world(self.q_home, [0.30, 0.0, 0.33], down_R(0.0), b, iters=200)
@@ -506,7 +507,7 @@ class GeneratedApproach:
  506    507          elif self.last_q is not None:
  507    508              self.scale = min(1.0, self.scale * 1.5)
  508    509          if rejected and self.cur is not None and self.cur[0] in ("move", "base"):
  509        -            if self.scale > 0.02 and self.cur[0] == "move":
         510 +            if self.scale > 0.02 and self.cur[0] == "move" and self.cur[3] != "escape":
  510    511                  pass            # retry the same segment with a smaller step
  511    512              else:
  512    513                  self._handle_reject(state)
@@ -600,6 +601,14 @@ class GeneratedApproach:
  600    601              self.segs = []
  601    602              self.cur = None
  602    603              return
  603        -        # generic: go up a bit, then replan
  604        -        self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.04]), None, "lift")]
         604 +        # generic: small escape displacement in a cycling direction, then replan
         605 +        dirs = [(0, 0, 1), (1, 0, 0.5), (-1, 0, 0.5), (0, 1, 0.5), (0, -1, 0.5),
         606 +                (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (1, 1, 1), (-1, -1, 1),
         607 +                (1, -1, 1), (-1, 1, 1)]
         608 +        d = np.array(dirs[self.esc % len(dirs)], dtype=float)
         609 +        self.esc += 1
         610 +        d /= np.linalg.norm(d)
         611 +        mag = 0.003 if tag != "escape" else 0.003 + 0.002 * (self.esc // len(dirs) % 3)
         612 +        self.segs = [("move", T[:3, 3] + d * mag, None, "escape")]
  605    613          self.cur = None
         614 +        self.scale = 0.3
diff --git a/d15.txt b/d15.txt
new file mode 100644
index 0000000..9d4a236
--- /dev/null
+++ b/d15.txt
@@ -0,0 +1,85 @@
           1 +obstruction0 {'x': 0.195, 'y': 0.004, 'z': 0.112, 'hx': 0.02, 'hy': 0.018, 'hz': 0.027, 'g': 0.0, 'yaw': 0.0}
           2 +obstruction1 {'x': 0.237, 'y': 0.317, 'z': 0.096, 'hx': 0.014, 'hy': 0.012, 'hz': 0.021, 'g': 0.0, 'yaw': 0.0}
           3 +obstruction2 {'x': 0.125, 'y': 0.027, 'z': 0.111, 'hx': 0.02, 'hy': 0.018, 'hz': 0.026, 'g': 0.0, 'yaw': 0.0}
           4 +obstruction3 {'x': 0.114, 'y': 0.077, 'z': 0.104, 'hx': 0.01, 'hy': 0.013, 'hz': 0.019, 'g': 0.0, 'yaw': 0.0}
           5 +obstruction4 {'x': 0.201, 'y': 0.047, 'z': 0.112, 'hx': 0.02, 'hy': 0.018, 'hz': 0.027, 'g': 0.0, 'yaw': 0.0}
           6 +obstruction5 {'x': 0.167, 'y': 0.085, 'z': 0.096, 'hx': 0.013, 'hy': 0.014, 'hz': 0.011, 'g': 0.0, 'yaw': 0.0}
           7 +obstruction6 {'x': 0.369, 'y': -0.248, 'z': 0.094, 'hx': 0.015, 'hy': 0.016, 'hz': 0.019, 'g': 0.0, 'yaw': 0.0}
           8 +obstruction7 {'x': 0.159, 'y': 0.031, 'z': 0.114, 'hx': 0.014, 'hy': 0.012, 'hz': 0.029, 'g': 0.0, 'yaw': 0.0}
           9 +target_block {'x': 0.373, 'y': -0.113, 'z': 0.1, 'hx': 0.033, 'hy': 0.036, 'hz': 0.025, 'g': 0.0, 'yaw': 0.0}
          10 +target_region {'x': 0.155, 'y': 0.051, 'z': 0.08, 'hx': 0.041, 'hy': 0.044, 'hz': 0.005, 'g': 0.0, 'yaw': 0.0}
          11 +0 ('move', (0.139, 0.001, 0.342), None, 'lift') ee [0.139 0.001 0.342] grasp 0.0 
          12 +1 ('base', (-0.17, 0.0, 0.0)) ee [0.089 0.001 0.342] grasp 0.0 
          13 +2 ('move', (0.114, 0.077, 0.33), 0.79, 'travel') ee [0.096 0.014 0.34 ] grasp 0.0 
          14 +8 ('move', (0.114, 0.077, 0.259), 0.79, 'grasp_descend', 'obstruction3') ee [0.118 0.075 0.291] grasp 0.0 
          15 +11 None ee [0.114 0.077 0.259] grasp 1.0 
          16 +12 ('move', (0.114, 0.077, 0.342), 0.79, 'lift') ee [0.114 0.077 0.289] grasp 1.0 
          17 +15 ('move', (0.16, 0.2, 0.342), 0.79, 'travel') ee [0.131 0.111 0.342] grasp 1.0 
          18 +19 ('move', (0.16, 0.2, 0.251), 0.79, 'place_descend') ee [0.164 0.199 0.284] grasp 1.0 
          19 +22 None ee [0.16  0.2   0.251] grasp 0.0 
          20 +23 ('move', (0.16, 0.2, 0.311), 0.79, 'retreat') ee [0.16  0.2   0.281] grasp 0.0 
          21 +25 ('move', (0.16, 0.2, 0.33), None, 'lift') ee [0.16 0.2  0.33] grasp 0.0 
          22 +26 ('move', (0.167, 0.085, 0.33), 0.0, 'travel') ee [0.166 0.156 0.33 ] grasp 0.0 
          23 +28 ('move', (0.167, 0.085, 0.257), 0.0, 'grasp_descend', 'obstruction5') ee [0.171 0.083 0.283] grasp 0.0 
          24 +30 None ee [0.167 0.085 0.257] grasp 1.0 
          25 +31 ('move', (0.167, 0.085, 0.34), 0.0, 'lift') ee [0.167 0.085 0.287] grasp 1.0 
          26 +34 ('move', (0.285, 0.175, 0.34), 0.0, 'travel') ee [0.213 0.118 0.341] grasp 1.0 
          27 +37 ('move', (0.285, 0.175, 0.249), 0.0, 'place_descend') ee [0.286 0.175 0.271] grasp 1.0 
          28 +39 None ee [0.285 0.175 0.249] grasp 0.0 
          29 +40 ('move', (0.285, 0.175, 0.309), 0.0, 'retreat') ee [0.285 0.175 0.279] grasp 0.0 
          30 +42 ('move', (0.285, 0.175, 0.33), None, 'lift') ee [0.285 0.175 0.33 ] grasp 0.0 
          31 +43 ('move', (0.125, 0.027, 0.33), 1.57, 'travel') ee [0.278 0.167 0.33 ] grasp 0.0 
          32 +54 ('move', (0.125, 0.027, 0.266), 1.57, 'grasp_descend', 'obstruction2') ee [0.127 0.03  0.308] grasp 0.0 
          33 +58 None ee [0.125 0.027 0.266] grasp 1.0 
          34 +59 ('move', (0.125, 0.027, 0.349), 1.57, 'lift') ee [0.125 0.027 0.266] grasp 1.0 REJ
          35 +60 ('move', (0.125, 0.027, 0.349), 1.57, 'lift') ee [0.125 0.027 0.266] grasp 1.0 REJ
          36 +62 ('move', (0.125, 0.027, 0.349), 1.57, 'lift') ee [0.125 0.027 0.268] grasp 1.0 REJ
          37 +65 ('move', (0.125, 0.027, 0.349), 1.57, 'lift') ee [0.125 0.027 0.27 ] grasp 1.0 REJ
          38 +67 ('move', (0.125, 0.027, 0.349), 1.57, 'lift') ee [0.125 0.027 0.271] grasp 1.0 REJ
          39 +70 ('move', (0.125, 0.027, 0.349), 1.57, 'lift') ee [0.125 0.027 0.273] grasp 1.0 REJ
          40 +74 ('move', (0.125, 0.027, 0.349), 1.57, 'lift') ee [0.125 0.027 0.275] grasp 1.0 REJ
          41 +76 ('move', (0.125, 0.027, 0.349), 1.57, 'lift') ee [0.125 0.027 0.276] grasp 1.0 REJ
          42 +77 ('move', (0.125, 0.027, 0.279), None, 'escape') ee [0.125 0.027 0.276] grasp 1.0 REJ
          43 +78 ('move', (0.128, 0.027, 0.277), None, 'escape') ee [0.125 0.027 0.276] grasp 1.0 REJ
          44 +79 ('move', (0.122, 0.027, 0.277), None, 'escape') ee [0.122 0.027 0.277] grasp 1.0 
          45 +80 ('move', (0.122, 0.027, 0.349), 1.57, 'lift') ee [0.123 0.027 0.284] grasp 1.0 
          46 +85 ('move', (0.335, 0.05, 0.349), 1.57, 'travel') ee [0.145 0.032 0.345] grasp 1.0 
          47 +91 ('move', (0.335, 0.05, 0.257), 1.57, 'place_descend') ee [0.335 0.05  0.27 ] grasp 1.0 
          48 +93 None ee [0.335 0.05  0.257] grasp 0.0 
          49 +94 ('move', (0.335, 0.05, 0.317), 1.57, 'retreat') ee [0.335 0.05  0.287] grasp 0.0 
          50 +96 ('move', (0.335, 0.05, 0.33), None, 'lift') ee [0.335 0.05  0.33 ] grasp 0.0 
          51 +97 ('move', (0.195, 0.004, 0.33), -3.14, 'travel') ee [0.322 0.048 0.326] grasp 0.0 
          52 +103 ('move', (0.195, 0.004, 0.267), -3.14, 'grasp_descend', 'obstruction0') ee [0.197 0.004 0.275] grasp 0.0 
          53 +105 None ee [0.195 0.004 0.267] grasp 1.0 
          54 +106 ('move', (0.195, 0.004, 0.35), -3.14, 'lift') ee [0.195 0.004 0.297] grasp 1.0 
          55 +109 ('move', (0.185, -0.225, 0.35), -3.14, 'travel') ee [ 0.193 -0.066  0.35 ] grasp 1.0 
          56 +113 ('move', (0.185, -0.225, 0.258), -3.14, 'place_descend') ee [ 0.185 -0.225  0.27 ] grasp 1.0 
          57 +115 None ee [ 0.185 -0.225  0.258] grasp 0.0 
          58 +116 ('move', (0.185, -0.225, 0.318), -3.14, 'retreat') ee [ 0.185 -0.225  0.288] grasp 0.0 
          59 +118 ('move', (0.185, -0.225, 0.33), None, 'lift') ee [ 0.185 -0.225  0.33 ] grasp 0.0 
          60 +119 ('move', (0.201, 0.047, 0.33), 1.57, 'travel') ee [ 0.186 -0.212  0.331] grasp 0.0 
          61 +129 ('move', (0.201, 0.047, 0.267), 1.57, 'grasp_descend', 'obstruction4') ee [0.203 0.045 0.293] grasp 0.0 
          62 +131 None ee [0.201 0.047 0.267] grasp 1.0 
          63 +132 ('move', (0.201, 0.047, 0.35), 1.57, 'lift') ee [0.201 0.047 0.297] grasp 1.0 
          64 +135 ('move', (0.41, 0.175, 0.35), 1.57, 'travel') ee [0.228 0.06  0.354] grasp 1.0 
          65 +140 ('move', (0.41, 0.175, 0.259), 1.57, 'place_descend') ee [0.41  0.175 0.27 ] grasp 1.0 
          66 +142 None ee [0.41  0.175 0.259] grasp 0.0 
          67 +143 ('move', (0.41, 0.175, 0.319), 1.57, 'retreat') ee [0.41  0.175 0.289] grasp 0.0 
          68 +145 ('move', (0.41, 0.175, 0.33), None, 'lift') ee [0.41  0.175 0.33 ] grasp 0.0 
          69 +146 ('move', (0.159, 0.031, 0.33), 0.0, 'travel') ee [0.399 0.171 0.329] grasp 0.0 
          70 +155 ('move', (0.159, 0.031, 0.269), 0.0, 'grasp_descend', 'obstruction7') ee [0.16  0.028 0.289] grasp 0.0 
          71 +157 None ee [0.159 0.031 0.269] grasp 1.0 
          72 +158 ('move', (0.159, 0.031, 0.34), 0.0, 'lift') ee [0.159 0.031 0.299] grasp 1.0 
          73 +161 ('move', (0.46, 0.05, 0.34), 0.0, 'travel') ee [0.21  0.033 0.341] grasp 1.0 
          74 +166 ('move', (0.46, 0.05, 0.26), 0.0, 'place_descend') ee [0.46 0.05 0.26] grasp 1.0 
          75 +167 None ee [0.46 0.05 0.26] grasp 0.0 
          76 +168 ('move', (0.46, 0.05, 0.32), 0.0, 'retreat') ee [0.46 0.05 0.29] grasp 0.0 
          77 +170 ('move', (0.46, 0.05, 0.33), None, 'lift') ee [0.46 0.05 0.33] grasp 0.0 
          78 +171 ('move', (0.373, -0.113, 0.33), 0.0, 'travel') ee [ 0.422 -0.021  0.33 ] grasp 0.0 
          79 +174 ('move', (0.373, -0.113, 0.255), 0.0, 'grasp_descend', 'target_block') ee [ 0.373 -0.113  0.255] grasp 0.0 
          80 +175 None ee [ 0.373 -0.113  0.255] grasp 1.0 
          81 +176 ('move', (0.373, -0.113, 0.339), -0.0, 'lift') ee [ 0.373 -0.113  0.285] grasp 1.0 
          82 +179 ('move', (0.155, 0.051, 0.339), -0.0, 'travel') ee [ 0.317 -0.07   0.34 ] grasp 1.0 
          83 +183 ('move', (0.155, 0.051, 0.265), -0.0, 'place_descend') ee [0.156 0.043 0.316] grasp 1.0 
          84 +187 None ee [0.155 0.051 0.266] grasp 0.0 
          85 +DONE 187
diff --git a/res_oc8.txt b/res_oc8.txt
new file mode 100644
index 0000000..4871f9e
--- /dev/null
+++ b/res_oc8.txt
@@ -0,0 +1,25 @@
           1 +(0, 8, True, 130, 64.2, 0.96, 0.105)
           2 +(1, 8, True, 147, 90.2, 1.04, 0.115)
           3 +(2, 8, True, 85, 59.1, 1.16, 0.502)
           4 +(3, 8, True, 83, 42.7, 0.63, 0.163)
           5 +(4, 8, True, 204, 115.0, 1.91, 0.555)
           6 +(5, 8, True, 149, 71.3, 1.2, 0.19)
           7 +(6, 8, True, 819, 265.1, 4.49, 0.17)
           8 +(7, 8, True, 151, 80.4, 1.11, 0.083)
           9 +(8, 8, True, 149, 88.0, 1.17, 0.14)
          10 +(9, 8, True, 127, 68.8, 0.79, 0.102)
          11 +(10, 8, True, 121, 73.6, 0.87, 0.107)
          12 +(11, 8, True, 113, 64.5, 0.68, 0.049)
          13 +(12, 8, True, 156, 90.0, 1.14, 0.054)
          14 +(13, 8, True, 403, 152.0, 2.57, 0.103)
          15 +(14, 8, True, 71, 40.8, 0.48, 0.068)
          16 +(15, 8, False, 1000, 124.1, 4.13, 0.867)
          17 +(16, 8, True, 87, 46.0, 0.56, 0.064)
          18 +(17, 8, True, 96, 47.6, 0.68, 0.049)
          19 +(18, 8, True, 168, 83.2, 1.17, 0.088)
          20 +(19, 8, True, 697, 102.9, 3.12, 0.068)
          21 +(20, 8, True, 103, 45.1, 0.75, 0.074)
          22 +(21, 8, True, 135, 56.9, 1.52, 0.78)
          23 +(22, 8, True, 96, 36.9, 0.59, 0.058)
          24 +(23, 8, True, 126, 21.9, 0.81, 0.082)
          25 +success 23 / 24 mean steps 225.66666666666666
```

</details>

<a id="C012"></a>
### C012 · Exact-on-line stepping with joint-cap shrink, bigger steps, lower safe height, drop spots near path

Commit `8e94aa7c7167f52814742c138e95640dbe717aa4`; parents: d17592f5b1c9d652a9d321308638fe97e04f5220. Recorded author date: 2026-09-30T23:03:01+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0989](01_timeline.md#E0989): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_8e94aa7_approach.py) · [Exact all-file diff](evidence/diffs/C012_8e94aa7.diff)

[Previous saved controller snapshot](evidence/versions/C011_d17592f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ec67c6c..9f38194 100644
--- a/approach.py
+++ b/approach.py
@@ -59,6 +59,15 @@ def down_R(yaw):
   59     59      return np.stack([x, y, z], axis=1)
   60     60  
   61     61  
          62 +def _expm(v):
          63 +    th = np.linalg.norm(v)
          64 +    if th < 1e-12:
          65 +        return np.eye(3)
          66 +    k = v / th
          67 +    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
          68 +    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * (K @ K)
          69 +
          70 +
   62     71  def _rotvec(Rm):
   63     72      cos = (np.trace(Rm) - 1) / 2
   64     73      cos = min(1.0, max(-1.0, cos))
@@ -109,6 +118,10 @@ def wrap(a):
  109    118  
  110    119  # ----------------------------------------------------------------------------- approach
  111    120  TABLE_TOP = 0.075
         121 +STEP_FAST = 0.12
         122 +STEP_LOW = 0.05
         123 +SAFE_FLOOR = 0.26
         124 +SAFE_CLR = 0.02
  112    125  MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
  113    126  TABLE_X = (0.10, 0.50)
  114    127  TABLE_Y = (-0.40, 0.40)
@@ -299,7 +312,7 @@ class GeneratedApproach:
  299    312              if b["g"] > 0.5 or n == exclude:
  300    313                  continue
  301    314              top = max(top, b["z"] + b["hz"])
  302        -        return max(0.33, top + 0.025 + held_below + FINGER)
         315 +        return max(SAFE_FLOOR, top + SAFE_CLR + held_below + FINGER)
  303    316  
  304    317      def _drop_spot(self, boxes, name, base, seeds, safe):
  305    318          reg = boxes["target_region"]
@@ -324,6 +337,9 @@ class GeneratedApproach:
  324    337                  for (px, py) in self.placed_spots:
  325    338                      clr = min(clr, max(abs(x - px), abs(y - py)) - 0.07)
  326    339                  dist = np.hypot(x - b["x"], y - b["y"])
         340 +                tb = boxes["target_block"]
         341 +                if name != "target_block":
         342 +                    dist += 0.7 * np.hypot(x - tb["x"], y - tb["y"])
  327    343                  cands.append((min(clr, 0.03) * 10 - dist, x, y))
  328    344          cands.sort(key=lambda c: -c[0])
  329    345          for sc, x, y in cands[:25]:
@@ -560,16 +576,29 @@ class GeneratedApproach:
  560    576                          continue
  561    577                      self._handle_reject(state)
  562    578                      continue
  563        -            step = 0.08
         579 +            step = STEP_FAST
  564    580              low = p[2] - FINGER < self.max_top + 0.03
  565    581              if low and seg[3] in ("lift", "grasp_descend", "place_descend", "retreat"):
  566        -                step = 0.03
         582 +                step = STEP_LOW
  567    583              step *= self.scale
  568        -            tgt = goal if nd < step else p + d * step / nd
  569        -            qt, err = self._ik_world(q, tgt, Rt, base)
  570        -            dq = qt - q
  571        -            m = np.max(np.abs(dq))
         584 +            rv = _rotvec(Rt @ Tw[:3, :3].T)
         585 +            f = 1.0
         586 +            if nd > 1e-9:
         587 +                f = min(f, step / nd)
         588 +            if rerr > 1e-9:
         589 +                f = min(f, max(0.5 * self.scale, 0.02) / rerr)
  572    590              lim = 0.2 * max(self.scale, 0.05)
         591 +            dq = None
         592 +            for _it in range(4):
         593 +                tgt = p + d * f
         594 +                Rs = _expm(rv * f) @ Tw[:3, :3]
         595 +                qt, err = self._ik_world(q, tgt, Rs, base)
         596 +                dq = qt - q
         597 +                m = np.max(np.abs(dq))
         598 +                if m <= lim:
         599 +                    break
         600 +                f *= lim / m * 0.97
         601 +            m = np.max(np.abs(dq))
  573    602              if m > lim:
  574    603                  dq *= lim / m
  575    604              if m < 1e-7:
diff --git a/probe_succ.py b/probe_succ.py
new file mode 100644
index 0000000..846feac
--- /dev/null
+++ b/probe_succ.py
@@ -0,0 +1,26 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seed=int(sys.argv[1]); DX=float(sys.argv[2]); DY=float(sys.argv[3]); DZ=float(sys.argv[4]) if len(sys.argv)>4 else 0.0
           5 +N=int(sys.argv[5]) if len(sys.argv)>5 else 600
           6 +class P(GeneratedApproach):
           7 +    def _plan_place(self, state, boxes, name, place_xy, bottom):
           8 +        if name=="target_block":
           9 +            place_xy=(place_xy[0]+DX, place_xy[1]+DY); bottom=bottom+DZ
          10 +        return super()._plan_place(state, boxes, name, place_xy, bottom)
          11 +    def _blocking(self, boxes): return []
          12 +env=make_env(); obs,info=env.reset(seed=seed, options={"object_count":0})
          13 +ap=P(env.action_space, env.observation_space, {}); ap.reset(obs,info)
          14 +b=ap._boxes(obs); r_=b["target_region"]; t_=b["target_block"]
          15 +print("reg", {k:round(v,6) for k,v in r_.items()}); print("blk", {k:round(v,6) for k,v in t_.items()})
          16 +rob=ap._robot(obs); opened=None; res="NOTERM"
          17 +for t in range(N):
          18 +    a=ap.get_action(obs); g0=obs.get(rob,"grasp_active")
          19 +    obs,r,term,trunc,info=env.step(a)
          20 +    b=ap._boxes(obs); bb=b["target_block"]; g=obs.get(rob,"grasp_active")
          21 +    if g0>0.5 and g<0.5 and opened is None and bb["z"]<0.3: opened=t
          22 +    if term or (opened is not None and t-opened>=1):
          23 +        res="TERM" if term else "NOTERM"
          24 +        print(res, "t",t,"opened",opened,"grasp",g,"blkg",bb["g"],"off", round(bb["x"]-r_["x"],6), round(bb["y"]-r_["y"],6),
          25 +              "bottom-regtop", round(bb["z"]-bb["hz"]-(r_["z"]+r_["hz"]),4), "yaw", round(bb["yaw"],3),"r",r); break
          26 +else: print("timeout", "opened", opened)
diff --git a/res_a.txt b/res_a.txt
index 37c6321..173f8bb 100644
--- a/res_a.txt
+++ b/res_a.txt
@@ -1,101 +1,121 @@
    1        -(0, 2, True, 54, 32.9)
    2        -(1, 1, True, 47, 24.6)
    3        -(2, 2, True, 61, 44.9)
    4        -(3, 2, True, 43, 27.8)
    5        -(4, 2, True, 57, 36.6)
    6        -(5, 2, True, 59, 45.6)
    7        -(6, 1, True, 41, 18.3)
    8        -(7, 2, True, 52, 29.3)
    9        -(8, 2, True, 53, 47.4)
   10        -(9, 1, True, 34, 26.4)
   11        -(10, 2, True, 38, 33.4)
   12        -(11, 0, True, 24, 19.0)
   13        -(12, 1, True, 44, 37.8)
   14        -(13, 2, True, 58, 46.7)
   15        -(14, 0, True, 17, 11.9)
   16        -(15, 2, True, 39, 25.8)
   17        -(16, 1, True, 33, 21.8)
   18        -(17, 2, True, 57, 46.0)
   19        -(18, 2, True, 40, 30.9)
   20        -(19, 1, True, 43, 32.6)
   21        -(20, 2, True, 62, 54.0)
   22        -(21, 0, True, 32, 26.1)
   23        -(22, 2, True, 38, 32.4)
   24        -(23, 0, True, 30, 29.4)
   25        -(24, 1, True, 27, 27.1)
   26        -(25, 1, True, 49, 44.7)
   27        -(26, 2, True, 42, 45.8)
   28        -(27, 0, True, 37, 29.1)
   29        -(28, 1, True, 54, 50.8)
   30        -(29, 2, True, 23, 19.9)
   31        -(30, 0, True, 31, 27.2)
   32        -(31, 1, True, 56, 55.3)
   33        -(32, 2, True, 50, 48.5)
   34        -(33, 2, True, 52, 57.6)
   35        -(34, 0, True, 22, 19.2)
   36        -(35, 0, True, 25, 21.4)
   37        -(36, 1, True, 35, 25.7)
   38        -(37, 0, True, 25, 19.2)
   39        -(38, 0, True, 23, 24.5)
   40        -(39, 2, True, 60, 65.9)
   41        -(40, 1, True, 90, 56.5)
   42        -(41, 1, True, 33, 28.7)
   43        -(42, 0, True, 23, 16.3)
   44        -(43, 1, True, 38, 22.5)
   45        -(44, 2, True, 39, 34.7)
   46        -(45, 2, True, 49, 39.4)
   47        -(46, 1, True, 31, 21.6)
   48        -(47, 0, True, 17, 12.1)
   49        -(48, 0, True, 19, 16.4)
   50        -(49, 0, True, 21, 25.0)
   51        -(50, 2, True, 58, 51.8)
   52        -(51, 1, True, 34, 27.6)
   53        -(52, 2, True, 60, 59.1)
   54        -(53, 2, True, 56, 47.3)
   55        -(54, 0, True, 22, 20.2)
   56        -(55, 2, True, 60, 59.1)
   57        -(56, 1, True, 36, 25.0)
   58        -(57, 0, True, 21, 13.2)
   59        -(58, 1, True, 34, 35.6)
   60        -(59, 2, True, 72, 65.3)
   61        -(60, 0, True, 20, 18.4)
   62        -(61, 1, True, 42, 33.8)
   63        -(62, 1, True, 37, 29.2)
   64        -(63, 1, True, 40, 32.7)
   65        -(64, 1, True, 38, 28.3)
   66        -(65, 0, True, 35, 30.5)
   67        -(66, 2, True, 50, 42.8)
   68        -(67, 2, True, 53, 49.6)
   69        -(68, 1, True, 22, 22.1)
   70        -(69, 0, True, 21, 14.6)
   71        -(70, 1, True, 47, 41.5)
   72        -(71, 2, True, 64, 54.1)
   73        -(72, 2, True, 62, 56.2)
   74        -(73, 2, True, 44, 36.5)
   75        -(74, 0, True, 18, 12.6)
   76        -(75, 1, True, 30, 18.6)
   77        -(76, 1, True, 52, 43.4)
   78        -(77, 0, True, 25, 16.3)
   79        -(78, 2, True, 38, 31.4)
   80        -(79, 0, True, 17, 11.9)
   81        -(80, 2, True, 51, 37.0)
   82        -(81, 0, True, 27, 21.5)
   83        -(82, 2, True, 56, 42.4)
   84        -(83, 2, True, 38, 29.5)
   85        -(84, 1, True, 36, 24.9)
   86        -(85, 2, True, 48, 36.8)
   87        -(86, 2, True, 51, 40.0)
   88        -(87, 1, True, 46, 39.6)
   89        -(88, 1, True, 41, 26.8)
   90        -(89, 2, True, 52, 54.3)
   91        -(90, 1, True, 34, 27.0)
   92        -(91, 2, True, 42, 37.7)
   93        -(92, 1, True, 37, 35.0)
   94        -(93, 2, True, 55, 39.2)
   95        -(94, 0, True, 25, 23.4)
   96        -(95, 1, True, 43, 27.1)
   97        -(96, 2, True, 60, 29.8)
   98        -(97, 0, True, 28, 18.0)
   99        -(98, 1, True, 49, 13.1)
  100        -(99, 2, True, 48, 9.4)
  101        -success 100 / 100 mean steps 41.02
           1 +(0, 2, True, 59, 41.5, 0.22, 0.031)
           2 +(1, 1, True, 50, 28.8, 0.21, 0.035)
           3 +(2, 2, True, 67, 49.1, 0.29, 0.034)
           4 +(3, 2, True, 46, 32.5, 0.23, 0.042)
           5 +(4, 2, True, 62, 43.2, 0.23, 0.024)
           6 +(5, 2, True, 64, 42.9, 0.27, 0.018)
           7 +(6, 1, True, 45, 18.8, 0.17, 0.026)
           8 +(7, 2, True, 55, 35.8, 0.22, 0.022)
           9 +(8, 2, True, 60, 49.4, 0.26, 0.033)
          10 +(9, 1, True, 38, 26.6, 0.15, 0.034)
          11 +(10, 2, True, 40, 34.0, 0.14, 0.015)
          12 +(11, 0, True, 25, 22.3, 0.08, 0.008)
          13 +(12, 1, True, 48, 42.1, 0.24, 0.049)
          14 +(13, 2, True, 72, 60.6, 0.36, 0.041)
          15 +(14, 0, True, 18, 12.0, 0.06, 0.012)
          16 +(15, 2, True, 41, 27.8, 0.24, 0.031)
          17 +(16, 1, True, 36, 28.1, 0.15, 0.022)
          18 +(17, 2, True, 62, 50.7, 0.32, 0.059)
          19 +(18, 2, True, 43, 31.4, 0.24, 0.038)
          20 +(19, 1, True, 45, 34.7, 0.22, 0.041)
          21 +(20, 2, True, 65, 62.7, 0.34, 0.053)
          22 +(21, 0, True, 33, 33.2, 0.16, 0.026)
          23 +(22, 2, True, 42, 39.3, 0.14, 0.02)
          24 +(23, 0, True, 30, 33.2, 0.13, 0.018)
          25 +(24, 1, True, 29, 32.4, 0.16, 0.041)
          26 +(25, 1, True, 53, 46.6, 0.2, 0.021)
          27 +(26, 2, True, 45, 34.8, 0.16, 0.015)
          28 +(27, 0, True, 37, 31.7, 0.16, 0.013)
          29 +(28, 1, True, 57, 49.3, 0.22, 0.018)
          30 +(29, 2, True, 24, 20.6, 0.08, 0.022)
          31 +(30, 0, True, 31, 24.9, 0.11, 0.015)
          32 +(31, 1, True, 58, 55.0, 0.26, 0.023)
          33 +(32, 2, True, 54, 47.9, 0.24, 0.029)
          34 +(33, 2, True, 57, 57.3, 0.22, 0.014)
          35 +(34, 0, True, 24, 20.3, 0.12, 0.047)
          36 +(35, 0, True, 26, 23.1, 0.11, 0.018)
          37 +(36, 1, True, 37, 33.8, 0.17, 0.027)
          38 +(37, 0, True, 27, 19.0, 0.13, 0.029)
          39 +(38, 0, True, 24, 25.5, 0.09, 0.016)
          40 +(39, 2, True, 65, 57.8, 0.39, 0.044)
          41 +(40, 1, True, 90, 63.6, 2.6, 0.17)
          42 +(41, 1, True, 37, 32.6, 0.22, 0.027)
          43 +(42, 0, True, 24, 20.1, 0.13, 0.027)
          44 +(43, 1, True, 40, 30.8, 0.19, 0.026)
          45 +(44, 2, True, 44, 42.5, 0.27, 0.025)
          46 +(45, 2, True, 54, 51.9, 0.35, 0.027)
          47 +(46, 1, True, 35, 23.1, 0.17, 0.024)
          48 +(47, 0, True, 19, 19.8, 0.09, 0.013)
          49 +(48, 0, True, 20, 25.6, 0.1, 0.014)
          50 +(49, 0, True, 23, 28.4, 0.1, 0.01)
          51 +(50, 2, True, 64, 64.8, 0.38, 0.062)
          52 +(51, 1, True, 36, 36.4, 0.16, 0.017)
          53 +(52, 2, True, 64, 65.0, 0.9, 0.546)
          54 +(53, 2, True, 63, 54.5, 0.38, 0.042)
          55 +(54, 0, True, 23, 19.5, 0.11, 0.016)
          56 +(55, 2, True, 66, 65.0, 0.31, 0.036)
          57 +(56, 1, True, 39, 27.9, 0.18, 0.014)
          58 +(57, 0, True, 22, 12.2, 0.11, 0.028)
          59 +(58, 1, True, 35, 38.4, 0.2, 0.042)
          60 +(59, 2, True, 76, 68.0, 0.41, 0.065)
          61 +(60, 0, True, 22, 12.2, 0.07, 0.011)
          62 +(61, 1, True, 46, 33.6, 0.18, 0.022)
          63 +(62, 1, True, 40, 36.2, 0.21, 0.048)
          64 +(63, 1, True, 44, 34.3, 0.25, 0.111)
          65 +(64, 1, True, 40, 24.5, 0.22, 0.063)
          66 +(65, 0, True, 37, 30.8, 0.19, 0.048)
          67 +(66, 2, True, 53, 36.2, 0.27, 0.043)
          68 +(67, 2, True, 57, 46.0, 0.28, 0.05)
          69 +(68, 1, True, 22, 21.0, 0.1, 0.041)
          70 +(69, 0, True, 22, 17.8, 0.08, 0.009)
          71 +(70, 1, True, 50, 42.7, 0.21, 0.03)
          72 +(71, 2, True, 69, 61.5, 0.35, 0.039)
          73 +(72, 2, True, 69, 54.9, 0.37, 0.048)
          74 +(73, 2, True, 52, 39.3, 0.23, 0.017)
          75 +(74, 0, True, 18, 17.0, 0.08, 0.017)
          76 +(75, 1, True, 35, 18.5, 0.16, 0.016)
          77 +(76, 1, True, 55, 48.0, 0.33, 0.045)
          78 +(77, 0, True, 27, 21.9, 0.15, 0.025)
          79 +(78, 2, True, 40, 38.2, 0.24, 0.043)
          80 +(79, 0, True, 18, 16.7, 0.13, 0.049)
          81 +(80, 2, True, 56, 49.5, 0.31, 0.033)
          82 +(81, 0, True, 27, 29.8, 0.13, 0.013)
          83 +(82, 2, True, 61, 53.5, 0.38, 0.038)
          84 +(83, 2, True, 42, 41.2, 0.26, 0.051)
          85 +(84, 1, True, 40, 30.0, 0.22, 0.026)
          86 +(85, 2, True, 54, 39.9, 0.43, 0.133)
          87 +(86, 2, True, 56, 45.9, 0.31, 0.033)
          88 +(87, 1, True, 49, 41.7, 0.26, 0.033)
          89 +(88, 1, True, 43, 31.3, 0.21, 0.035)
          90 +(89, 2, True, 56, 49.1, 0.82, 0.593)
          91 +(90, 1, True, 37, 28.2, 0.18, 0.033)
          92 +(91, 2, True, 44, 34.9, 0.17, 0.021)
          93 +(92, 1, True, 41, 32.0, 0.19, 0.039)
          94 +(93, 2, True, 63, 53.2, 0.27, 0.019)
          95 +(94, 0, True, 26, 20.0, 0.13, 0.02)
          96 +(95, 1, True, 46, 30.0, 0.17, 0.021)
          97 +(96, 2, True, 63, 50.8, 0.27, 0.021)
          98 +(97, 0, True, 29, 22.1, 0.15, 0.015)
          99 +(98, 1, True, 52, 58.0, 0.23, 0.024)
         100 +(99, 2, True, 53, 48.2, 0.24, 0.04)
         101 +(100, 2, True, 58, 59.3, 0.2, 0.025)
         102 +(101, 0, True, 23, 17.2, 0.09, 0.018)
         103 +(102, 1, True, 37, 24.2, 0.15, 0.024)
         104 +(103, 1, True, 39, 33.7, 0.16, 0.032)
         105 +(104, 2, True, 62, 63.6, 0.31, 0.043)
         106 +(105, 0, True, 22, 11.4, 0.08, 0.014)
         107 +(106, 1, True, 23, 31.9, 0.1, 0.014)
         108 +(107, 0, True, 23, 26.3, 0.1, 0.022)
         109 +(108, 0, True, 27, 29.8, 0.15, 0.033)
         110 +(109, 1, True, 42, 48.3, 0.26, 0.057)
         111 +(110, 1, True, 55, 53.1, 0.29, 0.07)
         112 +(111, 1, True, 37, 41.3, 0.25, 0.08)
         113 +(112, 0, True, 26, 24.3, 0.15, 0.041)
         114 +(113, 0, True, 27, 30.0, 0.14, 0.022)
         115 +(114, 0, True, 20, 18.9, 0.13, 0.064)
         116 +(115, 1, True, 47, 27.6, 0.19, 0.019)
         117 +(116, 0, True, 20, 17.4, 0.09, 0.018)
         118 +(117, 0, True, 22, 13.5, 0.1, 0.024)
         119 +(118, 1, True, 45, 11.6, 0.17, 0.026)
         120 +(119, 1, True, 50, 7.5, 0.15, 0.016)
         121 +success 120 / 120 mean steps 42.725
diff --git a/res_oc3.txt b/res_oc3.txt
new file mode 100644
index 0000000..9c97674
--- /dev/null
+++ b/res_oc3.txt
@@ -0,0 +1,33 @@
           1 +(200, 3, True, 84, 69.4, 0.46, 0.083)
           2 +(201, 3, True, 64, 41.8, 0.27, 0.024)
           3 +(202, 3, True, 60, 30.3, 0.34, 0.09)
           4 +(203, 3, True, 81, 55.1, 0.46, 0.052)
           5 +(204, 3, True, 79, 53.2, 0.43, 0.065)
           6 +(205, 3, True, 84, 57.1, 0.39, 0.038)
           7 +(206, 3, True, 54, 34.4, 0.34, 0.048)
           8 +(207, 3, True, 60, 35.2, 0.32, 0.044)
           9 +(208, 3, True, 60, 44.3, 0.29, 0.03)
          10 +(209, 3, True, 77, 70.9, 0.37, 0.046)
          11 +(210, 3, True, 66, 47.8, 0.34, 0.042)
          12 +(211, 3, True, 55, 34.5, 0.23, 0.038)
          13 +(212, 3, True, 59, 47.5, 0.33, 0.036)
          14 +(213, 3, True, 58, 38.5, 0.27, 0.036)
          15 +(214, 3, True, 52, 31.2, 0.26, 0.05)
          16 +(215, 3, True, 72, 49.5, 0.34, 0.03)
          17 +(216, 3, True, 57, 38.6, 0.24, 0.03)
          18 +(217, 3, True, 88, 63.1, 0.44, 0.041)
          19 +(218, 3, True, 70, 47.7, 0.35, 0.047)
          20 +(219, 3, True, 82, 56.4, 0.36, 0.056)
          21 +(220, 3, True, 86, 60.3, 0.35, 0.023)
          22 +(221, 3, True, 73, 40.7, 0.3, 0.026)
          23 +(222, 3, True, 53, 24.0, 0.25, 0.029)
          24 +(223, 3, True, 67, 46.5, 0.31, 0.026)
          25 +(224, 3, True, 78, 45.0, 0.39, 0.045)
          26 +(225, 3, True, 83, 48.8, 0.39, 0.05)
          27 +(226, 3, True, 78, 41.3, 0.39, 0.048)
          28 +(227, 3, True, 74, 34.2, 0.34, 0.038)
          29 +(228, 3, True, 55, 28.5, 0.19, 0.021)
          30 +(229, 3, True, 89, 28.8, 0.42, 0.035)
          31 +(230, 3, True, 57, 20.7, 0.23, 0.017)
          32 +(231, 3, True, 91, 17.3, 0.39, 0.04)
          33 +success 32 / 32 mean steps 70.1875
diff --git a/res_oc5.txt b/res_oc5.txt
new file mode 100644
index 0000000..290c697
--- /dev/null
+++ b/res_oc5.txt
@@ -0,0 +1,33 @@
           1 +(200, 5, True, 111, 85.4, 0.64, 0.059)
           2 +(201, 5, True, 100, 58.2, 0.67, 0.084)
           3 +(202, 5, True, 82, 54.8, 0.59, 0.073)
           4 +(203, 5, True, 100, 54.0, 0.6, 0.069)
           5 +(204, 5, True, 124, 79.8, 0.68, 0.049)
           6 +(205, 5, True, 135, 82.5, 0.78, 0.081)
           7 +(206, 5, True, 60, 28.2, 0.33, 0.031)
           8 +(207, 5, True, 63, 41.9, 0.34, 0.024)
           9 +(208, 5, True, 90, 59.5, 0.48, 0.043)
          10 +(209, 5, True, 124, 78.2, 0.62, 0.051)
          11 +(210, 5, True, 97, 54.0, 0.51, 0.039)
          12 +(211, 5, True, 82, 51.9, 0.47, 0.054)
          13 +(212, 5, True, 109, 62.2, 0.55, 0.038)
          14 +(213, 5, True, 102, 60.2, 0.53, 0.049)
          15 +(214, 5, True, 97, 56.3, 0.55, 0.056)
          16 +(215, 5, True, 117, 68.8, 0.63, 0.062)
          17 +(216, 5, True, 98, 54.7, 0.59, 0.077)
          18 +(217, 5, True, 104, 60.6, 0.51, 0.049)
          19 +(218, 5, True, 109, 61.3, 0.59, 0.045)
          20 +(219, 5, True, 126, 72.2, 0.69, 0.068)
          21 +(220, 5, True, 534, 121.8, 2.18, 0.076)
          22 +(221, 5, True, 91, 53.3, 0.47, 0.054)
          23 +(222, 5, True, 70, 34.9, 0.31, 0.03)
          24 +(223, 5, True, 113, 72.9, 0.6, 0.046)
          25 +(224, 5, True, 100, 58.8, 0.47, 0.036)
          26 +(225, 5, True, 104, 64.9, 0.49, 0.027)
          27 +(226, 5, True, 102, 56.6, 0.58, 0.073)
          28 +(227, 5, True, 100, 54.7, 0.5, 0.042)
          29 +(228, 5, True, 77, 42.5, 0.39, 0.069)
          30 +(229, 5, True, 105, 44.1, 0.53, 0.05)
          31 +(230, 5, True, 85, 20.5, 0.37, 0.026)
          32 +(231, 5, True, 97, 15.8, 0.43, 0.04)
          33 +success 32 / 32 mean steps 112.75
diff --git a/res_oc8.txt b/res_oc8.txt
index 4871f9e..79634c5 100644
--- a/res_oc8.txt
+++ b/res_oc8.txt
@@ -1,25 +1,41 @@
    1        -(0, 8, True, 130, 64.2, 0.96, 0.105)
    2        -(1, 8, True, 147, 90.2, 1.04, 0.115)
    3        -(2, 8, True, 85, 59.1, 1.16, 0.502)
    4        -(3, 8, True, 83, 42.7, 0.63, 0.163)
    5        -(4, 8, True, 204, 115.0, 1.91, 0.555)
    6        -(5, 8, True, 149, 71.3, 1.2, 0.19)
    7        -(6, 8, True, 819, 265.1, 4.49, 0.17)
    8        -(7, 8, True, 151, 80.4, 1.11, 0.083)
    9        -(8, 8, True, 149, 88.0, 1.17, 0.14)
   10        -(9, 8, True, 127, 68.8, 0.79, 0.102)
   11        -(10, 8, True, 121, 73.6, 0.87, 0.107)
   12        -(11, 8, True, 113, 64.5, 0.68, 0.049)
   13        -(12, 8, True, 156, 90.0, 1.14, 0.054)
   14        -(13, 8, True, 403, 152.0, 2.57, 0.103)
   15        -(14, 8, True, 71, 40.8, 0.48, 0.068)
   16        -(15, 8, False, 1000, 124.1, 4.13, 0.867)
   17        -(16, 8, True, 87, 46.0, 0.56, 0.064)
   18        -(17, 8, True, 96, 47.6, 0.68, 0.049)
   19        -(18, 8, True, 168, 83.2, 1.17, 0.088)
   20        -(19, 8, True, 697, 102.9, 3.12, 0.068)
   21        -(20, 8, True, 103, 45.1, 0.75, 0.074)
   22        -(21, 8, True, 135, 56.9, 1.52, 0.78)
   23        -(22, 8, True, 96, 36.9, 0.59, 0.058)
   24        -(23, 8, True, 126, 21.9, 0.81, 0.082)
   25        -success 23 / 24 mean steps 225.66666666666666
           1 +(0, 8, True, 130, 92.9, 0.77, 0.068)
           2 +(1, 8, True, 147, 101.7, 1.16, 0.074)
           3 +(2, 8, True, 85, 53.8, 1.04, 0.549)
           4 +(3, 8, True, 83, 44.8, 0.51, 0.06)
           5 +(4, 8, True, 204, 127.9, 1.82, 0.571)
           6 +(5, 8, True, 149, 77.9, 1.26, 0.126)
           7 +(6, 8, True, 819, 289.7, 4.86, 0.147)
           8 +(7, 8, True, 151, 88.7, 0.99, 0.059)
           9 +(8, 8, True, 149, 88.6, 1.04, 0.086)
          10 +(9, 8, True, 127, 72.0, 0.85, 0.063)
          11 +(10, 8, True, 121, 77.4, 0.69, 0.042)
          12 +(11, 8, True, 113, 65.7, 0.76, 0.06)
          13 +(12, 8, True, 156, 92.4, 1.03, 0.083)
          14 +(13, 8, True, 403, 182.7, 2.73, 0.113)
          15 +(14, 8, True, 71, 41.3, 0.39, 0.038)
          16 +(15, 8, True, 188, 102.5, 1.97, 0.507)
          17 +(16, 8, True, 87, 49.7, 0.63, 0.061)
          18 +(17, 8, True, 96, 52.0, 0.93, 0.076)
          19 +(18, 8, True, 168, 95.0, 1.31, 0.114)
          20 +(19, 8, True, 697, 262.9, 3.66, 0.095)
          21 +(20, 8, True, 103, 51.0, 0.77, 0.111)
          22 +(21, 8, True, 135, 76.6, 1.47, 0.533)
          23 +(22, 8, True, 96, 51.0, 0.63, 0.07)
          24 +(23, 8, True, 126, 81.4, 0.77, 0.086)
          25 +(24, 8, True, 114, 74.7, 0.69, 0.099)
          26 +(25, 8, True, 88, 50.6, 0.54, 0.071)
          27 +(26, 8, True, 87, 52.2, 0.51, 0.09)
          28 +(27, 8, True, 93, 60.3, 0.63, 0.068)
          29 +(28, 8, True, 145, 86.9, 0.83, 0.058)
          30 +(29, 8, True, 92, 53.0, 0.51, 0.062)
          31 +(30, 8, True, 86, 50.1, 0.49, 0.051)
          32 +(31, 8, True, 103, 61.9, 0.68, 0.078)
          33 +(32, 8, True, 116, 64.2, 0.66, 0.055)
          34 +(33, 8, True, 126, 68.0, 0.82, 0.062)
          35 +(34, 8, True, 101, 56.5, 0.54, 0.042)
          36 +(35, 8, True, 111, 54.3, 0.6, 0.063)
          37 +(36, 8, True, 115, 47.7, 0.64, 0.05)
          38 +(37, 8, True, 121, 41.4, 0.77, 0.072)
          39 +(38, 8, True, 265, 43.8, 1.39, 0.05)
          40 +(39, 8, True, 542, 44.3, 2.78, 0.076)
          41 +success 40 / 40 mean steps 172.725
diff --git a/res_t.txt b/res_t.txt
new file mode 100644
index 0000000..f398c79
--- /dev/null
+++ b/res_t.txt
@@ -0,0 +1,41 @@
           1 +(0, 2, True, 43, 31.6, 0.3, 0.078)
           2 +(1, 1, True, 45, 34.5, 0.3, 0.055)
           3 +(2, 2, True, 63, 61.2, 0.44, 0.068)
           4 +(3, 2, True, 40, 27.5, 0.22, 0.029)
           5 +(4, 2, True, 49, 42.5, 0.31, 0.049)
           6 +(5, 2, True, 65, 56.2, 0.4, 0.053)
           7 +(6, 1, True, 38, 25.2, 0.27, 0.073)
           8 +(7, 2, True, 50, 40.6, 0.29, 0.051)
           9 +(8, 2, True, 50, 53.1, 0.22, 0.02)
          10 +(9, 1, True, 28, 26.3, 0.11, 0.018)
          11 +(10, 2, True, 35, 37.3, 0.17, 0.043)
          12 +(11, 0, True, 22, 23.2, 0.1, 0.016)
          13 +(12, 1, True, 45, 44.1, 0.25, 0.024)
          14 +(13, 2, True, 58, 59.7, 0.37, 0.029)
          15 +(14, 0, True, 13, 12.9, 0.05, 0.01)
          16 +(15, 2, True, 37, 40.7, 0.21, 0.025)
          17 +(16, 1, True, 32, 22.7, 0.16, 0.019)
          18 +(17, 2, True, 51, 54.3, 0.36, 0.029)
          19 +(18, 2, True, 34, 32.8, 0.18, 0.025)
          20 +(19, 1, True, 42, 40.8, 0.39, 0.037)
          21 +(20, 2, True, 59, 66.2, 0.34, 0.026)
          22 +(21, 0, True, 30, 33.8, 0.2, 0.023)
          23 +(22, 2, True, 35, 37.9, 0.21, 0.026)
          24 +(23, 0, True, 29, 33.6, 0.19, 0.02)
          25 +(24, 1, True, 25, 24.1, 0.16, 0.023)
          26 +(25, 1, True, 49, 48.6, 0.24, 0.018)
          27 +(26, 2, True, 37, 33.4, 0.19, 0.026)
          28 +(27, 0, True, 37, 34.6, 0.23, 0.028)
          29 +(28, 1, True, 62, 58.0, 0.44, 0.04)
          30 +(29, 2, True, 22, 20.0, 0.11, 0.029)
          31 +(30, 0, True, 30, 26.2, 0.16, 0.027)
          32 +(31, 1, True, 51, 41.7, 0.32, 0.075)
          33 +(32, 2, True, 46, 37.0, 0.22, 0.02)
          34 +(33, 2, True, 47, 34.8, 0.28, 0.04)
          35 +(34, 0, True, 18, 15.4, 0.14, 0.07)
          36 +(35, 0, True, 20, 17.8, 0.16, 0.059)
          37 +(36, 1, True, 29, 18.2, 0.17, 0.028)
          38 +(37, 0, True, 23, 10.8, 0.17, 0.064)
          39 +(38, 0, True, 20, 8.1, 0.1, 0.014)
          40 +(39, 2, True, 52, 8.3, 0.28, 0.023)
          41 +success 40 / 40 mean steps 39.025
```

</details>

<a id="C013"></a>
### C013 · Corridor-based safe height, drop retreat segment

Commit `2c03cfcd71cd7b6a08433de725a1b999a9edf022`; parents: 8e94aa7c7167f52814742c138e95640dbe717aa4. Recorded author date: 2026-09-30T23:07:17+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E1042](01_timeline.md#E1042): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_2c03cfc_approach.py) · [Exact all-file diff](evidence/diffs/C013_2c03cfc.diff)

[Previous saved controller snapshot](evidence/versions/C012_8e94aa7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9f38194..a72711c 100644
--- a/approach.py
+++ b/approach.py
@@ -120,7 +120,7 @@ def wrap(a):
  120    120  TABLE_TOP = 0.075
  121    121  STEP_FAST = 0.12
  122    122  STEP_LOW = 0.05
  123        -SAFE_FLOOR = 0.26
         123 +SAFE_FLOOR = 0.2
  124    124  SAFE_CLR = 0.02
  125    125  MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
  126    126  TABLE_X = (0.10, 0.50)
@@ -306,11 +306,20 @@ class GeneratedApproach:
  306    306          cands.sort(key=lambda c: -c[0])
  307    307          return cands
  308    308  
  309        -    def _safe_z(self, boxes, exclude=None, held_below=0.0):
         309 +    def _safe_z(self, boxes, exclude=None, held_below=0.0, path=None, rad=0.08):
  310    310          top = TABLE_TOP + 0.03
  311    311          for n, b in boxes.items():
  312    312              if b["g"] > 0.5 or n == exclude:
  313    313                  continue
         314 +            if path is not None:
         315 +                a = np.asarray(path[0][:2], float)
         316 +                c = np.asarray(path[1][:2], float)
         317 +                o = np.array([b["x"], b["y"]])
         318 +                ab = c - a
         319 +                t = 0.0 if ab @ ab < 1e-12 else min(1.0, max(0.0, (o - a) @ ab / (ab @ ab)))
         320 +                ex, ey = self._extent_xy(b)
         321 +                if np.linalg.norm(a + t * ab - o) > rad + np.hypot(ex, ey):
         322 +                    continue
  314    323              top = max(top, b["z"] + b["hz"])
  315    324          return max(SAFE_FLOOR, top + SAFE_CLR + held_below + FINGER)
  316    325  
@@ -387,7 +396,8 @@ class GeneratedApproach:
  387    396          b = boxes[name]
  388    397          yaw, tip = cand
  389    398          seeds = [q, self.q_nom, self.q_home]
  390        -        safe = self._safe_z(boxes)
         399 +        Tw0 = self._ee_world(q, base)
         400 +        safe = self._safe_z(boxes, path=(Tw0[:3, 3], (b["x"], b["y"])))
  391    401          grasp_z = tip + FINGER
  392    402          above = np.array([b["x"], b["y"], safe])
  393    403          gpos = np.array([b["x"], b["y"], grasp_z])
@@ -420,8 +430,11 @@ class GeneratedApproach:
  420    430          # xy offset of object centre relative to EE (in world, keep yaw constant)
  421    431          dxy = np.array([b["x"] - Tw[0, 3], b["y"] - Tw[1, 3]])
  422    432          seeds = [q, self.q_nom, self.q_home]
  423        -        safe = max(self._safe_z(boxes, exclude=name, held_below=b["hz"] + off - FINGER),
  424        -                   Tw[2, 3])
         433 +        hb = b["hz"] + off - FINGER
         434 +        ex0 = np.array([place_xy[0] - dxy[0], place_xy[1] - dxy[1]])
         435 +        bex, bey = self._extent_xy(b)
         436 +        safe = self._safe_z(boxes, exclude=name, held_below=hb,
         437 +                            path=(Tw[:3, 3], ex0), rad=max(0.08, np.hypot(bex, bey) + 0.02))
  425    438          safe = max(safe, bottom + b["hz"] + off + 0.03)
  426    439          ex = np.array([place_xy[0] - dxy[0], place_xy[1] - dxy[1]])
  427    440          pz = bottom + b["hz"] + off
@@ -429,13 +442,12 @@ class GeneratedApproach:
  429    442          ppos = np.array([ex[0], ex[1], pz])
  430    443          nb, ok = self._choose_base(base, [(above, yaw), (ppos, yaw)], seeds)
  431    444          segs = []
  432        -        segs.append(("move", np.array([Tw[0, 3], Tw[1, 3], safe]), yaw, "lift"))
         445 +        segs.append(("move", np.array([Tw[0, 3], Tw[1, 3], max(safe, Tw[2, 3])]), yaw, "lift"))
  433    446          if np.max(np.abs(nb - base)) > 1e-6:
  434    447              segs.append(("base", nb))
  435    448          segs.append(("move", above, yaw, "travel"))
  436    449          segs.append(("move", ppos, yaw, "place_descend"))
  437    450          segs.append(("grip", 1.0, None))
  438        -        segs.append(("move", np.array([ex[0], ex[1], pz + 0.06]), yaw, "retreat"))
  439    451          return segs
  440    452  
  441    453      def _held(self, boxes):
diff --git a/probe_dz.py b/probe_dz.py
new file mode 100644
index 0000000..ebfc781
--- /dev/null
+++ b/probe_dz.py
@@ -0,0 +1,18 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seed=int(sys.argv[1]); DZ=float(sys.argv[2])
           5 +class P(GeneratedApproach):
           6 +    def _plan_place(self, state, boxes, name, place_xy, bottom):
           7 +        if name=="target_block": bottom=bottom+DZ
           8 +        return super()._plan_place(state, boxes, name, place_xy, bottom)
           9 +    def _blocking(self, boxes): return []
          10 +env=make_env(); obs,info=env.reset(seed=seed, options={"object_count":0})
          11 +ap=P(env.action_space, env.observation_space, {}); ap.reset(obs,info)
          12 +rob=ap._robot(obs); r_=ap._boxes(obs)["target_region"]
          13 +for t in range(40):
          14 +    a=ap.get_action(obs)
          15 +    obs,r,term,trunc,info=env.step(a)
          16 +    bb=ap._boxes(obs)["target_block"]
          17 +    print(t, "a10",round(float(a[10]),2),"grasp",obs.get(rob,"grasp_active"),"blkg",bb["g"],"bottom-regtop",round(bb["z"]-bb["hz"]-r_["z"]-r_["hz"],4),"term",term, ap.cur[0] if ap.cur else None)
          18 +    if term: break
diff --git a/res_t.txt b/res_t.txt
index f398c79..2eb641c 100644
--- a/res_t.txt
+++ b/res_t.txt
@@ -1,41 +1,41 @@
    1        -(0, 2, True, 43, 31.6, 0.3, 0.078)
    2        -(1, 1, True, 45, 34.5, 0.3, 0.055)
    3        -(2, 2, True, 63, 61.2, 0.44, 0.068)
    4        -(3, 2, True, 40, 27.5, 0.22, 0.029)
    5        -(4, 2, True, 49, 42.5, 0.31, 0.049)
    6        -(5, 2, True, 65, 56.2, 0.4, 0.053)
    7        -(6, 1, True, 38, 25.2, 0.27, 0.073)
    8        -(7, 2, True, 50, 40.6, 0.29, 0.051)
    9        -(8, 2, True, 50, 53.1, 0.22, 0.02)
   10        -(9, 1, True, 28, 26.3, 0.11, 0.018)
   11        -(10, 2, True, 35, 37.3, 0.17, 0.043)
   12        -(11, 0, True, 22, 23.2, 0.1, 0.016)
   13        -(12, 1, True, 45, 44.1, 0.25, 0.024)
   14        -(13, 2, True, 58, 59.7, 0.37, 0.029)
   15        -(14, 0, True, 13, 12.9, 0.05, 0.01)
   16        -(15, 2, True, 37, 40.7, 0.21, 0.025)
   17        -(16, 1, True, 32, 22.7, 0.16, 0.019)
   18        -(17, 2, True, 51, 54.3, 0.36, 0.029)
   19        -(18, 2, True, 34, 32.8, 0.18, 0.025)
   20        -(19, 1, True, 42, 40.8, 0.39, 0.037)
   21        -(20, 2, True, 59, 66.2, 0.34, 0.026)
   22        -(21, 0, True, 30, 33.8, 0.2, 0.023)
   23        -(22, 2, True, 35, 37.9, 0.21, 0.026)
   24        -(23, 0, True, 29, 33.6, 0.19, 0.02)
   25        -(24, 1, True, 25, 24.1, 0.16, 0.023)
   26        -(25, 1, True, 49, 48.6, 0.24, 0.018)
   27        -(26, 2, True, 37, 33.4, 0.19, 0.026)
   28        -(27, 0, True, 37, 34.6, 0.23, 0.028)
   29        -(28, 1, True, 62, 58.0, 0.44, 0.04)
   30        -(29, 2, True, 22, 20.0, 0.11, 0.029)
   31        -(30, 0, True, 30, 26.2, 0.16, 0.027)
   32        -(31, 1, True, 51, 41.7, 0.32, 0.075)
   33        -(32, 2, True, 46, 37.0, 0.22, 0.02)
   34        -(33, 2, True, 47, 34.8, 0.28, 0.04)
   35        -(34, 0, True, 18, 15.4, 0.14, 0.07)
   36        -(35, 0, True, 20, 17.8, 0.16, 0.059)
   37        -(36, 1, True, 29, 18.2, 0.17, 0.028)
   38        -(37, 0, True, 23, 10.8, 0.17, 0.064)
   39        -(38, 0, True, 20, 8.1, 0.1, 0.014)
   40        -(39, 2, True, 52, 8.3, 0.28, 0.023)
   41        -success 40 / 40 mean steps 39.025
           1 +(0, 2, True, 40, 63.9, 0.3, 0.065)
           2 +(1, 1, True, 43, 61.8, 0.34, 0.049)
           3 +(2, 2, True, 61, 87.9, 0.4, 0.026)
           4 +(3, 2, True, 37, 60.8, 0.31, 0.064)
           5 +(4, 2, True, 45, 71.8, 0.34, 0.073)
           6 +(5, 2, True, 60, 71.7, 0.43, 0.034)
           7 +(6, 1, True, 36, 47.6, 0.25, 0.026)
           8 +(7, 2, True, 49, 69.0, 0.43, 0.085)
           9 +(8, 2, True, 45, 48.7, 0.27, 0.021)
          10 +(9, 1, True, 28, 23.1, 0.2, 0.039)
          11 +(10, 2, True, 32, 31.3, 0.24, 0.057)
          12 +(11, 0, True, 22, 23.1, 0.14, 0.017)
          13 +(12, 1, True, 42, 36.7, 0.27, 0.035)
          14 +(13, 2, True, 59, 57.7, 0.38, 0.025)
          15 +(14, 0, True, 13, 14.3, 0.07, 0.018)
          16 +(15, 2, True, 38, 33.3, 0.23, 0.022)
          17 +(16, 1, True, 30, 23.8, 0.22, 0.027)
          18 +(17, 2, True, 47, 37.2, 0.34, 0.034)
          19 +(18, 2, True, 31, 25.3, 0.19, 0.02)
          20 +(19, 1, True, 41, 32.7, 0.32, 0.047)
          21 +(20, 2, True, 57, 55.8, 0.41, 0.05)
          22 +(21, 0, True, 30, 29.4, 0.18, 0.021)
          23 +(22, 2, True, 32, 31.3, 0.16, 0.019)
          24 +(23, 0, True, 29, 30.0, 0.21, 0.026)
          25 +(24, 1, True, 24, 22.6, 0.15, 0.014)
          26 +(25, 1, True, 47, 47.3, 0.46, 0.092)
          27 +(26, 2, True, 35, 30.1, 0.27, 0.034)
          28 +(27, 0, True, 37, 34.6, 0.31, 0.033)
          29 +(28, 1, True, 61, 57.3, 0.48, 0.073)
          30 +(29, 2, True, 22, 18.8, 0.15, 0.029)
          31 +(30, 0, True, 30, 30.7, 0.29, 0.032)
          32 +(31, 1, True, 50, 45.7, 0.38, 0.069)
          33 +(32, 2, True, 40, 36.8, 0.2, 0.015)
          34 +(33, 2, True, 41, 35.7, 0.27, 0.035)
          35 +(34, 0, True, 18, 17.3, 0.12, 0.023)
          36 +(35, 0, True, 20, 19.4, 0.12, 0.021)
          37 +(36, 1, True, 25, 19.7, 0.12, 0.017)
          38 +(37, 0, True, 23, 14.2, 0.14, 0.02)
          39 +(38, 0, True, 20, 9.3, 0.12, 0.033)
          40 +(39, 2, True, 56, 5.8, 0.33, 0.024)
          41 +success 40 / 40 mean steps 37.4
```

</details>

<a id="C014"></a>
### C014 · Base-assisted y travel when arm is extended (ASSIST_MINX=0.2)

Commit `f62384604602303bcb8f889bac53a383a7ff0f98`; parents: 2c03cfcd71cd7b6a08433de725a1b999a9edf022. Recorded author date: 2026-09-30T23:24:27+02:00.

File roles (automatic): policy, setup/other.

- [E1114](01_timeline.md#E1114): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_f623846_approach.py) · [Exact all-file diff](evidence/diffs/C014_f623846.diff)

[Previous saved controller snapshot](evidence/versions/C013_2c03cfc_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a72711c..9e92b1e 100644
--- a/approach.py
+++ b/approach.py
@@ -121,6 +121,9 @@ TABLE_TOP = 0.075
  121    121  STEP_FAST = 0.12
  122    122  STEP_LOW = 0.05
  123    123  SAFE_FLOOR = 0.2
         124 +BASE_ASSIST = True
         125 +STEP_TRAVEL = 0.25
         126 +ASSIST_MINX = 0.2
  124    127  SAFE_CLR = 0.02
  125    128  MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
  126    129  TABLE_X = (0.10, 0.50)
@@ -601,15 +604,28 @@ class GeneratedApproach:
  601    604                  f = min(f, max(0.5 * self.scale, 0.02) / rerr)
  602    605              lim = 0.2 * max(self.scale, 0.05)
  603    606              dq = None
  604        -            for _it in range(4):
         607 +            assist = BASE_ASSIST and seg[3] == "travel" and abs(d[1]) > 1e-4 and \
         608 +                min(p[0], goal[0]) - self._mount(base)[0, 3] > ASSIST_MINX
         609 +            if assist:
         610 +                f = min(1.0, STEP_TRAVEL * self.scale / nd, 0.2 * self.scale / abs(d[1]))
         611 +                if rerr > 1e-9:
         612 +                    f = min(f, max(0.5 * self.scale, 0.02) / rerr)
         613 +            db = np.zeros(3)
         614 +            for _it in range(5):
  605    615                  tgt = p + d * f
  606    616                  Rs = _expm(rv * f) @ Tw[:3, :3]
  607        -                qt, err = self._ik_world(q, tgt, Rs, base)
         617 +                bb = base
         618 +                if assist:
         619 +                    db = np.array([0.0, d[1] * f, 0.0])
         620 +                    bb = base + db
         621 +                qt, err = self._ik_world(q, tgt, Rs, bb)
  608    622                  dq = qt - q
  609    623                  m = np.max(np.abs(dq))
  610    624                  if m <= lim:
  611    625                      break
  612    626                  f *= lim / m * 0.97
         627 +            if assist:
         628 +                act[0:3] = db.astype(np.float32)
  613    629              m = np.max(np.abs(dq))
  614    630              if m > lim:
  615    631                  dq *= lim / m
diff --git a/res_t.txt b/res_t.txt
index 2eb641c..1d07efc 100644
--- a/res_t.txt
+++ b/res_t.txt
@@ -1,41 +1,41 @@
    1        -(0, 2, True, 40, 63.9, 0.3, 0.065)
    2        -(1, 1, True, 43, 61.8, 0.34, 0.049)
    3        -(2, 2, True, 61, 87.9, 0.4, 0.026)
    4        -(3, 2, True, 37, 60.8, 0.31, 0.064)
    5        -(4, 2, True, 45, 71.8, 0.34, 0.073)
    6        -(5, 2, True, 60, 71.7, 0.43, 0.034)
    7        -(6, 1, True, 36, 47.6, 0.25, 0.026)
    8        -(7, 2, True, 49, 69.0, 0.43, 0.085)
    9        -(8, 2, True, 45, 48.7, 0.27, 0.021)
   10        -(9, 1, True, 28, 23.1, 0.2, 0.039)
   11        -(10, 2, True, 32, 31.3, 0.24, 0.057)
   12        -(11, 0, True, 22, 23.1, 0.14, 0.017)
   13        -(12, 1, True, 42, 36.7, 0.27, 0.035)
   14        -(13, 2, True, 59, 57.7, 0.38, 0.025)
   15        -(14, 0, True, 13, 14.3, 0.07, 0.018)
   16        -(15, 2, True, 38, 33.3, 0.23, 0.022)
   17        -(16, 1, True, 30, 23.8, 0.22, 0.027)
   18        -(17, 2, True, 47, 37.2, 0.34, 0.034)
   19        -(18, 2, True, 31, 25.3, 0.19, 0.02)
   20        -(19, 1, True, 41, 32.7, 0.32, 0.047)
   21        -(20, 2, True, 57, 55.8, 0.41, 0.05)
   22        -(21, 0, True, 30, 29.4, 0.18, 0.021)
   23        -(22, 2, True, 32, 31.3, 0.16, 0.019)
   24        -(23, 0, True, 29, 30.0, 0.21, 0.026)
   25        -(24, 1, True, 24, 22.6, 0.15, 0.014)
   26        -(25, 1, True, 47, 47.3, 0.46, 0.092)
   27        -(26, 2, True, 35, 30.1, 0.27, 0.034)
   28        -(27, 0, True, 37, 34.6, 0.31, 0.033)
   29        -(28, 1, True, 61, 57.3, 0.48, 0.073)
   30        -(29, 2, True, 22, 18.8, 0.15, 0.029)
   31        -(30, 0, True, 30, 30.7, 0.29, 0.032)
   32        -(31, 1, True, 50, 45.7, 0.38, 0.069)
   33        -(32, 2, True, 40, 36.8, 0.2, 0.015)
   34        -(33, 2, True, 41, 35.7, 0.27, 0.035)
   35        -(34, 0, True, 18, 17.3, 0.12, 0.023)
   36        -(35, 0, True, 20, 19.4, 0.12, 0.021)
   37        -(36, 1, True, 25, 19.7, 0.12, 0.017)
   38        -(37, 0, True, 23, 14.2, 0.14, 0.02)
   39        -(38, 0, True, 20, 9.3, 0.12, 0.033)
   40        -(39, 2, True, 56, 5.8, 0.33, 0.024)
   41        -success 40 / 40 mean steps 37.4
           1 +(0, 2, True, 37, 25.1, 0.28, 0.061)
           2 +(1, 1, True, 38, 31.7, 0.24, 0.02)
           3 +(2, 2, True, 61, 59.5, 0.42, 0.042)
           4 +(3, 2, True, 70, 37.3, 2.23, 0.124)
           5 +(4, 2, True, 44, 31.3, 0.29, 0.023)
           6 +(5, 2, True, 53, 32.6, 0.41, 0.038)
           7 +(6, 1, True, 28, 11.0, 0.82, 0.638)
           8 +(7, 2, True, 47, 33.9, 0.33, 0.041)
           9 +(8, 2, True, 35, 37.2, 0.2, 0.022)
          10 +(9, 1, True, 29, 22.5, 0.2, 0.032)
          11 +(10, 2, True, 31, 29.3, 0.19, 0.048)
          12 +(11, 0, True, 20, 18.6, 0.09, 0.015)
          13 +(12, 1, True, 42, 32.1, 0.28, 0.044)
          14 +(13, 2, True, 55, 47.5, 0.38, 0.05)
          15 +(14, 0, True, 14, 11.9, 0.07, 0.027)
          16 +(15, 2, True, 37, 28.2, 0.17, 0.031)
          17 +(16, 1, True, 29, 19.8, 0.14, 0.02)
          18 +(17, 2, True, 42, 39.0, 0.21, 0.022)
          19 +(18, 2, True, 29, 23.7, 0.16, 0.025)
          20 +(19, 1, True, 40, 28.0, 0.27, 0.05)
          21 +(20, 2, True, 48, 36.8, 0.25, 0.036)
          22 +(21, 0, True, 27, 30.4, 0.15, 0.023)
          23 +(22, 2, True, 26, 34.6, 0.13, 0.02)
          24 +(23, 0, True, 29, 36.2, 0.23, 0.052)
          25 +(24, 1, True, 18, 17.3, 0.1, 0.015)
          26 +(25, 1, True, 37, 45.2, 1.6, 1.441)
          27 +(26, 2, True, 27, 28.1, 0.13, 0.019)
          28 +(27, 0, True, 35, 42.8, 0.27, 0.027)
          29 +(28, 1, True, 56, 54.6, 1.03, 0.51)
          30 +(29, 2, True, 18, 18.3, 0.08, 0.018)
          31 +(30, 0, True, 22, 20.2, 0.14, 0.023)
          32 +(31, 1, True, 47, 43.8, 0.31, 0.025)
          33 +(32, 2, True, 37, 38.7, 0.34, 0.06)
          34 +(33, 2, True, 37, 35.1, 0.22, 0.03)
          35 +(34, 0, True, 16, 17.8, 0.12, 0.021)
          36 +(35, 0, True, 16, 18.8, 0.14, 0.04)
          37 +(36, 1, True, 24, 19.5, 0.17, 0.037)
          38 +(37, 0, True, 17, 11.1, 0.13, 0.021)
          39 +(38, 0, True, 17, 8.9, 0.19, 0.102)
          40 +(39, 2, True, 48, 5.8, 0.38, 0.043)
          41 +success 40 / 40 mean steps 34.575
diff --git a/res_t2.txt b/res_t2.txt
new file mode 100644
index 0000000..508a733
--- /dev/null
+++ b/res_t2.txt
@@ -0,0 +1,81 @@
           1 +(40, 1, True, 76, 44.4, 2.46, 0.109)
           2 +(41, 1, True, 27, 35.7, 0.15, 0.022)
           3 +(42, 0, True, 19, 24.5, 0.16, 0.057)
           4 +(43, 1, True, 30, 39.5, 0.16, 0.02)
           5 +(44, 2, True, 36, 39.4, 0.27, 0.043)
           6 +(45, 2, True, 47, 45.7, 0.27, 0.03)
           7 +(46, 1, True, 23, 23.4, 0.15, 0.025)
           8 +(47, 0, True, 14, 10.9, 0.06, 0.016)
           9 +(48, 0, True, 16, 17.5, 0.07, 0.014)
          10 +(49, 0, True, 17, 16.9, 0.17, 0.064)
          11 +(50, 2, True, 105, 67.7, 3.5, 0.158)
          12 +(51, 1, True, 26, 24.4, 0.19, 0.039)
          13 +(52, 2, True, 60, 60.6, 0.99, 0.553)
          14 +(53, 2, True, 52, 45.1, 0.44, 0.039)
          15 +(54, 0, True, 19, 19.2, 0.09, 0.014)
          16 +(55, 2, True, 55, 55.2, 0.44, 0.035)
          17 +(56, 1, True, 30, 23.9, 0.2, 0.02)
          18 +(57, 0, True, 17, 13.0, 0.15, 0.049)
          19 +(58, 1, True, 33, 25.7, 0.29, 0.035)
          20 +(59, 2, True, 70, 72.2, 0.61, 0.059)
          21 +(60, 0, True, 16, 12.4, 0.14, 0.02)
          22 +(61, 1, True, 34, 33.2, 0.22, 0.033)
          23 +(62, 1, True, 27, 22.4, 0.19, 0.022)
          24 +(63, 1, True, 36, 30.5, 0.21, 0.021)
          25 +(64, 1, True, 27, 22.5, 0.16, 0.021)
          26 +(65, 0, True, 35, 27.1, 0.25, 0.03)
          27 +(66, 2, True, 39, 31.4, 0.26, 0.028)
          28 +(67, 2, True, 45, 41.5, 0.28, 0.059)
          29 +(68, 1, True, 22, 17.9, 0.19, 0.044)
          30 +(69, 0, True, 15, 9.5, 0.1, 0.044)
          31 +(70, 1, True, 38, 33.4, 0.28, 0.04)
          32 +(71, 2, True, 62, 60.7, 0.47, 0.03)
          33 +(72, 2, True, 58, 55.3, 0.5, 0.061)
          34 +(73, 2, True, 44, 40.3, 0.29, 0.041)
          35 +(74, 0, True, 16, 14.1, 0.09, 0.015)
          36 +(75, 1, True, 24, 20.9, 0.18, 0.032)
          37 +(76, 1, True, 44, 36.7, 0.41, 0.043)
          38 +(77, 0, True, 23, 19.1, 0.18, 0.042)
          39 +(78, 2, True, 32, 22.7, 0.22, 0.027)
          40 +(79, 0, True, 14, 7.0, 0.09, 0.031)
          41 +(80, 2, True, 43, 32.7, 0.27, 0.036)
          42 +(81, 0, True, 25, 22.9, 0.19, 0.031)
          43 +(82, 2, True, 51, 41.3, 0.31, 0.044)
          44 +(83, 2, True, 34, 28.7, 0.23, 0.049)
          45 +(84, 1, True, 31, 23.4, 0.2, 0.024)
          46 +(85, 2, True, 41, 28.7, 0.22, 0.022)
          47 +(86, 2, True, 44, 33.3, 0.21, 0.023)
          48 +(87, 1, True, 39, 28.8, 0.17, 0.019)
          49 +(88, 1, True, 35, 22.7, 0.18, 0.02)
          50 +(89, 2, True, 47, 38.6, 0.82, 0.536)
          51 +(90, 1, True, 25, 21.8, 0.13, 0.016)
          52 +(91, 2, True, 35, 32.9, 0.2, 0.033)
          53 +(92, 1, True, 32, 20.9, 0.17, 0.022)
          54 +(93, 2, True, 47, 45.7, 0.22, 0.018)
          55 +(94, 0, True, 22, 17.2, 0.1, 0.011)
          56 +(95, 1, True, 37, 28.4, 0.21, 0.029)
          57 +(96, 2, True, 50, 44.8, 0.3, 0.027)
          58 +(97, 0, True, 27, 18.9, 0.15, 0.011)
          59 +(98, 1, True, 42, 53.0, 0.3, 0.026)
          60 +(99, 2, True, 41, 35.7, 0.27, 0.036)
          61 +(100, 2, True, 39, 35.4, 0.22, 0.018)
          62 +(101, 0, True, 18, 16.1, 0.1, 0.017)
          63 +(102, 1, True, 26, 31.5, 0.2, 0.048)
          64 +(103, 1, True, 28, 37.6, 0.19, 0.043)
          65 +(104, 2, True, 49, 63.5, 0.4, 0.054)
          66 +(105, 0, True, 17, 9.8, 0.11, 0.028)
          67 +(106, 1, True, 23, 30.9, 0.3, 0.109)
          68 +(107, 0, True, 18, 23.3, 0.17, 0.055)
          69 +(108, 0, True, 20, 29.0, 0.14, 0.02)
          70 +(109, 1, True, 35, 44.6, 0.24, 0.032)
          71 +(110, 1, True, 43, 50.9, 0.35, 0.085)
          72 +(111, 1, True, 24, 24.6, 0.12, 0.016)
          73 +(112, 0, True, 22, 23.3, 0.14, 0.017)
          74 +(113, 0, True, 23, 29.3, 0.14, 0.016)
          75 +(114, 0, True, 18, 24.6, 0.08, 0.012)
          76 +(115, 1, True, 37, 26.5, 0.22, 0.02)
          77 +(116, 0, True, 20, 17.7, 0.08, 0.014)
          78 +(117, 0, True, 18, 11.9, 0.11, 0.028)
          79 +(118, 1, True, 35, 7.6, 0.2, 0.022)
          80 +(119, 1, True, 43, 8.1, 0.32, 0.047)
          81 +success 80 / 80 mean steps 34.0875
diff --git a/res_t8.txt b/res_t8.txt
new file mode 100644
index 0000000..ed27f32
--- /dev/null
+++ b/res_t8.txt
@@ -0,0 +1,25 @@
           1 +(0, 8, True, 107, 52.8, 1.03, 0.078)
           2 +(1, 8, True, 152, 85.7, 1.61, 0.072)
           3 +(2, 8, True, 79, 57.6, 1.4, 0.646)
           4 +(3, 8, True, 89, 51.9, 0.84, 0.085)
           5 +(4, 8, True, 197, 126.5, 2.47, 0.642)
           6 +(5, 8, True, 127, 66.6, 1.3, 0.117)
           7 +(6, 8, True, 720, 243.6, 5.7, 0.125)
           8 +(7, 8, True, 161, 92.0, 1.6, 0.098)
           9 +(8, 8, True, 121, 72.7, 1.05, 0.102)
          10 +(9, 8, True, 99, 53.2, 1.01, 0.11)
          11 +(10, 8, True, 98, 55.1, 1.0, 0.111)
          12 +(11, 8, True, 98, 67.6, 0.88, 0.102)
          13 +(12, 8, True, 162, 106.9, 1.58, 0.113)
          14 +(13, 8, True, 334, 138.1, 2.76, 0.1)
          15 +(14, 8, True, 60, 35.4, 0.59, 0.095)
          16 +(15, 8, True, 167, 95.0, 2.12, 0.556)
          17 +(16, 8, True, 77, 43.8, 0.7, 0.105)
          18 +(17, 8, True, 86, 48.3, 0.79, 0.054)
          19 +(18, 8, True, 141, 77.4, 1.63, 0.097)
          20 +(19, 8, True, 640, 110.2, 4.77, 0.333)
          21 +(20, 8, True, 101, 55.3, 1.01, 0.071)
          22 +(21, 8, True, 138, 62.3, 1.9, 0.647)
          23 +(22, 8, True, 91, 40.8, 0.7, 0.069)
          24 +(23, 8, True, 111, 21.8, 0.85, 0.119)
          25 +success 24 / 24 mean steps 173.16666666666666
```

</details>

<a id="C015"></a>
### C015 · Joint-space travel when interpolated path clears local obstacles

Commit `d7ac6b85afa9d8d4b1068e513b135b702934567e`; parents: f62384604602303bcb8f889bac53a383a7ff0f98. Recorded author date: 2026-09-30T23:41:08+02:00.

File roles (automatic): policy, setup/other.

- [E1165](01_timeline.md#E1165): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_d7ac6b8_approach.py) · [Exact all-file diff](evidence/diffs/C015_d7ac6b8.diff)

[Previous saved controller snapshot](evidence/versions/C014_f623846_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9e92b1e..26c8a0a 100644
--- a/approach.py
+++ b/approach.py
@@ -124,6 +124,7 @@ SAFE_FLOOR = 0.2
  124    124  BASE_ASSIST = True
  125    125  STEP_TRAVEL = 0.25
  126    126  ASSIST_MINX = 0.2
         127 +JOINT_TRAVEL = True
  127    128  SAFE_CLR = 0.02
  128    129  MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
  129    130  TABLE_X = (0.10, 0.50)
@@ -550,7 +551,24 @@ class GeneratedApproach:
  550    551                  self.cur = self.segs.pop(0)
  551    552                  self.best_d = None
  552    553                  self.stall = 0
         554 +                self.jplan = None
  553    555              seg = self.cur
         556 +            if JOINT_TRAVEL and seg[0] == "move" and seg[3] == "travel" and self.jplan is None:
         557 +                self.jplan = self._joint_plan(state, seg)
         558 +            if self.jplan is not None and self.jplan is not False and seg[0] == "move":
         559 +                if rejected:
         560 +                    self.jplan = False
         561 +                else:
         562 +                    dq = self.jplan - q
         563 +                    m = np.max(np.abs(dq))
         564 +                    if m > 1e-4:
         565 +                        lim = 0.2 * max(self.scale, 0.05)
         566 +                        if m > lim:
         567 +                            dq *= lim / m
         568 +                        act[3:10] = dq.astype(np.float32)
         569 +                        self.last_cmd = True
         570 +                        return act
         571 +                    self.jplan = False
  554    572              if seg[0] == "grip":
  555    573                  act[10] = seg[1]
  556    574                  self.cur = None
@@ -637,6 +655,53 @@ class GeneratedApproach:
  637    655              return act
  638    656          return act
  639    657  
         658 +    def _req_z(self, boxes, xy, held, hb):
         659 +        top = TABLE_TOP + 0.03
         660 +        rad = 0.08
         661 +        if held is not None:
         662 +            ex, ey = self._extent_xy(boxes[held])
         663 +            rad = max(rad, np.hypot(ex, ey) + 0.02)
         664 +        for n, b in boxes.items():
         665 +            if b["g"] > 0.5 or n == held:
         666 +                continue
         667 +            ex, ey = self._extent_xy(b)
         668 +            if np.hypot(xy[0] - b["x"], xy[1] - b["y"]) > rad + np.hypot(ex, ey):
         669 +                continue
         670 +            top = max(top, b["z"] + b["hz"])
         671 +        return top + SAFE_CLR + hb + FINGER
         672 +
         673 +    def _joint_plan(self, state, seg):
         674 +        q = self._q(state)
         675 +        base = self._base(state)
         676 +        goal, yaw = seg[1], seg[2]
         677 +        Tw = self._ee_world(q, base)
         678 +        Rt = down_R(yaw) if yaw is not None else down_R(_yaw_of(Tw[:3, :3]))
         679 +        boxes = self._boxes(state)
         680 +        held = self._held(boxes)
         681 +        hb = 0.0
         682 +        if held is not None:
         683 +            b = boxes[held]
         684 +            hb = max(0.0, (Tw[2, 3] - FINGER) - (b["z"] - b["hz"]))
         685 +        best = None
         686 +        for sd in (q, self.q_nom, self.q_home):
         687 +            qg, err = self._ik_world(sd, goal, Rt, base, iters=150)
         688 +            if err > 1e-4:
         689 +                continue
         690 +            dqm = np.max(np.abs(qg - q))
         691 +            if best is None or dqm < best[0]:
         692 +                best = (dqm, qg)
         693 +        if best is None:
         694 +            return False
         695 +        qg = best[1]
         696 +        for sv in np.linspace(0.0, 1.0, 13)[1:-1]:
         697 +            qs = q + sv * (qg - q)
         698 +            T = self._ee_world(qs, base)
         699 +            if T[2, 2] > -0.9:
         700 +                return False
         701 +            if T[2, 3] < self._req_z(boxes, T[:2, 3], held, hb) - 0.005:
         702 +                return False
         703 +        return qg
         704 +
  640    705      def _handle_reject(self, state):
  641    706          seg = self.cur
  642    707          tag = seg[3] if (seg[0] == "move" and len(seg) > 3) else None
diff --git a/res_t.txt b/res_t.txt
index 1d07efc..acabd4d 100644
--- a/res_t.txt
+++ b/res_t.txt
@@ -1,41 +1,41 @@
    1        -(0, 2, True, 37, 25.1, 0.28, 0.061)
    2        -(1, 1, True, 38, 31.7, 0.24, 0.02)
    3        -(2, 2, True, 61, 59.5, 0.42, 0.042)
    4        -(3, 2, True, 70, 37.3, 2.23, 0.124)
    5        -(4, 2, True, 44, 31.3, 0.29, 0.023)
    6        -(5, 2, True, 53, 32.6, 0.41, 0.038)
    7        -(6, 1, True, 28, 11.0, 0.82, 0.638)
    8        -(7, 2, True, 47, 33.9, 0.33, 0.041)
    9        -(8, 2, True, 35, 37.2, 0.2, 0.022)
   10        -(9, 1, True, 29, 22.5, 0.2, 0.032)
   11        -(10, 2, True, 31, 29.3, 0.19, 0.048)
   12        -(11, 0, True, 20, 18.6, 0.09, 0.015)
   13        -(12, 1, True, 42, 32.1, 0.28, 0.044)
   14        -(13, 2, True, 55, 47.5, 0.38, 0.05)
   15        -(14, 0, True, 14, 11.9, 0.07, 0.027)
   16        -(15, 2, True, 37, 28.2, 0.17, 0.031)
   17        -(16, 1, True, 29, 19.8, 0.14, 0.02)
   18        -(17, 2, True, 42, 39.0, 0.21, 0.022)
   19        -(18, 2, True, 29, 23.7, 0.16, 0.025)
   20        -(19, 1, True, 40, 28.0, 0.27, 0.05)
   21        -(20, 2, True, 48, 36.8, 0.25, 0.036)
   22        -(21, 0, True, 27, 30.4, 0.15, 0.023)
   23        -(22, 2, True, 26, 34.6, 0.13, 0.02)
   24        -(23, 0, True, 29, 36.2, 0.23, 0.052)
   25        -(24, 1, True, 18, 17.3, 0.1, 0.015)
   26        -(25, 1, True, 37, 45.2, 1.6, 1.441)
   27        -(26, 2, True, 27, 28.1, 0.13, 0.019)
   28        -(27, 0, True, 35, 42.8, 0.27, 0.027)
   29        -(28, 1, True, 56, 54.6, 1.03, 0.51)
   30        -(29, 2, True, 18, 18.3, 0.08, 0.018)
   31        -(30, 0, True, 22, 20.2, 0.14, 0.023)
   32        -(31, 1, True, 47, 43.8, 0.31, 0.025)
   33        -(32, 2, True, 37, 38.7, 0.34, 0.06)
   34        -(33, 2, True, 37, 35.1, 0.22, 0.03)
   35        -(34, 0, True, 16, 17.8, 0.12, 0.021)
   36        -(35, 0, True, 16, 18.8, 0.14, 0.04)
   37        -(36, 1, True, 24, 19.5, 0.17, 0.037)
   38        -(37, 0, True, 17, 11.1, 0.13, 0.021)
   39        -(38, 0, True, 17, 8.9, 0.19, 0.102)
   40        -(39, 2, True, 48, 5.8, 0.38, 0.043)
   41        -success 40 / 40 mean steps 34.575
           1 +(0, 2, True, 42, 31.8, 0.43, 0.089)
           2 +(1, 1, True, 36, 26.3, 0.18, 0.04)
           3 +(2, 2, True, 59, 59.1, 0.34, 0.052)
           4 +(3, 2, True, 35, 27.4, 0.29, 0.068)
           5 +(4, 2, True, 44, 39.5, 0.37, 0.051)
           6 +(5, 2, True, 56, 48.3, 0.51, 0.072)
           7 +(6, 1, True, 34, 18.0, 0.29, 0.069)
           8 +(7, 2, True, 45, 37.4, 0.33, 0.066)
           9 +(8, 2, True, 43, 52.1, 0.25, 0.032)
          10 +(9, 1, True, 27, 23.3, 0.19, 0.046)
          11 +(10, 2, True, 34, 36.5, 0.24, 0.051)
          12 +(11, 0, True, 19, 19.5, 0.08, 0.02)
          13 +(12, 1, True, 38, 38.7, 0.21, 0.049)
          14 +(13, 2, True, 55, 57.8, 0.27, 0.045)
          15 +(14, 0, True, 12, 12.9, 0.06, 0.014)
          16 +(15, 2, True, 38, 37.2, 0.17, 0.027)
          17 +(16, 1, True, 28, 22.2, 0.23, 0.045)
          18 +(17, 2, True, 45, 39.9, 0.3, 0.053)
          19 +(18, 2, True, 29, 25.7, 0.17, 0.051)
          20 +(19, 1, True, 42, 39.9, 0.29, 0.04)
          21 +(20, 2, True, 52, 54.1, 0.26, 0.039)
          22 +(21, 0, True, 25, 22.3, 0.14, 0.063)
          23 +(22, 2, True, 29, 24.9, 0.14, 0.024)
          24 +(23, 0, True, 26, 29.2, 0.09, 0.035)
          25 +(24, 1, True, 20, 21.1, 0.08, 0.021)
          26 +(25, 1, True, 43, 49.5, 0.16, 0.035)
          27 +(26, 2, True, 33, 36.0, 0.14, 0.03)
          28 +(27, 0, True, 26, 23.8, 0.09, 0.023)
          29 +(28, 1, True, 42, 40.9, 0.18, 0.032)
          30 +(29, 2, True, 18, 19.3, 0.08, 0.023)
          31 +(30, 0, True, 26, 23.7, 0.07, 0.021)
          32 +(31, 1, True, 44, 39.2, 0.16, 0.018)
          33 +(32, 2, True, 37, 35.2, 0.18, 0.024)
          34 +(33, 2, True, 42, 30.8, 0.27, 0.048)
          35 +(34, 0, True, 16, 16.7, 0.04, 0.015)
          36 +(35, 0, True, 17, 19.1, 0.06, 0.022)
          37 +(36, 1, True, 25, 16.9, 0.12, 0.022)
          38 +(37, 0, True, 20, 11.3, 0.07, 0.023)
          39 +(38, 0, True, 17, 7.1, 0.07, 0.024)
          40 +(39, 2, True, 54, 7.0, 0.28, 0.032)
          41 +success 40 / 40 mean steps 34.325
```

</details>

<a id="C016"></a>
### C016 · Per-call compute time guard

Commit `b3f709da810d2c27bf68b431808fbbfbfa8b64cf`; parents: d7ac6b85afa9d8d4b1068e513b135b702934567e. Recorded author date: 2026-09-30T23:58:21+02:00.

File roles (automatic): policy, setup/other.

- [E1231](01_timeline.md#E1231): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_b3f709d_approach.py) · [Exact all-file diff](evidence/diffs/C016_b3f709d.diff)

[Previous saved controller snapshot](evidence/versions/C015_d7ac6b8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 26c8a0a..d876a4e 100644
--- a/approach.py
+++ b/approach.py
@@ -1,6 +1,7 @@
    1      1  """Obstruction3D approach: clear obstructions off the target region, then place the
    2      2  target block on it.  Uses an internal FK/IK model of the Kinova Gen3 (arm base at the
    3      3  world origin, verified empirically) and Cartesian straight-line motions."""
           4 +import time
    4      5  import numpy as np
    5      6  
    6      7  PI = np.pi
@@ -544,7 +545,10 @@ class GeneratedApproach:
  544    545              else:
  545    546                  self._handle_reject(state)
  546    547  
         548 +        t_start = time.time()
  547    549          for _ in range(30):
         550 +            if time.time() - t_start > 1.5:
         551 +                break
  548    552              if self.cur is None:
  549    553                  if not self.segs:
  550    554                      self.segs = self._replan(state)
diff --git a/res_t2.txt b/res_t2.txt
index 508a733..017f422 100644
--- a/res_t2.txt
+++ b/res_t2.txt
@@ -1,81 +1,121 @@
    1        -(40, 1, True, 76, 44.4, 2.46, 0.109)
    2        -(41, 1, True, 27, 35.7, 0.15, 0.022)
    3        -(42, 0, True, 19, 24.5, 0.16, 0.057)
    4        -(43, 1, True, 30, 39.5, 0.16, 0.02)
    5        -(44, 2, True, 36, 39.4, 0.27, 0.043)
    6        -(45, 2, True, 47, 45.7, 0.27, 0.03)
    7        -(46, 1, True, 23, 23.4, 0.15, 0.025)
    8        -(47, 0, True, 14, 10.9, 0.06, 0.016)
    9        -(48, 0, True, 16, 17.5, 0.07, 0.014)
   10        -(49, 0, True, 17, 16.9, 0.17, 0.064)
   11        -(50, 2, True, 105, 67.7, 3.5, 0.158)
   12        -(51, 1, True, 26, 24.4, 0.19, 0.039)
   13        -(52, 2, True, 60, 60.6, 0.99, 0.553)
   14        -(53, 2, True, 52, 45.1, 0.44, 0.039)
   15        -(54, 0, True, 19, 19.2, 0.09, 0.014)
   16        -(55, 2, True, 55, 55.2, 0.44, 0.035)
   17        -(56, 1, True, 30, 23.9, 0.2, 0.02)
   18        -(57, 0, True, 17, 13.0, 0.15, 0.049)
   19        -(58, 1, True, 33, 25.7, 0.29, 0.035)
   20        -(59, 2, True, 70, 72.2, 0.61, 0.059)
   21        -(60, 0, True, 16, 12.4, 0.14, 0.02)
   22        -(61, 1, True, 34, 33.2, 0.22, 0.033)
   23        -(62, 1, True, 27, 22.4, 0.19, 0.022)
   24        -(63, 1, True, 36, 30.5, 0.21, 0.021)
   25        -(64, 1, True, 27, 22.5, 0.16, 0.021)
   26        -(65, 0, True, 35, 27.1, 0.25, 0.03)
   27        -(66, 2, True, 39, 31.4, 0.26, 0.028)
   28        -(67, 2, True, 45, 41.5, 0.28, 0.059)
   29        -(68, 1, True, 22, 17.9, 0.19, 0.044)
   30        -(69, 0, True, 15, 9.5, 0.1, 0.044)
   31        -(70, 1, True, 38, 33.4, 0.28, 0.04)
   32        -(71, 2, True, 62, 60.7, 0.47, 0.03)
   33        -(72, 2, True, 58, 55.3, 0.5, 0.061)
   34        -(73, 2, True, 44, 40.3, 0.29, 0.041)
   35        -(74, 0, True, 16, 14.1, 0.09, 0.015)
   36        -(75, 1, True, 24, 20.9, 0.18, 0.032)
   37        -(76, 1, True, 44, 36.7, 0.41, 0.043)
   38        -(77, 0, True, 23, 19.1, 0.18, 0.042)
   39        -(78, 2, True, 32, 22.7, 0.22, 0.027)
   40        -(79, 0, True, 14, 7.0, 0.09, 0.031)
   41        -(80, 2, True, 43, 32.7, 0.27, 0.036)
   42        -(81, 0, True, 25, 22.9, 0.19, 0.031)
   43        -(82, 2, True, 51, 41.3, 0.31, 0.044)
   44        -(83, 2, True, 34, 28.7, 0.23, 0.049)
   45        -(84, 1, True, 31, 23.4, 0.2, 0.024)
   46        -(85, 2, True, 41, 28.7, 0.22, 0.022)
   47        -(86, 2, True, 44, 33.3, 0.21, 0.023)
   48        -(87, 1, True, 39, 28.8, 0.17, 0.019)
   49        -(88, 1, True, 35, 22.7, 0.18, 0.02)
   50        -(89, 2, True, 47, 38.6, 0.82, 0.536)
   51        -(90, 1, True, 25, 21.8, 0.13, 0.016)
   52        -(91, 2, True, 35, 32.9, 0.2, 0.033)
   53        -(92, 1, True, 32, 20.9, 0.17, 0.022)
   54        -(93, 2, True, 47, 45.7, 0.22, 0.018)
   55        -(94, 0, True, 22, 17.2, 0.1, 0.011)
   56        -(95, 1, True, 37, 28.4, 0.21, 0.029)
   57        -(96, 2, True, 50, 44.8, 0.3, 0.027)
   58        -(97, 0, True, 27, 18.9, 0.15, 0.011)
   59        -(98, 1, True, 42, 53.0, 0.3, 0.026)
   60        -(99, 2, True, 41, 35.7, 0.27, 0.036)
   61        -(100, 2, True, 39, 35.4, 0.22, 0.018)
   62        -(101, 0, True, 18, 16.1, 0.1, 0.017)
   63        -(102, 1, True, 26, 31.5, 0.2, 0.048)
   64        -(103, 1, True, 28, 37.6, 0.19, 0.043)
   65        -(104, 2, True, 49, 63.5, 0.4, 0.054)
   66        -(105, 0, True, 17, 9.8, 0.11, 0.028)
   67        -(106, 1, True, 23, 30.9, 0.3, 0.109)
   68        -(107, 0, True, 18, 23.3, 0.17, 0.055)
   69        -(108, 0, True, 20, 29.0, 0.14, 0.02)
   70        -(109, 1, True, 35, 44.6, 0.24, 0.032)
   71        -(110, 1, True, 43, 50.9, 0.35, 0.085)
   72        -(111, 1, True, 24, 24.6, 0.12, 0.016)
   73        -(112, 0, True, 22, 23.3, 0.14, 0.017)
   74        -(113, 0, True, 23, 29.3, 0.14, 0.016)
   75        -(114, 0, True, 18, 24.6, 0.08, 0.012)
   76        -(115, 1, True, 37, 26.5, 0.22, 0.02)
   77        -(116, 0, True, 20, 17.7, 0.08, 0.014)
   78        -(117, 0, True, 18, 11.9, 0.11, 0.028)
   79        -(118, 1, True, 35, 7.6, 0.2, 0.022)
   80        -(119, 1, True, 43, 8.1, 0.32, 0.047)
   81        -success 80 / 80 mean steps 34.0875
           1 +(40, 1, True, 80, 58.3, 2.73, 0.122)
           2 +(41, 1, True, 26, 32.7, 0.17, 0.034)
           3 +(42, 0, True, 18, 17.6, 0.06, 0.019)
           4 +(43, 1, True, 28, 32.6, 0.14, 0.022)
           5 +(44, 2, True, 34, 37.8, 0.23, 0.037)
           6 +(45, 2, True, 46, 50.5, 0.26, 0.028)
           7 +(46, 1, True, 23, 18.9, 0.16, 0.038)
           8 +(47, 0, True, 14, 4.5, 0.1, 0.034)
           9 +(48, 0, True, 14, 16.7, 0.07, 0.017)
          10 +(49, 0, True, 16, 15.6, 0.11, 0.046)
          11 +(50, 2, True, 48, 52.0, 0.36, 0.153)
          12 +(51, 1, True, 25, 24.6, 0.16, 0.024)
          13 +(52, 2, True, 57, 67.5, 1.13, 0.839)
          14 +(53, 2, True, 49, 51.9, 0.28, 0.051)
          15 +(54, 0, True, 16, 19.6, 0.06, 0.013)
          16 +(55, 2, True, 49, 57.3, 0.36, 0.086)
          17 +(56, 1, True, 26, 19.5, 0.18, 0.029)
          18 +(57, 0, True, 16, 11.1, 0.05, 0.017)
          19 +(58, 1, True, 28, 34.0, 0.17, 0.056)
          20 +(59, 2, True, 61, 66.0, 0.35, 0.047)
          21 +(60, 0, True, 15, 12.2, 0.08, 0.028)
          22 +(61, 1, True, 32, 35.7, 0.14, 0.031)
          23 +(62, 1, True, 26, 26.1, 0.13, 0.021)
          24 +(63, 1, True, 33, 34.5, 0.15, 0.028)
          25 +(64, 1, True, 26, 20.5, 0.16, 0.032)
          26 +(65, 0, True, 27, 27.3, 0.1, 0.043)
          27 +(66, 2, True, 38, 36.1, 0.25, 0.027)
          28 +(67, 2, True, 43, 44.5, 0.23, 0.039)
          29 +(68, 1, True, 21, 26.8, 0.07, 0.026)
          30 +(69, 0, True, 15, 11.2, 0.06, 0.021)
          31 +(70, 1, True, 35, 36.5, 0.16, 0.028)
          32 +(71, 2, True, 46, 47.9, 0.27, 0.039)
          33 +(72, 2, True, 54, 64.1, 0.38, 0.075)
          34 +(73, 2, True, 43, 47.3, 0.25, 0.056)
          35 +(74, 0, True, 15, 13.0, 0.06, 0.018)
          36 +(75, 1, True, 23, 21.7, 0.15, 0.034)
          37 +(76, 1, True, 40, 43.5, 0.18, 0.038)
          38 +(77, 0, True, 20, 13.3, 0.1, 0.035)
          39 +(78, 2, True, 30, 27.9, 0.13, 0.034)
          40 +(79, 0, True, 14, 14.2, 0.06, 0.03)
          41 +(80, 2, True, 42, 43.8, 0.25, 0.027)
          42 +(81, 0, True, 21, 24.8, 0.07, 0.018)
          43 +(82, 2, True, 49, 48.7, 0.31, 0.039)
          44 +(83, 2, True, 33, 34.2, 0.18, 0.037)
          45 +(84, 1, True, 28, 21.5, 0.16, 0.027)
          46 +(85, 2, True, 40, 33.7, 0.34, 0.045)
          47 +(86, 2, True, 44, 44.3, 0.22, 0.033)
          48 +(87, 1, True, 37, 32.3, 0.26, 0.071)
          49 +(88, 1, True, 34, 30.1, 0.21, 0.027)
          50 +(89, 2, True, 46, 51.6, 0.95, 0.63)
          51 +(90, 1, True, 25, 23.4, 0.16, 0.027)
          52 +(91, 2, True, 33, 33.8, 0.25, 0.066)
          53 +(92, 1, True, 34, 27.8, 0.18, 0.033)
          54 +(93, 2, True, 51, 55.3, 0.31, 0.036)
          55 +(94, 0, True, 21, 22.9, 0.14, 0.05)
          56 +(95, 1, True, 30, 29.4, 0.23, 0.041)
          57 +(96, 2, True, 45, 46.2, 0.29, 0.047)
          58 +(97, 0, True, 24, 24.4, 0.11, 0.055)
          59 +(98, 1, True, 37, 37.2, 0.16, 0.024)
          60 +(99, 2, True, 39, 42.3, 0.29, 0.031)
          61 +(100, 2, True, 38, 41.3, 0.23, 0.036)
          62 +(101, 0, True, 15, 13.7, 0.08, 0.022)
          63 +(102, 1, True, 26, 35.8, 0.14, 0.029)
          64 +(103, 1, True, 29, 38.1, 0.21, 0.042)
          65 +(104, 2, True, 47, 67.3, 0.25, 0.038)
          66 +(105, 0, True, 15, 12.4, 0.08, 0.023)
          67 +(106, 1, True, 21, 31.0, 0.06, 0.016)
          68 +(107, 0, True, 17, 27.8, 0.05, 0.017)
          69 +(108, 0, True, 18, 28.9, 0.13, 0.079)
          70 +(109, 1, True, 33, 51.4, 0.2, 0.051)
          71 +(110, 1, True, 37, 54.1, 0.18, 0.032)
          72 +(111, 1, True, 22, 21.6, 0.16, 0.026)
          73 +(112, 0, True, 19, 19.5, 0.09, 0.052)
          74 +(113, 0, True, 20, 26.6, 0.05, 0.017)
          75 +(114, 0, True, 15, 16.3, 0.05, 0.012)
          76 +(115, 1, True, 31, 43.5, 0.14, 0.024)
          77 +(116, 0, True, 19, 26.9, 0.1, 0.029)
          78 +(117, 0, True, 15, 24.4, 0.05, 0.017)
          79 +(118, 1, True, 32, 46.1, 0.2, 0.072)
          80 +(119, 1, True, 40, 58.8, 0.26, 0.088)
          81 +(120, 0, True, 17, 21.5, 0.09, 0.034)
          82 +(121, 0, True, 18, 23.9, 0.09, 0.025)
          83 +(122, 2, True, 55, 60.1, 0.28, 0.041)
          84 +(123, 0, True, 18, 20.0, 0.07, 0.018)
          85 +(124, 2, True, 30, 30.7, 0.16, 0.022)
          86 +(125, 1, True, 44, 46.9, 0.19, 0.035)
          87 +(126, 0, True, 18, 19.6, 0.07, 0.024)
          88 +(127, 1, True, 16, 12.3, 0.07, 0.03)
          89 +(128, 2, True, 55, 47.0, 0.35, 0.036)
          90 +(129, 1, True, 28, 22.2, 0.18, 0.03)
          91 +(130, 2, True, 47, 46.0, 0.97, 0.701)
          92 +(131, 1, True, 41, 34.3, 0.17, 0.041)
          93 +(132, 2, True, 42, 30.4, 0.26, 0.038)
          94 +(133, 1, True, 32, 18.4, 0.16, 0.025)
          95 +(134, 2, True, 47, 48.7, 0.2, 0.023)
          96 +(135, 1, True, 31, 28.4, 0.19, 0.039)
          97 +(136, 2, True, 31, 32.6, 0.16, 0.044)
          98 +(137, 1, True, 30, 29.9, 0.17, 0.03)
          99 +(138, 1, True, 32, 33.3, 0.12, 0.033)
         100 +(139, 1, True, 33, 32.1, 0.13, 0.019)
         101 +(140, 1, True, 31, 36.2, 0.13, 0.021)
         102 +(141, 1, True, 29, 26.5, 0.15, 0.019)
         103 +(142, 0, True, 26, 35.6, 0.09, 0.026)
         104 +(143, 2, True, 51, 56.1, 0.31, 0.03)
         105 +(144, 0, True, 19, 23.3, 0.09, 0.031)
         106 +(145, 1, True, 25, 27.0, 0.11, 0.036)
         107 +(146, 2, True, 27, 36.5, 0.11, 0.019)
         108 +(147, 0, True, 15, 12.3, 0.05, 0.01)
         109 +(148, 0, True, 17, 17.8, 0.07, 0.028)
         110 +(149, 0, True, 17, 18.6, 0.07, 0.029)
         111 +(150, 1, True, 22, 23.0, 0.1, 0.035)
         112 +(151, 2, True, 37, 35.3, 0.14, 0.025)
         113 +(152, 2, True, 38, 33.1, 0.22, 0.044)
         114 +(153, 2, True, 44, 32.9, 0.2, 0.023)
         115 +(154, 0, True, 12, 9.7, 0.06, 0.022)
         116 +(155, 0, True, 18, 19.2, 0.08, 0.033)
         117 +(156, 2, True, 53, 21.3, 0.21, 0.028)
         118 +(157, 0, True, 19, 11.2, 0.08, 0.031)
         119 +(158, 1, True, 27, 8.2, 0.15, 0.033)
         120 +(159, 2, True, 40, 9.1, 0.21, 0.04)
         121 +success 120 / 120 mean steps 31.033333333333335
diff --git a/res_t8.txt b/res_t8.txt
index ed27f32..8b6414c 100644
--- a/res_t8.txt
+++ b/res_t8.txt
@@ -1,25 +1,33 @@
    1        -(0, 8, True, 107, 52.8, 1.03, 0.078)
    2        -(1, 8, True, 152, 85.7, 1.61, 0.072)
    3        -(2, 8, True, 79, 57.6, 1.4, 0.646)
    4        -(3, 8, True, 89, 51.9, 0.84, 0.085)
    5        -(4, 8, True, 197, 126.5, 2.47, 0.642)
    6        -(5, 8, True, 127, 66.6, 1.3, 0.117)
    7        -(6, 8, True, 720, 243.6, 5.7, 0.125)
    8        -(7, 8, True, 161, 92.0, 1.6, 0.098)
    9        -(8, 8, True, 121, 72.7, 1.05, 0.102)
   10        -(9, 8, True, 99, 53.2, 1.01, 0.11)
   11        -(10, 8, True, 98, 55.1, 1.0, 0.111)
   12        -(11, 8, True, 98, 67.6, 0.88, 0.102)
   13        -(12, 8, True, 162, 106.9, 1.58, 0.113)
   14        -(13, 8, True, 334, 138.1, 2.76, 0.1)
   15        -(14, 8, True, 60, 35.4, 0.59, 0.095)
   16        -(15, 8, True, 167, 95.0, 2.12, 0.556)
   17        -(16, 8, True, 77, 43.8, 0.7, 0.105)
   18        -(17, 8, True, 86, 48.3, 0.79, 0.054)
   19        -(18, 8, True, 141, 77.4, 1.63, 0.097)
   20        -(19, 8, True, 640, 110.2, 4.77, 0.333)
   21        -(20, 8, True, 101, 55.3, 1.01, 0.071)
   22        -(21, 8, True, 138, 62.3, 1.9, 0.647)
   23        -(22, 8, True, 91, 40.8, 0.7, 0.069)
   24        -(23, 8, True, 111, 21.8, 0.85, 0.119)
   25        -success 24 / 24 mean steps 173.16666666666666
           1 +(0, 8, True, 101, 63.4, 0.84, 0.068)
           2 +(1, 8, True, 130, 106.1, 1.17, 0.089)
           3 +(2, 8, True, 75, 53.5, 1.32, 0.556)
           4 +(3, 8, True, 75, 46.8, 0.87, 0.141)
           5 +(4, 8, True, 187, 137.4, 2.63, 0.839)
           6 +(5, 8, True, 125, 82.3, 1.24, 0.099)
           7 +(6, 8, True, 711, 276.9, 4.89, 0.151)
           8 +(7, 8, True, 147, 122.6, 1.4, 0.195)
           9 +(8, 8, True, 118, 82.1, 1.02, 0.071)
          10 +(9, 8, True, 95, 60.0, 0.81, 0.143)
          11 +(10, 8, True, 98, 62.4, 0.89, 0.092)
          12 +(11, 8, True, 104, 74.3, 0.79, 0.102)
          13 +(12, 8, True, 125, 84.4, 1.03, 0.082)
          14 +(13, 8, True, 324, 145.6, 2.29, 0.131)
          15 +(14, 8, True, 58, 31.4, 0.46, 0.07)
          16 +(15, 8, True, 181, 108.7, 1.58, 0.496)
          17 +(16, 8, True, 74, 46.4, 0.53, 0.067)
          18 +(17, 8, True, 77, 45.3, 0.69, 0.063)
          19 +(18, 8, True, 136, 77.6, 1.03, 0.062)
          20 +(19, 8, True, 605, 177.1, 4.38, 0.164)
          21 +(20, 8, True, 97, 51.5, 0.76, 0.134)
          22 +(21, 8, True, 118, 74.9, 1.43, 0.714)
          23 +(22, 8, True, 82, 39.7, 0.62, 0.051)
          24 +(23, 8, True, 107, 75.2, 0.73, 0.1)
          25 +(24, 8, True, 85, 47.2, 0.62, 0.057)
          26 +(25, 8, True, 81, 52.6, 0.5, 0.073)
          27 +(26, 8, True, 70, 40.2, 0.81, 0.434)
          28 +(27, 8, True, 75, 43.4, 0.43, 0.051)
          29 +(28, 8, True, 151, 65.7, 1.05, 0.092)
          30 +(29, 8, True, 68, 36.4, 0.63, 0.096)
          31 +(30, 8, True, 67, 32.5, 0.55, 0.084)
          32 +(31, 8, True, 101, 34.8, 0.96, 0.063)
          33 +success 32 / 32 mean steps 145.25
```

</details>

<a id="C017"></a>
### C017 · STEP_LOW 0.08

Commit `fcd604e4f08903d1d450791c54030f1396064e78`; parents: b3f709da810d2c27bf68b431808fbbfbfa8b64cf. Recorded author date: 2026-10-01T00:05:10+02:00.

File roles (automatic): policy, setup/other.

- [E1245](01_timeline.md#E1245): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_fcd604e_approach.py) · [Exact all-file diff](evidence/diffs/C017_fcd604e.diff)

[Previous saved controller snapshot](evidence/versions/C016_b3f709d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d876a4e..3b4ba34 100644
--- a/approach.py
+++ b/approach.py
@@ -120,7 +120,7 @@ def wrap(a):
  120    120  # ----------------------------------------------------------------------------- approach
  121    121  TABLE_TOP = 0.075
  122    122  STEP_FAST = 0.12
  123        -STEP_LOW = 0.05
         123 +STEP_LOW = 0.08
  124    124  SAFE_FLOOR = 0.2
  125    125  BASE_ASSIST = True
  126    126  STEP_TRAVEL = 0.25
diff --git a/res_t.txt b/res_t.txt
index acabd4d..e7c0295 100644
--- a/res_t.txt
+++ b/res_t.txt
@@ -1,41 +1,41 @@
    1        -(0, 2, True, 42, 31.8, 0.43, 0.089)
    2        -(1, 1, True, 36, 26.3, 0.18, 0.04)
    3        -(2, 2, True, 59, 59.1, 0.34, 0.052)
    4        -(3, 2, True, 35, 27.4, 0.29, 0.068)
    5        -(4, 2, True, 44, 39.5, 0.37, 0.051)
    6        -(5, 2, True, 56, 48.3, 0.51, 0.072)
    7        -(6, 1, True, 34, 18.0, 0.29, 0.069)
    8        -(7, 2, True, 45, 37.4, 0.33, 0.066)
    9        -(8, 2, True, 43, 52.1, 0.25, 0.032)
   10        -(9, 1, True, 27, 23.3, 0.19, 0.046)
   11        -(10, 2, True, 34, 36.5, 0.24, 0.051)
   12        -(11, 0, True, 19, 19.5, 0.08, 0.02)
   13        -(12, 1, True, 38, 38.7, 0.21, 0.049)
   14        -(13, 2, True, 55, 57.8, 0.27, 0.045)
   15        -(14, 0, True, 12, 12.9, 0.06, 0.014)
   16        -(15, 2, True, 38, 37.2, 0.17, 0.027)
   17        -(16, 1, True, 28, 22.2, 0.23, 0.045)
   18        -(17, 2, True, 45, 39.9, 0.3, 0.053)
   19        -(18, 2, True, 29, 25.7, 0.17, 0.051)
   20        -(19, 1, True, 42, 39.9, 0.29, 0.04)
   21        -(20, 2, True, 52, 54.1, 0.26, 0.039)
   22        -(21, 0, True, 25, 22.3, 0.14, 0.063)
   23        -(22, 2, True, 29, 24.9, 0.14, 0.024)
   24        -(23, 0, True, 26, 29.2, 0.09, 0.035)
   25        -(24, 1, True, 20, 21.1, 0.08, 0.021)
   26        -(25, 1, True, 43, 49.5, 0.16, 0.035)
   27        -(26, 2, True, 33, 36.0, 0.14, 0.03)
   28        -(27, 0, True, 26, 23.8, 0.09, 0.023)
   29        -(28, 1, True, 42, 40.9, 0.18, 0.032)
   30        -(29, 2, True, 18, 19.3, 0.08, 0.023)
   31        -(30, 0, True, 26, 23.7, 0.07, 0.021)
   32        -(31, 1, True, 44, 39.2, 0.16, 0.018)
   33        -(32, 2, True, 37, 35.2, 0.18, 0.024)
   34        -(33, 2, True, 42, 30.8, 0.27, 0.048)
   35        -(34, 0, True, 16, 16.7, 0.04, 0.015)
   36        -(35, 0, True, 17, 19.1, 0.06, 0.022)
   37        -(36, 1, True, 25, 16.9, 0.12, 0.022)
   38        -(37, 0, True, 20, 11.3, 0.07, 0.023)
   39        -(38, 0, True, 17, 7.1, 0.07, 0.024)
   40        -(39, 2, True, 54, 7.0, 0.28, 0.032)
   41        -success 40 / 40 mean steps 34.325
           1 +(0, 2, True, 39, 28.7, 0.23, 0.037)
           2 +(1, 1, True, 35, 23.6, 0.21, 0.05)
           3 +(2, 2, True, 58, 49.5, 0.34, 0.038)
           4 +(3, 2, True, 35, 30.5, 0.2, 0.041)
           5 +(4, 2, True, 44, 33.8, 0.29, 0.055)
           6 +(5, 2, True, 53, 48.0, 0.27, 0.04)
           7 +(6, 1, True, 33, 20.6, 0.13, 0.026)
           8 +(7, 2, True, 45, 34.5, 0.23, 0.054)
           9 +(8, 2, True, 42, 48.3, 0.24, 0.045)
          10 +(9, 1, True, 25, 24.4, 0.14, 0.034)
          11 +(10, 2, True, 32, 35.1, 0.12, 0.019)
          12 +(11, 0, True, 19, 16.0, 0.09, 0.028)
          13 +(12, 1, True, 37, 38.6, 0.17, 0.035)
          14 +(13, 2, True, 57, 53.7, 0.29, 0.051)
          15 +(14, 0, True, 12, 9.2, 0.08, 0.04)
          16 +(15, 2, True, 38, 35.9, 0.18, 0.041)
          17 +(16, 1, True, 27, 24.1, 0.15, 0.031)
          18 +(17, 2, True, 44, 38.5, 0.28, 0.056)
          19 +(18, 2, True, 28, 22.0, 0.13, 0.032)
          20 +(19, 1, True, 41, 33.3, 0.25, 0.037)
          21 +(20, 2, True, 49, 52.8, 0.2, 0.019)
          22 +(21, 0, True, 25, 22.7, 0.11, 0.021)
          23 +(22, 2, True, 28, 29.7, 0.14, 0.03)
          24 +(23, 0, True, 26, 26.8, 0.09, 0.039)
          25 +(24, 1, True, 20, 23.7, 0.05, 0.018)
          26 +(25, 1, True, 41, 45.6, 0.19, 0.029)
          27 +(26, 2, True, 31, 34.5, 0.14, 0.026)
          28 +(27, 0, True, 26, 22.9, 0.09, 0.039)
          29 +(28, 1, True, 41, 37.8, 0.16, 0.027)
          30 +(29, 2, True, 18, 18.7, 0.08, 0.037)
          31 +(30, 0, True, 26, 23.8, 0.07, 0.025)
          32 +(31, 1, True, 44, 39.8, 0.16, 0.022)
          33 +(32, 2, True, 36, 35.0, 0.18, 0.046)
          34 +(33, 2, True, 41, 33.7, 0.23, 0.031)
          35 +(34, 0, True, 16, 12.6, 0.05, 0.015)
          36 +(35, 0, True, 17, 19.0, 0.05, 0.016)
          37 +(36, 1, True, 25, 14.6, 0.09, 0.017)
          38 +(37, 0, True, 20, 9.7, 0.08, 0.028)
          39 +(38, 0, True, 17, 5.0, 0.06, 0.017)
          40 +(39, 2, True, 53, 7.4, 0.18, 0.03)
          41 +success 40 / 40 mean steps 33.6
diff --git a/res_t5.txt b/res_t5.txt
new file mode 100644
index 0000000..3da3f13
--- /dev/null
+++ b/res_t5.txt
@@ -0,0 +1,25 @@
           1 +(0, 5, True, 67, 57.1, 0.84, 0.21)
           2 +(1, 5, True, 77, 67.6, 0.62, 0.057)
           3 +(2, 5, True, 70, 61.3, 1.23, 0.529)
           4 +(3, 5, True, 45, 40.6, 0.38, 0.051)
           5 +(4, 5, True, 93, 74.5, 0.7, 0.088)
           6 +(5, 5, True, 102, 73.8, 0.85, 0.088)
           7 +(6, 5, True, 97, 71.0, 0.67, 0.088)
           8 +(7, 5, True, 100, 84.4, 0.79, 0.091)
           9 +(8, 5, True, 91, 72.8, 0.65, 0.068)
          10 +(9, 5, True, 88, 73.7, 0.73, 0.069)
          11 +(10, 5, True, 76, 59.5, 0.49, 0.066)
          12 +(11, 5, True, 96, 77.2, 0.72, 0.053)
          13 +(12, 5, True, 125, 101.4, 0.96, 0.092)
          14 +(13, 5, True, 116, 84.6, 0.73, 0.07)
          15 +(14, 5, True, 36, 18.6, 0.28, 0.073)
          16 +(15, 5, True, 98, 76.9, 1.25, 0.711)
          17 +(16, 5, True, 43, 27.9, 0.28, 0.05)
          18 +(17, 5, True, 66, 45.4, 0.46, 0.07)
          19 +(18, 5, True, 55, 34.6, 0.41, 0.066)
          20 +(19, 5, True, 611, 77.6, 3.16, 0.062)
          21 +(20, 5, True, 92, 43.5, 0.56, 0.048)
          22 +(21, 5, True, 75, 39.4, 0.6, 0.074)
          23 +(22, 5, True, 52, 23.4, 0.46, 0.07)
          24 +(23, 5, True, 106, 26.1, 0.77, 0.062)
          25 +success 24 / 24 mean steps 103.20833333333333
```

</details>

<a id="C018"></a>
### C018 · Travel via joint+base interpolation with base-translation/rotation candidates (mean 25.9 steps)

Commit `f688947d6612fcbcbfed60b1073b8a5c707bad98`; parents: fcd604e4f08903d1d450791c54030f1396064e78. Recorded author date: 2026-10-01T00:15:27+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E1329](01_timeline.md#E1329): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_f688947_approach.py) · [Exact all-file diff](evidence/diffs/C018_f688947.diff)

[Previous saved controller snapshot](evidence/versions/C017_fcd604e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3b4ba34..1604ae1 100644
--- a/approach.py
+++ b/approach.py
@@ -126,6 +126,10 @@ BASE_ASSIST = True
  126    126  STEP_TRAVEL = 0.25
  127    127  ASSIST_MINX = 0.2
  128    128  JOINT_TRAVEL = True
         129 +ROT_ASSIST = True
         130 +ROT_MAX = 0.8
         131 +BASE_TRAVEL = True
         132 +BASE_XMAX = -0.08
  129    133  SAFE_CLR = 0.02
  130    134  MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
  131    135  TABLE_X = (0.10, 0.50)
@@ -563,13 +567,17 @@ class GeneratedApproach:
  563    567                  if rejected:
  564    568                      self.jplan = False
  565    569                  else:
  566        -                    dq = self.jplan - q
  567        -                    m = np.max(np.abs(dq))
         570 +                    qg, bg = self.jplan
         571 +                    dq = qg - q
         572 +                    dq[0] = wrap(dq[0])
         573 +                    dbs = bg - base
         574 +                    dbs[2] = wrap(dbs[2])
         575 +                    m = max(np.max(np.abs(dq)), np.max(np.abs(dbs)))
  568    576                      if m > 1e-4:
  569    577                          lim = 0.2 * max(self.scale, 0.05)
  570        -                        if m > lim:
  571        -                            dq *= lim / m
  572        -                        act[3:10] = dq.astype(np.float32)
         578 +                        n = max(1.0, np.ceil(m / lim - 1e-9))
         579 +                        act[0:3] = (dbs / n).astype(np.float32)
         580 +                        act[3:10] = (dq / n).astype(np.float32)
  573    581                          self.last_cmd = True
  574    582                          return act
  575    583                      self.jplan = False
@@ -686,25 +694,63 @@ class GeneratedApproach:
  686    694          if held is not None:
  687    695              b = boxes[held]
  688    696              hb = max(0.0, (Tw[2, 3] - FINGER) - (b["z"] - b["hz"]))
         697 +        # pose that must also be reachable afterwards (next descend)
         698 +        nxt = None
         699 +        if self.segs and self.segs[0][0] == "move":
         700 +            nxt = self.segs[0][1]
         701 +        p = Tw[:3, 3]
         702 +        dxy = goal[:2] - p[:2]
         703 +        cands = [base.copy()]
         704 +        if BASE_TRAVEL:
         705 +            for fx, fy in ((1.0, 1.0), (0.0, 1.0), (0.5, 0.5), (0.0, 0.5)):
         706 +                bb = base.copy()
         707 +                bb[0] = min(base[0] + fx * dxy[0], max(base[0], BASE_XMAX))
         708 +                bb[1] = base[1] + fy * dxy[1]
         709 +                cands.append(bb)
         710 +        if ROT_ASSIST:
         711 +            Mw = self._mount(base)[:3, 3]
         712 +            a0 = np.arctan2(p[1] - Mw[1], p[0] - Mw[0])
         713 +            a1 = np.arctan2(goal[1] - Mw[1], goal[0] - Mw[0])
         714 +            th2 = float(np.clip(base[2] + wrap(a1 - a0), -ROT_MAX, ROT_MAX))
         715 +            bb = np.array([Mw[0] - MOUNT_OFF * np.cos(th2), Mw[1] - MOUNT_OFF * np.sin(th2), th2])
         716 +            if bb[0] <= max(base[0], BASE_XMAX):
         717 +                cands.append(bb)
  689    718          best = None
  690        -        for sd in (q, self.q_nom, self.q_home):
  691        -            qg, err = self._ik_world(sd, goal, Rt, base, iters=150)
  692        -            if err > 1e-4:
         719 +        for bb in cands:
         720 +            costb = max(abs(bb[0] - base[0]), abs(bb[1] - base[1]), abs(wrap(bb[2] - base[2])))
         721 +            if best is not None and costb >= best[0]:
  693    722                  continue
  694        -            dqm = np.max(np.abs(qg - q))
  695        -            if best is None or dqm < best[0]:
  696        -                best = (dqm, qg)
         723 +            for sd in (q, self.q_nom):
         724 +                qg, err = self._ik_world(sd, goal, Rt, bb, iters=150)
         725 +                if err > 1e-4:
         726 +                    continue
         727 +                dq = qg - q
         728 +                dq[0] = wrap(dq[0])
         729 +                c = max(np.max(np.abs(dq)), costb)
         730 +                if best is not None and c >= best[0] - 1e-3:
         731 +                    continue
         732 +                if nxt is not None:
         733 +                    qn, en = self._ik_world(qg, nxt, Rt, bb, iters=100)
         734 +                    if en > 1e-4:
         735 +                        continue
         736 +                if not self._path_ok(q, base, q + dq, bb, boxes, held, hb):
         737 +                    continue
         738 +                best = (c, q + dq, bb)
  697    739          if best is None:
  698    740              return False
  699        -        qg = best[1]
         741 +        return (best[1], best[2])
         742 +
         743 +    def _path_ok(self, q, base, qg, bg, boxes, held, hb):
         744 +        db = bg - base
         745 +        db[2] = wrap(db[2])
  700    746          for sv in np.linspace(0.0, 1.0, 13)[1:-1]:
  701    747              qs = q + sv * (qg - q)
  702        -            T = self._ee_world(qs, base)
         748 +            T = self._ee_world(qs, base + sv * db)
  703    749              if T[2, 2] > -0.9:
  704    750                  return False
  705    751              if T[2, 3] < self._req_z(boxes, T[:2, 3], held, hb) - 0.005:
  706    752                  return False
  707        -        return qg
         753 +        return True
  708    754  
  709    755      def _handle_reject(self, state):
  710    756          seg = self.cur
diff --git a/dbg_steps.py b/dbg_steps.py
new file mode 100644
index 0000000..db08fe1
--- /dev/null
+++ b/dbg_steps.py
@@ -0,0 +1,13 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seed=int(sys.argv[1]); t0=int(sys.argv[2]); t1=int(sys.argv[3]); OC=int(sys.argv[4]) if len(sys.argv)>4 else None
           5 +env = make_env(); obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None))
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +for t in range(t1):
           8 +    a = ap.get_action(obs)
           9 +    obs, r, term, trunc, info = env.step(a)
          10 +    if t>=t0:
          11 +        q=ap._q(obs); b=ap._base(obs); T=ap._ee_world(q,b)
          12 +        print(t, ap.cur[0], ap.cur[3] if ap.cur[0]=="move" else "", "jp", None if ap.jplan is None else (ap.jplan is not False), "a", np.round(a,3), "base", np.round(b,3), "ee", np.round(T[:3,3],3))
          13 +    if term: break
diff --git a/probe_rot.py b/probe_rot.py
new file mode 100644
index 0000000..f6efc6c
--- /dev/null
+++ b/probe_rot.py
@@ -0,0 +1,14 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env(); obs, info = env.reset(seed=2)
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           6 +def show(tag):
           7 +    q=ap._q(obs); b=ap._base(obs); T=ap._ee_world(q,b)
           8 +    print(tag, "base", np.round(b,4), "ee", np.round(T[:3,3],4), "q0", round(q[0],4))
           9 +show("init")
          10 +for a3 in ([0,0,0.1],[0,0,0.2],[0.0,0.05,0],[0.0,0,-0.3]):
          11 +    a=np.zeros(11,dtype=np.float32); a[0:3]=a3
          12 +    obs,*_=env.step(a); show(str(a3))
          13 +a=np.zeros(11,dtype=np.float32); a[0:3]=[0.012,-0.02,0.15]; a[3]=0.1
          14 +obs,*_=env.step(a); show("combo")
diff --git a/res_t.txt b/res_t.txt
index e7c0295..cad5540 100644
--- a/res_t.txt
+++ b/res_t.txt
@@ -1,41 +1,41 @@
    1        -(0, 2, True, 39, 28.7, 0.23, 0.037)
    2        -(1, 1, True, 35, 23.6, 0.21, 0.05)
    3        -(2, 2, True, 58, 49.5, 0.34, 0.038)
    4        -(3, 2, True, 35, 30.5, 0.2, 0.041)
    5        -(4, 2, True, 44, 33.8, 0.29, 0.055)
    6        -(5, 2, True, 53, 48.0, 0.27, 0.04)
    7        -(6, 1, True, 33, 20.6, 0.13, 0.026)
    8        -(7, 2, True, 45, 34.5, 0.23, 0.054)
    9        -(8, 2, True, 42, 48.3, 0.24, 0.045)
   10        -(9, 1, True, 25, 24.4, 0.14, 0.034)
   11        -(10, 2, True, 32, 35.1, 0.12, 0.019)
   12        -(11, 0, True, 19, 16.0, 0.09, 0.028)
   13        -(12, 1, True, 37, 38.6, 0.17, 0.035)
   14        -(13, 2, True, 57, 53.7, 0.29, 0.051)
   15        -(14, 0, True, 12, 9.2, 0.08, 0.04)
   16        -(15, 2, True, 38, 35.9, 0.18, 0.041)
   17        -(16, 1, True, 27, 24.1, 0.15, 0.031)
   18        -(17, 2, True, 44, 38.5, 0.28, 0.056)
   19        -(18, 2, True, 28, 22.0, 0.13, 0.032)
   20        -(19, 1, True, 41, 33.3, 0.25, 0.037)
   21        -(20, 2, True, 49, 52.8, 0.2, 0.019)
   22        -(21, 0, True, 25, 22.7, 0.11, 0.021)
   23        -(22, 2, True, 28, 29.7, 0.14, 0.03)
   24        -(23, 0, True, 26, 26.8, 0.09, 0.039)
   25        -(24, 1, True, 20, 23.7, 0.05, 0.018)
   26        -(25, 1, True, 41, 45.6, 0.19, 0.029)
   27        -(26, 2, True, 31, 34.5, 0.14, 0.026)
   28        -(27, 0, True, 26, 22.9, 0.09, 0.039)
   29        -(28, 1, True, 41, 37.8, 0.16, 0.027)
   30        -(29, 2, True, 18, 18.7, 0.08, 0.037)
   31        -(30, 0, True, 26, 23.8, 0.07, 0.025)
   32        -(31, 1, True, 44, 39.8, 0.16, 0.022)
   33        -(32, 2, True, 36, 35.0, 0.18, 0.046)
   34        -(33, 2, True, 41, 33.7, 0.23, 0.031)
   35        -(34, 0, True, 16, 12.6, 0.05, 0.015)
   36        -(35, 0, True, 17, 19.0, 0.05, 0.016)
   37        -(36, 1, True, 25, 14.6, 0.09, 0.017)
   38        -(37, 0, True, 20, 9.7, 0.08, 0.028)
   39        -(38, 0, True, 17, 5.0, 0.06, 0.017)
   40        -(39, 2, True, 53, 7.4, 0.18, 0.03)
   41        -success 40 / 40 mean steps 33.6
           1 +(0, 2, True, 30, 37.4, 4.43, 3.152)
           2 +(1, 1, True, 24, 22.6, 6.66, 5.921)
           3 +(2, 2, True, 36, 34.7, 2.18, 0.83)
           4 +(3, 2, True, 25, 16.8, 1.92, 0.627)
           5 +(4, 2, True, 33, 18.6, 2.14, 0.509)
           6 +(5, 2, True, 41, 40.9, 2.05, 0.633)
           7 +(6, 1, True, 25, 30.0, 4.5, 3.882)
           8 +(7, 2, True, 33, 36.0, 2.85, 2.06)
           9 +(8, 2, True, 30, 43.3, 0.75, 0.169)
          10 +(9, 1, True, 20, 25.5, 0.34, 0.12)
          11 +(10, 2, True, 23, 35.0, 0.51, 0.18)
          12 +(11, 0, True, 14, 20.4, 0.21, 0.106)
          13 +(12, 1, True, 29, 36.1, 0.62, 0.176)
          14 +(13, 2, True, 45, 52.0, 0.92, 0.154)
          15 +(14, 0, True, 12, 12.9, 0.29, 0.183)
          16 +(15, 2, True, 32, 36.7, 0.46, 0.161)
          17 +(16, 1, True, 21, 16.4, 0.48, 0.124)
          18 +(17, 2, True, 37, 43.3, 0.71, 0.229)
          19 +(18, 2, True, 25, 22.1, 0.47, 0.106)
          20 +(19, 1, True, 31, 34.2, 0.66, 0.366)
          21 +(20, 2, True, 34, 39.7, 0.58, 0.161)
          22 +(21, 0, True, 15, 15.9, 0.31, 0.156)
          23 +(22, 2, True, 22, 29.8, 0.43, 0.109)
          24 +(23, 0, True, 19, 34.7, 0.41, 0.237)
          25 +(24, 1, True, 14, 24.3, 0.17, 0.11)
          26 +(25, 1, True, 28, 37.3, 0.46, 0.172)
          27 +(26, 2, True, 23, 31.7, 0.38, 0.087)
          28 +(27, 0, True, 27, 40.0, 0.43, 0.245)
          29 +(28, 1, True, 53, 55.6, 1.46, 0.222)
          30 +(29, 2, True, 14, 16.9, 0.22, 0.145)
          31 +(30, 0, True, 18, 21.7, 0.27, 0.105)
          32 +(31, 1, True, 30, 34.2, 0.52, 0.174)
          33 +(32, 2, True, 30, 35.1, 0.54, 0.067)
          34 +(33, 2, True, 30, 32.9, 0.7, 0.13)
          35 +(34, 0, True, 13, 16.6, 0.13, 0.04)
          36 +(35, 0, True, 13, 16.7, 0.26, 0.169)
          37 +(36, 1, True, 20, 16.9, 0.5, 0.181)
          38 +(37, 0, True, 13, 10.8, 0.18, 0.127)
          39 +(38, 0, True, 14, 6.4, 0.32, 0.172)
          40 +(39, 2, True, 39, 6.7, 0.47, 0.055)
          41 +success 40 / 40 mean steps 25.875
diff --git a/tally.py b/tally.py
new file mode 100644
index 0000000..a1cad40
--- /dev/null
+++ b/tally.py
@@ -0,0 +1,16 @@
           1 +import sys, numpy as np, collections
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +cnt=collections.Counter(); env=make_env(); tot=0
           5 +for seed in range(int(sys.argv[1]), int(sys.argv[2])):
           6 +    obs, info = env.reset(seed=seed)
           7 +    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +    for t in range(1000):
           9 +        a = ap.get_action(obs)
          10 +        c = ap.cur
          11 +        tag = "grip" if c is None else (c[0] if c[0]!="move" else c[3])
          12 +        if tag=="travel": tag += "-J" if (ap.jplan is not None and ap.jplan is not False) else "-C"
          13 +        cnt[tag]+=1; tot+=1
          14 +        obs, r, term, trunc, info = env.step(a)
          15 +        if term: break
          16 +print(tot, cnt.most_common())
```

</details>

<a id="C019"></a>
### C019 · Faster FK/IK (vectorized Jacobian, early exit)

Commit `c698440abedb1466f13e7f754231a1c261042e8c`; parents: f688947d6612fcbcbfed60b1073b8a5c707bad98. Recorded author date: 2026-10-01T00:19:00+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E1362](01_timeline.md#E1362): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_c698440_approach.py) · [Exact all-file diff](evidence/diffs/C019_c698440.diff)

[Previous saved controller snapshot](evidence/versions/C018_f688947_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1604ae1..07e62d5 100644
--- a/approach.py
+++ b/approach.py
@@ -40,14 +40,16 @@ _LIM = [None, (-2.38, 2.38), None, (-2.63, 2.63), None, (-2.2, 2.2), None]
   40     40  
   41     41  def fk(q):
   42     42      T = np.eye(4)
   43        -    zs, ps = [], []
          43 +    zs = np.empty((7, 3))
          44 +    ps = np.empty((7, 3))
   44     45      for i in range(7):
   45     46          T = T @ _JOINTS[i]
   46        -        zs.append(T[:3, 2].copy())
   47        -        ps.append(T[:3, 3].copy())
          47 +        zs[i] = T[:3, 2]
          48 +        ps[i] = T[:3, 3]
   48     49          c, s = np.cos(q[i]), np.sin(q[i])
   49        -        Rz = np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1.0]])
   50        -        T = T @ Rz
          50 +        c0 = T[:, 0].copy()
          51 +        T[:, 0] = c * c0 + s * T[:, 1]
          52 +        T[:, 1] = -s * c0 + c * T[:, 1]
   51     53      T = T @ _EE
   52     54      return T, zs, ps
   53     55  
@@ -88,6 +90,8 @@ def _rotvec(Rm):
   88     90  def ik(q0, pos, Rt, iters=100, tol=1e-5):
   89     91      q = np.array(q0, dtype=float)
   90     92      err = 1e9
          93 +    best = 1e9
          94 +    since = 0
   91     95      for _ in range(iters):
   92     96          T, zs, ps = fk(q)
   93     97          ep = pos - T[:3, 3]
@@ -96,11 +100,19 @@ def ik(q0, pos, Rt, iters=100, tol=1e-5):
   96    100          err = np.linalg.norm(e)
   97    101          if err < tol:
   98    102              break
   99        -        J = np.zeros((6, 7))
  100        -        pe = T[:3, 3]
  101        -        for i in range(7):
  102        -            J[:3, i] = np.cross(zs[i], pe - ps[i])
  103        -            J[3:, i] = 0.3 * zs[i]
         103 +        if err < best - 1e-4:
         104 +            best = err
         105 +            since = 0
         106 +        else:
         107 +            since += 1
         108 +            if since > 12 and err > 1e-3:
         109 +                break
         110 +        J = np.empty((6, 7))
         111 +        D = T[:3, 3] - ps
         112 +        J[0] = zs[:, 1] * D[:, 2] - zs[:, 2] * D[:, 1]
         113 +        J[1] = zs[:, 2] * D[:, 0] - zs[:, 0] * D[:, 2]
         114 +        J[2] = zs[:, 0] * D[:, 1] - zs[:, 1] * D[:, 0]
         115 +        J[3:] = 0.3 * zs.T
  104    116          lam = 1e-4
  105    117          dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
  106    118          n = np.max(np.abs(dq))
diff --git a/p.out b/p.out
new file mode 100644
index 0000000..0497369
Binary files /dev/null and b/p.out differ
diff --git a/prof1.py b/prof1.py
new file mode 100644
index 0000000..6240e93
--- /dev/null
+++ b/prof1.py
@@ -0,0 +1,11 @@
           1 +import sys, time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seed=int(sys.argv[1]); OC=int(sys.argv[2]) if len(sys.argv)>2 else None
           5 +env = make_env(); obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None))
           6 +t=time.time(); ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info); print("reset", round(time.time()-t,3))
           7 +for k in range(1000):
           8 +    t=time.time(); a = ap.get_action(obs); dt=time.time()-t
           9 +    if dt>0.2: print(k, round(dt,3), ap.cur[0] if ap.cur else None, ap.cur[3] if ap.cur and ap.cur[0]=="move" else "")
          10 +    obs, r, term, trunc, info = env.step(a)
          11 +    if term: print("done", k); break
diff --git a/prof2.py b/prof2.py
new file mode 100644
index 0000000..d6e054a
--- /dev/null
+++ b/prof2.py
@@ -0,0 +1,10 @@
           1 +import sys, cProfile, pstats, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seed=int(sys.argv[1]); K=int(sys.argv[2])
           5 +env = make_env(); obs, info = env.reset(seed=seed)
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +for k in range(K):
           8 +    a = ap.get_action(obs); obs, *_ = env.step(a)
           9 +cProfile.run("ap.get_action(obs)", "p.out")
          10 +pstats.Stats("p.out").sort_stats("cumtime").print_stats(12)
diff --git a/res_t.txt b/res_t.txt
index cad5540..c9dfcc8 100644
--- a/res_t.txt
+++ b/res_t.txt
@@ -1,41 +1,41 @@
    1        -(0, 2, True, 30, 37.4, 4.43, 3.152)
    2        -(1, 1, True, 24, 22.6, 6.66, 5.921)
    3        -(2, 2, True, 36, 34.7, 2.18, 0.83)
    4        -(3, 2, True, 25, 16.8, 1.92, 0.627)
    5        -(4, 2, True, 33, 18.6, 2.14, 0.509)
    6        -(5, 2, True, 41, 40.9, 2.05, 0.633)
    7        -(6, 1, True, 25, 30.0, 4.5, 3.882)
    8        -(7, 2, True, 33, 36.0, 2.85, 2.06)
    9        -(8, 2, True, 30, 43.3, 0.75, 0.169)
   10        -(9, 1, True, 20, 25.5, 0.34, 0.12)
   11        -(10, 2, True, 23, 35.0, 0.51, 0.18)
   12        -(11, 0, True, 14, 20.4, 0.21, 0.106)
   13        -(12, 1, True, 29, 36.1, 0.62, 0.176)
   14        -(13, 2, True, 45, 52.0, 0.92, 0.154)
   15        -(14, 0, True, 12, 12.9, 0.29, 0.183)
   16        -(15, 2, True, 32, 36.7, 0.46, 0.161)
   17        -(16, 1, True, 21, 16.4, 0.48, 0.124)
   18        -(17, 2, True, 37, 43.3, 0.71, 0.229)
   19        -(18, 2, True, 25, 22.1, 0.47, 0.106)
   20        -(19, 1, True, 31, 34.2, 0.66, 0.366)
   21        -(20, 2, True, 34, 39.7, 0.58, 0.161)
   22        -(21, 0, True, 15, 15.9, 0.31, 0.156)
   23        -(22, 2, True, 22, 29.8, 0.43, 0.109)
   24        -(23, 0, True, 19, 34.7, 0.41, 0.237)
   25        -(24, 1, True, 14, 24.3, 0.17, 0.11)
   26        -(25, 1, True, 28, 37.3, 0.46, 0.172)
   27        -(26, 2, True, 23, 31.7, 0.38, 0.087)
   28        -(27, 0, True, 27, 40.0, 0.43, 0.245)
   29        -(28, 1, True, 53, 55.6, 1.46, 0.222)
   30        -(29, 2, True, 14, 16.9, 0.22, 0.145)
   31        -(30, 0, True, 18, 21.7, 0.27, 0.105)
   32        -(31, 1, True, 30, 34.2, 0.52, 0.174)
   33        -(32, 2, True, 30, 35.1, 0.54, 0.067)
   34        -(33, 2, True, 30, 32.9, 0.7, 0.13)
   35        -(34, 0, True, 13, 16.6, 0.13, 0.04)
   36        -(35, 0, True, 13, 16.7, 0.26, 0.169)
   37        -(36, 1, True, 20, 16.9, 0.5, 0.181)
   38        -(37, 0, True, 13, 10.8, 0.18, 0.127)
   39        -(38, 0, True, 14, 6.4, 0.32, 0.172)
   40        -(39, 2, True, 39, 6.7, 0.47, 0.055)
           1 +(0, 2, True, 30, 32.0, 0.49, 0.113)
           2 +(1, 1, True, 24, 18.2, 0.52, 0.295)
           3 +(2, 2, True, 36, 40.8, 0.6, 0.127)
           4 +(3, 2, True, 25, 19.7, 0.26, 0.049)
           5 +(4, 2, True, 33, 29.6, 0.35, 0.047)
           6 +(5, 2, True, 41, 39.7, 0.51, 0.11)
           7 +(6, 1, True, 25, 15.6, 0.34, 0.093)
           8 +(7, 2, True, 33, 35.8, 0.25, 0.058)
           9 +(8, 2, True, 30, 33.8, 0.41, 0.077)
          10 +(9, 1, True, 20, 23.0, 0.29, 0.084)
          11 +(10, 2, True, 23, 27.8, 0.28, 0.085)
          12 +(11, 0, True, 14, 13.6, 0.14, 0.06)
          13 +(12, 1, True, 29, 30.8, 0.32, 0.09)
          14 +(13, 2, True, 45, 47.6, 0.5, 0.073)
          15 +(14, 0, True, 12, 10.7, 0.11, 0.054)
          16 +(15, 2, True, 32, 33.7, 0.22, 0.055)
          17 +(16, 1, True, 21, 20.9, 0.28, 0.082)
          18 +(17, 2, True, 37, 43.8, 0.47, 0.085)
          19 +(18, 2, True, 25, 19.1, 0.27, 0.067)
          20 +(19, 1, True, 31, 28.9, 0.43, 0.205)
          21 +(20, 2, True, 34, 35.9, 0.63, 0.2)
          22 +(21, 0, True, 15, 16.4, 0.18, 0.086)
          23 +(22, 2, True, 22, 30.4, 0.25, 0.06)
          24 +(23, 0, True, 19, 33.7, 0.23, 0.146)
          25 +(24, 1, True, 14, 24.3, 0.2, 0.104)
          26 +(25, 1, True, 28, 37.5, 0.3, 0.089)
          27 +(26, 2, True, 23, 30.0, 0.2, 0.048)
          28 +(27, 0, True, 27, 38.6, 0.26, 0.158)
          29 +(28, 1, True, 53, 51.3, 0.75, 0.216)
          30 +(29, 2, True, 14, 15.4, 0.19, 0.15)
          31 +(30, 0, True, 18, 17.6, 0.12, 0.052)
          32 +(31, 1, True, 30, 34.4, 0.31, 0.069)
          33 +(32, 2, True, 30, 35.9, 0.41, 0.06)
          34 +(33, 2, True, 30, 32.6, 0.38, 0.067)
          35 +(34, 0, True, 13, 17.4, 0.24, 0.162)
          36 +(35, 0, True, 13, 16.5, 0.07, 0.02)
          37 +(36, 1, True, 20, 17.8, 0.18, 0.048)
          38 +(37, 0, True, 13, 10.5, 0.2, 0.141)
          39 +(38, 0, True, 14, 7.4, 0.15, 0.097)
          40 +(39, 2, True, 39, 5.9, 0.37, 0.052)
   41     41  success 40 / 40 mean steps 25.875
```

</details>

<a id="C020"></a>
### C020 · Lazy merge of travel+descend into one joint move

Commit `a6b25370e6861b1a62ea7bd28b71e5045f7aee10`; parents: c698440abedb1466f13e7f754231a1c261042e8c. Recorded author date: 2026-10-01T00:44:31+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E1457](01_timeline.md#E1457): commit title in command; output may not confirm creation.
- [E1459](01_timeline.md#E1459): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_a6b2537_approach.py) · [Exact all-file diff](evidence/diffs/C020_a6b2537.diff)

[Previous saved controller snapshot](evidence/versions/C019_c698440_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 07e62d5..454b01f 100644
--- a/approach.py
+++ b/approach.py
@@ -142,6 +142,7 @@ ROT_ASSIST = True
  142    142  ROT_MAX = 0.8
  143    143  BASE_TRAVEL = True
  144    144  BASE_XMAX = -0.08
         145 +MERGE = True
  145    146  SAFE_CLR = 0.02
  146    147  MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
  147    148  TABLE_X = (0.10, 0.50)
@@ -231,6 +232,7 @@ class GeneratedApproach:
  231    232          self.stall = 0
  232    233          self.q_home = self._q(state)
  233    234          self.nsteps = 0
         235 +        self.nomerge_until = 0
  234    236          self.scale = 1.0
  235    237          self.max_top = 0.15
  236    238          self.esc = 0
@@ -567,15 +569,38 @@ class GeneratedApproach:
  567    569                  break
  568    570              if self.cur is None:
  569    571                  if not self.segs:
  570        -                    self.segs = self._replan(state)
         572 +                    self.segs = self._merge(state, self._replan(state))
  571    573                  self.cur = self.segs.pop(0)
  572    574                  self.best_d = None
  573    575                  self.stall = 0
  574    576                  self.jplan = None
  575    577              seg = self.cur
         578 +            if seg[0] == "lazy":
         579 +                tr, de = seg[1], seg[2]
         580 +                r = self._jplan_to(state, de[1], tr[2], final_exempt=True)
         581 +                if r is not None:
         582 +                    self.cur = ("jmove", r[0], r[1], "m_" + de[3])
         583 +                else:
         584 +                    self.cur = tr
         585 +                    self.segs.insert(0, de)
         586 +                self.jplan = None
         587 +                self.best_d = None
         588 +                self.stall = 0
         589 +                seg = self.cur
         590 +            if seg[0] == "jmove":
         591 +                if rejected:
         592 +                    self.nomerge_until = self.nsteps + 8
         593 +                    self.segs = []
         594 +                    self.cur = None
         595 +                    continue
         596 +                if self.jplan is None:
         597 +                    self.jplan = (seg[1], seg[2])
         598 +                if self.jplan is False:
         599 +                    self.cur = None
         600 +                    continue
  576    601              if JOINT_TRAVEL and seg[0] == "move" and seg[3] == "travel" and self.jplan is None:
  577    602                  self.jplan = self._joint_plan(state, seg)
  578        -            if self.jplan is not None and self.jplan is not False and seg[0] == "move":
         603 +            if self.jplan is not None and self.jplan is not False and seg[0] in ("move", "jmove"):
  579    604                  if rejected:
  580    605                      self.jplan = False
  581    606                  else:
@@ -593,6 +618,9 @@ class GeneratedApproach:
  593    618                          self.last_cmd = True
  594    619                          return act
  595    620                      self.jplan = False
         621 +            if seg[0] == "jmove":
         622 +                self.cur = None
         623 +                continue
  596    624              if seg[0] == "grip":
  597    625                  act[10] = seg[1]
  598    626                  self.cur = None
@@ -695,9 +723,15 @@ class GeneratedApproach:
  695    723          return top + SAFE_CLR + hb + FINGER
  696    724  
  697    725      def _joint_plan(self, state, seg):
         726 +        nxt = None
         727 +        if self.segs and self.segs[0][0] == "move":
         728 +            nxt = self.segs[0][1]
         729 +        r = self._jplan_to(state, seg[1], seg[2], nxt=nxt)
         730 +        return False if r is None else r
         731 +
         732 +    def _jplan_to(self, state, goal, yaw, nxt=None, extra_bases=(), final_exempt=False):
  698    733          q = self._q(state)
  699    734          base = self._base(state)
  700        -        goal, yaw = seg[1], seg[2]
  701    735          Tw = self._ee_world(q, base)
  702    736          Rt = down_R(yaw) if yaw is not None else down_R(_yaw_of(Tw[:3, :3]))
  703    737          boxes = self._boxes(state)
@@ -706,13 +740,9 @@ class GeneratedApproach:
  706    740          if held is not None:
  707    741              b = boxes[held]
  708    742              hb = max(0.0, (Tw[2, 3] - FINGER) - (b["z"] - b["hz"]))
  709        -        # pose that must also be reachable afterwards (next descend)
  710        -        nxt = None
  711        -        if self.segs and self.segs[0][0] == "move":
  712        -            nxt = self.segs[0][1]
  713    743          p = Tw[:3, 3]
  714    744          dxy = goal[:2] - p[:2]
  715        -        cands = [base.copy()]
         745 +        cands = [base.copy()] + [np.array(e, float) for e in extra_bases]
  716    746          if BASE_TRAVEL:
  717    747              for fx, fy in ((1.0, 1.0), (0.0, 1.0), (0.5, 0.5), (0.0, 0.5)):
  718    748                  bb = base.copy()
@@ -745,17 +775,20 @@ class GeneratedApproach:
  745    775                      qn, en = self._ik_world(qg, nxt, Rt, bb, iters=100)
  746    776                      if en > 1e-4:
  747    777                          continue
  748        -                if not self._path_ok(q, base, q + dq, bb, boxes, held, hb):
         778 +                n = int(max(1, np.ceil(c / 0.2 - 1e-9)))
         779 +                if not self._path_ok(q, base, q + dq, bb, boxes, held, hb, n, final_exempt):
  749    780                      continue
  750    781                  best = (c, q + dq, bb)
  751    782          if best is None:
  752        -            return False
         783 +            return None
  753    784          return (best[1], best[2])
  754    785  
  755        -    def _path_ok(self, q, base, qg, bg, boxes, held, hb):
         786 +    def _path_ok(self, q, base, qg, bg, boxes, held, hb, n=12, final_exempt=False):
  756    787          db = bg - base
  757    788          db[2] = wrap(db[2])
  758        -        for sv in np.linspace(0.0, 1.0, 13)[1:-1]:
         789 +        ks = range(1, n) if final_exempt else range(1, n + 1)
         790 +        for k in ks:
         791 +            sv = k / n
  759    792              qs = q + sv * (qg - q)
  760    793              T = self._ee_world(qs, base + sv * db)
  761    794              if T[2, 2] > -0.9:
@@ -764,6 +797,18 @@ class GeneratedApproach:
  764    797                  return False
  765    798          return True
  766    799  
         800 +    def _merge(self, state, segs):
         801 +        """Replace (travel, descend) by a lazily planned joint move."""
         802 +        if not MERGE or self.nsteps < self.nomerge_until:
         803 +            return segs
         804 +        kinds = [sg[3] if sg[0] == "move" else sg[0] for sg in segs]
         805 +        if "travel" not in kinds:
         806 +            return segs
         807 +        it = kinds.index("travel")
         808 +        if it + 1 >= len(segs) or kinds[it + 1] not in ("grasp_descend", "place_descend"):
         809 +            return segs
         810 +        return segs[:it] + [("lazy", segs[it], segs[it + 1])] + segs[it + 2:]
         811 +
  767    812      def _handle_reject(self, state):
  768    813          seg = self.cur
  769    814          tag = seg[3] if (seg[0] == "move" and len(seg) > 3) else None
diff --git a/probe_rej.py b/probe_rej.py
new file mode 100644
index 0000000..7fffe59
--- /dev/null
+++ b/probe_rej.py
@@ -0,0 +1,22 @@
           1 +import sys, copy, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seed=int(sys.argv[1]); T=int(sys.argv[2])
           5 +env = make_env(); obs, info = env.reset(seed=seed)
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +acts=[]
           8 +for t in range(T):
           9 +    a = ap.get_action(obs); acts.append(a); obs, *_ = env.step(a)
          10 +a = ap.get_action(obs)
          11 +print("seg", ap.cur[0], ap.cur[3], "act", np.round(a,3))
          12 +def trial(aa, tag):
          13 +    e2 = make_env(); o,_ = e2.reset(seed=seed)
          14 +    for x in acts: o,*_ = e2.step(x)
          15 +    q0 = ap._q(o); b0=ap._base(o)
          16 +    o2,*_ = e2.step(aa)
          17 +    print(tag, "moved" if (np.abs(ap._q(o2)-q0).max()>1e-7 or np.abs(ap._base(o2)-b0).max()>1e-7) else "REJECTED")
          18 +trial(a, "full")
          19 +b = a.copy(); b[0:3]=0; trial(b, "arm only")
          20 +b = a.copy(); b[3:10]=0; trial(b, "base only")
          21 +b = a.copy(); b[3:10]*=0.3; b[0:3]*=0.3; trial(b, "0.3 scaled")
          22 +b = np.zeros(11,dtype=np.float32); b[0:3]=[0,0.02,0]; trial(b, "base y small")
diff --git a/res_base.txt b/res_base.txt
new file mode 100644
index 0000000..c631010
--- /dev/null
+++ b/res_base.txt
@@ -0,0 +1,41 @@
           1 +(0, 2, True, 30, 38.1, 0.83, 0.248)
           2 +(1, 1, True, 24, 31.8, 0.95, 0.516)
           3 +(2, 2, True, 36, 49.0, 0.9, 0.204)
           4 +(3, 2, True, 25, 27.1, 0.45, 0.096)
           5 +(4, 2, True, 33, 42.2, 0.58, 0.174)
           6 +(5, 2, True, 41, 48.6, 0.62, 0.13)
           7 +(6, 1, True, 25, 32.1, 0.87, 0.273)
           8 +(7, 2, True, 33, 51.6, 0.72, 0.18)
           9 +(8, 2, True, 30, 50.6, 0.97, 0.253)
          10 +(9, 1, True, 20, 28.8, 0.48, 0.161)
          11 +(10, 2, True, 23, 36.6, 0.46, 0.233)
          12 +(11, 0, True, 14, 18.5, 0.21, 0.083)
          13 +(12, 1, True, 29, 36.0, 0.49, 0.194)
          14 +(13, 2, True, 45, 72.3, 1.13, 0.316)
          15 +(14, 0, True, 12, 10.1, 0.17, 0.081)
          16 +(15, 2, True, 32, 43.6, 0.93, 0.321)
          17 +(16, 1, True, 21, 25.4, 0.66, 0.258)
          18 +(17, 2, True, 37, 58.8, 0.64, 0.124)
          19 +(18, 2, True, 25, 34.0, 0.4, 0.079)
          20 +(19, 1, True, 31, 44.8, 0.64, 0.28)
          21 +(20, 2, True, 34, 50.5, 0.74, 0.152)
          22 +(21, 0, True, 15, 12.1, 0.57, 0.314)
          23 +(22, 2, True, 22, 37.5, 0.61, 0.266)
          24 +(23, 0, True, 19, 24.2, 0.17, 0.052)
          25 +(24, 1, True, 14, 15.6, 0.23, 0.142)
          26 +(25, 1, True, 28, 37.4, 0.37, 0.074)
          27 +(26, 2, True, 23, 33.4, 0.46, 0.149)
          28 +(27, 0, True, 27, 29.7, 0.28, 0.142)
          29 +(28, 1, True, 53, 73.5, 1.46, 0.39)
          30 +(29, 2, True, 14, 22.1, 0.23, 0.128)
          31 +(30, 0, True, 18, 21.8, 0.44, 0.234)
          32 +(31, 1, True, 30, 44.3, 0.35, 0.068)
          33 +(32, 2, True, 30, 42.6, 0.69, 0.225)
          34 +(33, 2, True, 30, 43.2, 0.78, 0.385)
          35 +(34, 0, True, 13, 17.2, 0.11, 0.057)
          36 +(35, 0, True, 13, 17.2, 0.22, 0.116)
          37 +(36, 1, True, 20, 24.6, 0.72, 0.372)
          38 +(37, 0, True, 13, 13.2, 0.23, 0.134)
          39 +(38, 0, True, 14, 11.0, 0.56, 0.371)
          40 +(39, 2, True, 39, 29.3, 0.63, 0.361)
          41 +success 40 / 40 mean steps 25.875
diff --git a/res_t.txt b/res_t.txt
index c9dfcc8..0c4bdb4 100644
--- a/res_t.txt
+++ b/res_t.txt
@@ -1,41 +1,41 @@
    1        -(0, 2, True, 30, 32.0, 0.49, 0.113)
    2        -(1, 1, True, 24, 18.2, 0.52, 0.295)
    3        -(2, 2, True, 36, 40.8, 0.6, 0.127)
    4        -(3, 2, True, 25, 19.7, 0.26, 0.049)
    5        -(4, 2, True, 33, 29.6, 0.35, 0.047)
    6        -(5, 2, True, 41, 39.7, 0.51, 0.11)
    7        -(6, 1, True, 25, 15.6, 0.34, 0.093)
    8        -(7, 2, True, 33, 35.8, 0.25, 0.058)
    9        -(8, 2, True, 30, 33.8, 0.41, 0.077)
   10        -(9, 1, True, 20, 23.0, 0.29, 0.084)
   11        -(10, 2, True, 23, 27.8, 0.28, 0.085)
   12        -(11, 0, True, 14, 13.6, 0.14, 0.06)
   13        -(12, 1, True, 29, 30.8, 0.32, 0.09)
   14        -(13, 2, True, 45, 47.6, 0.5, 0.073)
   15        -(14, 0, True, 12, 10.7, 0.11, 0.054)
   16        -(15, 2, True, 32, 33.7, 0.22, 0.055)
   17        -(16, 1, True, 21, 20.9, 0.28, 0.082)
   18        -(17, 2, True, 37, 43.8, 0.47, 0.085)
   19        -(18, 2, True, 25, 19.1, 0.27, 0.067)
   20        -(19, 1, True, 31, 28.9, 0.43, 0.205)
   21        -(20, 2, True, 34, 35.9, 0.63, 0.2)
   22        -(21, 0, True, 15, 16.4, 0.18, 0.086)
   23        -(22, 2, True, 22, 30.4, 0.25, 0.06)
   24        -(23, 0, True, 19, 33.7, 0.23, 0.146)
   25        -(24, 1, True, 14, 24.3, 0.2, 0.104)
   26        -(25, 1, True, 28, 37.5, 0.3, 0.089)
   27        -(26, 2, True, 23, 30.0, 0.2, 0.048)
   28        -(27, 0, True, 27, 38.6, 0.26, 0.158)
   29        -(28, 1, True, 53, 51.3, 0.75, 0.216)
   30        -(29, 2, True, 14, 15.4, 0.19, 0.15)
   31        -(30, 0, True, 18, 17.6, 0.12, 0.052)
   32        -(31, 1, True, 30, 34.4, 0.31, 0.069)
   33        -(32, 2, True, 30, 35.9, 0.41, 0.06)
   34        -(33, 2, True, 30, 32.6, 0.38, 0.067)
   35        -(34, 0, True, 13, 17.4, 0.24, 0.162)
   36        -(35, 0, True, 13, 16.5, 0.07, 0.02)
   37        -(36, 1, True, 20, 17.8, 0.18, 0.048)
   38        -(37, 0, True, 13, 10.5, 0.2, 0.141)
   39        -(38, 0, True, 14, 7.4, 0.15, 0.097)
   40        -(39, 2, True, 39, 5.9, 0.37, 0.052)
   41        -success 40 / 40 mean steps 25.875
           1 +(0, 2, True, 27, 26.7, 0.34, 0.091)
           2 +(1, 1, True, 26, 24.7, 0.8, 0.516)
           3 +(2, 2, True, 35, 41.6, 0.58, 0.113)
           4 +(3, 2, True, 33, 34.2, 0.62, 0.19)
           5 +(4, 2, True, 36, 46.2, 0.62, 0.111)
           6 +(5, 2, True, 41, 49.2, 1.04, 0.257)
           7 +(6, 1, True, 21, 18.2, 0.28, 0.101)
           8 +(7, 2, True, 33, 33.5, 0.37, 0.068)
           9 +(8, 2, True, 26, 34.0, 0.82, 0.215)
          10 +(9, 1, True, 23, 28.9, 0.3, 0.065)
          11 +(10, 2, True, 25, 37.8, 0.32, 0.078)
          12 +(11, 0, True, 14, 17.9, 0.28, 0.108)
          13 +(12, 1, True, 28, 35.5, 0.83, 0.317)
          14 +(13, 2, True, 44, 78.7, 0.58, 0.112)
          15 +(14, 0, True, 11, 10.6, 0.1, 0.069)
          16 +(15, 2, True, 32, 54.8, 0.92, 0.321)
          17 +(16, 1, True, 19, 36.8, 0.7, 0.269)
          18 +(17, 2, True, 34, 66.9, 0.64, 0.186)
          19 +(18, 2, True, 22, 46.2, 1.09, 0.359)
          20 +(19, 1, True, 31, 51.7, 0.65, 0.23)
          21 +(20, 2, True, 36, 66.8, 0.79, 0.184)
          22 +(21, 0, True, 15, 22.6, 0.19, 0.105)
          23 +(22, 2, True, 20, 29.0, 0.62, 0.26)
          24 +(23, 0, True, 19, 20.0, 0.57, 0.273)
          25 +(24, 1, True, 14, 19.0, 0.28, 0.166)
          26 +(25, 1, True, 26, 35.9, 0.58, 0.363)
          27 +(26, 2, True, 20, 31.5, 0.28, 0.126)
          28 +(27, 0, True, 27, 30.5, 0.46, 0.296)
          29 +(28, 1, True, 53, 77.1, 1.21, 0.232)
          30 +(29, 2, True, 13, 19.6, 0.18, 0.109)
          31 +(30, 0, True, 18, 26.5, 0.24, 0.125)
          32 +(31, 1, True, 29, 46.6, 0.53, 0.156)
          33 +(32, 2, True, 27, 46.8, 0.49, 0.126)
          34 +(33, 2, True, 31, 51.1, 0.69, 0.128)
          35 +(34, 0, True, 12, 15.3, 0.16, 0.101)
          36 +(35, 0, True, 12, 15.7, 0.29, 0.12)
          37 +(36, 1, True, 17, 26.5, 0.46, 0.29)
          38 +(37, 0, True, 12, 16.0, 0.19, 0.126)
          39 +(38, 0, True, 14, 13.6, 0.33, 0.179)
          40 +(39, 2, True, 37, 31.7, 0.42, 0.079)
          41 +success 40 / 40 mean steps 25.325
diff --git a/res_t2.txt b/res_t2.txt
index 017f422..0835025 100644
--- a/res_t2.txt
+++ b/res_t2.txt
@@ -1,121 +1,121 @@
    1        -(40, 1, True, 80, 58.3, 2.73, 0.122)
    2        -(41, 1, True, 26, 32.7, 0.17, 0.034)
    3        -(42, 0, True, 18, 17.6, 0.06, 0.019)
    4        -(43, 1, True, 28, 32.6, 0.14, 0.022)
    5        -(44, 2, True, 34, 37.8, 0.23, 0.037)
    6        -(45, 2, True, 46, 50.5, 0.26, 0.028)
    7        -(46, 1, True, 23, 18.9, 0.16, 0.038)
    8        -(47, 0, True, 14, 4.5, 0.1, 0.034)
    9        -(48, 0, True, 14, 16.7, 0.07, 0.017)
   10        -(49, 0, True, 16, 15.6, 0.11, 0.046)
   11        -(50, 2, True, 48, 52.0, 0.36, 0.153)
   12        -(51, 1, True, 25, 24.6, 0.16, 0.024)
   13        -(52, 2, True, 57, 67.5, 1.13, 0.839)
   14        -(53, 2, True, 49, 51.9, 0.28, 0.051)
   15        -(54, 0, True, 16, 19.6, 0.06, 0.013)
   16        -(55, 2, True, 49, 57.3, 0.36, 0.086)
   17        -(56, 1, True, 26, 19.5, 0.18, 0.029)
   18        -(57, 0, True, 16, 11.1, 0.05, 0.017)
   19        -(58, 1, True, 28, 34.0, 0.17, 0.056)
   20        -(59, 2, True, 61, 66.0, 0.35, 0.047)
   21        -(60, 0, True, 15, 12.2, 0.08, 0.028)
   22        -(61, 1, True, 32, 35.7, 0.14, 0.031)
   23        -(62, 1, True, 26, 26.1, 0.13, 0.021)
   24        -(63, 1, True, 33, 34.5, 0.15, 0.028)
   25        -(64, 1, True, 26, 20.5, 0.16, 0.032)
   26        -(65, 0, True, 27, 27.3, 0.1, 0.043)
   27        -(66, 2, True, 38, 36.1, 0.25, 0.027)
   28        -(67, 2, True, 43, 44.5, 0.23, 0.039)
   29        -(68, 1, True, 21, 26.8, 0.07, 0.026)
   30        -(69, 0, True, 15, 11.2, 0.06, 0.021)
   31        -(70, 1, True, 35, 36.5, 0.16, 0.028)
   32        -(71, 2, True, 46, 47.9, 0.27, 0.039)
   33        -(72, 2, True, 54, 64.1, 0.38, 0.075)
   34        -(73, 2, True, 43, 47.3, 0.25, 0.056)
   35        -(74, 0, True, 15, 13.0, 0.06, 0.018)
   36        -(75, 1, True, 23, 21.7, 0.15, 0.034)
   37        -(76, 1, True, 40, 43.5, 0.18, 0.038)
   38        -(77, 0, True, 20, 13.3, 0.1, 0.035)
   39        -(78, 2, True, 30, 27.9, 0.13, 0.034)
   40        -(79, 0, True, 14, 14.2, 0.06, 0.03)
   41        -(80, 2, True, 42, 43.8, 0.25, 0.027)
   42        -(81, 0, True, 21, 24.8, 0.07, 0.018)
   43        -(82, 2, True, 49, 48.7, 0.31, 0.039)
   44        -(83, 2, True, 33, 34.2, 0.18, 0.037)
   45        -(84, 1, True, 28, 21.5, 0.16, 0.027)
   46        -(85, 2, True, 40, 33.7, 0.34, 0.045)
   47        -(86, 2, True, 44, 44.3, 0.22, 0.033)
   48        -(87, 1, True, 37, 32.3, 0.26, 0.071)
   49        -(88, 1, True, 34, 30.1, 0.21, 0.027)
   50        -(89, 2, True, 46, 51.6, 0.95, 0.63)
   51        -(90, 1, True, 25, 23.4, 0.16, 0.027)
   52        -(91, 2, True, 33, 33.8, 0.25, 0.066)
   53        -(92, 1, True, 34, 27.8, 0.18, 0.033)
   54        -(93, 2, True, 51, 55.3, 0.31, 0.036)
   55        -(94, 0, True, 21, 22.9, 0.14, 0.05)
   56        -(95, 1, True, 30, 29.4, 0.23, 0.041)
   57        -(96, 2, True, 45, 46.2, 0.29, 0.047)
   58        -(97, 0, True, 24, 24.4, 0.11, 0.055)
   59        -(98, 1, True, 37, 37.2, 0.16, 0.024)
   60        -(99, 2, True, 39, 42.3, 0.29, 0.031)
   61        -(100, 2, True, 38, 41.3, 0.23, 0.036)
   62        -(101, 0, True, 15, 13.7, 0.08, 0.022)
   63        -(102, 1, True, 26, 35.8, 0.14, 0.029)
   64        -(103, 1, True, 29, 38.1, 0.21, 0.042)
   65        -(104, 2, True, 47, 67.3, 0.25, 0.038)
   66        -(105, 0, True, 15, 12.4, 0.08, 0.023)
   67        -(106, 1, True, 21, 31.0, 0.06, 0.016)
   68        -(107, 0, True, 17, 27.8, 0.05, 0.017)
   69        -(108, 0, True, 18, 28.9, 0.13, 0.079)
   70        -(109, 1, True, 33, 51.4, 0.2, 0.051)
   71        -(110, 1, True, 37, 54.1, 0.18, 0.032)
   72        -(111, 1, True, 22, 21.6, 0.16, 0.026)
   73        -(112, 0, True, 19, 19.5, 0.09, 0.052)
   74        -(113, 0, True, 20, 26.6, 0.05, 0.017)
   75        -(114, 0, True, 15, 16.3, 0.05, 0.012)
   76        -(115, 1, True, 31, 43.5, 0.14, 0.024)
   77        -(116, 0, True, 19, 26.9, 0.1, 0.029)
   78        -(117, 0, True, 15, 24.4, 0.05, 0.017)
   79        -(118, 1, True, 32, 46.1, 0.2, 0.072)
   80        -(119, 1, True, 40, 58.8, 0.26, 0.088)
   81        -(120, 0, True, 17, 21.5, 0.09, 0.034)
   82        -(121, 0, True, 18, 23.9, 0.09, 0.025)
   83        -(122, 2, True, 55, 60.1, 0.28, 0.041)
   84        -(123, 0, True, 18, 20.0, 0.07, 0.018)
   85        -(124, 2, True, 30, 30.7, 0.16, 0.022)
   86        -(125, 1, True, 44, 46.9, 0.19, 0.035)
   87        -(126, 0, True, 18, 19.6, 0.07, 0.024)
   88        -(127, 1, True, 16, 12.3, 0.07, 0.03)
   89        -(128, 2, True, 55, 47.0, 0.35, 0.036)
   90        -(129, 1, True, 28, 22.2, 0.18, 0.03)
   91        -(130, 2, True, 47, 46.0, 0.97, 0.701)
   92        -(131, 1, True, 41, 34.3, 0.17, 0.041)
   93        -(132, 2, True, 42, 30.4, 0.26, 0.038)
   94        -(133, 1, True, 32, 18.4, 0.16, 0.025)
   95        -(134, 2, True, 47, 48.7, 0.2, 0.023)
   96        -(135, 1, True, 31, 28.4, 0.19, 0.039)
   97        -(136, 2, True, 31, 32.6, 0.16, 0.044)
   98        -(137, 1, True, 30, 29.9, 0.17, 0.03)
   99        -(138, 1, True, 32, 33.3, 0.12, 0.033)
  100        -(139, 1, True, 33, 32.1, 0.13, 0.019)
  101        -(140, 1, True, 31, 36.2, 0.13, 0.021)
  102        -(141, 1, True, 29, 26.5, 0.15, 0.019)
  103        -(142, 0, True, 26, 35.6, 0.09, 0.026)
  104        -(143, 2, True, 51, 56.1, 0.31, 0.03)
  105        -(144, 0, True, 19, 23.3, 0.09, 0.031)
  106        -(145, 1, True, 25, 27.0, 0.11, 0.036)
  107        -(146, 2, True, 27, 36.5, 0.11, 0.019)
  108        -(147, 0, True, 15, 12.3, 0.05, 0.01)
  109        -(148, 0, True, 17, 17.8, 0.07, 0.028)
  110        -(149, 0, True, 17, 18.6, 0.07, 0.029)
  111        -(150, 1, True, 22, 23.0, 0.1, 0.035)
  112        -(151, 2, True, 37, 35.3, 0.14, 0.025)
  113        -(152, 2, True, 38, 33.1, 0.22, 0.044)
  114        -(153, 2, True, 44, 32.9, 0.2, 0.023)
  115        -(154, 0, True, 12, 9.7, 0.06, 0.022)
  116        -(155, 0, True, 18, 19.2, 0.08, 0.033)
  117        -(156, 2, True, 53, 21.3, 0.21, 0.028)
  118        -(157, 0, True, 19, 11.2, 0.08, 0.031)
  119        -(158, 1, True, 27, 8.2, 0.15, 0.033)
  120        -(159, 2, True, 40, 9.1, 0.21, 0.04)
  121        -success 120 / 120 mean steps 31.033333333333335
           1 +(40, 1, True, 27, 43.5, 0.26, 0.074)
           2 +(41, 1, True, 20, 17.7, 0.17, 0.047)
           3 +(42, 0, True, 14, 11.5, 0.11, 0.052)
           4 +(43, 1, True, 21, 31.5, 0.14, 0.037)
           5 +(44, 2, True, 23, 36.9, 0.33, 0.08)
           6 +(45, 2, True, 34, 53.8, 0.33, 0.076)
           7 +(46, 1, True, 19, 20.3, 0.19, 0.035)
           8 +(47, 0, True, 12, 7.0, 0.08, 0.032)
           9 +(48, 0, True, 13, 19.6, 0.12, 0.056)
          10 +(49, 0, True, 13, 17.0, 0.13, 0.078)
          11 +(50, 2, True, 36, 49.1, 0.35, 0.114)
          12 +(51, 1, True, 20, 23.0, 0.25, 0.106)
          13 +(52, 2, True, 47, 58.1, 0.4, 0.086)
          14 +(53, 2, True, 32, 36.4, 0.34, 0.082)
          15 +(54, 0, True, 14, 19.1, 0.12, 0.056)
          16 +(55, 2, True, 41, 50.1, 0.34, 0.044)
          17 +(56, 1, True, 21, 20.1, 0.22, 0.07)
          18 +(57, 0, True, 12, 11.4, 0.09, 0.035)
          19 +(58, 1, True, 18, 25.8, 0.1, 0.026)
          20 +(59, 2, True, 42, 58.3, 0.46, 0.09)
          21 +(60, 0, True, 12, 14.0, 0.19, 0.105)
          22 +(61, 1, True, 23, 27.5, 0.16, 0.046)
          23 +(62, 1, True, 21, 21.7, 0.2, 0.049)
          24 +(63, 1, True, 23, 32.2, 0.35, 0.211)
          25 +(64, 1, True, 21, 22.7, 0.18, 0.047)
          26 +(65, 0, True, 20, 25.9, 0.12, 0.047)
          27 +(66, 2, True, 30, 39.5, 0.53, 0.164)
          28 +(67, 2, True, 31, 37.9, 0.57, 0.179)
          29 +(68, 1, True, 18, 23.4, 0.19, 0.075)
          30 +(69, 0, True, 13, 13.4, 0.11, 0.068)
          31 +(70, 1, True, 24, 33.0, 2.3, 2.04)
          32 +(71, 2, True, 36, 44.4, 0.57, 0.121)
          33 +(72, 2, True, 45, 61.3, 0.36, 0.074)
          34 +(73, 2, True, 34, 40.0, 0.63, 0.155)
          35 +(74, 0, True, 13, 9.8, 0.3, 0.169)
          36 +(75, 1, True, 21, 21.5, 0.26, 0.076)
          37 +(76, 1, True, 26, 31.6, 0.37, 0.089)
          38 +(77, 0, True, 13, 8.9, 0.13, 0.062)
          39 +(78, 2, True, 21, 24.8, 0.18, 0.048)
          40 +(79, 0, True, 11, 9.0, 0.16, 0.082)
          41 +(80, 2, True, 33, 40.7, 0.4, 0.074)
          42 +(81, 0, True, 15, 16.3, 0.19, 0.123)
          43 +(82, 2, True, 38, 48.7, 0.48, 0.109)
          44 +(83, 2, True, 27, 26.5, 0.38, 0.111)
          45 +(84, 1, True, 21, 18.4, 0.27, 0.056)
          46 +(85, 2, True, 28, 27.8, 0.35, 0.06)
          47 +(86, 2, True, 34, 34.3, 0.4, 0.141)
          48 +(87, 1, True, 26, 27.7, 0.28, 0.07)
          49 +(88, 1, True, 22, 21.8, 0.25, 0.076)
          50 +(89, 2, True, 46, 60.4, 1.2, 0.393)
          51 +(90, 1, True, 20, 26.5, 0.3, 0.076)
          52 +(91, 2, True, 22, 34.6, 0.25, 0.069)
          53 +(92, 1, True, 26, 34.4, 0.48, 0.192)
          54 +(93, 2, True, 43, 65.0, 0.57, 0.082)
          55 +(94, 0, True, 13, 15.7, 0.33, 0.256)
          56 +(95, 1, True, 23, 23.9, 0.24, 0.072)
          57 +(96, 2, True, 33, 40.4, 0.64, 0.246)
          58 +(97, 0, True, 25, 23.9, 0.56, 0.426)
          59 +(98, 1, True, 28, 37.0, 0.27, 0.061)
          60 +(99, 2, True, 29, 31.7, 0.47, 0.095)
          61 +(100, 2, True, 32, 49.5, 0.58, 0.225)
          62 +(101, 0, True, 13, 14.3, 0.2, 0.104)
          63 +(102, 1, True, 22, 23.7, 0.39, 0.111)
          64 +(103, 1, True, 20, 23.7, 0.42, 0.129)
          65 +(104, 2, True, 41, 60.3, 0.61, 0.124)
          66 +(105, 0, True, 13, 15.6, 0.28, 0.166)
          67 +(106, 1, True, 13, 24.9, 0.25, 0.116)
          68 +(107, 0, True, 12, 22.9, 0.2, 0.154)
          69 +(108, 0, True, 13, 22.4, 0.16, 0.066)
          70 +(109, 1, True, 24, 35.9, 0.43, 0.098)
          71 +(110, 1, True, 23, 36.4, 0.34, 0.078)
          72 +(111, 1, True, 20, 28.1, 0.33, 0.072)
          73 +(112, 0, True, 14, 17.0, 0.17, 0.072)
          74 +(113, 0, True, 15, 20.0, 0.15, 0.064)
          75 +(114, 0, True, 14, 17.9, 0.08, 0.038)
          76 +(115, 1, True, 22, 30.6, 0.18, 0.039)
          77 +(116, 0, True, 18, 30.4, 0.14, 0.077)
          78 +(117, 0, True, 13, 22.4, 0.07, 0.034)
          79 +(118, 1, True, 31, 40.2, 0.2, 0.047)
          80 +(119, 1, True, 29, 37.1, 0.52, 0.259)
          81 +(120, 0, True, 14, 15.2, 0.16, 0.08)
          82 +(121, 0, True, 14, 20.0, 0.09, 0.052)
          83 +(122, 2, True, 45, 53.0, 0.36, 0.053)
          84 +(123, 0, True, 14, 13.2, 0.08, 0.043)
          85 +(124, 2, True, 20, 21.3, 0.29, 0.06)
          86 +(125, 1, True, 29, 36.3, 0.19, 0.038)
          87 +(126, 0, True, 14, 22.1, 0.13, 0.058)
          88 +(127, 1, True, 13, 16.5, 0.1, 0.054)
          89 +(128, 2, True, 35, 38.2, 0.45, 0.064)
          90 +(129, 1, True, 23, 23.0, 0.35, 0.093)
          91 +(130, 2, True, 30, 33.5, 0.56, 0.131)
          92 +(131, 1, True, 33, 35.6, 0.59, 0.207)
          93 +(132, 2, True, 29, 26.7, 0.51, 0.11)
          94 +(133, 1, True, 27, 22.7, 0.39, 0.171)
          95 +(134, 2, True, 34, 44.0, 0.59, 0.245)
          96 +(135, 1, True, 22, 27.9, 0.34, 0.073)
          97 +(136, 2, True, 23, 31.0, 0.4, 0.097)
          98 +(137, 1, True, 24, 29.9, 0.35, 0.137)
          99 +(138, 1, True, 24, 29.9, 0.39, 0.18)
         100 +(139, 1, True, 22, 27.4, 0.41, 0.192)
         101 +(140, 1, True, 27, 42.4, 0.51, 0.152)
         102 +(141, 1, True, 22, 30.9, 0.18, 0.044)
         103 +(142, 0, True, 20, 21.5, 0.24, 0.121)
         104 +(143, 2, True, 41, 64.3, 0.32, 0.055)
         105 +(144, 0, True, 14, 25.6, 0.1, 0.031)
         106 +(145, 1, True, 21, 30.2, 0.33, 0.148)
         107 +(146, 2, True, 19, 26.8, 0.22, 0.046)
         108 +(147, 0, True, 12, 16.7, 0.16, 0.086)
         109 +(148, 0, True, 13, 13.5, 0.15, 0.057)
         110 +(149, 0, True, 14, 20.7, 0.07, 0.03)
         111 +(150, 1, True, 15, 18.6, 0.11, 0.043)
         112 +(151, 2, True, 26, 28.7, 0.26, 0.084)
         113 +(152, 2, True, 29, 27.1, 0.44, 0.093)
         114 +(153, 2, True, 32, 25.7, 0.34, 0.098)
         115 +(154, 0, True, 11, 9.7, 0.13, 0.068)
         116 +(155, 0, True, 13, 11.3, 0.12, 0.063)
         117 +(156, 2, True, 45, 17.3, 0.52, 0.11)
         118 +(157, 0, True, 14, 9.2, 0.12, 0.045)
         119 +(158, 1, True, 24, 7.6, 0.33, 0.167)
         120 +(159, 2, True, 30, 5.4, 0.34, 0.098)
         121 +success 120 / 120 mean steps 23.5
diff --git a/res_t4.txt b/res_t4.txt
new file mode 100644
index 0000000..e69de29
diff --git a/res_t8.txt b/res_t8.txt
index 8b6414c..e69de29 100644
--- a/res_t8.txt
+++ b/res_t8.txt
@@ -1,33 +0,0 @@
    1        -(0, 8, True, 101, 63.4, 0.84, 0.068)
    2        -(1, 8, True, 130, 106.1, 1.17, 0.089)
    3        -(2, 8, True, 75, 53.5, 1.32, 0.556)
    4        -(3, 8, True, 75, 46.8, 0.87, 0.141)
    5        -(4, 8, True, 187, 137.4, 2.63, 0.839)
    6        -(5, 8, True, 125, 82.3, 1.24, 0.099)
    7        -(6, 8, True, 711, 276.9, 4.89, 0.151)
    8        -(7, 8, True, 147, 122.6, 1.4, 0.195)
    9        -(8, 8, True, 118, 82.1, 1.02, 0.071)
   10        -(9, 8, True, 95, 60.0, 0.81, 0.143)
   11        -(10, 8, True, 98, 62.4, 0.89, 0.092)
   12        -(11, 8, True, 104, 74.3, 0.79, 0.102)
   13        -(12, 8, True, 125, 84.4, 1.03, 0.082)
   14        -(13, 8, True, 324, 145.6, 2.29, 0.131)
   15        -(14, 8, True, 58, 31.4, 0.46, 0.07)
   16        -(15, 8, True, 181, 108.7, 1.58, 0.496)
   17        -(16, 8, True, 74, 46.4, 0.53, 0.067)
   18        -(17, 8, True, 77, 45.3, 0.69, 0.063)
   19        -(18, 8, True, 136, 77.6, 1.03, 0.062)
   20        -(19, 8, True, 605, 177.1, 4.38, 0.164)
   21        -(20, 8, True, 97, 51.5, 0.76, 0.134)
   22        -(21, 8, True, 118, 74.9, 1.43, 0.714)
   23        -(22, 8, True, 82, 39.7, 0.62, 0.051)
   24        -(23, 8, True, 107, 75.2, 0.73, 0.1)
   25        -(24, 8, True, 85, 47.2, 0.62, 0.057)
   26        -(25, 8, True, 81, 52.6, 0.5, 0.073)
   27        -(26, 8, True, 70, 40.2, 0.81, 0.434)
   28        -(27, 8, True, 75, 43.4, 0.43, 0.051)
   29        -(28, 8, True, 151, 65.7, 1.05, 0.092)
   30        -(29, 8, True, 68, 36.4, 0.63, 0.096)
   31        -(30, 8, True, 67, 32.5, 0.55, 0.084)
   32        -(31, 8, True, 101, 34.8, 0.96, 0.063)
   33        -success 32 / 32 mean steps 145.25
```

</details>

<a id="C021"></a>
### C021 · Lower floor/safe clearances (mean ~24 steps default)

Commit `e0f7863121468b2bb0c7f947907c46bd38c71391`; parents: a6b25370e6861b1a62ea7bd28b71e5045f7aee10. Recorded author date: 2026-10-01T01:11:18+02:00.

File roles (automatic): policy.

- [E1551](01_timeline.md#E1551): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_e0f7863_approach.py) · [Exact all-file diff](evidence/diffs/C021_e0f7863.diff)

[Previous saved controller snapshot](evidence/versions/C020_a6b2537_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 454b01f..4cf693c 100644
--- a/approach.py
+++ b/approach.py
@@ -143,7 +143,9 @@ ROT_MAX = 0.8
  143    143  BASE_TRAVEL = True
  144    144  BASE_XMAX = -0.08
  145    145  MERGE = True
  146        -SAFE_CLR = 0.02
         146 +FLOOR_CLR = 0.005
         147 +LIFT_MIN = False
         148 +SAFE_CLR = 0.012
  147    149  MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
  148    150  TABLE_X = (0.10, 0.50)
  149    151  TABLE_Y = (-0.40, 0.40)
@@ -330,7 +332,7 @@ class GeneratedApproach:
  330    332          return cands
  331    333  
  332    334      def _safe_z(self, boxes, exclude=None, held_below=0.0, path=None, rad=0.08):
  333        -        top = TABLE_TOP + 0.03
         335 +        top = TABLE_TOP + FLOOR_CLR
  334    336          for n, b in boxes.items():
  335    337              if b["g"] > 0.5 or n == exclude:
  336    338                  continue
@@ -583,6 +585,9 @@ class GeneratedApproach:
  583    585                  else:
  584    586                      self.cur = tr
  585    587                      self.segs.insert(0, de)
         588 +                    if seg[3] is not None:
         589 +                        self.segs.insert(0, tr)
         590 +                        self.cur = seg[3]
  586    591                  self.jplan = None
  587    592                  self.best_d = None
  588    593                  self.stall = 0
@@ -708,7 +713,7 @@ class GeneratedApproach:
  708    713          return act
  709    714  
  710    715      def _req_z(self, boxes, xy, held, hb):
  711        -        top = TABLE_TOP + 0.03
         716 +        top = TABLE_TOP + FLOOR_CLR
  712    717          rad = 0.08
  713    718          if held is not None:
  714    719              ex, ey = self._extent_xy(boxes[held])
@@ -807,7 +812,25 @@ class GeneratedApproach:
  807    812          it = kinds.index("travel")
  808    813          if it + 1 >= len(segs) or kinds[it + 1] not in ("grasp_descend", "place_descend"):
  809    814              return segs
  810        -        return segs[:it] + [("lazy", segs[it], segs[it + 1])] + segs[it + 2:]
         815 +        pre = segs[:it]
         816 +        full_lift = None
         817 +        if LIFT_MIN and len(pre) == 1 and pre[0][0] == "move" and pre[0][3] == "lift":
         818 +            q = self._q(state)
         819 +            base = self._base(state)
         820 +            Tw = self._ee_world(q, base)
         821 +            boxes = self._boxes(state)
         822 +            held = self._held(boxes)
         823 +            hb = 0.0
         824 +            if held is not None:
         825 +                b = boxes[held]
         826 +                hb = max(0.0, (Tw[2, 3] - FINGER) - (b["z"] - b["hz"]))
         827 +            loc = self._req_z(boxes, Tw[:2, 3], held, hb)
         828 +            lg = pre[0][1]
         829 +            if loc < lg[2] - 0.01:
         830 +                full_lift = pre[0]
         831 +                nz = max(Tw[2, 3], loc)
         832 +                pre = [("move", np.array([lg[0], lg[1], nz]), pre[0][2], "lift")]
         833 +        return pre + [("lazy", segs[it], segs[it + 1], full_lift)] + segs[it + 2:]
  811    834  
  812    835      def _handle_reject(self, state):
  813    836          seg = self.cur
```

</details>

<a id="C022"></a>
### C022 · Close gripper when grasp descent is blocked but fingers already straddle object

Commit `9f441744a5d336f281edf2fc5a96776af50b222c`; parents: e0f7863121468b2bb0c7f947907c46bd38c71391. Recorded author date: 2026-10-01T01:46:28+02:00.

File roles (automatic): policy.

- [E1668](01_timeline.md#E1668): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_9f44174_approach.py) · [Exact all-file diff](evidence/diffs/C022_9f44174.diff)

[Previous saved controller snapshot](evidence/versions/C021_e0f7863_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4cf693c..b697140 100644
--- a/approach.py
+++ b/approach.py
@@ -843,6 +843,16 @@ class GeneratedApproach:
  843    843              self.cur = None
  844    844              return
  845    845          if tag == "grasp_descend":
         846 +            name = seg[4] if len(seg) > 4 else None
         847 +            boxes = self._boxes(state)
         848 +            if name in boxes:
         849 +                ob = boxes[name]
         850 +                tip = T[2, 3] - FINGER
         851 +                if tip <= ob["z"] + ob["hz"] + 0.002 and tip >= ob["z"] - ob["hz"] + 0.016:
         852 +                    # fingers already straddle the object: try closing here
         853 +                    self.segs = [("grip", -1.0, name)] + [sg for sg in self.segs if sg[0] != "grip"]
         854 +                    self.cur = None
         855 +                    return
  846    856              key = getattr(self, "cur_key", None)
  847    857              if key is not None:
  848    858                  self.fail[key] = self.fail.get(key, 0) + 1
```

</details>

<a id="C023"></a>
### C023 · Add validation results and debug scripts

Commit `3506b1ed994b01b7139dcbc15e39e6bd6b550bbc`; parents: 9f441744a5d336f281edf2fc5a96776af50b222c. Recorded author date: 2026-10-01T01:53:45+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E1705](01_timeline.md#E1705): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C023_3506b1e.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/d104.txt b/d104.txt
new file mode 100644
index 0000000..342421d
--- /dev/null
+++ b/d104.txt
@@ -0,0 +1,385 @@
           1 +obstruction0 {'x': 0.216, 'y': -0.114, 'z': 0.106, 'hx': 0.018, 'hy': 0.011, 'hz': 0.021, 'g': 0.0, 'yaw': 0.0}
           2 +obstruction1 {'x': 0.23, 'y': -0.09, 'z': 0.111, 'hx': 0.014, 'hy': 0.013, 'hz': 0.026, 'g': 0.0, 'yaw': 0.0}
           3 +obstruction2 {'x': 0.18, 'y': -0.086, 'z': 0.111, 'hx': 0.015, 'hy': 0.017, 'hz': 0.026, 'g': 0.0, 'yaw': 0.0}
           4 +obstruction3 {'x': 0.164, 'y': -0.056, 'z': 0.1, 'hx': 0.011, 'hy': 0.01, 'hz': 0.015, 'g': 0.0, 'yaw': 0.0}
           5 +obstruction4 {'x': 0.147, 'y': -0.09, 'z': 0.107, 'hx': 0.014, 'hy': 0.014, 'hz': 0.022, 'g': 0.0, 'yaw': 0.0}
           6 +obstruction5 {'x': 0.222, 'y': -0.046, 'z': 0.103, 'hx': 0.018, 'hy': 0.02, 'hz': 0.018, 'g': 0.0, 'yaw': 0.0}
           7 +obstruction6 {'x': 0.452, 'y': -0.012, 'z': 0.09, 'hx': 0.017, 'hy': 0.013, 'hz': 0.015, 'g': 0.0, 'yaw': 0.0}
           8 +obstruction7 {'x': 0.161, 'y': -0.123, 'z': 0.105, 'hx': 0.014, 'hy': 0.011, 'hz': 0.02, 'g': 0.0, 'yaw': 0.0}
           9 +target_block {'x': 0.377, 'y': -0.064, 'z': 0.1, 'hx': 0.036, 'hy': 0.033, 'hz': 0.025, 'g': 0.0, 'yaw': 0.0}
          10 +target_region {'x': 0.184, 'y': -0.09, 'z': 0.08, 'hx': 0.045, 'hy': 0.041, 'hz': 0.005, 'g': 0.0, 'yaw': 0.0}
          11 +0 ('move', (0.139, 0.001, 0.342), None, 'lift') ee [0.139 0.001 0.342] grasp 0.0 
          12 +1 ('move', (0.147, -0.09, 0.305), -3.14, 'travel') ee [ 0.142 -0.008  0.339] grasp 0.0 
          13 +11 ('move', (0.147, -0.09, 0.262), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.305] grasp 0.0 REJ
          14 +13 ('move', (0.147, -0.09, 0.262), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.294] grasp 0.0 REJ
          15 +14 ('move', (0.147, -0.09, 0.262), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.294] grasp 0.0 REJ
          16 +15 ('move', (0.147, -0.09, 0.262), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.294] grasp 0.0 REJ
          17 +16 ('move', (0.147, -0.09, 0.262), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.294] grasp 0.0 REJ
          18 +17 ('move', (0.147, -0.09, 0.354), None, 'lift') ee [ 0.147 -0.09   0.294] grasp 0.0 
          19 +28 ('move', (0.23, -0.09, 0.305), -3.14, 'travel') ee [ 0.191 -0.088  0.329] grasp 0.0 
          20 +30 ('move', (0.23, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.305] grasp 0.0 REJ
          21 +32 ('move', (0.23, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.294] grasp 0.0 REJ
          22 +33 ('move', (0.23, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.294] grasp 0.0 REJ
          23 +34 ('move', (0.23, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.294] grasp 0.0 REJ
          24 +36 ('move', (0.23, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.293] grasp 0.0 REJ
          25 +37 ('move', (0.23, -0.09, 0.353), None, 'lift') ee [ 0.23  -0.09   0.294] grasp 0.0 
          26 +48 ('move', (0.18, -0.086, 0.305), -3.14, 'travel') ee [ 0.206 -0.09   0.328] grasp 0.0 
          27 +50 ('move', (0.18, -0.086, 0.266), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.305] grasp 0.0 REJ
          28 +52 ('move', (0.18, -0.086, 0.266), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.294] grasp 0.0 REJ
          29 +53 ('move', (0.18, -0.086, 0.266), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.294] grasp 0.0 REJ
          30 +55 ('move', (0.18, -0.086, 0.266), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.292] grasp 0.0 REJ
          31 +56 ('move', (0.18, -0.086, 0.266), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.292] grasp 0.0 REJ
          32 +57 ('move', (0.18, -0.086, 0.352), None, 'lift') ee [ 0.18  -0.086  0.293] grasp 0.0 
          33 +68 ('move', (0.222, -0.046, 0.305), 2.36, 'travel') ee [ 0.196 -0.07   0.338] grasp 0.0 
          34 +71 ('move', (0.222, -0.046, 0.258), 2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.27 ] grasp 0.0 
          35 +73 None ee [ 0.222 -0.046  0.258] grasp 0.0 
          36 +74 ('move', (0.222, -0.046, 0.305), None, 'lift') ee [ 0.222 -0.046  0.29 ] grasp 0.0 
          37 +76 ('move', (0.216, -0.114, 0.305), -3.14, 'travel') ee [ 0.221 -0.063  0.305] grasp 0.0 
          38 +80 ('move', (0.216, -0.114, 0.261), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
          39 +82 ('move', (0.216, -0.114, 0.261), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.294] grasp 0.0 REJ
          40 +83 ('move', (0.216, -0.114, 0.261), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.294] grasp 0.0 REJ
          41 +85 ('move', (0.216, -0.114, 0.261), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.292] grasp 0.0 REJ
          42 +86 ('move', (0.216, -0.114, 0.261), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.292] grasp 0.0 REJ
          43 +87 ('move', (0.216, -0.114, 0.352), None, 'lift') ee [ 0.216 -0.114  0.293] grasp 0.0 
          44 +98 ('move', (0.161, -0.123, 0.305), -3.14, 'travel') ee [ 0.19  -0.12   0.327] grasp 0.0 
          45 +100 ('move', (0.161, -0.123, 0.26), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.282] grasp 0.0 
          46 +101 ('move', (0.161, -0.123, 0.26), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.282] grasp 0.0 REJ
          47 +102 ('move', (0.161, -0.123, 0.26), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.282] grasp 0.0 REJ
          48 +103 ('move', (0.161, -0.123, 0.26), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.282] grasp 0.0 REJ
          49 +104 ('move', (0.161, -0.123, 0.26), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.282] grasp 0.0 REJ
          50 +105 ('move', (0.161, -0.123, 0.342), None, 'lift') ee [ 0.161 -0.123  0.283] grasp 0.0 
          51 +115 ('move', (0.222, -0.046, 0.305), -3.14, 'travel') ee [ 0.194 -0.085  0.324] grasp 0.0 
          52 +117 ('move', (0.222, -0.046, 0.258), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.273] grasp 0.0 
          53 +118 ('move', (0.222, -0.046, 0.258), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.273] grasp 0.0 REJ
          54 +119 ('move', (0.222, -0.046, 0.258), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.273] grasp 0.0 REJ
          55 +121 ('move', (0.222, -0.046, 0.258), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.27 ] grasp 0.0 REJ
          56 +122 ('move', (0.222, -0.046, 0.258), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.27 ] grasp 0.0 REJ
          57 +123 ('move', (0.222, -0.046, 0.258), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.27 ] grasp 0.0 REJ
          58 +124 ('move', (0.222, -0.046, 0.33), None, 'lift') ee [ 0.222 -0.046  0.271] grasp 0.0 
          59 +135 ('base', (-0.13, 0.01, 0.0)) ee [ 0.172 -0.046  0.33 ] grasp 0.0 
          60 +136 ('move', (0.147, -0.09, 0.305), -3.14, 'travel') ee [ 0.147 -0.09   0.305] grasp 0.0 
          61 +137 ('move', (0.147, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.305] grasp 0.0 REJ
          62 +139 ('move', (0.147, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.293] grasp 0.0 REJ
          63 +140 ('move', (0.147, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.293] grasp 0.0 REJ
          64 +141 ('move', (0.147, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.293] grasp 0.0 REJ
          65 +142 ('move', (0.147, -0.09, 0.266), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.293] grasp 0.0 REJ
          66 +143 ('move', (0.147, -0.09, 0.353), None, 'lift') ee [ 0.147 -0.09   0.294] grasp 0.0 
          67 +154 ('move', (0.164, -0.056, 0.305), -3.14, 'travel') ee [ 0.158 -0.072  0.329] grasp 0.0 
          68 +156 ('move', (0.164, -0.056, 0.257), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
          69 +159 ('move', (0.164, -0.056, 0.257), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.278] grasp 0.0 REJ
          70 +160 ('move', (0.164, -0.056, 0.257), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.278] grasp 0.0 REJ
          71 +161 ('move', (0.164, -0.056, 0.257), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.278] grasp 0.0 REJ
          72 +163 ('move', (0.164, -0.056, 0.257), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.276] grasp 0.0 REJ
          73 +164 ('move', (0.164, -0.056, 0.336), None, 'lift') ee [ 0.164 -0.056  0.278] grasp 0.0 
          74 +174 ('jmove', (-0.436, 0.062, -2.45, -2.538, -0.075, -0.557, 3.459), (-0.08, -0.051, 0.0), 'm_grasp_descend') ee [ 0.2   -0.068  0.302] grasp 0.0 
          75 +175 ('jmove', (-0.436, 0.062, -2.45, -2.538, -0.075, -0.557, 3.459), (-0.08, -0.051, 0.0), 'm_grasp_descend') ee [ 0.2   -0.068  0.302] grasp 0.0 REJ
          76 +176 ('move', (0.2, -0.068, 0.305), None, 'lift') ee [ 0.2   -0.068  0.305] grasp 0.0 
          77 +177 ('move', (0.23, -0.09, 0.305), -3.14, 'travel') ee [ 0.23  -0.09   0.305] grasp 0.0 
          78 +178 ('move', (0.23, -0.09, 0.27), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.305] grasp 0.0 REJ
          79 +180 ('move', (0.23, -0.09, 0.27), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.295] grasp 0.0 REJ
          80 +181 ('move', (0.23, -0.09, 0.27), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.295] grasp 0.0 REJ
          81 +183 ('move', (0.23, -0.09, 0.27), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.293] grasp 0.0 REJ
          82 +184 ('move', (0.23, -0.09, 0.27), -3.14, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.293] grasp 0.0 REJ
          83 +185 ('move', (0.23, -0.09, 0.353), None, 'lift') ee [ 0.23  -0.09   0.294] grasp 0.0 
          84 +196 ('base', (-0.13, -0.055, 0.0)) ee [ 0.18  -0.09   0.353] grasp 0.0 
          85 +197 ('move', (0.18, -0.086, 0.305), 1.57, 'travel') ee [ 0.18  -0.088  0.348] grasp 0.0 
          86 +204 ('move', (0.18, -0.086, 0.266), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.305] grasp 0.0 REJ
          87 +206 ('move', (0.18, -0.086, 0.266), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.292] grasp 0.0 REJ
          88 +208 ('move', (0.18, -0.086, 0.266), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.285] grasp 0.0 REJ
          89 +210 ('move', (0.18, -0.086, 0.266), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.282] grasp 0.0 REJ
          90 +212 ('move', (0.18, -0.086, 0.266), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.28 ] grasp 0.0 REJ
          91 +213 ('move', (0.18, -0.086, 0.266), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.28 ] grasp 0.0 REJ
          92 +214 ('move', (0.18, -0.086, 0.34), None, 'lift') ee [ 0.18  -0.086  0.28 ] grasp 0.0 
          93 +225 ('move', (0.18, -0.086, 0.305), -3.14, 'travel') ee [ 0.18  -0.087  0.336] grasp 0.0 
          94 +233 ('move', (0.18, -0.086, 0.27), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.305] grasp 0.0 REJ
          95 +235 ('move', (0.18, -0.086, 0.27), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.292] grasp 0.0 REJ
          96 +236 ('move', (0.18, -0.086, 0.27), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.292] grasp 0.0 REJ
          97 +237 ('move', (0.18, -0.086, 0.27), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.292] grasp 0.0 REJ
          98 +238 ('move', (0.18, -0.086, 0.27), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.292] grasp 0.0 REJ
          99 +239 ('move', (0.18, -0.086, 0.352), None, 'lift') ee [ 0.18  -0.086  0.293] grasp 0.0 
         100 +250 ('move', (0.222, -0.046, 0.305), 2.36, 'travel') ee [ 0.189 -0.078  0.342] grasp 0.0 
         101 +255 ('move', (0.222, -0.046, 0.262), 2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.268] grasp 0.0 
         102 +257 None ee [ 0.222 -0.046  0.262] grasp 0.0 
         103 +258 ('move', (0.222, -0.046, 0.305), None, 'lift') ee [ 0.222 -0.046  0.299] grasp 0.0 
         104 +260 ('move', (0.222, -0.046, 0.305), -2.36, 'travel') ee [ 0.222 -0.046  0.305] grasp 0.0 
         105 +268 ('move', (0.222, -0.046, 0.258), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.305] grasp 0.0 REJ
         106 +269 ('move', (0.222, -0.046, 0.258), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.305] grasp 0.0 REJ
         107 +272 ('move', (0.222, -0.046, 0.258), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.293] grasp 0.0 REJ
         108 +273 ('move', (0.222, -0.046, 0.258), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.293] grasp 0.0 REJ
         109 +274 ('move', (0.222, -0.046, 0.258), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.293] grasp 0.0 REJ
         110 +275 ('move', (0.222, -0.046, 0.353), None, 'lift') ee [ 0.222 -0.046  0.294] grasp 0.0 
         111 +286 ('move', (0.216, -0.114, 0.305), -3.14, 'travel') ee [ 0.224 -0.07   0.337] grasp 0.0 
         112 +289 ('move', (0.216, -0.114, 0.265), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
         113 +290 ('move', (0.216, -0.114, 0.265), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
         114 +293 ('move', (0.216, -0.114, 0.265), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.293] grasp 0.0 REJ
         115 +294 ('move', (0.216, -0.114, 0.265), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.293] grasp 0.0 REJ
         116 +295 ('move', (0.216, -0.114, 0.265), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.293] grasp 0.0 REJ
         117 +296 ('move', (0.216, -0.114, 0.353), None, 'lift') ee [ 0.216 -0.114  0.294] grasp 0.0 
         118 +306 ('move', (0.161, -0.123, 0.305), -3.14, 'travel') ee [ 0.189 -0.122  0.328] grasp 0.0 
         119 +308 ('move', (0.161, -0.123, 0.264), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.305] grasp 0.0 REJ
         120 +310 ('move', (0.161, -0.123, 0.264), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.293] grasp 0.0 REJ
         121 +312 ('move', (0.161, -0.123, 0.264), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.286] grasp 0.0 REJ
         122 +314 ('move', (0.161, -0.123, 0.264), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.283] grasp 0.0 REJ
         123 +316 ('move', (0.161, -0.123, 0.264), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.281] grasp 0.0 REJ
         124 +317 ('move', (0.161, -0.123, 0.264), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.281] grasp 0.0 REJ
         125 +318 ('move', (0.161, -0.123, 0.341), None, 'lift') ee [ 0.161 -0.123  0.282] grasp 0.0 
         126 +329 ('base', (-0.137, -0.012, 0.0)) ee [ 0.111 -0.123  0.341] grasp 0.0 
         127 +330 ('move', (0.164, -0.056, 0.305), -2.36, 'travel') ee [ 0.142 -0.094  0.323] grasp 0.0 
         128 +332 ('move', (0.164, -0.056, 0.257), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
         129 +334 ('move', (0.164, -0.056, 0.257), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.292] grasp 0.0 REJ
         130 +336 ('move', (0.164, -0.056, 0.257), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.285] grasp 0.0 REJ
         131 +337 ('move', (0.164, -0.056, 0.257), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.285] grasp 0.0 REJ
         132 +338 ('move', (0.164, -0.056, 0.257), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.285] grasp 0.0 REJ
         133 +339 ('move', (0.164, -0.056, 0.345), None, 'lift') ee [ 0.164 -0.056  0.286] grasp 0.0 
         134 +350 ('move', (0.222, -0.046, 0.305), -3.14, 'travel') ee [ 0.177 -0.054  0.337] grasp 0.0 
         135 +355 ('move', (0.222, -0.046, 0.262), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.305] grasp 0.0 REJ
         136 +358 ('move', (0.222, -0.046, 0.262), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.273] grasp 0.0 REJ
         137 +359 ('move', (0.222, -0.046, 0.262), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.273] grasp 0.0 REJ
         138 +361 ('move', (0.222, -0.046, 0.262), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.27 ] grasp 0.0 REJ
         139 +362 ('move', (0.222, -0.046, 0.262), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.27 ] grasp 0.0 REJ
         140 +363 ('move', (0.222, -0.046, 0.33), None, 'lift') ee [ 0.222 -0.046  0.271] grasp 0.0 
         141 +373 ('move', (0.216, -0.114, 0.305), -2.36, 'travel') ee [ 0.221 -0.064  0.324] grasp 0.0 
         142 +377 ('move', (0.216, -0.114, 0.261), -2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
         143 +379 ('move', (0.216, -0.114, 0.261), -2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.292] grasp 0.0 REJ
         144 +380 ('move', (0.216, -0.114, 0.261), -2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.292] grasp 0.0 REJ
         145 +381 ('move', (0.216, -0.114, 0.261), -2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.292] grasp 0.0 REJ
         146 +382 ('move', (0.216, -0.114, 0.261), -2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.292] grasp 0.0 REJ
         147 +383 ('move', (0.216, -0.114, 0.352), None, 'lift') ee [ 0.216 -0.114  0.293] grasp 0.0 
         148 +394 ('base', (-0.136, -0.071, 0.0)) ee [ 0.166 -0.114  0.352] grasp 0.0 
         149 +395 ('move', (0.161, -0.123, 0.305), -2.36, 'travel') ee [ 0.165 -0.12   0.328] grasp 0.0 
         150 +397 ('move', (0.161, -0.123, 0.26), -2.36, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.305] grasp 0.0 REJ
         151 +398 ('move', (0.161, -0.123, 0.26), -2.36, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.305] grasp 0.0 REJ
         152 +401 ('move', (0.161, -0.123, 0.26), -2.36, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.294] grasp 0.0 REJ
         153 +402 ('move', (0.161, -0.123, 0.26), -2.36, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.294] grasp 0.0 REJ
         154 +403 ('move', (0.161, -0.123, 0.26), -2.36, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.294] grasp 0.0 REJ
         155 +404 ('move', (0.161, -0.123, 0.354), None, 'lift') ee [ 0.161 -0.123  0.295] grasp 0.0 
         156 +415 ('move', (0.147, -0.09, 0.305), -3.14, 'travel') ee [ 0.159 -0.115  0.341] grasp 0.0 
         157 +419 ('move', (0.147, -0.09, 0.282), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.305] grasp 0.0 REJ
         158 +421 ('move', (0.147, -0.09, 0.282), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.293] grasp 0.0 REJ
         159 +422 ('move', (0.147, -0.09, 0.282), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.293] grasp 0.0 REJ
         160 +423 ('move', (0.147, -0.09, 0.282), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.293] grasp 0.0 REJ
         161 +424 ('move', (0.147, -0.09, 0.282), -3.14, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.293] grasp 0.0 REJ
         162 +425 ('move', (0.147, -0.09, 0.353), None, 'lift') ee [ 0.147 -0.09   0.293] grasp 0.0 
         163 +436 ('move', (0.164, -0.056, 0.305), -3.14, 'travel') ee [ 0.157 -0.074  0.328] grasp 0.0 
         164 +438 ('move', (0.164, -0.056, 0.261), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
         165 +440 ('move', (0.164, -0.056, 0.261), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.293] grasp 0.0 REJ
         166 +443 ('move', (0.164, -0.056, 0.261), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.277] grasp 0.0 REJ
         167 +444 ('move', (0.164, -0.056, 0.261), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.277] grasp 0.0 REJ
         168 +446 ('move', (0.164, -0.056, 0.261), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.276] grasp 0.0 REJ
         169 +447 ('move', (0.164, -0.056, 0.261), -3.14, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.276] grasp 0.0 REJ
         170 +448 ('move', (0.164, -0.056, 0.336), None, 'lift') ee [ 0.164 -0.056  0.276] grasp 0.0 
         171 +459 ('move', (0.23, -0.09, 0.305), -1.57, 'travel') ee [ 0.172 -0.061  0.333] grasp 0.0 
         172 +466 ('move', (0.23, -0.09, 0.266), -1.57, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.305] grasp 0.0 REJ
         173 +468 ('move', (0.23, -0.09, 0.266), -1.57, 'grasp_descend', 'obstruction1') ee [ 0.23 -0.09  0.29] grasp 0.0 REJ
         174 +470 ('move', (0.23, -0.09, 0.266), -1.57, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.282] grasp 0.0 REJ
         175 +472 ('move', (0.23, -0.09, 0.266), -1.57, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.278] grasp 0.0 REJ
         176 +474 ('move', (0.23, -0.09, 0.266), -1.57, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.276] grasp 0.0 REJ
         177 +475 ('move', (0.23, -0.09, 0.266), -1.57, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.276] grasp 0.0 REJ
         178 +476 ('move', (0.23, -0.09, 0.336), None, 'lift') ee [ 0.23  -0.09   0.277] grasp 0.0 
         179 +487 ('move', (0.23, -0.09, 0.305), 0.0, 'travel') ee [ 0.23  -0.09   0.332] grasp 0.0 
         180 +495 ('move', (0.23, -0.09, 0.29), 0.0, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.305] grasp 0.0 REJ
         181 +496 ('move', (0.23, -0.09, 0.29), 0.0, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.305] grasp 0.0 REJ
         182 +498 ('move', (0.23, -0.09, 0.29), 0.0, 'grasp_descend', 'obstruction1') ee [ 0.23 -0.09  0.3 ] grasp 0.0 REJ
         183 +501 ('move', (0.23, -0.09, 0.29), 0.0, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.293] grasp 0.0 REJ
         184 +502 ('move', (0.23, -0.09, 0.29), 0.0, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.293] grasp 0.0 REJ
         185 +503 ('move', (0.23, -0.09, 0.353), None, 'lift') ee [ 0.23  -0.09   0.294] grasp 0.0 
         186 +512 ('move', (0.23, -0.09, 0.305), 0.79, 'travel') ee [ 0.23  -0.09   0.344] grasp 0.0 
         187 +517 ('move', (0.23, -0.09, 0.266), 0.79, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.305] grasp 0.0 REJ
         188 +519 ('move', (0.23, -0.09, 0.266), 0.79, 'grasp_descend', 'obstruction1') ee [ 0.23 -0.09  0.29] grasp 0.0 REJ
         189 +521 ('move', (0.23, -0.09, 0.266), 0.79, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.282] grasp 0.0 REJ
         190 +522 ('move', (0.23, -0.09, 0.266), 0.79, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.282] grasp 0.0 REJ
         191 +523 ('move', (0.23, -0.09, 0.266), 0.79, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.282] grasp 0.0 REJ
         192 +524 ('move', (0.23, -0.09, 0.342), None, 'lift') ee [ 0.23  -0.09   0.283] grasp 0.0 
         193 +534 ('move', (0.18, -0.086, 0.305), 1.57, 'travel') ee [ 0.222 -0.089  0.336] grasp 0.0 
         194 +539 ('move', (0.18, -0.086, 0.27), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.305] grasp 0.0 REJ
         195 +541 ('move', (0.18, -0.086, 0.27), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.29 ] grasp 0.0 REJ
         196 +543 ('move', (0.18, -0.086, 0.27), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.282] grasp 0.0 REJ
         197 +544 ('move', (0.18, -0.086, 0.27), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.282] grasp 0.0 REJ
         198 +546 ('move', (0.18, -0.086, 0.27), 1.57, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.28 ] grasp 0.0 REJ
         199 +547 ('move', (0.18, -0.086, 0.34), None, 'lift') ee [ 0.18  -0.086  0.281] grasp 0.0 
         200 +556 ('move', (0.23, -0.09, 0.305), 2.36, 'travel') ee [ 0.19  -0.088  0.334] grasp 0.0 
         201 +560 ('move', (0.23, -0.09, 0.266), 2.36, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.305] grasp 0.0 REJ
         202 +562 ('move', (0.23, -0.09, 0.266), 2.36, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.288] grasp 0.0 REJ
         203 +564 ('move', (0.23, -0.09, 0.266), 2.36, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.278] grasp 0.0 REJ
         204 +565 ('move', (0.23, -0.09, 0.266), 2.36, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.278] grasp 0.0 REJ
         205 +567 ('move', (0.23, -0.09, 0.266), 2.36, 'grasp_descend', 'obstruction1') ee [ 0.23  -0.09   0.276] grasp 0.0 REJ
         206 +568 ('move', (0.23, -0.09, 0.336), None, 'lift') ee [ 0.23  -0.09   0.277] grasp 0.0 
         207 +577 ('jmove', (0.581, 0.223, -3.595, -2.234, 0.149, -0.712, 9.449), (-0.218, -0.033, 0.0), 'm_grasp_descend') ee [ 0.22  -0.09   0.327] grasp 0.0 
         208 +580 ('jmove', (0.581, 0.223, -3.595, -2.234, 0.149, -0.712, 9.449), (-0.218, -0.033, 0.0), 'm_grasp_descend') ee [ 0.194 -0.088  0.302] grasp 0.0 REJ
         209 +581 ('move', (0.194, -0.088, 0.305), None, 'lift') ee [ 0.194 -0.088  0.305] grasp 0.0 
         210 +582 ('move', (0.18, -0.086, 0.305), -3.14, 'travel') ee [ 0.187 -0.087  0.305] grasp 0.0 
         211 +584 ('move', (0.18, -0.086, 0.291), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.305] grasp 0.0 REJ
         212 +585 ('move', (0.18, -0.086, 0.291), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.305] grasp 0.0 REJ
         213 +587 ('move', (0.18, -0.086, 0.291), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.299] grasp 0.0 REJ
         214 +589 ('move', (0.18, -0.086, 0.291), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.295] grasp 0.0 REJ
         215 +591 ('move', (0.18, -0.086, 0.291), -3.14, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.293] grasp 0.0 REJ
         216 +592 ('move', (0.18, -0.086, 0.353), None, 'lift') ee [ 0.18  -0.086  0.294] grasp 0.0 
         217 +601 ('move', (0.164, -0.056, 0.305), -1.57, 'travel') ee [ 0.179 -0.083  0.348] grasp 0.0 
         218 +609 ('move', (0.164, -0.056, 0.257), -1.57, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
         219 +610 ('move', (0.164, -0.056, 0.257), -1.57, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
         220 +612 ('move', (0.164, -0.056, 0.257), -1.57, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.299] grasp 0.0 REJ
         221 +614 ('move', (0.164, -0.056, 0.257), -1.57, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.295] grasp 0.0 REJ
         222 +616 ('move', (0.164, -0.056, 0.257), -1.57, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.293] grasp 0.0 REJ
         223 +617 ('move', (0.164, -0.056, 0.353), None, 'lift') ee [ 0.164 -0.056  0.294] grasp 0.0 
         224 +626 ('jmove', (0.661, 0.402, -3.876, -2.145, 0.403, -0.732, 11.397), (-0.219, -0.038, 0.044), 'm_grasp_descend') ee [ 0.184 -0.059  0.329] grasp 0.0 
         225 +628 ('jmove', (0.661, 0.402, -3.876, -2.145, 0.403, -0.732, 11.397), (-0.219, -0.038, 0.044), 'm_grasp_descend') ee [ 0.204 -0.056  0.303] grasp 0.0 REJ
         226 +629 ('move', (0.204, -0.056, 0.305), None, 'lift') ee [ 0.204 -0.056  0.305] grasp 0.0 
         227 +630 ('move', (0.222, -0.046, 0.305), -0.79, 'travel') ee [ 0.213 -0.051  0.305] grasp 0.0 
         228 +632 ('move', (0.222, -0.046, 0.274), -0.79, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.274] grasp 0.0 
         229 +633 None ee [ 0.222 -0.046  0.274] grasp 0.0 
         230 +634 ('move', (0.222, -0.046, 0.305), None, 'lift') ee [ 0.222 -0.046  0.305] grasp 0.0 
         231 +635 ('move', (0.161, -0.123, 0.305), -0.79, 'travel') ee [ 0.161 -0.123  0.305] grasp 0.0 
         232 +636 ('move', (0.161, -0.123, 0.26), -0.79, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.305] grasp 0.0 REJ
         233 +637 ('move', (0.161, -0.123, 0.26), -0.79, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.305] grasp 0.0 REJ
         234 +640 ('move', (0.161, -0.123, 0.26), -0.79, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.286] grasp 0.0 REJ
         235 +641 ('move', (0.161, -0.123, 0.26), -0.79, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.286] grasp 0.0 REJ
         236 +642 ('move', (0.161, -0.123, 0.26), -0.79, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.286] grasp 0.0 REJ
         237 +643 ('move', (0.161, -0.123, 0.346), None, 'lift') ee [ 0.161 -0.123  0.287] grasp 0.0 
         238 +653 ('move', (0.147, -0.09, 0.305), 0.79, 'travel') ee [ 0.16 -0.12  0.34] grasp 0.0 
         239 +659 ('move', (0.147, -0.09, 0.262), 0.79, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.305] grasp 0.0 REJ
         240 +661 ('move', (0.147, -0.09, 0.262), 0.79, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.283] grasp 0.0 REJ
         241 +663 ('move', (0.147, -0.09, 0.262), 0.79, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.271] grasp 0.0 REJ
         242 +664 ('move', (0.147, -0.09, 0.262), 0.79, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.271] grasp 0.0 REJ
         243 +665 ('move', (0.147, -0.09, 0.262), 0.79, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.271] grasp 0.0 REJ
         244 +666 ('move', (0.147, -0.09, 0.331), None, 'lift') ee [ 0.147 -0.09   0.272] grasp 0.0 
         245 +675 ('move', (0.161, -0.123, 0.305), 1.57, 'travel') ee [ 0.149 -0.096  0.326] grasp 0.0 
         246 +679 ('move', (0.161, -0.123, 0.26), 1.57, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.305] grasp 0.0 REJ
         247 +680 ('move', (0.161, -0.123, 0.26), 1.57, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.305] grasp 0.0 REJ
         248 +682 ('move', (0.161, -0.123, 0.26), 1.57, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.297] grasp 0.0 REJ
         249 +684 ('move', (0.161, -0.123, 0.26), 1.57, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.293] grasp 0.0 REJ
         250 +685 ('move', (0.161, -0.123, 0.26), 1.57, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.293] grasp 0.0 REJ
         251 +686 ('move', (0.161, -0.123, 0.353), None, 'lift') ee [ 0.161 -0.123  0.294] grasp 0.0 
         252 +695 ('jmove', (0.819, 0.666, -4.374, -2.2, 0.847, -0.891, 13.159), (-0.205, -0.07, 0.03), 'm_grasp_descend') ee [ 0.18  -0.106  0.329] grasp 0.0 
         253 +697 ('jmove', (0.819, 0.666, -4.374, -2.2, 0.847, -0.891, 13.159), (-0.205, -0.07, 0.03), 'm_grasp_descend') ee [ 0.204 -0.077  0.293] grasp 0.0 REJ
         254 +698 ('move', (0.204, -0.077, 0.305), None, 'lift') ee [ 0.204 -0.077  0.305] grasp 0.0 
         255 +699 ('move', (0.222, -0.046, 0.305), 1.57, 'travel') ee [ 0.222 -0.046  0.305] grasp 0.0 
         256 +700 ('move', (0.222, -0.046, 0.258), 1.57, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.305] grasp 0.0 REJ
         257 +701 ('move', (0.222, -0.046, 0.258), 1.57, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.305] grasp 0.0 REJ
         258 +703 ('move', (0.222, -0.046, 0.258), 1.57, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.298] grasp 0.0 REJ
         259 +705 ('move', (0.222, -0.046, 0.258), 1.57, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.295] grasp 0.0 REJ
         260 +707 ('move', (0.222, -0.046, 0.258), 1.57, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.293] grasp 0.0 REJ
         261 +708 ('move', (0.222, -0.046, 0.353), None, 'lift') ee [ 0.222 -0.046  0.294] grasp 0.0 
         262 +717 ('jmove', (0.94, 0.784, -4.651, -2.296, 0.953, -1.045, 13.734), (-0.209, -0.108, 0.03), 'm_grasp_descend') ee [ 0.214 -0.059  0.329] grasp 0.0 
         263 +719 ('jmove', (0.94, 0.784, -4.651, -2.296, 0.953, -1.045, 13.734), (-0.209, -0.108, 0.03), 'm_grasp_descend') ee [ 0.198 -0.074  0.296] grasp 0.0 REJ
         264 +720 ('move', (0.198, -0.074, 0.305), None, 'lift') ee [ 0.198 -0.074  0.305] grasp 0.0 
         265 +721 ('move', (0.18, -0.086, 0.305), 2.36, 'travel') ee [ 0.189 -0.08   0.305] grasp 0.0 
         266 +723 ('move', (0.18, -0.086, 0.266), 2.36, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.305] grasp 0.0 REJ
         267 +725 ('move', (0.18, -0.086, 0.266), 2.36, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.285] grasp 0.0 REJ
         268 +726 ('move', (0.18, -0.086, 0.266), 2.36, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.285] grasp 0.0 REJ
         269 +728 ('move', (0.18, -0.086, 0.266), 2.36, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.281] grasp 0.0 REJ
         270 +729 ('move', (0.18, -0.086, 0.266), 2.36, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.281] grasp 0.0 REJ
         271 +730 ('move', (0.18, -0.086, 0.341), None, 'lift') ee [ 0.18  -0.086  0.282] grasp 0.0 
         272 +740 ('jmove', (0.94, 0.777, -4.626, -2.303, 0.96, -1.022, 13.743), (-0.242, -0.109, 0.03), 'm_grasp_descend') ee [ 0.167 -0.089  0.301] grasp 0.0 
         273 +741 ('jmove', (0.94, 0.777, -4.626, -2.303, 0.96, -1.022, 13.743), (-0.242, -0.109, 0.03), 'm_grasp_descend') ee [ 0.167 -0.089  0.301] grasp 0.0 REJ
         274 +742 ('move', (0.167, -0.089, 0.305), None, 'lift') ee [ 0.167 -0.089  0.305] grasp 0.0 
         275 +743 ('move', (0.147, -0.09, 0.305), 2.36, 'travel') ee [ 0.147 -0.09   0.305] grasp 0.0 
         276 +744 ('move', (0.147, -0.09, 0.262), 2.36, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.305] grasp 0.0 REJ
         277 +746 ('move', (0.147, -0.09, 0.262), 2.36, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.289] grasp 0.0 REJ
         278 +748 ('move', (0.147, -0.09, 0.262), 2.36, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.28 ] grasp 0.0 REJ
         279 +749 ('move', (0.147, -0.09, 0.262), 2.36, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.28 ] grasp 0.0 REJ
         280 +750 ('move', (0.147, -0.09, 0.262), 2.36, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.28 ] grasp 0.0 REJ
         281 +751 ('move', (0.147, -0.09, 0.34), None, 'lift') ee [ 0.147 -0.09   0.281] grasp 0.0 
         282 +761 ('move', (0.164, -0.056, 0.305), 2.36, 'travel') ee [ 0.164 -0.056  0.305] grasp 0.0 
         283 +762 ('move', (0.164, -0.056, 0.257), 2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
         284 +763 ('move', (0.164, -0.056, 0.257), 2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
         285 +765 ('move', (0.164, -0.056, 0.257), 2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.299] grasp 0.0 REJ
         286 +767 ('move', (0.164, -0.056, 0.257), 2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.295] grasp 0.0 REJ
         287 +769 ('move', (0.164, -0.056, 0.257), 2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.293] grasp 0.0 REJ
         288 +770 ('move', (0.164, -0.056, 0.353), None, 'lift') ee [ 0.164 -0.056  0.294] grasp 0.0 
         289 +779 ('move', (0.147, -0.09, 0.305), 1.57, 'travel') ee [ 0.162 -0.061  0.342] grasp 0.0 
         290 +783 ('move', (0.147, -0.09, 0.262), 1.57, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.305] grasp 0.0 REJ
         291 +785 ('move', (0.147, -0.09, 0.262), 1.57, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.29 ] grasp 0.0 REJ
         292 +787 ('move', (0.147, -0.09, 0.262), 1.57, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.282] grasp 0.0 REJ
         293 +788 ('move', (0.147, -0.09, 0.262), 1.57, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.282] grasp 0.0 REJ
         294 +790 ('move', (0.147, -0.09, 0.262), 1.57, 'grasp_descend', 'obstruction4') ee [ 0.147 -0.09   0.28 ] grasp 0.0 REJ
         295 +791 ('move', (0.147, -0.09, 0.34), None, 'lift') ee [ 0.147 -0.09   0.281] grasp 0.0 
         296 +800 ('move', (0.18, -0.086, 0.305), 0.79, 'travel') ee [ 0.154 -0.088  0.331] grasp 0.0 
         297 +804 ('move', (0.18, -0.086, 0.266), 0.79, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.305] grasp 0.0 REJ
         298 +806 ('move', (0.18, -0.086, 0.266), 0.79, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.291] grasp 0.0 REJ
         299 +808 ('move', (0.18, -0.086, 0.266), 0.79, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.283] grasp 0.0 REJ
         300 +809 ('move', (0.18, -0.086, 0.266), 0.79, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.283] grasp 0.0 REJ
         301 +811 ('move', (0.18, -0.086, 0.266), 0.79, 'grasp_descend', 'obstruction2') ee [ 0.18  -0.086  0.281] grasp 0.0 REJ
         302 +812 ('move', (0.18, -0.086, 0.341), None, 'lift') ee [ 0.18  -0.086  0.283] grasp 0.0 
         303 +822 ('move', (0.216, -0.114, 0.305), 1.57, 'travel') ee [ 0.191 -0.097  0.33 ] grasp 0.0 
         304 +825 ('move', (0.216, -0.114, 0.261), 1.57, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
         305 +827 ('move', (0.216, -0.114, 0.261), 1.57, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.29 ] grasp 0.0 REJ
         306 +829 ('move', (0.216, -0.114, 0.261), 1.57, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.282] grasp 0.0 REJ
         307 +831 ('move', (0.216, -0.114, 0.261), 1.57, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.278] grasp 0.0 REJ
         308 +833 ('move', (0.216, -0.114, 0.261), 1.57, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.276] grasp 0.0 REJ
         309 +834 ('move', (0.216, -0.114, 0.261), 1.57, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.276] grasp 0.0 REJ
         310 +835 ('move', (0.216, -0.114, 0.336), None, 'lift') ee [ 0.216 -0.114  0.277] grasp 0.0 
         311 +846 ('move', (0.216, -0.114, 0.305), 2.36, 'travel') ee [ 0.215 -0.115  0.326] grasp 0.0 
         312 +849 ('move', (0.216, -0.114, 0.261), 2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
         313 +850 ('move', (0.216, -0.114, 0.261), 2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
         314 +852 ('move', (0.216, -0.114, 0.261), 2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.298] grasp 0.0 REJ
         315 +854 ('move', (0.216, -0.114, 0.261), 2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.295] grasp 0.0 REJ
         316 +855 ('move', (0.216, -0.114, 0.261), 2.36, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.295] grasp 0.0 REJ
         317 +856 ('move', (0.216, -0.114, 0.355), None, 'lift') ee [ 0.216 -0.114  0.295] grasp 0.0 
         318 +866 ('move', (0.222, -0.046, 0.305), -2.36, 'travel') ee [ 0.217 -0.106  0.348] grasp 0.0 
         319 +871 ('move', (0.222, -0.046, 0.262), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.305] grasp 0.0 REJ
         320 +872 ('move', (0.222, -0.046, 0.262), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.305] grasp 0.0 REJ
         321 +874 ('move', (0.222, -0.046, 0.262), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.296] grasp 0.0 REJ
         322 +875 ('move', (0.222, -0.046, 0.262), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.296] grasp 0.0 REJ
         323 +877 ('move', (0.222, -0.046, 0.262), -2.36, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.294] grasp 0.0 REJ
         324 +878 ('move', (0.222, -0.046, 0.354), None, 'lift') ee [ 0.222 -0.046  0.295] grasp 0.0 
         325 +887 ('jmove', (0.959, 0.982, -4.901, -2.313, 1.009, -1.308, 14.474), (-0.158, -0.082, -0.102), 'm_grasp_descend') ee [ 0.225 -0.056  0.341] grasp 0.0 
         326 +890 ('jmove', (0.959, 0.982, -4.901, -2.313, 1.009, -1.308, 14.474), (-0.158, -0.082, -0.102), 'm_grasp_descend') ee [ 0.224 -0.092  0.302] grasp 0.0 REJ
         327 +891 ('move', (0.224, -0.092, 0.305), None, 'lift') ee [ 0.224 -0.092  0.305] grasp 0.0 
         328 +892 ('move', (0.216, -0.114, 0.305), -3.14, 'travel') ee [ 0.22  -0.103  0.305] grasp 0.0 
         329 +894 ('move', (0.216, -0.114, 0.28), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
         330 +895 ('move', (0.216, -0.114, 0.28), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.305] grasp 0.0 REJ
         331 +897 ('move', (0.216, -0.114, 0.28), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.296] grasp 0.0 REJ
         332 +899 ('move', (0.216, -0.114, 0.28), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.292] grasp 0.0 REJ
         333 +900 ('move', (0.216, -0.114, 0.28), -3.14, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.292] grasp 0.0 REJ
         334 +901 ('move', (0.216, -0.114, 0.352), None, 'lift') ee [ 0.216 -0.114  0.293] grasp 0.0 
         335 +910 ('jmove', (0.955, 0.975, -4.892, -2.318, 1.009, -1.294, 14.478), (-0.212, -0.091, -0.108), 'm_grasp_descend') ee [ 0.201 -0.118  0.327] grasp 0.0 
         336 +911 ('jmove', (0.955, 0.975, -4.892, -2.318, 1.009, -1.294, 14.478), (-0.212, -0.091, -0.108), 'm_grasp_descend') ee [ 0.201 -0.118  0.327] grasp 0.0 REJ
         337 +912 ('move', (0.201, -0.118, 0.327), None, 'lift') ee [ 0.201 -0.118  0.327] grasp 0.0 
         338 +913 ('move', (0.161, -0.123, 0.305), -3.14, 'travel') ee [ 0.161 -0.123  0.305] grasp 0.0 
         339 +914 ('move', (0.161, -0.123, 0.278), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.305] grasp 0.0 REJ
         340 +916 ('move', (0.161, -0.123, 0.278), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.292] grasp 0.0 REJ
         341 +918 ('move', (0.161, -0.123, 0.278), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.285] grasp 0.0 REJ
         342 +920 ('move', (0.161, -0.123, 0.278), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.282] grasp 0.0 REJ
         343 +921 ('move', (0.161, -0.123, 0.278), -3.14, 'grasp_descend', 'obstruction7') ee [ 0.161 -0.123  0.282] grasp 0.0 REJ
         344 +922 ('move', (0.161, -0.123, 0.342), None, 'lift') ee [ 0.161 -0.123  0.283] grasp 0.0 
         345 +932 ('jmove', (0.889, 1.135, -4.931, -2.32, 1.107, -1.427, 14.895), (-0.214, -0.121, 0.152), 'm_grasp_descend') ee [ 0.167 -0.104  0.315] grasp 0.0 
         346 +934 ('jmove', (0.889, 1.135, -4.931, -2.32, 1.107, -1.427, 14.895), (-0.214, -0.121, 0.152), 'm_grasp_descend') ee [ 0.169 -0.081  0.288] grasp 0.0 REJ
         347 +935 ('move', (0.169, -0.081, 0.305), None, 'lift') ee [ 0.169 -0.081  0.305] grasp 0.0 
         348 +936 ('move', (0.164, -0.056, 0.305), -2.36, 'travel') ee [ 0.167 -0.068  0.305] grasp 0.0 
         349 +938 ('move', (0.164, -0.056, 0.261), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
         350 +939 ('move', (0.164, -0.056, 0.261), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.305] grasp 0.0 REJ
         351 +941 ('move', (0.164, -0.056, 0.261), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.296] grasp 0.0 REJ
         352 +944 ('move', (0.164, -0.056, 0.261), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.284] grasp 0.0 REJ
         353 +945 ('move', (0.164, -0.056, 0.261), -2.36, 'grasp_descend', 'obstruction3') ee [ 0.164 -0.056  0.284] grasp 0.0 REJ
         354 +946 ('move', (0.164, -0.056, 0.344), None, 'lift') ee [ 0.164 -0.056  0.286] grasp 0.0 
         355 +954 ('move', (0.222, -0.046, 0.305), -3.14, 'travel') ee [ 0.172 -0.052  0.339] grasp 0.0 
         356 +958 ('move', (0.222, -0.046, 0.274), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.222 -0.046  0.274] grasp 0.0 
         357 +959 None ee [ 0.222 -0.046  0.274] grasp 1.0 
         358 +960 ('move', (0.222, -0.046, 0.339), -3.14, 'lift') ee [ 0.222 -0.046  0.339] grasp 1.0 
         359 +961 ('jmove', (0.924, 0.969, -4.724, -2.187, 1.055, -1.246, 14.365), (-0.213, 0.008, 0.163), 'm_place_descend') ee [0.21  0.075 0.266] grasp 1.0 
         360 +962 None ee [0.21  0.075 0.266] grasp 0.0 
         361 +963 ('move', (0.21, 0.075, 0.305), None, 'lift') ee [0.21  0.075 0.305] grasp 0.0 
         362 +964 ('jmove', (0.927, 0.959, -4.724, -2.183, 1.045, -1.243, 14.374), (-0.259, -0.122, 0.163), 'm_grasp_descend') ee [ 0.164 -0.056  0.268] grasp 0.0 
         363 +965 None ee [ 0.164 -0.056  0.268] grasp 1.0 
         364 +966 ('move', (0.164, -0.056, 0.333), -3.14, 'lift') ee [ 0.164 -0.056  0.333] grasp 1.0 
         365 +967 ('jmove', (0.918, 0.952, -4.685, -2.195, 1.059, -1.206, 14.374), (-0.138, -0.292, 0.163), 'm_place_descend') ee [ 0.164 -0.056  0.333] grasp 1.0 REJ
         366 +968 ('move', (0.335, 0.1, 0.333), -3.14, 'travel') ee [ 0.188 -0.034  0.333] grasp 1.0 
         367 +973 ('move', (0.335, 0.1, 0.26), -3.14, 'place_descend') ee [0.335 0.1   0.26 ] grasp 1.0 
         368 +974 None ee [0.335 0.1   0.26 ] grasp 0.0 
         369 +975 ('move', (0.335, 0.1, 0.305), None, 'lift') ee [0.335 0.1   0.305] grasp 0.0 
         370 +976 ('move', (0.23, -0.09, 0.305), 2.36, 'travel') ee [0.314 0.028 0.307] grasp 0.0 
         371 +979 ('move', (0.23, -0.09, 0.27), 2.36, 'grasp_descend', 'obstruction1') ee [ 0.23 -0.09  0.27] grasp 0.0 
         372 +980 None ee [ 0.23 -0.09  0.27] grasp 1.0 
         373 +981 ('move', (0.23, -0.09, 0.335), 2.36, 'lift') ee [ 0.23 -0.09  0.27] grasp 1.0 REJ
         374 +984 ('jmove', (0.855, 0.997, -4.566, -1.922, 1.058, -1.264, 14.283), (-0.1, -0.047, -0.304), 'm_place_descend') ee [ 0.385 -0.225  0.261] grasp 1.0 
         375 +985 None ee [ 0.385 -0.225  0.261] grasp 0.0 
         376 +986 ('move', (0.385, -0.225, 0.305), None, 'lift') ee [ 0.385 -0.225  0.305] grasp 0.0 
         377 +987 ('move', (0.216, -0.114, 0.305), 1.57, 'travel') ee [ 0.329 -0.197  0.313] grasp 0.0 
         378 +990 ('move', (0.216, -0.114, 0.265), 1.57, 'grasp_descend', 'obstruction0') ee [ 0.216 -0.114  0.265] grasp 0.0 
         379 +991 None ee [ 0.216 -0.114  0.265] grasp 1.0 
         380 +992 ('move', (0.216, -0.114, 0.33), 1.57, 'lift') ee [ 0.216 -0.114  0.319] grasp 1.0 
         381 +994 ('move', (0.185, -0.25, 0.33), 1.57, 'travel') ee [ 0.185 -0.25   0.33 ] grasp 1.0 
         382 +995 ('move', (0.185, -0.25, 0.256), 1.57, 'place_descend') ee [ 0.185 -0.25   0.285] grasp 1.0 
         383 +997 None ee [ 0.185 -0.25   0.256] grasp 0.0 
         384 +998 ('move', (0.185, -0.25, 0.305), None, 'lift') ee [ 0.185 -0.25   0.305] grasp 0.0 
         385 +999 ('move', (0.18, -0.086, 0.305), 2.36, 'travel') ee [ 0.187 -0.166  0.305] grasp 0.0 
diff --git a/d112.txt b/d112.txt
new file mode 100644
index 0000000..41837a2
--- /dev/null
+++ b/d112.txt
@@ -0,0 +1,982 @@
           1 +obstruction0 {'x': 0.408, 'y': 0.377, 'z': 0.101, 'hx': 0.017, 'hy': 0.01, 'hz': 0.026, 'g': 0.0, 'yaw': 0.0}
           2 +obstruction1 {'x': 0.109, 'y': -0.318, 'z': 0.115, 'hx': 0.012, 'hy': 0.018, 'hz': 0.03, 'g': 0.0, 'yaw': 0.0}
           3 +obstruction2 {'x': 0.151, 'y': -0.313, 'z': 0.096, 'hx': 0.018, 'hy': 0.012, 'hz': 0.011, 'g': 0.0, 'yaw': 0.0}
           4 +obstruction3 {'x': 0.112, 'y': -0.276, 'z': 0.111, 'hx': 0.02, 'hy': 0.02, 'hz': 0.026, 'g': 0.0, 'yaw': 0.0}
           5 +obstruction4 {'x': 0.152, 'y': -0.343, 'z': 0.11, 'hx': 0.018, 'hy': 0.015, 'hz': 0.025, 'g': 0.0, 'yaw': 0.0}
           6 +obstruction5 {'x': 0.156, 'y': -0.253, 'z': 0.102, 'hx': 0.015, 'hy': 0.01, 'hz': 0.017, 'g': 0.0, 'yaw': 0.0}
           7 +obstruction6 {'x': 0.287, 'y': -0.03, 'z': 0.096, 'hx': 0.016, 'hy': 0.012, 'hz': 0.021, 'g': 0.0, 'yaw': 0.0}
           8 +obstruction7 {'x': 0.155, 'y': -0.284, 'z': 0.101, 'hx': 0.019, 'hy': 0.012, 'hz': 0.016, 'g': 0.0, 'yaw': 0.0}
           9 +obstruction8 {'x': 0.251, 'y': -0.287, 'z': 0.1, 'hx': 0.015, 'hy': 0.017, 'hz': 0.025, 'g': 0.0, 'yaw': 0.0}
          10 +obstruction9 {'x': 0.413, 'y': -0.258, 'z': 0.097, 'hx': 0.016, 'hy': 0.012, 'hz': 0.022, 'g': 0.0, 'yaw': 0.0}
          11 +target_block {'x': 0.419, 'y': -0.173, 'z': 0.1, 'hx': 0.019, 'hy': 0.036, 'hz': 0.025, 'g': 0.0, 'yaw': 0.0}
          12 +target_region {'x': 0.13, 'y': -0.3, 'z': 0.08, 'hx': 0.023, 'hy': 0.045, 'hz': 0.005, 'g': 0.0, 'yaw': 0.0}
          13 +0 ('move', (0.139, 0.001, 0.342), None, 'lift') ee [0.139 0.001 0.342] grasp 0.0 
          14 +1 ('jmove', (0.33, 0.083, -2.579, -2.411, -0.072, -0.661, 1.734), (-0.12, -0.172, 0.0), 'm_grasp_descend') ee [ 0.164 -0.104  0.327] grasp 0.0 
          15 +4 None ee [ 0.152 -0.343  0.288] grasp 1.0 
          16 +5 ('move', (0.152, -0.343, 0.359), 0.79, 'lift') ee [ 0.152 -0.343  0.332] grasp 1.0 
          17 +7 ('move', (0.285, -0.175, 0.359), 0.79, 'travel') ee [ 0.285 -0.175  0.359] grasp 1.0 
          18 +8 ('move', (0.285, -0.175, 0.279), 0.79, 'place_descend') ee [ 0.285 -0.175  0.306] grasp 1.0 
          19 +10 None ee [ 0.285 -0.175  0.279] grasp 0.0 
          20 +11 ('move', (0.285, -0.175, 0.311), None, 'lift') ee [ 0.285 -0.175  0.311] grasp 0.0 
          21 +12 ('jmove', (0.392, 0.212, -2.424, -2.24, -0.204, -0.752, 1.247), (-0.168, -0.075, 0.0), 'm_grasp_descend') ee [ 0.2   -0.251  0.304] grasp 0.0 
          22 +14 None ee [ 0.109 -0.318  0.297] grasp 1.0 
          23 +15 ('move', (0.109, -0.318, 0.361), 0.0, 'lift') ee [ 0.109 -0.318  0.352] grasp 1.0 
          24 +17 ('move', (0.16, -0.15, 0.361), 0.0, 'travel') ee [ 0.16  -0.15   0.361] grasp 1.0 
          25 +18 ('move', (0.16, -0.15, 0.289), 0.0, 'place_descend') ee [ 0.16  -0.15   0.306] grasp 1.0 
          26 +20 None ee [ 0.16  -0.15   0.289] grasp 0.0 
          27 +21 ('move', (0.16, -0.15, 0.304), None, 'lift') ee [ 0.16  -0.15   0.304] grasp 0.0 
          28 +22 ('jmove', (0.439, 0.327, -2.441, -2.302, -0.365, -0.618, 1.415), (-0.126, -0.071, 0.0), 'm_grasp_descend') ee [ 0.16  -0.15   0.304] grasp 0.0 REJ
          29 +23 ('move', (0.151, -0.313, 0.304), 0.0, 'travel') ee [ 0.159 -0.168  0.304] grasp 0.0 
          30 +27 ('move', (0.151, -0.313, 0.257), 0.0, 'grasp_descend', 'obstruction2') ee [ 0.151 -0.313  0.257] grasp 0.0 
          31 +28 None ee [ 0.151 -0.313  0.257] grasp 1.0 
          32 +29 ('move', (0.151, -0.313, 0.321), -0.0, 'lift') ee [ 0.151 -0.313  0.321] grasp 1.0 
          33 +30 ('move', (0.41, 0.0, 0.321), -0.0, 'travel') ee [ 0.233 -0.223  0.324] grasp 1.0 
          34 +33 ('move', (0.41, 0.0, 0.249), -0.0, 'place_descend') ee [0.41  0.    0.248] grasp 1.0 
          35 +34 None ee [0.41  0.    0.248] grasp 0.0 
          36 +35 ('move', (0.41, 0.0, 0.304), None, 'lift') ee [0.41  0.    0.304] grasp 0.0 
          37 +36 ('move', (0.112, -0.276, 0.304), 1.57, 'travel') ee [ 0.367 -0.04   0.302] grasp 0.0 
          38 +43 ('move', (0.112, -0.276, 0.266), 1.57, 'grasp_descend', 'obstruction3') ee [ 0.112 -0.276  0.266] grasp 0.0 
          39 +44 None ee [ 0.112 -0.276  0.266] grasp 1.0 
          40 +45 ('move', (0.112, -0.276, 0.329), 1.57, 'lift') ee [ 0.112 -0.276  0.329] grasp 1.0 
          41 +46 ('move', (0.26, 0.1, 0.329), 1.57, 'travel') ee [ 0.186 -0.088  0.329] grasp 1.0 
          42 +47 ('move', (0.26, 0.1, 0.329), 1.57, 'travel') ee [0.26  0.1   0.329] grasp 1.0 
          43 +48 ('move', (0.26, 0.1, 0.257), 1.57, 'place_descend') ee [0.26  0.1   0.257] grasp 1.0 
          44 +49 None ee [0.26  0.1   0.257] grasp 0.0 
          45 +50 ('move', (0.26, 0.1, 0.303), None, 'lift') ee [0.26  0.1   0.303] grasp 0.0 
          46 +51 ('base', (-0.23, 0.405, 0.0)) ee [0.26  0.    0.303] grasp 0.0 
          47 +52 ('move', (0.156, -0.253, 0.303), -3.14, 'travel') ee [ 0.245 -0.036  0.301] grasp 0.0 
          48 +59 ('move', (0.156, -0.253, 0.257), -3.14, 'grasp_descend', 'obstruction5') ee [ 0.156 -0.253  0.257] grasp 0.0 
          49 +60 None ee [ 0.156 -0.253  0.257] grasp 1.0 
          50 +61 ('move', (0.156, -0.253, 0.32), -3.14, 'lift') ee [ 0.156 -0.253  0.32 ] grasp 1.0 
          51 +62 ('move', (0.385, 0.125, 0.32), -3.14, 'travel') ee [ 0.271 -0.064  0.32 ] grasp 1.0 
          52 +63 ('move', (0.385, 0.125, 0.32), -3.14, 'travel') ee [0.385 0.125 0.32 ] grasp 1.0 
          53 +64 ('move', (0.385, 0.125, 0.249), -3.14, 'place_descend') ee [0.385 0.125 0.249] grasp 1.0 
          54 +65 None ee [0.385 0.125 0.249] grasp 0.0 
          55 +66 ('move', (0.385, 0.125, 0.303), None, 'lift') ee [0.385 0.125 0.303] grasp 0.0 
          56 +67 ('base', (-0.105, 0.33, 0.0)) ee [ 0.385 -0.075  0.303] grasp 0.0 
          57 +68 ('move', (0.155, -0.284, 0.303), -1.57, 'travel') ee [ 0.352 -0.104  0.301] grasp 0.0 
          58 +75 ('move', (0.155, -0.284, 0.257), -1.57, 'grasp_descend', 'obstruction7') ee [ 0.155 -0.284  0.257] grasp 0.0 
          59 +76 None ee [ 0.155 -0.284  0.257] grasp 1.0 
          60 +77 ('move', (0.155, -0.284, 0.32), -1.57, 'lift') ee [ 0.155 -0.284  0.32 ] grasp 1.0 
          61 +78 ('jmove', (1.085, 0.821, -3.621, -1.381, 0.403, -1.037, 5.243), (-0.335, 0.18, 0.0), 'm_place_descend') ee [ 0.16  -0.225  0.248] grasp 1.0 
          62 +79 None ee [ 0.16  -0.225  0.248] grasp 0.0 
          63 +80 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          64 +81 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          65 +82 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          66 +83 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          67 +84 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          68 +85 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          69 +86 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          70 +87 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          71 +88 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          72 +89 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          73 +90 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          74 +91 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          75 +92 ('base', (-0.376, 0.229, -0.036)) ee [ 0.16  -0.225  0.248] grasp 0.0 
          76 +93 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          77 +94 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          78 +95 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          79 +96 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          80 +97 ('base', (-0.388, 0.18, 0.02)) ee [ 0.16  -0.225  0.248] grasp 0.0 
          81 +98 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          82 +99 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          83 +100 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          84 +101 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          85 +102 ('base', (-0.345, 0.166, 0.041)) ee [ 0.16  -0.225  0.248] grasp 0.0 
          86 +103 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          87 +104 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          88 +105 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          89 +106 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          90 +107 ('base', (-0.345, 0.146, 0.012)) ee [ 0.16  -0.225  0.248] grasp 0.0 
          91 +108 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          92 +109 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          93 +110 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          94 +111 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          95 +112 ('base', (-0.378, 0.177, -0.076)) ee [ 0.16  -0.225  0.248] grasp 0.0 
          96 +113 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          97 +114 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          98 +115 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
          99 +116 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         100 +117 ('base', (-0.354, 0.195, -0.074)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         101 +118 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         102 +119 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         103 +120 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         104 +121 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         105 +122 ('base', (-0.366, 0.154, -0.086)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         106 +123 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         107 +124 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         108 +125 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         109 +126 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         110 +127 ('base', (-0.392, 0.181, 0.004)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         111 +128 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         112 +129 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         113 +130 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         114 +131 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         115 +132 ('base', (-0.386, 0.188, -0.025)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         116 +133 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         117 +134 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         118 +135 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         119 +136 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         120 +137 ('base', (-0.375, 0.176, 0.087)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         121 +138 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         122 +139 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         123 +140 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         124 +141 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         125 +142 ('base', (-0.366, 0.155, 0.044)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         126 +143 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         127 +144 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         128 +145 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         129 +146 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         130 +147 ('base', (-0.338, 0.207, -0.075)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         131 +148 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         132 +149 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         133 +150 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         134 +151 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         135 +152 ('base', (-0.388, 0.156, -0.019)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         136 +153 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         137 +154 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         138 +155 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         139 +156 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         140 +157 ('base', (-0.351, 0.206, -0.007)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         141 +158 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         142 +159 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         143 +160 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         144 +161 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         145 +162 ('base', (-0.348, 0.214, 0.01)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         146 +163 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         147 +164 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         148 +165 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         149 +166 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         150 +167 ('base', (-0.395, 0.202, -0.034)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         151 +168 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         152 +169 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         153 +170 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         154 +171 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         155 +172 ('base', (-0.352, 0.132, 0.096)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         156 +173 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         157 +174 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         158 +175 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         159 +176 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         160 +177 ('base', (-0.36, 0.213, -0.077)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         161 +178 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         162 +179 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         163 +180 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         164 +181 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         165 +182 ('base', (-0.359, 0.205, 0.056)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         166 +183 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         167 +184 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         168 +185 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         169 +186 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         170 +187 ('base', (-0.392, 0.182, -0.025)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         171 +188 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         172 +189 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         173 +190 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         174 +191 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         175 +192 ('base', (-0.366, 0.215, 0.035)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         176 +193 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         177 +194 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         178 +195 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         179 +196 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         180 +197 ('base', (-0.38, 0.183, 0.052)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         181 +198 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         182 +199 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         183 +200 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         184 +201 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         185 +202 ('base', (-0.342, 0.182, 0.035)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         186 +203 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         187 +204 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         188 +205 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         189 +206 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         190 +207 ('base', (-0.348, 0.186, -0.051)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         191 +208 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         192 +209 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         193 +210 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         194 +211 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         195 +212 ('base', (-0.351, 0.132, -0.093)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         196 +213 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         197 +214 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         198 +215 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         199 +216 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         200 +217 ('base', (-0.376, 0.135, 0.026)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         201 +218 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         202 +219 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         203 +220 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         204 +221 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         205 +222 ('base', (-0.358, 0.148, 0.023)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         206 +223 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         207 +224 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         208 +225 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         209 +226 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         210 +227 ('base', (-0.361, 0.207, 0.046)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         211 +228 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         212 +229 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         213 +230 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         214 +231 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         215 +232 ('base', (-0.359, 0.138, -0.03)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         216 +233 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         217 +234 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         218 +235 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         219 +236 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         220 +237 ('base', (-0.363, 0.222, -0.055)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         221 +238 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         222 +239 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         223 +240 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         224 +241 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         225 +242 ('base', (-0.339, 0.216, -0.086)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         226 +243 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         227 +244 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         228 +245 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         229 +246 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         230 +247 ('base', (-0.339, 0.166, 0.057)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         231 +248 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         232 +249 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         233 +250 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         234 +251 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         235 +252 ('base', (-0.345, 0.2, -0.057)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         236 +253 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         237 +254 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         238 +255 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         239 +256 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         240 +257 ('base', (-0.356, 0.178, 0.001)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         241 +258 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         242 +259 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         243 +260 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         244 +261 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         245 +262 ('base', (-0.339, 0.182, 0.043)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         246 +263 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         247 +264 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         248 +265 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         249 +266 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         250 +267 ('base', (-0.391, 0.145, -0.071)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         251 +268 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         252 +269 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         253 +270 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         254 +271 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         255 +272 ('base', (-0.385, 0.218, 0.091)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         256 +273 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         257 +274 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         258 +275 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         259 +276 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         260 +277 ('base', (-0.338, 0.204, 0.064)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         261 +278 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         262 +279 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         263 +280 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         264 +281 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         265 +282 ('base', (-0.346, 0.148, -0.024)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         266 +283 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         267 +284 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         268 +285 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         269 +286 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         270 +287 ('base', (-0.344, 0.18, -0.022)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         271 +288 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         272 +289 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         273 +290 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         274 +291 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         275 +292 ('base', (-0.356, 0.178, -0.013)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         276 +293 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         277 +294 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         278 +295 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         279 +296 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         280 +297 ('base', (-0.356, 0.191, 0.006)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         281 +298 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         282 +299 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         283 +300 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         284 +301 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         285 +302 ('base', (-0.337, 0.181, 0.009)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         286 +303 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         287 +304 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         288 +305 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         289 +306 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         290 +307 ('base', (-0.344, 0.158, -0.015)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         291 +308 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         292 +309 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         293 +310 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         294 +311 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         295 +312 ('base', (-0.355, 0.193, 0.041)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         296 +313 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         297 +314 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         298 +315 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         299 +316 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         300 +317 ('base', (-0.37, 0.228, 0.001)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         301 +318 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         302 +319 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         303 +320 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         304 +321 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         305 +322 ('base', (-0.347, 0.168, -0.015)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         306 +323 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         307 +324 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         308 +325 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         309 +326 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         310 +327 ('base', (-0.39, 0.156, -0.056)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         311 +328 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         312 +329 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         313 +330 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         314 +331 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         315 +332 ('base', (-0.382, 0.156, -0.09)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         316 +333 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         317 +334 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         318 +335 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         319 +336 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         320 +337 ('base', (-0.377, 0.213, -0.028)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         321 +338 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         322 +339 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         323 +340 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         324 +341 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         325 +342 ('base', (-0.337, 0.208, 0.019)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         326 +343 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         327 +344 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         328 +345 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         329 +346 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         330 +347 ('base', (-0.367, 0.203, -0.052)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         331 +348 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         332 +349 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         333 +350 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         334 +351 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         335 +352 ('base', (-0.391, 0.166, -0.027)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         336 +353 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         337 +354 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         338 +355 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         339 +356 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         340 +357 ('base', (-0.388, 0.195, 0.015)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         341 +358 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         342 +359 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         343 +360 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         344 +361 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         345 +362 ('base', (-0.348, 0.226, 0.072)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         346 +363 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         347 +364 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         348 +365 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         349 +366 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         350 +367 ('base', (-0.391, 0.181, -0.044)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         351 +368 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         352 +369 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         353 +370 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         354 +371 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         355 +372 ('base', (-0.341, 0.145, 0.086)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         356 +373 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         357 +374 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         358 +375 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         359 +376 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         360 +377 ('base', (-0.34, 0.224, 0.092)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         361 +378 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         362 +379 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         363 +380 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         364 +381 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         365 +382 ('base', (-0.385, 0.162, -0.005)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         366 +383 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         367 +384 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         368 +385 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         369 +386 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         370 +387 ('base', (-0.382, 0.184, -0.028)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         371 +388 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         372 +389 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         373 +390 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         374 +391 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         375 +392 ('base', (-0.389, 0.202, 0.067)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         376 +393 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         377 +394 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         378 +395 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         379 +396 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         380 +397 ('base', (-0.337, 0.21, -0.08)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         381 +398 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         382 +399 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         383 +400 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         384 +401 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         385 +402 ('base', (-0.343, 0.217, -0.047)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         386 +403 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         387 +404 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         388 +405 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         389 +406 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         390 +407 ('base', (-0.339, 0.209, 0.06)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         391 +408 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         392 +409 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         393 +410 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         394 +411 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         395 +412 ('base', (-0.356, 0.197, -0.094)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         396 +413 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         397 +414 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         398 +415 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         399 +416 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         400 +417 ('base', (-0.348, 0.165, -0.083)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         401 +418 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         402 +419 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         403 +420 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         404 +421 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         405 +422 ('base', (-0.344, 0.169, 0.099)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         406 +423 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         407 +424 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         408 +425 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         409 +426 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         410 +427 ('base', (-0.378, 0.189, 0.037)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         411 +428 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         412 +429 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         413 +430 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         414 +431 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         415 +432 ('base', (-0.361, 0.16, -0.004)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         416 +433 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         417 +434 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         418 +435 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         419 +436 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         420 +437 ('base', (-0.341, 0.135, 0.099)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         421 +438 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         422 +439 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         423 +440 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         424 +441 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         425 +442 ('base', (-0.336, 0.19, 0.06)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         426 +443 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         427 +444 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         428 +445 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         429 +446 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         430 +447 ('base', (-0.368, 0.157, 0.081)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         431 +448 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         432 +449 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         433 +450 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         434 +451 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         435 +452 ('base', (-0.363, 0.156, 0.023)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         436 +453 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         437 +454 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         438 +455 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         439 +456 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         440 +457 ('base', (-0.365, 0.179, -0.065)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         441 +458 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         442 +459 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         443 +460 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         444 +461 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         445 +462 ('base', (-0.395, 0.182, 0.083)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         446 +463 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         447 +464 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         448 +465 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         449 +466 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         450 +467 ('base', (-0.39, 0.188, -0.078)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         451 +468 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         452 +469 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         453 +470 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         454 +471 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         455 +472 ('base', (-0.346, 0.162, 0.084)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         456 +473 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         457 +474 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         458 +475 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         459 +476 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         460 +477 ('base', (-0.394, 0.155, 0.043)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         461 +478 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         462 +479 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         463 +480 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         464 +481 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         465 +482 ('base', (-0.39, 0.218, -0.016)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         466 +483 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         467 +484 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         468 +485 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         469 +486 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         470 +487 ('base', (-0.371, 0.177, -0.077)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         471 +488 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         472 +489 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         473 +490 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         474 +491 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         475 +492 ('base', (-0.356, 0.203, -0.091)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         476 +493 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         477 +494 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         478 +495 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         479 +496 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         480 +497 ('base', (-0.362, 0.219, -0.056)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         481 +498 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         482 +499 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         483 +500 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         484 +501 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         485 +502 ('base', (-0.369, 0.183, 0.05)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         486 +503 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         487 +504 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         488 +505 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         489 +506 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         490 +507 ('base', (-0.35, 0.215, 0.01)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         491 +508 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         492 +509 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         493 +510 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         494 +511 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         495 +512 ('base', (-0.339, 0.2, 0.04)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         496 +513 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         497 +514 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         498 +515 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         499 +516 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         500 +517 ('base', (-0.375, 0.142, -0.085)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         501 +518 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         502 +519 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         503 +520 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         504 +521 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         505 +522 ('base', (-0.383, 0.176, 0.083)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         506 +523 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         507 +524 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         508 +525 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         509 +526 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         510 +527 ('base', (-0.377, 0.175, -0.052)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         511 +528 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         512 +529 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         513 +530 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         514 +531 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         515 +532 ('base', (-0.369, 0.166, 0.031)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         516 +533 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         517 +534 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         518 +535 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         519 +536 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         520 +537 ('base', (-0.34, 0.21, -0.094)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         521 +538 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         522 +539 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         523 +540 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         524 +541 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         525 +542 ('base', (-0.353, 0.143, -0.044)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         526 +543 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         527 +544 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         528 +545 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         529 +546 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         530 +547 ('base', (-0.369, 0.221, -0.054)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         531 +548 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         532 +549 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         533 +550 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         534 +551 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         535 +552 ('base', (-0.357, 0.132, 0.021)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         536 +553 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         537 +554 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         538 +555 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         539 +556 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         540 +557 ('base', (-0.344, 0.202, -0.099)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         541 +558 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         542 +559 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         543 +560 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         544 +561 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         545 +562 ('base', (-0.372, 0.15, -0.031)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         546 +563 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         547 +564 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         548 +565 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         549 +566 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         550 +567 ('base', (-0.354, 0.215, -0.04)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         551 +568 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         552 +569 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         553 +570 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         554 +571 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         555 +572 ('base', (-0.355, 0.18, -0.045)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         556 +573 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         557 +574 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         558 +575 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         559 +576 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         560 +577 ('base', (-0.353, 0.169, -0.094)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         561 +578 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         562 +579 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         563 +580 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         564 +581 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         565 +582 ('base', (-0.35, 0.201, 0.1)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         566 +583 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         567 +584 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         568 +585 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         569 +586 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         570 +587 ('base', (-0.352, 0.2, -0.011)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         571 +588 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         572 +589 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         573 +590 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         574 +591 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         575 +592 ('base', (-0.354, 0.185, 0.07)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         576 +593 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         577 +594 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         578 +595 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         579 +596 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         580 +597 ('base', (-0.386, 0.187, 0.028)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         581 +598 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         582 +599 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         583 +600 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         584 +601 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         585 +602 ('base', (-0.34, 0.202, 0.05)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         586 +603 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         587 +604 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         588 +605 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         589 +606 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         590 +607 ('base', (-0.339, 0.151, 0.097)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         591 +608 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         592 +609 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         593 +610 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         594 +611 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         595 +612 ('base', (-0.346, 0.2, -0.06)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         596 +613 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         597 +614 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         598 +615 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         599 +616 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         600 +617 ('base', (-0.379, 0.214, 0.095)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         601 +618 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         602 +619 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         603 +620 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         604 +621 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         605 +622 ('base', (-0.392, 0.183, 0.074)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         606 +623 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         607 +624 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         608 +625 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         609 +626 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         610 +627 ('base', (-0.381, 0.157, -0.062)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         611 +628 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         612 +629 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         613 +630 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         614 +631 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         615 +632 ('base', (-0.387, 0.207, -0.041)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         616 +633 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         617 +634 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         618 +635 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         619 +636 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         620 +637 ('base', (-0.376, 0.177, -0.052)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         621 +638 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         622 +639 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         623 +640 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         624 +641 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         625 +642 ('base', (-0.35, 0.226, -0.004)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         626 +643 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         627 +644 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         628 +645 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         629 +646 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         630 +647 ('base', (-0.359, 0.18, -0.005)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         631 +648 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         632 +649 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         633 +650 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         634 +651 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         635 +652 ('base', (-0.353, 0.171, 0.095)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         636 +653 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         637 +654 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         638 +655 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         639 +656 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         640 +657 ('base', (-0.378, 0.191, 0.048)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         641 +658 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         642 +659 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         643 +660 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         644 +661 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         645 +662 ('base', (-0.341, 0.175, 0.007)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         646 +663 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         647 +664 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         648 +665 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         649 +666 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         650 +667 ('base', (-0.348, 0.136, 0.048)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         651 +668 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         652 +669 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         653 +670 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         654 +671 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         655 +672 ('base', (-0.379, 0.17, 0.025)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         656 +673 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         657 +674 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         658 +675 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         659 +676 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         660 +677 ('base', (-0.369, 0.193, -0.016)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         661 +678 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         662 +679 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         663 +680 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         664 +681 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         665 +682 ('base', (-0.387, 0.19, -0.058)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         666 +683 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         667 +684 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         668 +685 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         669 +686 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         670 +687 ('base', (-0.35, 0.207, 0.026)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         671 +688 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         672 +689 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         673 +690 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         674 +691 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         675 +692 ('base', (-0.376, 0.19, 0.02)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         676 +693 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         677 +694 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         678 +695 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         679 +696 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         680 +697 ('base', (-0.376, 0.218, -0.015)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         681 +698 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         682 +699 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         683 +700 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         684 +701 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         685 +702 ('base', (-0.388, 0.187, -0.047)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         686 +703 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         687 +704 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         688 +705 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         689 +706 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         690 +707 ('base', (-0.376, 0.167, -0.055)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         691 +708 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         692 +709 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         693 +710 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         694 +711 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         695 +712 ('base', (-0.382, 0.133, 0.033)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         696 +713 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         697 +714 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         698 +715 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         699 +716 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         700 +717 ('base', (-0.393, 0.211, 0.065)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         701 +718 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         702 +719 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         703 +720 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         704 +721 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         705 +722 ('base', (-0.381, 0.167, 0.055)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         706 +723 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         707 +724 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         708 +725 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         709 +726 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         710 +727 ('base', (-0.395, 0.184, -0.016)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         711 +728 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         712 +729 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         713 +730 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         714 +731 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         715 +732 ('base', (-0.38, 0.172, 0.083)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         716 +733 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         717 +734 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         718 +735 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         719 +736 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         720 +737 ('base', (-0.391, 0.195, 0.078)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         721 +738 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         722 +739 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         723 +740 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         724 +741 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         725 +742 ('base', (-0.347, 0.177, -0.009)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         726 +743 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         727 +744 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         728 +745 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         729 +746 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         730 +747 ('base', (-0.354, 0.169, -0.088)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         731 +748 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         732 +749 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         733 +750 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         734 +751 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         735 +752 ('base', (-0.377, 0.176, -0.039)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         736 +753 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         737 +754 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         738 +755 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         739 +756 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         740 +757 ('base', (-0.386, 0.156, 0.096)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         741 +758 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         742 +759 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         743 +760 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         744 +761 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         745 +762 ('base', (-0.368, 0.218, 0.071)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         746 +763 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         747 +764 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         748 +765 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         749 +766 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         750 +767 ('base', (-0.392, 0.179, -0.094)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         751 +768 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         752 +769 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         753 +770 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         754 +771 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         755 +772 ('base', (-0.395, 0.179, -0.05)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         756 +773 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         757 +774 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         758 +775 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         759 +776 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         760 +777 ('base', (-0.337, 0.209, -0.007)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         761 +778 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         762 +779 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         763 +780 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         764 +781 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         765 +782 ('base', (-0.358, 0.199, -0.017)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         766 +783 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         767 +784 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         768 +785 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         769 +786 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         770 +787 ('base', (-0.39, 0.148, -0.08)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         771 +788 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         772 +789 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         773 +790 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         774 +791 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         775 +792 ('base', (-0.357, 0.19, 0.024)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         776 +793 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         777 +794 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         778 +795 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         779 +796 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         780 +797 ('base', (-0.392, 0.214, 0.011)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         781 +798 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         782 +799 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         783 +800 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         784 +801 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         785 +802 ('base', (-0.381, 0.197, -0.079)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         786 +803 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         787 +804 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         788 +805 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         789 +806 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         790 +807 ('base', (-0.38, 0.209, -0.018)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         791 +808 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         792 +809 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         793 +810 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         794 +811 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         795 +812 ('base', (-0.337, 0.137, -0.025)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         796 +813 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         797 +814 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         798 +815 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         799 +816 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         800 +817 ('base', (-0.391, 0.175, 0.037)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         801 +818 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         802 +819 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         803 +820 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         804 +821 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         805 +822 ('base', (-0.351, 0.204, -0.025)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         806 +823 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         807 +824 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         808 +825 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         809 +826 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         810 +827 ('base', (-0.342, 0.147, 0.097)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         811 +828 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         812 +829 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         813 +830 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         814 +831 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         815 +832 ('base', (-0.338, 0.134, 0.058)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         816 +833 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         817 +834 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         818 +835 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         819 +836 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         820 +837 ('base', (-0.371, 0.23, -0.092)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         821 +838 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         822 +839 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         823 +840 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         824 +841 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         825 +842 ('base', (-0.358, 0.162, -0.082)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         826 +843 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         827 +844 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         828 +845 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         829 +846 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         830 +847 ('base', (-0.344, 0.176, -0.099)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         831 +848 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         832 +849 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         833 +850 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         834 +851 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         835 +852 ('base', (-0.362, 0.177, 0.099)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         836 +853 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         837 +854 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         838 +855 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         839 +856 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         840 +857 ('base', (-0.363, 0.192, 0.062)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         841 +858 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         842 +859 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         843 +860 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         844 +861 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         845 +862 ('base', (-0.368, 0.142, -0.063)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         846 +863 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         847 +864 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         848 +865 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         849 +866 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         850 +867 ('base', (-0.349, 0.172, -0.025)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         851 +868 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         852 +869 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         853 +870 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         854 +871 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         855 +872 ('base', (-0.393, 0.174, 0.098)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         856 +873 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         857 +874 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         858 +875 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         859 +876 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         860 +877 ('base', (-0.38, 0.188, -0.044)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         861 +878 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         862 +879 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         863 +880 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         864 +881 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         865 +882 ('base', (-0.352, 0.152, 0.053)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         866 +883 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         867 +884 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         868 +885 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         869 +886 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         870 +887 ('base', (-0.363, 0.169, 0.014)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         871 +888 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         872 +889 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         873 +890 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         874 +891 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         875 +892 ('base', (-0.394, 0.132, 0.08)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         876 +893 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         877 +894 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         878 +895 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         879 +896 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         880 +897 ('base', (-0.349, 0.226, -0.038)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         881 +898 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         882 +899 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         883 +900 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         884 +901 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         885 +902 ('base', (-0.342, 0.211, 0.055)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         886 +903 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         887 +904 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         888 +905 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         889 +906 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         890 +907 ('base', (-0.367, 0.193, 0.058)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         891 +908 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         892 +909 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         893 +910 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         894 +911 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         895 +912 ('base', (-0.361, 0.216, 0.029)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         896 +913 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         897 +914 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         898 +915 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         899 +916 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         900 +917 ('base', (-0.371, 0.155, 0.041)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         901 +918 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         902 +919 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         903 +920 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         904 +921 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         905 +922 ('base', (-0.377, 0.169, -0.008)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         906 +923 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         907 +924 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         908 +925 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         909 +926 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         910 +927 ('base', (-0.373, 0.225, 0.025)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         911 +928 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         912 +929 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         913 +930 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         914 +931 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         915 +932 ('base', (-0.385, 0.226, -0.093)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         916 +933 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         917 +934 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         918 +935 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         919 +936 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         920 +937 ('base', (-0.356, 0.14, 0.091)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         921 +938 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         922 +939 ('move', (0.162, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         923 +940 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         924 +941 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         925 +942 ('base', (-0.382, 0.223, -0.011)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         926 +943 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         927 +944 ('move', (0.158, -0.223, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         928 +945 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         929 +946 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         930 +947 ('base', (-0.348, 0.157, -0.004)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         931 +948 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         932 +949 ('move', (0.157, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         933 +950 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         934 +951 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         935 +952 ('base', (-0.389, 0.181, -0.024)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         936 +953 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         937 +954 ('move', (0.163, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         938 +955 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         939 +956 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         940 +957 ('base', (-0.364, 0.178, -0.034)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         941 +958 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         942 +959 ('move', (0.16, -0.228, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         943 +960 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         944 +961 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         945 +962 ('base', (-0.358, 0.144, 0.083)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         946 +963 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         947 +964 ('move', (0.162, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         948 +965 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         949 +966 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         950 +967 ('base', (-0.361, 0.194, 0.08)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         951 +968 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         952 +969 ('move', (0.163, -0.225, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         953 +970 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         954 +971 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         955 +972 ('base', (-0.383, 0.14, -0.074)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         956 +973 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         957 +974 ('move', (0.16, -0.228, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         958 +975 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         959 +976 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         960 +977 ('base', (-0.394, 0.174, 0.041)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         961 +978 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         962 +979 ('move', (0.16, -0.222, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         963 +980 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         964 +981 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         965 +982 ('base', (-0.336, 0.22, -0.096)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         966 +983 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         967 +984 ('move', (0.158, -0.227, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         968 +985 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         969 +986 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         970 +987 ('base', (-0.383, 0.212, 0.03)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         971 +988 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         972 +989 ('move', (0.16, -0.225, 0.251), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         973 +990 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         974 +991 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         975 +992 ('base', (-0.383, 0.19, 0.036)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         976 +993 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         977 +994 ('move', (0.16, -0.222, 0.25), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         978 +995 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         979 +996 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         980 +997 ('base', (-0.337, 0.152, 0.056)) ee [ 0.16  -0.225  0.248] grasp 0.0 
         981 +998 ('move', (0.16, -0.225, 0.303), None, 'lift') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
         982 +999 ('move', (0.157, -0.225, 0.248), None, 'escape') ee [ 0.16  -0.225  0.248] grasp 0.0 REJ
diff --git a/dev/approach.py b/dev/approach.py
new file mode 100644
index 0000000..4cf693c
--- /dev/null
+++ b/dev/approach.py
@@ -0,0 +1,866 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place the
           2 +target block on it.  Uses an internal FK/IK model of the Kinova Gen3 (arm base at the
           3 +world origin, verified empirically) and Cartesian straight-line motions."""
           4 +import time
           5 +import numpy as np
           6 +
           7 +PI = np.pi
           8 +
           9 +# ----------------------------------------------------------------------------- kinematics
          10 +def _rpy(r, p, y):
          11 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
          12 +    return np.array([[cy * cp, cy * sp * sr - sy * cr, cy * sp * cr + sy * sr],
          13 +                     [sy * cp, sy * sp * sr + cy * cr, sy * sp * cr - cy * sr],
          14 +                     [-sp, cp * sr, cp * cr]])
          15 +
          16 +
          17 +def _tf(xyz, rpy):
          18 +    T = np.eye(4)
          19 +    T[:3, :3] = _rpy(*rpy)
          20 +    T[:3, 3] = xyz
          21 +    return T
          22 +
          23 +
          24 +_JOINTS = [
          25 +    _tf([0, 0, 0.15643], [PI, 0, 0]),
          26 +    _tf([0, 0.005375, -0.12838], [PI / 2, 0, 0]),
          27 +    _tf([0, -0.21038, -0.006375], [-PI / 2, 0, 0]),
          28 +    _tf([0, 0.006375, -0.21038], [PI / 2, 0, 0]),
          29 +    _tf([0, -0.20843, -0.006375], [-PI / 2, 0, 0]),
          30 +    _tf([0, 0.00017505, -0.10593], [PI / 2, 0, 0]),
          31 +    _tf([0, -0.10593, -0.00017505], [-PI / 2, 0, 0]),
          32 +]
          33 +_EE = _tf([0, 0, -0.061525], [PI, 0, 0])
          34 +FINGER = 0.155          # EE frame -> fingertip distance (along tool z)
          35 +FINGER_OFF = 0.05       # finger centre offset from tool axis along closing direction
          36 +
          37 +# joint limits (Kinova Gen3); None = continuous
          38 +_LIM = [None, (-2.38, 2.38), None, (-2.63, 2.63), None, (-2.2, 2.2), None]
          39 +
          40 +
          41 +def fk(q):
          42 +    T = np.eye(4)
          43 +    zs = np.empty((7, 3))
          44 +    ps = np.empty((7, 3))
          45 +    for i in range(7):
          46 +        T = T @ _JOINTS[i]
          47 +        zs[i] = T[:3, 2]
          48 +        ps[i] = T[:3, 3]
          49 +        c, s = np.cos(q[i]), np.sin(q[i])
          50 +        c0 = T[:, 0].copy()
          51 +        T[:, 0] = c * c0 + s * T[:, 1]
          52 +        T[:, 1] = -s * c0 + c * T[:, 1]
          53 +    T = T @ _EE
          54 +    return T, zs, ps
          55 +
          56 +
          57 +def down_R(yaw):
          58 +    c, s = np.cos(yaw), np.sin(yaw)
          59 +    x = np.array([c, s, 0.0])
          60 +    z = np.array([0, 0, -1.0])
          61 +    y = np.cross(z, x)
          62 +    return np.stack([x, y, z], axis=1)
          63 +
          64 +
          65 +def _expm(v):
          66 +    th = np.linalg.norm(v)
          67 +    if th < 1e-12:
          68 +        return np.eye(3)
          69 +    k = v / th
          70 +    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
          71 +    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * (K @ K)
          72 +
          73 +
          74 +def _rotvec(Rm):
          75 +    cos = (np.trace(Rm) - 1) / 2
          76 +    cos = min(1.0, max(-1.0, cos))
          77 +    ang = np.arccos(cos)
          78 +    v = np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]])
          79 +    if ang < 1e-6:
          80 +        return v * 0.5
          81 +    if ang > PI - 1e-4:
          82 +        # 180 deg: axis from diagonal
          83 +        M = (Rm + np.eye(3)) / 2
          84 +        k = np.argmax(np.diag(M))
          85 +        ax = M[:, k] / np.sqrt(max(M[k, k], 1e-12))
          86 +        return ax * ang
          87 +    return v * ang / (2 * np.sin(ang))
          88 +
          89 +
          90 +def ik(q0, pos, Rt, iters=100, tol=1e-5):
          91 +    q = np.array(q0, dtype=float)
          92 +    err = 1e9
          93 +    best = 1e9
          94 +    since = 0
          95 +    for _ in range(iters):
          96 +        T, zs, ps = fk(q)
          97 +        ep = pos - T[:3, 3]
          98 +        er = _rotvec(Rt @ T[:3, :3].T)
          99 +        e = np.concatenate([ep, 0.3 * er])
         100 +        err = np.linalg.norm(e)
         101 +        if err < tol:
         102 +            break
         103 +        if err < best - 1e-4:
         104 +            best = err
         105 +            since = 0
         106 +        else:
         107 +            since += 1
         108 +            if since > 12 and err > 1e-3:
         109 +                break
         110 +        J = np.empty((6, 7))
         111 +        D = T[:3, 3] - ps
         112 +        J[0] = zs[:, 1] * D[:, 2] - zs[:, 2] * D[:, 1]
         113 +        J[1] = zs[:, 2] * D[:, 0] - zs[:, 0] * D[:, 2]
         114 +        J[2] = zs[:, 0] * D[:, 1] - zs[:, 1] * D[:, 0]
         115 +        J[3:] = 0.3 * zs.T
         116 +        lam = 1e-4
         117 +        dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
         118 +        n = np.max(np.abs(dq))
         119 +        if n > 0.4:
         120 +            dq *= 0.4 / n
         121 +        q += dq
         122 +        for i, lim in enumerate(_LIM):
         123 +            if lim is not None:
         124 +                q[i] = min(lim[1], max(lim[0], q[i]))
         125 +    return q, err
         126 +
         127 +
         128 +def wrap(a):
         129 +    return (a + PI) % (2 * PI) - PI
         130 +
         131 +
         132 +# ----------------------------------------------------------------------------- approach
         133 +TABLE_TOP = 0.075
         134 +STEP_FAST = 0.12
         135 +STEP_LOW = 0.08
         136 +SAFE_FLOOR = 0.2
         137 +BASE_ASSIST = True
         138 +STEP_TRAVEL = 0.25
         139 +ASSIST_MINX = 0.2
         140 +JOINT_TRAVEL = True
         141 +ROT_ASSIST = True
         142 +ROT_MAX = 0.8
         143 +BASE_TRAVEL = True
         144 +BASE_XMAX = -0.08
         145 +MERGE = True
         146 +FLOOR_CLR = 0.005
         147 +LIFT_MIN = False
         148 +SAFE_CLR = 0.012
         149 +MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
         150 +TABLE_X = (0.10, 0.50)
         151 +TABLE_Y = (-0.40, 0.40)
         152 +MAX_OPEN = 0.078            # max object width between the fingers
         153 +
         154 +
         155 +def _yaw_of(Rm):
         156 +    return np.arctan2(Rm[1, 0], Rm[0, 0])
         157 +
         158 +
         159 +class GeneratedApproach:
         160 +    def __init__(self, action_space, observation_space, primitives):
         161 +        self.action_space = action_space
         162 +        self.observation_space = observation_space
         163 +
         164 +    # ---------------------------------------------------------------- state helpers
         165 +    def _robot(self, state):
         166 +        return state.get_object_from_name("robot")
         167 +
         168 +    def _q(self, state):
         169 +        r = self._robot(state)
         170 +        return np.array([state.get(r, "joint_%d" % i) for i in range(1, 8)])
         171 +
         172 +    def _base(self, state):
         173 +        r = self._robot(state)
         174 +        return np.array([state.get(r, "pos_base_x"), state.get(r, "pos_base_y"),
         175 +                         state.get(r, "pos_base_rot")])
         176 +
         177 +    def _boxes(self, state):
         178 +        out = {}
         179 +        for n in state.get_object_names():
         180 +            if n == "robot":
         181 +                continue
         182 +            o = state.get_object_from_name(n)
         183 +            try:
         184 +                out[n] = dict(
         185 +                    x=state.get(o, "pose_x"), y=state.get(o, "pose_y"), z=state.get(o, "pose_z"),
         186 +                    hx=state.get(o, "half_extent_x"), hy=state.get(o, "half_extent_y"),
         187 +                    hz=state.get(o, "half_extent_z"), g=state.get(o, "grasp_active"),
         188 +                    yaw=2 * np.arctan2(state.get(o, "pose_qz"), state.get(o, "pose_qw")))
         189 +            except Exception:
         190 +                pass
         191 +        return out
         192 +
         193 +    # ---------------------------------------------------------------- frames
         194 +    @staticmethod
         195 +    def _mount(base):
         196 +        c, s = np.cos(base[2]), np.sin(base[2])
         197 +        M = np.eye(4)
         198 +        M[:3, :3] = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
         199 +        M[0, 3] = base[0] + MOUNT_OFF * c
         200 +        M[1, 3] = base[1] + MOUNT_OFF * s
         201 +        return M
         202 +
         203 +    def _ee_world(self, q, base):
         204 +        T, _, _ = fk(q)
         205 +        return self._mount(base) @ T
         206 +
         207 +    def _ik_world(self, q0, pos, Rw, base, iters=100):
         208 +        M = self._mount(base)
         209 +        pa = M[:3, :3].T @ (np.asarray(pos) - M[:3, 3])
         210 +        Ra = M[:3, :3].T @ Rw
         211 +        return ik(q0, pa, Ra, iters=iters)
         212 +
         213 +    def _feasible(self, base, pos, yaw, seeds):
         214 +        """IK feasibility of a top-down pose from a few seeds; returns q or None."""
         215 +        Rw = down_R(yaw)
         216 +        for s in seeds:
         217 +            q, e = self._ik_world(s, pos, Rw, base, iters=150)
         218 +            if e < 1e-4:
         219 +                return q
         220 +        return None
         221 +
         222 +    # ---------------------------------------------------------------- episode
         223 +    def reset(self, state, info):
         224 +        self.segs = []
         225 +        self.cur = None
         226 +        self.last_q = None
         227 +        self.last_base = None
         228 +        self.last_cmd = False
         229 +        self.fail = {}              # candidate key -> failures
         230 +        self.obj_fail = {}
         231 +        self.placed_spots = []
         232 +        self.pending_check = None
         233 +        self.best_d = None
         234 +        self.stall = 0
         235 +        self.q_home = self._q(state)
         236 +        self.nsteps = 0
         237 +        self.nomerge_until = 0
         238 +        self.scale = 1.0
         239 +        self.max_top = 0.15
         240 +        self.esc = 0
         241 +        # a nominal top-down configuration used as an extra IK seed
         242 +        b = self._base(state)
         243 +        qn, e = self._ik_world(self.q_home, [0.30, 0.0, 0.33], down_R(0.0), b, iters=200)
         244 +        self.q_nom = qn
         245 +
         246 +    # ---------------------------------------------------------------- geometry
         247 +    def _blocking(self, boxes):
         248 +        reg = boxes["target_region"]
         249 +        res = []
         250 +        for n, b in boxes.items():
         251 +            if n in ("target_region", "target_block") or b["g"] > 0.5:
         252 +                continue
         253 +            ex, ey = self._extent_xy(b)
         254 +            if abs(b["x"] - reg["x"]) < ex + reg["hx"] + 0.004 and \
         255 +               abs(b["y"] - reg["y"]) < ey + reg["hy"] + 0.004 and \
         256 +               b["z"] - b["hz"] < reg["z"] + reg["hz"] + 0.08:
         257 +                res.append(n)
         258 +        return res
         259 +
         260 +    @staticmethod
         261 +    def _extent_xy(b):
         262 +        c, s = abs(np.cos(b["yaw"])), abs(np.sin(b["yaw"]))
         263 +        return b["hx"] * c + b["hy"] * s, b["hx"] * s + b["hy"] * c
         264 +
         265 +    @staticmethod
         266 +    def _width_along(b, yaw):
         267 +        a = yaw - b["yaw"]
         268 +        c, s = abs(np.cos(a)), abs(np.sin(a))
         269 +        return 2 * (b["hx"] * c + b["hy"] * s), 2 * (b["hx"] * s + b["hy"] * c)
         270 +
         271 +    def _grasp_clear(self, boxes, name, yaw, tip):
         272 +        """Approximate clearance of the finger volumes (open + closing sweep) and the
         273 +        palm from other objects for a top-down grasp."""
         274 +        b = boxes[name]
         275 +        wu, wv = self._width_along(b, yaw)
         276 +        u = np.array([np.cos(yaw), np.sin(yaw)])
         277 +        v = np.array([-u[1], u[0]])
         278 +        c0 = np.array([b["x"], b["y"]])
         279 +        best = 1.0
         280 +        for n, o in boxes.items():
         281 +            if n == name or o["g"] > 0.5:
         282 +                continue
         283 +            otop = o["z"] + o["hz"]
         284 +            if n == "target_region":
         285 +                continue
         286 +            # z-overlap with finger volume (tip-0.015 .. tip+0.045) and palm (above)
         287 +            if otop < tip - 0.016:
         288 +                continue
         289 +            ex, ey = self._extent_xy(o)
         290 +            # sample the object's footprint corners/edges in gripper frame
         291 +            pts = []
         292 +            for fx in (-1, -0.5, 0, 0.5, 1):
         293 +                for fy in (-1, -0.5, 0, 0.5, 1):
         294 +                    pts.append([o["x"] + fx * ex, o["y"] + fy * ey])
         295 +            pts = np.array(pts) - c0
         296 +            pu = np.abs(pts @ u)
         297 +            pv = np.abs(pts @ v)
         298 +            # finger band: u in [wu/2, 0.068], |v| < 0.014
         299 +            du = np.maximum(wu / 2 - pu, pu - 0.068)
         300 +            dv = pv - 0.014
         301 +            d_f = np.min(np.maximum(du, dv))
         302 +            # palm: |u| < 0.07, |v| < 0.035, z > tip + 0.045
         303 +            if otop > tip + 0.040:
         304 +                d_p = np.min(np.maximum(pu - 0.07, pv - 0.035))
         305 +                d_f = min(d_f, d_p)
         306 +            best = min(best, d_f)
         307 +        return best
         308 +
         309 +    def _grasp_candidates(self, boxes, name):
         310 +        b = boxes[name]
         311 +        support = b["z"] - b["hz"]
         312 +        top = b["z"] + b["hz"]
         313 +        tip0 = min(max(b["z"], support + 0.017), top - 0.001)
         314 +        tips = [tip0, min(tip0 + 0.004, top - 0.001), top - 0.002]
         315 +        cands = []
         316 +        for yaw in (b["yaw"], b["yaw"] + PI / 2, b["yaw"] + PI / 4, b["yaw"] - PI / 4):
         317 +            yaw = wrap(yaw)
         318 +            wu, wv = self._width_along(b, yaw)
         319 +            if wu > MAX_OPEN:
         320 +                continue
         321 +            for ti, tip in enumerate(tips):
         322 +                if tip < support + 0.0125:
         323 +                    continue
         324 +                key = (name, round(yaw, 3), round(tip, 4))
         325 +                if self.fail.get(key, 0) > 0:
         326 +                    continue
         327 +                clr = self._grasp_clear(boxes, name, yaw, tip)
         328 +                diag = 0 if abs(wrap(2 * (yaw - b["yaw"]))) < 0.1 else 1
         329 +                score = min(clr, 0.02) - 0.004 * diag - 0.003 * ti - 0.1 * wu * (clr > 0.005)
         330 +                cands.append((score, yaw, tip, key, clr))
         331 +        cands.sort(key=lambda c: -c[0])
         332 +        return cands
         333 +
         334 +    def _safe_z(self, boxes, exclude=None, held_below=0.0, path=None, rad=0.08):
         335 +        top = TABLE_TOP + FLOOR_CLR
         336 +        for n, b in boxes.items():
         337 +            if b["g"] > 0.5 or n == exclude:
         338 +                continue
         339 +            if path is not None:
         340 +                a = np.asarray(path[0][:2], float)
         341 +                c = np.asarray(path[1][:2], float)
         342 +                o = np.array([b["x"], b["y"]])
         343 +                ab = c - a
         344 +                t = 0.0 if ab @ ab < 1e-12 else min(1.0, max(0.0, (o - a) @ ab / (ab @ ab)))
         345 +                ex, ey = self._extent_xy(b)
         346 +                if np.linalg.norm(a + t * ab - o) > rad + np.hypot(ex, ey):
         347 +                    continue
         348 +            top = max(top, b["z"] + b["hz"])
         349 +        return max(SAFE_FLOOR, top + SAFE_CLR + held_below + FINGER)
         350 +
         351 +    def _drop_spot(self, boxes, name, base, seeds, safe):
         352 +        reg = boxes["target_region"]
         353 +        b = boxes[name]
         354 +        bex, bey = self._extent_xy(b)
         355 +        cands = []
         356 +        for x in np.arange(TABLE_X[0] + 0.06, TABLE_X[1] - 0.03, 0.025):
         357 +            for y in np.arange(TABLE_Y[0] + 0.05, TABLE_Y[1] - 0.049, 0.025):
         358 +                if x < 0.2 and abs(y) < 0.14:
         359 +                    continue
         360 +                clr = 1.0
         361 +                for n, o in boxes.items():
         362 +                    if n == name:
         363 +                        continue
         364 +                    ex, ey = self._extent_xy(o)
         365 +                    m = 0.06 if n != "target_region" else 0.03
         366 +                    if n == "target_block":
         367 +                        m = 0.075
         368 +                    dx = abs(x - o["x"]) - ex - bex - m
         369 +                    dy = abs(y - o["y"]) - ey - bey - m
         370 +                    clr = min(clr, max(dx, dy))
         371 +                for (px, py) in self.placed_spots:
         372 +                    clr = min(clr, max(abs(x - px), abs(y - py)) - 0.07)
         373 +                dist = np.hypot(x - b["x"], y - b["y"])
         374 +                tb = boxes["target_block"]
         375 +                if name != "target_block":
         376 +                    dist += 0.7 * np.hypot(x - tb["x"], y - tb["y"])
         377 +                cands.append((min(clr, 0.03) * 10 - dist, x, y))
         378 +        cands.sort(key=lambda c: -c[0])
         379 +        for sc, x, y in cands[:25]:
         380 +            if self._feasible(base, [x, y, safe], 0.0, seeds) is not None:
         381 +                return (x, y)
         382 +        return (cands[0][1], cands[0][2])
         383 +
         384 +    # ---------------------------------------------------------------- base selection
         385 +    def _choose_base(self, base, poses, seeds):
         386 +        """Return a base pose from which all (pos, yaw) poses are IK-feasible, preferring
         387 +        the current base.  Returns (base, ok)."""
         388 +        def ok(bb):
         389 +            ss = list(seeds)
         390 +            for pos, yaw in poses:
         391 +                q = self._feasible(bb, pos, yaw, ss)
         392 +                if q is None:
         393 +                    return False
         394 +                ss = [q] + ss
         395 +            return True
         396 +        if ok(base):
         397 +            return base, True
         398 +        cx = np.mean([p[0][0] for p in poses])
         399 +        cy = np.mean([p[0][1] for p in poses])
         400 +        cands = []
         401 +        for dx in (0.0, -0.05, -0.1, -0.15, -0.2, -0.25, 0.05):
         402 +            for dy in (0.0, -0.1, 0.1, -0.2, 0.2):
         403 +                bx = min(base[0] + dx, -0.08)
         404 +                by = base[1] + dy
         405 +                # prefer reach distance ~0.35-0.45 from mount
         406 +                mx = bx + MOUNT_OFF
         407 +                r = np.hypot(cx - mx, cy - by)
         408 +                cost = abs(dx) + abs(dy) + 0.5 * abs(r - 0.4)
         409 +                cands.append((cost, np.array([bx, by, 0.0])))
         410 +        cands.sort(key=lambda c: c[0])
         411 +        for cost, bb in cands:
         412 +            if ok(bb):
         413 +                return bb, True
         414 +        return base, False
         415 +
         416 +    # ---------------------------------------------------------------- planning
         417 +    def _plan_pick(self, state, boxes, name, cand):
         418 +        """Segments to pick object `name` with candidate (yaw, tip)."""
         419 +        q = self._q(state)
         420 +        base = self._base(state)
         421 +        b = boxes[name]
         422 +        yaw, tip = cand
         423 +        seeds = [q, self.q_nom, self.q_home]
         424 +        Tw0 = self._ee_world(q, base)
         425 +        safe = self._safe_z(boxes, path=(Tw0[:3, 3], (b["x"], b["y"])))
         426 +        grasp_z = tip + FINGER
         427 +        above = np.array([b["x"], b["y"], safe])
         428 +        gpos = np.array([b["x"], b["y"], grasp_z])
         429 +        # choose equivalent yaw (yaw or yaw+pi) closest to current tool yaw
         430 +        Tw = self._ee_world(q, base)
         431 +        cur_yaw = _yaw_of(Tw[:3, :3])
         432 +        opts = sorted([yaw, wrap(yaw + PI)], key=lambda a: abs(wrap(a - cur_yaw)))
         433 +        for y in opts:
         434 +            nb, ok = self._choose_base(base, [(above, y), (gpos, y)], seeds)
         435 +            if ok:
         436 +                yaw = y
         437 +                break
         438 +        segs = []
         439 +        segs.append(("move", np.array([Tw[0, 3], Tw[1, 3], max(Tw[2, 3], safe)]), None, "lift"))
         440 +        if np.max(np.abs(nb - base)) > 1e-6:
         441 +            segs.append(("base", nb))
         442 +        segs.append(("move", above, yaw, "travel"))
         443 +        segs.append(("move", gpos, yaw, "grasp_descend", name))
         444 +        segs.append(("grip", -1.0, name))
         445 +        return segs
         446 +
         447 +    def _plan_place(self, state, boxes, name, place_xy, bottom):
         448 +        """Segments to place currently-held object `name` with its bottom at `bottom`."""
         449 +        q = self._q(state)
         450 +        base = self._base(state)
         451 +        b = boxes[name]
         452 +        Tw = self._ee_world(q, base)
         453 +        yaw = _yaw_of(Tw[:3, :3])
         454 +        off = Tw[2, 3] - b["z"]                 # EE z - object centre z
         455 +        # xy offset of object centre relative to EE (in world, keep yaw constant)
         456 +        dxy = np.array([b["x"] - Tw[0, 3], b["y"] - Tw[1, 3]])
         457 +        seeds = [q, self.q_nom, self.q_home]
         458 +        hb = b["hz"] + off - FINGER
         459 +        ex0 = np.array([place_xy[0] - dxy[0], place_xy[1] - dxy[1]])
         460 +        bex, bey = self._extent_xy(b)
         461 +        safe = self._safe_z(boxes, exclude=name, held_below=hb,
         462 +                            path=(Tw[:3, 3], ex0), rad=max(0.08, np.hypot(bex, bey) + 0.02))
         463 +        safe = max(safe, bottom + b["hz"] + off + 0.03)
         464 +        ex = np.array([place_xy[0] - dxy[0], place_xy[1] - dxy[1]])
         465 +        pz = bottom + b["hz"] + off
         466 +        above = np.array([ex[0], ex[1], safe])
         467 +        ppos = np.array([ex[0], ex[1], pz])
         468 +        nb, ok = self._choose_base(base, [(above, yaw), (ppos, yaw)], seeds)
         469 +        segs = []
         470 +        segs.append(("move", np.array([Tw[0, 3], Tw[1, 3], max(safe, Tw[2, 3])]), yaw, "lift"))
         471 +        if np.max(np.abs(nb - base)) > 1e-6:
         472 +            segs.append(("base", nb))
         473 +        segs.append(("move", above, yaw, "travel"))
         474 +        segs.append(("move", ppos, yaw, "place_descend"))
         475 +        segs.append(("grip", 1.0, None))
         476 +        return segs
         477 +
         478 +    def _held(self, boxes):
         479 +        for n, b in boxes.items():
         480 +            if b["g"] > 0.5:
         481 +                return n
         482 +        return None
         483 +
         484 +    def _replan(self, state):
         485 +        boxes = self._boxes(state)
         486 +        reg = boxes["target_region"]
         487 +        held = self._held(boxes)
         488 +        r = self._robot(state)
         489 +        if held is None and state.get(r, "grasp_active") > 0.5:
         490 +            held = None
         491 +        if held is not None:
         492 +            if held == "target_block" and not self._blocking(boxes):
         493 +                return self._plan_place(state, boxes, held, (reg["x"], reg["y"]),
         494 +                                        reg["z"] + reg["hz"] + 0.0005)
         495 +            if held == "target_block":
         496 +                # should not happen often: park the block somewhere free
         497 +                base = self._base(state)
         498 +                seeds = [self._q(state), self.q_nom, self.q_home]
         499 +                spot = self._drop_spot(boxes, held, base, seeds, self._safe_z(boxes))
         500 +                return self._plan_place(state, boxes, held, spot, TABLE_TOP + 0.001)
         501 +            base = self._base(state)
         502 +            seeds = [self._q(state), self.q_nom, self.q_home]
         503 +            spot = self._drop_spot(boxes, held, base, seeds, self._safe_z(boxes))
         504 +            self.placed_spots.append(spot)
         505 +            return self._plan_place(state, boxes, held, spot, TABLE_TOP + 0.0015)
         506 +        blk = self._blocking(boxes)
         507 +        targets = blk if blk else ["target_block"]
         508 +        best = None
         509 +        for n in targets:
         510 +            cands = self._grasp_candidates(boxes, n)
         511 +            if cands:
         512 +                c = cands[0]
         513 +                if best is None or c[0] > best[0][0]:
         514 +                    best = (c, n)
         515 +        if best is None:
         516 +            # everything failed once: reset failure memory and retry
         517 +            self.fail = {}
         518 +            for n in targets:
         519 +                cands = self._grasp_candidates(boxes, n)
         520 +                if cands:
         521 +                    best = (cands[0], n)
         522 +                    break
         523 +        if best is None:
         524 +            T = self._ee_world(self._q(state), self._base(state))
         525 +            return [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.02]), None, "lift")]
         526 +        c, n = best
         527 +        self.cur_key = c[3]
         528 +        return self._plan_pick(state, boxes, n, (c[1], c[2]))
         529 +
         530 +    # ---------------------------------------------------------------- control
         531 +    def get_action(self, state):
         532 +        self.nsteps += 1
         533 +        boxes0 = self._boxes(state)
         534 +        self.max_top = max([b["z"] + b["hz"] for n, b in boxes0.items() if b["g"] < 0.5] + [0.1])
         535 +        q = self._q(state)
         536 +        base = self._base(state)
         537 +        act = np.zeros(11, dtype=np.float32)
         538 +        rejected = False
         539 +        if self.last_cmd and self.last_q is not None:
         540 +            if np.max(np.abs(q - self.last_q)) < 1e-7 and \
         541 +               np.max(np.abs(base - self.last_base)) < 1e-7:
         542 +                rejected = True
         543 +        self.last_q = q.copy()
         544 +        self.last_base = base.copy()
         545 +        self.last_cmd = False
         546 +
         547 +        if self.pending_check is not None:
         548 +            name = self.pending_check
         549 +            self.pending_check = None
         550 +            r = self._robot(state)
         551 +            if state.get(r, "grasp_active") < 0.5:
         552 +                key = getattr(self, "cur_key", None)
         553 +                if key is not None:
         554 +                    self.fail[key] = self.fail.get(key, 0) + 1
         555 +                self.segs = []
         556 +                self.cur = None
         557 +
         558 +        if rejected:
         559 +            self.scale = max(self.scale * 0.35, 0.01)
         560 +        elif self.last_q is not None:
         561 +            self.scale = min(1.0, self.scale * 1.5)
         562 +        if rejected and self.cur is not None and self.cur[0] in ("move", "base"):
         563 +            if self.scale > 0.02 and self.cur[0] == "move" and self.cur[3] != "escape":
         564 +                pass            # retry the same segment with a smaller step
         565 +            else:
         566 +                self._handle_reject(state)
         567 +
         568 +        t_start = time.time()
         569 +        for _ in range(30):
         570 +            if time.time() - t_start > 1.5:
         571 +                break
         572 +            if self.cur is None:
         573 +                if not self.segs:
         574 +                    self.segs = self._merge(state, self._replan(state))
         575 +                self.cur = self.segs.pop(0)
         576 +                self.best_d = None
         577 +                self.stall = 0
         578 +                self.jplan = None
         579 +            seg = self.cur
         580 +            if seg[0] == "lazy":
         581 +                tr, de = seg[1], seg[2]
         582 +                r = self._jplan_to(state, de[1], tr[2], final_exempt=True)
         583 +                if r is not None:
         584 +                    self.cur = ("jmove", r[0], r[1], "m_" + de[3])
         585 +                else:
         586 +                    self.cur = tr
         587 +                    self.segs.insert(0, de)
         588 +                    if seg[3] is not None:
         589 +                        self.segs.insert(0, tr)
         590 +                        self.cur = seg[3]
         591 +                self.jplan = None
         592 +                self.best_d = None
         593 +                self.stall = 0
         594 +                seg = self.cur
         595 +            if seg[0] == "jmove":
         596 +                if rejected:
         597 +                    self.nomerge_until = self.nsteps + 8
         598 +                    self.segs = []
         599 +                    self.cur = None
         600 +                    continue
         601 +                if self.jplan is None:
         602 +                    self.jplan = (seg[1], seg[2])
         603 +                if self.jplan is False:
         604 +                    self.cur = None
         605 +                    continue
         606 +            if JOINT_TRAVEL and seg[0] == "move" and seg[3] == "travel" and self.jplan is None:
         607 +                self.jplan = self._joint_plan(state, seg)
         608 +            if self.jplan is not None and self.jplan is not False and seg[0] in ("move", "jmove"):
         609 +                if rejected:
         610 +                    self.jplan = False
         611 +                else:
         612 +                    qg, bg = self.jplan
         613 +                    dq = qg - q
         614 +                    dq[0] = wrap(dq[0])
         615 +                    dbs = bg - base
         616 +                    dbs[2] = wrap(dbs[2])
         617 +                    m = max(np.max(np.abs(dq)), np.max(np.abs(dbs)))
         618 +                    if m > 1e-4:
         619 +                        lim = 0.2 * max(self.scale, 0.05)
         620 +                        n = max(1.0, np.ceil(m / lim - 1e-9))
         621 +                        act[0:3] = (dbs / n).astype(np.float32)
         622 +                        act[3:10] = (dq / n).astype(np.float32)
         623 +                        self.last_cmd = True
         624 +                        return act
         625 +                    self.jplan = False
         626 +            if seg[0] == "jmove":
         627 +                self.cur = None
         628 +                continue
         629 +            if seg[0] == "grip":
         630 +                act[10] = seg[1]
         631 +                self.cur = None
         632 +                self.pending_check = seg[2] if seg[1] < 0 else None
         633 +                return act
         634 +            if seg[0] == "base":
         635 +                d = seg[1] - base
         636 +                d[2] = wrap(d[2])
         637 +                if np.max(np.abs(d)) < 1e-6:
         638 +                    self.cur = None
         639 +                    continue
         640 +                act[0:3] = np.clip(d, -0.2, 0.2)
         641 +                self.last_cmd = True
         642 +                return act
         643 +            goal, yaw = seg[1], seg[2]
         644 +            Tw = self._ee_world(q, base)
         645 +            if yaw is None:
         646 +                Rt = down_R(_yaw_of(Tw[:3, :3])) if Tw[2, 2] < -0.8 else Tw[:3, :3]
         647 +            else:
         648 +                Rt = down_R(yaw)
         649 +            p = Tw[:3, 3]
         650 +            d = goal - p
         651 +            nd = np.linalg.norm(d)
         652 +            rerr = np.linalg.norm(_rotvec(Rt @ Tw[:3, :3].T))
         653 +            if nd < 5e-4 and rerr < 2e-3:
         654 +                self.cur = None
         655 +                continue
         656 +            # stall detection
         657 +            prog = nd + 0.1 * rerr
         658 +            if self.best_d is None or prog < self.best_d - 2e-4:
         659 +                self.best_d = prog
         660 +                self.stall = 0
         661 +            else:
         662 +                self.stall += 1
         663 +                if self.stall >= 4:
         664 +                    if nd < 3e-3 and rerr < 2e-2:
         665 +                        self.cur = None
         666 +                        continue
         667 +                    self._handle_reject(state)
         668 +                    continue
         669 +            step = STEP_FAST
         670 +            low = p[2] - FINGER < self.max_top + 0.03
         671 +            if low and seg[3] in ("lift", "grasp_descend", "place_descend", "retreat"):
         672 +                step = STEP_LOW
         673 +            step *= self.scale
         674 +            rv = _rotvec(Rt @ Tw[:3, :3].T)
         675 +            f = 1.0
         676 +            if nd > 1e-9:
         677 +                f = min(f, step / nd)
         678 +            if rerr > 1e-9:
         679 +                f = min(f, max(0.5 * self.scale, 0.02) / rerr)
         680 +            lim = 0.2 * max(self.scale, 0.05)
         681 +            dq = None
         682 +            assist = BASE_ASSIST and seg[3] == "travel" and abs(d[1]) > 1e-4 and \
         683 +                min(p[0], goal[0]) - self._mount(base)[0, 3] > ASSIST_MINX
         684 +            if assist:
         685 +                f = min(1.0, STEP_TRAVEL * self.scale / nd, 0.2 * self.scale / abs(d[1]))
         686 +                if rerr > 1e-9:
         687 +                    f = min(f, max(0.5 * self.scale, 0.02) / rerr)
         688 +            db = np.zeros(3)
         689 +            for _it in range(5):
         690 +                tgt = p + d * f
         691 +                Rs = _expm(rv * f) @ Tw[:3, :3]
         692 +                bb = base
         693 +                if assist:
         694 +                    db = np.array([0.0, d[1] * f, 0.0])
         695 +                    bb = base + db
         696 +                qt, err = self._ik_world(q, tgt, Rs, bb)
         697 +                dq = qt - q
         698 +                m = np.max(np.abs(dq))
         699 +                if m <= lim:
         700 +                    break
         701 +                f *= lim / m * 0.97
         702 +            if assist:
         703 +                act[0:3] = db.astype(np.float32)
         704 +            m = np.max(np.abs(dq))
         705 +            if m > lim:
         706 +                dq *= lim / m
         707 +            if m < 1e-7:
         708 +                self.stall += 1
         709 +                continue
         710 +            act[3:10] = dq.astype(np.float32)
         711 +            self.last_cmd = True
         712 +            return act
         713 +        return act
         714 +
         715 +    def _req_z(self, boxes, xy, held, hb):
         716 +        top = TABLE_TOP + FLOOR_CLR
         717 +        rad = 0.08
         718 +        if held is not None:
         719 +            ex, ey = self._extent_xy(boxes[held])
         720 +            rad = max(rad, np.hypot(ex, ey) + 0.02)
         721 +        for n, b in boxes.items():
         722 +            if b["g"] > 0.5 or n == held:
         723 +                continue
         724 +            ex, ey = self._extent_xy(b)
         725 +            if np.hypot(xy[0] - b["x"], xy[1] - b["y"]) > rad + np.hypot(ex, ey):
         726 +                continue
         727 +            top = max(top, b["z"] + b["hz"])
         728 +        return top + SAFE_CLR + hb + FINGER
         729 +
         730 +    def _joint_plan(self, state, seg):
         731 +        nxt = None
         732 +        if self.segs and self.segs[0][0] == "move":
         733 +            nxt = self.segs[0][1]
         734 +        r = self._jplan_to(state, seg[1], seg[2], nxt=nxt)
         735 +        return False if r is None else r
         736 +
         737 +    def _jplan_to(self, state, goal, yaw, nxt=None, extra_bases=(), final_exempt=False):
         738 +        q = self._q(state)
         739 +        base = self._base(state)
         740 +        Tw = self._ee_world(q, base)
         741 +        Rt = down_R(yaw) if yaw is not None else down_R(_yaw_of(Tw[:3, :3]))
         742 +        boxes = self._boxes(state)
         743 +        held = self._held(boxes)
         744 +        hb = 0.0
         745 +        if held is not None:
         746 +            b = boxes[held]
         747 +            hb = max(0.0, (Tw[2, 3] - FINGER) - (b["z"] - b["hz"]))
         748 +        p = Tw[:3, 3]
         749 +        dxy = goal[:2] - p[:2]
         750 +        cands = [base.copy()] + [np.array(e, float) for e in extra_bases]
         751 +        if BASE_TRAVEL:
         752 +            for fx, fy in ((1.0, 1.0), (0.0, 1.0), (0.5, 0.5), (0.0, 0.5)):
         753 +                bb = base.copy()
         754 +                bb[0] = min(base[0] + fx * dxy[0], max(base[0], BASE_XMAX))
         755 +                bb[1] = base[1] + fy * dxy[1]
         756 +                cands.append(bb)
         757 +        if ROT_ASSIST:
         758 +            Mw = self._mount(base)[:3, 3]
         759 +            a0 = np.arctan2(p[1] - Mw[1], p[0] - Mw[0])
         760 +            a1 = np.arctan2(goal[1] - Mw[1], goal[0] - Mw[0])
         761 +            th2 = float(np.clip(base[2] + wrap(a1 - a0), -ROT_MAX, ROT_MAX))
         762 +            bb = np.array([Mw[0] - MOUNT_OFF * np.cos(th2), Mw[1] - MOUNT_OFF * np.sin(th2), th2])
         763 +            if bb[0] <= max(base[0], BASE_XMAX):
         764 +                cands.append(bb)
         765 +        best = None
         766 +        for bb in cands:
         767 +            costb = max(abs(bb[0] - base[0]), abs(bb[1] - base[1]), abs(wrap(bb[2] - base[2])))
         768 +            if best is not None and costb >= best[0]:
         769 +                continue
         770 +            for sd in (q, self.q_nom):
         771 +                qg, err = self._ik_world(sd, goal, Rt, bb, iters=150)
         772 +                if err > 1e-4:
         773 +                    continue
         774 +                dq = qg - q
         775 +                dq[0] = wrap(dq[0])
         776 +                c = max(np.max(np.abs(dq)), costb)
         777 +                if best is not None and c >= best[0] - 1e-3:
         778 +                    continue
         779 +                if nxt is not None:
         780 +                    qn, en = self._ik_world(qg, nxt, Rt, bb, iters=100)
         781 +                    if en > 1e-4:
         782 +                        continue
         783 +                n = int(max(1, np.ceil(c / 0.2 - 1e-9)))
         784 +                if not self._path_ok(q, base, q + dq, bb, boxes, held, hb, n, final_exempt):
         785 +                    continue
         786 +                best = (c, q + dq, bb)
         787 +        if best is None:
         788 +            return None
         789 +        return (best[1], best[2])
         790 +
         791 +    def _path_ok(self, q, base, qg, bg, boxes, held, hb, n=12, final_exempt=False):
         792 +        db = bg - base
         793 +        db[2] = wrap(db[2])
         794 +        ks = range(1, n) if final_exempt else range(1, n + 1)
         795 +        for k in ks:
         796 +            sv = k / n
         797 +            qs = q + sv * (qg - q)
         798 +            T = self._ee_world(qs, base + sv * db)
         799 +            if T[2, 2] > -0.9:
         800 +                return False
         801 +            if T[2, 3] < self._req_z(boxes, T[:2, 3], held, hb) - 0.005:
         802 +                return False
         803 +        return True
         804 +
         805 +    def _merge(self, state, segs):
         806 +        """Replace (travel, descend) by a lazily planned joint move."""
         807 +        if not MERGE or self.nsteps < self.nomerge_until:
         808 +            return segs
         809 +        kinds = [sg[3] if sg[0] == "move" else sg[0] for sg in segs]
         810 +        if "travel" not in kinds:
         811 +            return segs
         812 +        it = kinds.index("travel")
         813 +        if it + 1 >= len(segs) or kinds[it + 1] not in ("grasp_descend", "place_descend"):
         814 +            return segs
         815 +        pre = segs[:it]
         816 +        full_lift = None
         817 +        if LIFT_MIN and len(pre) == 1 and pre[0][0] == "move" and pre[0][3] == "lift":
         818 +            q = self._q(state)
         819 +            base = self._base(state)
         820 +            Tw = self._ee_world(q, base)
         821 +            boxes = self._boxes(state)
         822 +            held = self._held(boxes)
         823 +            hb = 0.0
         824 +            if held is not None:
         825 +                b = boxes[held]
         826 +                hb = max(0.0, (Tw[2, 3] - FINGER) - (b["z"] - b["hz"]))
         827 +            loc = self._req_z(boxes, Tw[:2, 3], held, hb)
         828 +            lg = pre[0][1]
         829 +            if loc < lg[2] - 0.01:
         830 +                full_lift = pre[0]
         831 +                nz = max(Tw[2, 3], loc)
         832 +                pre = [("move", np.array([lg[0], lg[1], nz]), pre[0][2], "lift")]
         833 +        return pre + [("lazy", segs[it], segs[it + 1], full_lift)] + segs[it + 2:]
         834 +
         835 +    def _handle_reject(self, state):
         836 +        seg = self.cur
         837 +        tag = seg[3] if (seg[0] == "move" and len(seg) > 3) else None
         838 +        q = self._q(state)
         839 +        base = self._base(state)
         840 +        T = self._ee_world(q, base)
         841 +        if tag == "place_descend":
         842 +            # contact: release here (object is resting on something)
         843 +            self.cur = None
         844 +            return
         845 +        if tag == "grasp_descend":
         846 +            key = getattr(self, "cur_key", None)
         847 +            if key is not None:
         848 +                self.fail[key] = self.fail.get(key, 0) + 1
         849 +            self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.06]), None, "lift")]
         850 +            self.cur = None
         851 +            return
         852 +        if seg[0] == "base":
         853 +            self.segs = []
         854 +            self.cur = None
         855 +            return
         856 +        # generic: small escape displacement in a cycling direction, then replan
         857 +        dirs = [(0, 0, 1), (1, 0, 0.5), (-1, 0, 0.5), (0, 1, 0.5), (0, -1, 0.5),
         858 +                (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (1, 1, 1), (-1, -1, 1),
         859 +                (1, -1, 1), (-1, 1, 1)]
         860 +        d = np.array(dirs[self.esc % len(dirs)], dtype=float)
         861 +        self.esc += 1
         862 +        d /= np.linalg.norm(d)
         863 +        mag = 0.003 if tag != "escape" else 0.003 + 0.002 * (self.esc // len(dirs) % 3)
         864 +        self.segs = [("move", T[:3, 3] + d * mag, None, "escape")]
         865 +        self.cur = None
         866 +        self.scale = 0.3
diff --git a/dev/dbg_run.py b/dev/dbg_run.py
new file mode 100644
index 0000000..d434e54
--- /dev/null
+++ b/dev/dbg_run.py
@@ -0,0 +1,21 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach, fk
           4 +import approach as AP
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 1000; OC=int(sys.argv[3]) if len(sys.argv)>3 else None
           6 +env = make_env(); obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None))
           7 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +bx = ap._boxes(obs)
           9 +for n,b in sorted(bx.items()): print(n, {k: round(v,3) for k,v in b.items()})
          10 +lastseg=None
          11 +for t in range(N):
          12 +    a = ap.get_action(obs)
          13 +    seg = ap.cur
          14 +    key = None if seg is None else tuple((tuple(np.round(v,3)) if isinstance(v,np.ndarray) else (round(v,2) if isinstance(v,float) else v)) for v in seg)
          15 +    obs, r, term, trunc, info = env.step(a)
          16 +    q = ap._q(obs); T = ap._ee_world(q, ap._base(obs))
          17 +    rob = ap._robot(obs)
          18 +    if key != lastseg or np.allclose(q, ap.last_q):
          19 +        print(t, key, "ee", np.round(T[:3,3],3), "grasp", obs.get(rob,'grasp_active'), "REJ" if np.allclose(q, ap.last_q) and np.any(a[3:10]!=0) else "")
          20 +        lastseg = key
          21 +    if term: print("DONE", t); break
diff --git a/dev/env_client.py b/dev/env_client.py
new file mode 100644
index 0000000..108c884
--- /dev/null
+++ b/dev/env_client.py
@@ -0,0 +1,737 @@
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
          86 +        # Match relational_structs.Type's dataclass repr, including name quoting.
          87 +        # Policies must see the same strings during synthesis and evaluation.
          88 +        return f"Type(name={self.name!r})"
          89 +
          90 +
          91 +class _Object:
          92 +    """A local mirror of relational_structs.Object (name + type)."""
          93 +
          94 +    def __init__(self, name: str, typ: _Type) -> None:
          95 +        self.name = name
          96 +        self.type = typ
          97 +
          98 +    def is_instance(self, typ: _Type) -> bool:
          99 +        """True if this object's type is *typ* or a descendant of it."""
         100 +        return typ in self.type.get_ancestors()
         101 +
         102 +    def __eq__(self, other: Any) -> bool:
         103 +        return isinstance(other, _Object) and other.name == self.name
         104 +
         105 +    def __hash__(self) -> int:
         106 +        return hash(self.name)
         107 +
         108 +    def __repr__(self) -> str:
         109 +        return f"{self.name}:{self.type.name}"
         110 +
         111 +
         112 +class _ObjectCentricState:
         113 +    """A local mirror of relational_structs.ObjectCentricState.
         114 +
         115 +    Holds ``{Object: feature ndarray}`` as ``data`` plus ``{Type: [feature names]}`` as
         116 +    ``type_features`` (both public, matching the real state) and exposes the read/write
         117 +    API a program uses. Iteration yields the objects, sorted by name for determinism.
         118 +    """
         119 +
         120 +    def __init__(
         121 +        self,
         122 +        data: dict[_Object, np.ndarray],
         123 +        type_features: dict[_Type, list[str]],
         124 +    ) -> None:
         125 +        self.data = data
         126 +        self.type_features = type_features
         127 +
         128 +    def __iter__(self) -> Any:
         129 +        return iter(sorted(self.data, key=lambda o: o.name))
         130 +
         131 +    def get_object_names(self) -> set[str]:
         132 +        """The set of object names in this state."""
         133 +        return {o.name for o in self.data}
         134 +
         135 +    def get_object_from_name(self, name: str) -> _Object:
         136 +        """The object with the given name."""
         137 +        for obj in self.data:
         138 +            if obj.name == name:
         139 +                return obj
         140 +        raise ValueError(f"No object named {name!r}")
         141 +
         142 +    def get_objects(self, typ: _Type) -> list[_Object]:
         143 +        """Objects that are instances of *typ* (its subtypes included), by name."""
         144 +        return sorted(
         145 +            (o for o in self.data if o.is_instance(typ)), key=lambda o: o.name
         146 +        )
         147 +
         148 +    def _feature_index(self, obj: _Object, feature: str) -> int:
         149 +        return self.type_features[obj.type].index(feature)
         150 +
         151 +    def get(self, obj: _Object, feature: str) -> float:
         152 +        """Read a named feature of an object."""
         153 +        return float(self.data[obj][self._feature_index(obj, feature)])
         154 +
         155 +    def set(self, obj: _Object, feature: str, value: float) -> None:
         156 +        """Write a named feature of an object in place."""
         157 +        self.data[obj][self._feature_index(obj, feature)] = value
         158 +
         159 +    def vec(self, objects: Any) -> np.ndarray:
         160 +        """Concatenate the feature vectors of the given objects."""
         161 +        return (
         162 +            np.concatenate([self.data[o] for o in objects]) if objects else np.array([])
         163 +        )
         164 +
         165 +    def copy(self) -> "_ObjectCentricState":
         166 +        """A deep copy of this state."""
         167 +        return _ObjectCentricState(
         168 +            {o: arr.copy() for o, arr in self.data.items()},
         169 +            {t: list(f) for t, f in self.type_features.items()},
         170 +        )
         171 +
         172 +    def allclose(self, other: "_ObjectCentricState") -> bool:
         173 +        """True if *other* has the same objects with numerically-close features."""
         174 +        if self.get_object_names() != other.get_object_names():
         175 +            return False
         176 +        return all(
         177 +            np.allclose(self.data[o], other.data[other.get_object_from_name(o.name)])
         178 +            for o in self.data
         179 +        )
         180 +
         181 +
         182 +def _build_local_types(
         183 +    types_payload: list[dict[str, Any]],
         184 +) -> tuple[dict[str, _Type], dict[_Type, list[str]]]:
         185 +    """Rebuild local {name: _Type} and {_Type: [features]} (parents-first payload)."""
         186 +    type_by_name: dict[str, _Type] = {}
         187 +    type_features: dict[_Type, list[str]] = {}
         188 +    for entry in types_payload:
         189 +        parent = type_by_name[entry["parent"]] if entry["parent"] is not None else None
         190 +        typ = _Type(entry["name"], parent)
         191 +        type_by_name[entry["name"]] = typ
         192 +        type_features[typ] = list(entry["features"])
         193 +    return type_by_name, type_features
         194 +
         195 +
         196 +def _ocs_from_payload(payload: dict[str, Any]) -> _ObjectCentricState:
         197 +    """Reconstruct a local ObjectCentricState from a self-contained codec payload."""
         198 +    type_by_name, type_features = _build_local_types(payload["types"])
         199 +    data: dict[_Object, np.ndarray] = {}
         200 +    for entry in payload["objects"]:
         201 +        obj = _Object(entry["name"], type_by_name[entry["type"]])
         202 +        data[obj] = np.array(entry["features"], dtype=np.float32)
         203 +    return _ObjectCentricState(data, type_features)
         204 +
         205 +
         206 +def _ocs_to_payload(state: _ObjectCentricState) -> dict[str, Any]:
         207 +    """Encode a local ObjectCentricState back to the self-contained codec payload."""
         208 +
         209 +    def depth(t: _Type) -> int:
         210 +        n, p = 0, t.parent
         211 +        while p is not None:
         212 +            n, p = n + 1, p.parent
         213 +        return n
         214 +
         215 +    types = sorted(state.type_features, key=lambda t: (depth(t), t.name))
         216 +    return {
         217 +        "types": [
         218 +            {
         219 +                "name": t.name,
         220 +                "parent": t.parent.name if t.parent is not None else None,
         221 +                "features": list(state.type_features[t]),
         222 +            }
         223 +            for t in types
         224 +        ],
         225 +        "objects": [
         226 +            {
         227 +                "name": o.name,
         228 +                "type": o.type.name,
         229 +                "features": [float(v) for v in state.data[o]],
         230 +            }
         231 +            for o in sorted(state.data, key=lambda o: o.name)
         232 +        ],
         233 +    }
         234 +
         235 +
         236 +def _encode(obj: Any) -> Any:
         237 +    """Encode values as tagged JSON (mirrors robocode.utils.env_server)."""
         238 +    if isinstance(obj, _ObjectCentricState):
         239 +        return {_OCS_TAG: _ocs_to_payload(obj)}
         240 +    if isinstance(obj, np.generic):
         241 +        return obj.item()
         242 +    if isinstance(obj, np.ndarray):
         243 +        return {_NDARRAY_TAG: obj.tolist(), "dtype": str(obj.dtype)}
         244 +    if isinstance(obj, dict):
         245 +        return {key: _encode(value) for key, value in obj.items()}
         246 +    if isinstance(obj, (list, tuple)):
         247 +        return [_encode(value) for value in obj]
         248 +    return obj
         249 +
         250 +
         251 +def _decode(obj: Any) -> Any:
         252 +    """Decode tagged JSON (mirrors robocode.utils.env_server)."""
         253 +    if isinstance(obj, dict):
         254 +        if _OCS_TAG in obj:
         255 +            return _ocs_from_payload(obj[_OCS_TAG])
         256 +        if _NDARRAY_TAG in obj:
         257 +            return np.array(obj[_NDARRAY_TAG], dtype=np.dtype(obj["dtype"]))
         258 +        return {key: _decode(value) for key, value in obj.items()}
         259 +    if isinstance(obj, list):
         260 +        return [_decode(value) for value in obj]
         261 +    return obj
         262 +
         263 +
         264 +def _encode_ref(obj: Any) -> Any:
         265 +    """Encode args/targets for the remote-object proxy commands.
         266 +
         267 +    Same as ``_encode`` but ``_RemoteHandle`` objects serialize to their
         268 +    ``{"__handle__": id}`` token so the host resolves them from its registry.
         269 +    Used only by devectorize/vectorize/getattr/call requests.
         270 +    """
         271 +    if isinstance(obj, _RemoteHandle):
         272 +        return {_HANDLE_TAG: obj._handle_id}  # pylint: disable=protected-access
         273 +    if isinstance(obj, _ObjectCentricState):
         274 +        return {_OCS_TAG: _ocs_to_payload(obj)}
         275 +    if isinstance(obj, np.generic):
         276 +        return obj.item()
         277 +    if isinstance(obj, np.ndarray):
         278 +        return {_NDARRAY_TAG: obj.tolist(), "dtype": str(obj.dtype)}
         279 +    if isinstance(obj, dict):
         280 +        return {key: _encode_ref(value) for key, value in obj.items()}
         281 +    if isinstance(obj, (list, tuple)):
         282 +        return [_encode_ref(value) for value in obj]
         283 +    if isinstance(obj, (set, frozenset)):
         284 +        return {_SET_TAG: [_encode_ref(value) for value in obj]}
         285 +    return obj
         286 +
         287 +
         288 +class SpaceInfo:
         289 +    """Metadata for a Box space: shape, low, high, dtype, and sample()."""
         290 +
         291 +    def __init__(self, spec: dict[str, Any]) -> None:
         292 +        if spec["type"] != "Box":
         293 +            raise TypeError(
         294 +                f"Unsupported space type {spec['type']!r}; extend SpaceInfo "
         295 +                "alongside the server's serialize_space"
         296 +            )
         297 +        self.shape: tuple[int, ...] = tuple(spec["shape"])
         298 +        self.dtype: np.dtype[Any] = np.dtype(spec["dtype"])
         299 +        self.low: np.ndarray = np.array(spec["low"], dtype=self.dtype)
         300 +        self.high: np.ndarray = np.array(spec["high"], dtype=self.dtype)
         301 +
         302 +    def sample(self, rng: np.random.Generator | None = None) -> np.ndarray:
         303 +        """Sample uniformly between low and high."""
         304 +        if rng is None:
         305 +            rng = np.random.default_rng()
         306 +        return rng.uniform(self.low, self.high).astype(self.dtype)
         307 +
         308 +
         309 +class _RemoteHandle:
         310 +    """A reference to a host-side object, used over the env server.
         311 +
         312 +    Attribute access and calls are proxied to the host: ``handle.method(...)``
         313 +    issues a ``getattr`` (returning another handle for the bound method) then a
         314 +    ``call``. Returned values are decoded the same way as any response, so a
         315 +    scalar/ndarray comes back inline and another object comes back as a nested
         316 +    ``_RemoteHandle``. Private/dunder attributes are refused client-side, both
         317 +    to avoid surprise round-trips and to mirror the host security guard.
         318 +    """
         319 +
         320 +    def __init__(self, client: "BlackboxEnv", handle_id: str) -> None:
         321 +        # Use object.__setattr__-free plain assignment; __getattr__ only fires
         322 +        # for names not found normally, and these two are set here.
         323 +        self._client = client
         324 +        self._handle_id = handle_id
         325 +
         326 +    def __getattr__(self, name: str) -> Any:
         327 +        if name.startswith("_"):
         328 +            raise AttributeError(
         329 +                f"refusing private/dunder attribute access on remote handle: "
         330 +                f"{name!r}"
         331 +            )
         332 +        response = self._client._request(  # pylint: disable=protected-access
         333 +            {
         334 +                "cmd": "getattr",
         335 +                "target": {_HANDLE_TAG: self._handle_id},
         336 +                "name": name,
         337 +            }
         338 +        )
         339 +        return self._client._decode_ref(  # pylint: disable=protected-access
         340 +            response["result"]
         341 +        )
         342 +
         343 +    def __call__(self, *args: Any, **kwargs: Any) -> Any:
         344 +        response = self._client._request(  # pylint: disable=protected-access
         345 +            {
         346 +                "cmd": "call",
         347 +                "target": {_HANDLE_TAG: self._handle_id},
         348 +                "args": _encode_ref(list(args)),
         349 +                "kwargs": _encode_ref(kwargs),
         350 +            }
         351 +        )
         352 +        return self._client._decode_ref(  # pylint: disable=protected-access
         353 +            response["result"]
         354 +        )
         355 +
         356 +
         357 +class _RemoteModule:
         358 +    """A reference to a whitelisted host module (e.g. crv_motion_planning).
         359 +
         360 +    Attribute access proxies a ``getattr`` against the ``{"__module__": name}``
         361 +    target, so ``module.plan_crv_actions`` returns a callable handle the agent
         362 +    can invoke. Mirrors how a remote-module primitive is used at eval time,
         363 +    where ``primitives['crv_motion_planning']`` is the real module.
         364 +    """
         365 +
         366 +    def __init__(self, client: "BlackboxEnv", short_name: str) -> None:
         367 +        self._client = client
         368 +        self._short_name = short_name
         369 +
         370 +    def __getattr__(self, name: str) -> Any:
         371 +        if name.startswith("_"):
         372 +            raise AttributeError(
         373 +                f"refusing private/dunder attribute access on remote module: "
         374 +                f"{name!r}"
         375 +            )
         376 +        response = self._client._request(  # pylint: disable=protected-access
         377 +            {
         378 +                "cmd": "getattr",
         379 +                "target": {_MODULE_TAG: self._short_name},
         380 +                "name": name,
         381 +            }
         382 +        )
         383 +        return self._client._decode_ref(  # pylint: disable=protected-access
         384 +            response["result"]
         385 +        )
         386 +
         387 +
         388 +class _BlackboxObservationSpace(SpaceInfo):
         389 +    """Box-space metadata plus client-backed devectorize/vectorize.
         390 +
         391 +    Stands in for the eval-time ``ObjectCentricBoxSpace``: it keeps the
         392 +    shape/low/high/dtype/sample() of a plain ``SpaceInfo`` and adds
         393 +    ``devectorize(obs)`` / ``vectorize(ocs)`` that proxy to the host. The agent
         394 +    writes ``observation_space.devectorize(obs)`` exactly as it would at eval.
         395 +    """
         396 +
         397 +    def __init__(self, spec: dict[str, Any], client: "BlackboxEnv") -> None:
         398 +        super().__init__(spec)
         399 +        self._client = client
         400 +
         401 +    def devectorize(self, obs: Any) -> Any:
         402 +        """Return an object-centric view of *obs* as a remote handle."""
         403 +        return self._client.devectorize(obs)
         404 +
         405 +    def vectorize(self, state: Any) -> np.ndarray:
         406 +        """Return the flat observation vector for an object-centric state."""
         407 +        return self._client.vectorize(state)
         408 +
         409 +
         410 +class _ObjectCentricObservationSpace:
         411 +    """Client-side view of a variable-count env's ObjectCentricStateSpace.
         412 +
         413 +    The observation is already an object-centric state (reconstructed locally from the
         414 +    wire), so this space has no fixed shape/vector: it exposes the domain ``types`` and
         415 +    ``type_features`` the program needs to enumerate objects, matching the eval-time
         416 +    ``observation_space.types``. There is no ``devectorize`` -- the state is not a
         417 +    vector.
         418 +    """
         419 +
         420 +    def __init__(self, spec: dict[str, Any]) -> None:
         421 +        self._type_by_name, self._type_features = _build_local_types(spec["types"])
         422 +
         423 +    @property
         424 +    def types(self) -> set[_Type]:
         425 +        """The domain object types (matches the eval-time observation_space.types)."""
         426 +        return set(self._type_features)
         427 +
         428 +    @property
         429 +    def type_features(self) -> dict[_Type, list[str]]:
         430 +        """Feature names for each type."""
         431 +        return {t: list(f) for t, f in self._type_features.items()}
         432 +
         433 +    def get_type(self, name: str) -> _Type:
         434 +        """The domain type with the given name (e.g. ``"rectangle"``)."""
         435 +        return self._type_by_name[name]
         436 +
         437 +
         438 +class BlackboxEnv:
         439 +    """A live environment instance, accessed over the wire."""
         440 +
         441 +    def __init__(self, meta: dict[str, Any], sandbox_root: Any = None) -> None:
         442 +        obs_spec = meta["observation_space"]
         443 +        self._strict = bool(meta.get("strict", False))
         444 +        # A variable-count env sends object-centric states, reconstructed locally; a
         445 +        # fixed-count env sends Box vectors as before.
         446 +        self._object_centric = obs_spec.get("type") == "ObjectCentric"
         447 +        if self._object_centric:
         448 +            self.observation_space: Any = _ObjectCentricObservationSpace(obs_spec)
         449 +        elif self._strict:
         450 +            # Strict blackbox exposes only generic array metadata. In particular,
         451 +            # do not attach the host-backed devectorize/vectorize helpers that make
         452 +            # the legacy blackbox convenient but confound the isolation ablation.
         453 +            self.observation_space = SpaceInfo(obs_spec)
         454 +        else:
         455 +            self.observation_space = _BlackboxObservationSpace(obs_spec, self)
         456 +        self.action_space = SpaceInfo(meta["action_space"])
         457 +        self.max_steps: int | None = meta["max_steps"]
         458 +        # How make_primitives rebuilds the eval-time primitives dict (see
         459 +        # robocode.primitives.blackbox_primitive_manifest). Empty when the
         460 +        # run configures no primitives.
         461 +        self._primitive_manifest: list[dict[str, Any]] = meta.get("primitives", [])
         462 +        # Where render_policy looks for approach.py and make_primitives imports
         463 +        # generic primitive sources; the sandbox dir in real runs (set by
         464 +        # make_env), the current dir for ad-hoc construction.
         465 +        self._sandbox_root = (
         466 +            Path(sandbox_root) if sandbox_root is not None else Path.cwd()
         467 +        )
         468 +        self._token: str = meta["token"]
         469 +        self._sock = socket.create_connection((meta["host"], meta["port"]))
         470 +        self._file = self._sock.makefile("rwb")
         471 +
         472 +    def _request(self, payload: dict[str, Any]) -> dict[str, Any]:
         473 +        payload["token"] = self._token
         474 +        self._file.write(json.dumps(payload).encode("utf-8") + b"\n")
         475 +        self._file.flush()
         476 +        line = self._file.readline()
         477 +        if not line:
         478 +            raise RuntimeError("Connection to the environment server was closed")
         479 +        response = json.loads(line)
         480 +        if "error" in response:
         481 +            raise RuntimeError(f"Environment server error: {response['error']}")
         482 +        return _decode(response)
         483 +
         484 +    def _decode_ref(self, obj: Any) -> Any:
         485 +        """Decode a remote-command result, mapping handles to _RemoteHandle.
         486 +
         487 +        ``_request`` already ran ``_decode`` over the response (so ndarrays are
         488 +        arrays), but it leaves ``{"__handle__": id}`` dicts intact since it does
         489 +        not know the handle tag. Here we turn those into ``_RemoteHandle``
         490 +        objects and recurse through the remaining containers.
         491 +        """
         492 +        if isinstance(obj, dict):
         493 +            if _HANDLE_TAG in obj:
         494 +                return _RemoteHandle(self, obj[_HANDLE_TAG])
         495 +            if _SET_TAG in obj:
         496 +                return {self._decode_ref(value) for value in obj[_SET_TAG]}
         497 +            return {key: self._decode_ref(value) for key, value in obj.items()}
         498 +        if isinstance(obj, list):
         499 +            return [self._decode_ref(value) for value in obj]
         500 +        return obj
         501 +
         502 +    def devectorize(self, obs: Any) -> _RemoteHandle:
         503 +        """Return an object-centric view of *obs* (a remote ObjectCentricState).
         504 +
         505 +        Proxies ``observation_space.devectorize`` to the host. The returned
         506 +        handle exposes the public ObjectCentricState API (``get_object_names``,
         507 +        ``get_object_from_name``, ``get_objects``, ``get``, ``set``, ``copy``,
         508 +        ...) over the wire. Pass it straight to the CRV planners from
         509 +        ``make_primitives``.
         510 +        """
         511 +        response = self._request(
         512 +            {"cmd": "devectorize", "obs": _encode(np.asarray(obs))}
         513 +        )
         514 +        return self._decode_ref(response["result"])
         515 +
         516 +    def vectorize(self, state: Any) -> np.ndarray:
         517 +        """Return the flat observation vector for an object-centric state handle."""
         518 +        response = self._request({"cmd": "vectorize", "state": _encode_ref(state)})
         519 +        return self._decode_ref(response["result"])
         520 +
         521 +    def reset(
         522 +        self, seed: int | None = None, options: dict[str, Any] | None = None
         523 +    ) -> tuple[np.ndarray, dict[str, Any]]:
         524 +        """Reset the environment; returns (obs, info)."""
         525 +        response = self._request({"cmd": "reset", "seed": seed, "options": options})
         526 +        return response["obs"], response["info"]
         527 +
         528 +    def step(self, action: Any) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
         529 +        """Step the environment; returns (obs, reward, terminated, truncated, info)."""
         530 +        action = np.asarray(action, dtype=self.action_space.dtype)
         531 +        response = self._request({"cmd": "step", "action": _encode(action)})
         532 +        return (
         533 +            response["obs"],
         534 +            response["reward"],
         535 +            response["terminated"],
         536 +            response["truncated"],
         537 +            response["info"],
         538 +        )
         539 +
         540 +    def get_state(self) -> Any:
         541 +        """Return a snapshot of the full environment state.
         542 +
         543 +        A Box vector for a fixed-count env; a local ObjectCentricState for a
         544 +        variable-count env (reconstructed by ``_decode``).
         545 +        """
         546 +        return self._request({"cmd": "get_state"})["state"]
         547 +
         548 +    def _encode_state(self, state: Any) -> Any:
         549 +        """Encode a state for the wire: an object-centric state or a Box vector."""
         550 +        if isinstance(state, _ObjectCentricState):
         551 +            return _encode(state)
         552 +        return _encode(np.asarray(state))
         553 +
         554 +    def render_state(
         555 +        self,
         556 +        seed: int = 42,
         557 +        state: Any = None,
         558 +        label: str = "",
         559 +        object_count: int | None = None,
         560 +    ) -> str:
         561 +        """Render a state on the host; returns a PNG path inside the sandbox.
         562 +
         563 +        Either pass ``seed`` to render the initial state after a reset (with
         564 +        ``object_count`` to pin a variable-count env's object count), or ``state`` (a
         565 +        flat list of floats, as from ``get_state().tolist()``) to render an arbitrary
         566 +        state. The path is relative to the sandbox dir.
         567 +        """
         568 +        if isinstance(state, _ObjectCentricState):
         569 +            state = _encode(state)  # tagged object-centric payload, decoded host-side
         570 +        elif isinstance(state, np.ndarray):
         571 +            state = state.tolist()
         572 +        return self._request(
         573 +            {
         574 +                "cmd": "render_state",
         575 +                "seed": seed,
         576 +                "state": state,
         577 +                "label": label,
         578 +                "object_count": object_count,
         579 +            }
         580 +        )["path"]
         581 +
         582 +    def render_policy(
         583 +        self,
         584 +        seed: int = 42,
         585 +        max_steps: int = 1000,
         586 +        max_frames: int = 100,
         587 +        approach_path: Any = None,
         588 +        object_count: int | None = None,
         589 +    ) -> list[str]:
         590 +        """Run an episode of approach.py here and render the visited states.
         591 +
         592 +        The policy runs in this process: only ``get_action`` (which needs the
         593 +        observation alone) executes locally, while each visited state is
         594 +        rendered on the host via ``render_state``. No approach code runs on the
         595 +        host, so a black-box agent cannot reach the env source through rendering.
         596 +        ``object_count`` pins a variable-count env's object count on the rollout reset.
         597 +        Returns the PNG paths (relative to the sandbox dir).
         598 +        """
         599 +        path = (
         600 +            Path(approach_path)
         601 +            if approach_path is not None
         602 +            else self._sandbox_root / "approach.py"
         603 +        )
         604 +        approach = _load_generated_approach(
         605 +            path, self.action_space, self.observation_space, self.make_primitives()
         606 +        )
         607 +        options = {"object_count": object_count} if object_count is not None else None
         608 +        obs, info = self.reset(seed=seed, options=options)
         609 +        approach.reset(obs, info)
         610 +        # Strict mode deliberately withholds raw state snapshots. Its observations
         611 +        # are nevertheless renderable, so use them to visualize a policy without
         612 +        # opening the get_state channel to agent scripts.
         613 +        states = [obs if self._strict else self.get_state()]
         614 +        for _ in range(max_steps):
         615 +            obs, reward, terminated, truncated, info = self.step(
         616 +                approach.get_action(obs)
         617 +            )
         618 +            if hasattr(approach, "update"):
         619 +                approach.update(obs, reward, terminated or truncated, info)
         620 +            states.append(obs if self._strict else self.get_state())
         621 +            if terminated or truncated:
         622 +                break
         623 +        return [
         624 +            self.render_state(state=state, label=f"policy_seed{seed}_{i:04d}")
         625 +            for i, state in enumerate(states[:max_frames])
         626 +        ]
         627 +
         628 +    def set_state(self, state: Any) -> None:
         629 +        """Restore a state snapshot previously returned by get_state()."""
         630 +        self._request({"cmd": "set_state", "state": self._encode_state(state)})
         631 +
         632 +    def check_action_collision(self, state: Any, action: Any) -> bool:
         633 +        """Return True if taking *action* in *state* causes a collision.
         634 +
         635 +        Runs the env-dependent collision primitive on the host (the sandbox
         636 +        lacks the env source), against this connection's env. Mirrors the
         637 +        eval-time ``primitives['check_action_collision']`` callable, so test
         638 +        scripts that get it from ``make_primitives`` call it the same way.
         639 +        """
         640 +        response = self._request(
         641 +            {
         642 +                "cmd": "check_action_collision",
         643 +                "state": self._encode_state(state),
         644 +                "action": _encode(np.asarray(action, dtype=self.action_space.dtype)),
         645 +            }
         646 +        )
         647 +        return response["collision"]
         648 +
         649 +    def make_primitives(self) -> dict[str, Any]:
         650 +        """Build the eval-time primitives dict for this black-box env.
         651 +
         652 +        Black-box counterpart of ``robocode.primitives.build_primitives``:
         653 +        env-dependent primitives proxy to the host, while generic ones are
         654 +        imported from their copies under ``primitives/`` in the sandbox. Use
         655 +        it in test scripts so they exercise exactly the primitives the harness
         656 +        passes to ``GeneratedApproach`` at evaluation time::
         657 +
         658 +            from env_client import make_env
         659 +
         660 +            env = make_env()
         661 +            primitives = env.make_primitives()
         662 +        """
         663 +        sandbox_dir = str(self._sandbox_root.resolve())
         664 +        if sandbox_dir not in sys.path:
         665 +            sys.path.insert(0, sandbox_dir)
         666 +        primitives: dict[str, Any] = {}
         667 +        for spec in self._primitive_manifest:
         668 +            if spec["kind"] == "host_proxy":
         669 +                primitives[spec["name"]] = getattr(self, spec["name"])
         670 +            elif spec["kind"] == "remote_module":
         671 +                # The module source is withheld from the sandbox; reach it on
         672 +                # the host via a remote-module proxy (e.g. crv_motion_planning).
         673 +                primitives[spec["name"]] = _RemoteModule(self, spec["module"])
         674 +            else:
         675 +                module = importlib.import_module(f"primitives.{spec['module']}")
         676 +                primitives[spec["name"]] = (
         677 +                    module if spec["attr"] is None else getattr(module, spec["attr"])
         678 +                )
         679 +        return primitives
         680 +
         681 +    def close(self) -> None:
         682 +        """Close the connection (and the server-side environment)."""
         683 +        try:
         684 +            self._file.write(
         685 +                json.dumps({"cmd": "close", "token": self._token}).encode("utf-8")
         686 +                + b"\n"
         687 +            )
         688 +            self._file.flush()
         689 +        finally:
         690 +            # makefile() wraps a dup of the socket; close it too so the buffered
         691 +            # file object does not leak (ResourceWarning) when close() runs.
         692 +            self._file.close()
         693 +            self._sock.close()
         694 +
         695 +    def __enter__(self) -> "BlackboxEnv":
         696 +        return self
         697 +
         698 +    def __exit__(self, *exc_info: Any) -> None:
         699 +        self.close()
         700 +
         701 +
         702 +def _load_generated_approach(
         703 +    path: Path, action_space: Any, observation_space: Any, primitives: dict[str, Any]
         704 +) -> Any:
         705 +    """Exec ``approach.py`` and instantiate its ``GeneratedApproach``.
         706 +
         707 +    Mirrors ``robocode.utils.episode.load_generated_approach``; duplicated here
         708 +    (like the codec above) because this module must stay importable with only
         709 +    the standard library and numpy, since it is copied standalone into the
         710 +    sandbox. Used only by ``render_policy`` for visual debugging.
         711 +    """
         712 +    sandbox_dir = str(path.resolve().parent)
         713 +    added = sandbox_dir not in sys.path
         714 +    if added:
         715 +        sys.path.insert(0, sandbox_dir)
         716 +    try:
         717 +        namespace: dict[str, Any] = {"__file__": str(path)}
         718 +        exec(  # pylint: disable=exec-used
         719 +            compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace
         720 +        )
         721 +    finally:
         722 +        if added:
         723 +            sys.path.remove(sandbox_dir)
         724 +    return namespace["GeneratedApproach"](
         725 +        action_space, observation_space, primitives=primitives
         726 +    )
         727 +
         728 +
         729 +def make_env(metadata_path: Any = None) -> BlackboxEnv:
         730 +    """Connect to the environment server; returns a fresh env instance.
         731 +
         732 +    *metadata_path* defaults to ``env_spaces.json`` next to this module
         733 +    (the agent's sandbox copy); the MCP server passes an explicit path.
         734 +    """
         735 +    path = Path(metadata_path) if metadata_path is not None else _METADATA_PATH
         736 +    meta = json.loads(path.read_text(encoding="utf-8"))
         737 +    return BlackboxEnv(meta, sandbox_root=path.parent)
diff --git a/dev/env_spaces.json b/dev/env_spaces.json
new file mode 100644
index 0000000..1d4e8d4
--- /dev/null
+++ b/dev/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "a55f540c5f383484c0efbffe8d1ca4c1", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
diff --git a/dev/res_t.txt b/dev/res_t.txt
new file mode 100644
index 0000000..026545b
--- /dev/null
+++ b/dev/res_t.txt
@@ -0,0 +1,41 @@
           1 +(0, 2, True, 37, 49.8, 0.74, 0.196)
           2 +(1, 1, True, 27, 33.1, 1.85, 1.119)
           3 +(2, 2, True, 32, 41.3, 0.93, 0.329)
           4 +(3, 2, True, 32, 44.4, 0.79, 0.196)
           5 +(4, 2, True, 34, 41.9, 0.83, 0.18)
           6 +(5, 2, True, 35, 46.9, 0.74, 0.212)
           7 +(6, 1, True, 20, 15.6, 0.52, 0.229)
           8 +(7, 2, True, 27, 31.9, 0.68, 0.312)
           9 +(8, 2, True, 26, 43.2, 0.64, 0.243)
          10 +(9, 1, True, 23, 40.2, 0.35, 0.096)
          11 +(10, 2, True, 25, 38.4, 0.33, 0.095)
          12 +(11, 0, True, 13, 15.5, 0.22, 0.143)
          13 +(12, 1, True, 23, 29.5, 0.48, 0.131)
          14 +(13, 2, True, 43, 53.2, 0.78, 0.197)
          15 +(14, 0, True, 15, 13.6, 0.2, 0.066)
          16 +(15, 2, True, 31, 39.2, 0.48, 0.126)
          17 +(16, 1, True, 19, 18.6, 0.26, 0.095)
          18 +(17, 2, True, 30, 38.5, 0.57, 0.122)
          19 +(18, 2, True, 18, 20.1, 0.43, 0.223)
          20 +(19, 1, True, 28, 35.6, 0.66, 0.231)
          21 +(20, 2, True, 33, 43.2, 0.61, 0.177)
          22 +(21, 0, True, 14, 11.5, 0.13, 0.084)
          23 +(22, 2, True, 19, 25.2, 0.46, 0.233)
          24 +(23, 0, True, 16, 28.8, 0.33, 0.269)
          25 +(24, 1, True, 13, 22.1, 0.25, 0.182)
          26 +(25, 1, True, 24, 49.8, 0.54, 0.23)
          27 +(26, 2, True, 20, 28.0, 0.63, 0.265)
          28 +(27, 0, True, 23, 53.0, 0.2, 0.117)
          29 +(28, 1, True, 50, 117.1, 1.0, 0.508)
          30 +(29, 2, True, 13, 21.6, 0.46, 0.322)
          31 +(30, 0, True, 16, 46.0, 0.25, 0.154)
          32 +(31, 1, True, 28, 63.6, 0.51, 0.176)
          33 +(32, 2, True, 27, 62.3, 0.45, 0.146)
          34 +(33, 2, True, 28, 78.7, 0.41, 0.071)
          35 +(34, 0, True, 11, 21.1, 0.05, 0.022)
          36 +(35, 0, True, 11, 15.5, 0.1, 0.069)
          37 +(36, 1, True, 15, 26.0, 0.21, 0.065)
          38 +(37, 0, True, 12, 26.3, 0.17, 0.084)
          39 +(38, 0, True, 13, 17.8, 0.13, 0.08)
          40 +(39, 2, True, 37, 49.8, 0.28, 0.052)
          41 +success 40 / 40 mean steps 24.025
diff --git a/dev/res_t5.txt b/dev/res_t5.txt
new file mode 100644
index 0000000..22abaaa
--- /dev/null
+++ b/dev/res_t5.txt
@@ -0,0 +1,25 @@
           1 +(100, 5, True, 70, 139.7, 1.18, 0.117)
           2 +(101, 5, True, 66, 150.4, 1.52, 0.465)
           3 +(102, 5, True, 67, 148.1, 1.84, 0.374)
           4 +(103, 5, True, 71, 150.4, 2.67, 1.327)
           5 +(104, 5, True, 126, 277.5, 2.87, 0.541)
           6 +(105, 5, True, 79, 146.1, 2.06, 0.525)
           7 +(106, 5, True, 52, 103.1, 1.58, 0.261)
           8 +(107, 5, True, 54, 103.2, 1.64, 0.393)
           9 +(108, 5, True, 70, 136.5, 0.82, 0.115)
          10 +(109, 5, True, 51, 93.6, 0.85, 0.206)
          11 +(110, 5, True, 42, 79.5, 0.58, 0.079)
          12 +(111, 5, True, 52, 85.0, 0.78, 0.167)
          13 +(112, 5, True, 133, 300.0, 2.74, 0.631)
          14 +(113, 5, True, 27, 53.8, 0.46, 0.114)
          15 +(114, 5, True, 42, 71.1, 0.34, 0.042)
          16 +(115, 5, True, 63, 145.4, 1.18, 0.156)
          17 +(116, 5, True, 39, 79.6, 0.62, 0.094)
          18 +(117, 5, True, 35, 83.6, 0.57, 0.156)
          19 +(118, 5, True, 80, 160.5, 1.5, 0.216)
          20 +(119, 5, True, 77, 158.3, 1.18, 0.12)
          21 +(120, 5, True, 55, 116.3, 1.04, 0.209)
          22 +(121, 5, True, 49, 109.5, 0.64, 0.109)
          23 +(122, 5, True, 55, 106.0, 3.35, 2.066)
          24 +(123, 5, True, 65, 110.5, 1.08, 0.192)
          25 +success 24 / 24 mean steps 63.333333333333336
diff --git a/dev/tally.py b/dev/tally.py
new file mode 100644
index 0000000..a1cad40
--- /dev/null
+++ b/dev/tally.py
@@ -0,0 +1,16 @@
           1 +import sys, numpy as np, collections
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +cnt=collections.Counter(); env=make_env(); tot=0
           5 +for seed in range(int(sys.argv[1]), int(sys.argv[2])):
           6 +    obs, info = env.reset(seed=seed)
           7 +    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +    for t in range(1000):
           9 +        a = ap.get_action(obs)
          10 +        c = ap.cur
          11 +        tag = "grip" if c is None else (c[0] if c[0]!="move" else c[3])
          12 +        if tag=="travel": tag += "-J" if (ap.jplan is not None and ap.jplan is not False) else "-C"
          13 +        cnt[tag]+=1; tot+=1
          14 +        obs, r, term, trunc, info = env.step(a)
          15 +        if term: break
          16 +print(tot, cnt.most_common())
diff --git a/dev/test_approach.py b/dev/test_approach.py
new file mode 100644
index 0000000..3f00c83
--- /dev/null
+++ b/dev/test_approach.py
@@ -0,0 +1,27 @@
           1 +import sys, time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +OC=None
           5 +def run(seed, verbose=False):
           6 +    env = make_env()
           7 +    obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
           8 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +    t = time.time(); ap.reset(obs, info)
          10 +    ret = 0; steps = 0; term = False; tot_a = 0.0; max_a = 0.0
          11 +    for steps in range(1, env.max_steps + 1):
          12 +        t1 = time.time(); a = ap.get_action(obs); ta = time.time() - t1
          13 +        tot_a += ta; max_a = max(max_a, ta)
          14 +        obs, r, term, trunc, info = env.step(a)
          15 +        ret += r
          16 +        if term or trunc: break
          17 +    dt = time.time() - t
          18 +    env.close()
          19 +    return seed, info.get('object_count'), term, steps, round(dt, 1), round(tot_a, 2), round(max_a, 3)
          20 +if __name__ == "__main__":
          21 +    from concurrent.futures import ThreadPoolExecutor
          22 +    seeds = list(range(int(sys.argv[1]), int(sys.argv[2])))
          23 +    if len(sys.argv) > 3: OC = int(sys.argv[3])
          24 +    with ThreadPoolExecutor(8) as ex:
          25 +        res = list(ex.map(run, seeds))
          26 +    for r in res: print(r)
          27 +    print("success", sum(r[2] for r in res), "/", len(res), "mean steps", np.mean([r[3] for r in res]))
diff --git a/probe_f.py b/probe_f.py
new file mode 100644
index 0000000..120bb72
--- /dev/null
+++ b/probe_f.py
@@ -0,0 +1,6 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +env = make_env(); obs, info = env.reset(seed=0)
           4 +r = obs.get_object_from_name("robot"); print("init", obs.get(r,"finger_state"))
           5 +a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a); print("closed", obs.get(r,"finger_state"))
           6 +a[10]=1; obs,*_=env.step(a); print("open", obs.get(r,"finger_state"))
diff --git a/res_f8.txt b/res_f8.txt
new file mode 100644
index 0000000..cc144d5
--- /dev/null
+++ b/res_f8.txt
@@ -0,0 +1,25 @@
           1 +(0, 8, True, 75, 50.2, 2.47, 0.432)
           2 +(1, 8, True, 90, 68.3, 15.06, 5.971)
           3 +(2, 8, True, 60, 34.5, 2.52, 1.087)
           4 +(3, 8, True, 47, 29.9, 1.87, 0.602)
           5 +(4, 8, True, 131, 69.9, 2.62, 0.147)
           6 +(5, 8, True, 87, 37.1, 2.58, 0.53)
           7 +(6, 8, True, 359, 127.1, 6.52, 0.56)
           8 +(7, 8, True, 92, 42.6, 2.64, 0.283)
           9 +(8, 8, True, 93, 72.9, 18.26, 7.135)
          10 +(9, 8, True, 140, 102.5, 24.36, 5.278)
          11 +(10, 8, True, 70, 37.0, 1.99, 0.493)
          12 +(11, 8, True, 111, 72.1, 4.34, 0.731)
          13 +(12, 8, True, 101, 52.8, 3.36, 0.342)
          14 +(13, 8, True, 281, 100.4, 7.3, 0.579)
          15 +(14, 8, True, 44, 17.5, 1.95, 0.319)
          16 +(15, 8, True, 132, 71.7, 3.51, 0.363)
          17 +(16, 8, True, 49, 23.9, 1.58, 0.257)
          18 +(17, 8, True, 51, 23.9, 1.89, 0.314)
          19 +(18, 8, True, 106, 52.7, 3.24, 0.48)
          20 +(19, 8, True, 313, 52.1, 4.33, 0.426)
          21 +(20, 8, True, 62, 30.4, 1.62, 0.272)
          22 +(21, 8, True, 99, 37.9, 2.83, 0.54)
          23 +(22, 8, True, 60, 24.9, 1.57, 0.217)
          24 +(23, 8, True, 64, 22.8, 1.95, 0.237)
          25 +success 24 / 24 mean steps 113.20833333333333
diff --git a/res_t.txt b/res_t.txt
index 0c4bdb4..63032d7 100644
--- a/res_t.txt
+++ b/res_t.txt
@@ -1,41 +1,41 @@
    1        -(0, 2, True, 27, 26.7, 0.34, 0.091)
    2        -(1, 1, True, 26, 24.7, 0.8, 0.516)
    3        -(2, 2, True, 35, 41.6, 0.58, 0.113)
    4        -(3, 2, True, 33, 34.2, 0.62, 0.19)
    5        -(4, 2, True, 36, 46.2, 0.62, 0.111)
    6        -(5, 2, True, 41, 49.2, 1.04, 0.257)
    7        -(6, 1, True, 21, 18.2, 0.28, 0.101)
    8        -(7, 2, True, 33, 33.5, 0.37, 0.068)
    9        -(8, 2, True, 26, 34.0, 0.82, 0.215)
   10        -(9, 1, True, 23, 28.9, 0.3, 0.065)
   11        -(10, 2, True, 25, 37.8, 0.32, 0.078)
   12        -(11, 0, True, 14, 17.9, 0.28, 0.108)
   13        -(12, 1, True, 28, 35.5, 0.83, 0.317)
   14        -(13, 2, True, 44, 78.7, 0.58, 0.112)
   15        -(14, 0, True, 11, 10.6, 0.1, 0.069)
   16        -(15, 2, True, 32, 54.8, 0.92, 0.321)
   17        -(16, 1, True, 19, 36.8, 0.7, 0.269)
   18        -(17, 2, True, 34, 66.9, 0.64, 0.186)
   19        -(18, 2, True, 22, 46.2, 1.09, 0.359)
   20        -(19, 1, True, 31, 51.7, 0.65, 0.23)
   21        -(20, 2, True, 36, 66.8, 0.79, 0.184)
   22        -(21, 0, True, 15, 22.6, 0.19, 0.105)
   23        -(22, 2, True, 20, 29.0, 0.62, 0.26)
   24        -(23, 0, True, 19, 20.0, 0.57, 0.273)
   25        -(24, 1, True, 14, 19.0, 0.28, 0.166)
   26        -(25, 1, True, 26, 35.9, 0.58, 0.363)
   27        -(26, 2, True, 20, 31.5, 0.28, 0.126)
   28        -(27, 0, True, 27, 30.5, 0.46, 0.296)
   29        -(28, 1, True, 53, 77.1, 1.21, 0.232)
   30        -(29, 2, True, 13, 19.6, 0.18, 0.109)
   31        -(30, 0, True, 18, 26.5, 0.24, 0.125)
   32        -(31, 1, True, 29, 46.6, 0.53, 0.156)
   33        -(32, 2, True, 27, 46.8, 0.49, 0.126)
   34        -(33, 2, True, 31, 51.1, 0.69, 0.128)
   35        -(34, 0, True, 12, 15.3, 0.16, 0.101)
   36        -(35, 0, True, 12, 15.7, 0.29, 0.12)
   37        -(36, 1, True, 17, 26.5, 0.46, 0.29)
   38        -(37, 0, True, 12, 16.0, 0.19, 0.126)
   39        -(38, 0, True, 14, 13.6, 0.33, 0.179)
   40        -(39, 2, True, 37, 31.7, 0.42, 0.079)
   41        -success 40 / 40 mean steps 25.325
           1 +(0, 2, True, 37, 29.0, 0.65, 0.168)
           2 +(1, 1, True, 27, 16.8, 0.69, 0.325)
           3 +(2, 2, True, 32, 30.9, 0.6, 0.154)
           4 +(3, 2, True, 32, 23.1, 0.56, 0.222)
           5 +(4, 2, True, 34, 17.6, 0.36, 0.061)
           6 +(5, 2, True, 35, 28.4, 0.64, 0.204)
           7 +(6, 1, True, 20, 11.8, 0.31, 0.133)
           8 +(7, 2, True, 27, 16.0, 0.33, 0.106)
           9 +(8, 2, True, 26, 25.3, 0.68, 0.314)
          10 +(9, 1, True, 23, 24.8, 0.31, 0.086)
          11 +(10, 2, True, 25, 28.2, 0.31, 0.08)
          12 +(11, 0, True, 13, 13.3, 0.14, 0.065)
          13 +(12, 1, True, 23, 23.4, 0.5, 0.242)
          14 +(13, 2, True, 43, 51.7, 0.79, 0.245)
          15 +(14, 0, True, 15, 9.4, 0.11, 0.037)
          16 +(15, 2, True, 31, 30.9, 0.82, 0.391)
          17 +(16, 1, True, 19, 15.2, 0.26, 0.062)
          18 +(17, 2, True, 30, 29.4, 0.35, 0.062)
          19 +(18, 2, True, 18, 17.2, 0.44, 0.28)
          20 +(19, 1, True, 28, 29.3, 0.52, 0.273)
          21 +(20, 2, True, 33, 35.5, 0.62, 0.294)
          22 +(21, 0, True, 14, 13.3, 0.24, 0.091)
          23 +(22, 2, True, 19, 16.3, 0.21, 0.057)
          24 +(23, 0, True, 16, 27.2, 0.26, 0.212)
          25 +(24, 1, True, 13, 20.6, 0.1, 0.051)
          26 +(25, 1, True, 24, 33.5, 0.22, 0.071)
          27 +(26, 2, True, 20, 25.8, 0.52, 0.319)
          28 +(27, 0, True, 23, 25.6, 0.2, 0.141)
          29 +(28, 1, True, 50, 46.2, 0.66, 0.161)
          30 +(29, 2, True, 13, 13.5, 0.16, 0.092)
          31 +(30, 0, True, 16, 23.1, 0.23, 0.111)
          32 +(31, 1, True, 28, 31.3, 0.58, 0.259)
          33 +(32, 2, True, 27, 27.6, 0.53, 0.177)
          34 +(33, 2, True, 28, 27.5, 0.5, 0.134)
          35 +(34, 0, True, 11, 13.9, 0.07, 0.029)
          36 +(35, 0, True, 11, 13.5, 0.11, 0.054)
          37 +(36, 1, True, 15, 14.3, 0.21, 0.089)
          38 +(37, 0, True, 12, 10.0, 0.21, 0.153)
          39 +(38, 0, True, 13, 6.7, 0.21, 0.106)
          40 +(39, 2, True, 37, 5.5, 0.52, 0.155)
          41 +success 40 / 40 mean steps 24.025
diff --git a/res_t2.txt b/res_t2.txt
index 0835025..dc81692 100644
--- a/res_t2.txt
+++ b/res_t2.txt
@@ -1,121 +1,121 @@
    1        -(40, 1, True, 27, 43.5, 0.26, 0.074)
    2        -(41, 1, True, 20, 17.7, 0.17, 0.047)
    3        -(42, 0, True, 14, 11.5, 0.11, 0.052)
    4        -(43, 1, True, 21, 31.5, 0.14, 0.037)
    5        -(44, 2, True, 23, 36.9, 0.33, 0.08)
    6        -(45, 2, True, 34, 53.8, 0.33, 0.076)
    7        -(46, 1, True, 19, 20.3, 0.19, 0.035)
    8        -(47, 0, True, 12, 7.0, 0.08, 0.032)
    9        -(48, 0, True, 13, 19.6, 0.12, 0.056)
   10        -(49, 0, True, 13, 17.0, 0.13, 0.078)
   11        -(50, 2, True, 36, 49.1, 0.35, 0.114)
   12        -(51, 1, True, 20, 23.0, 0.25, 0.106)
   13        -(52, 2, True, 47, 58.1, 0.4, 0.086)
   14        -(53, 2, True, 32, 36.4, 0.34, 0.082)
   15        -(54, 0, True, 14, 19.1, 0.12, 0.056)
   16        -(55, 2, True, 41, 50.1, 0.34, 0.044)
   17        -(56, 1, True, 21, 20.1, 0.22, 0.07)
   18        -(57, 0, True, 12, 11.4, 0.09, 0.035)
   19        -(58, 1, True, 18, 25.8, 0.1, 0.026)
   20        -(59, 2, True, 42, 58.3, 0.46, 0.09)
   21        -(60, 0, True, 12, 14.0, 0.19, 0.105)
   22        -(61, 1, True, 23, 27.5, 0.16, 0.046)
   23        -(62, 1, True, 21, 21.7, 0.2, 0.049)
   24        -(63, 1, True, 23, 32.2, 0.35, 0.211)
   25        -(64, 1, True, 21, 22.7, 0.18, 0.047)
   26        -(65, 0, True, 20, 25.9, 0.12, 0.047)
   27        -(66, 2, True, 30, 39.5, 0.53, 0.164)
   28        -(67, 2, True, 31, 37.9, 0.57, 0.179)
   29        -(68, 1, True, 18, 23.4, 0.19, 0.075)
   30        -(69, 0, True, 13, 13.4, 0.11, 0.068)
   31        -(70, 1, True, 24, 33.0, 2.3, 2.04)
   32        -(71, 2, True, 36, 44.4, 0.57, 0.121)
   33        -(72, 2, True, 45, 61.3, 0.36, 0.074)
   34        -(73, 2, True, 34, 40.0, 0.63, 0.155)
   35        -(74, 0, True, 13, 9.8, 0.3, 0.169)
   36        -(75, 1, True, 21, 21.5, 0.26, 0.076)
   37        -(76, 1, True, 26, 31.6, 0.37, 0.089)
   38        -(77, 0, True, 13, 8.9, 0.13, 0.062)
   39        -(78, 2, True, 21, 24.8, 0.18, 0.048)
   40        -(79, 0, True, 11, 9.0, 0.16, 0.082)
   41        -(80, 2, True, 33, 40.7, 0.4, 0.074)
   42        -(81, 0, True, 15, 16.3, 0.19, 0.123)
   43        -(82, 2, True, 38, 48.7, 0.48, 0.109)
   44        -(83, 2, True, 27, 26.5, 0.38, 0.111)
   45        -(84, 1, True, 21, 18.4, 0.27, 0.056)
   46        -(85, 2, True, 28, 27.8, 0.35, 0.06)
   47        -(86, 2, True, 34, 34.3, 0.4, 0.141)
   48        -(87, 1, True, 26, 27.7, 0.28, 0.07)
   49        -(88, 1, True, 22, 21.8, 0.25, 0.076)
   50        -(89, 2, True, 46, 60.4, 1.2, 0.393)
   51        -(90, 1, True, 20, 26.5, 0.3, 0.076)
   52        -(91, 2, True, 22, 34.6, 0.25, 0.069)
   53        -(92, 1, True, 26, 34.4, 0.48, 0.192)
   54        -(93, 2, True, 43, 65.0, 0.57, 0.082)
   55        -(94, 0, True, 13, 15.7, 0.33, 0.256)
   56        -(95, 1, True, 23, 23.9, 0.24, 0.072)
   57        -(96, 2, True, 33, 40.4, 0.64, 0.246)
   58        -(97, 0, True, 25, 23.9, 0.56, 0.426)
   59        -(98, 1, True, 28, 37.0, 0.27, 0.061)
   60        -(99, 2, True, 29, 31.7, 0.47, 0.095)
   61        -(100, 2, True, 32, 49.5, 0.58, 0.225)
   62        -(101, 0, True, 13, 14.3, 0.2, 0.104)
   63        -(102, 1, True, 22, 23.7, 0.39, 0.111)
   64        -(103, 1, True, 20, 23.7, 0.42, 0.129)
   65        -(104, 2, True, 41, 60.3, 0.61, 0.124)
   66        -(105, 0, True, 13, 15.6, 0.28, 0.166)
   67        -(106, 1, True, 13, 24.9, 0.25, 0.116)
   68        -(107, 0, True, 12, 22.9, 0.2, 0.154)
   69        -(108, 0, True, 13, 22.4, 0.16, 0.066)
   70        -(109, 1, True, 24, 35.9, 0.43, 0.098)
   71        -(110, 1, True, 23, 36.4, 0.34, 0.078)
   72        -(111, 1, True, 20, 28.1, 0.33, 0.072)
   73        -(112, 0, True, 14, 17.0, 0.17, 0.072)
   74        -(113, 0, True, 15, 20.0, 0.15, 0.064)
   75        -(114, 0, True, 14, 17.9, 0.08, 0.038)
   76        -(115, 1, True, 22, 30.6, 0.18, 0.039)
   77        -(116, 0, True, 18, 30.4, 0.14, 0.077)
   78        -(117, 0, True, 13, 22.4, 0.07, 0.034)
   79        -(118, 1, True, 31, 40.2, 0.2, 0.047)
   80        -(119, 1, True, 29, 37.1, 0.52, 0.259)
   81        -(120, 0, True, 14, 15.2, 0.16, 0.08)
   82        -(121, 0, True, 14, 20.0, 0.09, 0.052)
   83        -(122, 2, True, 45, 53.0, 0.36, 0.053)
   84        -(123, 0, True, 14, 13.2, 0.08, 0.043)
   85        -(124, 2, True, 20, 21.3, 0.29, 0.06)
   86        -(125, 1, True, 29, 36.3, 0.19, 0.038)
   87        -(126, 0, True, 14, 22.1, 0.13, 0.058)
   88        -(127, 1, True, 13, 16.5, 0.1, 0.054)
   89        -(128, 2, True, 35, 38.2, 0.45, 0.064)
   90        -(129, 1, True, 23, 23.0, 0.35, 0.093)
   91        -(130, 2, True, 30, 33.5, 0.56, 0.131)
   92        -(131, 1, True, 33, 35.6, 0.59, 0.207)
   93        -(132, 2, True, 29, 26.7, 0.51, 0.11)
   94        -(133, 1, True, 27, 22.7, 0.39, 0.171)
   95        -(134, 2, True, 34, 44.0, 0.59, 0.245)
   96        -(135, 1, True, 22, 27.9, 0.34, 0.073)
   97        -(136, 2, True, 23, 31.0, 0.4, 0.097)
   98        -(137, 1, True, 24, 29.9, 0.35, 0.137)
   99        -(138, 1, True, 24, 29.9, 0.39, 0.18)
  100        -(139, 1, True, 22, 27.4, 0.41, 0.192)
  101        -(140, 1, True, 27, 42.4, 0.51, 0.152)
  102        -(141, 1, True, 22, 30.9, 0.18, 0.044)
  103        -(142, 0, True, 20, 21.5, 0.24, 0.121)
  104        -(143, 2, True, 41, 64.3, 0.32, 0.055)
  105        -(144, 0, True, 14, 25.6, 0.1, 0.031)
  106        -(145, 1, True, 21, 30.2, 0.33, 0.148)
  107        -(146, 2, True, 19, 26.8, 0.22, 0.046)
  108        -(147, 0, True, 12, 16.7, 0.16, 0.086)
  109        -(148, 0, True, 13, 13.5, 0.15, 0.057)
  110        -(149, 0, True, 14, 20.7, 0.07, 0.03)
  111        -(150, 1, True, 15, 18.6, 0.11, 0.043)
  112        -(151, 2, True, 26, 28.7, 0.26, 0.084)
  113        -(152, 2, True, 29, 27.1, 0.44, 0.093)
  114        -(153, 2, True, 32, 25.7, 0.34, 0.098)
  115        -(154, 0, True, 11, 9.7, 0.13, 0.068)
  116        -(155, 0, True, 13, 11.3, 0.12, 0.063)
  117        -(156, 2, True, 45, 17.3, 0.52, 0.11)
  118        -(157, 0, True, 14, 9.2, 0.12, 0.045)
  119        -(158, 1, True, 24, 7.6, 0.33, 0.167)
  120        -(159, 2, True, 30, 5.4, 0.34, 0.098)
  121        -success 120 / 120 mean steps 23.5
           1 +(40, 1, True, 27, 62.8, 0.56, 0.191)
           2 +(41, 1, True, 21, 39.8, 0.29, 0.078)
           3 +(42, 0, True, 14, 42.7, 0.33, 0.218)
           4 +(43, 1, True, 24, 49.3, 0.36, 0.158)
           5 +(44, 2, True, 28, 50.2, 0.38, 0.112)
           6 +(45, 2, True, 37, 65.2, 0.6, 0.25)
           7 +(46, 1, True, 22, 49.9, 0.4, 0.149)
           8 +(47, 0, True, 11, 28.9, 0.24, 0.189)
           9 +(48, 0, True, 12, 24.9, 0.16, 0.117)
          10 +(49, 0, True, 13, 18.7, 0.1, 0.039)
          11 +(50, 2, True, 34, 50.8, 2.45, 2.061)
          12 +(51, 1, True, 18, 22.1, 0.22, 0.094)
          13 +(52, 2, True, 47, 90.4, 1.28, 0.592)
          14 +(53, 2, True, 34, 42.1, 0.86, 0.243)
          15 +(54, 0, True, 14, 19.9, 0.48, 0.3)
          16 +(55, 2, True, 40, 79.0, 0.93, 0.199)
          17 +(56, 1, True, 23, 18.3, 0.39, 0.089)
          18 +(57, 0, True, 12, 9.6, 0.52, 0.317)
          19 +(58, 1, True, 18, 24.1, 0.46, 0.264)
          20 +(59, 2, True, 42, 89.0, 1.69, 0.768)
          21 +(60, 0, True, 10, 17.5, 0.14, 0.077)
          22 +(61, 1, True, 21, 48.3, 0.56, 0.249)
          23 +(62, 1, True, 21, 54.4, 0.29, 0.075)
          24 +(63, 1, True, 26, 36.0, 0.66, 0.136)
          25 +(64, 1, True, 19, 28.4, 0.5, 0.1)
          26 +(65, 0, True, 25, 28.9, 0.32, 0.121)
          27 +(66, 2, True, 36, 55.6, 0.59, 0.125)
          28 +(67, 2, True, 27, 46.1, 0.51, 0.105)
          29 +(68, 1, True, 18, 20.3, 0.43, 0.301)
          30 +(69, 0, True, 13, 11.8, 0.28, 0.183)
          31 +(70, 1, True, 23, 46.4, 2.62, 2.026)
          32 +(71, 2, True, 32, 55.6, 0.86, 0.197)
          33 +(72, 2, True, 45, 75.9, 0.57, 0.115)
          34 +(73, 2, True, 39, 65.6, 0.52, 0.127)
          35 +(74, 0, True, 13, 22.2, 0.36, 0.25)
          36 +(75, 1, True, 19, 23.3, 0.24, 0.102)
          37 +(76, 1, True, 25, 44.5, 0.44, 0.128)
          38 +(77, 0, True, 12, 13.8, 0.14, 0.07)
          39 +(78, 2, True, 25, 40.3, 0.34, 0.132)
          40 +(79, 0, True, 10, 13.6, 0.12, 0.065)
          41 +(80, 2, True, 31, 49.5, 0.49, 0.134)
          42 +(81, 0, True, 15, 23.6, 0.18, 0.12)
          43 +(82, 2, True, 34, 45.4, 0.25, 0.064)
          44 +(83, 2, True, 27, 38.8, 0.41, 0.188)
          45 +(84, 1, True, 25, 29.2, 0.23, 0.075)
          46 +(85, 2, True, 22, 31.1, 0.25, 0.059)
          47 +(86, 2, True, 32, 55.6, 0.4, 0.125)
          48 +(87, 1, True, 25, 40.6, 0.42, 0.142)
          49 +(88, 1, True, 21, 34.4, 0.4, 0.129)
          50 +(89, 2, True, 46, 77.3, 0.68, 0.117)
          51 +(90, 1, True, 18, 23.6, 0.27, 0.096)
          52 +(91, 2, True, 20, 34.2, 0.31, 0.145)
          53 +(92, 1, True, 30, 44.4, 0.36, 0.129)
          54 +(93, 2, True, 42, 69.2, 0.34, 0.053)
          55 +(94, 0, True, 13, 12.5, 0.14, 0.059)
          56 +(95, 1, True, 31, 38.6, 0.32, 0.097)
          57 +(96, 2, True, 34, 42.9, 0.34, 0.069)
          58 +(97, 0, True, 25, 36.5, 0.17, 0.113)
          59 +(98, 1, True, 36, 63.5, 0.38, 0.103)
          60 +(99, 2, True, 29, 47.3, 0.28, 0.042)
          61 +(100, 2, True, 29, 55.3, 0.59, 0.104)
          62 +(101, 0, True, 12, 21.8, 0.16, 0.117)
          63 +(102, 1, True, 22, 41.3, 0.41, 0.141)
          64 +(103, 1, True, 25, 44.1, 0.39, 0.109)
          65 +(104, 2, True, 40, 72.5, 0.65, 0.132)
          66 +(105, 0, True, 12, 16.2, 0.41, 0.15)
          67 +(106, 1, True, 13, 14.9, 0.19, 0.114)
          68 +(107, 0, True, 16, 19.3, 0.24, 0.088)
          69 +(108, 0, True, 16, 18.1, 0.22, 0.105)
          70 +(109, 1, True, 26, 33.4, 0.53, 0.158)
          71 +(110, 1, True, 25, 33.4, 0.4, 0.12)
          72 +(111, 1, True, 18, 24.1, 0.24, 0.087)
          73 +(112, 0, True, 14, 15.3, 0.23, 0.15)
          74 +(113, 0, True, 15, 14.9, 0.22, 0.154)
          75 +(114, 0, True, 13, 14.2, 0.2, 0.081)
          76 +(115, 1, True, 20, 37.9, 0.31, 0.136)
          77 +(116, 0, True, 18, 35.2, 0.2, 0.098)
          78 +(117, 0, True, 12, 20.7, 0.17, 0.103)
          79 +(118, 1, True, 31, 50.4, 0.43, 0.125)
          80 +(119, 1, True, 31, 42.0, 0.69, 0.294)
          81 +(120, 0, True, 13, 19.5, 0.18, 0.137)
          82 +(121, 0, True, 13, 15.9, 0.21, 0.124)
          83 +(122, 2, True, 45, 62.6, 0.7, 0.125)
          84 +(123, 0, True, 14, 15.9, 0.21, 0.111)
          85 +(124, 2, True, 26, 36.4, 0.37, 0.097)
          86 +(125, 1, True, 32, 37.2, 0.48, 0.197)
          87 +(126, 0, True, 13, 14.3, 0.18, 0.123)
          88 +(127, 1, True, 13, 16.6, 0.17, 0.076)
          89 +(128, 2, True, 33, 45.9, 0.77, 0.28)
          90 +(129, 1, True, 22, 24.1, 0.36, 0.14)
          91 +(130, 2, True, 26, 28.7, 0.55, 0.115)
          92 +(131, 1, True, 33, 31.5, 0.61, 0.152)
          93 +(132, 2, True, 28, 35.5, 0.52, 0.125)
          94 +(133, 1, True, 27, 33.3, 0.62, 0.25)
          95 +(134, 2, True, 38, 47.0, 0.63, 0.293)
          96 +(135, 1, True, 23, 27.0, 0.48, 0.196)
          97 +(136, 2, True, 19, 29.3, 0.42, 0.134)
          98 +(137, 1, True, 23, 28.0, 0.41, 0.139)
          99 +(138, 1, True, 20, 30.7, 1.83, 1.571)
         100 +(139, 1, True, 22, 27.8, 0.31, 0.087)
         101 +(140, 1, True, 27, 33.8, 0.4, 0.089)
         102 +(141, 1, True, 28, 34.9, 0.43, 0.181)
         103 +(142, 0, True, 20, 25.9, 0.25, 0.129)
         104 +(143, 2, True, 40, 49.3, 0.51, 0.099)
         105 +(144, 0, True, 17, 14.1, 0.17, 0.051)
         106 +(145, 1, True, 27, 26.6, 0.38, 0.094)
         107 +(146, 2, True, 21, 27.9, 0.36, 0.1)
         108 +(147, 0, True, 12, 12.7, 0.16, 0.066)
         109 +(148, 0, True, 12, 15.9, 0.17, 0.116)
         110 +(149, 0, True, 12, 20.8, 0.1, 0.073)
         111 +(150, 1, True, 15, 21.9, 0.32, 0.223)
         112 +(151, 2, True, 27, 31.5, 0.54, 0.22)
         113 +(152, 2, True, 24, 30.5, 0.74, 0.192)
         114 +(153, 2, True, 37, 30.1, 0.59, 0.081)
         115 +(154, 0, True, 10, 15.4, 0.11, 0.071)
         116 +(155, 0, True, 13, 15.4, 0.18, 0.076)
         117 +(156, 2, True, 44, 20.4, 0.81, 0.244)
         118 +(157, 0, True, 14, 9.7, 0.53, 0.246)
         119 +(158, 1, True, 22, 9.4, 0.41, 0.249)
         120 +(159, 2, True, 26, 7.2, 0.47, 0.164)
         121 +success 120 / 120 mean steps 23.708333333333332
diff --git a/res_t4.txt b/res_t4.txt
index e69de29..266e755 100644
--- a/res_t4.txt
+++ b/res_t4.txt
@@ -0,0 +1,33 @@
           1 +(0, 4, True, 49, 115.6, 0.75, 0.097)
           2 +(1, 4, True, 47, 114.9, 2.34, 1.661)
           3 +(2, 4, True, 58, 130.4, 1.56, 0.288)
           4 +(3, 4, True, 29, 59.9, 0.47, 0.114)
           5 +(4, 4, True, 74, 172.2, 1.18, 0.127)
           6 +(5, 4, True, 65, 149.5, 1.11, 0.111)
           7 +(6, 4, True, 63, 135.7, 1.62, 0.592)
           8 +(7, 4, True, 68, 164.7, 0.86, 0.108)
           9 +(8, 4, True, 66, 152.9, 6.06, 4.802)
          10 +(9, 4, True, 58, 130.1, 6.15, 5.48)
          11 +(10, 4, True, 41, 90.6, 0.85, 0.218)
          12 +(11, 4, True, 73, 164.0, 1.41, 0.168)
          13 +(12, 4, True, 78, 153.9, 1.23, 0.154)
          14 +(13, 4, True, 62, 129.1, 1.25, 0.157)
          15 +(14, 4, True, 29, 72.3, 0.4, 0.056)
          16 +(15, 4, True, 69, 120.8, 1.36, 0.236)
          17 +(16, 4, True, 36, 70.9, 0.78, 0.145)
          18 +(17, 4, True, 52, 78.8, 0.77, 0.11)
          19 +(18, 4, True, 30, 40.5, 0.54, 0.075)
          20 +(19, 4, True, 75, 112.1, 1.87, 0.435)
          21 +(20, 4, True, 58, 80.0, 1.29, 0.183)
          22 +(21, 4, True, 50, 75.3, 1.28, 0.254)
          23 +(22, 4, True, 28, 37.6, 0.69, 0.172)
          24 +(23, 4, True, 61, 93.9, 1.76, 0.276)
          25 +(24, 4, True, 51, 71.7, 1.36, 0.298)
          26 +(25, 4, True, 36, 68.0, 1.21, 0.346)
          27 +(26, 4, True, 45, 83.5, 2.81, 1.436)
          28 +(27, 4, True, 55, 88.2, 1.6, 0.367)
          29 +(28, 4, True, 59, 108.7, 1.51, 0.388)
          30 +(29, 4, True, 44, 67.7, 0.69, 0.105)
          31 +(30, 4, True, 42, 60.3, 0.47, 0.111)
          32 +(31, 4, True, 49, 77.9, 1.06, 0.265)
          33 +success 32 / 32 mean steps 53.125
diff --git a/res_t8.txt b/res_t8.txt
index e69de29..9cd0fb4 100644
--- a/res_t8.txt
+++ b/res_t8.txt
@@ -0,0 +1,33 @@
           1 +(0, 8, True, 82, 64.6, 2.1, 0.364)
           2 +(1, 8, True, 107, 110.0, 15.32, 7.586)
           3 +(2, 8, True, 63, 63.1, 1.96, 0.598)
           4 +(3, 8, True, 49, 25.2, 1.71, 0.482)
           5 +(4, 8, True, 137, 99.9, 3.63, 0.404)
           6 +(5, 8, True, 87, 62.1, 2.05, 0.194)
           7 +(6, 8, True, 647, 381.5, 11.97, 1.026)
           8 +(7, 8, True, 96, 77.4, 2.22, 0.262)
           9 +(8, 8, True, 106, 96.0, 22.6, 17.913)
          10 +(9, 8, True, 87, 72.7, 16.82, 12.899)
          11 +(10, 8, True, 73, 43.9, 3.42, 0.671)
          12 +(11, 8, True, 102, 76.5, 4.79, 0.818)
          13 +(12, 8, True, 105, 68.7, 4.31, 0.557)
          14 +(13, 8, True, 283, 161.0, 6.27, 0.526)
          15 +(14, 8, True, 48, 21.3, 1.71, 0.394)
          16 +(15, 8, True, 143, 88.3, 3.03, 0.412)
          17 +(16, 8, True, 51, 35.2, 0.92, 0.143)
          18 +(17, 8, True, 54, 32.5, 1.18, 0.176)
          19 +(18, 8, True, 105, 65.6, 2.61, 0.33)
          20 +(19, 8, True, 578, 290.3, 7.15, 0.285)
          21 +(20, 8, True, 65, 33.0, 1.91, 0.312)
          22 +(21, 8, True, 105, 92.8, 2.19, 0.396)
          23 +(22, 8, True, 63, 36.3, 1.26, 0.146)
          24 +(23, 8, True, 68, 55.2, 1.46, 0.277)
          25 +(24, 8, True, 66, 65.6, 1.0, 0.17)
          26 +(25, 8, True, 55, 58.4, 0.86, 0.124)
          27 +(26, 8, True, 50, 64.7, 1.08, 0.253)
          28 +(27, 8, True, 48, 112.4, 3.08, 2.08)
          29 +(28, 8, True, 94, 162.3, 3.87, 1.908)
          30 +(29, 8, True, 46, 100.1, 0.99, 0.209)
          31 +(30, 8, True, 50, 110.8, 0.94, 0.146)
          32 +(31, 8, True, 68, 136.2, 1.13, 0.12)
          33 +success 32 / 32 mean steps 118.15625
diff --git a/res_v1.txt b/res_v1.txt
new file mode 100644
index 0000000..f411157
--- /dev/null
+++ b/res_v1.txt
@@ -0,0 +1,161 @@
           1 +(200, 0, True, 13, 20.0, 0.08, 0.05)
           2 +(201, 0, True, 11, 19.1, 0.15, 0.08)
           3 +(202, 0, True, 11, 25.7, 0.07, 0.028)
           4 +(203, 0, True, 12, 20.2, 0.15, 0.088)
           5 +(204, 2, True, 39, 62.9, 0.39, 0.076)
           6 +(205, 1, True, 28, 35.0, 0.55, 0.238)
           7 +(206, 1, True, 18, 20.0, 0.42, 0.264)
           8 +(207, 0, True, 13, 17.1, 0.16, 0.083)
           9 +(208, 2, True, 18, 26.8, 0.29, 0.118)
          10 +(209, 2, True, 41, 56.1, 0.62, 0.125)
          11 +(210, 0, True, 14, 18.9, 0.32, 0.249)
          12 +(211, 0, True, 11, 10.4, 0.3, 0.178)
          13 +(212, 0, True, 12, 11.9, 0.11, 0.088)
          14 +(213, 0, True, 13, 16.2, 0.14, 0.05)
          15 +(214, 0, True, 13, 18.6, 0.14, 0.094)
          16 +(215, 2, True, 29, 36.4, 0.39, 0.112)
          17 +(216, 2, True, 22, 19.8, 0.22, 0.033)
          18 +(217, 2, True, 35, 40.1, 0.46, 0.108)
          19 +(218, 1, True, 26, 28.1, 0.31, 0.084)
          20 +(219, 0, True, 25, 26.7, 0.31, 0.247)
          21 +(220, 2, True, 34, 38.0, 0.62, 0.186)
          22 +(221, 1, True, 19, 9.9, 0.24, 0.074)
          23 +(222, 1, True, 20, 17.5, 0.15, 0.047)
          24 +(223, 1, True, 24, 26.2, 0.36, 0.085)
          25 +(224, 2, True, 31, 34.5, 0.49, 0.083)
          26 +(225, 2, True, 32, 39.2, 0.5, 0.101)
          27 +(226, 2, True, 38, 48.7, 0.44, 0.096)
          28 +(227, 1, True, 18, 17.2, 0.26, 0.082)
          29 +(228, 1, True, 16, 17.4, 0.13, 0.032)
          30 +(229, 1, True, 19, 15.4, 0.18, 0.045)
          31 +(230, 1, True, 20, 20.1, 0.23, 0.115)
          32 +(231, 0, True, 13, 20.3, 0.22, 0.166)
          33 +(232, 1, True, 23, 28.6, 0.46, 0.163)
          34 +(233, 0, True, 18, 20.4, 0.44, 0.228)
          35 +(234, 1, True, 26, 28.7, 0.49, 0.145)
          36 +(235, 2, True, 19, 19.4, 0.27, 0.115)
          37 +(236, 1, True, 23, 21.8, 0.43, 0.15)
          38 +(237, 2, True, 36, 29.6, 0.92, 0.454)
          39 +(238, 1, True, 13, 12.1, 0.37, 0.175)
          40 +(239, 2, True, 26, 21.9, 0.27, 0.104)
          41 +(240, 2, True, 28, 28.7, 0.35, 0.085)
          42 +(241, 1, True, 32, 32.4, 0.76, 0.289)
          43 +(242, 2, True, 22, 10.8, 0.25, 0.061)
          44 +(243, 2, True, 31, 31.7, 0.84, 0.42)
          45 +(244, 2, True, 27, 21.1, 0.37, 0.13)
          46 +(245, 2, True, 39, 41.7, 0.58, 0.121)
          47 +(246, 2, True, 23, 27.9, 0.49, 0.197)
          48 +(247, 0, True, 11, 7.7, 0.18, 0.097)
          49 +(248, 1, True, 23, 22.0, 0.44, 0.273)
          50 +(249, 2, True, 30, 35.2, 0.39, 0.083)
          51 +(250, 1, True, 26, 40.7, 0.34, 0.105)
          52 +(251, 0, True, 16, 18.3, 0.14, 0.105)
          53 +(252, 2, True, 20, 23.0, 0.26, 0.066)
          54 +(253, 1, True, 25, 28.8, 0.27, 0.062)
          55 +(254, 0, True, 16, 10.7, 0.17, 0.059)
          56 +(255, 0, True, 15, 11.0, 0.1, 0.037)
          57 +(256, 1, True, 29, 31.8, 1.07, 0.734)
          58 +(257, 2, True, 23, 30.5, 0.52, 0.258)
          59 +(258, 1, True, 25, 29.7, 0.78, 0.333)
          60 +(259, 0, True, 14, 12.7, 0.56, 0.345)
          61 +(260, 2, True, 37, 40.8, 0.88, 0.15)
          62 +(261, 1, True, 25, 19.9, 0.71, 0.187)
          63 +(262, 2, True, 41, 37.5, 0.82, 0.207)
          64 +(263, 2, True, 37, 40.0, 0.57, 0.266)
          65 +(264, 0, True, 16, 19.8, 0.45, 0.29)
          66 +(265, 2, True, 26, 32.7, 0.46, 0.098)
          67 +(266, 1, True, 15, 10.4, 0.19, 0.069)
          68 +(267, 1, True, 26, 28.4, 0.56, 0.2)
          69 +(268, 2, True, 39, 51.0, 0.38, 0.068)
          70 +(269, 2, True, 27, 28.0, 0.32, 0.076)
          71 +(270, 1, True, 25, 35.4, 0.4, 0.126)
          72 +(271, 2, True, 43, 59.7, 0.66, 0.158)
          73 +(272, 0, True, 17, 16.8, 0.16, 0.047)
          74 +(273, 0, True, 13, 19.5, 0.14, 0.099)
          75 +(274, 1, True, 28, 36.5, 0.25, 0.073)
          76 +(275, 0, True, 15, 24.2, 0.16, 0.113)
          77 +(276, 1, True, 26, 36.0, 0.62, 0.364)
          78 +(277, 0, True, 17, 23.3, 0.2, 0.114)
          79 +(278, 1, True, 23, 34.4, 0.34, 0.145)
          80 +(279, 1, True, 13, 14.8, 0.17, 0.118)
          81 +(280, 1, True, 25, 34.6, 0.65, 0.272)
          82 +(281, 1, True, 22, 33.9, 0.71, 0.269)
          83 +(282, 2, True, 30, 42.9, 0.81, 0.318)
          84 +(283, 0, True, 13, 12.9, 0.26, 0.148)
          85 +(284, 0, True, 12, 15.3, 0.11, 0.074)
          86 +(285, 2, True, 39, 58.0, 1.21, 0.29)
          87 +(286, 0, True, 14, 20.4, 0.17, 0.111)
          88 +(287, 2, True, 30, 31.2, 0.97, 0.355)
          89 +(288, 0, True, 14, 16.5, 0.16, 0.098)
          90 +(289, 1, True, 21, 31.7, 2.8, 2.316)
          91 +(290, 0, True, 17, 22.3, 0.55, 0.502)
          92 +(291, 0, True, 16, 22.3, 0.22, 0.159)
          93 +(292, 2, True, 35, 50.4, 0.45, 0.089)
          94 +(293, 0, True, 17, 29.3, 0.28, 0.126)
          95 +(294, 0, True, 12, 19.0, 0.46, 0.398)
          96 +(295, 0, True, 11, 21.3, 0.18, 0.143)
          97 +(296, 0, True, 12, 21.8, 0.17, 0.078)
          98 +(297, 0, True, 13, 19.9, 0.34, 0.292)
          99 +(298, 1, True, 26, 36.7, 0.33, 0.079)
         100 +(299, 2, True, 23, 29.6, 0.29, 0.061)
         101 +(300, 0, True, 13, 19.1, 0.14, 0.062)
         102 +(301, 0, True, 21, 28.4, 0.37, 0.197)
         103 +(302, 2, True, 39, 45.2, 0.62, 0.18)
         104 +(303, 1, True, 9, 10.2, 0.08, 0.035)
         105 +(304, 2, True, 28, 35.3, 0.48, 0.142)
         106 +(305, 0, True, 13, 18.1, 0.2, 0.135)
         107 +(306, 2, True, 30, 46.1, 1.75, 1.329)
         108 +(307, 2, True, 33, 62.3, 0.57, 0.131)
         109 +(308, 1, True, 16, 15.4, 0.18, 0.107)
         110 +(309, 1, True, 13, 18.9, 0.23, 0.121)
         111 +(310, 0, True, 12, 18.7, 0.15, 0.08)
         112 +(311, 1, True, 20, 32.6, 0.44, 0.142)
         113 +(312, 0, True, 13, 25.2, 0.22, 0.115)
         114 +(313, 0, True, 13, 19.4, 0.15, 0.095)
         115 +(314, 1, True, 29, 42.6, 0.4, 0.112)
         116 +(315, 1, True, 23, 32.8, 0.39, 0.135)
         117 +(316, 0, True, 15, 19.9, 0.17, 0.068)
         118 +(317, 0, True, 18, 35.5, 0.33, 0.279)
         119 +(318, 0, True, 11, 16.3, 0.14, 0.071)
         120 +(319, 2, True, 27, 43.7, 0.45, 0.128)
         121 +(320, 0, True, 11, 16.6, 0.12, 0.051)
         122 +(321, 1, True, 24, 31.4, 0.51, 0.127)
         123 +(322, 0, True, 15, 22.5, 0.26, 0.106)
         124 +(323, 2, True, 30, 46.1, 0.67, 0.193)
         125 +(324, 1, True, 31, 51.4, 0.5, 0.143)
         126 +(325, 0, True, 13, 17.4, 0.25, 0.187)
         127 +(326, 0, True, 13, 22.3, 0.3, 0.166)
         128 +(327, 1, True, 19, 24.1, 0.61, 0.266)
         129 +(328, 0, True, 15, 22.2, 0.14, 0.047)
         130 +(329, 2, True, 34, 58.3, 0.56, 0.151)
         131 +(330, 1, True, 25, 41.6, 0.56, 0.184)
         132 +(331, 0, True, 10, 12.0, 0.08, 0.042)
         133 +(332, 1, True, 17, 24.3, 0.23, 0.09)
         134 +(333, 0, True, 12, 21.9, 0.16, 0.105)
         135 +(334, 1, True, 24, 41.3, 0.31, 0.101)
         136 +(335, 0, True, 15, 22.6, 0.14, 0.099)
         137 +(336, 1, True, 26, 36.1, 0.43, 0.163)
         138 +(337, 0, True, 10, 11.6, 0.09, 0.055)
         139 +(338, 1, True, 20, 31.9, 0.38, 0.233)
         140 +(339, 0, True, 17, 18.8, 0.14, 0.059)
         141 +(340, 0, True, 15, 25.9, 0.22, 0.115)
         142 +(341, 2, True, 24, 34.1, 0.62, 0.171)
         143 +(342, 2, True, 38, 64.0, 0.62, 0.108)
         144 +(343, 0, True, 14, 22.2, 0.2, 0.145)
         145 +(344, 0, True, 15, 22.1, 0.12, 0.077)
         146 +(345, 0, True, 16, 20.1, 0.22, 0.08)
         147 +(346, 1, True, 27, 48.0, 0.53, 0.21)
         148 +(347, 2, True, 22, 30.4, 0.8, 0.391)
         149 +(348, 0, True, 10, 6.2, 0.12, 0.087)
         150 +(349, 2, True, 31, 40.2, 0.49, 0.122)
         151 +(350, 1, True, 26, 40.8, 0.37, 0.168)
         152 +(351, 1, True, 34, 38.4, 0.46, 0.1)
         153 +(352, 0, True, 17, 12.0, 0.13, 0.054)
         154 +(353, 0, True, 16, 8.8, 0.26, 0.1)
         155 +(354, 2, True, 34, 29.3, 0.67, 0.145)
         156 +(355, 1, True, 19, 18.4, 0.29, 0.092)
         157 +(356, 0, True, 13, 14.5, 0.19, 0.109)
         158 +(357, 1, True, 25, 12.2, 0.31, 0.085)
         159 +(358, 2, True, 33, 12.8, 0.29, 0.039)
         160 +(359, 1, True, 24, 7.8, 0.26, 0.056)
         161 +success 160 / 160 mean steps 21.8
diff --git a/res_v10.txt b/res_v10.txt
new file mode 100644
index 0000000..0861157
--- /dev/null
+++ b/res_v10.txt
@@ -0,0 +1,17 @@
           1 +(100, 10, True, 119, 80.7, 11.47, 8.381)
           2 +(101, 10, True, 110, 42.8, 3.02, 0.467)
           3 +(102, 10, True, 75, 32.2, 2.16, 0.267)
           4 +(103, 10, True, 99, 54.0, 5.83, 2.553)
           5 +(104, 10, True, 172, 93.1, 5.81, 0.657)
           6 +(105, 10, True, 97, 52.1, 3.27, 0.328)
           7 +(106, 10, True, 76, 34.3, 6.41, 3.146)
           8 +(107, 10, True, 91, 45.3, 3.47, 0.55)
           9 +(108, 10, True, 98, 62.1, 2.75, 0.436)
          10 +(109, 10, True, 79, 53.2, 2.87, 0.39)
          11 +(110, 10, True, 128, 71.0, 22.8, 6.487)
          12 +(111, 10, True, 52, 28.7, 1.29, 0.156)
          13 +(112, 10, False, 1000, 59.7, 9.54, 0.754)
          14 +(113, 10, True, 57, 27.9, 1.49, 0.244)
          15 +(114, 10, True, 87, 27.5, 2.15, 0.411)
          16 +(115, 10, True, 141, 34.3, 14.35, 4.438)
          17 +success 15 / 16 mean steps 155.0625
diff --git a/res_v8.txt b/res_v8.txt
new file mode 100644
index 0000000..ad119d4
--- /dev/null
+++ b/res_v8.txt
@@ -0,0 +1,33 @@
           1 +(100, 8, True, 73, 40.8, 4.48, 0.967)
           2 +(101, 8, True, 408, 134.4, 9.43, 0.844)
           3 +(102, 8, True, 70, 56.9, 15.37, 12.373)
           4 +(103, 8, True, 81, 80.0, 23.88, 13.196)
           5 +(104, 8, False, 1000, 255.9, 21.98, 1.069)
           6 +(105, 8, True, 96, 42.3, 4.47, 0.792)
           7 +(106, 8, True, 77, 42.5, 8.1, 3.222)
           8 +(107, 8, True, 73, 23.3, 4.0, 0.846)
           9 +(108, 8, True, 95, 53.1, 3.43, 0.736)
          10 +(109, 8, True, 78, 43.2, 2.94, 0.551)
          11 +(110, 8, True, 99, 64.2, 2.91, 0.521)
          12 +(111, 8, True, 52, 16.7, 1.68, 0.401)
          13 +(112, 8, True, 90, 44.9, 2.76, 0.293)
          14 +(113, 8, True, 57, 27.4, 0.93, 0.158)
          15 +(114, 8, True, 57, 29.8, 1.03, 0.154)
          16 +(115, 8, True, 125, 106.4, 31.92, 10.96)
          17 +(116, 8, True, 45, 33.5, 7.99, 6.846)
          18 +(117, 8, True, 83, 42.4, 4.04, 0.906)
          19 +(118, 8, True, 108, 49.7, 4.49, 0.704)
          20 +(119, 8, True, 176, 103.0, 15.55, 2.986)
          21 +(120, 8, True, 727, 141.1, 14.0, 0.648)
          22 +(121, 8, True, 59, 25.5, 1.24, 0.258)
          23 +(122, 8, True, 85, 42.8, 9.22, 3.017)
          24 +(123, 8, True, 80, 30.2, 3.58, 0.609)
          25 +(124, 8, True, 61, 22.2, 5.77, 1.726)
          26 +(125, 8, True, 82, 35.4, 3.28, 0.579)
          27 +(126, 8, True, 73, 48.2, 5.81, 3.476)
          28 +(127, 8, True, 55, 34.5, 1.88, 0.33)
          29 +(128, 8, True, 65, 37.5, 2.27, 0.334)
          30 +(129, 8, True, 68, 33.0, 2.2, 0.273)
          31 +(130, 8, True, 131, 36.2, 3.1, 0.479)
          32 +(131, 8, True, 355, 36.8, 5.8, 0.29)
          33 +success 31 / 32 mean steps 149.5
```

</details>

