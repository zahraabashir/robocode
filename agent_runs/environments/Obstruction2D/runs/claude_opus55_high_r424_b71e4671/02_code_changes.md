# Obstruction2D · claude-opus-5-5 · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `e21245a` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `281b2bb` | initial state-machine approach | approach.py, dump.py, probe0.py, probe1.py, probe2.py, test_approach.py | [E0033](01_timeline.md#E0033) |
| [C003](#C003) · `a81561e` | reach-aware grasp offsets and drop positions | approach.py, dbg.py, probe3.py | [E0082](01_timeline.md#E0082) |
| [C004](#C004) · `f47aa67` | planner with Chebyshev controller, minimal obstruction removal | approach.py, approach_v1.py, probe4.py, test_approach.py | [E0215](01_timeline.md#E0215) |
| [C005](#C005) · `1599f2a` | check pick-pose feasibility | approach.py, dbg.py, test_approach.py | [E0241](01_timeline.md#E0241) |
| [C006](#C006) · `46e7fc6` | consistent drop feasibility, circular base approx | approach.py, dbg2.py, dbgplan.py | [E0288](01_timeline.md#E0288) |
| [C007](#C007) · `6cc7485` | check drop pose feasibility | approach.py | [E0302](01_timeline.md#E0302) |
| [C008](#C008) · `b19eb46` | stuck recovery via replanning; robust test harness | approach.py, res_100_300.txt, test_approach.py, timing.py | [E0391](01_timeline.md#E0391) |
| [C009](#C009) · `41e922c` | avoid grasp poses where vacuum could grab neighbours | approach.py, dbg3.py, legeff.py, res_300_600.txt | [E0443](01_timeline.md#E0443) |
| [C010](#C010) · `878bb40` | multi-candidate plans chosen by offline controller simulation | approach.py, res_600_1000.txt | [E0491](01_timeline.md#E0491) |
| [C011](#C011) · `e704574` | wider candidate search (k_drop=3,k_place=3,n_sim=20) | approach.py | [E0494](01_timeline.md#E0494) |
| [C012](#C012) · `c115fb9` | vectorize clearance computation | approach.py, prof.out, prof.py, res_0_300_v3.txt | [E0557](01_timeline.md#E0557) |
| [C013](#C013) · `6be1f90` | Controller uses arm joint as extra vertical DOF; vacuum clearance margin while carrying | approach.py, dbg4.py, res_0_300_v3.txt | [E0608](01_timeline.md#E0608) |
| [C014](#C014) · `5131e04` | wider plan search (n_sim 60, k 5) | approach.py, cmpcfg.py, res_0_300_v4.txt, res_300_1000_v4.txt | [E0680](01_timeline.md#E0680) |
| [C015](#C015) · `39d1e55` | time guard in planner | approach.py, res_0_300_v5.txt, resettime.py, test_approach.py | [E0701](01_timeline.md#E0701) |
| [C016](#C016) · `7ab5ce6` | soft deadline limits drop branching | approach.py | [E0708](01_timeline.md#E0708) |
| [C017](#C017) · `394a6f0` | test results for v5, tester prints slowest seeds | res_300_1000_v5.txt | [E0772](01_timeline.md#E0772) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `e21245a82a0e66cd5e463e9456f82fb44354b551`; parents: none (initial snapshot). Recorded author date: 2026-09-30T11:03:14+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_e21245a.diff)

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
index 0000000..67b6737
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "d97b0e02fe0ff36d8f221a063dbf5c8f", "observation_space": {"type": "ObjectCentric", "types": [{"name": "crv_robot", "parent": null, "features": ["x", "y", "theta", "base_radius", "arm_joint", "arm_length", "vacuum", "gripper_height", "gripper_width"]}, {"name": "kinematic2d", "parent": null, "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order"]}, {"name": "circle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "radius"]}, {"name": "double_rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height", "x1", "y1", "theta1", "width1", "height1", "z_order1", "color_r1", "color_g1", "color_b1"]}, {"name": "lobject", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "length_side1", "length_side2"]}, {"name": "rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_block", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_surface", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}]}, "action_space": {"type": "Box", "shape": [5], "low": [-0.05000000074505806, -0.05000000074505806, -0.19634954631328583, -0.10000000149011612, 0.0], "high": [0.05000000074505806, 0.05000000074505806, 0.19634954631328583, 0.10000000149011612, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · initial state-machine approach

Commit `281b2bbaf0828fe1409529f0aa9275a53f8ad2fb`; parents: e21245a82a0e66cd5e463e9456f82fb44354b551. Recorded author date: 2026-09-30T11:05:08+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0033](01_timeline.md#E0033): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_281b2bb_approach.py) · [Exact all-file diff](evidence/diffs/C002_281b2bb.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..dfda7f1
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,241 @@
           1 +import numpy as np
           2 +
           3 +WORLD_MIN_X = 0.0
           4 +WORLD_MAX_X = 1.618
           5 +FLOOR_Y = 0.1
           6 +
           7 +
           8 +class GeneratedApproach:
           9 +    def __init__(self, action_space, observation_space, primitives):
          10 +        self.low = np.array(action_space.low, dtype=np.float32)
          11 +        self.high = np.array(action_space.high, dtype=np.float32)
          12 +        self.max_dx = float(self.high[0])
          13 +        self.max_dth = float(self.high[2])
          14 +        self.max_darm = float(self.high[3])
          15 +
          16 +    # ------------------------------------------------------------------ utils
          17 +    def _g(self, s, o, f):
          18 +        return float(s.get(o, f))
          19 +
          20 +    def _rect(self, s, o):
          21 +        x, y = self._g(s, o, "x"), self._g(s, o, "y")
          22 +        w, h = self._g(s, o, "width"), self._g(s, o, "height")
          23 +        th = self._g(s, o, "theta")
          24 +        c, sn = np.cos(th), np.sin(th)
          25 +        pts = np.array([[0, 0], [w, 0], [w, h], [0, h]])
          26 +        R = np.array([[c, -sn], [sn, c]])
          27 +        v = pts @ R.T + np.array([x, y])
          28 +        return v[:, 0].min(), v[:, 0].max(), v[:, 1].min(), v[:, 1].max()
          29 +
          30 +    def _parse(self, s):
          31 +        robot = s.get_objects(self.t_robot)[0] if self.t_robot else None
          32 +        return robot
          33 +
          34 +    def _objs(self, s):
          35 +        d = {}
          36 +        for name in s.get_object_names():
          37 +            o = s.get_object_from_name(name)
          38 +            d[str(name) if isinstance(name, str) else o.name] = o
          39 +        return d
          40 +
          41 +    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0, vac=0.0):
          42 +        a = np.array([dx, dy, dth, darm, vac], dtype=np.float32)
          43 +        return np.clip(a, self.low, self.high)
          44 +
          45 +    # ------------------------------------------------------------------ api
          46 +    def reset(self, state, info):
          47 +        self.phase = "choose"
          48 +        self.target = None  # name of object being manipulated
          49 +        self.drop_x = None
          50 +        self.last_robot = None
          51 +        self.last_cmd = None
          52 +        self.blocked_count = 0
          53 +        self.grasp_offset = None
          54 +        self.steps = 0
          55 +
          56 +    def get_action(self, state):
          57 +        self.steps += 1
          58 +        objs = self._objs(state)
          59 +        robot = None
          60 +        for n, o in objs.items():
          61 +            if o.type.name == "crv_robot":
          62 +                robot = o
          63 +        rx, ry = self._g(state, robot, "x"), self._g(state, robot, "y")
          64 +        rth = self._g(state, robot, "theta")
          65 +        arm = self._g(state, robot, "arm_joint")
          66 +        arm_max = self._g(state, robot, "arm_length")
          67 +        gw = self._g(state, robot, "gripper_width")
          68 +        base_r = self._g(state, robot, "base_radius")
          69 +        vac = self._g(state, robot, "vacuum")
          70 +
          71 +        # detect blocked motion
          72 +        moved = True
          73 +        if self.last_robot is not None and self.last_cmd is not None:
          74 +            lx, ly = self.last_robot
          75 +            cdx, cdy = self.last_cmd
          76 +            if (abs(cdx) > 1e-5 or abs(cdy) > 1e-5) and abs(lx - rx) < 1e-7 and abs(ly - ry) < 1e-7:
          77 +                moved = False
          78 +        self.last_robot = (rx, ry)
          79 +
          80 +        block = surface = None
          81 +        obstructions = []
          82 +        for n, o in objs.items():
          83 +            tn = o.type.name
          84 +            if tn == "target_block":
          85 +                block = o
          86 +            elif tn == "target_surface":
          87 +                surface = o
          88 +            elif tn == "rectangle":
          89 +                obstructions.append(o)
          90 +        sx0, sx1, sy0, sy1 = self._rect(state, surface)
          91 +
          92 +        rects = {}
          93 +        for o in obstructions + [block]:
          94 +            rects[o.name] = self._rect(state, o)
          95 +
          96 +        # gripper face y (pointing down)
          97 +        face = ry - arm - gw
          98 +
          99 +        # travel height: carried object bottom clears all tops
         100 +        max_top = max(r[3] for r in rects.values())
         101 +        carry_h = 0.0
         102 +        if self.target is not None and vac > 0.5 and self.phase in ("lift", "carry", "lower"):
         103 +            tr = rects[self.target]
         104 +            carry_h = tr[3] - tr[2]
         105 +        travel_y = max_top + 0.05 + carry_h + arm_max + gw
         106 +        travel_y = min(max(travel_y, 0.6), 1.0 - base_r - 0.01)
         107 +
         108 +        dx = dy = dth = darm = 0.0
         109 +        vcmd = 1.0 if vac > 0.5 else 0.0
         110 +
         111 +        # keep orientation down and arm extended
         112 +        th_err = (-np.pi / 2 - rth + np.pi) % (2 * np.pi) - np.pi
         113 +        dth = np.clip(th_err, -self.max_dth, self.max_dth)
         114 +        darm = np.clip(arm_max - arm, -self.max_darm, self.max_darm)
         115 +
         116 +        if self.phase == "choose":
         117 +            # obstructions overlapping surface
         118 +            bw = rects[block.name][1] - rects[block.name][0]
         119 +            tgt = None
         120 +            best = None
         121 +            for o in obstructions:
         122 +                x0, x1, y0, y1 = rects[o.name]
         123 +                if x1 > sx0 - 0.005 and x0 < sx1 + 0.005 and y0 < sy1 + 0.3:
         124 +                    d = abs((x0 + x1) / 2 - (sx0 + sx1) / 2)
         125 +                    if best is None or d < best:
         126 +                        best, tgt = d, o.name
         127 +            if tgt is None:
         128 +                tgt = block.name
         129 +            self.target = tgt
         130 +            self.phase = "rise"
         131 +            self.last_cmd = (0, 0)
         132 +            return self._act(0, 0, dth, darm, 0.0)
         133 +
         134 +        tr = rects[self.target]
         135 +        tcx = (tr[0] + tr[1]) / 2
         136 +
         137 +        if self.phase == "rise":
         138 +            # go up to travel height without vacuum
         139 +            if ry < travel_y - 1e-3:
         140 +                dy = min(travel_y - ry, self.max_dx)
         141 +            else:
         142 +                self.phase = "over"
         143 +        if self.phase == "over":
         144 +            ex = tcx - rx
         145 +            if abs(ex) > 1e-4:
         146 +                dx = ex
         147 +            else:
         148 +                self.phase = "descend"
         149 +                self.blocked_count = 0
         150 +        if self.phase == "descend":
         151 +            contact_y = tr[3] + arm + gw
         152 +            if not moved:
         153 +                self.phase = "grasp"
         154 +            else:
         155 +                rem = ry - contact_y
         156 +                if rem > 0.006:
         157 +                    dy = -min(rem - 0.004, self.max_dx)
         158 +                else:
         159 +                    dy = -0.002
         160 +                if rem < -0.02:
         161 +                    self.phase = "grasp"
         162 +                    dy = 0.0
         163 +        if self.phase == "grasp":
         164 +            vcmd = 1.0
         165 +            dy = 0.0
         166 +            self.grasp_ref = (tr[0] - rx, tr[2] - ry)
         167 +            self.phase = "lift"
         168 +            self.last_cmd = (0, 0)
         169 +            return self._act(0, 0, dth, 0.0, vcmd)
         170 +        if self.phase == "lift":
         171 +            vcmd = 1.0
         172 +            if ry < travel_y - 1e-3:
         173 +                dy = min(travel_y - ry, self.max_dx)
         174 +            else:
         175 +                self.phase = "carry"
         176 +                self._plan_drop(state, rects, block, (sx0, sx1), rx)
         177 +        if self.phase == "carry":
         178 +            vcmd = 1.0
         179 +            ex = self.drop_x - rx
         180 +            if abs(ex) > 1e-4:
         181 +                dx = ex
         182 +            else:
         183 +                self.phase = "lower"
         184 +        if self.phase == "lower":
         185 +            vcmd = 1.0
         186 +            is_block = self.target == block.name
         187 +            floor_top = sy1 if is_block else FLOOR_Y
         188 +            rem = tr[2] - floor_top
         189 +            if not moved:
         190 +                self.phase = "release"
         191 +            else:
         192 +                if rem > 0.006:
         193 +                    dy = -min(rem - 0.003, self.max_dx)
         194 +                else:
         195 +                    dy = -0.002
         196 +        if self.phase == "release":
         197 +            vcmd = 0.0
         198 +            dy = 0.0
         199 +            self.phase = "post"
         200 +            self.last_cmd = (0, 0)
         201 +            return self._act(0, 0, dth, 0.0, vcmd)
         202 +        if self.phase == "post":
         203 +            vcmd = 0.0
         204 +            self.phase = "choose"
         205 +            dy = 0.02
         206 +
         207 +        dx = float(np.clip(dx, -self.max_dx, self.max_dx))
         208 +        dy = float(np.clip(dy, -self.max_dx, self.max_dx))
         209 +        # keep within world
         210 +        self.last_cmd = (dx, dy)
         211 +        return self._act(dx, dy, dth, darm, vcmd)
         212 +
         213 +    def _plan_drop(self, state, rects, block, surf, rx):
         214 +        tr = rects[self.target]
         215 +        w = tr[1] - tr[0]
         216 +        off = tr[0] - rx  # left edge relative to robot x
         217 +        if self.target == block.name:
         218 +            sx0, sx1 = surf
         219 +            want_left = (sx0 + sx1) / 2 - w / 2
         220 +            self.drop_x = want_left - off
         221 +            return
         222 +        # choose free floor location maximizing clearance
         223 +        sx0, sx1 = surf
         224 +        bw = rects[block.name][1] - rects[block.name][0]
         225 +        forb = [(sx0 - 0.02, sx1 + 0.02)]
         226 +        for n, r in rects.items():
         227 +            if n == self.target:
         228 +                continue
         229 +            forb.append((r[0], r[1]))
         230 +        best = None
         231 +        for left in np.arange(0.12, WORLD_MAX_X - 0.12 - w, 0.01):
         232 +            a, b = left, left + w
         233 +            clr = min(min(abs(a - f1) if a >= f1 else (abs(f0 - b) if b <= f0 else -1.0)
         234 +                          for f0, f1 in forb), 0.3)
         235 +            if clr < 0:
         236 +                continue
         237 +            score = clr - 0.02 * abs(left + w / 2 - rx)
         238 +            if best is None or score > best[0]:
         239 +                best = (score, left)
         240 +        left = best[1] if best else 0.15
         241 +        self.drop_x = left - off
diff --git a/dump.py b/dump.py
new file mode 100644
index 0000000..a76950e
--- /dev/null
+++ b/dump.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import sys
           3 +FE = {'crv_robot':["x","y","theta","base_radius","arm_joint","arm_length","vacuum","gripper_height","gripper_width"],
           4 + 'rectangle':["x","y","theta","static","color_r","color_g","color_b","z_order","width","height"]}
           5 +FE['target_block']=FE['rectangle']; FE['target_surface']=FE['rectangle']
           6 +def dump(obs):
           7 +    for name in sorted(obs.get_object_names(), key=str):
           8 +        o = obs.get_object_from_name(name)
           9 +        print(name, {f: round(float(obs.get(o,f)),3) for f in FE[o.type.name]})
          10 +if __name__=="__main__":
          11 +    env = make_env()
          12 +    for seed in map(int, sys.argv[1:]):
          13 +        obs, info = env.reset(seed=seed); print("seed",seed,info); dump(obs)
          14 +    env.close()
diff --git a/probe0.py b/probe0.py
new file mode 100644
index 0000000..0b7796c
--- /dev/null
+++ b/probe0.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +env = make_env()
           3 +for seed in [0,1,2]:
           4 +    obs, info = env.reset(seed=seed)
           5 +    print("seed", seed, info)
           6 +    for name in sorted(obs.get_object_names(), key=str):
           7 +        o = obs.get_object_from_name(name) if isinstance(name,str) else name
           8 +        t = o.type if hasattr(o,'type') else None
           9 +        print(name, t, {f: round(obs.get(o,f),3) for f in env.observation_space.get_type(t.name if hasattr(t,'name') else t).__dict__.get('feature_names', [])} if False else '')
          10 +    print(obs)
          11 +env.close()
diff --git a/probe1.py b/probe1.py
new file mode 100644
index 0000000..6e07bfb
--- /dev/null
+++ b/probe1.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +r = obs.get_object_from_name('robot')
           6 +def R(o): return {f: round(float(o_.get(r,f)),4) for f in ["x","y","theta","arm_joint","vacuum"] for o_ in [o]}
           7 +print(R(obs))
           8 +for a in [[0.05,0,0,0,0],[0,-0.05,0,0,0],[0,0,0,0.1,0],[0,0,0,0.1,0],[0,0,0,0.1,0],[0,0,0.19,0,0],[-0.07,0,0,0,0],[0,0,0,0,1],[0,0,-0.19,0,0]]:
           9 +    obs,rew,te,tr,_=env.step(np.array(a,dtype=np.float32)); print(a, R(obs), rew, te)
          10 +# move down until blocked
          11 +for i in range(30):
          12 +    obs,rew,te,tr,_=env.step(np.array([0,-0.05,0,0,0],dtype=np.float32))
          13 +print("after down", R(obs))
          14 +env.close()
diff --git a/probe2.py b/probe2.py
new file mode 100644
index 0000000..7332909
--- /dev/null
+++ b/probe2.py
@@ -0,0 +1,26 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +r = obs.get_object_from_name('robot'); b=obs.get_object_from_name('target_block')
           6 +def g(o,f,s=None): return float((s or obs).get(o,f))
           7 +def step(a):
           8 +    global obs
           9 +    a=np.clip(np.array(a,dtype=np.float32),env.action_space.low,env.action_space.high)
          10 +    obs,rew,te,tr,_=env.step(a); return te
          11 +# go to x=0.489
          12 +while abs(g(r,'x')-0.489)>1e-4:
          13 +    step([np.clip(0.489-g(r,'x'),-.05,.05),0,0,0,0])
          14 +step([0,0,0,0.1,0])
          15 +prev=None
          16 +for i in range(200):
          17 +    step([0,-0.01,0,0,0])
          18 +    y=g(r,'y')
          19 +    if prev is not None and abs(prev-y)<1e-6: break
          20 +    prev=y
          21 +print("stopped robot y", g(r,'y'), "arm", g(r,'arm_joint'), "block top", g(b,'y')+g(b,'height'))
          22 +# vacuum on, lift
          23 +step([0,0,0,0,1]); 
          24 +for i in range(5): step([0,0.05,0,0,1])
          25 +print("block after lift", g(b,'x'), g(b,'y'), "robot", g(r,'x'),g(r,'y'),g(r,'vacuum'))
          26 +env.close()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..cc38318
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,26 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +def run(seed, verbose=False):
           6 +    env = make_env()
           7 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           8 +    obs, info = env.reset(seed=seed)
           9 +    ap.reset(obs, info)
          10 +    t=time.time()
          11 +    for t_ in range(env.max_steps):
          12 +        a = ap.get_action(obs)
          13 +        obs, r, te, tr, _ = env.step(a)
          14 +        if te or tr: break
          15 +    env.close()
          16 +    return te, t_+1, info.get('object_count'), ap.phase
          17 +if __name__ == "__main__":
          18 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          19 +    from concurrent.futures import ThreadPoolExecutor
          20 +    with ThreadPoolExecutor(8) as ex:
          21 +        res = list(ex.map(run, seeds))
          22 +    ok = 0
          23 +    for s, (te, n, c, ph) in zip(seeds, res):
          24 +        ok += te
          25 +        if not te: print("FAIL seed", s, "n_obj", c, "phase", ph)
          26 +    print(f"solved {ok}/{len(res)}  mean steps {np.mean([r[1] for r in res if r[0]]) if ok else 0:.1f}")
```

</details>

<a id="C003"></a>
### C003 · reach-aware grasp offsets and drop positions

Commit `a81561e31ca29f98c34066c8b929a8f7847659ca`; parents: 281b2bbaf0828fe1409529f0aa9275a53f8ad2fb. Recorded author date: 2026-09-30T11:10:22+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0082](01_timeline.md#E0082): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_a81561e_approach.py) · [Exact all-file diff](evidence/diffs/C003_a81561e.diff)

[Previous saved controller snapshot](evidence/versions/C002_281b2bb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index dfda7f1..3808e73 100644
--- a/approach.py
+++ b/approach.py
@@ -103,7 +103,7 @@ class GeneratedApproach:
  103    103              tr = rects[self.target]
  104    104              carry_h = tr[3] - tr[2]
  105    105          travel_y = max_top + 0.05 + carry_h + arm_max + gw
  106        -        travel_y = min(max(travel_y, 0.6), 1.0 - base_r - 0.01)
         106 +        travel_y = min(max(travel_y, 0.6), 0.89)
  107    107  
  108    108          dx = dy = dth = darm = 0.0
  109    109          vcmd = 1.0 if vac > 0.5 else 0.0
@@ -132,7 +132,7 @@ class GeneratedApproach:
  132    132              return self._act(0, 0, dth, darm, 0.0)
  133    133  
  134    134          tr = rects[self.target]
  135        -        tcx = (tr[0] + tr[1]) / 2
         135 +        tcx = self._grasp_x(tr, rects[block.name], (sx0, sx1), self.target == block.name)
  136    136  
  137    137          if self.phase == "rise":
  138    138              # go up to travel height without vacuum
@@ -210,6 +210,28 @@ class GeneratedApproach:
  210    210          self.last_cmd = (dx, dy)
  211    211          return self._act(dx, dy, dth, darm, vcmd)
  212    212  
         213 +    XMIN, XMAX = 0.102, 1.516
         214 +
         215 +    def _grasp_x(self, tr, br, surf, is_block):
         216 +        """Robot x at which to grasp object with x-range tr."""
         217 +        cx = (tr[0] + tr[1]) / 2
         218 +        hw = (tr[1] - tr[0]) / 2
         219 +        dmax = max(hw + 0.035 - 0.012, 0.0)  # gripper overlap allowance
         220 +        lo, hi = -dmax, dmax
         221 +        # pick reachability
         222 +        lo = max(lo, self.XMIN - cx)
         223 +        hi = min(hi, self.XMAX - cx)
         224 +        if is_block:
         225 +            scx = (surf[0] + surf[1]) / 2
         226 +            lo2 = max(lo, self.XMIN - scx)
         227 +            hi2 = min(hi, self.XMAX - scx)
         228 +            if lo2 <= hi2:
         229 +                lo, hi = lo2, hi2
         230 +        if lo > hi:
         231 +            return float(np.clip(cx, self.XMIN, self.XMAX))
         232 +        d = float(np.clip(0.0, lo, hi))
         233 +        return cx + d
         234 +
  213    235      def _plan_drop(self, state, rects, block, surf, rx):
  214    236          tr = rects[self.target]
  215    237          w = tr[1] - tr[0]
@@ -217,7 +239,7 @@ class GeneratedApproach:
  217    239          if self.target == block.name:
  218    240              sx0, sx1 = surf
  219    241              want_left = (sx0 + sx1) / 2 - w / 2
  220        -            self.drop_x = want_left - off
         242 +            self.drop_x = float(np.clip(want_left - off, self.XMIN, self.XMAX))
  221    243              return
  222    244          # choose free floor location maximizing clearance
  223    245          sx0, sx1 = surf
@@ -228,8 +250,10 @@ class GeneratedApproach:
  228    250                  continue
  229    251              forb.append((r[0], r[1]))
  230    252          best = None
  231        -        for left in np.arange(0.12, WORLD_MAX_X - 0.12 - w, 0.01):
         253 +        for left in np.arange(0.005, WORLD_MAX_X - 0.005 - w, 0.005):
  232    254              a, b = left, left + w
         255 +            if not (self.XMIN <= left - off <= self.XMAX):
         256 +                continue
  233    257              clr = min(min(abs(a - f1) if a >= f1 else (abs(f0 - b) if b <= f0 else -1.0)
  234    258                            for f0, f1 in forb), 0.3)
  235    259              if clr < 0:
@@ -238,4 +262,4 @@ class GeneratedApproach:
  238    262              if best is None or score > best[0]:
  239    263                  best = (score, left)
  240    264          left = best[1] if best else 0.15
  241        -        self.drop_x = left - off
         265 +        self.drop_x = float(np.clip(left - off, self.XMIN, self.XMAX))
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..06ef7d7
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,17 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed=int(sys.argv[1]); every=int(sys.argv[2]) if len(sys.argv)>2 else 10
           6 +env = make_env()
           7 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           8 +obs, info = env.reset(seed=seed); ap.reset(obs, info)
           9 +r = obs.get_object_from_name('robot')
          10 +for t in range(env.max_steps):
          11 +    a = ap.get_action(obs)
          12 +    ph=ap.phase
          13 +    obs, rew, te, tr, _ = env.step(a)
          14 +    if t%every==0 or te:
          15 +        print(t, ph, ap.target, np.round(a,3), [round(float(obs.get(r,f)),3) for f in ['x','y','theta','arm_joint','vacuum']])
          16 +    if te: print("DONE", t+1); break
          17 +env.close()
diff --git a/probe3.py b/probe3.py
new file mode 100644
index 0000000..39676a3
--- /dev/null
+++ b/probe3.py
@@ -0,0 +1,20 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=21)
           5 +r = obs.get_object_from_name('robot')
           6 +for d in [0.001,-0.001]:
           7 +    prev=None
           8 +    for i in range(2000):
           9 +        obs,*_=env.step(np.array([d*50 if i<1 else d,0,0,0,0],dtype=np.float32)) if False else env.step(np.array([d,0,0,0,0],dtype=np.float32))
          10 +        x=float(obs.get(r,'x'))
          11 +        if prev is not None and x==prev: break
          12 +        prev=x
          13 +    print("limit",d,x)
          14 +prev=None
          15 +for i in range(2000):
          16 +    obs,*_=env.step(np.array([0,0.002,0,0,0],dtype=np.float32)); y=float(obs.get(r,'y'))
          17 +    if prev is not None and y==prev: break
          18 +    prev=y
          19 +print("ymax",y)
          20 +env.close()
```

</details>

<a id="C004"></a>
### C004 · planner with Chebyshev controller, minimal obstruction removal

Commit `f47aa672e8c0272618651a4d939ddf722b8e820e`; parents: a81561e31ca29f98c34066c8b929a8f7847659ca. Recorded author date: 2026-09-30T11:36:30+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0215](01_timeline.md#E0215): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_f47aa67_approach.py) · [Exact all-file diff](evidence/diffs/C004_f47aa67.diff)

[Previous saved controller snapshot](evidence/versions/C003_a81561e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3808e73..77a18be 100644
--- a/approach.py
+++ b/approach.py
@@ -1,265 +1,331 @@
           1 +"""Obstruction2D approach: plan pick/drop/place legs, execute each leg with a
           2 +greedy Chebyshev (simultaneous dx/dy) controller that keeps the robot
           3 +assembly above all obstacles via a look-ahead clearance cone."""
           4 +import itertools
    1      5  import numpy as np
    2      6  
    3        -WORLD_MIN_X = 0.0
    4      7  WORLD_MAX_X = 1.618
    5      8  FLOOR_Y = 0.1
           9 +XMIN, XMAX = 0.1015, 1.5170
          10 +YMAX = 0.897
          11 +MX = 0.006      # horizontal clearance margin
          12 +MY = 0.004      # vertical clearance margin
          13 +GAP = 0.006     # gripper gap to object top when grasping (grasp works <= ~0.01)
          14 +DROP_BOT = FLOOR_Y + 0.006
          15 +PLACE_BOT = FLOOR_Y + 0.012
          16 +STEP = 0.05
          17 +
          18 +
          19 +def _g(s, o, f):
          20 +    return float(s.get(o, f))
          21 +
          22 +
          23 +def _rect(s, o):
          24 +    x, y = _g(s, o, "x"), _g(s, o, "y")
          25 +    w, h = _g(s, o, "width"), _g(s, o, "height")
          26 +    th = _g(s, o, "theta")
          27 +    c, sn = np.cos(th), np.sin(th)
          28 +    pts = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=float)
          29 +    R = np.array([[c, -sn], [sn, c]])
          30 +    v = pts @ R.T + np.array([x, y])
          31 +    return (float(v[:, 0].min()), float(v[:, 0].max()),
          32 +            float(v[:, 1].min()), float(v[:, 1].max()))
    6     33  
    7     34  
    8     35  class GeneratedApproach:
    9     36      def __init__(self, action_space, observation_space, primitives):
   10     37          self.low = np.array(action_space.low, dtype=np.float32)
   11     38          self.high = np.array(action_space.high, dtype=np.float32)
   12        -        self.max_dx = float(self.high[0])
          39 +        self.max_d = float(self.high[0])
   13     40          self.max_dth = float(self.high[2])
   14     41          self.max_darm = float(self.high[3])
   15     42  
   16        -    # ------------------------------------------------------------------ utils
   17        -    def _g(self, s, o, f):
   18        -        return float(s.get(o, f))
   19        -
   20        -    def _rect(self, s, o):
   21        -        x, y = self._g(s, o, "x"), self._g(s, o, "y")
   22        -        w, h = self._g(s, o, "width"), self._g(s, o, "height")
   23        -        th = self._g(s, o, "theta")
   24        -        c, sn = np.cos(th), np.sin(th)
   25        -        pts = np.array([[0, 0], [w, 0], [w, h], [0, h]])
   26        -        R = np.array([[c, -sn], [sn, c]])
   27        -        v = pts @ R.T + np.array([x, y])
   28        -        return v[:, 0].min(), v[:, 0].max(), v[:, 1].min(), v[:, 1].max()
   29        -
          43 +    # ------------------------------------------------------------ parsing
   30     44      def _parse(self, s):
   31        -        robot = s.get_objects(self.t_robot)[0] if self.t_robot else None
   32        -        return robot
   33        -
   34        -    def _objs(self, s):
   35        -        d = {}
          45 +        robot = block = surface = None
          46 +        obst = []
   36     47          for name in s.get_object_names():
   37     48              o = s.get_object_from_name(name)
   38        -            d[str(name) if isinstance(name, str) else o.name] = o
   39        -        return d
          49 +            tn = o.type.name
          50 +            if tn == "crv_robot":
          51 +                robot = o
          52 +            elif tn == "target_block":
          53 +                block = o
          54 +            elif tn == "target_surface":
          55 +                surface = o
          56 +            else:
          57 +                try:
          58 +                    _g(s, o, "width")
          59 +                    _g(s, o, "height")
          60 +                    obst.append(o)
          61 +                except Exception:
          62 +                    pass
          63 +        return robot, block, surface, obst
   40     64  
   41        -    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0, vac=0.0):
   42        -        a = np.array([dx, dy, dth, darm, vac], dtype=np.float32)
   43        -        return np.clip(a, self.low, self.high)
          65 +    # ------------------------------------------------------------ geometry
          66 +    def _assembly(self, held_rel=None):
          67 +        """Boxes (x0, x1, bottom_offset) relative to robot position."""
          68 +        gh = self.gh / 2.0
          69 +        boxes = [(-self.base_r, self.base_r, -self.base_r),
          70 +                 (-gh, gh, -(self.arm + self.gw))]
          71 +        if held_rel is not None:
          72 +            boxes.append(held_rel)
          73 +        return boxes
   44     74  
   45        -    # ------------------------------------------------------------------ api
          75 +    @staticmethod
          76 +    def _safe(X, boxes, obstacles):
          77 +        """Minimal robot y at each x in X such that boxes clear obstacles."""
          78 +        req = np.full(X.shape, -1.0)
          79 +        for bx0, bx1, boff in boxes:
          80 +            req = np.maximum(req, FLOOR_Y + MY - boff)
          81 +            for ox0, ox1, otop in obstacles:
          82 +                ov = (X + bx1 > ox0 - MX) & (X + bx0 < ox1 + MX)
          83 +                req = np.where(ov, np.maximum(req, otop + MY - boff), req)
          84 +        return req
          85 +
          86 +    def _leg_cost(self, p0, p1, boxes, obstacles):
          87 +        x0, y0 = p0
          88 +        x1, y1 = p1
          89 +        n = max(2, int(abs(x1 - x0) / 0.01) + 2)
          90 +        X = np.linspace(x0, x1, n)
          91 +        peak = float(self._safe(X, boxes, obstacles).max())
          92 +        peak = max(peak, y0, y1)
          93 +        vert = (peak - y0) + (peak - y1)
          94 +        return max(abs(x1 - x0), vert) / STEP
          95 +
          96 +    # ------------------------------------------------------------ planning
   46     97      def reset(self, state, info):
   47        -        self.phase = "choose"
   48        -        self.target = None  # name of object being manipulated
   49        -        self.drop_x = None
   50        -        self.last_robot = None
   51        -        self.last_cmd = None
   52        -        self.blocked_count = 0
   53        -        self.grasp_offset = None
          98 +        robot, block, surface, obst = self._parse(state)
          99 +        self.base_r = _g(state, robot, "base_radius")
         100 +        self.arm = _g(state, robot, "arm_length")
         101 +        self.gw = _g(state, robot, "gripper_width")
         102 +        self.gh = _g(state, robot, "gripper_height")
         103 +        self.block_name = block.name
   54    104          self.steps = 0
         105 +        self.leg = 0
         106 +        self.last = None
         107 +        self.stuck = 0
         108 +        try:
         109 +            self.legs = self._plan(state)
         110 +        except Exception:
         111 +            self.legs = None
         112 +        if not self.legs:
         113 +            self.legs = self._fallback_plan(state)
   55    114  
   56        -    def get_action(self, state):
   57        -        self.steps += 1
   58        -        objs = self._objs(state)
   59        -        robot = None
   60        -        for n, o in objs.items():
   61        -            if o.type.name == "crv_robot":
   62        -                robot = o
   63        -        rx, ry = self._g(state, robot, "x"), self._g(state, robot, "y")
   64        -        rth = self._g(state, robot, "theta")
   65        -        arm = self._g(state, robot, "arm_joint")
   66        -        arm_max = self._g(state, robot, "arm_length")
   67        -        gw = self._g(state, robot, "gripper_width")
   68        -        base_r = self._g(state, robot, "base_radius")
   69        -        vac = self._g(state, robot, "vacuum")
         115 +    def _grasp_d(self, r):
         116 +        """Allowed range of grasp offsets d (gripper x - object center)."""
         117 +        cx = (r[0] + r[1]) / 2
         118 +        hw = (r[1] - r[0]) / 2
         119 +        dmax = max(hw + self.gh / 2 - 0.012, 0.0)
         120 +        return max(-dmax, XMIN - cx), min(dmax, XMAX - cx)
   70    121  
   71        -        # detect blocked motion
   72        -        moved = True
   73        -        if self.last_robot is not None and self.last_cmd is not None:
   74        -            lx, ly = self.last_robot
   75        -            cdx, cdy = self.last_cmd
   76        -            if (abs(cdx) > 1e-5 or abs(cdy) > 1e-5) and abs(lx - rx) < 1e-7 and abs(ly - ry) < 1e-7:
   77        -                moved = False
   78        -        self.last_robot = (rx, ry)
         122 +    def _pick_pose(self, r, d):
         123 +        cx = (r[0] + r[1]) / 2
         124 +        return (cx + d, r[3] + GAP + self.arm + self.gw)
   79    125  
   80        -        block = surface = None
   81        -        obstructions = []
   82        -        for n, o in objs.items():
   83        -            tn = o.type.name
   84        -            if tn == "target_block":
   85        -                block = o
   86        -            elif tn == "target_surface":
   87        -                surface = o
   88        -            elif tn == "rectangle":
   89        -                obstructions.append(o)
   90        -        sx0, sx1, sy0, sy1 = self._rect(state, surface)
         126 +    def _held_rel(self, r, d):
         127 +        rx, ry = self._pick_pose(r, d)
         128 +        return (r[0] - rx, r[1] - rx, r[2] - ry)
   91    129  
   92        -        rects = {}
   93        -        for o in obstructions + [block]:
   94        -            rects[o.name] = self._rect(state, o)
         130 +    def _plan(self, state):
         131 +        robot, block, surface, obst = self._parse(state)
         132 +        start = (_g(state, robot, "x"), _g(state, robot, "y"))
         133 +        sr = _rect(state, surface)
         134 +        br = _rect(state, block)
         135 +        orects = {o.name: _rect(state, o) for o in obst}
         136 +        boxes0 = self._assembly()
         137 +        cand = [n for n, r in orects.items()
         138 +                if r[1] > sr[0] - 0.1 and r[0] < sr[1] + 0.1]
         139 +        best = None
         140 +        for k in range(len(cand) + 1):
         141 +            if best is not None and k > 2:
         142 +                break
         143 +            for R in itertools.permutations(cand, k):
         144 +                res = self._plan_subset(start, R, orects, br, (sr[0], sr[1]), boxes0)
         145 +                if res is not None and (best is None or res[0] < best[0]):
         146 +                    best = res
         147 +        return None if best is None else best[1]
   95    148  
   96        -        # gripper face y (pointing down)
   97        -        face = ry - arm - gw
         149 +    def _plan_subset(self, start, R, orects, br, surf, boxes0):
         150 +        sx0, sx1 = surf
         151 +        bw = br[1] - br[0]
         152 +        lo, hi = self._grasp_d(br)
         153 +        if lo > hi:
         154 +            return None
         155 +        legs = []
         156 +        cost = 0.0
         157 +        pos = start
         158 +        cur = dict(orects)
         159 +        block_obs = (br[0], br[1], br[3])
         160 +        e = 0.004
         161 +        lefts = np.arange(sx0 + e, sx1 - bw - e + 1e-9, 0.004)
         162 +        if len(lefts) == 0:
         163 +            lefts = np.array([(sx0 + sx1) / 2 - bw / 2])
         164 +        for n in R:
         165 +            r = cur[n]
         166 +            lo_o, hi_o = self._grasp_d(r)
         167 +            if lo_o > hi_o:
         168 +                return None
         169 +            d = float(np.clip(0.0, lo_o, hi_o))
         170 +            pick = self._pick_pose(r, d)
         171 +            others = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [block_obs]
         172 +            c1 = self._leg_cost(pos, pick, boxes0, others + [(r[0], r[1], r[3])])
         173 +            held = self._held_rel(r, d)
         174 +            boxes_h = self._assembly(held)
         175 +            w, h = r[1] - r[0], r[3] - r[2]
         176 +            forb = [(q[0], q[1]) for m, q in cur.items() if m != n]
         177 +            forb.append((br[0], br[1]))
         178 +            bestd = None
         179 +            for left in np.arange(0.003, WORLD_MAX_X - 0.003 - w, 0.01):
         180 +                a, b = left, left + w
         181 +                if any(b > f0 - 0.012 and a < f1 + 0.012 for f0, f1 in forb):
         182 +                    continue
         183 +                if b > sx0 - 0.04 and a < sx1 + 0.04:
         184 +                    ok = any(b + 0.04 <= L or a - 0.04 >= L + bw for L in lefts)
         185 +                    if not ok:
         186 +                        continue
         187 +                tx = left - held[0]
         188 +                if not (XMIN <= tx <= XMAX):
         189 +                    continue
         190 +                ty = DROP_BOT - held[2]
         191 +                if ty > YMAX:
         192 +                    continue
         193 +                dpose = (tx, ty)
         194 +                c2 = self._leg_cost(pick, dpose, boxes_h, others)
         195 +                c3 = abs(tx - (br[0] + br[1]) / 2) / STEP
         196 +                sc = c2 + c3
         197 +                if bestd is None or sc < bestd[0]:
         198 +                    bestd = (sc, dpose, left, c2)
         199 +            if bestd is None:
         200 +                return None
         201 +            _, dpose, left, c2 = bestd
         202 +            cost += c1 + c2
         203 +            legs.append(("pick", n, d, pick))
         204 +            legs.append(("drop", n, dpose))
         205 +            cur[n] = (left, left + w, DROP_BOT, DROP_BOT + h)
         206 +            pos = dpose
         207 +        obst_final = [(q[0], q[1], q[3]) for q in cur.values()]
         208 +        bestp = None
         209 +        for d in np.unique(np.clip(np.array([0.0, lo, hi, (lo + hi) / 2]), lo, hi)):
         210 +            pick = self._pick_pose(br, d)
         211 +            held = self._held_rel(br, d)
         212 +            boxes_h = self._assembly(held)
         213 +            c1 = self._leg_cost(pos, pick, boxes0, obst_final + [block_obs])
         214 +            for L in lefts:
         215 +                if any(L + bw > q[0] - 0.003 and L < q[1] + 0.003 for q in cur.values()):
         216 +                    continue
         217 +                tx = L - held[0]
         218 +                if not (XMIN <= tx <= XMAX):
         219 +                    continue
         220 +                ty = PLACE_BOT - held[2]
         221 +                if ty > YMAX:
         222 +                    continue
         223 +                req = float(self._safe(np.array([tx]), boxes_h, obst_final)[0])
         224 +                if req > ty + 1e-6:
         225 +                    continue
         226 +                c2 = self._leg_cost(pick, (tx, ty), boxes_h, obst_final)
         227 +                sc = c1 + c2
         228 +                if bestp is None or sc < bestp[0]:
         229 +                    bestp = (sc, float(d), pick, (tx, ty))
         230 +        if bestp is None:
         231 +            return None
         232 +        sc, d, pick, ppose = bestp
         233 +        cost += sc
         234 +        legs.append(("pick", self.block_name, d, pick))
         235 +        legs.append(("place", self.block_name, ppose))
         236 +        return cost, legs
   98    237  
   99        -        # travel height: carried object bottom clears all tops
  100        -        max_top = max(r[3] for r in rects.values())
  101        -        carry_h = 0.0
  102        -        if self.target is not None and vac > 0.5 and self.phase in ("lift", "carry", "lower"):
  103        -            tr = rects[self.target]
  104        -            carry_h = tr[3] - tr[2]
  105        -        travel_y = max_top + 0.05 + carry_h + arm_max + gw
  106        -        travel_y = min(max(travel_y, 0.6), 0.89)
         238 +    def _fallback_plan(self, state):
         239 +        robot, block, surface, obst = self._parse(state)
         240 +        br = _rect(state, block)
         241 +        sr = _rect(state, surface)
         242 +        lo, hi = self._grasp_d(br)
         243 +        d = float(np.clip(0.0, lo, hi)) if lo <= hi else 0.0
         244 +        pick = self._pick_pose(br, d)
         245 +        held = self._held_rel(br, d)
         246 +        tx = float(np.clip((sr[0] + sr[1]) / 2 - (br[1] - br[0]) / 2 - held[0], XMIN, XMAX))
         247 +        return [("pick", self.block_name, d, pick),
         248 +                ("place", self.block_name, (tx, PLACE_BOT - held[2]))]
  107    249  
  108        -        dx = dy = dth = darm = 0.0
  109        -        vcmd = 1.0 if vac > 0.5 else 0.0
         250 +    # ------------------------------------------------------------ control
         251 +    def _act(self, dx, dy, dth, darm, vac):
         252 +        a = np.array([dx, dy, dth, darm, vac], dtype=np.float32)
         253 +        return np.clip(a, self.low, self.high)
  110    254  
  111        -        # keep orientation down and arm extended
         255 +    def get_action(self, state):
         256 +        self.steps += 1
         257 +        robot, block, surface, obst = self._parse(state)
         258 +        rx, ry = _g(state, robot, "x"), _g(state, robot, "y")
         259 +        rth = _g(state, robot, "theta")
         260 +        arm = _g(state, robot, "arm_joint")
         261 +        vac = _g(state, robot, "vacuum")
  112    262          th_err = (-np.pi / 2 - rth + np.pi) % (2 * np.pi) - np.pi
  113        -        dth = np.clip(th_err, -self.max_dth, self.max_dth)
  114        -        darm = np.clip(arm_max - arm, -self.max_darm, self.max_darm)
  115        -
  116        -        if self.phase == "choose":
  117        -            # obstructions overlapping surface
  118        -            bw = rects[block.name][1] - rects[block.name][0]
  119        -            tgt = None
  120        -            best = None
  121        -            for o in obstructions:
  122        -                x0, x1, y0, y1 = rects[o.name]
  123        -                if x1 > sx0 - 0.005 and x0 < sx1 + 0.005 and y0 < sy1 + 0.3:
  124        -                    d = abs((x0 + x1) / 2 - (sx0 + sx1) / 2)
  125        -                    if best is None or d < best:
  126        -                        best, tgt = d, o.name
  127        -            if tgt is None:
  128        -                tgt = block.name
  129        -            self.target = tgt
  130        -            self.phase = "rise"
  131        -            self.last_cmd = (0, 0)
  132        -            return self._act(0, 0, dth, darm, 0.0)
         263 +        dth = float(np.clip(th_err, -self.max_dth, self.max_dth))
         264 +        darm = float(np.clip(self.arm - arm, -self.max_darm, self.max_darm))
  133    265  
  134        -        tr = rects[self.target]
  135        -        tcx = self._grasp_x(tr, rects[block.name], (sx0, sx1), self.target == block.name)
  136        -
  137        -        if self.phase == "rise":
  138        -            # go up to travel height without vacuum
  139        -            if ry < travel_y - 1e-3:
  140        -                dy = min(travel_y - ry, self.max_dx)
  141        -            else:
  142        -                self.phase = "over"
  143        -        if self.phase == "over":
  144        -            ex = tcx - rx
  145        -            if abs(ex) > 1e-4:
  146        -                dx = ex
  147        -            else:
  148        -                self.phase = "descend"
  149        -                self.blocked_count = 0
  150        -        if self.phase == "descend":
  151        -            contact_y = tr[3] + arm + gw
  152        -            if not moved:
  153        -                self.phase = "grasp"
  154        -            else:
  155        -                rem = ry - contact_y
  156        -                if rem > 0.006:
  157        -                    dy = -min(rem - 0.004, self.max_dx)
  158        -                else:
  159        -                    dy = -0.002
  160        -                if rem < -0.02:
  161        -                    self.phase = "grasp"
  162        -                    dy = 0.0
  163        -        if self.phase == "grasp":
  164        -            vcmd = 1.0
  165        -            dy = 0.0
  166        -            self.grasp_ref = (tr[0] - rx, tr[2] - ry)
  167        -            self.phase = "lift"
  168        -            self.last_cmd = (0, 0)
  169        -            return self._act(0, 0, dth, 0.0, vcmd)
  170        -        if self.phase == "lift":
  171        -            vcmd = 1.0
  172        -            if ry < travel_y - 1e-3:
  173        -                dy = min(travel_y - ry, self.max_dx)
  174        -            else:
  175        -                self.phase = "carry"
  176        -                self._plan_drop(state, rects, block, (sx0, sx1), rx)
  177        -        if self.phase == "carry":
  178        -            vcmd = 1.0
  179        -            ex = self.drop_x - rx
  180        -            if abs(ex) > 1e-4:
  181        -                dx = ex
  182        -            else:
  183        -                self.phase = "lower"
  184        -        if self.phase == "lower":
  185        -            vcmd = 1.0
  186        -            is_block = self.target == block.name
  187        -            floor_top = sy1 if is_block else FLOOR_Y
  188        -            rem = tr[2] - floor_top
  189        -            if not moved:
  190        -                self.phase = "release"
         266 +        if self.last is not None:
         267 +            lx, ly, cdx, cdy = self.last
         268 +            if (abs(cdx) > 1e-5 or abs(cdy) > 1e-5) and abs(lx - rx) < 1e-7 and abs(ly - ry) < 1e-7:
         269 +                self.stuck += 1
  191    270              else:
  192        -                if rem > 0.006:
  193        -                    dy = -min(rem - 0.003, self.max_dx)
  194        -                else:
  195        -                    dy = -0.002
  196        -        if self.phase == "release":
  197        -            vcmd = 0.0
  198        -            dy = 0.0
  199        -            self.phase = "post"
  200        -            self.last_cmd = (0, 0)
  201        -            return self._act(0, 0, dth, 0.0, vcmd)
  202        -        if self.phase == "post":
  203        -            vcmd = 0.0
  204        -            self.phase = "choose"
  205        -            dy = 0.02
         271 +                self.stuck = 0
  206    272  
  207        -        dx = float(np.clip(dx, -self.max_dx, self.max_dx))
  208        -        dy = float(np.clip(dy, -self.max_dx, self.max_dx))
  209        -        # keep within world
  210        -        self.last_cmd = (dx, dy)
  211        -        return self._act(dx, dy, dth, darm, vcmd)
         273 +        if self.leg >= len(self.legs):
         274 +            self.last = None
         275 +            return self._act(0, 0.0, dth, darm, vac)
  212    276  
  213        -    XMIN, XMAX = 0.102, 1.516
         277 +        leg = self.legs[self.leg]
         278 +        kind, name = leg[0], leg[1]
         279 +        allr = {o.name: _rect(state, o) for o in obst + [block]}
         280 +        holding = kind in ("drop", "place")
         281 +        held_rel = None
         282 +        if holding:
         283 +            r = allr[name]
         284 +            held_rel = (r[0] - rx, r[1] - rx, r[2] - ry)
         285 +        obstacles = [(q[0], q[1], q[3]) for n, q in allr.items()
         286 +                     if not (holding and n == name)]
         287 +        tx, ty = leg[3] if kind == "pick" else leg[2]
         288 +        boxes = self._assembly(held_rel)
         289 +        vcmd = 1.0 if holding else 0.0
  214    290  
  215        -    def _grasp_x(self, tr, br, surf, is_block):
  216        -        """Robot x at which to grasp object with x-range tr."""
  217        -        cx = (tr[0] + tr[1]) / 2
  218        -        hw = (tr[1] - tr[0]) / 2
  219        -        dmax = max(hw + 0.035 - 0.012, 0.0)  # gripper overlap allowance
  220        -        lo, hi = -dmax, dmax
  221        -        # pick reachability
  222        -        lo = max(lo, self.XMIN - cx)
  223        -        hi = min(hi, self.XMAX - cx)
  224        -        if is_block:
  225        -            scx = (surf[0] + surf[1]) / 2
  226        -            lo2 = max(lo, self.XMIN - scx)
  227        -            hi2 = min(hi, self.XMAX - scx)
  228        -            if lo2 <= hi2:
  229        -                lo, hi = lo2, hi2
  230        -        if lo > hi:
  231        -            return float(np.clip(cx, self.XMIN, self.XMAX))
  232        -        d = float(np.clip(0.0, lo, hi))
  233        -        return cx + d
         291 +        dx, dy = self._control(rx, ry, tx, ty, boxes, obstacles)
         292 +        if self.stuck >= 2:
         293 +            dx, dy = 0.0, min(STEP, YMAX - ry)
         294 +        arrived = abs(rx + dx - tx) < 1e-5 and abs(ry + dy - ty) < 1e-5
         295 +        if arrived:
         296 +            if kind == "pick":
         297 +                vcmd = 1.0
         298 +            elif kind == "drop":
         299 +                vcmd = 0.0
         300 +            self.leg += 1
         301 +        self.last = (rx, ry, dx, dy)
         302 +        return self._act(dx, dy, dth, darm, vcmd)
  234    303  
  235        -    def _plan_drop(self, state, rects, block, surf, rx):
  236        -        tr = rects[self.target]
  237        -        w = tr[1] - tr[0]
  238        -        off = tr[0] - rx  # left edge relative to robot x
  239        -        if self.target == block.name:
  240        -            sx0, sx1 = surf
  241        -            want_left = (sx0 + sx1) / 2 - w / 2
  242        -            self.drop_x = float(np.clip(want_left - off, self.XMIN, self.XMAX))
  243        -            return
  244        -        # choose free floor location maximizing clearance
  245        -        sx0, sx1 = surf
  246        -        bw = rects[block.name][1] - rects[block.name][0]
  247        -        forb = [(sx0 - 0.02, sx1 + 0.02)]
  248        -        for n, r in rects.items():
  249        -            if n == self.target:
  250        -                continue
  251        -            forb.append((r[0], r[1]))
  252        -        best = None
  253        -        for left in np.arange(0.005, WORLD_MAX_X - 0.005 - w, 0.005):
  254        -            a, b = left, left + w
  255        -            if not (self.XMIN <= left - off <= self.XMAX):
  256        -                continue
  257        -            clr = min(min(abs(a - f1) if a >= f1 else (abs(f0 - b) if b <= f0 else -1.0)
  258        -                          for f0, f1 in forb), 0.3)
  259        -            if clr < 0:
         304 +    def _control(self, rx, ry, tx, ty, boxes, obstacles):
         305 +        md = self.max_d - 1e-6
         306 +        ex, ey = tx - rx, ty - ry
         307 +        if abs(ex) <= md and abs(ey) <= md:
         308 +            req = float(self._safe(np.array([tx]), boxes, obstacles)[0])
         309 +            X = np.linspace(rx, tx, 12)
         310 +            if req <= ty + 1e-6 and float(self._safe(X, boxes, obstacles).max()) <= max(ty, ry) + 1e-6:
         311 +                return ex, ey
         312 +        n = max(2, int(abs(ex) / 0.0025) + 2)
         313 +        X = np.linspace(rx, tx, n)
         314 +        S = self._safe(X, boxes, obstacles)
         315 +        sgn = 1.0 if ex >= 0 else -1.0
         316 +        dxf = float(np.clip(ex, -md, md))
         317 +        for f in (1.0, 0.8, 0.6, 0.4, 0.25, 0.1, 0.0):
         318 +            dx = dxf * f
         319 +            nx = rx + dx
         320 +            sw = (X - nx) * sgn <= 1e-9
         321 +            req_sweep = float(S[sw].max()) if sw.any() else -1.0
         322 +            req_sweep = max(req_sweep, float(self._safe(np.array([nx]), boxes, obstacles)[0]))
         323 +            ahead = ~sw
         324 +            req_ahead = float((S[ahead] - 0.9 * np.abs(X[ahead] - nx)).max()) if ahead.any() else -1.0
         325 +            req = max(req_sweep, req_ahead)
         326 +            ny = ry + float(np.clip(ey, -md, md))
         327 +            ny = max(ny, req + 1e-4)
         328 +            if ny - ry > md + 1e-9 or ny > YMAX:
  260    329                  continue
  261        -            score = clr - 0.02 * abs(left + w / 2 - rx)
  262        -            if best is None or score > best[0]:
  263        -                best = (score, left)
  264        -        left = best[1] if best else 0.15
  265        -        self.drop_x = float(np.clip(left - off, self.XMIN, self.XMAX))
         330 +            return dx, ny - ry
         331 +        return 0.0, max(0.0, min(md, YMAX - ry))
diff --git a/approach_v1.py b/approach_v1.py
new file mode 100644
index 0000000..3808e73
--- /dev/null
+++ b/approach_v1.py
@@ -0,0 +1,265 @@
           1 +import numpy as np
           2 +
           3 +WORLD_MIN_X = 0.0
           4 +WORLD_MAX_X = 1.618
           5 +FLOOR_Y = 0.1
           6 +
           7 +
           8 +class GeneratedApproach:
           9 +    def __init__(self, action_space, observation_space, primitives):
          10 +        self.low = np.array(action_space.low, dtype=np.float32)
          11 +        self.high = np.array(action_space.high, dtype=np.float32)
          12 +        self.max_dx = float(self.high[0])
          13 +        self.max_dth = float(self.high[2])
          14 +        self.max_darm = float(self.high[3])
          15 +
          16 +    # ------------------------------------------------------------------ utils
          17 +    def _g(self, s, o, f):
          18 +        return float(s.get(o, f))
          19 +
          20 +    def _rect(self, s, o):
          21 +        x, y = self._g(s, o, "x"), self._g(s, o, "y")
          22 +        w, h = self._g(s, o, "width"), self._g(s, o, "height")
          23 +        th = self._g(s, o, "theta")
          24 +        c, sn = np.cos(th), np.sin(th)
          25 +        pts = np.array([[0, 0], [w, 0], [w, h], [0, h]])
          26 +        R = np.array([[c, -sn], [sn, c]])
          27 +        v = pts @ R.T + np.array([x, y])
          28 +        return v[:, 0].min(), v[:, 0].max(), v[:, 1].min(), v[:, 1].max()
          29 +
          30 +    def _parse(self, s):
          31 +        robot = s.get_objects(self.t_robot)[0] if self.t_robot else None
          32 +        return robot
          33 +
          34 +    def _objs(self, s):
          35 +        d = {}
          36 +        for name in s.get_object_names():
          37 +            o = s.get_object_from_name(name)
          38 +            d[str(name) if isinstance(name, str) else o.name] = o
          39 +        return d
          40 +
          41 +    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0, vac=0.0):
          42 +        a = np.array([dx, dy, dth, darm, vac], dtype=np.float32)
          43 +        return np.clip(a, self.low, self.high)
          44 +
          45 +    # ------------------------------------------------------------------ api
          46 +    def reset(self, state, info):
          47 +        self.phase = "choose"
          48 +        self.target = None  # name of object being manipulated
          49 +        self.drop_x = None
          50 +        self.last_robot = None
          51 +        self.last_cmd = None
          52 +        self.blocked_count = 0
          53 +        self.grasp_offset = None
          54 +        self.steps = 0
          55 +
          56 +    def get_action(self, state):
          57 +        self.steps += 1
          58 +        objs = self._objs(state)
          59 +        robot = None
          60 +        for n, o in objs.items():
          61 +            if o.type.name == "crv_robot":
          62 +                robot = o
          63 +        rx, ry = self._g(state, robot, "x"), self._g(state, robot, "y")
          64 +        rth = self._g(state, robot, "theta")
          65 +        arm = self._g(state, robot, "arm_joint")
          66 +        arm_max = self._g(state, robot, "arm_length")
          67 +        gw = self._g(state, robot, "gripper_width")
          68 +        base_r = self._g(state, robot, "base_radius")
          69 +        vac = self._g(state, robot, "vacuum")
          70 +
          71 +        # detect blocked motion
          72 +        moved = True
          73 +        if self.last_robot is not None and self.last_cmd is not None:
          74 +            lx, ly = self.last_robot
          75 +            cdx, cdy = self.last_cmd
          76 +            if (abs(cdx) > 1e-5 or abs(cdy) > 1e-5) and abs(lx - rx) < 1e-7 and abs(ly - ry) < 1e-7:
          77 +                moved = False
          78 +        self.last_robot = (rx, ry)
          79 +
          80 +        block = surface = None
          81 +        obstructions = []
          82 +        for n, o in objs.items():
          83 +            tn = o.type.name
          84 +            if tn == "target_block":
          85 +                block = o
          86 +            elif tn == "target_surface":
          87 +                surface = o
          88 +            elif tn == "rectangle":
          89 +                obstructions.append(o)
          90 +        sx0, sx1, sy0, sy1 = self._rect(state, surface)
          91 +
          92 +        rects = {}
          93 +        for o in obstructions + [block]:
          94 +            rects[o.name] = self._rect(state, o)
          95 +
          96 +        # gripper face y (pointing down)
          97 +        face = ry - arm - gw
          98 +
          99 +        # travel height: carried object bottom clears all tops
         100 +        max_top = max(r[3] for r in rects.values())
         101 +        carry_h = 0.0
         102 +        if self.target is not None and vac > 0.5 and self.phase in ("lift", "carry", "lower"):
         103 +            tr = rects[self.target]
         104 +            carry_h = tr[3] - tr[2]
         105 +        travel_y = max_top + 0.05 + carry_h + arm_max + gw
         106 +        travel_y = min(max(travel_y, 0.6), 0.89)
         107 +
         108 +        dx = dy = dth = darm = 0.0
         109 +        vcmd = 1.0 if vac > 0.5 else 0.0
         110 +
         111 +        # keep orientation down and arm extended
         112 +        th_err = (-np.pi / 2 - rth + np.pi) % (2 * np.pi) - np.pi
         113 +        dth = np.clip(th_err, -self.max_dth, self.max_dth)
         114 +        darm = np.clip(arm_max - arm, -self.max_darm, self.max_darm)
         115 +
         116 +        if self.phase == "choose":
         117 +            # obstructions overlapping surface
         118 +            bw = rects[block.name][1] - rects[block.name][0]
         119 +            tgt = None
         120 +            best = None
         121 +            for o in obstructions:
         122 +                x0, x1, y0, y1 = rects[o.name]
         123 +                if x1 > sx0 - 0.005 and x0 < sx1 + 0.005 and y0 < sy1 + 0.3:
         124 +                    d = abs((x0 + x1) / 2 - (sx0 + sx1) / 2)
         125 +                    if best is None or d < best:
         126 +                        best, tgt = d, o.name
         127 +            if tgt is None:
         128 +                tgt = block.name
         129 +            self.target = tgt
         130 +            self.phase = "rise"
         131 +            self.last_cmd = (0, 0)
         132 +            return self._act(0, 0, dth, darm, 0.0)
         133 +
         134 +        tr = rects[self.target]
         135 +        tcx = self._grasp_x(tr, rects[block.name], (sx0, sx1), self.target == block.name)
         136 +
         137 +        if self.phase == "rise":
         138 +            # go up to travel height without vacuum
         139 +            if ry < travel_y - 1e-3:
         140 +                dy = min(travel_y - ry, self.max_dx)
         141 +            else:
         142 +                self.phase = "over"
         143 +        if self.phase == "over":
         144 +            ex = tcx - rx
         145 +            if abs(ex) > 1e-4:
         146 +                dx = ex
         147 +            else:
         148 +                self.phase = "descend"
         149 +                self.blocked_count = 0
         150 +        if self.phase == "descend":
         151 +            contact_y = tr[3] + arm + gw
         152 +            if not moved:
         153 +                self.phase = "grasp"
         154 +            else:
         155 +                rem = ry - contact_y
         156 +                if rem > 0.006:
         157 +                    dy = -min(rem - 0.004, self.max_dx)
         158 +                else:
         159 +                    dy = -0.002
         160 +                if rem < -0.02:
         161 +                    self.phase = "grasp"
         162 +                    dy = 0.0
         163 +        if self.phase == "grasp":
         164 +            vcmd = 1.0
         165 +            dy = 0.0
         166 +            self.grasp_ref = (tr[0] - rx, tr[2] - ry)
         167 +            self.phase = "lift"
         168 +            self.last_cmd = (0, 0)
         169 +            return self._act(0, 0, dth, 0.0, vcmd)
         170 +        if self.phase == "lift":
         171 +            vcmd = 1.0
         172 +            if ry < travel_y - 1e-3:
         173 +                dy = min(travel_y - ry, self.max_dx)
         174 +            else:
         175 +                self.phase = "carry"
         176 +                self._plan_drop(state, rects, block, (sx0, sx1), rx)
         177 +        if self.phase == "carry":
         178 +            vcmd = 1.0
         179 +            ex = self.drop_x - rx
         180 +            if abs(ex) > 1e-4:
         181 +                dx = ex
         182 +            else:
         183 +                self.phase = "lower"
         184 +        if self.phase == "lower":
         185 +            vcmd = 1.0
         186 +            is_block = self.target == block.name
         187 +            floor_top = sy1 if is_block else FLOOR_Y
         188 +            rem = tr[2] - floor_top
         189 +            if not moved:
         190 +                self.phase = "release"
         191 +            else:
         192 +                if rem > 0.006:
         193 +                    dy = -min(rem - 0.003, self.max_dx)
         194 +                else:
         195 +                    dy = -0.002
         196 +        if self.phase == "release":
         197 +            vcmd = 0.0
         198 +            dy = 0.0
         199 +            self.phase = "post"
         200 +            self.last_cmd = (0, 0)
         201 +            return self._act(0, 0, dth, 0.0, vcmd)
         202 +        if self.phase == "post":
         203 +            vcmd = 0.0
         204 +            self.phase = "choose"
         205 +            dy = 0.02
         206 +
         207 +        dx = float(np.clip(dx, -self.max_dx, self.max_dx))
         208 +        dy = float(np.clip(dy, -self.max_dx, self.max_dx))
         209 +        # keep within world
         210 +        self.last_cmd = (dx, dy)
         211 +        return self._act(dx, dy, dth, darm, vcmd)
         212 +
         213 +    XMIN, XMAX = 0.102, 1.516
         214 +
         215 +    def _grasp_x(self, tr, br, surf, is_block):
         216 +        """Robot x at which to grasp object with x-range tr."""
         217 +        cx = (tr[0] + tr[1]) / 2
         218 +        hw = (tr[1] - tr[0]) / 2
         219 +        dmax = max(hw + 0.035 - 0.012, 0.0)  # gripper overlap allowance
         220 +        lo, hi = -dmax, dmax
         221 +        # pick reachability
         222 +        lo = max(lo, self.XMIN - cx)
         223 +        hi = min(hi, self.XMAX - cx)
         224 +        if is_block:
         225 +            scx = (surf[0] + surf[1]) / 2
         226 +            lo2 = max(lo, self.XMIN - scx)
         227 +            hi2 = min(hi, self.XMAX - scx)
         228 +            if lo2 <= hi2:
         229 +                lo, hi = lo2, hi2
         230 +        if lo > hi:
         231 +            return float(np.clip(cx, self.XMIN, self.XMAX))
         232 +        d = float(np.clip(0.0, lo, hi))
         233 +        return cx + d
         234 +
         235 +    def _plan_drop(self, state, rects, block, surf, rx):
         236 +        tr = rects[self.target]
         237 +        w = tr[1] - tr[0]
         238 +        off = tr[0] - rx  # left edge relative to robot x
         239 +        if self.target == block.name:
         240 +            sx0, sx1 = surf
         241 +            want_left = (sx0 + sx1) / 2 - w / 2
         242 +            self.drop_x = float(np.clip(want_left - off, self.XMIN, self.XMAX))
         243 +            return
         244 +        # choose free floor location maximizing clearance
         245 +        sx0, sx1 = surf
         246 +        bw = rects[block.name][1] - rects[block.name][0]
         247 +        forb = [(sx0 - 0.02, sx1 + 0.02)]
         248 +        for n, r in rects.items():
         249 +            if n == self.target:
         250 +                continue
         251 +            forb.append((r[0], r[1]))
         252 +        best = None
         253 +        for left in np.arange(0.005, WORLD_MAX_X - 0.005 - w, 0.005):
         254 +            a, b = left, left + w
         255 +            if not (self.XMIN <= left - off <= self.XMAX):
         256 +                continue
         257 +            clr = min(min(abs(a - f1) if a >= f1 else (abs(f0 - b) if b <= f0 else -1.0)
         258 +                          for f0, f1 in forb), 0.3)
         259 +            if clr < 0:
         260 +                continue
         261 +            score = clr - 0.02 * abs(left + w / 2 - rx)
         262 +            if best is None or score > best[0]:
         263 +                best = (score, left)
         264 +        left = best[1] if best else 0.15
         265 +        self.drop_x = float(np.clip(left - off, self.XMIN, self.XMAX))
diff --git a/probe4.py b/probe4.py
new file mode 100644
index 0000000..e6fe778
--- /dev/null
+++ b/probe4.py
@@ -0,0 +1,32 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +def A(*a): return np.array(a,dtype=np.float32)
           4 +def setup(gap, vac_during=False, seed=0):
           5 +    env=make_env(); obs,_=env.reset(seed=seed)
           6 +    r=obs.get_object_from_name('robot'); b=obs.get_object_from_name('target_block')
           7 +    g=lambda o,f: float(obs.get(o,f))
           8 +    tx=g(b,'x')+g(b,'width')/2; top=g(b,'y')+g(b,'height')
           9 +    # move to x with arm extended
          10 +    obs,*_=env.step(A(0,0,0,0.1,0))
          11 +    for _ in range(40): obs,*_=env.step(A(np.clip(tx-g(r,'x'),-.05,.05),0,0,0,0))
          12 +    ty=top+0.2+0.01+gap
          13 +    for _ in range(40): obs,*_=env.step(A(0,np.clip(ty-g(r,'y'),-.05,.05),0,0,1 if vac_during else 0))
          14 +    return env,obs,r,b,g
          15 +# (b) grasp tolerance
          16 +for gap in [0.0005,0.002,0.005,0.01,0.02]:
          17 +    env,obs,r,b,g=setup(gap)
          18 +    obs,*_=env.step(A(0,0,0,0,1)); by=float(obs.get(b,'y'))
          19 +    obs,*_=env.step(A(0,0.05,0,0,1)); print("gap",gap,"lifted", round(float(obs.get(b,'y'))-by,4)); env.close()
          20 +# vac on during descent from far: grabbed?
          21 +env,obs,r,b,g=setup(0.0005, vac_during=True); by=float(obs.get(b,'y'))
          22 +obs,*_=env.step(A(0,0.05,0,0,1)); print("vac-during descent lifted", round(float(obs.get(b,'y'))-by,4))
          23 +# (c) release and move same step; gravity
          24 +obs,*_=env.step(A(0,0.05,0,0,1)); y1=float(obs.get(b,'y'))
          25 +obs,*_=env.step(A(0,0.05,0,0,0)); print("release+move: block dy", round(float(obs.get(b,'y'))-y1,4))
          26 +for i in range(3): obs,*_=env.step(A(0,0.0,0,0,0))
          27 +print("after release block y", float(obs.get(b,'y')), "(gravity if decreasing)")
          28 +env.close()
          29 +# move+vac same step: move into contact from gap 0.03 with dy=-0.03 and vac=1
          30 +env,obs,r,b,g=setup(0.03); by=float(obs.get(b,'y'))
          31 +obs,*_=env.step(A(0,-0.0295,0,0,1)); print("robot y after", g(r,'y'), "vac", g(r,'vacuum'))
          32 +obs,*_=env.step(A(0,0.05,0,0,1)); print("move+vac same step lifted", round(float(obs.get(b,'y'))-by,4)); env.close()
diff --git a/test_approach.py b/test_approach.py
index cc38318..c855e24 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -2,10 +2,11 @@ import sys, time
    2      2  import numpy as np
    3      3  from env_client import make_env
    4      4  from approach import GeneratedApproach
           5 +OC=None
    5      6  def run(seed, verbose=False):
    6      7      env = make_env()
    7      8      ap = GeneratedApproach(env.action_space, env.observation_space, {})
    8        -    obs, info = env.reset(seed=seed)
           9 +    obs, info = env.reset(seed=seed, options={'object_count':OC} if OC is not None else None)
    9     10      ap.reset(obs, info)
   10     11      t=time.time()
   11     12      for t_ in range(env.max_steps):
@@ -15,9 +16,10 @@ def run(seed, verbose=False):
   15     16      env.close()
   16     17      return te, t_+1, info.get('object_count'), ap.phase
   17     18  if __name__ == "__main__":
          19 +    if len(sys.argv)>3: OC=int(sys.argv[3])
   18     20      seeds = range(int(sys.argv[1]), int(sys.argv[2]))
   19     21      from concurrent.futures import ThreadPoolExecutor
   20        -    with ThreadPoolExecutor(8) as ex:
          22 +    with ThreadPoolExecutor(16) as ex:
   21     23          res = list(ex.map(run, seeds))
   22     24      ok = 0
   23     25      for s, (te, n, c, ph) in zip(seeds, res):
```

</details>

<a id="C005"></a>
### C005 · check pick-pose feasibility

Commit `1599f2acb4e64550e1bb359f49880d876e8ce0c0`; parents: f47aa672e8c0272618651a4d939ddf722b8e820e. Recorded author date: 2026-09-30T11:42:31+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0241](01_timeline.md#E0241): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_1599f2a_approach.py) · [Exact all-file diff](evidence/diffs/C005_1599f2a.diff)

[Previous saved controller snapshot](evidence/versions/C004_f47aa67_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 77a18be..8a08531 100644
--- a/approach.py
+++ b/approach.py
@@ -123,6 +123,22 @@ class GeneratedApproach:
  123    123          cx = (r[0] + r[1]) / 2
  124    124          return (cx + d, r[3] + GAP + self.arm + self.gw)
  125    125  
         126 +    def _pick_ok(self, r, d, obstacles):
         127 +        """Is the grasp pose over r at offset d clear of other obstacles?"""
         128 +        px, py = self._pick_pose(r, d)
         129 +        if not (XMIN <= px <= XMAX) or py > YMAX:
         130 +            return False
         131 +        req = float(self._safe(np.array([px]), self._assembly(), obstacles)[0])
         132 +        return req <= py + 1e-6
         133 +
         134 +    def _d_options(self, r):
         135 +        lo, hi = self._grasp_d(r)
         136 +        if lo > hi:
         137 +            return []
         138 +        c = float(np.clip(0.0, lo, hi))
         139 +        opts = [c] + list(np.linspace(lo, hi, 9))
         140 +        return sorted(set(float(v) for v in opts), key=lambda v: abs(v - c))
         141 +
  126    142      def _held_rel(self, r, d):
  127    143          rx, ry = self._pick_pose(r, d)
  128    144          return (r[0] - rx, r[1] - rx, r[2] - ry)
@@ -157,18 +173,19 @@ class GeneratedApproach:
  157    173          pos = start
  158    174          cur = dict(orects)
  159    175          block_obs = (br[0], br[1], br[3])
         176 +        bd_opts = self._d_options(br)
  160    177          e = 0.004
  161    178          lefts = np.arange(sx0 + e, sx1 - bw - e + 1e-9, 0.004)
  162    179          if len(lefts) == 0:
  163    180              lefts = np.array([(sx0 + sx1) / 2 - bw / 2])
  164    181          for n in R:
  165    182              r = cur[n]
  166        -            lo_o, hi_o = self._grasp_d(r)
  167        -            if lo_o > hi_o:
         183 +            others = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [block_obs]
         184 +            dl = [v for v in self._d_options(r) if self._pick_ok(r, v, others)]
         185 +            if not dl:
  168    186                  return None
  169        -            d = float(np.clip(0.0, lo_o, hi_o))
         187 +            d = dl[0]
  170    188              pick = self._pick_pose(r, d)
  171        -            others = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [block_obs]
  172    189              c1 = self._leg_cost(pos, pick, boxes0, others + [(r[0], r[1], r[3])])
  173    190              held = self._held_rel(r, d)
  174    191              boxes_h = self._assembly(held)
@@ -191,6 +208,10 @@ class GeneratedApproach:
  191    208                  if ty > YMAX:
  192    209                      continue
  193    210                  dpose = (tx, ty)
         211 +                nob = (left, left + w, DROP_BOT + h)
         212 +                obs_after = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [nob]
         213 +                if not any(self._pick_ok(br, v, obs_after) for v in bd_opts[:5]):
         214 +                    continue
  194    215                  c2 = self._leg_cost(pick, dpose, boxes_h, others)
  195    216                  c3 = abs(tx - (br[0] + br[1]) / 2) / STEP
  196    217                  sc = c2 + c3
@@ -206,7 +227,9 @@ class GeneratedApproach:
  206    227              pos = dpose
  207    228          obst_final = [(q[0], q[1], q[3]) for q in cur.values()]
  208    229          bestp = None
  209        -        for d in np.unique(np.clip(np.array([0.0, lo, hi, (lo + hi) / 2]), lo, hi)):
         230 +        for d in bd_opts:
         231 +            if not self._pick_ok(br, d, obst_final):
         232 +                continue
  210    233              pick = self._pick_pose(br, d)
  211    234              held = self._held_rel(br, d)
  212    235              boxes_h = self._assembly(held)
diff --git a/dbg.py b/dbg.py
index 06ef7d7..d7eef52 100644
--- a/dbg.py
+++ b/dbg.py
@@ -9,9 +9,9 @@ obs, info = env.reset(seed=seed); ap.reset(obs, info)
    9      9  r = obs.get_object_from_name('robot')
   10     10  for t in range(env.max_steps):
   11     11      a = ap.get_action(obs)
   12        -    ph=ap.phase
          12 +    ph=ap.leg
   13     13      obs, rew, te, tr, _ = env.step(a)
   14     14      if t%every==0 or te:
   15        -        print(t, ph, ap.target, np.round(a,3), [round(float(obs.get(r,f)),3) for f in ['x','y','theta','arm_joint','vacuum']])
          15 +        print(t, ph, np.round(a,3), [round(float(obs.get(r,f)),3) for f in ['x','y','theta','arm_joint','vacuum']])
   16     16      if te: print("DONE", t+1); break
   17     17  env.close()
diff --git a/test_approach.py b/test_approach.py
index c855e24..f575ff3 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -14,7 +14,7 @@ def run(seed, verbose=False):
   14     14          obs, r, te, tr, _ = env.step(a)
   15     15          if te or tr: break
   16     16      env.close()
   17        -    return te, t_+1, info.get('object_count'), ap.phase
          17 +    return te, t_+1, info.get('object_count'), getattr(ap,'leg',None)
   18     18  if __name__ == "__main__":
   19     19      if len(sys.argv)>3: OC=int(sys.argv[3])
   20     20      seeds = range(int(sys.argv[1]), int(sys.argv[2]))
```

</details>

<a id="C006"></a>
### C006 · consistent drop feasibility, circular base approx

Commit `46e7fc6d23d059f45e7d435ff31b7c4ffdbfc95d`; parents: 1599f2acb4e64550e1bb359f49880d876e8ce0c0. Recorded author date: 2026-09-30T11:46:19+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0288](01_timeline.md#E0288): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_46e7fc6_approach.py) · [Exact all-file diff](evidence/diffs/C006_46e7fc6.diff)

[Previous saved controller snapshot](evidence/versions/C005_1599f2a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8a08531..f574aae 100644
--- a/approach.py
+++ b/approach.py
@@ -66,8 +66,13 @@ class GeneratedApproach:
   66     66      def _assembly(self, held_rel=None):
   67     67          """Boxes (x0, x1, bottom_offset) relative to robot position."""
   68     68          gh = self.gh / 2.0
   69        -        boxes = [(-self.base_r, self.base_r, -self.base_r),
   70        -                 (-gh, gh, -(self.arm + self.gw))]
          69 +        rb = self.base_r
          70 +        boxes = [(-gh, gh, -(self.arm + self.gw))]
          71 +        edges = np.linspace(0.0, rb, 6)
          72 +        for a, b in zip(edges[:-1], edges[1:]):
          73 +            off = -np.sqrt(max(rb * rb - a * a, 0.0))
          74 +            boxes.append((a, b, off))
          75 +            boxes.append((-b, -a, off))
   71     76          if held_rel is not None:
   72     77              boxes.append(held_rel)
   73     78          return boxes
@@ -139,6 +144,22 @@ class GeneratedApproach:
  139    144          opts = [c] + list(np.linspace(lo, hi, 9))
  140    145          return sorted(set(float(v) for v in opts), key=lambda v: abs(v - c))
  141    146  
         147 +    def _place_any(self, br, d, lefts, obstacles):
         148 +        """Is there any feasible final placement given obstacles?"""
         149 +        bw = br[1] - br[0]
         150 +        held = self._held_rel(br, d)
         151 +        ok = np.ones(len(lefts), dtype=bool)
         152 +        for q in obstacles:
         153 +            ok &= ~((lefts + bw > q[0] - 0.003) & (lefts < q[1] + 0.003))
         154 +        X = lefts - held[0]
         155 +        ty = PLACE_BOT - held[2]
         156 +        ok &= (X >= XMIN) & (X <= XMAX)
         157 +        if ty > YMAX:
         158 +            return False
         159 +        req = self._safe(X, self._assembly(held), obstacles)
         160 +        ok &= req <= ty + 1e-6
         161 +        return bool(ok.any())
         162 +
  142    163      def _held_rel(self, r, d):
  143    164          rx, ry = self._pick_pose(r, d)
  144    165          return (r[0] - rx, r[1] - rx, r[2] - ry)
@@ -178,7 +199,8 @@ class GeneratedApproach:
  178    199          lefts = np.arange(sx0 + e, sx1 - bw - e + 1e-9, 0.004)
  179    200          if len(lefts) == 0:
  180    201              lefts = np.array([(sx0 + sx1) / 2 - bw / 2])
  181        -        for n in R:
         202 +        for i, n in enumerate(R):
         203 +            pending = set(R[i + 1:])
  182    204              r = cur[n]
  183    205              others = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [block_obs]
  184    206              dl = [v for v in self._d_options(r) if self._pick_ok(r, v, others)]
@@ -209,8 +231,10 @@ class GeneratedApproach:
  209    231                      continue
  210    232                  dpose = (tx, ty)
  211    233                  nob = (left, left + w, DROP_BOT + h)
  212        -                obs_after = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [nob]
  213        -                if not any(self._pick_ok(br, v, obs_after) for v in bd_opts[:5]):
         234 +                obs_after = [(q[0], q[1], q[3]) for m, q in cur.items()
         235 +                             if m != n and m not in pending] + [nob]
         236 +                if not any(self._pick_ok(br, v, obs_after) and
         237 +                           self._place_any(br, v, lefts, obs_after) for v in bd_opts):
  214    238                      continue
  215    239                  c2 = self._leg_cost(pick, dpose, boxes_h, others)
  216    240                  c3 = abs(tx - (br[0] + br[1]) / 2) / STEP
@@ -218,6 +242,7 @@ class GeneratedApproach:
  218    242                  if bestd is None or sc < bestd[0]:
  219    243                      bestd = (sc, dpose, left, c2)
  220    244              if bestd is None:
         245 +                self._why = ("nodrop", n)
  221    246                  return None
  222    247              _, dpose, left, c2 = bestd
  223    248              cost += c1 + c2
@@ -251,6 +276,7 @@ class GeneratedApproach:
  251    276                  if bestp is None or sc < bestp[0]:
  252    277                      bestp = (sc, float(d), pick, (tx, ty))
  253    278          if bestp is None:
         279 +            self._why = ("noplace",)
  254    280              return None
  255    281          sc, d, pick, ppose = bestp
  256    282          cost += sc
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..c242e95
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,17 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach as A
           4 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
           5 +ap=A.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           6 +robot, block, surface, obst = ap._parse(obs)
           7 +sr=A._rect(obs,surface); br=A._rect(obs,block)
           8 +orects={o.name:A._rect(obs,o) for o in obst}
           9 +print("surf",sr[:2],"block",br)
          10 +orig=ap._place_any
          11 +def pa(br_,d,lefts,obstacles):
          12 +    r=orig(br_,d,lefts,obstacles); print("place_any d",d,"obst",np.round(obstacles,3).tolist(),"->",r); return r
          13 +ap._place_any=pa
          14 +start=(A._g(obs,robot,'x'),A._g(obs,robot,'y'))
          15 +R=tuple(sys.argv[2].split(','))
          16 +print(ap._plan_subset(start,R,orects,br,(sr[0],sr[1]),ap._assembly()), ap._why)
          17 +env.close()
diff --git a/dbgplan.py b/dbgplan.py
new file mode 100644
index 0000000..acbd99f
--- /dev/null
+++ b/dbgplan.py
@@ -0,0 +1,22 @@
           1 +import sys, itertools
           2 +from env_client import make_env
           3 +import approach as A
           4 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
           5 +ap=A.GeneratedApproach(env.action_space, env.observation_space, {})
           6 +ap.reset(obs, info)
           7 +print("legs", ap.legs)
           8 +robot, block, surface, obst = ap._parse(obs)
           9 +sr=A._rect(obs,surface); br=A._rect(obs,block)
          10 +orects={o.name:A._rect(obs,o) for o in obst}
          11 +start=(A._g(obs,robot,'x'),A._g(obs,robot,'y'))
          12 +for k in range(len(orects)+1):
          13 +    for R in itertools.permutations(orects,k):
          14 +        print(R, ap._plan_subset(start,R,orects,br,(sr[0],sr[1]),ap._assembly()), getattr(ap,"_why",None))
          15 +env.close()
          16 +# instrument
          17 +import numpy as np
          18 +R=('obstruction0','obstruction1')
          19 +n='obstruction0'; r=orects[n]
          20 +others=[(q[0],q[1],q[3]) for m,q in orects.items() if m!=n]+[(br[0],br[1],br[3])]
          21 +print("dopts", ap._d_options(r), [ap._pick_ok(r,v,others) for v in ap._d_options(r)])
          22 +print("block dopts", [ap._pick_ok(br,v,[(q[0],q[1],q[3]) for q in orects.values()]) for v in ap._d_options(br)])
```

</details>

<a id="C007"></a>
### C007 · check drop pose feasibility

Commit `6cc748506989de85a8d08ac688dcf4e5a8727ffe`; parents: 46e7fc6d23d059f45e7d435ff31b7c4ffdbfc95d. Recorded author date: 2026-09-30T11:53:10+02:00.

File roles (automatic): policy.

- [E0302](01_timeline.md#E0302): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_6cc7485_approach.py) · [Exact all-file diff](evidence/diffs/C007_6cc7485.diff)

[Previous saved controller snapshot](evidence/versions/C006_46e7fc6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f574aae..cc4a540 100644
--- a/approach.py
+++ b/approach.py
@@ -230,6 +230,8 @@ class GeneratedApproach:
  230    230                  if ty > YMAX:
  231    231                      continue
  232    232                  dpose = (tx, ty)
         233 +                if float(self._safe(np.array([tx]), boxes_h, others)[0]) > ty + 1e-6:
         234 +                    continue
  233    235                  nob = (left, left + w, DROP_BOT + h)
  234    236                  obs_after = [(q[0], q[1], q[3]) for m, q in cur.items()
  235    237                               if m != n and m not in pending] + [nob]
```

</details>

<a id="C008"></a>
### C008 · stuck recovery via replanning; robust test harness

Commit `b19eb46b9e5c0724cec804ed0ff37f6752430359`; parents: 6cc748506989de85a8d08ac688dcf4e5a8727ffe. Recorded author date: 2026-09-30T12:18:47+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0391](01_timeline.md#E0391): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_b19eb46_approach.py) · [Exact all-file diff](evidence/diffs/C008_b19eb46.diff)

[Previous saved controller snapshot](evidence/versions/C007_6cc7485_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cc4a540..fe0b8aa 100644
--- a/approach.py
+++ b/approach.py
@@ -110,6 +110,9 @@ class GeneratedApproach:
  110    110          self.leg = 0
  111    111          self.last = None
  112    112          self.stuck = 0
         113 +        self.noprog = 0
         114 +        self.replan = False
         115 +        self.replans = 0
  113    116          try:
  114    117              self.legs = self._plan(state)
  115    118          except Exception:
@@ -321,10 +324,36 @@ class GeneratedApproach:
  321    324              else:
  322    325                  self.stuck = 0
  323    326  
         327 +        if self.last is not None and abs(self.last[0] - rx) < 1e-6 and abs(self.last[1] - ry) < 1e-6:
         328 +            self.noprog += 1
         329 +        else:
         330 +            self.noprog = 0
         331 +
         332 +        if self.replan and vac < 0.5:
         333 +            self.replan = False
         334 +            self.replans += 1
         335 +            try:
         336 +                legs = self._plan(state)
         337 +            except Exception:
         338 +                legs = None
         339 +            self.legs = legs if legs else self._fallback_plan(state)
         340 +            self.leg = 0
         341 +            self.noprog = 0
         342 +
  324    343          if self.leg >= len(self.legs):
  325    344              self.last = None
  326    345              return self._act(0, 0.0, dth, darm, vac)
  327    346  
         347 +        if self.noprog >= 6 and self.replans < 5:
         348 +            kind = self.legs[self.leg][0]
         349 +            self.noprog = 0
         350 +            self.replan = True
         351 +            self.last = (rx, ry, 0.0, 0.0)
         352 +            if kind == "drop":
         353 +                return self._act(0, 0, dth, darm, 0.0)
         354 +            if kind == "pick":
         355 +                return self._act(0, 0, dth, darm, 0.0)
         356 +
  328    357          leg = self.legs[self.leg]
  329    358          kind, name = leg[0], leg[1]
  330    359          allr = {o.name: _rect(state, o) for o in obst + [block]}
diff --git a/res_100_300.txt b/res_100_300.txt
new file mode 100644
index 0000000..7d5a37d
--- /dev/null
+++ b/res_100_300.txt
@@ -0,0 +1 @@
           1 +solved 200/200  mean steps 31.6 max time 49.2s
diff --git a/test_approach.py b/test_approach.py
index f575ff3..1d45dff 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -3,26 +3,35 @@ import numpy as np
    3      3  from env_client import make_env
    4      4  from approach import GeneratedApproach
    5      5  OC=None
    6        -def run(seed, verbose=False):
           6 +def run_once(seed):
    7      7      env = make_env()
    8        -    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    9        -    obs, info = env.reset(seed=seed, options={'object_count':OC} if OC is not None else None)
   10        -    ap.reset(obs, info)
   11        -    t=time.time()
   12        -    for t_ in range(env.max_steps):
   13        -        a = ap.get_action(obs)
   14        -        obs, r, te, tr, _ = env.step(a)
   15        -        if te or tr: break
   16        -    env.close()
   17        -    return te, t_+1, info.get('object_count'), getattr(ap,'leg',None)
           8 +    try:
           9 +        ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +        obs, info = env.reset(seed=seed, options={'object_count':OC} if OC is not None else None)
          11 +        t0=time.time(); ap.reset(obs, info)
          12 +        te=False
          13 +        for t_ in range(env.max_steps):
          14 +            a = ap.get_action(obs)
          15 +            obs, r, te, tr, _ = env.step(a)
          16 +            if te or tr: break
          17 +        return te, t_+1, info.get('object_count'), getattr(ap,'leg',None), time.time()-t0
          18 +    finally:
          19 +        try: env.close()
          20 +        except Exception: pass
          21 +def run(seed):
          22 +    for k in range(3):
          23 +        try: return run_once(seed)
          24 +        except Exception as e:
          25 +            err=e; time.sleep(2)
          26 +    return None, 0, None, repr(err)[:80], 0
   18     27  if __name__ == "__main__":
   19     28      if len(sys.argv)>3: OC=int(sys.argv[3])
   20     29      seeds = range(int(sys.argv[1]), int(sys.argv[2]))
   21     30      from concurrent.futures import ThreadPoolExecutor
   22        -    with ThreadPoolExecutor(16) as ex:
          31 +    with ThreadPoolExecutor(6) as ex:
   23     32          res = list(ex.map(run, seeds))
   24     33      ok = 0
   25        -    for s, (te, n, c, ph) in zip(seeds, res):
   26        -        ok += te
   27        -        if not te: print("FAIL seed", s, "n_obj", c, "phase", ph)
   28        -    print(f"solved {ok}/{len(res)}  mean steps {np.mean([r[1] for r in res if r[0]]) if ok else 0:.1f}")
          34 +    for s, (te, n, c, ph, dt) in zip(seeds, res):
          35 +        ok += bool(te)
          36 +        if not te: print("FAIL seed", s, "n_obj", c, "leg", ph, flush=True)
          37 +    print(f"solved {ok}/{len(res)}  mean steps {np.mean([r[1] for r in res if r[0]]) if ok else 0:.1f} max time {max(r[4] for r in res):.1f}s")
diff --git a/timing.py b/timing.py
new file mode 100644
index 0000000..cbd0ffa
--- /dev/null
+++ b/timing.py
@@ -0,0 +1,14 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env()
           5 +for seed in range(int(sys.argv[1]), int(sys.argv[2])):
           6 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           7 +    obs, info = env.reset(seed=seed)
           8 +    t0=time.time(); ap.reset(obs, info); tr=time.time()-t0
           9 +    ta=0; tenv=0; n=0
          10 +    for _ in range(1000):
          11 +        t0=time.time(); a=ap.get_action(obs); ta+=time.time()-t0
          12 +        t0=time.time(); obs,r,te,trr,_=env.step(a); tenv+=time.time()-t0; n+=1
          13 +        if te: break
          14 +    print(seed, info['object_count'], "reset %.3f act %.3f (%.4f/step) env %.2f steps %d"%(tr,ta,ta/n,tenv,n), flush=True)
```

</details>

<a id="C009"></a>
### C009 · avoid grasp poses where vacuum could grab neighbours

Commit `41e922c079b0273549ae0b017969e9e367eabbeb`; parents: b19eb46b9e5c0724cec804ed0ff37f6752430359. Recorded author date: 2026-09-30T12:29:22+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0443](01_timeline.md#E0443): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_41e922c_approach.py) · [Exact all-file diff](evidence/diffs/C009_41e922c.diff)

[Previous saved controller snapshot](evidence/versions/C008_b19eb46_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fe0b8aa..9fa83a8 100644
--- a/approach.py
+++ b/approach.py
@@ -137,7 +137,15 @@ class GeneratedApproach:
  137    137          if not (XMIN <= px <= XMAX) or py > YMAX:
  138    138              return False
  139    139          req = float(self._safe(np.array([px]), self._assembly(), obstacles)[0])
  140        -        return req <= py + 1e-6
         140 +        if req > py + 1e-6:
         141 +            return False
         142 +        # avoid vacuuming neighbours: no other object near the gripper face
         143 +        face = py - self.arm - self.gw
         144 +        g0, g1 = px - self.gh / 2 - 0.015, px + self.gh / 2 + 0.015
         145 +        for ox0, ox1, otop in obstacles:
         146 +            if ox1 > g0 and ox0 < g1 and otop > face - 0.04:
         147 +                return False
         148 +        return True
  141    149  
  142    150      def _d_options(self, r):
  143    151          lo, hi = self._grasp_d(r)
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..c1149fd
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,20 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach as A
           4 +seed=int(sys.argv[1]); upto=int(sys.argv[2])
           5 +env=make_env(); obs,info=env.reset(seed=seed)
           6 +ap=A.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +for t in range(upto):
           8 +    obs,*_=env.step(ap.get_action(obs))
           9 +robot, block, surface, obst = ap._parse(obs)
          10 +rx,ry=A._g(obs,robot,'x'),A._g(obs,robot,'y')
          11 +print("robot",rx,ry,"leg",ap.leg, ap.legs[ap.leg])
          12 +for o in obst+[block]: print(o.name, np.round(A._rect(obs,o),4))
          13 +leg=ap.legs[ap.leg]; name=leg[1]
          14 +allr={o.name:A._rect(obs,o) for o in obst+[block]}
          15 +r=allr[name]; held=(r[0]-rx,r[1]-rx,r[2]-ry)
          16 +obstacles=[(q[0],q[1],q[3]) for n,q in allr.items() if n!=name]
          17 +boxes=ap._assembly(held)
          18 +X=np.linspace(rx-0.2,rx+0.3,11)
          19 +print("held",np.round(held,4)); print("S",np.round(ap._safe(X,boxes,obstacles),3), "X", np.round(X,3))
          20 +tx,ty=leg[2]; print("control", ap._control(rx,ry,tx,ty,boxes,obstacles))
diff --git a/legeff.py b/legeff.py
new file mode 100644
index 0000000..2600812
--- /dev/null
+++ b/legeff.py
@@ -0,0 +1,21 @@
           1 +import sys, math
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env(); tot_a=tot_i=0
           5 +for seed in range(int(sys.argv[1]), int(sys.argv[2])):
           6 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           7 +    obs, info = env.reset(seed=seed); ap.reset(obs, info)
           8 +    r=obs.get_object_from_name('robot')
           9 +    pos=(float(obs.get(r,'x')),float(obs.get(r,'y')))
          10 +    ideal=[]
          11 +    for L in ap.legs:
          12 +        t = L[3] if L[0]=='pick' else L[2]
          13 +        ideal.append(math.ceil(max(abs(t[0]-pos[0]),abs(t[1]-pos[1]))/0.05-1e-6)); pos=t
          14 +    counts=[0]*len(ap.legs)
          15 +    for _ in range(1000):
          16 +        li=min(ap.leg,len(counts)-1); a=ap.get_action(obs); counts[li]+=1
          17 +        obs,rr,te,tr,_=env.step(a)
          18 +        if te: break
          19 +    tot_a+=sum(counts); tot_i+=sum(ideal)
          20 +    print(seed, "actual", counts, "ideal", ideal, flush=True)
          21 +print("total actual", tot_a, "ideal", tot_i)
diff --git a/res_300_600.txt b/res_300_600.txt
new file mode 100644
index 0000000..689a662
--- /dev/null
+++ b/res_300_600.txt
@@ -0,0 +1,7 @@
           1 +FAIL seed 319 n_obj 2 leg 3
           2 +FAIL seed 358 n_obj 2 leg 3
           3 +FAIL seed 402 n_obj 2 leg 5
           4 +FAIL seed 507 n_obj 2 leg 5
           5 +FAIL seed 577 n_obj 1 leg 3
           6 +FAIL seed 590 n_obj 1 leg 3
           7 +solved 294/300  mean steps 31.6 max time 120.3s
```

</details>

<a id="C010"></a>
### C010 · multi-candidate plans chosen by offline controller simulation

Commit `878bb40c4339333b2b135b440fe71a0da2650273`; parents: 41e922c079b0273549ae0b017969e9e367eabbeb. Recorded author date: 2026-09-30T12:39:35+02:00.

File roles (automatic): policy, setup/other.

- [E0491](01_timeline.md#E0491): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_878bb40_approach.py) · [Exact all-file diff](evidence/diffs/C010_878bb40.diff)

[Previous saved controller snapshot](evidence/versions/C009_41e922c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9fa83a8..264b948 100644
--- a/approach.py
+++ b/approach.py
@@ -39,6 +39,9 @@ class GeneratedApproach:
   39     39          self.max_d = float(self.high[0])
   40     40          self.max_dth = float(self.high[2])
   41     41          self.max_darm = float(self.high[3])
          42 +        self.n_sim = 8
          43 +        self.k_drop = 2
          44 +        self.k_place = 2
   42     45  
   43     46      # ------------------------------------------------------------ parsing
   44     47      def _parse(self, s):
@@ -184,39 +187,61 @@ class GeneratedApproach:
  184    187          boxes0 = self._assembly()
  185    188          cand = [n for n, r in orects.items()
  186    189                  if r[1] > sr[0] - 0.1 and r[0] < sr[1] + 0.1]
  187        -        best = None
         190 +        plans = []
  188    191          for k in range(len(cand) + 1):
  189        -            if best is not None and k > 2:
         192 +            if plans and k > 2:
  190    193                  break
  191    194              for R in itertools.permutations(cand, k):
  192        -                res = self._plan_subset(start, R, orects, br, (sr[0], sr[1]), boxes0)
  193        -                if res is not None and (best is None or res[0] < best[0]):
  194        -                    best = res
  195        -        return None if best is None else best[1]
         195 +                plans += self._plan_subset(start, R, orects, br, (sr[0], sr[1]), boxes0)
         196 +        if not plans:
         197 +            return None
         198 +        plans.sort(key=lambda p: p[0])
         199 +        best = None
         200 +        for cost, legs, specs in plans[:self.n_sim]:
         201 +            steps = sum(self._sim_leg(*sp) for sp in specs)
         202 +            key = (steps, cost)
         203 +            if best is None or key < best[0]:
         204 +                best = (key, legs)
         205 +        return best[1]
         206 +
         207 +    def _sim_leg(self, p0, p1, boxes, obstacles, cap=120):
         208 +        x, y = p0
         209 +        tx, ty = p1
         210 +        for i in range(cap):
         211 +            dx, dy = self._control(x, y, tx, ty, boxes, obstacles)
         212 +            if abs(x + dx - tx) < 1e-5 and abs(y + dy - ty) < 1e-5:
         213 +                return i + 1
         214 +            if abs(dx) < 1e-9 and abs(dy) < 1e-9:
         215 +                return 2 * cap
         216 +            x += dx
         217 +            y += dy
         218 +        return 2 * cap
  196    219  
  197    220      def _plan_subset(self, start, R, orects, br, surf, boxes0):
  198    221          sx0, sx1 = surf
  199    222          bw = br[1] - br[0]
  200    223          lo, hi = self._grasp_d(br)
  201    224          if lo > hi:
  202        -            return None
  203        -        legs = []
  204        -        cost = 0.0
  205        -        pos = start
  206        -        cur = dict(orects)
         225 +            return []
  207    226          block_obs = (br[0], br[1], br[3])
  208    227          bd_opts = self._d_options(br)
  209    228          e = 0.004
  210    229          lefts = np.arange(sx0 + e, sx1 - bw - e + 1e-9, 0.004)
  211    230          if len(lefts) == 0:
  212    231              lefts = np.array([(sx0 + sx1) / 2 - bw / 2])
  213        -        for i, n in enumerate(R):
         232 +        out = []
         233 +
         234 +        def rec(i, pos, cur, legs, specs, cost):
         235 +            if i == len(R):
         236 +                self._finish(pos, cur, legs, specs, cost, br, bd_opts, lefts, boxes0, out)
         237 +                return
         238 +            n = R[i]
  214    239              pending = set(R[i + 1:])
  215    240              r = cur[n]
  216    241              others = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [block_obs]
  217    242              dl = [v for v in self._d_options(r) if self._pick_ok(r, v, others)]
  218    243              if not dl:
  219        -                return None
         244 +                return
  220    245              d = dl[0]
  221    246              pick = self._pick_pose(r, d)
  222    247              c1 = self._leg_cost(pos, pick, boxes0, others + [(r[0], r[1], r[3])])
@@ -225,14 +250,18 @@ class GeneratedApproach:
  225    250              w, h = r[1] - r[0], r[3] - r[2]
  226    251              forb = [(q[0], q[1]) for m, q in cur.items() if m != n]
  227    252              forb.append((br[0], br[1]))
  228        -            bestd = None
         253 +            if pending:
         254 +                nr = cur[R[i + 1]]
         255 +                nxt = (nr[0] + nr[1]) / 2
         256 +            else:
         257 +                nxt = (br[0] + br[1]) / 2
         258 +            opts = []
  229    259              for left in np.arange(0.003, WORLD_MAX_X - 0.003 - w, 0.01):
  230    260                  a, b = left, left + w
  231    261                  if any(b > f0 - 0.012 and a < f1 + 0.012 for f0, f1 in forb):
  232    262                      continue
  233    263                  if b > sx0 - 0.04 and a < sx1 + 0.04:
  234        -                    ok = any(b + 0.04 <= L or a - 0.04 >= L + bw for L in lefts)
  235        -                    if not ok:
         264 +                    if not any(b + 0.04 <= L or a - 0.04 >= L + bw for L in lefts):
  236    265                          continue
  237    266                  tx = left - held[0]
  238    267                  if not (XMIN <= tx <= XMAX):
@@ -240,31 +269,40 @@ class GeneratedApproach:
  240    269                  ty = DROP_BOT - held[2]
  241    270                  if ty > YMAX:
  242    271                      continue
  243        -                dpose = (tx, ty)
  244    272                  if float(self._safe(np.array([tx]), boxes_h, others)[0]) > ty + 1e-6:
  245    273                      continue
         274 +                c2 = self._leg_cost(pick, (tx, ty), boxes_h, others)
         275 +                c3 = abs(tx - nxt) / STEP
         276 +                opts.append((c2 + c3, left, (tx, ty), c2))
         277 +            opts.sort(key=lambda o: o[0])
         278 +            taken = []
         279 +            for sc, left, dpose, c2 in opts:
         280 +                if len(taken) >= self.k_drop:
         281 +                    break
         282 +                if any(abs(left - tl) < 0.05 for tl in taken):
         283 +                    continue
  246    284                  nob = (left, left + w, DROP_BOT + h)
  247    285                  obs_after = [(q[0], q[1], q[3]) for m, q in cur.items()
  248    286                               if m != n and m not in pending] + [nob]
  249    287                  if not any(self._pick_ok(br, v, obs_after) and
  250    288                             self._place_any(br, v, lefts, obs_after) for v in bd_opts):
  251    289                      continue
  252        -                c2 = self._leg_cost(pick, dpose, boxes_h, others)
  253        -                c3 = abs(tx - (br[0] + br[1]) / 2) / STEP
  254        -                sc = c2 + c3
  255        -                if bestd is None or sc < bestd[0]:
  256        -                    bestd = (sc, dpose, left, c2)
  257        -            if bestd is None:
  258        -                self._why = ("nodrop", n)
  259        -                return None
  260        -            _, dpose, left, c2 = bestd
  261        -            cost += c1 + c2
  262        -            legs.append(("pick", n, d, pick))
  263        -            legs.append(("drop", n, dpose))
  264        -            cur[n] = (left, left + w, DROP_BOT, DROP_BOT + h)
  265        -            pos = dpose
         290 +                taken.append(left)
         291 +                ncur = dict(cur)
         292 +                ncur[n] = (left, left + w, DROP_BOT, DROP_BOT + h)
         293 +                nlegs = legs + [("pick", n, d, pick), ("drop", n, dpose)]
         294 +                nspecs = specs + [(pos, pick, boxes0, others + [(r[0], r[1], r[3])]),
         295 +                                  (pick, dpose, boxes_h, others)]
         296 +                rec(i + 1, dpose, ncur, nlegs, nspecs, cost + c1 + c2)
         297 +
         298 +        rec(0, start, dict(orects), [], [], 0.0)
         299 +        return out
         300 +
         301 +    def _finish(self, pos, cur, legs, specs, cost, br, bd_opts, lefts, boxes0, out):
         302 +        bw = br[1] - br[0]
         303 +        block_obs = (br[0], br[1], br[3])
  266    304          obst_final = [(q[0], q[1], q[3]) for q in cur.values()]
  267        -        bestp = None
         305 +        cands = []
  268    306          for d in bd_opts:
  269    307              if not self._pick_ok(br, d, obst_final):
  270    308                  continue
@@ -285,17 +323,20 @@ class GeneratedApproach:
  285    323                  if req > ty + 1e-6:
  286    324                      continue
  287    325                  c2 = self._leg_cost(pick, (tx, ty), boxes_h, obst_final)
  288        -                sc = c1 + c2
  289        -                if bestp is None or sc < bestp[0]:
  290        -                    bestp = (sc, float(d), pick, (tx, ty))
  291        -        if bestp is None:
  292        -            self._why = ("noplace",)
  293        -            return None
  294        -        sc, d, pick, ppose = bestp
  295        -        cost += sc
  296        -        legs.append(("pick", self.block_name, d, pick))
  297        -        legs.append(("place", self.block_name, ppose))
  298        -        return cost, legs
         326 +                cands.append((c1 + c2, float(d), pick, (tx, ty), boxes_h))
         327 +        cands.sort(key=lambda c: c[0])
         328 +        used = []
         329 +        for sc, d, pick, ppose, boxes_h in cands:
         330 +            if len(used) >= self.k_place:
         331 +                break
         332 +            if any(abs(d - ud) < 1e-9 and abs(ppose[0] - ux) < 0.02 for ud, ux in used):
         333 +                continue
         334 +            used.append((d, ppose[0]))
         335 +            nlegs = legs + [("pick", self.block_name, d, pick),
         336 +                            ("place", self.block_name, ppose)]
         337 +            nspecs = specs + [(pos, pick, boxes0, obst_final + [block_obs]),
         338 +                              (pick, ppose, boxes_h, obst_final)]
         339 +            out.append((cost + sc, nlegs, nspecs))
  299    340  
  300    341      def _fallback_plan(self, state):
  301    342          robot, block, surface, obst = self._parse(state)
diff --git a/res_600_1000.txt b/res_600_1000.txt
new file mode 100644
index 0000000..69c4541
--- /dev/null
+++ b/res_600_1000.txt
@@ -0,0 +1 @@
           1 +solved 400/400  mean steps 34.0 max time 15.1s
```

</details>

<a id="C011"></a>
### C011 · wider candidate search (k_drop=3,k_place=3,n_sim=20)

Commit `e7045740ccbdcd8224b813f85e0b3ad236e214c4`; parents: 878bb40c4339333b2b135b440fe71a0da2650273. Recorded author date: 2026-09-30T12:39:55+02:00.

File roles (automatic): policy.

- [E0494](01_timeline.md#E0494): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_e704574_approach.py) · [Exact all-file diff](evidence/diffs/C011_e704574.diff)

[Previous saved controller snapshot](evidence/versions/C010_878bb40_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 264b948..e5dcd3c 100644
--- a/approach.py
+++ b/approach.py
@@ -39,9 +39,9 @@ class GeneratedApproach:
   39     39          self.max_d = float(self.high[0])
   40     40          self.max_dth = float(self.high[2])
   41     41          self.max_darm = float(self.high[3])
   42        -        self.n_sim = 8
   43        -        self.k_drop = 2
   44        -        self.k_place = 2
          42 +        self.n_sim = 20
          43 +        self.k_drop = 3
          44 +        self.k_place = 3
   45     45  
   46     46      # ------------------------------------------------------------ parsing
   47     47      def _parse(self, s):
```

</details>

<a id="C012"></a>
### C012 · vectorize clearance computation

Commit `c115fb949d928be57c5b481f64da1f7e46227aba`; parents: e7045740ccbdcd8224b813f85e0b3ad236e214c4. Recorded author date: 2026-09-30T12:40:30+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0557](01_timeline.md#E0557): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_c115fb9_approach.py) · [Exact all-file diff](evidence/diffs/C012_c115fb9.diff)

[Previous saved controller snapshot](evidence/versions/C011_e704574_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e5dcd3c..1d39e81 100644
--- a/approach.py
+++ b/approach.py
@@ -83,13 +83,17 @@ class GeneratedApproach:
   83     83      @staticmethod
   84     84      def _safe(X, boxes, obstacles):
   85     85          """Minimal robot y at each x in X such that boxes clear obstacles."""
   86        -        req = np.full(X.shape, -1.0)
   87        -        for bx0, bx1, boff in boxes:
   88        -            req = np.maximum(req, FLOOR_Y + MY - boff)
   89        -            for ox0, ox1, otop in obstacles:
   90        -                ov = (X + bx1 > ox0 - MX) & (X + bx0 < ox1 + MX)
   91        -                req = np.where(ov, np.maximum(req, otop + MY - boff), req)
   92        -        return req
          86 +        B = np.asarray(boxes, dtype=float)
          87 +        base = FLOOR_Y + MY - float(B[:, 2].min())
          88 +        if len(obstacles) == 0:
          89 +            return np.full(np.shape(X), base)
          90 +        O = np.asarray(obstacles, dtype=float)
          91 +        Xa = np.asarray(X, dtype=float)[:, None, None]
          92 +        ov = ((Xa + B[None, :, 1:2] > O[None, None, :, 0] - MX) &
          93 +              (Xa + B[None, :, 0:1] < O[None, None, :, 1] + MX))
          94 +        val = O[None, None, :, 2] + MY - B[None, :, 2:3]
          95 +        req = np.where(ov, val, -1.0).max(axis=(1, 2))
          96 +        return np.maximum(req, base)
   93     97  
   94     98      def _leg_cost(self, p0, p1, boxes, obstacles):
   95     99          x0, y0 = p0
diff --git a/prof.out b/prof.out
new file mode 100644
index 0000000..6d0ff4f
Binary files /dev/null and b/prof.out differ
diff --git a/prof.py b/prof.py
new file mode 100644
index 0000000..3575ac3
--- /dev/null
+++ b/prof.py
@@ -0,0 +1,7 @@
           1 +import cProfile, pstats, sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
           5 +ap=GeneratedApproach(env.action_space, env.observation_space, {})
           6 +cProfile.run('ap.reset(obs,info)','prof.out')
           7 +pstats.Stats('prof.out').sort_stats('cumtime').print_stats(12)
diff --git a/res_0_300_v3.txt b/res_0_300_v3.txt
new file mode 100644
index 0000000..e69de29
```

</details>

<a id="C013"></a>
### C013 · Controller uses arm joint as extra vertical DOF; vacuum clearance margin while carrying

Commit `6be1f9052b0c2c44ca3efe269485cf21eeb38110`; parents: c115fb949d928be57c5b481f64da1f7e46227aba. Recorded author date: 2026-09-30T12:52:49+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0608](01_timeline.md#E0608): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_6be1f90_approach.py) · [Exact all-file diff](evidence/diffs/C013_6be1f90.diff)

[Previous saved controller snapshot](evidence/versions/C012_c115fb9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1d39e81..4d87283 100644
--- a/approach.py
+++ b/approach.py
@@ -14,6 +14,7 @@ GAP = 0.006     # gripper gap to object top when grasping (grasp works <= ~0.01)
   14     14  DROP_BOT = FLOOR_Y + 0.006
   15     15  PLACE_BOT = FLOOR_Y + 0.012
   16     16  STEP = 0.05
          17 +VAC_CLR = 0.02
   17     18  
   18     19  
   19     20  def _g(s, o, f):
@@ -118,6 +119,7 @@ class GeneratedApproach:
  118    119          self.last = None
  119    120          self.stuck = 0
  120    121          self.noprog = 0
         122 +        self.last_arm = 0.0
  121    123          self.replan = False
  122    124          self.replans = 0
  123    125          try:
@@ -201,25 +203,37 @@ class GeneratedApproach:
  201    203              return None
  202    204          plans.sort(key=lambda p: p[0])
  203    205          best = None
         206 +        a0 = _g(state, robot, "arm_joint")
  204    207          for cost, legs, specs in plans[:self.n_sim]:
  205        -            steps = sum(self._sim_leg(*sp) for sp in specs)
         208 +            steps = self._sim_plan(start, a0, specs)
  206    209              key = (steps, cost)
  207    210              if best is None or key < best[0]:
  208    211                  best = (key, legs)
  209    212          return best[1]
  210    213  
  211        -    def _sim_leg(self, p0, p1, boxes, obstacles, cap=120):
  212        -        x, y = p0
  213        -        tx, ty = p1
  214        -        for i in range(cap):
  215        -            dx, dy = self._control(x, y, tx, ty, boxes, obstacles)
  216        -            if abs(x + dx - tx) < 1e-5 and abs(y + dy - ty) < 1e-5:
  217        -                return i + 1
  218        -            if abs(dx) < 1e-9 and abs(dy) < 1e-9:
  219        -                return 2 * cap
  220        -            x += dx
  221        -            y += dy
  222        -        return 2 * cap
         214 +    def _sim_plan(self, start, a0, specs, cap=120):
         215 +        x, y = start
         216 +        a = a0
         217 +        total = 0
         218 +        for p0, p1, held_y, obstacles in specs:
         219 +            held_g = None
         220 +            if held_y is not None:
         221 +                held_g = (held_y[0], held_y[1], held_y[2] + self.arm)
         222 +            G, B = self._split_boxes(held_g)
         223 +            tx, tg = p1[0], p1[1] - self.arm
         224 +            for i in range(cap):
         225 +                dx, dy, da, arrived = self._control(x, y, a, tx, tg, G, B, obstacles)
         226 +                x += dx
         227 +                y += dy
         228 +                a += da
         229 +                total += 1
         230 +                if arrived:
         231 +                    break
         232 +                if abs(dx) < 1e-9 and abs(dy) < 1e-9 and abs(da) < 1e-9:
         233 +                    return total + 10 * cap
         234 +            else:
         235 +                return total + 10 * cap
         236 +        return total
  223    237  
  224    238      def _plan_subset(self, start, R, orects, br, surf, boxes0):
  225    239          sx0, sx1 = surf
@@ -295,8 +309,8 @@ class GeneratedApproach:
  295    309                  ncur = dict(cur)
  296    310                  ncur[n] = (left, left + w, DROP_BOT, DROP_BOT + h)
  297    311                  nlegs = legs + [("pick", n, d, pick), ("drop", n, dpose)]
  298        -                nspecs = specs + [(pos, pick, boxes0, others + [(r[0], r[1], r[3])]),
  299        -                                  (pick, dpose, boxes_h, others)]
         312 +                nspecs = specs + [(pos, pick, None, others + [(r[0], r[1], r[3])]),
         313 +                                  (pick, dpose, held, others)]
  300    314                  rec(i + 1, dpose, ncur, nlegs, nspecs, cost + c1 + c2)
  301    315  
  302    316          rec(0, start, dict(orects), [], [], 0.0)
@@ -327,10 +341,10 @@ class GeneratedApproach:
  327    341                  if req > ty + 1e-6:
  328    342                      continue
  329    343                  c2 = self._leg_cost(pick, (tx, ty), boxes_h, obst_final)
  330        -                cands.append((c1 + c2, float(d), pick, (tx, ty), boxes_h))
         344 +                cands.append((c1 + c2, float(d), pick, (tx, ty), held))
  331    345          cands.sort(key=lambda c: c[0])
  332    346          used = []
  333        -        for sc, d, pick, ppose, boxes_h in cands:
         347 +        for sc, d, pick, ppose, held in cands:
  334    348              if len(used) >= self.k_place:
  335    349                  break
  336    350              if any(abs(d - ud) < 1e-9 and abs(ppose[0] - ux) < 0.02 for ud, ux in used):
@@ -338,8 +352,8 @@ class GeneratedApproach:
  338    352              used.append((d, ppose[0]))
  339    353              nlegs = legs + [("pick", self.block_name, d, pick),
  340    354                              ("place", self.block_name, ppose)]
  341        -            nspecs = specs + [(pos, pick, boxes0, obst_final + [block_obs]),
  342        -                              (pick, ppose, boxes_h, obst_final)]
         355 +            nspecs = specs + [(pos, pick, None, obst_final + [block_obs]),
         356 +                              (pick, ppose, held, obst_final)]
  343    357              out.append((cost + sc, nlegs, nspecs))
  344    358  
  345    359      def _fallback_plan(self, state):
@@ -368,7 +382,7 @@ class GeneratedApproach:
  368    382          vac = _g(state, robot, "vacuum")
  369    383          th_err = (-np.pi / 2 - rth + np.pi) % (2 * np.pi) - np.pi
  370    384          dth = float(np.clip(th_err, -self.max_dth, self.max_dth))
  371        -        darm = float(np.clip(self.arm - arm, -self.max_darm, self.max_darm))
         385 +        darm = 0.0
  372    386  
  373    387          if self.last is not None:
  374    388              lx, ly, cdx, cdy = self.last
@@ -377,7 +391,8 @@ class GeneratedApproach:
  377    391              else:
  378    392                  self.stuck = 0
  379    393  
  380        -        if self.last is not None and abs(self.last[0] - rx) < 1e-6 and abs(self.last[1] - ry) < 1e-6:
         394 +        if self.last is not None and abs(self.last[0] - rx) < 1e-6 and abs(self.last[1] - ry) < 1e-6 \
         395 +                and abs(self.last_arm - arm) < 1e-6:
  381    396              self.noprog += 1
  382    397          else:
  383    398              self.noprog = 0
@@ -402,6 +417,7 @@ class GeneratedApproach:
  402    417              self.noprog = 0
  403    418              self.replan = True
  404    419              self.last = (rx, ry, 0.0, 0.0)
         420 +            self.last_arm = arm
  405    421              if kind == "drop":
  406    422                  return self._act(0, 0, dth, darm, 0.0)
  407    423              if kind == "pick":
@@ -411,20 +427,20 @@ class GeneratedApproach:
  411    427          kind, name = leg[0], leg[1]
  412    428          allr = {o.name: _rect(state, o) for o in obst + [block]}
  413    429          holding = kind in ("drop", "place")
  414        -        held_rel = None
         430 +        held_g = None
         431 +        gref = ry - arm
  415    432          if holding:
  416    433              r = allr[name]
  417        -            held_rel = (r[0] - rx, r[1] - rx, r[2] - ry)
         434 +            held_g = (r[0] - rx, r[1] - rx, r[2] - gref)
  418    435          obstacles = [(q[0], q[1], q[3]) for n, q in allr.items()
  419    436                       if not (holding and n == name)]
  420    437          tx, ty = leg[3] if kind == "pick" else leg[2]
  421        -        boxes = self._assembly(held_rel)
         438 +        G, B = self._split_boxes(held_g)
  422    439          vcmd = 1.0 if holding else 0.0
  423    440  
  424        -        dx, dy = self._control(rx, ry, tx, ty, boxes, obstacles)
         441 +        dx, dy, darm, arrived = self._control(rx, ry, arm, tx, ty - self.arm, G, B, obstacles)
  425    442          if self.stuck >= 2:
  426        -            dx, dy = 0.0, min(STEP, YMAX - ry)
  427        -        arrived = abs(rx + dx - tx) < 1e-5 and abs(ry + dy - ty) < 1e-5
         443 +            dx, dy, darm, arrived = 0.0, min(STEP, YMAX - ry), 0.0, False
  428    444          if arrived:
  429    445              if kind == "pick":
  430    446                  vcmd = 1.0
@@ -432,33 +448,66 @@ class GeneratedApproach:
  432    448                  vcmd = 0.0
  433    449              self.leg += 1
  434    450          self.last = (rx, ry, dx, dy)
         451 +        self.last_arm = arm
  435    452          return self._act(dx, dy, dth, darm, vcmd)
  436    453  
  437        -    def _control(self, rx, ry, tx, ty, boxes, obstacles):
         454 +    def _split_boxes(self, held_g=None):
         455 +        """Gripper-attached boxes (relative to g = y - arm) and base boxes."""
         456 +        gh = self.gh / 2.0
         457 +        G = [(-gh, gh, -self.gw)]
         458 +        if held_g is not None:
         459 +            # keep the vacuum face well above other objects while carrying
         460 +            G = [(-gh, gh, -self.gw - VAC_CLR), held_g]
         461 +        rb = self.base_r
         462 +        Bx = []
         463 +        edges = np.linspace(0.0, rb, 6)
         464 +        for a0, b0 in zip(edges[:-1], edges[1:]):
         465 +            off = -np.sqrt(max(rb * rb - a0 * a0, 0.0))
         466 +            Bx.append((a0, b0, off))
         467 +            Bx.append((-b0, -a0, off))
         468 +        return G, Bx
         469 +
         470 +    def _control(self, x, y, a, tx, tg, G, B, obstacles):
         471 +        """Returns (dx, dy, darm, arrived). g = y - a is the gripper ref."""
  438    472          md = self.max_d - 1e-6
  439        -        ex, ey = tx - rx, ty - ry
  440        -        if abs(ex) <= md and abs(ey) <= md:
  441        -            req = float(self._safe(np.array([tx]), boxes, obstacles)[0])
  442        -            X = np.linspace(rx, tx, 12)
  443        -            if req <= ty + 1e-6 and float(self._safe(X, boxes, obstacles).max()) <= max(ty, ry) + 1e-6:
  444        -                return ex, ey
         473 +        mda = self.max_darm - 1e-6
         474 +        amin, amax = self.base_r, self.arm
         475 +        g = y - a
         476 +        ex = tx - x
  445    477          n = max(2, int(abs(ex) / 0.0025) + 2)
  446        -        X = np.linspace(rx, tx, n)
  447        -        S = self._safe(X, boxes, obstacles)
         478 +        X = np.linspace(x, tx, n)
         479 +        SG = self._safe(X, G, obstacles)
         480 +        SB = self._safe(X, B, obstacles)
  448    481          sgn = 1.0 if ex >= 0 else -1.0
  449    482          dxf = float(np.clip(ex, -md, md))
         483 +        lo_a, hi_a = max(amin, a - mda), min(amax, a + mda)
  450    484          for f in (1.0, 0.8, 0.6, 0.4, 0.25, 0.1, 0.0):
  451    485              dx = dxf * f
  452        -            nx = rx + dx
         486 +            nx = x + dx
  453    487              sw = (X - nx) * sgn <= 1e-9
  454        -            req_sweep = float(S[sw].max()) if sw.any() else -1.0
  455        -            req_sweep = max(req_sweep, float(self._safe(np.array([nx]), boxes, obstacles)[0]))
         488 +            px = np.array([nx])
         489 +            rg_sw = max(float(SG[sw].max()) if sw.any() else -1.0,
         490 +                        float(self._safe(px, G, obstacles)[0]))
         491 +            rb_sw = max(float(SB[sw].max()) if sw.any() else -1.0,
         492 +                        float(self._safe(px, B, obstacles)[0]))
  456    493              ahead = ~sw
  457        -            req_ahead = float((S[ahead] - 0.9 * np.abs(X[ahead] - nx)).max()) if ahead.any() else -1.0
  458        -            req = max(req_sweep, req_ahead)
  459        -            ny = ry + float(np.clip(ey, -md, md))
  460        -            ny = max(ny, req + 1e-4)
  461        -            if ny - ry > md + 1e-9 or ny > YMAX:
         494 +            if ahead.any():
         495 +                dist = 0.9 * np.abs(X[ahead] - nx)
         496 +                rg_ah = float((SG[ahead] - dist).max())
         497 +                rb_ah = float((SB[ahead] - dist).max())
         498 +            else:
         499 +                rg_ah = rb_ah = -1.0
         500 +            y_lo = max(y - md, rb_sw, rb_ah, rg_ah + amin, rg_sw + amin)
         501 +            y_hi = min(y + md, YMAX)
         502 +            if y_lo > y_hi + 1e-9:
         503 +                continue
         504 +            g_des = float(np.clip(tg, g - md - mda, g + md + mda))
         505 +            g_des = max(g_des, rg_sw)
         506 +            ny = float(np.clip(g_des + amax, y_lo, y_hi))
         507 +            ng = float(np.clip(g_des, ny - hi_a, ny - lo_a))
         508 +            if ng < rg_sw - 1e-9:
  462    509                  continue
  463        -            return dx, ny - ry
  464        -        return 0.0, max(0.0, min(md, YMAX - ry))
         510 +            arrived = abs(nx - tx) < 1e-5 and abs(ng - tg) < 1e-5
         511 +            return dx, ny - y, (ny - ng) - a, arrived
         512 +        dy = max(0.0, min(md, YMAX - y))
         513 +        return 0.0, dy, -(a - lo_a), False
diff --git a/dbg4.py b/dbg4.py
new file mode 100644
index 0000000..30769f7
--- /dev/null
+++ b/dbg4.py
@@ -0,0 +1,23 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +import approach
           5 +from approach import GeneratedApproach
           6 +seed=int(sys.argv[1]); upto=int(sys.argv[2])
           7 +env = make_env()
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +obs, info = env.reset(seed=seed); ap.reset(obs, info)
          10 +print(ap.legs)
          11 +orig=ap._control
          12 +def wrap(x,y,a,tx,tg,G,B,obs_):
          13 +    out=orig(x,y,a,tx,tg,G,B,obs_)
          14 +    if wrap.on: print("CTRL",round(x,3),round(y,3),round(a,3),"t",round(tx,3),round(tg,3),"G",np.round(G,3).tolist(),"obs",np.round(obs_,3).tolist(),"->",np.round(out[:3],3))
          15 +    return out
          16 +wrap.on=False
          17 +ap._control=wrap
          18 +for t in range(upto):
          19 +    wrap.on = t>=upto-3
          20 +    a = ap.get_action(obs)
          21 +    obs, rew, te, tr, _ = env.step(a)
          22 +    if te: break
          23 +env.close()
diff --git a/res_0_300_v3.txt b/res_0_300_v3.txt
index e69de29..3081968 100644
--- a/res_0_300_v3.txt
+++ b/res_0_300_v3.txt
@@ -0,0 +1 @@
           1 +solved 300/300  mean steps 30.7 max time 22.0s
```

</details>

<a id="C014"></a>
### C014 · wider plan search (n_sim 60, k 5)

Commit `5131e04542fbf51671b306632b6339c45c9969d3`; parents: 6be1f9052b0c2c44ca3efe269485cf21eeb38110. Recorded author date: 2026-09-30T13:09:08+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0680](01_timeline.md#E0680): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_5131e04_approach.py) · [Exact all-file diff](evidence/diffs/C014_5131e04.diff)

[Previous saved controller snapshot](evidence/versions/C013_6be1f90_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4d87283..792fff8 100644
--- a/approach.py
+++ b/approach.py
@@ -40,9 +40,9 @@ class GeneratedApproach:
   40     40          self.max_d = float(self.high[0])
   41     41          self.max_dth = float(self.high[2])
   42     42          self.max_darm = float(self.high[3])
   43        -        self.n_sim = 20
   44        -        self.k_drop = 3
   45        -        self.k_place = 3
          43 +        self.n_sim = 60
          44 +        self.k_drop = 5
          45 +        self.k_place = 5
   46     46  
   47     47      # ------------------------------------------------------------ parsing
   48     48      def _parse(self, s):
@@ -209,6 +209,7 @@ class GeneratedApproach:
  209    209              key = (steps, cost)
  210    210              if best is None or key < best[0]:
  211    211                  best = (key, legs)
         212 +        self._best_key = best[0]
  212    213          return best[1]
  213    214  
  214    215      def _sim_plan(self, start, a0, specs, cap=120):
diff --git a/cmpcfg.py b/cmpcfg.py
new file mode 100644
index 0000000..811f573
--- /dev/null
+++ b/cmpcfg.py
@@ -0,0 +1,17 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +a,b=int(sys.argv[1]),int(sys.argv[2])
           5 +cfgs=[(20,3,3),(60,5,5),(150,8,8)]
           6 +env=make_env()
           7 +tot=[0]*len(cfgs); tm=[0]*len(cfgs)
           8 +for s in range(a,b):
           9 +    obs,info=env.reset(seed=s)
          10 +    row=[]
          11 +    for i,(n,kd,kp) in enumerate(cfgs):
          12 +        ap=GeneratedApproach(env.action_space,env.observation_space,{})
          13 +        ap.n_sim,ap.k_drop,ap.k_place=n,kd,kp
          14 +        t0=time.time(); ap.reset(obs,info); dt=time.time()-t0
          15 +        k=getattr(ap,'_best_key',(0,0))[0]; tot[i]+=k; tm[i]=max(tm[i],dt); row.append((k,round(dt,1)))
          16 +    print(s,row,flush=True)
          17 +print("tot",tot,"maxt",tm)
diff --git a/res_0_300_v4.txt b/res_0_300_v4.txt
new file mode 100644
index 0000000..93e0235
--- /dev/null
+++ b/res_0_300_v4.txt
@@ -0,0 +1 @@
           1 +solved 300/300  mean steps 30.3 max time 16.4s
diff --git a/res_300_1000_v4.txt b/res_300_1000_v4.txt
new file mode 100644
index 0000000..e4d510e
--- /dev/null
+++ b/res_300_1000_v4.txt
@@ -0,0 +1 @@
           1 +solved 700/700  mean steps 30.9 max time 16.3s
```

</details>

<a id="C015"></a>
### C015 · time guard in planner

Commit `39d1e55fdc14dbe2741b48fbc1051564c640d550`; parents: 5131e04542fbf51671b306632b6339c45c9969d3. Recorded author date: 2026-09-30T13:18:08+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0701](01_timeline.md#E0701): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_39d1e55_approach.py) · [Exact all-file diff](evidence/diffs/C015_39d1e55.diff)

[Previous saved controller snapshot](evidence/versions/C014_5131e04_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 792fff8..0a1970c 100644
--- a/approach.py
+++ b/approach.py
@@ -2,6 +2,7 @@
    2      2  greedy Chebyshev (simultaneous dx/dy) controller that keeps the robot
    3      3  assembly above all obstacles via a look-ahead clearance cone."""
    4      4  import itertools
           5 +import time
    5      6  import numpy as np
    6      7  
    7      8  WORLD_MAX_X = 1.618
@@ -194,8 +195,9 @@ class GeneratedApproach:
  194    195          cand = [n for n, r in orects.items()
  195    196                  if r[1] > sr[0] - 0.1 and r[0] < sr[1] + 0.1]
  196    197          plans = []
         198 +        t0 = time.time()
  197    199          for k in range(len(cand) + 1):
  198        -            if plans and k > 2:
         200 +            if plans and (k > 2 or time.time() - t0 > 15.0):
  199    201                  break
  200    202              for R in itertools.permutations(cand, k):
  201    203                  plans += self._plan_subset(start, R, orects, br, (sr[0], sr[1]), boxes0)
@@ -205,6 +207,8 @@ class GeneratedApproach:
  205    207          best = None
  206    208          a0 = _g(state, robot, "arm_joint")
  207    209          for cost, legs, specs in plans[:self.n_sim]:
         210 +            if best is not None and time.time() - t0 > 20.0:
         211 +                break
  208    212              steps = self._sim_plan(start, a0, specs)
  209    213              key = (steps, cost)
  210    214              if best is None or key < best[0]:
diff --git a/res_0_300_v5.txt b/res_0_300_v5.txt
new file mode 100644
index 0000000..887d050
--- /dev/null
+++ b/res_0_300_v5.txt
@@ -0,0 +1 @@
           1 +solved 300/300  mean steps 30.2 max time 42.0s
diff --git a/resettime.py b/resettime.py
new file mode 100644
index 0000000..6b56648
--- /dev/null
+++ b/resettime.py
@@ -0,0 +1,10 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +a,b=int(sys.argv[1]),int(sys.argv[2])
           5 +env=make_env(); ts=[]
           6 +for s in range(a,b):
           7 +    obs,info=env.reset(seed=s)
           8 +    ap=GeneratedApproach(env.action_space,env.observation_space,{})
           9 +    t0=time.time(); ap.reset(obs,info); ts.append((time.time()-t0,s))
          10 +ts.sort(); print("max",[(round(t,2),s) for t,s in ts[-5:]],"mean",sum(t for t,_ in ts)/len(ts))
diff --git a/test_approach.py b/test_approach.py
index 1d45dff..5c8e411 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -34,4 +34,5 @@ if __name__ == "__main__":
   34     34      for s, (te, n, c, ph, dt) in zip(seeds, res):
   35     35          ok += bool(te)
   36     36          if not te: print("FAIL seed", s, "n_obj", c, "leg", ph, flush=True)
          37 +    slow=sorted([(r[4],seeds[i]) for i,r in enumerate(res)])[-3:]; print("slowest idx",slow)
   37     38      print(f"solved {ok}/{len(res)}  mean steps {np.mean([r[1] for r in res if r[0]]) if ok else 0:.1f} max time {max(r[4] for r in res):.1f}s")
```

</details>

<a id="C016"></a>
### C016 · soft deadline limits drop branching

Commit `7ab5ce61881b366b9179d5dc99fc6bbab9ab5878`; parents: 39d1e55fdc14dbe2741b48fbc1051564c640d550. Recorded author date: 2026-09-30T13:18:29+02:00.

File roles (automatic): policy.

- [E0708](01_timeline.md#E0708): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_7ab5ce6_approach.py) · [Exact all-file diff](evidence/diffs/C016_7ab5ce6.diff)

[Previous saved controller snapshot](evidence/versions/C015_39d1e55_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0a1970c..e9f7984 100644
--- a/approach.py
+++ b/approach.py
@@ -196,6 +196,7 @@ class GeneratedApproach:
  196    196                  if r[1] > sr[0] - 0.1 and r[0] < sr[1] + 0.1]
  197    197          plans = []
  198    198          t0 = time.time()
         199 +        self._soft_dl = t0 + 8.0
  199    200          for k in range(len(cand) + 1):
  200    201              if plans and (k > 2 or time.time() - t0 > 15.0):
  201    202                  break
@@ -300,7 +301,7 @@ class GeneratedApproach:
  300    301              opts.sort(key=lambda o: o[0])
  301    302              taken = []
  302    303              for sc, left, dpose, c2 in opts:
  303        -                if len(taken) >= self.k_drop:
         304 +                if len(taken) >= (self.k_drop if time.time() < self._soft_dl else 1):
  304    305                      break
  305    306                  if any(abs(left - tl) < 0.05 for tl in taken):
  306    307                      continue
```

</details>

<a id="C017"></a>
### C017 · test results for v5, tester prints slowest seeds

Commit `394a6f0b22ad3e77326d9aa878362109d91b8990`; parents: 7ab5ce61881b366b9179d5dc99fc6bbab9ab5878. Recorded author date: 2026-09-30T13:40:57+02:00.

File roles (automatic): setup/other.

- [E0772](01_timeline.md#E0772): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C017_394a6f0.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res_300_1000_v5.txt b/res_300_1000_v5.txt
new file mode 100644
index 0000000..50df6dc
--- /dev/null
+++ b/res_300_1000_v5.txt
@@ -0,0 +1,2 @@
           1 +slowest idx [(22.539711475372314, 766), (22.776632070541382, 663), (22.996455907821655, 639)]
           2 +solved 700/700  mean steps 30.8 max time 23.0s
```

</details>

