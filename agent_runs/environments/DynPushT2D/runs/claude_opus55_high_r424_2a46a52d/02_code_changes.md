# DynPushT2D · claude-opus-5-5 · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `042f626` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `006fef5` | Model-based push planner v1 + push model + tests | approach.py, data_1.npz, data_2.npz, data_3.npz, data_4.npz, e0.py, e1.py, e10.py, e11.py, e2.py, e3.py, e4.py, e5.py, e6.py, e7.py, e8.py, e9.py, eval2.py, eval_model.py, eval_ro… | [E0174](01_timeline.md#E0174) |
| [C003](#C003) · `343f45d` | parametrize | approach.py, tune.py | [E0187](01_timeline.md#E0187) |
| [C004](#C004) · `4e9e824` | Fix goal angle: env compares theta raw (unwrapped); target clipped interval | approach.py, collect_term.py, fit_term.py, seq_term.py, term_data.npy, trace.py, tune.py | [E0239](01_timeline.md#E0239) |
| [C005](#C005) · `6fb871a` | Two-stage lookahead planner | approach.py, new_plan.py, timing.py | [E0255](01_timeline.md#E0255) |
| [C006](#C006) · `214da58` | Grid Dijkstra nav cost + nav paths | approach.py, breakdown.py, navgrid.py, t_nav.py | [E0282](01_timeline.md#E0282) |
| [C007](#C007) · `8284b12` | curved push option | approach.py, breakdown2.py | [E0299](01_timeline.md#E0299) |
| [C008](#C008) · `5e42bbd` | stage2 curvs param | approach.py | [E0306](01_timeline.md#E0306) |
| [C009](#C009) · `6bd49cf` | defaults: curved pushes, LOOK 15 | approach.py | [E0315](01_timeline.md#E0315) |
| [C010](#C010) · `7734cf0` | time guard + stagnation fallback | approach.py | [E0397](01_timeline.md#E0397) |
| [C011](#C011) · `cbb8923` | TC_THR param | approach.py | [E0406](01_timeline.md#E0406) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `042f626ce1e87762a3719d4de001cd1dcd298d9e`; parents: none (initial snapshot). Recorded author date: 2026-09-30T16:51:42+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_042f626.diff)

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
index 0000000..d92c4df
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "193a91d085d251bdec050c341c0e14db", "observation_space": {"type": "Box", "shape": [45], "low": [-Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity], "high": [Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity], "dtype": "float64"}, "action_space": {"type": "Box", "shape": [2], "low": [-0.05, -0.05], "high": [0.05, 0.05], "dtype": "float64"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Model-based push planner v1 + push model + tests

Commit `006fef5a37b4db13517bb8777ab8772bc1e84118`; parents: 042f626ce1e87762a3719d4de001cd1dcd298d9e. Recorded author date: 2026-09-30T17:04:50+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0174](01_timeline.md#E0174): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_006fef5_approach.py) · [Exact all-file diff](evidence/diffs/C002_006fef5.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..a38e996
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,394 @@
           1 +"""Model-based pushing controller for DynPushT2D.
           2 +
           3 +Uses an empirically-fitted quasi-static impulse push model (see push_model.py
           4 +notes) vectorised over many candidate pushes. Each decision: sample contact
           5 +points on the T boundary x push directions x step sizes, roll out, choose best
           6 +(cost + step penalty), navigate (A*) to pre-contact point, execute push, replan.
           7 +"""
           8 +import heapq
           9 +import math
          10 +
          11 +import numpy as np
          12 +
          13 +C_GAP = 0.265
          14 +MU = 1.0
          15 +LO, HI = 0.1, 4.9  # robot centre bounds
          16 +AMAX = 0.049
          17 +
          18 +
          19 +def _wrap(a):
          20 +    return (a + np.pi) % (2 * np.pi) - np.pi
          21 +
          22 +
          23 +def geometry(obs):
          24 +    w, L, V = float(obs[12]), float(obs[13]), float(obs[14])
          25 +    A1, A2 = L * w, V * w
          26 +    y1, y2 = -w / 2, -w - V / 2
          27 +    yc = (A1 * y1 + A2 * y2) / (A1 + A2)
          28 +    I = (A1 * (L * L + w * w) / 12 + A1 * (y1 - yc) ** 2
          29 +         + A2 * (V * V + w * w) / 12 + A2 * (y2 - yc) ** 2)
          30 +    rects = np.array([(-L / 2, L / 2, -w, 0.0), (-w / 2, w / 2, -w - V, -w)])
          31 +    return rects, np.array([0.0, yc]), I / (A1 + A2)
          32 +
          33 +
          34 +class Model:
          35 +    def __init__(self, obs):
          36 +        self.rects, self.com, self.k2 = geometry(obs)
          37 +        self.r = float(obs[28])
          38 +        w, L, V = float(obs[12]), float(obs[13]), float(obs[14])
          39 +        self.corners = np.array([(-L / 2, 0), (L / 2, 0), (L / 2, -w), (-L / 2, -w),
          40 +                                 (w / 2, -w - V), (-w / 2, -w - V)])
          41 +
          42 +    def closest(self, q):
          43 +        """q: (N,2) local points. returns p (N,2), d (N,), n (N,2) outward normal."""
          44 +        best_p = None
          45 +        best_d = None
          46 +        for x0, x1, y0, y1 in self.rects:
          47 +            p = np.stack([np.clip(q[:, 0], x0, x1), np.clip(q[:, 1], y0, y1)], 1)
          48 +            d = np.linalg.norm(q - p, axis=1)
          49 +            if best_p is None:
          50 +                best_p, best_d = p, d
          51 +            else:
          52 +                m = d < best_d
          53 +                best_p = np.where(m[:, None], p, best_p)
          54 +                best_d = np.where(m, d, best_d)
          55 +        n = (q - best_p) / np.maximum(best_d, 1e-12)[:, None]
          56 +        return best_p, best_d, n
          57 +
          58 +    def world_dist(self, pos, th, pts):
          59 +        """distance from world points pts (N,2) to T with pose (pos (N,2), th (N,))."""
          60 +        c, s = np.cos(th), np.sin(th)
          61 +        rel = pts - pos
          62 +        q = np.stack([c * rel[:, 0] + s * rel[:, 1], -s * rel[:, 0] + c * rel[:, 1]], 1)
          63 +        _, d, _ = self.closest(q)
          64 +        return d
          65 +
          66 +    def step(self, pos, th, rob, a, n_sub=2):
          67 +        for _ in range(n_sub):
          68 +            pos, th = self._step1(pos, th, rob, a / n_sub, C_GAP * n_sub)
          69 +            rob = rob + a / n_sub
          70 +        return pos, th
          71 +
          72 +    def _step1(self, pos, th, rob, a, c_gap):
          73 +        c, s = np.cos(th), np.sin(th)
          74 +        rob1 = rob + a
          75 +        rel = rob1 - pos
          76 +        q = np.stack([c * rel[:, 0] + s * rel[:, 1], -s * rel[:, 0] + c * rel[:, 1]], 1)
          77 +        al = np.stack([c * a[:, 0] + s * a[:, 1], -s * a[:, 0] + c * a[:, 1]], 1)
          78 +        p, d, n = self.closest(q)
          79 +        a_n = -(al * n).sum(1)
          80 +        gstar = self.r + c_gap * np.maximum(a_n, 0.0)
          81 +        active = (d < gstar) & (a_n > 1e-12)
          82 +        if not active.any():
          83 +            return pos, th
          84 +        frac = np.clip((gstar - d) / np.maximum(a_n, 1e-12), 0.0, 1.0)
          85 +        u = al * frac[:, None]
          86 +        rc = p - self.com
          87 +        k2 = self.k2
          88 +        K00 = 1 + rc[:, 1] ** 2 / k2
          89 +        K01 = -rc[:, 0] * rc[:, 1] / k2
          90 +        K11 = 1 + rc[:, 0] ** 2 / k2
          91 +        det = K00 * K11 - K01 * K01
          92 +        J0 = (K11 * u[:, 0] - K01 * u[:, 1]) / det
          93 +        J1 = (-K01 * u[:, 0] + K00 * u[:, 1]) / det
          94 +        nin = -n
          95 +        t = np.stack([-nin[:, 1], nin[:, 0]], 1)
          96 +        jn = J0 * nin[:, 0] + J1 * nin[:, 1]
          97 +        jt = J0 * t[:, 0] + J1 * t[:, 1]
          98 +        slide = np.abs(jt) > MU * jn
          99 +        if slide.any():
         100 +            dJ = nin + (MU * np.sign(jt))[:, None] * t
         101 +            KdJ0 = K00 * dJ[:, 0] + K01 * dJ[:, 1]
         102 +            KdJ1 = K01 * dJ[:, 0] + K11 * dJ[:, 1]
         103 +            den = nin[:, 0] * KdJ0 + nin[:, 1] * KdJ1
         104 +            un = (u * nin).sum(1)
         105 +            j = un / np.where(np.abs(den) < 1e-12, 1e-12, den)
         106 +            J0 = np.where(slide, j * dJ[:, 0], J0)
         107 +            J1 = np.where(slide, j * dJ[:, 1], J1)
         108 +        J0 = np.where(active, J0, 0.0)
         109 +        J1 = np.where(active, J1, 0.0)
         110 +        om = (rc[:, 0] * J1 - rc[:, 1] * J0) / k2
         111 +        # COM world
         112 +        cx, cy = self.com
         113 +        comw = pos + np.stack([c * cx - s * cy, s * cx + c * cy], 1)
         114 +        comw = comw + np.stack([c * J0 - s * J1, s * J0 + c * J1], 1)
         115 +        th2 = th + om
         116 +        c2, s2 = np.cos(th2), np.sin(th2)
         117 +        pos2 = comw - np.stack([c2 * cx - s2 * cy, s2 * cx + c2 * cy], 1)
         118 +        return pos2, th2
         119 +
         120 +
         121 +class GeneratedApproach:
         122 +    def __init__(self, action_space, observation_space, primitives):
         123 +        self.action_space = action_space
         124 +        self.rng = np.random.default_rng(0)
         125 +
         126 +    # ------------------------------------------------------------------
         127 +    def reset(self, state, info):
         128 +        self.model = Model(state)
         129 +        self.goal = np.array(state[29:32], float)
         130 +        self.plan = []  # list of actions
         131 +        self.expect_block = None
         132 +        self.nsteps = 0
         133 +        self._build_candidates(state)
         134 +
         135 +    def _build_candidates(self, obs):
         136 +        m = self.model
         137 +        w, L, V = float(obs[12]), float(obs[13]), float(obs[14])
         138 +        pts, nrm = [], []
         139 +
         140 +        def edge(p0, p1, n, k):
         141 +            for f in np.linspace(0, 1, k):
         142 +                pts.append(np.array(p0) * (1 - f) + np.array(p1) * f)
         143 +                nrm.append(n)
         144 +        e = 0.02
         145 +        edge((-L / 2 + e, 0), (L / 2 - e, 0), (0, 1), 13)          # top
         146 +        edge((-L / 2, -e), (-L / 2, -w + e), (-1, 0), 1)             # left end
         147 +        edge((L / 2, -e), (L / 2, -w + e), (1, 0), 1)                # right end
         148 +        edge((-L / 2 + e, -w), (-w / 2 - 0.12, -w), (0, -1), 5)      # bottom left
         149 +        edge((w / 2 + 0.12, -w), (L / 2 - e, -w), (0, -1), 5)       # bottom right
         150 +        edge((-w / 2, -w - 0.12), (-w / 2, -w - V + e), (-1, 0), 9)  # stem left
         151 +        edge((w / 2, -w - 0.12), (w / 2, -w - V + e), (1, 0), 9)     # stem right
         152 +        edge((0, -w - V), (0, -w - V), (0, -1), 1)                    # stem tip
         153 +        pts = np.array(pts, float)
         154 +        nrm = np.array(nrm, float)
         155 +        # side edges: only mid point, use exact mid
         156 +        angs = np.deg2rad(np.array([-50, -35, -20, -8, 0, 8, 20, 35, 50]))
         157 +        P, Nn, A = [], [], []
         158 +        for i in range(len(pts)):
         159 +            for a in angs:
         160 +                P.append(pts[i])
         161 +                Nn.append(nrm[i])
         162 +                A.append(a)
         163 +        self.c_pts = np.array(P)
         164 +        self.c_nrm = np.array(Nn)
         165 +        self.c_ang = np.array(A)
         166 +
         167 +    # ------------------------------------------------------------------
         168 +    def _cost(self, pos, th):
         169 +        ex = pos[..., 0] - self.goal[0]
         170 +        ey = pos[..., 1] - self.goal[1]
         171 +        et = _wrap(th - self.goal[2])
         172 +        return np.sqrt(ex ** 2 + ey ** 2) + 0.35 * np.abs(et)
         173 +
         174 +    def _solved(self, pos, th):
         175 +        return (abs(pos[0] - self.goal[0]) < 0.03 and abs(pos[1] - self.goal[1]) < 0.03
         176 +                and abs(_wrap(th - self.goal[2])) < np.deg2rad(8))
         177 +
         178 +    def _cost_tight(self, pos, th):
         179 +        ex = np.abs(pos[..., 0] - self.goal[0]) / 0.03
         180 +        ey = np.abs(pos[..., 1] - self.goal[1]) / 0.03
         181 +        et = np.abs(_wrap(th - self.goal[2])) / np.deg2rad(8)
         182 +        return np.maximum(np.maximum(ex, ey), et)
         183 +
         184 +    def _plan_push(self, obs):
         185 +        m = self.model
         186 +        pos0 = np.array(obs[0:2], float)
         187 +        th0 = float(obs[2])
         188 +        rob0 = np.array(obs[16:18], float)
         189 +        c, s = math.cos(th0), math.sin(th0)
         190 +        Rm = np.array([[c, -s], [s, c]])
         191 +        r = m.r
         192 +        cands_start, cands_dir = [], []
         193 +        # world contact points + normals
         194 +        pw = self.c_pts @ Rm.T + pos0
         195 +        nw = self.c_nrm @ Rm.T
         196 +        start = pw + nw * (r + 0.03)
         197 +        ca, sa = np.cos(self.c_ang), np.sin(self.c_ang)
         198 +        nin = -nw
         199 +        dirs = np.stack([ca * nin[:, 0] - sa * nin[:, 1], sa * nin[:, 0] + ca * nin[:, 1]], 1)
         200 +        # also: continue from current robot position in a set of directions
         201 +        cur_d = np.linspace(-np.pi, np.pi, 24, endpoint=False)
         202 +        cstart = np.repeat(rob0[None], len(cur_d), 0)
         203 +        cdirs = np.stack([np.cos(cur_d), np.sin(cur_d)], 1)
         204 +        starts = np.concatenate([start, cstart])
         205 +        dirs = np.concatenate([dirs, cdirs])
         206 +        # validity of starts
         207 +        ok = (starts[:, 0] >= LO + 0.01) & (starts[:, 0] <= HI - 0.01) & \
         208 +             (starts[:, 1] >= LO + 0.01) & (starts[:, 1] <= HI - 0.01)
         209 +        dstart = m.world_dist(np.repeat(pos0[None], len(starts), 0), np.full(len(starts), th0), starts)
         210 +        ok &= (dstart > r + 0.02) | (np.arange(len(starts)) >= len(start))
         211 +        starts, dirs = starts[ok], dirs[ok]
         212 +        # navigation cost estimate
         213 +        nav = np.linalg.norm(starts - rob0, axis=1) / AMAX
         214 +        nav = nav * 1.3 + np.where(nav > 1e-6, 3.0, 0.0)
         215 +        cost0 = float(self._cost(pos0, th0))
         216 +        err_pos = np.linalg.norm(pos0 - self.goal[:2])
         217 +        err_th = abs(_wrap(th0 - self.goal[2]))
         218 +        steps_opts = [AMAX, 0.02, 0.008]
         219 +        best = None
         220 +        KMAX = 30
         221 +        tight0 = float(self._cost_tight(pos0, th0))
         222 +        for ss in steps_opts:
         223 +            N = len(starts)
         224 +            pos = np.repeat(pos0[None], N, 0)
         225 +            th = np.full(N, th0)
         226 +            rob = starts.copy()
         227 +            a = dirs * ss
         228 +            alive = np.ones(N, bool)
         229 +            for k in range(1, KMAX + 1):
         230 +                nrob = rob + a
         231 +                inb = (nrob[:, 0] >= LO) & (nrob[:, 0] <= HI) & (nrob[:, 1] >= LO) & (nrob[:, 1] <= HI)
         232 +                alive &= inb
         233 +                pos_n, th_n = m.step(pos, th, rob, a)
         234 +                pos = np.where(alive[:, None], pos_n, pos)
         235 +                th = np.where(alive, th_n, th)
         236 +                rob = np.where(alive[:, None], nrob, rob)
         237 +                # block corners within walls
         238 +                cc, sc = np.cos(th), np.sin(th)
         239 +                cx = pos[:, 0:1] + cc[:, None] * m.corners[None, :, 0] - sc[:, None] * m.corners[None, :, 1]
         240 +                cy = pos[:, 1:2] + sc[:, None] * m.corners[None, :, 0] + cc[:, None] * m.corners[None, :, 1]
         241 +                wall = (cx.min(1) < 0.02) | (cx.max(1) > 4.98) | (cy.min(1) < 0.02) | (cy.max(1) > 4.98)
         242 +                alive &= ~wall
         243 +                cst = self._cost(pos, th)
         244 +                tc = self._cost_tight(pos, th)
         245 +                total = nav + k
         246 +                score = cst + 0.0015 * total + np.where(tc < 1.0, -1.0, 0.0) * 0
         247 +                score = np.where(tc < 0.8, -10.0 + 0.001 * total, score)
         248 +                score = np.where(alive, score, np.inf)
         249 +                i = int(np.argmin(score))
         250 +                if best is None or score[i] < best[0]:
         251 +                    best = (float(score[i]), starts[i].copy(), a[i].copy(), k, float(cst[i]))
         252 +        return best, cost0
         253 +
         254 +    # ------------------------------------------------------------------
         255 +    def _navigate(self, obs, target):
         256 +        """Return list of actions from robot pos to target avoiding the block."""
         257 +        m = self.model
         258 +        rob = np.array(obs[16:18], float)
         259 +        pos0 = np.array(obs[0:2], float)
         260 +        th0 = float(obs[2])
         261 +        clear = m.r + 0.015
         262 +
         263 +        def seg_clear(p, q):
         264 +            n = max(2, int(np.linalg.norm(q - p) / 0.01) + 1)
         265 +            f = np.linspace(0, 1, n)[:, None]
         266 +            pts = p * (1 - f) + q * f
         267 +            d = m.world_dist(np.repeat(pos0[None], n, 0), np.full(n, th0), pts)
         268 +            d0 = d[0]
         269 +            # allow starting inside margin as long as we don't get closer
         270 +            return bool(np.all((d >= clear) | (d >= d0 - 1e-9) & (np.arange(n) < 10)))
         271 +
         272 +        if seg_clear(rob, target):
         273 +            path = [rob, target]
         274 +        else:
         275 +            path = self._astar(rob, target, pos0, th0, clear)
         276 +            if path is None:
         277 +                path = [rob, target]
         278 +        acts = []
         279 +        cur = rob.copy()
         280 +        for wp in path[1:]:
         281 +            wp = np.asarray(wp, float)
         282 +            while True:
         283 +                d = wp - cur
         284 +                dist = np.linalg.norm(d)
         285 +                if dist < 1e-9:
         286 +                    break
         287 +                n = int(math.ceil(dist / AMAX - 1e-9))
         288 +                stp = d / n
         289 +                for _ in range(n):
         290 +                    acts.append(stp.copy())
         291 +                cur = wp.copy()
         292 +                break
         293 +        return acts
         294 +
         295 +    def _astar(self, start, goal, pos0, th0, clear):
         296 +        m = self.model
         297 +        res = 0.04
         298 +        n = int(round((HI - LO) / res)) + 1
         299 +        xs = LO + np.arange(n) * res
         300 +        X, Y = np.meshgrid(xs, xs, indexing="ij")
         301 +        pts = np.stack([X.ravel(), Y.ravel()], 1)
         302 +        d = m.world_dist(np.repeat(pos0[None], len(pts), 0), np.full(len(pts), th0), pts)
         303 +        free = (d >= clear + 0.01).reshape(n, n)
         304 +
         305 +        def cell(p):
         306 +            i = int(round((p[0] - LO) / res))
         307 +            j = int(round((p[1] - LO) / res))
         308 +            return min(max(i, 0), n - 1), min(max(j, 0), n - 1)
         309 +
         310 +        s = cell(start)
         311 +        g = cell(goal)
         312 +        # ensure start/goal free (search nearest free)
         313 +        def nearest_free(c):
         314 +            if free[c]:
         315 +                return c
         316 +            idx = np.argwhere(free)
         317 +            dd = ((idx - np.array(c)) ** 2).sum(1)
         318 +            k = int(np.argmin(dd))
         319 +            return tuple(idx[k])
         320 +        s2 = nearest_free(s)
         321 +        g2 = nearest_free(g)
         322 +        nbrs = [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (1, 1, 1.4142), (1, -1, 1.4142),
         323 +                (-1, 1, 1.4142), (-1, -1, 1.4142)]
         324 +        dist = {s2: 0.0}
         325 +        prev = {}
         326 +        h = lambda c: math.hypot(c[0] - g2[0], c[1] - g2[1])
         327 +        pq = [(h(s2), 0.0, s2)]
         328 +        found = False
         329 +        while pq:
         330 +            f, gc, c = heapq.heappop(pq)
         331 +            if c == g2:
         332 +                found = True
         333 +                break
         334 +            if gc > dist.get(c, 1e18):
         335 +                continue
         336 +            for di, dj, w in nbrs:
         337 +                nc = (c[0] + di, c[1] + dj)
         338 +                if 0 <= nc[0] < n and 0 <= nc[1] < n and free[nc]:
         339 +                    ng = gc + w
         340 +                    if ng < dist.get(nc, 1e18):
         341 +                        dist[nc] = ng
         342 +                        prev[nc] = c
         343 +                        heapq.heappush(pq, (ng + h(nc), ng, nc))
         344 +        if not found:
         345 +            return None
         346 +        cells = [g2]
         347 +        while cells[-1] != s2:
         348 +            cells.append(prev[cells[-1]])
         349 +        cells.reverse()
         350 +        raw = [np.array(start)] + [np.array([xs[i], xs[j]]) for i, j in cells] + [np.array(goal)]
         351 +        # shortcut smoothing
         352 +        def seg_ok(p, q):
         353 +            k = max(2, int(np.linalg.norm(q - p) / 0.01) + 1)
         354 +            f = np.linspace(0, 1, k)[:, None]
         355 +            pp = p * (1 - f) + q * f
         356 +            dd = m.world_dist(np.repeat(pos0[None], k, 0), np.full(k, th0), pp)
         357 +            return bool(np.all(dd >= clear))
         358 +        out = [raw[0]]
         359 +        i = 0
         360 +        while i < len(raw) - 1:
         361 +            j = len(raw) - 1
         362 +            while j > i + 1 and not seg_ok(raw[i], raw[j]):
         363 +                j -= 1
         364 +            out.append(raw[j])
         365 +            i = j
         366 +        return out
         367 +
         368 +    # ------------------------------------------------------------------
         369 +    def get_action(self, state):
         370 +        obs = np.asarray(state, float)
         371 +        self.nsteps += 1
         372 +        pos = obs[0:3]
         373 +        if self.plan and self.expect_block is not None:
         374 +            # replan if block moved unexpectedly during navigation
         375 +            if np.abs(pos[0:2] - self.expect_block[0:2]).max() > 0.01 or \
         376 +                    abs(_wrap(pos[2] - self.expect_block[2])) > 0.02:
         377 +                self.plan = []
         378 +        if not self.plan:
         379 +            best, cost0 = self._plan_push(obs)
         380 +            if best is None:
         381 +                return np.zeros(2)
         382 +            _, start, a, k, cst = best
         383 +            acts = self._navigate(obs, start) if np.linalg.norm(start - obs[16:18]) > 1e-9 else []
         384 +            self.expect_block = obs[0:3].copy()
         385 +            self.nav_len = len(acts)
         386 +            self.plan = acts + [a.copy() for _ in range(k)]
         387 +        act = self.plan.pop(0)
         388 +        if self.nav_len > 0:
         389 +            self.nav_len -= 1
         390 +            if self.nav_len == 0:
         391 +                self.expect_block = None
         392 +        else:
         393 +            self.expect_block = None
         394 +        return np.clip(act, -AMAX, AMAX)
diff --git a/data_1.npz b/data_1.npz
new file mode 100644
index 0000000..6d6afeb
Binary files /dev/null and b/data_1.npz differ
diff --git a/data_2.npz b/data_2.npz
new file mode 100644
index 0000000..f9f7b61
Binary files /dev/null and b/data_2.npz differ
diff --git a/data_3.npz b/data_3.npz
new file mode 100644
index 0000000..9da4ed5
Binary files /dev/null and b/data_3.npz differ
diff --git a/data_4.npz b/data_4.npz
new file mode 100644
index 0000000..00222b4
Binary files /dev/null and b/data_4.npz differ
diff --git a/e0.py b/e0.py
new file mode 100644
index 0000000..2632c8e
--- /dev/null
+++ b/e0.py
@@ -0,0 +1,5 @@
           1 +from pm_util import *
           2 +e=E()
           3 +for s in range(6):
           4 +    o=e.reset(s); print(s,o[0:3],o[12:15],o[16:18],o[28],o[29:32],o[41:44])
           5 +o=e.reset(0); print(o)
diff --git a/e1.py b/e1.py
new file mode 100644
index 0000000..5736b81
--- /dev/null
+++ b/e1.py
@@ -0,0 +1,6 @@
           1 +from pm_util import *
           2 +e=E()
           3 +for s in range(200):
           4 +    o=e.reset(s)
           5 +    d=np.linalg.norm(o[0:2]-2.5)
           6 +    if d<0.4: print(s,o[0:3],o[12:15],o[16:18])
diff --git a/e10.py b/e10.py
new file mode 100644
index 0000000..0f8109d
--- /dev/null
+++ b/e10.py
@@ -0,0 +1,18 @@
           1 +from pm_util import *
           2 +e=E()
           3 +for d in [[-1,0],[0,-1],[1,0],[0,1]]:
           4 +    for s in [0.001,0.01,0.049]:
           5 +        o=e.reset(12)
           6 +        for i in range(150): o=e.step(np.array(d)*0.049)
           7 +        for i in range(8): o=e.step(-np.array(d)*0.02)
           8 +        p=o[16:18].copy(); hist=[]
           9 +        for i in range(int(0.3/s)):
          10 +            o=e.step(np.array(d)*s); hist.append(o[16:18].copy())
          11 +        hist=np.array(hist)
          12 +        print(d,s,"final",hist[-1],"last moves",np.round(np.diff(hist[-4:],axis=0).ravel(),5))
          13 +# sliding along wall
          14 +o=e.reset(12)
          15 +for i in range(150): o=e.step(np.array([-0.049,0]))
          16 +p=o[16:18].copy()
          17 +for i in range(10): o=e.step(np.array([-0.02,0.02]))
          18 +print("slide along left wall", p, "->", o[16:18])
diff --git a/e11.py b/e11.py
new file mode 100644
index 0000000..e402dbb
--- /dev/null
+++ b/e11.py
@@ -0,0 +1,4 @@
           1 +from pm_util import *
           2 +e=E(); seed=12
           3 +mv,obs,act=run_push(e,seed,[-0.45,0.25],[0,-1],0.02,60)
           4 +th=obs[:,2]; print(np.round(th[::4],4)); print("min/max",th.min(),th.max(), "block pos end",obs[-1][0:2])
diff --git a/e2.py b/e2.py
new file mode 100644
index 0000000..d168e38
--- /dev/null
+++ b/e2.py
@@ -0,0 +1,10 @@
           1 +from pm_util import *
           2 +e=E()
           3 +for seed in [12,20,24]:
           4 +    o=e.reset(seed); w,L,V=o[12:15]; print("seed",seed,"w L V",w,L,V)
           5 +    tests={"top@x=.3":([0.3,0.5],[0,-1]),"top@x=0":([0.0,0.5],[0,-1]),
           6 +           "barbottom@x=.4":([0.4,-0.4],[0,1]),"barbottom@x=-.4":([-0.4,-0.4],[0,1]),
           7 +           "stembottom":([0,-1.6],[0,1]),"stemside+x@y=-.6":([0.5,-0.6],[-1,0]),"stemside-x@y=-.6":([-0.5,-0.6],[1,0])}
           8 +    for k,(p,d) in tests.items():
           9 +        mv,pv,cu,db=probe(e,seed,p,d)
          10 +        print(f"  {k:20s} navmove={mv:.1e} prev={pv} cur={cu} dblock={db}")
diff --git a/e3.py b/e3.py
new file mode 100644
index 0000000..1648cf0
--- /dev/null
+++ b/e3.py
@@ -0,0 +1,8 @@
           1 +from pm_util import *
           2 +e=E()
           3 +for seed in [12,20]:
           4 +    o=e.reset(seed); w,L,V=o[12:15]; print("seed",seed,"w L V",w,L,V, "L/2",L/2)
           5 +    tests={"rightend":([1.0,-w/2],[-1,0]),"leftend":([-1.0,-w/2],[1,0]),"corner_diag":([0.9,0.3],[-1,-1])}
           6 +    for k,(p,d) in tests.items():
           7 +        mv,pv,cu,db=probe(e,seed,p,d)
           8 +        print(f"  {k:20s} navmove={mv:.1e} prev={pv} cur={cu} dblock={db}")
diff --git a/e4.py b/e4.py
new file mode 100644
index 0000000..dd2d911
--- /dev/null
+++ b/e4.py
@@ -0,0 +1,12 @@
           1 +from pm_util import *
           2 +e=E()
           3 +seed=12
           4 +o=e.reset(seed); w,L,V=o[12:15]
           5 +for name,p,d in [("top x=0",[0,0.12],[0,-1]),("top x=.3",[0.3,0.12],[0,-1]),("stem side y=-.6",[0.08,-0.6],[-1,0]),("stem side y=-1.1",[0.08,-1.1],[-1,0]),("stem bottom",[0,-1.3],[0,1])]:
           6 +    mv,obs,a=run_push(e,seed,p,d,0.01,12)
           7 +    print(name,"navmv",mv)
           8 +    for i in range(1,len(obs)):
           9 +        b0=obs[i-1][0:3]; b1=obs[i][0:3]
          10 +        dl=R(b0[2]).T@(b1[0:2]-b0[0:2]); dth=b1[2]-b0[2]
          11 +        rl=R(b0[2]).T@(obs[i][16:18]-b0[0:2])
          12 +        print(f"  {i:2d} dloc={dl} dth={dth:+.5f} robot_loc_after={rl}")
diff --git a/e5.py b/e5.py
new file mode 100644
index 0000000..214ec1d
--- /dev/null
+++ b/e5.py
@@ -0,0 +1,18 @@
           1 +from pm_util import *
           2 +from geom import com_I
           3 +e=E(); seed=12
           4 +o=e.reset(seed); w,L,V=o[12:15]; c,k2=com_I(w,L,V); print("com",c,"k2",k2)
           5 +rows=[]
           6 +for name,p,d in [("top x=.3",[0.3,0.25],[0,-1]),("top x=-.45",[-0.45,0.25],[0,-1]),("barbot x=.4",[0.4,-0.35],[0,1]),("stem side y=-.6",[0.25,-0.6],[-1,0]),("stem side y=-1.1",[0.25,-1.1],[-1,0]),("stem side y=-.3",[-0.25,-0.3],[1,0]),("bar end",[0.8,-0.05],[-1,0])]:
           7 +    mv,obs,a=run_push(e,seed,p,d,0.01,25)
           8 +    i=len(obs)-1; b0=obs[i-1][0:3]; b1=obs[i][0:3]
           9 +    dl=R(b0[2]).T@(b1[0:2]-b0[0:2]); dth=b1[2]-b0[2]
          10 +    rl=R(b0[2]).T@(obs[i-1][16:18]-b0[0:2]); ul=R(b0[2]).T@a
          11 +    # sticking model: contact pt p (robot center projected ~) ; solve for impulse with unit mass
          12 +    for tag,pc in [("robotctr",rl),("surface",rl-0.0926*np.asarray(d,float)*-1*-1 if False else rl+0.0926*np.asarray(d,float)/np.linalg.norm(d))]:
          13 +        r=pc-c
          14 +        K=np.eye(2)+np.array([[r[1]**2,-r[0]*r[1]],[-r[0]*r[1],r[0]**2]])/k2
          15 +        J=np.linalg.solve(K,ul); vc=J; om=(r[0]*J[1]-r[1]*J[0])/k2
          16 +        vref=vc+om*np.array([c[1],-c[0]])*-1  # v_ref = v_com + om x (ref-com) ; ref-com=-c ; om x v = om*(-vy,vx)
          17 +        vref=vc+om*np.array([c[1],-c[0]])
          18 +        print(f"{name:16s} {tag:8s} meas dl={dl} dth={dth:+.5f} | pred dl={vref} dth={om:+.5f}  navmv={mv:.1e}")
diff --git a/e6.py b/e6.py
new file mode 100644
index 0000000..4b6ed55
--- /dev/null
+++ b/e6.py
@@ -0,0 +1,29 @@
           1 +from pm_util import *
           2 +from geom import com_I
           3 +def closest_pt(q,w,L,V):
           4 +    rects=[(-L/2,L/2,-w,0),(-w/2,w/2,-w-V,-w)]
           5 +    best=None
           6 +    for x0,x1,y0,y1 in rects:
           7 +        p=np.array([np.clip(q[0],x0,x1),np.clip(q[1],y0,y1)]); dd=np.linalg.norm(q-p)
           8 +        if best is None or dd<best[0]: best=(dd,p)
           9 +    return best
          10 +def stick_pred(pc,ul,c,k2):
          11 +    r=pc-c
          12 +    K=np.eye(2)+np.array([[r[1]**2,-r[0]*r[1]],[-r[0]*r[1],r[0]**2]])/k2
          13 +    J=np.linalg.solve(K,ul); om=(r[0]*J[1]-r[1]*J[0])/k2
          14 +    return J+om*np.array([c[1],-c[0]]), om
          15 +e=E(); seed=12
          16 +o=e.reset(seed); w,L,V=o[12:15]; c,k2=com_I(w,L,V)
          17 +for ang in [20,40,50,60]:
          18 +  for side in [1]:
          19 +    a=np.deg2rad(ang)*side
          20 +    d=[np.sin(a),-np.cos(a)]
          21 +    mv,obs,act=run_push(e,seed,[0-0.3*d[0],0.3],d,0.01,40)
          22 +    print(f"ang {ang*side:+d} navmv={mv:.1e}")
          23 +    for i in range(1,41,3):
          24 +        b0=obs[i-1][0:3]; b1=obs[i][0:3]
          25 +        dl=R(b0[2]).T@(b1[0:2]-b0[0:2]); dth=b1[2]-b0[2]
          26 +        rl=R(b0[2]).T@(obs[i-1][16:18]-b0[0:2]); ul=R(b0[2]).T@act
          27 +        dist,pc=closest_pt(rl,w,L,V)
          28 +        pd,po=stick_pred(pc,ul,c,k2) if dist<0.106 else (np.zeros(2),0)
          29 +        print(f"   {i} rob_loc={rl} dist={dist:.4f} meas dl={dl} dth={dth:+.5f} | stick pred dl={pd} dth={po:+.5f}")
diff --git a/e7.py b/e7.py
new file mode 100644
index 0000000..445b8ee
--- /dev/null
+++ b/e7.py
@@ -0,0 +1,13 @@
           1 +from pm_util import *
           2 +e=E(); seed=12
           3 +for s in [0.002,0.005,0.01,0.02,0.03,0.04,0.049]:
           4 +    for y0 in [0.2,0.2+s/3,0.2+2*s/3]:
           5 +        mv,obs,act=run_push(e,seed,[0,y0],[0,-1],s,int(0.2/s)+6)
           6 +        out=[]
           7 +        for i in range(1,len(obs)):
           8 +            b0=obs[i-1][0:3]; b1=obs[i][0:3]
           9 +            dl=R(b0[2]).T@(b1[0:2]-b0[0:2])
          10 +            g0=(R(b0[2]).T@(obs[i-1][16:18]-b0[0:2]))[1]
          11 +            g1=(R(b1[2]).T@(obs[i][16:18]-b1[0:2]))[1]
          12 +            if g0-s<0.1+s: out.append(f"({g0:.4f}->{g0-s:.4f}: d={-dl[1]:.5f} g1={g1:.5f})")
          13 +        print(s, " ".join(out[:5]))
diff --git a/e8.py b/e8.py
new file mode 100644
index 0000000..7b4a5ce
--- /dev/null
+++ b/e8.py
@@ -0,0 +1,18 @@
           1 +from pm_util import *
           2 +from geom import com_I
           3 +exec(open('e6.py').read().split('e=E()')[0].split('from geom import com_I')[1])
           4 +e=E(); seed=12
           5 +o=e.reset(seed); w,L,V=o[12:15]; c,k2=com_I(w,L,V)
           6 +for ang in [60,70,80,87]:
           7 +    a=np.deg2rad(ang); d=[np.sin(a),-np.cos(a)]
           8 +    # start so that we hit top at x ~ -0.2 after approach
           9 +    mv,obs,act=run_push(e,seed,[-0.35,0.1+0.2*np.cos(a)],d,0.01,30)
          10 +    print(f"ang {ang} navmv={mv:.1e}")
          11 +    for i in range(1,31,2):
          12 +        b0=obs[i-1][0:3]; b1=obs[i][0:3]
          13 +        dl=R(b0[2]).T@(b1[0:2]-b0[0:2]); dth=b1[2]-b0[2]
          14 +        rl=R(b0[2]).T@(obs[i-1][16:18]-b0[0:2]); ul=R(b0[2]).T@act
          15 +        dist,pc=closest_pt(rl,w,L,V)
          16 +        if dist>0.13: continue
          17 +        pd,po=stick_pred(pc,ul,c,k2)
          18 +        print(f"   {i} rob_loc={rl} dist={dist:.4f} meas dl={dl} dth={dth:+.5f} | stick dl={pd} dth={po:+.5f}")
diff --git a/e9.py b/e9.py
new file mode 100644
index 0000000..020cc6f
--- /dev/null
+++ b/e9.py
@@ -0,0 +1,13 @@
           1 +from pm_util import *
           2 +e=E()
           3 +o=e.reset(12); print("start robot",o[16:18],"block",o[0:3])
           4 +for d in [[-1,0],[0,-1],[1,0],[0,1]]:
           5 +    o=e.reset(12)
           6 +    # move away from block first: block at ~ (2.36,2.40); robot at (1.1,1.26)
           7 +    for i in range(150):
           8 +        o=e.step(np.array(d)*0.049)
           9 +    print(d,"robot",o[16:18],"block",o[0:3])
          10 +# go to corner (0,0) direction
          11 +o=e.reset(12)
          12 +for i in range(150): o=e.step(np.array([-0.049,-0.049]))
          13 +print("corner", o[16:18])
diff --git a/eval2.py b/eval2.py
new file mode 100644
index 0000000..673e995
--- /dev/null
+++ b/eval2.py
@@ -0,0 +1,19 @@
           1 +import numpy as np, glob
           2 +import push_model as pm
           3 +from eval_model import X,A,Y,moved
           4 +for mu in [0.9,1.0,1.1]:
           5 +    P=np.array([pm.predict(x,a,mu,0.265) for x,a in zip(X,A)])
           6 +    dp=np.linalg.norm(P[:,0:2]-Y[:,0:2],axis=1); dth=np.abs((P[:,2]-Y[:,2]+np.pi)%(2*np.pi)-np.pi)
           7 +    print(mu, "pos mean",dp[moved].mean(),"th mean",dth[moved].mean())
           8 +P=np.array([pm.predict(x,a,1.0,0.265) for x,a in zip(X,A)])
           9 +dp=np.linalg.norm(P[:,0:2]-Y[:,0:2],axis=1)
          10 +s=np.linalg.norm(A,axis=1)
          11 +rel=dp/np.maximum(np.linalg.norm(Y[:,0:2]-X[:,0:2],axis=1),1e-4)
          12 +for lo,hi in [(0,0.01),(0.01,0.02),(0.02,0.035),(0.035,0.08)]:
          13 +    m=moved&(s>=lo)&(s<hi); print(f"step {lo}-{hi}: n={m.sum()} pos err mean {dp[m].mean():.2e} rel median {np.median(rel[m]):.3f}")
          14 +idx=np.argsort(-dp)[:8]
          15 +np.set_printoptions(precision=4,suppress=True,linewidth=200)
          16 +for i in idx:
          17 +    th=X[i,2]; from push_model import _R
          18 +    q=_R(th).T@(X[i,16:18]+A[i]-X[i,0:2])
          19 +    print(i, "robot_local_new",q,"a_loc",_R(th).T@A[i],"meas",Y[i,0:3]-X[i,0:3],"pred",P[i]-X[i,0:3], "wlv",X[i,12:15])
diff --git a/eval_model.py b/eval_model.py
new file mode 100644
index 0000000..9b87547
--- /dev/null
+++ b/eval_model.py
@@ -0,0 +1,19 @@
           1 +import numpy as np, glob, sys
           2 +import push_model as pm
           3 +D=[np.load(f) for f in sorted(glob.glob("data_*.npz"))]
           4 +X=np.concatenate([d['X'] for d in D]);A=np.concatenate([d['A'] for d in D]);Y=np.concatenate([d['Y'] for d in D])
           5 +moved=np.abs(Y[:,0:3]-X[:,0:3]).max(1)>1e-9
           6 +def ev(mu,c,verbose=False):
           7 +    P=np.array([pm.predict(x,a,mu,c) for x,a in zip(X,A)])
           8 +    dp=np.linalg.norm(P[:,0:2]-Y[:,0:2],axis=1); dth=np.abs((P[:,2]-Y[:,2]+np.pi)%(2*np.pi)-np.pi)
           9 +    mag=np.linalg.norm(Y[:,0:2]-X[:,0:2],axis=1)
          10 +    if verbose:
          11 +        pm_=np.abs(P[:,0:3]-X[:,0:3]).max(1)>1e-9
          12 +        print(f"n={len(X)} moved={moved.sum()} pred-moved={pm_.sum()} contact-mismatch={(pm_!=moved).sum()}")
          13 +        print(f"pos err: mean {dp[moved].mean():.2e} p95 {np.percentile(dp[moved],95):.2e} max {dp.max():.2e}; mean |dpos| moved {mag[moved].mean():.2e}")
          14 +        print(f"th err: mean {dth[moved].mean():.2e} p95 {np.percentile(dth[moved],95):.2e} max {dth.max():.2e}")
          15 +    return dp.mean()+dth.mean()
          16 +if len(sys.argv)>1:
          17 +    for mu in [1.0,1.3,1.6,2.0,3.0,1e9]:
          18 +        print(mu, [round(ev(mu,c)*1e4,3) for c in [0.24,0.265,0.29]])
          19 +ev(pm.MU,pm.C_GAP,True)
diff --git a/eval_roll.py b/eval_roll.py
new file mode 100644
index 0000000..1fb7c97
--- /dev/null
+++ b/eval_roll.py
@@ -0,0 +1,17 @@
           1 +import numpy as np, push_model as pm
           2 +from eval_model import X,A,Y,moved
           3 +# segments
           4 +segs=[];cur=[0]
           5 +for i in range(1,len(X)):
           6 +    if np.allclose(X[i],Y[i-1]): cur.append(i)
           7 +    else: segs.append(cur);cur=[i]
           8 +segs.append(cur)
           9 +E=[];ET=[];M=[]
          10 +for sg in segs:
          11 +    x=X[sg[0]].copy()
          12 +    for i in sg:
          13 +        x[16:18]=X[i,16:18]; x[0:3]=pm.predict(x,A[i])
          14 +    E.append(np.linalg.norm(x[0:2]-Y[sg[-1],0:2])); ET.append(abs((x[2]-Y[sg[-1],2]+np.pi)%(2*np.pi)-np.pi))
          15 +    M.append(np.linalg.norm(Y[sg[-1],0:2]-X[sg[0],0:2]))
          16 +E=np.array(E);ET=np.array(ET);M=np.array(M)
          17 +print(f"{len(segs)} open-loop rollouts (~{len(X)/len(segs):.0f} steps): block travel mean {M.mean():.3f}; final pos err mean {E.mean():.4f} median {np.median(E):.4f} p90 {np.percentile(E,90):.4f}; theta err mean {ET.mean():.4f} median {np.median(ET):.4f}")
diff --git a/explore1.py b/explore1.py
new file mode 100644
index 0000000..2c88d65
--- /dev/null
+++ b/explore1.py
@@ -0,0 +1,13 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +env = make_env()
           4 +np.set_printoptions(precision=3, suppress=True, linewidth=200)
           5 +for s in range(5):
           6 +    obs,_ = env.reset(seed=s)
           7 +    print(s, obs[0:3], obs[12:16], "robot", obs[16:18], obs[28], "goal", obs[29:32])
           8 +obs,_ = env.reset(seed=0)
           9 +print(obs)
          10 +for i in range(5):
          11 +    obs,r,t,tr,info = env.step(np.array([0.049,0.0]))
          12 +    print(obs[16:21], r, t, tr, info)
          13 +env.close()
diff --git a/explore2.py b/explore2.py
new file mode 100644
index 0000000..ec0c572
--- /dev/null
+++ b/explore2.py
@@ -0,0 +1,26 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +env = make_env()
           4 +np.set_printoptions(precision=3, suppress=True, linewidth=200)
           5 +obs,_ = env.reset(seed=0)
           6 +def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
           7 +def goto(obs, p, tol=1e-3):
           8 +    for _ in range(200):
           9 +        d = p - obs[16:18]
          10 +        if np.linalg.norm(d)<tol: break
          11 +        a = np.clip(d,-0.049,0.049)
          12 +        obs,*_ = env.step(a)
          13 +    return obs
          14 +ref=obs[0:2]; th=obs[2]
          15 +start = ref + R(th)@np.array([-0.5,-0.5])
          16 +print("block",obs[0:6],"start",start)
          17 +obs=goto(obs,start)
          18 +print("after goto block",obs[0:6], "robot", obs[16:18])
          19 +dirn = R(th)@np.array([1.0,0])
          20 +for i in range(20):
          21 +    obs,*_=env.step(dirn*0.03)
          22 +    print(i,"blk",obs[0:6],"rob",obs[16:18])
          23 +for i in range(30):
          24 +    obs,*_=env.step(-dirn*0.0)
          25 +    print("coast",i,"blk",obs[0:6])
          26 +env.close()
diff --git a/gen_data.py b/gen_data.py
new file mode 100644
index 0000000..b0034b4
--- /dev/null
+++ b/gen_data.py
@@ -0,0 +1,33 @@
           1 +from pm_util import *
           2 +import sys
           3 +rng=np.random.default_rng(int(sys.argv[1])); N=int(sys.argv[2])
           4 +e=E(); X=[];A=[];Y=[]
           5 +seeds=[12,13,20,23,24,38,81,96,105,113,121,137,152,162]
           6 +for ep in range(N):
           7 +    seed=int(rng.choice(seeds)); o=e.reset(seed); w,L,V=o[12:15]
           8 +    # pick random point on T boundary
           9 +    if rng.random()<0.45:
          10 +        px=rng.uniform(-L/2,L/2); side=rng.choice(['top','bot','end'])
          11 +        if side=='top': p=np.array([px,0]); n=np.array([0,1.])
          12 +        elif side=='bot':
          13 +            px=rng.choice([-1,1])*rng.uniform(w/2+0.1,L/2); p=np.array([px,-w]); n=np.array([0,-1.])
          14 +        else: s=rng.choice([-1,1]); p=np.array([s*L/2,-rng.uniform(0,w)]); n=np.array([s,0.])
          15 +    else:
          16 +        side=rng.choice(['stem','bottom'])
          17 +        if side=='stem': s=rng.choice([-1,1]); p=np.array([s*w/2,-w-rng.uniform(0.1,V)]); n=np.array([s,0.])
          18 +        else: p=np.array([rng.uniform(-w/2,w/2),-w-V]); n=np.array([0,-1.])
          19 +    ang=rng.uniform(-1.3,1.3); dl=-(R(ang)@n)
          20 +    start=p+n*0.1-dl*rng.uniform(0.05,0.15)
          21 +    if np.linalg.norm(start-p)<0.1: continue
          22 +    mv=safe_goto_local(e,start)
          23 +    if mv>0: continue
          24 +    s=rng.uniform(0.003,0.049)
          25 +    dw=R(e.obs[2])@dl*s
          26 +    for i in range(int(0.25/s)+8):
          27 +        o0=e.obs.copy(); a=dw.copy()
          28 +        if rng.random()<0.3: a=a+rng.normal(0,0.3*s,2)
          29 +        a=np.clip(a,-0.049,0.049)
          30 +        o1=e.step(a).copy()
          31 +        X.append(o0);A.append(a);Y.append(o1)
          32 +np.savez(f"data_{sys.argv[1]}.npz",X=np.array(X),A=np.array(A),Y=np.array(Y))
          33 +print(len(X))
diff --git a/geom.py b/geom.py
new file mode 100644
index 0000000..dd074fb
--- /dev/null
+++ b/geom.py
@@ -0,0 +1,7 @@
           1 +import numpy as np
           2 +def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
           3 +def com_I(w,L,V):
           4 +    A1=L*w; A2=V*w; y1=-w/2; y2=-w-V/2
           5 +    yc=(A1*y1+A2*y2)/(A1+A2)
           6 +    I=A1*(L*L+w*w)/12+A1*(y1-yc)**2+A2*(V*V+w*w)/12+A2*(y2-yc)**2
           7 +    return np.array([0.0,yc]), I/(A1+A2)   # com local, k^2
diff --git a/pm_util.py b/pm_util.py
new file mode 100644
index 0000000..5b50d83
--- /dev/null
+++ b/pm_util.py
@@ -0,0 +1,59 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +np.set_printoptions(precision=5, suppress=True, linewidth=200)
           4 +def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
           5 +class E:
           6 +    def __init__(s): s.env=make_env()
           7 +    def reset(s,seed):
           8 +        s.obs,_=s.env.reset(seed=seed); return s.obs
           9 +    def step(s,a):
          10 +        a=np.clip(np.asarray(a,float),-0.049,0.049)
          11 +        s.obs,r,t,tr,info=s.env.step(a); return s.obs
          12 +    def goto(s,p,maxstep=0.049,tol=1e-9):
          13 +        for _ in range(2000):
          14 +            d=np.asarray(p)-s.obs[16:18]
          15 +            if np.linalg.norm(d)<tol: break
          16 +            n=np.abs(d).max()
          17 +            a=d if n<=maxstep else d*maxstep/n
          18 +            s.step(a)
          19 +        return s.obs
          20 +    def path(s,pts):
          21 +        b0=s.obs[0:3].copy()
          22 +        for p in pts: s.goto(p)
          23 +        return np.abs(s.obs[0:3]-b0).max()
          24 +
          25 +def safe_goto_local(e, pl, rad=1.7):
          26 +    """navigate robot to local point pl (block frame) by going around at radius rad"""
          27 +    o=e.obs; c=o[0:2]; th=o[2]
          28 +    target=c+R(th)@np.asarray(pl)
          29 +    b0=o[0:3].copy()
          30 +    rp=o[16:18]-c
          31 +    a0=np.arctan2(rp[1],rp[0]); tp=target-c; a1=np.arctan2(tp[1],tp[0])
          32 +    pts=[c+rad*np.array([np.cos(a0),np.sin(a0)])]
          33 +    da=(a1-a0+np.pi)%(2*np.pi)-np.pi
          34 +    for k in range(1,13): a=a0+da*k/12; pts.append(c+rad*np.array([np.cos(a),np.sin(a)]))
          35 +    pts.append(target)
          36 +    mv=e.path(pts)
          37 +    return mv
          38 +
          39 +def probe(e, seed, pl, dl, step=0.001, n=600):
          40 +    e.reset(seed); mv=safe_goto_local(e,pl)
          41 +    o=e.obs; b0=o[0:3].copy(); th=b0[2]; c=b0[0:2]
          42 +    dw=R(th)@np.asarray(dl,float); dw/=np.linalg.norm(dw)
          43 +    prev=R(th).T@(o[16:18]-c)
          44 +    for i in range(n):
          45 +        o=e.step(dw*step)
          46 +        if np.abs(o[0:3]-b0).max()>1e-9:
          47 +            return mv, prev, R(th).T@(o[16:18]-c), o[0:3]-b0
          48 +        prev=R(th).T@(o[16:18]-c)
          49 +    return mv,None,None,None
          50 +
          51 +def run_push(e, seed, pl, dl, step, n, pre_contact=True):
          52 +    """go to local pl, then move along local dir dl (fixed world dir) with given step for n steps. returns list of obs"""
          53 +    e.reset(seed); mv=safe_goto_local(e,pl)
          54 +    o=e.obs; th=o[2]
          55 +    dw=R(th)@np.asarray(dl,float); dw/=np.linalg.norm(dw)
          56 +    obs=[o.copy()]
          57 +    for i in range(n):
          58 +        obs.append(e.step(dw*step).copy())
          59 +    return mv,np.array(obs),dw*step
diff --git a/push_model.py b/push_model.py
new file mode 100644
index 0000000..6f95a34
--- /dev/null
+++ b/push_model.py
@@ -0,0 +1,100 @@
           1 +"""Empirical per-step push model for the T-block env (pure numpy).
           2 +
           3 +Geometry (block local frame, ref point = obs[0:2], theta = obs[2], world = R(theta) @ local + ref):
           4 +  bar  = [-L/2, L/2] x [-w, 0]           (ref = midpoint of the bar's TOP edge)
           5 +  stem = [-w/2, w/2] x [-(w+V), -w]      (w=obs[12], L=obs[13], V=obs[14])
           6 +  COM  = (0, yc), yc = (A1*(-w/2) + A2*(-w-V/2)) / (A1+A2), A1=L*w, A2=V*w  (uniform density)
           7 +  k2   = I/m of the union about COM.
           8 +Dynamics (robot radius r=obs[28], moves exactly by action a unless blocked by a wall):
           9 +  contact if dist(robot_new, T) < g* = r + C_GAP*a_n  (a_n = component of a into the surface)
          10 +  effective push u = a * clip((g* - dist)/a_n, 0, 1)   (partial on first-contact step)
          11 +  impulse at the surface point p with Coulomb friction MU (point sticks if inside cone):
          12 +     v_com = J, omega = cross(p-com, J)/k2, s.t. normal velocity of p equals u_n
          13 +  block rotates by omega about COM and COM translates by v_com.
          14 +"""
          15 +import numpy as np
          16 +
          17 +C_GAP = 0.265
          18 +MU = 1.0  # robot-block Coulomb friction (fitted; 0.9/1.1 are worse)
          19 +N_SUB = 2  # sub-steps per env step (small accuracy gain)
          20 +
          21 +
          22 +def _R(t):
          23 +    c, s = np.cos(t), np.sin(t)
          24 +    return np.array([[c, -s], [s, c]])
          25 +
          26 +
          27 +def geometry(obs):
          28 +    w, L, V = obs[12], obs[13], obs[14]
          29 +    A1, A2 = L * w, V * w
          30 +    y1, y2 = -w / 2, -w - V / 2
          31 +    yc = (A1 * y1 + A2 * y2) / (A1 + A2)
          32 +    I = A1 * (L * L + w * w) / 12 + A1 * (y1 - yc) ** 2 + A2 * (V * V + w * w) / 12 + A2 * (y2 - yc) ** 2
          33 +    rects = [(-L / 2, L / 2, -w, 0.0), (-w / 2, w / 2, -w - V, -w)]
          34 +    return rects, np.array([0.0, yc]), I / (A1 + A2)
          35 +
          36 +
          37 +def _closest(q, rects):
          38 +    """closest point on union boundary to external point q, distance, outward normal"""
          39 +    best = None
          40 +    for x0, x1, y0, y1 in rects:
          41 +        p = np.array([min(max(q[0], x0), x1), min(max(q[1], y0), y1)])
          42 +        d = np.linalg.norm(q - p)
          43 +        if best is None or d < best[1]:
          44 +            best = (p, d)
          45 +    p, d = best
          46 +    if d < 1e-12:  # q inside: fall back
          47 +        return p, d, np.array([0.0, 1.0])
          48 +    return p, d, (q - p) / d
          49 +
          50 +
          51 +def predict(obs, action, mu=None, c_gap=None, n_sub=None):
          52 +    """obs: 45-vector, action: robot delta (2,). returns new block (x, y, theta) in world."""
          53 +    n_sub = N_SUB if n_sub is None else n_sub
          54 +    c_gap = C_GAP if c_gap is None else c_gap
          55 +    x = np.array(obs, float)
          56 +    a = np.asarray(action, float)
          57 +    for _ in range(n_sub):
          58 +        b = _predict1(x, a / n_sub, mu, c_gap * n_sub)
          59 +        x[0:3] = b
          60 +        x[16:18] = x[16:18] + a / n_sub
          61 +    return x[0:3].copy()
          62 +
          63 +
          64 +def _predict1(obs, action, mu=None, c_gap=None):
          65 +    mu = MU if mu is None else mu
          66 +    c_gap = C_GAP if c_gap is None else c_gap
          67 +    obs = np.asarray(obs, float)
          68 +    a = np.asarray(action, float)
          69 +    pos, th = obs[0:2], obs[2]
          70 +    r = obs[28]
          71 +    rects, com, k2 = geometry(obs)
          72 +    Rt = _R(th)
          73 +    rob1 = obs[16:18] + a
          74 +    q = Rt.T @ (rob1 - pos)
          75 +    al = Rt.T @ a
          76 +    p, d, n = _closest(q, rects)
          77 +    a_n = -al @ n  # into-surface component of robot step
          78 +    gstar = r + c_gap * max(a_n, 0.0)
          79 +    if d >= gstar or a_n <= 1e-12:
          80 +        return np.array([pos[0], pos[1], th])
          81 +    frac = min((gstar - d) / a_n, 1.0)
          82 +    u = al * frac
          83 +    rc = p - com
          84 +    K = np.eye(2) + np.array([[rc[1] ** 2, -rc[0] * rc[1]], [-rc[0] * rc[1], rc[0] ** 2]]) / k2
          85 +    nin = -n
          86 +    t = np.array([-nin[1], nin[0]])
          87 +    J = np.linalg.solve(K, u)
          88 +    jn, jt = J @ nin, J @ t
          89 +    if abs(jt) > mu * jn:  # sliding
          90 +        dirJ = nin + mu * np.sign(jt) * t
          91 +        j = (u @ nin) / (nin @ (K @ dirJ))
          92 +        J = j * dirJ
          93 +    om = (rc[0] * J[1] - rc[1] * J[0]) / k2
          94 +    # rigid update: rotate by om about COM, translate COM by J (local frame of old pose)
          95 +    com_w = pos + Rt @ com
          96 +    com_w_new = com_w + Rt @ J
          97 +    th_new = th + om
          98 +    pos_new = com_w_new - _R(th_new) @ com
          99 +    th_new = (th_new + np.pi) % (2 * np.pi) - np.pi
         100 +    return np.array([pos_new[0], pos_new[1], th_new])
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..2f697a5
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,29 @@
           1 +import sys, time, numpy as np
           2 +from multiprocessing import Pool
           3 +from env_client import make_env
           4 +
           5 +def run(seed):
           6 +    from approach import GeneratedApproach
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    steps = 0; term = False
          13 +    for t in range(env.max_steps):
          14 +        a = ap.get_action(obs)
          15 +        obs, r, term, trunc, info = env.step(a)
          16 +        steps += 1
          17 +        if term or trunc: break
          18 +    g = obs[29:32]
          19 +    err = (abs(obs[0]-g[0]), abs(obs[1]-g[1]), abs((obs[2]-g[2]+np.pi)%(2*np.pi)-np.pi))
          20 +    env.close()
          21 +    return seed, bool(term), steps, time.time()-t0, err
          22 +
          23 +if __name__ == "__main__":
          24 +    a, b = int(sys.argv[1]), int(sys.argv[2])
          25 +    with Pool(8) as p:
          26 +        res = p.map(run, range(a, b))
          27 +    for s, ok, st, tt, err in res:
          28 +        print(s, ok, st, f"{tt:.1f}s", np.round(err, 3))
          29 +    print("success", sum(r[1] for r in res), "/", len(res), "mean steps", np.mean([r[2] for r in res]), "max time", max(r[3] for r in res))
```

</details>

<a id="C003"></a>
### C003 · parametrize

Commit `343f45d54e3112960cec0b2c8f18a1d140b33191`; parents: 006fef5a37b4db13517bb8777ab8772bc1e84118. Recorded author date: 2026-09-30T17:06:05+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0187](01_timeline.md#E0187): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_343f45d_approach.py) · [Exact all-file diff](evidence/diffs/C003_343f45d.diff)

[Previous saved controller snapshot](evidence/versions/C002_006fef5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a38e996..dd66245 100644
--- a/approach.py
+++ b/approach.py
@@ -119,6 +119,10 @@ class Model:
  119    119  
  120    120  
  121    121  class GeneratedApproach:
         122 +    W_TH = 0.35
         123 +    STEP_PEN = 0.0015
         124 +    KMAX = 30
         125 +    NAV_OVER = 3.0
  122    126      def __init__(self, action_space, observation_space, primitives):
  123    127          self.action_space = action_space
  124    128          self.rng = np.random.default_rng(0)
@@ -169,7 +173,7 @@ class GeneratedApproach:
  169    173          ex = pos[..., 0] - self.goal[0]
  170    174          ey = pos[..., 1] - self.goal[1]
  171    175          et = _wrap(th - self.goal[2])
  172        -        return np.sqrt(ex ** 2 + ey ** 2) + 0.35 * np.abs(et)
         176 +        return np.sqrt(ex ** 2 + ey ** 2) + self.W_TH * np.abs(et)
  173    177  
  174    178      def _solved(self, pos, th):
  175    179          return (abs(pos[0] - self.goal[0]) < 0.03 and abs(pos[1] - self.goal[1]) < 0.03
@@ -211,13 +215,13 @@ class GeneratedApproach:
  211    215          starts, dirs = starts[ok], dirs[ok]
  212    216          # navigation cost estimate
  213    217          nav = np.linalg.norm(starts - rob0, axis=1) / AMAX
  214        -        nav = nav * 1.3 + np.where(nav > 1e-6, 3.0, 0.0)
         218 +        nav = nav * 1.3 + np.where(nav > 1e-6, self.NAV_OVER, 0.0)
  215    219          cost0 = float(self._cost(pos0, th0))
  216    220          err_pos = np.linalg.norm(pos0 - self.goal[:2])
  217    221          err_th = abs(_wrap(th0 - self.goal[2]))
  218    222          steps_opts = [AMAX, 0.02, 0.008]
  219    223          best = None
  220        -        KMAX = 30
         224 +        KMAX = self.KMAX
  221    225          tight0 = float(self._cost_tight(pos0, th0))
  222    226          for ss in steps_opts:
  223    227              N = len(starts)
@@ -243,7 +247,7 @@ class GeneratedApproach:
  243    247                  cst = self._cost(pos, th)
  244    248                  tc = self._cost_tight(pos, th)
  245    249                  total = nav + k
  246        -                score = cst + 0.0015 * total + np.where(tc < 1.0, -1.0, 0.0) * 0
         250 +                score = cst + self.STEP_PEN * total + np.where(tc < 1.0, -1.0, 0.0) * 0
  247    251                  score = np.where(tc < 0.8, -10.0 + 0.001 * total, score)
  248    252                  score = np.where(alive, score, np.inf)
  249    253                  i = int(np.argmin(score))
diff --git a/tune.py b/tune.py
new file mode 100644
index 0000000..db76e1d
--- /dev/null
+++ b/tune.py
@@ -0,0 +1,10 @@
           1 +import sys, json, numpy as np
           2 +from multiprocessing import Pool
           3 +import test_approach as T
           4 +import approach
           5 +params = json.loads(sys.argv[1]); a,b = int(sys.argv[2]), int(sys.argv[3])
           6 +def run(seed):
           7 +    for k,v in params.items(): setattr(approach.GeneratedApproach, k, v)
           8 +    return T.run(seed)
           9 +with Pool(10) as p: res = p.map(run, range(a,b))
          10 +print(params, "succ", sum(r[1] for r in res), "/", len(res), "mean steps", np.mean([r[2] for r in res]), "maxt %.1f"%max(r[3] for r in res))
```

</details>

<a id="C004"></a>
### C004 · Fix goal angle: env compares theta raw (unwrapped); target clipped interval

Commit `4e9e8249367063ed06943b2ba7bdaec568adde22`; parents: 343f45d54e3112960cec0b2c8f18a1d140b33191. Recorded author date: 2026-09-30T17:14:10+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0239](01_timeline.md#E0239): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_4e9e824_approach.py) · [Exact all-file diff](evidence/diffs/C004_4e9e824.diff)

[Previous saved controller snapshot](evidence/versions/C003_343f45d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index dd66245..99272e5 100644
--- a/approach.py
+++ b/approach.py
@@ -131,6 +131,12 @@ class GeneratedApproach:
  131    131      def reset(self, state, info):
  132    132          self.model = Model(state)
  133    133          self.goal = np.array(state[29:32], float)
         134 +        # env compares theta WITHOUT wrapping: allowed raw interval clipped to [-pi, pi)
         135 +        tol = np.deg2rad(8)
         136 +        lo = max(self.goal[2] - tol, -np.pi + 0.005)
         137 +        hi = min(self.goal[2] + tol, np.pi - 0.005)
         138 +        self.goal[2] = 0.5 * (lo + hi)
         139 +        self.th_tol = 0.5 * (hi - lo)
  134    140          self.plan = []  # list of actions
  135    141          self.expect_block = None
  136    142          self.nsteps = 0
@@ -177,12 +183,12 @@ class GeneratedApproach:
  177    183  
  178    184      def _solved(self, pos, th):
  179    185          return (abs(pos[0] - self.goal[0]) < 0.03 and abs(pos[1] - self.goal[1]) < 0.03
  180        -                and abs(_wrap(th - self.goal[2])) < np.deg2rad(8))
         186 +                and abs(_wrap(th - self.goal[2])) < self.th_tol)
  181    187  
  182    188      def _cost_tight(self, pos, th):
  183    189          ex = np.abs(pos[..., 0] - self.goal[0]) / 0.03
  184    190          ey = np.abs(pos[..., 1] - self.goal[1]) / 0.03
  185        -        et = np.abs(_wrap(th - self.goal[2])) / np.deg2rad(8)
         191 +        et = np.abs(_wrap(th - self.goal[2])) / self.th_tol
  186    192          return np.maximum(np.maximum(ex, ey), et)
  187    193  
  188    194      def _plan_push(self, obs):
diff --git a/collect_term.py b/collect_term.py
new file mode 100644
index 0000000..bd7ae06
--- /dev/null
+++ b/collect_term.py
@@ -0,0 +1,15 @@
           1 +import sys, numpy as np
           2 +from multiprocessing import Pool
           3 +from env_client import make_env
           4 +import approach
           5 +def run(seed):
           6 +    env=make_env(); obs,info=env.reset(seed=seed)
           7 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
           8 +    rows=[]
           9 +    for t in range(400):
          10 +        a=ap.get_action(obs); obs,r,term,trunc,_=env.step(a)
          11 +        rows.append(np.concatenate([obs,[float(term)]]))
          12 +        if term: break
          13 +    env.close(); return np.array(rows)
          14 +with Pool(10) as p: res=p.map(run, range(300,340))
          15 +np.save("term_data.npy", np.concatenate(res))
diff --git a/fit_term.py b/fit_term.py
new file mode 100644
index 0000000..1192e5b
--- /dev/null
+++ b/fit_term.py
@@ -0,0 +1,19 @@
           1 +import numpy as np
           2 +from approach import geometry, _wrap
           3 +D=np.load("term_data.npy"); term=D[:,-1]>0.5
           4 +def pt(o, local):
           5 +    c,s=np.cos(o[2]),np.sin(o[2]); return o[0:2]+np.array([c*local[0]-s*local[1], s*local[0]+c*local[1]])
           6 +for name in ["ref","com","barcenter","bbox"]:
           7 +    ok=[]
           8 +    for o in D:
           9 +        rects,com,k2=geometry(o); w,L,V=o[12],o[13],o[14]
          10 +        loc={"ref":(0,0),"com":tuple(com),"barcenter":(0,-w/2),"bbox":(0,-(w+V)/2)}[name]
          11 +        p=pt(o[0:3],loc); g=pt(o[29:32],loc)
          12 +        e=np.abs(p-g); et=abs(_wrap(o[2]-o[31]))
          13 +        ok.append((e[0]<0.03)&(e[1]<0.03)&(et<np.deg2rad(8)))
          14 +    ok=np.array(ok)
          15 +    print(name, "agree", (ok==term).mean(), "pred_T_actual_F", (ok&~term).sum(), "pred_F_actual_T", (~ok&term).sum(), "nterm", term.sum())
          16 +E=np.stack([np.abs(D[:,0]-D[:,29]),np.abs(D[:,1]-D[:,30]),np.abs(_wrap(D[:,2]-D[:,31]))],1)
          17 +okref=(E[:,0]<0.03)&(E[:,1]<0.03)&(E[:,2]<np.deg2rad(8))
          18 +print("terminated errs max", E[term].max(0), "\n", np.round(E[term][:10],4))
          19 +print("ref-ok not term errs min", E[okref&~term].min(0)); print(np.round(E[okref&~term][::20],4))
diff --git a/seq_term.py b/seq_term.py
new file mode 100644
index 0000000..949fc81
--- /dev/null
+++ b/seq_term.py
@@ -0,0 +1,25 @@
           1 +import numpy as np
           2 +from approach import Model, _wrap
           3 +D=np.load("term_data.npy"); term=D[:,-1]>0.5
           4 +E=np.stack([np.abs(D[:,0]-D[:,29]),np.abs(D[:,1]-D[:,30]),np.abs(_wrap(D[:,2]-D[:,31]))],1)
           5 +okref=(E[:,0]<0.03)&(E[:,1]<0.03)&(E[:,2]<np.deg2rad(8))
           6 +# episode boundaries: goal change
           7 +ep=np.concatenate([[0],np.cumsum(np.any(np.abs(np.diff(D[:,29:32],axis=0))>1e-9,axis=1))])
           8 +for e in range(8):
           9 +    idx=np.where(ep==e)[0]
          10 +    first=idx[okref[idx]]
          11 +    if len(first)==0: continue
          12 +    i0=first[0]
          13 +    for i in range(max(idx[0],i0-2), min(idx[-1]+1, i0+6)):
          14 +        m=Model(D[i]); d=m.world_dist(D[i][None,0:2],np.array([D[i][2]]),D[i][None,16:18])[0]
          15 +        print(e,i-idx[0],np.round(E[i],4),okref[i],term[i],"robdist %.3f"%d, "blkmove", np.round(D[i,0:3]-D[i-1,0:3],4))
          16 +    print()
          17 +print("stuck candidates")
          18 +for e in range(ep.max()+1):
          19 +    idx=np.where(ep==e)[0]
          20 +    if not term[idx].any():
          21 +        i=idx[-1]; print(e, D[i,0:3], D[i,29:32])
          22 +# raw theta check
          23 +raw=np.abs(D[:,2]-D[:,31])
          24 +prev_ok=np.concatenate([[False],okref[:-1]])
          25 +print("term & raw>8deg:", (term & (np.concatenate([[9],raw[:-1]])>np.deg2rad(8))).sum())
diff --git a/term_data.npy b/term_data.npy
new file mode 100644
index 0000000..2157de8
Binary files /dev/null and b/term_data.npy differ
diff --git a/trace.py b/trace.py
new file mode 100644
index 0000000..185f1b3
--- /dev/null
+++ b/trace.py
@@ -0,0 +1,17 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +seed=int(sys.argv[1])
           5 +params = eval(sys.argv[2]) if len(sys.argv)>2 else {}
           6 +for k,v in params.items(): setattr(approach.GeneratedApproach,k,v)
           7 +env=make_env(); obs,info=env.reset(seed=seed)
           8 +ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
           9 +orig=ap._plan_push
          10 +def pp(o):
          11 +    b,c0=orig(o)
          12 +    g=ap.goal; print(f"t={ap.nsteps} blk=({o[0]-g[0]:+.3f},{o[1]-g[1]:+.3f},{approach._wrap(o[2]-g[2]):+.3f}) cost={c0:.3f} -> pred {b[4]:.3f} k={b[3]} step={np.linalg.norm(b[2]):.3f} navdist={np.linalg.norm(b[1]-o[16:18]):.2f}")
          13 +    return b,c0
          14 +ap._plan_push=pp
          15 +for t in range(1000):
          16 +    a=ap.get_action(obs); obs,r,term,trunc,_=env.step(a)
          17 +    if term: print("done",t+1); break
diff --git a/tune.py b/tune.py
index db76e1d..6501e09 100644
--- a/tune.py
+++ b/tune.py
@@ -8,3 +8,5 @@ def run(seed):
    8      8      return T.run(seed)
    9      9  with Pool(10) as p: res = p.map(run, range(a,b))
   10     10  print(params, "succ", sum(r[1] for r in res), "/", len(res), "mean steps", np.mean([r[2] for r in res]), "maxt %.1f"%max(r[3] for r in res))
          11 +for r in res:
          12 +    if not r[1] or r[3]>20 or r[2]>250: print("  bad", r[0], r[2], "%.1f"%r[3], np.round(r[4],3))
```

</details>

<a id="C005"></a>
### C005 · Two-stage lookahead planner

Commit `6fb871aa422ceaab6507657339f2d673bdaceeff`; parents: 4e9e8249367063ed06943b2ba7bdaec568adde22. Recorded author date: 2026-09-30T17:15:44+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0255](01_timeline.md#E0255): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_6fb871a_approach.py) · [Exact all-file diff](evidence/diffs/C005_6fb871a.diff)

[Previous saved controller snapshot](evidence/versions/C004_4e9e824_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 99272e5..362499c 100644
--- a/approach.py
+++ b/approach.py
@@ -123,6 +123,7 @@ class GeneratedApproach:
  123    123      STEP_PEN = 0.0015
  124    124      KMAX = 30
  125    125      NAV_OVER = 3.0
         126 +    LOOK = 10
  126    127      def __init__(self, action_space, observation_space, primitives):
  127    128          self.action_space = action_space
  128    129          self.rng = np.random.default_rng(0)
@@ -191,52 +192,49 @@ class GeneratedApproach:
  191    192          et = np.abs(_wrap(th - self.goal[2])) / self.th_tol
  192    193          return np.maximum(np.maximum(ex, ey), et)
  193    194  
  194        -    def _plan_push(self, obs):
         195 +    def _rollout(self, pos0, th0, rob0, steps_opts=None):
         196 +        """Evaluate all candidate pushes from block pose (pos0, th0), robot rob0.
         197 +        Returns dict of arrays over (candidate x stepsize): score, start, a, k, pos, th, rob, cost."""
  195    198          m = self.model
  196        -        pos0 = np.array(obs[0:2], float)
  197        -        th0 = float(obs[2])
  198        -        rob0 = np.array(obs[16:18], float)
  199    199          c, s = math.cos(th0), math.sin(th0)
  200    200          Rm = np.array([[c, -s], [s, c]])
  201    201          r = m.r
  202        -        cands_start, cands_dir = [], []
  203        -        # world contact points + normals
  204    202          pw = self.c_pts @ Rm.T + pos0
  205    203          nw = self.c_nrm @ Rm.T
  206    204          start = pw + nw * (r + 0.03)
  207    205          ca, sa = np.cos(self.c_ang), np.sin(self.c_ang)
  208    206          nin = -nw
  209    207          dirs = np.stack([ca * nin[:, 0] - sa * nin[:, 1], sa * nin[:, 0] + ca * nin[:, 1]], 1)
  210        -        # also: continue from current robot position in a set of directions
  211    208          cur_d = np.linspace(-np.pi, np.pi, 24, endpoint=False)
  212    209          cstart = np.repeat(rob0[None], len(cur_d), 0)
  213    210          cdirs = np.stack([np.cos(cur_d), np.sin(cur_d)], 1)
  214    211          starts = np.concatenate([start, cstart])
  215    212          dirs = np.concatenate([dirs, cdirs])
  216        -        # validity of starts
  217    213          ok = (starts[:, 0] >= LO + 0.01) & (starts[:, 0] <= HI - 0.01) & \
  218    214               (starts[:, 1] >= LO + 0.01) & (starts[:, 1] <= HI - 0.01)
  219    215          dstart = m.world_dist(np.repeat(pos0[None], len(starts), 0), np.full(len(starts), th0), starts)
  220    216          ok &= (dstart > r + 0.02) | (np.arange(len(starts)) >= len(start))
  221    217          starts, dirs = starts[ok], dirs[ok]
  222        -        # navigation cost estimate
  223    218          nav = np.linalg.norm(starts - rob0, axis=1) / AMAX
  224    219          nav = nav * 1.3 + np.where(nav > 1e-6, self.NAV_OVER, 0.0)
  225        -        cost0 = float(self._cost(pos0, th0))
  226        -        err_pos = np.linalg.norm(pos0 - self.goal[:2])
  227        -        err_th = abs(_wrap(th0 - self.goal[2]))
  228        -        steps_opts = [AMAX, 0.02, 0.008]
  229        -        best = None
  230        -        KMAX = self.KMAX
  231        -        tight0 = float(self._cost_tight(pos0, th0))
  232        -        for ss in steps_opts:
  233        -            N = len(starts)
         220 +        steps_opts = steps_opts or [AMAX, 0.02, 0.008]
         221 +        N = len(starts)
         222 +        S = len(steps_opts)
         223 +        out_score = np.full((S, N), np.inf)
         224 +        out_k = np.zeros((S, N), int)
         225 +        out_pos = np.zeros((S, N, 2))
         226 +        out_th = np.zeros((S, N))
         227 +        out_rob = np.zeros((S, N, 2))
         228 +        out_cost = np.zeros((S, N))
         229 +        out_a = np.zeros((S, N, 2))
         230 +        for si, ss in enumerate(steps_opts):
  234    231              pos = np.repeat(pos0[None], N, 0)
  235    232              th = np.full(N, th0)
  236    233              rob = starts.copy()
  237    234              a = dirs * ss
         235 +            out_a[si] = a
  238    236              alive = np.ones(N, bool)
  239        -            for k in range(1, KMAX + 1):
         237 +            for k in range(1, self.KMAX + 1):
  240    238                  nrob = rob + a
  241    239                  inb = (nrob[:, 0] >= LO) & (nrob[:, 0] <= HI) & (nrob[:, 1] >= LO) & (nrob[:, 1] <= HI)
  242    240                  alive &= inb
@@ -244,7 +242,6 @@ class GeneratedApproach:
  244    242                  pos = np.where(alive[:, None], pos_n, pos)
  245    243                  th = np.where(alive, th_n, th)
  246    244                  rob = np.where(alive[:, None], nrob, rob)
  247        -                # block corners within walls
  248    245                  cc, sc = np.cos(th), np.sin(th)
  249    246                  cx = pos[:, 0:1] + cc[:, None] * m.corners[None, :, 0] - sc[:, None] * m.corners[None, :, 1]
  250    247                  cy = pos[:, 1:2] + sc[:, None] * m.corners[None, :, 0] + cc[:, None] * m.corners[None, :, 1]
@@ -253,12 +250,55 @@ class GeneratedApproach:
  253    250                  cst = self._cost(pos, th)
  254    251                  tc = self._cost_tight(pos, th)
  255    252                  total = nav + k
  256        -                score = cst + self.STEP_PEN * total + np.where(tc < 1.0, -1.0, 0.0) * 0
         253 +                score = cst + self.STEP_PEN * total
  257    254                  score = np.where(tc < 0.8, -10.0 + 0.001 * total, score)
  258    255                  score = np.where(alive, score, np.inf)
  259        -                i = int(np.argmin(score))
  260        -                if best is None or score[i] < best[0]:
  261        -                    best = (float(score[i]), starts[i].copy(), a[i].copy(), k, float(cst[i]))
         256 +                better = score < out_score[si]
         257 +                if better.any():
         258 +                    out_score[si] = np.where(better, score, out_score[si])
         259 +                    out_k[si] = np.where(better, k, out_k[si])
         260 +                    out_pos[si] = np.where(better[:, None], pos, out_pos[si])
         261 +                    out_th[si] = np.where(better, th, out_th[si])
         262 +                    out_rob[si] = np.where(better[:, None], rob, out_rob[si])
         263 +                    out_cost[si] = np.where(better, cst, out_cost[si])
         264 +                if not alive.any():
         265 +                    break
         266 +        return dict(score=out_score.ravel(), k=out_k.ravel(), pos=out_pos.reshape(-1, 2),
         267 +                    th=out_th.ravel(), rob=out_rob.reshape(-1, 2), cost=out_cost.ravel(),
         268 +                    a=out_a.reshape(-1, 2), start=np.tile(starts, (S, 1)),
         269 +                    nav=np.tile(nav, S))
         270 +
         271 +    def _plan_push(self, obs):
         272 +        pos0 = np.array(obs[0:2], float)
         273 +        th0 = float(obs[2])
         274 +        rob0 = np.array(obs[16:18], float)
         275 +        cost0 = float(self._cost(pos0, th0))
         276 +        R1 = self._rollout(pos0, th0, rob0)
         277 +        order = np.argsort(R1["score"])
         278 +        i0 = int(order[0])
         279 +        best_i = i0
         280 +        if R1["score"][i0] > -5 and self.LOOK > 0:
         281 +            # two-stage lookahead over top-M first pushes (distinct-ish)
         282 +            cand = []
         283 +            for i in order:
         284 +                if not np.isfinite(R1["score"][i]):
         285 +                    break
         286 +                if all(np.abs(R1["pos"][i] - R1["pos"][j]).max() > 0.01 or
         287 +                       abs(R1["th"][i] - R1["th"][j]) > 0.02 for j in cand):
         288 +                    cand.append(int(i))
         289 +                if len(cand) >= self.LOOK:
         290 +                    break
         291 +            best_tot = np.inf
         292 +            for i in cand:
         293 +                steps1 = R1["nav"][i] + R1["k"][i]
         294 +                R2 = self._rollout(R1["pos"][i], float(R1["th"][i]), R1["rob"][i], [AMAX, 0.02])
         295 +                s2 = min(float(R2["score"].min()), R1["score"][i] - self.STEP_PEN * steps1)
         296 +                tot = s2 + self.STEP_PEN * steps1
         297 +                if tot < best_tot:
         298 +                    best_tot, best_i = tot, i
         299 +        i = best_i
         300 +        best = (float(R1["score"][i]), R1["start"][i].copy(), R1["a"][i].copy(), int(R1["k"][i]),
         301 +                float(R1["cost"][i]))
  262    302          return best, cost0
  263    303  
  264    304      # ------------------------------------------------------------------
diff --git a/new_plan.py b/new_plan.py
new file mode 100644
index 0000000..74d7d75
--- /dev/null
+++ b/new_plan.py
@@ -0,0 +1,108 @@
           1 +    def _rollout(self, pos0, th0, rob0, steps_opts=None):
           2 +        """Evaluate all candidate pushes from block pose (pos0, th0), robot rob0.
           3 +        Returns dict of arrays over (candidate x stepsize): score, start, a, k, pos, th, rob, cost."""
           4 +        m = self.model
           5 +        c, s = math.cos(th0), math.sin(th0)
           6 +        Rm = np.array([[c, -s], [s, c]])
           7 +        r = m.r
           8 +        pw = self.c_pts @ Rm.T + pos0
           9 +        nw = self.c_nrm @ Rm.T
          10 +        start = pw + nw * (r + 0.03)
          11 +        ca, sa = np.cos(self.c_ang), np.sin(self.c_ang)
          12 +        nin = -nw
          13 +        dirs = np.stack([ca * nin[:, 0] - sa * nin[:, 1], sa * nin[:, 0] + ca * nin[:, 1]], 1)
          14 +        cur_d = np.linspace(-np.pi, np.pi, 24, endpoint=False)
          15 +        cstart = np.repeat(rob0[None], len(cur_d), 0)
          16 +        cdirs = np.stack([np.cos(cur_d), np.sin(cur_d)], 1)
          17 +        starts = np.concatenate([start, cstart])
          18 +        dirs = np.concatenate([dirs, cdirs])
          19 +        ok = (starts[:, 0] >= LO + 0.01) & (starts[:, 0] <= HI - 0.01) & \
          20 +             (starts[:, 1] >= LO + 0.01) & (starts[:, 1] <= HI - 0.01)
          21 +        dstart = m.world_dist(np.repeat(pos0[None], len(starts), 0), np.full(len(starts), th0), starts)
          22 +        ok &= (dstart > r + 0.02) | (np.arange(len(starts)) >= len(start))
          23 +        starts, dirs = starts[ok], dirs[ok]
          24 +        nav = np.linalg.norm(starts - rob0, axis=1) / AMAX
          25 +        nav = nav * 1.3 + np.where(nav > 1e-6, self.NAV_OVER, 0.0)
          26 +        steps_opts = steps_opts or [AMAX, 0.02, 0.008]
          27 +        N = len(starts)
          28 +        S = len(steps_opts)
          29 +        out_score = np.full((S, N), np.inf)
          30 +        out_k = np.zeros((S, N), int)
          31 +        out_pos = np.zeros((S, N, 2))
          32 +        out_th = np.zeros((S, N))
          33 +        out_rob = np.zeros((S, N, 2))
          34 +        out_cost = np.zeros((S, N))
          35 +        out_a = np.zeros((S, N, 2))
          36 +        for si, ss in enumerate(steps_opts):
          37 +            pos = np.repeat(pos0[None], N, 0)
          38 +            th = np.full(N, th0)
          39 +            rob = starts.copy()
          40 +            a = dirs * ss
          41 +            out_a[si] = a
          42 +            alive = np.ones(N, bool)
          43 +            for k in range(1, self.KMAX + 1):
          44 +                nrob = rob + a
          45 +                inb = (nrob[:, 0] >= LO) & (nrob[:, 0] <= HI) & (nrob[:, 1] >= LO) & (nrob[:, 1] <= HI)
          46 +                alive &= inb
          47 +                pos_n, th_n = m.step(pos, th, rob, a)
          48 +                pos = np.where(alive[:, None], pos_n, pos)
          49 +                th = np.where(alive, th_n, th)
          50 +                rob = np.where(alive[:, None], nrob, rob)
          51 +                cc, sc = np.cos(th), np.sin(th)
          52 +                cx = pos[:, 0:1] + cc[:, None] * m.corners[None, :, 0] - sc[:, None] * m.corners[None, :, 1]
          53 +                cy = pos[:, 1:2] + sc[:, None] * m.corners[None, :, 0] + cc[:, None] * m.corners[None, :, 1]
          54 +                wall = (cx.min(1) < 0.02) | (cx.max(1) > 4.98) | (cy.min(1) < 0.02) | (cy.max(1) > 4.98)
          55 +                alive &= ~wall
          56 +                cst = self._cost(pos, th)
          57 +                tc = self._cost_tight(pos, th)
          58 +                total = nav + k
          59 +                score = cst + self.STEP_PEN * total
          60 +                score = np.where(tc < 0.8, -10.0 + 0.001 * total, score)
          61 +                score = np.where(alive, score, np.inf)
          62 +                better = score < out_score[si]
          63 +                if better.any():
          64 +                    out_score[si] = np.where(better, score, out_score[si])
          65 +                    out_k[si] = np.where(better, k, out_k[si])
          66 +                    out_pos[si] = np.where(better[:, None], pos, out_pos[si])
          67 +                    out_th[si] = np.where(better, th, out_th[si])
          68 +                    out_rob[si] = np.where(better[:, None], rob, out_rob[si])
          69 +                    out_cost[si] = np.where(better, cst, out_cost[si])
          70 +                if not alive.any():
          71 +                    break
          72 +        return dict(score=out_score.ravel(), k=out_k.ravel(), pos=out_pos.reshape(-1, 2),
          73 +                    th=out_th.ravel(), rob=out_rob.reshape(-1, 2), cost=out_cost.ravel(),
          74 +                    a=out_a.reshape(-1, 2), start=np.tile(starts, (S, 1)),
          75 +                    nav=np.tile(nav, S))
          76 +
          77 +    def _plan_push(self, obs):
          78 +        pos0 = np.array(obs[0:2], float)
          79 +        th0 = float(obs[2])
          80 +        rob0 = np.array(obs[16:18], float)
          81 +        cost0 = float(self._cost(pos0, th0))
          82 +        R1 = self._rollout(pos0, th0, rob0)
          83 +        order = np.argsort(R1["score"])
          84 +        i0 = int(order[0])
          85 +        best_i = i0
          86 +        if R1["score"][i0] > -5 and self.LOOK > 0:
          87 +            # two-stage lookahead over top-M first pushes (distinct-ish)
          88 +            cand = []
          89 +            for i in order:
          90 +                if not np.isfinite(R1["score"][i]):
          91 +                    break
          92 +                if all(np.abs(R1["pos"][i] - R1["pos"][j]).max() > 0.01 or
          93 +                       abs(R1["th"][i] - R1["th"][j]) > 0.02 for j in cand):
          94 +                    cand.append(int(i))
          95 +                if len(cand) >= self.LOOK:
          96 +                    break
          97 +            best_tot = np.inf
          98 +            for i in cand:
          99 +                steps1 = R1["nav"][i] + R1["k"][i]
         100 +                R2 = self._rollout(R1["pos"][i], float(R1["th"][i]), R1["rob"][i], [AMAX, 0.02])
         101 +                s2 = min(float(R2["score"].min()), R1["score"][i] - self.STEP_PEN * steps1)
         102 +                tot = s2 + self.STEP_PEN * steps1
         103 +                if tot < best_tot:
         104 +                    best_tot, best_i = tot, i
         105 +        i = best_i
         106 +        best = (float(R1["score"][i]), R1["start"][i].copy(), R1["a"][i].copy(), int(R1["k"][i]),
         107 +                float(R1["cost"][i]))
         108 +        return best, cost0
diff --git a/timing.py b/timing.py
new file mode 100644
index 0000000..87fde82
--- /dev/null
+++ b/timing.py
@@ -0,0 +1,9 @@
           1 +import time, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +env=make_env(); obs,info=env.reset(seed=5)
           5 +ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
           6 +t=time.time(); b=ap._plan_push(obs); print("plan", time.time()-t)
           7 +t=time.time(); a=ap._navigate(obs,b[0][1]); print("nav", time.time()-t, len(a))
           8 +t=time.time(); p=ap._astar(obs[16:18], b[0][1], obs[0:2], obs[2], 0.115); print("astar", time.time()-t)
           9 +print("ncand", len(ap.c_pts))
```

</details>

<a id="C006"></a>
### C006 · Grid Dijkstra nav cost + nav paths

Commit `214da58f5c2a5031116f3f4d2b9af7e0995690c2`; parents: 6fb871aa422ceaab6507657339f2d673bdaceeff. Recorded author date: 2026-09-30T17:19:31+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0282](01_timeline.md#E0282): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_214da58_approach.py) · [Exact all-file diff](evidence/diffs/C006_214da58.diff)

[Previous saved controller snapshot](evidence/versions/C005_6fb871a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 362499c..caa8a81 100644
--- a/approach.py
+++ b/approach.py
@@ -10,6 +10,8 @@ import math
   10     10  
   11     11  import numpy as np
   12     12  
          13 +from navgrid import NavGrid
          14 +
   13     15  C_GAP = 0.265
   14     16  MU = 1.0
   15     17  LO, HI = 0.1, 4.9  # robot centre bounds
@@ -124,6 +126,7 @@ class GeneratedApproach:
  124    126      KMAX = 30
  125    127      NAV_OVER = 3.0
  126    128      LOOK = 10
         129 +    GRIDNAV = True
  127    130      def __init__(self, action_space, observation_space, primitives):
  128    131          self.action_space = action_space
  129    132          self.rng = np.random.default_rng(0)
@@ -215,8 +218,17 @@ class GeneratedApproach:
  215    218          dstart = m.world_dist(np.repeat(pos0[None], len(starts), 0), np.full(len(starts), th0), starts)
  216    219          ok &= (dstart > r + 0.02) | (np.arange(len(starts)) >= len(start))
  217    220          starts, dirs = starts[ok], dirs[ok]
  218        -        nav = np.linalg.norm(starts - rob0, axis=1) / AMAX
  219        -        nav = nav * 1.3 + np.where(nav > 1e-6, self.NAV_OVER, 0.0)
         221 +        eu = np.linalg.norm(starts - rob0, axis=1)
         222 +        if self.GRIDNAV:
         223 +            g = NavGrid(m, pos0, th0, r + 0.015)
         224 +            src, dist, _ = g.from_source(rob0)
         225 +            gd = g.dist_to(dist, starts, rob0)
         226 +            gd = np.where(np.isfinite(gd), gd, eu * 3 + 1.0)
         227 +            pl = np.maximum(eu, gd * 0.97)
         228 +        else:
         229 +            pl = eu * 1.3
         230 +        nav = pl / AMAX
         231 +        nav = nav + np.where(eu > 1e-6, self.NAV_OVER, 0.0)
  220    232          steps_opts = steps_opts or [AMAX, 0.02, 0.008]
  221    233          N = len(starts)
  222    234          S = len(steps_opts)
@@ -322,7 +334,7 @@ class GeneratedApproach:
  322    334          if seg_clear(rob, target):
  323    335              path = [rob, target]
  324    336          else:
  325        -            path = self._astar(rob, target, pos0, th0, clear)
         337 +            path = self._gridpath(rob, target, pos0, th0, clear)
  326    338              if path is None:
  327    339                  path = [rob, target]
  328    340          acts = []
@@ -342,6 +354,32 @@ class GeneratedApproach:
  342    354                  break
  343    355          return acts
  344    356  
         357 +    def _gridpath(self, start, goal, pos0, th0, clear):
         358 +        m = self.model
         359 +        g = NavGrid(m, pos0, th0, clear + 0.005)
         360 +        src, dist, pred = g.from_source(start)
         361 +        dst = g.nearest_free(goal)
         362 +        cells = g.path(pred, src, dst)
         363 +        if cells is None:
         364 +            return None
         365 +        raw = [np.array(start)] + [c for c in cells] + [np.array(goal)]
         366 +
         367 +        def seg_ok(p, q):
         368 +            k = max(2, int(np.linalg.norm(q - p) / 0.01) + 1)
         369 +            f = np.linspace(0, 1, k)[:, None]
         370 +            pp = p * (1 - f) + q * f
         371 +            dd = m.world_dist(np.repeat(pos0[None], k, 0), np.full(k, th0), pp)
         372 +            return bool(np.all(dd >= clear))
         373 +        out = [raw[0]]
         374 +        i = 0
         375 +        while i < len(raw) - 1:
         376 +            j = len(raw) - 1
         377 +            while j > i + 1 and not seg_ok(raw[i], raw[j]):
         378 +                j -= 1
         379 +            out.append(raw[j])
         380 +            i = j
         381 +        return out
         382 +
  345    383      def _astar(self, start, goal, pos0, th0, clear):
  346    384          m = self.model
  347    385          res = 0.04
diff --git a/breakdown.py b/breakdown.py
new file mode 100644
index 0000000..0193c3a
--- /dev/null
+++ b/breakdown.py
@@ -0,0 +1,29 @@
           1 +import numpy as np
           2 +from multiprocessing import Pool
           3 +from env_client import make_env
           4 +import approach
           5 +def run(seed):
           6 +    env=make_env(); obs,info=env.reset(seed=seed)
           7 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
           8 +    nav=0; push={}; plans=0; orig=ap._plan_push
           9 +    def pp(o):
          10 +        nonlocal plans; plans+=1; return orig(o)
          11 +    ap._plan_push=pp
          12 +    for t in range(1000):
          13 +        navmode = ap.nav_len>0 if hasattr(ap,'nav_len') and ap.plan else None
          14 +        a=ap.get_action(obs)
          15 +        if ap.nav_len>0 or (len(ap.plan)>0 and False): pass
          16 +        obs2,r,term,trunc,_=env.step(a)
          17 +        moved = np.abs(obs2[0:3]-obs[0:3]).max()>1e-6
          18 +        if moved: 
          19 +            k=round(float(np.abs(a).max()),3); push[k]=push.get(k,0)+1
          20 +        else: nav+=1
          21 +        obs=obs2
          22 +        if term: break
          23 +    return t+1, nav, push, plans
          24 +with Pool(10) as p: res=p.map(run, range(200,240))
          25 +print("mean steps", np.mean([r[0] for r in res]), "nav(no block motion)", np.mean([r[1] for r in res]), "plans", np.mean([r[3] for r in res]))
          26 +tot={}
          27 +for r in res:
          28 +    for k,v in r[2].items(): tot[k]=tot.get(k,0)+v/len(res)
          29 +print(sorted(tot.items(), key=lambda x:-x[1])[:10])
diff --git a/navgrid.py b/navgrid.py
new file mode 100644
index 0000000..cb80815
--- /dev/null
+++ b/navgrid.py
@@ -0,0 +1,76 @@
           1 +"""Grid shortest-path distances around the T-block (scipy csgraph Dijkstra)."""
           2 +import numpy as np
           3 +from scipy.sparse import csr_matrix
           4 +from scipy.sparse.csgraph import dijkstra
           5 +
           6 +LO, HI = 0.1, 4.9
           7 +RES = 0.05
           8 +NG = int(round((HI - LO) / RES)) + 1
           9 +_xs = LO + np.arange(NG) * RES
          10 +_X, _Y = np.meshgrid(_xs, _xs, indexing="ij")
          11 +PTS = np.stack([_X.ravel(), _Y.ravel()], 1)
          12 +_idx = np.arange(NG * NG).reshape(NG, NG)
          13 +_E = []
          14 +for di, dj, w in [(1, 0, 1.0), (0, 1, 1.0), (1, 1, 2 ** 0.5), (1, -1, 2 ** 0.5)]:
          15 +    a = _idx[max(0, -di):NG - max(0, di), max(0, -dj):NG - max(0, dj)]
          16 +    b = _idx[max(0, di):NG - max(0, -di) if max(0, -di) else NG, max(0, dj):NG - max(0, -dj) if max(0, -dj) else NG]
          17 +    _E.append((a.ravel(), b.ravel(), w))
          18 +EA = np.concatenate([e[0] for e in _E])
          19 +EB = np.concatenate([e[1] for e in _E])
          20 +EW = np.concatenate([np.full(len(e[0]), e[2]) for e in _E]) * RES
          21 +
          22 +
          23 +def cell_of(p):
          24 +    i = np.clip(np.round((np.asarray(p)[..., 0] - LO) / RES).astype(int), 0, NG - 1)
          25 +    j = np.clip(np.round((np.asarray(p)[..., 1] - LO) / RES).astype(int), 0, NG - 1)
          26 +    return i * NG + j
          27 +
          28 +
          29 +class NavGrid:
          30 +    def __init__(self, model, pos, th, clear):
          31 +        d = model.world_dist(np.repeat(np.asarray(pos)[None], len(PTS), 0), np.full(len(PTS), th), PTS)
          32 +        self.free = d >= clear
          33 +        m = self.free[EA] & self.free[EB]
          34 +        a, b, w = EA[m], EB[m], EW[m]
          35 +        self.G = csr_matrix((np.concatenate([w, w]), (np.concatenate([a, b]), np.concatenate([b, a]))),
          36 +                            shape=(NG * NG, NG * NG))
          37 +
          38 +    def nearest_free(self, p):
          39 +        c = int(cell_of(p))
          40 +        if self.free[c]:
          41 +            return c
          42 +        fi = np.flatnonzero(self.free)
          43 +        dd = ((PTS[fi] - np.asarray(p)) ** 2).sum(1)
          44 +        return int(fi[np.argmin(dd)])
          45 +
          46 +    def from_source(self, p):
          47 +        src = self.nearest_free(p)
          48 +        dist, pred = dijkstra(self.G, directed=False, indices=src, return_predecessors=True)
          49 +        return src, dist, pred
          50 +
          51 +    def dist_to(self, dist, pts, src_p):
          52 +        """path length estimates from source to each of pts (N,2)."""
          53 +        c = cell_of(pts)
          54 +        base = dist[c]
          55 +        # fallback: pts in non-free cells -> look at 3x3 neighbourhood
          56 +        bad = ~np.isfinite(base) | ~self.free[c]
          57 +        if bad.any():
          58 +            ci, cj = c // NG, c % NG
          59 +            best = np.full(len(c), np.inf)
          60 +            for di in (-2, -1, 0, 1, 2):
          61 +                for dj in (-2, -1, 0, 1, 2):
          62 +                    ii = np.clip(ci + di, 0, NG - 1)
          63 +                    jj = np.clip(cj + dj, 0, NG - 1)
          64 +                    cc = ii * NG + jj
          65 +                    val = np.where(self.free[cc], dist[cc] + np.linalg.norm(PTS[cc] - pts, axis=1), np.inf)
          66 +                    best = np.minimum(best, val)
          67 +            base = np.where(bad, best, base)
          68 +        return base + np.linalg.norm(pts - PTS[c], axis=1) * 0.0
          69 +
          70 +    def path(self, pred, src, dst):
          71 +        cells = [dst]
          72 +        while cells[-1] != src and cells[-1] >= 0:
          73 +            cells.append(pred[cells[-1]])
          74 +        if cells[-1] != src:
          75 +            return None
          76 +        return PTS[np.array(cells[::-1])]
diff --git a/t_nav.py b/t_nav.py
new file mode 100644
index 0000000..17c203f
--- /dev/null
+++ b/t_nav.py
@@ -0,0 +1,7 @@
           1 +import time, numpy as np
           2 +from env_client import make_env
           3 +import approach, navgrid
           4 +env=make_env(); obs,_=env.reset(seed=5)
           5 +m=approach.Model(obs)
           6 +t=time.time(); g=navgrid.NavGrid(m,obs[0:2],obs[2],0.115); src,d,pr=g.from_source(obs[16:18]); print("t",time.time()-t)
           7 +print(np.isfinite(d).sum(), g.free.sum(), d[navgrid.cell_of(obs[0:2]+np.array([0,0.4]))])
```

</details>

<a id="C007"></a>
### C007 · curved push option

Commit `8284b125f4c7dc18b01a7f672e93fc2b0fd8d5a7`; parents: 214da58f5c2a5031116f3f4d2b9af7e0995690c2. Recorded author date: 2026-09-30T17:21:01+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0299](01_timeline.md#E0299): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_8284b12_approach.py) · [Exact all-file diff](evidence/diffs/C007_8284b12.diff)

[Previous saved controller snapshot](evidence/versions/C006_214da58_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index caa8a81..031ef40 100644
--- a/approach.py
+++ b/approach.py
@@ -127,6 +127,7 @@ class GeneratedApproach:
  127    127      NAV_OVER = 3.0
  128    128      LOOK = 10
  129    129      GRIDNAV = True
         130 +    CURVS = (0.0,)
  130    131      def __init__(self, action_space, observation_space, primitives):
  131    132          self.action_space = action_space
  132    133          self.rng = np.random.default_rng(0)
@@ -195,7 +196,7 @@ class GeneratedApproach:
  195    196          et = np.abs(_wrap(th - self.goal[2])) / self.th_tol
  196    197          return np.maximum(np.maximum(ex, ey), et)
  197    198  
  198        -    def _rollout(self, pos0, th0, rob0, steps_opts=None):
         199 +    def _rollout(self, pos0, th0, rob0, steps_opts=None, curvs=(0.0,)):
  199    200          """Evaluate all candidate pushes from block pose (pos0, th0), robot rob0.
  200    201          Returns dict of arrays over (candidate x stepsize): score, start, a, k, pos, th, rob, cost."""
  201    202          m = self.model
@@ -218,6 +219,11 @@ class GeneratedApproach:
  218    219          dstart = m.world_dist(np.repeat(pos0[None], len(starts), 0), np.full(len(starts), th0), starts)
  219    220          ok &= (dstart > r + 0.02) | (np.arange(len(starts)) >= len(start))
  220    221          starts, dirs = starts[ok], dirs[ok]
         222 +        nc = len(curvs)
         223 +        starts = np.tile(starts, (nc, 1))
         224 +        dirs = np.tile(dirs, (nc, 1))
         225 +        kap = np.repeat(np.asarray(curvs, float), len(starts) // nc)
         226 +        ck, sk = np.cos(kap), np.sin(kap)
  221    227          eu = np.linalg.norm(starts - rob0, axis=1)
  222    228          if self.GRIDNAV:
  223    229              g = NavGrid(m, pos0, th0, r + 0.015)
@@ -246,7 +252,10 @@ class GeneratedApproach:
  246    252              a = dirs * ss
  247    253              out_a[si] = a
  248    254              alive = np.ones(N, bool)
         255 +            a = a.copy()
  249    256              for k in range(1, self.KMAX + 1):
         257 +                if k > 1 and nc > 1:
         258 +                    a = np.stack([ck * a[:, 0] - sk * a[:, 1], sk * a[:, 0] + ck * a[:, 1]], 1)
  250    259                  nrob = rob + a
  251    260                  inb = (nrob[:, 0] >= LO) & (nrob[:, 0] <= HI) & (nrob[:, 1] >= LO) & (nrob[:, 1] <= HI)
  252    261                  alive &= inb
@@ -277,7 +286,7 @@ class GeneratedApproach:
  277    286                      break
  278    287          return dict(score=out_score.ravel(), k=out_k.ravel(), pos=out_pos.reshape(-1, 2),
  279    288                      th=out_th.ravel(), rob=out_rob.reshape(-1, 2), cost=out_cost.ravel(),
  280        -                    a=out_a.reshape(-1, 2), start=np.tile(starts, (S, 1)),
         289 +                    a=out_a.reshape(-1, 2), start=np.tile(starts, (S, 1)), kap=np.tile(kap, S),
  281    290                      nav=np.tile(nav, S))
  282    291  
  283    292      def _plan_push(self, obs):
@@ -285,7 +294,7 @@ class GeneratedApproach:
  285    294          th0 = float(obs[2])
  286    295          rob0 = np.array(obs[16:18], float)
  287    296          cost0 = float(self._cost(pos0, th0))
  288        -        R1 = self._rollout(pos0, th0, rob0)
         297 +        R1 = self._rollout(pos0, th0, rob0, curvs=self.CURVS)
  289    298          order = np.argsort(R1["score"])
  290    299          i0 = int(order[0])
  291    300          best_i = i0
@@ -310,7 +319,7 @@ class GeneratedApproach:
  310    319                      best_tot, best_i = tot, i
  311    320          i = best_i
  312    321          best = (float(R1["score"][i]), R1["start"][i].copy(), R1["a"][i].copy(), int(R1["k"][i]),
  313        -                float(R1["cost"][i]))
         322 +                float(R1["cost"][i]), float(R1["kap"][i]))
  314    323          return best, cost0
  315    324  
  316    325      # ------------------------------------------------------------------
@@ -467,11 +476,18 @@ class GeneratedApproach:
  467    476              best, cost0 = self._plan_push(obs)
  468    477              if best is None:
  469    478                  return np.zeros(2)
  470        -            _, start, a, k, cst = best
         479 +            _, start, a, k, cst, kap = best
  471    480              acts = self._navigate(obs, start) if np.linalg.norm(start - obs[16:18]) > 1e-9 else []
  472    481              self.expect_block = obs[0:3].copy()
  473    482              self.nav_len = len(acts)
  474        -            self.plan = acts + [a.copy() for _ in range(k)]
         483 +            pushes = []
         484 +            ck, sk = math.cos(kap), math.sin(kap)
         485 +            a = a.copy()
         486 +            for j in range(k):
         487 +                if j > 0:
         488 +                    a = np.array([ck * a[0] - sk * a[1], sk * a[0] + ck * a[1]])
         489 +                pushes.append(a.copy())
         490 +            self.plan = acts + pushes
  475    491          act = self.plan.pop(0)
  476    492          if self.nav_len > 0:
  477    493              self.nav_len -= 1
diff --git a/breakdown2.py b/breakdown2.py
new file mode 100644
index 0000000..acfe59f
--- /dev/null
+++ b/breakdown2.py
@@ -0,0 +1,23 @@
           1 +import numpy as np, sys, json
           2 +from multiprocessing import Pool
           3 +from env_client import make_env
           4 +import approach
           5 +params=json.loads(sys.argv[1]) if len(sys.argv)>1 else {}
           6 +def run(seed):
           7 +    for k,v in params.items(): setattr(approach.GeneratedApproach,k,v)
           8 +    env=make_env(); obs,info=env.reset(seed=seed)
           9 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
          10 +    first=None; nav=0; push=0; small=0
          11 +    for t in range(1000):
          12 +        a=ap.get_action(obs)
          13 +        obs2,r,term,trunc,_=env.step(a)
          14 +        moved = np.abs(obs2[0:3]-obs[0:3]).max()>1e-6
          15 +        if moved and first is None: first=t
          16 +        if moved:
          17 +            push+=1; small += np.abs(a).max()<0.03
          18 +        else: nav+=1
          19 +        obs=obs2
          20 +        if term: break
          21 +    return t+1, first, nav-first, push, small
          22 +with Pool(10) as p: res=np.array(p.map(run, range(200,260)))
          23 +print(params, "steps %.1f initial_nav %.1f later_nav %.1f push %.1f smallpush %.1f"%tuple(res.mean(0)))
```

</details>

<a id="C008"></a>
### C008 · stage2 curvs param

Commit `5e42bbdd7d1f6b0145589d6e9f4f8ca5ddaa6ec1`; parents: 8284b125f4c7dc18b01a7f672e93fc2b0fd8d5a7. Recorded author date: 2026-09-30T17:22:12+02:00.

File roles (automatic): policy.

- [E0306](01_timeline.md#E0306): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_5e42bbd_approach.py) · [Exact all-file diff](evidence/diffs/C008_5e42bbd.diff)

[Previous saved controller snapshot](evidence/versions/C007_8284b12_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 031ef40..1be8c16 100644
--- a/approach.py
+++ b/approach.py
@@ -128,6 +128,7 @@ class GeneratedApproach:
  128    128      LOOK = 10
  129    129      GRIDNAV = True
  130    130      CURVS = (0.0,)
         131 +    CURVS2 = (0.0,)
  131    132      def __init__(self, action_space, observation_space, primitives):
  132    133          self.action_space = action_space
  133    134          self.rng = np.random.default_rng(0)
@@ -312,7 +313,7 @@ class GeneratedApproach:
  312    313              best_tot = np.inf
  313    314              for i in cand:
  314    315                  steps1 = R1["nav"][i] + R1["k"][i]
  315        -                R2 = self._rollout(R1["pos"][i], float(R1["th"][i]), R1["rob"][i], [AMAX, 0.02])
         316 +                R2 = self._rollout(R1["pos"][i], float(R1["th"][i]), R1["rob"][i], [AMAX, 0.02], curvs=self.CURVS2)
  316    317                  s2 = min(float(R2["score"].min()), R1["score"][i] - self.STEP_PEN * steps1)
  317    318                  tot = s2 + self.STEP_PEN * steps1
  318    319                  if tot < best_tot:
```

</details>

<a id="C009"></a>
### C009 · defaults: curved pushes, LOOK 15

Commit `6bd49cfd2abdad1690e6c61fba63a11fd4f97f43`; parents: 5e42bbdd7d1f6b0145589d6e9f4f8ca5ddaa6ec1. Recorded author date: 2026-09-30T17:23:05+02:00.

File roles (automatic): policy.

- [E0315](01_timeline.md#E0315): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_6bd49cf_approach.py) · [Exact all-file diff](evidence/diffs/C009_6bd49cf.diff)

[Previous saved controller snapshot](evidence/versions/C008_5e42bbd_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1be8c16..245b3ab 100644
--- a/approach.py
+++ b/approach.py
@@ -125,10 +125,10 @@ class GeneratedApproach:
  125    125      STEP_PEN = 0.0015
  126    126      KMAX = 30
  127    127      NAV_OVER = 3.0
  128        -    LOOK = 10
         128 +    LOOK = 15
  129    129      GRIDNAV = True
  130        -    CURVS = (0.0,)
  131        -    CURVS2 = (0.0,)
         130 +    CURVS = (0.0, 0.02, -0.02, 0.06, -0.06)
         131 +    CURVS2 = (0.0, 0.04, -0.04)
  132    132      def __init__(self, action_space, observation_space, primitives):
  133    133          self.action_space = action_space
  134    134          self.rng = np.random.default_rng(0)
```

</details>

<a id="C010"></a>
### C010 · time guard + stagnation fallback

Commit `7734cf0921e1c361d3537833232ee09cbf06c451`; parents: 6bd49cfd2abdad1690e6c61fba63a11fd4f97f43. Recorded author date: 2026-09-30T17:25:17+02:00.

File roles (automatic): policy.

- [E0397](01_timeline.md#E0397): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_7734cf0_approach.py) · [Exact all-file diff](evidence/diffs/C010_7734cf0.diff)

[Previous saved controller snapshot](evidence/versions/C009_6bd49cf_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 245b3ab..f027227 100644
--- a/approach.py
+++ b/approach.py
@@ -7,6 +7,7 @@ points on the T boundary x push directions x step sizes, roll out, choose best
    7      7  """
    8      8  import heapq
    9      9  import math
          10 +import time
   10     11  
   11     12  import numpy as np
   12     13  
@@ -146,6 +147,13 @@ class GeneratedApproach:
  146    147          self.plan = []  # list of actions
  147    148          self.expect_block = None
  148    149          self.nsteps = 0
         150 +        self.t_used = 0.0
         151 +        self.last_move_step = 0
         152 +        self.prev_block = np.array(state[0:3], float)
         153 +        self.cls = type(self)
         154 +        self.LOOK = self.cls.LOOK
         155 +        self.CURVS = self.cls.CURVS
         156 +        self.CURVS2 = self.cls.CURVS2
  149    157          self._build_candidates(state)
  150    158  
  151    159      def _build_candidates(self, obs):
@@ -465,8 +473,35 @@ class GeneratedApproach:
  465    473  
  466    474      # ------------------------------------------------------------------
  467    475      def get_action(self, state):
         476 +        t0 = time.time()
         477 +        try:
         478 +            return self._get_action(state)
         479 +        finally:
         480 +            self.t_used += time.time() - t0
         481 +
         482 +    def _get_action(self, state):
  468    483          obs = np.asarray(state, float)
  469    484          self.nsteps += 1
         485 +        if np.abs(obs[0:3] - self.prev_block).max() > 1e-6:
         486 +            self.last_move_step = self.nsteps
         487 +        self.prev_block = obs[0:3].copy()
         488 +        # time guard: degrade planner if running slow
         489 +        if self.t_used > 30.0:
         490 +            self.LOOK = 0
         491 +            self.CURVS = (0.0,)
         492 +        elif self.t_used > 20.0:
         493 +            self.LOOK = 4
         494 +            self.CURVS = (0.0, 0.04, -0.04)
         495 +        if self.t_used > 50.0:
         496 +            return np.clip(self.plan.pop(0), -AMAX, AMAX) if self.plan else np.zeros(2)
         497 +        # stagnation fallback: random push if block hasn't moved for a while
         498 +        if self.nsteps - self.last_move_step > 80 and not self.plan:
         499 +            self.last_move_step = self.nsteps
         500 +            ang = self.rng.uniform(-np.pi, np.pi)
         501 +            d = np.array([math.cos(ang), math.sin(ang)]) * AMAX
         502 +            self.plan = [d] * 10
         503 +            self.nav_len = 0
         504 +            self.expect_block = None
  470    505          pos = obs[0:3]
  471    506          if self.plan and self.expect_block is not None:
  472    507              # replan if block moved unexpectedly during navigation
```

</details>

<a id="C011"></a>
### C011 · TC_THR param

Commit `cbb89235844112d3b2072ebf48704bf4d1897739`; parents: 7734cf0921e1c361d3537833232ee09cbf06c451. Recorded author date: 2026-09-30T17:25:52+02:00.

File roles (automatic): policy.

- [E0406](01_timeline.md#E0406): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_cbb8923_approach.py) · [Exact all-file diff](evidence/diffs/C011_cbb8923.diff)

[Previous saved controller snapshot](evidence/versions/C010_7734cf0_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f027227..cd24a8f 100644
--- a/approach.py
+++ b/approach.py
@@ -127,6 +127,7 @@ class GeneratedApproach:
  127    127      KMAX = 30
  128    128      NAV_OVER = 3.0
  129    129      LOOK = 15
         130 +    TC_THR = 0.8
  130    131      GRIDNAV = True
  131    132      CURVS = (0.0, 0.02, -0.02, 0.06, -0.06)
  132    133      CURVS2 = (0.0, 0.04, -0.04)
@@ -281,7 +282,7 @@ class GeneratedApproach:
  281    282                  tc = self._cost_tight(pos, th)
  282    283                  total = nav + k
  283    284                  score = cst + self.STEP_PEN * total
  284        -                score = np.where(tc < 0.8, -10.0 + 0.001 * total, score)
         285 +                score = np.where(tc < self.TC_THR, -10.0 + 0.001 * total, score)
  285    286                  score = np.where(alive, score, np.inf)
  286    287                  better = score < out_score[si]
  287    288                  if better.any():
```

</details>

