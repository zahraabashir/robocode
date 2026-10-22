# DynPushT2D · claude-opus-5-5 · replicate 444: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `a30f286` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `3ed9cea` | Initial model-based push controller skeleton | approach.py, geom_probe.py, plib.py, probe.py, probe2.py, probe3.py, probe4.py, test_approach.py | [E0074](01_timeline.md#E0074) |
| [C003](#C003) · `7d6d193` | Fix T geometry (origin at bar top-center), cap action at 0.049 | approach.py | [E0296](01_timeline.md#E0296) |
| [C004](#C004) · `6178627` | Staging point for approach, filter infeasible push candidates | approach.py, test_approach.py | [E0354](01_timeline.md#E0354) |
| [C005](#C005) · `0d1ab3f` | Wall filter for staging points, stuck detection | approach.py | [E0379](01_timeline.md#E0379) |
| [C006](#C006) · `fa5ec44` | Use fitted vectorized push model in planner | approach.py, model_v.py | [E0392](01_timeline.md#E0392) |
| [C007](#C007) · `97868d9` | Step-based planner score, goal detection, in-contact candidates, speeds, periodic replanning | approach.py, cmp_model.py, col_0.log, col_1.log, col_2.log, col_3.log, col_4.log, col_5.log, col_6.log, col_7.log, collect.py, dbg.py, dbg2.py, dbg3.py, dbg4.py, evalp.py, fit.py,… | [E0406](01_timeline.md#E0406) |
| [C008](#C008) · `4f0f793` | Progress-rate push selection | approach.py, dbg.py | [E0447](01_timeline.md#E0447) |
| [C009](#C009) · `3563285` | tunable params | approach.py, tune.py | [E0471](01_timeline.md#E0471) |
| [C010](#C010) · `8bfdcfc` | two-level lookahead (M param), zero action in goal | approach.py | [E0512](01_timeline.md#E0512) |
| [C011](#C011) · `3c87638` | M=0 | approach.py, dbg.py | [E0519](01_timeline.md#E0519) |
| [C012](#C012) · `b0a3cf9` | visibility-graph travel estimate for all candidates | approach.py | [E0537](01_timeline.md#E0537) |
| [C013](#C013) · `6e77bfe` | infl 0.115 | approach.py | [E0544](01_timeline.md#E0544) |
| [C014](#C014) · `e6da664` | wa=0.4, cost_mode option | approach.py | [E0557](01_timeline.md#E0557) |
| [C015](#C015) · `1fe8cd7` | Use raw (unwrapped) angle error: env termination does not wrap theta | approach.py, tune.py | [E0652](01_timeline.md#E0652) |
| [C016](#C016) · `515fcbf` | Wall-aware push validity, push stall detection, time guard | approach.py | [E0672](01_timeline.md#E0672) |
| [C017](#C017) · `a5e6da0` | Angle target: centre of the valid wrapped interval (env compares wrapped theta without wrapping diff) | approach.py | [E0690](01_timeline.md#E0690) |
| [C018](#C018) · `daa2253` | Push blacklist on stall/model mismatch; wall-clearance subgoal when stuck | approach.py | [E0736](01_timeline.md#E0736) |
| [C019](#C019) · `8730159` | Direct approach to push start (no staging), pre_clear param | approach.py | [E0765](01_timeline.md#E0765) |
| [C020](#C020) · `8e82a4d` | la_mode, candidate params | approach.py | [E0784](01_timeline.md#E0784) |
| [C021](#C021) · `a5e1d82` | wider push angles, tighter final approach | approach.py, tune.py | [E0799](01_timeline.md#E0799) |
| [C022](#C022) · `26c0676` | add debug scripts/data | data_0.npz, data_1.npz, data_2.npz, data_3.npz, data_4.npz, data_5.npz, data_6.npz, data_7.npz, dbg5.py, dbg6.py, dbg7.py, res.txt, res_wide.txt, stats.py, stats2.py, thcheck.py, … | [E0830](01_timeline.md#E0830) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `a30f2867fccb3d28f89c3b506561ac0a4ccd61fb`; parents: none (initial snapshot). Recorded author date: 2026-09-30T17:07:14+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_a30f286.diff)

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
index 0000000..71a6469
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "b33957308e47ba85e33e5388b6d35873", "observation_space": {"type": "Box", "shape": [45], "low": [-Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity], "high": [Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity], "dtype": "float64"}, "action_space": {"type": "Box", "shape": [2], "low": [-0.05, -0.05], "high": [0.05, 0.05], "dtype": "float64"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Initial model-based push controller skeleton

Commit `3ed9cea8bdb73ce4171f7c10e60ed91f65765d48`; parents: a30f2867fccb3d28f89c3b506561ac0a4ccd61fb. Recorded author date: 2026-09-30T17:09:59+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0074](01_timeline.md#E0074): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_3ed9cea_approach.py) · [Exact all-file diff](evidence/diffs/C002_3ed9cea.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..4420811
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,348 @@
           1 +"""Push-T controller: model-based greedy push selection + visibility-graph navigation."""
           2 +import heapq
           3 +import math
           4 +
           5 +import numpy as np
           6 +
           7 +R_ROBOT = 0.1
           8 +WALL_LO = 0.0
           9 +WALL_HI = 5.0
          10 +MAXD = 0.05
          11 +
          12 +
          13 +def wrap(a):
          14 +    return (a + math.pi) % (2 * math.pi) - math.pi
          15 +
          16 +
          17 +def local_poly(w, lh, lv):
          18 +    """T polygon in the block frame, CCW order."""
          19 +    a, h = lh / 2.0, w / 2.0
          20 +    return np.array([
          21 +        [-a, h], [-a, -h], [-h, -h], [-h, -lv], [h, -lv], [h, -h], [a, -h], [a, h],
          22 +    ])
          23 +
          24 +
          25 +def rects_local(w, lh, lv):
          26 +    a, h = lh / 2.0, w / 2.0
          27 +    # (xmin, xmax, ymin, ymax)
          28 +    return [(-a, a, -h, h), (-h, h, -lv, -h)]
          29 +
          30 +
          31 +def to_world(pts, pose):
          32 +    c, s = math.cos(pose[2]), math.sin(pose[2])
          33 +    R = np.array([[c, -s], [s, c]])
          34 +    return pts @ R.T + np.asarray(pose[:2])
          35 +
          36 +
          37 +def to_local(pts, pose):
          38 +    c, s = math.cos(pose[2]), math.sin(pose[2])
          39 +    R = np.array([[c, -s], [s, c]])
          40 +    return (np.asarray(pts) - np.asarray(pose[:2])) @ R
          41 +
          42 +
          43 +def dist_to_T_local(p, rects):
          44 +    """Signed-ish distance from local point(s) p (N,2) to the union of rects (positive outside)."""
          45 +    p = np.atleast_2d(p)
          46 +    best = None
          47 +    for (x0, x1, y0, y1) in rects:
          48 +        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
          49 +        hx, hy = (x1 - x0) / 2, (y1 - y0) / 2
          50 +        dx = np.abs(p[:, 0] - cx) - hx
          51 +        dy = np.abs(p[:, 1] - cy) - hy
          52 +        out = np.hypot(np.maximum(dx, 0), np.maximum(dy, 0))
          53 +        ins = np.minimum(np.maximum(dx, dy), 0)
          54 +        d = out + ins
          55 +        best = d if best is None else np.minimum(best, d)
          56 +    return best
          57 +
          58 +
          59 +class TModel:
          60 +    """Quasi-static single point contact push model (placeholder / fitted params)."""
          61 +
          62 +    def __init__(self, w, lh, lv, com=(0.0, None), rho2=None, mu=0.3):
          63 +        self.w, self.lh, self.lv = w, lh, lv
          64 +        self.rects = rects_local(w, lh, lv)
          65 +        self.poly = local_poly(w, lh, lv)
          66 +        # geometric centroid
          67 +        a1 = lh * w
          68 +        a2 = (lv - w / 2) * w
          69 +        cy = (a2 * (-(lv + w / 2) / 2)) / (a1 + a2)
          70 +        self.com = np.array([0.0, cy if com[1] is None else com[1]])
          71 +        if rho2 is None:
          72 +            # radius of gyration^2 about com (uniform density)
          73 +            i1 = a1 * (lh ** 2 + w ** 2) / 12 + a1 * (0 - self.com[1]) ** 2
          74 +            l2 = lv - w / 2
          75 +            i2 = a2 * (l2 ** 2 + w ** 2) / 12 + a2 * (-(lv + w / 2) / 2 - self.com[1]) ** 2
          76 +            rho2 = (i1 + i2) / (a1 + a2)
          77 +        self.rho2 = rho2
          78 +        self.mu = mu
          79 +
          80 +    def closest_local(self, p):
          81 +        """Closest boundary point and outward normal for local points p (N,2)."""
          82 +        p = np.atleast_2d(p)
          83 +        best_d = np.full(len(p), np.inf)
          84 +        best_q = np.zeros_like(p)
          85 +        best_n = np.zeros_like(p)
          86 +        poly = self.poly
          87 +        n = len(poly)
          88 +        for i in range(n):
          89 +            a = poly[i]
          90 +            b = poly[(i + 1) % n]
          91 +            ab = b - a
          92 +            L2 = ab @ ab
          93 +            t = np.clip(((p - a) @ ab) / L2, 0, 1)
          94 +            q = a + t[:, None] * ab
          95 +            d = np.hypot(p[:, 0] - q[:, 0], p[:, 1] - q[:, 1])
          96 +            m = d < best_d
          97 +            best_d = np.where(m, d, best_d)
          98 +            best_q[m] = q[m]
          99 +            # outward normal for CCW polygon: (dy, -dx)
         100 +            nn = np.array([ab[1], -ab[0]]) / math.sqrt(L2)
         101 +            best_n[m] = nn
         102 +        return best_q, best_n, best_d
         103 +
         104 +    def step(self, pose, robot, act):
         105 +        """Vectorized: pose (N,3), robot (N,2), act (N,2) -> new pose (N,3), new robot (N,2)."""
         106 +        pose = np.atleast_2d(pose).astype(float)
         107 +        robot = np.atleast_2d(robot).astype(float)
         108 +        act = np.atleast_2d(act).astype(float)
         109 +        newr = robot + act
         110 +        th = pose[:, 2]
         111 +        c, s = np.cos(th), np.sin(th)
         112 +        # to local
         113 +        d = newr - pose[:, :2]
         114 +        pl = np.stack([c * d[:, 0] + s * d[:, 1], -s * d[:, 0] + c * d[:, 1]], 1)
         115 +        al = np.stack([c * act[:, 0] + s * act[:, 1], -s * act[:, 0] + c * act[:, 1]], 1)
         116 +        inside = dist_to_T_local(pl, self.rects) < 0
         117 +        q, n, dist = self.closest_local(pl)
         118 +        # for points inside the polygon, closest boundary normal is correct (pointing out)
         119 +        pen = np.where(inside, R_ROBOT + dist, R_ROBOT - dist)
         120 +        active = pen > 1e-9
         121 +        out = pose.copy()
         122 +        if not np.any(active):
         123 +            return out, newr
         124 +        # contact point approx q, push direction into block = -n
         125 +        r = q - self.com
         126 +        # frictional: push direction within friction cone around -n toward -al projection
         127 +        fn = -n
         128 +        tdir = np.stack([-fn[:, 1], fn[:, 0]], 1)
         129 +        at = np.sum(al * tdir, 1)
         130 +        an = np.sum(al * fn, 1)
         131 +        # force direction: normal + mu*sign(tangential motion) (sticking approx if small)
         132 +        ratio = np.clip(np.where(an > 1e-9, at / np.maximum(an, 1e-9), 0.0), -self.mu, self.mu)
         133 +        f = fn + ratio[:, None] * tdir
         134 +        tau = r[:, 0] * f[:, 1] - r[:, 1] * f[:, 0]
         135 +        v = f
         136 +        om = tau / self.rho2
         137 +        # velocity of contact point along fn per unit scale
         138 +        vc = v + np.stack([-om * r[:, 1], om * r[:, 0]], 1)
         139 +        vn = np.sum(vc * fn, 1)
         140 +        k = np.where(active, pen / np.maximum(vn, 1e-6), 0.0)
         141 +        # block displacement (local, of com)
         142 +        dv = v * k[:, None]
         143 +        dom = om * k
         144 +        # new com position local: com + dv; origin moves as rotation about com
         145 +        cd, sd = np.cos(dom), np.sin(dom)
         146 +        oc = -self.com  # origin relative to com
         147 +        oc_new = np.stack([cd * oc[0] - sd * oc[1], sd * oc[0] + cd * oc[1]], 1)
         148 +        o_new_local = self.com + dv + oc_new
         149 +        wx = c * o_new_local[:, 0] - s * o_new_local[:, 1]
         150 +        wy = s * o_new_local[:, 0] + c * o_new_local[:, 1]
         151 +        out[:, 0] = pose[:, 0] + wx
         152 +        out[:, 1] = pose[:, 1] + wy
         153 +        out[:, 2] = th + dom
         154 +        return out, newr
         155 +
         156 +
         157 +class GeneratedApproach:
         158 +    def __init__(self, action_space, observation_space, primitives):
         159 +        self.action_space = action_space
         160 +        self.model = None
         161 +
         162 +    # ------------------------------------------------------------------
         163 +    def reset(self, state, info):
         164 +        s = np.asarray(state, dtype=float)
         165 +        self.w, self.lh, self.lv = s[12], s[13], s[14]
         166 +        self.model = TModel(self.w, self.lh, self.lv)
         167 +        self.goal = s[29:32].copy()
         168 +        self.mode = "plan"
         169 +        self.path = []
         170 +        self.push = None
         171 +        self.push_left = 0
         172 +        self.stall = 0
         173 +
         174 +    # ------------------------------------------------------------------
         175 +    def cost(self, pose):
         176 +        pose = np.atleast_2d(pose)
         177 +        dp = pose[:, :2] - self.goal[:2]
         178 +        da = np.abs(wrap_arr(pose[:, 2] - self.goal[2]))
         179 +        return np.hypot(dp[:, 0], dp[:, 1]) + 0.6 * da
         180 +
         181 +    def solved(self, pose):
         182 +        return (abs(pose[0] - self.goal[0]) < 0.03 and abs(pose[1] - self.goal[1]) < 0.03
         183 +                and abs(wrap(pose[2] - self.goal[2])) < math.radians(8))
         184 +
         185 +    # ------------------------------------------------------------------
         186 +    def candidates(self, pose):
         187 +        """Candidate pushes: list of (start_pt_world, dir_world)."""
         188 +        poly = self.model.poly
         189 +        n = len(poly)
         190 +        starts, dirs = [], []
         191 +        for i in range(n):
         192 +            a, b = poly[i], poly[(i + 1) % n]
         193 +            ab = b - a
         194 +            L = np.linalg.norm(ab)
         195 +            if L < 0.05:
         196 +                continue
         197 +            nn = np.array([ab[1], -ab[0]]) / L
         198 +            m = max(2, int(L / 0.06))
         199 +            for t in np.linspace(0.04 / L, 1 - 0.04 / L, m) if L > 0.1 else [0.5]:
         200 +                q = a + t * ab
         201 +                for ang in (-0.5, -0.25, 0.0, 0.25, 0.5):
         202 +                    ca, sa = math.cos(ang), math.sin(ang)
         203 +                    d = -nn
         204 +                    d = np.array([ca * d[0] - sa * d[1], sa * d[0] + ca * d[1]])
         205 +                    starts.append(q + nn * (R_ROBOT + 0.02))
         206 +                    dirs.append(d)
         207 +        starts = np.array(starts)
         208 +        dirs = np.array(dirs)
         209 +        return to_world(starts, pose), to_world(dirs, (0, 0, pose[2]))
         210 +
         211 +    def plan_push(self, pose, robot):
         212 +        sw, dw = self.candidates(pose)
         213 +        N = len(sw)
         214 +        # filter starts that are outside walls
         215 +        ok = np.all((sw > WALL_LO + R_ROBOT + 0.01) & (sw < WALL_HI - R_ROBOT - 0.01), 1)
         216 +        sw, dw = sw[ok], dw[ok]
         217 +        N = len(sw)
         218 +        poses = np.repeat(pose[None], N, 0)
         219 +        rob = sw.copy()
         220 +        c0 = self.cost(pose)[0]
         221 +        best = (np.inf, None)
         222 +        H = 40
         223 +        steplen = MAXD
         224 +        travel = np.hypot(*(sw - robot).T) / MAXD
         225 +        cur = poses
         226 +        bestscore = np.full(N, np.inf)
         227 +        bestk = np.zeros(N, int)
         228 +        for k in range(1, H + 1):
         229 +            cur, rob = self.model.step(cur, rob, dw * steplen)
         230 +            cst = self.cost(cur)
         231 +            # score: resulting cost + time penalty
         232 +            score = cst + 0.004 * (k + travel)
         233 +            m = score < bestscore
         234 +            bestscore[m] = score[m]
         235 +            bestk[m] = k
         236 +        i = int(np.argmin(bestscore))
         237 +        return sw[i], dw[i], bestk[i], bestscore[i], c0
         238 +
         239 +    # ------------------------------------------------------------------
         240 +    def nav_path(self, robot, target, pose):
         241 +        """Visibility-graph path around inflated T."""
         242 +        infl = R_ROBOT + 0.03
         243 +        rects = self.model.rects
         244 +
         245 +        def free_seg(p, q):
         246 +            pl = to_local(np.array([p, q]), pose)
         247 +            ts = np.linspace(0, 1, max(2, int(np.linalg.norm(q - p) / 0.02) + 2))
         248 +            pts = pl[0] + ts[:, None] * (pl[1] - pl[0])
         249 +            return np.all(dist_to_T_local(pts, rects) > infl - 1e-6)
         250 +
         251 +        if free_seg(robot, target):
         252 +            return [target]
         253 +        a, h = self.lh / 2, self.w / 2
         254 +        e = infl + 0.05
         255 +        lv = self.lv
         256 +        nodes_local = np.array([
         257 +            [-a - e, h + e], [a + e, h + e], [a + e, -h - e], [-a - e, -h - e],
         258 +            [h + e, -h - e], [-h - e, -h - e], [h + e, -lv - e], [-h - e, -lv - e],
         259 +            [0, h + e], [0, -lv - e],
         260 +        ])
         261 +        nodes = list(to_world(nodes_local, pose))
         262 +        nodes = [p for p in nodes if np.all(p > WALL_LO + R_ROBOT) and np.all(p < WALL_HI - R_ROBOT)]
         263 +        pts = [np.asarray(robot)] + nodes + [np.asarray(target)]
         264 +        n = len(pts)
         265 +        dist = [np.inf] * n
         266 +        prev = [-1] * n
         267 +        dist[0] = 0
         268 +        pq = [(0, 0)]
         269 +        while pq:
         270 +            d, u = heapq.heappop(pq)
         271 +            if d > dist[u]:
         272 +                continue
         273 +            if u == n - 1:
         274 +                break
         275 +            for v in range(n):
         276 +                if v == u:
         277 +                    continue
         278 +                if not free_seg(pts[u], pts[v]) and not (u == 0 and self._escape_ok(pts[u], pts[v], pose)):
         279 +                    continue
         280 +                nd = d + np.linalg.norm(pts[v] - pts[u])
         281 +                if nd < dist[v]:
         282 +                    dist[v] = nd
         283 +                    prev[v] = u
         284 +                    heapq.heappush(pq, (nd, v))
         285 +        if dist[n - 1] == np.inf:
         286 +            return [target]
         287 +        path = []
         288 +        v = n - 1
         289 +        while v != 0:
         290 +            path.append(pts[v])
         291 +            v = prev[v]
         292 +        return path[::-1]
         293 +
         294 +    def _escape_ok(self, p, q, pose):
         295 +        # allow leaving if robot currently inside inflated zone and moving away
         296 +        pl = to_local(np.array([p, q]), pose)
         297 +        d0 = dist_to_T_local(pl[:1], self.model.rects)[0]
         298 +        if d0 > R_ROBOT + 0.03:
         299 +            return False
         300 +        ts = np.linspace(0, 1, 20)
         301 +        pts = pl[0] + ts[:, None] * (pl[1] - pl[0])
         302 +        dd = dist_to_T_local(pts, self.model.rects)
         303 +        return np.all(dd >= d0 - 1e-6) and dd[-1] > R_ROBOT + 0.03
         304 +
         305 +    # ------------------------------------------------------------------
         306 +    def get_action(self, state):
         307 +        s = np.asarray(state, dtype=float)
         308 +        pose = s[0:3].copy()
         309 +        robot = s[16:18].copy()
         310 +        if self.model is None:
         311 +            self.reset(state, {})
         312 +        for _ in range(4):
         313 +            if self.mode == "plan":
         314 +                st, d, k, sc, c0 = self.plan_push(pose, robot)
         315 +                self.push = (st, d)
         316 +                self.push_left = k + 3
         317 +                self.path = self.nav_path(robot, st, pose)
         318 +                self.plan_pose = pose.copy()
         319 +                self.mode = "nav"
         320 +            if self.mode == "nav":
         321 +                if not self.path:
         322 +                    self.mode = "push"
         323 +                    continue
         324 +                tgt = self.path[0]
         325 +                dv = tgt - robot
         326 +                dn = np.linalg.norm(dv)
         327 +                if dn < 1e-3:
         328 +                    self.path.pop(0)
         329 +                    continue
         330 +                if dn <= MAXD:
         331 +                    self.path.pop(0)
         332 +                    return dv
         333 +                return dv / dn * MAXD
         334 +            if self.mode == "push":
         335 +                if self.push_left <= 0:
         336 +                    self.mode = "plan"
         337 +                    continue
         338 +                self.push_left -= 1
         339 +                d = self.push[1]
         340 +                # slow down near goal
         341 +                c = self.cost(pose)[0]
         342 +                sp = MAXD if c > 0.2 else max(0.01, MAXD * c / 0.2)
         343 +                return d * sp
         344 +        return np.zeros(2)
         345 +
         346 +
         347 +def wrap_arr(a):
         348 +    return (a + np.pi) % (2 * np.pi) - np.pi
diff --git a/geom_probe.py b/geom_probe.py
new file mode 100644
index 0000000..3f2f913
--- /dev/null
+++ b/geom_probe.py
@@ -0,0 +1,29 @@
           1 +from plib import *
           2 +np.set_printoptions(precision=4, suppress=True, linewidth=200)
           3 +env=make_env()
           4 +res=[]
           5 +for seed in range(12):
           6 +    for name,start,dirn in [('bartop',(0,0.45),(0,-1)),('stemend',(0,-1.7),(0,1)),('barbot',(0.35,-0.5),(0,1)),
           7 +                            ('barend',(0.95,0),(-1,0)),('stemside',(0.45,-0.8),(-1,0)),('barbotL',(-0.35,-0.5),(0,1))]:
           8 +        obs,_=env.reset(seed=seed)
           9 +        pose=obs[0:3].copy(); w,Lh,Lv=obs[12:15]
          10 +        st=np.array(start,float)
          11 +        if name=='barend': st[0]=Lh/2+0.35
          12 +        if name=='stemend': st[1]=-Lv-0.5
          13 +        sw=to_world(pose,st)
          14 +        if sw.min()<0.15 or sw.max()>4.85: continue
          15 +        obs,ok=navigate(env,obs,sw)
          16 +        if not ok: print(seed,name,'nav fail'); continue
          17 +        dw=rot(pose[2])@np.array(dirn,float)
          18 +        c=None
          19 +        for k in range(300):
          20 +            prev=obs[16:18].copy()
          21 +            obs,*_=env.step(dw*0.002)
          22 +            if np.abs(obs[0:3]-pose).max()>1e-7:
          23 +                c=to_local(pose,prev); c2=to_local(pose,obs[16:18]); break
          24 +        if c is None: print(seed,name,'no contact'); continue
          25 +        print(seed,name,'w=%.4f Lh=%.4f Lv=%.4f'%(w,Lh,Lv),'contact local prev',c,'after',c2)
          26 +        res.append((seed,name,w,Lh,Lv,*c,*c2))
          27 +np.save('geom_res.npy',np.array([r[2:] for r in res]))
          28 +import json; json.dump([list(map(lambda x: x if isinstance(x,str) else float(x),r)) for r in res],open('geom_res.json','w'))
          29 +env.close()
diff --git a/plib.py b/plib.py
new file mode 100644
index 0000000..5bcd2d8
--- /dev/null
+++ b/plib.py
@@ -0,0 +1,68 @@
           1 +import numpy as np, heapq
           2 +from env_client import make_env
           3 +M=0.0499
           4 +R=0.1
           5 +def rot(t): c,s=np.cos(t),np.sin(t); return np.array([[c,-s],[s,c]])
           6 +def t_polys_local(w,Lh,Lv,stem_end=None):
           7 +    # hypothesis: bar y in [-w/2,w/2], stem y in [stem_end,-w/2]
           8 +    if stem_end is None: stem_end=-Lv
           9 +    bar=np.array([[-Lh/2,-w/2],[Lh/2,-w/2],[Lh/2,w/2],[-Lh/2,w/2]])
          10 +    stem=np.array([[-w/2,stem_end],[w/2,stem_end],[w/2,-w/2],[-w/2,-w/2]])
          11 +    return [bar,stem]
          12 +def to_world(pose,P): return P@rot(pose[2]).T+pose[:2]
          13 +def to_local(pose,p): return (np.asarray(p)-pose[:2])@rot(pose[2])
          14 +def seg_dist(p,a,b):
          15 +    ab=b-a; t=np.clip(np.dot(p-a,ab)/np.dot(ab,ab),0,1); return np.linalg.norm(p-a-t*ab)
          16 +def poly_dist(p,P):
          17 +    # signed-ish: 0 if inside
          18 +    n=len(P); d=min(seg_dist(p,P[i],P[(i+1)%n]) for i in range(n))
          19 +    inside=all(np.cross(P[(i+1)%n]-P[i],p-P[i])>=0 for i in range(n))
          20 +    return 0.0 if inside else d
          21 +def block_dist(obs,p,stem_end=None,margin_local=0.0):
          22 +    pose=obs[0:3]; w,Lh,Lv=obs[12],obs[13],obs[14]
          23 +    pl=to_local(pose,p)
          24 +    return min(poly_dist(pl,P) for P in t_polys_local(w,Lh,Lv,stem_end))
          25 +def plan(obs,goal,clear=0.2,h=0.05,lo=0.13,hi=4.87):
          26 +    # A* on grid avoiding block by clearance (robot center distance to polygon)
          27 +    start=obs[16:18].copy(); goal=np.asarray(goal,float)
          28 +    xs=np.arange(lo,hi+1e-9,h); n=len(xs)
          29 +    free=np.ones((n,n),bool)
          30 +    for i in range(n):
          31 +        for j in range(n):
          32 +            free[i,j]=block_dist(obs,np.array([xs[i],xs[j]]))>clear
          33 +    def idx(p): return (int(np.clip(round((p[0]-lo)/h),0,n-1)),int(np.clip(round((p[1]-lo)/h),0,n-1)))
          34 +    s,g=idx(start),idx(goal)
          35 +    free[s]=True; free[g]=True
          36 +    pq=[(0,s)]; came={s:None}; cost={s:0}
          37 +    while pq:
          38 +        _,c=heapq.heappop(pq)
          39 +        if c==g: break
          40 +        for di in (-1,0,1):
          41 +            for dj in (-1,0,1):
          42 +                if di==dj==0: continue
          43 +                nb=(c[0]+di,c[1]+dj)
          44 +                if not(0<=nb[0]<n and 0<=nb[1]<n) or not free[nb]: continue
          45 +                nc=cost[c]+np.hypot(di,dj)
          46 +                if nb not in cost or nc<cost[nb]:
          47 +                    cost[nb]=nc; came[nb]=c
          48 +                    heapq.heappush(pq,(nc+np.hypot(nb[0]-g[0],nb[1]-g[1]),nb))
          49 +    if g not in came: return None
          50 +    path=[]; c=g
          51 +    while c is not None: path.append(np.array([xs[c[0]],xs[c[1]]])); c=came[c]
          52 +    path=path[::-1][1:]+[goal]
          53 +    return path
          54 +def goto(env,obs,pt,max_step=M):
          55 +    for _ in range(400):
          56 +        d=pt-obs[16:18]
          57 +        if np.linalg.norm(d)<1e-6: break
          58 +        a=d if np.max(np.abs(d))<=max_step else d/np.max(np.abs(d))*max_step
          59 +        obs,*_=env.step(a)
          60 +    return obs
          61 +def navigate(env,obs,goal,clear=0.2):
          62 +    path=plan(obs,goal,clear)
          63 +    if path is None: return obs,False
          64 +    b0=obs[0:3].copy()
          65 +    for wp in path:
          66 +        obs=goto(env,obs,wp)
          67 +    moved=np.abs(obs[0:3]-b0).max()>1e-6
          68 +    return obs,(not moved) and np.linalg.norm(obs[16:18]-goal)<1e-3
diff --git a/probe.py b/probe.py
new file mode 100644
index 0000000..9fc9931
--- /dev/null
+++ b/probe.py
@@ -0,0 +1,8 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=3, suppress=True, linewidth=200)
           4 +env = make_env()
           5 +for s in range(5):
           6 +    obs,_ = env.reset(seed=s)
           7 +    print(s, obs[[0,1,2,16,17,29,30,31]], obs[12:16], obs[28], obs[41:45])
           8 +env.close()
diff --git a/probe2.py b/probe2.py
new file mode 100644
index 0000000..6a086a8
--- /dev/null
+++ b/probe2.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=3, suppress=True, linewidth=200)
           4 +env = make_env()
           5 +obs,_ = env.reset(seed=1)
           6 +print(obs[[0,1,2,16,17]])
           7 +# move robot in straight line towards the block origin and keep going 
           8 +t=0
           9 +for i in range(80):
          10 +    d = obs[0:2]-obs[16:18]
          11 +    a = np.clip(d/np.linalg.norm(d)*0.05, -0.05,0.05) if i<40 else np.zeros(2)
          12 +    obs,r,te,tr,_ = env.step(a)
          13 +    print(i, a, obs[[0,1,2,3,4,5,16,17,19,20]], r)
          14 +env.close()
diff --git a/probe3.py b/probe3.py
new file mode 100644
index 0000000..a04c08c
--- /dev/null
+++ b/probe3.py
@@ -0,0 +1,6 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs,_ = env.reset(seed=0)
           5 +o=obs.copy(); o[0]=2.5;o[1]=2.5;o[2]=0.0; o[16]=2.5;o[17]=2.5; o[29]=1;o[30]=1;o[31]=0.5
           6 +print(o.tolist())
diff --git a/probe4.py b/probe4.py
new file mode 100644
index 0000000..c691198
--- /dev/null
+++ b/probe4.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=5, suppress=True, linewidth=200)
           4 +env = make_env()
           5 +M=0.0499
           6 +obs,_ = env.reset(seed=3)
           7 +for i in range(6):
           8 +    a=np.array([0.0,-M]) if i<3 else np.array([0.02,0.0])
           9 +    p=obs[16:18].copy(); obs,*_=env.step(a); print('d-a', obs[16:18]-p-a, obs[18:21])
          10 +for d,a in [('down',[0,-M]),('left',[-M,0])]:
          11 +    for i in range(40):
          12 +        obs,*_=env.step(np.array(a))
          13 +    print(d, obs[16:18], obs[18:21])
          14 +for i in range(90):
          15 +    obs,*_=env.step(np.array([0,M]))
          16 +print('up', obs[16:18], obs[[0,1,2]])
          17 +env.close()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..0268fd7
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,35 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +from multiprocessing import Pool
           6 +
           7 +def run(seed):
           8 +    env = make_env()
           9 +    obs, info = env.reset(seed=seed)
          10 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          11 +    ap.reset(obs, info)
          12 +    t0 = time.time()
          13 +    steps = 0
          14 +    done = False
          15 +    for steps in range(1, env.max_steps + 1):
          16 +        a = ap.get_action(obs)
          17 +        obs, r, term, trunc, _ = env.step(np.clip(a, -0.05, 0.05))
          18 +        if term:
          19 +            done = True
          20 +            break
          21 +        if trunc:
          22 +            break
          23 +    env.close()
          24 +    g = obs[29:32]
          25 +    err = (abs(obs[0]-g[0]), abs(obs[1]-g[1]), abs((obs[2]-g[2]+np.pi)%(2*np.pi)-np.pi))
          26 +    return seed, done, steps, time.time()-t0, err
          27 +
          28 +if __name__ == "__main__":
          29 +    a = int(sys.argv[1]) if len(sys.argv) > 1 else 0
          30 +    b = int(sys.argv[2]) if len(sys.argv) > 2 else 10
          31 +    with Pool(10) as p:
          32 +        res = p.map(run, range(a, b))
          33 +    for r in res:
          34 +        print(r[0], r[1], r[2], "%.1fs" % r[3], np.round(r[4], 3))
          35 +    print("solved", sum(r[1] for r in res), "/", len(res), "mean steps", np.mean([r[2] for r in res]))
```

</details>

<a id="C003"></a>
### C003 · Fix T geometry (origin at bar top-center), cap action at 0.049

Commit `7d6d1933d28b51e74bb1d25420abb4721de4fa44`; parents: 3ed9cea8bdb73ce4171f7c10e60ed91f65765d48. Recorded author date: 2026-09-30T17:27:05+02:00.

File roles (automatic): policy.

- [E0296](01_timeline.md#E0296): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_7d6d193_approach.py) · [Exact all-file diff](evidence/diffs/C003_7d6d193.diff)

[Previous saved controller snapshot](evidence/versions/C002_3ed9cea_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4420811..07b2344 100644
--- a/approach.py
+++ b/approach.py
@@ -7,7 +7,7 @@ import numpy as np
    7      7  R_ROBOT = 0.1
    8      8  WALL_LO = 0.0
    9      9  WALL_HI = 5.0
   10        -MAXD = 0.05
          10 +MAXD = 0.049
   11     11  
   12     12  
   13     13  def wrap(a):
@@ -18,14 +18,14 @@ def local_poly(w, lh, lv):
   18     18      """T polygon in the block frame, CCW order."""
   19     19      a, h = lh / 2.0, w / 2.0
   20     20      return np.array([
   21        -        [-a, h], [-a, -h], [-h, -h], [-h, -lv], [h, -lv], [h, -h], [a, -h], [a, h],
          21 +        [-a, 0], [-a, -w], [-h, -w], [-h, -w - lv], [h, -w - lv], [h, -w], [a, -w], [a, 0],
   22     22      ])
   23     23  
   24     24  
   25     25  def rects_local(w, lh, lv):
   26     26      a, h = lh / 2.0, w / 2.0
   27     27      # (xmin, xmax, ymin, ymax)
   28        -    return [(-a, a, -h, h), (-h, h, -lv, -h)]
          28 +    return [(-a, a, -w, 0.0), (-h, h, -w - lv, -w)]
   29     29  
   30     30  
   31     31  def to_world(pts, pose):
@@ -65,14 +65,13 @@ class TModel:
   65     65          self.poly = local_poly(w, lh, lv)
   66     66          # geometric centroid
   67     67          a1 = lh * w
   68        -        a2 = (lv - w / 2) * w
   69        -        cy = (a2 * (-(lv + w / 2) / 2)) / (a1 + a2)
          68 +        a2 = lv * w
          69 +        cy = (a1 * (-w / 2) + a2 * (-w - lv / 2)) / (a1 + a2)
   70     70          self.com = np.array([0.0, cy if com[1] is None else com[1]])
   71     71          if rho2 is None:
   72     72              # radius of gyration^2 about com (uniform density)
   73        -            i1 = a1 * (lh ** 2 + w ** 2) / 12 + a1 * (0 - self.com[1]) ** 2
   74        -            l2 = lv - w / 2
   75        -            i2 = a2 * (l2 ** 2 + w ** 2) / 12 + a2 * (-(lv + w / 2) / 2 - self.com[1]) ** 2
          73 +            i1 = a1 * (lh ** 2 + w ** 2) / 12 + a1 * (-w / 2 - self.com[1]) ** 2
          74 +            i2 = a2 * (lv ** 2 + w ** 2) / 12 + a2 * (-w - lv / 2 - self.com[1]) ** 2
   76     75              rho2 = (i1 + i2) / (a1 + a2)
   77     76          self.rho2 = rho2
   78     77          self.mu = mu
@@ -253,10 +252,11 @@ class GeneratedApproach:
  253    252          a, h = self.lh / 2, self.w / 2
  254    253          e = infl + 0.05
  255    254          lv = self.lv
         255 +        w = self.w
  256    256          nodes_local = np.array([
  257        -            [-a - e, h + e], [a + e, h + e], [a + e, -h - e], [-a - e, -h - e],
  258        -            [h + e, -h - e], [-h - e, -h - e], [h + e, -lv - e], [-h - e, -lv - e],
  259        -            [0, h + e], [0, -lv - e],
         257 +            [-a - e, e], [a + e, e], [a + e, -w - e], [-a - e, -w - e],
         258 +            [h + e, -w - e], [-h - e, -w - e], [h + e, -w - lv - e], [-h - e, -w - lv - e],
         259 +            [0, e], [0, -w - lv - e],
  260    260          ])
  261    261          nodes = list(to_world(nodes_local, pose))
  262    262          nodes = [p for p in nodes if np.all(p > WALL_LO + R_ROBOT) and np.all(p < WALL_HI - R_ROBOT)]
```

</details>

<a id="C004"></a>
### C004 · Staging point for approach, filter infeasible push candidates

Commit `617862708146b5a442cdd80d6d2a6cf1283cb268`; parents: 7d6d1933d28b51e74bb1d25420abb4721de4fa44. Recorded author date: 2026-09-30T17:30:38+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0354](01_timeline.md#E0354): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_6178627_approach.py) · [Exact all-file diff](evidence/diffs/C004_6178627.diff)

[Previous saved controller snapshot](evidence/versions/C003_7d6d193_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 07b2344..227a351 100644
--- a/approach.py
+++ b/approach.py
@@ -212,7 +212,13 @@ class GeneratedApproach:
  212    212          N = len(sw)
  213    213          # filter starts that are outside walls
  214    214          ok = np.all((sw > WALL_LO + R_ROBOT + 0.01) & (sw < WALL_HI - R_ROBOT - 0.01), 1)
  215        -        sw, dw = sw[ok], dw[ok]
         215 +        # start point must not overlap block, staging point must be clear
         216 +        pre = sw - dw * 0.12
         217 +        ds = dist_to_T_local(to_local(sw, pose), self.model.rects)
         218 +        dp = dist_to_T_local(to_local(pre, pose), self.model.rects)
         219 +        ok &= (ds > R_ROBOT + 0.005) & (dp > R_ROBOT + 0.035)
         220 +        if np.any(ok):
         221 +            sw, dw = sw[ok], dw[ok]
  216    222          N = len(sw)
  217    223          poses = np.repeat(pose[None], N, 0)
  218    224          rob = sw.copy()
@@ -314,7 +320,7 @@ class GeneratedApproach:
  314    320                  st, d, k, sc, c0 = self.plan_push(pose, robot)
  315    321                  self.push = (st, d)
  316    322                  self.push_left = k + 3
  317        -                self.path = self.nav_path(robot, st, pose)
         323 +                self.path = self.nav_path(robot, st - d * 0.12, pose) + [st]
  318    324                  self.plan_pose = pose.copy()
  319    325                  self.mode = "nav"
  320    326              if self.mode == "nav":
diff --git a/test_approach.py b/test_approach.py
index 0268fd7..6a75de4 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -13,7 +13,10 @@ def run(seed):
   13     13      steps = 0
   14     14      done = False
   15     15      for steps in range(1, env.max_steps + 1):
   16        -        a = ap.get_action(obs)
          16 +        try:
          17 +            a = ap.get_action(obs)
          18 +        except Exception as e:
          19 +            print("EXC", seed, steps, obs[[0,1,2,16,17]], repr(e)); break
   17     20          obs, r, term, trunc, _ = env.step(np.clip(a, -0.05, 0.05))
   18     21          if term:
   19     22              done = True
```

</details>

<a id="C005"></a>
### C005 · Wall filter for staging points, stuck detection

Commit `0d1ab3f1a54c409aaddb1bb0162e55e1b5beb728`; parents: 617862708146b5a442cdd80d6d2a6cf1283cb268. Recorded author date: 2026-09-30T17:31:07+02:00.

File roles (automatic): policy.

- [E0379](01_timeline.md#E0379): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_0d1ab3f_approach.py) · [Exact all-file diff](evidence/diffs/C005_0d1ab3f.diff)

[Previous saved controller snapshot](evidence/versions/C004_6178627_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 227a351..9434ee4 100644
--- a/approach.py
+++ b/approach.py
@@ -169,6 +169,8 @@ class GeneratedApproach:
  169    169          self.push = None
  170    170          self.push_left = 0
  171    171          self.stall = 0
         172 +        self.last_cmd = None
         173 +        self.last_robot = None
  172    174  
  173    175      # ------------------------------------------------------------------
  174    176      def cost(self, pose):
@@ -217,6 +219,7 @@ class GeneratedApproach:
  217    219          ds = dist_to_T_local(to_local(sw, pose), self.model.rects)
  218    220          dp = dist_to_T_local(to_local(pre, pose), self.model.rects)
  219    221          ok &= (ds > R_ROBOT + 0.005) & (dp > R_ROBOT + 0.035)
         222 +        ok &= np.all((pre > WALL_LO + R_ROBOT + 0.02) & (pre < WALL_HI - R_ROBOT - 0.02), 1)
  220    223          if np.any(ok):
  221    224              sw, dw = sw[ok], dw[ok]
  222    225          N = len(sw)
@@ -265,7 +268,7 @@ class GeneratedApproach:
  265    268              [0, e], [0, -w - lv - e],
  266    269          ])
  267    270          nodes = list(to_world(nodes_local, pose))
  268        -        nodes = [p for p in nodes if np.all(p > WALL_LO + R_ROBOT) and np.all(p < WALL_HI - R_ROBOT)]
         271 +        nodes = [p for p in nodes if np.all(p > WALL_LO + R_ROBOT + 0.01) and np.all(p < WALL_HI - R_ROBOT - 0.01)]
  269    272          pts = [np.asarray(robot)] + nodes + [np.asarray(target)]
  270    273          n = len(pts)
  271    274          dist = [np.inf] * n
@@ -315,6 +318,22 @@ class GeneratedApproach:
  315    318          robot = s[16:18].copy()
  316    319          if self.model is None:
  317    320              self.reset(state, {})
         321 +        if self.last_cmd is not None and self.mode == "nav":
         322 +            moved = np.linalg.norm(robot - self.last_robot)
         323 +            if moved < 0.3 * np.linalg.norm(self.last_cmd) and np.linalg.norm(self.last_cmd) > 1e-3:
         324 +                self.stall += 1
         325 +            else:
         326 +                self.stall = 0
         327 +            if self.stall >= 3:
         328 +                self.stall = 0
         329 +                self.mode = "plan"
         330 +        self.last_robot = robot
         331 +        a = self._act(pose, robot)
         332 +        a = np.clip(np.asarray(a, float), -MAXD, MAXD)
         333 +        self.last_cmd = a
         334 +        return a
         335 +
         336 +    def _act(self, pose, robot):
  318    337          for _ in range(4):
  319    338              if self.mode == "plan":
  320    339                  st, d, k, sc, c0 = self.plan_push(pose, robot)
```

</details>

<a id="C006"></a>
### C006 · Use fitted vectorized push model in planner

Commit `fa5ec4415fd4fe2e309a6a301d3e5d557d4c1faf`; parents: 0d1ab3f1a54c409aaddb1bb0162e55e1b5beb728. Recorded author date: 2026-09-30T17:32:08+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0392](01_timeline.md#E0392): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_fa5ec44_approach.py) · [Exact all-file diff](evidence/diffs/C006_fa5ec44.diff)

[Previous saved controller snapshot](evidence/versions/C005_0d1ab3f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9434ee4..0304083 100644
--- a/approach.py
+++ b/approach.py
@@ -4,6 +4,8 @@ import math
    4      4  
    5      5  import numpy as np
    6      6  
           7 +from model_v import VModel
           8 +
    7      9  R_ROBOT = 0.1
    8     10  WALL_LO = 0.0
    9     11  WALL_HI = 5.0
@@ -163,6 +165,7 @@ class GeneratedApproach:
  163    165          s = np.asarray(state, dtype=float)
  164    166          self.w, self.lh, self.lv = s[12], s[13], s[14]
  165    167          self.model = TModel(self.w, self.lh, self.lv)
         168 +        self.sim = VModel(self.w, self.lh, self.lv)
  166    169          self.goal = s[29:32].copy()
  167    170          self.mode = "plan"
  168    171          self.path = []
@@ -234,7 +237,7 @@ class GeneratedApproach:
  234    237          bestscore = np.full(N, np.inf)
  235    238          bestk = np.zeros(N, int)
  236    239          for k in range(1, H + 1):
  237        -            cur, rob = self.model.step(cur, rob, dw * steplen)
         240 +            cur, rob = self.sim.step(cur, rob, dw * steplen)
  238    241              cst = self.cost(cur)
  239    242              # score: resulting cost + time penalty
  240    243              score = cst + 0.004 * (k + travel)
diff --git a/model_v.py b/model_v.py
new file mode 100644
index 0000000..b2e5d32
--- /dev/null
+++ b/model_v.py
@@ -0,0 +1,104 @@
           1 +"""Vectorized quasi-static push model (fitted on env data)."""
           2 +import numpy as np
           3 +
           4 +R_ROBOT = 0.1
           5 +
           6 +
           7 +class VModel:
           8 +    def __init__(self, w, lh, lv, mu=0.99, nsub=4, reff=0.1015, beta=0.22):
           9 +        self.w, self.lh, self.lv = w, lh, lv
          10 +        a1, a2 = lh * w, lv * w
          11 +        y1, y2 = -w / 2, -w - lv / 2
          12 +        cy = (a1 * y1 + a2 * y2) / (a1 + a2)
          13 +        I = a1 * ((lh ** 2 + w ** 2) / 12 + (y1 - cy) ** 2) + a2 * ((w ** 2 + lv ** 2) / 12 + (y2 - cy) ** 2)
          14 +        self.com = np.array([0.0, cy])
          15 +        self.k2 = I / (a1 + a2)
          16 +        self.rects = [(-lh / 2, lh / 2, -w, 0.0), (-w / 2, w / 2, -w - lv, -w)]
          17 +        self.mu, self.nsub, self.reff, self.beta = mu, nsub, reff, beta
          18 +
          19 +    def step(self, pose, rob, act):
          20 +        pose = np.array(pose, float, ndmin=2)
          21 +        rob = np.array(rob, float, ndmin=2)
          22 +        a = np.array(act, float, ndmin=2)
          23 +        N = len(pose)
          24 +        if len(rob) != N:
          25 +            rob = np.repeat(rob, N, 0)
          26 +        if len(a) != N:
          27 +            a = np.repeat(a, N, 0)
          28 +        cl = self.com
          29 +        k2, mu, reff, beta = self.k2, self.mu, self.reff, self.beta
          30 +        lo, hi = R_ROBOT, 5.0 - R_ROBOT
          31 +        for _ in range(self.nsub):
          32 +            new = np.clip(rob + a / self.nsub, lo, hi)
          33 +            da = new - rob
          34 +            rob = new
          35 +            for (x0, x1, y0, y1) in self.rects:
          36 +                c, s = np.cos(pose[:, 2]), np.sin(pose[:, 2])
          37 +                dx = rob[:, 0] - pose[:, 0]
          38 +                dy = rob[:, 1] - pose[:, 1]
          39 +                plx = c * dx + s * dy
          40 +                ply = -s * dx + c * dy
          41 +                qx = np.clip(plx, x0, x1)
          42 +                qy = np.clip(ply, y0, y1)
          43 +                vx, vy = plx - qx, ply - qy
          44 +                d = np.hypot(vx, vy)
          45 +                act_m = d < reff
          46 +                if not np.any(act_m):
          47 +                    continue
          48 +                dsafe = np.where(d > 1e-9, d, 1.0)
          49 +                nx, ny = vx / dsafe, vy / dsafe
          50 +                # inside handling
          51 +                ins = d <= 1e-9
          52 +                if np.any(ins):
          53 +                    cand = np.stack([plx - x0, x1 - plx, ply - y0, y1 - ply], 1)
          54 +                    j = np.argmin(cand, 1)
          55 +                    dd = cand[np.arange(N), j]
          56 +                    nxs = np.array([-1.0, 1.0, 0.0, 0.0])[j]
          57 +                    nys = np.array([0.0, 0.0, -1.0, 1.0])[j]
          58 +                    nx = np.where(ins, nxs, nx)
          59 +                    ny = np.where(ins, nys, ny)
          60 +                    qx = np.where(ins, plx + nxs * dd, qx)
          61 +                    qy = np.where(ins, ply + nys * dd, qy)
          62 +                    d = np.where(ins, -dd, d)
          63 +                # world normal
          64 +                nwx = c * nx - s * ny
          65 +                nwy = s * nx + c * ny
          66 +                delta = reff + beta * np.maximum(0.0, -(a[:, 0] * nwx + a[:, 1] * nwy)) - d
          67 +                twx, twy = -nwy, nwx
          68 +                # contact point rel com (world)
          69 +                rlx, rly = qx - cl[0], qy - cl[1]
          70 +                rx = c * rlx - s * rly
          71 +                ry = s * rlx + c * rly
          72 +                rpx, rpy = -ry, rx
          73 +                # K = I + rp rp^T / k2 ; solve K P = want
          74 +                K11 = 1 + rpx * rpx / k2
          75 +                K12 = rpx * rpy / k2
          76 +                K22 = 1 + rpy * rpy / k2
          77 +                dt = da[:, 0] * twx + da[:, 1] * twy
          78 +                wx = -nwx * delta + twx * dt
          79 +                wy = -nwy * delta + twy * dt
          80 +                det = K11 * K22 - K12 * K12
          81 +                Px = (K22 * wx - K12 * wy) / det
          82 +                Py = (-K12 * wx + K11 * wy) / det
          83 +                Pn = -(Px * nwx + Py * nwy)
          84 +                Pt = Px * twx + Py * twy
          85 +                slide = np.abs(Pt) > mu * Pn
          86 +                sg = np.sign(Pt)
          87 +                dvx = -nwx + mu * sg * twx
          88 +                dvy = -nwy + mu * sg * twy
          89 +                Kdx = K11 * dvx + K12 * dvy
          90 +                Kdy = K12 * dvx + K22 * dvy
          91 +                den = -nwx * Kdx - nwy * Kdy
          92 +                Pn2 = delta / np.where(np.abs(den) > 1e-12, den, 1e-12)
          93 +                Px = np.where(slide, Pn2 * dvx, Px)
          94 +                Py = np.where(slide, Pn2 * dvy, Py)
          95 +                ok = act_m & (Pn > 0)
          96 +                Px = np.where(ok, Px, 0.0)
          97 +                Py = np.where(ok, Py, 0.0)
          98 +                dth = (rx * Py - ry * Px) / k2
          99 +                comx = pose[:, 0] + c * cl[0] - s * cl[1] + Px
         100 +                comy = pose[:, 1] + s * cl[0] + c * cl[1] + Py
         101 +                th = pose[:, 2] + dth
         102 +                c2, s2 = np.cos(th), np.sin(th)
         103 +                pose = np.stack([comx - (c2 * cl[0] - s2 * cl[1]), comy - (s2 * cl[0] + c2 * cl[1]), th], 1)
         104 +        return pose, rob
```

</details>

<a id="C007"></a>
### C007 · Step-based planner score, goal detection, in-contact candidates, speeds, periodic replanning

Commit `97868d94ade0ef93d0b673758cb92b99adf43812`; parents: fa5ec4415fd4fe2e309a6a301d3e5d557d4c1faf. Recorded author date: 2026-09-30T17:33:11+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0406](01_timeline.md#E0406): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_97868d9_approach.py) · [Exact all-file diff](evidence/diffs/C007_97868d9.diff)

[Previous saved controller snapshot](evidence/versions/C006_fa5ec44_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0304083..fa730d8 100644
--- a/approach.py
+++ b/approach.py
@@ -158,6 +158,9 @@ class TModel:
  158    158  class GeneratedApproach:
  159    159      def __init__(self, action_space, observation_space, primitives):
  160    160          self.action_space = action_space
         161 +        self.alpha = 50.0
         162 +        self.H = 40
         163 +        self.replan_every = 8
  161    164          self.model = None
  162    165  
  163    166      # ------------------------------------------------------------------
@@ -214,38 +217,67 @@ class GeneratedApproach:
  214    217  
  215    218      def plan_push(self, pose, robot):
  216    219          sw, dw = self.candidates(pose)
  217        -        N = len(sw)
  218        -        # filter starts that are outside walls
         220 +        # extra candidates: push from current robot position if close to block
         221 +        dr = dist_to_T_local(to_local(robot[None], pose), self.model.rects)[0]
         222 +        if dr < R_ROBOT + 0.06:
         223 +            angs = np.linspace(0, 2 * np.pi, 24, endpoint=False)
         224 +            sw = np.vstack([sw, np.repeat(robot[None], 24, 0)])
         225 +            dw = np.vstack([dw, np.stack([np.cos(angs), np.sin(angs)], 1)])
         226 +            here = np.zeros(len(sw), bool)
         227 +            here[-24:] = True
         228 +        else:
         229 +            here = np.zeros(len(sw), bool)
  219    230          ok = np.all((sw > WALL_LO + R_ROBOT + 0.01) & (sw < WALL_HI - R_ROBOT - 0.01), 1)
  220        -        # start point must not overlap block, staging point must be clear
  221    231          pre = sw - dw * 0.12
  222    232          ds = dist_to_T_local(to_local(sw, pose), self.model.rects)
  223    233          dp = dist_to_T_local(to_local(pre, pose), self.model.rects)
  224    234          ok &= (ds > R_ROBOT + 0.005) & (dp > R_ROBOT + 0.035)
  225    235          ok &= np.all((pre > WALL_LO + R_ROBOT + 0.02) & (pre < WALL_HI - R_ROBOT - 0.02), 1)
  226        -        if np.any(ok):
  227        -            sw, dw = sw[ok], dw[ok]
  228        -        N = len(sw)
  229        -        poses = np.repeat(pose[None], N, 0)
  230        -        rob = sw.copy()
         236 +        ok |= here
         237 +        sw, dw, pre, here = sw[ok], dw[ok], pre[ok], here[ok]
  231    238          c0 = self.cost(pose)[0]
  232        -        best = (np.inf, None)
  233        -        H = 40
  234        -        steplen = MAXD
  235        -        travel = np.hypot(*(sw - robot).T) / MAXD
  236        -        cur = poses
         239 +        # speeds
         240 +        speeds = [MAXD] if c0 > 0.35 else [MAXD, 0.02]
         241 +        SW = np.vstack([sw] * len(speeds))
         242 +        DW = np.vstack([dw] * len(speeds))
         243 +        PRE = np.vstack([pre] * len(speeds))
         244 +        HERE = np.concatenate([here] * len(speeds))
         245 +        SP = np.repeat(np.array(speeds), len(sw))
         246 +        N = len(SW)
         247 +        # travel estimate
         248 +        travel = np.where(HERE, 0.0, self.travel_est(robot, PRE, pose) + 0.12 / MAXD)
         249 +        cur = np.repeat(pose[None], N, 0)
         250 +        rob = SW.copy()
  237    251          bestscore = np.full(N, np.inf)
  238    252          bestk = np.zeros(N, int)
         253 +        H = self.H
  239    254          for k in range(1, H + 1):
  240        -            cur, rob = self.sim.step(cur, rob, dw * steplen)
         255 +            cur, rob = self.sim.step(cur, rob, DW * SP[:, None])
  241    256              cst = self.cost(cur)
  242        -            # score: resulting cost + time penalty
  243        -            score = cst + 0.004 * (k + travel)
         257 +            done = self.in_goal(cur, 0.75)
         258 +            score = np.where(done, 0.0, self.alpha * cst) + k + travel
  244    259              m = score < bestscore
  245    260              bestscore[m] = score[m]
  246    261              bestk[m] = k
  247    262          i = int(np.argmin(bestscore))
  248        -        return sw[i], dw[i], bestk[i], bestscore[i], c0
         263 +        return SW[i], DW[i] * SP[i], bestk[i], bestscore[i], c0, HERE[i]
         264 +
         265 +    def in_goal(self, poses, frac=1.0):
         266 +        dp = np.abs(poses[:, :2] - self.goal[:2])
         267 +        da = np.abs(wrap_arr(poses[:, 2] - self.goal[2]))
         268 +        return (dp[:, 0] < 0.03 * frac) & (dp[:, 1] < 0.03 * frac) & (da < math.radians(8) * frac)
         269 +
         270 +    def travel_est(self, robot, pts, pose):
         271 +        """Approximate travel steps from robot to each pt, detouring around block."""
         272 +        direct = np.hypot(*(pts - robot).T)
         273 +        ts = np.linspace(0, 1, 12)
         274 +        seg = robot[None, None, :] + ts[None, :, None] * (pts - robot)[:, None, :]
         275 +        flat = seg.reshape(-1, 2)
         276 +        dd = dist_to_T_local(to_local(flat, pose), self.model.rects).reshape(len(pts), -1)
         277 +        blocked = dd.min(1) < R_ROBOT + 0.03
         278 +        cen = to_world(np.array([[0.0, -(self.w + self.lv) / 2]]), pose)[0]
         279 +        det = (np.hypot(*(robot - cen)) + np.hypot(*(pts - cen).T)) * 1.25
         280 +        return np.where(blocked, np.maximum(det, direct), direct) / MAXD
  249    281  
  250    282      # ------------------------------------------------------------------
  251    283      def nav_path(self, robot, target, pose):
@@ -339,10 +371,14 @@ class GeneratedApproach:
  339    371      def _act(self, pose, robot):
  340    372          for _ in range(4):
  341    373              if self.mode == "plan":
  342        -                st, d, k, sc, c0 = self.plan_push(pose, robot)
         374 +                st, d, k, sc, c0, here = self.plan_push(pose, robot)
  343    375                  self.push = (st, d)
  344        -                self.push_left = k + 3
  345        -                self.path = self.nav_path(robot, st - d * 0.12, pose) + [st]
         376 +                self.push_left = min(k, self.replan_every)
         377 +                dn = d / np.linalg.norm(d)
         378 +                if here:
         379 +                    self.path = []
         380 +                else:
         381 +                    self.path = self.nav_path(robot, st - dn * 0.12, pose) + [st]
  346    382                  self.plan_pose = pose.copy()
  347    383                  self.mode = "nav"
  348    384              if self.mode == "nav":
@@ -364,11 +400,7 @@ class GeneratedApproach:
  364    400                      self.mode = "plan"
  365    401                      continue
  366    402                  self.push_left -= 1
  367        -                d = self.push[1]
  368        -                # slow down near goal
  369        -                c = self.cost(pose)[0]
  370        -                sp = MAXD if c > 0.2 else max(0.01, MAXD * c / 0.2)
  371        -                return d * sp
         403 +                return self.push[1]
  372    404          return np.zeros(2)
  373    405  
  374    406  
diff --git a/cmp_model.py b/cmp_model.py
new file mode 100644
index 0000000..db61209
--- /dev/null
+++ b/cmp_model.py
@@ -0,0 +1,12 @@
           1 +import numpy as np
           2 +from push_model import predict_step, geom_from_obs
           3 +from model_v import VModel
           4 +rng=np.random.default_rng(0)
           5 +g=dict(w=0.13,Lh=1.1,Lv=1.1); m=VModel(0.13,1.1,1.1)
           6 +P=[];Q=[]
           7 +for i in range(500):
           8 +    pose=np.array([2.5,2.5,rng.uniform(-3,3)]); rob=pose[:2]+rng.uniform(-0.8,0.8,2); a=rng.uniform(-0.049,0.049,2)
           9 +    p1,r1=predict_step(pose,rob,a,g); P.append(p1)
          10 +    Q.append((pose,rob,a))
          11 +p2,r2=m.step(np.array([q[0] for q in Q]),np.array([q[1] for q in Q]),np.array([q[2] for q in Q]))
          12 +print(np.abs(np.array(P)-p2).max(0))
diff --git a/col_0.log b/col_0.log
new file mode 100644
index 0000000..b992ae5
--- /dev/null
+++ b/col_0.log
@@ -0,0 +1,25 @@
           1 +navfail 100 0.5812486534949994 0.0
           2 +navfail 100 0.8260996124397624 0.0
           3 +100 84
           4 +navfail 101 0.4125059289850408 0.0
           5 +101 182
           6 +102 294
           7 +wall 103
           8 +103 294
           9 +104 406
          10 +navfail 105 0.35173101563142156 0.0
          11 +105 504
          12 +wall 106
          13 +106 504
          14 +navfail 107 0.1849157932959263 0.0
          15 +107 602
          16 +108 714
          17 +109 826
          18 +110 938
          19 +wall 111
          20 +111 952
          21 +wall 112
          22 +112 952
          23 +113 1064
          24 +wall 114
          25 +114 1148
diff --git a/col_1.log b/col_1.log
new file mode 100644
index 0000000..b48adc0
--- /dev/null
+++ b/col_1.log
@@ -0,0 +1,38 @@
           1 +115 112
           2 +wall 116
           3 +116 126
           4 +navfail 117 1.1475651190146916 0.0
           5 +navfail 117 0.4221659168517509 0.0
           6 +117 210
           7 +118 322
           8 +navfail 119 0.8009230698237192 0.0
           9 +wall 119
          10 +119 350
          11 +navfail 120 0.44146092687898025 0.0
          12 +navfail 120 0.5110994394478386 0.0
          13 +120 434
          14 +navfail 121 0.20184872717827138 0.0
          15 +121 532
          16 +navfail 122 0.22226888605768383 0.0
          17 +wall 122
          18 +122 602
          19 +navfail 123 2.543554076247497 0.0
          20 +navfail 123 0.4880511236819359 0.0
          21 +navfail 123 0.48919122114723657 0.0
          22 +wall 123
          23 +123 658
          24 +wall 124
          25 +124 714
          26 +navfail 125 2.772794797365419 0.0
          27 +125 812
          28 +navfail 126 0.5098488783358021 0.0
          29 +126 910
          30 +navfail 127 2.645676784633295 0.0
          31 +navfail 127 0.6436396121497455 0.0
          32 +wall 127
          33 +127 938
          34 +wall 128
          35 +128 938
          36 +navfail 129 2.5889565039174904 0.0
          37 +navfail 129 0.39896365549508395 0.0
          38 +129 1022
diff --git a/col_2.log b/col_2.log
new file mode 100644
index 0000000..f686c01
--- /dev/null
+++ b/col_2.log
@@ -0,0 +1,31 @@
           1 +navfail 130 0.7684981325068745 0.0
           2 +130 98
           3 +wall 131
           4 +131 98
           5 +wall 132
           6 +132 98
           7 +133 210
           8 +navfail 134 1.7010285408355144 0.0
           9 +wall 134
          10 +134 224
          11 +wall 135
          12 +135 308
          13 +navfail 136 2.530304464706826 0.0
          14 +136 406
          15 +navfail 137 0.48880359791056727 0.0
          16 +137 504
          17 +navfail 138 2.6810269391732584 0.0
          18 +navfail 138 2.6752274310495205 0.0
          19 +wall 138
          20 +138 518
          21 +139 630
          22 +navfail 140 0.9574091764623831 0.0
          23 +140 728
          24 +wall 141
          25 +141 826
          26 +wall 142
          27 +142 882
          28 +wall 143
          29 +143 896
          30 +wall 144
          31 +144 994
diff --git a/col_3.log b/col_3.log
new file mode 100644
index 0000000..23d3305
--- /dev/null
+++ b/col_3.log
@@ -0,0 +1,28 @@
           1 +navfail 145 0.9266363970869294 0.0
           2 +wall 145
           3 +145 84
           4 +146 196
           5 +147 308
           6 +wall 148
           7 +148 392
           8 +navfail 149 2.1717531628188653 0.0
           9 +navfail 149 0.27348078805485265 0.0
          10 +149 476
          11 +navfail 150 0.12396852419825222 0.0
          12 +150 574
          13 +navfail 151 0.785037533710175 0.0
          14 +151 672
          15 +wall 152
          16 +152 756
          17 +153 868
          18 +wall 154
          19 +154 868
          20 +wall 155
          21 +155 910
          22 +156 1022
          23 +navfail 157 0.5908641531104925 0.0
          24 +navfail 157 0.5558937147538678 0.0
          25 +157 1106
          26 +158 1218
          27 +wall 159
          28 +159 1274
diff --git a/col_4.log b/col_4.log
new file mode 100644
index 0000000..1da5e19
--- /dev/null
+++ b/col_4.log
@@ -0,0 +1,28 @@
           1 +160 112
           2 +wall 161
           3 +161 196
           4 +162 308
           5 +163 420
           6 +navfail 164 0.41273393996105184 0.0
           7 +164 518
           8 +wall 165
           9 +165 518
          10 +wall 166
          11 +166 532
          12 +wall 167
          13 +167 560
          14 +navfail 168 0.6687350278082417 0.0
          15 +168 658
          16 +169 770
          17 +navfail 170 1.9801773153957831 0.0
          18 +navfail 170 2.2527226459936913 0.0
          19 +170 854
          20 +wall 171
          21 +171 896
          22 +navfail 172 0.7561475776272608 0.0
          23 +172 994
          24 +navfail 173 1.731745438611625 0.0
          25 +navfail 173 1.7423290432203788 0.0
          26 +173 1078
          27 +wall 174
          28 +174 1078
diff --git a/col_5.log b/col_5.log
new file mode 100644
index 0000000..6348572
--- /dev/null
+++ b/col_5.log
@@ -0,0 +1,29 @@
           1 +175 112
           2 +wall 176
           3 +176 168
           4 +wall 177
           5 +177 196
           6 +navfail 178 0.655276635885516 0.0
           7 +navfail 178 0.8000479293263496 0.0
           8 +178 280
           9 +wall 179
          10 +179 294
          11 +wall 180
          12 +180 294
          13 +181 406
          14 +navfail 182 1.3021001737497 0.0
          15 +wall 182
          16 +182 490
          17 +navfail 183 0.8530726565273796 0.0
          18 +183 588
          19 +navfail 184 0.2892128213053389 0.0
          20 +184 686
          21 +wall 185
          22 +185 756
          23 +wall 186
          24 +186 812
          25 +navfail 187 0.5531063377104662 0.0
          26 +187 910
          27 +188 1022
          28 +navfail 189 0.5088085676215689 0.0
          29 +189 1120
diff --git a/col_6.log b/col_6.log
new file mode 100644
index 0000000..0451d50
--- /dev/null
+++ b/col_6.log
@@ -0,0 +1,29 @@
           1 +navfail 190 0.7071264522101917 0.0
           2 +190 98
           3 +navfail 191 0.7448537136233812 0.0
           4 +191 196
           5 +wall 192
           6 +192 224
           7 +wall 193
           8 +193 224
           9 +navfail 194 0.6989158382540994 0.0
          10 +194 322
          11 +navfail 195 1.7790465773785253 0.0
          12 +navfail 195 2.046819900411149 0.0
          13 +wall 195
          14 +195 336
          15 +navfail 196 1.132132942169156 0.0
          16 +196 434
          17 +197 546
          18 +198 658
          19 +navfail 199 1.2705206958708566 0.0
          20 +199 756
          21 +200 868
          22 +navfail 201 0.9475970762943132 0.0
          23 +201 966
          24 +wall 202
          25 +202 980
          26 +navfail 203 0.5222617492074764 0.0
          27 +203 1078
          28 +wall 204
          29 +204 1078
diff --git a/col_7.log b/col_7.log
new file mode 100644
index 0000000..7c8ae93
--- /dev/null
+++ b/col_7.log
@@ -0,0 +1,33 @@
           1 +205 112
           2 +wall 206
           3 +206 112
           4 +navfail 207 0.21234574365619477 0.0
           5 +navfail 207 0.42752221094340304 0.0
           6 +navfail 207 0.9578003135895781 0.0
           7 +navfail 207 0.7535009862496855 0.0
           8 +207 168
           9 +wall 208
          10 +208 224
          11 +navfail 209 0.49679942946845557 0.0
          12 +navfail 209 0.5096468444654819 0.0
          13 +navfail 209 0.5220134861817278 0.0
          14 +209 294
          15 +wall 210
          16 +210 294
          17 +navfail 211 0.1556071448495736 0.0
          18 +211 392
          19 +navfail 212 0.22485633576501715 0.0
          20 +212 490
          21 +navfail 213 0.7724978177966451 0.0
          22 +213 588
          23 +wall 214
          24 +214 588
          25 +navfail 215 2.4230063364031142 0.0
          26 +215 686
          27 +wall 216
          28 +216 784
          29 +217 896
          30 +navfail 218 1.0059030241486275 0.0
          31 +218 994
          32 +navfail 219 1.6751581782433222 0.0
          33 +219 1092
diff --git a/collect.py b/collect.py
new file mode 100644
index 0000000..6a35cbc
--- /dev/null
+++ b/collect.py
@@ -0,0 +1,34 @@
           1 +import sys
           2 +from plib import *
           3 +seed0=int(sys.argv[1]); nseeds=int(sys.argv[2]); out=sys.argv[3]
           4 +rng=np.random.default_rng(seed0)
           5 +env=make_env()
           6 +O,A,O2,META=[],[],[],[]
           7 +def outline(w,Lh,Lv):
           8 +    return np.array([(-Lh/2,0),(-Lh/2,-w),(-w/2,-w),(-w/2,-w-Lv),(w/2,-w-Lv),(w/2,-w),(Lh/2,-w),(Lh/2,0)])
           9 +for seed in range(seed0,seed0+nseeds):
          10 +    obs,_=env.reset(seed=seed); steps=0
          11 +    for push in range(8):
          12 +        pose=obs[0:3].copy(); w,Lh,Lv=obs[12:15]
          13 +        V=outline(w,Lh,Lv); E=np.roll(V,-1,0)-V; L=np.linalg.norm(E,axis=1)
          14 +        e=rng.choice(8,p=L/L.sum()); s=rng.uniform(0.01,L[e]-0.01)
          15 +        d=E[e]/L[e]; nout=np.array([d[1],-d[0]]); p=V[e]+s*d
          16 +        ang=rng.uniform(-0.9,0.9)
          17 +        nin=-nout; c,sn=np.cos(ang),np.sin(ang); u=np.array([c*nin[0]-sn*nin[1],sn*nin[0]+c*nin[1]])
          18 +        st=to_world(pose,p+nout*(R+0.02)); uw=rot(pose[2])@u
          19 +        if st.min()<0.2 or st.max()>4.8: continue
          20 +        # skip if block near wall
          21 +        if np.min(to_world(pose,V))<0.4 or np.max(to_world(pose,V))>4.6:
          22 +            print("wall",seed,flush=True); break
          23 +        obs,ok=navigate(env,obs,to_world(pose,p+nout*(R+0.16)))
          24 +        if ok: obs=goto(env,obs,st); ok=np.abs(obs[0:3]-pose).max()<1e-7
          25 +        if not ok:
          26 +            print("navfail",seed,np.linalg.norm(obs[16:18]-st),np.abs(obs[0:3]-pose).max(),flush=True); continue
          27 +        sp=rng.uniform(0.01,0.0499)
          28 +        for k in range(14):
          29 +            a=uw*sp
          30 +            o1,*_=env.step(a)
          31 +            O.append(obs);A.append(a);O2.append(o1);META.append([seed,e,s,ang,sp,k]); obs=o1
          32 +    print(seed,len(O),flush=True)
          33 +np.savez(out,O=np.array(O),A=np.array(A),O2=np.array(O2),META=np.array(META))
          34 +env.close()
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..0334dcf
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,14 @@
           1 +import numpy as np, sys
           2 +from env_client import make_env
           3 +from approach import *
           4 +np.set_printoptions(precision=3, suppress=True)
           5 +env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
           6 +ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
           7 +orig=ap.plan_push
           8 +def pp(pose,robot):
           9 +    r=orig(pose,robot); print("PLAN pose",pose,"cost %.3f pred %.3f k %d"%(r[4],r[3],r[2]), "start",r[0],"dir",r[1]); return r
          10 +ap.plan_push=pp
          11 +for i in range(int(sys.argv[2])):
          12 +    a=ap.get_action(obs)
          13 +    obs,r,te,tr,_=env.step(a)
          14 +print(obs[[0,1,2,16,17]], ap.mode, ap.path)
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..22d9a90
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,13 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from approach import *
           4 +np.set_printoptions(precision=3, suppress=True)
           5 +env=make_env(); obs,_=env.reset(seed=1)
           6 +m=TModel(obs[12],obs[13],obs[14])
           7 +pose=obs[0:3].copy(); rob=obs[16:18].copy()
           8 +for i in range(40):
           9 +    a=np.array([0.049,0.0])
          10 +    p2,r2=m.step(pose,rob,a)
          11 +    obs,*_=env.step(a)
          12 +    if i>=33: print(i, obs[[0,1,2,16,17]], p2[0], r2[0])
          13 +    pose=obs[0:3].copy(); rob=obs[16:18].copy()
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..673ca60
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,7 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +env=make_env(); obs,_=env.reset(seed=1)
           4 +for a in [np.array([0.05,0.0]), np.array([0.049,0.0]), np.array([0.05,0.0],dtype=np.float32)]:
           5 +    try: env.step(a); print("ok",a.dtype,a)
           6 +    except Exception as e: print("fail",a, e)
           7 +print(env.action_space.low, env.action_space.high, env.action_space.dtype)
diff --git a/dbg4.py b/dbg4.py
new file mode 100644
index 0000000..89d9843
--- /dev/null
+++ b/dbg4.py
@@ -0,0 +1,5 @@
           1 +import numpy as np
           2 +from approach import *
           3 +pose=np.array([3.846,1.935,-0.482]); 
           4 +for rx in [3.277,3.326]:
           5 +    pl=to_local(np.array([[rx,1.95]]),pose); print(pl, dist_to_T_local(pl, rects_local(0.141,1.102,1.137)))
diff --git a/evalp.py b/evalp.py
new file mode 100644
index 0000000..85775a5
--- /dev/null
+++ b/evalp.py
@@ -0,0 +1,15 @@
           1 +import numpy as np, glob, sys
           2 +import push_model as pm
           3 +O=[];A=[];O2=[]
           4 +for f in sorted(glob.glob('data_*.npz')):
           5 +    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2'])
           6 +O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2)
           7 +rng=np.random.default_rng(0); idx=rng.permutation(len(O)); te=idx[3000:4500]
           8 +for ps in sys.argv[1:]:
           9 +    params=eval(ps); E=[]
          10 +    for i in te:
          11 +        o=O[i]; p,rb=pm.predict_step(o[0:3],o[16:18],A[i],pm.geom_from_obs(o),params)
          12 +        dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
          13 +        E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt),np.linalg.norm(rb-O2[i,16:18])])
          14 +    E=np.array(E)
          15 +    print(ps,'pos %.5f p95 %.5f max %.4f th %.5f p95 %.5f max %.4f robot %.6f'%(E[:,0].mean(),np.percentile(E[:,0],95),E[:,0].max(),E[:,1].mean(),np.percentile(E[:,1],95),E[:,1].max(),E[:,2].max()),flush=True)
diff --git a/fit.py b/fit.py
new file mode 100644
index 0000000..650d1a7
--- /dev/null
+++ b/fit.py
@@ -0,0 +1,35 @@
           1 +import numpy as np, glob, sys
           2 +from scipy.optimize import minimize
           3 +import push_model as pm
           4 +O=[];A=[];O2=[]
           5 +for f in sorted(glob.glob('data_*.npz')):
           6 +    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2'])
           7 +O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2)
           8 +dpos=np.linalg.norm(O2[:,0:2]-O[:,0:2],axis=1); dth=np.abs(O2[:,2]-O[:,2])
           9 +print('N',len(O),'moved',(dpos>1e-7).sum())
          10 +# robot tracking
          11 +rerr=O2[:,16:18]-O[:,16:18]-A; print('robot track err max',np.abs(rerr).max(),'mean',np.abs(rerr).mean())
          12 +# block near walls? use polygon
          13 +ok=np.array([pm.t_polygon_world(o[0:3],pm.geom_from_obs(o)).min()>0.05 and pm.t_polygon_world(o2[0:3],pm.geom_from_obs(o)).max()<4.95 for o,o2 in zip(O,O2)])
          14 +print('not near wall',ok.sum())
          15 +rng=np.random.default_rng(0)
          16 +idx=np.where(ok)[0]; rng.shuffle(idx)
          17 +tr=idx[:int(sys.argv[1]) if len(sys.argv)>1 else 1500]; te=idx[3000:]
          18 +def errs(params,ids):
          19 +    E=[]
          20 +    for i in ids:
          21 +        o=O[i]; p,_=pm.predict_step(o[0:3],o[16:18],A[i],pm.geom_from_obs(o),params)
          22 +        dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
          23 +        E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt)])
          24 +    return np.array(E)
          25 +def loss(x,nsub):
          26 +    params=dict(cx=x[0],cy=x[1],k2=abs(x[2])+1e-3,mu=abs(x[3]),nsub=nsub,r_eff=x[4])
          27 +    E=errs(params,tr); return np.mean(E[:,0]**2+(0.4*E[:,1])**2)
          28 +for nsub in [1,4]:
          29 +    x0=np.array([0,-0.35,0.12,0.3,0.1])
          30 +    r=minimize(loss,x0,args=(nsub,),method='Nelder-Mead',options=dict(maxfev=400,xatol=1e-4,fatol=1e-10))
          31 +    print(nsub,r.x,r.fun)
          32 +    params=dict(cx=r.x[0],cy=r.x[1],k2=abs(r.x[2])+1e-3,mu=abs(r.x[3]),nsub=nsub,r_eff=r.x[4])
          33 +    E=errs(params,te[:2000]); mv=np.array([dpos[i]>1e-7 for i in te[:2000]])
          34 +    print(' test pos err mean %.5f p95 %.5f  th err mean %.5f p95 %.5f; moved-only pos %.5f'%(E[:,0].mean(),np.percentile(E[:,0],95),E[:,1].mean(),np.percentile(E[:,1],95),E[mv,0].mean()))
          35 +    print(' baseline (no motion) pos %.5f th %.5f'%(dpos[te[:2000]].mean(),dth[te[:2000]].mean()),flush=True)
diff --git a/fit2.log b/fit2.log
new file mode 100644
index 0000000..21da0fc
--- /dev/null
+++ b/fit2.log
@@ -0,0 +1,4 @@
           1 +full 0 nsub 1 [0.9843 0.1004 0.2584] test pos mean 0.00069 p95 0.00193 th mean 0.00090 p95 0.00213
           2 +full 0 nsub 4 [0.9914 0.1015 0.2202] test pos mean 0.00055 p95 0.00110 th mean 0.00067 p95 0.00119
           3 +full 1 nsub 1 [ 9.8040e-01  1.0040e-01  2.5820e-01 -1.0000e-04  1.0284e+00] test pos mean 0.00067 p95 0.00179 th mean 0.00088 p95 0.00194
           4 +full 1 nsub 4 [9.945e-01 1.014e-01 2.213e-01 3.000e-04 1.003e+00] test pos mean 0.00054 p95 0.00107 th mean 0.00066 p95 0.00122
diff --git a/fit2.py b/fit2.py
new file mode 100644
index 0000000..5f1bb51
--- /dev/null
+++ b/fit2.py
@@ -0,0 +1,29 @@
           1 +import numpy as np, glob, sys
           2 +from scipy.optimize import minimize
           3 +import push_model as pm
           4 +O=[];A=[];O2=[]
           5 +for f in sorted(glob.glob('data_*.npz')):
           6 +    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2'])
           7 +O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2)
           8 +rng=np.random.default_rng(0); idx=rng.permutation(len(O)); tr=idx[:700]; te=idx[3000:5000]
           9 +def errs(fn,ids):
          10 +    E=[]
          11 +    for i in ids:
          12 +        o=O[i]; g=pm.geom_from_obs(o); p,_=pm.predict_step(o[0:3],o[16:18],A[i],g,fn(g))
          13 +        dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
          14 +        E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt)])
          15 +    return np.array(E)
          16 +def mk(x,nsub,full):
          17 +    def fn(g):
          18 +        c,k2=pm.mass_props(g)
          19 +        d=dict(mu=abs(x[0]),r_eff=x[1],beta=x[2],nsub=nsub)
          20 +        if full: d.update(cx=0.0,cy=c[1]+x[3],k2=k2*abs(x[4]))
          21 +        return d
          22 +    return fn
          23 +for full in [0,1]:
          24 +  for nsub in [1,4]:
          25 +    x0=np.array([1.0,0.1,0.25]+([0,1.0] if full else []))
          26 +    loss=lambda x: np.mean((lambda E: E[:,0]**2+(0.4*E[:,1])**2)(errs(mk(x,nsub,full),tr)))
          27 +    r=minimize(loss,x0,method='Nelder-Mead',options=dict(maxfev=300 if not full else 500,xatol=1e-4,fatol=1e-11))
          28 +    E=errs(mk(r.x,nsub,full),te)
          29 +    print('full',full,'nsub',nsub,np.round(r.x,4),'test pos mean %.5f p95 %.5f th mean %.5f p95 %.5f'%(E[:,0].mean(),np.percentile(E[:,0],95),E[:,1].mean(),np.percentile(E[:,1],95)),flush=True)
diff --git a/geom_res.json b/geom_res.json
new file mode 100644
index 0000000..5b0743b
--- /dev/null
+++ b/geom_res.json
@@ -0,0 +1 @@
           1 +[[0.0, "bartop", 0.130331788788359, 1.1823741402459995, 1.1359062478663557, 6.256129797744957e-08, 0.10168996336433249, 6.251038458553192e-08, 0.09968801025464573], [0.0, "stemend", 0.130331788788359, 1.1823741402459995, 1.1359062478663557, -1.5374565251908802e-05, -1.367662709648011, -1.5374514338503007e-05, -1.365660756538324], [0.0, "barbot", 0.130331788788359, 1.1823741402459995, 1.1359062478663557, 0.3500251663384142, -0.23174655057449253, 0.35002516638932757, -0.22974459746480577], [0.0, "barend", 0.130331788788359, 1.1823741402459995, 1.1359062478663557, 0.6929333750743614, -8.490150234078011e-06, 0.6909314219646746, -8.490099320708306e-06], [0.0, "stemside", 0.130331788788359, 1.1823741402459995, 1.1359062478663557, 0.16571095619979354, -0.7999820735755382, 0.16370900309010677, -0.7999820735246248], [0.0, "barbotL", 0.130331788788359, 1.1823741402459995, 1.1359062478663557, -0.349980287148902, -0.23173290190478932, -0.3499802870979886, -0.22973094879510259], [1.0, "bartop", 0.14138512969102207, 1.1022997840922903, 1.137398421918265, 1.9175619861523982e-05, 0.10167685402923113, 1.9175588475128563e-05, 0.09967490092191915], [1.0, "stemend", 0.14138512969102207, 1.1022997840922903, 1.137398421918265, 4.248928641211807e-06, -1.3811432440938198, 4.248960027634979e-06, -1.379141290986508], [1.0, "barend", 0.14138512969102207, 1.1022997840922903, 1.137398421918265, 0.6529276192566287, -3.819414918897448e-06, 0.6509256661493168, -3.819383532478232e-06], [1.0, "barbotL", 0.14138512969102207, 1.1022997840922903, 1.137398421918265, -0.349990284069863, -0.24371980228286852, -0.34999028403847654, -0.24171784917555653], [2.0, "bartop", 0.10939505366833017, 1.013786656833267, 1.0687423419765096, -1.8707485644785402e-05, 0.10165973194765368, -1.870746568614583e-05, 0.09965777873972034], [2.0, "stemend", 0.10939505366833017, 1.013786656833267, 1.0687423419765096, 9.287412142906452e-06, -1.2804620001600662, 9.287392184249536e-06, -1.2784600469521328], [2.0, "barend", 0.10939505366833017, 1.013786656833267, 1.0687423419765096, 0.6086732547190732, -7.8928359094285e-06, 0.6066713015111399, -7.89285586807176e-06], [2.0, "barbotL", 0.10939505366833017, 1.013786656833267, 1.0687423419765096, -0.3499946976700568, -0.21171422089273048, -0.3499946976900154, -0.20971226768479714], [3.0, "bartop", 0.1239525649070417, 1.0399347286592697, 1.1836442878523037, -5.2749369286868575e-06, 0.10167390907770914, -5.274940914580815e-06, 0.09967195589895206], [3.0, "barbot", 0.1239525649070417, 1.0399347286592697, 1.1836442878523037, 0.3499828312364468, -0.22573871750389302, 0.3499828312404327, -0.22373676432513595], [3.0, "barend", 0.1239525649070417, 1.0399347286592697, 1.1836442878523037, 0.6217376655253606, 2.0973843592436598e-06, 0.6197357123466035, 2.09738834514412e-06], [3.0, "stemside", 0.1239525649070417, 1.0399347286592697, 1.1836442878523037, 0.16372820781353428, -0.8000099145690672, 0.1617262546347772, -0.8000099145650813], [3.0, "barbotL", 0.1239525649070417, 1.0399347286592697, 1.1836442878523037, -0.35000179016208394, -0.22574730754930025, -0.35000179015809807, -0.2237453543705432], [4.0, "bartop", 0.14009506034929037, 1.043631954036007, 1.217908818546914, -2.452866385687701e-05, 0.10165605357568677, -2.45285948480214e-05, 0.09965410046315916], [4.0, "barbot", 0.14009506034929037, 1.043631954036007, 1.217908818546914, 0.35001526173439396, -0.24174867841363915, 0.3500152616653851, -0.23974672530111152], [4.0, "barend", 0.14009506034929037, 1.043631954036007, 1.217908818546914, 0.6235778526690577, -2.347841982840335e-05, 0.6215758995565301, -2.3478488837244746e-05], [4.0, "stemside", 0.14009506034929037, 1.043631954036007, 1.217908818546914, 0.17174272506513413, -0.7999799606789058, 0.16974077195260656, -0.7999799607479146], [5.0, "bartop", 0.12042366027099993, 1.0113187984756113, 1.012189427681792, -2.6345387706597498e-05, 0.10165984900030098, -2.634535860505091e-05, 0.09965789592016286], [5.0, "barbot", 0.12042366027099993, 1.0113187984756113, 1.012189427681792, 0.3500179693618875, -0.22174588537763065, 0.35001796933278595, -0.21974393229749253], [5.0, "barend", 0.12042366027099993, 1.0113187984756113, 1.012189427681792, 0.6074227415735126, 1.5606103679734424e-05, 0.6054207884933746, 1.560607457820167e-05], [5.0, "stemside", 0.12042366027099993, 1.0113187984756113, 1.012189427681792, 0.16171290905891772, -0.8000252567296778, 0.1597109559787796, -0.8000252567587793], [5.0, "barbotL", 0.12042366027099993, 1.0113187984756113, 1.012189427681792, -0.3500088444623168, -0.22174587878247146, -0.3500088444914184, -0.21974392570233334], [6.0, "bartop", 0.1424932815547606, 1.1081237029137576, 1.1568669834257685, 1.8562522905755653e-06, 0.10167238004325599, 1.8562656937322673e-06, 0.09967042693962706], [6.0, "stemend", 0.1424932815547606, 1.1081237029137576, 1.1568669834257685, 3.833657661132013e-06, -1.4006405613032813, 3.833644257944087e-06, -1.3986386081996525], [6.0, "barbot", 0.1424932815547606, 1.1081237029137576, 1.1568669834257685, 0.3499914744840949, -0.24375340891795821, 0.3499914744706918, -0.2417514558143293], [6.0, "barend", 0.1424932815547606, 1.1081237029137576, 1.1568669834257685, 0.6558322852251905, -1.0553277862090992e-05, 0.6538303321215616, -1.0553291265255337e-05], [6.0, "stemside", 0.1424932815547606, 1.1081237029137576, 1.1568669834257685, 0.17374414272204486, -0.8000118675781889, 0.17174218961841595, -0.8000118675915922], [6.0, "barbotL", 0.1424932815547606, 1.1081237029137576, 1.1568669834257685, -0.3499812122418582, -0.24376114601484375, -0.34998121225526135, -0.24175919291121487], [7.0, "bartop", 0.13110896147205814, 1.2472400369204713, 1.0538271745588998, -1.1087993335045856e-05, 0.10166867855995354, -1.1087994193247597e-05, 0.09966672539334373], [7.0, "stemend", 0.13110896147205814, 1.2472400369204713, 1.0538271745588998, 2.242879012361203e-05, -1.2855520751530827, 2.2428790981803364e-05, -1.283550121986473], [7.0, "barbot", 0.13110896147205814, 1.2472400369204713, 1.0538271745588998, 0.3499726594269342, -0.23175286059637742, 0.3499726594277924, -0.22975090742976761], [7.0, "barbotL", 0.13110896147205814, 1.2472400369204713, 1.0538271745588998, -0.35000006938453243, -0.2317455634860252, -0.35000006938367423, -0.2297436103194154], [8.0, "bartop", 0.12189409365613994, 1.0931872257723383, 1.0267383991181935, 2.8538912915791916e-05, 0.101658132028922, 2.8538900593349397e-05, 0.09965617891745959], [8.0, "stemend", 0.12189409365613994, 1.0931872257723383, 1.0267383991181935, 1.75421967533647e-05, -1.2504607183959575, 1.7542209075758645e-05, -1.2484587652844952], [8.0, "barbot", 0.12189409365613994, 1.0931872257723383, 1.0267383991181935, 0.34998003116213094, -0.22372229240396138, 0.3499800311744534, -0.22172033929249899], [8.0, "barend", 0.12189409365613994, 1.0931872257723383, 1.0267383991181935, 0.6483305499538514, -2.4267807163669725e-06, 0.646328596842389, -2.426768393895997e-06], [8.0, "stemside", 0.12189409365613994, 1.0931872257723383, 1.0267383991181935, 0.1617197234625319, -0.8000319320236504, 0.15971777035106952, -0.8000319320113279], [8.0, "barbotL", 0.12189409365613994, 1.0931872257723383, 1.0267383991181935, -0.350009584619981, -0.22372326089157585, -0.3500095846076585, -0.22172130778011342], [9.0, "bartop", 0.14301968245914423, 1.2295594072621907, 1.0066469336168993, -3.0301066066336196e-05, 0.10166661525875156, -3.03010547235438e-05, 0.09966466215876299], [9.0, "stemend", 0.14301968245914423, 1.2295594072621907, 1.0066469336168993, -5.469367579768846e-06, -1.2504211825498956, -5.4693789225820566e-06, -1.248419229449907], [9.0, "barbot", 0.14301968245914423, 1.2295594072621907, 1.0066469336168993, 0.34998474121797907, -0.24373441658951145, 0.34998474120663625, -0.24173246348952288], [9.0, "barend", 0.14301968245914423, 1.2295594072621907, 1.0066469336168993, 0.7165254474117877, -1.6524544473110447e-05, 0.7145234943117991, -1.652455581590333e-05], [9.0, "stemside", 0.14301968245914423, 1.2295594072621907, 1.0066469336168993, 0.1737083801365302, -0.7999981491092713, 0.17170642703654163, -0.7999981491206141], [9.0, "barbotL", 0.14301968245914423, 1.2295594072621907, 1.0066469336168993, -0.349995800842389, -0.24377408124655053, -0.3499958008537318, -0.24177212814656196], [10.0, "bartop", 0.13445182398905656, 1.2104369310780698, 1.1063772493512443, -1.3945488150359039e-05, 0.10165917707194413, -1.3945554073801318e-05, 0.09965722394509698], [10.0, "stemend", 0.13445182398905656, 1.2104369310780698, 1.1063772493512443, -1.4420397920935757e-05, -1.342125197559053, -1.4420331997486539e-05, -1.3401232444322058], [10.0, "barbot", 0.13445182398905656, 1.2104369310780698, 1.1063772493512443, 0.34997610020299197, -0.23575085635967352, 0.34997610026891546, -0.23374890323282638], [10.0, "barend", 0.13445182398905656, 1.2104369310780698, 1.1063772493512443, 0.7069931058827631, 4.682124048153875e-07, 0.704991152755916, 4.682783282391077e-07], [10.0, "stemside", 0.13445182398905656, 1.2104369310780698, 1.1063772493512443, 0.16972019761818763, -0.7999825296002748, 0.16771824449134048, -0.7999825295343513], [10.0, "barbotL", 0.13445182398905656, 1.2104369310780698, 1.1063772493512443, -0.3500139497896404, -0.2357292650906068, -0.35001394972371697, -0.23372731196375962], [11.0, "bartop", 0.1408368217984829, 1.1372688172175065, 1.2452284098243265, -2.4239817080990886e-06, 0.1016423745293377, -2.423981888982704e-06, 0.09964042133544608], [11.0, "stemend", 0.1408368217984829, 1.1372688172175065, 1.2452284098243265, 1.851947312303612e-05, -1.4869885308965798, 1.851947330392754e-05, -1.4849865777026883], [11.0, "barbotL", 0.1408368217984829, 1.1372688172175065, 1.2452284098243265, -0.3499762372119007, -0.2417466102601729, -0.34997623721171983, -0.23974465706628129]]
\ No newline at end of file
diff --git a/geom_res.npy b/geom_res.npy
new file mode 100644
index 0000000..5544230
Binary files /dev/null and b/geom_res.npy differ
diff --git a/look.py b/look.py
new file mode 100644
index 0000000..b90423d
--- /dev/null
+++ b/look.py
@@ -0,0 +1,17 @@
           1 +import numpy as np, glob
           2 +import push_model as pm
           3 +O=[];A=[];O2=[];MT=[]
           4 +for f in sorted(glob.glob('data_*.npz')):
           5 +    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2']);MT.append(d['META'])
           6 +O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2);MT=np.concatenate(MT)
           7 +g=lambda o: pm.geom_from_obs(o)
           8 +m=np.where((np.abs(MT[:,3])<0.25))[0]
           9 +shown=0; last=None
          10 +for i in m:
          11 +    key=tuple(MT[i,:5])
          12 +    if key!=last:
          13 +        if shown>=4: break
          14 +        shown+=1; last=key; print('push seed %d edge %d s %.3f ang %.2f sp %.4f'%tuple(MT[i,:5]))
          15 +    o,o2=O[i],O2[i]
          16 +    d_pre=pm.block_distance(o[0:3],g(o),o[16:18]); d_post=pm.block_distance(o2[0:3],g(o),o2[16:18]); d_mid=pm.block_distance(o[0:3],g(o),o2[16:18])
          17 +    print('  k%2d dpre %.4f dnew_oldblock %.4f dpost %.4f  blk move %.4f dth %.4f  a %.4f'%(MT[i,5],d_pre,d_mid,d_post,np.linalg.norm(o2[:2]-o[:2]),o2[2]-o[2],np.linalg.norm(A[i])))
diff --git a/outl.py b/outl.py
new file mode 100644
index 0000000..f9b72a5
--- /dev/null
+++ b/outl.py
@@ -0,0 +1,19 @@
           1 +import numpy as np, glob
           2 +import push_model as pm
           3 +O=[];A=[];O2=[];MT=[]
           4 +for f in sorted(glob.glob('data_*.npz')):
           5 +    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2']);MT.append(d['META'])
           6 +O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2);MT=np.concatenate(MT)
           7 +P=dict(mu=0.99,r_eff=0.1015,beta=0.22,nsub=4)
           8 +E=[]
           9 +for i in range(len(O)):
          10 +    o=O[i]; p,_=pm.predict_step(o[0:3],o[16:18],A[i],pm.geom_from_obs(o),P)
          11 +    dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
          12 +    E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt)])
          13 +E=np.array(E); np.save('E_all.npy',E)
          14 +print('ALL N=%d pos mean %.5f p50 %.5f p95 %.5f p99 %.5f | th mean %.5f p95 %.5f p99 %.5f'%(len(E),E[:,0].mean(),np.median(E[:,0]),*np.percentile(E[:,0],[95,99]),E[:,1].mean(),*np.percentile(E[:,1],[95,99])))
          15 +for i in np.argsort(-E[:,0])[:12]:
          16 +    o=O[i]; g=pm.geom_from_obs(o); pl=pm.to_local if hasattr(pm,'to_local') else None
          17 +    poly=pm.t_polygon_world(o[0:3],g)
          18 +    rl=(o[16:18]-o[:2])@pm._rot(o[2])
          19 +    print('i%d err %.4f th %.4f meta %s rob_local %s dpre %.4f blkminmax %.2f %.2f true move %.4f %.4f'%(i,E[i,0],E[i,1],np.round(MT[i],3),np.round(rl,3),pm.block_distance(o[0:3],g,o[16:18]),poly.min(),poly.max(),np.linalg.norm(O2[i,:2]-o[:2]),O2[i,2]-o[2]))
diff --git a/plib.py b/plib.py
index 5bcd2d8..6017962 100644
--- a/plib.py
+++ b/plib.py
@@ -3,33 +3,24 @@ from env_client import make_env
    3      3  M=0.0499
    4      4  R=0.1
    5      5  def rot(t): c,s=np.cos(t),np.sin(t); return np.array([[c,-s],[s,c]])
    6        -def t_polys_local(w,Lh,Lv,stem_end=None):
    7        -    # hypothesis: bar y in [-w/2,w/2], stem y in [stem_end,-w/2]
    8        -    if stem_end is None: stem_end=-Lv
    9        -    bar=np.array([[-Lh/2,-w/2],[Lh/2,-w/2],[Lh/2,w/2],[-Lh/2,w/2]])
   10        -    stem=np.array([[-w/2,stem_end],[w/2,stem_end],[w/2,-w/2],[-w/2,-w/2]])
   11        -    return [bar,stem]
   12        -def to_world(pose,P): return P@rot(pose[2]).T+pose[:2]
           6 +def rects_local(w,Lh,Lv):
           7 +    # (x0,x1,y0,y1): bar then stem; origin = top-center of bar
           8 +    return [(-Lh/2,Lh/2,-w,0.0),(-w/2,w/2,-w-Lv,-w)]
           9 +def to_world(pose,P): return np.asarray(P)@rot(pose[2]).T+pose[:2]
   13     10  def to_local(pose,p): return (np.asarray(p)-pose[:2])@rot(pose[2])
   14        -def seg_dist(p,a,b):
   15        -    ab=b-a; t=np.clip(np.dot(p-a,ab)/np.dot(ab,ab),0,1); return np.linalg.norm(p-a-t*ab)
   16        -def poly_dist(p,P):
   17        -    # signed-ish: 0 if inside
   18        -    n=len(P); d=min(seg_dist(p,P[i],P[(i+1)%n]) for i in range(n))
   19        -    inside=all(np.cross(P[(i+1)%n]-P[i],p-P[i])>=0 for i in range(n))
   20        -    return 0.0 if inside else d
   21        -def block_dist(obs,p,stem_end=None,margin_local=0.0):
          11 +def block_dist_many(obs,pts):
   22     12      pose=obs[0:3]; w,Lh,Lv=obs[12],obs[13],obs[14]
   23        -    pl=to_local(pose,p)
   24        -    return min(poly_dist(pl,P) for P in t_polys_local(w,Lh,Lv,stem_end))
          13 +    pl=to_local(pose,np.atleast_2d(pts))
          14 +    ds=[]
          15 +    for x0,x1,y0,y1 in rects_local(w,Lh,Lv):
          16 +        dx=np.maximum(np.maximum(x0-pl[:,0],pl[:,0]-x1),0); dy=np.maximum(np.maximum(y0-pl[:,1],pl[:,1]-y1),0)
          17 +        ds.append(np.hypot(dx,dy))
          18 +    return np.min(ds,axis=0)
   25     19  def plan(obs,goal,clear=0.2,h=0.05,lo=0.13,hi=4.87):
   26        -    # A* on grid avoiding block by clearance (robot center distance to polygon)
   27     20      start=obs[16:18].copy(); goal=np.asarray(goal,float)
   28     21      xs=np.arange(lo,hi+1e-9,h); n=len(xs)
   29        -    free=np.ones((n,n),bool)
   30        -    for i in range(n):
   31        -        for j in range(n):
   32        -            free[i,j]=block_dist(obs,np.array([xs[i],xs[j]]))>clear
          22 +    X,Y=np.meshgrid(xs,xs,indexing='ij')
          23 +    free=(block_dist_many(obs,np.stack([X.ravel(),Y.ravel()],1))>clear).reshape(n,n)
   33     24      def idx(p): return (int(np.clip(round((p[0]-lo)/h),0,n-1)),int(np.clip(round((p[1]-lo)/h),0,n-1)))
   34     25      s,g=idx(start),idx(goal)
   35     26      free[s]=True; free[g]=True
@@ -49,8 +40,17 @@ def plan(obs,goal,clear=0.2,h=0.05,lo=0.13,hi=4.87):
   49     40      if g not in came: return None
   50     41      path=[]; c=g
   51     42      while c is not None: path.append(np.array([xs[c[0]],xs[c[1]]])); c=came[c]
   52        -    path=path[::-1][1:]+[goal]
   53        -    return path
          43 +    path=path[::-1][1:]
          44 +    # shortcut: prune waypoints whose straight segment is clear
          45 +    pts=[start]+path+[goal]; out=[]; i=0
          46 +    while i<len(pts)-1:
          47 +        j=len(pts)-1
          48 +        while j>i+1:
          49 +            seg=pts[i]+np.linspace(0,1,40)[:,None]*(pts[j]-pts[i])
          50 +            if (block_dist_many(obs,seg)>clear-0.03).all(): break
          51 +            j-=1
          52 +        out.append(pts[j]); i=j
          53 +    return out
   54     54  def goto(env,obs,pt,max_step=M):
   55     55      for _ in range(400):
   56     56          d=pt-obs[16:18]
@@ -66,3 +66,20 @@ def navigate(env,obs,goal,clear=0.2):
   66     66          obs=goto(env,obs,wp)
   67     67      moved=np.abs(obs[0:3]-b0).max()>1e-6
   68     68      return obs,(not moved) and np.linalg.norm(obs[16:18]-goal)<1e-3
          69 +def backoff(env,obs,clear=0.2):
          70 +    for _ in range(40):
          71 +        p=obs[16:18]; d0=block_dist_many(obs,p)[0]
          72 +        if d0>=clear+0.01: break
          73 +        eps=1e-4
          74 +        g=np.array([block_dist_many(obs,p+[eps,0])[0]-d0,block_dist_many(obs,p+[0,eps])[0]-d0])
          75 +        g=g/(np.linalg.norm(g)+1e-12)
          76 +        if p[0]<0.3: g[0]=max(g[0],0.3)
          77 +        if p[1]<0.3: g[1]=max(g[1],0.3)
          78 +        if p[0]>4.7: g[0]=min(g[0],-0.3)
          79 +        if p[1]>4.7: g[1]=min(g[1],-0.3)
          80 +        obs,*_=env.step(g/np.linalg.norm(g)*0.03)
          81 +    return obs
          82 +_nav_old=navigate
          83 +def navigate(env,obs,goal,clear=0.2):
          84 +    obs=backoff(env,obs,clear)
          85 +    return _nav_old(env,obs,goal,clear)
diff --git a/probe5.py b/probe5.py
new file mode 100644
index 0000000..64620c8
--- /dev/null
+++ b/probe5.py
@@ -0,0 +1,12 @@
           1 +from plib import *
           2 +np.set_printoptions(precision=5, suppress=True, linewidth=200)
           3 +env=make_env(); obs,_=env.reset(seed=0)
           4 +pose=obs[0:3].copy()
           5 +st=to_world(pose,np.array([0,0.35]))
           6 +obs,ok=navigate(env,obs,st); print(ok)
           7 +dw=rot(pose[2])@np.array([0,-1.0])
           8 +for k in range(12):
           9 +    a=dw*M if k<6 else np.zeros(2)
          10 +    o2,*_=env.step(a)
          11 +    print(k, 'blk d', o2[0:3]-obs[0:3], 'dist', block_dist_many(o2,o2[16:18]), 'vel?',o2[3:6])
          12 +    obs=o2
diff --git a/push_model.py b/push_model.py
new file mode 100644
index 0000000..40a4703
--- /dev/null
+++ b/push_model.py
@@ -0,0 +1,157 @@
           1 +"""Pure-numpy one-step model of the push-T block.
           2 +
           3 +Geometry (block local frame, origin = block pose (x, y), theta CCW):
           4 +  bar : x in [-Lh/2, Lh/2], y in [-w, 0]         (origin = top-centre of the bar)
           5 +  stem: x in [-w/2, w/2],   y in [-w-Lv, -w]
           6 +Robot: disc of radius R=0.1, kinematic, moves exactly by the (clipped) action.
           7 +
           8 +Model: per sub-step, the robot moves action/NSUB; for every rectangle of the T that the
           9 +robot disc penetrates, an inelastic point-contact impulse (with Coulomb friction) is
          10 +applied to the block so the contact point is pushed out of the robot:
          11 +    block COM displacement = P / m,  rotation = (r x P) / I   (m = 1, I = K2)
          12 +Block velocity is not carried between env steps (quasi-static).
          13 +"""
          14 +import numpy as np
          15 +
          16 +R_ROBOT = 0.1
          17 +ACT_MAX = 0.05
          18 +WORLD_LO, WORLD_HI = 0.0, 5.0
          19 +
          20 +# fitted parameters (see fit.py)
          21 +PARAMS = dict(cx=None, cy=None, k2=None, mu=0.99, nsub=4, r_eff=0.1015, beta=0.22)
          22 +
          23 +
          24 +def mass_props(geom):
          25 +    """Uniform-density COM (local) and I/m of the T about its COM."""
          26 +    w, Lh, Lv = geom['w'], geom['Lh'], geom['Lv']
          27 +    a1, a2 = Lh * w, Lv * w
          28 +    y1, y2 = -w / 2, -w - Lv / 2
          29 +    cy = (a1 * y1 + a2 * y2) / (a1 + a2)
          30 +    I = a1 * ((Lh ** 2 + w ** 2) / 12 + (y1 - cy) ** 2) + a2 * ((w ** 2 + Lv ** 2) / 12 + (y2 - cy) ** 2)
          31 +    return np.array([0.0, cy]), I / (a1 + a2)
          32 +
          33 +
          34 +def geom_from_obs(obs):
          35 +    """dict(w, Lh, Lv) from an env observation."""
          36 +    return dict(w=float(obs[12]), Lh=float(obs[13]), Lv=float(obs[14]))
          37 +
          38 +
          39 +def _rot(t):
          40 +    c, s = np.cos(t), np.sin(t)
          41 +    return np.array([[c, -s], [s, c]])
          42 +
          43 +
          44 +def t_rects_local(geom):
          45 +    """[(x0, x1, y0, y1), ...] for bar and stem in the block frame."""
          46 +    w, Lh, Lv = geom['w'], geom['Lh'], geom['Lv']
          47 +    return [(-Lh / 2, Lh / 2, -w, 0.0), (-w / 2, w / 2, -w - Lv, -w)]
          48 +
          49 +
          50 +def t_outline_local(geom):
          51 +    """8 vertices (CCW) of the T outline in the block frame."""
          52 +    w, Lh, Lv = geom['w'], geom['Lh'], geom['Lv']
          53 +    return np.array([(-Lh / 2, 0), (-Lh / 2, -w), (-w / 2, -w), (-w / 2, -w - Lv),
          54 +                     (w / 2, -w - Lv), (w / 2, -w), (Lh / 2, -w), (Lh / 2, 0)])
          55 +
          56 +
          57 +def t_polygon_world(pose, geom):
          58 +    """8x2 outline vertices (CCW) in world frame for block pose (x, y, theta)."""
          59 +    pose = np.asarray(pose, float)
          60 +    return t_outline_local(geom) @ _rot(pose[2]).T + pose[:2]
          61 +
          62 +
          63 +def t_rects_world(pose, geom):
          64 +    """Two 4x2 convex rectangles (bar, stem) in world frame."""
          65 +    pose = np.asarray(pose, float)
          66 +    Rm = _rot(pose[2])
          67 +    out = []
          68 +    for x0, x1, y0, y1 in t_rects_local(geom):
          69 +        P = np.array([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])
          70 +        out.append(P @ Rm.T + pose[:2])
          71 +    return out
          72 +
          73 +
          74 +def block_distance(pose, geom, p):
          75 +    """Distance from world point p to the T (0 if inside)."""
          76 +    pose = np.asarray(pose, float)
          77 +    pl = (np.asarray(p, float) - pose[:2]) @ _rot(pose[2])
          78 +    d = np.inf
          79 +    for x0, x1, y0, y1 in t_rects_local(geom):
          80 +        dx = max(x0 - pl[0], 0.0, pl[0] - x1)
          81 +        dy = max(y0 - pl[1], 0.0, pl[1] - y1)
          82 +        d = min(d, np.hypot(dx, dy))
          83 +    return d
          84 +
          85 +
          86 +def _rect_contact(pl, rect):
          87 +    """Nearest point q on rect to local point pl, outward normal n, distance d."""
          88 +    x0, x1, y0, y1 = rect
          89 +    q = np.array([min(max(pl[0], x0), x1), min(max(pl[1], y0), y1)])
          90 +    v = pl - q
          91 +    d = np.hypot(v[0], v[1])
          92 +    if d > 1e-9:
          93 +        return q, v / d, d
          94 +    # centre inside rectangle: push out through the nearest face
          95 +    cand = [(pl[0] - x0, np.array([-1.0, 0])), (x1 - pl[0], np.array([1.0, 0])),
          96 +            (pl[1] - y0, np.array([0, -1.0])), (y1 - pl[1], np.array([0, 1.0]))]
          97 +    dd, n = min(cand, key=lambda c: c[0])
          98 +    return pl + n * dd, n, -dd
          99 +
         100 +
         101 +def predict_step(block_pose, robot_xy, action, geom, params=None):
         102 +    """Predict (new_block_pose, new_robot_xy) after one env step.
         103 +
         104 +    block_pose: (x, y, theta); robot_xy: (x, y); action: (dx, dy) (clipped to +-0.05).
         105 +    geom: dict(w, Lh, Lv) (see geom_from_obs).
         106 +    """
         107 +    p = PARAMS if params is None else params
         108 +    cg, k2g = mass_props(geom)
         109 +    cl = cg if p.get('cx') is None else np.array([p['cx'], p['cy']])
         110 +    k2 = k2g if p.get('k2') is None else p['k2']
         111 +    mu, nsub, reff0, beta = p['mu'], int(p['nsub']), p['r_eff'], p.get('beta', 0.0)
         112 +    pose = np.array(block_pose, float)
         113 +    rob = np.array(robot_xy, float)
         114 +    a = np.clip(np.asarray(action, float), -ACT_MAX, ACT_MAX)
         115 +    lo, hi = WORLD_LO + R_ROBOT, WORLD_HI - R_ROBOT
         116 +    rects = t_rects_local(geom)
         117 +    for _ in range(nsub):
         118 +        new = np.clip(rob + a / nsub, lo, hi)
         119 +        da = new - rob
         120 +        rob = new
         121 +        for rect in rects:
         122 +            Rm = _rot(pose[2])
         123 +            pl = (rob - pose[:2]) @ Rm
         124 +            q, n, d = _rect_contact(pl, rect)
         125 +            if d >= reff0:
         126 +                continue
         127 +            nw = Rm @ n                           # outward normal (towards robot), world
         128 +            # block overshoots: ends ~beta*(normal push speed) beyond touching
         129 +            delta = reff0 + beta * max(0.0, -np.dot(a, nw)) - d
         130 +            tw = np.array([-nw[1], nw[0]])
         131 +            com = pose[:2] + Rm @ cl
         132 +            r = pose[:2] + Rm @ q - com           # contact point rel. COM
         133 +            rp = np.array([-r[1], r[0]])
         134 +            K = np.eye(2) + np.outer(rp, rp) / k2  # contact-point compliance
         135 +            # desired contact-point displacement: -n*delta (into block), tangential follows robot
         136 +            want = -nw * delta + tw * np.dot(da, tw)
         137 +            P = np.linalg.solve(K, want)
         138 +            Pn, Pt = -np.dot(P, nw), np.dot(P, tw)
         139 +            if Pn <= 0:
         140 +                continue
         141 +            if abs(Pt) > mu * Pn:                 # sliding
         142 +                s = np.sign(Pt)
         143 +                dirv = -nw + mu * s * tw
         144 +                Pn = delta / np.dot(-nw, K @ dirv)
         145 +                P = Pn * dirv
         146 +            dth = (r[0] * P[1] - r[1] * P[0]) / k2
         147 +            com = com + P
         148 +            pose[2] += dth
         149 +            pose[:2] = com - _rot(pose[2]) @ cl
         150 +    return pose, rob
         151 +
         152 +
         153 +def near_wall(pose, geom, margin=0.02):
         154 +    """True if the T is within `margin` of the world walls (x,y in [0,5]); the model
         155 +    ignores block-wall contact, so predictions there are unreliable."""
         156 +    P = t_polygon_world(pose, geom)
         157 +    return bool(P.min() < WORLD_LO + margin or P.max() > WORLD_HI - margin)
diff --git a/resid.py b/resid.py
new file mode 100644
index 0000000..cdf50fc
--- /dev/null
+++ b/resid.py
@@ -0,0 +1,21 @@
           1 +import numpy as np, glob, sys
           2 +import push_model as pm
           3 +O=[];A=[];O2=[];MT=[]
           4 +for f in sorted(glob.glob('data_*.npz')):
           5 +    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2']);MT.append(d['META'])
           6 +O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2);MT=np.concatenate(MT)
           7 +rng=np.random.default_rng(1); idx=rng.choice(len(O),1500,replace=False)
           8 +params=eval(sys.argv[1]) if len(sys.argv)>1 else None
           9 +E=[]
          10 +for i in idx:
          11 +    o=O[i]; p,_=pm.predict_step(o[0:3],o[16:18],A[i],pm.geom_from_obs(o),params)
          12 +    dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
          13 +    E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt),np.linalg.norm(O2[i,:2]-o[:2]),abs(O2[i,2]-o[2])])
          14 +E=np.array(E); M=MT[idx]
          15 +print('all: pos %.5f th %.5f | motion pos %.5f th %.5f'%tuple(E.mean(0)))
          16 +for k in [0,1,2,5,13]:
          17 +    m=M[:,5]==k; print(' k=%d pos %.5f th %.5f | mot %.5f %.5f'%((k,)+tuple(E[m].mean(0))))
          18 +for e in range(8):
          19 +    m=M[:,1]==e; print(' edge=%d pos %.5f th %.5f | mot %.5f %.5f'%((e,)+tuple(E[m].mean(0))))
          20 +for lo,hi in [(0,0.3),(0.3,0.6),(0.6,0.9)]:
          21 +    m=(np.abs(M[:,3])>=lo)&(np.abs(M[:,3])<hi); print(' |ang| %.1f-%.1f pos %.5f th %.5f | mot %.5f %.5f'%((lo,hi)+tuple(E[m].mean(0))))
```

</details>

<a id="C008"></a>
### C008 · Progress-rate push selection

Commit `4f0f79375e25979cfd6f5b6f1911e8f9b8ae72d9`; parents: 97868d94ade0ef93d0b673758cb92b99adf43812. Recorded author date: 2026-09-30T17:41:03+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0447](01_timeline.md#E0447): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_4f0f793_approach.py) · [Exact all-file diff](evidence/diffs/C008_4f0f793.diff)

[Previous saved controller snapshot](evidence/versions/C007_97868d9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fa730d8..fb75a6f 100644
--- a/approach.py
+++ b/approach.py
@@ -158,7 +158,8 @@ class TModel:
  158    158  class GeneratedApproach:
  159    159      def __init__(self, action_space, observation_space, primitives):
  160    160          self.action_space = action_space
  161        -        self.alpha = 50.0
         161 +        self.goal_bonus = 0.05
         162 +        self.overhead = 2.0
  162    163          self.H = 40
  163    164          self.replan_every = 8
  164    165          self.model = None
@@ -248,18 +249,19 @@ class GeneratedApproach:
  248    249          travel = np.where(HERE, 0.0, self.travel_est(robot, PRE, pose) + 0.12 / MAXD)
  249    250          cur = np.repeat(pose[None], N, 0)
  250    251          rob = SW.copy()
  251        -        bestscore = np.full(N, np.inf)
         252 +        bestscore = np.full(N, -np.inf)
  252    253          bestk = np.zeros(N, int)
  253    254          H = self.H
  254    255          for k in range(1, H + 1):
  255    256              cur, rob = self.sim.step(cur, rob, DW * SP[:, None])
  256    257              cst = self.cost(cur)
  257    258              done = self.in_goal(cur, 0.75)
  258        -            score = np.where(done, 0.0, self.alpha * cst) + k + travel
  259        -            m = score < bestscore
         259 +            cst = np.where(done, -self.goal_bonus, cst)
         260 +            score = (c0 - cst) / (k + travel + self.overhead)
         261 +            m = score > bestscore
  260    262              bestscore[m] = score[m]
  261    263              bestk[m] = k
  262        -        i = int(np.argmin(bestscore))
         264 +        i = int(np.argmax(bestscore))
  263    265          return SW[i], DW[i] * SP[i], bestk[i], bestscore[i], c0, HERE[i]
  264    266  
  265    267      def in_goal(self, poses, frac=1.0):
diff --git a/dbg.py b/dbg.py
index 0334dcf..b5d0511 100644
--- a/dbg.py
+++ b/dbg.py
@@ -6,9 +6,9 @@ env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
    6      6  ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
    7      7  orig=ap.plan_push
    8      8  def pp(pose,robot):
    9        -    r=orig(pose,robot); print("PLAN pose",pose,"cost %.3f pred %.3f k %d"%(r[4],r[3],r[2]), "start",r[0],"dir",r[1]); return r
           9 +    r=orig(pose,robot); print("PLAN pose",pose,"rob",robot,"cost %.3f score %.3f k %d here %d"%(r[4],r[3],r[2],r[5]), "start",r[0],"dir",r[1]); return r
   10     10  ap.plan_push=pp
   11     11  for i in range(int(sys.argv[2])):
   12     12      a=ap.get_action(obs)
   13     13      obs,r,te,tr,_=env.step(a)
   14        -print(obs[[0,1,2,16,17]], ap.mode, ap.path)
          14 +    if te: print("DONE",i); break
```

</details>

<a id="C009"></a>
### C009 · tunable params

Commit `35632852a07214dbcca1f63ab34663a3b79ab9cd`; parents: 4f0f79375e25979cfd6f5b6f1911e8f9b8ae72d9. Recorded author date: 2026-09-30T17:43:14+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0471](01_timeline.md#E0471): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_3563285_approach.py) · [Exact all-file diff](evidence/diffs/C009_3563285.diff)

[Previous saved controller snapshot](evidence/versions/C008_4f0f793_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fb75a6f..9c1e42d 100644
--- a/approach.py
+++ b/approach.py
@@ -160,6 +160,7 @@ class GeneratedApproach:
  160    160          self.action_space = action_space
  161    161          self.goal_bonus = 0.05
  162    162          self.overhead = 2.0
         163 +        self.wa = 0.6
  163    164          self.H = 40
  164    165          self.replan_every = 8
  165    166          self.model = None
@@ -184,7 +185,7 @@ class GeneratedApproach:
  184    185          pose = np.atleast_2d(pose)
  185    186          dp = pose[:, :2] - self.goal[:2]
  186    187          da = np.abs(wrap_arr(pose[:, 2] - self.goal[2]))
  187        -        return np.hypot(dp[:, 0], dp[:, 1]) + 0.6 * da
         188 +        return np.hypot(dp[:, 0], dp[:, 1]) + self.wa * da
  188    189  
  189    190      def solved(self, pose):
  190    191          return (abs(pose[0] - self.goal[0]) < 0.03 and abs(pose[1] - self.goal[1]) < 0.03
diff --git a/tune.py b/tune.py
new file mode 100644
index 0000000..3cdb96a
--- /dev/null
+++ b/tune.py
@@ -0,0 +1,25 @@
           1 +import sys, json, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +import approach
           5 +from multiprocessing import Pool
           6 +OV = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
           7 +def run(seed):
           8 +    env = make_env()
           9 +    obs, info = env.reset(seed=seed)
          10 +    ap = approach.GeneratedApproach(env.action_space, env.observation_space, {})
          11 +    for k,v in OV.items():
          12 +        if k.startswith("G_"): setattr(approach, k[2:], v)
          13 +        else: setattr(ap, k, v)
          14 +    ap.reset(obs, info)
          15 +    t0=time.time()
          16 +    for steps in range(1, env.max_steps + 1):
          17 +        obs, r, term, trunc, _ = env.step(np.clip(ap.get_action(obs), -0.049, 0.049))
          18 +        if term or trunc: break
          19 +    env.close()
          20 +    return term, steps, time.time()-t0
          21 +if __name__ == "__main__":
          22 +    a, b = int(sys.argv[1]), int(sys.argv[2])
          23 +    with Pool(15) as p:
          24 +        res = p.map(run, range(a, b))
          25 +    print(OV, "solved %d/%d mean %.1f maxt %.1f" % (sum(r[0] for r in res), len(res), np.mean([r[1] for r in res]), max(r[2] for r in res)))
```

</details>

<a id="C010"></a>
### C010 · two-level lookahead (M param), zero action in goal

Commit `8bfdcfcfe5a47cbda863abda8ef6b4b359bd5f23`; parents: 35632852a07214dbcca1f63ab34663a3b79ab9cd. Recorded author date: 2026-09-30T17:48:10+02:00.

File roles (automatic): policy.

- [E0512](01_timeline.md#E0512): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_8bfdcfc_approach.py) · [Exact all-file diff](evidence/diffs/C010_8bfdcfc.diff)

[Previous saved controller snapshot](evidence/versions/C009_3563285_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9c1e42d..587cb0a 100644
--- a/approach.py
+++ b/approach.py
@@ -161,6 +161,8 @@ class GeneratedApproach:
  161    161          self.goal_bonus = 0.05
  162    162          self.overhead = 2.0
  163    163          self.wa = 0.6
         164 +        self.M = 8
         165 +        self.H2 = 30
  164    166          self.H = 40
  165    167          self.replan_every = 8
  166    168          self.model = None
@@ -169,6 +171,7 @@ class GeneratedApproach:
  169    171      def reset(self, state, info):
  170    172          s = np.asarray(state, dtype=float)
  171    173          self.w, self.lh, self.lv = s[12], s[13], s[14]
         174 +        self._cand_cache = {}
  172    175          self.model = TModel(self.w, self.lh, self.lv)
  173    176          self.sim = VModel(self.w, self.lh, self.lv)
  174    177          self.goal = s[29:32].copy()
@@ -192,8 +195,10 @@ class GeneratedApproach:
  192    195                  and abs(wrap(pose[2] - self.goal[2])) < math.radians(8))
  193    196  
  194    197      # ------------------------------------------------------------------
  195        -    def candidates(self, pose):
  196        -        """Candidate pushes: list of (start_pt_world, dir_world)."""
         198 +    def local_candidates(self, spacing, angs):
         199 +        key = (spacing, tuple(angs))
         200 +        if key in self._cand_cache:
         201 +            return self._cand_cache[key]
  197    202          poly = self.model.poly
  198    203          n = len(poly)
  199    204          starts, dirs = [], []
@@ -204,29 +209,37 @@ class GeneratedApproach:
  204    209              if L < 0.05:
  205    210                  continue
  206    211              nn = np.array([ab[1], -ab[0]]) / L
  207        -            m = max(2, int(L / 0.06))
  208        -            for t in np.linspace(0.04 / L, 1 - 0.04 / L, m) if L > 0.1 else [0.5]:
         212 +            m = max(2, int(L / spacing))
         213 +            for t in (np.linspace(0.04 / L, 1 - 0.04 / L, m) if L > 0.1 else [0.5]):
  209    214                  q = a + t * ab
  210        -                for ang in (-0.5, -0.25, 0.0, 0.25, 0.5):
         215 +                for ang in angs:
  211    216                      ca, sa = math.cos(ang), math.sin(ang)
  212    217                      d = -nn
  213    218                      d = np.array([ca * d[0] - sa * d[1], sa * d[0] + ca * d[1]])
  214    219                      starts.append(q + nn * (R_ROBOT + 0.02))
  215    220                      dirs.append(d)
  216        -        starts = np.array(starts)
  217        -        dirs = np.array(dirs)
  218        -        return to_world(starts, pose), to_world(dirs, (0, 0, pose[2]))
         221 +        res = (np.array(starts), np.array(dirs))
         222 +        self._cand_cache[key] = res
         223 +        return res
  219    224  
  220        -    def plan_push(self, pose, robot):
  221        -        sw, dw = self.candidates(pose)
  222        -        # extra candidates: push from current robot position if close to block
         225 +    def candidates(self, pose, coarse=False):
         226 +        if coarse:
         227 +            st, dr = self.local_candidates(0.12, (-0.4, 0.0, 0.4))
         228 +        else:
         229 +            st, dr = self.local_candidates(0.06, (-0.5, -0.25, 0.0, 0.25, 0.5))
         230 +        return to_world(st, pose), to_world(dr, (0, 0, pose[2]))
         231 +
         232 +    def eval_pushes(self, pose, robot, coarse=False, H=None):
         233 +        """Simulate all candidate pushes; return dict of arrays."""
         234 +        sw, dw = self.candidates(pose, coarse)
  223    235          dr = dist_to_T_local(to_local(robot[None], pose), self.model.rects)[0]
         236 +        nh = 12 if coarse else 24
  224    237          if dr < R_ROBOT + 0.06:
  225        -            angs = np.linspace(0, 2 * np.pi, 24, endpoint=False)
  226        -            sw = np.vstack([sw, np.repeat(robot[None], 24, 0)])
         238 +            angs = np.linspace(0, 2 * np.pi, nh, endpoint=False)
         239 +            sw = np.vstack([sw, np.repeat(robot[None], nh, 0)])
  227    240              dw = np.vstack([dw, np.stack([np.cos(angs), np.sin(angs)], 1)])
  228    241              here = np.zeros(len(sw), bool)
  229        -            here[-24:] = True
         242 +            here[-nh:] = True
  230    243          else:
  231    244              here = np.zeros(len(sw), bool)
  232    245          ok = np.all((sw > WALL_LO + R_ROBOT + 0.01) & (sw < WALL_HI - R_ROBOT - 0.01), 1)
@@ -237,24 +250,27 @@ class GeneratedApproach:
  237    250          ok &= np.all((pre > WALL_LO + R_ROBOT + 0.02) & (pre < WALL_HI - R_ROBOT - 0.02), 1)
  238    251          ok |= here
  239    252          sw, dw, pre, here = sw[ok], dw[ok], pre[ok], here[ok]
  240        -        c0 = self.cost(pose)[0]
  241        -        # speeds
  242        -        speeds = [MAXD] if c0 > 0.35 else [MAXD, 0.02]
         253 +        c0 = self.cost(pose[None])[0]
         254 +        speeds = [MAXD] if (c0 > 0.35 or coarse) else [MAXD, 0.02]
         255 +        ns = len(sw)
  243    256          SW = np.vstack([sw] * len(speeds))
  244    257          DW = np.vstack([dw] * len(speeds))
  245    258          PRE = np.vstack([pre] * len(speeds))
  246    259          HERE = np.concatenate([here] * len(speeds))
  247        -        SP = np.repeat(np.array(speeds), len(sw))
         260 +        SP = np.repeat(np.array(speeds), ns)
  248    261          N = len(SW)
  249        -        # travel estimate
  250    262          travel = np.where(HERE, 0.0, self.travel_est(robot, PRE, pose) + 0.12 / MAXD)
  251    263          cur = np.repeat(pose[None], N, 0)
  252    264          rob = SW.copy()
  253    265          bestscore = np.full(N, -np.inf)
  254    266          bestk = np.zeros(N, int)
  255        -        H = self.H
         267 +        bestpose = cur.copy()
         268 +        bestrob = rob.copy()
         269 +        bestc = np.full(N, c0)
         270 +        H = H or self.H
         271 +        act = DW * SP[:, None]
  256    272          for k in range(1, H + 1):
  257        -            cur, rob = self.sim.step(cur, rob, DW * SP[:, None])
         273 +            cur, rob = self.sim.step(cur, rob, act)
  258    274              cst = self.cost(cur)
  259    275              done = self.in_goal(cur, 0.75)
  260    276              cst = np.where(done, -self.goal_bonus, cst)
@@ -262,8 +278,36 @@ class GeneratedApproach:
  262    278              m = score > bestscore
  263    279              bestscore[m] = score[m]
  264    280              bestk[m] = k
  265        -        i = int(np.argmax(bestscore))
  266        -        return SW[i], DW[i] * SP[i], bestk[i], bestscore[i], c0, HERE[i]
         281 +            bestpose[m] = cur[m]
         282 +            bestrob[m] = rob[m]
         283 +            bestc[m] = cst[m]
         284 +        return dict(start=SW, act=act, k=bestk, rate=bestscore, pose=bestpose, rob=bestrob,
         285 +                    c=bestc, here=HERE, travel=travel, c0=c0)
         286 +
         287 +    def plan_push(self, pose, robot):
         288 +        E = self.eval_pushes(pose, robot)
         289 +        order = np.argsort(-E["rate"])
         290 +        best_i = int(order[0])
         291 +        if self.M > 0:
         292 +            best_T = np.inf
         293 +            for i in order[: self.M]:
         294 +                if E["rate"][i] <= 0:
         295 +                    break
         296 +                T1 = E["travel"][i] + E["k"][i]
         297 +                if E["c"][i] < 0:
         298 +                    T = T1
         299 +                else:
         300 +                    E2 = self.eval_pushes(E["pose"][i], E["rob"][i], coarse=True, H=self.H2)
         301 +                    j = int(np.argmax(E2["rate"]))
         302 +                    r2 = E2["rate"][j]
         303 +                    if r2 <= 0:
         304 +                        continue
         305 +                    T = T1 + (E2["c0"] + self.goal_bonus) / r2
         306 +                if T < best_T:
         307 +                    best_T = T
         308 +                    best_i = int(i)
         309 +        i = best_i
         310 +        return E["start"][i], E["act"][i], E["k"][i], E["rate"][i], E["c0"], E["here"][i]
  267    311  
  268    312      def in_goal(self, poses, frac=1.0):
  269    313          dp = np.abs(poses[:, :2] - self.goal[:2])
@@ -366,6 +410,9 @@ class GeneratedApproach:
  366    410                  self.stall = 0
  367    411                  self.mode = "plan"
  368    412          self.last_robot = robot
         413 +        if self.in_goal(pose[None])[0]:
         414 +            self.last_cmd = None
         415 +            return np.zeros(2)
  369    416          a = self._act(pose, robot)
  370    417          a = np.clip(np.asarray(a, float), -MAXD, MAXD)
  371    418          self.last_cmd = a
```

</details>

<a id="C011"></a>
### C011 · M=0

Commit `3c87638ed04cf56fd41a4122d2b22d84771ab82e`; parents: 8bfdcfcfe5a47cbda863abda8ef6b4b359bd5f23. Recorded author date: 2026-09-30T17:49:37+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0519](01_timeline.md#E0519): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_3c87638_approach.py) · [Exact all-file diff](evidence/diffs/C011_3c87638.diff)

[Previous saved controller snapshot](evidence/versions/C010_8bfdcfc_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 587cb0a..c84da94 100644
--- a/approach.py
+++ b/approach.py
@@ -161,7 +161,7 @@ class GeneratedApproach:
  161    161          self.goal_bonus = 0.05
  162    162          self.overhead = 2.0
  163    163          self.wa = 0.6
  164        -        self.M = 8
         164 +        self.M = 0
  165    165          self.H2 = 30
  166    166          self.H = 40
  167    167          self.replan_every = 8
diff --git a/dbg.py b/dbg.py
index b5d0511..4b3f62c 100644
--- a/dbg.py
+++ b/dbg.py
@@ -6,9 +6,10 @@ env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
    6      6  ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
    7      7  orig=ap.plan_push
    8      8  def pp(pose,robot):
    9        -    r=orig(pose,robot); print("PLAN pose",pose,"rob",robot,"cost %.3f score %.3f k %d here %d"%(r[4],r[3],r[2],r[5]), "start",r[0],"dir",r[1]); return r
           9 +    r=orig(pose,robot); print("PLAN pose",pose,"rob",robot,"cost %.3f score %.4f k %d here %d"%(r[4],r[3],r[2],r[5]), "start",r[0],"dir",r[1]); return r
   10     10  ap.plan_push=pp
   11     11  for i in range(int(sys.argv[2])):
   12     12      a=ap.get_action(obs)
   13     13      obs,r,te,tr,_=env.step(a)
   14     14      if te: print("DONE",i); break
          15 +print("goal", ap.goal)
```

</details>

<a id="C012"></a>
### C012 · visibility-graph travel estimate for all candidates

Commit `b0a3cf92e9121bcc682588780ee4f5ff0a23019f`; parents: 3c87638ed04cf56fd41a4122d2b22d84771ab82e. Recorded author date: 2026-09-30T17:51:14+02:00.

File roles (automatic): policy.

- [E0537](01_timeline.md#E0537): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_b0a3cf9_approach.py) · [Exact all-file diff](evidence/diffs/C012_b0a3cf9.diff)

[Previous saved controller snapshot](evidence/versions/C011_3c87638_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c84da94..f8a5abb 100644
--- a/approach.py
+++ b/approach.py
@@ -162,6 +162,7 @@ class GeneratedApproach:
  162    162          self.overhead = 2.0
  163    163          self.wa = 0.6
  164    164          self.M = 0
         165 +        self.infl = R_ROBOT + 0.03
  165    166          self.H2 = 30
  166    167          self.H = 40
  167    168          self.replan_every = 8
@@ -314,22 +315,73 @@ class GeneratedApproach:
  314    315          da = np.abs(wrap_arr(poses[:, 2] - self.goal[2]))
  315    316          return (dp[:, 0] < 0.03 * frac) & (dp[:, 1] < 0.03 * frac) & (da < math.radians(8) * frac)
  316    317  
         318 +    def _nodes(self, pose):
         319 +        infl = self.infl
         320 +        a, h, w, lv = self.lh / 2, self.w / 2, self.w, self.lv
         321 +        e = infl + 0.04
         322 +        nodes_local = np.array([
         323 +            [-a - e, e], [a + e, e], [a + e, -w - e], [-a - e, -w - e],
         324 +            [h + e, -w - e], [-h - e, -w - e], [h + e, -w - lv - e], [-h - e, -w - lv - e],
         325 +            [0, e + 0.02], [0, -w - lv - e - 0.02],
         326 +        ])
         327 +        nodes = to_world(nodes_local, pose)
         328 +        ok = np.all((nodes > WALL_LO + R_ROBOT + 0.01) & (nodes < WALL_HI - R_ROBOT - 0.01), 1)
         329 +        return nodes[ok]
         330 +
         331 +    def _seg_free(self, P, Q, pose, ns=24):
         332 +        """Vectorized: segments P[i]->Q[i] free of inflated T."""
         333 +        ts = np.linspace(0, 1, ns)
         334 +        pts = P[:, None, :] + ts[None, :, None] * (Q - P)[:, None, :]
         335 +        dd = dist_to_T_local(to_local(pts.reshape(-1, 2), pose), self.model.rects).reshape(len(P), ns)
         336 +        return np.all(dd > self.infl - 1e-6, 1)
         337 +
  317    338      def travel_est(self, robot, pts, pose):
  318        -        """Approximate travel steps from robot to each pt, detouring around block."""
         339 +        """Travel steps from robot to each pt via visibility graph around block."""
         340 +        nodes = self._nodes(pose)
         341 +        K = len(nodes)
         342 +        allp = np.vstack([robot[None], nodes])
         343 +        # graph among robot+nodes
         344 +        I, J = np.triu_indices(K + 1, 1)
         345 +        free = self._seg_free(allp[I], allp[J], pose)
         346 +        # allow robot escaping if robot starts inside inflation
         347 +        D = np.full((K + 1, K + 1), np.inf)
         348 +        L = np.hypot(*(allp[I] - allp[J]).T)
         349 +        D[I[free], J[free]] = L[free]
         350 +        D[J[free], I[free]] = L[free]
         351 +        r0 = dist_to_T_local(to_local(robot[None], pose), self.model.rects)[0]
         352 +        if r0 <= self.infl:
         353 +            # robot too close to block: allow direct moves to all nodes (escape)
         354 +            Ln = np.hypot(*(nodes - robot).T)
         355 +            D[0, 1:] = np.minimum(D[0, 1:], Ln * 1.2)
         356 +        dist = np.full(K + 1, np.inf)
         357 +        dist[0] = 0.0
         358 +        done = np.zeros(K + 1, bool)
         359 +        for _ in range(K + 1):
         360 +            u = int(np.argmin(np.where(done, np.inf, dist)))
         361 +            if not np.isfinite(dist[u]):
         362 +                break
         363 +            done[u] = True
         364 +            dist = np.minimum(dist, dist[u] + D[u])
         365 +        N = len(pts)
  319    366          direct = np.hypot(*(pts - robot).T)
  320        -        ts = np.linspace(0, 1, 12)
  321        -        seg = robot[None, None, :] + ts[None, :, None] * (pts - robot)[:, None, :]
  322        -        flat = seg.reshape(-1, 2)
  323        -        dd = dist_to_T_local(to_local(flat, pose), self.model.rects).reshape(len(pts), -1)
  324        -        blocked = dd.min(1) < R_ROBOT + 0.03
  325        -        cen = to_world(np.array([[0.0, -(self.w + self.lv) / 2]]), pose)[0]
  326        -        det = (np.hypot(*(robot - cen)) + np.hypot(*(pts - cen).T)) * 1.25
  327        -        return np.where(blocked, np.maximum(det, direct), direct) / MAXD
         367 +        dfree = self._seg_free(np.repeat(robot[None], N, 0), pts, pose)
         368 +        if r0 <= self.infl:
         369 +            dfree |= True  # handled by staging (robot adjacent) - approximate
         370 +        best = np.where(dfree, direct, np.inf)
         371 +        if K > 0:
         372 +            PP = np.repeat(nodes, N, 0)
         373 +            QQ = np.tile(pts, (K, 1))
         374 +            f = self._seg_free(PP, QQ, pose).reshape(K, N)
         375 +            dn = np.hypot(*(PP - QQ).T).reshape(K, N)
         376 +            via = np.where(f, dist[1:, None] + dn, np.inf).min(0)
         377 +            best = np.minimum(best, via)
         378 +        best = np.where(np.isfinite(best), best, direct * 2.5)
         379 +        return best / MAXD
  328    380  
  329    381      # ------------------------------------------------------------------
  330    382      def nav_path(self, robot, target, pose):
  331    383          """Visibility-graph path around inflated T."""
  332        -        infl = R_ROBOT + 0.03
         384 +        infl = self.infl
  333    385          rects = self.model.rects
  334    386  
  335    387          def free_seg(p, q):
@@ -340,17 +392,7 @@ class GeneratedApproach:
  340    392  
  341    393          if free_seg(robot, target):
  342    394              return [target]
  343        -        a, h = self.lh / 2, self.w / 2
  344        -        e = infl + 0.05
  345        -        lv = self.lv
  346        -        w = self.w
  347        -        nodes_local = np.array([
  348        -            [-a - e, e], [a + e, e], [a + e, -w - e], [-a - e, -w - e],
  349        -            [h + e, -w - e], [-h - e, -w - e], [h + e, -w - lv - e], [-h - e, -w - lv - e],
  350        -            [0, e], [0, -w - lv - e],
  351        -        ])
  352        -        nodes = list(to_world(nodes_local, pose))
  353        -        nodes = [p for p in nodes if np.all(p > WALL_LO + R_ROBOT + 0.01) and np.all(p < WALL_HI - R_ROBOT - 0.01)]
         395 +        nodes = list(self._nodes(pose))
  354    396          pts = [np.asarray(robot)] + nodes + [np.asarray(target)]
  355    397          n = len(pts)
  356    398          dist = [np.inf] * n
```

</details>

<a id="C013"></a>
### C013 · infl 0.115

Commit `6e77bfe199f52808652cae668d37893abf46dc96`; parents: b0a3cf92e9121bcc682588780ee4f5ff0a23019f. Recorded author date: 2026-09-30T17:51:55+02:00.

File roles (automatic): policy.

- [E0544](01_timeline.md#E0544): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_6e77bfe_approach.py) · [Exact all-file diff](evidence/diffs/C013_6e77bfe.diff)

[Previous saved controller snapshot](evidence/versions/C012_b0a3cf9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f8a5abb..6e93ab8 100644
--- a/approach.py
+++ b/approach.py
@@ -162,7 +162,7 @@ class GeneratedApproach:
  162    162          self.overhead = 2.0
  163    163          self.wa = 0.6
  164    164          self.M = 0
  165        -        self.infl = R_ROBOT + 0.03
         165 +        self.infl = R_ROBOT + 0.015
  166    166          self.H2 = 30
  167    167          self.H = 40
  168    168          self.replan_every = 8
```

</details>

<a id="C014"></a>
### C014 · wa=0.4, cost_mode option

Commit `e6da664c2e8554b6637659a76c5f4b27d9ac1e73`; parents: 6e77bfe199f52808652cae668d37893abf46dc96. Recorded author date: 2026-09-30T17:53:25+02:00.

File roles (automatic): policy.

- [E0557](01_timeline.md#E0557): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_e6da664_approach.py) · [Exact all-file diff](evidence/diffs/C014_e6da664.diff)

[Previous saved controller snapshot](evidence/versions/C013_6e77bfe_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6e93ab8..2b33e81 100644
--- a/approach.py
+++ b/approach.py
@@ -160,7 +160,8 @@ class GeneratedApproach:
  160    160          self.action_space = action_space
  161    161          self.goal_bonus = 0.05
  162    162          self.overhead = 2.0
  163        -        self.wa = 0.6
         163 +        self.wa = 0.4
         164 +        self.cost_mode = 0
  164    165          self.M = 0
  165    166          self.infl = R_ROBOT + 0.015
  166    167          self.H2 = 30
@@ -189,6 +190,8 @@ class GeneratedApproach:
  189    190          pose = np.atleast_2d(pose)
  190    191          dp = pose[:, :2] - self.goal[:2]
  191    192          da = np.abs(wrap_arr(pose[:, 2] - self.goal[2]))
         193 +        if self.cost_mode == 1:
         194 +            return np.sqrt(dp[:, 0] ** 2 + dp[:, 1] ** 2 + (self.wa * da) ** 2)
  192    195          return np.hypot(dp[:, 0], dp[:, 1]) + self.wa * da
  193    196  
  194    197      def solved(self, pose):
```

</details>

<a id="C015"></a>
### C015 · Use raw (unwrapped) angle error: env termination does not wrap theta

Commit `1fe8cd7be5ac6f2a16344a619a98a6ba7dd5cb7c`; parents: e6da664c2e8554b6637659a76c5f4b27d9ac1e73. Recorded author date: 2026-09-30T17:56:50+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0652](01_timeline.md#E0652): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_1fe8cd7_approach.py) · [Exact all-file diff](evidence/diffs/C015_1fe8cd7.diff)

[Previous saved controller snapshot](evidence/versions/C014_e6da664_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2b33e81..7939d33 100644
--- a/approach.py
+++ b/approach.py
@@ -189,14 +189,14 @@ class GeneratedApproach:
  189    189      def cost(self, pose):
  190    190          pose = np.atleast_2d(pose)
  191    191          dp = pose[:, :2] - self.goal[:2]
  192        -        da = np.abs(wrap_arr(pose[:, 2] - self.goal[2]))
         192 +        da = np.abs(pose[:, 2] - self.goal[2])
  193    193          if self.cost_mode == 1:
  194    194              return np.sqrt(dp[:, 0] ** 2 + dp[:, 1] ** 2 + (self.wa * da) ** 2)
  195    195          return np.hypot(dp[:, 0], dp[:, 1]) + self.wa * da
  196    196  
  197    197      def solved(self, pose):
  198    198          return (abs(pose[0] - self.goal[0]) < 0.03 and abs(pose[1] - self.goal[1]) < 0.03
  199        -                and abs(wrap(pose[2] - self.goal[2])) < math.radians(8))
         199 +                and abs(pose[2] - self.goal[2]) < math.radians(8))
  200    200  
  201    201      # ------------------------------------------------------------------
  202    202      def local_candidates(self, spacing, angs):
@@ -315,7 +315,7 @@ class GeneratedApproach:
  315    315  
  316    316      def in_goal(self, poses, frac=1.0):
  317    317          dp = np.abs(poses[:, :2] - self.goal[:2])
  318        -        da = np.abs(wrap_arr(poses[:, 2] - self.goal[2]))
         318 +        da = np.abs(poses[:, 2] - self.goal[2])
  319    319          return (dp[:, 0] < 0.03 * frac) & (dp[:, 1] < 0.03 * frac) & (da < math.radians(8) * frac)
  320    320  
  321    321      def _nodes(self, pose):
diff --git a/tune.py b/tune.py
index 3cdb96a..6d61f6c 100644
--- a/tune.py
+++ b/tune.py
@@ -17,6 +17,7 @@ def run(seed):
   17     17          obs, r, term, trunc, _ = env.step(np.clip(ap.get_action(obs), -0.049, 0.049))
   18     18          if term or trunc: break
   19     19      env.close()
          20 +    if not term: print("FAIL", seed, obs[0:3]-obs[29:32], flush=True)
   20     21      return term, steps, time.time()-t0
   21     22  if __name__ == "__main__":
   22     23      a, b = int(sys.argv[1]), int(sys.argv[2])
```

</details>

<a id="C016"></a>
### C016 · Wall-aware push validity, push stall detection, time guard

Commit `515fcbff7c63a0c8763c0b2723dbd433064d382c`; parents: 1fe8cd7be5ac6f2a16344a619a98a6ba7dd5cb7c. Recorded author date: 2026-09-30T17:59:58+02:00.

File roles (automatic): policy.

- [E0672](01_timeline.md#E0672): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_515fcbf_approach.py) · [Exact all-file diff](evidence/diffs/C016_515fcbf.diff)

[Previous saved controller snapshot](evidence/versions/C015_1fe8cd7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7939d33..8328960 100644
--- a/approach.py
+++ b/approach.py
@@ -1,5 +1,6 @@
    1      1  """Push-T controller: model-based greedy push selection + visibility-graph navigation."""
    2      2  import heapq
           3 +import time
    3      4  import math
    4      5  
    5      6  import numpy as np
@@ -164,6 +165,7 @@ class GeneratedApproach:
  164    165          self.cost_mode = 0
  165    166          self.M = 0
  166    167          self.infl = R_ROBOT + 0.015
         168 +        self.wall_margin = 0.01
  167    169          self.H2 = 30
  168    170          self.H = 40
  169    171          self.replan_every = 8
@@ -174,6 +176,7 @@ class GeneratedApproach:
  174    176          s = np.asarray(state, dtype=float)
  175    177          self.w, self.lh, self.lv = s[12], s[13], s[14]
  176    178          self._cand_cache = {}
         179 +        self.t0 = time.time()
  177    180          self.model = TModel(self.w, self.lh, self.lv)
  178    181          self.sim = VModel(self.w, self.lh, self.lv)
  179    182          self.goal = s[29:32].copy()
@@ -273,12 +276,22 @@ class GeneratedApproach:
  273    276          bestc = np.full(N, c0)
  274    277          H = H or self.H
  275    278          act = DW * SP[:, None]
         279 +        valid = np.ones(N, bool)
         280 +        poly = self.model.poly
  276    281          for k in range(1, H + 1):
  277    282              cur, rob = self.sim.step(cur, rob, act)
         283 +            # wall check: all T vertices must stay inside the arena
         284 +            c, s_ = np.cos(cur[:, 2]), np.sin(cur[:, 2])
         285 +            vx = cur[:, 0:1] + c[:, None] * poly[None, :, 0] - s_[:, None] * poly[None, :, 1]
         286 +            vy = cur[:, 1:2] + s_[:, None] * poly[None, :, 0] + c[:, None] * poly[None, :, 1]
         287 +            m_ = self.wall_margin
         288 +            inside = ((vx.min(1) > m_) & (vx.max(1) < 5.0 - m_) & (vy.min(1) > m_) & (vy.max(1) < 5.0 - m_))
         289 +            valid &= inside
  278    290              cst = self.cost(cur)
  279    291              done = self.in_goal(cur, 0.75)
  280    292              cst = np.where(done, -self.goal_bonus, cst)
  281    293              score = (c0 - cst) / (k + travel + self.overhead)
         294 +            score = np.where(valid, score, -np.inf)
  282    295              m = score > bestscore
  283    296              bestscore[m] = score[m]
  284    297              bestk[m] = k
@@ -289,7 +302,11 @@ class GeneratedApproach:
  289    302                      c=bestc, here=HERE, travel=travel, c0=c0)
  290    303  
  291    304      def plan_push(self, pose, robot):
  292        -        E = self.eval_pushes(pose, robot)
         305 +        el = time.time() - self.t0
         306 +        if el > 35.0:
         307 +            E = self.eval_pushes(pose, robot, coarse=True, H=20 if el > 45 else 30)
         308 +        else:
         309 +            E = self.eval_pushes(pose, robot)
  293    310          order = np.argsort(-E["rate"])
  294    311          best_i = int(order[0])
  295    312          if self.M > 0:
@@ -445,6 +462,10 @@ class GeneratedApproach:
  445    462          robot = s[16:18].copy()
  446    463          if self.model is None:
  447    464              self.reset(state, {})
         465 +        if self.last_cmd is not None and self.mode == "push":
         466 +            moved = np.linalg.norm(robot - self.last_robot)
         467 +            if moved < 0.3 * np.linalg.norm(self.last_cmd):
         468 +                self.mode = "plan"
  448    469          if self.last_cmd is not None and self.mode == "nav":
  449    470              moved = np.linalg.norm(robot - self.last_robot)
  450    471              if moved < 0.3 * np.linalg.norm(self.last_cmd) and np.linalg.norm(self.last_cmd) > 1e-3:
```

</details>

<a id="C017"></a>
### C017 · Angle target: centre of the valid wrapped interval (env compares wrapped theta without wrapping diff)

Commit `a5e6da0e17e06d8c740632bbb7f7cb5dbc2fdeca`; parents: 515fcbff7c63a0c8763c0b2723dbd433064d382c. Recorded author date: 2026-09-30T18:02:44+02:00.

File roles (automatic): policy.

- [E0690](01_timeline.md#E0690): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_a5e6da0_approach.py) · [Exact all-file diff](evidence/diffs/C017_a5e6da0.diff)

[Previous saved controller snapshot](evidence/versions/C016_515fcbf_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8328960..c7575e8 100644
--- a/approach.py
+++ b/approach.py
@@ -180,6 +180,11 @@ class GeneratedApproach:
  180    180          self.model = TModel(self.w, self.lh, self.lv)
  181    181          self.sim = VModel(self.w, self.lh, self.lv)
  182    182          self.goal = s[29:32].copy()
         183 +        tol = math.radians(8) - 0.004
         184 +        lo = max(self.goal[2] - tol, -math.pi)
         185 +        hi = min(self.goal[2] + tol, math.pi)
         186 +        self.gc = 0.5 * (lo + hi)   # centre of the valid (wrapped) angle interval
         187 +        self.ghw = 0.5 * (hi - lo)
  183    188          self.mode = "plan"
  184    189          self.path = []
  185    190          self.push = None
@@ -192,14 +197,14 @@ class GeneratedApproach:
  192    197      def cost(self, pose):
  193    198          pose = np.atleast_2d(pose)
  194    199          dp = pose[:, :2] - self.goal[:2]
  195        -        da = np.abs(pose[:, 2] - self.goal[2])
         200 +        da = np.abs(wrap_arr(pose[:, 2] - self.gc))
  196    201          if self.cost_mode == 1:
  197    202              return np.sqrt(dp[:, 0] ** 2 + dp[:, 1] ** 2 + (self.wa * da) ** 2)
  198    203          return np.hypot(dp[:, 0], dp[:, 1]) + self.wa * da
  199    204  
  200    205      def solved(self, pose):
  201    206          return (abs(pose[0] - self.goal[0]) < 0.03 and abs(pose[1] - self.goal[1]) < 0.03
  202        -                and abs(pose[2] - self.goal[2]) < math.radians(8))
         207 +                and abs(wrap(pose[2] - self.gc)) < self.ghw)
  203    208  
  204    209      # ------------------------------------------------------------------
  205    210      def local_candidates(self, spacing, angs):
@@ -332,8 +337,8 @@ class GeneratedApproach:
  332    337  
  333    338      def in_goal(self, poses, frac=1.0):
  334    339          dp = np.abs(poses[:, :2] - self.goal[:2])
  335        -        da = np.abs(poses[:, 2] - self.goal[2])
  336        -        return (dp[:, 0] < 0.03 * frac) & (dp[:, 1] < 0.03 * frac) & (da < math.radians(8) * frac)
         340 +        da = np.abs(wrap_arr(poses[:, 2] - self.gc))
         341 +        return (dp[:, 0] < 0.03 * frac) & (dp[:, 1] < 0.03 * frac) & (da < self.ghw * frac)
  337    342  
  338    343      def _nodes(self, pose):
  339    344          infl = self.infl
```

</details>

<a id="C018"></a>
### C018 · Push blacklist on stall/model mismatch; wall-clearance subgoal when stuck

Commit `daa2253857dbb780361958de7f5364cd3527cb1a`; parents: a5e6da0e17e06d8c740632bbb7f7cb5dbc2fdeca. Recorded author date: 2026-09-30T18:08:44+02:00.

File roles (automatic): policy.

- [E0736](01_timeline.md#E0736): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_daa2253_approach.py) · [Exact all-file diff](evidence/diffs/C018_daa2253.diff)

[Previous saved controller snapshot](evidence/versions/C017_a5e6da0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c7575e8..1528ee2 100644
--- a/approach.py
+++ b/approach.py
@@ -166,6 +166,8 @@ class GeneratedApproach:
  166    166          self.M = 0
  167    167          self.infl = R_ROBOT + 0.015
  168    168          self.wall_margin = 0.01
         169 +        self.stuck_rate = 1e-3
         170 +        self.sub_clear = 1.0
  169    171          self.H2 = 30
  170    172          self.H = 40
  171    173          self.replan_every = 8
@@ -185,6 +187,9 @@ class GeneratedApproach:
  185    187          hi = min(self.goal[2] + tol, math.pi)
  186    188          self.gc = 0.5 * (lo + hi)   # centre of the valid (wrapped) angle interval
  187    189          self.ghw = 0.5 * (hi - lo)
         190 +        self.real_tgt = np.array([self.goal[0], self.goal[1], self.gc, self.ghw, 0.03])
         191 +        self.tgt = self.real_tgt.copy()
         192 +        self.sub_active = False
  188    193          self.mode = "plan"
  189    194          self.path = []
  190    195          self.push = None
@@ -192,12 +197,15 @@ class GeneratedApproach:
  192    197          self.stall = 0
  193    198          self.last_cmd = None
  194    199          self.last_robot = None
         200 +        self.last_pose = None
         201 +        self.blacklist = []
         202 +        self.bl_pose = None
  195    203  
  196    204      # ------------------------------------------------------------------
  197    205      def cost(self, pose):
  198    206          pose = np.atleast_2d(pose)
  199        -        dp = pose[:, :2] - self.goal[:2]
  200        -        da = np.abs(wrap_arr(pose[:, 2] - self.gc))
         207 +        dp = pose[:, :2] - self.tgt[:2]
         208 +        da = np.abs(wrap_arr(pose[:, 2] - self.tgt[2]))
  201    209          if self.cost_mode == 1:
  202    210              return np.sqrt(dp[:, 0] ** 2 + dp[:, 1] ** 2 + (self.wa * da) ** 2)
  203    211          return np.hypot(dp[:, 0], dp[:, 1]) + self.wa * da
@@ -261,6 +269,14 @@ class GeneratedApproach:
  261    269          ok &= (ds > R_ROBOT + 0.005) & (dp > R_ROBOT + 0.035)
  262    270          ok &= np.all((pre > WALL_LO + R_ROBOT + 0.02) & (pre < WALL_HI - R_ROBOT - 0.02), 1)
  263    271          ok |= here
         272 +        if self.blacklist:
         273 +            sl = to_local(sw, pose)
         274 +            dl = to_local(dw, (0, 0, pose[2]))
         275 +            for (bp, bd) in self.blacklist:
         276 +                bdn = bd / (np.linalg.norm(bd) + 1e-9)
         277 +                near = np.hypot(*(sl - bp).T) < 0.12
         278 +                same = (dl @ bdn) > 0.8
         279 +                ok &= ~(near & same)
  264    280          sw, dw, pre, here = sw[ok], dw[ok], pre[ok], here[ok]
  265    281          c0 = self.cost(pose[None])[0]
  266    282          speeds = [MAXD] if (c0 > 0.35 or coarse) else [MAXD, 0.02]
@@ -335,10 +351,30 @@ class GeneratedApproach:
  335    351          i = best_i
  336    352          return E["start"][i], E["act"][i], E["k"][i], E["rate"][i], E["c0"], E["here"][i]
  337    353  
         354 +    def make_subgoal(self, pose):
         355 +        """Goal orientation at a position with the COM clamped away from the walls."""
         356 +        th = self.gc
         357 +        c, s_ = math.cos(th), math.sin(th)
         358 +        com = self.sim.com
         359 +        gcom = self.goal[:2] + np.array([c * com[0] - s_ * com[1], s_ * com[0] + c * com[1]])
         360 +        m = self.sub_clear
         361 +        ncom = np.clip(gcom, m, 5.0 - m)
         362 +        if np.linalg.norm(ncom - gcom) < 0.05:
         363 +            # goal is interior: use current COM pulled toward centre
         364 +            cc, sc_ = math.cos(pose[2]), math.sin(pose[2])
         365 +            pcom = pose[:2] + np.array([cc * com[0] - sc_ * com[1], sc_ * com[0] + cc * com[1]])
         366 +            ncom = np.clip(pcom, m, 5.0 - m)
         367 +            if np.linalg.norm(ncom - pcom) < 0.05:
         368 +                return None
         369 +            xy = ncom - np.array([cc * com[0] - sc_ * com[1], sc_ * com[0] + cc * com[1]])
         370 +            return np.array([xy[0], xy[1], pose[2], 0.3, 0.08])
         371 +        xy = self.goal[:2] + (ncom - gcom)
         372 +        return np.array([xy[0], xy[1], th, 0.1, 0.1])
         373 +
  338    374      def in_goal(self, poses, frac=1.0):
  339        -        dp = np.abs(poses[:, :2] - self.goal[:2])
  340        -        da = np.abs(wrap_arr(poses[:, 2] - self.gc))
  341        -        return (dp[:, 0] < 0.03 * frac) & (dp[:, 1] < 0.03 * frac) & (da < self.ghw * frac)
         375 +        dp = np.abs(poses[:, :2] - self.tgt[:2])
         376 +        da = np.abs(wrap_arr(poses[:, 2] - self.tgt[2]))
         377 +        return (dp[:, 0] < self.tgt[4] * frac) & (dp[:, 1] < self.tgt[4] * frac) & (da < self.tgt[3] * frac)
  342    378  
  343    379      def _nodes(self, pose):
  344    380          infl = self.infl
@@ -467,10 +503,21 @@ class GeneratedApproach:
  467    503          robot = s[16:18].copy()
  468    504          if self.model is None:
  469    505              self.reset(state, {})
         506 +        # clear blacklist once block moved noticeably
         507 +        if self.bl_pose is not None and (np.linalg.norm(pose[:2] - self.bl_pose[:2]) > 0.03
         508 +                                         or abs(wrap(pose[2] - self.bl_pose[2])) > 0.05):
         509 +            self.blacklist = []
         510 +            self.bl_pose = None
  470    511          if self.last_cmd is not None and self.mode == "push":
  471    512              moved = np.linalg.norm(robot - self.last_robot)
  472        -            if moved < 0.3 * np.linalg.norm(self.last_cmd):
         513 +            pred_pose, _ = self.sim.step(self.last_pose, self.last_robot, self.last_cmd)
         514 +            perr = np.linalg.norm(pred_pose[0, :2] - pose[:2]) + 0.5 * abs(wrap(pred_pose[0, 2] - pose[2]))
         515 +            if moved < 0.3 * np.linalg.norm(self.last_cmd) or perr > 0.01:
  473    516                  self.mode = "plan"
         517 +                self.blacklist.append((to_local(self.last_robot[None], pose)[0],
         518 +                                       to_local(self.last_cmd[None], (0, 0, pose[2]))[0]))
         519 +                if self.bl_pose is None:
         520 +                    self.bl_pose = pose.copy()
  474    521          if self.last_cmd is not None and self.mode == "nav":
  475    522              moved = np.linalg.norm(robot - self.last_robot)
  476    523              if moved < 0.3 * np.linalg.norm(self.last_cmd) and np.linalg.norm(self.last_cmd) > 1e-3:
@@ -481,9 +528,14 @@ class GeneratedApproach:
  481    528                  self.stall = 0
  482    529                  self.mode = "plan"
  483    530          self.last_robot = robot
  484        -        if self.in_goal(pose[None])[0]:
         531 +        self.last_pose = pose.copy()
         532 +        if self.solved(pose):
  485    533              self.last_cmd = None
  486    534              return np.zeros(2)
         535 +        if self.sub_active and self.in_goal(pose[None])[0]:
         536 +            self.sub_active = False
         537 +            self.tgt = self.real_tgt.copy()
         538 +            self.mode = "plan"
  487    539          a = self._act(pose, robot)
  488    540          a = np.clip(np.asarray(a, float), -MAXD, MAXD)
  489    541          self.last_cmd = a
@@ -493,6 +545,16 @@ class GeneratedApproach:
  493    545          for _ in range(4):
  494    546              if self.mode == "plan":
  495    547                  st, d, k, sc, c0, here = self.plan_push(pose, robot)
         548 +                if sc < self.stuck_rate and not self.sub_active:
         549 +                    sub = self.make_subgoal(pose)
         550 +                    if sub is not None:
         551 +                        self.sub_active = True
         552 +                        self.tgt = sub
         553 +                        st, d, k, sc, c0, here = self.plan_push(pose, robot)
         554 +                elif sc < self.stuck_rate and self.sub_active:
         555 +                    self.sub_active = False
         556 +                    self.tgt = self.real_tgt.copy()
         557 +                    st, d, k, sc, c0, here = self.plan_push(pose, robot)
  496    558                  self.push = (st, d)
  497    559                  self.push_left = min(k, self.replan_every)
  498    560                  dn = d / np.linalg.norm(d)
```

</details>

<a id="C019"></a>
### C019 · Direct approach to push start (no staging), pre_clear param

Commit `8730159dc0c7b23faec8e136d0dd6cad90d02c74`; parents: daa2253857dbb780361958de7f5364cd3527cb1a. Recorded author date: 2026-09-30T18:14:02+02:00.

File roles (automatic): policy.

- [E0765](01_timeline.md#E0765): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_8730159_approach.py) · [Exact all-file diff](evidence/diffs/C019_8730159.diff)

[Previous saved controller snapshot](evidence/versions/C018_daa2253_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1528ee2..e6506f5 100644
--- a/approach.py
+++ b/approach.py
@@ -167,6 +167,9 @@ class GeneratedApproach:
  167    167          self.infl = R_ROBOT + 0.015
  168    168          self.wall_margin = 0.01
  169    169          self.stuck_rate = 1e-3
         170 +        self.stage = 0
         171 +        self.pre_clear = 0.035
         172 +        self.final_infl = R_ROBOT + 0.008
  170    173          self.sub_clear = 1.0
  171    174          self.H2 = 30
  172    175          self.H = 40
@@ -266,7 +269,7 @@ class GeneratedApproach:
  266    269          pre = sw - dw * 0.12
  267    270          ds = dist_to_T_local(to_local(sw, pose), self.model.rects)
  268    271          dp = dist_to_T_local(to_local(pre, pose), self.model.rects)
  269        -        ok &= (ds > R_ROBOT + 0.005) & (dp > R_ROBOT + 0.035)
         272 +        ok &= (ds > R_ROBOT + 0.005) & (dp > R_ROBOT + self.pre_clear)
  270    273          ok &= np.all((pre > WALL_LO + R_ROBOT + 0.02) & (pre < WALL_HI - R_ROBOT - 0.02), 1)
  271    274          ok |= here
  272    275          if self.blacklist:
@@ -287,7 +290,10 @@ class GeneratedApproach:
  287    290          HERE = np.concatenate([here] * len(speeds))
  288    291          SP = np.repeat(np.array(speeds), ns)
  289    292          N = len(SW)
  290        -        travel = np.where(HERE, 0.0, self.travel_est(robot, PRE, pose) + 0.12 / MAXD)
         293 +        if self.stage:
         294 +            travel = np.where(HERE, 0.0, self.travel_est(robot, PRE, pose) + 0.12 / MAXD)
         295 +        else:
         296 +            travel = np.where(HERE, 0.0, self.travel_est(robot, SW, pose))
  291    297          cur = np.repeat(pose[None], N, 0)
  292    298          rob = SW.copy()
  293    299          bestscore = np.full(N, -np.inf)
@@ -389,12 +395,13 @@ class GeneratedApproach:
  389    395          ok = np.all((nodes > WALL_LO + R_ROBOT + 0.01) & (nodes < WALL_HI - R_ROBOT - 0.01), 1)
  390    396          return nodes[ok]
  391    397  
  392        -    def _seg_free(self, P, Q, pose, ns=24):
         398 +    def _seg_free(self, P, Q, pose, ns=24, infl=None):
  393    399          """Vectorized: segments P[i]->Q[i] free of inflated T."""
         400 +        infl = self.infl if infl is None else infl
  394    401          ts = np.linspace(0, 1, ns)
  395    402          pts = P[:, None, :] + ts[None, :, None] * (Q - P)[:, None, :]
  396    403          dd = dist_to_T_local(to_local(pts.reshape(-1, 2), pose), self.model.rects).reshape(len(P), ns)
  397        -        return np.all(dd > self.infl - 1e-6, 1)
         404 +        return np.all(dd > infl - 1e-6, 1)
  398    405  
  399    406      def travel_est(self, robot, pts, pose):
  400    407          """Travel steps from robot to each pt via visibility graph around block."""
@@ -425,14 +432,15 @@ class GeneratedApproach:
  425    432              dist = np.minimum(dist, dist[u] + D[u])
  426    433          N = len(pts)
  427    434          direct = np.hypot(*(pts - robot).T)
  428        -        dfree = self._seg_free(np.repeat(robot[None], N, 0), pts, pose)
         435 +        tinf = self.final_infl if self.stage == 0 else self.infl
         436 +        dfree = self._seg_free(np.repeat(robot[None], N, 0), pts, pose, infl=tinf)
  429    437          if r0 <= self.infl:
  430    438              dfree |= True  # handled by staging (robot adjacent) - approximate
  431    439          best = np.where(dfree, direct, np.inf)
  432    440          if K > 0:
  433    441              PP = np.repeat(nodes, N, 0)
  434    442              QQ = np.tile(pts, (K, 1))
  435        -            f = self._seg_free(PP, QQ, pose).reshape(K, N)
         443 +            f = self._seg_free(PP, QQ, pose, infl=tinf).reshape(K, N)
  436    444              dn = np.hypot(*(PP - QQ).T).reshape(K, N)
  437    445              via = np.where(f, dist[1:, None] + dn, np.inf).min(0)
  438    446              best = np.minimum(best, via)
@@ -445,13 +453,15 @@ class GeneratedApproach:
  445    453          infl = self.infl
  446    454          rects = self.model.rects
  447    455  
  448        -        def free_seg(p, q):
         456 +        tinf = self.final_infl
         457 +
         458 +        def free_seg(p, q, tol=infl):
  449    459              pl = to_local(np.array([p, q]), pose)
  450    460              ts = np.linspace(0, 1, max(2, int(np.linalg.norm(q - p) / 0.02) + 2))
  451    461              pts = pl[0] + ts[:, None] * (pl[1] - pl[0])
  452        -            return np.all(dist_to_T_local(pts, rects) > infl - 1e-6)
         462 +            return np.all(dist_to_T_local(pts, rects) > tol - 1e-6)
  453    463  
  454        -        if free_seg(robot, target):
         464 +        if free_seg(robot, target, tinf):
  455    465              return [target]
  456    466          nodes = list(self._nodes(pose))
  457    467          pts = [np.asarray(robot)] + nodes + [np.asarray(target)]
@@ -469,7 +479,8 @@ class GeneratedApproach:
  469    479              for v in range(n):
  470    480                  if v == u:
  471    481                      continue
  472        -                if not free_seg(pts[u], pts[v]) and not (u == 0 and self._escape_ok(pts[u], pts[v], pose)):
         482 +                tol = tinf if v == n - 1 else infl
         483 +                if not free_seg(pts[u], pts[v], tol) and not (u == 0 and self._escape_ok(pts[u], pts[v], pose)):
  473    484                      continue
  474    485                  nd = d + np.linalg.norm(pts[v] - pts[u])
  475    486                  if nd < dist[v]:
@@ -561,7 +572,10 @@ class GeneratedApproach:
  561    572                  if here:
  562    573                      self.path = []
  563    574                  else:
  564        -                    self.path = self.nav_path(robot, st - dn * 0.12, pose) + [st]
         575 +                    if self.stage:
         576 +                        self.path = self.nav_path(robot, st - dn * 0.12, pose) + [st]
         577 +                    else:
         578 +                        self.path = self.nav_path(robot, st, pose)
  565    579                  self.plan_pose = pose.copy()
  566    580                  self.mode = "nav"
  567    581              if self.mode == "nav":
```

</details>

<a id="C020"></a>
### C020 · la_mode, candidate params

Commit `8e82a4d155d0524a03d3f330c3efad778dda3dba`; parents: 8730159dc0c7b23faec8e136d0dd6cad90d02c74. Recorded author date: 2026-09-30T18:15:52+02:00.

File roles (automatic): policy.

- [E0784](01_timeline.md#E0784): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_8e82a4d_approach.py) · [Exact all-file diff](evidence/diffs/C020_8e82a4d.diff)

[Previous saved controller snapshot](evidence/versions/C019_8730159_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e6506f5..659eedc 100644
--- a/approach.py
+++ b/approach.py
@@ -168,6 +168,10 @@ class GeneratedApproach:
  168    168          self.wall_margin = 0.01
  169    169          self.stuck_rate = 1e-3
  170    170          self.stage = 0
         171 +        self.spacing = 0.06
         172 +        self.angs = (-0.5, -0.25, 0.0, 0.25, 0.5)
         173 +        self.la_mode = 1
         174 +        self.rbar = 0.03
  171    175          self.pre_clear = 0.035
  172    176          self.final_infl = R_ROBOT + 0.008
  173    177          self.sub_clear = 1.0
@@ -249,7 +253,7 @@ class GeneratedApproach:
  249    253          if coarse:
  250    254              st, dr = self.local_candidates(0.12, (-0.4, 0.0, 0.4))
  251    255          else:
  252        -            st, dr = self.local_candidates(0.06, (-0.5, -0.25, 0.0, 0.25, 0.5))
         256 +            st, dr = self.local_candidates(self.spacing, self.angs)
  253    257          return to_world(st, pose), to_world(dr, (0, 0, pose[2]))
  254    258  
  255    259      def eval_pushes(self, pose, robot, coarse=False, H=None):
@@ -346,11 +350,15 @@ class GeneratedApproach:
  346    350                      T = T1
  347    351                  else:
  348    352                      E2 = self.eval_pushes(E["pose"][i], E["rob"][i], coarse=True, H=self.H2)
  349        -                    j = int(np.argmax(E2["rate"]))
  350        -                    r2 = E2["rate"][j]
  351        -                    if r2 <= 0:
  352        -                        continue
  353        -                    T = T1 + (E2["c0"] + self.goal_bonus) / r2
         353 +                    if self.la_mode == 0:
         354 +                        j = int(np.argmax(E2["rate"]))
         355 +                        r2 = E2["rate"][j]
         356 +                        if r2 <= 0:
         357 +                            continue
         358 +                        T = T1 + (E2["c0"] + self.goal_bonus) / r2
         359 +                    else:
         360 +                        T2 = E2["travel"] + E2["k"] + np.maximum(E2["c"], 0) / self.rbar
         361 +                        T = T1 + min(T2.min(), E2["c0"] / self.rbar)
  354    362                  if T < best_T:
  355    363                      best_T = T
  356    364                      best_i = int(i)
```

</details>

<a id="C021"></a>
### C021 · wider push angles, tighter final approach

Commit `a5e1d82c18edb50573724c16d53d700427c0b8b6`; parents: 8e82a4d155d0524a03d3f330c3efad778dda3dba. Recorded author date: 2026-09-30T18:18:09+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0799](01_timeline.md#E0799): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_a5e1d82_approach.py) · [Exact all-file diff](evidence/diffs/C021_a5e1d82.diff)

[Previous saved controller snapshot](evidence/versions/C020_8e82a4d_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 659eedc..6c95e3e 100644
--- a/approach.py
+++ b/approach.py
@@ -169,11 +169,11 @@ class GeneratedApproach:
  169    169          self.stuck_rate = 1e-3
  170    170          self.stage = 0
  171    171          self.spacing = 0.06
  172        -        self.angs = (-0.5, -0.25, 0.0, 0.25, 0.5)
         172 +        self.angs = (-0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75)
  173    173          self.la_mode = 1
  174    174          self.rbar = 0.03
  175        -        self.pre_clear = 0.035
  176        -        self.final_infl = R_ROBOT + 0.008
         175 +        self.pre_clear = -0.1
         176 +        self.final_infl = R_ROBOT + 0.004
  177    177          self.sub_clear = 1.0
  178    178          self.H2 = 30
  179    179          self.H = 40
diff --git a/tune.py b/tune.py
index 6d61f6c..d358788 100644
--- a/tune.py
+++ b/tune.py
@@ -17,6 +17,7 @@ def run(seed):
   17     17          obs, r, term, trunc, _ = env.step(np.clip(ap.get_action(obs), -0.049, 0.049))
   18     18          if term or trunc: break
   19     19      env.close()
          20 +    if time.time()-t0 > 10: print("SLOW", seed, steps, time.time()-t0, flush=True)
   20     21      if not term: print("FAIL", seed, obs[0:3]-obs[29:32], flush=True)
   21     22      return term, steps, time.time()-t0
   22     23  if __name__ == "__main__":
```

</details>

<a id="C022"></a>
### C022 · add debug scripts/data

Commit `26c067613f9fab4446012250b059eebc35b89165`; parents: a5e1d82c18edb50573724c16d53d700427c0b8b6. Recorded author date: 2026-09-30T18:21:11+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E0830](01_timeline.md#E0830): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C022_26c0676.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/data_0.npz b/data_0.npz
new file mode 100644
index 0000000..5b56b1f
Binary files /dev/null and b/data_0.npz differ
diff --git a/data_1.npz b/data_1.npz
new file mode 100644
index 0000000..d954406
Binary files /dev/null and b/data_1.npz differ
diff --git a/data_2.npz b/data_2.npz
new file mode 100644
index 0000000..a60dd98
Binary files /dev/null and b/data_2.npz differ
diff --git a/data_3.npz b/data_3.npz
new file mode 100644
index 0000000..0c3f9f1
Binary files /dev/null and b/data_3.npz differ
diff --git a/data_4.npz b/data_4.npz
new file mode 100644
index 0000000..60b4496
Binary files /dev/null and b/data_4.npz differ
diff --git a/data_5.npz b/data_5.npz
new file mode 100644
index 0000000..99edee9
Binary files /dev/null and b/data_5.npz differ
diff --git a/data_6.npz b/data_6.npz
new file mode 100644
index 0000000..8fe6b55
Binary files /dev/null and b/data_6.npz differ
diff --git a/data_7.npz b/data_7.npz
new file mode 100644
index 0000000..fb58e4a
Binary files /dev/null and b/data_7.npz differ
diff --git a/dbg5.py b/dbg5.py
new file mode 100644
index 0000000..db5a6c2
--- /dev/null
+++ b/dbg5.py
@@ -0,0 +1,3 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env(); obs,_=env.reset(seed=38); print(obs[29:32])
diff --git a/dbg6.py b/dbg6.py
new file mode 100644
index 0000000..dc343e5
--- /dev/null
+++ b/dbg6.py
@@ -0,0 +1,11 @@
           1 +import numpy as np, sys
           2 +from env_client import make_env
           3 +from approach import *
           4 +np.set_printoptions(precision=4, suppress=True)
           5 +env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
           6 +ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
           7 +for i in range(1000):
           8 +    a=ap.get_action(obs)
           9 +    obs,r,te,tr,_=env.step(a)
          10 +    if i>int(sys.argv[2]): print(i, ap.mode, obs[[0,1,2,16,17]]-np.r_[obs[29:32],0,0], te)
          11 +    if te: break
diff --git a/dbg7.py b/dbg7.py
new file mode 100644
index 0000000..7348358
--- /dev/null
+++ b/dbg7.py
@@ -0,0 +1,15 @@
           1 +import numpy as np, sys
           2 +from env_client import make_env
           3 +from approach import *
           4 +np.set_printoptions(precision=3, suppress=True)
           5 +env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
           6 +ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
           7 +prev=None
           8 +for i in range(1000):
           9 +    m0=ap.mode
          10 +    a=ap.get_action(obs)
          11 +    if ap.mode=="nav" and m0!="nav":
          12 +        L=sum(np.linalg.norm(np.diff(np.vstack([obs[16:18]]+ap.path),axis=0),axis=1))
          13 +        print(i,"NAV start rob",obs[16:18],"path",np.round(np.array(ap.path),2).tolist(),"len %.2f steps %.0f"%(L,L/0.049), "pose",obs[0:3])
          14 +    obs,r,te,tr,_=env.step(a)
          15 +    if te: print("done",i); break
diff --git a/res.txt b/res.txt
new file mode 100644
index 0000000..77f495c
--- /dev/null
+++ b/res.txt
@@ -0,0 +1,41 @@
           1 +0 True 139 2.9s [0.013 0.008 0.025]
           2 +1 True 159 3.3s [0.016 0.003 0.069]
           3 +2 True 127 2.6s [0.019 0.019 0.033]
           4 +3 True 108 2.0s [0.017 0.007 0.062]
           5 +4 True 132 2.3s [0.016 0.006 0.064]
           6 +5 True 140 3.3s [0.01  0.013 0.079]
           7 +6 True 169 3.5s [0.013 0.006 0.05 ]
           8 +7 True 193 3.7s [0.011 0.015 0.014]
           9 +8 True 152 3.0s [0.007 0.018 0.01 ]
          10 +9 True 160 2.2s [0.008 0.006 0.1  ]
          11 +10 True 158 3.2s [0.007 0.019 0.082]
          12 +11 True 118 2.7s [0.001 0.012 0.104]
          13 +12 True 117 2.5s [0.016 0.02  0.088]
          14 +13 True 140 3.5s [0.019 0.004 0.102]
          15 +14 True 196 4.5s [0.007 0.009 0.054]
          16 +15 True 57 1.5s [0.022 0.    0.066]
          17 +16 True 130 3.1s [0.015 0.004 0.047]
          18 +17 True 78 1.8s [0.    0.017 0.054]
          19 +18 True 141 2.5s [0.011 0.021 0.039]
          20 +19 True 106 2.4s [0.018 0.004 0.051]
          21 +20 True 114 2.9s [0.02  0.01  0.006]
          22 +21 True 147 3.8s [0.018 0.009 0.083]
          23 +22 True 65 1.2s [0.012 0.002 0.007]
          24 +23 True 65 1.6s [0.023 0.008 0.031]
          25 +24 True 71 1.8s [0.019 0.01  0.101]
          26 +25 True 113 2.8s [0.004 0.012 0.004]
          27 +26 True 188 4.0s [0.011 0.004 0.034]
          28 +27 True 134 3.3s [0.042 0.004 0.041]
          29 +28 True 22 0.5s [0.006 0.01  0.061]
          30 +29 True 140 3.0s [0.01  0.003 0.063]
          31 +30 True 132 2.9s [0.01  0.017 0.063]
          32 +31 True 81 1.4s [0.015 0.003 0.036]
          33 +32 True 245 4.0s [0.002 0.021 0.104]
          34 +33 True 145 3.0s [0.021 0.02  0.099]
          35 +34 True 220 2.9s [0.01  0.    0.089]
          36 +35 True 103 2.1s [0.    0.001 0.128]
          37 +36 True 63 1.4s [0.022 0.017 0.027]
          38 +37 True 167 2.4s [0.017 0.013 0.073]
          39 +38 True 99 1.2s [0.01  0.015 0.004]
          40 +39 True 55 1.1s [0.019 0.021 0.031]
          41 +solved 40 / 40 mean steps 127.225
diff --git a/res_wide.txt b/res_wide.txt
new file mode 100644
index 0000000..438f896
--- /dev/null
+++ b/res_wide.txt
@@ -0,0 +1,201 @@
           1 +40 True 119 2.5s [0.005 0.004 0.081]
           2 +41 True 153 3.3s [0.017 0.004 0.046]
           3 +42 True 97 1.6s [0.017 0.019 0.001]
           4 +43 True 134 2.7s [0.014 0.027 0.048]
           5 +44 True 216 4.1s [0.019 0.008 0.047]
           6 +45 True 77 1.3s [0.004 0.002 0.083]
           7 +46 True 202 3.2s [0.017 0.012 0.023]
           8 +47 True 214 4.1s [0.011 0.019 0.025]
           9 +48 True 122 2.3s [0.016 0.012 0.016]
          10 +49 True 171 3.3s [0.014 0.003 0.069]
          11 +50 True 185 3.3s [0.029 0.017 0.012]
          12 +51 True 168 3.4s [0.02  0.018 0.015]
          13 +52 True 160 3.2s [0.013 0.011 0.076]
          14 +53 True 158 2.8s [0.019 0.01  0.072]
          15 +54 True 152 3.3s [0.005 0.034 0.072]
          16 +55 True 220 3.9s [0.013 0.028 0.069]
          17 +56 True 137 2.7s [0.013 0.006 0.101]
          18 +57 True 166 3.2s [0.02 0.01 0.  ]
          19 +58 True 162 3.5s [0.011 0.02  0.098]
          20 +59 True 120 2.0s [0.009 0.001 0.066]
          21 +60 True 280 5.2s [0.022 0.016 0.022]
          22 +61 True 164 2.9s [0.014 0.013 0.043]
          23 +62 True 76 1.4s [0.011 0.02  0.062]
          24 +63 True 152 3.2s [0.009 0.014 0.011]
          25 +64 True 210 4.2s [0.007 0.021 0.054]
          26 +65 True 182 3.1s [0.004 0.016 0.095]
          27 +66 True 117 2.3s [0.01  0.031 0.084]
          28 +67 True 202 3.8s [0.019 0.022 0.074]
          29 +68 True 172 3.8s [0.011 0.003 0.042]
          30 +69 True 86 1.6s [0.017 0.006 0.102]
          31 +70 True 266 4.4s [0.017 0.002 0.058]
          32 +71 True 147 2.9s [0.014 0.008 0.088]
          33 +72 True 166 3.9s [0.022 0.005 0.055]
          34 +73 True 111 1.7s [0.006 0.02  0.11 ]
          35 +74 True 145 2.8s [0.011 0.014 0.054]
          36 +75 True 190 3.5s [0.01  0.025 0.046]
          37 +76 True 116 2.1s [0.    0.019 0.08 ]
          38 +77 True 162 2.8s [0.012 0.019 0.067]
          39 +78 True 149 3.1s [0.021 0.018 0.011]
          40 +79 True 172 3.6s [0.017 0.011 0.084]
          41 +80 True 78 1.6s [0.002 0.017 0.013]
          42 +81 True 131 2.3s [0.    0.002 0.011]
          43 +82 True 233 4.7s [0.017 0.006 0.03 ]
          44 +83 True 107 1.9s [0.    0.022 0.056]
          45 +84 True 161 2.9s [0.003 0.009 0.1  ]
          46 +85 True 235 4.0s [0.023 0.009 0.003]
          47 +86 True 142 2.8s [0.022 0.009 0.097]
          48 +87 True 139 2.2s [0.016 0.013 0.005]
          49 +88 True 256 4.9s [0.012 0.01  0.008]
          50 +89 True 78 1.4s [0.016 0.016 0.006]
          51 +90 True 147 2.4s [0.01  0.005 0.065]
          52 +91 True 113 2.3s [0.003 0.002 0.1  ]
          53 +92 True 205 4.4s [0.    0.017 0.07 ]
          54 +93 True 112 2.5s [0.    0.009 0.053]
          55 +94 True 180 3.6s [0.007 0.007 0.051]
          56 +95 True 71 1.2s [0.018 0.017 0.083]
          57 +96 True 142 3.2s [0.002 0.007 0.096]
          58 +97 True 158 3.1s [0.006 0.01  0.015]
          59 +98 True 105 2.4s [0.014 0.013 0.078]
          60 +99 True 208 3.7s [0.015 0.02  0.09 ]
          61 +100 True 251 4.8s [0.009 0.025 0.1  ]
          62 +101 True 100 2.1s [0.013 0.007 0.082]
          63 +102 True 92 2.0s [0.02  0.013 0.069]
          64 +103 True 256 4.8s [0.022 0.015 0.04 ]
          65 +104 True 94 2.6s [0.003 0.006 0.103]
          66 +105 True 173 3.6s [0.01  0.029 0.003]
          67 +106 True 123 2.6s [0.02  0.001 0.046]
          68 +107 True 114 2.3s [0.01  0.017 0.045]
          69 +108 True 164 3.2s [0.022 0.022 0.067]
          70 +109 True 133 2.8s [0.011 0.014 0.058]
          71 +110 True 137 3.1s [0.014 0.02  0.03 ]
          72 +111 True 264 5.2s [0.005 0.015 0.054]
          73 +112 True 177 4.1s [0.009 0.001 0.047]
          74 +113 True 152 3.2s [0.024 0.001 0.041]
          75 +114 True 215 5.3s [0.017 0.012 0.061]
          76 +115 True 193 4.1s [0.016 0.005 0.064]
          77 +116 True 228 4.5s [0.02  0.019 0.095]
          78 +117 True 69 1.6s [0.002 0.013 0.101]
          79 +118 True 201 4.6s [0.02  0.001 0.077]
          80 +119 True 132 3.7s [0.016 0.011 0.026]
          81 +120 True 91 1.7s [0.02  0.019 0.101]
          82 +121 True 90 2.3s [0.002 0.029 0.138]
          83 +122 True 190 3.5s [0.009 0.022 0.1  ]
          84 +123 True 185 3.6s [0.017 0.001 0.086]
          85 +124 True 157 3.4s [0.02  0.021 0.081]
          86 +125 True 99 1.5s [0.015 0.02  0.095]
          87 +126 True 188 3.8s [0.007 0.023 0.098]
          88 +127 True 244 5.2s [0.015 0.001 0.073]
          89 +128 True 146 3.0s [0.009 0.022 0.079]
          90 +129 True 69 2.1s [0.019 0.009 0.011]
          91 +130 True 147 2.9s [0.01  0.009 0.079]
          92 +131 True 166 2.6s [0.006 0.009 0.058]
          93 +132 True 190 3.9s [0.006 0.013 0.08 ]
          94 +133 True 185 3.7s [0.013 0.014 0.037]
          95 +134 True 159 4.0s [0.009 0.008 0.084]
          96 +135 True 96 1.7s [0.013 0.017 0.045]
          97 +136 True 149 2.9s [0.019 0.006 0.024]
          98 +137 True 97 2.4s [0.017 0.008 0.104]
          99 +138 True 183 4.0s [0.019 0.009 0.069]
         100 +139 True 132 3.0s [0.013 0.021 0.073]
         101 +140 True 118 2.8s [0.013 0.004 0.065]
         102 +141 True 102 2.4s [0.023 0.011 0.101]
         103 +142 True 154 3.6s [0.013 0.012 0.063]
         104 +143 True 113 2.9s [0.019 0.018 0.085]
         105 +144 True 216 4.8s [0.018 0.008 0.071]
         106 +145 True 167 4.4s [0.004 0.002 0.053]
         107 +146 True 87 2.0s [0.004 0.022 0.06 ]
         108 +147 True 120 3.5s [0.018 0.013 0.021]
         109 +148 True 201 8.7s [0.01  0.004 0.051]
         110 +149 True 131 3.4s [0.003 0.007 0.037]
         111 +150 True 84 2.1s [0.002 0.013 0.04 ]
         112 +151 True 218 5.2s [0.012 0.    0.053]
         113 +152 True 126 3.2s [0.016 0.01  0.001]
         114 +153 True 64 1.4s [0.006 0.015 0.025]
         115 +154 True 110 2.6s [0.016 0.013 0.08 ]
         116 +155 True 86 2.0s [0.02  0.02  0.025]
         117 +156 True 135 3.1s [0.007 0.007 0.104]
         118 +157 True 87 2.7s [0.012 0.02  0.068]
         119 +158 True 108 2.8s [0.017 0.022 0.037]
         120 +159 True 166 3.7s [0.02  0.002 0.062]
         121 +160 True 104 2.3s [0.012 0.011 0.016]
         122 +161 True 145 3.7s [0.013 0.014 0.084]
         123 +162 True 79 2.4s [0.001 0.006 0.138]
         124 +163 True 181 4.7s [0.027 0.028 0.006]
         125 +164 True 119 3.0s [0.003 0.021 0.081]
         126 +165 True 218 6.5s [0.003 0.004 0.043]
         127 +166 True 197 4.9s [0.006 0.016 0.051]
         128 +167 True 68 1.5s [0.018 0.013 0.074]
         129 +168 True 163 4.4s [0.004 0.018 0.101]
         130 +169 True 148 3.8s [0.013 0.01  0.001]
         131 +170 True 132 3.0s [0.002 0.013 0.047]
         132 +171 True 137 3.7s [0.001 0.01  0.061]
         133 +172 True 157 4.1s [0.    0.003 0.062]
         134 +173 True 138 3.4s [0.024 0.004 0.002]
         135 +174 True 181 5.1s [0.02  0.005 0.077]
         136 +175 True 83 2.0s [0.012 0.014 0.045]
         137 +176 True 120 3.5s [0.015 0.03  0.117]
         138 +177 True 98 2.7s [0.021 0.004 0.015]
         139 +178 True 141 3.8s [0.029 0.012 0.007]
         140 +179 True 248 10.9s [0.022 0.008 0.007]
         141 +180 True 132 3.2s [0.01  0.021 0.102]
         142 +181 True 179 4.6s [0.001 0.024 0.075]
         143 +182 True 156 3.9s [0.014 0.013 0.095]
         144 +183 True 192 5.1s [0.009 0.013 0.092]
         145 +184 True 162 3.7s [0.013 0.009 0.047]
         146 +185 True 122 3.0s [0.021 0.016 0.051]
         147 +186 True 58 1.7s [0.02  0.011 0.103]
         148 +187 True 87 2.1s [0.009 0.011 0.098]
         149 +188 True 150 3.6s [0.013 0.02  0.094]
         150 +189 True 206 5.4s [0.022 0.003 0.097]
         151 +190 True 97 2.4s [0.021 0.02  0.029]
         152 +191 True 83 2.3s [0.021 0.023 0.096]
         153 +192 True 168 3.9s [0.012 0.017 0.024]
         154 +193 True 190 4.7s [0.011 0.005 0.087]
         155 +194 True 151 4.2s [0.007 0.01  0.098]
         156 +195 True 118 3.2s [0.013 0.014 0.057]
         157 +196 True 213 5.1s [0.021 0.013 0.063]
         158 +197 True 150 3.3s [0.004 0.002 0.096]
         159 +198 True 145 3.9s [0.016 0.016 0.027]
         160 +199 True 53 1.7s [0.039 0.016 0.028]
         161 +200 True 133 3.3s [0.019 0.005 0.104]
         162 +201 True 60 1.6s [0.009 0.    0.09 ]
         163 +202 True 85 2.2s [0.013 0.005 0.047]
         164 +203 True 150 3.5s [0.025 0.017 0.014]
         165 +204 True 110 3.5s [0.017 0.018 0.014]
         166 +205 True 176 4.7s [0.011 0.007 0.026]
         167 +206 True 107 2.6s [0.006 0.016 0.076]
         168 +207 True 104 2.6s [0.021 0.01  0.014]
         169 +208 True 142 3.6s [0.02  0.012 0.098]
         170 +209 True 208 5.1s [0.008 0.02  0.082]
         171 +210 True 210 5.0s [0.017 0.003 0.109]
         172 +211 True 64 2.2s [0.006 0.027 0.135]
         173 +212 True 123 3.1s [0.007 0.019 0.008]
         174 +213 True 80 2.3s [0.009 0.021 0.082]
         175 +214 True 165 3.6s [0.02  0.02  0.103]
         176 +215 True 130 3.2s [0.002 0.003 0.072]
         177 +216 True 158 3.7s [0.02  0.018 0.069]
         178 +217 True 170 4.3s [0.008 0.013 0.082]
         179 +218 True 147 3.2s [0.002 0.016 0.074]
         180 +219 True 124 2.6s [0.022 0.02  0.045]
         181 +220 True 197 4.6s [0.017 0.018 0.099]
         182 +221 True 71 1.6s [0.013 0.013 0.063]
         183 +222 True 139 3.0s [0.01  0.002 0.097]
         184 +223 True 185 4.7s [0.003 0.023 0.075]
         185 +224 True 163 2.5s [0.016 0.021 0.035]
         186 +225 True 115 2.6s [0.01  0.002 0.124]
         187 +226 True 156 4.1s [0.015 0.018 0.04 ]
         188 +227 True 235 4.9s [0.014 0.006 0.011]
         189 +228 True 140 3.1s [0.019 0.016 0.011]
         190 +229 True 157 1.9s [0.005 0.02  0.054]
         191 +230 True 122 2.0s [0.013 0.021 0.06 ]
         192 +231 True 122 3.7s [0.007 0.002 0.049]
         193 +232 True 161 3.2s [0.018 0.013 0.047]
         194 +233 True 98 1.4s [0.    0.006 0.102]
         195 +234 True 127 3.0s [0.003 0.02  0.012]
         196 +235 True 158 4.0s [0.004 0.01  0.037]
         197 +236 True 114 2.8s [0.013 0.005 0.098]
         198 +237 True 106 2.5s [0.004 0.006 0.025]
         199 +238 True 213 3.0s [0.014 0.013 0.051]
         200 +239 True 102 0.5s [0.002 0.012 0.091]
         201 +solved 200 / 200 mean steps 147.095
diff --git a/stats.py b/stats.py
new file mode 100644
index 0000000..c6222af
--- /dev/null
+++ b/stats.py
@@ -0,0 +1,18 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +from multiprocessing import Pool
           5 +def run(seed):
           6 +    env=make_env(); obs,_=env.reset(seed=seed)
           7 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,{})
           8 +    cnt={"nav":0,"push":0}; plans=0
           9 +    for i in range(1000):
          10 +        m0=ap.mode
          11 +        a=ap.get_action(obs)
          12 +        cnt[ap.mode if ap.mode in cnt else "nav"]+=1
          13 +        obs,r,te,tr,_=env.step(np.clip(a,-0.049,0.049))
          14 +        if te: break
          15 +    env.close()
          16 +    return i+1, cnt["nav"], cnt["push"]
          17 +with Pool(15) as p: res=p.map(run, range(1000,1030))
          18 +r=np.array(res); print(r.mean(0)); print(r[:10])
diff --git a/stats2.py b/stats2.py
new file mode 100644
index 0000000..11eaee4
--- /dev/null
+++ b/stats2.py
@@ -0,0 +1,21 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +from multiprocessing import Pool
           5 +def run(seed):
           6 +    env=make_env(); obs,_=env.reset(seed=seed)
           7 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,{})
           8 +    p0=obs[0:3].copy(); first=None; nplans=0; segs=[]; cur=None
           9 +    for i in range(1000):
          10 +        a=ap.get_action(obs)
          11 +        m=ap.mode
          12 +        if m!=cur: segs.append([m,0]); cur=m
          13 +        segs[-1][1]+=1
          14 +        obs,r,te,tr,_=env.step(np.clip(a,-0.049,0.049))
          15 +        if first is None and np.any(np.abs(obs[0:3]-p0)>1e-6): first=i
          16 +        if te: break
          17 +    env.close()
          18 +    return i+1, first, segs
          19 +with Pool(15) as p: res=p.map(run, range(1000,1030))
          20 +print(np.mean([r[0] for r in res]), np.mean([r[1] for r in res]))
          21 +for r in res[:8]: print(r[0], r[1], " ".join("%s%d"%(m[0][0],m[1]) for m in r[2]))
diff --git a/thcheck.py b/thcheck.py
new file mode 100644
index 0000000..e08fb2b
--- /dev/null
+++ b/thcheck.py
@@ -0,0 +1,17 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +from multiprocessing import Pool
           5 +def run(seed):
           6 +    env=make_env(); obs,_=env.reset(seed=seed)
           7 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,{})
           8 +    ths=[obs[2]]; jumps=0
           9 +    for i in range(400):
          10 +        obs,r,te,tr,_=env.step(np.clip(ap.get_action(obs),-0.049,0.049))
          11 +        if abs(obs[2]-ths[-1])>1: jumps+=1
          12 +        ths.append(obs[2])
          13 +        if te: break
          14 +    env.close()
          15 +    return seed, round(ths[0],2), round(min(ths),2), round(max(ths),2), jumps, round(obs[31],2)
          16 +with Pool(15) as p: res=p.map(run, range(2000,2030))
          17 +for r in res: print(r)
diff --git a/thcheck2.py b/thcheck2.py
new file mode 100644
index 0000000..a68155d
--- /dev/null
+++ b/thcheck2.py
@@ -0,0 +1,11 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +env=make_env(); obs,_=env.reset(seed=2006)
           5 +ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,{})
           6 +ap.goal=np.array([obs[0],obs[1],obs[2]+0.8])
           7 +ths=[]
           8 +for i in range(300):
           9 +    obs,r,te,tr,_=env.step(np.clip(ap.get_action(obs),-0.049,0.049))
          10 +    ths.append(obs[2])
          11 +print(np.round(ths[::10],3))
diff --git a/timing.py b/timing.py
new file mode 100644
index 0000000..553dc17
--- /dev/null
+++ b/timing.py
@@ -0,0 +1,9 @@
           1 +import numpy as np, time
           2 +from env_client import make_env
           3 +from approach import *
           4 +env=make_env(); obs,_=env.reset(seed=1003)
           5 +ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
           6 +t=time.time()
           7 +for _ in range(5): r=ap.plan_push(obs[0:3],obs[16:18])
           8 +print((time.time()-t)/5)
           9 +sw,dw=ap.candidates(obs[0:3]); print(len(sw))
```

</details>

