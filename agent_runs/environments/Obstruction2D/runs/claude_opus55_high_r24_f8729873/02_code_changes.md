# Obstruction2D · claude-opus-5-5 · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `116c194` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `5e7d2f3` | Initial approach: remove blockers, place target | approach.py, dump.py, probe.py, probe2.py, probe3.py, test_approach.py | [E0035](01_timeline.md#E0035) |
| [C003](#C003) · `536f820` | Grasp offsets respecting robot x bounds | approach.py, res_0.txt, res_1.txt, res_2.txt, res_3.txt | [E0063](01_timeline.md#E0063) |
| [C004](#C004) · `9e7bfa8` | Allow partial-overlap grasps near world edge | approach.py, res_0.txt, res_1.txt, res_2.txt, res_3.txt, trace.py | [E0078](01_timeline.md#E0078) |
| [C005](#C005) · `cd87509` | Better parking spot search (stacking, sweep-based exclusion) | approach.py, c3.txt, c4.txt, c5.txt, cd.txt, cnt_3.txt, cnt_4.txt, cnt_6.txt, cnt_8.txt, dump2.py, test_approach.py, trace.py | [E0146](01_timeline.md#E0146) |
| [C006](#C006) · `e24e591` | Motion planner: diagonal collision-checked paths, grasp on final descent step | approach.py, approach_v1.py, r3.txt, r4.txt, rd.txt | [E0166](01_timeline.md#E0166) |
| [C007](#C007) · `82c16cf` | DP path planner, binned spot reranking, placement minimizing blockers | approach.py, approach_prev.py, c3.txt, c4.txt, c5.txt, cd.txt, cnt_3.txt, cnt_4.txt, cnt_6.txt, cnt_8.txt, dbg_spot.py, quick.py, r3.txt, r4.txt, rd.txt, res_0.txt, res_1.txt, res… | [E0289](01_timeline.md#E0289) |
| [C008](#C008) · `c162fd4` | Spot cost uses next blocker as next target; nearest-first blocker order | a_near3.txt, a_near4.txt, a_tall3.txt, a_tall4.txt, approach.py, approach_tall.py, events.py, q_3.txt, q_4.txt, q_d.txt, timing2.py | [E0381](01_timeline.md#E0381) |
| [C009](#C009) · `091283e` | Allow higher floating parking | approach.py, approach_t36.py, quick.py, t36.txt, t46.txt | [E0407](01_timeline.md#E0407) |
| [C010](#C010) · `421d9a5` | Arm-aware 3D DP path planner (uses arm extension for free vertical motion) | approach.py, approach_head.py, approach_noarm.py, dbg3.py, probe_stuck.py | [E0466](01_timeline.md#E0466) |
| [C011](#C011) · `fec32dd` | 3D DP: don&#x27;t force goal cell free for arms where exact goal collides | approach.py | [E0495](01_timeline.md#E0495) |
| [C012](#C012) · `c6c922b` | Add optional 3D DP spot costs (disabled: no gain, slower) | approach.py | [E0545](01_timeline.md#E0545) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `116c19480d4ef8b40e19ef696286fe7a94fc3798`; parents: none (initial snapshot). Recorded author date: 2026-09-30T10:21:40+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_116c194.diff)

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
index 0000000..20cecd0
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "d32653855f952d7a41b07443ef7fe868", "observation_space": {"type": "ObjectCentric", "types": [{"name": "crv_robot", "parent": null, "features": ["x", "y", "theta", "base_radius", "arm_joint", "arm_length", "vacuum", "gripper_height", "gripper_width"]}, {"name": "kinematic2d", "parent": null, "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order"]}, {"name": "circle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "radius"]}, {"name": "double_rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height", "x1", "y1", "theta1", "width1", "height1", "z_order1", "color_r1", "color_g1", "color_b1"]}, {"name": "lobject", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "length_side1", "length_side2"]}, {"name": "rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_block", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_surface", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}]}, "action_space": {"type": "Box", "shape": [5], "low": [-0.05000000074505806, -0.05000000074505806, -0.19634954631328583, -0.10000000149011612, 0.0], "high": [0.05000000074505806, 0.05000000074505806, 0.19634954631328583, 0.10000000149011612, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Initial approach: remove blockers, place target

Commit `5e7d2f3ab66326dec9ed97b0f25b6179e5e5ef70`; parents: 116c19480d4ef8b40e19ef696286fe7a94fc3798. Recorded author date: 2026-09-30T10:24:27+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0035](01_timeline.md#E0035): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_5e7d2f3_approach.py) · [Exact all-file diff](evidence/diffs/C002_5e7d2f3.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..a6e4d1b
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,322 @@
           1 +import math
           2 +import numpy as np
           3 +
           4 +WORLD_X = (0.0, 1.618)
           5 +ROBOT_Y_MAX = 0.895
           6 +FLOOR = 0.1
           7 +ARM = 0.2          # extended arm length we use
           8 +GW = 0.01          # gripper width (along arm)
           9 +GH = 0.07          # gripper height (perpendicular)
          10 +BASE_R = 0.1
          11 +TIP = ARM + GW     # distance from robot center to gripper tip (pointing down)
          12 +
          13 +
          14 +def _rect_bbox(state, o):
          15 +    x = float(state.get(o, "x")); y = float(state.get(o, "y"))
          16 +    w = float(state.get(o, "width")); h = float(state.get(o, "height"))
          17 +    th = float(state.get(o, "theta"))
          18 +    if abs(th) < 1e-6:
          19 +        return (x, y, x + w, y + h)
          20 +    c, s = math.cos(th), math.sin(th)
          21 +    pts = [(x, y), (x + w * c, y + w * s), (x - h * s, y + h * c),
          22 +           (x + w * c - h * s, y + w * s + h * c)]
          23 +    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
          24 +    return (min(xs), min(ys), max(xs), max(ys))
          25 +
          26 +
          27 +def _circle_rect_dist(cx, cy, b):
          28 +    dx = max(b[0] - cx, 0.0, cx - b[2])
          29 +    dy = max(b[1] - cy, 0.0, cy - b[3])
          30 +    return math.hypot(dx, dy)
          31 +
          32 +
          33 +def _overlap(a, b, m=0.0):
          34 +    return a[0] < b[2] + m and b[0] < a[2] + m and a[1] < b[3] + m and b[1] < a[3] + m
          35 +
          36 +
          37 +class GeneratedApproach:
          38 +    def __init__(self, action_space, observation_space, primitives):
          39 +        self.low = np.array(action_space.low, dtype=np.float32)
          40 +        self.high = np.array(action_space.high, dtype=np.float32)
          41 +
          42 +    # ------------------------------------------------------------------
          43 +    def reset(self, state, info):
          44 +        self.state = state
          45 +        self.gen = self._plan()
          46 +        self.vac = 0.0
          47 +
          48 +    def get_action(self, state):
          49 +        self.state = state
          50 +        try:
          51 +            a = next(self.gen)
          52 +        except StopIteration:
          53 +            self.gen = self._plan()
          54 +            try:
          55 +                a = next(self.gen)
          56 +            except StopIteration:
          57 +                a = np.zeros(5, dtype=np.float32)
          58 +        a = np.clip(np.asarray(a, dtype=np.float32), self.low, self.high)
          59 +        return a
          60 +
          61 +    # ------------------------------------------------------------------
          62 +    def _objs(self):
          63 +        s = self.state
          64 +        robot = None; block = None; surf = None; obst = []
          65 +        for n in sorted(s.get_object_names()):
          66 +            o = s.get_object_from_name(n)
          67 +            tn = o.type.name
          68 +            if tn == "crv_robot":
          69 +                robot = o
          70 +            elif tn == "target_block":
          71 +                block = o
          72 +            elif tn == "target_surface":
          73 +                surf = o
          74 +            else:
          75 +                obst.append(o)
          76 +        return robot, block, surf, obst
          77 +
          78 +    def _rpos(self):
          79 +        r = self._objs()[0]
          80 +        s = self.state
          81 +        return (float(s.get(r, "x")), float(s.get(r, "y")),
          82 +                float(s.get(r, "theta")), float(s.get(r, "arm_joint")))
          83 +
          84 +    # ------------------------------------------------------------------
          85 +    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0):
          86 +        return np.array([dx, dy, dth, darm, self.vac], dtype=np.float32)
          87 +
          88 +    def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200):
          89 +        """Move towards (tx, ty); yields actions. Returns True on success."""
          90 +        stuck = 0
          91 +        last = None
          92 +        for _ in range(max_steps):
          93 +            x, y, th, aj = self._rpos()
          94 +            gx = x if tx is None else tx
          95 +            gy = y if ty is None else ty
          96 +            ex, ey = gx - x, gy - y
          97 +            if abs(ex) <= tol and abs(ey) <= tol:
          98 +                return True
          99 +            if last is not None and abs(last[0] - x) < 1e-7 and abs(last[1] - y) < 1e-7:
         100 +                stuck += 1
         101 +                if stuck >= 2:
         102 +                    return False
         103 +            else:
         104 +                stuck = 0
         105 +            last = (x, y)
         106 +            yield self._act(float(np.clip(ex, -0.05, 0.05)), float(np.clip(ey, -0.05, 0.05)))
         107 +        return False
         108 +
         109 +    def _setup_pose(self):
         110 +        # rise, orient downwards, extend arm
         111 +        x, y, th, aj = self._rpos()
         112 +        yield from self._goto(None, ROBOT_Y_MAX)
         113 +        for _ in range(60):
         114 +            x, y, th, aj = self._rpos()
         115 +            eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
         116 +            ea = ARM - aj
         117 +            if abs(eth) < 1e-4 and abs(ea) < 1e-4:
         118 +                break
         119 +            yield np.array([0, 0, np.clip(eth, -0.19, 0.19), np.clip(ea, -0.1, 0.1), self.vac],
         120 +                           dtype=np.float32)
         121 +
         122 +    # ------------------------------------------------------------------
         123 +    def _others_bboxes(self, exclude):
         124 +        robot, block, surf, obst = self._objs()
         125 +        out = []
         126 +        for o in [block] + obst:
         127 +            if o in exclude:
         128 +                continue
         129 +            out.append(_rect_bbox(self.state, o))
         130 +        return out
         131 +
         132 +    def _descent_free(self, rx, ry_final, carried_bbox_final, others, margin=0.01):
         133 +        """Check vertical descent from travel height to ry_final at x=rx is collision free."""
         134 +        # base circle sweep: check at the final (lowest) position -- sweep is vertical,
         135 +        # and anything below is covered by checking the column.
         136 +        for b in others:
         137 +            # circle swept vertically from ry_final upwards
         138 +            cy = min(max(ry_final, b[1]), ROBOT_Y_MAX)
         139 +            cy = max(cy, ry_final)
         140 +            if _circle_rect_dist(rx, cy, b) < BASE_R + margin:
         141 +                return False
         142 +            # arm + gripper column
         143 +            col = (rx - GH / 2, ry_final - TIP, rx + GH / 2, ROBOT_Y_MAX)
         144 +            if _overlap(col, b, margin * 0.3):
         145 +                return False
         146 +            if carried_bbox_final is not None:
         147 +                cb = carried_bbox_final
         148 +                colc = (cb[0], cb[1], cb[2], cb[3] + (ROBOT_Y_MAX - ry_final))
         149 +                if _overlap(colc, b, margin * 0.5):
         150 +                    return False
         151 +        return True
         152 +
         153 +    def _choose_grasp_x(self, o, others):
         154 +        b = _rect_bbox(self.state, o)
         155 +        top = b[3]
         156 +        ry = top + TIP + 0.003
         157 +        lo = b[0] + GH / 2 - 0.01
         158 +        hi = b[2] - GH / 2 + 0.01
         159 +        cx = (b[0] + b[2]) / 2
         160 +        if hi < lo:
         161 +            lo = hi = cx
         162 +        cands = sorted(np.linspace(lo, hi, 21).tolist() + [cx], key=lambda v: abs(v - cx))
         163 +        for gx in cands:
         164 +            if gx < WORLD_X[0] + BASE_R + 0.002 or gx > WORLD_X[1] - BASE_R - 0.002:
         165 +                continue
         166 +            if self._descent_free(gx, ry, None, others):
         167 +                return gx
         168 +        return None
         169 +
         170 +    def _pick(self, o):
         171 +        """Pick object o. Yields actions; returns (dx_off) offset of object x relative to robot."""
         172 +        others = self._others_bboxes([o])
         173 +        gx = self._choose_grasp_x(o, others)
         174 +        if gx is None:
         175 +            return False
         176 +        b = _rect_bbox(self.state, o)
         177 +        yield from self._goto(None, ROBOT_Y_MAX)
         178 +        yield from self._goto(gx, None)
         179 +        ry = b[3] + TIP + 0.003
         180 +        ok = yield from self._goto(None, ry, tol=1e-4)
         181 +        self.vac = 1.0
         182 +        yield self._act()
         183 +        yield self._act()
         184 +        # lift
         185 +        yield from self._goto(None, ROBOT_Y_MAX)
         186 +        nb = _rect_bbox(self.state, o)
         187 +        if nb[1] < b[1] + 0.05:
         188 +            # grasp failed
         189 +            self.vac = 0.0
         190 +            yield self._act()
         191 +            return False
         192 +        return True
         193 +
         194 +    def _place_at(self, o, target_left, target_bottom):
         195 +        x, y, _, _ = self._rpos()
         196 +        b = _rect_bbox(self.state, o)
         197 +        rx = x + (target_left - b[0])
         198 +        yield from self._goto(rx, None)
         199 +        x, y, _, _ = self._rpos()
         200 +        b = _rect_bbox(self.state, o)
         201 +        ry = y - (b[1] - target_bottom)
         202 +        yield from self._goto(None, ry, tol=1e-4)
         203 +
         204 +    # ------------------------------------------------------------------
         205 +    def _final_placement(self):
         206 +        robot, block, surf, obst = self._objs()
         207 +        s = self.state
         208 +        sb = _rect_bbox(s, surf)
         209 +        bb = _rect_bbox(s, block)
         210 +        bw = bb[2] - bb[0]
         211 +        left = sb[0] + (sb[2] - sb[0] - bw) / 2
         212 +        return left, sb[3] + 0.008, sb
         213 +
         214 +    def _blocking(self):
         215 +        """Obstructions that interfere with placing the block on the surface."""
         216 +        robot, block, surf, obst = self._objs()
         217 +        s = self.state
         218 +        left, bottom, sb = self._final_placement()
         219 +        bb = _rect_bbox(s, block)
         220 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         221 +        final_bb = (left, bottom, left + bw, bottom + bh)
         222 +        rx = left + bw / 2
         223 +        ry = bottom + bh + TIP + 0.003
         224 +        res = []
         225 +        for o in obst:
         226 +            ob = _rect_bbox(s, o)
         227 +            if not self._descent_free(rx, ry, final_bb, [ob], margin=0.015):
         228 +                res.append(o)
         229 +            elif ob[0] < sb[2] and ob[2] > sb[0] and ob[1] < sb[3] + 0.05:
         230 +                res.append(o)
         231 +        return res
         232 +
         233 +    def _find_spot(self, o):
         234 +        """Find (left, bottom) to park obstruction o."""
         235 +        robot, block, surf, obst = self._objs()
         236 +        s = self.state
         237 +        ob = _rect_bbox(s, o)
         238 +        w, h = ob[2] - ob[0], ob[3] - ob[1]
         239 +        # offset of grasp relative to object left
         240 +        x, y, _, _ = self._rpos()
         241 +        goff = x - ob[0]
         242 +        sb = _rect_bbox(s, surf)
         243 +        others = self._others_bboxes([o])
         244 +        left_f, bottom_f, _ = self._final_placement()
         245 +        bb = _rect_bbox(s, block)
         246 +        bw = bb[2] - bb[0]
         247 +        # forbidden zone around the surface / final block placement
         248 +        fz = (min(sb[0], left_f) - 0.13, max(sb[2], left_f + bw) + 0.13)
         249 +        levels = [FLOOR + 0.005]
         250 +        best = None
         251 +        xs = np.arange(WORLD_X[0] + 0.01, WORLD_X[1] - w - 0.01, 0.01)
         252 +        for bottom in levels:
         253 +            for lx in xs:
         254 +                if lx < fz[1] and lx + w > fz[0]:
         255 +                    continue
         256 +                rx = lx + goff
         257 +                if rx < BASE_R + 0.003 or rx > WORLD_X[1] - BASE_R - 0.003:
         258 +                    continue
         259 +                cand = (lx, bottom, lx + w, bottom + h)
         260 +                bad = False
         261 +                for b in others:
         262 +                    if _overlap(cand, b, 0.02):
         263 +                        bad = True
         264 +                        break
         265 +                if bad:
         266 +                    continue
         267 +                ry = bottom + h + (y - ob[3])
         268 +                if not self._descent_free(rx, ry, cand, others, margin=0.015):
         269 +                    continue
         270 +                cost = abs(rx - x)
         271 +                if best is None or cost < best[0]:
         272 +                    best = (cost, lx, bottom)
         273 +            if best is not None:
         274 +                break
         275 +        if best is None:
         276 +            # fallback: park in the air high above in the far region
         277 +            far = WORLD_X[1] - w - 0.15 if (sb[0] + sb[2]) / 2 < WORLD_X[1] / 2 else 0.15
         278 +            return far, 0.45
         279 +        return best[1], best[2]
         280 +
         281 +    def _plan(self):
         282 +        self.vac = 0.0
         283 +        yield from self._setup_pose()
         284 +        failures = 0
         285 +        for _ in range(30):
         286 +            blockers = self._blocking()
         287 +            if not blockers:
         288 +                break
         289 +            # pick blockers in order of height (tallest first) that are graspable
         290 +            robot, block, surf, obst = self._objs()
         291 +            blockers.sort(key=lambda o: -_rect_bbox(self.state, o)[3])
         292 +            picked = False
         293 +            for o in blockers:
         294 +                others = self._others_bboxes([o])
         295 +                if self._choose_grasp_x(o, others) is None:
         296 +                    continue
         297 +                ok = yield from self._pick(o)
         298 +                if not ok:
         299 +                    failures += 1
         300 +                    continue
         301 +                left, bottom = self._find_spot(o)
         302 +                yield from self._place_at(o, left, bottom)
         303 +                self.vac = 0.0
         304 +                yield self._act()
         305 +                yield from self._goto(None, ROBOT_Y_MAX)
         306 +                picked = True
         307 +                break
         308 +            if not picked:
         309 +                failures += 1
         310 +                if failures > 5:
         311 +                    break
         312 +        # now the target block
         313 +        for _ in range(10):
         314 +            robot, block, surf, obst = self._objs()
         315 +            ok = yield from self._pick(block)
         316 +            if ok:
         317 +                break
         318 +        left, bottom, sb = self._final_placement()
         319 +        yield from self._place_at(block, left, bottom)
         320 +        self.vac = 0.0
         321 +        for _ in range(5):
         322 +            yield self._act()
diff --git a/dump.py b/dump.py
new file mode 100644
index 0000000..cd0a296
--- /dev/null
+++ b/dump.py
@@ -0,0 +1,10 @@
           1 +from env_client import make_env
           2 +import sys
           3 +env = make_env()
           4 +for seed in range(int(sys.argv[1]), int(sys.argv[2])):
           5 +    obs, info = env.reset(seed=seed)
           6 +    print("seed", seed, type(obs))
           7 +    for n in sorted(obs.get_object_names(), key=str):
           8 +        o = obs.get_object_from_name(n) if isinstance(n,str) else n
           9 +        print(" ", o, {f: round(float(obs.get(o, f)),3) for f in ["x","y","theta","width","height","static"] if True} if 'robot' not in str(o) else {f: round(float(obs.get(o,f)),3) for f in env.observation_space.type_features[env.observation_space.get_type('crv_robot')] } )
          10 +env.close()
diff --git a/probe.py b/probe.py
new file mode 100644
index 0000000..03f6232
--- /dev/null
+++ b/probe.py
@@ -0,0 +1,28 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
           6 +def rs(o): return tuple(round(float(o.get(R,f)),3) for f in ['x','y','theta','arm_joint','vacuum'])
           7 +def bs(o): return tuple(round(float(o.get(B,f)),3) for f in ['x','y','theta'])
           8 +bx = obs.get(B,'x')+obs.get(B,'width')/2
           9 +# move to x above block center
          10 +for i in range(40):
          11 +    dx = np.clip(bx-obs.get(R,'x'),-0.05,0.05)
          12 +    obs,r,t,tr,_ = env.step(np.array([dx,0,0,0,0],dtype=np.float32))
          13 +print(rs(obs), bs(obs))
          14 +# go down
          15 +for i in range(30):
          16 +    prev = rs(obs)
          17 +    obs,r,t,tr,_ = env.step(np.array([0,-0.05,0,0,0],dtype=np.float32))
          18 +    print('down', rs(obs))
          19 +    if rs(obs)==prev: break
          20 +for i in range(5):
          21 +    obs,r,t,tr,_ = env.step(np.array([0,0,0,0.1,0],dtype=np.float32))
          22 +    print('ext', rs(obs))
          23 +for i in range(3):
          24 +    obs,r,t,tr,_ = env.step(np.array([0,0,0,0.0,1],dtype=np.float32))
          25 +    print('vac', rs(obs), bs(obs))
          26 +for i in range(4):
          27 +    obs,r,t,tr,_ = env.step(np.array([0,0.05,0,0.0,1],dtype=np.float32))
          28 +    print('up', rs(obs), bs(obs))
diff --git a/probe2.py b/probe2.py
new file mode 100644
index 0000000..12ca266
--- /dev/null
+++ b/probe2.py
@@ -0,0 +1,20 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +R = obs.get_object_from_name('robot')
           6 +def rs(o): return tuple(round(float(o.get(R,f)),3) for f in ['x','y','theta','arm_joint','vacuum'])
           7 +def run(a,n):
           8 +    global obs
           9 +    for i in range(n):
          10 +        p=rs(obs); obs,*_ = env.step(np.array(a,dtype=np.float32))
          11 +        if rs(obs)==p: break
          12 +    print(a, rs(obs))
          13 +run([0,0.05,0,0,0],20)
          14 +run([-0.05,0,0,0,0],30)
          15 +run([0,0,0,0.1,0],3)
          16 +run([0,-0.05,0,0,0],30)
          17 +run([0,-0.01,0,0,0],30)
          18 +run([0,0,0,-0.1,0],3)
          19 +run([0,-0.01,0,0,0],30)
          20 +run([0.05,0,0,0,0],60)
diff --git a/probe3.py b/probe3.py
new file mode 100644
index 0000000..ce92fb2
--- /dev/null
+++ b/probe3.py
@@ -0,0 +1,18 @@
           1 +# check gravity: grasp block, lift, release midair
           2 +from env_client import make_env
           3 +import numpy as np
           4 +env = make_env()
           5 +obs, info = env.reset(seed=1)
           6 +R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
           7 +bs=lambda: tuple(round(float(obs.get(B,f)),3) for f in ['x','y'])
           8 +bx = obs.get(B,'x')+obs.get(B,'width')/2
           9 +for i in range(40):
          10 +    obs,*_ = env.step(np.array([np.clip(bx-obs.get(R,'x'),-.05,.05),0,0,0,0],dtype=np.float32))
          11 +top=obs.get(B,'y')+obs.get(B,'height')
          12 +while obs.get(R,'y')-0.11-top>0.004:
          13 +    obs,*_ = env.step(np.array([0,-min(.05,obs.get(R,'y')-0.11-top-0.003),0,0,0],dtype=np.float32))
          14 +print(obs.get(R,'y')-0.11-top)
          15 +obs,*_ = env.step(np.array([0,0,0,0,1],dtype=np.float32))
          16 +for i in range(4): obs,*_ = env.step(np.array([0,0.05,0,0,1],dtype=np.float32))
          17 +print(bs())
          18 +for i in range(4): obs,*_ = env.step(np.array([0,0.05,0,0,0],dtype=np.float32)); print(bs())
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..f2cd0e6
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,25 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +def run(seed, verbose=False):
           6 +    env = make_env()
           7 +    obs, info = env.reset(seed=seed)
           8 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +    ap.reset(obs, info)
          10 +    n_obs = len(obs.get_object_names()) - 3
          11 +    t0=time.time()
          12 +    for t in range(env.max_steps):
          13 +        a = ap.get_action(obs)
          14 +        obs, r, term, trunc, info = env.step(a)
          15 +        if term or trunc: break
          16 +    env.close()
          17 +    return term, t+1, n_obs, time.time()-t0
          18 +if __name__ == "__main__":
          19 +    s0, s1 = int(sys.argv[1]), int(sys.argv[2])
          20 +    succ=0
          21 +    for s in range(s0, s1):
          22 +        term, steps, n, dt = run(s)
          23 +        succ += term
          24 +        print(f"seed {s} nobs {n} success {term} steps {steps} time {dt:.1f}", flush=True)
          25 +    print("success", succ, "/", s1-s0)
```

</details>

<a id="C003"></a>
### C003 · Grasp offsets respecting robot x bounds

Commit `536f820f235b80570a659c909d09dd0393026aa0`; parents: 5e7d2f3ab66326dec9ed97b0f25b6179e5e5ef70. Recorded author date: 2026-09-30T10:28:20+02:00.

File roles (automatic): policy, setup/other.

- [E0063](01_timeline.md#E0063): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_536f820_approach.py) · [Exact all-file diff](evidence/diffs/C003_536f820.diff)

[Previous saved controller snapshot](evidence/versions/C002_5e7d2f3_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a6e4d1b..6d2fd70 100644
--- a/approach.py
+++ b/approach.py
@@ -8,6 +8,8 @@ ARM = 0.2          # extended arm length we use
    8      8  GW = 0.01          # gripper width (along arm)
    9      9  GH = 0.07          # gripper height (perpendicular)
   10     10  BASE_R = 0.1
          11 +RX_MIN = 0.1 + 0.002
          12 +RX_MAX = 1.618 - 0.1 - 0.002
   11     13  TIP = ARM + GW     # distance from robot center to gripper tip (pointing down)
   12     14  
   13     15  
@@ -150,42 +152,50 @@ class GeneratedApproach:
  150    152                      return False
  151    153          return True
  152    154  
  153        -    def _choose_grasp_x(self, o, others):
  154        -        b = _rect_bbox(self.state, o)
  155        -        top = b[3]
  156        -        ry = top + TIP + 0.003
  157        -        lo = b[0] + GH / 2 - 0.01
  158        -        hi = b[2] - GH / 2 + 0.01
  159        -        cx = (b[0] + b[2]) / 2
         155 +    def _grasp_cands(self, b, pref=None):
         156 +        lo = b[0] + 0.012
         157 +        hi = b[2] - 0.012
         158 +        cx = (b[0] + b[2]) / 2 if pref is None else pref
  160    159          if hi < lo:
  161        -            lo = hi = cx
  162        -        cands = sorted(np.linspace(lo, hi, 21).tolist() + [cx], key=lambda v: abs(v - cx))
  163        -        for gx in cands:
  164        -            if gx < WORLD_X[0] + BASE_R + 0.002 or gx > WORLD_X[1] - BASE_R - 0.002:
         160 +            lo = hi = (b[0] + b[2]) / 2
         161 +        full_lo = b[0] + GH / 2
         162 +        full_hi = b[2] - GH / 2
         163 +        vals = np.linspace(lo, hi, 41).tolist() + [min(max(cx, lo), hi)]
         164 +
         165 +        def key(v):
         166 +            # prefer full gripper contact, then closeness to preferred
         167 +            pen = 0.0
         168 +            if full_lo <= full_hi:
         169 +                pen = max(0.0, full_lo - v, v - full_hi)
         170 +            return (round(pen, 4) > 0.0, abs(v - cx))
         171 +        return sorted(vals, key=key)
         172 +
         173 +    def _choose_grasp_x(self, o, others, pref=None):
         174 +        b = _rect_bbox(self.state, o)
         175 +        ry = b[3] + TIP + 0.003
         176 +        for gx in self._grasp_cands(b, pref):
         177 +            if gx < RX_MIN or gx > RX_MAX:
  165    178                  continue
  166    179              if self._descent_free(gx, ry, None, others):
  167    180                  return gx
  168    181          return None
  169    182  
  170        -    def _pick(self, o):
  171        -        """Pick object o. Yields actions; returns (dx_off) offset of object x relative to robot."""
         183 +    def _pick(self, o, pref=None):
  172    184          others = self._others_bboxes([o])
  173        -        gx = self._choose_grasp_x(o, others)
         185 +        gx = self._choose_grasp_x(o, others, pref)
  174    186          if gx is None:
  175    187              return False
  176    188          b = _rect_bbox(self.state, o)
  177    189          yield from self._goto(None, ROBOT_Y_MAX)
  178    190          yield from self._goto(gx, None)
  179    191          ry = b[3] + TIP + 0.003
  180        -        ok = yield from self._goto(None, ry, tol=1e-4)
         192 +        yield from self._goto(None, ry, tol=1e-4)
  181    193          self.vac = 1.0
  182    194          yield self._act()
  183    195          yield self._act()
  184        -        # lift
  185    196          yield from self._goto(None, ROBOT_Y_MAX)
  186    197          nb = _rect_bbox(self.state, o)
  187    198          if nb[1] < b[1] + 0.05:
  188        -            # grasp failed
  189    199              self.vac = 0.0
  190    200              yield self._act()
  191    201              return False
@@ -203,23 +213,38 @@ class GeneratedApproach:
  203    213  
  204    214      # ------------------------------------------------------------------
  205    215      def _final_placement(self):
         216 +        """Returns (left, bottom, surface_bbox, grasp_offset_from_block_left)."""
  206    217          robot, block, surf, obst = self._objs()
  207    218          s = self.state
  208    219          sb = _rect_bbox(s, surf)
  209    220          bb = _rect_bbox(s, block)
  210    221          bw = bb[2] - bb[0]
  211        -        left = sb[0] + (sb[2] - sb[0] - bw) / 2
  212        -        return left, sb[3] + 0.008, sb
         222 +        Llo = sb[0] + min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
         223 +        Lhi = sb[2] - bw - min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
         224 +        Lc = sb[0] + (sb[2] - sb[0] - bw) / 2
         225 +        if Lhi < Llo:
         226 +            Llo = Lhi = Lc
         227 +        best = None
         228 +        for g in self._grasp_cands((0.0, 0.0, bw, 1.0)):
         229 +            for L in sorted(np.linspace(Llo, Lhi, 21).tolist() + [Lc], key=lambda v: abs(v - Lc)):
         230 +                if RX_MIN <= L + g <= RX_MAX:
         231 +                    best = (L, g)
         232 +                    break
         233 +            if best is not None:
         234 +                break
         235 +        if best is None:
         236 +            best = (Lc, bw / 2)
         237 +        return best[0], sb[3] + 0.008, sb, best[1]
  213    238  
  214    239      def _blocking(self):
  215    240          """Obstructions that interfere with placing the block on the surface."""
  216    241          robot, block, surf, obst = self._objs()
  217    242          s = self.state
  218        -        left, bottom, sb = self._final_placement()
         243 +        left, bottom, sb, g = self._final_placement()
  219    244          bb = _rect_bbox(s, block)
  220    245          bw, bh = bb[2] - bb[0], bb[3] - bb[1]
  221    246          final_bb = (left, bottom, left + bw, bottom + bh)
  222        -        rx = left + bw / 2
         247 +        rx = left + g
  223    248          ry = bottom + bh + TIP + 0.003
  224    249          res = []
  225    250          for o in obst:
@@ -241,7 +266,7 @@ class GeneratedApproach:
  241    266          goff = x - ob[0]
  242    267          sb = _rect_bbox(s, surf)
  243    268          others = self._others_bboxes([o])
  244        -        left_f, bottom_f, _ = self._final_placement()
         269 +        left_f, bottom_f, _, _ = self._final_placement()
  245    270          bb = _rect_bbox(s, block)
  246    271          bw = bb[2] - bb[0]
  247    272          # forbidden zone around the surface / final block placement
@@ -254,7 +279,7 @@ class GeneratedApproach:
  254    279                  if lx < fz[1] and lx + w > fz[0]:
  255    280                      continue
  256    281                  rx = lx + goff
  257        -                if rx < BASE_R + 0.003 or rx > WORLD_X[1] - BASE_R - 0.003:
         282 +                if rx < RX_MIN or rx > RX_MAX:
  258    283                      continue
  259    284                  cand = (lx, bottom, lx + w, bottom + h)
  260    285                  bad = False
@@ -312,10 +337,12 @@ class GeneratedApproach:
  312    337          # now the target block
  313    338          for _ in range(10):
  314    339              robot, block, surf, obst = self._objs()
  315        -            ok = yield from self._pick(block)
         340 +            left, bottom, sb, g = self._final_placement()
         341 +            bb = _rect_bbox(self.state, block)
         342 +            ok = yield from self._pick(block, pref=bb[0] + g)
  316    343              if ok:
  317    344                  break
  318        -        left, bottom, sb = self._final_placement()
         345 +        left, bottom, sb, g = self._final_placement()
  319    346          yield from self._place_at(block, left, bottom)
  320    347          self.vac = 0.0
  321    348          for _ in range(5):
diff --git a/res_0.txt b/res_0.txt
new file mode 100644
index 0000000..ac8b438
--- /dev/null
+++ b/res_0.txt
@@ -0,0 +1,28 @@
           1 +seed 10 nobs 2 success True steps 165 time 6.5
           2 +seed 11 nobs 0 success True steps 66 time 2.6
           3 +seed 12 nobs 1 success True steps 141 time 7.0
           4 +seed 13 nobs 2 success True steps 153 time 4.3
           5 +seed 14 nobs 0 success True steps 45 time 1.9
           6 +seed 15 nobs 2 success True steps 92 time 5.0
           7 +seed 16 nobs 1 success True steps 45 time 1.1
           8 +seed 17 nobs 2 success True steps 158 time 8.1
           9 +seed 18 nobs 2 success True steps 180 time 9.5
          10 +seed 19 nobs 1 success True steps 101 time 4.9
          11 +seed 20 nobs 2 success True steps 119 time 6.1
          12 +seed 21 nobs 0 success False steps 1000 time 41.4
          13 +seed 22 nobs 2 success True steps 163 time 8.3
          14 +seed 23 nobs 0 success True steps 68 time 3.3
          15 +seed 24 nobs 1 success True steps 125 time 4.6
          16 +seed 25 nobs 1 success True steps 93 time 4.3
          17 +seed 26 nobs 2 success True steps 162 time 7.7
          18 +seed 27 nobs 0 success True steps 49 time 2.0
          19 +seed 28 nobs 1 success True steps 65 time 2.3
          20 +seed 29 nobs 2 success True steps 99 time 5.3
          21 +seed 30 nobs 0 success True steps 55 time 2.2
          22 +seed 31 nobs 1 success False steps 1000 time 44.2
          23 +seed 32 nobs 2 success True steps 165 time 8.0
          24 +seed 33 nobs 2 success True steps 143 time 8.3
          25 +seed 34 nobs 0 success True steps 53 time 1.1
          26 +seed 35 nobs 0 success True steps 51 time 1.6
          27 +seed 36 nobs 1 success True steps 89 time 3.8
          28 +seed 37 nobs 0 success True steps 53 time 2.3
diff --git a/res_1.txt b/res_1.txt
new file mode 100644
index 0000000..0fe513b
--- /dev/null
+++ b/res_1.txt
@@ -0,0 +1,27 @@
           1 +seed 60 nobs 0 success True steps 46 time 1.3
           2 +seed 61 nobs 1 success True steps 114 time 3.6
           3 +seed 62 nobs 1 success True steps 113 time 4.9
           4 +seed 63 nobs 1 success True steps 97 time 4.2
           5 +seed 64 nobs 1 success True steps 52 time 2.0
           6 +seed 65 nobs 0 success True steps 47 time 1.1
           7 +seed 66 nobs 2 success True steps 110 time 5.5
           8 +seed 67 nobs 2 success True steps 105 time 5.1
           9 +seed 68 nobs 1 success True steps 104 time 4.8
          10 +seed 69 nobs 0 success True steps 60 time 2.1
          11 +seed 70 nobs 1 success True steps 115 time 4.7
          12 +seed 71 nobs 2 success True steps 105 time 4.8
          13 +seed 72 nobs 2 success True steps 144 time 7.0
          14 +seed 73 nobs 2 success True steps 175 time 8.7
          15 +seed 74 nobs 0 success False steps 1000 time 40.9
          16 +seed 75 nobs 1 success False steps 1000 time 43.9
          17 +seed 76 nobs 1 success True steps 126 time 4.7
          18 +seed 77 nobs 0 success True steps 50 time 1.5
          19 +seed 78 nobs 2 success True steps 164 time 8.4
          20 +seed 79 nobs 0 success True steps 62 time 2.5
          21 +seed 80 nobs 2 success True steps 166 time 8.9
          22 +seed 81 nobs 0 success True steps 54 time 2.3
          23 +seed 82 nobs 2 success True steps 131 time 5.0
          24 +seed 83 nobs 2 success True steps 174 time 8.6
          25 +seed 84 nobs 1 success True steps 121 time 5.7
          26 +seed 85 nobs 2 success True steps 156 time 7.9
          27 +seed 86 nobs 2 success True steps 95 time 4.4
diff --git a/res_2.txt b/res_2.txt
new file mode 100644
index 0000000..72e1cb2
--- /dev/null
+++ b/res_2.txt
@@ -0,0 +1,47 @@
           1 +seed 110 nobs 1 success True steps 117 time 4.2
           2 +seed 111 nobs 1 success True steps 102 time 4.1
           3 +seed 112 nobs 0 success True steps 45 time 1.7
           4 +seed 113 nobs 0 success True steps 70 time 2.8
           5 +seed 114 nobs 0 success True steps 41 time 1.8
           6 +seed 115 nobs 1 success True steps 126 time 3.8
           7 +seed 116 nobs 0 success True steps 73 time 2.9
           8 +seed 117 nobs 0 success True steps 53 time 2.3
           9 +seed 118 nobs 1 success True steps 109 time 4.8
          10 +seed 119 nobs 1 success True steps 112 time 4.9
          11 +seed 120 nobs 0 success True steps 40 time 1.7
          12 +seed 121 nobs 0 success True steps 45 time 1.4
          13 +seed 122 nobs 2 success True steps 170 time 8.7
          14 +seed 123 nobs 0 success True steps 67 time 3.0
          15 +seed 124 nobs 2 success True steps 120 time 4.5
          16 +seed 125 nobs 1 success True steps 127 time 5.8
          17 +seed 126 nobs 0 success True steps 40 time 1.7
          18 +seed 127 nobs 1 success True steps 130 time 6.3
          19 +seed 128 nobs 2 success True steps 173 time 9.4
          20 +seed 129 nobs 1 success True steps 111 time 5.0
          21 +seed 130 nobs 2 success True steps 113 time 3.9
          22 +seed 131 nobs 1 success True steps 107 time 4.9
          23 +seed 132 nobs 2 success True steps 160 time 8.0
          24 +seed 133 nobs 1 success True steps 103 time 5.2
          25 +seed 134 nobs 2 success True steps 49 time 2.4
          26 +seed 135 nobs 1 success True steps 41 time 1.8
          27 +seed 136 nobs 2 success True steps 107 time 4.4
          28 +seed 137 nobs 1 success True steps 132 time 4.4
          29 +seed 138 nobs 1 success True steps 144 time 5.5
          30 +seed 139 nobs 1 success True steps 129 time 6.6
          31 +seed 140 nobs 1 success True steps 104 time 4.8
          32 +seed 141 nobs 1 success True steps 100 time 3.8
          33 +seed 142 nobs 0 success True steps 80 time 2.6
          34 +seed 143 nobs 2 success True steps 161 time 7.1
          35 +seed 144 nobs 0 success True steps 61 time 2.7
          36 +seed 145 nobs 1 success True steps 93 time 3.9
          37 +seed 146 nobs 2 success True steps 113 time 5.1
          38 +seed 147 nobs 0 success True steps 48 time 2.5
          39 +seed 148 nobs 0 success True steps 39 time 1.8
          40 +seed 149 nobs 0 success True steps 51 time 2.1
          41 +seed 150 nobs 1 success True steps 96 time 3.9
          42 +seed 151 nobs 2 success True steps 137 time 6.7
          43 +seed 152 nobs 2 success True steps 101 time 2.7
          44 +seed 153 nobs 2 success True steps 160 time 8.4
          45 +seed 154 nobs 0 success True steps 61 time 2.2
          46 +seed 155 nobs 0 success True steps 49 time 2.1
          47 +seed 156 nobs 2 success True steps 141 time 7.5
diff --git a/res_3.txt b/res_3.txt
new file mode 100644
index 0000000..9f7d02d
--- /dev/null
+++ b/res_3.txt
@@ -0,0 +1,39 @@
           1 +seed 160 nobs 0 success True steps 46 time 1.4
           2 +seed 161 nobs 2 success True steps 111 time 3.2
           3 +seed 162 nobs 1 success True steps 110 time 5.4
           4 +seed 163 nobs 1 success True steps 115 time 5.8
           5 +seed 164 nobs 1 success True steps 100 time 3.0
           6 +seed 165 nobs 1 success True steps 126 time 5.7
           7 +seed 166 nobs 2 success True steps 107 time 5.6
           8 +seed 167 nobs 2 success True steps 165 time 8.9
           9 +seed 168 nobs 1 success True steps 129 time 5.5
          10 +seed 169 nobs 2 success True steps 187 time 10.1
          11 +seed 170 nobs 2 success True steps 157 time 8.2
          12 +seed 171 nobs 2 success True steps 161 time 9.0
          13 +seed 172 nobs 1 success True steps 94 time 4.9
          14 +seed 173 nobs 2 success True steps 170 time 8.5
          15 +seed 174 nobs 1 success True steps 101 time 4.3
          16 +seed 175 nobs 2 success True steps 107 time 4.0
          17 +seed 176 nobs 0 success True steps 57 time 2.2
          18 +seed 177 nobs 2 success True steps 119 time 5.8
          19 +seed 178 nobs 1 success True steps 119 time 6.1
          20 +seed 179 nobs 2 success True steps 115 time 4.5
          21 +seed 180 nobs 0 success True steps 57 time 2.3
          22 +seed 181 nobs 2 success True steps 164 time 6.3
          23 +seed 182 nobs 2 success True steps 181 time 9.5
          24 +seed 183 nobs 2 success True steps 179 time 9.6
          25 +seed 184 nobs 1 success True steps 114 time 4.9
          26 +seed 185 nobs 0 success True steps 50 time 2.0
          27 +seed 186 nobs 0 success True steps 46 time 2.0
          28 +seed 187 nobs 1 success True steps 109 time 5.3
          29 +seed 188 nobs 1 success True steps 95 time 4.2
          30 +seed 189 nobs 1 success True steps 131 time 6.3
          31 +seed 190 nobs 0 success True steps 46 time 2.1
          32 +seed 191 nobs 0 success True steps 54 time 1.9
          33 +seed 192 nobs 2 success True steps 163 time 6.5
          34 +seed 193 nobs 1 success True steps 116 time 2.6
          35 +seed 194 nobs 2 success True steps 158 time 7.6
          36 +seed 195 nobs 0 success True steps 50 time 2.0
          37 +seed 196 nobs 0 success True steps 61 time 2.6
          38 +seed 197 nobs 2 success True steps 184 time 8.3
          39 +seed 198 nobs 1 success True steps 119 time 5.8
```

</details>

<a id="C004"></a>
### C004 · Allow partial-overlap grasps near world edge

Commit `9e7bfa8f3930de4f417d9ea9120ddb364481d484`; parents: 536f820f235b80570a659c909d09dd0393026aa0. Recorded author date: 2026-09-30T10:29:41+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0078](01_timeline.md#E0078): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_9e7bfa8_approach.py) · [Exact all-file diff](evidence/diffs/C004_9e7bfa8.diff)

[Previous saved controller snapshot](evidence/versions/C003_536f820_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6d2fd70..2d869ed 100644
--- a/approach.py
+++ b/approach.py
@@ -153,8 +153,8 @@ class GeneratedApproach:
  153    153          return True
  154    154  
  155    155      def _grasp_cands(self, b, pref=None):
  156        -        lo = b[0] + 0.012
  157        -        hi = b[2] - 0.012
         156 +        lo = b[0] + 0.012 - (GH / 2 - 0.02)
         157 +        hi = b[2] - 0.012 + (GH / 2 - 0.02)
  158    158          cx = (b[0] + b[2]) / 2 if pref is None else pref
  159    159          if hi < lo:
  160    160              lo = hi = (b[0] + b[2]) / 2
diff --git a/res_0.txt b/res_0.txt
index ac8b438..cdf493c 100644
--- a/res_0.txt
+++ b/res_0.txt
@@ -26,3 +26,26 @@ seed 34 nobs 0 success True steps 53 time 1.1
   26     26  seed 35 nobs 0 success True steps 51 time 1.6
   27     27  seed 36 nobs 1 success True steps 89 time 3.8
   28     28  seed 37 nobs 0 success True steps 53 time 2.3
          29 +seed 38 nobs 0 success True steps 46 time 1.9
          30 +seed 39 nobs 2 success True steps 175 time 10.1
          31 +seed 40 nobs 1 success True steps 116 time 5.3
          32 +seed 41 nobs 1 success True steps 113 time 2.8
          33 +seed 42 nobs 0 success True steps 48 time 1.3
          34 +seed 43 nobs 1 success True steps 119 time 4.0
          35 +seed 44 nobs 2 success True steps 155 time 7.0
          36 +seed 45 nobs 2 success True steps 170 time 8.6
          37 +seed 46 nobs 1 success True steps 114 time 5.4
          38 +seed 47 nobs 0 success True steps 61 time 0.8
          39 +seed 48 nobs 0 success True steps 47 time 1.0
          40 +seed 49 nobs 0 success True steps 41 time 0.7
          41 +seed 50 nobs 2 success True steps 170 time 2.6
          42 +seed 51 nobs 1 success True steps 102 time 1.2
          43 +seed 52 nobs 2 success True steps 160 time 3.5
          44 +seed 53 nobs 2 success True steps 169 time 3.8
          45 +seed 54 nobs 0 success True steps 59 time 0.4
          46 +seed 55 nobs 2 success True steps 154 time 1.5
          47 +seed 56 nobs 1 success True steps 117 time 1.3
          48 +seed 57 nobs 0 success True steps 41 time 0.4
          49 +seed 58 nobs 1 success True steps 119 time 1.1
          50 +seed 59 nobs 2 success True steps 179 time 1.5
          51 +success 48 / 50
diff --git a/res_1.txt b/res_1.txt
index 0fe513b..51dea27 100644
--- a/res_1.txt
+++ b/res_1.txt
@@ -25,3 +25,27 @@ seed 83 nobs 2 success True steps 174 time 8.6
   25     25  seed 84 nobs 1 success True steps 121 time 5.7
   26     26  seed 85 nobs 2 success True steps 156 time 7.9
   27     27  seed 86 nobs 2 success True steps 95 time 4.4
          28 +seed 87 nobs 1 success True steps 112 time 6.3
          29 +seed 88 nobs 1 success True steps 118 time 5.8
          30 +seed 89 nobs 2 success True steps 112 time 6.9
          31 +seed 90 nobs 1 success True steps 114 time 4.4
          32 +seed 91 nobs 2 success True steps 96 time 3.9
          33 +seed 92 nobs 1 success True steps 112 time 4.9
          34 +seed 93 nobs 2 success True steps 162 time 8.0
          35 +seed 94 nobs 0 success True steps 41 time 1.4
          36 +seed 95 nobs 1 success True steps 106 time 2.8
          37 +seed 96 nobs 2 success True steps 95 time 4.6
          38 +seed 97 nobs 0 success True steps 65 time 2.3
          39 +seed 98 nobs 1 success True steps 108 time 1.5
          40 +seed 99 nobs 2 success True steps 107 time 1.3
          41 +seed 100 nobs 2 success True steps 180 time 2.6
          42 +seed 101 nobs 0 success True steps 42 time 0.6
          43 +seed 102 nobs 1 success True steps 122 time 2.7
          44 +seed 103 nobs 1 success True steps 97 time 1.5
          45 +seed 104 nobs 2 success True steps 165 time 1.9
          46 +seed 105 nobs 0 success True steps 39 time 0.3
          47 +seed 106 nobs 1 success True steps 123 time 1.5
          48 +seed 107 nobs 0 success True steps 48 time 0.6
          49 +seed 108 nobs 0 success True steps 45 time 0.4
          50 +seed 109 nobs 1 success True steps 104 time 1.6
          51 +success 48 / 50
diff --git a/res_2.txt b/res_2.txt
index 72e1cb2..ad1b157 100644
--- a/res_2.txt
+++ b/res_2.txt
@@ -45,3 +45,7 @@ seed 153 nobs 2 success True steps 160 time 8.4
   45     45  seed 154 nobs 0 success True steps 61 time 2.2
   46     46  seed 155 nobs 0 success True steps 49 time 2.1
   47     47  seed 156 nobs 2 success True steps 141 time 7.5
          48 +seed 157 nobs 0 success True steps 52 time 2.1
          49 +seed 158 nobs 1 success True steps 135 time 5.7
          50 +seed 159 nobs 2 success True steps 156 time 8.4
          51 +success 50 / 50
diff --git a/res_3.txt b/res_3.txt
index 9f7d02d..6c248bd 100644
--- a/res_3.txt
+++ b/res_3.txt
@@ -37,3 +37,15 @@ seed 195 nobs 0 success True steps 50 time 2.0
   37     37  seed 196 nobs 0 success True steps 61 time 2.6
   38     38  seed 197 nobs 2 success True steps 184 time 8.3
   39     39  seed 198 nobs 1 success True steps 119 time 5.8
          40 +seed 199 nobs 1 success True steps 105 time 5.0
          41 +seed 200 nobs 0 success True steps 51 time 2.2
          42 +seed 201 nobs 0 success True steps 53 time 1.5
          43 +seed 202 nobs 0 success True steps 57 time 2.0
          44 +seed 203 nobs 0 success True steps 63 time 2.5
          45 +seed 204 nobs 2 success True steps 154 time 7.7
          46 +seed 205 nobs 1 success True steps 107 time 4.2
          47 +seed 206 nobs 1 success True steps 114 time 5.7
          48 +seed 207 nobs 0 success True steps 48 time 1.7
          49 +seed 208 nobs 2 success True steps 112 time 4.7
          50 +seed 209 nobs 2 success True steps 94 time 5.1
          51 +success 50 / 50
diff --git a/trace.py b/trace.py
new file mode 100644
index 0000000..bddd368
--- /dev/null
+++ b/trace.py
@@ -0,0 +1,18 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 300
           6 +env = make_env(); obs, info = env.reset(seed=seed)
           7 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +names=sorted(obs.get_object_names())
           9 +for t in range(N):
          10 +    a = ap.get_action(obs)
          11 +    obs, r, term, trunc, info = env.step(a)
          12 +    R=obs.get_object_from_name('robot')
          13 +    line=f"{t} a={np.round(a,3)} R=({obs.get(R,'x'):.3f},{obs.get(R,'y'):.3f},{obs.get(R,'arm_joint'):.2f})"
          14 +    for n in names:
          15 +        if n in('robot','target_surface'):continue
          16 +        o=obs.get_object_from_name(n); line+=f" {n[:4]}{n[-1]}=({obs.get(o,'x'):.3f},{obs.get(o,'y'):.3f})"
          17 +    print(line)
          18 +    if term: print("TERM"); break
```

</details>

<a id="C005"></a>
### C005 · Better parking spot search (stacking, sweep-based exclusion)

Commit `cd87509345aea40f91463ddbf7f5c6cff8451a8c`; parents: 9e7bfa8f3930de4f417d9ea9120ddb364481d484. Recorded author date: 2026-09-30T10:40:43+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0146](01_timeline.md#E0146): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_cd87509_approach.py) · [Exact all-file diff](evidence/diffs/C005_cd87509.diff)

[Previous saved controller snapshot](evidence/versions/C004_9e7bfa8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2d869ed..4ee334e 100644
--- a/approach.py
+++ b/approach.py
@@ -255,52 +255,65 @@ class GeneratedApproach:
  255    255                  res.append(o)
  256    256          return res
  257    257  
         258 +    def _final_sweep(self):
         259 +        """(rx, ry, final_bb) for the final block placement."""
         260 +        robot, block, surf, obst = self._objs()
         261 +        left, bottom, sb, g = self._final_placement()
         262 +        bb = _rect_bbox(self.state, block)
         263 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         264 +        final_bb = (left, bottom, left + bw, bottom + bh)
         265 +        return left + g, bottom + bh + TIP + 0.003, final_bb
         266 +
  258    267      def _find_spot(self, o):
  259        -        """Find (left, bottom) to park obstruction o."""
         268 +        """Find (left, bottom) to park the (currently grasped) obstruction o."""
  260    269          robot, block, surf, obst = self._objs()
  261    270          s = self.state
  262    271          ob = _rect_bbox(s, o)
  263    272          w, h = ob[2] - ob[0], ob[3] - ob[1]
  264        -        # offset of grasp relative to object left
  265    273          x, y, _, _ = self._rpos()
  266    274          goff = x - ob[0]
         275 +        hang = y - ob[3]  # robot y minus object top
  267    276          sb = _rect_bbox(s, surf)
  268    277          others = self._others_bboxes([o])
  269        -        left_f, bottom_f, _, _ = self._final_placement()
         278 +        frx, fry, fbb = self._final_sweep()
         279 +        # target block pickup sweep
         280 +        _, _, _, g = self._final_placement()
  270    281          bb = _rect_bbox(s, block)
  271        -        bw = bb[2] - bb[0]
  272        -        # forbidden zone around the surface / final block placement
  273        -        fz = (min(sb[0], left_f) - 0.13, max(sb[2], left_f + bw) + 0.13)
  274        -        levels = [FLOOR + 0.005]
         282 +        brx = bb[0] + g
         283 +        bry = bb[3] + TIP + 0.003
         284 +        levels = [(FLOOR + 0.005, 0.0)]
         285 +        for b in others:
         286 +            if b[3] + 0.005 + h < 0.42:
         287 +                levels.append((b[3] + 0.005, 1.0 + b[3]))
  275    288          best = None
  276        -        xs = np.arange(WORLD_X[0] + 0.01, WORLD_X[1] - w - 0.01, 0.01)
  277        -        for bottom in levels:
         289 +        xs = np.arange(WORLD_X[0] + 0.002, WORLD_X[1] - w - 0.002, 0.005)
         290 +        for bottom, pen in levels:
  278    291              for lx in xs:
  279        -                if lx < fz[1] and lx + w > fz[0]:
  280        -                    continue
  281    292                  rx = lx + goff
  282    293                  if rx < RX_MIN or rx > RX_MAX:
  283    294                      continue
  284    295                  cand = (lx, bottom, lx + w, bottom + h)
         296 +                if cand[0] < sb[2] + 0.01 and cand[2] > sb[0] - 0.01:
         297 +                    continue
  285    298                  bad = False
  286    299                  for b in others:
  287        -                    if _overlap(cand, b, 0.02):
         300 +                    if _overlap(cand, b, 0.01):
  288    301                          bad = True
  289    302                          break
  290    303                  if bad:
  291    304                      continue
  292        -                ry = bottom + h + (y - ob[3])
  293        -                if not self._descent_free(rx, ry, cand, others, margin=0.015):
         305 +                if not self._descent_free(frx, fry, fbb, [cand], margin=0.02):
         306 +                    continue
         307 +                if not self._descent_free(brx, bry, None, [cand], margin=0.02):
         308 +                    continue
         309 +                ry = bottom + h + hang
         310 +                if not self._descent_free(rx, ry, cand, others, margin=0.012):
  294    311                      continue
  295        -                cost = abs(rx - x)
         312 +                cost = abs(rx - x) + pen
  296    313                  if best is None or cost < best[0]:
  297    314                      best = (cost, lx, bottom)
  298        -            if best is not None:
  299        -                break
  300    315          if best is None:
  301        -            # fallback: park in the air high above in the far region
  302        -            far = WORLD_X[1] - w - 0.15 if (sb[0] + sb[2]) / 2 < WORLD_X[1] / 2 else 0.15
  303        -            return far, 0.45
         316 +            return None
  304    317          return best[1], best[2]
  305    318  
  306    319      def _plan(self):
@@ -323,7 +336,12 @@ class GeneratedApproach:
  323    336                  if not ok:
  324    337                      failures += 1
  325    338                      continue
  326        -                left, bottom = self._find_spot(o)
         339 +                spot = self._find_spot(o)
         340 +                if spot is None:
         341 +                    # put it back where it was
         342 +                    spot = (_rect_bbox(self.state, o)[0], FLOOR + 0.005)
         343 +                    failures += 1
         344 +                left, bottom = spot
  327    345                  yield from self._place_at(o, left, bottom)
  328    346                  self.vac = 0.0
  329    347                  yield self._act()
diff --git a/c3.txt b/c3.txt
new file mode 100644
index 0000000..fc61cda
--- /dev/null
+++ b/c3.txt
@@ -0,0 +1,41 @@
           1 +seed 200 nobs 3 success True steps 181 time 11.3
           2 +seed 201 nobs 3 success True steps 176 time 12.5
           3 +seed 202 nobs 3 success True steps 175 time 12.9
           4 +seed 203 nobs 3 success True steps 238 time 16.9
           5 +seed 204 nobs 3 success True steps 182 time 10.2
           6 +seed 205 nobs 3 success True steps 217 time 14.1
           7 +seed 206 nobs 3 success True steps 180 time 14.6
           8 +seed 207 nobs 3 success True steps 220 time 15.3
           9 +seed 208 nobs 3 success True steps 164 time 11.4
          10 +seed 209 nobs 3 success True steps 94 time 6.2
          11 +seed 210 nobs 3 success True steps 246 time 15.3
          12 +seed 211 nobs 3 success True steps 183 time 12.6
          13 +seed 212 nobs 3 success True steps 135 time 9.8
          14 +seed 213 nobs 3 success True steps 162 time 8.6
          15 +seed 214 nobs 3 success True steps 170 time 10.3
          16 +seed 215 nobs 3 success True steps 216 time 15.3
          17 +seed 216 nobs 3 success True steps 188 time 12.6
          18 +seed 217 nobs 3 success True steps 153 time 8.6
          19 +seed 218 nobs 3 success True steps 183 time 9.8
          20 +seed 219 nobs 3 success True steps 173 time 10.1
          21 +seed 220 nobs 3 success True steps 186 time 9.8
          22 +seed 221 nobs 3 success True steps 179 time 11.1
          23 +seed 222 nobs 3 success True steps 165 time 5.0
          24 +seed 223 nobs 3 success True steps 209 time 7.3
          25 +seed 224 nobs 3 success True steps 113 time 4.8
          26 +seed 225 nobs 3 success True steps 175 time 4.1
          27 +seed 226 nobs 3 success True steps 161 time 6.4
          28 +seed 227 nobs 3 success True steps 106 time 3.2
          29 +seed 228 nobs 3 success True steps 169 time 6.6
          30 +seed 229 nobs 3 success True steps 223 time 8.6
          31 +seed 230 nobs 3 success True steps 113 time 3.1
          32 +seed 231 nobs 3 success True steps 226 time 6.4
          33 +seed 232 nobs 3 success True steps 173 time 5.7
          34 +seed 233 nobs 3 success True steps 123 time 5.0
          35 +seed 234 nobs 3 success True steps 171 time 6.2
          36 +seed 235 nobs 3 success True steps 156 time 5.0
          37 +seed 236 nobs 3 success True steps 166 time 5.5
          38 +seed 237 nobs 3 success True steps 197 time 6.8
          39 +seed 238 nobs 3 success True steps 220 time 9.5
          40 +seed 239 nobs 3 success True steps 187 time 6.1
          41 +success 40 / 40
diff --git a/c4.txt b/c4.txt
new file mode 100644
index 0000000..0cb9db7
--- /dev/null
+++ b/c4.txt
@@ -0,0 +1,41 @@
           1 +seed 100 nobs 4 success True steps 232 time 17.1
           2 +seed 101 nobs 4 success True steps 259 time 18.3
           3 +seed 102 nobs 4 success True steps 175 time 11.2
           4 +seed 103 nobs 4 success True steps 247 time 16.2
           5 +seed 104 nobs 4 success True steps 246 time 17.2
           6 +seed 105 nobs 4 success True steps 191 time 14.2
           7 +seed 106 nobs 4 success True steps 220 time 14.8
           8 +seed 107 nobs 4 success True steps 161 time 11.2
           9 +seed 108 nobs 4 success True steps 203 time 11.9
          10 +seed 109 nobs 4 success True steps 187 time 9.4
          11 +seed 110 nobs 4 success True steps 178 time 10.9
          12 +seed 111 nobs 4 success True steps 163 time 5.3
          13 +seed 112 nobs 4 success True steps 173 time 5.7
          14 +seed 113 nobs 4 success True steps 211 time 7.7
          15 +seed 114 nobs 4 success True steps 170 time 7.2
          16 +seed 115 nobs 4 success True steps 233 time 7.3
          17 +seed 116 nobs 4 success True steps 249 time 8.7
          18 +seed 117 nobs 4 success True steps 241 time 9.0
          19 +seed 118 nobs 4 success True steps 223 time 7.0
          20 +seed 119 nobs 4 success True steps 213 time 4.2
          21 +seed 120 nobs 4 success True steps 250 time 3.2
          22 +seed 121 nobs 4 success True steps 159 time 0.9
          23 +seed 122 nobs 4 success True steps 208 time 1.1
          24 +seed 123 nobs 4 success True steps 123 time 0.7
          25 +seed 124 nobs 4 success True steps 274 time 1.4
          26 +seed 125 nobs 4 success True steps 112 time 0.7
          27 +seed 126 nobs 4 success True steps 218 time 1.2
          28 +seed 127 nobs 4 success True steps 254 time 1.1
          29 +seed 128 nobs 4 success True steps 217 time 1.1
          30 +seed 129 nobs 4 success True steps 169 time 0.9
          31 +seed 130 nobs 4 success False steps 1000 time 4.3
          32 +seed 131 nobs 4 success True steps 93 time 0.4
          33 +seed 132 nobs 4 success True steps 160 time 0.8
          34 +seed 133 nobs 4 success True steps 222 time 1.1
          35 +seed 134 nobs 4 success True steps 236 time 1.1
          36 +seed 135 nobs 4 success True steps 205 time 1.1
          37 +seed 136 nobs 4 success True steps 170 time 0.8
          38 +seed 137 nobs 4 success True steps 239 time 1.0
          39 +seed 138 nobs 4 success True steps 285 time 1.5
          40 +seed 139 nobs 4 success True steps 234 time 1.1
          41 +success 39 / 40
diff --git a/c5.txt b/c5.txt
new file mode 100644
index 0000000..0682116
--- /dev/null
+++ b/c5.txt
@@ -0,0 +1,13 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/test_approach.py", line 23, in <module>
           3 +    term, steps, n, dt = run(s, count=cnt)
           4 +                         ^^^^^^^^^^^^^^^^^
           5 +  File "/sandbox/test_approach.py", line 7, in run
           6 +    obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
           7 +                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           8 +  File "/sandbox/env_client.py", line 525, in reset
           9 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          10 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          11 +  File "/sandbox/env_client.py", line 478, in _request
          12 +    raise RuntimeError("Connection to the environment server was closed")
          13 +RuntimeError: Connection to the environment server was closed
diff --git a/cd.txt b/cd.txt
new file mode 100644
index 0000000..9c75310
--- /dev/null
+++ b/cd.txt
@@ -0,0 +1,101 @@
           1 +seed 300 nobs 0 success True steps 50 time 2.0
           2 +seed 301 nobs 0 success True steps 80 time 3.1
           3 +seed 302 nobs 2 success True steps 155 time 9.5
           4 +seed 303 nobs 1 success True steps 134 time 8.0
           5 +seed 304 nobs 2 success True steps 169 time 5.6
           6 +seed 305 nobs 0 success True steps 49 time 2.4
           7 +seed 306 nobs 2 success True steps 163 time 9.5
           8 +seed 307 nobs 2 success True steps 187 time 11.6
           9 +seed 308 nobs 1 success True steps 110 time 7.2
          10 +seed 309 nobs 1 success True steps 125 time 4.4
          11 +seed 310 nobs 0 success True steps 44 time 1.7
          12 +seed 311 nobs 1 success True steps 117 time 6.8
          13 +seed 312 nobs 0 success True steps 74 time 5.0
          14 +seed 313 nobs 0 success True steps 48 time 3.1
          15 +seed 314 nobs 1 success True steps 66 time 4.0
          16 +seed 315 nobs 1 success True steps 41 time 2.3
          17 +seed 316 nobs 0 success True steps 48 time 2.9
          18 +seed 317 nobs 0 success True steps 41 time 2.0
          19 +seed 318 nobs 0 success True steps 74 time 3.2
          20 +seed 319 nobs 2 success True steps 113 time 5.8
          21 +seed 320 nobs 0 success True steps 39 time 1.8
          22 +seed 321 nobs 1 success True steps 101 time 4.9
          23 +seed 322 nobs 0 success True steps 46 time 2.3
          24 +seed 323 nobs 2 success True steps 115 time 8.2
          25 +seed 324 nobs 1 success True steps 132 time 7.4
          26 +seed 325 nobs 0 success True steps 48 time 2.8
          27 +seed 326 nobs 0 success True steps 75 time 4.2
          28 +seed 327 nobs 1 success True steps 104 time 6.8
          29 +seed 328 nobs 0 success True steps 40 time 1.7
          30 +seed 329 nobs 2 success True steps 165 time 9.1
          31 +seed 330 nobs 1 success True steps 117 time 1.9
          32 +seed 331 nobs 0 success True steps 38 time 1.4
          33 +seed 332 nobs 1 success True steps 103 time 6.8
          34 +seed 333 nobs 0 success True steps 34 time 1.9
          35 +seed 334 nobs 1 success True steps 93 time 5.4
          36 +seed 335 nobs 0 success True steps 44 time 2.2
          37 +seed 336 nobs 1 success True steps 119 time 6.2
          38 +seed 337 nobs 0 success True steps 81 time 3.7
          39 +seed 338 nobs 1 success True steps 98 time 5.9
          40 +seed 339 nobs 0 success True steps 62 time 4.5
          41 +seed 340 nobs 0 success True steps 42 time 1.7
          42 +seed 341 nobs 2 success True steps 99 time 6.2
          43 +seed 342 nobs 2 success True steps 191 time 10.7
          44 +seed 343 nobs 0 success True steps 58 time 2.4
          45 +seed 344 nobs 0 success True steps 59 time 3.2
          46 +seed 345 nobs 0 success True steps 58 time 3.4
          47 +seed 346 nobs 1 success True steps 133 time 6.3
          48 +seed 347 nobs 2 success True steps 96 time 5.4
          49 +seed 348 nobs 0 success True steps 52 time 1.8
          50 +seed 349 nobs 2 success True steps 105 time 5.0
          51 +seed 350 nobs 1 success True steps 98 time 4.9
          52 +seed 351 nobs 1 success True steps 120 time 4.6
          53 +seed 352 nobs 0 success True steps 61 time 2.7
          54 +seed 353 nobs 0 success True steps 45 time 1.6
          55 +seed 354 nobs 2 success True steps 177 time 8.0
          56 +seed 355 nobs 1 success True steps 57 time 2.5
          57 +seed 356 nobs 0 success True steps 54 time 1.2
          58 +seed 357 nobs 1 success True steps 125 time 6.2
          59 +seed 358 nobs 2 success True steps 140 time 8.1
          60 +seed 359 nobs 1 success True steps 109 time 4.6
          61 +seed 360 nobs 2 success True steps 155 time 4.0
          62 +seed 361 nobs 2 success True steps 162 time 5.5
          63 +seed 362 nobs 2 success True steps 163 time 5.2
          64 +seed 363 nobs 0 success True steps 66 time 1.9
          65 +seed 364 nobs 1 success True steps 108 time 1.7
          66 +seed 365 nobs 0 success True steps 71 time 1.8
          67 +seed 366 nobs 0 success True steps 45 time 1.1
          68 +seed 367 nobs 2 success True steps 199 time 7.2
          69 +seed 368 nobs 2 success True steps 151 time 3.8
          70 +seed 369 nobs 2 success True steps 163 time 5.3
          71 +seed 370 nobs 1 success True steps 114 time 1.8
          72 +seed 371 nobs 2 success True steps 97 time 3.2
          73 +seed 372 nobs 1 success True steps 137 time 3.4
          74 +seed 373 nobs 1 success True steps 118 time 2.1
          75 +seed 374 nobs 2 success True steps 165 time 4.7
          76 +seed 375 nobs 0 success True steps 51 time 1.1
          77 +seed 376 nobs 1 success True steps 118 time 4.1
          78 +seed 377 nobs 2 success True steps 132 time 3.4
          79 +seed 378 nobs 1 success True steps 141 time 4.5
          80 +seed 379 nobs 2 success True steps 166 time 6.3
          81 +seed 380 nobs 1 success True steps 123 time 2.9
          82 +seed 381 nobs 2 success True steps 133 time 3.2
          83 +seed 382 nobs 0 success True steps 67 time 1.4
          84 +seed 383 nobs 0 success True steps 63 time 1.8
          85 +seed 384 nobs 0 success True steps 64 time 2.0
          86 +seed 385 nobs 2 success True steps 140 time 4.6
          87 +seed 386 nobs 1 success True steps 104 time 3.3
          88 +seed 387 nobs 1 success True steps 113 time 3.2
          89 +seed 388 nobs 1 success True steps 106 time 3.9
          90 +seed 389 nobs 0 success True steps 53 time 1.6
          91 +seed 390 nobs 1 success True steps 122 time 3.7
          92 +seed 391 nobs 0 success True steps 66 time 2.3
          93 +seed 392 nobs 2 success True steps 101 time 3.0
          94 +seed 393 nobs 2 success True steps 46 time 1.3
          95 +seed 394 nobs 0 success True steps 44 time 1.5
          96 +seed 395 nobs 1 success True steps 131 time 2.3
          97 +seed 396 nobs 1 success True steps 134 time 2.5
          98 +seed 397 nobs 2 success True steps 159 time 2.8
          99 +seed 398 nobs 2 success True steps 97 time 1.0
         100 +seed 399 nobs 2 success True steps 165 time 1.6
         101 +success 100 / 100
diff --git a/cnt_3.txt b/cnt_3.txt
new file mode 100644
index 0000000..295924d
--- /dev/null
+++ b/cnt_3.txt
@@ -0,0 +1,4 @@
           1 +seed 0 nobs 3 success True steps 105 time 4.6
           2 +seed 1 nobs 3 success True steps 177 time 9.8
           3 +seed 2 nobs 3 success True steps 187 time 10.0
           4 +success 3 / 3
diff --git a/cnt_4.txt b/cnt_4.txt
new file mode 100644
index 0000000..c14d154
--- /dev/null
+++ b/cnt_4.txt
@@ -0,0 +1,4 @@
           1 +seed 0 nobs 4 success True steps 160 time 8.6
           2 +seed 1 nobs 4 success True steps 214 time 9.0
           3 +seed 2 nobs 4 success True steps 179 time 6.6
           4 +success 3 / 3
diff --git a/cnt_6.txt b/cnt_6.txt
new file mode 100644
index 0000000..42485f0
--- /dev/null
+++ b/cnt_6.txt
@@ -0,0 +1,13 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/test_approach.py", line 23, in <module>
           3 +    term, steps, n, dt = run(s, count=cnt)
           4 +                         ^^^^^^^^^^^^^^^^^
           5 +  File "/sandbox/test_approach.py", line 7, in run
           6 +    obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
           7 +                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           8 +  File "/sandbox/env_client.py", line 525, in reset
           9 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          10 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          11 +  File "/sandbox/env_client.py", line 481, in _request
          12 +    raise RuntimeError(f"Environment server error: {response['error']}")
          13 +RuntimeError: Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts.
diff --git a/cnt_8.txt b/cnt_8.txt
new file mode 100644
index 0000000..f18b7e3
--- /dev/null
+++ b/cnt_8.txt
@@ -0,0 +1,13 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/test_approach.py", line 23, in <module>
           3 +    term, steps, n, dt = run(s, count=cnt)
           4 +                         ^^^^^^^^^^^^^^^^^
           5 +  File "/sandbox/test_approach.py", line 7, in run
           6 +    obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
           7 +                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           8 +  File "/sandbox/env_client.py", line 525, in reset
           9 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          10 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          11 +  File "/sandbox/env_client.py", line 481, in _request
          12 +    raise RuntimeError(f"Environment server error: {response['error']}")
          13 +RuntimeError: Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=8; it likely exceeds the family's feasible object count. Lower the configured counts.
diff --git a/dump2.py b/dump2.py
new file mode 100644
index 0000000..4539a4a
--- /dev/null
+++ b/dump2.py
@@ -0,0 +1,9 @@
           1 +from env_client import make_env
           2 +import sys
           3 +env = make_env()
           4 +seed=int(sys.argv[1]); cnt=int(sys.argv[2]) if len(sys.argv)>2 else None
           5 +obs, info = env.reset(seed=seed, options={'object_count':cnt} if cnt else None)
           6 +for n in sorted(obs.get_object_names()):
           7 +    o=obs.get_object_from_name(n)
           8 +    fs=["x","y","width","height"] if n!='robot' else ['x','y']
           9 +    print(n, {f: round(float(obs.get(o,f)),3) for f in fs})
diff --git a/test_approach.py b/test_approach.py
index f2cd0e6..1457b4b 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -2,9 +2,9 @@ import sys, time
    2      2  import numpy as np
    3      3  from env_client import make_env
    4      4  from approach import GeneratedApproach
    5        -def run(seed, verbose=False):
           5 +def run(seed, verbose=False, count=None):
    6      6      env = make_env()
    7        -    obs, info = env.reset(seed=seed)
           7 +    obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
    8      8      ap = GeneratedApproach(env.action_space, env.observation_space, {})
    9      9      ap.reset(obs, info)
   10     10      n_obs = len(obs.get_object_names()) - 3
@@ -17,9 +17,10 @@ def run(seed, verbose=False):
   17     17      return term, t+1, n_obs, time.time()-t0
   18     18  if __name__ == "__main__":
   19     19      s0, s1 = int(sys.argv[1]), int(sys.argv[2])
          20 +    cnt = int(sys.argv[3]) if len(sys.argv) > 3 else None
   20     21      succ=0
   21     22      for s in range(s0, s1):
   22        -        term, steps, n, dt = run(s)
          23 +        term, steps, n, dt = run(s, count=cnt)
   23     24          succ += term
   24     25          print(f"seed {s} nobs {n} success {term} steps {steps} time {dt:.1f}", flush=True)
   25     26      print("success", succ, "/", s1-s0)
diff --git a/trace.py b/trace.py
index bddd368..4e823f8 100644
--- a/trace.py
+++ b/trace.py
@@ -2,8 +2,8 @@ import sys
    2      2  import numpy as np
    3      3  from env_client import make_env
    4      4  from approach import GeneratedApproach
    5        -seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 300
    6        -env = make_env(); obs, info = env.reset(seed=seed)
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2]); C=int(sys.argv[3]) if len(sys.argv)>3 else None
           6 +env = make_env(); obs, info = env.reset(seed=seed, options={'object_count':C} if C else None)
    7      7  ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    8      8  names=sorted(obs.get_object_names())
    9      9  for t in range(N):
```

</details>

<a id="C006"></a>
### C006 · Motion planner: diagonal collision-checked paths, grasp on final descent step

Commit `e24e591f5ef916db93a0aa99a7696779e41d0f66`; parents: cd87509345aea40f91463ddbf7f5c6cff8451a8c. Recorded author date: 2026-09-30T10:42:17+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0166](01_timeline.md#E0166): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_e24e591_approach.py) · [Exact all-file diff](evidence/diffs/C006_e24e591.diff)

[Previous saved controller snapshot](evidence/versions/C005_cd87509_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4ee334e..1f918f2 100644
--- a/approach.py
+++ b/approach.py
@@ -88,7 +88,7 @@ class GeneratedApproach:
   88     88          return np.array([dx, dy, dth, darm, self.vac], dtype=np.float32)
   89     89  
   90     90      def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200):
   91        -        """Move towards (tx, ty); yields actions. Returns True on success."""
          91 +        """Straight-line move towards (tx, ty). Returns True on success."""
   92     92          stuck = 0
   93     93          last = None
   94     94          for _ in range(max_steps):
@@ -96,30 +96,104 @@ class GeneratedApproach:
   96     96              gx = x if tx is None else tx
   97     97              gy = y if ty is None else ty
   98     98              ex, ey = gx - x, gy - y
          99 +            eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
         100 +            ea = ARM - aj
   99    101              if abs(ex) <= tol and abs(ey) <= tol:
  100        -                return True
  101        -            if last is not None and abs(last[0] - x) < 1e-7 and abs(last[1] - y) < 1e-7:
         102 +                if abs(eth) < 1e-4 and abs(ea) < 1e-4:
         103 +                    return True
         104 +            if last is not None and abs(last[0] - x) < 1e-7 and abs(last[1] - y) < 1e-7 \
         105 +                    and abs(last[2] - aj) < 1e-7 and abs(last[3] - th) < 1e-7:
  102    106                  stuck += 1
  103    107                  if stuck >= 2:
  104    108                      return False
  105    109              else:
  106    110                  stuck = 0
  107        -            last = (x, y)
  108        -            yield self._act(float(np.clip(ex, -0.05, 0.05)), float(np.clip(ey, -0.05, 0.05)))
         111 +            last = (x, y, aj, th)
         112 +            n = max(1, int(math.ceil(max(abs(ex), abs(ey)) / 0.05 - 1e-6)))
         113 +            yield np.array([ex / n, ey / n, np.clip(eth, -0.19, 0.19),
         114 +                            np.clip(ea, -0.1, 0.1), self.vac], dtype=np.float32)
  109    115          return False
  110    116  
  111        -    def _setup_pose(self):
  112        -        # rise, orient downwards, extend arm
  113        -        x, y, th, aj = self._rpos()
  114        -        yield from self._goto(None, ROBOT_Y_MAX)
  115        -        for _ in range(60):
  116        -            x, y, th, aj = self._rpos()
  117        -            eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
  118        -            ea = ARM - aj
  119        -            if abs(eth) < 1e-4 and abs(ea) < 1e-4:
  120        -                break
  121        -            yield np.array([0, 0, np.clip(eth, -0.19, 0.19), np.clip(ea, -0.1, 0.1), self.vac],
  122        -                           dtype=np.float32)
         117 +    def _collides(self, x, y, obstacles, crel, m=0.008):
         118 +        if y > ROBOT_Y_MAX + 1e-6 or x < RX_MIN - 1e-6 or x > RX_MAX + 1e-6:
         119 +            return True
         120 +        col = (x - GH / 2, y - TIP, x + GH / 2, y)
         121 +        cb = None
         122 +        if crel is not None:
         123 +            cb = (x + crel[0], y + crel[1], x + crel[2], y + crel[3])
         124 +            if cb[1] < FLOOR - 1e-3:
         125 +                return True
         126 +        for b in obstacles:
         127 +            if _circle_rect_dist(x, y, b) < BASE_R + m:
         128 +                return True
         129 +            if _overlap(col, b, 0.001):
         130 +                return True
         131 +            if cb is not None and _overlap(cb, b, m * 0.6):
         132 +                return True
         133 +        return False
         134 +
         135 +    def _seg_free(self, p, q, obstacles, crel):
         136 +        d = max(abs(q[0] - p[0]), abs(q[1] - p[1]))
         137 +        n = max(1, int(math.ceil(d / 0.008)))
         138 +        for i in range(1, n + 1):
         139 +            t = i / n
         140 +            if self._collides(p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]), obstacles, crel):
         141 +                return False
         142 +        return True
         143 +
         144 +    def _plan_path(self, x1, y1, obstacles, crel):
         145 +        x0, y0, _, _ = self._rpos()
         146 +        p0 = (x0, y0)
         147 +        if self._seg_free(p0, (x1, y1), obstacles, crel):
         148 +            return [(x1, y1)]
         149 +        dx = x1 - x0
         150 +        sg = 1.0 if dx >= 0 else -1.0
         151 +        tys = sorted(set([round(v, 4) for v in np.arange(max(y0, y1) + 0.01, ROBOT_Y_MAX, 0.02)]
         152 +                         + [ROBOT_Y_MAX]))
         153 +        for ty in tys:
         154 +            a = min(abs(dx), ty - y0)
         155 +            b = min(abs(dx) - a, ty - y1)
         156 +            pa = (x0 + sg * a, ty)
         157 +            pb = (x1 - sg * b, ty)
         158 +            path = [pa, pb, (x1, y1)]
         159 +            pts = [p0] + path
         160 +            if all(self._seg_free(pts[i], pts[i + 1], obstacles, crel) for i in range(3)):
         161 +                return path
         162 +            path = [(x0, ty), (x1, ty), (x1, y1)]
         163 +            pts = [p0] + path
         164 +            if all(self._seg_free(pts[i], pts[i + 1], obstacles, crel) for i in range(3)):
         165 +                return path
         166 +        return [(x0, ROBOT_Y_MAX), (x1, ROBOT_Y_MAX), (x1, y1)]
         167 +
         168 +    def _move(self, x1, y1, carried=None, last_vac=None):
         169 +        """Plan & execute a collision-free path. carried: grasped object or None."""
         170 +        x0, y0, _, _ = self._rpos()
         171 +        excl = [carried] if carried is not None else []
         172 +        obstacles = self._others_bboxes(excl)
         173 +        robot, block, surf, obst = self._objs()
         174 +        obstacles.append(_rect_bbox(self.state, surf))
         175 +        crel = None
         176 +        if carried is not None:
         177 +            cb = _rect_bbox(self.state, carried)
         178 +            crel = (cb[0] - x0, cb[1] - y0, cb[2] - x0, cb[3] - y0)
         179 +        path = self._plan_path(x1, y1, obstacles, crel)
         180 +        for i, (px, py) in enumerate(path):
         181 +            if last_vac is not None and i == len(path) - 1:
         182 +                # final segment: run all but last step, then set vacuum on last step
         183 +                gen = self._goto(px, py)
         184 +                while True:
         185 +                    x, y, _, _ = self._rpos()
         186 +                    if max(abs(px - x), abs(py - y)) <= 0.05 + 1e-6:
         187 +                        break
         188 +                    try:
         189 +                        yield next(gen)
         190 +                    except StopIteration:
         191 +                        break
         192 +                self.vac = last_vac
         193 +            ok = yield from self._goto(px, py)
         194 +            if not ok:
         195 +                return False
         196 +        return True
  123    197  
  124    198      # ------------------------------------------------------------------
  125    199      def _others_bboxes(self, exclude):
@@ -186,30 +260,32 @@ class GeneratedApproach:
  186    260          if gx is None:
  187    261              return False
  188    262          b = _rect_bbox(self.state, o)
  189        -        yield from self._goto(None, ROBOT_Y_MAX)
  190        -        yield from self._goto(gx, None)
  191    263          ry = b[3] + TIP + 0.003
  192        -        yield from self._goto(None, ry, tol=1e-4)
         264 +        yield from self._move(gx, ry, None, last_vac=1.0)
  193    265          self.vac = 1.0
  194        -        yield self._act()
  195        -        yield self._act()
  196        -        yield from self._goto(None, ROBOT_Y_MAX)
  197        -        nb = _rect_bbox(self.state, o)
  198        -        if nb[1] < b[1] + 0.05:
  199        -            self.vac = 0.0
  200        -            yield self._act()
  201        -            return False
  202    266          return True
  203    267  
  204        -    def _place_at(self, o, target_left, target_bottom):
  205        -        x, y, _, _ = self._rpos()
  206        -        b = _rect_bbox(self.state, o)
  207        -        rx = x + (target_left - b[0])
  208        -        yield from self._goto(rx, None)
         268 +    def _place_at(self, o, target_left, target_bottom, check=True):
  209    269          x, y, _, _ = self._rpos()
  210        -        b = _rect_bbox(self.state, o)
  211        -        ry = y - (b[1] - target_bottom)
  212        -        yield from self._goto(None, ry, tol=1e-4)
         270 +        b0 = _rect_bbox(self.state, o)
         271 +        rx = x + (target_left - b0[0])
         272 +        ry = y - (b0[1] - target_bottom)
         273 +        gen = self._move(rx, ry, o)
         274 +        first = True
         275 +        while True:
         276 +            try:
         277 +                a = next(gen)
         278 +            except StopIteration as e:
         279 +                return True
         280 +            yield a
         281 +            if first and check:
         282 +                first = False
         283 +                nb = _rect_bbox(self.state, o)
         284 +                if abs(nb[0] - b0[0]) + abs(nb[1] - b0[1]) < 1e-6:
         285 +                    # grasp failed
         286 +                    self.vac = 0.0
         287 +                    yield self._act()
         288 +                    return False
  213    289  
  214    290      # ------------------------------------------------------------------
  215    291      def _final_placement(self):
@@ -318,15 +394,14 @@ class GeneratedApproach:
  318    394  
  319    395      def _plan(self):
  320    396          self.vac = 0.0
  321        -        yield from self._setup_pose()
  322    397          failures = 0
  323    398          for _ in range(30):
  324    399              blockers = self._blocking()
  325    400              if not blockers:
  326    401                  break
  327        -            # pick blockers in order of height (tallest first) that are graspable
  328    402              robot, block, surf, obst = self._objs()
  329        -            blockers.sort(key=lambda o: -_rect_bbox(self.state, o)[3])
         403 +            x, y, _, _ = self._rpos()
         404 +            blockers.sort(key=lambda o: (-_rect_bbox(self.state, o)[3]))
  330    405              picked = False
  331    406              for o in blockers:
  332    407                  others = self._others_bboxes([o])
@@ -338,14 +413,15 @@ class GeneratedApproach:
  338    413                      continue
  339    414                  spot = self._find_spot(o)
  340    415                  if spot is None:
  341        -                    # put it back where it was
  342    416                      spot = (_rect_bbox(self.state, o)[0], FLOOR + 0.005)
  343    417                      failures += 1
  344    418                  left, bottom = spot
  345        -                yield from self._place_at(o, left, bottom)
         419 +                ok = yield from self._place_at(o, left, bottom)
  346    420                  self.vac = 0.0
  347    421                  yield self._act()
  348        -                yield from self._goto(None, ROBOT_Y_MAX)
         422 +                if not ok:
         423 +                    failures += 1
         424 +                    continue
  349    425                  picked = True
  350    426                  break
  351    427              if not picked:
@@ -353,15 +429,19 @@ class GeneratedApproach:
  353    429                  if failures > 5:
  354    430                      break
  355    431          # now the target block
         432 +        robot, block, surf, obst = self._objs()
  356    433          for _ in range(10):
  357        -            robot, block, surf, obst = self._objs()
  358    434              left, bottom, sb, g = self._final_placement()
  359    435              bb = _rect_bbox(self.state, block)
  360    436              ok = yield from self._pick(block, pref=bb[0] + g)
         437 +            if not ok:
         438 +                self.vac = 0.0
         439 +                yield self._act()
         440 +                continue
         441 +            left, bottom, sb, g = self._final_placement()
         442 +            ok = yield from self._place_at(block, left, bottom)
  361    443              if ok:
  362    444                  break
  363        -        left, bottom, sb, g = self._final_placement()
  364        -        yield from self._place_at(block, left, bottom)
  365    445          self.vac = 0.0
  366    446          for _ in range(5):
  367    447              yield self._act()
diff --git a/approach_v1.py b/approach_v1.py
new file mode 100644
index 0000000..4ee334e
--- /dev/null
+++ b/approach_v1.py
@@ -0,0 +1,367 @@
           1 +import math
           2 +import numpy as np
           3 +
           4 +WORLD_X = (0.0, 1.618)
           5 +ROBOT_Y_MAX = 0.895
           6 +FLOOR = 0.1
           7 +ARM = 0.2          # extended arm length we use
           8 +GW = 0.01          # gripper width (along arm)
           9 +GH = 0.07          # gripper height (perpendicular)
          10 +BASE_R = 0.1
          11 +RX_MIN = 0.1 + 0.002
          12 +RX_MAX = 1.618 - 0.1 - 0.002
          13 +TIP = ARM + GW     # distance from robot center to gripper tip (pointing down)
          14 +
          15 +
          16 +def _rect_bbox(state, o):
          17 +    x = float(state.get(o, "x")); y = float(state.get(o, "y"))
          18 +    w = float(state.get(o, "width")); h = float(state.get(o, "height"))
          19 +    th = float(state.get(o, "theta"))
          20 +    if abs(th) < 1e-6:
          21 +        return (x, y, x + w, y + h)
          22 +    c, s = math.cos(th), math.sin(th)
          23 +    pts = [(x, y), (x + w * c, y + w * s), (x - h * s, y + h * c),
          24 +           (x + w * c - h * s, y + w * s + h * c)]
          25 +    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
          26 +    return (min(xs), min(ys), max(xs), max(ys))
          27 +
          28 +
          29 +def _circle_rect_dist(cx, cy, b):
          30 +    dx = max(b[0] - cx, 0.0, cx - b[2])
          31 +    dy = max(b[1] - cy, 0.0, cy - b[3])
          32 +    return math.hypot(dx, dy)
          33 +
          34 +
          35 +def _overlap(a, b, m=0.0):
          36 +    return a[0] < b[2] + m and b[0] < a[2] + m and a[1] < b[3] + m and b[1] < a[3] + m
          37 +
          38 +
          39 +class GeneratedApproach:
          40 +    def __init__(self, action_space, observation_space, primitives):
          41 +        self.low = np.array(action_space.low, dtype=np.float32)
          42 +        self.high = np.array(action_space.high, dtype=np.float32)
          43 +
          44 +    # ------------------------------------------------------------------
          45 +    def reset(self, state, info):
          46 +        self.state = state
          47 +        self.gen = self._plan()
          48 +        self.vac = 0.0
          49 +
          50 +    def get_action(self, state):
          51 +        self.state = state
          52 +        try:
          53 +            a = next(self.gen)
          54 +        except StopIteration:
          55 +            self.gen = self._plan()
          56 +            try:
          57 +                a = next(self.gen)
          58 +            except StopIteration:
          59 +                a = np.zeros(5, dtype=np.float32)
          60 +        a = np.clip(np.asarray(a, dtype=np.float32), self.low, self.high)
          61 +        return a
          62 +
          63 +    # ------------------------------------------------------------------
          64 +    def _objs(self):
          65 +        s = self.state
          66 +        robot = None; block = None; surf = None; obst = []
          67 +        for n in sorted(s.get_object_names()):
          68 +            o = s.get_object_from_name(n)
          69 +            tn = o.type.name
          70 +            if tn == "crv_robot":
          71 +                robot = o
          72 +            elif tn == "target_block":
          73 +                block = o
          74 +            elif tn == "target_surface":
          75 +                surf = o
          76 +            else:
          77 +                obst.append(o)
          78 +        return robot, block, surf, obst
          79 +
          80 +    def _rpos(self):
          81 +        r = self._objs()[0]
          82 +        s = self.state
          83 +        return (float(s.get(r, "x")), float(s.get(r, "y")),
          84 +                float(s.get(r, "theta")), float(s.get(r, "arm_joint")))
          85 +
          86 +    # ------------------------------------------------------------------
          87 +    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0):
          88 +        return np.array([dx, dy, dth, darm, self.vac], dtype=np.float32)
          89 +
          90 +    def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200):
          91 +        """Move towards (tx, ty); yields actions. Returns True on success."""
          92 +        stuck = 0
          93 +        last = None
          94 +        for _ in range(max_steps):
          95 +            x, y, th, aj = self._rpos()
          96 +            gx = x if tx is None else tx
          97 +            gy = y if ty is None else ty
          98 +            ex, ey = gx - x, gy - y
          99 +            if abs(ex) <= tol and abs(ey) <= tol:
         100 +                return True
         101 +            if last is not None and abs(last[0] - x) < 1e-7 and abs(last[1] - y) < 1e-7:
         102 +                stuck += 1
         103 +                if stuck >= 2:
         104 +                    return False
         105 +            else:
         106 +                stuck = 0
         107 +            last = (x, y)
         108 +            yield self._act(float(np.clip(ex, -0.05, 0.05)), float(np.clip(ey, -0.05, 0.05)))
         109 +        return False
         110 +
         111 +    def _setup_pose(self):
         112 +        # rise, orient downwards, extend arm
         113 +        x, y, th, aj = self._rpos()
         114 +        yield from self._goto(None, ROBOT_Y_MAX)
         115 +        for _ in range(60):
         116 +            x, y, th, aj = self._rpos()
         117 +            eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
         118 +            ea = ARM - aj
         119 +            if abs(eth) < 1e-4 and abs(ea) < 1e-4:
         120 +                break
         121 +            yield np.array([0, 0, np.clip(eth, -0.19, 0.19), np.clip(ea, -0.1, 0.1), self.vac],
         122 +                           dtype=np.float32)
         123 +
         124 +    # ------------------------------------------------------------------
         125 +    def _others_bboxes(self, exclude):
         126 +        robot, block, surf, obst = self._objs()
         127 +        out = []
         128 +        for o in [block] + obst:
         129 +            if o in exclude:
         130 +                continue
         131 +            out.append(_rect_bbox(self.state, o))
         132 +        return out
         133 +
         134 +    def _descent_free(self, rx, ry_final, carried_bbox_final, others, margin=0.01):
         135 +        """Check vertical descent from travel height to ry_final at x=rx is collision free."""
         136 +        # base circle sweep: check at the final (lowest) position -- sweep is vertical,
         137 +        # and anything below is covered by checking the column.
         138 +        for b in others:
         139 +            # circle swept vertically from ry_final upwards
         140 +            cy = min(max(ry_final, b[1]), ROBOT_Y_MAX)
         141 +            cy = max(cy, ry_final)
         142 +            if _circle_rect_dist(rx, cy, b) < BASE_R + margin:
         143 +                return False
         144 +            # arm + gripper column
         145 +            col = (rx - GH / 2, ry_final - TIP, rx + GH / 2, ROBOT_Y_MAX)
         146 +            if _overlap(col, b, margin * 0.3):
         147 +                return False
         148 +            if carried_bbox_final is not None:
         149 +                cb = carried_bbox_final
         150 +                colc = (cb[0], cb[1], cb[2], cb[3] + (ROBOT_Y_MAX - ry_final))
         151 +                if _overlap(colc, b, margin * 0.5):
         152 +                    return False
         153 +        return True
         154 +
         155 +    def _grasp_cands(self, b, pref=None):
         156 +        lo = b[0] + 0.012 - (GH / 2 - 0.02)
         157 +        hi = b[2] - 0.012 + (GH / 2 - 0.02)
         158 +        cx = (b[0] + b[2]) / 2 if pref is None else pref
         159 +        if hi < lo:
         160 +            lo = hi = (b[0] + b[2]) / 2
         161 +        full_lo = b[0] + GH / 2
         162 +        full_hi = b[2] - GH / 2
         163 +        vals = np.linspace(lo, hi, 41).tolist() + [min(max(cx, lo), hi)]
         164 +
         165 +        def key(v):
         166 +            # prefer full gripper contact, then closeness to preferred
         167 +            pen = 0.0
         168 +            if full_lo <= full_hi:
         169 +                pen = max(0.0, full_lo - v, v - full_hi)
         170 +            return (round(pen, 4) > 0.0, abs(v - cx))
         171 +        return sorted(vals, key=key)
         172 +
         173 +    def _choose_grasp_x(self, o, others, pref=None):
         174 +        b = _rect_bbox(self.state, o)
         175 +        ry = b[3] + TIP + 0.003
         176 +        for gx in self._grasp_cands(b, pref):
         177 +            if gx < RX_MIN or gx > RX_MAX:
         178 +                continue
         179 +            if self._descent_free(gx, ry, None, others):
         180 +                return gx
         181 +        return None
         182 +
         183 +    def _pick(self, o, pref=None):
         184 +        others = self._others_bboxes([o])
         185 +        gx = self._choose_grasp_x(o, others, pref)
         186 +        if gx is None:
         187 +            return False
         188 +        b = _rect_bbox(self.state, o)
         189 +        yield from self._goto(None, ROBOT_Y_MAX)
         190 +        yield from self._goto(gx, None)
         191 +        ry = b[3] + TIP + 0.003
         192 +        yield from self._goto(None, ry, tol=1e-4)
         193 +        self.vac = 1.0
         194 +        yield self._act()
         195 +        yield self._act()
         196 +        yield from self._goto(None, ROBOT_Y_MAX)
         197 +        nb = _rect_bbox(self.state, o)
         198 +        if nb[1] < b[1] + 0.05:
         199 +            self.vac = 0.0
         200 +            yield self._act()
         201 +            return False
         202 +        return True
         203 +
         204 +    def _place_at(self, o, target_left, target_bottom):
         205 +        x, y, _, _ = self._rpos()
         206 +        b = _rect_bbox(self.state, o)
         207 +        rx = x + (target_left - b[0])
         208 +        yield from self._goto(rx, None)
         209 +        x, y, _, _ = self._rpos()
         210 +        b = _rect_bbox(self.state, o)
         211 +        ry = y - (b[1] - target_bottom)
         212 +        yield from self._goto(None, ry, tol=1e-4)
         213 +
         214 +    # ------------------------------------------------------------------
         215 +    def _final_placement(self):
         216 +        """Returns (left, bottom, surface_bbox, grasp_offset_from_block_left)."""
         217 +        robot, block, surf, obst = self._objs()
         218 +        s = self.state
         219 +        sb = _rect_bbox(s, surf)
         220 +        bb = _rect_bbox(s, block)
         221 +        bw = bb[2] - bb[0]
         222 +        Llo = sb[0] + min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
         223 +        Lhi = sb[2] - bw - min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
         224 +        Lc = sb[0] + (sb[2] - sb[0] - bw) / 2
         225 +        if Lhi < Llo:
         226 +            Llo = Lhi = Lc
         227 +        best = None
         228 +        for g in self._grasp_cands((0.0, 0.0, bw, 1.0)):
         229 +            for L in sorted(np.linspace(Llo, Lhi, 21).tolist() + [Lc], key=lambda v: abs(v - Lc)):
         230 +                if RX_MIN <= L + g <= RX_MAX:
         231 +                    best = (L, g)
         232 +                    break
         233 +            if best is not None:
         234 +                break
         235 +        if best is None:
         236 +            best = (Lc, bw / 2)
         237 +        return best[0], sb[3] + 0.008, sb, best[1]
         238 +
         239 +    def _blocking(self):
         240 +        """Obstructions that interfere with placing the block on the surface."""
         241 +        robot, block, surf, obst = self._objs()
         242 +        s = self.state
         243 +        left, bottom, sb, g = self._final_placement()
         244 +        bb = _rect_bbox(s, block)
         245 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         246 +        final_bb = (left, bottom, left + bw, bottom + bh)
         247 +        rx = left + g
         248 +        ry = bottom + bh + TIP + 0.003
         249 +        res = []
         250 +        for o in obst:
         251 +            ob = _rect_bbox(s, o)
         252 +            if not self._descent_free(rx, ry, final_bb, [ob], margin=0.015):
         253 +                res.append(o)
         254 +            elif ob[0] < sb[2] and ob[2] > sb[0] and ob[1] < sb[3] + 0.05:
         255 +                res.append(o)
         256 +        return res
         257 +
         258 +    def _final_sweep(self):
         259 +        """(rx, ry, final_bb) for the final block placement."""
         260 +        robot, block, surf, obst = self._objs()
         261 +        left, bottom, sb, g = self._final_placement()
         262 +        bb = _rect_bbox(self.state, block)
         263 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         264 +        final_bb = (left, bottom, left + bw, bottom + bh)
         265 +        return left + g, bottom + bh + TIP + 0.003, final_bb
         266 +
         267 +    def _find_spot(self, o):
         268 +        """Find (left, bottom) to park the (currently grasped) obstruction o."""
         269 +        robot, block, surf, obst = self._objs()
         270 +        s = self.state
         271 +        ob = _rect_bbox(s, o)
         272 +        w, h = ob[2] - ob[0], ob[3] - ob[1]
         273 +        x, y, _, _ = self._rpos()
         274 +        goff = x - ob[0]
         275 +        hang = y - ob[3]  # robot y minus object top
         276 +        sb = _rect_bbox(s, surf)
         277 +        others = self._others_bboxes([o])
         278 +        frx, fry, fbb = self._final_sweep()
         279 +        # target block pickup sweep
         280 +        _, _, _, g = self._final_placement()
         281 +        bb = _rect_bbox(s, block)
         282 +        brx = bb[0] + g
         283 +        bry = bb[3] + TIP + 0.003
         284 +        levels = [(FLOOR + 0.005, 0.0)]
         285 +        for b in others:
         286 +            if b[3] + 0.005 + h < 0.42:
         287 +                levels.append((b[3] + 0.005, 1.0 + b[3]))
         288 +        best = None
         289 +        xs = np.arange(WORLD_X[0] + 0.002, WORLD_X[1] - w - 0.002, 0.005)
         290 +        for bottom, pen in levels:
         291 +            for lx in xs:
         292 +                rx = lx + goff
         293 +                if rx < RX_MIN or rx > RX_MAX:
         294 +                    continue
         295 +                cand = (lx, bottom, lx + w, bottom + h)
         296 +                if cand[0] < sb[2] + 0.01 and cand[2] > sb[0] - 0.01:
         297 +                    continue
         298 +                bad = False
         299 +                for b in others:
         300 +                    if _overlap(cand, b, 0.01):
         301 +                        bad = True
         302 +                        break
         303 +                if bad:
         304 +                    continue
         305 +                if not self._descent_free(frx, fry, fbb, [cand], margin=0.02):
         306 +                    continue
         307 +                if not self._descent_free(brx, bry, None, [cand], margin=0.02):
         308 +                    continue
         309 +                ry = bottom + h + hang
         310 +                if not self._descent_free(rx, ry, cand, others, margin=0.012):
         311 +                    continue
         312 +                cost = abs(rx - x) + pen
         313 +                if best is None or cost < best[0]:
         314 +                    best = (cost, lx, bottom)
         315 +        if best is None:
         316 +            return None
         317 +        return best[1], best[2]
         318 +
         319 +    def _plan(self):
         320 +        self.vac = 0.0
         321 +        yield from self._setup_pose()
         322 +        failures = 0
         323 +        for _ in range(30):
         324 +            blockers = self._blocking()
         325 +            if not blockers:
         326 +                break
         327 +            # pick blockers in order of height (tallest first) that are graspable
         328 +            robot, block, surf, obst = self._objs()
         329 +            blockers.sort(key=lambda o: -_rect_bbox(self.state, o)[3])
         330 +            picked = False
         331 +            for o in blockers:
         332 +                others = self._others_bboxes([o])
         333 +                if self._choose_grasp_x(o, others) is None:
         334 +                    continue
         335 +                ok = yield from self._pick(o)
         336 +                if not ok:
         337 +                    failures += 1
         338 +                    continue
         339 +                spot = self._find_spot(o)
         340 +                if spot is None:
         341 +                    # put it back where it was
         342 +                    spot = (_rect_bbox(self.state, o)[0], FLOOR + 0.005)
         343 +                    failures += 1
         344 +                left, bottom = spot
         345 +                yield from self._place_at(o, left, bottom)
         346 +                self.vac = 0.0
         347 +                yield self._act()
         348 +                yield from self._goto(None, ROBOT_Y_MAX)
         349 +                picked = True
         350 +                break
         351 +            if not picked:
         352 +                failures += 1
         353 +                if failures > 5:
         354 +                    break
         355 +        # now the target block
         356 +        for _ in range(10):
         357 +            robot, block, surf, obst = self._objs()
         358 +            left, bottom, sb, g = self._final_placement()
         359 +            bb = _rect_bbox(self.state, block)
         360 +            ok = yield from self._pick(block, pref=bb[0] + g)
         361 +            if ok:
         362 +                break
         363 +        left, bottom, sb, g = self._final_placement()
         364 +        yield from self._place_at(block, left, bottom)
         365 +        self.vac = 0.0
         366 +        for _ in range(5):
         367 +            yield self._act()
diff --git a/r3.txt b/r3.txt
new file mode 100644
index 0000000..6520d25
--- /dev/null
+++ b/r3.txt
@@ -0,0 +1,10 @@
           1 +seed 2000 nobs 3 success True steps 204 time 8.5
           2 +seed 2001 nobs 3 success True steps 150 time 5.9
           3 +seed 2002 nobs 3 success True steps 204 time 8.2
           4 +seed 2003 nobs 3 success True steps 211 time 6.2
           5 +seed 2004 nobs 3 success True steps 160 time 4.1
           6 +seed 2005 nobs 3 success True steps 156 time 5.5
           7 +seed 2006 nobs 3 success True steps 203 time 8.2
           8 +seed 2007 nobs 3 success True steps 164 time 5.4
           9 +seed 2008 nobs 3 success True steps 176 time 7.2
          10 +seed 2009 nobs 3 success True steps 174 time 8.3
diff --git a/r4.txt b/r4.txt
new file mode 100644
index 0000000..83560bf
--- /dev/null
+++ b/r4.txt
@@ -0,0 +1,6 @@
           1 +seed 1000 nobs 4 success True steps 160 time 6.5
           2 +seed 1001 nobs 4 success True steps 158 time 5.8
           3 +seed 1002 nobs 4 success True steps 245 time 9.4
           4 +seed 1003 nobs 4 success True steps 160 time 6.7
           5 +seed 1004 nobs 4 success True steps 140 time 6.0
           6 +seed 1005 nobs 4 success True steps 145 time 6.0
diff --git a/rd.txt b/rd.txt
new file mode 100644
index 0000000..0bcb4be
--- /dev/null
+++ b/rd.txt
@@ -0,0 +1,22 @@
           1 +seed 3000 nobs 2 success True steps 178 time 6.6
           2 +seed 3001 nobs 0 success True steps 50 time 1.8
           3 +seed 3002 nobs 1 success True steps 111 time 3.2
           4 +seed 3003 nobs 2 success True steps 148 time 5.2
           5 +seed 3004 nobs 0 success True steps 52 time 1.9
           6 +seed 3005 nobs 1 success True steps 108 time 4.1
           7 +seed 3006 nobs 0 success True steps 51 time 2.0
           8 +seed 3007 nobs 2 success True steps 91 time 2.2
           9 +seed 3008 nobs 2 success True steps 99 time 3.4
          10 +seed 3009 nobs 0 success True steps 58 time 2.2
          11 +seed 3010 nobs 2 success True steps 176 time 4.0
          12 +seed 3011 nobs 2 success True steps 176 time 5.9
          13 +seed 3012 nobs 1 success True steps 111 time 3.4
          14 +seed 3013 nobs 2 success True steps 160 time 5.7
          15 +seed 3014 nobs 0 success True steps 43 time 1.1
          16 +seed 3015 nobs 1 success True steps 91 time 2.4
          17 +seed 3016 nobs 2 success True steps 133 time 3.7
          18 +seed 3017 nobs 0 success True steps 37 time 1.2
          19 +seed 3018 nobs 1 success True steps 101 time 3.4
          20 +seed 3019 nobs 2 success True steps 158 time 7.0
          21 +seed 3020 nobs 1 success True steps 107 time 3.0
          22 +seed 3021 nobs 1 success True steps 86 time 2.0
```

</details>

<a id="C007"></a>
### C007 · DP path planner, binned spot reranking, placement minimizing blockers

Commit `82c16cf5103b0e60740ba496cea01c863e188e11`; parents: e24e591f5ef916db93a0aa99a7696779e41d0f66. Recorded author date: 2026-09-30T10:55:12+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0289](01_timeline.md#E0289): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_82c16cf_approach.py) · [Exact all-file diff](evidence/diffs/C007_82c16cf.diff)

[Previous saved controller snapshot](evidence/versions/C006_e24e591_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1f918f2..5ab4177 100644
--- a/approach.py
+++ b/approach.py
@@ -42,6 +42,8 @@ class GeneratedApproach:
   42     42          self.high = np.array(action_space.high, dtype=np.float32)
   43     43  
   44     44      # ------------------------------------------------------------------
          45 +    K_RERANK = 20
          46 +
   45     47      def reset(self, state, info):
   46     48          self.state = state
   47     49          self.gen = self._plan()
@@ -141,8 +143,141 @@ class GeneratedApproach:
  141    143                  return False
  142    144          return True
  143    145  
  144        -    def _plan_path(self, x1, y1, obstacles, crel):
  145        -        x0, y0, _, _ = self._rpos()
         146 +    def _free_pts(self, X, Y, obstacles, crel, m=0.008):
         147 +        X = np.asarray(X, dtype=float); Y = np.asarray(Y, dtype=float)
         148 +        free = (X >= RX_MIN - 1e-6) & (X <= RX_MAX + 1e-6) & (Y <= ROBOT_Y_MAX + 1e-6)
         149 +        if crel is not None:
         150 +            free &= (Y + crel[1]) >= FLOOR - 1e-3
         151 +        for b in obstacles:
         152 +            ddx = np.maximum(np.maximum(b[0] - X, 0.0), X - b[2])
         153 +            ddy = np.maximum(np.maximum(b[1] - Y, 0.0), Y - b[3])
         154 +            free &= (ddx * ddx + ddy * ddy) >= (BASE_R + m) ** 2
         155 +            e = 0.001
         156 +            ov = (X - GH / 2 < b[2] + e) & (b[0] < X + GH / 2 + e) & (Y - TIP < b[3] + e) & (b[1] < Y + e)
         157 +            free &= ~ov
         158 +            if crel is not None:
         159 +                e = m * 0.6
         160 +                ov = (X + crel[0] < b[2] + e) & (b[0] < X + crel[2] + e) & \
         161 +                     (Y + crel[1] < b[3] + e) & (b[1] < Y + crel[3] + e)
         162 +                free &= ~ov
         163 +        return free
         164 +
         165 +    def _dp_path(self, x0, y0, x1, y1, obstacles, crel):
         166 +        """DP over x-columns / y-levels. Returns (cost, waypoints) or None."""
         167 +        res = 0.005
         168 +        ylo = 0.3
         169 +        nl = int(round((ROBOT_Y_MAX - ylo) / res)) + 1
         170 +        levels = ylo + res * np.arange(nl)
         171 +        K = int(round(0.05 / res))
         172 +        j0 = int(min(nl - 1, max(0, math.ceil((y0 - ylo) / res - 1e-6))))
         173 +        j1 = int(min(nl - 1, max(0, math.ceil((y1 - ylo) / res - 1e-6))))
         174 +        dx = x1 - x0
         175 +        N = int(math.ceil(abs(dx) / 0.05 - 1e-6))
         176 +        # columns at half steps
         177 +        cols = x0 + dx * (np.arange(2 * N + 1) / max(1, 2 * N)) if N > 0 else np.array([x0])
         178 +        XX = np.repeat(cols[:, None], nl, axis=1)
         179 +        YY = np.repeat(levels[None, :], len(cols), axis=0)
         180 +        F = self._free_pts(XX, YY, obstacles, crel)
         181 +        INF = 1e9
         182 +        # vertical cost matrix within a column
         183 +        J = np.arange(nl)
         184 +        vc = np.ceil(np.abs(J[:, None] - J[None, :]) / K)
         185 +
         186 +        def vert_relax(cost, free):
         187 +            # segments of contiguous free cells
         188 +            seg = np.cumsum(~free)
         189 +            same = (seg[:, None] == seg[None, :]) & free[:, None] & free[None, :]
         190 +            M = np.where(same, cost[None, :] + vc, INF)
         191 +            arg = np.argmin(M, axis=1)
         192 +            return M[J, arg], arg
         193 +
         194 +        cost = np.full(nl, INF)
         195 +        if not F[0, j0]:
         196 +            # allow starting cell even if flagged (numerical contact)
         197 +            F[0, j0] = True
         198 +        cost[j0] = 0.0
         199 +        costs = []
         200 +        backs = []
         201 +        c, arg = vert_relax(cost, F[0])
         202 +        costs.append(c); backs.append(("v", arg))
         203 +        for i in range(1, N + 1):
         204 +            fm = F[2 * i - 1]; fe = F[2 * i]
         205 +            new = np.full(nl, INF)
         206 +            parent = np.full(nl, -1)
         207 +            prev = costs[-1]
         208 +            for d in range(-K, K + 1):
         209 +                # from j to j+d; midpoint level j + d/2
         210 +                src_j = np.arange(max(0, -d), min(nl, nl - d))
         211 +                dst_j = src_j + d
         212 +                mid = src_j + d / 2.0
         213 +                mlo = np.floor(mid).astype(int); mhi = np.ceil(mid).astype(int)
         214 +                ok = fe[dst_j] & fm[mlo] & fm[mhi] & (prev[src_j] < INF)
         215 +                cand = prev[src_j] + 1.0
         216 +                better = ok & (cand < new[dst_j])
         217 +                new[dst_j[better]] = cand[better]
         218 +                parent[dst_j[better]] = src_j[better]
         219 +            if i == N and not fe[j1]:
         220 +                fe = fe.copy(); fe[j1] = True
         221 +            c, arg = vert_relax(new, fe)
         222 +            costs.append(new); backs.append(("h", parent))
         223 +            costs[-1] = c; backs.append(("v", arg))
         224 +            # note: backs holds pairs per column after the first
         225 +        final = costs[-1]
         226 +        if final[j1] >= INF:
         227 +            return None
         228 +        # backtrack
         229 +        pts = []
         230 +        j = j1
         231 +        ci = N
         232 +        bi = len(backs) - 1
         233 +        while bi >= 0:
         234 +            kind, arr = backs[bi]
         235 +            if kind == "v":
         236 +                jp = int(arr[j])
         237 +                # vertical moves from jp to j at column ci
         238 +                if jp != j:
         239 +                    steps = int(math.ceil(abs(j - jp) / K))
         240 +                    for s_ in range(steps, 0, -1):
         241 +                        jj = jp + int(round((j - jp) * s_ / steps))
         242 +                        pts.append((float(cols[2 * ci]), float(levels[jj])))
         243 +                j = jp
         244 +            else:
         245 +                jp = int(arr[j])
         246 +                pts.append((float(cols[2 * ci]), float(levels[j])))
         247 +                j = jp
         248 +                ci -= 1
         249 +            bi -= 1
         250 +        pts.reverse()
         251 +        # dedupe and fix endpoints
         252 +        out = []
         253 +        for p in pts:
         254 +            if not out or abs(out[-1][0] - p[0]) > 1e-9 or abs(out[-1][1] - p[1]) > 1e-9:
         255 +                out.append(p)
         256 +        if out and abs(out[0][0] - x0) < 1e-9 and abs(out[0][1] - levels[j0]) < 1e-9:
         257 +            # first waypoint is the snapped start
         258 +            if abs(levels[j0] - y0) < 1e-9:
         259 +                out = out[1:]
         260 +        if out and abs(out[-1][0] - x1) < 1e-6 and abs(out[-1][1] - levels[j1]) <= res + 1e-9:
         261 +            out[-1] = (x1, y1)
         262 +        else:
         263 +            out.append((x1, y1))
         264 +        return float(final[j1]), out
         265 +
         266 +    def _plan_path(self, x1, y1, obstacles, crel, start=None):
         267 +        if start is None:
         268 +            x0, y0, _, _ = self._rpos()
         269 +        else:
         270 +            x0, y0 = start
         271 +        r = self._dp_path(x0, y0, x1, y1, obstacles, crel)
         272 +        if r is not None:
         273 +            return r[1]
         274 +        return self._plan_path_old(x1, y1, obstacles, crel, (x0, y0))
         275 +
         276 +    def _plan_path_old(self, x1, y1, obstacles, crel, start=None):
         277 +        if start is None:
         278 +            x0, y0, _, _ = self._rpos()
         279 +        else:
         280 +            x0, y0 = start
  146    281          p0 = (x0, y0)
  147    282          if self._seg_free(p0, (x1, y1), obstacles, crel):
  148    283              return [(x1, y1)]
@@ -165,6 +300,14 @@ class GeneratedApproach:
  165    300                  return path
  166    301          return [(x0, ROBOT_Y_MAX), (x1, ROBOT_Y_MAX), (x1, y1)]
  167    302  
         303 +    def _path_cost(self, p0, p1, obstacles, crel):
         304 +        path = self._plan_path(p1[0], p1[1], obstacles, crel, start=p0)
         305 +        pts = [p0] + path
         306 +        c = 0.0
         307 +        for i in range(len(pts) - 1):
         308 +            c += math.ceil(max(abs(pts[i + 1][0] - pts[i][0]), abs(pts[i + 1][1] - pts[i][1])) / 0.05 - 1e-6)
         309 +        return c
         310 +
  168    311      def _move(self, x1, y1, carried=None, last_vac=None):
  169    312          """Plan & execute a collision-free path. carried: grasped object or None."""
  170    313          x0, y0, _, _ = self._rpos()
@@ -265,12 +408,12 @@ class GeneratedApproach:
  265    408          self.vac = 1.0
  266    409          return True
  267    410  
  268        -    def _place_at(self, o, target_left, target_bottom, check=True):
         411 +    def _place_at(self, o, target_left, target_bottom, check=True, release=False):
  269    412          x, y, _, _ = self._rpos()
  270    413          b0 = _rect_bbox(self.state, o)
  271    414          rx = x + (target_left - b0[0])
  272    415          ry = y - (b0[1] - target_bottom)
  273        -        gen = self._move(rx, ry, o)
         416 +        gen = self._move(rx, ry, o, last_vac=(0.0 if release else None))
  274    417          first = True
  275    418          while True:
  276    419              try:
@@ -294,23 +437,39 @@ class GeneratedApproach:
  294    437          s = self.state
  295    438          sb = _rect_bbox(s, surf)
  296    439          bb = _rect_bbox(s, block)
  297        -        bw = bb[2] - bb[0]
         440 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         441 +        bottom = sb[3] + 0.014
  298    442          Llo = sb[0] + min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
  299    443          Lhi = sb[2] - bw - min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
  300    444          Lc = sb[0] + (sb[2] - sb[0] - bw) / 2
  301    445          if Lhi < Llo:
  302    446              Llo = Lhi = Lc
  303        -        best = None
         447 +        obbs = [_rect_bbox(s, o) for o in obst]
         448 +        gs = []
  304    449          for g in self._grasp_cands((0.0, 0.0, bw, 1.0)):
  305        -            for L in sorted(np.linspace(Llo, Lhi, 21).tolist() + [Lc], key=lambda v: abs(v - Lc)):
  306        -                if RX_MIN <= L + g <= RX_MAX:
  307        -                    best = (L, g)
  308        -                    break
  309        -            if best is not None:
         450 +            if all(abs(g - g2) > 0.004 for g2 in gs):
         451 +                gs.append(g)
         452 +            if len(gs) >= 7:
  310    453                  break
         454 +        Ls = np.linspace(Llo, Lhi, 25).tolist() + [Lc]
         455 +        best = None
         456 +        for gi, g in enumerate(gs):
         457 +            for L in Ls:
         458 +                rx = L + g
         459 +                if not (RX_MIN <= rx <= RX_MAX):
         460 +                    continue
         461 +                fbb = (L, bottom, L + bw, bottom + bh)
         462 +                ry = bottom + bh + TIP + 0.003
         463 +                nb = 0
         464 +                for ob in obbs:
         465 +                    if not self._descent_free(rx, ry, fbb, [ob], margin=0.015):
         466 +                        nb += 1
         467 +                cost = nb * 100.0 + abs(L - bb[0]) / 0.05 + gi * 0.01 + abs(L - Lc) * 0.01
         468 +                if best is None or cost < best[0]:
         469 +                    best = (cost, L, g)
  311    470          if best is None:
  312        -            best = (Lc, bw / 2)
  313        -        return best[0], sb[3] + 0.008, sb, best[1]
         471 +            return Lc, bottom, sb, bw / 2
         472 +        return best[1], bottom, sb, best[2]
  314    473  
  315    474      def _blocking(self):
  316    475          """Obstructions that interfere with placing the block on the surface."""
@@ -327,8 +486,6 @@ class GeneratedApproach:
  327    486              ob = _rect_bbox(s, o)
  328    487              if not self._descent_free(rx, ry, final_bb, [ob], margin=0.015):
  329    488                  res.append(o)
  330        -            elif ob[0] < sb[2] and ob[2] > sb[0] and ob[1] < sb[3] + 0.05:
  331        -                res.append(o)
  332    489          return res
  333    490  
  334    491      def _final_sweep(self):
@@ -357,12 +514,16 @@ class GeneratedApproach:
  357    514          bb = _rect_bbox(s, block)
  358    515          brx = bb[0] + g
  359    516          bry = bb[3] + TIP + 0.003
  360        -        levels = [(FLOOR + 0.005, 0.0)]
  361        -        for b in others:
  362        -            if b[3] + 0.005 + h < 0.42:
  363        -                levels.append((b[3] + 0.005, 1.0 + b[3]))
  364        -        best = None
  365        -        xs = np.arange(WORLD_X[0] + 0.002, WORLD_X[1] - w - 0.002, 0.005)
         517 +        levels = [(v, 0.0) for v in np.arange(FLOOR + 0.005, 0.36 - h, 0.02)]
         518 +        # remaining blockers' pickup columns must stay free
         519 +        cols = []
         520 +        for ob2 in self._blocking():
         521 +            if ob2 == o:
         522 +                continue
         523 +            b2 = _rect_bbox(s, ob2)
         524 +            cols.append(((b2[0] + b2[2]) / 2, b2[3] + TIP + 0.003, b2))
         525 +        cands = []
         526 +        xs = np.arange(WORLD_X[0] + 0.002, WORLD_X[1] - w - 0.002, 0.01)
  366    527          for bottom, pen in levels:
  367    528              for lx in xs:
  368    529                  rx = lx + goff
@@ -380,16 +541,40 @@ class GeneratedApproach:
  380    541                      continue
  381    542                  if not self._descent_free(frx, fry, fbb, [cand], margin=0.02):
  382    543                      continue
  383        -                if not self._descent_free(brx, bry, None, [cand], margin=0.02):
         544 +                if not self._descent_free(brx, bry, bb, [cand], margin=0.02):
         545 +                    continue
         546 +                if any(not self._descent_free(cx2, cy2, b2, [cand], margin=0.01)
         547 +                       for cx2, cy2, b2 in cols):
  384    548                      continue
  385    549                  ry = bottom + h + hang
  386    550                  if not self._descent_free(rx, ry, cand, others, margin=0.012):
  387    551                      continue
  388        -                cost = abs(rx - x) + pen
  389        -                if best is None or cost < best[0]:
  390        -                    best = (cost, lx, bottom)
  391        -        if best is None:
         552 +                cost = max(abs(rx - x), abs(ry - y)) + max(abs(rx - brx), abs(ry - bry)) + pen
         553 +                cands.append((cost, lx, bottom, rx, ry, cand))
         554 +        if not cands:
  392    555              return None
         556 +        cands.sort(key=lambda c: c[0])
         557 +        binned = {}
         558 +        for c in cands:
         559 +            k = int(c[3] / 0.08)
         560 +            if k not in binned:
         561 +                binned[k] = c
         562 +        cands = sorted(binned.values(), key=lambda c: c[0])
         563 +        # rerank a few best candidates by planned path costs
         564 +        surf_bb = sb
         565 +        crel_o = (ob[0] - x, ob[1] - y, ob[2] - x, ob[3] - y)
         566 +        crel_b = (bb[0] - brx, bb[1] - bry, bb[2] - brx, bb[3] - bry)
         567 +        best = None
         568 +        for cost, lx, bottom, rx, ry, cand in cands[:self.K_RERANK]:
         569 +            obs1 = others + [surf_bb]
         570 +            c1 = self._path_cost((x, y), (rx, ry), obs1, crel_o)
         571 +            obs2 = [bx for bx in others] + [cand, surf_bb]
         572 +            c2 = self._path_cost((rx, ry + 0.01), (brx, bry), obs2, None)
         573 +            obs3 = [bx for bx in others if bx != bb] + [cand, surf_bb]
         574 +            c3 = self._path_cost((brx, bry), (frx, fry), obs3, crel_b)
         575 +            tot = c1 + c2 + c3
         576 +            if best is None or tot < best[0]:
         577 +                best = (tot, lx, bottom)
  393    578          return best[1], best[2]
  394    579  
  395    580      def _plan(self):
@@ -416,9 +601,11 @@ class GeneratedApproach:
  416    601                      spot = (_rect_bbox(self.state, o)[0], FLOOR + 0.005)
  417    602                      failures += 1
  418    603                  left, bottom = spot
  419        -                ok = yield from self._place_at(o, left, bottom)
         604 +                ok = yield from self._place_at(o, left, bottom, release=True)
         605 +                if self.vac > 0.5:
         606 +                    self.vac = 0.0
         607 +                    yield self._act()
  420    608                  self.vac = 0.0
  421        -                yield self._act()
  422    609                  if not ok:
  423    610                      failures += 1
  424    611                      continue
diff --git a/approach_prev.py b/approach_prev.py
new file mode 100644
index 0000000..1f918f2
--- /dev/null
+++ b/approach_prev.py
@@ -0,0 +1,447 @@
           1 +import math
           2 +import numpy as np
           3 +
           4 +WORLD_X = (0.0, 1.618)
           5 +ROBOT_Y_MAX = 0.895
           6 +FLOOR = 0.1
           7 +ARM = 0.2          # extended arm length we use
           8 +GW = 0.01          # gripper width (along arm)
           9 +GH = 0.07          # gripper height (perpendicular)
          10 +BASE_R = 0.1
          11 +RX_MIN = 0.1 + 0.002
          12 +RX_MAX = 1.618 - 0.1 - 0.002
          13 +TIP = ARM + GW     # distance from robot center to gripper tip (pointing down)
          14 +
          15 +
          16 +def _rect_bbox(state, o):
          17 +    x = float(state.get(o, "x")); y = float(state.get(o, "y"))
          18 +    w = float(state.get(o, "width")); h = float(state.get(o, "height"))
          19 +    th = float(state.get(o, "theta"))
          20 +    if abs(th) < 1e-6:
          21 +        return (x, y, x + w, y + h)
          22 +    c, s = math.cos(th), math.sin(th)
          23 +    pts = [(x, y), (x + w * c, y + w * s), (x - h * s, y + h * c),
          24 +           (x + w * c - h * s, y + w * s + h * c)]
          25 +    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
          26 +    return (min(xs), min(ys), max(xs), max(ys))
          27 +
          28 +
          29 +def _circle_rect_dist(cx, cy, b):
          30 +    dx = max(b[0] - cx, 0.0, cx - b[2])
          31 +    dy = max(b[1] - cy, 0.0, cy - b[3])
          32 +    return math.hypot(dx, dy)
          33 +
          34 +
          35 +def _overlap(a, b, m=0.0):
          36 +    return a[0] < b[2] + m and b[0] < a[2] + m and a[1] < b[3] + m and b[1] < a[3] + m
          37 +
          38 +
          39 +class GeneratedApproach:
          40 +    def __init__(self, action_space, observation_space, primitives):
          41 +        self.low = np.array(action_space.low, dtype=np.float32)
          42 +        self.high = np.array(action_space.high, dtype=np.float32)
          43 +
          44 +    # ------------------------------------------------------------------
          45 +    def reset(self, state, info):
          46 +        self.state = state
          47 +        self.gen = self._plan()
          48 +        self.vac = 0.0
          49 +
          50 +    def get_action(self, state):
          51 +        self.state = state
          52 +        try:
          53 +            a = next(self.gen)
          54 +        except StopIteration:
          55 +            self.gen = self._plan()
          56 +            try:
          57 +                a = next(self.gen)
          58 +            except StopIteration:
          59 +                a = np.zeros(5, dtype=np.float32)
          60 +        a = np.clip(np.asarray(a, dtype=np.float32), self.low, self.high)
          61 +        return a
          62 +
          63 +    # ------------------------------------------------------------------
          64 +    def _objs(self):
          65 +        s = self.state
          66 +        robot = None; block = None; surf = None; obst = []
          67 +        for n in sorted(s.get_object_names()):
          68 +            o = s.get_object_from_name(n)
          69 +            tn = o.type.name
          70 +            if tn == "crv_robot":
          71 +                robot = o
          72 +            elif tn == "target_block":
          73 +                block = o
          74 +            elif tn == "target_surface":
          75 +                surf = o
          76 +            else:
          77 +                obst.append(o)
          78 +        return robot, block, surf, obst
          79 +
          80 +    def _rpos(self):
          81 +        r = self._objs()[0]
          82 +        s = self.state
          83 +        return (float(s.get(r, "x")), float(s.get(r, "y")),
          84 +                float(s.get(r, "theta")), float(s.get(r, "arm_joint")))
          85 +
          86 +    # ------------------------------------------------------------------
          87 +    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0):
          88 +        return np.array([dx, dy, dth, darm, self.vac], dtype=np.float32)
          89 +
          90 +    def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200):
          91 +        """Straight-line move towards (tx, ty). Returns True on success."""
          92 +        stuck = 0
          93 +        last = None
          94 +        for _ in range(max_steps):
          95 +            x, y, th, aj = self._rpos()
          96 +            gx = x if tx is None else tx
          97 +            gy = y if ty is None else ty
          98 +            ex, ey = gx - x, gy - y
          99 +            eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
         100 +            ea = ARM - aj
         101 +            if abs(ex) <= tol and abs(ey) <= tol:
         102 +                if abs(eth) < 1e-4 and abs(ea) < 1e-4:
         103 +                    return True
         104 +            if last is not None and abs(last[0] - x) < 1e-7 and abs(last[1] - y) < 1e-7 \
         105 +                    and abs(last[2] - aj) < 1e-7 and abs(last[3] - th) < 1e-7:
         106 +                stuck += 1
         107 +                if stuck >= 2:
         108 +                    return False
         109 +            else:
         110 +                stuck = 0
         111 +            last = (x, y, aj, th)
         112 +            n = max(1, int(math.ceil(max(abs(ex), abs(ey)) / 0.05 - 1e-6)))
         113 +            yield np.array([ex / n, ey / n, np.clip(eth, -0.19, 0.19),
         114 +                            np.clip(ea, -0.1, 0.1), self.vac], dtype=np.float32)
         115 +        return False
         116 +
         117 +    def _collides(self, x, y, obstacles, crel, m=0.008):
         118 +        if y > ROBOT_Y_MAX + 1e-6 or x < RX_MIN - 1e-6 or x > RX_MAX + 1e-6:
         119 +            return True
         120 +        col = (x - GH / 2, y - TIP, x + GH / 2, y)
         121 +        cb = None
         122 +        if crel is not None:
         123 +            cb = (x + crel[0], y + crel[1], x + crel[2], y + crel[3])
         124 +            if cb[1] < FLOOR - 1e-3:
         125 +                return True
         126 +        for b in obstacles:
         127 +            if _circle_rect_dist(x, y, b) < BASE_R + m:
         128 +                return True
         129 +            if _overlap(col, b, 0.001):
         130 +                return True
         131 +            if cb is not None and _overlap(cb, b, m * 0.6):
         132 +                return True
         133 +        return False
         134 +
         135 +    def _seg_free(self, p, q, obstacles, crel):
         136 +        d = max(abs(q[0] - p[0]), abs(q[1] - p[1]))
         137 +        n = max(1, int(math.ceil(d / 0.008)))
         138 +        for i in range(1, n + 1):
         139 +            t = i / n
         140 +            if self._collides(p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]), obstacles, crel):
         141 +                return False
         142 +        return True
         143 +
         144 +    def _plan_path(self, x1, y1, obstacles, crel):
         145 +        x0, y0, _, _ = self._rpos()
         146 +        p0 = (x0, y0)
         147 +        if self._seg_free(p0, (x1, y1), obstacles, crel):
         148 +            return [(x1, y1)]
         149 +        dx = x1 - x0
         150 +        sg = 1.0 if dx >= 0 else -1.0
         151 +        tys = sorted(set([round(v, 4) for v in np.arange(max(y0, y1) + 0.01, ROBOT_Y_MAX, 0.02)]
         152 +                         + [ROBOT_Y_MAX]))
         153 +        for ty in tys:
         154 +            a = min(abs(dx), ty - y0)
         155 +            b = min(abs(dx) - a, ty - y1)
         156 +            pa = (x0 + sg * a, ty)
         157 +            pb = (x1 - sg * b, ty)
         158 +            path = [pa, pb, (x1, y1)]
         159 +            pts = [p0] + path
         160 +            if all(self._seg_free(pts[i], pts[i + 1], obstacles, crel) for i in range(3)):
         161 +                return path
         162 +            path = [(x0, ty), (x1, ty), (x1, y1)]
         163 +            pts = [p0] + path
         164 +            if all(self._seg_free(pts[i], pts[i + 1], obstacles, crel) for i in range(3)):
         165 +                return path
         166 +        return [(x0, ROBOT_Y_MAX), (x1, ROBOT_Y_MAX), (x1, y1)]
         167 +
         168 +    def _move(self, x1, y1, carried=None, last_vac=None):
         169 +        """Plan & execute a collision-free path. carried: grasped object or None."""
         170 +        x0, y0, _, _ = self._rpos()
         171 +        excl = [carried] if carried is not None else []
         172 +        obstacles = self._others_bboxes(excl)
         173 +        robot, block, surf, obst = self._objs()
         174 +        obstacles.append(_rect_bbox(self.state, surf))
         175 +        crel = None
         176 +        if carried is not None:
         177 +            cb = _rect_bbox(self.state, carried)
         178 +            crel = (cb[0] - x0, cb[1] - y0, cb[2] - x0, cb[3] - y0)
         179 +        path = self._plan_path(x1, y1, obstacles, crel)
         180 +        for i, (px, py) in enumerate(path):
         181 +            if last_vac is not None and i == len(path) - 1:
         182 +                # final segment: run all but last step, then set vacuum on last step
         183 +                gen = self._goto(px, py)
         184 +                while True:
         185 +                    x, y, _, _ = self._rpos()
         186 +                    if max(abs(px - x), abs(py - y)) <= 0.05 + 1e-6:
         187 +                        break
         188 +                    try:
         189 +                        yield next(gen)
         190 +                    except StopIteration:
         191 +                        break
         192 +                self.vac = last_vac
         193 +            ok = yield from self._goto(px, py)
         194 +            if not ok:
         195 +                return False
         196 +        return True
         197 +
         198 +    # ------------------------------------------------------------------
         199 +    def _others_bboxes(self, exclude):
         200 +        robot, block, surf, obst = self._objs()
         201 +        out = []
         202 +        for o in [block] + obst:
         203 +            if o in exclude:
         204 +                continue
         205 +            out.append(_rect_bbox(self.state, o))
         206 +        return out
         207 +
         208 +    def _descent_free(self, rx, ry_final, carried_bbox_final, others, margin=0.01):
         209 +        """Check vertical descent from travel height to ry_final at x=rx is collision free."""
         210 +        # base circle sweep: check at the final (lowest) position -- sweep is vertical,
         211 +        # and anything below is covered by checking the column.
         212 +        for b in others:
         213 +            # circle swept vertically from ry_final upwards
         214 +            cy = min(max(ry_final, b[1]), ROBOT_Y_MAX)
         215 +            cy = max(cy, ry_final)
         216 +            if _circle_rect_dist(rx, cy, b) < BASE_R + margin:
         217 +                return False
         218 +            # arm + gripper column
         219 +            col = (rx - GH / 2, ry_final - TIP, rx + GH / 2, ROBOT_Y_MAX)
         220 +            if _overlap(col, b, margin * 0.3):
         221 +                return False
         222 +            if carried_bbox_final is not None:
         223 +                cb = carried_bbox_final
         224 +                colc = (cb[0], cb[1], cb[2], cb[3] + (ROBOT_Y_MAX - ry_final))
         225 +                if _overlap(colc, b, margin * 0.5):
         226 +                    return False
         227 +        return True
         228 +
         229 +    def _grasp_cands(self, b, pref=None):
         230 +        lo = b[0] + 0.012 - (GH / 2 - 0.02)
         231 +        hi = b[2] - 0.012 + (GH / 2 - 0.02)
         232 +        cx = (b[0] + b[2]) / 2 if pref is None else pref
         233 +        if hi < lo:
         234 +            lo = hi = (b[0] + b[2]) / 2
         235 +        full_lo = b[0] + GH / 2
         236 +        full_hi = b[2] - GH / 2
         237 +        vals = np.linspace(lo, hi, 41).tolist() + [min(max(cx, lo), hi)]
         238 +
         239 +        def key(v):
         240 +            # prefer full gripper contact, then closeness to preferred
         241 +            pen = 0.0
         242 +            if full_lo <= full_hi:
         243 +                pen = max(0.0, full_lo - v, v - full_hi)
         244 +            return (round(pen, 4) > 0.0, abs(v - cx))
         245 +        return sorted(vals, key=key)
         246 +
         247 +    def _choose_grasp_x(self, o, others, pref=None):
         248 +        b = _rect_bbox(self.state, o)
         249 +        ry = b[3] + TIP + 0.003
         250 +        for gx in self._grasp_cands(b, pref):
         251 +            if gx < RX_MIN or gx > RX_MAX:
         252 +                continue
         253 +            if self._descent_free(gx, ry, None, others):
         254 +                return gx
         255 +        return None
         256 +
         257 +    def _pick(self, o, pref=None):
         258 +        others = self._others_bboxes([o])
         259 +        gx = self._choose_grasp_x(o, others, pref)
         260 +        if gx is None:
         261 +            return False
         262 +        b = _rect_bbox(self.state, o)
         263 +        ry = b[3] + TIP + 0.003
         264 +        yield from self._move(gx, ry, None, last_vac=1.0)
         265 +        self.vac = 1.0
         266 +        return True
         267 +
         268 +    def _place_at(self, o, target_left, target_bottom, check=True):
         269 +        x, y, _, _ = self._rpos()
         270 +        b0 = _rect_bbox(self.state, o)
         271 +        rx = x + (target_left - b0[0])
         272 +        ry = y - (b0[1] - target_bottom)
         273 +        gen = self._move(rx, ry, o)
         274 +        first = True
         275 +        while True:
         276 +            try:
         277 +                a = next(gen)
         278 +            except StopIteration as e:
         279 +                return True
         280 +            yield a
         281 +            if first and check:
         282 +                first = False
         283 +                nb = _rect_bbox(self.state, o)
         284 +                if abs(nb[0] - b0[0]) + abs(nb[1] - b0[1]) < 1e-6:
         285 +                    # grasp failed
         286 +                    self.vac = 0.0
         287 +                    yield self._act()
         288 +                    return False
         289 +
         290 +    # ------------------------------------------------------------------
         291 +    def _final_placement(self):
         292 +        """Returns (left, bottom, surface_bbox, grasp_offset_from_block_left)."""
         293 +        robot, block, surf, obst = self._objs()
         294 +        s = self.state
         295 +        sb = _rect_bbox(s, surf)
         296 +        bb = _rect_bbox(s, block)
         297 +        bw = bb[2] - bb[0]
         298 +        Llo = sb[0] + min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
         299 +        Lhi = sb[2] - bw - min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
         300 +        Lc = sb[0] + (sb[2] - sb[0] - bw) / 2
         301 +        if Lhi < Llo:
         302 +            Llo = Lhi = Lc
         303 +        best = None
         304 +        for g in self._grasp_cands((0.0, 0.0, bw, 1.0)):
         305 +            for L in sorted(np.linspace(Llo, Lhi, 21).tolist() + [Lc], key=lambda v: abs(v - Lc)):
         306 +                if RX_MIN <= L + g <= RX_MAX:
         307 +                    best = (L, g)
         308 +                    break
         309 +            if best is not None:
         310 +                break
         311 +        if best is None:
         312 +            best = (Lc, bw / 2)
         313 +        return best[0], sb[3] + 0.008, sb, best[1]
         314 +
         315 +    def _blocking(self):
         316 +        """Obstructions that interfere with placing the block on the surface."""
         317 +        robot, block, surf, obst = self._objs()
         318 +        s = self.state
         319 +        left, bottom, sb, g = self._final_placement()
         320 +        bb = _rect_bbox(s, block)
         321 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         322 +        final_bb = (left, bottom, left + bw, bottom + bh)
         323 +        rx = left + g
         324 +        ry = bottom + bh + TIP + 0.003
         325 +        res = []
         326 +        for o in obst:
         327 +            ob = _rect_bbox(s, o)
         328 +            if not self._descent_free(rx, ry, final_bb, [ob], margin=0.015):
         329 +                res.append(o)
         330 +            elif ob[0] < sb[2] and ob[2] > sb[0] and ob[1] < sb[3] + 0.05:
         331 +                res.append(o)
         332 +        return res
         333 +
         334 +    def _final_sweep(self):
         335 +        """(rx, ry, final_bb) for the final block placement."""
         336 +        robot, block, surf, obst = self._objs()
         337 +        left, bottom, sb, g = self._final_placement()
         338 +        bb = _rect_bbox(self.state, block)
         339 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         340 +        final_bb = (left, bottom, left + bw, bottom + bh)
         341 +        return left + g, bottom + bh + TIP + 0.003, final_bb
         342 +
         343 +    def _find_spot(self, o):
         344 +        """Find (left, bottom) to park the (currently grasped) obstruction o."""
         345 +        robot, block, surf, obst = self._objs()
         346 +        s = self.state
         347 +        ob = _rect_bbox(s, o)
         348 +        w, h = ob[2] - ob[0], ob[3] - ob[1]
         349 +        x, y, _, _ = self._rpos()
         350 +        goff = x - ob[0]
         351 +        hang = y - ob[3]  # robot y minus object top
         352 +        sb = _rect_bbox(s, surf)
         353 +        others = self._others_bboxes([o])
         354 +        frx, fry, fbb = self._final_sweep()
         355 +        # target block pickup sweep
         356 +        _, _, _, g = self._final_placement()
         357 +        bb = _rect_bbox(s, block)
         358 +        brx = bb[0] + g
         359 +        bry = bb[3] + TIP + 0.003
         360 +        levels = [(FLOOR + 0.005, 0.0)]
         361 +        for b in others:
         362 +            if b[3] + 0.005 + h < 0.42:
         363 +                levels.append((b[3] + 0.005, 1.0 + b[3]))
         364 +        best = None
         365 +        xs = np.arange(WORLD_X[0] + 0.002, WORLD_X[1] - w - 0.002, 0.005)
         366 +        for bottom, pen in levels:
         367 +            for lx in xs:
         368 +                rx = lx + goff
         369 +                if rx < RX_MIN or rx > RX_MAX:
         370 +                    continue
         371 +                cand = (lx, bottom, lx + w, bottom + h)
         372 +                if cand[0] < sb[2] + 0.01 and cand[2] > sb[0] - 0.01:
         373 +                    continue
         374 +                bad = False
         375 +                for b in others:
         376 +                    if _overlap(cand, b, 0.01):
         377 +                        bad = True
         378 +                        break
         379 +                if bad:
         380 +                    continue
         381 +                if not self._descent_free(frx, fry, fbb, [cand], margin=0.02):
         382 +                    continue
         383 +                if not self._descent_free(brx, bry, None, [cand], margin=0.02):
         384 +                    continue
         385 +                ry = bottom + h + hang
         386 +                if not self._descent_free(rx, ry, cand, others, margin=0.012):
         387 +                    continue
         388 +                cost = abs(rx - x) + pen
         389 +                if best is None or cost < best[0]:
         390 +                    best = (cost, lx, bottom)
         391 +        if best is None:
         392 +            return None
         393 +        return best[1], best[2]
         394 +
         395 +    def _plan(self):
         396 +        self.vac = 0.0
         397 +        failures = 0
         398 +        for _ in range(30):
         399 +            blockers = self._blocking()
         400 +            if not blockers:
         401 +                break
         402 +            robot, block, surf, obst = self._objs()
         403 +            x, y, _, _ = self._rpos()
         404 +            blockers.sort(key=lambda o: (-_rect_bbox(self.state, o)[3]))
         405 +            picked = False
         406 +            for o in blockers:
         407 +                others = self._others_bboxes([o])
         408 +                if self._choose_grasp_x(o, others) is None:
         409 +                    continue
         410 +                ok = yield from self._pick(o)
         411 +                if not ok:
         412 +                    failures += 1
         413 +                    continue
         414 +                spot = self._find_spot(o)
         415 +                if spot is None:
         416 +                    spot = (_rect_bbox(self.state, o)[0], FLOOR + 0.005)
         417 +                    failures += 1
         418 +                left, bottom = spot
         419 +                ok = yield from self._place_at(o, left, bottom)
         420 +                self.vac = 0.0
         421 +                yield self._act()
         422 +                if not ok:
         423 +                    failures += 1
         424 +                    continue
         425 +                picked = True
         426 +                break
         427 +            if not picked:
         428 +                failures += 1
         429 +                if failures > 5:
         430 +                    break
         431 +        # now the target block
         432 +        robot, block, surf, obst = self._objs()
         433 +        for _ in range(10):
         434 +            left, bottom, sb, g = self._final_placement()
         435 +            bb = _rect_bbox(self.state, block)
         436 +            ok = yield from self._pick(block, pref=bb[0] + g)
         437 +            if not ok:
         438 +                self.vac = 0.0
         439 +                yield self._act()
         440 +                continue
         441 +            left, bottom, sb, g = self._final_placement()
         442 +            ok = yield from self._place_at(block, left, bottom)
         443 +            if ok:
         444 +                break
         445 +        self.vac = 0.0
         446 +        for _ in range(5):
         447 +            yield self._act()
diff --git a/c3.txt b/c3.txt
deleted file mode 100644
index fc61cda..0000000
--- a/c3.txt
+++ /dev/null
@@ -1,41 +0,0 @@
    1        -seed 200 nobs 3 success True steps 181 time 11.3
    2        -seed 201 nobs 3 success True steps 176 time 12.5
    3        -seed 202 nobs 3 success True steps 175 time 12.9
    4        -seed 203 nobs 3 success True steps 238 time 16.9
    5        -seed 204 nobs 3 success True steps 182 time 10.2
    6        -seed 205 nobs 3 success True steps 217 time 14.1
    7        -seed 206 nobs 3 success True steps 180 time 14.6
    8        -seed 207 nobs 3 success True steps 220 time 15.3
    9        -seed 208 nobs 3 success True steps 164 time 11.4
   10        -seed 209 nobs 3 success True steps 94 time 6.2
   11        -seed 210 nobs 3 success True steps 246 time 15.3
   12        -seed 211 nobs 3 success True steps 183 time 12.6
   13        -seed 212 nobs 3 success True steps 135 time 9.8
   14        -seed 213 nobs 3 success True steps 162 time 8.6
   15        -seed 214 nobs 3 success True steps 170 time 10.3
   16        -seed 215 nobs 3 success True steps 216 time 15.3
   17        -seed 216 nobs 3 success True steps 188 time 12.6
   18        -seed 217 nobs 3 success True steps 153 time 8.6
   19        -seed 218 nobs 3 success True steps 183 time 9.8
   20        -seed 219 nobs 3 success True steps 173 time 10.1
   21        -seed 220 nobs 3 success True steps 186 time 9.8
   22        -seed 221 nobs 3 success True steps 179 time 11.1
   23        -seed 222 nobs 3 success True steps 165 time 5.0
   24        -seed 223 nobs 3 success True steps 209 time 7.3
   25        -seed 224 nobs 3 success True steps 113 time 4.8
   26        -seed 225 nobs 3 success True steps 175 time 4.1
   27        -seed 226 nobs 3 success True steps 161 time 6.4
   28        -seed 227 nobs 3 success True steps 106 time 3.2
   29        -seed 228 nobs 3 success True steps 169 time 6.6
   30        -seed 229 nobs 3 success True steps 223 time 8.6
   31        -seed 230 nobs 3 success True steps 113 time 3.1
   32        -seed 231 nobs 3 success True steps 226 time 6.4
   33        -seed 232 nobs 3 success True steps 173 time 5.7
   34        -seed 233 nobs 3 success True steps 123 time 5.0
   35        -seed 234 nobs 3 success True steps 171 time 6.2
   36        -seed 235 nobs 3 success True steps 156 time 5.0
   37        -seed 236 nobs 3 success True steps 166 time 5.5
   38        -seed 237 nobs 3 success True steps 197 time 6.8
   39        -seed 238 nobs 3 success True steps 220 time 9.5
   40        -seed 239 nobs 3 success True steps 187 time 6.1
   41        -success 40 / 40
diff --git a/c4.txt b/c4.txt
deleted file mode 100644
index 0cb9db7..0000000
--- a/c4.txt
+++ /dev/null
@@ -1,41 +0,0 @@
    1        -seed 100 nobs 4 success True steps 232 time 17.1
    2        -seed 101 nobs 4 success True steps 259 time 18.3
    3        -seed 102 nobs 4 success True steps 175 time 11.2
    4        -seed 103 nobs 4 success True steps 247 time 16.2
    5        -seed 104 nobs 4 success True steps 246 time 17.2
    6        -seed 105 nobs 4 success True steps 191 time 14.2
    7        -seed 106 nobs 4 success True steps 220 time 14.8
    8        -seed 107 nobs 4 success True steps 161 time 11.2
    9        -seed 108 nobs 4 success True steps 203 time 11.9
   10        -seed 109 nobs 4 success True steps 187 time 9.4
   11        -seed 110 nobs 4 success True steps 178 time 10.9
   12        -seed 111 nobs 4 success True steps 163 time 5.3
   13        -seed 112 nobs 4 success True steps 173 time 5.7
   14        -seed 113 nobs 4 success True steps 211 time 7.7
   15        -seed 114 nobs 4 success True steps 170 time 7.2
   16        -seed 115 nobs 4 success True steps 233 time 7.3
   17        -seed 116 nobs 4 success True steps 249 time 8.7
   18        -seed 117 nobs 4 success True steps 241 time 9.0
   19        -seed 118 nobs 4 success True steps 223 time 7.0
   20        -seed 119 nobs 4 success True steps 213 time 4.2
   21        -seed 120 nobs 4 success True steps 250 time 3.2
   22        -seed 121 nobs 4 success True steps 159 time 0.9
   23        -seed 122 nobs 4 success True steps 208 time 1.1
   24        -seed 123 nobs 4 success True steps 123 time 0.7
   25        -seed 124 nobs 4 success True steps 274 time 1.4
   26        -seed 125 nobs 4 success True steps 112 time 0.7
   27        -seed 126 nobs 4 success True steps 218 time 1.2
   28        -seed 127 nobs 4 success True steps 254 time 1.1
   29        -seed 128 nobs 4 success True steps 217 time 1.1
   30        -seed 129 nobs 4 success True steps 169 time 0.9
   31        -seed 130 nobs 4 success False steps 1000 time 4.3
   32        -seed 131 nobs 4 success True steps 93 time 0.4
   33        -seed 132 nobs 4 success True steps 160 time 0.8
   34        -seed 133 nobs 4 success True steps 222 time 1.1
   35        -seed 134 nobs 4 success True steps 236 time 1.1
   36        -seed 135 nobs 4 success True steps 205 time 1.1
   37        -seed 136 nobs 4 success True steps 170 time 0.8
   38        -seed 137 nobs 4 success True steps 239 time 1.0
   39        -seed 138 nobs 4 success True steps 285 time 1.5
   40        -seed 139 nobs 4 success True steps 234 time 1.1
   41        -success 39 / 40
diff --git a/c5.txt b/c5.txt
deleted file mode 100644
index 0682116..0000000
--- a/c5.txt
+++ /dev/null
@@ -1,13 +0,0 @@
    1        -Traceback (most recent call last):
    2        -  File "/sandbox/test_approach.py", line 23, in <module>
    3        -    term, steps, n, dt = run(s, count=cnt)
    4        -                         ^^^^^^^^^^^^^^^^^
    5        -  File "/sandbox/test_approach.py", line 7, in run
    6        -    obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
    7        -                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    8        -  File "/sandbox/env_client.py", line 525, in reset
    9        -    response = self._request({"cmd": "reset", "seed": seed, "options": options})
   10        -               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   11        -  File "/sandbox/env_client.py", line 478, in _request
   12        -    raise RuntimeError("Connection to the environment server was closed")
   13        -RuntimeError: Connection to the environment server was closed
diff --git a/cd.txt b/cd.txt
deleted file mode 100644
index 9c75310..0000000
--- a/cd.txt
+++ /dev/null
@@ -1,101 +0,0 @@
    1        -seed 300 nobs 0 success True steps 50 time 2.0
    2        -seed 301 nobs 0 success True steps 80 time 3.1
    3        -seed 302 nobs 2 success True steps 155 time 9.5
    4        -seed 303 nobs 1 success True steps 134 time 8.0
    5        -seed 304 nobs 2 success True steps 169 time 5.6
    6        -seed 305 nobs 0 success True steps 49 time 2.4
    7        -seed 306 nobs 2 success True steps 163 time 9.5
    8        -seed 307 nobs 2 success True steps 187 time 11.6
    9        -seed 308 nobs 1 success True steps 110 time 7.2
   10        -seed 309 nobs 1 success True steps 125 time 4.4
   11        -seed 310 nobs 0 success True steps 44 time 1.7
   12        -seed 311 nobs 1 success True steps 117 time 6.8
   13        -seed 312 nobs 0 success True steps 74 time 5.0
   14        -seed 313 nobs 0 success True steps 48 time 3.1
   15        -seed 314 nobs 1 success True steps 66 time 4.0
   16        -seed 315 nobs 1 success True steps 41 time 2.3
   17        -seed 316 nobs 0 success True steps 48 time 2.9
   18        -seed 317 nobs 0 success True steps 41 time 2.0
   19        -seed 318 nobs 0 success True steps 74 time 3.2
   20        -seed 319 nobs 2 success True steps 113 time 5.8
   21        -seed 320 nobs 0 success True steps 39 time 1.8
   22        -seed 321 nobs 1 success True steps 101 time 4.9
   23        -seed 322 nobs 0 success True steps 46 time 2.3
   24        -seed 323 nobs 2 success True steps 115 time 8.2
   25        -seed 324 nobs 1 success True steps 132 time 7.4
   26        -seed 325 nobs 0 success True steps 48 time 2.8
   27        -seed 326 nobs 0 success True steps 75 time 4.2
   28        -seed 327 nobs 1 success True steps 104 time 6.8
   29        -seed 328 nobs 0 success True steps 40 time 1.7
   30        -seed 329 nobs 2 success True steps 165 time 9.1
   31        -seed 330 nobs 1 success True steps 117 time 1.9
   32        -seed 331 nobs 0 success True steps 38 time 1.4
   33        -seed 332 nobs 1 success True steps 103 time 6.8
   34        -seed 333 nobs 0 success True steps 34 time 1.9
   35        -seed 334 nobs 1 success True steps 93 time 5.4
   36        -seed 335 nobs 0 success True steps 44 time 2.2
   37        -seed 336 nobs 1 success True steps 119 time 6.2
   38        -seed 337 nobs 0 success True steps 81 time 3.7
   39        -seed 338 nobs 1 success True steps 98 time 5.9
   40        -seed 339 nobs 0 success True steps 62 time 4.5
   41        -seed 340 nobs 0 success True steps 42 time 1.7
   42        -seed 341 nobs 2 success True steps 99 time 6.2
   43        -seed 342 nobs 2 success True steps 191 time 10.7
   44        -seed 343 nobs 0 success True steps 58 time 2.4
   45        -seed 344 nobs 0 success True steps 59 time 3.2
   46        -seed 345 nobs 0 success True steps 58 time 3.4
   47        -seed 346 nobs 1 success True steps 133 time 6.3
   48        -seed 347 nobs 2 success True steps 96 time 5.4
   49        -seed 348 nobs 0 success True steps 52 time 1.8
   50        -seed 349 nobs 2 success True steps 105 time 5.0
   51        -seed 350 nobs 1 success True steps 98 time 4.9
   52        -seed 351 nobs 1 success True steps 120 time 4.6
   53        -seed 352 nobs 0 success True steps 61 time 2.7
   54        -seed 353 nobs 0 success True steps 45 time 1.6
   55        -seed 354 nobs 2 success True steps 177 time 8.0
   56        -seed 355 nobs 1 success True steps 57 time 2.5
   57        -seed 356 nobs 0 success True steps 54 time 1.2
   58        -seed 357 nobs 1 success True steps 125 time 6.2
   59        -seed 358 nobs 2 success True steps 140 time 8.1
   60        -seed 359 nobs 1 success True steps 109 time 4.6
   61        -seed 360 nobs 2 success True steps 155 time 4.0
   62        -seed 361 nobs 2 success True steps 162 time 5.5
   63        -seed 362 nobs 2 success True steps 163 time 5.2
   64        -seed 363 nobs 0 success True steps 66 time 1.9
   65        -seed 364 nobs 1 success True steps 108 time 1.7
   66        -seed 365 nobs 0 success True steps 71 time 1.8
   67        -seed 366 nobs 0 success True steps 45 time 1.1
   68        -seed 367 nobs 2 success True steps 199 time 7.2
   69        -seed 368 nobs 2 success True steps 151 time 3.8
   70        -seed 369 nobs 2 success True steps 163 time 5.3
   71        -seed 370 nobs 1 success True steps 114 time 1.8
   72        -seed 371 nobs 2 success True steps 97 time 3.2
   73        -seed 372 nobs 1 success True steps 137 time 3.4
   74        -seed 373 nobs 1 success True steps 118 time 2.1
   75        -seed 374 nobs 2 success True steps 165 time 4.7
   76        -seed 375 nobs 0 success True steps 51 time 1.1
   77        -seed 376 nobs 1 success True steps 118 time 4.1
   78        -seed 377 nobs 2 success True steps 132 time 3.4
   79        -seed 378 nobs 1 success True steps 141 time 4.5
   80        -seed 379 nobs 2 success True steps 166 time 6.3
   81        -seed 380 nobs 1 success True steps 123 time 2.9
   82        -seed 381 nobs 2 success True steps 133 time 3.2
   83        -seed 382 nobs 0 success True steps 67 time 1.4
   84        -seed 383 nobs 0 success True steps 63 time 1.8
   85        -seed 384 nobs 0 success True steps 64 time 2.0
   86        -seed 385 nobs 2 success True steps 140 time 4.6
   87        -seed 386 nobs 1 success True steps 104 time 3.3
   88        -seed 387 nobs 1 success True steps 113 time 3.2
   89        -seed 388 nobs 1 success True steps 106 time 3.9
   90        -seed 389 nobs 0 success True steps 53 time 1.6
   91        -seed 390 nobs 1 success True steps 122 time 3.7
   92        -seed 391 nobs 0 success True steps 66 time 2.3
   93        -seed 392 nobs 2 success True steps 101 time 3.0
   94        -seed 393 nobs 2 success True steps 46 time 1.3
   95        -seed 394 nobs 0 success True steps 44 time 1.5
   96        -seed 395 nobs 1 success True steps 131 time 2.3
   97        -seed 396 nobs 1 success True steps 134 time 2.5
   98        -seed 397 nobs 2 success True steps 159 time 2.8
   99        -seed 398 nobs 2 success True steps 97 time 1.0
  100        -seed 399 nobs 2 success True steps 165 time 1.6
  101        -success 100 / 100
diff --git a/cnt_3.txt b/cnt_3.txt
deleted file mode 100644
index 295924d..0000000
--- a/cnt_3.txt
+++ /dev/null
@@ -1,4 +0,0 @@
    1        -seed 0 nobs 3 success True steps 105 time 4.6
    2        -seed 1 nobs 3 success True steps 177 time 9.8
    3        -seed 2 nobs 3 success True steps 187 time 10.0
    4        -success 3 / 3
diff --git a/cnt_4.txt b/cnt_4.txt
deleted file mode 100644
index c14d154..0000000
--- a/cnt_4.txt
+++ /dev/null
@@ -1,4 +0,0 @@
    1        -seed 0 nobs 4 success True steps 160 time 8.6
    2        -seed 1 nobs 4 success True steps 214 time 9.0
    3        -seed 2 nobs 4 success True steps 179 time 6.6
    4        -success 3 / 3
diff --git a/cnt_6.txt b/cnt_6.txt
deleted file mode 100644
index 42485f0..0000000
--- a/cnt_6.txt
+++ /dev/null
@@ -1,13 +0,0 @@
    1        -Traceback (most recent call last):
    2        -  File "/sandbox/test_approach.py", line 23, in <module>
    3        -    term, steps, n, dt = run(s, count=cnt)
    4        -                         ^^^^^^^^^^^^^^^^^
    5        -  File "/sandbox/test_approach.py", line 7, in run
    6        -    obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
    7        -                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    8        -  File "/sandbox/env_client.py", line 525, in reset
    9        -    response = self._request({"cmd": "reset", "seed": seed, "options": options})
   10        -               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   11        -  File "/sandbox/env_client.py", line 481, in _request
   12        -    raise RuntimeError(f"Environment server error: {response['error']}")
   13        -RuntimeError: Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts.
diff --git a/cnt_8.txt b/cnt_8.txt
deleted file mode 100644
index f18b7e3..0000000
--- a/cnt_8.txt
+++ /dev/null
@@ -1,13 +0,0 @@
    1        -Traceback (most recent call last):
    2        -  File "/sandbox/test_approach.py", line 23, in <module>
    3        -    term, steps, n, dt = run(s, count=cnt)
    4        -                         ^^^^^^^^^^^^^^^^^
    5        -  File "/sandbox/test_approach.py", line 7, in run
    6        -    obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
    7        -                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    8        -  File "/sandbox/env_client.py", line 525, in reset
    9        -    response = self._request({"cmd": "reset", "seed": seed, "options": options})
   10        -               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   11        -  File "/sandbox/env_client.py", line 481, in _request
   12        -    raise RuntimeError(f"Environment server error: {response['error']}")
   13        -RuntimeError: Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=8; it likely exceeds the family's feasible object count. Lower the configured counts.
diff --git a/dbg_spot.py b/dbg_spot.py
new file mode 100644
index 0000000..6f9b50b
--- /dev/null
+++ b/dbg_spot.py
@@ -0,0 +1,23 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +from approach import GeneratedApproach, _rect_bbox
           5 +seed=int(sys.argv[1])
           6 +env=make_env(); obs,info=env.reset(seed=seed)
           7 +ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
           8 +# monkeypatch path cost to print
           9 +orig=ap._path_cost
          10 +log=[]
          11 +def pc(p0,p1,o,c):
          12 +    v=orig(p0,p1,o,c); log.append((p0,p1,v)); return v
          13 +ap._path_cost=pc
          14 +orig_fs=ap._find_spot
          15 +def fs(o):
          16 +    log.clear(); r=orig_fs(o)
          17 +    for i in range(0,len(log),3):
          18 +        print("cand rx=%.3f ry=%.3f  c1=%d c2=%d c3=%d"%(log[i][1][0],log[i][1][1],log[i][2],log[i+1][2],log[i+2][2]))
          19 +    print("chosen",r); return r
          20 +ap._find_spot=fs
          21 +for t in range(200):
          22 +    a=ap.get_action(obs); obs,r,term,tr,_=env.step(a)
          23 +    if term: print("steps",t+1); break
diff --git a/quick.py b/quick.py
new file mode 100644
index 0000000..0ce7f88
--- /dev/null
+++ b/quick.py
@@ -0,0 +1,11 @@
           1 +import sys, time
           2 +import test_approach as t
           3 +from concurrent.futures import ThreadPoolExecutor
           4 +seeds=[int(a) for a in sys.argv[1].split(',')] if ',' in sys.argv[1] else list(range(int(sys.argv[1]), int(sys.argv[2])))
           5 +cnt=int(sys.argv[3]) if len(sys.argv)>3 and sys.argv[3]!='-' else None
           6 +with ThreadPoolExecutor(4) as ex:
           7 +    res=list(ex.map(lambda s: (s,)+tuple(t.run(s,count=cnt)), seeds))
           8 +print(" ".join(f"{r[0]}:{r[2]}" for r in res))
           9 +for r in res:
          10 +    if not r[1]: print("FAIL", r)
          11 +print("succ", sum(r[1] for r in res), "/", len(res), "mean steps", sum(r[2] for r in res)/len(res), "max time", max(r[4] for r in res))
diff --git a/r3.txt b/r3.txt
index 6520d25..80fc373 100644
--- a/r3.txt
+++ b/r3.txt
@@ -1,10 +1,101 @@
    1        -seed 2000 nobs 3 success True steps 204 time 8.5
    2        -seed 2001 nobs 3 success True steps 150 time 5.9
    3        -seed 2002 nobs 3 success True steps 204 time 8.2
    4        -seed 2003 nobs 3 success True steps 211 time 6.2
    5        -seed 2004 nobs 3 success True steps 160 time 4.1
    6        -seed 2005 nobs 3 success True steps 156 time 5.5
    7        -seed 2006 nobs 3 success True steps 203 time 8.2
    8        -seed 2007 nobs 3 success True steps 164 time 5.4
    9        -seed 2008 nobs 3 success True steps 176 time 7.2
   10        -seed 2009 nobs 3 success True steps 174 time 8.3
           1 +seed 2000 nobs 3 success True steps 92 time 3.0
           2 +seed 2001 nobs 3 success True steps 50 time 2.0
           3 +seed 2002 nobs 3 success True steps 76 time 2.7
           4 +seed 2003 nobs 3 success True steps 84 time 2.7
           5 +seed 2004 nobs 3 success True steps 56 time 1.9
           6 +seed 2005 nobs 3 success True steps 63 time 1.7
           7 +seed 2006 nobs 3 success True steps 98 time 3.0
           8 +seed 2007 nobs 3 success True steps 68 time 2.4
           9 +seed 2008 nobs 3 success True steps 82 time 2.7
          10 +seed 2009 nobs 3 success True steps 68 time 1.9
          11 +seed 2010 nobs 3 success True steps 71 time 2.6
          12 +seed 2011 nobs 3 success True steps 43 time 1.6
          13 +seed 2012 nobs 3 success True steps 48 time 1.3
          14 +seed 2013 nobs 3 success True steps 46 time 1.6
          15 +seed 2014 nobs 3 success True steps 58 time 2.5
          16 +seed 2015 nobs 3 success True steps 73 time 2.3
          17 +seed 2016 nobs 3 success True steps 55 time 2.1
          18 +seed 2017 nobs 3 success True steps 77 time 3.2
          19 +seed 2018 nobs 3 success True steps 85 time 4.0
          20 +seed 2019 nobs 3 success True steps 68 time 3.2
          21 +seed 2020 nobs 3 success True steps 71 time 2.5
          22 +seed 2021 nobs 3 success True steps 72 time 3.1
          23 +seed 2022 nobs 3 success True steps 115 time 4.7
          24 +seed 2023 nobs 3 success True steps 45 time 1.8
          25 +seed 2024 nobs 3 success True steps 57 time 2.8
          26 +seed 2025 nobs 3 success True steps 63 time 2.3
          27 +seed 2026 nobs 3 success True steps 84 time 3.3
          28 +seed 2027 nobs 3 success True steps 40 time 1.8
          29 +seed 2028 nobs 3 success True steps 72 time 3.2
          30 +seed 2029 nobs 3 success True steps 96 time 4.0
          31 +seed 2030 nobs 3 success True steps 57 time 2.4
          32 +seed 2031 nobs 3 success True steps 80 time 3.1
          33 +seed 2032 nobs 3 success True steps 90 time 4.3
          34 +seed 2033 nobs 3 success True steps 80 time 2.3
          35 +seed 2034 nobs 3 success True steps 103 time 4.2
          36 +seed 2035 nobs 3 success True steps 61 time 2.1
          37 +seed 2036 nobs 3 success True steps 77 time 3.2
          38 +seed 2037 nobs 3 success True steps 18 time 0.6
          39 +seed 2038 nobs 3 success True steps 65 time 3.0
          40 +seed 2039 nobs 3 success True steps 70 time 3.0
          41 +seed 2040 nobs 3 success True steps 59 time 1.5
          42 +seed 2041 nobs 3 success True steps 84 time 3.3
          43 +seed 2042 nobs 3 success True steps 71 time 2.7
          44 +seed 2043 nobs 3 success True steps 124 time 5.3
          45 +seed 2044 nobs 3 success True steps 67 time 2.5
          46 +seed 2045 nobs 3 success True steps 64 time 2.6
          47 +seed 2046 nobs 3 success True steps 74 time 3.4
          48 +seed 2047 nobs 3 success True steps 55 time 2.3
          49 +seed 2048 nobs 3 success True steps 82 time 2.8
          50 +seed 2049 nobs 3 success True steps 47 time 2.1
          51 +seed 2050 nobs 3 success True steps 47 time 2.3
          52 +seed 2051 nobs 3 success True steps 48 time 1.9
          53 +seed 2052 nobs 3 success True steps 97 time 4.5
          54 +seed 2053 nobs 3 success True steps 91 time 3.8
          55 +seed 2054 nobs 3 success True steps 68 time 2.5
          56 +seed 2055 nobs 3 success True steps 69 time 2.4
          57 +seed 2056 nobs 3 success True steps 42 time 1.5
          58 +seed 2057 nobs 3 success True steps 83 time 4.9
          59 +seed 2058 nobs 3 success True steps 64 time 4.1
          60 +seed 2059 nobs 3 success True steps 46 time 2.3
          61 +seed 2060 nobs 3 success True steps 30 time 1.4
          62 +seed 2061 nobs 3 success True steps 53 time 3.4
          63 +seed 2062 nobs 3 success True steps 44 time 2.6
          64 +seed 2063 nobs 3 success True steps 102 time 5.0
          65 +seed 2064 nobs 3 success True steps 36 time 2.4
          66 +seed 2065 nobs 3 success True steps 42 time 2.1
          67 +seed 2066 nobs 3 success True steps 50 time 2.4
          68 +seed 2067 nobs 3 success True steps 78 time 4.8
          69 +seed 2068 nobs 3 success True steps 66 time 3.3
          70 +seed 2069 nobs 3 success True steps 71 time 4.0
          71 +seed 2070 nobs 3 success True steps 63 time 3.3
          72 +seed 2071 nobs 3 success True steps 55 time 2.7
          73 +seed 2072 nobs 3 success True steps 74 time 4.5
          74 +seed 2073 nobs 3 success True steps 60 time 3.2
          75 +seed 2074 nobs 3 success True steps 64 time 3.3
          76 +seed 2075 nobs 3 success True steps 40 time 2.7
          77 +seed 2076 nobs 3 success True steps 69 time 4.7
          78 +seed 2077 nobs 3 success True steps 64 time 3.7
          79 +seed 2078 nobs 3 success True steps 48 time 2.9
          80 +seed 2079 nobs 3 success True steps 51 time 2.8
          81 +seed 2080 nobs 3 success True steps 58 time 2.9
          82 +seed 2081 nobs 3 success True steps 74 time 4.6
          83 +seed 2082 nobs 3 success True steps 73 time 4.1
          84 +seed 2083 nobs 3 success False steps 1000 time 41.7
          85 +seed 2084 nobs 3 success True steps 84 time 2.4
          86 +seed 2085 nobs 3 success True steps 55 time 5.7
          87 +seed 2086 nobs 3 success True steps 69 time 6.4
          88 +seed 2087 nobs 3 success True steps 76 time 2.5
          89 +seed 2088 nobs 3 success True steps 20 time 0.8
          90 +seed 2089 nobs 3 success True steps 59 time 6.1
          91 +seed 2090 nobs 3 success True steps 80 time 6.9
          92 +seed 2091 nobs 3 success True steps 53 time 1.9
          93 +seed 2092 nobs 3 success True steps 89 time 7.3
          94 +seed 2093 nobs 3 success True steps 69 time 7.2
          95 +seed 2094 nobs 3 success True steps 45 time 3.9
          96 +seed 2095 nobs 3 success False steps 1000 time 53.1
          97 +seed 2096 nobs 3 success True steps 73 time 6.9
          98 +seed 2097 nobs 3 success True steps 78 time 4.3
          99 +seed 2098 nobs 3 success True steps 19 time 0.5
         100 +seed 2099 nobs 3 success True steps 126 time 5.0
         101 +success 98 / 100
diff --git a/r4.txt b/r4.txt
index 83560bf..684115e 100644
--- a/r4.txt
+++ b/r4.txt
@@ -1,6 +1,101 @@
    1        -seed 1000 nobs 4 success True steps 160 time 6.5
    2        -seed 1001 nobs 4 success True steps 158 time 5.8
    3        -seed 1002 nobs 4 success True steps 245 time 9.4
    4        -seed 1003 nobs 4 success True steps 160 time 6.7
    5        -seed 1004 nobs 4 success True steps 140 time 6.0
    6        -seed 1005 nobs 4 success True steps 145 time 6.0
           1 +seed 1000 nobs 4 success True steps 65 time 2.4
           2 +seed 1001 nobs 4 success True steps 43 time 1.5
           3 +seed 1002 nobs 4 success True steps 92 time 3.7
           4 +seed 1003 nobs 4 success True steps 50 time 1.3
           5 +seed 1004 nobs 4 success True steps 51 time 2.4
           6 +seed 1005 nobs 4 success True steps 63 time 2.1
           7 +seed 1006 nobs 4 success True steps 88 time 3.5
           8 +seed 1007 nobs 4 success True steps 41 time 2.0
           9 +seed 1008 nobs 4 success True steps 73 time 3.4
          10 +seed 1009 nobs 4 success True steps 69 time 2.8
          11 +seed 1010 nobs 4 success True steps 92 time 3.7
          12 +seed 1011 nobs 4 success True steps 55 time 2.3
          13 +seed 1012 nobs 4 success True steps 59 time 2.7
          14 +seed 1013 nobs 4 success True steps 107 time 4.4
          15 +seed 1014 nobs 4 success True steps 78 time 3.3
          16 +seed 1015 nobs 4 success True steps 60 time 2.8
          17 +seed 1016 nobs 4 success True steps 73 time 3.0
          18 +seed 1017 nobs 4 success True steps 44 time 1.8
          19 +seed 1018 nobs 4 success True steps 89 time 3.9
          20 +seed 1019 nobs 4 success True steps 68 time 3.0
          21 +seed 1020 nobs 4 success True steps 87 time 4.5
          22 +seed 1021 nobs 4 success True steps 99 time 4.2
          23 +seed 1022 nobs 4 success True steps 78 time 3.7
          24 +seed 1023 nobs 4 success True steps 48 time 3.1
          25 +seed 1024 nobs 4 success True steps 73 time 3.6
          26 +seed 1025 nobs 4 success True steps 89 time 5.4
          27 +seed 1026 nobs 4 success True steps 117 time 6.2
          28 +seed 1027 nobs 4 success True steps 88 time 5.7
          29 +seed 1028 nobs 4 success True steps 102 time 7.4
          30 +seed 1029 nobs 4 success True steps 72 time 3.1
          31 +seed 1030 nobs 4 success True steps 77 time 2.7
          32 +seed 1031 nobs 4 success True steps 71 time 2.7
          33 +seed 1032 nobs 4 success True steps 64 time 6.0
          34 +seed 1033 nobs 4 success True steps 57 time 5.1
          35 +seed 1034 nobs 4 success True steps 81 time 4.7
          36 +seed 1035 nobs 4 success True steps 111 time 11.4
          37 +seed 1036 nobs 4 success True steps 48 time 1.6
          38 +seed 1037 nobs 4 success True steps 86 time 2.8
          39 +seed 1038 nobs 4 success True steps 109 time 4.9
          40 +seed 1039 nobs 4 success True steps 61 time 6.1
          41 +seed 1040 nobs 4 success True steps 108 time 5.0
          42 +seed 1041 nobs 4 success True steps 87 time 1.9
          43 +seed 1042 nobs 4 success True steps 112 time 2.3
          44 +seed 1043 nobs 4 success True steps 53 time 0.9
          45 +seed 1044 nobs 4 success True steps 90 time 1.5
          46 +seed 1045 nobs 4 success True steps 98 time 1.8
          47 +seed 1046 nobs 4 success True steps 46 time 0.8
          48 +seed 1047 nobs 4 success True steps 52 time 0.9
          49 +seed 1048 nobs 4 success True steps 59 time 0.8
          50 +seed 1049 nobs 4 success True steps 106 time 0.7
          51 +seed 1050 nobs 4 success True steps 44 time 0.3
          52 +seed 1051 nobs 4 success True steps 80 time 0.5
          53 +seed 1052 nobs 4 success True steps 61 time 0.4
          54 +seed 1053 nobs 4 success True steps 79 time 0.5
          55 +seed 1054 nobs 4 success True steps 99 time 0.7
          56 +seed 1055 nobs 4 success True steps 57 time 0.4
          57 +seed 1056 nobs 4 success True steps 84 time 0.5
          58 +seed 1057 nobs 4 success True steps 80 time 0.6
          59 +seed 1058 nobs 4 success True steps 72 time 0.4
          60 +seed 1059 nobs 4 success True steps 72 time 0.4
          61 +seed 1060 nobs 4 success True steps 58 time 0.4
          62 +seed 1061 nobs 4 success True steps 43 time 0.4
          63 +seed 1062 nobs 4 success True steps 105 time 0.7
          64 +seed 1063 nobs 4 success True steps 51 time 0.3
          65 +seed 1064 nobs 4 success True steps 127 time 0.9
          66 +seed 1065 nobs 4 success True steps 83 time 0.5
          67 +seed 1066 nobs 4 success True steps 82 time 0.6
          68 +seed 1067 nobs 4 success True steps 59 time 0.9
          69 +seed 1068 nobs 4 success True steps 81 time 5.0
          70 +seed 1069 nobs 4 success True steps 90 time 0.6
          71 +seed 1070 nobs 4 success True steps 138 time 0.9
          72 +seed 1071 nobs 4 success True steps 83 time 0.6
          73 +seed 1072 nobs 4 success True steps 75 time 0.5
          74 +seed 1073 nobs 4 success True steps 30 time 0.3
          75 +seed 1074 nobs 4 success True steps 74 time 0.4
          76 +seed 1075 nobs 4 success True steps 26 time 0.1
          77 +seed 1076 nobs 4 success True steps 81 time 0.7
          78 +seed 1077 nobs 4 success True steps 103 time 0.7
          79 +seed 1078 nobs 4 success True steps 98 time 0.7
          80 +seed 1079 nobs 4 success True steps 116 time 0.8
          81 +seed 1080 nobs 4 success True steps 68 time 0.4
          82 +seed 1081 nobs 4 success True steps 55 time 0.4
          83 +seed 1082 nobs 4 success True steps 125 time 0.8
          84 +seed 1083 nobs 4 success True steps 81 time 0.6
          85 +seed 1084 nobs 4 success True steps 52 time 0.4
          86 +seed 1085 nobs 4 success True steps 118 time 0.8
          87 +seed 1086 nobs 4 success True steps 91 time 0.6
          88 +seed 1087 nobs 4 success True steps 78 time 0.5
          89 +seed 1088 nobs 4 success True steps 92 time 0.6
          90 +seed 1089 nobs 4 success True steps 64 time 3.2
          91 +seed 1090 nobs 4 success True steps 84 time 2.3
          92 +seed 1091 nobs 4 success True steps 122 time 1.3
          93 +seed 1092 nobs 4 success True steps 117 time 0.7
          94 +seed 1093 nobs 4 success True steps 67 time 0.5
          95 +seed 1094 nobs 4 success True steps 47 time 0.3
          96 +seed 1095 nobs 4 success True steps 88 time 0.6
          97 +seed 1096 nobs 4 success True steps 94 time 0.9
          98 +seed 1097 nobs 4 success True steps 84 time 0.5
          99 +seed 1098 nobs 4 success True steps 90 time 0.6
         100 +seed 1099 nobs 4 success True steps 85 time 0.6
         101 +success 100 / 100
diff --git a/rd.txt b/rd.txt
index 0bcb4be..d5df934 100644
--- a/rd.txt
+++ b/rd.txt
@@ -1,22 +1,301 @@
    1        -seed 3000 nobs 2 success True steps 178 time 6.6
    2        -seed 3001 nobs 0 success True steps 50 time 1.8
    3        -seed 3002 nobs 1 success True steps 111 time 3.2
    4        -seed 3003 nobs 2 success True steps 148 time 5.2
    5        -seed 3004 nobs 0 success True steps 52 time 1.9
    6        -seed 3005 nobs 1 success True steps 108 time 4.1
    7        -seed 3006 nobs 0 success True steps 51 time 2.0
    8        -seed 3007 nobs 2 success True steps 91 time 2.2
    9        -seed 3008 nobs 2 success True steps 99 time 3.4
   10        -seed 3009 nobs 0 success True steps 58 time 2.2
   11        -seed 3010 nobs 2 success True steps 176 time 4.0
   12        -seed 3011 nobs 2 success True steps 176 time 5.9
   13        -seed 3012 nobs 1 success True steps 111 time 3.4
   14        -seed 3013 nobs 2 success True steps 160 time 5.7
   15        -seed 3014 nobs 0 success True steps 43 time 1.1
   16        -seed 3015 nobs 1 success True steps 91 time 2.4
   17        -seed 3016 nobs 2 success True steps 133 time 3.7
   18        -seed 3017 nobs 0 success True steps 37 time 1.2
   19        -seed 3018 nobs 1 success True steps 101 time 3.4
   20        -seed 3019 nobs 2 success True steps 158 time 7.0
   21        -seed 3020 nobs 1 success True steps 107 time 3.0
   22        -seed 3021 nobs 1 success True steps 86 time 2.0
           1 +seed 0 nobs 2 success True steps 55 time 1.2
           2 +seed 1 nobs 1 success True steps 42 time 1.5
           3 +seed 2 nobs 2 success True steps 56 time 2.0
           4 +seed 3 nobs 2 success True steps 47 time 1.8
           5 +seed 4 nobs 2 success True steps 67 time 2.7
           6 +seed 5 nobs 2 success True steps 77 time 2.1
           7 +seed 6 nobs 1 success True steps 36 time 1.5
           8 +seed 7 nobs 2 success True steps 91 time 3.0
           9 +seed 8 nobs 2 success True steps 57 time 1.4
          10 +seed 9 nobs 1 success True steps 74 time 2.4
          11 +seed 10 nobs 2 success True steps 69 time 1.9
          12 +seed 11 nobs 0 success True steps 37 time 0.8
          13 +seed 12 nobs 1 success True steps 71 time 1.7
          14 +seed 13 nobs 2 success True steps 54 time 1.6
          15 +seed 14 nobs 0 success True steps 19 time 0.5
          16 +seed 15 nobs 2 success True steps 29 time 0.8
          17 +seed 16 nobs 1 success True steps 17 time 0.3
          18 +seed 17 nobs 2 success True steps 58 time 2.2
          19 +seed 18 nobs 2 success True steps 64 time 2.2
          20 +seed 19 nobs 1 success True steps 36 time 1.1
          21 +seed 20 nobs 2 success True steps 48 time 0.8
          22 +seed 21 nobs 0 success True steps 44 time 1.3
          23 +seed 22 nobs 2 success True steps 63 time 2.3
          24 +seed 23 nobs 0 success True steps 34 time 0.6
          25 +seed 24 nobs 1 success True steps 41 time 0.9
          26 +seed 25 nobs 1 success True steps 32 time 0.5
          27 +seed 26 nobs 2 success True steps 81 time 2.5
          28 +seed 27 nobs 0 success True steps 12 time 0.5
          29 +seed 28 nobs 1 success True steps 38 time 1.1
          30 +seed 29 nobs 2 success True steps 22 time 0.9
          31 +seed 30 nobs 0 success True steps 18 time 0.7
          32 +seed 31 nobs 1 success True steps 45 time 1.6
          33 +seed 32 nobs 2 success True steps 58 time 2.7
          34 +seed 33 nobs 2 success True steps 60 time 2.6
          35 +seed 34 nobs 0 success True steps 25 time 0.8
          36 +seed 35 nobs 0 success True steps 24 time 0.8
          37 +seed 36 nobs 1 success True steps 26 time 1.1
          38 +seed 37 nobs 0 success True steps 25 time 1.0
          39 +seed 38 nobs 0 success True steps 14 time 0.5
          40 +seed 39 nobs 2 success True steps 50 time 1.5
          41 +seed 40 nobs 1 success True steps 49 time 1.6
          42 +seed 41 nobs 1 success True steps 49 time 1.9
          43 +seed 42 nobs 0 success True steps 24 time 0.9
          44 +seed 43 nobs 1 success True steps 37 time 1.6
          45 +seed 44 nobs 2 success True steps 47 time 1.8
          46 +seed 45 nobs 2 success True steps 61 time 1.6
          47 +seed 46 nobs 1 success True steps 37 time 1.4
          48 +seed 47 nobs 0 success True steps 31 time 0.5
          49 +seed 48 nobs 0 success True steps 14 time 0.3
          50 +seed 49 nobs 0 success True steps 14 time 0.6
          51 +seed 50 nobs 2 success True steps 59 time 2.5
          52 +seed 51 nobs 1 success True steps 30 time 1.1
          53 +seed 52 nobs 2 success True steps 47 time 1.5
          54 +seed 53 nobs 2 success True steps 66 time 2.0
          55 +seed 54 nobs 0 success True steps 23 time 0.7
          56 +seed 55 nobs 2 success True steps 50 time 1.8
          57 +seed 56 nobs 1 success True steps 52 time 1.8
          58 +seed 57 nobs 0 success True steps 11 time 0.2
          59 +seed 58 nobs 1 success True steps 41 time 1.4
          60 +seed 59 nobs 2 success True steps 70 time 3.1
          61 +seed 60 nobs 0 success True steps 18 time 0.5
          62 +seed 61 nobs 1 success True steps 51 time 2.3
          63 +seed 62 nobs 1 success True steps 51 time 1.8
          64 +seed 63 nobs 1 success True steps 24 time 0.6
          65 +seed 64 nobs 1 success True steps 21 time 0.6
          66 +seed 65 nobs 0 success True steps 13 time 0.4
          67 +seed 66 nobs 2 success True steps 39 time 1.3
          68 +seed 67 nobs 2 success True steps 28 time 0.9
          69 +seed 68 nobs 1 success True steps 26 time 1.0
          70 +seed 69 nobs 0 success True steps 30 time 1.2
          71 +seed 70 nobs 1 success True steps 30 time 1.1
          72 +seed 71 nobs 2 success True steps 20 time 0.7
          73 +seed 72 nobs 2 success True steps 83 time 2.6
          74 +seed 73 nobs 2 success True steps 60 time 2.6
          75 +seed 74 nobs 0 success True steps 17 time 0.3
          76 +seed 75 nobs 1 success True steps 61 time 2.3
          77 +seed 76 nobs 1 success True steps 53 time 1.8
          78 +seed 77 nobs 0 success True steps 14 time 0.4
          79 +seed 78 nobs 2 success True steps 50 time 1.6
          80 +seed 79 nobs 0 success True steps 27 time 0.6
          81 +seed 80 nobs 2 success True steps 60 time 2.0
          82 +seed 81 nobs 0 success True steps 19 time 0.7
          83 +seed 82 nobs 2 success True steps 65 time 2.4
          84 +seed 83 nobs 2 success True steps 66 time 3.4
          85 +seed 84 nobs 1 success True steps 52 time 1.6
          86 +seed 85 nobs 2 success True steps 54 time 1.3
          87 +seed 86 nobs 2 success True steps 31 time 1.4
          88 +seed 87 nobs 1 success True steps 36 time 1.0
          89 +seed 88 nobs 1 success True steps 46 time 1.3
          90 +seed 89 nobs 2 success True steps 44 time 1.0
          91 +seed 90 nobs 1 success True steps 55 time 1.9
          92 +seed 91 nobs 2 success True steps 26 time 1.1
          93 +seed 92 nobs 1 success True steps 35 time 1.1
          94 +seed 93 nobs 2 success True steps 53 time 2.1
          95 +seed 94 nobs 0 success True steps 17 time 0.5
          96 +seed 95 nobs 1 success True steps 42 time 1.5
          97 +seed 96 nobs 2 success True steps 43 time 1.3
          98 +seed 97 nobs 0 success True steps 28 time 0.7
          99 +seed 98 nobs 1 success True steps 47 time 1.7
         100 +seed 99 nobs 2 success True steps 48 time 2.1
         101 +seed 100 nobs 2 success True steps 67 time 2.4
         102 +seed 101 nobs 0 success True steps 11 time 0.2
         103 +seed 102 nobs 1 success True steps 45 time 1.7
         104 +seed 103 nobs 1 success True steps 29 time 1.2
         105 +seed 104 nobs 2 success True steps 52 time 2.0
         106 +seed 105 nobs 0 success True steps 14 time 0.3
         107 +seed 106 nobs 1 success True steps 38 time 1.1
         108 +seed 107 nobs 0 success True steps 23 time 0.8
         109 +seed 108 nobs 0 success True steps 18 time 0.7
         110 +seed 109 nobs 1 success True steps 32 time 1.0
         111 +seed 110 nobs 1 success True steps 57 time 1.7
         112 +seed 111 nobs 1 success True steps 40 time 1.5
         113 +seed 112 nobs 0 success True steps 20 time 0.7
         114 +seed 113 nobs 0 success True steps 33 time 1.0
         115 +seed 114 nobs 0 success True steps 14 time 0.5
         116 +seed 115 nobs 1 success True steps 53 time 2.0
         117 +seed 116 nobs 0 success True steps 42 time 1.1
         118 +seed 117 nobs 0 success True steps 20 time 0.6
         119 +seed 118 nobs 1 success True steps 38 time 1.1
         120 +seed 119 nobs 1 success True steps 48 time 1.6
         121 +seed 120 nobs 0 success True steps 14 time 0.2
         122 +seed 121 nobs 0 success True steps 19 time 0.6
         123 +seed 122 nobs 2 success True steps 63 time 2.3
         124 +seed 123 nobs 0 success True steps 32 time 1.1
         125 +seed 124 nobs 2 success True steps 38 time 1.2
         126 +seed 125 nobs 1 success True steps 61 time 2.1
         127 +seed 126 nobs 0 success True steps 11 time 0.7
         128 +seed 127 nobs 1 success True steps 56 time 2.3
         129 +seed 128 nobs 2 success True steps 80 time 3.5
         130 +seed 129 nobs 1 success True steps 49 time 2.2
         131 +seed 130 nobs 2 success True steps 43 time 2.3
         132 +seed 131 nobs 1 success True steps 45 time 1.8
         133 +seed 132 nobs 2 success True steps 70 time 3.7
         134 +seed 133 nobs 1 success True steps 54 time 2.8
         135 +seed 134 nobs 2 success True steps 12 time 0.5
         136 +seed 135 nobs 1 success True steps 12 time 0.6
         137 +seed 136 nobs 2 success True steps 32 time 1.9
         138 +seed 137 nobs 1 success True steps 63 time 2.5
         139 +seed 138 nobs 1 success True steps 70 time 3.5
         140 +seed 139 nobs 1 success True steps 74 time 4.1
         141 +seed 140 nobs 1 success True steps 26 time 0.9
         142 +seed 141 nobs 1 success True steps 41 time 1.8
         143 +seed 142 nobs 0 success True steps 45 time 1.9
         144 +seed 143 nobs 2 success True steps 51 time 2.4
         145 +seed 144 nobs 0 success True steps 30 time 1.2
         146 +seed 145 nobs 1 success True steps 23 time 1.1
         147 +seed 146 nobs 2 success True steps 36 time 1.9
         148 +seed 147 nobs 0 success True steps 17 time 0.9
         149 +seed 148 nobs 0 success True steps 12 time 0.3
         150 +seed 149 nobs 0 success True steps 22 time 0.8
         151 +seed 150 nobs 1 success True steps 28 time 1.1
         152 +seed 151 nobs 2 success True steps 39 time 1.8
         153 +seed 152 nobs 2 success True steps 33 time 1.4
         154 +seed 153 nobs 2 success True steps 42 time 2.3
         155 +seed 154 nobs 0 success True steps 31 time 1.0
         156 +seed 155 nobs 0 success True steps 19 time 0.7
         157 +seed 156 nobs 2 success True steps 47 time 2.0
         158 +seed 157 nobs 0 success True steps 29 time 0.9
         159 +seed 158 nobs 1 success True steps 59 time 2.7
         160 +seed 159 nobs 2 success True steps 48 time 2.9
         161 +seed 160 nobs 0 success True steps 15 time 0.9
         162 +seed 161 nobs 2 success True steps 32 time 2.0
         163 +seed 162 nobs 1 success True steps 37 time 1.8
         164 +seed 163 nobs 1 success True steps 33 time 1.7
         165 +seed 164 nobs 1 success True steps 30 time 1.2
         166 +seed 165 nobs 1 success True steps 53 time 2.6
         167 +seed 166 nobs 2 success True steps 30 time 1.5
         168 +seed 167 nobs 2 success True steps 60 time 3.3
         169 +seed 168 nobs 1 success True steps 57 time 3.0
         170 +seed 169 nobs 2 success True steps 74 time 4.3
         171 +seed 170 nobs 2 success True steps 51 time 3.0
         172 +seed 171 nobs 2 success True steps 54 time 2.3
         173 +seed 172 nobs 1 success True steps 28 time 1.6
         174 +seed 173 nobs 2 success True steps 64 time 3.2
         175 +seed 174 nobs 1 success True steps 50 time 2.9
         176 +seed 175 nobs 2 success True steps 36 time 1.4
         177 +seed 176 nobs 0 success True steps 28 time 1.3
         178 +seed 177 nobs 2 success True steps 41 time 2.4
         179 +seed 178 nobs 1 success True steps 63 time 2.8
         180 +seed 179 nobs 2 success True steps 39 time 2.4
         181 +seed 180 nobs 0 success True steps 29 time 1.2
         182 +seed 181 nobs 2 success True steps 58 time 2.8
         183 +seed 182 nobs 2 success True steps 74 time 2.7
         184 +seed 183 nobs 2 success True steps 79 time 2.7
         185 +seed 184 nobs 1 success True steps 46 time 0.7
         186 +seed 185 nobs 0 success True steps 19 time 0.4
         187 +seed 186 nobs 0 success True steps 16 time 0.6
         188 +seed 187 nobs 1 success True steps 35 time 1.4
         189 +seed 188 nobs 1 success True steps 29 time 1.0
         190 +seed 189 nobs 1 success True steps 51 time 2.0
         191 +seed 190 nobs 0 success True steps 13 time 0.3
         192 +seed 191 nobs 0 success True steps 24 time 0.4
         193 +seed 192 nobs 2 success True steps 52 time 1.6
         194 +seed 193 nobs 1 success True steps 44 time 1.3
         195 +seed 194 nobs 2 success True steps 51 time 1.6
         196 +seed 195 nobs 0 success True steps 18 time 0.5
         197 +seed 196 nobs 0 success True steps 33 time 0.9
         198 +seed 197 nobs 2 success True steps 79 time 3.2
         199 +seed 198 nobs 1 success True steps 43 time 1.3
         200 +seed 199 nobs 1 success True steps 40 time 1.6
         201 +seed 200 nobs 0 success True steps 17 time 0.3
         202 +seed 201 nobs 0 success True steps 20 time 0.5
         203 +seed 202 nobs 0 success True steps 26 time 0.5
         204 +seed 203 nobs 0 success True steps 29 time 0.8
         205 +seed 204 nobs 2 success True steps 49 time 2.0
         206 +seed 205 nobs 1 success True steps 33 time 1.3
         207 +seed 206 nobs 1 success True steps 41 time 0.9
         208 +seed 207 nobs 0 success True steps 15 time 0.2
         209 +seed 208 nobs 2 success True steps 41 time 2.8
         210 +seed 209 nobs 2 success True steps 27 time 2.3
         211 +seed 210 nobs 0 success True steps 16 time 1.2
         212 +seed 211 nobs 0 success True steps 23 time 1.3
         213 +seed 212 nobs 0 success True steps 25 time 1.1
         214 +seed 213 nobs 0 success True steps 14 time 0.8
         215 +seed 214 nobs 0 success True steps 38 time 2.4
         216 +seed 215 nobs 2 success True steps 59 time 1.8
         217 +seed 216 nobs 2 success True steps 49 time 2.3
         218 +seed 217 nobs 2 success True steps 61 time 5.4
         219 +seed 218 nobs 1 success True steps 25 time 2.2
         220 +seed 219 nobs 0 success True steps 17 time 1.3
         221 +seed 220 nobs 2 success True steps 54 time 3.7
         222 +seed 221 nobs 1 success True steps 48 time 1.3
         223 +seed 222 nobs 1 success True steps 36 time 1.1
         224 +seed 223 nobs 1 success True steps 39 time 0.8
         225 +seed 224 nobs 2 success True steps 43 time 2.1
         226 +seed 225 nobs 2 success True steps 76 time 7.7
         227 +seed 226 nobs 2 success True steps 54 time 4.9
         228 +seed 227 nobs 1 success True steps 33 time 1.8
         229 +seed 228 nobs 1 success True steps 37 time 2.8
         230 +seed 229 nobs 1 success True steps 19 time 1.5
         231 +seed 230 nobs 1 success True steps 28 time 2.1
         232 +seed 231 nobs 0 success True steps 27 time 1.7
         233 +seed 232 nobs 1 success True steps 34 time 1.4
         234 +seed 233 nobs 0 success True steps 18 time 0.5
         235 +seed 234 nobs 1 success True steps 30 time 0.8
         236 +seed 235 nobs 2 success True steps 57 time 1.3
         237 +seed 236 nobs 1 success True steps 58 time 2.0
         238 +seed 237 nobs 2 success True steps 67 time 2.7
         239 +seed 238 nobs 1 success True steps 10 time 0.3
         240 +seed 239 nobs 2 success True steps 62 time 1.6
         241 +seed 240 nobs 2 success True steps 65 time 2.1
         242 +seed 241 nobs 1 success True steps 10 time 0.4
         243 +seed 242 nobs 2 success True steps 60 time 2.4
         244 +seed 243 nobs 2 success True steps 43 time 1.8
         245 +seed 244 nobs 2 success True steps 46 time 1.7
         246 +seed 245 nobs 2 success True steps 72 time 2.6
         247 +seed 246 nobs 2 success True steps 59 time 2.4
         248 +seed 247 nobs 0 success True steps 24 time 0.4
         249 +seed 248 nobs 1 success True steps 40 time 1.6
         250 +seed 249 nobs 2 success True steps 52 time 1.5
         251 +seed 250 nobs 1 success True steps 62 time 3.8
         252 +seed 251 nobs 0 success True steps 15 time 0.9
         253 +seed 252 nobs 2 success True steps 72 time 6.4
         254 +seed 253 nobs 1 success True steps 48 time 4.4
         255 +seed 254 nobs 0 success True steps 23 time 0.8
         256 +seed 255 nobs 0 success True steps 18 time 0.6
         257 +seed 256 nobs 1 success True steps 28 time 0.9
         258 +seed 257 nobs 2 success True steps 22 time 0.8
         259 +seed 258 nobs 1 success True steps 35 time 1.1
         260 +seed 259 nobs 0 success True steps 12 time 0.4
         261 +seed 260 nobs 2 success True steps 40 time 1.4
         262 +seed 261 nobs 1 success True steps 71 time 1.8
         263 +seed 262 nobs 2 success True steps 52 time 1.7
         264 +seed 263 nobs 2 success True steps 58 time 0.8
         265 +seed 264 nobs 0 success True steps 34 time 0.3
         266 +seed 265 nobs 2 success True steps 47 time 1.0
         267 +seed 266 nobs 1 success True steps 34 time 0.5
         268 +seed 267 nobs 1 success True steps 33 time 0.4
         269 +seed 268 nobs 2 success True steps 72 time 1.6
         270 +seed 269 nobs 2 success True steps 66 time 1.1
         271 +seed 270 nobs 1 success True steps 33 time 0.5
         272 +seed 271 nobs 2 success True steps 39 time 0.5
         273 +seed 272 nobs 0 success True steps 10 time 0.1
         274 +seed 273 nobs 0 success True steps 24 time 0.3
         275 +seed 274 nobs 1 success True steps 79 time 1.2
         276 +seed 275 nobs 0 success True steps 28 time 0.4
         277 +seed 276 nobs 1 success True steps 33 time 1.0
         278 +seed 277 nobs 0 success True steps 26 time 0.3
         279 +seed 278 nobs 1 success True steps 37 time 0.6
         280 +seed 279 nobs 1 success True steps 37 time 1.2
         281 +seed 280 nobs 1 success True steps 49 time 1.0
         282 +seed 281 nobs 1 success True steps 34 time 0.3
         283 +seed 282 nobs 2 success True steps 38 time 0.7
         284 +seed 283 nobs 0 success True steps 45 time 0.7
         285 +seed 284 nobs 0 success True steps 18 time 0.2
         286 +seed 285 nobs 2 success True steps 69 time 1.5
         287 +seed 286 nobs 0 success True steps 24 time 0.3
         288 +seed 287 nobs 2 success True steps 90 time 1.1
         289 +seed 288 nobs 0 success True steps 16 time 0.3
         290 +seed 289 nobs 1 success True steps 20 time 0.2
         291 +seed 290 nobs 0 success True steps 31 time 0.5
         292 +seed 291 nobs 0 success True steps 27 time 0.3
         293 +seed 292 nobs 2 success True steps 112 time 2.6
         294 +seed 293 nobs 0 success True steps 26 time 0.3
         295 +seed 294 nobs 0 success True steps 24 time 0.3
         296 +seed 295 nobs 0 success True steps 42 time 0.7
         297 +seed 296 nobs 0 success True steps 19 time 0.2
         298 +seed 297 nobs 0 success True steps 27 time 0.4
         299 +seed 298 nobs 1 success True steps 35 time 0.9
         300 +seed 299 nobs 2 success True steps 83 time 1.9
         301 +success 300 / 300
diff --git a/res_0.txt b/res_0.txt
deleted file mode 100644
index cdf493c..0000000
--- a/res_0.txt
+++ /dev/null
@@ -1,51 +0,0 @@
    1        -seed 10 nobs 2 success True steps 165 time 6.5
    2        -seed 11 nobs 0 success True steps 66 time 2.6
    3        -seed 12 nobs 1 success True steps 141 time 7.0
    4        -seed 13 nobs 2 success True steps 153 time 4.3
    5        -seed 14 nobs 0 success True steps 45 time 1.9
    6        -seed 15 nobs 2 success True steps 92 time 5.0
    7        -seed 16 nobs 1 success True steps 45 time 1.1
    8        -seed 17 nobs 2 success True steps 158 time 8.1
    9        -seed 18 nobs 2 success True steps 180 time 9.5
   10        -seed 19 nobs 1 success True steps 101 time 4.9
   11        -seed 20 nobs 2 success True steps 119 time 6.1
   12        -seed 21 nobs 0 success False steps 1000 time 41.4
   13        -seed 22 nobs 2 success True steps 163 time 8.3
   14        -seed 23 nobs 0 success True steps 68 time 3.3
   15        -seed 24 nobs 1 success True steps 125 time 4.6
   16        -seed 25 nobs 1 success True steps 93 time 4.3
   17        -seed 26 nobs 2 success True steps 162 time 7.7
   18        -seed 27 nobs 0 success True steps 49 time 2.0
   19        -seed 28 nobs 1 success True steps 65 time 2.3
   20        -seed 29 nobs 2 success True steps 99 time 5.3
   21        -seed 30 nobs 0 success True steps 55 time 2.2
   22        -seed 31 nobs 1 success False steps 1000 time 44.2
   23        -seed 32 nobs 2 success True steps 165 time 8.0
   24        -seed 33 nobs 2 success True steps 143 time 8.3
   25        -seed 34 nobs 0 success True steps 53 time 1.1
   26        -seed 35 nobs 0 success True steps 51 time 1.6
   27        -seed 36 nobs 1 success True steps 89 time 3.8
   28        -seed 37 nobs 0 success True steps 53 time 2.3
   29        -seed 38 nobs 0 success True steps 46 time 1.9
   30        -seed 39 nobs 2 success True steps 175 time 10.1
   31        -seed 40 nobs 1 success True steps 116 time 5.3
   32        -seed 41 nobs 1 success True steps 113 time 2.8
   33        -seed 42 nobs 0 success True steps 48 time 1.3
   34        -seed 43 nobs 1 success True steps 119 time 4.0
   35        -seed 44 nobs 2 success True steps 155 time 7.0
   36        -seed 45 nobs 2 success True steps 170 time 8.6
   37        -seed 46 nobs 1 success True steps 114 time 5.4
   38        -seed 47 nobs 0 success True steps 61 time 0.8
   39        -seed 48 nobs 0 success True steps 47 time 1.0
   40        -seed 49 nobs 0 success True steps 41 time 0.7
   41        -seed 50 nobs 2 success True steps 170 time 2.6
   42        -seed 51 nobs 1 success True steps 102 time 1.2
   43        -seed 52 nobs 2 success True steps 160 time 3.5
   44        -seed 53 nobs 2 success True steps 169 time 3.8
   45        -seed 54 nobs 0 success True steps 59 time 0.4
   46        -seed 55 nobs 2 success True steps 154 time 1.5
   47        -seed 56 nobs 1 success True steps 117 time 1.3
   48        -seed 57 nobs 0 success True steps 41 time 0.4
   49        -seed 58 nobs 1 success True steps 119 time 1.1
   50        -seed 59 nobs 2 success True steps 179 time 1.5
   51        -success 48 / 50
diff --git a/res_1.txt b/res_1.txt
deleted file mode 100644
index 51dea27..0000000
--- a/res_1.txt
+++ /dev/null
@@ -1,51 +0,0 @@
    1        -seed 60 nobs 0 success True steps 46 time 1.3
    2        -seed 61 nobs 1 success True steps 114 time 3.6
    3        -seed 62 nobs 1 success True steps 113 time 4.9
    4        -seed 63 nobs 1 success True steps 97 time 4.2
    5        -seed 64 nobs 1 success True steps 52 time 2.0
    6        -seed 65 nobs 0 success True steps 47 time 1.1
    7        -seed 66 nobs 2 success True steps 110 time 5.5
    8        -seed 67 nobs 2 success True steps 105 time 5.1
    9        -seed 68 nobs 1 success True steps 104 time 4.8
   10        -seed 69 nobs 0 success True steps 60 time 2.1
   11        -seed 70 nobs 1 success True steps 115 time 4.7
   12        -seed 71 nobs 2 success True steps 105 time 4.8
   13        -seed 72 nobs 2 success True steps 144 time 7.0
   14        -seed 73 nobs 2 success True steps 175 time 8.7
   15        -seed 74 nobs 0 success False steps 1000 time 40.9
   16        -seed 75 nobs 1 success False steps 1000 time 43.9
   17        -seed 76 nobs 1 success True steps 126 time 4.7
   18        -seed 77 nobs 0 success True steps 50 time 1.5
   19        -seed 78 nobs 2 success True steps 164 time 8.4
   20        -seed 79 nobs 0 success True steps 62 time 2.5
   21        -seed 80 nobs 2 success True steps 166 time 8.9
   22        -seed 81 nobs 0 success True steps 54 time 2.3
   23        -seed 82 nobs 2 success True steps 131 time 5.0
   24        -seed 83 nobs 2 success True steps 174 time 8.6
   25        -seed 84 nobs 1 success True steps 121 time 5.7
   26        -seed 85 nobs 2 success True steps 156 time 7.9
   27        -seed 86 nobs 2 success True steps 95 time 4.4
   28        -seed 87 nobs 1 success True steps 112 time 6.3
   29        -seed 88 nobs 1 success True steps 118 time 5.8
   30        -seed 89 nobs 2 success True steps 112 time 6.9
   31        -seed 90 nobs 1 success True steps 114 time 4.4
   32        -seed 91 nobs 2 success True steps 96 time 3.9
   33        -seed 92 nobs 1 success True steps 112 time 4.9
   34        -seed 93 nobs 2 success True steps 162 time 8.0
   35        -seed 94 nobs 0 success True steps 41 time 1.4
   36        -seed 95 nobs 1 success True steps 106 time 2.8
   37        -seed 96 nobs 2 success True steps 95 time 4.6
   38        -seed 97 nobs 0 success True steps 65 time 2.3
   39        -seed 98 nobs 1 success True steps 108 time 1.5
   40        -seed 99 nobs 2 success True steps 107 time 1.3
   41        -seed 100 nobs 2 success True steps 180 time 2.6
   42        -seed 101 nobs 0 success True steps 42 time 0.6
   43        -seed 102 nobs 1 success True steps 122 time 2.7
   44        -seed 103 nobs 1 success True steps 97 time 1.5
   45        -seed 104 nobs 2 success True steps 165 time 1.9
   46        -seed 105 nobs 0 success True steps 39 time 0.3
   47        -seed 106 nobs 1 success True steps 123 time 1.5
   48        -seed 107 nobs 0 success True steps 48 time 0.6
   49        -seed 108 nobs 0 success True steps 45 time 0.4
   50        -seed 109 nobs 1 success True steps 104 time 1.6
   51        -success 48 / 50
diff --git a/res_2.txt b/res_2.txt
deleted file mode 100644
index ad1b157..0000000
--- a/res_2.txt
+++ /dev/null
@@ -1,51 +0,0 @@
    1        -seed 110 nobs 1 success True steps 117 time 4.2
    2        -seed 111 nobs 1 success True steps 102 time 4.1
    3        -seed 112 nobs 0 success True steps 45 time 1.7
    4        -seed 113 nobs 0 success True steps 70 time 2.8
    5        -seed 114 nobs 0 success True steps 41 time 1.8
    6        -seed 115 nobs 1 success True steps 126 time 3.8
    7        -seed 116 nobs 0 success True steps 73 time 2.9
    8        -seed 117 nobs 0 success True steps 53 time 2.3
    9        -seed 118 nobs 1 success True steps 109 time 4.8
   10        -seed 119 nobs 1 success True steps 112 time 4.9
   11        -seed 120 nobs 0 success True steps 40 time 1.7
   12        -seed 121 nobs 0 success True steps 45 time 1.4
   13        -seed 122 nobs 2 success True steps 170 time 8.7
   14        -seed 123 nobs 0 success True steps 67 time 3.0
   15        -seed 124 nobs 2 success True steps 120 time 4.5
   16        -seed 125 nobs 1 success True steps 127 time 5.8
   17        -seed 126 nobs 0 success True steps 40 time 1.7
   18        -seed 127 nobs 1 success True steps 130 time 6.3
   19        -seed 128 nobs 2 success True steps 173 time 9.4
   20        -seed 129 nobs 1 success True steps 111 time 5.0
   21        -seed 130 nobs 2 success True steps 113 time 3.9
   22        -seed 131 nobs 1 success True steps 107 time 4.9
   23        -seed 132 nobs 2 success True steps 160 time 8.0
   24        -seed 133 nobs 1 success True steps 103 time 5.2
   25        -seed 134 nobs 2 success True steps 49 time 2.4
   26        -seed 135 nobs 1 success True steps 41 time 1.8
   27        -seed 136 nobs 2 success True steps 107 time 4.4
   28        -seed 137 nobs 1 success True steps 132 time 4.4
   29        -seed 138 nobs 1 success True steps 144 time 5.5
   30        -seed 139 nobs 1 success True steps 129 time 6.6
   31        -seed 140 nobs 1 success True steps 104 time 4.8
   32        -seed 141 nobs 1 success True steps 100 time 3.8
   33        -seed 142 nobs 0 success True steps 80 time 2.6
   34        -seed 143 nobs 2 success True steps 161 time 7.1
   35        -seed 144 nobs 0 success True steps 61 time 2.7
   36        -seed 145 nobs 1 success True steps 93 time 3.9
   37        -seed 146 nobs 2 success True steps 113 time 5.1
   38        -seed 147 nobs 0 success True steps 48 time 2.5
   39        -seed 148 nobs 0 success True steps 39 time 1.8
   40        -seed 149 nobs 0 success True steps 51 time 2.1
   41        -seed 150 nobs 1 success True steps 96 time 3.9
   42        -seed 151 nobs 2 success True steps 137 time 6.7
   43        -seed 152 nobs 2 success True steps 101 time 2.7
   44        -seed 153 nobs 2 success True steps 160 time 8.4
   45        -seed 154 nobs 0 success True steps 61 time 2.2
   46        -seed 155 nobs 0 success True steps 49 time 2.1
   47        -seed 156 nobs 2 success True steps 141 time 7.5
   48        -seed 157 nobs 0 success True steps 52 time 2.1
   49        -seed 158 nobs 1 success True steps 135 time 5.7
   50        -seed 159 nobs 2 success True steps 156 time 8.4
   51        -success 50 / 50
diff --git a/res_3.txt b/res_3.txt
deleted file mode 100644
index 6c248bd..0000000
--- a/res_3.txt
+++ /dev/null
@@ -1,51 +0,0 @@
    1        -seed 160 nobs 0 success True steps 46 time 1.4
    2        -seed 161 nobs 2 success True steps 111 time 3.2
    3        -seed 162 nobs 1 success True steps 110 time 5.4
    4        -seed 163 nobs 1 success True steps 115 time 5.8
    5        -seed 164 nobs 1 success True steps 100 time 3.0
    6        -seed 165 nobs 1 success True steps 126 time 5.7
    7        -seed 166 nobs 2 success True steps 107 time 5.6
    8        -seed 167 nobs 2 success True steps 165 time 8.9
    9        -seed 168 nobs 1 success True steps 129 time 5.5
   10        -seed 169 nobs 2 success True steps 187 time 10.1
   11        -seed 170 nobs 2 success True steps 157 time 8.2
   12        -seed 171 nobs 2 success True steps 161 time 9.0
   13        -seed 172 nobs 1 success True steps 94 time 4.9
   14        -seed 173 nobs 2 success True steps 170 time 8.5
   15        -seed 174 nobs 1 success True steps 101 time 4.3
   16        -seed 175 nobs 2 success True steps 107 time 4.0
   17        -seed 176 nobs 0 success True steps 57 time 2.2
   18        -seed 177 nobs 2 success True steps 119 time 5.8
   19        -seed 178 nobs 1 success True steps 119 time 6.1
   20        -seed 179 nobs 2 success True steps 115 time 4.5
   21        -seed 180 nobs 0 success True steps 57 time 2.3
   22        -seed 181 nobs 2 success True steps 164 time 6.3
   23        -seed 182 nobs 2 success True steps 181 time 9.5
   24        -seed 183 nobs 2 success True steps 179 time 9.6
   25        -seed 184 nobs 1 success True steps 114 time 4.9
   26        -seed 185 nobs 0 success True steps 50 time 2.0
   27        -seed 186 nobs 0 success True steps 46 time 2.0
   28        -seed 187 nobs 1 success True steps 109 time 5.3
   29        -seed 188 nobs 1 success True steps 95 time 4.2
   30        -seed 189 nobs 1 success True steps 131 time 6.3
   31        -seed 190 nobs 0 success True steps 46 time 2.1
   32        -seed 191 nobs 0 success True steps 54 time 1.9
   33        -seed 192 nobs 2 success True steps 163 time 6.5
   34        -seed 193 nobs 1 success True steps 116 time 2.6
   35        -seed 194 nobs 2 success True steps 158 time 7.6
   36        -seed 195 nobs 0 success True steps 50 time 2.0
   37        -seed 196 nobs 0 success True steps 61 time 2.6
   38        -seed 197 nobs 2 success True steps 184 time 8.3
   39        -seed 198 nobs 1 success True steps 119 time 5.8
   40        -seed 199 nobs 1 success True steps 105 time 5.0
   41        -seed 200 nobs 0 success True steps 51 time 2.2
   42        -seed 201 nobs 0 success True steps 53 time 1.5
   43        -seed 202 nobs 0 success True steps 57 time 2.0
   44        -seed 203 nobs 0 success True steps 63 time 2.5
   45        -seed 204 nobs 2 success True steps 154 time 7.7
   46        -seed 205 nobs 1 success True steps 107 time 4.2
   47        -seed 206 nobs 1 success True steps 114 time 5.7
   48        -seed 207 nobs 0 success True steps 48 time 1.7
   49        -seed 208 nobs 2 success True steps 112 time 4.7
   50        -seed 209 nobs 2 success True steps 94 time 5.1
   51        -success 50 / 50
diff --git a/test_approach.py b/test_approach.py
index 1457b4b..13e4f63 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -1,7 +1,8 @@
    1      1  import sys, time
    2      2  import numpy as np
    3      3  from env_client import make_env
    4        -from approach import GeneratedApproach
           4 +import os, importlib
           5 +GeneratedApproach = importlib.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
    5      6  def run(seed, verbose=False, count=None):
    6      7      env = make_env()
    7      8      obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
diff --git a/timing.py b/timing.py
new file mode 100644
index 0000000..db2cdeb
--- /dev/null
+++ b/timing.py
@@ -0,0 +1,13 @@
           1 +import time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env=make_env(); obs,info=env.reset(seed=1)
           5 +ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info); ap.state=obs
           6 +robot,block,surf,obst=ap._objs()
           7 +obstacles=ap._others_bboxes([])+[ap._others_bboxes([])[0]]
           8 +t=time.time()
           9 +for _ in range(20): r=ap._dp_path(0.389,0.826,1.09,0.38,obstacles,None)
          10 +print("dp ms", (time.time()-t)/20*1000, r[0])
          11 +t=time.time()
          12 +for _ in range(5): ap._find_spot(obst[0])
          13 +print("find_spot ms", (time.time()-t)/5*1000)
```

</details>

<a id="C008"></a>
### C008 · Spot cost uses next blocker as next target; nearest-first blocker order

Commit `c162fd43402cff3274796523d571b942555bc8b1`; parents: 82c16cf5103b0e60740ba496cea01c863e188e11. Recorded author date: 2026-09-30T11:10:51+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0381](01_timeline.md#E0381): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_c162fd4_approach.py) · [Exact all-file diff](evidence/diffs/C008_c162fd4.diff)

[Previous saved controller snapshot](evidence/versions/C007_82c16cf_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/a_near3.txt b/a_near3.txt
new file mode 100644
index 0000000..fdf1ac1
--- /dev/null
+++ b/a_near3.txt
@@ -0,0 +1,2 @@
           1 +300:52 301:37 302:73 303:72 304:76 305:29 306:46 307:55 308:43 309:77 310:51 311:77 312:61 313:39 314:65 315:24 316:52 317:50 318:52 319:62
           2 +succ 20 / 20 mean steps 54.65 max time 20.048581838607788
diff --git a/a_near4.txt b/a_near4.txt
new file mode 100644
index 0000000..e69de29
diff --git a/a_tall3.txt b/a_tall3.txt
new file mode 100644
index 0000000..325baf5
--- /dev/null
+++ b/a_tall3.txt
@@ -0,0 +1,2 @@
           1 +300:60 301:37 302:73 303:72 304:76 305:29 306:46 307:55 308:43 309:79 310:51 311:77 312:61 313:39 314:65 315:24 316:52 317:50 318:52 319:62
           2 +succ 20 / 20 mean steps 55.15 max time 19.499479293823242
diff --git a/a_tall4.txt b/a_tall4.txt
new file mode 100644
index 0000000..0135a2b
--- /dev/null
+++ b/a_tall4.txt
@@ -0,0 +1,2 @@
           1 +400:42 401:53 402:60 403:115 404:41 405:79 406:51 407:53 408:68 409:68 410:54 411:127 412:53 413:44 414:52 415:54 416:70 417:66 418:48 419:41
           2 +succ 20 / 20 mean steps 61.95 max time 32.59266257286072
diff --git a/approach.py b/approach.py
index 5ab4177..49a65bc 100644
--- a/approach.py
+++ b/approach.py
@@ -43,6 +43,7 @@ class GeneratedApproach:
   43     43  
   44     44      # ------------------------------------------------------------------
   45     45      K_RERANK = 20
          46 +    ORDER = 'near'
   46     47  
   47     48      def reset(self, state, info):
   48     49          self.state = state
@@ -569,7 +570,13 @@ class GeneratedApproach:
  569    570              obs1 = others + [surf_bb]
  570    571              c1 = self._path_cost((x, y), (rx, ry), obs1, crel_o)
  571    572              obs2 = [bx for bx in others] + [cand, surf_bb]
  572        -            c2 = self._path_cost((rx, ry + 0.01), (brx, bry), obs2, None)
         573 +            if cols:
         574 +                nx, ny = min(((cx2, cy2) for cx2, cy2, _ in cols),
         575 +                             key=lambda p: max(abs(p[0] - rx), abs(p[1] - ry)))
         576 +                c2 = self._path_cost((rx, ry + 0.01), (nx, ny), obs2, None)
         577 +                c2 += max(abs(nx - brx), abs(ny - bry)) / 0.05 * 0.5
         578 +            else:
         579 +                c2 = self._path_cost((rx, ry + 0.01), (brx, bry), obs2, None)
  573    580              obs3 = [bx for bx in others if bx != bb] + [cand, surf_bb]
  574    581              c3 = self._path_cost((brx, bry), (frx, fry), obs3, crel_b)
  575    582              tot = c1 + c2 + c3
@@ -586,7 +593,13 @@ class GeneratedApproach:
  586    593                  break
  587    594              robot, block, surf, obst = self._objs()
  588    595              x, y, _, _ = self._rpos()
  589        -            blockers.sort(key=lambda o: (-_rect_bbox(self.state, o)[3]))
         596 +            if self.ORDER == "tall":
         597 +                blockers.sort(key=lambda o: (-_rect_bbox(self.state, o)[3]))
         598 +            else:
         599 +                def _d(o):
         600 +                    b = _rect_bbox(self.state, o)
         601 +                    return max(abs((b[0] + b[2]) / 2 - x), abs(b[3] + TIP - y))
         602 +                blockers.sort(key=_d)
  590    603              picked = False
  591    604              for o in blockers:
  592    605                  others = self._others_bboxes([o])
diff --git a/approach_tall.py b/approach_tall.py
new file mode 100644
index 0000000..ace0ee9
--- /dev/null
+++ b/approach_tall.py
@@ -0,0 +1,3 @@
           1 +from approach import GeneratedApproach as _G
           2 +class GeneratedApproach(_G):
           3 +    ORDER = 'tall'
diff --git a/events.py b/events.py
new file mode 100644
index 0000000..92a67c1
--- /dev/null
+++ b/events.py
@@ -0,0 +1,21 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed=int(sys.argv[1]); C=int(sys.argv[2]) if len(sys.argv)>2 else None
           6 +env = make_env(); obs, info = env.reset(seed=seed, options={'object_count':C} if C else None)
           7 +for n in sorted(obs.get_object_names()):
           8 +    o=obs.get_object_from_name(n)
           9 +    print(n, {f: round(float(obs.get(o,f)),3) for f in (["x","y","width","height"] if n!='robot' else ['x','y'])})
          10 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
          11 +pv=0
          12 +R=obs.get_object_from_name('robot')
          13 +for t in range(1000):
          14 +    a = ap.get_action(obs)
          15 +    prev=obs
          16 +    obs, r, term, trunc, info = env.step(a)
          17 +    if a[4]!=pv or term:
          18 +        moved=[n for n in obs.get_object_names() if n!='robot' and abs(obs.get(obs.get_object_from_name(n),'y')-prev.get(prev.get_object_from_name(n),'y'))+abs(obs.get(obs.get_object_from_name(n),'x')-prev.get(prev.get_object_from_name(n),'x'))>1e-6]
          19 +        print(t, "vac" , a[4], "R=(%.3f,%.3f)"%(obs.get(R,'x'),obs.get(R,'y')), moved, [(n, round(obs.get(obs.get_object_from_name(n),'x'),3), round(obs.get(obs.get_object_from_name(n),'y'),3)) for n in moved])
          20 +        pv=a[4]
          21 +    if term: print("TERM", t+1); break
diff --git a/q_3.txt b/q_3.txt
new file mode 100644
index 0000000..e25f649
--- /dev/null
+++ b/q_3.txt
@@ -0,0 +1,2 @@
           1 +300:60 301:37 302:73 303:109 304:76 305:29 306:46 307:55 308:43 309:96 310:51 311:89 312:61 313:39 314:65 315:24 316:52 317:50 318:52 319:62 320:35 321:31 322:67 323:78 324:77 325:70 326:59 327:65 328:81 329:111 330:75 331:67 332:54 333:22 334:55 335:90 336:57 337:64 338:91 339:87
           2 +succ 40 / 40 mean steps 62.625 max time 20.109220504760742
diff --git a/q_4.txt b/q_4.txt
new file mode 100644
index 0000000..047aca3
--- /dev/null
+++ b/q_4.txt
@@ -0,0 +1,2 @@
           1 +400:42 401:53 402:82 403:122 404:41 405:89 406:51 407:59 408:68 409:68 410:54 411:133 412:53 413:44 414:52 415:64 416:74 417:66 418:48 419:41 420:51 421:108 422:93 423:36 424:66 425:52 426:66 427:73 428:52 429:70 430:73 431:81 432:39 433:94 434:77 435:32 436:72 437:80 438:91 439:77
           2 +succ 40 / 40 mean steps 67.175 max time 26.45576572418213
diff --git a/q_d.txt b/q_d.txt
new file mode 100644
index 0000000..d235992
--- /dev/null
+++ b/q_d.txt
@@ -0,0 +1,2 @@
           1 +100:64 101:13 102:49 103:25 104:61 105:17 106:42 107:26 108:20 109:35 110:53 111:34 112:23 113:37 114:17 115:53 116:46 117:23 118:41 119:44 120:16 121:22 122:56 123:36 124:35 125:59 126:12 127:53 128:68 129:50 130:44 131:31 132:69 133:47 134:12 135:13 136:33 137:61 138:72 139:66 140:14 141:38 142:49 143:40 144:35 145:26 146:37 147:19 148:12 149:23 150:26 151:28 152:24 153:55 154:33 155:22 156:45 157:32 158:61 159:37 160:19 161:32 162:39 163:30 164:34 165:53 166:35 167:82 168:40 169:66 170:33 171:49 172:30 173:50 174:44 175:33 176:30 177:38 178:62 179:39 180:32 181:44 182:94 183:48 184:45 185:22 186:20 187:38 188:16 189:31 190:16 191:26 192:39 193:44 194:51 195:23 196:35 197:73 198:47 199:35
           2 +succ 100 / 100 mean steps 38.51 max time 13.728600978851318
diff --git a/timing2.py b/timing2.py
new file mode 100644
index 0000000..19b9c3d
--- /dev/null
+++ b/timing2.py
@@ -0,0 +1,13 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +for seed,cnt in [(411,4),(403,4),(329,3),(182,None)]:
           5 +    env=make_env(); obs,info=env.reset(seed=seed, options={'object_count':cnt} if cnt else None)
           6 +    ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
           7 +    tc=0; mx=0
           8 +    for t in range(1000):
           9 +        t0=time.time(); a=ap.get_action(obs); dt=time.time()-t0; tc+=dt; mx=max(mx,dt)
          10 +        obs,r,term,tr,_=env.step(a)
          11 +        if term: break
          12 +    print(seed, cnt, "steps", t+1, "compute %.2fs maxstep %.3fs"%(tc,mx))
          13 +    env.close()
```

</details>

<a id="C009"></a>
### C009 · Allow higher floating parking

Commit `091283e27d47e0229a81d52c2973b84898784cf0`; parents: c162fd43402cff3274796523d571b942555bc8b1. Recorded author date: 2026-09-30T11:15:57+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0407](01_timeline.md#E0407): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_091283e_approach.py) · [Exact all-file diff](evidence/diffs/C009_091283e.diff)

[Previous saved controller snapshot](evidence/versions/C008_c162fd4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 49a65bc..883d2a9 100644
--- a/approach.py
+++ b/approach.py
@@ -44,6 +44,7 @@ class GeneratedApproach:
   44     44      # ------------------------------------------------------------------
   45     45      K_RERANK = 20
   46     46      ORDER = 'near'
          47 +    TOP_MAX = 0.46
   47     48  
   48     49      def reset(self, state, info):
   49     50          self.state = state
@@ -515,7 +516,7 @@ class GeneratedApproach:
  515    516          bb = _rect_bbox(s, block)
  516    517          brx = bb[0] + g
  517    518          bry = bb[3] + TIP + 0.003
  518        -        levels = [(v, 0.0) for v in np.arange(FLOOR + 0.005, 0.36 - h, 0.02)]
         519 +        levels = [(v, 0.0) for v in np.arange(FLOOR + 0.005, self.TOP_MAX - h, 0.02)]
  519    520          # remaining blockers' pickup columns must stay free
  520    521          cols = []
  521    522          for ob2 in self._blocking():
diff --git a/approach_t36.py b/approach_t36.py
new file mode 100644
index 0000000..f6228b7
--- /dev/null
+++ b/approach_t36.py
@@ -0,0 +1,3 @@
           1 +from approach import GeneratedApproach as _G
           2 +class GeneratedApproach(_G):
           3 +    TOP_MAX = 0.36
diff --git a/quick.py b/quick.py
index 0ce7f88..674d4d1 100644
--- a/quick.py
+++ b/quick.py
@@ -3,7 +3,7 @@ import test_approach as t
    3      3  from concurrent.futures import ThreadPoolExecutor
    4      4  seeds=[int(a) for a in sys.argv[1].split(',')] if ',' in sys.argv[1] else list(range(int(sys.argv[1]), int(sys.argv[2])))
    5      5  cnt=int(sys.argv[3]) if len(sys.argv)>3 and sys.argv[3]!='-' else None
    6        -with ThreadPoolExecutor(4) as ex:
           6 +with ThreadPoolExecutor(int(__import__("os").environ.get("NT","2"))) as ex:
    7      7      res=list(ex.map(lambda s: (s,)+tuple(t.run(s,count=cnt)), seeds))
    8      8  print(" ".join(f"{r[0]}:{r[2]}" for r in res))
    9      9  for r in res:
diff --git a/t36.txt b/t36.txt
new file mode 100644
index 0000000..7dbc98e
--- /dev/null
+++ b/t36.txt
@@ -0,0 +1,2 @@
           1 +0:52 1:44 2:50 3:40 4:49 5:67 6:37 7:83 8:54 9:70 10:45 11:40 12:69 13:45 14:22 15:21 16:18 17:46 18:40 19:38 20:49 21:47 22:64 23:37 24:46 25:37 26:35 27:14 28:40 29:24 30:21 31:44 32:53 33:51 34:27 35:26 36:30 37:27 38:17 39:46 40:49 41:27 42:27 43:23 44:42 45:59 46:34 47:34 48:18 49:16 50:53 51:29 52:47 53:49 54:26 55:22 56:48 57:11 58:38 59:49 60:21 61:46 62:49 63:25 64:24 65:16 66:41 67:32 68:29 69:32 70:30 71:21 72:82 73:38 74:20 75:57 76:26 77:16 78:50 79:30 80:51 81:21 82:34 83:64 84:51 85:41 86:24 87:34 88:45 89:40 90:55 91:28 92:35 93:48 94:19 95:43 96:27 97:31 98:45 99:37
           2 +succ 100 / 100 mean steps 38.24 max time 4.384720087051392
diff --git a/t46.txt b/t46.txt
new file mode 100644
index 0000000..0fce2ce
--- /dev/null
+++ b/t46.txt
@@ -0,0 +1,2 @@
           1 +0:52 1:44 2:50 3:40 4:49 5:67 6:37 7:83 8:54 9:70 10:43 11:40 12:69 13:45 14:22 15:21 16:18 17:46 18:40 19:38 20:49 21:47 22:64 23:37 24:46 25:37 26:35 27:14 28:40 29:24 30:21 31:44 32:53 33:51 34:27 35:26 36:30 37:27 38:17 39:46 40:49 41:27 42:27 43:23 44:42 45:59 46:34 47:34 48:18 49:16 50:53 51:29 52:47 53:49 54:26 55:22 56:48 57:11 58:38 59:49 60:21 61:46 62:49 63:25 64:24 65:16 66:41 67:32 68:29 69:32 70:30 71:21 72:82 73:38 74:20 75:57 76:26 77:16 78:50 79:30 80:51 81:21 82:34 83:58 84:51 85:41 86:20 87:34 88:45 89:40 90:55 91:28 92:35 93:48 94:19 95:43 96:27 97:31 98:45 99:37
           2 +succ 100 / 100 mean steps 38.12 max time 6.809597730636597
```

</details>

<a id="C010"></a>
### C010 · Arm-aware 3D DP path planner (uses arm extension for free vertical motion)

Commit `421d9a586411b4d5ca9cc889e07e2f5d60724059`; parents: 091283e27d47e0229a81d52c2973b84898784cf0. Recorded author date: 2026-09-30T11:20:30+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0466](01_timeline.md#E0466): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_421d9a5_approach.py) · [Exact all-file diff](evidence/diffs/C010_421d9a5.diff)

[Previous saved controller snapshot](evidence/versions/C009_091283e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 883d2a9..c3c6fee 100644
--- a/approach.py
+++ b/approach.py
@@ -45,6 +45,7 @@ class GeneratedApproach:
   45     45      K_RERANK = 20
   46     46      ORDER = 'near'
   47     47      TOP_MAX = 0.46
          48 +    USE_ARM_DP = True
   48     49  
   49     50      def reset(self, state, info):
   50     51          self.state = state
@@ -91,7 +92,7 @@ class GeneratedApproach:
   91     92      def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0):
   92     93          return np.array([dx, dy, dth, darm, self.vac], dtype=np.float32)
   93     94  
   94        -    def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200):
          95 +    def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200, tarm=ARM, final_vac=None):
   95     96          """Straight-line move towards (tx, ty). Returns True on success."""
   96     97          stuck = 0
   97     98          last = None
@@ -101,7 +102,7 @@ class GeneratedApproach:
  101    102              gy = y if ty is None else ty
  102    103              ex, ey = gx - x, gy - y
  103    104              eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
  104        -            ea = ARM - aj
         105 +            ea = tarm - aj
  105    106              if abs(ex) <= tol and abs(ey) <= tol:
  106    107                  if abs(eth) < 1e-4 and abs(ea) < 1e-4:
  107    108                      return True
@@ -113,9 +114,11 @@ class GeneratedApproach:
  113    114              else:
  114    115                  stuck = 0
  115    116              last = (x, y, aj, th)
  116        -            n = max(1, int(math.ceil(max(abs(ex), abs(ey)) / 0.05 - 1e-6)))
         117 +            n = max(1, int(math.ceil(max(abs(ex) / 0.05, abs(ey) / 0.05, abs(ea) / 0.1) - 1e-6)))
         118 +            if final_vac is not None and n == 1:
         119 +                self.vac = final_vac
  117    120              yield np.array([ex / n, ey / n, np.clip(eth, -0.19, 0.19),
  118        -                            np.clip(ea, -0.1, 0.1), self.vac], dtype=np.float32)
         121 +                            ea / n, self.vac], dtype=np.float32)
  119    122          return False
  120    123  
  121    124      def _collides(self, x, y, obstacles, crel, m=0.008):
@@ -310,32 +313,178 @@ class GeneratedApproach:
  310    313              c += math.ceil(max(abs(pts[i + 1][0] - pts[i][0]), abs(pts[i + 1][1] - pts[i][1])) / 0.05 - 1e-6)
  311    314          return c
  312    315  
         316 +    ARMS = (0.1, 0.2)
         317 +
         318 +    def _free_pts3(self, X, Y, obstacles, ctip, arm, m=0.008):
         319 +        """Free check for robot base at (X, Y) with arm length `arm`.
         320 +        ctip: carried bbox relative to the gripper tip point (x, y - arm - GW)."""
         321 +        tipl = arm + GW
         322 +        free = (X >= RX_MIN - 1e-6) & (X <= RX_MAX + 1e-6) & (Y <= ROBOT_Y_MAX + 1e-6)
         323 +        free &= (Y - tipl) >= FLOOR - 0.004
         324 +        if ctip is not None:
         325 +            free &= (Y - tipl + ctip[1]) >= FLOOR - 1e-3
         326 +        for b in obstacles:
         327 +            ddx = np.maximum(np.maximum(b[0] - X, 0.0), X - b[2])
         328 +            ddy = np.maximum(np.maximum(b[1] - Y, 0.0), Y - b[3])
         329 +            free &= (ddx * ddx + ddy * ddy) >= (BASE_R + m) ** 2
         330 +            e = 0.001
         331 +            ov = (X - GH / 2 < b[2] + e) & (b[0] < X + GH / 2 + e) & (Y - tipl < b[3] + e) & (b[1] < Y + e)
         332 +            free &= ~ov
         333 +            if ctip is not None:
         334 +                e = m * 0.6
         335 +                ov = (X + ctip[0] < b[2] + e) & (b[0] < X + ctip[2] + e) & \
         336 +                     (Y - tipl + ctip[1] < b[3] + e) & (b[1] < Y - tipl + ctip[3] + e)
         337 +                free &= ~ov
         338 +        return free
         339 +
         340 +    def _dp_path3(self, x0, y0, arm0, x1, tipy1, obstacles, ctip):
         341 +        """DP over (column, y-level, arm in ARMS). Goal is a tip position.
         342 +        Returns list of waypoints (x, y, arm) or None."""
         343 +        res = 0.005
         344 +        ylo = 0.2
         345 +        nl = int(round((ROBOT_Y_MAX - ylo) / res)) + 1
         346 +        levels = ylo + res * np.arange(nl)
         347 +        K = int(round(0.05 / res))
         348 +        A = self.ARMS
         349 +        NA = len(A)
         350 +        a0 = int(np.argmin([abs(arm0 - v) for v in A]))
         351 +        j0 = int(min(nl - 1, max(0, math.ceil((y0 - ylo) / res - 1e-6))))
         352 +        jg = [int(min(nl - 1, max(0, math.ceil((tipy1 + A[a] + GW - ylo) / res - 1e-6)))) for a in range(NA)]
         353 +        dx = x1 - x0
         354 +        N = int(math.ceil(abs(dx) / 0.05 - 1e-6))
         355 +        cols = x0 + dx * (np.arange(2 * N + 1) / max(1, 2 * N)) if N > 0 else np.array([x0])
         356 +        XX = np.repeat(cols[:, None], nl, axis=1)
         357 +        YY = np.repeat(levels[None, :], len(cols), axis=0)
         358 +        F = [self._free_pts3(XX, YY, obstacles, ctip, A[a]) for a in range(NA)]
         359 +        for a in range(NA):
         360 +            for ci_ in ({0, 2 * N}):
         361 +                F[a][ci_] |= self._free_pts3(XX[ci_], YY[ci_], obstacles, ctip, A[a], m=0.001)
         362 +        F[a0][0, j0] = True
         363 +        for a in range(NA):
         364 +            F[a][2 * N, jg[a]] = True
         365 +        INF = 1e9
         366 +        J = np.arange(nl)
         367 +        vc = np.ceil(np.abs(J[:, None] - J[None, :]) / K)
         368 +
         369 +        def vlayer(C, ci):
         370 +            newC = []; par = []
         371 +            for a in range(NA):
         372 +                free = F[a][2 * ci]
         373 +                seg = np.cumsum(~free)
         374 +                same = (seg[:, None] == seg[None, :]) & free[:, None] & free[None, :]
         375 +                M = np.where(same, C[a][None, :] + vc, INF)
         376 +                arg = np.argmin(M, axis=1)
         377 +                c = M[J, arg]
         378 +                keep = C[a] <= c
         379 +                c = np.where(keep, C[a], c)
         380 +                pj = np.where(keep | (c >= INF), -1, arg)
         381 +                newC.append(c); par.append((np.full(nl, a), pj))
         382 +            return newC, ("v", par)
         383 +
         384 +        def slayer(C, ci):
         385 +            both = np.ones(nl, dtype=bool)
         386 +            for a in range(NA):
         387 +                both &= F[a][2 * ci]
         388 +            bad = np.concatenate([[0], np.cumsum(~both)])
         389 +            newC = [c.copy() for c in C]
         390 +            par = [(np.full(nl, -1), np.full(nl, -1)) for _ in range(NA)]
         391 +            for a in range(NA):
         392 +                for asrc in range(NA):
         393 +                    if asrc == a:
         394 +                        continue
         395 +                    for d in range(-K, K + 1):
         396 +                        sj = np.arange(max(0, -d), min(nl, nl - d))
         397 +                        dj = sj + d
         398 +                        lo = np.minimum(sj, dj); hi = np.maximum(sj, dj)
         399 +                        ok = (bad[hi + 1] - bad[lo]) == 0
         400 +                        cand = C[asrc][sj] + 1.0
         401 +                        better = ok & (cand < newC[a][dj])
         402 +                        newC[a][dj[better]] = cand[better]
         403 +                        par[a][0][dj[better]] = asrc
         404 +                        par[a][1][dj[better]] = sj[better]
         405 +            return newC, ("s", par)
         406 +
         407 +        def hlayer(Cprev, i):
         408 +            fm = [F[a][2 * i - 1] for a in range(NA)]
         409 +            fe = [F[a][2 * i] for a in range(NA)]
         410 +            newC = [np.full(nl, INF) for _ in range(NA)]
         411 +            par = [(np.full(nl, -1), np.full(nl, -1)) for _ in range(NA)]
         412 +            for a in range(NA):
         413 +                for asrc in range(NA):
         414 +                    for d in range(-K, K + 1):
         415 +                        sj = np.arange(max(0, -d), min(nl, nl - d))
         416 +                        dj = sj + d
         417 +                        mid = sj + d / 2.0
         418 +                        mlo = np.floor(mid).astype(int); mhi = np.ceil(mid).astype(int)
         419 +                        ok = fe[a][dj] & fm[a][mlo] & fm[a][mhi] & fm[asrc][mlo] & fm[asrc][mhi]
         420 +                        cand = Cprev[asrc][sj] + 1.0
         421 +                        better = ok & (cand < newC[a][dj])
         422 +                        newC[a][dj[better]] = cand[better]
         423 +                        par[a][0][dj[better]] = asrc
         424 +                        par[a][1][dj[better]] = sj[better]
         425 +            return newC, ("h", par)
         426 +
         427 +        layers = []  # (column, kind, par)
         428 +        C = [np.full(nl, INF) for _ in range(NA)]
         429 +        C[a0][j0] = 0.0
         430 +        for ci in range(N + 1):
         431 +            if ci > 0:
         432 +                C, L = hlayer(C, ci); layers.append((ci,) + L)
         433 +            for _ in range(2):
         434 +                C, L = vlayer(C, ci); layers.append((ci,) + L)
         435 +                C, L = slayer(C, ci); layers.append((ci,) + L)
         436 +        best_a = int(np.argmin([C[a][jg[a]] for a in range(NA)]))
         437 +        if C[best_a][jg[best_a]] >= INF:
         438 +            return None
         439 +        # backtrack
         440 +        pts = []
         441 +        a, j = best_a, jg[best_a]
         442 +        for ci, kind, par in reversed(layers):
         443 +            pa, pj = par[a][0][j], par[a][1][j]
         444 +            if pj < 0:
         445 +                continue
         446 +            x = float(cols[2 * ci])
         447 +            if kind == "v":
         448 +                steps = int(math.ceil(abs(j - pj) / K))
         449 +                for s_ in range(steps, 0, -1):
         450 +                    jj = pj + int(round((j - pj) * s_ / steps))
         451 +                    pts.append((x, float(levels[jj]), A[a]))
         452 +            else:
         453 +                pts.append((x, float(levels[j]), A[a]))
         454 +            a, j = int(pa), int(pj)
         455 +        pts.reverse()
         456 +        if pts:
         457 +            ex, ey, ea = pts[-1]
         458 +            pts[-1] = (x1, tipy1 + ea + GW, ea)
         459 +        else:
         460 +            pts = [(x1, tipy1 + A[best_a] + GW, A[best_a])]
         461 +        return pts
         462 +
  313    463      def _move(self, x1, y1, carried=None, last_vac=None):
  314        -        """Plan & execute a collision-free path. carried: grasped object or None."""
  315        -        x0, y0, _, _ = self._rpos()
         464 +        """Plan & execute a collision-free path. (x1, y1) is the robot target assuming
         465 +        arm length ARM; the planner may use other arm lengths (same tip target)."""
         466 +        x0, y0, _, aj = self._rpos()
  316    467          excl = [carried] if carried is not None else []
  317    468          obstacles = self._others_bboxes(excl)
  318    469          robot, block, surf, obst = self._objs()
  319    470          obstacles.append(_rect_bbox(self.state, surf))
  320    471          crel = None
         472 +        ctip = None
  321    473          if carried is not None:
  322    474              cb = _rect_bbox(self.state, carried)
  323    475              crel = (cb[0] - x0, cb[1] - y0, cb[2] - x0, cb[3] - y0)
  324        -        path = self._plan_path(x1, y1, obstacles, crel)
  325        -        for i, (px, py) in enumerate(path):
  326        -            if last_vac is not None and i == len(path) - 1:
  327        -                # final segment: run all but last step, then set vacuum on last step
  328        -                gen = self._goto(px, py)
  329        -                while True:
  330        -                    x, y, _, _ = self._rpos()
  331        -                    if max(abs(px - x), abs(py - y)) <= 0.05 + 1e-6:
  332        -                        break
  333        -                    try:
  334        -                        yield next(gen)
  335        -                    except StopIteration:
  336        -                        break
  337        -                self.vac = last_vac
  338        -            ok = yield from self._goto(px, py)
         476 +            ty0 = y0 - aj - GW
         477 +            ctip = (cb[0] - x0, cb[1] - ty0, cb[2] - x0, cb[3] - ty0)
         478 +        path = None
         479 +        if self.USE_ARM_DP:
         480 +            path = self._dp_path3(x0, y0, aj, x1, y1 - TIP, obstacles, ctip)
         481 +        if path is None:
         482 +            if abs(aj - ARM) > 1e-4:
         483 +                crel = None if ctip is None else (ctip[0], ctip[1] - TIP, ctip[2], ctip[3] - TIP)
         484 +            path = [(px, py, ARM) for (px, py) in self._plan_path(x1, y1, obstacles, crel)]
         485 +        for i, (px, py, pa) in enumerate(path):
         486 +            fv = last_vac if i == len(path) - 1 else None
         487 +            ok = yield from self._goto(px, py, tarm=pa, final_vac=fv)
  339    488              if not ok:
  340    489                  return False
  341    490          return True
@@ -414,7 +563,7 @@ class GeneratedApproach:
  414    563          x, y, _, _ = self._rpos()
  415    564          b0 = _rect_bbox(self.state, o)
  416    565          rx = x + (target_left - b0[0])
  417        -        ry = y - (b0[1] - target_bottom)
         566 +        ry = y - (b0[1] - target_bottom) + (ARM - self._rpos()[3])
  418    567          gen = self._move(rx, ry, o, last_vac=(0.0 if release else None))
  419    568          first = True
  420    569          while True:
diff --git a/approach_head.py b/approach_head.py
new file mode 100644
index 0000000..883d2a9
--- /dev/null
+++ b/approach_head.py
@@ -0,0 +1,648 @@
           1 +import math
           2 +import numpy as np
           3 +
           4 +WORLD_X = (0.0, 1.618)
           5 +ROBOT_Y_MAX = 0.895
           6 +FLOOR = 0.1
           7 +ARM = 0.2          # extended arm length we use
           8 +GW = 0.01          # gripper width (along arm)
           9 +GH = 0.07          # gripper height (perpendicular)
          10 +BASE_R = 0.1
          11 +RX_MIN = 0.1 + 0.002
          12 +RX_MAX = 1.618 - 0.1 - 0.002
          13 +TIP = ARM + GW     # distance from robot center to gripper tip (pointing down)
          14 +
          15 +
          16 +def _rect_bbox(state, o):
          17 +    x = float(state.get(o, "x")); y = float(state.get(o, "y"))
          18 +    w = float(state.get(o, "width")); h = float(state.get(o, "height"))
          19 +    th = float(state.get(o, "theta"))
          20 +    if abs(th) < 1e-6:
          21 +        return (x, y, x + w, y + h)
          22 +    c, s = math.cos(th), math.sin(th)
          23 +    pts = [(x, y), (x + w * c, y + w * s), (x - h * s, y + h * c),
          24 +           (x + w * c - h * s, y + w * s + h * c)]
          25 +    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
          26 +    return (min(xs), min(ys), max(xs), max(ys))
          27 +
          28 +
          29 +def _circle_rect_dist(cx, cy, b):
          30 +    dx = max(b[0] - cx, 0.0, cx - b[2])
          31 +    dy = max(b[1] - cy, 0.0, cy - b[3])
          32 +    return math.hypot(dx, dy)
          33 +
          34 +
          35 +def _overlap(a, b, m=0.0):
          36 +    return a[0] < b[2] + m and b[0] < a[2] + m and a[1] < b[3] + m and b[1] < a[3] + m
          37 +
          38 +
          39 +class GeneratedApproach:
          40 +    def __init__(self, action_space, observation_space, primitives):
          41 +        self.low = np.array(action_space.low, dtype=np.float32)
          42 +        self.high = np.array(action_space.high, dtype=np.float32)
          43 +
          44 +    # ------------------------------------------------------------------
          45 +    K_RERANK = 20
          46 +    ORDER = 'near'
          47 +    TOP_MAX = 0.46
          48 +
          49 +    def reset(self, state, info):
          50 +        self.state = state
          51 +        self.gen = self._plan()
          52 +        self.vac = 0.0
          53 +
          54 +    def get_action(self, state):
          55 +        self.state = state
          56 +        try:
          57 +            a = next(self.gen)
          58 +        except StopIteration:
          59 +            self.gen = self._plan()
          60 +            try:
          61 +                a = next(self.gen)
          62 +            except StopIteration:
          63 +                a = np.zeros(5, dtype=np.float32)
          64 +        a = np.clip(np.asarray(a, dtype=np.float32), self.low, self.high)
          65 +        return a
          66 +
          67 +    # ------------------------------------------------------------------
          68 +    def _objs(self):
          69 +        s = self.state
          70 +        robot = None; block = None; surf = None; obst = []
          71 +        for n in sorted(s.get_object_names()):
          72 +            o = s.get_object_from_name(n)
          73 +            tn = o.type.name
          74 +            if tn == "crv_robot":
          75 +                robot = o
          76 +            elif tn == "target_block":
          77 +                block = o
          78 +            elif tn == "target_surface":
          79 +                surf = o
          80 +            else:
          81 +                obst.append(o)
          82 +        return robot, block, surf, obst
          83 +
          84 +    def _rpos(self):
          85 +        r = self._objs()[0]
          86 +        s = self.state
          87 +        return (float(s.get(r, "x")), float(s.get(r, "y")),
          88 +                float(s.get(r, "theta")), float(s.get(r, "arm_joint")))
          89 +
          90 +    # ------------------------------------------------------------------
          91 +    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0):
          92 +        return np.array([dx, dy, dth, darm, self.vac], dtype=np.float32)
          93 +
          94 +    def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200):
          95 +        """Straight-line move towards (tx, ty). Returns True on success."""
          96 +        stuck = 0
          97 +        last = None
          98 +        for _ in range(max_steps):
          99 +            x, y, th, aj = self._rpos()
         100 +            gx = x if tx is None else tx
         101 +            gy = y if ty is None else ty
         102 +            ex, ey = gx - x, gy - y
         103 +            eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
         104 +            ea = ARM - aj
         105 +            if abs(ex) <= tol and abs(ey) <= tol:
         106 +                if abs(eth) < 1e-4 and abs(ea) < 1e-4:
         107 +                    return True
         108 +            if last is not None and abs(last[0] - x) < 1e-7 and abs(last[1] - y) < 1e-7 \
         109 +                    and abs(last[2] - aj) < 1e-7 and abs(last[3] - th) < 1e-7:
         110 +                stuck += 1
         111 +                if stuck >= 2:
         112 +                    return False
         113 +            else:
         114 +                stuck = 0
         115 +            last = (x, y, aj, th)
         116 +            n = max(1, int(math.ceil(max(abs(ex), abs(ey)) / 0.05 - 1e-6)))
         117 +            yield np.array([ex / n, ey / n, np.clip(eth, -0.19, 0.19),
         118 +                            np.clip(ea, -0.1, 0.1), self.vac], dtype=np.float32)
         119 +        return False
         120 +
         121 +    def _collides(self, x, y, obstacles, crel, m=0.008):
         122 +        if y > ROBOT_Y_MAX + 1e-6 or x < RX_MIN - 1e-6 or x > RX_MAX + 1e-6:
         123 +            return True
         124 +        col = (x - GH / 2, y - TIP, x + GH / 2, y)
         125 +        cb = None
         126 +        if crel is not None:
         127 +            cb = (x + crel[0], y + crel[1], x + crel[2], y + crel[3])
         128 +            if cb[1] < FLOOR - 1e-3:
         129 +                return True
         130 +        for b in obstacles:
         131 +            if _circle_rect_dist(x, y, b) < BASE_R + m:
         132 +                return True
         133 +            if _overlap(col, b, 0.001):
         134 +                return True
         135 +            if cb is not None and _overlap(cb, b, m * 0.6):
         136 +                return True
         137 +        return False
         138 +
         139 +    def _seg_free(self, p, q, obstacles, crel):
         140 +        d = max(abs(q[0] - p[0]), abs(q[1] - p[1]))
         141 +        n = max(1, int(math.ceil(d / 0.008)))
         142 +        for i in range(1, n + 1):
         143 +            t = i / n
         144 +            if self._collides(p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]), obstacles, crel):
         145 +                return False
         146 +        return True
         147 +
         148 +    def _free_pts(self, X, Y, obstacles, crel, m=0.008):
         149 +        X = np.asarray(X, dtype=float); Y = np.asarray(Y, dtype=float)
         150 +        free = (X >= RX_MIN - 1e-6) & (X <= RX_MAX + 1e-6) & (Y <= ROBOT_Y_MAX + 1e-6)
         151 +        if crel is not None:
         152 +            free &= (Y + crel[1]) >= FLOOR - 1e-3
         153 +        for b in obstacles:
         154 +            ddx = np.maximum(np.maximum(b[0] - X, 0.0), X - b[2])
         155 +            ddy = np.maximum(np.maximum(b[1] - Y, 0.0), Y - b[3])
         156 +            free &= (ddx * ddx + ddy * ddy) >= (BASE_R + m) ** 2
         157 +            e = 0.001
         158 +            ov = (X - GH / 2 < b[2] + e) & (b[0] < X + GH / 2 + e) & (Y - TIP < b[3] + e) & (b[1] < Y + e)
         159 +            free &= ~ov
         160 +            if crel is not None:
         161 +                e = m * 0.6
         162 +                ov = (X + crel[0] < b[2] + e) & (b[0] < X + crel[2] + e) & \
         163 +                     (Y + crel[1] < b[3] + e) & (b[1] < Y + crel[3] + e)
         164 +                free &= ~ov
         165 +        return free
         166 +
         167 +    def _dp_path(self, x0, y0, x1, y1, obstacles, crel):
         168 +        """DP over x-columns / y-levels. Returns (cost, waypoints) or None."""
         169 +        res = 0.005
         170 +        ylo = 0.3
         171 +        nl = int(round((ROBOT_Y_MAX - ylo) / res)) + 1
         172 +        levels = ylo + res * np.arange(nl)
         173 +        K = int(round(0.05 / res))
         174 +        j0 = int(min(nl - 1, max(0, math.ceil((y0 - ylo) / res - 1e-6))))
         175 +        j1 = int(min(nl - 1, max(0, math.ceil((y1 - ylo) / res - 1e-6))))
         176 +        dx = x1 - x0
         177 +        N = int(math.ceil(abs(dx) / 0.05 - 1e-6))
         178 +        # columns at half steps
         179 +        cols = x0 + dx * (np.arange(2 * N + 1) / max(1, 2 * N)) if N > 0 else np.array([x0])
         180 +        XX = np.repeat(cols[:, None], nl, axis=1)
         181 +        YY = np.repeat(levels[None, :], len(cols), axis=0)
         182 +        F = self._free_pts(XX, YY, obstacles, crel)
         183 +        INF = 1e9
         184 +        # vertical cost matrix within a column
         185 +        J = np.arange(nl)
         186 +        vc = np.ceil(np.abs(J[:, None] - J[None, :]) / K)
         187 +
         188 +        def vert_relax(cost, free):
         189 +            # segments of contiguous free cells
         190 +            seg = np.cumsum(~free)
         191 +            same = (seg[:, None] == seg[None, :]) & free[:, None] & free[None, :]
         192 +            M = np.where(same, cost[None, :] + vc, INF)
         193 +            arg = np.argmin(M, axis=1)
         194 +            return M[J, arg], arg
         195 +
         196 +        cost = np.full(nl, INF)
         197 +        if not F[0, j0]:
         198 +            # allow starting cell even if flagged (numerical contact)
         199 +            F[0, j0] = True
         200 +        cost[j0] = 0.0
         201 +        costs = []
         202 +        backs = []
         203 +        c, arg = vert_relax(cost, F[0])
         204 +        costs.append(c); backs.append(("v", arg))
         205 +        for i in range(1, N + 1):
         206 +            fm = F[2 * i - 1]; fe = F[2 * i]
         207 +            new = np.full(nl, INF)
         208 +            parent = np.full(nl, -1)
         209 +            prev = costs[-1]
         210 +            for d in range(-K, K + 1):
         211 +                # from j to j+d; midpoint level j + d/2
         212 +                src_j = np.arange(max(0, -d), min(nl, nl - d))
         213 +                dst_j = src_j + d
         214 +                mid = src_j + d / 2.0
         215 +                mlo = np.floor(mid).astype(int); mhi = np.ceil(mid).astype(int)
         216 +                ok = fe[dst_j] & fm[mlo] & fm[mhi] & (prev[src_j] < INF)
         217 +                cand = prev[src_j] + 1.0
         218 +                better = ok & (cand < new[dst_j])
         219 +                new[dst_j[better]] = cand[better]
         220 +                parent[dst_j[better]] = src_j[better]
         221 +            if i == N and not fe[j1]:
         222 +                fe = fe.copy(); fe[j1] = True
         223 +            c, arg = vert_relax(new, fe)
         224 +            costs.append(new); backs.append(("h", parent))
         225 +            costs[-1] = c; backs.append(("v", arg))
         226 +            # note: backs holds pairs per column after the first
         227 +        final = costs[-1]
         228 +        if final[j1] >= INF:
         229 +            return None
         230 +        # backtrack
         231 +        pts = []
         232 +        j = j1
         233 +        ci = N
         234 +        bi = len(backs) - 1
         235 +        while bi >= 0:
         236 +            kind, arr = backs[bi]
         237 +            if kind == "v":
         238 +                jp = int(arr[j])
         239 +                # vertical moves from jp to j at column ci
         240 +                if jp != j:
         241 +                    steps = int(math.ceil(abs(j - jp) / K))
         242 +                    for s_ in range(steps, 0, -1):
         243 +                        jj = jp + int(round((j - jp) * s_ / steps))
         244 +                        pts.append((float(cols[2 * ci]), float(levels[jj])))
         245 +                j = jp
         246 +            else:
         247 +                jp = int(arr[j])
         248 +                pts.append((float(cols[2 * ci]), float(levels[j])))
         249 +                j = jp
         250 +                ci -= 1
         251 +            bi -= 1
         252 +        pts.reverse()
         253 +        # dedupe and fix endpoints
         254 +        out = []
         255 +        for p in pts:
         256 +            if not out or abs(out[-1][0] - p[0]) > 1e-9 or abs(out[-1][1] - p[1]) > 1e-9:
         257 +                out.append(p)
         258 +        if out and abs(out[0][0] - x0) < 1e-9 and abs(out[0][1] - levels[j0]) < 1e-9:
         259 +            # first waypoint is the snapped start
         260 +            if abs(levels[j0] - y0) < 1e-9:
         261 +                out = out[1:]
         262 +        if out and abs(out[-1][0] - x1) < 1e-6 and abs(out[-1][1] - levels[j1]) <= res + 1e-9:
         263 +            out[-1] = (x1, y1)
         264 +        else:
         265 +            out.append((x1, y1))
         266 +        return float(final[j1]), out
         267 +
         268 +    def _plan_path(self, x1, y1, obstacles, crel, start=None):
         269 +        if start is None:
         270 +            x0, y0, _, _ = self._rpos()
         271 +        else:
         272 +            x0, y0 = start
         273 +        r = self._dp_path(x0, y0, x1, y1, obstacles, crel)
         274 +        if r is not None:
         275 +            return r[1]
         276 +        return self._plan_path_old(x1, y1, obstacles, crel, (x0, y0))
         277 +
         278 +    def _plan_path_old(self, x1, y1, obstacles, crel, start=None):
         279 +        if start is None:
         280 +            x0, y0, _, _ = self._rpos()
         281 +        else:
         282 +            x0, y0 = start
         283 +        p0 = (x0, y0)
         284 +        if self._seg_free(p0, (x1, y1), obstacles, crel):
         285 +            return [(x1, y1)]
         286 +        dx = x1 - x0
         287 +        sg = 1.0 if dx >= 0 else -1.0
         288 +        tys = sorted(set([round(v, 4) for v in np.arange(max(y0, y1) + 0.01, ROBOT_Y_MAX, 0.02)]
         289 +                         + [ROBOT_Y_MAX]))
         290 +        for ty in tys:
         291 +            a = min(abs(dx), ty - y0)
         292 +            b = min(abs(dx) - a, ty - y1)
         293 +            pa = (x0 + sg * a, ty)
         294 +            pb = (x1 - sg * b, ty)
         295 +            path = [pa, pb, (x1, y1)]
         296 +            pts = [p0] + path
         297 +            if all(self._seg_free(pts[i], pts[i + 1], obstacles, crel) for i in range(3)):
         298 +                return path
         299 +            path = [(x0, ty), (x1, ty), (x1, y1)]
         300 +            pts = [p0] + path
         301 +            if all(self._seg_free(pts[i], pts[i + 1], obstacles, crel) for i in range(3)):
         302 +                return path
         303 +        return [(x0, ROBOT_Y_MAX), (x1, ROBOT_Y_MAX), (x1, y1)]
         304 +
         305 +    def _path_cost(self, p0, p1, obstacles, crel):
         306 +        path = self._plan_path(p1[0], p1[1], obstacles, crel, start=p0)
         307 +        pts = [p0] + path
         308 +        c = 0.0
         309 +        for i in range(len(pts) - 1):
         310 +            c += math.ceil(max(abs(pts[i + 1][0] - pts[i][0]), abs(pts[i + 1][1] - pts[i][1])) / 0.05 - 1e-6)
         311 +        return c
         312 +
         313 +    def _move(self, x1, y1, carried=None, last_vac=None):
         314 +        """Plan & execute a collision-free path. carried: grasped object or None."""
         315 +        x0, y0, _, _ = self._rpos()
         316 +        excl = [carried] if carried is not None else []
         317 +        obstacles = self._others_bboxes(excl)
         318 +        robot, block, surf, obst = self._objs()
         319 +        obstacles.append(_rect_bbox(self.state, surf))
         320 +        crel = None
         321 +        if carried is not None:
         322 +            cb = _rect_bbox(self.state, carried)
         323 +            crel = (cb[0] - x0, cb[1] - y0, cb[2] - x0, cb[3] - y0)
         324 +        path = self._plan_path(x1, y1, obstacles, crel)
         325 +        for i, (px, py) in enumerate(path):
         326 +            if last_vac is not None and i == len(path) - 1:
         327 +                # final segment: run all but last step, then set vacuum on last step
         328 +                gen = self._goto(px, py)
         329 +                while True:
         330 +                    x, y, _, _ = self._rpos()
         331 +                    if max(abs(px - x), abs(py - y)) <= 0.05 + 1e-6:
         332 +                        break
         333 +                    try:
         334 +                        yield next(gen)
         335 +                    except StopIteration:
         336 +                        break
         337 +                self.vac = last_vac
         338 +            ok = yield from self._goto(px, py)
         339 +            if not ok:
         340 +                return False
         341 +        return True
         342 +
         343 +    # ------------------------------------------------------------------
         344 +    def _others_bboxes(self, exclude):
         345 +        robot, block, surf, obst = self._objs()
         346 +        out = []
         347 +        for o in [block] + obst:
         348 +            if o in exclude:
         349 +                continue
         350 +            out.append(_rect_bbox(self.state, o))
         351 +        return out
         352 +
         353 +    def _descent_free(self, rx, ry_final, carried_bbox_final, others, margin=0.01):
         354 +        """Check vertical descent from travel height to ry_final at x=rx is collision free."""
         355 +        # base circle sweep: check at the final (lowest) position -- sweep is vertical,
         356 +        # and anything below is covered by checking the column.
         357 +        for b in others:
         358 +            # circle swept vertically from ry_final upwards
         359 +            cy = min(max(ry_final, b[1]), ROBOT_Y_MAX)
         360 +            cy = max(cy, ry_final)
         361 +            if _circle_rect_dist(rx, cy, b) < BASE_R + margin:
         362 +                return False
         363 +            # arm + gripper column
         364 +            col = (rx - GH / 2, ry_final - TIP, rx + GH / 2, ROBOT_Y_MAX)
         365 +            if _overlap(col, b, margin * 0.3):
         366 +                return False
         367 +            if carried_bbox_final is not None:
         368 +                cb = carried_bbox_final
         369 +                colc = (cb[0], cb[1], cb[2], cb[3] + (ROBOT_Y_MAX - ry_final))
         370 +                if _overlap(colc, b, margin * 0.5):
         371 +                    return False
         372 +        return True
         373 +
         374 +    def _grasp_cands(self, b, pref=None):
         375 +        lo = b[0] + 0.012 - (GH / 2 - 0.02)
         376 +        hi = b[2] - 0.012 + (GH / 2 - 0.02)
         377 +        cx = (b[0] + b[2]) / 2 if pref is None else pref
         378 +        if hi < lo:
         379 +            lo = hi = (b[0] + b[2]) / 2
         380 +        full_lo = b[0] + GH / 2
         381 +        full_hi = b[2] - GH / 2
         382 +        vals = np.linspace(lo, hi, 41).tolist() + [min(max(cx, lo), hi)]
         383 +
         384 +        def key(v):
         385 +            # prefer full gripper contact, then closeness to preferred
         386 +            pen = 0.0
         387 +            if full_lo <= full_hi:
         388 +                pen = max(0.0, full_lo - v, v - full_hi)
         389 +            return (round(pen, 4) > 0.0, abs(v - cx))
         390 +        return sorted(vals, key=key)
         391 +
         392 +    def _choose_grasp_x(self, o, others, pref=None):
         393 +        b = _rect_bbox(self.state, o)
         394 +        ry = b[3] + TIP + 0.003
         395 +        for gx in self._grasp_cands(b, pref):
         396 +            if gx < RX_MIN or gx > RX_MAX:
         397 +                continue
         398 +            if self._descent_free(gx, ry, None, others):
         399 +                return gx
         400 +        return None
         401 +
         402 +    def _pick(self, o, pref=None):
         403 +        others = self._others_bboxes([o])
         404 +        gx = self._choose_grasp_x(o, others, pref)
         405 +        if gx is None:
         406 +            return False
         407 +        b = _rect_bbox(self.state, o)
         408 +        ry = b[3] + TIP + 0.003
         409 +        yield from self._move(gx, ry, None, last_vac=1.0)
         410 +        self.vac = 1.0
         411 +        return True
         412 +
         413 +    def _place_at(self, o, target_left, target_bottom, check=True, release=False):
         414 +        x, y, _, _ = self._rpos()
         415 +        b0 = _rect_bbox(self.state, o)
         416 +        rx = x + (target_left - b0[0])
         417 +        ry = y - (b0[1] - target_bottom)
         418 +        gen = self._move(rx, ry, o, last_vac=(0.0 if release else None))
         419 +        first = True
         420 +        while True:
         421 +            try:
         422 +                a = next(gen)
         423 +            except StopIteration as e:
         424 +                return True
         425 +            yield a
         426 +            if first and check:
         427 +                first = False
         428 +                nb = _rect_bbox(self.state, o)
         429 +                if abs(nb[0] - b0[0]) + abs(nb[1] - b0[1]) < 1e-6:
         430 +                    # grasp failed
         431 +                    self.vac = 0.0
         432 +                    yield self._act()
         433 +                    return False
         434 +
         435 +    # ------------------------------------------------------------------
         436 +    def _final_placement(self):
         437 +        """Returns (left, bottom, surface_bbox, grasp_offset_from_block_left)."""
         438 +        robot, block, surf, obst = self._objs()
         439 +        s = self.state
         440 +        sb = _rect_bbox(s, surf)
         441 +        bb = _rect_bbox(s, block)
         442 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         443 +        bottom = sb[3] + 0.014
         444 +        Llo = sb[0] + min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
         445 +        Lhi = sb[2] - bw - min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
         446 +        Lc = sb[0] + (sb[2] - sb[0] - bw) / 2
         447 +        if Lhi < Llo:
         448 +            Llo = Lhi = Lc
         449 +        obbs = [_rect_bbox(s, o) for o in obst]
         450 +        gs = []
         451 +        for g in self._grasp_cands((0.0, 0.0, bw, 1.0)):
         452 +            if all(abs(g - g2) > 0.004 for g2 in gs):
         453 +                gs.append(g)
         454 +            if len(gs) >= 7:
         455 +                break
         456 +        Ls = np.linspace(Llo, Lhi, 25).tolist() + [Lc]
         457 +        best = None
         458 +        for gi, g in enumerate(gs):
         459 +            for L in Ls:
         460 +                rx = L + g
         461 +                if not (RX_MIN <= rx <= RX_MAX):
         462 +                    continue
         463 +                fbb = (L, bottom, L + bw, bottom + bh)
         464 +                ry = bottom + bh + TIP + 0.003
         465 +                nb = 0
         466 +                for ob in obbs:
         467 +                    if not self._descent_free(rx, ry, fbb, [ob], margin=0.015):
         468 +                        nb += 1
         469 +                cost = nb * 100.0 + abs(L - bb[0]) / 0.05 + gi * 0.01 + abs(L - Lc) * 0.01
         470 +                if best is None or cost < best[0]:
         471 +                    best = (cost, L, g)
         472 +        if best is None:
         473 +            return Lc, bottom, sb, bw / 2
         474 +        return best[1], bottom, sb, best[2]
         475 +
         476 +    def _blocking(self):
         477 +        """Obstructions that interfere with placing the block on the surface."""
         478 +        robot, block, surf, obst = self._objs()
         479 +        s = self.state
         480 +        left, bottom, sb, g = self._final_placement()
         481 +        bb = _rect_bbox(s, block)
         482 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         483 +        final_bb = (left, bottom, left + bw, bottom + bh)
         484 +        rx = left + g
         485 +        ry = bottom + bh + TIP + 0.003
         486 +        res = []
         487 +        for o in obst:
         488 +            ob = _rect_bbox(s, o)
         489 +            if not self._descent_free(rx, ry, final_bb, [ob], margin=0.015):
         490 +                res.append(o)
         491 +        return res
         492 +
         493 +    def _final_sweep(self):
         494 +        """(rx, ry, final_bb) for the final block placement."""
         495 +        robot, block, surf, obst = self._objs()
         496 +        left, bottom, sb, g = self._final_placement()
         497 +        bb = _rect_bbox(self.state, block)
         498 +        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
         499 +        final_bb = (left, bottom, left + bw, bottom + bh)
         500 +        return left + g, bottom + bh + TIP + 0.003, final_bb
         501 +
         502 +    def _find_spot(self, o):
         503 +        """Find (left, bottom) to park the (currently grasped) obstruction o."""
         504 +        robot, block, surf, obst = self._objs()
         505 +        s = self.state
         506 +        ob = _rect_bbox(s, o)
         507 +        w, h = ob[2] - ob[0], ob[3] - ob[1]
         508 +        x, y, _, _ = self._rpos()
         509 +        goff = x - ob[0]
         510 +        hang = y - ob[3]  # robot y minus object top
         511 +        sb = _rect_bbox(s, surf)
         512 +        others = self._others_bboxes([o])
         513 +        frx, fry, fbb = self._final_sweep()
         514 +        # target block pickup sweep
         515 +        _, _, _, g = self._final_placement()
         516 +        bb = _rect_bbox(s, block)
         517 +        brx = bb[0] + g
         518 +        bry = bb[3] + TIP + 0.003
         519 +        levels = [(v, 0.0) for v in np.arange(FLOOR + 0.005, self.TOP_MAX - h, 0.02)]
         520 +        # remaining blockers' pickup columns must stay free
         521 +        cols = []
         522 +        for ob2 in self._blocking():
         523 +            if ob2 == o:
         524 +                continue
         525 +            b2 = _rect_bbox(s, ob2)
         526 +            cols.append(((b2[0] + b2[2]) / 2, b2[3] + TIP + 0.003, b2))
         527 +        cands = []
         528 +        xs = np.arange(WORLD_X[0] + 0.002, WORLD_X[1] - w - 0.002, 0.01)
         529 +        for bottom, pen in levels:
         530 +            for lx in xs:
         531 +                rx = lx + goff
         532 +                if rx < RX_MIN or rx > RX_MAX:
         533 +                    continue
         534 +                cand = (lx, bottom, lx + w, bottom + h)
         535 +                if cand[0] < sb[2] + 0.01 and cand[2] > sb[0] - 0.01:
         536 +                    continue
         537 +                bad = False
         538 +                for b in others:
         539 +                    if _overlap(cand, b, 0.01):
         540 +                        bad = True
         541 +                        break
         542 +                if bad:
         543 +                    continue
         544 +                if not self._descent_free(frx, fry, fbb, [cand], margin=0.02):
         545 +                    continue
         546 +                if not self._descent_free(brx, bry, bb, [cand], margin=0.02):
         547 +                    continue
         548 +                if any(not self._descent_free(cx2, cy2, b2, [cand], margin=0.01)
         549 +                       for cx2, cy2, b2 in cols):
         550 +                    continue
         551 +                ry = bottom + h + hang
         552 +                if not self._descent_free(rx, ry, cand, others, margin=0.012):
         553 +                    continue
         554 +                cost = max(abs(rx - x), abs(ry - y)) + max(abs(rx - brx), abs(ry - bry)) + pen
         555 +                cands.append((cost, lx, bottom, rx, ry, cand))
         556 +        if not cands:
         557 +            return None
         558 +        cands.sort(key=lambda c: c[0])
         559 +        binned = {}
         560 +        for c in cands:
         561 +            k = int(c[3] / 0.08)
         562 +            if k not in binned:
         563 +                binned[k] = c
         564 +        cands = sorted(binned.values(), key=lambda c: c[0])
         565 +        # rerank a few best candidates by planned path costs
         566 +        surf_bb = sb
         567 +        crel_o = (ob[0] - x, ob[1] - y, ob[2] - x, ob[3] - y)
         568 +        crel_b = (bb[0] - brx, bb[1] - bry, bb[2] - brx, bb[3] - bry)
         569 +        best = None
         570 +        for cost, lx, bottom, rx, ry, cand in cands[:self.K_RERANK]:
         571 +            obs1 = others + [surf_bb]
         572 +            c1 = self._path_cost((x, y), (rx, ry), obs1, crel_o)
         573 +            obs2 = [bx for bx in others] + [cand, surf_bb]
         574 +            if cols:
         575 +                nx, ny = min(((cx2, cy2) for cx2, cy2, _ in cols),
         576 +                             key=lambda p: max(abs(p[0] - rx), abs(p[1] - ry)))
         577 +                c2 = self._path_cost((rx, ry + 0.01), (nx, ny), obs2, None)
         578 +                c2 += max(abs(nx - brx), abs(ny - bry)) / 0.05 * 0.5
         579 +            else:
         580 +                c2 = self._path_cost((rx, ry + 0.01), (brx, bry), obs2, None)
         581 +            obs3 = [bx for bx in others if bx != bb] + [cand, surf_bb]
         582 +            c3 = self._path_cost((brx, bry), (frx, fry), obs3, crel_b)
         583 +            tot = c1 + c2 + c3
         584 +            if best is None or tot < best[0]:
         585 +                best = (tot, lx, bottom)
         586 +        return best[1], best[2]
         587 +
         588 +    def _plan(self):
         589 +        self.vac = 0.0
         590 +        failures = 0
         591 +        for _ in range(30):
         592 +            blockers = self._blocking()
         593 +            if not blockers:
         594 +                break
         595 +            robot, block, surf, obst = self._objs()
         596 +            x, y, _, _ = self._rpos()
         597 +            if self.ORDER == "tall":
         598 +                blockers.sort(key=lambda o: (-_rect_bbox(self.state, o)[3]))
         599 +            else:
         600 +                def _d(o):
         601 +                    b = _rect_bbox(self.state, o)
         602 +                    return max(abs((b[0] + b[2]) / 2 - x), abs(b[3] + TIP - y))
         603 +                blockers.sort(key=_d)
         604 +            picked = False
         605 +            for o in blockers:
         606 +                others = self._others_bboxes([o])
         607 +                if self._choose_grasp_x(o, others) is None:
         608 +                    continue
         609 +                ok = yield from self._pick(o)
         610 +                if not ok:
         611 +                    failures += 1
         612 +                    continue
         613 +                spot = self._find_spot(o)
         614 +                if spot is None:
         615 +                    spot = (_rect_bbox(self.state, o)[0], FLOOR + 0.005)
         616 +                    failures += 1
         617 +                left, bottom = spot
         618 +                ok = yield from self._place_at(o, left, bottom, release=True)
         619 +                if self.vac > 0.5:
         620 +                    self.vac = 0.0
         621 +                    yield self._act()
         622 +                self.vac = 0.0
         623 +                if not ok:
         624 +                    failures += 1
         625 +                    continue
         626 +                picked = True
         627 +                break
         628 +            if not picked:
         629 +                failures += 1
         630 +                if failures > 5:
         631 +                    break
         632 +        # now the target block
         633 +        robot, block, surf, obst = self._objs()
         634 +        for _ in range(10):
         635 +            left, bottom, sb, g = self._final_placement()
         636 +            bb = _rect_bbox(self.state, block)
         637 +            ok = yield from self._pick(block, pref=bb[0] + g)
         638 +            if not ok:
         639 +                self.vac = 0.0
         640 +                yield self._act()
         641 +                continue
         642 +            left, bottom, sb, g = self._final_placement()
         643 +            ok = yield from self._place_at(block, left, bottom)
         644 +            if ok:
         645 +                break
         646 +        self.vac = 0.0
         647 +        for _ in range(5):
         648 +            yield self._act()
