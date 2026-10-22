# DynPushT2D · claude-opus-5-5 · replicate 42: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `73bb6a8` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `c66d154` | Model-based greedy push planner v1 | approach.py, probe.py, probe2.py, probe3.py, probe4.py, probe_dyn_X.npy, probe_dyn_a.py, probe_dyn_b.py, probe_dyn_c.py, probe_dyn_collect.py, probe_dyn_data_1.npy, probe_dyn_data… | [E0260](01_timeline.md#E0260) |
| [C003](#C003) · `076d2b6` | retreat after push before navigating | approach.py, dbg.py, res_0.txt, res_1.txt, res_2.txt, res_3.txt, res_4.txt | [E0307](01_timeline.md#E0307) |
| [C004](#C004) · `ea6e8e1` | K_ANG=0.8 (fixes rotation local minima, fewer steps) | approach.py, sw_0.8_0_50.txt, sw_0.8_50_100.txt, sw_1.2_0_50.txt, sw_1.2_50_100.txt, sw_1.6_0_50.txt, sw_1.6_50_100.txt, sweep.py | [E0334](01_timeline.md#E0334) |
| [C005](#C005) · `b032fa7` | 2-step lookahead planner | approach.py, big_200_250.txt, big_250_300.txt, big_300_350.txt, big_350_400.txt, big_400_450.txt, big_450_500.txt, big_500_550.txt, big_550_600.txt, sweep.py | [E0363](01_timeline.md#E0363) |
| [C006](#C006) · `c6944f5` | block-frame push family | approach.py, la_0_0_25.txt, la_0_25_50.txt, la_0_50_75.txt, la_0_75_100.txt, la_8_0_25.txt, la_8_25_50.txt, la_8_50_75.txt, la_8_75_100.txt, sweep.py | [E0389](01_timeline.md#E0389) |
| [C007](#C007) · `341c0e1` | lookahead 16 | approach.py, la16_0_25.txt, la16_25_50.txt, la16_50_75.txt, la16_75_100.txt, lf_0_0_25.txt, lf_0_25_50.txt, lf_0_50_75.txt, lf_0_75_100.txt, lf_1_0_25.txt, lf_1_25_50.txt, lf_1_50… | [E0408](01_timeline.md#E0408) |
| [C008](#C008) · `96fd518` | exception-safe get_action, cleanup | approach.py, v_600_650.txt, v_650_700.txt, v_700_750.txt, v_750_800.txt, v_800_850.txt, v_850_900.txt, v_900_950.txt, v_950_1000.txt | [E0420](01_timeline.md#E0420) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `73bb6a884d79735052e12d28b166d686dbe4be31`; parents: none (initial snapshot). Recorded author date: 2026-09-28T18:47:13+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_73bb6a8.diff)

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
index 0000000..fa4a4e7
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "5c3a3437f7db938d77da54378e3330e5", "observation_space": {"type": "Box", "shape": [45], "low": [-Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity], "high": [Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity, Infinity], "dtype": "float64"}, "action_space": {"type": "Box", "shape": [2], "low": [-0.05, -0.05], "high": [0.05, 0.05], "dtype": "float64"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Model-based greedy push planner v1

Commit `c66d154cb4c7da49470d7e7a6e1aab4762c8fb29`; parents: 73bb6a884d79735052e12d28b166d686dbe4be31. Recorded author date: 2026-09-28T18:58:21+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0260](01_timeline.md#E0260): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_c66d154_approach.py) · [Exact all-file diff](evidence/diffs/C002_c66d154.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..f059a65
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,252 @@
           1 +import heapq
           2 +import numpy as np
           3 +from tmodel import TGeom, sim_step, wrap, corners_world, R_ROBOT
           4 +
           5 +AMAX = 0.0499
           6 +LO, HI = 0.1 + 1e-3, 4.9 - 1e-3
           7 +POS_TOL, ANG_TOL = 0.03, np.deg2rad(8.0)
           8 +K_ANG = 0.3
           9 +
          10 +
          11 +def cost(bx, by, bt, goal):
          12 +    return np.hypot(bx - goal[0], by - goal[1]) + K_ANG * np.abs(wrap(bt - goal[2]))
          13 +
          14 +
          15 +def solved(bx, by, bt, goal, pf=0.7, af=0.7):
          16 +    return (np.abs(bx - goal[0]) < POS_TOL * pf) & (np.abs(by - goal[1]) < POS_TOL * pf) & \
          17 +        (np.abs(wrap(bt - goal[2])) < ANG_TOL * af)
          18 +
          19 +
          20 +class GeneratedApproach:
          21 +    def __init__(self, action_space, observation_space, primitives):
          22 +        self.action_space = action_space
          23 +        self.queue = []
          24 +        self.g = None
          25 +
          26 +    def reset(self, state, info):
          27 +        self.queue = []
          28 +        self.g = TGeom(state[12], state[13], state[14])
          29 +        self.goal = np.array(state[29:32], dtype=float)
          30 +        self.expect = None
          31 +        self.mode = None
          32 +
          33 +    # ---------------- navigation -----------------
          34 +    def _seg_free(self, pose, ax, ay, bx_, by_, m):
          35 +        """Is segment (a->b) (world, arrays) free of T inflated by m? vectorized over segments."""
          36 +        c, s = np.cos(pose[2]), np.sin(pose[2])
          37 +        lax = c * (ax - pose[0]) + s * (ay - pose[1])
          38 +        lay = -s * (ax - pose[0]) + c * (ay - pose[1])
          39 +        lbx = c * (bx_ - pose[0]) + s * (by_ - pose[1])
          40 +        lby = -s * (bx_ - pose[0]) + c * (by_ - pose[1])
          41 +        dx, dy = lbx - lax, lby - lay
          42 +        free = np.ones(np.broadcast(lax, lbx).shape, bool)
          43 +        for (x0, x1, y0, y1) in self.g.rects:
          44 +            x0, x1, y0, y1 = x0 - m, x1 + m, y0 - m, y1 + m
          45 +            t0 = np.zeros_like(free, dtype=float)
          46 +            t1 = np.ones_like(free, dtype=float)
          47 +            hit = np.ones_like(free)
          48 +            for (p, d, lo, hi) in ((lax, dx, x0, x1), (lay, dy, y0, y1)):
          49 +                p = np.broadcast_to(p, free.shape)
          50 +                d = np.broadcast_to(d, free.shape)
          51 +                small = np.abs(d) < 1e-12
          52 +                inside = (p >= lo) & (p <= hi)
          53 +                hit &= ~(small & ~inside)
          54 +                with np.errstate(divide='ignore', invalid='ignore'):
          55 +                    ta = (lo - p) / d
          56 +                    tb = (hi - p) / d
          57 +                tmin = np.where(small, -np.inf, np.minimum(ta, tb))
          58 +                tmax = np.where(small, np.inf, np.maximum(ta, tb))
          59 +                t0 = np.maximum(t0, tmin)
          60 +                t1 = np.minimum(t1, tmax)
          61 +            hit &= t0 <= t1
          62 +            free &= ~hit
          63 +        return free
          64 +
          65 +    def _nav_nodes(self, pose, m):
          66 +        c, s = np.cos(pose[2]), np.sin(pose[2])
          67 +        pts = []
          68 +        for (x0, x1, y0, y1) in self.g.rects:
          69 +            for lx, ly in ((x0 - m, y0 - m), (x0 - m, y1 + m), (x1 + m, y0 - m), (x1 + m, y1 + m)):
          70 +                pts.append((pose[0] + c * lx - s * ly, pose[1] + s * lx + c * ly))
          71 +        pts = np.array(pts)
          72 +        ok = (pts[:, 0] > LO) & (pts[:, 0] < HI) & (pts[:, 1] > LO) & (pts[:, 1] < HI)
          73 +        pts = pts[ok]
          74 +        # remove nodes inside inflated T
          75 +        lx = c * (pts[:, 0] - pose[0]) + s * (pts[:, 1] - pose[1])
          76 +        ly = -s * (pts[:, 0] - pose[0]) + c * (pts[:, 1] - pose[1])
          77 +        _, _, _, _, d = self.g.closest(lx, ly)
          78 +        return pts[d > R_ROBOT + m * 0.6]
          79 +
          80 +    def _plan_paths(self, pose, start, targets):
          81 +        """Shortest paths from start to each target avoiding T. Returns dist array, and
          82 +        function to get path waypoints."""
          83 +        mcol = 0.012
          84 +        nodes = self._nav_nodes(pose, 0.035 + R_ROBOT)
          85 +        allp = np.vstack([start[None], nodes])
          86 +        n = len(allp)
          87 +        # adjacency
          88 +        A = allp[:, None, :].repeat(n, 1)
          89 +        B = allp[None, :, :].repeat(n, 0)
          90 +        free = self._seg_free(pose, A[..., 0], A[..., 1], B[..., 0], B[..., 1], R_ROBOT + mcol)
          91 +        # start may be close to block: allow edges from start if it moves away? keep as is but
          92 +        # if start is itself inside inflation, relax with smaller margin
          93 +        free_s = self._seg_free(pose, A[0, :, 0], A[0, :, 1], B[0, :, 0], B[0, :, 1], R_ROBOT - 0.005)
          94 +        free[0, :] = free_s
          95 +        free[:, 0] = free_s
          96 +        D = np.hypot(A[..., 0] - B[..., 0], A[..., 1] - B[..., 1])
          97 +        dist = np.full(n, np.inf)
          98 +        prev = np.full(n, -1)
          99 +        dist[0] = 0
         100 +        pq = [(0.0, 0)]
         101 +        done = np.zeros(n, bool)
         102 +        while pq:
         103 +            d0, i = heapq.heappop(pq)
         104 +            if done[i]:
         105 +                continue
         106 +            done[i] = True
         107 +            for j in range(n):
         108 +                if free[i, j] and not done[j]:
         109 +                    nd = d0 + D[i, j]
         110 +                    if nd < dist[j]:
         111 +                        dist[j] = nd
         112 +                        prev[j] = i
         113 +                        heapq.heappush(pq, (nd, j))
         114 +        # targets
         115 +        T = np.asarray(targets)
         116 +        fr = self._seg_free(pose, allp[:, None, 0], allp[:, None, 1], T[None, :, 0], T[None, :, 1], R_ROBOT + mcol)
         117 +        fr[0, :] = self._seg_free(pose, allp[0, 0], allp[0, 1], T[:, 0], T[:, 1], R_ROBOT - 0.005)
         118 +        DT = np.hypot(allp[:, None, 0] - T[None, :, 0], allp[:, None, 1] - T[None, :, 1])
         119 +        tot = np.where(fr, dist[:, None] + DT, np.inf)
         120 +        best = np.argmin(tot, axis=0)
         121 +        tdist = tot[best, np.arange(len(T))]
         122 +
         123 +        def path(k):
         124 +            i = best[k]
         125 +            wp = [T[k]]
         126 +            while i > 0:
         127 +                wp.append(allp[i])
         128 +                i = prev[i]
         129 +            return wp[::-1]
         130 +        return tdist, path
         131 +
         132 +    # ---------------- planning -----------------
         133 +    def _plan(self, obs):
         134 +        g = self.g
         135 +        pose = np.array(obs[0:3], float)
         136 +        robot = np.array(obs[16:18], float)
         137 +        goal = self.goal
         138 +        J0 = cost(pose[0], pose[1], pose[2], goal)
         139 +        fine = J0 < 0.12
         140 +        step = AMAX if not fine else AMAX / 3
         141 +        nsteps = 40 if not fine else 30
         142 +        pts = g.boundary_points(0.05)
         143 +        c, s = np.cos(pose[2]), np.sin(pose[2])
         144 +        # contact center (robot center touching) and pre-point in world
         145 +        lcx = pts[:, 0] + pts[:, 2] * (R_ROBOT + 0.003)
         146 +        lcy = pts[:, 1] + pts[:, 3] * (R_ROBOT + 0.003)
         147 +        wcx = pose[0] + c * lcx - s * lcy
         148 +        wcy = pose[1] + s * lcx + c * lcy
         149 +        lpx = pts[:, 0] + pts[:, 2] * (R_ROBOT + 0.045)
         150 +        lpy = pts[:, 1] + pts[:, 3] * (R_ROBOT + 0.045)
         151 +        wpx = pose[0] + c * lpx - s * lpy
         152 +        wpy = pose[1] + s * lpx + c * lpy
         153 +        inb = (wcx > LO) & (wcx < HI) & (wcy > LO) & (wcy < HI) & (wpx > LO) & (wpx < HI) & (wpy > LO) & (wpy < HI)
         154 +        # pre-point must be free
         155 +        _, _, _, _, dpre = g.closest(lpx, lpy)
         156 +        inb &= dpre > R_ROBOT + 0.03
         157 +        idx = np.nonzero(inb)[0]
         158 +        if len(idx) == 0:
         159 +            return None
         160 +        pre = np.stack([wpx[idx], wpy[idx]], 1)
         161 +        tdist, pathf = self._plan_paths(pose, robot, pre)
         162 +        tdist = tdist + 0.045
         163 +        # world inward normal
         164 +        nwx = -(c * pts[idx, 2] - s * pts[idx, 3])
         165 +        nwy = -(s * pts[idx, 2] + c * pts[idx, 3])
         166 +        angs = np.deg2rad(np.array([-40, -25, -12, 0, 12, 25, 40]))
         167 +        K = len(idx) * len(angs)
         168 +        ci = np.repeat(np.arange(len(idx)), len(angs))
         169 +        aa = np.tile(angs, len(idx))
         170 +        dirx = np.cos(aa) * nwx[ci] - np.sin(aa) * nwy[ci]
         171 +        diry = np.sin(aa) * nwx[ci] + np.cos(aa) * nwy[ci]
         172 +        ux, uy = dirx * step, diry * step
         173 +        bx = np.full(K, pose[0]); by = np.full(K, pose[1]); bt = np.full(K, pose[2])
         174 +        rx = wcx[idx][ci].copy(); ry = wcy[idx][ci].copy()
         175 +        valid = np.isfinite(tdist[ci])
         176 +        travel = tdist[ci] / AMAX + 1.0
         177 +        # current wall margin
         178 +        cx0, cy0 = corners_world(g, pose[0], pose[1], pose[2])
         179 +        m0 = min(cx0.min(), cy0.min(), 5 - cx0.max(), 5 - cy0.max())
         180 +        wall_lim = min(0.06, m0 - 0.01)
         181 +        best_score = np.full(K, -np.inf)
         182 +        best_n = np.zeros(K, int)
         183 +        best_J = np.full(K, np.inf)
         184 +        alive = valid.copy()
         185 +        for k in range(1, nsteps + 1):
         186 +            bx, by, bt, rx, ry = sim_step(g, bx, by, bt, rx, ry, ux, uy)
         187 +            alive &= (rx > LO) & (rx < HI) & (ry > LO) & (ry < HI)
         188 +            cxw, cyw = corners_world(g, bx, by, bt)
         189 +            mm = np.minimum(np.minimum(cxw.min(0), cyw.min(0)), np.minimum(5 - cxw.max(0), 5 - cyw.max(0)))
         190 +            alive &= mm > wall_lim
         191 +            J = cost(bx, by, bt, goal)
         192 +            J = np.where(solved(bx, by, bt, goal), J - 0.5, J)
         193 +            steps_k = k if not fine else k / 3.0
         194 +            sc = (J0 - J) / (travel + steps_k + 1.0)
         195 +            upd = alive & (sc > best_score)
         196 +            best_score = np.where(upd, sc, best_score)
         197 +            best_n = np.where(upd, k, best_n)
         198 +            best_J = np.where(upd, J, best_J)
         199 +        j = int(np.argmax(best_score))
         200 +        if not np.isfinite(best_score[j]) or best_score[j] <= 0:
         201 +            return None
         202 +        n = int(best_n[j])
         203 +        wp = pathf(ci[j])
         204 +        acts = []
         205 +        cur = robot.copy()
         206 +        for w in wp + [np.array([wcx[idx][ci[j]], wcy[idx][ci[j]]])]:
         207 +            w = np.asarray(w, float)
         208 +            while True:
         209 +                d = w - cur
         210 +                L = np.hypot(*d)
         211 +                if L < 1e-9:
         212 +                    break
         213 +                nst = int(np.ceil(L / AMAX - 1e-9))
         214 +                a = d / nst
         215 +                for _ in range(nst):
         216 +                    acts.append(('nav', a.copy()))
         217 +                cur = w.copy()
         218 +                break
         219 +        # push
         220 +        a = np.array([ux[j], uy[j]])
         221 +        if fine:
         222 +            # combine into fewer steps
         223 +            tot = a * n
         224 +            L = np.hypot(*tot)
         225 +            nst = max(1, int(np.ceil(L / AMAX - 1e-9)))
         226 +            for _ in range(nst):
         227 +                acts.append(('push', tot / nst))
         228 +        else:
         229 +            for _ in range(n):
         230 +                acts.append(('push', a.copy()))
         231 +        self.dbg = (best_score[j], best_J[j], n, travel[j], J0)
         232 +        return acts
         233 +
         234 +    def get_action(self, state):
         235 +        obs = np.asarray(state, float)
         236 +        pose = obs[0:3]
         237 +        replan = not self.queue
         238 +        if self.expect is not None and self.queue:
         239 +            ep = self.expect
         240 +            if self.queue[0][0] == 'nav':
         241 +                if np.abs(pose - ep).max() > 1e-4:
         242 +                    replan = True
         243 +        if replan:
         244 +            self.queue = self._plan(obs) or []
         245 +        if not self.queue:
         246 +            self.expect = None
         247 +            # fallback: move toward block
         248 +            d = pose[0:2] - obs[16:18]
         249 +            return np.clip(d, -AMAX, AMAX)
         250 +        kind, a = self.queue.pop(0)
         251 +        self.expect = pose.copy()
         252 +        return np.clip(a, -AMAX, AMAX)
diff --git a/probe.py b/probe.py
new file mode 100644
index 0000000..3831559
--- /dev/null
+++ b/probe.py
@@ -0,0 +1,8 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=3, suppress=True)
           4 +env = make_env()
           5 +print(env.max_steps)
           6 +for s in range(3):
           7 +    obs,_ = env.reset(seed=s)
           8 +    print(obs)
diff --git a/probe2.py b/probe2.py
new file mode 100644
index 0000000..71d92c5
--- /dev/null
+++ b/probe2.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=3, suppress=True)
           4 +env = make_env()
           5 +obs,_ = env.reset(seed=0)
           6 +# robot at 1.637,1.27; block at 1.05,3.44 theta 2.593
           7 +# move robot toward walls to find bounds: move left for 60 steps
           8 +for i in range(60):
           9 +    obs,r,te,tr,info=env.step(np.clip(np.array([-0.05,0.0]),-0.0499,0.0499))
          10 +print('left', obs[16:18])
          11 +for i in range(80):
          12 +    obs,r,te,tr,info=env.step(np.clip(np.array([0.0,-0.05]),-0.0499,0.0499))
          13 +print('down', obs[16:18])
          14 +for i in range(120):
          15 +    obs,r,te,tr,info=env.step(np.clip(np.array([0.05,0.0]),-0.0499,0.0499))
          16 +print('right', obs[16:18], obs[0:6])
          17 +# big action out of bounds
          18 +obs,r,te,tr,info=env.step(np.clip(np.array([0.2,0.2]),-0.0499,0.0499))
          19 +print('clip', obs[16:18], r, info)
diff --git a/probe3.py b/probe3.py
new file mode 100644
index 0000000..0a673a9
--- /dev/null
+++ b/probe3.py
@@ -0,0 +1,23 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=3, suppress=True)
           4 +env = make_env()
           5 +obs,_ = env.reset(seed=1)
           6 +print(obs[0:3], obs[16:18])
           7 +# go to x below block by 0.8 in world y
           8 +tgt = obs[0:2] + np.array([0.0,-0.9])
           9 +def goto(obs,tgt,n=200):
          10 +    for i in range(n):
          11 +        d = tgt-obs[16:18]
          12 +        if np.linalg.norm(d)<1e-3: break
          13 +        a = np.clip(d,-0.0499,0.0499)
          14 +        obs,r,te,tr,info=env.step(a)
          15 +    return obs
          16 +obs=goto(obs,tgt)
          17 +print('at', obs[16:18], obs[0:6])
          18 +for i in range(30):
          19 +    obs,r,te,tr,info=env.step(np.array([0,0.0499]))
          20 +    print(i, obs[16:18], obs[0:6])
          21 +for i in range(15):
          22 +    obs,r,te,tr,info=env.step(np.array([0,-0.0499]))
          23 +    print('back',i, obs[16:18], obs[0:6])
diff --git a/probe4.py b/probe4.py
new file mode 100644
index 0000000..1e03403
--- /dev/null
+++ b/probe4.py
@@ -0,0 +1,7 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=3, suppress=True)
           4 +env = make_env()
           5 +for s in range(20):
           6 +    obs,_ = env.reset(seed=s)
           7 +    print(s, obs[0:3], obs[16:18], obs[29:32], obs[12:15])
diff --git a/probe_dyn_X.npy b/probe_dyn_X.npy
new file mode 100644
index 0000000..194c682
Binary files /dev/null and b/probe_dyn_X.npy differ
diff --git a/probe_dyn_a.py b/probe_dyn_a.py
new file mode 100644
index 0000000..1e7e63e
--- /dev/null
+++ b/probe_dyn_a.py
@@ -0,0 +1,9 @@
           1 +from probe_dyn_lib import *
           2 +S=Sim()
           3 +# pick seed with central block
           4 +o=S.reset(3); print(o[0:3],o[12:15])
           5 +w,lh,lv=o[12:15]
           6 +moved=S.goto_local([0,-lv-0.1-0.15]); print('moved during nav',moved)
           7 +print('robot local',w2l(S.obs,S.obs[16:18]))
           8 +R=S.push([0,1],0.03,25)
           9 +for r in R: print(r[:3], 'rp',r[3:5],'rp2',r[5:7])
diff --git a/probe_dyn_b.py b/probe_dyn_b.py
new file mode 100644
index 0000000..28f3b9a
--- /dev/null
+++ b/probe_dyn_b.py
@@ -0,0 +1,22 @@
           1 +from probe_dyn_lib import *
           2 +import sys
           3 +S=Sim()
           4 +def exp(name,start,d,v,n,seed=81,verbose=False):
           5 +    S.reset(seed); S.goto_local(start)
           6 +    R=S.push(d,v,n)
           7 +    act=np.abs(R[:,:3]).max(1)>1e-7
           8 +    k=np.argmax(act)
           9 +    if verbose:
          10 +        for r in R[k:k+8]: print('   ',r[:3].round(5),'rp',r[3:5].round(4))
          11 +    Rs=R[k+1:]
          12 +    m=Rs[:,:3].mean(0)
          13 +    # instantaneous rotation center in local frame (of pre-step): p = (-dy/dth, dx/dth)
          14 +    rc=np.array([-m[1]/m[2],m[0]/m[2]]) if abs(m[2])>1e-6 else None
          15 +    print(f'{name:28s} v={v} first_contact_step={k} mean twist/step={m.round(5)} |dxy|/v={np.hypot(m[0],m[1])/v:.3f} rotC={None if rc is None else rc.round(3)} rp_first={R[k,3:5].round(3)} rp_last={R[-1,5:7].round(3)}')
          16 +    return R
          17 +if __name__=='__main__':
          18 +    for v in [0.01,0.03,0.0499]:
          19 +        exp('a stem bottom up x0',[0,-1.4],[0,1],v,int(0.6/v),verbose=(v==0.03))
          20 +    for x in [0,0.1,0.25,0.4,0.5]:
          21 +        for v in [0.01,0.0499]:
          22 +            exp(f'b bar top down x{x}',[x,0.3],[0,-1],v,int(0.5/v))
diff --git a/probe_dyn_c.py b/probe_dyn_c.py
new file mode 100644
index 0000000..db218bc
--- /dev/null
+++ b/probe_dyn_c.py
@@ -0,0 +1,11 @@
           1 +from probe_dyn_lib import *
           2 +from probe_dyn_b import exp
           3 +S=None
           4 +for v in [0.01,0.0499]:
           5 +    exp('c bar end -x push (from +x)',[0.8,-0.06],[-1,0],v,int(0.5/v))
           6 +    exp('c bar end +x push (from -x)',[-0.8,-0.06],[1,0],v,int(0.5/v))
           7 +    exp('c bar end -x at y=-0.01',[0.8,-0.01],[-1,0],v,int(0.5/v))
           8 +    exp('d stem side y-.6 push -x',[0.6,-0.6],[-1,0],v,int(0.6/v))
           9 +    exp('d stem side y-1.0 push -x',[0.6,-1.0],[-1,0],v,int(0.6/v))
          10 +    exp('d stem side y-.3 push +x',[-0.6,-0.3],[1,0],v,int(0.6/v))
          11 +    exp('bar under x.4 push up',[0.4,-0.5],[0,1],v,int(0.5/v))
diff --git a/probe_dyn_collect.py b/probe_dyn_collect.py
new file mode 100644
index 0000000..9eda5d1
--- /dev/null
+++ b/probe_dyn_collect.py
@@ -0,0 +1,31 @@
           1 +from probe_dyn_lib import *
           2 +import sys
           3 +rng=np.random.default_rng(int(sys.argv[1]))
           4 +seeds=[int(s) for s in sys.argv[2].split(',')]
           5 +nexp=int(sys.argv[3])
           6 +S=Sim(); data=[]
           7 +def faces(w,L,lv):
           8 +    return [((-L/2,0),(L/2,0),(0,1)),((L/2,-w),(L/2,0),(1,0)),((-L/2,-w),(-L/2,0),(-1,0)),
           9 +            ((w/2,-w),(L/2,-w),(0,-1)),((-L/2,-w),(-w/2,-w),(0,-1)),
          10 +            ((w/2,-w-lv),(w/2,-w),(1,0)),((-w/2,-w-lv),(-w/2,-w),(-1,0)),((-w/2,-w-lv),(w/2,-w-lv),(0,-1))]
          11 +def dist_T(q,w,L,lv):
          12 +    def dr(q,x0,x1,y0,y1):
          13 +        dx=max(x0-q[0],0,q[0]-x1); dy=max(y0-q[1],0,q[1]-y1); return np.hypot(dx,dy)
          14 +    return min(dr(q,-L/2,L/2,-w,0),dr(q,-w/2,w/2,-w-lv,-w))
          15 +for e in range(nexp):
          16 +    seed=seeds[e%len(seeds)]; o=S.reset(seed); w,L,lv=o[12:15]
          17 +    F=faces(w,L,lv); lens=[np.hypot(f[1][0]-f[0][0],f[1][1]-f[0][1]) for f in F]
          18 +    i=rng.choice(len(F),p=np.array(lens)/sum(lens)); a,b,n=F[i]; s=rng.uniform(0.03,0.97)
          19 +    p=np.array(a)+s*(np.array(b)-np.array(a)); n=np.array(n,float)
          20 +    ang=rng.uniform(-1.2,1.2); t=np.array([-n[1],n[0]])
          21 +    ud=-n*np.cos(ang)+t*np.sin(ang)
          22 +    start=p+n*0.1-ud*0.12
          23 +    if dist_T(start,w,L,lv)<0.105: continue
          24 +    mv=S.goto_local(start)
          25 +    if mv>1e-9: continue
          26 +    v=rng.choice([0.01,0.02,0.03,0.0499]); nst=int(0.12/v)+int(rng.integers(4,10))
          27 +    for k in range(nst):
          28 +        o=S.obs.copy(); u=rot(o[2])@ud*v
          29 +        o2=S.step(u)
          30 +        data.append(np.r_[seed,e,k,o[0:3],o[16:18],u,o2[0:3],o2[16:18],w,L,lv,v,ang])
          31 +np.save(f'probe_dyn_data_{sys.argv[1]}.npy',np.array(data)); print(len(data))
diff --git a/probe_dyn_data_1.npy b/probe_dyn_data_1.npy
new file mode 100644
index 0000000..6ad3f79
Binary files /dev/null and b/probe_dyn_data_1.npy differ
diff --git a/probe_dyn_data_2.npy b/probe_dyn_data_2.npy
new file mode 100644
index 0000000..9cd1e76
Binary files /dev/null and b/probe_dyn_data_2.npy differ
diff --git a/probe_dyn_data_3.npy b/probe_dyn_data_3.npy
new file mode 100644
index 0000000..4c184c6
Binary files /dev/null and b/probe_dyn_data_3.npy differ
diff --git a/probe_dyn_data_4.npy b/probe_dyn_data_4.npy
new file mode 100644
index 0000000..24a52ae
Binary files /dev/null and b/probe_dyn_data_4.npy differ
diff --git a/probe_dyn_e.py b/probe_dyn_e.py
new file mode 100644
index 0000000..984c95f
--- /dev/null
+++ b/probe_dyn_e.py
@@ -0,0 +1,9 @@
           1 +from probe_dyn_lib import *
           2 +from probe_dyn_b import exp
           3 +for v in [0.01,0.0499]:
           4 +  for a in [10,20,30,45,60]:
           5 +    t=np.radians(a)
           6 +    exp(f'e stem bottom oblique {a}',[-np.sin(t)*0.25,-1.2-np.cos(t)*0.25],[np.sin(t),np.cos(t)],v,int(0.35/v),verbose=(v==0.01 and a in(20,45)))
           7 +  for a in [20,45]:
           8 +    t=np.radians(a)
           9 +    exp(f'e bar top x0 oblique {a}',[-np.sin(t)*0.3,0.3*np.cos(t)],[np.sin(t),-np.cos(t)],v,int(0.35/v))
diff --git a/probe_dyn_first.py b/probe_dyn_first.py
new file mode 100644
index 0000000..d450054
--- /dev/null
+++ b/probe_dyn_first.py
@@ -0,0 +1,15 @@
           1 +import numpy as np
           2 +exec(open('probe_dyn_fit.py').read().split("rows=[]")[0])
           3 +moved=np.abs(D[:,10:13]-D[:,3:6]).max(1)>1e-8
           4 +out=[]
           5 +for i in range(1,len(D)):
           6 +    r=D[i]
           7 +    if not moved[i] or (moved[i-1] and D[i-1,1]==r[1]): continue
           8 +    R=rot(r[5]).T; q=R@(r[6:8]-r[3:5]); u=R@r[8:10]
           9 +    p,n,d=closest(q,*r[15:18]); g=d-0.1; un=-(u@n)
          10 +    # post-step robot relative to post-step block
          11 +    R2=rot(r[12]).T; q2=R2@(r[13:15]-r[10:13][:2]); p2,n2,d2=closest(q2,*r[15:18])
          12 +    out.append([r[18],g,un,un-g,d2-0.1])
          13 +O=np.array(out)
          14 +print('first-contact steps: v, pre-gap, u_n, penetration-if-static(u_n-g), post-step gap')
          15 +for o in O[np.argsort(O[:,3])][::max(1,len(O)//15)]: print(o.round(4))
diff --git a/probe_dyn_fit.py b/probe_dyn_fit.py
new file mode 100644
index 0000000..3e46472
--- /dev/null
+++ b/probe_dyn_fit.py
@@ -0,0 +1,66 @@
           1 +import numpy as np, glob
           2 +from scipy.optimize import least_squares
           3 +from probe_dyn_lib import rot, wrap
           4 +np.set_printoptions(precision=4,suppress=True)
           5 +D=np.concatenate([np.load(f) for f in sorted(glob.glob('probe_dyn_data_*.npy'))])
           6 +# cols: seed e k | bx by bt(3:6) | rx ry(6:8) | ux uy(8:10) | b2(10:13) | r2(13:15) | w L lv(15:18) | v ang
           7 +def closest(q,w,L,lv):
           8 +    best=None
           9 +    for x0,x1,y0,y1 in [(-L/2,L/2,-w,0),(-w/2,w/2,-w-lv,-w)]:
          10 +        c=np.array([np.clip(q[0],x0,x1),np.clip(q[1],y0,y1)]); d=np.linalg.norm(q-c)
          11 +        if best is None or d<best[0]: best=(d,c)
          12 +    d,c=best; return c,(q-c)/max(d,1e-9),d
          13 +rows=[]
          14 +moved=np.abs(D[:,10:13]-D[:,3:6]).max(1)>1e-8
          15 +for i in range(len(D)):
          16 +    r=D[i]
          17 +    if not moved[i] or i==0 or not moved[i-1] or D[i-1,1]!=r[1]: continue
          18 +    R=rot(r[5]).T
          19 +    q=R@(r[6:8]-r[3:5]); u=R@r[8:10]
          20 +    tw=np.r_[R@(r[10:12]-r[3:5]), wrap(r[12]-r[5])]
          21 +    p,n,d=closest(q,*r[15:18])
          22 +    rows.append(np.r_[p,n,u,tw,r[15:18],d,r[18],r[19],r[0]])
          23 +X=np.array(rows); print('steady contact steps',len(X))
          24 +P,N,U,TW,G,DD=X[:,0:2],X[:,2:4],X[:,4:6],X[:,6:9],X[:,9:12],X[:,12]
          25 +print('robot-surface distance at pre-step (gap+r): per speed')
          26 +for v in [0.01,0.02,0.03,0.0499]:
          27 +    m=np.isclose(X[:,13],v); print(' v',v,'dist-0.1 mean',(DD[m]-0.1).mean().round(4),'n',m.sum())
          28 +def centroid(w,L,lv):
          29 +    A1,A2=L*w,w*lv; cy=(A1*(-w/2)+A2*(-w-lv/2))/(A1+A2)
          30 +    I1=A1*((L**2+w**2)/12+(w/2)**2); I2=A2*((w**2+lv**2)/12+(w+lv/2)**2)
          31 +    return cy,(I1+I2)/(A1+A2)-cy**2
          32 +def predict(th,X,ret_mode=False):
          33 +    dcx,dcy,sc2,mu=th; out=[];modes=[]
          34 +    for x in X:
          35 +        p,n,u=x[0:2],x[2:4],x[4:6]; w,L,lv=x[9:12]
          36 +        cy0,c20=centroid(w,L,lv); c0=np.array([dcx,cy0+dcy]); c2=c20*sc2
          37 +        rr=p-c0; rp=np.array([-rr[1],rr[0]])
          38 +        M=c2*np.eye(2)+np.outer(rp,rp)
          39 +        f=np.linalg.solve(M,u); fn=-f@n; t=np.array([-n[1],n[0]]); ft=f@t
          40 +        mode=0
          41 +        if abs(ft)>mu*fn:
          42 +            # sliding: force on cone edge; sign of ft same as sticking solution
          43 +            f=-n+np.sign(ft)*mu*t; vp=M@f; lam=(u@n)/(vp@n); f=f*lam; mode=1
          44 +        V=c2*f; om=rr[0]*f[1]-rr[1]*f[0]
          45 +        Vo=V+om*np.array([c0[1],-c0[0]])  # om x (0-c0)
          46 +        out.append(np.r_[Vo,om]); modes.append(mode)
          47 +    return (np.array(out),np.array(modes)) if ret_mode else np.array(out)
          48 +def res(th): return ((predict(th,X)-X[:,6:9])/X[:,13:14]).ravel()
          49 +for th0 in [[0,0,1,0.5]]:
          50 +    s=least_squares(res,th0,x_scale=[0.05,0.05,0.1,0.1])
          51 +    print('fit dcx,dcy,c2scale,mu',s.x,'rms rel',np.sqrt(np.mean(s.fun**2)))
          52 +pr,md=predict(s.x,X,True); e=np.abs(pr-X[:,6:9])/X[:,13:14]
          53 +print('sliding frac',md.mean(),'rel err mean per comp',e.mean(0),'95pct',np.percentile(e,95,axis=0))
          54 +print('baseline (dcx=dcy=0,sc=1) rms',np.sqrt(np.mean(res([0,0,1,s.x[3]])**2)))
          55 +for mu in [0.2,0.3,0.4,0.5,0.7,1.0,5]:
          56 +    print(' mu',mu,'rms',np.sqrt(np.mean(res([s.x[0],s.x[1],s.x[2],mu])**2)).round(4))
          57 +np.save('probe_dyn_X.npy',X)
          58 +for sd in np.unique(X[:,15]):
          59 +    m=X[:,15]==sd; Xs=X[m]
          60 +    s2=least_squares(lambda th:((predict(th,Xs)-Xs[:,6:9])/Xs[:,13:14]).ravel(),s.x)
          61 +    print('seed',int(sd),'n',m.sum(),'fit',s2.x.round(4),'dims',Xs[0,9:12].round(3),'centroid cy,c2',np.round(centroid(*Xs[0,9:12]),4))
          62 +# robot kinematic check
          63 +rd=np.linalg.norm(D[:,13:15]-D[:,6:8]-D[:,8:10],axis=1); print('max |robot disp - u|',rd.max())
          64 +# per-speed error
          65 +for v in [0.01,0.02,0.03,0.0499]:
          66 +    m=np.isclose(X[:,13],v); print('v',v,'rel err',e[m].mean(0).round(4))
diff --git a/probe_dyn_geo.py b/probe_dyn_geo.py
new file mode 100644
index 0000000..9f1c7e1
--- /dev/null
+++ b/probe_dyn_geo.py
@@ -0,0 +1,16 @@
           1 +from probe_dyn_lib import *
           2 +S=Sim()
           3 +def probe(start,d,seed=81,spd=0.004,n=200):
           4 +    S.reset(seed); S.goto_local(start); o0=S.obs.copy()
           5 +    rp0=w2l(o0,o0[16:18])
           6 +    for i in range(n):
           7 +        o=S.obs.copy(); S.step(rot(o[2])@np.array(d)*spd)
           8 +        if np.abs(S.obs[0:3]-o[0:3]).max()>1e-7:
           9 +            return w2l(o,o[16:18]), w2l(S.obs,S.obs[16:18]), rp0
          10 +    return None,None,rp0
          11 +o=S.reset(81); print(o[0:3],o[12:15])
          12 +for name,st,d in [('stem bottom x0',[0,-1.45],[0,1]),('stem bottom x.05',[0.05,-1.45],[0,1]),('stem bottom x.1',[0.1,-1.45],[0,1]),
          13 +                  ('bar top x0',[0,0.45],[0,-1]),('bar top x.5',[0.5,0.45],[0,-1]),('bar top x-.5',[-0.5,0.45],[0,-1]),
          14 +                  ('bar under x.4',[0.4,-0.5],[0,1]),('bar end +x',[0.9,0],[-1,0]),('bar end -x',[-0.9,0],[1,0]),
          15 +                  ('stem side +x y-.6',[0.6,-0.6],[-1,0]),('stem side -x y-.6',[-0.6,-0.6],[1,0])]:
          16 +    a,b,r0=probe(st,d); print(name,'start',r0,'contact at robot local',a)
diff --git a/probe_dyn_lib.py b/probe_dyn_lib.py
new file mode 100644
index 0000000..e2956d9
--- /dev/null
+++ b/probe_dyn_lib.py
@@ -0,0 +1,43 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=4, suppress=True)
           4 +A=0.0499
           5 +def rot(t): c,s=np.cos(t),np.sin(t); return np.array([[c,-s],[s,c]])
           6 +def w2l(obs,p): return rot(obs[2]).T@(np.asarray(p)-obs[0:2])
           7 +def l2w(obs,p): return obs[0:2]+rot(obs[2])@np.asarray(p)
           8 +def wrap(a): return (a+np.pi)%(2*np.pi)-np.pi
           9 +class Sim:
          10 +    def __init__(s): s.env=make_env()
          11 +    def reset(s,seed): s.obs,_=s.env.reset(seed=seed); return s.obs
          12 +    def step(s,a):
          13 +        a=np.clip(np.asarray(a,float),-A,A)
          14 +        s.obs,*_=s.env.step(a); return s.obs
          15 +    def moveto(s,tgt,n=400,tol=1e-4,spd=A):
          16 +        for i in range(n):
          17 +            d=tgt-s.obs[16:18]
          18 +            if np.linalg.norm(d)<tol: break
          19 +            m=np.max(np.abs(d)); 
          20 +            a=d if m<=spd else d/m*spd
          21 +            s.step(a)
          22 +    def goto_local(s,pl,R=1.05,center=(0,-0.45)):
          23 +        """navigate around block via circle of radius R around local center, then to local point pl"""
          24 +        o=s.obs; c=np.array(center); b0=o[0:3].copy()
          25 +        rl=w2l(o,o[16:18])-c; tl=np.asarray(pl)-c
          26 +        a0=np.arctan2(rl[1],rl[0]); a1=np.arctan2(tl[1],tl[0])
          27 +        # go radially out to R
          28 +        s.moveto(l2w(o,c+R*np.array([np.cos(a0),np.sin(a0)])*max(1,np.linalg.norm(rl)/R)))
          29 +        da=wrap(a1-a0); n=int(abs(da)/0.1)+1
          30 +        for k in range(1,n+1):
          31 +            a=a0+da*k/n; s.moveto(l2w(o,c+R*np.array([np.cos(a),np.sin(a)])))
          32 +        s.moveto(l2w(o,pl))
          33 +        moved=np.abs(s.obs[0:3]-b0).max()
          34 +        return moved
          35 +    def push(s,dir_local,speed,n,log=True):
          36 +        rows=[]
          37 +        for i in range(n):
          38 +            o=s.obs.copy(); d=rot(o[2])@np.asarray(dir_local,float); d=d/np.linalg.norm(d)*speed
          39 +            o2=s.step(d)
          40 +            dl=rot(o[2]).T@(o2[0:2]-o[0:2]); dth=wrap(o2[2]-o[2])
          41 +            rp=w2l(o,o[16:18]); rp2=w2l(o2,o2[16:18])
          42 +            rows.append(np.r_[dl,dth,rp,rp2,o2[16:18]-o[16:18]])
          43 +        return np.array(rows)
diff --git a/probe_geom_1.py b/probe_geom_1.py
new file mode 100644
index 0000000..cf36f7a
--- /dev/null
+++ b/probe_geom_1.py
@@ -0,0 +1,51 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +np.set_printoptions(precision=4, suppress=True)
           4 +env = make_env()
           5 +def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
           6 +def step(a):
           7 +    global obs
           8 +    obs,r,te,tr,info = env.step(np.clip(a,-0.0499,0.0499)); return obs
           9 +def goto(tgt, tol=1e-4, n=400):
          10 +    for i in range(n):
          11 +        d = tgt-obs[16:18]
          12 +        if np.linalg.norm(d)<tol: break
          13 +        step(d)
          14 +def route(tgt, cen, Rr):
          15 +    # go radially out to Rr, arc, then go to tgt
          16 +    p = obs[16:18]; v=p-cen; a0=np.arctan2(v[1],v[0])
          17 +    goto(cen+Rr*np.array([np.cos(a0),np.sin(a0)]))
          18 +    v=tgt-cen; a1=np.arctan2(v[1],v[0])
          19 +    da=(a1-a0+np.pi)%(2*np.pi)-np.pi
          20 +    for k in range(1,41):
          21 +        a=a0+da*k/40; goto(cen+Rr*np.array([np.cos(a),np.sin(a)]),tol=1e-3)
          22 +    goto(tgt)
          23 +def probe(seed, start_local, dir_local, name):
          24 +    global obs
          25 +    obs,_=env.reset(seed=seed)
          26 +    pose=obs[0:3].copy(); w,lh,lv=obs[12],obs[13],obs[14]
          27 +    Rm=R(pose[2]); cen=pose[:2]+Rm@np.array([0,-lv/2])
          28 +    start=pose[:2]+Rm@np.array(start_local)
          29 +    route(start,cen,1.05)
          30 +    assert np.allclose(obs[0:3],pose), ('moved en route',obs[0:3],pose)
          31 +    d=Rm@np.array(dir_local); d/=np.linalg.norm(d)
          32 +    prev=obs[16:18].copy()
          33 +    for i in range(2000):
          34 +        step(d*0.001)
          35 +        if not np.allclose(obs[0:3],pose,atol=1e-7):
          36 +            loc_prev=Rm.T@(prev-pose[:2]); loc_now=Rm.T@(obs[16:18]-pose[:2])
          37 +            print(f"seed{seed} {name}: w={w:.4f} lh={lh:.4f} lv={lv:.4f} contact robot local prev={loc_prev} now={loc_now} dpose={obs[0:3]-pose}")
          38 +            return
          39 +        prev=obs[16:18].copy()
          40 +    print(name,'no contact')
          41 +for seed in [int(s) for s in sys.argv[1:]]:
          42 +    obs,_=env.reset(seed=seed); w,lh,lv=obs[12],obs[13],obs[14]
          43 +    print('pose',obs[0:3],'robot',obs[16:18],'goal',obs[29:32])
          44 +    if 0: probe(seed,[0, 0.4],[0,-1],'bar top (x=0)')
          45 +    probe(seed,[0.3, 0.4],[0,-1],'bar top (x=0.3)')
          46 +    probe(seed,[0,-lv-0.3],[0,1],'stem bottom')
          47 +    probe(seed,[lh/2+0.3,0],[-1,0],'bar end +x (y=0)')
          48 +    probe(seed,[-lh/2-0.3,0],[1,0],'bar end -x (y=0)')
          49 +    probe(seed,[0.35,-lv/2],[-1,0],'stem side +x mid')
          50 +    probe(seed,[-0.35,-lv/2],[1,0],'stem side -x mid')
          51 +    probe(seed,[0.4,-0.45],[0,1],'bar underside x=0.4')
diff --git a/probe_geom_2.py b/probe_geom_2.py
new file mode 100644
index 0000000..0243335
--- /dev/null
+++ b/probe_geom_2.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=4, suppress=True)
           4 +exec(open('probe_geom_1.py').read().split('def probe')[0])
           5 +obs,_=env.reset(seed=12)
           6 +w,lh,lv=obs[12],obs[13],obs[14]
           7 +ths=[obs[2]]; trace=[]
           8 +for it in range(60):
           9 +    pose=obs[0:3].copy(); Rm=R(pose[2]); cen=pose[:2]+Rm@np.array([0,-lv/2])
          10 +    start=pose[:2]+Rm@np.array([lh/2-0.08,-w-0.13])
          11 +    route(start,cen,1.05)
          12 +    d=Rm@np.array([0,1.0])
          13 +    for k in range(8):
          14 +        step(d*0.04); ths.append(obs[2]); trace.append((obs[2],r if False else 0))
          15 +    # back off
          16 +    for k in range(3): step(-d*0.04)
          17 +    if it%5==0: print(it, obs[0:3])
          18 +ths=np.array(ths)
          19 +print('theta min/max',ths.min(),ths.max())
          20 +jumps=np.where(np.abs(np.diff(ths))>1)[0]
          21 +for j in jumps[:6]: print('jump',ths[j],'->',ths[j+1])
          22 +print('unwrapped total rotation', np.unwrap(ths)[-1]-ths[0])
diff --git a/probe_geom_3.py b/probe_geom_3.py
new file mode 100644
index 0000000..ccc0035
--- /dev/null
+++ b/probe_geom_3.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=4, suppress=True)
           4 +exec(open('probe_geom_1.py').read().split('def probe')[0])
           5 +def verts(o):
           6 +    w,lh,lv=o[12],o[13],o[14]; Rm=R(o[2])
           7 +    loc=np.array([[-lh/2,0],[lh/2,0],[lh/2,-w],[-lh/2,-w],[-w/2,-w-lv],[w/2,-w-lv]])
           8 +    return o[0:2]+loc@Rm.T
           9 +obs,_=env.reset(seed=12)
          10 +w,lh,lv=obs[12],obs[13],obs[14]
          11 +for it in range(40):
          12 +    pose=obs[0:3].copy(); Rm=R(pose[2]); cen=pose[:2]+Rm@np.array([0,-lv/2])
          13 +    V=verts(obs); 
          14 +    # start at right of block at centroid height
          15 +    start=np.array([V[:,0].max()+0.2, cen[1]])
          16 +    route(start,cen,1.05)
          17 +    for k in range(40):
          18 +        step(np.array([-0.04,0.0]))
          19 +        if obs[16]<=0.1001: break
          20 +    V=verts(obs)
          21 +    print(it,'pose',obs[0:3],'min vert x %.4f'%V[:,0].min(),'robot',obs[16:18])
          22 +    if obs[16]<=0.2: break
diff --git a/probe_geom_4.py b/probe_geom_4.py
new file mode 100644
index 0000000..d7a3cfd
--- /dev/null
+++ b/probe_geom_4.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +np.set_printoptions(precision=4, suppress=True)
           4 +exec(open('probe_geom_3.py').read().split('obs,_=env.reset')[0])
           5 +obs,_=env.reset(seed=12)
           6 +w,lh,lv=obs[12],obs[13],obs[14]
           7 +for it in range(2):
           8 +    pose=obs[0:3].copy(); Rm=R(pose[2]); cen=pose[:2]+Rm@np.array([0,-lv/2])
           9 +    V=verts(obs); start=np.array([V[:,0].max()+0.2, cen[1]])
          10 +    route(start,cen,1.05)
          11 +    for k in range(60):
          12 +        p=obs[16:18].copy(); b=obs[0:3].copy()
          13 +        step(np.array([-0.04,0.0]))
          14 +        if it==1 and k>=36: print(k,'robot dx %.4f'%(obs[16]-p[0]),'block d',obs[0:3]-b,'minx %.4f'%verts(obs)[:,0].min())
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..8f053e5
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,24 @@
           1 +import sys, time, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +seeds = range(int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else range(10)
           5 +env = make_env()
           6 +res = []
           7 +for sd in seeds:
           8 +    obs, info = env.reset(seed=sd)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    ok = False
          13 +    for t in range(env.max_steps):
          14 +        a = ap.get_action(obs)
          15 +        obs, r, term, trunc, info = env.step(a)
          16 +        if term:
          17 +            ok = True; break
          18 +        if trunc: break
          19 +    dt = time.time() - t0
          20 +    g = obs[29:32]
          21 +    err = (obs[0]-g[0], obs[1]-g[1], (obs[2]-g[2]+np.pi)%(2*np.pi)-np.pi)
          22 +    res.append(ok)
          23 +    print(f"seed {sd} ok={ok} steps={t+1} time={dt:.1f}s err={np.round(err,3)}", flush=True)
          24 +print('success', np.mean(res), sum(res), len(res))
diff --git a/test_model.py b/test_model.py
new file mode 100644
index 0000000..eaa4898
--- /dev/null
+++ b/test_model.py
@@ -0,0 +1,24 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from tmodel import TGeom, sim_step, wrap, corners_world
           4 +env = make_env()
           5 +rng=np.random.default_rng(0)
           6 +rows=[]
           7 +for seed in range(4):
           8 +    obs,_=env.reset(seed=seed)
           9 +    g=TGeom(*obs[12:15])
          10 +    for k in range(150):
          11 +        tgt = obs[0:2] + rng.normal(0,0.4,2)
          12 +        d=tgt-obs[16:18]; a=np.clip(d/max(np.linalg.norm(d),1e-9)*0.0499,-0.0499,0.0499)
          13 +        A=lambda v: np.array([v])
          14 +        bx,by,bt,rx,ry=sim_step(g,A(obs[0]),A(obs[1]),A(obs[2]),A(obs[16]),A(obs[17]),a[0],a[1])
          15 +        obs2,*_=env.step(a)
          16 +        moved=np.abs(obs2[0:3]-obs[0:3]).max()
          17 +        e=np.r_[obs2[0]-bx[0],obs2[1]-by[0],wrap(obs2[2]-bt[0])]
          18 +        cx,cy=corners_world(g,obs2[0],obs2[1],obs2[2]); inside=(cx.min()>0.15)&(cx.max()<4.85)&(cy.min()>0.15)&(cy.max()<4.85)
          19 +        c_,s_=np.cos(obs[2]),np.sin(obs[2]); lx=c_*(obs[16]-obs[0])+s_*(obs[17]-obs[1]); ly=-s_*(obs[16]-obs[0])+c_*(obs[17]-obs[1]); px,py,nx,ny,dd=g.closest(lx,ly); lu=np.array([c_*a[0]+s_*a[1],-s_*a[0]+c_*a[1]]); un=-(lu[0]*nx+lu[1]*ny)
          20 +        if inside and moved>1e-7: rows.append((dd-0.1,un,np.abs(e).max(),moved))
          21 +        obs=obs2
          22 +R=np.array(rows)
          23 +print('n',len(R),'mean err',R[:,2].mean(),'p95',np.percentile(R[:,2],95),'max',R[:,2].max())
          24 +for r in R[np.argsort(-R[:,2])][:8]: print(np.round(r,4))
diff --git a/tmodel.py b/tmodel.py
new file mode 100644
index 0000000..033be86
--- /dev/null
+++ b/tmodel.py
@@ -0,0 +1,164 @@
           1 +"""Quasi-static push model of the T block + geometry helpers (vectorized)."""
           2 +import numpy as np
           3 +
           4 +R_ROBOT = 0.1
           5 +MU = 1.0
           6 +
           7 +
           8 +def wrap(a):
           9 +    return (a + np.pi) % (2 * np.pi) - np.pi
          10 +
          11 +
          12 +class TGeom:
          13 +    def __init__(self, w, L, lv):
          14 +        self.w, self.L, self.lv = w, L, lv
          15 +        # rects in local frame: (x0,x1,y0,y1)
          16 +        self.rects = [(-L / 2, L / 2, -w, 0.0), (-w / 2, w / 2, -w - lv, -w)]
          17 +        A1, A2 = L * w, w * lv
          18 +        cy = (A1 * (-w / 2) + A2 * (-w - lv / 2)) / (A1 + A2)
          19 +        I1 = A1 * ((L ** 2 + w ** 2) / 12 + (w / 2) ** 2)
          20 +        I2 = A2 * ((w ** 2 + lv ** 2) / 12 + (w + lv / 2) ** 2)
          21 +        self.cy = cy
          22 +        self.c2 = (I1 + I2) / (A1 + A2) - cy ** 2
          23 +
          24 +    def closest(self, qx, qy):
          25 +        """Vectorized closest point on T (local frame). Returns px,py,nx,ny,dist."""
          26 +        best = None
          27 +        for (x0, x1, y0, y1) in self.rects:
          28 +            cx = np.clip(qx, x0, x1)
          29 +            cy = np.clip(qy, y0, y1)
          30 +            d = np.hypot(qx - cx, qy - cy)
          31 +            if best is None:
          32 +                best = [cx, cy, d]
          33 +            else:
          34 +                m = d < best[2]
          35 +                best[0] = np.where(m, cx, best[0])
          36 +                best[1] = np.where(m, cy, best[1])
          37 +                best[2] = np.where(m, d, best[2])
          38 +        px, py, d = best
          39 +        dd = np.maximum(d, 1e-9)
          40 +        nx = (qx - px) / dd
          41 +        ny = (qy - py) / dd
          42 +        return px, py, nx, ny, d
          43 +
          44 +    def boundary_points(self, spacing=0.06):
          45 +        """Sample boundary points with outward normals (local frame), excluding
          46 +        points unreachable by the robot disc."""
          47 +        w, L, lv = self.w, self.L, self.lv
          48 +        segs = []
          49 +        # bar top: y=0, normal +y
          50 +        segs.append(((-L / 2, 0), (L / 2, 0), (0, 1)))
          51 +        # bar ends
          52 +        segs.append(((L / 2, -w), (L / 2, 0), (1, 0)))
          53 +        segs.append(((-L / 2, -w), (-L / 2, 0), (-1, 0)))
          54 +        # bar underside (both sides of stem), normal -y
          55 +        segs.append(((w / 2, -w), (L / 2, -w), (0, -1)))
          56 +        segs.append(((-L / 2, -w), (-w / 2, -w), (0, -1)))
          57 +        # stem sides
          58 +        segs.append(((w / 2, -w - lv), (w / 2, -w), (1, 0)))
          59 +        segs.append(((-w / 2, -w - lv), (-w / 2, -w), (-1, 0)))
          60 +        # stem bottom
          61 +        segs.append(((-w / 2, -w - lv), (w / 2, -w - lv), (0, -1)))
          62 +        pts = []
          63 +        for a, b, n in segs:
          64 +            a = np.array(a, float); b = np.array(b, float)
          65 +            ln = np.linalg.norm(b - a)
          66 +            k = max(2, int(np.ceil(ln / spacing)) + 1)
          67 +            for t in np.linspace(0, 1, k):
          68 +                p = a + t * (b - a)
          69 +                pts.append((p[0], p[1], n[0], n[1]))
          70 +        pts = np.array(pts)
          71 +        # robot center at contact
          72 +        cx = pts[:, 0] + pts[:, 2] * R_ROBOT
          73 +        cy = pts[:, 1] + pts[:, 3] * R_ROBOT
          74 +        _, _, _, _, d = self.closest(cx, cy)
          75 +        ok = d > R_ROBOT - 1e-6
          76 +        pts = pts[ok]
          77 +        # dedupe
          78 +        _, idx = np.unique(np.round(pts, 5), axis=0, return_index=True)
          79 +        return pts[np.sort(idx)]
          80 +
          81 +
          82 +GAP_K = 0.27
          83 +
          84 +
          85 +def _push(g, c, s, bx, by, bt, lx, ly, lux, luy):
          86 +    """Apply contact displacement (lux,luy) (local frame) at robot local pos lx,ly."""
          87 +    px, py, nx, ny, d = g.closest(lx, ly)
          88 +    c0x, c0y = 0.0, g.cy
          89 +    rrx, rry = px - c0x, py - c0y
          90 +    rpx, rpy = -rry, rrx
          91 +    c2 = g.c2
          92 +    M11 = c2 + rpx * rpx
          93 +    M12 = rpx * rpy
          94 +    M22 = c2 + rpy * rpy
          95 +    det = M11 * M22 - M12 * M12
          96 +    fx = (M22 * lux - M12 * luy) / det
          97 +    fy = (-M12 * lux + M11 * luy) / det
          98 +    tx, ty = -ny, nx
          99 +    fn = -(fx * nx + fy * ny)
         100 +    ft = fx * tx + fy * ty
         101 +    slide = np.abs(ft) > MU * fn
         102 +    sg = np.sign(ft)
         103 +    gx = -nx + sg * MU * tx
         104 +    gy = -ny + sg * MU * ty
         105 +    vpx = M11 * gx + M12 * gy
         106 +    vpy = M12 * gx + M22 * gy
         107 +    den = vpx * nx + vpy * ny
         108 +    den = np.where(np.abs(den) < 1e-12, -1e-12, den)
         109 +    lam = (lux * nx + luy * ny) / den
         110 +    fx = np.where(slide, gx * lam, fx)
         111 +    fy = np.where(slide, gy * lam, fy)
         112 +    Vx, Vy = c2 * fx, c2 * fy
         113 +    om = rrx * fy - rry * fx
         114 +    Vox = Vx + om * c0y
         115 +    Voy = Vy - om * c0x
         116 +    return bx + c * Vox - s * Voy, by + s * Vox + c * Voy, bt + om
         117 +
         118 +
         119 +def sim_step(g, bx, by, bt, rx, ry, ux, uy, nsub=3):
         120 +    """One env step, vectorized. Robot moves by (ux,uy) world.
         121 +    Returns new bx,by,bt,rx,ry."""
         122 +    c, s = np.cos(bt), np.sin(bt)
         123 +    lx0 = c * (rx - bx) + s * (ry - by)
         124 +    ly0 = -s * (rx - bx) + c * (ry - by)
         125 +    lux = c * ux + s * uy
         126 +    luy = -s * ux + c * uy
         127 +    px, py, nx, ny, d = g.closest(lx0, ly0)
         128 +    gap = d - R_ROBOT
         129 +    un = -(lux * nx + luy * ny)
         130 +    eff = (1.0 + GAP_K) * un - np.maximum(gap, 0.0)
         131 +    active = (un > 1e-12) & (eff > 0)
         132 +    frac = np.where(active, eff / np.maximum(un, 1e-12), 0.0)
         133 +    # contact displacement: first part (1-frac) free (or extra), rest pushes
         134 +    bx1, by1, bt1 = bx, by, bt
         135 +    if np.any(active):
         136 +        # start from robot at contact: shift robot local pos so it touches
         137 +        sx = lx0 - nx * np.maximum(gap, 0.0)
         138 +        sy = ly0 - ny * np.maximum(gap, 0.0)
         139 +        dux, duy = lux * frac / nsub, luy * frac / nsub
         140 +        cx_, cy_ = sx, sy
         141 +        for k in range(nsub):
         142 +            nbx, nby, nbt = _push(g, np.cos(bt1), np.sin(bt1), bx1, by1, bt1, cx_, cy_, dux, duy)
         143 +            # robot contact point in world after moving; re-express in new frame
         144 +            cc, ss = np.cos(bt1), np.sin(bt1)
         145 +            wx = bx1 + cc * (cx_ + dux) - ss * (cy_ + duy)
         146 +            wy = by1 + ss * (cx_ + dux) + cc * (cy_ + duy)
         147 +            cn, sn = np.cos(nbt), np.sin(nbt)
         148 +            cx_ = cn * (wx - nbx) + sn * (wy - nby)
         149 +            cy_ = -sn * (wx - nbx) + cn * (wy - nby)
         150 +            bx1 = np.where(active, nbx, bx1)
         151 +            by1 = np.where(active, nby, by1)
         152 +            bt1 = np.where(active, nbt, bt1)
         153 +    return bx1, by1, bt1, rx + ux, ry + uy
         154 +
         155 +
         156 +def corners_world(g, bx, by, bt):
         157 +    """All rect corners in world, arrays shape (8, K) for x and y."""
         158 +    c, s = np.cos(bt), np.sin(bt)
         159 +    xs, ys = [], []
         160 +    for (x0, x1, y0, y1) in g.rects:
         161 +        for (lx, ly) in ((x0, y0), (x0, y1), (x1, y0), (x1, y1)):
         162 +            xs.append(bx + c * lx - s * ly)
         163 +            ys.append(by + s * lx + c * ly)
         164 +    return np.array(xs), np.array(ys)
```

</details>

<a id="C003"></a>
### C003 · retreat after push before navigating

Commit `076d2b66df7c445182abc5067bd3ceeb37c099de`; parents: c66d154cb4c7da49470d7e7a6e1aab4762c8fb29. Recorded author date: 2026-09-28T19:00:44+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0307](01_timeline.md#E0307): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_076d2b6_approach.py) · [Exact all-file diff](evidence/diffs/C003_076d2b6.diff)

[Previous saved controller snapshot](evidence/versions/C002_c66d154_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f059a65..b32c32b 100644
--- a/approach.py
+++ b/approach.py
@@ -158,7 +158,20 @@ class GeneratedApproach:
  158    158          if len(idx) == 0:
  159    159              return None
  160    160          pre = np.stack([wpx[idx], wpy[idx]], 1)
  161        -        tdist, pathf = self._plan_paths(pose, robot, pre)
         161 +        # retreat if robot is close to the block
         162 +        rlx = c * (robot[0] - pose[0]) + s * (robot[1] - pose[1])
         163 +        rly = -s * (robot[0] - pose[0]) + c * (robot[1] - pose[1])
         164 +        _, _, rnx, rny, rd = g.closest(np.array([rlx]), np.array([rly]))
         165 +        retreat = None
         166 +        if rd[0] < R_ROBOT + 0.03:
         167 +            back = R_ROBOT + 0.035 - rd[0]
         168 +            cand = robot + back * np.array([c * rnx[0] - s * rny[0], s * rnx[0] + c * rny[0]])
         169 +            if LO < cand[0] < HI and LO < cand[1] < HI:
         170 +                retreat = cand
         171 +        start = robot if retreat is None else retreat
         172 +        tdist, pathf = self._plan_paths(pose, start, pre)
         173 +        if retreat is not None:
         174 +            tdist = tdist + np.hypot(*(retreat - robot))
  162    175          tdist = tdist + 0.045
  163    176          # world inward normal
  164    177          nwx = -(c * pts[idx, 2] - s * pts[idx, 3])
@@ -201,6 +214,8 @@ class GeneratedApproach:
  201    214              return None
  202    215          n = int(best_n[j])
  203    216          wp = pathf(ci[j])
         217 +        if retreat is not None:
         218 +            wp = [retreat] + wp
  204    219          acts = []
  205    220          cur = robot.copy()
  206    221          for w in wp + [np.array([wcx[idx][ci[j]], wcy[idx][ci[j]]])]:
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..13fcf11
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,15 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +sd=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 1000
           5 +env = make_env(); obs,info=env.reset(seed=sd)
           6 +np.set_printoptions(precision=3, suppress=True)
           7 +print('init', obs[0:3], obs[16:18], obs[29:32], obs[12:15])
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           9 +for t in range(N):
          10 +    q=len(ap.queue)
          11 +    a=ap.get_action(obs)
          12 +    if len(ap.queue)>=q and hasattr(ap,'dbg'): print(t, 'pose',obs[0:3],'robot',obs[16:18],'dbg',np.round(ap.dbg,3))
          13 +    obs,r,term,trunc,info=env.step(a)
          14 +    if term: print('solved',t); break
          15 +print('final', obs[0:3])
diff --git a/res_0.txt b/res_0.txt
new file mode 100644
index 0000000..5d88aea
--- /dev/null
+++ b/res_0.txt
@@ -0,0 +1,41 @@
           1 +seed 0 ok=True steps=146 time=2.9s err=[ 0.006 -0.016 -0.012]
           2 +seed 1 ok=True steps=158 time=2.2s err=[0.01  0.008 0.053]
           3 +seed 2 ok=True steps=138 time=2.4s err=[ 0.002  0.006 -0.087]
           4 +seed 3 ok=True steps=102 time=1.8s err=[-0.017 -0.02   0.061]
           5 +seed 4 ok=True steps=108 time=1.7s err=[-0.007 -0.01  -0.078]
           6 +seed 5 ok=True steps=141 time=2.8s err=[ 0.02  -0.006 -0.069]
           7 +seed 6 ok=True steps=162 time=2.6s err=[ 0.007  0.021 -0.061]
           8 +seed 7 ok=True steps=172 time=2.0s err=[ 0.004  0.015 -0.094]
           9 +seed 8 ok=True steps=147 time=2.3s err=[-0.035 -0.007 -0.012]
          10 +seed 9 ok=True steps=144 time=2.5s err=[ 0.007  0.002 -0.075]
          11 +seed 10 ok=True steps=105 time=2.5s err=[ 0.015 -0.018  0.112]
          12 +seed 11 ok=True steps=105 time=1.8s err=[ 0.011 -0.024  0.044]
          13 +seed 12 ok=True steps=115 time=1.8s err=[0.018 0.016 0.094]
          14 +seed 13 ok=True steps=126 time=2.0s err=[-0.019 -0.003 -0.071]
          15 +seed 14 ok=True steps=146 time=1.7s err=[-0.009 -0.002  0.083]
          16 +seed 15 ok=True steps=60 time=0.8s err=[-0.012 -0.001  0.078]
          17 +seed 16 ok=True steps=133 time=2.7s err=[-0.007 -0.001  0.061]
          18 +seed 17 ok=True steps=82 time=1.7s err=[ 0.012 -0.031  0.078]
          19 +seed 18 ok=True steps=140 time=2.9s err=[-0.006  0.002  0.018]
          20 +seed 19 ok=True steps=85 time=1.7s err=[ 0.021 -0.007  0.045]
          21 +seed 20 ok=True steps=100 time=1.2s err=[ 0.002 -0.007 -0.061]
          22 +seed 21 ok=True steps=160 time=3.1s err=[0.024 0.013 0.101]
          23 +seed 22 ok=True steps=76 time=1.6s err=[ 0.015  0.018 -0.083]
          24 +seed 23 ok=True steps=48 time=1.0s err=[-0.007 -0.013 -0.054]
          25 +seed 24 ok=True steps=80 time=1.7s err=[-0.016  0.017 -0.017]
          26 +seed 25 ok=True steps=119 time=3.2s err=[ 0.017 -0.011  0.071]
          27 +seed 26 ok=True steps=139 time=2.5s err=[-0.012 -0.016  0.076]
          28 +seed 27 ok=True steps=178 time=2.4s err=[ 0.002  0.009 -0.014]
          29 +seed 28 ok=True steps=16 time=0.4s err=[ 0.023 -0.006 -0.073]
          30 +seed 29 ok=True steps=144 time=2.4s err=[-0.005 -0.007  0.073]
          31 +seed 30 ok=True steps=139 time=1.6s err=[ 0.032 -0.02   0.074]
          32 +seed 31 ok=True steps=81 time=1.3s err=[-0.016  0.017  0.028]
          33 +seed 32 ok=True steps=179 time=3.2s err=[-0.015 -0.001  0.081]
          34 +seed 33 ok=True steps=168 time=2.8s err=[0.012 0.006 0.103]
          35 +seed 34 ok=True steps=219 time=3.6s err=[-0.016  0.019  0.066]
          36 +seed 35 ok=True steps=102 time=2.1s err=[-0.003 -0.009 -0.07 ]
          37 +seed 36 ok=True steps=53 time=1.3s err=[ 0.023 -0.007  0.061]
          38 +seed 37 ok=True steps=160 time=2.9s err=[-0.006 -0.009 -0.054]
          39 +seed 38 ok=True steps=89 time=1.8s err=[ 0.008 -0.007  0.001]
          40 +seed 39 ok=True steps=53 time=1.1s err=[-0.004  0.012 -0.04 ]
          41 +success 1.0 40 40
diff --git a/res_1.txt b/res_1.txt
new file mode 100644
index 0000000..547a2a4
--- /dev/null
+++ b/res_1.txt
@@ -0,0 +1,41 @@
           1 +seed 40 ok=True steps=135 time=2.7s err=[-0.007  0.017  0.079]
           2 +seed 41 ok=True steps=159 time=2.4s err=[-0.017 -0.009 -0.052]
           3 +seed 42 ok=True steps=90 time=1.3s err=[ 0.005  0.002 -0.057]
           4 +seed 43 ok=True steps=144 time=2.8s err=[-0.012  0.001 -0.037]
           5 +seed 44 ok=True steps=212 time=3.9s err=[-0.014 -0.019  0.057]
           6 +seed 45 ok=True steps=82 time=1.8s err=[ 0.008  0.015 -0.076]
           7 +seed 46 ok=True steps=152 time=2.5s err=[-0.025  0.006 -0.058]
           8 +seed 47 ok=True steps=182 time=3.4s err=[0.013 0.008 0.091]
           9 +seed 48 ok=True steps=114 time=2.6s err=[ 0.001 -0.005  0.048]
          10 +seed 49 ok=True steps=190 time=3.5s err=[-0.009  0.001  0.001]
          11 +seed 50 ok=True steps=175 time=2.3s err=[ 0.002  0.014 -0.03 ]
          12 +seed 51 ok=True steps=125 time=2.3s err=[0.021 0.01  0.089]
          13 +seed 52 ok=True steps=174 time=1.9s err=[0.014 0.021 0.034]
          14 +seed 53 ok=True steps=149 time=3.0s err=[-0.017  0.    -0.036]
          15 +seed 54 ok=True steps=131 time=2.4s err=[0.015 0.023 0.071]
          16 +seed 55 ok=True steps=210 time=4.1s err=[-0.008 -0.006  0.086]
          17 +seed 56 ok=True steps=85 time=1.6s err=[ 0.006 -0.01   0.01 ]
          18 +seed 57 ok=True steps=165 time=3.3s err=[-0.019  0.009  0.094]
          19 +seed 58 ok=True steps=93 time=2.1s err=[-0.007 -0.009  0.032]
          20 +seed 59 ok=True steps=120 time=2.3s err=[-0.023 -0.01  -0.084]
          21 +seed 60 ok=True steps=224 time=3.8s err=[ 0.023  0.024 -0.077]
          22 +seed 61 ok=True steps=124 time=1.7s err=[-0.013  0.01   0.05 ]
          23 +seed 62 ok=True steps=64 time=1.4s err=[ 0.027 -0.009 -0.043]
          24 +seed 63 ok=True steps=153 time=2.7s err=[-0.007 -0.016 -0.089]
          25 +seed 64 ok=True steps=196 time=3.3s err=[ 0.019 -0.016  0.084]
          26 +seed 65 ok=True steps=168 time=2.9s err=[-0.011 -0.01   0.023]
          27 +seed 66 ok=True steps=113 time=2.1s err=[-0.001 -0.026  0.085]
          28 +seed 67 ok=True steps=155 time=3.1s err=[0.013 0.021 0.024]
          29 +seed 68 ok=True steps=78 time=1.8s err=[0.013 0.024 0.025]
          30 +seed 69 ok=True steps=76 time=1.9s err=[ 0.028  0.007 -0.056]
          31 +seed 70 ok=True steps=143 time=3.0s err=[ 0.001 -0.017 -0.045]
          32 +seed 71 ok=True steps=224 time=4.2s err=[-0.016 -0.017  0.09 ]
          33 +seed 72 ok=True steps=115 time=2.1s err=[-0.019  0.002  0.07 ]
          34 +seed 73 ok=True steps=113 time=1.6s err=[-0.022  0.002 -0.089]
          35 +seed 74 ok=True steps=92 time=1.4s err=[ 0.005  0.005 -0.087]
          36 +seed 75 ok=True steps=145 time=2.1s err=[ 0.012  0.013 -0.094]
          37 +seed 76 ok=True steps=98 time=1.3s err=[ 0.014 -0.022  0.088]
          38 +seed 77 ok=True steps=133 time=1.1s err=[-0.013 -0.016 -0.099]
          39 +seed 78 ok=True steps=140 time=1.4s err=[ 0.009 -0.007  0.042]
          40 +seed 79 ok=True steps=173 time=1.5s err=[-0.006  0.002 -0.092]
          41 +success 1.0 40 40
diff --git a/res_2.txt b/res_2.txt
new file mode 100644
index 0000000..3f71021
--- /dev/null
+++ b/res_2.txt
@@ -0,0 +1,41 @@
           1 +seed 80 ok=True steps=77 time=1.6s err=[0.006 0.004 0.032]
           2 +seed 81 ok=True steps=152 time=2.5s err=[ 0.018 -0.004  0.011]
           3 +seed 82 ok=True steps=200 time=4.3s err=[ 0.017 -0.009 -0.08 ]
           4 +seed 83 ok=True steps=102 time=1.6s err=[-0.007 -0.009 -0.086]
           5 +seed 84 ok=True steps=113 time=2.1s err=[-0.002  0.008  0.083]
           6 +seed 85 ok=True steps=183 time=3.6s err=[-0.018  0.007  0.041]
           7 +seed 86 ok=True steps=146 time=2.5s err=[-0.007  0.009 -0.087]
           8 +seed 87 ok=True steps=98 time=1.8s err=[-0.003  0.022  0.041]
           9 +seed 88 ok=True steps=175 time=3.9s err=[-0.018 -0.006 -0.092]
          10 +seed 89 ok=True steps=48 time=0.9s err=[-0.018  0.018  0.009]
          11 +seed 90 ok=True steps=122 time=1.3s err=[0.008 0.012 0.08 ]
          12 +seed 91 ok=True steps=120 time=1.4s err=[ 0.018 -0.022 -0.083]
          13 +seed 92 ok=True steps=160 time=3.2s err=[-0.01   0.    -0.078]
          14 +seed 93 ok=True steps=103 time=1.6s err=[0.016 0.009 0.055]
          15 +seed 94 ok=True steps=153 time=2.1s err=[0.019 0.025 0.044]
          16 +seed 95 ok=True steps=60 time=1.1s err=[ 0.01  -0.006  0.084]
          17 +seed 96 ok=True steps=145 time=2.9s err=[ 0.017 -0.011  0.084]
          18 +seed 97 ok=True steps=107 time=2.1s err=[-0.018 -0.008 -0.094]
          19 +seed 98 ok=True steps=96 time=2.0s err=[0.009 0.02  0.061]
          20 +seed 99 ok=True steps=168 time=2.7s err=[ 0.008  0.02  -0.028]
          21 +seed 100 ok=True steps=134 time=2.4s err=[ 0.008 -0.028  0.072]
          22 +seed 101 ok=True steps=118 time=2.0s err=[-0.     0.022  0.079]
          23 +seed 102 ok=True steps=91 time=1.8s err=[-0.018 -0.008 -0.073]
          24 +seed 103 ok=True steps=220 time=4.1s err=[-0.022 -0.017 -0.051]
          25 +seed 104 ok=True steps=61 time=1.1s err=[-0.031  0.019  0.091]
          26 +seed 105 ok=True steps=138 time=2.7s err=[-0.016 -0.004  0.087]
          27 +seed 106 ok=True steps=121 time=1.8s err=[ 0.006  0.013 -0.098]
          28 +seed 107 ok=True steps=96 time=1.7s err=[ 0.006  0.019 -0.097]
          29 +seed 108 ok=True steps=113 time=1.6s err=[ 0.002 -0.004  0.055]
          30 +seed 109 ok=True steps=126 time=2.5s err=[ 0.001  0.002 -0.05 ]
          31 +seed 110 ok=True steps=111 time=2.4s err=[-0.013 -0.    -0.081]
          32 +seed 111 ok=True steps=210 time=3.3s err=[0.039 0.024 0.057]
          33 +seed 112 ok=True steps=131 time=2.3s err=[ 0.029 -0.006 -0.099]
          34 +seed 113 ok=True steps=101 time=2.1s err=[ 0.023 -0.003  0.083]
          35 +seed 114 ok=True steps=190 time=4.0s err=[ 0.015  0.013 -0.019]
          36 +seed 115 ok=True steps=139 time=2.7s err=[-0.     0.009 -0.078]
          37 +seed 116 ok=True steps=181 time=2.9s err=[ 0.012 -0.001 -0.04 ]
          38 +seed 117 ok=True steps=68 time=1.0s err=[-0.021  0.017  0.087]
          39 +seed 118 ok=True steps=155 time=2.2s err=[-0.015 -0.006  0.059]
          40 +seed 119 ok=True steps=177 time=2.5s err=[ 0.007  0.01  -0.105]
          41 +success 1.0 40 40
diff --git a/res_3.txt b/res_3.txt
new file mode 100644
index 0000000..eda9c5f
--- /dev/null
+++ b/res_3.txt
@@ -0,0 +1,41 @@
           1 +seed 120 ok=True steps=97 time=1.9s err=[-0.024  0.011 -0.052]
           2 +seed 121 ok=True steps=98 time=1.6s err=[0.018 0.01  0.086]
           3 +seed 122 ok=True steps=150 time=2.6s err=[-0.017 -0.018 -0.028]
           4 +seed 123 ok=True steps=178 time=3.3s err=[-0.009  0.012 -0.08 ]
           5 +seed 124 ok=True steps=166 time=2.4s err=[0.008 0.007 0.081]
           6 +seed 125 ok=True steps=77 time=1.5s err=[-0.018  0.011  0.07 ]
           7 +seed 126 ok=True steps=159 time=2.4s err=[-0.007  0.005 -0.099]
           8 +seed 127 ok=True steps=254 time=4.5s err=[ 0.018  0.009 -0.09 ]
           9 +seed 128 ok=True steps=144 time=2.3s err=[-0.014 -0.014  0.066]
          10 +seed 129 ok=True steps=68 time=1.6s err=[ 0.011  0.023 -0.058]
          11 +seed 130 ok=True steps=197 time=3.6s err=[-0.022  0.025 -0.009]
          12 +seed 131 ok=True steps=156 time=2.7s err=[0.003 0.006 0.027]
          13 +seed 132 ok=True steps=149 time=2.3s err=[-0.016 -0.003  0.005]
          14 +seed 133 ok=True steps=125 time=1.7s err=[-0.019  0.016 -0.051]
          15 +seed 134 ok=True steps=153 time=3.0s err=[ 0.019 -0.004  0.083]
          16 +seed 135 ok=True steps=109 time=2.2s err=[ 0.005 -0.021 -0.01 ]
          17 +seed 136 ok=True steps=142 time=3.1s err=[-0.032 -0.003  0.055]
          18 +seed 137 ok=True steps=72 time=1.4s err=[ 0.01   0.003 -0.067]
          19 +seed 138 ok=True steps=171 time=3.4s err=[ 0.006 -0.012  0.034]
          20 +seed 139 ok=True steps=102 time=1.9s err=[0.007 0.01  0.011]
          21 +seed 140 ok=True steps=101 time=2.0s err=[-0.004  0.015 -0.082]
          22 +seed 141 ok=True steps=92 time=2.0s err=[0.001 0.001 0.06 ]
          23 +seed 142 ok=True steps=141 time=2.4s err=[ 0.016  0.014 -0.087]
          24 +seed 143 ok=True steps=123 time=1.9s err=[-0.002  0.004  0.046]
          25 +seed 144 ok=True steps=142 time=2.8s err=[-0.011 -0.014 -0.076]
          26 +seed 145 ok=True steps=119 time=2.0s err=[0.01  0.002 0.047]
          27 +seed 146 ok=True steps=83 time=1.2s err=[-0.016  0.019 -0.001]
          28 +seed 147 ok=True steps=73 time=1.0s err=[ 0.006 -0.007  0.018]
          29 +seed 148 ok=True steps=51 time=1.0s err=[ 0.003 -0.008 -0.054]
          30 +seed 149 ok=True steps=87 time=1.5s err=[ 0.02   0.009 -0.02 ]
          31 +seed 150 ok=True steps=79 time=1.3s err=[0.002 0.005 0.001]
          32 +seed 151 ok=True steps=171 time=2.3s err=[-0.009  0.018 -0.045]
          33 +seed 152 ok=True steps=89 time=1.6s err=[0.023 0.014 0.082]
          34 +seed 153 ok=True steps=64 time=1.0s err=[-0.004 -0.021 -0.039]
          35 +seed 154 ok=True steps=124 time=1.9s err=[ 0.017 -0.011 -0.023]
          36 +seed 155 ok=True steps=134 time=2.7s err=[-0.011 -0.013  0.009]
          37 +seed 156 ok=True steps=79 time=2.1s err=[-0.024  0.014  0.076]
          38 +seed 157 ok=True steps=112 time=2.5s err=[ 0.013  0.02  -0.042]
          39 +seed 158 ok=True steps=91 time=2.1s err=[ 0.008 -0.002 -0.077]
          40 +seed 159 ok=True steps=155 time=2.0s err=[-0.026  0.004 -0.075]
          41 +success 1.0 40 40
diff --git a/res_4.txt b/res_4.txt
new file mode 100644
index 0000000..7ef8974
--- /dev/null
+++ b/res_4.txt
@@ -0,0 +1,41 @@
           1 +seed 160 ok=True steps=103 time=1.9s err=[0.008 0.007 0.088]
           2 +seed 161 ok=True steps=145 time=2.8s err=[-0.002  0.016 -0.082]
           3 +seed 162 ok=True steps=87 time=1.5s err=[ 0.026  0.019 -0.015]
           4 +seed 163 ok=True steps=157 time=3.3s err=[-0.007  0.026  0.089]
           5 +seed 164 ok=True steps=50 time=0.7s err=[-0.005  0.008 -0.015]
           6 +seed 165 ok=True steps=122 time=2.8s err=[0.006 0.    0.003]
           7 +seed 166 ok=True steps=148 time=2.3s err=[-0.008  0.006 -0.068]
           8 +seed 167 ok=True steps=64 time=1.0s err=[-0.021 -0.024 -0.073]
           9 +seed 168 ok=True steps=178 time=3.4s err=[-0.003 -0.004 -0.009]
          10 +seed 169 ok=True steps=148 time=2.7s err=[-0.022 -0.027  0.014]
          11 +seed 170 ok=True steps=111 time=2.3s err=[ 0.001 -0.01  -0.048]
          12 +seed 171 ok=True steps=99 time=1.8s err=[ 0.015 -0.004 -0.015]
          13 +seed 172 ok=True steps=148 time=1.9s err=[ 0.003 -0.005  0.076]
          14 +seed 173 ok=False steps=1000 time=22.2s err=[-0.043 -0.015 -1.469]
          15 +seed 174 ok=True steps=112 time=1.7s err=[-0.006 -0.008 -0.074]
          16 +seed 175 ok=True steps=82 time=1.9s err=[ 0.017  0.01  -0.007]
          17 +seed 176 ok=True steps=126 time=2.2s err=[-0.026 -0.026  0.034]
          18 +seed 177 ok=True steps=80 time=1.2s err=[-0.013 -0.    -0.053]
          19 +seed 178 ok=True steps=153 time=3.1s err=[ 0.033  0.019 -0.065]
          20 +seed 179 ok=True steps=230 time=3.6s err=[ 0.021 -0.015 -0.019]
          21 +seed 180 ok=True steps=119 time=2.0s err=[-0.004  0.     0.039]
          22 +seed 181 ok=True steps=177 time=2.7s err=[-0.005 -0.016 -0.037]
          23 +seed 182 ok=True steps=179 time=3.0s err=[ 0.009 -0.024  0.042]
          24 +seed 183 ok=True steps=164 time=2.8s err=[-0.008  0.022 -0.016]
          25 +seed 184 ok=True steps=112 time=2.1s err=[-0.008  0.009 -0.075]
          26 +seed 185 ok=True steps=82 time=1.7s err=[ 0.001  0.017 -0.017]
          27 +seed 186 ok=True steps=59 time=1.2s err=[-0.016  0.007  0.012]
          28 +seed 187 ok=True steps=114 time=2.4s err=[-0.011  0.016 -0.098]
          29 +seed 188 ok=True steps=139 time=2.7s err=[-0.029  0.002  0.082]
          30 +seed 189 ok=True steps=185 time=2.6s err=[0.015 0.018 0.007]
          31 +seed 190 ok=True steps=109 time=1.7s err=[0.021 0.022 0.087]
          32 +seed 191 ok=True steps=35 time=0.6s err=[-0.014 -0.025 -0.045]
          33 +seed 192 ok=True steps=162 time=1.8s err=[-0.004 -0.013  0.09 ]
          34 +seed 193 ok=True steps=185 time=2.1s err=[ 0.004  0.003 -0.074]
          35 +seed 194 ok=True steps=145 time=1.4s err=[ 0.021  0.015 -0.096]
          36 +seed 195 ok=True steps=102 time=1.0s err=[-0.011 -0.011  0.079]
          37 +seed 196 ok=True steps=95 time=0.7s err=[0.001 0.012 0.048]
          38 +seed 197 ok=True steps=114 time=0.5s err=[-0.015  0.025 -0.105]
          39 +seed 198 ok=True steps=135 time=0.6s err=[ 0.008  0.01  -0.024]
          40 +seed 199 ok=True steps=62 time=0.4s err=[-0.009 -0.01  -0.01 ]
          41 +success 0.975 39 40
```

</details>

<a id="C004"></a>
### C004 · K_ANG=0.8 (fixes rotation local minima, fewer steps)

Commit `ea6e8e1a3fec197e2119decbe19f20a16b311566`; parents: 076d2b66df7c445182abc5067bd3ceeb37c099de. Recorded author date: 2026-09-28T19:04:12+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0334](01_timeline.md#E0334): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_ea6e8e1_approach.py) · [Exact all-file diff](evidence/diffs/C004_ea6e8e1.diff)

[Previous saved controller snapshot](evidence/versions/C003_076d2b6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b32c32b..a562a4a 100644
--- a/approach.py
+++ b/approach.py
@@ -5,7 +5,7 @@ from tmodel import TGeom, sim_step, wrap, corners_world, R_ROBOT
    5      5  AMAX = 0.0499
    6      6  LO, HI = 0.1 + 1e-3, 4.9 - 1e-3
    7      7  POS_TOL, ANG_TOL = 0.03, np.deg2rad(8.0)
    8        -K_ANG = 0.3
           8 +K_ANG = 0.8
    9      9  
   10     10  
   11     11  def cost(bx, by, bt, goal):
diff --git a/sw_0.8_0_50.txt b/sw_0.8_0_50.txt
new file mode 100644
index 0000000..c9358ee
--- /dev/null
+++ b/sw_0.8_0_50.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 119.58
diff --git a/sw_0.8_50_100.txt b/sw_0.8_50_100.txt
new file mode 100644
index 0000000..cb87cfa
--- /dev/null
+++ b/sw_0.8_50_100.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 133.06
diff --git a/sw_1.2_0_50.txt b/sw_1.2_0_50.txt
new file mode 100644
index 0000000..3249ac6
--- /dev/null
+++ b/sw_1.2_0_50.txt
@@ -0,0 +1 @@
           1 +K 1.2 succ 1.0 meansteps 122.04
diff --git a/sw_1.2_50_100.txt b/sw_1.2_50_100.txt
new file mode 100644
index 0000000..661de90
--- /dev/null
+++ b/sw_1.2_50_100.txt
@@ -0,0 +1 @@
           1 +K 1.2 succ 1.0 meansteps 136.34
diff --git a/sw_1.6_0_50.txt b/sw_1.6_0_50.txt
new file mode 100644
index 0000000..4f4eb3f
--- /dev/null
+++ b/sw_1.6_0_50.txt
@@ -0,0 +1 @@
           1 +K 1.6 succ 1.0 meansteps 125.12
diff --git a/sw_1.6_50_100.txt b/sw_1.6_50_100.txt
new file mode 100644
index 0000000..d8f41cc
--- /dev/null
+++ b/sw_1.6_50_100.txt
@@ -0,0 +1 @@
           1 +K 1.6 succ 1.0 meansteps 140.0
diff --git a/sweep.py b/sweep.py
new file mode 100644
index 0000000..b485eb5
--- /dev/null
+++ b/sweep.py
@@ -0,0 +1,15 @@
           1 +import sys, time, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +K=float(sys.argv[1]); approach.K_ANG=K
           5 +seeds=[int(x) for x in sys.argv[2].split(',')] if ',' in sys.argv[2] else range(*map(int,sys.argv[2].split(':')))
           6 +env=make_env(); res=[]; steps=[]
           7 +for sd in seeds:
           8 +    obs,info=env.reset(seed=sd); ap=approach.GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           9 +    ok=False
          10 +    for t in range(1000):
          11 +        obs,r,term,trunc,info=env.step(ap.get_action(obs))
          12 +        if term: ok=True; break
          13 +    res.append(ok); steps.append(t+1)
          14 +    if not ok: print('fail',sd)
          15 +print('K',K,'succ',np.mean(res),'meansteps',np.mean(steps))
```

</details>

<a id="C005"></a>
### C005 · 2-step lookahead planner

Commit `b032fa735ad676b62b2f0711aab3d268a931b0d6`; parents: ea6e8e1a3fec197e2119decbe19f20a16b311566. Recorded author date: 2026-09-28T19:08:44+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0363](01_timeline.md#E0363): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_b032fa7_approach.py) · [Exact all-file diff](evidence/diffs/C005_b032fa7.diff)

[Previous saved controller snapshot](evidence/versions/C004_ea6e8e1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a562a4a..8664548 100644
--- a/approach.py
+++ b/approach.py
@@ -6,6 +6,7 @@ AMAX = 0.0499
    6      6  LO, HI = 0.1 + 1e-3, 4.9 - 1e-3
    7      7  POS_TOL, ANG_TOL = 0.03, np.deg2rad(8.0)
    8      8  K_ANG = 0.8
           9 +LOOKAHEAD = 8
    9     10  
   10     11  
   11     12  def cost(bx, by, bt, goal):
@@ -22,6 +23,7 @@ class GeneratedApproach:
   22     23          self.action_space = action_space
   23     24          self.queue = []
   24     25          self.g = None
          26 +        self.lookahead = LOOKAHEAD
   25     27  
   26     28      def reset(self, state, info):
   27     29          self.queue = []
@@ -29,6 +31,13 @@ class GeneratedApproach:
   29     31          self.goal = np.array(state[29:32], dtype=float)
   30     32          self.expect = None
   31     33          self.mode = None
          34 +        import time as _t
          35 +        self.t_start = _t.time()
          36 +        self.pts = self.g.boundary_points(0.05)
          37 +        lpx = self.pts[:, 0] + self.pts[:, 2] * (R_ROBOT + 0.045)
          38 +        lpy = self.pts[:, 1] + self.pts[:, 3] * (R_ROBOT + 0.045)
          39 +        self.pre_ok = self.g.closest(lpx, lpy)[4] > R_ROBOT + 0.03
          40 +        self.angs = np.deg2rad(np.array([-40, -25, -12, 0, 12, 25, 40]))
   32     41  
   33     42      # ---------------- navigation -----------------
   34     43      def _seg_free(self, pose, ax, ay, bx_, by_, m):
@@ -130,18 +139,15 @@ class GeneratedApproach:
  130    139          return tdist, path
  131    140  
  132    141      # ---------------- planning -----------------
  133        -    def _plan(self, obs):
         142 +    def _eval(self, pose, robot, fine):
         143 +        """Evaluate all single push segments from (pose, robot). Returns dict or None."""
  134    144          g = self.g
  135        -        pose = np.array(obs[0:3], float)
  136        -        robot = np.array(obs[16:18], float)
  137    145          goal = self.goal
  138        -        J0 = cost(pose[0], pose[1], pose[2], goal)
  139        -        fine = J0 < 0.12
         146 +        J0 = float(cost(pose[0], pose[1], pose[2], goal))
  140    147          step = AMAX if not fine else AMAX / 3
  141    148          nsteps = 40 if not fine else 30
  142        -        pts = g.boundary_points(0.05)
         149 +        pts = self.pts
  143    150          c, s = np.cos(pose[2]), np.sin(pose[2])
  144        -        # contact center (robot center touching) and pre-point in world
  145    151          lcx = pts[:, 0] + pts[:, 2] * (R_ROBOT + 0.003)
  146    152          lcy = pts[:, 1] + pts[:, 3] * (R_ROBOT + 0.003)
  147    153          wcx = pose[0] + c * lcx - s * lcy
@@ -151,14 +157,11 @@ class GeneratedApproach:
  151    157          wpx = pose[0] + c * lpx - s * lpy
  152    158          wpy = pose[1] + s * lpx + c * lpy
  153    159          inb = (wcx > LO) & (wcx < HI) & (wcy > LO) & (wcy < HI) & (wpx > LO) & (wpx < HI) & (wpy > LO) & (wpy < HI)
  154        -        # pre-point must be free
  155        -        _, _, _, _, dpre = g.closest(lpx, lpy)
  156        -        inb &= dpre > R_ROBOT + 0.03
         160 +        inb &= self.pre_ok
  157    161          idx = np.nonzero(inb)[0]
  158    162          if len(idx) == 0:
  159    163              return None
  160    164          pre = np.stack([wpx[idx], wpy[idx]], 1)
  161        -        # retreat if robot is close to the block
  162    165          rlx = c * (robot[0] - pose[0]) + s * (robot[1] - pose[1])
  163    166          rly = -s * (robot[0] - pose[0]) + c * (robot[1] - pose[1])
  164    167          _, _, rnx, rny, rd = g.closest(np.array([rlx]), np.array([rly]))
@@ -170,13 +173,12 @@ class GeneratedApproach:
  170    173                  retreat = cand
  171    174          start = robot if retreat is None else retreat
  172    175          tdist, pathf = self._plan_paths(pose, start, pre)
         176 +        tdist = tdist + 0.045
  173    177          if retreat is not None:
  174    178              tdist = tdist + np.hypot(*(retreat - robot))
  175        -        tdist = tdist + 0.045
  176        -        # world inward normal
  177    179          nwx = -(c * pts[idx, 2] - s * pts[idx, 3])
  178    180          nwy = -(s * pts[idx, 2] + c * pts[idx, 3])
  179        -        angs = np.deg2rad(np.array([-40, -25, -12, 0, 12, 25, 40]))
         181 +        angs = self.angs
  180    182          K = len(idx) * len(angs)
  181    183          ci = np.repeat(np.arange(len(idx)), len(angs))
  182    184          aa = np.tile(angs, len(idx))
@@ -186,14 +188,14 @@ class GeneratedApproach:
  186    188          bx = np.full(K, pose[0]); by = np.full(K, pose[1]); bt = np.full(K, pose[2])
  187    189          rx = wcx[idx][ci].copy(); ry = wcy[idx][ci].copy()
  188    190          valid = np.isfinite(tdist[ci])
  189        -        travel = tdist[ci] / AMAX + 1.0
  190        -        # current wall margin
         191 +        travel = np.ceil(tdist[ci] / AMAX) + 1.0
  191    192          cx0, cy0 = corners_world(g, pose[0], pose[1], pose[2])
  192    193          m0 = min(cx0.min(), cy0.min(), 5 - cx0.max(), 5 - cy0.max())
  193    194          wall_lim = min(0.06, m0 - 0.01)
  194    195          best_score = np.full(K, -np.inf)
  195    196          best_n = np.zeros(K, int)
  196    197          best_J = np.full(K, np.inf)
         198 +        fin = np.zeros((K, 5))
  197    199          alive = valid.copy()
  198    200          for k in range(1, nsteps + 1):
  199    201              bx, by, bt, rx, ry = sim_step(g, bx, by, bt, rx, ry, ux, uy)
@@ -201,40 +203,85 @@ class GeneratedApproach:
  201    203              cxw, cyw = corners_world(g, bx, by, bt)
  202    204              mm = np.minimum(np.minimum(cxw.min(0), cyw.min(0)), np.minimum(5 - cxw.max(0), 5 - cyw.max(0)))
  203    205              alive &= mm > wall_lim
         206 +            if not alive.any():
         207 +                break
  204    208              J = cost(bx, by, bt, goal)
  205    209              J = np.where(solved(bx, by, bt, goal), J - 0.5, J)
  206        -            steps_k = k if not fine else k / 3.0
         210 +            steps_k = k if not fine else np.ceil(k / 3.0)
  207    211              sc = (J0 - J) / (travel + steps_k + 1.0)
  208    212              upd = alive & (sc > best_score)
  209    213              best_score = np.where(upd, sc, best_score)
  210    214              best_n = np.where(upd, k, best_n)
  211    215              best_J = np.where(upd, J, best_J)
  212        -        j = int(np.argmax(best_score))
  213        -        if not np.isfinite(best_score[j]) or best_score[j] <= 0:
         216 +            if upd.any():
         217 +                fin[upd] = np.stack([bx, by, bt, rx, ry], 1)[upd]
         218 +        steps_n = best_n if not fine else np.ceil(best_n / 3.0)
         219 +        return dict(J0=J0, score=best_score, n=best_n, J=best_J, fin=fin, ci=ci, idx=idx,
         220 +                    ux=ux, uy=uy, travel=travel, tot=travel + steps_n + 1.0, pathf=pathf,
         221 +                    retreat=retreat, wc=np.stack([wcx, wcy], 1), fine=fine)
         222 +
         223 +    def _plan(self, obs):
         224 +        pose = np.array(obs[0:3], float)
         225 +        robot = np.array(obs[16:18], float)
         226 +        J0 = float(cost(pose[0], pose[1], pose[2], self.goal))
         227 +        fine = J0 < 0.12
         228 +        E = self._eval(pose, robot, fine)
         229 +        if E is None:
  214    230              return None
  215        -        n = int(best_n[j])
  216        -        wp = pathf(ci[j])
  217        -        if retreat is not None:
  218        -            wp = [retreat] + wp
         231 +        sc = E['score']
         232 +        order = np.argsort(-sc)
         233 +        j = int(order[0])
         234 +        if not np.isfinite(sc[j]) or sc[j] <= 0:
         235 +            return None
         236 +        import time as _t
         237 +        if self.lookahead > 0 and not fine and _t.time() - self.t_start < 25.0:
         238 +            best_val, best_j = -np.inf, j
         239 +            seen = set()
         240 +            cnt = 0
         241 +            for jj in order:
         242 +                if cnt >= self.lookahead or not np.isfinite(sc[jj]) or sc[jj] <= 0:
         243 +                    break
         244 +                key = (E['ci'][jj] // 2, int(E['n'][jj] // 8))
         245 +                if key in seen:
         246 +                    continue
         247 +                seen.add(key)
         248 +                cnt += 1
         249 +                f = E['fin'][jj]
         250 +                t1 = E['tot'][jj]
         251 +                J1 = E['J'][jj]
         252 +                val = (E['J0'] - J1) / t1
         253 +                if J1 > -0.2:  # not solved
         254 +                    fine2 = J1 + 0.0 < 0.12
         255 +                    E2 = self._eval(f[0:3], f[3:5], fine2)
         256 +                    if E2 is not None:
         257 +                        s2 = (E['J0'] - E2['J']) / (t1 + E2['tot'])
         258 +                        s2 = np.where(E2['score'] > -np.inf, s2, -np.inf)
         259 +                        val = max(val, float(np.max(s2)))
         260 +                if val > best_val:
         261 +                    best_val, best_j = val, int(jj)
         262 +            j = best_j
         263 +        return self._build(E, j, robot)
         264 +
         265 +    def _build(self, E, j, robot):
         266 +        ci = E['ci']; idx = E['idx']
         267 +        n = int(E['n'][j])
         268 +        wp = E['pathf'](ci[j])
         269 +        if E['retreat'] is not None:
         270 +            wp = [E['retreat']] + wp
  219    271          acts = []
  220    272          cur = robot.copy()
  221        -        for w in wp + [np.array([wcx[idx][ci[j]], wcy[idx][ci[j]]])]:
         273 +        for w in wp + [E['wc'][idx][ci[j]]]:
  222    274              w = np.asarray(w, float)
  223        -            while True:
  224        -                d = w - cur
  225        -                L = np.hypot(*d)
  226        -                if L < 1e-9:
  227        -                    break
  228        -                nst = int(np.ceil(L / AMAX - 1e-9))
  229        -                a = d / nst
  230        -                for _ in range(nst):
  231        -                    acts.append(('nav', a.copy()))
  232        -                cur = w.copy()
  233        -                break
  234        -        # push
  235        -        a = np.array([ux[j], uy[j]])
  236        -        if fine:
  237        -            # combine into fewer steps
         275 +            d = w - cur
         276 +            L = np.hypot(*d)
         277 +            if L < 1e-9:
         278 +                continue
         279 +            nst = int(np.ceil(L / AMAX - 1e-9))
         280 +            for _ in range(nst):
         281 +                acts.append(('nav', d / nst))
         282 +            cur = w.copy()
         283 +        a = np.array([E['ux'][j], E['uy'][j]])
         284 +        if E['fine']:
  238    285              tot = a * n
  239    286              L = np.hypot(*tot)
  240    287              nst = max(1, int(np.ceil(L / AMAX - 1e-9)))
@@ -243,7 +290,7 @@ class GeneratedApproach:
  243    290          else:
  244    291              for _ in range(n):
  245    292                  acts.append(('push', a.copy()))
  246        -        self.dbg = (best_score[j], best_J[j], n, travel[j], J0)
         293 +        self.dbg = (E['score'][j], E['J'][j], n, E['travel'][j], E['J0'])
  247    294          return acts
  248    295  
  249    296      def get_action(self, state):
diff --git a/big_200_250.txt b/big_200_250.txt
new file mode 100644
index 0000000..a6ad36e
--- /dev/null
+++ b/big_200_250.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 129.52
diff --git a/big_250_300.txt b/big_250_300.txt
new file mode 100644
index 0000000..106a1db
--- /dev/null
+++ b/big_250_300.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 122.12
diff --git a/big_300_350.txt b/big_300_350.txt
new file mode 100644
index 0000000..0476caa
--- /dev/null
+++ b/big_300_350.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 128.42
diff --git a/big_350_400.txt b/big_350_400.txt
new file mode 100644
index 0000000..d5e520b
--- /dev/null
+++ b/big_350_400.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 127.04
diff --git a/big_400_450.txt b/big_400_450.txt
new file mode 100644
index 0000000..ea4235e
--- /dev/null
+++ b/big_400_450.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 128.32
diff --git a/big_450_500.txt b/big_450_500.txt
new file mode 100644
index 0000000..af35d9c
--- /dev/null
+++ b/big_450_500.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 121.3
diff --git a/big_500_550.txt b/big_500_550.txt
new file mode 100644
index 0000000..670cd7f
--- /dev/null
+++ b/big_500_550.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 125.32
diff --git a/big_550_600.txt b/big_550_600.txt
new file mode 100644
index 0000000..cd49c6f
--- /dev/null
+++ b/big_550_600.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 127.42
diff --git a/sweep.py b/sweep.py
index b485eb5..81cde69 100644
--- a/sweep.py
+++ b/sweep.py
@@ -1,7 +1,7 @@
    1      1  import sys, time, numpy as np
    2      2  from env_client import make_env
    3      3  import approach
    4        -K=float(sys.argv[1]); approach.K_ANG=K
           4 +K=float(sys.argv[1]); approach.K_ANG=K; approach.LOOKAHEAD=int(sys.argv[3]) if len(sys.argv)>3 else 8
    5      5  seeds=[int(x) for x in sys.argv[2].split(',')] if ',' in sys.argv[2] else range(*map(int,sys.argv[2].split(':')))
    6      6  env=make_env(); res=[]; steps=[]
    7      7  for sd in seeds:
```

</details>

<a id="C006"></a>
### C006 · block-frame push family

Commit `c6944f5164653d9d2b124b34eec874e29f72ad04`; parents: b032fa735ad676b62b2f0711aab3d268a931b0d6. Recorded author date: 2026-09-28T19:11:18+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0389](01_timeline.md#E0389): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_c6944f5_approach.py) · [Exact all-file diff](evidence/diffs/C006_c6944f5.diff)

[Previous saved controller snapshot](evidence/versions/C005_b032fa7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8664548..eca7767 100644
--- a/approach.py
+++ b/approach.py
@@ -7,6 +7,7 @@ LO, HI = 0.1 + 1e-3, 4.9 - 1e-3
    7      7  POS_TOL, ANG_TOL = 0.03, np.deg2rad(8.0)
    8      8  K_ANG = 0.8
    9      9  LOOKAHEAD = 8
          10 +LOCAL_FAMILY = True
   10     11  
   11     12  
   12     13  def cost(bx, by, bt, goal):
@@ -24,6 +25,7 @@ class GeneratedApproach:
   24     25          self.queue = []
   25     26          self.g = None
   26     27          self.lookahead = LOOKAHEAD
          28 +        self.local_family = LOCAL_FAMILY
   27     29  
   28     30      def reset(self, state, info):
   29     31          self.queue = []
@@ -179,12 +181,19 @@ class GeneratedApproach:
  179    181          nwx = -(c * pts[idx, 2] - s * pts[idx, 3])
  180    182          nwy = -(s * pts[idx, 2] + c * pts[idx, 3])
  181    183          angs = self.angs
  182        -        K = len(idx) * len(angs)
  183        -        ci = np.repeat(np.arange(len(idx)), len(angs))
  184        -        aa = np.tile(angs, len(idx))
         184 +        nf = 2 if self.local_family else 1
         185 +        na = len(angs)
         186 +        K = len(idx) * na * nf
         187 +        ci = np.tile(np.repeat(np.arange(len(idx)), na), nf)
         188 +        aa = np.tile(angs, len(idx) * nf)
         189 +        fam = np.repeat(np.arange(nf), len(idx) * na)
  185    190          dirx = np.cos(aa) * nwx[ci] - np.sin(aa) * nwy[ci]
  186    191          diry = np.sin(aa) * nwx[ci] + np.cos(aa) * nwy[ci]
  187    192          ux, uy = dirx * step, diry * step
         193 +        # local-frame direction (for family 1)
         194 +        lux0 = c * ux + s * uy
         195 +        luy0 = -s * ux + c * uy
         196 +        isloc = fam == 1
  188    197          bx = np.full(K, pose[0]); by = np.full(K, pose[1]); bt = np.full(K, pose[2])
  189    198          rx = wcx[idx][ci].copy(); ry = wcy[idx][ci].copy()
  190    199          valid = np.isfinite(tdist[ci])
@@ -198,7 +207,13 @@ class GeneratedApproach:
  198    207          fin = np.zeros((K, 5))
  199    208          alive = valid.copy()
  200    209          for k in range(1, nsteps + 1):
  201        -            bx, by, bt, rx, ry = sim_step(g, bx, by, bt, rx, ry, ux, uy)
         210 +            if nf > 1:
         211 +                cb, sb = np.cos(bt), np.sin(bt)
         212 +                uxk = np.where(isloc, cb * lux0 - sb * luy0, ux)
         213 +                uyk = np.where(isloc, sb * lux0 + cb * luy0, uy)
         214 +            else:
         215 +                uxk, uyk = ux, uy
         216 +            bx, by, bt, rx, ry = sim_step(g, bx, by, bt, rx, ry, uxk, uyk)
  202    217              alive &= (rx > LO) & (rx < HI) & (ry > LO) & (ry < HI)
  203    218              cxw, cyw = corners_world(g, bx, by, bt)
  204    219              mm = np.minimum(np.minimum(cxw.min(0), cyw.min(0)), np.minimum(5 - cxw.max(0), 5 - cyw.max(0)))
@@ -217,7 +232,7 @@ class GeneratedApproach:
  217    232                  fin[upd] = np.stack([bx, by, bt, rx, ry], 1)[upd]
  218    233          steps_n = best_n if not fine else np.ceil(best_n / 3.0)
  219    234          return dict(J0=J0, score=best_score, n=best_n, J=best_J, fin=fin, ci=ci, idx=idx,
  220        -                    ux=ux, uy=uy, travel=travel, tot=travel + steps_n + 1.0, pathf=pathf,
         235 +                    ux=ux, uy=uy, lux=lux0, luy=luy0, fam=fam, travel=travel, tot=travel + steps_n + 1.0, pathf=pathf,
  221    236                      retreat=retreat, wc=np.stack([wcx, wcy], 1), fine=fine)
  222    237  
  223    238      def _plan(self, obs):
@@ -254,9 +269,11 @@ class GeneratedApproach:
  254    269                      fine2 = J1 + 0.0 < 0.12
  255    270                      E2 = self._eval(f[0:3], f[3:5], fine2)
  256    271                      if E2 is not None:
  257        -                        s2 = (E['J0'] - E2['J']) / (t1 + E2['tot'])
  258        -                        s2 = np.where(E2['score'] > -np.inf, s2, -np.inf)
  259        -                        val = max(val, float(np.max(s2)))
         272 +                        with np.errstate(invalid='ignore'):
         273 +                            s2 = (E['J0'] - E2['J']) / (t1 + E2['tot'])
         274 +                        ok2 = (E2['score'] > -np.inf) & np.isfinite(E2['tot'])
         275 +                        if ok2.any():
         276 +                            val = max(val, float(np.max(s2[ok2])))
  260    277                  if val > best_val:
  261    278                      best_val, best_j = val, int(jj)
  262    279              j = best_j
@@ -281,7 +298,14 @@ class GeneratedApproach:
  281    298                  acts.append(('nav', d / nst))
  282    299              cur = w.copy()
  283    300          a = np.array([E['ux'][j], E['uy'][j]])
  284        -        if E['fine']:
         301 +        if E['fam'][j] == 1:
         302 +            la = np.array([E['lux'][j], E['luy'][j]])
         303 +            if E['fine']:
         304 +                la = la * 3
         305 +                n = int(np.ceil(n / 3.0))
         306 +            for _ in range(n):
         307 +                acts.append(('pushL', la.copy()))
         308 +        elif E['fine']:
  285    309              tot = a * n
  286    310              L = np.hypot(*tot)
  287    311              nst = max(1, int(np.ceil(L / AMAX - 1e-9)))
@@ -310,5 +334,9 @@ class GeneratedApproach:
  310    334              d = pose[0:2] - obs[16:18]
  311    335              return np.clip(d, -AMAX, AMAX)
  312    336          kind, a = self.queue.pop(0)
         337 +        if kind == 'pushL':
         338 +            cb, sb = np.cos(pose[2]), np.sin(pose[2])
         339 +            a = np.array([cb * a[0] - sb * a[1], sb * a[0] + cb * a[1]])
         340 +        self.last_kind = kind
  313    341          self.expect = pose.copy()
  314    342          return np.clip(a, -AMAX, AMAX)
diff --git a/la_0_0_25.txt b/la_0_0_25.txt
new file mode 100644
index 0000000..ab5c260
--- /dev/null
+++ b/la_0_0_25.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 117.72
diff --git a/la_0_25_50.txt b/la_0_25_50.txt
new file mode 100644
index 0000000..219d6cc
--- /dev/null
+++ b/la_0_25_50.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 125.04
diff --git a/la_0_50_75.txt b/la_0_50_75.txt
new file mode 100644
index 0000000..063e34f
--- /dev/null
+++ b/la_0_50_75.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 138.88
diff --git a/la_0_75_100.txt b/la_0_75_100.txt
new file mode 100644
index 0000000..b95ac24
--- /dev/null
+++ b/la_0_75_100.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 131.12
diff --git a/la_8_0_25.txt b/la_8_0_25.txt
new file mode 100644
index 0000000..217129f
--- /dev/null
+++ b/la_8_0_25.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 105.4
diff --git a/la_8_25_50.txt b/la_8_25_50.txt
new file mode 100644
index 0000000..101b4dd
--- /dev/null
+++ b/la_8_25_50.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 111.72
diff --git a/la_8_50_75.txt b/la_8_50_75.txt
new file mode 100644
index 0000000..732fcc5
--- /dev/null
+++ b/la_8_50_75.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 128.84
diff --git a/la_8_75_100.txt b/la_8_75_100.txt
new file mode 100644
index 0000000..93a7c5c
--- /dev/null
+++ b/la_8_75_100.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 121.28
diff --git a/sweep.py b/sweep.py
index 81cde69..c9db88c 100644
--- a/sweep.py
+++ b/sweep.py
@@ -1,7 +1,7 @@
    1      1  import sys, time, numpy as np
    2      2  from env_client import make_env
    3      3  import approach
    4        -K=float(sys.argv[1]); approach.K_ANG=K; approach.LOOKAHEAD=int(sys.argv[3]) if len(sys.argv)>3 else 8
           4 +K=float(sys.argv[1]); approach.K_ANG=K; approach.LOOKAHEAD=int(sys.argv[3]) if len(sys.argv)>3 else 8; approach.LOCAL_FAMILY=(sys.argv[4]=="1") if len(sys.argv)>4 else True
    5      5  seeds=[int(x) for x in sys.argv[2].split(',')] if ',' in sys.argv[2] else range(*map(int,sys.argv[2].split(':')))
    6      6  env=make_env(); res=[]; steps=[]
    7      7  for sd in seeds:
```

</details>

<a id="C007"></a>
### C007 · lookahead 16

Commit `341c0e1db6b2cf4f32c26b5b4de2c9117fce7b36`; parents: c6944f5164653d9d2b124b34eec874e29f72ad04. Recorded author date: 2026-09-28T19:14:12+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0408](01_timeline.md#E0408): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_341c0e1_approach.py) · [Exact all-file diff](evidence/diffs/C007_341c0e1.diff)

[Previous saved controller snapshot](evidence/versions/C006_c6944f5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index eca7767..d12cec7 100644
--- a/approach.py
+++ b/approach.py
@@ -6,7 +6,7 @@ AMAX = 0.0499
    6      6  LO, HI = 0.1 + 1e-3, 4.9 - 1e-3
    7      7  POS_TOL, ANG_TOL = 0.03, np.deg2rad(8.0)
    8      8  K_ANG = 0.8
    9        -LOOKAHEAD = 8
           9 +LOOKAHEAD = 16
   10     10  LOCAL_FAMILY = True
   11     11  
   12     12  
diff --git a/la16_0_25.txt b/la16_0_25.txt
new file mode 100644
index 0000000..d4372b7
--- /dev/null
+++ b/la16_0_25.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 107.04 tmax 4.7
diff --git a/la16_25_50.txt b/la16_25_50.txt
new file mode 100644
index 0000000..e608101
--- /dev/null
+++ b/la16_25_50.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 106.92 tmax 4.3
diff --git a/la16_50_75.txt b/la16_50_75.txt
new file mode 100644
index 0000000..7022b1e
--- /dev/null
+++ b/la16_50_75.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 116.52 tmax 5.3
diff --git a/la16_75_100.txt b/la16_75_100.txt
new file mode 100644
index 0000000..633e5a7
--- /dev/null
+++ b/la16_75_100.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 114.24 tmax 5.3
diff --git a/lf_0_0_25.txt b/lf_0_0_25.txt
new file mode 100644
index 0000000..217129f
--- /dev/null
+++ b/lf_0_0_25.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 105.4
diff --git a/lf_0_25_50.txt b/lf_0_25_50.txt
new file mode 100644
index 0000000..101b4dd
--- /dev/null
+++ b/lf_0_25_50.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 111.72
diff --git a/lf_0_50_75.txt b/lf_0_50_75.txt
new file mode 100644
index 0000000..732fcc5
--- /dev/null
+++ b/lf_0_50_75.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 128.84
diff --git a/lf_0_75_100.txt b/lf_0_75_100.txt
new file mode 100644
index 0000000..93a7c5c
--- /dev/null
+++ b/lf_0_75_100.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 121.28
diff --git a/lf_1_0_25.txt b/lf_1_0_25.txt
new file mode 100644
index 0000000..201367a
--- /dev/null
+++ b/lf_1_0_25.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 105.52
diff --git a/lf_1_25_50.txt b/lf_1_25_50.txt
new file mode 100644
index 0000000..941a2ad
--- /dev/null
+++ b/lf_1_25_50.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 110.12
diff --git a/lf_1_50_75.txt b/lf_1_50_75.txt
new file mode 100644
index 0000000..106a1db
--- /dev/null
+++ b/lf_1_50_75.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 122.12
diff --git a/lf_1_75_100.txt b/lf_1_75_100.txt
new file mode 100644
index 0000000..90d40d9
--- /dev/null
+++ b/lf_1_75_100.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 115.0
diff --git a/sweep.py b/sweep.py
index c9db88c..fb05330 100644
--- a/sweep.py
+++ b/sweep.py
@@ -3,13 +3,14 @@ from env_client import make_env
    3      3  import approach
    4      4  K=float(sys.argv[1]); approach.K_ANG=K; approach.LOOKAHEAD=int(sys.argv[3]) if len(sys.argv)>3 else 8; approach.LOCAL_FAMILY=(sys.argv[4]=="1") if len(sys.argv)>4 else True
    5      5  seeds=[int(x) for x in sys.argv[2].split(',')] if ',' in sys.argv[2] else range(*map(int,sys.argv[2].split(':')))
    6        -env=make_env(); res=[]; steps=[]
           6 +import time
           7 +env=make_env(); res=[]; steps=[]; tmax=0
    7      8  for sd in seeds:
    8      9      obs,info=env.reset(seed=sd); ap=approach.GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
    9        -    ok=False
          10 +    ok=False; t0=time.time()
   10     11      for t in range(1000):
   11     12          obs,r,term,trunc,info=env.step(ap.get_action(obs))
   12     13          if term: ok=True; break
   13        -    res.append(ok); steps.append(t+1)
          14 +    res.append(ok); steps.append(t+1); tmax=max(tmax,time.time()-t0)
   14     15      if not ok: print('fail',sd)
   15        -print('K',K,'succ',np.mean(res),'meansteps',np.mean(steps))
          16 +print('K',K,'succ',np.mean(res),'meansteps',np.mean(steps),'tmax',round(tmax,1))
```

</details>

<a id="C008"></a>
### C008 · exception-safe get_action, cleanup

Commit `96fd518c4e5419032fa809e389603a27cb160873`; parents: 341c0e1db6b2cf4f32c26b5b4de2c9117fce7b36. Recorded author date: 2026-09-28T19:17:32+02:00.

File roles (automatic): policy, setup/other.

- [E0420](01_timeline.md#E0420): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_96fd518_approach.py) · [Exact all-file diff](evidence/diffs/C008_96fd518.diff)

[Previous saved controller snapshot](evidence/versions/C007_341c0e1_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d12cec7..9633c75 100644
--- a/approach.py
+++ b/approach.py
@@ -318,6 +318,17 @@ class GeneratedApproach:
  318    318          return acts
  319    319  
  320    320      def get_action(self, state):
         321 +        try:
         322 +            a = self._get_action(state)
         323 +            a = np.clip(np.asarray(a, dtype=np.float64).reshape(2), -AMAX, AMAX)
         324 +            if not np.all(np.isfinite(a)):
         325 +                a = np.zeros(2)
         326 +            return a
         327 +        except Exception:
         328 +            self.queue = []
         329 +            return np.zeros(2)
         330 +
         331 +    def _get_action(self, state):
  321    332          obs = np.asarray(state, float)
  322    333          pose = obs[0:3]
  323    334          replan = not self.queue
diff --git a/v_600_650.txt b/v_600_650.txt
new file mode 100644
index 0000000..4f1369a
--- /dev/null
+++ b/v_600_650.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 108.08 tmax 5.0
diff --git a/v_650_700.txt b/v_650_700.txt
new file mode 100644
index 0000000..64eba85
--- /dev/null
+++ b/v_650_700.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 116.5 tmax 5.9
diff --git a/v_700_750.txt b/v_700_750.txt
new file mode 100644
index 0000000..74d2458
--- /dev/null
+++ b/v_700_750.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 105.4 tmax 6.2
diff --git a/v_750_800.txt b/v_750_800.txt
new file mode 100644
index 0000000..78ca64a
--- /dev/null
+++ b/v_750_800.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 104.86 tmax 6.5
diff --git a/v_800_850.txt b/v_800_850.txt
new file mode 100644
index 0000000..388d972
--- /dev/null
+++ b/v_800_850.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 112.04 tmax 8.3
diff --git a/v_850_900.txt b/v_850_900.txt
new file mode 100644
index 0000000..530580f
--- /dev/null
+++ b/v_850_900.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 103.76 tmax 6.5
diff --git a/v_900_950.txt b/v_900_950.txt
new file mode 100644
index 0000000..6201a42
--- /dev/null
+++ b/v_900_950.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 112.66 tmax 5.8
diff --git a/v_950_1000.txt b/v_950_1000.txt
new file mode 100644
index 0000000..46f5a20
--- /dev/null
+++ b/v_950_1000.txt
@@ -0,0 +1 @@
           1 +K 0.8 succ 1.0 meansteps 96.1 tmax 5.6
```

</details>

