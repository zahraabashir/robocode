# Obstruction3D · claude-opus-5-5 · replicate 42: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `7142efa` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `c8036df` | Calibrated Kinova FK (mount offset, tool offset), IK, probe scripts | calib1.py, calib2.py, calib3.py, calib4.py, calib5.py, calib6.py, calib_data.json, e_n0.txt, e_n1.txt, e_x0.txt, e_x1.txt, e_y0.txt, e_y1.txt, fit.py, g_0.25.txt, g_0.25_0.785.txt… | [E0159](01_timeline.md#E0159) |
| [C003](#C003) · `f57fd55` | First full approach: clear obstructions then place block | approach.py, gm_-0.02.txt, gm_-0.04.txt, gm_0.0.txt, gm_0.02.txt, grasp_map.py, release2.py, release_test.py, test_approach.py, th.py, zs1.txt, zs2.txt, zs3.txt, zs4.txt, zs5.txt,… | [E0229](01_timeline.md#E0229) |
| [C004](#C004) · `e721694` | Yaw selection avoiding neighbors, grasp retry | approach.py, dbg.py, ptest.py | [E0247](01_timeline.md#E0247) |
| [C005](#C005) · `47df3f3` | Axis-aligned yaw choice, step halving on block | approach.py, dbg2.py | [E0283](01_timeline.md#E0283) |
| [C006](#C006) · `e143b4c` | Dynamic safe height, larger waypoint steps; incremental test runner | approach.py, r_def.txt, r_oc5.txt, r_oc8.txt, test_approach.py | [E0415](01_timeline.md#E0415), [E0418](01_timeline.md#E0418) |
| [C007](#C007) · `105ef1d` | incremental test runner | ptest.py | [E0415](01_timeline.md#E0415), [E0418](01_timeline.md#E0418), [E0431](01_timeline.md#E0431), [E0446](01_timeline.md#E0446) |
| [C008](#C008) · `65e3006` | Yaw: minimize rotation from current tool yaw, keep yaw at place | approach.py, dbg3.py, r_def.txt | [E0469](01_timeline.md#E0469) |
| [C009](#C009) · `df3b962` | Finger-footprint collision model, 15deg yaw options, blocker-first ordering, better free spot | approach.py, d204.txt, geo_0_0.txt, geo_0_1.txt, geo_1.5708_0.txt, geo_1.5708_1.txt, gripgeo.py, r_def.txt, r_oc5.txt, th.py | [E0590](01_timeline.md#E0590) |
| [C010](#C010) · `d6f9c28` | Blocked recovery: straight cartesian small steps instead of scaling joint deltas | approach.py, d215.txt, probe215.py, probe215b.py | [E0644](01_timeline.md#E0644) |
| [C011](#C011) · `0205421` | Tilt tool toward mount for targets near the arm base | approach.py, d312.txt, dbg3.py, reach.py, tilt.py, tilt2.py, tilt3.py | [E0738](01_timeline.md#E0738) |
| [C012](#C012) · `cd05160` | Allow moving target block out of the way as blocker | approach.py, d312.txt, d408.txt, d431.txt, sweep1.txt | [E0828](01_timeline.md#E0828) |
| [C013](#C013) · `1763b8a` | Combine close/open with final motion step; drop retreat phase | approach.py, combo.py, d3.txt, d431.txt, d478.txt, probe478.py, probe478b.py, sweep2.txt, touch.py | [E0955](01_timeline.md#E0955) |
| [C014](#C014) · `d3ee669` | Obstacle-aware routing (diagonal when clear, minimal lift height) | approach.py, sweep3.txt | [E0993](01_timeline.md#E0993) |
| [C015](#C015) · `f985a91` | Tighter intermediate waypoint tolerance to avoid corner cutting | approach.py, d55.txt, p55.py, sweep3.txt | [E1068](01_timeline.md#E1068) |
| [C016](#C016) · `1a3898c` | Tight tolerance only at route corners | approach.py, sweep4.txt | [E1105](01_timeline.md#E1105) |
| [C017](#C017) · `b4a45de` | Pursuit tracking: farthest reachable point along path per step; skip needless vertical exit | approach.py, sweep5.txt | [E1142](01_timeline.md#E1142) |
| [C018](#C018) · `4e8d1b7` | Free spot: penalize travel incl. to target block | approach.py, sweep6.txt | [E1187](01_timeline.md#E1187) |
| [C019](#C019) · `e4e82e8` | Revert free-spot travel weighting (worse mean steps) | approach.py, sweep7.txt | [E1194](01_timeline.md#E1194) |
| [C020](#C020) · `e54126c` | Add sweep results (default 1000-1100: 100/100, 23.2 steps; OC=8: 40/40) | sweep8.txt | [E1247](01_timeline.md#E1247) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `7142efadf2a895128d03b19b6786f6355b927f72`; parents: none (initial snapshot). Recorded author date: 2026-09-28T19:18:34+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_7142efa.diff)

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
index 0000000..25ecad4
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "e0842a41959273c4fbf2530724d35592", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Calibrated Kinova FK (mount offset, tool offset), IK, probe scripts

Commit `c8036df9077f72c4644964fbd7a3fbc0b330fb39`; parents: 7142efadf2a895128d03b19b6786f6355b927f72. Recorded author date: 2026-09-28T19:29:08+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0159](01_timeline.md#E0159): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C002_c8036df.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/calib1.py b/calib1.py
new file mode 100644
index 0000000..ed38796
--- /dev/null
+++ b/calib1.py
@@ -0,0 +1,40 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +np.set_printoptions(precision=4,suppress=True)
           5 +env = make_env()
           6 +seed=int(sys.argv[1]); YAW=float(sys.argv[2])
           7 +obs, info = env.reset(seed=seed)
           8 +R = obs.get_object_from_name('robot')
           9 +tb = obs.get_object_from_name('target_block')
          10 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
          11 +def base_of(o): return (o.get(R,'pos_base_x'),o.get(R,'pos_base_y'),o.get(R,'pos_base_rot'))
          12 +def goto(qt, grip=0.0, maxsteps=40):
          13 +    global obs
          14 +    for _ in range(maxsteps):
          15 +        q = q_of(obs); d = qt-q
          16 +        d = (d+np.pi)%(2*np.pi)-np.pi
          17 +        if np.max(np.abs(d))<1e-4: return True
          18 +        a = np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=grip
          19 +        obs2,r,te,tr,_ = env.step(a)
          20 +        if np.allclose(q_of(obs2), q): obs=obs2; return False
          21 +        obs=obs2
          22 +    return False
          23 +bx,by,bz = [obs.get(tb,f) for f in ("pose_x","pose_y","pose_z")]
          24 +if len(sys.argv)>3: bx,by=float(sys.argv[3]),float(sys.argv[4])
          25 +print('block', bx,by,bz, [obs.get(tb,f'half_extent_{c}') for c in 'xyz'])
          26 +q = q_of(obs)
          27 +for z in np.arange(0.40, 0.05, -0.01):
          28 +    qt,e = ik(base_of(obs), q_of(obs), np.array([bx,by,z]), down_R(YAW))
          29 +    ok = goto(qt)
          30 +    M = fk(base_of(obs), q_of(obs))
          31 +    a = np.zeros(11,dtype=np.float32); a[10]=-1
          32 +    obs,*_ = env.step(a)
          33 +    g = obs.get(R,'grasp_active'); fs=obs.get(R,'finger_state')
          34 +    print(f'z={z:.3f} reached={ok} ee={M[:3,3]} grasp={g} finger={fs}')
          35 +    if g>0.5:
          36 +        print('grasp_tf', [obs.get(R,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
          37 +        print('block now', [obs.get(tb,f) for f in ('pose_x','pose_y','pose_z','grasp_active')])
          38 +        break
          39 +    a[10]=1; obs,*_ = env.step(a)
          40 +    if not ok: print('blocked', q_of(obs), qt); break
diff --git a/calib2.py b/calib2.py
new file mode 100644
index 0000000..8b5ec2e
--- /dev/null
+++ b/calib2.py
@@ -0,0 +1,26 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +np.set_printoptions(precision=4,suppress=True)
           5 +env = make_env()
           6 +pts = [tuple(map(float,p.split(','))) for p in sys.argv[2:]]
           7 +seed=int(sys.argv[1]); YAW=float(__import__("os").environ.get("YAW","0"))
           8 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           9 +def base_of(o): return (o.get(R,'pos_base_x'),o.get(R,'pos_base_y'),o.get(R,'pos_base_rot'))
          10 +for (x,y) in pts:
          11 +    obs, info = env.reset(seed=seed)
          12 +    R = obs.get_object_from_name('robot')
          13 +    last=None
          14 +    for z in np.arange(0.30, 0.0, -0.005):
          15 +        qt,e = ik(base_of(obs), q_of(obs), np.array([x,y,z]), down_R(YAW))
          16 +        ok=True
          17 +        for _ in range(30):
          18 +            q=q_of(obs); d=qt-q
          19 +            if np.max(np.abs(d))<1e-4: break
          20 +            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          21 +            obs2,*_=env.step(a)
          22 +            if np.allclose(q_of(obs2),q): ok=False; break
          23 +            obs=obs2
          24 +        if not ok: break
          25 +        last=z
          26 +    print(f'({x},{y}) lowest reached ee z={last:.3f}, e={e:.1e}')
diff --git a/calib3.py b/calib3.py
new file mode 100644
index 0000000..666dc5a
--- /dev/null
+++ b/calib3.py
@@ -0,0 +1,28 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +np.set_printoptions(precision=4,suppress=True)
           5 +env = make_env()
           6 +seed=int(sys.argv[1]); z=float(sys.argv[2]); yaw=float(sys.argv[3])
           7 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           8 +def base_of(o): return (o.get(R,'pos_base_x'),o.get(R,'pos_base_y'),o.get(R,'pos_base_rot'))
           9 +obs, info = env.reset(seed=seed)
          10 +R = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
          11 +bx,by = obs.get(tb,'pose_x'),obs.get(tb,'pose_y')
          12 +offs=[-0.08,-0.04,0,0.04,0.08]
          13 +for dx in offs:
          14 +  for dy in offs:
          15 +    qt,e = ik(base_of(obs), q_of(obs), np.array([bx+dx,by+dy,z]), down_R(yaw))
          16 +    ok=True
          17 +    for _ in range(30):
          18 +        q=q_of(obs); d=qt-q
          19 +        if np.max(np.abs(d))<1e-4: break
          20 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          21 +        obs2,*_=env.step(a)
          22 +        if np.allclose(q_of(obs2),q): ok=False; break
          23 +        obs=obs2
          24 +    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          25 +    g=obs.get(R,'grasp_active')
          26 +    print(dx,dy,ok,g, [round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']] if g else '')
          27 +    if g: sys.exit()
          28 +    a[10]=1; obs,*_=env.step(a)
diff --git a/calib4.py b/calib4.py
new file mode 100644
index 0000000..f8e83fa
--- /dev/null
+++ b/calib4.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys
           4 +np.set_printoptions(precision=4,suppress=True)
           5 +env = make_env()
           6 +seed=int(sys.argv[1]); z=float(sys.argv[2]); yaw=float(sys.argv[3]); dx=float(sys.argv[4]); dy=float(sys.argv[5])
           7 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           8 +def base_of(o): return (o.get(R,'pos_base_x'),o.get(R,'pos_base_y'),o.get(R,'pos_base_rot'))
           9 +obs, info = env.reset(seed=seed)
          10 +R = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
          11 +bx,by = obs.get(tb,'pose_x'),obs.get(tb,'pose_y')
          12 +qt,e = ik(base_of(obs), q_of(obs), np.array([bx+dx,by+dy,z]), down_R(yaw))
          13 +for _ in range(30):
          14 +    q=q_of(obs); d=qt-q
          15 +    if np.max(np.abs(d))<1e-4: break
          16 +    a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          17 +    obs2,*_=env.step(a)
          18 +    if np.allclose(q_of(obs2),q): print('blocked'); break
          19 +    obs=obs2
          20 +for i in range(8):
          21 +    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          22 +    print(i, obs.get(R,'grasp_active'), obs.get(R,'finger_state'), obs.get(tb,'grasp_active'))
diff --git a/calib5.py b/calib5.py
new file mode 100644
index 0000000..f1f9235
--- /dev/null
+++ b/calib5.py
@@ -0,0 +1,27 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys, time
           4 +env = make_env()
           5 +seed=int(sys.argv[1]); z=float(sys.argv[2]); yaw=float(sys.argv[3])
           6 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           7 +def base_of(o): return (o.get(R,'pos_base_x'),o.get(R,'pos_base_y'),o.get(R,'pos_base_rot'))
           8 +obs, info = env.reset(seed=seed)
           9 +R = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
          10 +bx,by = obs.get(tb,"pose_x")-float(__import__("os").environ.get("DX","0")),obs.get(tb,"pose_y")
          11 +offs=np.arange(-0.06,0.061,0.02); t0=time.time(); n=0
          12 +for dx in offs:
          13 +  for dy in offs:
          14 +    qt,e = ik(base_of(obs), q_of(obs), np.array([bx+dx,by+dy,z]), down_R(yaw))
          15 +    for _ in range(30):
          16 +        q=q_of(obs); d=qt-q
          17 +        if np.max(np.abs(d))<1e-4: break
          18 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          19 +        obs2,*_=env.step(a); n+=1
          20 +        if np.allclose(q_of(obs2),q): break
          21 +        obs=obs2
          22 +    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          23 +    g=obs.get(R,'grasp_active')
          24 +    if g:
          25 +        print('GRASP', z, dx,dy, [round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']]); sys.exit()
          26 +    a[10]=1; obs,*_=env.step(a)
          27 +print('none at z',z, 'steps',n,'time',time.time()-t0)
diff --git a/calib6.py b/calib6.py
new file mode 100644
index 0000000..a86be30
--- /dev/null
+++ b/calib6.py
@@ -0,0 +1,32 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np, sys, json
           4 +env = make_env()
           5 +def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
           6 +def base_of(o): return (o.get(R,'pos_base_x'),o.get(R,'pos_base_y'),o.get(R,'pos_base_rot'))
           7 +obs, info = env.reset(seed=1)
           8 +R = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
           9 +bx,by = obs.get(tb,"pose_x")-0.1-0.02, obs.get(tb,"pose_y")-0.04
          10 +qt,e = ik(base_of(obs), q_of(obs), np.array([bx,by,0.25]), down_R(0))
          11 +for _ in range(30):
          12 +    q=q_of(obs); d=qt-q
          13 +    if np.max(np.abs(d))<1e-4: break
          14 +    a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); obs,*_=env.step(a)
          15 +a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          16 +assert obs.get(R,'grasp_active')>0.5
          17 +GF=['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']
          18 +BF=['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']
          19 +data=[]
          20 +rng=np.random.default_rng(0)
          21 +def rec():
          22 +    data.append(dict(base=list(base_of(obs)), q=q_of(obs).tolist(), blk=[obs.get(tb,f) for f in BF], gtf=[obs.get(R,f) for f in GF]))
          23 +rec()
          24 +# lift first
          25 +a=np.zeros(11,dtype=np.float32); a[4]=-0.15; obs,*_=env.step(a); rec()
          26 +for i in range(80):
          27 +    a=np.zeros(11,dtype=np.float32); a[2:10]=rng.uniform(-0.2,0.2,8)
          28 +    if i%3==0: a[2]=0
          29 +    q0=q_of(obs); obs,*_=env.step(a)
          30 +    if not np.allclose(q_of(obs),q0): rec()
          31 +print(len(data), 'grasp still', obs.get(R,'grasp_active'))
          32 +json.dump(data, open('calib_data.json','w'))
diff --git a/calib_data.json b/calib_data.json
new file mode 100644
index 0000000..93b4f45
--- /dev/null
+++ b/calib_data.json
@@ -0,0 +1 @@
           1 +[{"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.5255274176597595, 0.12704649567604065, -3.4360482692718506, -2.598949909210205, 0.12100589275360107, -0.2879761755466461, 2.2125749588012695], "blk": [0.13774842023849487, 0.18313223123550415, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.5255274176597595, -0.02295350842177868, -3.4360482692718506, -2.598949909210205, 0.12100589275360107, -0.2879761755466461, 2.2125749588012695], "blk": [0.1589166671037674, 0.19540783762931824, 0.13356612622737885, 0.03758993744850159, -0.06481865048408508, -7.508942303502408e-07, 0.9971888065338135], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.6176127195358276, -0.20656409859657288, -3.629437208175659, -2.473641872406006, 0.286108136177063, -0.2453218549489975, 2.3043735027313232], "blk": [0.15048104524612427, 0.30336883664131165, 0.22750474512577057, 0.11225103586912155, -0.2333471029996872, 0.25019511580467224, 0.9329261779785156], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.0174499973654747], "q": [-0.44358378648757935, -0.08022268116474152, -3.8283417224884033, -2.3306801319122314, 0.09954234957695007, -0.15345968306064606, 2.174635648727417], "blk": [0.15153735876083374, 0.39824017882347107, 0.2659831941127777, 0.2284015268087387, -0.17864108085632324, 0.13738799095153809, 0.9471244215965271], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.16272157430648804], "q": [-0.4269993007183075, -0.1603379249572754, -3.859266757965088, -2.519352436065674, -0.05074433609843254, -0.0852099061012268, 2.233511447906494], "blk": [0.06949249655008316, 0.3704335689544678, 0.22106796503067017, 0.21649561822414398, -0.14734703302383423, 0.1812984049320221, 0.9479184746742249], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.16272157430648804], "q": [-0.47352826595306396, 0.03854605555534363, -3.6669325828552246, -2.4451355934143066, 0.009439373388886452, -0.009831213392317295, 2.189079999923706], "blk": [0.13153724372386932, 0.4011688232421875, 0.21084527671337128, 0.23096726834774017, -0.11309836804866791, 0.10508609563112259, 0.9606351256370544], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.016760163009166718], "q": [-0.3849329352378845, 0.04868778586387634, -3.7428359985351562, -2.450801372528076, 0.1652345061302185, 0.16378618776798248, 2.1321980953216553], "blk": [0.20106223225593567, 0.39045000076293945, 0.24259208142757416, 0.2806692123413086, -0.17960591614246368, 0.07536827027797699, 0.9398330450057983], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.045372094959020615], "q": [-0.45618516206741333, 0.08640780299901962, -3.807671546936035, -2.4941537380218506, 0.3213442265987396, 0.0546492338180542, 2.1814730167388916], "blk": [0.11151652038097382, 0.3738318383693695, 0.18781086802482605, 0.2069692313671112, -0.136052668094635, 0.2449941635131836, 0.9373533129692078], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.045372094959020615], "q": [-0.32312750816345215, 0.20124712586402893, -3.91192364692688, -2.343560218811035, 0.14477145671844482, -0.010903940536081791, 2.0415847301483154], "blk": [0.1531260460615158, 0.42274922132492065, 0.2077634483575821, 0.25411543250083923, -0.062168046832084656, 0.06837525963783264, 0.9627488255500793], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.025507841259241104], "q": [-0.2045978158712387, 0.09350401163101196, -4.0911149978637695, -2.381739377975464, 0.024176666513085365, -0.1746027171611786, 2.0737178325653076], "blk": [0.11667171120643616, 0.376663476228714, 0.19941769540309906, 0.19911709427833557, -0.044165484607219696, 0.060790542513132095, 0.9770907163619995], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.05501370504498482], "q": [-0.1357998549938202, -0.026689816266298294, -3.9142699241638184, -2.4356954097747803, -0.13362520933151245, -0.12295945733785629, 2.244579553604126], "blk": [0.22668980062007904, 0.3036220073699951, 0.21373270452022552, 0.1949520856142044, -0.12821780145168304, -0.07665324211120605, 0.9693700075149536], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.05501370504498482], "q": [0.04603634402155876, -0.02673148922622204, -3.944178581237793, -2.3876099586486816, 0.0644133910536766, 0.056618012487888336, 2.228597640991211], "blk": [0.3165763020515442, 0.3036210536956787, 0.2693061828613281, 0.2333315908908844, -0.2475232183933258, -0.06469753384590149, 0.938137948513031], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.04807783290743828], "q": [0.045005422085523605, -0.015006626024842262, -3.829864263534546, -2.4217476844787598, 0.15820682048797607, 0.14107516407966614, 2.401421546936035], "blk": [0.3135802447795868, 0.3164406418800354, 0.2657434344291687, 0.20727293193340302, -0.2964926064014435, 0.05021647363901138, 0.9309180378913879], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.10594910383224487], "q": [0.1366114616394043, 0.15596294403076172, -3.6426937580108643, -2.6158649921417236, 0.30366286635398865, 0.33355316519737244, 2.58430552482605], "blk": [0.3384374678134918, 0.14718097448349, 0.17127177119255066, 0.12086747586727142, -0.2707084119319916, -0.011493791826069355, 0.9549742937088013], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.10594910383224487], "q": [0.3256630003452301, 0.3119371831417084, -3.5137441158294678, -2.6238698959350586, 0.19661203026771545, 0.45430541038513184, 2.7537176609039307], "blk": [0.3790774345397949, 0.031687621027231216, 0.13637587428092957, 0.07478104531764984, -0.27318060398101807, -0.1490209400653839, 0.9474032521247864], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.19949699938297272], "q": [0.34123674035072327, 0.2890383005142212, -3.341337203979492, -2.6600000858306885, 0.28941449522972107, 0.5000547170639038, 2.565063714981079], "blk": [0.37054136395454407, -0.07358380407094955, 0.13799019157886505, 0.05527026578783989, -0.2787567377090454, -0.30787405371665955, 0.9079942107200623], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.11180908977985382], "q": [0.14763344824314117, 0.3922187089920044, -3.3362338542938232, -2.48835825920105, 0.11584750562906265, 0.6365815997123718, 2.391739845275879], "blk": [0.4894454777240753, 0.006568688899278641, 0.18136294186115265, 0.15794871747493744, -0.3441168963909149, -0.3347882628440857, 0.8628746271133423], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.26198720932006836], "q": [0.0629657432436943, 0.4266679286956787, -3.3145976066589355, -2.364474058151245, 0.1400378942489624, 0.5519500970840454, 2.356898307800293], "blk": [0.5264122486114502, -0.060276519507169724, 0.18488794565200806, 0.14561758935451508, -0.3509075939655304, -0.3741583228111267, 0.8459698557853699], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.13473881781101227], "q": [0.11356832832098007, 0.6102989912033081, -3.366835832595825, -2.3434293270111084, 0.17760756611824036, 0.6912665963172913, 2.215087890625], "blk": [0.5451130270957947, 0.03244509920477867, 0.140181764960289, 0.22914905846118927, -0.3044370710849762, -0.37946510314941406, 0.8430984616279602], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.13473881781101227], "q": [0.27755191922187805, 0.42752575874328613, -3.237753391265869, -2.3772757053375244, 0.3095291554927826, 0.495248407125473, 2.1611063480377197], "blk": [0.5027405619621277, -0.10215730965137482, 0.16320927441120148, 0.1372525542974472, -0.31294000148773193, -0.4430295526981354, 0.8288275599479675], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.3032867908477783], "q": [0.33859774470329285, 0.3370653986930847, -3.1566925048828125, -2.1997551918029785, 0.16025599837303162, 0.64115971326828, 1.9848918914794922], "blk": [0.5262159705162048, -0.3531542718410492, 0.33138811588287354, 0.1530095636844635, -0.504558801651001, -0.6004643440246582, 0.601207971572876], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.3509786128997803], "q": [0.3105073571205139, 0.3326052129268646, -2.9661076068878174, -2.0894787311553955, 0.08379894495010376, 0.5490944385528564, 2.1301400661468506], "blk": [0.4652734398841858, -0.4883252680301666, 0.3591614365577698, 0.028589237481355667, -0.5368740558624268, -0.6299646496772766, 0.5604403614997864], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.3509786128997803], "q": [0.3147899806499481, 0.2703234851360321, -2.7681405544281006, -2.1631011962890625, -0.04311610385775566, 0.701133668422699, 2.2550742626190186], "blk": [0.34756001830101013, -0.5651147365570068, 0.41508692502975464, 0.07666324079036713, 0.5983816981315613, 0.6458604335784912, -0.4678957164287567], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.28382283449172974], "q": [0.498155415058136, 0.440609335899353, -2.6688411235809326, -2.0188207626342773, -0.14425741136074066, 0.557632327079773, 2.32309889793396], "blk": [0.24963334202766418, -0.6671944260597229, 0.34920409321784973, 0.1779106855392456, 0.5210856795310974, 0.7195798754692078, -0.42311030626296997], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.19797542691230774], "q": [0.36497658491134644, 0.398832231760025, -2.5047388076782227, -1.9942604303359985, -0.1129230409860611, 0.43528422713279724, 2.333507776260376], "blk": [0.29965370893478394, -0.6287618279457092, 0.368486225605011, 0.17767921090126038, 0.5102556943893433, 0.6973813772201538, -0.4708804786205292], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.19797542691230774], "q": [0.200550839304924, 0.5916092991828918, -2.4761805534362793, -2.191696882247925, -0.003863358637318015, 0.6265904903411865, 2.3694558143615723], "blk": [0.35805371403694153, -0.5364643335342407, 0.2214493602514267, -0.20408640801906586, -0.4349169135093689, -0.6210440993309021, 0.6192739009857178], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.27010276913642883], "q": [0.07555393129587173, 0.6606199741363525, -2.598137617111206, -2.1606216430664062, 0.03703231364488602, 0.8115597367286682, 2.198361873626709], "blk": [0.4724592864513397, -0.48361915349960327, 0.22579312324523926, -0.091164231300354, -0.5083841681480408, -0.5805249214172363, 0.6294643878936768], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.27011364698410034], "q": [0.17319291830062866, 0.5315106511116028, -2.642910957336426, -2.335463523864746, 0.12738466262817383, 0.6466668844223022, 2.1563985347747803], "blk": [0.3762330114841461, -0.4488864541053772, 0.17682763934135437, -0.07598249614238739, -0.40058478713035583, -0.6580563187599182, 0.6330247521400452], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.27011364698410034], "q": [0.16211305558681488, 0.6965594291687012, -2.53654408454895, -2.1693339347839355, -0.02165413089096546, 0.47609204053878784, 1.9845291376113892], "blk": [0.3366662263870239, -0.5334329009056091, 0.13601498305797577, -0.11254454404115677, -0.36147353053092957, -0.7635449767112732, 0.5231344699859619], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.1225719153881073], "q": [0.21574105322360992, 0.6951881051063538, -2.6711268424987793, -2.0998406410217285, -0.09444717317819595, 0.5604439973831177, 1.968671202659607], "blk": [0.4725562036037445, -0.45869311690330505, 0.16351307928562164, -0.018685458227992058, -0.422769159078598, -0.7187331914901733, 0.5516699552536011], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.11958397179841995], "q": [0.3316073417663574, 0.5322863459587097, -2.6396234035491943, -2.2209465503692627, 0.02880752645432949, 0.5559824109077454, 2.164149284362793], "blk": [0.38962072134017944, -0.4762561619281769, 0.20210477709770203, -0.08581314980983734, -0.41804981231689453, -0.6836780905723572, 0.5919921398162842], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.11958397179841995], "q": [0.5168150067329407, 0.652653157711029, -2.6471192836761475, -2.0955328941345215, 0.06994708627462387, 0.618030846118927, 2.3296256065368652], "blk": [0.34620463848114014, -0.571431577205658, 0.19051896035671234, -0.18023920059204102, -0.4236486256122589, -0.6454726457595825, 0.6094265580177307], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.29347580671310425], "q": [0.6508103013038635, 0.605379045009613, -2.7169008255004883, -1.8979222774505615, 0.18242329359054565, 0.6122449040412903, 2.2986769676208496], "blk": [0.2539825439453125, -0.7160670161247253, 0.29161161184310913, -0.22457805275917053, -0.49235111474990845, -0.6516492962837219, 0.5315150618553162], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.14246423542499542], "q": [0.48553621768951416, 0.6887465715408325, -2.6012392044067383, -1.7782436609268188, 0.11133797466754913, 0.7309005856513977, 2.1888084411621094], "blk": [0.4451482892036438, -0.6534074544906616, 0.3487060070037842, -0.16043215990066528, -0.5951719284057617, -0.5641074776649475, 0.5493766665458679], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.14246423542499542], "q": [0.45251545310020447, 0.7053105235099792, -2.7561936378479004, -1.8154646158218384, -0.08854174613952637, 0.8286528587341309, 2.329558849334717], "blk": [0.4999287724494934, -0.6048134565353394, 0.3384615480899811, -0.12327683717012405, -0.621216893196106, -0.5616597533226013, 0.532382071018219], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.2868915796279907], "q": [0.5340297818183899, 0.8337517976760864, -2.563462257385254, -1.6779483556747437, -0.1188991516828537, 1.0205283164978027, 2.5191524028778076], "blk": [0.309277206659317, -0.7798726558685303, 0.3950899839401245, 0.3656005859375, 0.6360018849372864, 0.4924224019050598, -0.4683566689491272], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.2854207754135132], "q": [0.6354084014892578, 0.9992868304252625, -2.5730035305023193, -1.5324338674545288, -0.038271721452474594, 0.9380980134010315, 2.626213312149048], "blk": [0.2917768955230713, -0.8347035050392151, 0.2942284345626831, -0.4148232638835907, -0.5582473874092102, -0.46810442209243774, 0.5451236367225647], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.2854207754135132], "q": [0.472946435213089, 0.9558390378952026, -2.743507146835327, -1.5419670343399048, -0.06685587763786316, 0.9075930118560791, 2.660733461380005], "blk": [0.47285333275794983, -0.7382144927978516, 0.28974512219429016, -0.30225321650505066, -0.6093319654464722, -0.4494156241416931, 0.57912278175354], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.4363445043563843], "q": [0.6464540362358093, 1.0294592380523682, -2.613994598388672, -1.3832465410232544, -0.033527858555316925, 0.723680317401886, 2.745328187942505], "blk": [0.18251150846481323, -0.9177699685096741, 0.26673978567123413, -0.46394187211990356, -0.4716451168060303, -0.5071262121200562, 0.5523874163627625], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.40873417258262634], "q": [0.7768369317054749, 1.042323350906372, -2.488696813583374, -1.1844425201416016, -0.09330593794584274, 0.5920888781547546, 2.701998233795166], "blk": [0.06805524975061417, -0.9733256101608276, 0.3500667214393616, 0.5268118381500244, 0.45734456181526184, 0.525878369808197, -0.48657700419425964], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.40873417258262634], "q": [0.7525284886360168, 1.077675461769104, -2.637753486633301, -1.093993067741394, -0.1812729686498642, 0.468335896730423, 2.8471782207489014], "blk": [0.15140888094902039, -0.9796918034553528, 0.3009105622768402, -0.47792214155197144, -0.45432817935943604, -0.5465890169143677, 0.5161557793617249], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.38296905159950256], "q": [0.7463280558586121, 1.237204909324646, -2.8033485412597656, -1.015531301498413, -0.25008004903793335, 0.3384998142719269, 2.917097568511963], "blk": [0.2514786422252655, -0.9517715573310852, 0.12957270443439484, -0.3724311888217926, -0.41485559940338135, -0.59525465965271, 0.5786724090576172], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.4378402531147003], "q": [0.6782863736152649, 1.4146760702133179, -2.9236292839050293, -1.0106618404388428, -0.4404747784137726, 0.20384705066680908, 3.070465087890625], "blk": [0.2755456864833832, -0.8780131936073303, -0.0791461169719696, -0.2684997320175171, -0.3098514676094055, -0.664489209651947, 0.6247831583023071], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.4378402531147003], "q": [0.7010205984115601, 1.3036574125289917, -2.9005300998687744, -1.2058031558990479, -0.35527732968330383, 0.29054731130599976, 3.128883123397827], "blk": [0.21691292524337769, -0.8646580576896667, -0.04781191796064377, -0.32096394896507263, -0.2793544828891754, -0.6310740113258362, 0.648605227470398], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.3933047950267792], "q": [0.5305071473121643, 1.2022197246551514, -2.870779037475586, -1.2481285333633423, -0.15846802294254303, 0.4600454568862915, 2.9896862506866455], "blk": [0.41022035479545593, -0.8241335153579712, 0.06721173971891403, -0.33220428228378296, -0.4062492847442627, -0.5027236938476562, 0.6869285106658936], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.35732054710388184], "q": [0.6089932322502136, 1.0568372011184692, -2.9457406997680664, -1.1617614030838013, 0.001975203165784478, 0.3967425227165222, 2.8852639198303223], "blk": [0.4567641019821167, -0.8388685584068298, 0.21389855444431305, -0.31496304273605347, -0.48551973700523376, -0.47849005460739136, 0.6603909134864807], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.35732054710388184], "q": [0.6429862976074219, 1.0474724769592285, -3.043280601501465, -1.3326979875564575, -0.19086822867393494, 0.4287306070327759, 2.7617080211639404], "blk": [0.42287084460258484, -0.8046350479125977, 0.14577007293701172, -0.20436663925647736, -0.4679315984249115, -0.6268379092216492, 0.5885137915611267], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.16710735857486725], "q": [0.4859771728515625, 1.0283080339431763, -3.085416793823242, -1.439773440361023, -0.09136594831943512, 0.48621249198913574, 2.85201096534729], "blk": [0.6596421003341675, -0.5458806753158569, 0.12101230025291443, -0.13935640454292297, -0.4800337255001068, -0.44991710782051086, 0.7400824427604675], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.3339839279651642], "q": [0.4270745515823364, 1.0362412929534912, -3.1147282123565674, -1.6235264539718628, -0.21375496685504913, 0.6642223596572876, 2.717038869857788], "blk": [0.5506155490875244, -0.6075379848480225, 0.08518499881029129, -0.11944326758384705, -0.47114771604537964, -0.5841957330703735, 0.6499757766723633], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.3339839279651642], "q": [0.55592942237854, 0.9927587509155273, -3.1280148029327393, -1.49392569065094, -0.1414804309606552, 0.7989998459815979, 2.820077419281006], "blk": [0.5260328054428101, -0.7114273309707642, 0.22003576159477234, -0.20363804697990417, -0.5819481015205383, -0.5207793712615967, 0.5904716849327087], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.257475346326828], "q": [0.7211190462112427, 1.1218816041946411, -3.256389856338501, -1.3946359157562256, -0.30680790543556213, 0.7693423628807068, 2.778778314590454], "blk": [0.49883151054382324, -0.742164134979248, 0.14826573431491852, -0.1447225958108902, -0.5559545755386353, -0.6387165784835815, 0.5118700861930847], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.37660810351371765], "q": [0.8962811231613159, 0.9597922563552856, -3.454430103302002, -1.4654676914215088, -0.11051002889871597, 0.6752204298973083, 2.9110560417175293], "blk": [0.40455836057662964, -0.7987102270126343, 0.24853649735450745, -0.17508777976036072, -0.5667985677719116, -0.6073207259178162, 0.528436541557312], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.37660810351371765], "q": [0.9308324456214905, 1.1431560516357422, -3.3678247928619385, -1.2732644081115723, -0.08068736642599106, 0.8685542941093445, 3.045874834060669], "blk": [0.32817235589027405, -0.8865007162094116, 0.230600044131279, 0.31802642345428467, 0.589918315410614, 0.5560362935066223, -0.49160873889923096], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.26530882716178894], "q": [1.086228370666504, 1.1957526206970215, -3.425278902053833, -1.2619514465332031, -0.1900872141122818, 0.9795719385147095, 2.9139060974121094], "blk": [0.2797442674636841, -0.8901864886283875, 0.225018709897995, 0.2776234447956085, 0.6193088889122009, 0.6301908493041992, -0.3771487772464752], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.23442964255809784], "q": [1.1005879640579224, 1.2645137310028076, -3.3210842609405518, -1.4180203676223755, -0.1401108205318451, 0.9451543092727661, 2.9595868587493896], "blk": [0.2684468626976013, -0.8350940942764282, 0.07276853173971176, 0.28808146715164185, 0.5162344574928284, 0.6384365558624268, -0.4928588569164276], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.23442964255809784], "q": [1.1347798109054565, 1.357668161392212, -3.3130741119384766, -1.432873249053955, -0.22540327906608582, 0.8368149399757385, 3.037707567214966], "blk": [0.2184171825647354, -0.8058966994285583, -0.0486936941742897, -0.2758435308933258, -0.4132629930973053, -0.6926916837692261, 0.5227832198143005], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.3311198651790619], "q": [0.9972339868545532, 1.4423164129257202, -3.1754298210144043, -1.3617537021636963, -0.2778746783733368, 0.8671038150787354, 3.063072681427002], "blk": [0.16705961525440216, -0.8304363489151001, -0.08739335834980011, -0.34116676449775696, -0.38389164209365845, -0.6722952723503113, 0.5331524014472961], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.3311198651790619], "q": [0.9523036479949951, 1.3082294464111328, -3.0246565341949463, -1.2038623094558716, -0.45856842398643494, 0.7463933825492859, 3.117586135864258], "blk": [0.13180077075958252, -0.9237664341926575, 0.06482590734958649, 0.4181308448314667, 0.41766443848609924, 0.6566568613052368, -0.4685347080230713], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.21558181941509247], "q": [0.9949806928634644, 1.184865117073059, -3.1775999069213867, -1.2014732360839844, -0.3323642611503601, 0.6332202553749084, 2.947639226913452], "blk": [0.30542609095573425, -0.8852866291999817, 0.14319241046905518, 0.2767565846443176, 0.5082839131355286, 0.6596883535385132, -0.47944194078445435], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.1951638162136078], "q": [0.871707558631897, 1.0118346214294434, -3.0682942867279053, -1.0729825496673584, -0.37303003668785095, 0.5508508086204529, 2.858487367630005], "blk": [0.3981630206108093, -0.8800351619720459, 0.35581979155540466, 0.2572195529937744, 0.6152315735816956, 0.6015675663948059, -0.4398234784603119], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.1951638162136078], "q": [0.902470588684082, 1.0229626893997192, -3.1261544227600098, -1.0180141925811768, -0.3027230501174927, 0.5741624236106873, 2.8134055137634277], "blk": [0.40728622674942017, -0.8846220374107361, 0.3857406973838806, 0.24166524410247803, 0.6466927528381348, 0.5856423377990723, -0.42474639415740967], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.14560270309448242], "q": [0.9392316937446594, 0.9590921998023987, -3.204874038696289, -0.9997146725654602, -0.257786363363266, 0.6184817552566528, 2.766540765762329], "blk": [0.4454132616519928, -0.8478851914405823, 0.47298428416252136, 0.20182935893535614, 0.7036842703819275, 0.5555747747421265, -0.3942461311817169], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.11929313838481903], "q": [1.1335395574569702, 0.9303020238876343, -3.0676681995391846, -1.1671851873397827, -0.1076950654387474, 0.7951642274856567, 2.6712863445281982], "blk": [0.26176121830940247, -0.8898820281028748, 0.45774540305137634, 0.32516077160835266, 0.6820493936538696, 0.5363803505897522, -0.3759990632534027], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.11929313838481903], "q": [1.126742959022522, 0.803386926651001, -2.8790156841278076, -1.0081058740615845, 0.07657089084386826, 0.836712121963501, 2.6773505210876465], "blk": [0.24126625061035156, -0.8521439433097839, 0.6672389507293701, 0.45889419317245483, 0.7210825681686401, 0.3588114380836487, -0.3751138746738434], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.0137940039858222], "q": [1.1876825094223022, 0.7028099894523621, -2.705301284790039, -1.0322260856628418, 0.18599338829517365, 0.8370872735977173, 2.5506927967071533], "blk": [0.2504173517227173, -0.7915491461753845, 0.7357779145240784, 0.47804173827171326, 0.7241215109825134, 0.30324026942253113, -0.3939156234264374], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.0678352564573288], "q": [1.2174468040466309, 0.5600107908248901, -2.899806261062622, -1.0586695671081543, 0.2908722460269928, 0.8827502131462097, 2.480351448059082], "blk": [0.22858956456184387, -0.7313569784164429, 0.8305191397666931, 0.4380042254924774, 0.7818689346313477, 0.2711724042892456, -0.3511391878128052], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.0678352564573288], "q": [1.2112526893615723, 0.7598113417625427, -2.789393424987793, -0.9264169931411743, 0.19469180703163147, 0.7436681985855103, 2.3600730895996094], "blk": [0.20800086855888367, -0.841152012348175, 0.7243587374687195, 0.40785521268844604, 0.7484522461891174, 0.3729143440723419, -0.3666173815727234], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.0949292704463005], "q": [1.2161123752593994, 0.6376550793647766, -2.677415609359741, -0.779044508934021, 0.12109380215406418, 0.7468938827514648, 2.397822856903076], "blk": [0.1419174075126648, -0.7560678124427795, 0.9089909195899963, 0.4928084909915924, 0.7747352719306946, 0.2777903079986572, -0.28241387009620667], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.005978004075586796], "q": [1.0751012563705444, 0.5500035285949707, -2.5851330757141113, -0.7517675757408142, 0.28107210993766785, 0.7260372042655945, 2.3604679107666016], "blk": [0.29101210832595825, -0.6468570828437805, 0.9655948877334595, 0.4708271324634552, 0.7963650822639465, 0.181860089302063, -0.333243727684021], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, -0.005978004075586796], "q": [0.9676503539085388, 0.6103100776672363, -2.6792588233947754, -0.606857419013977, 0.18933148682117462, 0.7953810691833496, 2.3877415657043457], "blk": [0.3906727731227875, -0.5588901042938232, 1.0008996725082397, 0.3694981336593628, 0.8769441246986389, 0.11325322836637497, -0.28568145632743835], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.045405514538288116], "q": [1.125817060470581, 0.4783054292201996, -2.8193325996398926, -0.7580965161323547, 0.019907096400856972, 0.8090734481811523, 2.2540340423583984], "blk": [0.262905091047287, -0.5509206056594849, 1.045157790184021, 0.25261542201042175, 0.9266470074653625, 0.20527265965938568, -0.18807941675186157], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.1682726889848709], "q": [0.9348612427711487, 0.42814821004867554, -2.8300509452819824, -0.87148517370224, -0.03773041442036629, 0.6981900334358215, 2.1667654514312744], "blk": [0.41155627369880676, -0.473985493183136, 1.0165045261383057, 0.04413742199540138, 0.93387770652771, 0.2691859006881714, -0.23122122883796692], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.1682726889848709], "q": [0.9017314314842224, 0.382494181394577, -2.785581111907959, -0.8058284521102905, 0.026380198076367378, 0.5320936441421509, 2.199526309967041], "blk": [0.41354310512542725, -0.4563767910003662, 1.0453150272369385, 0.08850309997797012, 0.9201616644859314, 0.27403777837753296, -0.265279084444046], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.26264211535453796], "q": [1.019958734512329, 0.4179078936576843, -2.933351993560791, -0.9723322987556458, -0.04439832642674446, 0.7031171321868896, 2.1885733604431152], "blk": [0.44608137011528015, -0.46564096212387085, 0.9737295508384705, -0.0007663591532036662, 0.9180335402488708, 0.3057241439819336, -0.25248077511787415], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.42083168029785156], "q": [1.003828763961792, 0.5199551582336426, -2.939301013946533, -0.8888514041900635, -0.11752662062644958, 0.8590632677078247, 2.0948567390441895], "blk": [0.5183976888656616, -0.36178454756736755, 0.9747738242149353, -0.15090148150920868, 0.931667149066925, 0.2534613013267517, -0.21209056675434113], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.42083168029785156], "q": [1.0922950506210327, 0.5905969142913818, -2.876540422439575, -0.8138853907585144, -0.08302093297243118, 0.7051748037338257, 2.1625380516052246], "blk": [0.5281844735145569, -0.4521315395832062, 0.9341846704483032, -0.03665327653288841, 0.9159883856773376, 0.29511988162994385, -0.26930660009384155], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.22347110509872437], "q": [0.9654321670532227, 0.558948278427124, -2.9251928329467773, -0.9662993550300598, -0.11223789304494858, 0.7546217441558838, 2.113523483276367], "blk": [0.49879640340805054, -0.5237506628036499, 0.8908036947250366, -0.05311276763677597, 0.9003462791442871, 0.34978532791137695, -0.25338879227638245], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.3068709075450897], "q": [0.8578010201454163, 0.41647839546203613, -2.8256328105926514, -0.8988081216812134, -0.1404896080493927, 0.6093286275863647, 2.178997039794922], "blk": [0.5010324120521545, -0.39366933703422546, 0.9988062381744385, -0.07756677269935608, 0.9131247401237488, 0.3067622184753418, -0.2570672631263733], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.3068709075450897], "q": [0.72337806224823, 0.4921990931034088, -2.883378028869629, -0.7327606678009033, -0.03987374156713486, 0.518821120262146, 2.3542075157165527], "blk": [0.6077253818511963, -0.28710123896598816, 1.003269910812378, -0.05356500297784805, 0.9133426547050476, 0.23506399989128113, -0.32814767956733704], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}, {"base": [-0.11999999731779099, 0.0, 0.11696400493383408], "q": [0.5973076820373535, 0.3889602720737457, -2.79054594039917, -0.7222934365272522, -0.05412357673048973, 0.4078344404697418, 2.456794261932373], "blk": [0.5231311917304993, -0.35213702917099, 1.0560027360916138, 0.0643121600151062, 0.9150351285934448, 0.24466781318187714, -0.3141852021217346], "gtf": [0.013171643018722534, 0.02537059783935547, 0.02747468650341034, 5.026847247791011e-06, 0.9977238178253174, 0.04993142560124397, -0.045321736484766006]}]
\ No newline at end of file
diff --git a/e_n0.txt b/e_n0.txt
new file mode 100644
index 0000000..3c9d1e2
--- /dev/null
+++ b/e_n0.txt
@@ -0,0 +1,9 @@
           1 +(0.25,-0.36) lowest reached ee z=0.230, e=8.6e-05
           2 +(0.25,-0.37) lowest reached ee z=0.230, e=8.4e-05
           3 +(0.25,-0.38) lowest reached ee z=0.230, e=8.3e-05
           4 +(0.25,-0.39) lowest reached ee z=0.230, e=8.1e-05
           5 +(0.25,-0.4) lowest reached ee z=0.230, e=8.0e-05
           6 +(0.25,-0.41) lowest reached ee z=0.230, e=7.8e-05
           7 +(0.25,-0.42) lowest reached ee z=0.155, e=6.6e-05
           8 +(0.25,-0.43) lowest reached ee z=0.130, e=6.1e-05
           9 +(0.25,-0.44) lowest reached ee z=0.005, e=5.0e-05
diff --git a/e_n1.txt b/e_n1.txt
new file mode 100644
index 0000000..dc6dd12
--- /dev/null
+++ b/e_n1.txt
@@ -0,0 +1,9 @@
           1 +(0.25,-0.36) lowest reached ee z=0.230, e=8.8e-05
           2 +(0.25,-0.37) lowest reached ee z=0.230, e=8.6e-05
           3 +(0.25,-0.38) lowest reached ee z=0.230, e=8.4e-05
           4 +(0.25,-0.39) lowest reached ee z=0.230, e=8.2e-05
           5 +(0.25,-0.4) lowest reached ee z=0.230, e=8.1e-05
           6 +(0.25,-0.41) lowest reached ee z=0.230, e=7.9e-05
           7 +(0.25,-0.42) lowest reached ee z=0.230, e=7.8e-05
           8 +(0.25,-0.43) lowest reached ee z=0.230, e=7.7e-05
           9 +(0.25,-0.44) lowest reached ee z=0.230, e=7.6e-05
diff --git a/e_x0.txt b/e_x0.txt
new file mode 100644
index 0000000..f280889
--- /dev/null
+++ b/e_x0.txt
@@ -0,0 +1,9 @@
           1 +(0.4,0.0) lowest reached ee z=0.235, e=4.4e-05
           2 +(0.41,0.0) lowest reached ee z=0.220, e=4.4e-05
           3 +(0.42,0.0) lowest reached ee z=0.210, e=4.4e-05
           4 +(0.43,0.0) lowest reached ee z=0.200, e=4.4e-05
           5 +(0.44,0.0) lowest reached ee z=0.135, e=4.7e-05
           6 +(0.45,0.0) lowest reached ee z=0.005, e=5.5e-05
           7 +(0.46,0.0) lowest reached ee z=0.005, e=5.6e-05
           8 +(0.47,0.0) lowest reached ee z=0.005, e=5.6e-05
           9 +(0.48,0.0) lowest reached ee z=0.005, e=5.6e-05
diff --git a/e_x1.txt b/e_x1.txt
new file mode 100644
index 0000000..2ce02af
--- /dev/null
+++ b/e_x1.txt
@@ -0,0 +1,9 @@
           1 +(0.4,0.0) lowest reached ee z=0.160, e=6.1e-05
           2 +(0.41,0.0) lowest reached ee z=0.130, e=5.5e-05
           3 +(0.42,0.0) lowest reached ee z=0.005, e=4.8e-05
           4 +(0.43,0.0) lowest reached ee z=0.005, e=4.8e-05
           5 +(0.44,0.0) lowest reached ee z=0.005, e=4.8e-05
           6 +(0.45,0.0) lowest reached ee z=0.005, e=4.8e-05
           7 +(0.46,0.0) lowest reached ee z=0.005, e=4.9e-05
           8 +(0.47,0.0) lowest reached ee z=0.005, e=4.9e-05
           9 +(0.48,0.0) lowest reached ee z=0.005, e=5.0e-05
diff --git a/e_y0.txt b/e_y0.txt
new file mode 100644
index 0000000..35a00f5
--- /dev/null
+++ b/e_y0.txt
@@ -0,0 +1,9 @@
           1 +(0.25,0.36) lowest reached ee z=0.235, e=4.6e-05
           2 +(0.25,0.37) lowest reached ee z=0.235, e=4.5e-05
           3 +(0.25,0.38) lowest reached ee z=0.210, e=4.6e-05
           4 +(0.25,0.39) lowest reached ee z=0.190, e=4.6e-05
           5 +(0.25,0.4) lowest reached ee z=0.165, e=4.7e-05
           6 +(0.25,0.41) lowest reached ee z=0.145, e=4.7e-05
           7 +(0.25,0.42) lowest reached ee z=0.135, e=4.8e-05
           8 +(0.25,0.43) lowest reached ee z=0.120, e=4.8e-05
           9 +(0.25,0.44) lowest reached ee z=0.080, e=5.1e-05
diff --git a/e_y1.txt b/e_y1.txt
new file mode 100644
index 0000000..6394277
--- /dev/null
+++ b/e_y1.txt
@@ -0,0 +1,9 @@
           1 +(0.25,0.36) lowest reached ee z=0.230, e=8.4e-05
           2 +(0.25,0.37) lowest reached ee z=0.230, e=8.3e-05
           3 +(0.25,0.38) lowest reached ee z=0.230, e=8.1e-05
           4 +(0.25,0.39) lowest reached ee z=0.230, e=8.0e-05
           5 +(0.25,0.4) lowest reached ee z=0.230, e=7.8e-05
           6 +(0.25,0.41) lowest reached ee z=0.230, e=7.7e-05
           7 +(0.25,0.42) lowest reached ee z=0.230, e=7.6e-05
           8 +(0.25,0.43) lowest reached ee z=0.230, e=7.5e-05
           9 +(0.25,0.44) lowest reached ee z=0.230, e=7.4e-05
diff --git a/fit.py b/fit.py
new file mode 100644
index 0000000..6e13672
--- /dev/null
+++ b/fit.py
@@ -0,0 +1,27 @@
           1 +import numpy as np, json
           2 +from scipy.optimize import least_squares
           3 +from scipy.spatial.transform import Rotation as Rot
           4 +from kin import *
           5 +D=json.load(open('calib_data.json'))
           6 +def pose(v):
           7 +    M=np.eye(4); M[:3,:3]=Rot.from_quat(v[3:7]).as_matrix(); M[:3,3]=v[:3]; return M
           8 +g=np.array([d['gtf'] for d in D]); print('gtf std', g.std(0).round(5), g[0].round(4))
           9 +EEt=[pose(d['blk'])@np.linalg.inv(pose(d['gtf'])) for d in D]
          10 +def chain(base,q):
          11 +    return fk(base,q)
          12 +def Tp(p):
          13 +    M=np.eye(4); M[:3,:3]=Rot.from_rotvec(p[3:6]).as_matrix(); M[:3,3]=p[:3]; return M
          14 +def res(p):
          15 +    A=Tp(p[:6]); B=Tp(p[6:12]); r=[]
          16 +    for d,E in zip(D,EEt):
          17 +        bx,by,br=d['base']
          18 +        Bw=Rz(br); Bw[0,3]=bx; Bw[1,3]=by
          19 +        M=Bw@A@np.linalg.inv(Bw)@fk(d['base'],d['q'])@B  # A applied in base frame
          20 +        r.extend(M[:3,3]-E[:3,3]); r.extend(0.1*(M[:3,:3]-E[:3,:3]).ravel())
          21 +    return np.array(r)
          22 +sol=least_squares(res,np.zeros(12))
          23 +np.set_printoptions(precision=5,suppress=True)
          24 +print('A',sol.x[:6]); print('B',sol.x[6:]); r=res(sol.x).reshape(len(D),-1)
          25 +print('pos resid max',np.abs(r[:,:3]).max(),'rot resid max',np.abs(r[:,3:]).max())
          26 +print('raw EE pos err (no fit) first',EEt[0][:3,3]-fk(D[0]['base'],D[0]['q'])[:3,3])
          27 +print(EEt[0].round(4)); print(fk(D[0]['base'],D[0]['q']).round(4))
diff --git a/g_0.25.txt b/g_0.25.txt
new file mode 100644
index 0000000..806b219
--- /dev/null
+++ b/g_0.25.txt
@@ -0,0 +1 @@
           1 +none at z 0.25 steps 52 time 11.063755750656128
diff --git a/g_0.25_0.785.txt b/g_0.25_0.785.txt
new file mode 100644
index 0000000..2aaa982
--- /dev/null
+++ b/g_0.25_0.785.txt
@@ -0,0 +1 @@
           1 +none at z 0.25 steps 61 time 35.490243673324585
diff --git a/g_0.25_1.5708.txt b/g_0.25_1.5708.txt
new file mode 100644
index 0000000..9cf78fd
--- /dev/null
+++ b/g_0.25_1.5708.txt
@@ -0,0 +1 @@
           1 +none at z 0.25 steps 59 time 22.313653469085693
diff --git a/g_0.27.txt b/g_0.27.txt
new file mode 100644
index 0000000..da19c18
--- /dev/null
+++ b/g_0.27.txt
@@ -0,0 +1 @@
           1 +none at z 0.27 steps 52 time 14.83537483215332
diff --git a/g_0.27_0.785.txt b/g_0.27_0.785.txt
new file mode 100644
index 0000000..3783fa5
--- /dev/null
+++ b/g_0.27_0.785.txt
@@ -0,0 +1 @@
           1 +none at z 0.27 steps 61 time 30.145485162734985
diff --git a/g_0.27_1.5708.txt b/g_0.27_1.5708.txt
new file mode 100644
index 0000000..953f649
--- /dev/null
+++ b/g_0.27_1.5708.txt
@@ -0,0 +1 @@
           1 +none at z 0.27 steps 60 time 33.91507005691528
diff --git a/g_0.29.txt b/g_0.29.txt
new file mode 100644
index 0000000..c2a5abc
--- /dev/null
+++ b/g_0.29.txt
@@ -0,0 +1 @@
           1 +none at z 0.29 steps 53 time 21.4253511428833
diff --git a/g_0.29_0.785.txt b/g_0.29_0.785.txt
new file mode 100644
index 0000000..58616b3
--- /dev/null
+++ b/g_0.29_0.785.txt
@@ -0,0 +1 @@
           1 +none at z 0.29 steps 65 time 34.08960676193237
diff --git a/g_0.29_1.5708.txt b/g_0.29_1.5708.txt
new file mode 100644
index 0000000..420b7a9
--- /dev/null
+++ b/g_0.29_1.5708.txt
@@ -0,0 +1 @@
           1 +none at z 0.29 steps 61 time 25.39711356163025
diff --git a/g_0.31.txt b/g_0.31.txt
new file mode 100644
index 0000000..78a5170
--- /dev/null
+++ b/g_0.31.txt
@@ -0,0 +1 @@
           1 +none at z 0.31 steps 54 time 17.78290319442749
diff --git a/g_0.33.txt b/g_0.33.txt
new file mode 100644
index 0000000..42dbe9b
--- /dev/null
+++ b/g_0.33.txt
@@ -0,0 +1 @@
           1 +none at z 0.33 steps 54 time 27.491010189056396
diff --git a/g_0.35.txt b/g_0.35.txt
new file mode 100644
index 0000000..602a9c6
--- /dev/null
+++ b/g_0.35.txt
@@ -0,0 +1 @@
           1 +none at z 0.35 steps 55 time 25.460607528686523
diff --git a/h2_0.23.txt b/h2_0.23.txt
new file mode 100644
index 0000000..5f75282
--- /dev/null
+++ b/h2_0.23.txt
@@ -0,0 +1 @@
           1 +none at z 0.23 steps 55 time 17.34662365913391
diff --git a/h2_0.25.txt b/h2_0.25.txt
new file mode 100644
index 0000000..c99dea5
--- /dev/null
+++ b/h2_0.25.txt
@@ -0,0 +1 @@
           1 +none at z 0.25 steps 51 time 8.317227363586426
diff --git a/h2_0.27.txt b/h2_0.27.txt
new file mode 100644
index 0000000..55966a0
--- /dev/null
+++ b/h2_0.27.txt
@@ -0,0 +1 @@
           1 +none at z 0.27 steps 51 time 20.923149585723877
diff --git a/h_0.23.txt b/h_0.23.txt
new file mode 100644
index 0000000..1361807
--- /dev/null
+++ b/h_0.23.txt
@@ -0,0 +1 @@
           1 +none at z 0.23 steps 51 time 11.331629514694214
diff --git a/h_0.25.txt b/h_0.25.txt
new file mode 100644
index 0000000..d9a317f
--- /dev/null
+++ b/h_0.25.txt
@@ -0,0 +1 @@
           1 +GRASP 0.25 -0.01999999999999999 -0.039999999999999994 [0.0049, 0.0384, 0.0252, 0.0, 0.9998, 0.0054, -0.0174]
diff --git a/h_0.27.txt b/h_0.27.txt
new file mode 100644
index 0000000..87d18a4
--- /dev/null
+++ b/h_0.27.txt
@@ -0,0 +1 @@
           1 +GRASP 0.27 -0.039999999999999994 -0.039999999999999994 [-0.0029, 0.0294, 0.0482, 0.0, 0.9982, 0.0317, -0.0516]
diff --git a/kin.py b/kin.py
new file mode 100644
index 0000000..8a84b74
--- /dev/null
+++ b/kin.py
@@ -0,0 +1,80 @@
           1 +import numpy as np
           2 +# Kinova Gen3 7DOF chain (kortex gen3.urdf); calibrated mount offset & tool offset.
           3 +JOINTS = [
           4 +    ((0, 0, 0.15643), (np.pi, 0, 0)),
           5 +    ((0, 0.005375, -0.12838), (np.pi/2, 0, 0)),
           6 +    ((0, -0.21038, -0.006375), (-np.pi/2, 0, 0)),
           7 +    ((0, 0.006375, -0.21038), (np.pi/2, 0, 0)),
           8 +    ((0, -0.20843, -0.006375), (-np.pi/2, 0, 0)),
           9 +    ((0, 0.00017505, -0.10593), (np.pi/2, 0, 0)),
          10 +    ((0, -0.10593, -0.00017505), (-np.pi/2, 0, 0)),
          11 +]
          12 +MOUNT = (0.12, 0.0, -0.0052)
          13 +TOOL = 0.12  # grasp frame is TOOL beyond end_effector_link along its z
          14 +
          15 +def rpy2R(r, p, y):
          16 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
          17 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
          18 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
          19 +                     [-sp, cp*sr, cp*cr]])
          20 +
          21 +def T(xyz, rpy):
          22 +    M = np.eye(4); M[:3,:3] = rpy2R(*rpy); M[:3,3] = xyz; return M
          23 +
          24 +def Rz(q):
          25 +    M = np.eye(4); c, s = np.cos(q), np.sin(q); M[0,0]=c; M[0,1]=-s; M[1,0]=s; M[1,1]=c; return M
          26 +
          27 +JT = [T(*j) for j in JOINTS]
          28 +EET = T((0, 0, -0.061525 - TOOL), (np.pi, 0, 0))  # combined end effector + tool
          29 +
          30 +def base_T(base):
          31 +    bx, by, br = base
          32 +    M = Rz(br); M[0,3] = bx; M[1,3] = by
          33 +    return M @ T(MOUNT, (0, 0, 0))
          34 +
          35 +def fk(base, q):
          36 +    M = base_T(base)
          37 +    for i in range(7):
          38 +        M = M @ JT[i] @ Rz(q[i])
          39 +    return M @ EET
          40 +
          41 +def fk_all(base, q):
          42 +    """Return list of frames: mount, after each joint, tool."""
          43 +    M = base_T(base); out = [M]
          44 +    for i in range(7):
          45 +        M = M @ JT[i] @ Rz(q[i]); out.append(M)
          46 +    out.append(M @ EET)
          47 +    return out
          48 +
          49 +def jac(base, q):
          50 +    """Geometric Jacobian (6x7) of tool point: rows pos, rot."""
          51 +    Ms = fk_all(base, q)
          52 +    p = Ms[-1][:3,3]
          53 +    J = np.zeros((6,7))
          54 +    for i in range(7):
          55 +        z = Ms[i+1][:3,2]; o = Ms[i+1][:3,3]
          56 +        J[:3,i] = np.cross(z, p - o); J[3:,i] = z
          57 +    return J, Ms[-1]
          58 +
          59 +def rot_err(Rc, Rt):
          60 +    E = Rt @ Rc.T
          61 +    return 0.5*np.array([E[2,1]-E[1,2], E[0,2]-E[2,0], E[1,0]-E[0,1]])
          62 +
          63 +def ik(base, q0, pos, R, iters=100, w_ori=0.5, tol=1e-5):
          64 +    q = np.array(q0, dtype=float)
          65 +    err = 1e9
          66 +    for it in range(iters):
          67 +        J, M = jac(base, q)
          68 +        e = np.concatenate([pos - M[:3,3], w_ori*rot_err(M[:3,:3], R)])
          69 +        err = np.linalg.norm(e)
          70 +        if err < tol: break
          71 +        Jw = J.copy(); Jw[3:] *= w_ori
          72 +        dq = Jw.T @ np.linalg.solve(Jw@Jw.T + 1e-4*np.eye(6), e)
          73 +        n = np.linalg.norm(dq)
          74 +        if n > 0.4: dq *= 0.4/n
          75 +        q += dq
          76 +    return q, err
          77 +
          78 +def down_R(yaw):
          79 +    c, s = np.cos(yaw), np.sin(yaw)
          80 +    return np.array([[c, s, 0],[s, -c, 0],[0, 0, -1.0]])
diff --git a/m1.txt b/m1.txt
new file mode 100644
index 0000000..b38c076
--- /dev/null
+++ b/m1.txt
@@ -0,0 +1,4 @@
           1 +(0.35,0.1) lowest reached ee z=0.240, e=1.2e-06
           2 +(0.4,0.1) lowest reached ee z=0.240, e=1.2e-06
           3 +(0.45,0.1) lowest reached ee z=0.120, e=1.3e-06
           4 +(0.5,0.1) lowest reached ee z=-0.090, e=2.8e-06
diff --git a/m2.txt b/m2.txt
new file mode 100644
index 0000000..cd0909c
--- /dev/null
+++ b/m2.txt
@@ -0,0 +1,4 @@
           1 +(0.25,0.35) lowest reached ee z=0.240, e=1.2e-06
           2 +(0.25,0.4) lowest reached ee z=0.190, e=1.2e-06
           3 +(0.25,0.45) lowest reached ee z=-0.050, e=2.0e-06
           4 +(0.25,-0.4) lowest reached ee z=0.230, e=4.9e-06
diff --git a/probe0.py b/probe0.py
new file mode 100644
index 0000000..6ca8c2e
--- /dev/null
+++ b/probe0.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +print(type(obs), info)
           6 +for t in obs.get_objects.__self__.__class__.__mro__: pass
           7 +for name in obs.get_object_names():
           8 +    o = obs.get_object_from_name(name)
           9 +    print(name, o.type if hasattr(o,'type') else '', end=': ')
          10 +    try:
          11 +        feats = env.observation_space.get_type(o.type.name if hasattr(o.type,'name') else o.type)
          12 +    except Exception as e: feats=None
          13 +    print(o)
          14 +print(dir(obs))
diff --git a/probe1.py b/probe1.py
new file mode 100644
index 0000000..b3f0b74
--- /dev/null
+++ b/probe1.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +for seed in [0,1,2]:
           5 +    obs, info = env.reset(seed=seed)
           6 +    print('seed',seed,info)
           7 +    for name in sorted(obs.get_object_names()):
           8 +        o = obs.get_object_from_name(name)
           9 +        feats = obs.type_features[o.type] if isinstance(obs.type_features, dict) else None
          10 +        vals = {f: round(float(obs.get(o,f)),4) for f in feats}
          11 +        print(' ',name, vals)
diff --git a/probe2.py b/probe2.py
new file mode 100644
index 0000000..da37b16
--- /dev/null
+++ b/probe2.py
@@ -0,0 +1,24 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +R = obs.get_object_from_name('robot')
           6 +feats = obs.type_features[R.type]
           7 +def rv(o): return np.array([obs.get(R,f) for f in feats])
           8 +def show(tag):
           9 +    print(tag, {f: round(float(obs.get(R,f)),4) for f in feats if not f.startswith('grasp_tf')})
          10 +show('init')
          11 +a = np.zeros(11,dtype=np.float32)
          12 +obs,r,te,tr,_ = env.step(a); show('zero'); print(r,te,tr)
          13 +a[3]=0.5; obs,*_ = env.step(a); show('j1 +0.5 (clip?)')
          14 +a[:]=0; a[0]=0.1; obs,*_ = env.step(a); show('base x+0.1')
          15 +a[:]=0; a[2]=0.1; obs,*_ = env.step(a); show('base rot+0.1')
          16 +a[:]=0; a[10]=-1; obs,*_ = env.step(a); show('close')
          17 +obs,*_ = env.step(a); show('close2')
          18 +a[:]=0; a[10]=1; obs,*_ = env.step(a); show('open')
          19 +a[:]=0; a[5]=0.2; 
          20 +for i in range(20): obs,*_ = env.step(a)
          21 +show('j3 +4.0')
          22 +a[:]=0; a[4]=0.2
          23 +for i in range(20): obs,*_ = env.step(a)
          24 +show('j2 +4.0')
diff --git a/probe3.py b/probe3.py
new file mode 100644
index 0000000..3205f87
--- /dev/null
+++ b/probe3.py
@@ -0,0 +1,9 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +R = obs.get_object_from_name('robot')
           6 +for g in [1,1,1,-1,-1,-1,0.7,-0.7,0,1,0,-1]:
           7 +    a=np.zeros(11,dtype=np.float32); a[10]=g
           8 +    obs,r,te,tr,inf=env.step(a)
           9 +    print(g, obs.get(R,'finger_state'), obs.get(R,'grasp_active'), inf)
diff --git a/stats.py b/stats.py
new file mode 100644
index 0000000..feacd71
--- /dev/null
+++ b/stats.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +P={'target_region':[], 'target_block':[], 'obs':[]}; cnt=[]
           5 +for s in range(150):
           6 +    o,info=env.reset(seed=s); cnt.append(info['object_count'])
           7 +    for n in o.get_object_names():
           8 +        if n=='robot': continue
           9 +        ob=o.get_object_from_name(n); v=[o.get(ob,f) for f in ('pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z')]
          10 +        P['obs' if n.startswith('obst') else n].append(v)
          11 +for k,v in P.items():
          12 +    v=np.array(v); print(k, 'min',v.min(0).round(3),'max',v.max(0).round(3))
          13 +print('counts', np.bincount(cnt))
diff --git a/viz1/approach.py b/viz1/approach.py
new file mode 100644
index 0000000..5de9876
--- /dev/null
+++ b/viz1/approach.py
@@ -0,0 +1,15 @@
           1 +import numpy as np
           2 +from kin import *
           3 +class GeneratedApproach:
           4 +    def __init__(self, action_space, observation_space, primitives): pass
           5 +    def reset(self, state, info):
           6 +        self.t=0
           7 +    def get_action(self, s):
           8 +        self.t+=1
           9 +        R=s.get_object_from_name('robot'); tb=s.get_object_from_name('target_block')
          10 +        q=np.array([s.get(R,f'joint_{i}') for i in range(1,8)])
          11 +        base=(s.get(R,'pos_base_x'),s.get(R,'pos_base_y'),s.get(R,'pos_base_rot'))
          12 +        qt,e=ik(base,q,np.array([s.get(tb,'pose_x'),s.get(tb,'pose_y'),0.25]),down_R(0))
          13 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.2,0.2)
          14 +        if self.t>12: a[:]=0; a[10]=-1
          15 +        return a
diff --git a/viz1/kin.py b/viz1/kin.py
new file mode 100644
index 0000000..591fa9f
--- /dev/null
+++ b/viz1/kin.py
@@ -0,0 +1,68 @@
           1 +import numpy as np
           2 +# Kinova Gen3 7DOF (kortex_description gen3.urdf) joint origins: xyz, rpy; all axes z
           3 +JOINTS = [
           4 +    ((0, 0, 0.15643), (np.pi, 0, 0)),
           5 +    ((0, 0.005375, -0.12838), (np.pi/2, 0, 0)),
           6 +    ((0, -0.21038, -0.006375), (-np.pi/2, 0, 0)),
           7 +    ((0, 0.006375, -0.21038), (np.pi/2, 0, 0)),
           8 +    ((0, -0.20843, -0.006375), (-np.pi/2, 0, 0)),
           9 +    ((0, 0.00017505, -0.10593), (np.pi/2, 0, 0)),
          10 +    ((0, -0.10593, -0.00017505), (-np.pi/2, 0, 0)),
          11 +]
          12 +EE = ((0, 0, -0.061525), (np.pi, 0, 0))
          13 +
          14 +def rpy2R(r, p, y):
          15 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
          16 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
          17 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
          18 +                     [-sp, cp*sr, cp*cr]])
          19 +
          20 +def T(xyz, rpy):
          21 +    M = np.eye(4); M[:3,:3] = rpy2R(*rpy); M[:3,3] = xyz; return M
          22 +
          23 +def Rz(q):
          24 +    M = np.eye(4); c, s = np.cos(q), np.sin(q); M[0,0]=c; M[0,1]=-s; M[1,0]=s; M[1,1]=c; return M
          25 +
          26 +JT = [T(*j) for j in JOINTS]
          27 +EET = T(*EE)
          28 +
          29 +def fk(base, q, base_z=0.0, tool=0.0):
          30 +    bx, by, br = base
          31 +    M = Rz(br); M[0,3]=bx; M[1,3]=by; M[2,3]=base_z
          32 +    for i in range(7):
          33 +        M = M @ JT[i] @ Rz(q[i])
          34 +    M = M @ EET
          35 +    if tool:
          36 +        M = M.copy(); M[:3,3] = M[:3,3] + M[:3,2]*tool
          37 +    return M
          38 +
          39 +def pose_err(M, pos, R):
          40 +    ep = pos - M[:3,3]
          41 +    Rc = M[:3,:3]
          42 +    # orientation error (axis-angle approx)
          43 +    E = R @ Rc.T
          44 +    eo = 0.5*np.array([E[2,1]-E[1,2], E[0,2]-E[2,0], E[1,0]-E[0,1]])
          45 +    return np.concatenate([ep, eo])
          46 +
          47 +def ik(base, q0, pos, R, base_z=0.0, tool=0.0, iters=200, w_ori=0.3, tol=1e-4):
          48 +    q = np.array(q0, dtype=float)
          49 +    for it in range(iters):
          50 +        M = fk(base, q, base_z, tool)
          51 +        e = pose_err(M, pos, R); e[3:] *= w_ori
          52 +        if np.linalg.norm(e) < tol: break
          53 +        J = np.zeros((6,7)); h=1e-6
          54 +        for i in range(7):
          55 +            dq = q.copy(); dq[i]+=h
          56 +            e2 = pose_err(fk(base, dq, base_z, tool), pos, R); e2[3:]*=w_ori
          57 +            J[:,i] = -(e2-e)/h
          58 +        lam = 1e-3
          59 +        dq = J.T @ np.linalg.solve(J@J.T + lam*np.eye(6), e)
          60 +        n = np.linalg.norm(dq)
          61 +        if n > 0.3: dq *= 0.3/n
          62 +        q += dq
          63 +    return q, np.linalg.norm(e)
          64 +
          65 +def down_R(yaw):
          66 +    # tool z pointing down, tool x along yaw
          67 +    c, s = np.cos(yaw), np.sin(yaw)
          68 +    return np.array([[c, s, 0],[s, -c, 0],[0, 0, -1.0]])
```

</details>

<a id="C003"></a>
### C003 · First full approach: clear obstructions then place block

Commit `f57fd5548266345cdd0e1a723a19341328353de5`; parents: c8036df9077f72c4644964fbd7a3fbc0b330fb39. Recorded author date: 2026-09-28T19:38:38+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0229](01_timeline.md#E0229): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_f57fd55_approach.py) · [Exact all-file diff](evidence/diffs/C003_f57fd55.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..6f1e4fd
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,302 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on the region.  Uses a calibrated Kinova Gen3 FK/IK model
           3 +(see kin.py) and a Cartesian waypoint controller."""
           4 +import numpy as np
           5 +from kin import fk, ik, down_R, jac, rot_err
           6 +
           7 +TABLE_Z = 0.075
           8 +TABLE_X = (0.10, 0.50)
           9 +TABLE_Y = (-0.40, 0.40)
          10 +SAFE_Z = 0.30          # tool height for transport
          11 +GRASP_DZ = 0.015       # tool height above object top when closing
          12 +PLACE_EPS = 0.0015     # clearance above support surface when releasing
          13 +MAX_DQ = 0.2
          14 +JLIM = {1: 2.41, 3: 2.66, 5: 2.23}   # limited joints (0-indexed): 2,4,6 in 1-index
          15 +
          16 +
          17 +def wrap(a):
          18 +    return (a + np.pi) % (2 * np.pi) - np.pi
          19 +
          20 +
          21 +class GeneratedApproach:
          22 +    def __init__(self, action_space, observation_space, primitives):
          23 +        self.action_space = action_space
          24 +
          25 +    # ------------------------------------------------------------------ utils
          26 +    def _read(self, s):
          27 +        self.s = s
          28 +        self.R = s.get_object_from_name('robot')
          29 +        self.q = np.array([s.get(self.R, f'joint_{i}') for i in range(1, 8)])
          30 +        self.base = tuple(s.get(self.R, f) for f in ('pos_base_x', 'pos_base_y', 'pos_base_rot'))
          31 +        self.grasped = s.get(self.R, 'grasp_active') > 0.5
          32 +        self.objs = {}
          33 +        for n in s.get_object_names():
          34 +            if n == 'robot':
          35 +                continue
          36 +            o = s.get_object_from_name(n)
          37 +            try:
          38 +                p = np.array([s.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')])
          39 +                he = np.array([s.get(o, 'half_extent_' + c) for c in 'xyz'])
          40 +            except Exception:
          41 +                continue
          42 +            self.objs[n] = (p, he)
          43 +
          44 +    def _obstructions(self):
          45 +        return sorted(n for n in self.objs if n not in ('target_block', 'target_region'))
          46 +
          47 +    def reset(self, state, info):
          48 +        self._read(state)
          49 +        self.phase = 'plan'
          50 +        self.task = None
          51 +        self.path = []
          52 +        self.last_q = None
          53 +        self.last_cmd = None
          54 +        self.blocked = 0
          55 +        self.fail = {}
          56 +        self.t = 0
          57 +        self.wait = 0
          58 +
          59 +    # ------------------------------------------------------------ geometry
          60 +    def _final_block_xy(self):
          61 +        p, _ = self.objs['target_region']
          62 +        return p[:2].copy()
          63 +
          64 +    def _needs_clearing(self, n):
          65 +        """Obstruction overlaps the target block's final footprint (+margin)."""
          66 +        rp, rhe = self.objs['target_region']
          67 +        bp, bhe = self.objs['target_block']
          68 +        p, he = self.objs[n]
          69 +        c = self._final_block_xy()
          70 +        m = 0.012
          71 +        ox = abs(p[0] - c[0]) < he[0] + bhe[0] + m
          72 +        oy = abs(p[1] - c[1]) < he[1] + bhe[1] + m
          73 +        # also anything touching the region itself
          74 +        rx = abs(p[0] - rp[0]) < he[0] + rhe[0] + 0.005
          75 +        ry = abs(p[1] - rp[1]) < he[1] + rhe[1] + 0.005
          76 +        return (ox and oy) or (rx and ry and p[2] - he[2] > rp[2])
          77 +
          78 +    def _free_spot(self, name):
          79 +        """Pick a table location for obstruction `name` far from other stuff."""
          80 +        p0, he0 = self.objs[name]
          81 +        rp, rhe = self.objs['target_region']
          82 +        c = self._final_block_xy()
          83 +        best, bestv = None, -1e9
          84 +        r0 = max(he0[0], he0[1])
          85 +        for x in np.linspace(TABLE_X[0] + 0.07, TABLE_X[1] - 0.06, 11):
          86 +            for y in np.linspace(TABLE_Y[0] + 0.06, TABLE_Y[1] - 0.06, 17):
          87 +                clear = 1e9
          88 +                for n, (p, he) in self.objs.items():
          89 +                    if n == name:
          90 +                        continue
          91 +                    ext = he[:2].copy()
          92 +                    if n == 'target_region':
          93 +                        ext = ext + 0.03
          94 +                    dx = max(0.0, abs(x - p[0]) - ext[0] - r0)
          95 +                    dy = max(0.0, abs(y - p[1]) - ext[1] - r0)
          96 +                    clear = min(clear, np.hypot(dx, dy))
          97 +                dxy = abs(x - c[0]), abs(y - c[1])
          98 +                clear = min(clear, np.hypot(max(0, dxy[0] - 0.08), max(0, dxy[1] - 0.08)) + 0.02)
          99 +                for bad in self.fail.get(name, []):
         100 +                    if np.hypot(x - bad[0], y - bad[1]) < 0.05:
         101 +                        clear = -1
         102 +                v = min(clear, 0.08) - 0.05 * np.hypot(x - p0[0], y - p0[1])
         103 +                if v > bestv:
         104 +                    bestv, best = v, np.array([x, y])
         105 +        return best
         106 +
         107 +    # ------------------------------------------------------------- planning
         108 +    def _plan_next(self):
         109 +        obs = [n for n in self._obstructions() if self._needs_clearing(n)]
         110 +        if obs:
         111 +            # clear the tallest / closest-to-center first
         112 +            c = self._final_block_xy()
         113 +            obs.sort(key=lambda n: np.hypot(*(self.objs[n][0][:2] - c)))
         114 +            n = obs[0]
         115 +            spot = self._free_spot(n)
         116 +            place_z = TABLE_Z
         117 +            self.task = dict(name=n, dest=spot, surf=place_z, yaw_dest=None)
         118 +        else:
         119 +            rp, rhe = self.objs['target_region']
         120 +            self.task = dict(name='target_block', dest=self._final_block_xy(),
         121 +                             surf=rp[2] + rhe[2], yaw_dest=None)
         122 +        n = self.task['name']
         123 +        p, he = self.objs[n]
         124 +        self.task['yaw'] = self._yaw_for(p[:2])
         125 +        self.task['yaw_place'] = self._match_yaw(self.task['yaw'], self._yaw_for(self.task['dest']))
         126 +        self.phase = 'to_pick'
         127 +        tool = fk(self.base, self.q)[:3, 3]
         128 +        pick_above = np.array([p[0], p[1], SAFE_Z])
         129 +        path = []
         130 +        if tool[2] < SAFE_Z - 0.01:
         131 +            path += self._line(tool, np.array([tool[0], tool[1], SAFE_Z]), 0.05)
         132 +            tool = np.array([tool[0], tool[1], SAFE_Z])
         133 +        path += self._line(tool, pick_above, 0.06)
         134 +        path += self._line(pick_above, np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ]), 0.05)
         135 +        self._set_path(path, self.task['yaw'])
         136 +
         137 +    def _yaw_for(self, xy):
         138 +        mx = self.base[0] + 0.12 * np.cos(self.base[2])
         139 +        my = self.base[1] + 0.12 * np.sin(self.base[2])
         140 +        return np.arctan2(xy[1] - my, xy[0] - mx)
         141 +
         142 +    @staticmethod
         143 +    def _match_yaw(y0, ydes):
         144 +        # object must keep orientation up to pi
         145 +        k = np.round((ydes - y0) / np.pi)
         146 +        return y0 + k * np.pi
         147 +
         148 +    @staticmethod
         149 +    def _line(a, b, step):
         150 +        d = np.linalg.norm(b - a)
         151 +        n = max(1, int(np.ceil(d / step)))
         152 +        return [a + (b - a) * (i / n) for i in range(1, n + 1)]
         153 +
         154 +    def _set_path(self, pts, yaw, yaw_end=None):
         155 +        if yaw_end is None:
         156 +            yaw_end = yaw
         157 +        n = len(pts)
         158 +        self.path = [(p, yaw + (yaw_end - yaw) * (i + 1) / n) for i, p in enumerate(pts)]
         159 +
         160 +    # -------------------------------------------------------------- control
         161 +    def _ik(self, pos, yaw):
         162 +        q, err = ik(self.base, self.q, pos, down_R(yaw), iters=60)
         163 +        for i, lim in JLIM.items():
         164 +            q[i] = np.clip(q[i], -lim, lim)
         165 +        return q, err
         166 +
         167 +    def _track(self):
         168 +        """Return joint delta toward current path, or None when path done."""
         169 +        while self.path:
         170 +            pos, yaw = self.path[0]
         171 +            M = fk(self.base, self.q)
         172 +            final = len(self.path) == 1
         173 +            tol = 5e-4 if final else 0.02
         174 +            e = np.linalg.norm(M[:3, 3] - pos)
         175 +            eo = np.linalg.norm(rot_err(M[:3, :3], down_R(yaw)))
         176 +            if e < tol and (eo < (0.01 if final else 0.1)):
         177 +                self.path.pop(0)
         178 +                continue
         179 +            qt, err = self._ik(pos, yaw)
         180 +            dq = qt - self.q
         181 +            m = np.max(np.abs(dq))
         182 +            if m > MAX_DQ:
         183 +                dq = dq * (MAX_DQ / m)
         184 +            return dq
         185 +        return None
         186 +
         187 +    def _act(self, dq=None, grip=0.0):
         188 +        a = np.zeros(11, dtype=np.float32)
         189 +        if dq is not None:
         190 +            a[3:10] = dq
         191 +        a[10] = grip
         192 +        self.last_q = self.q.copy()
         193 +        self.last_cmd = a.copy()
         194 +        return a
         195 +
         196 +    def get_action(self, state):
         197 +        self._read(state)
         198 +        self.t += 1
         199 +        # detect blocked motion
         200 +        blocked = False
         201 +        if self.last_cmd is not None and np.max(np.abs(self.last_cmd[3:10])) > 1e-6:
         202 +            if np.allclose(self.q, self.last_q, atol=1e-7):
         203 +                blocked = True
         204 +        self.last_cmd = None
         205 +
         206 +        for _ in range(8):
         207 +            a = self._step_fsm(blocked)
         208 +            if a is not None:
         209 +                return a
         210 +            blocked = False
         211 +        return self._act()
         212 +
         213 +    def _step_fsm(self, blocked):
         214 +        ph = self.phase
         215 +        if ph == 'plan':
         216 +            if self.grasped:
         217 +                # holding something unexpectedly: lower & release
         218 +                self.phase = 'release'
         219 +                return None
         220 +            self._plan_next()
         221 +            return None
         222 +        n = self.task['name']
         223 +        if ph == 'to_pick':
         224 +            if blocked:
         225 +                # blocked while approaching: close anyway if near, else lift
         226 +                self.phase = 'grasp'
         227 +                return None
         228 +            dq = self._track()
         229 +            if dq is None:
         230 +                self.phase = 'grasp'
         231 +                return None
         232 +            return self._act(dq)
         233 +        if ph == 'grasp':
         234 +            if self.grasped:
         235 +                self.phase = 'to_place'
         236 +                p, he = self.objs[n]
         237 +                tool = fk(self.base, self.q)[:3, 3]
         238 +                self.grasp_off = tool[2] - p[2]   # tool z above object center
         239 +                dest = self.task['dest']
         240 +                up = np.array([tool[0], tool[1], SAFE_Z])
         241 +                above = np.array([dest[0], dest[1], SAFE_Z])
         242 +                place = np.array([dest[0], dest[1], self.task['surf'] + he[2] + self.grasp_off + PLACE_EPS])
         243 +                pts = self._line(tool, up, 0.05)
         244 +                pts2 = self._line(up, above, 0.06)
         245 +                pts3 = self._line(above, place, 0.05)
         246 +                y0, y1 = self.task['yaw'], self.task['yaw_place']
         247 +                self.path = [(p_, y0) for p_ in pts]
         248 +                k = len(pts2)
         249 +                self.path += [(p_, y0 + (y1 - y0) * (i + 1) / k) for i, p_ in enumerate(pts2)]
         250 +                self.path += [(p_, y1) for p_ in pts3]
         251 +                return None
         252 +            self.wait += 1
         253 +            if self.wait > 3:
         254 +                # grasp failed: re-plan (lift first)
         255 +                self.wait = 0
         256 +                self.phase = 'plan'
         257 +                return None
         258 +            if self.wait == 1:
         259 +                return self._act(grip=-1.0)
         260 +            # nudge down a bit and retry
         261 +            tool = fk(self.base, self.q)[:3, 3]
         262 +            self.path = [(tool - np.array([0, 0, 0.01]), self.task['yaw'])]
         263 +            dq = self._track()
         264 +            self.wait = 0 if dq is None else self.wait
         265 +            return self._act(dq, grip=-1.0)
         266 +        if ph == 'to_place':
         267 +            if not self.grasped:
         268 +                self.phase = 'plan'
         269 +                return None
         270 +            if blocked:
         271 +                self.phase = 'release'
         272 +                return None
         273 +            dq = self._track()
         274 +            if dq is None:
         275 +                self.phase = 'release'
         276 +                return None
         277 +            return self._act(dq)
         278 +        if ph == 'release':
         279 +            if not self.grasped:
         280 +                self.phase = 'retreat'
         281 +                tool = fk(self.base, self.q)[:3, 3]
         282 +                self.path = [(p_, self.task['yaw_place'] if self.task else 0.0)
         283 +                             for p_ in self._line(tool, np.array([tool[0], tool[1], tool[2] + 0.06]), 0.05)]
         284 +                self.wait = 0
         285 +                return None
         286 +            self.wait += 1
         287 +            if self.wait <= 2:
         288 +                return self._act(grip=1.0)
         289 +            # could not release: move down a little
         290 +            self.wait = 0
         291 +            tool = fk(self.base, self.q)[:3, 3]
         292 +            yaw = self.task['yaw_place'] if self.task else 0.0
         293 +            self.path = [(tool - np.array([0, 0, 0.003]), yaw)]
         294 +            dq = self._track()
         295 +            return self._act(dq, grip=1.0)
         296 +        if ph == 'retreat':
         297 +            dq = self._track()
         298 +            if dq is None or blocked:
         299 +                self.phase = 'plan'
         300 +                return None
         301 +            return self._act(dq)
         302 +        return self._act()
diff --git a/gm_-0.02.txt b/gm_-0.02.txt
new file mode 100644
index 0000000..37a70f5
--- /dev/null
+++ b/gm_-0.02.txt
@@ -0,0 +1,8 @@
           1 +dz=-0.02 yaw=0.0 he=[0.028 0.039 0.025] (rows dx, cols dy)
           2 +xxxxxxx
           3 +xxxxxxx
           4 +xxxxxxx
           5 +xxx..x.
           6 +xxxxxxx
           7 +xxxxxxx
           8 +xxxxxx.
diff --git a/gm_-0.04.txt b/gm_-0.04.txt
new file mode 100644
index 0000000..e69de29
diff --git a/gm_0.0.txt b/gm_0.0.txt
new file mode 100644
index 0000000..e69de29
diff --git a/gm_0.02.txt b/gm_0.02.txt
new file mode 100644
index 0000000..e69de29
diff --git a/grasp_map.py b/grasp_map.py
new file mode 100644
index 0000000..5548e89
--- /dev/null
+++ b/grasp_map.py
@@ -0,0 +1,16 @@
           1 +from th import *
           2 +import sys
           3 +dz=float(sys.argv[1]); yaw=float(sys.argv[2])
           4 +h=H(1); p=h.pose('target_block'); he=h.he('target_block'); top=p[2]+he[2]
           5 +res=[]
           6 +for dx in np.arange(-0.06,0.061,0.02):
           7 +  row=''
           8 +  for dy in np.arange(-0.06,0.061,0.02):
           9 +    h.goto([p[0],p[1],top+0.1],yaw)
          10 +    ok,_=h.goto([p[0]+dx,p[1]+dy,top+dz],yaw)
          11 +    h.grip(-1); g=h.grasped(); row+=('G' if g else '.') if ok else 'x'
          12 +    h.grip(1)
          13 +    if g:
          14 +        h=H(1)
          15 +  res.append(row)
          16 +print(f'dz={dz} yaw={yaw} he={he.round(3)} (rows dx, cols dy)'); print('\n'.join(res))
diff --git a/release2.py b/release2.py
new file mode 100644
index 0000000..51ae87a
--- /dev/null
+++ b/release2.py
@@ -0,0 +1,15 @@
           1 +from th import *
           2 +h=H(1); p=h.pose('target_block'); he=h.he('target_block'); top=p[2]+he[2]
           3 +h.goto([p[0],p[1],top+0.1],0)
           4 +h.goto([p[0],p[1],top-0.01],0); h.grip(-1); print('grasp',h.grasped())
           5 +tgt=[p[0]+0.08,p[1]-0.15]
           6 +ok,_=h.goto([tgt[0],tgt[1],top+0.1],0); print('moved',ok, h.pose('target_block')[:3].round(4))
           7 +z=top+0.1
           8 +while z>0.0:
           9 +    z-=0.005
          10 +    ok,e=h.goto([tgt[0],tgt[1],z],0)
          11 +    if not ok:
          12 +        print('blocked at tool z',z,'block',h.pose('target_block')[:3].round(4), 'tool', h.tool()[:3,3].round(4)); break
          13 +for i in range(2):
          14 +    h.grip(1); print('open', h.grasped(), h.pose('target_block')[:3].round(4))
          15 +h.goto([tgt[0],tgt[1],top+0.1],0); print('after lift, block', h.pose('target_block')[:3].round(4), h.grasped())
diff --git a/release_test.py b/release_test.py
new file mode 100644
index 0000000..ef15d1a
--- /dev/null
+++ b/release_test.py
@@ -0,0 +1,19 @@
           1 +from th import *
           2 +h=H(1); p=h.pose('target_block'); he=h.he('target_block'); top=p[2]+he[2]
           3 +h.goto([p[0],p[1],top+0.1],0)
           4 +for dz in [-0.01,-0.02,-0.03]:
           5 +    h.goto([p[0],p[1],top+dz],0); h.grip(-1)
           6 +    if h.grasped(): break
           7 +print('grasped at dz',dz,h.grasped(), h.obs.get(h.R,'grasp_tf_z'))
           8 +h.goto([p[0],p[1],top+0.1],0); print('lifted block', h.pose('target_block')[:3].round(4))
           9 +h.goto([p[0]+0.05,p[1]-0.1,top+0.1],0)
          10 +b1=h.pose('target_block'); h.grip(1); b2=h.pose('target_block')
          11 +print('release in air: before',b1[:3].round(4),'after',b2[:3].round(4),'grasp',h.grasped())
          12 +for i in range(3): h.step(np.zeros(11))
          13 +print('after 3 steps', h.pose('target_block')[:3].round(4))
          14 +for i in range(3):
          15 +    h.grip(1); print('open again', h.grasped())
          16 +h.goto([p[0]+0.05,p[1]-0.1,top+0.0],0); print('lowered', h.pose('target_block')[:3].round(4))
          17 +h.grip(1); print('open near table', h.grasped(), h.pose('target_block')[:3].round(4))
          18 +h.goto([p[0]+0.05,p[1]-0.1,top-0.01],0); print('lowered more', h.pose('target_block')[:3].round(4))
          19 +h.grip(1); print('open near table', h.grasped(), h.pose('target_block')[:3].round(4))
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..5ad95bb
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,20 @@
           1 +import sys, time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +def run(seed, verbose=False):
           5 +    env = make_env()
           6 +    obs, info = env.reset(seed=seed)
           7 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           8 +    t0 = time.time(); ap.reset(obs, info); tc = 0
           9 +    for t in range(env.max_steps):
          10 +        t1 = time.time(); a = ap.get_action(obs); tc += time.time() - t1
          11 +        obs, r, te, tr, info = env.step(a)
          12 +        if verbose: print(t, ap.phase, ap.task['name'] if ap.task else None)
          13 +        if te: env.close(); return True, t + 1, tc, ap
          14 +        if tr: break
          15 +    env.close(); return False, env.max_steps, tc, ap
          16 +if __name__ == '__main__':
          17 +    seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
          18 +    for s in seeds:
          19 +        ok, n, tc, ap = run(s)
          20 +        print(f'seed {s}: success={ok} steps={n} compute={tc:.1f}s phase={ap.phase} task={ap.task["name"] if ap.task else None}', flush=True)
diff --git a/th.py b/th.py
new file mode 100644
index 0000000..727af6c
--- /dev/null
+++ b/th.py
@@ -0,0 +1,34 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +import numpy as np
           4 +GF=['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']
           5 +BF=['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']
           6 +class H:
           7 +    def __init__(self, seed, env=None):
           8 +        self.env = env or make_env(); self.obs,_ = self.env.reset(seed=seed)
           9 +        self.R = self.obs.get_object_from_name('robot'); self.n=0; self.done=False
          10 +    def o(self, name): return self.obs.get_object_from_name(name)
          11 +    def g(self, name, f): return self.obs.get(self.o(name), f)
          12 +    def q(self): return np.array([self.obs.get(self.R,f'joint_{i}') for i in range(1,8)])
          13 +    def base(self): return tuple(self.obs.get(self.R,f) for f in ('pos_base_x','pos_base_y','pos_base_rot'))
          14 +    def tool(self): return fk(self.base(), self.q())
          15 +    def step(self, a):
          16 +        self.obs, r, te, tr, _ = self.env.step(np.asarray(a,dtype=np.float32)); self.n+=1
          17 +        if te: self.done=True
          18 +        return te
          19 +    def grip(self, v):
          20 +        a=np.zeros(11); a[10]=v; return self.step(a)
          21 +    def goto_q(self, qt, grip=0.0, maxsteps=60):
          22 +        for _ in range(maxsteps):
          23 +            q=self.q(); d=qt-q
          24 +            if np.max(np.abs(d))<1e-5: return True
          25 +            a=np.zeros(11); a[3:10]=np.clip(d,-0.2,0.2); a[10]=grip
          26 +            self.step(a)
          27 +            if np.allclose(self.q(),q): return False
          28 +        return False
          29 +    def goto(self, pos, yaw=0.0):
          30 +        qt,e=ik(self.base(), self.q(), np.asarray(pos,float), down_R(yaw))
          31 +        return self.goto_q(qt), e
          32 +    def grasped(self): return self.obs.get(self.R,'grasp_active')>0.5
          33 +    def pose(self, name): return np.array([self.g(name,f) for f in BF])
          34 +    def he(self, name): return np.array([self.g(name,'half_extent_'+c) for c in 'xyz'])
diff --git a/zs1.txt b/zs1.txt
new file mode 100644
index 0000000..ff5700a
--- /dev/null
+++ b/zs1.txt
@@ -0,0 +1 @@
           1 +1 target_block yaw 0.0 d 0.0 0.0 he [0.028 0.039 0.025] +0.120:. +0.110:. +0.100:. +0.090:. +0.080:. +0.070:. +0.060:. +0.050:. +0.040:. +0.030:G tf=[ 0.    -0.     0.055]
diff --git a/zs2.txt b/zs2.txt
new file mode 100644
index 0000000..11f7e61
--- /dev/null
+++ b/zs2.txt
@@ -0,0 +1 @@
           1 +1 obstruction0 yaw 0.0 d 0.0 0.0 he [0.013 0.018 0.016] +0.120:. +0.110:. +0.100:. +0.090:. +0.080:. +0.070:. +0.060:. +0.050:. +0.040:. +0.030:G tf=[ 0.    -0.     0.046]
diff --git a/zs3.txt b/zs3.txt
new file mode 100644
index 0000000..76698ef
--- /dev/null
+++ b/zs3.txt
@@ -0,0 +1 @@
           1 +1 target_block yaw 0.0 d 0.05 0.0 he [0.028 0.039 0.025] +0.050:. +0.045:. +0.040:. +0.035:. +0.030:. +0.025:X
diff --git a/zs4.txt b/zs4.txt
new file mode 100644
index 0000000..1ab5452
--- /dev/null
+++ b/zs4.txt
@@ -0,0 +1 @@
           1 +1 target_block yaw 0.0 d 0.0 0.05 he [0.028 0.039 0.025] +0.050:. +0.045:. +0.040:. +0.035:. +0.030:. +0.025:. +0.020:. +0.015:. +0.010:. +0.005:. +0.000:. -0.005:. -0.010:. -0.015:. -0.020:. -0.025:X
diff --git a/zs5.txt b/zs5.txt
new file mode 100644
index 0000000..1bf7840
--- /dev/null
+++ b/zs5.txt
@@ -0,0 +1 @@
           1 +1 target_block yaw 0.0 d 0.03 0.0 he [0.028 0.039 0.025] +0.050:. +0.045:. +0.040:. +0.035:. +0.030:G tf=[-0.03  -0.     0.055]
diff --git a/zs6.txt b/zs6.txt
new file mode 100644
index 0000000..4808a13
--- /dev/null
+++ b/zs6.txt
@@ -0,0 +1 @@
           1 +1 target_block yaw 0.0 d 0.0 0.04 he [0.028 0.039 0.025] +0.050:. +0.045:. +0.040:. +0.035:. +0.030:G tf=[0.    0.04  0.055]
diff --git a/zs7.txt b/zs7.txt
new file mode 100644
index 0000000..6bca6a5
--- /dev/null
+++ b/zs7.txt
@@ -0,0 +1 @@
           1 +1 target_block yaw 0.0 d 0.02 0.0 he [0.028 0.039 0.025] +0.030:G tf=[-0.02  -0.     0.055]
diff --git a/zs8.txt b/zs8.txt
new file mode 100644
index 0000000..a6d3a5b
--- /dev/null
+++ b/zs8.txt
@@ -0,0 +1 @@
           1 +1 target_block yaw 0.0 d 0.0 0.02 he [0.028 0.039 0.025] +0.030:G tf=[0.    0.02  0.055]
diff --git a/zscan.py b/zscan.py
new file mode 100644
index 0000000..518551b
--- /dev/null
+++ b/zscan.py
@@ -0,0 +1,13 @@
           1 +from th import *
           2 +import sys
           3 +seed=int(sys.argv[1]); name=sys.argv[2]; yaw=float(sys.argv[3]); dx=float(sys.argv[4]); dy=float(sys.argv[5])
           4 +h=H(seed); p=h.pose(name); he=h.he(name); top=p[2]+he[2]
           5 +h.goto([p[0]+dx,p[1]+dy,top+float(sys.argv[6])+0.02],yaw)
           6 +out=[]
           7 +for dz in np.arange(float(sys.argv[6]),-0.035,-float(sys.argv[7])):
           8 +    ok,_=h.goto([p[0]+dx,p[1]+dy,top+dz],yaw)
           9 +    if not ok: out.append(f'{dz:+.3f}:X'); break
          10 +    h.grip(-1)
          11 +    if h.grasped(): out.append(f'{dz:+.3f}:G tf={np.array([h.obs.get(h.R,f) for f in GF[:3]]).round(3)}'); break
          12 +    out.append(f'{dz:+.3f}:.')
          13 +print(seed,name,'yaw',yaw,'d',dx,dy,'he',he.round(3),' '.join(out))
```

</details>

<a id="C004"></a>
### C004 · Yaw selection avoiding neighbors, grasp retry

Commit `e7216948a63e629ba0d4321fe892e403158cdb7c`; parents: f57fd5548266345cdd0e1a723a19341328353de5. Recorded author date: 2026-09-28T19:40:47+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0247](01_timeline.md#E0247): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_e721694_approach.py) · [Exact all-file diff](evidence/diffs/C004_e721694.diff)

[Previous saved controller snapshot](evidence/versions/C003_f57fd55_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6f1e4fd..62d9060 100644
--- a/approach.py
+++ b/approach.py
@@ -8,7 +8,7 @@ TABLE_Z = 0.075
    8      8  TABLE_X = (0.10, 0.50)
    9      9  TABLE_Y = (-0.40, 0.40)
   10     10  SAFE_Z = 0.30          # tool height for transport
   11        -GRASP_DZ = 0.015       # tool height above object top when closing
          11 +GRASP_DZ = 0.025       # tool height above object top when closing
   12     12  PLACE_EPS = 0.0015     # clearance above support surface when releasing
   13     13  MAX_DQ = 0.2
   14     14  JLIM = {1: 2.41, 3: 2.66, 5: 2.23}   # limited joints (0-indexed): 2,4,6 in 1-index
@@ -121,7 +121,8 @@ class GeneratedApproach:
  121    121                               surf=rp[2] + rhe[2], yaw_dest=None)
  122    122          n = self.task['name']
  123    123          p, he = self.objs[n]
  124        -        self.task['yaw'] = self._yaw_for(p[:2])
         124 +        att = self.fail.get(('grasp', n), 0)
         125 +        self.task['yaw'] = self._choose_yaw(n, p[:2], p[2] + he[2] + GRASP_DZ - 0.05, att)
  125    126          self.task['yaw_place'] = self._match_yaw(self.task['yaw'], self._yaw_for(self.task['dest']))
  126    127          self.phase = 'to_pick'
  127    128          tool = fk(self.base, self.q)[:3, 3]
@@ -134,6 +135,44 @@ class GeneratedApproach:
  134    135          path += self._line(pick_above, np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ]), 0.05)
  135    136          self._set_path(path, self.task['yaw'])
  136    137  
         138 +    def _footprint_hits(self, name, xy, yaw, bottom):
         139 +        """Count collisions of gripper footprint (at xy, yaw, lowest z=bottom) with other objects."""
         140 +        c, s_ = np.cos(yaw), np.sin(yaw)
         141 +        ax = np.array([c, s_]); ay = np.array([-s_, c])
         142 +        gx, gy = 0.065, 0.03
         143 +        hits = 0.0
         144 +        for n, (p, he) in self.objs.items():
         145 +            if n == name or n == 'target_region':
         146 +                continue
         147 +            if p[2] + he[2] < bottom:
         148 +                continue
         149 +            d = p[:2] - xy
         150 +            # SAT between rotated rect (gx,gy) and AABB he
         151 +            sep = False
         152 +            for axis, r1 in ((np.array([1.0, 0]), abs(ax[0]) * gx + abs(ay[0]) * gy),
         153 +                             (np.array([0, 1.0]), abs(ax[1]) * gx + abs(ay[1]) * gy)):
         154 +                if abs(d @ axis) > r1 + (he[0] if axis[0] else he[1]):
         155 +                    sep = True
         156 +            for axis, r1 in ((ax, gx), (ay, gy)):
         157 +                r2 = abs(axis[0]) * he[0] + abs(axis[1]) * he[1]
         158 +                if abs(d @ axis) > r1 + r2:
         159 +                    sep = True
         160 +            if not sep:
         161 +                hits += 1
         162 +        return hits
         163 +
         164 +    def _choose_yaw(self, name, xy, bottom, attempt=0):
         165 +        rad = self._yaw_for(xy)
         166 +        best, bv = rad, 1e9
         167 +        for k in range(12):
         168 +            y = rad + k * np.pi / 12
         169 +            y = y if k < 7 else y - np.pi   # prefer small deviation either side
         170 +            dev = min(abs(wrap(y - rad)), abs(wrap(y - rad + np.pi)))
         171 +            v = self._footprint_hits(name, xy, y, bottom) * 10 + dev
         172 +            if v < bv:
         173 +                bv, best = v, y
         174 +        return best + attempt * np.pi / 2
         175 +
  137    176      def _yaw_for(self, xy):
  138    177          mx = self.base[0] + 0.12 * np.cos(self.base[2])
  139    178          my = self.base[1] + 0.12 * np.sin(self.base[2])
@@ -250,19 +289,12 @@ class GeneratedApproach:
  250    289                  self.path += [(p_, y1) for p_ in pts3]
  251    290                  return None
  252    291              self.wait += 1
  253        -            if self.wait > 3:
  254        -                # grasp failed: re-plan (lift first)
  255        -                self.wait = 0
  256        -                self.phase = 'plan'
  257        -                return None
  258    292              if self.wait == 1:
  259    293                  return self._act(grip=-1.0)
  260        -            # nudge down a bit and retry
  261        -            tool = fk(self.base, self.q)[:3, 3]
  262        -            self.path = [(tool - np.array([0, 0, 0.01]), self.task['yaw'])]
  263        -            dq = self._track()
  264        -            self.wait = 0 if dq is None else self.wait
  265        -            return self._act(dq, grip=-1.0)
         294 +            self.wait = 0
         295 +            self.fail[('grasp', n)] = self.fail.get(('grasp', n), 0) + 1
         296 +            self.phase = 'plan'
         297 +            return None
  266    298          if ph == 'to_place':
  267    299              if not self.grasped:
  268    300                  self.phase = 'plan'
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..6b42f0a
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,15 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import fk
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2])
           6 +env = make_env(); obs, info = env.reset(seed=seed)
           7 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +for t in range(N):
           9 +    a = ap.get_action(obs)
          10 +    obs, r, te, tr, info = env.step(a)
          11 +    n = ap.task['name'] if ap.task else None
          12 +    tool = fk(ap.base, ap.q)[:3,3]
          13 +    top = ap.objs[n][0][2]+ap.objs[n][1][2] if n else 0
          14 +    print(t, ap.phase, n, 'tool', tool.round(3), 'obj', ap.objs[n][0].round(3) if n else '', 'top', round(top,3), 'grip', a[10], 'g', ap.grasped, 'dq', np.abs(a[3:10]).max().round(3))
          15 +    if te: print('DONE'); break
diff --git a/ptest.py b/ptest.py
new file mode 100644
index 0000000..2f97a1e
--- /dev/null
+++ b/ptest.py
@@ -0,0 +1,16 @@
           1 +import sys
           2 +from multiprocessing import Pool
           3 +from test_approach import run
           4 +def f(s):
           5 +    try:
           6 +        ok,n,tc,ap=run(s); return (s,ok,n,tc,ap.phase,ap.task['name'] if ap.task else None, ap.objs and len(ap._obstructions()))
           7 +    except Exception as e:
           8 +        return (s,False,-1,0,'EXC',repr(e)[:200],0)
           9 +if __name__=='__main__':
          10 +    a,b=int(sys.argv[1]),int(sys.argv[2]); npar=int(sys.argv[3]) if len(sys.argv)>3 else 8
          11 +    with Pool(npar) as p:
          12 +        res=p.map(f, range(a,b))
          13 +    for r in res:
          14 +        if not r[1]: print('FAIL', r)
          15 +    ok=[r for r in res if r[1]]
          16 +    print(f'success {len(ok)}/{len(res)}  mean steps(success) {sum(r[2] for r in ok)/max(1,len(ok)):.1f}  max compute {max(r[3] for r in res):.1f}s')
```

</details>

<a id="C005"></a>
### C005 · Axis-aligned yaw choice, step halving on block

Commit `47df3f38ace3ac429c3672cdc2b2902f4e83588c`; parents: e7216948a63e629ba0d4321fe892e403158cdb7c. Recorded author date: 2026-09-28T19:45:22+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0283](01_timeline.md#E0283): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_47df3f3_approach.py) · [Exact all-file diff](evidence/diffs/C005_47df3f3.diff)

[Previous saved controller snapshot](evidence/versions/C004_e721694_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 62d9060..00dd1c0 100644
--- a/approach.py
+++ b/approach.py
@@ -8,7 +8,7 @@ TABLE_Z = 0.075
    8      8  TABLE_X = (0.10, 0.50)
    9      9  TABLE_Y = (-0.40, 0.40)
   10     10  SAFE_Z = 0.30          # tool height for transport
   11        -GRASP_DZ = 0.025       # tool height above object top when closing
          11 +GRASP_DZ = 0.028       # tool height above object top when closing
   12     12  PLACE_EPS = 0.0015     # clearance above support surface when releasing
   13     13  MAX_DQ = 0.2
   14     14  JLIM = {1: 2.41, 3: 2.66, 5: 2.23}   # limited joints (0-indexed): 2,4,6 in 1-index
@@ -52,6 +52,7 @@ class GeneratedApproach:
   52     52          self.last_q = None
   53     53          self.last_cmd = None
   54     54          self.blocked = 0
          55 +        self.scale = 1.0
   55     56          self.fail = {}
   56     57          self.t = 0
   57     58          self.wait = 0
@@ -162,16 +163,19 @@ class GeneratedApproach:
  162    163          return hits
  163    164  
  164    165      def _choose_yaw(self, name, xy, bottom, attempt=0):
         166 +        """Object-axis-aligned yaw; fingers (tool x) along the smaller extent
         167 +        when possible, avoiding neighbours."""
         168 +        p, he = self.objs[name]
  165    169          rad = self._yaw_for(xy)
  166        -        best, bv = rad, 1e9
  167        -        for k in range(12):
  168        -            y = rad + k * np.pi / 12
  169        -            y = y if k < 7 else y - np.pi   # prefer small deviation either side
  170        -            dev = min(abs(wrap(y - rad)), abs(wrap(y - rad + np.pi)))
  171        -            v = self._footprint_hits(name, xy, y, bottom) * 10 + dev
  172        -            if v < bv:
  173        -                bv, best = v, y
  174        -        return best + attempt * np.pi / 2
         170 +        cands = []
         171 +        for k in range(4):
         172 +            y = k * np.pi / 2
         173 +            finger_ext = he[0] if k % 2 == 0 else he[1]
         174 +            hits = self._footprint_hits(name, xy, y, bottom)
         175 +            dev = abs(wrap(y - rad))
         176 +            cands.append((hits * 10 + (finger_ext > 0.036) * 5 + finger_ext * 10 + 0.01 * dev, y))
         177 +        cands.sort()
         178 +        return cands[attempt % 4][1]
  175    179  
  176    180      def _yaw_for(self, xy):
  177    181          mx = self.base[0] + 0.12 * np.cos(self.base[2])
@@ -220,7 +224,7 @@ class GeneratedApproach:
  220    224              m = np.max(np.abs(dq))
  221    225              if m > MAX_DQ:
  222    226                  dq = dq * (MAX_DQ / m)
  223        -            return dq
         227 +            return dq * self.scale
  224    228          return None
  225    229  
  226    230      def _act(self, dq=None, grip=0.0):
@@ -240,6 +244,13 @@ class GeneratedApproach:
  240    244          if self.last_cmd is not None and np.max(np.abs(self.last_cmd[3:10])) > 1e-6:
  241    245              if np.allclose(self.q, self.last_q, atol=1e-7):
  242    246                  blocked = True
         247 +        if self.last_cmd is not None and not blocked:
         248 +            self.scale = 1.0
         249 +        if blocked and self.scale > 1.0 / 16:
         250 +            self.scale *= 0.5
         251 +            blocked = False
         252 +        elif blocked:
         253 +            self.scale = 1.0
  243    254          self.last_cmd = None
  244    255  
  245    256          for _ in range(8):
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..bdcbabc
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,14 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import fk
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2])
           6 +env = make_env(); obs, info = env.reset(seed=seed)
           7 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +for t in range(N):
           9 +    a = ap.get_action(obs); obs, *_ = env.step(a)
          10 +ap._read(obs)
          11 +np.set_printoptions(precision=3, suppress=True)
          12 +print('q', ap.q, 'base', ap.base, 'last a', a)
          13 +for n,(p,he) in ap.objs.items(): print(n, p, he)
          14 +qt,e = ap._ik(np.array([0.337,-0.362,0.15]), ap.task['yaw']); print('ik target q', qt, e, 'yaw', ap.task['yaw'])
```

</details>

<a id="C006"></a>
### C006 · Dynamic safe height, larger waypoint steps; incremental test runner

Commit `e143b4c6f37eac90f6037833cc7a0a2d951a9dfc`; parents: 47df3f38ace3ac429c3672cdc2b2902f4e83588c. Recorded author date: 2026-09-28T20:23:52+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0415](01_timeline.md#E0415): commit title in command; output may not confirm creation.
- [E0418](01_timeline.md#E0418): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_e143b4c_approach.py) · [Exact all-file diff](evidence/diffs/C006_e143b4c.diff)

[Previous saved controller snapshot](evidence/versions/C005_47df3f3_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 00dd1c0..0e1a31f 100644
--- a/approach.py
+++ b/approach.py
@@ -7,7 +7,9 @@ from kin import fk, ik, down_R, jac, rot_err
    7      7  TABLE_Z = 0.075
    8      8  TABLE_X = (0.10, 0.50)
    9      9  TABLE_Y = (-0.40, 0.40)
   10        -SAFE_Z = 0.30          # tool height for transport
          10 +SAFE_MARGIN = 0.03
          11 +VSTEP = 0.08
          12 +HSTEP = 0.10
   11     13  GRASP_DZ = 0.028       # tool height above object top when closing
   12     14  PLACE_EPS = 0.0015     # clearance above support surface when releasing
   13     15  MAX_DQ = 0.2
@@ -127,13 +129,14 @@ class GeneratedApproach:
  127    129          self.task['yaw_place'] = self._match_yaw(self.task['yaw'], self._yaw_for(self.task['dest']))
  128    130          self.phase = 'to_pick'
  129    131          tool = fk(self.base, self.q)[:3, 3]
  130        -        pick_above = np.array([p[0], p[1], SAFE_Z])
         132 +        sz = self._safe_z(None, 0.05)
         133 +        pick_above = np.array([p[0], p[1], sz])
  131    134          path = []
  132        -        if tool[2] < SAFE_Z - 0.01:
  133        -            path += self._line(tool, np.array([tool[0], tool[1], SAFE_Z]), 0.05)
  134        -            tool = np.array([tool[0], tool[1], SAFE_Z])
  135        -        path += self._line(tool, pick_above, 0.06)
  136        -        path += self._line(pick_above, np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ]), 0.05)
         135 +        if tool[2] < sz - 0.01:
         136 +            path += self._line(tool, np.array([tool[0], tool[1], sz]), VSTEP)
         137 +            tool = np.array([tool[0], tool[1], sz])
         138 +        path += self._line(tool, pick_above, HSTEP)
         139 +        path += self._line(pick_above, np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ]), VSTEP)
  137    140          self._set_path(path, self.task['yaw'])
  138    141  
  139    142      def _footprint_hits(self, name, xy, yaw, bottom):
@@ -188,6 +191,13 @@ class GeneratedApproach:
  188    191          k = np.round((ydes - y0) / np.pi)
  189    192          return y0 + k * np.pi
  190    193  
         194 +    def _safe_z(self, held, depth):
         195 +        top = TABLE_Z
         196 +        for n, (p, he) in self.objs.items():
         197 +            if n != held:
         198 +                top = max(top, p[2] + he[2])
         199 +        return max(top + depth + SAFE_MARGIN, 0.18)
         200 +
  191    201      @staticmethod
  192    202      def _line(a, b, step):
  193    203          d = np.linalg.norm(b - a)
@@ -213,7 +223,7 @@ class GeneratedApproach:
  213    223              pos, yaw = self.path[0]
  214    224              M = fk(self.base, self.q)
  215    225              final = len(self.path) == 1
  216        -            tol = 5e-4 if final else 0.02
         226 +            tol = 5e-4 if final else 0.03
  217    227              e = np.linalg.norm(M[:3, 3] - pos)
  218    228              eo = np.linalg.norm(rot_err(M[:3, :3], down_R(yaw)))
  219    229              if e < tol and (eo < (0.01 if final else 0.1)):
@@ -287,12 +297,13 @@ class GeneratedApproach:
  287    297                  tool = fk(self.base, self.q)[:3, 3]
  288    298                  self.grasp_off = tool[2] - p[2]   # tool z above object center
  289    299                  dest = self.task['dest']
  290        -                up = np.array([tool[0], tool[1], SAFE_Z])
  291        -                above = np.array([dest[0], dest[1], SAFE_Z])
         300 +                sz = self._safe_z(n, self.grasp_off + he[2])
         301 +                up = np.array([tool[0], tool[1], sz])
         302 +                above = np.array([dest[0], dest[1], sz])
  292    303                  place = np.array([dest[0], dest[1], self.task['surf'] + he[2] + self.grasp_off + PLACE_EPS])
  293        -                pts = self._line(tool, up, 0.05)
  294        -                pts2 = self._line(up, above, 0.06)
  295        -                pts3 = self._line(above, place, 0.05)
         304 +                pts = self._line(tool, up, VSTEP)
         305 +                pts2 = self._line(up, above, HSTEP)
         306 +                pts3 = self._line(above, place, VSTEP)
  296    307                  y0, y1 = self.task['yaw'], self.task['yaw_place']
  297    308                  self.path = [(p_, y0) for p_ in pts]
  298    309                  k = len(pts2)
diff --git a/r_def.txt b/r_def.txt
new file mode 100644
index 0000000..e69de29
diff --git a/r_oc5.txt b/r_oc5.txt
new file mode 100644
index 0000000..e69de29
diff --git a/r_oc8.txt b/r_oc8.txt
new file mode 100644
index 0000000..e69de29
diff --git a/test_approach.py b/test_approach.py
index 5ad95bb..489a6cd 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -1,9 +1,11 @@
    1      1  import sys, time, numpy as np
    2      2  from env_client import make_env
    3      3  from approach import GeneratedApproach
           4 +import os
           5 +OC=os.environ.get('OC')
    4      6  def run(seed, verbose=False):
    5      7      env = make_env()
    6        -    obs, info = env.reset(seed=seed)
           8 +    obs, info = env.reset(seed=seed, options={'object_count': int(OC)} if OC else None)
    7      9      ap = GeneratedApproach(env.action_space, env.observation_space, {})
    8     10      t0 = time.time(); ap.reset(obs, info); tc = 0
    9     11      for t in range(env.max_steps):
```

</details>

<a id="C007"></a>
### C007 · incremental test runner

Commit `105ef1d65c027dac1e464e210356efdec660a87a`; parents: e143b4c6f37eac90f6037833cc7a0a2d951a9dfc. Recorded author date: 2026-09-28T20:27:14+02:00.

File roles (automatic): diagnostic/test.

- [E0415](01_timeline.md#E0415): commit title in command; output may not confirm creation.
- [E0418](01_timeline.md#E0418): commit title in command; output may not confirm creation.
- [E0431](01_timeline.md#E0431): commit title in command; output may not confirm creation.
- [E0446](01_timeline.md#E0446): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C007_105ef1d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/ptest.py b/ptest.py
index 2f97a1e..82672e1 100644
--- a/ptest.py
+++ b/ptest.py
@@ -1,16 +1,27 @@
    1        -import sys
           1 +import sys, time
    2      2  from multiprocessing import Pool
    3      3  from test_approach import run
           4 +
           5 +
    4      6  def f(s):
           7 +    t = time.time()
    5      8      try:
    6        -        ok,n,tc,ap=run(s); return (s,ok,n,tc,ap.phase,ap.task['name'] if ap.task else None, ap.objs and len(ap._obstructions()))
           9 +        ok, n, tc, ap = run(s)
          10 +        return (s, ok, n, round(tc, 1), round(time.time() - t), ap.phase,
          11 +                ap.task['name'] if ap.task else None, len(ap._obstructions()))
    7     12      except Exception as e:
    8        -        return (s,False,-1,0,'EXC',repr(e)[:200],0)
    9        -if __name__=='__main__':
   10        -    a,b=int(sys.argv[1]),int(sys.argv[2]); npar=int(sys.argv[3]) if len(sys.argv)>3 else 8
          13 +        return (s, False, -1, 0, 0, 'EXC', repr(e)[:200], 0)
          14 +
          15 +
          16 +if __name__ == '__main__':
          17 +    a, b = int(sys.argv[1]), int(sys.argv[2])
          18 +    npar = int(sys.argv[3]) if len(sys.argv) > 3 else 8
          19 +    res = []
   11     20      with Pool(npar) as p:
   12        -        res=p.map(f, range(a,b))
   13        -    for r in res:
   14        -        if not r[1]: print('FAIL', r)
   15        -    ok=[r for r in res if r[1]]
   16        -    print(f'success {len(ok)}/{len(res)}  mean steps(success) {sum(r[2] for r in ok)/max(1,len(ok)):.1f}  max compute {max(r[3] for r in res):.1f}s')
          21 +        for r in p.imap_unordered(f, range(a, b)):
          22 +            res.append(r)
          23 +            print(('ok  ' if r[1] else 'FAIL'), r, flush=True)
          24 +    ok = [r for r in res if r[1]]
          25 +    print(f'success {len(ok)}/{len(res)}  mean steps(success) '
          26 +          f'{sum(r[2] for r in ok) / max(1, len(ok)):.1f}  max compute '
          27 +          f'{max(r[3] for r in res):.1f}s', flush=True)
```

</details>

<a id="C008"></a>
### C008 · Yaw: minimize rotation from current tool yaw, keep yaw at place

Commit `65e3006e2082ab2aa0a18e4113da87b0fd74ebf4`; parents: 105ef1d65c027dac1e464e210356efdec660a87a. Recorded author date: 2026-09-28T20:33:03+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0469](01_timeline.md#E0469): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_65e3006_approach.py) · [Exact all-file diff](evidence/diffs/C008_65e3006.diff)

[Previous saved controller snapshot](evidence/versions/C006_e143b4c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0e1a31f..5d9c068 100644
--- a/approach.py
+++ b/approach.py
@@ -126,7 +126,7 @@ class GeneratedApproach:
  126    126          p, he = self.objs[n]
  127    127          att = self.fail.get(('grasp', n), 0)
  128    128          self.task['yaw'] = self._choose_yaw(n, p[:2], p[2] + he[2] + GRASP_DZ - 0.05, att)
  129        -        self.task['yaw_place'] = self._match_yaw(self.task['yaw'], self._yaw_for(self.task['dest']))
         129 +        self.task['yaw_place'] = self.task['yaw']
  130    130          self.phase = 'to_pick'
  131    131          tool = fk(self.base, self.q)[:3, 3]
  132    132          sz = self._safe_z(None, 0.05)
@@ -169,14 +169,18 @@ class GeneratedApproach:
  169    169          """Object-axis-aligned yaw; fingers (tool x) along the smaller extent
  170    170          when possible, avoiding neighbours."""
  171    171          p, he = self.objs[name]
  172        -        rad = self._yaw_for(xy)
         172 +        M = fk(self.base, self.q)
         173 +        cur = np.arctan2(M[1, 0], M[0, 0])
  173    174          cands = []
  174    175          for k in range(4):
  175    176              y = k * np.pi / 2
  176    177              finger_ext = he[0] if k % 2 == 0 else he[1]
  177    178              hits = self._footprint_hits(name, xy, y, bottom)
  178        -            dev = abs(wrap(y - rad))
  179        -            cands.append((hits * 10 + (finger_ext > 0.036) * 5 + finger_ext * 10 + 0.01 * dev, y))
         179 +            y = cur + wrap(y - cur)
         180 +            if abs(wrap(y + np.pi - cur)) < abs(y - cur):
         181 +                y = cur + wrap(y + np.pi - cur)
         182 +            dev = abs(y - cur)
         183 +            cands.append((hits * 10 + (finger_ext > 0.036) * 5 + finger_ext * 10 + 0.3 * dev, y))
  180    184          cands.sort()
  181    185          return cands[attempt % 4][1]
  182    186  
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..0e96f4b
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,13 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import fk
           5 +seed=int(sys.argv[1]); oc=int(sys.argv[2]) if len(sys.argv)>2 else None
           6 +env = make_env(); obs, info = env.reset(seed=seed, options={'object_count':oc} if oc is not None else None)
           7 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +for n,(p,he) in ap.objs.items(): print(n, p.round(3), he.round(3))
           9 +for t in range(400):
          10 +    a = ap.get_action(obs); obs, r, te, *_ = env.step(a)
          11 +    tool = fk(ap.base, ap.q)[:3,3]
          12 +    print(t, ap.phase[:6], (ap.task or {}).get('name','')[-6:], tool.round(3), 'sc', ap.scale, 'g', int(ap.grasped), 'gr', a[10], 'np', len(ap.path), 'dq', np.abs(a[3:10]).max().round(2))
          13 +    if te: print('DONE', t+1); break
diff --git a/r_def.txt b/r_def.txt
index e69de29..949c010 100644
--- a/r_def.txt
+++ b/r_def.txt
@@ -0,0 +1,41 @@
           1 +ok   (1, True, 40, 0.2, 32, 'release', 'target_block', 1)
           2 +ok   (5, True, 56, 0.3, 41, 'release', 'target_block', 2)
           3 +ok   (0, True, 81, 0.4, 51, 'release', 'target_block', 2)
           4 +ok   (4, True, 74, 0.4, 59, 'release', 'target_block', 2)
           5 +ok   (3, True, 76, 0.5, 66, 'release', 'target_block', 2)
           6 +ok   (2, True, 98, 0.5, 72, 'release', 'target_block', 2)
           7 +ok   (8, True, 51, 0.2, 30, 'release', 'target_block', 2)
           8 +ok   (6, True, 63, 0.3, 53, 'release', 'target_block', 1)
           9 +ok   (11, True, 19, 0.1, 19, 'release', 'target_block', 0)
          10 +ok   (10, True, 26, 0.1, 27, 'release', 'target_block', 2)
          11 +ok   (9, True, 41, 0.2, 40, 'release', 'target_block', 1)
          12 +ok   (14, True, 11, 0.0, 14, 'release', 'target_block', 0)
          13 +ok   (7, True, 83, 0.5, 76, 'release', 'target_block', 2)
          14 +ok   (16, True, 25, 0.1, 20, 'release', 'target_block', 1)
          15 +ok   (15, True, 41, 0.2, 38, 'release', 'target_block', 2)
          16 +ok   (12, True, 57, 0.4, 56, 'release', 'target_block', 1)
          17 +ok   (19, True, 33, 0.1, 23, 'release', 'target_block', 1)
          18 +ok   (18, True, 38, 0.2, 30, 'release', 'target_block', 2)
          19 +ok   (17, True, 58, 0.3, 47, 'release', 'target_block', 2)
          20 +ok   (24, True, 23, 0.1, 17, 'release', 'target_block', 1)
          21 +ok   (21, True, 44, 0.2, 40, 'release', 'target_block', 0)
          22 +ok   (23, True, 44, 0.2, 37, 'release', 'target_block', 0)
          23 +ok   (22, True, 52, 0.2, 45, 'release', 'target_block', 2)
          24 +ok   (20, True, 87, 0.5, 71, 'release', 'target_block', 2)
          25 +ok   (25, True, 47, 0.2, 35, 'release', 'target_block', 1)
          26 +ok   (13, True, 133, 0.8, 127, 'release', 'target_block', 2)
          27 +ok   (27, True, 36, 0.2, 34, 'release', 'target_block', 0)
          28 +ok   (29, True, 19, 0.1, 18, 'release', 'target_block', 2)
          29 +ok   (30, True, 24, 0.1, 21, 'release', 'target_block', 0)
          30 +ok   (26, True, 58, 0.3, 53, 'release', 'target_block', 2)
          31 +ok   (34, True, 24, 0.1, 18, 'release', 'target_block', 0)
          32 +ok   (32, True, 46, 0.2, 34, 'release', 'target_block', 2)
          33 +ok   (35, True, 28, 0.1, 22, 'release', 'target_block', 0)
          34 +ok   (28, True, 95, 0.5, 77, 'release', 'target_block', 1)
          35 +ok   (33, True, 59, 0.3, 50, 'release', 'target_block', 2)
          36 +ok   (31, True, 69, 0.3, 60, 'release', 'target_block', 1)
          37 +ok   (36, True, 31, 0.2, 30, 'release', 'target_block', 1)
          38 +ok   (38, True, 40, 0.2, 25, 'release', 'target_block', 0)
          39 +ok   (37, True, 53, 0.3, 29, 'release', 'target_block', 0)
          40 +ok   (39, True, 62, 0.3, 15, 'release', 'target_block', 2)
          41 +success 40/40  mean steps(success) 51.1  max compute 0.8s
```

</details>

<a id="C009"></a>
### C009 · Finger-footprint collision model, 15deg yaw options, blocker-first ordering, better free spot

Commit `df3b962586dabc8b6d5b7df0112c23f503409366`; parents: 65e3006e2082ab2aa0a18e4113da87b0fd74ebf4. Recorded author date: 2026-09-28T20:59:19+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0590](01_timeline.md#E0590): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_df3b962_approach.py) · [Exact all-file diff](evidence/diffs/C009_df3b962.diff)

[Previous saved controller snapshot](evidence/versions/C008_65e3006_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5d9c068..5592610 100644
--- a/approach.py
+++ b/approach.py
@@ -10,7 +10,7 @@ TABLE_Y = (-0.40, 0.40)
   10     10  SAFE_MARGIN = 0.03
   11     11  VSTEP = 0.08
   12     12  HSTEP = 0.10
   13        -GRASP_DZ = 0.028       # tool height above object top when closing
          13 +GRASP_DZ = 0.031       # tool height above object top when closing
   14     14  PLACE_EPS = 0.0015     # clearance above support surface when releasing
   15     15  MAX_DQ = 0.2
   16     16  JLIM = {1: 2.41, 3: 2.66, 5: 2.23}   # limited joints (0-indexed): 2,4,6 in 1-index
@@ -65,68 +65,170 @@ class GeneratedApproach:
   65     65          return p[:2].copy()
   66     66  
   67     67      def _needs_clearing(self, n):
   68        -        """Obstruction overlaps the target block's final footprint (+margin)."""
          68 +        """Obstruction overlaps the target block's final footprint (+margin)
          69 +        or would block the gripper when placing the block."""
   69     70          rp, rhe = self.objs['target_region']
   70     71          bp, bhe = self.objs['target_block']
   71     72          p, he = self.objs[n]
   72     73          c = self._final_block_xy()
   73        -        m = 0.012
          74 +        m = 0.008
   74     75          ox = abs(p[0] - c[0]) < he[0] + bhe[0] + m
   75     76          oy = abs(p[1] - c[1]) < he[1] + bhe[1] + m
   76        -        # also anything touching the region itself
   77        -        rx = abs(p[0] - rp[0]) < he[0] + rhe[0] + 0.005
   78        -        ry = abs(p[1] - rp[1]) < he[1] + rhe[1] + 0.005
   79        -        return (ox and oy) or (rx and ry and p[2] - he[2] > rp[2])
          77 +        rx = abs(p[0] - rp[0]) < he[0] + rhe[0] + 0.003
          78 +        ry = abs(p[1] - rp[1]) < he[1] + rhe[1] + 0.003
          79 +        if (ox and oy) or (rx and ry and p[2] - he[2] > rp[2] + rhe[2] - 0.003):
          80 +            return True
          81 +        return False
   80     82  
   81        -    def _free_spot(self, name):
   82        -        """Pick a table location for obstruction `name` far from other stuff."""
          83 +    # finger model (tool frame): two boxes centred at +-FX, half extents
          84 +    FX, FHX, FHY, TIP = 0.061, 0.025, 0.017, 0.032
          85 +
          86 +    def _rect_hit(self, cxy, ax, ay, hx, hy, p, he, m):
          87 +        d = p[:2] - cxy
          88 +        for axis, r1 in ((np.array([1.0, 0]), abs(ax[0]) * hx + abs(ay[0]) * hy),
          89 +                         (np.array([0, 1.0]), abs(ax[1]) * hx + abs(ay[1]) * hy)):
          90 +            if abs(d @ axis) > r1 + (he[0] if axis[0] else he[1]) + m:
          91 +                return False
          92 +        for axis, r1 in ((ax, hx), (ay, hy)):
          93 +            r2 = abs(axis[0]) * he[0] + abs(axis[1]) * he[1]
          94 +            if abs(d @ axis) > r1 + r2 + m:
          95 +                return False
          96 +        return True
          97 +
          98 +    def _finger_hits(self, name, xy, yaw, tool_z, held=None, m=0.004):
          99 +        """Number of objects hit by the finger boxes (tips at tool_z - TIP)."""
         100 +        c, s_ = np.cos(yaw), np.sin(yaw)
         101 +        ax = np.array([c, s_]); ay = np.array([-s_, c])
         102 +        tip = tool_z - self.TIP
         103 +        hits = 0
         104 +        for n, (p, he) in self.objs.items():
         105 +            if n in (name, held, 'target_region'):
         106 +                continue
         107 +            if p[2] + he[2] < tip - 0.003:
         108 +                continue
         109 +            for sgn in (1, -1):
         110 +                if self._rect_hit(xy + sgn * self.FX * ax, ax, ay, self.FHX, self.FHY, p, he, m):
         111 +                    hits += 1
         112 +                    break
         113 +        return hits
         114 +
         115 +    def _self_overlap(self, he, yaw):
         116 +        """Extent of object along finger axis beyond the finger gap."""
         117 +        c, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
         118 +        ext = c * he[0] + s_ * he[1]
         119 +        return max(0.0, ext - 0.036)
         120 +
         121 +    def _cur_yaw(self):
         122 +        M = fk(self.base, self.q)
         123 +        return np.arctan2(M[1, 0], M[0, 0])
         124 +
         125 +    def _yaw_options(self, name, xy, tool_z, cur, held=None):
         126 +        p, he = self.objs[name]
         127 +        out = []
         128 +        for k in range(12):
         129 +            y = cur + k * np.pi / 12
         130 +            if k > 6:
         131 +                y -= np.pi
         132 +            dev = abs(y - cur)
         133 +            hits = self._finger_hits(name, xy, y, tool_z, held)
         134 +            ov = self._self_overlap(he, y)
         135 +            out.append((hits * 10 + ov * 50 + 0.2 * dev, hits, y))
         136 +        out.sort()
         137 +        return out
         138 +
         139 +    def _free_spot(self, name, yaw):
         140 +        """Pick a table location for obstruction `name` (held at yaw)."""
   83    141          p0, he0 = self.objs[name]
         142 +        c, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
         143 +        ex = np.array([c * he0[0] + s_ * he0[1], s_ * he0[0] + c * he0[1]])
   84    144          rp, rhe = self.objs['target_region']
   85        -        c = self._final_block_xy()
         145 +        bp, bhe = self.objs['target_block']
         146 +        tool_z = TABLE_Z + 2 * he0[2] + GRASP_DZ
   86    147          best, bestv = None, -1e9
   87        -        r0 = max(he0[0], he0[1])
   88        -        for x in np.linspace(TABLE_X[0] + 0.07, TABLE_X[1] - 0.06, 11):
   89        -            for y in np.linspace(TABLE_Y[0] + 0.06, TABLE_Y[1] - 0.06, 17):
   90        -                clear = 1e9
         148 +        for x in np.linspace(TABLE_X[0] + 0.05, TABLE_X[1] - 0.05, 15):
         149 +            for y in np.linspace(TABLE_Y[0] + 0.05, TABLE_Y[1] - 0.05, 25):
         150 +                xy = np.array([x, y])
         151 +                clear = 1.0
   91    152                  for n, (p, he) in self.objs.items():
   92    153                      if n == name:
   93    154                          continue
   94    155                      ext = he[:2].copy()
   95    156                      if n == 'target_region':
   96        -                        ext = ext + 0.03
   97        -                    dx = max(0.0, abs(x - p[0]) - ext[0] - r0)
   98        -                    dy = max(0.0, abs(y - p[1]) - ext[1] - r0)
         157 +                        ext = ext + 0.02
         158 +                    dx = max(0.0, abs(x - p[0]) - ext[0] - ex[0])
         159 +                    dy = max(0.0, abs(y - p[1]) - ext[1] - ex[1])
   99    160                      clear = min(clear, np.hypot(dx, dy))
  100        -                dxy = abs(x - c[0]), abs(y - c[1])
  101        -                clear = min(clear, np.hypot(max(0, dxy[0] - 0.08), max(0, dxy[1] - 0.08)) + 0.02)
  102        -                for bad in self.fail.get(name, []):
  103        -                    if np.hypot(x - bad[0], y - bad[1]) < 0.05:
  104        -                        clear = -1
  105        -                v = min(clear, 0.08) - 0.05 * np.hypot(x - p0[0], y - p0[1])
         161 +                if clear < 0.012:
         162 +                    continue
         163 +                # keep away from the target block (future pick) and region
         164 +                kb = min(np.hypot(max(0, abs(x - bp[0]) - bhe[0] - ex[0]), max(0, abs(y - bp[1]) - bhe[1] - ex[1])),
         165 +                         np.hypot(max(0, abs(x - rp[0]) - rhe[0] - ex[0]), max(0, abs(y - rp[1]) - rhe[1] - ex[1])))
         166 +                if self._finger_hits(name, xy, yaw, tool_z) > 0:
         167 +                    continue
         168 +                bad = any(np.hypot(x - b[0], y - b[1]) < 0.04 for b in self.fail.get(name, []))
         169 +                if bad:
         170 +                    continue
         171 +                v = min(clear, 0.05) + min(kb, 0.10) - 0.08 * np.hypot(x - p0[0], y - p0[1])
  106    172                  if v > bestv:
  107        -                    bestv, best = v, np.array([x, y])
         173 +                    bestv, best = v, xy
         174 +        if best is None:
         175 +            best = np.array([0.3, 0.3 if p0[1] < 0 else -0.3])
  108    176          return best
  109    177  
  110    178      # ------------------------------------------------------------- planning
         179 +    def _pick_choice(self, n, cur):
         180 +        p, he = self.objs[n]
         181 +        tz = p[2] + he[2] + GRASP_DZ
         182 +        opts = self._yaw_options(n, p[:2], tz, cur)
         183 +        att = self.fail.get(('grasp', n), 0)
         184 +        return opts[min(att, len(opts) - 1)]
         185 +
  111    186      def _plan_next(self):
  112        -        obs = [n for n in self._obstructions() if self._needs_clearing(n)]
  113        -        if obs:
  114        -            # clear the tallest / closest-to-center first
  115        -            c = self._final_block_xy()
  116        -            obs.sort(key=lambda n: np.hypot(*(self.objs[n][0][:2] - c)))
  117        -            n = obs[0]
  118        -            spot = self._free_spot(n)
  119        -            place_z = TABLE_Z
  120        -            self.task = dict(name=n, dest=spot, surf=place_z, yaw_dest=None)
         187 +        cur = self._cur_yaw()
         188 +        tool = fk(self.base, self.q)[:3, 3]
         189 +        need = [n for n in self._obstructions() if self._needs_clearing(n)]
         190 +        name = None
         191 +        if need:
         192 +            scored = []
         193 +            for n in need:
         194 +                v, hits, y = self._pick_choice(n, cur)
         195 +                d = np.hypot(*(self.objs[n][0][:2] - tool[:2]))
         196 +                scored.append((hits, self.fail.get(('grasp', n), 0), d, n, y))
         197 +            scored.sort()
         198 +            if scored[0][0] > 0:
         199 +                # try to move a blocker first
         200 +                others = [n for n in self._obstructions() if n not in need]
         201 +                alt = []
         202 +                for n in others:
         203 +                    v, hits, y = self._pick_choice(n, cur)
         204 +                    if hits == 0:
         205 +                        d = np.hypot(*(self.objs[n][0][:2] - tool[:2]))
         206 +                        alt.append((self.fail.get(('grasp', n), 0), d, n, y))
         207 +                # only blockers that are actually hit by best option of first needed
         208 +                n0, y0 = scored[0][3], scored[0][4]
         209 +                p0, he0 = self.objs[n0]
         210 +                blockers = []
         211 +                for f, d, n, y in sorted(alt):
         212 +                    saved = self.objs.pop(n)
         213 +                    h = self._finger_hits(n0, p0[:2], y0, p0[2] + he0[2] + GRASP_DZ)
         214 +                    self.objs[n] = saved
         215 +                    if h < scored[0][0]:
         216 +                        blockers.append((n, y))
         217 +                if blockers:
         218 +                    name, yaw = blockers[0]
         219 +            if name is None:
         220 +                name, yaw = scored[0][3], scored[0][4]
         221 +            p, he = self.objs[name]
         222 +            self.task = dict(name=name, dest=self._free_spot(name, yaw), surf=TABLE_Z)
  121    223          else:
  122    224              rp, rhe = self.objs['target_region']
  123        -            self.task = dict(name='target_block', dest=self._final_block_xy(),
  124        -                             surf=rp[2] + rhe[2], yaw_dest=None)
  125        -        n = self.task['name']
         225 +            name = 'target_block'
         226 +            v, hits, yaw = self._pick_choice(name, cur)
         227 +            self.task = dict(name=name, dest=self._final_block_xy(), surf=rp[2] + rhe[2])
         228 +        n = name
  126    229          p, he = self.objs[n]
  127        -        att = self.fail.get(('grasp', n), 0)
  128        -        self.task['yaw'] = self._choose_yaw(n, p[:2], p[2] + he[2] + GRASP_DZ - 0.05, att)
  129        -        self.task['yaw_place'] = self.task['yaw']
         230 +        self.task['yaw'] = yaw
         231 +        self.task['yaw_place'] = yaw
  130    232          self.phase = 'to_pick'
  131    233          tool = fk(self.base, self.q)[:3, 3]
  132    234          sz = self._safe_z(None, 0.05)
@@ -139,51 +241,6 @@ class GeneratedApproach:
  139    241          path += self._line(pick_above, np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ]), VSTEP)
  140    242          self._set_path(path, self.task['yaw'])
  141    243  
  142        -    def _footprint_hits(self, name, xy, yaw, bottom):
  143        -        """Count collisions of gripper footprint (at xy, yaw, lowest z=bottom) with other objects."""
  144        -        c, s_ = np.cos(yaw), np.sin(yaw)
  145        -        ax = np.array([c, s_]); ay = np.array([-s_, c])
  146        -        gx, gy = 0.065, 0.03
  147        -        hits = 0.0
  148        -        for n, (p, he) in self.objs.items():
  149        -            if n == name or n == 'target_region':
  150        -                continue
  151        -            if p[2] + he[2] < bottom:
  152        -                continue
  153        -            d = p[:2] - xy
  154        -            # SAT between rotated rect (gx,gy) and AABB he
  155        -            sep = False
  156        -            for axis, r1 in ((np.array([1.0, 0]), abs(ax[0]) * gx + abs(ay[0]) * gy),
  157        -                             (np.array([0, 1.0]), abs(ax[1]) * gx + abs(ay[1]) * gy)):
  158        -                if abs(d @ axis) > r1 + (he[0] if axis[0] else he[1]):
  159        -                    sep = True
  160        -            for axis, r1 in ((ax, gx), (ay, gy)):
  161        -                r2 = abs(axis[0]) * he[0] + abs(axis[1]) * he[1]
  162        -                if abs(d @ axis) > r1 + r2:
  163        -                    sep = True
  164        -            if not sep:
  165        -                hits += 1
  166        -        return hits
  167        -
  168        -    def _choose_yaw(self, name, xy, bottom, attempt=0):
  169        -        """Object-axis-aligned yaw; fingers (tool x) along the smaller extent
  170        -        when possible, avoiding neighbours."""
  171        -        p, he = self.objs[name]
  172        -        M = fk(self.base, self.q)
  173        -        cur = np.arctan2(M[1, 0], M[0, 0])
  174        -        cands = []
  175        -        for k in range(4):
  176        -            y = k * np.pi / 2
  177        -            finger_ext = he[0] if k % 2 == 0 else he[1]
  178        -            hits = self._footprint_hits(name, xy, y, bottom)
  179        -            y = cur + wrap(y - cur)
  180        -            if abs(wrap(y + np.pi - cur)) < abs(y - cur):
  181        -                y = cur + wrap(y + np.pi - cur)
  182        -            dev = abs(y - cur)
  183        -            cands.append((hits * 10 + (finger_ext > 0.036) * 5 + finger_ext * 10 + 0.3 * dev, y))
  184        -        cands.sort()
  185        -        return cands[attempt % 4][1]
  186        -
  187    244      def _yaw_for(self, xy):
  188    245          mx = self.base[0] + 0.12 * np.cos(self.base[2])
  189    246          my = self.base[1] + 0.12 * np.sin(self.base[2])
diff --git a/d204.txt b/d204.txt
new file mode 100644
index 0000000..380e7e8
--- /dev/null
+++ b/d204.txt
@@ -0,0 +1,407 @@
           1 +target_block [ 0.149 -0.166  0.1  ] [0.029 0.035 0.025]
           2 +obstruction0 [ 0.186 -0.377  0.096] [0.018 0.014 0.011]
           3 +obstruction2 [ 0.248 -0.346  0.112] [0.017 0.014 0.027]
           4 +obstruction3 [ 0.244 -0.385  0.107] [0.02  0.016 0.022]
           5 +obstruction4 [ 0.171 -0.31   0.108] [0.016 0.018 0.023]
           6 +obstruction1 [ 0.209 -0.341  0.106] [0.015 0.012 0.021]
           7 +target_region [ 0.21  -0.348  0.08 ] [0.036 0.044 0.005]
           8 +0 to_pic ction1 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 5 dq 0.2
           9 +1 to_pic ction1 [ 0.167 -0.043  0.219] sc 1.0 g 0 gr 0.0 np 5 dq 0.16
          10 +2 to_pic ction1 [ 0.167 -0.084  0.218] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          11 +3 to_pic ction1 [ 0.179 -0.125  0.218] sc 1.0 g 0 gr 0.0 np 4 dq 0.19
          12 +4 to_pic ction1 [ 0.181 -0.17   0.218] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          13 +5 to_pic ction1 [ 0.192 -0.215  0.219] sc 1.0 g 0 gr 0.0 np 3 dq 0.15
          14 +6 to_pic ction1 [ 0.195 -0.255  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          15 +7 to_pic ction1 [ 0.208 -0.33   0.219] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
          16 +8 grasp ction1 [ 0.209 -0.341  0.155] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          17 +9 to_pla ction1 [ 0.209 -0.341  0.155] sc 1.0 g 1 gr 0.0 np 6 dq 0.12
          18 +10 to_pla ction1 [ 0.209 -0.341  0.196] sc 1.0 g 1 gr 0.0 np 5 dq 0.12
          19 +11 to_pla ction1 [ 0.209 -0.341  0.238] sc 1.0 g 1 gr 0.0 np 4 dq 0.17
          20 +12 to_pla ction1 [ 0.297 -0.34   0.238] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          21 +13 to_pla ction1 [ 0.374 -0.341  0.238] sc 1.0 g 1 gr 0.0 np 2 dq 0.1
          22 +14 to_pla ction1 [ 0.386 -0.34   0.192] sc 1.0 g 1 gr 0.0 np 1 dq 0.11
          23 +15 releas ction1 [ 0.386 -0.34   0.146] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          24 +16 retrea ction1 [ 0.386 -0.34   0.146] sc 1.0 g 0 gr 0.0 np 2 dq 0.07
          25 +17 retrea ction1 [ 0.386 -0.34   0.176] sc 1.0 g 0 gr 0.0 np 1 dq 0.07
          26 +18 to_pic ction0 [ 0.386 -0.34   0.206] sc 1.0 g 0 gr 0.0 np 5 dq 0.13
          27 +19 to_pic ction0 [ 0.319 -0.352  0.218] sc 1.0 g 0 gr 0.0 np 4 dq 0.13
          28 +20 to_pic ction0 [ 0.253 -0.365  0.218] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
          29 +21 to_pic ction0 [ 0.186 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
          30 +22 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
          31 +23 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
          32 +24 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
          33 +25 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
          34 +26 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
          35 +27 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          36 +28 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
          37 +29 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
          38 +30 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
          39 +31 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
          40 +32 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          41 +33 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
          42 +34 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
          43 +35 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
          44 +36 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
          45 +37 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
          46 +38 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
          47 +39 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
          48 +40 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
          49 +41 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
          50 +42 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          51 +43 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
          52 +44 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
          53 +45 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
          54 +46 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
          55 +47 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          56 +48 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
          57 +49 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
          58 +50 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          59 +51 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
          60 +52 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
          61 +53 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          62 +54 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
          63 +55 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
          64 +56 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
          65 +57 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
          66 +58 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
          67 +59 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          68 +60 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
          69 +61 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
          70 +62 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
          71 +63 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
          72 +64 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
          73 +65 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
          74 +66 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
          75 +67 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
          76 +68 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
          77 +69 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
          78 +70 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
          79 +71 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
          80 +72 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          81 +73 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
          82 +74 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
          83 +75 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
          84 +76 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
          85 +77 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          86 +78 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
          87 +79 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
          88 +80 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
          89 +81 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
          90 +82 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
          91 +83 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
          92 +84 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
          93 +85 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
          94 +86 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
          95 +87 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          96 +88 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
          97 +89 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
          98 +90 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
          99 +91 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         100 +92 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         101 +93 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         102 +94 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         103 +95 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         104 +96 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         105 +97 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         106 +98 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         107 +99 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         108 +100 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         109 +101 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         110 +102 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         111 +103 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         112 +104 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         113 +105 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         114 +106 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         115 +107 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         116 +108 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         117 +109 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         118 +110 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         119 +111 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         120 +112 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         121 +113 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         122 +114 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         123 +115 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         124 +116 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         125 +117 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         126 +118 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         127 +119 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         128 +120 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         129 +121 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         130 +122 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         131 +123 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         132 +124 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         133 +125 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         134 +126 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         135 +127 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         136 +128 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         137 +129 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         138 +130 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         139 +131 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         140 +132 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         141 +133 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         142 +134 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         143 +135 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         144 +136 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         145 +137 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         146 +138 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         147 +139 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         148 +140 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         149 +141 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         150 +142 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         151 +143 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         152 +144 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         153 +145 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         154 +146 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         155 +147 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         156 +148 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         157 +149 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         158 +150 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         159 +151 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         160 +152 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         161 +153 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         162 +154 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         163 +155 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         164 +156 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         165 +157 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         166 +158 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         167 +159 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         168 +160 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         169 +161 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         170 +162 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         171 +163 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         172 +164 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         173 +165 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         174 +166 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         175 +167 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         176 +168 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         177 +169 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         178 +170 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         179 +171 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         180 +172 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         181 +173 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         182 +174 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         183 +175 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         184 +176 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         185 +177 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         186 +178 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         187 +179 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         188 +180 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         189 +181 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         190 +182 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         191 +183 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         192 +184 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         193 +185 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         194 +186 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         195 +187 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         196 +188 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         197 +189 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         198 +190 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         199 +191 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         200 +192 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         201 +193 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         202 +194 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         203 +195 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         204 +196 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         205 +197 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         206 +198 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         207 +199 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         208 +200 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         209 +201 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         210 +202 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         211 +203 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         212 +204 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         213 +205 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         214 +206 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         215 +207 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         216 +208 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         217 +209 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         218 +210 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         219 +211 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         220 +212 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         221 +213 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         222 +214 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         223 +215 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         224 +216 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         225 +217 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         226 +218 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         227 +219 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         228 +220 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         229 +221 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         230 +222 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         231 +223 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         232 +224 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         233 +225 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         234 +226 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         235 +227 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         236 +228 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         237 +229 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         238 +230 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         239 +231 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         240 +232 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         241 +233 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         242 +234 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         243 +235 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         244 +236 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         245 +237 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         246 +238 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         247 +239 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         248 +240 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         249 +241 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         250 +242 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         251 +243 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         252 +244 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         253 +245 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         254 +246 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         255 +247 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         256 +248 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         257 +249 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         258 +250 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         259 +251 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         260 +252 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         261 +253 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         262 +254 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         263 +255 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         264 +256 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         265 +257 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         266 +258 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         267 +259 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         268 +260 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         269 +261 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         270 +262 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         271 +263 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         272 +264 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         273 +265 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         274 +266 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         275 +267 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         276 +268 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         277 +269 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         278 +270 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         279 +271 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         280 +272 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         281 +273 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         282 +274 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         283 +275 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         284 +276 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         285 +277 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         286 +278 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         287 +279 to_pic ction0 [ 0.187 -0.377  0.155] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         288 +280 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         289 +281 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         290 +282 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         291 +283 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         292 +284 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         293 +285 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         294 +286 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         295 +287 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         296 +288 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         297 +289 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         298 +290 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         299 +291 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         300 +292 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         301 +293 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         302 +294 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         303 +295 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         304 +296 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         305 +297 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         306 +298 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         307 +299 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         308 +300 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         309 +301 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         310 +302 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         311 +303 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         312 +304 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         313 +305 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         314 +306 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         315 +307 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         316 +308 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         317 +309 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         318 +310 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         319 +311 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         320 +312 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         321 +313 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         322 +314 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         323 +315 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         324 +316 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         325 +317 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         326 +318 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         327 +319 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         328 +320 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         329 +321 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         330 +322 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         331 +323 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         332 +324 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         333 +325 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         334 +326 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         335 +327 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         336 +328 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         337 +329 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         338 +330 to_pic ction0 [ 0.187 -0.377  0.155] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         339 +331 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         340 +332 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         341 +333 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         342 +334 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         343 +335 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         344 +336 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         345 +337 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         346 +338 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         347 +339 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         348 +340 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         349 +341 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         350 +342 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         351 +343 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         352 +344 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         353 +345 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         354 +346 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         355 +347 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         356 +348 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         357 +349 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         358 +350 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         359 +351 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         360 +352 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         361 +353 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         362 +354 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         363 +355 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         364 +356 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         365 +357 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         366 +358 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         367 +359 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         368 +360 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         369 +361 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         370 +362 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         371 +363 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         372 +364 to_pic ction0 [ 0.186 -0.377  0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         373 +365 to_pic ction0 [ 0.186 -0.377  0.177] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         374 +366 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         375 +367 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         376 +368 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         377 +369 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         378 +370 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         379 +371 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         380 +372 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         381 +373 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 1 dq 0.01
         382 +374 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         383 +375 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.0625 g 0 gr 0.0 np 1 dq 0.0
         384 +376 grasp ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         385 +377 to_pic ction0 [ 0.187 -0.377  0.154] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         386 +378 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         387 +379 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         388 +380 to_pic ction0 [ 0.187 -0.377  0.154] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         389 +381 to_pic ction0 [ 0.187 -0.377  0.155] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         390 +382 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         391 +383 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         392 +384 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         393 +385 to_pic ction0 [ 0.187 -0.377  0.155] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         394 +386 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         395 +387 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         396 +388 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         397 +389 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         398 +390 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         399 +391 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         400 +392 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         401 +393 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.5 g 0 gr 0.0 np 4 dq 0.1
         402 +394 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.25 g 0 gr 0.0 np 4 dq 0.05
         403 +395 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.125 g 0 gr 0.0 np 4 dq 0.02
         404 +396 to_pic ction0 [ 0.187 -0.377  0.156] sc 0.0625 g 0 gr 0.0 np 4 dq 0.01
         405 +397 grasp ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr -1.0 np 4 dq 0.0
         406 +398 to_pic ction0 [ 0.187 -0.377  0.156] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
         407 +399 to_pic ction0 [ 0.187 -0.377  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
diff --git a/geo_0_0.txt b/geo_0_0.txt
new file mode 100644
index 0000000..4820e67
--- /dev/null
+++ b/geo_0_0.txt
@@ -0,0 +1 @@
           1 +seed 0 he [0.031 0.022 0.025] yaw 0.0 axis 0 0.00:-0.019 0.01:-0.013 0.02:+0.032 0.03:+0.032 0.04:+0.032 0.05:+0.032 0.06:+0.032 0.07:+0.032 0.08:+0.029 0.09:+0.017
diff --git a/geo_0_1.txt b/geo_0_1.txt
new file mode 100644
index 0000000..37deb6b
--- /dev/null
+++ b/geo_0_1.txt
@@ -0,0 +1 @@
           1 +seed 0 he [0.031 0.022 0.025] yaw 0.0 axis 1 0.00:-0.019 0.01:-0.019 0.02:-0.019 0.03:-0.019 0.04:-0.019 0.05:-0.019 0.06:-0.019 0.07:-0.019 0.08:-0.019 0.09:-0.019
diff --git a/geo_1.5708_0.txt b/geo_1.5708_0.txt
new file mode 100644
index 0000000..b88ac31
--- /dev/null
+++ b/geo_1.5708_0.txt
@@ -0,0 +1 @@
           1 +seed 0 he [0.031 0.022 0.025] yaw 1.5708 axis 0 0.00:-0.019 0.01:-0.019 0.02:-0.019 0.03:-0.019 0.04:-0.019 0.05:-0.019 0.06:-0.019 0.07:-0.019 0.08:-0.019 0.09:-0.019
diff --git a/geo_1.5708_1.txt b/geo_1.5708_1.txt
new file mode 100644
index 0000000..04abb66
--- /dev/null
+++ b/geo_1.5708_1.txt
@@ -0,0 +1 @@
           1 +seed 0 he [0.031 0.022 0.025] yaw 1.5708 axis 1 0.00:-0.019 0.01:-0.019 0.02:-0.013 0.03:+0.032 0.04:+0.032 0.05:+0.032 0.06:+0.032 0.07:+0.032 0.08:+0.020 0.09:-0.004
diff --git a/gripgeo.py b/gripgeo.py
new file mode 100644
index 0000000..5880374
--- /dev/null
+++ b/gripgeo.py
@@ -0,0 +1,27 @@
           1 +from th import *
           2 +import sys
           3 +yaw=float(sys.argv[1]); axis=int(sys.argv[2])
           4 +env=make_env(); 
           5 +for seed in range(50):
           6 +    obs,_=env.reset(seed=seed, options={'object_count':0})
           7 +    tb=obs.get_object_from_name('target_block'); tr=obs.get_object_from_name('target_region')
           8 +    bx,by=obs.get(tb,'pose_x'),obs.get(tb,'pose_y'); rx,ry=obs.get(tr,'pose_x'),obs.get(tr,'pose_y')
           9 +    if 0.22<bx<0.38 and abs(by)<0.25 and np.hypot(bx-rx,by-ry)>0.2: break
          10 +h=H(seed, env=env, oc=0); name='target_block'
          11 +p=h.pose(name); he=h.he(name); top=p[2]+he[2]
          12 +out=[]
          13 +for d in np.arange(0.0, 0.10, 0.01):
          14 +    xy=p[:2].copy(); xy[axis]+=d
          15 +    ok0,_=h.goto([xy[0],xy[1],top+0.08],yaw)
          16 +    if not ok0: out.append(f'{d:.2f}:NA'); continue
          17 +    z=top+0.08
          18 +    while z>top-0.08:
          19 +        z-=0.003
          20 +        ok,_=h.goto([xy[0],xy[1],z],yaw)
          21 +        if not ok: break
          22 +    out.append(f'{d:.2f}:{z+0.003-top:+.3f}')
          23 +    z=top+0.08
          24 +    while h.tool()[2,3] < top+0.075:
          25 +        ok,_=h.goto([xy[0],xy[1],h.tool()[2,3]+0.01],yaw)
          26 +        if not ok: print('stuck'); break
          27 +print('seed',seed,'he',he.round(3),'yaw',yaw,'axis',axis,' '.join(out))
diff --git a/r_def.txt b/r_def.txt
index 949c010..c774766 100644
--- a/r_def.txt
+++ b/r_def.txt
@@ -1,41 +1,41 @@
    1        -ok   (1, True, 40, 0.2, 32, 'release', 'target_block', 1)
    2        -ok   (5, True, 56, 0.3, 41, 'release', 'target_block', 2)
    3        -ok   (0, True, 81, 0.4, 51, 'release', 'target_block', 2)
    4        -ok   (4, True, 74, 0.4, 59, 'release', 'target_block', 2)
    5        -ok   (3, True, 76, 0.5, 66, 'release', 'target_block', 2)
    6        -ok   (2, True, 98, 0.5, 72, 'release', 'target_block', 2)
    7        -ok   (8, True, 51, 0.2, 30, 'release', 'target_block', 2)
    8        -ok   (6, True, 63, 0.3, 53, 'release', 'target_block', 1)
    9        -ok   (11, True, 19, 0.1, 19, 'release', 'target_block', 0)
   10        -ok   (10, True, 26, 0.1, 27, 'release', 'target_block', 2)
   11        -ok   (9, True, 41, 0.2, 40, 'release', 'target_block', 1)
   12        -ok   (14, True, 11, 0.0, 14, 'release', 'target_block', 0)
   13        -ok   (7, True, 83, 0.5, 76, 'release', 'target_block', 2)
   14        -ok   (16, True, 25, 0.1, 20, 'release', 'target_block', 1)
   15        -ok   (15, True, 41, 0.2, 38, 'release', 'target_block', 2)
   16        -ok   (12, True, 57, 0.4, 56, 'release', 'target_block', 1)
   17        -ok   (19, True, 33, 0.1, 23, 'release', 'target_block', 1)
   18        -ok   (18, True, 38, 0.2, 30, 'release', 'target_block', 2)
   19        -ok   (17, True, 58, 0.3, 47, 'release', 'target_block', 2)
   20        -ok   (24, True, 23, 0.1, 17, 'release', 'target_block', 1)
   21        -ok   (21, True, 44, 0.2, 40, 'release', 'target_block', 0)
   22        -ok   (23, True, 44, 0.2, 37, 'release', 'target_block', 0)
   23        -ok   (22, True, 52, 0.2, 45, 'release', 'target_block', 2)
   24        -ok   (20, True, 87, 0.5, 71, 'release', 'target_block', 2)
   25        -ok   (25, True, 47, 0.2, 35, 'release', 'target_block', 1)
   26        -ok   (13, True, 133, 0.8, 127, 'release', 'target_block', 2)
   27        -ok   (27, True, 36, 0.2, 34, 'release', 'target_block', 0)
   28        -ok   (29, True, 19, 0.1, 18, 'release', 'target_block', 2)
   29        -ok   (30, True, 24, 0.1, 21, 'release', 'target_block', 0)
   30        -ok   (26, True, 58, 0.3, 53, 'release', 'target_block', 2)
   31        -ok   (34, True, 24, 0.1, 18, 'release', 'target_block', 0)
   32        -ok   (32, True, 46, 0.2, 34, 'release', 'target_block', 2)
   33        -ok   (35, True, 28, 0.1, 22, 'release', 'target_block', 0)
   34        -ok   (28, True, 95, 0.5, 77, 'release', 'target_block', 1)
   35        -ok   (33, True, 59, 0.3, 50, 'release', 'target_block', 2)
   36        -ok   (31, True, 69, 0.3, 60, 'release', 'target_block', 1)
   37        -ok   (36, True, 31, 0.2, 30, 'release', 'target_block', 1)
   38        -ok   (38, True, 40, 0.2, 25, 'release', 'target_block', 0)
   39        -ok   (37, True, 53, 0.3, 29, 'release', 'target_block', 0)
   40        -ok   (39, True, 62, 0.3, 15, 'release', 'target_block', 2)
   41        -success 40/40  mean steps(success) 51.1  max compute 0.8s
           1 +ok   (3, True, 30, 0.1, 49, 'release', 'target_block', 2)
           2 +ok   (6, True, 38, 0.1, 60, 'release', 'target_block', 1)
           3 +ok   (7, True, 42, 0.2, 66, 'release', 'target_block', 2)
           4 +ok   (1, True, 43, 0.2, 68, 'release', 'target_block', 1)
           5 +ok   (4, True, 46, 0.2, 69, 'release', 'target_block', 2)
           6 +ok   (5, True, 54, 0.2, 82, 'release', 'target_block', 2)
           7 +ok   (11, True, 13, 0.0, 18, 'release', 'target_block', 0)
           8 +ok   (0, True, 89, 0.3, 96, 'release', 'target_block', 2)
           9 +ok   (9, True, 26, 0.1, 40, 'release', 'target_block', 1)
          10 +ok   (14, True, 11, 0.0, 16, 'release', 'target_block', 0)
          11 +ok   (10, True, 26, 0.1, 42, 'release', 'target_block', 2)
          12 +ok   (12, True, 31, 0.1, 44, 'release', 'target_block', 1)
          13 +ok   (8, True, 49, 0.2, 71, 'release', 'target_block', 2)
          14 +ok   (2, True, 105, 0.4, 125, 'release', 'target_block', 2)
          15 +ok   (15, True, 26, 0.1, 38, 'release', 'target_block', 2)
          16 +ok   (16, True, 25, 0.1, 37, 'release', 'target_block', 1)
          17 +ok   (13, True, 45, 0.2, 60, 'release', 'target_block', 2)
          18 +ok   (21, True, 18, 0.1, 27, 'release', 'target_block', 0)
          19 +ok   (18, True, 31, 0.1, 50, 'release', 'target_block', 2)
          20 +ok   (19, True, 31, 0.1, 50, 'release', 'target_block', 1)
          21 +ok   (23, True, 18, 0.1, 43, 'release', 'target_block', 0)
          22 +ok   (17, True, 48, 0.2, 84, 'release', 'target_block', 2)
          23 +ok   (24, True, 18, 0.1, 47, 'release', 'target_block', 1)
          24 +ok   (22, True, 31, 0.1, 60, 'release', 'target_block', 2)
          25 +ok   (27, True, 24, 0.1, 36, 'release', 'target_block', 0)
          26 +ok   (29, True, 13, 0.1, 21, 'release', 'target_block', 2)
          27 +ok   (20, True, 57, 0.2, 92, 'release', 'target_block', 2)
          28 +ok   (26, True, 31, 0.1, 57, 'release', 'target_block', 2)
          29 +ok   (25, True, 38, 0.2, 63, 'release', 'target_block', 1)
          30 +ok   (30, True, 20, 0.1, 32, 'release', 'target_block', 0)
          31 +ok   (34, True, 21, 0.1, 34, 'release', 'target_block', 0)
          32 +ok   (35, True, 19, 0.1, 36, 'release', 'target_block', 0)
          33 +ok   (28, True, 47, 0.2, 74, 'release', 'target_block', 1)
          34 +ok   (37, True, 16, 0.1, 32, 'release', 'target_block', 0)
          35 +ok   (32, True, 39, 0.2, 58, 'release', 'target_block', 2)
          36 +ok   (36, True, 25, 0.1, 42, 'release', 'target_block', 1)
          37 +ok   (38, True, 13, 0.0, 11, 'release', 'target_block', 0)
          38 +ok   (31, True, 42, 0.2, 63, 'release', 'target_block', 1)
          39 +ok   (33, True, 43, 0.2, 52, 'release', 'target_block', 2)
          40 +ok   (39, True, 47, 0.2, 21, 'release', 'target_block', 2)
          41 +success 40/40  mean steps(success) 34.7  max compute 0.4s
diff --git a/r_oc5.txt b/r_oc5.txt
index e69de29..2fde4a1 100644
--- a/r_oc5.txt
+++ b/r_oc5.txt
@@ -0,0 +1,17 @@
           1 +ok   (202, True, 75, 0.3, 142, 'release', 'target_block', 5)
           2 +ok   (203, True, 83, 0.4, 162, 'release', 'target_block', 5)
           3 +ok   (201, True, 125, 0.6, 232, 'release', 'target_block', 5)
           4 +ok   (206, True, 48, 0.2, 36, 'release', 'target_block', 5)
           5 +ok   (205, True, 146, 0.7, 120, 'release', 'target_block', 5)
           6 +ok   (207, True, 86, 0.5, 31, 'release', 'target_block', 5)
           7 +ok   (208, True, 65, 0.3, 28, 'release', 'target_block', 5)
           8 +ok   (200, True, 408, 1.8, 321, 'release', 'target_block', 5)
           9 +ok   (209, True, 108, 0.4, 35, 'release', 'target_block', 5)
          10 +ok   (211, True, 66, 0.3, 25, 'release', 'target_block', 5)
          11 +FAIL (204, False, 1000, 5.2, 211, 'to_pick', 'obstruction0', 5)
          12 +ok   (212, True, 92, 0.4, 37, 'release', 'target_block', 5)
          13 +ok   (213, True, 105, 0.4, 35, 'release', 'target_block', 5)
          14 +ok   (214, True, 144, 0.6, 30, 'release', 'target_block', 5)
          15 +FAIL (210, False, 1000, 3.9, 101, 'to_pick', 'obstruction3', 5)
          16 +FAIL (215, False, 1000, 6.1, 52, 'to_pick', 'obstruction2', 5)
          17 +success 13/16  mean steps(success) 119.3  max compute 6.1s
diff --git a/th.py b/th.py
index 727af6c..ae8eb16 100644
--- a/th.py
+++ b/th.py
@@ -4,8 +4,8 @@ import numpy as np
    4      4  GF=['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']
    5      5  BF=['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']
    6      6  class H:
    7        -    def __init__(self, seed, env=None):
    8        -        self.env = env or make_env(); self.obs,_ = self.env.reset(seed=seed)
           7 +    def __init__(self, seed, env=None, oc=None):
           8 +        self.env = env or make_env(); self.obs,_ = self.env.reset(seed=seed, options={'object_count':oc} if oc is not None else None)
    9      9          self.R = self.obs.get_object_from_name('robot'); self.n=0; self.done=False
   10     10      def o(self, name): return self.obs.get_object_from_name(name)
   11     11      def g(self, name, f): return self.obs.get(self.o(name), f)
```

</details>

<a id="C010"></a>
### C010 · Blocked recovery: straight cartesian small steps instead of scaling joint deltas

Commit `d6f9c2860017345fcfbd1dfe2bcc8b1c1b1eabc2`; parents: df3b962586dabc8b6d5b7df0112c23f503409366. Recorded author date: 2026-09-28T21:08:49+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0644](01_timeline.md#E0644): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_d6f9c28_approach.py) · [Exact all-file diff](evidence/diffs/C010_d6f9c28.diff)

[Previous saved controller snapshot](evidence/versions/C009_df3b962_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5592610..2890c25 100644
--- a/approach.py
+++ b/approach.py
@@ -290,12 +290,17 @@ class GeneratedApproach:
  290    290              if e < tol and (eo < (0.01 if final else 0.1)):
  291    291                  self.path.pop(0)
  292    292                  continue
         293 +            if self.scale < 1.0:
         294 +                # blocked recently: move along straight cartesian line, small step
         295 +                cs = 0.04 * self.scale
         296 +                if e > cs:
         297 +                    pos = M[:3, 3] + (pos - M[:3, 3]) * (cs / e)
  293    298              qt, err = self._ik(pos, yaw)
  294    299              dq = qt - self.q
  295    300              m = np.max(np.abs(dq))
  296    301              if m > MAX_DQ:
  297    302                  dq = dq * (MAX_DQ / m)
  298        -            return dq * self.scale
         303 +            return dq
  299    304          return None
  300    305  
  301    306      def _act(self, dq=None, grip=0.0):
@@ -316,7 +321,7 @@ class GeneratedApproach:
  316    321              if np.allclose(self.q, self.last_q, atol=1e-7):
  317    322                  blocked = True
  318    323          if self.last_cmd is not None and not blocked:
  319        -            self.scale = 1.0
         324 +            self.scale = min(1.0, self.scale * 2)
  320    325          if blocked and self.scale > 1.0 / 16:
  321    326              self.scale *= 0.5
  322    327              blocked = False
diff --git a/d215.txt b/d215.txt
new file mode 100644
index 0000000..a44dc2d
--- /dev/null
+++ b/d215.txt
@@ -0,0 +1,407 @@
           1 +obstruction4 [0.456 0.025 0.102] [0.014 0.015 0.017]
           2 +obstruction0 [0.421 0.04  0.1  ] [0.013 0.013 0.015]
           3 +obstruction1 [ 0.434 -0.004  0.112] [0.02  0.01  0.027]
           4 +target_region [0.408 0.018 0.08 ] [0.047 0.021 0.005]
           5 +obstruction3 [0.363 0.043 0.111] [0.019 0.015 0.026]
           6 +obstruction2 [0.395 0.02  0.097] [0.011 0.013 0.012]
           7 +target_block [0.285 0.061 0.1  ] [0.038 0.017 0.025]
           8 +0 to_pic ction3 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
           9 +1 to_pic ction3 [0.2   0.01  0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          10 +2 to_pic ction3 [0.271 0.023 0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          11 +3 to_pic ction3 [0.344 0.038 0.221] sc 1.0 g 0 gr 0.0 np 1 dq 0.16
          12 +4 grasp ction3 [0.363 0.043 0.168] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          13 +5 to_pla ction3 [0.363 0.043 0.168] sc 1.0 g 1 gr 0.0 np 6 dq 0.14
          14 +6 to_pla ction3 [0.363 0.043 0.209] sc 1.0 g 1 gr 0.0 np 5 dq 0.14
          15 +7 to_pla ction3 [0.363 0.043 0.251] sc 1.0 g 1 gr 0.0 np 4 dq 0.18
          16 +8 to_pla ction3 [0.385 0.109 0.251] sc 1.0 g 1 gr 0.0 np 3 dq 0.15
          17 +9 to_pla ction3 [0.407 0.175 0.251] sc 1.0 g 1 gr 0.0 np 2 dq 0.13
          18 +10 to_pla ction3 [0.407 0.175 0.205] sc 1.0 g 1 gr 0.0 np 1 dq 0.13
          19 +11 releas ction3 [0.407 0.175 0.159] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          20 +12 retrea ction3 [0.407 0.175 0.159] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          21 +13 retrea ction3 [0.407 0.175 0.189] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          22 +14 to_pic ction0 [0.407 0.175 0.219] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          23 +15 to_pic ction0 [0.411 0.15  0.219] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          24 +16 to_pic ction0 [0.413 0.125 0.218] sc 1.0 g 0 gr 0.0 np 3 dq 0.15
          25 +17 to_pic ction0 [0.414 0.108 0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.17
          26 +18 to_pic ction0 [0.421 0.04  0.218] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          27 +19 to_pic ction0 [0.421 0.04  0.151] sc 1.0 g 0 gr 0.0 np 1 dq 0.02
          28 +20 grasp ction0 [0.421 0.04  0.145] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          29 +21 to_pic ction4 [0.421 0.04  0.145] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          30 +22 to_pic ction4 [0.422 0.039 0.16 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          31 +23 to_pic ction4 [0.422 0.038 0.175] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          32 +24 to_pic ction4 [0.422 0.038 0.191] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          33 +25 to_pic ction4 [0.421 0.039 0.207] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
          34 +26 to_pic ction4 [0.421 0.04  0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.12
          35 +27 to_pic ction4 [0.456 0.025 0.218] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
          36 +28 grasp ction4 [0.456 0.025 0.149] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          37 +29 to_pic ction1 [0.456 0.025 0.149] sc 1.0 g 0 gr 0.0 np 3 dq 0.19
          38 +30 to_pic ction1 [0.456 0.025 0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
          39 +31 to_pic ction1 [ 0.434 -0.004  0.218] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
          40 +32 grasp ction1 [ 0.434 -0.004  0.169] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          41 +33 to_pla ction1 [ 0.434 -0.004  0.169] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          42 +34 to_pla ction1 [ 0.434 -0.004  0.239] sc 1.0 g 1 gr 0.0 np 4 dq 0.14
          43 +35 to_pla ction1 [ 0.431 -0.061  0.243] sc 1.0 g 1 gr 0.0 np 3 dq 0.14
          44 +36 to_pla ction1 [ 0.429 -0.117  0.243] sc 1.0 g 1 gr 0.0 np 2 dq 0.12
          45 +37 to_pla ction1 [ 0.429 -0.117  0.202] sc 1.0 g 1 gr 0.0 np 1 dq 0.11
          46 +38 releas ction1 [ 0.429 -0.117  0.161] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          47 +39 retrea ction1 [ 0.429 -0.117  0.161] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
          48 +40 retrea ction1 [ 0.429 -0.117  0.191] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
          49 +41 to_pic ction2 [ 0.429 -0.117  0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          50 +42 to_pic ction2 [ 0.426 -0.1    0.219] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          51 +43 to_pic ction2 [ 0.422 -0.084  0.218] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          52 +44 to_pic ction2 [ 0.418 -0.068  0.217] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          53 +45 to_pic ction2 [ 0.413 -0.053  0.216] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          54 +46 to_pic ction2 [0.399 0.008 0.211] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          55 +47 to_pic ction2 [0.395 0.02  0.144] sc 1.0 g 0 gr 0.0 np 1 dq 0.01
          56 +48 grasp ction2 [0.395 0.02  0.14 ] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          57 +49 to_pla ction2 [0.395 0.02  0.14 ] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          58 +50 to_pla ction2 [0.395 0.02  0.14 ] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
          59 +51 to_pla ction2 [0.395 0.02  0.14 ] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
          60 +52 to_pla ction2 [0.396 0.022 0.157] sc 1.0 g 1 gr 0.0 np 5 dq 0.17
          61 +53 to_pla ction2 [0.396 0.022 0.157] sc 0.5 g 1 gr 0.0 np 5 dq 0.08
          62 +54 to_pla ction2 [0.396 0.022 0.157] sc 0.25 g 1 gr 0.0 np 5 dq 0.04
          63 +55 to_pla ction2 [0.396 0.022 0.157] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
          64 +56 to_pla ction2 [0.396 0.022 0.157] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
          65 +57 to_pla ction2 [0.396 0.022 0.161] sc 1.0 g 1 gr 0.0 np 5 dq 0.16
          66 +58 to_pla ction2 [0.396 0.022 0.161] sc 0.5 g 1 gr 0.0 np 5 dq 0.08
          67 +59 to_pla ction2 [0.396 0.022 0.161] sc 0.25 g 1 gr 0.0 np 5 dq 0.04
          68 +60 to_pla ction2 [0.396 0.022 0.161] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
          69 +61 to_pla ction2 [0.396 0.022 0.161] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
          70 +62 to_pla ction2 [0.396 0.022 0.164] sc 1.0 g 1 gr 0.0 np 5 dq 0.15
          71 +63 to_pla ction2 [0.396 0.022 0.164] sc 0.5 g 1 gr 0.0 np 5 dq 0.07
          72 +64 to_pla ction2 [0.396 0.022 0.164] sc 0.25 g 1 gr 0.0 np 5 dq 0.04
          73 +65 to_pla ction2 [0.396 0.022 0.164] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
          74 +66 to_pla ction2 [0.396 0.022 0.164] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
          75 +67 releas ction2 [0.396 0.022 0.164] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
          76 +68 releas ction2 [0.396 0.022 0.164] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          77 +69 releas ction2 [0.396 0.022 0.161] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          78 +70 releas ction2 [0.396 0.022 0.161] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          79 +71 releas ction2 [0.396 0.022 0.161] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          80 +72 releas ction2 [0.396 0.022 0.158] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          81 +73 releas ction2 [0.396 0.022 0.158] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          82 +74 releas ction2 [0.396 0.022 0.158] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          83 +75 releas ction2 [0.396 0.022 0.155] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          84 +76 releas ction2 [0.396 0.022 0.155] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          85 +77 releas ction2 [0.396 0.022 0.155] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          86 +78 releas ction2 [0.396 0.022 0.152] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          87 +79 releas ction2 [0.396 0.022 0.152] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          88 +80 releas ction2 [0.396 0.022 0.152] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          89 +81 releas ction2 [0.396 0.022 0.149] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          90 +82 releas ction2 [0.396 0.022 0.149] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          91 +83 releas ction2 [0.396 0.022 0.149] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          92 +84 releas ction2 [0.396 0.022 0.146] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          93 +85 releas ction2 [0.396 0.022 0.146] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          94 +86 releas ction2 [0.396 0.022 0.146] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          95 +87 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          96 +88 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          97 +89 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
          98 +90 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          99 +91 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         100 +92 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         101 +93 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         102 +94 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         103 +95 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         104 +96 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         105 +97 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         106 +98 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         107 +99 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         108 +100 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         109 +101 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         110 +102 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         111 +103 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         112 +104 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         113 +105 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         114 +106 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         115 +107 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         116 +108 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         117 +109 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         118 +110 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         119 +111 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         120 +112 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         121 +113 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         122 +114 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         123 +115 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         124 +116 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         125 +117 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         126 +118 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         127 +119 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         128 +120 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         129 +121 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         130 +122 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         131 +123 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         132 +124 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         133 +125 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         134 +126 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         135 +127 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         136 +128 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         137 +129 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         138 +130 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         139 +131 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         140 +132 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         141 +133 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         142 +134 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         143 +135 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         144 +136 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         145 +137 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         146 +138 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         147 +139 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         148 +140 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         149 +141 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         150 +142 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         151 +143 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         152 +144 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         153 +145 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         154 +146 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         155 +147 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         156 +148 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         157 +149 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         158 +150 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         159 +151 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         160 +152 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         161 +153 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         162 +154 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         163 +155 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         164 +156 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         165 +157 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         166 +158 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         167 +159 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         168 +160 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         169 +161 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         170 +162 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         171 +163 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         172 +164 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         173 +165 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         174 +166 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         175 +167 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         176 +168 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         177 +169 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         178 +170 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         179 +171 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         180 +172 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         181 +173 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         182 +174 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         183 +175 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         184 +176 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         185 +177 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         186 +178 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         187 +179 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         188 +180 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         189 +181 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         190 +182 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         191 +183 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         192 +184 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         193 +185 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         194 +186 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         195 +187 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         196 +188 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         197 +189 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         198 +190 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         199 +191 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         200 +192 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         201 +193 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         202 +194 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         203 +195 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         204 +196 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         205 +197 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         206 +198 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         207 +199 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         208 +200 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         209 +201 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         210 +202 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         211 +203 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         212 +204 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         213 +205 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         214 +206 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         215 +207 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         216 +208 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         217 +209 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         218 +210 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         219 +211 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         220 +212 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         221 +213 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         222 +214 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         223 +215 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         224 +216 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         225 +217 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         226 +218 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         227 +219 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         228 +220 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         229 +221 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         230 +222 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         231 +223 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         232 +224 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         233 +225 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         234 +226 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         235 +227 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         236 +228 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         237 +229 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         238 +230 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         239 +231 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         240 +232 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         241 +233 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         242 +234 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         243 +235 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         244 +236 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         245 +237 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         246 +238 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         247 +239 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         248 +240 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         249 +241 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         250 +242 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         251 +243 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         252 +244 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         253 +245 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         254 +246 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         255 +247 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         256 +248 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         257 +249 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         258 +250 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         259 +251 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         260 +252 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         261 +253 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         262 +254 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         263 +255 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         264 +256 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         265 +257 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         266 +258 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         267 +259 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         268 +260 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         269 +261 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         270 +262 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         271 +263 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         272 +264 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         273 +265 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         274 +266 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         275 +267 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         276 +268 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         277 +269 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         278 +270 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         279 +271 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         280 +272 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         281 +273 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         282 +274 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         283 +275 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         284 +276 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         285 +277 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         286 +278 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         287 +279 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         288 +280 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         289 +281 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         290 +282 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         291 +283 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         292 +284 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         293 +285 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         294 +286 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         295 +287 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         296 +288 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         297 +289 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         298 +290 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         299 +291 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         300 +292 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         301 +293 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         302 +294 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         303 +295 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         304 +296 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         305 +297 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         306 +298 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         307 +299 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         308 +300 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         309 +301 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         310 +302 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         311 +303 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         312 +304 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         313 +305 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         314 +306 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         315 +307 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         316 +308 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         317 +309 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         318 +310 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         319 +311 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         320 +312 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         321 +313 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         322 +314 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         323 +315 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         324 +316 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         325 +317 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         326 +318 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         327 +319 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         328 +320 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         329 +321 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         330 +322 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         331 +323 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         332 +324 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         333 +325 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         334 +326 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         335 +327 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         336 +328 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         337 +329 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         338 +330 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         339 +331 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         340 +332 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         341 +333 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         342 +334 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         343 +335 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         344 +336 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         345 +337 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         346 +338 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         347 +339 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         348 +340 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         349 +341 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         350 +342 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         351 +343 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         352 +344 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         353 +345 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         354 +346 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         355 +347 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         356 +348 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         357 +349 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         358 +350 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         359 +351 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         360 +352 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         361 +353 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         362 +354 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         363 +355 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         364 +356 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         365 +357 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         366 +358 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         367 +359 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         368 +360 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         369 +361 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         370 +362 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         371 +363 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         372 +364 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         373 +365 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         374 +366 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         375 +367 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         376 +368 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         377 +369 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         378 +370 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         379 +371 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         380 +372 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         381 +373 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         382 +374 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         383 +375 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         384 +376 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         385 +377 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         386 +378 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         387 +379 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.16
         388 +380 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         389 +381 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         390 +382 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         391 +383 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         392 +384 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         393 +385 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         394 +386 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         395 +387 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         396 +388 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         397 +389 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.16
         398 +390 grasp ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         399 +391 to_pla ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         400 +392 to_pla ction2 [0.396 0.022 0.143] sc 0.5 g 1 gr 0.0 np 5 dq 0.1
         401 +393 to_pla ction2 [0.396 0.022 0.143] sc 0.25 g 1 gr 0.0 np 5 dq 0.05
         402 +394 to_pla ction2 [0.396 0.022 0.143] sc 0.125 g 1 gr 0.0 np 5 dq 0.02
         403 +395 to_pla ction2 [0.396 0.022 0.143] sc 0.0625 g 1 gr 0.0 np 5 dq 0.01
         404 +396 releas ction2 [0.396 0.022 0.143] sc 1.0 g 1 gr 1.0 np 5 dq 0.0
         405 +397 retrea ction2 [0.396 0.022 0.143] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
         406 +398 retrea ction2 [0.396 0.022 0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
         407 +399 to_pic ction2 [0.396 0.022 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.16
diff --git a/probe215.py b/probe215.py
new file mode 100644
index 0000000..39b11d7
--- /dev/null
+++ b/probe215.py
@@ -0,0 +1,22 @@
           1 +import numpy as np
           2 +from th import H
           3 +from approach import GeneratedApproach
           4 +from kin import fk
           5 +h=H(215,oc=5)
           6 +ap=GeneratedApproach(None,None,{}); ap.reset(h.obs,{})
           7 +for t in range(49):
           8 +    a=ap.get_action(h.obs); h.step(a)
           9 +print('grasped',h.grasped(), 'yaw', ap.task['yaw'])
          10 +M=h.tool(); p=M[:3,3]; print('tool',p.round(3))
          11 +print('grasp_tf', [round(h.obs.get(h.R,f),3) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']])
          12 +for n in ['obstruction2','obstruction1','obstruction0','obstruction4']: print(n,h.pose(n)[:3].round(3), h.he(n).round(3))
          13 +q0=h.q()
          14 +from kin import ik, down_R
          15 +y=ap.task['yaw']
          16 +for d in [(0,0,0.01),(0.01,0,0),(-0.01,0,0),(0,0.01,0),(0,-0.01,0),(0,0,-0.003)]:
          17 +    qt,e=ik(h.base(),q0,p+np.array(d),down_R(y))
          18 +    a=np.zeros(11); a[3:10]=np.clip(qt-q0,-.2,.2); h.step(a)
          19 +    moved=not np.allclose(h.q(),q0)
          20 +    print(d,'moved',moved)
          21 +    if moved:
          22 +        a=np.zeros(11); a[3:10]=np.clip(q0-h.q(),-.2,.2); h.step(a)
diff --git a/probe215b.py b/probe215b.py
new file mode 100644
index 0000000..ba1d95c
--- /dev/null
+++ b/probe215b.py
@@ -0,0 +1,25 @@
           1 +import numpy as np
           2 +from th import H
           3 +from approach import GeneratedApproach
           4 +from kin import fk, ik, down_R, rot_err
           5 +h=H(215,oc=5)
           6 +ap=GeneratedApproach(None,None,{}); ap.reset(h.obs,{})
           7 +for t in range(49):
           8 +    a=ap.get_action(h.obs); h.step(a)
           9 +a=ap.get_action(h.obs)
          10 +print('path', [ (np.round(w[0],3) if isinstance(w,tuple) else np.round(w,3)) for w in ap.path][:6])
          11 +print('action dq', a[3:10].round(3), 'grip', a[10])
          12 +M=h.tool(); print('cur yaw', np.arctan2(M[1,0],M[0,0]), 'ori err', rot_err(M[:3,:3], down_R(ap.task['yaw'])).round(3))
          13 +q0=h.q()
          14 +for frac in [1,0.5,0.25,0.1,0.05]:
          15 +    b=a.copy(); b[3:10]*=frac; h.step(b); moved=not np.allclose(h.q(),q0)
          16 +    print(frac,'moved',moved, h.tool()[:3,3].round(3))
          17 +    if moved: break
          18 +q1=h.q(); p=h.tool()[:3,3]; y=ap.task['yaw']
          19 +print('grasp_tf', [round(h.obs.get(h.R,f),3) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']], 'obj', h.pose('obstruction2')[:3].round(3))
          20 +for d in [(0,0,0.005),(0,0,-0.005),(0.005,0,0),(-0.005,0,0),(0,0.005,0),(0,-0.005,0)]:
          21 +    qt,e=ik(h.base(),q1,p+np.array(d),down_R(y))
          22 +    b=np.zeros(11); b[3:10]=np.clip(qt-q1,-.2,.2); h.step(b)
          23 +    moved=not np.allclose(h.q(),q1); print(d,'moved',moved)
          24 +    if moved:
          25 +        b=np.zeros(11); b[3:10]=np.clip(q1-h.q(),-.2,.2); h.step(b); print(' back', np.allclose(h.q(),q1))
```

</details>

<a id="C011"></a>
### C011 · Tilt tool toward mount for targets near the arm base

Commit `020542133848bbf90eac9df3c5cdc2d29c80fb1a`; parents: d6f9c2860017345fcfbd1dfe2bcc8b1c1b1eabc2. Recorded author date: 2026-09-28T21:30:36+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0738](01_timeline.md#E0738): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_0205421_approach.py) · [Exact all-file diff](evidence/diffs/C011_0205421.diff)

[Previous saved controller snapshot](evidence/versions/C010_d6f9c28_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2890c25..514364e 100644
--- a/approach.py
+++ b/approach.py
@@ -55,6 +55,7 @@ class GeneratedApproach:
   55     55          self.last_cmd = None
   56     56          self.blocked = 0
   57     57          self.scale = 1.0
          58 +        self.tilt = (0.0, 0.0)
   58     59          self.fail = {}
   59     60          self.t = 0
   60     61          self.wait = 0
@@ -168,7 +169,7 @@ class GeneratedApproach:
  168    169                  bad = any(np.hypot(x - b[0], y - b[1]) < 0.04 for b in self.fail.get(name, []))
  169    170                  if bad:
  170    171                      continue
  171        -                v = min(clear, 0.05) + min(kb, 0.10) - 0.08 * np.hypot(x - p0[0], y - p0[1])
         172 +                v = min(clear, 0.05) + min(kb, 0.10) - 0.08 * np.hypot(x - p0[0], y - p0[1]) - 0.2 * self._tilt_needed(np.hypot(*(xy - self._mount())))
  172    173                  if v > bestv:
  173    174                      bestv, best = v, xy
  174    175          if best is None:
@@ -229,6 +230,7 @@ class GeneratedApproach:
  229    230          p, he = self.objs[n]
  230    231          self.task['yaw'] = yaw
  231    232          self.task['yaw_place'] = yaw
         233 +        self._set_tilt(p[:2], self.task['dest'])
  232    234          self.phase = 'to_pick'
  233    235          tool = fk(self.base, self.q)[:3, 3]
  234    236          sz = self._safe_z(None, 0.05)
@@ -241,6 +243,33 @@ class GeneratedApproach:
  241    243          path += self._line(pick_above, np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ]), VSTEP)
  242    244          self._set_path(path, self.task['yaw'])
  243    245  
         246 +    def _mount(self):
         247 +        return np.array([self.base[0] + 0.12 * np.cos(self.base[2]),
         248 +                         self.base[1] + 0.12 * np.sin(self.base[2])])
         249 +
         250 +    @staticmethod
         251 +    def _tilt_needed(r):
         252 +        return float(np.clip((0.15 - r) * 8.0, 0.0, 0.35))
         253 +
         254 +    def _set_tilt(self, a, b):
         255 +        m = self._mount()
         256 +        best = (0.0, 0.0)
         257 +        for xy in (a, b):
         258 +            d = np.asarray(xy[:2]) - m
         259 +            t = self._tilt_needed(np.hypot(*d))
         260 +            if t > best[0]:
         261 +                best = (t, np.arctan2(d[1], d[0]))
         262 +        self.tilt = best
         263 +
         264 +    def _Rot(self, yaw):
         265 +        R = down_R(yaw)
         266 +        t, phi = self.tilt
         267 +        if t <= 0:
         268 +            return R
         269 +        ax = np.array([-np.sin(phi), np.cos(phi), 0.0])
         270 +        K = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
         271 +        return (np.eye(3) + np.sin(t) * K + (1 - np.cos(t)) * K @ K) @ R
         272 +
  244    273      def _yaw_for(self, xy):
  245    274          mx = self.base[0] + 0.12 * np.cos(self.base[2])
  246    275          my = self.base[1] + 0.12 * np.sin(self.base[2])
@@ -273,7 +302,7 @@ class GeneratedApproach:
  273    302  
  274    303      # -------------------------------------------------------------- control
  275    304      def _ik(self, pos, yaw):
  276        -        q, err = ik(self.base, self.q, pos, down_R(yaw), iters=60)
         305 +        q, err = ik(self.base, self.q, pos, self._Rot(yaw), iters=60)
  277    306          for i, lim in JLIM.items():
  278    307              q[i] = np.clip(q[i], -lim, lim)
  279    308          return q, err
@@ -286,7 +315,7 @@ class GeneratedApproach:
  286    315              final = len(self.path) == 1
  287    316              tol = 5e-4 if final else 0.03
  288    317              e = np.linalg.norm(M[:3, 3] - pos)
  289        -            eo = np.linalg.norm(rot_err(M[:3, :3], down_R(yaw)))
         318 +            eo = np.linalg.norm(rot_err(M[:3, :3], self._Rot(yaw)))
  290    319              if e < tol and (eo < (0.01 if final else 0.1)):
  291    320                  self.path.pop(0)
  292    321                  continue
diff --git a/d312.txt b/d312.txt
new file mode 100644
index 0000000..e8038b5
--- /dev/null
+++ b/d312.txt
@@ -0,0 +1,257 @@
           1 +obstruction3 [0.106 0.006 0.1  ] [0.018 0.013 0.015]
           2 +obstruction1 [0.171 0.009 0.104] [0.015 0.016 0.019]
           3 +target_region [0.143 0.038 0.08 ] [0.036 0.031 0.005]
           4 +obstruction4 [0.345 0.1   0.087] [0.014 0.016 0.012]
           5 +obstruction0 [0.126 0.034 0.111] [0.015 0.013 0.026]
           6 +target_block [ 0.47  -0.266  0.1  ] [0.029 0.025 0.025]
           7 +obstruction2 [0.166 0.064 0.113] [0.02  0.018 0.028]
           8 +0 to_pic ction1 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
           9 +1 to_pic ction1 [0.157 0.002 0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          10 +2 to_pic ction1 [0.16  0.003 0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          11 +3 to_pic ction1 [0.164 0.005 0.22 ] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          12 +4 to_pic ction1 [0.167 0.007 0.22 ] sc 1.0 g 0 gr 0.0 np 2 dq 0.19
          13 +5 to_pic ction1 [0.171 0.009 0.221] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          14 +6 to_pic ction1 [0.173 0.008 0.18 ] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
          15 +7 grasp ction1 [0.171 0.009 0.155] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          16 +8 to_pla ction1 [0.171 0.009 0.155] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          17 +9 to_pla ction1 [0.171 0.009 0.192] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          18 +10 to_pla ction1 [0.172 0.009 0.234] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          19 +11 to_pla ction1 [ 0.173 -0.039  0.239] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          20 +12 to_pla ction1 [ 0.175 -0.091  0.241] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
          21 +13 to_pla ction1 [ 0.172 -0.115  0.196] sc 1.0 g 1 gr 0.0 np 1 dq 0.2
          22 +14 to_pla ction1 [ 0.172 -0.117  0.154] sc 1.0 g 1 gr 0.0 np 1 dq 0.04
          23 +15 releas ction1 [ 0.171 -0.117  0.146] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          24 +16 retrea ction1 [ 0.171 -0.117  0.146] sc 1.0 g 0 gr 0.0 np 2 dq 0.15
          25 +17 retrea ction1 [ 0.171 -0.117  0.176] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
          26 +18 to_pic ction3 [ 0.171 -0.117  0.206] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          27 +19 to_pic ction3 [ 0.172 -0.117  0.21 ] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          28 +20 to_pic ction3 [ 0.172 -0.117  0.214] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          29 +21 to_pic ction3 [ 0.171 -0.117  0.217] sc 1.0 g 0 gr 0.0 np 4 dq 0.18
          30 +22 to_pic ction3 [ 0.171 -0.117  0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
          31 +23 to_pic ction3 [ 0.139 -0.055  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          32 +24 to_pic ction3 [ 0.139 -0.055  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.05
          33 +25 to_pic ction3 [ 0.13  -0.038  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.15
          34 +26 to_pic ction3 [ 0.13  -0.038  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.06
          35 +27 to_pic ction3 [ 0.13  -0.038  0.221] sc 0.25 g 0 gr 0.0 np 2 dq 0.03
          36 +28 to_pic ction3 [ 0.125 -0.029  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.06
          37 +29 to_pic ction3 [ 0.125 -0.029  0.221] sc 0.25 g 0 gr 0.0 np 2 dq 0.03
          38 +30 to_pic ction3 [ 0.125 -0.029  0.221] sc 0.125 g 0 gr 0.0 np 2 dq 0.01
          39 +31 to_pic ction3 [ 0.125 -0.029  0.221] sc 0.0625 g 0 gr 0.0 np 2 dq 0.01
          40 +32 to_pic ction3 [ 0.124 -0.026  0.221] sc 0.125 g 0 gr 0.0 np 2 dq 0.01
          41 +33 to_pic ction3 [ 0.124 -0.026  0.221] sc 0.0625 g 0 gr 0.0 np 2 dq 0.01
          42 +34 grasp ction3 [ 0.124 -0.026  0.221] sc 1.0 g 0 gr -1.0 np 2 dq 0.0
          43 +35 to_pic ction0 [ 0.124 -0.026  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          44 +36 to_pic ction0 [ 0.124 -0.026  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.09
          45 +37 to_pic ction0 [ 0.124 -0.026  0.221] sc 0.25 g 0 gr 0.0 np 2 dq 0.04
          46 +38 to_pic ction0 [ 0.124 -0.026  0.221] sc 0.125 g 0 gr 0.0 np 2 dq 0.02
          47 +39 to_pic ction0 [ 0.124 -0.026  0.221] sc 0.0625 g 0 gr 0.0 np 2 dq 0.01
          48 +40 to_pic ction0 [ 0.124 -0.024  0.221] sc 0.125 g 0 gr 0.0 np 2 dq 0.02
          49 +41 to_pic ction0 [ 0.124 -0.024  0.221] sc 0.0625 g 0 gr 0.0 np 2 dq 0.01
          50 +42 grasp ction0 [ 0.124 -0.024  0.221] sc 1.0 g 0 gr -1.0 np 2 dq 0.0
          51 +43 to_pic ction2 [ 0.124 -0.024  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          52 +44 to_pic ction2 [0.149 0.009 0.222] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          53 +45 to_pic ction2 [0.164 0.054 0.221] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          54 +46 to_pic ction2 [0.166 0.06  0.182] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
          55 +47 grasp ction2 [0.166 0.064 0.172] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          56 +48 to_pla ction2 [0.166 0.064 0.172] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          57 +49 to_pla ction2 [0.166 0.063 0.209] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          58 +50 to_pla ction2 [0.166 0.064 0.253] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          59 +51 to_pla ction2 [0.171 0.106 0.253] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          60 +52 to_pla ction2 [0.175 0.131 0.25 ] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          61 +53 to_pla ction2 [0.177 0.163 0.251] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          62 +54 to_pla ction2 [0.172 0.201 0.254] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
          63 +55 to_pla ction2 [0.173 0.202 0.218] sc 1.0 g 1 gr 0.0 np 1 dq 0.2
          64 +56 to_pla ction2 [0.174 0.203 0.174] sc 1.0 g 1 gr 0.0 np 1 dq 0.04
          65 +57 releas ction2 [0.171 0.204 0.163] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          66 +58 retrea ction2 [0.171 0.204 0.163] sc 1.0 g 0 gr 0.0 np 2 dq 0.12
          67 +59 retrea ction2 [0.171 0.204 0.193] sc 1.0 g 0 gr 0.0 np 1 dq 0.13
          68 +60 to_pic ction0 [0.171 0.204 0.223] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          69 +61 to_pic ction0 [0.165 0.162 0.222] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          70 +62 to_pic ction0 [0.154 0.129 0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          71 +63 to_pic ction0 [0.15  0.084 0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          72 +64 to_pic ction0 [0.137 0.049 0.218] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          73 +65 to_pic ction0 [0.131 0.038 0.18 ] sc 1.0 g 0 gr 0.0 np 1 dq 0.07
          74 +66 grasp ction0 [0.126 0.034 0.168] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          75 +67 to_pla ction0 [0.126 0.034 0.168] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          76 +68 to_pla ction0 [0.126 0.034 0.168] sc 0.5 g 1 gr 0.0 np 5 dq 0.12
          77 +69 to_pla ction0 [0.126 0.034 0.188] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          78 +70 to_pla ction0 [0.128 0.034 0.227] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          79 +71 to_pla ction0 [0.201 0.02  0.244] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          80 +72 to_pla ction0 [0.272 0.005 0.247] sc 1.0 g 1 gr 0.0 np 2 dq 0.16
          81 +73 to_pla ction0 [ 0.3   -0.     0.203] sc 1.0 g 1 gr 0.0 np 1 dq 0.15
          82 +74 releas ction0 [ 0.3  -0.    0.16] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          83 +75 retrea ction0 [ 0.3  -0.    0.16] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
          84 +76 retrea ction0 [ 0.3  -0.    0.19] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
          85 +77 to_pic ction3 [ 0.3  -0.    0.22] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          86 +78 to_pic ction3 [ 0.259 -0.     0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          87 +79 to_pic ction3 [0.218 0.002 0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          88 +80 to_pic ction3 [ 0.152 -0.002  0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.15
          89 +81 to_pic ction3 [ 0.152 -0.002  0.219] sc 0.5 g 0 gr 0.0 np 2 dq 0.08
          90 +82 to_pic ction3 [0.133 0.001 0.216] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          91 +83 to_pic ction3 [0.134 0.002 0.182] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
          92 +84 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          93 +85 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          94 +86 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          95 +87 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          96 +88 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          97 +89 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          98 +90 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          99 +91 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         100 +92 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         101 +93 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         102 +94 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         103 +95 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         104 +96 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         105 +97 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         106 +98 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         107 +99 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         108 +100 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         109 +101 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         110 +102 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         111 +103 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         112 +104 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         113 +105 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         114 +106 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         115 +107 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         116 +108 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         117 +109 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         118 +110 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         119 +111 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         120 +112 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         121 +113 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         122 +114 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         123 +115 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         124 +116 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         125 +117 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         126 +118 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         127 +119 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         128 +120 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         129 +121 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         130 +122 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         131 +123 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         132 +124 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         133 +125 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         134 +126 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         135 +127 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         136 +128 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         137 +129 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         138 +130 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         139 +131 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         140 +132 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         141 +133 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         142 +134 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         143 +135 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         144 +136 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         145 +137 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         146 +138 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         147 +139 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         148 +140 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         149 +141 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         150 +142 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         151 +143 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         152 +144 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         153 +145 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         154 +146 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         155 +147 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         156 +148 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         157 +149 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         158 +150 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         159 +151 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         160 +152 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         161 +153 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         162 +154 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         163 +155 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         164 +156 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         165 +157 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         166 +158 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         167 +159 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         168 +160 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         169 +161 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         170 +162 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         171 +163 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         172 +164 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         173 +165 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         174 +166 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         175 +167 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         176 +168 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         177 +169 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         178 +170 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         179 +171 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         180 +172 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         181 +173 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         182 +174 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         183 +175 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         184 +176 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         185 +177 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         186 +178 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         187 +179 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         188 +180 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         189 +181 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         190 +182 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         191 +183 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         192 +184 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         193 +185 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         194 +186 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         195 +187 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         196 +188 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         197 +189 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         198 +190 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         199 +191 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         200 +192 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         201 +193 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         202 +194 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         203 +195 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         204 +196 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         205 +197 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         206 +198 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         207 +199 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         208 +200 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         209 +201 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         210 +202 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         211 +203 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         212 +204 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         213 +205 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         214 +206 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         215 +207 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         216 +208 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         217 +209 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         218 +210 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         219 +211 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         220 +212 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         221 +213 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         222 +214 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         223 +215 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         224 +216 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         225 +217 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         226 +218 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         227 +219 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         228 +220 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         229 +221 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         230 +222 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         231 +223 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         232 +224 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         233 +225 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         234 +226 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         235 +227 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         236 +228 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         237 +229 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         238 +230 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         239 +231 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         240 +232 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         241 +233 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         242 +234 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         243 +235 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         244 +236 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         245 +237 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         246 +238 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         247 +239 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         248 +240 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         249 +241 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         250 +242 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         251 +243 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         252 +244 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         253 +245 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         254 +246 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         255 +247 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         256 +248 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         257 +249 to_pic ction3 [0.129 0.004 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
diff --git a/dbg3.py b/dbg3.py
index 0e96f4b..c97bb29 100644
--- a/dbg3.py
+++ b/dbg3.py
@@ -6,7 +6,7 @@ seed=int(sys.argv[1]); oc=int(sys.argv[2]) if len(sys.argv)>2 else None
    6      6  env = make_env(); obs, info = env.reset(seed=seed, options={'object_count':oc} if oc is not None else None)
    7      7  ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    8      8  for n,(p,he) in ap.objs.items(): print(n, p.round(3), he.round(3))
    9        -for t in range(400):
           9 +for t in range(int(__import__("os").environ.get("NS","400"))):
   10     10      a = ap.get_action(obs); obs, r, te, *_ = env.step(a)
   11     11      tool = fk(ap.base, ap.q)[:3,3]
   12     12      print(t, ap.phase[:6], (ap.task or {}).get('name','')[-6:], tool.round(3), 'sc', ap.scale, 'g', int(ap.grasped), 'gr', a[10], 'np', len(ap.path), 'dq', np.abs(a[3:10]).max().round(2))
diff --git a/reach.py b/reach.py
new file mode 100644
index 0000000..8f8e695
--- /dev/null
+++ b/reach.py
@@ -0,0 +1,15 @@
           1 +import numpy as np
           2 +from kin import ik, down_R, fk
           3 +from th import H
           4 +h=H(312,oc=5); base=h.base(); print('base',base, 'q',h.q().round(2))
           5 +rng=np.random.default_rng(0)
           6 +JL={1:2.41,3:2.66,5:2.23}
           7 +for pos in [(0.106,0.006,0.146),(0.13,0.005,0.153),(0.106,0.006,0.2),(0.2,0.0,0.146),(0.12,0.1,0.146)]:
           8 +    best=None
           9 +    for t in range(100):
          10 +        q0=rng.uniform(-2.2,2.2,7)
          11 +        for yaw in [0, np.pi/2]:
          12 +            q,e=ik(base,q0,np.array(pos),down_R(yaw),iters=200)
          13 +            ok=all(abs(q[i])<=JL[i] for i in JL)
          14 +            if ok and (best is None or e<best[0]): best=(e,yaw,q.round(2))
          15 +    print(pos,best)
diff --git a/tilt.py b/tilt.py
new file mode 100644
index 0000000..2c2ae11
--- /dev/null
+++ b/tilt.py
@@ -0,0 +1,19 @@
           1 +import numpy as np
           2 +from kin import ik, down_R, fk
           3 +from th import H
           4 +def Ry(a):
           5 +    c,s=np.cos(a),np.sin(a); return np.array([[c,0,s],[0,1,0],[-s,0,c]])
           6 +h=H(312,oc=5); base=h.base()
           7 +rng=np.random.default_rng(0)
           8 +JL={1:2.41,3:2.66,5:2.23}
           9 +pos=np.array((0.106,0.006,0.146))
          10 +for tilt in [0.2,0.4,0.6]:
          11 +    for yaw in [0,np.pi/2]:
          12 +        R=Ry(tilt)@down_R(yaw)   # world-frame rotation about y: tool z axis leans
          13 +        best=None
          14 +        for t in range(60):
          15 +            q0=rng.uniform(-2.2,2.2,7)
          16 +            q,e=ik(base,q0,pos,R,iters=200)
          17 +            ok=all(abs(q[i])<=JL[i] for i in JL)
          18 +            if ok and (best is None or e<best[0]): best=(e,q)
          19 +        print(tilt,yaw,None if best is None else best[0], fk(base,best[1])[:3,2].round(2) if best else '')
diff --git a/tilt2.py b/tilt2.py
new file mode 100644
index 0000000..ca27ad0
--- /dev/null
+++ b/tilt2.py
@@ -0,0 +1,23 @@
           1 +import numpy as np
           2 +from kin import ik, down_R, fk
           3 +from th import H
           4 +def Rax(ax,a):
           5 +    ax=np.asarray(ax,float); K=np.array([[0,-ax[2],ax[1]],[ax[2],0,-ax[0]],[-ax[1],ax[0],0]])
           6 +    return np.eye(3)+np.sin(a)*K+(1-np.cos(a))*K@K
           7 +h=H(312,oc=5); base=h.base()
           8 +n='obstruction3'; p=h.pose(n)[:3]; he=h.he(n)
           9 +R=Rax((0,1,0),0.3)@down_R(np.pi/2)
          10 +def go(pos):
          11 +    for k in range(40):
          12 +        q=h.q(); qt,e=ik(base,q,np.asarray(pos,float),R,iters=100)
          13 +        d=qt-q; m=np.abs(d).max()
          14 +        if m<1e-4: break
          15 +        a=np.zeros(11); a[3:10]=d*min(1,0.2/m); h.step(a)
          16 +        if np.allclose(h.q(),q): print(' blocked'); break
          17 +    print('at',h.tool()[:3,3].round(3),'target',np.round(pos,3), 'e',e)
          18 +top=p[2]+he[2]
          19 +go((p[0],p[1],0.25)); go((p[0],p[1],top+0.03))
          20 +h.grip(-1); print('grasped',h.grasped(), [round(h.obs.get(h.R,f),3) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
          21 +go((p[0]+0.15,p[1],0.25)); go((p[0]+0.15,p[1],top+0.03+0.001))
          22 +print('obj pose', h.pose(n).round(3))
          23 +h.grip(1); print('grasped after open',h.grasped(), h.pose(n).round(3))
diff --git a/tilt3.py b/tilt3.py
new file mode 100644
index 0000000..4bce27a
--- /dev/null
+++ b/tilt3.py
@@ -0,0 +1,23 @@
           1 +import numpy as np, sys
           2 +from kin import ik, down_R, fk
           3 +from th import H
           4 +def Rax(ax,a):
           5 +    ax=np.asarray(ax,float); K=np.array([[0,-ax[2],ax[1]],[ax[2],0,-ax[0]],[-ax[1],ax[0],0]])
           6 +    return np.eye(3)+np.sin(a)*K+(1-np.cos(a))*K@K
           7 +tilt=float(sys.argv[1]); dz=float(sys.argv[2]); yaw=float(sys.argv[3])
           8 +h=H(312,oc=5); base=h.base()
           9 +n='target_block'; p=h.pose(n)[:3]; he=h.he(n)
          10 +R=Rax((0,1,0),tilt)@down_R(yaw)
          11 +def go(pos):
          12 +    for k in range(40):
          13 +        q=h.q(); qt,e=ik(base,q,np.asarray(pos,float),R,iters=100)
          14 +        d=qt-q; m=np.abs(d).max()
          15 +        if m<1e-4: break
          16 +        a=np.zeros(11); a[3:10]=d*min(1,0.2/m); h.step(a)
          17 +        if np.allclose(h.q(),q): print(' blocked'); break
          18 +    return h.tool()[:3,3].round(3)
          19 +top=p[2]+he[2]
          20 +go((p[0],p[1],0.25)); print(go((p[0],p[1],top+dz)))
          21 +h.grip(-1); print('tilt',tilt,'dz',dz,'grasped',h.grasped(), [round(h.obs.get(h.R,f),3) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
          22 +if h.grasped():
          23 +    print(go((p[0]-0.1,p[1],top+dz+0.001)), h.pose(n).round(3)); h.grip(1); print('released', not h.grasped(), h.pose(n).round(3))
```

</details>

<a id="C012"></a>
### C012 · Allow moving target block out of the way as blocker

Commit `cd051602be53c6f56708632c9c151d040bccf763`; parents: 020542133848bbf90eac9df3c5cdc2d29c80fb1a. Recorded author date: 2026-09-28T22:00:07+02:00.

File roles (automatic): policy, setup/other.

- [E0828](01_timeline.md#E0828): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_cd05160_approach.py) · [Exact all-file diff](evidence/diffs/C012_cd05160.diff)

[Previous saved controller snapshot](evidence/versions/C011_0205421_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 514364e..55290e5 100644
--- a/approach.py
+++ b/approach.py
@@ -198,7 +198,7 @@ class GeneratedApproach:
  198    198              scored.sort()
  199    199              if scored[0][0] > 0:
  200    200                  # try to move a blocker first
  201        -                others = [n for n in self._obstructions() if n not in need]
         201 +                others = [n for n in self._obstructions() if n not in need] + ['target_block']
  202    202                  alt = []
  203    203                  for n in others:
  204    204                      v, hits, y = self._pick_choice(n, cur)
diff --git a/d312.txt b/d312.txt
index e8038b5..fb5922e 100644
--- a/d312.txt
+++ b/d312.txt
@@ -1,10 +1,10 @@
           1 +obstruction0 [0.126 0.034 0.111] [0.015 0.013 0.026]
           2 +obstruction2 [0.166 0.064 0.113] [0.02  0.018 0.028]
    1      3  obstruction3 [0.106 0.006 0.1  ] [0.018 0.013 0.015]
    2        -obstruction1 [0.171 0.009 0.104] [0.015 0.016 0.019]
           4 +target_block [ 0.47  -0.266  0.1  ] [0.029 0.025 0.025]
    3      5  target_region [0.143 0.038 0.08 ] [0.036 0.031 0.005]
    4      6  obstruction4 [0.345 0.1   0.087] [0.014 0.016 0.012]
    5        -obstruction0 [0.126 0.034 0.111] [0.015 0.013 0.026]
    6        -target_block [ 0.47  -0.266  0.1  ] [0.029 0.025 0.025]
    7        -obstruction2 [0.166 0.064 0.113] [0.02  0.018 0.028]
           7 +obstruction1 [0.171 0.009 0.104] [0.015 0.016 0.019]
    8      8  0 to_pic ction1 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
    9      9  1 to_pic ction1 [0.157 0.002 0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   10     10  2 to_pic ction1 [0.16  0.003 0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
@@ -24,234 +24,103 @@ obstruction2 [0.166 0.064 0.113] [0.02  0.018 0.028]
   24     24  16 retrea ction1 [ 0.171 -0.117  0.146] sc 1.0 g 0 gr 0.0 np 2 dq 0.15
   25     25  17 retrea ction1 [ 0.171 -0.117  0.176] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
   26     26  18 to_pic ction3 [ 0.171 -0.117  0.206] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
   27        -19 to_pic ction3 [ 0.172 -0.117  0.21 ] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
   28        -20 to_pic ction3 [ 0.172 -0.117  0.214] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
   29        -21 to_pic ction3 [ 0.171 -0.117  0.217] sc 1.0 g 0 gr 0.0 np 4 dq 0.18
   30        -22 to_pic ction3 [ 0.171 -0.117  0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
   31        -23 to_pic ction3 [ 0.139 -0.055  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   32        -24 to_pic ction3 [ 0.139 -0.055  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.05
   33        -25 to_pic ction3 [ 0.13  -0.038  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.15
   34        -26 to_pic ction3 [ 0.13  -0.038  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.06
   35        -27 to_pic ction3 [ 0.13  -0.038  0.221] sc 0.25 g 0 gr 0.0 np 2 dq 0.03
   36        -28 to_pic ction3 [ 0.125 -0.029  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.06
   37        -29 to_pic ction3 [ 0.125 -0.029  0.221] sc 0.25 g 0 gr 0.0 np 2 dq 0.03
   38        -30 to_pic ction3 [ 0.125 -0.029  0.221] sc 0.125 g 0 gr 0.0 np 2 dq 0.01
   39        -31 to_pic ction3 [ 0.125 -0.029  0.221] sc 0.0625 g 0 gr 0.0 np 2 dq 0.01
   40        -32 to_pic ction3 [ 0.124 -0.026  0.221] sc 0.125 g 0 gr 0.0 np 2 dq 0.01
   41        -33 to_pic ction3 [ 0.124 -0.026  0.221] sc 0.0625 g 0 gr 0.0 np 2 dq 0.01
   42        -34 grasp ction3 [ 0.124 -0.026  0.221] sc 1.0 g 0 gr -1.0 np 2 dq 0.0
   43        -35 to_pic ction0 [ 0.124 -0.026  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   44        -36 to_pic ction0 [ 0.124 -0.026  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.09
   45        -37 to_pic ction0 [ 0.124 -0.026  0.221] sc 0.25 g 0 gr 0.0 np 2 dq 0.04
   46        -38 to_pic ction0 [ 0.124 -0.026  0.221] sc 0.125 g 0 gr 0.0 np 2 dq 0.02
   47        -39 to_pic ction0 [ 0.124 -0.026  0.221] sc 0.0625 g 0 gr 0.0 np 2 dq 0.01
   48        -40 to_pic ction0 [ 0.124 -0.024  0.221] sc 0.125 g 0 gr 0.0 np 2 dq 0.02
   49        -41 to_pic ction0 [ 0.124 -0.024  0.221] sc 0.0625 g 0 gr 0.0 np 2 dq 0.01
   50        -42 grasp ction0 [ 0.124 -0.024  0.221] sc 1.0 g 0 gr -1.0 np 2 dq 0.0
   51        -43 to_pic ction2 [ 0.124 -0.024  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   52        -44 to_pic ction2 [0.149 0.009 0.222] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   53        -45 to_pic ction2 [0.164 0.054 0.221] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
   54        -46 to_pic ction2 [0.166 0.06  0.182] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
   55        -47 grasp ction2 [0.166 0.064 0.172] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
   56        -48 to_pla ction2 [0.166 0.064 0.172] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
   57        -49 to_pla ction2 [0.166 0.063 0.209] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
   58        -50 to_pla ction2 [0.166 0.064 0.253] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
   59        -51 to_pla ction2 [0.171 0.106 0.253] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
   60        -52 to_pla ction2 [0.175 0.131 0.25 ] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
   61        -53 to_pla ction2 [0.177 0.163 0.251] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
   62        -54 to_pla ction2 [0.172 0.201 0.254] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
   63        -55 to_pla ction2 [0.173 0.202 0.218] sc 1.0 g 1 gr 0.0 np 1 dq 0.2
   64        -56 to_pla ction2 [0.174 0.203 0.174] sc 1.0 g 1 gr 0.0 np 1 dq 0.04
   65        -57 releas ction2 [0.171 0.204 0.163] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
   66        -58 retrea ction2 [0.171 0.204 0.163] sc 1.0 g 0 gr 0.0 np 2 dq 0.12
   67        -59 retrea ction2 [0.171 0.204 0.193] sc 1.0 g 0 gr 0.0 np 1 dq 0.13
   68        -60 to_pic ction0 [0.171 0.204 0.223] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
   69        -61 to_pic ction0 [0.165 0.162 0.222] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
   70        -62 to_pic ction0 [0.154 0.129 0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   71        -63 to_pic ction0 [0.15  0.084 0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   72        -64 to_pic ction0 [0.137 0.049 0.218] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
   73        -65 to_pic ction0 [0.131 0.038 0.18 ] sc 1.0 g 0 gr 0.0 np 1 dq 0.07
   74        -66 grasp ction0 [0.126 0.034 0.168] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
   75        -67 to_pla ction0 [0.126 0.034 0.168] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
   76        -68 to_pla ction0 [0.126 0.034 0.168] sc 0.5 g 1 gr 0.0 np 5 dq 0.12
   77        -69 to_pla ction0 [0.126 0.034 0.188] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
   78        -70 to_pla ction0 [0.128 0.034 0.227] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
   79        -71 to_pla ction0 [0.201 0.02  0.244] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
   80        -72 to_pla ction0 [0.272 0.005 0.247] sc 1.0 g 1 gr 0.0 np 2 dq 0.16
   81        -73 to_pla ction0 [ 0.3   -0.     0.203] sc 1.0 g 1 gr 0.0 np 1 dq 0.15
   82        -74 releas ction0 [ 0.3  -0.    0.16] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
   83        -75 retrea ction0 [ 0.3  -0.    0.16] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
   84        -76 retrea ction0 [ 0.3  -0.    0.19] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
   85        -77 to_pic ction3 [ 0.3  -0.    0.22] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
   86        -78 to_pic ction3 [ 0.259 -0.     0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
   87        -79 to_pic ction3 [0.218 0.002 0.218] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   88        -80 to_pic ction3 [ 0.152 -0.002  0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.15
   89        -81 to_pic ction3 [ 0.152 -0.002  0.219] sc 0.5 g 0 gr 0.0 np 2 dq 0.08
   90        -82 to_pic ction3 [0.133 0.001 0.216] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
   91        -83 to_pic ction3 [0.134 0.002 0.182] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
   92        -84 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
   93        -85 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
   94        -86 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
   95        -87 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
   96        -88 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
   97        -89 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
   98        -90 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
   99        -91 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  100        -92 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  101        -93 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  102        -94 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  103        -95 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  104        -96 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  105        -97 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  106        -98 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  107        -99 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  108        -100 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  109        -101 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  110        -102 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  111        -103 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  112        -104 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  113        -105 to_pic ction3 [0.13  0.005 0.154] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  114        -106 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  115        -107 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  116        -108 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  117        -109 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  118        -110 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  119        -111 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  120        -112 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  121        -113 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  122        -114 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  123        -115 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  124        -116 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  125        -117 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  126        -118 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  127        -119 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  128        -120 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  129        -121 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  130        -122 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  131        -123 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  132        -124 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  133        -125 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  134        -126 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  135        -127 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  136        -128 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  137        -129 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  138        -130 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  139        -131 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  140        -132 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  141        -133 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  142        -134 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  143        -135 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  144        -136 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  145        -137 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  146        -138 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  147        -139 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  148        -140 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  149        -141 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  150        -142 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  151        -143 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  152        -144 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  153        -145 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  154        -146 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  155        -147 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  156        -148 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  157        -149 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  158        -150 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  159        -151 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  160        -152 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  161        -153 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  162        -154 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  163        -155 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  164        -156 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  165        -157 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  166        -158 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  167        -159 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  168        -160 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  169        -161 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  170        -162 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  171        -163 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  172        -164 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  173        -165 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  174        -166 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  175        -167 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  176        -168 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  177        -169 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  178        -170 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  179        -171 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  180        -172 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  181        -173 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  182        -174 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  183        -175 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  184        -176 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  185        -177 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  186        -178 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  187        -179 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  188        -180 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  189        -181 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  190        -182 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  191        -183 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  192        -184 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  193        -185 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  194        -186 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  195        -187 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  196        -188 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  197        -189 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  198        -190 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  199        -191 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  200        -192 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  201        -193 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  202        -194 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  203        -195 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  204        -196 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  205        -197 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  206        -198 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  207        -199 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  208        -200 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  209        -201 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  210        -202 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  211        -203 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  212        -204 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  213        -205 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  214        -206 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  215        -207 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  216        -208 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  217        -209 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  218        -210 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  219        -211 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  220        -212 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  221        -213 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  222        -214 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  223        -215 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  224        -216 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  225        -217 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  226        -218 to_pic ction3 [0.13  0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  227        -219 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  228        -220 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  229        -221 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  230        -222 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  231        -223 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  232        -224 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  233        -225 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  234        -226 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  235        -227 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  236        -228 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  237        -229 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  238        -230 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  239        -231 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  240        -232 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  241        -233 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  242        -234 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  243        -235 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  244        -236 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  245        -237 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  246        -238 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  247        -239 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  248        -240 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  249        -241 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  250        -242 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  251        -243 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  252        -244 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  253        -245 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  254        -246 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  255        -247 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  256        -248 to_pic ction3 [0.129 0.005 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
  257        -249 to_pic ction3 [0.129 0.004 0.153] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          27 +19 to_pic ction3 [ 0.171 -0.116  0.208] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          28 +20 to_pic ction3 [ 0.17  -0.115  0.21 ] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          29 +21 to_pic ction3 [ 0.17  -0.115  0.213] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          30 +22 to_pic ction3 [ 0.17  -0.115  0.216] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          31 +23 to_pic ction3 [ 0.171 -0.116  0.22 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          32 +24 to_pic ction3 [ 0.141 -0.057  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          33 +25 to_pic ction3 [ 0.141 -0.057  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.05
          34 +26 to_pic ction3 [ 0.131 -0.04   0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.15
          35 +27 to_pic ction3 [ 0.131 -0.04   0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.06
          36 +28 to_pic ction3 [ 0.122 -0.022  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          37 +29 to_pic ction3 [ 0.122 -0.022  0.221] sc 0.5 g 0 gr 0.0 np 2 dq 0.06
          38 +30 to_pic ction3 [ 0.112 -0.004  0.221] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          39 +31 to_pic ction3 [0.113 0.001 0.178] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
          40 +32 to_pic ction3 [0.113 0.001 0.178] sc 0.5 g 0 gr 0.0 np 1 dq 0.1
          41 +33 to_pic ction3 [0.113 0.001 0.178] sc 0.25 g 0 gr 0.0 np 1 dq 0.05
          42 +34 to_pic ction3 [0.113 0.001 0.178] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
          43 +35 to_pic ction3 [0.113 0.001 0.178] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
          44 +36 to_pic ction3 [0.112 0.001 0.176] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
          45 +37 to_pic ction3 [0.112 0.001 0.176] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
          46 +38 grasp ction3 [0.112 0.001 0.176] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
          47 +39 to_pic ction0 [0.112 0.001 0.176] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          48 +40 to_pic ction0 [0.112 0.001 0.176] sc 0.5 g 0 gr 0.0 np 3 dq 0.2
          49 +41 to_pic ction0 [0.112 0.001 0.176] sc 0.25 g 0 gr 0.0 np 3 dq 0.2
          50 +42 to_pic ction0 [0.112 0.001 0.176] sc 0.125 g 0 gr 0.0 np 3 dq 0.2
          51 +43 to_pic ction0 [0.112 0.001 0.176] sc 0.0625 g 0 gr 0.0 np 3 dq 0.19
          52 +44 grasp ction0 [0.112 0.001 0.176] sc 1.0 g 0 gr -1.0 np 3 dq 0.0
          53 +45 to_pic ction2 [0.112 0.001 0.176] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          54 +46 to_pic ction2 [0.112 0.001 0.176] sc 0.5 g 0 gr 0.0 np 3 dq 0.2
          55 +47 to_pic ction2 [0.112 0.001 0.176] sc 0.25 g 0 gr 0.0 np 3 dq 0.2
          56 +48 to_pic ction2 [0.112 0.001 0.176] sc 0.125 g 0 gr 0.0 np 3 dq 0.2
          57 +49 to_pic ction2 [0.112 0.001 0.176] sc 0.0625 g 0 gr 0.0 np 3 dq 0.2
          58 +50 grasp ction2 [0.112 0.001 0.176] sc 1.0 g 0 gr -1.0 np 3 dq 0.0
          59 +51 to_pic ction3 [0.112 0.001 0.176] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          60 +52 to_pic ction3 [0.113 0.001 0.21 ] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          61 +53 to_pic ction3 [0.111 0.004 0.169] sc 1.0 g 0 gr 0.0 np 1 dq 0.13
          62 +54 grasp ction3 [0.106 0.006 0.145] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          63 +55 to_pla ction3 [0.106 0.006 0.145] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          64 +56 to_pla ction3 [0.107 0.006 0.184] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          65 +57 to_pla ction3 [0.107 0.006 0.226] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          66 +58 to_pla ction3 [ 0.186 -0.036  0.231] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          67 +59 to_pla ction3 [ 0.254 -0.071  0.233] sc 1.0 g 1 gr 0.0 np 3 dq 0.08
          68 +60 to_pla ction3 [ 0.279 -0.087  0.231] sc 1.0 g 1 gr 0.0 np 2 dq 0.15
          69 +61 to_pla ction3 [ 0.279 -0.088  0.184] sc 1.0 g 1 gr 0.0 np 1 dq 0.15
          70 +62 releas ction3 [ 0.279 -0.087  0.137] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          71 +63 retrea ction3 [ 0.279 -0.087  0.137] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          72 +64 retrea ction3 [ 0.279 -0.087  0.167] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          73 +65 to_pic ction2 [ 0.279 -0.087  0.197] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          74 +66 to_pic ction2 [ 0.279 -0.087  0.209] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
          75 +67 to_pic ction2 [ 0.279 -0.087  0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          76 +68 to_pic ction2 [ 0.231 -0.02   0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          77 +69 to_pic ction2 [0.196 0.036 0.223] sc 1.0 g 0 gr 0.0 np 2 dq 0.13
          78 +70 to_pic ction2 [0.166 0.064 0.221] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          79 +71 to_pic ction2 [0.167 0.063 0.18 ] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
          80 +72 grasp ction2 [0.166 0.064 0.172] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          81 +73 to_pla ction2 [0.166 0.064 0.172] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          82 +74 to_pla ction2 [0.166 0.064 0.211] sc 1.0 g 1 gr 0.0 np 5 dq 0.19
          83 +75 to_pla ction2 [0.166 0.064 0.254] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          84 +76 to_pla ction2 [0.171 0.107 0.254] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          85 +77 to_pla ction2 [0.177 0.144 0.253] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          86 +78 to_pla ction2 [0.175 0.187 0.254] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
          87 +79 to_pla ction2 [0.172 0.204 0.21 ] sc 1.0 g 1 gr 0.0 np 1 dq 0.18
          88 +80 releas ction2 [0.171 0.204 0.163] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          89 +81 retrea ction2 [0.171 0.204 0.163] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
          90 +82 retrea ction2 [0.171 0.204 0.193] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
          91 +83 to_pic ction0 [0.171 0.204 0.223] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          92 +84 to_pic ction0 [0.169 0.176 0.222] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          93 +85 to_pic ction0 [0.163 0.15  0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          94 +86 to_pic ction0 [0.154 0.128 0.22 ] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          95 +87 to_pic ction0 [0.15  0.087 0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          96 +88 to_pic ction0 [0.138 0.052 0.218] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          97 +89 to_pic ction0 [0.129 0.037 0.177] sc 1.0 g 0 gr 0.0 np 1 dq 0.04
          98 +90 grasp ction0 [0.126 0.034 0.168] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          99 +91 to_pla ction0 [0.126 0.034 0.168] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         100 +92 to_pla ction0 [0.13  0.032 0.207] sc 1.0 g 1 gr 0.0 np 5 dq 0.18
         101 +93 to_pla ction0 [0.126 0.034 0.245] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
         102 +94 to_pla ction0 [0.196 0.02  0.247] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
         103 +95 to_pla ction0 [0.276 0.005 0.248] sc 1.0 g 1 gr 0.0 np 2 dq 0.14
         104 +96 to_pla ction0 [ 0.3   -0.     0.203] sc 1.0 g 1 gr 0.0 np 1 dq 0.14
         105 +97 releas ction0 [0.3  0.   0.16] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
         106 +98 retrea ction0 [0.3  0.   0.16] sc 1.0 g 0 gr 0.0 np 2 dq 0.1
         107 +99 retrea ction0 [ 0.3  -0.    0.19] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
         108 +100 to_pic _block [ 0.3  -0.    0.22] sc 1.0 g 0 gr 0.0 np 5 dq 0.2
         109 +101 to_pic _block [ 0.337 -0.056  0.218] sc 1.0 g 0 gr 0.0 np 4 dq 0.18
         110 +102 to_pic _block [ 0.385 -0.133  0.216] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         111 +103 to_pic _block [ 0.425 -0.195  0.214] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
         112 +104 to_pic _block [ 0.46  -0.247  0.213] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         113 +105 grasp _block [ 0.47  -0.266  0.156] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         114 +106 to_pla _block [ 0.47  -0.266  0.156] sc 1.0 g 1 gr 0.0 np 8 dq 0.11
         115 +107 to_pla _block [ 0.47  -0.266  0.2  ] sc 1.0 g 1 gr 0.0 np 7 dq 0.11
         116 +108 to_pla _block [ 0.47  -0.266  0.243] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
         117 +109 to_pla _block [ 0.432 -0.229  0.245] sc 1.0 g 1 gr 0.0 np 6 dq 0.13
         118 +110 to_pla _block [ 0.405 -0.205  0.243] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         119 +111 to_pla _block [ 0.357 -0.159  0.244] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
         120 +112 to_pla _block [ 0.302 -0.105  0.246] sc 1.0 g 1 gr 0.0 np 4 dq 0.09
         121 +113 to_pla _block [ 0.274 -0.083  0.243] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
         122 +114 to_pla _block [ 0.212 -0.025  0.243] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
         123 +115 to_pla _block [0.156 0.028 0.245] sc 1.0 g 1 gr 0.0 np 1 dq 0.2
         124 +116 to_pla _block [0.153 0.032 0.202] sc 1.0 g 1 gr 0.0 np 1 dq 0.19
         125 +117 releas _block [0.143 0.038 0.168] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
         126 +DONE 118
diff --git a/d408.txt b/d408.txt
new file mode 100644
index 0000000..ede029e
--- /dev/null
+++ b/d408.txt
@@ -0,0 +1,90 @@
           1 +target_block [0.356 0.119 0.1  ] [0.03  0.021 0.025]
           2 +obstruction7 [ 0.146 -0.213  0.088] [0.016 0.015 0.013]
           3 +obstruction3 [ 0.109 -0.045  0.099] [0.012 0.011 0.014]
           4 +obstruction0 [ 0.119 -0.004  0.106] [0.013 0.02  0.021]
           5 +obstruction2 [ 0.148 -0.039  0.097] [0.011 0.016 0.012]
           6 +obstruction4 [ 0.172 -0.008  0.107] [0.019 0.014 0.022]
           7 +obstruction5 [ 0.204 -0.101  0.085] [0.016 0.014 0.01 ]
           8 +target_region [ 0.145 -0.024  0.08 ] [0.038 0.026 0.005]
           9 +obstruction1 [0.187 0.213 0.105] [0.016 0.019 0.03 ]
          10 +obstruction6 [ 0.148 -0.083  0.095] [0.018 0.02  0.02 ]
          11 +0 to_pic ction4 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 2 dq 0.16
          12 +1 to_pic ction4 [ 0.172 -0.008  0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          13 +2 to_pic ction4 [ 0.173 -0.007  0.175] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
          14 +3 grasp ction4 [ 0.172 -0.008  0.16 ] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          15 +4 to_pla ction4 [ 0.172 -0.008  0.16 ] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          16 +5 to_pla ction4 [ 0.176 -0.007  0.198] sc 1.0 g 1 gr 0.0 np 5 dq 0.19
          17 +6 to_pla ction4 [ 0.172 -0.008  0.239] sc 1.0 g 1 gr 0.0 np 4 dq 0.17
          18 +7 to_pla ction4 [ 0.236 -0.018  0.239] sc 1.0 g 1 gr 0.0 np 3 dq 0.16
          19 +8 to_pla ction4 [ 0.3   -0.029  0.239] sc 1.0 g 1 gr 0.0 np 2 dq 0.16
          20 +9 to_pla ction4 [ 0.3   -0.029  0.195] sc 1.0 g 1 gr 0.0 np 1 dq 0.17
          21 +10 releas ction4 [ 0.3   -0.029  0.151] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          22 +11 retrea ction4 [ 0.3   -0.029  0.151] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
          23 +12 retrea ction4 [ 0.3   -0.029  0.181] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
          24 +13 to_pic ction0 [ 0.3   -0.029  0.211] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          25 +14 to_pic ction0 [ 0.213 -0.017  0.213] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          26 +15 to_pic ction0 [ 0.129 -0.005  0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          27 +16 to_pic ction0 [ 0.124 -0.004  0.174] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          28 +17 grasp ction0 [ 0.119 -0.004  0.158] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          29 +18 to_pla ction0 [ 0.119 -0.004  0.158] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          30 +19 to_pla ction0 [ 0.123 -0.004  0.197] sc 1.0 g 1 gr 0.0 np 6 dq 0.19
          31 +20 to_pla ction0 [ 0.119 -0.004  0.237] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          32 +21 to_pla ction0 [ 0.164 -0.058  0.237] sc 1.0 g 1 gr 0.0 np 4 dq 0.19
          33 +22 to_pla ction0 [ 0.211 -0.118  0.237] sc 1.0 g 1 gr 0.0 np 3 dq 0.18
          34 +23 to_pla ction0 [ 0.257 -0.175  0.237] sc 1.0 g 1 gr 0.0 np 2 dq 0.14
          35 +24 to_pla ction0 [ 0.257 -0.175  0.193] sc 1.0 g 1 gr 0.0 np 1 dq 0.14
          36 +25 releas ction0 [ 0.257 -0.175  0.149] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          37 +26 retrea ction0 [ 0.257 -0.175  0.149] sc 1.0 g 0 gr 0.0 np 2 dq 0.1
          38 +27 retrea ction0 [ 0.257 -0.175  0.179] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
          39 +28 to_pic ction3 [ 0.257 -0.175  0.209] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          40 +29 to_pic ction3 [ 0.204 -0.128  0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          41 +30 to_pic ction3 [ 0.144 -0.068  0.217] sc 1.0 g 0 gr 0.0 np 2 dq 0.1
          42 +31 to_pic ction3 [ 0.109 -0.045  0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          43 +32 to_pic ction3 [ 0.113 -0.044  0.174] sc 1.0 g 0 gr 0.0 np 1 dq 0.16
          44 +33 grasp ction3 [ 0.109 -0.045  0.144] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          45 +34 to_pla ction3 [ 0.109 -0.045  0.144] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          46 +35 to_pla ction3 [ 0.114 -0.044  0.181] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          47 +36 to_pla ction3 [ 0.109 -0.045  0.223] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          48 +37 to_pla ction3 [0.149 0.006 0.224] sc 1.0 g 1 gr 0.0 np 4 dq 0.09
          49 +38 to_pla ction3 [0.162 0.036 0.224] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          50 +39 to_pla ction3 [0.209 0.103 0.224] sc 1.0 g 1 gr 0.0 np 2 dq 0.17
          51 +40 to_pla ction3 [0.214 0.117 0.18 ] sc 1.0 g 1 gr 0.0 np 1 dq 0.17
          52 +41 releas ction3 [0.214 0.117 0.136] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          53 +42 retrea ction3 [0.214 0.117 0.136] sc 1.0 g 0 gr 0.0 np 2 dq 0.12
          54 +43 retrea ction3 [0.214 0.117 0.166] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
          55 +44 to_pic ction2 [0.214 0.117 0.196] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          56 +45 to_pic ction2 [0.213 0.116 0.198] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          57 +46 to_pic ction2 [0.213 0.115 0.202] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          58 +47 to_pic ction2 [0.213 0.115 0.205] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          59 +48 to_pic ction2 [0.213 0.116 0.209] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          60 +49 to_pic ction2 [0.214 0.116 0.213] sc 1.0 g 0 gr 0.0 np 3 dq 0.17
          61 +50 to_pic ction2 [0.181 0.039 0.215] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          62 +51 to_pic ction2 [ 0.164 -0.014  0.216] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          63 +52 to_pic ction2 [ 0.161 -0.024  0.176] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          64 +53 to_pic ction2 [ 0.149 -0.038  0.142] sc 1.0 g 0 gr 0.0 np 1 dq 0.01
          65 +54 grasp ction2 [ 0.148 -0.039  0.14 ] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          66 +55 to_pla ction2 [ 0.148 -0.039  0.14 ] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          67 +56 to_pla ction2 [ 0.153 -0.036  0.173] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          68 +57 to_pla ction2 [ 0.15  -0.038  0.21 ] sc 1.0 g 1 gr 0.0 np 5 dq 0.19
          69 +58 to_pla ction2 [ 0.22  -0.065  0.22 ] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          70 +59 to_pla ction2 [ 0.292 -0.091  0.22 ] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          71 +60 to_pla ction2 [ 0.359 -0.115  0.22 ] sc 1.0 g 1 gr 0.0 np 2 dq 0.13
          72 +61 to_pla ction2 [ 0.364 -0.117  0.176] sc 1.0 g 1 gr 0.0 np 1 dq 0.13
          73 +62 releas ction2 [ 0.364 -0.117  0.132] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          74 +63 retrea ction2 [ 0.364 -0.117  0.132] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          75 +64 retrea ction2 [ 0.364 -0.117  0.162] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          76 +65 to_pic _block [ 0.364 -0.117  0.192] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          77 +66 to_pic _block [ 0.364 -0.053  0.21 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          78 +67 to_pic _block [0.362 0.014 0.213] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          79 +68 to_pic _block [0.361 0.087 0.214] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          80 +69 to_pic _block [0.356 0.119 0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.18
          81 +70 grasp _block [0.356 0.119 0.156] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          82 +71 to_pla _block [0.356 0.119 0.156] sc 1.0 g 1 gr 0.0 np 6 dq 0.14
          83 +72 to_pla _block [0.356 0.119 0.201] sc 1.0 g 1 gr 0.0 np 5 dq 0.14
          84 +73 to_pla _block [0.356 0.119 0.246] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          85 +74 to_pla _block [0.293 0.076 0.246] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          86 +75 to_pla _block [0.226 0.03  0.247] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
          87 +76 to_pla _block [ 0.167 -0.011  0.249] sc 1.0 g 1 gr 0.0 np 1 dq 0.2
          88 +77 to_pla _block [ 0.159 -0.018  0.204] sc 1.0 g 1 gr 0.0 np 1 dq 0.19
          89 +78 releas _block [ 0.145 -0.024  0.168] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          90 +DONE 79
diff --git a/d431.txt b/d431.txt
new file mode 100644
index 0000000..486c0b3
--- /dev/null
+++ b/d431.txt
@@ -0,0 +1,310 @@
           1 +target_block [ 0.269 -0.229  0.1  ] [0.017 0.036 0.025]
           2 +obstruction2 [ 0.301 -0.231  0.095] [0.012 0.015 0.01 ]
           3 +obstruction6 [0.388 0.338 0.091] [0.017 0.014 0.016]
           4 +obstruction7 [ 0.248 -0.055  0.104] [0.016 0.014 0.029]
           5 +obstruction0 [ 0.348 -0.286  0.099] [0.019 0.018 0.014]
           6 +obstruction3 [ 0.333 -0.241  0.111] [0.019 0.016 0.026]
           7 +obstruction4 [ 0.316 -0.274  0.096] [0.012 0.013 0.011]
           8 +obstruction1 [0.442 0.086 0.098] [0.01  0.017 0.023]
           9 +obstruction5 [ 0.302 -0.319  0.11 ] [0.014 0.01  0.025]
          10 +target_region [ 0.322 -0.273  0.08 ] [0.022 0.045 0.005]
          11 +0 to_pic ction3 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 5 dq 0.2
          12 +1 to_pic ction3 [ 0.174 -0.018  0.22 ] sc 1.0 g 0 gr 0.0 np 5 dq 0.2
          13 +2 to_pic ction3 [ 0.191 -0.044  0.219] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          14 +3 to_pic ction3 [ 0.223 -0.081  0.219] sc 1.0 g 0 gr 0.0 np 4 dq 0.16
          15 +4 to_pic ction3 [ 0.243 -0.12   0.217] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          16 +5 to_pic ction3 [ 0.287 -0.178  0.217] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          17 +6 to_pic ction3 [ 0.329 -0.235  0.216] sc 1.0 g 0 gr 0.0 np 1 dq 0.13
          18 +7 grasp ction3 [ 0.333 -0.241  0.167] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          19 +8 to_pla ction3 [ 0.333 -0.241  0.167] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          20 +9 to_pla ction3 [ 0.334 -0.241  0.235] sc 1.0 g 1 gr 0.0 np 4 dq 0.18
          21 +10 to_pla ction3 [ 0.392 -0.194  0.247] sc 1.0 g 1 gr 0.0 np 3 dq 0.14
          22 +11 to_pla ction3 [ 0.45  -0.146  0.247] sc 1.0 g 1 gr 0.0 np 2 dq 0.12
          23 +12 to_pla ction3 [ 0.45  -0.146  0.203] sc 1.0 g 1 gr 0.0 np 1 dq 0.12
          24 +13 releas ction3 [ 0.45  -0.146  0.159] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          25 +14 retrea ction3 [ 0.45  -0.146  0.159] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
          26 +15 retrea ction3 [ 0.45  -0.146  0.189] sc 1.0 g 0 gr 0.0 np 1 dq 0.08
          27 +16 to_pic ction0 [ 0.45  -0.146  0.219] sc 1.0 g 0 gr 0.0 np 3 dq 0.19
          28 +17 to_pic ction0 [ 0.399 -0.216  0.217] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          29 +18 to_pic ction0 [ 0.348 -0.286  0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
          30 +19 grasp ction0 [ 0.348 -0.286  0.143] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          31 +20 to_pla ction0 [ 0.348 -0.286  0.143] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          32 +21 to_pla ction0 [ 0.349 -0.286  0.216] sc 1.0 g 1 gr 0.0 np 5 dq 0.13
          33 +22 to_pla ction0 [ 0.282 -0.308  0.223] sc 1.0 g 1 gr 0.0 np 4 dq 0.16
          34 +23 to_pla ction0 [ 0.216 -0.329  0.223] sc 1.0 g 1 gr 0.0 np 3 dq 0.18
          35 +24 to_pla ction0 [ 0.15  -0.35   0.223] sc 1.0 g 1 gr 0.0 np 2 dq 0.13
          36 +25 to_pla ction0 [ 0.15  -0.35   0.179] sc 1.0 g 1 gr 0.0 np 1 dq 0.13
          37 +26 releas ction0 [ 0.15  -0.35   0.135] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          38 +27 retrea ction0 [ 0.15  -0.35   0.135] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          39 +28 retrea ction0 [ 0.15  -0.35   0.165] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          40 +29 to_pic ction5 [ 0.15  -0.35   0.195] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          41 +30 to_pic ction5 [ 0.223 -0.336  0.214] sc 1.0 g 0 gr 0.0 np 2 dq 0.17
          42 +31 to_pic ction5 [ 0.302 -0.319  0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.13
          43 +32 grasp ction5 [ 0.302 -0.319  0.166] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          44 +33 to_pla ction5 [ 0.302 -0.319  0.166] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          45 +34 to_pla ction5 [ 0.303 -0.319  0.238] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          46 +35 to_pla ction5 [ 0.365 -0.333  0.243] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          47 +36 to_pla ction5 [ 0.418 -0.346  0.245] sc 1.0 g 1 gr 0.0 np 3 dq 0.12
          48 +37 to_pla ction5 [ 0.45  -0.35   0.243] sc 1.0 g 1 gr 0.0 np 2 dq 0.11
          49 +38 to_pla ction5 [ 0.45 -0.35  0.2 ] sc 1.0 g 1 gr 0.0 np 1 dq 0.1
          50 +39 releas ction5 [ 0.45  -0.35   0.157] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          51 +40 retrea ction5 [ 0.45  -0.35   0.157] sc 1.0 g 0 gr 0.0 np 2 dq 0.07
          52 +41 retrea ction5 [ 0.45  -0.35   0.187] sc 1.0 g 0 gr 0.0 np 1 dq 0.07
          53 +42 to_pic ction4 [ 0.45  -0.35   0.217] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          54 +43 to_pic ction4 [ 0.43  -0.339  0.217] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          55 +44 to_pic ction4 [ 0.409 -0.327  0.216] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          56 +45 to_pic ction4 [ 0.388 -0.315  0.215] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          57 +46 to_pic ction4 [ 0.338 -0.288  0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          58 +47 to_pic ction4 [ 0.321 -0.277  0.15 ] sc 1.0 g 0 gr 0.0 np 1 dq 0.04
          59 +48 grasp ction4 [ 0.316 -0.274  0.137] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          60 +49 to_pla ction4 [ 0.316 -0.274  0.137] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          61 +50 to_pla ction4 [ 0.316 -0.274  0.212] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          62 +51 to_pla ction4 [ 0.337 -0.205  0.214] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          63 +52 to_pla ction4 [ 0.357 -0.136  0.214] sc 1.0 g 1 gr 0.0 np 3 dq 0.14
          64 +53 to_pla ction4 [ 0.364 -0.088  0.214] sc 1.0 g 1 gr 0.0 np 2 dq 0.12
          65 +54 to_pla ction4 [ 0.364 -0.087  0.172] sc 1.0 g 1 gr 0.0 np 1 dq 0.12
          66 +55 releas ction4 [ 0.364 -0.088  0.129] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          67 +56 retrea ction4 [ 0.364 -0.088  0.129] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          68 +57 retrea ction4 [ 0.364 -0.087  0.159] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          69 +58 to_pic ction2 [ 0.364 -0.087  0.189] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
          70 +59 to_pic ction2 [ 0.333 -0.159  0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          71 +60 to_pic ction2 [ 0.306 -0.222  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          72 +61 to_pic ction2 [ 0.306 -0.222  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
          73 +62 to_pic ction2 [ 0.305 -0.224  0.193] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
          74 +63 to_pic ction2 [ 0.305 -0.224  0.193] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
          75 +64 to_pic ction2 [ 0.303 -0.227  0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
          76 +65 to_pic ction2 [ 0.303 -0.227  0.173] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
          77 +66 to_pic ction2 [ 0.303 -0.227  0.173] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
          78 +67 to_pic ction2 [ 0.303 -0.228  0.163] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
          79 +68 to_pic ction2 [ 0.303 -0.228  0.163] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
          80 +69 to_pic ction2 [ 0.303 -0.228  0.163] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          81 +70 to_pic ction2 [ 0.302 -0.228  0.158] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
          82 +71 to_pic ction2 [ 0.302 -0.228  0.158] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          83 +72 to_pic ction2 [ 0.302 -0.228  0.158] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
          84 +73 to_pic ction2 [ 0.302 -0.229  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          85 +74 to_pic ction2 [ 0.302 -0.229  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
          86 +75 grasp ction2 [ 0.302 -0.229  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
          87 +76 to_pic ction2 [ 0.302 -0.229  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          88 +77 to_pic ction2 [ 0.304 -0.229  0.191] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
          89 +78 to_pic ction2 [ 0.304 -0.229  0.191] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
          90 +79 to_pic ction2 [ 0.303 -0.23   0.171] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          91 +80 to_pic ction2 [ 0.303 -0.23   0.171] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
          92 +81 to_pic ction2 [ 0.303 -0.23   0.171] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
          93 +82 to_pic ction2 [ 0.302 -0.23   0.161] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
          94 +83 to_pic ction2 [ 0.302 -0.23   0.161] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
          95 +84 to_pic ction2 [ 0.302 -0.23   0.161] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          96 +85 to_pic ction2 [ 0.302 -0.23   0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
          97 +86 to_pic ction2 [ 0.302 -0.23   0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
          98 +87 to_pic ction2 [ 0.302 -0.23   0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
          99 +88 grasp ction2 [ 0.302 -0.23   0.156] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         100 +89 to_pic ction2 [ 0.302 -0.23   0.156] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
         101 +90 to_pic ction2 [ 0.302 -0.23   0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         102 +91 to_pic ction2 [ 0.302 -0.23   0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         103 +92 to_pic ction2 [ 0.302 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
         104 +93 to_pic ction2 [ 0.302 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         105 +94 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
         106 +95 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         107 +96 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         108 +97 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         109 +98 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         110 +99 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         111 +100 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         112 +101 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         113 +102 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         114 +103 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         115 +104 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         116 +105 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         117 +106 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         118 +107 to_pic ction2 [ 0.302 -0.232  0.176] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         119 +108 to_pic ction2 [ 0.302 -0.232  0.197] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
         120 +109 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         121 +110 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         122 +111 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
         123 +112 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         124 +113 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         125 +114 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         126 +115 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         127 +116 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         128 +117 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         129 +118 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         130 +119 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         131 +120 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         132 +121 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         133 +122 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         134 +123 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         135 +124 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         136 +125 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         137 +126 to_pic ction2 [ 0.303 -0.23   0.188] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
         138 +127 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         139 +128 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         140 +129 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
         141 +130 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         142 +131 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
         143 +132 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         144 +133 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         145 +134 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         146 +135 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         147 +136 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         148 +137 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         149 +138 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         150 +139 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         151 +140 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         152 +141 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         153 +142 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         154 +143 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         155 +144 to_pic ction2 [ 0.301 -0.232  0.169] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         156 +145 to_pic ction2 [ 0.301 -0.232  0.184] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         157 +146 to_pic ction2 [ 0.301 -0.232  0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.16
         158 +147 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
         159 +148 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         160 +149 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
         161 +150 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         162 +151 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         163 +152 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         164 +153 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         165 +154 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         166 +155 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         167 +156 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         168 +157 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         169 +158 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         170 +159 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         171 +160 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         172 +161 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         173 +162 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         174 +163 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         175 +164 to_pic ction2 [ 0.302 -0.229  0.174] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         176 +165 to_pic ction2 [ 0.302 -0.229  0.195] sc 1.0 g 0 gr 0.0 np 3 dq 0.15
         177 +166 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         178 +167 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         179 +168 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
         180 +169 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         181 +170 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
         182 +171 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         183 +172 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         184 +173 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         185 +174 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         186 +175 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         187 +176 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         188 +177 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         189 +178 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         190 +179 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         191 +180 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         192 +181 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         193 +182 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         194 +183 to_pic ction2 [ 0.3   -0.232  0.165] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         195 +184 to_pic ction2 [ 0.3   -0.233  0.177] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         196 +185 to_pic ction2 [ 0.3   -0.233  0.189] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         197 +186 to_pic ction2 [ 0.3   -0.232  0.201] sc 1.0 g 0 gr 0.0 np 3 dq 0.17
         198 +187 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
         199 +188 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         200 +189 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
         201 +190 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         202 +191 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         203 +192 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         204 +193 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
         205 +194 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         206 +195 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
         207 +196 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         208 +197 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
         209 +198 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         210 +199 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         211 +200 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         212 +201 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         213 +202 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         214 +203 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         215 +204 to_pic ction2 [ 0.302 -0.229  0.168] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         216 +205 to_pic ction2 [ 0.302 -0.228  0.183] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         217 +206 to_pic ction2 [ 0.302 -0.229  0.198] sc 1.0 g 0 gr 0.0 np 3 dq 0.16
         218 +207 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         219 +208 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         220 +209 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
         221 +210 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         222 +211 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
         223 +212 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         224 +213 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         225 +214 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         226 +215 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         227 +216 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         228 +217 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         229 +218 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         230 +219 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         231 +220 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         232 +221 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         233 +222 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         234 +223 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         235 +224 to_pic ction2 [ 0.3   -0.232  0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         236 +225 to_pic ction2 [ 0.299 -0.233  0.172] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         237 +226 to_pic ction2 [ 0.299 -0.233  0.181] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         238 +227 to_pic ction2 [ 0.299 -0.233  0.191] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         239 +228 to_pic ction2 [ 0.3   -0.232  0.202] sc 1.0 g 0 gr 0.0 np 3 dq 0.17
         240 +229 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.18
         241 +230 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         242 +231 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.13
         243 +232 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         244 +233 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         245 +234 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         246 +235 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
         247 +236 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         248 +237 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
         249 +238 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         250 +239 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
         251 +240 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         252 +241 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         253 +242 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         254 +243 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         255 +244 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         256 +245 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         257 +246 to_pic ction2 [ 0.301 -0.228  0.164] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         258 +247 to_pic ction2 [ 0.301 -0.227  0.175] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         259 +248 to_pic ction2 [ 0.301 -0.227  0.187] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         260 +249 to_pic ction2 [ 0.301 -0.229  0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
         261 +250 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         262 +251 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         263 +252 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
         264 +253 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         265 +254 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
         266 +255 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         267 +256 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         268 +257 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
         269 +258 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         270 +259 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         271 +260 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         272 +261 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         273 +262 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         274 +263 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
         275 +264 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         276 +265 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         277 +266 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         278 +267 to_pic ction2 [ 0.301 -0.229  0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         279 +268 to_pic ction2 [ 0.302 -0.228  0.17 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         280 +269 to_pic ction2 [ 0.302 -0.227  0.178] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         281 +270 to_pic ction2 [ 0.302 -0.228  0.187] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         282 +271 to_pic ction2 [ 0.302 -0.229  0.197] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         283 +272 to_pic ction2 [ 0.301 -0.23   0.208] sc 1.0 g 0 gr 0.0 np 3 dq 0.09
         284 +273 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         285 +274 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         286 +275 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         287 +276 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         288 +277 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         289 +278 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         290 +279 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         291 +280 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         292 +281 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         293 +282 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
         294 +283 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         295 +284 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
         296 +285 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         297 +286 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
         298 +287 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         299 +288 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         300 +289 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         301 +290 to_pic ction2 [ 0.302 -0.23   0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         302 +291 to_pic ction2 [ 0.302 -0.229  0.17 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         303 +292 to_pic ction2 [ 0.303 -0.229  0.178] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         304 +293 to_pic ction2 [ 0.303 -0.229  0.186] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         305 +294 to_pic ction2 [ 0.302 -0.229  0.195] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         306 +295 to_pic ction2 [ 0.302 -0.23   0.204] sc 1.0 g 0 gr 0.0 np 3 dq 0.17
         307 +296 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         308 +297 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         309 +298 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.18
         310 +299 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
diff --git a/sweep1.txt b/sweep1.txt
new file mode 100644
index 0000000..4e5bfb6
--- /dev/null
+++ b/sweep1.txt
@@ -0,0 +1,4 @@
           1 +success 60/60  mean steps(success) 30.7  max compute 0.4s
           2 +success 60/60  mean steps(success) 75.4  max compute 1.0s
           3 +FAIL (431, False, 1000, 7.7, 163, 'to_pick', 'obstruction2', 8)
           4 +success 39/40  mean steps(success) 98.0  max compute 7.7s
```

</details>

<a id="C013"></a>
### C013 · Combine close/open with final motion step; drop retreat phase

Commit `1763b8ac1500ea631780996e7a130a2c92dd24b0`; parents: cd051602be53c6f56708632c9c151d040bccf763. Recorded author date: 2026-09-28T22:25:51+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0955](01_timeline.md#E0955): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_1763b8a_approach.py) · [Exact all-file diff](evidence/diffs/C013_1763b8a.diff)

[Previous saved controller snapshot](evidence/versions/C012_cd05160_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 55290e5..4f7ed33 100644
--- a/approach.py
+++ b/approach.py
@@ -55,6 +55,7 @@ class GeneratedApproach:
   55     55          self.last_cmd = None
   56     56          self.blocked = 0
   57     57          self.scale = 1.0
          58 +        self.last_final = False
   58     59          self.tilt = (0.0, 0.0)
   59     60          self.fail = {}
   60     61          self.t = 0
@@ -309,6 +310,7 @@ class GeneratedApproach:
  309    310  
  310    311      def _track(self):
  311    312          """Return joint delta toward current path, or None when path done."""
         313 +        self.last_final = False
  312    314          while self.path:
  313    315              pos, yaw = self.path[0]
  314    316              M = fk(self.base, self.q)
@@ -327,6 +329,7 @@ class GeneratedApproach:
  327    329              qt, err = self._ik(pos, yaw)
  328    330              dq = qt - self.q
  329    331              m = np.max(np.abs(dq))
         332 +            self.last_final = bool(final and m <= MAX_DQ and err < 1e-3 and self.scale >= 1.0)
  330    333              if m > MAX_DQ:
  331    334                  dq = dq * (MAX_DQ / m)
  332    335              return dq
@@ -384,7 +387,15 @@ class GeneratedApproach:
  384    387              if dq is None:
  385    388                  self.phase = 'grasp'
  386    389                  return None
         390 +            if self.last_final:
         391 +                self.phase = 'grasp_c'
         392 +                self.path = []
         393 +                return self._act(dq, grip=-1.0)
  387    394              return self._act(dq)
         395 +        if ph == 'grasp_c':
         396 +            self.phase = 'grasp'
         397 +            self.wait = 0
         398 +            return None
  388    399          if ph == 'grasp':
  389    400              if self.grasped:
  390    401                  self.phase = 'to_place'
@@ -423,10 +434,18 @@ class GeneratedApproach:
  423    434              if dq is None:
  424    435                  self.phase = 'release'
  425    436                  return None
         437 +            if self.last_final:
         438 +                self.phase = 'release'
         439 +                self.path = []
         440 +                self.wait = 1
         441 +                return self._act(dq, grip=1.0)
  426    442              return self._act(dq)
  427    443          if ph == 'release':
  428    444              if not self.grasped:
  429        -                self.phase = 'retreat'
         445 +                self.phase = 'plan'
         446 +                self.wait = 0
         447 +                return None
         448 +            if False:
  430    449                  tool = fk(self.base, self.q)[:3, 3]
  431    450                  self.path = [(p_, self.task['yaw_place'] if self.task else 0.0)
  432    451                               for p_ in self._line(tool, np.array([tool[0], tool[1], tool[2] + 0.06]), 0.05)]
diff --git a/combo.py b/combo.py
new file mode 100644
index 0000000..f3ddfe8
--- /dev/null
+++ b/combo.py
@@ -0,0 +1,17 @@
           1 +import numpy as np
           2 +from th import H
           3 +from kin import ik, down_R
           4 +h=H(3)
           5 +n='target_block'; p=h.pose(n)[:3]; he=h.he(n); top=p[2]+he[2]
           6 +h.goto((p[0],p[1],top+0.06),0.0)
           7 +# final step: move down to top+0.028 with close in same action
           8 +q=h.q(); qt,e=ik(h.base(),q,np.array([p[0],p[1],top+0.028]),down_R(0.0))
           9 +a=np.zeros(11); a[3:10]=np.clip(qt-q,-.2,.2); a[10]=-1; h.step(a)
          10 +print('tool',h.tool()[:3,3].round(3),'grasped',h.grasped())
          11 +h.grip(-1); print('after extra close', h.grasped())
          12 +# move to release spot then combined open
          13 +tgt=np.array([p[0]+0.1,p[1],top+0.028+0.0015])
          14 +h.goto(tgt+np.array([0,0,0.03]),0.0)
          15 +q=h.q(); qt,e=ik(h.base(),q,tgt,down_R(0.0))
          16 +a=np.zeros(11); a[3:10]=np.clip(qt-q,-.2,.2); a[10]=1; h.step(a)
          17 +print('tool',h.tool()[:3,3].round(3),'grasped after combined open',h.grasped(), h.pose(n)[:3].round(3))
diff --git a/d3.txt b/d3.txt
new file mode 100644
index 0000000..75ddf66
--- /dev/null
+++ b/d3.txt
@@ -0,0 +1,35 @@
           1 +obstruction1 [ 0.32  -0.279  0.114] [0.013 0.01  0.029]
           2 +target_block [ 0.159 -0.082  0.1  ] [0.018 0.022 0.025]
           3 +target_region [ 0.329 -0.303  0.08 ] [0.023 0.027 0.005]
           4 +obstruction0 [0.22  0.114 0.1  ] [0.014 0.016 0.025]
           5 +0 to_pic ction1 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 5 dq 0.2
           6 +1 to_pic ction1 [ 0.185 -0.043  0.221] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
           7 +2 to_pic ction1 [ 0.217 -0.088  0.223] sc 1.0 g 0 gr 0.0 np 4 dq 0.17
           8 +3 to_pic ction1 [ 0.237 -0.139  0.221] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
           9 +4 to_pic ction1 [ 0.274 -0.201  0.223] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          10 +5 to_pic ction1 [ 0.311 -0.261  0.225] sc 1.0 g 0 gr 0.0 np 1 dq 0.12
          11 +6 grasp ction1 [ 0.32  -0.279  0.175] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          12 +7 to_pla ction1 [ 0.32  -0.279  0.175] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          13 +8 to_pla ction1 [ 0.32  -0.28   0.245] sc 1.0 g 1 gr 0.0 np 3 dq 0.13
          14 +9 to_pla ction1 [ 0.256 -0.286  0.245] sc 1.0 g 1 gr 0.0 np 2 dq 0.12
          15 +10 to_pla ction1 [ 0.193 -0.292  0.245] sc 1.0 g 1 gr 0.0 np 1 dq 0.2
          16 +11 to_pla ction1 [ 0.195 -0.292  0.181] sc 1.0 g 1 gr 0.0 np 1 dq 0.05
          17 +12 releas ction1 [ 0.193 -0.292  0.166] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          18 +13 retrea ction1 [ 0.193 -0.292  0.166] sc 1.0 g 0 gr 0.0 np 2 dq 0.1
          19 +14 retrea ction1 [ 0.193 -0.292  0.196] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
          20 +15 to_pic _block [ 0.193 -0.292  0.226] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          21 +16 to_pic _block [ 0.182 -0.224  0.223] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          22 +17 to_pic _block [ 0.176 -0.172  0.221] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          23 +18 to_pic _block [ 0.173 -0.123  0.219] sc 1.0 g 0 gr 0.0 np 2 dq 0.19
          24 +19 to_pic _block [ 0.159 -0.082  0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          25 +20 to_pic _block [ 0.162 -0.082  0.175] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
          26 +21 grasp _block [ 0.159 -0.082  0.156] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          27 +22 to_pla _block [ 0.159 -0.082  0.156] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
          28 +23 to_pla _block [ 0.16  -0.082  0.194] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          29 +24 to_pla _block [ 0.161 -0.082  0.237] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          30 +25 to_pla _block [ 0.204 -0.134  0.245] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          31 +26 to_pla _block [ 0.251 -0.192  0.248] sc 1.0 g 1 gr 0.0 np 3 dq 0.1
          32 +27 to_pla _block [ 0.273 -0.229  0.246] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
          33 +28 to_pla _block [ 0.314 -0.281  0.248] sc 1.0 g 1 gr 0.0 np 1 dq 0.19
          34 +29 releas _block [ 0.329 -0.303  0.168] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          35 +DONE 30
diff --git a/d431.txt b/d431.txt
index 486c0b3..ecc08eb 100644
--- a/d431.txt
+++ b/d431.txt
@@ -1,13 +1,13 @@
    1        -target_block [ 0.269 -0.229  0.1  ] [0.017 0.036 0.025]
    2        -obstruction2 [ 0.301 -0.231  0.095] [0.012 0.015 0.01 ]
    3        -obstruction6 [0.388 0.338 0.091] [0.017 0.014 0.016]
    4        -obstruction7 [ 0.248 -0.055  0.104] [0.016 0.014 0.029]
    5      1  obstruction0 [ 0.348 -0.286  0.099] [0.019 0.018 0.014]
    6        -obstruction3 [ 0.333 -0.241  0.111] [0.019 0.016 0.026]
    7        -obstruction4 [ 0.316 -0.274  0.096] [0.012 0.013 0.011]
    8        -obstruction1 [0.442 0.086 0.098] [0.01  0.017 0.023]
    9      2  obstruction5 [ 0.302 -0.319  0.11 ] [0.014 0.01  0.025]
           3 +target_block [ 0.269 -0.229  0.1  ] [0.017 0.036 0.025]
           4 +obstruction1 [0.442 0.086 0.098] [0.01  0.017 0.023]
           5 +obstruction4 [ 0.316 -0.274  0.096] [0.012 0.013 0.011]
   10      6  target_region [ 0.322 -0.273  0.08 ] [0.022 0.045 0.005]
           7 +obstruction7 [ 0.248 -0.055  0.104] [0.016 0.014 0.029]
           8 +obstruction6 [0.388 0.338 0.091] [0.017 0.014 0.016]
           9 +obstruction2 [ 0.301 -0.231  0.095] [0.012 0.015 0.01 ]
          10 +obstruction3 [ 0.333 -0.241  0.111] [0.019 0.016 0.026]
   11     11  0 to_pic ction3 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 5 dq 0.2
   12     12  1 to_pic ction3 [ 0.174 -0.018  0.22 ] sc 1.0 g 0 gr 0.0 np 5 dq 0.2
   13     13  2 to_pic ction3 [ 0.191 -0.044  0.219] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
@@ -66,245 +66,58 @@ target_region [ 0.322 -0.273  0.08 ] [0.022 0.045 0.005]
   66     66  55 releas ction4 [ 0.364 -0.088  0.129] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
   67     67  56 retrea ction4 [ 0.364 -0.088  0.129] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
   68     68  57 retrea ction4 [ 0.364 -0.087  0.159] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
   69        -58 to_pic ction2 [ 0.364 -0.087  0.189] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
   70        -59 to_pic ction2 [ 0.333 -0.159  0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
   71        -60 to_pic ction2 [ 0.306 -0.222  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
   72        -61 to_pic ction2 [ 0.306 -0.222  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
   73        -62 to_pic ction2 [ 0.305 -0.224  0.193] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
   74        -63 to_pic ction2 [ 0.305 -0.224  0.193] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
   75        -64 to_pic ction2 [ 0.303 -0.227  0.173] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
   76        -65 to_pic ction2 [ 0.303 -0.227  0.173] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
   77        -66 to_pic ction2 [ 0.303 -0.227  0.173] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
   78        -67 to_pic ction2 [ 0.303 -0.228  0.163] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
   79        -68 to_pic ction2 [ 0.303 -0.228  0.163] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
   80        -69 to_pic ction2 [ 0.303 -0.228  0.163] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
   81        -70 to_pic ction2 [ 0.302 -0.228  0.158] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
   82        -71 to_pic ction2 [ 0.302 -0.228  0.158] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
   83        -72 to_pic ction2 [ 0.302 -0.228  0.158] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
   84        -73 to_pic ction2 [ 0.302 -0.229  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
   85        -74 to_pic ction2 [ 0.302 -0.229  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
   86        -75 grasp ction2 [ 0.302 -0.229  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
   87        -76 to_pic ction2 [ 0.302 -0.229  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
   88        -77 to_pic ction2 [ 0.304 -0.229  0.191] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
   89        -78 to_pic ction2 [ 0.304 -0.229  0.191] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
   90        -79 to_pic ction2 [ 0.303 -0.23   0.171] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
   91        -80 to_pic ction2 [ 0.303 -0.23   0.171] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
   92        -81 to_pic ction2 [ 0.303 -0.23   0.171] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
   93        -82 to_pic ction2 [ 0.302 -0.23   0.161] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
   94        -83 to_pic ction2 [ 0.302 -0.23   0.161] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
   95        -84 to_pic ction2 [ 0.302 -0.23   0.161] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
   96        -85 to_pic ction2 [ 0.302 -0.23   0.156] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
   97        -86 to_pic ction2 [ 0.302 -0.23   0.156] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
   98        -87 to_pic ction2 [ 0.302 -0.23   0.156] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
   99        -88 grasp ction2 [ 0.302 -0.23   0.156] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  100        -89 to_pic ction2 [ 0.302 -0.23   0.156] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
  101        -90 to_pic ction2 [ 0.302 -0.23   0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
  102        -91 to_pic ction2 [ 0.302 -0.23   0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  103        -92 to_pic ction2 [ 0.302 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
  104        -93 to_pic ction2 [ 0.302 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  105        -94 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
  106        -95 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  107        -96 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  108        -97 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  109        -98 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  110        -99 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  111        -100 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  112        -101 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  113        -102 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  114        -103 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  115        -104 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  116        -105 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  117        -106 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  118        -107 to_pic ction2 [ 0.302 -0.232  0.176] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  119        -108 to_pic ction2 [ 0.302 -0.232  0.197] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
  120        -109 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
  121        -110 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  122        -111 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
  123        -112 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  124        -113 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
  125        -114 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  126        -115 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  127        -116 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  128        -117 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  129        -118 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  130        -119 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  131        -120 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  132        -121 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  133        -122 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  134        -123 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  135        -124 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  136        -125 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  137        -126 to_pic ction2 [ 0.303 -0.23   0.188] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
  138        -127 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
  139        -128 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  140        -129 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
  141        -130 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  142        -131 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
  143        -132 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  144        -133 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  145        -134 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  146        -135 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  147        -136 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  148        -137 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  149        -138 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  150        -139 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  151        -140 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  152        -141 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  153        -142 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  154        -143 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  155        -144 to_pic ction2 [ 0.301 -0.232  0.169] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  156        -145 to_pic ction2 [ 0.301 -0.232  0.184] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  157        -146 to_pic ction2 [ 0.301 -0.232  0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.16
  158        -147 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
  159        -148 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  160        -149 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
  161        -150 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  162        -151 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
  163        -152 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  164        -153 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  165        -154 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  166        -155 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  167        -156 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  168        -157 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  169        -158 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  170        -159 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  171        -160 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  172        -161 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  173        -162 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  174        -163 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  175        -164 to_pic ction2 [ 0.302 -0.229  0.174] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  176        -165 to_pic ction2 [ 0.302 -0.229  0.195] sc 1.0 g 0 gr 0.0 np 3 dq 0.15
  177        -166 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
  178        -167 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  179        -168 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
  180        -169 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  181        -170 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
  182        -171 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  183        -172 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  184        -173 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  185        -174 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  186        -175 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  187        -176 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  188        -177 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  189        -178 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  190        -179 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  191        -180 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  192        -181 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  193        -182 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  194        -183 to_pic ction2 [ 0.3   -0.232  0.165] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  195        -184 to_pic ction2 [ 0.3   -0.233  0.177] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  196        -185 to_pic ction2 [ 0.3   -0.233  0.189] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  197        -186 to_pic ction2 [ 0.3   -0.232  0.201] sc 1.0 g 0 gr 0.0 np 3 dq 0.17
  198        -187 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
  199        -188 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  200        -189 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
  201        -190 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  202        -191 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
  203        -192 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  204        -193 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
  205        -194 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  206        -195 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
  207        -196 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  208        -197 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
  209        -198 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  210        -199 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  211        -200 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  212        -201 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  213        -202 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  214        -203 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  215        -204 to_pic ction2 [ 0.302 -0.229  0.168] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  216        -205 to_pic ction2 [ 0.302 -0.228  0.183] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  217        -206 to_pic ction2 [ 0.302 -0.229  0.198] sc 1.0 g 0 gr 0.0 np 3 dq 0.16
  218        -207 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
  219        -208 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  220        -209 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
  221        -210 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  222        -211 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
  223        -212 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  224        -213 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  225        -214 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  226        -215 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  227        -216 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  228        -217 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  229        -218 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  230        -219 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  231        -220 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  232        -221 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  233        -222 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  234        -223 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  235        -224 to_pic ction2 [ 0.3   -0.232  0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  236        -225 to_pic ction2 [ 0.299 -0.233  0.172] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  237        -226 to_pic ction2 [ 0.299 -0.233  0.181] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  238        -227 to_pic ction2 [ 0.299 -0.233  0.191] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  239        -228 to_pic ction2 [ 0.3   -0.232  0.202] sc 1.0 g 0 gr 0.0 np 3 dq 0.17
  240        -229 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.18
  241        -230 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  242        -231 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.13
  243        -232 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  244        -233 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
  245        -234 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  246        -235 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
  247        -236 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  248        -237 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
  249        -238 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  250        -239 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.02
  251        -240 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  252        -241 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  253        -242 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  254        -243 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  255        -244 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  256        -245 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  257        -246 to_pic ction2 [ 0.301 -0.228  0.164] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  258        -247 to_pic ction2 [ 0.301 -0.227  0.175] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  259        -248 to_pic ction2 [ 0.301 -0.227  0.187] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  260        -249 to_pic ction2 [ 0.301 -0.229  0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
  261        -250 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
  262        -251 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  263        -252 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
  264        -253 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  265        -254 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
  266        -255 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  267        -256 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  268        -257 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.05
  269        -258 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  270        -259 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  271        -260 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  272        -261 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  273        -262 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  274        -263 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.01
  275        -264 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  276        -265 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  277        -266 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  278        -267 to_pic ction2 [ 0.301 -0.229  0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  279        -268 to_pic ction2 [ 0.302 -0.228  0.17 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  280        -269 to_pic ction2 [ 0.302 -0.227  0.178] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  281        -270 to_pic ction2 [ 0.302 -0.228  0.187] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  282        -271 to_pic ction2 [ 0.302 -0.229  0.197] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  283        -272 to_pic ction2 [ 0.301 -0.23   0.208] sc 1.0 g 0 gr 0.0 np 3 dq 0.09
  284        -273 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
  285        -274 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  286        -275 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
  287        -276 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  288        -277 to_pic ction2 [ 0.301 -0.231  0.172] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
  289        -278 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  290        -279 to_pic ction2 [ 0.301 -0.231  0.172] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  291        -280 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  292        -281 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  293        -282 to_pic ction2 [ 0.301 -0.231  0.162] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
  294        -283 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
  295        -284 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
  296        -285 to_pic ction2 [ 0.301 -0.231  0.157] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  297        -286 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
  298        -287 to_pic ction2 [ 0.301 -0.231  0.155] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
  299        -288 grasp ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
  300        -289 to_pic ction2 [ 0.301 -0.231  0.155] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  301        -290 to_pic ction2 [ 0.302 -0.23   0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  302        -291 to_pic ction2 [ 0.302 -0.229  0.17 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  303        -292 to_pic ction2 [ 0.303 -0.229  0.178] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  304        -293 to_pic ction2 [ 0.303 -0.229  0.186] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  305        -294 to_pic ction2 [ 0.302 -0.229  0.195] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
  306        -295 to_pic ction2 [ 0.302 -0.23   0.204] sc 1.0 g 0 gr 0.0 np 3 dq 0.17
  307        -296 to_pic ction2 [ 0.301 -0.231  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
  308        -297 to_pic ction2 [ 0.301 -0.231  0.212] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
  309        -298 to_pic ction2 [ 0.301 -0.231  0.192] sc 1.0 g 0 gr 0.0 np 1 dq 0.18
  310        -299 to_pic ction2 [ 0.301 -0.231  0.192] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
          69 +58 to_pic _block [ 0.364 -0.087  0.189] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          70 +59 to_pic _block [ 0.364 -0.088  0.198] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          71 +60 to_pic _block [ 0.364 -0.088  0.208] sc 1.0 g 0 gr 0.0 np 3 dq 0.15
          72 +61 to_pic _block [ 0.317 -0.158  0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          73 +62 to_pic _block [ 0.28  -0.215  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.18
          74 +63 grasp _block [ 0.269 -0.229  0.156] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          75 +64 to_pla _block [ 0.269 -0.229  0.156] sc 1.0 g 1 gr 0.0 np 7 dq 0.12
          76 +65 to_pla _block [ 0.269 -0.229  0.2  ] sc 1.0 g 1 gr 0.0 np 6 dq 0.12
          77 +66 to_pla _block [ 0.269 -0.229  0.243] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          78 +67 to_pla _block [ 0.241 -0.187  0.246] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          79 +68 to_pla _block [ 0.223 -0.153  0.246] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          80 +69 to_pla _block [ 0.201 -0.126  0.245] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          81 +70 to_pla _block [ 0.179 -0.086  0.244] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          82 +71 to_pla _block [ 0.151 -0.059  0.243] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
          83 +72 to_pla _block [ 0.15  -0.058  0.202] sc 1.0 g 1 gr 0.0 np 1 dq 0.2
          84 +73 to_pla _block [ 0.151 -0.057  0.167] sc 1.0 g 1 gr 0.0 np 1 dq 0.06
          85 +74 releas _block [ 0.15  -0.058  0.158] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          86 +75 retrea _block [ 0.15  -0.058  0.158] sc 1.0 g 0 gr 0.0 np 2 dq 0.18
          87 +76 retrea _block [ 0.15  -0.058  0.188] sc 1.0 g 0 gr 0.0 np 1 dq 0.16
          88 +77 to_pic ction2 [ 0.15  -0.058  0.218] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
          89 +78 to_pic ction2 [ 0.178 -0.082  0.216] sc 1.0 g 0 gr 0.0 np 4 dq 0.19
          90 +79 to_pic ction2 [ 0.2   -0.116  0.216] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          91 +80 to_pic ction2 [ 0.218 -0.133  0.215] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          92 +81 to_pic ction2 [ 0.241 -0.159  0.215] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          93 +82 to_pic ction2 [ 0.283 -0.208  0.217] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          94 +83 to_pic ction2 [ 0.3   -0.228  0.147] sc 1.0 g 0 gr 0.0 np 1 dq 0.03
          95 +84 grasp ction2 [ 0.301 -0.231  0.137] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          96 +85 to_pla ction2 [ 0.301 -0.231  0.137] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          97 +86 to_pla ction2 [ 0.301 -0.231  0.212] sc 1.0 g 1 gr 0.0 np 4 dq 0.14
          98 +87 to_pla ction2 [ 0.236 -0.232  0.214] sc 1.0 g 1 gr 0.0 np 3 dq 0.13
          99 +88 to_pla ction2 [ 0.171 -0.233  0.214] sc 1.0 g 1 gr 0.0 np 2 dq 0.19
         100 +89 to_pla ction2 [ 0.171 -0.233  0.171] sc 1.0 g 1 gr 0.0 np 1 dq 0.18
         101 +90 releas ction2 [ 0.171 -0.233  0.128] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
         102 +91 retrea ction2 [ 0.171 -0.233  0.128] sc 1.0 g 0 gr 0.0 np 2 dq 0.12
         103 +92 retrea ction2 [ 0.171 -0.233  0.158] sc 1.0 g 0 gr 0.0 np 1 dq 0.12
         104 +93 to_pic _block [ 0.171 -0.233  0.188] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         105 +94 to_pic _block [ 0.173 -0.204  0.197] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         106 +95 to_pic _block [ 0.17  -0.179  0.203] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         107 +96 to_pic _block [ 0.165 -0.159  0.208] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
         108 +97 to_pic _block [ 0.167 -0.121  0.209] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
         109 +98 to_pic _block [ 0.162 -0.088  0.21 ] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
         110 +99 to_pic _block [ 0.152 -0.061  0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         111 +100 to_pic _block [ 0.153 -0.058  0.175] sc 1.0 g 0 gr 0.0 np 1 dq 0.1
         112 +101 grasp _block [ 0.15  -0.058  0.158] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         113 +102 to_pla _block [ 0.15  -0.058  0.158] sc 1.0 g 1 gr 0.0 np 6 dq 0.2
         114 +103 to_pla _block [ 0.151 -0.057  0.192] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         115 +104 to_pla _block [ 0.151 -0.058  0.231] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
         116 +105 to_pla _block [ 0.183 -0.089  0.238] sc 1.0 g 1 gr 0.0 np 4 dq 0.19
         117 +106 to_pla _block [ 0.207 -0.13   0.243] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
         118 +107 to_pla _block [ 0.23  -0.152  0.244] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
         119 +108 to_pla _block [ 0.255 -0.186  0.244] sc 1.0 g 1 gr 0.0 np 2 dq 0.2
         120 +109 to_pla _block [ 0.3   -0.242  0.248] sc 1.0 g 1 gr 0.0 np 2 dq 0.11
         121 +110 to_pla _block [ 0.322 -0.273  0.243] sc 1.0 g 1 gr 0.0 np 1 dq 0.19
         122 +111 releas _block [ 0.322 -0.273  0.168] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
         123 +DONE 112
diff --git a/d478.txt b/d478.txt
new file mode 100644
index 0000000..e7aa86e
--- /dev/null
+++ b/d478.txt
@@ -0,0 +1,310 @@
           1 +target_region [0.207 0.148 0.08 ] [0.033 0.03  0.005]
           2 +obstruction3 [0.39  0.02  0.103] [0.02  0.015 0.028]
           3 +obstruction5 [0.183 0.148 0.104] [0.018 0.013 0.019]
           4 +obstruction6 [ 0.219 -0.068  0.092] [0.02  0.018 0.017]
           5 +target_block [0.368 0.261 0.1  ] [0.027 0.024 0.025]
           6 +obstruction4 [0.242 0.117 0.107] [0.01  0.012 0.022]
           7 +obstruction1 [0.221 0.147 0.108] [0.015 0.013 0.023]
           8 +obstruction7 [0.177 0.182 0.102] [0.016 0.019 0.017]
           9 +obstruction0 [0.192 0.115 0.11 ] [0.012 0.011 0.025]
          10 +obstruction2 [0.217 0.171 0.108] [0.015 0.011 0.023]
          11 +0 to_pic ction0 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          12 +1 to_pic ction0 [0.171 0.048 0.217] sc 1.0 g 0 gr 0.0 np 2 dq 0.19
          13 +2 to_pic ction0 [0.192 0.115 0.215] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          14 +3 to_pic ction0 [0.193 0.115 0.17 ] sc 1.0 g 0 gr 0.0 np 1 dq 0.02
          15 +4 grasp ction0 [0.192 0.115 0.166] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          16 +5 to_pla ction0 [0.192 0.115 0.166] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          17 +6 to_pla ction0 [0.196 0.115 0.211] sc 1.0 g 1 gr 0.0 np 5 dq 0.14
          18 +7 to_pla ction0 [0.192 0.115 0.243] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          19 +8 to_pla ction0 [0.174 0.063 0.243] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
          20 +9 to_pla ction0 [0.157 0.012 0.244] sc 1.0 g 1 gr 0.0 np 2 dq 0.19
          21 +10 to_pla ction0 [0.15 0.   0.2 ] sc 1.0 g 1 gr 0.0 np 1 dq 0.2
          22 +11 to_pla ction0 [0.151 0.    0.164] sc 1.0 g 1 gr 0.0 np 1 dq 0.04
          23 +12 releas ction0 [0.15  0.    0.158] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          24 +13 retrea ction0 [0.15  0.    0.158] sc 1.0 g 0 gr 0.0 np 2 dq 0.17
          25 +14 retrea ction0 [0.15  0.    0.188] sc 1.0 g 0 gr 0.0 np 1 dq 0.15
          26 +15 to_pic ction4 [0.15  0.    0.218] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          27 +16 to_pic ction4 [0.158 0.007 0.218] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          28 +17 to_pic ction4 [0.167 0.015 0.218] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          29 +18 to_pic ction4 [0.174 0.024 0.218] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          30 +19 to_pic ction4 [0.182 0.034 0.217] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          31 +20 to_pic ction4 [0.188 0.044 0.216] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          32 +21 to_pic ction4 [0.194 0.055 0.215] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
          33 +22 to_pic ction4 [0.227 0.092 0.214] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          34 +23 to_pic ction4 [0.242 0.115 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.01
          35 +24 grasp ction4 [0.242 0.117 0.16 ] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          36 +25 to_pla ction4 [0.242 0.117 0.16 ] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
          37 +26 to_pla ction4 [0.245 0.116 0.21 ] sc 1.0 g 1 gr 0.0 np 4 dq 0.19
          38 +27 to_pla ction4 [0.303 0.117 0.237] sc 1.0 g 1 gr 0.0 np 3 dq 0.16
          39 +28 to_pla ction4 [0.364 0.117 0.237] sc 1.0 g 1 gr 0.0 np 2 dq 0.13
          40 +29 to_pla ction4 [0.364 0.117 0.194] sc 1.0 g 1 gr 0.0 np 1 dq 0.13
          41 +30 releas ction4 [0.364 0.117 0.152] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
          42 +31 retrea ction4 [0.364 0.117 0.152] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
          43 +32 retrea ction4 [0.364 0.117 0.182] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
          44 +33 to_pic ction1 [0.364 0.117 0.212] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          45 +34 to_pic ction1 [0.34  0.124 0.212] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          46 +35 to_pic ction1 [0.315 0.129 0.212] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
          47 +36 to_pic ction1 [0.293 0.132 0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.14
          48 +37 to_pic ction1 [0.221 0.147 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          49 +38 to_pic ction1 [0.222 0.147 0.162] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
          50 +39 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          51 +40 to_pic ction2 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          52 +41 to_pic ction2 [0.222 0.147 0.211] sc 1.0 g 0 gr 0.0 np 1 dq 0.18
          53 +42 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          54 +43 to_pic ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.19
          55 +44 to_pic ction2 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
          56 +45 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          57 +46 to_pic ction1 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          58 +47 to_pic ction1 [0.218 0.172 0.193] sc 1.0 g 0 gr 0.0 np 3 dq 0.12
          59 +48 to_pic ction1 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          60 +49 to_pic ction1 [0.222 0.147 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.01
          61 +50 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          62 +51 to_pic ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          63 +52 to_pic ction1 [0.223 0.146 0.184] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          64 +53 to_pic ction1 [0.222 0.146 0.208] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
          65 +54 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          66 +55 to_pic ction2 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          67 +56 to_pic ction2 [0.222 0.147 0.211] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
          68 +57 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          69 +58 to_pic ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          70 +59 to_pic ction2 [0.217 0.172 0.174] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          71 +60 to_pic ction2 [0.218 0.172 0.186] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          72 +61 to_pic ction2 [0.218 0.172 0.198] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          73 +62 to_pic ction2 [0.217 0.172 0.21 ] sc 1.0 g 0 gr 0.0 np 1 dq 0.18
          74 +63 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          75 +64 to_pic ction1 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          76 +65 to_pic ction1 [0.218 0.171 0.177] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          77 +66 to_pic ction1 [0.218 0.171 0.191] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          78 +67 to_pic ction1 [0.217 0.171 0.206] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
          79 +68 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
          80 +69 to_pic ction5 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          81 +70 to_pic ction5 [0.222 0.147 0.211] sc 1.0 g 0 gr 0.0 np 2 dq 0.08
          82 +71 to_pic ction5 [0.183 0.148 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          83 +72 to_pic ction5 [0.185 0.147 0.166] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
          84 +73 to_pic ction5 [0.185 0.147 0.166] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
          85 +74 to_pic ction5 [0.185 0.147 0.166] sc 0.25 g 0 gr 0.0 np 1 dq 0.05
          86 +75 to_pic ction5 [0.185 0.147 0.166] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
          87 +76 to_pic ction5 [0.184 0.147 0.161] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
          88 +77 to_pic ction5 [0.184 0.147 0.161] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
          89 +78 to_pic ction5 [0.184 0.147 0.161] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
          90 +79 grasp ction5 [0.184 0.147 0.161] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
          91 +80 to_pic ction7 [0.184 0.147 0.161] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
          92 +81 to_pic ction7 [0.186 0.147 0.19 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.15
          93 +82 to_pic ction7 [0.184 0.147 0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.16
          94 +83 to_pic ction7 [0.177 0.182 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
          95 +84 to_pic ction7 [0.179 0.182 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
          96 +85 to_pic ction7 [0.179 0.182 0.163] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
          97 +86 to_pic ction7 [0.179 0.182 0.163] sc 0.25 g 0 gr 0.0 np 1 dq 0.04
          98 +87 to_pic ction7 [0.179 0.182 0.163] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
          99 +88 to_pic ction7 [0.179 0.182 0.163] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         100 +89 grasp ction7 [0.179 0.182 0.163] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         101 +90 to_pic ction7 [0.179 0.182 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         102 +91 to_pic ction7 [0.181 0.182 0.189] sc 1.0 g 0 gr 0.0 np 3 dq 0.17
         103 +92 to_pic ction7 [0.179 0.182 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         104 +93 to_pic ction7 [0.18  0.182 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
         105 +94 to_pic ction7 [0.18  0.182 0.163] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         106 +95 to_pic ction7 [0.18  0.182 0.163] sc 0.25 g 0 gr 0.0 np 1 dq 0.04
         107 +96 to_pic ction7 [0.18  0.182 0.163] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
         108 +97 to_pic ction7 [0.18  0.182 0.163] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         109 +98 to_pic ction7 [0.179 0.182 0.16 ] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
         110 +99 to_pic ction7 [0.179 0.182 0.16 ] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         111 +100 grasp ction7 [0.179 0.182 0.16 ] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         112 +101 to_pic ction5 [0.179 0.182 0.16 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         113 +102 to_pic ction5 [0.18  0.181 0.168] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         114 +103 to_pic ction5 [0.181 0.181 0.177] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         115 +104 to_pic ction5 [0.181 0.181 0.185] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         116 +105 to_pic ction5 [0.181 0.181 0.194] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         117 +106 to_pic ction5 [0.18  0.181 0.204] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
         118 +107 to_pic ction5 [0.179 0.182 0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.15
         119 +108 to_pic ction5 [0.183 0.148 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         120 +109 to_pic ction5 [0.185 0.147 0.166] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
         121 +110 grasp ction5 [0.183 0.148 0.153] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         122 +111 to_pic ction5 [0.183 0.148 0.153] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         123 +112 to_pic ction5 [0.185 0.148 0.166] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         124 +113 to_pic ction5 [0.185 0.148 0.179] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         125 +114 to_pic ction5 [0.185 0.148 0.193] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         126 +115 to_pic ction5 [0.184 0.148 0.206] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         127 +116 to_pic ction5 [0.184 0.147 0.161] sc 1.0 g 0 gr 0.0 np 1 dq 0.03
         128 +117 to_pic ction5 [0.184 0.147 0.161] sc 0.5 g 0 gr 0.0 np 1 dq 0.03
         129 +118 to_pic ction5 [0.184 0.147 0.161] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         130 +119 to_pic ction5 [0.184 0.147 0.161] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
         131 +120 to_pic ction5 [0.184 0.147 0.161] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         132 +121 grasp ction5 [0.184 0.147 0.161] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         133 +122 to_pic ction2 [0.184 0.147 0.161] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         134 +123 to_pic ction2 [0.185 0.147 0.169] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         135 +124 to_pic ction2 [0.186 0.147 0.178] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         136 +125 to_pic ction2 [0.186 0.147 0.187] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         137 +126 to_pic ction2 [0.186 0.147 0.196] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         138 +127 to_pic ction2 [0.185 0.147 0.205] sc 1.0 g 0 gr 0.0 np 3 dq 0.15
         139 +128 to_pic ction2 [0.184 0.147 0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.1
         140 +129 to_pic ction2 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
         141 +130 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         142 +131 to_pic ction7 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         143 +132 to_pic ction7 [0.218 0.172 0.192] sc 1.0 g 0 gr 0.0 np 3 dq 0.14
         144 +133 to_pic ction7 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         145 +134 to_pic ction7 [0.177 0.182 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         146 +135 to_pic ction7 [0.179 0.182 0.162] sc 1.0 g 0 gr 0.0 np 1 dq 0.05
         147 +136 grasp ction7 [0.177 0.182 0.15 ] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         148 +137 to_pic ction7 [0.177 0.182 0.15 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         149 +138 to_pic ction7 [0.18  0.181 0.184] sc 1.0 g 0 gr 0.0 np 3 dq 0.15
         150 +139 to_pic ction7 [0.177 0.182 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         151 +140 to_pic ction7 [0.179 0.182 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
         152 +141 grasp ction7 [0.177 0.182 0.15 ] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         153 +142 to_pla ction7 [0.177 0.182 0.15 ] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         154 +143 to_pla ction7 [0.181 0.182 0.198] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
         155 +144 to_pla ction7 [0.175 0.247 0.224] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
         156 +145 to_pla ction7 [0.173 0.313 0.227] sc 1.0 g 1 gr 0.0 np 2 dq 0.13
         157 +146 to_pla ction7 [0.171 0.321 0.184] sc 1.0 g 1 gr 0.0 np 1 dq 0.13
         158 +147 releas ction7 [0.171 0.321 0.141] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
         159 +148 retrea ction7 [0.171 0.321 0.141] sc 1.0 g 0 gr 0.0 np 2 dq 0.09
         160 +149 retrea ction7 [0.171 0.321 0.171] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         161 +150 to_pic ction5 [0.171 0.321 0.201] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         162 +151 to_pic ction5 [0.171 0.32  0.204] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         163 +152 to_pic ction5 [0.172 0.32  0.207] sc 1.0 g 0 gr 0.0 np 4 dq 0.2
         164 +153 to_pic ction5 [0.171 0.321 0.21 ] sc 1.0 g 0 gr 0.0 np 4 dq 0.09
         165 +154 to_pic ction5 [0.171 0.321 0.212] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         166 +155 to_pic ction5 [0.178 0.246 0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
         167 +156 to_pic ction5 [0.186 0.19  0.213] sc 1.0 g 0 gr 0.0 np 2 dq 0.17
         168 +157 to_pic ction5 [0.183 0.148 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         169 +158 to_pic ction5 [0.185 0.147 0.166] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
         170 +159 to_pic ction5 [0.185 0.147 0.166] sc 0.5 g 0 gr 0.0 np 1 dq 0.06
         171 +160 to_pic ction5 [0.185 0.147 0.166] sc 0.25 g 0 gr 0.0 np 1 dq 0.05
         172 +161 to_pic ction5 [0.185 0.147 0.166] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
         173 +162 to_pic ction5 [0.184 0.148 0.161] sc 0.25 g 0 gr 0.0 np 1 dq 0.03
         174 +163 to_pic ction5 [0.184 0.148 0.161] sc 0.125 g 0 gr 0.0 np 1 dq 0.02
         175 +164 to_pic ction5 [0.184 0.148 0.161] sc 0.0625 g 0 gr 0.0 np 1 dq 0.01
         176 +165 grasp ction5 [0.184 0.148 0.161] sc 1.0 g 0 gr -1.0 np 1 dq 0.0
         177 +166 to_pic ction5 [0.184 0.148 0.161] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         178 +167 to_pic ction5 [0.186 0.147 0.183] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         179 +168 to_pic ction5 [0.185 0.147 0.206] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         180 +169 to_pic ction5 [0.184 0.148 0.161] sc 1.0 g 0 gr 0.0 np 1 dq 0.03
         181 +170 grasp ction5 [0.183 0.148 0.153] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         182 +171 to_pic ction1 [0.183 0.148 0.153] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         183 +172 to_pic ction1 [0.185 0.148 0.198] sc 1.0 g 0 gr 0.0 np 2 dq 0.1
         184 +173 to_pic ction1 [0.221 0.147 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         185 +174 to_pic ction1 [0.222 0.147 0.162] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         186 +175 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         187 +176 to_pic ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         188 +177 to_pic ction1 [0.222 0.147 0.211] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         189 +178 grasp ction1 [0.222 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         190 +179 to_pic ction2 [0.222 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         191 +180 to_pic ction2 [0.222 0.147 0.211] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
         192 +181 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         193 +182 to_pic ction5 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         194 +183 to_pic ction5 [0.218 0.171 0.176] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         195 +184 to_pic ction5 [0.218 0.171 0.19 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         196 +185 to_pic ction5 [0.217 0.171 0.204] sc 1.0 g 0 gr 0.0 np 3 dq 0.11
         197 +186 to_pic ction5 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 2 dq 0.1
         198 +187 to_pic ction5 [0.183 0.148 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         199 +188 to_pic ction5 [0.185 0.148 0.166] sc 1.0 g 0 gr 0.0 np 1 dq 0.06
         200 +189 grasp ction5 [0.183 0.148 0.153] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         201 +190 to_pla ction5 [0.183 0.148 0.153] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         202 +191 to_pla ction5 [0.183 0.148 0.153] sc 0.5 g 1 gr 0.0 np 5 dq 0.09
         203 +192 to_pla ction5 [0.183 0.148 0.173] sc 1.0 g 1 gr 0.0 np 5 dq 0.2
         204 +193 to_pla ction5 [0.183 0.148 0.173] sc 0.5 g 1 gr 0.0 np 5 dq 0.09
         205 +194 to_pla ction5 [0.183 0.148 0.193] sc 1.0 g 1 gr 0.0 np 5 dq 0.15
         206 +195 to_pla ction5 [0.183 0.148 0.23 ] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
         207 +196 to_pla ction5 [0.218 0.111 0.23 ] sc 1.0 g 1 gr 0.0 np 4 dq 0.17
         208 +197 to_pla ction5 [0.242 0.074 0.23 ] sc 1.0 g 1 gr 0.0 np 3 dq 0.2
         209 +198 to_pla ction5 [0.28  0.032 0.231] sc 1.0 g 1 gr 0.0 np 3 dq 0.12
         210 +199 to_pla ction5 [ 0.3  -0.    0.23] sc 1.0 g 1 gr 0.0 np 2 dq 0.16
         211 +200 to_pla ction5 [0.3   0.    0.188] sc 1.0 g 1 gr 0.0 np 1 dq 0.16
         212 +201 releas ction5 [ 0.3   -0.     0.145] sc 1.0 g 1 gr 1.0 np 0 dq 0.0
         213 +202 retrea ction5 [ 0.3   -0.     0.145] sc 1.0 g 0 gr 0.0 np 2 dq 0.11
         214 +203 retrea ction5 [0.3   0.    0.175] sc 1.0 g 0 gr 0.0 np 1 dq 0.11
         215 +204 to_pic ction1 [0.3   0.    0.205] sc 1.0 g 0 gr 0.0 np 3 dq 0.16
         216 +205 to_pic ction1 [0.261 0.073 0.208] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
         217 +206 to_pic ction1 [0.239 0.12  0.211] sc 1.0 g 0 gr 0.0 np 2 dq 0.12
         218 +207 to_pic ction1 [0.221 0.147 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         219 +208 to_pic ction1 [0.222 0.147 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.01
         220 +209 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         221 +210 to_pic ction2 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         222 +211 to_pic ction2 [0.222 0.147 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.16
         223 +212 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         224 +213 to_pic ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         225 +214 to_pic ction2 [0.217 0.172 0.198] sc 1.0 g 0 gr 0.0 np 1 dq 0.14
         226 +215 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         227 +216 to_pic ction1 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         228 +217 to_pic ction1 [0.218 0.172 0.182] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         229 +218 to_pic ction1 [0.217 0.172 0.203] sc 1.0 g 0 gr 0.0 np 1 dq 0.17
         230 +219 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         231 +220 to_pic ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         232 +221 to_pic ction1 [0.222 0.147 0.174] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         233 +222 to_pic ction1 [0.222 0.147 0.187] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         234 +223 to_pic ction1 [0.222 0.147 0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.18
         235 +224 to_pic ction1 [0.221 0.147 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         236 +225 to_pic ction1 [0.222 0.147 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.01
         237 +226 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         238 +227 to_pic ction2 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         239 +228 to_pic ction2 [0.223 0.147 0.181] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         240 +229 to_pic ction2 [0.222 0.147 0.202] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         241 +230 to_pic ction2 [0.217 0.171 0.164] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         242 +231 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         243 +232 to_pic ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         244 +233 to_pic ction2 [0.217 0.172 0.175] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         245 +234 to_pic ction2 [0.217 0.172 0.187] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         246 +235 to_pic ction2 [0.217 0.172 0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.19
         247 +236 to_pic ction2 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
         248 +237 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         249 +238 to_pic ction1 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         250 +239 to_pic ction1 [0.218 0.171 0.176] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         251 +240 to_pic ction1 [0.218 0.171 0.189] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         252 +241 to_pic ction1 [0.217 0.171 0.203] sc 1.0 g 0 gr 0.0 np 3 dq 0.13
         253 +242 to_pic ction1 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         254 +243 to_pic ction1 [0.222 0.148 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.01
         255 +244 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         256 +245 to_pic ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         257 +246 to_pic ction1 [0.222 0.147 0.171] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         258 +247 to_pic ction1 [0.222 0.147 0.18 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         259 +248 to_pic ction1 [0.222 0.147 0.19 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         260 +249 to_pic ction1 [0.222 0.147 0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         261 +250 to_pic ction1 [0.222 0.147 0.209] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         262 +251 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         263 +252 to_pic ction2 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         264 +253 to_pic ction2 [0.222 0.146 0.171] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         265 +254 to_pic ction2 [0.223 0.146 0.181] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         266 +255 to_pic ction2 [0.223 0.146 0.191] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         267 +256 to_pic ction2 [0.222 0.147 0.201] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         268 +257 to_pic ction2 [0.221 0.147 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
         269 +258 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         270 +259 to_pic ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         271 +260 to_pic ction2 [0.217 0.172 0.17 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         272 +261 to_pic ction2 [0.217 0.172 0.177] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         273 +262 to_pic ction2 [0.217 0.172 0.185] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         274 +263 to_pic ction2 [0.217 0.172 0.192] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         275 +264 to_pic ction2 [0.217 0.172 0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         276 +265 to_pic ction2 [0.217 0.172 0.208] sc 1.0 g 0 gr 0.0 np 3 dq 0.11
         277 +266 to_pic ction2 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
         278 +267 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         279 +268 to_pic ction1 [0.217 0.171 0.163] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         280 +269 to_pic ction1 [0.217 0.172 0.169] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         281 +270 to_pic ction1 [0.217 0.172 0.175] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         282 +271 to_pic ction1 [0.217 0.172 0.181] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         283 +272 to_pic ction1 [0.217 0.172 0.187] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         284 +273 to_pic ction1 [0.217 0.172 0.194] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         285 +274 to_pic ction1 [0.217 0.172 0.2  ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         286 +275 to_pic ction1 [0.217 0.172 0.206] sc 1.0 g 0 gr 0.0 np 3 dq 0.19
         287 +276 to_pic ction1 [0.217 0.171 0.212] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         288 +277 to_pic ction1 [0.222 0.147 0.163] sc 1.0 g 0 gr 0.0 np 1 dq 0.0
         289 +278 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         290 +279 to_pic ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         291 +280 to_pic ction1 [0.222 0.147 0.168] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         292 +281 to_pic ction1 [0.222 0.147 0.174] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         293 +282 to_pic ction1 [0.223 0.147 0.18 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         294 +283 to_pic ction1 [0.223 0.147 0.186] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         295 +284 to_pic ction1 [0.223 0.147 0.192] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         296 +285 to_pic ction1 [0.223 0.147 0.199] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         297 +286 to_pic ction1 [0.222 0.147 0.205] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         298 +287 to_pic ction1 [0.222 0.147 0.211] sc 1.0 g 0 gr 0.0 np 1 dq 0.19
         299 +288 grasp ction1 [0.221 0.147 0.162] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
         300 +289 to_pic ction2 [0.221 0.147 0.162] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         301 +290 to_pic ction2 [0.222 0.147 0.168] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         302 +291 to_pic ction2 [0.222 0.147 0.174] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         303 +292 to_pic ction2 [0.223 0.147 0.18 ] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         304 +293 to_pic ction2 [0.223 0.147 0.186] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         305 +294 to_pic ction2 [0.223 0.147 0.193] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         306 +295 to_pic ction2 [0.223 0.147 0.199] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         307 +296 to_pic ction2 [0.222 0.147 0.205] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
         308 +297 to_pic ction2 [0.222 0.147 0.211] sc 1.0 g 0 gr 0.0 np 1 dq 0.2
         309 +298 to_pic ction2 [0.221 0.161 0.179] sc 1.0 g 0 gr 0.0 np 1 dq 0.09
         310 +299 grasp ction2 [0.217 0.171 0.163] sc 1.0 g 0 gr -1.0 np 0 dq 0.0
diff --git a/probe478.py b/probe478.py
new file mode 100644
index 0000000..9ad2d62
--- /dev/null
+++ b/probe478.py
@@ -0,0 +1,31 @@
           1 +import numpy as np, copy
           2 +from th import H
           3 +from approach import GeneratedApproach
           4 +from kin import fk, ik, down_R
           5 +h=H(478,oc=8)
           6 +ap=GeneratedApproach(None,None,{}); ap.reset(h.obs,{})
           7 +for t in range(39):
           8 +    a=ap.get_action(h.obs); h.step(a)
           9 +print(ap.phase, ap.task['name'], 'yaw', ap.task['yaw'], 'tool', h.tool()[:3,3].round(3))
          10 +n=ap.task['name']; p=h.pose(n)[:3]; he=h.he(n); top=p[2]+he[2]
          11 +q0=h.q(); y=ap.task['yaw']
          12 +def go(pos,yaw):
          13 +    for k in range(30):
          14 +        q=h.q(); qt,e=ik(h.base(),q,np.asarray(pos,float),down_R(yaw),iters=100)
          15 +        d=qt-q; m=np.abs(d).max()
          16 +        if m<1e-5: return True
          17 +        a=np.zeros(11); a[3:10]=d*min(1,0.2/m); h.step(a)
          18 +        if np.allclose(h.q(),q): return False
          19 +    return False
          20 +for dz in [0.031,0.028,0.025,0.02]:
          21 +    ok=go((p[0],p[1],top+dz),y)
          22 +    h.grip(-1); g=h.grasped()
          23 +    print('dz',dz,'reached',ok,h.tool()[:3,3].round(3),'grasped',g)
          24 +    if g: break
          25 +    h.grip(1)
          26 +for k in range(12):
          27 +    yy=k*np.pi/12
          28 +    go((p[0],p[1],0.2),yy); ok=go((p[0],p[1],top+0.025),yy)
          29 +    h.grip(-1); g=h.grasped(); print('yaw',round(np.degrees(yy)),'reached',ok,'grasped',g)
          30 +    if g: break
          31 +    h.grip(1)
diff --git a/probe478b.py b/probe478b.py
new file mode 100644
index 0000000..2dc564f
--- /dev/null
+++ b/probe478b.py
@@ -0,0 +1,27 @@
           1 +import numpy as np
           2 +from th import H
           3 +from approach import GeneratedApproach
           4 +from kin import fk, ik, down_R
           5 +h=H(478,oc=8)
           6 +ap=GeneratedApproach(None,None,{}); ap.reset(h.obs,{})
           7 +for t in range(39):
           8 +    a=ap.get_action(h.obs); h.step(a)
           9 +def go(pos,yaw):
          10 +    for k in range(30):
          11 +        q=h.q(); qt,e=ik(h.base(),q,np.asarray(pos,float),down_R(yaw),iters=100)
          12 +        d=qt-q; m=np.abs(d).max()
          13 +        if m<1e-5: return True
          14 +        a=np.zeros(11); a[3:10]=d*min(1,0.2/m); h.step(a)
          15 +        if np.allclose(h.q(),q): return False
          16 +    return False
          17 +for n in ['obstruction2','obstruction5','obstruction7']:
          18 +    p=h.pose(n)[:3]; he=h.he(n); top=p[2]+he[2]; res=[]
          19 +    for k in range(0,12,1):
          20 +        yy=k*np.pi/12
          21 +        go((p[0],p[1],0.21),yy); ok=go((p[0],p[1],top+0.025),yy)
          22 +        h.grip(-1); g=h.grasped(); res.append((k*15,int(ok),int(g)))
          23 +        if g:
          24 +            go((p[0],p[1],top+0.03),yy); h.grip(1); 
          25 +        else: h.grip(1)
          26 +        go((p[0],p[1],0.21),yy)
          27 +    print(n,res)
diff --git a/sweep2.txt b/sweep2.txt
new file mode 100644
index 0000000..1ed51cf
--- /dev/null
+++ b/sweep2.txt
@@ -0,0 +1,3 @@
           1 +success 100/100  mean steps(success) 29.4  max compute 0.4s
           2 +FAIL (478, False, 1000, 9.0, 306, 'to_pick', 'obstruction2', 8)
           3 +success 59/60  mean steps(success) 97.8  max compute 9.0s
diff --git a/touch.py b/touch.py
new file mode 100644
index 0000000..560b9ce
--- /dev/null
+++ b/touch.py
@@ -0,0 +1,30 @@
           1 +import numpy as np, sys
           2 +from th import H
           3 +from approach import GeneratedApproach
           4 +from kin import fk, ik, down_R
           5 +gap=float(sys.argv[1])
           6 +h=H(478,oc=8)
           7 +ap=GeneratedApproach(None,None,{}); ap.reset(h.obs,{})
           8 +for t in range(39):
           9 +    a=ap.get_action(h.obs); h.step(a)
          10 +def go(pos,yaw):
          11 +    for k in range(40):
          12 +        q=h.q(); qt,e=ik(h.base(),q,np.asarray(pos,float),down_R(yaw),iters=100)
          13 +        d=qt-q; m=np.abs(d).max()
          14 +        if m<1e-5: return True
          15 +        a=np.zeros(11); a[3:10]=d*min(1,0.2/m); h.step(a)
          16 +        if np.allclose(h.q(),q): return False
          17 +    return False
          18 +n='obstruction7'; p=h.pose(n)[:3]; he=h.he(n); top=p[2]+he[2]; yy=np.pi/6
          19 +go((p[0],p[1],0.21),yy); go((p[0],p[1],top+0.025),yy); h.grip(-1); print('g7',h.grasped())
          20 +off=h.tool()[2,3]-p[2]
          21 +b=h.pose('target_block')[:3]; bhe=h.he('target_block')
          22 +# yaw 30 deg: obj rotates by 0 (held with same yaw at place) -> AABB same
          23 +dest=np.array([b[0]-bhe[0]-he[0]-gap, b[1], 0.075+he[2]+off+0.0015])
          24 +go((p[0],p[1],0.23),yy); go((dest[0],dest[1],0.23),yy); r=go(dest,yy); print('reached',r,h.tool()[:3,3].round(4))
          25 +h.grip(1); h.grip(1); print('released', not h.grasped(), h.pose(n)[:3].round(4), 'gapx', round(b[0]-bhe[0]-(h.pose(n)[0]+he[0]),4))
          26 +go((dest[0],dest[1],0.23),yy)
          27 +for yb in [np.pi/2, 0.0]:
          28 +    go((b[0],b[1],0.23),yb); ok=go((b[0],b[1],b[2]+bhe[2]+0.025),yb); h.grip(-1); print('block yaw',yb,'reached',ok,'grasped',h.grasped())
          29 +    if h.grasped(): break
          30 +    h.grip(1); go((b[0],b[1],0.23),yb)
```

</details>

<a id="C014"></a>
### C014 · Obstacle-aware routing (diagonal when clear, minimal lift height)

Commit `d3ee669b908f83cdff4833477d4353de4990dac7`; parents: 1763b8ac1500ea631780996e7a130a2c92dd24b0. Recorded author date: 2026-09-28T22:36:43+02:00.

File roles (automatic): policy, setup/other.

- [E0993](01_timeline.md#E0993): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_d3ee669_approach.py) · [Exact all-file diff](evidence/diffs/C014_d3ee669.diff)

[Previous saved controller snapshot](evidence/versions/C013_1763b8a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4f7ed33..963c6f0 100644
--- a/approach.py
+++ b/approach.py
@@ -7,6 +7,7 @@ from kin import fk, ik, down_R, jac, rot_err
    7      7  TABLE_Z = 0.075
    8      8  TABLE_X = (0.10, 0.50)
    9      9  TABLE_Y = (-0.40, 0.40)
          10 +ROUTE_MARGIN = 0.02
   10     11  SAFE_MARGIN = 0.03
   11     12  VSTEP = 0.08
   12     13  HSTEP = 0.10
@@ -234,14 +235,8 @@ class GeneratedApproach:
  234    235          self._set_tilt(p[:2], self.task['dest'])
  235    236          self.phase = 'to_pick'
  236    237          tool = fk(self.base, self.q)[:3, 3]
  237        -        sz = self._safe_z(None, 0.05)
  238        -        pick_above = np.array([p[0], p[1], sz])
  239        -        path = []
  240        -        if tool[2] < sz - 0.01:
  241        -            path += self._line(tool, np.array([tool[0], tool[1], sz]), VSTEP)
  242        -            tool = np.array([tool[0], tool[1], sz])
  243        -        path += self._line(tool, pick_above, HSTEP)
  244        -        path += self._line(pick_above, np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ]), VSTEP)
         238 +        pick = np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ])
         239 +        path = self._route(tool, pick, None, 0.036, 0.09)
  245    240          self._set_path(path, self.task['yaw'])
  246    241  
  247    242      def _mount(self):
@@ -282,6 +277,53 @@ class GeneratedApproach:
  282    277          k = np.round((ydes - y0) / np.pi)
  283    278          return y0 + k * np.pi
  284    279  
         280 +    def _need_z(self, xy, held, depth, rad, skip=()):
         281 +        """Min tool z at xy so nothing within rad (xy) is hit."""
         282 +        need = TABLE_Z + depth + 0.01
         283 +        for n, (p, he) in self.objs.items():
         284 +            if n == held or n in skip:
         285 +                continue
         286 +            dx = max(0.0, abs(xy[0] - p[0]) - he[0])
         287 +            dy = max(0.0, abs(xy[1] - p[1]) - he[1])
         288 +            if dx * dx + dy * dy < rad * rad:
         289 +                need = max(need, p[2] + he[2] + depth + ROUTE_MARGIN)
         290 +        return need
         291 +
         292 +    def _route(self, start, goal, held, depth, rad, approach=0.035, skip_start=(), skip_goal=()):
         293 +        """Waypoints from start to goal: vertical exit, diagonal/flat transit, vertical entry."""
         294 +        a = np.array([start[0], start[1], max(start[2], min(start[2] + approach, 0.30))])
         295 +        g = np.array([goal[0], goal[1], goal[2] + approach])
         296 +        # vertical exit only needed if tool low near objects
         297 +        d = np.linalg.norm(g[:2] - a[:2])
         298 +        ns = max(2, int(np.ceil(d / 0.01)))
         299 +        need = []
         300 +        for i in range(ns + 1):
         301 +            f = i / ns
         302 +            xy = a[:2] + (g[:2] - a[:2]) * f
         303 +            sk = set()
         304 +            if f < 0.3:
         305 +                sk |= set(skip_start)
         306 +            if f > 0.7:
         307 +                sk |= set(skip_goal)
         308 +            need.append(self._need_z(xy, held, depth, rad, sk))
         309 +        need = np.array(need)
         310 +        zs = a[2] + (g[2] - a[2]) * np.linspace(0, 1, ns + 1)
         311 +        pts = []
         312 +        if start[2] < a[2] - 1e-4:
         313 +            pts.append(a)
         314 +        if np.all(zs >= need):
         315 +            pts += self._line(a, g, HSTEP)
         316 +        else:
         317 +            h = max(need.max(), a[2], g[2])
         318 +            b = np.array([a[0], a[1], h]); c = np.array([g[0], g[1], h])
         319 +            # try to skip vertical parts by diagonals where clear
         320 +            pts += self._line(a, b, VSTEP) if h > a[2] + 1e-4 else []
         321 +            pts += self._line(b, c, HSTEP)
         322 +            if h > g[2] + 1e-4:
         323 +                pts += self._line(c, g, VSTEP)
         324 +        pts.append(np.asarray(goal, float))
         325 +        return pts
         326 +
  285    327      def _safe_z(self, held, depth):
  286    328          top = TABLE_Z
  287    329          for n, (p, he) in self.objs.items():
@@ -403,18 +445,10 @@ class GeneratedApproach:
  403    445                  tool = fk(self.base, self.q)[:3, 3]
  404    446                  self.grasp_off = tool[2] - p[2]   # tool z above object center
  405    447                  dest = self.task['dest']
  406        -                sz = self._safe_z(n, self.grasp_off + he[2])
  407        -                up = np.array([tool[0], tool[1], sz])
  408        -                above = np.array([dest[0], dest[1], sz])
  409    448                  place = np.array([dest[0], dest[1], self.task['surf'] + he[2] + self.grasp_off + PLACE_EPS])
  410        -                pts = self._line(tool, up, VSTEP)
  411        -                pts2 = self._line(up, above, HSTEP)
  412        -                pts3 = self._line(above, place, VSTEP)
  413        -                y0, y1 = self.task['yaw'], self.task['yaw_place']
  414        -                self.path = [(p_, y0) for p_ in pts]
  415        -                k = len(pts2)
  416        -                self.path += [(p_, y0 + (y1 - y0) * (i + 1) / k) for i, p_ in enumerate(pts2)]
  417        -                self.path += [(p_, y1) for p_ in pts3]
         449 +                rad = max(0.09, np.hypot(he[0], he[1]) + 0.015)
         450 +                pts = self._route(tool, place, n, max(self.grasp_off + he[2], 0.036), rad)
         451 +                self.path = [(p_, self.task['yaw_place']) for p_ in pts]
  418    452                  return None
  419    453              self.wait += 1
  420    454              if self.wait == 1:
diff --git a/sweep3.txt b/sweep3.txt
new file mode 100644
index 0000000..a09d07f
--- /dev/null
+++ b/sweep3.txt
@@ -0,0 +1 @@
           1 +success 100/100  mean steps(success) 26.1  max compute 0.3s
```

</details>

<a id="C015"></a>
### C015 · Tighter intermediate waypoint tolerance to avoid corner cutting

Commit `f985a915314208ef3d58842379ee53a520913481`; parents: d3ee669b908f83cdff4833477d4353de4990dac7. Recorded author date: 2026-09-28T22:57:46+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E1068](01_timeline.md#E1068): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_f985a91_approach.py) · [Exact all-file diff](evidence/diffs/C015_f985a91.diff)

[Previous saved controller snapshot](evidence/versions/C014_d3ee669_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 963c6f0..a0b054d 100644
--- a/approach.py
+++ b/approach.py
@@ -357,7 +357,7 @@ class GeneratedApproach:
  357    357              pos, yaw = self.path[0]
  358    358              M = fk(self.base, self.q)
  359    359              final = len(self.path) == 1
  360        -            tol = 5e-4 if final else 0.03
         360 +            tol = 5e-4 if final else 0.01
  361    361              e = np.linalg.norm(M[:3, 3] - pos)
  362    362              eo = np.linalg.norm(rot_err(M[:3, :3], self._Rot(yaw)))
  363    363              if e < tol and (eo < (0.01 if final else 0.1)):
diff --git a/d55.txt b/d55.txt
new file mode 100644
index 0000000..5239ee2
--- /dev/null
+++ b/d55.txt
@@ -0,0 +1,64 @@
           1 +target_block [0.367 0.325 0.1  ] [0.036 0.037 0.025]
           2 +obstruction1 [ 0.21  -0.003  0.115] [0.016 0.015 0.03 ]
           3 +target_region [ 0.216 -0.005  0.08 ] [0.045 0.046 0.005]
           4 +obstruction0 [ 0.201 -0.047  0.107] [0.015 0.013 0.022]
           5 +0 to_pic ction1 [0.154 0.001 0.217] sc 1.0 g 0 gr 0.0 np 3 dq 0.2
           6 +1 to_pic ction1 [0.154 0.001 0.247] sc 1.0 g 0 gr 0.0 np 2 dq 0.2
           7 +2 grasp_ ction1 [ 0.201 -0.002  0.217] sc 1.0 g 0 gr -1.0 np 0 dq 0.19
           8 +3 to_pla ction1 [ 0.21  -0.003  0.175] sc 1.0 g 1 gr 0.0 np 6 dq 0.16
           9 +4 to_pla ction1 [ 0.21  -0.003  0.21 ] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          10 +5 to_pla ction1 [ 0.21  -0.003  0.21 ] sc 0.5 g 1 gr 0.0 np 4 dq 0.08
          11 +6 to_pla ction1 [ 0.21  -0.003  0.21 ] sc 0.25 g 1 gr 0.0 np 4 dq 0.04
          12 +7 to_pla ction1 [ 0.21  -0.012  0.213] sc 0.5 g 1 gr 0.0 np 4 dq 0.08
          13 +8 to_pla ction1 [ 0.21  -0.012  0.213] sc 0.25 g 1 gr 0.0 np 4 dq 0.04
          14 +9 to_pla ction1 [ 0.21  -0.012  0.213] sc 0.125 g 1 gr 0.0 np 4 dq 0.02
          15 +10 to_pla ction1 [ 0.21  -0.017  0.215] sc 0.25 g 1 gr 0.0 np 4 dq 0.04
          16 +11 to_pla ction1 [ 0.21  -0.017  0.215] sc 0.125 g 1 gr 0.0 np 4 dq 0.02
          17 +12 to_pla ction1 [ 0.21  -0.017  0.215] sc 0.0625 g 1 gr 0.0 np 4 dq 0.01
          18 +13 releas ction1 [ 0.21  -0.017  0.215] sc 1.0 g 1 gr 1.0 np 4 dq 0.0
          19 +14 releas ction1 [ 0.21  -0.017  0.215] sc 1.0 g 1 gr 1.0 np 4 dq 0.0
          20 +15 releas ction1 [ 0.21  -0.017  0.215] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          21 +16 releas ction1 [ 0.21  -0.017  0.212] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          22 +17 releas ction1 [ 0.21  -0.017  0.212] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          23 +18 releas ction1 [ 0.21  -0.017  0.212] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          24 +19 releas ction1 [ 0.21  -0.017  0.209] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          25 +20 releas ction1 [ 0.21  -0.017  0.209] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          26 +21 releas ction1 [ 0.21  -0.017  0.209] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          27 +22 releas ction1 [ 0.21  -0.017  0.206] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          28 +23 releas ction1 [ 0.21  -0.017  0.206] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          29 +24 releas ction1 [ 0.21  -0.017  0.206] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          30 +25 releas ction1 [ 0.21  -0.017  0.203] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          31 +26 releas ction1 [ 0.21  -0.017  0.203] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          32 +27 releas ction1 [ 0.21  -0.017  0.203] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          33 +28 releas ction1 [ 0.21  -0.017  0.2  ] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          34 +29 releas ction1 [ 0.21  -0.017  0.2  ] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          35 +30 releas ction1 [ 0.21  -0.017  0.2  ] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          36 +31 releas ction1 [ 0.21  -0.017  0.197] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          37 +32 releas ction1 [ 0.21  -0.017  0.197] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          38 +33 releas ction1 [ 0.21  -0.017  0.197] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          39 +34 releas ction1 [ 0.21  -0.017  0.194] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          40 +35 releas ction1 [ 0.21  -0.017  0.194] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          41 +36 releas ction1 [ 0.21  -0.017  0.194] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          42 +37 releas ction1 [ 0.21  -0.017  0.191] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          43 +38 releas ction1 [ 0.21  -0.017  0.191] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          44 +39 releas ction1 [ 0.21  -0.017  0.191] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          45 +40 releas ction1 [ 0.21  -0.017  0.188] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          46 +41 releas ction1 [ 0.21  -0.017  0.188] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          47 +42 releas ction1 [ 0.21  -0.017  0.188] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          48 +43 releas ction1 [ 0.21  -0.017  0.185] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          49 +44 releas ction1 [ 0.21  -0.017  0.185] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          50 +45 releas ction1 [ 0.21  -0.017  0.185] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          51 +46 releas ction1 [ 0.21  -0.017  0.182] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          52 +47 releas ction1 [ 0.21  -0.017  0.182] sc 1.0 g 1 gr 1.0 np 1 dq 0.0
          53 +48 releas ction1 [ 0.21  -0.017  0.182] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
          54 +49 to_pic ction1 [ 0.21  -0.017  0.179] sc 1.0 g 0 gr 0.0 np 3 dq 0.16
          55 +50 grasp_ ction1 [ 0.21  -0.017  0.214] sc 1.0 g 0 gr -1.0 np 0 dq 0.16
          56 +51 to_pla ction1 [ 0.21  -0.017  0.179] sc 1.0 g 1 gr 0.0 np 6 dq 0.16
          57 +52 to_pla ction1 [ 0.21  -0.017  0.214] sc 1.0 g 1 gr 0.0 np 4 dq 0.2
          58 +53 to_pla ction1 [ 0.21  -0.017  0.214] sc 0.5 g 1 gr 0.0 np 4 dq 0.08
          59 +54 to_pla ction1 [ 0.21  -0.017  0.214] sc 0.25 g 1 gr 0.0 np 4 dq 0.04
          60 +55 to_pla ction1 [ 0.21  -0.017  0.214] sc 0.125 g 1 gr 0.0 np 4 dq 0.02
          61 +56 to_pla ction1 [ 0.21  -0.017  0.214] sc 0.0625 g 1 gr 0.0 np 4 dq 0.01
          62 +57 releas ction1 [ 0.21  -0.017  0.214] sc 1.0 g 1 gr 1.0 np 4 dq 0.0
          63 +58 releas ction1 [ 0.21  -0.017  0.214] sc 1.0 g 1 gr 1.0 np 4 dq 0.0
          64 +59 releas ction1 [ 0.21  -0.017  0.214] sc 1.0 g 1 gr 1.0 np 1 dq 0.01
diff --git a/p55.py b/p55.py
new file mode 100644
index 0000000..ed227e6
--- /dev/null
+++ b/p55.py
@@ -0,0 +1,18 @@
           1 +import numpy as np
           2 +from th import H
           3 +from approach import GeneratedApproach
           4 +h=H(55)
           5 +ap=GeneratedApproach(None,None,{}); ap.reset(h.obs,{})
           6 +for t in range(4):
           7 +    a=ap.get_action(h.obs); h.step(a)
           8 +    print(t, ap.phase, h.tool()[:3,3].round(3), [ (np.round(w[0],3)) for w in ap.path])
           9 +print(ap.task, ap.grasp_off)
          10 +from kin import ik, fk
          11 +q=h.q(); print('q',q.round(2))
          12 +for z in [0.215,0.225,0.239]:
          13 +    qt,e=ap._ik(np.array([0.21,-0.003,z]),ap.task['yaw']); print(z,'err',e, 'qt',qt.round(2), 'fk',fk(ap.base,qt)[:3,3].round(3))
          14 +print('obj', h.pose('obstruction1')[:3].round(3), 'grasped', h.grasped())
          15 +for z in [0.239,0.225,0.215]:
          16 +    q=h.q(); qt,e=ap._ik(np.array([0.21,-0.003,z]),ap.task['yaw'])
          17 +    a=np.zeros(11); a[3:10]=qt-q; h.step(a); print(z,'moved', not np.allclose(h.q(),q), h.tool()[:3,3].round(3))
          18 +a=np.zeros(11); a[10]=1; h.step(a); print('open ->grasped', h.grasped(), h.pose('obstruction1')[:3].round(3))
diff --git a/sweep3.txt b/sweep3.txt
index a09d07f..cd03d2c 100644
--- a/sweep3.txt
+++ b/sweep3.txt
@@ -1 +1,5 @@
    1      1  success 100/100  mean steps(success) 26.1  max compute 0.3s
           2 +success 40/40  mean steps(success) 63.2  max compute 1.1s
           3 +FAIL (434, False, 1000, 1.7, 143, 'release', 'obstruction0', 8)
           4 +FAIL (417, False, 1000, 3.9, 344, 'to_place', 'obstruction6', 8)
           5 +success 38/40  mean steps(success) 78.3  max compute 3.9s
```

</details>

<a id="C016"></a>
### C016 · Tight tolerance only at route corners

Commit `1a3898c0e33f3411ffe46a78adcb07f56745d9e0`; parents: f985a915314208ef3d58842379ee53a520913481. Recorded author date: 2026-09-28T23:08:22+02:00.

File roles (automatic): policy, setup/other.

- [E1105](01_timeline.md#E1105): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_1a3898c_approach.py) · [Exact all-file diff](evidence/diffs/C016_1a3898c.diff)

[Previous saved controller snapshot](evidence/versions/C015_f985a91_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a0b054d..9298468 100644
--- a/approach.py
+++ b/approach.py
@@ -237,6 +237,8 @@ class GeneratedApproach:
  237    237          tool = fk(self.base, self.q)[:3, 3]
  238    238          pick = np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ])
  239    239          path = self._route(tool, pick, None, 0.036, 0.09)
         240 +        self.path = self._mk(path, self.task['yaw'])
         241 +        return
  240    242          self._set_path(path, self.task['yaw'])
  241    243  
  242    244      def _mount(self):
@@ -289,6 +291,9 @@ class GeneratedApproach:
  289    291                  need = max(need, p[2] + he[2] + depth + ROUTE_MARGIN)
  290    292          return need
  291    293  
         294 +    def _mk(self, pts, yaw):
         295 +        return [(p, yaw, 0.006 if any(np.linalg.norm(p - t) < 1e-6 for t in self.tight) else 0.03) for p in pts]
         296 +
  292    297      def _route(self, start, goal, held, depth, rad, approach=0.035, skip_start=(), skip_goal=()):
  293    298          """Waypoints from start to goal: vertical exit, diagonal/flat transit, vertical entry."""
  294    299          a = np.array([start[0], start[1], max(start[2], min(start[2] + approach, 0.30))])
@@ -309,8 +314,10 @@ class GeneratedApproach:
  309    314          need = np.array(need)
  310    315          zs = a[2] + (g[2] - a[2]) * np.linspace(0, 1, ns + 1)
  311    316          pts = []
         317 +        self.tight = []
  312    318          if start[2] < a[2] - 1e-4:
  313    319              pts.append(a)
         320 +            self.tight.append(a)
  314    321          if np.all(zs >= need):
  315    322              pts += self._line(a, g, HSTEP)
  316    323          else:
@@ -318,7 +325,9 @@ class GeneratedApproach:
  318    325              b = np.array([a[0], a[1], h]); c = np.array([g[0], g[1], h])
  319    326              # try to skip vertical parts by diagonals where clear
  320    327              pts += self._line(a, b, VSTEP) if h > a[2] + 1e-4 else []
         328 +            self.tight.append(b)
  321    329              pts += self._line(b, c, HSTEP)
         330 +            self.tight.append(c)
  322    331              if h > g[2] + 1e-4:
  323    332                  pts += self._line(c, g, VSTEP)
  324    333          pts.append(np.asarray(goal, float))
@@ -354,10 +363,12 @@ class GeneratedApproach:
  354    363          """Return joint delta toward current path, or None when path done."""
  355    364          self.last_final = False
  356    365          while self.path:
  357        -            pos, yaw = self.path[0]
         366 +            pos, yaw = self.path[0][:2]
  358    367              M = fk(self.base, self.q)
  359    368              final = len(self.path) == 1
  360        -            tol = 5e-4 if final else 0.01
         369 +            tol = 5e-4 if final else 0.03
         370 +            if len(self.path[0]) > 2 and not final:
         371 +                tol = self.path[0][2]
  361    372              e = np.linalg.norm(M[:3, 3] - pos)
  362    373              eo = np.linalg.norm(rot_err(M[:3, :3], self._Rot(yaw)))
  363    374              if e < tol and (eo < (0.01 if final else 0.1)):
@@ -448,7 +459,7 @@ class GeneratedApproach:
  448    459                  place = np.array([dest[0], dest[1], self.task['surf'] + he[2] + self.grasp_off + PLACE_EPS])
  449    460                  rad = max(0.09, np.hypot(he[0], he[1]) + 0.015)
  450    461                  pts = self._route(tool, place, n, max(self.grasp_off + he[2], 0.036), rad)
  451        -                self.path = [(p_, self.task['yaw_place']) for p_ in pts]
         462 +                self.path = self._mk(pts, self.task['yaw_place'])
  452    463                  return None
  453    464              self.wait += 1
  454    465              if self.wait == 1:
diff --git a/sweep4.txt b/sweep4.txt
new file mode 100644
index 0000000..c2206f8
--- /dev/null
+++ b/sweep4.txt
@@ -0,0 +1,101 @@
           1 +ok   (11, True, 12, 0.1, 37, 'release', 'target_block', 0)
           2 +ok   (9, True, 25, 0.1, 48, 'release', 'target_block', 1)
           3 +ok   (3, True, 30, 0.1, 52, 'release', 'target_block', 2)
           4 +ok   (10, True, 20, 0.1, 59, 'release', 'target_block', 2)
           5 +ok   (1, True, 32, 0.2, 63, 'release', 'target_block', 1)
           6 +ok   (7, True, 33, 0.2, 64, 'release', 'target_block', 2)
           7 +ok   (14, True, 11, 0.1, 20, 'release', 'target_block', 0)
           8 +ok   (6, True, 39, 0.2, 76, 'release', 'target_block', 1)
           9 +ok   (12, True, 23, 0.1, 38, 'release', 'target_block', 1)
          10 +ok   (8, True, 47, 0.3, 85, 'release', 'target_block', 2)
          11 +ok   (0, True, 41, 0.3, 85, 'release', 'target_block', 2)
          12 +ok   (15, True, 24, 0.1, 38, 'release', 'target_block', 2)
          13 +ok   (5, True, 51, 0.2, 97, 'release', 'target_block', 2)
          14 +ok   (2, True, 51, 0.3, 103, 'release', 'target_block', 2)
          15 +ok   (4, True, 51, 0.3, 104, 'release', 'target_block', 2)
          16 +ok   (16, True, 23, 0.1, 51, 'release', 'target_block', 1)
          17 +ok   (13, True, 37, 0.2, 74, 'release', 'target_block', 2)
          18 +ok   (19, True, 26, 0.1, 53, 'release', 'target_block', 1)
          19 +ok   (21, True, 21, 0.1, 44, 'release', 'target_block', 0)
          20 +ok   (24, True, 20, 0.1, 40, 'release', 'target_block', 1)
          21 +ok   (23, True, 18, 0.1, 43, 'release', 'target_block', 0)
          22 +ok   (18, True, 34, 0.2, 71, 'release', 'target_block', 2)
          23 +ok   (22, True, 26, 0.1, 61, 'release', 'target_block', 2)
          24 +ok   (17, True, 45, 0.3, 88, 'release', 'target_block', 2)
          25 +ok   (29, True, 11, 0.0, 28, 'release', 'target_block', 2)
          26 +ok   (27, True, 25, 0.1, 43, 'release', 'target_block', 0)
          27 +ok   (26, True, 32, 0.2, 62, 'release', 'target_block', 2)
          28 +ok   (30, True, 22, 0.1, 43, 'release', 'target_block', 0)
          29 +ok   (25, True, 38, 0.2, 72, 'release', 'target_block', 1)
          30 +ok   (34, True, 16, 0.1, 30, 'release', 'target_block', 0)
          31 +ok   (20, True, 43, 0.3, 108, 'release', 'target_block', 2)
          32 +ok   (37, True, 17, 0.1, 34, 'release', 'target_block', 0)
          33 +ok   (35, True, 23, 0.1, 43, 'release', 'target_block', 0)
          34 +ok   (38, True, 15, 0.1, 29, 'release', 'target_block', 0)
          35 +ok   (36, True, 20, 0.1, 44, 'release', 'target_block', 1)
          36 +ok   (31, True, 34, 0.2, 74, 'release', 'target_block', 1)
          37 +ok   (42, True, 18, 0.1, 30, 'release', 'target_block', 0)
          38 +ok   (32, True, 35, 0.2, 78, 'release', 'target_block', 2)
          39 +ok   (33, True, 36, 0.2, 79, 'release', 'target_block', 2)
          40 +ok   (28, True, 45, 0.2, 101, 'release', 'target_block', 1)
          41 +ok   (41, True, 27, 0.1, 56, 'release', 'target_block', 1)
          42 +ok   (40, True, 27, 0.1, 60, 'release', 'target_block', 1)
          43 +ok   (48, True, 10, 0.0, 22, 'release', 'target_block', 0)
          44 +ok   (47, True, 12, 0.0, 25, 'release', 'target_block', 0)
          45 +ok   (46, True, 23, 0.1, 47, 'release', 'target_block', 1)
          46 +ok   (49, True, 17, 0.1, 29, 'release', 'target_block', 0)
          47 +ok   (43, True, 26, 0.1, 56, 'release', 'target_block', 1)
          48 +ok   (39, True, 37, 0.3, 88, 'release', 'target_block', 2)
          49 +ok   (44, True, 29, 0.1, 65, 'release', 'target_block', 2)
          50 +ok   (54, True, 13, 0.1, 35, 'release', 'target_block', 0)
          51 +ok   (57, True, 14, 0.1, 32, 'release', 'target_block', 0)
          52 +ok   (51, True, 23, 0.1, 59, 'release', 'target_block', 1)
          53 +ok   (45, True, 41, 0.2, 94, 'release', 'target_block', 2)
          54 +ok   (60, True, 16, 0.1, 36, 'release', 'target_block', 0)
          55 +ok   (56, True, 21, 0.1, 50, 'release', 'target_block', 1)
          56 +ok   (58, True, 23, 0.1, 56, 'release', 'target_block', 1)
          57 +ok   (50, True, 40, 0.2, 83, 'release', 'target_block', 2)
          58 +ok   (61, True, 26, 0.1, 49, 'release', 'target_block', 1)
          59 +ok   (62, True, 25, 0.1, 47, 'release', 'target_block', 1)
          60 +ok   (63, True, 28, 0.2, 47, 'release', 'target_block', 1)
          61 +ok   (55, True, 45, 0.3, 92, 'release', 'target_block', 2)
          62 +ok   (53, True, 48, 0.2, 97, 'release', 'target_block', 2)
          63 +ok   (68, True, 14, 0.1, 27, 'release', 'target_block', 1)
          64 +ok   (52, True, 47, 0.3, 101, 'release', 'target_block', 2)
          65 +ok   (64, True, 29, 0.2, 55, 'release', 'target_block', 1)
          66 +ok   (65, True, 25, 0.1, 57, 'release', 'target_block', 0)
          67 +ok   (69, True, 12, 0.1, 36, 'release', 'target_block', 0)
          68 +ok   (74, True, 13, 0.1, 31, 'release', 'target_block', 0)
          69 +ok   (66, True, 37, 0.2, 74, 'release', 'target_block', 2)
          70 +ok   (67, True, 32, 0.3, 70, 'release', 'target_block', 2)
          71 +ok   (59, True, 65, 0.4, 120, 'release', 'target_block', 2)
          72 +ok   (77, True, 16, 0.1, 27, 'release', 'target_block', 0)
          73 +ok   (79, True, 14, 0.1, 21, 'release', 'target_block', 0)
          74 +ok   (75, True, 27, 0.1, 52, 'release', 'target_block', 1)
          75 +ok   (73, True, 33, 0.2, 62, 'release', 'target_block', 2)
          76 +ok   (78, True, 24, 0.2, 42, 'release', 'target_block', 2)
          77 +ok   (81, True, 17, 0.1, 30, 'release', 'target_block', 0)
          78 +ok   (70, True, 38, 0.2, 79, 'release', 'target_block', 1)
          79 +ok   (76, True, 42, 0.2, 69, 'release', 'target_block', 1)
          80 +ok   (84, True, 20, 0.1, 37, 'release', 'target_block', 1)
          81 +ok   (71, True, 52, 0.3, 94, 'release', 'target_block', 2)
          82 +ok   (72, True, 49, 0.3, 100, 'release', 'target_block', 2)
          83 +ok   (83, True, 24, 0.1, 51, 'release', 'target_block', 2)
          84 +ok   (80, True, 34, 0.2, 66, 'release', 'target_block', 2)
          85 +ok   (82, True, 37, 0.2, 65, 'release', 'target_block', 2)
          86 +ok   (85, True, 41, 0.2, 67, 'release', 'target_block', 2)
          87 +ok   (90, True, 20, 0.1, 38, 'release', 'target_block', 1)
          88 +ok   (86, True, 37, 0.2, 59, 'release', 'target_block', 2)
          89 +ok   (87, True, 32, 0.1, 57, 'release', 'target_block', 1)
          90 +ok   (88, True, 30, 0.2, 51, 'release', 'target_block', 1)
          91 +ok   (94, True, 21, 0.1, 33, 'release', 'target_block', 0)
          92 +ok   (92, True, 28, 0.1, 43, 'release', 'target_block', 1)
          93 +ok   (89, True, 39, 0.2, 64, 'release', 'target_block', 2)
          94 +ok   (91, True, 34, 0.2, 48, 'release', 'target_block', 2)
          95 +ok   (95, True, 26, 0.1, 33, 'release', 'target_block', 1)
          96 +ok   (93, True, 35, 0.2, 43, 'release', 'target_block', 2)
          97 +ok   (97, True, 17, 0.1, 20, 'release', 'target_block', 0)
          98 +ok   (96, True, 41, 0.2, 30, 'release', 'target_block', 2)
          99 +ok   (98, True, 31, 0.2, 23, 'release', 'target_block', 1)
         100 +ok   (99, True, 44, 0.3, 23, 'release', 'target_block', 2)
         101 +success 100/100  mean steps(success) 29.2  max compute 0.4s
```

</details>

<a id="C017"></a>
### C017 · Pursuit tracking: farthest reachable point along path per step; skip needless vertical exit

Commit `b4a45de2f45545fc322b2ce53fa58438cbc87979`; parents: 1a3898c0e33f3411ffe46a78adcb07f56745d9e0. Recorded author date: 2026-09-28T23:19:02+02:00.

File roles (automatic): policy, setup/other.

- [E1142](01_timeline.md#E1142): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_b4a45de_approach.py) · [Exact all-file diff](evidence/diffs/C017_b4a45de.diff)

[Previous saved controller snapshot](evidence/versions/C016_1a3898c_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9298468..576849c 100644
--- a/approach.py
+++ b/approach.py
@@ -315,6 +315,8 @@ class GeneratedApproach:
  315    315          zs = a[2] + (g[2] - a[2]) * np.linspace(0, 1, ns + 1)
  316    316          pts = []
  317    317          self.tight = []
         318 +        if start[2] > self._need_z(start[:2], held, depth, rad) + 0.005:
         319 +            a = np.asarray(start, float).copy()
  318    320          if start[2] < a[2] - 1e-4:
  319    321              pts.append(a)
  320    322              self.tight.append(a)
@@ -362,31 +364,75 @@ class GeneratedApproach:
  362    364      def _track(self):
  363    365          """Return joint delta toward current path, or None when path done."""
  364    366          self.last_final = False
         367 +        M = fk(self.base, self.q)
         368 +        cur = M[:3, 3]
  365    369          while self.path:
  366    370              pos, yaw = self.path[0][:2]
  367        -            M = fk(self.base, self.q)
  368    371              final = len(self.path) == 1
  369    372              tol = 5e-4 if final else 0.03
  370    373              if len(self.path[0]) > 2 and not final:
  371    374                  tol = self.path[0][2]
  372        -            e = np.linalg.norm(M[:3, 3] - pos)
         375 +            e = np.linalg.norm(cur - pos)
  373    376              eo = np.linalg.norm(rot_err(M[:3, :3], self._Rot(yaw)))
  374    377              if e < tol and (eo < (0.01 if final else 0.1)):
  375    378                  self.path.pop(0)
  376    379                  continue
  377        -            if self.scale < 1.0:
  378        -                # blocked recently: move along straight cartesian line, small step
  379        -                cs = 0.04 * self.scale
  380        -                if e > cs:
  381        -                    pos = M[:3, 3] + (pos - M[:3, 3]) * (cs / e)
  382        -            qt, err = self._ik(pos, yaw)
  383        -            dq = qt - self.q
  384        -            m = np.max(np.abs(dq))
  385        -            self.last_final = bool(final and m <= MAX_DQ and err < 1e-3 and self.scale >= 1.0)
  386        -            if m > MAX_DQ:
  387        -                dq = dq * (MAX_DQ / m)
  388        -            return dq
  389        -        return None
         380 +            break
         381 +        if not self.path:
         382 +            return None
         383 +        # polyline up to first tight corner / final waypoint
         384 +        pts = [cur]
         385 +        k = 0
         386 +        for i, w in enumerate(self.path):
         387 +            pts.append(np.asarray(w[0], float))
         388 +            k = i
         389 +            if (len(w) > 2 and w[2] < 0.01) or i == len(self.path) - 1:
         390 +                break
         391 +        stop_final = (k == len(self.path) - 1)
         392 +        yaw = self.path[k][1]
         393 +        segs = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(pts) - 1)]
         394 +        cum = np.concatenate([[0.0], np.cumsum(segs)])
         395 +        L = cum[-1]
         396 +
         397 +        def at(sv):
         398 +            j = int(np.searchsorted(cum, sv, side='right') - 1)
         399 +            j = min(max(j, 0), len(segs) - 1)
         400 +            f = 0.0 if segs[j] < 1e-9 else (sv - cum[j]) / segs[j]
         401 +            return pts[j] + (pts[j + 1] - pts[j]) * min(max(f, 0.0), 1.0)
         402 +
         403 +        s_max = L
         404 +        if self.scale < 1.0:
         405 +            s_max = min(L, 0.04 * self.scale)
         406 +        qt, err = self._ik(at(s_max), yaw)
         407 +        m = np.max(np.abs(qt - self.q))
         408 +        s_sel = s_max
         409 +        if m > MAX_DQ and s_max > 0.005:
         410 +            lo, hi = 0.0, s_max
         411 +            best = None
         412 +            for _ in range(6):
         413 +                mid = 0.5 * (lo + hi)
         414 +                q2, e2 = self._ik(at(mid), yaw)
         415 +                if np.max(np.abs(q2 - self.q)) <= MAX_DQ:
         416 +                    lo, best = mid, (q2, e2)
         417 +                else:
         418 +                    hi = mid
         419 +            if best is not None:
         420 +                qt, err = best
         421 +                s_sel = lo
         422 +        dq = qt - self.q
         423 +        m = np.max(np.abs(dq))
         424 +        self.last_final = bool(stop_final and s_sel >= L - 1e-9 and m <= MAX_DQ
         425 +                               and err < 1e-3 and self.scale >= 1.0)
         426 +        if m > MAX_DQ:
         427 +            dq = dq * (MAX_DQ / m)
         428 +        # drop intermediate waypoints we pass this step
         429 +        npop = 0
         430 +        for i in range(1, len(cum) - 1):
         431 +            if cum[i] <= s_sel - 1e-9:
         432 +                npop += 1
         433 +        if npop and not (m > MAX_DQ):
         434 +            del self.path[:npop]
         435 +        return dq
  390    436  
  391    437      def _act(self, dq=None, grip=0.0):
  392    438          a = np.zeros(11, dtype=np.float32)
diff --git a/sweep5.txt b/sweep5.txt
new file mode 100644
index 0000000..02c62c0
--- /dev/null
+++ b/sweep5.txt
@@ -0,0 +1,101 @@
           1 +ok   (11, True, 12, 0.0, 37, 'release', 'target_block', 0)
           2 +ok   (10, True, 19, 0.1, 47, 'release', 'target_block', 2)
           3 +ok   (1, True, 30, 0.1, 50, 'release', 'target_block', 1)
           4 +ok   (9, True, 24, 0.1, 52, 'release', 'target_block', 1)
           5 +ok   (3, True, 26, 0.1, 56, 'release', 'target_block', 2)
           6 +ok   (6, True, 33, 0.1, 62, 'release', 'target_block', 1)
           7 +ok   (7, True, 31, 0.2, 67, 'release', 'target_block', 2)
           8 +ok   (14, True, 9, 0.0, 19, 'release', 'target_block', 0)
           9 +ok   (12, True, 21, 0.1, 34, 'release', 'target_block', 1)
          10 +ok   (8, True, 41, 0.2, 79, 'release', 'target_block', 2)
          11 +ok   (0, True, 41, 0.2, 84, 'release', 'target_block', 2)
          12 +ok   (16, True, 19, 0.1, 33, 'release', 'target_block', 1)
          13 +ok   (2, True, 47, 0.3, 93, 'release', 'target_block', 2)
          14 +ok   (4, True, 47, 0.3, 100, 'release', 'target_block', 2)
          15 +ok   (15, True, 20, 0.1, 48, 'release', 'target_block', 2)
          16 +ok   (5, True, 46, 0.2, 100, 'release', 'target_block', 2)
          17 +ok   (13, True, 36, 0.2, 70, 'release', 'target_block', 2)
          18 +ok   (21, True, 17, 0.1, 41, 'release', 'target_block', 0)
          19 +ok   (23, True, 17, 0.1, 36, 'release', 'target_block', 0)
          20 +ok   (19, True, 22, 0.1, 58, 'release', 'target_block', 1)
          21 +ok   (24, True, 17, 0.1, 34, 'release', 'target_block', 1)
          22 +ok   (18, True, 29, 0.1, 69, 'release', 'target_block', 2)
          23 +ok   (22, True, 23, 0.1, 55, 'release', 'target_block', 2)
          24 +ok   (29, True, 10, 0.0, 24, 'release', 'target_block', 2)
          25 +ok   (17, True, 42, 0.3, 88, 'release', 'target_block', 2)
          26 +ok   (27, True, 22, 0.1, 52, 'release', 'target_block', 0)
          27 +ok   (26, True, 27, 0.1, 60, 'release', 'target_block', 2)
          28 +ok   (20, True, 39, 0.3, 95, 'release', 'target_block', 2)
          29 +ok   (25, True, 34, 0.1, 69, 'release', 'target_block', 1)
          30 +ok   (34, True, 14, 0.1, 30, 'release', 'target_block', 0)
          31 +ok   (30, True, 19, 0.1, 52, 'release', 'target_block', 0)
          32 +ok   (37, True, 14, 0.1, 33, 'release', 'target_block', 0)
          33 +ok   (38, True, 12, 0.1, 28, 'release', 'target_block', 0)
          34 +ok   (35, True, 19, 0.1, 45, 'release', 'target_block', 0)
          35 +ok   (36, True, 17, 0.1, 41, 'release', 'target_block', 1)
          36 +ok   (32, True, 32, 0.2, 73, 'release', 'target_block', 2)
          37 +ok   (31, True, 31, 0.1, 76, 'release', 'target_block', 1)
          38 +ok   (42, True, 15, 0.1, 29, 'release', 'target_block', 0)
          39 +ok   (33, True, 32, 0.2, 73, 'release', 'target_block', 2)
          40 +ok   (28, True, 40, 0.2, 94, 'release', 'target_block', 1)
          41 +ok   (41, True, 22, 0.1, 53, 'release', 'target_block', 1)
          42 +ok   (48, True, 8, 0.0, 24, 'release', 'target_block', 0)
          43 +ok   (47, True, 11, 0.0, 27, 'release', 'target_block', 0)
          44 +ok   (40, True, 26, 0.1, 61, 'release', 'target_block', 1)
          45 +ok   (49, True, 15, 0.1, 33, 'release', 'target_block', 0)
          46 +ok   (46, True, 22, 0.1, 48, 'release', 'target_block', 1)
          47 +ok   (43, True, 22, 0.1, 61, 'release', 'target_block', 1)
          48 +ok   (39, True, 36, 0.2, 88, 'release', 'target_block', 2)
          49 +ok   (44, True, 25, 0.1, 70, 'release', 'target_block', 2)
          50 +ok   (54, True, 12, 0.1, 35, 'release', 'target_block', 0)
          51 +ok   (51, True, 20, 0.1, 58, 'release', 'target_block', 1)
          52 +ok   (45, True, 37, 0.2, 85, 'release', 'target_block', 2)
          53 +ok   (57, True, 12, 0.1, 37, 'release', 'target_block', 0)
          54 +ok   (56, True, 18, 0.1, 47, 'release', 'target_block', 1)
          55 +ok   (60, True, 15, 0.1, 34, 'release', 'target_block', 0)
          56 +ok   (50, True, 36, 0.2, 86, 'release', 'target_block', 2)
          57 +ok   (58, True, 22, 0.1, 54, 'release', 'target_block', 1)
          58 +ok   (61, True, 24, 0.2, 47, 'release', 'target_block', 1)
          59 +ok   (53, True, 42, 0.3, 86, 'release', 'target_block', 2)
          60 +ok   (62, True, 24, 0.1, 51, 'release', 'target_block', 1)
          61 +ok   (68, True, 12, 0.1, 23, 'release', 'target_block', 1)
          62 +ok   (63, True, 24, 0.1, 49, 'release', 'target_block', 1)
          63 +ok   (52, True, 45, 0.3, 103, 'release', 'target_block', 2)
          64 +ok   (55, True, 40, 0.3, 98, 'release', 'target_block', 2)
          65 +ok   (65, True, 23, 0.1, 41, 'release', 'target_block', 0)
          66 +ok   (64, True, 24, 0.2, 52, 'release', 'target_block', 1)
          67 +ok   (69, True, 11, 0.1, 40, 'release', 'target_block', 0)
          68 +ok   (74, True, 13, 0.1, 33, 'release', 'target_block', 0)
          69 +ok   (77, True, 14, 0.1, 34, 'release', 'target_block', 0)
          70 +ok   (67, True, 29, 0.2, 72, 'release', 'target_block', 2)
          71 +ok   (66, True, 33, 0.2, 77, 'release', 'target_block', 2)
          72 +ok   (59, True, 56, 0.4, 126, 'release', 'target_block', 2)
          73 +ok   (75, True, 23, 0.1, 52, 'release', 'target_block', 1)
          74 +ok   (79, True, 11, 0.0, 28, 'release', 'target_block', 0)
          75 +ok   (70, True, 32, 0.2, 76, 'release', 'target_block', 1)
          76 +ok   (78, True, 22, 0.1, 42, 'release', 'target_block', 2)
          77 +ok   (73, True, 30, 0.2, 71, 'release', 'target_block', 2)
          78 +ok   (81, True, 14, 0.0, 35, 'release', 'target_block', 0)
          79 +ok   (76, True, 37, 0.2, 80, 'release', 'target_block', 1)
          80 +ok   (84, True, 19, 0.1, 37, 'release', 'target_block', 1)
          81 +ok   (83, True, 21, 0.1, 40, 'release', 'target_block', 2)
          82 +ok   (72, True, 45, 0.3, 96, 'release', 'target_block', 2)
          83 +ok   (71, True, 47, 0.3, 103, 'release', 'target_block', 2)
          84 +ok   (80, True, 32, 0.2, 65, 'release', 'target_block', 2)
          85 +ok   (82, True, 33, 0.2, 64, 'release', 'target_block', 2)
          86 +ok   (90, True, 19, 0.1, 36, 'release', 'target_block', 1)
          87 +ok   (87, True, 29, 0.1, 53, 'release', 'target_block', 1)
          88 +ok   (88, True, 27, 0.2, 54, 'release', 'target_block', 1)
          89 +ok   (86, True, 35, 0.2, 69, 'release', 'target_block', 2)
          90 +ok   (85, True, 36, 0.2, 72, 'release', 'target_block', 2)
          91 +ok   (94, True, 17, 0.1, 44, 'release', 'target_block', 0)
          92 +ok   (89, True, 36, 0.2, 64, 'release', 'target_block', 2)
          93 +ok   (92, True, 29, 0.2, 48, 'release', 'target_block', 1)
          94 +ok   (91, True, 28, 0.2, 54, 'release', 'target_block', 2)
          95 +ok   (97, True, 16, 0.1, 25, 'release', 'target_block', 0)
          96 +ok   (93, True, 32, 0.2, 52, 'release', 'target_block', 2)
          97 +ok   (95, True, 24, 0.1, 44, 'release', 'target_block', 1)
          98 +ok   (98, True, 29, 0.2, 29, 'release', 'target_block', 1)
          99 +ok   (96, True, 36, 0.2, 41, 'release', 'target_block', 2)
         100 +ok   (99, True, 40, 0.3, 25, 'release', 'target_block', 2)
         101 +success 100/100  mean steps(success) 26.2  max compute 0.4s
```

</details>

<a id="C018"></a>
### C018 · Free spot: penalize travel incl. to target block

Commit `4e8d1b7ffac83488a944beb9778eb9ac1ddabb9f`; parents: b4a45de2f45545fc322b2ce53fa58438cbc87979. Recorded author date: 2026-09-28T23:36:16+02:00.

File roles (automatic): policy, setup/other.

- [E1187](01_timeline.md#E1187): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_4e8d1b7_approach.py) · [Exact all-file diff](evidence/diffs/C018_4e8d1b7.diff)

[Previous saved controller snapshot](evidence/versions/C017_b4a45de_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 576849c..1660a1c 100644
--- a/approach.py
+++ b/approach.py
@@ -8,6 +8,7 @@ TABLE_Z = 0.075
    8      8  TABLE_X = (0.10, 0.50)
    9      9  TABLE_Y = (-0.40, 0.40)
   10     10  ROUTE_MARGIN = 0.02
          11 +W_TRAVEL = 0.15
   11     12  SAFE_MARGIN = 0.03
   12     13  VSTEP = 0.08
   13     14  HSTEP = 0.10
@@ -171,7 +172,7 @@ class GeneratedApproach:
  171    172                  bad = any(np.hypot(x - b[0], y - b[1]) < 0.04 for b in self.fail.get(name, []))
  172    173                  if bad:
  173    174                      continue
  174        -                v = min(clear, 0.05) + min(kb, 0.10) - 0.08 * np.hypot(x - p0[0], y - p0[1]) - 0.2 * self._tilt_needed(np.hypot(*(xy - self._mount())))
         175 +                v = min(clear, 0.03) + min(kb, 0.06) - W_TRAVEL * (np.hypot(x - p0[0], y - p0[1]) + np.hypot(x - bp[0], y - bp[1])) - 0.2 * self._tilt_needed(np.hypot(*(xy - self._mount())))
  175    176                  if v > bestv:
  176    177                      bestv, best = v, xy
  177    178          if best is None:
diff --git a/sweep6.txt b/sweep6.txt
new file mode 100644
index 0000000..67e7bd1
--- /dev/null
+++ b/sweep6.txt
@@ -0,0 +1,2 @@
           1 +success 100/100  mean steps(success) 23.6  max compute 1.0s
           2 +success 40/40  mean steps(success) 61.4  max compute 1.7s
```

</details>

<a id="C019"></a>
### C019 · Revert free-spot travel weighting (worse mean steps)

Commit `e4e82e8a091569d83dd5de6002cd8c1121667866`; parents: 4e8d1b7ffac83488a944beb9778eb9ac1ddabb9f. Recorded author date: 2026-09-28T23:46:19+02:00.

File roles (automatic): policy, setup/other.

- [E1194](01_timeline.md#E1194): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_e4e82e8_approach.py) · [Exact all-file diff](evidence/diffs/C019_e4e82e8.diff)

[Previous saved controller snapshot](evidence/versions/C018_4e8d1b7_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C017](#C017). Other files may differ.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1660a1c..576849c 100644
--- a/approach.py
+++ b/approach.py
@@ -8,7 +8,6 @@ TABLE_Z = 0.075
    8      8  TABLE_X = (0.10, 0.50)
    9      9  TABLE_Y = (-0.40, 0.40)
   10     10  ROUTE_MARGIN = 0.02
   11        -W_TRAVEL = 0.15
   12     11  SAFE_MARGIN = 0.03
   13     12  VSTEP = 0.08
   14     13  HSTEP = 0.10
@@ -172,7 +171,7 @@ class GeneratedApproach:
  172    171                  bad = any(np.hypot(x - b[0], y - b[1]) < 0.04 for b in self.fail.get(name, []))
  173    172                  if bad:
  174    173                      continue
  175        -                v = min(clear, 0.03) + min(kb, 0.06) - W_TRAVEL * (np.hypot(x - p0[0], y - p0[1]) + np.hypot(x - bp[0], y - bp[1])) - 0.2 * self._tilt_needed(np.hypot(*(xy - self._mount())))
         174 +                v = min(clear, 0.05) + min(kb, 0.10) - 0.08 * np.hypot(x - p0[0], y - p0[1]) - 0.2 * self._tilt_needed(np.hypot(*(xy - self._mount())))
  176    175                  if v > bestv:
  177    176                      bestv, best = v, xy
  178    177          if best is None:
diff --git a/sweep7.txt b/sweep7.txt
new file mode 100644
index 0000000..69625a2
--- /dev/null
+++ b/sweep7.txt
@@ -0,0 +1 @@
           1 +success 100/100  mean steps(success) 24.4  max compute 0.9s
```

</details>

<a id="C020"></a>
### C020 · Add sweep results (default 1000-1100: 100/100, 23.2 steps; OC=8: 40/40)

Commit `e54126cb892ff019b7f4421273cfa17c63579d26`; parents: e4e82e8a091569d83dd5de6002cd8c1121667866. Recorded author date: 2026-09-29T00:05:32+02:00.

File roles (automatic): setup/other.

- [E1247](01_timeline.md#E1247): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C020_e54126c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/sweep8.txt b/sweep8.txt
new file mode 100644
index 0000000..c42518f
--- /dev/null
+++ b/sweep8.txt
@@ -0,0 +1,2 @@
           1 +success 100/100  mean steps(success) 23.2  max compute 0.9s
           2 +success 40/40  mean steps(success) 79.2  max compute 3.3s
```

</details>