diff --git a/approach_noarm.py b/approach_noarm.py
new file mode 100644
index 0000000..89c6528
--- /dev/null
+++ b/approach_noarm.py
@@ -0,0 +1,3 @@
           1 +from approach import GeneratedApproach as _G
           2 +class GeneratedApproach(_G):
           3 +    USE_ARM_DP = False
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..88ea02a
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,18 @@
           1 +import sys, numpy as np, approach
           2 +from env_client import make_env
           3 +seed=int(sys.argv[1]); N=int(sys.argv[2])
           4 +env=make_env(); obs,info=env.reset(seed=seed)
           5 +ap=approach.GeneratedApproach(env.action_space, env.observation_space, None); ap.reset(obs,info)
           6 +orig=ap._dp_path3
           7 +def wrap(x0,y0,arm0,x1,tipy1,obstacles,ctip):
           8 +    r=orig(x0,y0,arm0,x1,tipy1,obstacles,ctip)
           9 +    if r is None:
          10 +        print('DP3 FAIL', x0,y0,arm0,x1,tipy1,ctip, obstacles)
          11 +        A=ap.ARMS
          12 +        for a in A:
          13 +            for yy in np.arange(0.2,0.9,0.05):
          14 +                print(a, round(yy,2), ap._free_pts3(np.array([x0]),np.array([yy]),obstacles,ctip,a), ap._free_pts3(np.array([x1]),np.array([yy]),obstacles,ctip,a))
          15 +    return r
          16 +ap._dp_path3=wrap
          17 +for i in range(N):
          18 +    a=ap.get_action(obs); obs,*_=env.step(a)
