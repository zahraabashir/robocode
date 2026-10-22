# Obstruction2D · claude-opus-5-5 · replicate 42: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `c3031be` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `d7d0509` | initial approach: clear surface obstructions then place block | approach.py, dump.py, dump2.py, probe.py, probe2.py, probe3.py, test_approach.py | [E0028](01_timeline.md#E0028) |
| [C003](#C003) · `6a87dcf` | handle gripper conflicts with taller neighbors; zero motion during grasp/release | approach.py, dbg.py | [E0094](01_timeline.md#E0094) |
| [C004](#C004) · `2c18ad0` | collision-checked diagonal path planner, release during final move | approach.py, probe4.py, probe5.py | [E0129](01_timeline.md#E0129) |
| [C005](#C005) · `cfc6d45` | floor as obstacle box so endpoint-contact logic applies | approach.py | [E0146](01_timeline.md#E0146) |
| [C006](#C006) · `2a94e9e` | choose block placement on surface minimizing blockers; clearance-height pruning in path search | approach.py, dbg2.py, test_approach.py | [E0178](01_timeline.md#E0178) |
| [C007](#C007) · `e4f1922` | base-collision grasp conflicts; retry fallback | approach.py | [E0204](01_timeline.md#E0204) |
| [C008](#C008) · `1304463` | reachability-aware block placement + off-center grasp; smaller column margin | approach.py, dbg.py, dbg3.py | [E0257](01_timeline.md#E0257) |
| [C009](#C009) · `9a3cd47` | consistent block grasp offset w/ column check; carry replanning when stuck | approach.py, dbg4.py, run_many.sh, test_approach.py | [E0318](01_timeline.md#E0318) |
| [C010](#C010) · `ad61105` | allow gripper-overhang grasps to reach edge objects; evaluate multiple grasp offsets for block dest | approach.py, run_many.sh, scan.py | [E0381](01_timeline.md#E0381) |
| [C011](#C011) · `445a406` | fix robot bounds (start pose was out of assumed bounds -&gt; fallback paths) | approach.py, steps_0.txt, steps_1.txt, steps_2.txt, steps_3.txt, steps_list.py | [E0444](01_timeline.md#E0444) |
| [C012](#C012) · `4c36d8b` | arm-aware path planning (retract arm on plateaus), fix bounds check precedence | approach.py, steps2_0.txt, steps2_1.txt, steps2_2.txt, steps2_3.txt | [E0465](01_timeline.md#E0465) |
| [C013](#C013) · `1479166` | place block slightly higher within tolerance | approach.py, steps3_0.txt, steps3_1.txt, steps3_2.txt, steps3_3.txt, steps4_0.txt, steps4_1.txt, steps4_2.txt, steps4_3.txt | [E0528](01_timeline.md#E0528) |
| [C014](#C014) · `5585401` | stage block near surface when far; next_pos uses next blocker | approach.py | [E0550](01_timeline.md#E0550) |
| [C015](#C015) · `a1cd712` | fix STAGE_GAIN const | approach.py | [E0573](01_timeline.md#E0573) |
| [C016](#C016) · `b8cbba6` | STAGE_GAIN 1.0 | approach.py | [E0627](01_timeline.md#E0627) |
| [C017](#C017) · `e19f0c8` | suction depth ~0.015: widen grasp conflict; release before free moves | approach.py | [E0728](01_timeline.md#E0728) |
| [C018](#C018) · `a6e42ea` | group grasps: carry co-sucked obstructions together as union box | approach.py | [E0746](01_timeline.md#E0746) |
| [C019](#C019) · `c4cf818` | add debug/probe scripts | dbg5.py, probe_at.py, probe_suck.py | [E0918](01_timeline.md#E0918) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `c3031be7afc77b9b0d86d8d691c5bca4473aaa38`; parents: none (initial snapshot). Recorded author date: 2026-09-28T13:29:43+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_c3031be.diff)

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
index 0000000..0cea968
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "dd7adc19c865533e8650a0f0f3811d83", "observation_space": {"type": "ObjectCentric", "types": [{"name": "crv_robot", "parent": null, "features": ["x", "y", "theta", "base_radius", "arm_joint", "arm_length", "vacuum", "gripper_height", "gripper_width"]}, {"name": "kinematic2d", "parent": null, "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order"]}, {"name": "circle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "radius"]}, {"name": "double_rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height", "x1", "y1", "theta1", "width1", "height1", "z_order1", "color_r1", "color_g1", "color_b1"]}, {"name": "lobject", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "length_side1", "length_side2"]}, {"name": "rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_block", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_surface", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}]}, "action_space": {"type": "Box", "shape": [5], "low": [-0.05000000074505806, -0.05000000074505806, -0.19634954631328583, -0.10000000149011612, 0.0], "high": [0.05000000074505806, 0.05000000074505806, 0.19634954631328583, 0.10000000149011612, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · initial approach: clear surface obstructions then place block

Commit `d7d0509bdd82e1d36bcedc43587a6675a4dab81e`; parents: c3031be7afc77b9b0d86d8d691c5bca4473aaa38. Recorded author date: 2026-09-28T13:32:08+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0028](01_timeline.md#E0028): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_d7d0509_approach.py) · [Exact all-file diff](evidence/diffs/C002_d7d0509.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..0355bba
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,250 @@
           1 +"""Approach for Obstruction2DEnv: clear obstructions off the target surface,
           2 +then pick the target block and place it on the surface."""
           3 +import math
           4 +import numpy as np
           5 +
           6 +FLOOR = 0.1
           7 +X_MIN, X_MAX = 0.1005, 1.5175   # robot base x limits
           8 +Y_MAX = 0.895                   # robot base y limit
           9 +WORLD_X = 1.618
          10 +BASE_R = 0.1
          11 +GRIP_OFF = 0.205                # base center to gripper tip (arm 0.2 + half gripper width)
          12 +GAP = 0.0015
          13 +
          14 +
          15 +def _objs(state, tname):
          16 +    out = []
          17 +    for o in state.get_object_names() if False else []:
          18 +        pass
          19 +    return out
          20 +
          21 +
          22 +class GeneratedApproach:
          23 +    def __init__(self, action_space, observation_space, primitives):
          24 +        self.action_space = action_space
          25 +        self.observation_space = observation_space
          26 +        self.low = np.asarray(action_space.low, dtype=np.float32)
          27 +        self.high = np.asarray(action_space.high, dtype=np.float32)
          28 +
          29 +    # ------------------------------------------------------------------ utils
          30 +    def _parse(self, state):
          31 +        robot = None
          32 +        rects = {}
          33 +        block = surface = None
          34 +        for name in state.get_object_names():
          35 +            o = state.get_object_from_name(name) if isinstance(name, str) else name
          36 +            tn = o.type.name
          37 +            if tn == "crv_robot":
          38 +                robot = o
          39 +            elif tn == "target_block":
          40 +                block = o
          41 +            elif tn == "target_surface":
          42 +                surface = o
          43 +            elif tn == "rectangle":
          44 +                rects[o.name] = o
          45 +        g = lambda o, f: float(state.get(o, f))
          46 +        self.robot = dict(x=g(robot, "x"), y=g(robot, "y"), theta=g(robot, "theta"),
          47 +                          arm=g(robot, "arm_joint"), vac=g(robot, "vacuum"),
          48 +                          arm_max=g(robot, "arm_length"),
          49 +                          gw=g(robot, "gripper_width"), gh=g(robot, "gripper_height"),
          50 +                          r=g(robot, "base_radius"))
          51 +        def box(o):
          52 +            return dict(name=o.name, x=g(o, "x"), y=g(o, "y"), w=g(o, "width"), h=g(o, "height"))
          53 +        self.block = box(block)
          54 +        self.surface = box(surface)
          55 +        self.obst = {n: box(o) for n, o in rects.items()}
          56 +
          57 +    def _all_movable(self):
          58 +        d = dict(self.obst)
          59 +        d[self.block["name"]] = self.block
          60 +        return d
          61 +
          62 +    # --------------------------------------------------------------- planning
          63 +    def reset(self, state, info):
          64 +        self.plan = []
          65 +        self.cur = None
          66 +        self.stall = 0
          67 +        self.last_pos = None
          68 +        self.held = None
          69 +        self.grasp_offset = None
          70 +        self.fail_count = {}
          71 +        self.moved_away = set()
          72 +
          73 +    def _grip_off(self):
          74 +        return self.robot["arm_max"] + self.robot["gw"] / 2.0
          75 +
          76 +    def _max_top(self, exclude=()):
          77 +        t = FLOOR
          78 +        for n, b in self._all_movable().items():
          79 +            if n in exclude:
          80 +                continue
          81 +            t = max(t, b["y"] + b["h"])
          82 +        return t
          83 +
          84 +    def _travel_y(self, carried_h, exclude=()):
          85 +        need = self._max_top(exclude) + 0.03 + self._grip_off() + carried_h
          86 +        return min(Y_MAX, max(need, 0.0))
          87 +
          88 +    def _grasp_x(self, b, others):
          89 +        """Choose base x above object b such that base doesn't hit taller neighbors."""
          90 +        half = self.robot["gh"] / 2.0
          91 +        lo, hi = b["x"] + half + 0.003, b["x"] + b["w"] - half - 0.003
          92 +        if hi < lo:
          93 +            lo = hi = b["x"] + b["w"] / 2
          94 +        by = b["y"] + b["h"] + self._grip_off() + GAP
          95 +        c = b["x"] + b["w"] / 2
          96 +        cands = sorted(np.linspace(lo, hi, 21), key=lambda x: abs(x - c))
          97 +        R = self.robot["r"] + 0.005
          98 +        for x in cands:
          99 +            if x < X_MIN or x > X_MAX:
         100 +                continue
         101 +            ok = True
         102 +            for o in others:
         103 +                x0, x1 = o["x"], o["x"] + o["w"]
         104 +                d = 0.0 if x0 <= x <= x1 else min(abs(x - x0), abs(x - x1))
         105 +                if d >= R:
         106 +                    continue
         107 +                if o["y"] + o["h"] > by - math.sqrt(R * R - d * d):
         108 +                    ok = False
         109 +                    break
         110 +            if ok:
         111 +                return x
         112 +        return min(max(c, X_MIN), X_MAX)
         113 +
         114 +    def _free_spot(self, b, others, forbid):
         115 +        """Find x (left edge) on the floor for box b avoiding others and forbid intervals."""
         116 +        w = b["w"]
         117 +        m = 0.03
         118 +        ivs = [(o["x"] - m, o["x"] + o["w"] + m) for o in others] + forbid
         119 +        cur_c = b["x"] + w / 2
         120 +        best = None
         121 +        for c in np.arange(X_MIN, X_MAX, 0.005):
         122 +            x0 = c - w / 2
         123 +            if x0 < 0.0 or x0 + w > WORLD_X:
         124 +                continue
         125 +            if any(x0 < i1 and x0 + w > i0 for i0, i1 in ivs):
         126 +                continue
         127 +            # base clearance check wrt taller neighbours when descending
         128 +            cost = abs(c - cur_c)
         129 +            if best is None or cost < best[0]:
         130 +                best = (cost, x0)
         131 +        if best is not None:
         132 +            return best[1], FLOOR
         133 +        # fallback: stack on top of some other object far from surface
         134 +        best = None
         135 +        for o in others:
         136 +            c = o["x"] + o["w"] / 2
         137 +            if any(o["x"] < i1 and o["x"] + o["w"] > i0 for i0, i1 in forbid):
         138 +                continue
         139 +            top = o["y"] + o["h"]
         140 +            cost = top
         141 +            if best is None or cost < best[0]:
         142 +                best = (cost, c - w / 2, top)
         143 +        if best is not None:
         144 +            return best[1], best[2]
         145 +        return None
         146 +
         147 +    def _make_plan(self):
         148 +        """Create a list of waypoints: dict(x, y, vac, kind)."""
         149 +        s = self.surface
         150 +        s0, s1 = s["x"], s["x"] + s["w"]
         151 +        blockers = [b for n, b in self.obst.items()
         152 +                    if b["x"] < s1 + 0.005 and b["x"] + b["w"] > s0 - 0.005]
         153 +        if blockers:
         154 +            # nearest blocker to robot
         155 +            rx = self.robot["x"]
         156 +            tgt = min(blockers, key=lambda b: abs(b["x"] + b["w"] / 2 - rx))
         157 +            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
         158 +            forbid = [(s0 - 0.03, s1 + 0.03)]
         159 +            spot = self._free_spot(tgt, others, forbid)
         160 +            if spot is None:
         161 +                spot = (0.0, FLOOR)
         162 +            dest_x, dest_y = spot
         163 +        else:
         164 +            tgt = self.block
         165 +            others = [b for n, b in self.obst.items()]
         166 +            dest_x = s0 + (s["w"] - tgt["w"]) / 2
         167 +            dest_y = FLOOR
         168 +        self.target_name = tgt["name"]
         169 +        others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
         170 +        gx = self._grasp_x(tgt, others)
         171 +        gy = tgt["y"] + tgt["h"] + self._grip_off() + GAP
         172 +        ty_empty = max(self._travel_y(0.0), self.robot["y"] if False else 0)
         173 +        ty_empty = max(ty_empty, gy)
         174 +        plan = []
         175 +        plan.append(dict(x=self.robot["x"], y=max(self.robot["y"], ty_empty), vac=0, kind="move"))
         176 +        plan.append(dict(x=gx, y=max(self.robot["y"], ty_empty), vac=0, kind="move"))
         177 +        plan.append(dict(x=gx, y=gy, vac=0, kind="descend"))
         178 +        plan.append(dict(x=gx, y=gy, vac=1, kind="grasp"))
         179 +        off = gy - tgt["y"]  # base y minus object bottom
         180 +        ty_c = max(self._travel_y(tgt["h"] + 0.005, exclude=(tgt["name"],)), gy)
         181 +        # carried object must clear things; object bottom = base_y - off
         182 +        ty_c = min(Y_MAX, max(ty_c, self._max_top((tgt["name"],)) + 0.03 + off))
         183 +        dx = dest_x + (gx - tgt["x"])
         184 +        dx = min(max(dx, X_MIN), X_MAX)
         185 +        py = dest_y + off + 0.004
         186 +        plan.append(dict(x=gx, y=ty_c, vac=1, kind="lift"))
         187 +        plan.append(dict(x=dx, y=ty_c, vac=1, kind="carry"))
         188 +        plan.append(dict(x=dx, y=py, vac=1, kind="lower"))
         189 +        plan.append(dict(x=dx, y=py, vac=0, kind="release"))
         190 +        plan.append(dict(x=dx, y=ty_c, vac=0, kind="retreat"))
         191 +        return plan
         192 +
         193 +    # ---------------------------------------------------------------- control
         194 +    def get_action(self, state):
         195 +        self._parse(state)
         196 +        r = self.robot
         197 +        if not self.plan:
         198 +            self.plan = self._make_plan()
         199 +            self.stall = 0
         200 +        wp = self.plan[0]
         201 +        # check waypoint reached
         202 +        for _ in range(12):
         203 +            wp = self.plan[0]
         204 +            reached = abs(r["x"] - wp["x"]) < 1e-4 and abs(r["y"] - wp["y"]) < 1e-4 \
         205 +                and abs(r["arm"] - r["arm_max"]) < 1e-4
         206 +            if wp["kind"] in ("grasp", "release"):
         207 +                reached = (r["vac"] > 0.5) == (wp["vac"] > 0.5)
         208 +            if wp["kind"] == "lift" and reached:
         209 +                # verify grasp
         210 +                t = self._all_movable()[self.target_name]
         211 +                if abs((r["y"] - t["y"]) - (self.plan[0]["y"] - t["y"])) > 1e-3 or \
         212 +                        t["y"] < FLOOR + 0.01 and r["y"] > t["y"] + t["h"] + 0.3:
         213 +                    pass
         214 +            if reached:
         215 +                self.plan.pop(0)
         216 +                self.stall = 0
         217 +                if not self.plan:
         218 +                    self.plan = self._make_plan()
         219 +                continue
         220 +            break
         221 +        wp = self.plan[0]
         222 +        # stall detection
         223 +        pos = (round(r["x"], 5), round(r["y"], 5), round(r["arm"], 5))
         224 +        if self.last_pos == pos and wp["kind"] not in ("grasp", "release"):
         225 +            self.stall += 1
         226 +        else:
         227 +            self.stall = 0
         228 +        self.last_pos = pos
         229 +        if self.stall >= 2:
         230 +            if wp["kind"] in ("descend", "lower"):
         231 +                # can't go lower: accept current height
         232 +                self.plan.pop(0)
         233 +                self.stall = 0
         234 +                if wp["kind"] == "lower":
         235 +                    pass
         236 +                return self.get_action(state) if self.plan else self._act(0, 0, 0, wp["vac"])
         237 +            else:
         238 +                # try going up a bit, then replan
         239 +                self.plan = []
         240 +                self.stall = 0
         241 +                return self._act(0, 0.05, 0, wp["vac"])
         242 +        dx = wp["x"] - r["x"]
         243 +        dy = wp["y"] - r["y"]
         244 +        dth = -math.pi / 2 - r["theta"]
         245 +        darm = r["arm_max"] - r["arm"]
         246 +        return self._act(dx, dy, darm, wp["vac"], dth)
         247 +
         248 +    def _act(self, dx, dy, darm, vac, dth=0.0):
         249 +        a = np.array([dx, dy, dth, darm, float(vac)], dtype=np.float32)
         250 +        return np.clip(a, self.low, self.high).astype(np.float32)
diff --git a/dump.py b/dump.py
new file mode 100644
index 0000000..2186485
--- /dev/null
+++ b/dump.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +import sys
           3 +env = make_env()
           4 +for seed in range(int(sys.argv[1]), int(sys.argv[2])):
           5 +    obs, info = env.reset(seed=seed)
           6 +    print("seed", seed, info)
           7 +    for n in sorted(obs.get_object_names(), key=str):
           8 +        o = obs.get_object_from_name(n) if isinstance(n,str) else n
           9 +        t = o.type
          10 +        feats = env.observation_space.type_features[t] if hasattr(env.observation_space,'type_features') else None
          11 +        print(" ", o.name, t.name if hasattr(t,'name') else t, {f: round(float(obs.get(o,f)),3) for f in feats})
diff --git a/dump2.py b/dump2.py
new file mode 100644
index 0000000..ab6a549
--- /dev/null
+++ b/dump2.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +env = make_env()
           3 +import collections
           4 +cnt=collections.Counter()
           5 +for seed in range(0,60):
           6 +    obs, info = env.reset(seed=seed)
           7 +    cnt[info.get('object_count')]+=1
           8 +    r=[o for o in obs.get_objects(env.observation_space.get_type('crv_robot'))][0]
           9 +    ths=[round(float(obs.get(o,'theta')),3) for o in obs.get_objects(env.observation_space.get_type('rectangle'))]
          10 +    ys=[round(float(obs.get(o,'y')),3) for o in obs.get_objects(env.observation_space.get_type('rectangle'))]
          11 +    if any(ths) or set(ys)-{0.1,0.0} or abs(obs.get(r,'theta')+1.5708)>1e-3: print(seed, ths, ys, obs.get(r,'theta'))
          12 +print(cnt)
diff --git a/probe.py b/probe.py
new file mode 100644
index 0000000..699749d
--- /dev/null
+++ b/probe.py
@@ -0,0 +1,26 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +def R(o):
           6 +    r = o.get_objects(env.observation_space.get_type('crv_robot'))[0]
           7 +    return {f: round(float(o.get(r,f)),4) for f in ['x','y','theta','arm_joint','vacuum']}
           8 +def B(o, name='target_block'):
           9 +    b = o.get_object_from_name(name)
          10 +    return {f: round(float(o.get(b,f)),4) for f in ['x','y','theta']}
          11 +print(R(obs), B(obs))
          12 +# move right toward block center x=0.595
          13 +for i in range(20):
          14 +    a = np.array([0.05,0,0,0.1,0],dtype=np.float32)
          15 +    obs,r,t,tr,_ = env.step(a)
          16 +    print(i, R(obs), r)
          17 +# move down
          18 +for i in range(20):
          19 +    obs,r,t,tr,_ = env.step(np.array([0,-0.05,0,0,1],dtype=np.float32))
          20 +    print('down',i,R(obs),B(obs))
          21 +for i in range(6):
          22 +    obs,r,t,tr,_ = env.step(np.array([0,0.05,0,0,1],dtype=np.float32))
          23 +    print('up',i,R(obs),B(obs))
          24 +for i in range(3):
          25 +    obs,r,t,tr,_ = env.step(np.array([0,0.0,0,0,0],dtype=np.float32))
          26 +    print('rel',i,R(obs),B(obs))
diff --git a/probe2.py b/probe2.py
new file mode 100644
index 0000000..6785de3
--- /dev/null
+++ b/probe2.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +def R(o):
           6 +    r = o.get_objects(env.observation_space.get_type('crv_robot'))[0]
           7 +    return {f: round(float(o.get(r,f)),4) for f in ['x','y','theta','arm_joint','vacuum']}
           8 +def B(o, name='target_block'):
           9 +    b = o.get_object_from_name(name)
          10 +    return {f: round(float(o.get(b,f)),4) for f in ['x','y','theta']}
          11 +def step(a):
          12 +    global obs
          13 +    obs,r,t,tr,_ = env.step(np.array(a,dtype=np.float32)); return t
          14 +tx = 0.4976+0.097
          15 +while abs(R(obs)['x']-tx)>1e-4:
          16 +    step([np.clip(tx-R(obs)['x'],-.05,.05),0,0,0.1,0])
          17 +print(R(obs))
          18 +prev=None
          19 +for i in range(200):
          20 +    step([0,-0.005,0,0,0])
          21 +    if R(obs)['y']==prev: break
          22 +    prev=R(obs)['y']
          23 +print('lowest', R(obs), B(obs))
          24 +step([0,0,0,0,1]); print('vac on', R(obs), B(obs))
          25 +for i in range(5):
          26 +    step([0,0.05,0,0,1]); print('up', R(obs), B(obs))
          27 +step([0.05,0,0.1,0,1]); print('rot', R(obs), B(obs))
          28 +step([0,0,0,-0.05,1]); print('retract', R(obs), B(obs))
          29 +step([0,0,0,0,0]); print('rel', R(obs), B(obs))
          30 +step([0,0.05,0,0,0]); print('up', R(obs), B(obs))
diff --git a/probe3.py b/probe3.py
new file mode 100644
index 0000000..f36f945
--- /dev/null
+++ b/probe3.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +r = obs.get_objects(env.observation_space.get_type('crv_robot'))[0]
           6 +def g(): return [round(float(obs.get(r,f)),4) for f in ['x','y','arm_joint']]
           7 +for d,a in [('up',[0,.05,0,0,0]),('left',[-.05,0,0,0,0]),('right',[.05,0,0,0,0])]:
           8 +    for i in range(40): obs,*_ = env.step(np.array(a,dtype=np.float32))
           9 +    print(d, g())
          10 +# retract arm then go down
          11 +for i in range(3): obs,*_ = env.step(np.array([0,0,0,-.1,0],dtype=np.float32))
          12 +for i in range(40): obs,*_ = env.step(np.array([0,-.05,0,0,0],dtype=np.float32))
          13 +print('down retract', g())
          14 +print(env.max_steps)
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..48f12cf
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,27 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +def run(seed, count=None, verbose=False):
           6 +    env = make_env()
           7 +    kw = {}
           8 +    if count is not None: kw['options'] = {'object_count': count}
           9 +    obs, info = env.reset(seed=seed, **kw)
          10 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          11 +    ap.reset(obs, info)
          12 +    n_obj = info.get('object_count')
          13 +    for t in range(env.max_steps):
          14 +        a = ap.get_action(obs)
          15 +        obs, r, term, trunc, info = env.step(a)
          16 +        if term: env.close(); return True, t+1, n_obj
          17 +        if trunc: break
          18 +    env.close(); return False, env.max_steps, n_obj
          19 +if __name__ == '__main__':
          20 +    s0, s1 = int(sys.argv[1]), int(sys.argv[2])
          21 +    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
          22 +    ok = 0; steps=[]
          23 +    for s in range(s0, s1):
          24 +        succ, n, c = run(s, count)
          25 +        ok += succ; steps.append(n)
          26 +        if not succ: print('FAIL seed', s, 'count', c)
          27 +    print(f'success {ok}/{s1-s0}, mean steps {np.mean(steps):.1f}')
```

</details>

<a id="C003"></a>
### C003 · handle gripper conflicts with taller neighbors; zero motion during grasp/release

Commit `6a87dcf2773626453bf61354334fca3569cd1653`; parents: d7d0509bdd82e1d36bcedc43587a6675a4dab81e. Recorded author date: 2026-09-28T13:39:15+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0094](01_timeline.md#E0094): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_6a87dcf_approach.py) · [Exact all-file diff](evidence/diffs/C003_6a87dcf.diff)

[Previous saved controller snapshot](evidence/versions/C002_d7d0509_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0355bba..4ef9310 100644
--- a/approach.py
+++ b/approach.py
@@ -95,10 +95,21 @@ class GeneratedApproach:
   95     95          c = b["x"] + b["w"] / 2
   96     96          cands = sorted(np.linspace(lo, hi, 21), key=lambda x: abs(x - c))
   97     97          R = self.robot["r"] + 0.005
          98 +        btop = b["y"] + b["h"]
          99 +        self.grasp_conflict = None
   98    100          for x in cands:
   99    101              if x < X_MIN or x > X_MAX:
  100    102                  continue
  101    103              ok = True
         104 +            for o in others:
         105 +                if o["y"] + o["h"] > btop - 0.005 and o["x"] < x + half + 0.004 \
         106 +                        and o["x"] + o["w"] > x - half - 0.004:
         107 +                    ok = False
         108 +                    if self.grasp_conflict is None:
         109 +                        self.grasp_conflict = o
         110 +                    break
         111 +            if not ok:
         112 +                continue
  102    113              for o in others:
  103    114                  x0, x1 = o["x"], o["x"] + o["w"]
  104    115                  d = 0.0 if x0 <= x <= x1 else min(abs(x - x0), abs(x - x1))
@@ -109,7 +120,7 @@ class GeneratedApproach:
  109    120                      break
  110    121              if ok:
  111    122                  return x
  112        -        return min(max(c, X_MIN), X_MAX)
         123 +        return None
  113    124  
  114    125      def _free_spot(self, b, others, forbid):
  115    126          """Find x (left edge) on the floor for box b avoiding others and forbid intervals."""
@@ -165,9 +176,22 @@ class GeneratedApproach:
  165    176              others = [b for n, b in self.obst.items()]
  166    177              dest_x = s0 + (s["w"] - tgt["w"]) / 2
  167    178              dest_y = FLOOR
         179 +        for _ in range(10):
         180 +            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
         181 +            gx = self._grasp_x(tgt, others)
         182 +            if gx is not None or self.grasp_conflict is None:
         183 +                break
         184 +            tgt = self.grasp_conflict
         185 +            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
         186 +            forbid = [(s0 - 0.03, s1 + 0.03)]
         187 +            spot = self._free_spot(tgt, others, forbid)
         188 +            if spot is None:
         189 +                spot = (0.0, FLOOR)
         190 +            dest_x, dest_y = spot
         191 +        if gx is None:
         192 +            gx = min(max(tgt["x"] + tgt["w"] / 2, X_MIN), X_MAX)
  168    193          self.target_name = tgt["name"]
  169    194          others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
  170        -        gx = self._grasp_x(tgt, others)
  171    195          gy = tgt["y"] + tgt["h"] + self._grip_off() + GAP
  172    196          ty_empty = max(self._travel_y(0.0), self.robot["y"] if False else 0)
  173    197          ty_empty = max(ty_empty, gy)
@@ -241,6 +265,8 @@ class GeneratedApproach:
  241    265                  return self._act(0, 0.05, 0, wp["vac"])
  242    266          dx = wp["x"] - r["x"]
  243    267          dy = wp["y"] - r["y"]
         268 +        if wp["kind"] in ("grasp", "release"):
         269 +            dx = dy = 0.0
  244    270          dth = -math.pi / 2 - r["theta"]
  245    271          darm = r["arm_max"] - r["arm"]
  246    272          return self._act(dx, dy, darm, wp["vac"], dth)
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..84d9cf1
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,19 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed, count = int(sys.argv[1]), int(sys.argv[2])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed, options={'object_count': count})
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +ap.reset(obs, info)
          10 +ap._parse(obs)
          11 +print('surface', ap.surface); print('block', ap.block)
          12 +for n,b in ap.obst.items(): print(n, b)
          13 +lastkind=None
          14 +for t in range(int(sys.argv[3]) if len(sys.argv)>3 else 1000):
          15 +    a = ap.get_action(obs)
          16 +    k = (ap.target_name, ap.plan[0]['kind'] if ap.plan else None)
          17 +    if k!=lastkind: print(t, k, {kk:round(v,3) for kk,v in ap.robot.items() if kk in 'x y arm vac'.split()}, ap.plan[0] if ap.plan else None); lastkind=k
          18 +    obs, r, term, trunc, info = env.step(a)
          19 +    if term: print('done', t+1); break
```

</details>

<a id="C004"></a>
### C004 · collision-checked diagonal path planner, release during final move

Commit `2c18ad068f9545e337458b598779f3d91f430b13`; parents: 6a87dcf2773626453bf61354334fca3569cd1653. Recorded author date: 2026-09-28T13:50:23+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0129](01_timeline.md#E0129): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_2c18ad0_approach.py) · [Exact all-file diff](evidence/diffs/C004_2c18ad0.diff)

[Previous saved controller snapshot](evidence/versions/C003_6a87dcf_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4ef9310..1c11df4 100644
--- a/approach.py
+++ b/approach.py
@@ -1,5 +1,9 @@
    1      1  """Approach for Obstruction2DEnv: clear obstructions off the target surface,
    2        -then pick the target block and place it on the surface."""
           2 +then pick the target block and place it on the surface.
           3 +
           4 +Robot is kept pointing straight down (theta=-pi/2) with arm fully extended.
           5 +Motions between key poses are planned with a small collision-checked
           6 +path search (plateau paths with diagonal rise/fall)."""
    3      7  import math
    4      8  import numpy as np
    5      9  
@@ -7,16 +11,17 @@ FLOOR = 0.1
    7     11  X_MIN, X_MAX = 0.1005, 1.5175   # robot base x limits
    8     12  Y_MAX = 0.895                   # robot base y limit
    9     13  WORLD_X = 1.618
   10        -BASE_R = 0.1
   11        -GRIP_OFF = 0.205                # base center to gripper tip (arm 0.2 + half gripper width)
   12        -GAP = 0.0015
          14 +GAP = 0.0015                    # gripper gap above object when grasping
          15 +PLACE_GAP = 0.004               # object gap above floor when releasing
          16 +SPEED = 0.05
          17 +
          18 +
          19 +def _cheb(a, b):
          20 +    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
   13     21  
   14     22  
   15        -def _objs(state, tname):
   16        -    out = []
   17        -    for o in state.get_object_names() if False else []:
   18        -        pass
   19        -    return out
          23 +def _nsteps(path):
          24 +    return sum(math.ceil(_cheb(path[i], path[i + 1]) / SPEED - 1e-6) for i in range(len(path) - 1))
   20     25  
   21     26  
   22     27  class GeneratedApproach:
@@ -26,7 +31,7 @@ class GeneratedApproach:
   26     31          self.low = np.asarray(action_space.low, dtype=np.float32)
   27     32          self.high = np.asarray(action_space.high, dtype=np.float32)
   28     33  
   29        -    # ------------------------------------------------------------------ utils
          34 +    # ------------------------------------------------------------------ parse
   30     35      def _parse(self, state):
   31     36          robot = None
   32     37          rects = {}
@@ -40,7 +45,7 @@ class GeneratedApproach:
   40     45                  block = o
   41     46              elif tn == "target_surface":
   42     47                  surface = o
   43        -            elif tn == "rectangle":
          48 +            elif tn in ("rectangle",):
   44     49                  rects[o.name] = o
   45     50          g = lambda o, f: float(state.get(o, f))
   46     51          self.robot = dict(x=g(robot, "x"), y=g(robot, "y"), theta=g(robot, "theta"),
@@ -48,6 +53,7 @@ class GeneratedApproach:
   48     53                            arm_max=g(robot, "arm_length"),
   49     54                            gw=g(robot, "gripper_width"), gh=g(robot, "gripper_height"),
   50     55                            r=g(robot, "base_radius"))
          56 +
   51     57          def box(o):
   52     58              return dict(name=o.name, x=g(o, "x"), y=g(o, "y"), w=g(o, "width"), h=g(o, "height"))
   53     59          self.block = box(block)
@@ -59,34 +65,103 @@ class GeneratedApproach:
   59     65          d[self.block["name"]] = self.block
   60     66          return d
   61     67  
          68 +    def _grip_off(self):
          69 +        return self.robot["arm_max"] + self.robot["gw"] / 2.0
          70 +
          71 +    # --------------------------------------------------------- collision check
          72 +    def _collides(self, pts, obstacles, carried, margin_map, default_margin):
          73 +        """pts: (N,2) base positions. carried: (dx0, dx1, dy0, dy1) rel to base or None.
          74 +        obstacles: list of boxes. Returns True if any sample collides."""
          75 +        X = pts[:, 0]
          76 +        Y = pts[:, 1]
          77 +        r = self.robot["r"]
          78 +        half = self.robot["gh"] / 2.0
          79 +        go = self._grip_off()
          80 +        if np.any(X < X_MIN - 1e-6) or np.any(X > X_MAX + 1e-6) or np.any(Y > Y_MAX + 1e-6):
          81 +            return True
          82 +        # boxes attached to robot: gripper/arm, carried
          83 +        att = [(X - half, X + half, Y - go, Y)]
          84 +        if carried is not None:
          85 +            att.append((X + carried[0], X + carried[1], Y + carried[2], Y + carried[3]))
          86 +        # floor
          87 +        if np.any(Y - r < FLOOR + 0.002):
          88 +            return True
          89 +        for (x0, x1, y0, y1) in att:
          90 +            if np.any(y0 < FLOOR + 0.001):
          91 +                return True
          92 +        for o in obstacles:
          93 +            m = margin_map.get(o["name"], default_margin)
          94 +            ox0, ox1 = o["x"] - m, o["x"] + o["w"] + m
          95 +            oy0, oy1 = o["y"] - m, o["y"] + o["h"] + m
          96 +            # circle vs rect
          97 +            cx = np.clip(X, ox0, ox1)
          98 +            cy = np.clip(Y, oy0, oy1)
          99 +            if np.any((X - cx) ** 2 + (Y - cy) ** 2 < r * r):
         100 +                return True
         101 +            for (x0, x1, y0, y1) in att:
         102 +                if np.any((x0 < ox1) & (x1 > ox0) & (y0 < oy1) & (y1 > oy0)):
         103 +                    return True
         104 +        return False
         105 +
         106 +    def _path_free(self, path, obstacles, carried, margin_map, m):
         107 +        for i in range(len(path) - 1):
         108 +            a, b = np.array(path[i]), np.array(path[i + 1])
         109 +            L = max(np.linalg.norm(b - a), 1e-9)
         110 +            n = int(L / 0.003) + 2
         111 +            t = np.linspace(0, 1, n)[:, None]
         112 +            pts = a[None] * (1 - t) + b[None] * t
         113 +            if self._collides(pts, obstacles, carried, margin_map, m):
         114 +                return False
         115 +        return True
         116 +
         117 +    def _plan_path(self, A, B, obstacles, carried, special_margin=None):
         118 +        """Find short collision-free polyline from A to B."""
         119 +        m = 0.004
         120 +        margin_map = {}
         121 +        # obstacles in contact at endpoints get zero margin
         122 +        for o in obstacles:
         123 +            for P in (A, B):
         124 +                if self._collides(np.array([P]), [o], carried, {}, m):
         125 +                    margin_map[o["name"]] = 0.0
         126 +        if special_margin:
         127 +            margin_map.update(special_margin)
         128 +        cands = [[A, B]]
         129 +        sgn = 1.0 if B[0] >= A[0] else -1.0
         130 +        hs = np.arange(max(A[1], B[1]), Y_MAX + 1e-9, 0.01)
         131 +        hs = np.append(hs, Y_MAX)
         132 +        for h in hs:
         133 +            for k1 in (1.0, 0.5, 0.0):
         134 +                for k2 in (1.0, 0.5, 0.0):
         135 +                    x1 = A[0] + sgn * k1 * (h - A[1])
         136 +                    x2 = B[0] - sgn * k2 * (h - B[1])
         137 +                    if sgn * (x2 - x1) <= 0:
         138 +                        # triangle: find intersection point
         139 +                        continue
         140 +                    p = [A, (x1, h), (x2, h), B]
         141 +                    cands.append(p)
         142 +            # triangle via single apex
         143 +            for xv in np.linspace(A[0], B[0], 9)[1:-1]:
         144 +                cands.append([A, (xv, h), B])
         145 +        scored = sorted(((_nsteps(p), len(p), i) for i, p in enumerate(cands)))
         146 +        checked = 0
         147 +        for s, _, i in scored:
         148 +            p = cands[i]
         149 +            checked += 1
         150 +            if checked > 400:
         151 +                break
         152 +            if self._path_free(p, obstacles, carried, margin_map, m):
         153 +                return p
         154 +        # fallback: straight up, over, down
         155 +        return [A, (A[0], Y_MAX), (B[0], Y_MAX), B]
         156 +
   62    157      # --------------------------------------------------------------- planning
   63    158      def reset(self, state, info):
   64    159          self.plan = []
   65        -        self.cur = None
   66    160          self.stall = 0
   67    161          self.last_pos = None
   68        -        self.held = None
   69        -        self.grasp_offset = None
   70        -        self.fail_count = {}
   71        -        self.moved_away = set()
   72        -
   73        -    def _grip_off(self):
   74        -        return self.robot["arm_max"] + self.robot["gw"] / 2.0
   75        -
   76        -    def _max_top(self, exclude=()):
   77        -        t = FLOOR
   78        -        for n, b in self._all_movable().items():
   79        -            if n in exclude:
   80        -                continue
   81        -            t = max(t, b["y"] + b["h"])
   82        -        return t
   83        -
   84        -    def _travel_y(self, carried_h, exclude=()):
   85        -        need = self._max_top(exclude) + 0.03 + self._grip_off() + carried_h
   86        -        return min(Y_MAX, max(need, 0.0))
         162 +        self.target_name = None
   87    163  
   88    164      def _grasp_x(self, b, others):
   89        -        """Choose base x above object b such that base doesn't hit taller neighbors."""
   90    165          half = self.robot["gh"] / 2.0
   91    166          lo, hi = b["x"] + half + 0.003, b["x"] + b["w"] - half - 0.003
   92    167          if hi < lo:
@@ -122,97 +197,94 @@ class GeneratedApproach:
  122    197                  return x
  123    198          return None
  124    199  
  125        -    def _free_spot(self, b, others, forbid):
  126        -        """Find x (left edge) on the floor for box b avoiding others and forbid intervals."""
         200 +    def _free_spot(self, b, others, forbid, gx_rel, gpos, next_pos):
         201 +        """Find (left x, bottom y) for box b on floor avoiding others and forbid."""
  127    202          w = b["w"]
  128    203          m = 0.03
  129    204          ivs = [(o["x"] - m, o["x"] + o["w"] + m) for o in others] + forbid
  130        -        cur_c = b["x"] + w / 2
  131    205          best = None
  132        -        for c in np.arange(X_MIN, X_MAX, 0.005):
  133        -            x0 = c - w / 2
         206 +        off = gpos[1] - b["y"]
         207 +        for bx in np.arange(X_MIN, X_MAX, 0.005):
         208 +            x0 = bx - gx_rel
  134    209              if x0 < 0.0 or x0 + w > WORLD_X:
  135    210                  continue
  136    211              if any(x0 < i1 and x0 + w > i0 for i0, i1 in ivs):
  137    212                  continue
  138        -            # base clearance check wrt taller neighbours when descending
  139        -            cost = abs(c - cur_c)
         213 +            P = (bx, FLOOR + PLACE_GAP + off)
         214 +            cost = _cheb(gpos, P) + _cheb(P, next_pos)
  140    215              if best is None or cost < best[0]:
  141    216                  best = (cost, x0)
  142    217          if best is not None:
  143    218              return best[1], FLOOR
  144        -        # fallback: stack on top of some other object far from surface
         219 +        # fallback: stack on top of some other object away from surface
  145    220          best = None
  146    221          for o in others:
  147        -            c = o["x"] + o["w"] / 2
  148    222              if any(o["x"] < i1 and o["x"] + o["w"] > i0 for i0, i1 in forbid):
  149    223                  continue
  150    224              top = o["y"] + o["h"]
  151        -            cost = top
  152        -            if best is None or cost < best[0]:
  153        -                best = (cost, c - w / 2, top)
         225 +            x0 = o["x"] + o["w"] / 2 - w / 2
         226 +            if best is None or top < best[0]:
         227 +                best = (top, x0)
  154    228          if best is not None:
  155        -            return best[1], best[2]
         229 +            return best[1], best[0]
  156    230          return None
  157    231  
  158    232      def _make_plan(self):
  159        -        """Create a list of waypoints: dict(x, y, vac, kind)."""
         233 +        """Returns list of segments: each (waypoint list, vac, kind)."""
  160    234          s = self.surface
  161    235          s0, s1 = s["x"], s["x"] + s["w"]
         236 +        movable = self._all_movable()
  162    237          blockers = [b for n, b in self.obst.items()
  163    238                      if b["x"] < s1 + 0.005 and b["x"] + b["w"] > s0 - 0.005]
         239 +        rx, ry = self.robot["x"], self.robot["y"]
  164    240          if blockers:
  165        -            # nearest blocker to robot
  166        -            rx = self.robot["x"]
  167    241              tgt = min(blockers, key=lambda b: abs(b["x"] + b["w"] / 2 - rx))
  168        -            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
  169        -            forbid = [(s0 - 0.03, s1 + 0.03)]
  170        -            spot = self._free_spot(tgt, others, forbid)
  171        -            if spot is None:
  172        -                spot = (0.0, FLOOR)
  173        -            dest_x, dest_y = spot
  174    242          else:
  175    243              tgt = self.block
  176        -            others = [b for n, b in self.obst.items()]
  177        -            dest_x = s0 + (s["w"] - tgt["w"]) / 2
  178        -            dest_y = FLOOR
         244 +        gx = None
  179    245          for _ in range(10):
  180        -            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
         246 +            others = [b for n, b in movable.items() if n != tgt["name"]]
  181    247              gx = self._grasp_x(tgt, others)
  182    248              if gx is not None or self.grasp_conflict is None:
  183    249                  break
  184    250              tgt = self.grasp_conflict
  185        -            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
  186        -            forbid = [(s0 - 0.03, s1 + 0.03)]
  187        -            spot = self._free_spot(tgt, others, forbid)
  188        -            if spot is None:
  189        -                spot = (0.0, FLOOR)
  190        -            dest_x, dest_y = spot
  191    251          if gx is None:
  192    252              gx = min(max(tgt["x"] + tgt["w"] / 2, X_MIN), X_MAX)
         253 +        others = [b for n, b in movable.items() if n != tgt["name"]]
  193    254          self.target_name = tgt["name"]
  194        -        others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
         255 +        is_block = tgt["name"] == self.block["name"]
  195    256          gy = tgt["y"] + tgt["h"] + self._grip_off() + GAP
  196        -        ty_empty = max(self._travel_y(0.0), self.robot["y"] if False else 0)
  197        -        ty_empty = max(ty_empty, gy)
  198        -        plan = []
  199        -        plan.append(dict(x=self.robot["x"], y=max(self.robot["y"], ty_empty), vac=0, kind="move"))
  200        -        plan.append(dict(x=gx, y=max(self.robot["y"], ty_empty), vac=0, kind="move"))
  201        -        plan.append(dict(x=gx, y=gy, vac=0, kind="descend"))
  202        -        plan.append(dict(x=gx, y=gy, vac=1, kind="grasp"))
  203        -        off = gy - tgt["y"]  # base y minus object bottom
  204        -        ty_c = max(self._travel_y(tgt["h"] + 0.005, exclude=(tgt["name"],)), gy)
  205        -        # carried object must clear things; object bottom = base_y - off
  206        -        ty_c = min(Y_MAX, max(ty_c, self._max_top((tgt["name"],)) + 0.03 + off))
  207        -        dx = dest_x + (gx - tgt["x"])
  208        -        dx = min(max(dx, X_MIN), X_MAX)
  209        -        py = dest_y + off + 0.004
  210        -        plan.append(dict(x=gx, y=ty_c, vac=1, kind="lift"))
  211        -        plan.append(dict(x=dx, y=ty_c, vac=1, kind="carry"))
  212        -        plan.append(dict(x=dx, y=py, vac=1, kind="lower"))
  213        -        plan.append(dict(x=dx, y=py, vac=0, kind="release"))
  214        -        plan.append(dict(x=dx, y=ty_c, vac=0, kind="retreat"))
  215        -        return plan
         257 +        gpos = (gx, gy)
         258 +        off = gy - tgt["y"]
         259 +        gx_rel = gx - tgt["x"]
         260 +        if is_block:
         261 +            dest_x = s0 + (s["w"] - tgt["w"]) / 2
         262 +            dest_y = FLOOR + 0.012 - PLACE_GAP
         263 +        else:
         264 +            b = self.block
         265 +            bgx = b["x"] + b["w"] / 2
         266 +            next_pos = (bgx, b["y"] + b["h"] + self._grip_off() + GAP)
         267 +            forbid = [(s0 - 0.03, s1 + 0.03)]
         268 +            spot = self._free_spot(tgt, others, forbid, gx_rel, gpos, next_pos)
         269 +            if spot is None:
         270 +                spot = (tgt["x"], min(0.6, tgt["y"] + 0.3))
         271 +            dest_x, dest_y = spot
         272 +        px = min(max(dest_x + gx_rel, X_MIN), X_MAX)
         273 +        py = dest_y + off + PLACE_GAP
         274 +        # approach path (nothing carried)
         275 +        p1 = self._plan_path((rx, ry), gpos, others + [tgt], None,
         276 +                             special_margin={tgt["name"]: 0.0})
         277 +        carried = (tgt["x"] - gx, tgt["x"] + tgt["w"] - gx, tgt["y"] - gy, tgt["y"] + tgt["h"] - gy)
         278 +        p2 = self._plan_path(gpos, (px, py), others, carried)
         279 +        segs = []
         280 +        for w in p1[1:]:
         281 +            segs.append(dict(x=w[0], y=w[1], vac=0, kind="move"))
         282 +        segs.append(dict(x=gx, y=gy, vac=1, kind="grasp"))
         283 +        for w in p2[1:]:
         284 +            segs.append(dict(x=w[0], y=w[1], vac=1, kind="carry"))
         285 +        # release on the final step of the carry
         286 +        segs[-1]["release_last"] = not is_block
         287 +        return segs
  216    288  
  217    289      # ---------------------------------------------------------------- control
  218    290      def get_action(self, state):
@@ -221,20 +293,14 @@ class GeneratedApproach:
  221    293          if not self.plan:
  222    294              self.plan = self._make_plan()
  223    295              self.stall = 0
  224        -        wp = self.plan[0]
  225        -        # check waypoint reached
  226        -        for _ in range(12):
         296 +        for _ in range(20):
  227    297              wp = self.plan[0]
  228        -            reached = abs(r["x"] - wp["x"]) < 1e-4 and abs(r["y"] - wp["y"]) < 1e-4 \
  229        -                and abs(r["arm"] - r["arm_max"]) < 1e-4
  230        -            if wp["kind"] in ("grasp", "release"):
  231        -                reached = (r["vac"] > 0.5) == (wp["vac"] > 0.5)
  232        -            if wp["kind"] == "lift" and reached:
  233        -                # verify grasp
  234        -                t = self._all_movable()[self.target_name]
  235        -                if abs((r["y"] - t["y"]) - (self.plan[0]["y"] - t["y"])) > 1e-3 or \
  236        -                        t["y"] < FLOOR + 0.01 and r["y"] > t["y"] + t["h"] + 0.3:
  237        -                    pass
         298 +            if wp["kind"] == "grasp":
         299 +                reached = r["vac"] > 0.5
         300 +            else:
         301 +                reached = abs(r["x"] - wp["x"]) < 1e-4 and abs(r["y"] - wp["y"]) < 1e-4
         302 +                if wp.get("release_last"):
         303 +                    reached = reached and r["vac"] < 0.5
  238    304              if reached:
  239    305                  self.plan.pop(0)
  240    306                  self.stall = 0
@@ -243,33 +309,31 @@ class GeneratedApproach:
  243    309                  continue
  244    310              break
  245    311          wp = self.plan[0]
  246        -        # stall detection
  247        -        pos = (round(r["x"], 5), round(r["y"], 5), round(r["arm"], 5))
  248        -        if self.last_pos == pos and wp["kind"] not in ("grasp", "release"):
         312 +        pos = (round(r["x"], 5), round(r["y"], 5), round(r["arm"], 5), round(r["vac"]))
         313 +        if self.last_pos == pos:
  249    314              self.stall += 1
  250    315          else:
  251    316              self.stall = 0
  252    317          self.last_pos = pos
         318 +        dth = -math.pi / 2 - r["theta"]
         319 +        darm = r["arm_max"] - r["arm"]
         320 +        if wp["kind"] == "grasp":
         321 +            return self._act(0, 0, darm, 1, dth)
  253    322          if self.stall >= 2:
  254        -            if wp["kind"] in ("descend", "lower"):
  255        -                # can't go lower: accept current height
  256        -                self.plan.pop(0)
  257        -                self.stall = 0
  258        -                if wp["kind"] == "lower":
  259        -                    pass
  260        -                return self.get_action(state) if self.plan else self._act(0, 0, 0, wp["vac"])
  261        -            else:
  262        -                # try going up a bit, then replan
  263        -                self.plan = []
  264        -                self.stall = 0
  265        -                return self._act(0, 0.05, 0, wp["vac"])
         323 +            # stuck: nudge up and replan
         324 +            self.stall = 0
         325 +            self.plan = []
         326 +            if wp["kind"] == "carry" and wp is not None:
         327 +                return self._act(0, 0.02, 0, 1 if r["vac"] > 0.5 else 0, dth)
         328 +            return self._act(0, 0.02, 0, 0, dth)
  266    329          dx = wp["x"] - r["x"]
  267    330          dy = wp["y"] - r["y"]
  268        -        if wp["kind"] in ("grasp", "release"):
  269        -            dx = dy = 0.0
  270        -        dth = -math.pi / 2 - r["theta"]
  271        -        darm = r["arm_max"] - r["arm"]
  272        -        return self._act(dx, dy, darm, wp["vac"], dth)
         331 +        mx = max(abs(dx), abs(dy))
         332 +        sc = min(1.0, SPEED / mx) if mx > 0 else 1.0
         333 +        vac = wp["vac"]
         334 +        if wp.get("release_last") and sc >= 1.0:
         335 +            vac = 0
         336 +        return self._act(dx * sc, dy * sc, darm, vac, dth)
  273    337  
  274    338      def _act(self, dx, dy, darm, vac, dth=0.0):
  275    339          a = np.array([dx, dy, dth, darm, float(vac)], dtype=np.float32)
diff --git a/probe4.py b/probe4.py
new file mode 100644
index 0000000..e07486e
--- /dev/null
+++ b/probe4.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +r = obs.get_objects(env.observation_space.get_type('crv_robot'))[0]
           6 +b = obs.get_object_from_name('target_block')
           7 +def R(): return [round(float(obs.get(r,f)),4) for f in ['x','y','arm_joint','vacuum']]+[round(float(obs.get(b,f)),4) for f in ['x','y']]
           8 +def step(a):
           9 +    global obs
          10 +    obs,*_ = env.step(np.array(a,dtype=np.float32))
          11 +tx = 0.4976+0.097; gy = 0.1+0.159+0.205+0.0015
          12 +step([0,0,0,0.1,1])
          13 +while abs(R()[0]-tx)>1e-5 or abs(R()[1]-gy)>1e-5:
          14 +    dx=tx-R()[0]; dy=gy-R()[1]; s=min(1,0.05/max(abs(dx),abs(dy)))
          15 +    step([dx*s,dy*s,0,0,1]); print(R())
          16 +step([0,0.05,0,0,1]); print('lift', R())
          17 +# lower back and release on same step
          18 +step([0,-0.05+0.003,0,0,0]); print('lower+release', R())
          19 +step([0,0.05,0,0,0]); print('up', R())
diff --git a/probe5.py b/probe5.py
new file mode 100644
index 0000000..fdf07bf
--- /dev/null
+++ b/probe5.py
@@ -0,0 +1,21 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +r = obs.get_objects(env.observation_space.get_type('crv_robot'))[0]
           6 +b = obs.get_object_from_name('target_block')
           7 +def R(): return [round(float(obs.get(r,f)),4) for f in ['x','y','arm_joint','vacuum']]+[round(float(obs.get(b,f)),4) for f in ['x','y']]
           8 +def step(a):
           9 +    global obs
          10 +    obs,*_ = env.step(np.array(a,dtype=np.float32))
          11 +tx = 0.4976+0.097; gy = 0.1+0.159+0.205+0.0015
          12 +step([0,0,0,0.1,0])
          13 +for i in range(40):
          14 +    dx=tx-R()[0]; dy=gy-R()[1]; s=min(1,0.05/max(abs(dx),abs(dy),1e-9))
          15 +    step([dx*s,dy*s,0,0,0])
          16 +print(R())
          17 +step([0,0.05,0,0,1]); print('grasp+lift', R())
          18 +step([0,0.05,0,0,1]); print('lift', R())
          19 +step([0,0.05,0,0,1]); print('lift', R())
          20 +step([0.05,-0.05+0.003,0,0,0]); print('lower+release', R())
          21 +step([0,0.05,0,0,0]); print('up', R())
```

</details>

<a id="C005"></a>
### C005 · floor as obstacle box so endpoint-contact logic applies

Commit `cfc6d45b156cfebdc93a53d4dfcc7c90cef170ac`; parents: 2c18ad068f9545e337458b598779f3d91f430b13. Recorded author date: 2026-09-28T13:50:43+02:00.

File roles (automatic): policy.

- [E0146](01_timeline.md#E0146): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_cfc6d45_approach.py) · [Exact all-file diff](evidence/diffs/C005_cfc6d45.diff)

[Previous saved controller snapshot](evidence/versions/C004_2c18ad0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1c11df4..c75bbff 100644
--- a/approach.py
+++ b/approach.py
@@ -25,6 +25,7 @@ def _nsteps(path):
   25     25  
   26     26  
   27     27  class GeneratedApproach:
          28 +    FLOOR_BOX = dict(name="__floor__", x=-2.0, y=-2.0, w=6.0, h=2.0 + FLOOR)
   28     29      def __init__(self, action_space, observation_space, primitives):
   29     30          self.action_space = action_space
   30     31          self.observation_space = observation_space
@@ -83,13 +84,7 @@ class GeneratedApproach:
   83     84          att = [(X - half, X + half, Y - go, Y)]
   84     85          if carried is not None:
   85     86              att.append((X + carried[0], X + carried[1], Y + carried[2], Y + carried[3]))
   86        -        # floor
   87        -        if np.any(Y - r < FLOOR + 0.002):
   88        -            return True
   89        -        for (x0, x1, y0, y1) in att:
   90        -            if np.any(y0 < FLOOR + 0.001):
   91        -                return True
   92        -        for o in obstacles:
          87 +        for o in list(obstacles) + [self.FLOOR_BOX]:
   93     88              m = margin_map.get(o["name"], default_margin)
   94     89              ox0, ox1 = o["x"] - m, o["x"] + o["w"] + m
   95     90              oy0, oy1 = o["y"] - m, o["y"] + o["h"] + m
@@ -119,7 +114,7 @@ class GeneratedApproach:
  119    114          m = 0.004
  120    115          margin_map = {}
  121    116          # obstacles in contact at endpoints get zero margin
  122        -        for o in obstacles:
         117 +        for o in list(obstacles) + [self.FLOOR_BOX]:
  123    118              for P in (A, B):
  124    119                  if self._collides(np.array([P]), [o], carried, {}, m):
  125    120                      margin_map[o["name"]] = 0.0
```

</details>

<a id="C006"></a>
### C006 · choose block placement on surface minimizing blockers; clearance-height pruning in path search

Commit `2a94e9e45cd7b02d4d10b50094f0b6e038a58845`; parents: cfc6d45b156cfebdc93a53d4dfcc7c90cef170ac. Recorded author date: 2026-09-28T13:57:06+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0178](01_timeline.md#E0178): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_2a94e9e_approach.py) · [Exact all-file diff](evidence/diffs/C006_2a94e9e.diff)

[Previous saved controller snapshot](evidence/versions/C005_cfc6d45_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c75bbff..8023419 100644
--- a/approach.py
+++ b/approach.py
@@ -124,6 +124,12 @@ class GeneratedApproach:
  124    124          sgn = 1.0 if B[0] >= A[0] else -1.0
  125    125          hs = np.arange(max(A[1], B[1]), Y_MAX + 1e-9, 0.01)
  126    126          hs = np.append(hs, Y_MAX)
         127 +        h_min = Y_MAX
         128 +        for h in hs:
         129 +            if self._path_free([(A[0], h), (B[0], h)], obstacles, carried, margin_map, m):
         130 +                h_min = h
         131 +                break
         132 +        hs = hs[hs >= h_min - 1e-9]
  127    133          for h in hs:
  128    134              for k1 in (1.0, 0.5, 0.0):
  129    135                  for k2 in (1.0, 0.5, 0.0):
@@ -142,7 +148,7 @@ class GeneratedApproach:
  142    148          for s, _, i in scored:
  143    149              p = cands[i]
  144    150              checked += 1
  145        -            if checked > 400:
         151 +            if checked > 3000:
  146    152                  break
  147    153              if self._path_free(p, obstacles, carried, margin_map, m):
  148    154                  return p
@@ -155,6 +161,7 @@ class GeneratedApproach:
  155    161          self.stall = 0
  156    162          self.last_pos = None
  157    163          self.target_name = None
         164 +        self.block_dest = None
  158    165  
  159    166      def _grasp_x(self, b, others):
  160    167          half = self.robot["gh"] / 2.0
@@ -205,6 +212,8 @@ class GeneratedApproach:
  205    212                  continue
  206    213              if any(x0 < i1 and x0 + w > i0 for i0, i1 in ivs):
  207    214                  continue
         215 +            if self._column_hit(dict(b, x=x0, y=FLOOR + PLACE_GAP), extra=0.02):
         216 +                continue
  208    217              P = (bx, FLOOR + PLACE_GAP + off)
  209    218              cost = _cheb(gpos, P) + _cheb(P, next_pos)
  210    219              if best is None or cost < best[0]:
@@ -214,23 +223,59 @@ class GeneratedApproach:
  214    223          # fallback: stack on top of some other object away from surface
  215    224          best = None
  216    225          for o in others:
  217        -            if any(o["x"] < i1 and o["x"] + o["w"] > i0 for i0, i1 in forbid):
  218        -                continue
  219    226              top = o["y"] + o["h"]
  220    227              x0 = o["x"] + o["w"] / 2 - w / 2
         228 +            if self._column_hit(dict(b, x=x0, y=top + PLACE_GAP), extra=0.02):
         229 +                continue
  221    230              if best is None or top < best[0]:
  222    231                  best = (top, x0)
  223    232          if best is not None:
  224    233              return best[1], best[0]
  225    234          return None
  226    235  
         236 +    def _column_info(self, dest_x):
         237 +        b = self.block
         238 +        gx_rel = b["w"] / 2
         239 +        gy_rel = b["h"] + self._grip_off() + GAP
         240 +        bx = dest_x + gx_rel
         241 +        py = FLOOR + 0.012 + gy_rel
         242 +        pts = np.stack([np.full(40, bx), np.linspace(py, Y_MAX, 40)], axis=1)
         243 +        carried = (-gx_rel, b["w"] - gx_rel, -gy_rel, b["h"] - gy_rel)
         244 +        return pts, carried
         245 +
         246 +    def _column_hit(self, o, extra=0.0, dest_x=None):
         247 +        if dest_x is None:
         248 +            dest_x = self.block_dest
         249 +        pts, carried = self._column_info(dest_x)
         250 +        return self._collides(pts, [o], carried, {"__floor__": -1.0}, 0.01 + extra)
         251 +
         252 +    def _choose_block_dest(self):
         253 +        s = self.surface
         254 +        b = self.block
         255 +        lo = s["x"] + 0.003
         256 +        hi = s["x"] + s["w"] - b["w"] - 0.003
         257 +        center = s["x"] + (s["w"] - b["w"]) / 2
         258 +        if hi <= lo:
         259 +            return center
         260 +        best = None
         261 +        for dx in np.linspace(lo, hi, 25):
         262 +            nb = 0
         263 +            for o in self.obst.values():
         264 +                if self._column_hit(o, dest_x=dx):
         265 +                    nb += 1
         266 +            cost = nb * 100 + abs(dx - center) * 0.1
         267 +            if best is None or cost < best[0]:
         268 +                best = (cost, dx)
         269 +        return best[1]
         270 +
  227    271      def _make_plan(self):
  228    272          """Returns list of segments: each (waypoint list, vac, kind)."""
  229    273          s = self.surface
  230    274          s0, s1 = s["x"], s["x"] + s["w"]
  231    275          movable = self._all_movable()
  232        -        blockers = [b for n, b in self.obst.items()
  233        -                    if b["x"] < s1 + 0.005 and b["x"] + b["w"] > s0 - 0.005]
         276 +        if self.block_dest is None:
         277 +            self.block_dest = self._choose_block_dest()
         278 +        blockers = [o for o in self.obst.values() if self._column_hit(o)]
  234    279          rx, ry = self.robot["x"], self.robot["y"]
  235    280          if blockers:
  236    281              tgt = min(blockers, key=lambda b: abs(b["x"] + b["w"] / 2 - rx))
@@ -253,14 +298,13 @@ class GeneratedApproach:
  253    298          off = gy - tgt["y"]
  254    299          gx_rel = gx - tgt["x"]
  255    300          if is_block:
  256        -            dest_x = s0 + (s["w"] - tgt["w"]) / 2
         301 +            dest_x = self.block_dest
  257    302              dest_y = FLOOR + 0.012 - PLACE_GAP
  258    303          else:
  259    304              b = self.block
  260    305              bgx = b["x"] + b["w"] / 2
  261    306              next_pos = (bgx, b["y"] + b["h"] + self._grip_off() + GAP)
  262        -            forbid = [(s0 - 0.03, s1 + 0.03)]
  263        -            spot = self._free_spot(tgt, others, forbid, gx_rel, gpos, next_pos)
         307 +            spot = self._free_spot(tgt, others, [], gx_rel, gpos, next_pos)
  264    308              if spot is None:
  265    309                  spot = (tgt["x"], min(0.6, tgt["y"] + 0.3))
  266    310              dest_x, dest_y = spot
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..6e7b81c
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,29 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed, count, T = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed, options={'object_count': count})
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +ap.reset(obs, info)
          10 +for t in range(T):
          11 +    a = ap.get_action(obs)
          12 +    obs, r, term, trunc, info = env.step(a)
          13 +ap._parse(obs)
          14 +print('dest', ap.block_dest, 'surface', ap.surface)
          15 +for n,b in ap._all_movable().items(): print(n, {k:round(v,3) for k,v in b.items() if k!='name'}, 'hit', ap._column_hit(b))
          16 +tgt=ap.block; gx=0.8293184079229832; gy=tgt['y']+tgt['h']+ap._grip_off()+0.0015
          17 +carried = (tgt["x"] - gx, tgt["x"] + tgt["w"] - gx, tgt["y"] - gy, tgt["y"] + tgt["h"] - gy)
          18 +others=list(ap.obst.values())
          19 +B=(ap.block_dest+gx-tgt['x'], 0.112+gy-tgt['y'])
          20 +print('B', B)
          21 +for o in others+[ap.FLOOR_BOX]:
          22 +    print(o['name'], ap._collides(np.array([B]), [o], carried, {}, 0.004), ap._collides(np.array([(gx,gy)]), [o], carried, {}, 0.004))
          23 +print(ap._collides(np.array([B]), [], carried, {}, 0.004))
          24 +A=(gx,gy)
          25 +p=ap._plan_path(A,B,others,carried); print(p)
          26 +for h in [0.65,0.7,0.8]:
          27 +    path=[A,(A[0],h),(B[0],h),B]
          28 +    for i in range(3):
          29 +        print(h,i,ap._path_free(path[i:i+2],others,carried,{o['name']:0.0 for o in others+[ap.FLOOR_BOX]},0.004))
diff --git a/test_approach.py b/test_approach.py
index 48f12cf..17ddc6a 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -2,6 +2,7 @@ import sys, time
    2      2  import numpy as np
    3      3  from env_client import make_env
    4      4  from approach import GeneratedApproach
           5 +TMAX=0
    5      6  def run(seed, count=None, verbose=False):
    6      7      env = make_env()
    7      8      kw = {}
@@ -10,10 +11,12 @@ def run(seed, count=None, verbose=False):
   10     11      ap = GeneratedApproach(env.action_space, env.observation_space, {})
   11     12      ap.reset(obs, info)
   12     13      n_obj = info.get('object_count')
          14 +    global TMAX
          15 +    t0=time.time()
   13     16      for t in range(env.max_steps):
   14     17          a = ap.get_action(obs)
   15     18          obs, r, term, trunc, info = env.step(a)
   16        -        if term: env.close(); return True, t+1, n_obj
          19 +        if term: env.close(); TMAX=max(TMAX, time.time()-t0); return True, t+1, n_obj
   17     20          if trunc: break
   18     21      env.close(); return False, env.max_steps, n_obj
   19     22  if __name__ == '__main__':
@@ -24,4 +27,4 @@ if __name__ == '__main__':
   24     27          succ, n, c = run(s, count)
   25     28          ok += succ; steps.append(n)
   26     29          if not succ: print('FAIL seed', s, 'count', c)
   27        -    print(f'success {ok}/{s1-s0}, mean steps {np.mean(steps):.1f}')
          30 +    print(f'success {ok}/{s1-s0}, mean steps {np.mean(steps):.1f} max ep time {TMAX:.1f}s')
```

</details>

<a id="C007"></a>
### C007 · base-collision grasp conflicts; retry fallback

Commit `e4f1922918e18328e9ca7ad7fb2bba857c43506c`; parents: 2a94e9e45cd7b02d4d10b50094f0b6e038a58845. Recorded author date: 2026-09-28T14:01:55+02:00.

File roles (automatic): policy.

- [E0204](01_timeline.md#E0204): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_e4f1922_approach.py) · [Exact all-file diff](evidence/diffs/C007_e4f1922.diff)

[Previous saved controller snapshot](evidence/versions/C006_2a94e9e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8023419..6956765 100644
--- a/approach.py
+++ b/approach.py
@@ -162,6 +162,7 @@ class GeneratedApproach:
  162    162          self.last_pos = None
  163    163          self.target_name = None
  164    164          self.block_dest = None
         165 +        self.attempts = {}
  165    166  
  166    167      def _grasp_x(self, b, others):
  167    168          half = self.robot["gh"] / 2.0
@@ -194,6 +195,8 @@ class GeneratedApproach:
  194    195                      continue
  195    196                  if o["y"] + o["h"] > by - math.sqrt(R * R - d * d):
  196    197                      ok = False
         198 +                    if self.grasp_conflict is None:
         199 +                        self.grasp_conflict = o
  197    200                      break
  198    201              if ok:
  199    202                  return x
@@ -288,6 +291,18 @@ class GeneratedApproach:
  288    291              if gx is not None or self.grasp_conflict is None:
  289    292                  break
  290    293              tgt = self.grasp_conflict
         294 +        n_att = self.attempts.get(tgt["name"], 0)
         295 +        self.attempts[tgt["name"]] = n_att + 1
         296 +        if n_att >= 3:
         297 +            # repeated failure: move the tallest nearby object instead
         298 +            near = [o for o in movable.values() if o["name"] != tgt["name"]
         299 +                    and o["name"] != self.block["name"]
         300 +                    and abs((o["x"] + o["w"] / 2) - (tgt["x"] + tgt["w"] / 2)) < 0.3
         301 +                    and self.attempts.get(o["name"], 0) < 3]
         302 +            if near:
         303 +                tgt = max(near, key=lambda o: o["y"] + o["h"])
         304 +                others = [b for n, b in movable.items() if n != tgt["name"]]
         305 +                gx = self._grasp_x(tgt, others)
  291    306          if gx is None:
  292    307              gx = min(max(tgt["x"] + tgt["w"] / 2, X_MIN), X_MAX)
  293    308          others = [b for n, b in movable.items() if n != tgt["name"]]
```

</details>

<a id="C008"></a>
### C008 · reachability-aware block placement + off-center grasp; smaller column margin

Commit `13044631bf5f7cc5cca75b156de8ed4e3a50de14`; parents: e4f1922918e18328e9ca7ad7fb2bba857c43506c. Recorded author date: 2026-09-28T14:10:35+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0257](01_timeline.md#E0257): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_1304463_approach.py) · [Exact all-file diff](evidence/diffs/C008_1304463.diff)

[Previous saved controller snapshot](evidence/versions/C007_e4f1922_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6956765..2fec6ed 100644
--- a/approach.py
+++ b/approach.py
@@ -70,7 +70,7 @@ class GeneratedApproach:
   70     70          return self.robot["arm_max"] + self.robot["gw"] / 2.0
   71     71  
   72     72      # --------------------------------------------------------- collision check
   73        -    def _collides(self, pts, obstacles, carried, margin_map, default_margin):
          73 +    def _collides(self, pts, obstacles, carried, margin_map, default_margin, check_bounds=True):
   74     74          """pts: (N,2) base positions. carried: (dx0, dx1, dy0, dy1) rel to base or None.
   75     75          obstacles: list of boxes. Returns True if any sample collides."""
   76     76          X = pts[:, 0]
@@ -78,7 +78,7 @@ class GeneratedApproach:
   78     78          r = self.robot["r"]
   79     79          half = self.robot["gh"] / 2.0
   80     80          go = self._grip_off()
   81        -        if np.any(X < X_MIN - 1e-6) or np.any(X > X_MAX + 1e-6) or np.any(Y > Y_MAX + 1e-6):
          81 +        if check_bounds and np.any(X < X_MIN - 1e-6) or np.any(X > X_MAX + 1e-6) or np.any(Y > Y_MAX + 1e-6):
   82     82              return True
   83     83          # boxes attached to robot: gripper/arm, carried
   84     84          att = [(X - half, X + half, Y - go, Y)]
@@ -164,14 +164,22 @@ class GeneratedApproach:
  164    164          self.block_dest = None
  165    165          self.attempts = {}
  166    166  
  167        -    def _grasp_x(self, b, others):
         167 +    def _grasp_x(self, b, others, rng=None, pref=None):
  168    168          half = self.robot["gh"] / 2.0
  169        -        lo, hi = b["x"] + half + 0.003, b["x"] + b["w"] - half - 0.003
         169 +        lo, hi = b["x"] + 0.006, b["x"] + b["w"] - 0.006
         170 +        if rng is not None:
         171 +            lo, hi = max(lo, rng[0]), min(hi, rng[1])
         172 +        lo, hi = max(lo, X_MIN), min(hi, X_MAX)
  170    173          if hi < lo:
  171        -            lo = hi = b["x"] + b["w"] / 2
         174 +            lo = hi = min(max(b["x"] + b["w"] / 2, X_MIN), X_MAX)
  172    175          by = b["y"] + b["h"] + self._grip_off() + GAP
  173        -        c = b["x"] + b["w"] / 2
  174        -        cands = sorted(np.linspace(lo, hi, 21), key=lambda x: abs(x - c))
         176 +        c = b["x"] + b["w"] / 2 if pref is None else pref
         177 +        ilo, ihi = b["x"] + half + 0.003, b["x"] + b["w"] - half - 0.003
         178 +
         179 +        def key(x):
         180 +            over = 0.0 if ilo <= x <= ihi else min(abs(x - ilo), abs(x - ihi))
         181 +            return (round(over, 4) > 0, abs(x - c))
         182 +        cands = sorted(np.linspace(lo, hi, 41), key=key)
  175    183          R = self.robot["r"] + 0.005
  176    184          btop = b["y"] + b["h"]
  177    185          self.grasp_conflict = None
@@ -236,9 +244,9 @@ class GeneratedApproach:
  236    244              return best[1], best[0]
  237    245          return None
  238    246  
  239        -    def _column_info(self, dest_x):
         247 +    def _column_info(self, dest_x, grel=None):
  240    248          b = self.block
  241        -        gx_rel = b["w"] / 2
         249 +        gx_rel = self.block_grel if grel is None else grel
  242    250          gy_rel = b["h"] + self._grip_off() + GAP
  243    251          bx = dest_x + gx_rel
  244    252          py = FLOOR + 0.012 + gy_rel
@@ -246,11 +254,12 @@ class GeneratedApproach:
  246    254          carried = (-gx_rel, b["w"] - gx_rel, -gy_rel, b["h"] - gy_rel)
  247    255          return pts, carried
  248    256  
  249        -    def _column_hit(self, o, extra=0.0, dest_x=None):
         257 +    def _column_hit(self, o, extra=0.0, dest_x=None, grel=None):
  250    258          if dest_x is None:
  251    259              dest_x = self.block_dest
  252        -        pts, carried = self._column_info(dest_x)
  253        -        return self._collides(pts, [o], carried, {"__floor__": -1.0}, 0.01 + extra)
         260 +        pts, carried = self._column_info(dest_x, grel)
         261 +        return self._collides(pts, [o], carried, {"__floor__": -1.0}, 0.002 + extra,
         262 +                              check_bounds=False)
  254    263  
  255    264      def _choose_block_dest(self):
  256    265          s = self.surface
@@ -259,17 +268,25 @@ class GeneratedApproach:
  259    268          hi = s["x"] + s["w"] - b["w"] - 0.003
  260    269          center = s["x"] + (s["w"] - b["w"]) / 2
  261    270          if hi <= lo:
  262        -            return center
         271 +            lo = hi = center
  263    272          best = None
  264    273          for dx in np.linspace(lo, hi, 25):
         274 +            glo = max(0.006, X_MIN - dx)
         275 +            ghi = min(b["w"] - 0.006, X_MAX - dx)
         276 +            if ghi < glo:
         277 +                continue
         278 +            grel = min(max(b["w"] / 2, glo), ghi)
  265    279              nb = 0
  266    280              for o in self.obst.values():
  267        -                if self._column_hit(o, dest_x=dx):
  268        -                    nb += 1
         281 +                if self._column_hit(o, dest_x=dx, grel=grel):
         282 +                    reach = o["x"] + 0.006 <= X_MAX and o["x"] + o["w"] - 0.006 >= X_MIN
         283 +                    nb += 1 if reach else 100
  269    284              cost = nb * 100 + abs(dx - center) * 0.1
  270    285              if best is None or cost < best[0]:
  271        -                best = (cost, dx)
  272        -        return best[1]
         286 +                best = (cost, dx, grel)
         287 +        if best is None:
         288 +            return center, b["w"] / 2
         289 +        return best[1], best[2]
  273    290  
  274    291      def _make_plan(self):
  275    292          """Returns list of segments: each (waypoint list, vac, kind)."""
@@ -277,7 +294,7 @@ class GeneratedApproach:
  277    294          s0, s1 = s["x"], s["x"] + s["w"]
  278    295          movable = self._all_movable()
  279    296          if self.block_dest is None:
  280        -            self.block_dest = self._choose_block_dest()
         297 +            self.block_dest, self.block_grel = self._choose_block_dest()
  281    298          blockers = [o for o in self.obst.values() if self._column_hit(o)]
  282    299          rx, ry = self.robot["x"], self.robot["y"]
  283    300          if blockers:
@@ -287,7 +304,12 @@ class GeneratedApproach:
  287    304          gx = None
  288    305          for _ in range(10):
  289    306              others = [b for n, b in movable.items() if n != tgt["name"]]
  290        -            gx = self._grasp_x(tgt, others)
         307 +            if tgt["name"] == self.block["name"]:
         308 +                bb = self.block
         309 +                rng = (bb["x"] + X_MIN - self.block_dest, bb["x"] + X_MAX - self.block_dest)
         310 +                gx = self._grasp_x(tgt, others, rng=rng, pref=bb["x"] + self.block_grel)
         311 +            else:
         312 +                gx = self._grasp_x(tgt, others)
  291    313              if gx is not None or self.grasp_conflict is None:
  292    314                  break
  293    315              tgt = self.grasp_conflict
diff --git a/dbg.py b/dbg.py
index 84d9cf1..06c95dd 100644
--- a/dbg.py
+++ b/dbg.py
@@ -4,7 +4,7 @@ from env_client import make_env
    4      4  from approach import GeneratedApproach
    5      5  seed, count = int(sys.argv[1]), int(sys.argv[2])
    6      6  env = make_env()
    7        -obs, info = env.reset(seed=seed, options={'object_count': count})
           7 +obs, info = env.reset(seed=seed, options=({'object_count': count} if count>0 else None))
    8      8  ap = GeneratedApproach(env.action_space, env.observation_space, {})
    9      9  ap.reset(obs, info)
   10     10  ap._parse(obs)
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..41ec382
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,16 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +import approach as A
           6 +seed, count = int(sys.argv[1]), int(sys.argv[2])
           7 +env = make_env()
           8 +obs, info = env.reset(seed=seed, options=({'object_count': count} if count>0 else None))
           9 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +ap.reset(obs, info); ap._parse(obs)
          11 +s=ap.surface; b=ap.block
          12 +lo = s["x"] + 0.003; hi = s["x"] + s["w"] - b["w"] - 0.003
          13 +for dx in np.linspace(lo, hi, 7):
          14 +    glo = max(0.006, A.X_MIN - dx); ghi = min(b["w"] - 0.006, A.X_MAX - dx)
          15 +    grel = min(max(b["w"] / 2, glo), ghi)
          16 +    print(round(dx,4), round(grel,4), [o['name'] for o in ap.obst.values() if ap._column_hit(o, dest_x=dx, grel=grel)])
```

</details>

<a id="C009"></a>
### C009 · consistent block grasp offset w/ column check; carry replanning when stuck

Commit `9a3cd474e95d08874055277d95ba6cdf32b16f5e`; parents: 13044631bf5f7cc5cca75b156de8ed4e3a50de14. Recorded author date: 2026-09-28T14:33:05+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0318](01_timeline.md#E0318): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_9a3cd47_approach.py) · [Exact all-file diff](evidence/diffs/C009_9a3cd47.diff)

[Previous saved controller snapshot](evidence/versions/C008_1304463_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2fec6ed..4ca92f1 100644
--- a/approach.py
+++ b/approach.py
@@ -163,6 +163,8 @@ class GeneratedApproach:
  163    163          self.target_name = None
  164    164          self.block_dest = None
  165    165          self.attempts = {}
         166 +        self.carry = None
         167 +        self.stuck_carry = 0
  166    168  
  167    169      def _grasp_x(self, b, others, rng=None, pref=None):
  168    170          half = self.robot["gh"] / 2.0
@@ -271,8 +273,8 @@ class GeneratedApproach:
  271    273              lo = hi = center
  272    274          best = None
  273    275          for dx in np.linspace(lo, hi, 25):
  274        -            glo = max(0.006, X_MIN - dx)
  275        -            ghi = min(b["w"] - 0.006, X_MAX - dx)
         276 +            glo = max(0.006, X_MIN - dx, X_MIN - b["x"])
         277 +            ghi = min(b["w"] - 0.006, X_MAX - dx, X_MAX - b["x"])
  276    278              if ghi < glo:
  277    279                  continue
  278    280              grel = min(max(b["w"] / 2, glo), ghi)
@@ -297,6 +299,17 @@ class GeneratedApproach:
  297    299              self.block_dest, self.block_grel = self._choose_block_dest()
  298    300          blockers = [o for o in self.obst.values() if self._column_hit(o)]
  299    301          rx, ry = self.robot["x"], self.robot["y"]
         302 +        if not blockers:
         303 +            bb = self.block
         304 +            others = [b for n, b in movable.items() if n != bb["name"]]
         305 +            rng = (bb["x"] + X_MIN - self.block_dest, bb["x"] + X_MAX - self.block_dest)
         306 +            gxb = self._grasp_x(bb, others, rng=rng, pref=bb["x"] + self.block_grel)
         307 +            if gxb is not None and abs(gxb - bb["x"] - self.block_grel) > 1e-4:
         308 +                grel = gxb - bb["x"]
         309 +                bl2 = [o for o in self.obst.values() if self._column_hit(o, grel=grel)]
         310 +                if bl2:
         311 +                    self.block_grel = grel
         312 +                    blockers = bl2
  300    313          if blockers:
  301    314              tgt = min(blockers, key=lambda b: abs(b["x"] + b["w"] / 2 - rx))
  302    315          else:
@@ -360,6 +373,29 @@ class GeneratedApproach:
  360    373              segs.append(dict(x=w[0], y=w[1], vac=1, kind="carry"))
  361    374          # release on the final step of the carry
  362    375          segs[-1]["release_last"] = not is_block
         376 +        self.carry = dict(name=tgt["name"], px=px, py=py, release=not is_block,
         377 +                          rel=(tgt["x"] - gx, tgt["y"] - gy))
         378 +        return segs
         379 +
         380 +    def _replan_carry(self):
         381 +        """Replan carry path from current pose if still holding the object."""
         382 +        c = self.carry
         383 +        if c is None or self.robot["vac"] < 0.5:
         384 +            return None
         385 +        movable = self._all_movable()
         386 +        if c["name"] not in movable:
         387 +            return None
         388 +        o = movable[c["name"]]
         389 +        rx, ry = self.robot["x"], self.robot["y"]
         390 +        if abs(o["x"] - rx - c["rel"][0]) > 2e-3 or abs(o["y"] - ry - c["rel"][1]) > 2e-3:
         391 +            return None
         392 +        others = [b for n, b in movable.items() if n != o["name"]]
         393 +        carried = (o["x"] - rx, o["x"] + o["w"] - rx, o["y"] - ry, o["y"] + o["h"] - ry)
         394 +        p = self._plan_path((rx, ry), (c["px"], c["py"]), others, carried)
         395 +        segs = [dict(x=w[0], y=w[1], vac=1, kind="carry") for w in p[1:]]
         396 +        if not segs:
         397 +            return None
         398 +        segs[-1]["release_last"] = c["release"]
  363    399          return segs
  364    400  
  365    401      # ---------------------------------------------------------------- control
@@ -399,6 +435,13 @@ class GeneratedApproach:
  399    435              # stuck: nudge up and replan
  400    436              self.stall = 0
  401    437              self.plan = []
         438 +            if wp["kind"] == "carry":
         439 +                self.stuck_carry += 1
         440 +                if self.stuck_carry <= 4:
         441 +                    segs = self._replan_carry()
         442 +                    if segs:
         443 +                        self.plan = [dict(x=r["x"], y=min(Y_MAX, r["y"] + 0.02), vac=1,
         444 +                                          kind="carry")] + segs
  402    445              if wp["kind"] == "carry" and wp is not None:
  403    446                  return self._act(0, 0.02, 0, 1 if r["vac"] > 0.5 else 0, dth)
  404    447              return self._act(0, 0.02, 0, 0, dth)
diff --git a/dbg4.py b/dbg4.py
new file mode 100644
index 0000000..94b8c0c
--- /dev/null
+++ b/dbg4.py
@@ -0,0 +1,17 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed, count, T = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed, options={'object_count': count})
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +ap.reset(obs, info)
          10 +for t in range(T):
          11 +    a = ap.get_action(obs)
          12 +    obs, r, term, trunc, info = env.step(a)
          13 +ap._parse(obs)
          14 +print('robot', {k:round(v,3) for k,v in ap.robot.items()})
          15 +print('dest', ap.block_dest, ap.block_grel, 'surface', ap.surface)
          16 +for n,b in ap._all_movable().items(): print(n, {k:round(v,3) for k,v in b.items() if k!='name'}, 'hit', ap._column_hit(b))
          17 +print(ap.plan)
diff --git a/run_many.sh b/run_many.sh
new file mode 100755
index 0000000..6f5ae4a
--- /dev/null
+++ b/run_many.sh
@@ -0,0 +1,8 @@
           1 +#!/bin/bash
           2 +# usage: run_many.sh count start end nproc
           3 +c=$1; s=$2; e=$3; p=$4
           4 +step=$(( (e - s + p - 1) / p ))
           5 +for ((i=s; i<e; i+=step)); do
           6 +  j=$((i+step)); [ $j -gt $e ] && j=$e
           7 +  timeout 1500 /opt/robocode-strict/bin/python test_approach.py $i $j $c 2>&1 | grep -E "FAIL|success|Error" &
           8 +done; wait
diff --git a/test_approach.py b/test_approach.py
index 17ddc6a..d5cbcbc 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -3,6 +3,7 @@ import numpy as np
    3      3  from env_client import make_env
    4      4  from approach import GeneratedApproach
    5      5  TMAX=0
           6 +AT=[0]
    6      7  def run(seed, count=None, verbose=False):
    7      8      env = make_env()
    8      9      kw = {}
@@ -12,11 +13,12 @@ def run(seed, count=None, verbose=False):
   12     13      ap.reset(obs, info)
   13     14      n_obj = info.get('object_count')
   14     15      global TMAX
          16 +    AT[0]=0
   15     17      t0=time.time()
   16     18      for t in range(env.max_steps):
   17        -        a = ap.get_action(obs)
          19 +        tt=time.time(); a = ap.get_action(obs); AT[0]+=time.time()-tt
   18     20          obs, r, term, trunc, info = env.step(a)
   19        -        if term: env.close(); TMAX=max(TMAX, time.time()-t0); return True, t+1, n_obj
          21 +        if term: env.close(); TMAX=max(TMAX, AT[0]); return True, t+1, n_obj
   20     22          if trunc: break
   21     23      env.close(); return False, env.max_steps, n_obj
   22     24  if __name__ == '__main__':
@@ -27,4 +29,4 @@ if __name__ == '__main__':
   27     29          succ, n, c = run(s, count)
   28     30          ok += succ; steps.append(n)
   29     31          if not succ: print('FAIL seed', s, 'count', c)
   30        -    print(f'success {ok}/{s1-s0}, mean steps {np.mean(steps):.1f} max ep time {TMAX:.1f}s')
          32 +    print(f'success {ok}/{s1-s0}, mean steps {np.mean(steps):.1f} max approach time {TMAX:.1f}s')
```

</details>

<a id="C010"></a>
### C010 · allow gripper-overhang grasps to reach edge objects; evaluate multiple grasp offsets for block dest

Commit `ad61105e95faabb63b8bfd309f19e4fc49a7ec61`; parents: 9a3cd474e95d08874055277d95ba6cdf32b16f5e. Recorded author date: 2026-09-28T14:49:33+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0381](01_timeline.md#E0381): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_ad61105_approach.py) · [Exact all-file diff](evidence/diffs/C010_ad61105.diff)

[Previous saved controller snapshot](evidence/versions/C009_9a3cd47_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4ca92f1..7e94b75 100644
--- a/approach.py
+++ b/approach.py
@@ -168,7 +168,7 @@ class GeneratedApproach:
  168    168  
  169    169      def _grasp_x(self, b, others, rng=None, pref=None):
  170    170          half = self.robot["gh"] / 2.0
  171        -        lo, hi = b["x"] + 0.006, b["x"] + b["w"] - 0.006
         171 +        lo, hi = b["x"] + 0.012 - half, b["x"] + b["w"] - 0.012 + half
  172    172          if rng is not None:
  173    173              lo, hi = max(lo, rng[0]), min(hi, rng[1])
  174    174          lo, hi = max(lo, X_MIN), min(hi, X_MAX)
@@ -273,19 +273,27 @@ class GeneratedApproach:
  273    273              lo = hi = center
  274    274          best = None
  275    275          for dx in np.linspace(lo, hi, 25):
  276        -            glo = max(0.006, X_MIN - dx, X_MIN - b["x"])
  277        -            ghi = min(b["w"] - 0.006, X_MAX - dx, X_MAX - b["x"])
         276 +            half = self.robot["gh"] / 2.0
         277 +            glo = max(0.012 - half, X_MIN - dx, X_MIN - b["x"])
         278 +            ghi = min(b["w"] - 0.012 + half, X_MAX - dx, X_MAX - b["x"])
         279 +            if ghi >= glo:
         280 +                # prefer no gripper overhang
         281 +                ilo, ihi = max(glo, half + 0.003), min(ghi, b["w"] - half - 0.003)
  278    282              if ghi < glo:
  279    283                  continue
  280        -            grel = min(max(b["w"] / 2, glo), ghi)
  281        -            nb = 0
  282        -            for o in self.obst.values():
  283        -                if self._column_hit(o, dest_x=dx, grel=grel):
  284        -                    reach = o["x"] + 0.006 <= X_MAX and o["x"] + o["w"] - 0.006 >= X_MIN
  285        -                    nb += 1 if reach else 100
  286        -            cost = nb * 100 + abs(dx - center) * 0.1
  287        -            if best is None or cost < best[0]:
  288        -                best = (cost, dx, grel)
         284 +            if ilo <= ihi:
         285 +                pref = min(max(b["w"] / 2, ilo), ihi)
         286 +            else:
         287 +                pref = min(max(b["w"] / 2, glo), ghi)
         288 +            for grel in (pref, glo, ghi, 0.5 * (pref + glo), 0.5 * (pref + ghi)):
         289 +                nb = 0
         290 +                for o in self.obst.values():
         291 +                    if self._column_hit(o, dest_x=dx, grel=grel):
         292 +                        reach = o["x"] + 0.012 - half <= X_MAX and o["x"] + o["w"] - 0.012 + half >= X_MIN
         293 +                        nb += 1 if reach else 100
         294 +                cost = nb * 100 + abs(dx - center) * 0.1 + abs(grel - pref) * 0.5
         295 +                if best is None or cost < best[0]:
         296 +                    best = (cost, dx, grel)
  289    297          if best is None:
  290    298              return center, b["w"] / 2
  291    299          return best[1], best[2]
diff --git a/run_many.sh b/run_many.sh
index 6f5ae4a..3ad5121 100755
--- a/run_many.sh
+++ b/run_many.sh
@@ -4,5 +4,5 @@ c=$1; s=$2; e=$3; p=$4
    4      4  step=$(( (e - s + p - 1) / p ))
    5      5  for ((i=s; i<e; i+=step)); do
    6      6    j=$((i+step)); [ $j -gt $e ] && j=$e
    7        -  timeout 1500 /opt/robocode-strict/bin/python test_approach.py $i $j $c 2>&1 | grep -E "FAIL|success|Error" &
           7 +  timeout 1500 /opt/robocode-strict/bin/python test_approach.py $i $j ${c/none/} 2>&1 | grep -E "FAIL|success|Error" &
    8      8  done; wait
diff --git a/scan.py b/scan.py
new file mode 100644
index 0000000..8f9d750
--- /dev/null
+++ b/scan.py
@@ -0,0 +1,17 @@
           1 +import sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach, X_MIN, X_MAX
           4 +env = make_env()
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           6 +s0,s1=int(sys.argv[1]),int(sys.argv[2]); c=int(sys.argv[3]) if len(sys.argv)>3 else None
           7 +nb=nu=0
           8 +for seed in range(s0,s1):
           9 +    obs,info=env.reset(seed=seed, options=({'object_count':c} if c is not None else None))
          10 +    ap.reset(obs,info); ap._parse(obs)
          11 +    b=ap.block
          12 +    reach=lambda o: o["x"] + 0.006 <= X_MAX and o["x"] + o["w"] - 0.006 >= X_MIN
          13 +    if not reach(b): nb+=1; print('block unreachable', seed, b)
          14 +    d,g=ap._choose_block_dest(); ap.block_dest, ap.block_grel = d,g
          15 +    for o in ap.obst.values():
          16 +        if ap._column_hit(o) and not reach(o): nu+=1; print('unreach blocker', seed, o)
          17 +print('done', nb, nu)
```

</details>

<a id="C011"></a>
### C011 · fix robot bounds (start pose was out of assumed bounds -> fallback paths)

Commit `445a406ccdd829eea22562ef71783c5e92e5f895`; parents: ad61105e95faabb63b8bfd309f19e4fc49a7ec61. Recorded author date: 2026-09-28T15:07:39+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0444](01_timeline.md#E0444): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_445a406_approach.py) · [Exact all-file diff](evidence/diffs/C011_445a406.diff)

[Previous saved controller snapshot](evidence/versions/C010_ad61105_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7e94b75..bc0a4a0 100644
--- a/approach.py
+++ b/approach.py
@@ -8,8 +8,8 @@ import math
    8      8  import numpy as np
    9      9  
   10     10  FLOOR = 0.1
   11        -X_MIN, X_MAX = 0.1005, 1.5175   # robot base x limits
   12        -Y_MAX = 0.895                   # robot base y limit
          11 +X_MIN, X_MAX = 0.1001, 1.5179   # robot base x limits
          12 +Y_MAX = 0.8995                  # robot base y limit
   13     13  WORLD_X = 1.618
   14     14  GAP = 0.0015                    # gripper gap above object when grasping
   15     15  PLACE_GAP = 0.004               # object gap above floor when releasing
diff --git a/steps_0.txt b/steps_0.txt
new file mode 100644
index 0000000..4a3841f
--- /dev/null
+++ b/steps_0.txt
@@ -0,0 +1,25 @@
           1 +0 True 52 2
           2 +1 True 39 1
           3 +2 True 61 2
           4 +3 True 37 2
           5 +4 True 47 2
           6 +5 True 66 2
           7 +6 True 37 1
           8 +7 True 87 2
           9 +8 True 51 2
          10 +9 True 79 1
          11 +10 True 44 2
          12 +11 True 38 0
          13 +12 True 68 1
          14 +13 True 42 2
          15 +14 True 20 0
          16 +15 True 22 2
          17 +16 True 17 1
          18 +17 True 49 2
          19 +18 True 36 2
          20 +19 True 35 1
          21 +20 True 46 2
          22 +21 True 45 0
          23 +22 True 66 2
          24 +23 True 35 0
          25 +24 True 40 1
diff --git a/steps_1.txt b/steps_1.txt
new file mode 100644
index 0000000..a143bb4
--- /dev/null
+++ b/steps_1.txt
@@ -0,0 +1,25 @@
           1 +25 True 36 1
           2 +26 True 44 2
           3 +27 True 13 0
           4 +28 True 38 1
           5 +29 True 19 2
           6 +30 True 18 0
           7 +31 True 32 1
           8 +32 True 51 2
           9 +33 True 39 2
          10 +34 True 25 0
          11 +35 True 24 0
          12 +36 True 23 1
          13 +37 True 25 0
          14 +38 True 15 0
          15 +39 True 43 2
          16 +40 True 46 1
          17 +41 True 26 1
          18 +42 True 25 0
          19 +43 True 21 1
          20 +44 True 40 2
          21 +45 True 53 2
          22 +46 True 32 1
          23 +47 True 31 0
          24 +48 True 15 0
          25 +49 True 14 0
diff --git a/steps_2.txt b/steps_2.txt
new file mode 100644
index 0000000..49abb40
--- /dev/null
+++ b/steps_2.txt
@@ -0,0 +1,25 @@
           1 +50 True 53 2
           2 +51 True 26 1
           3 +52 True 43 2
           4 +53 True 43 2
           5 +54 True 23 0
           6 +55 True 22 2
           7 +56 True 48 1
           8 +57 True 11 0
           9 +58 True 36 1
          10 +59 True 48 2
          11 +60 True 20 0
          12 +61 True 46 1
          13 +62 True 48 1
          14 +63 True 26 1
          15 +64 True 22 1
          16 +65 True 13 0
          17 +66 True 36 2
          18 +67 True 29 2
          19 +68 True 25 1
          20 +69 True 30 0
          21 +70 True 28 1
          22 +71 True 19 2
          23 +72 True 83 2
          24 +73 True 49 2
          25 +74 True 18 0
diff --git a/steps_3.txt b/steps_3.txt
new file mode 100644
index 0000000..90a88c6
--- /dev/null
+++ b/steps_3.txt
@@ -0,0 +1,25 @@
           1 +75 True 52 1
           2 +76 True 26 1
           3 +77 True 15 0
           4 +78 True 66 2
           5 +79 True 27 0
           6 +80 True 64 2
           7 +81 True 19 0
           8 +82 True 32 2
           9 +83 True 59 2
          10 +84 True 48 1
          11 +85 True 38 2
          12 +86 True 24 2
          13 +87 True 32 1
          14 +88 True 43 1
          15 +89 True 41 2
          16 +90 True 50 1
          17 +91 True 23 2
          18 +92 True 34 1
          19 +93 True 63 2
          20 +94 True 17 0
          21 +95 True 42 1
          22 +96 True 27 2
          23 +97 True 29 0
          24 +98 True 44 1
          25 +99 True 46 2
diff --git a/steps_list.py b/steps_list.py
new file mode 100644
index 0000000..2503c20
--- /dev/null
+++ b/steps_list.py
@@ -0,0 +1,6 @@
           1 +import sys
           2 +from test_approach import run
           3 +s0,s1=int(sys.argv[1]),int(sys.argv[2])
           4 +for s in range(s0,s1):
           5 +    ok,n,c=run(s)
           6 +    print(s,ok,n,c,flush=True)
```

</details>

<a id="C012"></a>
### C012 · arm-aware path planning (retract arm on plateaus), fix bounds check precedence

Commit `4c36d8ba1744c72de6b93c7f4ec0d7c1626230ed`; parents: 445a406ccdd829eea22562ef71783c5e92e5f895. Recorded author date: 2026-09-28T15:10:00+02:00.

File roles (automatic): policy, setup/other.

- [E0465](01_timeline.md#E0465): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_4c36d8b_approach.py) · [Exact all-file diff](evidence/diffs/C012_4c36d8b.diff)

[Previous saved controller snapshot](evidence/versions/C011_445a406_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bc0a4a0..6793e56 100644
--- a/approach.py
+++ b/approach.py
@@ -14,14 +14,22 @@ WORLD_X = 1.618
   14     14  GAP = 0.0015                    # gripper gap above object when grasping
   15     15  PLACE_GAP = 0.004               # object gap above floor when releasing
   16     16  SPEED = 0.05
          17 +ARM_SPEED = 0.1
   17     18  
   18     19  
   19     20  def _cheb(a, b):
   20     21      return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
   21     22  
   22     23  
          24 +def _seg_steps(a, b):
          25 +    v = max(abs(a[0] - b[0]) / SPEED, abs(a[1] - b[1]) / SPEED)
          26 +    if len(a) > 2 and len(b) > 2:
          27 +        v = max(v, abs(a[2] - b[2]) / ARM_SPEED)
          28 +    return math.ceil(v - 1e-6)
          29 +
          30 +
   23     31  def _nsteps(path):
   24        -    return sum(math.ceil(_cheb(path[i], path[i + 1]) / SPEED - 1e-6) for i in range(len(path) - 1))
          32 +    return sum(_seg_steps(path[i], path[i + 1]) for i in range(len(path) - 1))
   25     33  
   26     34  
   27     35  class GeneratedApproach:
@@ -77,13 +85,20 @@ class GeneratedApproach:
   77     85          Y = pts[:, 1]
   78     86          r = self.robot["r"]
   79     87          half = self.robot["gh"] / 2.0
   80        -        go = self._grip_off()
   81        -        if check_bounds and np.any(X < X_MIN - 1e-6) or np.any(X > X_MAX + 1e-6) or np.any(Y > Y_MAX + 1e-6):
          88 +        amax = self.robot["arm_max"]
          89 +        if pts.shape[1] > 2:
          90 +            Ar = pts[:, 2]
          91 +        else:
          92 +            Ar = np.full(len(X), amax)
          93 +        go = Ar + self.robot["gw"] / 2.0
          94 +        if check_bounds and (np.any(X < X_MIN - 1e-6) or np.any(X > X_MAX + 1e-6)
          95 +                             or np.any(Y > Y_MAX + 1e-6)):
   82     96              return True
   83     97          # boxes attached to robot: gripper/arm, carried
   84     98          att = [(X - half, X + half, Y - go, Y)]
   85     99          if carried is not None:
   86        -            att.append((X + carried[0], X + carried[1], Y + carried[2], Y + carried[3]))
         100 +            sh = amax - Ar
         101 +            att.append((X + carried[0], X + carried[1], Y + carried[2] + sh, Y + carried[3] + sh))
   87    102          for o in list(obstacles) + [self.FLOOR_BOX]:
   88    103              m = margin_map.get(o["name"], default_margin)
   89    104              ox0, ox1 = o["x"] - m, o["x"] + o["w"] + m
@@ -100,8 +115,8 @@ class GeneratedApproach:
  100    115  
  101    116      def _path_free(self, path, obstacles, carried, margin_map, m):
  102    117          for i in range(len(path) - 1):
  103        -            a, b = np.array(path[i]), np.array(path[i + 1])
  104        -            L = max(np.linalg.norm(b - a), 1e-9)
         118 +            a, b = np.array(path[i], dtype=float), np.array(path[i + 1], dtype=float)
         119 +            L = max(np.linalg.norm(b[:2] - a[:2]), abs(b[2] - a[2]) if len(a) > 2 else 0.0, 1e-9)
  105    120              n = int(L / 0.003) + 2
  106    121              t = np.linspace(0, 1, n)[:, None]
  107    122              pts = a[None] * (1 - t) + b[None] * t
@@ -110,7 +125,11 @@ class GeneratedApproach:
  110    125          return True
  111    126  
  112    127      def _plan_path(self, A, B, obstacles, carried, special_margin=None):
  113        -        """Find short collision-free polyline from A to B."""
         128 +        """Find short collision-free polyline from A to B (points are (x, y, arm))."""
         129 +        amax = self.robot["arm_max"]
         130 +        amin = self.robot["r"]
         131 +        A = (A[0], A[1], A[2] if len(A) > 2 else amax)
         132 +        B = (B[0], B[1], B[2] if len(B) > 2 else amax)
  114    133          m = 0.004
  115    134          margin_map = {}
  116    135          # obstacles in contact at endpoints get zero margin
@@ -122,27 +141,31 @@ class GeneratedApproach:
  122    141              margin_map.update(special_margin)
  123    142          cands = [[A, B]]
  124    143          sgn = 1.0 if B[0] >= A[0] else -1.0
  125        -        hs = np.arange(max(A[1], B[1]), Y_MAX + 1e-9, 0.01)
  126        -        hs = np.append(hs, Y_MAX)
  127        -        h_min = Y_MAX
  128        -        for h in hs:
  129        -            if self._path_free([(A[0], h), (B[0], h)], obstacles, carried, margin_map, m):
  130        -                h_min = h
  131        -                break
  132        -        hs = hs[hs >= h_min - 1e-9]
  133        -        for h in hs:
  134        -            for k1 in (1.0, 0.5, 0.0):
  135        -                for k2 in (1.0, 0.5, 0.0):
  136        -                    x1 = A[0] + sgn * k1 * (h - A[1])
  137        -                    x2 = B[0] - sgn * k2 * (h - B[1])
  138        -                    if sgn * (x2 - x1) <= 0:
  139        -                        # triangle: find intersection point
  140        -                        continue
  141        -                    p = [A, (x1, h), (x2, h), B]
  142        -                    cands.append(p)
  143        -            # triangle via single apex
  144        -            for xv in np.linspace(A[0], B[0], 9)[1:-1]:
  145        -                cands.append([A, (xv, h), B])
         144 +        for ap in (amax, amin):
         145 +            h0 = max(A[1], B[1]) - (amax - ap)
         146 +            hs = np.arange(h0, Y_MAX + 1e-9, 0.01)
         147 +            hs = np.append(hs, Y_MAX)
         148 +            h_min = None
         149 +            for h in hs:
         150 +                if self._path_free([(A[0], h, ap), (B[0], h, ap)], obstacles, carried, margin_map, m):
         151 +                    h_min = h
         152 +                    break
         153 +            if h_min is None:
         154 +                continue
         155 +            hs = hs[hs >= h_min - 1e-9]
         156 +            for h in hs:
         157 +                r1 = max(abs(h - A[1]), SPEED if abs(ap - A[2]) > 1e-9 else 0.0)
         158 +                r2 = max(abs(h - B[1]), SPEED if abs(ap - B[2]) > 1e-9 else 0.0)
         159 +                for k1 in (1.0, 0.5, 0.0):
         160 +                    for k2 in (1.0, 0.5, 0.0):
         161 +                        x1 = A[0] + sgn * k1 * r1
         162 +                        x2 = B[0] - sgn * k2 * r2
         163 +                        if sgn * (x2 - x1) < 0:
         164 +                            continue
         165 +                        p = [A, (x1, h, ap), (x2, h, ap), B]
         166 +                        cands.append(p)
         167 +                for xv in np.linspace(A[0], B[0], 9)[1:-1]:
         168 +                    cands.append([A, (xv, h, ap), B])
  146    169          scored = sorted(((_nsteps(p), len(p), i) for i, p in enumerate(cands)))
  147    170          checked = 0
  148    171          for s, _, i in scored:
@@ -153,7 +176,7 @@ class GeneratedApproach:
  153    176              if self._path_free(p, obstacles, carried, margin_map, m):
  154    177                  return p
  155    178          # fallback: straight up, over, down
  156        -        return [A, (A[0], Y_MAX), (B[0], Y_MAX), B]
         179 +        return [A, (A[0], Y_MAX, amax), (B[0], Y_MAX, amax), B]
  157    180  
  158    181      # --------------------------------------------------------------- planning
  159    182      def reset(self, state, info):
@@ -369,16 +392,16 @@ class GeneratedApproach:
  369    392          px = min(max(dest_x + gx_rel, X_MIN), X_MAX)
  370    393          py = dest_y + off + PLACE_GAP
  371    394          # approach path (nothing carried)
  372        -        p1 = self._plan_path((rx, ry), gpos, others + [tgt], None,
         395 +        p1 = self._plan_path((rx, ry, self.robot["arm"]), gpos, others + [tgt], None,
  373    396                               special_margin={tgt["name"]: 0.0})
  374    397          carried = (tgt["x"] - gx, tgt["x"] + tgt["w"] - gx, tgt["y"] - gy, tgt["y"] + tgt["h"] - gy)
  375    398          p2 = self._plan_path(gpos, (px, py), others, carried)
  376    399          segs = []
  377    400          for w in p1[1:]:
  378        -            segs.append(dict(x=w[0], y=w[1], vac=0, kind="move"))
         401 +            segs.append(dict(x=w[0], y=w[1], a=w[2], vac=0, kind="move"))
  379    402          segs.append(dict(x=gx, y=gy, vac=1, kind="grasp"))
  380    403          for w in p2[1:]:
  381        -            segs.append(dict(x=w[0], y=w[1], vac=1, kind="carry"))
         404 +            segs.append(dict(x=w[0], y=w[1], a=w[2], vac=1, kind="carry"))
  382    405          # release on the final step of the carry
  383    406          segs[-1]["release_last"] = not is_block
  384    407          self.carry = dict(name=tgt["name"], px=px, py=py, release=not is_block,
@@ -395,12 +418,13 @@ class GeneratedApproach:
  395    418              return None
  396    419          o = movable[c["name"]]
  397    420          rx, ry = self.robot["x"], self.robot["y"]
  398        -        if abs(o["x"] - rx - c["rel"][0]) > 2e-3 or abs(o["y"] - ry - c["rel"][1]) > 2e-3:
         421 +        sh = self.robot["arm_max"] - self.robot["arm"]
         422 +        if abs(o["x"] - rx - c["rel"][0]) > 2e-3 or abs(o["y"] - ry - sh - c["rel"][1]) > 2e-3:
  399    423              return None
  400    424          others = [b for n, b in movable.items() if n != o["name"]]
  401        -        carried = (o["x"] - rx, o["x"] + o["w"] - rx, o["y"] - ry, o["y"] + o["h"] - ry)
  402        -        p = self._plan_path((rx, ry), (c["px"], c["py"]), others, carried)
  403        -        segs = [dict(x=w[0], y=w[1], vac=1, kind="carry") for w in p[1:]]
         425 +        carried = (o["x"] - rx, o["x"] + o["w"] - rx, o["y"] - ry - sh, o["y"] + o["h"] - ry - sh)
         426 +        p = self._plan_path((rx, ry, self.robot["arm"]), (c["px"], c["py"]), others, carried)
         427 +        segs = [dict(x=w[0], y=w[1], a=w[2], vac=1, kind="carry") for w in p[1:]]
  404    428          if not segs:
  405    429              return None
  406    430          segs[-1]["release_last"] = c["release"]
@@ -418,7 +442,8 @@ class GeneratedApproach:
  418    442              if wp["kind"] == "grasp":
  419    443                  reached = r["vac"] > 0.5
  420    444              else:
  421        -                reached = abs(r["x"] - wp["x"]) < 1e-4 and abs(r["y"] - wp["y"]) < 1e-4
         445 +                reached = abs(r["x"] - wp["x"]) < 1e-4 and abs(r["y"] - wp["y"]) < 1e-4 \
         446 +                    and abs(r["arm"] - wp.get("a", r["arm_max"])) < 1e-4
  422    447                  if wp.get("release_last"):
  423    448                      reached = reached and r["vac"] < 0.5
  424    449              if reached:
@@ -448,15 +473,17 @@ class GeneratedApproach:
  448    473                  if self.stuck_carry <= 4:
  449    474                      segs = self._replan_carry()
  450    475                      if segs:
  451        -                        self.plan = [dict(x=r["x"], y=min(Y_MAX, r["y"] + 0.02), vac=1,
         476 +                        self.plan = [dict(x=r["x"], y=min(Y_MAX, r["y"] + 0.02), a=r["arm"], vac=1,
  452    477                                            kind="carry")] + segs
  453    478              if wp["kind"] == "carry" and wp is not None:
  454    479                  return self._act(0, 0.02, 0, 1 if r["vac"] > 0.5 else 0, dth)
  455    480              return self._act(0, 0.02, 0, 0, dth)
  456    481          dx = wp["x"] - r["x"]
  457    482          dy = wp["y"] - r["y"]
  458        -        mx = max(abs(dx), abs(dy))
  459        -        sc = min(1.0, SPEED / mx) if mx > 0 else 1.0
         483 +        da = wp.get("a", r["arm_max"]) - r["arm"]
         484 +        mx = max(abs(dx) / SPEED, abs(dy) / SPEED, abs(da) / ARM_SPEED)
         485 +        sc = min(1.0, 1.0 / mx) if mx > 0 else 1.0
         486 +        darm = da * sc
  460    487          vac = wp["vac"]
  461    488          if wp.get("release_last") and sc >= 1.0:
  462    489              vac = 0
diff --git a/steps2_0.txt b/steps2_0.txt
new file mode 100644
index 0000000..3bac9ae
--- /dev/null
+++ b/steps2_0.txt
@@ -0,0 +1,25 @@
           1 +0 True 52 2
           2 +1 True 40 1
           3 +2 True 62 2
           4 +3 True 37 2
           5 +4 True 47 2
           6 +5 True 68 2
           7 +6 True 37 1
           8 +7 True 87 2
           9 +8 True 51 2
          10 +9 True 69 1
          11 +10 True 44 2
          12 +11 True 38 0
          13 +12 True 68 1
          14 +13 True 42 2
          15 +14 True 20 0
          16 +15 True 22 2
          17 +16 True 17 1
          18 +17 True 49 2
          19 +18 True 36 2
          20 +19 True 35 1
          21 +20 True 46 2
          22 +21 True 45 0
          23 +22 True 66 2
          24 +23 True 35 0
          25 +24 True 40 1
diff --git a/steps2_1.txt b/steps2_1.txt
new file mode 100644
index 0000000..db228f8
--- /dev/null
+++ b/steps2_1.txt
@@ -0,0 +1,25 @@
           1 +25 True 36 1
           2 +26 True 44 2
           3 +27 True 13 0
           4 +28 True 38 1
           5 +29 True 19 2
           6 +30 True 18 0
           7 +31 True 32 1
           8 +32 True 51 2
           9 +33 True 39 2
          10 +34 True 25 0
          11 +35 True 24 0
          12 +36 True 23 1
          13 +37 True 25 0
          14 +38 True 15 0
          15 +39 True 42 2
          16 +40 True 46 1
          17 +41 True 26 1
          18 +42 True 25 0
          19 +43 True 21 1
          20 +44 True 40 2
          21 +45 True 53 2
          22 +46 True 32 1
          23 +47 True 31 0
          24 +48 True 15 0
          25 +49 True 14 0
diff --git a/steps2_2.txt b/steps2_2.txt
new file mode 100644
index 0000000..1f672ca
--- /dev/null
+++ b/steps2_2.txt
@@ -0,0 +1,25 @@
           1 +50 True 53 2
           2 +51 True 26 1
           3 +52 True 43 2
           4 +53 True 43 2
           5 +54 True 23 0
           6 +55 True 22 2
           7 +56 True 48 1
           8 +57 True 11 0
           9 +58 True 36 1
          10 +59 True 48 2
          11 +60 True 20 0
          12 +61 True 46 1
          13 +62 True 48 1
          14 +63 True 21 1
          15 +64 True 22 1
          16 +65 True 13 0
          17 +66 True 36 2
          18 +67 True 29 2
          19 +68 True 25 1
          20 +69 True 30 0
          21 +70 True 28 1
          22 +71 True 19 2
          23 +72 True 83 2
          24 +73 True 49 2
          25 +74 True 18 0
diff --git a/steps2_3.txt b/steps2_3.txt
new file mode 100644
index 0000000..de984eb
--- /dev/null
+++ b/steps2_3.txt
@@ -0,0 +1,25 @@
           1 +75 True 52 1
           2 +76 True 23 1
           3 +77 True 15 0
           4 +78 True 66 2
           5 +79 True 27 0
           6 +80 True 54 2
           7 +81 True 19 0
           8 +82 True 32 2
           9 +83 True 59 2
          10 +84 True 48 1
          11 +85 True 38 2
          12 +86 True 24 2
          13 +87 True 32 1
          14 +88 True 43 1
          15 +89 True 41 2
          16 +90 True 50 1
          17 +91 True 23 2
          18 +92 True 34 1
          19 +93 True 59 2
          20 +94 True 17 0
          21 +95 True 42 1
          22 +96 True 27 2
          23 +97 True 29 0
          24 +98 True 44 1
          25 +99 True 36 2
```

</details>

<a id="C013"></a>
### C013 · place block slightly higher within tolerance

Commit `14791667a9097b1cc1bfbe3eca93a18fab66f29b`; parents: 4c36d8ba1744c72de6b93c7f4ec0d7c1626230ed. Recorded author date: 2026-09-28T15:30:37+02:00.

File roles (automatic): policy, setup/other.

- [E0528](01_timeline.md#E0528): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_1479166_approach.py) · [Exact all-file diff](evidence/diffs/C013_1479166.diff)

[Previous saved controller snapshot](evidence/versions/C012_4c36d8b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6793e56..a3204a3 100644
--- a/approach.py
+++ b/approach.py
@@ -15,6 +15,7 @@ GAP = 0.0015                    # gripper gap above object when grasping
   15     15  PLACE_GAP = 0.004               # object gap above floor when releasing
   16     16  SPEED = 0.05
   17     17  ARM_SPEED = 0.1
          18 +BLOCK_Z = 0.019                 # block bottom height above surface when placing (tol 0.025)
   18     19  
   19     20  
   20     21  def _cheb(a, b):
@@ -274,7 +275,7 @@ class GeneratedApproach:
  274    275          gx_rel = self.block_grel if grel is None else grel
  275    276          gy_rel = b["h"] + self._grip_off() + GAP
  276    277          bx = dest_x + gx_rel
  277        -        py = FLOOR + 0.012 + gy_rel
         278 +        py = FLOOR + BLOCK_Z + gy_rel
  278    279          pts = np.stack([np.full(40, bx), np.linspace(py, Y_MAX, 40)], axis=1)
  279    280          carried = (-gx_rel, b["w"] - gx_rel, -gy_rel, b["h"] - gy_rel)
  280    281          return pts, carried
@@ -380,7 +381,7 @@ class GeneratedApproach:
  380    381          gx_rel = gx - tgt["x"]
  381    382          if is_block:
  382    383              dest_x = self.block_dest
  383        -            dest_y = FLOOR + 0.012 - PLACE_GAP
         384 +            dest_y = FLOOR + BLOCK_Z - PLACE_GAP
  384    385          else:
  385    386              b = self.block
  386    387              bgx = b["x"] + b["w"] / 2
diff --git a/steps3_0.txt b/steps3_0.txt
new file mode 100644
index 0000000..7df49b8
--- /dev/null
+++ b/steps3_0.txt
@@ -0,0 +1,25 @@
           1 +0 True 44 2
           2 +1 True 36 1
           3 +2 True 54 2
           4 +3 True 34 2
           5 +4 True 47 2
           6 +5 True 57 2
           7 +6 True 35 1
           8 +7 True 81 2
           9 +8 True 44 2
          10 +9 True 66 1
          11 +10 True 36 2
          12 +11 True 38 0
          13 +12 True 65 1
          14 +13 True 40 2
          15 +14 True 20 0
          16 +15 True 18 2
          17 +16 True 17 1
          18 +17 True 42 2
          19 +18 True 35 2
          20 +19 True 29 1
          21 +20 True 42 2
          22 +21 True 45 0
          23 +22 True 60 2
          24 +23 True 35 0
          25 +24 True 40 1
diff --git a/steps3_1.txt b/steps3_1.txt
new file mode 100644
index 0000000..ad660f9
--- /dev/null
+++ b/steps3_1.txt
@@ -0,0 +1,25 @@
           1 +25 True 32 1
           2 +26 True 37 2
           3 +27 True 13 0
           4 +28 True 38 1
           5 +29 True 19 2
           6 +30 True 18 0
           7 +31 True 30 1
           8 +32 True 47 2
           9 +33 True 35 2
          10 +34 True 25 0
          11 +35 True 24 0
          12 +36 True 23 1
          13 +37 True 25 0
          14 +38 True 15 0
          15 +39 True 41 2
          16 +40 True 45 1
          17 +41 True 25 1
          18 +42 True 25 0
          19 +43 True 21 1
          20 +44 True 37 2
          21 +45 True 50 2
          22 +46 True 28 1
          23 +47 True 31 0
          24 +48 True 15 0
          25 +49 True 14 0
diff --git a/steps3_2.txt b/steps3_2.txt
new file mode 100644
index 0000000..3859252
--- /dev/null
+++ b/steps3_2.txt
@@ -0,0 +1,25 @@
           1 +50 True 49 2
           2 +51 True 26 1
           3 +52 True 39 2
           4 +53 True 41 2
           5 +54 True 23 0
           6 +55 True 19 2
           7 +56 True 43 1
           8 +57 True 11 0
           9 +58 True 33 1
          10 +59 True 45 2
          11 +60 True 20 0
          12 +61 True 43 1
          13 +62 True 44 1
          14 +63 True 21 1
          15 +64 True 22 1
          16 +65 True 13 0
          17 +66 True 36 2
          18 +67 True 26 2
          19 +68 True 25 1
          20 +69 True 30 0
          21 +70 True 25 1
          22 +71 True 19 2
          23 +72 True 76 2
          24 +73 True 45 2
          25 +74 True 18 0
diff --git a/steps3_3.txt b/steps3_3.txt
new file mode 100644
index 0000000..41341e8
--- /dev/null
+++ b/steps3_3.txt
@@ -0,0 +1,25 @@
           1 +75 True 48 1
           2 +76 True 23 1
           3 +77 True 15 0
           4 +78 True 58 2
           5 +79 True 27 0
           6 +80 True 46 2
           7 +81 True 19 0
           8 +82 True 31 2
           9 +83 True 51 2
          10 +84 True 46 1
          11 +85 True 36 2
          12 +86 True 22 2
          13 +87 True 30 1
          14 +88 True 41 1
          15 +89 True 38 2
          16 +90 True 46 1
          17 +91 True 23 2
          18 +92 True 31 1
          19 +93 True 54 2
          20 +94 True 17 0
          21 +95 True 41 1
          22 +96 True 23 2
          23 +97 True 29 0
          24 +98 True 42 1
          25 +99 True 36 2
diff --git a/steps4_0.txt b/steps4_0.txt
new file mode 100644
index 0000000..fd3e338
--- /dev/null
+++ b/steps4_0.txt
@@ -0,0 +1,25 @@
           1 +0 True 43 2
           2 +1 True 36 1
           3 +2 True 54 2
           4 +3 True 34 2
           5 +4 True 47 2
           6 +5 True 57 2
           7 +6 True 35 1
           8 +7 True 81 2
           9 +8 True 44 2
          10 +9 True 65 1
          11 +10 True 36 2
          12 +11 True 38 0
          13 +12 True 64 1
          14 +13 True 40 2
          15 +14 True 20 0
          16 +15 True 17 2
          17 +16 True 17 1
          18 +17 True 42 2
          19 +18 True 35 2
          20 +19 True 28 1
          21 +20 True 42 2
          22 +21 True 45 0
          23 +22 True 60 2
          24 +23 True 35 0
          25 +24 True 40 1
diff --git a/steps4_1.txt b/steps4_1.txt
new file mode 100644
index 0000000..0e492b2
--- /dev/null
+++ b/steps4_1.txt
@@ -0,0 +1,25 @@
           1 +25 True 32 1
           2 +26 True 37 2
           3 +27 True 13 0
           4 +28 True 38 1
           5 +29 True 19 2
           6 +30 True 18 0
           7 +31 True 30 1
           8 +32 True 47 2
           9 +33 True 35 2
          10 +34 True 25 0
          11 +35 True 24 0
          12 +36 True 23 1
          13 +37 True 25 0
          14 +38 True 15 0
          15 +39 True 41 2
          16 +40 True 45 1
          17 +41 True 25 1
          18 +42 True 25 0
          19 +43 True 21 1
          20 +44 True 36 2
          21 +45 True 50 2
          22 +46 True 28 1
          23 +47 True 31 0
          24 +48 True 15 0
          25 +49 True 14 0
diff --git a/steps4_2.txt b/steps4_2.txt
new file mode 100644
index 0000000..ad191e4
--- /dev/null
+++ b/steps4_2.txt
@@ -0,0 +1,25 @@
           1 +50 True 48 2
           2 +51 True 26 1
           3 +52 True 39 2
           4 +53 True 41 2
           5 +54 True 23 0
           6 +55 True 18 2
           7 +56 True 43 1
           8 +57 True 11 0
           9 +58 True 33 1
          10 +59 True 45 2
          11 +60 True 20 0
          12 +61 True 43 1
          13 +62 True 44 1
          14 +63 True 21 1
          15 +64 True 22 1
          16 +65 True 13 0
          17 +66 True 36 2
          18 +67 True 26 2
          19 +68 True 25 1
          20 +69 True 30 0
          21 +70 True 25 1
          22 +71 True 19 2
          23 +72 True 76 2
          24 +73 True 44 2
          25 +74 True 18 0
diff --git a/steps4_3.txt b/steps4_3.txt
new file mode 100644
index 0000000..c51d2f3
--- /dev/null
+++ b/steps4_3.txt
@@ -0,0 +1,25 @@
           1 +75 True 48 1
           2 +76 True 23 1
           3 +77 True 15 0
           4 +78 True 58 2
           5 +79 True 27 0
           6 +80 True 46 2
           7 +81 True 19 0
           8 +82 True 31 2
           9 +83 True 51 2
          10 +84 True 46 1
          11 +85 True 36 2
          12 +86 True 22 2
          13 +87 True 30 1
          14 +88 True 41 1
          15 +89 True 38 2
          16 +90 True 45 1
          17 +91 True 23 2
          18 +92 True 31 1
          19 +93 True 54 2
          20 +94 True 17 0
          21 +95 True 40 1
          22 +96 True 23 2
          23 +97 True 29 0
          24 +98 True 42 1
          25 +99 True 36 2
```

</details>

<a id="C014"></a>
### C014 · stage block near surface when far; next_pos uses next blocker

Commit `55854010df49b4ec6cc50568edb70575f7c467da`; parents: 14791667a9097b1cc1bfbe3eca93a18fab66f29b. Recorded author date: 2026-09-28T15:32:26+02:00.

File roles (automatic): policy.

- [E0550](01_timeline.md#E0550): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_5585401_approach.py) · [Exact all-file diff](evidence/diffs/C014_5585401.diff)

[Previous saved controller snapshot](evidence/versions/C013_1479166_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a3204a3..4195637 100644
--- a/approach.py
+++ b/approach.py
@@ -186,6 +186,7 @@ class GeneratedApproach:
  186    186          self.last_pos = None
  187    187          self.target_name = None
  188    188          self.block_dest = None
         189 +        self.staged = False
  189    190          self.attempts = {}
  190    191          self.carry = None
  191    192          self.stuck_carry = 0
@@ -342,8 +343,16 @@ class GeneratedApproach:
  342    343                  if bl2:
  343    344                      self.block_grel = grel
  344    345                      blockers = bl2
         346 +        stage = False
  345    347          if blockers:
  346    348              tgt = min(blockers, key=lambda b: abs(b["x"] + b["w"] / 2 - rx))
         349 +            if not self.staged:
         350 +                oc = tgt["x"] + tgt["w"] / 2
         351 +                bc = self.block["x"] + self.block_grel
         352 +                gain = abs(rx - oc) + abs(oc - bc) - abs(rx - bc) - abs(bc - self.block_dest)
         353 +                if gain > STAGE_GAIN:
         354 +                    stage = True
         355 +                    tgt = self.block
  347    356          else:
  348    357              tgt = self.block
  349    358          gx = None
@@ -379,13 +388,26 @@ class GeneratedApproach:
  379    388          gpos = (gx, gy)
  380    389          off = gy - tgt["y"]
  381    390          gx_rel = gx - tgt["x"]
  382        -        if is_block:
         391 +        if is_block and stage and tgt["name"] == self.block["name"]:
         392 +            self.staged = True
         393 +            nb = min(blockers, key=lambda b: abs(b["x"] + b["w"] / 2 - self.block_dest))
         394 +            next_pos = (nb["x"] + nb["w"] / 2, nb["y"] + nb["h"] + self._grip_off() + GAP)
         395 +            spot = self._free_spot(tgt, others, [], gx_rel, gpos, next_pos)
         396 +            if spot is None:
         397 +                spot = (tgt["x"], min(0.6, tgt["y"] + 0.3))
         398 +            is_block = False
         399 +            dest_x, dest_y = spot
         400 +        elif is_block:
  383    401              dest_x = self.block_dest
  384    402              dest_y = FLOOR + BLOCK_Z - PLACE_GAP
  385    403          else:
  386    404              b = self.block
  387    405              bgx = b["x"] + b["w"] / 2
  388    406              next_pos = (bgx, b["y"] + b["h"] + self._grip_off() + GAP)
         407 +            rem = [o for o in blockers if o["name"] != tgt["name"]]
         408 +            if rem:
         409 +                nb = min(rem, key=lambda o: abs(o["x"] + o["w"] / 2 - gx))
         410 +                next_pos = (nb["x"] + nb["w"] / 2, nb["y"] + nb["h"] + self._grip_off() + GAP)
  389    411              spot = self._free_spot(tgt, others, [], gx_rel, gpos, next_pos)
  390    412              if spot is None:
  391    413                  spot = (tgt["x"], min(0.6, tgt["y"] + 0.3))
```

</details>

<a id="C015"></a>
### C015 · fix STAGE_GAIN const

Commit `a1cd712be8df1e7769fa822cd074975f76919751`; parents: 55854010df49b4ec6cc50568edb70575f7c467da. Recorded author date: 2026-09-28T15:32:49+02:00.

File roles (automatic): policy.

- [E0573](01_timeline.md#E0573): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_a1cd712_approach.py) · [Exact all-file diff](evidence/diffs/C015_a1cd712.diff)

[Previous saved controller snapshot](evidence/versions/C014_5585401_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4195637..0607954 100644
--- a/approach.py
+++ b/approach.py
@@ -16,6 +16,7 @@ PLACE_GAP = 0.004               # object gap above floor when releasing
   16     16  SPEED = 0.05
   17     17  ARM_SPEED = 0.1
   18     18  BLOCK_Z = 0.019                 # block bottom height above surface when placing (tol 0.025)
          19 +STAGE_GAIN = 0.6
   19     20  
   20     21  
   21     22  def _cheb(a, b):
```

</details>

<a id="C016"></a>
### C016 · STAGE_GAIN 1.0

Commit `b8cbba66a5fe1fbe17bfc95caac29d1ca6da61ff`; parents: a1cd712be8df1e7769fa822cd074975f76919751. Recorded author date: 2026-09-28T15:57:59+02:00.

File roles (automatic): policy.

- [E0627](01_timeline.md#E0627): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_b8cbba6_approach.py) · [Exact all-file diff](evidence/diffs/C016_b8cbba6.diff)

[Previous saved controller snapshot](evidence/versions/C015_a1cd712_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0607954..c5162bb 100644
--- a/approach.py
+++ b/approach.py
@@ -16,7 +16,7 @@ PLACE_GAP = 0.004               # object gap above floor when releasing
   16     16  SPEED = 0.05
   17     17  ARM_SPEED = 0.1
   18     18  BLOCK_Z = 0.019                 # block bottom height above surface when placing (tol 0.025)
   19        -STAGE_GAIN = 0.6
          19 +STAGE_GAIN = 1.0
   20     20  
   21     21  
   22     22  def _cheb(a, b):
```

</details>

<a id="C017"></a>
### C017 · suction depth ~0.015: widen grasp conflict; release before free moves

Commit `e19f0c845d17cb4a045053b28996518b9b3f6276`; parents: b8cbba66a5fe1fbe17bfc95caac29d1ca6da61ff. Recorded author date: 2026-09-28T16:21:12+02:00.

File roles (automatic): policy.

- [E0728](01_timeline.md#E0728): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_e19f0c8_approach.py) · [Exact all-file diff](evidence/diffs/C017_e19f0c8.diff)

[Previous saved controller snapshot](evidence/versions/C016_b8cbba6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c5162bb..2a47316 100644
--- a/approach.py
+++ b/approach.py
@@ -216,7 +216,7 @@ class GeneratedApproach:
  216    216                  continue
  217    217              ok = True
  218    218              for o in others:
  219        -                if o["y"] + o["h"] > btop - 0.005 and o["x"] < x + half + 0.004 \
         219 +                if o["y"] + o["h"] > btop - 0.02 and o["x"] < x + half + 0.004 \
  220    220                          and o["x"] + o["w"] > x - half - 0.004:
  221    221                      ok = False
  222    222                      if self.grasp_conflict is None:
@@ -488,6 +488,9 @@ class GeneratedApproach:
  488    488          darm = r["arm_max"] - r["arm"]
  489    489          if wp["kind"] == "grasp":
  490    490              return self._act(0, 0, darm, 1, dth)
         491 +        if wp["kind"] == "move" and r["vac"] > 0.5:
         492 +            # make sure nothing is held before moving freely
         493 +            return self._act(0, 0, 0, 0, 0)
  491    494          if self.stall >= 2:
  492    495              # stuck: nudge up and replan
  493    496              self.stall = 0
```

</details>

<a id="C018"></a>
### C018 · group grasps: carry co-sucked obstructions together as union box

Commit `a6e42eaef26b68bbb74b2aec5e25e7be29adb91b`; parents: e19f0c845d17cb4a045053b28996518b9b3f6276. Recorded author date: 2026-09-28T16:22:19+02:00.

File roles (automatic): policy.

- [E0746](01_timeline.md#E0746): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_a6e42ea_approach.py) · [Exact all-file diff](evidence/diffs/C018_a6e42ea.diff)

[Previous saved controller snapshot](evidence/versions/C017_e19f0c8_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2a47316..9a8325b 100644
--- a/approach.py
+++ b/approach.py
@@ -192,7 +192,22 @@ class GeneratedApproach:
  192    192          self.carry = None
  193    193          self.stuck_carry = 0
  194    194  
  195        -    def _grasp_x(self, b, others, rng=None, pref=None):
         195 +    def _union(self, objs):
         196 +        x0 = min(o["x"] for o in objs)
         197 +        y0 = min(o["y"] for o in objs)
         198 +        x1 = max(o["x"] + o["w"] for o in objs)
         199 +        y1 = max(o["y"] + o["h"] for o in objs)
         200 +        return dict(name=objs[0]["name"], x=x0, y=y0, w=x1 - x0, h=y1 - y0)
         201 +
         202 +    def _cograsp(self, tgt, gx, others):
         203 +        """Objects that will be sucked up together with tgt when grasping at gx."""
         204 +        half = self.robot["gh"] / 2.0
         205 +        btop = tgt["y"] + tgt["h"]
         206 +        return [o for o in others if o["name"] != self.block["name"]
         207 +                and btop - 0.016 <= o["y"] + o["h"] <= btop + 1e-4
         208 +                and o["x"] < gx + half and o["x"] + o["w"] > gx - half]
         209 +
         210 +    def _grasp_x(self, b, others, rng=None, pref=None, allow_group=False):
  196    211          half = self.robot["gh"] / 2.0
  197    212          lo, hi = b["x"] + 0.012 - half, b["x"] + b["w"] - 0.012 + half
  198    213          if rng is not None:
@@ -211,13 +226,21 @@ class GeneratedApproach:
  211    226          R = self.robot["r"] + 0.005
  212    227          btop = b["y"] + b["h"]
  213    228          self.grasp_conflict = None
         229 +        self.grasp_group = []
         230 +        bname = self.block["name"]
  214    231          for x in cands:
  215    232              if x < X_MIN or x > X_MAX:
  216    233                  continue
  217    234              ok = True
         235 +            group = []
  218    236              for o in others:
  219        -                if o["y"] + o["h"] > btop - 0.02 and o["x"] < x + half + 0.004 \
         237 +                otop = o["y"] + o["h"]
         238 +                if otop > btop - 0.02 and o["x"] < x + half + 0.004 \
  220    239                          and o["x"] + o["w"] > x - half - 0.004:
         240 +                    if allow_group and o["name"] != bname and btop - 0.009 <= otop <= btop + 1e-4 \
         241 +                            and o["x"] < x + half - 0.004 and o["x"] + o["w"] > x - half + 0.004:
         242 +                        group.append(o)
         243 +                        continue
  221    244                      ok = False
  222    245                      if self.grasp_conflict is None:
  223    246                          self.grasp_conflict = o
@@ -235,6 +258,7 @@ class GeneratedApproach:
  235    258                          self.grasp_conflict = o
  236    259                      break
  237    260              if ok:
         261 +                self.grasp_group = group
  238    262                  return x
  239    263          return None
  240    264  
@@ -357,7 +381,9 @@ class GeneratedApproach:
  357    381          else:
  358    382              tgt = self.block
  359    383          gx = None
         384 +        tried = []
  360    385          for _ in range(10):
         386 +            tried.append(tgt)
  361    387              others = [b for n, b in movable.items() if n != tgt["name"]]
  362    388              if tgt["name"] == self.block["name"]:
  363    389                  bb = self.block
@@ -368,6 +394,15 @@ class GeneratedApproach:
  368    394              if gx is not None or self.grasp_conflict is None:
  369    395                  break
  370    396              tgt = self.grasp_conflict
         397 +        if gx is None:
         398 +            for t in tried:
         399 +                if t["name"] == self.block["name"]:
         400 +                    continue
         401 +                oth = [b for n, b in movable.items() if n != t["name"]]
         402 +                g = self._grasp_x(t, oth, allow_group=True)
         403 +                if g is not None:
         404 +                    tgt, gx = t, g
         405 +                    break
  371    406          n_att = self.attempts.get(tgt["name"], 0)
  372    407          self.attempts[tgt["name"]] = n_att + 1
  373    408          if n_att >= 3:
@@ -387,6 +422,11 @@ class GeneratedApproach:
  387    422          is_block = tgt["name"] == self.block["name"]
  388    423          gy = tgt["y"] + tgt["h"] + self._grip_off() + GAP
  389    424          gpos = (gx, gy)
         425 +        group = [] if is_block else self._cograsp(tgt, gx, others)
         426 +        gnames = [tgt["name"]] + [o["name"] for o in group]
         427 +        others = [b for b in others if b["name"] not in gnames]
         428 +        tgt0 = tgt
         429 +        tgt = self._union([tgt0] + group)
  390    430          off = gy - tgt["y"]
  391    431          gx_rel = gx - tgt["x"]
  392    432          if is_block and stage and tgt["name"] == self.block["name"]:
@@ -416,8 +456,8 @@ class GeneratedApproach:
  416    456          px = min(max(dest_x + gx_rel, X_MIN), X_MAX)
  417    457          py = dest_y + off + PLACE_GAP
  418    458          # approach path (nothing carried)
  419        -        p1 = self._plan_path((rx, ry, self.robot["arm"]), gpos, others + [tgt], None,
  420        -                             special_margin={tgt["name"]: 0.0})
         459 +        p1 = self._plan_path((rx, ry, self.robot["arm"]), gpos, others + [tgt0] + group, None,
         460 +                             special_margin={n: 0.0 for n in gnames})
  421    461          carried = (tgt["x"] - gx, tgt["x"] + tgt["w"] - gx, tgt["y"] - gy, tgt["y"] + tgt["h"] - gy)
  422    462          p2 = self._plan_path(gpos, (px, py), others, carried)
  423    463          segs = []
@@ -428,7 +468,7 @@ class GeneratedApproach:
  428    468              segs.append(dict(x=w[0], y=w[1], a=w[2], vac=1, kind="carry"))
  429    469          # release on the final step of the carry
  430    470          segs[-1]["release_last"] = not is_block
  431        -        self.carry = dict(name=tgt["name"], px=px, py=py, release=not is_block,
         471 +        self.carry = dict(name=tgt["name"], names=gnames, px=px, py=py, release=not is_block,
  432    472                            rel=(tgt["x"] - gx, tgt["y"] - gy))
  433    473          return segs
  434    474  
@@ -445,7 +485,9 @@ class GeneratedApproach:
  445    485          sh = self.robot["arm_max"] - self.robot["arm"]
  446    486          if abs(o["x"] - rx - c["rel"][0]) > 2e-3 or abs(o["y"] - ry - sh - c["rel"][1]) > 2e-3:
  447    487              return None
  448        -        others = [b for n, b in movable.items() if n != o["name"]]
         488 +        names = c.get("names", [c["name"]])
         489 +        others = [b for n, b in movable.items() if n not in names]
         490 +        o = self._union([movable[n] for n in names if n in movable])
  449    491          carried = (o["x"] - rx, o["x"] + o["w"] - rx, o["y"] - ry - sh, o["y"] + o["h"] - ry - sh)
  450    492          p = self._plan_path((rx, ry, self.robot["arm"]), (c["px"], c["py"]), others, carried)
  451    493          segs = [dict(x=w[0], y=w[1], a=w[2], vac=1, kind="carry") for w in p[1:]]
```

</details>

<a id="C019"></a>
### C019 · add debug/probe scripts

Commit `c4cf81824e979a872ffc29e19b75787faeb06856`; parents: a6e42eaef26b68bbb74b2aec5e25e7be29adb91b. Recorded author date: 2026-09-28T17:18:11+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0918](01_timeline.md#E0918): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C019_c4cf818.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/dbg5.py b/dbg5.py
new file mode 100644
index 0000000..852b88d
--- /dev/null
+++ b/dbg5.py
@@ -0,0 +1,16 @@
           1 +import sys
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed, count, T, N = map(int, sys.argv[1:5])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +ap.reset(obs, info)
          10 +for t in range(T + N):
          11 +    a = ap.get_action(obs)
          12 +    if t >= T:
          13 +        r = ap.robot
          14 +        print(t, 'rob', round(r['x'],4), round(r['y'],4), round(r['arm'],4), r['vac'], 'act', np.round(a,4), 'wp', ap.plan[0] if ap.plan else None)
          15 +    obs, rew, term, trunc, info = env.step(a)
          16 +    if term: print('term', t); break
diff --git a/probe_at.py b/probe_at.py
new file mode 100644
index 0000000..6666eb7
--- /dev/null
+++ b/probe_at.py
@@ -0,0 +1,16 @@
           1 +import sys, json
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +seed, count, T = map(int, sys.argv[1:4]); acts = json.loads(sys.argv[4])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +ap.reset(obs, info)
          10 +for t in range(T):
          11 +    obs, *_ = env.step(ap.get_action(obs))
          12 +for a in acts:
          13 +    obs, *_ = env.step(np.array(a, dtype=np.float32))
          14 +    ap._parse(obs); r = ap.robot
          15 +    print(a, 'rob', round(r['x'],4), round(r['y'],4), round(r['arm'],4), r['vac'])
          16 +for n,b in ap._all_movable().items(): print(n, {k:round(v,3) for k,v in b.items() if k!='name'})
diff --git a/probe_suck.py b/probe_suck.py
new file mode 100644
index 0000000..6d94df2
--- /dev/null
+++ b/probe_suck.py
@@ -0,0 +1,20 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env = make_env()
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           6 +for gap in [0.004, 0.008, 0.012, 0.016, 0.02, 0.03]:
           7 +    obs, info = env.reset(seed=2104, options={'object_count': 4})
           8 +    obs, *_ = env.step(np.array([0,0,0,0.1,0], dtype=np.float32))
           9 +    ap._parse(obs); o = ap.obst['obstruction0']
          10 +    tx = o['x'] + o['w']/2
          11 +    ty = o['y'] + o['h'] + gap + 0.005 + 0.2
          12 +    for _ in range(60):
          13 +        ap._parse(obs); rx, ry = ap.robot['x'], ap.robot['y']
          14 +        if abs(tx-rx) < 1e-5 and abs(ty-ry) < 1e-5: break
          15 +        dx, dy = np.clip(tx-rx, -0.05, 0.05), np.clip(ty-ry, -0.05, 0.05)
          16 +        obs, *_ = env.step(np.array([dx,dy,0,0,0], dtype=np.float32))
          17 +    obs, *_ = env.step(np.array([0,0,0,0,1], dtype=np.float32))
          18 +    obs, *_ = env.step(np.array([0,0.05,0,0,1], dtype=np.float32))
          19 +    ap._parse(obs)
          20 +    print('gap', gap, 'robot y', round(ap.robot['y']-ty,4), 'obj y moved', round(ap.obst['obstruction0']['y']-o['y'],4))
```

</details>

