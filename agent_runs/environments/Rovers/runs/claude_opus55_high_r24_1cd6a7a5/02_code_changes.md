# Rovers · claude-opus-5-5 · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `dc861b5` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `6fd490b` | Initial lattice+subset-DP planner approach | approach.py, probe.py, probe_motion_1.py, probe_motion_2.py, probe_motion_3.py, probe_motion_4.py, probe_motion_5.py, probe_motion_6.py, probe_motion_lib.py, probe_ops_1.py, probe… | [E0255](01_timeline.md#E0255) |
| [C003](#C003) · `8832f94` | Conservative image radius 1.85; all 8 seeds solved | approach.py, dbg.py, probe_img.py, probe_img2.py, probe_vis_0.py | [E0299](01_timeline.md#E0299) |
| [C004](#C004) · `4351d31` | Heading control (face away from target), exact camera visibility model, send LOS model | approach.py, dbg.py, eval_many.py, probe_s21.py, probe_send_0.py, probe_send_1.py, probe_send_10.py, probe_send_11.py, probe_send_12.py, probe_send_13.py, probe_send_14.py, probe_… | [E0803](01_timeline.md#E0803) |
| [C005](#C005) · `f480a81` | Return to home heading (at_home needs theta), send cone fallback | approach.py, dbg2.py, probe_home.py | [E0827](01_timeline.md#E0827) |
| [C006](#C006) · `63b13d1` | Send-cone heading chosen to minimise total rotation | approach.py | [E0839](01_timeline.md#E0839) |
| [C007](#C007) · `6945310` | Send whenever possible; keep home heading if future LOS send is predicted | approach.py | [E0850](01_timeline.md#E0850) |
| [C008](#C008) · `340d148` | approach2: time-expanded BFS planner (wip) | approach2.py, eval_many.py | [E0865](01_timeline.md#E0865) |
| [C009](#C009) · `4524e2b` | approach2: send mask respects LOS/heading | approach2.py, dbg2.py | [E0884](01_timeline.md#E0884) |
| [C010](#C010) · `617ca9f` | approach2: time-dependent send mask using other rover trajectory | approach2.py, approach2_old.py, cmp.py, eval_many.py, res_approach2_a.json, res_approach2_old_a.json | [E0907](01_timeline.md#E0907) |
| [C011](#C011) · `c8236a8` | approach2: keep refined plan only if not longer | approach2.py, res_approach2_b.json | [E0927](01_timeline.md#E0927) |
| [C012](#C012) · `3e4a72a` | approach2: replan immediately when failed op changed state unexpectedly | approach2.py, res_approach2_d.json | [E0941](01_timeline.md#E0941) |
| [C013](#C013) · `86fe1c7` | Adopt time-expanded BFS planner (approach2) as approach.py; mean 21.52 on seeds 0-47 | approach.py, approach_v1.py, res_approach2_e.json | [E0952](01_timeline.md#E0952) |
| [C014](#C014) · `97c75ea` | Refinement: penalize original plan when its sends lack LOS | approach.py, eval_many.py, res_approach_oc1.json, res_approach_oc2.json, res_approach_oc3.json, res_approach_oc4.json, res_approach_w.json | [E0991](01_timeline.md#E0991) |
| [C015](#C015) · `5b692fc` | SEND_PEN=0 (penalty hurt) | approach.py, res_approach_f.json | [E0995](01_timeline.md#E0995) |
| [C016](#C016) · `ece4612` | Pre-rotate to send cone before planned sample when no LOS predicted | approach.py | [E1002](01_timeline.md#E1002) |
| [C017](#C017) · `5776b80` | Allow finishing at cells within HOME_TOL of home | approach.py, res_approach_g.json, res_approach_wg.json | [E1023](01_timeline.md#E1023) |
| [C018](#C018) · `c6089ab` | HOME_TOL=0 (near-home finish hurt) | approach.py, res_approach_h.json | [E1030](01_timeline.md#E1030) |
| [C019](#C019) · `6fb1c9f` | Global time cap on replanning | approach.py, res_approach_i.json | [E1039](01_timeline.md#E1039) |
| [C020](#C020) · `cf0ca46` | Tighter reset time budgets | approach.py, res_approach_j.json | [E1042](01_timeline.md#E1042) |
| [C021](#C021) · `4b16eec` | test script update | test_approach.py | [E1055](01_timeline.md#E1055) |
| [C022](#C022) · `a010326` | eval results | res_approach_oc4b.json | [E1060](01_timeline.md#E1060) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `dc861b52bad675da4bbca31bbccc5db79c5bce08`; parents: none (initial snapshot). Recorded author date: 2026-10-01T10:20:51+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_dc861b5.diff)

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
index 0000000..c9e914b
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "4195a5ccfe437a45c58686a5300b5750", "observation_space": {"type": "ObjectCentric", "types": [{"name": "lander", "parent": null, "features": ["x", "y", "z"]}, {"name": "objective", "parent": null, "features": ["x", "y", "z", "have_image_rover0", "have_image_rover1", "received_image"]}, {"name": "obstacle", "parent": null, "features": ["x", "y", "z", "half_x", "half_y", "half_z"]}, {"name": "rover", "parent": null, "features": ["x", "y", "theta", "store_full", "calibrated", "at_home"]}, {"name": "sample", "parent": null, "features": ["x", "y", "z", "is_soil", "analyzed_rover0", "analyzed_rover1", "received_analysis"]}]}, "action_space": {"type": "Box", "shape": [8], "low": [-0.20000000298023224, -0.20000000298023224, -0.4000000059604645, -1.0, -0.20000000298023224, -0.20000000298023224, -0.4000000059604645, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.4000000059604645, 1.0, 0.20000000298023224, 0.20000000298023224, 0.4000000059604645, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Initial lattice+subset-DP planner approach

Commit `6fd490bb568b26e35f424be4251c0dd08ed71e2b`; parents: dc861b52bad675da4bbca31bbccc5db79c5bce08. Recorded author date: 2026-10-01T10:33:36+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0255](01_timeline.md#E0255): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_6fd490b_approach.py) · [Exact all-file diff](evidence/diffs/C002_6fd490b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..4db1072
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,379 @@
           1 +import itertools
           2 +import numpy as np
           3 +
           4 +H = 0.1            # lattice spacing (a step can move up to 2 cells per axis)
           5 +R_STEP = 2         # cells per step
           6 +IMG_R = 1.96       # imaging range (true ~2.0)
           7 +SAMP_R = 0.235     # sampling range (true 0.25)
           8 +SEND_R = 3.85      # send range (true ~4.0)
           9 +BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
          10 +        "send": 0.5, "drop": 5 / 6}
          11 +INF = 1e9
          12 +
          13 +
          14 +def _type(space, name):
          15 +    for t in space.types:
          16 +        if t.name == name:
          17 +            return t
          18 +    return None
          19 +
          20 +
          21 +class Scene:
          22 +    def __init__(self, state, space):
          23 +        self.T = {n: _type(space, n) for n in ["rover", "lander", "objective", "sample", "obstacle"]}
          24 +        g = state.get
          25 +        self.rovers = sorted(state.get_objects(self.T["rover"]), key=lambda o: o.name)
          26 +        self.lander = state.get_objects(self.T["lander"])[0]
          27 +        self.objectives = sorted(state.get_objects(self.T["objective"]), key=lambda o: o.name)
          28 +        self.samples = sorted(state.get_objects(self.T["sample"]), key=lambda o: o.name)
          29 +        self.obstacles = state.get_objects(self.T["obstacle"])
          30 +        self.lpos = np.array([g(self.lander, "x"), g(self.lander, "y")])
          31 +        self.obs_boxes = []
          32 +        for o in self.obstacles:
          33 +            self.obs_boxes.append((g(o, "x"), g(o, "y"), g(o, "half_x"), g(o, "half_y"), g(o, "half_z")))
          34 +        self.opos = [np.array([g(o, "x"), g(o, "y")]) for o in self.objectives]
          35 +        self.spos = [np.array([g(o, "x"), g(o, "y")]) for o in self.samples]
          36 +        self.ssoil = [g(o, "is_soil") > 0.5 for o in self.samples]
          37 +
          38 +
          39 +class RoverPlanner:
          40 +    """Lattice anchored at the rover's home; subset DP over task regions."""
          41 +
          42 +    def __init__(self, scene, idx, home):
          43 +        self.scene = scene
          44 +        self.idx = idx
          45 +        self.home = np.array(home, dtype=float)
          46 +        side = 1.0 if home[0] > 0 else -1.0
          47 +        self.side = side
          48 +        xs = []
          49 +        x = self.home[0]
          50 +        while x - H >= -2.27:
          51 +            x -= H
          52 +        while x <= 2.27:
          53 +            xs.append(x)
          54 +            x += H
          55 +        ys = []
          56 +        y = self.home[1]
          57 +        while y - H >= -2.27:
          58 +            y -= H
          59 +        while y <= 2.27:
          60 +            ys.append(y)
          61 +            y += H
          62 +        self.xs = np.array(xs)
          63 +        self.ys = np.array(ys)
          64 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
          65 +        self.X, self.Y = X, Y
          66 +        free = (np.abs(X) <= 2.265) & (np.abs(Y) <= 2.265) & (X * side >= 0.235)
          67 +        for (ox, oy, hx, hy, hz) in scene.obs_boxes:
          68 +            margin = 0.21 if max(hx, hy) >= 0.15 else 0.25
          69 +            dx = np.maximum(np.abs(X - ox) - hx, 0.0)
          70 +            dy = np.maximum(np.abs(Y - oy) - hy, 0.0)
          71 +            free &= (dx * dx + dy * dy) >= margin * margin
          72 +        lx, ly = scene.lpos
          73 +        free &= ~((X < lx + 0.71) & (Y < ly + 0.54))
          74 +        self.hi = int(np.argmin(np.abs(self.xs - self.home[0])))
          75 +        self.hj = int(np.argmin(np.abs(self.ys - self.home[1])))
          76 +        free[self.hi, self.hj] = True
          77 +        self.free = free
          78 +        self.shape = free.shape
          79 +        self.offsets = [(a, b) for a in range(-R_STEP, R_STEP + 1) for b in range(-R_STEP, R_STEP + 1)
          80 +                        if (a, b) != (0, 0)]
          81 +
          82 +    def pos(self, c):
          83 +        return np.array([self.xs[c[0]], self.ys[c[1]]])
          84 +
          85 +    def cell(self, p):
          86 +        i = int(np.argmin(np.abs(self.xs - p[0])))
          87 +        j = int(np.argmin(np.abs(self.ys - p[1])))
          88 +        return (i, j)
          89 +
          90 +    def region_mask(self, task):
          91 +        kind, k = task
          92 +        sc = self.scene
          93 +        if kind == "obj":
          94 +            o = sc.opos[k]
          95 +            m = (self.X - o[0]) ** 2 + (self.Y - o[1]) ** 2 <= IMG_R ** 2
          96 +        else:  # 'stone' or 'soil'
          97 +            want_soil = kind == "soil"
          98 +            m = np.zeros(self.shape, bool)
          99 +            for s, soil in zip(sc.spos, sc.ssoil):
         100 +                if soil == want_soil:
         101 +                    m |= (self.X - s[0]) ** 2 + (self.Y - s[1]) ** 2 <= SAMP_R ** 2
         102 +        return m & self.free
         103 +
         104 +    def propagate(self, F):
         105 +        G = F.copy()
         106 +        R = R_STEP
         107 +        W, Hh = self.shape
         108 +        free = self.free
         109 +        while True:
         110 +            P = np.full((W + 2 * R, Hh + 2 * R), INF)
         111 +            P[R:R + W, R:R + Hh] = G
         112 +            best = G.copy()
         113 +            for a, b in self.offsets:
         114 +                np.minimum(best, P[R + a:R + a + W, R + b:R + b + Hh] + 1.0, out=best)
         115 +            best[~free] = INF
         116 +            if np.array_equal(best, G):
         117 +                return G
         118 +            G = best
         119 +
         120 +    def dp(self, tasks, start=None):
         121 +        """Returns dict subset(bitmask)->cost of tour start->tasks->home, and stores fields."""
         122 +        if start is None:
         123 +            start = (self.hi, self.hj)
         124 +        n = len(tasks)
         125 +        masks = [self.region_mask(t) for t in tasks]
         126 +        F0 = np.full(self.shape, INF)
         127 +        F0[start] = 0.0
         128 +        Fs = {0: F0}
         129 +        Gs = {}
         130 +        order = sorted(range(1 << n), key=lambda s: bin(s).count("1"))
         131 +        for s in order:
         132 +            F = Fs.get(s)
         133 +            if F is None:
         134 +                continue
         135 +            G = self.propagate(F)
         136 +            Gs[s] = G
         137 +            for r in range(n):
         138 +                if s & (1 << r):
         139 +                    continue
         140 +                if not masks[r].any():
         141 +                    continue
         142 +                s2 = s | (1 << r)
         143 +                cand = np.where(masks[r], G, INF)
         144 +                if s2 in Fs:
         145 +                    np.minimum(Fs[s2], cand, out=Fs[s2])
         146 +                else:
         147 +                    Fs[s2] = cand
         148 +        self._tasks = tasks
         149 +        self._masks = masks
         150 +        self._Fs = Fs
         151 +        self._Gs = Gs
         152 +        self._start = start
         153 +        costs = {}
         154 +        for s, G in Gs.items():
         155 +            costs[s] = G[self.hi, self.hj]
         156 +        return costs
         157 +
         158 +    def extract(self, s):
         159 +        """Backtrack path for subset s (from last dp). Returns list of cells and visits dict idx->[tasks]."""
         160 +        Gs, Fs, masks = self._Gs, self._Fs, self._masks
         161 +        c = (self.hi, self.hj)
         162 +        v = Gs[s][c]
         163 +        rev = [c]
         164 +        rev_visits = []  # (position in rev, task index)
         165 +        W, Hh = self.shape
         166 +        guard = 0
         167 +        while True:
         168 +            guard += 1
         169 +            if guard > 10000:
         170 +                break
         171 +            if s == 0 and c == self._start:
         172 +                break
         173 +            # try region entry at c
         174 +            moved = False
         175 +            if s != 0 and Fs[s][c] <= v + 1e-9:
         176 +                for r in range(len(masks)):
         177 +                    if s & (1 << r) and masks[r][c]:
         178 +                        s2 = s & ~(1 << r)
         179 +                        if s2 in Gs and Gs[s2][c] <= v + 1e-9:
         180 +                            rev_visits.append((len(rev) - 1, r))
         181 +                            s = s2
         182 +                            moved = True
         183 +                            break
         184 +            if moved:
         185 +                continue
         186 +            for a, b in self.offsets:
         187 +                n = (c[0] + a, c[1] + b)
         188 +                if 0 <= n[0] < W and 0 <= n[1] < Hh and Gs[s][n] <= v - 1 + 1e-9:
         189 +                    c = n
         190 +                    v = Gs[s][n]
         191 +                    rev.append(c)
         192 +                    moved = True
         193 +                    break
         194 +            if not moved:
         195 +                break
         196 +        L = len(rev)
         197 +        path = rev[::-1]
         198 +        visits = {}
         199 +        for (ri, r) in rev_visits:
         200 +            visits.setdefault(L - 1 - ri, []).append(self._tasks[r])
         201 +        return path, visits
         202 +
         203 +
         204 +class GeneratedApproach:
         205 +    def __init__(self, action_space, observation_space, primitives):
         206 +        self.action_space = action_space
         207 +        self.space = observation_space
         208 +
         209 +    # ------------------------------------------------------------------
         210 +    def reset(self, state, info):
         211 +        self.sc = Scene(state, self.space)
         212 +        sc = self.sc
         213 +        g = state.get
         214 +        self.homes = [np.array([g(r, "x"), g(r, "y")]) for r in sc.rovers]
         215 +        self.planners = [RoverPlanner(sc, i, self.homes[i]) for i in range(2)]
         216 +        nobj = len(sc.objectives)
         217 +        tasks = [("obj", k) for k in range(nobj)] + [("stone", 0), ("soil", 0)]
         218 +        self.tasks = tasks
         219 +        costs = []
         220 +        for i in range(2):
         221 +            costs.append(self.planners[i].dp(tasks))
         222 +        # store fields per rover (dp overwrote): re-run later for chosen subset
         223 +        n = len(tasks)
         224 +        full = (1 << n) - 1
         225 +        best = None
         226 +        for s0 in range(1 << n):
         227 +            s1 = full & ~s0
         228 +            c0 = costs[0].get(s0, INF)
         229 +            c1 = costs[1].get(s1, INF)
         230 +            if c0 >= INF or c1 >= INF:
         231 +                continue
         232 +            ops0 = self._ops(tasks, s0)
         233 +            ops1 = self._ops(tasks, s1)
         234 +            k0 = max(c0, ops0) + 0.5 * self._extra(tasks, s0)
         235 +            k1 = max(c1, ops1) + 0.5 * self._extra(tasks, s1)
         236 +            key = (max(k0, k1), k0 + k1)
         237 +            if best is None or key < best[0]:
         238 +                best = (key, s0, s1)
         239 +        self.assign = [best[1], best[2]] if best else [full, 0]
         240 +        self.plans = []
         241 +        for i in range(2):
         242 +            p = self.planners[i]
         243 +            p.dp(tasks)
         244 +            path, visits = p.extract(self.assign[i])
         245 +            self.plans.append({"path": path, "visits": visits, "k": 0, "wait": 0, "stuck": 0})
         246 +        self.my_tasks = [[tasks[r] for r in range(n) if self.assign[i] & (1 << r)] for i in range(2)]
         247 +        self.last_target = [None, None]
         248 +
         249 +    def _ops(self, tasks, s):
         250 +        c = 0
         251 +        for r, t in enumerate(tasks):
         252 +            if s & (1 << r):
         253 +                c += 2 if t[0] == "obj" else 2
         254 +        return c + 1
         255 +
         256 +    def _extra(self, tasks, s):
         257 +        return 0
         258 +
         259 +    # ------------------------------------------------------------------
         260 +    def _task_done(self, state, t):
         261 +        sc = self.sc
         262 +        g = state.get
         263 +        if t[0] == "obj":
         264 +            o = sc.objectives[t[1]]
         265 +            return g(o, "have_image_rover0") > 0.5 or g(o, "have_image_rover1") > 0.5 or g(o, "received_image") > 0.5
         266 +        want_soil = t[0] == "soil"
         267 +        for s, soil in zip(sc.samples, sc.ssoil):
         268 +            if soil == want_soil and (g(s, "analyzed_rover0") > 0.5 or g(s, "analyzed_rover1") > 0.5
         269 +                                      or g(s, "received_analysis") > 0.5):
         270 +                return True
         271 +        return False
         272 +
         273 +    def _choose_op(self, state, i, p, at_visit_tasks):
         274 +        sc = self.sc
         275 +        g = state.get
         276 +        rv = sc.rovers[i]
         277 +        me = "rover%d" % i
         278 +        other = "rover%d" % (1 - i)
         279 +        store_full = g(rv, "store_full") > 0.5
         280 +        calibrated = g(rv, "calibrated") > 0.5
         281 +        # sample
         282 +        if not store_full:
         283 +            for s, soil, sp in zip(sc.samples, sc.ssoil, sc.spos):
         284 +                if np.linalg.norm(sp - p) <= SAMP_R:
         285 +                    t = ("soil", 0) if soil else ("stone", 0)
         286 +                    if not self._task_done(state, t):
         287 +                        return "sample"
         288 +        # imaging
         289 +        visible = [k for k in range(len(sc.objectives)) if np.linalg.norm(sc.opos[k] - p) <= IMG_R]
         290 +        need = [k for k in range(len(sc.objectives)) if not self._task_done(state, ("obj", k))]
         291 +        vis_need = [k for k in visible if k in need]
         292 +        if vis_need:
         293 +            if calibrated:
         294 +                cands = [k for k in visible if g(sc.objectives[k], "have_image_" + me) < 0.5]
         295 +                if cands:
         296 +                    return "image"
         297 +            else:
         298 +                return "calibrate"
         299 +        # calibrate early if I still have images to take and something is visible
         300 +        mine_left = [t for t in self.my_tasks[i] if t[0] == "obj" and not self._task_done(state, t)]
         301 +        if not calibrated and mine_left and any(
         302 +                np.linalg.norm(sc.opos[k] - p) <= IMG_R for k in range(len(sc.objectives))):
         303 +            return "calibrate"
         304 +        if store_full:
         305 +            # is my store's analysis already recorded? (store full => yes)
         306 +            return "drop"
         307 +        # send
         308 +        all_done = all(self._task_done(state, t) for t in self.my_tasks[i])
         309 +        holding = False
         310 +        for o in sc.objectives:
         311 +            if g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5:
         312 +                holding = True
         313 +        for s in sc.samples:
         314 +            if g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5:
         315 +                holding = True
         316 +        if holding and all_done and np.linalg.norm(p - sc.lpos) <= SEND_R:
         317 +            return "send"
         318 +        return "noop"
         319 +
         320 +    def _rover_action(self, state, i):
         321 +        sc = self.sc
         322 +        g = state.get
         323 +        rv = sc.rovers[i]
         324 +        cur = np.array([g(rv, "x"), g(rv, "y")])
         325 +        plan = self.plans[i]
         326 +        path = plan["path"]
         327 +        P = self.planners[i]
         328 +        k = plan["k"]
         329 +        # verify position
         330 +        exp = P.pos(path[k])
         331 +        if np.linalg.norm(exp - cur) > 0.02:
         332 +            # previous move blocked or drifted; find closest path index or stay
         333 +            plan["stuck"] += 1
         334 +            if plan["stuck"] > 3:
         335 +                self._replan(state, i, cur)
         336 +                plan = self.plans[i]
         337 +                path = plan["path"]
         338 +                k = plan["k"]
         339 +            else:
         340 +                # step back on k to retry previous move
         341 +                if k > 0 and np.linalg.norm(P.pos(path[k - 1]) - cur) < 0.02:
         342 +                    k = k - 1
         343 +                    plan["k"] = k
         344 +        # decide whether to stay at current index
         345 +        stay = False
         346 +        vt = plan["visits"].get(k, [])
         347 +        for t in vt:
         348 +            if not self._task_done(state, t) and plan["wait"] < 12:
         349 +                stay = True
         350 +        if k >= len(path) - 1:
         351 +            stay = True
         352 +        if stay:
         353 +            plan["wait"] += 1
         354 +            nxt = k
         355 +        else:
         356 +            plan["wait"] = 0
         357 +            nxt = k + 1
         358 +            # don't leave if next index arrival leaves region needed... (handled by visits)
         359 +        target = P.pos(path[nxt])
         360 +        d = target - cur
         361 +        d = np.clip(d, -0.2, 0.2)
         362 +        newp = cur + d
         363 +        op = self._choose_op(state, i, newp, vt)
         364 +        plan["k"] = nxt
         365 +        return np.array([d[0], d[1], 0.0, BAND[op]], dtype=np.float32)
         366 +
         367 +    def _replan(self, state, i, cur):
         368 +        P = self.planners[i]
         369 +        rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
         370 +        start = P.cell(cur)
         371 +        P.free[start] = True
         372 +        costs = P.dp(rem, start=start)
         373 +        path, visits = P.extract((1 << len(rem)) - 1)
         374 +        self.plans[i] = {"path": path, "visits": visits, "k": 0, "wait": 0, "stuck": 0}
         375 +
         376 +    def get_action(self, state):
         377 +        a0 = self._rover_action(state, 0)
         378 +        a1 = self._rover_action(state, 1)
         379 +        return np.concatenate([a0, a1]).astype(np.float32)
diff --git a/probe.py b/probe.py
new file mode 100644
index 0000000..fc443f5
--- /dev/null
+++ b/probe.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +env = make_env()
           3 +for seed in [0,1]:
           4 +    obs, info = env.reset(seed=seed)
           5 +    print("seed", seed, info)
           6 +    for t in obs.get_objects(None) if False else []: pass
           7 +    for name in obs.get_object_names():
           8 +        o = obs.get_object_from_name(name)
           9 +        tname = o.type.name if hasattr(o.type,'name') else o.type
          10 +        feats = env.observation_space.type_features[env.observation_space.get_type(tname)] if False else None
          11 +        print(name, tname, end=' ')
          12 +        for typ in ['rover','lander','objective','sample','obstacle']:
          13 +            pass
          14 +        print()
          15 +    for typ in env.observation_space.types:
          16 +        for o in obs.get_objects(typ):
          17 +            print(o.name, [round(float(obs.get(o,f)),3) for f in env.observation_space.type_features[typ]])
          18 +env.close()
diff --git a/probe_motion_1.py b/probe_motion_1.py
new file mode 100644
index 0000000..6a0dbda
--- /dev/null
+++ b/probe_motion_1.py
@@ -0,0 +1,7 @@
           1 +from probe_motion_lib import *
           2 +obs,info = env.reset(seed=0)
           3 +for n,v in obstacles(obs): print(n,v)
           4 +print('max_steps', getattr(env,'max_steps',None))
           5 +print(rov(obs,0))
           6 +for a in [(0.1,0,0),(0,0.1,0),(0.3,0,0),(0,0,0.3),(0.1,0,0),(0,0,1.0),(0.1,0.0,0)]:
           7 +    obs,r,te,tr,inf = step(0,*a); print(a, np.round(rov(obs,0),4), r, te, tr)
diff --git a/probe_motion_2.py b/probe_motion_2.py
new file mode 100644
index 0000000..13e5194
--- /dev/null
+++ b/probe_motion_2.py
@@ -0,0 +1,12 @@
           1 +from probe_motion_lib import *
           2 +# bounds with rover0 (step 0.2 then 0.01)
           3 +for d in [(1,0),(0,1),(0,-1)]:
           4 +    obs,_=env.reset(seed=0)
           5 +    drive_until_stop(0, .2*d[0], .2*d[1])
           6 +    p=drive_until_stop(0, .01*d[0], .01*d[1])
           7 +    print('rover0 dir',d,np.round(p,4))
           8 +for d in [(-1,0),(0,1),(0,-1)]:
           9 +    obs,_=env.reset(seed=0)
          10 +    p=drive_until_stop(1, .2*d[0], .2*d[1]); print(' coarse',np.round(p,4))
          11 +    p=drive_until_stop(1, .01*d[0], .01*d[1])
          12 +    print('rover1 dir',d,np.round(p,4))
diff --git a/probe_motion_3.py b/probe_motion_3.py
new file mode 100644
index 0000000..c5f08a3
--- /dev/null
+++ b/probe_motion_3.py
@@ -0,0 +1,15 @@
           1 +from probe_motion_lib import *
           2 +obs,_=env.reset(seed=0)
           3 +L=[o for o in obs.get_objects(T['lander'])][0]
           4 +print('lander feats', {f:round(float(obs.get(L,f)),3) for f in env.observation_space.type_features[T['lander']]})
           5 +# partial move test: rover1 toward lander with big step from near contact
           6 +obs,_=env.reset(seed=0)
           7 +goto(1,-1.15,-1.75,s=0.05); obs,*_=step(1,-0.2,0); print('big step near block ->',np.round(rov(obs,1)[:2],4))
           8 +# wall: rover0 at x=1, various y, drive -x
           9 +for seed in [0]:
          10 +  for y in np.arange(-2.25,2.26,0.25):
          11 +    obs,_=env.reset(seed=seed)
          12 +    p=goto(0,1.0,y)
          13 +    if abs(p[1]-y)>1e-3: print(y,'could not reach',np.round(p,3)); continue
          14 +    p=approach(0,-1,0)
          15 +    print(f'y={y:.2f} blocked at x={p[0]:.3f} y={p[1]:.3f}')
diff --git a/probe_motion_4.py b/probe_motion_4.py
new file mode 100644
index 0000000..99fc58d
--- /dev/null
+++ b/probe_motion_4.py
@@ -0,0 +1,14 @@
           1 +from probe_motion_lib import *
           2 +import sys
           3 +seed=int(sys.argv[1])
           4 +obs,_=env.reset(seed=seed)
           5 +print('pillars/mounds', [(n,v[0],v[1],v[3]) for n,v in obstacles(obs)])
           6 +for i,sx,ux in [(0,1.0,-1),(1,-1.0,1)]:
           7 +  res=[]
           8 +  for y in np.arange(-2.25,2.26,0.05):
           9 +    obs,_=env.reset(seed=seed)
          10 +    p=goto(i,sx,-1.75); p=goto(i,sx,y)
          11 +    if abs(p[1]-y)>1e-3: res.append((round(y,2),'unreach')); continue
          12 +    p=approach(i,ux,0,steps=(0.2,0.05,0.01))
          13 +    res.append((round(y,2),round(p[0],3)))
          14 +  print('rover',i,res)
diff --git a/probe_motion_5.py b/probe_motion_5.py
new file mode 100644
index 0000000..c3ed225
--- /dev/null
+++ b/probe_motion_5.py
@@ -0,0 +1,43 @@
           1 +from probe_motion_lib import *
           2 +import math,sys
           3 +def probe(seed, i, start, ang, th=None):
           4 +    obs,_=env.reset(seed=seed)
           5 +    p=goto(i,*start)
           6 +    if th is not None:
           7 +        for _ in range(20):
           8 +            cur=rov(env.step(act(i))[0],i)[2]; d=(th-cur+math.pi)%(2*math.pi)-math.pi
           9 +            if abs(d)<1e-4: break
          10 +            step(i,0,0,np.clip(d,-.4,.4))
          11 +    ux,uy=math.cos(ang),math.sin(ang)
          12 +    p=approach(i,ux,uy,steps=(0.1,0.02,0.004,0.001,0.0002))
          13 +    return p
          14 +mode=sys.argv[1]
          15 +if mode=='pillar':
          16 +    # seed2 pillar obstacle11 at (0.735,0.444) half .05
          17 +    cx,cy=0.735,0.444
          18 +    for deg in [0,30,45,60,90,180,225,270]:
          19 +        a=math.radians(deg)
          20 +        st=(cx-0.5*math.cos(a), cy-0.5*math.sin(a))
          21 +        p=probe(2,0,st,a)
          22 +        dx,dy=p[0]-cx,p[1]-cy
          23 +        # box distance
          24 +        bx=max(abs(dx)-0.05,0); by=max(abs(dy)-0.05,0)
          25 +        print(f'pillar approach {deg}deg stop ({p[0]:.4f},{p[1]:.4f}) center-dist {math.hypot(dx,dy):.4f} box-dist {math.hypot(bx,by):.4f} gaps {abs(dx)-0.05:.4f},{abs(dy)-0.05:.4f}')
          26 +    for th in [0, math.pi/4, math.pi/2]:
          27 +        p=probe(2,0,(cx+0.5,cy),math.pi,th); print('theta',round(th,3),'from +x stop x',round(p[0],4),'gap',round(p[0]-cx-0.05,4))
          28 +elif mode=='mound':
          29 +    # mound obstacle2 (0.5,2.0) half .25 ; approach from below and from right, diag
          30 +    cx,cy=0.5,2.0
          31 +    for deg,st in [(90,(0.5,1.2)),(180,(1.3,2.0)),(135,(1.2,1.3)),(90,(0.9,1.2)),(90,(0.95,1.2)),(90,(1.0,1.2)),(180,(1.3,2.3))]:
          32 +        a=math.radians(deg); p=probe(int(sys.argv[2]),0,st,a)
          33 +        dx,dy=p[0]-cx,p[1]-cy; bx=max(abs(dx)-0.25,0); by=max(abs(dy)-0.25,0)
          34 +        print(f'mound from {st} dir {deg} stop ({p[0]:.4f},{p[1]:.4f}) box-dist {math.hypot(bx,by):.4f} center-dist {math.hypot(dx,dy):.4f}')
          35 +elif mode=='bounds':
          36 +    for deg,st in [(0,(1,0)),(90,(1,0)),(270,(1,0)),(180,(-1,0.)),(180,(1,0))]:
          37 +        i=1 if st[0]<0 else 0
          38 +        p=probe(2,i,st,math.radians(deg)); print('bound dir',deg,'rover',i,np.round(p,4))
          39 +elif mode=='lander':
          40 +    cx,cy=-1.9,-2.0
          41 +    for deg,st in [(180,(-1.0,-2.0)),(180,(-1.0,-1.75)),(270,(-1.9,-1.0)),(270,(-1.7,-1.0)),(225,(-1.2,-1.3)),(180,(-1.0,-2.2))]:
          42 +        p=probe(int(sys.argv[2]),1,st,math.radians(deg))
          43 +        print(f'lander from {st} dir {deg} stop ({p[0]:.4f},{p[1]:.4f}) center-dist {math.hypot(p[0]-cx,p[1]-cy):.4f}')
diff --git a/probe_motion_6.py b/probe_motion_6.py
new file mode 100644
index 0000000..8b3b9cd
--- /dev/null
+++ b/probe_motion_6.py
@@ -0,0 +1,12 @@
           1 +from probe_motion_lib import *
           2 +import math
           3 +for ang in [0,90,180,270]:
           4 +    obs,_=env.reset(seed=0); ux,uy=math.cos(math.radians(ang)),math.sin(math.radians(ang))
           5 +    d=0
           6 +    for k in range(200):
           7 +        obs,*_=step(0,0.005*ux,0.005*uy); r=rov(obs,0)
           8 +        if r[5]<0.5: print('dir',ang,'at_home->0 at dist',round(math.hypot(r[0]-1,r[1]+1.75),4)); break
           9 +obs,_=env.reset(seed=0); n=0
          10 +while True:
          11 +    obs,r,te,tr,inf=env.step(act(0)); n+=1
          12 +    if te or tr or n>1100: print('ended at',n,te,tr); break
diff --git a/probe_motion_lib.py b/probe_motion_lib.py
new file mode 100644
index 0000000..9683999
--- /dev/null
+++ b/probe_motion_lib.py
@@ -0,0 +1,33 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +T = {t.name: t for t in env.observation_space.types}
           5 +def rov(obs, i):
           6 +    o = [r for r in obs.get_objects(T['rover']) if r.name==f'rover{i}'][0]
           7 +    return [float(obs.get(o,f)) for f in ['x','y','theta','store_full','calibrated','at_home']]
           8 +def obstacles(obs):
           9 +    return [(o.name,[round(float(obs.get(o,f)),3) for f in ['x','y','z','half_x','half_y','half_z']]) for o in obs.get_objects(T['obstacle'])]
          10 +def act(i, dx=0, dy=0, dth=0):
          11 +    a = np.zeros(8, dtype=np.float32); a[4*i:4*i+3]=[dx,dy,dth]; return a
          12 +def step(i, dx=0, dy=0, dth=0):
          13 +    return env.step(act(i,dx,dy,dth))
          14 +def drive_until_stop(i, dx, dy, nmax=200):
          15 +    obs = None
          16 +    prev = None
          17 +    for k in range(nmax):
          18 +        obs,*_ = step(i,dx,dy)
          19 +        p = rov(obs,i)[:2]
          20 +        if prev is not None and abs(p[0]-prev[0])<1e-9 and abs(p[1]-prev[1])<1e-9: return p
          21 +        prev = p
          22 +    return prev
          23 +def goto(i, tx, ty, s=0.2, n=100):
          24 +    for k in range(n):
          25 +        obs,*_ = step(i,0,0); p=rov(obs,i)
          26 +        ex,ey = tx-p[0], ty-p[1]
          27 +        if abs(ex)<1e-6 and abs(ey)<1e-6: return p
          28 +        obs,*_ = step(i, np.clip(ex,-s,s), np.clip(ey,-s,s))
          29 +    return rov(obs,i)
          30 +def approach(i, ux, uy, steps=(0.2,0.05,0.01,0.002)):
          31 +    p=None
          32 +    for s in steps: p=drive_until_stop(i, s*ux, s*uy)
          33 +    return p
diff --git a/probe_ops_1.py b/probe_ops_1.py
new file mode 100644
index 0000000..f228da9
--- /dev/null
+++ b/probe_ops_1.py
@@ -0,0 +1,12 @@
           1 +from probe_ops_lib import *
           2 +reset(1)
           3 +# test move semantics: is dx world frame? rover1 theta=0
           4 +print(pos(1)); step(1,0.1,0); print(pos(1)); step(1,dth=0.4); step(1,0.1,0); print(pos(1))
           5 +# sample1 at (-1.49,-1.37); approach to various distances
           6 +sx,sy=get('sample1')[:2]
           7 +for d in [0.4,0.3,0.27,0.25,0.23,0.2,0.15,0.1]:
           8 +    goto(1,sx+d,sy)
           9 +    step(1,op='sample'); p=pos(1)
          10 +    print('d',d,'pos',[round(v,3) for v in p],'dist',round(math.hypot(p[0]-sx,p[1]-sy),3),'s1',[round(v,2) for v in get('sample1')] if 'sample1' in names('sample') else 'GONE')
          11 +    if p[3]==1: break
          12 +print(dump('sample'))
diff --git a/probe_ops_10.py b/probe_ops_10.py
new file mode 100644
index 0000000..0a80d05
--- /dev/null
+++ b/probe_ops_10.py
@@ -0,0 +1,15 @@
           1 +from probe_ops_lib import *
           2 +reset(14)
           3 +ox,oy=get('objective0')[:2]; px,py=get('obstacle7')[:2]
           4 +dd=math.hypot(px-ox,py-oy); ux,uy=(px-ox)/dd,(py-oy)/dd; vx,vy=-uy,ux
           5 +goto(0,1.0,0.0)
           6 +for L in [1.8,1.3]:
           7 +  for s in [-0.4,-0.3,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.3,0.4]:
           8 +    tx,ty=ox+L*ux+s*vx,oy+L*uy+s*vy
           9 +    ok=goto(0,tx,ty,tol=0.005)
          10 +    step(0,op='calibrate'); c=pos(0)[4]
          11 +    if c: step(0,op='image')
          12 +    x,y=pos(0)[:2]
          13 +    # perpendicular distance of pillar center from rover-objective segment
          14 +    ax,ay=ox-x,oy-y; t=((px-x)*ax+(py-y)*ay)/(ax*ax+ay*ay); perp=math.hypot(x+t*ax-px,y+t*ay-py)
          15 +    print('L',L,'s',s,'reached',ok,'cal',c,'perp_dist_pillar_to_line',round(perp,3),'img',get('objective0')[3])
diff --git a/probe_ops_11.py b/probe_ops_11.py
new file mode 100644
index 0000000..3c263cd
--- /dev/null
+++ b/probe_ops_11.py
@@ -0,0 +1,13 @@
           1 +from probe_ops_lib import *
           2 +reset(0)
           3 +for wp in [(-0.5,-1.2),(-0.45,-0.2),(-0.3,0.6)]: print(goto(1,*wp),[round(v,2) for v in pos(1)[:2]])
           4 +x,y=pos(1)[:2]
           5 +for n in names('objective'): o=get(n); print(n,'dist',round(math.hypot(o[0]-x,o[1]-y),2))
           6 +step(1,op='calibrate'); print('cal',pos(1)[4])
           7 +if pos(1)[4]: step(1,op='image'); print(dump('objective'))
           8 +# move closer to wall & up
           9 +for wp in [(-0.3,1.2)]:
          10 +    print(goto(1,*wp)); x,y=pos(1)[:2]
          11 +    for n in names('objective'): o=get(n); print(n,'dist',round(math.hypot(o[0]-x,o[1]-y),2))
          12 +    step(1,op='calibrate'); print('cal',pos(1)[4])
          13 +    if pos(1)[4]: step(1,op='image'); print(dump('objective'))
diff --git a/probe_ops_12.py b/probe_ops_12.py
new file mode 100644
index 0000000..eb01e4b
--- /dev/null
+++ b/probe_ops_12.py
@@ -0,0 +1,11 @@
           1 +from probe_ops_lib import *
           2 +reset(14)
           3 +ox,oy=get('objective0')[:2]; px,py=get('obstacle7')[:2]
           4 +dd=math.hypot(px-ox,py-oy); ux,uy=(px-ox)/dd,(py-oy)/dd
           5 +goto(0,1.0,0.0)
           6 +for L in [1.6,1.45,1.4,1.36]:
           7 +    tx,ty=ox+L*ux,oy+L*uy
           8 +    ok=goto(0,tx,ty,tol=0.005); x,y=pos(0)[:2]
           9 +    step(0,op='calibrate'); c=pos(0)[4]
          10 +    if c: step(0,op='image')
          11 +    print('L',L,ok,'pos',round(x,3),round(y,3),'distpillar',round(math.hypot(px-x,py-y),3),'cal',c)
diff --git a/probe_ops_13.py b/probe_ops_13.py
new file mode 100644
index 0000000..5fc182d
--- /dev/null
+++ b/probe_ops_13.py
@@ -0,0 +1,15 @@
           1 +from probe_ops_lib import *
           2 +reset(14)
           3 +for wp in [(1.0,0.0),(1.3,1.2),(1.78,1.45)]: print(goto(0,*wp),[round(v,2) for v in pos(0)[:2]])
           4 +step(0,op='sample'); print('store',pos(0)[3],get('sample5'))
           5 +step(0,op='calibrate'); step(0,op='image'); print('img',get('objective0'))
           6 +for wp in [(2.2,1.2),(2.2,0.6)]: print(goto(0,*wp))
           7 +lx,ly=get('lander')[:2]
           8 +turn_to(0,0.56); print('theta',pos(0)[2])
           9 +x,y=pos(0)[:2]; d=math.hypot(lx-x,ly-y); ux,uy=(lx-x)/d,(ly-y)/d
          10 +for k in range(40):
          11 +    step(0,op='send'); x,y=pos(0)[:2]
          12 +    r1=get('objective0')[5]; r2=get('sample5')[6]
          13 +    if r1 or r2: print('send ok at dist',round(math.hypot(lx-x,ly-y),3),'img recv',r1,'ana recv',r2,'store',pos(0)[3],'theta',pos(0)[2]); break
          14 +    step(0,0.05*ux,0.05*uy)
          15 +print(dump('rover'))
diff --git a/probe_ops_14.py b/probe_ops_14.py
new file mode 100644
index 0000000..d4f0cb3
--- /dev/null
+++ b/probe_ops_14.py
@@ -0,0 +1,26 @@
           1 +from probe_ops_lib import *
           2 +reset(14)
           3 +for wp in [(1.0,0.0),(1.3,1.2),(1.78,1.45)]: goto(0,*wp)
           4 +step(0,op='sample')
           5 +ox,oy=get('objective0')[:2]
           6 +# calibrate threshold: move away to 2.1, approach in 0.005 steps
           7 +for wp in [(2.2,1.2),(2.2,0.6)]: goto(0,*wp)
           8 +x,y=pos(0)[:2]; d=math.hypot(ox-x,oy-y); ux,uy=(ox-x)/d,(oy-y)/d
           9 +goto(0,ox-2.05*ux,oy-2.05*uy,tol=0.002)
          10 +for k in range(30):
          11 +    step(0,op='calibrate'); x,y=pos(0)[:2]
          12 +    if pos(0)[4]: print('cal at 2D',round(math.hypot(ox-x,oy-y),4)); break
          13 +    step(0,0.005*ux,0.005*uy)
          14 +step(0,op='image')
          15 +lx,ly=get('lander')[:2]
          16 +x,y=pos(0)[:2]; d=math.hypot(lx-x,ly-y); ux,uy=(lx-x)/d,(ly-y)/d
          17 +goto(0,lx-4.12*ux,ly-4.12*uy,tol=0.002)
          18 +for k in range(30):
          19 +    step(0,op='send'); x,y=pos(0)[:2]
          20 +    if get('objective0')[5]: print('send at 2D',round(math.hypot(lx-x,ly-y),4)); break
          21 +    step(0,0.005*ux,0.005*uy)
          22 +step(0,op='drop'); print('after drop',pos(0))
          23 +goto(0,1.0,0.0); goto(0,1.0,-1.75,tol=0.001)
          24 +r,term,trunc=step(0); print('home',pos(0),'r',r,'term',term,'n',S.n, dump('sample'),dump('objective'), S.info)
          25 +for (x,y) in [(1.2,-1.75),(1.0,-1.4)]:
          26 +    goto(0,x,y,tol=0.001); r,term,trunc=step(0); print((x,y),'at_home',pos(0)[5],r,term)
diff --git a/probe_ops_15.py b/probe_ops_15.py
new file mode 100644
index 0000000..6242249
--- /dev/null
+++ b/probe_ops_15.py
@@ -0,0 +1,12 @@
           1 +from probe_ops_lib import *
           2 +reset(14)
           3 +for wp in [(-1.0,-1.2),(-1.5,-1.2),(-1.47,-0.65)]: print(goto(1,*wp))
           4 +step(1,op='sample'); print('r1 store',pos(1)[3])
           5 +for wp in [(-1.5,0.0),(-1.5,2.25)]: print(goto(1,*wp,tol=0.002),pos(1)[:2])
           6 +lx,ly=get('lander')[:2]
           7 +for k in range(80):
           8 +    step(1,op='send'); x,y=pos(1)[:2]
           9 +    if get('sample2')[6]: print('send at 2D',round(math.hypot(lx-x,ly-y),4),'pos',x,y); break
          10 +    yy=pos(1)[1]; step(1,0,-0.005)
          11 +    if abs(pos(1)[1]-yy)<1e-6: print('blocked'); break
          12 +print(S.n)
diff --git a/probe_ops_16.py b/probe_ops_16.py
new file mode 100644
index 0000000..d9bb9ce
--- /dev/null
+++ b/probe_ops_16.py
@@ -0,0 +1,11 @@
           1 +from probe_ops_lib import *
           2 +reset(14)
           3 +for wp in [(-1.0,-1.2),(-1.5,-1.2),(-1.47,-0.65)]: goto(1,*wp)
           4 +step(1,op='sample'); goto(1,-1.5,-1.2); step(1,op='send'); step(1,op='drop'); goto(1,-1.0,-1.75,tol=0.001)
           5 +r,term,tr=step(1); print('r1 home',pos(1),r,term,S.n)
           6 +for wp in [(1.0,0.0),(1.3,1.2),(1.78,1.45)]: goto(0,*wp)
           7 +step(0,op='sample'); step(0,op='calibrate'); step(0,op='image')
           8 +for wp in [(1.3,1.2),(1.0,0.0),(1.0,-0.5)]: goto(0,*wp)
           9 +r,term,tr=step(0,op='send'); print('sent',r,term,dump('objective'),get('sample5'))
          10 +r,term,tr=step(0,op='drop'); print('drop',r,term)
          11 +goto(0,1.0,-1.75,tol=0.001); r,term,tr=step(0); print('home',r,term,tr,pos(0),pos(1),S.n,S.info)
diff --git a/probe_ops_17.py b/probe_ops_17.py
new file mode 100644
index 0000000..4c61611
--- /dev/null
+++ b/probe_ops_17.py
@@ -0,0 +1,17 @@
           1 +from probe_ops_lib import *
           2 +import sys
           3 +def run(do_rock, do_drop):
           4 +    reset(14)
           5 +    for wp in [(-1.0,-1.2),(-1.5,-1.2),(-1.47,-0.65)]: goto(1,*wp)
           6 +    step(1,op='sample'); goto(1,-1.5,-1.2); step(1,op='send')
           7 +    if do_drop: step(1,op='drop')
           8 +    goto(1,-1.0,-1.75,tol=0.001)
           9 +    for wp in [(1.0,0.0),(1.3,1.2),(1.78,1.45)]: goto(0,*wp)
          10 +    if do_rock: step(0,op='sample')
          11 +    step(0,op='calibrate'); step(0,op='image')
          12 +    for wp in [(1.3,1.2),(1.0,0.0),(1.0,-0.5)]: goto(0,*wp)
          13 +    step(0,op='send'); step(0,op='drop')
          14 +    goto(0,1.0,-1.75,tol=0.001); r,term,tr=step(0); print('rock',do_rock,'drop',do_drop,'term',term,'store1',pos(1)[3])
          15 +    if not term and not do_drop:
          16 +        r,term,tr=step(1,op='drop'); print(' after r1 drop term',term)
          17 +run(False,True); run(True,False)
diff --git a/probe_ops_18.py b/probe_ops_18.py
new file mode 100644
index 0000000..7ea76d6
--- /dev/null
+++ b/probe_ops_18.py
@@ -0,0 +1,19 @@
           1 +from probe_ops_lib import *
           2 +def run(two_soil, two_rock=True):
           3 +    reset(1)
           4 +    goto(1,-1.27,-1.37); step(1,op='sample'); step(1,op='send'); step(1,op='drop')
           5 +    goto(1,-1.7,-1.2); goto(1,-1.7,0.17)
           6 +    if two_soil:
           7 +        goto(1,-1.92,0.17); step(1,op='sample'); step(1,op='send'); step(1,op='drop')
           8 +    goto(1,-1.92,0.17); step(1,op='calibrate'); step(1,op='image'); step(1,op='send')
           9 +    goto(1,-1.7,-1.2); goto(1,-1.0,-1.2); goto(1,-1.0,-1.75,tol=0.001)
          10 +    goto(0,0.77,-1.35); step(0,op='sample'); step(0,op='send'); step(0,op='drop')
          11 +    if two_rock:
          12 +        goto(0,1.0,-0.5); goto(0,2.0,0.5); goto(0,2.3,1.17); step(0,op='sample')
          13 +    else: goto(0,1.0,-0.5); goto(0,2.0,0.5); goto(0,2.3,1.17)
          14 +    step(0,op='calibrate'); step(0,op='image')
          15 +    goto(0,2.0,0.5); goto(0,1.0,-0.5); step(0,op='send'); step(0,op='drop')
          16 +    goto(0,1.0,-1.75,tol=0.001); r,term,tr=step(0)
          17 +    print('two_soil',two_soil,'two_rock',two_rock,'term',term,'n',S.n)
          18 +    print(' ',dump('objective')); print(' ',dump('sample')); print(' ',dump('rover'))
          19 +run(True); run(False); run(True,False)
diff --git a/probe_ops_2.py b/probe_ops_2.py
new file mode 100644
index 0000000..ab25be3
--- /dev/null
+++ b/probe_ops_2.py
@@ -0,0 +1,17 @@
           1 +from probe_ops_lib import *
           2 +reset(1)
           3 +sx,sy=get('sample3')[:2]
           4 +goto(0,sx+0.3,sy); print(pos(0))
           5 +for k in range(20):
           6 +    step(0,-0.005,0,op='sample'); p=pos(0)
           7 +    if p[3]==1: print('sampled at dist',round(math.hypot(p[0]-sx,p[1]-sy),4),'theta',p[2]); break
           8 +# small move test
           9 +x0=pos(0)[0]; step(0,0.01,0); print('small move dx', pos(0)[0]-x0)
          10 +# drop
          11 +step(0,op='drop'); print('after drop',[round(v,2) for v in pos(0)], get('sample3'))
          12 +# sample again same sample with rover0
          13 +step(0,op='sample'); print('resample', pos(0)[3], get('sample3'))
          14 +step(0,op='drop')
          15 +# rover1: go to sample3? wall in middle; try sample1 by rover1 then rover0 can't. Instead try rover1 sampling sample1, drop, then sample again
          16 +sx1,sy1=get('sample1')[:2]
          17 +goto(1,sx1+0.2,sy1); step(1,op='sample'); print('r1 sample1',pos(1)[3],get('sample1'))
diff --git a/probe_ops_3.py b/probe_ops_3.py
new file mode 100644
index 0000000..5e02842
--- /dev/null
+++ b/probe_ops_3.py
@@ -0,0 +1,12 @@
           1 +from probe_ops_lib import *
           2 +reset(0)
           3 +for y in [-1.75,-1.0,0.5,1.5,2.4]:
           4 +    goto(0,1.0,y); goto(0,-0.5,y,maxn=30); print('r0 wall test y',y,[round(v,3) for v in pos(0)[:2]])
           5 +reset(0)
           6 +goto(1,-0.27,-1.75); goto(1,0.5,-1.75,maxn=20); print('r1 rightmost',pos(1)[:2])
           7 +# sample4 at -0.27,-2.04
           8 +sx,sy=get('sample4')[:2]
           9 +goto(1,sx-0.2,sy); step(1,op='sample'); print('r1 sampled',pos(1)[3],get('sample4'))
          10 +step(1,op='drop'); goto(1,sx-0.4,sy+0.3)
          11 +goto(0,0.3,-1.75); goto(0,sx+0.22,sy); print('r0 pos',pos(0)[:2],'dist',math.hypot(pos(0)[0]-sx,pos(0)[1]-sy))
          12 +step(0,op='sample'); print('r0 sampled',pos(0)[3],get('sample4'))
diff --git a/probe_ops_4.py b/probe_ops_4.py
new file mode 100644
index 0000000..bc2fc17
--- /dev/null
+++ b/probe_ops_4.py
@@ -0,0 +1,19 @@
           1 +from probe_ops_lib import *
           2 +reset(0)
           3 +last=None
           4 +for k in range(60):
           5 +    step(0,-0.02,0); x=pos(0)[0]
           6 +    if last is not None and abs(x-last)<1e-6: break
           7 +    last=x
           8 +print('r0 stops at',pos(0)[:2])
           9 +for k in range(30):
          10 +    step(1,0.02,0); 
          11 +print('r1 at',pos(1)[:2])
          12 +reset(1)
          13 +# approach sample1 from +x in tiny steps on its y
          14 +sx,sy=get('sample1')[:2]
          15 +goto(1,sx+0.4,sy)
          16 +for k in range(40):
          17 +    x=pos(1)[0]; step(1,-0.005,0); 
          18 +    if abs(pos(1)[0]-x)<1e-6: print('blocked at dist',pos(1)[0]-sx); break
          19 +else: print('no block, dist',pos(1)[0]-sx)
diff --git a/probe_ops_5.py b/probe_ops_5.py
new file mode 100644
index 0000000..d53aeca
--- /dev/null
+++ b/probe_ops_5.py
@@ -0,0 +1,13 @@
           1 +from probe_ops_lib import *
           2 +for y in [-1.75,-1.2]:
           3 +    reset(0)
           4 +    if y!=-1.75:
           5 +        for k in range(3): step(1,0,0.2)
           6 +    for k in range(80):
           7 +        x=pos(1)[0]; step(1,0.02,0)
           8 +        if abs(pos(1)[0]-x)<1e-6: break
           9 +    print('r1 stops',pos(1)[:2])
          10 +    for k in range(80):
          11 +        x=pos(0)[0]; step(0,-0.02,0)
          12 +        if abs(pos(0)[0]-x)<1e-6: break
          13 +    print('r0 stops',pos(0)[:2])
diff --git a/probe_ops_6.py b/probe_ops_6.py
new file mode 100644
index 0000000..ebef129
--- /dev/null
+++ b/probe_ops_6.py
@@ -0,0 +1,18 @@
           1 +from probe_ops_lib import *
           2 +reset(1)
           3 +def push(i,dx,dy,n=200):
           4 +    for k in range(n):
           5 +        x,y=pos(i)[:2]; step(i,dx,dy)
           6 +        if math.hypot(pos(i)[0]-x,pos(i)[1]-y)<1e-6: break
           7 +    return [round(v,3) for v in pos(i)[:2]]
           8 +print('down',push(1,0,-0.05)); print('left',push(1,-0.05,0))
           9 +print('right', push(1,0.05,0))
          10 +for yy in [-1.0,-0.5,0,0.5,1.0,1.5,2.0,2.5]:
          11 +    p=pos(1); 
          12 +    push(1,-0.05,0,n=4)
          13 +    for k in range(60):
          14 +        y=pos(1)[1]
          15 +        if y>=yy: break
          16 +        step(1,0,min(0.1,yy-y)); 
          17 +    print('y',round(pos(1)[1],2),'right',push(1,0.05,0))
          18 +print('up',push(1,0,0.05))
diff --git a/probe_ops_7.py b/probe_ops_7.py
new file mode 100644
index 0000000..9eb4421
--- /dev/null
+++ b/probe_ops_7.py
@@ -0,0 +1,15 @@
           1 +from probe_ops_lib import *
           2 +reset(1)
           3 +for wp in [(-1.0,-1.2),(-1.7,-1.2),(-1.7,0.9)]:
           4 +    print(goto(1,*wp), [round(v,2) for v in pos(1)])
           5 +ox,oy=get('objective1')[:2]
           6 +x,y=pos(1)[:2]; bearing=math.atan2(oy-y,ox-x); print('bearing',bearing,'dist',math.hypot(ox-x,oy-y))
           7 +th0=pos(1)[2]
           8 +for k in range(17):
           9 +    step(1,op='calibrate'); c=pos(1)[4]
          10 +    msg=''
          11 +    if c==1:
          12 +        step(1,op='image'); msg='img->'+str(get('objective1')[3:6])+' cal '+str(pos(1)[4])
          13 +    rel=(pos(1)[2]-bearing+math.pi)%(2*math.pi)-math.pi
          14 +    print('theta',round(pos(1)[2],2),'rel',round(rel,2),'cal',c,msg)
          15 +    step(1,dth=0.4)
diff --git a/probe_ops_8.py b/probe_ops_8.py
new file mode 100644
index 0000000..9f3d716
--- /dev/null
+++ b/probe_ops_8.py
@@ -0,0 +1,18 @@
           1 +from probe_ops_lib import *
           2 +reset(1)
           3 +for wp in [(-1.0,-1.2),(-1.7,-1.2)]: goto(1,*wp)
           4 +ox,oy=get('objective1')[:2]
           5 +def d(): x,y=pos(1)[:2]; return math.hypot(ox-x,oy-y)
           6 +step(1,op='image'); print('image w/o cal ->',get('objective1')[3:6])
           7 +# scan calibrate far->near
           8 +while pos(1)[1]<1.0:
           9 +    step(1,op='calibrate')
          10 +    if pos(1)[4]==1: print('calibrated at dist',round(d(),3),pos(1)[:2]); break
          11 +    step(1,0,0.05)
          12 +# move back far keeping cal
          13 +goto(1,-1.7,-1.2); print('cal after moving',pos(1)[4])
          14 +while pos(1)[1]<1.0:
          15 +    step(1,op='image')
          16 +    if get('objective1')[4]==1: print('image at dist',round(d(),3),'cal now',pos(1)[4]); break
          17 +    if pos(1)[4]==0: print('cal lost at',d()); break
          18 +    step(1,0,0.05)
diff --git a/probe_ops_9.py b/probe_ops_9.py
new file mode 100644
index 0000000..151cbc6
--- /dev/null
+++ b/probe_ops_9.py
@@ -0,0 +1,13 @@
           1 +from probe_ops_lib import *
           2 +for seed in range(30):
           3 +    reset(seed)
           4 +    pil=[get(n) for n in names('obstacle') if get(n)[3]<0.1]
           5 +    for on in names('objective'):
           6 +        ox,oy=get(on)[:2]
           7 +        for p in pil:
           8 +            dd=math.hypot(p[0]-ox,p[1]-oy)
           9 +            if 0.5<dd<1.3 and p[0]*ox>0:
          10 +                ux,uy=(p[0]-ox)/dd,(p[1]-oy)/dd
          11 +                tx,ty=ox+1.8*ux,oy+1.8*uy
          12 +                if abs(tx)>0.4 and tx*ox>0 and abs(ty)<2.2 and abs(tx)<2.2:
          13 +                    print(seed,on,(round(ox,2),round(oy,2)),'pillar',(round(p[0],2),round(p[1],2)),'d',round(dd,2),'target',(round(tx,2),round(ty,2)))
diff --git a/probe_ops_layout.py b/probe_ops_layout.py
new file mode 100644
index 0000000..1f10e8a
--- /dev/null
+++ b/probe_ops_layout.py
@@ -0,0 +1,9 @@
           1 +from env_client import make_env
           2 +env=make_env()
           3 +T={t.name:t for t in env.observation_space.types}
           4 +F={'rover':['x','y','theta','store_full','calibrated','at_home'],'lander':['x','y','z'],'objective':['x','y','z','have_image_rover0','have_image_rover1','received_image'],'sample':['x','y','z','is_soil','analyzed_rover0','analyzed_rover1','received_analysis'],'obstacle':['x','y','z','half_x','half_y','half_z']}
           5 +import sys
           6 +for seed in map(int,sys.argv[1:]):
           7 +    obs,info=env.reset(seed=seed); print('seed',seed,info)
           8 +    for t in F:
           9 +        for o in obs.get_objects(T[t]): print(' ',o.name,[round(float(obs.get(o,f)),2) for f in F[t]])
diff --git a/probe_ops_lib.py b/probe_ops_lib.py
new file mode 100644
index 0000000..291c92b
--- /dev/null
+++ b/probe_ops_lib.py
@@ -0,0 +1,50 @@
           1 +from env_client import make_env
           2 +import numpy as np, math
           3 +env=make_env()
           4 +T={t.name:t for t in env.observation_space.types}
           5 +F={'rover':['x','y','theta','store_full','calibrated','at_home'],'lander':['x','y','z'],'objective':['x','y','z','have_image_rover0','have_image_rover1','received_image'],'sample':['x','y','z','is_soil','analyzed_rover0','analyzed_rover1','received_analysis'],'obstacle':['x','y','z','half_x','half_y','half_z']}
           6 +SEL={'sample':-5/6,'calibrate':-0.5,'image':-1/6,'noop':1/6,'send':0.5,'drop':5/6}
           7 +class S:
           8 +    obs=None; term=False; info=None; n=0
           9 +def reset(seed):
          10 +    S.obs,S.info=env.reset(seed=seed); S.n=0; return S.obs
          11 +def get(name):
          12 +    o=S.obs.get_object_from_name(name)
          13 +    return [float(S.obs.get(o,f)) for f in F[o.type.name]]
          14 +def names(t): return [o.name for o in S.obs.get_objects(T[t])]
          15 +def dump(t):
          16 +    return {n:[round(v,2) for v in get(n)] for n in names(t)}
          17 +def step(i=0,dx=0,dy=0,dth=0,op='noop',op2='noop'):
          18 +    a=np.zeros(8,dtype=np.float32)
          19 +    a[3]=SEL['noop']; a[7]=SEL['noop']
          20 +    a[4*i:4*i+3]=[dx,dy,dth]; a[4*i+3]=SEL[op]
          21 +    a[4*(1-i)+3]=SEL[op2]
          22 +    S.obs,r,term,trunc,S.info=env.step(a); S.n+=1; S.term=term
          23 +    return r,term,trunc
          24 +def pos(i): return get(f'rover{i}')
          25 +def goto(i,tx,ty,tol=0.02,maxn=200):
          26 +    import random
          27 +    stuck=0
          28 +    for k in range(maxn):
          29 +        x,y=pos(i)[:2]; d=math.hypot(tx-x,ty-y)
          30 +        if d<tol: return True
          31 +        s=min(0.2,d); dx=(tx-x)/d*s; dy=(ty-y)/d*s
          32 +        step(i,dx,dy)
          33 +        x2,y2=pos(i)[:2]
          34 +        if math.hypot(x2-x,y2-y)<1e-4:
          35 +            # detour
          36 +            moved=False
          37 +            for ang in [math.pi/2,-math.pi/2,math.pi/4,-math.pi/4,3*math.pi/4,-3*math.pi/4]:
          38 +                c,sn=math.cos(ang),math.sin(ang)
          39 +                ddx=(dx*c-dy*sn); ddy=(dx*sn+dy*c)
          40 +                n=0.2/max(1e-9,math.hypot(ddx,ddy))
          41 +                for _ in range(2): step(i,ddx*n,ddy*n)
          42 +                x3,y3=pos(i)[:2]
          43 +                if math.hypot(x3-x,y3-y)>1e-3: moved=True; break
          44 +            if not moved: return False
          45 +    return False
          46 +def turn_to(i,th):
          47 +    for _ in range(40):
          48 +        t=pos(i)[2]; e=(th-t+math.pi)%(2*math.pi)-math.pi
          49 +        if abs(e)<1e-3: return
          50 +        step(i,dth=max(-0.4,min(0.4,e)))
diff --git a/probe_order.py b/probe_order.py
new file mode 100644
index 0000000..7f459d2
--- /dev/null
+++ b/probe_order.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +T = {t.name:t for t in env.observation_space.types}
           6 +def g(name,f): return float(obs.get(obs.get_object_from_name(name),f))
           7 +# rover1 at (-1,-1.75). sample3 soil at (-1.387,0.152). move rover1 up along x=-1 ... find path: go to x=-1.387+? check pillars
           8 +print([ (o.name, round(g(o.name,'x'),2), round(g(o.name,'y'),2)) for o in obs.get_objects(T['obstacle'])])
           9 +def step(a):
          10 +    global obs
          11 +    obs,r,te,tr,info = env.step(np.array(a,dtype=np.float32)); return te
          12 +# move rover1 to (-1.0, 0.152-0.45) area: path along x=-1 upward: pillars at (-0.808,0.192),(-1.354,0.554),(-1.808,-1.549)
          13 +for i in range(10): step([0,0,0,1/6, 0,0.2,0,1/6])
          14 +print('r1', g('rover1','x'), g('rover1','y'))
          15 +# now at y=0.25? compute
          16 +step([0,0,0,1/6, -0.2,0.15,0,-5/6])
          17 +print('r1', g('rover1','x'), g('rover1','y'), 'store', g('rover1','store_full'))
          18 +# move away while sampling? test pre: drop then move away with sample
          19 +step([0,0,0,1/6, 0,0,0,5/6])
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..3d83868
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,22 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seeds = [int(s) for s in sys.argv[1].split(',')] if len(sys.argv) > 1 else list(range(10))
           6 +env = make_env()
           7 +res = []
           8 +for seed in seeds:
           9 +    obs, info = env.reset(seed=seed)
          10 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          11 +    t0 = time.time()
          12 +    ap.reset(obs, info)
          13 +    tp = time.time() - t0
          14 +    steps = 0; term = False
          15 +    while steps < 400:
          16 +        obs, r, term, trunc, info = env.step(ap.get_action(obs))
          17 +        steps += 1
          18 +        if term or trunc: break
          19 +    nobj = len(ap.sc.objectives)
          20 +    print(f"seed {seed} nobj {nobj} steps {steps} term {term} plan {tp:.2f}s assign {ap.assign} pathlens {[len(p['path'])-1 for p in ap.plans]}", flush=True)
          21 +    res.append(steps if term else 9999)
          22 +print("mean", np.mean(res), "fails", sum(r == 9999 for r in res))
```

</details>

<a id="C003"></a>
### C003 · Conservative image radius 1.85; all 8 seeds solved

Commit `8832f94b338244b74be1135de4f7938ea705af57`; parents: 6fd490bb568b26e35f424be4251c0dd08ed71e2b. Recorded author date: 2026-10-01T10:35:22+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0299](01_timeline.md#E0299): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_8832f94_approach.py) · [Exact all-file diff](evidence/diffs/C003_8832f94.diff)

[Previous saved controller snapshot](evidence/versions/C002_6fd490b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4db1072..95fd02e 100644
--- a/approach.py
+++ b/approach.py
@@ -3,7 +3,7 @@ import numpy as np
    3      3  
    4      4  H = 0.1            # lattice spacing (a step can move up to 2 cells per axis)
    5      5  R_STEP = 2         # cells per step
    6        -IMG_R = 1.96       # imaging range (true ~2.0)
           6 +IMG_R = 1.85       # imaging range (conservative)
    7      7  SAMP_R = 0.235     # sampling range (true 0.25)
    8      8  SEND_R = 3.85      # send range (true ~4.0)
    9      9  BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..60c15ae
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,21 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed = int(sys.argv[1])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed)
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +ap.reset(obs, info)
          10 +print("tasks", ap.tasks, "mytasks", ap.my_tasks)
          11 +for i in range(2): print(i, "visits", ap.plans[i]['visits'], "path", [tuple(np.round(ap.planners[i].pos(c),2)) for c in ap.plans[i]['path']][:40])
          12 +
          13 +for step in range(int(sys.argv[2]) if len(sys.argv)>2 else 60):
          14 +    a = ap.get_action(obs)
          15 +    obs, r, term, trunc, info = env.step(a)
          16 +    g = obs.get
          17 +    rs = [(round(g(rv,'x'),2), round(g(rv,'y'),2), int(g(rv,'store_full')), int(g(rv,'calibrated'))) for rv in ap.sc.rovers]
          18 +    objs = [(int(g(o,'have_image_rover0')), int(g(o,'have_image_rover1')), int(g(o,'received_image'))) for o in ap.sc.objectives]
          19 +    sm = [(int(g(s,'analyzed_rover0')), int(g(s,'analyzed_rover1')), int(g(s,'received_analysis'))) for s in ap.sc.samples]
          20 +    print(step, np.round(a,2).tolist(), rs, objs, sm, term)
          21 +    if term: break
diff --git a/probe_img.py b/probe_img.py
new file mode 100644
index 0000000..d6a9a56
--- /dev/null
+++ b/probe_img.py
@@ -0,0 +1,7 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=2)
           5 +T = {t.name:t for t in env.observation_space.types}
           6 +for o in obs.get_objects(T['objective']): print(o.name, obs.get(o,'x'), obs.get(o,'y'))
           7 +for o in obs.get_objects(T['obstacle']): print(o.name, round(obs.get(o,'x'),2), round(obs.get(o,'y'),2), obs.get(o,'half_x'))
diff --git a/probe_img2.py b/probe_img2.py
new file mode 100644
index 0000000..87efb3c
--- /dev/null
+++ b/probe_img2.py
@@ -0,0 +1,25 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +T=None
           5 +def run(target, nimg):
           6 +    global T
           7 +    obs, info = env.reset(seed=2)
           8 +    T = {t.name:t for t in env.observation_space.types}
           9 +    r1 = obs.get_object_from_name('rover1')
          10 +    objs = sorted(obs.get_objects(T['objective']), key=lambda o:o.name)
          11 +    def pos(): return np.array([obs.get(r1,'x'), obs.get(r1,'y')])
          12 +    # go straight up x=-1 to y=target y, then x
          13 +    for wp in [(-1.0, target[1]), target]:
          14 +        for _ in range(30):
          15 +            d = np.clip(np.array(wp)-pos(), -0.2, 0.2)
          16 +            if np.abs(d).max() < 1e-6: break
          17 +            obs,*_ = env.step(np.array([0,0,0,1/6, d[0],d[1],0,1/6],dtype=np.float32))
          18 +    print('at', pos().round(3))
          19 +    for k in range(nimg):
          20 +        for op in [-0.5, -1/6]:
          21 +            obs,*_ = env.step(np.array([0,0,0,1/6, 0,0,0,op],dtype=np.float32))
          22 +        print(' after img', k, [(int(obs.get(o,'have_image_rover1'))) for o in objs], 'cal', obs.get(r1,'calibrated'))
          23 +run((-1.1,0.5), 3)
          24 +run((-1.5,0.25), 3)
          25 +run((-1.57,0.31), 3)
diff --git a/probe_vis_0.py b/probe_vis_0.py
new file mode 100644
index 0000000..e2dd86d
--- /dev/null
+++ b/probe_vis_0.py
@@ -0,0 +1,9 @@
           1 +from env_client import make_env
           2 +import sys
           3 +env=make_env()
           4 +for seed in [int(s) for s in sys.argv[1:]]:
           5 +    obs,info=env.reset(seed=seed)
           6 +    print('SEED',seed)
           7 +    for o in obs:
           8 +        f=obs.type_features[o.type]
           9 +        print(o.type.name,o.name,{k:round(float(v),3) for k,v in zip(f,obs.data[o]) if not k.startswith('have_') and k not in('r','g','b')})
```

</details>

<a id="C004"></a>
### C004 · Heading control (face away from target), exact camera visibility model, send LOS model

Commit `4351d31ae2a09db536407d6f1ffb5525ffc7b5ab`; parents: 8832f94b338244b74be1135de4f7938ea705af57. Recorded author date: 2026-10-01T11:03:51+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0803](01_timeline.md#E0803): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_4351d31_approach.py) · [Exact all-file diff](evidence/diffs/C004_4351d31.diff)

[Previous saved controller snapshot](evidence/versions/C003_8832f94_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 95fd02e..5526419 100644
--- a/approach.py
+++ b/approach.py
@@ -3,7 +3,7 @@ import numpy as np
    3      3  
    4      4  H = 0.1            # lattice spacing (a step can move up to 2 cells per axis)
    5      5  R_STEP = 2         # cells per step
    6        -IMG_R = 1.85       # imaging range (conservative)
           6 +IMG_R = 2.0        # imaging range from base when facing away (true ~2.08)
    7      7  SAMP_R = 0.235     # sampling range (true 0.25)
    8      8  SEND_R = 3.85      # send range (true ~4.0)
    9      9  BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
@@ -11,6 +11,10 @@ BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
   11     11  INF = 1e9
   12     12  
   13     13  
          14 +def _wrap(a):
          15 +    return (a + np.pi) % (2 * np.pi) - np.pi
          16 +
          17 +
   14     18  def _type(space, name):
   15     19      for t in space.types:
   16     20          if t.name == name:
@@ -45,6 +49,7 @@ class RoverPlanner:
   45     49          self.home = np.array(home, dtype=float)
   46     50          side = 1.0 if home[0] > 0 else -1.0
   47     51          self.side = side
          52 +        self.img_r = IMG_R
   48     53          xs = []
   49     54          x = self.home[0]
   50     55          while x - H >= -2.27:
@@ -92,7 +97,7 @@ class RoverPlanner:
   92     97          sc = self.scene
   93     98          if kind == "obj":
   94     99              o = sc.opos[k]
   95        -            m = (self.X - o[0]) ** 2 + (self.Y - o[1]) ** 2 <= IMG_R ** 2
         100 +            m = (self.X - o[0]) ** 2 + (self.Y - o[1]) ** 2 <= self.img_r ** 2
   96    101          else:  # 'stone' or 'soil'
   97    102              want_soil = kind == "soil"
   98    103              m = np.zeros(self.shape, bool)
@@ -270,12 +275,53 @@ class GeneratedApproach:
  270    275                  return True
  271    276          return False
  272    277  
  273        -    def _choose_op(self, state, i, p, at_visit_tasks):
         278 +    # ---------------- visibility models ----------------
         279 +    def _pillars(self):
         280 +        return [(b[0], b[1]) for b in self.sc.obs_boxes if max(b[2], b[3]) < 0.15]
         281 +
         282 +    @staticmethod
         283 +    def _seg_dist(p, a, b):
         284 +        ab = b - a
         285 +        t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-12), 0.0, 1.0)
         286 +        return np.linalg.norm(a + t * ab - p)
         287 +
         288 +    def _visible(self, p, th, k, margin=0.03):
         289 +        c = p + np.array([-0.087 * np.cos(th) + 0.0125 * np.sin(th), -0.087 * np.sin(th) - 0.0125 * np.cos(th)])
         290 +        o = self.sc.opos[k]
         291 +        v = o - c
         292 +        if np.linalg.norm(v) > 1.9972 - margin:
         293 +            return False, np.linalg.norm(v)
         294 +        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
         295 +        if ang < np.radians(108):
         296 +            for pc in self._pillars():
         297 +                if self._seg_dist(np.array(pc), c, o) < 0.11:
         298 +                    return False, np.linalg.norm(v)
         299 +        return True, np.linalg.norm(v)
         300 +
         301 +    def _can_send(self, state, i, p, th):
         302 +        sc = self.sc
         303 +        v = sc.lpos - p
         304 +        d = np.linalg.norm(v)
         305 +        if d > SEND_R:
         306 +            return False
         307 +        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
         308 +        if ang >= np.radians(115):
         309 +            return True
         310 +        g = state.get
         311 +        orv = sc.rovers[1 - i]
         312 +        op = np.array([g(orv, "x"), g(orv, "y")])
         313 +        if self._seg_dist(op, p, sc.lpos) < 0.27:
         314 +            return False
         315 +        for pc in self._pillars():
         316 +            if self._seg_dist(np.array(pc), p, sc.lpos) < 0.13:
         317 +                return False
         318 +        return True
         319 +
         320 +    def _choose_op(self, state, i, p, th):
  274    321          sc = self.sc
  275    322          g = state.get
  276    323          rv = sc.rovers[i]
  277    324          me = "rover%d" % i
  278        -        other = "rover%d" % (1 - i)
  279    325          store_full = g(rv, "store_full") > 0.5
  280    326          calibrated = g(rv, "calibrated") > 0.5
  281    327          # sample
@@ -286,25 +332,27 @@ class GeneratedApproach:
  286    332                      if not self._task_done(state, t):
  287    333                          return "sample"
  288    334          # imaging
  289        -        visible = [k for k in range(len(sc.objectives)) if np.linalg.norm(sc.opos[k] - p) <= IMG_R]
  290        -        need = [k for k in range(len(sc.objectives)) if not self._task_done(state, ("obj", k))]
  291        -        vis_need = [k for k in visible if k in need]
  292        -        if vis_need:
         335 +        nobj = len(sc.objectives)
         336 +        vis = {}
         337 +        for k in range(nobj):
         338 +            ok, d = self._visible(p, th, k)
         339 +            if ok:
         340 +                vis[k] = d
         341 +        need = [k for k in range(nobj) if not self._task_done(state, ("obj", k))]
         342 +        if any(k in vis for k in need):
  293    343              if calibrated:
  294        -                cands = [k for k in visible if g(sc.objectives[k], "have_image_" + me) < 0.5]
         344 +                cands = [k for k in vis if g(sc.objectives[k], "have_image_" + me) < 0.5]
  295    345                  if cands:
  296        -                    return "image"
         346 +                    kbest = min(cands, key=lambda k: vis[k])
         347 +                    if kbest in need:
         348 +                        return "image"
  297    349              else:
  298    350                  return "calibrate"
  299        -        # calibrate early if I still have images to take and something is visible
  300    351          mine_left = [t for t in self.my_tasks[i] if t[0] == "obj" and not self._task_done(state, t)]
  301        -        if not calibrated and mine_left and any(
  302        -                np.linalg.norm(sc.opos[k] - p) <= IMG_R for k in range(len(sc.objectives))):
         352 +        if not calibrated and mine_left and vis:
  303    353              return "calibrate"
  304    354          if store_full:
  305        -            # is my store's analysis already recorded? (store full => yes)
  306    355              return "drop"
  307        -        # send
  308    356          all_done = all(self._task_done(state, t) for t in self.my_tasks[i])
  309    357          holding = False
  310    358          for o in sc.objectives:
@@ -313,59 +361,87 @@ class GeneratedApproach:
  313    361          for s in sc.samples:
  314    362              if g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5:
  315    363                  holding = True
  316        -        if holding and all_done and np.linalg.norm(p - sc.lpos) <= SEND_R:
         364 +        if holding and all_done and self._can_send(state, i, p, th):
  317    365              return "send"
  318    366          return "noop"
  319    367  
         368 +    def _desired_heading(self, state, i, p, k):
         369 +        """Face away from the next objective still to image on my path; else away from lander."""
         370 +        sc = self.sc
         371 +        plan = self.plans[i]
         372 +        visits = plan["visits"]
         373 +        for idx in sorted(visits):
         374 +            if idx < k:
         375 +                continue
         376 +            for t in visits[idx]:
         377 +                if t[0] == "obj" and not self._task_done(state, t):
         378 +                    v = p - sc.opos[t[1]]
         379 +                    return np.arctan2(v[1], v[0])
         380 +        # any of my objectives left (e.g. skipped)
         381 +        for t in self.my_tasks[i]:
         382 +            if t[0] == "obj" and not self._task_done(state, t):
         383 +                v = p - sc.opos[t[1]]
         384 +                return np.arctan2(v[1], v[0])
         385 +        v = p - sc.lpos
         386 +        return np.arctan2(v[1], v[0])
         387 +
  320    388      def _rover_action(self, state, i):
  321    389          sc = self.sc
  322    390          g = state.get
  323    391          rv = sc.rovers[i]
  324    392          cur = np.array([g(rv, "x"), g(rv, "y")])
         393 +        th = g(rv, "theta")
  325    394          plan = self.plans[i]
  326        -        path = plan["path"]
  327    395          P = self.planners[i]
  328    396          k = plan["k"]
  329        -        # verify position
  330        -        exp = P.pos(path[k])
         397 +        exp = P.pos(plan["path"][k])
  331    398          if np.linalg.norm(exp - cur) > 0.02:
  332        -            # previous move blocked or drifted; find closest path index or stay
  333    399              plan["stuck"] += 1
  334        -            if plan["stuck"] > 3:
         400 +            if k > 0 and np.linalg.norm(P.pos(plan["path"][k - 1]) - cur) < 0.02 and plan["stuck"] <= 3:
         401 +                k = k - 1
         402 +                plan["k"] = k
         403 +            else:
  335    404                  self._replan(state, i, cur)
  336    405                  plan = self.plans[i]
  337        -                path = plan["path"]
  338    406                  k = plan["k"]
  339        -            else:
  340        -                # step back on k to retry previous move
  341        -                if k > 0 and np.linalg.norm(P.pos(path[k - 1]) - cur) < 0.02:
  342        -                    k = k - 1
  343        -                    plan["k"] = k
  344        -        # decide whether to stay at current index
         407 +        else:
         408 +            plan["stuck"] = 0
         409 +        path = plan["path"]
  345    410          stay = False
  346    411          vt = plan["visits"].get(k, [])
  347    412          for t in vt:
  348        -            if not self._task_done(state, t) and plan["wait"] < 12:
         413 +            if not self._task_done(state, t) and plan["wait"] < 10:
  349    414                  stay = True
  350    415          if k >= len(path) - 1:
  351    416              stay = True
         417 +            # path finished but my tasks undone -> replan
         418 +            rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
         419 +            if rem and plan["wait"] >= 10:
         420 +                self._replan(state, i, cur, shrink=True)
         421 +                plan = self.plans[i]
         422 +                path = plan["path"]
         423 +                k = plan["k"]
         424 +                stay = len(path) <= 1
  352    425          if stay:
  353    426              plan["wait"] += 1
  354    427              nxt = k
  355    428          else:
  356    429              plan["wait"] = 0
  357    430              nxt = k + 1
  358        -            # don't leave if next index arrival leaves region needed... (handled by visits)
  359    431          target = P.pos(path[nxt])
  360        -        d = target - cur
  361        -        d = np.clip(d, -0.2, 0.2)
         432 +        d = np.clip(target - cur, -0.2, 0.2)
  362    433          newp = cur + d
  363        -        op = self._choose_op(state, i, newp, vt)
         434 +        dth_des = _wrap(self._desired_heading(state, i, newp, nxt) - th)
         435 +        dth = float(np.clip(dth_des, -0.4, 0.4))
         436 +        newth = _wrap(th + dth)
         437 +        op = self._choose_op(state, i, newp, newth)
  364    438          plan["k"] = nxt
  365        -        return np.array([d[0], d[1], 0.0, BAND[op]], dtype=np.float32)
         439 +        return np.array([d[0], d[1], dth, BAND[op]], dtype=np.float32)
  366    440  
  367        -    def _replan(self, state, i, cur):
         441 +    def _replan(self, state, i, cur, shrink=False):
  368    442          P = self.planners[i]
         443 +        if shrink:
         444 +            P.img_r = max(1.6, P.img_r - 0.1)
  369    445          rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
  370    446          start = P.cell(cur)
  371    447          P.free[start] = True
diff --git a/dbg.py b/dbg.py
index 60c15ae..cf19a08 100644
--- a/dbg.py
+++ b/dbg.py
@@ -11,6 +11,7 @@ print("tasks", ap.tasks, "mytasks", ap.my_tasks)
   11     11  for i in range(2): print(i, "visits", ap.plans[i]['visits'], "path", [tuple(np.round(ap.planners[i].pos(c),2)) for c in ap.plans[i]['path']][:40])
   12     12  
   13     13  for step in range(int(sys.argv[2]) if len(sys.argv)>2 else 60):
          14 +    pass
   14     15      a = ap.get_action(obs)
   15     16      obs, r, term, trunc, info = env.step(a)
   16     17      g = obs.get
diff --git a/eval_many.py b/eval_many.py
new file mode 100644
index 0000000..930adab
--- /dev/null
+++ b/eval_many.py
@@ -0,0 +1,25 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from multiprocessing import Pool
           4 +def run(seed):
           5 +    from env_client import make_env
           6 +    from approach import GeneratedApproach
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time(); ap.reset(obs, info); tp = time.time()-t0
          11 +    pl = [len(p['path'])-1 for p in ap.plans]
          12 +    steps=0; term=False
          13 +    while steps < 300:
          14 +        obs, r, term, trunc, info = env.step(ap.get_action(obs)); steps+=1
          15 +        if term or trunc: break
          16 +    env.close()
          17 +    return seed, len(ap.sc.objectives), steps if term else 9999, max(pl), tp
          18 +if __name__ == '__main__':
          19 +    a, b = int(sys.argv[1]), int(sys.argv[2])
          20 +    with Pool(8) as p:
          21 +        res = p.map(run, range(a, b))
          22 +    for r in res:
          23 +        if r[2] == 9999 or r[2] - r[3] > 2: print("seed %d nobj %d steps %d plan %d t %.2f" % r)
          24 +    st = [r[2] for r in res]
          25 +    print("mean", np.mean([s for s in st if s < 9999]), "fails", sum(s == 9999 for s in st), "maxplan", max(r[4] for r in res))
diff --git a/probe_s21.py b/probe_s21.py
new file mode 100644
index 0000000..10b77f3
--- /dev/null
+++ b/probe_s21.py
@@ -0,0 +1,6 @@
           1 +from env_client import make_env
           2 +env = make_env()
           3 +obs, info = env.reset(seed=21)
           4 +T = {t.name:t for t in env.observation_space.types}
           5 +for t in ['sample','objective','lander']:
           6 +    for o in obs.get_objects(T[t]): print(o.name, [round(obs.get(o,f),3) for f in ['x','y']], obs.get(o,'is_soil') if t=='sample' else '')
diff --git a/probe_send_0.py b/probe_send_0.py
new file mode 100644
index 0000000..fe91dc2
--- /dev/null
+++ b/probe_send_0.py
@@ -0,0 +1,3 @@
           1 +from probe_ops_lib import *
           2 +reset(21)
           3 +for t in ['sample','lander','obstacle','rover','objective']: print(t, dump(t))
diff --git a/probe_send_1.py b/probe_send_1.py
new file mode 100644
index 0000000..9e73c21
--- /dev/null
+++ b/probe_send_1.py
@@ -0,0 +1,12 @@
           1 +from probe_ops_lib import *
           2 +import sys
           3 +reset(21)
           4 +print(goto(0,0.62,-0.92+0.1))
           5 +step(0,op='sample'); print('after sample', dump('sample')['sample3'], pos(0))
           6 +cands=[(1.0,-1.75),(0.62,-0.82),(0.3,-1.75),(0.3,-2.25),(0.3,-1.0),(0.3,0.0),(0.3,1.0),(1.5,-1.0)]
           7 +for c in cands:
           8 +    ok=goto(0,*c)
           9 +    for th in [None]:
          10 +        step(0,op='send')
          11 +    print(c, ok, [round(v,2) for v in pos(0)], 'recv', dump('sample')['sample3'][-1], S.info if S.n<3 else '')
          12 +    if dump('sample')['sample3'][-1]>0: break
diff --git a/probe_send_10.py b/probe_send_10.py
new file mode 100644
index 0000000..9da6891
--- /dev/null
+++ b/probe_send_10.py
@@ -0,0 +1,8 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
           3 +X=0.5; base=L+d*((X-L[0])/d[0])
           4 +for th in [0.0, math.pi/2]:
           5 +    def setup(): goto(1,-1.0,0.3); turn_to(0,th)
           6 +    for sgn in [1,-1]:
           7 +        pts=[tuple(base+n*s*sgn) for s in np.arange(0.0,0.3,0.003)]
           8 +        r=scan(P,pts,setup); print(th,sgn,r,'theta',round(pos(0)[2],2))
diff --git a/probe_send_11.py b/probe_send_11.py
new file mode 100644
index 0000000..d9df962
--- /dev/null
+++ b/probe_send_11.py
@@ -0,0 +1,7 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L)
           3 +X=0.5; base=L+d*((X-L[0])/d[0])
           4 +for th in [math.pi, -math.pi/2, math.pi*0.75, 0.0, math.pi/4]:
           5 +    reset(21); goto(0,0.62,-0.82); step(0,op='sample'); goto(1,-1.0,0.3)
           6 +    goto(0,*base,tol=0.001); turn_to(0,th); step(0,op='send')
           7 +    print(round(th,2), 'r0',np.round(pos(0),3),'r1',np.round(pos(1)[:2],3),'recv',dump('sample')['sample3'][-1])
diff --git a/probe_send_12.py b/probe_send_12.py
new file mode 100644
index 0000000..35b556f
--- /dev/null
+++ b/probe_send_12.py
@@ -0,0 +1,17 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +import sys
           3 +P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
           4 +X=float(sys.argv[1]) if len(sys.argv)>1 else 0.5
           5 +base=L+d*((X-L[0])/d[0])
           6 +S_=np.round(np.arange(-0.16,0.161,0.02),3)
           7 +for k in range(8):
           8 +    th=-math.pi+k*math.pi/4
           9 +    rem=list(S_); row={}
          10 +    while rem:
          11 +        reset(21); goto(0,0.62,-0.82); step(0,op='sample'); goto(1,-1.0,0.3); turn_to(0,th)
          12 +        while rem:
          13 +            s=rem.pop(0); goto(0,*(base+n*s),tol=0.001); step(0,op='send')
          14 +            ok=dump('sample')['sample3'][-1]>0; row[s]='o' if ok else 'X'
          15 +            if ok: break
          16 +    print(f'{th:6.2f}', ''.join(row[s] for s in S_))
          17 +print('s:',S_[0],'..',S_[-1])
diff --git a/probe_send_13.py b/probe_send_13.py
new file mode 100644
index 0000000..b426f66
--- /dev/null
+++ b/probe_send_13.py
@@ -0,0 +1,15 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +R1=np.array([-1.0,-1.75]); d=(R1-L)/np.linalg.norm(R1-L); n=np.array([-d[1],d[0]])
           3 +X=1.0; base=L+d*((X-L[0])/d[0])
           4 +S_=np.round(np.arange(-0.3,0.301,0.03),3)
           5 +for k in range(8):
           6 +    th=-math.pi+k*math.pi/4
           7 +    rem=list(S_); row={}
           8 +    while rem:
           9 +        reset(21); goto(0,0.62,-0.82); step(0,op='sample'); turn_to(0,th)
          10 +        while rem:
          11 +            s=rem.pop(0); goto(0,*(base+n*s),tol=0.001); step(0,op='send')
          12 +            ok=dump('sample')['sample3'][-1]>0; row[s]='o' if ok else 'X'
          13 +            if ok: break
          14 +    print(f'{th:6.2f}', ''.join(row[s] for s in S_))
          15 +print('s:',S_[0],'..',S_[-1], 'base',base)
diff --git a/probe_send_14.py b/probe_send_14.py
new file mode 100644
index 0000000..9288b96
--- /dev/null
+++ b/probe_send_14.py
@@ -0,0 +1,9 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +def one(p, th, r1=None):
           3 +    reset(21); goto(0,0.62,-0.82); step(0,op='sample')
           4 +    if r1: goto(1,*r1)
           5 +    turn_to(0,th); goto(0,*p,tol=0.002); step(0,op='send')
           6 +    q=pos(0); dl=math.hypot(q[0]+1.9,q[1]+2.0); rel=(math.degrees(q[2]-math.atan2(-2-q[1],-1.9-q[0]))+180)%360-180
           7 +    print(np.round(q[:3],3),'dist',round(dl,3),'rel',round(rel),'recv',dump('sample')['sample3'][-1])
           8 +for th in [0.0, math.pi, math.pi/2]:
           9 +    one((1.0,-1.75),th); one((0.3,1.0),th); one((0.3,0.0),th); one((2.08,-1.5),th,(-1,-1)); one((1.5,1.2),th)
diff --git a/probe_send_15.py b/probe_send_15.py
new file mode 100644
index 0000000..aaf2973
--- /dev/null
+++ b/probe_send_15.py
@@ -0,0 +1,5 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +for sd in range(30):
           3 +    reset(sd); s=dump('sample'); 
           4 +    c=[(k,v[:2]) for k,v in s.items() if v[0]<-0.4]
           5 +    if c: print(sd,c, {k:v[:2] for k,v in dump('obstacle').items() if v[3]<0.1}); 
diff --git a/probe_send_16.py b/probe_send_16.py
new file mode 100644
index 0000000..d32df89
--- /dev/null
+++ b/probe_send_16.py
@@ -0,0 +1,15 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +P=np.array([-1.81,-1.55]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
           3 +S_=np.round(np.arange(-0.3,0.301,0.03),3)
           4 +for Y in [-0.5,0.5]:
           5 +  t=(Y-L[1])/d[1]; base=L+d*t
           6 +  for th in [-math.pi/2, math.pi/2, 0.0]:
           7 +    rem=list(S_); row={}
           8 +    while rem:
           9 +        reset(0); goto(1,-1.39,0.15+0.1); step(1,op='sample'); assert dump('sample')['sample3'][5]==1
          10 +        turn_to(1,th)
          11 +        while rem:
          12 +            s=rem.pop(0); goto(1,*(base+n*s),tol=0.002); step(1,op='send')
          13 +            ok=dump('sample')['sample3'][-1]>0; row[s]='o' if ok else 'X'
          14 +            if ok: break
          15 +    print(Y, f'{th:6.2f}', ''.join(row[s] for s in S_), np.round(base,2))
diff --git a/probe_send_17.py b/probe_send_17.py
new file mode 100644
index 0000000..2fc9425
--- /dev/null
+++ b/probe_send_17.py
@@ -0,0 +1,14 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +def one(p, mode, r1=None):
           3 +    reset(21); goto(0,0.62,-0.82); step(0,op='sample')
           4 +    if r1: goto(1,*r1)
           5 +    goto(0,*p,tol=0.002); q=pos(0); a=math.atan2(q[1]+2,q[0]+1.9)
           6 +    turn_to(0, a if mode=='away' else a+math.pi); step(0,op='send')
           7 +    q=pos(0); print(mode,np.round(q[:3],3),'dist',round(math.hypot(q[0]+1.9,q[1]+2.0),3),'recv',dump('sample')['sample3'][-1])
           8 +for mode in ['away','toward']:
           9 +    one((1.3,-0.176),mode)          # behind obstacle5 at 0.47
          10 +    one((1.08,-0.29),mode)          # behind obstacle5 at 0.22 
          11 +    one((0.26,-0.84),mode,(-1,0.3)) # behind obstacle10
          12 +    one((1.0,-1.194),mode)          # rover1 dead centre
          13 +    one((0.4,-1.36),mode)           # rover1 dead centre closer (0.58 from r1)
          14 +    one((2.05,-1.45),mode,(-1,0.3)) # dist ~4.0
diff --git a/probe_send_2.py b/probe_send_2.py
new file mode 100644
index 0000000..dcf993a
--- /dev/null
+++ b/probe_send_2.py
@@ -0,0 +1,7 @@
           1 +from probe_send_lib import *
           2 +import time
           3 +t=time.time()
           4 +# move along x=0.3 downward from -1.75 to -2.25 in steps
           5 +print(test([(0.3,y) for y in [-1.8,-1.85,-1.9,-1.95,-2.0,-2.05,-2.1,-2.15,-2.2,-2.25]]))
           6 +print(time.time()-t)
           7 +print(test([(x,-2.25) for x in [2.0,1.8,1.6,1.4,1.2,1.0,0.8,0.6,0.4,0.3]]))
diff --git a/probe_send_3.py b/probe_send_3.py
new file mode 100644
index 0000000..88763cd
--- /dev/null
+++ b/probe_send_3.py
@@ -0,0 +1,8 @@
           1 +from probe_send_lib import *
           2 +import numpy as np
           3 +for x in [0.25,0.5,1.0,1.5]:
           4 +    r=test([(x,y) for y in np.arange(-1.6,-2.45,-0.01)])
           5 +    print(x, r[-2:])
           6 +for y in [-2.25,-2.4,-2.1]:
           7 +    r=test([(x,y) for x in np.arange(2.3,0.5,-0.01)])
           8 +    print(y, r[-2:])
diff --git a/probe_send_4.py b/probe_send_4.py
new file mode 100644
index 0000000..f826c67
--- /dev/null
+++ b/probe_send_4.py
@@ -0,0 +1,16 @@
           1 +from probe_send_lib import *
           2 +import numpy as np, probe_ops_lib as L
           3 +def scan(x,y0,y1,dy=-0.004):
           4 +    reset(21); goto(0,0.62,-0.82); step(0,op='sample')
           5 +    goto(0,x,y0+0.05)
           6 +    prev=None
           7 +    for y in np.arange(y0,y1,dy):
           8 +        goto(0,x,y,tol=0.001)
           9 +        step(0,op='send')
          10 +        if dump('sample')['sample3'][-1]>0:
          11 +            p=pos(0)[:2]; 
          12 +            yc=p[1]+(-2-p[1])*p[0]/(p[0]+1.9)
          13 +            return prev, [round(v,4) for v in p], 'cross0', round(yc,4)
          14 +        prev=[round(v,4) for v in pos(0)[:2]]
          15 +for x in [0.24,0.4,0.7,1.2,1.8,2.0]:
          16 +    print(x, scan(x,-1.6,-2.2))
diff --git a/probe_send_5.py b/probe_send_5.py
new file mode 100644
index 0000000..25bc57f
--- /dev/null
+++ b/probe_send_5.py
@@ -0,0 +1,9 @@
           1 +from probe_send_lib import *
           2 +reset(21)
           3 +def straight(tx,ty,n=40):
           4 +    for _ in range(n):
           5 +        x,y=pos(0)[:2]; dx=max(-.2,min(.2,tx-x)); dy=max(-.2,min(.2,ty-y))
           6 +        if abs(dx)+abs(dy)<1e-4: break
           7 +        step(0,dx,dy)
           8 +for y in [-2.6,-2.45,-2.3,-2.1,-1.95,-1.8,0,2.5]:
           9 +    straight(0.5,y); a=[round(v,3) for v in pos(0)[:2]]; straight(-0.5,y,10); print(y,a,[round(v,3) for v in pos(0)[:2]])
diff --git a/probe_send_6.py b/probe_send_6.py
new file mode 100644
index 0000000..e75639e
--- /dev/null
+++ b/probe_send_6.py
@@ -0,0 +1,5 @@
           1 +from probe_send_lib import *
           2 +reset(21)
           3 +goto(0,0.62,-0.82); step(0,op='sample')
           4 +goto(0,1.0,-1.75); step(0,op='send'); print('r1 home', dump('sample')['sample3'][-1])
           5 +goto(1,-1.0,-1.0); print(pos(1)[:2]); goto(0,1.0,-1.75); step(0,op='send'); print('r1 moved', dump('sample')['sample3'][-1])
diff --git a/probe_send_7.py b/probe_send_7.py
new file mode 100644
index 0000000..6fe6802
--- /dev/null
+++ b/probe_send_7.py
@@ -0,0 +1,31 @@
           1 +from probe_send_lib import *
           2 +import numpy as np
           3 +L=np.array([-1.9,-2.0])
           4 +def segd(p,a,b):
           5 +    a,b,p=map(np.array,(a,b,p)); t=np.clip(np.dot(p-a,b-a)/np.dot(b-a,b-a),0,1); return float(np.linalg.norm(a+t*(b-a)-p))
           6 +def scan(blk, pts, setup=None):
           7 +    reset(21); goto(0,0.62,-0.82); step(0,op='sample')
           8 +    if setup: setup()
           9 +    goto(0,*pts[0]); prev=None
          10 +    for p in pts:
          11 +        goto(0,*p,tol=0.001); step(0,op='send')
          12 +        q=pos(0)[:2]
          13 +        if dump('sample')['sample3'][-1]>0:
          14 +            return prev, round(segd(blk,q,L),4)
          15 +        prev=round(segd(blk,q,L),4)
          16 +    return 'nosuccess',prev
          17 +# rover1 blocker at home, scan rover0 at x=1.0 and x=0.4 and x=2.0 downward
          18 +r1=(-1.0,-1.75)
          19 +for x in [0.4,1.0,1.6]:
          20 +    print('rover1', x, scan(r1,[(x,y) for y in np.arange(-1.6,-2.1,-0.003)]))
          21 +# rover1 rotated 90deg
          22 +def rot(): 
          23 +    for _ in range(4): step(1,dth=0.4)
          24 +    print(' r1 theta', pos(1)[2])
          25 +print('rover1 rot', scan(r1,[(1.0,y) for y in np.arange(-1.6,-2.1,-0.003)],rot))
          26 +# pillar obstacle10 (-0.47,-1.23): rover1 moved away
          27 +P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
          28 +def away(): goto(1,-1.0,0.3)
          29 +base=L+d*((0.6-L[0])/d[0])
          30 +print('pillar', scan(P,[tuple(base+n*s) for s in np.arange(0.4,-0.4,-0.004)],away))
          31 +print('pillar rev', scan(P,[tuple(base+n*s) for s in np.arange(-0.4,0.4,0.004)],away))
diff --git a/probe_send_8.py b/probe_send_8.py
new file mode 100644
index 0000000..8c55c7d
--- /dev/null
+++ b/probe_send_8.py
@@ -0,0 +1,14 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
           3 +def away(): goto(1,-1.0,0.3)
           4 +for X in [0.4,0.6]:
           5 +    base=L+d*((X-L[0])/d[0])
           6 +    for sgn in [1,-1]:
           7 +        pts=[tuple(base+n*s*sgn) for s in np.arange(0.0,0.4,0.004)]
           8 +        print(X,sgn,'start',np.round(pts[0],3),scan(P,pts,away), np.round(pos(0)[:2],3))
           9 +# also pillar obstacle9 (-1.24,-0.79) and obstacle11 (-1.49,-1.03)
          10 +for P in [np.array([-1.24,-0.79]),np.array([-1.49,-1.03])]:
          11 +    d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
          12 +    base=L+d*((0.5-L[0])/d[0])
          13 +    pts=[tuple(base+n*s) for s in np.arange(0.0,0.4,0.004)]
          14 +    print(P,'start',np.round(pts[0],3),scan(P,pts,away), np.round(pos(0)[:2],3))
diff --git a/probe_send_9.py b/probe_send_9.py
new file mode 100644
index 0000000..4bb49a9
--- /dev/null
+++ b/probe_send_9.py
@@ -0,0 +1,11 @@
           1 +exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
           2 +import math
           3 +L=np.array([-1.9,-2.0])
           4 +for yy in [-2.1,-2.3,-1.5]:
           5 +    if yy==-1.5:
           6 +        pts=[(x,yy) for x in np.arange(2.2,1.6,-0.003)]
           7 +        r=scan((0,0),pts,lambda: goto(1,-1.0,-1.0))
           8 +    else:
           9 +        pts=[(x,yy) for x in np.arange(2.2,1.8,-0.003)]
          10 +        r=scan((0,0),pts)
          11 +    q=pos(0)[:2]; print(yy, np.round(q,4), 'dist', round(math.hypot(q[0]-L[0],q[1]-L[1]),4))
diff --git a/probe_send_lib.py b/probe_send_lib.py
new file mode 100644
index 0000000..d0ea78a
--- /dev/null
+++ b/probe_send_lib.py
@@ -0,0 +1,17 @@
           1 +from probe_ops_lib import *
           2 +import time
           3 +def test(pts, via=None):
           4 +    """one episode: sample sample3, visit pts in order trying send; return index of first success or None"""
           5 +    reset(21)
           6 +    goto(0,0.62,-0.82); step(0,op='sample')
           7 +    assert dump('sample')['sample3'][4]==1
           8 +    res=[]
           9 +    for p in pts:
          10 +        if via: goto(0,*via(p))
          11 +        ok=goto(0,*p)
          12 +        step(0,op='send')
          13 +        x,y=pos(0)[:2]
          14 +        r=dump('sample')['sample3'][-1]
          15 +        res.append(((round(x,2),round(y,2)),ok,r))
          16 +        if r>0: break
          17 +    return res
diff --git a/probe_vis_1.py b/probe_vis_1.py
new file mode 100644
index 0000000..3efe351
--- /dev/null
+++ b/probe_vis_1.py
@@ -0,0 +1,8 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L
           3 +t=time.time()
           4 +for th in [0,np.pi/2,np.pi,-np.pi/2]:
           5 +  for p in [(-1.5,0.25),(-1.57,0.31)]:
           6 +    reset(2); goto([(-1.0,p[1]),p]); q=turn(th); c=cal()
           7 +    print(p,th,L.pos().round(4),c)
           8 +print(time.time()-t)
diff --git a/probe_vis_10.py b/probe_vis_10.py
new file mode 100644
index 0000000..3ec66fe
--- /dev/null
+++ b/probe_vis_10.py
@@ -0,0 +1,9 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +L.RV=sys.argv[1]; seed=int(sys.argv[2]); name=sys.argv[3]; ang=float(sys.argv[4]); via=eval(sys.argv[5]); ths=eval(sys.argv[6])
           4 +lo=float(sys.argv[7]) if len(sys.argv)>7 else 1.3
           5 +for thd in ths:
           6 +    th=np.deg2rad(thd); b=bis(seed,name,np.deg2rad(ang),th,lo=lo,via=via)
           7 +    if b and not isinstance(b[0],str):
           8 +        reset(seed); o=objpos(name); print(thd,b,'camdist',round(model(b[2],th,o),4))
           9 +    else: print(thd,b)
diff --git a/probe_vis_11.py b/probe_vis_11.py
new file mode 100644
index 0000000..44f9486
--- /dev/null
+++ b/probe_vis_11.py
@@ -0,0 +1,22 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys, json
           3 +L.RV='rover0'
           4 +seed=2; name='objective0'; pill=np.array([0.735,0.444])
           5 +thd=float(sys.argv[1]); rs=np.arange(float(sys.argv[2]),float(sys.argv[3])+1e-9,float(sys.argv[4])); ss=np.arange(-0.15,0.15+1e-9,0.01)
           6 +reset(seed); o=objpos(name)[:2]
           7 +u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
           8 +goto([(1.0,-1.75),(0.9,-1.75)]); turn(np.deg2rad(thd))
           9 +rows=[]; data=[]
          10 +for i,r in enumerate(rs[::-1]):
          11 +    line=''
          12 +    for s in (ss if i%2==0 else ss[::-1]):
          13 +        p=o+r*u+s*n; q=goto([tuple(p)])
          14 +        if np.linalg.norm(q[:2]-p)>1e-4: ch='X'
          15 +        else:
          16 +            c=cal(); ch=str(int(c))
          17 +            if c>0.5: step(op=-1/6)
          18 +            data.append((float(q[0]),float(q[1]),float(q[2]),int(c)))
          19 +        line+=ch
          20 +    rows.append((r,line if i%2==0 else line[::-1]))
          21 +for r,l in rows: print(f"{r:.3f} {l}")
          22 +json.dump(data,open(f'probe_vis_data_r0_{int(thd)}.json','w'))
diff --git a/probe_vis_12.py b/probe_vis_12.py
new file mode 100644
index 0000000..ee15b2e
--- /dev/null
+++ b/probe_vis_12.py
@@ -0,0 +1,17 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +L.RV='rover0'
           4 +seed=2; name='objective0'; pill=np.array([0.735,0.444])
           5 +r=float(sys.argv[1]); s=float(sys.argv[2]); ths=eval(sys.argv[3])
           6 +reset(seed); o=objpos(name)[:2]
           7 +u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
           8 +p=o+r*u+s*n; q=goto([(1.0,-1.75),(p[0],-1.75),tuple(p)])
           9 +brg=np.degrees(np.arctan2(*(o-q[:2])[::-1]))
          10 +print('at',q.round(4),'bearing',round(brg,2))
          11 +out=[]
          12 +for thd in ths:
          13 +    turn(np.deg2rad(thd)); c=cal()
          14 +    if c>0.5: step(op=-1/6)
          15 +    rel=(brg-thd+180)%360-180
          16 +    out.append(f"{thd}({rel:.0f}):{int(c)}")
          17 +print(' '.join(out))
diff --git a/probe_vis_13.py b/probe_vis_13.py
new file mode 100644
index 0000000..927511b
--- /dev/null
+++ b/probe_vis_13.py
@@ -0,0 +1,21 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys, json
           3 +L.RV='rover0'
           4 +seed=2; name='objective0'; pill=np.array([0.735,0.444])
           5 +r=float(sys.argv[1]); ths=eval(sys.argv[2]); ss=np.arange(-0.4,0.4001,0.01)
           6 +reset(seed); o=objpos(name)[:2]
           7 +u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
           8 +p=o+r*u+ss[0]*n; goto([(1.0,-1.75),(p[0],-1.75),tuple(p)])
           9 +data=[]
          10 +for k,thd in enumerate(ths):
          11 +    turn(np.deg2rad(thd)); line=''
          12 +    seq=ss if k%2==0 else ss[::-1]
          13 +    for s in seq:
          14 +        p=o+r*u+s*n; q=goto([tuple(p)])
          15 +        if np.linalg.norm(q[:2]-p)>1e-4: line+='X'; continue
          16 +        c=cal(); line+=str(int(c))
          17 +        if c>0.5: step(op=-1/6)
          18 +        data.append((float(q[0]),float(q[1]),float(q[2]),int(c)))
          19 +    if k%2: line=line[::-1]
          20 +    print(f"{thd:5d} {line}",flush=True)
          21 +json.dump(data,open(f'probe_vis_data_row_{r}.json','w'))
diff --git a/probe_vis_14.py b/probe_vis_14.py
new file mode 100644
index 0000000..7f01d03
--- /dev/null
+++ b/probe_vis_14.py
@@ -0,0 +1,18 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +L.RV=sys.argv[1]; seed=int(sys.argv[2]); name=sys.argv[3]; pill=np.array(eval(sys.argv[4])); r=float(sys.argv[5]); ths=eval(sys.argv[6]); via=eval(sys.argv[7])
           4 +lat=float(sys.argv[8]) if len(sys.argv)>8 else 0.0
           5 +reset(seed); o=objpos(name)[:2]
           6 +u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
           7 +ct=o+r*u+lat*n; goto(via)
           8 +ox,oy=-0.087,-0.0125; out=[]
           9 +brg=np.degrees(np.arctan2(*(o-ct)[::-1]))
          10 +for thd in ths:
          11 +    th=np.deg2rad(thd)
          12 +    b=ct-np.array([ox*np.cos(th)-oy*np.sin(th), ox*np.sin(th)+oy*np.cos(th)])
          13 +    turn(th); q=goto([tuple(b)])
          14 +    if np.linalg.norm(q[:2]-b)>1e-4: out.append(f"{thd}:X"); continue
          15 +    c=cal()
          16 +    if c>0.5: step(op=-1/6)
          17 +    out.append(f"{thd}({(brg-thd+180)%360-180:.0f}):{int(c)}")
          18 +print('bearing',round(brg,1)); print(' '.join(out))
diff --git a/probe_vis_15.py b/probe_vis_15.py
new file mode 100644
index 0000000..414c026
--- /dev/null
+++ b/probe_vis_15.py
@@ -0,0 +1,17 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +L.RV=sys.argv[1]; seed=int(sys.argv[2]); name=sys.argv[3]; pill=np.array(eval(sys.argv[4])); rs=eval(sys.argv[5]); threl=float(sys.argv[6]); via=eval(sys.argv[7]); lats=eval(sys.argv[8])
           4 +reset(seed); o=objpos(name)[:2]
           5 +u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
           6 +goto(via); ox,oy=-0.087,-0.0125
           7 +th=np.arctan2(-u[1],-u[0])-np.deg2rad(threl); turn(th); th=pos()[2]
           8 +for r in rs:
           9 +    line=''
          10 +    for lat in lats:
          11 +        ct=o+r*u+lat*n
          12 +        b=ct-np.array([ox*np.cos(th)-oy*np.sin(th), ox*np.sin(th)+oy*np.cos(th)])
          13 +        q=goto([tuple(b)])
          14 +        if np.linalg.norm(q[:2]-b)>1e-4: line+='X'; continue
          15 +        c=cal(); line+=str(int(c))
          16 +        if c>0.5: step(op=-1/6)
          17 +    print(r,line,flush=True)
diff --git a/probe_vis_16.py b/probe_vis_16.py
new file mode 100644
index 0000000..7339282
--- /dev/null
+++ b/probe_vis_16.py
@@ -0,0 +1,35 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +L.RV=sys.argv[1]; seed=int(sys.argv[2]); N=int(sys.argv[3])
           4 +rng=np.random.default_rng(seed*7+len(L.RV))
           5 +reset(seed)
           6 +objs=[objpos(o.name) for o in L.obs.get_objects(L.T['objective'])]
           7 +pills=[np.array([L.obs.get(b,'x'),L.obs.get(b,'y')]) for b in L.obs.get_objects(L.T['obstacle']) if L.obs.get(b,'half_x')<0.1]
           8 +def segdist(a,b,p):
           9 +    d=b-a; t=np.clip(np.dot(p-a,d)/np.dot(d,d),0,1); return np.linalg.norm(a+t*d-p)
          10 +def pred(b,th):
          11 +    c=b+np.array([-0.087*np.cos(th)+0.0125*np.sin(th), -0.087*np.sin(th)-0.0125*np.cos(th)])
          12 +    res=[]
          13 +    for o in objs:
          14 +        dist=np.linalg.norm(o[:2]-c)
          15 +        rel=abs((np.degrees(np.arctan2(o[1]-c[1],o[0]-c[0])-th)+180)%360-180)
          16 +        clr=min(segdist(c,o[:2],p) for p in pills)
          17 +        if dist>2.007 or (rel<=95 and clr<0.05): v=0
          18 +        elif dist<1.987 and (rel>=100 or clr>=0.09): v=1
          19 +        else: v=None
          20 +        res.append(v)
          21 +    return res
          22 +sx=1 if L.RV=='rover0' else -1
          23 +goto([(sx*1.0,-1.0)])
          24 +stats={'ok':0,'bad':0,'amb':0}
          25 +for i in range(N):
          26 +    tgt=np.array([sx*rng.uniform(0.3,2.3), rng.uniform(-0.5,1.6)])
          27 +    goto([tuple(tgt)]); turn(rng.uniform(-np.pi,np.pi)); p=pos()
          28 +    pr=pred(p[:2],p[2]); c=cal()
          29 +    if c>0.5: step(op=-1/6)
          30 +    if any(v==1 for v in pr): exp=1
          31 +    elif all(v==0 for v in pr): exp=0
          32 +    else: stats['amb']+=1; continue
          33 +    if exp==int(c): stats['ok']+=1
          34 +    else: stats['bad']+=1; print('MISMATCH',p.round(3),pr,int(c))
          35 +print(stats)
diff --git a/probe_vis_2.py b/probe_vis_2.py
new file mode 100644
index 0000000..aece0eb
--- /dev/null
+++ b/probe_vis_2.py
@@ -0,0 +1,9 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L
           3 +objs=None
           4 +for p in [(-1.5,0.25),(-1.57,0.31)]:
           5 +    reset(2); objs=L.obs.get_objects(L.T['objective'])
           6 +    goto([(-1.0,p[1]),p])
           7 +    for k in range(3):
           8 +        c=cal(); step(op=-1/6)
           9 +        print(p,k,'cal',c,[int(L.obs.get(o,'have_image_rover1')) for o in objs],'cal after',L.obs.get(L.r1,'calibrated'))
diff --git a/probe_vis_3.py b/probe_vis_3.py
new file mode 100644
index 0000000..6f52fd5
--- /dev/null
+++ b/probe_vis_3.py
@@ -0,0 +1,5 @@
           1 +from probe_vis_lib import *
           2 +import time
           3 +t=time.time()
           4 +print(scan(2,'objective2',-np.pi/2,2.1,1.8,0.01,via=[(-0.492,-1.75)]))
           5 +print(time.time()-t)
diff --git a/probe_vis_4.py b/probe_vis_4.py
new file mode 100644
index 0000000..4b244f1
--- /dev/null
+++ b/probe_vis_4.py
@@ -0,0 +1,8 @@
           1 +from probe_vis_lib import *
           2 +import sys
           3 +ang=float(sys.argv[1])*np.pi/180
           4 +for thd in range(0,360,45):
           5 +    th=np.deg2rad(thd); th=(th+np.pi)%(2*np.pi)-np.pi
           6 +    a=scan(2,'objective2',ang,2.3,1.5,0.01,th=th,via=[(-0.492,-1.75)])
           7 +    b=scan(2,'objective2',ang,a[0]+0.01,a[0]-0.001,0.0005,th=th,via=[(-0.492,-1.75)]) if a and a[0]!='unreach' else None
           8 +    print('th',thd,a,b)
diff --git a/probe_vis_5.py b/probe_vis_5.py
new file mode 100644
index 0000000..115a830
--- /dev/null
+++ b/probe_vis_5.py
@@ -0,0 +1,11 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +seed=int(sys.argv[1]); L.RV=sys.argv[2]; name=sys.argv[3]; ang=float(sys.argv[4])
           4 +via=eval(sys.argv[5]) if len(sys.argv)>5 else None
           5 +for thd in [0,90,180,-90]:
           6 +    th=np.deg2rad(thd)
           7 +    b=bis(seed,name,np.deg2rad(ang),th,via=via)
           8 +    if b and not isinstance(b[0],str):
           9 +        reset(seed); o=objpos(name)
          10 +        print(thd,b,'model',round(model(b[2],th,o),4))
          11 +    else: print(thd,b)
diff --git a/probe_vis_6.py b/probe_vis_6.py
new file mode 100644
index 0000000..3c18e54
--- /dev/null
+++ b/probe_vis_6.py
@@ -0,0 +1,15 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +seed=2; name='objective2'
           4 +R=float(sys.argv[1]); a0=float(sys.argv[2]); a1=float(sys.argv[3]); da=float(sys.argv[4]); thd=float(sys.argv[5])
           5 +reset(seed); c=objpos(name)[:2]
           6 +P=lambda a: tuple(c+R*np.array([np.cos(np.deg2rad(a)),np.sin(np.deg2rad(a))]))
           7 +s=P(a0); goto([(-1.0,-1.75),(-1.0,s[1]),s]); turn(np.deg2rad(thd))
           8 +cal(); step(op=-1/6); print('pre',imaged())
           9 +n=int(round(abs(a1-a0)/da))+1
          10 +for i in range(n):
          11 +    a=a0+(a1-a0)*i/(n-1); q=goto([P(a)])
          12 +    cal(); step(op=-1/6)
          13 +    if name in imaged():
          14 +        print('visible at ang',a,q.round(4)); break
          15 +else: print('never')
diff --git a/probe_vis_7.py b/probe_vis_7.py
new file mode 100644
index 0000000..d510b9f
--- /dev/null
+++ b/probe_vis_7.py
@@ -0,0 +1,8 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +seed=int(sys.argv[1]); p=eval(sys.argv[2]); thd=float(sys.argv[3]); via=eval(sys.argv[4]) if len(sys.argv)>4 else [(-1.0,-1.75),(-1.0,p[1])]
           4 +reset(seed); q=goto(via+[p]); turn(np.deg2rad(thd)); q=pos()
           5 +out=[]
           6 +for k in range(3):
           7 +    c=cal(); step(op=-1/6); out.append((c,imaged()))
           8 +print(p,thd,q.round(4),out)
diff --git a/probe_vis_8.py b/probe_vis_8.py
new file mode 100644
index 0000000..9f0126b
--- /dev/null
+++ b/probe_vis_8.py
@@ -0,0 +1,16 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +L.RV='rover0'
           4 +seed=2; name='objective0'; pill=np.array([0.735,0.444])
           5 +reset(seed); o=objpos(name)[:2]
           6 +r=float(sys.argv[1]); thd=float(sys.argv[2]); s0,s1,ds=map(float,sys.argv[3:6])
           7 +u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
           8 +goto([(1.0,-1.75),(0.9,-1.75)]); turn(np.deg2rad(thd))
           9 +res=[]
          10 +for s in np.arange(s0,s1+1e-9,ds):
          11 +    p=o+r*u+s*n; q=goto([tuple(p)])
          12 +    if np.linalg.norm(q[:2]-p)>1e-4: res.append((round(s,3),'X')); continue
          13 +    c=cal()
          14 +    if c>0.5: step(op=-1/6)
          15 +    res.append((round(s,3),int(c)))
          16 +print(r,thd,' '.join(f"{a}:{b}" for a,b in res))
diff --git a/probe_vis_9.py b/probe_vis_9.py
new file mode 100644
index 0000000..c4f91a5
--- /dev/null
+++ b/probe_vis_9.py
@@ -0,0 +1,12 @@
           1 +from probe_vis_lib import *
           2 +import probe_vis_lib as L, sys
           3 +L.RV=sys.argv[1]; seed=int(sys.argv[2]); p=eval(sys.argv[3]); via=eval(sys.argv[4]); dth=float(sys.argv[5]) if len(sys.argv)>5 else 15
           4 +reset(seed); q=goto(via+[p]); print('at',q.round(4))
           5 +res=[]
           6 +for thd in np.arange(-180,180,dth):
           7 +    turn(np.deg2rad(thd)); c=cal()
           8 +    got=''
           9 +    if c>0.5:
          10 +        before=set(imaged()); step(op=-1/6); got=','.join(n[-1] for n in set(imaged())-before) or '='
          11 +    res.append(f"{int(thd)}:{int(c)}{got}")
          12 +print(' '.join(res))
diff --git a/probe_vis_data_r0_-90.json b/probe_vis_data_r0_-90.json
new file mode 100644
index 0000000..b0aa754
--- /dev/null
+++ b/probe_vis_data_r0_-90.json
@@ -0,0 +1 @@
           1 +[[0.7052074670791626, -0.1425783336162567, -1.570796251296997, 1], [0.7149929404258728, -0.14051814377307892, -1.570796251296997, 1], [0.724778413772583, -0.13845795392990112, -1.570796251296997, 1], [0.7345638871192932, -0.13639776408672333, -1.570796251296997, 1], [0.7443493604660034, -0.13433755934238434, -1.570796251296997, 1], [0.7541348338127136, -0.13227736949920654, -1.570796251296997, 1], [0.7639203667640686, -0.13021717965602875, -1.570796251296997, 1], [0.773705780506134, -0.12815697491168976, -1.570796251296997, 1], [0.783491313457489, -0.12609678506851196, -1.570796251296997, 1], [0.7932767271995544, -0.12403658777475357, -1.570796251296997, 1], [0.8030622601509094, -0.12197639048099518, -1.570796251296997, 1], [0.8128477334976196, -0.11991620063781738, -1.570796251296997, 1], [0.8226331472396851, -0.11785600334405899, -1.570796251296997, 1], [0.83241868019104, -0.1157958135008812, -1.570796251296997, 1], [0.8422041535377502, -0.1137356087565422, -1.570796251296997, 1], [0.8519896864891052, -0.11167542636394501, -1.570796251296997, 1], [0.8617751002311707, -0.10961522161960602, -1.570796251296997, 1], [0.8715605735778809, -0.10755503177642822, -1.570796251296997, 1], [0.8813461065292358, -0.10549483448266983, -1.570796251296997, 1], [0.8911315202713013, -0.10343464463949203, -1.570796251296997, 1], [0.9009170532226562, -0.10137443989515305, -1.570796251296997, 1], [0.9107025265693665, -0.09931425005197525, -1.570796251296997, 1], [0.9204879403114319, -0.09725406020879745, -1.570796251296997, 1], [0.9302734732627869, -0.09519386291503906, -1.570796251296997, 1], [0.9400589466094971, -0.09313366562128067, -1.570796251296997, 1], [0.9498444199562073, -0.09107346832752228, -1.570796251296997, 1], [0.9596298933029175, -0.08901327848434448, -1.570796251296997, 1], [0.9694154262542725, -0.08695308119058609, -1.570796251296997, 1], [0.9792008399963379, -0.0848928913474083, -1.570796251296997, 1], [0.9889863729476929, -0.0828326940536499, -1.570796251296997, 1], [0.9987717866897583, -0.08077249675989151, -1.570796251296997, 1], [0.9946514368057251, -0.061201538890600204, -1.570796251296997, 1], [0.9848659634590149, -0.0632617324590683, -1.570796251296997, 1], [0.9750804305076599, -0.06532192975282669, -1.570796251296997, 1], [0.9652950167655945, -0.06738212704658508, -1.570796251296997, 1], [0.9555095434188843, -0.06944231688976288, -1.570796251296997, 1], [0.9457240104675293, -0.07150251418352127, -1.570796251296997, 1], [0.9359385371208191, -0.07356271147727966, -1.570796251296997, 1], [0.9261531233787537, -0.07562290132045746, -1.570796251296997, 1], [0.9163675904273987, -0.07768309861421585, -1.570796251296997, 1], [0.9065821170806885, -0.07974329590797424, -1.570796251296997, 1], [0.8967966437339783, -0.08180348575115204, -1.570796251296997, 1], [0.8870111703872681, -0.08386368304491043, -1.570796251296997, 1], [0.8772256374359131, -0.08592388033866882, -1.570796251296997, 1], [0.8674402236938477, -0.08798407018184662, -1.570796251296997, 1], [0.8576547503471375, -0.09004426747560501, -1.570796251296997, 1], [0.8478692173957825, -0.0921044647693634, -1.570796251296997, 1], [0.8380837440490723, -0.0941646546125412, -1.570796251296997, 1], [0.8282983303070068, -0.09622485190629959, -1.570796251296997, 1], [0.8185127973556519, -0.09828504920005798, -1.570796251296997, 1], [0.8087273240089417, -0.10034523904323578, -1.570796251296997, 1], [0.7989418506622314, -0.10240543633699417, -1.570796251296997, 1], [0.7891563773155212, -0.10446563363075256, -1.570796251296997, 1], [0.779370903968811, -0.10652582347393036, -1.570796251296997, 1], [0.7695854306221008, -0.10858602076768875, -1.570796251296997, 1], [0.7597998976707458, -0.11064621806144714, -1.570796251296997, 1], [0.7500144839286804, -0.11270640790462494, -1.570796251296997, 1], [0.7402289509773254, -0.11476660519838333, -1.570796251296997, 1], [0.73044353723526, -0.11682680249214172, -1.570796251296997, 1], [0.720658004283905, -0.11888699233531952, -1.570796251296997, 1], [0.7108725309371948, -0.12094718962907791, -1.570796251296997, 1], [0.7010870575904846, -0.1230073869228363, -1.570796251296997, 1], [0.6969667077064514, -0.1034364253282547, -1.570796251296997, 1], [0.7067521214485168, -0.1013762354850769, -1.570796251296997, 1], [0.7165376543998718, -0.09931603819131851, -1.570796251296997, 1], [0.7263230681419373, -0.09725584089756012, -1.570796251296997, 1], [0.7361086010932922, -0.09519564360380173, -1.570796251296997, 1], [0.7458940744400024, -0.09313545376062393, -1.570796251296997, 1], [0.7556795477867126, -0.09107525646686554, -1.570796251296997, 1], [0.7654650211334229, -0.08901506662368774, -1.570796251296997, 1], [0.7752504944801331, -0.08695486932992935, -1.570796251296997, 1], [0.785036027431488, -0.08489467203617096, -1.570796251296997, 1], [0.7948214411735535, -0.08283447474241257, -1.570796251296997, 1], [0.8046069145202637, -0.08077428489923477, -1.570796251296997, 1], [0.8143924474716187, -0.07871408760547638, -1.570796251296997, 1], [0.8241779208183289, -0.07665389776229858, -1.570796251296997, 1], [0.8339633345603943, -0.07459370046854019, -1.570796251296997, 1], [0.8437488675117493, -0.0725335031747818, -1.570796251296997, 1], [0.8535343408584595, -0.07047330588102341, -1.570796251296997, 1], [0.8633198142051697, -0.06841311603784561, -1.570796251296997, 1], [0.8731052875518799, -0.06635291874408722, -1.570796251296997, 1], [0.8828907608985901, -0.06429272890090942, -1.570796251296997, 1], [0.8926762938499451, -0.06223252788186073, -1.570796251296997, 1], [0.9024617075920105, -0.06017233803868294, -1.570796251296997, 1], [0.9122471809387207, -0.058112140744924545, -1.570796251296997, 1], [0.9220327138900757, -0.05605194345116615, -1.570796251296997, 1], [0.9318181872367859, -0.05399175360798836, -1.570796251296997, 1], [0.9416036009788513, -0.051931556314229965, -1.570796251296997, 1], [0.9513891339302063, -0.04987135902047157, -1.570796251296997, 1], [0.9611746072769165, -0.04781116917729378, -1.570796251296997, 1], [0.9709600806236267, -0.045750971883535385, -1.570796251296997, 1], [0.9807455539703369, -0.04369077458977699, -1.570796251296997, 1], [0.9905310869216919, -0.0416305847465992, -1.570796251296997, 1], [0.9864106178283691, -0.022059623152017593, -1.570796251296997, 1], [0.9766252040863037, -0.024119820445775986, -1.570796251296997, 1], [0.9668396711349487, -0.02618001401424408, -1.570796251296997, 1], [0.9570541977882385, -0.028240209445357323, -1.570796251296997, 1], [0.9472687244415283, -0.030300403013825417, -1.570796251296997, 1], [0.9374832510948181, -0.03236059844493866, -1.570796251296997, 1], [0.9276977777481079, -0.034420792013406754, -1.570796251296997, 1], [0.9179123044013977, -0.036480989307165146, -1.570796251296997, 1], [0.9081268310546875, -0.03854118287563324, -1.570796251296997, 1], [0.8983413577079773, -0.04060138016939163, -1.570796251296997, 1], [0.8885558247566223, -0.04266157001256943, -1.570796251296997, 1], [0.8787704110145569, -0.04472176730632782, -1.570796251296997, 1], [0.8689848780632019, -0.04678196460008621, -1.570796251296997, 1], [0.8591994643211365, -0.04884215444326401, -1.570796251296997, 1], [0.8494139313697815, -0.0509023517370224, -1.570796251296997, 1], [0.8396284580230713, -0.05296254903078079, -1.570796251296997, 1], [0.8298429846763611, -0.05502273887395859, -1.570796251296997, 1], [0.8200575113296509, -0.05708293616771698, -1.570796251296997, 1], [0.8102720379829407, -0.05914313346147537, -1.570796251296997, 1], [0.8004865646362305, -0.06120332330465317, -1.570796251296997, 1], [0.7907010316848755, -0.06326352059841156, -1.570796251296997, 1], [0.7809156179428101, -0.06532371789216995, -1.570796251296997, 1], [0.7711301445960999, -0.06738390773534775, -1.570796251296997, 1], [0.7613446116447449, -0.06944410502910614, -1.570796251296997, 1], [0.7515591382980347, -0.07150430232286453, -1.570796251296997, 1], [0.7417737245559692, -0.07356449216604233, -1.570796251296997, 1], [0.7319881916046143, -0.07562468945980072, -1.570796251296997, 1], [0.722202718257904, -0.07768488675355911, -1.570796251296997, 1], [0.7124172449111938, -0.07974507659673691, -1.570796251296997, 1], [0.7026317119598389, -0.0818052738904953, -1.570796251296997, 1], [0.6928462982177734, -0.08386547118425369, -1.570796251296997, 1], [0.6887258887290955, -0.06429450958967209, -1.570796251296997, 1], [0.6985113620758057, -0.062234316021203995, -1.570796251296997, 1], [0.7082968950271606, -0.0601741224527359, -1.570796251296997, 1], [0.7180823087692261, -0.05811392515897751, -1.570796251296997, 1], [0.727867841720581, -0.056053731590509415, -1.570796251296997, 1], [0.7376532554626465, -0.05399353802204132, -1.570796251296997, 1], [0.7474387884140015, -0.05193334445357323, -1.570796251296997, 1], [0.7572242021560669, -0.049873147159814835, -1.570796251296997, 1], [0.7670097351074219, -0.04781294986605644, -1.570796251296997, 1], [0.7767952084541321, -0.04575276002287865, -1.570796251296997, 1], [0.7865806818008423, -0.043692562729120255, -1.570796251296997, 1], [0.7963661551475525, -0.04163236543536186, -1.570796251296997, 1], [0.8061516880989075, -0.03957217559218407, -1.570796251296997, 1], [0.8159371018409729, -0.037511978298425674, -1.570796251296997, 1], [0.8257225751876831, -0.03545178100466728, -1.570796251296997, 1], [0.8355081081390381, -0.03339159116148949, -1.570796251296997, 1], [0.8452935218811035, -0.031331393867731094, -1.570796251296997, 1], [0.8550790548324585, -0.02927119843661785, -1.570796251296997, 1], [0.8648645281791687, -0.027211004868149757, -1.570796251296997, 1], [0.8746500015258789, -0.025150809437036514, -1.570796251296997, 1], [0.8844354748725891, -0.02309061400592327, -1.570796251296997, 1], [0.8942209482192993, -0.021030420437455177, -1.570796251296997, 1], [0.9040064215660095, -0.018970225006341934, -1.570796251296997, 1], [0.9137918949127197, -0.01691003143787384, -1.570796251296997, 1], [0.9235773682594299, -0.014849835075438023, -1.570796251296997, 1], [0.9333629012107849, -0.012789640575647354, -1.570796251296997, 1], [0.9431483149528503, -0.010729446075856686, -1.570796251296997, 1], [0.9529338479042053, -0.008669251576066017, -1.570796251296997, 1], [0.9627193212509155, -0.006609056144952774, -1.570796251296997, 1], [0.972504734992981, -0.0045488616451621056, -1.570796251296997, 1], [0.9822902679443359, -0.002488666446879506, -1.570796251296997, 1], [0.978169858455658, 0.01708229072391987, -1.570796251296997, 1], [0.9683844447135925, 0.015022097155451775, -1.570796251296997, 1], [0.9585989117622375, 0.012961900793015957, -1.570796251296997, 1], [0.9488134384155273, 0.010901707224547863, -1.570796251296997, 1], [0.9390279054641724, 0.00884151179343462, -1.570796251296997, 1], [0.9292424917221069, 0.006781316827982664, -1.570796251296997, 1], [0.9194570183753967, 0.004721122328191996, -1.570796251296997, 1], [0.9096714854240417, 0.0026609275955706835, -1.570796251296997, 1], [0.8998860716819763, 0.0006007325137034059, -1.570796251296997, 1], [0.8901005387306213, -0.0014594622189179063, -1.570796251296997, 1], [0.8803150653839111, -0.0035196568351238966, -1.570796251296997, 1], [0.8705296516418457, -0.005579852033406496, -1.570796251296997, 1], [0.8607441186904907, -0.0076400465331971645, -1.570796251296997, 1], [0.8509586453437805, -0.00970024149864912, -1.570796251296997, 1], [0.8411731719970703, -0.011760435998439789, -1.570796251296997, 1], [0.8313876390457153, -0.013820631429553032, -1.570796251296997, 1], [0.8216022253036499, -0.015880824998021126, -1.570796251296997, 1], [0.8118167519569397, -0.01794102042913437, -1.570796251296997, 1], [0.8020312190055847, -0.020001215860247612, -1.570796251296997, 1], [0.7922458052635193, -0.022061411291360855, -1.570796251296997, 1], [0.7824602723121643, -0.02412160485982895, -1.570796251296997, 1], [0.7726747989654541, -0.026181800290942192, -1.570796251296997, 1], [0.7628893852233887, -0.028241993859410286, -1.570796251296997, 1], [0.7531038522720337, -0.03030218929052353, -1.570796251296997, 1], [0.7433183789253235, -0.03236238285899162, -1.570796251296997, 1], [0.7335329055786133, -0.034422580152750015, -1.570796251296997, 1], [0.7237473726272583, -0.03648277372121811, -1.570796251296997, 1], [0.7139619588851929, -0.0385429710149765, -1.570796251296997, 1], [0.7041764855384827, -0.0406031608581543, -1.570796251296997, 1], [0.6943909525871277, -0.04266335815191269, -1.570796251296997, 1], [0.6846055388450623, -0.04472355544567108, -1.570796251296997, 1], [0.6804850697517395, -0.025152593851089478, -1.570796251296997, 1], [0.6902706027030945, -0.023092400282621384, -1.570796251296997, 1], [0.7000560760498047, -0.02103220671415329, -1.570796251296997, 1], [0.7098415493965149, -0.018972011283040047, -1.570796251296997, 1], [0.7196270227432251, -0.016911815851926804, -1.570796251296997, 1], [0.7294125556945801, -0.014851621352136135, -1.570796251296997, 1], [0.7391979694366455, -0.012791425921022892, -1.570796251296997, 1], [0.7489834427833557, -0.010731231421232224, -1.570796251296997, 1], [0.7587689757347107, -0.008671036921441555, -1.570796251296997, 1], [0.7685543894767761, -0.0066108424216508865, -1.570796251296997, 1], [0.7783399224281311, -0.004550646990537643, -1.570796251296997, 1], [0.7881253957748413, -0.002490452490746975, -1.570796251296997, 1], [0.7979108691215515, -0.0004302576126065105, -1.570796251296997, 1], [0.8076963424682617, 0.0016299370909109712, -1.570796251296997, 1], [0.8174818158149719, 0.003690132172778249, -1.570796251296997, 1], [0.8272672891616821, 0.005750326439738274, -1.570796251296997, 1], [0.8370527625083923, 0.007810521870851517, -1.570796251296997, 1], [0.8468382358551025, 0.009870716370642185, -1.570796251296997, 1], [0.8566237688064575, 0.011930910870432854, -1.570796251296997, 1], [0.866409182548523, 0.013991106301546097, -1.570796251296997, 1], [0.8761947154998779, 0.01605129987001419, -1.570796251296997, 1], [0.8859801888465881, 0.018111497163772583, -1.570796251296997, 1], [0.8957656621932983, 0.020171688869595528, -1.570796251296997, 1], [0.9055511355400085, 0.02223188616335392, -1.570796251296997, 1], [0.915336549282074, 0.024292079731822014, -1.570796251296997, 1], [0.9251221418380737, 0.026352275162935257, -1.570796251296997, 1], [0.9349075555801392, 0.02841246873140335, -1.570796251296997, 1], [0.9446930289268494, 0.030472666025161743, -1.570796251296997, 1], [0.9544785022735596, 0.03253285959362984, -1.570796251296997, 1], [0.9642640352249146, 0.03459305316209793, -1.570796251296997, 1], [0.97404944896698, 0.03665325045585632, -1.570796251296997, 1], [0.9699290990829468, 0.05622420459985733, -1.570796251296997, 1], [0.9601436257362366, 0.054164011031389236, -1.570796251296997, 1], [0.9503581523895264, 0.05210381746292114, -1.570796251296997, 1], [0.9405726194381714, 0.05004362389445305, -1.570796251296997, 1], [0.930787205696106, 0.047983426600694656, -1.570796251296997, 1], [0.921001672744751, 0.04592323303222656, -1.570796251296997, 1], [0.9112162590026855, 0.04386303573846817, -1.570796251296997, 1], [0.9014307260513306, 0.041802845895290375, -1.570796251296997, 1], [0.8916452527046204, 0.03974264860153198, -1.570796251296997, 1], [0.8818597793579102, 0.03768245130777359, -1.570796251296997, 1], [0.8720743060112, 0.035622257739305496, -1.570796251296997, 1], [0.8622888326644897, 0.0335620641708374, -1.570796251296997, 1], [0.8525033593177795, 0.03150187060236931, -1.570796251296997, 1], [0.8427178263664246, 0.029441673308610916, -1.570796251296997, 1], [0.8329324126243591, 0.027381479740142822, -1.570796251296997, 1], [0.8231468796730042, 0.02532128430902958, -1.570796251296997, 1], [0.8133614659309387, 0.023261090740561485, -1.570796251296997, 1], [0.8035759329795837, 0.021200893446803093, -1.570796251296997, 1], [0.7937904596328735, 0.01914070174098015, -1.570796251296997, 1], [0.7840049862861633, 0.017080504447221756, -1.570796251296997, 1], [0.7742195129394531, 0.015020310878753662, -1.570796251296997, 1], [0.7644340395927429, 0.012960115447640419, -1.570796251296997, 1], [0.7546485662460327, 0.01089992094784975, -1.570796251296997, 1], [0.7448630928993225, 0.008839726448059082, -1.570796251296997, 1], [0.7350775599479675, 0.006779531016945839, -1.570796251296997, 1], [0.7252921462059021, 0.0047193365171551704, -1.570796251296997, 1], [0.7155066132545471, 0.002659142017364502, -1.570796251296997, 1], [0.7057211995124817, 0.0005989467026665807, -1.570796251296997, 1], [0.6959356665611267, -0.0014612477971240878, -1.570796251296997, 1], [0.6861501932144165, -0.0035214426461607218, -1.570796251296997, 1], [0.6763647198677063, -0.005581637378782034, -1.570796251296997, 1], [0.6722443699836731, 0.013989320024847984, -1.570796251296997, 1], [0.6820297837257385, 0.016049515455961227, -1.570796251296997, 1], [0.6918153166770935, 0.01810971088707447, -1.570796251296997, 1], [0.7016007900238037, 0.020169904455542564, -1.570796251296997, 1], [0.7113862037658691, 0.022230098024010658, -1.570796251296997, 1], [0.7211717367172241, 0.02429029531776905, -1.570796251296997, 1], [0.7309572100639343, 0.026350488886237144, -1.570796251296997, 1], [0.7407426834106445, 0.028410684317350388, -1.570796251296997, 1], [0.7505282163619995, 0.03047087788581848, -1.570796251296997, 1], [0.7603136301040649, 0.032531075179576874, -1.570796251296997, 1], [0.7700991034507751, 0.03459126874804497, -1.570796251296997, 1], [0.7798846364021301, 0.03665146231651306, -1.570796251296997, 1], [0.7896700501441956, 0.038711655884981155, -1.570796251296997, 1], [0.7994555830955505, 0.04077185317873955, -1.570796251296997, 1], [0.8092410564422607, 0.04283205047249794, -1.570796251296997, 1], [0.8190264701843262, 0.044892240315675735, -1.570796251296997, 1], [0.8288120031356812, 0.04695243760943413, -1.570796251296997, 1], [0.8385974764823914, 0.04901263117790222, -1.570796251296997, 1], [0.8483829498291016, 0.051072828471660614, -1.570796251296997, 1], [0.8581684827804565, 0.05313302204012871, -1.570796251296997, 1], [0.867953896522522, 0.0551932156085968, -1.570796251296997, 1], [0.8777393698692322, 0.057253409177064896, -1.570796251296997, 1], [0.8875249028205872, 0.05931360647082329, -1.570796251296997, 1], [0.8973103165626526, 0.06137380376458168, -1.570796251296997, 1], [0.9070958495140076, 0.06343399733304977, -1.570796251296997, 1], [0.9168813228607178, 0.06549418717622757, -1.570796251296997, 1], [0.9266667366027832, 0.06755438446998596, -1.570796251296997, 1], [0.9364522695541382, 0.06961458176374435, -1.570796251296997, 1], [0.9462377429008484, 0.07167477160692215, -1.570796251296997, 1], [0.9560232758522034, 0.07373496890068054, -1.570796251296997, 1], [0.9658086895942688, 0.07579516619443893, -1.570796251296997, 1], [0.9616882801055908, 0.09536612033843994, -1.570796251296997, 1], [0.9519028663635254, 0.09330593049526215, -1.570796251296997, 1], [0.9421173334121704, 0.09124573320150375, -1.570796251296997, 1], [0.9323318600654602, 0.08918553590774536, -1.570796251296997, 1], [0.9225464463233948, 0.08712534606456757, -1.570796251296997, 1], [0.9127609133720398, 0.08506514877080917, -1.570796251296997, 1], [0.9029754400253296, 0.08300495147705078, -1.570796251296997, 1], [0.8931899666786194, 0.08094476163387299, -1.570796251296997, 1], [0.8834044337272644, 0.0788845643401146, -1.570796251296997, 1], [0.873619019985199, 0.0768243670463562, -1.570796251296997, 1], [0.8638335466384888, 0.07476416975259781, -1.570796251296997, 1], [0.8540480136871338, 0.07270397990942001, -1.570796251296997, 1], [0.8442625999450684, 0.07064379006624222, -1.570796251296997, 1], [0.8344770669937134, 0.06858358532190323, -1.570796251296997, 1], [0.8246915936470032, 0.06652339547872543, -1.570796251296997, 1], [0.814906120300293, 0.06446319818496704, -1.570796251296997, 1], [0.8051207065582275, 0.062403008341789246, -1.570796251296997, 1], [0.7953351140022278, 0.06034281104803085, -1.570796251296997, 1], [0.7855497002601624, 0.05828261375427246, -1.570796251296997, 1], [0.7757642269134521, 0.056222423911094666, -1.570796251296997, 1], [0.7659787535667419, 0.05416222661733627, -1.570796251296997, 1], [0.756193220615387, 0.05210202932357788, -1.570796251296997, 1], [0.7464078068733215, 0.05004183575510979, -1.570796251296997, 1], [0.7366222739219666, 0.04798164218664169, -1.570796251296997, 1], [0.7268368601799011, 0.0459214486181736, -1.570796251296997, 1], [0.7170513272285461, 0.04386125132441521, -1.570796251296997, 1], [0.7072658538818359, 0.04180105775594711, -1.570796251296997, 1], [0.6974803805351257, 0.03974086046218872, -1.570796251296997, 1], [0.6876949071884155, 0.037680670619010925, -1.570796251296997, 1], [0.6779094338417053, 0.03562047332525253, -1.570796251296997, 1], [0.6681239604949951, 0.03356027603149414, -1.570796251296997, 1], [0.6640035510063171, 0.053131237626075745, -1.570796251296997, 1], [0.6737890243530273, 0.05519142746925354, -1.570796251296997, 1], [0.6835744976997375, 0.05725162848830223, -1.570796251296997, 1], [0.6933599710464478, 0.059311818331480026, -1.570796251296997, 1], [0.7031455039978027, 0.06137201562523842, -1.570796251296997, 1], [0.7129309177398682, 0.06343220919370651, -1.570796251296997, 1], [0.7227164506912231, 0.0654924064874649, -1.570796251296997, 1], [0.7325019240379333, 0.0675525963306427, -1.570796251296997, 1], [0.7422873973846436, 0.06961279362440109, -1.570796251296997, 1], [0.7520728707313538, 0.07167299091815948, -1.570796251296997, 1], [0.761858344078064, 0.07373318821191788, -1.570796251296997, 1], [0.7716438174247742, 0.07579337805509567, -1.570796251296997, 1], [0.7814292907714844, 0.07785357534885406, -1.570796251296997, 1], [0.7912147641181946, 0.07991376519203186, -1.570796251296997, 1], [0.8010002970695496, 0.08197396248579025, -1.570796251296997, 1], [0.810785710811615, 0.08403415977954865, -1.570796251296997, 1], [0.82057124376297, 0.08609434962272644, -1.570796251296997, 1], [0.8303566575050354, 0.08815454691648483, -1.570796251296997, 1], [0.8401421904563904, 0.09021474421024323, -1.570796251296997, 1], [0.8499276638031006, 0.09227494150400162, -1.570796251296997, 1], [0.8597131371498108, 0.09433513134717941, -1.570796251296997, 1], [0.869498610496521, 0.09639532119035721, -1.570796251296997, 1], [0.8792840838432312, 0.0984555259346962, -1.570796251296997, 1], [0.8890695571899414, 0.10051571577787399, -1.570796251296997, 1], [0.8988550901412964, 0.10257591307163239, -1.570796251296997, 1], [0.9086405038833618, 0.10463610291481018, -1.570796251296997, 1], [0.9184260368347168, 0.10669630020856857, -1.570796251296997, 1], [0.9282114505767822, 0.10875649750232697, -1.570796251296997, 1], [0.9379969835281372, 0.11081668734550476, -1.570796251296997, 1], [0.9477824568748474, 0.11287688463926315, -1.570796251296997, 1], [0.9575679302215576, 0.11493708193302155, -1.570796251296997, 1], [0.9534475207328796, 0.13450804352760315, -1.570796251296997, 1], [0.9436620473861694, 0.13244783878326416, -1.570796251296997, 1], [0.9338765740394592, 0.13038764894008636, -1.570796251296997, 1], [0.924091100692749, 0.12832745909690857, -1.570796251296997, 1], [0.9143056273460388, 0.12626725435256958, -1.570796251296997, 1], [0.9045201539993286, 0.12420706450939178, -1.570796251296997, 1], [0.8947346210479736, 0.12214686721563339, -1.570796251296997, 1], [0.8849492073059082, 0.1200866773724556, -1.570796251296997, 1], [0.8751636743545532, 0.11802647262811661, -1.570796251296997, 1], [0.8653782606124878, 0.11596629023551941, -1.570796251296997, 1], [0.8555927276611328, 0.11390608549118042, -1.570796251296997, 1], [0.8458072543144226, 0.11184589564800262, -1.570796251296997, 1], [0.8360217809677124, 0.10978569835424423, -1.570796251296997, 1], [0.8262363076210022, 0.10772550851106644, -1.570796251296997, 1], [0.816450834274292, 0.10566531121730804, -1.570796251296997, 1], [0.8066653609275818, 0.10360511392354965, -1.570796251296997, 1], [0.7968798875808716, 0.10154492408037186, -1.570796251296997, 1], [0.7870943546295166, 0.09948472678661346, -1.570796251296997, 1], [0.7773089408874512, 0.09742452949285507, -1.570796251296997, 1], [0.7675234079360962, 0.09536433964967728, -1.570796251296997, 1], [0.7577379941940308, 0.09330413490533829, -1.570796251296997, 1], [0.7479524612426758, 0.09124395251274109, -1.570796251296997, 1], [0.7381669878959656, 0.0891837477684021, -1.570796251296997, 1], [0.7283815145492554, 0.0871235579252243, -1.570796251296997, 1], [0.7185960412025452, 0.08506336808204651, -1.570796251296997, 1], [0.708810567855835, 0.08300316333770752, -1.570796251296997, 1], [0.6990250945091248, 0.08094297349452972, -1.570796251296997, 1], [0.6892395615577698, 0.07888277620077133, -1.570796251296997, 1], [0.6794541478157043, 0.07682258635759354, -1.570796251296997, 1], [0.6696686744689941, 0.07476238906383514, -1.570796251296997, 1], [0.6598831415176392, 0.07270219177007675, -1.570796251296997, 1], [0.655762791633606, 0.09227315336465836, -1.570796251296997, 1], [0.6655482649803162, 0.09433334320783615, -1.570796251296997, 1], [0.6753337383270264, 0.09639354050159454, -1.570796251296997, 1], [0.6851192116737366, 0.09845373779535294, -1.570796251296997, 1], [0.6949046850204468, 0.10051392763853073, -1.570796251296997, 1], [0.704690158367157, 0.10257413238286972, -1.570796251296997, 1], [0.7144756317138672, 0.10463431477546692, -1.570796251296997, 1], [0.7242611646652222, 0.10669451951980591, -1.570796251296997, 1], [0.7340465784072876, 0.1087547093629837, -1.570796251296997, 1], [0.7438321113586426, 0.1108149066567421, -1.570796251296997, 1], [0.753617525100708, 0.11287509649991989, -1.570796251296997, 1], [0.763403058052063, 0.11493529379367828, -1.570796251296997, 1], [0.7731885313987732, 0.11699549108743668, -1.570796251296997, 1], [0.7829740047454834, 0.11905568093061447, -1.570796251296997, 1], [0.7927594780921936, 0.12111587822437286, -1.570796251296997, 1], [0.8025449514389038, 0.12317607551813126, -1.570796251296997, 1], [0.8123304843902588, 0.12523627281188965, -1.570796251296997, 1], [0.8221158981323242, 0.12729646265506744, -1.570796251296997, 1], [0.8319013714790344, 0.12935665249824524, -1.570796251296997, 1], [0.8416869044303894, 0.13141685724258423, -1.570796251296997, 1], [0.8514723181724548, 0.13347704708576202, -1.570796251296997, 1], [0.8612578511238098, 0.13553723692893982, -1.570796251296997, 1], [0.87104332447052, 0.1375974416732788, -1.570796251296997, 1], [0.8808287978172302, 0.1396576315164566, -1.570796251296997, 1], [0.8906142711639404, 0.1417178213596344, -1.570796251296997, 1], [0.9003997445106506, 0.1437780261039734, -1.570796251296997, 1], [0.9101852178573608, 0.14583821594715118, -1.570796251296997, 1], [0.919970691204071, 0.14789840579032898, -1.570796251296997, 1], [0.929756224155426, 0.14995861053466797, -1.570796251296997, 1], [0.9395416378974915, 0.15201880037784576, -1.570796251296997, 1], [0.9493271708488464, 0.15407900512218475, -1.570796251296997, 1], [0.9452067613601685, 0.17364995181560516, -1.570796251296997, 1], [0.9354212284088135, 0.17158974707126617, -1.570796251296997, 1], [0.925635814666748, 0.16952957212924957, -1.570796251296997, 1], [0.9158503413200378, 0.16746936738491058, -1.570796251296997, 1], [0.9060648083686829, 0.1654091775417328, -1.570796251296997, 1], [0.8962793946266174, 0.1633489727973938, -1.570796251296997, 1], [0.8864938616752625, 0.161288782954216, -1.570796251296997, 1], [0.8767083883285522, 0.1592285931110382, -1.570796251296997, 1], [0.866922914981842, 0.1571684032678604, -1.570796251296997, 1], [0.8571374416351318, 0.15510819852352142, -1.570796251296997, 1], [0.8473519682884216, 0.15304800868034363, -1.570796251296997, 1], [0.8375664949417114, 0.15098780393600464, -1.570796251296997, 1], [0.8277810215950012, 0.14892761409282684, -1.570796251296997, 1], [0.817995548248291, 0.14686742424964905, -1.570796251296997, 1], [0.808210015296936, 0.14480721950531006, -1.570796251296997, 1], [0.7984246015548706, 0.14274702966213226, -1.570796251296997, 1], [0.7886390686035156, 0.14068683981895447, -1.570796251296997, 1], [0.7788535952568054, 0.13862664997577667, -1.570796251296997, 1], [0.76906818151474, 0.13656644523143768, -1.570796251296997, 1], [0.759282648563385, 0.1345062553882599, -1.570796251296997, 1], [0.7494971752166748, 0.1324460506439209, -1.570796251296997, 1], [0.7397117018699646, 0.1303858608007431, -1.570796251296997, 1], [0.7299262285232544, 0.1283256709575653, -1.570796251296997, 1], [0.7201406955718994, 0.12626546621322632, -1.570796251296997, 1], [0.710355281829834, 0.12420528382062912, -1.570796251296997, 1], [0.700569748878479, 0.12214508652687073, -1.570796251296997, 1], [0.6907843351364136, 0.12008488923311234, -1.570796251296997, 1], [0.6809988021850586, 0.11802469193935394, -1.570796251296997, 1], [0.6712133884429932, 0.11596449464559555, -1.570796251296997, 1], [0.6614278554916382, 0.11390430480241776, -1.570796251296997, 1], [0.651642382144928, 0.11184411495923996, -1.570796251296997, 1], [0.64752197265625, 0.13141506910324097, -1.570796251296997, 1], [0.657307505607605, 0.13347525894641876, -1.570796251296997, 1], [0.6670929193496704, 0.13553544878959656, -1.570796251296997, 1], [0.6768784523010254, 0.13759565353393555, -1.570796251296997, 1], [0.6866639256477356, 0.13965584337711334, -1.570796251296997, 1], [0.6964493989944458, 0.14171604812145233, -1.570796251296997, 1], [0.706234872341156, 0.14377623796463013, -1.570796251296997, 1], [0.7160203456878662, 0.14583642780780792, -1.570796251296997, 1], [0.7258058190345764, 0.1478966325521469, -1.570796251296997, 1], [0.7355912923812866, 0.1499568074941635, -1.570796251296997, 1], [0.7453768253326416, 0.1520170271396637, -1.570796251296997, 1], [0.755162239074707, 0.1540772020816803, -1.570796251296997, 1], [0.764947772026062, 0.1561374068260193, -1.570796251296997, 1], [0.7747331857681274, 0.15819759666919708, -1.570796251296997, 1], [0.7845187187194824, 0.16025780141353607, -1.570796251296997, 1], [0.7943041920661926, 0.16231799125671387, -1.570796251296997, 1], [0.8040896654129028, 0.16437818109989166, -1.570796251296997, 1], [0.813875138759613, 0.16643837094306946, -1.570796251296997, 1], [0.8236606121063232, 0.16849857568740845, -1.570796251296997, 1], [0.8334460854530334, 0.17055876553058624, -1.570796251296997, 1], [0.8432315587997437, 0.17261897027492523, -1.570796251296997, 1], [0.8530170917510986, 0.17467916011810303, -1.570796251296997, 1], [0.8628025054931641, 0.17673934996128082, -1.570796251296997, 1], [0.872588038444519, 0.1787995547056198, -1.570796251296997, 1], [0.8823734521865845, 0.1808597296476364, -1.570796251296997, 1], [0.8921589851379395, 0.1829199492931366, -1.570796251296997, 1], [0.9019444584846497, 0.1849801242351532, -1.570796251296997, 1], [0.9117299318313599, 0.1870403289794922, -1.570796251296997, 1], [0.9215154051780701, 0.18910051882266998, -1.570796251296997, 1], [0.9313008785247803, 0.19116072356700897, -1.570796251296997, 1], [0.9410863518714905, 0.19322091341018677, -1.570796251296997, 1], [0.9369660019874573, 0.21279186010360718, -1.570796251296997, 1], [0.9271804690361023, 0.21073167026042938, -1.570796251296997, 1], [0.9173950552940369, 0.2086714804172516, -1.570796251296997, 1], [0.8488966226577759, 0.19425012171268463, -1.570796251296997, 1], [0.8391112089157104, 0.19218991696834564, -1.570796251296997, 1], [0.8293257355690002, 0.19012972712516785, -1.570796251296997, 1], [0.8195402026176453, 0.18806953728199005, -1.570796251296997, 1], [0.8097547292709351, 0.18600933253765106, -1.570796251296997, 1], [0.7999693155288696, 0.18394914269447327, -1.570796251296997, 1], [0.7901837825775146, 0.18188895285129547, -1.570796251296997, 1], [0.7803983092308044, 0.17982874810695648, -1.570796251296997, 1], [0.7706128358840942, 0.1777685582637787, -1.570796251296997, 1], [0.760827362537384, 0.1757083684206009, -1.570796251296997, 1], [0.751041829586029, 0.1736481636762619, -1.570796251296997, 1], [0.7412564158439636, 0.1715879738330841, -1.570796251296997, 1], [0.7314709424972534, 0.16952776908874512, -1.570796251296997, 1], [0.7216854095458984, 0.16746759414672852, -1.570796251296997, 1], [0.711899995803833, 0.16540738940238953, -1.570796251296997, 1], [0.702114462852478, 0.16334718465805054, -1.570796251296997, 1], [0.6923289895057678, 0.16128699481487274, -1.570796251296997, 1], [0.6825435161590576, 0.15922680497169495, -1.570796251296997, 1], [0.6727580428123474, 0.15716661512851715, -1.570796251296997, 1], [0.6629725694656372, 0.15510641038417816, -1.570796251296997, 1], [0.653187096118927, 0.15304622054100037, -1.570796251296997, 1], [0.6434016227722168, 0.15098603069782257, -1.570796251296997, 1], [0.6392812132835388, 0.17055697739124298, -1.570796251296997, 1], [0.649066686630249, 0.17261718213558197, -1.570796251296997, 1], [0.6588521599769592, 0.17467737197875977, -1.570796251296997, 1], [0.6686376929283142, 0.17673756182193756, -1.570796251296997, 1], [0.6784231066703796, 0.17879776656627655, -1.570796251296997, 1], [0.6882086396217346, 0.18085795640945435, -1.570796251296997, 1], [0.6979940533638, 0.18291814625263214, -1.570796251296997, 1], [0.707779586315155, 0.18497835099697113, -1.570796251296997, 1], [0.7175650596618652, 0.18703854084014893, -1.570796251296997, 1], [0.7273505330085754, 0.18909873068332672, -1.570796251296997, 1], [0.7371360063552856, 0.1911589354276657, -1.570796251296997, 1], [0.7469214797019958, 0.1932191252708435, -1.570796251296997, 1], [0.654731810092926, 0.19424833357334137, -1.570796251296997, 1], [0.644946277141571, 0.19218812882900238, -1.570796251296997, 1], [0.6351608633995056, 0.19012795388698578, -1.570796251296997, 1]]
\ No newline at end of file
diff --git a/probe_vis_data_r0_0.json b/probe_vis_data_r0_0.json
new file mode 100644
index 0000000..71dad1a
--- /dev/null
+++ b/probe_vis_data_r0_0.json
@@ -0,0 +1 @@
           1 +[[0.7052074670791626, -0.1425783336162567, 1.390511439325337e-08, 0], [0.7149929404258728, -0.14051814377307892, 1.390511439325337e-08, 0], [0.724778413772583, -0.13845795392990112, 1.390511439325337e-08, 0], [0.7345638871192932, -0.13639776408672333, 1.390511439325337e-08, 0], [0.7443493604660034, -0.13433755934238434, 1.390511439325337e-08, 0], [0.7541348338127136, -0.13227736949920654, 1.390511439325337e-08, 0], [0.7639203667640686, -0.13021717965602875, 1.390511439325337e-08, 0], [0.773705780506134, -0.12815697491168976, 1.390511439325337e-08, 0], [0.783491313457489, -0.12609678506851196, 1.390511439325337e-08, 0], [0.7932767271995544, -0.12403658777475357, 1.390511439325337e-08, 0], [0.8030622601509094, -0.12197639048099518, 1.390511439325337e-08, 0], [0.8128477334976196, -0.11991620063781738, 1.390511439325337e-08, 0], [0.8226331472396851, -0.11785600334405899, 1.390511439325337e-08, 0], [0.83241868019104, -0.1157958135008812, 1.390511439325337e-08, 1], [0.8422041535377502, -0.1137356087565422, 1.390511439325337e-08, 1], [0.8519896864891052, -0.11167542636394501, 1.390511439325337e-08, 1], [0.8617751002311707, -0.10961522161960602, 1.390511439325337e-08, 1], [0.8715605735778809, -0.10755503177642822, 1.390511439325337e-08, 1], [0.8813461065292358, -0.10549483448266983, 1.390511439325337e-08, 1], [0.8911315202713013, -0.10343464463949203, 1.390511439325337e-08, 1], [0.9009170532226562, -0.10137443989515305, 1.390511439325337e-08, 1], [0.9107025265693665, -0.09931425005197525, 1.390511439325337e-08, 1], [0.9204879403114319, -0.09725406020879745, 1.390511439325337e-08, 1], [0.9302734732627869, -0.09519386291503906, 1.390511439325337e-08, 1], [0.9400589466094971, -0.09313366562128067, 1.390511439325337e-08, 1], [0.9498444199562073, -0.09107346832752228, 1.390511439325337e-08, 1], [0.9596298933029175, -0.08901327848434448, 1.390511439325337e-08, 1], [0.9694154262542725, -0.08695308119058609, 1.390511439325337e-08, 1], [0.9792008399963379, -0.0848928913474083, 1.390511439325337e-08, 1], [0.9889863729476929, -0.0828326940536499, 1.390511439325337e-08, 1], [0.9987717866897583, -0.08077249675989151, 1.390511439325337e-08, 1], [0.9946514368057251, -0.061201538890600204, 1.390511439325337e-08, 1], [0.9848659634590149, -0.0632617324590683, 1.390511439325337e-08, 1], [0.9750804305076599, -0.06532192975282669, 1.390511439325337e-08, 1], [0.9652950167655945, -0.06738212704658508, 1.390511439325337e-08, 1], [0.9555095434188843, -0.06944231688976288, 1.390511439325337e-08, 1], [0.9457240104675293, -0.07150251418352127, 1.390511439325337e-08, 1], [0.9359385371208191, -0.07356271147727966, 1.390511439325337e-08, 1], [0.9261531233787537, -0.07562290132045746, 1.390511439325337e-08, 1], [0.9163675904273987, -0.07768309861421585, 1.390511439325337e-08, 1], [0.9065821170806885, -0.07974329590797424, 1.390511439325337e-08, 1], [0.8967966437339783, -0.08180348575115204, 1.390511439325337e-08, 1], [0.8870111703872681, -0.08386368304491043, 1.390511439325337e-08, 1], [0.8772256374359131, -0.08592388033866882, 1.390511439325337e-08, 1], [0.8674402236938477, -0.08798407018184662, 1.390511439325337e-08, 1], [0.8576547503471375, -0.09004426747560501, 1.390511439325337e-08, 1], [0.8478692173957825, -0.0921044647693634, 1.390511439325337e-08, 1], [0.8380837440490723, -0.0941646546125412, 1.390511439325337e-08, 1], [0.8282983303070068, -0.09622485190629959, 1.390511439325337e-08, 1], [0.8185127973556519, -0.09828504920005798, 1.390511439325337e-08, 1], [0.8087273240089417, -0.10034523904323578, 1.390511439325337e-08, 1], [0.7989418506622314, -0.10240543633699417, 1.390511439325337e-08, 1], [0.7891563773155212, -0.10446563363075256, 1.390511439325337e-08, 1], [0.779370903968811, -0.10652582347393036, 1.390511439325337e-08, 1], [0.7695854306221008, -0.10858602076768875, 1.390511439325337e-08, 1], [0.7597998976707458, -0.11064621806144714, 1.390511439325337e-08, 1], [0.7500144839286804, -0.11270640790462494, 1.390511439325337e-08, 1], [0.7402289509773254, -0.11476660519838333, 1.390511439325337e-08, 1], [0.73044353723526, -0.11682680249214172, 1.390511439325337e-08, 1], [0.720658004283905, -0.11888699233531952, 1.390511439325337e-08, 1], [0.7108725309371948, -0.12094718962907791, 1.390511439325337e-08, 1], [0.7010870575904846, -0.1230073869228363, 1.390511439325337e-08, 1], [0.6969667077064514, -0.1034364253282547, 1.390511439325337e-08, 1], [0.7067521214485168, -0.1013762354850769, 1.390511439325337e-08, 1], [0.7165376543998718, -0.09931603819131851, 1.390511439325337e-08, 1], [0.7263230681419373, -0.09725584089756012, 1.390511439325337e-08, 1], [0.7361086010932922, -0.09519564360380173, 1.390511439325337e-08, 1], [0.7458940744400024, -0.09313545376062393, 1.390511439325337e-08, 1], [0.7556795477867126, -0.09107525646686554, 1.390511439325337e-08, 1], [0.7654650211334229, -0.08901506662368774, 1.390511439325337e-08, 1], [0.7752504944801331, -0.08695486932992935, 1.390511439325337e-08, 1], [0.785036027431488, -0.08489467203617096, 1.390511439325337e-08, 1], [0.7948214411735535, -0.08283447474241257, 1.390511439325337e-08, 1], [0.8046069145202637, -0.08077428489923477, 1.390511439325337e-08, 1], [0.8143924474716187, -0.07871408760547638, 1.390511439325337e-08, 1], [0.8241779208183289, -0.07665389776229858, 1.390511439325337e-08, 1], [0.8339633345603943, -0.07459370046854019, 1.390511439325337e-08, 1], [0.8437488675117493, -0.0725335031747818, 1.390511439325337e-08, 1], [0.8535343408584595, -0.07047330588102341, 1.390511439325337e-08, 1], [0.8633198142051697, -0.06841311603784561, 1.390511439325337e-08, 1], [0.8731052875518799, -0.06635291874408722, 1.390511439325337e-08, 1], [0.8828907608985901, -0.06429272890090942, 1.390511439325337e-08, 1], [0.8926762938499451, -0.06223252788186073, 1.390511439325337e-08, 1], [0.9024617075920105, -0.06017233803868294, 1.390511439325337e-08, 1], [0.9122471809387207, -0.058112140744924545, 1.390511439325337e-08, 1], [0.9220327138900757, -0.05605194345116615, 1.390511439325337e-08, 1], [0.9318181872367859, -0.05399175360798836, 1.390511439325337e-08, 1], [0.9416036009788513, -0.051931556314229965, 1.390511439325337e-08, 1], [0.9513891339302063, -0.04987135902047157, 1.390511439325337e-08, 1], [0.9611746072769165, -0.04781116917729378, 1.390511439325337e-08, 1], [0.9709600806236267, -0.045750971883535385, 1.390511439325337e-08, 1], [0.9807455539703369, -0.04369077458977699, 1.390511439325337e-08, 1], [0.9905310869216919, -0.0416305847465992, 1.390511439325337e-08, 1], [0.9864106178283691, -0.022059623152017593, 1.390511439325337e-08, 1], [0.9766252040863037, -0.024119820445775986, 1.390511439325337e-08, 1], [0.9668396711349487, -0.02618001401424408, 1.390511439325337e-08, 1], [0.9570541977882385, -0.028240209445357323, 1.390511439325337e-08, 1], [0.9472687244415283, -0.030300403013825417, 1.390511439325337e-08, 1], [0.9374832510948181, -0.03236059844493866, 1.390511439325337e-08, 1], [0.9276977777481079, -0.034420792013406754, 1.390511439325337e-08, 1], [0.9179123044013977, -0.036480989307165146, 1.390511439325337e-08, 1], [0.9081268310546875, -0.03854118287563324, 1.390511439325337e-08, 1], [0.8983413577079773, -0.04060138016939163, 1.390511439325337e-08, 1], [0.8885558247566223, -0.04266157001256943, 1.390511439325337e-08, 1], [0.8787704110145569, -0.04472176730632782, 1.390511439325337e-08, 1], [0.8689848780632019, -0.04678196460008621, 1.390511439325337e-08, 1], [0.8591994643211365, -0.04884215444326401, 1.390511439325337e-08, 1], [0.8494139313697815, -0.0509023517370224, 1.390511439325337e-08, 1], [0.8396284580230713, -0.05296254903078079, 1.390511439325337e-08, 1], [0.8298429846763611, -0.05502273887395859, 1.390511439325337e-08, 1], [0.8200575113296509, -0.05708293616771698, 1.390511439325337e-08, 1], [0.8102720379829407, -0.05914313346147537, 1.390511439325337e-08, 1], [0.8004865646362305, -0.06120332330465317, 1.390511439325337e-08, 1], [0.7907010316848755, -0.06326352059841156, 1.390511439325337e-08, 1], [0.7809156179428101, -0.06532371789216995, 1.390511439325337e-08, 1], [0.7711301445960999, -0.06738390773534775, 1.390511439325337e-08, 1], [0.7613446116447449, -0.06944410502910614, 1.390511439325337e-08, 1], [0.7515591382980347, -0.07150430232286453, 1.390511439325337e-08, 1], [0.7417737245559692, -0.07356449216604233, 1.390511439325337e-08, 1], [0.7319881916046143, -0.07562468945980072, 1.390511439325337e-08, 1], [0.722202718257904, -0.07768488675355911, 1.390511439325337e-08, 1], [0.7124172449111938, -0.07974507659673691, 1.390511439325337e-08, 1], [0.7026317119598389, -0.0818052738904953, 1.390511439325337e-08, 1], [0.6928462982177734, -0.08386547118425369, 1.390511439325337e-08, 1], [0.6887258887290955, -0.06429450958967209, 1.390511439325337e-08, 1], [0.6985113620758057, -0.062234316021203995, 1.390511439325337e-08, 1], [0.7082968950271606, -0.0601741224527359, 1.390511439325337e-08, 1], [0.7180823087692261, -0.05811392515897751, 1.390511439325337e-08, 1], [0.727867841720581, -0.056053731590509415, 1.390511439325337e-08, 1], [0.7376532554626465, -0.05399353802204132, 1.390511439325337e-08, 1], [0.7474387884140015, -0.05193334445357323, 1.390511439325337e-08, 1], [0.7572242021560669, -0.049873147159814835, 1.390511439325337e-08, 1], [0.7670097351074219, -0.04781294986605644, 1.390511439325337e-08, 1], [0.7767952084541321, -0.04575276002287865, 1.390511439325337e-08, 1], [0.7865806818008423, -0.043692562729120255, 1.390511439325337e-08, 1], [0.7963661551475525, -0.04163236543536186, 1.390511439325337e-08, 1], [0.8061516880989075, -0.03957217559218407, 1.390511439325337e-08, 1], [0.8159371018409729, -0.037511978298425674, 1.390511439325337e-08, 1], [0.8257225751876831, -0.03545178100466728, 1.390511439325337e-08, 1], [0.8355081081390381, -0.03339159116148949, 1.390511439325337e-08, 1], [0.8452935218811035, -0.031331393867731094, 1.390511439325337e-08, 1], [0.8550790548324585, -0.02927119843661785, 1.390511439325337e-08, 1], [0.8648645281791687, -0.027211004868149757, 1.390511439325337e-08, 1], [0.8746500015258789, -0.025150809437036514, 1.390511439325337e-08, 1], [0.8844354748725891, -0.02309061400592327, 1.390511439325337e-08, 1], [0.8942209482192993, -0.021030420437455177, 1.390511439325337e-08, 1], [0.9040064215660095, -0.018970225006341934, 1.390511439325337e-08, 1], [0.9137918949127197, -0.01691003143787384, 1.390511439325337e-08, 1], [0.9235773682594299, -0.014849835075438023, 1.390511439325337e-08, 1], [0.9333629012107849, -0.012789640575647354, 1.390511439325337e-08, 1], [0.9431483149528503, -0.010729446075856686, 1.390511439325337e-08, 1], [0.9529338479042053, -0.008669251576066017, 1.390511439325337e-08, 1], [0.9627193212509155, -0.006609056144952774, 1.390511439325337e-08, 1], [0.972504734992981, -0.0045488616451621056, 1.390511439325337e-08, 1], [0.9822902679443359, -0.002488666446879506, 1.390511439325337e-08, 1], [0.978169858455658, 0.01708229072391987, 1.390511439325337e-08, 1], [0.9683844447135925, 0.015022097155451775, 1.390511439325337e-08, 1], [0.9585989117622375, 0.012961900793015957, 1.390511439325337e-08, 1], [0.9488134384155273, 0.010901707224547863, 1.390511439325337e-08, 1], [0.9390279054641724, 0.00884151179343462, 1.390511439325337e-08, 1], [0.9292424917221069, 0.006781316827982664, 1.390511439325337e-08, 1], [0.9194570183753967, 0.004721122328191996, 1.390511439325337e-08, 1], [0.9096714854240417, 0.0026609275955706835, 1.390511439325337e-08, 1], [0.8998860716819763, 0.0006007325137034059, 1.390511439325337e-08, 1], [0.8901005387306213, -0.0014594622189179063, 1.390511439325337e-08, 1], [0.8803150653839111, -0.0035196568351238966, 1.390511439325337e-08, 1], [0.8705296516418457, -0.005579852033406496, 1.390511439325337e-08, 1], [0.8607441186904907, -0.0076400465331971645, 1.390511439325337e-08, 1], [0.8509586453437805, -0.00970024149864912, 1.390511439325337e-08, 1], [0.8411731719970703, -0.011760435998439789, 1.390511439325337e-08, 1], [0.8313876390457153, -0.013820631429553032, 1.390511439325337e-08, 1], [0.8216022253036499, -0.015880824998021126, 1.390511439325337e-08, 1], [0.8118167519569397, -0.01794102042913437, 1.390511439325337e-08, 1], [0.8020312190055847, -0.020001215860247612, 1.390511439325337e-08, 1], [0.7922458052635193, -0.022061411291360855, 1.390511439325337e-08, 1], [0.7824602723121643, -0.02412160485982895, 1.390511439325337e-08, 1], [0.7726747989654541, -0.026181800290942192, 1.390511439325337e-08, 1], [0.7628893852233887, -0.028241993859410286, 1.390511439325337e-08, 1], [0.7531038522720337, -0.03030218929052353, 1.390511439325337e-08, 1], [0.7433183789253235, -0.03236238285899162, 1.390511439325337e-08, 1], [0.7335329055786133, -0.034422580152750015, 1.390511439325337e-08, 1], [0.7237473726272583, -0.03648277372121811, 1.390511439325337e-08, 1], [0.7139619588851929, -0.0385429710149765, 1.390511439325337e-08, 1], [0.7041764855384827, -0.0406031608581543, 1.390511439325337e-08, 1], [0.6943909525871277, -0.04266335815191269, 1.390511439325337e-08, 1], [0.6846055388450623, -0.04472355544567108, 1.390511439325337e-08, 1], [0.6804850697517395, -0.025152593851089478, 1.390511439325337e-08, 1], [0.6902706027030945, -0.023092400282621384, 1.390511439325337e-08, 1], [0.7000560760498047, -0.02103220671415329, 1.390511439325337e-08, 1], [0.7098415493965149, -0.018972011283040047, 1.390511439325337e-08, 1], [0.7196270227432251, -0.016911815851926804, 1.390511439325337e-08, 1], [0.7294125556945801, -0.014851621352136135, 1.390511439325337e-08, 1], [0.7391979694366455, -0.012791425921022892, 1.390511439325337e-08, 1], [0.7489834427833557, -0.010731231421232224, 1.390511439325337e-08, 1], [0.7587689757347107, -0.008671036921441555, 1.390511439325337e-08, 1], [0.7685543894767761, -0.0066108424216508865, 1.390511439325337e-08, 1], [0.7783399224281311, -0.004550646990537643, 1.390511439325337e-08, 1], [0.7881253957748413, -0.002490452490746975, 1.390511439325337e-08, 1], [0.7979108691215515, -0.0004302576126065105, 1.390511439325337e-08, 1], [0.8076963424682617, 0.0016299370909109712, 1.390511439325337e-08, 1], [0.8174818158149719, 0.003690132172778249, 1.390511439325337e-08, 1], [0.8272672891616821, 0.005750326439738274, 1.390511439325337e-08, 1], [0.8370527625083923, 0.007810521870851517, 1.390511439325337e-08, 1], [0.8468382358551025, 0.009870716370642185, 1.390511439325337e-08, 1], [0.8566237688064575, 0.011930910870432854, 1.390511439325337e-08, 1], [0.866409182548523, 0.013991106301546097, 1.390511439325337e-08, 1], [0.8761947154998779, 0.01605129987001419, 1.390511439325337e-08, 1], [0.8859801888465881, 0.018111497163772583, 1.390511439325337e-08, 1], [0.8957656621932983, 0.020171688869595528, 1.390511439325337e-08, 1], [0.9055511355400085, 0.02223188616335392, 1.390511439325337e-08, 1], [0.915336549282074, 0.024292079731822014, 1.390511439325337e-08, 1], [0.9251221418380737, 0.026352275162935257, 1.390511439325337e-08, 1], [0.9349075555801392, 0.02841246873140335, 1.390511439325337e-08, 1], [0.9446930289268494, 0.030472666025161743, 1.390511439325337e-08, 1], [0.9544785022735596, 0.03253285959362984, 1.390511439325337e-08, 1], [0.9642640352249146, 0.03459305316209793, 1.390511439325337e-08, 1], [0.97404944896698, 0.03665325045585632, 1.390511439325337e-08, 1], [0.9699290990829468, 0.05622420459985733, 1.390511439325337e-08, 1], [0.9601436257362366, 0.054164011031389236, 1.390511439325337e-08, 1], [0.9503581523895264, 0.05210381746292114, 1.390511439325337e-08, 1], [0.9405726194381714, 0.05004362389445305, 1.390511439325337e-08, 1], [0.930787205696106, 0.047983426600694656, 1.390511439325337e-08, 1], [0.921001672744751, 0.04592323303222656, 1.390511439325337e-08, 1], [0.9112162590026855, 0.04386303573846817, 1.390511439325337e-08, 1], [0.9014307260513306, 0.041802845895290375, 1.390511439325337e-08, 1], [0.8916452527046204, 0.03974264860153198, 1.390511439325337e-08, 1], [0.8818597793579102, 0.03768245130777359, 1.390511439325337e-08, 1], [0.8720743060112, 0.035622257739305496, 1.390511439325337e-08, 1], [0.8622888326644897, 0.0335620641708374, 1.390511439325337e-08, 1], [0.8525033593177795, 0.03150187060236931, 1.390511439325337e-08, 1], [0.8427178263664246, 0.029441673308610916, 1.390511439325337e-08, 1], [0.8329324126243591, 0.027381479740142822, 1.390511439325337e-08, 1], [0.8231468796730042, 0.02532128430902958, 1.390511439325337e-08, 1], [0.8133614659309387, 0.023261090740561485, 1.390511439325337e-08, 1], [0.8035759329795837, 0.021200893446803093, 1.390511439325337e-08, 1], [0.7937904596328735, 0.01914070174098015, 1.390511439325337e-08, 1], [0.7840049862861633, 0.017080504447221756, 1.390511439325337e-08, 1], [0.7742195129394531, 0.015020310878753662, 1.390511439325337e-08, 1], [0.7644340395927429, 0.012960115447640419, 1.390511439325337e-08, 1], [0.7546485662460327, 0.01089992094784975, 1.390511439325337e-08, 1], [0.7448630928993225, 0.008839726448059082, 1.390511439325337e-08, 1], [0.7350775599479675, 0.006779531016945839, 1.390511439325337e-08, 1], [0.7252921462059021, 0.0047193365171551704, 1.390511439325337e-08, 1], [0.7155066132545471, 0.002659142017364502, 1.390511439325337e-08, 1], [0.7057211995124817, 0.0005989467026665807, 1.390511439325337e-08, 1], [0.6959356665611267, -0.0014612477971240878, 1.390511439325337e-08, 1], [0.6861501932144165, -0.0035214426461607218, 1.390511439325337e-08, 1], [0.6763647198677063, -0.005581637378782034, 1.390511439325337e-08, 1], [0.6722443699836731, 0.013989320024847984, 1.390511439325337e-08, 1], [0.6820297837257385, 0.016049515455961227, 1.390511439325337e-08, 1], [0.6918153166770935, 0.01810971088707447, 1.390511439325337e-08, 1], [0.7016007900238037, 0.020169904455542564, 1.390511439325337e-08, 1], [0.7113862037658691, 0.022230098024010658, 1.390511439325337e-08, 1], [0.7211717367172241, 0.02429029531776905, 1.390511439325337e-08, 1], [0.7309572100639343, 0.026350488886237144, 1.390511439325337e-08, 1], [0.7407426834106445, 0.028410684317350388, 1.390511439325337e-08, 1], [0.7505282163619995, 0.03047087788581848, 1.390511439325337e-08, 1], [0.7603136301040649, 0.032531075179576874, 1.390511439325337e-08, 1], [0.7700991034507751, 0.03459126874804497, 1.390511439325337e-08, 1], [0.7798846364021301, 0.03665146231651306, 1.390511439325337e-08, 1], [0.7896700501441956, 0.038711655884981155, 1.390511439325337e-08, 1], [0.7994555830955505, 0.04077185317873955, 1.390511439325337e-08, 1], [0.8092410564422607, 0.04283205047249794, 1.390511439325337e-08, 1], [0.8190264701843262, 0.044892240315675735, 1.390511439325337e-08, 1], [0.8288120031356812, 0.04695243760943413, 1.390511439325337e-08, 1], [0.8385974764823914, 0.04901263117790222, 1.390511439325337e-08, 1], [0.8483829498291016, 0.051072828471660614, 1.390511439325337e-08, 1], [0.8581684827804565, 0.05313302204012871, 1.390511439325337e-08, 1], [0.867953896522522, 0.0551932156085968, 1.390511439325337e-08, 1], [0.8777393698692322, 0.057253409177064896, 1.390511439325337e-08, 1], [0.8875249028205872, 0.05931360647082329, 1.390511439325337e-08, 1], [0.8973103165626526, 0.06137380376458168, 1.390511439325337e-08, 1], [0.9070958495140076, 0.06343399733304977, 1.390511439325337e-08, 1], [0.9168813228607178, 0.06549418717622757, 1.390511439325337e-08, 1], [0.9266667366027832, 0.06755438446998596, 1.390511439325337e-08, 1], [0.9364522695541382, 0.06961458176374435, 1.390511439325337e-08, 1], [0.9462377429008484, 0.07167477160692215, 1.390511439325337e-08, 1], [0.9560232758522034, 0.07373496890068054, 1.390511439325337e-08, 1], [0.9658086895942688, 0.07579516619443893, 1.390511439325337e-08, 1], [0.9616882801055908, 0.09536612033843994, 1.390511439325337e-08, 1], [0.9519028663635254, 0.09330593049526215, 1.390511439325337e-08, 1], [0.9421173334121704, 0.09124573320150375, 1.390511439325337e-08, 1], [0.9323318600654602, 0.08918553590774536, 1.390511439325337e-08, 1], [0.9225464463233948, 0.08712534606456757, 1.390511439325337e-08, 1], [0.9127609133720398, 0.08506514877080917, 1.390511439325337e-08, 1], [0.9029754400253296, 0.08300495147705078, 1.390511439325337e-08, 1], [0.8931899666786194, 0.08094476163387299, 1.390511439325337e-08, 1], [0.8834044337272644, 0.0788845643401146, 1.390511439325337e-08, 1], [0.873619019985199, 0.0768243670463562, 1.390511439325337e-08, 1], [0.8638335466384888, 0.07476416975259781, 1.390511439325337e-08, 1], [0.8540480136871338, 0.07270397990942001, 1.390511439325337e-08, 1], [0.8442625999450684, 0.07064379006624222, 1.390511439325337e-08, 1], [0.8344770669937134, 0.06858358532190323, 1.390511439325337e-08, 1], [0.8246915936470032, 0.06652339547872543, 1.390511439325337e-08, 1], [0.814906120300293, 0.06446319818496704, 1.390511439325337e-08, 1], [0.8051207065582275, 0.062403008341789246, 1.390511439325337e-08, 1], [0.7953351140022278, 0.06034281104803085, 1.390511439325337e-08, 1], [0.7855497002601624, 0.05828261375427246, 1.390511439325337e-08, 1], [0.7757642269134521, 0.056222423911094666, 1.390511439325337e-08, 1], [0.7659787535667419, 0.05416222661733627, 1.390511439325337e-08, 1], [0.756193220615387, 0.05210202932357788, 1.390511439325337e-08, 1], [0.7464078068733215, 0.05004183575510979, 1.390511439325337e-08, 1], [0.7366222739219666, 0.04798164218664169, 1.390511439325337e-08, 1], [0.7268368601799011, 0.0459214486181736, 1.390511439325337e-08, 1], [0.7170513272285461, 0.04386125132441521, 1.390511439325337e-08, 1], [0.7072658538818359, 0.04180105775594711, 1.390511439325337e-08, 1], [0.6974803805351257, 0.03974086046218872, 1.390511439325337e-08, 1], [0.6876949071884155, 0.037680670619010925, 1.390511439325337e-08, 1], [0.6779094338417053, 0.03562047332525253, 1.390511439325337e-08, 1], [0.6681239604949951, 0.03356027603149414, 1.390511439325337e-08, 1], [0.6640035510063171, 0.053131237626075745, 1.390511439325337e-08, 1], [0.6737890243530273, 0.05519142746925354, 1.390511439325337e-08, 1], [0.6835744976997375, 0.05725162848830223, 1.390511439325337e-08, 1], [0.6933599710464478, 0.059311818331480026, 1.390511439325337e-08, 1], [0.7031455039978027, 0.06137201562523842, 1.390511439325337e-08, 1], [0.7129309177398682, 0.06343220919370651, 1.390511439325337e-08, 1], [0.7227164506912231, 0.0654924064874649, 1.390511439325337e-08, 1], [0.7325019240379333, 0.0675525963306427, 1.390511439325337e-08, 1], [0.7422873973846436, 0.06961279362440109, 1.390511439325337e-08, 1], [0.7520728707313538, 0.07167299091815948, 1.390511439325337e-08, 1], [0.761858344078064, 0.07373318821191788, 1.390511439325337e-08, 1], [0.7716438174247742, 0.07579337805509567, 1.390511439325337e-08, 1], [0.7814292907714844, 0.07785357534885406, 1.390511439325337e-08, 1], [0.7912147641181946, 0.07991376519203186, 1.390511439325337e-08, 1], [0.8010002970695496, 0.08197396248579025, 1.390511439325337e-08, 1], [0.810785710811615, 0.08403415977954865, 1.390511439325337e-08, 1], [0.82057124376297, 0.08609434962272644, 1.390511439325337e-08, 1], [0.8303566575050354, 0.08815454691648483, 1.390511439325337e-08, 1], [0.8401421904563904, 0.09021474421024323, 1.390511439325337e-08, 1], [0.8499276638031006, 0.09227494150400162, 1.390511439325337e-08, 1], [0.8597131371498108, 0.09433513134717941, 1.390511439325337e-08, 1], [0.869498610496521, 0.09639532119035721, 1.390511439325337e-08, 1], [0.8792840838432312, 0.0984555259346962, 1.390511439325337e-08, 1], [0.8890695571899414, 0.10051571577787399, 1.390511439325337e-08, 1], [0.8988550901412964, 0.10257591307163239, 1.390511439325337e-08, 1], [0.9086405038833618, 0.10463610291481018, 1.390511439325337e-08, 1], [0.9184260368347168, 0.10669630020856857, 1.390511439325337e-08, 1], [0.9282114505767822, 0.10875649750232697, 1.390511439325337e-08, 1], [0.9379969835281372, 0.11081668734550476, 1.390511439325337e-08, 1], [0.9477824568748474, 0.11287688463926315, 1.390511439325337e-08, 1], [0.9575679302215576, 0.11493708193302155, 1.390511439325337e-08, 1], [0.9534475207328796, 0.13450804352760315, 1.390511439325337e-08, 1], [0.9436620473861694, 0.13244783878326416, 1.390511439325337e-08, 1], [0.9338765740394592, 0.13038764894008636, 1.390511439325337e-08, 1], [0.924091100692749, 0.12832745909690857, 1.390511439325337e-08, 1], [0.9143056273460388, 0.12626725435256958, 1.390511439325337e-08, 1], [0.9045201539993286, 0.12420706450939178, 1.390511439325337e-08, 1], [0.8947346210479736, 0.12214686721563339, 1.390511439325337e-08, 1], [0.8849492073059082, 0.1200866773724556, 1.390511439325337e-08, 1], [0.8751636743545532, 0.11802647262811661, 1.390511439325337e-08, 1], [0.8653782606124878, 0.11596629023551941, 1.390511439325337e-08, 1], [0.8555927276611328, 0.11390608549118042, 1.390511439325337e-08, 1], [0.8458072543144226, 0.11184589564800262, 1.390511439325337e-08, 1], [0.8360217809677124, 0.10978569835424423, 1.390511439325337e-08, 1], [0.8262363076210022, 0.10772550851106644, 1.390511439325337e-08, 1], [0.816450834274292, 0.10566531121730804, 1.390511439325337e-08, 1], [0.8066653609275818, 0.10360511392354965, 1.390511439325337e-08, 1], [0.7968798875808716, 0.10154492408037186, 1.390511439325337e-08, 1], [0.7870943546295166, 0.09948472678661346, 1.390511439325337e-08, 1], [0.7773089408874512, 0.09742452949285507, 1.390511439325337e-08, 1], [0.7675234079360962, 0.09536433964967728, 1.390511439325337e-08, 1], [0.7577379941940308, 0.09330413490533829, 1.390511439325337e-08, 1], [0.7479524612426758, 0.09124395251274109, 1.390511439325337e-08, 1], [0.7381669878959656, 0.0891837477684021, 1.390511439325337e-08, 1], [0.7283815145492554, 0.0871235579252243, 1.390511439325337e-08, 1], [0.7185960412025452, 0.08506336808204651, 1.390511439325337e-08, 1], [0.708810567855835, 0.08300316333770752, 1.390511439325337e-08, 1], [0.6990250945091248, 0.08094297349452972, 1.390511439325337e-08, 1], [0.6892395615577698, 0.07888277620077133, 1.390511439325337e-08, 1], [0.6794541478157043, 0.07682258635759354, 1.390511439325337e-08, 1], [0.6696686744689941, 0.07476238906383514, 1.390511439325337e-08, 1], [0.6598831415176392, 0.07270219177007675, 1.390511439325337e-08, 1], [0.655762791633606, 0.09227315336465836, 1.390511439325337e-08, 1], [0.6655482649803162, 0.09433334320783615, 1.390511439325337e-08, 1], [0.6753337383270264, 0.09639354050159454, 1.390511439325337e-08, 1], [0.6851192116737366, 0.09845373779535294, 1.390511439325337e-08, 1], [0.6949046850204468, 0.10051392763853073, 1.390511439325337e-08, 1], [0.704690158367157, 0.10257413238286972, 1.390511439325337e-08, 1], [0.7144756317138672, 0.10463431477546692, 1.390511439325337e-08, 1], [0.7242611646652222, 0.10669451951980591, 1.390511439325337e-08, 1], [0.7340465784072876, 0.1087547093629837, 1.390511439325337e-08, 1], [0.7438321113586426, 0.1108149066567421, 1.390511439325337e-08, 1], [0.753617525100708, 0.11287509649991989, 1.390511439325337e-08, 1], [0.763403058052063, 0.11493529379367828, 1.390511439325337e-08, 1], [0.7731885313987732, 0.11699549108743668, 1.390511439325337e-08, 1], [0.7829740047454834, 0.11905568093061447, 1.390511439325337e-08, 1], [0.7927594780921936, 0.12111587822437286, 1.390511439325337e-08, 1], [0.8025449514389038, 0.12317607551813126, 1.390511439325337e-08, 1], [0.8123304843902588, 0.12523627281188965, 1.390511439325337e-08, 1], [0.8221158981323242, 0.12729646265506744, 1.390511439325337e-08, 1], [0.8319013714790344, 0.12935665249824524, 1.390511439325337e-08, 1], [0.8416869044303894, 0.13141685724258423, 1.390511439325337e-08, 1], [0.8514723181724548, 0.13347704708576202, 1.390511439325337e-08, 1], [0.8612578511238098, 0.13553723692893982, 1.390511439325337e-08, 1], [0.87104332447052, 0.1375974416732788, 1.390511439325337e-08, 1], [0.8808287978172302, 0.1396576315164566, 1.390511439325337e-08, 1], [0.8906142711639404, 0.1417178213596344, 1.390511439325337e-08, 1], [0.9003997445106506, 0.1437780261039734, 1.390511439325337e-08, 1], [0.9101852178573608, 0.14583821594715118, 1.390511439325337e-08, 1], [0.919970691204071, 0.14789840579032898, 1.390511439325337e-08, 1], [0.929756224155426, 0.14995861053466797, 1.390511439325337e-08, 1], [0.9395416378974915, 0.15201880037784576, 1.390511439325337e-08, 1], [0.9493271708488464, 0.15407900512218475, 1.390511439325337e-08, 1], [0.9452067613601685, 0.17364995181560516, 1.390511439325337e-08, 1], [0.9354212284088135, 0.17158974707126617, 1.390511439325337e-08, 1], [0.925635814666748, 0.16952957212924957, 1.390511439325337e-08, 1], [0.9158503413200378, 0.16746936738491058, 1.390511439325337e-08, 1], [0.9060648083686829, 0.1654091775417328, 1.390511439325337e-08, 1], [0.8962793946266174, 0.1633489727973938, 1.390511439325337e-08, 1], [0.8864938616752625, 0.161288782954216, 1.390511439325337e-08, 1], [0.8767083883285522, 0.1592285931110382, 1.390511439325337e-08, 1], [0.866922914981842, 0.1571684032678604, 1.390511439325337e-08, 1], [0.8571374416351318, 0.15510819852352142, 1.390511439325337e-08, 1], [0.8473519682884216, 0.15304800868034363, 1.390511439325337e-08, 1], [0.8375664949417114, 0.15098780393600464, 1.390511439325337e-08, 1], [0.8277810215950012, 0.14892761409282684, 1.390511439325337e-08, 1], [0.817995548248291, 0.14686742424964905, 1.390511439325337e-08, 1], [0.808210015296936, 0.14480721950531006, 1.390511439325337e-08, 1], [0.7984246015548706, 0.14274702966213226, 1.390511439325337e-08, 1], [0.7886390686035156, 0.14068683981895447, 1.390511439325337e-08, 1], [0.7788535952568054, 0.13862664997577667, 1.390511439325337e-08, 1], [0.76906818151474, 0.13656644523143768, 1.390511439325337e-08, 1], [0.759282648563385, 0.1345062553882599, 1.390511439325337e-08, 1], [0.7494971752166748, 0.1324460506439209, 1.390511439325337e-08, 1], [0.7397117018699646, 0.1303858608007431, 1.390511439325337e-08, 1], [0.7299262285232544, 0.1283256709575653, 1.390511439325337e-08, 1], [0.7201406955718994, 0.12626546621322632, 1.390511439325337e-08, 1], [0.710355281829834, 0.12420528382062912, 1.390511439325337e-08, 1], [0.700569748878479, 0.12214508652687073, 1.390511439325337e-08, 1], [0.6907843351364136, 0.12008488923311234, 1.390511439325337e-08, 1], [0.6809988021850586, 0.11802469193935394, 1.390511439325337e-08, 1], [0.6712133884429932, 0.11596449464559555, 1.390511439325337e-08, 1], [0.6614278554916382, 0.11390430480241776, 1.390511439325337e-08, 1], [0.651642382144928, 0.11184411495923996, 1.390511439325337e-08, 1], [0.64752197265625, 0.13141506910324097, 1.390511439325337e-08, 1], [0.657307505607605, 0.13347525894641876, 1.390511439325337e-08, 1], [0.6670929193496704, 0.13553544878959656, 1.390511439325337e-08, 1], [0.6768784523010254, 0.13759565353393555, 1.390511439325337e-08, 1], [0.6866639256477356, 0.13965584337711334, 1.390511439325337e-08, 1], [0.6964493989944458, 0.14171604812145233, 1.390511439325337e-08, 1], [0.706234872341156, 0.14377623796463013, 1.390511439325337e-08, 1], [0.7160203456878662, 0.14583642780780792, 1.390511439325337e-08, 1], [0.7258058190345764, 0.1478966325521469, 1.390511439325337e-08, 1], [0.7355912923812866, 0.1499568074941635, 1.390511439325337e-08, 1], [0.7453768253326416, 0.1520170271396637, 1.390511439325337e-08, 1], [0.755162239074707, 0.1540772020816803, 1.390511439325337e-08, 1], [0.764947772026062, 0.1561374068260193, 1.390511439325337e-08, 1], [0.7747331857681274, 0.15819759666919708, 1.390511439325337e-08, 1], [0.7845187187194824, 0.16025780141353607, 1.390511439325337e-08, 1], [0.7943041920661926, 0.16231799125671387, 1.390511439325337e-08, 1], [0.8040896654129028, 0.16437818109989166, 1.390511439325337e-08, 1], [0.813875138759613, 0.16643837094306946, 1.390511439325337e-08, 1], [0.8236606121063232, 0.16849857568740845, 1.390511439325337e-08, 1], [0.8334460854530334, 0.17055876553058624, 1.390511439325337e-08, 1], [0.8432315587997437, 0.17261897027492523, 1.390511439325337e-08, 1], [0.8530170917510986, 0.17467916011810303, 1.390511439325337e-08, 1], [0.8628025054931641, 0.17673934996128082, 1.390511439325337e-08, 1], [0.872588038444519, 0.1787995547056198, 1.390511439325337e-08, 1], [0.8823734521865845, 0.1808597296476364, 1.390511439325337e-08, 1], [0.8921589851379395, 0.1829199492931366, 1.390511439325337e-08, 1], [0.9019444584846497, 0.1849801242351532, 1.390511439325337e-08, 1], [0.9117299318313599, 0.1870403289794922, 1.390511439325337e-08, 1], [0.9215154051780701, 0.18910051882266998, 1.390511439325337e-08, 1], [0.9313008785247803, 0.19116072356700897, 1.390511439325337e-08, 1], [0.9410863518714905, 0.19322091341018677, 1.390511439325337e-08, 1], [0.9369660019874573, 0.21279186010360718, 1.390511439325337e-08, 1], [0.9271804690361023, 0.21073167026042938, 1.390511439325337e-08, 1], [0.9173950552940369, 0.2086714804172516, 1.390511439325337e-08, 1], [0.9076095223426819, 0.2066112905740738, 1.390511439325337e-08, 1], [0.8978240489959717, 0.2045510858297348, 1.390511439325337e-08, 1], [0.8880385756492615, 0.202490895986557, 1.390511439325337e-08, 1], [0.8782531023025513, 0.2004307061433792, 1.390511439325337e-08, 1], [0.8684676289558411, 0.19837050139904022, 1.390511439325337e-08, 1], [0.8586821556091309, 0.19631031155586243, 1.390511439325337e-08, 1], [0.8488966822624207, 0.19425012171268463, 1.390511439325337e-08, 1], [0.8391111493110657, 0.19218991696834564, 1.390511439325337e-08, 1], [0.8293257355690002, 0.19012972712516785, 1.390511439325337e-08, 1], [0.8195402026176453, 0.18806952238082886, 1.390511439325337e-08, 1], [0.8097547888755798, 0.18600934743881226, 1.390511439325337e-08, 1], [0.7999692559242249, 0.18394914269447327, 1.390511439325337e-08, 1], [0.7901837825775146, 0.18188893795013428, 1.390511439325337e-08, 1], [0.7803983092308044, 0.17982876300811768, 1.390511439325337e-08, 1], [0.7706128358840942, 0.1777685582637787, 1.390511439325337e-08, 1], [0.760827362537384, 0.1757083535194397, 1.390511439325337e-08, 1], [0.7510418891906738, 0.1736481636762619, 1.390511439325337e-08, 1], [0.7412563562393188, 0.1715879738330841, 1.390511439325337e-08, 1], [0.7314709424972534, 0.1695277839899063, 1.390511439325337e-08, 1], [0.7216854095458984, 0.16746757924556732, 1.390511439325337e-08, 1], [0.711899995803833, 0.16540738940238953, 1.390511439325337e-08, 1], [0.702114462852478, 0.16334719955921173, 1.390511439325337e-08, 1], [0.6923289895057678, 0.16128699481487274, 1.390511439325337e-08, 1], [0.6825435161590576, 0.15922680497169495, 1.390511439325337e-08, 1], [0.6727581024169922, 0.15716661512851715, 1.390511439325337e-08, 1], [0.6629725098609924, 0.15510641038417816, 1.390511439325337e-08, 1], [0.653187096118927, 0.15304622054100037, 1.390511439325337e-08, 1], [0.6434016227722168, 0.15098601579666138, 1.390511439325337e-08, 1], [0.6392812132835388, 0.17055699229240417, 1.390511439325337e-08, 1], [0.649066686630249, 0.17261718213558197, 1.390511439325337e-08, 1], [0.658852219581604, 0.17467737197875977, 1.390511439325337e-08, 1], [0.6686376333236694, 0.17673756182193756, 1.390511439325337e-08, 1], [0.6784231066703796, 0.17879776656627655, 1.390511439325337e-08, 1], [0.6882086396217346, 0.18085795640945435, 1.390511439325337e-08, 1], [0.6979941129684448, 0.18291814625263214, 1.390511439325337e-08, 1], [0.7077795267105103, 0.18497835099697113, 1.390511439325337e-08, 1], [0.7175650596618652, 0.18703854084014893, 1.390511439325337e-08, 1], [0.7273505330085754, 0.18909873068332672, 1.390511439325337e-08, 1], [0.7371360063552856, 0.1911589354276657, 1.390511439325337e-08, 1], [0.7469214797019958, 0.1932191252708435, 1.390511439325337e-08, 1], [0.756706953048706, 0.1952793151140213, 1.390511439325337e-08, 1], [0.766492486000061, 0.1973395198583603, 1.390511439325337e-08, 1], [0.7762778997421265, 0.19939970970153809, 1.390511439325337e-08, 1], [0.7860634326934814, 0.20145989954471588, 1.390511439325337e-08, 1], [0.7958488464355469, 0.20352010428905487, 1.390511439325337e-08, 1], [0.8056343793869019, 0.20558029413223267, 1.390511439325337e-08, 1], [0.8154198527336121, 0.20764048397541046, 1.390511439325337e-08, 1], [0.8252052664756775, 0.20970068871974945, 1.390511439325337e-08, 1], [0.9328455924987793, 0.23236282169818878, 1.390511439325337e-08, 1], [0.7134446501731873, 0.20660950243473053, 1.390511439325337e-08, 1], [0.703659176826477, 0.20454929769039154, 1.390511439325337e-08, 1], [0.6938737034797668, 0.20248910784721375, 1.390511439325337e-08, 1], [0.6840882301330566, 0.20042891800403595, 1.390511439325337e-08, 1], [0.6743027567863464, 0.19836872816085815, 1.390511439325337e-08, 1], [0.6645172834396362, 0.19630852341651917, 1.390511439325337e-08, 1], [0.6547317504882812, 0.19424833357334137, 1.390511439325337e-08, 1], [0.6449463367462158, 0.19218812882900238, 1.390511439325337e-08, 1], [0.6351608037948608, 0.19012793898582458, 1.390511439325337e-08, 1], [0.6310404539108276, 0.2096989005804062, 1.390511439325337e-08, 1]]
\ No newline at end of file
diff --git a/probe_vis_data_r0_180.json b/probe_vis_data_r0_180.json
new file mode 100644
index 0000000..a43121c
--- /dev/null
+++ b/probe_vis_data_r0_180.json
@@ -0,0 +1 @@
           1 +[[0.7052074670791626, -0.1425783336162567, -3.1415927410125732, 0], [0.7149929404258728, -0.14051814377307892, -3.1415927410125732, 0], [0.724778413772583, -0.13845795392990112, -3.1415927410125732, 0], [0.7345638871192932, -0.13639776408672333, -3.1415927410125732, 0], [0.7443493604660034, -0.13433755934238434, -3.1415927410125732, 0], [0.7541348338127136, -0.13227736949920654, -3.1415927410125732, 0], [0.7639203667640686, -0.13021717965602875, -3.1415927410125732, 0], [0.773705780506134, -0.12815697491168976, -3.1415927410125732, 0], [0.783491313457489, -0.12609678506851196, -3.1415927410125732, 0], [0.7932767271995544, -0.12403658777475357, -3.1415927410125732, 0], [0.8030622601509094, -0.12197639048099518, -3.1415927410125732, 0], [0.8128477334976196, -0.11991620063781738, -3.1415927410125732, 0], [0.8226331472396851, -0.11785600334405899, -3.1415927410125732, 0], [0.83241868019104, -0.1157958135008812, -3.1415927410125732, 0], [0.8422041535377502, -0.1137356087565422, -3.1415927410125732, 0], [0.8519896864891052, -0.11167542636394501, -3.1415927410125732, 0], [0.8617751002311707, -0.10961522161960602, -3.1415927410125732, 0], [0.8715605735778809, -0.10755503177642822, -3.1415927410125732, 0], [0.8813461065292358, -0.10549483448266983, -3.1415927410125732, 0], [0.8911315202713013, -0.10343464463949203, -3.1415927410125732, 0], [0.9009170532226562, -0.10137443989515305, -3.1415927410125732, 0], [0.9107025265693665, -0.09931425005197525, -3.1415927410125732, 0], [0.9204879403114319, -0.09725406020879745, -3.1415927410125732, 0], [0.9302734732627869, -0.09519386291503906, -3.1415927410125732, 0], [0.9400589466094971, -0.09313366562128067, -3.1415927410125732, 0], [0.9498444199562073, -0.09107346832752228, -3.1415927410125732, 0], [0.9596298933029175, -0.08901327848434448, -3.1415927410125732, 0], [0.9694154262542725, -0.08695308119058609, -3.1415927410125732, 0], [0.9792008399963379, -0.0848928913474083, -3.1415927410125732, 0], [0.9889863729476929, -0.0828326940536499, -3.1415927410125732, 0], [0.9987717866897583, -0.08077249675989151, -3.1415927410125732, 0], [0.9946514368057251, -0.061201538890600204, -3.1415927410125732, 0], [0.9848659634590149, -0.0632617324590683, -3.1415927410125732, 0], [0.9750804305076599, -0.06532192975282669, -3.1415927410125732, 0], [0.9652950167655945, -0.06738212704658508, -3.1415927410125732, 1], [0.9555095434188843, -0.06944231688976288, -3.1415927410125732, 1], [0.9457240104675293, -0.07150251418352127, -3.1415927410125732, 1], [0.9359385371208191, -0.07356271147727966, -3.1415927410125732, 1], [0.9261531233787537, -0.07562290132045746, -3.1415927410125732, 1], [0.9163675904273987, -0.07768309861421585, -3.1415927410125732, 1], [0.9065821170806885, -0.07974329590797424, -3.1415927410125732, 1], [0.8967966437339783, -0.08180348575115204, -3.1415927410125732, 1], [0.8870111703872681, -0.08386368304491043, -3.1415927410125732, 1], [0.8772256374359131, -0.08592388033866882, -3.1415927410125732, 1], [0.8674402236938477, -0.08798407018184662, -3.1415927410125732, 1], [0.8576547503471375, -0.09004426747560501, -3.1415927410125732, 1], [0.8478692173957825, -0.0921044647693634, -3.1415927410125732, 0], [0.8380837440490723, -0.0941646546125412, -3.1415927410125732, 0], [0.8282983303070068, -0.09622485190629959, -3.1415927410125732, 0], [0.8185127973556519, -0.09828504920005798, -3.1415927410125732, 0], [0.8087273240089417, -0.10034523904323578, -3.1415927410125732, 0], [0.7989418506622314, -0.10240543633699417, -3.1415927410125732, 0], [0.7891563773155212, -0.10446563363075256, -3.1415927410125732, 0], [0.779370903968811, -0.10652582347393036, -3.1415927410125732, 0], [0.7695854306221008, -0.10858602076768875, -3.1415927410125732, 0], [0.7597998976707458, -0.11064621806144714, -3.1415927410125732, 0], [0.7500144839286804, -0.11270640790462494, -3.1415927410125732, 0], [0.7402289509773254, -0.11476660519838333, -3.1415927410125732, 0], [0.73044353723526, -0.11682680249214172, -3.1415927410125732, 0], [0.720658004283905, -0.11888699233531952, -3.1415927410125732, 0], [0.7108725309371948, -0.12094718962907791, -3.1415927410125732, 0], [0.7010870575904846, -0.1230073869228363, -3.1415927410125732, 0], [0.6969667077064514, -0.1034364253282547, -3.1415927410125732, 0], [0.7067521214485168, -0.1013762354850769, -3.1415927410125732, 0], [0.7165376543998718, -0.09931603819131851, -3.1415927410125732, 0], [0.7263230681419373, -0.09725584089756012, -3.1415927410125732, 0], [0.7361086010932922, -0.09519564360380173, -3.1415927410125732, 0], [0.7458940744400024, -0.09313545376062393, -3.1415927410125732, 0], [0.7556795477867126, -0.09107525646686554, -3.1415927410125732, 0], [0.7654650211334229, -0.08901506662368774, -3.1415927410125732, 0], [0.7752504944801331, -0.08695486932992935, -3.1415927410125732, 0], [0.785036027431488, -0.08489467203617096, -3.1415927410125732, 0], [0.7948214411735535, -0.08283447474241257, -3.1415927410125732, 0], [0.8046069145202637, -0.08077428489923477, -3.1415927410125732, 0], [0.8143924474716187, -0.07871408760547638, -3.1415927410125732, 0], [0.8241779208183289, -0.07665389776229858, -3.1415927410125732, 0], [0.8339633345603943, -0.07459370046854019, -3.1415927410125732, 0], [0.8437488675117493, -0.0725335031747818, -3.1415927410125732, 0], [0.8535343408584595, -0.07047330588102341, -3.1415927410125732, 1], [0.8633198142051697, -0.06841311603784561, -3.1415927410125732, 1], [0.8731052875518799, -0.06635291874408722, -3.1415927410125732, 1], [0.8828907608985901, -0.06429272890090942, -3.1415927410125732, 1], [0.8926762938499451, -0.06223252788186073, -3.1415927410125732, 1], [0.9024617075920105, -0.06017233803868294, -3.1415927410125732, 1], [0.9122471809387207, -0.058112140744924545, -3.1415927410125732, 1], [0.9220327138900757, -0.05605194345116615, -3.1415927410125732, 1], [0.9318181872367859, -0.05399175360798836, -3.1415927410125732, 1], [0.9416036009788513, -0.051931556314229965, -3.1415927410125732, 1], [0.9513891339302063, -0.04987135902047157, -3.1415927410125732, 1], [0.9611746072769165, -0.04781116917729378, -3.1415927410125732, 1], [0.9709600806236267, -0.045750971883535385, -3.1415927410125732, 1], [0.9807455539703369, -0.04369077458977699, -3.1415927410125732, 1], [0.9905310869216919, -0.0416305847465992, -3.1415927410125732, 1], [0.9864106178283691, -0.022059623152017593, -3.1415927410125732, 1], [0.9766252040863037, -0.024119820445775986, -3.1415927410125732, 1], [0.9668396711349487, -0.02618001401424408, -3.1415927410125732, 1], [0.9570541977882385, -0.028240209445357323, -3.1415927410125732, 1], [0.9472687244415283, -0.030300403013825417, -3.1415927410125732, 1], [0.9374832510948181, -0.03236059844493866, -3.1415927410125732, 1], [0.9276977777481079, -0.034420792013406754, -3.1415927410125732, 1], [0.9179123044013977, -0.036480989307165146, -3.1415927410125732, 1], [0.9081268310546875, -0.03854118287563324, -3.1415927410125732, 1], [0.8983413577079773, -0.04060138016939163, -3.1415927410125732, 1], [0.8885558247566223, -0.04266157001256943, -3.1415927410125732, 1], [0.8787704110145569, -0.04472176730632782, -3.1415927410125732, 1], [0.8689848780632019, -0.04678196460008621, -3.1415927410125732, 1], [0.8591994643211365, -0.04884215444326401, -3.1415927410125732, 1], [0.8494139313697815, -0.0509023517370224, -3.1415927410125732, 1], [0.8396284580230713, -0.05296254903078079, -3.1415927410125732, 0], [0.8298429846763611, -0.05502273887395859, -3.1415927410125732, 0], [0.8200575113296509, -0.05708293616771698, -3.1415927410125732, 0], [0.8102720379829407, -0.05914313346147537, -3.1415927410125732, 0], [0.8004865646362305, -0.06120332330465317, -3.1415927410125732, 0], [0.7907010316848755, -0.06326352059841156, -3.1415927410125732, 0], [0.7809156179428101, -0.06532371789216995, -3.1415927410125732, 0], [0.7711301445960999, -0.06738390773534775, -3.1415927410125732, 0], [0.7613446116447449, -0.06944410502910614, -3.1415927410125732, 0], [0.7515591382980347, -0.07150430232286453, -3.1415927410125732, 0], [0.7417737245559692, -0.07356449216604233, -3.1415927410125732, 0], [0.7319881916046143, -0.07562468945980072, -3.1415927410125732, 0], [0.722202718257904, -0.07768488675355911, -3.1415927410125732, 0], [0.7124172449111938, -0.07974507659673691, -3.1415927410125732, 0], [0.7026317119598389, -0.0818052738904953, -3.1415927410125732, 0], [0.6928462982177734, -0.08386547118425369, -3.1415927410125732, 0], [0.6887258887290955, -0.06429450958967209, -3.1415927410125732, 0], [0.6985113620758057, -0.062234316021203995, -3.1415927410125732, 0], [0.7082968950271606, -0.0601741224527359, -3.1415927410125732, 0], [0.7180823087692261, -0.05811392515897751, -3.1415927410125732, 0], [0.727867841720581, -0.056053731590509415, -3.1415927410125732, 0], [0.7376532554626465, -0.05399353802204132, -3.1415927410125732, 0], [0.7474387884140015, -0.05193334445357323, -3.1415927410125732, 0], [0.7572242021560669, -0.049873147159814835, -3.1415927410125732, 0], [0.7670097351074219, -0.04781294986605644, -3.1415927410125732, 0], [0.7767952084541321, -0.04575276002287865, -3.1415927410125732, 0], [0.7865806818008423, -0.043692562729120255, -3.1415927410125732, 0], [0.7963661551475525, -0.04163236543536186, -3.1415927410125732, 0], [0.8061516880989075, -0.03957217559218407, -3.1415927410125732, 0], [0.8159371018409729, -0.037511978298425674, -3.1415927410125732, 0], [0.8257225751876831, -0.03545178100466728, -3.1415927410125732, 0], [0.8355081081390381, -0.03339159116148949, -3.1415927410125732, 0], [0.8452935218811035, -0.031331393867731094, -3.1415927410125732, 1], [0.8550790548324585, -0.02927119843661785, -3.1415927410125732, 1], [0.8648645281791687, -0.027211004868149757, -3.1415927410125732, 1], [0.8746500015258789, -0.025150809437036514, -3.1415927410125732, 1], [0.8844354748725891, -0.02309061400592327, -3.1415927410125732, 1], [0.8942209482192993, -0.021030420437455177, -3.1415927410125732, 1], [0.9040064215660095, -0.018970225006341934, -3.1415927410125732, 1], [0.9137918949127197, -0.01691003143787384, -3.1415927410125732, 1], [0.9235773682594299, -0.014849835075438023, -3.1415927410125732, 1], [0.9333629012107849, -0.012789640575647354, -3.1415927410125732, 1], [0.9431483149528503, -0.010729446075856686, -3.1415927410125732, 1], [0.9529338479042053, -0.008669251576066017, -3.1415927410125732, 1], [0.9627193212509155, -0.006609056144952774, -3.1415927410125732, 1], [0.972504734992981, -0.0045488616451621056, -3.1415927410125732, 1], [0.9822902679443359, -0.002488666446879506, -3.1415927410125732, 1], [0.978169858455658, 0.01708229072391987, -3.1415927410125732, 1], [0.9683844447135925, 0.015022097155451775, -3.1415927410125732, 1], [0.9585989117622375, 0.012961900793015957, -3.1415927410125732, 1], [0.9488134384155273, 0.010901707224547863, -3.1415927410125732, 1], [0.9390279054641724, 0.00884151179343462, -3.1415927410125732, 1], [0.9292424917221069, 0.006781316827982664, -3.1415927410125732, 1], [0.9194570183753967, 0.004721122328191996, -3.1415927410125732, 1], [0.9096714854240417, 0.0026609275955706835, -3.1415927410125732, 1], [0.8998860716819763, 0.0006007325137034059, -3.1415927410125732, 1], [0.8901005387306213, -0.0014594622189179063, -3.1415927410125732, 1], [0.8803150653839111, -0.0035196568351238966, -3.1415927410125732, 1], [0.8705296516418457, -0.005579852033406496, -3.1415927410125732, 1], [0.8607441186904907, -0.0076400465331971645, -3.1415927410125732, 1], [0.8509586453437805, -0.00970024149864912, -3.1415927410125732, 1], [0.8411731719970703, -0.011760435998439789, -3.1415927410125732, 1], [0.8313876390457153, -0.013820631429553032, -3.1415927410125732, 0], [0.8216022253036499, -0.015880824998021126, -3.1415927410125732, 0], [0.8118167519569397, -0.01794102042913437, -3.1415927410125732, 0], [0.8020312190055847, -0.020001215860247612, -3.1415927410125732, 0], [0.7922458052635193, -0.022061411291360855, -3.1415927410125732, 0], [0.7824602723121643, -0.02412160485982895, -3.1415927410125732, 0], [0.7726747989654541, -0.026181800290942192, -3.1415927410125732, 0], [0.7628893852233887, -0.028241993859410286, -3.1415927410125732, 0], [0.7531038522720337, -0.03030218929052353, -3.1415927410125732, 0], [0.7433183789253235, -0.03236238285899162, -3.1415927410125732, 0], [0.7335329055786133, -0.034422580152750015, -3.1415927410125732, 0], [0.7237473726272583, -0.03648277372121811, -3.1415927410125732, 0], [0.7139619588851929, -0.0385429710149765, -3.1415927410125732, 0], [0.7041764855384827, -0.0406031608581543, -3.1415927410125732, 0], [0.6943909525871277, -0.04266335815191269, -3.1415927410125732, 0], [0.6846055388450623, -0.04472355544567108, -3.1415927410125732, 0], [0.6804850697517395, -0.025152593851089478, -3.1415927410125732, 0], [0.6902706027030945, -0.023092400282621384, -3.1415927410125732, 0], [0.7000560760498047, -0.02103220671415329, -3.1415927410125732, 0], [0.7098415493965149, -0.018972011283040047, -3.1415927410125732, 0], [0.7196270227432251, -0.016911815851926804, -3.1415927410125732, 0], [0.7294125556945801, -0.014851621352136135, -3.1415927410125732, 0], [0.7391979694366455, -0.012791425921022892, -3.1415927410125732, 0], [0.7489834427833557, -0.010731231421232224, -3.1415927410125732, 0], [0.7587689757347107, -0.008671036921441555, -3.1415927410125732, 0], [0.7685543894767761, -0.0066108424216508865, -3.1415927410125732, 0], [0.7783399224281311, -0.004550646990537643, -3.1415927410125732, 0], [0.7881253957748413, -0.002490452490746975, -3.1415927410125732, 0], [0.7979108691215515, -0.0004302576126065105, -3.1415927410125732, 0], [0.8076963424682617, 0.0016299370909109712, -3.1415927410125732, 0], [0.8174818158149719, 0.003690132172778249, -3.1415927410125732, 0], [0.8272672891616821, 0.005750326439738274, -3.1415927410125732, 0], [0.8370527625083923, 0.007810521870851517, -3.1415927410125732, 1], [0.8468382358551025, 0.009870716370642185, -3.1415927410125732, 1], [0.8566237688064575, 0.011930910870432854, -3.1415927410125732, 1], [0.866409182548523, 0.013991106301546097, -3.1415927410125732, 1], [0.8761947154998779, 0.01605129987001419, -3.1415927410125732, 1], [0.8859801888465881, 0.018111497163772583, -3.1415927410125732, 1], [0.8957656621932983, 0.020171688869595528, -3.1415927410125732, 1], [0.9055511355400085, 0.02223188616335392, -3.1415927410125732, 1], [0.915336549282074, 0.024292079731822014, -3.1415927410125732, 1], [0.9251221418380737, 0.026352275162935257, -3.1415927410125732, 1], [0.9349075555801392, 0.02841246873140335, -3.1415927410125732, 1], [0.9446930289268494, 0.030472666025161743, -3.1415927410125732, 1], [0.9544785022735596, 0.03253285959362984, -3.1415927410125732, 1], [0.9642640352249146, 0.03459305316209793, -3.1415927410125732, 1], [0.97404944896698, 0.03665325045585632, -3.1415927410125732, 1], [0.9699290990829468, 0.05622420459985733, -3.1415927410125732, 1], [0.9601436257362366, 0.054164011031389236, -3.1415927410125732, 1], [0.9503581523895264, 0.05210381746292114, -3.1415927410125732, 1], [0.9405726194381714, 0.05004362389445305, -3.1415927410125732, 1], [0.930787205696106, 0.047983426600694656, -3.1415927410125732, 1], [0.921001672744751, 0.04592323303222656, -3.1415927410125732, 1], [0.9112162590026855, 0.04386303573846817, -3.1415927410125732, 1], [0.9014307260513306, 0.041802845895290375, -3.1415927410125732, 1], [0.8916452527046204, 0.03974264860153198, -3.1415927410125732, 1], [0.8818597793579102, 0.03768245130777359, -3.1415927410125732, 1], [0.8720743060112, 0.035622257739305496, -3.1415927410125732, 1], [0.8622888326644897, 0.0335620641708374, -3.1415927410125732, 1], [0.8525033593177795, 0.03150187060236931, -3.1415927410125732, 1], [0.8427178263664246, 0.029441673308610916, -3.1415927410125732, 1], [0.8329324126243591, 0.027381479740142822, -3.1415927410125732, 1], [0.8231468796730042, 0.02532128430902958, -3.1415927410125732, 0], [0.8133614659309387, 0.023261090740561485, -3.1415927410125732, 0], [0.8035759329795837, 0.021200893446803093, -3.1415927410125732, 0], [0.7937904596328735, 0.01914070174098015, -3.1415927410125732, 0], [0.7840049862861633, 0.017080504447221756, -3.1415927410125732, 0], [0.7742195129394531, 0.015020310878753662, -3.1415927410125732, 0], [0.7644340395927429, 0.012960115447640419, -3.1415927410125732, 0], [0.7546485662460327, 0.01089992094784975, -3.1415927410125732, 0], [0.7448630928993225, 0.008839726448059082, -3.1415927410125732, 0], [0.7350775599479675, 0.006779531016945839, -3.1415927410125732, 0], [0.7252921462059021, 0.0047193365171551704, -3.1415927410125732, 0], [0.7155066132545471, 0.002659142017364502, -3.1415927410125732, 0], [0.7057211995124817, 0.0005989467026665807, -3.1415927410125732, 0], [0.6959356665611267, -0.0014612477971240878, -3.1415927410125732, 0], [0.6861501932144165, -0.0035214426461607218, -3.1415927410125732, 0], [0.6763647198677063, -0.005581637378782034, -3.1415927410125732, 0], [0.6722443699836731, 0.013989320024847984, -3.1415927410125732, 0], [0.6820297837257385, 0.016049515455961227, -3.1415927410125732, 0], [0.6918153166770935, 0.01810971088707447, -3.1415927410125732, 0], [0.7016007900238037, 0.020169904455542564, -3.1415927410125732, 0], [0.7113862037658691, 0.022230098024010658, -3.1415927410125732, 0], [0.7211717367172241, 0.02429029531776905, -3.1415927410125732, 0], [0.7309572100639343, 0.026350488886237144, -3.1415927410125732, 0], [0.7407426834106445, 0.028410684317350388, -3.1415927410125732, 0], [0.7505282163619995, 0.03047087788581848, -3.1415927410125732, 0], [0.7603136301040649, 0.032531075179576874, -3.1415927410125732, 0], [0.7700991034507751, 0.03459126874804497, -3.1415927410125732, 0], [0.7798846364021301, 0.03665146231651306, -3.1415927410125732, 0], [0.7896700501441956, 0.038711655884981155, -3.1415927410125732, 0], [0.7994555830955505, 0.04077185317873955, -3.1415927410125732, 0], [0.8092410564422607, 0.04283205047249794, -3.1415927410125732, 0], [0.8190264701843262, 0.044892240315675735, -3.1415927410125732, 0], [0.8288120031356812, 0.04695243760943413, -3.1415927410125732, 1], [0.8385974764823914, 0.04901263117790222, -3.1415927410125732, 1], [0.8483829498291016, 0.051072828471660614, -3.1415927410125732, 1], [0.8581684827804565, 0.05313302204012871, -3.1415927410125732, 1], [0.867953896522522, 0.0551932156085968, -3.1415927410125732, 1], [0.8777393698692322, 0.057253409177064896, -3.1415927410125732, 1], [0.8875249028205872, 0.05931360647082329, -3.1415927410125732, 1], [0.8973103165626526, 0.06137380376458168, -3.1415927410125732, 1], [0.9070958495140076, 0.06343399733304977, -3.1415927410125732, 1], [0.9168813228607178, 0.06549418717622757, -3.1415927410125732, 1], [0.9266667366027832, 0.06755438446998596, -3.1415927410125732, 1], [0.9364522695541382, 0.06961458176374435, -3.1415927410125732, 1], [0.9462377429008484, 0.07167477160692215, -3.1415927410125732, 1], [0.9560232758522034, 0.07373496890068054, -3.1415927410125732, 1], [0.9658086895942688, 0.07579516619443893, -3.1415927410125732, 1], [0.9616882801055908, 0.09536612033843994, -3.1415927410125732, 1], [0.9519028663635254, 0.09330593049526215, -3.1415927410125732, 1], [0.9421173334121704, 0.09124573320150375, -3.1415927410125732, 1], [0.9323318600654602, 0.08918553590774536, -3.1415927410125732, 1], [0.9225464463233948, 0.08712534606456757, -3.1415927410125732, 1], [0.9127609133720398, 0.08506514877080917, -3.1415927410125732, 1], [0.9029754400253296, 0.08300495147705078, -3.1415927410125732, 1], [0.8931899666786194, 0.08094476163387299, -3.1415927410125732, 1], [0.8834044337272644, 0.0788845643401146, -3.1415927410125732, 1], [0.873619019985199, 0.0768243670463562, -3.1415927410125732, 1], [0.8638335466384888, 0.07476416975259781, -3.1415927410125732, 1], [0.8540480136871338, 0.07270397990942001, -3.1415927410125732, 1], [0.8442625999450684, 0.07064379006624222, -3.1415927410125732, 1], [0.8344770669937134, 0.06858358532190323, -3.1415927410125732, 1], [0.8246915936470032, 0.06652339547872543, -3.1415927410125732, 1], [0.814906120300293, 0.06446319818496704, -3.1415927410125732, 0], [0.8051207065582275, 0.062403008341789246, -3.1415927410125732, 0], [0.7953351140022278, 0.06034281104803085, -3.1415927410125732, 0], [0.7855497002601624, 0.05828261375427246, -3.1415927410125732, 0], [0.7757642269134521, 0.056222423911094666, -3.1415927410125732, 0], [0.7659787535667419, 0.05416222661733627, -3.1415927410125732, 0], [0.756193220615387, 0.05210202932357788, -3.1415927410125732, 0], [0.7464078068733215, 0.05004183575510979, -3.1415927410125732, 0], [0.7366222739219666, 0.04798164218664169, -3.1415927410125732, 0], [0.7268368601799011, 0.0459214486181736, -3.1415927410125732, 0], [0.7170513272285461, 0.04386125132441521, -3.1415927410125732, 0], [0.7072658538818359, 0.04180105775594711, -3.1415927410125732, 0], [0.6974803805351257, 0.03974086046218872, -3.1415927410125732, 0], [0.6876949071884155, 0.037680670619010925, -3.1415927410125732, 0], [0.6779094338417053, 0.03562047332525253, -3.1415927410125732, 0], [0.6681239604949951, 0.03356027603149414, -3.1415927410125732, 0], [0.6640035510063171, 0.053131237626075745, -3.1415927410125732, 0], [0.6737890243530273, 0.05519142746925354, -3.1415927410125732, 0], [0.6835744976997375, 0.05725162848830223, -3.1415927410125732, 0], [0.6933599710464478, 0.059311818331480026, -3.1415927410125732, 0], [0.7031455039978027, 0.06137201562523842, -3.1415927410125732, 0], [0.7129309177398682, 0.06343220919370651, -3.1415927410125732, 0], [0.7227164506912231, 0.0654924064874649, -3.1415927410125732, 0], [0.7325019240379333, 0.0675525963306427, -3.1415927410125732, 0], [0.7422873973846436, 0.06961279362440109, -3.1415927410125732, 0], [0.7520728707313538, 0.07167299091815948, -3.1415927410125732, 0], [0.761858344078064, 0.07373318821191788, -3.1415927410125732, 0], [0.7716438174247742, 0.07579337805509567, -3.1415927410125732, 0], [0.7814292907714844, 0.07785357534885406, -3.1415927410125732, 0], [0.7912147641181946, 0.07991376519203186, -3.1415927410125732, 0], [0.8010002970695496, 0.08197396248579025, -3.1415927410125732, 0], [0.810785710811615, 0.08403415977954865, -3.1415927410125732, 1], [0.82057124376297, 0.08609434962272644, -3.1415927410125732, 1], [0.8303566575050354, 0.08815454691648483, -3.1415927410125732, 1], [0.8401421904563904, 0.09021474421024323, -3.1415927410125732, 1], [0.8499276638031006, 0.09227494150400162, -3.1415927410125732, 1], [0.8597131371498108, 0.09433513134717941, -3.1415927410125732, 1], [0.869498610496521, 0.09639532119035721, -3.1415927410125732, 1], [0.8792840838432312, 0.0984555259346962, -3.1415927410125732, 1], [0.8890695571899414, 0.10051571577787399, -3.1415927410125732, 1], [0.8988550901412964, 0.10257591307163239, -3.1415927410125732, 1], [0.9086405038833618, 0.10463610291481018, -3.1415927410125732, 1], [0.9184260368347168, 0.10669630020856857, -3.1415927410125732, 1], [0.9282114505767822, 0.10875649750232697, -3.1415927410125732, 1], [0.9379969835281372, 0.11081668734550476, -3.1415927410125732, 1], [0.9477824568748474, 0.11287688463926315, -3.1415927410125732, 1], [0.9575679302215576, 0.11493708193302155, -3.1415927410125732, 1], [0.9534475207328796, 0.13450804352760315, -3.1415927410125732, 1], [0.9436620473861694, 0.13244783878326416, -3.1415927410125732, 1], [0.9338765740394592, 0.13038764894008636, -3.1415927410125732, 1], [0.924091100692749, 0.12832745909690857, -3.1415927410125732, 1], [0.9143056273460388, 0.12626725435256958, -3.1415927410125732, 1], [0.9045201539993286, 0.12420706450939178, -3.1415927410125732, 1], [0.8947346210479736, 0.12214686721563339, -3.1415927410125732, 1], [0.8849492073059082, 0.1200866773724556, -3.1415927410125732, 1], [0.8751636743545532, 0.11802647262811661, -3.1415927410125732, 1], [0.8653782606124878, 0.11596629023551941, -3.1415927410125732, 1], [0.8555927276611328, 0.11390608549118042, -3.1415927410125732, 1], [0.8458072543144226, 0.11184589564800262, -3.1415927410125732, 1], [0.8360217809677124, 0.10978569835424423, -3.1415927410125732, 1], [0.8262363076210022, 0.10772550851106644, -3.1415927410125732, 1], [0.816450834274292, 0.10566531121730804, -3.1415927410125732, 1], [0.8066653609275818, 0.10360511392354965, -3.1415927410125732, 1], [0.7968798875808716, 0.10154492408037186, -3.1415927410125732, 0], [0.7870943546295166, 0.09948472678661346, -3.1415927410125732, 0], [0.7773089408874512, 0.09742452949285507, -3.1415927410125732, 0], [0.7675234079360962, 0.09536433964967728, -3.1415927410125732, 0], [0.7577379941940308, 0.09330413490533829, -3.1415927410125732, 0], [0.7479524612426758, 0.09124395251274109, -3.1415927410125732, 0], [0.7381669878959656, 0.0891837477684021, -3.1415927410125732, 0], [0.7283815145492554, 0.0871235579252243, -3.1415927410125732, 0], [0.7185960412025452, 0.08506336808204651, -3.1415927410125732, 0], [0.708810567855835, 0.08300316333770752, -3.1415927410125732, 0], [0.6990250945091248, 0.08094297349452972, -3.1415927410125732, 0], [0.6892395615577698, 0.07888277620077133, -3.1415927410125732, 0], [0.6794541478157043, 0.07682258635759354, -3.1415927410125732, 0], [0.6696686744689941, 0.07476238906383514, -3.1415927410125732, 0], [0.6598831415176392, 0.07270219177007675, -3.1415927410125732, 0], [0.655762791633606, 0.09227315336465836, -3.1415927410125732, 0], [0.6655482649803162, 0.09433334320783615, -3.1415927410125732, 0], [0.6753337383270264, 0.09639354050159454, -3.1415927410125732, 0], [0.6851192116737366, 0.09845373779535294, -3.1415927410125732, 0], [0.6949046850204468, 0.10051392763853073, -3.1415927410125732, 0], [0.704690158367157, 0.10257413238286972, -3.1415927410125732, 0], [0.7144756317138672, 0.10463431477546692, -3.1415927410125732, 0], [0.7242611646652222, 0.10669451951980591, -3.1415927410125732, 0], [0.7340465784072876, 0.1087547093629837, -3.1415927410125732, 0], [0.7438321113586426, 0.1108149066567421, -3.1415927410125732, 0], [0.753617525100708, 0.11287509649991989, -3.1415927410125732, 0], [0.763403058052063, 0.11493529379367828, -3.1415927410125732, 0], [0.7731885313987732, 0.11699549108743668, -3.1415927410125732, 0], [0.7829740047454834, 0.11905568093061447, -3.1415927410125732, 0], [0.7927594780921936, 0.12111587822437286, -3.1415927410125732, 0], [0.8025449514389038, 0.12317607551813126, -3.1415927410125732, 1], [0.8123304843902588, 0.12523627281188965, -3.1415927410125732, 1], [0.8221158981323242, 0.12729646265506744, -3.1415927410125732, 1], [0.8319013714790344, 0.12935665249824524, -3.1415927410125732, 1], [0.8416869044303894, 0.13141685724258423, -3.1415927410125732, 1], [0.8514723181724548, 0.13347704708576202, -3.1415927410125732, 1], [0.8612578511238098, 0.13553723692893982, -3.1415927410125732, 1], [0.87104332447052, 0.1375974416732788, -3.1415927410125732, 1], [0.8808287978172302, 0.1396576315164566, -3.1415927410125732, 1], [0.8906142711639404, 0.1417178213596344, -3.1415927410125732, 1], [0.9003997445106506, 0.1437780261039734, -3.1415927410125732, 1], [0.9101852178573608, 0.14583821594715118, -3.1415927410125732, 1], [0.919970691204071, 0.14789840579032898, -3.1415927410125732, 1], [0.929756224155426, 0.14995861053466797, -3.1415927410125732, 1], [0.9395416378974915, 0.15201880037784576, -3.1415927410125732, 1], [0.9493271708488464, 0.15407900512218475, -3.1415927410125732, 1], [0.9452067613601685, 0.17364995181560516, -3.1415927410125732, 1], [0.9354212284088135, 0.17158974707126617, -3.1415927410125732, 1], [0.925635814666748, 0.16952957212924957, -3.1415927410125732, 1], [0.9158503413200378, 0.16746936738491058, -3.1415927410125732, 1], [0.9060648083686829, 0.1654091775417328, -3.1415927410125732, 1], [0.8962793946266174, 0.1633489727973938, -3.1415927410125732, 1], [0.8864938616752625, 0.161288782954216, -3.1415927410125732, 1], [0.8767083883285522, 0.1592285931110382, -3.1415927410125732, 1], [0.866922914981842, 0.1571684032678604, -3.1415927410125732, 1], [0.8571374416351318, 0.15510819852352142, -3.1415927410125732, 1], [0.8473519682884216, 0.15304800868034363, -3.1415927410125732, 1], [0.8375664949417114, 0.15098780393600464, -3.1415927410125732, 1], [0.8277810215950012, 0.14892761409282684, -3.1415927410125732, 1], [0.817995548248291, 0.14686742424964905, -3.1415927410125732, 1], [0.808210015296936, 0.14480721950531006, -3.1415927410125732, 1], [0.7984246015548706, 0.14274702966213226, -3.1415927410125732, 1], [0.7886390686035156, 0.14068683981895447, -3.1415927410125732, 0], [0.7788535952568054, 0.13862664997577667, -3.1415927410125732, 0], [0.76906818151474, 0.13656644523143768, -3.1415927410125732, 0], [0.759282648563385, 0.1345062553882599, -3.1415927410125732, 0], [0.7494971752166748, 0.1324460506439209, -3.1415927410125732, 0], [0.7397117018699646, 0.1303858608007431, -3.1415927410125732, 0], [0.7299262285232544, 0.1283256709575653, -3.1415927410125732, 0], [0.7201406955718994, 0.12626546621322632, -3.1415927410125732, 0], [0.710355281829834, 0.12420528382062912, -3.1415927410125732, 0], [0.700569748878479, 0.12214508652687073, -3.1415927410125732, 0], [0.6907843351364136, 0.12008488923311234, -3.1415927410125732, 0], [0.6809988021850586, 0.11802469193935394, -3.1415927410125732, 0], [0.6712133884429932, 0.11596449464559555, -3.1415927410125732, 0], [0.6614278554916382, 0.11390430480241776, -3.1415927410125732, 0], [0.651642382144928, 0.11184411495923996, -3.1415927410125732, 0], [0.64752197265625, 0.13141506910324097, -3.1415927410125732, 0], [0.657307505607605, 0.13347525894641876, -3.1415927410125732, 0], [0.6670929193496704, 0.13553544878959656, -3.1415927410125732, 0], [0.6768784523010254, 0.13759565353393555, -3.1415927410125732, 0], [0.6866639256477356, 0.13965584337711334, -3.1415927410125732, 0], [0.6964493989944458, 0.14171604812145233, -3.1415927410125732, 0], [0.706234872341156, 0.14377623796463013, -3.1415927410125732, 0], [0.7160203456878662, 0.14583642780780792, -3.1415927410125732, 0], [0.7258058190345764, 0.1478966325521469, -3.1415927410125732, 0], [0.7355912923812866, 0.1499568074941635, -3.1415927410125732, 0], [0.7453768253326416, 0.1520170271396637, -3.1415927410125732, 0], [0.755162239074707, 0.1540772020816803, -3.1415927410125732, 0], [0.764947772026062, 0.1561374068260193, -3.1415927410125732, 0], [0.7747331857681274, 0.15819759666919708, -3.1415927410125732, 0], [0.7845187187194824, 0.16025780141353607, -3.1415927410125732, 0], [0.7943041920661926, 0.16231799125671387, -3.1415927410125732, 1], [0.8040896654129028, 0.16437818109989166, -3.1415927410125732, 1], [0.813875138759613, 0.16643837094306946, -3.1415927410125732, 1], [0.8236606121063232, 0.16849857568740845, -3.1415927410125732, 1], [0.8334460854530334, 0.17055876553058624, -3.1415927410125732, 1], [0.8432315587997437, 0.17261897027492523, -3.1415927410125732, 1], [0.8530170917510986, 0.17467916011810303, -3.1415927410125732, 1], [0.8628025054931641, 0.17673934996128082, -3.1415927410125732, 1], [0.872588038444519, 0.1787995547056198, -3.1415927410125732, 1], [0.8823734521865845, 0.1808597296476364, -3.1415927410125732, 1], [0.8921589851379395, 0.1829199492931366, -3.1415927410125732, 1], [0.9019444584846497, 0.1849801242351532, -3.1415927410125732, 1], [0.9117299318313599, 0.1870403289794922, -3.1415927410125732, 1], [0.9215154051780701, 0.18910051882266998, -3.1415927410125732, 1], [0.9313008785247803, 0.19116072356700897, -3.1415927410125732, 1], [0.9410863518714905, 0.19322091341018677, -3.1415927410125732, 1], [0.9369660019874573, 0.21279186010360718, -3.1415927410125732, 1], [0.9271804690361023, 0.21073167026042938, -3.1415927410125732, 1], [0.9173950552940369, 0.2086714804172516, -3.1415927410125732, 1], [0.9076095223426819, 0.2066112905740738, -3.1415927410125732, 1], [0.8978240489959717, 0.2045510858297348, -3.1415927410125732, 1], [0.8880385756492615, 0.202490895986557, -3.1415927410125732, 1], [0.8782531023025513, 0.2004307061433792, -3.1415927410125732, 1], [0.8684676289558411, 0.19837050139904022, -3.1415927410125732, 1], [0.8586821556091309, 0.19631031155586243, -3.1415927410125732, 1], [0.8488966822624207, 0.19425012171268463, -3.1415927410125732, 1], [0.8391111493110657, 0.19218991696834564, -3.1415927410125732, 1], [0.8293257355690002, 0.19012972712516785, -3.1415927410125732, 1], [0.8195402026176453, 0.18806952238082886, -3.1415927410125732, 1], [0.8097547888755798, 0.18600934743881226, -3.1415927410125732, 1], [0.7999692559242249, 0.18394914269447327, -3.1415927410125732, 1], [0.7901837825775146, 0.18188893795013428, -3.1415927410125732, 1], [0.7803983092308044, 0.17982876300811768, -3.1415927410125732, 0], [0.7706128358840942, 0.1777685582637787, -3.1415927410125732, 0], [0.760827362537384, 0.1757083535194397, -3.1415927410125732, 0], [0.7510418891906738, 0.1736481636762619, -3.1415927410125732, 0], [0.7412563562393188, 0.1715879738330841, -3.1415927410125732, 0], [0.7314709424972534, 0.1695277839899063, -3.1415927410125732, 0], [0.7216854095458984, 0.16746757924556732, -3.1415927410125732, 0], [0.711899995803833, 0.16540738940238953, -3.1415927410125732, 0], [0.702114462852478, 0.16334719955921173, -3.1415927410125732, 0], [0.6923289895057678, 0.16128699481487274, -3.1415927410125732, 0], [0.6825435161590576, 0.15922680497169495, -3.1415927410125732, 0], [0.6727581024169922, 0.15716661512851715, -3.1415927410125732, 0], [0.6629725098609924, 0.15510641038417816, -3.1415927410125732, 0], [0.653187096118927, 0.15304622054100037, -3.1415927410125732, 0], [0.6434016227722168, 0.15098601579666138, -3.1415927410125732, 0], [0.6392812132835388, 0.17055699229240417, -3.1415927410125732, 0], [0.649066686630249, 0.17261718213558197, -3.1415927410125732, 0], [0.658852219581604, 0.17467737197875977, -3.1415927410125732, 0], [0.6686376333236694, 0.17673756182193756, -3.1415927410125732, 0], [0.6784231066703796, 0.17879776656627655, -3.1415927410125732, 0], [0.6882086396217346, 0.18085795640945435, -3.1415927410125732, 0], [0.6979941129684448, 0.18291814625263214, -3.1415927410125732, 0], [0.7077795267105103, 0.18497835099697113, -3.1415927410125732, 0], [0.7175650596618652, 0.18703854084014893, -3.1415927410125732, 0], [0.7273505330085754, 0.18909873068332672, -3.1415927410125732, 0], [0.7371360063552856, 0.1911589354276657, -3.1415927410125732, 0], [0.7469214797019958, 0.1932191252708435, -3.1415927410125732, 0], [0.756706953048706, 0.1952793151140213, -3.1415927410125732, 0], [0.766492486000061, 0.1973395198583603, -3.1415927410125732, 0], [0.7762778997421265, 0.19939970970153809, -3.1415927410125732, 0], [0.7860634326934814, 0.20145989954471588, -3.1415927410125732, 1], [0.7958488464355469, 0.20352010428905487, -3.1415927410125732, 1], [0.8056343793869019, 0.20558029413223267, -3.1415927410125732, 1], [0.8154198527336121, 0.20764048397541046, -3.1415927410125732, 1], [0.8252052664756775, 0.20970068871974945, -3.1415927410125732, 1], [0.9328455924987793, 0.23236282169818878, -3.1415927410125732, 1], [0.7134446501731873, 0.20660950243473053, -3.1415927410125732, 0], [0.703659176826477, 0.20454929769039154, -3.1415927410125732, 0], [0.6938737034797668, 0.20248910784721375, -3.1415927410125732, 0], [0.6840882301330566, 0.20042891800403595, -3.1415927410125732, 0], [0.6743027567863464, 0.19836872816085815, -3.1415927410125732, 0], [0.6645172834396362, 0.19630852341651917, -3.1415927410125732, 0], [0.6547317504882812, 0.19424833357334137, -3.1415927410125732, 0], [0.6449463367462158, 0.19218812882900238, -3.1415927410125732, 0], [0.6351608037948608, 0.19012793898582458, -3.1415927410125732, 0], [0.6310404539108276, 0.2096989005804062, -3.1415927410125732, 0]]
\ No newline at end of file
diff --git a/probe_vis_data_r0_90.json b/probe_vis_data_r0_90.json
new file mode 100644
index 0000000..129526b
--- /dev/null
+++ b/probe_vis_data_r0_90.json
@@ -0,0 +1 @@
           1 +[[0.7052074670791626, -0.1425783336162567, 1.570796251296997, 0], [0.7149929404258728, -0.14051814377307892, 1.570796251296997, 0], [0.724778413772583, -0.13845795392990112, 1.570796251296997, 0], [0.7345638871192932, -0.13639776408672333, 1.570796251296997, 0], [0.7443493604660034, -0.13433755934238434, 1.570796251296997, 0], [0.7541348338127136, -0.13227736949920654, 1.570796251296997, 0], [0.7639203667640686, -0.13021717965602875, 1.570796251296997, 0], [0.773705780506134, -0.12815697491168976, 1.570796251296997, 0], [0.783491313457489, -0.12609678506851196, 1.570796251296997, 0], [0.7932767271995544, -0.12403658777475357, 1.570796251296997, 0], [0.8030622601509094, -0.12197639048099518, 1.570796251296997, 0], [0.8128477334976196, -0.11991620063781738, 1.570796251296997, 0], [0.8226331472396851, -0.11785600334405899, 1.570796251296997, 0], [0.83241868019104, -0.1157958135008812, 1.570796251296997, 0], [0.8422041535377502, -0.1137356087565422, 1.570796251296997, 0], [0.8519896864891052, -0.11167542636394501, 1.570796251296997, 0], [0.8617751002311707, -0.10961522161960602, 1.570796251296997, 0], [0.8715605735778809, -0.10755503177642822, 1.570796251296997, 0], [0.8813461065292358, -0.10549483448266983, 1.570796251296997, 0], [0.8911315202713013, -0.10343464463949203, 1.570796251296997, 0], [0.9009170532226562, -0.10137443989515305, 1.570796251296997, 0], [0.9107025265693665, -0.09931425005197525, 1.570796251296997, 0], [0.9204879403114319, -0.09725406020879745, 1.570796251296997, 0], [0.9302734732627869, -0.09519386291503906, 1.570796251296997, 0], [0.9400589466094971, -0.09313366562128067, 1.570796251296997, 0], [0.9498444199562073, -0.09107346832752228, 1.570796251296997, 0], [0.9596298933029175, -0.08901327848434448, 1.570796251296997, 0], [0.9694154262542725, -0.08695308119058609, 1.570796251296997, 0], [0.9792008399963379, -0.0848928913474083, 1.570796251296997, 0], [0.9889863729476929, -0.0828326940536499, 1.570796251296997, 0], [0.9987717866897583, -0.08077249675989151, 1.570796251296997, 0], [0.9946514368057251, -0.061201538890600204, 1.570796251296997, 0], [0.9848659634590149, -0.0632617324590683, 1.570796251296997, 0], [0.9750804305076599, -0.06532192975282669, 1.570796251296997, 0], [0.9652950167655945, -0.06738212704658508, 1.570796251296997, 0], [0.9555095434188843, -0.06944231688976288, 1.570796251296997, 0], [0.9457240104675293, -0.07150251418352127, 1.570796251296997, 0], [0.9359385371208191, -0.07356271147727966, 1.570796251296997, 0], [0.9261531233787537, -0.07562290132045746, 1.570796251296997, 0], [0.9163675904273987, -0.07768309861421585, 1.570796251296997, 0], [0.9065821170806885, -0.07974329590797424, 1.570796251296997, 0], [0.8967966437339783, -0.08180348575115204, 1.570796251296997, 0], [0.8870111703872681, -0.08386368304491043, 1.570796251296997, 0], [0.8772256374359131, -0.08592388033866882, 1.570796251296997, 0], [0.8674402236938477, -0.08798407018184662, 1.570796251296997, 0], [0.8576547503471375, -0.09004426747560501, 1.570796251296997, 0], [0.8478692173957825, -0.0921044647693634, 1.570796251296997, 0], [0.8380837440490723, -0.0941646546125412, 1.570796251296997, 0], [0.8282983303070068, -0.09622485190629959, 1.570796251296997, 0], [0.8185127973556519, -0.09828504920005798, 1.570796251296997, 0], [0.8087273240089417, -0.10034523904323578, 1.570796251296997, 0], [0.7989418506622314, -0.10240543633699417, 1.570796251296997, 0], [0.7891563773155212, -0.10446563363075256, 1.570796251296997, 0], [0.779370903968811, -0.10652582347393036, 1.570796251296997, 0], [0.7695854306221008, -0.10858602076768875, 1.570796251296997, 0], [0.7597998976707458, -0.11064621806144714, 1.570796251296997, 0], [0.7500144839286804, -0.11270640790462494, 1.570796251296997, 0], [0.7402289509773254, -0.11476660519838333, 1.570796251296997, 0], [0.73044353723526, -0.11682680249214172, 1.570796251296997, 0], [0.720658004283905, -0.11888699233531952, 1.570796251296997, 0], [0.7108725309371948, -0.12094718962907791, 1.570796251296997, 0], [0.7010870575904846, -0.1230073869228363, 1.570796251296997, 0], [0.6969667077064514, -0.1034364253282547, 1.570796251296997, 0], [0.7067521214485168, -0.1013762354850769, 1.570796251296997, 0], [0.7165376543998718, -0.09931603819131851, 1.570796251296997, 0], [0.7263230681419373, -0.09725584089756012, 1.570796251296997, 0], [0.7361086010932922, -0.09519564360380173, 1.570796251296997, 0], [0.7458940744400024, -0.09313545376062393, 1.570796251296997, 0], [0.7556795477867126, -0.09107525646686554, 1.570796251296997, 0], [0.7654650211334229, -0.08901506662368774, 1.570796251296997, 0], [0.7752504944801331, -0.08695486932992935, 1.570796251296997, 0], [0.785036027431488, -0.08489467203617096, 1.570796251296997, 0], [0.7948214411735535, -0.08283447474241257, 1.570796251296997, 0], [0.8046069145202637, -0.08077428489923477, 1.570796251296997, 0], [0.8143924474716187, -0.07871408760547638, 1.570796251296997, 0], [0.8241779208183289, -0.07665389776229858, 1.570796251296997, 0], [0.8339633345603943, -0.07459370046854019, 1.570796251296997, 0], [0.8437488675117493, -0.0725335031747818, 1.570796251296997, 0], [0.8535343408584595, -0.07047330588102341, 1.570796251296997, 0], [0.8633198142051697, -0.06841311603784561, 1.570796251296997, 0], [0.8731052875518799, -0.06635291874408722, 1.570796251296997, 0], [0.8828907608985901, -0.06429272890090942, 1.570796251296997, 0], [0.8926762938499451, -0.06223252788186073, 1.570796251296997, 0], [0.9024617075920105, -0.06017233803868294, 1.570796251296997, 0], [0.9122471809387207, -0.058112140744924545, 1.570796251296997, 0], [0.9220327138900757, -0.05605194345116615, 1.570796251296997, 0], [0.9318181872367859, -0.05399175360798836, 1.570796251296997, 0], [0.9416036009788513, -0.051931556314229965, 1.570796251296997, 0], [0.9513891339302063, -0.04987135902047157, 1.570796251296997, 0], [0.9611746072769165, -0.04781116917729378, 1.570796251296997, 0], [0.9709600806236267, -0.045750971883535385, 1.570796251296997, 0], [0.9807455539703369, -0.04369077458977699, 1.570796251296997, 0], [0.9905310869216919, -0.0416305847465992, 1.570796251296997, 0], [0.9864106178283691, -0.022059623152017593, 1.570796251296997, 0], [0.9766252040863037, -0.024119820445775986, 1.570796251296997, 0], [0.9668396711349487, -0.02618001401424408, 1.570796251296997, 0], [0.9570541977882385, -0.028240209445357323, 1.570796251296997, 0], [0.9472687244415283, -0.030300403013825417, 1.570796251296997, 0], [0.9374832510948181, -0.03236059844493866, 1.570796251296997, 0], [0.9276977777481079, -0.034420792013406754, 1.570796251296997, 0], [0.9179123044013977, -0.036480989307165146, 1.570796251296997, 0], [0.9081268310546875, -0.03854118287563324, 1.570796251296997, 0], [0.8983413577079773, -0.04060138016939163, 1.570796251296997, 0], [0.8885558247566223, -0.04266157001256943, 1.570796251296997, 0], [0.8787704110145569, -0.04472176730632782, 1.570796251296997, 0], [0.8689848780632019, -0.04678196460008621, 1.570796251296997, 0], [0.8591994643211365, -0.04884215444326401, 1.570796251296997, 0], [0.8494139313697815, -0.0509023517370224, 1.570796251296997, 0], [0.8396284580230713, -0.05296254903078079, 1.570796251296997, 0], [0.8298429846763611, -0.05502273887395859, 1.570796251296997, 0], [0.8200575113296509, -0.05708293616771698, 1.570796251296997, 0], [0.8102720379829407, -0.05914313346147537, 1.570796251296997, 0], [0.8004865646362305, -0.06120332330465317, 1.570796251296997, 0], [0.7907010316848755, -0.06326352059841156, 1.570796251296997, 0], [0.7809156179428101, -0.06532371789216995, 1.570796251296997, 0], [0.7711301445960999, -0.06738390773534775, 1.570796251296997, 0], [0.7613446116447449, -0.06944410502910614, 1.570796251296997, 0], [0.7515591382980347, -0.07150430232286453, 1.570796251296997, 0], [0.7417737245559692, -0.07356449216604233, 1.570796251296997, 0], [0.7319881916046143, -0.07562468945980072, 1.570796251296997, 0], [0.722202718257904, -0.07768488675355911, 1.570796251296997, 0], [0.7124172449111938, -0.07974507659673691, 1.570796251296997, 0], [0.7026317119598389, -0.0818052738904953, 1.570796251296997, 0], [0.6928462982177734, -0.08386547118425369, 1.570796251296997, 0], [0.6887258887290955, -0.06429450958967209, 1.570796251296997, 0], [0.6985113620758057, -0.062234316021203995, 1.570796251296997, 0], [0.7082968950271606, -0.0601741224527359, 1.570796251296997, 0], [0.7180823087692261, -0.05811392515897751, 1.570796251296997, 0], [0.727867841720581, -0.056053731590509415, 1.570796251296997, 0], [0.7376532554626465, -0.05399353802204132, 1.570796251296997, 0], [0.7474387884140015, -0.05193334445357323, 1.570796251296997, 0], [0.7572242021560669, -0.049873147159814835, 1.570796251296997, 0], [0.7670097351074219, -0.04781294986605644, 1.570796251296997, 0], [0.7767952084541321, -0.04575276002287865, 1.570796251296997, 0], [0.7865806818008423, -0.043692562729120255, 1.570796251296997, 0], [0.7963661551475525, -0.04163236543536186, 1.570796251296997, 0], [0.8061516880989075, -0.03957217559218407, 1.570796251296997, 0], [0.8159371018409729, -0.037511978298425674, 1.570796251296997, 0], [0.8257225751876831, -0.03545178100466728, 1.570796251296997, 0], [0.8355081081390381, -0.03339159116148949, 1.570796251296997, 0], [0.8452935218811035, -0.031331393867731094, 1.570796251296997, 0], [0.8550790548324585, -0.02927119843661785, 1.570796251296997, 0], [0.8648645281791687, -0.027211004868149757, 1.570796251296997, 0], [0.8746500015258789, -0.025150809437036514, 1.570796251296997, 0], [0.8844354748725891, -0.02309061400592327, 1.570796251296997, 0], [0.8942209482192993, -0.021030420437455177, 1.570796251296997, 0], [0.9040064215660095, -0.018970225006341934, 1.570796251296997, 0], [0.9137918949127197, -0.01691003143787384, 1.570796251296997, 0], [0.9235773682594299, -0.014849835075438023, 1.570796251296997, 0], [0.9333629012107849, -0.012789640575647354, 1.570796251296997, 0], [0.9431483149528503, -0.010729446075856686, 1.570796251296997, 0], [0.9529338479042053, -0.008669251576066017, 1.570796251296997, 0], [0.9627193212509155, -0.006609056144952774, 1.570796251296997, 0], [0.972504734992981, -0.0045488616451621056, 1.570796251296997, 0], [0.9822902679443359, -0.002488666446879506, 1.570796251296997, 0], [0.978169858455658, 0.01708229072391987, 1.570796251296997, 1], [0.9683844447135925, 0.015022097155451775, 1.570796251296997, 1], [0.9585989117622375, 0.012961900793015957, 1.570796251296997, 1], [0.9488134384155273, 0.010901707224547863, 1.570796251296997, 1], [0.9390279054641724, 0.00884151179343462, 1.570796251296997, 1], [0.9292424917221069, 0.006781316827982664, 1.570796251296997, 0], [0.9194570183753967, 0.004721122328191996, 1.570796251296997, 0], [0.9096714854240417, 0.0026609275955706835, 1.570796251296997, 0], [0.8998860716819763, 0.0006007325137034059, 1.570796251296997, 0], [0.8901005387306213, -0.0014594622189179063, 1.570796251296997, 0], [0.8803150653839111, -0.0035196568351238966, 1.570796251296997, 0], [0.8705296516418457, -0.005579852033406496, 1.570796251296997, 0], [0.8607441186904907, -0.0076400465331971645, 1.570796251296997, 0], [0.8509586453437805, -0.00970024149864912, 1.570796251296997, 0], [0.8411731719970703, -0.011760435998439789, 1.570796251296997, 0], [0.8313876390457153, -0.013820631429553032, 1.570796251296997, 0], [0.8216022253036499, -0.015880824998021126, 1.570796251296997, 0], [0.8118167519569397, -0.01794102042913437, 1.570796251296997, 0], [0.8020312190055847, -0.020001215860247612, 1.570796251296997, 0], [0.7922458052635193, -0.022061411291360855, 1.570796251296997, 0], [0.7824602723121643, -0.02412160485982895, 1.570796251296997, 0], [0.7726747989654541, -0.026181800290942192, 1.570796251296997, 0], [0.7628893852233887, -0.028241993859410286, 1.570796251296997, 0], [0.7531038522720337, -0.03030218929052353, 1.570796251296997, 0], [0.7433183789253235, -0.03236238285899162, 1.570796251296997, 1], [0.7335329055786133, -0.034422580152750015, 1.570796251296997, 1], [0.7237473726272583, -0.03648277372121811, 1.570796251296997, 1], [0.7139619588851929, -0.0385429710149765, 1.570796251296997, 1], [0.7041764855384827, -0.0406031608581543, 1.570796251296997, 1], [0.6943909525871277, -0.04266335815191269, 1.570796251296997, 1], [0.6846055388450623, -0.04472355544567108, 1.570796251296997, 1], [0.6804850697517395, -0.025152593851089478, 1.570796251296997, 1], [0.6902706027030945, -0.023092400282621384, 1.570796251296997, 1], [0.7000560760498047, -0.02103220671415329, 1.570796251296997, 1], [0.7098415493965149, -0.018972011283040047, 1.570796251296997, 1], [0.7196270227432251, -0.016911815851926804, 1.570796251296997, 1], [0.7294125556945801, -0.014851621352136135, 1.570796251296997, 1], [0.7391979694366455, -0.012791425921022892, 1.570796251296997, 1], [0.7489834427833557, -0.010731231421232224, 1.570796251296997, 0], [0.7587689757347107, -0.008671036921441555, 1.570796251296997, 0], [0.7685543894767761, -0.0066108424216508865, 1.570796251296997, 0], [0.7783399224281311, -0.004550646990537643, 1.570796251296997, 0], [0.7881253957748413, -0.002490452490746975, 1.570796251296997, 0], [0.7979108691215515, -0.0004302576126065105, 1.570796251296997, 0], [0.8076963424682617, 0.0016299370909109712, 1.570796251296997, 0], [0.8174818158149719, 0.003690132172778249, 1.570796251296997, 0], [0.8272672891616821, 0.005750326439738274, 1.570796251296997, 0], [0.8370527625083923, 0.007810521870851517, 1.570796251296997, 0], [0.8468382358551025, 0.009870716370642185, 1.570796251296997, 0], [0.8566237688064575, 0.011930910870432854, 1.570796251296997, 0], [0.866409182548523, 0.013991106301546097, 1.570796251296997, 0], [0.8761947154998779, 0.01605129987001419, 1.570796251296997, 0], [0.8859801888465881, 0.018111497163772583, 1.570796251296997, 0], [0.8957656621932983, 0.020171688869595528, 1.570796251296997, 0], [0.9055511355400085, 0.02223188616335392, 1.570796251296997, 0], [0.915336549282074, 0.024292079731822014, 1.570796251296997, 0], [0.9251221418380737, 0.026352275162935257, 1.570796251296997, 0], [0.9349075555801392, 0.02841246873140335, 1.570796251296997, 1], [0.9446930289268494, 0.030472666025161743, 1.570796251296997, 1], [0.9544785022735596, 0.03253285959362984, 1.570796251296997, 1], [0.9642640352249146, 0.03459305316209793, 1.570796251296997, 1], [0.97404944896698, 0.03665325045585632, 1.570796251296997, 1], [0.9699290990829468, 0.05622420459985733, 1.570796251296997, 1], [0.9601436257362366, 0.054164011031389236, 1.570796251296997, 1], [0.9503581523895264, 0.05210381746292114, 1.570796251296997, 1], [0.9405726194381714, 0.05004362389445305, 1.570796251296997, 1], [0.930787205696106, 0.047983426600694656, 1.570796251296997, 1], [0.921001672744751, 0.04592323303222656, 1.570796251296997, 1], [0.9112162590026855, 0.04386303573846817, 1.570796251296997, 0], [0.9014307260513306, 0.041802845895290375, 1.570796251296997, 0], [0.8916452527046204, 0.03974264860153198, 1.570796251296997, 0], [0.8818597793579102, 0.03768245130777359, 1.570796251296997, 0], [0.8720743060112, 0.035622257739305496, 1.570796251296997, 0], [0.8622888326644897, 0.0335620641708374, 1.570796251296997, 0], [0.8525033593177795, 0.03150187060236931, 1.570796251296997, 0], [0.8427178263664246, 0.029441673308610916, 1.570796251296997, 0], [0.8329324126243591, 0.027381479740142822, 1.570796251296997, 0], [0.8231468796730042, 0.02532128430902958, 1.570796251296997, 0], [0.8133614659309387, 0.023261090740561485, 1.570796251296997, 0], [0.8035759329795837, 0.021200893446803093, 1.570796251296997, 0], [0.7937904596328735, 0.01914070174098015, 1.570796251296997, 0], [0.7840049862861633, 0.017080504447221756, 1.570796251296997, 0], [0.7742195129394531, 0.015020310878753662, 1.570796251296997, 0], [0.7644340395927429, 0.012960115447640419, 1.570796251296997, 0], [0.7546485662460327, 0.01089992094784975, 1.570796251296997, 0], [0.7448630928993225, 0.008839726448059082, 1.570796251296997, 0], [0.7350775599479675, 0.006779531016945839, 1.570796251296997, 1], [0.7252921462059021, 0.0047193365171551704, 1.570796251296997, 1], [0.7155066132545471, 0.002659142017364502, 1.570796251296997, 1], [0.7057211995124817, 0.0005989467026665807, 1.570796251296997, 1], [0.6959356665611267, -0.0014612477971240878, 1.570796251296997, 1], [0.6861501932144165, -0.0035214426461607218, 1.570796251296997, 1], [0.6763647198677063, -0.005581637378782034, 1.570796251296997, 1], [0.6722443699836731, 0.013989320024847984, 1.570796251296997, 1], [0.6820297837257385, 0.016049515455961227, 1.570796251296997, 1], [0.6918153166770935, 0.01810971088707447, 1.570796251296997, 1], [0.7016007900238037, 0.020169904455542564, 1.570796251296997, 1], [0.7113862037658691, 0.022230098024010658, 1.570796251296997, 1], [0.7211717367172241, 0.02429029531776905, 1.570796251296997, 1], [0.7309572100639343, 0.026350488886237144, 1.570796251296997, 1], [0.7407426834106445, 0.028410684317350388, 1.570796251296997, 0], [0.7505282163619995, 0.03047087788581848, 1.570796251296997, 0], [0.7603136301040649, 0.032531075179576874, 1.570796251296997, 0], [0.7700991034507751, 0.03459126874804497, 1.570796251296997, 0], [0.7798846364021301, 0.03665146231651306, 1.570796251296997, 0], [0.7896700501441956, 0.038711655884981155, 1.570796251296997, 0], [0.7994555830955505, 0.04077185317873955, 1.570796251296997, 0], [0.8092410564422607, 0.04283205047249794, 1.570796251296997, 0], [0.8190264701843262, 0.044892240315675735, 1.570796251296997, 0], [0.8288120031356812, 0.04695243760943413, 1.570796251296997, 0], [0.8385974764823914, 0.04901263117790222, 1.570796251296997, 0], [0.8483829498291016, 0.051072828471660614, 1.570796251296997, 0], [0.8581684827804565, 0.05313302204012871, 1.570796251296997, 0], [0.867953896522522, 0.0551932156085968, 1.570796251296997, 0], [0.8777393698692322, 0.057253409177064896, 1.570796251296997, 0], [0.8875249028205872, 0.05931360647082329, 1.570796251296997, 0], [0.8973103165626526, 0.06137380376458168, 1.570796251296997, 0], [0.9070958495140076, 0.06343399733304977, 1.570796251296997, 0], [0.9168813228607178, 0.06549418717622757, 1.570796251296997, 1], [0.9266667366027832, 0.06755438446998596, 1.570796251296997, 1], [0.9364522695541382, 0.06961458176374435, 1.570796251296997, 1], [0.9462377429008484, 0.07167477160692215, 1.570796251296997, 1], [0.9560232758522034, 0.07373496890068054, 1.570796251296997, 1], [0.9658086895942688, 0.07579516619443893, 1.570796251296997, 1], [0.9616882801055908, 0.09536612033843994, 1.570796251296997, 1], [0.9519028663635254, 0.09330593049526215, 1.570796251296997, 1], [0.9421173334121704, 0.09124573320150375, 1.570796251296997, 1], [0.9323318600654602, 0.08918553590774536, 1.570796251296997, 1], [0.9225464463233948, 0.08712534606456757, 1.570796251296997, 1], [0.9127609133720398, 0.08506514877080917, 1.570796251296997, 1], [0.9029754400253296, 0.08300495147705078, 1.570796251296997, 0], [0.8931899666786194, 0.08094476163387299, 1.570796251296997, 0], [0.8834044337272644, 0.0788845643401146, 1.570796251296997, 0], [0.873619019985199, 0.0768243670463562, 1.570796251296997, 0], [0.8638335466384888, 0.07476416975259781, 1.570796251296997, 0], [0.8540480136871338, 0.07270397990942001, 1.570796251296997, 0], [0.8442625999450684, 0.07064379006624222, 1.570796251296997, 0], [0.8344770669937134, 0.06858358532190323, 1.570796251296997, 0], [0.8246915936470032, 0.06652339547872543, 1.570796251296997, 0], [0.814906120300293, 0.06446319818496704, 1.570796251296997, 0], [0.8051207065582275, 0.062403008341789246, 1.570796251296997, 0], [0.7953351140022278, 0.06034281104803085, 1.570796251296997, 0], [0.7855497002601624, 0.05828261375427246, 1.570796251296997, 0], [0.7757642269134521, 0.056222423911094666, 1.570796251296997, 0], [0.7659787535667419, 0.05416222661733627, 1.570796251296997, 0], [0.756193220615387, 0.05210202932357788, 1.570796251296997, 0], [0.7464078068733215, 0.05004183575510979, 1.570796251296997, 0], [0.7366222739219666, 0.04798164218664169, 1.570796251296997, 0], [0.7268368601799011, 0.0459214486181736, 1.570796251296997, 1], [0.7170513272285461, 0.04386125132441521, 1.570796251296997, 1], [0.7072658538818359, 0.04180105775594711, 1.570796251296997, 1], [0.6974803805351257, 0.03974086046218872, 1.570796251296997, 1], [0.6876949071884155, 0.037680670619010925, 1.570796251296997, 1], [0.6779094338417053, 0.03562047332525253, 1.570796251296997, 1], [0.6681239604949951, 0.03356027603149414, 1.570796251296997, 1], [0.6640035510063171, 0.053131237626075745, 1.570796251296997, 1], [0.6737890243530273, 0.05519142746925354, 1.570796251296997, 1], [0.6835744976997375, 0.05725162848830223, 1.570796251296997, 1], [0.6933599710464478, 0.059311818331480026, 1.570796251296997, 1], [0.7031455039978027, 0.06137201562523842, 1.570796251296997, 1], [0.7129309177398682, 0.06343220919370651, 1.570796251296997, 1], [0.7227164506912231, 0.0654924064874649, 1.570796251296997, 1], [0.7325019240379333, 0.0675525963306427, 1.570796251296997, 0], [0.7422873973846436, 0.06961279362440109, 1.570796251296997, 0], [0.7520728707313538, 0.07167299091815948, 1.570796251296997, 0], [0.761858344078064, 0.07373318821191788, 1.570796251296997, 0], [0.7716438174247742, 0.07579337805509567, 1.570796251296997, 0], [0.7814292907714844, 0.07785357534885406, 1.570796251296997, 0], [0.7912147641181946, 0.07991376519203186, 1.570796251296997, 0], [0.8010002970695496, 0.08197396248579025, 1.570796251296997, 0], [0.810785710811615, 0.08403415977954865, 1.570796251296997, 0], [0.82057124376297, 0.08609434962272644, 1.570796251296997, 0], [0.8303566575050354, 0.08815454691648483, 1.570796251296997, 0], [0.8401421904563904, 0.09021474421024323, 1.570796251296997, 0], [0.8499276638031006, 0.09227494150400162, 1.570796251296997, 0], [0.8597131371498108, 0.09433513134717941, 1.570796251296997, 0], [0.869498610496521, 0.09639532119035721, 1.570796251296997, 0], [0.8792840838432312, 0.0984555259346962, 1.570796251296997, 0], [0.8890695571899414, 0.10051571577787399, 1.570796251296997, 0], [0.8988550901412964, 0.10257591307163239, 1.570796251296997, 0], [0.9086405038833618, 0.10463610291481018, 1.570796251296997, 1], [0.9184260368347168, 0.10669630020856857, 1.570796251296997, 1], [0.9282114505767822, 0.10875649750232697, 1.570796251296997, 1], [0.9379969835281372, 0.11081668734550476, 1.570796251296997, 1], [0.9477824568748474, 0.11287688463926315, 1.570796251296997, 1], [0.9575679302215576, 0.11493708193302155, 1.570796251296997, 1], [0.9534475207328796, 0.13450804352760315, 1.570796251296997, 1], [0.9436620473861694, 0.13244783878326416, 1.570796251296997, 1], [0.9338765740394592, 0.13038764894008636, 1.570796251296997, 1], [0.924091100692749, 0.12832745909690857, 1.570796251296997, 1], [0.9143056273460388, 0.12626725435256958, 1.570796251296997, 1], [0.9045201539993286, 0.12420706450939178, 1.570796251296997, 1], [0.8947346210479736, 0.12214686721563339, 1.570796251296997, 0], [0.8849492073059082, 0.1200866773724556, 1.570796251296997, 0], [0.8751636743545532, 0.11802647262811661, 1.570796251296997, 0], [0.8653782606124878, 0.11596629023551941, 1.570796251296997, 0], [0.8555927276611328, 0.11390608549118042, 1.570796251296997, 0], [0.8458072543144226, 0.11184589564800262, 1.570796251296997, 0], [0.8360217809677124, 0.10978569835424423, 1.570796251296997, 0], [0.8262363076210022, 0.10772550851106644, 1.570796251296997, 0], [0.816450834274292, 0.10566531121730804, 1.570796251296997, 0], [0.8066653609275818, 0.10360511392354965, 1.570796251296997, 0], [0.7968798875808716, 0.10154492408037186, 1.570796251296997, 0], [0.7870943546295166, 0.09948472678661346, 1.570796251296997, 0], [0.7773089408874512, 0.09742452949285507, 1.570796251296997, 0], [0.7675234079360962, 0.09536433964967728, 1.570796251296997, 0], [0.7577379941940308, 0.09330413490533829, 1.570796251296997, 0], [0.7479524612426758, 0.09124395251274109, 1.570796251296997, 0], [0.7381669878959656, 0.0891837477684021, 1.570796251296997, 0], [0.7283815145492554, 0.0871235579252243, 1.570796251296997, 0], [0.7185960412025452, 0.08506336808204651, 1.570796251296997, 1], [0.708810567855835, 0.08300316333770752, 1.570796251296997, 1], [0.6990250945091248, 0.08094297349452972, 1.570796251296997, 1], [0.6892395615577698, 0.07888277620077133, 1.570796251296997, 1], [0.6794541478157043, 0.07682258635759354, 1.570796251296997, 1], [0.6696686744689941, 0.07476238906383514, 1.570796251296997, 1], [0.6598831415176392, 0.07270219177007675, 1.570796251296997, 1], [0.655762791633606, 0.09227315336465836, 1.570796251296997, 1], [0.6655482649803162, 0.09433334320783615, 1.570796251296997, 1], [0.6753337383270264, 0.09639354050159454, 1.570796251296997, 1], [0.6851192116737366, 0.09845373779535294, 1.570796251296997, 1], [0.6949046850204468, 0.10051392763853073, 1.570796251296997, 1], [0.704690158367157, 0.10257413238286972, 1.570796251296997, 1], [0.7144756317138672, 0.10463431477546692, 1.570796251296997, 1], [0.7242611646652222, 0.10669451951980591, 1.570796251296997, 0], [0.7340465784072876, 0.1087547093629837, 1.570796251296997, 0], [0.7438321113586426, 0.1108149066567421, 1.570796251296997, 0], [0.753617525100708, 0.11287509649991989, 1.570796251296997, 0], [0.763403058052063, 0.11493529379367828, 1.570796251296997, 0], [0.7731885313987732, 0.11699549108743668, 1.570796251296997, 0], [0.7829740047454834, 0.11905568093061447, 1.570796251296997, 0], [0.7927594780921936, 0.12111587822437286, 1.570796251296997, 0], [0.8025449514389038, 0.12317607551813126, 1.570796251296997, 0], [0.8123304843902588, 0.12523627281188965, 1.570796251296997, 0], [0.8221158981323242, 0.12729646265506744, 1.570796251296997, 0], [0.8319013714790344, 0.12935665249824524, 1.570796251296997, 0], [0.8416869044303894, 0.13141685724258423, 1.570796251296997, 0], [0.8514723181724548, 0.13347704708576202, 1.570796251296997, 0], [0.8612578511238098, 0.13553723692893982, 1.570796251296997, 0], [0.87104332447052, 0.1375974416732788, 1.570796251296997, 0], [0.8808287978172302, 0.1396576315164566, 1.570796251296997, 0], [0.8906142711639404, 0.1417178213596344, 1.570796251296997, 0], [0.9003997445106506, 0.1437780261039734, 1.570796251296997, 1], [0.9101852178573608, 0.14583821594715118, 1.570796251296997, 1], [0.919970691204071, 0.14789840579032898, 1.570796251296997, 1], [0.929756224155426, 0.14995861053466797, 1.570796251296997, 1], [0.9395416378974915, 0.15201880037784576, 1.570796251296997, 1], [0.9493271708488464, 0.15407900512218475, 1.570796251296997, 1], [0.9452067613601685, 0.17364995181560516, 1.570796251296997, 1], [0.9354212284088135, 0.17158974707126617, 1.570796251296997, 1], [0.925635814666748, 0.16952957212924957, 1.570796251296997, 1], [0.9158503413200378, 0.16746936738491058, 1.570796251296997, 1], [0.9060648083686829, 0.1654091775417328, 1.570796251296997, 1], [0.8962793946266174, 0.1633489727973938, 1.570796251296997, 1], [0.8864938616752625, 0.161288782954216, 1.570796251296997, 0], [0.8767083883285522, 0.1592285931110382, 1.570796251296997, 0], [0.866922914981842, 0.1571684032678604, 1.570796251296997, 0], [0.8571374416351318, 0.15510819852352142, 1.570796251296997, 0], [0.8473519682884216, 0.15304800868034363, 1.570796251296997, 0], [0.8375664949417114, 0.15098780393600464, 1.570796251296997, 0], [0.8277810215950012, 0.14892761409282684, 1.570796251296997, 0], [0.817995548248291, 0.14686742424964905, 1.570796251296997, 0], [0.808210015296936, 0.14480721950531006, 1.570796251296997, 0], [0.7984246015548706, 0.14274702966213226, 1.570796251296997, 0], [0.7886390686035156, 0.14068683981895447, 1.570796251296997, 0], [0.7788535952568054, 0.13862664997577667, 1.570796251296997, 0], [0.76906818151474, 0.13656644523143768, 1.570796251296997, 0], [0.759282648563385, 0.1345062553882599, 1.570796251296997, 0], [0.7494971752166748, 0.1324460506439209, 1.570796251296997, 0], [0.7397117018699646, 0.1303858608007431, 1.570796251296997, 0], [0.7299262285232544, 0.1283256709575653, 1.570796251296997, 0], [0.7201406955718994, 0.12626546621322632, 1.570796251296997, 0], [0.710355281829834, 0.12420528382062912, 1.570796251296997, 1], [0.700569748878479, 0.12214508652687073, 1.570796251296997, 1], [0.6907843351364136, 0.12008488923311234, 1.570796251296997, 1], [0.6809988021850586, 0.11802469193935394, 1.570796251296997, 1], [0.6712133884429932, 0.11596449464559555, 1.570796251296997, 1], [0.6614278554916382, 0.11390430480241776, 1.570796251296997, 1], [0.651642382144928, 0.11184411495923996, 1.570796251296997, 1], [0.64752197265625, 0.13141506910324097, 1.570796251296997, 1], [0.657307505607605, 0.13347525894641876, 1.570796251296997, 1], [0.6670929193496704, 0.13553544878959656, 1.570796251296997, 1], [0.6768784523010254, 0.13759565353393555, 1.570796251296997, 1], [0.6866639256477356, 0.13965584337711334, 1.570796251296997, 1], [0.6964493989944458, 0.14171604812145233, 1.570796251296997, 1], [0.706234872341156, 0.14377623796463013, 1.570796251296997, 1], [0.7160203456878662, 0.14583642780780792, 1.570796251296997, 0], [0.7258058190345764, 0.1478966325521469, 1.570796251296997, 0], [0.7355912923812866, 0.1499568074941635, 1.570796251296997, 0], [0.7453768253326416, 0.1520170271396637, 1.570796251296997, 0], [0.755162239074707, 0.1540772020816803, 1.570796251296997, 0], [0.764947772026062, 0.1561374068260193, 1.570796251296997, 0], [0.7747331857681274, 0.15819759666919708, 1.570796251296997, 0], [0.7845187187194824, 0.16025780141353607, 1.570796251296997, 0], [0.7943041920661926, 0.16231799125671387, 1.570796251296997, 0], [0.8040896654129028, 0.16437818109989166, 1.570796251296997, 0], [0.813875138759613, 0.16643837094306946, 1.570796251296997, 0], [0.8236606121063232, 0.16849857568740845, 1.570796251296997, 0], [0.8334460854530334, 0.17055876553058624, 1.570796251296997, 0], [0.8432315587997437, 0.17261897027492523, 1.570796251296997, 0], [0.8530170917510986, 0.17467916011810303, 1.570796251296997, 0], [0.8628025054931641, 0.17673934996128082, 1.570796251296997, 0], [0.872588038444519, 0.1787995547056198, 1.570796251296997, 0], [0.8823734521865845, 0.1808597296476364, 1.570796251296997, 0], [0.8921589851379395, 0.1829199492931366, 1.570796251296997, 1], [0.9019444584846497, 0.1849801242351532, 1.570796251296997, 1], [0.9117299318313599, 0.1870403289794922, 1.570796251296997, 1], [0.9215154051780701, 0.18910051882266998, 1.570796251296997, 1], [0.9313008785247803, 0.19116072356700897, 1.570796251296997, 1], [0.9410863518714905, 0.19322091341018677, 1.570796251296997, 1], [0.9369660019874573, 0.21279186010360718, 1.570796251296997, 1], [0.9271804690361023, 0.21073167026042938, 1.570796251296997, 1], [0.9173950552940369, 0.2086714804172516, 1.570796251296997, 1], [0.9076095223426819, 0.2066112905740738, 1.570796251296997, 1], [0.8978240489959717, 0.2045510858297348, 1.570796251296997, 1], [0.8880385756492615, 0.202490895986557, 1.570796251296997, 1], [0.8782531023025513, 0.2004307061433792, 1.570796251296997, 0], [0.8684676289558411, 0.19837050139904022, 1.570796251296997, 0], [0.8586821556091309, 0.19631031155586243, 1.570796251296997, 0], [0.8488966822624207, 0.19425012171268463, 1.570796251296997, 0], [0.8391111493110657, 0.19218991696834564, 1.570796251296997, 0], [0.8293257355690002, 0.19012972712516785, 1.570796251296997, 0], [0.8195402026176453, 0.18806952238082886, 1.570796251296997, 0], [0.8097547888755798, 0.18600934743881226, 1.570796251296997, 0], [0.7999692559242249, 0.18394914269447327, 1.570796251296997, 0], [0.7901837825775146, 0.18188893795013428, 1.570796251296997, 0], [0.7803983092308044, 0.17982876300811768, 1.570796251296997, 0], [0.7706128358840942, 0.1777685582637787, 1.570796251296997, 0], [0.760827362537384, 0.1757083535194397, 1.570796251296997, 0], [0.7510418891906738, 0.1736481636762619, 1.570796251296997, 0], [0.7412563562393188, 0.1715879738330841, 1.570796251296997, 0], [0.7314709424972534, 0.1695277839899063, 1.570796251296997, 0], [0.7216854095458984, 0.16746757924556732, 1.570796251296997, 0], [0.711899995803833, 0.16540738940238953, 1.570796251296997, 0], [0.702114462852478, 0.16334719955921173, 1.570796251296997, 1], [0.6923289895057678, 0.16128699481487274, 1.570796251296997, 1], [0.6825435161590576, 0.15922680497169495, 1.570796251296997, 1], [0.6727581024169922, 0.15716661512851715, 1.570796251296997, 1], [0.6629725098609924, 0.15510641038417816, 1.570796251296997, 1], [0.653187096118927, 0.15304622054100037, 1.570796251296997, 1], [0.6434016227722168, 0.15098601579666138, 1.570796251296997, 1], [0.6392812132835388, 0.17055699229240417, 1.570796251296997, 1], [0.649066686630249, 0.17261718213558197, 1.570796251296997, 1], [0.658852219581604, 0.17467737197875977, 1.570796251296997, 1], [0.6686376333236694, 0.17673756182193756, 1.570796251296997, 1], [0.6784231066703796, 0.17879776656627655, 1.570796251296997, 1], [0.6882086396217346, 0.18085795640945435, 1.570796251296997, 1], [0.6979941129684448, 0.18291814625263214, 1.570796251296997, 1], [0.7077795267105103, 0.18497835099697113, 1.570796251296997, 1], [0.7175650596618652, 0.18703854084014893, 1.570796251296997, 0], [0.7273505330085754, 0.18909873068332672, 1.570796251296997, 0], [0.7371360063552856, 0.1911589354276657, 1.570796251296997, 0], [0.7469214797019958, 0.1932191252708435, 1.570796251296997, 0], [0.756706953048706, 0.1952793151140213, 1.570796251296997, 0], [0.766492486000061, 0.1973395198583603, 1.570796251296997, 0], [0.7762778997421265, 0.19939970970153809, 1.570796251296997, 0], [0.7860634326934814, 0.20145989954471588, 1.570796251296997, 0], [0.7958488464355469, 0.20352010428905487, 1.570796251296997, 0], [0.8056343793869019, 0.20558029413223267, 1.570796251296997, 0], [0.8154198527336121, 0.20764048397541046, 1.570796251296997, 0], [0.8252052664756775, 0.20970068871974945, 1.570796251296997, 0], [0.8349907994270325, 0.21176087856292725, 1.570796251296997, 0], [0.8447762727737427, 0.21382106840610504, 1.570796251296997, 0], [0.8545618057250977, 0.21588127315044403, 1.570796251296997, 0], [0.8643472194671631, 0.21794146299362183, 1.570796251296997, 0], [0.8741326928138733, 0.22000165283679962, 1.570796251296997, 0], [0.8839182257652283, 0.2220618575811386, 1.570796251296997, 1], [0.7232301235198975, 0.20866969227790833, 1.570796251296997, 0], [0.7134446501731873, 0.20660950243473053, 1.570796251296997, 0], [0.703659176826477, 0.20454929769039154, 1.570796251296997, 1], [0.6938737034797668, 0.20248912274837494, 1.570796251296997, 1], [0.6840882301330566, 0.20042890310287476, 1.570796251296997, 1], [0.6743027567863464, 0.19836872816085815, 1.570796251296997, 1], [0.6645172238349915, 0.19630852341651917, 1.570796251296997, 1], [0.654731810092926, 0.19424833357334137, 1.570796251296997, 1], [0.6449463367462158, 0.19218812882900238, 1.570796251296997, 1], [0.6351608037948608, 0.19012793898582458, 1.570796251296997, 1], [0.6310404539108276, 0.2096989005804062, 1.570796251296997, 1], [0.6408259272575378, 0.21175909042358398, 1.570796251296997, 1], [0.650611400604248, 0.21381929516792297, 1.570796251296997, 1], [0.6603968739509583, 0.21587948501110077, 1.570796251296997, 1], [0.6701823472976685, 0.21793967485427856, 1.570796251296997, 1], [0.6799678206443787, 0.21999986469745636, 1.570796251296997, 1]]
\ No newline at end of file
diff --git a/probe_vis_data_row_1.8.json b/probe_vis_data_row_1.8.json
new file mode 100644
index 0000000..7365753
--- /dev/null
+++ b/probe_vis_data_row_1.8.json
@@ -0,0 +1 @@
           1 +[[0.4193665683269501, 0.0016263782745227218, -3.1415927410125732, 1], [0.42915207147598267, 0.003686560783535242, -3.1415927410125732, 1], [0.43893754482269287, 0.005746755283325911, -3.1415927410125732, 1], [0.4487230181694031, 0.007806950248777866, -3.1415927410125732, 1], [0.4585084915161133, 0.009867144748568535, -3.1415927410125732, 1], [0.4682939946651459, 0.011927340179681778, -3.1415927410125732, 1], [0.4780794382095337, 0.013987534679472446, -3.1415927410125732, 1], [0.4878649413585663, 0.016047729179263115, -3.1415927410125732, 1], [0.4976504147052765, 0.018107924610376358, -3.1415927410125732, 1], [0.5074359178543091, 0.020168118178844452, -3.1415927410125732, 1], [0.5172213315963745, 0.022228313609957695, -3.1415927410125732, 1], [0.5270068645477295, 0.024288509041070938, -3.1415927410125732, 1], [0.5367923378944397, 0.02634870447218418, -3.1415927410125732, 1], [0.5465778112411499, 0.028408898040652275, -3.1415927410125732, 1], [0.5563632845878601, 0.03046909160912037, -3.1415927410125732, 1], [0.5661487579345703, 0.03252928704023361, -3.1415927410125732, 1], [0.5759342312812805, 0.034589484333992004, -3.1415927410125732, 1], [0.5857197642326355, 0.0366496779024601, -3.1415927410125732, 1], [0.5955051779747009, 0.03870987147092819, -3.1415927410125732, 1], [0.6052907109260559, 0.040770068764686584, -3.1415927410125732, 1], [0.6150761246681213, 0.04283026233315468, -3.1415927410125732, 1], [0.6248616576194763, 0.04489045590162277, -3.1415927410125732, 1], [0.6346471309661865, 0.046950649470090866, -3.1415927410125732, 1], [0.6444326043128967, 0.04901084676384926, -3.1415927410125732, 0], [0.6542180776596069, 0.05107104033231735, -3.1415927410125732, 0], [0.6640035510063171, 0.053131237626075745, -3.1415927410125732, 0], [0.6737890243530273, 0.05519143119454384, -3.1415927410125732, 0], [0.6835744976997375, 0.05725162476301193, -3.1415927410125732, 0], [0.6933600306510925, 0.059311822056770325, -3.1415927410125732, 0], [0.703145444393158, 0.06137201189994812, -3.1415927410125732, 0], [0.7129309773445129, 0.06343220919370651, -3.1415927410125732, 0], [0.7227163910865784, 0.0654924064874649, -3.1415927410125732, 0], [0.7325019240379333, 0.0675526037812233, -3.1415927410125732, 0], [0.7422873973846436, 0.06961279362440109, -3.1415927410125732, 0], [0.7520728707313538, 0.07167298346757889, -3.1415927410125732, 0], [0.761858344078064, 0.07373318821191788, -3.1415927410125732, 0], [0.7716438174247742, 0.07579337805509567, -3.1415927410125732, 0], [0.7814292907714844, 0.07785357534885406, -3.1415927410125732, 0], [0.7912147641181946, 0.07991376519203186, -3.1415927410125732, 0], [0.8010002970695496, 0.08197396248579025, -3.1415927410125732, 0], [0.810785710811615, 0.08403415977954865, -3.1415927410125732, 1], [0.82057124376297, 0.08609434962272644, -3.1415927410125732, 1], [0.8303567171096802, 0.08815454691648483, -3.1415927410125732, 1], [0.8401421308517456, 0.09021474421024323, -3.1415927410125732, 1], [0.8499276638031006, 0.09227494150400162, -3.1415927410125732, 1], [0.8597131371498108, 0.09433513134717941, -3.1415927410125732, 1], [0.869498610496521, 0.0963953286409378, -3.1415927410125732, 1], [0.8792840838432312, 0.0984555184841156, -3.1415927410125732, 1], [0.8890696167945862, 0.10051571577787399, -3.1415927410125732, 1], [0.8988550305366516, 0.10257591307163239, -3.1415927410125732, 1], [0.9086405038833618, 0.10463610291481018, -3.1415927410125732, 1], [0.9184260368347168, 0.10669630020856857, -3.1415927410125732, 1], [0.9282114505767822, 0.10875649750232697, -3.1415927410125732, 1], [0.9379969835281372, 0.11081668734550476, -3.1415927410125732, 1], [0.9477824568748474, 0.11287689208984375, -3.1415927410125732, 1], [0.9575679302215576, 0.11493707448244095, -3.1415927410125732, 1], [0.9673534035682678, 0.11699727922677994, -3.1415927410125732, 1], [0.977138876914978, 0.11905746906995773, -3.1415927410125732, 1], [0.9869243502616882, 0.12111766636371613, -3.1415927410125732, 1], [0.9967098236083984, 0.12317785620689392, -3.1415927410125732, 1], [1.0064953565597534, 0.1252380609512329, -3.1415927410125732, 1], [1.0162807703018188, 0.1272982358932495, -3.1415927410125732, 1], [1.0260663032531738, 0.1293584555387497, -3.1415927410125732, 1], [1.0358517169952393, 0.1314186304807663, -3.1415927410125732, 1], [1.0456372499465942, 0.13347883522510529, -3.1415927410125732, 1], [1.0554226636886597, 0.13553902506828308, -3.1415927410125732, 1], [1.0652081966400146, 0.13759922981262207, -3.1415927410125732, 1], [1.0749937295913696, 0.13965941965579987, -3.1415927410125732, 1], [1.084779143333435, 0.14171960949897766, -3.1415927410125732, 1], [1.09456467628479, 0.14377979934215546, -3.1415927410125732, 1], [1.1043500900268555, 0.14584000408649445, -3.1415927410125732, 1], [1.114135503768921, 0.14790019392967224, -3.1415927410125732, 1], [1.1239211559295654, 0.14996039867401123, -3.1415927410125732, 1], [1.1337064504623413, 0.15202058851718903, -3.1415927410125732, 1], [1.1434921026229858, 0.15408077836036682, -3.1415927410125732, 1], [1.1532775163650513, 0.1561409831047058, -3.1415927410125732, 1], [1.1630629301071167, 0.1582011580467224, -3.1415927410125732, 1], [1.1728484630584717, 0.1602613776922226, -3.1415927410125732, 1], [1.182633876800537, 0.1623215526342392, -3.1415927410125732, 1], [1.192419409751892, 0.16438175737857819, -3.1415927410125732, 1], [1.2022048234939575, 0.16644194722175598, -3.1415927410125732, 1], [1.2022048234939575, 0.16644194722175598, -2.6179938316345215, 1], [1.192419409751892, 0.16438175737857819, -2.6179938316345215, 1], [1.1826339960098267, 0.1623215675354004, -2.6179938316345215, 1], [1.1728484630584717, 0.1602613627910614, -2.6179938316345215, 1], [1.1630629301071167, 0.1582011729478836, -2.6179938316345215, 1], [1.1532775163650513, 0.15614096820354462, -2.6179938316345215, 1], [1.1434919834136963, 0.15408077836036682, -2.6179938316345215, 1], [1.1337065696716309, 0.15202058851718903, -2.6179938316345215, 1], [1.1239210367202759, 0.14996039867401123, -2.6179938316345215, 1], [1.1141356229782104, 0.14790019392967224, -2.6179938316345215, 1], [1.1043500900268555, 0.14584000408649445, -2.6179938316345215, 1], [1.09456467628479, 0.14377979934215546, -2.6179938316345215, 1], [1.084779143333435, 0.14171962440013885, -2.6179938316345215, 1], [1.07499361038208, 0.13965940475463867, -2.6179938316345215, 1], [1.0652081966400146, 0.13759922981262207, -2.6179938316345215, 1], [1.0554227828979492, 0.13553902506828308, -2.6179938316345215, 1], [1.0456372499465942, 0.13347883522510529, -2.6179938316345215, 1], [1.0358517169952393, 0.1314186453819275, -2.6179938316345215, 1], [1.0260663032531738, 0.1293584406375885, -2.6179938316345215, 1], [1.0162807703018188, 0.1272982507944107, -2.6179938316345215, 1], [1.0064953565597534, 0.12523804605007172, -2.6179938316345215, 1], [0.9967097640037537, 0.12317786365747452, -2.6179938316345215, 1], [0.9869243502616882, 0.12111766636371613, -2.6179938316345215, 1], [0.9771389365196228, 0.11905746906995773, -2.6179938316345215, 1], [0.9673534035682678, 0.11699727177619934, -2.6179938316345215, 1], [0.9575678706169128, 0.11493708193302155, -2.6179938316345215, 1], [0.9477824568748474, 0.11287688463926315, -2.6179938316345215, 1], [0.9379969835281372, 0.11081668734550476, -2.6179938316345215, 1], [0.928211510181427, 0.10875649750232697, -2.6179938316345215, 1], [0.918425977230072, 0.10669630020856857, -2.6179938316345215, 1], [0.9086405038833618, 0.10463611036539078, -2.6179938316345215, 1], [0.8988550901412964, 0.10257591307163239, -2.6179938316345215, 1], [0.8890695571899414, 0.10051571577787399, -2.6179938316345215, 1], [0.8792840838432312, 0.0984555184841156, -2.6179938316345215, 1], [0.869498610496521, 0.0963953286409378, -2.6179938316345215, 1], [0.8597131371498108, 0.09433513134717941, -2.6179938316345215, 1], [0.8499276638031006, 0.09227493405342102, -2.6179938316345215, 1], [0.8401421904563904, 0.09021474421024323, -2.6179938316345215, 1], [0.8303566575050354, 0.08815454691648483, -2.6179938316345215, 1], [0.82057124376297, 0.08609435707330704, -2.6179938316345215, 1], [0.8107857704162598, 0.08403415232896805, -2.6179938316345215, 1], [0.8010002374649048, 0.08197396248579025, -2.6179938316345215, 1], [0.7912147641181946, 0.07991377264261246, -2.6179938316345215, 1], [0.7814292907714844, 0.07785357534885406, -2.6179938316345215, 1], [0.771643877029419, 0.07579337805509567, -2.6179938316345215, 1], [0.761858344078064, 0.07373318076133728, -2.6179938316345215, 1], [0.752072811126709, 0.07167299091815948, -2.6179938316345215, 1], [0.7422873973846436, 0.06961279362440109, -2.6179938316345215, 1], [0.7325019240379333, 0.0675525963306427, -2.6179938316345215, 1], [0.7227164506912231, 0.0654924064874649, -2.6179938316345215, 1], [0.7129309177398682, 0.06343220919370651, -2.6179938316345215, 1], [0.7031455039978027, 0.06137201935052872, -2.6179938316345215, 1], [0.6933599710464478, 0.059311818331480026, -2.6179938316345215, 1], [0.6835744976997375, 0.05725162476301193, -2.6179938316345215, 1], [0.6737890839576721, 0.05519143119454384, -2.6179938316345215, 1], [0.6640035510063171, 0.053131237626075745, -2.6179938316345215, 1], [0.6542180776596069, 0.05107104033231735, -2.6179938316345215, 1], [0.6444326043128967, 0.04901084676384926, -2.6179938316345215, 1], [0.6346470713615417, 0.046950649470090866, -2.6179938316345215, 1], [0.6248616576194763, 0.04489045962691307, -2.6179938316345215, 1], [0.6150761842727661, 0.04283025860786438, -2.6179938316345215, 1], [0.6052906513214111, 0.040770068764686584, -2.6179938316345215, 1], [0.5955052375793457, 0.03870987147092819, -2.6179938316345215, 1], [0.5857197046279907, 0.0366496779024601, -2.6179938316345215, 1], [0.5759342312812805, 0.034589484333992004, -2.6179938316345215, 1], [0.5661487579345703, 0.03252928704023361, -2.6179938316345215, 1], [0.5563632845878601, 0.030469093471765518, -2.6179938316345215, 1], [0.5465778112411499, 0.028408898040652275, -2.6179938316345215, 1], [0.5367923378944397, 0.026348702609539032, -2.6179938316345215, 1], [0.5270068645477295, 0.024288509041070938, -2.6179938316345215, 1], [0.5172213912010193, 0.022228313609957695, -2.6179938316345215, 1], [0.5074358582496643, 0.0201681200414896, -2.6179938316345215, 1], [0.4976504445075989, 0.01810792274773121, -2.6179938316345215, 1], [0.4878649413585663, 0.016047729179263115, -2.6179938316345215, 1], [0.4780794382095337, 0.013987535610795021, -2.6179938316345215, 1], [0.4682939946651459, 0.011927339248359203, -2.6179938316345215, 1], [0.4585084915161133, 0.00986714567989111, -2.6179938316345215, 1], [0.4487230181694031, 0.007806949783116579, -2.6179938316345215, 1], [0.43893754482269287, 0.005746755283325911, -2.6179938316345215, 1], [0.42915207147598267, 0.0036865605507045984, -2.6179938316345215, 1], [0.4193665683269501, 0.0016263658180832863, -2.6179938316345215, 1], [0.4193665683269501, 0.0016263658180832863, -2.094395160675049, 1], [0.42915207147598267, 0.0036865605507045984, -2.094395160675049, 1], [0.43893754482269287, 0.005746755283325911, -2.094395160675049, 1], [0.4487230181694031, 0.007806950248777866, -2.094395160675049, 1], [0.4585084915161133, 0.009867144748568535, -2.094395160675049, 1], [0.4682939648628235, 0.011927340179681778, -2.094395160675049, 1], [0.4780794680118561, 0.013987534679472446, -2.094395160675049, 1], [0.4878649413585663, 0.016047729179263115, -2.094395160675049, 1], [0.4976504147052765, 0.018107924610376358, -2.094395160675049, 1], [0.5074358582496643, 0.020168118178844452, -2.094395160675049, 1], [0.5172213912010193, 0.022228313609957695, -2.094395160675049, 1], [0.5270068645477295, 0.024288509041070938, -2.094395160675049, 1], [0.5367923378944397, 0.02634870447218418, -2.094395160675049, 1], [0.5465778112411499, 0.028408898040652275, -2.094395160675049, 1], [0.5563632845878601, 0.030469093471765518, -2.094395160675049, 1], [0.5661487579345703, 0.03252928704023361, -2.094395160675049, 1], [0.5759342312812805, 0.034589484333992004, -2.094395160675049, 1], [0.5857197642326355, 0.0366496741771698, -2.094395160675049, 1], [0.5955051779747009, 0.03870987519621849, -2.094395160675049, 1], [0.6052907109260559, 0.040770065039396286, -2.094395160675049, 1], [0.6150761246681213, 0.04283026233315468, -2.094395160675049, 1], [0.6248616576194763, 0.04489045590162277, -2.094395160675049, 1], [0.6346471309661865, 0.046950653195381165, -2.094395160675049, 1], [0.6444326043128967, 0.04901084676384926, -2.094395160675049, 1], [0.6542180776596069, 0.05107104033231735, -2.094395160675049, 1], [0.6640035510063171, 0.053131233900785446, -2.094395160675049, 1], [0.6737890243530273, 0.05519143119454384, -2.094395160675049, 1], [0.6835744976997375, 0.05725162848830223, -2.094395160675049, 1], [0.6933600306510925, 0.059311818331480026, -2.094395160675049, 1], [0.703145444393158, 0.06137201562523842, -2.094395160675049, 1], [0.7129309773445129, 0.06343220919370651, -2.094395160675049, 1], [0.7227163910865784, 0.0654924064874649, -2.094395160675049, 1], [0.7325019240379333, 0.0675525963306427, -2.094395160675049, 1], [0.7422873973846436, 0.06961279362440109, -2.094395160675049, 1], [0.7520728707313538, 0.07167299091815948, -2.094395160675049, 1], [0.761858344078064, 0.07373318821191788, -2.094395160675049, 1], [0.7716438174247742, 0.07579337805509567, -2.094395160675049, 1], [0.7814292907714844, 0.07785356789827347, -2.094395160675049, 1], [0.7912147641181946, 0.07991377264261246, -2.094395160675049, 1], [0.8010002970695496, 0.08197396248579025, -2.094395160675049, 1], [0.810785710811615, 0.08403415977954865, -2.094395160675049, 1], [0.82057124376297, 0.08609434962272644, -2.094395160675049, 1], [0.8303566575050354, 0.08815454691648483, -2.094395160675049, 1], [0.8401421904563904, 0.09021474421024323, -2.094395160675049, 1], [0.8499276638031006, 0.09227493405342102, -2.094395160675049, 1], [0.8597131371498108, 0.09433513879776001, -2.094395160675049, 1], [0.869498610496521, 0.09639532119035721, -2.094395160675049, 1], [0.8792840838432312, 0.0984555259346962, -2.094395160675049, 1], [0.8890695571899414, 0.10051571577787399, -2.094395160675049, 1], [0.8988550901412964, 0.10257591307163239, -2.094395160675049, 1], [0.9086405038833618, 0.10463610291481018, -2.094395160675049, 1], [0.9184260368347168, 0.10669630020856857, -2.094395160675049, 1], [0.9282114505767822, 0.10875649750232697, -2.094395160675049, 1], [0.9379969835281372, 0.11081668734550476, -2.094395160675049, 1], [0.9477824568748474, 0.11287688463926315, -2.094395160675049, 1], [0.9575679302215576, 0.11493708193302155, -2.094395160675049, 1], [0.9673534035682678, 0.11699727922677994, -2.094395160675049, 1], [0.977138876914978, 0.11905746906995773, -2.094395160675049, 1], [0.9869243502616882, 0.12111765891313553, -2.094395160675049, 1], [0.9967098236083984, 0.12317786365747452, -2.094395160675049, 1], [1.0064953565597534, 0.12523804605007172, -2.094395160675049, 1], [1.0162807703018188, 0.1272982507944107, -2.094395160675049, 1], [1.0260663032531738, 0.1293584555387497, -2.094395160675049, 1], [1.0358517169952393, 0.1314186304807663, -2.094395160675049, 1], [1.0456372499465942, 0.13347883522510529, -2.094395160675049, 1], [1.0554226636886597, 0.13553902506828308, -2.094395160675049, 1], [1.0652081966400146, 0.13759922981262207, -2.094395160675049, 1], [1.0749937295913696, 0.13965941965579987, -2.094395160675049, 1], [1.084779143333435, 0.14171960949897766, -2.094395160675049, 1], [1.0945645570755005, 0.14377979934215546, -2.094395160675049, 1], [1.1043500900268555, 0.14584000408649445, -2.094395160675049, 1], [1.114135503768921, 0.14790019392967224, -2.094395160675049, 1], [1.1239211559295654, 0.14996039867401123, -2.094395160675049, 1], [1.1337064504623413, 0.15202058851718903, -2.094395160675049, 1], [1.1434921026229858, 0.15408077836036682, -2.094395160675049, 1], [1.1532775163650513, 0.15614096820354462, -2.094395160675049, 1], [1.1630629301071167, 0.1582011729478836, -2.094395160675049, 1], [1.1728484630584717, 0.1602613627910614, -2.094395160675049, 1], [1.1826339960098267, 0.1623215675354004, -2.094395160675049, 1], [1.192419409751892, 0.16438175737857819, -2.094395160675049, 1], [1.2022048234939575, 0.16644194722175598, -2.094395160675049, 1], [1.2022048234939575, 0.16644194722175598, -1.5707963705062866, 1], [1.192419409751892, 0.16438175737857819, -1.5707963705062866, 1], [1.1826339960098267, 0.1623215526342392, -1.5707963705062866, 1], [1.1728484630584717, 0.1602613776922226, -1.5707963705062866, 1], [1.1630629301071167, 0.1582011729478836, -1.5707963705062866, 1], [1.1532775163650513, 0.15614096820354462, -1.5707963705062866, 1], [1.1434919834136963, 0.15408077836036682, -1.5707963705062866, 1], [1.1337065696716309, 0.15202058851718903, -1.5707963705062866, 1], [1.1239210367202759, 0.14996039867401123, -1.5707963705062866, 1], [1.1141356229782104, 0.14790019392967224, -1.5707963705062866, 1], [1.1043500900268555, 0.14584000408649445, -1.5707963705062866, 1], [1.09456467628479, 0.14377979934215546, -1.5707963705062866, 1], [1.084779143333435, 0.14171962440013885, -1.5707963705062866, 1], [1.07499361038208, 0.13965940475463867, -1.5707963705062866, 1], [1.0652081966400146, 0.13759922981262207, -1.5707963705062866, 1], [1.0554227828979492, 0.13553902506828308, -1.5707963705062866, 1], [1.0456372499465942, 0.13347883522510529, -1.5707963705062866, 1], [1.0358517169952393, 0.1314186453819275, -1.5707963705062866, 1], [1.0260663032531738, 0.1293584406375885, -1.5707963705062866, 1], [1.0162807703018188, 0.1272982507944107, -1.5707963705062866, 1], [1.0064953565597534, 0.12523804605007172, -1.5707963705062866, 1], [0.9967097640037537, 0.12317786365747452, -1.5707963705062866, 1], [0.9869243502616882, 0.12111766636371613, -1.5707963705062866, 1], [0.9771389365196228, 0.11905746906995773, -1.5707963705062866, 1], [0.9673534035682678, 0.11699727177619934, -1.5707963705062866, 1], [0.9575678706169128, 0.11493708193302155, -1.5707963705062866, 1], [0.9477824568748474, 0.11287688463926315, -1.5707963705062866, 1], [0.9379969835281372, 0.11081668734550476, -1.5707963705062866, 1], [0.928211510181427, 0.10875649750232697, -1.5707963705062866, 1], [0.918425977230072, 0.10669630020856857, -1.5707963705062866, 1], [0.9086405038833618, 0.10463611036539078, -1.5707963705062866, 1], [0.8988550901412964, 0.10257590562105179, -1.5707963705062866, 1], [0.8890695571899414, 0.10051571577787399, -1.5707963705062866, 1], [0.8792840838432312, 0.0984555259346962, -1.5707963705062866, 1], [0.869498610496521, 0.0963953286409378, -1.5707963705062866, 1], [0.8597131371498108, 0.09433513134717941, -1.5707963705062866, 1], [0.8499276638031006, 0.09227493405342102, -1.5707963705062866, 1], [0.8401421904563904, 0.09021474421024323, -1.5707963705062866, 1], [0.8303566575050354, 0.08815454691648483, -1.5707963705062866, 1], [0.82057124376297, 0.08609434962272644, -1.5707963705062866, 1], [0.8107857704162598, 0.08403415977954865, -1.5707963705062866, 1], [0.8010002374649048, 0.08197396248579025, -1.5707963705062866, 1], [0.7912147641181946, 0.07991377264261246, -1.5707963705062866, 1], [0.7814292907714844, 0.07785356789827347, -1.5707963705062866, 1], [0.771643877029419, 0.07579338550567627, -1.5707963705062866, 1], [0.761858344078064, 0.07373318076133728, -1.5707963705062866, 1], [0.752072811126709, 0.07167299091815948, -1.5707963705062866, 1], [0.7422873973846436, 0.06961279362440109, -1.5707963705062866, 1], [0.7325019240379333, 0.0675525963306427, -1.5707963705062866, 1], [0.7227164506912231, 0.0654924064874649, -1.5707963705062866, 1], [0.7129309177398682, 0.06343220919370651, -1.5707963705062866, 1], [0.7031455039978027, 0.06137201562523842, -1.5707963705062866, 1], [0.6933599710464478, 0.059311822056770325, -1.5707963705062866, 1], [0.6835744976997375, 0.05725162476301193, -1.5707963705062866, 1], [0.6737890839576721, 0.05519143119454384, -1.5707963705062866, 1], [0.6640035510063171, 0.053131233900785446, -1.5707963705062866, 1], [0.6542180776596069, 0.05107104405760765, -1.5707963705062866, 1], [0.6444326043128967, 0.04901084303855896, -1.5707963705062866, 1], [0.6346470713615417, 0.046950653195381165, -1.5707963705062866, 1], [0.6248616576194763, 0.04489045590162277, -1.5707963705062866, 1], [0.6150761842727661, 0.04283026233315468, -1.5707963705062866, 1], [0.6052906513214111, 0.040770068764686584, -1.5707963705062866, 1], [0.5955052375793457, 0.03870987147092819, -1.5707963705062866, 1], [0.5857197046279907, 0.0366496779024601, -1.5707963705062866, 1], [0.5759342312812805, 0.034589480608701706, -1.5707963705062866, 1], [0.5661487579345703, 0.03252928704023361, -1.5707963705062866, 1], [0.5563632845878601, 0.030469095334410667, -1.5707963705062866, 1], [0.5465778112411499, 0.028408898040652275, -1.5707963705062866, 1], [0.5367923378944397, 0.026348702609539032, -1.5707963705062866, 1], [0.5270068645477295, 0.024288509041070938, -1.5707963705062866, 1], [0.5172213912010193, 0.022228313609957695, -1.5707963705062866, 1], [0.5074358582496643, 0.0201681200414896, -1.5707963705062866, 1], [0.4976504445075989, 0.01810792274773121, -1.5707963705062866, 1], [0.4878649413585663, 0.016047731041908264, -1.5707963705062866, 1], [0.4780794382095337, 0.013987533748149872, -1.5707963705062866, 1], [0.4682939946651459, 0.011927340179681778, -1.5707963705062866, 1], [0.4585084915161133, 0.009867144748568535, -1.5707963705062866, 1], [0.4487230181694031, 0.007806950248777866, -1.5707963705062866, 1], [0.43893754482269287, 0.005746755283325911, -1.5707963705062866, 1], [0.42915207147598267, 0.0036865603178739548, -1.5707963705062866, 1], [0.4193665683269501, 0.0016263658180832863, -1.5707963705062866, 1], [0.4193665683269501, 0.0016263658180832863, -1.0471975803375244, 1], [0.42915207147598267, 0.0036865605507045984, -1.0471975803375244, 1], [0.43893754482269287, 0.005746755283325911, -1.0471975803375244, 1], [0.4487230181694031, 0.007806950248777866, -1.0471975803375244, 1], [0.4585084915161133, 0.009867144748568535, -1.0471975803375244, 1], [0.4682939648628235, 0.011927340179681778, -1.0471975803375244, 1], [0.4780794680118561, 0.013987534679472446, -1.0471975803375244, 1], [0.4878649413585663, 0.016047729179263115, -1.0471975803375244, 1], [0.4976504147052765, 0.018107924610376358, -1.0471975803375244, 1], [0.5074358582496643, 0.020168118178844452, -1.0471975803375244, 1], [0.5172213912010193, 0.022228313609957695, -1.0471975803375244, 1], [0.5270068645477295, 0.024288509041070938, -1.0471975803375244, 1], [0.5367923378944397, 0.02634870447218418, -1.0471975803375244, 1], [0.5465778112411499, 0.028408898040652275, -1.0471975803375244, 1], [0.5563632845878601, 0.030469093471765518, -1.0471975803375244, 1], [0.5661487579345703, 0.03252928704023361, -1.0471975803375244, 1], [0.5759342312812805, 0.034589484333992004, -1.0471975803375244, 1], [0.5857197642326355, 0.0366496741771698, -1.0471975803375244, 1], [0.5955051779747009, 0.03870987519621849, -1.0471975803375244, 1], [0.6052907109260559, 0.040770065039396286, -1.0471975803375244, 1], [0.6150761246681213, 0.04283026233315468, -1.0471975803375244, 1], [0.6248616576194763, 0.04489045590162277, -1.0471975803375244, 1], [0.6346471309661865, 0.046950653195381165, -1.0471975803375244, 1], [0.6444326043128967, 0.04901084676384926, -1.0471975803375244, 1], [0.6542180776596069, 0.05107104033231735, -1.0471975803375244, 1], [0.6640035510063171, 0.053131233900785446, -1.0471975803375244, 1], [0.6737890243530273, 0.05519143119454384, -1.0471975803375244, 1], [0.6835744976997375, 0.05725162848830223, -1.0471975803375244, 1], [0.6933600306510925, 0.059311818331480026, -1.0471975803375244, 1], [0.703145444393158, 0.06137201562523842, -1.0471975803375244, 1], [0.7129309773445129, 0.06343220919370651, -1.0471975803375244, 1], [0.7227163910865784, 0.0654924064874649, -1.0471975803375244, 1], [0.7325019240379333, 0.0675525963306427, -1.0471975803375244, 1], [0.7422873973846436, 0.06961279362440109, -1.0471975803375244, 1], [0.7520728707313538, 0.07167299091815948, -1.0471975803375244, 1], [0.761858344078064, 0.07373318821191788, -1.0471975803375244, 1], [0.7716438174247742, 0.07579337805509567, -1.0471975803375244, 1], [0.7814292907714844, 0.07785356789827347, -1.0471975803375244, 1], [0.7912147641181946, 0.07991377264261246, -1.0471975803375244, 1], [0.8010002970695496, 0.08197396248579025, -1.0471975803375244, 1], [0.810785710811615, 0.08403415977954865, -1.0471975803375244, 1], [0.82057124376297, 0.08609434962272644, -1.0471975803375244, 1], [0.8303566575050354, 0.08815454691648483, -1.0471975803375244, 1], [0.8401421904563904, 0.09021474421024323, -1.0471975803375244, 1], [0.8499276638031006, 0.09227493405342102, -1.0471975803375244, 1], [0.8597131371498108, 0.09433513879776001, -1.0471975803375244, 1], [0.869498610496521, 0.09639532119035721, -1.0471975803375244, 1], [0.8792840838432312, 0.0984555259346962, -1.0471975803375244, 1], [0.8890695571899414, 0.10051571577787399, -1.0471975803375244, 1], [0.8988550901412964, 0.10257591307163239, -1.0471975803375244, 1], [0.9086405038833618, 0.10463610291481018, -1.0471975803375244, 1], [0.9184260368347168, 0.10669630020856857, -1.0471975803375244, 1], [0.9282114505767822, 0.10875649750232697, -1.0471975803375244, 1], [0.9379969835281372, 0.11081668734550476, -1.0471975803375244, 1], [0.9477824568748474, 0.11287688463926315, -1.0471975803375244, 1], [0.9575679302215576, 0.11493708193302155, -1.0471975803375244, 1], [0.9673534035682678, 0.11699727922677994, -1.0471975803375244, 1], [0.977138876914978, 0.11905746906995773, -1.0471975803375244, 1], [0.9869243502616882, 0.12111765891313553, -1.0471975803375244, 1], [0.9967098236083984, 0.12317786365747452, -1.0471975803375244, 1], [1.0064953565597534, 0.12523804605007172, -1.0471975803375244, 1], [1.0162807703018188, 0.1272982507944107, -1.0471975803375244, 1], [1.0260663032531738, 0.1293584555387497, -1.0471975803375244, 1], [1.0358517169952393, 0.1314186304807663, -1.0471975803375244, 1], [1.0456372499465942, 0.13347883522510529, -1.0471975803375244, 1], [1.0554226636886597, 0.13553902506828308, -1.0471975803375244, 1], [1.0652081966400146, 0.13759922981262207, -1.0471975803375244, 1], [1.0749937295913696, 0.13965941965579987, -1.0471975803375244, 1], [1.084779143333435, 0.14171960949897766, -1.0471975803375244, 1], [1.0945645570755005, 0.14377979934215546, -1.0471975803375244, 1], [1.1043500900268555, 0.14584000408649445, -1.0471975803375244, 1], [1.114135503768921, 0.14790019392967224, -1.0471975803375244, 1], [1.1239211559295654, 0.14996039867401123, -1.0471975803375244, 1], [1.1337064504623413, 0.15202058851718903, -1.0471975803375244, 1], [1.1434921026229858, 0.15408077836036682, -1.0471975803375244, 1], [1.1532775163650513, 0.15614096820354462, -1.0471975803375244, 1], [1.1630629301071167, 0.1582011729478836, -1.0471975803375244, 1], [1.1728484630584717, 0.1602613627910614, -1.0471975803375244, 1], [1.1826339960098267, 0.1623215675354004, -1.0471975803375244, 1], [1.192419409751892, 0.16438175737857819, -1.0471975803375244, 1], [1.2022048234939575, 0.16644194722175598, -1.0471975803375244, 1], [1.2022048234939575, 0.16644194722175598, -0.5235987901687622, 1], [1.192419409751892, 0.16438175737857819, -0.5235987901687622, 1], [1.1826339960098267, 0.1623215526342392, -0.5235987901687622, 1], [1.1728484630584717, 0.1602613776922226, -0.5235987901687622, 1], [1.1630629301071167, 0.1582011729478836, -0.5235987901687622, 1], [1.1532775163650513, 0.15614096820354462, -0.5235987901687622, 1], [1.1434919834136963, 0.15408077836036682, -0.5235987901687622, 1], [1.1337065696716309, 0.15202058851718903, -0.5235987901687622, 1], [1.1239210367202759, 0.14996039867401123, -0.5235987901687622, 1], [1.1141356229782104, 0.14790019392967224, -0.5235987901687622, 1], [1.1043500900268555, 0.14584000408649445, -0.5235987901687622, 1], [1.09456467628479, 0.14377979934215546, -0.5235987901687622, 1], [1.084779143333435, 0.14171960949897766, -0.5235987901687622, 1], [1.07499361038208, 0.13965941965579987, -0.5235987901687622, 1], [1.0652081966400146, 0.13759922981262207, -0.5235987901687622, 1], [1.0554227828979492, 0.13553902506828308, -0.5235987901687622, 1], [1.0456372499465942, 0.13347883522510529, -0.5235987901687622, 1], [1.0358517169952393, 0.1314186453819275, -0.5235987901687622, 1], [1.0260663032531738, 0.1293584406375885, -0.5235987901687622, 1], [1.0162807703018188, 0.1272982507944107, -0.5235987901687622, 1], [1.0064953565597534, 0.12523804605007172, -0.5235987901687622, 1], [0.9967097640037537, 0.12317786365747452, -0.5235987901687622, 1], [0.9869243502616882, 0.12111765891313553, -0.5235987901687622, 1], [0.9771389365196228, 0.11905747652053833, -0.5235987901687622, 1], [0.9673534035682678, 0.11699727177619934, -0.5235987901687622, 1], [0.9575678706169128, 0.11493708193302155, -0.5235987901687622, 1], [0.9477824568748474, 0.11287688463926315, -0.5235987901687622, 1], [0.9379969835281372, 0.11081668734550476, -0.5235987901687622, 1], [0.928211510181427, 0.10875649750232697, -0.5235987901687622, 1], [0.918425977230072, 0.10669630020856857, -0.5235987901687622, 1], [0.9086405038833618, 0.10463611036539078, -0.5235987901687622, 1], [0.8988550901412964, 0.10257590562105179, -0.5235987901687622, 1], [0.8890695571899414, 0.10051571577787399, -0.5235987901687622, 1], [0.8792840838432312, 0.0984555259346962, -0.5235987901687622, 1], [0.869498610496521, 0.0963953286409378, -0.5235987901687622, 1], [0.8597131371498108, 0.09433513134717941, -0.5235987901687622, 1], [0.8499276638031006, 0.09227493405342102, -0.5235987901687622, 1], [0.8401421904563904, 0.09021474421024323, -0.5235987901687622, 1], [0.8303566575050354, 0.08815454691648483, -0.5235987901687622, 1], [0.82057124376297, 0.08609434962272644, -0.5235987901687622, 1], [0.8107857704162598, 0.08403415977954865, -0.5235987901687622, 1], [0.8010002374649048, 0.08197396248579025, -0.5235987901687622, 1], [0.7912147641181946, 0.07991377264261246, -0.5235987901687622, 1], [0.7814292907714844, 0.07785356789827347, -0.5235987901687622, 1], [0.771643877029419, 0.07579337805509567, -0.5235987901687622, 1], [0.761858344078064, 0.07373318821191788, -0.5235987901687622, 1], [0.752072811126709, 0.07167299091815948, -0.5235987901687622, 1], [0.7422873973846436, 0.06961279362440109, -0.5235987901687622, 1], [0.7325019240379333, 0.0675525963306427, -0.5235987901687622, 1], [0.7227164506912231, 0.0654924064874649, -0.5235987901687622, 1], [0.7129309177398682, 0.06343220919370651, -0.5235987901687622, 1], [0.7031455039978027, 0.06137201562523842, -0.5235987901687622, 1], [0.6933599710464478, 0.059311822056770325, -0.5235987901687622, 1], [0.6835744976997375, 0.05725162476301193, -0.5235987901687622, 1], [0.6737890839576721, 0.05519143119454384, -0.5235987901687622, 1], [0.6640035510063171, 0.053131233900785446, -0.5235987901687622, 1], [0.6542180776596069, 0.05107104033231735, -0.5235987901687622, 1], [0.6444326043128967, 0.04901084676384926, -0.5235987901687622, 1], [0.6346470713615417, 0.046950653195381165, -0.5235987901687622, 1], [0.6248616576194763, 0.04489045590162277, -0.5235987901687622, 1], [0.6150761842727661, 0.04283026233315468, -0.5235987901687622, 1], [0.6052906513214111, 0.040770068764686584, -0.5235987901687622, 1], [0.5955052375793457, 0.03870987147092819, -0.5235987901687622, 1], [0.5857197046279907, 0.0366496779024601, -0.5235987901687622, 1], [0.5759342312812805, 0.034589480608701706, -0.5235987901687622, 1], [0.5661487579345703, 0.03252928704023361, -0.5235987901687622, 1], [0.5563632845878601, 0.030469095334410667, -0.5235987901687622, 1], [0.5465778112411499, 0.028408898040652275, -0.5235987901687622, 1], [0.5367923378944397, 0.026348702609539032, -0.5235987901687622, 1], [0.5270068645477295, 0.024288509041070938, -0.5235987901687622, 1], [0.5172213912010193, 0.022228313609957695, -0.5235987901687622, 1], [0.5074358582496643, 0.0201681200414896, -0.5235987901687622, 1], [0.4976504445075989, 0.01810792274773121, -0.5235987901687622, 1], [0.4878649413585663, 0.016047729179263115, -0.5235987901687622, 1], [0.4780794382095337, 0.013987535610795021, -0.5235987901687622, 1], [0.4682939946651459, 0.011927339248359203, -0.5235987901687622, 1], [0.4585084915161133, 0.00986714567989111, -0.5235987901687622, 1], [0.4487230181694031, 0.007806949783116579, -0.5235987901687622, 1], [0.43893754482269287, 0.005746755283325911, -0.5235987901687622, 1], [0.42915207147598267, 0.003686560783535242, -0.5235987901687622, 1], [0.4193665683269501, 0.0016263658180832863, -0.5235987901687622, 1], [0.4193665683269501, 0.0016263658180832863, -1.8168604398738353e-09, 1], [0.42915207147598267, 0.0036865605507045984, -1.8168604398738353e-09, 1], [0.43893754482269287, 0.005746755283325911, -1.8168604398738353e-09, 1], [0.4487230181694031, 0.007806950248777866, -1.8168604398738353e-09, 1], [0.4585084915161133, 0.009867144748568535, -1.8168604398738353e-09, 1], [0.4682939648628235, 0.011927340179681778, -1.8168604398738353e-09, 1], [0.4780794680118561, 0.013987534679472446, -1.8168604398738353e-09, 1], [0.4878649413585663, 0.016047729179263115, -1.8168604398738353e-09, 1], [0.4976504147052765, 0.018107924610376358, -1.8168604398738353e-09, 1], [0.5074358582496643, 0.020168118178844452, -1.8168604398738353e-09, 1], [0.5172213912010193, 0.022228313609957695, -1.8168604398738353e-09, 1], [0.5270068645477295, 0.024288509041070938, -1.8168604398738353e-09, 1], [0.5367923378944397, 0.02634870447218418, -1.8168604398738353e-09, 1], [0.5465778112411499, 0.028408898040652275, -1.8168604398738353e-09, 1], [0.5563632845878601, 0.03046909160912037, -1.8168604398738353e-09, 1], [0.5661487579345703, 0.03252928704023361, -1.8168604398738353e-09, 1], [0.5759342312812805, 0.034589484333992004, -1.8168604398738353e-09, 1], [0.5857197642326355, 0.0366496779024601, -1.8168604398738353e-09, 1], [0.5955051779747009, 0.03870987147092819, -1.8168604398738353e-09, 1], [0.6052907109260559, 0.040770068764686584, -1.8168604398738353e-09, 1], [0.6150761246681213, 0.04283026233315468, -1.8168604398738353e-09, 1], [0.6248616576194763, 0.04489045590162277, -1.8168604398738353e-09, 1], [0.6346471309661865, 0.046950649470090866, -1.8168604398738353e-09, 1], [0.6444326043128967, 0.04901084676384926, -1.8168604398738353e-09, 1], [0.6542180776596069, 0.05107104033231735, -1.8168604398738353e-09, 1], [0.6640035510063171, 0.053131237626075745, -1.8168604398738353e-09, 1], [0.6737890243530273, 0.05519143119454384, -1.8168604398738353e-09, 1], [0.6835744976997375, 0.05725162476301193, -1.8168604398738353e-09, 1], [0.6933600306510925, 0.059311822056770325, -1.8168604398738353e-09, 1], [0.703145444393158, 0.06137201189994812, -1.8168604398738353e-09, 1], [0.7129309773445129, 0.06343220919370651, -1.8168604398738353e-09, 1], [0.7227163910865784, 0.0654924064874649, -1.8168604398738353e-09, 1], [0.7325019240379333, 0.0675526037812233, -1.8168604398738353e-09, 1], [0.7422873973846436, 0.06961279362440109, -1.8168604398738353e-09, 1], [0.7520728707313538, 0.07167298346757889, -1.8168604398738353e-09, 1], [0.761858344078064, 0.07373318821191788, -1.8168604398738353e-09, 1], [0.7716438174247742, 0.07579337805509567, -1.8168604398738353e-09, 1], [0.7814292907714844, 0.07785357534885406, -1.8168604398738353e-09, 1], [0.7912147641181946, 0.07991376519203186, -1.8168604398738353e-09, 1], [0.8010002970695496, 0.08197396248579025, -1.8168604398738353e-09, 1], [0.810785710811615, 0.08403415977954865, -1.8168604398738353e-09, 1], [0.82057124376297, 0.08609434962272644, -1.8168604398738353e-09, 1], [0.8303566575050354, 0.08815454691648483, -1.8168604398738353e-09, 1], [0.8401421904563904, 0.09021474421024323, -1.8168604398738353e-09, 1], [0.8499276638031006, 0.09227494150400162, -1.8168604398738353e-09, 1], [0.8597131371498108, 0.09433513134717941, -1.8168604398738353e-09, 1], [0.869498610496521, 0.0963953286409378, -1.8168604398738353e-09, 1], [0.8792840838432312, 0.0984555184841156, -1.8168604398738353e-09, 1], [0.8890695571899414, 0.10051571577787399, -1.8168604398738353e-09, 1], [0.8988550901412964, 0.10257591307163239, -1.8168604398738353e-09, 1], [0.9086405038833618, 0.10463610291481018, -1.8168604398738353e-09, 1], [0.9184260368347168, 0.10669630020856857, -1.8168604398738353e-09, 1], [0.9282114505767822, 0.10875649750232697, -1.8168604398738353e-09, 1], [0.9379969835281372, 0.11081668734550476, -1.8168604398738353e-09, 1], [0.9477824568748474, 0.11287689208984375, -1.8168604398738353e-09, 1], [0.9575679302215576, 0.11493707448244095, -1.8168604398738353e-09, 1], [0.9673534035682678, 0.11699727922677994, -1.8168604398738353e-09, 1], [0.977138876914978, 0.11905746906995773, -1.8168604398738353e-09, 1], [0.9869243502616882, 0.12111766636371613, -1.8168604398738353e-09, 1], [0.9967098236083984, 0.12317785620689392, -1.8168604398738353e-09, 1], [1.0064953565597534, 0.1252380609512329, -1.8168604398738353e-09, 1], [1.0162807703018188, 0.1272982358932495, -1.8168604398738353e-09, 1], [1.0260663032531738, 0.1293584555387497, -1.8168604398738353e-09, 1], [1.0358517169952393, 0.1314186304807663, -1.8168604398738353e-09, 1], [1.0456372499465942, 0.13347883522510529, -1.8168604398738353e-09, 1], [1.0554226636886597, 0.13553902506828308, -1.8168604398738353e-09, 1], [1.0652081966400146, 0.13759922981262207, -1.8168604398738353e-09, 1], [1.0749937295913696, 0.13965941965579987, -1.8168604398738353e-09, 1], [1.084779143333435, 0.14171960949897766, -1.8168604398738353e-09, 1], [1.0945645570755005, 0.14377979934215546, -1.8168604398738353e-09, 1], [1.1043500900268555, 0.14584000408649445, -1.8168604398738353e-09, 1], [1.114135503768921, 0.14790019392967224, -1.8168604398738353e-09, 1], [1.1239211559295654, 0.14996039867401123, -1.8168604398738353e-09, 1], [1.1337064504623413, 0.15202058851718903, -1.8168604398738353e-09, 1], [1.1434921026229858, 0.15408077836036682, -1.8168604398738353e-09, 1], [1.1532775163650513, 0.15614096820354462, -1.8168604398738353e-09, 1], [1.1630629301071167, 0.1582011729478836, -1.8168604398738353e-09, 1], [1.1728484630584717, 0.1602613776922226, -1.8168604398738353e-09, 1], [1.1826339960098267, 0.1623215526342392, -1.8168604398738353e-09, 1], [1.192419409751892, 0.16438175737857819, -1.8168604398738353e-09, 1], [1.2022048234939575, 0.16644194722175598, -1.8168604398738353e-09, 1], [1.2022048234939575, 0.16644194722175598, 0.5235987901687622, 1], [1.192419409751892, 0.16438175737857819, 0.5235987901687622, 1], [1.1826339960098267, 0.1623215675354004, 0.5235987901687622, 1], [1.1728484630584717, 0.1602613627910614, 0.5235987901687622, 1], [1.1630629301071167, 0.1582011729478836, 0.5235987901687622, 1], [1.1532775163650513, 0.15614096820354462, 0.5235987901687622, 1], [1.1434919834136963, 0.15408077836036682, 0.5235987901687622, 1], [1.1337065696716309, 0.15202058851718903, 0.5235987901687622, 1], [1.1239210367202759, 0.14996039867401123, 0.5235987901687622, 1], [1.1141356229782104, 0.14790019392967224, 0.5235987901687622, 1], [1.1043500900268555, 0.14584000408649445, 0.5235987901687622, 1], [1.09456467628479, 0.14377979934215546, 0.5235987901687622, 1], [1.084779143333435, 0.14171962440013885, 0.5235987901687622, 1], [1.07499361038208, 0.13965940475463867, 0.5235987901687622, 1], [1.0652081966400146, 0.13759922981262207, 0.5235987901687622, 1], [1.0554227828979492, 0.13553902506828308, 0.5235987901687622, 1], [1.0456372499465942, 0.13347883522510529, 0.5235987901687622, 1], [1.0358517169952393, 0.1314186453819275, 0.5235987901687622, 1], [1.0260663032531738, 0.1293584406375885, 0.5235987901687622, 1], [1.0162807703018188, 0.1272982507944107, 0.5235987901687622, 1], [1.0064953565597534, 0.12523804605007172, 0.5235987901687622, 1], [0.9967097640037537, 0.12317786365747452, 0.5235987901687622, 1], [0.9869243502616882, 0.12111766636371613, 0.5235987901687622, 1], [0.9771389365196228, 0.11905746906995773, 0.5235987901687622, 1], [0.9673534035682678, 0.11699727177619934, 0.5235987901687622, 1], [0.9575678706169128, 0.11493708193302155, 0.5235987901687622, 1], [0.9477824568748474, 0.11287688463926315, 0.5235987901687622, 1], [0.9379969835281372, 0.11081668734550476, 0.5235987901687622, 1], [0.928211510181427, 0.10875649750232697, 0.5235987901687622, 1], [0.918425977230072, 0.10669630020856857, 0.5235987901687622, 1], [0.9086405038833618, 0.10463611036539078, 0.5235987901687622, 1], [0.8988550901412964, 0.10257591307163239, 0.5235987901687622, 1], [0.8890695571899414, 0.10051571577787399, 0.5235987901687622, 1], [0.8792840838432312, 0.0984555184841156, 0.5235987901687622, 1], [0.869498610496521, 0.0963953286409378, 0.5235987901687622, 1], [0.8597131371498108, 0.09433513134717941, 0.5235987901687622, 1], [0.8499276638031006, 0.09227493405342102, 0.5235987901687622, 1], [0.8401421904563904, 0.09021474421024323, 0.5235987901687622, 0], [0.8303566575050354, 0.08815454691648483, 0.5235987901687622, 0], [0.82057124376297, 0.08609435707330704, 0.5235987901687622, 0], [0.8107857704162598, 0.08403415232896805, 0.5235987901687622, 0], [0.8010002374649048, 0.08197396248579025, 0.5235987901687622, 1], [0.7912147641181946, 0.07991377264261246, 0.5235987901687622, 1], [0.7814292907714844, 0.07785357534885406, 0.5235987901687622, 1], [0.771643877029419, 0.07579337805509567, 0.5235987901687622, 1], [0.761858344078064, 0.07373318076133728, 0.5235987901687622, 1], [0.752072811126709, 0.07167299091815948, 0.5235987901687622, 1], [0.7422873973846436, 0.06961279362440109, 0.5235987901687622, 1], [0.7325019240379333, 0.0675525963306427, 0.5235987901687622, 1], [0.7227164506912231, 0.0654924064874649, 0.5235987901687622, 1], [0.7129309177398682, 0.06343220919370651, 0.5235987901687622, 1], [0.7031455039978027, 0.06137201935052872, 0.5235987901687622, 1], [0.6933599710464478, 0.059311818331480026, 0.5235987901687622, 1], [0.6835744976997375, 0.05725162476301193, 0.5235987901687622, 1], [0.6737890839576721, 0.05519143119454384, 0.5235987901687622, 1], [0.6640035510063171, 0.053131237626075745, 0.5235987901687622, 1], [0.6542180776596069, 0.05107104033231735, 0.5235987901687622, 1], [0.6444326043128967, 0.04901084676384926, 0.5235987901687622, 1], [0.6346470713615417, 0.046950649470090866, 0.5235987901687622, 1], [0.6248616576194763, 0.04489045962691307, 0.5235987901687622, 1], [0.6150761842727661, 0.04283025860786438, 0.5235987901687622, 1], [0.6052906513214111, 0.040770068764686584, 0.5235987901687622, 1], [0.5955052375793457, 0.03870987147092819, 0.5235987901687622, 1], [0.5857197046279907, 0.0366496779024601, 0.5235987901687622, 1], [0.5759342312812805, 0.034589484333992004, 0.5235987901687622, 1], [0.5661487579345703, 0.03252928704023361, 0.5235987901687622, 1], [0.5563632845878601, 0.030469093471765518, 0.5235987901687622, 1], [0.5465778112411499, 0.028408898040652275, 0.5235987901687622, 1], [0.5367923378944397, 0.026348702609539032, 0.5235987901687622, 1], [0.5270068645477295, 0.024288509041070938, 0.5235987901687622, 1], [0.5172213912010193, 0.022228313609957695, 0.5235987901687622, 1], [0.5074358582496643, 0.0201681200414896, 0.5235987901687622, 1], [0.4976504445075989, 0.01810792274773121, 0.5235987901687622, 1], [0.4878649413585663, 0.016047729179263115, 0.5235987901687622, 1], [0.4780794382095337, 0.013987535610795021, 0.5235987901687622, 1], [0.4682939946651459, 0.011927339248359203, 0.5235987901687622, 1], [0.4585084915161133, 0.00986714567989111, 0.5235987901687622, 1], [0.4487230181694031, 0.007806949783116579, 0.5235987901687622, 1], [0.43893754482269287, 0.005746755283325911, 0.5235987901687622, 1], [0.42915207147598267, 0.003686560783535242, 0.5235987901687622, 1], [0.4193665683269501, 0.0016263657016679645, 0.5235987901687622, 1], [0.4193665683269501, 0.0016263657016679645, 1.0471975803375244, 1], [0.42915207147598267, 0.003686560783535242, 1.0471975803375244, 1], [0.43893754482269287, 0.005746755283325911, 1.0471975803375244, 1], [0.4487230181694031, 0.007806950248777866, 1.0471975803375244, 1], [0.4585084915161133, 0.009867144748568535, 1.0471975803375244, 1], [0.4682939648628235, 0.011927340179681778, 1.0471975803375244, 1], [0.4780794680118561, 0.013987534679472446, 1.0471975803375244, 1], [0.4878649413585663, 0.016047729179263115, 1.0471975803375244, 1], [0.4976504147052765, 0.018107924610376358, 1.0471975803375244, 1], [0.5074358582496643, 0.020168118178844452, 1.0471975803375244, 1], [0.5172213912010193, 0.022228313609957695, 1.0471975803375244, 1], [0.5270068645477295, 0.024288509041070938, 1.0471975803375244, 1], [0.5367923378944397, 0.02634870447218418, 1.0471975803375244, 1], [0.5465778112411499, 0.028408898040652275, 1.0471975803375244, 1], [0.5563632845878601, 0.03046909160912037, 1.0471975803375244, 1], [0.5661487579345703, 0.03252928704023361, 1.0471975803375244, 1], [0.5759342312812805, 0.034589484333992004, 1.0471975803375244, 1], [0.5857197642326355, 0.0366496779024601, 1.0471975803375244, 1], [0.5955051779747009, 0.03870987147092819, 1.0471975803375244, 1], [0.6052907109260559, 0.040770068764686584, 1.0471975803375244, 1], [0.6150761246681213, 0.04283026233315468, 1.0471975803375244, 1], [0.6248616576194763, 0.04489045590162277, 1.0471975803375244, 1], [0.6346471309661865, 0.046950649470090866, 1.0471975803375244, 1], [0.6444326043128967, 0.04901084676384926, 1.0471975803375244, 1], [0.6542180776596069, 0.05107104033231735, 1.0471975803375244, 1], [0.6640035510063171, 0.053131237626075745, 1.0471975803375244, 1], [0.6737890243530273, 0.05519143119454384, 1.0471975803375244, 1], [0.6835744976997375, 0.05725162476301193, 1.0471975803375244, 1], [0.6933600306510925, 0.059311822056770325, 1.0471975803375244, 1], [0.703145444393158, 0.06137201189994812, 1.0471975803375244, 1], [0.7129309773445129, 0.06343220919370651, 1.0471975803375244, 1], [0.7227163910865784, 0.0654924064874649, 1.0471975803375244, 1], [0.7325019240379333, 0.0675526037812233, 1.0471975803375244, 1], [0.7422873973846436, 0.06961279362440109, 1.0471975803375244, 1], [0.7520728707313538, 0.07167298346757889, 1.0471975803375244, 1], [0.761858344078064, 0.07373318821191788, 1.0471975803375244, 1], [0.7716438174247742, 0.07579337805509567, 1.0471975803375244, 0], [0.7814292907714844, 0.07785357534885406, 1.0471975803375244, 0], [0.7912147641181946, 0.07991376519203186, 1.0471975803375244, 0], [0.8010002970695496, 0.08197396248579025, 1.0471975803375244, 0], [0.810785710811615, 0.08403415977954865, 1.0471975803375244, 0], [0.82057124376297, 0.08609434962272644, 1.0471975803375244, 0], [0.8303566575050354, 0.08815454691648483, 1.0471975803375244, 0], [0.8401421904563904, 0.09021474421024323, 1.0471975803375244, 0], [0.8499276638031006, 0.09227494150400162, 1.0471975803375244, 0], [0.8597131371498108, 0.09433513134717941, 1.0471975803375244, 0], [0.869498610496521, 0.0963953286409378, 1.0471975803375244, 0], [0.8792840838432312, 0.0984555184841156, 1.0471975803375244, 0], [0.8890695571899414, 0.10051571577787399, 1.0471975803375244, 0], [0.8988550901412964, 0.10257591307163239, 1.0471975803375244, 0], [0.9086405038833618, 0.10463610291481018, 1.0471975803375244, 0], [0.9184260368347168, 0.10669630020856857, 1.0471975803375244, 0], [0.9282114505767822, 0.10875649750232697, 1.0471975803375244, 0], [0.9379969835281372, 0.11081668734550476, 1.0471975803375244, 0], [0.9477824568748474, 0.11287689208984375, 1.0471975803375244, 1], [0.9575679302215576, 0.11493707448244095, 1.0471975803375244, 1], [0.9673534035682678, 0.11699727922677994, 1.0471975803375244, 1], [0.977138876914978, 0.11905746906995773, 1.0471975803375244, 1], [0.9869243502616882, 0.12111766636371613, 1.0471975803375244, 1], [0.9967098236083984, 0.12317785620689392, 1.0471975803375244, 1], [1.0064953565597534, 0.1252380609512329, 1.0471975803375244, 1], [1.0162807703018188, 0.1272982358932495, 1.0471975803375244, 1], [1.0260663032531738, 0.1293584555387497, 1.0471975803375244, 1], [1.0358517169952393, 0.1314186304807663, 1.0471975803375244, 1], [1.0456372499465942, 0.13347883522510529, 1.0471975803375244, 1], [1.0554226636886597, 0.13553902506828308, 1.0471975803375244, 1], [1.0652081966400146, 0.13759922981262207, 1.0471975803375244, 1], [1.0749937295913696, 0.13965941965579987, 1.0471975803375244, 1], [1.084779143333435, 0.14171960949897766, 1.0471975803375244, 1], [1.0945645570755005, 0.14377979934215546, 1.0471975803375244, 1], [1.1043500900268555, 0.14584000408649445, 1.0471975803375244, 1], [1.114135503768921, 0.14790019392967224, 1.0471975803375244, 1], [1.1239211559295654, 0.14996039867401123, 1.0471975803375244, 1], [1.1337064504623413, 0.15202058851718903, 1.0471975803375244, 1], [1.1434921026229858, 0.15408077836036682, 1.0471975803375244, 1], [1.1532775163650513, 0.15614096820354462, 1.0471975803375244, 1], [1.1630629301071167, 0.1582011729478836, 1.0471975803375244, 1], [1.1728484630584717, 0.1602613776922226, 1.0471975803375244, 1], [1.1826339960098267, 0.1623215526342392, 1.0471975803375244, 1], [1.192419409751892, 0.16438175737857819, 1.0471975803375244, 1], [1.2022048234939575, 0.16644194722175598, 1.0471975803375244, 1], [1.2022048234939575, 0.16644194722175598, 1.5707963705062866, 1], [1.192419409751892, 0.16438175737857819, 1.5707963705062866, 1], [1.1826339960098267, 0.1623215675354004, 1.5707963705062866, 1], [1.1728484630584717, 0.1602613627910614, 1.5707963705062866, 1], [1.1630629301071167, 0.1582011729478836, 1.5707963705062866, 1], [1.1532775163650513, 0.15614096820354462, 1.5707963705062866, 1], [1.1434919834136963, 0.15408077836036682, 1.5707963705062866, 1], [1.1337065696716309, 0.15202058851718903, 1.5707963705062866, 1], [1.1239210367202759, 0.14996039867401123, 1.5707963705062866, 1], [1.1141356229782104, 0.14790019392967224, 1.5707963705062866, 1], [1.1043500900268555, 0.14584000408649445, 1.5707963705062866, 1], [1.09456467628479, 0.14377979934215546, 1.5707963705062866, 1], [1.084779143333435, 0.14171962440013885, 1.5707963705062866, 1], [1.07499361038208, 0.13965940475463867, 1.5707963705062866, 1], [1.0652081966400146, 0.13759922981262207, 1.5707963705062866, 1], [1.0554227828979492, 0.13553902506828308, 1.5707963705062866, 1], [1.0456372499465942, 0.13347883522510529, 1.5707963705062866, 1], [1.0358517169952393, 0.1314186453819275, 1.5707963705062866, 1], [1.0260663032531738, 0.1293584406375885, 1.5707963705062866, 1], [1.0162807703018188, 0.1272982507944107, 1.5707963705062866, 1], [1.0064953565597534, 0.12523804605007172, 1.5707963705062866, 1], [0.9967097640037537, 0.12317786365747452, 1.5707963705062866, 1], [0.9869243502616882, 0.12111766636371613, 1.5707963705062866, 1], [0.9771389365196228, 0.11905746906995773, 1.5707963705062866, 1], [0.9673534035682678, 0.11699727177619934, 1.5707963705062866, 1], [0.9575678706169128, 0.11493708193302155, 1.5707963705062866, 1], [0.9477824568748474, 0.11287688463926315, 1.5707963705062866, 1], [0.9379969835281372, 0.11081668734550476, 1.5707963705062866, 1], [0.928211510181427, 0.10875649750232697, 1.5707963705062866, 1], [0.918425977230072, 0.10669630020856857, 1.5707963705062866, 1], [0.9086405038833618, 0.10463611036539078, 1.5707963705062866, 1], [0.8988550901412964, 0.10257591307163239, 1.5707963705062866, 0], [0.8890695571899414, 0.10051571577787399, 1.5707963705062866, 0], [0.8792840838432312, 0.0984555184841156, 1.5707963705062866, 0], [0.869498610496521, 0.0963953286409378, 1.5707963705062866, 0], [0.8597131371498108, 0.09433513134717941, 1.5707963705062866, 0], [0.8499276638031006, 0.09227493405342102, 1.5707963705062866, 0], [0.8401421904563904, 0.09021474421024323, 1.5707963705062866, 0], [0.8303566575050354, 0.08815454691648483, 1.5707963705062866, 0], [0.82057124376297, 0.08609435707330704, 1.5707963705062866, 0], [0.8107857704162598, 0.08403415232896805, 1.5707963705062866, 0], [0.8010002374649048, 0.08197396248579025, 1.5707963705062866, 0], [0.7912147641181946, 0.07991377264261246, 1.5707963705062866, 0], [0.7814292907714844, 0.07785357534885406, 1.5707963705062866, 0], [0.771643877029419, 0.07579337805509567, 1.5707963705062866, 0], [0.761858344078064, 0.07373318076133728, 1.5707963705062866, 0], [0.752072811126709, 0.07167299091815948, 1.5707963705062866, 0], [0.7422873973846436, 0.06961279362440109, 1.5707963705062866, 0], [0.7325019240379333, 0.0675525963306427, 1.5707963705062866, 0], [0.7227164506912231, 0.0654924064874649, 1.5707963705062866, 1], [0.7129309177398682, 0.06343220919370651, 1.5707963705062866, 1], [0.7031455039978027, 0.06137201935052872, 1.5707963705062866, 1], [0.6933599710464478, 0.059311818331480026, 1.5707963705062866, 1], [0.6835744976997375, 0.05725162476301193, 1.5707963705062866, 1], [0.6737890839576721, 0.05519143119454384, 1.5707963705062866, 1], [0.6640035510063171, 0.053131237626075745, 1.5707963705062866, 1], [0.6542180776596069, 0.05107104033231735, 1.5707963705062866, 1], [0.6444326043128967, 0.04901084676384926, 1.5707963705062866, 1], [0.6346470713615417, 0.046950649470090866, 1.5707963705062866, 1], [0.6248616576194763, 0.04489045962691307, 1.5707963705062866, 1], [0.6150761842727661, 0.04283025860786438, 1.5707963705062866, 1], [0.6052906513214111, 0.040770068764686584, 1.5707963705062866, 1], [0.5955052375793457, 0.03870987147092819, 1.5707963705062866, 1], [0.5857197046279907, 0.0366496779024601, 1.5707963705062866, 1], [0.5759342312812805, 0.034589484333992004, 1.5707963705062866, 1], [0.5661487579345703, 0.03252928704023361, 1.5707963705062866, 1], [0.5563632845878601, 0.030469093471765518, 1.5707963705062866, 1], [0.5465778112411499, 0.028408898040652275, 1.5707963705062866, 1], [0.5367923378944397, 0.026348702609539032, 1.5707963705062866, 1], [0.5270068645477295, 0.024288509041070938, 1.5707963705062866, 1], [0.5172213912010193, 0.022228313609957695, 1.5707963705062866, 1], [0.5074358582496643, 0.0201681200414896, 1.5707963705062866, 1], [0.4976504445075989, 0.01810792274773121, 1.5707963705062866, 1], [0.4878649413585663, 0.016047729179263115, 1.5707963705062866, 1], [0.4780794382095337, 0.013987535610795021, 1.5707963705062866, 1], [0.4682939946651459, 0.011927339248359203, 1.5707963705062866, 1], [0.4585084915161133, 0.00986714567989111, 1.5707963705062866, 1], [0.4487230181694031, 0.007806949783116579, 1.5707963705062866, 1], [0.43893754482269287, 0.005746755283325911, 1.5707963705062866, 1], [0.42915207147598267, 0.0036865605507045984, 1.5707963705062866, 1], [0.4193665683269501, 0.0016263659344986081, 1.5707963705062866, 1], [0.4193665683269501, 0.0016263659344986081, 2.094395160675049, 1], [0.42915207147598267, 0.0036865605507045984, 2.094395160675049, 1], [0.43893754482269287, 0.005746755283325911, 2.094395160675049, 1], [0.4487230181694031, 0.007806950248777866, 2.094395160675049, 1], [0.4585084915161133, 0.009867144748568535, 2.094395160675049, 1], [0.4682939648628235, 0.011927340179681778, 2.094395160675049, 1], [0.4780794680118561, 0.013987534679472446, 2.094395160675049, 1], [0.4878649413585663, 0.016047729179263115, 2.094395160675049, 1], [0.4976504147052765, 0.018107924610376358, 2.094395160675049, 1], [0.5074358582496643, 0.020168118178844452, 2.094395160675049, 1], [0.5172213912010193, 0.022228313609957695, 2.094395160675049, 1], [0.5270068645477295, 0.024288509041070938, 2.094395160675049, 1], [0.5367923378944397, 0.02634870447218418, 2.094395160675049, 1], [0.5465778112411499, 0.028408898040652275, 2.094395160675049, 1], [0.5563632845878601, 0.030469093471765518, 2.094395160675049, 1], [0.5661487579345703, 0.03252928704023361, 2.094395160675049, 1], [0.5759342312812805, 0.034589484333992004, 2.094395160675049, 1], [0.5857197642326355, 0.0366496741771698, 2.094395160675049, 1], [0.5955051779747009, 0.03870987519621849, 2.094395160675049, 1], [0.6052907109260559, 0.040770065039396286, 2.094395160675049, 1], [0.6150761246681213, 0.04283026233315468, 2.094395160675049, 1], [0.6248616576194763, 0.04489045590162277, 2.094395160675049, 1], [0.6346471309661865, 0.046950653195381165, 2.094395160675049, 1], [0.6444326043128967, 0.04901084676384926, 2.094395160675049, 1], [0.6542180776596069, 0.05107104033231735, 2.094395160675049, 1], [0.6640035510063171, 0.053131233900785446, 2.094395160675049, 1], [0.6737890243530273, 0.05519143119454384, 2.094395160675049, 1], [0.6835744976997375, 0.05725162848830223, 2.094395160675049, 1], [0.6933600306510925, 0.059311818331480026, 2.094395160675049, 0], [0.703145444393158, 0.06137201562523842, 2.094395160675049, 0], [0.7129309773445129, 0.06343220919370651, 2.094395160675049, 0], [0.7227163910865784, 0.0654924064874649, 2.094395160675049, 0], [0.7325019240379333, 0.0675525963306427, 2.094395160675049, 0], [0.7422873973846436, 0.06961279362440109, 2.094395160675049, 0], [0.7520728707313538, 0.07167299091815948, 2.094395160675049, 0], [0.761858344078064, 0.07373318821191788, 2.094395160675049, 0], [0.7716438174247742, 0.07579337805509567, 2.094395160675049, 0], [0.7814292907714844, 0.07785356789827347, 2.094395160675049, 0], [0.7912147641181946, 0.07991377264261246, 2.094395160675049, 0], [0.8010002970695496, 0.08197396248579025, 2.094395160675049, 0], [0.810785710811615, 0.08403415977954865, 2.094395160675049, 0], [0.82057124376297, 0.08609434962272644, 2.094395160675049, 0], [0.8303566575050354, 0.08815454691648483, 2.094395160675049, 0], [0.8401421904563904, 0.09021474421024323, 2.094395160675049, 0], [0.8499276638031006, 0.09227493405342102, 2.094395160675049, 0], [0.8597131371498108, 0.09433513879776001, 2.094395160675049, 0], [0.869498610496521, 0.09639532119035721, 2.094395160675049, 1], [0.8792840838432312, 0.0984555259346962, 2.094395160675049, 1], [0.8890695571899414, 0.10051571577787399, 2.094395160675049, 1], [0.8988550901412964, 0.10257591307163239, 2.094395160675049, 1], [0.9086405038833618, 0.10463610291481018, 2.094395160675049, 1], [0.9184260368347168, 0.10669630020856857, 2.094395160675049, 1], [0.9282114505767822, 0.10875649750232697, 2.094395160675049, 1], [0.9379969835281372, 0.11081668734550476, 2.094395160675049, 1], [0.9477824568748474, 0.11287688463926315, 2.094395160675049, 1], [0.9575679302215576, 0.11493708193302155, 2.094395160675049, 1], [0.9673534035682678, 0.11699727922677994, 2.094395160675049, 1], [0.977138876914978, 0.11905746906995773, 2.094395160675049, 1], [0.9869243502616882, 0.12111765891313553, 2.094395160675049, 1], [0.9967098236083984, 0.12317786365747452, 2.094395160675049, 1], [1.0064953565597534, 0.12523804605007172, 2.094395160675049, 1], [1.0162807703018188, 0.1272982507944107, 2.094395160675049, 1], [1.0260663032531738, 0.1293584555387497, 2.094395160675049, 1], [1.0358517169952393, 0.1314186304807663, 2.094395160675049, 1], [1.0456372499465942, 0.13347883522510529, 2.094395160675049, 1], [1.0554226636886597, 0.13553902506828308, 2.094395160675049, 1], [1.0652081966400146, 0.13759922981262207, 2.094395160675049, 1], [1.0749937295913696, 0.13965941965579987, 2.094395160675049, 1], [1.084779143333435, 0.14171960949897766, 2.094395160675049, 1], [1.0945645570755005, 0.14377979934215546, 2.094395160675049, 1], [1.1043500900268555, 0.14584000408649445, 2.094395160675049, 1], [1.114135503768921, 0.14790019392967224, 2.094395160675049, 1], [1.1239211559295654, 0.14996039867401123, 2.094395160675049, 1], [1.1337064504623413, 0.15202058851718903, 2.094395160675049, 1], [1.1434921026229858, 0.15408077836036682, 2.094395160675049, 1], [1.1532775163650513, 0.15614096820354462, 2.094395160675049, 1], [1.1630629301071167, 0.1582011729478836, 2.094395160675049, 1], [1.1728484630584717, 0.1602613627910614, 2.094395160675049, 1], [1.1826339960098267, 0.1623215675354004, 2.094395160675049, 1], [1.192419409751892, 0.16438175737857819, 2.094395160675049, 1], [1.2022048234939575, 0.16644194722175598, 2.094395160675049, 1], [1.2022048234939575, 0.16644194722175598, 2.6179938316345215, 1], [1.192419409751892, 0.16438175737857819, 2.6179938316345215, 1], [1.1826339960098267, 0.1623215526342392, 2.6179938316345215, 1], [1.1728484630584717, 0.1602613776922226, 2.6179938316345215, 1], [1.1630629301071167, 0.1582011729478836, 2.6179938316345215, 1], [1.1532775163650513, 0.15614096820354462, 2.6179938316345215, 1], [1.1434919834136963, 0.15408077836036682, 2.6179938316345215, 1], [1.1337065696716309, 0.15202058851718903, 2.6179938316345215, 1], [1.1239210367202759, 0.14996039867401123, 2.6179938316345215, 1], [1.1141356229782104, 0.14790019392967224, 2.6179938316345215, 1], [1.1043500900268555, 0.14584000408649445, 2.6179938316345215, 1], [1.09456467628479, 0.14377979934215546, 2.6179938316345215, 1], [1.084779143333435, 0.14171962440013885, 2.6179938316345215, 1], [1.07499361038208, 0.13965940475463867, 2.6179938316345215, 1], [1.0652081966400146, 0.13759922981262207, 2.6179938316345215, 1], [1.0554227828979492, 0.13553902506828308, 2.6179938316345215, 1], [1.0456372499465942, 0.13347883522510529, 2.6179938316345215, 1], [1.0358517169952393, 0.1314186453819275, 2.6179938316345215, 1], [1.0260663032531738, 0.1293584406375885, 2.6179938316345215, 1], [1.0162807703018188, 0.1272982507944107, 2.6179938316345215, 1], [1.0064953565597534, 0.12523804605007172, 2.6179938316345215, 1], [0.9967097640037537, 0.12317786365747452, 2.6179938316345215, 1], [0.9869243502616882, 0.12111766636371613, 2.6179938316345215, 1], [0.9771389365196228, 0.11905746906995773, 2.6179938316345215, 1], [0.9673534035682678, 0.11699727177619934, 2.6179938316345215, 1], [0.9575678706169128, 0.11493708193302155, 2.6179938316345215, 1], [0.9477824568748474, 0.11287688463926315, 2.6179938316345215, 1], [0.9379969835281372, 0.11081668734550476, 2.6179938316345215, 1], [0.928211510181427, 0.10875649750232697, 2.6179938316345215, 1], [0.918425977230072, 0.10669630020856857, 2.6179938316345215, 1], [0.9086405038833618, 0.10463611036539078, 2.6179938316345215, 1], [0.8988550901412964, 0.10257590562105179, 2.6179938316345215, 1], [0.8890695571899414, 0.10051571577787399, 2.6179938316345215, 1], [0.8792840838432312, 0.0984555259346962, 2.6179938316345215, 1], [0.869498610496521, 0.0963953286409378, 2.6179938316345215, 1], [0.8597131371498108, 0.09433513134717941, 2.6179938316345215, 1], [0.8499276638031006, 0.09227493405342102, 2.6179938316345215, 1], [0.8401421904563904, 0.09021474421024323, 2.6179938316345215, 1], [0.8303566575050354, 0.08815454691648483, 2.6179938316345215, 1], [0.82057124376297, 0.08609434962272644, 2.6179938316345215, 1], [0.8107857704162598, 0.08403415977954865, 2.6179938316345215, 1], [0.8010002374649048, 0.08197396248579025, 2.6179938316345215, 1], [0.7912147641181946, 0.07991377264261246, 2.6179938316345215, 1], [0.7814292907714844, 0.07785356789827347, 2.6179938316345215, 1], [0.771643877029419, 0.07579338550567627, 2.6179938316345215, 1], [0.761858344078064, 0.07373318076133728, 2.6179938316345215, 1], [0.752072811126709, 0.07167299091815948, 2.6179938316345215, 1], [0.7422873973846436, 0.06961279362440109, 2.6179938316345215, 1], [0.7325019240379333, 0.0675525963306427, 2.6179938316345215, 1], [0.7227164506912231, 0.0654924064874649, 2.6179938316345215, 1], [0.7129309177398682, 0.06343220919370651, 2.6179938316345215, 1], [0.7031455039978027, 0.06137201562523842, 2.6179938316345215, 1], [0.6933599710464478, 0.059311822056770325, 2.6179938316345215, 1], [0.6835744976997375, 0.05725162476301193, 2.6179938316345215, 1], [0.6737890839576721, 0.05519143119454384, 2.6179938316345215, 1], [0.6640035510063171, 0.053131233900785446, 2.6179938316345215, 0], [0.6542180776596069, 0.05107104405760765, 2.6179938316345215, 0], [0.6444326043128967, 0.04901084303855896, 2.6179938316345215, 1], [0.6346470713615417, 0.046950653195381165, 2.6179938316345215, 1], [0.6248616576194763, 0.04489045590162277, 2.6179938316345215, 1], [0.6150761842727661, 0.04283026233315468, 2.6179938316345215, 1], [0.6052906513214111, 0.040770068764686584, 2.6179938316345215, 1], [0.5955052375793457, 0.03870987147092819, 2.6179938316345215, 1], [0.5857197046279907, 0.0366496779024601, 2.6179938316345215, 1], [0.5759342312812805, 0.034589480608701706, 2.6179938316345215, 1], [0.5661487579345703, 0.03252928704023361, 2.6179938316345215, 1], [0.5563632845878601, 0.030469095334410667, 2.6179938316345215, 1], [0.5465778112411499, 0.028408898040652275, 2.6179938316345215, 1], [0.5367923378944397, 0.026348702609539032, 2.6179938316345215, 1], [0.5270068645477295, 0.024288509041070938, 2.6179938316345215, 1], [0.5172213912010193, 0.022228313609957695, 2.6179938316345215, 1], [0.5074358582496643, 0.0201681200414896, 2.6179938316345215, 1], [0.4976504445075989, 0.01810792274773121, 2.6179938316345215, 1], [0.4878649413585663, 0.016047731041908264, 2.6179938316345215, 1], [0.4780794382095337, 0.013987533748149872, 2.6179938316345215, 1], [0.4682939946651459, 0.011927340179681778, 2.6179938316345215, 1], [0.4585084915161133, 0.009867144748568535, 2.6179938316345215, 1], [0.4487230181694031, 0.007806950248777866, 2.6179938316345215, 1], [0.43893754482269287, 0.005746755283325911, 2.6179938316345215, 1], [0.42915207147598267, 0.0036865603178739548, 2.6179938316345215, 1], [0.4193665683269501, 0.0016263659344986081, 2.6179938316345215, 1]]
\ No newline at end of file
diff --git a/probe_vis_fit.py b/probe_vis_fit.py
new file mode 100644
index 0000000..b120cf4
--- /dev/null
+++ b/probe_vis_fit.py
@@ -0,0 +1,16 @@
           1 +import numpy as np
           2 +from probe_vis_geo import cam, segd
           3 +exec(open('probe_vis_geo2.py').read().split('for th')[0].split('\n',2)[2])
           4 +b=(-1.5267,0.3485)
           5 +best=[]
           6 +for ox in np.arange(-0.25,0.2501,0.0025):
           7 +  for oy in np.arange(-0.25,0.2501,0.0025):
           8 +    sc=0
           9 +    for v,o,p in [(v1,(-2.176,1.837),(-1.717,0.906)),(v2,(-0.4922,1.8822),(-0.907,1.268))]:
          10 +        offs=np.array([segd(cam(b,np.deg2rad(t),ox,oy),o,p)[1] for t in sorted(v)]); vis=np.array([v[t] for t in sorted(v)])
          11 +        # best interval [lo,hi] of invisibles: count errors
          12 +        bi=offs[vis==0]; lo,hi=bi.min(),bi.max()
          13 +        err=np.sum((offs>=lo)&(offs<=hi)&(vis==1))
          14 +        sc+=err
          15 +    best.append((sc,round(ox,4),round(oy,4)))
          16 +best.sort(); print(best[:15])
diff --git a/probe_vis_fit2.py b/probe_vis_fit2.py
new file mode 100644
index 0000000..46587d1
--- /dev/null
+++ b/probe_vis_fit2.py
@@ -0,0 +1,7 @@
           1 +import numpy as np
           2 +from probe_vis_geo import cam, segd
           3 +b=(0.81,0.083); o=(0.44,1.845); p=(0.735,0.444)
           4 +s="-180:0 -165:0 -150:1 -135:1 -120:1 -105:1 -90:1 -75:1 -60:1 -45:1 -30:1 -15:1 0:1 15:0 30:0 45:0 60:0 75:0 90:0 105:0 120:0 135:0 150:1 165:0"
           5 +for kv in s.split():
           6 +    t,v=map(int,kv.split(':')); c=cam(b,np.deg2rad(t))
           7 +    print(t,v,f"{segd(c,o,p)[1]:+.4f}", c.round(3), round(np.linalg.norm(c-np.array(o)),3))
diff --git a/probe_vis_fit3.py b/probe_vis_fit3.py
new file mode 100644
index 0000000..6e1976d
--- /dev/null
+++ b/probe_vis_fit3.py
@@ -0,0 +1,40 @@
           1 +import numpy as np
           2 +from probe_vis_geo import cam
           3 +from probe_vis_fit2 import s as s0
           4 +boxes=[(2.0,2.0,0.05,.25,.25,.05),(-2,2,.05,.25,.25,.05),(-0.215,-0.556,.201,.05,.05,.2),(0.735,0.444,.201,.05,.05,.2),(0.5,2,.05,.25,.25,.05),(-0.5,2,.05,.25,.25,.05),
           5 +(2.118,-0.961,.201,.05,.05,.2),(-1.717,0.906,.201,.05,.05,.2),(1.64,0.734,.201,.05,.05,.2),(1.786,-0.54,.201,.05,.05,.2),(-0.907,1.268,.201,.05,.05,.2),(-2.156,-1.004,.201,.05,.05,.2)]
           6 +O={'o0':(0.44,1.845,0.201),'o1':(-2.176,1.837,0.201),'o2':(-0.4922,1.8822,0.201)}
           7 +def hit(a,b,bx,eps=0.0):
           8 +    a=np.array(a);b=np.array(b);c=np.array(bx[:3]);h=np.array(bx[3:])+eps
           9 +    d=b-a; t0,t1=0.0,1.0
          10 +    for i in range(3):
          11 +        if abs(d[i])<1e-12:
          12 +            if abs(a[i]-c[i])>h[i]: return False
          13 +            continue
          14 +        ta=(c[i]-h[i]-a[i])/d[i]; tb=(c[i]+h[i]-a[i])/d[i]
          15 +        if ta>tb: ta,tb=tb,ta
          16 +        t0=max(t0,ta); t1=min(t1,tb)
          17 +        if t0>t1: return False
          18 +    return True
          19 +D=[]
          20 +for kv in s0.split():
          21 +    t,v=map(int,kv.split(':')); D.append(((0.81,0.083),t,'o0',v))
          22 +v1={-180:0,-165:0,-150:0,-135:1,-120:1,-105:1,-90:1,-75:1,-60:1,-45:1,-30:1,-15:1,0:1,15:1,30:1,45:1,60:1,75:1,90:0,105:0,120:0,135:0,150:0,165:1}
          23 +v2={-180:1,-165:1,-150:1,-135:1,-120:1,-105:1,-90:1,-75:1,-60:1,-45:1,-30:0,-15:0,0:1,15:0,30:0,45:0,60:0,75:0,90:0,105:1,120:0,135:0,150:0,165:1}
          24 +for t in v1: D.append(((-1.5267,0.3485),t,'o1',v1[t])); D.append(((-1.5267,0.3485),t,'o2',v2[t]))
          25 +D+= [((0.8138,0.0714),180,'o0',1),((0.8137,0.0719),180,'o0',0),((-1.5,0.25),0,'o2',0),((-1.57,0.31),0,'o2',1)]
          26 +def score(hc,zt=0.201,eps=0.0,ox=-0.087,oy=-0.0125,verbose=False):
          27 +    err=0
          28 +    for b,t,o,v in D:
          29 +        c=cam(b,np.deg2rad(t),ox,oy); a=(c[0],c[1],hc); ob=O[o]; tgt=(ob[0],ob[1],zt)
          30 +        vis= not any(hit(a,tgt,bx,eps) for bx in boxes)
          31 +        if vis!=bool(v):
          32 +            err+=1
          33 +            if verbose: print('miss',b,t,o,v)
          34 +    return err
          35 +if __name__=='__main__':
          36 +    res=[]
          37 +    for hc in np.arange(0.05,1.0,0.01):
          38 +      for zt in [0.15,0.201,0.25,0.3]:
          39 +        res.append((score(hc,zt),round(hc,3),zt))
          40 +    res.sort(); print(len(D),res[:10])
diff --git a/probe_vis_geo.py b/probe_vis_geo.py
new file mode 100644
index 0000000..2ff4845
--- /dev/null
+++ b/probe_vis_geo.py
@@ -0,0 +1,13 @@
           1 +import numpy as np
           2 +pill={'p5':(-1.717,0.906),'p8':(-0.907,1.268)}
           3 +objs={'o1':(-2.176,1.837),'o2':(-0.4922,1.8822)}
           4 +def cam(b,th,ox=-0.087,oy=-0.0125):
           5 +    return np.array([b[0]+ox*np.cos(th)-oy*np.sin(th), b[1]+ox*np.sin(th)+oy*np.cos(th)])
           6 +def segd(a,b,p):
           7 +    a,b,p=map(np.array,(a,b,p)); d=b-a; t=np.clip(np.dot(p-a,d)/np.dot(d,d),0,1); return np.linalg.norm(a+t*d-p), np.cross(d,p-a)/np.linalg.norm(d)
           8 +import sys
           9 +if __name__=='__main__':
          10 +  b=eval(sys.argv[1])
          11 +  for thd in eval(sys.argv[2]):
          12 +    c=cam(b,np.deg2rad(thd)); s=[f"{o}:{np.linalg.norm(c-np.array(op)):.3f} "+" ".join(f"{pn}={segd(c,op,pp)[1]:+.4f}" for pn,pp in pill.items()) for o,op in objs.items()]
          13 +    print(thd,c.round(4),' | '.join(s))
diff --git a/probe_vis_geo2.py b/probe_vis_geo2.py
new file mode 100644
index 0000000..e59d5bc
--- /dev/null
+++ b/probe_vis_geo2.py
@@ -0,0 +1,8 @@
           1 +import numpy as np
           2 +from probe_vis_geo import cam, segd
           3 +b=(-1.5267,0.3485)
           4 +v1={-180:0,-165:0,-150:0,-135:1,-120:1,-105:1,-90:1,-75:1,-60:1,-45:1,-30:1,-15:1,0:1,15:1,30:1,45:1,60:1,75:1,90:0,105:0,120:0,135:0,150:0,165:1}
           5 +v2={-180:1,-165:1,-150:1,-135:1,-120:1,-105:1,-90:1,-75:1,-60:1,-45:1,-30:0,-15:0,0:1,15:0,30:0,45:0,60:0,75:0,90:0,105:1,120:0,135:0,150:0,165:1}
           6 +for th in sorted(v1):
           7 +    c=cam(b,np.deg2rad(th))
           8 +    print(th, v1[th], f"{segd(c,(-2.176,1.837),(-1.717,0.906))[1]:+.4f}", v2[th], f"{segd(c,(-0.4922,1.8822),(-0.907,1.268))[1]:+.4f}")
diff --git a/probe_vis_lib.py b/probe_vis_lib.py
new file mode 100644
index 0000000..4356bba
--- /dev/null
+++ b/probe_vis_lib.py
@@ -0,0 +1,66 @@
           1 +from env_client import make_env
           2 +import numpy as np, time
           3 +env=make_env()
           4 +RV='rover1'
           5 +def reset(seed):
           6 +    global obs, r1, T
           7 +    obs,info=env.reset(seed=seed)
           8 +    T={t.name:t for t in env.observation_space.types}
           9 +    r1=obs.get_object_from_name(RV)
          10 +    return obs
          11 +def pos(): return np.array([obs.get(r1,'x'),obs.get(r1,'y'),obs.get(r1,'theta')])
          12 +def step(dx=0,dy=0,dth=0,op=1/6):
          13 +    global obs
          14 +    a=[0,0,0,1/6]; b=[dx,dy,dth,op]
          15 +    act=a+b if RV=='rover1' else b+a
          16 +    obs,*_=env.step(np.array(act,dtype=np.float32))
          17 +    return obs
          18 +def goto(wps):
          19 +    for wp in wps:
          20 +        for _ in range(60):
          21 +            d=np.clip(np.array(wp[:2])-pos()[:2],-0.2,0.2)
          22 +            if np.abs(d).max()<1e-7: break
          23 +            step(d[0],d[1])
          24 +    return pos()
          25 +def turn(th):
          26 +    for _ in range(40):
          27 +        e=(th-pos()[2]+np.pi)%(2*np.pi)-np.pi
          28 +        if abs(e)<1e-7: break
          29 +        step(0,0,float(np.clip(e,-0.4,0.4)))
          30 +    return pos()
          31 +def cal():
          32 +    step(op=-0.5); return obs.get(r1,'calibrated')
          33 +def objpos(name):
          34 +    o=obs.get_object_from_name(name); return np.array([obs.get(o,'x'),obs.get(o,'y'),obs.get(o,'z')])
          35 +def imaged():
          36 +    return [o.name for o in obs.get_objects(T['objective']) if obs.get(o,'have_image_'+RV)>0.5]
          37 +def scan(seed,name,ang,r0,r1_,dr,th=0.0,via=None,mode='cal',pre=None):
          38 +    """walk along ray at angle ang from objective, radius r0 -> r1_. mode 'cal': first calibrate success.
          39 +    mode 'img': at each point cal+img, stop when `name` imaged. pre: point to go first and image there."""
          40 +    reset(seed); c=objpos(name)[:2]; u=np.array([np.cos(ang),np.sin(ang)])
          41 +    start=c+r0*u
          42 +    if pre is not None:
          43 +        goto(pre); cal(); step(op=-1/6)
          44 +    p=goto((via or [])+[tuple(start)])
          45 +    if np.linalg.norm(p[:2]-start)>1e-4: return ('unreach',p.round(3))
          46 +    turn(th)
          47 +    r=r0; n=int(round(abs(r0-r1_)/dr))+1
          48 +    for i in range(n):
          49 +        r=r0+(r1_-r0)*i/max(n-1,1)
          50 +        q=goto([tuple(c+r*u)])
          51 +        if np.linalg.norm(q[:2]-(c+r*u))>1e-4: return ('blocked',r,q.round(3))
          52 +        ok=cal()>0.5
          53 +        if mode=='cal' and ok:
          54 +            step(op=-1/6); return (round(r,4), imaged(), pos().round(4))
          55 +        if mode=='img':
          56 +            step(op=-1/6)
          57 +            if name in imaged(): return (round(r,4), pos().round(4))
          58 +    return None
          59 +def bis(seed,name,ang,th,lo=1.5,hi=2.3,via=None,mode='cal',pre=None):
          60 +    a=scan(seed,name,ang,hi,lo,0.01,th=th,via=via,mode=mode,pre=pre)
          61 +    if not a or isinstance(a[0],str): return a
          62 +    b=scan(seed,name,ang,a[0]+0.01,a[0]-0.001,0.0005,th=th,via=via,mode=mode,pre=pre)
          63 +    return b
          64 +def model(base,th,obj,ox=-0.087,oy=-0.0125):
          65 +    cam=np.array([base[0]+ox*np.cos(th)-oy*np.sin(th), base[1]+ox*np.sin(th)+oy*np.cos(th)])
          66 +    return np.linalg.norm(np.array(obj[:2])-cam)
```

</details>

<a id="C005"></a>
### C005 · Return to home heading (at_home needs theta), send cone fallback

Commit `f480a81455d49199342c0f6a136d5cc611ab8985`; parents: 4351d31ae2a09db536407d6f1ffb5525ffc7b5ab. Recorded author date: 2026-10-01T11:07:35+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0827](01_timeline.md#E0827): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_f480a81_approach.py) · [Exact all-file diff](evidence/diffs/C005_f480a81.diff)

[Previous saved controller snapshot](evidence/versions/C004_4351d31_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5526419..21944a2 100644
--- a/approach.py
+++ b/approach.py
@@ -217,6 +217,7 @@ class GeneratedApproach:
  217    217          sc = self.sc
  218    218          g = state.get
  219    219          self.homes = [np.array([g(r, "x"), g(r, "y")]) for r in sc.rovers]
         220 +        self.home_th = [g(r, "theta") for r in sc.rovers]
  220    221          self.planners = [RoverPlanner(sc, i, self.homes[i]) for i in range(2)]
  221    222          nobj = len(sc.objectives)
  222    223          tasks = [("obj", k) for k in range(nobj)] + [("stone", 0), ("soil", 0)]
@@ -382,8 +383,18 @@ class GeneratedApproach:
  382    383              if t[0] == "obj" and not self._task_done(state, t):
  383    384                  v = p - sc.opos[t[1]]
  384    385                  return np.arctan2(v[1], v[0])
  385        -        v = p - sc.lpos
  386        -        return np.arctan2(v[1], v[0])
         386 +        # images done: head back to home heading unless stuck at home without having sent
         387 +        g = state.get
         388 +        me = "rover%d" % i
         389 +        holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
         390 +            any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
         391 +        if holding and k >= len(plan["path"]) - 1:
         392 +            v = p - sc.lpos
         393 +            away = np.arctan2(v[1], v[0])
         394 +            # heading within the send cone (+-60 deg of away) closest to home heading
         395 +            dlt = float(np.clip(_wrap(self.home_th[i] - away), -np.radians(60), np.radians(60)))
         396 +            return away + dlt
         397 +        return self.home_th[i]
  387    398  
  388    399      def _rover_action(self, state, i):
  389    400          sc = self.sc
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..98f9cc5
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,22 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed = int(sys.argv[1]); N = int(sys.argv[2])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed)
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +ap.reset(obs, info)
          10 +print("mytasks", ap.my_tasks)
          11 +for i in range(2): print(i, "visits", ap.plans[i]['visits'], "len", len(ap.plans[i]['path']))
          12 +names = {v:k for k,v in {"sample": -5/6, "calibrate": -0.5, "image": -1/6, "noop": 1/6, "send": 0.5, "drop": 5/6}.items()}
          13 +for step in range(N):
          14 +    a = ap.get_action(obs)
          15 +    obs, r, term, trunc, info = env.step(a)
          16 +    g = obs.get
          17 +    rs = [(round(g(rv,'x'),2), round(g(rv,'y'),2), round(g(rv,'theta'),2), int(g(rv,'at_home')), int(g(rv,'store_full')), int(g(rv,'calibrated'))) for rv in ap.sc.rovers]
          18 +    ops = [min(names, key=lambda b: abs(b-a[3])), min(names, key=lambda b: abs(b-a[7]))]
          19 +    objs = ''.join('%d%d%d ' % (g(o,'have_image_rover0'), g(o,'have_image_rover1'), g(o,'received_image')) for o in ap.sc.objectives)
          20 +    sm = ''.join('%d%d%d ' % (g(s,'analyzed_rover0'), g(s,'analyzed_rover1'), g(s,'received_analysis')) for s in ap.sc.samples)
          21 +    print(step, [names[o] for o in ops], rs, objs, '|', sm, term)
          22 +    if term: break
diff --git a/probe_home.py b/probe_home.py
new file mode 100644
index 0000000..df858d8
--- /dev/null
+++ b/probe_home.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +r1 = obs.get_object_from_name('rover1')
           6 +for k in range(12):
           7 +    obs,*_ = env.step(np.array([0,0,0,1/6, 0,0,0.1,1/6],dtype=np.float32))
           8 +    print(round(obs.get(r1,'theta'),2), obs.get(r1,'at_home'), end='; ')
           9 +print()
          10 +obs, info = env.reset(seed=0)
          11 +for k in range(12):
          12 +    obs,*_ = env.step(np.array([0,0,0,1/6, 0,0,-0.1,1/6],dtype=np.float32))
          13 +    print(round(obs.get(r1,'theta'),2), obs.get(r1,'at_home'), end='; ')
```

</details>

<a id="C006"></a>
### C006 · Send-cone heading chosen to minimise total rotation

Commit `63b13d162448a8061f4438aa35dc0f37bdc35b81`; parents: f480a81455d49199342c0f6a136d5cc611ab8985. Recorded author date: 2026-10-01T11:08:49+02:00.

File roles (automatic): policy.

- [E0839](01_timeline.md#E0839): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_63b13d1_approach.py) · [Exact all-file diff](evidence/diffs/C006_63b13d1.diff)

[Previous saved controller snapshot](evidence/versions/C005_f480a81_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 21944a2..ac1cb1b 100644
--- a/approach.py
+++ b/approach.py
@@ -388,12 +388,18 @@ class GeneratedApproach:
  388    388          me = "rover%d" % i
  389    389          holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
  390    390              any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
  391        -        if holding and k >= len(plan["path"]) - 1:
         391 +        if holding:
  392    392              v = p - sc.lpos
  393    393              away = np.arctan2(v[1], v[0])
  394        -            # heading within the send cone (+-60 deg of away) closest to home heading
  395        -            dlt = float(np.clip(_wrap(self.home_th[i] - away), -np.radians(60), np.radians(60)))
  396        -            return away + dlt
         394 +            th = g(sc.rovers[i], "theta")
         395 +            hth = self.home_th[i]
         396 +            best, bc = None, None
         397 +            for c in np.linspace(-np.radians(60), np.radians(60), 25):
         398 +                h = away + c
         399 +                cost = abs(_wrap(h - th)) + abs(_wrap(hth - h)) + 0.01 * abs(_wrap(h - th))
         400 +                if best is None or cost < best:
         401 +                    best, bc = cost, h
         402 +            return bc
  397    403          return self.home_th[i]
  398    404  
  399    405      def _rover_action(self, state, i):
```

</details>

<a id="C007"></a>
### C007 · Send whenever possible; keep home heading if future LOS send is predicted

Commit `6945310af04ec102ffc25767a20a168086a7c004`; parents: 63b13d162448a8061f4438aa35dc0f37bdc35b81. Recorded author date: 2026-10-01T11:10:36+02:00.

File roles (automatic): policy.

- [E0850](01_timeline.md#E0850): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_6945310_approach.py) · [Exact all-file diff](evidence/diffs/C007_6945310.diff)

[Previous saved controller snapshot](evidence/versions/C006_63b13d1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ac1cb1b..f4ca772 100644
--- a/approach.py
+++ b/approach.py
@@ -362,10 +362,38 @@ class GeneratedApproach:
  362    362          for s in sc.samples:
  363    363              if g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5:
  364    364                  holding = True
  365        -        if holding and all_done and self._can_send(state, i, p, th):
         365 +        if holding and self._can_send(state, i, p, th):
  366    366              return "send"
  367    367          return "noop"
  368    368  
         369 +    def _los_clear(self, p, q):
         370 +        sc = self.sc
         371 +        if np.linalg.norm(sc.lpos - p) > SEND_R:
         372 +            return False
         373 +        if self._seg_dist(q, p, sc.lpos) < 0.29:
         374 +            return False
         375 +        for pc in self._pillars():
         376 +            if self._seg_dist(np.array(pc), p, sc.lpos) < 0.14:
         377 +                return False
         378 +        return True
         379 +
         380 +    def _future_los(self, state, i, k):
         381 +        """Will a send facing any direction be possible later on my path (after my last task visit)?"""
         382 +        plan = self.plans[i]
         383 +        path = plan["path"]
         384 +        P = self.planners[i]
         385 +        last = max([idx for idx, ts in plan["visits"].items()
         386 +                    if any(not self._task_done(state, t) for t in ts)] + [k])
         387 +        op = self.plans[1 - i]
         388 +        opath = op["path"]
         389 +        ok0 = op["k"]
         390 +        Po = self.planners[1 - i]
         391 +        for idx in range(last, len(path)):
         392 +            q = Po.pos(opath[min(len(opath) - 1, ok0 + (idx - k))])
         393 +            if self._los_clear(P.pos(path[idx]), q):
         394 +                return True
         395 +        return False
         396 +
  369    397      def _desired_heading(self, state, i, p, k):
  370    398          """Face away from the next objective still to image on my path; else away from lander."""
  371    399          sc = self.sc
@@ -388,7 +416,7 @@ class GeneratedApproach:
  388    416          me = "rover%d" % i
  389    417          holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
  390    418              any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
  391        -        if holding:
         419 +        if holding and not self._future_los(state, i, k):
  392    420              v = p - sc.lpos
  393    421              away = np.arctan2(v[1], v[0])
  394    422              th = g(sc.rovers[i], "theta")
```

</details>

<a id="C008"></a>
### C008 · approach2: time-expanded BFS planner (wip)

Commit `340d14811a3f9f90c5f06ff9c8c1876a43250d83`; parents: 6945310af04ec102ffc25767a20a168086a7c004. Recorded author date: 2026-10-01T11:14:14+02:00.

File roles (automatic): support code (role needs review).

- [E0865](01_timeline.md#E0865): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C008_340d148.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach2.py b/approach2.py
new file mode 100644
index 0000000..3748e9e
--- /dev/null
+++ b/approach2.py
@@ -0,0 +1,515 @@
           1 +"""Rovers: per-rover time-expanded BFS over (cell, done-set, calibrated, store, sent)."""
           2 +import numpy as np
           3 +
           4 +H = 0.1            # lattice spacing; a step moves up to 2 cells per axis (0.2m)
           5 +IMG_R = 2.0        # imaging range from base when facing away (true ~2.08)
           6 +SAMP_R = 0.235     # sampling range (true 0.25)
           7 +SEND_R = 3.85      # send range (true ~4.0)
           8 +TMAX = 120
           9 +BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
          10 +        "send": 0.5, "drop": 5 / 6}
          11 +NOOP, CAL, IMG, SAMP, DROP, SEND = "noop", "calibrate", "image", "sample", "drop", "send"
          12 +
          13 +
          14 +def _wrap(a):
          15 +    return (a + np.pi) % (2 * np.pi) - np.pi
          16 +
          17 +
          18 +def _type(space, name):
          19 +    for t in space.types:
          20 +        if t.name == name:
          21 +            return t
          22 +    return None
          23 +
          24 +
          25 +def _seg_dist(p, a, b):
          26 +    ab = b - a
          27 +    t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-12), 0.0, 1.0)
          28 +    return float(np.linalg.norm(a + t * ab - p))
          29 +
          30 +
          31 +class Scene:
          32 +    def __init__(self, state, space):
          33 +        self.T = {n: _type(space, n) for n in ["rover", "lander", "objective", "sample", "obstacle"]}
          34 +        g = state.get
          35 +        self.rovers = sorted(state.get_objects(self.T["rover"]), key=lambda o: o.name)
          36 +        self.lander = state.get_objects(self.T["lander"])[0]
          37 +        self.objectives = sorted(state.get_objects(self.T["objective"]), key=lambda o: o.name)
          38 +        self.samples = sorted(state.get_objects(self.T["sample"]), key=lambda o: o.name)
          39 +        self.obstacles = state.get_objects(self.T["obstacle"])
          40 +        self.lpos = np.array([g(self.lander, "x"), g(self.lander, "y")])
          41 +        self.obs_boxes = [(g(o, "x"), g(o, "y"), g(o, "half_x"), g(o, "half_y"), g(o, "half_z"))
          42 +                          for o in self.obstacles]
          43 +        self.pillars = [np.array([b[0], b[1]]) for b in self.obs_boxes if max(b[2], b[3]) < 0.15]
          44 +        self.opos = [np.array([g(o, "x"), g(o, "y")]) for o in self.objectives]
          45 +        self.spos = [np.array([g(o, "x"), g(o, "y")]) for o in self.samples]
          46 +        self.ssoil = [g(o, "is_soil") > 0.5 for o in self.samples]
          47 +
          48 +
          49 +def _shift_or(A, a, b):
          50 +    """OR of A shifted so that out[i,j] |= A[i-a, j-b]."""
          51 +    out = np.zeros_like(A)
          52 +    W, Hh = A.shape
          53 +    xs0, xs1 = max(0, a), min(W, W + a)
          54 +    ys0, ys1 = max(0, b), min(Hh, Hh + b)
          55 +    out[xs0:xs1, ys0:ys1] = A[xs0 - a:xs1 - a, ys0 - b:ys1 - b]
          56 +    return out
          57 +
          58 +
          59 +class RoverBFS:
          60 +    def __init__(self, scene, idx, home, img_r=IMG_R):
          61 +        self.sc = scene
          62 +        self.idx = idx
          63 +        self.home = np.array(home, dtype=float)
          64 +        side = 1.0 if home[0] > 0 else -1.0
          65 +        x0 = self.home[0] - H * np.floor((self.home[0] + 2.27) / H)
          66 +        y0 = self.home[1] - H * np.floor((self.home[1] + 2.27) / H)
          67 +        self.xs = np.arange(x0, 2.2701, H)
          68 +        self.ys = np.arange(y0, 2.2701, H)
          69 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
          70 +        self.X, self.Y = X, Y
          71 +        free = (np.abs(X) <= 2.265) & (np.abs(Y) <= 2.265) & (X * side >= 0.235)
          72 +        for (ox, oy, hx, hy, hz) in scene.obs_boxes:
          73 +            margin = 0.21 if max(hx, hy) >= 0.15 else 0.25
          74 +            dx = np.maximum(np.abs(X - ox) - hx, 0.0)
          75 +            dy = np.maximum(np.abs(Y - oy) - hy, 0.0)
          76 +            free &= (dx * dx + dy * dy) >= margin * margin
          77 +        lx, ly = scene.lpos
          78 +        free &= ~((X < lx + 0.71) & (Y < ly + 0.54))
          79 +        self.hc = (int(np.argmin(np.abs(self.xs - self.home[0]))), int(np.argmin(np.abs(self.ys - self.home[1]))))
          80 +        free[self.hc] = True
          81 +        self.free = free
          82 +        self.shape = free.shape
          83 +        self.nobj = len(scene.opos)
          84 +        self.n = self.nobj + 2
          85 +        self.STONE = 1 << self.nobj
          86 +        self.SOIL = 1 << (self.nobj + 1)
          87 +        self.CALB = 1 << self.n
          88 +        self.STOREB = 1 << (self.n + 1)
          89 +        self.SENTB = 1 << (self.n + 2)
          90 +        self.img_r = img_r
          91 +        self._prep()
          92 +
          93 +    def _prep(self):
          94 +        X, Y = self.X, self.Y
          95 +        sc = self.sc
          96 +        self.odist = [np.sqrt((X - o[0]) ** 2 + (Y - o[1]) ** 2) for o in sc.opos]
          97 +        vis_any = np.zeros(self.shape, bool)
          98 +        for d in self.odist:
          99 +            vis_any |= d <= self.img_r
         100 +        self.vis_any = vis_any & self.free
         101 +        stone = np.zeros(self.shape, bool)
         102 +        soil = np.zeros(self.shape, bool)
         103 +        for s, so in zip(sc.spos, sc.ssoil):
         104 +            m = (X - s[0]) ** 2 + (Y - s[1]) ** 2 <= SAMP_R ** 2
         105 +            if so:
         106 +                soil |= m
         107 +            else:
         108 +                stone |= m
         109 +        both = stone & soil
         110 +        self.stone_m = stone & ~both & self.free
         111 +        self.soil_m = soil & ~both & self.free
         112 +        self.send_m = ((X - sc.lpos[0]) ** 2 + (Y - sc.lpos[1]) ** 2 <= SEND_R ** 2) & self.free
         113 +        self._img_cache = {}
         114 +
         115 +    def pos(self, c):
         116 +        return np.array([self.xs[c[0]], self.ys[c[1]]])
         117 +
         118 +    def cell(self, p):
         119 +        return (int(np.argmin(np.abs(self.xs - p[0]))), int(np.argmin(np.abs(self.ys - p[1]))))
         120 +
         121 +    def img_masks(self, S):
         122 +        """For image op with done-set S: list of (r, mask) where r is nearest visible not-yet-imaged."""
         123 +        key = S & ((1 << self.nobj) - 1)
         124 +        if key in self._img_cache:
         125 +            return self._img_cache[key]
         126 +        best = np.full(self.shape, np.inf)
         127 +        arg = np.full(self.shape, -1)
         128 +        for r in range(self.nobj):
         129 +            if key & (1 << r):
         130 +                continue
         131 +            d = np.where(self.odist[r] <= self.img_r, self.odist[r], np.inf)
         132 +            better = d < best
         133 +            best = np.where(better, d, best)
         134 +            arg = np.where(better, r, arg)
         135 +        res = []
         136 +        for r in range(self.nobj):
         137 +            m = (arg == r) & self.free
         138 +            if m.any():
         139 +                res.append((r, m))
         140 +        self._img_cache[key] = res
         141 +        return res
         142 +
         143 +    def transitions(self, L):
         144 +        out = []
         145 +        S = L & ((1 << self.n) - 1)
         146 +        cal = L & self.CALB
         147 +        store = L & self.STOREB
         148 +        sent = L & self.SENTB
         149 +        if not sent:
         150 +            if not cal:
         151 +                out.append((CAL, L | self.CALB, self.vis_any))
         152 +            else:
         153 +                for r, m in self.img_masks(S):
         154 +                    out.append((IMG, (L | (1 << r)) & ~self.CALB, m))
         155 +            if not store:
         156 +                if not (S & self.STONE):
         157 +                    out.append((SAMP, L | self.STONE | self.STOREB, self.stone_m))
         158 +                if not (S & self.SOIL):
         159 +                    out.append((SAMP, L | self.SOIL | self.STOREB, self.soil_m))
         160 +            if S:
         161 +                out.append((SEND, L | self.SENTB, self.send_m))
         162 +        if store:
         163 +            out.append((DROP, L & ~self.STOREB, None))
         164 +        return out
         165 +
         166 +    def dilate(self, R):
         167 +        A = R | _shift_or(R, 1, 0) | _shift_or(R, -1, 0)
         168 +        A = A | _shift_or(R, 2, 0) | _shift_or(R, -2, 0)
         169 +        B = A | _shift_or(A, 0, 1) | _shift_or(A, 0, -1)
         170 +        B = B | _shift_or(A, 0, 2) | _shift_or(A, 0, -2)
         171 +        return B & self.free
         172 +
         173 +    def run(self, start_cell, L0, wanted=None, tmax=TMAX, time_budget=None):
         174 +        """Forward BFS. Returns dict S->earliest finish time (home, store empty, sent)."""
         175 +        import time as _t
         176 +        t_start = _t.time()
         177 +        R0 = np.zeros(self.shape, bool)
         178 +        R0[start_cell] = True
         179 +        self.layers = [{L0: R0}]
         180 +        self.rev = {}
         181 +        self.trans_cache = {}
         182 +        finish = {}
         183 +        hc = self.hc
         184 +        for t in range(1, tmax + 1):
         185 +            prev = self.layers[-1]
         186 +            new = {}
         187 +            for L, R in prev.items():
         188 +                D = self.dilate(R)
         189 +                if L in new:
         190 +                    new[L] |= D
         191 +                else:
         192 +                    new[L] = D.copy()
         193 +                tr = self.trans_cache.get(L)
         194 +                if tr is None:
         195 +                    tr = self.transitions(L)
         196 +                    self.trans_cache[L] = tr
         197 +                for op, L2, m in tr:
         198 +                    M = D if m is None else (D & m)
         199 +                    if not M.any():
         200 +                        continue
         201 +                    if L2 in new:
         202 +                        new[L2] |= M
         203 +                    else:
         204 +                        new[L2] = M.copy()
         205 +            self.layers.append(new)
         206 +            for L, R in new.items():
         207 +                if (L & self.SENTB) and not (L & self.STOREB) and R[hc]:
         208 +                    S = L & ((1 << self.n) - 1)
         209 +                    if S not in finish:
         210 +                        finish[S] = (t, L)
         211 +            if wanted is not None and all(any((S & w) == w for S in finish) for w in wanted):
         212 +                break
         213 +            if time_budget is not None and _t.time() - t_start > time_budget:
         214 +                break
         215 +        return finish
         216 +
         217 +    def extract(self, T, Lgoal):
         218 +        """Backtrack from (T, Lgoal, home). Returns list of (cell, op) for steps 1..T."""
         219 +        c = self.hc
         220 +        L = Lgoal
         221 +        steps = []
         222 +        W, Hh = self.shape
         223 +        for t in range(T, 0, -1):
         224 +            prev = self.layers[t - 1]
         225 +            # candidate predecessors: (Lp, op) such that transition Lp --op--> L valid at c
         226 +            cands = []
         227 +            if L in prev:
         228 +                cands.append((L, NOOP))
         229 +            for Lp in prev:
         230 +                tr = self.trans_cache.get(Lp)
         231 +                if tr is None:
         232 +                    tr = self.transitions(Lp)
         233 +                    self.trans_cache[Lp] = tr
         234 +                for op, L2, m in tr:
         235 +                    if L2 == L and (m is None or m[c]):
         236 +                        cands.append((Lp, op))
         237 +            found = None
         238 +            # prefer real ops over noop when tie (keeps ops early); prefer staying still
         239 +            for Lp, op in cands:
         240 +                R = prev[Lp]
         241 +                i0, j0 = c
         242 +                best = None
         243 +                for a in range(-2, 3):
         244 +                    for b in range(-2, 3):
         245 +                        ii, jj = i0 + a, j0 + b
         246 +                        if 0 <= ii < W and 0 <= jj < Hh and R[ii, jj]:
         247 +                            score = max(abs(a), abs(b)) * 0.01 + (abs(a) + abs(b)) * 0.001
         248 +                            if best is None or score < best[0]:
         249 +                                best = (score, (ii, jj))
         250 +                if best is not None:
         251 +                    found = (Lp, op, best[1])
         252 +                    break
         253 +            if found is None:
         254 +                return None
         255 +            Lp, op, cp = found
         256 +            steps.append((c, op, L))
         257 +            c = cp
         258 +            L = Lp
         259 +        steps.reverse()
         260 +        return steps
         261 +
         262 +
         263 +class GeneratedApproach:
         264 +    def __init__(self, action_space, observation_space, primitives):
         265 +        self.action_space = action_space
         266 +        self.space = observation_space
         267 +
         268 +    # ------------------------------------------------------------------
         269 +    def reset(self, state, info):
         270 +        self.sc = Scene(state, self.space)
         271 +        sc = self.sc
         272 +        g = state.get
         273 +        self.homes = [np.array([g(r, "x"), g(r, "y")]) for r in sc.rovers]
         274 +        self.home_th = [g(r, "theta") for r in sc.rovers]
         275 +        self.bfs = [RoverBFS(sc, i, self.homes[i]) for i in range(2)]
         276 +        nobj = len(sc.objectives)
         277 +        n = nobj + 2
         278 +        full = (1 << n) - 1
         279 +        fins = []
         280 +        for i in range(2):
         281 +            B = self.bfs[i]
         282 +            fins.append(B.run(B.hc, 0, wanted=[full], tmax=TMAX, time_budget=12.0))
         283 +        # best finish time for a superset-closed requirement: T_i(req) = min over S ⊇ req
         284 +        def best_for(fin, req):
         285 +            bt = None
         286 +            for S, (t, L) in fin.items():
         287 +                if (S & req) == req and (bt is None or t < bt[0]):
         288 +                    bt = (t, L, S)
         289 +            return bt
         290 +        best = None
         291 +        for s0 in range(1 << n):
         292 +            s1 = full & ~s0
         293 +            b0 = best_for(fins[0], s0) if s0 else (0, None, 0)
         294 +            b1 = best_for(fins[1], s1) if s1 else (0, None, 0)
         295 +            if b0 is None or b1 is None:
         296 +                continue
         297 +            key = (max(b0[0], b1[0]), b0[0] + b1[0])
         298 +            if best is None or key < best[0]:
         299 +                best = (key, b0, b1)
         300 +        self.plans = []
         301 +        self.my_req = [0, 0]
         302 +        for i in range(2):
         303 +            b = best[1 + i] if best else None
         304 +            steps = []
         305 +            if b is not None and b[1] is not None:
         306 +                # need layers from the run for rover i: rerun to be safe (layers overwritten? no: per-rover object)
         307 +                steps = self.bfs[i].extract(b[0], b[1]) or []
         308 +                self.my_req[i] = b[2]
         309 +            self.plans.append({"steps": steps, "k": 0, "fail": 0})
         310 +        self.done_flag = False
         311 +
         312 +    # ------------------------------------------------------------------
         313 +    def _flags(self, state, i):
         314 +        sc = self.sc
         315 +        g = state.get
         316 +        me = "rover%d" % i
         317 +        S = 0
         318 +        for r, o in enumerate(sc.objectives):
         319 +            if g(o, "have_image_" + me) > 0.5:
         320 +                S |= 1 << r
         321 +        nobj = len(sc.objectives)
         322 +        for s, soil in zip(sc.samples, sc.ssoil):
         323 +            if g(s, "analyzed_" + me) > 0.5:
         324 +                S |= 1 << (nobj + (1 if soil else 0))
         325 +        cal = g(sc.rovers[i], "calibrated") > 0.5
         326 +        store = g(sc.rovers[i], "store_full") > 0.5
         327 +        holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
         328 +            any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
         329 +        return S, cal, store, holding
         330 +
         331 +    def _visible(self, p, th, k, margin=0.03):
         332 +        c = p + np.array([-0.087 * np.cos(th) + 0.0125 * np.sin(th), -0.087 * np.sin(th) - 0.0125 * np.cos(th)])
         333 +        o = self.sc.opos[k]
         334 +        v = o - c
         335 +        if np.linalg.norm(v) > 1.9972 - margin:
         336 +            return False
         337 +        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
         338 +        if ang < np.radians(108):
         339 +            for pc in self.sc.pillars:
         340 +                if _seg_dist(pc, c, o) < 0.11:
         341 +                    return False
         342 +        return True
         343 +
         344 +    def _can_send(self, state, i, p, th):
         345 +        sc = self.sc
         346 +        v = sc.lpos - p
         347 +        if np.linalg.norm(v) > SEND_R:
         348 +            return False
         349 +        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
         350 +        if ang >= np.radians(115):
         351 +            return True
         352 +        g = state.get
         353 +        orv = sc.rovers[1 - i]
         354 +        op = np.array([g(orv, "x"), g(orv, "y")])
         355 +        if _seg_dist(op, p, sc.lpos) < 0.27:
         356 +            return False
         357 +        for pc in sc.pillars:
         358 +            if _seg_dist(pc, p, sc.lpos) < 0.13:
         359 +                return False
         360 +        return True
         361 +
         362 +    def _los_clear(self, p, q):
         363 +        sc = self.sc
         364 +        if np.linalg.norm(sc.lpos - p) > SEND_R:
         365 +            return False
         366 +        if _seg_dist(q, p, sc.lpos) < 0.29:
         367 +            return False
         368 +        for pc in sc.pillars:
         369 +            if _seg_dist(pc, p, sc.lpos) < 0.14:
         370 +                return False
         371 +        return True
         372 +
         373 +    def _other_pos_at(self, i, dt, state):
         374 +        """Predicted position of rover (1-i) dt steps from now."""
         375 +        j = 1 - i
         376 +        plan = self.plans[j]
         377 +        steps = plan["steps"]
         378 +        B = self.bfs[j]
         379 +        if not steps:
         380 +            g = state.get
         381 +            return np.array([g(self.sc.rovers[j], "x"), g(self.sc.rovers[j], "y")])
         382 +        idx = min(len(steps) - 1, plan["k"] + dt - 1)
         383 +        if idx < 0:
         384 +            g = state.get
         385 +            return np.array([g(self.sc.rovers[j], "x"), g(self.sc.rovers[j], "y")])
         386 +        return B.pos(steps[idx][0])
         387 +
         388 +    def _desired_heading(self, state, i, p, th, k, holding):
         389 +        sc = self.sc
         390 +        plan = self.plans[i]
         391 +        steps = plan["steps"]
         392 +        B = self.bfs[i]
         393 +        nobj = len(sc.objectives)
         394 +        # next image op in plan: face away from the objective it targets
         395 +        for idx in range(k, len(steps)):
         396 +            c, op, L = steps[idx]
         397 +            if op == IMG:
         398 +                # which objective: bit newly set in L vs previous
         399 +                Lp = steps[idx - 1][2] if idx > 0 else plan.get("L0", 0)
         400 +                newbits = (L & ~Lp) & ((1 << nobj) - 1)
         401 +                if newbits:
         402 +                    r = int(np.log2(newbits & -newbits))
         403 +                    v = B.pos(c) - sc.opos[r]
         404 +                    return np.arctan2(v[1], v[0])
         405 +        hth = self.home_th[i]
         406 +        if holding:
         407 +            # will a send be possible facing home-ish heading later?
         408 +            last = len(steps)
         409 +            ok = False
         410 +            for idx in range(k, last):
         411 +                q = self._other_pos_at(i, idx - k + 1, state)
         412 +                if self._los_clear(B.pos(steps[idx][0]), q):
         413 +                    ok = True
         414 +                    break
         415 +            if not ok and self._los_clear(p, self._other_pos_at(i, 0, state)):
         416 +                ok = True
         417 +            if not ok:
         418 +                v = p - sc.lpos
         419 +                away = np.arctan2(v[1], v[0])
         420 +                best, bc = None, None
         421 +                for c in np.linspace(-np.radians(60), np.radians(60), 25):
         422 +                    h = away + c
         423 +                    cost = abs(_wrap(h - th)) + abs(_wrap(hth - h)) + 0.01 * abs(_wrap(h - th))
         424 +                    if best is None or cost < best:
         425 +                        best, bc = cost, h
         426 +                return bc
         427 +        return hth
         428 +
         429 +    def _replan(self, state, i, cur):
         430 +        B = self.bfs[i]
         431 +        S, cal, store, holding = self._flags(state, i)
         432 +        L0 = S | (B.CALB if cal else 0) | (B.STOREB if store else 0)
         433 +        if not holding and S:
         434 +            L0 |= B.SENTB
         435 +        c = B.cell(cur)
         436 +        B.free[c] = True
         437 +        req = self.my_req[i] | S
         438 +        fin = B.run(c, L0, wanted=[req], tmax=TMAX, time_budget=5.0)
         439 +        bt = None
         440 +        for S2, (t, L) in fin.items():
         441 +            if (S2 & req) == req and (bt is None or t < bt[0]):
         442 +                bt = (t, L)
         443 +        steps = B.extract(bt[0], bt[1]) if bt else []
         444 +        self.plans[i] = {"steps": steps or [], "k": 0, "fail": 0, "L0": L0}
         445 +
         446 +    def _rover_action(self, state, i):
         447 +        sc = self.sc
         448 +        g = state.get
         449 +        rv = sc.rovers[i]
         450 +        cur = np.array([g(rv, "x"), g(rv, "y")])
         451 +        th = g(rv, "theta")
         452 +        B = self.bfs[i]
         453 +        plan = self.plans[i]
         454 +        S, cal, store, holding = self._flags(state, i)
         455 +        steps = plan["steps"]
         456 +        k = plan["k"]
         457 +        # verify previous step outcome
         458 +        if k > 0 and k <= len(steps):
         459 +            c, op, L = steps[k - 1]
         460 +            pos_ok = np.linalg.norm(B.pos(c) - cur) < 0.02
         461 +            Sp = L & ((1 << B.n) - 1)
         462 +            op_ok = True
         463 +            if op in (IMG, SAMP):
         464 +                op_ok = (S & Sp) == Sp
         465 +            elif op == CAL:
         466 +                op_ok = cal
         467 +            elif op == DROP:
         468 +                op_ok = not store
         469 +            if not (pos_ok and op_ok):
         470 +                plan["fail"] += 1
         471 +                if plan["fail"] > 4 or (not pos_ok and plan["fail"] > 2):
         472 +                    self._replan(state, i, cur)
         473 +                    plan = self.plans[i]
         474 +                    steps = plan["steps"]
         475 +                    k = 0
         476 +                else:
         477 +                    k = k - 1  # retry the step
         478 +            else:
         479 +                plan["fail"] = 0
         480 +        if k < len(steps):
         481 +            c, op, L = steps[k]
         482 +            target = B.pos(c)
         483 +            plan["k"] = k + 1
         484 +        else:
         485 +            target = cur if np.linalg.norm(cur - self.homes[i]) < 0.02 else self.homes[i]
         486 +            op = NOOP
         487 +            plan["k"] = len(steps) + 1 if steps else 1
         488 +            # finished plan: if tasks remain undone, replan
         489 +            if (S & self.my_req[i]) != self.my_req[i] or store:
         490 +                self._replan(state, i, cur)
         491 +                return self._rover_action_fresh(state, i)
         492 +        d = np.clip(target - cur, -0.2, 0.2)
         493 +        newp = cur + d
         494 +        dth = float(np.clip(_wrap(self._desired_heading(state, i, newp, th, k + 1, holding) - th), -0.4, 0.4))
         495 +        newth = _wrap(th + dth)
         496 +        # op adjustments
         497 +        if op == SEND:
         498 +            op = NOOP
         499 +        if op in (NOOP,) and holding and self._can_send(state, i, newp, newth):
         500 +            op = SEND
         501 +        elif op == NOOP and store and not any(s[1] == SAMP for s in steps[k:]):
         502 +            op = NOOP
         503 +        return np.array([d[0], d[1], dth, BAND[op]], dtype=np.float32)
         504 +
         505 +    def _rover_action_fresh(self, state, i):
         506 +        plan = self.plans[i]
         507 +        if not plan["steps"]:
         508 +            return np.array([0, 0, 0, BAND[NOOP]], dtype=np.float32)
         509 +        plan["k"] = 0
         510 +        return self._rover_action(state, i)
         511 +
         512 +    def get_action(self, state):
         513 +        a0 = self._rover_action(state, 0)
         514 +        a1 = self._rover_action(state, 1)
         515 +        return np.concatenate([a0, a1]).astype(np.float32)
diff --git a/eval_many.py b/eval_many.py
index 930adab..82f4b1b 100644
--- a/eval_many.py
+++ b/eval_many.py
@@ -3,12 +3,12 @@ import numpy as np
    3      3  from multiprocessing import Pool
    4      4  def run(seed):
    5      5      from env_client import make_env
    6        -    from approach import GeneratedApproach
           6 +    import os, importlib; GeneratedApproach = importlib.import_module(os.environ.get("APP", "approach")).GeneratedApproach
    7      7      env = make_env()
    8      8      obs, info = env.reset(seed=seed)
    9      9      ap = GeneratedApproach(env.action_space, env.observation_space, {})
   10     10      t0 = time.time(); ap.reset(obs, info); tp = time.time()-t0
   11        -    pl = [len(p['path'])-1 for p in ap.plans]
          11 +    pl = [len(p.get('path', p.get('steps', [])))-('path' in p) for p in ap.plans]
   12     12      steps=0; term=False
   13     13      while steps < 300:
   14     14          obs, r, term, trunc, info = env.step(ap.get_action(obs)); steps+=1
```

</details>

<a id="C009"></a>
### C009 · approach2: send mask respects LOS/heading

Commit `4524e2b774eed119ec14408dc98892844b7b30a0`; parents: 340d14811a3f9f90c5f06ff9c8c1876a43250d83. Recorded author date: 2026-10-01T11:15:42+02:00.

File roles (automatic): support code (role needs review).

- [E0884](01_timeline.md#E0884): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C009_4524e2b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach2.py b/approach2.py
index 3748e9e..b6e2421 100644
--- a/approach2.py
+++ b/approach2.py
@@ -57,8 +57,10 @@ def _shift_or(A, a, b):
   57     57  
   58     58  
   59     59  class RoverBFS:
   60        -    def __init__(self, scene, idx, home, img_r=IMG_R):
          60 +    def __init__(self, scene, idx, home, img_r=IMG_R, home_th=0.0, other_home=None):
   61     61          self.sc = scene
          62 +        self.home_th = home_th
          63 +        self.other_home = other_home
   62     64          self.idx = idx
   63     65          self.home = np.array(home, dtype=float)
   64     66          side = 1.0 if home[0] > 0 else -1.0
@@ -109,7 +111,21 @@ class RoverBFS:
  109    111          both = stone & soil
  110    112          self.stone_m = stone & ~both & self.free
  111    113          self.soil_m = soil & ~both & self.free
  112        -        self.send_m = ((X - sc.lpos[0]) ** 2 + (Y - sc.lpos[1]) ** 2 <= SEND_R ** 2) & self.free
         114 +        inr = ((X - sc.lpos[0]) ** 2 + (Y - sc.lpos[1]) ** 2 <= SEND_R ** 2) & self.free
         115 +        ok = np.zeros(self.shape, bool)
         116 +        if self.other_home is not None:
         117 +            away = np.arctan2(Y - sc.lpos[1], X - sc.lpos[0])
         118 +            ok |= np.abs(_wrap(self.home_th - away)) <= np.radians(60)
         119 +            for (i, j) in zip(*np.nonzero(inr & ~ok)):
         120 +                p = np.array([self.xs[i], self.ys[j]])
         121 +                if _seg_dist(self.other_home, p, sc.lpos) < 0.29:
         122 +                    continue
         123 +                if any(_seg_dist(pc, p, sc.lpos) < 0.14 for pc in sc.pillars):
         124 +                    continue
         125 +                ok[i, j] = True
         126 +        else:
         127 +            ok[:] = True
         128 +        self.send_m = inr & ok
  113    129          self._img_cache = {}
  114    130  
  115    131      def pos(self, c):
@@ -272,7 +288,8 @@ class GeneratedApproach:
  272    288          g = state.get
  273    289          self.homes = [np.array([g(r, "x"), g(r, "y")]) for r in sc.rovers]
  274    290          self.home_th = [g(r, "theta") for r in sc.rovers]
  275        -        self.bfs = [RoverBFS(sc, i, self.homes[i]) for i in range(2)]
         291 +        self.bfs = [RoverBFS(sc, i, self.homes[i], home_th=self.home_th[i], other_home=self.homes[1 - i])
         292 +                    for i in range(2)]
  276    293          nobj = len(sc.objectives)
  277    294          n = nobj + 2
  278    295          full = (1 << n) - 1
diff --git a/dbg2.py b/dbg2.py
index 98f9cc5..130309e 100644
--- a/dbg2.py
+++ b/dbg2.py
@@ -1,14 +1,14 @@
    1      1  import sys
    2      2  import numpy as np
    3      3  from env_client import make_env
    4        -from approach import GeneratedApproach
           4 +import os, importlib; GeneratedApproach = importlib.import_module(os.environ.get("APP", "approach")).GeneratedApproach
    5      5  seed = int(sys.argv[1]); N = int(sys.argv[2])
    6      6  env = make_env()
    7      7  obs, info = env.reset(seed=seed)
    8      8  ap = GeneratedApproach(env.action_space, env.observation_space, {})
    9      9  ap.reset(obs, info)
   10        -print("mytasks", ap.my_tasks)
   11        -for i in range(2): print(i, "visits", ap.plans[i]['visits'], "len", len(ap.plans[i]['path']))
          10 +print("req", getattr(ap, "my_req", None))
          11 +for i in range(2): print(i, [(tuple(np.round(ap.bfs[i].pos(c),2)), op) for c, op, L in ap.plans[i]["steps"]])
   12     12  names = {v:k for k,v in {"sample": -5/6, "calibrate": -0.5, "image": -1/6, "noop": 1/6, "send": 0.5, "drop": 5/6}.items()}
   13     13  for step in range(N):
   14     14      a = ap.get_action(obs)
```

</details>

<a id="C010"></a>
### C010 · approach2: time-dependent send mask using other rover trajectory

Commit `617ca9f129760e7fe93b3631ea1ea3e52b698fa7`; parents: 4524e2b774eed119ec14408dc98892844b7b30a0. Recorded author date: 2026-10-01T11:19:09+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E0907](01_timeline.md#E0907): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C010_617ca9f.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach2.py b/approach2.py
index b6e2421..adbedab 100644
--- a/approach2.py
+++ b/approach2.py
@@ -112,22 +112,37 @@ class RoverBFS:
  112    112          self.stone_m = stone & ~both & self.free
  113    113          self.soil_m = soil & ~both & self.free
  114    114          inr = ((X - sc.lpos[0]) ** 2 + (Y - sc.lpos[1]) ** 2 <= SEND_R ** 2) & self.free
  115        -        ok = np.zeros(self.shape, bool)
  116        -        if self.other_home is not None:
  117        -            away = np.arctan2(Y - sc.lpos[1], X - sc.lpos[0])
  118        -            ok |= np.abs(_wrap(self.home_th - away)) <= np.radians(60)
  119        -            for (i, j) in zip(*np.nonzero(inr & ~ok)):
  120        -                p = np.array([self.xs[i], self.ys[j]])
  121        -                if _seg_dist(self.other_home, p, sc.lpos) < 0.29:
  122        -                    continue
  123        -                if any(_seg_dist(pc, p, sc.lpos) < 0.14 for pc in sc.pillars):
  124        -                    continue
  125        -                ok[i, j] = True
  126        -        else:
  127        -            ok[:] = True
  128        -        self.send_m = inr & ok
         115 +        away = np.arctan2(Y - sc.lpos[1], X - sc.lpos[0])
         116 +        self.send_head_ok = inr & (np.abs(_wrap(self.home_th - away)) <= np.radians(60))
         117 +        pill = np.zeros(self.shape, bool)
         118 +        for pc in sc.pillars:
         119 +            pill |= self._segdist_grid(pc) < 0.14
         120 +        self.send_static = inr & ~pill
         121 +        self.send_m = inr
         122 +        self.other_traj = None
         123 +        self._send_t_cache = {}
  129    124          self._img_cache = {}
  130    125  
         126 +    def _segdist_grid(self, q):
         127 +        """Distance from point q to segment (cell -> lander) for every cell."""
         128 +        L = self.sc.lpos
         129 +        ax, ay = self.X, self.Y
         130 +        bx, by = L[0] - ax, L[1] - ay
         131 +        qx, qy = q[0] - ax, q[1] - ay
         132 +        t = np.clip((qx * bx + qy * by) / np.maximum(bx * bx + by * by, 1e-12), 0.0, 1.0)
         133 +        return np.sqrt((qx - t * bx) ** 2 + (qy - t * by) ** 2)
         134 +
         135 +    def send_mask_t(self, t):
         136 +        if self.other_traj is None:
         137 +            return self.send_m
         138 +        q = self.other_traj[min(t, len(self.other_traj) - 1)]
         139 +        key = (round(float(q[0]), 3), round(float(q[1]), 3))
         140 +        m = self._send_t_cache.get(key)
         141 +        if m is None:
         142 +            m = self.send_head_ok | (self.send_static & (self._segdist_grid(q) >= 0.29))
         143 +            self._send_t_cache[key] = m
         144 +        return m
         145 +
  131    146      def pos(self, c):
  132    147          return np.array([self.xs[c[0]], self.ys[c[1]]])
  133    148  
@@ -174,7 +189,7 @@ class RoverBFS:
  174    189                  if not (S & self.SOIL):
  175    190                      out.append((SAMP, L | self.SOIL | self.STOREB, self.soil_m))
  176    191              if S:
  177        -                out.append((SEND, L | self.SENTB, self.send_m))
         192 +                out.append((SEND, L | self.SENTB, "SEND"))
  178    193          if store:
  179    194              out.append((DROP, L & ~self.STOREB, None))
  180    195          return out
@@ -211,6 +226,8 @@ class RoverBFS:
  211    226                      tr = self.transitions(L)
  212    227                      self.trans_cache[L] = tr
  213    228                  for op, L2, m in tr:
         229 +                    if isinstance(m, str):
         230 +                        m = self.send_mask_t(t)
  214    231                      M = D if m is None else (D & m)
  215    232                      if not M.any():
  216    233                          continue
@@ -248,6 +265,8 @@ class RoverBFS:
  248    265                      tr = self.transitions(Lp)
  249    266                      self.trans_cache[Lp] = tr
  250    267                  for op, L2, m in tr:
         268 +                    if isinstance(m, str):
         269 +                        m = self.send_mask_t(t)
  251    270                      if L2 == L and (m is None or m[c]):
  252    271                          cands.append((Lp, op))
  253    272              found = None
@@ -324,8 +343,40 @@ class GeneratedApproach:
  324    343                  steps = self.bfs[i].extract(b[0], b[1]) or []
  325    344                  self.my_req[i] = b[2]
  326    345              self.plans.append({"steps": steps, "k": 0, "fail": 0})
         346 +        # refine each rover's plan given the other's trajectory (send line-of-sight)
         347 +        for i in range(2):
         348 +            if not self.plans[i]["steps"]:
         349 +                continue
         350 +            B = self.bfs[i]
         351 +            B.other_traj = self._traj(1 - i)
         352 +            B._send_t_cache = {}
         353 +            req = self.my_req[i]
         354 +            fin = B.run(B.hc, 0, wanted=[req], tmax=TMAX, time_budget=8.0)
         355 +            bt = None
         356 +            for S2, (t, L) in fin.items():
         357 +                if (S2 & req) == req and (bt is None or t < bt[0]):
         358 +                    bt = (t, L)
         359 +            if bt is not None:
         360 +                st = B.extract(bt[0], bt[1])
         361 +                if st:
         362 +                    self.plans[i] = {"steps": st, "k": 0, "fail": 0}
  327    363          self.done_flag = False
  328    364  
         365 +    def _traj(self, j):
         366 +        """Positions of rover j at times 0,1,2,... from its current plan pointer."""
         367 +        plan = self.plans[j]
         368 +        B = self.bfs[j]
         369 +        steps = plan["steps"]
         370 +        k = plan["k"]
         371 +        if k > 0 and k <= len(steps):
         372 +            cur = B.pos(steps[k - 1][0])
         373 +        else:
         374 +            cur = self.homes[j]
         375 +        out = [cur]
         376 +        for idx in range(k, len(steps)):
         377 +            out.append(B.pos(steps[idx][0]))
         378 +        return out
         379 +
  329    380      # ------------------------------------------------------------------
  330    381      def _flags(self, state, i):
  331    382          sc = self.sc
@@ -452,6 +503,8 @@ class GeneratedApproach:
  452    503          c = B.cell(cur)
  453    504          B.free[c] = True
  454    505          req = self.my_req[i] | S
         506 +        B.other_traj = self._traj(1 - i)
         507 +        B._send_t_cache = {}
  455    508          fin = B.run(c, L0, wanted=[req], tmax=TMAX, time_budget=5.0)
  456    509          bt = None
  457    510          for S2, (t, L) in fin.items():
diff --git a/approach2_old.py b/approach2_old.py
new file mode 100644
index 0000000..3748e9e
--- /dev/null
+++ b/approach2_old.py
@@ -0,0 +1,515 @@
           1 +"""Rovers: per-rover time-expanded BFS over (cell, done-set, calibrated, store, sent)."""
           2 +import numpy as np
           3 +
           4 +H = 0.1            # lattice spacing; a step moves up to 2 cells per axis (0.2m)
           5 +IMG_R = 2.0        # imaging range from base when facing away (true ~2.08)
           6 +SAMP_R = 0.235     # sampling range (true 0.25)
           7 +SEND_R = 3.85      # send range (true ~4.0)
           8 +TMAX = 120
           9 +BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
          10 +        "send": 0.5, "drop": 5 / 6}
          11 +NOOP, CAL, IMG, SAMP, DROP, SEND = "noop", "calibrate", "image", "sample", "drop", "send"
          12 +
          13 +
          14 +def _wrap(a):
          15 +    return (a + np.pi) % (2 * np.pi) - np.pi
          16 +
          17 +
          18 +def _type(space, name):
          19 +    for t in space.types:
          20 +        if t.name == name:
          21 +            return t
          22 +    return None
          23 +
          24 +
          25 +def _seg_dist(p, a, b):
          26 +    ab = b - a
          27 +    t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-12), 0.0, 1.0)
          28 +    return float(np.linalg.norm(a + t * ab - p))
          29 +
          30 +
          31 +class Scene:
          32 +    def __init__(self, state, space):
          33 +        self.T = {n: _type(space, n) for n in ["rover", "lander", "objective", "sample", "obstacle"]}
          34 +        g = state.get
          35 +        self.rovers = sorted(state.get_objects(self.T["rover"]), key=lambda o: o.name)
          36 +        self.lander = state.get_objects(self.T["lander"])[0]
          37 +        self.objectives = sorted(state.get_objects(self.T["objective"]), key=lambda o: o.name)
          38 +        self.samples = sorted(state.get_objects(self.T["sample"]), key=lambda o: o.name)
          39 +        self.obstacles = state.get_objects(self.T["obstacle"])
          40 +        self.lpos = np.array([g(self.lander, "x"), g(self.lander, "y")])
          41 +        self.obs_boxes = [(g(o, "x"), g(o, "y"), g(o, "half_x"), g(o, "half_y"), g(o, "half_z"))
          42 +                          for o in self.obstacles]
          43 +        self.pillars = [np.array([b[0], b[1]]) for b in self.obs_boxes if max(b[2], b[3]) < 0.15]
          44 +        self.opos = [np.array([g(o, "x"), g(o, "y")]) for o in self.objectives]
          45 +        self.spos = [np.array([g(o, "x"), g(o, "y")]) for o in self.samples]
          46 +        self.ssoil = [g(o, "is_soil") > 0.5 for o in self.samples]
          47 +
          48 +
          49 +def _shift_or(A, a, b):
          50 +    """OR of A shifted so that out[i,j] |= A[i-a, j-b]."""
          51 +    out = np.zeros_like(A)
          52 +    W, Hh = A.shape
          53 +    xs0, xs1 = max(0, a), min(W, W + a)
          54 +    ys0, ys1 = max(0, b), min(Hh, Hh + b)
          55 +    out[xs0:xs1, ys0:ys1] = A[xs0 - a:xs1 - a, ys0 - b:ys1 - b]
          56 +    return out
          57 +
          58 +
          59 +class RoverBFS:
          60 +    def __init__(self, scene, idx, home, img_r=IMG_R):
          61 +        self.sc = scene
          62 +        self.idx = idx
          63 +        self.home = np.array(home, dtype=float)
          64 +        side = 1.0 if home[0] > 0 else -1.0
          65 +        x0 = self.home[0] - H * np.floor((self.home[0] + 2.27) / H)
          66 +        y0 = self.home[1] - H * np.floor((self.home[1] + 2.27) / H)
          67 +        self.xs = np.arange(x0, 2.2701, H)
          68 +        self.ys = np.arange(y0, 2.2701, H)
          69 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
          70 +        self.X, self.Y = X, Y
          71 +        free = (np.abs(X) <= 2.265) & (np.abs(Y) <= 2.265) & (X * side >= 0.235)
          72 +        for (ox, oy, hx, hy, hz) in scene.obs_boxes:
          73 +            margin = 0.21 if max(hx, hy) >= 0.15 else 0.25
          74 +            dx = np.maximum(np.abs(X - ox) - hx, 0.0)
          75 +            dy = np.maximum(np.abs(Y - oy) - hy, 0.0)
          76 +            free &= (dx * dx + dy * dy) >= margin * margin
          77 +        lx, ly = scene.lpos
          78 +        free &= ~((X < lx + 0.71) & (Y < ly + 0.54))
          79 +        self.hc = (int(np.argmin(np.abs(self.xs - self.home[0]))), int(np.argmin(np.abs(self.ys - self.home[1]))))
          80 +        free[self.hc] = True
          81 +        self.free = free
          82 +        self.shape = free.shape
          83 +        self.nobj = len(scene.opos)
          84 +        self.n = self.nobj + 2
          85 +        self.STONE = 1 << self.nobj
          86 +        self.SOIL = 1 << (self.nobj + 1)
          87 +        self.CALB = 1 << self.n
          88 +        self.STOREB = 1 << (self.n + 1)
          89 +        self.SENTB = 1 << (self.n + 2)
          90 +        self.img_r = img_r
          91 +        self._prep()
          92 +
          93 +    def _prep(self):
          94 +        X, Y = self.X, self.Y
          95 +        sc = self.sc
          96 +        self.odist = [np.sqrt((X - o[0]) ** 2 + (Y - o[1]) ** 2) for o in sc.opos]
          97 +        vis_any = np.zeros(self.shape, bool)
          98 +        for d in self.odist:
          99 +            vis_any |= d <= self.img_r
         100 +        self.vis_any = vis_any & self.free
         101 +        stone = np.zeros(self.shape, bool)
         102 +        soil = np.zeros(self.shape, bool)
         103 +        for s, so in zip(sc.spos, sc.ssoil):
         104 +            m = (X - s[0]) ** 2 + (Y - s[1]) ** 2 <= SAMP_R ** 2
         105 +            if so:
         106 +                soil |= m
         107 +            else:
         108 +                stone |= m
         109 +        both = stone & soil
         110 +        self.stone_m = stone & ~both & self.free
         111 +        self.soil_m = soil & ~both & self.free
         112 +        self.send_m = ((X - sc.lpos[0]) ** 2 + (Y - sc.lpos[1]) ** 2 <= SEND_R ** 2) & self.free
         113 +        self._img_cache = {}
         114 +
         115 +    def pos(self, c):
         116 +        return np.array([self.xs[c[0]], self.ys[c[1]]])
         117 +
         118 +    def cell(self, p):
         119 +        return (int(np.argmin(np.abs(self.xs - p[0]))), int(np.argmin(np.abs(self.ys - p[1]))))
         120 +
         121 +    def img_masks(self, S):
         122 +        """For image op with done-set S: list of (r, mask) where r is nearest visible not-yet-imaged."""
         123 +        key = S & ((1 << self.nobj) - 1)
         124 +        if key in self._img_cache:
         125 +            return self._img_cache[key]
         126 +        best = np.full(self.shape, np.inf)
         127 +        arg = np.full(self.shape, -1)
         128 +        for r in range(self.nobj):
         129 +            if key & (1 << r):
         130 +                continue
         131 +            d = np.where(self.odist[r] <= self.img_r, self.odist[r], np.inf)
         132 +            better = d < best
         133 +            best = np.where(better, d, best)
         134 +            arg = np.where(better, r, arg)
         135 +        res = []
         136 +        for r in range(self.nobj):
         137 +            m = (arg == r) & self.free
         138 +            if m.any():
         139 +                res.append((r, m))
         140 +        self._img_cache[key] = res
         141 +        return res
         142 +
         143 +    def transitions(self, L):
         144 +        out = []
         145 +        S = L & ((1 << self.n) - 1)
         146 +        cal = L & self.CALB
         147 +        store = L & self.STOREB
         148 +        sent = L & self.SENTB
         149 +        if not sent:
         150 +            if not cal:
         151 +                out.append((CAL, L | self.CALB, self.vis_any))
         152 +            else:
         153 +                for r, m in self.img_masks(S):
         154 +                    out.append((IMG, (L | (1 << r)) & ~self.CALB, m))
         155 +            if not store:
         156 +                if not (S & self.STONE):
         157 +                    out.append((SAMP, L | self.STONE | self.STOREB, self.stone_m))
         158 +                if not (S & self.SOIL):
         159 +                    out.append((SAMP, L | self.SOIL | self.STOREB, self.soil_m))
         160 +            if S:
         161 +                out.append((SEND, L | self.SENTB, self.send_m))
         162 +        if store:
         163 +            out.append((DROP, L & ~self.STOREB, None))
         164 +        return out
         165 +
         166 +    def dilate(self, R):
         167 +        A = R | _shift_or(R, 1, 0) | _shift_or(R, -1, 0)
         168 +        A = A | _shift_or(R, 2, 0) | _shift_or(R, -2, 0)
         169 +        B = A | _shift_or(A, 0, 1) | _shift_or(A, 0, -1)
         170 +        B = B | _shift_or(A, 0, 2) | _shift_or(A, 0, -2)
         171 +        return B & self.free
         172 +
         173 +    def run(self, start_cell, L0, wanted=None, tmax=TMAX, time_budget=None):
         174 +        """Forward BFS. Returns dict S->earliest finish time (home, store empty, sent)."""
         175 +        import time as _t
         176 +        t_start = _t.time()
         177 +        R0 = np.zeros(self.shape, bool)
         178 +        R0[start_cell] = True
         179 +        self.layers = [{L0: R0}]
         180 +        self.rev = {}
         181 +        self.trans_cache = {}
         182 +        finish = {}
         183 +        hc = self.hc
         184 +        for t in range(1, tmax + 1):
         185 +            prev = self.layers[-1]
         186 +            new = {}
         187 +            for L, R in prev.items():
         188 +                D = self.dilate(R)
         189 +                if L in new:
         190 +                    new[L] |= D
         191 +                else:
         192 +                    new[L] = D.copy()
         193 +                tr = self.trans_cache.get(L)
         194 +                if tr is None:
         195 +                    tr = self.transitions(L)
         196 +                    self.trans_cache[L] = tr
         197 +                for op, L2, m in tr:
         198 +                    M = D if m is None else (D & m)
         199 +                    if not M.any():
         200 +                        continue
         201 +                    if L2 in new:
         202 +                        new[L2] |= M
         203 +                    else:
         204 +                        new[L2] = M.copy()
         205 +            self.layers.append(new)
         206 +            for L, R in new.items():
         207 +                if (L & self.SENTB) and not (L & self.STOREB) and R[hc]:
         208 +                    S = L & ((1 << self.n) - 1)
         209 +                    if S not in finish:
         210 +                        finish[S] = (t, L)
         211 +            if wanted is not None and all(any((S & w) == w for S in finish) for w in wanted):
         212 +                break
         213 +            if time_budget is not None and _t.time() - t_start > time_budget:
         214 +                break
         215 +        return finish
         216 +
         217 +    def extract(self, T, Lgoal):
         218 +        """Backtrack from (T, Lgoal, home). Returns list of (cell, op) for steps 1..T."""
         219 +        c = self.hc
         220 +        L = Lgoal
         221 +        steps = []
         222 +        W, Hh = self.shape
         223 +        for t in range(T, 0, -1):
         224 +            prev = self.layers[t - 1]
         225 +            # candidate predecessors: (Lp, op) such that transition Lp --op--> L valid at c
         226 +            cands = []
         227 +            if L in prev:
         228 +                cands.append((L, NOOP))
         229 +            for Lp in prev:
         230 +                tr = self.trans_cache.get(Lp)
         231 +                if tr is None:
         232 +                    tr = self.transitions(Lp)
         233 +                    self.trans_cache[Lp] = tr
         234 +                for op, L2, m in tr:
         235 +                    if L2 == L and (m is None or m[c]):
         236 +                        cands.append((Lp, op))
         237 +            found = None
         238 +            # prefer real ops over noop when tie (keeps ops early); prefer staying still
         239 +            for Lp, op in cands:
         240 +                R = prev[Lp]
         241 +                i0, j0 = c
         242 +                best = None
         243 +                for a in range(-2, 3):
         244 +                    for b in range(-2, 3):
         245 +                        ii, jj = i0 + a, j0 + b
         246 +                        if 0 <= ii < W and 0 <= jj < Hh and R[ii, jj]:
         247 +                            score = max(abs(a), abs(b)) * 0.01 + (abs(a) + abs(b)) * 0.001
         248 +                            if best is None or score < best[0]:
         249 +                                best = (score, (ii, jj))
         250 +                if best is not None:
         251 +                    found = (Lp, op, best[1])
         252 +                    break
         253 +            if found is None:
         254 +                return None
         255 +            Lp, op, cp = found
         256 +            steps.append((c, op, L))
         257 +            c = cp
         258 +            L = Lp
         259 +        steps.reverse()
         260 +        return steps
         261 +
         262 +
         263 +class GeneratedApproach:
         264 +    def __init__(self, action_space, observation_space, primitives):
         265 +        self.action_space = action_space
         266 +        self.space = observation_space
         267 +
         268 +    # ------------------------------------------------------------------
         269 +    def reset(self, state, info):
         270 +        self.sc = Scene(state, self.space)
         271 +        sc = self.sc
         272 +        g = state.get
         273 +        self.homes = [np.array([g(r, "x"), g(r, "y")]) for r in sc.rovers]
         274 +        self.home_th = [g(r, "theta") for r in sc.rovers]
         275 +        self.bfs = [RoverBFS(sc, i, self.homes[i]) for i in range(2)]
         276 +        nobj = len(sc.objectives)
         277 +        n = nobj + 2
         278 +        full = (1 << n) - 1
         279 +        fins = []
         280 +        for i in range(2):
         281 +            B = self.bfs[i]
         282 +            fins.append(B.run(B.hc, 0, wanted=[full], tmax=TMAX, time_budget=12.0))
         283 +        # best finish time for a superset-closed requirement: T_i(req) = min over S ⊇ req
         284 +        def best_for(fin, req):
         285 +            bt = None
         286 +            for S, (t, L) in fin.items():
         287 +                if (S & req) == req and (bt is None or t < bt[0]):
         288 +                    bt = (t, L, S)
         289 +            return bt
         290 +        best = None
         291 +        for s0 in range(1 << n):
         292 +            s1 = full & ~s0
         293 +            b0 = best_for(fins[0], s0) if s0 else (0, None, 0)
         294 +            b1 = best_for(fins[1], s1) if s1 else (0, None, 0)
         295 +            if b0 is None or b1 is None:
         296 +                continue
         297 +            key = (max(b0[0], b1[0]), b0[0] + b1[0])
         298 +            if best is None or key < best[0]:
         299 +                best = (key, b0, b1)
         300 +        self.plans = []
         301 +        self.my_req = [0, 0]
         302 +        for i in range(2):
         303 +            b = best[1 + i] if best else None
         304 +            steps = []
         305 +            if b is not None and b[1] is not None:
         306 +                # need layers from the run for rover i: rerun to be safe (layers overwritten? no: per-rover object)
         307 +                steps = self.bfs[i].extract(b[0], b[1]) or []
         308 +                self.my_req[i] = b[2]
         309 +            self.plans.append({"steps": steps, "k": 0, "fail": 0})
         310 +        self.done_flag = False
         311 +
         312 +    # ------------------------------------------------------------------
         313 +    def _flags(self, state, i):
         314 +        sc = self.sc
         315 +        g = state.get
         316 +        me = "rover%d" % i
         317 +        S = 0
         318 +        for r, o in enumerate(sc.objectives):
         319 +            if g(o, "have_image_" + me) > 0.5:
         320 +                S |= 1 << r
         321 +        nobj = len(sc.objectives)
         322 +        for s, soil in zip(sc.samples, sc.ssoil):
         323 +            if g(s, "analyzed_" + me) > 0.5:
         324 +                S |= 1 << (nobj + (1 if soil else 0))
         325 +        cal = g(sc.rovers[i], "calibrated") > 0.5
         326 +        store = g(sc.rovers[i], "store_full") > 0.5
         327 +        holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
         328 +            any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
         329 +        return S, cal, store, holding
         330 +
         331 +    def _visible(self, p, th, k, margin=0.03):
         332 +        c = p + np.array([-0.087 * np.cos(th) + 0.0125 * np.sin(th), -0.087 * np.sin(th) - 0.0125 * np.cos(th)])
         333 +        o = self.sc.opos[k]
         334 +        v = o - c
         335 +        if np.linalg.norm(v) > 1.9972 - margin:
         336 +            return False
         337 +        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
         338 +        if ang < np.radians(108):
         339 +            for pc in self.sc.pillars:
         340 +                if _seg_dist(pc, c, o) < 0.11:
         341 +                    return False
         342 +        return True
         343 +
         344 +    def _can_send(self, state, i, p, th):
         345 +        sc = self.sc
         346 +        v = sc.lpos - p
         347 +        if np.linalg.norm(v) > SEND_R:
         348 +            return False
         349 +        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
         350 +        if ang >= np.radians(115):
         351 +            return True
         352 +        g = state.get
         353 +        orv = sc.rovers[1 - i]
         354 +        op = np.array([g(orv, "x"), g(orv, "y")])
         355 +        if _seg_dist(op, p, sc.lpos) < 0.27:
         356 +            return False
         357 +        for pc in sc.pillars:
         358 +            if _seg_dist(pc, p, sc.lpos) < 0.13:
         359 +                return False
         360 +        return True
         361 +
         362 +    def _los_clear(self, p, q):
         363 +        sc = self.sc
         364 +        if np.linalg.norm(sc.lpos - p) > SEND_R:
         365 +            return False
         366 +        if _seg_dist(q, p, sc.lpos) < 0.29:
         367 +            return False
         368 +        for pc in sc.pillars:
         369 +            if _seg_dist(pc, p, sc.lpos) < 0.14:
         370 +                return False
         371 +        return True
         372 +
         373 +    def _other_pos_at(self, i, dt, state):
         374 +        """Predicted position of rover (1-i) dt steps from now."""
         375 +        j = 1 - i
         376 +        plan = self.plans[j]
         377 +        steps = plan["steps"]
         378 +        B = self.bfs[j]
         379 +        if not steps:
         380 +            g = state.get
         381 +            return np.array([g(self.sc.rovers[j], "x"), g(self.sc.rovers[j], "y")])
         382 +        idx = min(len(steps) - 1, plan["k"] + dt - 1)
         383 +        if idx < 0:
         384 +            g = state.get
         385 +            return np.array([g(self.sc.rovers[j], "x"), g(self.sc.rovers[j], "y")])
         386 +        return B.pos(steps[idx][0])
         387 +
         388 +    def _desired_heading(self, state, i, p, th, k, holding):
         389 +        sc = self.sc
         390 +        plan = self.plans[i]
         391 +        steps = plan["steps"]
         392 +        B = self.bfs[i]
         393 +        nobj = len(sc.objectives)
         394 +        # next image op in plan: face away from the objective it targets
         395 +        for idx in range(k, len(steps)):
         396 +            c, op, L = steps[idx]
         397 +            if op == IMG:
         398 +                # which objective: bit newly set in L vs previous
         399 +                Lp = steps[idx - 1][2] if idx > 0 else plan.get("L0", 0)
         400 +                newbits = (L & ~Lp) & ((1 << nobj) - 1)
         401 +                if newbits:
         402 +                    r = int(np.log2(newbits & -newbits))
         403 +                    v = B.pos(c) - sc.opos[r]
         404 +                    return np.arctan2(v[1], v[0])
         405 +        hth = self.home_th[i]
         406 +        if holding:
         407 +            # will a send be possible facing home-ish heading later?
         408 +            last = len(steps)
         409 +            ok = False
         410 +            for idx in range(k, last):
         411 +                q = self._other_pos_at(i, idx - k + 1, state)
         412 +                if self._los_clear(B.pos(steps[idx][0]), q):
         413 +                    ok = True
         414 +                    break
         415 +            if not ok and self._los_clear(p, self._other_pos_at(i, 0, state)):
         416 +                ok = True
         417 +            if not ok:
         418 +                v = p - sc.lpos
         419 +                away = np.arctan2(v[1], v[0])
         420 +                best, bc = None, None
         421 +                for c in np.linspace(-np.radians(60), np.radians(60), 25):
         422 +                    h = away + c
         423 +                    cost = abs(_wrap(h - th)) + abs(_wrap(hth - h)) + 0.01 * abs(_wrap(h - th))
         424 +                    if best is None or cost < best:
         425 +                        best, bc = cost, h
         426 +                return bc
         427 +        return hth
         428 +
         429 +    def _replan(self, state, i, cur):
         430 +        B = self.bfs[i]
         431 +        S, cal, store, holding = self._flags(state, i)
         432 +        L0 = S | (B.CALB if cal else 0) | (B.STOREB if store else 0)
         433 +        if not holding and S:
         434 +            L0 |= B.SENTB
         435 +        c = B.cell(cur)
         436 +        B.free[c] = True
         437 +        req = self.my_req[i] | S
         438 +        fin = B.run(c, L0, wanted=[req], tmax=TMAX, time_budget=5.0)
         439 +        bt = None
         440 +        for S2, (t, L) in fin.items():
         441 +            if (S2 & req) == req and (bt is None or t < bt[0]):
         442 +                bt = (t, L)
         443 +        steps = B.extract(bt[0], bt[1]) if bt else []
         444 +        self.plans[i] = {"steps": steps or [], "k": 0, "fail": 0, "L0": L0}
         445 +
         446 +    def _rover_action(self, state, i):
         447 +        sc = self.sc
         448 +        g = state.get
         449 +        rv = sc.rovers[i]
         450 +        cur = np.array([g(rv, "x"), g(rv, "y")])
         451 +        th = g(rv, "theta")
         452 +        B = self.bfs[i]
         453 +        plan = self.plans[i]
         454 +        S, cal, store, holding = self._flags(state, i)
         455 +        steps = plan["steps"]
         456 +        k = plan["k"]
         457 +        # verify previous step outcome
         458 +        if k > 0 and k <= len(steps):
         459 +            c, op, L = steps[k - 1]
         460 +            pos_ok = np.linalg.norm(B.pos(c) - cur) < 0.02
         461 +            Sp = L & ((1 << B.n) - 1)
         462 +            op_ok = True
         463 +            if op in (IMG, SAMP):
         464 +                op_ok = (S & Sp) == Sp
         465 +            elif op == CAL:
         466 +                op_ok = cal
         467 +            elif op == DROP:
         468 +                op_ok = not store
         469 +            if not (pos_ok and op_ok):
         470 +                plan["fail"] += 1
         471 +                if plan["fail"] > 4 or (not pos_ok and plan["fail"] > 2):
         472 +                    self._replan(state, i, cur)
         473 +                    plan = self.plans[i]
         474 +                    steps = plan["steps"]
         475 +                    k = 0
         476 +                else:
         477 +                    k = k - 1  # retry the step
         478 +            else:
         479 +                plan["fail"] = 0
         480 +        if k < len(steps):
         481 +            c, op, L = steps[k]
         482 +            target = B.pos(c)
         483 +            plan["k"] = k + 1
         484 +        else:
         485 +            target = cur if np.linalg.norm(cur - self.homes[i]) < 0.02 else self.homes[i]
         486 +            op = NOOP
         487 +            plan["k"] = len(steps) + 1 if steps else 1
         488 +            # finished plan: if tasks remain undone, replan
         489 +            if (S & self.my_req[i]) != self.my_req[i] or store:
         490 +                self._replan(state, i, cur)
         491 +                return self._rover_action_fresh(state, i)
         492 +        d = np.clip(target - cur, -0.2, 0.2)
         493 +        newp = cur + d
         494 +        dth = float(np.clip(_wrap(self._desired_heading(state, i, newp, th, k + 1, holding) - th), -0.4, 0.4))
         495 +        newth = _wrap(th + dth)
         496 +        # op adjustments
         497 +        if op == SEND:
         498 +            op = NOOP
         499 +        if op in (NOOP,) and holding and self._can_send(state, i, newp, newth):
         500 +            op = SEND
         501 +        elif op == NOOP and store and not any(s[1] == SAMP for s in steps[k:]):
         502 +            op = NOOP
         503 +        return np.array([d[0], d[1], dth, BAND[op]], dtype=np.float32)
         504 +
         505 +    def _rover_action_fresh(self, state, i):
         506 +        plan = self.plans[i]
         507 +        if not plan["steps"]:
         508 +            return np.array([0, 0, 0, BAND[NOOP]], dtype=np.float32)
         509 +        plan["k"] = 0
         510 +        return self._rover_action(state, i)
         511 +
         512 +    def get_action(self, state):
         513 +        a0 = self._rover_action(state, 0)
         514 +        a1 = self._rover_action(state, 1)
         515 +        return np.concatenate([a0, a1]).astype(np.float32)
diff --git a/cmp.py b/cmp.py
new file mode 100644
index 0000000..83c15c4
--- /dev/null
+++ b/cmp.py
@@ -0,0 +1,4 @@
           1 +import json, sys
           2 +a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
           3 +d = [(k, a[k], b[k]) for k in a if k in b and a[k] != b[k]]
           4 +print(d)
diff --git a/eval_many.py b/eval_many.py
index 82f4b1b..7d79e37 100644
--- a/eval_many.py
+++ b/eval_many.py
@@ -23,3 +23,5 @@ if __name__ == '__main__':
   23     23          if r[2] == 9999 or r[2] - r[3] > 2: print("seed %d nobj %d steps %d plan %d t %.2f" % r)
   24     24      st = [r[2] for r in res]
   25     25      print("mean", np.mean([s for s in st if s < 9999]), "fails", sum(s == 9999 for s in st), "maxplan", max(r[4] for r in res))
          26 +    import json, os
          27 +    json.dump({r[0]: r[2] for r in res}, open('res_%s_%s.json' % (os.environ.get('APP','approach'), os.environ.get('TAG','x')), 'w'))
diff --git a/res_approach2_a.json b/res_approach2_a.json
new file mode 100644
index 0000000..7b0d24d
--- /dev/null
+++ b/res_approach2_a.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 22, "4": 25, "5": 25, "6": 20, "7": 22, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 25, "14": 29, "15": 25, "16": 22, "17": 22, "18": 22, "19": 27, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 21, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 22, "37": 18, "38": 21, "39": 25, "40": 21, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 20}
\ No newline at end of file
diff --git a/res_approach2_old_a.json b/res_approach2_old_a.json
new file mode 100644
index 0000000..9e876f4
--- /dev/null
+++ b/res_approach2_old_a.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 21, "4": 25, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 25, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 22, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 29, "37": 18, "38": 21, "39": 22, "40": 21, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 19}
\ No newline at end of file
```

</details>

<a id="C011"></a>
### C011 · approach2: keep refined plan only if not longer

Commit `c8236a81c37f9062b9a8b27b35c1caf2a2f9c578`; parents: 617ca9f129760e7fe93b3631ea1ea3e52b698fa7. Recorded author date: 2026-10-01T11:21:39+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E0927](01_timeline.md#E0927): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C011_c8236a8.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach2.py b/approach2.py
index adbedab..f6c9959 100644
--- a/approach2.py
+++ b/approach2.py
@@ -358,7 +358,7 @@ class GeneratedApproach:
  358    358                      bt = (t, L)
  359    359              if bt is not None:
  360    360                  st = B.extract(bt[0], bt[1])
  361        -                if st:
         361 +                if st and len(st) <= len(self.plans[i]["steps"]):
  362    362                      self.plans[i] = {"steps": st, "k": 0, "fail": 0}
  363    363          self.done_flag = False
  364    364  
diff --git a/res_approach2_b.json b/res_approach2_b.json
new file mode 100644
index 0000000..5a44145
--- /dev/null
+++ b/res_approach2_b.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 21, "4": 26, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 28, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 23, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 21, "37": 18, "38": 23, "39": 22, "40": 23, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 20}
\ No newline at end of file
```

</details>

<a id="C012"></a>
### C012 · approach2: replan immediately when failed op changed state unexpectedly

Commit `3e4a72a89c3d5c9832537741d4028de12f4e70c8`; parents: c8236a81c37f9062b9a8b27b35c1caf2a2f9c578. Recorded author date: 2026-10-01T11:22:55+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E0941](01_timeline.md#E0941): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C012_3e4a72a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach2.py b/approach2.py
index f6c9959..fd3529a 100644
--- a/approach2.py
+++ b/approach2.py
@@ -538,7 +538,11 @@ class GeneratedApproach:
  538    538                  op_ok = not store
  539    539              if not (pos_ok and op_ok):
  540    540                  plan["fail"] += 1
  541        -                if plan["fail"] > 4 or (not pos_ok and plan["fail"] > 2):
         541 +                Lpre = steps[k - 2][2] if k >= 2 else plan.get("L0", 0)
         542 +                mask = ((1 << B.n) - 1) | B.CALB | B.STOREB
         543 +                Lact = S | (B.CALB if cal else 0) | (B.STOREB if store else 0)
         544 +                changed = (Lact & mask) != (Lpre & mask)
         545 +                if plan["fail"] > 4 or (not pos_ok and plan["fail"] > 2) or (pos_ok and changed):
  542    546                      self._replan(state, i, cur)
  543    547                      plan = self.plans[i]
  544    548                      steps = plan["steps"]
diff --git a/res_approach2_d.json b/res_approach2_d.json
new file mode 100644
index 0000000..58478cd
--- /dev/null
+++ b/res_approach2_d.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 21, "4": 26, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 25, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 22, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 21, "37": 18, "38": 23, "39": 22, "40": 21, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 19}
\ No newline at end of file
```

</details>

<a id="C013"></a>
### C013 · Adopt time-expanded BFS planner (approach2) as approach.py; mean 21.52 on seeds 0-47

Commit `86fe1c7be532017d992ba4365b1aaa941885666d`; parents: 3e4a72a89c3d5c9832537741d4028de12f4e70c8. Recorded author date: 2026-10-01T11:23:55+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0952](01_timeline.md#E0952): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_86fe1c7_approach.py) · [Exact all-file diff](evidence/diffs/C013_86fe1c7.diff)

[Previous saved controller snapshot](evidence/versions/C007_6945310_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f4ca772..fd3529a 100644
--- a/approach.py
+++ b/approach.py
@@ -1,14 +1,14 @@
    1        -import itertools
           1 +"""Rovers: per-rover time-expanded BFS over (cell, done-set, calibrated, store, sent)."""
    2      2  import numpy as np
    3      3  
    4        -H = 0.1            # lattice spacing (a step can move up to 2 cells per axis)
    5        -R_STEP = 2         # cells per step
           4 +H = 0.1            # lattice spacing; a step moves up to 2 cells per axis (0.2m)
    6      5  IMG_R = 2.0        # imaging range from base when facing away (true ~2.08)
    7      6  SAMP_R = 0.235     # sampling range (true 0.25)
    8      7  SEND_R = 3.85      # send range (true ~4.0)
           8 +TMAX = 120
    9      9  BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
   10     10          "send": 0.5, "drop": 5 / 6}
   11        -INF = 1e9
          11 +NOOP, CAL, IMG, SAMP, DROP, SEND = "noop", "calibrate", "image", "sample", "drop", "send"
   12     12  
   13     13  
   14     14  def _wrap(a):
@@ -22,6 +22,12 @@ def _type(space, name):
   22     22      return None
   23     23  
   24     24  
          25 +def _seg_dist(p, a, b):
          26 +    ab = b - a
          27 +    t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-12), 0.0, 1.0)
          28 +    return float(np.linalg.norm(a + t * ab - p))
          29 +
          30 +
   25     31  class Scene:
   26     32      def __init__(self, state, space):
   27     33          self.T = {n: _type(space, n) for n in ["rover", "lander", "objective", "sample", "obstacle"]}
@@ -32,40 +38,36 @@ class Scene:
   32     38          self.samples = sorted(state.get_objects(self.T["sample"]), key=lambda o: o.name)
   33     39          self.obstacles = state.get_objects(self.T["obstacle"])
   34     40          self.lpos = np.array([g(self.lander, "x"), g(self.lander, "y")])
   35        -        self.obs_boxes = []
   36        -        for o in self.obstacles:
   37        -            self.obs_boxes.append((g(o, "x"), g(o, "y"), g(o, "half_x"), g(o, "half_y"), g(o, "half_z")))
          41 +        self.obs_boxes = [(g(o, "x"), g(o, "y"), g(o, "half_x"), g(o, "half_y"), g(o, "half_z"))
          42 +                          for o in self.obstacles]
          43 +        self.pillars = [np.array([b[0], b[1]]) for b in self.obs_boxes if max(b[2], b[3]) < 0.15]
   38     44          self.opos = [np.array([g(o, "x"), g(o, "y")]) for o in self.objectives]
   39     45          self.spos = [np.array([g(o, "x"), g(o, "y")]) for o in self.samples]
   40     46          self.ssoil = [g(o, "is_soil") > 0.5 for o in self.samples]
   41     47  
   42     48  
   43        -class RoverPlanner:
   44        -    """Lattice anchored at the rover's home; subset DP over task regions."""
          49 +def _shift_or(A, a, b):
          50 +    """OR of A shifted so that out[i,j] |= A[i-a, j-b]."""
          51 +    out = np.zeros_like(A)
          52 +    W, Hh = A.shape
          53 +    xs0, xs1 = max(0, a), min(W, W + a)
          54 +    ys0, ys1 = max(0, b), min(Hh, Hh + b)
          55 +    out[xs0:xs1, ys0:ys1] = A[xs0 - a:xs1 - a, ys0 - b:ys1 - b]
          56 +    return out
          57 +
   45     58  
   46        -    def __init__(self, scene, idx, home):
   47        -        self.scene = scene
          59 +class RoverBFS:
          60 +    def __init__(self, scene, idx, home, img_r=IMG_R, home_th=0.0, other_home=None):
          61 +        self.sc = scene
          62 +        self.home_th = home_th
          63 +        self.other_home = other_home
   48     64          self.idx = idx
   49     65          self.home = np.array(home, dtype=float)
   50     66          side = 1.0 if home[0] > 0 else -1.0
   51        -        self.side = side
   52        -        self.img_r = IMG_R
   53        -        xs = []
   54        -        x = self.home[0]
   55        -        while x - H >= -2.27:
   56        -            x -= H
   57        -        while x <= 2.27:
   58        -            xs.append(x)
   59        -            x += H
   60        -        ys = []
   61        -        y = self.home[1]
   62        -        while y - H >= -2.27:
   63        -            y -= H
   64        -        while y <= 2.27:
   65        -            ys.append(y)
   66        -            y += H
   67        -        self.xs = np.array(xs)
   68        -        self.ys = np.array(ys)
          67 +        x0 = self.home[0] - H * np.floor((self.home[0] + 2.27) / H)
          68 +        y0 = self.home[1] - H * np.floor((self.home[1] + 2.27) / H)
          69 +        self.xs = np.arange(x0, 2.2701, H)
          70 +        self.ys = np.arange(y0, 2.2701, H)
   69     71          X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
   70     72          self.X, self.Y = X, Y
   71     73          free = (np.abs(X) <= 2.265) & (np.abs(Y) <= 2.265) & (X * side >= 0.235)
@@ -76,134 +78,221 @@ class RoverPlanner:
   76     78              free &= (dx * dx + dy * dy) >= margin * margin
   77     79          lx, ly = scene.lpos
   78     80          free &= ~((X < lx + 0.71) & (Y < ly + 0.54))
   79        -        self.hi = int(np.argmin(np.abs(self.xs - self.home[0])))
   80        -        self.hj = int(np.argmin(np.abs(self.ys - self.home[1])))
   81        -        free[self.hi, self.hj] = True
          81 +        self.hc = (int(np.argmin(np.abs(self.xs - self.home[0]))), int(np.argmin(np.abs(self.ys - self.home[1]))))
          82 +        free[self.hc] = True
   82     83          self.free = free
   83     84          self.shape = free.shape
   84        -        self.offsets = [(a, b) for a in range(-R_STEP, R_STEP + 1) for b in range(-R_STEP, R_STEP + 1)
   85        -                        if (a, b) != (0, 0)]
          85 +        self.nobj = len(scene.opos)
          86 +        self.n = self.nobj + 2
          87 +        self.STONE = 1 << self.nobj
          88 +        self.SOIL = 1 << (self.nobj + 1)
          89 +        self.CALB = 1 << self.n
          90 +        self.STOREB = 1 << (self.n + 1)
          91 +        self.SENTB = 1 << (self.n + 2)
          92 +        self.img_r = img_r
          93 +        self._prep()
          94 +
          95 +    def _prep(self):
          96 +        X, Y = self.X, self.Y
          97 +        sc = self.sc
          98 +        self.odist = [np.sqrt((X - o[0]) ** 2 + (Y - o[1]) ** 2) for o in sc.opos]
          99 +        vis_any = np.zeros(self.shape, bool)
         100 +        for d in self.odist:
         101 +            vis_any |= d <= self.img_r
         102 +        self.vis_any = vis_any & self.free
         103 +        stone = np.zeros(self.shape, bool)
         104 +        soil = np.zeros(self.shape, bool)
         105 +        for s, so in zip(sc.spos, sc.ssoil):
         106 +            m = (X - s[0]) ** 2 + (Y - s[1]) ** 2 <= SAMP_R ** 2
         107 +            if so:
         108 +                soil |= m
         109 +            else:
         110 +                stone |= m
         111 +        both = stone & soil
         112 +        self.stone_m = stone & ~both & self.free
         113 +        self.soil_m = soil & ~both & self.free
         114 +        inr = ((X - sc.lpos[0]) ** 2 + (Y - sc.lpos[1]) ** 2 <= SEND_R ** 2) & self.free
         115 +        away = np.arctan2(Y - sc.lpos[1], X - sc.lpos[0])
         116 +        self.send_head_ok = inr & (np.abs(_wrap(self.home_th - away)) <= np.radians(60))
         117 +        pill = np.zeros(self.shape, bool)
         118 +        for pc in sc.pillars:
         119 +            pill |= self._segdist_grid(pc) < 0.14
         120 +        self.send_static = inr & ~pill
         121 +        self.send_m = inr
         122 +        self.other_traj = None
         123 +        self._send_t_cache = {}
         124 +        self._img_cache = {}
         125 +
         126 +    def _segdist_grid(self, q):
         127 +        """Distance from point q to segment (cell -> lander) for every cell."""
         128 +        L = self.sc.lpos
         129 +        ax, ay = self.X, self.Y
         130 +        bx, by = L[0] - ax, L[1] - ay
         131 +        qx, qy = q[0] - ax, q[1] - ay
         132 +        t = np.clip((qx * bx + qy * by) / np.maximum(bx * bx + by * by, 1e-12), 0.0, 1.0)
         133 +        return np.sqrt((qx - t * bx) ** 2 + (qy - t * by) ** 2)
         134 +
         135 +    def send_mask_t(self, t):
         136 +        if self.other_traj is None:
         137 +            return self.send_m
         138 +        q = self.other_traj[min(t, len(self.other_traj) - 1)]
         139 +        key = (round(float(q[0]), 3), round(float(q[1]), 3))
         140 +        m = self._send_t_cache.get(key)
         141 +        if m is None:
         142 +            m = self.send_head_ok | (self.send_static & (self._segdist_grid(q) >= 0.29))
         143 +            self._send_t_cache[key] = m
         144 +        return m
   86    145  
   87    146      def pos(self, c):
   88    147          return np.array([self.xs[c[0]], self.ys[c[1]]])
   89    148  
   90    149      def cell(self, p):
   91        -        i = int(np.argmin(np.abs(self.xs - p[0])))
   92        -        j = int(np.argmin(np.abs(self.ys - p[1])))
   93        -        return (i, j)
   94        -
   95        -    def region_mask(self, task):
   96        -        kind, k = task
   97        -        sc = self.scene
   98        -        if kind == "obj":
   99        -            o = sc.opos[k]
  100        -            m = (self.X - o[0]) ** 2 + (self.Y - o[1]) ** 2 <= self.img_r ** 2
  101        -        else:  # 'stone' or 'soil'
  102        -            want_soil = kind == "soil"
  103        -            m = np.zeros(self.shape, bool)
  104        -            for s, soil in zip(sc.spos, sc.ssoil):
  105        -                if soil == want_soil:
  106        -                    m |= (self.X - s[0]) ** 2 + (self.Y - s[1]) ** 2 <= SAMP_R ** 2
  107        -        return m & self.free
  108        -
  109        -    def propagate(self, F):
  110        -        G = F.copy()
  111        -        R = R_STEP
  112        -        W, Hh = self.shape
  113        -        free = self.free
  114        -        while True:
  115        -            P = np.full((W + 2 * R, Hh + 2 * R), INF)
  116        -            P[R:R + W, R:R + Hh] = G
  117        -            best = G.copy()
  118        -            for a, b in self.offsets:
  119        -                np.minimum(best, P[R + a:R + a + W, R + b:R + b + Hh] + 1.0, out=best)
  120        -            best[~free] = INF
  121        -            if np.array_equal(best, G):
  122        -                return G
  123        -            G = best
  124        -
  125        -    def dp(self, tasks, start=None):
  126        -        """Returns dict subset(bitmask)->cost of tour start->tasks->home, and stores fields."""
  127        -        if start is None:
  128        -            start = (self.hi, self.hj)
  129        -        n = len(tasks)
  130        -        masks = [self.region_mask(t) for t in tasks]
  131        -        F0 = np.full(self.shape, INF)
  132        -        F0[start] = 0.0
  133        -        Fs = {0: F0}
  134        -        Gs = {}
  135        -        order = sorted(range(1 << n), key=lambda s: bin(s).count("1"))
  136        -        for s in order:
  137        -            F = Fs.get(s)
  138        -            if F is None:
         150 +        return (int(np.argmin(np.abs(self.xs - p[0]))), int(np.argmin(np.abs(self.ys - p[1]))))
         151 +
         152 +    def img_masks(self, S):
         153 +        """For image op with done-set S: list of (r, mask) where r is nearest visible not-yet-imaged."""
         154 +        key = S & ((1 << self.nobj) - 1)
         155 +        if key in self._img_cache:
         156 +            return self._img_cache[key]
         157 +        best = np.full(self.shape, np.inf)
         158 +        arg = np.full(self.shape, -1)
         159 +        for r in range(self.nobj):
         160 +            if key & (1 << r):
  139    161                  continue
  140        -            G = self.propagate(F)
  141        -            Gs[s] = G
  142        -            for r in range(n):
  143        -                if s & (1 << r):
  144        -                    continue
  145        -                if not masks[r].any():
  146        -                    continue
  147        -                s2 = s | (1 << r)
  148        -                cand = np.where(masks[r], G, INF)
  149        -                if s2 in Fs:
  150        -                    np.minimum(Fs[s2], cand, out=Fs[s2])
         162 +            d = np.where(self.odist[r] <= self.img_r, self.odist[r], np.inf)
         163 +            better = d < best
         164 +            best = np.where(better, d, best)
         165 +            arg = np.where(better, r, arg)
         166 +        res = []
         167 +        for r in range(self.nobj):
         168 +            m = (arg == r) & self.free
         169 +            if m.any():
         170 +                res.append((r, m))
         171 +        self._img_cache[key] = res
         172 +        return res
         173 +
         174 +    def transitions(self, L):
         175 +        out = []
         176 +        S = L & ((1 << self.n) - 1)
         177 +        cal = L & self.CALB
         178 +        store = L & self.STOREB
         179 +        sent = L & self.SENTB
         180 +        if not sent:
         181 +            if not cal:
         182 +                out.append((CAL, L | self.CALB, self.vis_any))
         183 +            else:
         184 +                for r, m in self.img_masks(S):
         185 +                    out.append((IMG, (L | (1 << r)) & ~self.CALB, m))
         186 +            if not store:
         187 +                if not (S & self.STONE):
         188 +                    out.append((SAMP, L | self.STONE | self.STOREB, self.stone_m))
         189 +                if not (S & self.SOIL):
         190 +                    out.append((SAMP, L | self.SOIL | self.STOREB, self.soil_m))
         191 +            if S:
         192 +                out.append((SEND, L | self.SENTB, "SEND"))
         193 +        if store:
         194 +            out.append((DROP, L & ~self.STOREB, None))
         195 +        return out
         196 +
         197 +    def dilate(self, R):
         198 +        A = R | _shift_or(R, 1, 0) | _shift_or(R, -1, 0)
         199 +        A = A | _shift_or(R, 2, 0) | _shift_or(R, -2, 0)
         200 +        B = A | _shift_or(A, 0, 1) | _shift_or(A, 0, -1)
         201 +        B = B | _shift_or(A, 0, 2) | _shift_or(A, 0, -2)
         202 +        return B & self.free
         203 +
         204 +    def run(self, start_cell, L0, wanted=None, tmax=TMAX, time_budget=None):
         205 +        """Forward BFS. Returns dict S->earliest finish time (home, store empty, sent)."""
         206 +        import time as _t
         207 +        t_start = _t.time()
         208 +        R0 = np.zeros(self.shape, bool)
         209 +        R0[start_cell] = True
         210 +        self.layers = [{L0: R0}]
         211 +        self.rev = {}
         212 +        self.trans_cache = {}
         213 +        finish = {}
         214 +        hc = self.hc
         215 +        for t in range(1, tmax + 1):
         216 +            prev = self.layers[-1]
         217 +            new = {}
         218 +            for L, R in prev.items():
         219 +                D = self.dilate(R)
         220 +                if L in new:
         221 +                    new[L] |= D
  151    222                  else:
  152        -                    Fs[s2] = cand
  153        -        self._tasks = tasks
  154        -        self._masks = masks
  155        -        self._Fs = Fs
  156        -        self._Gs = Gs
  157        -        self._start = start
  158        -        costs = {}
  159        -        for s, G in Gs.items():
  160        -            costs[s] = G[self.hi, self.hj]
  161        -        return costs
  162        -
  163        -    def extract(self, s):
  164        -        """Backtrack path for subset s (from last dp). Returns list of cells and visits dict idx->[tasks]."""
  165        -        Gs, Fs, masks = self._Gs, self._Fs, self._masks
  166        -        c = (self.hi, self.hj)
  167        -        v = Gs[s][c]
  168        -        rev = [c]
  169        -        rev_visits = []  # (position in rev, task index)
  170        -        W, Hh = self.shape
  171        -        guard = 0
  172        -        while True:
  173        -            guard += 1
  174        -            if guard > 10000:
         223 +                    new[L] = D.copy()
         224 +                tr = self.trans_cache.get(L)
         225 +                if tr is None:
         226 +                    tr = self.transitions(L)
         227 +                    self.trans_cache[L] = tr
         228 +                for op, L2, m in tr:
         229 +                    if isinstance(m, str):
         230 +                        m = self.send_mask_t(t)
         231 +                    M = D if m is None else (D & m)
         232 +                    if not M.any():
         233 +                        continue
         234 +                    if L2 in new:
         235 +                        new[L2] |= M
         236 +                    else:
         237 +                        new[L2] = M.copy()
         238 +            self.layers.append(new)
         239 +            for L, R in new.items():
         240 +                if (L & self.SENTB) and not (L & self.STOREB) and R[hc]:
         241 +                    S = L & ((1 << self.n) - 1)
         242 +                    if S not in finish:
         243 +                        finish[S] = (t, L)
         244 +            if wanted is not None and all(any((S & w) == w for S in finish) for w in wanted):
  175    245                  break
  176        -            if s == 0 and c == self._start:
         246 +            if time_budget is not None and _t.time() - t_start > time_budget:
  177    247                  break
  178        -            # try region entry at c
  179        -            moved = False
  180        -            if s != 0 and Fs[s][c] <= v + 1e-9:
  181        -                for r in range(len(masks)):
  182        -                    if s & (1 << r) and masks[r][c]:
  183        -                        s2 = s & ~(1 << r)
  184        -                        if s2 in Gs and Gs[s2][c] <= v + 1e-9:
  185        -                            rev_visits.append((len(rev) - 1, r))
  186        -                            s = s2
  187        -                            moved = True
  188        -                            break
  189        -            if moved:
  190        -                continue
  191        -            for a, b in self.offsets:
  192        -                n = (c[0] + a, c[1] + b)
  193        -                if 0 <= n[0] < W and 0 <= n[1] < Hh and Gs[s][n] <= v - 1 + 1e-9:
  194        -                    c = n
  195        -                    v = Gs[s][n]
  196        -                    rev.append(c)
  197        -                    moved = True
         248 +        return finish
         249 +
         250 +    def extract(self, T, Lgoal):
         251 +        """Backtrack from (T, Lgoal, home). Returns list of (cell, op) for steps 1..T."""
         252 +        c = self.hc
         253 +        L = Lgoal
         254 +        steps = []
         255 +        W, Hh = self.shape
         256 +        for t in range(T, 0, -1):
         257 +            prev = self.layers[t - 1]
         258 +            # candidate predecessors: (Lp, op) such that transition Lp --op--> L valid at c
         259 +            cands = []
         260 +            if L in prev:
         261 +                cands.append((L, NOOP))
         262 +            for Lp in prev:
         263 +                tr = self.trans_cache.get(Lp)
         264 +                if tr is None:
         265 +                    tr = self.transitions(Lp)
         266 +                    self.trans_cache[Lp] = tr
         267 +                for op, L2, m in tr:
         268 +                    if isinstance(m, str):
         269 +                        m = self.send_mask_t(t)
         270 +                    if L2 == L and (m is None or m[c]):
         271 +                        cands.append((Lp, op))
         272 +            found = None
         273 +            # prefer real ops over noop when tie (keeps ops early); prefer staying still
         274 +            for Lp, op in cands:
         275 +                R = prev[Lp]
         276 +                i0, j0 = c
         277 +                best = None
         278 +                for a in range(-2, 3):
         279 +                    for b in range(-2, 3):
         280 +                        ii, jj = i0 + a, j0 + b
         281 +                        if 0 <= ii < W and 0 <= jj < Hh and R[ii, jj]:
         282 +                            score = max(abs(a), abs(b)) * 0.01 + (abs(a) + abs(b)) * 0.001
         283 +                            if best is None or score < best[0]:
         284 +                                best = (score, (ii, jj))
         285 +                if best is not None:
         286 +                    found = (Lp, op, best[1])
  198    287                      break
  199        -            if not moved:
  200        -                break
  201        -        L = len(rev)
  202        -        path = rev[::-1]
  203        -        visits = {}
  204        -        for (ri, r) in rev_visits:
  205        -            visits.setdefault(L - 1 - ri, []).append(self._tasks[r])
  206        -        return path, visits
         288 +            if found is None:
         289 +                return None
         290 +            Lp, op, cp = found
         291 +            steps.append((c, op, L))
         292 +            c = cp
         293 +            L = Lp
         294 +        steps.reverse()
         295 +        return steps
  207    296  
  208    297  
  209    298  class GeneratedApproach:
@@ -218,92 +307,112 @@ class GeneratedApproach:
  218    307          g = state.get
  219    308          self.homes = [np.array([g(r, "x"), g(r, "y")]) for r in sc.rovers]
  220    309          self.home_th = [g(r, "theta") for r in sc.rovers]
  221        -        self.planners = [RoverPlanner(sc, i, self.homes[i]) for i in range(2)]
         310 +        self.bfs = [RoverBFS(sc, i, self.homes[i], home_th=self.home_th[i], other_home=self.homes[1 - i])
         311 +                    for i in range(2)]
  222    312          nobj = len(sc.objectives)
  223        -        tasks = [("obj", k) for k in range(nobj)] + [("stone", 0), ("soil", 0)]
  224        -        self.tasks = tasks
  225        -        costs = []
  226        -        for i in range(2):
  227        -            costs.append(self.planners[i].dp(tasks))
  228        -        # store fields per rover (dp overwrote): re-run later for chosen subset
  229        -        n = len(tasks)
         313 +        n = nobj + 2
  230    314          full = (1 << n) - 1
         315 +        fins = []
         316 +        for i in range(2):
         317 +            B = self.bfs[i]
         318 +            fins.append(B.run(B.hc, 0, wanted=[full], tmax=TMAX, time_budget=12.0))
         319 +        # best finish time for a superset-closed requirement: T_i(req) = min over S ⊇ req
         320 +        def best_for(fin, req):
         321 +            bt = None
         322 +            for S, (t, L) in fin.items():
         323 +                if (S & req) == req and (bt is None or t < bt[0]):
         324 +                    bt = (t, L, S)
         325 +            return bt
  231    326          best = None
  232    327          for s0 in range(1 << n):
  233    328              s1 = full & ~s0
  234        -            c0 = costs[0].get(s0, INF)
  235        -            c1 = costs[1].get(s1, INF)
  236        -            if c0 >= INF or c1 >= INF:
         329 +            b0 = best_for(fins[0], s0) if s0 else (0, None, 0)
         330 +            b1 = best_for(fins[1], s1) if s1 else (0, None, 0)
         331 +            if b0 is None or b1 is None:
  237    332                  continue
  238        -            ops0 = self._ops(tasks, s0)
  239        -            ops1 = self._ops(tasks, s1)
  240        -            k0 = max(c0, ops0) + 0.5 * self._extra(tasks, s0)
  241        -            k1 = max(c1, ops1) + 0.5 * self._extra(tasks, s1)
  242        -            key = (max(k0, k1), k0 + k1)
         333 +            key = (max(b0[0], b1[0]), b0[0] + b1[0])
  243    334              if best is None or key < best[0]:
  244        -                best = (key, s0, s1)
  245        -        self.assign = [best[1], best[2]] if best else [full, 0]
         335 +                best = (key, b0, b1)
  246    336          self.plans = []
         337 +        self.my_req = [0, 0]
         338 +        for i in range(2):
         339 +            b = best[1 + i] if best else None
         340 +            steps = []
         341 +            if b is not None and b[1] is not None:
         342 +                # need layers from the run for rover i: rerun to be safe (layers overwritten? no: per-rover object)
         343 +                steps = self.bfs[i].extract(b[0], b[1]) or []
         344 +                self.my_req[i] = b[2]
         345 +            self.plans.append({"steps": steps, "k": 0, "fail": 0})
         346 +        # refine each rover's plan given the other's trajectory (send line-of-sight)
  247    347          for i in range(2):
  248        -            p = self.planners[i]
  249        -            p.dp(tasks)
  250        -            path, visits = p.extract(self.assign[i])
  251        -            self.plans.append({"path": path, "visits": visits, "k": 0, "wait": 0, "stuck": 0})
  252        -        self.my_tasks = [[tasks[r] for r in range(n) if self.assign[i] & (1 << r)] for i in range(2)]
  253        -        self.last_target = [None, None]
  254        -
  255        -    def _ops(self, tasks, s):
  256        -        c = 0
  257        -        for r, t in enumerate(tasks):
  258        -            if s & (1 << r):
  259        -                c += 2 if t[0] == "obj" else 2
  260        -        return c + 1
  261        -
  262        -    def _extra(self, tasks, s):
  263        -        return 0
         348 +            if not self.plans[i]["steps"]:
         349 +                continue
         350 +            B = self.bfs[i]
         351 +            B.other_traj = self._traj(1 - i)
         352 +            B._send_t_cache = {}
         353 +            req = self.my_req[i]
         354 +            fin = B.run(B.hc, 0, wanted=[req], tmax=TMAX, time_budget=8.0)
         355 +            bt = None
         356 +            for S2, (t, L) in fin.items():
         357 +                if (S2 & req) == req and (bt is None or t < bt[0]):
         358 +                    bt = (t, L)
         359 +            if bt is not None:
         360 +                st = B.extract(bt[0], bt[1])
         361 +                if st and len(st) <= len(self.plans[i]["steps"]):
         362 +                    self.plans[i] = {"steps": st, "k": 0, "fail": 0}
         363 +        self.done_flag = False
         364 +
         365 +    def _traj(self, j):
         366 +        """Positions of rover j at times 0,1,2,... from its current plan pointer."""
         367 +        plan = self.plans[j]
         368 +        B = self.bfs[j]
         369 +        steps = plan["steps"]
         370 +        k = plan["k"]
         371 +        if k > 0 and k <= len(steps):
         372 +            cur = B.pos(steps[k - 1][0])
         373 +        else:
         374 +            cur = self.homes[j]
         375 +        out = [cur]
         376 +        for idx in range(k, len(steps)):
         377 +            out.append(B.pos(steps[idx][0]))
         378 +        return out
  264    379  
  265    380      # ------------------------------------------------------------------
  266        -    def _task_done(self, state, t):
         381 +    def _flags(self, state, i):
  267    382          sc = self.sc
  268    383          g = state.get
  269        -        if t[0] == "obj":
  270        -            o = sc.objectives[t[1]]
  271        -            return g(o, "have_image_rover0") > 0.5 or g(o, "have_image_rover1") > 0.5 or g(o, "received_image") > 0.5
  272        -        want_soil = t[0] == "soil"
         384 +        me = "rover%d" % i
         385 +        S = 0
         386 +        for r, o in enumerate(sc.objectives):
         387 +            if g(o, "have_image_" + me) > 0.5:
         388 +                S |= 1 << r
         389 +        nobj = len(sc.objectives)
  273    390          for s, soil in zip(sc.samples, sc.ssoil):
  274        -            if soil == want_soil and (g(s, "analyzed_rover0") > 0.5 or g(s, "analyzed_rover1") > 0.5
  275        -                                      or g(s, "received_analysis") > 0.5):
  276        -                return True
  277        -        return False
  278        -
  279        -    # ---------------- visibility models ----------------
  280        -    def _pillars(self):
  281        -        return [(b[0], b[1]) for b in self.sc.obs_boxes if max(b[2], b[3]) < 0.15]
  282        -
  283        -    @staticmethod
  284        -    def _seg_dist(p, a, b):
  285        -        ab = b - a
  286        -        t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-12), 0.0, 1.0)
  287        -        return np.linalg.norm(a + t * ab - p)
         391 +            if g(s, "analyzed_" + me) > 0.5:
         392 +                S |= 1 << (nobj + (1 if soil else 0))
         393 +        cal = g(sc.rovers[i], "calibrated") > 0.5
         394 +        store = g(sc.rovers[i], "store_full") > 0.5
         395 +        holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
         396 +            any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
         397 +        return S, cal, store, holding
  288    398  
  289    399      def _visible(self, p, th, k, margin=0.03):
  290    400          c = p + np.array([-0.087 * np.cos(th) + 0.0125 * np.sin(th), -0.087 * np.sin(th) - 0.0125 * np.cos(th)])
  291    401          o = self.sc.opos[k]
  292    402          v = o - c
  293    403          if np.linalg.norm(v) > 1.9972 - margin:
  294        -            return False, np.linalg.norm(v)
         404 +            return False
  295    405          ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
  296    406          if ang < np.radians(108):
  297        -            for pc in self._pillars():
  298        -                if self._seg_dist(np.array(pc), c, o) < 0.11:
  299        -                    return False, np.linalg.norm(v)
  300        -        return True, np.linalg.norm(v)
         407 +            for pc in self.sc.pillars:
         408 +                if _seg_dist(pc, c, o) < 0.11:
         409 +                    return False
         410 +        return True
  301    411  
  302    412      def _can_send(self, state, i, p, th):
  303    413          sc = self.sc
  304    414          v = sc.lpos - p
  305        -        d = np.linalg.norm(v)
  306        -        if d > SEND_R:
         415 +        if np.linalg.norm(v) > SEND_R:
  307    416              return False
  308    417          ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
  309    418          if ang >= np.radians(115):
@@ -311,124 +420,98 @@ class GeneratedApproach:
  311    420          g = state.get
  312    421          orv = sc.rovers[1 - i]
  313    422          op = np.array([g(orv, "x"), g(orv, "y")])
  314        -        if self._seg_dist(op, p, sc.lpos) < 0.27:
         423 +        if _seg_dist(op, p, sc.lpos) < 0.27:
  315    424              return False
  316        -        for pc in self._pillars():
  317        -            if self._seg_dist(np.array(pc), p, sc.lpos) < 0.13:
         425 +        for pc in sc.pillars:
         426 +            if _seg_dist(pc, p, sc.lpos) < 0.13:
  318    427                  return False
  319    428          return True
  320    429  
  321        -    def _choose_op(self, state, i, p, th):
  322        -        sc = self.sc
  323        -        g = state.get
  324        -        rv = sc.rovers[i]
  325        -        me = "rover%d" % i
  326        -        store_full = g(rv, "store_full") > 0.5
  327        -        calibrated = g(rv, "calibrated") > 0.5
  328        -        # sample
  329        -        if not store_full:
  330        -            for s, soil, sp in zip(sc.samples, sc.ssoil, sc.spos):
  331        -                if np.linalg.norm(sp - p) <= SAMP_R:
  332        -                    t = ("soil", 0) if soil else ("stone", 0)
  333        -                    if not self._task_done(state, t):
  334        -                        return "sample"
  335        -        # imaging
  336        -        nobj = len(sc.objectives)
  337        -        vis = {}
  338        -        for k in range(nobj):
  339        -            ok, d = self._visible(p, th, k)
  340        -            if ok:
  341        -                vis[k] = d
  342        -        need = [k for k in range(nobj) if not self._task_done(state, ("obj", k))]
  343        -        if any(k in vis for k in need):
  344        -            if calibrated:
  345        -                cands = [k for k in vis if g(sc.objectives[k], "have_image_" + me) < 0.5]
  346        -                if cands:
  347        -                    kbest = min(cands, key=lambda k: vis[k])
  348        -                    if kbest in need:
  349        -                        return "image"
  350        -            else:
  351        -                return "calibrate"
  352        -        mine_left = [t for t in self.my_tasks[i] if t[0] == "obj" and not self._task_done(state, t)]
  353        -        if not calibrated and mine_left and vis:
  354        -            return "calibrate"
  355        -        if store_full:
  356        -            return "drop"
  357        -        all_done = all(self._task_done(state, t) for t in self.my_tasks[i])
  358        -        holding = False
  359        -        for o in sc.objectives:
  360        -            if g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5:
  361        -                holding = True
  362        -        for s in sc.samples:
  363        -            if g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5:
  364        -                holding = True
  365        -        if holding and self._can_send(state, i, p, th):
  366        -            return "send"
  367        -        return "noop"
  368        -
  369    430      def _los_clear(self, p, q):
  370    431          sc = self.sc
  371    432          if np.linalg.norm(sc.lpos - p) > SEND_R:
  372    433              return False
  373        -        if self._seg_dist(q, p, sc.lpos) < 0.29:
         434 +        if _seg_dist(q, p, sc.lpos) < 0.29:
  374    435              return False
  375        -        for pc in self._pillars():
  376        -            if self._seg_dist(np.array(pc), p, sc.lpos) < 0.14:
         436 +        for pc in sc.pillars:
         437 +            if _seg_dist(pc, p, sc.lpos) < 0.14:
  377    438                  return False
  378    439          return True
  379    440  
  380        -    def _future_los(self, state, i, k):
  381        -        """Will a send facing any direction be possible later on my path (after my last task visit)?"""
  382        -        plan = self.plans[i]
  383        -        path = plan["path"]
  384        -        P = self.planners[i]
  385        -        last = max([idx for idx, ts in plan["visits"].items()
  386        -                    if any(not self._task_done(state, t) for t in ts)] + [k])
  387        -        op = self.plans[1 - i]
  388        -        opath = op["path"]
  389        -        ok0 = op["k"]
  390        -        Po = self.planners[1 - i]
  391        -        for idx in range(last, len(path)):
  392        -            q = Po.pos(opath[min(len(opath) - 1, ok0 + (idx - k))])
  393        -            if self._los_clear(P.pos(path[idx]), q):
  394        -                return True
  395        -        return False
  396        -
  397        -    def _desired_heading(self, state, i, p, k):
  398        -        """Face away from the next objective still to image on my path; else away from lander."""
         441 +    def _other_pos_at(self, i, dt, state):
         442 +        """Predicted position of rover (1-i) dt steps from now."""
         443 +        j = 1 - i
         444 +        plan = self.plans[j]
         445 +        steps = plan["steps"]
         446 +        B = self.bfs[j]
         447 +        if not steps:
         448 +            g = state.get
         449 +            return np.array([g(self.sc.rovers[j], "x"), g(self.sc.rovers[j], "y")])
         450 +        idx = min(len(steps) - 1, plan["k"] + dt - 1)
         451 +        if idx < 0:
         452 +            g = state.get
         453 +            return np.array([g(self.sc.rovers[j], "x"), g(self.sc.rovers[j], "y")])
         454 +        return B.pos(steps[idx][0])
         455 +
         456 +    def _desired_heading(self, state, i, p, th, k, holding):
  399    457          sc = self.sc
  400    458          plan = self.plans[i]
  401        -        visits = plan["visits"]
  402        -        for idx in sorted(visits):
  403        -            if idx < k:
  404        -                continue
  405        -            for t in visits[idx]:
  406        -                if t[0] == "obj" and not self._task_done(state, t):
  407        -                    v = p - sc.opos[t[1]]
         459 +        steps = plan["steps"]
         460 +        B = self.bfs[i]
         461 +        nobj = len(sc.objectives)
         462 +        # next image op in plan: face away from the objective it targets
         463 +        for idx in range(k, len(steps)):
         464 +            c, op, L = steps[idx]
         465 +            if op == IMG:
         466 +                # which objective: bit newly set in L vs previous
         467 +                Lp = steps[idx - 1][2] if idx > 0 else plan.get("L0", 0)
         468 +                newbits = (L & ~Lp) & ((1 << nobj) - 1)
         469 +                if newbits:
         470 +                    r = int(np.log2(newbits & -newbits))
         471 +                    v = B.pos(c) - sc.opos[r]
  408    472                      return np.arctan2(v[1], v[0])
  409        -        # any of my objectives left (e.g. skipped)
  410        -        for t in self.my_tasks[i]:
  411        -            if t[0] == "obj" and not self._task_done(state, t):
  412        -                v = p - sc.opos[t[1]]
  413        -                return np.arctan2(v[1], v[0])
  414        -        # images done: head back to home heading unless stuck at home without having sent
  415        -        g = state.get
  416        -        me = "rover%d" % i
  417        -        holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
  418        -            any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
  419        -        if holding and not self._future_los(state, i, k):
  420        -            v = p - sc.lpos
  421        -            away = np.arctan2(v[1], v[0])
  422        -            th = g(sc.rovers[i], "theta")
  423        -            hth = self.home_th[i]
  424        -            best, bc = None, None
  425        -            for c in np.linspace(-np.radians(60), np.radians(60), 25):
  426        -                h = away + c
  427        -                cost = abs(_wrap(h - th)) + abs(_wrap(hth - h)) + 0.01 * abs(_wrap(h - th))
  428        -                if best is None or cost < best:
  429        -                    best, bc = cost, h
  430        -            return bc
  431        -        return self.home_th[i]
         473 +        hth = self.home_th[i]
         474 +        if holding:
         475 +            # will a send be possible facing home-ish heading later?
         476 +            last = len(steps)
         477 +            ok = False
         478 +            for idx in range(k, last):
         479 +                q = self._other_pos_at(i, idx - k + 1, state)
         480 +                if self._los_clear(B.pos(steps[idx][0]), q):
         481 +                    ok = True
         482 +                    break
         483 +            if not ok and self._los_clear(p, self._other_pos_at(i, 0, state)):
         484 +                ok = True
         485 +            if not ok:
         486 +                v = p - sc.lpos
         487 +                away = np.arctan2(v[1], v[0])
         488 +                best, bc = None, None
         489 +                for c in np.linspace(-np.radians(60), np.radians(60), 25):
         490 +                    h = away + c
         491 +                    cost = abs(_wrap(h - th)) + abs(_wrap(hth - h)) + 0.01 * abs(_wrap(h - th))
         492 +                    if best is None or cost < best:
         493 +                        best, bc = cost, h
         494 +                return bc
         495 +        return hth
         496 +
         497 +    def _replan(self, state, i, cur):
         498 +        B = self.bfs[i]
         499 +        S, cal, store, holding = self._flags(state, i)
         500 +        L0 = S | (B.CALB if cal else 0) | (B.STOREB if store else 0)
         501 +        if not holding and S:
         502 +            L0 |= B.SENTB
         503 +        c = B.cell(cur)
         504 +        B.free[c] = True
         505 +        req = self.my_req[i] | S
         506 +        B.other_traj = self._traj(1 - i)
         507 +        B._send_t_cache = {}
         508 +        fin = B.run(c, L0, wanted=[req], tmax=TMAX, time_budget=5.0)
         509 +        bt = None
         510 +        for S2, (t, L) in fin.items():
         511 +            if (S2 & req) == req and (bt is None or t < bt[0]):
         512 +                bt = (t, L)
         513 +        steps = B.extract(bt[0], bt[1]) if bt else []
         514 +        self.plans[i] = {"steps": steps or [], "k": 0, "fail": 0, "L0": L0}
  432    515  
  433    516      def _rover_action(self, state, i):
  434    517          sc = self.sc
@@ -436,63 +519,69 @@ class GeneratedApproach:
  436    519          rv = sc.rovers[i]
  437    520          cur = np.array([g(rv, "x"), g(rv, "y")])
  438    521          th = g(rv, "theta")
         522 +        B = self.bfs[i]
  439    523          plan = self.plans[i]
  440        -        P = self.planners[i]
         524 +        S, cal, store, holding = self._flags(state, i)
         525 +        steps = plan["steps"]
  441    526          k = plan["k"]
  442        -        exp = P.pos(plan["path"][k])
  443        -        if np.linalg.norm(exp - cur) > 0.02:
  444        -            plan["stuck"] += 1
  445        -            if k > 0 and np.linalg.norm(P.pos(plan["path"][k - 1]) - cur) < 0.02 and plan["stuck"] <= 3:
  446        -                k = k - 1
  447        -                plan["k"] = k
         527 +        # verify previous step outcome
         528 +        if k > 0 and k <= len(steps):
         529 +            c, op, L = steps[k - 1]
         530 +            pos_ok = np.linalg.norm(B.pos(c) - cur) < 0.02
         531 +            Sp = L & ((1 << B.n) - 1)
         532 +            op_ok = True
         533 +            if op in (IMG, SAMP):
         534 +                op_ok = (S & Sp) == Sp
         535 +            elif op == CAL:
         536 +                op_ok = cal
         537 +            elif op == DROP:
         538 +                op_ok = not store
         539 +            if not (pos_ok and op_ok):
         540 +                plan["fail"] += 1
         541 +                Lpre = steps[k - 2][2] if k >= 2 else plan.get("L0", 0)
         542 +                mask = ((1 << B.n) - 1) | B.CALB | B.STOREB
         543 +                Lact = S | (B.CALB if cal else 0) | (B.STOREB if store else 0)
         544 +                changed = (Lact & mask) != (Lpre & mask)
         545 +                if plan["fail"] > 4 or (not pos_ok and plan["fail"] > 2) or (pos_ok and changed):
         546 +                    self._replan(state, i, cur)
         547 +                    plan = self.plans[i]
         548 +                    steps = plan["steps"]
         549 +                    k = 0
         550 +                else:
         551 +                    k = k - 1  # retry the step
  448    552              else:
  449        -                self._replan(state, i, cur)
  450        -                plan = self.plans[i]
  451        -                k = plan["k"]
  452        -        else:
  453        -            plan["stuck"] = 0
  454        -        path = plan["path"]
  455        -        stay = False
  456        -        vt = plan["visits"].get(k, [])
  457        -        for t in vt:
  458        -            if not self._task_done(state, t) and plan["wait"] < 10:
  459        -                stay = True
  460        -        if k >= len(path) - 1:
  461        -            stay = True
  462        -            # path finished but my tasks undone -> replan
  463        -            rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
  464        -            if rem and plan["wait"] >= 10:
  465        -                self._replan(state, i, cur, shrink=True)
  466        -                plan = self.plans[i]
  467        -                path = plan["path"]
  468        -                k = plan["k"]
  469        -                stay = len(path) <= 1
  470        -        if stay:
  471        -            plan["wait"] += 1
  472        -            nxt = k
         553 +                plan["fail"] = 0
         554 +        if k < len(steps):
         555 +            c, op, L = steps[k]
         556 +            target = B.pos(c)
         557 +            plan["k"] = k + 1
  473    558          else:
  474        -            plan["wait"] = 0
  475        -            nxt = k + 1
  476        -        target = P.pos(path[nxt])
         559 +            target = cur if np.linalg.norm(cur - self.homes[i]) < 0.02 else self.homes[i]
         560 +            op = NOOP
         561 +            plan["k"] = len(steps) + 1 if steps else 1
         562 +            # finished plan: if tasks remain undone, replan
         563 +            if (S & self.my_req[i]) != self.my_req[i] or store:
         564 +                self._replan(state, i, cur)
         565 +                return self._rover_action_fresh(state, i)
  477    566          d = np.clip(target - cur, -0.2, 0.2)
  478    567          newp = cur + d
  479        -        dth_des = _wrap(self._desired_heading(state, i, newp, nxt) - th)
  480        -        dth = float(np.clip(dth_des, -0.4, 0.4))
         568 +        dth = float(np.clip(_wrap(self._desired_heading(state, i, newp, th, k + 1, holding) - th), -0.4, 0.4))
  481    569          newth = _wrap(th + dth)
  482        -        op = self._choose_op(state, i, newp, newth)
  483        -        plan["k"] = nxt
         570 +        # op adjustments
         571 +        if op == SEND:
         572 +            op = NOOP
         573 +        if op in (NOOP,) and holding and self._can_send(state, i, newp, newth):
         574 +            op = SEND
         575 +        elif op == NOOP and store and not any(s[1] == SAMP for s in steps[k:]):
         576 +            op = NOOP
  484    577          return np.array([d[0], d[1], dth, BAND[op]], dtype=np.float32)
  485    578  
  486        -    def _replan(self, state, i, cur, shrink=False):
  487        -        P = self.planners[i]
  488        -        if shrink:
  489        -            P.img_r = max(1.6, P.img_r - 0.1)
  490        -        rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
  491        -        start = P.cell(cur)
  492        -        P.free[start] = True
  493        -        costs = P.dp(rem, start=start)
  494        -        path, visits = P.extract((1 << len(rem)) - 1)
  495        -        self.plans[i] = {"path": path, "visits": visits, "k": 0, "wait": 0, "stuck": 0}
         579 +    def _rover_action_fresh(self, state, i):
         580 +        plan = self.plans[i]
         581 +        if not plan["steps"]:
         582 +            return np.array([0, 0, 0, BAND[NOOP]], dtype=np.float32)
         583 +        plan["k"] = 0
         584 +        return self._rover_action(state, i)
  496    585  
  497    586      def get_action(self, state):
  498    587          a0 = self._rover_action(state, 0)
diff --git a/approach_v1.py b/approach_v1.py
new file mode 100644
index 0000000..f4ca772
--- /dev/null
+++ b/approach_v1.py
@@ -0,0 +1,500 @@
           1 +import itertools
           2 +import numpy as np
           3 +
           4 +H = 0.1            # lattice spacing (a step can move up to 2 cells per axis)
           5 +R_STEP = 2         # cells per step
           6 +IMG_R = 2.0        # imaging range from base when facing away (true ~2.08)
           7 +SAMP_R = 0.235     # sampling range (true 0.25)
           8 +SEND_R = 3.85      # send range (true ~4.0)
           9 +BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
          10 +        "send": 0.5, "drop": 5 / 6}
          11 +INF = 1e9
          12 +
          13 +
          14 +def _wrap(a):
          15 +    return (a + np.pi) % (2 * np.pi) - np.pi
          16 +
          17 +
          18 +def _type(space, name):
          19 +    for t in space.types:
          20 +        if t.name == name:
          21 +            return t
          22 +    return None
          23 +
          24 +
          25 +class Scene:
          26 +    def __init__(self, state, space):
          27 +        self.T = {n: _type(space, n) for n in ["rover", "lander", "objective", "sample", "obstacle"]}
          28 +        g = state.get
          29 +        self.rovers = sorted(state.get_objects(self.T["rover"]), key=lambda o: o.name)
          30 +        self.lander = state.get_objects(self.T["lander"])[0]
          31 +        self.objectives = sorted(state.get_objects(self.T["objective"]), key=lambda o: o.name)
          32 +        self.samples = sorted(state.get_objects(self.T["sample"]), key=lambda o: o.name)
          33 +        self.obstacles = state.get_objects(self.T["obstacle"])
          34 +        self.lpos = np.array([g(self.lander, "x"), g(self.lander, "y")])
          35 +        self.obs_boxes = []
          36 +        for o in self.obstacles:
          37 +            self.obs_boxes.append((g(o, "x"), g(o, "y"), g(o, "half_x"), g(o, "half_y"), g(o, "half_z")))
          38 +        self.opos = [np.array([g(o, "x"), g(o, "y")]) for o in self.objectives]
          39 +        self.spos = [np.array([g(o, "x"), g(o, "y")]) for o in self.samples]
          40 +        self.ssoil = [g(o, "is_soil") > 0.5 for o in self.samples]
          41 +
          42 +
          43 +class RoverPlanner:
          44 +    """Lattice anchored at the rover's home; subset DP over task regions."""
          45 +
          46 +    def __init__(self, scene, idx, home):
          47 +        self.scene = scene
          48 +        self.idx = idx
          49 +        self.home = np.array(home, dtype=float)
          50 +        side = 1.0 if home[0] > 0 else -1.0
          51 +        self.side = side
          52 +        self.img_r = IMG_R
          53 +        xs = []
          54 +        x = self.home[0]
          55 +        while x - H >= -2.27:
          56 +            x -= H
          57 +        while x <= 2.27:
          58 +            xs.append(x)
          59 +            x += H
          60 +        ys = []
          61 +        y = self.home[1]
          62 +        while y - H >= -2.27:
          63 +            y -= H
          64 +        while y <= 2.27:
          65 +            ys.append(y)
          66 +            y += H
          67 +        self.xs = np.array(xs)
          68 +        self.ys = np.array(ys)
          69 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
          70 +        self.X, self.Y = X, Y
          71 +        free = (np.abs(X) <= 2.265) & (np.abs(Y) <= 2.265) & (X * side >= 0.235)
          72 +        for (ox, oy, hx, hy, hz) in scene.obs_boxes:
          73 +            margin = 0.21 if max(hx, hy) >= 0.15 else 0.25
          74 +            dx = np.maximum(np.abs(X - ox) - hx, 0.0)
          75 +            dy = np.maximum(np.abs(Y - oy) - hy, 0.0)
          76 +            free &= (dx * dx + dy * dy) >= margin * margin
          77 +        lx, ly = scene.lpos
          78 +        free &= ~((X < lx + 0.71) & (Y < ly + 0.54))
          79 +        self.hi = int(np.argmin(np.abs(self.xs - self.home[0])))
          80 +        self.hj = int(np.argmin(np.abs(self.ys - self.home[1])))
          81 +        free[self.hi, self.hj] = True
          82 +        self.free = free
          83 +        self.shape = free.shape
          84 +        self.offsets = [(a, b) for a in range(-R_STEP, R_STEP + 1) for b in range(-R_STEP, R_STEP + 1)
          85 +                        if (a, b) != (0, 0)]
          86 +
          87 +    def pos(self, c):
          88 +        return np.array([self.xs[c[0]], self.ys[c[1]]])
          89 +
          90 +    def cell(self, p):
          91 +        i = int(np.argmin(np.abs(self.xs - p[0])))
          92 +        j = int(np.argmin(np.abs(self.ys - p[1])))
          93 +        return (i, j)
          94 +
          95 +    def region_mask(self, task):
          96 +        kind, k = task
          97 +        sc = self.scene
          98 +        if kind == "obj":
          99 +            o = sc.opos[k]
         100 +            m = (self.X - o[0]) ** 2 + (self.Y - o[1]) ** 2 <= self.img_r ** 2
         101 +        else:  # 'stone' or 'soil'
         102 +            want_soil = kind == "soil"
         103 +            m = np.zeros(self.shape, bool)
         104 +            for s, soil in zip(sc.spos, sc.ssoil):
         105 +                if soil == want_soil:
         106 +                    m |= (self.X - s[0]) ** 2 + (self.Y - s[1]) ** 2 <= SAMP_R ** 2
         107 +        return m & self.free
         108 +
         109 +    def propagate(self, F):
         110 +        G = F.copy()
         111 +        R = R_STEP
         112 +        W, Hh = self.shape
         113 +        free = self.free
         114 +        while True:
         115 +            P = np.full((W + 2 * R, Hh + 2 * R), INF)
         116 +            P[R:R + W, R:R + Hh] = G
         117 +            best = G.copy()
         118 +            for a, b in self.offsets:
         119 +                np.minimum(best, P[R + a:R + a + W, R + b:R + b + Hh] + 1.0, out=best)
         120 +            best[~free] = INF
         121 +            if np.array_equal(best, G):
         122 +                return G
         123 +            G = best
         124 +
         125 +    def dp(self, tasks, start=None):
         126 +        """Returns dict subset(bitmask)->cost of tour start->tasks->home, and stores fields."""
         127 +        if start is None:
         128 +            start = (self.hi, self.hj)
         129 +        n = len(tasks)
         130 +        masks = [self.region_mask(t) for t in tasks]
         131 +        F0 = np.full(self.shape, INF)
         132 +        F0[start] = 0.0
         133 +        Fs = {0: F0}
         134 +        Gs = {}
         135 +        order = sorted(range(1 << n), key=lambda s: bin(s).count("1"))
         136 +        for s in order:
         137 +            F = Fs.get(s)
         138 +            if F is None:
         139 +                continue
         140 +            G = self.propagate(F)
         141 +            Gs[s] = G
         142 +            for r in range(n):
         143 +                if s & (1 << r):
         144 +                    continue
         145 +                if not masks[r].any():
         146 +                    continue
         147 +                s2 = s | (1 << r)
         148 +                cand = np.where(masks[r], G, INF)
         149 +                if s2 in Fs:
         150 +                    np.minimum(Fs[s2], cand, out=Fs[s2])
         151 +                else:
         152 +                    Fs[s2] = cand
         153 +        self._tasks = tasks
         154 +        self._masks = masks
         155 +        self._Fs = Fs
         156 +        self._Gs = Gs
         157 +        self._start = start
         158 +        costs = {}
         159 +        for s, G in Gs.items():
         160 +            costs[s] = G[self.hi, self.hj]
         161 +        return costs
         162 +
         163 +    def extract(self, s):
         164 +        """Backtrack path for subset s (from last dp). Returns list of cells and visits dict idx->[tasks]."""
         165 +        Gs, Fs, masks = self._Gs, self._Fs, self._masks
         166 +        c = (self.hi, self.hj)
         167 +        v = Gs[s][c]
         168 +        rev = [c]
         169 +        rev_visits = []  # (position in rev, task index)
         170 +        W, Hh = self.shape
         171 +        guard = 0
         172 +        while True:
         173 +            guard += 1
         174 +            if guard > 10000:
         175 +                break
         176 +            if s == 0 and c == self._start:
         177 +                break
         178 +            # try region entry at c
         179 +            moved = False
         180 +            if s != 0 and Fs[s][c] <= v + 1e-9:
         181 +                for r in range(len(masks)):
         182 +                    if s & (1 << r) and masks[r][c]:
         183 +                        s2 = s & ~(1 << r)
         184 +                        if s2 in Gs and Gs[s2][c] <= v + 1e-9:
         185 +                            rev_visits.append((len(rev) - 1, r))
         186 +                            s = s2
         187 +                            moved = True
         188 +                            break
         189 +            if moved:
         190 +                continue
         191 +            for a, b in self.offsets:
         192 +                n = (c[0] + a, c[1] + b)
         193 +                if 0 <= n[0] < W and 0 <= n[1] < Hh and Gs[s][n] <= v - 1 + 1e-9:
         194 +                    c = n
         195 +                    v = Gs[s][n]
         196 +                    rev.append(c)
         197 +                    moved = True
         198 +                    break
         199 +            if not moved:
         200 +                break
         201 +        L = len(rev)
         202 +        path = rev[::-1]
         203 +        visits = {}
         204 +        for (ri, r) in rev_visits:
         205 +            visits.setdefault(L - 1 - ri, []).append(self._tasks[r])
         206 +        return path, visits
         207 +
         208 +
         209 +class GeneratedApproach:
         210 +    def __init__(self, action_space, observation_space, primitives):
         211 +        self.action_space = action_space
         212 +        self.space = observation_space
         213 +
         214 +    # ------------------------------------------------------------------
         215 +    def reset(self, state, info):
         216 +        self.sc = Scene(state, self.space)
         217 +        sc = self.sc
         218 +        g = state.get
         219 +        self.homes = [np.array([g(r, "x"), g(r, "y")]) for r in sc.rovers]
         220 +        self.home_th = [g(r, "theta") for r in sc.rovers]
         221 +        self.planners = [RoverPlanner(sc, i, self.homes[i]) for i in range(2)]
         222 +        nobj = len(sc.objectives)
         223 +        tasks = [("obj", k) for k in range(nobj)] + [("stone", 0), ("soil", 0)]
         224 +        self.tasks = tasks
         225 +        costs = []
         226 +        for i in range(2):
         227 +            costs.append(self.planners[i].dp(tasks))
         228 +        # store fields per rover (dp overwrote): re-run later for chosen subset
         229 +        n = len(tasks)
         230 +        full = (1 << n) - 1
         231 +        best = None
         232 +        for s0 in range(1 << n):
         233 +            s1 = full & ~s0
         234 +            c0 = costs[0].get(s0, INF)
         235 +            c1 = costs[1].get(s1, INF)
         236 +            if c0 >= INF or c1 >= INF:
         237 +                continue
         238 +            ops0 = self._ops(tasks, s0)
         239 +            ops1 = self._ops(tasks, s1)
         240 +            k0 = max(c0, ops0) + 0.5 * self._extra(tasks, s0)
         241 +            k1 = max(c1, ops1) + 0.5 * self._extra(tasks, s1)
         242 +            key = (max(k0, k1), k0 + k1)
         243 +            if best is None or key < best[0]:
         244 +                best = (key, s0, s1)
         245 +        self.assign = [best[1], best[2]] if best else [full, 0]
         246 +        self.plans = []
         247 +        for i in range(2):
         248 +            p = self.planners[i]
         249 +            p.dp(tasks)
         250 +            path, visits = p.extract(self.assign[i])
         251 +            self.plans.append({"path": path, "visits": visits, "k": 0, "wait": 0, "stuck": 0})
         252 +        self.my_tasks = [[tasks[r] for r in range(n) if self.assign[i] & (1 << r)] for i in range(2)]
         253 +        self.last_target = [None, None]
         254 +
         255 +    def _ops(self, tasks, s):
         256 +        c = 0
         257 +        for r, t in enumerate(tasks):
         258 +            if s & (1 << r):
         259 +                c += 2 if t[0] == "obj" else 2
         260 +        return c + 1
         261 +
         262 +    def _extra(self, tasks, s):
         263 +        return 0
         264 +
         265 +    # ------------------------------------------------------------------
         266 +    def _task_done(self, state, t):
         267 +        sc = self.sc
         268 +        g = state.get
         269 +        if t[0] == "obj":
         270 +            o = sc.objectives[t[1]]
         271 +            return g(o, "have_image_rover0") > 0.5 or g(o, "have_image_rover1") > 0.5 or g(o, "received_image") > 0.5
         272 +        want_soil = t[0] == "soil"
         273 +        for s, soil in zip(sc.samples, sc.ssoil):
         274 +            if soil == want_soil and (g(s, "analyzed_rover0") > 0.5 or g(s, "analyzed_rover1") > 0.5
         275 +                                      or g(s, "received_analysis") > 0.5):
         276 +                return True
         277 +        return False
         278 +
         279 +    # ---------------- visibility models ----------------
         280 +    def _pillars(self):
         281 +        return [(b[0], b[1]) for b in self.sc.obs_boxes if max(b[2], b[3]) < 0.15]
         282 +
         283 +    @staticmethod
         284 +    def _seg_dist(p, a, b):
         285 +        ab = b - a
         286 +        t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-12), 0.0, 1.0)
         287 +        return np.linalg.norm(a + t * ab - p)
         288 +
         289 +    def _visible(self, p, th, k, margin=0.03):
         290 +        c = p + np.array([-0.087 * np.cos(th) + 0.0125 * np.sin(th), -0.087 * np.sin(th) - 0.0125 * np.cos(th)])
         291 +        o = self.sc.opos[k]
         292 +        v = o - c
         293 +        if np.linalg.norm(v) > 1.9972 - margin:
         294 +            return False, np.linalg.norm(v)
         295 +        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
         296 +        if ang < np.radians(108):
         297 +            for pc in self._pillars():
         298 +                if self._seg_dist(np.array(pc), c, o) < 0.11:
         299 +                    return False, np.linalg.norm(v)
         300 +        return True, np.linalg.norm(v)
         301 +
         302 +    def _can_send(self, state, i, p, th):
         303 +        sc = self.sc
         304 +        v = sc.lpos - p
         305 +        d = np.linalg.norm(v)
         306 +        if d > SEND_R:
         307 +            return False
         308 +        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
         309 +        if ang >= np.radians(115):
         310 +            return True
         311 +        g = state.get
         312 +        orv = sc.rovers[1 - i]
         313 +        op = np.array([g(orv, "x"), g(orv, "y")])
         314 +        if self._seg_dist(op, p, sc.lpos) < 0.27:
         315 +            return False
         316 +        for pc in self._pillars():
         317 +            if self._seg_dist(np.array(pc), p, sc.lpos) < 0.13:
         318 +                return False
         319 +        return True
         320 +
         321 +    def _choose_op(self, state, i, p, th):
         322 +        sc = self.sc
         323 +        g = state.get
         324 +        rv = sc.rovers[i]
         325 +        me = "rover%d" % i
         326 +        store_full = g(rv, "store_full") > 0.5
         327 +        calibrated = g(rv, "calibrated") > 0.5
         328 +        # sample
         329 +        if not store_full:
         330 +            for s, soil, sp in zip(sc.samples, sc.ssoil, sc.spos):
         331 +                if np.linalg.norm(sp - p) <= SAMP_R:
         332 +                    t = ("soil", 0) if soil else ("stone", 0)
         333 +                    if not self._task_done(state, t):
         334 +                        return "sample"
         335 +        # imaging
         336 +        nobj = len(sc.objectives)
         337 +        vis = {}
         338 +        for k in range(nobj):
         339 +            ok, d = self._visible(p, th, k)
         340 +            if ok:
         341 +                vis[k] = d
         342 +        need = [k for k in range(nobj) if not self._task_done(state, ("obj", k))]
         343 +        if any(k in vis for k in need):
         344 +            if calibrated:
         345 +                cands = [k for k in vis if g(sc.objectives[k], "have_image_" + me) < 0.5]
         346 +                if cands:
         347 +                    kbest = min(cands, key=lambda k: vis[k])
         348 +                    if kbest in need:
         349 +                        return "image"
         350 +            else:
         351 +                return "calibrate"
         352 +        mine_left = [t for t in self.my_tasks[i] if t[0] == "obj" and not self._task_done(state, t)]
         353 +        if not calibrated and mine_left and vis:
         354 +            return "calibrate"
         355 +        if store_full:
         356 +            return "drop"
         357 +        all_done = all(self._task_done(state, t) for t in self.my_tasks[i])
         358 +        holding = False
         359 +        for o in sc.objectives:
         360 +            if g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5:
         361 +                holding = True
         362 +        for s in sc.samples:
         363 +            if g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5:
         364 +                holding = True
         365 +        if holding and self._can_send(state, i, p, th):
         366 +            return "send"
         367 +        return "noop"
         368 +
         369 +    def _los_clear(self, p, q):
         370 +        sc = self.sc
         371 +        if np.linalg.norm(sc.lpos - p) > SEND_R:
         372 +            return False
         373 +        if self._seg_dist(q, p, sc.lpos) < 0.29:
         374 +            return False
         375 +        for pc in self._pillars():
         376 +            if self._seg_dist(np.array(pc), p, sc.lpos) < 0.14:
         377 +                return False
         378 +        return True
         379 +
         380 +    def _future_los(self, state, i, k):
         381 +        """Will a send facing any direction be possible later on my path (after my last task visit)?"""
         382 +        plan = self.plans[i]
         383 +        path = plan["path"]
         384 +        P = self.planners[i]
         385 +        last = max([idx for idx, ts in plan["visits"].items()
         386 +                    if any(not self._task_done(state, t) for t in ts)] + [k])
         387 +        op = self.plans[1 - i]
         388 +        opath = op["path"]
         389 +        ok0 = op["k"]
         390 +        Po = self.planners[1 - i]
         391 +        for idx in range(last, len(path)):
         392 +            q = Po.pos(opath[min(len(opath) - 1, ok0 + (idx - k))])
         393 +            if self._los_clear(P.pos(path[idx]), q):
         394 +                return True
         395 +        return False
         396 +
         397 +    def _desired_heading(self, state, i, p, k):
         398 +        """Face away from the next objective still to image on my path; else away from lander."""
         399 +        sc = self.sc
         400 +        plan = self.plans[i]
         401 +        visits = plan["visits"]
         402 +        for idx in sorted(visits):
         403 +            if idx < k:
         404 +                continue
         405 +            for t in visits[idx]:
         406 +                if t[0] == "obj" and not self._task_done(state, t):
         407 +                    v = p - sc.opos[t[1]]
         408 +                    return np.arctan2(v[1], v[0])
         409 +        # any of my objectives left (e.g. skipped)
         410 +        for t in self.my_tasks[i]:
         411 +            if t[0] == "obj" and not self._task_done(state, t):
         412 +                v = p - sc.opos[t[1]]
         413 +                return np.arctan2(v[1], v[0])
         414 +        # images done: head back to home heading unless stuck at home without having sent
         415 +        g = state.get
         416 +        me = "rover%d" % i
         417 +        holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
         418 +            any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
         419 +        if holding and not self._future_los(state, i, k):
         420 +            v = p - sc.lpos
         421 +            away = np.arctan2(v[1], v[0])
         422 +            th = g(sc.rovers[i], "theta")
         423 +            hth = self.home_th[i]
         424 +            best, bc = None, None
         425 +            for c in np.linspace(-np.radians(60), np.radians(60), 25):
         426 +                h = away + c
         427 +                cost = abs(_wrap(h - th)) + abs(_wrap(hth - h)) + 0.01 * abs(_wrap(h - th))
         428 +                if best is None or cost < best:
         429 +                    best, bc = cost, h
         430 +            return bc
         431 +        return self.home_th[i]
         432 +
         433 +    def _rover_action(self, state, i):
         434 +        sc = self.sc
         435 +        g = state.get
         436 +        rv = sc.rovers[i]
         437 +        cur = np.array([g(rv, "x"), g(rv, "y")])
         438 +        th = g(rv, "theta")
         439 +        plan = self.plans[i]
         440 +        P = self.planners[i]
         441 +        k = plan["k"]
         442 +        exp = P.pos(plan["path"][k])
         443 +        if np.linalg.norm(exp - cur) > 0.02:
         444 +            plan["stuck"] += 1
         445 +            if k > 0 and np.linalg.norm(P.pos(plan["path"][k - 1]) - cur) < 0.02 and plan["stuck"] <= 3:
         446 +                k = k - 1
         447 +                plan["k"] = k
         448 +            else:
         449 +                self._replan(state, i, cur)
         450 +                plan = self.plans[i]
         451 +                k = plan["k"]
         452 +        else:
         453 +            plan["stuck"] = 0
         454 +        path = plan["path"]
         455 +        stay = False
         456 +        vt = plan["visits"].get(k, [])
         457 +        for t in vt:
         458 +            if not self._task_done(state, t) and plan["wait"] < 10:
         459 +                stay = True
         460 +        if k >= len(path) - 1:
         461 +            stay = True
         462 +            # path finished but my tasks undone -> replan
         463 +            rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
         464 +            if rem and plan["wait"] >= 10:
         465 +                self._replan(state, i, cur, shrink=True)
         466 +                plan = self.plans[i]
         467 +                path = plan["path"]
         468 +                k = plan["k"]
         469 +                stay = len(path) <= 1
         470 +        if stay:
         471 +            plan["wait"] += 1
         472 +            nxt = k
         473 +        else:
         474 +            plan["wait"] = 0
         475 +            nxt = k + 1
         476 +        target = P.pos(path[nxt])
         477 +        d = np.clip(target - cur, -0.2, 0.2)
         478 +        newp = cur + d
         479 +        dth_des = _wrap(self._desired_heading(state, i, newp, nxt) - th)
         480 +        dth = float(np.clip(dth_des, -0.4, 0.4))
         481 +        newth = _wrap(th + dth)
         482 +        op = self._choose_op(state, i, newp, newth)
         483 +        plan["k"] = nxt
         484 +        return np.array([d[0], d[1], dth, BAND[op]], dtype=np.float32)
         485 +
         486 +    def _replan(self, state, i, cur, shrink=False):
         487 +        P = self.planners[i]
         488 +        if shrink:
         489 +            P.img_r = max(1.6, P.img_r - 0.1)
         490 +        rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
         491 +        start = P.cell(cur)
         492 +        P.free[start] = True
         493 +        costs = P.dp(rem, start=start)
         494 +        path, visits = P.extract((1 << len(rem)) - 1)
         495 +        self.plans[i] = {"path": path, "visits": visits, "k": 0, "wait": 0, "stuck": 0}
         496 +
         497 +    def get_action(self, state):
         498 +        a0 = self._rover_action(state, 0)
         499 +        a1 = self._rover_action(state, 1)
         500 +        return np.concatenate([a0, a1]).astype(np.float32)
diff --git a/res_approach2_e.json b/res_approach2_e.json
new file mode 100644
index 0000000..a18da89
--- /dev/null
+++ b/res_approach2_e.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 21, "4": 21, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 25, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 22, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 21, "37": 18, "38": 23, "39": 22, "40": 21, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 19}
\ No newline at end of file
```

</details>

<a id="C014"></a>
### C014 · Refinement: penalize original plan when its sends lack LOS

Commit `97c75ea38b8eb8312aed16e10edf91b60f1fc6d4`; parents: 86fe1c7be532017d992ba4365b1aaa941885666d. Recorded author date: 2026-10-01T11:28:58+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0991](01_timeline.md#E0991): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_97c75ea_approach.py) · [Exact all-file diff](evidence/diffs/C014_97c75ea.diff)

[Previous saved controller snapshot](evidence/versions/C013_86fe1c7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fd3529a..89e78ae 100644
--- a/approach.py
+++ b/approach.py
@@ -8,6 +8,7 @@ SEND_R = 3.85      # send range (true ~4.0)
    8      8  TMAX = 120
    9      9  BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
   10     10          "send": 0.5, "drop": 5 / 6}
          11 +SEND_PEN = 3
   11     12  NOOP, CAL, IMG, SAMP, DROP, SEND = "noop", "calibrate", "image", "sample", "drop", "send"
   12     13  
   13     14  
@@ -358,10 +359,29 @@ class GeneratedApproach:
  358    359                      bt = (t, L)
  359    360              if bt is not None:
  360    361                  st = B.extract(bt[0], bt[1])
  361        -                if st and len(st) <= len(self.plans[i]["steps"]):
         362 +                orig = self.plans[i]["steps"]
         363 +                pen = 0 if self._sends_feasible(B, orig) else SEND_PEN
         364 +                if st and len(st) <= len(orig) + pen:
  362    365                      self.plans[i] = {"steps": st, "k": 0, "fail": 0}
  363    366          self.done_flag = False
  364    367  
         368 +    def _sends_feasible(self, B, steps):
         369 +        """Check each planned SEND can happen with LOS given B.other_traj before the next acquisition."""
         370 +        n = len(steps)
         371 +        for j, (c, op, L) in enumerate(steps):
         372 +            if op != SEND:
         373 +                continue
         374 +            ok = False
         375 +            for j2 in range(j, n):
         376 +                if j2 > j and steps[j2][1] in (SAMP, IMG):
         377 +                    break
         378 +                if B.send_mask_t(j2 + 1)[steps[j2][0]]:
         379 +                    ok = True
         380 +                    break
         381 +            if not ok:
         382 +                return False
         383 +        return True
         384 +
  365    385      def _traj(self, j):
  366    386          """Positions of rover j at times 0,1,2,... from its current plan pointer."""
  367    387          plan = self.plans[j]
diff --git a/eval_many.py b/eval_many.py
index 7d79e37..281a105 100644
--- a/eval_many.py
+++ b/eval_many.py
@@ -5,7 +5,7 @@ def run(seed):
    5      5      from env_client import make_env
    6      6      import os, importlib; GeneratedApproach = importlib.import_module(os.environ.get("APP", "approach")).GeneratedApproach
    7      7      env = make_env()
    8        -    obs, info = env.reset(seed=seed)
           8 +    oc = os.environ.get("OC"); obs, info = env.reset(seed=seed, options=({"object_count": int(oc)} if oc else None))
    9      9      ap = GeneratedApproach(env.action_space, env.observation_space, {})
   10     10      t0 = time.time(); ap.reset(obs, info); tp = time.time()-t0
   11     11      pl = [len(p.get('path', p.get('steps', [])))-('path' in p) for p in ap.plans]
diff --git a/res_approach_oc1.json b/res_approach_oc1.json
new file mode 100644
index 0000000..22e6b41
--- /dev/null
+++ b/res_approach_oc1.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 18, "2": 18, "3": 20, "4": 18, "5": 27, "6": 18, "7": 20, "8": 20, "9": 20, "10": 18, "11": 19, "12": 18, "13": 23, "14": 29, "15": 23, "16": 22, "17": 18, "18": 21, "19": 25, "20": 27, "21": 20, "22": 21, "23": 18}
\ No newline at end of file
diff --git a/res_approach_oc2.json b/res_approach_oc2.json
new file mode 100644
index 0000000..44ce8fe
--- /dev/null
+++ b/res_approach_oc2.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 16, "3": 20, "4": 21, "5": 28, "6": 20, "7": 21, "8": 20, "9": 22, "10": 18, "11": 22, "12": 23, "13": 23, "14": 21, "15": 23, "16": 22, "17": 19, "18": 21, "19": 25, "20": 27, "21": 20, "22": 21, "23": 20, "24": 19, "25": 20, "26": 20, "27": 21, "28": 22, "29": 21, "30": 20, "31": 25}
\ No newline at end of file
diff --git a/res_approach_oc3.json b/res_approach_oc3.json
new file mode 100644
index 0000000..8c6b5f2
--- /dev/null
+++ b/res_approach_oc3.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 21, "2": 19, "3": 21, "4": 21, "5": 25, "6": 21, "7": 21, "8": 21, "9": 23, "10": 22, "11": 25, "12": 21, "13": 23, "14": 23, "15": 23, "16": 29, "17": 21, "18": 21, "19": 25, "20": 27, "21": 20, "22": 23, "23": 21, "24": 20, "25": 20, "26": 21, "27": 22, "28": 21, "29": 21, "30": 23, "31": 25}
\ No newline at end of file
diff --git a/res_approach_oc4.json b/res_approach_oc4.json
new file mode 100644
index 0000000..e4b6a4b
--- /dev/null
+++ b/res_approach_oc4.json
@@ -0,0 +1 @@
           1 +{"24": 23, "25": 21, "26": 23, "27": 23, "28": 23, "29": 21, "30": 23, "31": 25, "32": 20, "33": 23, "34": 21, "35": 20, "36": 22, "37": 22, "38": 21, "39": 23, "40": 21, "41": 23, "42": 24, "43": 26, "44": 21, "45": 22, "46": 22, "47": 22, "48": 21, "49": 22, "50": 22, "51": 21, "52": 22, "53": 22, "54": 22, "55": 27}
\ No newline at end of file
diff --git a/res_approach_w.json b/res_approach_w.json
new file mode 100644
index 0000000..14d5601
--- /dev/null
+++ b/res_approach_w.json
@@ -0,0 +1 @@
           1 +{"48": 18, "49": 22, "50": 22, "51": 21, "52": 21, "53": 21, "54": 20, "55": 27, "56": 23, "57": 16, "58": 29, "59": 22, "60": 22, "61": 20, "62": 22, "63": 22, "64": 22, "65": 18, "66": 21, "67": 21, "68": 20, "69": 21, "70": 20, "71": 21, "72": 22, "73": 23, "74": 22, "75": 18, "76": 22, "77": 20, "78": 21, "79": 23, "80": 21, "81": 20, "82": 20, "83": 21, "84": 22, "85": 20, "86": 21, "87": 23, "88": 20, "89": 29, "90": 21, "91": 23, "92": 23, "93": 22, "94": 19, "95": 21, "96": 21, "97": 27, "98": 23, "99": 22, "100": 24, "101": 18, "102": 22, "103": 21, "104": 21, "105": 20, "106": 19, "107": 24, "108": 19, "109": 20, "110": 20, "111": 20, "112": 18, "113": 19, "114": 20, "115": 21, "116": 21, "117": 25, "118": 20, "119": 21, "120": 19, "121": 20, "122": 20, "123": 21, "124": 22, "125": 18, "126": 19, "127": 21, "128": 21, "129": 22, "130": 24, "131": 21, "132": 25, "133": 20, "134": 23, "135": 20, "136": 21, "137": 21, "138": 22, "139": 23, "140": 18, "141": 20, "142": 22, "143": 23, "144": 19, "145": 23, "146": 20, "147": 18, "148": 20, "149": 16, "150": 21, "151": 27, "152": 27, "153": 22, "154": 20, "155": 18, "156": 21, "157": 22, "158": 20, "159": 22}
\ No newline at end of file
```

</details>

<a id="C015"></a>
### C015 · SEND_PEN=0 (penalty hurt)

Commit `5b692fc93b62e56f5e6cd393ffb22a5ff9be0cb4`; parents: 97c75ea38b8eb8312aed16e10edf91b60f1fc6d4. Recorded author date: 2026-10-01T11:30:11+02:00.

File roles (automatic): policy, setup/other.

- [E0995](01_timeline.md#E0995): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_5b692fc_approach.py) · [Exact all-file diff](evidence/diffs/C015_5b692fc.diff)

[Previous saved controller snapshot](evidence/versions/C014_97c75ea_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 89e78ae..17183db 100644
--- a/approach.py
+++ b/approach.py
@@ -8,7 +8,7 @@ SEND_R = 3.85      # send range (true ~4.0)
    8      8  TMAX = 120
    9      9  BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
   10     10          "send": 0.5, "drop": 5 / 6}
   11        -SEND_PEN = 3
          11 +SEND_PEN = 0
   12     12  NOOP, CAL, IMG, SAMP, DROP, SEND = "noop", "calibrate", "image", "sample", "drop", "send"
   13     13  
   14     14  
diff --git a/res_approach_f.json b/res_approach_f.json
new file mode 100644
index 0000000..f397d6f
--- /dev/null
+++ b/res_approach_f.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 21, "4": 21, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 28, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 23, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 21, "37": 18, "38": 23, "39": 22, "40": 23, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 20}
\ No newline at end of file
```

</details>

<a id="C016"></a>
### C016 · Pre-rotate to send cone before planned sample when no LOS predicted

Commit `ece46124314ee79c002785a0e3c6174dce4628cb`; parents: 5b692fc93b62e56f5e6cd393ffb22a5ff9be0cb4. Recorded author date: 2026-10-01T11:30:22+02:00.

File roles (automatic): policy.

- [E1002](01_timeline.md#E1002): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_ece4612_approach.py) · [Exact all-file diff](evidence/diffs/C016_ece4612.diff)

[Previous saved controller snapshot](evidence/versions/C015_5b692fc_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 17183db..1f76749 100644
--- a/approach.py
+++ b/approach.py
@@ -491,19 +491,25 @@ class GeneratedApproach:
  491    491                      v = B.pos(c) - sc.opos[r]
  492    492                      return np.arctan2(v[1], v[0])
  493    493          hth = self.home_th[i]
  494        -        if holding:
         494 +        fs = None
         495 +        if not holding:
         496 +            for idx in range(k, len(steps)):
         497 +                if steps[idx][1] == SAMP:
         498 +                    fs = idx
         499 +                    break
         500 +        if holding or fs is not None:
  495    501              # will a send be possible facing home-ish heading later?
  496    502              last = len(steps)
  497    503              ok = False
  498        -            for idx in range(k, last):
         504 +            for idx in range(k if fs is None else fs, last):
  499    505                  q = self._other_pos_at(i, idx - k + 1, state)
  500    506                  if self._los_clear(B.pos(steps[idx][0]), q):
  501    507                      ok = True
  502    508                      break
  503        -            if not ok and self._los_clear(p, self._other_pos_at(i, 0, state)):
         509 +            if not ok and fs is None and self._los_clear(p, self._other_pos_at(i, 0, state)):
  504    510                  ok = True
  505    511              if not ok:
  506        -                v = p - sc.lpos
         512 +                v = (p if fs is None else B.pos(steps[fs][0])) - sc.lpos
  507    513                  away = np.arctan2(v[1], v[0])
  508    514                  best, bc = None, None
  509    515                  for c in np.linspace(-np.radians(60), np.radians(60), 25):
```

</details>

<a id="C017"></a>
### C017 · Allow finishing at cells within HOME_TOL of home

Commit `5776b80095ee11d7114d7097b3156db114e6c44b`; parents: ece46124314ee79c002785a0e3c6174dce4628cb. Recorded author date: 2026-10-01T11:33:08+02:00.

File roles (automatic): policy, setup/other.

- [E1023](01_timeline.md#E1023): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_5776b80_approach.py) · [Exact all-file diff](evidence/diffs/C017_5776b80.diff)

[Previous saved controller snapshot](evidence/versions/C016_ece4612_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1f76749..854b20a 100644
--- a/approach.py
+++ b/approach.py
@@ -9,6 +9,7 @@ TMAX = 120
    9      9  BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
   10     10          "send": 0.5, "drop": 5 / 6}
   11     11  SEND_PEN = 0
          12 +HOME_TOL = 0.15
   12     13  NOOP, CAL, IMG, SAMP, DROP, SEND = "noop", "calibrate", "image", "sample", "drop", "send"
   13     14  
   14     15  
@@ -81,6 +82,12 @@ class RoverBFS:
   81     82          free &= ~((X < lx + 0.71) & (Y < ly + 0.54))
   82     83          self.hc = (int(np.argmin(np.abs(self.xs - self.home[0]))), int(np.argmin(np.abs(self.ys - self.home[1]))))
   83     84          free[self.hc] = True
          85 +        XX, YY = np.meshgrid(self.xs, self.ys, indexing="ij")
          86 +        dh = np.hypot(XX - self.home[0], YY - self.home[1])
          87 +        self.home_mask = (dh <= HOME_TOL) & free
          88 +        self.home_mask[self.hc] = True
          89 +        self.home_d = dh
          90 +        self.finish_cell = {}
   84     91          self.free = free
   85     92          self.shape = free.shape
   86     93          self.nobj = len(scene.opos)
@@ -238,10 +245,15 @@ class RoverBFS:
  238    245                          new[L2] = M.copy()
  239    246              self.layers.append(new)
  240    247              for L, R in new.items():
  241        -                if (L & self.SENTB) and not (L & self.STOREB) and R[hc]:
         248 +                if (L & self.SENTB) and not (L & self.STOREB):
         249 +                    Rh = R & self.home_mask
         250 +                    if not Rh.any():
         251 +                        continue
  242    252                      S = L & ((1 << self.n) - 1)
  243    253                      if S not in finish:
  244    254                          finish[S] = (t, L)
         255 +                        dd = np.where(Rh, self.home_d, np.inf)
         256 +                        self.finish_cell[(t, L)] = tuple(int(v) for v in np.unravel_index(np.argmin(dd), dd.shape))
  245    257              if wanted is not None and all(any((S & w) == w for S in finish) for w in wanted):
  246    258                  break
  247    259              if time_budget is not None and _t.time() - t_start > time_budget:
@@ -250,7 +262,7 @@ class RoverBFS:
  250    262  
  251    263      def extract(self, T, Lgoal):
  252    264          """Backtrack from (T, Lgoal, home). Returns list of (cell, op) for steps 1..T."""
  253        -        c = self.hc
         265 +        c = self.finish_cell.get((T, Lgoal), self.hc)
  254    266          L = Lgoal
  255    267          steps = []
  256    268          W, Hh = self.shape
diff --git a/res_approach_g.json b/res_approach_g.json
new file mode 100644
index 0000000..a18da89
--- /dev/null
+++ b/res_approach_g.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 21, "4": 21, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 25, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 22, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 21, "37": 18, "38": 23, "39": 22, "40": 21, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 19}
\ No newline at end of file
diff --git a/res_approach_wg.json b/res_approach_wg.json
new file mode 100644
index 0000000..8281f26
--- /dev/null
+++ b/res_approach_wg.json
@@ -0,0 +1 @@
           1 +{"48": 18, "49": 22, "50": 22, "51": 21, "52": 21, "53": 21, "54": 20, "55": 27, "56": 23, "57": 16, "58": 26, "59": 22, "60": 22, "61": 20, "62": 22, "63": 22, "64": 22, "65": 18, "66": 21, "67": 21, "68": 20, "69": 21, "70": 20, "71": 21, "72": 22, "73": 23, "74": 20, "75": 18, "76": 22, "77": 20, "78": 21, "79": 23, "80": 21, "81": 20, "82": 20, "83": 21, "84": 22, "85": 20, "86": 21, "87": 23, "88": 20, "89": 29, "90": 21, "91": 23, "92": 23, "93": 22, "94": 19, "95": 21, "96": 21, "97": 27, "98": 23, "99": 22, "100": 24, "101": 18, "102": 22, "103": 21, "104": 21, "105": 20, "106": 19, "107": 23, "108": 19, "109": 20, "110": 20, "111": 20, "112": 18, "113": 19, "114": 20, "115": 21, "116": 21, "117": 25, "118": 20, "119": 21, "120": 19, "121": 20, "122": 20, "123": 21, "124": 22, "125": 18, "126": 19, "127": 21, "128": 21, "129": 22, "130": 24, "131": 21, "132": 25, "133": 20, "134": 23, "135": 20, "136": 21, "137": 21, "138": 22, "139": 23, "140": 18, "141": 20, "142": 22, "143": 23, "144": 19, "145": 23, "146": 20, "147": 18, "148": 20, "149": 16, "150": 21, "151": 27, "152": 27, "153": 22, "154": 20, "155": 18, "156": 21, "157": 22, "158": 20, "159": 22}
\ No newline at end of file
```

</details>

<a id="C018"></a>
### C018 · HOME_TOL=0 (near-home finish hurt)

Commit `c6089abc4487953a9cb9296c4b28c2fe196f817e`; parents: 5776b80095ee11d7114d7097b3156db114e6c44b. Recorded author date: 2026-10-01T11:33:47+02:00.

File roles (automatic): policy, setup/other.

- [E1030](01_timeline.md#E1030): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_c6089ab_approach.py) · [Exact all-file diff](evidence/diffs/C018_c6089ab.diff)

[Previous saved controller snapshot](evidence/versions/C017_5776b80_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 854b20a..9b0d875 100644
--- a/approach.py
+++ b/approach.py
@@ -9,7 +9,7 @@ TMAX = 120
    9      9  BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
   10     10          "send": 0.5, "drop": 5 / 6}
   11     11  SEND_PEN = 0
   12        -HOME_TOL = 0.15
          12 +HOME_TOL = 0.0
   13     13  NOOP, CAL, IMG, SAMP, DROP, SEND = "noop", "calibrate", "image", "sample", "drop", "send"
   14     14  
   15     15  
diff --git a/res_approach_h.json b/res_approach_h.json
new file mode 100644
index 0000000..202b119
--- /dev/null
+++ b/res_approach_h.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 20, "3": 21, "4": 21, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 25, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 22, "27": 21, "28": 22, "29": 21, "30": 22, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 29, "37": 18, "38": 23, "39": 22, "40": 21, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 19}
\ No newline at end of file
```

</details>

<a id="C019"></a>
### C019 · Global time cap on replanning

Commit `6fb1c9f3794af85443dc3a7c0f9fc9ee8704de6b`; parents: c6089abc4487953a9cb9296c4b28c2fe196f817e. Recorded author date: 2026-10-01T11:34:29+02:00.

File roles (automatic): policy, setup/other.

- [E1039](01_timeline.md#E1039): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_6fb1c9f_approach.py) · [Exact all-file diff](evidence/diffs/C019_6fb1c9f.diff)

[Previous saved controller snapshot](evidence/versions/C018_c6089ab_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9b0d875..05fa21a 100644
--- a/approach.py
+++ b/approach.py
@@ -1,4 +1,5 @@
    1      1  """Rovers: per-rover time-expanded BFS over (cell, done-set, calibrated, store, sent)."""
           2 +import time as _t
    2      3  import numpy as np
    3      4  
    4      5  H = 0.1            # lattice spacing; a step moves up to 2 cells per axis (0.2m)
@@ -315,6 +316,8 @@ class GeneratedApproach:
  315    316  
  316    317      # ------------------------------------------------------------------
  317    318      def reset(self, state, info):
         319 +        self.t_used = 0.0
         320 +        _t0 = _t.time()
  318    321          self.sc = Scene(state, self.space)
  319    322          sc = self.sc
  320    323          g = state.get
@@ -376,6 +379,7 @@ class GeneratedApproach:
  376    379                  if st and len(st) <= len(orig) + pen:
  377    380                      self.plans[i] = {"steps": st, "k": 0, "fail": 0}
  378    381          self.done_flag = False
         382 +        self.t_used = _t.time() - _t0
  379    383  
  380    384      def _sends_feasible(self, B, steps):
  381    385          """Check each planned SEND can happen with LOS given B.other_traj before the next acquisition."""
@@ -543,7 +547,10 @@ class GeneratedApproach:
  543    547          req = self.my_req[i] | S
  544    548          B.other_traj = self._traj(1 - i)
  545    549          B._send_t_cache = {}
  546        -        fin = B.run(c, L0, wanted=[req], tmax=TMAX, time_budget=5.0)
         550 +        t0 = _t.time()
         551 +        budget = min(5.0, max(0.3, 35.0 - self.t_used))
         552 +        fin = B.run(c, L0, wanted=[req], tmax=TMAX, time_budget=budget)
         553 +        self.t_used += _t.time() - t0
  547    554          bt = None
  548    555          for S2, (t, L) in fin.items():
  549    556              if (S2 & req) == req and (bt is None or t < bt[0]):
diff --git a/res_approach_i.json b/res_approach_i.json
new file mode 100644
index 0000000..a18da89
--- /dev/null
+++ b/res_approach_i.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 21, "4": 21, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 25, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 22, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 21, "37": 18, "38": 23, "39": 22, "40": 21, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 19}
\ No newline at end of file
```

</details>

<a id="C020"></a>
### C020 · Tighter reset time budgets

Commit `cf0ca467430d9248c01f08d1df9615be87686d0c`; parents: 6fb1c9f3794af85443dc3a7c0f9fc9ee8704de6b. Recorded author date: 2026-10-01T11:35:17+02:00.

File roles (automatic): policy, setup/other.

- [E1042](01_timeline.md#E1042): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_cf0ca46_approach.py) · [Exact all-file diff](evidence/diffs/C020_cf0ca46.diff)

[Previous saved controller snapshot](evidence/versions/C019_6fb1c9f_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 05fa21a..3d41261 100644
--- a/approach.py
+++ b/approach.py
@@ -331,7 +331,7 @@ class GeneratedApproach:
  331    331          fins = []
  332    332          for i in range(2):
  333    333              B = self.bfs[i]
  334        -            fins.append(B.run(B.hc, 0, wanted=[full], tmax=TMAX, time_budget=12.0))
         334 +            fins.append(B.run(B.hc, 0, wanted=[full], tmax=TMAX, time_budget=10.0))
  335    335          # best finish time for a superset-closed requirement: T_i(req) = min over S ⊇ req
  336    336          def best_for(fin, req):
  337    337              bt = None
@@ -367,7 +367,7 @@ class GeneratedApproach:
  367    367              B.other_traj = self._traj(1 - i)
  368    368              B._send_t_cache = {}
  369    369              req = self.my_req[i]
  370        -            fin = B.run(B.hc, 0, wanted=[req], tmax=TMAX, time_budget=8.0)
         370 +            fin = B.run(B.hc, 0, wanted=[req], tmax=TMAX, time_budget=5.0)
  371    371              bt = None
  372    372              for S2, (t, L) in fin.items():
  373    373                  if (S2 & req) == req and (bt is None or t < bt[0]):
diff --git a/res_approach_j.json b/res_approach_j.json
new file mode 100644
index 0000000..a18da89
--- /dev/null
+++ b/res_approach_j.json
@@ -0,0 +1 @@
           1 +{"0": 25, "1": 20, "2": 19, "3": 21, "4": 21, "5": 25, "6": 20, "7": 21, "8": 21, "9": 22, "10": 22, "11": 19, "12": 23, "13": 23, "14": 29, "15": 23, "16": 22, "17": 21, "18": 21, "19": 25, "20": 27, "21": 20, "22": 23, "23": 18, "24": 19, "25": 20, "26": 21, "27": 21, "28": 22, "29": 21, "30": 22, "31": 25, "32": 20, "33": 23, "34": 19, "35": 18, "36": 21, "37": 18, "38": 23, "39": 22, "40": 21, "41": 19, "42": 22, "43": 25, "44": 20, "45": 21, "46": 20, "47": 19}
\ No newline at end of file
```

</details>

<a id="C021"></a>
### C021 · test script update

Commit `4b16eec721cc1a3f9b5aa3106c02e635e07873f9`; parents: cf0ca467430d9248c01f08d1df9615be87686d0c. Recorded author date: 2026-10-01T11:35:42+02:00.

File roles (automatic): diagnostic/test.

- [E1055](01_timeline.md#E1055): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C021_4b16eec.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index 3d83868..7ec792f 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -17,6 +17,6 @@ for seed in seeds:
   17     17          steps += 1
   18     18          if term or trunc: break
   19     19      nobj = len(ap.sc.objectives)
   20        -    print(f"seed {seed} nobj {nobj} steps {steps} term {term} plan {tp:.2f}s assign {ap.assign} pathlens {[len(p['path'])-1 for p in ap.plans]}", flush=True)
          20 +    print(f"seed {seed} nobj {nobj} steps {steps} term {term} plan {tp:.2f}s", flush=True)
   21     21      res.append(steps if term else 9999)
   22     22  print("mean", np.mean(res), "fails", sum(r == 9999 for r in res))
```

</details>

<a id="C022"></a>
### C022 · eval results

Commit `a010326ad1d8164ef0eea61ce7410b6d82c804e1`; parents: 4b16eec721cc1a3f9b5aa3106c02e635e07873f9. Recorded author date: 2026-10-01T11:37:27+02:00.

File roles (automatic): setup/other.

- [E1060](01_timeline.md#E1060): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C022_a010326.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res_approach_oc4b.json b/res_approach_oc4b.json
new file mode 100644
index 0000000..de0be87
--- /dev/null
+++ b/res_approach_oc4b.json
@@ -0,0 +1 @@
           1 +{"100": 24, "101": 21, "102": 24, "103": 23, "104": 21, "105": 24, "106": 21, "107": 21, "108": 25, "109": 22, "110": 31, "111": 21, "112": 20, "113": 21, "114": 20, "115": 22, "116": 21, "117": 20, "118": 22, "119": 22, "120": 22, "121": 22, "122": 20, "123": 23, "124": 22, "125": 21, "126": 22, "127": 23, "128": 21, "129": 22, "130": 24, "131": 25, "132": 25, "133": 21, "134": 22, "135": 23, "136": 21, "137": 21, "138": 23, "139": 23, "140": 20, "141": 22, "142": 22, "143": 23, "144": 21, "145": 22, "146": 22, "147": 22, "148": 24, "149": 22, "150": 21, "151": 24, "152": 27, "153": 22, "154": 23, "155": 22, "156": 23, "157": 22, "158": 22, "159": 22, "160": 20, "161": 21, "162": 22, "163": 21, "164": 27, "165": 22, "166": 21, "167": 20, "168": 23, "169": 31, "170": 22, "171": 23, "172": 22, "173": 33, "174": 23, "175": 24, "176": 23, "177": 21, "178": 22, "179": 23}
\ No newline at end of file
```

</details>