diff --git a/probe_stuck.py b/probe_stuck.py
new file mode 100644
index 0000000..2cfb133
--- /dev/null
+++ b/probe_stuck.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +import numpy as np, approach
           3 +env = make_env()
           4 +obs, info = env.reset(seed=7)
           5 +ap = approach.GeneratedApproach(env.action_space, env.observation_space, None)
           6 +ap.reset(obs, info)
           7 +for i in range(32):
           8 +    a = ap.get_action(obs); obs,*_ = env.step(a)
           9 +R = obs.get_object_from_name('robot')
          10 +for n in obs.get_object_names():
          11 +    o=obs.get_object_from_name(n)
          12 +    print(n, [round(float(obs.get(o,f)),3) for f in (['x','y','arm_joint','theta'] if n=='robot' else ['x','y','width','height'])])
          13 +import copy
          14 +for a in [[0,-0.026,0,0,1],[0.024,0,0,0,1],[0,-0.01,0,0,1],[0,-0.02,0,0,1],[0,0,0,0.0,0]]:
          15 +    o2,*_ = env.step(np.array(a,dtype=np.float32))
          16 +    print(a, [round(float(o2.get(R,f)),3) for f in ['x','y','arm_joint','vacuum']])
          17 +print('---')
          18 +o2,*_ = env.step(np.array([0,0,0,0,1],dtype=np.float32))
          19 +for a in [[0,0.004,0,0,1],[0.024,0,0,0,1],[0.024,0,0,0,1],[0.05,0,0,0,1],[0,0.03,0,0,1],[0.05,0,0,0,1]]:
          20 +    o2,*_ = env.step(np.array(a,dtype=np.float32))
          21 +    B=o2.get_object_from_name('obstruction0')
          22 +    print(a, [round(float(o2.get(R,f)),3) for f in ['x','y','arm_joint','vacuum']], round(float(o2.get(B,'x')),3), round(float(o2.get(B,'y')),3))
