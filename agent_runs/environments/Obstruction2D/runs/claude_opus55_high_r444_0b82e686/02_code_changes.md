# Obstruction2D · claude-opus-5-5 · replicate 444: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `b1acbfd` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `8329727` | Initial state-machine approach: clear obstructions, place block | approach.py, explore.py, probe.py, probe2.py, probe3.py, test_approach.py | [E0054](01_timeline.md#E0054) |
| [C003](#C003) · `ca413ab` | Clamp grasp x to reachable range | approach.py | [E0071](01_timeline.md#E0071) |
| [C004](#C004) · `e4c016a` | Rewrite: clearance-profile motion, placement planning, reachable grasp offsets | approach.py, dbg.py | [E0094](01_timeline.md#E0094) |
| [C005](#C005) · `9bb174d` | Clearance planner approach: 100/100, 35.9 steps | dbg.py | [E0108](01_timeline.md#E0108) |
| [C006](#C006) · `6715e91` | Feasibility-aware target ordering, drop-spot fallbacks | approach.py, dbg.py, test_approach.py | [E0155](01_timeline.md#E0155) |
| [C007](#C007) · `eefe6f4` | Drop spots must not block remaining grasps | approach.py, test_approach.py | [E0234](01_timeline.md#E0234) |
| [C008](#C008) · `13cd388` | Grasp on landing step, release on final carry step; 100/100 at 33.5 steps | approach.py | [E0339](01_timeline.md#E0339) |
| [C009](#C009) · `2b642b7` | Cost-model drop spots incl. elevated drops | approach.py | [E0356](01_timeline.md#E0356) |
| [C010](#C010) · `0b90e15` | Always include block carry cost in drop choice | approach.py | [E0367](01_timeline.md#E0367) |
| [C011](#C011) · `93444da` | Plan search over removal orders and block staging with cost model | approach.py | [E0396](01_timeline.md#E0396) |
| [C012](#C012) · `576514b` | Keep pick target as obstacle with tiny margin (fix diagonal collisions) | approach.py | [E0453](01_timeline.md#E0453) |
| [C013](#C013) · `f86a47c` | Tilted-arm grasps for objects beyond vertical reach near walls | approach.py | [E0501](01_timeline.md#E0501) |
| [C014](#C014) · `4f4bd2e` | Add debug/probe scripts; tilt support verified on regression sets | counts.py, dbg2.py, dbg3.py, dbg4.py, lb.py, ping.py, probe4.py, probe5.py, timing.py | [E0553](01_timeline.md#E0553) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `b1acbfddd4add04850dd25a3bdfb161ced3a04b6`; parents: none (initial snapshot). Recorded author date: 2026-09-30T11:38:46+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_b1acbfd.diff)

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
index 0000000..9711696
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "9b95b5080a46ab86e259065adc10b91f", "observation_space": {"type": "ObjectCentric", "types": [{"name": "crv_robot", "parent": null, "features": ["x", "y", "theta", "base_radius", "arm_joint", "arm_length", "vacuum", "gripper_height", "gripper_width"]}, {"name": "kinematic2d", "parent": null, "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order"]}, {"name": "circle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "radius"]}, {"name": "double_rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height", "x1", "y1", "theta1", "width1", "height1", "z_order1", "color_r1", "color_g1", "color_b1"]}, {"name": "lobject", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "length_side1", "length_side2"]}, {"name": "rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_block", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_surface", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}]}, "action_space": {"type": "Box", "shape": [5], "low": [-0.05000000074505806, -0.05000000074505806, -0.19634954631328583, -0.10000000149011612, 0.0], "high": [0.05000000074505806, 0.05000000074505806, 0.19634954631328583, 0.10000000149011612, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Initial state-machine approach: clear obstructions, place block

Commit `832972742c7dcd83e426eaaf8620ff260cb911ab`; parents: b1acbfddd4add04850dd25a3bdfb161ced3a04b6. Recorded author date: 2026-09-30T11:41:08+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0054](01_timeline.md#E0054): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_8329727_approach.py) · [Exact all-file diff](evidence/diffs/C002_8329727.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..738ce82
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,183 @@
           1 +import numpy as np
           2 +
           3 +W, H = 1.618, 1.0
           4 +FLOOR = 0.1
           5 +DOWN = -np.pi / 2
           6 +
           7 +
           8 +class GeneratedApproach:
           9 +    def __init__(self, action_space, observation_space, primitives):
          10 +        self.low = np.asarray(action_space.low, dtype=np.float64)
          11 +        self.high = np.asarray(action_space.high, dtype=np.float64)
          12 +        self.reset(None, None)
          13 +
          14 +    def reset(self, state, info):
          15 +        self.phase = "lift"
          16 +        self.obj_name = None
          17 +        self.drop_x = None
          18 +        self.last_robot = None
          19 +        self.stuck = 0
          20 +
          21 +    # ---------------- helpers ----------------
          22 +    def _rect(self, s, o):
          23 +        g = lambda f: float(s.get(o, f))
          24 +        return dict(name=o.name, x=g("x"), y=g("y"), w=g("width"), h=g("height"))
          25 +
          26 +    def _parse(self, s):
          27 +        r = s.get_objects(self._rtype(s))[0]
          28 +        g = lambda f: float(s.get(r, f))
          29 +        robot = dict(x=g("x"), y=g("y"), th=g("theta"), arm=g("arm_joint"),
          30 +                     vac=g("vacuum"), gw=g("gripper_width"), gh=g("gripper_height"),
          31 +                     rad=g("base_radius"), maxarm=g("arm_length"))
          32 +        objs = {}
          33 +        surf = block = None
          34 +        for n in s.get_object_names():
          35 +            o = n if not isinstance(n, str) else s.get_object_from_name(n)
          36 +            tn = o.type.name if hasattr(o.type, "name") else str(o.type)
          37 +            if tn == "crv_robot":
          38 +                continue
          39 +            rr = self._rect(s, o)
          40 +            rr["type"] = tn
          41 +            if tn == "target_surface":
          42 +                surf = rr
          43 +            else:
          44 +                objs[rr["name"]] = rr
          45 +                if tn == "target_block":
          46 +                    block = rr
          47 +        return robot, objs, surf, block
          48 +
          49 +    def _rtype(self, s):
          50 +        for n in s.get_object_names():
          51 +            o = n if not isinstance(n, str) else s.get_object_from_name(n)
          52 +            tn = o.type.name if hasattr(o.type, "name") else str(o.type)
          53 +            if tn == "crv_robot":
          54 +                return o.type
          55 +        raise RuntimeError
          56 +
          57 +    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0, vac=0.0):
          58 +        a = np.array([dx, dy, dth, darm, vac], dtype=np.float64)
          59 +        a = np.clip(a, self.low, self.high)
          60 +        return a.astype(np.float32)
          61 +
          62 +    def _choose_next(self, objs, surf, robot):
          63 +        # obstructions that conflict with placing the block on the surface
          64 +        sx0, sx1 = surf["x"], surf["x"] + surf["w"]
          65 +        cands = []
          66 +        for o in objs.values():
          67 +            if o["type"] == "target_block":
          68 +                continue
          69 +            if o["x"] < sx1 + 0.005 and o["x"] + o["w"] > sx0 - 0.005 and o["y"] < FLOOR + 0.3:
          70 +                cands.append(o)
          71 +        if cands:
          72 +            cands.sort(key=lambda o: -(o["y"] + o["h"]))
          73 +            return cands[0]["name"]
          74 +        return "target_block"
          75 +
          76 +    def _drop_x(self, objs, surf, held, block):
          77 +        w = held["w"]
          78 +        occ = [(surf["x"] - 0.02, surf["x"] + surf["w"] + 0.02)]
          79 +        for o in objs.values():
          80 +            if o["name"] == held["name"]:
          81 +                continue
          82 +            occ.append((o["x"], o["x"] + o["w"]))
          83 +        margin = 0.03
          84 +        best, bestc = None, 1e9
          85 +        cur = held["x"] + w / 2
          86 +        for c in np.arange(0.1 + 1e-3, W - 0.1, 0.005):
          87 +            l, r = c - w / 2 - margin, c + w / 2 + margin
          88 +            if l < 0 or r > W:
          89 +                continue
          90 +            if any(l < b and r > a for a, b in occ):
          91 +                continue
          92 +            cost = abs(c - cur)
          93 +            if cost < bestc:
          94 +                best, bestc = c, cost
          95 +        if best is None:
          96 +            best = 0.1 + 1e-3 if surf["x"] > W / 2 else W - 0.1 - 1e-3
          97 +        return best
          98 +
          99 +    # ---------------- main ----------------
         100 +    def get_action(self, state):
         101 +        robot, objs, surf, block = self._parse(state)
         102 +        arm_t = robot["maxarm"]
         103 +        max_top = max([o["y"] + o["h"] for o in objs.values()] + [FLOOR])
         104 +        held = objs.get(self.obj_name) if self.obj_name else None
         105 +
         106 +        # posture correction first
         107 +        dth = np.clip(DOWN - robot["th"], -0.19, 0.19)
         108 +        darm = np.clip(arm_t - robot["arm"], -0.1, 0.1)
         109 +
         110 +        def goto(tx, ty, vac):
         111 +            return self._act(tx - robot["x"], ty - robot["y"], dth, darm, vac)
         112 +
         113 +        def near(a, b, tol=1e-4):
         114 +            return abs(a - b) < tol
         115 +
         116 +        grip_off = arm_t + robot["gw"]  # robot_y - gripper bottom
         117 +        hh = held["h"] if (held and robot["vac"] > 0.5) else 0.0
         118 +        travel_y = min(H - robot["rad"] - 1e-3,
         119 +                       max(max_top + robot["rad"] + 0.03, max_top + 0.03 + grip_off + hh))
         120 +
         121 +        for _ in range(10):
         122 +            ph = self.phase
         123 +            if ph == "lift":
         124 +                if self.obj_name is None:
         125 +                    self.obj_name = self._choose_next(objs, surf, robot)
         126 +                    held = objs[self.obj_name]
         127 +                if robot["y"] < travel_y - 1e-4 or not near(robot["arm"], arm_t) or not near(robot["th"], DOWN):
         128 +                    return goto(robot["x"], max(travel_y, robot["y"]), 0.0)
         129 +                self.phase = "goto"
         130 +                continue
         131 +            if ph == "goto":
         132 +                tgt = objs[self.obj_name]
         133 +                cx = tgt["x"] + tgt["w"] / 2
         134 +                if not near(robot["x"], cx):
         135 +                    return goto(cx, robot["y"], 0.0)
         136 +                self.phase = "descend"
         137 +                continue
         138 +            if ph == "descend":
         139 +                tgt = objs[self.obj_name]
         140 +                ty = tgt["y"] + tgt["h"] + grip_off + 2e-4
         141 +                if not near(robot["y"], ty, 5e-5):
         142 +                    return goto(robot["x"], ty, 0.0)
         143 +                self.phase = "grasp"
         144 +                return goto(robot["x"], robot["y"], 1.0)
         145 +            if ph == "grasp":
         146 +                self.phase = "lift_held"
         147 +                self.grasp_y = objs[self.obj_name]["y"]
         148 +                continue
         149 +            if ph == "lift_held":
         150 +                if robot["y"] < travel_y - 1e-4:
         151 +                    return goto(robot["x"], travel_y, 1.0)
         152 +                tgt = objs[self.obj_name]
         153 +                if tgt["y"] < self.grasp_y + 1e-3:
         154 +                    # grasp failed; retry
         155 +                    self.phase = "lift"
         156 +                    self.obj_name = None
         157 +                    return goto(robot["x"], robot["y"], 0.0)
         158 +                if self.obj_name == "target_block":
         159 +                    self.drop_x = surf["x"] + surf["w"] / 2
         160 +                else:
         161 +                    self.drop_x = self._drop_x(objs, surf, tgt, block)
         162 +                self.phase = "carry"
         163 +                continue
         164 +            if ph == "carry":
         165 +                tgt = objs[self.obj_name]
         166 +                cx = tgt["x"] + tgt["w"] / 2
         167 +                tx = robot["x"] + (self.drop_x - cx)
         168 +                if not near(cx, self.drop_x):
         169 +                    return goto(tx, robot["y"], 1.0)
         170 +                self.phase = "lower"
         171 +                continue
         172 +            if ph == "lower":
         173 +                tgt = objs[self.obj_name]
         174 +                ty = robot["y"] - (tgt["y"] - (FLOOR + 2e-3))
         175 +                if not near(tgt["y"], FLOOR + 2e-3, 5e-4):
         176 +                    return goto(robot["x"], ty, 1.0)
         177 +                self.phase = "release"
         178 +                continue
         179 +            if ph == "release":
         180 +                self.phase = "lift"
         181 +                self.obj_name = None
         182 +                return goto(robot["x"], robot["y"], 0.0)
         183 +        return goto(robot["x"], robot["y"], robot["vac"])
diff --git a/explore.py b/explore.py
new file mode 100644
index 0000000..12fe97d
--- /dev/null
+++ b/explore.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +env = make_env()
           3 +F={'crv_robot':["x", "y", "theta", "base_radius", "arm_joint", "arm_length", "vacuum", "gripper_height", "gripper_width"]}
           4 +R=["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]
           5 +def dump(obs):
           6 +    for n in sorted(obs.get_object_names(), key=str):
           7 +        o = obs.get_object_from_name(n) if isinstance(n,str) else n
           8 +        fs = F.get(o.type.name if hasattr(o.type,'name') else str(o.type), R)
           9 +        print(" ", n, {f: round(float(obs.get(o,f)),3) for f in fs})
          10 +for seed in range(4):
          11 +    obs, info = env.reset(seed=seed)
          12 +    print("seed", seed); dump(obs)
          13 +env.close()
diff --git a/probe.py b/probe.py
new file mode 100644
index 0000000..157e6e2
--- /dev/null
+++ b/probe.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +def rb(o):
           6 +    r=o.get_object_from_name('robot'); return [round(float(o.get(r,f)),3) for f in ["x","y","theta","arm_joint","vacuum"]]
           7 +def blk(o,n='target_block'):
           8 +    b=o.get_object_from_name(n); return [round(float(o.get(b,f)),3) for f in ["x","y","theta"]]
           9 +print(rb(obs))
          10 +for a in [[0.05,0,0,0,0],[0,-0.05,0,0,0],[0,0,0.196,0,0],[0,0,-0.196,0,0],[0,0,0,0.1,0],[0,0,0,0.1,0],[0,0,0,-0.1,0]]:
          11 +    obs,r,t,tr,_=env.step(np.array(a,dtype=np.float32)); print(a, rb(obs), r,t,tr)
          12 +# move down until stop
          13 +for i in range(20):
          14 +    obs,r,t,tr,_=env.step(np.array([0,-0.05,0,0,0],dtype=np.float32))
          15 +print("after down", rb(obs))
          16 +for i in range(20):
          17 +    obs,r,t,tr,_=env.step(np.array([-0.05,0,0,0,0],dtype=np.float32))
          18 +print("after left", rb(obs))
          19 +env.close()
diff --git a/probe2.py b/probe2.py
new file mode 100644
index 0000000..abbfa01
--- /dev/null
+++ b/probe2.py
@@ -0,0 +1,27 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +def rb(o):
           6 +    r=o.get_object_from_name('robot'); return [round(float(o.get(r,f)),4) for f in ["x","y","theta","arm_joint","vacuum"]]
           7 +def blk(o,n='target_block'):
           8 +    b=o.get_object_from_name(n); return [round(float(o.get(b,f)),4) for f in ["x","y","theta"]]
           9 +def st(a):
          10 +    global obs
          11 +    obs,r,t,tr,_=env.step(np.array(a,dtype=np.float32)); return t
          12 +# go to x=0.489
          13 +while abs(rb(obs)[0]-0.489)>1e-4:
          14 +    d=np.clip(0.489-rb(obs)[0],-0.05,0.05); st([d,0,0,0,0])
          15 +print(rb(obs))
          16 +for i in range(80):
          17 +    y0=rb(obs)[1]; st([0,-0.01,0,0,0])
          18 +    if abs(rb(obs)[1]-y0)<1e-6: print("stopped at",rb(obs)); break
          19 +print(rb(obs), blk(obs))
          20 +st([0,0,0,0,1]); print("vac", rb(obs), blk(obs))
          21 +for i in range(5): st([0,0.05,0,0,1])
          22 +print("lift", rb(obs), blk(obs))
          23 +st([0.05,0,0.1,0.1,1]); print("move", rb(obs), blk(obs))
          24 +st([0,0,0,0,0]); print("release", rb(obs), blk(obs))
          25 +for i in range(3): st([0,0,0,0,0])
          26 +print("after", rb(obs), blk(obs))
          27 +env.close()
diff --git a/probe3.py b/probe3.py
new file mode 100644
index 0000000..f7ce152
--- /dev/null
+++ b/probe3.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +def rb(o):
           6 +    r=o.get_object_from_name('robot'); return [round(float(o.get(r,f)),4) for f in ["x","y","theta","arm_joint","vacuum"]]
           7 +def st(a):
           8 +    global obs
           9 +    obs,r,t,tr,_=env.step(np.array(a,dtype=np.float32)); return t
          10 +for d,a in [("right",[0.01,0,0,0,0]),("up",[0,0.01,0,0,0])]:
          11 +    for i in range(200):
          12 +        y0=rb(obs); st(a)
          13 +        if rb(obs)==y0: print(d,"stopped",rb(obs)); break
          14 +env.close()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..1370d4d
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,31 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +from concurrent.futures import ThreadPoolExecutor
           6 +
           7 +def run(seed):
           8 +    env = make_env()
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    obs, info = env.reset(seed=seed)
          11 +    ap.reset(obs, info)
          12 +    t0 = time.time()
          13 +    for step in range(env.max_steps):
          14 +        a = ap.get_action(obs)
          15 +        obs, r, term, trunc, info = env.step(a)
          16 +        if term:
          17 +            env.close(); return seed, True, step + 1, time.time() - t0
          18 +        if trunc:
          19 +            break
          20 +    env.close()
          21 +    return seed, False, env.max_steps, time.time() - t0
          22 +
          23 +if __name__ == "__main__":
          24 +    s0 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
          25 +    n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
          26 +    with ThreadPoolExecutor(8) as ex:
          27 +        res = list(ex.map(run, range(s0, s0 + n)))
          28 +    for r in res:
          29 +        if not r[1]: print("FAIL", r)
          30 +    ok = [r for r in res if r[1]]
          31 +    print(f"success {len(ok)}/{len(res)}, mean steps (succ) {np.mean([r[2] for r in ok]) if ok else 0:.1f}")
```

</details>

<a id="C003"></a>
### C003 · Clamp grasp x to reachable range

Commit `ca413ab4ae17b2090bf33b956f44813a4bdccabe`; parents: 832972742c7dcd83e426eaaf8620ff260cb911ab. Recorded author date: 2026-09-30T11:42:08+02:00.

File roles (automatic): policy.

- [E0071](01_timeline.md#E0071): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_ca413ab_approach.py) · [Exact all-file diff](evidence/diffs/C003_ca413ab.diff)

[Previous saved controller snapshot](evidence/versions/C002_8329727_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 738ce82..be60912 100644
--- a/approach.py
+++ b/approach.py
@@ -96,6 +96,10 @@ class GeneratedApproach:
   96     96              best = 0.1 + 1e-3 if surf["x"] > W / 2 else W - 0.1 - 1e-3
   97     97          return best
   98     98  
          99 +    def _grasp_x(self, tgt, robot):
         100 +        lo, hi = robot["rad"] + 1e-3, W - robot["rad"] - 1e-3
         101 +        return float(np.clip(tgt["x"] + tgt["w"] / 2, lo, hi))
         102 +
   99    103      # ---------------- main ----------------
  100    104      def get_action(self, state):
  101    105          robot, objs, surf, block = self._parse(state)
@@ -130,7 +134,7 @@ class GeneratedApproach:
  130    134                  continue
  131    135              if ph == "goto":
  132    136                  tgt = objs[self.obj_name]
  133        -                cx = tgt["x"] + tgt["w"] / 2
         137 +                cx = self._grasp_x(tgt, robot)
  134    138                  if not near(robot["x"], cx):
  135    139                      return goto(cx, robot["y"], 0.0)
  136    140                  self.phase = "descend"
```

</details>

<a id="C004"></a>
### C004 · Rewrite: clearance-profile motion, placement planning, reachable grasp offsets

Commit `e4c016a8afbda5eb20852a1787812d226e839d6f`; parents: ca413ab4ae17b2090bf33b956f44813a4bdccabe. Recorded author date: 2026-09-30T11:47:38+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0094](01_timeline.md#E0094): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_e4c016a_approach.py) · [Exact all-file diff](evidence/diffs/C004_e4c016a.diff)

[Previous saved controller snapshot](evidence/versions/C003_ca413ab_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index be60912..8487c8d 100644
--- a/approach.py
+++ b/approach.py
@@ -3,6 +3,16 @@ import numpy as np
    3      3  W, H = 1.618, 1.0
    4      4  FLOOR = 0.1
    5      5  DOWN = -np.pi / 2
           6 +MARGIN = 0.012      # vertical clearance margin to obstacles
           7 +XMARGIN = 0.006     # horizontal clearance margin to obstacles
           8 +GRASP_GAP = 2e-4    # gap between gripper and object top when grasping
           9 +PLACE_GAP = 2e-3    # gap between object bottom and floor when placing
          10 +MAXD = 0.05
          11 +
          12 +
          13 +def _tname(o):
          14 +    t = o.type
          15 +    return t.name if hasattr(t, "name") else str(t)
    6     16  
    7     17  
    8     18  class GeneratedApproach:
@@ -12,176 +22,334 @@ class GeneratedApproach:
   12     22          self.reset(None, None)
   13     23  
   14     24      def reset(self, state, info):
   15        -        self.phase = "lift"
   16        -        self.obj_name = None
   17        -        self.drop_x = None
   18        -        self.last_robot = None
          25 +        self.mode = "pick"
          26 +        self.cur = None           # name of object currently being handled
          27 +        self.grasp_off = 0.0      # robot_x - object center x (planned / actual)
          28 +        self.drop = None          # (object center x) target for placement/drop
          29 +        self.place_c = None       # planned block center on surface
          30 +        self.block_g = 0.0
          31 +        self.blockers = None
          32 +        self.last_pose = None
   19     33          self.stuck = 0
          34 +        self.escape = 0
          35 +        self.done = set()
   20     36  
   21        -    # ---------------- helpers ----------------
   22        -    def _rect(self, s, o):
   23        -        g = lambda f: float(s.get(o, f))
   24        -        return dict(name=o.name, x=g("x"), y=g("y"), w=g("width"), h=g("height"))
   25        -
          37 +    # ------------------------------------------------------------------
   26     38      def _parse(self, s):
   27        -        r = s.get_objects(self._rtype(s))[0]
   28        -        g = lambda f: float(s.get(r, f))
   29        -        robot = dict(x=g("x"), y=g("y"), th=g("theta"), arm=g("arm_joint"),
   30        -                     vac=g("vacuum"), gw=g("gripper_width"), gh=g("gripper_height"),
   31        -                     rad=g("base_radius"), maxarm=g("arm_length"))
          39 +        robot = None
   32     40          objs = {}
   33        -        surf = block = None
          41 +        surf = None
   34     42          for n in s.get_object_names():
   35        -            o = n if not isinstance(n, str) else s.get_object_from_name(n)
   36        -            tn = o.type.name if hasattr(o.type, "name") else str(o.type)
          43 +            o = s.get_object_from_name(n) if isinstance(n, str) else n
          44 +            tn = _tname(o)
          45 +            g = lambda f: float(s.get(o, f))
   37     46              if tn == "crv_robot":
          47 +                robot = dict(x=g("x"), y=g("y"), th=g("theta"), arm=g("arm_joint"),
          48 +                             vac=g("vacuum"), gw=g("gripper_width"), gh=g("gripper_height"),
          49 +                             r=g("base_radius"), maxarm=g("arm_length"))
   38     50                  continue
   39        -            rr = self._rect(s, o)
   40        -            rr["type"] = tn
          51 +            rr = dict(name=o.name, type=tn, x=g("x"), y=g("y"), w=g("width"), h=g("height"))
          52 +            rr["cx"] = rr["x"] + rr["w"] / 2
          53 +            rr["top"] = rr["y"] + rr["h"]
   41     54              if tn == "target_surface":
   42     55                  surf = rr
   43     56              else:
   44     57                  objs[rr["name"]] = rr
   45        -                if tn == "target_block":
   46        -                    block = rr
   47        -        return robot, objs, surf, block
   48        -
   49        -    def _rtype(self, s):
   50        -        for n in s.get_object_names():
   51        -            o = n if not isinstance(n, str) else s.get_object_from_name(n)
   52        -            tn = o.type.name if hasattr(o.type, "name") else str(o.type)
   53        -            if tn == "crv_robot":
   54        -                return o.type
   55        -        raise RuntimeError
          58 +        return robot, objs, surf
   56     59  
   57     60      def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0, vac=0.0):
   58     61          a = np.array([dx, dy, dth, darm, vac], dtype=np.float64)
   59     62          a = np.clip(a, self.low, self.high)
   60     63          return a.astype(np.float32)
   61     64  
   62        -    def _choose_next(self, objs, surf, robot):
   63        -        # obstructions that conflict with placing the block on the surface
   64        -        sx0, sx1 = surf["x"], surf["x"] + surf["w"]
   65        -        cands = []
   66        -        for o in objs.values():
   67        -            if o["type"] == "target_block":
          65 +    # ---------------- geometry ----------------
          66 +    def _parts(self, robot, held=None, held_off=None, held_depth=None):
          67 +        """Footprint parts relative to robot x: (lo, hi, depth below robot y)."""
          68 +        arm = robot["maxarm"]
          69 +        parts = [(-robot["r"], robot["r"], robot["r"]),
          70 +                 (-robot["gh"] / 2, robot["gh"] / 2, arm + robot["gw"])]
          71 +        if held is not None:
          72 +            # held_off: object left edge relative to robot x; held_depth: robot y - object bottom
          73 +            parts.append((held_off, held_off + held["w"], held_depth))
          74 +        return parts
          75 +
          76 +    def _req(self, x, parts, obst):
          77 +        """Min robot y at horizontal position x so no part collides."""
          78 +        req = 0.0
          79 +        for lo, hi, d in parts:
          80 +            a, b = x + lo, x + hi
          81 +            req = max(req, FLOOR + d)  # floor
          82 +            for (o0, o1, top) in obst:
          83 +                if a < o1 + XMARGIN and b > o0 - XMARGIN:
          84 +                    req = max(req, top + d + MARGIN)
          85 +        return req
          86 +
          87 +    def _req_range(self, x0, x1, parts, obst):
          88 +        lo, hi = min(x0, x1), max(x0, x1)
          89 +        req = 0.0
          90 +        for plo, phi, d in parts:
          91 +            a, b = lo + plo, hi + phi
          92 +            req = max(req, FLOOR + d)
          93 +            for (o0, o1, top) in obst:
          94 +                if a < o1 + XMARGIN and b > o0 - XMARGIN:
          95 +                    req = max(req, top + d + MARGIN)
          96 +        return req
          97 +
          98 +    def _obst(self, objs, exclude=()):
          99 +        return [(o["x"], o["x"] + o["w"], o["top"]) for n, o in objs.items() if n not in exclude]
         100 +
         101 +    def _xlim(self, robot):
         102 +        return robot["r"] + 1e-3, W - robot["r"] - 1e-3
         103 +
         104 +    # ---------------- motion ----------------
         105 +    def _move(self, robot, tx, ty, parts, obst, vac):
         106 +        """One step toward (tx, ty) staying above clearance profile. Returns (action, arrived)."""
         107 +        x, y = robot["x"], robot["y"]
         108 +        ymax = H - robot["r"] - 1e-3
         109 +        dth = float(np.clip(DOWN - robot["th"], -0.19, 0.19))
         110 +        darm = float(np.clip(robot["maxarm"] - robot["arm"], -0.1, 0.1))
         111 +        posture_ok = abs(dth) < 1e-4 and abs(darm) < 1e-4
         112 +        if abs(tx - x) < 1e-5 and abs(ty - y) < 3e-5 and posture_ok:
         113 +            return None, True
         114 +        dx = float(np.clip(tx - x, -MAXD, MAXD))
         115 +        x1 = x + dx
         116 +        # lookahead requirement from x1 toward tx (slope-1 relaxation)
         117 +        R = self._req_range(x, x1, parts, obst)
         118 +        if abs(tx - x1) > 1e-6:
         119 +            n = int(abs(tx - x1) / 0.01) + 1
         120 +            for i in range(1, n + 1):
         121 +                xs = x1 + (tx - x1) * i / n
         122 +                r_here = self._req(xs, parts, obst)
         123 +                if i == n:
         124 +                    r_here = min(r_here, ty)
         125 +                R = max(R, r_here - abs(xs - x1))
         126 +        else:
         127 +            R = min(R, ty)
         128 +        R = min(R, ymax)
         129 +        y_des = y + float(np.clip(ty - y, -MAXD, MAXD))
         130 +        y1 = max(y_des, R)
         131 +        if y1 - y > MAXD + 1e-9:
         132 +            # cannot rise enough while moving horizontally: rise first
         133 +            dx = 0.0
         134 +            y1 = y + MAXD
         135 +        dy = y1 - y
         136 +        return self._act(dx, dy, dth, darm, vac), False
         137 +
         138 +    # ---------------- planning ----------------
         139 +    def _plan_block(self, robot, objs, surf):
         140 +        blk = objs["target_block"]
         141 +        bw = blk["w"]
         142 +        lo, hi = self._xlim(robot)
         143 +        s0, s1 = surf["x"], surf["x"] + surf["w"]
         144 +        cmin, cmax = s0 + bw / 2 + 0.002, s1 - bw / 2 - 0.002
         145 +        if cmax < cmin:
         146 +            cmin = cmax = (s0 + s1) / 2
         147 +        obstructions = [o for n, o in objs.items() if n != "target_block"]
         148 +        center = (s0 + s1) / 2
         149 +        best = None
         150 +        cands = list(np.linspace(cmin, cmax, max(2, int((cmax - cmin) / 0.002) + 1)))
         151 +        cands.append(center)
         152 +        gmax = max(0.0, bw / 2 - 0.004)
         153 +        place_depth = None
         154 +        for c in cands:
         155 +            c = float(np.clip(c, cmin, cmax))
         156 +            # grasp offset g so that robot x at placement and at grasp is reachable
         157 +            glo = max(-gmax, lo - c, lo - blk["cx"])
         158 +            ghi = min(gmax, hi - c, hi - blk["cx"])
         159 +            if glo > ghi:
   68    160                  continue
   69        -            if o["x"] < sx1 + 0.005 and o["x"] + o["w"] > sx0 - 0.005 and o["y"] < FLOOR + 0.3:
   70        -                cands.append(o)
   71        -        if cands:
   72        -            cands.sort(key=lambda o: -(o["y"] + o["h"]))
   73        -            return cands[0]["name"]
   74        -        return "target_block"
         161 +            g = float(np.clip(0.0, glo, ghi))
         162 +            blockers = set()
         163 +            for o in obstructions:
         164 +                if o["x"] < c + bw / 2 + 0.003 and o["x"] + o["w"] > c - bw / 2 - 0.003:
         165 +                    blockers.add(o["name"])
         166 +            # also obstacles that would hit the robot when placing
         167 +            depth = robot["maxarm"] + robot["gw"] + blk["h"]
         168 +            parts = self._parts(robot, blk, -g - bw / 2, depth)
         169 +            ty = FLOOR + PLACE_GAP + depth
         170 +            for o in obstructions:
         171 +                if o["name"] in blockers:
         172 +                    continue
         173 +                if self._req(c + g, parts, [(o["x"], o["x"] + o["w"], o["top"])]) > ty + 1e-6:
         174 +                    blockers.add(o["name"])
         175 +            cost = (len(blockers), abs(g) > 1e-6, abs(g), abs(c - center))
         176 +            if best is None or cost < best[0]:
         177 +                best = (cost, c, g, blockers)
         178 +        if best is None:
         179 +            c = float(np.clip(center, lo, hi))
         180 +            return c, 0.0, set(o["name"] for o in obstructions)
         181 +        return best[1], best[2], best[3]
         182 +
         183 +    def _grasp_x(self, robot, obj, objs, prefer_g=0.0):
         184 +        """Choose robot x to grasp obj (reachable, collision free)."""
         185 +        lo, hi = self._xlim(robot)
         186 +        parts = self._parts(robot)
         187 +        obst = self._obst(objs, exclude=(obj["name"],))
         188 +        ty = obj["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
         189 +        gmax = max(0.0, obj["w"] / 2 - 0.004)
         190 +        best = None
         191 +        for g in np.linspace(-gmax, gmax, 41).tolist() + [prefer_g, 0.0]:
         192 +            if abs(g) > gmax + 1e-9:
         193 +                continue
         194 +            x = obj["cx"] + g
         195 +            if x < lo or x > hi:
         196 +                continue
         197 +            ok = self._req(x, parts, obst) <= ty + 1e-9
         198 +            cost = (not ok, abs(g - prefer_g))
         199 +            if best is None or cost < best[0]:
         200 +                best = (cost, x)
         201 +        if best is None:
         202 +            return float(np.clip(obj["cx"], lo, hi)), ty
         203 +        return best[1], ty
   75    204  
   76        -    def _drop_x(self, objs, surf, held, block):
         205 +    def _drop_spot(self, robot, objs, held, g, next_x):
         206 +        """Choose drop center for obstruction held with offset g (robot_x - center)."""
         207 +        lo, hi = self._xlim(robot)
   77    208          w = held["w"]
   78        -        occ = [(surf["x"] - 0.02, surf["x"] + surf["w"] + 0.02)]
   79        -        for o in objs.values():
   80        -            if o["name"] == held["name"]:
         209 +        others = {n: o for n, o in objs.items() if n != held["name"]}
         210 +        obst = self._obst(others)
         211 +        depth = robot["y"] - held["y"]
         212 +        ty_off = FLOOR + PLACE_GAP
         213 +        parts = self._parts(robot, held, -g - w / 2, depth)
         214 +        # reserved zones: block placement and robot columns for future block ops
         215 +        blk = objs.get("target_block")
         216 +        reserved = []
         217 +        if self.place_c is not None and blk is not None:
         218 +            bw = blk["w"]
         219 +            reserved.append((self.place_c - bw / 2 - 0.01, self.place_c + bw / 2 + 0.01))
         220 +        cur = held["cx"]
         221 +        best = None
         222 +        for c in np.arange(w / 2 + 0.002, W - w / 2 - 0.002, 0.004):
         223 +            c = float(c)
         224 +            rx = c + g
         225 +            if rx < lo or rx > hi:
   81    226                  continue
   82        -            occ.append((o["x"], o["x"] + o["w"]))
   83        -        margin = 0.03
   84        -        best, bestc = None, 1e9
   85        -        cur = held["x"] + w / 2
   86        -        for c in np.arange(0.1 + 1e-3, W - 0.1, 0.005):
   87        -            l, r = c - w / 2 - margin, c + w / 2 + margin
   88        -            if l < 0 or r > W:
         227 +            a, b = c - w / 2, c + w / 2
         228 +            if any(a < o1 + 0.01 and b > o0 - 0.01 for (o0, o1, _) in obst):
   89    229                  continue
   90        -            if any(l < b and r > a for a, b in occ):
         230 +            if any(a < r1 and b > r0 for (r0, r1) in reserved):
   91    231                  continue
   92        -            cost = abs(c - cur)
   93        -            if cost < bestc:
   94        -                best, bestc = c, cost
         232 +            ty = ty_off + depth
         233 +            if self._req(rx, parts, obst) > ty + 1e-9:
         234 +                continue
         235 +            # does dropping here block future block grasp/placement?
         236 +            if blk is not None and self.place_c is not None:
         237 +                newob = [(a, b, FLOOR + held["h"])]
         238 +                bparts = self._parts(robot)
         239 +                gx = blk["cx"] + self.block_g
         240 +                gty = blk["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
         241 +                if self._req(gx, bparts, newob) > gty + 1e-9:
         242 +                    continue
         243 +                bdepth = robot["maxarm"] + robot["gw"] + blk["h"]
         244 +                pparts = self._parts(robot, blk, -self.block_g - blk["w"] / 2, bdepth)
         245 +                pty = FLOOR + PLACE_GAP + bdepth
         246 +                if self._req(self.place_c + self.block_g, pparts, newob) > pty + 1e-9:
         247 +                    continue
         248 +            cost = abs(c - cur) + abs(c + g - next_x) + 1e-3 * abs(c - cur)
         249 +            if best is None or cost < best[0]:
         250 +                best = (cost, c)
   95    251          if best is None:
   96        -            best = 0.1 + 1e-3 if surf["x"] > W / 2 else W - 0.1 - 1e-3
   97        -        return best
   98        -
   99        -    def _grasp_x(self, tgt, robot):
  100        -        lo, hi = robot["rad"] + 1e-3, W - robot["rad"] - 1e-3
  101        -        return float(np.clip(tgt["x"] + tgt["w"] / 2, lo, hi))
         252 +            return None
         253 +        return best[1]
  102    254  
  103    255      # ---------------- main ----------------
  104    256      def get_action(self, state):
  105        -        robot, objs, surf, block = self._parse(state)
  106        -        arm_t = robot["maxarm"]
  107        -        max_top = max([o["y"] + o["h"] for o in objs.values()] + [FLOOR])
  108        -        held = objs.get(self.obj_name) if self.obj_name else None
  109        -
  110        -        # posture correction first
  111        -        dth = np.clip(DOWN - robot["th"], -0.19, 0.19)
  112        -        darm = np.clip(arm_t - robot["arm"], -0.1, 0.1)
  113        -
  114        -        def goto(tx, ty, vac):
  115        -            return self._act(tx - robot["x"], ty - robot["y"], dth, darm, vac)
  116        -
  117        -        def near(a, b, tol=1e-4):
  118        -            return abs(a - b) < tol
  119        -
  120        -        grip_off = arm_t + robot["gw"]  # robot_y - gripper bottom
  121        -        hh = held["h"] if (held and robot["vac"] > 0.5) else 0.0
  122        -        travel_y = min(H - robot["rad"] - 1e-3,
  123        -                       max(max_top + robot["rad"] + 0.03, max_top + 0.03 + grip_off + hh))
  124        -
  125        -        for _ in range(10):
  126        -            ph = self.phase
  127        -            if ph == "lift":
  128        -                if self.obj_name is None:
  129        -                    self.obj_name = self._choose_next(objs, surf, robot)
  130        -                    held = objs[self.obj_name]
  131        -                if robot["y"] < travel_y - 1e-4 or not near(robot["arm"], arm_t) or not near(robot["th"], DOWN):
  132        -                    return goto(robot["x"], max(travel_y, robot["y"]), 0.0)
  133        -                self.phase = "goto"
  134        -                continue
  135        -            if ph == "goto":
  136        -                tgt = objs[self.obj_name]
  137        -                cx = self._grasp_x(tgt, robot)
  138        -                if not near(robot["x"], cx):
  139        -                    return goto(cx, robot["y"], 0.0)
  140        -                self.phase = "descend"
  141        -                continue
  142        -            if ph == "descend":
  143        -                tgt = objs[self.obj_name]
  144        -                ty = tgt["y"] + tgt["h"] + grip_off + 2e-4
  145        -                if not near(robot["y"], ty, 5e-5):
  146        -                    return goto(robot["x"], ty, 0.0)
  147        -                self.phase = "grasp"
  148        -                return goto(robot["x"], robot["y"], 1.0)
  149        -            if ph == "grasp":
  150        -                self.phase = "lift_held"
  151        -                self.grasp_y = objs[self.obj_name]["y"]
  152        -                continue
  153        -            if ph == "lift_held":
  154        -                if robot["y"] < travel_y - 1e-4:
  155        -                    return goto(robot["x"], travel_y, 1.0)
  156        -                tgt = objs[self.obj_name]
  157        -                if tgt["y"] < self.grasp_y + 1e-3:
  158        -                    # grasp failed; retry
  159        -                    self.phase = "lift"
  160        -                    self.obj_name = None
  161        -                    return goto(robot["x"], robot["y"], 0.0)
  162        -                if self.obj_name == "target_block":
  163        -                    self.drop_x = surf["x"] + surf["w"] / 2
         257 +        robot, objs, surf = self._parse(state)
         258 +        if self.place_c is None:
         259 +            self.place_c, self.block_g, self.blockers = self._plan_block(robot, objs, surf)
         260 +
         261 +        # stuck detection / escape
         262 +        pose = (round(robot["x"], 6), round(robot["y"], 6))
         263 +        if self.escape > 0:
         264 +            self.escape -= 1
         265 +            self.last_pose = pose
         266 +            return self._act(0.0, MAXD, 0.0, 0.0, robot["vac"])
         267 +        if self.last_pose == pose and self.mode in ("pick", "carry"):
         268 +            self.stuck += 1
         269 +            if self.stuck >= 3:
         270 +                self.stuck = 0
         271 +                self.escape = 2
         272 +        else:
         273 +            self.stuck = 0
         274 +        self.last_pose = pose
         275 +
         276 +        for _ in range(6):
         277 +            if self.mode == "pick":
         278 +                if self.cur is None:
         279 +                    self.cur = self._next_target(robot, objs)
         280 +                obj = objs[self.cur]
         281 +                prefer = self.block_g if self.cur == "target_block" else 0.0
         282 +                gx, gty = self._grasp_x(robot, obj, objs, prefer)
         283 +                parts = self._parts(robot)
         284 +                obst = self._obst(objs, exclude=(obj["name"],))
         285 +                act, arrived = self._move(robot, gx, gty, parts, obst, 0.0)
         286 +                if not arrived:
         287 +                    return act
         288 +                self.mode = "grasp"
         289 +                self.grasp_y = obj["y"]
         290 +                return self._act(0, 0, 0, 0, 1.0)
         291 +            if self.mode == "grasp":
         292 +                obj = objs[self.cur]
         293 +                self.g_actual = robot["x"] - obj["cx"]
         294 +                self.depth = robot["y"] - obj["y"]
         295 +                if self.cur == "target_block":
         296 +                    self.drop = self.place_c
  164    297                  else:
  165        -                    self.drop_x = self._drop_x(objs, surf, tgt, block)
  166        -                self.phase = "carry"
  167        -                continue
  168        -            if ph == "carry":
  169        -                tgt = objs[self.obj_name]
  170        -                cx = tgt["x"] + tgt["w"] / 2
  171        -                tx = robot["x"] + (self.drop_x - cx)
  172        -                if not near(cx, self.drop_x):
  173        -                    return goto(tx, robot["y"], 1.0)
  174        -                self.phase = "lower"
         298 +                    nxt = self._peek_next(robot, objs, exclude=self.cur)
         299 +                    d = self._drop_spot(robot, objs, obj, self.g_actual, nxt)
         300 +                    if d is None:
         301 +                        d = obj["cx"]  # fallback: lift and put back higher later
         302 +                    self.drop = d
         303 +                self.mode = "carry"
  175    304                  continue
  176        -            if ph == "lower":
  177        -                tgt = objs[self.obj_name]
  178        -                ty = robot["y"] - (tgt["y"] - (FLOOR + 2e-3))
  179        -                if not near(tgt["y"], FLOOR + 2e-3, 5e-4):
  180        -                    return goto(robot["x"], ty, 1.0)
  181        -                self.phase = "release"
  182        -                continue
  183        -            if ph == "release":
  184        -                self.phase = "lift"
  185        -                self.obj_name = None
  186        -                return goto(robot["x"], robot["y"], 0.0)
  187        -        return goto(robot["x"], robot["y"], robot["vac"])
         305 +            if self.mode == "carry":
         306 +                obj = objs[self.cur]
         307 +                if robot["vac"] < 0.5:
         308 +                    self.mode = "pick"
         309 +                    continue
         310 +                parts = self._parts(robot, obj, obj["x"] - robot["x"], robot["y"] - obj["y"])
         311 +                obst = self._obst(objs, exclude=(obj["name"],))
         312 +                tx = self.drop + (robot["x"] - obj["cx"])
         313 +                ty = robot["y"] - obj["y"] + FLOOR + PLACE_GAP
         314 +                act, arrived = self._move(robot, tx, ty, parts, obst, 1.0)
         315 +                # detect failed grasp: object not following
         316 +                if abs(robot["y"] - obj["y"] - self.depth) > 5e-3:
         317 +                    self.mode = "pick"
         318 +                    return self._act(0, 0, 0, 0, 0.0)
         319 +                if not arrived:
         320 +                    return act
         321 +                self.mode = "pick"
         322 +                self.cur = None
         323 +                return self._act(0, 0, 0, 0, 0.0)
         324 +        return self._act(0, 0, 0, 0, robot["vac"])
         325 +
         326 +    def _remaining_blockers(self, objs):
         327 +        return [n for n in self.blockers if n in objs and self._still_blocks(objs[n], objs)]
         328 +
         329 +    def _still_blocks(self, o, objs):
         330 +        blk = objs["target_block"]
         331 +        bw = blk["w"]
         332 +        c = self.place_c
         333 +        if o["x"] < c + bw / 2 + 0.003 and o["x"] + o["w"] > c - bw / 2 - 0.003:
         334 +            return True
         335 +        return False if o.get("_moved") else True
         336 +
         337 +    def _next_target(self, robot, objs):
         338 +        rem = [n for n in self.blockers if n in objs]
         339 +        rem = [n for n in rem if n not in getattr(self, "done", set())]
         340 +        if not hasattr(self, "done"):
         341 +            self.done = set()
         342 +        if rem:
         343 +            rem.sort(key=lambda n: abs(objs[n]["cx"] - robot["x"]))
         344 +            n = rem[0]
         345 +            self.done.add(n)
         346 +            return n
         347 +        return "target_block"
         348 +
         349 +    def _peek_next(self, robot, objs, exclude):
         350 +        done = getattr(self, "done", set())
         351 +        rem = [n for n in self.blockers if n in objs and n not in done and n != exclude]
         352 +        if rem:
         353 +            rem.sort(key=lambda n: abs(objs[n]["cx"] - robot["x"]))
         354 +            return objs[rem[0]]["cx"]
         355 +        return objs["target_block"]["cx"] + self.block_g
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..89a425b
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,19 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 200
           6 +env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
           7 +obs, info = env.reset(seed=seed); ap.reset(obs, info)
           8 +r0,objs,surf,blk=ap._parse(obs)
           9 +print("surf",surf); [print(o) for o in objs.values()]
          10 +prev=None
          11 +for step in range(N):
          12 +    a = ap.get_action(obs)
          13 +    obs, r, term, trunc, info = env.step(a)
          14 +    rb=ap._parse(obs)[0]
          15 +    key=(ap.phase,ap.obj_name)
          16 +    if key!=prev or step%50==0: print(step,key,[round(v,3) for v in (rb['x'],rb['y'],rb['th'],rb['arm'],rb['vac'])],np.round(a,3))
          17 +    prev=key
          18 +    if term: print("DONE",step+1);break
          19 +env.close()
```

</details>

<a id="C005"></a>
### C005 · Clearance planner approach: 100/100, 35.9 steps

Commit `9bb174d296bfcd692fd761fd121883efe4f5fe29`; parents: e4c016a8afbda5eb20852a1787812d226e839d6f. Recorded author date: 2026-09-30T11:48:55+02:00.

File roles (automatic): support code (role needs review).

- [E0108](01_timeline.md#E0108): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C005_9bb174d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/dbg.py b/dbg.py
index 89a425b..058b94b 100644
--- a/dbg.py
+++ b/dbg.py
@@ -5,14 +5,14 @@ from approach import GeneratedApproach
    5      5  seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 200
    6      6  env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
    7      7  obs, info = env.reset(seed=seed); ap.reset(obs, info)
    8        -r0,objs,surf,blk=ap._parse(obs)
           8 +r0,objs,surf=ap._parse(obs)
    9      9  print("surf",surf); [print(o) for o in objs.values()]
   10     10  prev=None
   11     11  for step in range(N):
   12     12      a = ap.get_action(obs)
   13     13      obs, r, term, trunc, info = env.step(a)
   14     14      rb=ap._parse(obs)[0]
   15        -    key=(ap.phase,ap.obj_name)
          15 +    key=(ap.mode,ap.cur)
   16     16      if key!=prev or step%50==0: print(step,key,[round(v,3) for v in (rb['x'],rb['y'],rb['th'],rb['arm'],rb['vac'])],np.round(a,3))
   17     17      prev=key
   18     18      if term: print("DONE",step+1);break
```

</details>

<a id="C006"></a>
### C006 · Feasibility-aware target ordering, drop-spot fallbacks

Commit `6715e9125d9abd81f42816e0fe7961e35a298ce3`; parents: 9bb174d296bfcd692fd761fd121883efe4f5fe29. Recorded author date: 2026-09-30T11:58:42+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0155](01_timeline.md#E0155): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_6715e91_approach.py) · [Exact all-file diff](evidence/diffs/C006_6715e91.diff)

[Previous saved controller snapshot](evidence/versions/C004_e4c016a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8487c8d..588cb11 100644
--- a/approach.py
+++ b/approach.py
@@ -200,9 +200,25 @@ class GeneratedApproach:
  200    200                  best = (cost, x)
  201    201          if best is None:
  202    202              return float(np.clip(obj["cx"], lo, hi)), ty
         203 +        self._last_grasp_ok = not best[0][0]
  203    204          return best[1], ty
  204    205  
  205        -    def _drop_spot(self, robot, objs, held, g, next_x):
         206 +    def _grasp_ok(self, robot, obj, objs, prefer_g=0.0):
         207 +        self._last_grasp_ok = False
         208 +        gx, ty = self._grasp_x(robot, obj, objs, prefer_g)
         209 +        return self._last_grasp_ok, gx, ty
         210 +
         211 +    def _violators(self, robot, obj, objs, gx, ty):
         212 +        parts = self._parts(robot)
         213 +        res = []
         214 +        for n, o in objs.items():
         215 +            if n == obj["name"]:
         216 +                continue
         217 +            if self._req(gx, parts, [(o["x"], o["x"] + o["w"], o["top"])]) > ty + 1e-9:
         218 +                res.append(n)
         219 +        return res
         220 +
         221 +    def _drop_spot(self, robot, objs, held, g, next_x, strict=True):
  206    222          """Choose drop center for obstruction held with offset g (robot_x - center)."""
  207    223          lo, hi = self._xlim(robot)
  208    224          w = held["w"]
@@ -225,7 +241,8 @@ class GeneratedApproach:
  225    241              if rx < lo or rx > hi:
  226    242                  continue
  227    243              a, b = c - w / 2, c + w / 2
  228        -            if any(a < o1 + 0.01 and b > o0 - 0.01 for (o0, o1, _) in obst):
         244 +            sep = 0.01 if strict else 0.002
         245 +            if any(a < o1 + sep and b > o0 - sep for (o0, o1, _) in obst):
  229    246                  continue
  230    247              if any(a < r1 and b > r0 for (r0, r1) in reserved):
  231    248                  continue
@@ -233,7 +250,7 @@ class GeneratedApproach:
  233    250              if self._req(rx, parts, obst) > ty + 1e-9:
  234    251                  continue
  235    252              # does dropping here block future block grasp/placement?
  236        -            if blk is not None and self.place_c is not None:
         253 +            if strict and blk is not None and self.place_c is not None:
  237    254                  newob = [(a, b, FLOOR + held["h"])]
  238    255                  bparts = self._parts(robot)
  239    256                  gx = blk["cx"] + self.block_g
@@ -252,6 +269,23 @@ class GeneratedApproach:
  252    269              return None
  253    270          return best[1]
  254    271  
         272 +    def _air_spot(self, robot, objs, held, g):
         273 +        lo, hi = self._xlim(robot)
         274 +        blk = objs.get("target_block")
         275 +        best = None
         276 +        for rx in np.linspace(lo, hi, 200):
         277 +            c = float(rx) - g
         278 +            a, b = c - held["w"] / 2, c + held["w"] / 2
         279 +            d = 0.0
         280 +            for zc in [self.place_c + self.block_g, (blk["cx"] + self.block_g) if blk else None]:
         281 +                if zc is not None:
         282 +                    d = min(d, abs(rx - zc) - 0.35) if d < 0 else min(abs(rx - zc) - 0.35, 1e9)
         283 +            score = min(abs(float(rx) - (self.place_c + self.block_g)),
         284 +                        abs(float(rx) - (blk["cx"] + self.block_g)) if blk else 1e9)
         285 +            if best is None or score > best[0]:
         286 +                best = (score, c)
         287 +        return best[1]
         288 +
  255    289      # ---------------- main ----------------
  256    290      def get_action(self, state):
  257    291          robot, objs, surf = self._parse(state)
@@ -298,7 +332,11 @@ class GeneratedApproach:
  298    332                      nxt = self._peek_next(robot, objs, exclude=self.cur)
  299    333                      d = self._drop_spot(robot, objs, obj, self.g_actual, nxt)
  300    334                      if d is None:
  301        -                        d = obj["cx"]  # fallback: lift and put back higher later
         335 +                        d = self._drop_spot(robot, objs, obj, self.g_actual, nxt, strict=False)
         336 +                    self.drop_y = None
         337 +                    if d is None:
         338 +                        d = self._air_spot(robot, objs, obj, self.g_actual)
         339 +                        self.drop_y = H - robot["r"] - 1e-3
  302    340                      self.drop = d
  303    341                  self.mode = "carry"
  304    342                  continue
@@ -311,6 +349,8 @@ class GeneratedApproach:
  311    349                  obst = self._obst(objs, exclude=(obj["name"],))
  312    350                  tx = self.drop + (robot["x"] - obj["cx"])
  313    351                  ty = robot["y"] - obj["y"] + FLOOR + PLACE_GAP
         352 +                if self.cur != "target_block" and getattr(self, "drop_y", None) is not None:
         353 +                    ty = self.drop_y
  314    354                  act, arrived = self._move(robot, tx, ty, parts, obst, 1.0)
  315    355                  # detect failed grasp: object not following
  316    356                  if abs(robot["y"] - obj["y"] - self.depth) > 5e-3:
@@ -335,16 +375,31 @@ class GeneratedApproach:
  335    375          return False if o.get("_moved") else True
  336    376  
  337    377      def _next_target(self, robot, objs):
  338        -        rem = [n for n in self.blockers if n in objs]
  339        -        rem = [n for n in rem if n not in getattr(self, "done", set())]
  340        -        if not hasattr(self, "done"):
  341        -            self.done = set()
  342        -        if rem:
  343        -            rem.sort(key=lambda n: abs(objs[n]["cx"] - robot["x"]))
  344        -            n = rem[0]
         378 +        rem = [n for n in self.blockers if n in objs and n not in self.done]
         379 +        goals = rem if rem else ["target_block"]
         380 +        goals = sorted(goals, key=lambda n: abs(objs[n]["cx"] - robot["x"]))
         381 +        infeasible = []
         382 +        for n in goals:
         383 +            pref = self.block_g if n == "target_block" else 0.0
         384 +            ok, gx, ty = self._grasp_ok(robot, objs[n], objs, pref)
         385 +            if ok:
         386 +                if n != "target_block":
         387 +                    self.done.add(n)
         388 +                return n
         389 +            infeasible.append((n, gx, ty))
         390 +        # nothing directly graspable: move an obstacle that blocks a goal's grasp
         391 +        for n, gx, ty in infeasible:
         392 +            for v in self._violators(robot, objs[n], objs, gx, ty):
         393 +                if v == "target_block":
         394 +                    continue
         395 +                ok, _, _ = self._grasp_ok(robot, objs[v], objs)
         396 +                if ok:
         397 +                    self.done.add(v)
         398 +                    return v
         399 +        n = goals[0]
         400 +        if n != "target_block":
  345    401              self.done.add(n)
  346        -            return n
  347        -        return "target_block"
         402 +        return n
  348    403  
  349    404      def _peek_next(self, robot, objs, exclude):
  350    405          done = getattr(self, "done", set())
diff --git a/dbg.py b/dbg.py
index 058b94b..50595af 100644
--- a/dbg.py
+++ b/dbg.py
@@ -4,7 +4,8 @@ from env_client import make_env
    4      4  from approach import GeneratedApproach
    5      5  seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 200
    6      6  env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
    7        -obs, info = env.reset(seed=seed); ap.reset(obs, info)
           7 +OC=int(sys.argv[3]) if len(sys.argv)>3 else None
           8 +obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None)); ap.reset(obs, info)
    8      9  r0,objs,surf=ap._parse(obs)
    9     10  print("surf",surf); [print(o) for o in objs.values()]
   10     11  prev=None
diff --git a/test_approach.py b/test_approach.py
index 1370d4d..12b4a46 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -4,10 +4,11 @@ from env_client import make_env
    4      4  from approach import GeneratedApproach
    5      5  from concurrent.futures import ThreadPoolExecutor
    6      6  
           7 +OC=None
    7      8  def run(seed):
    8      9      env = make_env()
    9     10      ap = GeneratedApproach(env.action_space, env.observation_space, {})
   10        -    obs, info = env.reset(seed=seed)
          11 +    obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
   11     12      ap.reset(obs, info)
   12     13      t0 = time.time()
   13     14      for step in range(env.max_steps):
@@ -21,8 +22,10 @@ def run(seed):
   21     22      return seed, False, env.max_steps, time.time() - t0
   22     23  
   23     24  if __name__ == "__main__":
          25 +    global_oc = None
   24     26      s0 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
   25     27      n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
          28 +    globals()["OC"] = int(sys.argv[3]) if len(sys.argv) > 3 else None
   26     29      with ThreadPoolExecutor(8) as ex:
   27     30          res = list(ex.map(run, range(s0, s0 + n)))
   28     31      for r in res:
```

</details>

<a id="C007"></a>
### C007 · Drop spots must not block remaining grasps

Commit `eefe6f42405db31c3ea394ca5cbbaec7cbc7767a`; parents: 6715e9125d9abd81f42816e0fe7961e35a298ce3. Recorded author date: 2026-09-30T12:18:48+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0234](01_timeline.md#E0234): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_eefe6f4_approach.py) · [Exact all-file diff](evidence/diffs/C007_eefe6f4.diff)

[Previous saved controller snapshot](evidence/versions/C006_6715e91_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 588cb11..bea2eb7 100644
--- a/approach.py
+++ b/approach.py
@@ -234,6 +234,11 @@ class GeneratedApproach:
  234    234              bw = blk["w"]
  235    235              reserved.append((self.place_c - bw / 2 - 0.01, self.place_c + bw / 2 + 0.01))
  236    236          cur = held["cx"]
         237 +        future = []
         238 +        for n in self.blockers:
         239 +            if n in others and n not in self.done:
         240 +                gx, gty = self._grasp_x(robot, others[n], others)
         241 +                future.append((gx, gty))
  237    242          best = None
  238    243          for c in np.arange(w / 2 + 0.002, W - w / 2 - 0.002, 0.004):
  239    244              c = float(c)
@@ -250,8 +255,11 @@ class GeneratedApproach:
  250    255              if self._req(rx, parts, obst) > ty + 1e-9:
  251    256                  continue
  252    257              # does dropping here block future block grasp/placement?
         258 +            newob = [(a, b, FLOOR + held["h"])]
         259 +            bparts0 = self._parts(robot)
         260 +            if any(self._req(gx, bparts0, newob) > gty + 1e-9 for gx, gty in future):
         261 +                continue
  253    262              if strict and blk is not None and self.place_c is not None:
  254        -                newob = [(a, b, FLOOR + held["h"])]
  255    263                  bparts = self._parts(robot)
  256    264                  gx = blk["cx"] + self.block_g
  257    265                  gty = blk["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
diff --git a/test_approach.py b/test_approach.py
index 12b4a46..a2eeed9 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -6,6 +6,12 @@ from concurrent.futures import ThreadPoolExecutor
    6      6  
    7      7  OC=None
    8      8  def run(seed):
           9 +    try:
          10 +        return run_(seed)
          11 +    except Exception as e:
          12 +        return seed, None, 0, str(e)[:80]
          13 +
          14 +def run_(seed):
    9     15      env = make_env()
   10     16      ap = GeneratedApproach(env.action_space, env.observation_space, {})
   11     17      obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
@@ -29,6 +35,6 @@ if __name__ == "__main__":
   29     35      with ThreadPoolExecutor(8) as ex:
   30     36          res = list(ex.map(run, range(s0, s0 + n)))
   31     37      for r in res:
   32        -        if not r[1]: print("FAIL", r)
          38 +        if r[1] is False: print("FAIL", r)
   33     39      ok = [r for r in res if r[1]]
   34        -    print(f"success {len(ok)}/{len(res)}, mean steps (succ) {np.mean([r[2] for r in ok]) if ok else 0:.1f}")
          40 +    print("errors", [r[0] for r in res if r[1] is None]); print(f"success {len(ok)}/{len(res)}, mean steps (succ) {np.mean([r[2] for r in ok]) if ok else 0:.1f}")
```

</details>

<a id="C008"></a>
### C008 · Grasp on landing step, release on final carry step; 100/100 at 33.5 steps

Commit `13cd3880c4d235f80f8ea943a39986856cfa83c6`; parents: eefe6f42405db31c3ea394ca5cbbaec7cbc7767a. Recorded author date: 2026-09-30T12:40:53+02:00.

File roles (automatic): policy.

- [E0339](01_timeline.md#E0339): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_13cd388_approach.py) · [Exact all-file diff](evidence/diffs/C008_13cd388.diff)

[Previous saved controller snapshot](evidence/versions/C007_eefe6f4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bea2eb7..646bda0 100644
--- a/approach.py
+++ b/approach.py
@@ -33,6 +33,7 @@ class GeneratedApproach:
   33     33          self.stuck = 0
   34     34          self.escape = 0
   35     35          self.done = set()
          36 +        self.released = None
   36     37  
   37     38      # ------------------------------------------------------------------
   38     39      def _parse(self, s):
@@ -325,13 +326,25 @@ class GeneratedApproach:
  325    326                  parts = self._parts(robot)
  326    327                  obst = self._obst(objs, exclude=(obj["name"],))
  327    328                  act, arrived = self._move(robot, gx, gty, parts, obst, 0.0)
         329 +                self.released = None
  328    330                  if not arrived:
         331 +                    lands = (abs(robot["x"] + float(act[0]) - gx) < 1e-5
         332 +                             and abs(robot["y"] + float(act[1]) - gty) < 3e-5
         333 +                             and abs(float(act[2])) < 1e-4 and abs(float(act[3])) < 1e-4)
         334 +                    if lands:
         335 +                        act[4] = 1.0
         336 +                        self.mode = "grasp"
  329    337                      return act
         338 +                if robot["vac"] < 0.5:
         339 +                    self.mode = "grasp"
         340 +                    return self._act(0, 0, 0, 0, 1.0)
  330    341                  self.mode = "grasp"
  331        -                self.grasp_y = obj["y"]
  332        -                return self._act(0, 0, 0, 0, 1.0)
         342 +                continue
  333    343              if self.mode == "grasp":
  334    344                  obj = objs[self.cur]
         345 +                if robot["vac"] < 0.5:
         346 +                    self.mode = "pick"
         347 +                    continue
  335    348                  self.g_actual = robot["x"] - obj["cx"]
  336    349                  self.depth = robot["y"] - obj["y"]
  337    350                  if self.cur == "target_block":
@@ -365,9 +378,18 @@ class GeneratedApproach:
  365    378                      self.mode = "pick"
  366    379                      return self._act(0, 0, 0, 0, 0.0)
  367    380                  if not arrived:
         381 +                    lands = (abs(robot["x"] + float(act[0]) - tx) < 1e-5
         382 +                             and abs(robot["y"] + float(act[1]) - ty) < 3e-5
         383 +                             and abs(float(act[2])) < 1e-4 and abs(float(act[3])) < 1e-4)
         384 +                    if lands and self.cur != "target_block":
         385 +                        act[4] = 0.0
         386 +                        self.mode = "pick"
         387 +                        self.cur = None
         388 +                        self.last_pose = None
  368    389                      return act
  369    390                  self.mode = "pick"
  370    391                  self.cur = None
         392 +                self.last_pose = None
  371    393                  return self._act(0, 0, 0, 0, 0.0)
  372    394          return self._act(0, 0, 0, 0, robot["vac"])
  373    395  
```

</details>

<a id="C009"></a>
### C009 · Cost-model drop spots incl. elevated drops

Commit `2b642b7729eb1b028fda64de53090686da7f6a6b`; parents: 13cd3880c4d235f80f8ea943a39986856cfa83c6. Recorded author date: 2026-09-30T12:47:18+02:00.

File roles (automatic): policy.

- [E0356](01_timeline.md#E0356): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_2b642b7_approach.py) · [Exact all-file diff](evidence/diffs/C009_2b642b7.diff)

[Previous saved controller snapshot](evidence/versions/C008_13cd388_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 646bda0..8864fb7 100644
--- a/approach.py
+++ b/approach.py
@@ -219,64 +219,83 @@ class GeneratedApproach:
  219    219                  res.append(n)
  220    220          return res
  221    221  
  222        -    def _drop_spot(self, robot, objs, held, g, next_x, strict=True):
  223        -        """Choose drop center for obstruction held with offset g (robot_x - center)."""
         222 +    def _steps(self, x0, y0, x1, y1, parts, obst):
         223 +        peak = max(y0, y1, self._req_range(x0, x1, parts, obst))
         224 +        peak = min(peak, H - 0.1)
         225 +        return max(abs(x1 - x0), (peak - y0) + (peak - y1)) / MAXD
         226 +
         227 +    def _drop_spot(self, robot, objs, held, g, next_name, strict=True):
         228 +        """Choose (object center x, object bottom y) drop pose for held obstruction."""
  224    229          lo, hi = self._xlim(robot)
  225    230          w = held["w"]
  226    231          others = {n: o for n, o in objs.items() if n != held["name"]}
  227    232          obst = self._obst(others)
  228    233          depth = robot["y"] - held["y"]
  229        -        ty_off = FLOOR + PLACE_GAP
  230    234          parts = self._parts(robot, held, -g - w / 2, depth)
  231        -        # reserved zones: block placement and robot columns for future block ops
  232    235          blk = objs.get("target_block")
  233    236          reserved = []
  234    237          if self.place_c is not None and blk is not None:
  235    238              bw = blk["w"]
  236    239              reserved.append((self.place_c - bw / 2 - 0.01, self.place_c + bw / 2 + 0.01))
  237        -        cur = held["cx"]
  238    240          future = []
  239    241          for n in self.blockers:
  240    242              if n in others and n not in self.done:
  241    243                  gx, gty = self._grasp_x(robot, others[n], others)
  242    244                  future.append((gx, gty))
         245 +        # next pick pose
         246 +        nxt = others.get(next_name)
         247 +        if nxt is not None:
         248 +            pref = self.block_g if next_name == "target_block" else 0.0
         249 +            ngx, ngty = self._grasp_x(robot, nxt, others, pref)
         250 +        bparts0 = self._parts(robot)
         251 +        if blk is not None:
         252 +            bgx = blk["cx"] + self.block_g
         253 +            bgty = blk["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
         254 +            bdepth = robot["maxarm"] + robot["gw"] + blk["h"]
         255 +            pparts = self._parts(robot, blk, -self.block_g - blk["w"] / 2, bdepth)
         256 +            px = self.place_c + self.block_g
         257 +            pty = FLOOR + PLACE_GAP + bdepth
         258 +        levels = [FLOOR + PLACE_GAP + 0.04 * k for k in range(0, 9)]
         259 +        sep = 0.01 if strict else 0.002
  243    260          best = None
  244        -        for c in np.arange(w / 2 + 0.002, W - w / 2 - 0.002, 0.004):
         261 +        for c in np.arange(w / 2 + 0.002, W - w / 2 - 0.002, 0.005):
  245    262              c = float(c)
  246    263              rx = c + g
  247    264              if rx < lo or rx > hi:
  248    265                  continue
  249    266              a, b = c - w / 2, c + w / 2
  250        -            sep = 0.01 if strict else 0.002
  251    267              if any(a < o1 + sep and b > o0 - sep for (o0, o1, _) in obst):
  252    268                  continue
  253    269              if any(a < r1 and b > r0 for (r0, r1) in reserved):
  254    270                  continue
  255        -            ty = ty_off + depth
  256        -            if self._req(rx, parts, obst) > ty + 1e-9:
  257        -                continue
  258        -            # does dropping here block future block grasp/placement?
  259        -            newob = [(a, b, FLOOR + held["h"])]
  260        -            bparts0 = self._parts(robot)
  261        -            if any(self._req(gx, bparts0, newob) > gty + 1e-9 for gx, gty in future):
  262        -                continue
  263        -            if strict and blk is not None and self.place_c is not None:
  264        -                bparts = self._parts(robot)
  265        -                gx = blk["cx"] + self.block_g
  266        -                gty = blk["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
  267        -                if self._req(gx, bparts, newob) > gty + 1e-9:
         271 +            req = self._req(rx, parts, obst)
         272 +            for bot in levels:
         273 +                ty = bot + depth
         274 +                if ty > H - robot["r"] - 1e-3:
         275 +                    break
         276 +                if req > ty + 1e-9:
  268    277                      continue
  269        -                bdepth = robot["maxarm"] + robot["gw"] + blk["h"]
  270        -                pparts = self._parts(robot, blk, -self.block_g - blk["w"] / 2, bdepth)
  271        -                pty = FLOOR + PLACE_GAP + bdepth
  272        -                if self._req(self.place_c + self.block_g, pparts, newob) > pty + 1e-9:
         278 +                newob = [(a, b, bot + held["h"])]
         279 +                if any(self._req(gx, bparts0, newob) > gty + 1e-9 for gx, gty in future):
  273    280                      continue
  274        -            cost = abs(c - cur) + abs(c + g - next_x) + 1e-3 * abs(c - cur)
  275        -            if best is None or cost < best[0]:
  276        -                best = (cost, c)
         281 +                if blk is not None and self.place_c is not None:
         282 +                    if self._req(bgx, bparts0, newob) > bgty + 1e-9:
         283 +                        continue
         284 +                    if self._req(px, pparts, newob) > pty + 1e-9:
         285 +                        continue
         286 +                cost = self._steps(robot["x"], robot["y"], rx, ty, parts, obst)
         287 +                obst2 = obst + newob
         288 +                if nxt is not None:
         289 +                    obst_n = [o for o in obst2 if not (o[0] == nxt["x"] and o[2] == nxt["top"])]
         290 +                    cost += self._steps(rx, ty, ngx, ngty, bparts0, obst_n)
         291 +                    if next_name == "target_block":
         292 +                        cost += self._steps(ngx, ngty, px, pty, pparts, obst_n)
         293 +                cost += 1e-3 * abs(c - held["cx"])
         294 +                if best is None or cost < best[0]:
         295 +                    best = (cost, c, bot)
  277    296          if best is None:
  278    297              return None
  279        -        return best[1]
         298 +        return best[1], best[2]
  280    299  
  281    300      def _air_spot(self, robot, objs, held, g):
  282    301          lo, hi = self._xlim(robot)
@@ -354,11 +373,10 @@ class GeneratedApproach:
  354    373                      d = self._drop_spot(robot, objs, obj, self.g_actual, nxt)
  355    374                      if d is None:
  356    375                          d = self._drop_spot(robot, objs, obj, self.g_actual, nxt, strict=False)
  357        -                    self.drop_y = None
  358    376                      if d is None:
  359        -                        d = self._air_spot(robot, objs, obj, self.g_actual)
  360        -                        self.drop_y = H - robot["r"] - 1e-3
  361        -                    self.drop = d
         377 +                        d = (self._air_spot(robot, objs, obj, self.g_actual),
         378 +                             H - robot["r"] - 1e-3 - self.depth)
         379 +                    self.drop, self.drop_bot = d
  362    380                  self.mode = "carry"
  363    381                  continue
  364    382              if self.mode == "carry":
@@ -370,8 +388,8 @@ class GeneratedApproach:
  370    388                  obst = self._obst(objs, exclude=(obj["name"],))
  371    389                  tx = self.drop + (robot["x"] - obj["cx"])
  372    390                  ty = robot["y"] - obj["y"] + FLOOR + PLACE_GAP
  373        -                if self.cur != "target_block" and getattr(self, "drop_y", None) is not None:
  374        -                    ty = self.drop_y
         391 +                if self.cur != "target_block":
         392 +                    ty = robot["y"] - obj["y"] + self.drop_bot
  375    393                  act, arrived = self._move(robot, tx, ty, parts, obst, 1.0)
  376    394                  # detect failed grasp: object not following
  377    395                  if abs(robot["y"] - obj["y"] - self.depth) > 5e-3:
@@ -432,9 +450,8 @@ class GeneratedApproach:
  432    450          return n
  433    451  
  434    452      def _peek_next(self, robot, objs, exclude):
  435        -        done = getattr(self, "done", set())
  436        -        rem = [n for n in self.blockers if n in objs and n not in done and n != exclude]
         453 +        rem = [n for n in self.blockers if n in objs and n not in self.done and n != exclude]
  437    454          if rem:
  438    455              rem.sort(key=lambda n: abs(objs[n]["cx"] - robot["x"]))
  439        -            return objs[rem[0]]["cx"]
  440        -        return objs["target_block"]["cx"] + self.block_g
         456 +            return rem[0]
         457 +        return "target_block"
```

</details>

<a id="C010"></a>
### C010 · Always include block carry cost in drop choice

Commit `0b90e154b04212e9848f8d1bff0429fd9bce1982`; parents: 2b642b7729eb1b028fda64de53090686da7f6a6b. Recorded author date: 2026-09-30T12:48:38+02:00.

File roles (automatic): policy.

- [E0367](01_timeline.md#E0367): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_0b90e15_approach.py) · [Exact all-file diff](evidence/diffs/C010_0b90e15.diff)

[Previous saved controller snapshot](evidence/versions/C009_2b642b7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8864fb7..b7ff0dd 100644
--- a/approach.py
+++ b/approach.py
@@ -288,8 +288,9 @@ class GeneratedApproach:
  288    288                  if nxt is not None:
  289    289                      obst_n = [o for o in obst2 if not (o[0] == nxt["x"] and o[2] == nxt["top"])]
  290    290                      cost += self._steps(rx, ty, ngx, ngty, bparts0, obst_n)
  291        -                    if next_name == "target_block":
  292        -                        cost += self._steps(ngx, ngty, px, pty, pparts, obst_n)
         291 +                if blk is not None and self.place_c is not None:
         292 +                    obst_b = [o for o in obst2 if not (o[0] == blk["x"] and o[2] == blk["top"])]
         293 +                    cost += self._steps(bgx, bgty, px, pty, pparts, obst_b)
  293    294                  cost += 1e-3 * abs(c - held["cx"])
  294    295                  if best is None or cost < best[0]:
  295    296                      best = (cost, c, bot)
```

</details>

<a id="C011"></a>
### C011 · Plan search over removal orders and block staging with cost model

Commit `93444da744352b04623ac1724e5fbe3457f81c4a`; parents: 0b90e154b04212e9848f8d1bff0429fd9bce1982. Recorded author date: 2026-09-30T12:51:48+02:00.

File roles (automatic): policy.

- [E0396](01_timeline.md#E0396): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_93444da_approach.py) · [Exact all-file diff](evidence/diffs/C011_93444da.diff)

[Previous saved controller snapshot](evidence/versions/C010_0b90e15_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b7ff0dd..8943dfd 100644
--- a/approach.py
+++ b/approach.py
@@ -224,7 +224,7 @@ class GeneratedApproach:
  224    224          peak = min(peak, H - 0.1)
  225    225          return max(abs(x1 - x0), (peak - y0) + (peak - y1)) / MAXD
  226    226  
  227        -    def _drop_spot(self, robot, objs, held, g, next_name, strict=True):
         227 +    def _drop_spot(self, robot, objs, held, g, next_name, remaining=(), strict=True, staging=False):
  228    228          """Choose (object center x, object bottom y) drop pose for held obstruction."""
  229    229          lo, hi = self._xlim(robot)
  230    230          w = held["w"]
@@ -238,10 +238,18 @@ class GeneratedApproach:
  238    238              bw = blk["w"]
  239    239              reserved.append((self.place_c - bw / 2 - 0.01, self.place_c + bw / 2 + 0.01))
  240    240          future = []
  241        -        for n in self.blockers:
  242        -            if n in others and n not in self.done:
         241 +        for n in remaining:
         242 +            if n in others:
  243    243                  gx, gty = self._grasp_x(robot, others[n], others)
  244    244                  future.append((gx, gty))
         245 +        if staging:
         246 +            blk = None
         247 +            bw = held["w"]
         248 +            reserved = [(self.place_c - bw / 2 - 0.01, self.place_c + bw / 2 + 0.01)]
         249 +            pdepth = robot["maxarm"] + robot["gw"] + held["h"]
         250 +            spparts = self._parts(robot, held, -self.block_g - bw / 2, pdepth)
         251 +            spx = self.place_c + self.block_g
         252 +            spty = FLOOR + PLACE_GAP + pdepth
  245    253          # next pick pose
  246    254          nxt = others.get(next_name)
  247    255          if nxt is not None:
@@ -291,6 +299,13 @@ class GeneratedApproach:
  291    299                  if blk is not None and self.place_c is not None:
  292    300                      obst_b = [o for o in obst2 if not (o[0] == blk["x"] and o[2] == blk["top"])]
  293    301                      cost += self._steps(bgx, bgty, px, pty, pparts, obst_b)
         302 +                if staging:
         303 +                    # later: re-grasp block at (c + block_g) and carry to placement
         304 +                    sgx = c + self.block_g
         305 +                    sgty = bot + held["h"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
         306 +                    if sgx < lo or sgx > hi:
         307 +                        continue
         308 +                    cost += self._steps(sgx, sgty, spx, spty, spparts, obst2)
  294    309                  cost += 1e-3 * abs(c - held["cx"])
  295    310                  if best is None or cost < best[0]:
  296    311                      best = (cost, c, bot)
@@ -339,9 +354,11 @@ class GeneratedApproach:
  339    354          for _ in range(6):
  340    355              if self.mode == "pick":
  341    356                  if self.cur is None:
  342        -                    self.cur = self._next_target(robot, objs)
         357 +                    self.kind, self.cur = self._next_task(robot, objs)
  343    358                  obj = objs[self.cur]
  344    359                  prefer = self.block_g if self.cur == "target_block" else 0.0
         360 +                if self.cur == "target_block" and self.kind == "stage":
         361 +                    prefer = self.stage_g
  345    362                  gx, gty = self._grasp_x(robot, obj, objs, prefer)
  346    363                  parts = self._parts(robot)
  347    364                  obst = self._obst(objs, exclude=(obj["name"],))
@@ -367,13 +384,16 @@ class GeneratedApproach:
  367    384                      continue
  368    385                  self.g_actual = robot["x"] - obj["cx"]
  369    386                  self.depth = robot["y"] - obj["y"]
  370        -                if self.cur == "target_block":
         387 +                if self.kind == "place":
  371    388                      self.drop = self.place_c
         389 +                    self.drop_bot = FLOOR + PLACE_GAP
  372    390                  else:
  373        -                    nxt = self._peek_next(robot, objs, exclude=self.cur)
  374        -                    d = self._drop_spot(robot, objs, obj, self.g_actual, nxt)
         391 +                    rem = [n for n in self.remaining if n != self.cur]
         392 +                    nxt = rem[0] if rem else "target_block"
         393 +                    stg = self.kind == "stage"
         394 +                    d = self._drop_spot(robot, objs, obj, self.g_actual, nxt, rem, staging=stg)
  375    395                      if d is None:
  376        -                        d = self._drop_spot(robot, objs, obj, self.g_actual, nxt, strict=False)
         396 +                        d = self._drop_spot(robot, objs, obj, self.g_actual, nxt, rem, strict=False, staging=stg)
  377    397                      if d is None:
  378    398                          d = (self._air_spot(robot, objs, obj, self.g_actual),
  379    399                               H - robot["r"] - 1e-3 - self.depth)
@@ -388,9 +408,7 @@ class GeneratedApproach:
  388    408                  parts = self._parts(robot, obj, obj["x"] - robot["x"], robot["y"] - obj["y"])
  389    409                  obst = self._obst(objs, exclude=(obj["name"],))
  390    410                  tx = self.drop + (robot["x"] - obj["cx"])
  391        -                ty = robot["y"] - obj["y"] + FLOOR + PLACE_GAP
  392        -                if self.cur != "target_block":
  393        -                    ty = robot["y"] - obj["y"] + self.drop_bot
         411 +                ty = robot["y"] - obj["y"] + self.drop_bot
  394    412                  act, arrived = self._move(robot, tx, ty, parts, obst, 1.0)
  395    413                  # detect failed grasp: object not following
  396    414                  if abs(robot["y"] - obj["y"] - self.depth) > 5e-3:
@@ -400,7 +418,7 @@ class GeneratedApproach:
  400    418                      lands = (abs(robot["x"] + float(act[0]) - tx) < 1e-5
  401    419                               and abs(robot["y"] + float(act[1]) - ty) < 3e-5
  402    420                               and abs(float(act[2])) < 1e-4 and abs(float(act[3])) < 1e-4)
  403        -                    if lands and self.cur != "target_block":
         421 +                    if lands and self.kind != "place":
  404    422                          act[4] = 0.0
  405    423                          self.mode = "pick"
  406    424                          self.cur = None
@@ -412,47 +430,107 @@ class GeneratedApproach:
  412    430                  return self._act(0, 0, 0, 0, 0.0)
  413    431          return self._act(0, 0, 0, 0, robot["vac"])
  414    432  
  415        -    def _remaining_blockers(self, objs):
  416        -        return [n for n in self.blockers if n in objs and self._still_blocks(objs[n], objs)]
  417        -
  418        -    def _still_blocks(self, o, objs):
         433 +    def _blockers_now(self, robot, objs):
  419    434          blk = objs["target_block"]
  420    435          bw = blk["w"]
  421        -        c = self.place_c
  422        -        if o["x"] < c + bw / 2 + 0.003 and o["x"] + o["w"] > c - bw / 2 - 0.003:
  423        -            return True
  424        -        return False if o.get("_moved") else True
         436 +        c, g = self.place_c, self.block_g
         437 +        depth = robot["maxarm"] + robot["gw"] + blk["h"]
         438 +        parts = self._parts(robot, blk, -g - bw / 2, depth)
         439 +        ty = FLOOR + PLACE_GAP + depth
         440 +        res = []
         441 +        for n, o in objs.items():
         442 +            if n == "target_block":
         443 +                continue
         444 +            if o["x"] < c + bw / 2 + 0.003 and o["x"] + o["w"] > c - bw / 2 - 0.003:
         445 +                res.append(n)
         446 +            elif self._req(c + g, parts, [(o["x"], o["x"] + o["w"], o["top"])]) > ty + 1e-6:
         447 +                res.append(n)
         448 +        return res
  425    449  
  426        -    def _next_target(self, robot, objs):
  427        -        rem = [n for n in self.blockers if n in objs and n not in self.done]
  428        -        goals = rem if rem else ["target_block"]
  429        -        goals = sorted(goals, key=lambda n: abs(objs[n]["cx"] - robot["x"]))
  430        -        infeasible = []
  431        -        for n in goals:
  432        -            pref = self.block_g if n == "target_block" else 0.0
  433        -            ok, gx, ty = self._grasp_ok(robot, objs[n], objs, pref)
  434        -            if ok:
  435        -                if n != "target_block":
  436        -                    self.done.add(n)
  437        -                return n
  438        -            infeasible.append((n, gx, ty))
  439        -        # nothing directly graspable: move an obstacle that blocks a goal's grasp
  440        -        for n, gx, ty in infeasible:
  441        -            for v in self._violators(robot, objs[n], objs, gx, ty):
  442        -                if v == "target_block":
  443        -                    continue
  444        -                ok, _, _ = self._grasp_ok(robot, objs[v], objs)
  445        -                if ok:
  446        -                    self.done.add(v)
  447        -                    return v
  448        -        n = goals[0]
  449        -        if n != "target_block":
  450        -            self.done.add(n)
  451        -        return n
         450 +    def _simulate(self, robot, objs, tasks):
         451 +        """Estimate step cost of executing tasks [(kind, name)] from current state."""
         452 +        objs = {n: dict(o) for n, o in objs.items()}
         453 +        x, y = robot["x"], robot["y"]
         454 +        cost = 0.0
         455 +        first_info = None
         456 +        names = [n for k, n in tasks if k == "remove"]
         457 +        for i, (kind, name) in enumerate(tasks):
         458 +            obj = objs[name]
         459 +            if name == "target_block":
         460 +                prefer = self.block_g
         461 +            else:
         462 +                prefer = 0.0
         463 +            ok, gx, gty = self._grasp_ok(robot, obj, objs, prefer)
         464 +            if not ok:
         465 +                cost += 1000.0
         466 +            cost += self._steps(x, y, gx, gty, self._parts(robot), self._obst(objs, exclude=(name,)))
         467 +            g = gx - obj["cx"]
         468 +            depth = gty - obj["y"]
         469 +            rsim = dict(robot)
         470 +            rsim["x"], rsim["y"] = gx, gty
         471 +            if kind == "place":
         472 +                c, bot = self.place_c, FLOOR + PLACE_GAP
         473 +            else:
         474 +                rem = names[names.index(name) + 1:] if (kind == "remove" and name in names) else list(names)
         475 +                nxt = rem[0] if rem else "target_block"
         476 +                d = self._drop_spot(rsim, objs, obj, g, nxt, rem, staging=(kind == "stage"))
         477 +                if d is None:
         478 +                    d = self._drop_spot(rsim, objs, obj, g, nxt, rem, strict=False, staging=(kind == "stage"))
         479 +                if d is None:
         480 +                    return cost + 5000.0
         481 +                c, bot = d
         482 +            tx, ty = c + g, bot + depth
         483 +            parts = self._parts(robot, obj, obj["x"] - gx, depth)
         484 +            cost += self._steps(gx, gty, tx, ty, parts, self._obst(objs, exclude=(name,)))
         485 +            obj["x"] = c - obj["w"] / 2
         486 +            obj["cx"] = c
         487 +            obj["y"] = bot
         488 +            obj["top"] = bot + obj["h"]
         489 +            x, y = tx, ty
         490 +            cost += 1.0
         491 +        return cost
  452    492  
  453        -    def _peek_next(self, robot, objs, exclude):
  454        -        rem = [n for n in self.blockers if n in objs and n not in self.done and n != exclude]
  455        -        if rem:
  456        -            rem.sort(key=lambda n: abs(objs[n]["cx"] - robot["x"]))
  457        -            return rem[0]
  458        -        return "target_block"
         493 +    def _next_task(self, robot, objs):
         494 +        import itertools
         495 +        blockers = self._blockers_now(robot, objs)
         496 +        if not blockers:
         497 +            self.remaining = []
         498 +            return ("place", "target_block")
         499 +        if len(blockers) <= 3:
         500 +            orders = list(itertools.permutations(blockers))
         501 +        else:
         502 +            orders = [tuple(sorted(blockers, key=lambda n: abs(objs[n]["cx"] - robot["x"]))),
         503 +                      tuple(sorted(blockers, key=lambda n: objs[n]["cx"])),
         504 +                      tuple(sorted(blockers, key=lambda n: -objs[n]["cx"]))]
         505 +        best = None
         506 +        for order in orders:
         507 +            base = [("remove", n) for n in order] + [("place", "target_block")]
         508 +            for stage in (False, True):
         509 +                tasks = ([("stage", "target_block")] if stage else []) + base
         510 +                c = self._simulate(robot, objs, tasks)
         511 +                if best is None or c < best[0] - 1e-9:
         512 +                    best = (c, tasks, order)
         513 +        cost, tasks, order = best
         514 +        self.remaining = list(order)
         515 +        self.stage_g = self.block_g
         516 +        if cost >= 1000.0:
         517 +            # some grasp infeasible: clear an obstacle blocking a grasp
         518 +            for n in list(order) + ["target_block"]:
         519 +                pref = self.block_g if n == "target_block" else 0.0
         520 +                ok, gx, ty = self._grasp_ok(robot, objs[n], objs, pref)
         521 +                if ok:
         522 +                    if n in order:
         523 +                        self.remaining = [m for m in order if m != n]
         524 +                        return ("remove", n)
         525 +                    continue
         526 +                for v in self._violators(robot, objs[n], objs, gx, ty):
         527 +                    if v == "target_block":
         528 +                        continue
         529 +                    ok2, _, _ = self._grasp_ok(robot, objs[v], objs)
         530 +                    if ok2:
         531 +                        self.remaining = list(order)
         532 +                        return ("remove", v)
         533 +        kind, name = tasks[0]
         534 +        if kind == "remove":
         535 +            self.remaining = [m for m in order if m != name]
         536 +        return (kind, name)
```

</details>

<a id="C012"></a>
### C012 · Keep pick target as obstacle with tiny margin (fix diagonal collisions)

Commit `576514bdee11d070ede0822d52548cc4025ddd34`; parents: 93444da744352b04623ac1724e5fbe3457f81c4a. Recorded author date: 2026-09-30T13:00:52+02:00.

File roles (automatic): policy.

- [E0453](01_timeline.md#E0453): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_576514b_approach.py) · [Exact all-file diff](evidence/diffs/C012_576514b.diff)

[Previous saved controller snapshot](evidence/versions/C011_93444da_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8943dfd..ed09c2b 100644
--- a/approach.py
+++ b/approach.py
@@ -80,9 +80,9 @@ class GeneratedApproach:
   80     80          for lo, hi, d in parts:
   81     81              a, b = x + lo, x + hi
   82     82              req = max(req, FLOOR + d)  # floor
   83        -            for (o0, o1, top) in obst:
   84        -                if a < o1 + XMARGIN and b > o0 - XMARGIN:
   85        -                    req = max(req, top + d + MARGIN)
          83 +            for ob in obst:
          84 +                if a < ob[1] + XMARGIN and b > ob[0] - XMARGIN:
          85 +                    req = max(req, ob[2] + d + (ob[3] if len(ob) > 3 else MARGIN))
   86     86          return req
   87     87  
   88     88      def _req_range(self, x0, x1, parts, obst):
@@ -91,14 +91,21 @@ class GeneratedApproach:
   91     91          for plo, phi, d in parts:
   92     92              a, b = lo + plo, hi + phi
   93     93              req = max(req, FLOOR + d)
   94        -            for (o0, o1, top) in obst:
   95        -                if a < o1 + XMARGIN and b > o0 - XMARGIN:
   96        -                    req = max(req, top + d + MARGIN)
          94 +            for ob in obst:
          95 +                if a < ob[1] + XMARGIN and b > ob[0] - XMARGIN:
          96 +                    req = max(req, ob[2] + d + (ob[3] if len(ob) > 3 else MARGIN))
   97     97          return req
   98     98  
   99     99      def _obst(self, objs, exclude=()):
  100    100          return [(o["x"], o["x"] + o["w"], o["top"]) for n, o in objs.items() if n not in exclude]
  101    101  
         102 +    def _obst_pick(self, objs, name):
         103 +        """Obstacles when approaching object `name` for a grasp (target kept, tiny margin)."""
         104 +        res = self._obst(objs, exclude=(name,))
         105 +        o = objs[name]
         106 +        res.append((o["x"], o["x"] + o["w"], o["top"], GRASP_GAP * 0.5))
         107 +        return res
         108 +
  102    109      def _xlim(self, robot):
  103    110          return robot["r"] + 1e-3, W - robot["r"] - 1e-3
  104    111  
@@ -295,6 +302,7 @@ class GeneratedApproach:
  295    302                  obst2 = obst + newob
  296    303                  if nxt is not None:
  297    304                      obst_n = [o for o in obst2 if not (o[0] == nxt["x"] and o[2] == nxt["top"])]
         305 +                    obst_n.append((nxt["x"], nxt["x"] + nxt["w"], nxt["top"], GRASP_GAP * 0.5))
  298    306                      cost += self._steps(rx, ty, ngx, ngty, bparts0, obst_n)
  299    307                  if blk is not None and self.place_c is not None:
  300    308                      obst_b = [o for o in obst2 if not (o[0] == blk["x"] and o[2] == blk["top"])]
@@ -361,7 +369,7 @@ class GeneratedApproach:
  361    369                      prefer = self.stage_g
  362    370                  gx, gty = self._grasp_x(robot, obj, objs, prefer)
  363    371                  parts = self._parts(robot)
  364        -                obst = self._obst(objs, exclude=(obj["name"],))
         372 +                obst = self._obst_pick(objs, obj["name"])
  365    373                  act, arrived = self._move(robot, gx, gty, parts, obst, 0.0)
  366    374                  self.released = None
  367    375                  if not arrived:
@@ -463,7 +471,7 @@ class GeneratedApproach:
  463    471              ok, gx, gty = self._grasp_ok(robot, obj, objs, prefer)
  464    472              if not ok:
  465    473                  cost += 1000.0
  466        -            cost += self._steps(x, y, gx, gty, self._parts(robot), self._obst(objs, exclude=(name,)))
         474 +            cost += self._steps(x, y, gx, gty, self._parts(robot), self._obst_pick(objs, name))
  467    475              g = gx - obj["cx"]
  468    476              depth = gty - obj["y"]
  469    477              rsim = dict(robot)
```

</details>

<a id="C013"></a>
### C013 · Tilted-arm grasps for objects beyond vertical reach near walls

Commit `f86a47c281a710c2caf40d12354deb8bb1eb71b6`; parents: 576514bdee11d070ede0822d52548cc4025ddd34. Recorded author date: 2026-09-30T13:12:36+02:00.

File roles (automatic): policy.

- [E0501](01_timeline.md#E0501): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_f86a47c_approach.py) · [Exact all-file diff](evidence/diffs/C013_f86a47c.diff)

[Previous saved controller snapshot](evidence/versions/C012_576514b_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ed09c2b..6073f57 100644
--- a/approach.py
+++ b/approach.py
@@ -34,6 +34,9 @@ class GeneratedApproach:
   34     34          self.escape = 0
   35     35          self.done = set()
   36     36          self.released = None
          37 +        self.fails = {}
          38 +        self.carry_th = DOWN
          39 +        self._last_tilt = 0.0
   37     40  
   38     41      # ------------------------------------------------------------------
   39     42      def _parse(self, s):
@@ -64,16 +67,62 @@ class GeneratedApproach:
   64     67          return a.astype(np.float32)
   65     68  
   66     69      # ---------------- geometry ----------------
   67        -    def _parts(self, robot, held=None, held_off=None, held_depth=None):
          70 +    def _gripper_geom(self, robot, a):
          71 +        """Gripper corners relative to robot center for tilt a (theta = DOWN + a)."""
          72 +        arm, gw, gh = robot["maxarm"], robot["gw"], robot["gh"]
          73 +        d = (np.sin(a), -np.cos(a))
          74 +        p = (np.cos(a), np.sin(a))
          75 +        L = arm + gw / 2
          76 +        cs = []
          77 +        for sd in (-1, 1):
          78 +            for sp in (-1, 1):
          79 +                cs.append((L * d[0] + sd * gw / 2 * d[0] + sp * gh / 2 * p[0],
          80 +                           L * d[1] + sd * gw / 2 * d[1] + sp * gh / 2 * p[1]))
          81 +        return cs, d, p
          82 +
          83 +    def _parts(self, robot, held=None, held_off=None, held_depth=None, tilt=0.0):
   68     84          """Footprint parts relative to robot x: (lo, hi, depth below robot y)."""
   69     85          arm = robot["maxarm"]
   70        -        parts = [(-robot["r"], robot["r"], robot["r"]),
   71        -                 (-robot["gh"] / 2, robot["gh"] / 2, arm + robot["gw"])]
          86 +        if abs(tilt) < 1e-6:
          87 +            parts = [(-robot["r"], robot["r"], robot["r"]),
          88 +                     (-robot["gh"] / 2, robot["gh"] / 2, arm + robot["gw"])]
          89 +        else:
          90 +            cs, d, p = self._gripper_geom(robot, tilt)
          91 +            xs = [c[0] for c in cs]
          92 +            ys = [c[1] for c in cs]
          93 +            ex, ey = arm * d[0], arm * d[1]
          94 +            parts = [(-robot["r"], robot["r"], robot["r"]),
          95 +                     (min(xs), max(xs), -min(ys)),
          96 +                     (min(0.0, ex) - 0.005, max(0.0, ex) + 0.005, -ey)]
   72     97          if held is not None:
   73     98              # held_off: object left edge relative to robot x; held_depth: robot y - object bottom
   74     99              parts.append((held_off, held_off + held["w"], held_depth))
   75    100          return parts
   76    101  
         102 +    def _contact(self, robot, rx, obj, a):
         103 +        """Robot y at which gripper (tilt a) at robot x rx touches obj top; None if no overlap."""
         104 +        if abs(a) < 1e-6:
         105 +            if min(rx + robot["gh"] / 2, obj["x"] + obj["w"]) - max(rx - robot["gh"] / 2, obj["x"]) < 0.012:
         106 +                return None
         107 +            return obj["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
         108 +        arm, gw, gh = robot["maxarm"], robot["gw"], robot["gh"]
         109 +        d = (np.sin(a), -np.cos(a))
         110 +        p = (np.cos(a), np.sin(a))
         111 +        Lb = arm + gw
         112 +        p1 = (Lb * d[0] - gh / 2 * p[0], Lb * d[1] - gh / 2 * p[1])
         113 +        p2 = (Lb * d[0] + gh / 2 * p[0], Lb * d[1] + gh / 2 * p[1])
         114 +        if p1[0] > p2[0]:
         115 +            p1, p2 = p2, p1
         116 +        o0, o1 = obj["x"] - rx, obj["x"] + obj["w"] - rx
         117 +        lo_, hi_ = max(o0, p1[0]), min(o1, p2[0])
         118 +        if hi_ - lo_ < 0.012:
         119 +            return None
         120 +        def rel_y(x):
         121 +            t = (x - p1[0]) / (p2[0] - p1[0])
         122 +            return p1[1] + t * (p2[1] - p1[1])
         123 +        m = min(rel_y(lo_), rel_y(hi_))
         124 +        return obj["top"] - m + GRASP_GAP
         125 +
   77    126      def _req(self, x, parts, obst):
   78    127          """Min robot y at horizontal position x so no part collides."""
   79    128          req = 0.0
@@ -110,11 +159,11 @@ class GeneratedApproach:
  110    159          return robot["r"] + 1e-3, W - robot["r"] - 1e-3
  111    160  
  112    161      # ---------------- motion ----------------
  113        -    def _move(self, robot, tx, ty, parts, obst, vac):
         162 +    def _move(self, robot, tx, ty, parts, obst, vac, th=DOWN):
  114    163          """One step toward (tx, ty) staying above clearance profile. Returns (action, arrived)."""
  115    164          x, y = robot["x"], robot["y"]
  116    165          ymax = H - robot["r"] - 1e-3
  117        -        dth = float(np.clip(DOWN - robot["th"], -0.19, 0.19))
         166 +        dth = float(np.clip(th - robot["th"], -0.19, 0.19))
  118    167          darm = float(np.clip(robot["maxarm"] - robot["arm"], -0.1, 0.1))
  119    168          posture_ok = abs(dth) < 1e-4 and abs(darm) < 1e-4
  120    169          if abs(tx - x) < 1e-5 and abs(ty - y) < 3e-5 and posture_ok:
@@ -157,7 +206,8 @@ class GeneratedApproach:
  157    206          best = None
  158    207          cands = list(np.linspace(cmin, cmax, max(2, int((cmax - cmin) / 0.002) + 1)))
  159    208          cands.append(center)
  160        -        gmax = max(0.0, bw / 2 - 0.004)
         209 +        gvert = max(0.0, bw / 2 - 0.004)
         210 +        gmax = bw / 2 + 0.05
  161    211          place_depth = None
  162    212          for c in cands:
  163    213              c = float(np.clip(c, cmin, cmax))
@@ -180,7 +230,7 @@ class GeneratedApproach:
  180    230                      continue
  181    231                  if self._req(c + g, parts, [(o["x"], o["x"] + o["w"], o["top"])]) > ty + 1e-6:
  182    232                      blockers.add(o["name"])
  183        -            cost = (len(blockers), abs(g) > 1e-6, abs(g), abs(c - center))
         233 +            cost = (len(blockers), abs(g) > gvert + 1e-9, abs(g) > 1e-6, abs(g), abs(c - center))
  184    234              if best is None or cost < best[0]:
  185    235                  best = (cost, c, g, blockers)
  186    236          if best is None:
@@ -189,27 +239,36 @@ class GeneratedApproach:
  189    239          return best[1], best[2], best[3]
  190    240  
  191    241      def _grasp_x(self, robot, obj, objs, prefer_g=0.0):
  192        -        """Choose robot x to grasp obj (reachable, collision free)."""
         242 +        """Choose robot x (and tilt) to grasp obj. Sets self._last_tilt, self._last_grasp_ok."""
  193    243          lo, hi = self._xlim(robot)
  194        -        parts = self._parts(robot)
  195    244          obst = self._obst(objs, exclude=(obj["name"],))
  196        -        ty = obj["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
  197    245          gmax = max(0.0, obj["w"] / 2 - 0.004)
  198    246          best = None
  199        -        for g in np.linspace(-gmax, gmax, 41).tolist() + [prefer_g, 0.0]:
  200        -            if abs(g) > gmax + 1e-9:
  201        -                continue
  202        -            x = obj["cx"] + g
  203        -            if x < lo or x > hi:
  204        -                continue
  205        -            ok = self._req(x, parts, obst) <= ty + 1e-9
  206        -            cost = (not ok, abs(g - prefer_g))
  207        -            if best is None or cost < best[0]:
  208        -                best = (cost, x)
         247 +        cands = [obj["cx"] + g for g in np.linspace(-gmax, gmax, 41).tolist() + [prefer_g, 0.0]]
         248 +        cands = [x for x in cands if lo <= x <= hi]
         249 +        tilts = [0.0]
         250 +        if not cands:
         251 +            cands = [float(np.clip(obj["cx"], lo, hi))]
         252 +            sgn = 1.0 if obj["cx"] > cands[0] else -1.0
         253 +            tilts = [sgn * k * 0.05 for k in range(1, 19)]
         254 +        for x in cands:
         255 +            for a in tilts:
         256 +                ty = self._contact(robot, x, obj, a)
         257 +                if ty is None:
         258 +                    continue
         259 +                parts = self._parts(robot, tilt=a)
         260 +                ok = self._req(x, parts, obst) <= ty + 1e-9
         261 +                cost = (not ok, abs(a), abs(x - obj["cx"] - prefer_g))
         262 +                if best is None or cost < best[0]:
         263 +                    best = (cost, x, ty, a)
         264 +                break
  209    265          if best is None:
  210        -            return float(np.clip(obj["cx"], lo, hi)), ty
         266 +            self._last_tilt = 0.0
         267 +            x = float(np.clip(obj["cx"], lo, hi))
         268 +            return x, obj["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
  211    269          self._last_grasp_ok = not best[0][0]
  212        -        return best[1], ty
         270 +        self._last_tilt = best[3]
         271 +        return best[1], best[2]
  213    272  
  214    273      def _grasp_ok(self, robot, obj, objs, prefer_g=0.0):
  215    274          self._last_grasp_ok = False
@@ -368,9 +427,12 @@ class GeneratedApproach:
  368    427                  if self.cur == "target_block" and self.kind == "stage":
  369    428                      prefer = self.stage_g
  370    429                  gx, gty = self._grasp_x(robot, obj, objs, prefer)
  371        -                parts = self._parts(robot)
         430 +                tilt = self._last_tilt
         431 +                if self.fails.get(self.cur, 0) > 0:
         432 +                    gty -= 0.002 * self.fails[self.cur]
         433 +                parts = self._parts(robot, tilt=tilt)
  372    434                  obst = self._obst_pick(objs, obj["name"])
  373        -                act, arrived = self._move(robot, gx, gty, parts, obst, 0.0)
         435 +                act, arrived = self._move(robot, gx, gty, parts, obst, 0.0, th=DOWN + tilt)
  374    436                  self.released = None
  375    437                  if not arrived:
  376    438                      lands = (abs(robot["x"] + float(act[0]) - gx) < 1e-5
@@ -391,6 +453,7 @@ class GeneratedApproach:
  391    453                      self.mode = "pick"
  392    454                      continue
  393    455                  self.g_actual = robot["x"] - obj["cx"]
         456 +                self.carry_th = robot["th"]
  394    457                  self.depth = robot["y"] - obj["y"]
  395    458                  if self.kind == "place":
  396    459                      self.drop = self.place_c
@@ -413,13 +476,15 @@ class GeneratedApproach:
  413    476                  if robot["vac"] < 0.5:
  414    477                      self.mode = "pick"
  415    478                      continue
  416        -                parts = self._parts(robot, obj, obj["x"] - robot["x"], robot["y"] - obj["y"])
         479 +                ctilt = self.carry_th - DOWN
         480 +                parts = self._parts(robot, obj, obj["x"] - robot["x"], robot["y"] - obj["y"], tilt=ctilt)
  417    481                  obst = self._obst(objs, exclude=(obj["name"],))
  418    482                  tx = self.drop + (robot["x"] - obj["cx"])
  419    483                  ty = robot["y"] - obj["y"] + self.drop_bot
  420        -                act, arrived = self._move(robot, tx, ty, parts, obst, 1.0)
         484 +                act, arrived = self._move(robot, tx, ty, parts, obst, 1.0, th=self.carry_th)
  421    485                  # detect failed grasp: object not following
  422    486                  if abs(robot["y"] - obj["y"] - self.depth) > 5e-3:
         487 +                    self.fails[self.cur] = self.fails.get(self.cur, 0) + 1
  423    488                      self.mode = "pick"
  424    489                      return self._act(0, 0, 0, 0, 0.0)
  425    490                  if not arrived:
```

</details>

<a id="C014"></a>
### C014 · Add debug/probe scripts; tilt support verified on regression sets

Commit `4f4bd2eae931a263272d051c158682fa46f330d8`; parents: f86a47c281a710c2caf40d12354deb8bb1eb71b6. Recorded author date: 2026-09-30T13:25:50+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0553](01_timeline.md#E0553): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C014_4f4bd2e.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/counts.py b/counts.py
new file mode 100644
index 0000000..86a356e
--- /dev/null
+++ b/counts.py
@@ -0,0 +1,7 @@
           1 +import time
           2 +from env_client import make_env
           3 +from collections import Counter
           4 +env=make_env(); c=Counter(); t=time.time()
           5 +for s in range(30):
           6 +    o,i=env.reset(seed=s); c[i['object_count']]+=1
           7 +print(c, time.time()-t)
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..b757a13
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,9 @@
           1 +import sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
           5 +obs, info = env.reset(seed=1029, options={"object_count":4}); ap.reset(obs, info)
           6 +for i in range(10):
           7 +    a=ap.get_action(obs); obs,*_=env.step(a)
           8 +    print(i, ap.mode, ap.cur, ap.place_c, ap.block_g, ap.blockers, ap.drop, getattr(ap,'drop_y',None))
           9 +env.close()
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..1f4873f
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,12 @@
           1 +import sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seed=int(sys.argv[1]); T=int(sys.argv[2])
           5 +env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
           6 +obs, info = env.reset(seed=seed); ap.reset(obs, info)
           7 +for i in range(T):
           8 +    a=ap.get_action(obs); obs,*_=env.step(a)
           9 +r,objs,s=ap._parse(obs)
          10 +print(r); [print({k:(round(v,3) if isinstance(v,float) else v) for k,v in o.items()}) for o in objs.values()]
          11 +print(ap.mode, ap.cur, ap.place_c, ap.block_g, ap.blockers, ap.drop)
          12 +env.close()
diff --git a/dbg4.py b/dbg4.py
new file mode 100644
index 0000000..3954825
--- /dev/null
+++ b/dbg4.py
@@ -0,0 +1,14 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed=int(sys.argv[1]); T0=int(sys.argv[2]); T1=int(sys.argv[3]); name=sys.argv[4]
           6 +env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
           7 +obs, info = env.reset(seed=seed); ap.reset(obs, info)
           8 +for i in range(T1):
           9 +    a=ap.get_action(obs)
          10 +    if i>=T0:
          11 +        r,objs,s=ap._parse(obs); o=objs[name]
          12 +        print(i, ap.mode, ap.cur, "robot",round(r['x'],4),round(r['y'],4),r['vac'], name, round(o['x'],4), round(o['y'],4), "act",np.round(a,4), "drop",ap.drop)
          13 +    obs,*_=env.step(a)
          14 +env.close()
diff --git a/lb.py b/lb.py
new file mode 100644
index 0000000..a7987cc
--- /dev/null
+++ b/lb.py
@@ -0,0 +1,18 @@
           1 +import sys, math
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +from concurrent.futures import ThreadPoolExecutor
           6 +def run(seed):
           7 +    env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
           8 +    obs, info = env.reset(seed=seed); ap.reset(obs, info)
           9 +    r,objs,s=ap._parse(obs); b=objs['target_block']
          10 +    gy=b['top']+0.21; py=0.1+0.21+b['h']
          11 +    lb=math.ceil(max(abs(b['cx']-r['x']),abs(gy-r['y']))/0.05)+math.ceil(max(abs(s['x']+s['w']/2-b['cx']),abs(py-gy))/0.05)
          12 +    for t in range(300):
          13 +        obs,rew,term,tr,_=env.step(ap.get_action(obs))
          14 +        if term: break
          15 +    env.close()
          16 +    return seed, info['object_count'], t+1, lb
          17 +with ThreadPoolExecutor(8) as ex: res=list(ex.map(run, range(int(sys.argv[1]), int(sys.argv[2]))))
          18 +for r in res: print(r, r[2]-r[3])
diff --git a/ping.py b/ping.py
new file mode 100644
index 0000000..b77279b
--- /dev/null
+++ b/ping.py
@@ -0,0 +1,3 @@
           1 +import time
           2 +from env_client import make_env
           3 +t=time.time(); env=make_env(); o,i=env.reset(seed=0); print("ok", time.time()-t); env.close()
diff --git a/probe4.py b/probe4.py
new file mode 100644
index 0000000..7fa722a
--- /dev/null
+++ b/probe4.py
@@ -0,0 +1,23 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def rb(o):
           5 +    r=o.get_object_from_name('robot'); return [float(o.get(r,f)) for f in ["x","y","arm_joint","vacuum"]]
           6 +def blk(o,n='target_block'):
           7 +    b=o.get_object_from_name(n); return [round(float(o.get(b,f)),4) for f in ["x","y"]]
           8 +for mode in ["vac_during","vac_on_last","none"]:
           9 +    obs,_=env.reset(seed=0)
          10 +    def st(a):
          11 +        global obs
          12 +        obs,*_=env.step(np.array(a,dtype=np.float32))
          13 +    v = 1.0 if mode=="vac_during" else 0.0
          14 +    st([0.05,0,0,0.1,v])
          15 +    for _ in range(20): st([np.clip(0.4896-rb(obs)[0],-.05,.05),0,0,0,v])
          16 +    ty=0.17254292219877243+0.21+2e-4
          17 +    for _ in range(20):
          18 +        d=np.clip(ty-rb(obs)[1],-.05,.05); last=abs(d)<0.05
          19 +        st([0,d,0,0,1.0 if (mode=="vac_during" or (last and mode!="none")) else 0])
          20 +    print(mode, np.round(rb(obs),4), blk(obs))
          21 +    st([0.05,0.05,0,0,1.0]); print(" after move", np.round(rb(obs),4), blk(obs))
          22 +    st([-0.05,0,0,0,0.0]); print(" release+move", np.round(rb(obs),4), blk(obs))
          23 +env.close()
diff --git a/probe5.py b/probe5.py
new file mode 100644
index 0000000..a190513
--- /dev/null
+++ b/probe5.py
@@ -0,0 +1,38 @@
           1 +import numpy as np, math
           2 +from env_client import make_env
           3 +env = make_env()
           4 +def R(o):
           5 +    r=o.get_object_from_name('robot'); return {f:float(o.get(r,f)) for f in ["x","y","theta","arm_joint","vacuum"]}
           6 +def B(o,n):
           7 +    b=o.get_object_from_name(n); return {f:round(float(o.get(b,f)),4) for f in ["x","y","theta"]}
           8 +def go(env,obs,tx,ty,tth,vac=0.0,n=60):
           9 +    for _ in range(n):
          10 +        r=R(obs)
          11 +        a=[np.clip(tx-r['x'],-.05,.05),np.clip(ty-r['y'],-.05,.05),np.clip(tth-r['theta'],-.19,.19),np.clip(0.2-r['arm_joint'],-.1,.1),vac]
          12 +        if max(abs(a[0]),abs(a[1]),abs(a[2]),abs(a[3]))<1e-7: break
          13 +        obs,*_=env.step(np.array(a,dtype=np.float32))
          14 +    return obs
          15 +for mode in ["tilt","side"]:
          16 +    obs,_=env.reset(seed=6016, options={"object_count":3})
          17 +    from approach import GeneratedApproach
          18 +    ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,None)
          19 +    for _ in range(17): obs,*_=env.step(ap.get_action(obs))
          20 +    print("obs1", B(obs,'obstruction1'))
          21 +    # first move obstruction1 away: skip — go high first
          22 +    obs=go(env,obs,1.2,0.8,-math.pi/2)
          23 +    if mode=="tilt":
          24 +        a=0.45
          25 +        obs=go(env,obs,1.517,0.6,-math.pi/2+a)
          26 +        # descend until blocked
          27 +        for _ in range(80):
          28 +            y0=R(obs)['y']; obs,*_=env.step(np.array([0,-0.005,0,0,0],dtype=np.float32))
          29 +            if abs(R(obs)['y']-y0)<1e-7: break
          30 +        print("tilt stopped", R(obs), B(obs,'obstruction0'))
          31 +    else:
          32 +        obs=go(env,obs,1.2,0.8,0.0)
          33 +        obs=go(env,obs,1.5604-0.21-0.0003,0.2+0.001,0.0)
          34 +        print("side at", R(obs), B(obs,'obstruction0'))
          35 +    obs,*_=env.step(np.array([0,0,0,0,1.0],dtype=np.float32))
          36 +    obs,*_=env.step(np.array([-0.05,0.05,0,0,1.0],dtype=np.float32))
          37 +    print(mode,"after", R(obs), B(obs,'obstruction0'))
          38 +env.close()
diff --git a/timing.py b/timing.py
new file mode 100644
index 0000000..4d0c6fb
--- /dev/null
+++ b/timing.py
@@ -0,0 +1,15 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +oc=int(sys.argv[1]); worst=0; tot=0
           5 +env = make_env()
           6 +for seed in range(int(sys.argv[2]), int(sys.argv[3])):
           7 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           8 +    obs, info = env.reset(seed=seed, options={"object_count":oc}); ap.reset(obs, info)
           9 +    t_ep=0
          10 +    for i in range(300):
          11 +        t=time.time(); a=ap.get_action(obs); dt=time.time()-t; t_ep+=dt; worst=max(worst,dt)
          12 +        obs,r,term,*_=env.step(a)
          13 +        if term: break
          14 +    print(seed, i+1, round(t_ep,2))
          15 +print("worst call", worst)
```

</details>

