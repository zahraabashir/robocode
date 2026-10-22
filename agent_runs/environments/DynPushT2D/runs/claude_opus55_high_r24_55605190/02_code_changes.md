# DynPushT2D · claude-opus-5-5 · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `56b6024` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `b7366c0` | Greedy model-based push planner v1 | approach.py, dyn_fit.py, dyn_fit2.py, dyn_fric.py, dyn_fric2.py, dyn_gap.py, dyn_lib.py, dyn_model.py, dyn_obs.py, dyn_probe.py, dyn_push.py, dyn_push2.py, dyn_q45.py, dyn_validat… | [E0239](01_timeline.md#E0239) |
| [C003](#C003) · `aaedd14` | Better retreat from contact, relaxed start clearance, fallback move | approach.py, dbg.py | [E0289](01_timeline.md#E0289) |
| [C004](#C004) · `6bf1355` | Relative wall bounds when block starts near a wall | approach.py, res_100_300.txt, test_list.py | [E0311](01_timeline.md#E0311) |
| [C005](#C005) · `1dcac36` | results | res_300_600.txt | [E0327](01_timeline.md#E0327), [E0334](01_timeline.md#E0334), [E0407](01_timeline.md#E0407), [E0644](01_timeline.md#E0644) |
| [C006](#C006) · `49bdb1d` | Diagonal-speed pushes, longer push horizon | approach.py, stats.py | [E0334](01_timeline.md#E0334) |
| [C007](#C007) · `ac79154` | Hinge cost with success-region margins | approach.py | [E0344](01_timeline.md#E0344) |
| [C008](#C008) · `3c76c01` | Unwrapped angle success interval; tighten margins on stall | approach.py, stats.py | [E0366](01_timeline.md#E0366) |
| [C009](#C009) · `8950f03` | Configurable scoring modes | approach.py, res_600_800.txt, sweep.py | [E0407](01_timeline.md#E0407) |
| [C010](#C010) · `9cfce52` | Tuned angle weight 2.2; more config attrs | approach.py | [E0436](01_timeline.md#E0436) |
| [C011](#C011) · `42cff16` | Contact continuation candidates and optional mid-push replanning | approach.py | [E0473](01_timeline.md#E0473) |
| [C012](#C012) · `b644810` | REPLAN_K=10 | approach.py | [E0476](01_timeline.md#E0476) |
| [C013](#C013) · `f5b0c56` | 2-step lookahead (LOOK=8) | approach.py, timeit_plan.py | [E0528](01_timeline.md#E0528) |
| [C014](#C014) · `b1a7b71` | Time budget guard and exception safety | approach.py | [E0558](01_timeline.md#E0558) |
| [C015](#C015) · `159e97d` | fix indentation | approach.py, res_1000.txt | [E0586](01_timeline.md#E0586) |
| [C016](#C016) · `b52486c` | results 1000-1300: 300/300 | res_1000.txt | [E0644](01_timeline.md#E0644) |
| [C017](#C017) · `c6a9370` | Exception safety in get_action | approach.py, dbg.py, sw_ANGW1.6.txt, sw_ANGW3.0.txt, sw_REPLANK15.txt, sw_REPLANK6.txt | [E0729](01_timeline.md#E0729) |
| [C018](#C018) · `9deee5d` | MARGIN class attr; res 5000-5300 300/300 | approach.py, res_5000.txt | [E0813](01_timeline.md#E0813) |
| [C019](#C019) · `936a3d2` | Final sweeps | sw_m0008002005.txt, sw_m0015005008.txt, sw_m0018004009.txt | [E0816](01_timeline.md#E0816) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `56b6024251bd0ae40f7919db09697837f73e3c4b`; parents: none (initial snapshot). Recorded author date: 2026-09-30T16:51:12+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_56b6024.diff)

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
index 0000000..de07542
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "5c8dcec442af8c5a2dd5dce49c1169bf", "observation_space": {"type": "Box", "shape": [45], "low": [-Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity], "high": [Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity], "dtype": "float64"}, "action_space": {"type": "Box", "shape": [2], "low": [-0.05, -0.05], "high": [0.05, 0.05], "dtype": "float64"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Greedy model-based push planner v1

Commit `b7366c092dfeaf4a2e197d86d3a5578f430a5451`; parents: 56b6024251bd0ae40f7919db09697837f73e3c4b. Recorded author date: 2026-09-30T17:02:53+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0239](01_timeline.md#E0239): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_b7366c0_approach.py) · [Exact all-file diff](evidence/diffs/C002_b7366c0.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..80210c9
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,328 @@
           1 +"""Model-based greedy push planner for DynPushT2D.
           2 +
           3 +Block model: quasi-static, sticking point contact (mu~1), ellipsoidal limit surface
           4 +about the centre of mass with c^2 = I/m of a uniform T.
           5 +Body frame: origin = obs[0:2]; bar x in [-L/2,L/2], y in [-w,0]; stem x in [-w/2,w/2], y in [-w-Lv,-w].
           6 +"""
           7 +import heapq
           8 +import numpy as np
           9 +
          10 +RAD = 0.1
          11 +AMAX = 0.049
          12 +LO, HI = 0.1, 4.9
          13 +
          14 +
          15 +def wrap(a):
          16 +    return (a + np.pi) % (2 * np.pi) - np.pi
          17 +
          18 +
          19 +def rot(t):
          20 +    c, s = np.cos(t), np.sin(t)
          21 +    return np.array([[c, -s], [s, c]])
          22 +
          23 +
          24 +class Geom:
          25 +    def __init__(self, w, L, Lv):
          26 +        self.w, self.L, self.Lv = w, L, Lv
          27 +        a1, a2 = w * L, w * Lv
          28 +        y1, y2 = -w / 2, -w - Lv / 2
          29 +        yc = (a1 * y1 + a2 * y2) / (a1 + a2)
          30 +        I = a1 * ((L * L + w * w) / 12 + (y1 - yc) ** 2) + a2 * ((w * w + Lv * Lv) / 12 + (y2 - yc) ** 2)
          31 +        self.C = np.array([0.0, yc])
          32 +        self.c2 = I / (a1 + a2)
          33 +        self.rects = np.array([[-L / 2, L / 2, -w, 0.0], [-w / 2, w / 2, -w - Lv, -w]])
          34 +        self.corners = np.array([[-L / 2, 0], [L / 2, 0], [L / 2, -w], [-L / 2, -w],
          35 +                                 [-w / 2, -w - Lv], [w / 2, -w - Lv]])
          36 +        # contact candidates: (point, outward normal)
          37 +        cands = []
          38 +        h = L / 2
          39 +        for x in np.linspace(-h + 0.03, h - 0.03, 9):
          40 +            cands.append(((x, 0.0), (0, 1)))
          41 +        for x in np.linspace(w / 2 + 0.03, h - 0.03, 4):
          42 +            cands.append(((x, -w), (0, -1)))
          43 +            cands.append(((-x, -w), (0, -1)))
          44 +        cands.append(((h, -w / 2), (1, 0)))
          45 +        cands.append(((-h, -w / 2), (-1, 0)))
          46 +        for y in np.linspace(-w - 0.08, -w - Lv + 0.03, 6):
          47 +            cands.append(((w / 2, y), (1, 0)))
          48 +            cands.append(((-w / 2, y), (-1, 0)))
          49 +        cands.append(((0.0, -w - Lv), (0, -1)))
          50 +        self.cq = np.array([c[0] for c in cands], dtype=float)
          51 +        self.cn = np.array([c[1] for c in cands], dtype=float)
          52 +
          53 +    def dist_body(self, P):
          54 +        """min distance from body-frame points P (N,2) to T (0 inside)."""
          55 +        best = None
          56 +        for (x0, x1, y0, y1) in self.rects:
          57 +            dx = np.maximum(np.maximum(x0 - P[:, 0], P[:, 0] - x1), 0)
          58 +            dy = np.maximum(np.maximum(y0 - P[:, 1], P[:, 1] - y1), 0)
          59 +            d = np.hypot(dx, dy)
          60 +            best = d if best is None else np.minimum(best, d)
          61 +        return best
          62 +
          63 +
          64 +class GeneratedApproach:
          65 +    def __init__(self, action_space, observation_space, primitives):
          66 +        self.action_space = action_space
          67 +        self.plan = []
          68 +
          69 +    def reset(self, state, info):
          70 +        s = np.asarray(state, dtype=float)
          71 +        self.g = Geom(s[12], s[13], s[14])
          72 +        self.plan = []
          73 +        self.last_pose = None
          74 +
          75 +    # ---------------- helpers ----------------
          76 +    def err(self, ref, th, goal):
          77 +        g = self.g
          78 +        gref, gth = goal[0:2], goal[2]
          79 +        Rg = rot(gth)
          80 +        gcom = gref + Rg @ g.C
          81 +        dth = wrap(th - gth)
          82 +        # com position
          83 +        c, s = np.cos(th), np.sin(th)
          84 +        comx = ref[..., 0] - s * g.C[1]
          85 +        comy = ref[..., 1] + c * g.C[1]
          86 +        e_ref = np.hypot(ref[..., 0] - gref[0], ref[..., 1] - gref[1])
          87 +        e_com = np.hypot(comx - gcom[0], comy - gcom[1])
          88 +        return e_ref + e_com + 0.6 * np.abs(dth)
          89 +
          90 +    def seg_free(self, pose, a, b, clear):
          91 +        n = max(2, int(np.linalg.norm(b - a) / 0.01) + 1)
          92 +        t = np.linspace(0, 1, n)[:, None]
          93 +        P = a[None] + t * (b - a)[None]
          94 +        Pb = (P - pose[0:2]) @ rot(pose[2])  # world->body: R^T (p - o)
          95 +        return bool(np.all(self.g.dist_body(Pb) > clear))
          96 +
          97 +    def nav_path(self, pose, start, target):
          98 +        """visibility-graph shortest path; returns (waypoints, cost) or (None, inf)."""
          99 +        clear = RAD + 0.012
         100 +        if self.seg_free(pose, start, target, clear):
         101 +            return [target], self._plen([start, target])
         102 +        nodes = self.nodes
         103 +        pts = [start] + nodes + [target]
         104 +        N = len(pts)
         105 +        dist = [np.inf] * N
         106 +        prev = [-1] * N
         107 +        dist[0] = 0.0
         108 +        pq = [(0.0, 0)]
         109 +        while pq:
         110 +            d, i = heapq.heappop(pq)
         111 +            if d > dist[i]:
         112 +                continue
         113 +            if i == N - 1:
         114 +                break
         115 +            for j in range(1, N):
         116 +                if j == i:
         117 +                    continue
         118 +                key = (min(i, j), max(i, j))
         119 +                if i > 0 and j < N - 1:
         120 +                    ok = self.node_vis.get(key)
         121 +                    if ok is None:
         122 +                        ok = self.seg_free(pose, pts[i], pts[j], clear)
         123 +                        self.node_vis[key] = ok
         124 +                else:
         125 +                    ok = self.seg_free(pose, pts[i], pts[j], clear)
         126 +                if not ok:
         127 +                    continue
         128 +                nd = d + self._plen([pts[i], pts[j]])
         129 +                if nd < dist[j]:
         130 +                    dist[j] = nd
         131 +                    prev[j] = i
         132 +                    heapq.heappush(pq, (nd, j))
         133 +        if not np.isfinite(dist[N - 1]):
         134 +            return None, np.inf
         135 +        path = []
         136 +        k = N - 1
         137 +        while k > 0:
         138 +            path.append(pts[k])
         139 +            k = prev[k]
         140 +        return path[::-1], dist[N - 1]
         141 +
         142 +    @staticmethod
         143 +    def _plen(pts):
         144 +        s = 0.0
         145 +        for a, b in zip(pts[:-1], pts[1:]):
         146 +            s += np.max(np.abs(b - a)) / AMAX
         147 +        return s
         148 +
         149 +    def build_nodes(self, pose):
         150 +        g = self.g
         151 +        R = rot(pose[2])
         152 +        d = RAD + 0.05
         153 +        nodes = []
         154 +        for (x0, x1, y0, y1) in g.rects:
         155 +            for (x, y) in [(x0 - d, y0 - d), (x0 - d, y1 + d), (x1 + d, y0 - d), (x1 + d, y1 + d)]:
         156 +                nodes.append(np.array([x, y]))
         157 +        nb = np.array(nodes)
         158 +        ok = g.dist_body(nb) > RAD + 0.02
         159 +        out = []
         160 +        for p, o in zip(nb, ok):
         161 +            if not o:
         162 +                continue
         163 +            w = pose[0:2] + R @ p
         164 +            if LO + 0.01 <= w[0] <= HI - 0.01 and LO + 0.01 <= w[1] <= HI - 0.01:
         165 +                out.append(w)
         166 +        self.nodes = out
         167 +        self.node_vis = {}
         168 +
         169 +    # ---------------- planning ----------------
         170 +    def plan_push(self, s):
         171 +        g = self.g
         172 +        pose = s[0:3].copy()
         173 +        goal = s[29:32]
         174 +        robot = s[16:18].copy()
         175 +        E0 = float(self.err(pose[0:2], pose[2], goal))
         176 +
         177 +        angs = np.deg2rad([-35, -18, 0, 18, 35])
         178 +        Q = np.repeat(g.cq, len(angs), 0)
         179 +        Nn = np.repeat(g.cn, len(angs), 0)
         180 +        A = np.tile(angs, len(g.cq))
         181 +        K = len(Q)
         182 +        R0 = rot(pose[2])
         183 +        # push direction in body frame (inward normal rotated), then world
         184 +        inn = -Nn
         185 +        ca, sa = np.cos(A), np.sin(A)
         186 +        ub = np.stack([ca * inn[:, 0] - sa * inn[:, 1], sa * inn[:, 0] + ca * inn[:, 1]], 1)
         187 +        uw = ub @ R0.T
         188 +        pb_body = Q + Nn * RAD
         189 +        r = Q - g.C
         190 +        c2 = g.c2
         191 +        a11 = 1 + r[:, 1] ** 2 / c2
         192 +        a22 = 1 + r[:, 0] ** 2 / c2
         193 +        a12 = -r[:, 0] * r[:, 1] / c2
         194 +        det = a11 * a22 - a12 * a12
         195 +        tb = np.stack([-Nn[:, 1], Nn[:, 0]], 1)
         196 +
         197 +        com = np.tile(pose[0:2] + R0 @ g.C, (K, 1))
         198 +        th = np.full(K, pose[2])
         199 +        valid = np.ones(K, bool)
         200 +        ds = 0.01
         201 +        nsteps = 100
         202 +        best = (-np.inf, None)
         203 +        # travel cost to each candidate start
         204 +        standoff = 0.04
         205 +        pre = pose[0:2] + pb_body @ R0.T - uw * standoff
         206 +        travel = np.full(K, np.inf)
         207 +        paths = [None] * K
         208 +        self.build_nodes(pose)
         209 +        start = robot.copy()
         210 +        # retreat if touching
         211 +        rb = (robot - pose[0:2]) @ R0
         212 +        dd = g.dist_body(rb[None])[0]
         213 +        prefix = []
         214 +        if dd < RAD + 0.03:
         215 +            # outward direction approx: numeric gradient
         216 +            eps = 1e-3
         217 +            gx = g.dist_body((rb + [eps, 0])[None])[0] - g.dist_body((rb - [eps, 0])[None])[0]
         218 +            gy = g.dist_body((rb + [0, eps])[None])[0] - g.dist_body((rb - [0, eps])[None])[0]
         219 +            gv = np.array([gx, gy])
         220 +            if np.linalg.norm(gv) < 1e-9:
         221 +                gv = rb - g.C
         222 +            gv = R0 @ (gv / np.linalg.norm(gv))
         223 +            st = np.clip(robot + gv * (RAD + 0.035 - dd), LO + 0.005, HI - 0.005)
         224 +            prefix = [st]
         225 +            start = st
         226 +        pre_body = (pre - pose[0:2]) @ R0
         227 +        pre_ok = g.dist_body(pre_body) > RAD + 0.015
         228 +        pre_ok &= np.all((pre >= LO + 0.005) & (pre <= HI - 0.005), 1)
         229 +        valid &= pre_ok
         230 +        # lower bound travel (straight line) for pruning
         231 +        lb = np.max(np.abs(pre - start), 1) / AMAX + len(prefix)
         232 +
         233 +        pusher = pre.copy()
         234 +        results_len = np.zeros(K)
         235 +        results_E = np.full(K, np.inf)
         236 +        stepcnt = standoff / ds
         237 +        for k in range(1, nsteps + 1):
         238 +            c, sn = np.cos(th), np.sin(th)
         239 +            # world->body of push dir
         240 +            db = np.stack([c * uw[:, 0] + sn * uw[:, 1], -sn * uw[:, 0] + c * uw[:, 1]], 1) * ds
         241 +            f0 = (a22 * db[:, 0] - a12 * db[:, 1]) / det
         242 +            f1 = (-a12 * db[:, 0] + a11 * db[:, 1]) / det
         243 +            fn = -(f0 * Nn[:, 0] + f1 * Nn[:, 1])
         244 +            ft = f0 * tb[:, 0] + f1 * tb[:, 1]
         245 +            valid &= (fn > 0) & (np.abs(ft) <= 0.85 * fn)
         246 +            om = (r[:, 0] * f1 - r[:, 1] * f0) / c2
         247 +            com = com + np.stack([c * f0 - sn * f1, sn * f0 + c * f1], 1)
         248 +            th = th + om
         249 +            c, sn = np.cos(th), np.sin(th)
         250 +            ref = com - np.stack([-sn * g.C[1], c * g.C[1]], 1)
         251 +            # wall check on corners
         252 +            cx = ref[:, 0][:, None] + c[:, None] * g.corners[None, :, 0] - sn[:, None] * g.corners[None, :, 1]
         253 +            cy = ref[:, 1][:, None] + sn[:, None] * g.corners[None, :, 0] + c[:, None] * g.corners[None, :, 1]
         254 +            valid &= (cx.min(1) > 0.03) & (cx.max(1) < 4.97) & (cy.min(1) > 0.03) & (cy.max(1) < 4.97)
         255 +            pw = pre + uw * (standoff + k * ds)
         256 +            valid &= np.all((pw >= LO + 0.005) & (pw <= HI - 0.005), 1)
         257 +            if not valid.any():
         258 +                break
         259 +            E = self.err(ref, th, goal)
         260 +            better = valid & (E < results_E - 1e-9)
         261 +            results_E = np.where(better, E, results_E)
         262 +            results_len = np.where(better, k * ds, results_len)
         263 +
         264 +        imp = E0 - results_E
         265 +        # rate = improvement / steps, with lower bound travel first
         266 +        push_steps = results_len / AMAX + 3
         267 +        order = np.argsort(-(imp / (lb + push_steps + 4)))
         268 +        best_i, best_rate, best_path = None, -np.inf, None
         269 +        for i in order[:25]:
         270 +            if not np.isfinite(results_E[i]) or imp[i] <= 1e-4:
         271 +                continue
         272 +            ub_rate = imp[i] / (lb[i] + push_steps[i] + 4)
         273 +            if ub_rate <= best_rate:
         274 +                break
         275 +            path, cost = self.nav_path(pose, start, pre[i])
         276 +            if path is None:
         277 +                continue
         278 +            rate = imp[i] / (cost + len(prefix) + push_steps[i] + 4)
         279 +            if rate > best_rate:
         280 +                best_rate, best_i, best_path = rate, i, path
         281 +        if best_i is None:
         282 +            return None
         283 +        i = best_i
         284 +        return dict(path=prefix + best_path, u=uw[i], L=results_len[i] + standoff,
         285 +                    Epred=results_E[i], E0=E0)
         286 +
         287 +    # ---------------- execution ----------------
         288 +    def build_actions(self, robot, plan):
         289 +        acts = []
         290 +        p = robot.copy()
         291 +        for wp in plan['path']:
         292 +            while True:
         293 +                d = wp - p
         294 +                m = np.max(np.abs(d))
         295 +                if m < 1e-6:
         296 +                    break
         297 +                a = d if m <= AMAX else d * (AMAX / m)
         298 +                acts.append(('nav', a))
         299 +                p = p + a
         300 +        u = plan['u']
         301 +        Ltot = plan['L']
         302 +        done = 0.0
         303 +        while done < Ltot - 1e-6:
         304 +            rem = Ltot - done
         305 +            st = AMAX if rem > 0.15 else max(0.01, min(AMAX, rem / 3))
         306 +            st = min(st, rem)
         307 +            acts.append(('push', u * st / max(abs(u[0]), abs(u[1]), 1e-9) * max(abs(u[0]), abs(u[1]))))
         308 +            done += st
         309 +        return acts
         310 +
         311 +    def get_action(self, state):
         312 +        s = np.asarray(state, dtype=float)
         313 +        if not self.plan:
         314 +            p = self.plan_push(s)
         315 +            if p is None:
         316 +                # fallback: small random-ish wiggle away
         317 +                a = np.array([0.0, 0.0])
         318 +                return self._safe(s, a)
         319 +            self.plan = self.build_actions(s[16:18], p)
         320 +        _, a = self.plan.pop(0)
         321 +        return self._safe(s, a)
         322 +
         323 +    def _safe(self, s, a):
         324 +        a = np.clip(np.asarray(a, dtype=float), -AMAX, AMAX)
         325 +        rob = s[16:18]
         326 +        nxt = np.clip(rob + a, LO + 1e-3, HI - 1e-3)
         327 +        a = np.clip(nxt - rob, -AMAX, AMAX)
         328 +        return a.astype(np.float64)
diff --git a/dyn_fit.py b/dyn_fit.py
new file mode 100644
index 0000000..6f101db
--- /dev/null
+++ b/dyn_fit.py
@@ -0,0 +1,19 @@
           1 +from dyn_push import *
           2 +from scipy.optimize import least_squares
           3 +import pickle
           4 +cases=[ # start_b, dir_b, normal(outward) for contact point
           5 + ([0.2,0.6],[0,-1],[0,1]),([0.4,0.6],[0,-1],[0,1]),([0.55,0.6],[0,-1],[0,1]),([-0.3,0.6],[0,-1],[0,1]),
           6 + ([-0.8,-0.5],[1,0],[-1,0]),([-0.8,-0.8],[1,0],[-1,0]),([-0.8,-1.1],[1,0],[-1,0]),
           7 + ([0.8,-0.4],[-1,0],[1,0]),([0.8,-0.9],[-1,0],[1,0]),
           8 + ([0.4,-0.8],[0,1],[0,-1]),([0.25,-0.8],[0,1],[0,-1]),
           9 + ([0.03,-1.8],[0,1],[0,-1]),([0.0,-1.8],[0,1],[0,-1]),
          10 + ([1.0,-0.065],[-1,0],[1,0]),
          11 +]
          12 +data=[]
          13 +for sb,d,n in cases:
          14 +    out,e=push(0,sb,d,0.01,5)
          15 +    cb,tw=out[3]
          16 +    u=np.array(d,float)*0.01
          17 +    cp=cb-0.1*np.array(n)
          18 +    data.append((cp,u,tw)); print(sb,d,'contact',cp,'twist',tw)
          19 +pickle.dump(data,open('dyn_fitdata.pkl','wb'))
diff --git a/dyn_fit2.py b/dyn_fit2.py
new file mode 100644
index 0000000..3928296
--- /dev/null
+++ b/dyn_fit2.py
@@ -0,0 +1,15 @@
           1 +import numpy as np, pickle
           2 +from scipy.optimize import least_squares
           3 +data=pickle.load(open('dyn_fitdata.pkl','rb'))
           4 +data=[d for i,d in enumerate(data) if i!=10]
           5 +def pred(params,cp,u):
           6 +    xc,yc,c2=params
           7 +    rx,ry=cp[0]-xc,cp[1]-yc
           8 +    A=np.array([[1+ry**2/c2,-rx*ry/c2],[-rx*ry/c2,1+rx**2/c2]])
           9 +    f=np.linalg.solve(A,u)
          10 +    w=(rx*f[1]-ry*f[0])/c2
          11 +    return np.array([f[0]+w*yc, f[1]-w*xc, w])
          12 +def res(p): return np.concatenate([pred(p,cp,u)-tw for cp,u,tw in data])*1000
          13 +for fix in [None]:
          14 +    r=least_squares(res,[0,-0.3,0.2]); print('fit xc,yc,c2',r.x,'rms(1e-3)',np.sqrt(np.mean(r.fun**2)))
          15 +    for cp,u,tw in data: print(cp.round(3),u,tw,pred(r.x,cp,u).round(5))
diff --git a/dyn_fric.py b/dyn_fric.py
new file mode 100644
index 0000000..0503add
--- /dev/null
+++ b/dyn_fric.py
@@ -0,0 +1,12 @@
           1 +from dyn_push import *
           2 +import sys
           3 +sys.path.insert(0,'.')
           4 +from dyn_fit2 import pred
           5 +P=[0,-0.375,0.2129]
           6 +for a in [0,5,10,15,20,25,30,40]:
           7 +    ar=np.radians(a); d=np.array([np.sin(ar),-np.cos(ar)])
           8 +    out,e=push(0,[-0.2*np.sin(ar)/np.cos(ar)*0,0.6],d,0.005,6)
           9 +    for k in [1,3]:
          10 +        cb,tw=out[k]; cb2=out[k+1][0]
          11 +        cp=cb-[0,0.1]; u=d*0.005
          12 +        print(f'a={a} k={k} cp={cp.round(4)} slip_x/step={cb2[0]-cb[0]:.5f} ut={u[0]:.5f} twist={tw} stickpred={pred(P,cp,u).round(5)}')
diff --git a/dyn_fric2.py b/dyn_fric2.py
new file mode 100644
index 0000000..0d2ad58
--- /dev/null
+++ b/dyn_fric2.py
@@ -0,0 +1,12 @@
           1 +from dyn_push import *
           2 +from dyn_fit2 import pred
           3 +P=[0,-0.375,0.2129]
           4 +for a in [40,50,55,60,65,70,75]:
           5 +    ar=np.radians(a); d=np.array([np.sin(ar),-np.cos(ar)])
           6 +    out,e=push(0,[-np.tan(ar)*0.5,0.6],d,0.005,8)
           7 +    for k in [0,1,3,6]:
           8 +        cb,tw=out[k]
           9 +        cp=cb-[0,0.1]; u=d*0.005
          10 +        rx,ry=cp[0],cp[1]+0.375; c2=0.2129
          11 +        A=np.array([[1+ry**2/c2,-rx*ry/c2],[-rx*ry/c2,1+rx**2/c2]]); f=np.linalg.solve(A,u)
          12 +        print(f'a={a} k={k} cp={cp.round(4)} twist={tw} stickpred={pred(P,cp,u).round(5)} |ft/fn|={abs(f[0]/f[1]):.3f}')
diff --git a/dyn_gap.py b/dyn_gap.py
new file mode 100644
index 0000000..f37c21d
--- /dev/null
+++ b/dyn_gap.py
@@ -0,0 +1,11 @@
           1 +from dyn_lib import *
           2 +for s in [0.005,0.02,0.035,0.049]:
           3 +    e=E(0); e.goto_safe([0,0.1+s*3.5+1e-4]); o0=e.obs.copy(); dw=R(o0[2])@np.array([0,-1.0])
           4 +    rows=[]
           5 +    for k in range(8):
           6 +        ob=e.obs.copy(); o=e.step(dw*s)
           7 +        rows.append((to_body(ob,ob[16:18])[1]-0.1, R(ob[2]).T@(o[0:2]-ob[0:2])))
           8 +    print('step',s,' '.join(f'[gap {g:.4f} dy {d[1]:.4f}]' for g,d in rows))
           9 +    # then change step size to s/2 and 0
          10 +    for s2 in [s/2,0.0,s]:
          11 +        ob=e.obs.copy(); o=e.step(dw*s2); print('   next step',s2,'dy',(R(ob[2]).T@(o[0:2]-ob[0:2]))[1].round(5),'gap after',(to_body(o,o[16:18])[1]-0.1).round(5))
diff --git a/dyn_lib.py b/dyn_lib.py
new file mode 100644
index 0000000..0e12781
--- /dev/null
+++ b/dyn_lib.py
@@ -0,0 +1,31 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=5, suppress=True, linewidth=200)
           4 +def R(t): c,s=np.cos(t),np.sin(t); return np.array([[c,-s],[s,c]])
           5 +def to_body(obs,p): return R(obs[2]).T@(np.asarray(p)-obs[0:2])
           6 +def to_world(obs,pb): return obs[0:2]+R(obs[2])@np.asarray(pb)
           7 +class E:
           8 +    def __init__(s,seed=0):
           9 +        s.env=make_env(); s.obs,_=s.env.reset(seed=seed); s.n=0
          10 +    def step(s,a):
          11 +        a=np.clip(np.asarray(a,float),-0.049,0.049)
          12 +        s.obs,r,te,tr,_=s.env.step(a); s.n+=1; return s.obs
          13 +    def goto(s,tgt,maxstep=0.049,n=400):
          14 +        for _ in range(n):
          15 +            d=np.asarray(tgt)-s.obs[16:18]
          16 +            if np.linalg.norm(d)<1e-7: break
          17 +            m=np.max(np.abs(d)); a=d if m<=maxstep else d*maxstep/m
          18 +            s.step(a)
          19 +        return s.obs
          20 +    def goto_safe(s,tgt_body):
          21 +        # move radially out to radius 1.6 from block center, go around circle, then to target (in body frame)
          22 +        o=s.obs; c=o[0:2]; p=o[16:18]
          23 +        tw=to_world(o,tgt_body)
          24 +        Rr=1.7
          25 +        v=p-c; a0=np.arctan2(v[1],v[0])
          26 +        if np.linalg.norm(v)<Rr: s.goto(c+Rr*np.array([np.cos(a0),np.sin(a0)]))
          27 +        vt=tw-c; a1=np.arctan2(vt[1],vt[0])
          28 +        da=(a1-a0+np.pi)%(2*np.pi)-np.pi
          29 +        for k in range(1,21):
          30 +            a=a0+da*k/20; s.goto(c+Rr*np.array([np.cos(a),np.sin(a)]))
          31 +        s.goto(tw); return s.obs
diff --git a/dyn_model.py b/dyn_model.py
new file mode 100644
index 0000000..8859919
--- /dev/null
+++ b/dyn_model.py
@@ -0,0 +1,68 @@
           1 +"""Approximate quasi-static push model for the T block (fitted to env).
           2 +Body frame: origin = obs[0:2]; bar: x in [-L/2,L/2], y in [-w,0]; stem: x in [-w/2,w/2], y in [-w-Lv,-w].
           3 +Motion: sticking/sliding point contact (mu=1), ellipsoidal limit surface == free body impulse model about CoM,
           4 +c^2 = I/m of uniform-density T."""
           5 +import numpy as np
           6 +MU=1.0; RP=0.1
           7 +def Rm(t): c,s=np.cos(t),np.sin(t); return np.array([[c,-s],[s,c]])
           8 +def geom(w,L,Lv):
           9 +    a1,a2=w*L,w*Lv; y1,y2=-w/2,-w-Lv/2
          10 +    yc=(a1*y1+a2*y2)/(a1+a2)
          11 +    I=a1*((L*L+w*w)/12+(y1-yc)**2)+a2*((w*w+Lv*Lv)/12+(y2-yc)**2)
          12 +    return dict(w=w,L=L,Lv=Lv,C=np.array([0.0,yc]),c2=I/(a1+a2),
          13 +                rects=[(-L/2,L/2,-w,0.0),(-w/2,w/2,-w-Lv,-w)])
          14 +def closest(g,p):
          15 +    """closest point on T boundary to p (body frame), signed distance, outward normal"""
          16 +    best=None
          17 +    for (x0,x1,y0,y1) in g['rects']:
          18 +        q=np.array([min(max(p[0],x0),x1),min(max(p[1],y0),y1)])
          19 +        d=np.linalg.norm(p-q)
          20 +        if d>1e-12: n=(p-q)/d; sd=d
          21 +        else:  # inside rect
          22 +            ds=[p[0]-x0,x1-p[0],p[1]-y0,y1-p[1]]; k=int(np.argmin(ds)); sd=-ds[k]
          23 +            n=[np.array([-1,0.]),np.array([1,0.]),np.array([0,-1.]),np.array([0,1.])][k]
          24 +            q=p-n*sd
          25 +        if best is None or sd<best[0]: best=(sd,q,n)
          26 +    return best
          27 +def twist_from_force(g,cp,f):
          28 +    r=cp-g['C']; w=(r[0]*f[1]-r[1]*f[0])/g['c2']
          29 +    return np.array([f[0],f[1]]),w   # velocity of C, omega
          30 +def contact_vel(v,w,r): return v+w*np.array([-r[1],r[0]])
          31 +def sim_substep(g,pose,pb_world,dp_world,rp=RP):
          32 +    """pose=(x,y,th). pusher moves by dp. returns new pose"""
          33 +    x,y,th=pose; Rt=Rm(th)
          34 +    p_new=Rt.T@(pb_world+dp_world-np.array([x,y]))
          35 +    sd,q,n=closest(g,p_new)
          36 +    pen=rp-sd
          37 +    if pen<=0: return np.array(pose,float)
          38 +    u=Rt.T@dp_world  # pusher velocity body
          39 +    r=q-g['C']; c2=g['c2']
          40 +    # sticking
          41 +    A=np.array([[1+r[1]**2/c2,-r[0]*r[1]/c2],[-r[0]*r[1]/c2,1+r[0]**2/c2]])
          42 +    un=np.dot(u,n)
          43 +    # required contact displacement: normal component = penetration removal
          44 +    t=np.array([-n[1],n[0]])
          45 +    utan=np.dot(u,t)
          46 +    dcont=-pen*n + utan*t   # want contact pt to move by this (normal: remove penetration)
          47 +    f=np.linalg.solve(A,dcont)
          48 +    fn=-np.dot(f,n); ft=np.dot(f,t)
          49 +    if fn<=0: return np.array(pose,float)
          50 +    if abs(ft)>MU*fn:
          51 +        fdir=-n+MU*np.sign(ft)*t
          52 +        v1,w1=twist_from_force(g,q,fdir); cv=contact_vel(v1,w1,r)
          53 +        lam=pen/(-np.dot(cv,n)); f=lam*fdir
          54 +    v,w=twist_from_force(g,q,f)
          55 +    # displacement of origin in body frame: v_C + w x (0-C)
          56 +    vo=v+w*np.array([g['C'][1],-g['C'][0]])
          57 +    # integrate exactly as rotation about ICR-ish (small): use midpoint rotation
          58 +    dpos=Rm(th+w/2)@vo
          59 +    return np.array([x+dpos[0],y+dpos[1],th+w])
          60 +KAPPA=0.265  # block ends each step separated by extra KAPPA*normal pusher step (velocity-dependent gap)
          61 +def sim_step(g,pose,pb_world,action,nsub=10,kappa=KAPPA):
          62 +    pose=np.array(pose,float); pb=np.array(pb_world,float); a=np.asarray(action,float); d=a/nsub
          63 +    sd,q,n=closest(g,Rm(pose[2]).T@(pb+a-pose[0:2]))
          64 +    un=max(0.0,-np.dot(Rm(pose[2]).T@a,n))
          65 +    rp=RP+kappa*un
          66 +    for _ in range(nsub):
          67 +        pose=sim_substep(g,pose,pb,d,rp); pb=pb+d
          68 +    return pose,pb
diff --git a/dyn_obs.py b/dyn_obs.py
new file mode 100644
index 0000000..f86a414
--- /dev/null
+++ b/dyn_obs.py
@@ -0,0 +1,6 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=4, suppress=True, linewidth=200)
           4 +env=make_env()
           5 +for s in range(3):
           6 +    o,_=env.reset(seed=s); print(s,o)
diff --git a/dyn_probe.py b/dyn_probe.py
new file mode 100644
index 0000000..f5084cb
--- /dev/null
+++ b/dyn_probe.py
@@ -0,0 +1,24 @@
           1 +from dyn_lib import *
           2 +import sys
           3 +# probe surface: approach along body-frame direction, detect first block motion
           4 +def probe(seed, start_b, dir_b, step=0.002):
           5 +    e=E(seed); e.goto_safe(start_b); o0=e.obs.copy()
           6 +    d=np.asarray(dir_b,float); d/=np.linalg.norm(d)
           7 +    dw=R(o0[2])@d
           8 +    for i in range(1500):
           9 +        p_before=e.obs[16:18].copy()
          10 +        o=e.step(dw*step)
          11 +        if np.linalg.norm(o[0:3]-o0[0:3])>1e-9:
          12 +            return to_body(o0,p_before), o[0:3]-o0[0:3]
          13 +    return None,None
          14 +for s in [0,1]:
          15 +  for x in [0.0,0.3,0.5,-0.5]:
          16 +    pb,dp=probe(s,[x,1.0],[0,-1]); print('seed',s,'bar top x',x,'contact robot body',pb,dp)
          17 +  for x in [0.0]:
          18 +    pb,dp=probe(s,[x,-1.8],[0,1]); print('seed',s,'stem end',x,pb,dp)
          19 +    pb,dp=probe(s,[x,-0.3],[0,1]) if False else (None,None)
          20 +  for y in [-0.3,-0.6]:
          21 +    pb,dp=probe(s,[1.0,y],[-1,0]); print('seed',s,'stem side y',y,pb,dp)
          22 +  pb,dp=probe(s,[1.2,0.0],[-1,0]); print('seed',s,'bar end +x',pb,dp)
          23 +  pb,dp=probe(s,[0.4,-0.6],[0,1]); print('seed',s,'bar bottom x=.4',pb,dp)
          24 +  print('dims',E(s).obs[12:15])
diff --git a/dyn_push.py b/dyn_push.py
new file mode 100644
index 0000000..0a51ff2
--- /dev/null
+++ b/dyn_push.py
@@ -0,0 +1,28 @@
           1 +from dyn_lib import *
           2 +import sys
           3 +def body_twist(o0,o1):
           4 +    dpw=o1[0:2]-o0[0:2]; dth=(o1[2]-o0[2]+np.pi)%(2*np.pi)-np.pi
           5 +    return np.r_[R(o0[2]).T@dpw, dth]
           6 +def push(seed, start_b, dir_b, step, nsteps, verbose=False):
           7 +    e=E(seed); e.goto_safe(start_b); o0=e.obs.copy()
           8 +    d=np.asarray(dir_b,float); d/=np.linalg.norm(d)
           9 +    # approach slowly until contact
          10 +    for i in range(2000):
          11 +        o=e.step(R(e.obs[2])@d*0.001)
          12 +        if np.linalg.norm(o[0:3]-o0[0:3])>1e-9: break
          13 +    out=[]
          14 +    for k in range(nsteps):
          15 +        ob=e.obs.copy()
          16 +        o=e.step(R(ob[2])@d*step)   # direction fixed in body frame
          17 +        tw=body_twist(ob,o)
          18 +        cb=to_body(ob,ob[16:18])  # pusher pos in body frame before step
          19 +        out.append((cb,tw))
          20 +    return out,e
          21 +if __name__=='__main__':
          22 +    for x in [0.0,0.2,0.4,0.55]:
          23 +        out,e=push(0,[x,0.6],[0,-1],0.01,12)
          24 +        for k in [1,5,11]:
          25 +            cb,tw=out[k]
          26 +            # ICR in body frame: v = w x (p - c) => c = p_origin + (-vy/w, vx/w)
          27 +            icr = np.array([-tw[1]/tw[2], tw[0]/tw[2]]) if abs(tw[2])>1e-9 else None
          28 +            print(f'x={x} k={k} pusher_b={cb} twist={tw} icr={icr}')
diff --git a/dyn_push2.py b/dyn_push2.py
new file mode 100644
index 0000000..0b2773d
--- /dev/null
+++ b/dyn_push2.py
@@ -0,0 +1,17 @@
           1 +from dyn_push import *
           2 +print('--- side push +x on stem left face (x=-w/2) at various y')
           3 +for y in [-0.2,-0.5,-0.8,-1.1]:
           4 +    out,e=push(0,[-0.8,y],[1,0],0.01,8)
           5 +    cb,tw=out[5]
           6 +    icr=np.array([-tw[1]/tw[2], tw[0]/tw[2]]) if abs(tw[2])>1e-9 else None
           7 +    print(f'y={y} pusher_b={cb} twist={tw} icr={icr}', 'c2=',None if icr is None else -icr[1]*cb[1])
           8 +print('--- side push on bar end (x=+L/2) moving -x at y=-0.065')
           9 +out,e=push(0,[1.0,-0.065],[-1,0],0.01,8)
          10 +cb,tw=out[5]; print(cb,tw)
          11 +print('--- oblique push at top center, angle a from normal')
          12 +for a in [10,20,30,45,60]:
          13 +    ar=np.radians(a)
          14 +    out,e=push(0,[0.0,0.6],[np.sin(ar),-np.cos(ar)],0.01,10)
          15 +    cb0=out[1][0]; cb1=out[-1][0]
          16 +    tws=np.array([t for _,t in out[1:]])
          17 +    print(f'a={a} pusher body x drift {cb1[0]-cb0[0]:.4f} over {len(out)-2} steps; mean twist {tws.mean(0)}')
diff --git a/dyn_q45.py b/dyn_q45.py
new file mode 100644
index 0000000..c2bf6b4
--- /dev/null
+++ b/dyn_q45.py
@@ -0,0 +1,11 @@
           1 +from dyn_push import *
           2 +def run(seed, sb, d, step, total):
           3 +    e=E(seed); e.goto_safe(sb); dw=R(e.obs[2])@np.array(d,float)
           4 +    n=int(round(total/step))
           5 +    for i in range(n): e.step(dw*step)
           6 +    return e.obs.copy()
           7 +for sb,d in [([0.4,0.4],[0,-1]),([-0.8,-0.9],[1,0]),([-0.5,0.5],[0.5,-0.866])]:
           8 +    res=[run(0,sb,d,s,0.98) for s in [0.049,0.0245,0.01,0.005]]
           9 +    for s,o in zip([0.049,0.0245,0.01,0.005],res): print(sb,d,'step',s,'pose',o[0:3],'pusher',o[16:18])
          10 +print('determinism:')
          11 +a=run(3,[0.3,0.4],[0.2,-1],0.03,1.2); b=run(3,[0.3,0.4],[0.2,-1],0.03,1.2); print(a[0:3],b[0:3],np.abs(a-b).max())
diff --git a/dyn_validate.py b/dyn_validate.py
new file mode 100644
index 0000000..d176b2e
--- /dev/null
+++ b/dyn_validate.py
@@ -0,0 +1,23 @@
           1 +from dyn_lib import *
           2 +from dyn_model import *
           3 +rng=np.random.default_rng(0)
           4 +errs1=[];errsN=[]
           5 +for trial in range(12):
           6 +    seed=int(rng.integers(0,100)); e=E(seed)
           7 +    ang=rng.uniform(0,2*np.pi); tgt_b=np.array([0,-0.4])+0.9*np.array([np.cos(ang),np.sin(ang)])
           8 +    e.goto_safe(tgt_b)
           9 +    o=e.obs; g=geom(o[12],o[13],o[14])
          10 +    pose0=o[0:3].copy(); pb0=o[16:18].copy(); poseN=pose0.copy(); pbN=pb0.copy()
          11 +    cw=to_world(o,[0,-0.4]); 
          12 +    moved=0
          13 +    for k in range(40):
          14 +        d=cw-e.obs[16:18]; d=d/np.linalg.norm(d)*0.04 + rng.normal(0,0.01,2)
          15 +        d=np.clip(d,-0.049,0.049)
          16 +        ob=e.obs.copy()
          17 +        p1,_=sim_step(g,ob[0:3],ob[16:18],d)
          18 +        poseN,pbN=sim_step(g,poseN,pbN,d)
          19 +        o2=e.step(d)
          20 +        if np.linalg.norm(o2[0:3]-ob[0:3])>1e-6: moved+=1; errs1.append(np.r_[p1[0:2]-o2[0:2],p1[2]-o2[2]])
          21 +    errN=np.r_[poseN[0:2]-e.obs[0:2],poseN[2]-e.obs[2]]
          22 +    print(f'trial {trial} seed {seed} moved_steps {moved} open-loop final err pos {np.linalg.norm(errN[:2]):.4f} th {errN[2]:.4f}  total disp {np.linalg.norm(e.obs[0:2]-pose0[0:2]):.3f} dth {e.obs[2]-pose0[2]:.3f}')
          23 +E1=np.array(errs1); print('1-step err (contact steps): pos rms',np.sqrt((E1[:,:2]**2).sum(1).mean()),'max',np.sqrt((E1[:,:2]**2).sum(1)).max(),'th rms',np.sqrt((E1[:,2]**2).mean()),'max',np.abs(E1[:,2]).max())
diff --git a/explore.py b/explore.py
new file mode 100644
index 0000000..57c5102
--- /dev/null
+++ b/explore.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=4, suppress=True, linewidth=200)
           4 +env = make_env()
           5 +for s in range(5):
           6 +    obs,_ = env.reset(seed=s)
           7 +    print(s, obs)
           8 +print(env.max_steps)
           9 +obs,_=env.reset(seed=0)
          10 +for t in range(10):
          11 +    obs,r,te,tr,_=env.step(np.array([0.049,0.0]))
          12 +    print(t, obs[16:22], obs[0:6], r, te)
          13 +env.close()
diff --git a/explore2.py b/explore2.py
new file mode 100644
index 0000000..bd2146a
--- /dev/null
+++ b/explore2.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=4, suppress=True, linewidth=200)
           4 +env = make_env()
           5 +obs,_=env.reset(seed=0)
           6 +# block at (1.05,3.44). robot at (1.637,1.27). move robot to (1.05, 2.3) then push up
           7 +def goto(obs, tgt, n=200):
           8 +    for _ in range(n):
           9 +        d = np.array(tgt)-obs[16:18]
          10 +        if np.linalg.norm(d)<1e-4: break
          11 +        a = np.clip(d, -0.049, 0.049)
          12 +        obs,r,te,tr,_=env.step(a)
          13 +    return obs
          14 +obs = goto(obs,[1.05,2.3])
          15 +print(obs[16:18], obs[0:6])
          16 +for t in range(40):
          17 +    obs,r,te,tr,_=env.step(np.array([0,0.04]))
          18 +    if t%4==0: print(t, obs[16:18], obs[0:6])
          19 +for t in range(20):
          20 +    obs,r,te,tr,_=env.step(np.array([0,0.0]))
          21 +    if t%2==0: print('stop',t, obs[16:18], obs[0:6])
          22 +env.close()
diff --git a/geom_blow.py b/geom_blow.py
new file mode 100644
index 0000000..e9e72cf
--- /dev/null
+++ b/geom_blow.py
@@ -0,0 +1,12 @@
           1 +from geom_lib import *
           2 +from geom_wall import corners
           3 +P=Prober()
           4 +seed=20
           5 +o=P.reset(seed); th=P.b0[2]; M=rot(th); c=P.b0[:2]
           6 +d=M@np.array([0,-1.0])
           7 +P.nav(c+M@np.array([0,0.5]))
           8 +for k in range(150):
           9 +    prev=P.obs.copy(); P.step(d*0.03)
          10 +    if np.abs(P.obs[0:3]-prev[0:3]).max()>0.2 or k%10==0:
          11 +        cs=corners(P.obs); print(k,'robot',np.round(P.obs[16:18],3),'block',np.round(P.obs[0:3],3),'vel',np.round(P.obs[3:6],2),'cmin',np.round(cs.min(0),3),'cmax',np.round(cs.max(0),3))
          12 +    if np.abs(P.obs[0:3]-prev[0:3]).max()>0.2: break
diff --git a/geom_bounds.py b/geom_bounds.py
new file mode 100644
index 0000000..a9650c8
--- /dev/null
+++ b/geom_bounds.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env()
           4 +for s in [0,1]:
           5 +  for d in [(1,0),(-1,0),(0,1),(0,-1)]:
           6 +    obs,_=env.reset(seed=s)
           7 +    prev=obs[16:18].copy(); stuck=0
           8 +    for t in range(300):
           9 +        obs,*_=env.step(np.array(d)*0.0499)
          10 +        if np.linalg.norm(obs[16:18]-prev)<1e-4: stuck+=1
          11 +        else: stuck=0
          12 +        prev=obs[16:18].copy()
          13 +        if stuck>5: break
          14 +    print(s,d,'t',t,'robot',obs[16:18],'block',obs[0:3])
diff --git a/geom_bounds2.py b/geom_bounds2.py
new file mode 100644
index 0000000..116fc92
--- /dev/null
+++ b/geom_bounds2.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env()
           4 +obs,_=env.reset(seed=0)
           5 +for d in [(1,0),(-1,0),(0,1),(0,-1)]:
           6 +    obs,_=env.reset(seed=0)
           7 +    for t in range(200):
           8 +        obs,*_=env.step(np.array(d)*0.0499)
           9 +    p=obs[16:18].copy()
          10 +    # now fine steps
          11 +    seq=[]
          12 +    for t in range(10):
          13 +        obs,*_=env.step(np.array(d)*0.001); seq.append(obs[16:18].copy())
          14 +    print(d,'after coarse',p,'after fine',seq[-1], 'fine deltas', np.round(np.diff([p]+seq,axis=0)[:,0 if d[0] else 1],5))
diff --git a/geom_bounds3.py b/geom_bounds3.py
new file mode 100644
index 0000000..a64289d
--- /dev/null
+++ b/geom_bounds3.py
@@ -0,0 +1,21 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env()
           4 +obs,_=env.reset(seed=0)
           5 +for t in range(64): obs,*_=env.step(np.array([0.0499,0]))
           6 +print('x',obs[16])
           7 +for a in [0.01,0.005,0.003,0.002,0.001,0.0005,0.0002,0.0001]:
           8 +    for k in range(40):
           9 +        x0=obs[16]; obs,*_=env.step(np.array([a,0])); 
          10 +        if abs(obs[16]-x0)<1e-6: print('a',a,'rejected at x0',x0,'x0+a',x0+a); break
          11 +    else: print('a',a,'no reject x',obs[16])
          12 +# go to left via y bottom
          13 +obs,_=env.reset(seed=0)
          14 +for t in range(31): obs,*_=env.step(np.array([-0.0499,0]))
          15 +print('x',obs[16])
          16 +for a in [0.01,0.005,0.002,0.001,0.0005,0.0002,0.0001]:
          17 +    for k in range(40):
          18 +        x0=obs[16]; obs,*_=env.step(np.array([-a,0]))
          19 +        if abs(obs[16]-x0)<1e-6: print('a',a,'rejected at x0',x0,'x0-a',x0-a); break
          20 +        print('  moved',x0,'->',obs[16]) if k<3 else None
          21 +    else: print('a',a,'no reject x',obs[16])
diff --git a/geom_com.py b/geom_com.py
new file mode 100644
index 0000000..516e395
--- /dev/null
+++ b/geom_com.py
@@ -0,0 +1,14 @@
           1 +from geom_lib import *
           2 +P=Prober()
           3 +for seed in [12,24]:
           4 +    o=P.reset(seed); w,Lh,Lv=o[12:15]
           5 +    Ab,As=Lh*w,w*Lv; yc=(Ab*(-w/2)+As*(-w-Lv/2))/(Ab+As)
           6 +    print('seed',seed,'area centroid y=%.4f'%yc, 'bar-center y=%.4f'%(-w/2), 'stem-mid y=%.4f'%(-w-Lv/2))
           7 +    for y in [-0.05,-0.15,-0.25,-0.3,-0.35,-0.4,-0.45,-0.55,-0.7]:
           8 +        sx = -1.0 if y<-w else -0.9
           9 +        P.reset(seed); th=P.b0[2]; M=rot(th); c=P.b0[:2]
          10 +        P.nav(c+M@np.array([sx,y]))
          11 +        d=M@np.array([1.0,0])
          12 +        for k in range(int((abs(sx)+0.15)/0.005)): P.step(d*0.005)
          13 +        db=P.obs[0:3]-P.b0
          14 +        print('  push y=%.2f dtheta=%+.5f dpos_body=%s'%(y,db[2],np.round(M.T@db[:2],4)))
diff --git a/geom_confirm.py b/geom_confirm.py
new file mode 100644
index 0000000..a386127
--- /dev/null
+++ b/geom_confirm.py
@@ -0,0 +1,18 @@
           1 +from geom_lib import *
           2 +import sys
           3 +P=Prober()
           4 +for seed in [20,31,24]:
           5 +    o=P.reset(seed); w,Lh,Lv=o[12:15]; r=o[28]
           6 +    print('seed',seed,'w %.4f Lh %.4f Lv %.4f'%(w,Lh,Lv))
           7 +    probes={'top(y=0)':((0.2,1.0),(0,-1),1,0.0),
           8 +            'bar_bottom(y=-w)':((0.35,-1.0),(0,1),1,-w),
           9 +            'bar_end_right(x=Lh/2)':((1.2,-w/2),(-1,0),0,Lh/2),
          10 +            'bar_end_left(x=-Lh/2)':((-1.2,-w/2),(1,0),0,-Lh/2),
          11 +            'stem_right(x=w/2)':((1.0,-0.7),(-1,0),0,w/2),
          12 +            'stem_left(x=-w/2)':((-1.0,-0.7),(1,0),0,-w/2),
          13 +            'stem_tip(y=-w-Lv)':((0.0,-1.55),(0,1),1,-w-Lv)}
          14 +    for name,(s,d,ax,pred) in probes.items():
          15 +        res,msg=P.probe(seed,np.array(s),np.array(d,float))
          16 +        if res is None: print(name,msg); continue
          17 +        surf=res[1][ax]-r*np.array(d)[ax]
          18 +        print('  %-24s surface=%.4f predicted=%.4f err=%.5f'%(name,surf,pred,surf-pred))
diff --git a/geom_lib.py b/geom_lib.py
new file mode 100644
index 0000000..dfec0cf
--- /dev/null
+++ b/geom_lib.py
@@ -0,0 +1,48 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +R=1.6
           4 +def rot(th): c,s=np.cos(th),np.sin(th); return np.array([[c,-s],[s,c]])
           5 +class Prober:
           6 +    def __init__(s): s.env=make_env()
           7 +    def reset(s,seed):
           8 +        s.seed=seed; s.obs,_=s.env.reset(seed=seed); s.b0=s.obs[0:3].copy(); return s.obs
           9 +    def moved(s): return np.max(np.abs(s.obs[0:3]-s.b0))>1e-7
          10 +    def step(s,a):
          11 +        s.obs,*_=s.env.step(np.clip(np.asarray(a,float),-0.0499,0.0499))
          12 +    def goto(s,p,maxstep=0.04):
          13 +        for _ in range(2000):
          14 +            d=p-s.obs[16:18]; n=np.linalg.norm(d)
          15 +            if n<1e-9: return
          16 +            a=d if n<=maxstep else d/n*maxstep
          17 +            s.step(a)
          18 +            if n<=maxstep: return
          19 +    def nav(s,world_pt):
          20 +        c=s.b0[:2]; r=s.obs[16:18]-c; ang=np.arctan2(r[1],r[0])
          21 +        s.goto(c+R*np.array([np.cos(ang),np.sin(ang)]))
          22 +        v=world_pt-c; tang=np.arctan2(v[1],v[0])
          23 +        da=(tang-ang+np.pi)%(2*np.pi)-np.pi
          24 +        n=int(abs(da)/0.02)+1
          25 +        for k in range(1,n+1):
          26 +            a=ang+da*k/n; s.goto(c+R*np.array([np.cos(a),np.sin(a)]))
          27 +        s.goto(world_pt)
          28 +    def probe(s,seed,start_b,dir_b,maxdist=2.0,fine=0.0002):
          29 +        """start_b, dir_b in body frame. returns distance travelled at contact (bounds)."""
          30 +        th=s.b0[2]; M=rot(th)
          31 +        s.reset(seed); c=s.b0[:2]; start_w=c+M@start_b; d=M@(dir_b/np.linalg.norm(dir_b))
          32 +        s.nav(start_w)
          33 +        if s.moved(): return None,'moved during nav'
          34 +        p0=s.obs[16:18].copy(); t=0
          35 +        while t<maxdist:
          36 +            prev=s.obs[16:18].copy(); s.step(d*0.005); t+=0.005
          37 +            if s.moved(): break
          38 +        else: return None,'no contact'
          39 +        coarse=np.dot(prev-p0,d)
          40 +        s.reset(seed); s.nav(start_w); p0=s.obs[16:18].copy()
          41 +        s.goto(p0+d*(coarse-0.006),0.005)
          42 +        while True:
          43 +            prev=s.obs[16:18].copy(); s.step(d*fine)
          44 +            if s.moved(): break
          45 +        dprev=np.dot(prev-p0,d); dnow=np.dot(s.obs[16:18]-p0,d)
          46 +        # contact point robot center in body frame
          47 +        pb_prev=M.T@(prev-c); pb_now=M.T@(s.obs[16:18]-c)
          48 +        return (pb_prev,pb_now),'ok'
diff --git a/geom_limits.py b/geom_limits.py
new file mode 100644
index 0000000..d7899c8
--- /dev/null
+++ b/geom_limits.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env()
           4 +obs,_=env.reset(seed=0)
           5 +for a in [[0.0499,0],[0.04999999,0],[0.05,0],[0,0.05],[-0.05,0],[0.035,0.035],[0.049,0.049],[0.0499,0.0499],[-0.0499,-0.0499]]:
           6 +    try:
           7 +        o,*_=env.step(np.array(a,dtype=float)); print(a,'ok', o[16:18]-obs[16:18]); obs=o
           8 +    except Exception as e:
           9 +        print(a,'ERR',repr(e)[:300]); env.close(); env=make_env(); obs,_=env.reset(seed=0)
          10 +try:
          11 +    o,*_=env.step(np.array([0.05,0],dtype=np.float32)); print('f32 ok')
          12 +except Exception as e: print('f32 ERR',repr(e)[:200])
diff --git a/geom_radial.py b/geom_radial.py
new file mode 100644
index 0000000..1f40ba4
--- /dev/null
+++ b/geom_radial.py
@@ -0,0 +1,9 @@
           1 +from geom_lib import *
           2 +import sys
           3 +P=Prober(); seed=int(sys.argv[1])
           4 +o=P.reset(seed); print('seed',seed,'w,Lh,Lv',o[12:15],'r',o[28])
           5 +for k in range(24):
           6 +    a=2*np.pi*k/24; u=np.array([np.cos(a),np.sin(a)])
           7 +    res,msg=P.probe(seed,1.5*u,-u)
           8 +    if res is None: print(k,msg); continue
           9 +    print('ang %5.1f contact robot body pos prev %s now %s'%(np.degrees(a),np.round(res[0],4),np.round(res[1],4)))
diff --git a/geom_seeds.py b/geom_seeds.py
new file mode 100644
index 0000000..48ceb09
--- /dev/null
+++ b/geom_seeds.py
@@ -0,0 +1,6 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env()
           4 +for s in range(60):
           5 +    o,_=env.reset(seed=s)
           6 +    if 1.7<o[0]<3.3 and 1.7<o[1]<3.3: print(s, np.round(o[[0,1,2,12,13,14,16,17]],4))
diff --git a/geom_wall.py b/geom_wall.py
new file mode 100644
index 0000000..ea0ed8d
--- /dev/null
+++ b/geom_wall.py
@@ -0,0 +1,17 @@
           1 +from geom_lib import *
           2 +def corners(o):
           3 +    x,y,th=o[0:3]; w,Lh,Lv=o[12:15]; M=rot(th)
           4 +    pts=np.array([[-Lh/2,0],[Lh/2,0],[Lh/2,-w],[-Lh/2,-w],[w/2,-w-Lv],[-w/2,-w-Lv]])
           5 +    return (M@pts.T).T+[x,y]
           6 +if __name__=="__main__":
           7 +  P=Prober()
           8 +  for seed,d in [(1,(1,0)),(12,(1,0)),(12,(-1,0)),(12,(0,1)),(12,(0,-1))]:
           9 +      o=P.reset(seed); d=np.array(d,float); c=P.b0[:2]
          10 +      # go behind block (opposite side), then push through center line
          11 +      P.nav(c-d*1.55)
          12 +      ext=[]
          13 +      for k in range(200):
          14 +          P.step(d*0.0499)
          15 +          ext.append(np.max(corners(P.obs)@d))
          16 +      print('seed',seed,'dir',d,'robot',np.round(P.obs[16:18],3),'block',np.round(P.obs[0:3],3),'block extreme along dir: max %.3f final %.3f'%(max(ext),ext[-1]))
          17 +  
\ No newline at end of file
diff --git a/geom_wall2.py b/geom_wall2.py
new file mode 100644
index 0000000..1b6ca7c
--- /dev/null
+++ b/geom_wall2.py
@@ -0,0 +1,13 @@
           1 +from geom_lib import *
           2 +from geom_wall import corners
           3 +P=Prober()
           4 +for seed in [12,20,24,31]:
           5 +    o=P.reset(seed); th=P.b0[2]; M=rot(th); c=P.b0[:2]
           6 +    d=M@np.array([0,-1.0])  # stem direction
           7 +    P.nav(c+M@np.array([0,0.5]))
           8 +    lo,hi=[],[]
           9 +    for k in range(150):
          10 +        P.step(d*0.03)
          11 +        cs=corners(P.obs); lo.append(cs.min(0)); hi.append(cs.max(0))
          12 +    lo=np.min(lo,0); hi=np.max(hi,0)
          13 +    print('seed',seed,'stemdir',np.round(d,2),'robot',np.round(P.obs[16:18],3),'block',np.round(P.obs[0:3],3),'corner min',np.round(lo,3),'max',np.round(hi,3))
diff --git a/geom_wrap.py b/geom_wrap.py
new file mode 100644
index 0000000..7babea3
--- /dev/null
+++ b/geom_wrap.py
@@ -0,0 +1,10 @@
           1 +from geom_lib import *
           2 +P=Prober()
           3 +for seed in [22,16]:
           4 +    o=P.reset(seed); th=P.b0[2]; M=rot(th); c=P.b0[:2]
           5 +    print('seed',seed,'theta0',th)
           6 +    P.nav(c+M@np.array([0.45,-0.5]))
           7 +    ths=[]
           8 +    for k in range(200):
           9 +        P.step(M@np.array([0,1.0])*0.005); ths.append(P.obs[2])
          10 +    print('  theta traj', np.round(ths[40::8],4))
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..37f5560
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,26 @@
           1 +import sys, time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from concurrent.futures import ThreadPoolExecutor
           5 +def run(seed):
           6 +    env = make_env()
           7 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           8 +    obs, info = env.reset(seed=seed)
           9 +    ap.reset(obs, info)
          10 +    t0 = time.time(); ok=False
          11 +    for t in range(env.max_steps):
          12 +        a = ap.get_action(obs)
          13 +        obs, r, term, trunc, info = env.step(a)
          14 +        if term: ok=True; break
          15 +        if trunc: break
          16 +    dt=time.time()-t0
          17 +    e = (obs[0]-obs[29], obs[1]-obs[30], (obs[2]-obs[31]+np.pi)%(2*np.pi)-np.pi)
          18 +    env.close()
          19 +    return seed, ok, t+1, dt, e
          20 +if __name__=='__main__':
          21 +    a,b = int(sys.argv[1]), int(sys.argv[2])
          22 +    with ThreadPoolExecutor(8) as ex:
          23 +        res = list(ex.map(run, range(a,b)))
          24 +    for s,ok,n,dt,e in res:
          25 +        print(s, ok, n, f'{dt:.1f}s', np.round(e,3))
          26 +    print('success', sum(r[1] for r in res), '/', len(res), 'mean steps', np.mean([r[2] for r in res]))
```

</details>

<a id="C003"></a>
### C003 · Better retreat from contact, relaxed start clearance, fallback move

Commit `aaedd14c6da7992be16f0c9e2f0dd2c03677f007`; parents: b7366c092dfeaf4a2e197d86d3a5578f430a5451. Recorded author date: 2026-09-30T17:10:57+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0289](01_timeline.md#E0289): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_aaedd14_approach.py) · [Exact all-file diff](evidence/diffs/C003_aaedd14.diff)

[Previous saved controller snapshot](evidence/versions/C002_b7366c0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 80210c9..8a095a3 100644
--- a/approach.py
+++ b/approach.py
@@ -88,6 +88,8 @@ class GeneratedApproach:
   88     88          return e_ref + e_com + 0.6 * np.abs(dth)
   89     89  
   90     90      def seg_free(self, pose, a, b, clear):
          91 +        if a is self.start_pt:
          92 +            clear = min(clear, self.start_d - 0.004)
   91     93          n = max(2, int(np.linalg.norm(b - a) / 0.01) + 1)
   92     94          t = np.linspace(0, 1, n)[:, None]
   93     95          P = a[None] + t * (b - a)[None]
@@ -207,22 +209,30 @@ class GeneratedApproach:
  207    209          paths = [None] * K
  208    210          self.build_nodes(pose)
  209    211          start = robot.copy()
  210        -        # retreat if touching
         212 +        prefix = []
  211    213          rb = (robot - pose[0:2]) @ R0
  212    214          dd = g.dist_body(rb[None])[0]
  213        -        prefix = []
  214    215          if dd < RAD + 0.03:
  215        -            # outward direction approx: numeric gradient
  216        -            eps = 1e-3
  217        -            gx = g.dist_body((rb + [eps, 0])[None])[0] - g.dist_body((rb - [eps, 0])[None])[0]
  218        -            gy = g.dist_body((rb + [0, eps])[None])[0] - g.dist_body((rb - [0, eps])[None])[0]
  219        -            gv = np.array([gx, gy])
  220        -            if np.linalg.norm(gv) < 1e-9:
  221        -                gv = rb - g.C
  222        -            gv = R0 @ (gv / np.linalg.norm(gv))
  223        -            st = np.clip(robot + gv * (RAD + 0.035 - dd), LO + 0.005, HI - 0.005)
  224        -            prefix = [st]
  225        -            start = st
         216 +            # retreat: pick direction maximizing clearance
         217 +            angs_r = np.linspace(0, 2 * np.pi, 24, endpoint=False)
         218 +            dirs = np.stack([np.cos(angs_r), np.sin(angs_r)], 1)
         219 +            bestd, bestp = -1, None
         220 +            for mag in (0.04, 0.08):
         221 +                P = rb[None] + dirs * mag
         222 +                Pw = pose[0:2] + P @ R0.T
         223 +                dv = g.dist_body(P)
         224 +                inb = np.all((Pw >= LO + 0.005) & (Pw <= HI - 0.005), 1)
         225 +                dv = np.where(inb, dv, -1)
         226 +                j = int(np.argmax(dv))
         227 +                if dv[j] > bestd + 0.01:
         228 +                    bestd, bestp = dv[j], Pw[j]
         229 +                if bestd > RAD + 0.02:
         230 +                    break
         231 +            if bestp is not None:
         232 +                prefix = [bestp]
         233 +                start = bestp
         234 +        self.start_d = g.dist_body(((start - pose[0:2]) @ R0)[None])[0]
         235 +        self.start_pt = start
  226    236          pre_body = (pre - pose[0:2]) @ R0
  227    237          pre_ok = g.dist_body(pre_body) > RAD + 0.015
  228    238          pre_ok &= np.all((pre >= LO + 0.005) & (pre <= HI - 0.005), 1)
@@ -266,7 +276,7 @@ class GeneratedApproach:
  266    276          push_steps = results_len / AMAX + 3
  267    277          order = np.argsort(-(imp / (lb + push_steps + 4)))
  268    278          best_i, best_rate, best_path = None, -np.inf, None
  269        -        for i in order[:25]:
         279 +        for i in order[:60]:
  270    280              if not np.isfinite(results_E[i]) or imp[i] <= 1e-4:
  271    281                  continue
  272    282              ub_rate = imp[i] / (lb[i] + push_steps[i] + 4)
@@ -313,8 +323,13 @@ class GeneratedApproach:
  313    323          if not self.plan:
  314    324              p = self.plan_push(s)
  315    325              if p is None:
  316        -                # fallback: small random-ish wiggle away
  317        -                a = np.array([0.0, 0.0])
         326 +                # fallback: move away from the block, towards the arena centre
         327 +                com = s[0:2] + rot(s[2]) @ self.g.C
         328 +                d = s[16:18] - com
         329 +                d = d / (np.linalg.norm(d) + 1e-9) + 0.5 * (np.array([2.5, 2.5]) - s[16:18]) / 2.5
         330 +                d = d / (np.linalg.norm(d) + 1e-9)
         331 +                self.plan = [('nav', d * AMAX)] * 3
         332 +                _, a = self.plan.pop(0)
  318    333                  return self._safe(s, a)
  319    334              self.plan = self.build_actions(s[16:18], p)
  320    335          _, a = self.plan.pop(0)
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..91be273
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,16 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +from approach import GeneratedApproach
           5 +seed=int(sys.argv[1])
           6 +env=make_env(); ap=GeneratedApproach(None,None,{})
           7 +obs,info=env.reset(seed=seed); ap.reset(obs,info)
           8 +orig=ap.plan_push
           9 +def pp(s):
          10 +    p=orig(s)
          11 +    print('t',t,'pose',np.round(s[0:3],3),'goal',np.round(s[29:32],3),'robot',np.round(s[16:18],2), 'plan', None if p is None else (len(p['path']), np.round(p['u'],2), round(p['L'],2), round(p['E0'],3), round(p['Epred'],3)))
          12 +    return p
          13 +ap.plan_push=pp
          14 +for t in range(int(sys.argv[2])):
          15 +    a=ap.get_action(obs); obs,r,te,tr,_=env.step(a)
          16 +    if te: print('done',t); break
```

</details>

<a id="C004"></a>
### C004 · Relative wall bounds when block starts near a wall

Commit `6bf13553402e17c17fc6574b1f48e87a37ad49da`; parents: aaedd14c6da7992be16f0c9e2f0dd2c03677f007. Recorded author date: 2026-09-30T17:13:43+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0311](01_timeline.md#E0311): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_6bf1355_approach.py) · [Exact all-file diff](evidence/diffs/C004_6bf1355.diff)

[Previous saved controller snapshot](evidence/versions/C003_aaedd14_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8a095a3..d0ff213 100644
--- a/approach.py
+++ b/approach.py
@@ -240,7 +240,9 @@ class GeneratedApproach:
  240    240          # lower bound travel (straight line) for pruning
  241    241          lb = np.max(np.abs(pre - start), 1) / AMAX + len(prefix)
  242    242  
  243        -        pusher = pre.copy()
         243 +        cw = pose[0:2] + g.corners @ R0.T
         244 +        wlo = np.minimum(0.03, cw.min(0) - 0.01)
         245 +        whi = np.maximum(4.97, cw.max(0) + 0.01)
  244    246          results_len = np.zeros(K)
  245    247          results_E = np.full(K, np.inf)
  246    248          stepcnt = standoff / ds
@@ -261,7 +263,7 @@ class GeneratedApproach:
  261    263              # wall check on corners
  262    264              cx = ref[:, 0][:, None] + c[:, None] * g.corners[None, :, 0] - sn[:, None] * g.corners[None, :, 1]
  263    265              cy = ref[:, 1][:, None] + sn[:, None] * g.corners[None, :, 0] + c[:, None] * g.corners[None, :, 1]
  264        -            valid &= (cx.min(1) > 0.03) & (cx.max(1) < 4.97) & (cy.min(1) > 0.03) & (cy.max(1) < 4.97)
         266 +            valid &= (cx.min(1) > wlo[0]) & (cx.max(1) < whi[0]) & (cy.min(1) > wlo[1]) & (cy.max(1) < whi[1])
  265    267              pw = pre + uw * (standoff + k * ds)
  266    268              valid &= np.all((pw >= LO + 0.005) & (pw <= HI - 0.005), 1)
  267    269              if not valid.any():
diff --git a/res_100_300.txt b/res_100_300.txt
new file mode 100644
index 0000000..197b158
--- /dev/null
+++ b/res_100_300.txt
@@ -0,0 +1,201 @@
           1 +100 True 276 5.9s [-0.018  0.013  0.001]
           2 +101 True 146 2.6s [-0.015  0.021  0.017]
           3 +102 True 139 1.9s [-0.015  0.014 -0.002]
           4 +103 True 304 6.6s [ 0.018 -0.029  0.022]
           5 +104 True 135 2.9s [0.027 0.016 0.032]
           6 +105 True 189 3.5s [-0.    -0.002  0.09 ]
           7 +106 True 137 2.3s [-0.017  0.014  0.032]
           8 +107 True 107 1.5s [ 0.028 -0.027 -0.091]
           9 +108 True 183 4.8s [ 0.016 -0.013 -0.013]
          10 +109 True 208 5.5s [ 0.016 -0.006 -0.011]
          11 +110 True 201 5.7s [ 0.027 -0.014 -0.047]
          12 +111 True 232 5.8s [-0.006 -0.022  0.043]
          13 +112 False 1000 23.2s [-2.115  0.083 -2.045]
          14 +113 True 150 3.8s [-0.037 -0.002  0.126]
          15 +114 True 265 7.6s [-0.004 -0.001 -0.042]
          16 +115 True 319 9.7s [0.003 0.019 0.003]
          17 +116 True 271 6.8s [-0.023  0.015  0.12 ]
          18 +117 True 125 3.8s [-0.012  0.016  0.005]
          19 +118 True 263 7.7s [ 0.022 -0.021  0.077]
          20 +119 True 286 7.9s [0.017 0.01  0.044]
          21 +120 True 130 3.7s [-0.017 -0.025 -0.075]
          22 +121 True 165 4.6s [ 0.003  0.013 -0.006]
          23 +122 True 194 5.9s [ 0.02   0.021 -0.055]
          24 +123 True 275 5.5s [-0.021  0.028 -0.015]
          25 +124 True 343 9.2s [0.011 0.013 0.   ]
          26 +125 True 109 2.8s [-0.016  0.019  0.111]
          27 +126 True 165 4.5s [ 0.012  0.01  -0.017]
          28 +127 True 457 12.6s [0.02  0.005 0.007]
          29 +128 True 155 4.0s [0.028 0.025 0.07 ]
          30 +129 True 61 1.5s [-0.025 -0.021  0.028]
          31 +130 True 309 7.7s [-0.02   0.002  0.002]
          32 +131 True 233 5.3s [ 0.025 -0.015  0.005]
          33 +132 True 187 5.0s [0.015 0.006 0.04 ]
          34 +133 True 241 6.3s [ 0.003  0.018 -0.001]
          35 +134 True 227 6.3s [-0.018 -0.016  0.112]
          36 +135 True 146 4.0s [0.007 0.007 0.062]
          37 +136 True 230 6.3s [0.022 0.011 0.011]
          38 +137 True 157 5.0s [-0.     0.017  0.003]
          39 +138 True 263 8.0s [-0.009  0.015  0.004]
          40 +139 True 88 2.7s [-0.016  0.017 -0.08 ]
          41 +140 True 225 6.4s [ 0.019  0.011 -0.098]
          42 +141 True 206 5.6s [-0.019  0.014  0.067]
          43 +142 True 214 5.9s [-0.016  0.018 -0.02 ]
          44 +143 True 200 5.9s [-0.002  0.017  0.088]
          45 +144 True 259 8.1s [ 0.02  -0.014 -0.073]
          46 +145 True 148 3.6s [-0.018  0.004  0.123]
          47 +146 True 118 3.5s [ 0.013 -0.009 -0.113]
          48 +147 True 114 3.7s [0.025 0.012 0.087]
          49 +148 True 174 4.7s [-0.    -0.    -0.001]
          50 +149 True 136 3.7s [-0.     0.015  0.085]
          51 +150 True 126 3.0s [-0.02  -0.01   0.033]
          52 +151 True 299 8.6s [ 0.008  0.022 -0.061]
          53 +152 True 100 3.1s [-0.016  0.017  0.042]
          54 +153 True 91 2.7s [ 0.017 -0.004 -0.006]
          55 +154 True 164 4.6s [-0.023 -0.003 -0.01 ]
          56 +155 True 123 3.2s [ 0.006 -0.019  0.007]
          57 +156 True 185 4.4s [-0.006  0.019  0.019]
          58 +157 True 133 3.2s [0.001 0.017 0.003]
          59 +158 True 86 2.6s [-0.02   0.01   0.011]
          60 +159 True 202 5.7s [-0.016  0.007 -0.036]
          61 +160 True 159 4.0s [0.012 0.016 0.005]
          62 +161 True 257 6.5s [ 0.019  0.018 -0.004]
          63 +162 True 108 3.0s [-0.021  0.015  0.058]
          64 +163 True 235 5.8s [-0.024  0.02  -0.048]
          65 +164 True 89 1.6s [ 0.014 -0.026  0.036]
          66 +165 True 200 4.9s [-0.002 -0.001 -0.001]
          67 +166 True 155 3.5s [-0.017 -0.001 -0.098]
          68 +167 True 91 1.9s [ 0.018  0.005 -0.003]
          69 +168 True 222 5.4s [-0.011  0.008 -0.088]
          70 +169 True 146 3.4s [ 0.003  0.02  -0.01 ]
          71 +170 True 147 3.7s [ 0.002  0.019 -0.005]
          72 +171 True 162 4.6s [ 0.016  0.005 -0.043]
          73 +172 True 193 4.4s [ 0.007 -0.018  0.016]
          74 +173 True 365 9.5s [0.016 0.013 0.01 ]
          75 +174 False 1000 22.6s [-0.815  0.298 -2.398]
          76 +175 True 106 2.5s [-0.027  0.008 -0.124]
          77 +176 True 201 4.1s [ 0.015  0.013 -0.021]
          78 +177 True 172 3.5s [-0.009  0.019 -0.014]
          79 +178 True 204 5.5s [-0.025  0.03  -0.09 ]
          80 +179 True 252 6.4s [-0.014 -0.015 -0.018]
          81 +180 True 191 5.0s [-0.018  0.014  0.011]
          82 +181 True 269 7.5s [-0.017 -0.    -0.007]
          83 +182 True 252 8.2s [-0.018 -0.02  -0.004]
          84 +183 True 192 5.1s [-0.026  0.027  0.021]
          85 +184 True 255 7.1s [-0.004  0.016 -0.003]
          86 +185 True 89 2.5s [ 0.018 -0.018  0.047]
          87 +186 True 117 3.6s [0.019 0.002 0.003]
          88 +187 True 154 4.5s [-0.017  0.003  0.035]
          89 +188 True 233 6.1s [ 0.012 -0.004 -0.009]
          90 +189 True 245 7.1s [ 0.003 -0.013 -0.093]
          91 +190 True 139 3.6s [-0.01  -0.025 -0.018]
          92 +191 True 35 1.0s [-0.003  0.029  0.027]
          93 +192 True 260 8.1s [-0.014  0.011  0.026]
          94 +193 False 1000 24.8s [-0.066  2.129 -2.388]
          95 +194 True 218 6.7s [-0.017 -0.011  0.053]
          96 +195 True 182 5.6s [0.012 0.012 0.002]
          97 +196 True 121 3.3s [-0.008 -0.016 -0.117]
          98 +197 True 180 5.2s [-0.013 -0.024 -0.027]
          99 +198 True 218 6.3s [-0.013 -0.016  0.006]
         100 +199 True 62 1.6s [-0.005 -0.014 -0.01 ]
         101 +200 True 165 5.9s [0.014 0.025 0.038]
         102 +201 True 145 3.5s [ 0.01  -0.007  0.   ]
         103 +202 True 298 8.4s [ 0.006  0.019 -0.001]
         104 +203 True 198 5.4s [-0.007 -0.015 -0.016]
         105 +204 True 199 5.6s [-0.026  0.012  0.002]
         106 +205 True 297 8.9s [ 0.023  0.013 -0.083]
         107 +206 True 266 7.7s [ 0.026 -0.026 -0.006]
         108 +207 True 130 3.8s [ 0.028  0.004 -0.031]
         109 +208 True 129 3.2s [-0.02   0.012 -0.043]
         110 +209 True 199 5.1s [-0.021  0.002 -0.024]
         111 +210 True 329 8.7s [-0.019 -0.012  0.012]
         112 +211 True 110 2.6s [-0.001  0.007 -0.083]
         113 +212 True 103 2.9s [ 0.003 -0.015 -0.015]
         114 +213 True 151 4.4s [ 0.013  0.005 -0.002]
         115 +214 True 230 6.6s [ 0.005 -0.016 -0.119]
         116 +215 True 201 5.9s [-0.02  -0.012  0.03 ]
         117 +216 True 285 8.7s [-0.014  0.011  0.006]
         118 +217 True 165 4.5s [ 0.013  0.018 -0.098]
         119 +218 True 244 6.6s [ 0.02  -0.008 -0.002]
         120 +219 True 190 5.8s [ 0.009 -0.016 -0.044]
         121 +220 True 273 8.3s [-0.006  0.011 -0.058]
         122 +221 True 36 1.1s [ 0.011 -0.018 -0.07 ]
         123 +222 True 179 4.8s [-0.006 -0.02  -0.008]
         124 +223 True 311 8.4s [0.016 0.006 0.043]
         125 +224 True 195 5.7s [ 0.011 -0.013 -0.059]
         126 +225 True 117 3.5s [0.023 0.023 0.094]
         127 +226 True 228 6.4s [ 0.015 -0.021 -0.013]
         128 +227 True 311 7.8s [ 0.006 -0.015  0.064]
         129 +228 True 226 5.9s [0.009 0.025 0.055]
         130 +229 True 272 6.3s [-0.001  0.004  0.072]
         131 +230 True 192 4.3s [-0.013 -0.004 -0.009]
         132 +231 True 292 6.8s [ 0.021  0.017 -0.027]
         133 +232 True 192 4.5s [ 0.008  0.016 -0.117]
         134 +233 True 161 3.4s [-0.018  0.009 -0.001]
         135 +234 True 123 3.0s [ 0.002  0.014 -0.029]
         136 +235 True 277 6.0s [ 0.025  0.006 -0.008]
         137 +236 True 173 4.0s [-0.017  0.01   0.018]
         138 +237 True 175 3.7s [ 0.013  0.018 -0.01 ]
         139 +238 True 321 6.7s [ 0.013 -0.004 -0.01 ]
         140 +239 True 113 2.3s [-0.017 -0.012  0.019]
         141 +240 True 186 3.8s [-0.009 -0.018  0.027]
         142 +241 True 203 4.2s [0.023 0.012 0.04 ]
         143 +242 True 177 3.2s [ 0.013 -0.015 -0.002]
         144 +243 True 211 4.5s [0.021 0.001 0.078]
         145 +244 True 182 4.0s [ 0.012 -0.015 -0.011]
         146 +245 True 198 4.3s [ 0.019 -0.    -0.024]
         147 +246 True 144 3.3s [-0.02  -0.023  0.087]
         148 +247 True 359 9.3s [-0.008  0.019 -0.106]
         149 +248 False 1000 19.2s [-1.194 -0.417 -2.407]
         150 +249 True 281 5.4s [-0.006  0.012  0.077]
         151 +250 True 141 3.3s [-0.025  0.017  0.131]
         152 +251 True 146 3.7s [ 0.021 -0.011  0.01 ]
         153 +252 True 260 6.2s [-0.016 -0.013 -0.015]
         154 +253 True 327 8.2s [ 0.004  0.019 -0.021]
         155 +254 True 218 4.4s [ 0.007 -0.017  0.003]
         156 +255 True 32 0.7s [-0.013 -0.012 -0.043]
         157 +256 True 339 8.1s [ 0.02  -0.015  0.089]
         158 +257 True 173 4.1s [ 0.017  0.002 -0.011]
         159 +258 True 122 3.2s [ 0.003 -0.022 -0.016]
         160 +259 True 129 3.3s [ 0.003 -0.009 -0.082]
         161 +260 True 230 6.0s [-0.011 -0.014  0.005]
         162 +261 True 133 3.1s [-0.012 -0.007  0.098]
         163 +262 True 142 2.8s [ 0.023 -0.015 -0.085]
         164 +263 True 161 4.2s [ 0.004 -0.02  -0.013]
         165 +264 True 207 6.6s [-0.013 -0.014 -0.052]
         166 +265 True 142 3.0s [-0.023  0.011 -0.026]
         167 +266 True 167 5.1s [ 0.021 -0.003  0.014]
         168 +267 True 278 8.8s [ 0.015  0.011 -0.054]
         169 +268 True 183 6.4s [-0.017 -0.01  -0.024]
         170 +269 True 372 11.3s [-0.017 -0.018  0.004]
         171 +270 True 177 5.3s [ 0.012 -0.016 -0.008]
         172 +271 True 164 4.8s [ 0.003 -0.014 -0.016]
         173 +272 True 265 8.3s [-0.007  0.021  0.064]
         174 +273 True 78 1.5s [0.02  0.011 0.015]
         175 +274 True 233 6.8s [-0.015  0.013 -0.015]
         176 +275 True 74 2.1s [-0.015  0.003  0.082]
         177 +276 True 251 7.5s [ 0.004  0.017 -0.019]
         178 +277 True 182 5.4s [-0.004  0.02  -0.018]
         179 +278 True 178 4.6s [-0.018 -0.022  0.026]
         180 +279 True 247 7.2s [ 0.014 -0.019  0.01 ]
         181 +280 True 151 5.1s [-0.012  0.015  0.003]
         182 +281 True 112 4.0s [ 0.005 -0.008 -0.101]
         183 +282 True 193 5.2s [-0.001  0.02  -0.037]
         184 +283 True 218 5.2s [ 0.007 -0.022  0.026]
         185 +284 True 186 4.8s [ 0.021  0.015 -0.01 ]
         186 +285 True 232 6.8s [-0.019 -0.016  0.026]
         187 +286 True 43 1.3s [-0.001 -0.032  0.123]
         188 +287 True 202 4.6s [-0.02  -0.014  0.009]
         189 +288 True 161 4.1s [-0.004  0.014 -0.062]
         190 +289 True 216 5.4s [-0.002  0.012  0.079]
         191 +290 True 263 6.7s [-0.01   0.013 -0.125]
         192 +291 True 277 6.9s [-0.02  -0.007 -0.087]
         193 +292 True 138 3.9s [-0.013  0.019  0.041]
         194 +293 True 224 6.3s [-0.019 -0.008  0.033]
         195 +294 True 316 6.3s [0.019 0.012 0.011]
         196 +295 True 278 6.2s [ 0.017 -0.01   0.006]
         197 +296 True 190 4.5s [ 0.021 -0.006 -0.006]
         198 +297 True 86 2.5s [-0.012  0.009  0.061]
         199 +298 True 196 3.4s [-0.004 -0.02   0.008]
         200 +299 True 204 2.7s [-0.016  0.005 -0.052]
         201 +success 196 / 200 mean steps 210.145
diff --git a/test_list.py b/test_list.py
new file mode 100644
index 0000000..13d3401
--- /dev/null
+++ b/test_list.py
@@ -0,0 +1,8 @@
           1 +import sys, numpy as np
           2 +from test_approach import run
           3 +from concurrent.futures import ThreadPoolExecutor
           4 +seeds=[int(x) for x in sys.argv[1:]]
           5 +with ThreadPoolExecutor(8) as ex:
           6 +    res=list(ex.map(run, seeds))
           7 +for s,ok,n,dt,e in res: print(s,ok,n,f'{dt:.1f}s',np.round(e,3))
           8 +print('success', sum(r[1] for r in res), '/', len(res), 'mean steps', np.mean([r[2] for r in res]))
```

</details>

<a id="C005"></a>
### C005 · results

Commit `1dcac3607669f95bedf7710bea56e4be49df6ed0`; parents: 6bf13553402e17c17fc6574b1f48e87a37ad49da. Recorded author date: 2026-09-30T17:16:54+02:00.

File roles (automatic): setup/other.

- [E0327](01_timeline.md#E0327): commit title in command; output may not confirm creation.
- [E0334](01_timeline.md#E0334): commit title in command; output may not confirm creation.
- [E0407](01_timeline.md#E0407): commit title in command; output may not confirm creation.
- [E0644](01_timeline.md#E0644): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C005_1dcac36.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res_300_600.txt b/res_300_600.txt
new file mode 100644
index 0000000..2feb295
--- /dev/null
+++ b/res_300_600.txt
@@ -0,0 +1,301 @@
           1 +300 True 205 6.0s [-0.023  0.008  0.046]
           2 +301 True 174 4.7s [ 0.013 -0.028  0.036]
           3 +302 True 215 4.9s [-0.023  0.013  0.02 ]
           4 +303 True 184 3.6s [0.003 0.02  0.017]
           5 +304 True 201 5.2s [-0.015  0.027 -0.027]
           6 +305 True 136 2.9s [0.013 0.006 0.078]
           7 +306 True 288 7.9s [0.017 0.02  0.002]
           8 +307 True 232 7.0s [-0.02   0.005 -0.009]
           9 +308 True 259 8.7s [ 0.012 -0.006 -0.002]
          10 +309 True 158 5.0s [ 0.012  0.014 -0.002]
          11 +310 True 158 3.9s [ 0.008 -0.022 -0.108]
          12 +311 True 189 6.0s [-0.027 -0.018 -0.032]
          13 +312 True 157 5.1s [0.017 0.014 0.008]
          14 +313 True 128 4.0s [-0.016  0.012  0.001]
          15 +314 True 206 6.6s [ 0.015  0.013 -0.076]
          16 +315 True 259 6.9s [0.018 0.011 0.016]
          17 +316 True 130 3.6s [-0.007  0.025 -0.078]
          18 +317 True 180 5.4s [0.026 0.019 0.019]
          19 +318 True 132 2.6s [ 0.014  0.022 -0.057]
          20 +319 True 288 7.8s [0.025 0.015 0.083]
          21 +320 True 92 2.6s [-0.004  0.012  0.041]
          22 +321 True 178 5.5s [ 0.018 -0.017 -0.053]
          23 +322 True 220 6.7s [ 0.023 -0.027  0.011]
          24 +323 True 274 7.7s [-0.029 -0.002 -0.01 ]
          25 +324 True 306 8.4s [-0.004 -0.02  -0.048]
          26 +325 True 99 3.5s [ 0.02   0.008 -0.008]
          27 +326 True 287 7.8s [-0.003  0.014 -0.015]
          28 +327 True 330 9.7s [ 0.02  -0.012 -0.01 ]
          29 +328 True 339 8.8s [ 0.015  0.02  -0.004]
          30 +329 True 134 3.5s [-0.001 -0.013  0.112]
          31 +330 True 253 7.0s [ 0.024 -0.003  0.11 ]
          32 +331 True 211 6.5s [0.006 0.02  0.021]
          33 +332 True 120 3.6s [-0.019 -0.006  0.091]
          34 +333 True 184 5.0s [0.017 0.016 0.066]
          35 +334 True 354 8.1s [0.012 0.016 0.003]
          36 +335 True 188 5.1s [-0.017 -0.018 -0.01 ]
          37 +336 True 177 3.8s [-0.003  0.016 -0.02 ]
          38 +337 True 263 7.2s [ 0.017 -0.001  0.009]
          39 +338 True 257 7.4s [ 0.015 -0.019 -0.017]
          40 +339 True 205 5.7s [0.018 0.007 0.014]
          41 +340 True 130 2.9s [-0.011  0.021 -0.033]
          42 +341 True 221 6.2s [-0.001 -0.022 -0.016]
          43 +342 True 146 4.2s [-0.001  0.015  0.004]
          44 +343 True 152 4.3s [-0.    -0.024  0.006]
          45 +344 True 196 4.0s [ 0.015  0.005 -0.042]
          46 +345 True 136 3.5s [ 0.021 -0.022  0.038]
          47 +346 True 320 8.0s [-0.018  0.009  0.102]
          48 +347 True 249 6.0s [-0.002  0.013  0.011]
          49 +348 True 167 3.5s [0.021 0.007 0.007]
          50 +349 True 241 4.8s [ 0.002 -0.02  -0.004]
          51 +350 True 355 7.0s [-0.014  0.012  0.02 ]
          52 +351 True 204 4.7s [-0.005 -0.018 -0.009]
          53 +352 True 154 3.6s [-0.009  0.009  0.065]
          54 +353 True 240 5.0s [-0.015 -0.017 -0.038]
          55 +354 True 287 6.0s [0.031 0.011 0.076]
          56 +355 True 153 4.0s [ 0.006 -0.019  0.065]
          57 +356 True 202 4.1s [-0.02  -0.004 -0.012]
          58 +357 True 142 2.8s [0.001 0.021 0.07 ]
          59 +358 True 152 3.3s [ 0.017 -0.002 -0.052]
          60 +359 True 209 4.8s [-0.024 -0.026 -0.018]
          61 +360 True 179 4.3s [ 0.011 -0.016 -0.012]
          62 +361 True 187 5.0s [0.019 0.001 0.072]
          63 +362 True 159 4.5s [-0.016  0.013  0.02 ]
          64 +363 True 231 5.9s [ 0.009 -0.015 -0.038]
          65 +364 True 148 4.2s [-0.021 -0.005  0.012]
          66 +365 True 214 5.9s [0.02  0.001 0.03 ]
          67 +366 True 159 3.3s [ 0.004  0.012 -0.096]
          68 +367 True 235 5.2s [-0.023  0.004 -0.086]
          69 +368 True 194 5.7s [0.018 0.015 0.067]
          70 +369 True 98 2.7s [-0.002  0.003 -0.079]
          71 +370 True 239 5.8s [ 0.025 -0.026 -0.039]
          72 +371 True 211 5.1s [-0.021 -0.005 -0.012]
          73 +372 True 270 5.8s [-0.01   0.017 -0.   ]
          74 +373 True 139 3.7s [0.005 0.015 0.04 ]
          75 +374 True 182 4.8s [ 0.013  0.025 -0.102]
          76 +375 True 261 5.7s [-0.02   0.006 -0.002]
          77 +376 True 136 2.9s [0.002 0.018 0.005]
          78 +377 True 233 6.1s [0.022 0.036 0.099]
          79 +378 True 147 4.5s [ 0.009 -0.02  -0.014]
          80 +379 True 284 6.9s [ 0.023 -0.021  0.006]
          81 +380 True 269 5.7s [ 0.021  0.017 -0.004]
          82 +381 True 208 5.6s [ 0.029 -0.001 -0.017]
          83 +382 True 233 5.2s [ 0.009 -0.018 -0.031]
          84 +383 True 303 7.3s [ 0.016 -0.021  0.012]
          85 +384 True 71 1.1s [ 0.004 -0.019 -0.076]
          86 +385 True 152 3.5s [ 0.006  0.001 -0.079]
          87 +386 True 265 6.3s [ 0.007 -0.017  0.06 ]
          88 +387 True 192 4.5s [-0.005  0.005 -0.076]
          89 +388 True 211 5.2s [ 0.014 -0.022 -0.015]
          90 +389 True 151 3.3s [-0.014  0.005  0.052]
          91 +390 True 151 3.4s [-0.022 -0.017 -0.039]
          92 +391 True 228 6.0s [-0.028  0.02  -0.01 ]
          93 +392 True 153 4.0s [-0.017 -0.025 -0.007]
          94 +393 True 266 5.8s [0.021 0.015 0.037]
          95 +394 True 212 4.3s [-0.024  0.019 -0.073]
          96 +395 True 274 6.6s [0.009 0.015 0.009]
          97 +396 True 138 3.0s [-0.002 -0.006  0.127]
          98 +397 True 118 2.9s [0.005 0.014 0.133]
          99 +398 True 136 3.2s [ 0.022 -0.029  0.064]
         100 +399 True 348 8.3s [ 0.013 -0.012 -0.091]
         101 +400 True 58 2.0s [0.019 0.019 0.093]
         102 +401 True 347 8.7s [-0.009  0.018 -0.008]
         103 +402 True 187 4.9s [-0.01  -0.016 -0.003]
         104 +403 True 145 3.4s [-0.021 -0.024  0.048]
         105 +404 True 242 7.0s [ 0.016 -0.008  0.001]
         106 +405 True 244 5.4s [-0.018  0.014 -0.003]
         107 +406 True 328 7.8s [0.018 0.001 0.07 ]
         108 +407 True 232 4.8s [-0.01  -0.01   0.068]
         109 +408 True 135 3.5s [-0.002  0.003  0.089]
         110 +409 True 266 7.8s [ 0.019 -0.003 -0.016]
         111 +410 True 39 0.8s [-0.016  0.     0.097]
         112 +411 True 187 5.5s [ 0.02   0.015 -0.114]
         113 +412 True 177 5.2s [ 0.009 -0.017  0.053]
         114 +413 True 156 4.8s [-0.004 -0.018  0.006]
         115 +414 True 86 2.3s [-0.02  -0.027 -0.095]
         116 +415 True 362 10.4s [ 0.001 -0.     0.085]
         117 +416 True 154 4.6s [-0.021  0.007  0.066]
         118 +417 True 274 7.7s [-0.014  0.016  0.032]
         119 +418 True 152 3.9s [-0.019  0.008 -0.01 ]
         120 +419 True 204 6.6s [-0.013 -0.028  0.044]
         121 +420 True 156 4.7s [ 0.015  0.024 -0.048]
         122 +421 True 162 4.9s [ 0.007 -0.018  0.031]
         123 +422 True 364 11.8s [-0.022  0.    -0.005]
         124 +423 True 66 2.0s [-0.016 -0.005  0.01 ]
         125 +424 True 296 8.3s [ 0.021  0.017 -0.071]
         126 +425 True 164 4.1s [ 0.02  -0.022  0.049]
         127 +426 True 105 2.2s [ 0.028 -0.004 -0.002]
         128 +427 True 54 1.2s [-0.013  0.01  -0.014]
         129 +428 True 239 7.3s [0.009 0.02  0.011]
         130 +429 True 207 6.9s [0.022 0.022 0.041]
         131 +430 True 207 5.6s [ 0.015 -0.004 -0.097]
         132 +431 True 129 3.7s [ 0.015 -0.012 -0.121]
         133 +432 True 138 4.2s [ 0.02  -0.018  0.034]
         134 +433 True 326 10.6s [-0.002  0.012  0.104]
         135 +434 True 211 5.5s [ 0.007 -0.02   0.005]
         136 +435 True 108 2.8s [-0.024  0.027 -0.067]
         137 +436 True 127 3.1s [-0.015 -0.018 -0.064]
         138 +437 True 122 4.9s [0.    0.011 0.067]
         139 +438 True 154 5.0s [-0.022  0.028 -0.073]
         140 +439 True 187 5.7s [-0.001  0.018 -0.001]
         141 +440 True 230 7.7s [-0.001 -0.009  0.067]
         142 +441 True 217 6.4s [ 0.023  0.011 -0.052]
         143 +442 True 116 3.3s [-0.01  -0.002  0.109]
         144 +443 True 135 3.3s [-0.018 -0.017 -0.023]
         145 +444 True 275 8.2s [-0.005  0.013  0.087]
         146 +445 True 198 6.0s [-0.008  0.022 -0.039]
         147 +446 True 94 2.4s [-0.018 -0.029  0.13 ]
         148 +447 True 157 4.9s [0.019 0.022 0.016]
         149 +448 True 37 0.9s [-0.004 -0.013 -0.042]
         150 +449 True 282 8.5s [-0.01  -0.011 -0.086]
         151 +450 True 147 4.5s [ 0.021  0.005 -0.011]
         152 +451 True 260 7.2s [-0.01   0.024  0.102]
         153 +452 True 249 7.0s [0.01  0.016 0.07 ]
         154 +453 True 124 3.9s [-0.002  0.029 -0.119]
         155 +454 True 55 1.8s [0.002 0.017 0.054]
         156 +455 True 162 4.4s [ 0.002 -0.018 -0.005]
         157 +456 True 137 4.3s [-0.016  0.026 -0.041]
         158 +457 True 419 11.0s [ 0.007 -0.015 -0.004]
         159 +458 True 288 8.4s [-0.006  0.023  0.047]
         160 +459 True 150 4.9s [ 0.01   0.02  -0.004]
         161 +460 True 102 2.7s [-0.001 -0.015 -0.014]
         162 +461 True 178 4.7s [0.007 0.021 0.106]
         163 +462 True 419 8.8s [-0.007  0.027  0.033]
         164 +463 True 295 7.2s [ 0.013 -0.018  0.01 ]
         165 +464 True 107 3.0s [-0.021 -0.03   0.088]
         166 +465 True 191 4.7s [-0.018 -0.023 -0.006]
         167 +466 True 127 3.5s [-0.01   0.021  0.12 ]
         168 +467 True 236 4.9s [0.029 0.017 0.041]
         169 +468 True 126 3.3s [ 0.009 -0.005  0.061]
         170 +469 True 149 2.8s [0.018 0.011 0.03 ]
         171 +470 True 209 3.8s [-0.01   0.021  0.004]
         172 +471 True 265 4.3s [0.009 0.012 0.038]
         173 +472 True 123 2.1s [ 0.005  0.014 -0.004]
         174 +473 True 192 3.0s [-0.014 -0.013 -0.072]
         175 +474 True 74 1.2s [-0.005  0.017  0.004]
         176 +475 True 104 1.8s [ 0.023 -0.016 -0.069]
         177 +476 True 236 3.7s [ 0.017  0.002 -0.049]
         178 +477 True 161 2.6s [-0.019  0.015  0.012]
         179 +478 True 117 2.1s [ 0.02   0.011 -0.005]
         180 +479 True 282 4.4s [-0.018 -0.006  0.004]
         181 +480 True 269 3.7s [-0.005  0.01   0.002]
         182 +481 True 282 4.9s [ 0.016 -0.002  0.013]
         183 +482 True 361 5.8s [ 0.01  -0.013 -0.015]
         184 +483 True 139 2.0s [-0.015  0.026  0.063]
         185 +484 True 93 1.3s [ 0.001 -0.016  0.065]
         186 +485 True 224 3.4s [-0.001  0.022 -0.008]
         187 +486 True 334 5.6s [-0.018 -0.014  0.012]
         188 +487 True 195 3.1s [0.011 0.016 0.039]
         189 +488 True 107 1.4s [0.008 0.019 0.079]
         190 +489 True 152 2.2s [ 0.011 -0.016 -0.004]
         191 +490 True 190 3.6s [0.015 0.004 0.123]
         192 +491 True 250 4.1s [0.    0.018 0.005]
         193 +492 True 104 1.4s [-0.011  0.014 -0.102]
         194 +493 True 252 4.3s [-0.005  0.011 -0.008]
         195 +494 True 134 1.9s [ 0.007  0.015 -0.108]
         196 +495 True 198 3.0s [ 0.013  0.026 -0.037]
         197 +496 True 183 2.8s [ 0.018 -0.007 -0.034]
         198 +497 True 223 3.6s [-0.005  0.019  0.057]
         199 +498 True 252 4.1s [-0.009 -0.002  0.076]
         200 +499 True 113 2.0s [0.018 0.023 0.092]
         201 +500 True 97 1.5s [-0.011  0.004 -0.088]
         202 +501 True 201 3.3s [ 0.016 -0.014  0.003]
         203 +502 True 257 4.9s [-0.004 -0.001 -0.111]
         204 +503 True 331 6.9s [ 0.013  0.018 -0.027]
         205 +504 True 157 2.8s [-0.009  0.023 -0.108]
         206 +505 True 306 6.0s [-0.017  0.02  -0.032]
         207 +506 True 28 0.5s [-0.014  0.006 -0.06 ]
         208 +507 True 132 2.7s [ 0.016  0.005 -0.025]
         209 +508 True 146 2.6s [ 0.026  0.004 -0.079]
         210 +509 True 219 5.3s [ 0.005 -0.015 -0.025]
         211 +510 True 108 2.4s [0.014 0.001 0.007]
         212 +511 True 259 5.2s [-0.014  0.014  0.004]
         213 +512 True 219 4.9s [-0.014  0.012 -0.006]
         214 +513 True 144 3.1s [ 0.015  0.016 -0.133]
         215 +514 True 114 2.4s [-0.006  0.021 -0.008]
         216 +515 True 317 6.9s [ 0.001  0.018 -0.028]
         217 +516 True 205 4.7s [ 0.017  0.006 -0.007]
         218 +517 True 165 4.0s [ 0.017 -0.018  0.104]
         219 +518 True 123 2.8s [0.024 0.021 0.007]
         220 +519 True 152 3.3s [-0.022  0.016  0.003]
         221 +520 True 105 1.7s [0.004 0.014 0.001]
         222 +521 True 197 4.3s [ 0.    -0.012  0.113]
         223 +522 True 210 4.3s [0.027 0.01  0.032]
         224 +523 True 125 2.3s [-0.002  0.019  0.005]
         225 +524 True 221 4.8s [-0.013  0.007 -0.105]
         226 +525 True 410 9.1s [ 0.018 -0.008  0.003]
         227 +526 True 257 4.7s [ 0.013 -0.     0.004]
         228 +527 True 179 2.7s [-0.009  0.012  0.084]
         229 +528 True 121 2.5s [ 0.026 -0.018 -0.003]
         230 +529 True 207 3.9s [ 0.019  0.019 -0.002]
         231 +530 True 130 2.4s [-0.018 -0.016 -0.113]
         232 +531 True 46 0.9s [0.007 0.021 0.123]
         233 +532 True 137 2.3s [ 0.015 -0.008 -0.003]
         234 +533 True 241 5.7s [-0.01   0.02   0.074]
         235 +534 True 239 4.4s [-0.025 -0.023  0.024]
         236 +535 True 101 1.8s [0.021 0.021 0.056]
         237 +536 True 257 5.3s [-0.014  0.001  0.082]
         238 +537 True 169 3.3s [0.012 0.006 0.003]
         239 +538 True 327 6.2s [-0.021  0.006 -0.088]
         240 +539 True 280 6.1s [-0.018  0.025  0.036]
         241 +540 True 368 7.2s [-0.02  -0.002 -0.032]
         242 +541 True 306 6.0s [-0.008 -0.018 -0.092]
         243 +542 True 190 3.6s [0.018 0.022 0.059]
         244 +543 True 140 2.3s [ 0.023 -0.016 -0.025]
         245 +544 True 213 4.6s [ 0.004  0.02  -0.095]
         246 +545 True 311 6.0s [-0.012  0.01  -0.002]
         247 +546 True 223 5.1s [-0.002 -0.021  0.002]
         248 +547 True 141 2.8s [0.013 0.021 0.049]
         249 +548 True 63 1.4s [-0.023  0.015  0.003]
         250 +549 True 135 3.0s [0.004 0.015 0.059]
         251 +550 True 169 4.1s [ 0.021 -0.002  0.078]
         252 +551 True 273 7.5s [0.014 0.02  0.001]
         253 +552 True 289 7.9s [ 0.001 -0.014  0.079]
         254 +553 True 180 4.6s [0.016 0.023 0.095]
         255 +554 True 116 2.5s [0.027 0.017 0.026]
         256 +555 True 208 4.5s [-0.009 -0.018  0.018]
         257 +556 True 190 4.9s [ 0.001 -0.016  0.097]
         258 +557 True 140 3.8s [-0.023  0.028  0.016]
         259 +558 True 203 5.0s [ 0.023 -0.008 -0.072]
         260 +559 True 142 3.9s [-0.026  0.029 -0.138]
         261 +560 True 280 5.8s [-0.007  0.014  0.02 ]
         262 +561 True 83 2.0s [-0.006 -0.026  0.127]
         263 +562 True 165 2.7s [-0.009 -0.005  0.077]
         264 +563 True 239 3.7s [-0.005 -0.021  0.072]
         265 +564 True 104 1.3s [ 0.003  0.02  -0.008]
         266 +565 True 167 2.4s [ 0.013  0.011 -0.02 ]
         267 +566 True 343 5.3s [-0.006  0.018  0.004]
         268 +567 True 225 3.7s [-0.005 -0.012  0.007]
         269 +568 True 84 1.2s [-0.018  0.006 -0.104]
         270 +569 True 175 2.7s [ 0.003 -0.02   0.076]
         271 +570 True 370 5.9s [-0.01  -0.017  0.065]
         272 +571 True 196 2.9s [ 0.001 -0.014 -0.124]
         273 +572 True 219 3.5s [ 0.03   0.002 -0.004]
         274 +573 True 269 4.7s [0.005 0.007 0.125]
         275 +574 True 155 2.9s [-0.014  0.01  -0.003]
         276 +575 True 158 2.5s [ 0.016 -0.016 -0.06 ]
         277 +576 True 104 1.6s [ 0.019 -0.004  0.03 ]
         278 +577 True 212 4.1s [-0.011  0.032  0.085]
         279 +578 True 144 2.8s [-0.023 -0.007 -0.061]
         280 +579 True 77 1.4s [ 0.025  0.022 -0.07 ]
         281 +580 True 167 2.9s [-0.009 -0.019 -0.002]
         282 +581 True 263 4.3s [ 0.021 -0.     0.028]
         283 +582 True 146 2.9s [ 0.022 -0.01   0.086]
         284 +583 True 150 2.8s [ 0.013  0.012 -0.008]
         285 +584 True 275 4.7s [-0.009 -0.022  0.002]
         286 +585 True 285 5.0s [-0.017 -0.001  0.026]
         287 +586 True 155 2.5s [-0.019 -0.017 -0.048]
         288 +587 True 341 5.4s [-0.019 -0.008 -0.005]
         289 +588 True 213 3.7s [ 0.005 -0.02   0.016]
         290 +589 True 263 4.5s [-0.03   0.006 -0.117]
         291 +590 True 299 4.5s [-0.009  0.001  0.078]
         292 +591 True 151 2.9s [-0.019  0.022 -0.014]
         293 +592 True 108 1.6s [ 0.007 -0.026 -0.085]
         294 +593 True 160 2.4s [ 0.014 -0.014  0.033]
         295 +594 True 129 2.0s [ 0.018  0.005 -0.   ]
         296 +595 True 75 1.1s [-0.023 -0.023 -0.025]
         297 +596 True 181 2.5s [ 0.021  0.015 -0.012]
         298 +597 True 274 2.6s [ 0.001  0.013 -0.001]
         299 +598 True 211 2.4s [ 0.015 -0.012 -0.007]
         300 +599 True 185 1.9s [-0.02  -0.023 -0.107]
         301 +success 300 / 300 mean steps 196.02333333333334
```

</details>

<a id="C006"></a>
### C006 · Diagonal-speed pushes, longer push horizon

Commit `49bdb1d479429e61c3c570a06acfe4c26bc3b521`; parents: 1dcac3607669f95bedf7710bea56e4be49df6ed0. Recorded author date: 2026-09-30T17:17:17+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0334](01_timeline.md#E0334): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_49bdb1d_approach.py) · [Exact all-file diff](evidence/diffs/C006_49bdb1d.diff)

[Previous saved controller snapshot](evidence/versions/C004_6bf1355_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d0ff213..85c350e 100644
--- a/approach.py
+++ b/approach.py
@@ -200,7 +200,7 @@ class GeneratedApproach:
  200    200          th = np.full(K, pose[2])
  201    201          valid = np.ones(K, bool)
  202    202          ds = 0.01
  203        -        nsteps = 100
         203 +        nsteps = 150
  204    204          best = (-np.inf, None)
  205    205          # travel cost to each candidate start
  206    206          standoff = 0.04
@@ -275,7 +275,7 @@ class GeneratedApproach:
  275    275  
  276    276          imp = E0 - results_E
  277    277          # rate = improvement / steps, with lower bound travel first
  278        -        push_steps = results_len / AMAX + 3
         278 +        push_steps = results_len * np.max(np.abs(uw), 1) / AMAX + 3
  279    279          order = np.argsort(-(imp / (lb + push_steps + 4)))
  280    280          best_i, best_rate, best_path = None, -np.inf, None
  281    281          for i in order[:60]:
@@ -314,9 +314,10 @@ class GeneratedApproach:
  314    314          done = 0.0
  315    315          while done < Ltot - 1e-6:
  316    316              rem = Ltot - done
  317        -            st = AMAX if rem > 0.15 else max(0.01, min(AMAX, rem / 3))
         317 +            mc = max(abs(u[0]), abs(u[1]))
         318 +            st = AMAX / mc if rem > 0.15 else max(0.01, min(AMAX, rem / 3))
  318    319              st = min(st, rem)
  319        -            acts.append(('push', u * st / max(abs(u[0]), abs(u[1]), 1e-9) * max(abs(u[0]), abs(u[1]))))
         320 +            acts.append(('push', u * st))
  320    321              done += st
  321    322          return acts
  322    323  
diff --git a/stats.py b/stats.py
new file mode 100644
index 0000000..6997914
--- /dev/null
+++ b/stats.py
@@ -0,0 +1,18 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from concurrent.futures import ThreadPoolExecutor
           5 +def run(seed):
           6 +    env=make_env(); ap=GeneratedApproach(None,None,{})
           7 +    obs,info=env.reset(seed=seed); ap.reset(obs,info)
           8 +    nav=push=npl=0
           9 +    for t in range(1000):
          10 +        if not ap.plan: npl+=1
          11 +        a=ap.get_action(obs)
          12 +        kind = ap._lastkind if hasattr(ap,'_lastkind') else None
          13 +        obs,r,te,tr,_=env.step(a)
          14 +        if te: break
          15 +    env.close()
          16 +    return seed,t+1,npl
          17 +with ThreadPoolExecutor(8) as ex: res=list(ex.map(run, range(int(sys.argv[1]),int(sys.argv[2]))))
          18 +print(np.mean([r[1] for r in res]), np.mean([r[2] for r in res]))
```

</details>

<a id="C007"></a>
### C007 · Hinge cost with success-region margins

Commit `ac791545304276d795aa311f589d544fc4fab223`; parents: 49bdb1d479429e61c3c570a06acfe4c26bc3b521. Recorded author date: 2026-09-30T17:17:50+02:00.

File roles (automatic): policy.

- [E0344](01_timeline.md#E0344): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_ac79154_approach.py) · [Exact all-file diff](evidence/diffs/C007_ac79154.diff)

[Previous saved controller snapshot](evidence/versions/C006_49bdb1d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 85c350e..7d6dcc9 100644
--- a/approach.py
+++ b/approach.py
@@ -71,6 +71,7 @@ class GeneratedApproach:
   71     71          self.g = Geom(s[12], s[13], s[14])
   72     72          self.plan = []
   73     73          self.last_pose = None
          74 +        self.margin = (0.012, 0.03, 0.07)
   74     75  
   75     76      # ---------------- helpers ----------------
   76     77      def err(self, ref, th, goal):
@@ -83,9 +84,12 @@ class GeneratedApproach:
   83     84          c, s = np.cos(th), np.sin(th)
   84     85          comx = ref[..., 0] - s * g.C[1]
   85     86          comy = ref[..., 1] + c * g.C[1]
   86        -        e_ref = np.hypot(ref[..., 0] - gref[0], ref[..., 1] - gref[1])
   87        -        e_com = np.hypot(comx - gcom[0], comy - gcom[1])
   88        -        return e_ref + e_com + 0.6 * np.abs(dth)
          87 +        m = self.margin
          88 +        e_ref = np.hypot(np.maximum(np.abs(ref[..., 0] - gref[0]) - m[0], 0),
          89 +                         np.maximum(np.abs(ref[..., 1] - gref[1]) - m[0], 0))
          90 +        e_com = np.hypot(np.maximum(np.abs(comx - gcom[0]) - m[1], 0),
          91 +                         np.maximum(np.abs(comy - gcom[1]) - m[1], 0))
          92 +        return e_ref + e_com + 0.6 * np.maximum(np.abs(dth) - m[2], 0)
   89     93  
   90     94      def seg_free(self, pose, a, b, clear):
   91     95          if a is self.start_pt:
```

</details>

<a id="C008"></a>
### C008 · Unwrapped angle success interval; tighten margins on stall

Commit `3c76c01dd2ed2b5c042a6eae9ab5d107785dc088`; parents: ac791545304276d795aa311f589d544fc4fab223. Recorded author date: 2026-09-30T17:19:25+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0366](01_timeline.md#E0366): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_3c76c01_approach.py) · [Exact all-file diff](evidence/diffs/C008_3c76c01.diff)

[Previous saved controller snapshot](evidence/versions/C007_ac79154_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7d6dcc9..91805d0 100644
--- a/approach.py
+++ b/approach.py
@@ -77,19 +77,24 @@ class GeneratedApproach:
   77     77      def err(self, ref, th, goal):
   78     78          g = self.g
   79     79          gref, gth = goal[0:2], goal[2]
          80 +        m = self.margin
   80     81          Rg = rot(gth)
   81     82          gcom = gref + Rg @ g.C
   82        -        dth = wrap(th - gth)
          83 +        # env checks |theta - theta_goal| WITHOUT wrapping; theta obs is in (-pi, pi]
          84 +        alo = max(gth - m[2], -np.pi + 0.015)
          85 +        ahi = min(gth + m[2], np.pi - 0.015)
          86 +        if alo > ahi:
          87 +            alo = ahi = gth
          88 +        dth = np.maximum(np.abs(wrap(th - 0.5 * (alo + ahi))) - 0.5 * (ahi - alo), 0)
   83     89          # com position
   84     90          c, s = np.cos(th), np.sin(th)
   85     91          comx = ref[..., 0] - s * g.C[1]
   86     92          comy = ref[..., 1] + c * g.C[1]
   87        -        m = self.margin
   88     93          e_ref = np.hypot(np.maximum(np.abs(ref[..., 0] - gref[0]) - m[0], 0),
   89     94                           np.maximum(np.abs(ref[..., 1] - gref[1]) - m[0], 0))
   90     95          e_com = np.hypot(np.maximum(np.abs(comx - gcom[0]) - m[1], 0),
   91     96                           np.maximum(np.abs(comy - gcom[1]) - m[1], 0))
   92        -        return e_ref + e_com + 0.6 * np.maximum(np.abs(dth) - m[2], 0)
          97 +        return e_ref + e_com + 0.6 * dth
   93     98  
   94     99      def seg_free(self, pose, a, b, clear):
   95    100          if a is self.start_pt:
@@ -329,6 +334,10 @@ class GeneratedApproach:
  329    334          s = np.asarray(state, dtype=float)
  330    335          if not self.plan:
  331    336              p = self.plan_push(s)
         337 +            if p is None and max(self.margin) > 0:
         338 +                # predicted success but env did not terminate: tighten margins
         339 +                self.margin = tuple(0.5 * x for x in self.margin) if max(self.margin) > 0.01 else (0.0, 0.0, 0.0)
         340 +                p = self.plan_push(s)
  332    341              if p is None:
  333    342                  # fallback: move away from the block, towards the arena centre
  334    343                  com = s[0:2] + rot(s[2]) @ self.g.C
diff --git a/stats.py b/stats.py
index 6997914..1fcb6b7 100644
--- a/stats.py
+++ b/stats.py
@@ -15,4 +15,5 @@ def run(seed):
   15     15      env.close()
   16     16      return seed,t+1,npl
   17     17  with ThreadPoolExecutor(8) as ex: res=list(ex.map(run, range(int(sys.argv[1]),int(sys.argv[2]))))
          18 +for r in res: print(*r)
   18     19  print(np.mean([r[1] for r in res]), np.mean([r[2] for r in res]))
```

</details>

<a id="C009"></a>
### C009 · Configurable scoring modes

Commit `8950f03ac1149dda396093068727253c070180af`; parents: 3c76c01dd2ed2b5c042a6eae9ab5d107785dc088. Recorded author date: 2026-09-30T17:22:19+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0407](01_timeline.md#E0407): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_8950f03_approach.py) · [Exact all-file diff](evidence/diffs/C009_8950f03.diff)

[Previous saved controller snapshot](evidence/versions/C008_3c76c01_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 91805d0..0d277ab 100644
--- a/approach.py
+++ b/approach.py
@@ -73,6 +73,8 @@ class GeneratedApproach:
   73     73          self.last_pose = None
   74     74          self.margin = (0.012, 0.03, 0.07)
   75     75  
          76 +    ANG_W = 0.6
          77 +
   76     78      # ---------------- helpers ----------------
   77     79      def err(self, ref, th, goal):
   78     80          g = self.g
@@ -94,7 +96,7 @@ class GeneratedApproach:
   94     96                           np.maximum(np.abs(ref[..., 1] - gref[1]) - m[0], 0))
   95     97          e_com = np.hypot(np.maximum(np.abs(comx - gcom[0]) - m[1], 0),
   96     98                           np.maximum(np.abs(comy - gcom[1]) - m[1], 0))
   97        -        return e_ref + e_com + 0.6 * dth
          99 +        return e_ref + e_com + self.ANG_W * dth
   98    100  
   99    101      def seg_free(self, pose, a, b, clear):
  100    102          if a is self.start_pt:
@@ -178,6 +180,15 @@ class GeneratedApproach:
  178    180          self.node_vis = {}
  179    181  
  180    182      # ---------------- planning ----------------
         183 +    MODE = 'rate'
         184 +    RC = 4.0
         185 +    V = 0.03
         186 +
         187 +    def score(self, E0, E, steps):
         188 +        if self.MODE in ('rate', 'rate_old'):
         189 +            return (E0 - E) / (steps + self.RC)
         190 +        return -(steps + E / self.V)
         191 +
  181    192      def plan_push(self, s):
  182    193          g = self.g
  183    194          pose = s[0:3].copy()
@@ -254,6 +265,8 @@ class GeneratedApproach:
  254    265          whi = np.maximum(4.97, cw.max(0) + 0.01)
  255    266          results_len = np.zeros(K)
  256    267          results_E = np.full(K, np.inf)
         268 +        results_S = np.full(K, -np.inf)
         269 +        mcu = np.max(np.abs(uw), 1)
  257    270          stepcnt = standoff / ds
  258    271          for k in range(1, nsteps + 1):
  259    272              c, sn = np.cos(th), np.sin(th)
@@ -278,25 +291,24 @@ class GeneratedApproach:
  278    291              if not valid.any():
  279    292                  break
  280    293              E = self.err(ref, th, goal)
  281        -            better = valid & (E < results_E - 1e-9)
         294 +            sc = -E if self.MODE == 'rate_old' else self.score(E0, E, lb + k * ds * mcu / AMAX + 3)
         295 +            better = valid & (E < E0 - 1e-4) & (sc > results_S)
         296 +            results_S = np.where(better, sc, results_S)
  282    297              results_E = np.where(better, E, results_E)
  283    298              results_len = np.where(better, k * ds, results_len)
  284    299  
  285        -        imp = E0 - results_E
  286        -        # rate = improvement / steps, with lower bound travel first
  287        -        push_steps = results_len * np.max(np.abs(uw), 1) / AMAX + 3
  288        -        order = np.argsort(-(imp / (lb + push_steps + 4)))
         300 +        push_steps = results_len * mcu / AMAX + 3
         301 +        order = np.argsort(-results_S)
  289    302          best_i, best_rate, best_path = None, -np.inf, None
  290    303          for i in order[:60]:
  291        -            if not np.isfinite(results_E[i]) or imp[i] <= 1e-4:
  292        -                continue
  293        -            ub_rate = imp[i] / (lb[i] + push_steps[i] + 4)
  294        -            if ub_rate <= best_rate:
         304 +            if not np.isfinite(results_S[i]):
         305 +                break
         306 +            if self.MODE != 'rate_old' and results_S[i] <= best_rate:
  295    307                  break
  296    308              path, cost = self.nav_path(pose, start, pre[i])
  297    309              if path is None:
  298    310                  continue
  299        -            rate = imp[i] / (cost + len(prefix) + push_steps[i] + 4)
         311 +            rate = self.score(E0, results_E[i], cost + len(prefix) + push_steps[i])
  300    312              if rate > best_rate:
  301    313                  best_rate, best_i, best_path = rate, i, path
  302    314          if best_i is None:
diff --git a/res_600_800.txt b/res_600_800.txt
new file mode 100644
index 0000000..2b9614d
--- /dev/null
+++ b/res_600_800.txt
@@ -0,0 +1,201 @@
           1 +600 True 219 2.9s [ 0.015 -0.012 -0.026]
           2 +601 True 147 2.4s [0.025 0.003 0.107]
           3 +602 True 134 1.5s [-0.008  0.012  0.103]
           4 +603 True 171 3.0s [ 0.005 -0.017  0.02 ]
           5 +604 True 151 2.9s [ 0.007 -0.021 -0.106]
           6 +605 True 148 3.0s [-0.009  0.01   0.116]
           7 +606 True 167 2.7s [ 0.014 -0.02  -0.071]
           8 +607 True 229 4.0s [ 0.019 -0.022  0.115]
           9 +608 True 291 4.9s [ 0.015 -0.005 -0.116]
          10 +609 True 271 4.2s [-0.006 -0.008 -0.099]
          11 +610 True 195 3.1s [0.015 0.007 0.11 ]
          12 +611 True 138 3.0s [-0.021  0.012 -0.03 ]
          13 +612 True 107 1.4s [-0.002  0.03   0.104]
          14 +613 True 107 1.5s [ 0.014 -0.003 -0.053]
          15 +614 True 194 3.5s [ 0.01  -0.014  0.092]
          16 +615 True 77 1.0s [-0.023 -0.019  0.013]
          17 +616 True 67 1.0s [ 0.015  0.027 -0.13 ]
          18 +617 True 243 4.7s [ 0.018 -0.013 -0.069]
          19 +618 True 212 4.0s [ 0.02  -0.004 -0.115]
          20 +619 True 174 3.0s [ 0.009 -0.025  0.021]
          21 +620 True 232 3.9s [ 0.013  0.005 -0.123]
          22 +621 True 152 2.8s [0.002 0.024 0.032]
          23 +622 True 195 2.4s [-0.012 -0.022 -0.1  ]
          24 +623 True 209 3.1s [ 0.003 -0.019  0.088]
          25 +624 True 134 1.5s [ 0.009  0.013 -0.126]
          26 +625 True 183 2.4s [-0.022  0.024 -0.086]
          27 +626 True 354 8.5s [ 0.02  -0.016  0.076]
          28 +627 True 144 2.5s [0.003 0.027 0.053]
          29 +628 True 182 3.2s [-0.011 -0.013  0.032]
          30 +629 True 257 4.2s [-0.022 -0.007  0.017]
          31 +630 True 243 4.3s [0.01  0.022 0.021]
          32 +631 True 205 3.7s [-0.024 -0.    -0.031]
          33 +632 True 235 5.7s [-0.016  0.022 -0.08 ]
          34 +633 True 175 4.3s [ 0.022 -0.006  0.017]
          35 +634 True 164 5.3s [-0.014  0.021 -0.058]
          36 +635 True 166 5.3s [ 0.003 -0.02   0.015]
          37 +636 True 128 3.1s [-0.008  0.02   0.089]
          38 +637 True 188 5.6s [-0.023  0.011 -0.115]
          39 +638 True 159 5.3s [-0.002  0.023 -0.02 ]
          40 +639 True 88 3.2s [ 0.01  -0.019  0.007]
          41 +640 True 237 7.1s [-0.009  0.027  0.106]
          42 +641 True 119 3.2s [-0.016  0.018  0.026]
          43 +642 True 209 5.5s [0.022 0.008 0.045]
          44 +643 True 221 6.2s [0.021 0.009 0.041]
          45 +644 True 183 5.4s [ 0.02  -0.012 -0.035]
          46 +645 True 204 5.9s [-0.001 -0.019  0.069]
          47 +646 True 254 5.2s [ 0.015  0.014 -0.075]
          48 +647 True 182 3.5s [ 0.008 -0.022  0.085]
          49 +648 True 156 2.4s [-0.01  -0.011 -0.105]
          50 +649 True 251 5.1s [ 0.028 -0.007 -0.068]
          51 +650 True 182 2.8s [-0.021  0.015  0.076]
          52 +651 True 359 6.6s [0.018 0.011 0.023]
          53 +652 True 226 4.9s [-0.008  0.01  -0.117]
          54 +653 True 250 5.0s [0.008 0.014 0.091]
          55 +654 True 160 2.1s [-0.012  0.022 -0.018]
          56 +655 True 209 4.0s [0.016 0.008 0.005]
          57 +656 True 199 3.8s [0.015 0.027 0.106]
          58 +657 True 214 3.6s [ 0.019  0.016 -0.059]
          59 +658 True 291 4.7s [-0.001  0.029  0.114]
          60 +659 True 217 3.8s [-0.005 -0.01   0.102]
          61 +660 True 219 4.6s [0.003 0.024 0.011]
          62 +661 True 181 3.1s [-0.02   0.014 -0.01 ]
          63 +662 True 273 5.8s [-0.002  0.017  0.055]
          64 +663 True 314 7.3s [-0.004 -0.018 -0.004]
          65 +664 True 209 4.8s [ 0.01   0.019 -0.08 ]
          66 +665 True 97 2.0s [0.012 0.024 0.109]
          67 +666 True 55 1.4s [-0.016 -0.006  0.06 ]
          68 +667 True 266 8.0s [-0.025 -0.018 -0.02 ]
          69 +668 True 259 6.0s [0.018 0.01  0.107]
          70 +669 True 121 3.4s [ 0.022 -0.011 -0.012]
          71 +670 True 214 5.4s [-0.015 -0.018 -0.028]
          72 +671 True 272 5.8s [-0.021 -0.001  0.027]
          73 +672 True 108 2.6s [-0.003 -0.031  0.114]
          74 +673 True 171 4.5s [ 0.009 -0.016 -0.069]
          75 +674 True 127 3.3s [0.022 0.004 0.118]
          76 +675 True 110 2.1s [-0.023  0.016 -0.099]
          77 +676 True 336 8.6s [ 0.003 -0.024 -0.047]
          78 +677 True 232 7.0s [ 0.01  -0.023  0.028]
          79 +678 True 198 6.5s [-0.012  0.02  -0.073]
          80 +679 True 102 2.4s [-0.011 -0.017  0.113]
          81 +680 True 212 4.9s [ 0.014 -0.02   0.009]
          82 +681 True 275 6.2s [-0.016  0.031  0.115]
          83 +682 True 181 4.6s [-0.011  0.014  0.099]
          84 +683 True 222 6.7s [-0.018 -0.014 -0.027]
          85 +684 True 124 3.2s [ 0.006  0.021 -0.107]
          86 +685 True 223 7.3s [ 0.018  0.023 -0.044]
          87 +686 True 170 5.9s [ 0.008 -0.018  0.06 ]
          88 +687 True 204 5.6s [ 0.01  -0.005  0.109]
          89 +688 True 190 6.2s [ 0.018  0.021 -0.032]
          90 +689 True 149 4.8s [-0.02  -0.025  0.002]
          91 +690 True 293 8.2s [ 0.013  0.02  -0.117]
          92 +691 True 245 7.5s [0.018 0.012 0.037]
          93 +692 True 269 7.3s [ 0.01  -0.017 -0.079]
          94 +693 True 205 5.5s [0.01  0.017 0.047]
          95 +694 True 215 5.5s [-0.012  0.021  0.089]
          96 +695 True 175 6.1s [-0.022  0.017 -0.066]
          97 +696 True 82 2.4s [0.024 0.021 0.001]
          98 +697 True 398 10.9s [ 0.017 -0.005  0.023]
          99 +698 True 120 3.9s [ 0.014 -0.019  0.04 ]
         100 +699 True 165 5.3s [-0.019  0.018 -0.039]
         101 +700 True 140 2.8s [-0.017  0.006 -0.129]
         102 +701 True 180 2.9s [ 0.008  0.005 -0.113]
         103 +702 True 157 3.8s [-0.012  0.011  0.007]
         104 +703 True 266 8.0s [-0.024 -0.023  0.   ]
         105 +704 True 79 2.4s [0.007 0.02  0.082]
         106 +705 True 141 4.5s [0.023 0.018 0.101]
         107 +706 True 112 3.2s [0.001 0.021 0.022]
         108 +707 True 251 6.5s [-0.013  0.009 -0.103]
         109 +708 True 113 2.5s [ 0.013 -0.02  -0.017]
         110 +709 True 228 4.6s [ 0.011 -0.003 -0.109]
         111 +710 True 96 2.4s [0.02  0.027 0.091]
         112 +711 True 134 1.6s [-0.003 -0.008 -0.1  ]
         113 +712 True 151 3.7s [0.021 0.011 0.043]
         114 +713 True 121 4.1s [-0.006  0.023 -0.011]
         115 +714 True 109 3.0s [ 0.01   0.007 -0.123]
         116 +715 True 186 4.0s [ 0.021  0.002 -0.069]
         117 +716 True 205 3.9s [-0.017  0.001  0.067]
         118 +717 True 275 4.8s [ 0.008 -0.018  0.076]
         119 +718 True 248 4.5s [0.014 0.013 0.093]
         120 +719 True 201 3.5s [ 0.016 -0.019 -0.019]
         121 +720 True 197 3.3s [-0.005  0.021  0.055]
         122 +721 True 222 4.4s [ 0.019 -0.012 -0.104]
         123 +722 True 141 2.2s [ 0.016 -0.007 -0.085]
         124 +723 True 133 2.7s [-0.015  0.019  0.075]
         125 +724 True 224 3.4s [-0.01  -0.013  0.067]
         126 +725 True 177 3.1s [-0.024  0.002 -0.048]
         127 +726 True 216 3.2s [-0.03   0.014 -0.102]
         128 +727 True 101 1.2s [ 0.009 -0.004 -0.122]
         129 +728 True 210 3.6s [-0.017 -0.025 -0.047]
         130 +729 True 200 3.3s [-0.025  0.006  0.012]
         131 +730 True 197 3.5s [-0.018 -0.007  0.016]
         132 +731 True 253 4.6s [ 0.015  0.015 -0.077]
         133 +732 True 180 4.1s [-0.017 -0.001 -0.082]
         134 +733 True 206 3.5s [ 0.007 -0.025 -0.098]
         135 +734 True 121 1.6s [ 0.022 -0.008  0.089]
         136 +735 True 118 1.9s [0.029 0.027 0.09 ]
         137 +736 True 209 2.9s [-0.007  0.031  0.121]
         138 +737 True 224 3.8s [-0.002  0.033  0.111]
         139 +738 True 224 3.7s [-0.007  0.012 -0.097]
         140 +739 True 187 3.4s [ 0.023  0.028 -0.046]
         141 +740 True 146 1.6s [-0.019 -0.02   0.059]
         142 +741 True 234 3.7s [-0.004  0.021  0.061]
         143 +742 True 154 2.7s [0.009 0.019 0.088]
         144 +743 True 80 1.3s [ 0.018  0.033 -0.105]
         145 +744 True 203 4.1s [ 0.01   0.004 -0.115]
         146 +745 True 101 2.1s [-0.021 -0.     0.057]
         147 +746 True 443 6.8s [ 0.014 -0.018 -0.058]
         148 +747 True 228 4.2s [0.016 0.025 0.081]
         149 +748 True 103 1.6s [-0.001  0.008 -0.108]
         150 +749 True 105 2.1s [-0.006  0.02  -0.026]
         151 +750 True 103 2.2s [-0.001  0.022 -0.049]
         152 +751 True 205 3.1s [-0.024 -0.015 -0.014]
         153 +752 True 263 4.5s [0.018 0.018 0.062]
         154 +753 True 189 3.0s [-0.011  0.022 -0.028]
         155 +754 True 191 3.0s [ 0.018 -0.004  0.05 ]
         156 +755 True 195 3.5s [-0.001  0.018  0.003]
         157 +756 True 114 2.2s [0.014 0.014 0.029]
         158 +757 True 209 4.1s [-0.018 -0.    -0.08 ]
         159 +758 True 28 0.9s [-0.01   0.018 -0.011]
         160 +759 True 273 5.0s [-0.006 -0.02   0.044]
         161 +760 True 203 5.0s [-0.021  0.011 -0.054]
         162 +761 True 204 3.1s [-0.028  0.029  0.099]
         163 +762 True 136 3.3s [-0.007 -0.015  0.059]
         164 +763 True 230 5.2s [ 0.02  -0.016 -0.073]
         165 +764 True 85 1.6s [ 0.017 -0.018 -0.056]
         166 +765 True 176 3.5s [-0.01  -0.019 -0.115]
         167 +766 True 135 2.8s [ 0.024 -0.019 -0.102]
         168 +767 True 133 2.7s [ 0.028 -0.017  0.118]
         169 +768 True 102 1.8s [-0.001 -0.01  -0.082]
         170 +769 True 150 2.5s [ 0.007 -0.024 -0.101]
         171 +770 True 100 2.1s [0.018 0.009 0.059]
         172 +771 True 185 3.7s [-0.021 -0.014 -0.004]
         173 +772 True 217 4.4s [-0.013 -0.016  0.071]
         174 +773 True 123 2.2s [ 0.021 -0.004  0.001]
         175 +774 True 290 5.4s [-0.021  0.009  0.104]
         176 +775 True 102 2.3s [0.019 0.014 0.13 ]
         177 +776 True 101 1.8s [-0.01  -0.022  0.014]
         178 +777 True 104 1.9s [-0.018  0.007  0.047]
         179 +778 True 101 2.3s [-0.021 -0.015  0.   ]
         180 +779 True 208 4.7s [-0.005  0.02  -0.014]
         181 +780 True 188 2.4s [-0.024 -0.003 -0.123]
         182 +781 True 232 4.0s [0.02  0.005 0.007]
         183 +782 True 226 3.1s [0.006 0.018 0.041]
         184 +783 True 161 2.2s [ 0.009  0.02  -0.044]
         185 +784 True 138 2.5s [-0.019 -0.006  0.081]
         186 +785 True 153 2.3s [0.003 0.009 0.131]
         187 +786 True 198 3.3s [-0.021  0.003 -0.001]
         188 +787 True 242 4.5s [-0.018  0.002 -0.098]
         189 +788 True 273 4.7s [-0.008  0.013 -0.137]
         190 +789 True 184 3.2s [-0.019  0.018  0.043]
         191 +790 True 180 2.6s [-0.004 -0.019  0.114]
         192 +791 True 167 3.4s [0.016 0.008 0.111]
         193 +792 True 248 3.1s [-0.016  0.022 -0.096]
         194 +793 True 220 2.7s [-0.015  0.022  0.072]
         195 +794 True 117 2.0s [-0.017 -0.012 -0.109]
         196 +795 True 166 2.6s [-0.012  0.019 -0.06 ]
         197 +796 True 140 1.8s [ 0.027 -0.026  0.008]
         198 +797 True 216 2.2s [-0.023  0.005  0.002]
         199 +798 True 121 1.6s [ 0.018 -0.004  0.013]
         200 +799 True 178 1.7s [ 0.02  -0.008  0.106]
         201 +success 200 / 200 mean steps 185.36
diff --git a/sweep.py b/sweep.py
new file mode 100644
index 0000000..68388fb
--- /dev/null
+++ b/sweep.py
@@ -0,0 +1,15 @@
           1 +import sys, json, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +from concurrent.futures import ThreadPoolExecutor
           5 +cfg=json.loads(sys.argv[1]); a,b=int(sys.argv[2]),int(sys.argv[3])
           6 +for k,v in cfg.items(): setattr(approach.GeneratedApproach,k,v)
           7 +def run(seed):
           8 +    env=make_env(); ap=approach.GeneratedApproach(None,None,{})
           9 +    obs,info=env.reset(seed=seed); ap.reset(obs,info)
          10 +    for t in range(1000):
          11 +        obs,r,te,tr,_=env.step(ap.get_action(obs))
          12 +        if te: break
          13 +    env.close(); return t+1, te
          14 +with ThreadPoolExecutor(6) as ex: res=list(ex.map(run, range(a,b)))
          15 +print(sys.argv[1], 'mean', np.mean([r[0] for r in res]), 'succ', sum(r[1] for r in res), '/', len(res))
```

</details>

<a id="C010"></a>
### C010 · Tuned angle weight 2.2; more config attrs

Commit `9cfce5290bd77f14b83bc9e2f583d4c7ff6f8a61`; parents: 8950f03ac1149dda396093068727253c070180af. Recorded author date: 2026-09-30T17:32:55+02:00.

File roles (automatic): policy.

- [E0436](01_timeline.md#E0436): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_9cfce52_approach.py) · [Exact all-file diff](evidence/diffs/C010_9cfce52.diff)

[Previous saved controller snapshot](evidence/versions/C009_8950f03_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0d277ab..9bb4685 100644
--- a/approach.py
+++ b/approach.py
@@ -73,7 +73,10 @@ class GeneratedApproach:
   73     73          self.last_pose = None
   74     74          self.margin = (0.012, 0.03, 0.07)
   75     75  
   76        -    ANG_W = 0.6
          76 +    ANG_W = 2.2
          77 +    ANGS = (-35, -18, 0, 18, 35)
          78 +    STANDOFF = 0.04
          79 +    FRIC = 0.85
   77     80  
   78     81      # ---------------- helpers ----------------
   79     82      def err(self, ref, th, goal):
@@ -196,7 +199,7 @@ class GeneratedApproach:
  196    199          robot = s[16:18].copy()
  197    200          E0 = float(self.err(pose[0:2], pose[2], goal))
  198    201  
  199        -        angs = np.deg2rad([-35, -18, 0, 18, 35])
         202 +        angs = np.deg2rad(list(self.ANGS))
  200    203          Q = np.repeat(g.cq, len(angs), 0)
  201    204          Nn = np.repeat(g.cn, len(angs), 0)
  202    205          A = np.tile(angs, len(g.cq))
@@ -223,7 +226,7 @@ class GeneratedApproach:
  223    226          nsteps = 150
  224    227          best = (-np.inf, None)
  225    228          # travel cost to each candidate start
  226        -        standoff = 0.04
         229 +        standoff = self.STANDOFF
  227    230          pre = pose[0:2] + pb_body @ R0.T - uw * standoff
  228    231          travel = np.full(K, np.inf)
  229    232          paths = [None] * K
@@ -276,7 +279,7 @@ class GeneratedApproach:
  276    279              f1 = (-a12 * db[:, 0] + a11 * db[:, 1]) / det
  277    280              fn = -(f0 * Nn[:, 0] + f1 * Nn[:, 1])
  278    281              ft = f0 * tb[:, 0] + f1 * tb[:, 1]
  279        -            valid &= (fn > 0) & (np.abs(ft) <= 0.85 * fn)
         282 +            valid &= (fn > 0) & (np.abs(ft) <= self.FRIC * fn)
  280    283              om = (r[:, 0] * f1 - r[:, 1] * f0) / c2
  281    284              com = com + np.stack([c * f0 - sn * f1, sn * f0 + c * f1], 1)
  282    285              th = th + om
```

</details>

<a id="C011"></a>
### C011 · Contact continuation candidates and optional mid-push replanning

Commit `42cff1653603cadc800009ea270bdcbde3c54716`; parents: 9cfce5290bd77f14b83bc9e2f583d4c7ff6f8a61. Recorded author date: 2026-09-30T17:37:49+02:00.

File roles (automatic): policy.

- [E0473](01_timeline.md#E0473): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_42cff16_approach.py) · [Exact all-file diff](evidence/diffs/C011_42cff16.diff)

[Previous saved controller snapshot](evidence/versions/C010_9cfce52_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9bb4685..779e341 100644
--- a/approach.py
+++ b/approach.py
@@ -50,6 +50,19 @@ class Geom:
   50     50          self.cq = np.array([c[0] for c in cands], dtype=float)
   51     51          self.cn = np.array([c[1] for c in cands], dtype=float)
   52     52  
          53 +    def closest(self, p):
          54 +        best = None
          55 +        for (x0, x1, y0, y1) in self.rects:
          56 +            q = np.array([min(max(p[0], x0), x1), min(max(p[1], y0), y1)])
          57 +            d = np.linalg.norm(p - q)
          58 +            if d < 1e-9:
          59 +                continue
          60 +            if best is None or d < best[0]:
          61 +                best = (d, q, (p - q) / d)
          62 +        if best is None:
          63 +            return None, None
          64 +        return best[1], best[2]
          65 +
   53     66      def dist_body(self, P):
   54     67          """min distance from body-frame points P (N,2) to T (0 inside)."""
   55     68          best = None
@@ -72,11 +85,15 @@ class GeneratedApproach:
   72     85          self.plan = []
   73     86          self.last_pose = None
   74     87          self.margin = (0.012, 0.03, 0.07)
          88 +        self.push_count = 0
   75     89  
   76     90      ANG_W = 2.2
   77     91      ANGS = (-35, -18, 0, 18, 35)
   78     92      STANDOFF = 0.04
   79     93      FRIC = 0.85
          94 +    NSTEPS = 150
          95 +    USE_CONTACT = True
          96 +    REPLAN_K = 0
   80     97  
   81     98      # ---------------- helpers ----------------
   82     99      def err(self, ref, th, goal):
@@ -200,11 +217,23 @@ class GeneratedApproach:
  200    217          E0 = float(self.err(pose[0:2], pose[2], goal))
  201    218  
  202    219          angs = np.deg2rad(list(self.ANGS))
  203        -        Q = np.repeat(g.cq, len(angs), 0)
  204        -        Nn = np.repeat(g.cn, len(angs), 0)
  205        -        A = np.tile(angs, len(g.cq))
  206        -        K = len(Q)
  207    220          R0 = rot(pose[2])
         221 +        cq, cn = g.cq, g.cn
         222 +        ncont = 0
         223 +        rb0 = (robot - pose[0:2]) @ R0
         224 +        if self.USE_CONTACT and g.dist_body(rb0[None])[0] < RAD + 0.012:
         225 +            q, n = g.closest(rb0)
         226 +            if q is not None:
         227 +                cq = np.vstack([cq, q[None]])
         228 +                cn = np.vstack([cn, n[None]])
         229 +                ncont = 1
         230 +        Q = np.repeat(cq, len(angs), 0)
         231 +        Nn = np.repeat(cn, len(angs), 0)
         232 +        A = np.tile(angs, len(cq))
         233 +        K = len(Q)
         234 +        is_cont = np.zeros(K, bool)
         235 +        if ncont:
         236 +            is_cont[-len(angs):] = True
  208    237          # push direction in body frame (inward normal rotated), then world
  209    238          inn = -Nn
  210    239          ca, sa = np.cos(A), np.sin(A)
@@ -223,11 +252,13 @@ class GeneratedApproach:
  223    252          th = np.full(K, pose[2])
  224    253          valid = np.ones(K, bool)
  225    254          ds = 0.01
  226        -        nsteps = 150
         255 +        nsteps = self.NSTEPS
  227    256          best = (-np.inf, None)
  228    257          # travel cost to each candidate start
  229    258          standoff = self.STANDOFF
  230        -        pre = pose[0:2] + pb_body @ R0.T - uw * standoff
         259 +        so = np.where(is_cont, 0.0, standoff)
         260 +        pre = pose[0:2] + pb_body @ R0.T - uw * so[:, None]
         261 +        pre[is_cont] = robot
  231    262          travel = np.full(K, np.inf)
  232    263          paths = [None] * K
  233    264          self.build_nodes(pose)
@@ -259,9 +290,10 @@ class GeneratedApproach:
  259    290          pre_body = (pre - pose[0:2]) @ R0
  260    291          pre_ok = g.dist_body(pre_body) > RAD + 0.015
  261    292          pre_ok &= np.all((pre >= LO + 0.005) & (pre <= HI - 0.005), 1)
  262        -        valid &= pre_ok
         293 +        valid &= pre_ok | is_cont
  263    294          # lower bound travel (straight line) for pruning
  264    295          lb = np.max(np.abs(pre - start), 1) / AMAX + len(prefix)
         296 +        lb[is_cont] = 0.0
  265    297  
  266    298          cw = pose[0:2] + g.corners @ R0.T
  267    299          wlo = np.minimum(0.03, cw.min(0) - 0.01)
@@ -289,7 +321,7 @@ class GeneratedApproach:
  289    321              cx = ref[:, 0][:, None] + c[:, None] * g.corners[None, :, 0] - sn[:, None] * g.corners[None, :, 1]
  290    322              cy = ref[:, 1][:, None] + sn[:, None] * g.corners[None, :, 0] + c[:, None] * g.corners[None, :, 1]
  291    323              valid &= (cx.min(1) > wlo[0]) & (cx.max(1) < whi[0]) & (cy.min(1) > wlo[1]) & (cy.max(1) < whi[1])
  292        -            pw = pre + uw * (standoff + k * ds)
         324 +            pw = pre + uw * (so[:, None] + k * ds)
  293    325              valid &= np.all((pw >= LO + 0.005) & (pw <= HI - 0.005), 1)
  294    326              if not valid.any():
  295    327                  break
@@ -308,7 +340,10 @@ class GeneratedApproach:
  308    340                  break
  309    341              if self.MODE != 'rate_old' and results_S[i] <= best_rate:
  310    342                  break
  311        -            path, cost = self.nav_path(pose, start, pre[i])
         343 +            if is_cont[i]:
         344 +                path, cost = [], -len(prefix)
         345 +            else:
         346 +                path, cost = self.nav_path(pose, start, pre[i])
  312    347              if path is None:
  313    348                  continue
  314    349              rate = self.score(E0, results_E[i], cost + len(prefix) + push_steps[i])
@@ -317,7 +352,7 @@ class GeneratedApproach:
  317    352          if best_i is None:
  318    353              return None
  319    354          i = best_i
  320        -        return dict(path=prefix + best_path, u=uw[i], L=results_len[i] + standoff,
         355 +        return dict(path=(prefix + best_path) if not is_cont[i] else [], u=uw[i], L=results_len[i] + so[i],
  321    356                      Epred=results_E[i], E0=E0)
  322    357  
  323    358      # ---------------- execution ----------------
@@ -347,7 +382,11 @@ class GeneratedApproach:
  347    382  
  348    383      def get_action(self, state):
  349    384          s = np.asarray(state, dtype=float)
         385 +        if (self.plan and self.REPLAN_K > 0 and self.plan[0][0] == 'push'
         386 +                and self.push_count >= self.REPLAN_K and len(self.plan) > 2):
         387 +            self.plan = []
  350    388          if not self.plan:
         389 +            self.push_count = 0
  351    390              p = self.plan_push(s)
  352    391              if p is None and max(self.margin) > 0:
  353    392                  # predicted success but env did not terminate: tighten margins
@@ -363,7 +402,9 @@ class GeneratedApproach:
  363    402                  _, a = self.plan.pop(0)
  364    403                  return self._safe(s, a)
  365    404              self.plan = self.build_actions(s[16:18], p)
  366        -        _, a = self.plan.pop(0)
         405 +        kind, a = self.plan.pop(0)
         406 +        if kind == 'push':
         407 +            self.push_count += 1
  367    408          return self._safe(s, a)
  368    409  
  369    410      def _safe(self, s, a):
```

</details>

<a id="C012"></a>
### C012 · REPLAN_K=10

Commit `b644810ea5d0889315f056fa49b0948dd13e6216`; parents: 42cff1653603cadc800009ea270bdcbde3c54716. Recorded author date: 2026-09-30T17:40:08+02:00.

File roles (automatic): policy.

- [E0476](01_timeline.md#E0476): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_b644810_approach.py) · [Exact all-file diff](evidence/diffs/C012_b644810.diff)

[Previous saved controller snapshot](evidence/versions/C011_42cff16_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 779e341..0671973 100644
--- a/approach.py
+++ b/approach.py
@@ -93,7 +93,7 @@ class GeneratedApproach:
   93     93      FRIC = 0.85
   94     94      NSTEPS = 150
   95     95      USE_CONTACT = True
   96        -    REPLAN_K = 0
          96 +    REPLAN_K = 10
   97     97  
   98     98      # ---------------- helpers ----------------
   99     99      def err(self, ref, th, goal):
```

</details>

<a id="C013"></a>
### C013 · 2-step lookahead (LOOK=8)

Commit `f5b0c5696ea29ad06067deeeb66db607394daf62`; parents: b644810ea5d0889315f056fa49b0948dd13e6216. Recorded author date: 2026-09-30T17:48:52+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0528](01_timeline.md#E0528): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_f5b0c56_approach.py) · [Exact all-file diff](evidence/diffs/C013_f5b0c56.diff)

[Previous saved controller snapshot](evidence/versions/C012_b644810_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0671973..7fcf888 100644
--- a/approach.py
+++ b/approach.py
@@ -94,6 +94,7 @@ class GeneratedApproach:
   94     94      NSTEPS = 150
   95     95      USE_CONTACT = True
   96     96      REPLAN_K = 10
          97 +    LOOK = 8
   97     98  
   98     99      # ---------------- helpers ----------------
   99    100      def err(self, ref, th, goal):
@@ -209,7 +210,7 @@ class GeneratedApproach:
  209    210              return (E0 - E) / (steps + self.RC)
  210    211          return -(steps + E / self.V)
  211    212  
  212        -    def plan_push(self, s):
         213 +    def plan_push(self, s, lookahead=0):
  213    214          g = self.g
  214    215          pose = s[0:3].copy()
  215    216          goal = s[29:32]
@@ -301,6 +302,8 @@ class GeneratedApproach:
  301    302          results_len = np.zeros(K)
  302    303          results_E = np.full(K, np.inf)
  303    304          results_S = np.full(K, -np.inf)
         305 +        results_ref = np.zeros((K, 2))
         306 +        results_th = np.zeros(K)
  304    307          mcu = np.max(np.abs(uw), 1)
  305    308          stepcnt = standoff / ds
  306    309          for k in range(1, nsteps + 1):
@@ -331,14 +334,17 @@ class GeneratedApproach:
  331    334              results_S = np.where(better, sc, results_S)
  332    335              results_E = np.where(better, E, results_E)
  333    336              results_len = np.where(better, k * ds, results_len)
         337 +            results_ref = np.where(better[:, None], ref, results_ref)
         338 +            results_th = np.where(better, th, results_th)
  334    339  
  335    340          push_steps = results_len * mcu / AMAX + 3
  336    341          order = np.argsort(-results_S)
  337        -        best_i, best_rate, best_path = None, -np.inf, None
         342 +        feas = []
         343 +        best_rate = -np.inf
  338    344          for i in order[:60]:
  339    345              if not np.isfinite(results_S[i]):
  340    346                  break
  341        -            if self.MODE != 'rate_old' and results_S[i] <= best_rate:
         347 +            if not lookahead and self.MODE != 'rate_old' and results_S[i] <= best_rate:
  342    348                  break
  343    349              if is_cont[i]:
  344    350                  path, cost = [], -len(prefix)
@@ -346,14 +352,33 @@ class GeneratedApproach:
  346    352                  path, cost = self.nav_path(pose, start, pre[i])
  347    353              if path is None:
  348    354                  continue
  349        -            rate = self.score(E0, results_E[i], cost + len(prefix) + push_steps[i])
  350        -            if rate > best_rate:
  351        -                best_rate, best_i, best_path = rate, i, path
  352        -        if best_i is None:
         355 +            steps = cost + len(prefix) + push_steps[i]
         356 +            rate = self.score(E0, results_E[i], steps)
         357 +            feas.append((rate, i, path, steps))
         358 +            best_rate = max(best_rate, rate)
         359 +            if lookahead and len(feas) >= 3 * lookahead:
         360 +                break
         361 +        if not feas:
  353    362              return None
  354        -        i = best_i
  355        -        return dict(path=(prefix + best_path) if not is_cont[i] else [], u=uw[i], L=results_len[i] + so[i],
  356        -                    Epred=results_E[i], E0=E0)
         363 +        feas.sort(key=lambda x: -x[0])
         364 +        best = feas[0]
         365 +        if lookahead and results_E[best[1]] > 0:
         366 +            best_c = -np.inf
         367 +            for (rate, i, path, steps) in feas[:lookahead]:
         368 +                s2 = s.copy()
         369 +                s2[0:2] = results_ref[i]
         370 +                s2[2] = wrap(results_th[i])
         371 +                s2[16:18] = pre[i] + uw[i] * (so[i] + results_len[i])
         372 +                p2 = self.plan_push(s2, 0)
         373 +                if p2 is None or results_E[i] <= 0:
         374 +                    c = self.score(E0, results_E[i], steps)
         375 +                else:
         376 +                    c = self.score(E0, p2['Epred'], steps + p2['steps'])
         377 +                if c > best_c:
         378 +                    best_c, best = c, (rate, i, path, steps)
         379 +        rate, i, path, steps = best
         380 +        return dict(path=(prefix + path) if not is_cont[i] else [], u=uw[i], L=results_len[i] + so[i],
         381 +                    Epred=results_E[i], E0=E0, steps=steps)
  357    382  
  358    383      # ---------------- execution ----------------
  359    384      def build_actions(self, robot, plan):
@@ -387,11 +412,11 @@ class GeneratedApproach:
  387    412              self.plan = []
  388    413          if not self.plan:
  389    414              self.push_count = 0
  390        -            p = self.plan_push(s)
         415 +            p = self.plan_push(s, self.LOOK)
  391    416              if p is None and max(self.margin) > 0:
  392    417                  # predicted success but env did not terminate: tighten margins
  393    418                  self.margin = tuple(0.5 * x for x in self.margin) if max(self.margin) > 0.01 else (0.0, 0.0, 0.0)
  394        -                p = self.plan_push(s)
         419 +                p = self.plan_push(s, self.LOOK)
  395    420              if p is None:
  396    421                  # fallback: move away from the block, towards the arena centre
  397    422                  com = s[0:2] + rot(s[2]) @ self.g.C
diff --git a/timeit_plan.py b/timeit_plan.py
new file mode 100644
index 0000000..b0275e6
--- /dev/null
+++ b/timeit_plan.py
@@ -0,0 +1,7 @@
           1 +import time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env=make_env(); ap=GeneratedApproach(None,None,{})
           5 +for seed in range(5):
           6 +    obs,info=env.reset(seed=seed); ap.reset(obs,info)
           7 +    t0=time.time(); ap.plan_push(obs); print(time.time()-t0)
```

</details>

<a id="C014"></a>
### C014 · Time budget guard and exception safety

Commit `b1a7b714c3cc9e000e66438b0a499fe3eea2beb6`; parents: f5b0c5696ea29ad06067deeeb66db607394daf62. Recorded author date: 2026-09-30T18:03:53+02:00.

File roles (automatic): policy.

- [E0558](01_timeline.md#E0558): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_b1a7b71_approach.py) · [Exact all-file diff](evidence/diffs/C014_b1a7b71.diff)

[Previous saved controller snapshot](evidence/versions/C013_f5b0c56_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7fcf888..79896a0 100644
--- a/approach.py
+++ b/approach.py
@@ -5,6 +5,7 @@ about the centre of mass with c^2 = I/m of a uniform T.
    5      5  Body frame: origin = obs[0:2]; bar x in [-L/2,L/2], y in [-w,0]; stem x in [-w/2,w/2], y in [-w-Lv,-w].
    6      6  """
    7      7  import heapq
           8 +import time
    8      9  import numpy as np
    9     10  
   10     11  RAD = 0.1
@@ -86,6 +87,7 @@ class GeneratedApproach:
   86     87          self.last_pose = None
   87     88          self.margin = (0.012, 0.03, 0.07)
   88     89          self.push_count = 0
          90 +        self.t_used = 0.0
   89     91  
   90     92      ANG_W = 2.2
   91     93      ANGS = (-35, -18, 0, 18, 35)
@@ -407,16 +409,23 @@ class GeneratedApproach:
  407    409  
  408    410      def get_action(self, state):
  409    411          s = np.asarray(state, dtype=float)
  410        -        if (self.plan and self.REPLAN_K > 0 and self.plan[0][0] == 'push'
         412 +        if (self.plan and self.REPLAN_K > 0 and self.t_used < 40.0 and self.plan[0][0] == 'push'
  411    413                  and self.push_count >= self.REPLAN_K and len(self.plan) > 2):
  412    414              self.plan = []
  413    415          if not self.plan:
  414    416              self.push_count = 0
  415        -            p = self.plan_push(s, self.LOOK)
  416        -            if p is None and max(self.margin) > 0:
  417        -                # predicted success but env did not terminate: tighten margins
  418        -                self.margin = tuple(0.5 * x for x in self.margin) if max(self.margin) > 0.01 else (0.0, 0.0, 0.0)
  419        -                p = self.plan_push(s, self.LOOK)
         417 +        self.t_used = 0.0
         418 +            t0 = time.time()
         419 +            look = self.LOOK if self.t_used < 25.0 else 0
         420 +            try:
         421 +                p = self.plan_push(s, look)
         422 +                if p is None and max(self.margin) > 0:
         423 +                    # predicted success but env did not terminate: tighten margins
         424 +                    self.margin = tuple(0.5 * x for x in self.margin) if max(self.margin) > 0.01 else (0.0, 0.0, 0.0)
         425 +                    p = self.plan_push(s, look)
         426 +            except Exception:
         427 +                p = None
         428 +            self.t_used += time.time() - t0
  420    429              if p is None:
  421    430                  # fallback: move away from the block, towards the arena centre
  422    431                  com = s[0:2] + rot(s[2]) @ self.g.C
```

</details>

<a id="C015"></a>
### C015 · fix indentation

Commit `159e97d0e232a1540838b9cfd81902a7f4235ba9`; parents: b1a7b714c3cc9e000e66438b0a499fe3eea2beb6. Recorded author date: 2026-09-30T18:03:59+02:00.

File roles (automatic): policy, setup/other.

- [E0586](01_timeline.md#E0586): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_159e97d_approach.py) · [Exact all-file diff](evidence/diffs/C015_159e97d.diff)

[Previous saved controller snapshot](evidence/versions/C014_b1a7b71_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 79896a0..40f3211 100644
--- a/approach.py
+++ b/approach.py
@@ -86,6 +86,7 @@ class GeneratedApproach:
   86     86          self.plan = []
   87     87          self.last_pose = None
   88     88          self.margin = (0.012, 0.03, 0.07)
          89 +        self.t_used = 0.0
   89     90          self.push_count = 0
   90     91          self.t_used = 0.0
   91     92  
@@ -414,7 +415,6 @@ class GeneratedApproach:
  414    415              self.plan = []
  415    416          if not self.plan:
  416    417              self.push_count = 0
  417        -        self.t_used = 0.0
  418    418              t0 = time.time()
  419    419              look = self.LOOK if self.t_used < 25.0 else 0
  420    420              try:
diff --git a/res_1000.txt b/res_1000.txt
new file mode 100644
index 0000000..1ce7722
--- /dev/null
+++ b/res_1000.txt
@@ -0,0 +1,6 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/test_approach.py", line 3, in <module>
           3 +    from approach import GeneratedApproach
           4 +  File "/sandbox/approach.py", line 418
           5 +    t0 = time.time()
           6 +IndentationError: unexpected indent
```

</details>

<a id="C016"></a>
### C016 · results 1000-1300: 300/300

Commit `b52486c74a756f308ecc27a8d0f14350395baa54`; parents: 159e97d0e232a1540838b9cfd81902a7f4235ba9. Recorded author date: 2026-09-30T18:26:27+02:00.

File roles (automatic): setup/other.

- [E0644](01_timeline.md#E0644): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C016_b52486c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res_1000.txt b/res_1000.txt
index 1ce7722..eff47e5 100644
--- a/res_1000.txt
+++ b/res_1000.txt
@@ -1,6 +1,301 @@
    1        -Traceback (most recent call last):
    2        -  File "/sandbox/test_approach.py", line 3, in <module>
    3        -    from approach import GeneratedApproach
    4        -  File "/sandbox/approach.py", line 418
    5        -    t0 = time.time()
    6        -IndentationError: unexpected indent
           1 +1000 True 83 24.0s [-0.015 -0.008 -0.004]
           2 +1001 True 180 30.1s [ 0.014 -0.025  0.067]
           3 +1002 True 122 29.8s [ 0.017 -0.018  0.05 ]
           4 +1003 True 194 29.6s [-0.021 -0.015 -0.034]
           5 +1004 True 162 29.6s [ 0.023  0.017 -0.03 ]
           6 +1005 True 164 24.7s [0.02  0.008 0.052]
           7 +1006 True 175 30.2s [-0.005  0.016  0.068]
           8 +1007 True 127 28.6s [0.009 0.022 0.059]
           9 +1008 True 78 10.3s [0.007 0.018 0.055]
          10 +1009 True 143 29.3s [ 0.014 -0.021  0.068]
          11 +1010 True 135 28.1s [ 0.022 -0.012  0.041]
          12 +1011 True 80 19.0s [-0.007  0.022  0.066]
          13 +1012 True 210 29.6s [-0.01  -0.022 -0.063]
          14 +1013 True 156 29.0s [0.022 0.02  0.064]
          15 +1014 True 129 24.0s [0.01  0.015 0.011]
          16 +1015 True 97 19.2s [-0.011 -0.019 -0.057]
          17 +1016 True 137 28.9s [ 0.009 -0.018  0.076]
          18 +1017 True 121 27.6s [0.012 0.016 0.048]
          19 +1018 True 124 27.5s [ 0.016 -0.004  0.016]
          20 +1019 True 167 29.1s [ 0.017 -0.011 -0.001]
          21 +1020 True 213 29.0s [ 0.002 -0.02   0.003]
          22 +1021 True 98 27.1s [ 0.017 -0.02   0.015]
          23 +1022 True 101 18.5s [0.014 0.015 0.021]
          24 +1023 True 113 23.2s [0.011 0.02  0.06 ]
          25 +1024 True 131 27.9s [-0.001  0.017 -0.074]
          26 +1025 True 172 30.4s [-0.003  0.012 -0.051]
          27 +1026 True 173 30.1s [-0.021 -0.016 -0.03 ]
          28 +1027 True 192 31.1s [-0.015  0.009 -0.078]
          29 +1028 True 150 31.9s [-0.027  0.02   0.073]
          30 +1029 True 118 32.8s [-0.019 -0.019 -0.133]
          31 +1030 True 140 26.3s [-0.02   0.016 -0.074]
          32 +1031 True 107 25.4s [ 0.01   0.023 -0.026]
          33 +1032 True 82 15.0s [ 0.008  0.018 -0.005]
          34 +1033 True 137 28.4s [0.012 0.016 0.075]
          35 +1034 True 104 22.7s [0.017 0.011 0.071]
          36 +1035 True 142 28.6s [-0.     0.022 -0.1  ]
          37 +1036 True 192 29.6s [-0.017 -0.016 -0.037]
          38 +1037 True 93 21.2s [0.01  0.011 0.059]
          39 +1038 True 115 28.0s [-0.019  0.011 -0.019]
          40 +1039 True 162 27.0s [-0.01   0.02   0.063]
          41 +1040 True 155 28.7s [-0.006  0.018 -0.067]
          42 +1041 True 141 30.5s [0.007 0.021 0.035]
          43 +1042 True 187 32.6s [-0.008  0.013 -0.066]
          44 +1043 True 130 32.2s [ 0.01   0.019 -0.036]
          45 +1044 True 162 33.7s [0.019 0.022 0.004]
          46 +1045 True 128 31.7s [-0.002  0.02  -0.054]
          47 +1046 True 76 31.1s [ 0.018 -0.019 -0.082]
          48 +1047 True 160 34.0s [-0.005  0.015  0.083]
          49 +1048 True 127 26.4s [0.016 0.002 0.062]
          50 +1049 True 162 31.3s [ 0.005 -0.024 -0.004]
          51 +1050 True 88 32.0s [ 0.019 -0.019 -0.07 ]
          52 +1051 True 152 32.3s [ 0.015  0.019 -0.063]
          53 +1052 True 147 31.9s [-0.017  0.012 -0.058]
          54 +1053 True 114 29.7s [0.01  0.022 0.094]
          55 +1054 True 112 23.7s [ 0.014  0.023 -0.048]
          56 +1055 True 118 30.5s [ 0.016 -0.015  0.008]
          57 +1056 True 128 29.0s [ 0.022 -0.028  0.078]
          58 +1057 True 91 26.8s [-0.001 -0.022 -0.028]
          59 +1058 True 109 26.1s [ 0.024  0.011 -0.1  ]
          60 +1059 True 156 27.0s [-0.011 -0.012 -0.086]
          61 +1060 True 95 29.5s [-0.015  0.004 -0.051]
          62 +1061 True 78 20.2s [-0.019 -0.004  0.026]
          63 +1062 True 115 20.3s [ 0.013 -0.021 -0.057]
          64 +1063 True 142 30.3s [0.022 0.016 0.073]
          65 +1064 True 72 14.7s [ 0.005 -0.023 -0.018]
          66 +1065 True 133 28.3s [-0.017  0.016 -0.092]
          67 +1066 True 110 24.3s [ 0.015  0.016 -0.004]
          68 +1067 True 154 28.6s [-0.019 -0.015 -0.013]
          69 +1068 True 58 23.5s [-0.02  -0.008 -0.081]
          70 +1069 True 75 19.0s [-0.018  0.004 -0.137]
          71 +1070 True 128 28.6s [-0.023 -0.02   0.067]
          72 +1071 True 116 19.2s [ 0.022 -0.005 -0.055]
          73 +1072 True 74 28.0s [-0.013 -0.023 -0.029]
          74 +1073 True 123 29.0s [ 0.021 -0.017  0.103]
          75 +1074 True 135 27.9s [0.02  0.022 0.013]
          76 +1075 True 156 29.0s [0.029 0.014 0.077]
          77 +1076 True 150 28.5s [ 0.022  0.004 -0.048]
          78 +1077 True 234 30.5s [-0.014 -0.017 -0.085]
          79 +1078 True 129 24.1s [-0.02   0.015 -0.032]
          80 +1079 True 60 19.1s [-0.014 -0.    -0.011]
          81 +1080 True 139 29.9s [-0.005 -0.007 -0.114]
          82 +1081 True 75 26.1s [ 0.022 -0.002  0.059]
          83 +1082 True 89 25.4s [ 0.007 -0.018 -0.084]
          84 +1083 True 188 28.5s [ 0.012 -0.015 -0.065]
          85 +1084 True 135 27.0s [ 0.02   0.016 -0.035]
          86 +1085 True 42 10.1s [ 0.011 -0.018 -0.039]
          87 +1086 True 193 29.1s [-0.015  0.027  0.07 ]
          88 +1087 True 143 28.1s [-0.019  0.007  0.055]
          89 +1088 True 119 26.9s [0.003 0.023 0.043]
          90 +1089 True 169 30.5s [-0.023 -0.012  0.028]
          91 +1090 True 91 25.1s [-0.019 -0.017 -0.036]
          92 +1091 True 195 31.2s [-0.019 -0.022 -0.008]
          93 +1092 True 98 15.2s [-0.025 -0.019 -0.049]
          94 +1093 True 114 19.4s [-0.017  0.001 -0.041]
          95 +1094 True 96 18.8s [ 0.007  0.023 -0.032]
          96 +1095 True 167 30.5s [-0.025 -0.    -0.112]
          97 +1096 True 129 29.6s [ 0.016  0.02  -0.043]
          98 +1097 True 189 29.7s [0.016 0.027 0.036]
          99 +1098 True 85 14.2s [0.018 0.018 0.   ]
         100 +1099 True 213 29.8s [-0.005  0.022  0.064]
         101 +1100 True 133 29.3s [ 0.024 -0.007  0.038]
         102 +1101 True 121 23.5s [ 0.019  0.021 -0.075]
         103 +1102 True 113 28.8s [-0.026  0.017 -0.072]
         104 +1103 True 120 29.8s [ 0.02  -0.001  0.071]
         105 +1104 True 98 31.2s [-0.015 -0.012 -0.038]
         106 +1105 True 109 31.8s [ 0.025  0.012 -0.004]
         107 +1106 True 154 29.4s [-0.021 -0.018  0.071]
         108 +1107 True 133 28.7s [ 0.023 -0.027  0.067]
         109 +1108 True 188 29.5s [ 0.014 -0.005  0.063]
         110 +1109 True 100 11.7s [-0.006  0.018 -0.024]
         111 +1110 True 176 29.6s [-0.019  0.014 -0.016]
         112 +1111 True 116 27.0s [ 0.02   0.018 -0.004]
         113 +1112 True 120 29.5s [ 0.028 -0.016 -0.006]
         114 +1113 True 110 30.2s [0.011 0.027 0.076]
         115 +1114 True 117 21.7s [0.021 0.004 0.071]
         116 +1115 True 144 29.2s [ 0.016 -0.004  0.05 ]
         117 +1116 True 203 29.4s [ 0.    -0.019 -0.071]
         118 +1117 True 90 21.7s [ 0.023 -0.01  -0.066]
         119 +1118 True 137 32.0s [ 0.021 -0.016 -0.059]
         120 +1119 True 116 30.4s [ 0.016 -0.007 -0.052]
         121 +1120 True 199 31.9s [ 0.008 -0.021  0.014]
         122 +1121 True 159 32.5s [ 0.005 -0.019  0.059]
         123 +1122 True 144 30.5s [-0.017  0.022  0.088]
         124 +1123 True 81 29.1s [ 0.023 -0.015 -0.048]
         125 +1124 True 115 30.0s [ 0.021 -0.013 -0.048]
         126 +1125 True 193 30.8s [-0.017  0.001  0.07 ]
         127 +1126 True 110 25.4s [-0.015 -0.013  0.017]
         128 +1127 True 81 16.1s [ 0.015 -0.004 -0.066]
         129 +1128 True 157 31.0s [-0.029 -0.016  0.009]
         130 +1129 True 190 30.3s [0.021 0.021 0.043]
         131 +1130 True 148 29.9s [ 0.011 -0.016  0.028]
         132 +1131 True 139 29.1s [-0.015  0.014  0.036]
         133 +1132 True 125 24.0s [ 0.019 -0.017 -0.071]
         134 +1133 True 206 30.8s [-0.003 -0.023 -0.004]
         135 +1134 True 179 30.4s [-0.02   0.016  0.001]
         136 +1135 True 145 24.0s [ 0.018 -0.019  0.007]
         137 +1136 True 155 27.9s [ 0.012 -0.006  0.074]
         138 +1137 True 135 28.1s [ 0.019 -0.002  0.076]
         139 +1138 True 117 28.5s [-0.022 -0.021  0.033]
         140 +1139 True 108 23.5s [-0.015  0.02  -0.029]
         141 +1140 True 134 28.9s [ 0.014 -0.014 -0.057]
         142 +1141 True 120 28.9s [ 0.011 -0.02   0.023]
         143 +1142 True 170 29.4s [ 0.023  0.024 -0.008]
         144 +1143 True 131 23.1s [ 0.021 -0.033 -0.066]
         145 +1144 True 145 30.3s [-0.015 -0.003 -0.048]
         146 +1145 True 184 31.3s [ 0.013 -0.014  0.092]
         147 +1146 True 166 31.8s [-0.009 -0.021  0.043]
         148 +1147 True 85 30.2s [-0.02   0.007  0.058]
         149 +1148 True 193 28.3s [-0.02  -0.026  0.037]
         150 +1149 True 162 27.0s [ 0.014  0.01  -0.127]
         151 +1150 True 102 26.9s [ 0.006  0.016 -0.081]
         152 +1151 True 250 30.9s [-0.012 -0.017  0.062]
         153 +1152 True 75 31.0s [ 0.025  0.03  -0.125]
         154 +1153 True 174 34.9s [ 0.002 -0.024 -0.026]
         155 +1154 True 172 28.5s [0.021 0.023 0.043]
         156 +1155 True 160 34.9s [-0.021 -0.013 -0.008]
         157 +1156 True 108 25.8s [-0.012  0.019 -0.024]
         158 +1157 True 168 33.7s [-0.021  0.011  0.056]
         159 +1158 True 76 27.4s [-0.018  0.011  0.046]
         160 +1159 True 110 30.0s [ 0.018 -0.031  0.085]
         161 +1160 True 98 29.4s [ 0.007 -0.023 -0.05 ]
         162 +1161 True 122 30.5s [ 0.021 -0.019  0.   ]
         163 +1162 True 201 31.3s [-0.014  0.005  0.069]
         164 +1163 True 188 29.5s [0.018 0.018 0.023]
         165 +1164 True 133 28.9s [-0.013  0.015 -0.078]
         166 +1165 True 99 29.1s [-0.013 -0.02   0.109]
         167 +1166 True 108 22.4s [-0.007  0.017  0.098]
         168 +1167 True 171 27.5s [ 0.02   0.008 -0.056]
         169 +1168 True 151 28.1s [ 0.018 -0.017 -0.064]
         170 +1169 True 128 29.1s [0.015 0.009 0.075]
         171 +1170 True 120 29.5s [ 0.019  0.034 -0.097]
         172 +1171 True 141 28.3s [ 0.007 -0.02   0.016]
         173 +1172 True 139 28.8s [ 0.014  0.01  -0.083]
         174 +1173 True 119 31.2s [ 0.004 -0.016 -0.061]
         175 +1174 True 126 28.3s [0.021 0.019 0.018]
         176 +1175 True 100 28.5s [-0.021 -0.016 -0.078]
         177 +1176 True 91 27.7s [-0.023 -0.006  0.062]
         178 +1177 True 112 26.7s [ 0.019  0.006 -0.052]
         179 +1178 True 122 26.4s [-0.025 -0.004  0.098]
         180 +1179 True 140 28.1s [ 0.027 -0.016 -0.074]
         181 +1180 True 161 27.2s [-0.008 -0.018  0.063]
         182 +1181 True 112 27.3s [-0.028  0.021  0.071]
         183 +1182 True 91 20.9s [0.02  0.019 0.039]
         184 +1183 True 139 29.5s [0.022 0.005 0.011]
         185 +1184 True 140 30.6s [ 0.008  0.025 -0.024]
         186 +1185 True 77 29.1s [ 0.001 -0.024 -0.123]
         187 +1186 True 78 19.8s [-0.018 -0.008  0.04 ]
         188 +1187 True 117 31.9s [0.025 0.008 0.065]
         189 +1188 True 210 33.8s [-0.021  0.01   0.067]
         190 +1189 True 74 23.6s [-0.009 -0.014  0.001]
         191 +1190 True 149 34.3s [-0.021  0.014 -0.073]
         192 +1191 True 140 31.8s [ 0.017  0.002 -0.07 ]
         193 +1192 True 213 32.9s [-0.016  0.002  0.069]
         194 +1193 True 140 31.4s [-0.01  -0.016 -0.068]
         195 +1194 True 148 31.3s [-0.021  0.013 -0.078]
         196 +1195 True 100 29.8s [ 0.021 -0.021  0.069]
         197 +1196 True 203 28.6s [ 0.017 -0.019 -0.068]
         198 +1197 True 89 15.5s [ 0.016 -0.006  0.06 ]
         199 +1198 True 127 25.8s [ 0.022 -0.01   0.047]
         200 +1199 True 233 35.2s [-0.014 -0.015 -0.069]
         201 +1200 True 118 28.8s [-0.024 -0.011 -0.105]
         202 +1201 True 165 31.6s [ 0.005  0.017 -0.047]
         203 +1202 True 142 30.1s [0.021 0.007 0.015]
         204 +1203 True 207 31.5s [ 0.025 -0.03   0.067]
         205 +1204 True 144 30.2s [ 0.006 -0.019  0.009]
         206 +1205 True 142 30.7s [0.    0.021 0.037]
         207 +1206 True 76 19.0s [ 0.01   0.018 -0.046]
         208 +1207 True 133 29.5s [ 0.02   0.02  -0.036]
         209 +1208 True 148 27.7s [ 0.02  -0.005 -0.015]
         210 +1209 True 164 28.2s [0.015 0.019 0.049]
         211 +1210 True 99 26.4s [-0.001  0.018 -0.047]
         212 +1211 True 105 28.3s [-0.017 -0.015 -0.075]
         213 +1212 True 199 30.9s [ 0.021  0.    -0.022]
         214 +1213 True 96 21.8s [0.004 0.014 0.081]
         215 +1214 True 193 30.6s [0.008 0.023 0.068]
         216 +1215 True 155 28.3s [-0.029 -0.017  0.07 ]
         217 +1216 True 156 28.3s [0.021 0.018 0.058]
         218 +1217 True 160 28.4s [ 0.011  0.012 -0.066]
         219 +1218 True 179 29.1s [ 0.018 -0.018 -0.005]
         220 +1219 True 134 27.5s [-0.013  0.019  0.051]
         221 +1220 True 116 27.2s [ 0.022 -0.003  0.068]
         222 +1221 True 179 31.0s [-0.008  0.024 -0.071]
         223 +1222 True 155 24.9s [ 0.016 -0.002 -0.062]
         224 +1223 True 224 31.8s [-0.022 -0.009  0.057]
         225 +1224 True 144 31.6s [-0.016 -0.014 -0.047]
         226 +1225 True 108 24.6s [ 0.018  0.005 -0.067]
         227 +1226 True 112 26.0s [0.02  0.006 0.083]
         228 +1227 True 163 27.9s [ 0.022 -0.004  0.045]
         229 +1228 True 140 27.1s [ 0.027 -0.026  0.06 ]
         230 +1229 True 121 28.2s [ 0.021  0.004 -0.063]
         231 +1230 True 163 28.1s [0.005 0.014 0.072]
         232 +1231 True 207 28.5s [-0.027 -0.024  0.033]
         233 +1232 True 135 27.0s [ 0.024 -0.026  0.018]
         234 +1233 True 131 26.4s [ 0.016 -0.018  0.073]
         235 +1234 True 148 27.5s [-0.023  0.004  0.   ]
         236 +1235 True 126 21.2s [-0.01   0.013 -0.091]
         237 +1236 True 112 30.5s [ 0.019 -0.006  0.065]
         238 +1237 True 173 31.3s [ 0.015 -0.015  0.069]
         239 +1238 True 136 29.4s [-0.002 -0.013 -0.045]
         240 +1239 True 129 28.1s [ 0.007  0.017 -0.042]
         241 +1240 True 118 28.6s [ 0.018 -0.002 -0.066]
         242 +1241 True 72 27.4s [ 0.012 -0.017 -0.033]
         243 +1242 True 141 23.8s [ 0.017  0.005 -0.021]
         244 +1243 True 137 29.7s [ 0.014 -0.021  0.05 ]
         245 +1244 True 165 27.8s [0.019 0.022 0.061]
         246 +1245 True 139 27.5s [ 0.013 -0.018  0.058]
         247 +1246 True 89 28.4s [-0.013  0.006 -0.068]
         248 +1247 True 167 29.6s [ 0.014 -0.024  0.031]
         249 +1248 True 104 24.0s [ 0.    -0.009  0.108]
         250 +1249 True 225 31.8s [ 0.02   0.013 -0.037]
         251 +1250 True 159 29.6s [0.013 0.004 0.019]
         252 +1251 True 82 14.6s [ 0.015  0.001 -0.093]
         253 +1252 True 197 30.7s [-0.021  0.019  0.04 ]
         254 +1253 True 153 29.9s [-0.01  -0.011 -0.076]
         255 +1254 True 119 29.5s [-0.01   0.021  0.013]
         256 +1255 True 248 31.5s [ 0.02  -0.016  0.056]
         257 +1256 True 155 30.1s [-0.024  0.019  0.045]
         258 +1257 True 249 30.9s [-0.025 -0.005 -0.064]
         259 +1258 True 241 31.1s [-0.006  0.02   0.058]
         260 +1259 True 121 29.5s [-0.013 -0.014 -0.005]
         261 +1260 True 66 9.7s [-0.024  0.005 -0.118]
         262 +1261 True 158 30.0s [-0.014 -0.021 -0.021]
         263 +1262 True 143 23.4s [ 0.004  0.019 -0.044]
         264 +1263 True 189 30.0s [-0.01  -0.021  0.027]
         265 +1264 True 123 29.4s [0.017 0.023 0.056]
         266 +1265 True 118 18.9s [ 0.016 -0.01   0.027]
         267 +1266 True 152 29.8s [-0.003 -0.016 -0.045]
         268 +1267 True 202 32.5s [0.019 0.03  0.064]
         269 +1268 True 139 30.1s [ 0.02  -0.021 -0.045]
         270 +1269 True 158 26.9s [ 0.023  0.005 -0.003]
         271 +1270 True 131 26.9s [ 0.023 -0.01   0.073]
         272 +1271 True 153 27.5s [-0.017 -0.024 -0.053]
         273 +1272 True 55 10.4s [ 0.002 -0.024  0.049]
         274 +1273 True 65 10.5s [ 0.022  0.02  -0.002]
         275 +1274 True 135 30.9s [-0.012  0.014 -0.004]
         276 +1275 True 166 28.8s [ 0.002  0.023 -0.027]
         277 +1276 True 75 23.8s [0.001 0.02  0.021]
         278 +1277 True 154 30.9s [ 0.019 -0.01   0.002]
         279 +1278 True 67 29.3s [ 0.022 -0.015 -0.067]
         280 +1279 True 94 18.4s [-0.01   0.011  0.068]
         281 +1280 True 119 29.7s [ 0.016 -0.01  -0.078]
         282 +1281 True 84 28.6s [-0.021 -0.01   0.056]
         283 +1282 True 139 26.9s [ 0.023 -0.018  0.066]
         284 +1283 True 112 28.6s [ 0.022  0.006 -0.025]
         285 +1284 True 132 28.9s [-0.023 -0.018 -0.001]
         286 +1285 True 182 28.8s [-0.02  -0.003  0.069]
         287 +1286 True 101 11.4s [-0.004 -0.016  0.003]
         288 +1287 True 117 22.1s [0.004 0.016 0.044]
         289 +1288 True 128 27.1s [0.008 0.019 0.004]
         290 +1289 True 137 28.1s [ 0.003  0.015 -0.087]
         291 +1290 True 192 28.2s [-0.021 -0.018 -0.047]
         292 +1291 True 78 16.3s [ 0.021  0.018 -0.037]
         293 +1292 True 64 15.5s [-0.017  0.02  -0.057]
         294 +1293 True 177 32.0s [ 0.019  0.011 -0.061]
         295 +1294 True 150 30.0s [-0.023 -0.02   0.035]
         296 +1295 True 152 30.2s [0.005 0.019 0.064]
         297 +1296 True 70 23.5s [ 0.028 -0.007 -0.069]
         298 +1297 True 114 19.8s [ 0.024 -0.008 -0.006]
         299 +1298 True 125 21.7s [ 0.004  0.023 -0.006]
         300 +1299 True 111 20.5s [0.019 0.011 0.037]
         301 +success 300 / 300 mean steps 136.10666666666665
```

</details>

<a id="C017"></a>
### C017 · Exception safety in get_action

Commit `c6a9370a7e45170cfb6a4578874266b55f59f134`; parents: b52486c74a756f308ecc27a8d0f14350395baa54. Recorded author date: 2026-09-30T18:36:01+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0729](01_timeline.md#E0729): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_c6a9370_approach.py) · [Exact all-file diff](evidence/diffs/C017_c6a9370.diff)

[Previous saved controller snapshot](evidence/versions/C015_159e97d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 40f3211..e79af21 100644
--- a/approach.py
+++ b/approach.py
@@ -409,6 +409,13 @@ class GeneratedApproach:
  409    409          return acts
  410    410  
  411    411      def get_action(self, state):
         412 +        try:
         413 +            return self._get_action(state)
         414 +        except Exception:
         415 +            self.plan = []
         416 +            return np.zeros(2, dtype=np.float64)
         417 +
         418 +    def _get_action(self, state):
  412    419          s = np.asarray(state, dtype=float)
  413    420          if (self.plan and self.REPLAN_K > 0 and self.t_used < 40.0 and self.plan[0][0] == 'push'
  414    421                  and self.push_count >= self.REPLAN_K and len(self.plan) > 2):
diff --git a/dbg.py b/dbg.py
index 91be273..ebf2c20 100644
--- a/dbg.py
+++ b/dbg.py
@@ -6,11 +6,12 @@ seed=int(sys.argv[1])
    6      6  env=make_env(); ap=GeneratedApproach(None,None,{})
    7      7  obs,info=env.reset(seed=seed); ap.reset(obs,info)
    8      8  orig=ap.plan_push
    9        -def pp(s):
   10        -    p=orig(s)
           9 +def pp(s, look=0):
          10 +    p=orig(s, look)
   11     11      print('t',t,'pose',np.round(s[0:3],3),'goal',np.round(s[29:32],3),'robot',np.round(s[16:18],2), 'plan', None if p is None else (len(p['path']), np.round(p['u'],2), round(p['L'],2), round(p['E0'],3), round(p['Epred'],3)))
   12     12      return p
   13     13  ap.plan_push=pp
          14 +import builtins
   14     15  for t in range(int(sys.argv[2])):
   15     16      a=ap.get_action(obs); obs,r,te,tr,_=env.step(a)
   16     17      if te: print('done',t); break
diff --git a/sw_ANGW1.6.txt b/sw_ANGW1.6.txt
new file mode 100644
index 0000000..26be997
--- /dev/null
+++ b/sw_ANGW1.6.txt
@@ -0,0 +1 @@
           1 +{"ANG_W":1.6} mean 145.11458333333334 succ 96 / 96
diff --git a/sw_ANGW3.0.txt b/sw_ANGW3.0.txt
new file mode 100644
index 0000000..a732432
--- /dev/null
+++ b/sw_ANGW3.0.txt
@@ -0,0 +1 @@
           1 +{"ANG_W":3.0} mean 146.13541666666666 succ 96 / 96
diff --git a/sw_REPLANK15.txt b/sw_REPLANK15.txt
new file mode 100644
index 0000000..5314c1e
--- /dev/null
+++ b/sw_REPLANK15.txt
@@ -0,0 +1 @@
           1 +{"REPLAN_K":15} mean 146.38541666666666 succ 96 / 96
diff --git a/sw_REPLANK6.txt b/sw_REPLANK6.txt
new file mode 100644
index 0000000..524904c
--- /dev/null
+++ b/sw_REPLANK6.txt
@@ -0,0 +1 @@
           1 +{"REPLAN_K":6} mean 146.92708333333334 succ 96 / 96
```

</details>

<a id="C018"></a>
### C018 · MARGIN class attr; res 5000-5300 300/300

Commit `9deee5d63426610c436c6adb8fd6dd53c248de01`; parents: c6a9370a7e45170cfb6a4578874266b55f59f134. Recorded author date: 2026-09-30T18:57:14+02:00.

File roles (automatic): policy, setup/other.

- [E0813](01_timeline.md#E0813): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_9deee5d_approach.py) · [Exact all-file diff](evidence/diffs/C018_9deee5d.diff)

[Previous saved controller snapshot](evidence/versions/C017_c6a9370_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e79af21..467ffcb 100644
--- a/approach.py
+++ b/approach.py
@@ -85,7 +85,7 @@ class GeneratedApproach:
   85     85          self.g = Geom(s[12], s[13], s[14])
   86     86          self.plan = []
   87     87          self.last_pose = None
   88        -        self.margin = (0.012, 0.03, 0.07)
          88 +        self.margin = tuple(self.MARGIN)
   89     89          self.t_used = 0.0
   90     90          self.push_count = 0
   91     91          self.t_used = 0.0
@@ -98,6 +98,7 @@ class GeneratedApproach:
   98     98      USE_CONTACT = True
   99     99      REPLAN_K = 10
  100    100      LOOK = 8
         101 +    MARGIN = (0.012, 0.03, 0.07)
  101    102  
  102    103      # ---------------- helpers ----------------
  103    104      def err(self, ref, th, goal):
diff --git a/res_5000.txt b/res_5000.txt
new file mode 100644
index 0000000..2a8ac71
--- /dev/null
+++ b/res_5000.txt
@@ -0,0 +1,301 @@
           1 +5000 True 105 19.1s [ 0.019 -0.007 -0.009]
           2 +5001 True 86 18.7s [-0.023  0.004  0.022]
           3 +5002 True 110 29.4s [ 0.016 -0.011  0.068]
           4 +5003 True 89 30.4s [-0.003 -0.021  0.039]
           5 +5004 True 118 28.7s [-0.009 -0.018  0.105]
           6 +5005 True 134 30.8s [0.025 0.02  0.048]
           7 +5006 True 106 24.4s [0.018 0.022 0.032]
           8 +5007 True 103 30.8s [ 0.004  0.016 -0.049]
           9 +5008 True 195 32.6s [-0.015  0.028  0.071]
          10 +5009 True 118 26.1s [-0.019  0.016 -0.056]
          11 +5010 True 104 20.0s [ 0.005  0.016 -0.024]
          12 +5011 True 224 32.8s [-0.022 -0.005 -0.005]
          13 +5012 True 167 26.6s [0.022 0.02  0.006]
          14 +5013 True 117 30.3s [ 0.009 -0.018  0.078]
          15 +5014 True 162 27.5s [ 0.013 -0.02   0.032]
          16 +5015 True 154 26.4s [ 0.017 -0.014  0.063]
          17 +5016 True 144 26.8s [ 0.025  0.019 -0.071]
          18 +5017 True 110 24.8s [ 0.018  0.003 -0.059]
          19 +5018 True 102 29.2s [-0.017  0.006 -0.075]
          20 +5019 True 84 29.5s [ 0.022 -0.021  0.052]
          21 +5020 True 103 23.9s [ 0.021 -0.011  0.093]
          22 +5021 True 91 19.7s [ 0.02   0.008 -0.064]
          23 +5022 True 73 20.4s [-0.015  0.013 -0.04 ]
          24 +5023 True 96 28.8s [ 0.001 -0.024 -0.085]
          25 +5024 True 175 31.0s [-0.015  0.021 -0.029]
          26 +5025 True 140 32.3s [-0.018 -0.015  0.017]
          27 +5026 True 208 27.9s [-0.021  0.016 -0.011]
          28 +5027 True 153 27.1s [-0.017  0.015  0.075]
          29 +5028 True 83 25.6s [ 0.023 -0.019 -0.025]
          30 +5029 True 112 26.9s [-0.     0.021 -0.008]
          31 +5030 True 123 26.7s [0.022 0.01  0.056]
          32 +5031 True 165 28.7s [ 0.02   0.02  -0.015]
          33 +5032 True 100 25.9s [ 0.001 -0.016  0.078]
          34 +5033 True 156 28.3s [-0.017  0.004 -0.063]
          35 +5034 True 210 28.7s [-0.016  0.006  0.065]
          36 +5035 True 130 27.6s [0.021 0.019 0.024]
          37 +5036 True 84 20.4s [0.013 0.021 0.032]
          38 +5037 True 175 28.3s [0.014 0.014 0.062]
          39 +5038 True 73 25.4s [ 0.009  0.01  -0.092]
          40 +5039 True 157 30.6s [-0.018 -0.004  0.055]
          41 +5040 True 103 25.0s [-0.017  0.021 -0.002]
          42 +5041 True 168 32.3s [-0.023  0.01  -0.008]
          43 +5042 True 119 24.6s [-0.001 -0.025  0.062]
          44 +5043 True 95 28.9s [0.006 0.021 0.044]
          45 +5044 True 140 30.3s [-0.003  0.022  0.027]
          46 +5045 True 133 24.7s [-0.009  0.016 -0.068]
          47 +5046 True 75 24.6s [ 0.016 -0.026  0.022]
          48 +5047 True 142 30.4s [ 0.023 -0.002 -0.071]
          49 +5048 True 78 15.3s [-0.007 -0.015  0.029]
          50 +5049 True 184 30.1s [-0.022 -0.011 -0.07 ]
          51 +5050 True 122 28.3s [ 0.02  -0.015 -0.068]
          52 +5051 True 112 29.4s [0.011 0.021 0.008]
          53 +5052 True 83 14.7s [ 0.017  0.018 -0.053]
          54 +5053 True 91 14.5s [ 0.01  -0.018 -0.087]
          55 +5054 True 74 24.2s [-0.009 -0.018 -0.063]
          56 +5055 True 182 30.1s [0.013 0.015 0.072]
          57 +5056 True 127 19.0s [ 0.021  0.    -0.035]
          58 +5057 True 88 18.6s [-0.017  0.031 -0.125]
          59 +5058 True 170 29.2s [-0.006 -0.025 -0.042]
          60 +5059 True 122 27.9s [-0.008 -0.021  0.057]
          61 +5060 True 231 31.1s [ 0.015  0.017 -0.055]
          62 +5061 True 190 31.2s [-0.027 -0.021  0.048]
          63 +5062 True 163 32.3s [0.018 0.013 0.077]
          64 +5063 True 142 34.9s [ 0.008  0.016 -0.058]
          65 +5064 True 115 18.4s [ 0.015 -0.015  0.076]
          66 +5065 True 216 31.2s [ 0.015 -0.017  0.036]
          67 +5066 True 62 20.3s [ 0.002 -0.018  0.054]
          68 +5067 True 155 36.7s [-0.022  0.024 -0.035]
          69 +5068 True 110 31.8s [-0.02  -0.012  0.065]
          70 +5069 True 42 8.6s [-0.024 -0.018 -0.047]
          71 +5070 True 185 28.9s [ 0.025 -0.012  0.067]
          72 +5071 True 81 34.5s [-0.017 -0.006 -0.086]
          73 +5072 True 149 34.6s [ 0.022 -0.012 -0.065]
          74 +5073 True 169 30.3s [0.014 0.005 0.034]
          75 +5074 True 65 24.9s [-0.009 -0.018  0.005]
          76 +5075 True 151 36.7s [ 0.012 -0.014  0.055]
          77 +5076 True 173 33.6s [-0.018 -0.014  0.039]
          78 +5077 True 167 31.5s [-0.017 -0.016 -0.066]
          79 +5078 True 174 34.8s [-0.024 -0.013  0.072]
          80 +5079 True 102 31.1s [-0.013 -0.011 -0.07 ]
          81 +5080 True 128 29.3s [ 0.023  0.001 -0.067]
          82 +5081 True 149 30.0s [-0.015  0.018  0.091]
          83 +5082 True 113 31.2s [ 0.018  0.022 -0.059]
          84 +5083 True 149 30.9s [-0.017 -0.015  0.044]
          85 +5084 True 137 31.1s [-0.03  -0.026  0.055]
          86 +5085 True 94 31.0s [0.005 0.016 0.072]
          87 +5086 True 172 32.8s [-0.017  0.022 -0.01 ]
          88 +5087 True 120 32.4s [-0.015 -0.013  0.06 ]
          89 +5088 True 122 29.6s [ 0.024 -0.014 -0.011]
          90 +5089 True 155 31.0s [ 0.022 -0.013 -0.063]
          91 +5090 True 148 33.0s [-0.007  0.017 -0.05 ]
          92 +5091 True 102 28.6s [-0.009  0.026  0.07 ]
          93 +5092 True 110 29.7s [ 0.026 -0.025 -0.08 ]
          94 +5093 True 119 28.4s [-0.016 -0.024  0.059]
          95 +5094 True 85 27.4s [-0.023  0.022  0.074]
          96 +5095 True 105 28.4s [-0.016 -0.007  0.02 ]
          97 +5096 True 153 29.1s [-0.018  0.02   0.018]
          98 +5097 True 100 29.2s [-0.022  0.005  0.066]
          99 +5098 True 68 26.8s [-0.007  0.017  0.076]
         100 +5099 True 174 31.3s [-0.003 -0.028 -0.085]
         101 +5100 True 116 30.8s [-0.     0.018  0.059]
         102 +5101 True 162 33.5s [-0.004 -0.019  0.018]
         103 +5102 True 66 31.9s [-0.026  0.012  0.057]
         104 +5103 True 123 34.4s [ 0.016  0.004 -0.074]
         105 +5104 True 119 32.8s [0.02  0.021 0.042]
         106 +5105 True 97 32.4s [ 0.003 -0.022  0.011]
         107 +5106 True 39 17.4s [-0.009 -0.022 -0.042]
         108 +5107 True 161 31.0s [-0.007 -0.016 -0.057]
         109 +5108 True 102 27.1s [ 0.022 -0.     0.053]
         110 +5109 True 165 31.5s [-0.014 -0.019  0.053]
         111 +5110 True 193 34.0s [-0.015 -0.021 -0.059]
         112 +5111 True 156 30.8s [-0.019 -0.02   0.065]
         113 +5112 True 155 35.6s [ 0.003  0.013 -0.042]
         114 +5113 True 150 36.1s [-0.017 -0.001  0.058]
         115 +5114 True 36 9.7s [-0.012 -0.025  0.061]
         116 +5115 True 144 28.2s [ 0.015 -0.016  0.065]
         117 +5116 True 139 37.1s [-0.024  0.023 -0.055]
         118 +5117 True 114 29.3s [ 0.021 -0.007  0.1  ]
         119 +5118 True 93 28.9s [-0.017  0.019  0.08 ]
         120 +5119 True 88 25.2s [ 0.016  0.002 -0.005]
         121 +5120 True 162 32.0s [0.019 0.011 0.045]
         122 +5121 True 145 30.1s [ 0.027 -0.015  0.075]
         123 +5122 True 112 33.9s [0.019 0.    0.137]
         124 +5123 True 132 32.9s [ 0.01  -0.02   0.092]
         125 +5124 True 145 34.7s [-0.015 -0.    -0.103]
         126 +5125 True 171 35.1s [ 0.021  0.006 -0.01 ]
         127 +5126 True 80 23.6s [-0.001  0.019 -0.058]
         128 +5127 True 155 32.8s [0.003 0.015 0.014]
         129 +5128 True 101 28.5s [-0.017  0.017  0.082]
         130 +5129 True 213 29.5s [ 0.028  0.001 -0.063]
         131 +5130 True 147 32.1s [ 0.003 -0.022 -0.052]
         132 +5131 True 137 27.4s [-0.022  0.008  0.011]
         133 +5132 True 85 18.5s [ 0.02  -0.01  -0.039]
         134 +5133 True 83 29.3s [-0.012  0.024  0.038]
         135 +5134 True 91 30.3s [-0.012  0.026 -0.072]
         136 +5135 True 130 23.8s [-0.02   0.008  0.024]
         137 +5136 True 129 31.1s [-0.016 -0.002  0.076]
         138 +5137 True 147 33.8s [-0.003  0.016  0.032]
         139 +5138 True 171 28.7s [-0.022 -0.014 -0.043]
         140 +5139 True 105 27.4s [-0.007  0.017 -0.016]
         141 +5140 True 237 31.7s [-0.019  0.005  0.068]
         142 +5141 True 166 29.8s [0.015 0.018 0.052]
         143 +5142 True 109 28.5s [ 0.034 -0.023  0.017]
         144 +5143 True 45 7.6s [-0.019 -0.008 -0.012]
         145 +5144 True 72 7.8s [-0.022  0.006  0.011]
         146 +5145 True 194 31.2s [ 0.009  0.019 -0.07 ]
         147 +5146 True 64 7.9s [-0.016  0.011  0.024]
         148 +5147 True 95 28.8s [-0.025  0.025  0.013]
         149 +5148 True 62 21.5s [ 0.014  0.02  -0.063]
         150 +5149 True 78 27.5s [ 0.006 -0.01  -0.074]
         151 +5150 True 193 31.0s [0.025 0.015 0.022]
         152 +5151 True 89 28.2s [-0.017  0.012  0.027]
         153 +5152 True 168 29.8s [0.015 0.004 0.042]
         154 +5153 True 187 30.4s [-0.007  0.024 -0.034]
         155 +5154 True 169 29.2s [ 0.015 -0.006 -0.033]
         156 +5155 True 211 30.8s [-0.019  0.013 -0.003]
         157 +5156 True 184 33.7s [ 0.005  0.014 -0.076]
         158 +5157 True 257 29.1s [-0.012  0.017 -0.084]
         159 +5158 True 128 31.5s [-0.022  0.019 -0.054]
         160 +5159 True 215 32.5s [ 0.015 -0.016  0.094]
         161 +5160 True 131 30.2s [-0.019 -0.016 -0.016]
         162 +5161 True 94 28.7s [-0.018  0.003  0.116]
         163 +5162 True 193 30.1s [ 0.02   0.015 -0.03 ]
         164 +5163 True 155 29.0s [ 0.007  0.014 -0.082]
         165 +5164 True 87 28.5s [-0.012  0.02  -0.003]
         166 +5165 True 205 30.6s [ 0.019 -0.003 -0.05 ]
         167 +5166 True 104 28.5s [ 0.006  0.012 -0.095]
         168 +5167 True 153 29.3s [ 0.019 -0.015 -0.03 ]
         169 +5168 True 80 22.3s [-0.    -0.02  -0.078]
         170 +5169 True 62 22.6s [-0.004 -0.024 -0.07 ]
         171 +5170 True 164 30.2s [-0.018 -0.004 -0.035]
         172 +5171 True 129 27.8s [-0.012  0.007 -0.057]
         173 +5172 True 188 29.3s [ 0.016 -0.026  0.071]
         174 +5173 True 161 27.9s [ 0.016  0.01  -0.058]
         175 +5174 True 96 26.0s [-0.002  0.015  0.081]
         176 +5175 True 107 27.9s [-0.018  0.01  -0.107]
         177 +5176 True 138 26.8s [-0.021 -0.005 -0.063]
         178 +5177 True 150 25.8s [ 0.022 -0.007  0.026]
         179 +5178 True 124 25.6s [ 0.022  0.019 -0.002]
         180 +5179 True 110 20.5s [-0.018  0.018  0.045]
         181 +5180 True 154 25.1s [-0.009 -0.021  0.019]
         182 +5181 True 131 29.9s [ 0.03   0.018 -0.094]
         183 +5182 True 49 20.1s [0.011 0.026 0.014]
         184 +5183 True 119 26.9s [-0.011  0.029  0.07 ]
         185 +5184 True 76 9.8s [-0.016  0.021 -0.039]
         186 +5185 True 133 27.0s [ 0.002  0.024 -0.034]
         187 +5186 True 108 27.1s [0.022 0.023 0.024]
         188 +5187 True 69 25.8s [-0.017  0.018  0.053]
         189 +5188 True 126 27.2s [ 0.02  -0.    -0.014]
         190 +5189 True 147 29.1s [-0.008 -0.014 -0.063]
         191 +5190 True 152 27.0s [ 0.021  0.01  -0.068]
         192 +5191 True 220 27.4s [-0.012 -0.018 -0.003]
         193 +5192 True 60 25.3s [-0.02   0.017  0.024]
         194 +5193 True 131 20.4s [ 0.024  0.016 -0.106]
         195 +5194 True 65 19.8s [ 0.018 -0.021  0.065]
         196 +5195 True 131 27.2s [-0.02  -0.009 -0.021]
         197 +5196 True 177 27.7s [ 0.017  0.013 -0.102]
         198 +5197 True 152 28.2s [-0.02  -0.024 -0.073]
         199 +5198 True 127 25.9s [-0.003  0.02   0.072]
         200 +5199 True 177 29.6s [ 0.019 -0.009  0.   ]
         201 +5200 True 186 32.2s [ 0.019  0.016 -0.006]
         202 +5201 True 141 32.0s [-0.018 -0.013 -0.081]
         203 +5202 True 118 30.8s [ 0.028  0.013 -0.027]
         204 +5203 True 163 31.1s [-0.015 -0.016  0.03 ]
         205 +5204 True 163 34.9s [ 0.021 -0.003 -0.092]
         206 +5205 True 143 27.1s [-0.009  0.016 -0.057]
         207 +5206 True 203 36.8s [-0.02   0.03   0.052]
         208 +5207 True 215 29.2s [0.009 0.014 0.016]
         209 +5208 True 180 30.2s [ 0.015  0.023 -0.053]
         210 +5209 True 129 27.9s [ 0.014 -0.016  0.102]
         211 +5210 True 78 26.0s [0.022 0.026 0.062]
         212 +5211 True 200 31.2s [ 0.021 -0.009 -0.072]
         213 +5212 True 115 29.8s [ 0.006 -0.016  0.067]
         214 +5213 True 122 27.4s [-0.004  0.022 -0.006]
         215 +5214 True 198 31.5s [-0.016  0.009 -0.052]
         216 +5215 True 144 27.9s [-0.024  0.019  0.046]
         217 +5216 True 144 29.5s [-0.021 -0.015 -0.074]
         218 +5217 True 76 20.7s [0.023 0.002 0.076]
         219 +5218 True 132 30.9s [ 0.028 -0.015  0.051]
         220 +5219 True 104 25.3s [-0.022  0.001  0.01 ]
         221 +5220 True 98 31.7s [-0.022  0.004  0.05 ]
         222 +5221 True 192 34.4s [ 0.02  -0.017 -0.103]
         223 +5222 True 120 31.4s [ 0.013 -0.021  0.059]
         224 +5223 True 179 34.7s [-0.013 -0.012  0.061]
         225 +5224 True 144 32.2s [0.013 0.013 0.064]
         226 +5225 True 112 28.0s [-0.012 -0.018 -0.051]
         227 +5226 True 175 28.5s [-0.014 -0.003  0.101]
         228 +5227 True 137 30.6s [ 0.011 -0.016 -0.049]
         229 +5228 True 153 36.3s [ 0.027  0.004 -0.076]
         230 +5229 True 81 35.6s [ 0.001 -0.013 -0.038]
         231 +5230 True 61 27.4s [-0.002 -0.016 -0.071]
         232 +5231 True 94 30.1s [ 0.005 -0.017 -0.041]
         233 +5232 True 177 31.4s [0.016 0.019 0.057]
         234 +5233 True 128 28.6s [ 0.017  0.012 -0.017]
         235 +5234 True 48 29.0s [-0.02 -0.02  0.07]
         236 +5235 True 161 31.5s [0.001 0.013 0.079]
         237 +5236 True 157 33.1s [ 0.008 -0.019  0.027]
         238 +5237 True 95 28.6s [-0.004  0.022  0.06 ]
         239 +5238 True 163 34.3s [ 0.018  0.022 -0.065]
         240 +5239 True 79 33.3s [-0.007  0.021 -0.037]
         241 +5240 True 99 27.7s [-0.     0.014  0.03 ]
         242 +5241 True 188 36.2s [-0.02   0.015 -0.059]
         243 +5242 True 143 31.2s [-0.016  0.005 -0.067]
         244 +5243 True 125 28.1s [ 0.019  0.01  -0.086]
         245 +5244 True 144 33.8s [-0.01   0.019 -0.07 ]
         246 +5245 True 152 33.7s [ 0.019 -0.002  0.06 ]
         247 +5246 True 116 31.0s [ 0.025  0.018 -0.072]
         248 +5247 True 79 27.3s [ 0.021 -0.023  0.071]
         249 +5248 True 134 32.4s [-0.019 -0.009  0.043]
         250 +5249 True 167 31.9s [ 0.001  0.022 -0.067]
         251 +5250 True 139 33.2s [ 0.015 -0.016  0.063]
         252 +5251 True 148 31.7s [0.016 0.012 0.067]
         253 +5252 True 204 32.1s [ 0.024 -0.01   0.018]
         254 +5253 True 131 31.0s [-0.022  0.017 -0.044]
         255 +5254 True 200 32.9s [0.015 0.021 0.072]
         256 +5255 True 118 28.8s [-0.021  0.01  -0.047]
         257 +5256 True 168 33.2s [-0.009 -0.023 -0.007]
         258 +5257 True 177 32.3s [ 0.013  0.023 -0.071]
         259 +5258 True 179 33.0s [-0.024 -0.011 -0.001]
         260 +5259 True 166 35.8s [-0.018 -0.011 -0.087]
         261 +5260 True 156 33.7s [-0.02  -0.001  0.042]
         262 +5261 True 175 36.0s [-0.02   0.019  0.052]
         263 +5262 True 232 36.2s [-0.02   0.008 -0.039]
         264 +5263 True 95 30.0s [-0.017 -0.017  0.112]
         265 +5264 True 89 31.0s [ 0.016  0.028 -0.007]
         266 +5265 True 141 33.4s [0.008 0.021 0.083]
         267 +5266 True 198 35.9s [ 0.021  0.021 -0.063]
         268 +5267 True 129 34.0s [ 0.021  0.009 -0.011]
         269 +5268 True 136 30.5s [-0.014 -0.016 -0.068]
         270 +5269 True 62 29.9s [ 0.022  0.02  -0.006]
         271 +5270 True 101 29.1s [-0.     0.018 -0.056]
         272 +5271 True 185 30.2s [0.008 0.023 0.069]
         273 +5272 True 167 29.6s [-0.017  0.019  0.071]
         274 +5273 True 133 27.6s [-0.017  0.011  0.056]
         275 +5274 True 160 30.9s [0.021 0.015 0.106]
         276 +5275 True 150 28.3s [-0.019 -0.006  0.051]
         277 +5276 True 171 30.5s [-0.02  -0.     0.022]
         278 +5277 True 80 25.9s [-0.016 -0.01   0.083]
         279 +5278 True 94 29.8s [ 0.011 -0.014  0.   ]
         280 +5279 True 109 29.8s [-0.012  0.022 -0.021]
         281 +5280 True 106 30.0s [-0.02  -0.008 -0.062]
         282 +5281 True 228 31.7s [0.003 0.017 0.017]
         283 +5282 True 134 30.6s [ 0.021 -0.02  -0.023]
         284 +5283 True 120 19.8s [ 0.028 -0.012 -0.052]
         285 +5284 True 170 33.4s [-0.005 -0.021  0.073]
         286 +5285 True 111 29.4s [-0.029  0.025  0.083]
         287 +5286 True 94 21.2s [ 0.012 -0.018  0.068]
         288 +5287 True 144 31.3s [-0.016 -0.022 -0.011]
         289 +5288 True 163 31.5s [ 0.016 -0.001 -0.04 ]
         290 +5289 True 174 32.3s [ 0.017 -0.017  0.076]
         291 +5290 True 92 29.2s [ 0.02  -0.012  0.063]
         292 +5291 True 179 31.8s [-0.015  0.003 -0.065]
         293 +5292 True 110 26.3s [-0.017 -0.018 -0.011]
         294 +5293 True 242 28.9s [-0.003 -0.02   0.039]
         295 +5294 True 155 27.1s [ 0.003 -0.015  0.072]
         296 +5295 True 98 27.1s [0.018 0.021 0.028]
         297 +5296 True 182 27.4s [-0.004 -0.018  0.01 ]
         298 +5297 True 170 27.2s [ 0.001 -0.016  0.093]
         299 +5298 True 47 11.8s [-0.019 -0.016  0.053]
         300 +5299 True 165 14.9s [ 0.015  0.016 -0.057]
         301 +success 300 / 300 mean steps 133.80333333333334
```

</details>

<a id="C019"></a>
### C019 · Final sweeps

Commit `936a3d271afdec81ccc81a3a57d8e0bd2311fd58`; parents: 9deee5d63426610c436c6adb8fd6dd53c248de01. Recorded author date: 2026-09-30T19:03:57+02:00.

File roles (automatic): setup/other.

- [E0816](01_timeline.md#E0816): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C019_936a3d2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/sw_m0008002005.txt b/sw_m0008002005.txt
new file mode 100644
index 0000000..9395de4
--- /dev/null
+++ b/sw_m0008002005.txt
@@ -0,0 +1 @@
           1 +{"MARGIN":[0.008,0.02,0.05]} mean 142.79166666666666 succ 96 / 96
diff --git a/sw_m0015005008.txt b/sw_m0015005008.txt
new file mode 100644
index 0000000..af30a69
--- /dev/null
+++ b/sw_m0015005008.txt
@@ -0,0 +1 @@
           1 +{"MARGIN":[0.015,0.05,0.08]} mean 142.86458333333334 succ 96 / 96
diff --git a/sw_m0018004009.txt b/sw_m0018004009.txt
new file mode 100644
index 0000000..d7320ad
--- /dev/null
+++ b/sw_m0018004009.txt
@@ -0,0 +1 @@
           1 +{"MARGIN":[0.018,0.04,0.09]} mean 142.36458333333334 succ 96 / 96
```

</details>