```

</details>

<a id="C011"></a>
### C011 · 3D DP: don't force goal cell free for arms where exact goal collides

Commit `fec32dd911ab498c5a5ecd25f407b14403a1aac9`; parents: 421d9a586411b4d5ca9cc889e07e2f5d60724059. Recorded author date: 2026-09-30T11:24:48+02:00.

File roles (automatic): policy.

- [E0495](01_timeline.md#E0495): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_fec32dd_approach.py) · [Exact all-file diff](evidence/diffs/C011_fec32dd.diff)

[Previous saved controller snapshot](evidence/versions/C010_421d9a5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c3c6fee..e812c56 100644
--- a/approach.py
+++ b/approach.py
@@ -361,7 +361,8 @@ class GeneratedApproach:
  361    361                  F[a][ci_] |= self._free_pts3(XX[ci_], YY[ci_], obstacles, ctip, A[a], m=0.001)
  362    362          F[a0][0, j0] = True
  363    363          for a in range(NA):
  364        -            F[a][2 * N, jg[a]] = True
         364 +            gok = self._free_pts3(np.array([x1]), np.array([tipy1 + A[a] + GW]), obstacles, ctip, A[a], m=0.001)[0]
         365 +            F[a][2 * N, jg[a]] = bool(gok)
  365    366          INF = 1e9
  366    367          J = np.arange(nl)
  367    368          vc = np.ceil(np.abs(J[:, None] - J[None, :]) / K)
```

