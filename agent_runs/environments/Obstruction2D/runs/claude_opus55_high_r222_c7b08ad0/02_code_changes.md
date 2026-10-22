# Obstruction2D · claude-opus-5-5 · replicate 222: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `351ecfc` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `0b8ce0f` | Initial state-machine approach: clear obstructions, place target | approach.py, exp1.py, exp2.py, probe.py, test_approach.py | [E0028](01_timeline.md#E0028) |
| [C003](#C003) · `5372949` | Jointly choose grasp offset and placement for target (reach near world edge) | approach.py, dbg.py | [E0052](01_timeline.md#E0052) |
| [C004](#C004) · `bd5eeb7` | Fix motion deadlock, grasp/release on arrival step | approach.py, dbg.py, test_approach.py | [E0125](01_timeline.md#E0125) |
| [C005](#C005) · `332cf94` | Cost-based drop-spot selection (can drop in air), target bottom offset 0.018 | approach.py | [E0141](01_timeline.md#E0141) |
| [C006](#C006) · `d18ea75` | Step-cost based target placement choice | approach.py | [E0169](01_timeline.md#E0169) |
| [C007](#C007) · `ab5c4ba` | Simulated step estimator for costs | approach.py, dbg2.py | [E0192](01_timeline.md#E0192) |
| [C008](#C008) · `634fc60` | Keep gripper away from other objects while vacuum on (vacuum grabs within ~0.015) | approach.py, big_test.txt, dbg3.py, exp3.py | [E0253](01_timeline.md#E0253) |
| [C009](#C009) · `3d23ca4` | Fix premature grasp when arm not yet extended | approach.py | [E0284](01_timeline.md#E0284) |
| [C010](#C010) · `8dc1a43` | Resolve grasp blockers (remove neighbors preventing top-down grasp first) | approach.py, big_test.txt | [E0309](01_timeline.md#E0309) |
| [C011](#C011) · `cb4c8c6` | Drop spots must not block other grasps or target placement | approach.py, big_test.txt | [E0340](01_timeline.md#E0340) |
| [C012](#C012) · `f4dbcae` | Grasp overhang, spread grasp offsets by x, drop-spot check keeps target placement feasible | approach.py, big_test2.txt, dbg4.py, exp4.py | [E0399](01_timeline.md#E0399) |
| [C013](#C013) · `2e88eb5` | Drop-spot search over grasp offsets incl. approach cost; bottom offset 0.021 | approach.py, big_test2.txt, big_test3.txt, test_approach.py | [E0471](01_timeline.md#E0471) |
| [C014](#C014) · `deae307` | grasp_eps 0.007 | approach.py, prof.out, prof.py, test_approach.py | [E0502](01_timeline.md#E0502) |
| [C015](#C015) · `3bd283d` | keep VM 0.025; add analysis scripts | big_test4.txt, cnt.py | [E0626](01_timeline.md#E0626) |
| [C016](#C016) · `0ce0924` | Drop-spot: next-leg to next blocker, margins merged with penalty | approach.py, test_approach.py | [E0667](01_timeline.md#E0667) |
| [C017](#C017) · `320dd7d` | Time guard in drop-spot search | approach.py, prof.out, test_approach.py | [E0697](01_timeline.md#E0697) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `351ecfc2ba8cfe8b1bd1d8427f2cfee4c70f5ad1`; parents: none (initial snapshot). Recorded author date: 2026-09-30T12:15:53+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_351ecfc.diff)

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
index 0000000..d11f8f3
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "2c01dd627858952dd53667cfaead1aeb", "observation_space": {"type": "ObjectCentric", "types": [{"name": "crv_robot", "parent": null, "features": ["x", "y", "theta", "base_radius", "arm_joint", "arm_length", "vacuum", "gripper_height", "gripper_width"]}, {"name": "kinematic2d", "parent": null, "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order"]}, {"name": "circle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "radius"]}, {"name": "double_rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height", "x1", "y1", "theta1", "width1", "height1", "z_order1", "color_r1", "color_g1", "color_b1"]}, {"name": "lobject", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "length_side1", "length_side2"]}, {"name": "rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_block", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_surface", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}]}, "action_space": {"type": "Box", "shape": [5], "low": [-0.05000000074505806, -0.05000000074505806, -0.19634954631328583, -0.10000000149011612, 0.0], "high": [0.05000000074505806, 0.05000000074505806, 0.19634954631328583, 0.10000000149011612, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Initial state-machine approach: clear obstructions, place target

Commit `0b8ce0f860cecdd4c82fbc03a0a60655df38a04e`; parents: 351ecfc2ba8cfe8b1bd1d8427f2cfee4c70f5ad1. Recorded author date: 2026-09-30T12:19:27+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0028](01_timeline.md#E0028): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_0b8ce0f_approach.py) · [Exact all-file diff](evidence/diffs/C002_0b8ce0f.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..6841ad0
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,350 @@
           1 +import numpy as np
           2 +
           3 +WORLD_X = (0.0, 1.618)
           4 +WORLD_Y = (0.0, 1.0)
           5 +MAXD = 0.05
           6 +ARM_MAX = 0.2
           7 +
           8 +
           9 +class GeneratedApproach:
          10 +    def __init__(self, action_space, observation_space, primitives):
          11 +        self.action_space = action_space
          12 +        self.observation_space = observation_space
          13 +        self.low = np.array(action_space.low, dtype=np.float32)
          14 +        self.high = np.array(action_space.high, dtype=np.float32)
          15 +
          16 +    # ------------------------------------------------------------------ utils
          17 +    def _parse(self, state):
          18 +        robot = None
          19 +        rects = {}
          20 +        for name in state.get_object_names():
          21 +            obj = state.get_object_from_name(name)
          22 +            tname = obj.type.name
          23 +            if tname == 'crv_robot':
          24 +                robot = obj
          25 +                continue
          26 +            try:
          27 +                d = dict(x=float(state.get(obj, 'x')), y=float(state.get(obj, 'y')),
          28 +                         w=float(state.get(obj, 'width')), h=float(state.get(obj, 'height')),
          29 +                         theta=float(state.get(obj, 'theta')), type=tname, name=name)
          30 +            except Exception:
          31 +                continue
          32 +            # axis aligned bounding box (x,y is a corner, rotation about it)
          33 +            c, s = np.cos(d['theta']), np.sin(d['theta'])
          34 +            pts = np.array([[0, 0], [d['w'], 0], [d['w'], d['h']], [0, d['h']]])
          35 +            rot = pts @ np.array([[c, s], [-s, c]])
          36 +            d['x0'] = d['x'] + rot[:, 0].min()
          37 +            d['x1'] = d['x'] + rot[:, 0].max()
          38 +            d['y0'] = d['y'] + rot[:, 1].min()
          39 +            d['y1'] = d['y'] + rot[:, 1].max()
          40 +            rects[name] = d
          41 +        r = dict(x=float(state.get(robot, 'x')), y=float(state.get(robot, 'y')),
          42 +                 theta=float(state.get(robot, 'theta')),
          43 +                 R=float(state.get(robot, 'base_radius')),
          44 +                 aj=float(state.get(robot, 'arm_joint')),
          45 +                 al=float(state.get(robot, 'arm_length')),
          46 +                 vac=float(state.get(robot, 'vacuum')),
          47 +                 gh=float(state.get(robot, 'gripper_height')),
          48 +                 gw=float(state.get(robot, 'gripper_width')))
          49 +        return r, rects
          50 +
          51 +    def _clear_y_at(self, x, rects, held=None, aj=None, exclude=()):
          52 +        """Min robot y at horizontal pos x so nothing collides (robot above objects)."""
          53 +        r = self.r
          54 +        if aj is None:
          55 +            aj = r['aj']
          56 +        R = r['R']
          57 +        need = -1.0
          58 +        for name, o in rects.items():
          59 +            if name in exclude or (held is not None and name == held['name']):
          60 +                continue
          61 +            x0, x1, y1 = o['x0'], o['x1'], o['y1']
          62 +            # base circle
          63 +            dx = max(x0 - x, 0.0, x - x1)
          64 +            if dx < R:
          65 +                need = max(need, y1 + np.sqrt(R * R - dx * dx))
          66 +            # arm + gripper
          67 +            g0, g1 = x - r['gh'] / 2, x + r['gh'] / 2
          68 +            if g1 > x0 and g0 < x1:
          69 +                need = max(need, y1 + aj + r['gw'])
          70 +            # held object
          71 +            if held is not None:
          72 +                hx0 = x + held['dx0']
          73 +                hx1 = x + held['dx1']
          74 +                if hx1 > x0 and hx0 < x1:
          75 +                    need = max(need, y1 - held['dy0'])
          76 +        return need
          77 +
          78 +    def _clear_y_range(self, a, b, rects, held=None, aj=None, exclude=()):
          79 +        lo, hi = min(a, b), max(a, b)
          80 +        n = max(2, int(np.ceil((hi - lo) / 0.004)) + 1)
          81 +        xs = np.linspace(lo, hi, n)
          82 +        return max(self._clear_y_at(x, rects, held, aj, exclude) for x in xs)
          83 +
          84 +    # ----------------------------------------------------------------- reset
          85 +    def reset(self, state, info):
          86 +        self.phase = 'plan'
          87 +        self.task = None
          88 +        self.held = None
          89 +        self.stuck = 0
          90 +        self.last_pos = None
          91 +        self.grasp_eps = 0.002
          92 +        self.fail_count = {}
          93 +        self.t = 0
          94 +
          95 +    # -------------------------------------------------------------- planning
          96 +    def _held_info(self, o, r):
          97 +        return dict(name=o['name'], dx0=o['x0'] - r['x'], dx1=o['x1'] - r['x'],
          98 +                    dy0=o['y0'] - r['y'], dy1=o['y1'] - r['y'])
          99 +
         100 +    def _grasp_x(self, o, rects):
         101 +        """Choose robot x to grasp object o from above, minimizing needed height."""
         102 +        r = self.r
         103 +        top = o['y1']
         104 +        cands = np.linspace(o['x0'] + 0.01, o['x1'] - 0.01, 15)
         105 +        best, bestv = None, None
         106 +        centre = (o['x0'] + o['x1']) / 2
         107 +        for cx in cands:
         108 +            if cx < WORLD_X[0] + r['R'] + 1e-3 or cx > WORLD_X[1] - r['R'] - 1e-3:
         109 +                continue
         110 +            need = self._clear_y_at(cx, rects, None, ARM_MAX, exclude=(o['name'],))
         111 +            goal = top + ARM_MAX + r['gw'] + self.grasp_eps
         112 +            bad = max(0.0, need - goal)
         113 +            v = (round(bad, 4), abs(cx - centre))
         114 +            if bestv is None or v < bestv:
         115 +                best, bestv = cx, v
         116 +        if best is None:
         117 +            best = float(np.clip(centre, WORLD_X[0] + r['R'] + 1e-3, WORLD_X[1] - r['R'] - 1e-3))
         118 +        return best
         119 +
         120 +    def _place_candidates_target(self, blk, surf, rects):
         121 +        """Return list of (n_blockers, cost, rx, ry, blockers)."""
         122 +        r = self.r
         123 +        gx = self._grasp_x(blk, rects)
         124 +        held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx)
         125 +        gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
         126 +        held['dy0'] = blk['y0'] - gy
         127 +        held['dy1'] = blk['y1'] - gy
         128 +        bw = blk['x1'] - blk['x0']
         129 +        m = 0.004
         130 +        lo = surf['x0'] + m
         131 +        hi = surf['x1'] - bw - m
         132 +        if hi < lo:
         133 +            lo = hi = (surf['x0'] + surf['x1']) / 2 - bw / 2
         134 +        xs = np.linspace(lo, hi, max(2, int((hi - lo) / 0.004) + 2))
         135 +        bottom = surf['y1'] + 0.008
         136 +        ry = bottom - held['dy0']
         137 +        res = []
         138 +        centre = (surf['x0'] + surf['x1']) / 2 - bw / 2
         139 +        for px in xs:
         140 +            rx = px - held['dx0']
         141 +            if rx < WORLD_X[0] + r['R'] + 1e-3 or rx > WORLD_X[1] - r['R'] - 1e-3:
         142 +                continue
         143 +            blockers = []
         144 +            for name, o in rects.items():
         145 +                if o['type'] == 'target_surface' or name == blk['name']:
         146 +                    continue
         147 +                need = self._clear_y_at(rx, {name: o}, held, ARM_MAX)
         148 +                if need > ry - 1e-4:
         149 +                    blockers.append(name)
         150 +            cost = abs(px - centre) * 0.1 + abs(rx - blk['x0'] + held['dx0']) * 0.0
         151 +            res.append((len(blockers), cost, rx, ry, blockers))
         152 +        res.sort(key=lambda t: (t[0], t[1]))
         153 +        return res, held, gx, gy
         154 +
         155 +    def _drop_spot(self, o, rects, surf, blk):
         156 +        r = self.r
         157 +        gx = self._grasp_x(o, rects)
         158 +        held = dict(name=o['name'], dx0=o['x0'] - gx, dx1=o['x1'] - gx)
         159 +        gy = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
         160 +        held['dy0'] = o['y0'] - gy
         161 +        held['dy1'] = o['y1'] - gy
         162 +        ry = gy + 0.003
         163 +        others = {k: v for k, v in rects.items() if k != o['name']}
         164 +        for margin in (0.12, 0.06, 0.02, 0.005):
         165 +            best = None
         166 +            for rx in np.arange(WORLD_X[0] + r['R'] + 0.002, WORLD_X[1] - r['R'] - 0.002, 0.005):
         167 +                x0, x1 = rx + held['dx0'], rx + held['dx1']
         168 +                if x0 < WORLD_X[0] or x1 > WORLD_X[1]:
         169 +                    continue
         170 +                # stay away from the surface
         171 +                if x1 > surf['x0'] - margin - 0.02 and x0 < surf['x1'] + margin + 0.02:
         172 +                    continue
         173 +                ok = True
         174 +                for k, v in others.items():
         175 +                    if x1 > v['x0'] - margin and x0 < v['x1'] + margin:
         176 +                        ok = False
         177 +                        break
         178 +                if not ok:
         179 +                    continue
         180 +                if self._clear_y_at(rx, others, held, ARM_MAX) > ry - 1e-4:
         181 +                    continue
         182 +                cost = abs(rx - gx) + abs(rx - self.r['x']) * 0.2
         183 +                if best is None or cost < best[0]:
         184 +                    best = (cost, rx)
         185 +            if best is not None:
         186 +                return best[1], ry, gx, gy
         187 +        return None
         188 +
         189 +    def _plan(self, rects):
         190 +        surf = None
         191 +        blk = None
         192 +        for o in rects.values():
         193 +            if o['type'] == 'target_surface':
         194 +                surf = o
         195 +            elif o['type'] == 'target_block':
         196 +                blk = o
         197 +        cands, held, gx, gy = self._place_candidates_target(blk, surf, rects)
         198 +        if not cands or cands[0][0] == 0:
         199 +            if cands:
         200 +                _, _, rx, ry, _ = cands[0]
         201 +            else:
         202 +                rx = (surf['x0'] + surf['x1']) / 2 - (held['dx0'] + held['dx1']) / 2
         203 +                ry = surf['y1'] + 0.008 - held['dy0']
         204 +            return dict(obj=blk['name'], gx=gx, gy=gy, px=rx, py=ry, kind='target')
         205 +        blockers = cands[0][4]
         206 +        # remove the blocker closest to robot
         207 +        blockers = sorted(blockers, key=lambda n: abs((rects[n]['x0'] + rects[n]['x1']) / 2 - self.r['x']))
         208 +        name = blockers[0]
         209 +        o = rects[name]
         210 +        spot = self._drop_spot(o, rects, surf, blk)
         211 +        if spot is None:
         212 +            rx = WORLD_X[0] + 0.15 if (o['x0'] > 0.8) else WORLD_X[1] - 0.15
         213 +            gxx = self._grasp_x(o, rects)
         214 +            return dict(obj=name, gx=gxx, gy=o['y1'] + ARM_MAX + self.r['gw'] + self.grasp_eps,
         215 +                        px=rx, py=0.6, kind='obst')
         216 +        rx, ry, gxx, gyy = spot
         217 +        return dict(obj=name, gx=gxx, gy=gyy, px=rx, py=ry, kind='obst')
         218 +
         219 +    # ---------------------------------------------------------------- motion
         220 +    def _move_toward(self, gx, gy, rects, held, margin=0.004):
         221 +        """One step toward (gx, gy) avoiding collisions, returns (dx, dy)."""
         222 +        r = self.r
         223 +        x, y = r['x'], r['y']
         224 +        dx = float(np.clip(gx - x, -MAXD, MAXD))
         225 +        nx = x + dx
         226 +        # the height needed over remaining horizontal sweep
         227 +        if abs(gx - x) > 1e-6:
         228 +            need_rest = self._clear_y_range(nx, gx, rects, held) + margin
         229 +            need_step = self._clear_y_range(x, nx, rects, held) + margin
         230 +            ty = max(gy, need_rest)
         231 +            dy = float(np.clip(ty - y, -MAXD, MAXD))
         232 +            ny = y + dy
         233 +            if min(ny, y) < need_step and ny < need_step:
         234 +                # can't move horizontally yet; go up only
         235 +                dx = 0.0
         236 +                dy = float(np.clip(max(need_step, ty) - y, -MAXD, MAXD))
         237 +                if dy < 0:
         238 +                    dy = 0.0
         239 +                dy = max(dy, min(MAXD, need_step - y)) if need_step > y else dy
         240 +            elif ny < need_step:
         241 +                ny = need_step
         242 +                dy = ny - y
         243 +        else:
         244 +            dy = float(np.clip(gy - y, -MAXD, MAXD))
         245 +        ymax = WORLD_Y[1] - r['R'] - 1e-3
         246 +        if y + dy > ymax:
         247 +            dy = max(0.0, ymax - y)
         248 +        return dx, dy
         249 +
         250 +    def _action(self, dx=0.0, dy=0.0, darm=0.0, vac=0.0):
         251 +        a = np.array([dx, dy, 0.0, darm, vac], dtype=np.float32)
         252 +        return np.clip(a, self.low, self.high)
         253 +
         254 +    # ------------------------------------------------------------------- act
         255 +    def get_action(self, state):
         256 +        self.t += 1
         257 +        r, rects = self._parse(state)
         258 +        self.r = r
         259 +        darm = float(np.clip(ARM_MAX - r['aj'], 0, 0.1))
         260 +        dth = 0.0
         261 +        # keep theta pointing down
         262 +        if abs(r['theta'] + np.pi / 2) > 1e-3:
         263 +            dth = float(np.clip(-np.pi / 2 - r['theta'], -0.19, 0.19))
         264 +
         265 +        if self.phase == 'plan':
         266 +            self.task = self._plan(rects)
         267 +            self.phase = 'to_grasp'
         268 +            self.held = None
         269 +            self.stuck = 0
         270 +
         271 +        task = self.task
         272 +        o = rects.get(task['obj'])
         273 +
         274 +        if self.phase == 'to_grasp':
         275 +            # recompute grasp height from current object
         276 +            gy = o['y1'] + r['aj'] + r['gw'] + self.grasp_eps
         277 +            if r['aj'] < ARM_MAX - 1e-6:
         278 +                gy = max(gy, r['y'])  # wait for arm to extend before going down much
         279 +            if abs(r['x'] - task['gx']) < 1e-4 and abs(r['y'] - gy) < 1e-4 and r['aj'] >= ARM_MAX - 1e-6:
         280 +                self.phase = 'grasp'
         281 +                self.grasp_pose = (r['x'], r['y'], o['x'], o['y'])
         282 +                return self._action(0, 0, 0, 1.0)
         283 +            dx, dy = self._move_toward(task['gx'], gy, rects, None)
         284 +            # allow reaching the grasp contact height (target object excluded margin)
         285 +            if abs(r['x'] - task['gx']) < 1e-6:
         286 +                dy = float(np.clip(gy - r['y'], -MAXD, MAXD))
         287 +            a = self._action(dx, dy, darm, 0.0)
         288 +            a[2] = dth
         289 +            return self._check_stuck(a, r)
         290 +
         291 +        if self.phase == 'grasp':
         292 +            self.phase = 'lift'
         293 +            self.lift_start = (o['x'], o['y'])
         294 +            self.held = self._held_info(o, r)
         295 +            self.lift_steps = 0
         296 +
         297 +        if self.phase == 'lift' or self.phase == 'carry':
         298 +            held = self.held
         299 +            # verify object moves with robot
         300 +            ex_y = r['y'] + held['dy0']
         301 +            if abs(o['y0'] - ex_y) > 0.01 or abs(o['x0'] - (r['x'] + held['dx0'])) > 0.01:
         302 +                # grasp failed
         303 +                self.fail_count[task['obj']] = self.fail_count.get(task['obj'], 0) + 1
         304 +                self.grasp_eps = max(0.0, self.grasp_eps - 0.001)
         305 +                self.phase = 'plan'
         306 +                return self._action(0, MAXD, darm, 0.0)
         307 +            self.held = held = self._held_info(o, r)
         308 +            px, py = task['px'], task['py']
         309 +            if abs(r['x'] - px) < 1e-4 and abs(r['y'] - py) < 1e-4:
         310 +                self.phase = 'release'
         311 +            else:
         312 +                dx, dy = self._move_toward(px, py, rects, held)
         313 +                if abs(r['x'] - px) < 1e-6:
         314 +                    dy = float(np.clip(py - r['y'], -MAXD, MAXD))
         315 +                a = self._action(dx, dy, darm, 1.0)
         316 +                a[2] = dth
         317 +                res = self._check_stuck(a, r)
         318 +                if self.stuck > 4 and self.task['kind'] == 'obst' and r['x'] == px:
         319 +                    self.phase = 'release'
         320 +                else:
         321 +                    return res
         322 +
         323 +        if self.phase == 'release':
         324 +            self.phase = 'after_release'
         325 +            self.rel_steps = 0
         326 +            return self._action(0, 0, 0, 0.0)
         327 +
         328 +        if self.phase == 'after_release':
         329 +            self.phase = 'plan'
         330 +            self.held = None
         331 +            return self.get_action_replan(state)
         332 +
         333 +        return self._action(0, 0, darm, 0.0)
         334 +
         335 +    def get_action_replan(self, state):
         336 +        self.t -= 1
         337 +        return self.get_action(state)
         338 +
         339 +    def _check_stuck(self, a, r):
         340 +        pos = (round(r['x'], 5), round(r['y'], 5))
         341 +        if self.last_pos == pos:
         342 +            self.stuck += 1
         343 +        else:
         344 +            self.stuck = 0
         345 +        self.last_pos = pos
         346 +        if self.stuck > 3:
         347 +            # jiggle upward
         348 +            a[0] = 0.0
         349 +            a[1] = MAXD * 0.5
         350 +        return a
diff --git a/exp1.py b/exp1.py
new file mode 100644
index 0000000..94d2561
--- /dev/null
+++ b/exp1.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
           6 +def rs(o): return tuple(round(float(o.get(R,f)),3) for f in ['x','y','theta','arm_joint','vacuum'])
           7 +def bs(o): return tuple(round(float(o.get(B,f)),3) for f in ['x','y','theta'])
           8 +tx = 0.439+0.05
           9 +for i in range(20):
          10 +    dx = np.clip(tx-obs.get(R,'x'),-0.05,0.05)
          11 +    obs,r,t,tr,_ = env.step(np.array([dx,0,0,0,0],dtype=np.float32))
          12 +print(rs(obs))
          13 +for i in range(15):
          14 +    obs,r,t,tr,_ = env.step(np.array([0,-0.05,0,0,0],dtype=np.float32))
          15 +    print('down',rs(obs))
          16 +for i in range(5):
          17 +    obs,r,t,tr,_ = env.step(np.array([0,0,0,0.1,0],dtype=np.float32))
          18 +    print('arm',rs(obs))
          19 +obs,r,t,tr,_ = env.step(np.array([0,0,0,0,1],dtype=np.float32)); print('vac',rs(obs),bs(obs))
          20 +for i in range(5):
          21 +    obs,r,t,tr,_ = env.step(np.array([0,0.05,0,0,1],dtype=np.float32)); print('up',rs(obs),bs(obs))
          22 +env.close()
diff --git a/exp2.py b/exp2.py
new file mode 100644
index 0000000..4a3ed4c
--- /dev/null
+++ b/exp2.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
           6 +def rs(o): return tuple(round(float(o.get(R,f)),3) for f in ['x','y','theta','arm_joint','vacuum'])
           7 +def bs(o): return tuple(round(float(o.get(B,f)),3) for f in ['x','y','theta'])
           8 +def st(a):
           9 +    global obs
          10 +    obs,r,t,tr,_ = env.step(np.array(a,dtype=np.float32)); return r,t
          11 +# extend arm
          12 +for i in range(3): st([0,0,0,0.1,0]); print('arm',rs(obs))
          13 +for i in range(60): st([-0.05,0,0,0,0])
          14 +print('left', rs(obs))
          15 +for i in range(60): st([0.05,0,0,0,0])
          16 +print('right', rs(obs))
          17 +for i in range(10): st([0,0.05,0,0,0])
          18 +print('up', rs(obs))
          19 +# go grasp block with arm extended
          20 +tx=0.489
          21 +for i in range(40): st([np.clip(tx-obs.get(R,'x'),-.05,.05),0,0,0,0])
          22 +for i in range(80):
          23 +    st([0,-0.01,0,0,0])
          24 +print('down',rs(obs))
          25 +st([0,0,0,0,1]); 
          26 +for i in range(4): st([0,0.05,0,0,1])
          27 +print('lift',rs(obs),bs(obs))
          28 +st([0,0,0,0,0]); print('release', bs(obs))
          29 +st([0,0,0,0,0]); print('release', bs(obs))
          30 +env.close()
diff --git a/probe.py b/probe.py
new file mode 100644
index 0000000..95f9861
--- /dev/null
+++ b/probe.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +import sys
           3 +env = make_env()
           4 +tf = env.observation_space.type_features
           5 +for seed in range(int(sys.argv[1]), int(sys.argv[2])):
           6 +    obs, info = env.reset(seed=seed)
           7 +    print("seed", seed, info)
           8 +    for n in sorted(obs.get_object_names()):
           9 +        o = obs.get_object_from_name(n)
          10 +        print(" ", n, o.type.name, {f: round(float(obs.get(o,f)),3) for f in tf[o.type]})
          11 +env.close()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..580f9aa
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,26 @@
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
          12 +    tot = 0; t0 = time.time()
          13 +    for t in range(env.max_steps):
          14 +        a = ap.get_action(obs)
          15 +        obs, r, term, trunc, info2 = env.step(a)
          16 +        tot += r
          17 +        if term or trunc: break
          18 +    env.close()
          19 +    return seed, info.get('object_count'), term, t+1, round(time.time()-t0,1)
          20 +
          21 +if __name__ == '__main__':
          22 +    a, b = int(sys.argv[1]), int(sys.argv[2])
          23 +    with ThreadPoolExecutor(8) as ex:
          24 +        res = list(ex.map(run, range(a, b)))
          25 +    for r in res: print(r)
          26 +    print('success', sum(r[2] for r in res), '/', len(res), 'mean steps', np.mean([r[3] for r in res]))
```

</details>

<a id="C003"></a>
### C003 · Jointly choose grasp offset and placement for target (reach near world edge)

Commit `5372949cea73b7aba878cab52e3c13f1fad4564f`; parents: 0b8ce0f860cecdd4c82fbc03a0a60655df38a04e. Recorded author date: 2026-09-30T12:22:04+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0052](01_timeline.md#E0052): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_5372949_approach.py) · [Exact all-file diff](evidence/diffs/C003_5372949.diff)

[Previous saved controller snapshot](evidence/versions/C002_0b8ce0f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6841ad0..631df04 100644
--- a/approach.py
+++ b/approach.py
@@ -97,34 +97,38 @@ class GeneratedApproach:
   97     97          return dict(name=o['name'], dx0=o['x0'] - r['x'], dx1=o['x1'] - r['x'],
   98     98                      dy0=o['y0'] - r['y'], dy1=o['y1'] - r['y'])
   99     99  
  100        -    def _grasp_x(self, o, rects):
  101        -        """Choose robot x to grasp object o from above, minimizing needed height."""
         100 +    def _grasp_xs(self, o, rects):
         101 +        """Candidate robot x's to grasp object o from above, best first (only collision-free ones if any)."""
  102    102          r = self.r
  103    103          top = o['y1']
  104        -        cands = np.linspace(o['x0'] + 0.01, o['x1'] - 0.01, 15)
  105        -        best, bestv = None, None
         104 +        cands = np.linspace(o['x0'] + 0.008, o['x1'] - 0.008, 21)
  106    105          centre = (o['x0'] + o['x1']) / 2
         106 +        out = []
  107    107          for cx in cands:
  108    108              if cx < WORLD_X[0] + r['R'] + 1e-3 or cx > WORLD_X[1] - r['R'] - 1e-3:
  109    109                  continue
  110    110              need = self._clear_y_at(cx, rects, None, ARM_MAX, exclude=(o['name'],))
  111    111              goal = top + ARM_MAX + r['gw'] + self.grasp_eps
  112    112              bad = max(0.0, need - goal)
  113        -            v = (round(bad, 4), abs(cx - centre))
  114        -            if bestv is None or v < bestv:
  115        -                best, bestv = cx, v
  116        -        if best is None:
  117        -            best = float(np.clip(centre, WORLD_X[0] + r['R'] + 1e-3, WORLD_X[1] - r['R'] - 1e-3))
  118        -        return best
         113 +            out.append((round(bad, 4), abs(cx - centre), float(cx)))
         114 +        out.sort()
         115 +        if not out:
         116 +            return [float(np.clip(centre, WORLD_X[0] + r['R'] + 1e-3, WORLD_X[1] - r['R'] - 1e-3))]
         117 +        good = [c[2] for c in out if c[0] == 0]
         118 +        return good if good else [out[0][2]]
         119 +
         120 +    def _grasp_x(self, o, rects):
         121 +        return self._grasp_xs(o, rects)[0]
  119    122  
  120    123      def _place_candidates_target(self, blk, surf, rects):
  121        -        """Return list of (n_blockers, cost, rx, ry, blockers)."""
         124 +        """Return (list of (n_blockers, cost, rx, ry, blockers), held, gx, gy)."""
  122    125          r = self.r
  123        -        gx = self._grasp_x(blk, rects)
  124        -        held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx)
  125        -        gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  126        -        held['dy0'] = blk['y0'] - gy
  127        -        held['dy1'] = blk['y1'] - gy
         126 +        gxs = self._grasp_xs(blk, rects)
         127 +        centre_g = (blk['x0'] + blk['x1']) / 2
         128 +        # a handful of grasp offsets: best one, then spread
         129 +        if len(gxs) > 5:
         130 +            idx = np.linspace(0, len(gxs) - 1, 5).astype(int)
         131 +            gxs = [gxs[0]] + [gxs[i] for i in idx]
  128    132          bw = blk['x1'] - blk['x0']
  129    133          m = 0.004
  130    134          lo = surf['x0'] + m
@@ -132,25 +136,40 @@ class GeneratedApproach:
  132    136          if hi < lo:
  133    137              lo = hi = (surf['x0'] + surf['x1']) / 2 - bw / 2
  134    138          xs = np.linspace(lo, hi, max(2, int((hi - lo) / 0.004) + 2))
  135        -        bottom = surf['y1'] + 0.008
  136        -        ry = bottom - held['dy0']
  137        -        res = []
  138    139          centre = (surf['x0'] + surf['x1']) / 2 - bw / 2
  139        -        for px in xs:
  140        -            rx = px - held['dx0']
  141        -            if rx < WORLD_X[0] + r['R'] + 1e-3 or rx > WORLD_X[1] - r['R'] - 1e-3:
  142        -                continue
  143        -            blockers = []
  144        -            for name, o in rects.items():
  145        -                if o['type'] == 'target_surface' or name == blk['name']:
         140 +        best = None
         141 +        others = [(n, o) for n, o in rects.items()
         142 +                  if o['type'] != 'target_surface' and n != blk['name']]
         143 +        for gi, gx in enumerate(gxs):
         144 +            gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
         145 +            held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx,
         146 +                        dy0=blk['y0'] - gy, dy1=blk['y1'] - gy)
         147 +            bottom = surf['y1'] + 0.008
         148 +            ry = bottom - held['dy0']
         149 +            res = []
         150 +            for px in xs:
         151 +                rx = px - held['dx0']
         152 +                if rx < WORLD_X[0] + r['R'] + 1e-3 or rx > WORLD_X[1] - r['R'] - 1e-3:
  146    153                      continue
  147        -                need = self._clear_y_at(rx, {name: o}, held, ARM_MAX)
  148        -                if need > ry - 1e-4:
  149        -                    blockers.append(name)
  150        -            cost = abs(px - centre) * 0.1 + abs(rx - blk['x0'] + held['dx0']) * 0.0
  151        -            res.append((len(blockers), cost, rx, ry, blockers))
  152        -        res.sort(key=lambda t: (t[0], t[1]))
  153        -        return res, held, gx, gy
         154 +                blockers = []
         155 +                for name, o in others:
         156 +                    need = self._clear_y_at(rx, {name: o}, held, ARM_MAX)
         157 +                    if need > ry - 1e-4:
         158 +                        blockers.append(name)
         159 +                cost = abs(px - centre) * 0.1 + 0.001 * gi
         160 +                res.append((len(blockers), cost, rx, ry, blockers))
         161 +            if not res:
         162 +                continue
         163 +            res.sort(key=lambda t: (t[0], t[1]))
         164 +            if best is None or (res[0][0], res[0][1]) < (best[0][0][0], best[0][0][1]):
         165 +                best = (res, held, gx, gy)
         166 +        if best is None:
         167 +            gx = gxs[0]
         168 +            gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
         169 +            held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx,
         170 +                        dy0=blk['y0'] - gy, dy1=blk['y1'] - gy)
         171 +            return [], held, gx, gy
         172 +        return best
  154    173  
  155    174      def _drop_spot(self, o, rects, surf, blk):
  156    175          r = self.r
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..96529e2
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,21 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed=int(sys.argv[1]); opts = {'object_count': int(sys.argv[2])} if len(sys.argv)>2 else None
           6 +env = make_env()
           7 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           8 +obs, info = env.reset(seed=seed, options=opts)
           9 +print(info)
          10 +ap.reset(obs, info)
          11 +r,rects = ap._parse(obs)
          12 +for k,v in sorted(rects.items()): print(k, {q: round(v[q],3) for q in ['x0','x1','y0','y1']})
          13 +print('robot', r)
          14 +tt=0
          15 +for t in range(300):
          16 +    t0=time.time(); a = ap.get_action(obs); tt+=time.time()-t0
          17 +    obs, rew, term, trunc, _ = env.step(a)
          18 +    rr,_ = ap._parse(obs)
          19 +    if t<300 and (t%5==0 or ap.phase!='to_grasp'): print(t, ap.phase, ap.task['obj'], np.round(a,3), round(rr['x'],3), round(rr['y'],3), ap.stuck)
          20 +    if term: print('done', t); break
          21 +print('compute', tt)
```

</details>

<a id="C004"></a>
### C004 · Fix motion deadlock, grasp/release on arrival step

Commit `bd5eeb77c0fd32c71816ad99fd36e8ddb547fc67`; parents: 5372949cea73b7aba878cab52e3c13f1fad4564f. Recorded author date: 2026-09-30T12:33:57+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0125](01_timeline.md#E0125): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_bd5eeb7_approach.py) · [Exact all-file diff](evidence/diffs/C004_bd5eeb7.diff)

[Previous saved controller snapshot](evidence/versions/C003_5372949_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 631df04..0f005da 100644
--- a/approach.py
+++ b/approach.py
@@ -4,6 +4,7 @@ WORLD_X = (0.0, 1.618)
    4      4  WORLD_Y = (0.0, 1.0)
    5      5  MAXD = 0.05
    6      6  ARM_MAX = 0.2
           7 +EARLY = True
    7      8  
    8      9  
    9     10  class GeneratedApproach:
@@ -248,17 +249,11 @@ class GeneratedApproach:
  248    249              need_step = self._clear_y_range(x, nx, rects, held) + margin
  249    250              ty = max(gy, need_rest)
  250    251              dy = float(np.clip(ty - y, -MAXD, MAXD))
  251        -            ny = y + dy
  252        -            if min(ny, y) < need_step and ny < need_step:
  253        -                # can't move horizontally yet; go up only
         252 +            if y + dy < need_step:
         253 +                dy = float(np.clip(need_step - y, -MAXD, MAXD))
         254 +            if y + dy < need_step - 1e-9:
  254    255                  dx = 0.0
  255        -                dy = float(np.clip(max(need_step, ty) - y, -MAXD, MAXD))
  256        -                if dy < 0:
  257        -                    dy = 0.0
  258        -                dy = max(dy, min(MAXD, need_step - y)) if need_step > y else dy
  259        -            elif ny < need_step:
  260        -                ny = need_step
  261        -                dy = ny - y
         256 +                dy = MAXD
  262    257          else:
  263    258              dy = float(np.clip(gy - y, -MAXD, MAXD))
  264    259          ymax = WORLD_Y[1] - r['R'] - 1e-3
@@ -303,7 +298,12 @@ class GeneratedApproach:
  303    298              # allow reaching the grasp contact height (target object excluded margin)
  304    299              if abs(r['x'] - task['gx']) < 1e-6:
  305    300                  dy = float(np.clip(gy - r['y'], -MAXD, MAXD))
  306        -            a = self._action(dx, dy, darm, 0.0)
         301 +            vac = 0.0
         302 +            if (EARLY and abs(r['x'] + dx - task['gx']) < 1e-6 and abs(r['y'] + dy - gy) < 1e-6
         303 +                    and r['aj'] + darm >= ARM_MAX - 1e-6):
         304 +                vac = 1.0
         305 +                self.phase = 'grasp'
         306 +            a = self._action(dx, dy, darm, vac)
  307    307              a[2] = dth
  308    308              return self._check_stuck(a, r)
  309    309  
@@ -331,7 +331,12 @@ class GeneratedApproach:
  331    331                  dx, dy = self._move_toward(px, py, rects, held)
  332    332                  if abs(r['x'] - px) < 1e-6:
  333    333                      dy = float(np.clip(py - r['y'], -MAXD, MAXD))
  334        -                a = self._action(dx, dy, darm, 1.0)
         334 +                vac = 1.0
         335 +                if (EARLY and task['kind'] == 'obst' and abs(r['x'] + dx - px) < 1e-6
         336 +                        and abs(r['y'] + dy - py) < 1e-6):
         337 +                    vac = 0.0
         338 +                    self.phase = 'after_release'
         339 +                a = self._action(dx, dy, darm, vac)
  335    340                  a[2] = dth
  336    341                  res = self._check_stuck(a, r)
  337    342                  if self.stuck > 4 and self.task['kind'] == 'obst' and r['x'] == px:
diff --git a/dbg.py b/dbg.py
index 96529e2..ce93c4c 100644
--- a/dbg.py
+++ b/dbg.py
@@ -19,3 +19,5 @@ for t in range(300):
   19     19      if t<300 and (t%5==0 or ap.phase!='to_grasp'): print(t, ap.phase, ap.task['obj'], np.round(a,3), round(rr['x'],3), round(rr['y'],3), ap.stuck)
   20     20      if term: print('done', t); break
   21     21  print('compute', tt)
          22 +_,rects = ap._parse(obs)
          23 +for k,v in sorted(rects.items()): print(k, {q: round(v[q],3) for q in ['x0','x1','y0','y1']})
diff --git a/test_approach.py b/test_approach.py
index 580f9aa..5dd1163 100644
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
          11 +    obs, info = env.reset(seed=seed, options=({'object_count':OC} if OC is not None else None))
   11     12      ap.reset(obs, info)
   12     13      tot = 0; t0 = time.time()
   13     14      for t in range(env.max_steps):
@@ -20,7 +21,9 @@ def run(seed):
   20     21  
   21     22  if __name__ == '__main__':
   22     23      a, b = int(sys.argv[1]), int(sys.argv[2])
          24 +    if len(sys.argv)>3: OC=int(sys.argv[3])
   23     25      with ThreadPoolExecutor(8) as ex:
   24     26          res = list(ex.map(run, range(a, b)))
   25        -    for r in res: print(r)
          27 +    for r in res:
          28 +        if not r[2] or len(res)<20: print(r)
   26     29      print('success', sum(r[2] for r in res), '/', len(res), 'mean steps', np.mean([r[3] for r in res]))
```

</details>

<a id="C005"></a>
### C005 · Cost-based drop-spot selection (can drop in air), target bottom offset 0.018

Commit `332cf946cf4e4053315780f5e2880177551a22af`; parents: bd5eeb77c0fd32c71816ad99fd36e8ddb547fc67. Recorded author date: 2026-09-30T12:36:16+02:00.

File roles (automatic): policy.

- [E0141](01_timeline.md#E0141): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_332cf94_approach.py) · [Exact all-file diff](evidence/diffs/C005_332cf94.diff)

[Previous saved controller snapshot](evidence/versions/C004_bd5eeb7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0f005da..9b89149 100644
--- a/approach.py
+++ b/approach.py
@@ -5,6 +5,7 @@ WORLD_Y = (0.0, 1.0)
    5      5  MAXD = 0.05
    6      6  ARM_MAX = 0.2
    7      7  EARLY = True
           8 +BOTTOM_OFF = 0.018
    8      9  
    9     10  
   10     11  class GeneratedApproach:
@@ -145,7 +146,7 @@ class GeneratedApproach:
  145    146              gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  146    147              held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx,
  147    148                          dy0=blk['y0'] - gy, dy1=blk['y1'] - gy)
  148        -            bottom = surf['y1'] + 0.008
         149 +            bottom = surf['y1'] + BOTTOM_OFF
  149    150              ry = bottom - held['dy0']
  150    151              res = []
  151    152              for px in xs:
@@ -172,23 +173,72 @@ class GeneratedApproach:
  172    173              return [], held, gx, gy
  173    174          return best
  174    175  
         176 +    # ------------------------------------------------------ vectorised costs
         177 +    def _colprof(self, xs, b, held, aj=ARM_MAX):
         178 +        r = self.r
         179 +        R = r['R']
         180 +        bx0, bx1, by1 = b
         181 +        d = np.maximum(np.maximum(bx0 - xs, 0.0), xs - bx1)
         182 +        out = np.where(d < R, by1 + np.sqrt(np.maximum(R * R - d * d, 0.0)), -1.0)
         183 +        g = (xs + r['gh'] / 2 > bx0) & (xs - r['gh'] / 2 < bx1)
         184 +        out = np.maximum(out, np.where(g, by1 + aj + r['gw'], -1.0))
         185 +        if held is not None:
         186 +            h = (xs + held['dx1'] > bx0) & (xs + held['dx0'] < bx1)
         187 +            out = np.maximum(out, np.where(h, by1 - held['dy0'], -1.0))
         188 +        return out
         189 +
         190 +    def _profile(self, xs, rects, held, exclude=()):
         191 +        out = np.full(len(xs), -1.0)
         192 +        for n, o in rects.items():
         193 +            if n in exclude or (held is not None and n == held['name']):
         194 +                continue
         195 +            out = np.maximum(out, self._colprof(xs, (o['x0'], o['x1'], o['y1']), held))
         196 +        return out
         197 +
         198 +    def _xi(self, x):
         199 +        return int(np.clip(round((x - self.xs[0]) / self.dxs), 0, len(self.xs) - 1))
         200 +
         201 +    def _est(self, xa, ya, xb, yb, prof, margin=0.004):
         202 +        dx = abs(xb - xa)
         203 +        if dx < 1e-6:
         204 +            return np.ceil(abs(yb - ya) / MAXD - 1e-6)
         205 +        i, j = sorted((self._xi(xa), self._xi(xb)))
         206 +        H = prof[i:j + 1].max() + margin
         207 +        top = max(H, ya, yb)
         208 +        vert = (top - ya) + (top - yb)
         209 +        return np.ceil(max(dx, vert) / MAXD - 1e-6)
         210 +
         211 +    def _mk_held(self, o, gx, gy):
         212 +        return dict(name=o['name'], dx0=o['x0'] - gx, dx1=o['x1'] - gx,
         213 +                    dy0=o['y0'] - gy, dy1=o['y1'] - gy)
         214 +
  175    215      def _drop_spot(self, o, rects, surf, blk):
  176    216          r = self.r
         217 +        self.xs = xs = np.arange(0.0, WORLD_X[1] + 1e-9, 0.005)
         218 +        self.dxs = 0.005
  177    219          gx = self._grasp_x(o, rects)
  178        -        held = dict(name=o['name'], dx0=o['x0'] - gx, dx1=o['x1'] - gx)
  179    220          gy = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  180        -        held['dy0'] = o['y0'] - gy
  181        -        held['dy1'] = o['y1'] - gy
  182        -        ry = gy + 0.003
         221 +        held = self._mk_held(o, gx, gy)
  183    222          others = {k: v for k, v in rects.items() if k != o['name']}
  184        -        for margin in (0.12, 0.06, 0.02, 0.005):
  185        -            best = None
  186        -            for rx in np.arange(WORLD_X[0] + r['R'] + 0.002, WORLD_X[1] - r['R'] - 0.002, 0.005):
         223 +        # target plan assuming o removed
         224 +        cands, held_b, gxb, gyb = self._place_candidates_target(blk, surf, others)
         225 +        if cands:
         226 +            _, _, rxt, ryt, _ = cands[0]
         227 +        else:
         228 +            rxt, ryt = (surf['x0'] + surf['x1']) / 2, 0.5
         229 +        P1 = self._profile(xs, others, held)
         230 +        P2 = self._profile(xs, others, None)
         231 +        P3 = self._profile(xs, {k: v for k, v in others.items() if k != blk['name']}, held_b)
         232 +        ymax = WORLD_Y[1] - r['R'] - 0.002
         233 +        best = None
         234 +        for margin in (0.03, 0.01):
         235 +            for rx in xs:
         236 +                if rx < WORLD_X[0] + r['R'] + 0.002 or rx > WORLD_X[1] - r['R'] - 0.002:
         237 +                    continue
  187    238                  x0, x1 = rx + held['dx0'], rx + held['dx1']
  188    239                  if x0 < WORLD_X[0] or x1 > WORLD_X[1]:
  189    240                      continue
  190        -                # stay away from the surface
  191        -                if x1 > surf['x0'] - margin - 0.02 and x0 < surf['x1'] + margin + 0.02:
         241 +                if x1 > surf['x0'] - margin and x0 < surf['x1'] + margin:
  192    242                      continue
  193    243                  ok = True
  194    244                  for k, v in others.items():
@@ -197,13 +247,19 @@ class GeneratedApproach:
  197    247                          break
  198    248                  if not ok:
  199    249                      continue
  200        -                if self._clear_y_at(rx, others, held, ARM_MAX) > ry - 1e-4:
  201        -                    continue
  202        -                cost = abs(rx - gx) + abs(rx - self.r['x']) * 0.2
  203        -                if best is None or cost < best[0]:
  204        -                    best = (cost, rx)
         250 +                ry_low = max(gy + 0.003, P1[self._xi(rx)] + 0.004)
         251 +                for ry in np.arange(ry_low, ymax, 0.05)[:8]:
         252 +                    c1 = self._est(gx, gy, rx, ry, P1)
         253 +                    box = (x0, x1, ry + held['dy1'])
         254 +                    P2n = np.maximum(P2, self._colprof(xs, box, None))
         255 +                    c2 = self._est(rx, ry, gxb, gyb, P2n)
         256 +                    P3n = np.maximum(P3, self._colprof(xs, box, held_b))
         257 +                    c3 = self._est(gxb, gyb, rxt, ryt, P3n)
         258 +                    cost = c1 + c2 + c3 + 0.01 * (ry - ry_low)
         259 +                    if best is None or cost < best[0]:
         260 +                        best = (cost, rx, ry)
  205    261              if best is not None:
  206        -                return best[1], ry, gx, gy
         262 +                return best[1], best[2], gx, gy
  207    263          return None
  208    264  
  209    265      def _plan(self, rects):
@@ -220,7 +276,7 @@ class GeneratedApproach:
  220    276                  _, _, rx, ry, _ = cands[0]
  221    277              else:
  222    278                  rx = (surf['x0'] + surf['x1']) / 2 - (held['dx0'] + held['dx1']) / 2
  223        -                ry = surf['y1'] + 0.008 - held['dy0']
         279 +                ry = surf['y1'] + BOTTOM_OFF - held['dy0']
  224    280              return dict(obj=blk['name'], gx=gx, gy=gy, px=rx, py=ry, kind='target')
  225    281          blockers = cands[0][4]
  226    282          # remove the blocker closest to robot
```

</details>

<a id="C006"></a>
### C006 · Step-cost based target placement choice

Commit `d18ea75d0ff2f60d294c443eec216cc239e27c79`; parents: 332cf946cf4e4053315780f5e2880177551a22af. Recorded author date: 2026-09-30T12:41:46+02:00.

File roles (automatic): policy.

- [E0169](01_timeline.md#E0169): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_d18ea75_approach.py) · [Exact all-file diff](evidence/diffs/C006_d18ea75.diff)

[Previous saved controller snapshot](evidence/versions/C005_332cf94_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9b89149..050d383 100644
--- a/approach.py
+++ b/approach.py
@@ -85,6 +85,8 @@ class GeneratedApproach:
   85     85  
   86     86      # ----------------------------------------------------------------- reset
   87     87      def reset(self, state, info):
          88 +        self.xs = np.arange(0.0, WORLD_X[1] + 1e-9, 0.005)
          89 +        self.dxs = 0.005
   88     90          self.phase = 'plan'
   89     91          self.task = None
   90     92          self.held = None
@@ -142,10 +144,13 @@ class GeneratedApproach:
  142    144          best = None
  143    145          others = [(n, o) for n, o in rects.items()
  144    146                    if o['type'] != 'target_surface' and n != blk['name']]
         147 +        PA = self._profile(self.xs, rects, None)
  145    148          for gi, gx in enumerate(gxs):
  146    149              gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  147    150              held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx,
  148    151                          dy0=blk['y0'] - gy, dy1=blk['y1'] - gy)
         152 +            cA = self._est(r['x'], r['y'], gx, gy, PA)
         153 +            PB = self._profile(self.xs, {n: o for n, o in others}, held)
  149    154              bottom = surf['y1'] + BOTTOM_OFF
  150    155              ry = bottom - held['dy0']
  151    156              res = []
@@ -158,7 +163,7 @@ class GeneratedApproach:
  158    163                      need = self._clear_y_at(rx, {name: o}, held, ARM_MAX)
  159    164                      if need > ry - 1e-4:
  160    165                          blockers.append(name)
  161        -                cost = abs(px - centre) * 0.1 + 0.001 * gi
         166 +                cost = cA + self._est(gx, gy, rx, ry, PB) + abs(px - centre) * 0.1 + 0.001 * gi
  162    167                  res.append((len(blockers), cost, rx, ry, blockers))
  163    168              if not res:
  164    169                  continue
@@ -214,8 +219,7 @@ class GeneratedApproach:
  214    219  
  215    220      def _drop_spot(self, o, rects, surf, blk):
  216    221          r = self.r
  217        -        self.xs = xs = np.arange(0.0, WORLD_X[1] + 1e-9, 0.005)
  218        -        self.dxs = 0.005
         222 +        xs = self.xs
  219    223          gx = self._grasp_x(o, rects)
  220    224          gy = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  221    225          held = self._mk_held(o, gx, gy)
```

</details>

<a id="C007"></a>
### C007 · Simulated step estimator for costs

Commit `ab5c4ba38c8f919dc6ddb3a714cb193ef004cabf`; parents: d18ea75d0ff2f60d294c443eec216cc239e27c79. Recorded author date: 2026-09-30T12:46:59+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0192](01_timeline.md#E0192): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_ab5c4ba_approach.py) · [Exact all-file diff](evidence/diffs/C007_ab5c4ba.diff)

[Previous saved controller snapshot](evidence/versions/C006_d18ea75_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 050d383..874e567 100644
--- a/approach.py
+++ b/approach.py
@@ -204,14 +204,40 @@ class GeneratedApproach:
  204    204          return int(np.clip(round((x - self.xs[0]) / self.dxs), 0, len(self.xs) - 1))
  205    205  
  206    206      def _est(self, xa, ya, xb, yb, prof, margin=0.004):
  207        -        dx = abs(xb - xa)
  208        -        if dx < 1e-6:
         207 +        """Simulate the greedy controller on a 1-D clearance profile; return #steps."""
         208 +        if abs(xb - xa) < 1e-6:
  209    209              return np.ceil(abs(yb - ya) / MAXD - 1e-6)
  210        -        i, j = sorted((self._xi(xa), self._xi(xb)))
  211        -        H = prof[i:j + 1].max() + margin
  212        -        top = max(H, ya, yb)
  213        -        vert = (top - ya) + (top - yb)
  214        -        return np.ceil(max(dx, vert) / MAXD - 1e-6)
         210 +        ia, ib = self._xi(xa), self._xi(xb)
         211 +        if ia <= ib:
         212 +            seg = prof[ia:ib + 1] + margin
         213 +        else:
         214 +            seg = prof[ib:ia + 1][::-1] + margin
         215 +        rem = np.maximum.accumulate(seg[::-1])[::-1]
         216 +        n = len(seg)
         217 +        d = abs(xb - xa)
         218 +        pos = 0.0
         219 +        y = ya
         220 +        steps = 0
         221 +        while steps < 200:
         222 +            if d - pos < 1e-6:
         223 +                steps += np.ceil(abs(yb - y) / MAXD - 1e-6)
         224 +                break
         225 +            npos = min(d, pos + MAXD)
         226 +            k0 = int(round(pos / d * (n - 1)))
         227 +            k1 = int(round(npos / d * (n - 1)))
         228 +            need_rest = rem[k1]
         229 +            need_step = seg[k0:k1 + 1].max()
         230 +            ty = max(yb, need_rest)
         231 +            dy = min(MAXD, max(-MAXD, ty - y))
         232 +            if y + dy < need_step:
         233 +                dy = min(MAXD, max(-MAXD, need_step - y))
         234 +            if y + dy < need_step - 1e-9:
         235 +                y += MAXD
         236 +            else:
         237 +                y += dy
         238 +                pos = npos
         239 +            steps += 1
         240 +        return steps
  215    241  
  216    242      def _mk_held(self, o, gx, gy):
  217    243          return dict(name=o['name'], dx0=o['x0'] - gx, dx1=o['x1'] - gx,
@@ -236,7 +262,7 @@ class GeneratedApproach:
  236    262          ymax = WORLD_Y[1] - r['R'] - 0.002
  237    263          best = None
  238    264          for margin in (0.03, 0.01):
  239        -            for rx in xs:
         265 +            for rx in xs[::2]:
  240    266                  if rx < WORLD_X[0] + r['R'] + 0.002 or rx > WORLD_X[1] - r['R'] - 0.002:
  241    267                      continue
  242    268                  x0, x1 = rx + held['dx0'], rx + held['dx1']
@@ -252,7 +278,7 @@ class GeneratedApproach:
  252    278                  if not ok:
  253    279                      continue
  254    280                  ry_low = max(gy + 0.003, P1[self._xi(rx)] + 0.004)
  255        -                for ry in np.arange(ry_low, ymax, 0.05)[:8]:
         281 +                for ry in np.arange(ry_low, ymax, 0.05)[:5]:
  256    282                      c1 = self._est(gx, gy, rx, ry, P1)
  257    283                      box = (x0, x1, ry + held['dy1'])
  258    284                      P2n = np.maximum(P2, self._colprof(xs, box, None))
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..a3948f9
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,26 @@
           1 +import numpy as np, sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +import approach
           5 +env = make_env()
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           7 +obs, info = env.reset(seed=3, options={'object_count':4})
           8 +ap.reset(obs, info)
           9 +r, rects = ap._parse(obs); ap.r = r
          10 +o = rects['obstruction1']; surf=rects['target_surface']; blk=rects['target_block']
          11 +xs=ap.xs
          12 +gx = ap._grasp_x(o, rects); gy = o['y1']+0.2+r['gw']+ap.grasp_eps
          13 +held = ap._mk_held(o,gx,gy)
          14 +others = {k:v for k,v in rects.items() if k!=o['name']}
          15 +cands, held_b, gxb, gyb = ap._place_candidates_target(blk, surf, others)
          16 +print('gx',gx,'gy',gy,'target', cands[0][:4], gxb, gyb)
          17 +P1 = ap._profile(xs, others, held); P2 = ap._profile(xs, others, None)
          18 +P3 = ap._profile(xs, {k: v for k, v in others.items() if k != blk['name']}, held_b)
          19 +_,_,rxt,ryt,_ = cands[0]
          20 +for rx in [0.36, 1.45, 1.47, 1.5]:
          21 +    ry = max(gy+0.003, P1[ap._xi(rx)]+0.004)
          22 +    x0,x1 = rx+held['dx0'], rx+held['dx1']
          23 +    box=(x0,x1,ry+held['dy1'])
          24 +    c1=ap._est(gx,gy,rx,ry,P1); c2=ap._est(rx,ry,gxb,gyb,np.maximum(P2,ap._colprof(xs,box,None))); c3=ap._est(gxb,gyb,rxt,ryt,np.maximum(P3,ap._colprof(xs,box,held_b)))
          25 +    print(rx, ry, c1,c2,c3)
          26 +print(ap._drop_spot(o, rects, surf, blk))
```

</details>

<a id="C008"></a>
### C008 · Keep gripper away from other objects while vacuum on (vacuum grabs within ~0.015)

Commit `634fc60717c8ad3f3331d779afc0fa4006ee15a5`; parents: ab5c4ba38c8f919dc6ddb3a714cb193ef004cabf. Recorded author date: 2026-09-30T12:59:08+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0253](01_timeline.md#E0253): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_634fc60_approach.py) · [Exact all-file diff](evidence/diffs/C008_634fc60.diff)

[Previous saved controller snapshot](evidence/versions/C007_ab5c4ba_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 874e567..616bc89 100644
--- a/approach.py
+++ b/approach.py
@@ -6,6 +6,7 @@ MAXD = 0.05
    6      6  ARM_MAX = 0.2
    7      7  EARLY = True
    8      8  BOTTOM_OFF = 0.018
           9 +VM = 0.025  # keep gripper this far from non-held objects while vacuum is on
    9     10  
   10     11  
   11     12  class GeneratedApproach:
@@ -50,9 +51,11 @@ class GeneratedApproach:
   50     51                   gw=float(state.get(robot, 'gripper_width')))
   51     52          return r, rects
   52     53  
   53        -    def _clear_y_at(self, x, rects, held=None, aj=None, exclude=()):
          54 +    def _clear_y_at(self, x, rects, held=None, aj=None, exclude=(), vm=None):
   54     55          """Min robot y at horizontal pos x so nothing collides (robot above objects)."""
   55     56          r = self.r
          57 +        if vm is None:
          58 +            vm = VM if held is not None else 0.0
   56     59          if aj is None:
   57     60              aj = r['aj']
   58     61          R = r['R']
@@ -66,9 +69,9 @@ class GeneratedApproach:
   66     69              if dx < R:
   67     70                  need = max(need, y1 + np.sqrt(R * R - dx * dx))
   68     71              # arm + gripper
   69        -            g0, g1 = x - r['gh'] / 2, x + r['gh'] / 2
          72 +            g0, g1 = x - r['gh'] / 2 - vm, x + r['gh'] / 2 + vm
   70     73              if g1 > x0 and g0 < x1:
   71        -                need = max(need, y1 + aj + r['gw'])
          74 +                need = max(need, y1 + aj + r['gw'] + vm)
   72     75              # held object
   73     76              if held is not None:
   74     77                  hx0 = x + held['dx0']
@@ -111,7 +114,7 @@ class GeneratedApproach:
  111    114          for cx in cands:
  112    115              if cx < WORLD_X[0] + r['R'] + 1e-3 or cx > WORLD_X[1] - r['R'] - 1e-3:
  113    116                  continue
  114        -            need = self._clear_y_at(cx, rects, None, ARM_MAX, exclude=(o['name'],))
         117 +            need = self._clear_y_at(cx, rects, None, ARM_MAX, exclude=(o['name'],), vm=VM)
  115    118              goal = top + ARM_MAX + r['gw'] + self.grasp_eps
  116    119              bad = max(0.0, need - goal)
  117    120              out.append((round(bad, 4), abs(cx - centre), float(cx)))
@@ -185,8 +188,9 @@ class GeneratedApproach:
  185    188          bx0, bx1, by1 = b
  186    189          d = np.maximum(np.maximum(bx0 - xs, 0.0), xs - bx1)
  187    190          out = np.where(d < R, by1 + np.sqrt(np.maximum(R * R - d * d, 0.0)), -1.0)
  188        -        g = (xs + r['gh'] / 2 > bx0) & (xs - r['gh'] / 2 < bx1)
  189        -        out = np.maximum(out, np.where(g, by1 + aj + r['gw'], -1.0))
         191 +        vm = VM if held is not None else 0.0
         192 +        g = (xs + r['gh'] / 2 + vm > bx0) & (xs - r['gh'] / 2 - vm < bx1)
         193 +        out = np.maximum(out, np.where(g, by1 + aj + r['gw'] + vm, -1.0))
  190    194          if held is not None:
  191    195              h = (xs + held['dx1'] > bx0) & (xs + held['dx0'] < bx1)
  192    196              out = np.maximum(out, np.where(h, by1 - held['dy0'], -1.0))
diff --git a/big_test.txt b/big_test.txt
new file mode 100644
index 0000000..f870ad2
--- /dev/null
+++ b/big_test.txt
@@ -0,0 +1,5 @@
           1 +(1072, 1, False, 1000, 13.5)
           2 +success 79 / 80 mean steps 46.675
           3 +success 80 / 80 mean steps 44.2875
           4 +(1038, 3, False, 1000, 65.5)
           5 +success 79 / 80 mean steps 58.7125
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..b2f950e
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,14 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seed=int(sys.argv[1]); oc=int(sys.argv[2]); T=int(sys.argv[3])
           5 +env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
           6 +obs, info = env.reset(seed=seed, options={'object_count':oc}); ap.reset(obs, info)
           7 +for t in range(T):
           8 +    a = ap.get_action(obs); obs, *_ = env.step(a)
           9 +r,rects = ap._parse(obs); ap.r=r
          10 +print(ap.phase, ap.task, ap.held)
          11 +print('robot', {k: round(v,3) for k,v in r.items()})
          12 +for k,v in sorted(rects.items()): print(k, {q: round(v[q],3) for q in ['x0','x1','y0','y1']})
          13 +print('need here', ap._clear_y_at(r['x'], rects, ap.held))
          14 +for n,o in rects.items(): print(n, ap._clear_y_at(r['x'], {n:o}, ap.held))
diff --git a/exp3.py b/exp3.py
new file mode 100644
index 0000000..c4d4fd3
--- /dev/null
+++ b/exp3.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +for gap in [0.0, 0.005, 0.01, 0.015, 0.02, 0.03, 0.05]:
           5 +    obs, info = env.reset(seed=0)
           6 +    R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
           7 +    def st(a):
           8 +        global obs
           9 +        obs,*_ = env.step(np.array(a,dtype=np.float32))
          10 +    st([0,0,0,0.1,0])
          11 +    top = obs.get(B,'y')+obs.get(B,'height'); tx = obs.get(B,'x')+obs.get(B,'width')/2
          12 +    gy = top + 0.21 + gap
          13 +    for i in range(40):
          14 +        st([np.clip(tx-obs.get(R,'x'),-.05,.05), np.clip(gy-obs.get(R,'y'),-.05,.05),0,0,0])
          15 +    y0 = obs.get(R,'y')
          16 +    st([0,0,0,0,1]); st([0,0.05,0,0,1])
          17 +    print(gap, round(y0-0.21-top,4), 'block y', round(obs.get(B,'y'),3))
          18 +env.close()
```

</details>

<a id="C009"></a>
### C009 · Fix premature grasp when arm not yet extended

Commit `3d23ca4cda6b71503a2dafc90477871cbac62da5`; parents: 634fc60717c8ad3f3331d779afc0fa4006ee15a5. Recorded author date: 2026-09-30T13:00:26+02:00.

File roles (automatic): policy.

- [E0284](01_timeline.md#E0284): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_3d23ca4_approach.py) · [Exact all-file diff](evidence/diffs/C009_3d23ca4.diff)

[Previous saved controller snapshot](evidence/versions/C008_634fc60_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 616bc89..9c84cc6 100644
--- a/approach.py
+++ b/approach.py
@@ -377,9 +377,7 @@ class GeneratedApproach:
  377    377  
  378    378          if self.phase == 'to_grasp':
  379    379              # recompute grasp height from current object
  380        -            gy = o['y1'] + r['aj'] + r['gw'] + self.grasp_eps
  381        -            if r['aj'] < ARM_MAX - 1e-6:
  382        -                gy = max(gy, r['y'])  # wait for arm to extend before going down much
         380 +            gy = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  383    381              if abs(r['x'] - task['gx']) < 1e-4 and abs(r['y'] - gy) < 1e-4 and r['aj'] >= ARM_MAX - 1e-6:
  384    382                  self.phase = 'grasp'
  385    383                  self.grasp_pose = (r['x'], r['y'], o['x'], o['y'])
```

</details>

<a id="C010"></a>
### C010 · Resolve grasp blockers (remove neighbors preventing top-down grasp first)

Commit `8dc1a43f48f539cd0672ec6b94d052cf896096ac`; parents: 3d23ca4cda6b71503a2dafc90477871cbac62da5. Recorded author date: 2026-09-30T13:13:03+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0309](01_timeline.md#E0309): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_8dc1a43_approach.py) · [Exact all-file diff](evidence/diffs/C010_8dc1a43.diff)

[Previous saved controller snapshot](evidence/versions/C009_3d23ca4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9c84cc6..b4a9f6d 100644
--- a/approach.py
+++ b/approach.py
@@ -296,6 +296,33 @@ class GeneratedApproach:
  296    296                  return best[1], best[2], gx, gy
  297    297          return None
  298    298  
         299 +    def _grasp_blockers(self, o, rects):
         300 +        """Names of objects preventing a top-down grasp of o (best offset)."""
         301 +        r = self.r
         302 +        goal = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
         303 +        best = None
         304 +        for cx in np.linspace(o['x0'] + 0.008, o['x1'] - 0.008, 21):
         305 +            if cx < WORLD_X[0] + r['R'] + 1e-3 or cx > WORLD_X[1] - r['R'] - 1e-3:
         306 +                continue
         307 +            bl = []
         308 +            for n, q in rects.items():
         309 +                if n == o['name']:
         310 +                    continue
         311 +                if self._clear_y_at(cx, {n: q}, None, ARM_MAX, vm=VM) > goal + 1e-6:
         312 +                    bl.append(n)
         313 +            if best is None or len(bl) < len(best):
         314 +                best = bl
         315 +                if not bl:
         316 +                    break
         317 +        return best or []
         318 +
         319 +    def _resolve(self, name, rects, depth=0):
         320 +        bl = self._grasp_blockers(rects[name], rects)
         321 +        if not bl or depth > 4:
         322 +            return name
         323 +        bl.sort(key=lambda n: -rects[n]['y1'])
         324 +        return self._resolve(bl[0], rects, depth + 1)
         325 +
  299    326      def _plan(self, rects):
  300    327          surf = None
  301    328          blk = None
@@ -306,16 +333,19 @@ class GeneratedApproach:
  306    333                  blk = o
  307    334          cands, held, gx, gy = self._place_candidates_target(blk, surf, rects)
  308    335          if not cands or cands[0][0] == 0:
  309        -            if cands:
  310        -                _, _, rx, ry, _ = cands[0]
  311        -            else:
  312        -                rx = (surf['x0'] + surf['x1']) / 2 - (held['dx0'] + held['dx1']) / 2
  313        -                ry = surf['y1'] + BOTTOM_OFF - held['dy0']
  314        -            return dict(obj=blk['name'], gx=gx, gy=gy, px=rx, py=ry, kind='target')
  315        -        blockers = cands[0][4]
  316        -        # remove the blocker closest to robot
  317        -        blockers = sorted(blockers, key=lambda n: abs((rects[n]['x0'] + rects[n]['x1']) / 2 - self.r['x']))
  318        -        name = blockers[0]
         336 +            name = self._resolve(blk['name'], rects)
         337 +            if name == blk['name']:
         338 +                if cands:
         339 +                    _, _, rx, ry, _ = cands[0]
         340 +                else:
         341 +                    rx = (surf['x0'] + surf['x1']) / 2 - (held['dx0'] + held['dx1']) / 2
         342 +                    ry = surf['y1'] + BOTTOM_OFF - held['dy0']
         343 +                return dict(obj=blk['name'], gx=gx, gy=gy, px=rx, py=ry, kind='target')
         344 +        else:
         345 +            blockers = cands[0][4]
         346 +            # remove the blocker closest to robot
         347 +            blockers = sorted(blockers, key=lambda n: abs((rects[n]['x0'] + rects[n]['x1']) / 2 - self.r['x']))
         348 +            name = self._resolve(blockers[0], rects)
  319    349          o = rects[name]
  320    350          spot = self._drop_spot(o, rects, surf, blk)
  321    351          if spot is None:
diff --git a/big_test.txt b/big_test.txt
index f870ad2..45069c7 100644
--- a/big_test.txt
+++ b/big_test.txt
@@ -1,5 +1,9 @@
    1        -(1072, 1, False, 1000, 13.5)
    2        -success 79 / 80 mean steps 46.675
    3        -success 80 / 80 mean steps 44.2875
    4        -(1038, 3, False, 1000, 65.5)
    5        -success 79 / 80 mean steps 58.7125
           1 +success 60 / 60 mean steps 21.15
           2 +success 60 / 60 mean steps 33.18333333333333
           3 +success 60 / 60 mean steps 48.75
           4 +(2049, 3, False, 1000, 62.1)
           5 +(2051, 3, False, 1000, 41.5)
           6 +success 58 / 60 mean steps 82.1
           7 + False, 1000, 197.2)
           8 +(1077, 4, False, 1000, 133.9)
           9 +success 76 / 80 mean steps 103.3625
```

</details>

<a id="C011"></a>
### C011 · Drop spots must not block other grasps or target placement

Commit `cb4c8c63f4bdc22081f1e3cfdd11c011d52413d3`; parents: 8dc1a43f48f539cd0672ec6b94d052cf896096ac. Recorded author date: 2026-09-30T13:13:42+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0340](01_timeline.md#E0340): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_cb4c8c6_approach.py) · [Exact all-file diff](evidence/diffs/C011_cb4c8c6.diff)

[Previous saved controller snapshot](evidence/versions/C010_8dc1a43_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b4a9f6d..e8e2eec 100644
--- a/approach.py
+++ b/approach.py
@@ -243,6 +243,18 @@ class GeneratedApproach:
  243    243              steps += 1
  244    244          return steps
  245    245  
         246 +    def _box_ok(self, bx, grasps, tplace):
         247 +        """Dropped box must not block grasps of other objects nor the target placement."""
         248 +        rs = {'_box': bx}
         249 +        for gx, gy in grasps:
         250 +            if self._clear_y_at(gx, rs, None, ARM_MAX, vm=VM) > gy - 1e-4:
         251 +                return False
         252 +        if tplace is not None:
         253 +            rx, ry, hb = tplace
         254 +            if self._clear_y_at(rx, rs, hb, ARM_MAX) > ry - 1e-4:
         255 +                return False
         256 +        return True
         257 +
  246    258      def _mk_held(self, o, gx, gy):
  247    259          return dict(name=o['name'], dx0=o['x0'] - gx, dx1=o['x1'] - gx,
  248    260                      dy0=o['y0'] - gy, dy1=o['y1'] - gy)
@@ -260,6 +272,14 @@ class GeneratedApproach:
  260    272              _, _, rxt, ryt, _ = cands[0]
  261    273          else:
  262    274              rxt, ryt = (surf['x0'] + surf['x1']) / 2, 0.5
         275 +        tplace = None
         276 +        if cands:
         277 +            tplace = (cands[0][2], cands[0][3], held_b)
         278 +        grasps = []
         279 +        for k, q in others.items():
         280 +            if q['type'] == 'target_surface':
         281 +                continue
         282 +            grasps.append((self._grasp_x(q, others), q['y1'] + ARM_MAX + r['gw'] + self.grasp_eps))
  263    283          P1 = self._profile(xs, others, held)
  264    284          P2 = self._profile(xs, others, None)
  265    285          P3 = self._profile(xs, {k: v for k, v in others.items() if k != blk['name']}, held_b)
@@ -291,7 +311,9 @@ class GeneratedApproach:
  291    311                      c3 = self._est(gxb, gyb, rxt, ryt, P3n)
  292    312                      cost = c1 + c2 + c3 + 0.01 * (ry - ry_low)
  293    313                      if best is None or cost < best[0]:
  294        -                        best = (cost, rx, ry)
         314 +                        bx = dict(x0=x0, x1=x1, y1=ry + held['dy1'], name='_box')
         315 +                        if self._box_ok(bx, grasps, tplace):
         316 +                            best = (cost, rx, ry)
  295    317              if best is not None:
  296    318                  return best[1], best[2], gx, gy
  297    319          return None
diff --git a/big_test.txt b/big_test.txt
index 45069c7..c9bf6dc 100644
--- a/big_test.txt
+++ b/big_test.txt
@@ -4,6 +4,6 @@ success 60 / 60 mean steps 48.75
    4      4  (2049, 3, False, 1000, 62.1)
    5      5  (2051, 3, False, 1000, 41.5)
    6      6  success 58 / 60 mean steps 82.1
    7        - False, 1000, 197.2)
    8        -(1077, 4, False, 1000, 133.9)
    9        -success 76 / 80 mean steps 103.3625
           7 +(2021, 4, False, 1000, 71.3)
           8 +(2024, 4, False, 1000, 78.7)
           9 +success 58 / 60 mean steps 86.53333333333333
```

</details>

<a id="C012"></a>
### C012 · Grasp overhang, spread grasp offsets by x, drop-spot check keeps target placement feasible

Commit `f4dbcaec8ab192c97e9a8f722905401b492cc0d0`; parents: cb4c8c63f4bdc22081f1e3cfdd11c011d52413d3. Recorded author date: 2026-09-30T13:25:02+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0399](01_timeline.md#E0399): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_f4dbcae_approach.py) · [Exact all-file diff](evidence/diffs/C012_f4dbcae.diff)

[Previous saved controller snapshot](evidence/versions/C011_cb4c8c6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e8e2eec..0c4809e 100644
--- a/approach.py
+++ b/approach.py
@@ -6,6 +6,7 @@ MAXD = 0.05
    6      6  ARM_MAX = 0.2
    7      7  EARLY = True
    8      8  BOTTOM_OFF = 0.018
           9 +GOFF = 0.022  # gripper centre may overhang object edge by this much
    9     10  VM = 0.025  # keep gripper this far from non-held objects while vacuum is on
   10     11  
   11     12  
@@ -108,7 +109,7 @@ class GeneratedApproach:
  108    109          """Candidate robot x's to grasp object o from above, best first (only collision-free ones if any)."""
  109    110          r = self.r
  110    111          top = o['y1']
  111        -        cands = np.linspace(o['x0'] + 0.008, o['x1'] - 0.008, 21)
         112 +        cands = np.linspace(o['x0'] - GOFF, o['x1'] + GOFF, 25)
  112    113          centre = (o['x0'] + o['x1']) / 2
  113    114          out = []
  114    115          for cx in cands:
@@ -127,15 +128,16 @@ class GeneratedApproach:
  127    128      def _grasp_x(self, o, rects):
  128    129          return self._grasp_xs(o, rects)[0]
  129    130  
  130        -    def _place_candidates_target(self, blk, surf, rects):
         131 +    def _place_candidates_target(self, blk, surf, rects, fast=False):
  131    132          """Return (list of (n_blockers, cost, rx, ry, blockers), held, gx, gy)."""
  132    133          r = self.r
  133    134          gxs = self._grasp_xs(blk, rects)
  134    135          centre_g = (blk['x0'] + blk['x1']) / 2
  135    136          # a handful of grasp offsets: best one, then spread
  136        -        if len(gxs) > 5:
  137        -            idx = np.linspace(0, len(gxs) - 1, 5).astype(int)
  138        -            gxs = [gxs[0]] + [gxs[i] for i in idx]
         137 +        if len(gxs) > 7:
         138 +            sx = sorted(gxs)
         139 +            idx = np.linspace(0, len(sx) - 1, 7).astype(int)
         140 +            gxs = [gxs[0]] + [sx[i] for i in idx]
  139    141          bw = blk['x1'] - blk['x0']
  140    142          m = 0.004
  141    143          lo = surf['x0'] + m
@@ -147,13 +149,17 @@ class GeneratedApproach:
  147    149          best = None
  148    150          others = [(n, o) for n, o in rects.items()
  149    151                    if o['type'] != 'target_surface' and n != blk['name']]
  150        -        PA = self._profile(self.xs, rects, None)
         152 +        PA = None if fast else self._profile(self.xs, rects, None)
  151    153          for gi, gx in enumerate(gxs):
  152    154              gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  153    155              held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx,
  154    156                          dy0=blk['y0'] - gy, dy1=blk['y1'] - gy)
  155        -            cA = self._est(r['x'], r['y'], gx, gy, PA)
  156        -            PB = self._profile(self.xs, {n: o for n, o in others}, held)
         157 +            if fast:
         158 +                cA = 0
         159 +                PB = None
         160 +            else:
         161 +                cA = self._est(r['x'], r['y'], gx, gy, PA)
         162 +                PB = self._profile(self.xs, {n: o for n, o in others}, held)
  157    163              bottom = surf['y1'] + BOTTOM_OFF
  158    164              ry = bottom - held['dy0']
  159    165              res = []
@@ -166,7 +172,7 @@ class GeneratedApproach:
  166    172                      need = self._clear_y_at(rx, {name: o}, held, ARM_MAX)
  167    173                      if need > ry - 1e-4:
  168    174                          blockers.append(name)
  169        -                cost = cA + self._est(gx, gy, rx, ry, PB) + abs(px - centre) * 0.1 + 0.001 * gi
         175 +                cost = (cA + self._est(gx, gy, rx, ry, PB) if not fast else 0) + abs(px - centre) * 0.1 + 0.001 * gi
  170    176                  res.append((len(blockers), cost, rx, ry, blockers))
  171    177              if not res:
  172    178                  continue
@@ -250,8 +256,11 @@ class GeneratedApproach:
  250    256              if self._clear_y_at(gx, rs, None, ARM_MAX, vm=VM) > gy - 1e-4:
  251    257                  return False
  252    258          if tplace is not None:
  253        -            rx, ry, hb = tplace
  254        -            if self._clear_y_at(rx, rs, hb, ARM_MAX) > ry - 1e-4:
         259 +            blk, surf, others, nb = tplace
         260 +            r2 = dict(others)
         261 +            r2['_box'] = bx
         262 +            c2 = self._place_candidates_target(blk, surf, r2, fast=True)[0]
         263 +            if not c2 or c2[0][0] > nb:
  255    264                  return False
  256    265          return True
  257    266  
@@ -272,9 +281,7 @@ class GeneratedApproach:
  272    281              _, _, rxt, ryt, _ = cands[0]
  273    282          else:
  274    283              rxt, ryt = (surf['x0'] + surf['x1']) / 2, 0.5
  275        -        tplace = None
  276        -        if cands:
  277        -            tplace = (cands[0][2], cands[0][3], held_b)
         284 +        tplace = (blk, surf, others, cands[0][0] if cands else 99)
  278    285          grasps = []
  279    286          for k, q in others.items():
  280    287              if q['type'] == 'target_surface':
@@ -311,7 +318,7 @@ class GeneratedApproach:
  311    318                      c3 = self._est(gxb, gyb, rxt, ryt, P3n)
  312    319                      cost = c1 + c2 + c3 + 0.01 * (ry - ry_low)
  313    320                      if best is None or cost < best[0]:
  314        -                        bx = dict(x0=x0, x1=x1, y1=ry + held['dy1'], name='_box')
         321 +                        bx = dict(x0=x0, x1=x1, y0=ry + held['dy0'], y1=ry + held['dy1'], name='_box', type='rectangle')
  315    322                          if self._box_ok(bx, grasps, tplace):
  316    323                              best = (cost, rx, ry)
  317    324              if best is not None:
@@ -323,7 +330,7 @@ class GeneratedApproach:
  323    330          r = self.r
  324    331          goal = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  325    332          best = None
  326        -        for cx in np.linspace(o['x0'] + 0.008, o['x1'] - 0.008, 21):
         333 +        for cx in np.linspace(o['x0'] - GOFF, o['x1'] + GOFF, 25):
  327    334              if cx < WORLD_X[0] + r['R'] + 1e-3 or cx > WORLD_X[1] - r['R'] - 1e-3:
  328    335                  continue
  329    336              bl = []
diff --git a/big_test2.txt b/big_test2.txt
new file mode 100644
index 0000000..bd2fa2d
--- /dev/null
+++ b/big_test2.txt
@@ -0,0 +1,5 @@
           1 +(3038, 3, False, 1000, 73.0)
           2 +success 79 / 80 mean steps 60.3125
           3 +(3057, 4, False, 1000, 99.3)
           4 +success 79 / 80 mean steps 70.1
           5 +success 100 / 100 mean steps 32.53
diff --git a/dbg4.py b/dbg4.py
new file mode 100644
index 0000000..b41f208
--- /dev/null
+++ b/dbg4.py
@@ -0,0 +1,13 @@
           1 +import numpy as np, sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env()
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           6 +obs, info = env.reset(seed=int(sys.argv[1]), options={'object_count':int(sys.argv[2])})
           7 +ap.reset(obs, info)
           8 +r, rects = ap._parse(obs); ap.r = r
           9 +blk=rects['target_block']; surf=rects['target_surface']
          10 +print(ap._grasp_xs(blk, rects))
          11 +c, held, gx, gy = ap._place_candidates_target(blk, surf, rects)
          12 +print(len(c), c[:3], gx)
          13 +print(ap._plan(rects))
diff --git a/exp4.py b/exp4.py
new file mode 100644
index 0000000..0023008
--- /dev/null
+++ b/exp4.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +for off in [0.0, 0.02, 0.03, 0.034, 0.04]:
           5 +    obs, info = env.reset(seed=0)
           6 +    R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
           7 +    def st(a):
           8 +        global obs
           9 +        obs,*_ = env.step(np.array(a,dtype=np.float32))
          10 +    st([0,0,0,0.1,0])
          11 +    top = obs.get(B,'y')+obs.get(B,'height'); tx = obs.get(B,'x') - off
          12 +    gy = top + 0.21 + 0.002
          13 +    for i in range(40):
          14 +        st([np.clip(tx-obs.get(R,'x'),-.05,.05), np.clip(gy-obs.get(R,'y'),-.05,.05),0,0,0])
          15 +    st([0,0,0,0,1]); st([0,0.05,0,0,1])
          16 +    print(off, 'block y', round(obs.get(B,'y'),3), round(obs.get(R,'y')-gy,3))
          17 +env.close()
```

</details>

<a id="C013"></a>
### C013 · Drop-spot search over grasp offsets incl. approach cost; bottom offset 0.021

Commit `2e88eb5f3ef644ac34dd7c59de79747345bd3aac`; parents: f4dbcaec8ab192c97e9a8f722905401b492cc0d0. Recorded author date: 2026-09-30T13:48:46+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0471](01_timeline.md#E0471): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_2e88eb5_approach.py) · [Exact all-file diff](evidence/diffs/C013_2e88eb5.diff)

[Previous saved controller snapshot](evidence/versions/C012_f4dbcae_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0c4809e..95168a4 100644
--- a/approach.py
+++ b/approach.py
@@ -5,7 +5,7 @@ WORLD_Y = (0.0, 1.0)
    5      5  MAXD = 0.05
    6      6  ARM_MAX = 0.2
    7      7  EARLY = True
    8        -BOTTOM_OFF = 0.018
           8 +BOTTOM_OFF = 0.021
    9      9  GOFF = 0.022  # gripper centre may overhang object edge by this much
   10     10  VM = 0.025  # keep gripper this far from non-held objects while vacuum is on
   11     11  
@@ -271,9 +271,6 @@ class GeneratedApproach:
  271    271      def _drop_spot(self, o, rects, surf, blk):
  272    272          r = self.r
  273    273          xs = self.xs
  274        -        gx = self._grasp_x(o, rects)
  275        -        gy = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
  276        -        held = self._mk_held(o, gx, gy)
  277    274          others = {k: v for k, v in rects.items() if k != o['name']}
  278    275          # target plan assuming o removed
  279    276          cands, held_b, gxb, gyb = self._place_candidates_target(blk, surf, others)
@@ -287,42 +284,57 @@ class GeneratedApproach:
  287    284              if q['type'] == 'target_surface':
  288    285                  continue
  289    286              grasps.append((self._grasp_x(q, others), q['y1'] + ARM_MAX + r['gw'] + self.grasp_eps))
  290        -        P1 = self._profile(xs, others, held)
         287 +        P0 = self._profile(xs, rects, None)
  291    288          P2 = self._profile(xs, others, None)
  292    289          P3 = self._profile(xs, {k: v for k, v in others.items() if k != blk['name']}, held_b)
  293    290          ymax = WORLD_Y[1] - r['R'] - 0.002
  294        -        best = None
         291 +        gy = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
         292 +        gl = self._grasp_xs(o, rects)
         293 +        gcands = []
         294 +        for g in (gl[0], min(gl), max(gl)):
         295 +            if all(abs(g - q) > 1e-4 for q in gcands):
         296 +                gcands.append(g)
         297 +        cache = {}
  295    298          for margin in (0.03, 0.01):
  296        -            for rx in xs[::2]:
  297        -                if rx < WORLD_X[0] + r['R'] + 0.002 or rx > WORLD_X[1] - r['R'] - 0.002:
  298        -                    continue
  299        -                x0, x1 = rx + held['dx0'], rx + held['dx1']
  300        -                if x0 < WORLD_X[0] or x1 > WORLD_X[1]:
  301        -                    continue
  302        -                if x1 > surf['x0'] - margin and x0 < surf['x1'] + margin:
  303        -                    continue
  304        -                ok = True
  305        -                for k, v in others.items():
  306        -                    if x1 > v['x0'] - margin and x0 < v['x1'] + margin:
  307        -                        ok = False
  308        -                        break
  309        -                if not ok:
  310        -                    continue
  311        -                ry_low = max(gy + 0.003, P1[self._xi(rx)] + 0.004)
  312        -                for ry in np.arange(ry_low, ymax, 0.05)[:5]:
  313        -                    c1 = self._est(gx, gy, rx, ry, P1)
  314        -                    box = (x0, x1, ry + held['dy1'])
  315        -                    P2n = np.maximum(P2, self._colprof(xs, box, None))
  316        -                    c2 = self._est(rx, ry, gxb, gyb, P2n)
  317        -                    P3n = np.maximum(P3, self._colprof(xs, box, held_b))
  318        -                    c3 = self._est(gxb, gyb, rxt, ryt, P3n)
  319        -                    cost = c1 + c2 + c3 + 0.01 * (ry - ry_low)
  320        -                    if best is None or cost < best[0]:
  321        -                        bx = dict(x0=x0, x1=x1, y0=ry + held['dy0'], y1=ry + held['dy1'], name='_box', type='rectangle')
  322        -                        if self._box_ok(bx, grasps, tplace):
  323        -                            best = (cost, rx, ry)
         299 +            best = None
         300 +            for gx in gcands:
         301 +                held = self._mk_held(o, gx, gy)
         302 +                c0 = self._est(r['x'], r['y'], gx, gy, P0, margin=0.0)
         303 +                P1 = self._profile(xs, others, held)
         304 +                for rx in xs[::2]:
         305 +                    if rx < WORLD_X[0] + r['R'] + 0.002 or rx > WORLD_X[1] - r['R'] - 0.002:
         306 +                        continue
         307 +                    x0, x1 = rx + held['dx0'], rx + held['dx1']
         308 +                    if x0 < WORLD_X[0] or x1 > WORLD_X[1]:
         309 +                        continue
         310 +                    if x1 > surf['x0'] - margin and x0 < surf['x1'] + margin:
         311 +                        continue
         312 +                    ok = True
         313 +                    for k, v in others.items():
         314 +                        if x1 > v['x0'] - margin and x0 < v['x1'] + margin:
         315 +                            ok = False
         316 +                            break
         317 +                    if not ok:
         318 +                        continue
         319 +                    ry_low = max(gy + 0.003, P1[self._xi(rx)] + 0.004)
         320 +                    for ry in np.arange(ry_low, ymax, 0.05)[:5]:
         321 +                        c1 = self._est(gx, gy, rx, ry, P1)
         322 +                        box = (x0, x1, ry + held['dy1'])
         323 +                        P2n = np.maximum(P2, self._colprof(xs, box, None))
         324 +                        c2 = self._est(rx, ry, gxb, gyb, P2n)
         325 +                        P3n = np.maximum(P3, self._colprof(xs, box, held_b))
         326 +                        c3 = self._est(gxb, gyb, rxt, ryt, P3n)
         327 +                        cost = c0 + c1 + c2 + c3 + 0.01 * (ry - ry_low) + 0.001 * abs(gx - gl[0])
         328 +                        if best is None or cost < best[0]:
         329 +                            bx = dict(x0=x0, x1=x1, y0=ry + held['dy0'], y1=ry + held['dy1'],
         330 +                                      name='_box', type='rectangle')
         331 +                            key = (round(x0, 4), round(bx['y1'], 4))
         332 +                            if key not in cache:
         333 +                                cache[key] = self._box_ok(bx, grasps, tplace)
         334 +                            if cache[key]:
         335 +                                best = (cost, rx, ry, gx)
  324    336              if best is not None:
  325        -                return best[1], best[2], gx, gy
         337 +                return best[1], best[2], best[3], gy
  326    338          return None
  327    339  
  328    340      def _grasp_blockers(self, o, rects):
diff --git a/big_test2.txt b/big_test2.txt
index bd2fa2d..9740bb6 100644
--- a/big_test2.txt
+++ b/big_test2.txt
@@ -1,5 +1,3 @@
    1        -(3038, 3, False, 1000, 73.0)
    2        -success 79 / 80 mean steps 60.3125
    3        -(3057, 4, False, 1000, 99.3)
    4        -success 79 / 80 mean steps 70.1
    5        -success 100 / 100 mean steps 32.53
           1 +success 80 / 80 mean steps 47.25
           2 +success 80 / 80 mean steps 57.3
           3 +success 100 / 100 mean steps 32.14
diff --git a/big_test3.txt b/big_test3.txt
new file mode 100644
index 0000000..a69dfdf
--- /dev/null
+++ b/big_test3.txt
@@ -0,0 +1,6 @@
           1 +max compute 2.59
           2 +success 200 / 200 mean steps 32.435
           3 +max compute 1.15
           4 +success 100 / 100 mean steps 52.73
           5 +max compute 2.61
           6 +success 100 / 100 mean steps 47.32
diff --git a/test_approach.py b/test_approach.py
index 5dd1163..9bb08e6 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -10,14 +10,14 @@ def run(seed):
   10     10      ap = GeneratedApproach(env.action_space, env.observation_space, {})
   11     11      obs, info = env.reset(seed=seed, options=({'object_count':OC} if OC is not None else None))
   12     12      ap.reset(obs, info)
   13        -    tot = 0; t0 = time.time()
          13 +    tot = 0; t0 = time.time(); ct = 0
   14     14      for t in range(env.max_steps):
   15        -        a = ap.get_action(obs)
          15 +        tc=time.time(); a = ap.get_action(obs); ct += time.time()-tc
   16     16          obs, r, term, trunc, info2 = env.step(a)
   17     17          tot += r
   18     18          if term or trunc: break
   19     19      env.close()
   20        -    return seed, info.get('object_count'), term, t+1, round(time.time()-t0,1)
          20 +    return seed, info.get('object_count'), term, t+1, round(time.time()-t0,1), round(ct,2)
   21     21  
   22     22  if __name__ == '__main__':
   23     23      a, b = int(sys.argv[1]), int(sys.argv[2])
@@ -26,4 +26,4 @@ if __name__ == '__main__':
   26     26          res = list(ex.map(run, range(a, b)))
   27     27      for r in res:
   28     28          if not r[2] or len(res)<20: print(r)
   29        -    print('success', sum(r[2] for r in res), '/', len(res), 'mean steps', np.mean([r[3] for r in res]))
          29 +    print('max compute', max(r[5] for r in res)); print('success', sum(r[2] for r in res), '/', len(res), 'mean steps', np.mean([r[3] for r in res]))
```

</details>

<a id="C014"></a>
### C014 · grasp_eps 0.007

Commit `deae307cb70a4e80c83243b471672b09f1d49a67`; parents: 2e88eb5f3ef644ac34dd7c59de79747345bd3aac. Recorded author date: 2026-09-30T14:03:55+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0502](01_timeline.md#E0502): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_deae307_approach.py) · [Exact all-file diff](evidence/diffs/C014_deae307.diff)

[Previous saved controller snapshot](evidence/versions/C013_2e88eb5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 95168a4..07b756e 100644
--- a/approach.py
+++ b/approach.py
@@ -96,7 +96,7 @@ class GeneratedApproach:
   96     96          self.held = None
   97     97          self.stuck = 0
   98     98          self.last_pos = None
   99        -        self.grasp_eps = 0.002
          99 +        self.grasp_eps = 0.007
  100    100          self.fail_count = {}
  101    101          self.t = 0
  102    102  
diff --git a/prof.out b/prof.out
new file mode 100644
index 0000000..da3cc74
Binary files /dev/null and b/prof.out differ
diff --git a/prof.py b/prof.py
new file mode 100644
index 0000000..10e4e1a
--- /dev/null
+++ b/prof.py
@@ -0,0 +1,12 @@
           1 +import cProfile, pstats, sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
           5 +obs, info = env.reset(seed=int(sys.argv[1])); ap.reset(obs, info)
           6 +def run():
           7 +    global obs
           8 +    for t in range(200):
           9 +        a = ap.get_action(obs); obs, r, term, *_ = env.step(a)
          10 +        if term: break
          11 +cProfile.run('run()', 'prof.out')
          12 +pstats.Stats('prof.out').sort_stats('cumulative').print_stats(15)
diff --git a/test_approach.py b/test_approach.py
index 9bb08e6..5b3c1f1 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -25,5 +25,5 @@ if __name__ == '__main__':
   25     25      with ThreadPoolExecutor(8) as ex:
   26     26          res = list(ex.map(run, range(a, b)))
   27     27      for r in res:
   28        -        if not r[2] or len(res)<20: print(r)
          28 +        if not r[2] or len(res)<20 or r[5] > 3: print(r)
   29     29      print('max compute', max(r[5] for r in res)); print('success', sum(r[2] for r in res), '/', len(res), 'mean steps', np.mean([r[3] for r in res]))
```

</details>

<a id="C015"></a>
### C015 · keep VM 0.025; add analysis scripts

Commit `3bd283d9df3563ce11c34b30b89d753a8ad61b1c`; parents: deae307cb70a4e80c83243b471672b09f1d49a67. Recorded author date: 2026-09-30T14:18:07+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0626](01_timeline.md#E0626): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C015_3bd283d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/big_test4.txt b/big_test4.txt
new file mode 100644
index 0000000..f355903
--- /dev/null
+++ b/big_test4.txt
@@ -0,0 +1,4 @@
           1 +max compute 16.48
           2 +success 200 / 200 mean steps 28.57
           3 +max compute 1.72
           4 +success 100 / 100 mean steps 47.22
diff --git a/cnt.py b/cnt.py
new file mode 100644
index 0000000..11358ac
--- /dev/null
+++ b/cnt.py
@@ -0,0 +1,17 @@
           1 +import numpy as np, sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env()
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           6 +multi=0; tot=0
           7 +for seed in range(6000, 6060):
           8 +    obs, info = env.reset(seed=seed, options={'object_count':int(sys.argv[1])})
           9 +    ap.reset(obs, info)
          10 +    r, rects = ap._parse(obs); ap.r = r
          11 +    blk=rects['target_block']; surf=rects['target_surface']
          12 +    c, held, gx, gy = ap._place_candidates_target(blk, surf, rects)
          13 +    k = c[0][0]
          14 +    sets = set(tuple(sorted(x[4])) for x in c if x[0]==k)
          15 +    tot+=1; multi += len(sets)>1
          16 +    if len(sets)>1: print(seed, k, sets)
          17 +print(multi, tot)
```

</details>

<a id="C016"></a>
### C016 · Drop-spot: next-leg to next blocker, margins merged with penalty

Commit `0ce09243c59c82d7eee86dfb3a306224ea1b226f`; parents: 3bd283d9df3563ce11c34b30b89d753a8ad61b1c. Recorded author date: 2026-09-30T14:25:12+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0667](01_timeline.md#E0667): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_0ce0924_approach.py) · [Exact all-file diff](evidence/diffs/C016_0ce0924.diff)

[Previous saved controller snapshot](evidence/versions/C014_deae307_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 07b756e..be42595 100644
--- a/approach.py
+++ b/approach.py
@@ -268,7 +268,7 @@ class GeneratedApproach:
  268    268          return dict(name=o['name'], dx0=o['x0'] - gx, dx1=o['x1'] - gx,
  269    269                      dy0=o['y0'] - gy, dy1=o['y1'] - gy)
  270    270  
  271        -    def _drop_spot(self, o, rects, surf, blk):
         271 +    def _drop_spot(self, o, rects, surf, blk, nxt=None):
  272    272          r = self.r
  273    273          xs = self.xs
  274    274          others = {k: v for k, v in rects.items() if k != o['name']}
@@ -295,8 +295,8 @@ class GeneratedApproach:
  295    295              if all(abs(g - q) > 1e-4 for q in gcands):
  296    296                  gcands.append(g)
  297    297          cache = {}
  298        -        for margin in (0.03, 0.01):
  299        -            best = None
         298 +        best = None
         299 +        for margin, pen in ((0.03, 0.0), (0.01, 1.0)):
  300    300              for gx in gcands:
  301    301                  held = self._mk_held(o, gx, gy)
  302    302                  c0 = self._est(r['x'], r['y'], gx, gy, P0, margin=0.0)
@@ -307,24 +307,22 @@ class GeneratedApproach:
  307    307                      x0, x1 = rx + held['dx0'], rx + held['dx1']
  308    308                      if x0 < WORLD_X[0] or x1 > WORLD_X[1]:
  309    309                          continue
  310        -                    if x1 > surf['x0'] - margin and x0 < surf['x1'] + margin:
  311        -                        continue
  312        -                    ok = True
  313        -                    for k, v in others.items():
  314        -                        if x1 > v['x0'] - margin and x0 < v['x1'] + margin:
  315        -                            ok = False
  316        -                            break
  317        -                    if not ok:
         310 +                    if not self._free(x0, x1, margin, surf, others):
  318    311                          continue
         312 +                    if pen > 0 and self._free(x0, x1, 0.03, surf, others):
         313 +                        continue  # already evaluated with the larger margin
  319    314                      ry_low = max(gy + 0.003, P1[self._xi(rx)] + 0.004)
  320    315                      for ry in np.arange(ry_low, ymax, 0.05)[:5]:
  321    316                          c1 = self._est(gx, gy, rx, ry, P1)
  322    317                          box = (x0, x1, ry + held['dy1'])
  323    318                          P2n = np.maximum(P2, self._colprof(xs, box, None))
  324        -                        c2 = self._est(rx, ry, gxb, gyb, P2n)
         319 +                        if nxt is not None:
         320 +                            c2 = self._est(rx, ry, nxt[0], nxt[1], P2n)
         321 +                        else:
         322 +                            c2 = self._est(rx, ry, gxb, gyb, P2n)
  325    323                          P3n = np.maximum(P3, self._colprof(xs, box, held_b))
  326    324                          c3 = self._est(gxb, gyb, rxt, ryt, P3n)
  327        -                        cost = c0 + c1 + c2 + c3 + 0.01 * (ry - ry_low) + 0.001 * abs(gx - gl[0])
         325 +                        cost = c0 + c1 + c2 + c3 + pen + 0.01 * (ry - ry_low) + 0.001 * abs(gx - gl[0])
  328    326                          if best is None or cost < best[0]:
  329    327                              bx = dict(x0=x0, x1=x1, y0=ry + held['dy0'], y1=ry + held['dy1'],
  330    328                                        name='_box', type='rectangle')
@@ -333,10 +331,19 @@ class GeneratedApproach:
  333    331                                  cache[key] = self._box_ok(bx, grasps, tplace)
  334    332                              if cache[key]:
  335    333                                  best = (cost, rx, ry, gx)
  336        -            if best is not None:
  337        -                return best[1], best[2], best[3], gy
         334 +        if best is not None:
         335 +            return best[1], best[2], best[3], gy
  338    336          return None
  339    337  
         338 +    @staticmethod
         339 +    def _free(x0, x1, margin, surf, others):
         340 +        if x1 > surf['x0'] - margin and x0 < surf['x1'] + margin:
         341 +            return False
         342 +        for v in others.values():
         343 +            if x1 > v['x0'] - margin and x0 < v['x1'] + margin:
         344 +                return False
         345 +        return True
         346 +
  340    347      def _grasp_blockers(self, o, rects):
  341    348          """Names of objects preventing a top-down grasp of o (best offset)."""
  342    349          r = self.r
@@ -373,6 +380,7 @@ class GeneratedApproach:
  373    380              elif o['type'] == 'target_block':
  374    381                  blk = o
  375    382          cands, held, gx, gy = self._place_candidates_target(blk, surf, rects)
         383 +        nxt = None
  376    384          if not cands or cands[0][0] == 0:
  377    385              name = self._resolve(blk['name'], rects)
  378    386              if name == blk['name']:
@@ -387,8 +395,12 @@ class GeneratedApproach:
  387    395              # remove the blocker closest to robot
  388    396              blockers = sorted(blockers, key=lambda n: abs((rects[n]['x0'] + rects[n]['x1']) / 2 - self.r['x']))
  389    397              name = self._resolve(blockers[0], rects)
         398 +            rest = [n for n in blockers if n != name]
         399 +            if rest:
         400 +                q = rects[rest[0]]
         401 +                nxt = (self._grasp_x(q, rects), q['y1'] + ARM_MAX + self.r['gw'] + self.grasp_eps)
  390    402          o = rects[name]
  391        -        spot = self._drop_spot(o, rects, surf, blk)
         403 +        spot = self._drop_spot(o, rects, surf, blk, nxt)
  392    404          if spot is None:
  393    405              rx = WORLD_X[0] + 0.15 if (o['x0'] > 0.8) else WORLD_X[1] - 0.15
  394    406              gxx = self._grasp_x(o, rects)
diff --git a/test_approach.py b/test_approach.py
index 5b3c1f1..c42539c 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -25,5 +25,5 @@ if __name__ == '__main__':
   25     25      with ThreadPoolExecutor(8) as ex:
   26     26          res = list(ex.map(run, range(a, b)))
   27     27      for r in res:
   28        -        if not r[2] or len(res)<20 or r[5] > 3: print(r)
          28 +        if not r[2] or len(res)<20 or r[3] > 90: print(r)
   29     29      print('max compute', max(r[5] for r in res)); print('success', sum(r[2] for r in res), '/', len(res), 'mean steps', np.mean([r[3] for r in res]))
```

</details>

<a id="C017"></a>
### C017 · Time guard in drop-spot search

Commit `320dd7d33d70ac9b0f153039a15eb561ddf1677b`; parents: 0ce09243c59c82d7eee86dfb3a306224ea1b226f. Recorded author date: 2026-09-30T14:39:46+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0697](01_timeline.md#E0697): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_320dd7d_approach.py) · [Exact all-file diff](evidence/diffs/C017_320dd7d.diff)

[Previous saved controller snapshot](evidence/versions/C016_0ce0924_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index be42595..43d8701 100644
--- a/approach.py
+++ b/approach.py
@@ -1,3 +1,4 @@
           1 +import time
    1      2  import numpy as np
    2      3  
    3      4  WORLD_X = (0.0, 1.618)
@@ -296,8 +297,11 @@ class GeneratedApproach:
  296    297                  gcands.append(g)
  297    298          cache = {}
  298    299          best = None
         300 +        t_start = time.time()
  299    301          for margin, pen in ((0.03, 0.0), (0.01, 1.0)):
  300    302              for gx in gcands:
         303 +                if best is not None and time.time() - t_start > 3.0:
         304 +                    break
  301    305                  held = self._mk_held(o, gx, gy)
  302    306                  c0 = self._est(r['x'], r['y'], gx, gy, P0, margin=0.0)
  303    307                  P1 = self._profile(xs, others, held)
diff --git a/prof.out b/prof.out
index da3cc74..9c6dc0d 100644
Binary files a/prof.out and b/prof.out differ
diff --git a/test_approach.py b/test_approach.py
index c42539c..ac17ecb 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -25,5 +25,5 @@ if __name__ == '__main__':
   25     25      with ThreadPoolExecutor(8) as ex:
   26     26          res = list(ex.map(run, range(a, b)))
   27     27      for r in res:
   28        -        if not r[2] or len(res)<20 or r[3] > 90: print(r)
          28 +        if not r[2] or len(res)<20 or r[5] > 6: print(r)
   29     29      print('max compute', max(r[5] for r in res)); print('success', sum(r[2] for r in res), '/', len(res), 'mean steps', np.mean([r[3] for r in res]))
```

</details>