</details>

<a id="C012"></a>
### C012 · Add optional 3D DP spot costs (disabled: no gain, slower)

Commit `c6c922b66d02fd0d4acc8cfb3ddb4d572ce2588e`; parents: fec32dd911ab498c5a5ecd25f407b14403a1aac9. Recorded author date: 2026-09-30T11:36:02+02:00.

File roles (automatic): policy.

- [E0545](01_timeline.md#E0545): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_c6c922b_approach.py) · [Exact all-file diff](evidence/diffs/C012_c6c922b.diff)

[Previous saved controller snapshot](evidence/versions/C011_fec32dd_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e812c56..b749f66 100644
--- a/approach.py
+++ b/approach.py
@@ -305,7 +305,22 @@ class GeneratedApproach:
  305    305                  return path
  306    306          return [(x0, ROBOT_Y_MAX), (x1, ROBOT_Y_MAX), (x1, y1)]
  307    307  
  308        -    def _path_cost(self, p0, p1, obstacles, crel):
         308 +    COST3 = False
         309 +
         310 +    def _path_cost(self, p0, p1, obstacles, crel, arm0=ARM):
         311 +        if self.COST3:
         312 +            ctip = None
         313 +            if crel is not None:
         314 +                ctip = (crel[0], crel[1] + arm0 + GW, crel[2], crel[3] + arm0 + GW)
         315 +            path = self._dp_path3(p0[0], p0[1], arm0, p1[0], p1[1] - TIP, obstacles, ctip)
         316 +            if path is not None:
         317 +                c = 0.0
         318 +                prev = (p0[0], p0[1], arm0)
         319 +                for q in path:
         320 +                    c += max(1, math.ceil(max(abs(q[0] - prev[0]) / 0.05, abs(q[1] - prev[1]) / 0.05,
         321 +                                              abs(q[2] - prev[2]) / 0.1) - 1e-6)) if q != prev else 0
         322 +                    prev = q
         323 +                return c
  309    324          path = self._plan_path(p1[0], p1[1], obstacles, crel, start=p0)
  310    325          pts = [p0] + path
  311    326          c = 0.0
@@ -719,7 +734,7 @@ class GeneratedApproach:
  719    734          best = None
  720    735          for cost, lx, bottom, rx, ry, cand in cands[:self.K_RERANK]:
  721    736              obs1 = others + [surf_bb]
  722        -            c1 = self._path_cost((x, y), (rx, ry), obs1, crel_o)
         737 +            c1 = self._path_cost((x, y), (rx, ry), obs1, crel_o, arm0=self._rpos()[3])
  723    738              obs2 = [bx for bx in others] + [cand, surf_bb]
  724    739              if cols:
  725    740                  nx, ny = min(((cx2, cy2) for cx2, cy2, _ in cols),
```

</details>

