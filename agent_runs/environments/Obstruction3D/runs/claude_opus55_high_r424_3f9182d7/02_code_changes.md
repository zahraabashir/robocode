# Obstruction3D · claude-opus-5-5 · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `6188fcc` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `62c9e40` | Initial kinematics (kortex FK/IK), exploration scripts, skeleton pick-place approach | approach.py, calib_0.py, dbg/approach.py, dbg/cfg.json, dbg/kin.py, explore0.py, explore1.py, explore2.py, explore3.py, explore4.py, explore5.py, explore6.py, explore7.py, explore… | [E0146](01_timeline.md#E0146) |
| [C003](#C003) · `d6db4fc` | Use calibrated kinematics (arm offset, TCP=0.12), grasp/place via grasp_tf, release retries | approach.py, calib_1.py, calib_10.py, calib_11.py, calib_12.py, calib_13.py, calib_14.py, calib_15.py, calib_2.py, calib_3.py, calib_4.py, calib_5.py, calib_6.py, calib_7.py, cali… | [E0422](01_timeline.md#E0422) |
| [C004](#C004) · `ae6fc4b` | Cartesian straight-line waypoint execution | approach.py, trace.py | [E0434](01_timeline.md#E0434) |
| [C005](#C005) · `03653b7` | fix waypoint index tracking | approach.py | [E0439](01_timeline.md#E0439) |
| [C006](#C006) · `18af7cc` | grasp height centre+0.035 | approach.py, gsweep.py | [E0489](01_timeline.md#E0489) |
| [C007](#C007) · `81d1da0` | finger clearance-aware grasp yaw, place yaw from grasp_tf | approach.py | [E0506](01_timeline.md#E0506) |
| [C008](#C008) · `0611c4d` | fine small steps near objects (grasp descent, lift, place) | approach.py, esc.py, show.py | [E0540](01_timeline.md#E0540) |
| [C009](#C009) · `9816a62` | replan with held object, bad spot memory, narrower spot range | approach.py, trace2.py | [E0552](01_timeline.md#E0552) |
| [C010](#C010) · `8e6d343` | choose most accessible obstruction first; failure counts | approach.py, show2.py, test_count.py, trace2.py | [E0612](01_timeline.md#E0612) |
| [C011](#C011) · `3206016` | prefer axis-aligned grasps strongly | approach.py | [E0646](01_timeline.md#E0646) |
| [C012](#C012) · `f7501d3` | grasp dz 0.04 | approach.py | [E0674](01_timeline.md#E0674) |
| [C013](#C013) · `0989e5b` | revert to 60/60 version (access/aligned changes didn&#x27;t help) | approach.py | [E0687](01_timeline.md#E0687) |
| [C014](#C014) · `50044fb` | in-place grasp depth retries | approach.py | [E0707](01_timeline.md#E0707) |
| [C015](#C015) · `71151ae` | retry rejected coarse moves with fine steps | approach.py | [E0778](01_timeline.md#E0778) |
| [C016](#C016) · `c5d29bf` | count approach rejections as grasp failures, cycle yaw candidates, deprioritize failing objects | approach.py | [E0813](01_timeline.md#E0813) |
| [C017](#C017) · `1731ff2` | target grasp yaw considers finger clearance at the place pose | approach.py | [E0873](01_timeline.md#E0873) |
| [C018](#C018) · `99399cd` | release-failure fallback: re-place elsewhere, clear near-region obstructions | approach.py | [E0883](01_timeline.md#E0883) |
| [C019](#C019) · `9c018b1` | finger clearance: only objects reaching fingertip height matter | approach.py | [E0918](01_timeline.md#E0918) |
| [C020](#C020) · `104631d` | prefer blocking obstructions with a clear aligned grasp | approach.py | [E0926](01_timeline.md#E0926) |
| [C021](#C021) · `c6d49bb` | restore fingertip clearance threshold | approach.py, res1.txt, res2.txt, res3.txt, show3.py | [E0948](01_timeline.md#E0948) |
| [C022](#C022) · `98402a6` | per-object yaw cycling; skip depth retries when descent blocked high | approach.py, clr.py, res3.txt | [E0966](01_timeline.md#E0966) |
| [C023](#C023) · `96188c9` | dedupe grasp yaw candidates modulo pi | approach.py, res4.txt | [E1032](01_timeline.md#E1032) |
| [C024](#C024) · `b927ada` | coarse approach/lift/place moves with fine fallback on rejection | approach.py, res5.txt, timeit.py | [E1113](01_timeline.md#E1113) |
| [C025](#C025) · `1fc5850` | drop intermediate waypoints | approach.py | [E1136](01_timeline.md#E1136) |
| [C026](#C026) · `73e7580` | dynamic transit heights | approach.py | [E1153](01_timeline.md#E1153) |
| [C027](#C027) · `9d0edff` | fine mode only for first 6 waypoints | approach.py | [E1178](01_timeline.md#E1178) |
| [C028](#C028) · `f0d925a` | joint-space interpolation for high transits | approach.py | [E1199](01_timeline.md#E1199) |
| [C029](#C029) · `c30325a` | test results/scripts | res6.txt, res7.txt | [E1309](01_timeline.md#E1309) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `6188fccd811088b0f02f75fd3551bc378e15dd50`; parents: none (initial snapshot). Recorded author date: 2026-09-30T20:08:16+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_6188fcc.diff)

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
index 0000000..1d210ef
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "4d6ba86a39283a38de5d4ce877dbd2f1", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Initial kinematics (kortex FK/IK), exploration scripts, skeleton pick-place approach

Commit `62c9e4056ea3130b5ffab63f9d4363c78985eacd`; parents: 6188fccd811088b0f02f75fd3551bc378e15dd50. Recorded author date: 2026-09-30T20:20:32+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0146](01_timeline.md#E0146): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_62c9e40_approach.py) · [Exact all-file diff](evidence/diffs/C002_62c9e40.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..2b71c5c
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,127 @@
           1 +import numpy as np
           2 +from kin import fk, ik, down_R
           3 +
           4 +JF = ['joint_%d' % i for i in range(1, 8)]
           5 +MAXD = 0.19
           6 +SAFE_Z = 0.33       # EE transit height
           7 +GRASP_DZ = 0.14     # EE height above object center when grasping (calibrate)
           8 +TABLE_Z = 0.075
           9 +
          10 +
          11 +def _pose(s, o):
          12 +    return np.array([s.get(o, 'pose_x'), s.get(o, 'pose_y'), s.get(o, 'pose_z')])
          13 +
          14 +
          15 +def _he(s, o):
          16 +    return np.array([s.get(o, 'half_extent_x'), s.get(o, 'half_extent_y'), s.get(o, 'half_extent_z')])
          17 +
          18 +
          19 +def _yaw(s, o):
          20 +    qx, qy, qz, qw = [s.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]
          21 +    return np.arctan2(2 * (qw * qz + qx * qy), 1 - 2 * (qy * qy + qz * qz))
          22 +
          23 +
          24 +class GeneratedApproach:
          25 +    def __init__(self, action_space, observation_space, primitives):
          26 +        self.action_space = action_space
          27 +
          28 +    # ------------------------------------------------------------------
          29 +    def reset(self, state, info):
          30 +        self.queue = []       # list of ('move', pos, yaw) | ('grip', val, n)
          31 +        self.phase = 'plan'
          32 +        self.qtarget = None
          33 +        self.stuck = 0
          34 +        self.last_q = None
          35 +
          36 +    def _robot(self, s):
          37 +        r = s.get_object_from_name('robot')
          38 +        q = np.array([s.get(r, f) for f in JF])
          39 +        base = (s.get(r, 'pos_base_x'), s.get(r, 'pos_base_y'), s.get(r, 'pos_base_rot'))
          40 +        return r, q, base
          41 +
          42 +    # ------------------------------------------------------------------
          43 +    def _overlaps(self, s, o, reg):
          44 +        p, h = _pose(s, o), _he(s, o)
          45 +        rp, rh = _pose(s, reg), _he(s, reg)
          46 +        return (abs(p[0] - rp[0]) < h[0] + rh[0] + 0.005 and
          47 +                abs(p[1] - rp[1]) < h[1] + rh[1] + 0.005)
          48 +
          49 +    def _free_spot(self, s, obj, avoid):
          50 +        """Find a free table spot for obj away from the objects in avoid."""
          51 +        h = _he(s, obj)
          52 +        best, bestd = None, -1
          53 +        for x in np.linspace(0.05, 0.35, 13):
          54 +            for y in np.linspace(-0.3, 0.3, 25):
          55 +                dmin = 1e9
          56 +                for o in avoid:
          57 +                    p, oh = _pose(s, o), _he(s, o)
          58 +                    dx = abs(x - p[0]) - (h[0] + oh[0])
          59 +                    dy = abs(y - p[1]) - (h[1] + oh[1])
          60 +                    dmin = min(dmin, max(dx, dy))
          61 +                if dmin > 0.06:
          62 +                    # prefer close to robot centre line
          63 +                    score = dmin - 0.2 * abs(y)
          64 +                    if best is None or score > bestd:
          65 +                        best, bestd = (x, y), score
          66 +                elif best is None and dmin > bestd:
          67 +                    bestd = dmin
          68 +                    best = (x, y)
          69 +        return np.array(best)
          70 +
          71 +    def _plan_pick_place(self, s, obj, place_xy, place_z_center):
          72 +        p = _pose(s, obj)
          73 +        yaw = _yaw(s, obj)
          74 +        q = []
          75 +        q.append(('grip', 1.0, 1))
          76 +        q.append(('move', np.array([p[0], p[1], SAFE_Z]), yaw))
          77 +        q.append(('move', np.array([p[0], p[1], p[2] + GRASP_DZ]), yaw))
          78 +        q.append(('grip', -1.0, 2))
          79 +        q.append(('move', np.array([p[0], p[1], SAFE_Z]), yaw))
          80 +        q.append(('move', np.array([place_xy[0], place_xy[1], SAFE_Z]), yaw))
          81 +        q.append(('move', np.array([place_xy[0], place_xy[1], place_z_center + GRASP_DZ + 0.003]), yaw))
          82 +        q.append(('grip', 1.0, 2))
          83 +        q.append(('move', np.array([place_xy[0], place_xy[1], SAFE_Z]), yaw))
          84 +        return q
          85 +
          86 +    def _plan(self, s):
          87 +        reg = s.get_object_from_name('target_region')
          88 +        tb = s.get_object_from_name('target_block')
          89 +        cubes = [s.get_object_from_name(n) for n in s.get_object_names()
          90 +                 if n.startswith('obstruction')]
          91 +        blocking = [o for o in cubes if self._overlaps(s, o, reg)]
          92 +        if blocking:
          93 +            o = blocking[0]
          94 +            others = [c for c in cubes if c.name != o.name] + [reg, tb]
          95 +            spot = self._free_spot(s, o, others)
          96 +            return self._plan_pick_place(s, o, spot, TABLE_Z + _he(s, o)[2])
          97 +        rp = _pose(s, reg)
          98 +        z = rp[2] + _he(s, reg)[2] + _he(s, tb)[2]
          99 +        return self._plan_pick_place(s, tb, rp[:2], z)
         100 +
         101 +    # ------------------------------------------------------------------
         102 +    def get_action(self, s):
         103 +        a = np.zeros(11, dtype=np.float32)
         104 +        r, q, base = self._robot(s)
         105 +        if not self.queue:
         106 +            self.queue = self._plan(s)
         107 +            self.qtarget = None
         108 +        cmd = self.queue[0]
         109 +        if cmd[0] == 'grip':
         110 +            a[10] = cmd[1]
         111 +            n = cmd[2] - 1
         112 +            if n <= 0:
         113 +                self.queue.pop(0)
         114 +            else:
         115 +                self.queue[0] = ('grip', cmd[1], n)
         116 +            return a
         117 +        # move
         118 +        if self.qtarget is None:
         119 +            qt, ok = ik(base, q, cmd[1], down_R(cmd[2]))
         120 +            self.qtarget = qt
         121 +        d = self.qtarget - q
         122 +        if np.max(np.abs(d)) < 1e-4:
         123 +            self.queue.pop(0)
         124 +            self.qtarget = None
         125 +            return self.get_action(s) if self.queue else a
         126 +        a[3:10] = np.clip(d, -MAXD, MAXD)
         127 +        return a
diff --git a/calib_0.py b/calib_0.py
new file mode 100644
index 0000000..3519bf2
--- /dev/null
+++ b/calib_0.py
@@ -0,0 +1,8 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env()
           4 +obs,info=env.reset(seed=1)
           5 +print(type(obs)); print(env._primitive_manifest)
           6 +for o in obs: print(o, [ (f,round(obs.get(o,f),4)) for f in env.observation_space.type_features[o.type]] if hasattr(env.observation_space,'type_features') else '')
           7 +print(info)
           8 +s=env.get_state(); print(type(s))
diff --git a/dbg/approach.py b/dbg/approach.py
new file mode 100644
index 0000000..ea4e81b
--- /dev/null
+++ b/dbg/approach.py
@@ -0,0 +1,17 @@
           1 +import numpy as np, json, os
           2 +from kin import fk, ik, down_R
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +CFG=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cfg.json')))
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives): pass
           7 +    def reset(self, state, info):
           8 +        self.t=0
           9 +    def get_action(self, s):
          10 +        r=s.get_object_from_name('robot')
          11 +        tb=s.get_object_from_name(CFG.get('obj','target_block'))
          12 +        q=np.array([s.get(r,f) for f in F]); base=(s.get(r,'pos_base_x'),s.get(r,'pos_base_y'),s.get(r,'pos_base_rot'))
          13 +        bx,by,bz=[s.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
          14 +        self.t+=1
          15 +        a=np.zeros(11,dtype=np.float32)
          16 +        qt,ok=ik(base,q,np.array([bx+CFG['dx'],by+CFG['dy'],bz+CFG['dz']]),down_R(CFG['yaw']))
          17 +        a[3:10]=np.clip(qt-q,-0.19,0.19); return a
diff --git a/dbg/cfg.json b/dbg/cfg.json
new file mode 100644
index 0000000..fca0bb6
--- /dev/null
+++ b/dbg/cfg.json
@@ -0,0 +1 @@
           1 +{"obj":"target_region","dx":0,"dy":0,"dz":0.237,"yaw":0}
diff --git a/dbg/kin.py b/dbg/kin.py
new file mode 100644
index 0000000..49670b8
--- /dev/null
+++ b/dbg/kin.py
@@ -0,0 +1,73 @@
           1 +import numpy as np
           2 +PI = np.pi
           3 +
           4 +def _rpy(r, p, y):
           5 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           6 +    return np.array([[cy*cp, cy*sp*sr-sy*cr, cy*sp*cr+sy*sr],
           7 +                     [sy*cp, sy*sp*sr+cy*cr, sy*sp*cr-cy*sr],
           8 +                     [-sp, cp*sr, cp*cr]])
           9 +
          10 +def _T(xyz, R):
          11 +    M = np.eye(4); M[:3, :3] = R; M[:3, 3] = xyz; return M
          12 +
          13 +def _rz(q):
          14 +    c, s = np.cos(q), np.sin(q)
          15 +    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
          16 +
          17 +_J = [((0, 0, 0.15643), (PI, 0, 0)), ((0, 0.005375, -0.12838), (PI/2, 0, 0)),
          18 +      ((0, -0.21038, -0.006375), (-PI/2, 0, 0)), ((0, 0.006375, -0.21038), (PI/2, 0, 0)),
          19 +      ((0, -0.20843, -0.006375), (-PI/2, 0, 0)), ((0, 0.00017505, -0.10593), (PI/2, 0, 0)),
          20 +      ((0, -0.10593, -0.00017505), (-PI/2, 0, 0))]
          21 +_JT = [_T(xyz, _rpy(*r)) for xyz, r in _J]
          22 +_EE = _T((0, 0, -0.061525), _rpy(PI, 0, 0))
          23 +
          24 +BASE_Z = 0.0
          25 +TOOL = 0.0
          26 +
          27 +def fk(base, q, tool=None):
          28 +    if tool is None:
          29 +        tool = TOOL
          30 +    bx, by, br = base
          31 +    M = _T((bx, by, BASE_Z), _rz(br))
          32 +    for Jt, qi in zip(_JT, q):
          33 +        M = M @ Jt @ _T((0, 0, 0), _rz(qi))
          34 +    M = M @ _EE
          35 +    if tool:
          36 +        M = M @ _T((0, 0, tool), np.eye(3))
          37 +    return M
          38 +
          39 +def _err(M, pos, R):
          40 +    ep = pos - M[:3, 3]
          41 +    Re = R @ M[:3, :3].T
          42 +    # rotation error as axis-angle (small-angle approx ok via skew)
          43 +    eo = 0.5 * np.array([Re[2, 1]-Re[1, 2], Re[0, 2]-Re[2, 0], Re[1, 0]-Re[0, 1]])
          44 +    return np.concatenate([ep, eo])
          45 +
          46 +def ik(base, q0, pos, R, iters=200, tol=1e-4, rot_w=0.3, tool=None):
          47 +    q = np.array(q0, dtype=float)
          48 +    W = np.array([1, 1, 1, rot_w, rot_w, rot_w])
          49 +    for _ in range(iters):
          50 +        M = fk(base, q, tool)
          51 +        e = _err(M, pos, R) * W
          52 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < tol*3:
          53 +            return q, True
          54 +        Jm = np.zeros((6, 7))
          55 +        h = 1e-6
          56 +        for i in range(7):
          57 +            dq = q.copy(); dq[i] += h
          58 +            Jm[:, i] = (_err(M, pos, R) - _err(fk(base, dq, tool), pos, R)) * W / h
          59 +        lam = 1e-3
          60 +        d = Jm.T @ np.linalg.solve(Jm @ Jm.T + lam*np.eye(6), e)
          61 +        n = np.max(np.abs(d))
          62 +        if n > 0.3:
          63 +            d *= 0.3 / n
          64 +        q = q + d
          65 +    M = fk(base, q, tool)
          66 +    e = _err(M, pos, R)
          67 +    return q, bool(np.linalg.norm(e[:3]) < 1e-3 and np.linalg.norm(e[3:]) < 1e-2)
          68 +
          69 +def down_R(yaw):
          70 +    # gripper z axis pointing down, x axis direction by yaw
          71 +    c, s = np.cos(yaw), np.sin(yaw)
          72 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          73 +    return np.stack([x, y, z], axis=1)
diff --git a/explore0.py b/explore0.py
new file mode 100644
index 0000000..0dcd79c
--- /dev/null
+++ b/explore0.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +for seed in [0,1]:
           5 +    obs, info = env.reset(seed=seed)
           6 +    print("seed",seed, info)
           7 +    for name in sorted(obs.get_object_names()):
           8 +        o = obs.get_object_from_name(name)
           9 +        feats = env.observation_space.type_features[o.type] if hasattr(o,'type') else None
          10 +        print(name, o, {f: round(obs.get(o,f),4) for f in feats})
          11 +env.close()
diff --git a/explore1.py b/explore1.py
new file mode 100644
index 0000000..9af8db5
--- /dev/null
+++ b/explore1.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +r = obs.get_object_from_name('robot')
           6 +F = ['pos_base_x','pos_base_y','pos_base_rot','joint_1','joint_2','joint_3','joint_4','joint_5','joint_6','joint_7','finger_state','grasp_active']
           7 +def show(o): return [round(o.get(r,f),4) for f in F]
           8 +print(show(obs))
           9 +for a in [[0.1,0,0,0,0,0,0,0,0,0,0],[0,0.1,0,0,0,0,0,0,0,0,0],[0,0,0.1,0,0,0,0,0,0,0,0],[0,0,0,0.3,0.05,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,-1],[0,0,0,0,0,0,0,0,0,0,1]]:
          10 +    obs, rew, term, trunc, info = env.step(np.array(a,dtype=np.float32))
          11 +    print(a, rew, term, trunc, info, show(obs))
          12 +env.close()
diff --git a/explore2.py b/explore2.py
new file mode 100644
index 0000000..0af6f7f
--- /dev/null
+++ b/explore2.py
@@ -0,0 +1,32 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +env = make_env()
           5 +obs, info = env.reset(seed=1)
           6 +r = obs.get_object_from_name('robot')
           7 +def getq(o): return np.array([o.get(r,f) for f in F])
           8 +base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
           9 +q=getq(obs)
          10 +M=kin.fk(base,q); print("init ee",M[:3,3], M[:3,2])
          11 +yaw=np.arctan2(M[1,0],M[0,0])
          12 +def goto(pos, yaw):
          13 +    global obs,q
          14 +    qt,ok=kin.ik(base,q,np.array(pos),kin.down_R(yaw))
          15 +    if not ok: print("ik fail",pos); return False
          16 +    while True:
          17 +        d=qt-q; 
          18 +        if np.max(np.abs(d))<1e-6: return True
          19 +        d=np.clip(d,-0.19,0.19)
          20 +        a=np.zeros(11,dtype=np.float32); a[3:10]=d
          21 +        obs,_,_,_,_=env.step(a); qn=getq(obs)
          22 +        if np.allclose(qn,q): print("rejected at", kin.fk(base,q)[:3,3]); return False
          23 +        q=qn
          24 +x,y=0.25,-0.2
          25 +z=0.34
          26 +goto([x,y,z],yaw)
          27 +print("at",kin.fk(base,q)[:3,3])
          28 +while z>-0.1:
          29 +    z-=0.005
          30 +    if not goto([x,y,z],yaw): break
          31 +print("final ee", kin.fk(base,q)[:3,3])
          32 +env.close()
diff --git a/explore3.py b/explore3.py
new file mode 100644
index 0000000..66ad09f
--- /dev/null
+++ b/explore3.py
@@ -0,0 +1,41 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin, sys
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +env = make_env()
           5 +obs, info = env.reset(seed=1)
           6 +r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
           7 +def getq(o): return np.array([o.get(r,f) for f in F])
           8 +base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
           9 +q=getq(obs)
          10 +def step(a):
          11 +    global obs,q
          12 +    obs,_,_,_,_=env.step(np.array(a,dtype=np.float32)); q=getq(obs)
          13 +def goto(pos, yaw):
          14 +    global obs,q
          15 +    qt,ok=kin.ik(base,q,np.array(pos),kin.down_R(yaw))
          16 +    if not ok: print("ik fail",pos); return False
          17 +    while True:
          18 +        d=qt-q
          19 +        if np.max(np.abs(d))<1e-6: return True
          20 +        d=np.clip(d,-0.19,0.19)
          21 +        a=np.zeros(11); a[3:10]=d
          22 +        q0=q.copy(); step(a)
          23 +        if np.allclose(q0,q): print("rejected at", kin.fk(base,q)[:3,3]); return False
          24 +bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
          25 +hx,hy=obs.get(tb,'half_extent_x'),obs.get(tb,'half_extent_y')
          26 +print("block",bx,by,bz,hx,hy)
          27 +off=float(sys.argv[1]); yaw=float(sys.argv[2])
          28 +step([0]*10+[1])
          29 +goto([bx,by,bz+0.25],yaw)
          30 +for zz in np.arange(bz+0.25,bz+off-1e-9,-0.01):
          31 +    if not goto([bx,by,zz],yaw): break
          32 +goto([bx,by,bz+off],yaw)
          33 +print("ee",kin.fk(base,q)[:3,3], "finger",obs.get(r,'finger_state'))
          34 +for i in range(3):
          35 +    step([0]*10+[-1])
          36 +    print("after close: finger",obs.get(r,'finger_state'),"grasp",obs.get(r,'grasp_active'),obs.get(tb,'grasp_active'),
          37 +      [round(obs.get(r,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
          38 +goto([bx,by,bz+0.25],yaw)
          39 +print("block now",[round(obs.get(tb,f),4) for f in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']])
          40 +M=kin.fk(base,q); print("ee",M[:3,3]); 
          41 +env.close()
diff --git a/explore4.py b/explore4.py
new file mode 100644
index 0000000..615f35f
--- /dev/null
+++ b/explore4.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin, sys
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +env = make_env()
           5 +res=[]
           6 +for (x,y,yaw) in [(0.25,-0.2,0),(0.3,0.0,0),(0.1,-0.25,0.7),(0.35,0.3,0),(0.2,0.1,1.5)]:
           7 +    obs, info = env.reset(seed=1)
           8 +    r = obs.get_object_from_name('robot')
           9 +    getq=lambda o: np.array([o.get(r,f) for f in F])
          10 +    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          11 +    q=getq(obs)
          12 +    z=0.34; stop=None
          13 +    while z>0.1 and stop is None:
          14 +        qt,ok=kin.ik(base,q,np.array([x,y,z]),kin.down_R(yaw))
          15 +        while np.max(np.abs(qt-q))>1e-6:
          16 +            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
          17 +            obs,_,_,_,_=env.step(a); qn=getq(obs)
          18 +            if np.allclose(qn,q): stop=kin.fk(base,q)[:3,3]; break
          19 +            q=qn
          20 +        z-=0.004
          21 +    print(x,y,yaw,"stop",stop)
          22 +env.close()
diff --git a/explore5.py b/explore5.py
new file mode 100644
index 0000000..ce521ed
--- /dev/null
+++ b/explore5.py
@@ -0,0 +1,25 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin, sys
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +env = make_env()
           5 +yaw=float(sys.argv[1])
           6 +for dz in [0.13,0.15,0.17,0.19,0.21]:
           7 +  for dx,dy in [(0,0),(0.02,0),(-0.02,0),(0,0.02),(0,-0.02)]:
           8 +    obs, info = env.reset(seed=1)
           9 +    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
          10 +    getq=lambda o: np.array([o.get(r,f) for f in F])
          11 +    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          12 +    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
          13 +    q=getq(obs); stop=False
          14 +    for z in list(np.arange(bz+0.3,bz+dz,-0.01))+[bz+dz]:
          15 +        qt,ok=kin.ik(base,q,np.array([bx+dx,by+dy,z]),kin.down_R(yaw))
          16 +        while np.max(np.abs(qt-q))>1e-6:
          17 +            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
          18 +            obs,_,_,_,_=env.step(a); qn=getq(obs)
          19 +            if np.allclose(qn,q): stop=True; break
          20 +            q=qn
          21 +        if stop: break
          22 +    a=np.zeros(11,dtype=np.float32); a[10]=-1
          23 +    obs,_,_,_,_=env.step(a)
          24 +    print(dz,dx,dy,"blocked" if stop else "", "ee",np.round(kin.fk(base,q)[:3,3],3),"finger",obs.get(r,'finger_state'),"grasp",obs.get(r,'grasp_active'))
          25 +env.close()
diff --git a/explore6.py b/explore6.py
new file mode 100644
index 0000000..e6f40fb
--- /dev/null
+++ b/explore6.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=1)
           5 +r = obs.get_object_from_name('robot')
           6 +F=env.observation_space.type_features[r.type]
           7 +prev=np.array([obs.get(r,f) for f in F])
           8 +for g in [-1,-1,-1,1,1,1,-0.7,0.7]:
           9 +    a=np.zeros(11,dtype=np.float32); a[10]=g
          10 +    obs,rew,te,tr,info=env.step(a)
          11 +    cur=np.array([obs.get(r,f) for f in F])
          12 +    print(g, {f:(round(p,4),round(c,4)) for f,p,c in zip(F,prev,cur) if abs(p-c)>1e-9})
          13 +    prev=cur
          14 +env.close()
diff --git a/explore7.py b/explore7.py
new file mode 100644
index 0000000..c967288
--- /dev/null
+++ b/explore7.py
@@ -0,0 +1,25 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin, sys
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +env = make_env()
           5 +for yaw in [0, 1.5708]:
           6 +  for dx,dy in [(0,0),(-0.02,0),(0.02,0),(0,0.02),(0,-0.02),(-0.035,0),(0,-0.04)]:
           7 +    obs, info = env.reset(seed=1)
           8 +    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
           9 +    getq=lambda o: np.array([o.get(r,f) for f in F])
          10 +    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          11 +    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
          12 +    q=getq(obs); stop=False
          13 +    z=bz+0.3
          14 +    while not stop and z>0.2:
          15 +        qt,ok=kin.ik(base,q,np.array([bx+dx,by+dy,z]),kin.down_R(yaw))
          16 +        while np.max(np.abs(qt-q))>1e-6:
          17 +            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
          18 +            obs,_,_,_,_=env.step(a); qn=getq(obs)
          19 +            if np.allclose(qn,q): stop=True; break
          20 +            q=qn
          21 +        z-= 0.01 if z>bz+0.2 else 0.002
          22 +    a=np.zeros(11,dtype=np.float32); a[10]=-1
          23 +    obs,_,_,_,_=env.step(a)
          24 +    print(yaw,dx,dy,"ee",np.round(kin.fk(base,q)[:3,3],3),"grasp",obs.get(r,'grasp_active'),obs.get(tb,'grasp_active'))
          25 +env.close()
diff --git a/explore8.py b/explore8.py
new file mode 100644
index 0000000..9126017
--- /dev/null
+++ b/explore8.py
@@ -0,0 +1,27 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin, sys
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +env = make_env()
           5 +yaw=float(sys.argv[1]); dys=[float(v) for v in sys.argv[2].split(',')]
           6 +rng=np.arange(-0.08,0.081,0.02)
           7 +for dy in dys:
           8 +  row=[]
           9 +  for dx in rng:
          10 +    obs, info = env.reset(seed=1)
          11 +    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
          12 +    getq=lambda o: np.array([o.get(r,f) for f in F])
          13 +    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          14 +    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
          15 +    q=getq(obs); stop=False
          16 +    z=bz+0.22
          17 +    while not stop and z>0.22:
          18 +        qt,ok=kin.ik(base,q,np.array([bx+dx,by+dy,z]),kin.down_R(yaw))
          19 +        while np.max(np.abs(qt-q))>1e-6:
          20 +            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
          21 +            obs,_,_,_,_=env.step(a); qn=getq(obs)
          22 +            if np.allclose(qn,q): stop=True; break
          23 +            q=qn
          24 +        z-=0.005
          25 +    row.append(kin.fk(base,q)[2,3])
          26 +  print("dy=%.2f "%dy+" ".join("%.3f"%v for v in row), flush=True)
          27 +env.close()
diff --git a/explore9.py b/explore9.py
new file mode 100644
index 0000000..20a2dcf
--- /dev/null
+++ b/explore9.py
@@ -0,0 +1,28 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin, sys
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +env = make_env()
           5 +yaw=float(sys.argv[1]); axis=sys.argv[2]; other=float(sys.argv[3])
           6 +rng=np.arange(-0.12,0.121,0.02)
           7 +row=[]
           8 +for v in rng:
           9 +    dx,dy=(v,other) if axis=='x' else (other,v)
          10 +    obs, info = env.reset(seed=1)
          11 +    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
          12 +    getq=lambda o: np.array([o.get(r,f) for f in F])
          13 +    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          14 +    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
          15 +    q=getq(obs); stop=False
          16 +    z=bz+0.22
          17 +    while not stop and z>0.22:
          18 +        qt,ok=kin.ik(base,q,np.array([bx+dx,by+dy,z]),kin.down_R(yaw))
          19 +        if not ok: print("IKFAIL")
          20 +        while np.max(np.abs(qt-q))>1e-6:
          21 +            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
          22 +            obs,_,_,_,_=env.step(a); qn=getq(obs)
          23 +            if np.allclose(qn,q): stop=True; break
          24 +            q=qn
          25 +        z-=0.005
          26 +    row.append(kin.fk(base,q)[2,3])
          27 +print("yaw=%s axis=%s other=%s: "%(sys.argv[1],axis,other)+" ".join("%.3f"%v for v in row), flush=True)
          28 +env.close()
diff --git a/fk.py b/fk.py
new file mode 100644
index 0000000..1c903b5
--- /dev/null
+++ b/fk.py
@@ -0,0 +1,24 @@
           1 +import numpy as np
           2 +def rpy(r,p,y):
           3 +    cr,sr,cp,sp,cy,sy=np.cos(r),np.sin(r),np.cos(p),np.sin(p),np.cos(y),np.sin(y)
           4 +    return np.array([[cy*cp, cy*sp*sr-sy*cr, cy*sp*cr+sy*sr],[sy*cp, sy*sp*sr+cy*cr, sy*sp*cr-cy*sr],[-sp, cp*sr, cp*cr]])
           5 +def T(xyz, R):
           6 +    M=np.eye(4); M[:3,:3]=R; M[:3,3]=xyz; return M
           7 +def rz(q):
           8 +    c,s=np.cos(q),np.sin(q); return np.array([[c,-s,0],[s,c,0],[0,0,1]])
           9 +PI=np.pi
          10 +JOINTS=[((0,0,0.15643),(PI,0,0)),((0,0.005375,-0.12838),(PI/2,0,0)),((0,-0.21038,-0.006375),(-PI/2,0,0)),
          11 +((0,0.006375,-0.21038),(PI/2,0,0)),((0,-0.20843,-0.006375),(-PI/2,0,0)),((0,0.00017505,-0.10593),(PI/2,0,0)),((0,-0.10593,-0.00017505),(-PI/2,0,0))]
          12 +EE=((0,0,-0.061525),(PI,0,0))
          13 +def fk(base, q, base_z=0.0, tool=0.0):
          14 +    bx,by,br=base
          15 +    M=T((bx,by,base_z), rz(br))
          16 +    for (xyz,r),qi in zip(JOINTS,q):
          17 +        M=M@T(xyz,rpy(*r))@T((0,0,0),rz(qi))
          18 +    M=M@T(EE[0],rpy(*EE[1]))
          19 +    M=M@T((0,0,tool),np.eye(3))
          20 +    return M
          21 +if __name__=="__main__":
          22 +    q=[0,-0.35,-PI,-2.5,0,-0.87,PI/2]
          23 +    np.set_printoptions(precision=4,suppress=True)
          24 +    print(fk((-0.12,0,0),q))
diff --git a/grid0_-0.04,-0.02.txt b/grid0_-0.04,-0.02.txt
new file mode 100644
index 0000000..ce7bf2f
--- /dev/null
+++ b/grid0_-0.04,-0.02.txt
@@ -0,0 +1,2 @@
           1 +dy=-0.04 0.285 0.285 0.270 0.245 0.235 0.235 0.230 0.230 0.235
           2 +dy=-0.02 0.285 0.285 0.270 0.240 0.235 0.230 0.230 0.230 0.235
diff --git a/grid0_-0.08,-0.06.txt b/grid0_-0.08,-0.06.txt
new file mode 100644
index 0000000..ee7969a
--- /dev/null
+++ b/grid0_-0.08,-0.06.txt
@@ -0,0 +1,2 @@
           1 +dy=-0.08 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.230 0.235
           2 +dy=-0.06 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.230 0.235
diff --git a/grid0_0.0,0.02.txt b/grid0_0.0,0.02.txt
new file mode 100644
index 0000000..2762d34
--- /dev/null
+++ b/grid0_0.0,0.02.txt
@@ -0,0 +1,2 @@
           1 +dy=0.00 0.285 0.285 0.270 0.240 0.235 0.230 0.230 0.235 0.235
           2 +dy=0.02 0.285 0.285 0.270 0.245 0.235 0.230 0.230 0.235 0.235
diff --git a/grid0_0.04,0.06.txt b/grid0_0.04,0.06.txt
new file mode 100644
index 0000000..a79cd8b
--- /dev/null
+++ b/grid0_0.04,0.06.txt
@@ -0,0 +1,2 @@
           1 +dy=0.04 0.260 0.260 0.250 0.240 0.235 0.235 0.230 0.235 0.235
           2 +dy=0.06 0.235 0.235 0.235 0.235 0.235 0.235 0.230 0.235 0.235
diff --git a/grid0_0.08.txt b/grid0_0.08.txt
new file mode 100644
index 0000000..215be5f
--- /dev/null
+++ b/grid0_0.08.txt
@@ -0,0 +1 @@
           1 +dy=0.08 0.235 0.235 0.235 0.235 0.235 0.230 0.230 0.235 0.235
diff --git a/grid1_-0.04,-0.02.txt b/grid1_-0.04,-0.02.txt
new file mode 100644
index 0000000..c64c21d
--- /dev/null
+++ b/grid1_-0.04,-0.02.txt
@@ -0,0 +1,2 @@
           1 +dy=-0.04 0.245 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           2 +dy=-0.02 0.245 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
diff --git a/grid1_-0.08,-0.06.txt b/grid1_-0.08,-0.06.txt
new file mode 100644
index 0000000..9a9284c
--- /dev/null
+++ b/grid1_-0.08,-0.06.txt
@@ -0,0 +1,2 @@
           1 +dy=-0.08 0.245 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           2 +dy=-0.06 0.245 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
diff --git a/grid1_0.0,0.02.txt b/grid1_0.0,0.02.txt
new file mode 100644
index 0000000..0f6f493
--- /dev/null
+++ b/grid1_0.0,0.02.txt
@@ -0,0 +1,2 @@
           1 +dy=0.00 0.235 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           2 +dy=0.02 0.245 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
diff --git a/grid1_0.04,0.06.txt b/grid1_0.04,0.06.txt
new file mode 100644
index 0000000..565a8a8
--- /dev/null
+++ b/grid1_0.04,0.06.txt
@@ -0,0 +1,2 @@
           1 +dy=0.04 0.245 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
           2 +dy=0.06 0.245 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
diff --git a/grid1_0.08.txt b/grid1_0.08.txt
new file mode 100644
index 0000000..602c588
--- /dev/null
+++ b/grid1_0.08.txt
@@ -0,0 +1 @@
           1 +dy=0.08 0.245 0.230 0.230 0.230 0.230 0.230 0.230 0.230 0.230
diff --git a/kin.py b/kin.py
new file mode 100644
index 0000000..49670b8
--- /dev/null
+++ b/kin.py
@@ -0,0 +1,73 @@
           1 +import numpy as np
           2 +PI = np.pi
           3 +
           4 +def _rpy(r, p, y):
           5 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           6 +    return np.array([[cy*cp, cy*sp*sr-sy*cr, cy*sp*cr+sy*sr],
           7 +                     [sy*cp, sy*sp*sr+cy*cr, sy*sp*cr-cy*sr],
           8 +                     [-sp, cp*sr, cp*cr]])
           9 +
          10 +def _T(xyz, R):
          11 +    M = np.eye(4); M[:3, :3] = R; M[:3, 3] = xyz; return M
          12 +
          13 +def _rz(q):
          14 +    c, s = np.cos(q), np.sin(q)
          15 +    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
          16 +
          17 +_J = [((0, 0, 0.15643), (PI, 0, 0)), ((0, 0.005375, -0.12838), (PI/2, 0, 0)),
          18 +      ((0, -0.21038, -0.006375), (-PI/2, 0, 0)), ((0, 0.006375, -0.21038), (PI/2, 0, 0)),
          19 +      ((0, -0.20843, -0.006375), (-PI/2, 0, 0)), ((0, 0.00017505, -0.10593), (PI/2, 0, 0)),
          20 +      ((0, -0.10593, -0.00017505), (-PI/2, 0, 0))]
          21 +_JT = [_T(xyz, _rpy(*r)) for xyz, r in _J]
          22 +_EE = _T((0, 0, -0.061525), _rpy(PI, 0, 0))
          23 +
          24 +BASE_Z = 0.0
          25 +TOOL = 0.0
          26 +
          27 +def fk(base, q, tool=None):
          28 +    if tool is None:
          29 +        tool = TOOL
          30 +    bx, by, br = base
          31 +    M = _T((bx, by, BASE_Z), _rz(br))
          32 +    for Jt, qi in zip(_JT, q):
          33 +        M = M @ Jt @ _T((0, 0, 0), _rz(qi))
          34 +    M = M @ _EE
          35 +    if tool:
          36 +        M = M @ _T((0, 0, tool), np.eye(3))
          37 +    return M
          38 +
          39 +def _err(M, pos, R):
          40 +    ep = pos - M[:3, 3]
          41 +    Re = R @ M[:3, :3].T
          42 +    # rotation error as axis-angle (small-angle approx ok via skew)
          43 +    eo = 0.5 * np.array([Re[2, 1]-Re[1, 2], Re[0, 2]-Re[2, 0], Re[1, 0]-Re[0, 1]])
          44 +    return np.concatenate([ep, eo])
          45 +
          46 +def ik(base, q0, pos, R, iters=200, tol=1e-4, rot_w=0.3, tool=None):
          47 +    q = np.array(q0, dtype=float)
          48 +    W = np.array([1, 1, 1, rot_w, rot_w, rot_w])
          49 +    for _ in range(iters):
          50 +        M = fk(base, q, tool)
          51 +        e = _err(M, pos, R) * W
          52 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < tol*3:
          53 +            return q, True
          54 +        Jm = np.zeros((6, 7))
          55 +        h = 1e-6
          56 +        for i in range(7):
          57 +            dq = q.copy(); dq[i] += h
          58 +            Jm[:, i] = (_err(M, pos, R) - _err(fk(base, dq, tool), pos, R)) * W / h
          59 +        lam = 1e-3
          60 +        d = Jm.T @ np.linalg.solve(Jm @ Jm.T + lam*np.eye(6), e)
          61 +        n = np.max(np.abs(d))
          62 +        if n > 0.3:
          63 +            d *= 0.3 / n
          64 +        q = q + d
          65 +    M = fk(base, q, tool)
          66 +    e = _err(M, pos, R)
          67 +    return q, bool(np.linalg.norm(e[:3]) < 1e-3 and np.linalg.norm(e[3:]) < 1e-2)
          68 +
          69 +def down_R(yaw):
          70 +    # gripper z axis pointing down, x axis direction by yaw
          71 +    c, s = np.cos(yaw), np.sin(yaw)
          72 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          73 +    return np.stack([x, y, z], axis=1)
diff --git a/probe.py b/probe.py
new file mode 100644
index 0000000..94ea10a
--- /dev/null
+++ b/probe.py
@@ -0,0 +1,32 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin, sys
           3 +F = ['joint_%d'%i for i in range(1,8)]
           4 +env = make_env()
           5 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); obj=sys.argv[3] if len(sys.argv)>3 else 'target_block'
           6 +out=[]
           7 +for ang in [0,90,180,270]:
           8 +    d=np.array([np.cos(np.radians(ang)),np.sin(np.radians(ang))])
           9 +    obs, info = env.reset(seed=seed)
          10 +    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name(obj)
          11 +    getq=lambda o: np.array([o.get(r,f) for f in F])
          12 +    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          13 +    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
          14 +    q=getq(obs)
          15 +    def go(p):
          16 +        global q,obs
          17 +        qt,ok=kin.ik(base,q,np.array(p),kin.down_R(yaw))
          18 +        while np.max(np.abs(qt-q))>1e-6:
          19 +            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
          20 +            obs,_,_,_,_=env.step(a); qn=getq(obs)
          21 +            if np.allclose(qn,q): return False
          22 +            q=qn
          23 +        return True
          24 +    s=0.2
          25 +    go([bx-d[0]*s,by-d[1]*s,bz+0.3]); ok=go([bx-d[0]*s,by-d[1]*s,bz+0.165])
          26 +    if not ok: out.append((ang,'startblocked')); continue
          27 +    while s>-0.2:
          28 +        s-=0.002
          29 +        if not go([bx-d[0]*s,by-d[1]*s,bz+0.165]): break
          30 +    out.append((ang, round(-s,3)))
          31 +print("seed",seed,"yaw",yaw,obj,"block",round(bx,3),round(by,3),"contact offsets (EE - block along -d):",out)
          32 +env.close()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..a6ba162
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,23 @@
           1 +import sys, time, numpy as np
           2 +from concurrent.futures import ProcessPoolExecutor
           3 +def run(seed):
           4 +    from env_client import make_env
           5 +    import approach
           6 +    env = make_env()
           7 +    obs, info = env.reset(seed=seed)
           8 +    ap = approach.GeneratedApproach(env.action_space, env.observation_space, {})
           9 +    ap.reset(obs, info)
          10 +    t0=time.time(); steps=0; term=False
          11 +    n=len([x for x in obs.get_object_names() if x.startswith('obstruction')])
          12 +    for steps in range(1, env.max_steps+1):
          13 +        a = ap.get_action(obs)
          14 +        obs, rew, term, trunc, info = env.step(a)
          15 +        if term or trunc: break
          16 +    env.close()
          17 +    return seed, n, bool(term), steps, round(time.time()-t0,1)
          18 +if __name__ == "__main__":
          19 +    a=int(sys.argv[1]) if len(sys.argv)>1 else 0; b=int(sys.argv[2]) if len(sys.argv)>2 else 10
          20 +    with ProcessPoolExecutor(8) as ex:
          21 +        res=list(ex.map(run, range(a,b)))
          22 +    for r in res: print(r)
          23 +    print("success", sum(r[2] for r in res), "/", len(res), "mean steps", np.mean([r[3] for r in res]))
```

</details>

<a id="C003"></a>
### C003 · Use calibrated kinematics (arm offset, TCP=0.12), grasp/place via grasp_tf, release retries

Commit `d6db4fc3270cc809eea1acd23aef24d2876c28a9`; parents: 62c9e4056ea3130b5ffab63f9d4363c78985eacd. Recorded author date: 2026-09-30T20:54:07+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0422](01_timeline.md#E0422): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_d6db4fc_approach.py) · [Exact all-file diff](evidence/diffs/C003_d6db4fc.diff)

[Previous saved controller snapshot](evidence/versions/C002_62c9e40_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2b71c5c..917085e 100644
--- a/approach.py
+++ b/approach.py
@@ -2,10 +2,12 @@ import numpy as np
    2      2  from kin import fk, ik, down_R
    3      3  
    4      4  JF = ['joint_%d' % i for i in range(1, 8)]
           5 +TOOL = 0.12          # TCP offset along EE z (gripper centre)
    5      6  MAXD = 0.19
    6        -SAFE_Z = 0.33       # EE transit height
    7        -GRASP_DZ = 0.14     # EE height above object center when grasping (calibrate)
           7 +SAFE_Z = 0.27        # TCP transit height
    8      8  TABLE_Z = 0.075
           9 +X_RANGE = (0.12, 0.44)
          10 +Y_RANGE = (-0.36, 0.36)
    9     11  
   10     12  
   11     13  def _pose(s, o):
@@ -16,22 +18,26 @@ def _he(s, o):
   16     18      return np.array([s.get(o, 'half_extent_x'), s.get(o, 'half_extent_y'), s.get(o, 'half_extent_z')])
   17     19  
   18     20  
   19        -def _yaw(s, o):
   20        -    qx, qy, qz, qw = [s.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]
   21        -    return np.arctan2(2 * (qw * qz + qx * qy), 1 - 2 * (qy * qy + qz * qz))
          21 +def _quat_R(x, y, z, w):
          22 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          23 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          24 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          25 +
          26 +
          27 +def _wrap(a):
          28 +    return (a + np.pi) % (2 * np.pi) - np.pi
   22     29  
   23     30  
   24     31  class GeneratedApproach:
   25     32      def __init__(self, action_space, observation_space, primitives):
   26     33          self.action_space = action_space
   27     34  
   28        -    # ------------------------------------------------------------------
   29     35      def reset(self, state, info):
   30        -        self.queue = []       # list of ('move', pos, yaw) | ('grip', val, n)
   31        -        self.phase = 'plan'
          36 +        self.queue = []
   32     37          self.qtarget = None
   33        -        self.stuck = 0
          38 +        self.cur = None
   34     39          self.last_q = None
          40 +        self.retries = 0
   35     41  
   36     42      def _robot(self, s):
   37     43          r = s.get_object_from_name('robot')
@@ -39,89 +45,157 @@ class GeneratedApproach:
   39     45          base = (s.get(r, 'pos_base_x'), s.get(r, 'pos_base_y'), s.get(r, 'pos_base_rot'))
   40     46          return r, q, base
   41     47  
   42        -    # ------------------------------------------------------------------
   43        -    def _overlaps(self, s, o, reg):
          48 +    # ------------------------------------------------------------------ planning
          49 +    def _overlaps(self, s, o, reg, margin=0.004):
   44     50          p, h = _pose(s, o), _he(s, o)
   45     51          rp, rh = _pose(s, reg), _he(s, reg)
   46        -        return (abs(p[0] - rp[0]) < h[0] + rh[0] + 0.005 and
   47        -                abs(p[1] - rp[1]) < h[1] + rh[1] + 0.005)
          52 +        return (abs(p[0] - rp[0]) < h[0] + rh[0] + margin and
          53 +                abs(p[1] - rp[1]) < h[1] + rh[1] + margin)
   48     54  
   49        -    def _free_spot(self, s, obj, avoid):
   50        -        """Find a free table spot for obj away from the objects in avoid."""
          55 +    def _free_spot(self, s, obj, avoid, cur):
   51     56          h = _he(s, obj)
   52        -        best, bestd = None, -1
   53        -        for x in np.linspace(0.05, 0.35, 13):
   54        -            for y in np.linspace(-0.3, 0.3, 25):
          57 +        best, bestscore = None, -1e9
          58 +        for x in np.linspace(X_RANGE[0], X_RANGE[1], 17):
          59 +            for y in np.linspace(Y_RANGE[0], Y_RANGE[1], 37):
   55     60                  dmin = 1e9
   56     61                  for o in avoid:
   57     62                      p, oh = _pose(s, o), _he(s, o)
   58     63                      dx = abs(x - p[0]) - (h[0] + oh[0])
   59     64                      dy = abs(y - p[1]) - (h[1] + oh[1])
   60     65                      dmin = min(dmin, max(dx, dy))
   61        -                if dmin > 0.06:
   62        -                    # prefer close to robot centre line
   63        -                    score = dmin - 0.2 * abs(y)
   64        -                    if best is None or score > bestd:
   65        -                        best, bestd = (x, y), score
   66        -                elif best is None and dmin > bestd:
   67        -                    bestd = dmin
   68        -                    best = (x, y)
          66 +                score = min(dmin, 0.07) - 0.1 * np.hypot(x - cur[0], y - cur[1])
          67 +                if score > bestscore:
          68 +                    best, bestscore = (x, y), score
   69     69          return np.array(best)
   70     70  
   71        -    def _plan_pick_place(self, s, obj, place_xy, place_z_center):
          71 +    def _grasp_yaw(self, s, obj, q, base):
          72 +        h = _he(s, obj)
          73 +        R = _quat_R(*[s.get(obj, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')])
          74 +        oyaw = np.arctan2(R[1, 0], R[0, 0])
          75 +        # fingers close along EE x: span the smaller side
          76 +        yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
          77 +        # choose yaw or yaw+pi closest to current gripper yaw
          78 +        M = fk(base, q, TOOL)
          79 +        cy = np.arctan2(M[1, 0], M[0, 0])
          80 +        if abs(_wrap(yaw - cy)) > np.pi / 2:
          81 +            yaw += np.pi
          82 +        return _wrap(yaw)
          83 +
          84 +    def _plan_pick_place(self, s, obj, place_xy, support_top):
          85 +        _, q, base = self._robot(s)
   72     86          p = _pose(s, obj)
   73        -        yaw = _yaw(s, obj)
   74        -        q = []
   75        -        q.append(('grip', 1.0, 1))
   76        -        q.append(('move', np.array([p[0], p[1], SAFE_Z]), yaw))
   77        -        q.append(('move', np.array([p[0], p[1], p[2] + GRASP_DZ]), yaw))
   78        -        q.append(('grip', -1.0, 2))
   79        -        q.append(('move', np.array([p[0], p[1], SAFE_Z]), yaw))
   80        -        q.append(('move', np.array([place_xy[0], place_xy[1], SAFE_Z]), yaw))
   81        -        q.append(('move', np.array([place_xy[0], place_xy[1], place_z_center + GRASP_DZ + 0.003]), yaw))
   82        -        q.append(('grip', 1.0, 2))
   83        -        q.append(('move', np.array([place_xy[0], place_xy[1], SAFE_Z]), yaw))
   84        -        return q
          87 +        h = _he(s, obj)
          88 +        yaw = self._grasp_yaw(s, obj, q, base)
          89 +        gz = p[2] + min(0.03, h[2] + 0.005)  # TCP height for grasp
          90 +        gz = max(gz, 0.108)
          91 +        place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
          92 +        return [
          93 +            ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
          94 +            ('move', np.array([p[0], p[1], gz]), yaw, True),
          95 +            ('close', obj.name),
          96 +            ('move', np.array([p[0], p[1], SAFE_Z]), yaw, False),
          97 +            ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
          98 +            ('place_move', place_center + np.array([0, 0, 0.02]), yaw, False),
          99 +            ('place_move', place_center, yaw, True),
         100 +            ('open', place_center, yaw),
         101 +            ('move_rel_up', SAFE_Z, yaw),
         102 +        ]
   85    103  
   86    104      def _plan(self, s):
   87    105          reg = s.get_object_from_name('target_region')
   88    106          tb = s.get_object_from_name('target_block')
   89        -        cubes = [s.get_object_from_name(n) for n in s.get_object_names()
         107 +        _, q, base = self._robot(s)
         108 +        cur = fk(base, q, TOOL)[:3, 3]
         109 +        cubes = [s.get_object_from_name(n) for n in sorted(s.get_object_names())
   90    110                   if n.startswith('obstruction')]
   91    111          blocking = [o for o in cubes if self._overlaps(s, o, reg)]
   92    112          if blocking:
   93        -            o = blocking[0]
         113 +            # remove the tallest (top-most) first
         114 +            o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2])
   94    115              others = [c for c in cubes if c.name != o.name] + [reg, tb]
   95        -            spot = self._free_spot(s, o, others)
   96        -            return self._plan_pick_place(s, o, spot, TABLE_Z + _he(s, o)[2])
         116 +            spot = self._free_spot(s, o, others, cur)
         117 +            return self._plan_pick_place(s, o, spot, TABLE_Z)
   97    118          rp = _pose(s, reg)
   98        -        z = rp[2] + _he(s, reg)[2] + _he(s, tb)[2]
   99        -        return self._plan_pick_place(s, tb, rp[:2], z)
         119 +        return self._plan_pick_place(s, tb, rp[:2], rp[2] + _he(s, reg)[2])
         120 +
         121 +    # ------------------------------------------------------------------ execution
         122 +    def _tcp_target_for_block(self, s, center, yaw):
         123 +        """TCP position so that the held block's centre lands at `center`."""
         124 +        r = s.get_object_from_name('robot')
         125 +        t = np.array([s.get(r, 'grasp_tf_x'), s.get(r, 'grasp_tf_y'), s.get(r, 'grasp_tf_z')])
         126 +        return center - down_R(yaw) @ t
  100    127  
  101        -    # ------------------------------------------------------------------
  102    128      def get_action(self, s):
         129 +        for _ in range(20):
         130 +            a = self._step(s)
         131 +            if a is not None:
         132 +                return a
         133 +        return np.zeros(11, dtype=np.float32)
         134 +
         135 +    def _step(self, s):
  103    136          a = np.zeros(11, dtype=np.float32)
  104    137          r, q, base = self._robot(s)
         138 +        grasping = s.get(r, 'grasp_active') > 0.5
         139 +        if grasping:
         140 +            a[10] = -1.0
  105    141          if not self.queue:
  106    142              self.queue = self._plan(s)
  107    143              self.qtarget = None
         144 +            self.last_q = None
  108    145          cmd = self.queue[0]
  109        -        if cmd[0] == 'grip':
  110        -            a[10] = cmd[1]
  111        -            n = cmd[2] - 1
  112        -            if n <= 0:
         146 +        kind = cmd[0]
         147 +        if kind == 'close':
         148 +            if grasping:
         149 +                self.queue.pop(0)
         150 +                return None
         151 +            self.retries += 1
         152 +            if self.retries > 3:
         153 +                # failed grasp: replan from scratch
         154 +                self.retries = 0
         155 +                self.queue = [('move_rel_up', SAFE_Z, None)]
         156 +                return None
         157 +            a[10] = -1.0
         158 +            return a
         159 +        if kind == 'open':
         160 +            if not grasping:
  113    161                  self.queue.pop(0)
  114        -            else:
  115        -                self.queue[0] = ('grip', cmd[1], n)
         162 +                self.retries = 0
         163 +                return None
         164 +            self.retries += 1
         165 +            if self.retries > 1:
         166 +                # lower a bit and try again
         167 +                self.retries = 0
         168 +                c = cmd[1] - np.array([0, 0, 0.002])
         169 +                self.queue[0] = ('open', c, cmd[2])
         170 +                self.queue.insert(0, ('place_move', c, cmd[2], True))
         171 +                return None
         172 +            a[10] = 1.0
  116    173              return a
  117        -        # move
  118    174          if self.qtarget is None:
  119        -            qt, ok = ik(base, q, cmd[1], down_R(cmd[2]))
         175 +            if kind == 'move':
         176 +                pos, yaw = cmd[1], cmd[2]
         177 +            elif kind == 'place_move':
         178 +                pos, yaw = self._tcp_target_for_block(s, cmd[1], cmd[2]), cmd[2]
         179 +            elif kind == 'move_rel_up':
         180 +                M = fk(base, q, TOOL)
         181 +                pos = M[:3, 3].copy(); pos[2] = max(pos[2], cmd[1])
         182 +                yaw = np.arctan2(M[1, 0], M[0, 0]) if cmd[2] is None else cmd[2]
         183 +            qt, ok = ik(base, q, pos, down_R(yaw), tool=TOOL)
  120    184              self.qtarget = qt
         185 +            self.last_q = None
  121    186          d = self.qtarget - q
  122    187          if np.max(np.abs(d)) < 1e-4:
  123    188              self.queue.pop(0)
  124    189              self.qtarget = None
  125        -            return self.get_action(s) if self.queue else a
         190 +            return None
         191 +        if self.last_q is not None and np.allclose(self.last_q, q, atol=1e-7):
         192 +            # previous action rejected (collision)
         193 +            allow = len(cmd) > 3 and cmd[3]
         194 +            self.queue.pop(0)
         195 +            self.qtarget = None
         196 +            if not allow:
         197 +                self.queue = []  # replan
         198 +            return None
         199 +        self.last_q = q.copy()
  126    200          a[3:10] = np.clip(d, -MAXD, MAXD)
  127    201          return a
diff --git a/calib_1.py b/calib_1.py
new file mode 100644
index 0000000..14f0f69
--- /dev/null
+++ b/calib_1.py
@@ -0,0 +1,7 @@
           1 +from calib_u import *
           2 +e=R()
           3 +for seed in range(8):
           4 +    e.reset(seed); print(seed, 'block',np.round(e.blk(),3),'obst',[np.round(e.blk(n),3) for n in e.obs.get_object_names() if 'obst' in n][:2], 'region', np.round(e.blk('target_region')[:3],3))
           5 +e.reset(1)
           6 +for g in [1,1,1,-1,-1,-1,-1,0,1]:
           7 +    e.stepq(np.zeros(7),g); print(g, e.rob('finger_state'), e.rob('grasp_active'))
diff --git a/calib_10.py b/calib_10.py
new file mode 100644
index 0000000..270c786
--- /dev/null
+++ b/calib_10.py
@@ -0,0 +1,24 @@
           1 +import numpy as np, kin
           2 +from scipy.optimize import least_squares
           3 +from scipy.spatial.transform import Rotation as Rot
           4 +D=np.concatenate([np.load(f'dbg/g{s}.npy') for s in [1,5,6]])
           5 +def T6(p): M=np.eye(4); M[:3,:3]=Rot.from_rotvec(p[3:6]).as_matrix(); M[:3,3]=p[:3]; return M
           6 +blk=[]
           7 +for d in D:  # block pose in mobile-base frame
           8 +    M=np.eye(4); M[:3,:3]=Rot.from_quat(d[13:17]).as_matrix(); M[:3,3]=d[10:13]
           9 +    Tb=np.eye(4); Tb[:3,:3]=kin._rz(d[2]); Tb[:3,3]=[d[0],d[1],0]; blk.append(np.linalg.inv(Tb)@M)
          10 +def res(p):
          11 +    r=[]
          12 +    for i,d in enumerate(D):
          13 +        P=T6(p[:6])@kin.fk((0,0,0),d[3:10]+p[12:19])@T6(p[6:12])
          14 +        r.append(P[:3,3]-blk[i][:3,3]); r.append(0.1*(P[:3,:3]-blk[i][:3,:3]).ravel())
          15 +    return np.concatenate(r)
          16 +best=None
          17 +for k in range(8):
          18 +    p0=np.random.default_rng(k).normal(0,0.3,19) if k else np.zeros(19)
          19 +    s=least_squares(res,p0)
          20 +    if best is None or s.cost<best.cost: best=s
          21 +    print(k, s.cost)
          22 +p=best.x; r=res(p).reshape(len(D),-1)
          23 +print('pos rms',np.sqrt((r[:,:3]**2).mean()),'max',np.abs(r[:,:3]).max(),'rot rms',np.sqrt((r[:,3:]**2).mean())*10)
          24 +np.set_printoptions(precision=4,suppress=True); print(p)
diff --git a/calib_11.py b/calib_11.py
new file mode 100644
index 0000000..4866ec7
--- /dev/null
+++ b/calib_11.py
@@ -0,0 +1,31 @@
           1 +# per-joint axis identification from grasped block
           2 +from calib_u import *
           3 +from scipy.spatial.transform import Rotation as Rot
           4 +import sys
           5 +seed=int(sys.argv[1]); e=R(); e.reset(seed); b=e.blk()
           6 +x,y=b[0]-0.10,b[1]-0.01; z=0.40
           7 +e.go([x,y,z],0.0)
           8 +while z>0.25+1e-9:
           9 +    if not e.go([x,y,z-0.005],0.0): break
          10 +    z-=0.005
          11 +for i in range(2): e.stepq(np.zeros(7),-1.0)
          12 +e.go([x,y,0.42],0.0,grip=-1)
          13 +def bp():
          14 +    return np.array([e.g('target_block',k) for k in ['pose_x','pose_y','pose_z']]), Rot.from_quat([e.g('target_block',k) for k in ['pose_qx','pose_qy','pose_qz','pose_qw']]).as_matrix()
          15 +def jframes(base,q):
          16 +    bx,by,br=base; M=kin._T((bx,by,0),kin._rz(br)); out=[]
          17 +    for Jt,qi in zip(kin._JT,q):
          18 +        M=M@Jt; out.append(M.copy()); M=M@kin._T((0,0,0),kin._rz(qi))
          19 +    return out
          20 +np.set_printoptions(precision=3,suppress=True)
          21 +d=0.1
          22 +for j in range(7):
          23 +    p0,R0=bp(); q=e.q(); fr=jframes(e.base(),q)
          24 +    dq=np.zeros(7); dq[j]=d; ok=e.stepq(dq,-1.0)
          25 +    p1,R1=bp(); e.stepq(-dq,-1.0)
          26 +    rv=Rot.from_matrix(R1@R0.T).as_rotvec(); ang=np.linalg.norm(rv); w=rv/ang
          27 +    A=np.eye(3)-R1@R0.T; c=np.linalg.pinv(A,rcond=1e-3)@(p1-R1@R0.T@p0)
          28 +    zf=fr[j][:3,2]; of=fr[j][:3,3]
          29 +    # distance between true axis line and FK axis line points
          30 +    cperp=c-of; cperp-=np.dot(cperp,w)*w
          31 +    print(f"j{j+1} ok={ok} ang={ang:.3f} true_w={w} fk_z={zf} dot={np.dot(w,zf):+.3f} true_pt={c} fk_org={of} off_perp={cperp}")
diff --git a/calib_12.py b/calib_12.py
new file mode 100644
index 0000000..28e3802
--- /dev/null
+++ b/calib_12.py
@@ -0,0 +1,24 @@
           1 +import numpy as np, kin
           2 +from scipy.optimize import least_squares
           3 +from scipy.spatial.transform import Rotation as Rot
           4 +S=[1,5,6]; DS=[np.load(f'dbg/g{s}.npy') for s in S]
           5 +np.set_printoptions(precision=4,suppress=True)
           6 +def prep(D):
           7 +    blk=[];arm=[]
           8 +    for d in D:
           9 +        M=np.eye(4); M[:3,:3]=Rot.from_quat(d[13:17]).as_matrix(); M[:3,3]=d[10:13]
          10 +        Tb=np.eye(4); Tb[:3,:3]=kin._rz(d[2]); Tb[:3,3]=[d[0],d[1],0]; blk.append(np.linalg.inv(Tb)@M); arm.append(kin.fk((0,0,0),d[3:10]))
          11 +    return blk,arm
          12 +P=[prep(D) for D in DS]
          13 +def res(p):
          14 +    r=[]
          15 +    for k,(blk,arm) in enumerate(P):
          16 +        t=p[3+3*k:6+3*k]
          17 +        for a,b in zip(arm,blk): r.append(a[:3,:3]@t+a[:3,3]+p[:3]-b[:3,3])
          18 +    return np.concatenate(r)
          19 +s=least_squares(res,np.zeros(3+3*len(S))); r=res(s.x).reshape(-1,3)
          20 +print('pos rms',np.sqrt((r**2).mean()),'max',np.abs(r).max())
          21 +print('base offset (arm-base frame)',s.x[:3])
          22 +for k,D in enumerate(DS):
          23 +    blk,arm=P[k]; Rt=arm[0][:3,:3].T@blk[0][:3,:3]
          24 +    print('seed',S[k],'block pos in EE frame',s.x[3+3*k:6+3*k],'Rrel quat',Rot.from_matrix(Rt).as_quat(),'| grasp_tf',D[0,17:24])
diff --git a/calib_13.py b/calib_13.py
new file mode 100644
index 0000000..d6030d0
--- /dev/null
+++ b/calib_13.py
@@ -0,0 +1,7 @@
           1 +import numpy as np, kin
           2 +from scipy.spatial.transform import Rotation as Rot
           3 +D=np.load('dbg/g1.npy')
           4 +np.set_printoptions(precision=3,suppress=True)
           5 +for i in [0,1,2,3,4,5,10,20,40]:
           6 +    d=D[i]; Rb=Rot.from_quat(d[13:17]).as_matrix(); Ra=kin.fk(d[:3],d[3:10])[:3,:3]
           7 +    print(i, np.round(d[:3],3), Rot.from_matrix(Ra.T@Rb).as_rotvec(), 'blkpos',d[10:13])
diff --git a/calib_14.py b/calib_14.py
new file mode 100644
index 0000000..f408111
--- /dev/null
+++ b/calib_14.py
@@ -0,0 +1,13 @@
           1 +# grasp test in TCP coords: python calib_14.py seed yaw dx dy tcpz
           2 +from calib_u import *
           3 +import sys
           4 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); dx,dy,zt=[float(v) for v in sys.argv[3:6]]; T=0.12
           5 +e=R(); e.reset(seed); b=e.blk(); x,y=b[0]+dx,b[1]+dy; z=0.25
           6 +e.go([x,y,z],yaw,tool=T)
           7 +while z>zt+1e-9:
           8 +    if not e.go([x,y,z-0.0025],yaw,tool=T): break
           9 +    z-=0.0025
          10 +e.stepq(np.zeros(7),-1.0)
          11 +ga=e.rob('grasp_active'); fs=e.rob('finger_state')
          12 +e.go([x,y,0.25],yaw,tool=T,grip=-1)
          13 +print(f"seed{seed} yaw{yaw:.2f} d=({dx:+.3f},{dy:+.3f}) tcpz={z:.4f} grasp={ga} fs={fs:.3f} blk_after_lift_z={e.blk()[2]:.3f} tf={[round(e.rob('grasp_tf_'+k),4) for k in 'x y z qx qy qz qw'.split()]}")
diff --git a/calib_15.py b/calib_15.py
new file mode 100644
index 0000000..1e2fd45
--- /dev/null
+++ b/calib_15.py
@@ -0,0 +1,20 @@
           1 +# release test: python calib_15.py seed relx rely relz(tcp)
           2 +from calib_u import *
           3 +import sys
           4 +seed=int(sys.argv[1]); T=0.12; e=R(); e.reset(seed); b=e.blk(); yaw=0.0 if b[3]<b[4] else np.pi/2
           5 +x,y=b[0],b[1]; z=0.25; e.go([x,y,z],yaw,tool=T)
           6 +while z>b[2]+b[5]+0.005: 
           7 +    e.go([x,y,z-0.005],yaw,tool=T); z-=0.005
           8 +e.stepq(np.zeros(7),-1.0); print('grasp',e.rob('grasp_active'))
           9 +tx,ty,tz=[float(v) for v in sys.argv[2:5]]
          10 +e.go([x,y,0.25],yaw,tool=T,grip=-1); print('go target',e.go([tx,ty,0.25],yaw,tool=T,grip=-1))
          11 +zz=0.25
          12 +while zz>tz+1e-9:
          13 +    if not e.go([tx,ty,zz-0.0025],yaw,tool=T,grip=-1): print('lower blocked at tcp z',round(zz,4),'blk',np.round(e.blk()[:3],4)); break
          14 +    zz-=0.0025
          15 +print('before open blk',np.round(e.blk()[:3],4))
          16 +for i in range(3):
          17 +    ok=e.stepq(np.zeros(7),1.0); print('open',i,'grasp',e.rob('grasp_active'),'fs',e.rob('finger_state'),'blk',np.round(e.blk()[:3],4),'blk_ga',e.g('target_block','grasp_active'))
          18 +e.go([tx,ty,0.3],yaw,tool=T,grip=0); print('after retreat blk',np.round(e.blk()[:3],4))
          19 +for n in e.obs.get_object_names():
          20 +    if n!='robot': print(n,np.round(e.blk(n),3))
diff --git a/calib_2.py b/calib_2.py
new file mode 100644
index 0000000..dc0e907
--- /dev/null
+++ b/calib_2.py
@@ -0,0 +1,22 @@
           1 +# horizontal approach probe: python calib_2.py seed yaw zoff
           2 +from calib_u import *
           3 +import sys
           4 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); zfk=float(sys.argv[3])
           5 +e=R(); res=[]
           6 +for ang in [0,90,180,270]:
           7 +    d=np.array([np.cos(np.radians(ang)),np.sin(np.radians(ang)),0])
           8 +    e.reset(seed); b=e.blk(); c=b[:3].copy(); c[2]=zfk
           9 +    s=0.25
          10 +    e.go(c-d*s+[0,0,0.1],yaw); ok=e.go(c-d*s,yaw)
          11 +    if not ok: res.append((ang,'startblk')); continue
          12 +    for step in [0.01,0.001]:
          13 +        while s>-0.25:
          14 +            r=e.go(c-d*(s-step),yaw)
          15 +            if r is None: print('ikfail'); break
          16 +            if not r: break
          17 +            s-=step
          18 +    res.append(s)
          19 +# contact positions along axis: EE coordinate at contact relative to block center
          20 +xa=-res[0]; xb=res[2]; ya=-res[1]; yb=res[3]
          21 +b=e.blk()
          22 +print(f"seed {seed} yaw {yaw:.2f} z {zfk} blk {np.round(b[:2],3)} he {np.round(b[3:5],3)} | x: {xa:.3f} {xb:.3f} ctr {-(xa+xb)/2:+.3f} w {xb-xa-2*b[3]:.3f} | y: {ya:.3f} {yb:.3f} ctr {-(ya+yb)/2:+.3f} w {yb-ya-2*b[4]:.3f}",flush=True)
diff --git a/calib_3.py b/calib_3.py
new file mode 100644
index 0000000..0fa2b48
--- /dev/null
+++ b/calib_3.py
@@ -0,0 +1,15 @@
           1 +from calib_u import *
           2 +import sys
           3 +e=R(); e.reset(1)
           4 +yaw=float(sys.argv[1]); p=[float(v) for v in sys.argv[2:5]]
           5 +qt,ok=kin.ik(e.base(),e.q(),np.array(p),kin.down_R(yaw)); print(ok, np.round(qt,3))
           6 +o=e.obs.copy()
           7 +for i,f in enumerate(F): o.set(e.r,f,qt[i])
           8 +M=kin.fk(e.base(),qt)
           9 +def put(name,pos,h=0.015):
          10 +    b=o.get_object_from_name(name)
          11 +    for k,v in zip(['pose_x','pose_y','pose_z'],pos): o.set(b,k,v)
          12 +    for k in ['half_extent_x','half_extent_y','half_extent_z']: o.set(b,k,h)
          13 +put('target_block',M[:3,3]); put('obstruction0',M[:3,3]+M[:3,2]*0.157)
          14 +put('target_region',[p[0],p[1],0.08],0.01)
          15 +import shutil; pth=e.env.render_state(state=o); shutil.copy(pth,'dbg/r_'+sys.argv[5]+'.png'); print(pth)
diff --git a/calib_4.py b/calib_4.py
new file mode 100644
index 0000000..c57bfd9
--- /dev/null
+++ b/calib_4.py
@@ -0,0 +1,8 @@
           1 +from calib_u import *
           2 +import sys, shutil
           3 +e=R(); e.reset(int(sys.argv[1])); yaw=float(sys.argv[2]); b=e.blk()
           4 +dx,dy,z=[float(v) for v in sys.argv[3:6]]
           5 +qt,ok=kin.ik(e.base(),e.q(),np.array([b[0]+dx,b[1]+dy,z]),kin.down_R(yaw))
           6 +o=e.obs.copy()
           7 +for i,f in enumerate(F): o.set(e.r,f,qt[i])
           8 +pth=e.env.render_state(state=o); shutil.copy(pth,'dbg/r_'+sys.argv[6]+'.png'); print(ok,np.round(qt,3))
diff --git a/calib_5.py b/calib_5.py
new file mode 100644
index 0000000..86ceab4
--- /dev/null
+++ b/calib_5.py
@@ -0,0 +1,15 @@
           1 +# descend-grid in TCP coords (tool=0.12): python calib_5.py seed yaw dy -> TCP z where descent stopped, over dx
           2 +from calib_u import *
           3 +import sys
           4 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); dy=float(sys.argv[3]); T=0.12
           5 +e=R(); row=[]
           6 +for dx in np.arange(-0.08,0.081,0.01):
           7 +    e.reset(seed); b=e.blk(); z=0.25
           8 +    r0=e.go([b[0]+dx,b[1]+dy,z],yaw,tool=T)
           9 +    while z>0.06:
          10 +        r=e.go([b[0]+dx,b[1]+dy,z-0.0025],yaw,tool=T)
          11 +        if not r: break
          12 +        z-=0.0025
          13 +    M=e.ee(T); err=np.linalg.norm(M[:3,:3]-kin.down_R(yaw))
          14 +    row.append(z if (r is not None and err<0.05) else -1)
          15 +print(f"{dy:+.2f} "+" ".join(f"{v:.3f}" for v in row),flush=True)
diff --git a/calib_6.py b/calib_6.py
new file mode 100644
index 0000000..116f792
--- /dev/null
+++ b/calib_6.py
@@ -0,0 +1,19 @@
           1 +# grasp attempt: python calib_6.py seed yaw ox oy zfinal
           2 +from calib_u import *
           3 +import sys
           4 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); ox,oy,zf=[float(v) for v in sys.argv[3:6]]
           5 +e=R(); e.reset(seed); b=e.blk()
           6 +x,y=b[0]-ox,b[1]-oy; z=0.40
           7 +e.go([x,y,z],yaw)
           8 +while z>zf+1e-9:
           9 +    if not e.go([x,y,z-0.005],yaw): break
          10 +    z-=0.005
          11 +print('stopped z',round(z,3))
          12 +for i in range(6):
          13 +    e.stepq(np.zeros(7),-1.0); print('close',i,e.rob('finger_state'),e.rob('grasp_active'),e.g('target_block','grasp_active'))
          14 +for i in range(5):
          15 +    r=e.go([x,y,z+0.02*(i+1)],yaw); print('lift',r,np.round(e.blk()[:3],4),'ee',np.round(e.ee()[:3,3],4))
          16 +print('tf',[round(e.rob('grasp_tf_'+k),4) for k in ['x','y','z','qx','qy','qz','qw']])
          17 +from scipy.spatial.transform import Rotation as Rot
          18 +Rb=Rot.from_quat([e.g('target_block',k) for k in ['pose_qx','pose_qy','pose_qz','pose_qw']]).as_matrix()
          19 +M=e.ee(); print('EE R\n',np.round(M[:3,:3],3),'\nblock R\n',np.round(Rb,3))
diff --git a/calib_7.py b/calib_7.py
new file mode 100644
index 0000000..8a67dd2
--- /dev/null
+++ b/calib_7.py
@@ -0,0 +1,23 @@
           1 +# collect grasped samples: python calib_7.py seed out.npy
           2 +from calib_u import *
           3 +import sys
           4 +seed=int(sys.argv[1]); e=R(); e.reset(seed); b=e.blk(); yaw=0.0
           5 +x,y=b[0]-0.10,b[1]-0.01; z=0.40
           6 +e.go([x,y,z],yaw)
           7 +while z>0.25+1e-9:
           8 +    if not e.go([x,y,z-0.005],yaw): break
           9 +    z-=0.005
          10 +for i in range(2): e.stepq(np.zeros(7),-1.0)
          11 +print('grasp',e.rob('grasp_active'))
          12 +e.go([x,y,0.40],yaw,grip=-1)
          13 +rng=np.random.default_rng(seed); D=[]
          14 +def rec():
          15 +    D.append(np.concatenate([e.base(),e.q(),[e.g('target_block',k) for k in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']],[e.rob('grasp_tf_'+k) for k in ['x','y','z','qx','qy','qz','qw']],[e.rob('grasp_active')]]))
          16 +rec(); q0=e.q()
          17 +for t in range(120):
          18 +    a=np.zeros(11,np.float32); a[10]=-1
          19 +    if t%4==3: a[:3]=rng.uniform(-0.1,0.1,3)
          20 +    else:
          21 +        a[3:10]=np.clip(rng.uniform(-0.15,0.15,7)+0.3*(q0-e.q()),-0.2,0.2)
          22 +    e.step(a); rec()
          23 +D=np.array(D); np.save(sys.argv[2],D); print(D.shape, 'grasp_active all', D[:,-1].min(), 'tf std', D[:,17:24].std(0).round(5))
diff --git a/calib_8.py b/calib_8.py
new file mode 100644
index 0000000..7d82155
--- /dev/null
+++ b/calib_8.py
@@ -0,0 +1,28 @@
           1 +import numpy as np, kin
           2 +from scipy.optimize import least_squares
           3 +from scipy.spatial.transform import Rotation as Rot
           4 +D=np.concatenate([np.load(f'dbg/g{s}.npy') for s in [1,5,6]])
           5 +def T6(p): M=np.eye(4); M[:3,:3]=Rot.from_rotvec(p[3:6]).as_matrix(); M[:3,3]=p[:3]; return M
           6 +def Tbase(b): M=np.eye(4); M[:3,:3]=kin._rz(b[2]); M[:3,3]=[b[0],b[1],0]; return M
           7 +blkT=[]
           8 +for d in D:
           9 +    M=np.eye(4); M[:3,:3]=Rot.from_quat(d[13:17]).as_matrix(); M[:3,3]=d[10:13]; blkT.append(M)
          10 +arm=[kin.fk((0,0,0),d[3:10]) for d in D]
          11 +def pred(p,i): return Tbase(D[i,:3])@T6(p[:6])@arm[i]@T6(p[6:12])
          12 +def res(p):
          13 +    r=[]
          14 +    for i in range(len(D)):
          15 +        P=pred(p,i); r.append(P[:3,3]-blkT[i][:3,3]); r.append(0.1*(P[:3,:3]-blkT[i][:3,:3]).ravel())
          16 +    return np.concatenate(r)
          17 +best=None
          18 +for k in range(5):
          19 +    p0=np.random.default_rng(k).normal(0,0.3,12) if k else np.zeros(12)
          20 +    s=least_squares(res,p0)
          21 +    if best is None or s.cost<best.cost: best=s
          22 +p=best.x; r=res(p).reshape(len(D),-1)
          23 +print('pos rms',np.sqrt((r[:,:3]**2).mean()), 'max',np.abs(r[:,:3]).max(), 'rot rms',np.sqrt((r[:,3:]**2).mean())*10)
          24 +B=T6(p[:6]); T=T6(p[6:12])
          25 +np.set_printoptions(precision=4,suppress=True)
          26 +print('B=\n',B,'\nB rpy',Rot.from_matrix(B[:3,:3]).as_euler('xyz'),'\nT=\n',T,'\nT rpy',Rot.from_matrix(T[:3,:3]).as_euler('xyz'))
          27 +print('grasp_tf',D[0,17:24])
          28 +np.save('dbg/fitp.npy',p)
diff --git a/calib_9.py b/calib_9.py
new file mode 100644
index 0000000..7f1d379
--- /dev/null
+++ b/calib_9.py
@@ -0,0 +1,10 @@
           1 +import numpy as np, kin
           2 +D=np.load('dbg/g1.npy')
           3 +for i in range(1,len(D)):
           4 +    db=D[i,:3]-D[i-1,:3]; dq=D[i,3:10]-D[i-1,3:10]
           5 +    if np.abs(db).max()>1e-6 and np.abs(dq).max()<1e-9:
           6 +        # predicted: rotate previous block pos about previous base (x,y) by dtheta then translate
           7 +        b0=D[i-1,:3]; b1=D[i,:3]; p0=D[i-1,10:13]; p1=D[i,10:13]
           8 +        rel=kin._rz(-b0[2])@(p0-[b0[0],b0[1],0]); pred=kin._rz(b1[2])@rel+[b1[0],b1[1],0]
           9 +        print(np.round(db,3),'err',np.round(p1-pred,4))
          10 +    if i>40: break
diff --git a/calib_u.py b/calib_u.py
new file mode 100644
index 0000000..0381a16
--- /dev/null
+++ b/calib_u.py
@@ -0,0 +1,29 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin
           3 +F=['joint_%d'%i for i in range(1,8)]
           4 +class R:
           5 +    def __init__(s): s.env=make_env()
           6 +    def reset(s,seed):
           7 +        s.obs,_=s.env.reset(seed=seed); s.r=s.obs.get_object_from_name('robot'); return s.obs
           8 +    def g(s,name,f): return s.obs.get(s.obs.get_object_from_name(name),f)
           9 +    def rob(s,f): return s.obs.get(s.r,f)
          10 +    def q(s): return np.array([s.rob(f) for f in F])
          11 +    def base(s): return (s.rob('pos_base_x'),s.rob('pos_base_y'),s.rob('pos_base_rot'))
          12 +    def blk(s,name='target_block'): return np.array([s.g(name,f) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
          13 +    def step(s,a):
          14 +        a=np.asarray(a,dtype=np.float32); s.obs,rew,term,trunc,info=s.env.step(a); return rew,term,info
          15 +    def stepq(s,dq,grip=0.0,db=(0,0,0)):
          16 +        a=np.zeros(11,np.float32); a[:3]=db; a[3:10]=dq; a[10]=grip
          17 +        v0=s.env and np.concatenate([s.q(),s.base()]); s.step(a)
          18 +        return not np.allclose(v0,np.concatenate([s.q(),s.base()]))
          19 +    def goq(s,qt,grip=0.0):
          20 +        q=s.q()
          21 +        while np.max(np.abs(qt-q))>1e-6:
          22 +            if not s.stepq(np.clip(qt-q,-0.19,0.19),grip): return False
          23 +            q=s.q()
          24 +        return True
          25 +    def go(s,p,yaw=0.0,grip=0.0,R=None,tool=None):
          26 +        qt,ok=kin.ik(s.base(),s.q(),np.array(p,float),kin.down_R(yaw) if R is None else R,tool=tool)
          27 +        if not ok: return None
          28 +        return s.goq(qt,grip)
          29 +    def ee(s,tool=None): return kin.fk(s.base(),s.q(),tool)
diff --git a/dbg/c2_1_-1.5708.txt b/dbg/c2_1_-1.5708.txt
new file mode 100644
index 0000000..52e5076
--- /dev/null
+++ b/dbg/c2_1_-1.5708.txt
@@ -0,0 +1,5 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/calib_2.py", line 20, in <module>
           3 +    xa=-res[0]; xb=res[2]; ya=-res[1]; yb=res[3]
           4 +       ^^^^^^^
           5 +TypeError: bad operand type for unary -: 'tuple'
diff --git a/dbg/c2_1_0.txt b/dbg/c2_1_0.txt
new file mode 100644
index 0000000..135093e
--- /dev/null
+++ b/dbg/c2_1_0.txt
@@ -0,0 +1 @@
           1 +seed 1 yaw 0.00 z 0.277 blk [0.138 0.183] he [0.028 0.039] | x: -0.191 -0.062 ctr +0.127 w 0.072 | y: 0.250 -0.250 ctr -0.000 w -0.578
diff --git a/dbg/c2_1_1.5708.txt b/dbg/c2_1_1.5708.txt
new file mode 100644
index 0000000..7bac9f8
--- /dev/null
+++ b/dbg/c2_1_1.5708.txt
@@ -0,0 +1 @@
           1 +seed 1 yaw 1.57 z 0.277 blk [0.138 0.183] he [0.028 0.039] | x: 0.250 -0.250 ctr -0.000 w -0.557 | y: 0.250 -0.250 ctr -0.000 w -0.578
diff --git a/dbg/c2_1_3.1416.txt b/dbg/c2_1_3.1416.txt
new file mode 100644
index 0000000..3384cbf
--- /dev/null
+++ b/dbg/c2_1_3.1416.txt
@@ -0,0 +1 @@
           1 +seed 1 yaw 3.14 z 0.277 blk [0.138 0.183] he [0.028 0.039] | x: -0.198 -0.042 ctr +0.120 w 0.099 | y: 0.250 -0.250 ctr -0.000 w -0.578
diff --git a/dbg/c2_3_-1.5708.txt b/dbg/c2_3_-1.5708.txt
new file mode 100644
index 0000000..52e5076
--- /dev/null
+++ b/dbg/c2_3_-1.5708.txt
@@ -0,0 +1,5 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/calib_2.py", line 20, in <module>
           3 +    xa=-res[0]; xb=res[2]; ya=-res[1]; yb=res[3]
           4 +       ^^^^^^^
           5 +TypeError: bad operand type for unary -: 'tuple'
diff --git a/dbg/c2_3_0.txt b/dbg/c2_3_0.txt
new file mode 100644
index 0000000..52e5076
--- /dev/null
+++ b/dbg/c2_3_0.txt
@@ -0,0 +1,5 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/calib_2.py", line 20, in <module>
           3 +    xa=-res[0]; xb=res[2]; ya=-res[1]; yb=res[3]
           4 +       ^^^^^^^
           5 +TypeError: bad operand type for unary -: 'tuple'
diff --git a/dbg/c2_3_1.5708.txt b/dbg/c2_3_1.5708.txt
new file mode 100644
index 0000000..52e5076
--- /dev/null
+++ b/dbg/c2_3_1.5708.txt
@@ -0,0 +1,5 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/calib_2.py", line 20, in <module>
           3 +    xa=-res[0]; xb=res[2]; ya=-res[1]; yb=res[3]
           4 +       ^^^^^^^
           5 +TypeError: bad operand type for unary -: 'tuple'
diff --git a/dbg/c2_3_3.1416.txt b/dbg/c2_3_3.1416.txt
new file mode 100644
index 0000000..52e5076
--- /dev/null
+++ b/dbg/c2_3_3.1416.txt
@@ -0,0 +1,5 @@
           1 +Traceback (most recent call last):
           2 +  File "/sandbox/calib_2.py", line 20, in <module>
           3 +    xa=-res[0]; xb=res[2]; ya=-res[1]; yb=res[3]
           4 +       ^^^^^^^
           5 +TypeError: bad operand type for unary -: 'tuple'
diff --git a/dbg/c5_1_0_-0.02.txt b/dbg/c5_1_0_-0.02.txt
new file mode 100644
index 0000000..f54e54f
--- /dev/null
+++ b/dbg/c5_1_0_-0.02.txt
@@ -0,0 +1 @@
           1 +-0.02 0.285 0.285 0.285 0.245 0.275 0.275 0.275 0.265 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_-0.04.txt b/dbg/c5_1_0_-0.04.txt
new file mode 100644
index 0000000..d396ab7
--- /dev/null
+++ b/dbg/c5_1_0_-0.04.txt
@@ -0,0 +1 @@
           1 +-0.04 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_-0.06.txt b/dbg/c5_1_0_-0.06.txt
new file mode 100644
index 0000000..0004d68
--- /dev/null
+++ b/dbg/c5_1_0_-0.06.txt
@@ -0,0 +1 @@
           1 +-0.06 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_-0.08.txt b/dbg/c5_1_0_-0.08.txt
new file mode 100644
index 0000000..189d136
--- /dev/null
+++ b/dbg/c5_1_0_-0.08.txt
@@ -0,0 +1 @@
           1 +-0.08 0.235 0.235 0.235 0.235 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_-0.10.txt b/dbg/c5_1_0_-0.10.txt
new file mode 100644
index 0000000..a262328
--- /dev/null
+++ b/dbg/c5_1_0_-0.10.txt
@@ -0,0 +1 @@
           1 +-0.10 0.235 0.235 0.235 0.235 0.235 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_-0.12.txt b/dbg/c5_1_0_-0.12.txt
new file mode 100644
index 0000000..8b4901d
--- /dev/null
+++ b/dbg/c5_1_0_-0.12.txt
@@ -0,0 +1 @@
           1 +-0.12 0.335 0.285 0.235 0.235 0.235 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_-0.14.txt b/dbg/c5_1_0_-0.14.txt
new file mode 100644
index 0000000..4ea00ae
--- /dev/null
+++ b/dbg/c5_1_0_-0.14.txt
@@ -0,0 +1 @@
           1 +-0.14 0.370 0.325 0.265 0.235 0.235 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_-0.16.txt b/dbg/c5_1_0_-0.16.txt
new file mode 100644
index 0000000..db4b55c
--- /dev/null
+++ b/dbg/c5_1_0_-0.16.txt
@@ -0,0 +1 @@
           1 +-0.16 0.400 0.355 0.280 0.235 0.235 0.235 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.00.txt b/dbg/c5_1_0_0.00.txt
new file mode 100644
index 0000000..5c33b59
--- /dev/null
+++ b/dbg/c5_1_0_0.00.txt
@@ -0,0 +1 @@
           1 ++0.00 0.290 0.285 0.285 0.245 0.275 0.275 0.275 0.265 0.240 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.02.txt b/dbg/c5_1_0_0.02.txt
new file mode 100644
index 0000000..376d646
--- /dev/null
+++ b/dbg/c5_1_0_0.02.txt
@@ -0,0 +1 @@
           1 ++0.02 0.290 0.285 0.285 0.240 0.275 0.275 0.275 0.265 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.04.txt b/dbg/c5_1_0_0.04.txt
new file mode 100644
index 0000000..59879d4
--- /dev/null
+++ b/dbg/c5_1_0_0.04.txt
@@ -0,0 +1 @@
           1 ++0.04 0.290 0.285 0.285 0.240 0.275 0.275 0.275 0.265 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.06.txt b/dbg/c5_1_0_0.06.txt
new file mode 100644
index 0000000..97548cb
--- /dev/null
+++ b/dbg/c5_1_0_0.06.txt
@@ -0,0 +1 @@
           1 ++0.06 0.245 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.08.txt b/dbg/c5_1_0_0.08.txt
new file mode 100644
index 0000000..f4bdcb1
--- /dev/null
+++ b/dbg/c5_1_0_0.08.txt
@@ -0,0 +1 @@
           1 ++0.08 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.10.txt b/dbg/c5_1_0_0.10.txt
new file mode 100644
index 0000000..efa8693
--- /dev/null
+++ b/dbg/c5_1_0_0.10.txt
@@ -0,0 +1 @@
           1 ++0.10 0.235 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.12.txt b/dbg/c5_1_0_0.12.txt
new file mode 100644
index 0000000..840f8da
--- /dev/null
+++ b/dbg/c5_1_0_0.12.txt
@@ -0,0 +1 @@
           1 ++0.12 0.235 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.14.txt b/dbg/c5_1_0_0.14.txt
new file mode 100644
index 0000000..3693d61
--- /dev/null
+++ b/dbg/c5_1_0_0.14.txt
@@ -0,0 +1 @@
           1 ++0.14 0.235 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5_1_0_0.16.txt b/dbg/c5_1_0_0.16.txt
new file mode 100644
index 0000000..617c990
--- /dev/null
+++ b/dbg/c5_1_0_0.16.txt
@@ -0,0 +1 @@
           1 ++0.16 0.235 0.240 0.240 0.240 0.240 0.240 0.240 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235 0.235
diff --git a/dbg/c5b_0_-0.01.txt b/dbg/c5b_0_-0.01.txt
new file mode 100644
index 0000000..9ef3234
--- /dev/null
+++ b/dbg/c5b_0_-0.01.txt
@@ -0,0 +1 @@
           1 +-0.01 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_-0.02.txt b/dbg/c5b_0_-0.02.txt
new file mode 100644
index 0000000..6118036
--- /dev/null
+++ b/dbg/c5b_0_-0.02.txt
@@ -0,0 +1 @@
           1 +-0.02 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_-0.03.txt b/dbg/c5b_0_-0.03.txt
new file mode 100644
index 0000000..cfc4628
--- /dev/null
+++ b/dbg/c5b_0_-0.03.txt
@@ -0,0 +1 @@
           1 +-0.03 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_-0.04.txt b/dbg/c5b_0_-0.04.txt
new file mode 100644
index 0000000..c5386c7
--- /dev/null
+++ b/dbg/c5b_0_-0.04.txt
@@ -0,0 +1 @@
           1 +-0.04 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_-0.05.txt b/dbg/c5b_0_-0.05.txt
new file mode 100644
index 0000000..8f36ace
--- /dev/null
+++ b/dbg/c5b_0_-0.05.txt
@@ -0,0 +1 @@
           1 +-0.05 0.125 0.120 0.117 0.117 0.117 0.117 0.117 0.107 0.105 0.107 0.117 0.117 0.117 0.117 0.117 0.117 0.117
diff --git a/dbg/c5b_0_-0.06.txt b/dbg/c5b_0_-0.06.txt
new file mode 100644
index 0000000..86dcac8
--- /dev/null
+++ b/dbg/c5b_0_-0.06.txt
@@ -0,0 +1 @@
           1 +-0.06 0.135 0.130 0.125 0.117 0.110 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_0_-0.07.txt b/dbg/c5b_0_-0.07.txt
new file mode 100644
index 0000000..8804525
--- /dev/null
+++ b/dbg/c5b_0_-0.07.txt
@@ -0,0 +1 @@
           1 +-0.07 0.142 0.140 0.132 0.127 0.120 0.112 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_0_-0.08.txt b/dbg/c5b_0_-0.08.txt
new file mode 100644
index 0000000..1e9f99f
--- /dev/null
+++ b/dbg/c5b_0_-0.08.txt
@@ -0,0 +1 @@
           1 +-0.08 0.152 0.147 0.140 0.135 0.127 0.120 0.112 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_0_0.00.txt b/dbg/c5b_0_0.00.txt
new file mode 100644
index 0000000..5a94653
--- /dev/null
+++ b/dbg/c5b_0_0.00.txt
@@ -0,0 +1 @@
           1 ++0.00 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_0.01.txt b/dbg/c5b_0_0.01.txt
new file mode 100644
index 0000000..ebb8c08
--- /dev/null
+++ b/dbg/c5b_0_0.01.txt
@@ -0,0 +1 @@
           1 ++0.01 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_0.02.txt b/dbg/c5b_0_0.02.txt
new file mode 100644
index 0000000..0cefe12
--- /dev/null
+++ b/dbg/c5b_0_0.02.txt
@@ -0,0 +1 @@
           1 ++0.02 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_0.03.txt b/dbg/c5b_0_0.03.txt
new file mode 100644
index 0000000..5c3f880
--- /dev/null
+++ b/dbg/c5b_0_0.03.txt
@@ -0,0 +1 @@
           1 ++0.03 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_0.04.txt b/dbg/c5b_0_0.04.txt
new file mode 100644
index 0000000..d514e8e
--- /dev/null
+++ b/dbg/c5b_0_0.04.txt
@@ -0,0 +1 @@
           1 ++0.04 0.150 0.155 0.155 0.155 0.155 0.155 0.155 0.107 0.105 0.107 0.155 0.155 0.155 0.155 0.155 0.155 0.150
diff --git a/dbg/c5b_0_0.05.txt b/dbg/c5b_0_0.05.txt
new file mode 100644
index 0000000..08a5cae
--- /dev/null
+++ b/dbg/c5b_0_0.05.txt
@@ -0,0 +1 @@
           1 ++0.05 0.117 0.117 0.117 0.117 0.117 0.117 0.117 0.107 0.105 0.107 0.117 0.117 0.117 0.117 0.117 0.117 0.117
diff --git a/dbg/c5b_0_0.06.txt b/dbg/c5b_0_0.06.txt
new file mode 100644
index 0000000..5f4eed2
--- /dev/null
+++ b/dbg/c5b_0_0.06.txt
@@ -0,0 +1 @@
           1 ++0.06 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_0_0.07.txt b/dbg/c5b_0_0.07.txt
new file mode 100644
index 0000000..0c68951
--- /dev/null
+++ b/dbg/c5b_0_0.07.txt
@@ -0,0 +1 @@
           1 ++0.07 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_0_0.08.txt b/dbg/c5b_0_0.08.txt
new file mode 100644
index 0000000..0d9e4f0
--- /dev/null
+++ b/dbg/c5b_0_0.08.txt
@@ -0,0 +1 @@
           1 ++0.08 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_-0.01.txt b/dbg/c5b_1.5708_-0.01.txt
new file mode 100644
index 0000000..05463c6
--- /dev/null
+++ b/dbg/c5b_1.5708_-0.01.txt
@@ -0,0 +1 @@
           1 +-0.01 0.072 0.067 0.060 0.072 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_-0.02.txt b/dbg/c5b_1.5708_-0.02.txt
new file mode 100644
index 0000000..c582c54
--- /dev/null
+++ b/dbg/c5b_1.5708_-0.02.txt
@@ -0,0 +1 @@
           1 +-0.02 0.090 0.085 0.077 0.072 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_-0.03.txt b/dbg/c5b_1.5708_-0.03.txt
new file mode 100644
index 0000000..5b8c17c
--- /dev/null
+++ b/dbg/c5b_1.5708_-0.03.txt
@@ -0,0 +1 @@
           1 +-0.03 0.105 0.097 0.092 0.085 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_-0.04.txt b/dbg/c5b_1.5708_-0.04.txt
new file mode 100644
index 0000000..b0ca567
--- /dev/null
+++ b/dbg/c5b_1.5708_-0.04.txt
@@ -0,0 +1 @@
           1 +-0.04 0.115 0.110 0.105 0.100 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_-0.05.txt b/dbg/c5b_1.5708_-0.05.txt
new file mode 100644
index 0000000..8959ac2
--- /dev/null
+++ b/dbg/c5b_1.5708_-0.05.txt
@@ -0,0 +1 @@
           1 +-0.05 0.125 0.120 0.115 0.110 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_-0.06.txt b/dbg/c5b_1.5708_-0.06.txt
new file mode 100644
index 0000000..b1233b4
--- /dev/null
+++ b/dbg/c5b_1.5708_-0.06.txt
@@ -0,0 +1 @@
           1 +-0.06 0.135 0.130 0.125 0.120 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_-0.07.txt b/dbg/c5b_1.5708_-0.07.txt
new file mode 100644
index 0000000..45c93d4
--- /dev/null
+++ b/dbg/c5b_1.5708_-0.07.txt
@@ -0,0 +1 @@
           1 +-0.07 0.142 0.140 0.135 0.130 0.122 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_-0.08.txt b/dbg/c5b_1.5708_-0.08.txt
new file mode 100644
index 0000000..9795f4d
--- /dev/null
+++ b/dbg/c5b_1.5708_-0.08.txt
@@ -0,0 +1 @@
           1 +-0.08 0.152 0.147 0.142 0.137 0.130 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.00.txt b/dbg/c5b_1.5708_0.00.txt
new file mode 100644
index 0000000..fd90bc8
--- /dev/null
+++ b/dbg/c5b_1.5708_0.00.txt
@@ -0,0 +1 @@
           1 ++0.00 0.060 0.060 0.060 0.072 0.107 0.107 0.107 0.107 0.107 0.107 0.107 0.107 0.107 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.01.txt b/dbg/c5b_1.5708_0.01.txt
new file mode 100644
index 0000000..7497653
--- /dev/null
+++ b/dbg/c5b_1.5708_0.01.txt
@@ -0,0 +1 @@
           1 ++0.01 0.060 0.060 0.060 0.072 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.02.txt b/dbg/c5b_1.5708_0.02.txt
new file mode 100644
index 0000000..a6bb7cc
--- /dev/null
+++ b/dbg/c5b_1.5708_0.02.txt
@@ -0,0 +1 @@
           1 ++0.02 0.060 0.060 0.060 0.072 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.03.txt b/dbg/c5b_1.5708_0.03.txt
new file mode 100644
index 0000000..722621f
--- /dev/null
+++ b/dbg/c5b_1.5708_0.03.txt
@@ -0,0 +1 @@
           1 ++0.03 0.060 0.060 0.060 0.072 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.04.txt b/dbg/c5b_1.5708_0.04.txt
new file mode 100644
index 0000000..b7fb752
--- /dev/null
+++ b/dbg/c5b_1.5708_0.04.txt
@@ -0,0 +1 @@
           1 ++0.04 0.060 0.060 0.060 0.072 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.05.txt b/dbg/c5b_1.5708_0.05.txt
new file mode 100644
index 0000000..08dc9b2
--- /dev/null
+++ b/dbg/c5b_1.5708_0.05.txt
@@ -0,0 +1 @@
           1 ++0.05 0.060 0.060 0.060 0.072 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.06.txt b/dbg/c5b_1.5708_0.06.txt
new file mode 100644
index 0000000..685abde
--- /dev/null
+++ b/dbg/c5b_1.5708_0.06.txt
@@ -0,0 +1 @@
           1 ++0.06 0.060 0.060 0.060 0.067 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.07.txt b/dbg/c5b_1.5708_0.07.txt
new file mode 100644
index 0000000..6be0d5e
--- /dev/null
+++ b/dbg/c5b_1.5708_0.07.txt
@@ -0,0 +1 @@
           1 ++0.07 0.060 0.060 0.060 0.067 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/c5b_1.5708_0.08.txt b/dbg/c5b_1.5708_0.08.txt
new file mode 100644
index 0000000..47d596f
--- /dev/null
+++ b/dbg/c5b_1.5708_0.08.txt
@@ -0,0 +1 @@
           1 ++0.08 0.060 0.060 0.060 0.067 0.117 0.155 0.155 0.155 0.155 0.155 0.155 0.155 0.117 0.105 0.105 0.105 0.105
diff --git a/dbg/fitp.npy b/dbg/fitp.npy
new file mode 100644
index 0000000..d149873
Binary files /dev/null and b/dbg/fitp.npy differ
diff --git a/dbg/g1.npy b/dbg/g1.npy
new file mode 100644
index 0000000..bd1b6eb
Binary files /dev/null and b/dbg/g1.npy differ
diff --git a/dbg/g5.npy b/dbg/g5.npy
new file mode 100644
index 0000000..ac9fd13
Binary files /dev/null and b/dbg/g5.npy differ
diff --git a/dbg/g6.npy b/dbg/g6.npy
new file mode 100644
index 0000000..d7ad5ac
Binary files /dev/null and b/dbg/g6.npy differ
diff --git a/dbg/kin_orig.py b/dbg/kin_orig.py
new file mode 100644
index 0000000..49670b8
--- /dev/null
+++ b/dbg/kin_orig.py
@@ -0,0 +1,73 @@
           1 +import numpy as np
           2 +PI = np.pi
           3 +
           4 +def _rpy(r, p, y):
           5 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           6 +    return np.array([[cy*cp, cy*sp*sr-sy*cr, cy*sp*cr+sy*sr],
           7 +                     [sy*cp, sy*sp*sr+cy*cr, sy*sp*cr-cy*sr],
           8 +                     [-sp, cp*sr, cp*cr]])
           9 +
          10 +def _T(xyz, R):
          11 +    M = np.eye(4); M[:3, :3] = R; M[:3, 3] = xyz; return M
          12 +
          13 +def _rz(q):
          14 +    c, s = np.cos(q), np.sin(q)
          15 +    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
          16 +
          17 +_J = [((0, 0, 0.15643), (PI, 0, 0)), ((0, 0.005375, -0.12838), (PI/2, 0, 0)),
          18 +      ((0, -0.21038, -0.006375), (-PI/2, 0, 0)), ((0, 0.006375, -0.21038), (PI/2, 0, 0)),
          19 +      ((0, -0.20843, -0.006375), (-PI/2, 0, 0)), ((0, 0.00017505, -0.10593), (PI/2, 0, 0)),
          20 +      ((0, -0.10593, -0.00017505), (-PI/2, 0, 0))]
          21 +_JT = [_T(xyz, _rpy(*r)) for xyz, r in _J]
          22 +_EE = _T((0, 0, -0.061525), _rpy(PI, 0, 0))
          23 +
          24 +BASE_Z = 0.0
          25 +TOOL = 0.0
          26 +
          27 +def fk(base, q, tool=None):
          28 +    if tool is None:
          29 +        tool = TOOL
          30 +    bx, by, br = base
          31 +    M = _T((bx, by, BASE_Z), _rz(br))
          32 +    for Jt, qi in zip(_JT, q):
          33 +        M = M @ Jt @ _T((0, 0, 0), _rz(qi))
          34 +    M = M @ _EE
          35 +    if tool:
          36 +        M = M @ _T((0, 0, tool), np.eye(3))
          37 +    return M
          38 +
          39 +def _err(M, pos, R):
          40 +    ep = pos - M[:3, 3]
          41 +    Re = R @ M[:3, :3].T
          42 +    # rotation error as axis-angle (small-angle approx ok via skew)
          43 +    eo = 0.5 * np.array([Re[2, 1]-Re[1, 2], Re[0, 2]-Re[2, 0], Re[1, 0]-Re[0, 1]])
          44 +    return np.concatenate([ep, eo])
          45 +
          46 +def ik(base, q0, pos, R, iters=200, tol=1e-4, rot_w=0.3, tool=None):
          47 +    q = np.array(q0, dtype=float)
          48 +    W = np.array([1, 1, 1, rot_w, rot_w, rot_w])
          49 +    for _ in range(iters):
          50 +        M = fk(base, q, tool)
          51 +        e = _err(M, pos, R) * W
          52 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < tol*3:
          53 +            return q, True
          54 +        Jm = np.zeros((6, 7))
          55 +        h = 1e-6
          56 +        for i in range(7):
          57 +            dq = q.copy(); dq[i] += h
          58 +            Jm[:, i] = (_err(M, pos, R) - _err(fk(base, dq, tool), pos, R)) * W / h
          59 +        lam = 1e-3
          60 +        d = Jm.T @ np.linalg.solve(Jm @ Jm.T + lam*np.eye(6), e)
          61 +        n = np.max(np.abs(d))
          62 +        if n > 0.3:
          63 +            d *= 0.3 / n
          64 +        q = q + d
          65 +    M = fk(base, q, tool)
          66 +    e = _err(M, pos, R)
          67 +    return q, bool(np.linalg.norm(e[:3]) < 1e-3 and np.linalg.norm(e[3:]) < 1e-2)
          68 +
          69 +def down_R(yaw):
          70 +    # gripper z axis pointing down, x axis direction by yaw
          71 +    c, s = np.cos(yaw), np.sin(yaw)
          72 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          73 +    return np.stack([x, y, z], axis=1)
diff --git a/kin.py b/kin.py
index 49670b8..eb41d9d 100644
--- a/kin.py
+++ b/kin.py
@@ -23,12 +23,17 @@ _EE = _T((0, 0, -0.061525), _rpy(PI, 0, 0))
   23     23  
   24     24  BASE_Z = 0.0
   25     25  TOOL = 0.0
          26 +# Calibrated from grasped-block poses (fit rms 5e-7 m): the arm's base link sits at
          27 +# this offset from (pos_base_x, pos_base_y, 0), expressed in the mobile-base frame.
          28 +ARM_OFFSET = (0.1199, 0.0, -0.0052)
          29 +# grasp_tf_* is the block pose relative to the frame end_effector_link @ Tz(GRASP_Z).
          30 +GRASP_Z = 0.12
   26     31  
   27     32  def fk(base, q, tool=None):
   28     33      if tool is None:
   29     34          tool = TOOL
   30     35      bx, by, br = base
   31        -    M = _T((bx, by, BASE_Z), _rz(br))
          36 +    M = _T((bx, by, BASE_Z), _rz(br)) @ _T(ARM_OFFSET, np.eye(3))
   32     37      for Jt, qi in zip(_JT, q):
   33     38          M = M @ Jt @ _T((0, 0, 0), _rz(qi))
   34     39      M = M @ _EE
@@ -39,8 +44,18 @@ def fk(base, q, tool=None):
   39     44  def _err(M, pos, R):
   40     45      ep = pos - M[:3, 3]
   41     46      Re = R @ M[:3, :3].T
   42        -    # rotation error as axis-angle (small-angle approx ok via skew)
   43        -    eo = 0.5 * np.array([Re[2, 1]-Re[1, 2], Re[0, 2]-Re[2, 0], Re[1, 0]-Re[0, 1]])
          47 +    # rotation error as proper axis-angle (log map); the old skew-only version
          48 +    # was blind to 180-degree flips and let IK converge to flipped wrists.
          49 +    v = 0.5 * np.array([Re[2, 1]-Re[1, 2], Re[0, 2]-Re[2, 0], Re[1, 0]-Re[0, 1]])
          50 +    c = np.clip((np.trace(Re) - 1) / 2, -1.0, 1.0); sn = np.linalg.norm(v)
          51 +    ang = np.arctan2(sn, c)
          52 +    if sn > 1e-9:
          53 +        eo = v / sn * ang
          54 +    elif c > 0:
          55 +        eo = v
          56 +    else:  # ~180 deg: axis from the symmetric part
          57 +        B = (Re + np.eye(3)) / 2
          58 +        ax = B[:, np.argmax(np.diag(B))]; eo = ax / np.linalg.norm(ax) * np.pi
   44     59      return np.concatenate([ep, eo])
   45     60  
   46     61  def ik(base, q0, pos, R, iters=200, tol=1e-4, rot_w=0.3, tool=None):
diff --git a/stats.py b/stats.py
new file mode 100644
index 0000000..8f625b5
--- /dev/null
+++ b/stats.py
@@ -0,0 +1,10 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env()
           4 +for s in range(0,40):
           5 +    obs,info=env.reset(seed=s)
           6 +    g=lambda n,f: obs.get(obs.get_object_from_name(n),f)
           7 +    names=sorted(obs.get_object_names())
           8 +    obst=[n for n in names if n.startswith('obs')]
           9 +    print(s, info['object_count'], "reg",round(g('target_region','pose_x'),2),round(g('target_region','pose_y'),2), "blk",round(g('target_block','pose_x'),2),round(g('target_block','pose_y'),2),
          10 +      "yaw?",round(g('target_block','pose_qz'),2), "obs",[(round(g(n,'pose_x'),2),round(g(n,'pose_y'),2),round(g(n,'pose_z'),3)) for n in obst])
```

</details>

<a id="C004"></a>
### C004 · Cartesian straight-line waypoint execution

Commit `ae6fc4bc5410cf1faf89745b115c1baf8970b8d2`; parents: d6db4fc3270cc809eea1acd23aef24d2876c28a9. Recorded author date: 2026-09-30T21:00:57+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0434](01_timeline.md#E0434): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_ae6fc4b_approach.py) · [Exact all-file diff](evidence/diffs/C004_ae6fc4b.diff)

[Previous saved controller snapshot](evidence/versions/C003_d6db4fc_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 917085e..ddc2400 100644
--- a/approach.py
+++ b/approach.py
@@ -172,19 +172,31 @@ class GeneratedApproach:
  172    172              a[10] = 1.0
  173    173              return a
  174    174          if self.qtarget is None:
         175 +            M = fk(base, q, TOOL)
         176 +            p0 = M[:3, 3].copy(); y0 = np.arctan2(M[1, 0], M[0, 0])
  175    177              if kind == 'move':
  176    178                  pos, yaw = cmd[1], cmd[2]
  177    179              elif kind == 'place_move':
  178    180                  pos, yaw = self._tcp_target_for_block(s, cmd[1], cmd[2]), cmd[2]
  179    181              elif kind == 'move_rel_up':
  180        -                M = fk(base, q, TOOL)
  181        -                pos = M[:3, 3].copy(); pos[2] = max(pos[2], cmd[1])
  182        -                yaw = np.arctan2(M[1, 0], M[0, 0]) if cmd[2] is None else cmd[2]
  183        -            qt, ok = ik(base, q, pos, down_R(yaw), tool=TOOL)
  184        -            self.qtarget = qt
         182 +                pos = p0.copy(); pos[2] = max(pos[2], cmd[1])
         183 +                yaw = y0 if cmd[2] is None else cmd[2]
         184 +            dy = _wrap(yaw - y0)
         185 +            n = int(np.ceil(max(np.linalg.norm(pos - p0) / 0.01, abs(dy) / 0.1, 1)))
         186 +            path = []
         187 +            qc = q.copy()
         188 +            for i in range(1, n + 1):
         189 +                f = i / n
         190 +                qc, ok = ik(base, qc, p0 + f * (pos - p0), down_R(y0 + f * dy), tool=TOOL,
         191 +                            iters=100 if i < n else 300)
         192 +                path.append(qc.copy())
         193 +            self.qtarget = path
  185    194              self.last_q = None
  186        -        d = self.qtarget - q
  187        -        if np.max(np.abs(d)) < 1e-4:
         195 +        path = self.qtarget
         196 +        # drop waypoints already reached
         197 +        while len(path) > 1 and np.max(np.abs(path[0] - q)) < 1e-4:
         198 +            path.pop(0)
         199 +        if np.max(np.abs(path[-1] - q)) < 1e-4:
  188    200              self.queue.pop(0)
  189    201              self.qtarget = None
  190    202              return None
@@ -194,8 +206,12 @@ class GeneratedApproach:
  194    206              self.queue.pop(0)
  195    207              self.qtarget = None
  196    208              if not allow:
  197        -                self.queue = []  # replan
         209 +                self.queue = [('move_rel_up', SAFE_Z + 0.03, None, True)]  # retreat, then replan
  198    210              return None
         211 +        # furthest waypoint reachable in one step
         212 +        k = 0
         213 +        while k + 1 < len(path) and np.max(np.abs(path[k + 1] - q)) <= MAXD:
         214 +            k += 1
  199    215          self.last_q = q.copy()
  200        -        a[3:10] = np.clip(d, -MAXD, MAXD)
         216 +        a[3:10] = np.clip(path[k] - q, -MAXD, MAXD)
  201    217          return a
diff --git a/trace.py b/trace.py
new file mode 100644
index 0000000..87481c9
--- /dev/null
+++ b/trace.py
@@ -0,0 +1,17 @@
           1 +import sys, time, numpy as np
           2 +from env_client import make_env
           3 +import approach, kin
           4 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 200
           5 +env=make_env(); obs,info=env.reset(seed=seed)
           6 +ap=approach.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
           7 +tc=0
           8 +for t in range(N):
           9 +    t0=time.time(); a=ap.get_action(obs); tc+=time.time()-t0
          10 +    r=obs.get_object_from_name('robot')
          11 +    q=np.array([obs.get(r,f) for f in approach.JF]); base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          12 +    tcp=kin.fk(base,q,0.12)[:3,3]
          13 +    cmd=ap.queue[0] if ap.queue else None
          14 +    print(t, cmd[0] if cmd else None, np.round(cmd[1],3) if cmd is not None and not isinstance(cmd[1],str) else (cmd[1] if cmd else ''), "tcp",np.round(tcp,3),"g",obs.get(r,'grasp_active'), "a",np.round(a[3:10],2).tolist(), a[10])
          15 +    obs,rew,term,trunc,info=env.step(a)
          16 +    if term: print("TERM"); break
          17 +print("compute time",tc)
```

</details>

<a id="C005"></a>
### C005 · fix waypoint index tracking

Commit `03653b71da0d39f05fb0ae8ea71dd1767c3f04fe`; parents: ae6fc4bc5410cf1faf89745b115c1baf8970b8d2. Recorded author date: 2026-09-30T21:01:21+02:00.

File roles (automatic): policy.

- [E0439](01_timeline.md#E0439): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_03653b7_approach.py) · [Exact all-file diff](evidence/diffs/C005_03653b7.diff)

[Previous saved controller snapshot](evidence/versions/C004_ae6fc4b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ddc2400..33bb7a6 100644
--- a/approach.py
+++ b/approach.py
@@ -191,11 +191,9 @@ class GeneratedApproach:
  191    191                              iters=100 if i < n else 300)
  192    192                  path.append(qc.copy())
  193    193              self.qtarget = path
         194 +            self.pidx = 0
  194    195              self.last_q = None
  195    196          path = self.qtarget
  196        -        # drop waypoints already reached
  197        -        while len(path) > 1 and np.max(np.abs(path[0] - q)) < 1e-4:
  198        -            path.pop(0)
  199    197          if np.max(np.abs(path[-1] - q)) < 1e-4:
  200    198              self.queue.pop(0)
  201    199              self.qtarget = None
@@ -209,9 +207,10 @@ class GeneratedApproach:
  209    207                  self.queue = [('move_rel_up', SAFE_Z + 0.03, None, True)]  # retreat, then replan
  210    208              return None
  211    209          # furthest waypoint reachable in one step
  212        -        k = 0
         210 +        k = self.pidx
  213    211          while k + 1 < len(path) and np.max(np.abs(path[k + 1] - q)) <= MAXD:
  214    212              k += 1
  215    213          self.last_q = q.copy()
         214 +        self.pidx = k
  216    215          a[3:10] = np.clip(path[k] - q, -MAXD, MAXD)
  217    216          return a
```

</details>

<a id="C006"></a>
### C006 · grasp height centre+0.035

Commit `18af7ccf645cff0944bdb70f7f7ff9f67300d67b`; parents: 03653b71da0d39f05fb0ae8ea71dd1767c3f04fe. Recorded author date: 2026-09-30T21:11:28+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0489](01_timeline.md#E0489): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_18af7cc_approach.py) · [Exact all-file diff](evidence/diffs/C006_18af7cc.diff)

[Previous saved controller snapshot](evidence/versions/C005_03653b7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 33bb7a6..fd607d9 100644
--- a/approach.py
+++ b/approach.py
@@ -86,8 +86,7 @@ class GeneratedApproach:
   86     86          p = _pose(s, obj)
   87     87          h = _he(s, obj)
   88     88          yaw = self._grasp_yaw(s, obj, q, base)
   89        -        gz = p[2] + min(0.03, h[2] + 0.005)  # TCP height for grasp
   90        -        gz = max(gz, 0.108)
          89 +        gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
   91     90          place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
   92     91          return [
   93     92              ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
diff --git a/gsweep.py b/gsweep.py
new file mode 100644
index 0000000..3fe18e9
--- /dev/null
+++ b/gsweep.py
@@ -0,0 +1,25 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin, sys
           3 +F=['joint_%d'%i for i in range(1,8)]
           4 +seed=int(sys.argv[1]); name=sys.argv[2]; yaw=float(sys.argv[3])
           5 +env=make_env()
           6 +res=[]
           7 +for dz in [0.0,0.01,0.02,0.03,0.04,0.05]:
           8 +    obs,_=env.reset(seed=seed)
           9 +    r=obs.get_object_from_name('robot'); o=obs.get_object_from_name(name)
          10 +    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          11 +    p=np.array([obs.get(o,f) for f in ['pose_x','pose_y','pose_z']])
          12 +    q=np.array([obs.get(r,f) for f in F])
          13 +    blocked=False
          14 +    for z in list(np.arange(0.3,p[2]+dz,-0.01))+[p[2]+dz]:
          15 +        qt,ok=kin.ik(base,q,np.array([p[0],p[1],z]),kin.down_R(yaw),tool=0.12)
          16 +        while np.max(np.abs(qt-q))>1e-6:
          17 +            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
          18 +            obs,_,_,_,_=env.step(a); qn=np.array([obs.get(r,f) for f in F])
          19 +            if np.allclose(qn,q): blocked=True; break
          20 +            q=qn
          21 +        if blocked: break
          22 +    a=np.zeros(11,dtype=np.float32); a[10]=-1
          23 +    obs,_,_,_,_=env.step(a)
          24 +    res.append((dz, 'B' if blocked else '', round(kin.fk(base,q,0.12)[2,3]-p[2],3), obs.get(r,'grasp_active'), round(obs.get(r,'finger_state'),3)))
          25 +print(seed,name,yaw,res)
```

</details>

<a id="C007"></a>
### C007 · finger clearance-aware grasp yaw, place yaw from grasp_tf

Commit `81d1da0b4ed93714e6c822279c1dcc60aaac8e08`; parents: 18af7ccf645cff0944bdb70f7f7ff9f67300d67b. Recorded author date: 2026-09-30T21:17:12+02:00.

File roles (automatic): policy.

- [E0506](01_timeline.md#E0506): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_81d1da0_approach.py) · [Exact all-file diff](evidence/diffs/C007_81d1da0.diff)

[Previous saved controller snapshot](evidence/versions/C006_18af7cc_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fd607d9..415478d 100644
--- a/approach.py
+++ b/approach.py
@@ -7,6 +7,9 @@ MAXD = 0.19
    7      7  SAFE_Z = 0.27        # TCP transit height
    8      8  TABLE_Z = 0.075
    9      9  X_RANGE = (0.12, 0.44)
          10 +FINGER_OFF = 0.052   # finger centre offset along EE x (open)
          11 +FINGER_HX = 0.011
          12 +FINGER_HY = 0.013
   10     13  Y_RANGE = (-0.36, 0.36)
   11     14  
   12     15  
@@ -38,6 +41,8 @@ class GeneratedApproach:
   38     41          self.cur = None
   39     42          self.last_q = None
   40     43          self.retries = 0
          44 +        self.grasp_fail = 0
          45 +        self.place_yaw = None
   41     46  
   42     47      def _robot(self, s):
   43     48          r = s.get_object_from_name('robot')
@@ -68,24 +73,66 @@ class GeneratedApproach:
   68     73                      best, bestscore = (x, y), score
   69     74          return np.array(best)
   70     75  
   71        -    def _grasp_yaw(self, s, obj, q, base):
          76 +    def _obj_yaw(self, s, o):
          77 +        R = _quat_R(*[s.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')])
          78 +        return np.arctan2(R[1, 0], R[0, 0])
          79 +
          80 +    def _finger_clearance(self, s, obj, yaw, others):
          81 +        """Min clearance between finger boxes (at obj, given yaw) and other objects' footprints."""
          82 +        p = _pose(s, obj)
          83 +        c, sn = np.cos(yaw), np.sin(yaw)
          84 +        ax = np.array([c, sn]); ay = np.array([-sn, c])
          85 +        best = 1e9
          86 +        for o in others:
          87 +            op, oh = _pose(s, o), _he(s, o)
          88 +            if op[2] + oh[2] < p[2] - 0.035:   # below fingertips
          89 +                continue
          90 +            oyaw = self._obj_yaw(s, o)
          91 +            oc, os_ = np.cos(oyaw), np.sin(oyaw)
          92 +            corners = [op[:2] + sx * oh[0] * np.array([oc, os_]) + sy * oh[1] * np.array([-os_, oc])
          93 +                       for sx in (-1, 1) for sy in (-1, 1)]
          94 +            for side in (-1, 1):
          95 +                fc = p[:2] + side * FINGER_OFF * ax
          96 +                # separating-axis distance between finger rect and object rect
          97 +                d = -1e9
          98 +                for axis in (ax, ay, np.array([oc, os_]), np.array([-os_, oc])):
          99 +                    fr = FINGER_HX * abs(axis @ ax) + FINGER_HY * abs(axis @ ay)
         100 +                    pr = [axis @ (cc - fc) for cc in corners]
         101 +                    gap = max(min(pr) - fr, -fr - max(pr))
         102 +                    d = max(d, gap)
         103 +                best = min(best, d)
         104 +        return best
         105 +
         106 +    def _grasp_yaw(self, s, obj, q, base, others, aligned_only):
   72    107          h = _he(s, obj)
   73        -        R = _quat_R(*[s.get(obj, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')])
   74        -        oyaw = np.arctan2(R[1, 0], R[0, 0])
   75        -        # fingers close along EE x: span the smaller side
   76        -        yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
   77        -        # choose yaw or yaw+pi closest to current gripper yaw
         108 +        oyaw = self._obj_yaw(s, obj)
   78    109          M = fk(base, q, TOOL)
   79    110          cy = np.arctan2(M[1, 0], M[0, 0])
   80        -        if abs(_wrap(yaw - cy)) > np.pi / 2:
   81        -            yaw += np.pi
   82        -        return _wrap(yaw)
         111 +        steps = 4 if aligned_only else 24
         112 +        cands = []
         113 +        for k in range(steps):
         114 +            yaw = oyaw + k * (2 * np.pi / steps)
         115 +            rel = yaw - oyaw
         116 +            span = abs(np.cos(rel)) * h[0] + abs(np.sin(rel)) * h[1]
         117 +            if span > 0.041:
         118 +                continue
         119 +            clr = self._finger_clearance(s, obj, yaw, others)
         120 +            score = min(clr, 0.02) - 0.002 * abs(_wrap(yaw - cy)) - 0.01 * span \
         121 +                - (0.0 if abs(np.sin(2 * rel)) < 1e-6 else 0.005)
         122 +            cands.append((score, _wrap(yaw)))
         123 +        if not cands:
         124 +            yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
         125 +            return _wrap(yaw)
         126 +        cands.sort(reverse=True)
         127 +        idx = min(self.grasp_fail, len(cands) - 1)
         128 +        return cands[idx][1]
   83    129  
   84        -    def _plan_pick_place(self, s, obj, place_xy, support_top):
         130 +    def _plan_pick_place(self, s, obj, place_xy, support_top, others, place_yaw=None):
   85    131          _, q, base = self._robot(s)
   86    132          p = _pose(s, obj)
   87    133          h = _he(s, obj)
   88        -        yaw = self._grasp_yaw(s, obj, q, base)
         134 +        yaw = self._grasp_yaw(s, obj, q, base, others, place_yaw is not None)
         135 +        self.place_yaw = place_yaw
   89    136          gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
   90    137          place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
   91    138          return [
@@ -113,9 +160,11 @@ class GeneratedApproach:
  113    160              o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2])
  114    161              others = [c for c in cubes if c.name != o.name] + [reg, tb]
  115    162              spot = self._free_spot(s, o, others, cur)
  116        -            return self._plan_pick_place(s, o, spot, TABLE_Z)
         163 +            return self._plan_pick_place(s, o, spot, TABLE_Z, others)
  117    164          rp = _pose(s, reg)
  118        -        return self._plan_pick_place(s, tb, rp[:2], rp[2] + _he(s, reg)[2])
         165 +        others = cubes
         166 +        return self._plan_pick_place(s, tb, rp[:2], rp[2] + _he(s, reg)[2], others,
         167 +                                     place_yaw=self._obj_yaw(s, reg))
  119    168  
  120    169      # ------------------------------------------------------------------ execution
  121    170      def _tcp_target_for_block(self, s, center, yaw):
@@ -124,6 +173,19 @@ class GeneratedApproach:
  124    173          t = np.array([s.get(r, 'grasp_tf_x'), s.get(r, 'grasp_tf_y'), s.get(r, 'grasp_tf_z')])
  125    174          return center - down_R(yaw) @ t
  126    175  
         176 +    def _resolve_place_yaw(self, s, yaw, cur_yaw):
         177 +        if self.place_yaw is None:
         178 +            return yaw
         179 +        r = s.get_object_from_name('robot')
         180 +        Rtf = _quat_R(*[s.get(r, f) for f in ('grasp_tf_qx', 'grasp_tf_qy', 'grasp_tf_qz', 'grasp_tf_qw')])
         181 +        Rb = down_R(0.0) @ Rtf
         182 +        rel = np.arctan2(Rb[1, 0], Rb[0, 0])
         183 +        y = self.place_yaw - rel
         184 +        # block symmetric under pi rotation: pick closest to current gripper yaw
         185 +        if abs(_wrap(y - cur_yaw)) > np.pi / 2:
         186 +            y += np.pi
         187 +        return _wrap(y)
         188 +
  127    189      def get_action(self, s):
  128    190          for _ in range(20):
  129    191              a = self._step(s)
@@ -146,11 +208,14 @@ class GeneratedApproach:
  146    208          if kind == 'close':
  147    209              if grasping:
  148    210                  self.queue.pop(0)
         211 +                self.retries = 0
         212 +                self.grasp_fail = 0
  149    213                  return None
  150    214              self.retries += 1
  151        -            if self.retries > 3:
  152        -                # failed grasp: replan from scratch
         215 +            if self.retries > 2:
         216 +                # failed grasp: replan from scratch with another yaw
  153    217                  self.retries = 0
         218 +                self.grasp_fail += 1
  154    219                  self.queue = [('move_rel_up', SAFE_Z, None)]
  155    220                  return None
  156    221              a[10] = -1.0
@@ -176,7 +241,8 @@ class GeneratedApproach:
  176    241              if kind == 'move':
  177    242                  pos, yaw = cmd[1], cmd[2]
  178    243              elif kind == 'place_move':
  179        -                pos, yaw = self._tcp_target_for_block(s, cmd[1], cmd[2]), cmd[2]
         244 +                yaw = self._resolve_place_yaw(s, cmd[2], y0)
         245 +                pos = self._tcp_target_for_block(s, cmd[1], yaw)
  180    246              elif kind == 'move_rel_up':
  181    247                  pos = p0.copy(); pos[2] = max(pos[2], cmd[1])
  182    248                  yaw = y0 if cmd[2] is None else cmd[2]
```

</details>

<a id="C008"></a>
### C008 · fine small steps near objects (grasp descent, lift, place)

Commit `0611c4d0e4abc0a37eb8dfc37d893ad16da13255`; parents: 81d1da0b4ed93714e6c822279c1dcc60aaac8e08. Recorded author date: 2026-09-30T21:22:29+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0540](01_timeline.md#E0540): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_0611c4d_approach.py) · [Exact all-file diff](evidence/diffs/C008_0611c4d.diff)

[Previous saved controller snapshot](evidence/versions/C007_81d1da0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 415478d..06bcea6 100644
--- a/approach.py
+++ b/approach.py
@@ -7,6 +7,7 @@ MAXD = 0.19
    7      7  SAFE_Z = 0.27        # TCP transit height
    8      8  TABLE_Z = 0.075
    9      9  X_RANGE = (0.12, 0.44)
          10 +FINE = 0.004        # max cartesian advance per step near objects
   10     11  FINGER_OFF = 0.052   # finger centre offset along EE x (open)
   11     12  FINGER_HX = 0.011
   12     13  FINGER_HY = 0.013
@@ -137,12 +138,14 @@ class GeneratedApproach:
  137    138          place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
  138    139          return [
  139    140              ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
  140        -            ('move', np.array([p[0], p[1], gz]), yaw, True),
         141 +            ('move', np.array([p[0], p[1], gz + 0.02]), yaw, False),
         142 +            ('move', np.array([p[0], p[1], gz]), yaw, True, FINE),
  141    143              ('close', obj.name),
         144 +            ('move', np.array([p[0], p[1], gz + 0.03]), yaw, False, FINE),
  142    145              ('move', np.array([p[0], p[1], SAFE_Z]), yaw, False),
  143    146              ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
  144    147              ('place_move', place_center + np.array([0, 0, 0.02]), yaw, False),
  145        -            ('place_move', place_center, yaw, True),
         148 +            ('place_move', place_center, yaw, True, FINE),
  146    149              ('open', place_center, yaw),
  147    150              ('move_rel_up', SAFE_Z, yaw),
  148    151          ]
@@ -231,7 +234,7 @@ class GeneratedApproach:
  231    234                  self.retries = 0
  232    235                  c = cmd[1] - np.array([0, 0, 0.002])
  233    236                  self.queue[0] = ('open', c, cmd[2])
  234        -                self.queue.insert(0, ('place_move', c, cmd[2], True))
         237 +                self.queue.insert(0, ('place_move', c, cmd[2], True, FINE))
  235    238                  return None
  236    239              a[10] = 1.0
  237    240              return a
@@ -247,7 +250,10 @@ class GeneratedApproach:
  247    250                  pos = p0.copy(); pos[2] = max(pos[2], cmd[1])
  248    251                  yaw = y0 if cmd[2] is None else cmd[2]
  249    252              dy = _wrap(yaw - y0)
  250        -            n = int(np.ceil(max(np.linalg.norm(pos - p0) / 0.01, abs(dy) / 0.1, 1)))
         253 +            fine = cmd[4] if len(cmd) > 4 else None
         254 +            spacing = fine if fine else 0.01
         255 +            n = int(np.ceil(max(np.linalg.norm(pos - p0) / spacing, abs(dy) / 0.1, 1)))
         256 +            self.fine = fine is not None
  251    257              path = []
  252    258              qc = q.copy()
  253    259              for i in range(1, n + 1):
@@ -273,8 +279,11 @@ class GeneratedApproach:
  273    279              return None
  274    280          # furthest waypoint reachable in one step
  275    281          k = self.pidx
  276        -        while k + 1 < len(path) and np.max(np.abs(path[k + 1] - q)) <= MAXD:
  277        -            k += 1
         282 +        if self.fine:
         283 +            k = min(k + 1, len(path) - 1)
         284 +        else:
         285 +            while k + 1 < len(path) and np.max(np.abs(path[k + 1] - q)) <= MAXD:
         286 +                k += 1
  278    287          self.last_q = q.copy()
  279    288          self.pidx = k
  280    289          a[3:10] = np.clip(path[k] - q, -MAXD, MAXD)
diff --git a/esc.py b/esc.py
new file mode 100644
index 0000000..7887dfd
--- /dev/null
+++ b/esc.py
@@ -0,0 +1,28 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +import approach, kin
           4 +env=make_env(); obs,info=env.reset(seed=2)
           5 +ap=approach.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
           6 +r=obs.get_object_from_name('robot')
           7 +for t in range(40):
           8 +    if obs.get(r,'grasp_active')>0.5: break
           9 +    obs,*_=env.step(ap.get_action(obs))
          10 +print("grasped at", t)
          11 +F=approach.JF
          12 +def state():
          13 +    q=np.array([obs.get(r,f) for f in F]); base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          14 +    return q,base
          15 +for d in []:
          16 +    q,base=state(); M=kin.fk(base,q,0.12)
          17 +    qt,ok=kin.ik(base,q,M[:3,3]+np.array(d),M[:3,:3],tool=0.12)
          18 +    a=np.zeros(11,dtype=np.float32); a[3:10]=qt-q; a[10]=-1
          19 +    obs,*_=env.step(a); q2,_=state()
          20 +    print(d, "moved" if not np.allclose(q,q2) else "REJECTED")
          21 +print("---- 3mm steps")
          22 +o1=obs.get_object_from_name('obstruction1')
          23 +for i in range(30):
          24 +    q,base=state(); M=kin.fk(base,q,0.12)
          25 +    qt,ok=kin.ik(base,q,M[:3,3]+np.array([0,0,0.003]),M[:3,:3],tool=0.12)
          26 +    a=np.zeros(11,dtype=np.float32); a[3:10]=qt-q; a[10]=-1
          27 +    obs,*_=env.step(a); q2,_=state()
          28 +    print(i, round(M[2,3],3), "moved" if not np.allclose(q,q2) else "REJECTED", [round(obs.get(o1,f),3) for f in ['pose_x','pose_y','pose_z']], np.round(qt-q,3))
diff --git a/show.py b/show.py
new file mode 100644
index 0000000..e896f5c
--- /dev/null
+++ b/show.py
@@ -0,0 +1,7 @@
           1 +import sys
           2 +from env_client import make_env
           3 +env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
           4 +for n in sorted(obs.get_object_names()):
           5 +    if n=='robot': continue
           6 +    o=obs.get_object_from_name(n)
           7 +    print(n,[round(obs.get(o,f),4) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z','pose_qz']])
```

</details>

<a id="C009"></a>
### C009 · replan with held object, bad spot memory, narrower spot range

Commit `9816a620e4dcb548d88b227bb7966936106f2bae`; parents: 0611c4d0e4abc0a37eb8dfc37d893ad16da13255. Recorded author date: 2026-09-30T21:28:25+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0552](01_timeline.md#E0552): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_9816a62_approach.py) · [Exact all-file diff](evidence/diffs/C009_9816a62.diff)

[Previous saved controller snapshot](evidence/versions/C008_0611c4d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 06bcea6..e7901a6 100644
--- a/approach.py
+++ b/approach.py
@@ -6,12 +6,12 @@ TOOL = 0.12          # TCP offset along EE z (gripper centre)
    6      6  MAXD = 0.19
    7      7  SAFE_Z = 0.27        # TCP transit height
    8      8  TABLE_Z = 0.075
    9        -X_RANGE = (0.12, 0.44)
           9 +X_RANGE = (0.17, 0.43)
   10     10  FINE = 0.004        # max cartesian advance per step near objects
   11     11  FINGER_OFF = 0.052   # finger centre offset along EE x (open)
   12     12  FINGER_HX = 0.011
   13     13  FINGER_HY = 0.013
   14        -Y_RANGE = (-0.36, 0.36)
          14 +Y_RANGE = (-0.33, 0.33)
   15     15  
   16     16  
   17     17  def _pose(s, o):
@@ -44,6 +44,8 @@ class GeneratedApproach:
   44     44          self.retries = 0
   45     45          self.grasp_fail = 0
   46     46          self.place_yaw = None
          47 +        self.bad_spots = []
          48 +        self.cur_spot = None
   47     49  
   48     50      def _robot(self, s):
   49     51          r = s.get_object_from_name('robot')
@@ -70,6 +72,9 @@ class GeneratedApproach:
   70     72                      dy = abs(y - p[1]) - (h[1] + oh[1])
   71     73                      dmin = min(dmin, max(dx, dy))
   72     74                  score = min(dmin, 0.07) - 0.1 * np.hypot(x - cur[0], y - cur[1])
          75 +                for bx, by in self.bad_spots:
          76 +                    if np.hypot(x - bx, y - by) < 0.05:
          77 +                        score -= 1.0
   73     78                  if score > bestscore:
   74     79                      best, bestscore = (x, y), score
   75     80          return np.array(best)
@@ -150,6 +155,22 @@ class GeneratedApproach:
  150    155              ('move_rel_up', SAFE_Z, yaw),
  151    156          ]
  152    157  
         158 +    def _plan_place(self, s, obj, place_xy, support_top, place_yaw):
         159 +        _, q, base = self._robot(s)
         160 +        M = fk(base, q, TOOL)
         161 +        yaw = np.arctan2(M[1, 0], M[0, 0])
         162 +        self.place_yaw = place_yaw
         163 +        h = _he(s, obj)
         164 +        place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
         165 +        return [
         166 +            ('move_rel_up', SAFE_Z, yaw),
         167 +            ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
         168 +            ('place_move', place_center + np.array([0, 0, 0.02]), yaw, False),
         169 +            ('place_move', place_center, yaw, True, FINE),
         170 +            ('open', place_center, yaw),
         171 +            ('move_rel_up', SAFE_Z, yaw),
         172 +        ]
         173 +
  153    174      def _plan(self, s):
  154    175          reg = s.get_object_from_name('target_region')
  155    176          tb = s.get_object_from_name('target_block')
@@ -157,12 +178,24 @@ class GeneratedApproach:
  157    178          cur = fk(base, q, TOOL)[:3, 3]
  158    179          cubes = [s.get_object_from_name(n) for n in sorted(s.get_object_names())
  159    180                   if n.startswith('obstruction')]
         181 +        held = [c for c in cubes + [tb] if s.get(c, 'grasp_active') > 0.5]
         182 +        if held:
         183 +            o = held[0]
         184 +            others = [c for c in cubes if c.name != o.name] + [reg, tb]
         185 +            others = [c for c in others if c.name != o.name]
         186 +            if o.name == 'target_block':
         187 +                rp = _pose(s, reg)
         188 +                return self._plan_place(s, o, rp[:2], rp[2] + _he(s, reg)[2], self._obj_yaw(s, reg))
         189 +            spot = self._free_spot(s, o, others, cur)
         190 +            self.cur_spot = spot
         191 +            return self._plan_place(s, o, spot, TABLE_Z, None)
  160    192          blocking = [o for o in cubes if self._overlaps(s, o, reg)]
  161    193          if blocking:
  162    194              # remove the tallest (top-most) first
  163    195              o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2])
  164    196              others = [c for c in cubes if c.name != o.name] + [reg, tb]
  165    197              spot = self._free_spot(s, o, others, cur)
         198 +            self.cur_spot = spot
  166    199              return self._plan_pick_place(s, o, spot, TABLE_Z, others)
  167    200          rp = _pose(s, reg)
  168    201          others = cubes
@@ -275,6 +308,8 @@ class GeneratedApproach:
  275    308              self.queue.pop(0)
  276    309              self.qtarget = None
  277    310              if not allow:
         311 +                if kind == 'place_move' and self.cur_spot is not None and self.place_yaw is None:
         312 +                    self.bad_spots.append(tuple(self.cur_spot))
  278    313                  self.queue = [('move_rel_up', SAFE_Z + 0.03, None, True)]  # retreat, then replan
  279    314              return None
  280    315          # furthest waypoint reachable in one step
diff --git a/trace2.py b/trace2.py
new file mode 100644
index 0000000..a61676a
--- /dev/null
+++ b/trace2.py
@@ -0,0 +1,22 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach, kin
           4 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 300
           5 +env=make_env(); obs,info=env.reset(seed=seed)
           6 +ap=approach.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
           7 +last=None; rej=0
           8 +for t in range(N):
           9 +    a=ap.get_action(obs)
          10 +    r=obs.get_object_from_name('robot')
          11 +    q=np.array([obs.get(r,f) for f in approach.JF]); base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
          12 +    tcp=kin.fk(base,q,0.12)[:3,3]
          13 +    cmd=ap.queue[0] if ap.queue else None
          14 +    key=(cmd[0], str(cmd[1])) if cmd else None
          15 +    if key!=last:
          16 +        print(t, cmd[0], np.round(cmd[1],3) if not isinstance(cmd[1],(str,float)) else cmd[1], "tcp",np.round(tcp,3),"g",obs.get(r,'grasp_active'))
          17 +        last=key
          18 +    obs2,rew,term,trunc,info=env.step(a)
          19 +    q2=np.array([obs2.get(r,f) for f in approach.JF])
          20 +    if np.allclose(q,q2) and np.any(a[3:10]!=0): print("   rejected at",t)
          21 +    obs=obs2
          22 +    if term: print("TERM",t); break
```

</details>

<a id="C010"></a>
### C010 · choose most accessible obstruction first; failure counts

Commit `8e6d34373c8a87c92f8299e230ce5dfa362faf04`; parents: 9816a620e4dcb548d88b227bb7966936106f2bae. Recorded author date: 2026-09-30T21:40:46+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0612](01_timeline.md#E0612): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_8e6d343_approach.py) · [Exact all-file diff](evidence/diffs/C010_8e6d343.diff)

[Previous saved controller snapshot](evidence/versions/C009_9816a62_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e7901a6..b47cc0e 100644
--- a/approach.py
+++ b/approach.py
@@ -45,6 +45,8 @@ class GeneratedApproach:
   45     45          self.grasp_fail = 0
   46     46          self.place_yaw = None
   47     47          self.bad_spots = []
          48 +        self.fail_count = {}
          49 +        self.last_target = None
   48     50          self.cur_spot = None
   49     51  
   50     52      def _robot(self, s):
@@ -191,8 +193,23 @@ class GeneratedApproach:
  191    193              return self._plan_place(s, o, spot, TABLE_Z, None)
  192    194          blocking = [o for o in cubes if self._overlaps(s, o, reg)]
  193    195          if blocking:
  194        -            # remove the tallest (top-most) first
  195        -            o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2])
         196 +            # remove the most accessible first (best finger clearance), penalise failures
         197 +            def access(c):
         198 +                oth = [x for x in cubes if x.name != c.name] + [tb]
         199 +                oy = self._obj_yaw(s, c)
         200 +                h = _he(s, c)
         201 +                best = -1e9
         202 +                for k in range(4):
         203 +                    yaw = oy + k * np.pi / 2
         204 +                    span = h[0] if k % 2 == 0 else h[1]
         205 +                    if span > 0.041:
         206 +                        continue
         207 +                    best = max(best, self._finger_clearance(s, c, yaw, oth))
         208 +                return min(best, 0.03) - 0.05 * self.fail_count.get(c.name, 0)
         209 +            o = max(blocking, key=access)
         210 +            if o.name != self.last_target:
         211 +                self.grasp_fail = 0
         212 +            self.last_target = o.name
  196    213              others = [c for c in cubes if c.name != o.name] + [reg, tb]
  197    214              spot = self._free_spot(s, o, others, cur)
  198    215              self.cur_spot = spot
@@ -252,6 +269,7 @@ class GeneratedApproach:
  252    269                  # failed grasp: replan from scratch with another yaw
  253    270                  self.retries = 0
  254    271                  self.grasp_fail += 1
         272 +                self.fail_count[cmd[1]] = self.fail_count.get(cmd[1], 0) + 1
  255    273                  self.queue = [('move_rel_up', SAFE_Z, None)]
  256    274                  return None
  257    275              a[10] = -1.0
diff --git a/show2.py b/show2.py
new file mode 100644
index 0000000..e6cd986
--- /dev/null
+++ b/show2.py
@@ -0,0 +1,7 @@
           1 +import sys
           2 +from env_client import make_env
           3 +env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]), options={"object_count":int(sys.argv[2])})
           4 +for n in sorted(obs.get_object_names()):
           5 +    if n=='robot': continue
           6 +    o=obs.get_object_from_name(n)
           7 +    print(n,[round(obs.get(o,f),4) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z','pose_qz']])
diff --git a/test_count.py b/test_count.py
new file mode 100644
index 0000000..bc2e17e
--- /dev/null
+++ b/test_count.py
@@ -0,0 +1,25 @@
           1 +import sys, time, numpy as np
           2 +from concurrent.futures import ProcessPoolExecutor
           3 +def run(args):
           4 +    seed, cnt = args
           5 +    from env_client import make_env
           6 +    import approach
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed, options={"object_count": cnt})
           9 +    ap = approach.GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    ap.reset(obs, info)
          11 +    t0=time.time(); tc=0; term=False
          12 +    n=len([x for x in obs.get_object_names() if x.startswith('obstruction')])
          13 +    for steps in range(1, env.max_steps+1):
          14 +        t1=time.time(); a = ap.get_action(obs); tc+=time.time()-t1
          15 +        obs, rew, term, trunc, info = env.step(a)
          16 +        if term or trunc: break
          17 +    env.close()
          18 +    return seed, n, bool(term), steps, round(tc,1)
          19 +if __name__ == "__main__":
          20 +    cnt=int(sys.argv[1]); a=int(sys.argv[2]); b=int(sys.argv[3])
          21 +    with ProcessPoolExecutor(8) as ex:
          22 +        res=list(ex.map(run, [(s,cnt) for s in range(a,b)]))
          23 +    for r in res:
          24 +        if not r[2]: print(r)
          25 +    print("count",cnt,"success", sum(r[2] for r in res), "/", len(res), "mean steps", np.mean([r[3] for r in res]), "max compute", max(r[4] for r in res))
diff --git a/trace2.py b/trace2.py
index a61676a..d5762c9 100644
--- a/trace2.py
+++ b/trace2.py
@@ -1,8 +1,8 @@
    1      1  import sys, numpy as np
    2      2  from env_client import make_env
    3      3  import approach, kin
    4        -seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 300
    5        -env=make_env(); obs,info=env.reset(seed=seed)
           4 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 300; CNT=int(sys.argv[3]) if len(sys.argv)>3 else None
           5 +env=make_env(); obs,info=env.reset(seed=seed, options=({"object_count":CNT} if CNT else None))
    6      6  ap=approach.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
    7      7  last=None; rej=0
    8      8  for t in range(N):
@@ -13,7 +13,7 @@ for t in range(N):
   13     13      cmd=ap.queue[0] if ap.queue else None
   14     14      key=(cmd[0], str(cmd[1])) if cmd else None
   15     15      if key!=last:
   16        -        print(t, cmd[0], np.round(cmd[1],3) if not isinstance(cmd[1],(str,float)) else cmd[1], "tcp",np.round(tcp,3),"g",obs.get(r,'grasp_active'))
          16 +        print(t, cmd[0], round(cmd[2],2) if len(cmd)>2 and isinstance(cmd[2],float) else "", round(obs.get(r,"finger_state"),2), np.round(cmd[1],3) if not isinstance(cmd[1],(str,float)) else cmd[1], "tcp",np.round(tcp,3),"g",obs.get(r,'grasp_active'))
   17     17          last=key
   18     18      obs2,rew,term,trunc,info=env.step(a)
   19     19      q2=np.array([obs2.get(r,f) for f in approach.JF])
```

</details>

<a id="C011"></a>
### C011 · prefer axis-aligned grasps strongly

Commit `32060165ae2c2824b3a231de977b40a0238c7176`; parents: 8e6d34373c8a87c92f8299e230ce5dfa362faf04. Recorded author date: 2026-09-30T21:41:57+02:00.

File roles (automatic): policy.

- [E0646](01_timeline.md#E0646): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_3206016_approach.py) · [Exact all-file diff](evidence/diffs/C011_3206016.diff)

[Previous saved controller snapshot](evidence/versions/C010_8e6d343_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b47cc0e..2e997d2 100644
--- a/approach.py
+++ b/approach.py
@@ -125,8 +125,11 @@ class GeneratedApproach:
  125    125              if span > 0.041:
  126    126                  continue
  127    127              clr = self._finger_clearance(s, obj, yaw, others)
         128 +            aligned = abs(np.sin(2 * rel)) < 1e-6
  128    129              score = min(clr, 0.02) - 0.002 * abs(_wrap(yaw - cy)) - 0.01 * span \
  129        -                - (0.0 if abs(np.sin(2 * rel)) < 1e-6 else 0.005)
         130 +                - (0.0 if aligned else 0.03)
         131 +            if not aligned and clr < 0.004:
         132 +                continue
  130    133              cands.append((score, _wrap(yaw)))
  131    134          if not cands:
  132    135              yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
```

</details>

<a id="C012"></a>
### C012 · grasp dz 0.04

Commit `f7501d3205e66cc1de0f0f918f554118ae1affa6`; parents: 32060165ae2c2824b3a231de977b40a0238c7176. Recorded author date: 2026-09-30T21:53:10+02:00.

File roles (automatic): policy.

- [E0674](01_timeline.md#E0674): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_f7501d3_approach.py) · [Exact all-file diff](evidence/diffs/C012_f7501d3.diff)

[Previous saved controller snapshot](evidence/versions/C011_3206016_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2e997d2..2e3486b 100644
--- a/approach.py
+++ b/approach.py
@@ -127,7 +127,7 @@ class GeneratedApproach:
  127    127              clr = self._finger_clearance(s, obj, yaw, others)
  128    128              aligned = abs(np.sin(2 * rel)) < 1e-6
  129    129              score = min(clr, 0.02) - 0.002 * abs(_wrap(yaw - cy)) - 0.01 * span \
  130        -                - (0.0 if aligned else 0.03)
         130 +                - (0.0 if aligned else 0.01)
  131    131              if not aligned and clr < 0.004:
  132    132                  continue
  133    133              cands.append((score, _wrap(yaw)))
@@ -144,7 +144,7 @@ class GeneratedApproach:
  144    144          h = _he(s, obj)
  145    145          yaw = self._grasp_yaw(s, obj, q, base, others, place_yaw is not None)
  146    146          self.place_yaw = place_yaw
  147        -        gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
         147 +        gz = p[2] + 0.04  # TCP height for grasp: object centre 4cm below TCP is most reliable
  148    148          place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
  149    149          return [
  150    150              ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
```

</details>

<a id="C013"></a>
### C013 · revert to 60/60 version (access/aligned changes didn't help)

Commit `0989e5bd2d0d007150dfe4253a912565632c16b9`; parents: f7501d3205e66cc1de0f0f918f554118ae1affa6. Recorded author date: 2026-09-30T22:03:00+02:00.

File roles (automatic): policy.

- [E0687](01_timeline.md#E0687): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_0989e5b_approach.py) · [Exact all-file diff](evidence/diffs/C013_0989e5b.diff)

[Previous saved controller snapshot](evidence/versions/C012_f7501d3_approach.py) — not the first-ever controller.

Identical complete controller bytes to earlier [C009](#C009). Other files may differ.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2e3486b..e7901a6 100644
--- a/approach.py
+++ b/approach.py
@@ -45,8 +45,6 @@ class GeneratedApproach:
   45     45          self.grasp_fail = 0
   46     46          self.place_yaw = None
   47     47          self.bad_spots = []
   48        -        self.fail_count = {}
   49        -        self.last_target = None
   50     48          self.cur_spot = None
   51     49  
   52     50      def _robot(self, s):
@@ -125,11 +123,8 @@ class GeneratedApproach:
  125    123              if span > 0.041:
  126    124                  continue
  127    125              clr = self._finger_clearance(s, obj, yaw, others)
  128        -            aligned = abs(np.sin(2 * rel)) < 1e-6
  129    126              score = min(clr, 0.02) - 0.002 * abs(_wrap(yaw - cy)) - 0.01 * span \
  130        -                - (0.0 if aligned else 0.01)
  131        -            if not aligned and clr < 0.004:
  132        -                continue
         127 +                - (0.0 if abs(np.sin(2 * rel)) < 1e-6 else 0.005)
  133    128              cands.append((score, _wrap(yaw)))
  134    129          if not cands:
  135    130              yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
@@ -144,7 +139,7 @@ class GeneratedApproach:
  144    139          h = _he(s, obj)
  145    140          yaw = self._grasp_yaw(s, obj, q, base, others, place_yaw is not None)
  146    141          self.place_yaw = place_yaw
  147        -        gz = p[2] + 0.04  # TCP height for grasp: object centre 4cm below TCP is most reliable
         142 +        gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
  148    143          place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
  149    144          return [
  150    145              ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
@@ -196,23 +191,8 @@ class GeneratedApproach:
  196    191              return self._plan_place(s, o, spot, TABLE_Z, None)
  197    192          blocking = [o for o in cubes if self._overlaps(s, o, reg)]
  198    193          if blocking:
  199        -            # remove the most accessible first (best finger clearance), penalise failures
  200        -            def access(c):
  201        -                oth = [x for x in cubes if x.name != c.name] + [tb]
  202        -                oy = self._obj_yaw(s, c)
  203        -                h = _he(s, c)
  204        -                best = -1e9
  205        -                for k in range(4):
  206        -                    yaw = oy + k * np.pi / 2
  207        -                    span = h[0] if k % 2 == 0 else h[1]
  208        -                    if span > 0.041:
  209        -                        continue
  210        -                    best = max(best, self._finger_clearance(s, c, yaw, oth))
  211        -                return min(best, 0.03) - 0.05 * self.fail_count.get(c.name, 0)
  212        -            o = max(blocking, key=access)
  213        -            if o.name != self.last_target:
  214        -                self.grasp_fail = 0
  215        -            self.last_target = o.name
         194 +            # remove the tallest (top-most) first
         195 +            o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2])
  216    196              others = [c for c in cubes if c.name != o.name] + [reg, tb]
  217    197              spot = self._free_spot(s, o, others, cur)
  218    198              self.cur_spot = spot
@@ -272,7 +252,6 @@ class GeneratedApproach:
  272    252                  # failed grasp: replan from scratch with another yaw
  273    253                  self.retries = 0
  274    254                  self.grasp_fail += 1
  275        -                self.fail_count[cmd[1]] = self.fail_count.get(cmd[1], 0) + 1
  276    255                  self.queue = [('move_rel_up', SAFE_Z, None)]
  277    256                  return None
  278    257              a[10] = -1.0
```

</details>

<a id="C014"></a>
### C014 · in-place grasp depth retries

Commit `50044fb994e62f2ded74d19e09ad7547dfa3a0c6`; parents: 0989e5bd2d0d007150dfe4253a912565632c16b9. Recorded author date: 2026-09-30T22:03:28+02:00.

File roles (automatic): policy.

- [E0707](01_timeline.md#E0707): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_50044fb_approach.py) · [Exact all-file diff](evidence/diffs/C014_50044fb.diff)

[Previous saved controller snapshot](evidence/versions/C013_0989e5b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e7901a6..d2e18ad 100644
--- a/approach.py
+++ b/approach.py
@@ -145,7 +145,7 @@ class GeneratedApproach:
  145    145              ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
  146    146              ('move', np.array([p[0], p[1], gz + 0.02]), yaw, False),
  147    147              ('move', np.array([p[0], p[1], gz]), yaw, True, FINE),
  148        -            ('close', obj.name),
         148 +            ('close', obj.name, p.copy(), yaw, [0.045, 0.03, 0.05, 0.025]),
  149    149              ('move', np.array([p[0], p[1], gz + 0.03]), yaw, False, FINE),
  150    150              ('move', np.array([p[0], p[1], SAFE_Z]), yaw, False),
  151    151              ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
@@ -248,6 +248,16 @@ class GeneratedApproach:
  248    248                  self.grasp_fail = 0
  249    249                  return None
  250    250              self.retries += 1
         251 +            if self.retries > 2 and len(cmd) > 4 and cmd[4]:
         252 +                # failed grasp: open, try another depth in place
         253 +                self.retries = 0
         254 +                dz = cmd[4][0]
         255 +                self.queue[0] = cmd[:4] + (cmd[4][1:],)
         256 +                pc = cmd[2]
         257 +                self.queue.insert(0, ('move', np.array([pc[0], pc[1], pc[2] + dz]), cmd[3], True, FINE))
         258 +                self.queue.insert(0, ('move', np.array([pc[0], pc[1], pc[2] + max(dz, 0.035) + 0.01]), cmd[3], True, FINE))
         259 +                self.queue.insert(0, ('ungrip',))
         260 +                return None
  251    261              if self.retries > 2:
  252    262                  # failed grasp: replan from scratch with another yaw
  253    263                  self.retries = 0
@@ -256,6 +266,10 @@ class GeneratedApproach:
  256    266                  return None
  257    267              a[10] = -1.0
  258    268              return a
         269 +        if kind == 'ungrip':
         270 +            self.queue.pop(0)
         271 +            a[10] = 1.0
         272 +            return a
  259    273          if kind == 'open':
  260    274              if not grasping:
  261    275                  self.queue.pop(0)
```

</details>

<a id="C015"></a>
### C015 · retry rejected coarse moves with fine steps

Commit `71151aeac4a2e60b76302a8809ee11a780782a0e`; parents: 50044fb994e62f2ded74d19e09ad7547dfa3a0c6. Recorded author date: 2026-09-30T22:29:18+02:00.

File roles (automatic): policy.

- [E0778](01_timeline.md#E0778): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_71151ae_approach.py) · [Exact all-file diff](evidence/diffs/C015_71151ae.diff)

[Previous saved controller snapshot](evidence/versions/C014_50044fb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d2e18ad..d444777 100644
--- a/approach.py
+++ b/approach.py
@@ -319,8 +319,12 @@ class GeneratedApproach:
  319    319          if self.last_q is not None and np.allclose(self.last_q, q, atol=1e-7):
  320    320              # previous action rejected (collision)
  321    321              allow = len(cmd) > 3 and cmd[3]
  322        -            self.queue.pop(0)
  323    322              self.qtarget = None
         323 +            if not self.fine and kind in ('move', 'place_move', 'move_rel_up'):
         324 +                # retry same motion with small interpolation steps
         325 +                self.queue[0] = tuple(cmd[:3]) + (allow, FINE)
         326 +                return None
         327 +            self.queue.pop(0)
  324    328              if not allow:
  325    329                  if kind == 'place_move' and self.cur_spot is not None and self.place_yaw is None:
  326    330                      self.bad_spots.append(tuple(self.cur_spot))
```

</details>

<a id="C016"></a>
### C016 · count approach rejections as grasp failures, cycle yaw candidates, deprioritize failing objects

Commit `c5d29bf85619c55e3f2bff7f08f8ca1fab24cdf8`; parents: 71151aeac4a2e60b76302a8809ee11a780782a0e. Recorded author date: 2026-09-30T22:34:27+02:00.

File roles (automatic): policy.

- [E0813](01_timeline.md#E0813): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_c5d29bf_approach.py) · [Exact all-file diff](evidence/diffs/C016_c5d29bf.diff)

[Previous saved controller snapshot](evidence/versions/C015_71151ae_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d444777..b568c06 100644
--- a/approach.py
+++ b/approach.py
@@ -43,6 +43,8 @@ class GeneratedApproach:
   43     43          self.last_q = None
   44     44          self.retries = 0
   45     45          self.grasp_fail = 0
          46 +        self.fail_count = {}
          47 +        self.cur_obj = None
   46     48          self.place_yaw = None
   47     49          self.bad_spots = []
   48     50          self.cur_spot = None
@@ -130,7 +132,7 @@ class GeneratedApproach:
  130    132              yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
  131    133              return _wrap(yaw)
  132    134          cands.sort(reverse=True)
  133        -        idx = min(self.grasp_fail, len(cands) - 1)
         135 +        idx = self.grasp_fail % len(cands)
  134    136          return cands[idx][1]
  135    137  
  136    138      def _plan_pick_place(self, s, obj, place_xy, support_top, others, place_yaw=None):
@@ -139,6 +141,7 @@ class GeneratedApproach:
  139    141          h = _he(s, obj)
  140    142          yaw = self._grasp_yaw(s, obj, q, base, others, place_yaw is not None)
  141    143          self.place_yaw = place_yaw
         144 +        self.cur_obj = obj.name
  142    145          gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
  143    146          place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
  144    147          return [
@@ -192,7 +195,8 @@ class GeneratedApproach:
  192    195          blocking = [o for o in cubes if self._overlaps(s, o, reg)]
  193    196          if blocking:
  194    197              # remove the tallest (top-most) first
  195        -            o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2])
         198 +            o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2]
         199 +                    - 0.05 * self.fail_count.get(c.name, 0))
  196    200              others = [c for c in cubes if c.name != o.name] + [reg, tb]
  197    201              spot = self._free_spot(s, o, others, cur)
  198    202              self.cur_spot = spot
@@ -262,6 +266,8 @@ class GeneratedApproach:
  262    266                  # failed grasp: replan from scratch with another yaw
  263    267                  self.retries = 0
  264    268                  self.grasp_fail += 1
         269 +                if self.cur_obj is not None:
         270 +                    self.fail_count[self.cur_obj] = self.fail_count.get(self.cur_obj, 0) + 1
  265    271                  self.queue = [('move_rel_up', SAFE_Z, None)]
  266    272                  return None
  267    273              a[10] = -1.0
@@ -326,6 +332,9 @@ class GeneratedApproach:
  326    332                  return None
  327    333              self.queue.pop(0)
  328    334              if not allow:
         335 +                if not grasping and self.cur_obj is not None:
         336 +                    self.grasp_fail += 1
         337 +                    self.fail_count[self.cur_obj] = self.fail_count.get(self.cur_obj, 0) + 1
  329    338                  if kind == 'place_move' and self.cur_spot is not None and self.place_yaw is None:
  330    339                      self.bad_spots.append(tuple(self.cur_spot))
  331    340                  self.queue = [('move_rel_up', SAFE_Z + 0.03, None, True)]  # retreat, then replan
```

</details>

<a id="C017"></a>
### C017 · target grasp yaw considers finger clearance at the place pose

Commit `1731ff2620aa4b40eefd2481d716414a77afeeb2`; parents: c5d29bf85619c55e3f2bff7f08f8ca1fab24cdf8. Recorded author date: 2026-09-30T22:51:59+02:00.

File roles (automatic): policy.

- [E0873](01_timeline.md#E0873): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_1731ff2_approach.py) · [Exact all-file diff](evidence/diffs/C017_1731ff2.diff)

[Previous saved controller snapshot](evidence/versions/C016_c5d29bf_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b568c06..0fcf890 100644
--- a/approach.py
+++ b/approach.py
@@ -85,9 +85,9 @@ class GeneratedApproach:
   85     85          R = _quat_R(*[s.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')])
   86     86          return np.arctan2(R[1, 0], R[0, 0])
   87     87  
   88        -    def _finger_clearance(self, s, obj, yaw, others):
          88 +    def _finger_clearance(self, s, obj, yaw, others, center=None):
   89     89          """Min clearance between finger boxes (at obj, given yaw) and other objects' footprints."""
   90        -        p = _pose(s, obj)
          90 +        p = _pose(s, obj) if center is None else center
   91     91          c, sn = np.cos(yaw), np.sin(yaw)
   92     92          ax = np.array([c, sn]); ay = np.array([-sn, c])
   93     93          best = 1e9
@@ -111,7 +111,7 @@ class GeneratedApproach:
  111    111                  best = min(best, d)
  112    112          return best
  113    113  
  114        -    def _grasp_yaw(self, s, obj, q, base, others, aligned_only):
         114 +    def _grasp_yaw(self, s, obj, q, base, others, aligned_only, place=None):
  115    115          h = _he(s, obj)
  116    116          oyaw = self._obj_yaw(s, obj)
  117    117          M = fk(base, q, TOOL)
@@ -125,6 +125,9 @@ class GeneratedApproach:
  125    125              if span > 0.041:
  126    126                  continue
  127    127              clr = self._finger_clearance(s, obj, yaw, others)
         128 +            if place is not None:
         129 +                pc, pyaw = place
         130 +                clr = min(clr, self._finger_clearance(s, obj, pyaw + rel, others, center=pc))
  128    131              score = min(clr, 0.02) - 0.002 * abs(_wrap(yaw - cy)) - 0.01 * span \
  129    132                  - (0.0 if abs(np.sin(2 * rel)) < 1e-6 else 0.005)
  130    133              cands.append((score, _wrap(yaw)))
@@ -139,11 +142,12 @@ class GeneratedApproach:
  139    142          _, q, base = self._robot(s)
  140    143          p = _pose(s, obj)
  141    144          h = _he(s, obj)
  142        -        yaw = self._grasp_yaw(s, obj, q, base, others, place_yaw is not None)
         145 +        place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
         146 +        yaw = self._grasp_yaw(s, obj, q, base, others, place_yaw is not None,
         147 +                              None if place_yaw is None else (place_center, place_yaw))
  143    148          self.place_yaw = place_yaw
  144    149          self.cur_obj = obj.name
  145    150          gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
  146        -        place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
  147    151          return [
  148    152              ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
  149    153              ('move', np.array([p[0], p[1], gz + 0.02]), yaw, False),
```

</details>

<a id="C018"></a>
### C018 · release-failure fallback: re-place elsewhere, clear near-region obstructions

Commit `99399cddd2a2cfd765934e93e105a7e01d5ae223`; parents: 1731ff2620aa4b40eefd2481d716414a77afeeb2. Recorded author date: 2026-09-30T22:52:55+02:00.

File roles (automatic): policy.

- [E0883](01_timeline.md#E0883): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_99399cd_approach.py) · [Exact all-file diff](evidence/diffs/C018_99399cd.diff)

[Previous saved controller snapshot](evidence/versions/C017_1731ff2_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0fcf890..36fb54f 100644
--- a/approach.py
+++ b/approach.py
@@ -44,6 +44,8 @@ class GeneratedApproach:
   44     44          self.retries = 0
   45     45          self.grasp_fail = 0
   46     46          self.fail_count = {}
          47 +        self.open_fail = 0
          48 +        self.place_fail = 0
   47     49          self.cur_obj = None
   48     50          self.place_yaw = None
   49     51          self.bad_spots = []
@@ -190,13 +192,15 @@ class GeneratedApproach:
  190    192              o = held[0]
  191    193              others = [c for c in cubes if c.name != o.name] + [reg, tb]
  192    194              others = [c for c in others if c.name != o.name]
  193        -            if o.name == 'target_block':
         195 +            near = [c for c in cubes if c.name != o.name and self._overlaps(s, c, reg, 0.06)]
         196 +            if o.name == 'target_block' and not (self.place_fail > 0 and near):
  194    197                  rp = _pose(s, reg)
  195    198                  return self._plan_place(s, o, rp[:2], rp[2] + _he(s, reg)[2], self._obj_yaw(s, reg))
  196    199              spot = self._free_spot(s, o, others, cur)
  197    200              self.cur_spot = spot
  198    201              return self._plan_place(s, o, spot, TABLE_Z, None)
  199        -        blocking = [o for o in cubes if self._overlaps(s, o, reg)]
         202 +        blocking = [o for o in cubes
         203 +                    if self._overlaps(s, o, reg, 0.004 if self.place_fail == 0 else 0.06)]
  200    204          if blocking:
  201    205              # remove the tallest (top-most) first
  202    206              o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2]
@@ -284,8 +288,21 @@ class GeneratedApproach:
  284    288              if not grasping:
  285    289                  self.queue.pop(0)
  286    290                  self.retries = 0
         291 +                self.open_fail = 0
  287    292                  return None
  288    293              self.retries += 1
         294 +            if self.retries > 1:
         295 +                self.open_fail += 1
         296 +            if self.open_fail > 8:
         297 +                # cannot release here: lift and replan
         298 +                self.open_fail = 0
         299 +                self.retries = 0
         300 +                if self.place_yaw is not None:
         301 +                    self.place_fail += 1
         302 +                elif self.cur_spot is not None:
         303 +                    self.bad_spots.append(tuple(self.cur_spot))
         304 +                self.queue = [('move_rel_up', SAFE_Z, None, True)]
         305 +                return None
  289    306              if self.retries > 1:
  290    307                  # lower a bit and try again
  291    308                  self.retries = 0
```

</details>

<a id="C019"></a>
### C019 · finger clearance: only objects reaching fingertip height matter

Commit `9c018b1fc83045d1cc3b3a179293c071493e10f7`; parents: 99399cddd2a2cfd765934e93e105a7e01d5ae223. Recorded author date: 2026-09-30T22:58:20+02:00.

File roles (automatic): policy.

- [E0918](01_timeline.md#E0918): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_9c018b1_approach.py) · [Exact all-file diff](evidence/diffs/C019_9c018b1.diff)

[Previous saved controller snapshot](evidence/versions/C018_99399cd_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 36fb54f..28903fd 100644
--- a/approach.py
+++ b/approach.py
@@ -95,7 +95,7 @@ class GeneratedApproach:
   95     95          best = 1e9
   96     96          for o in others:
   97     97              op, oh = _pose(s, o), _he(s, o)
   98        -            if op[2] + oh[2] < p[2] - 0.035:   # below fingertips
          98 +            if op[2] + oh[2] < p[2] - 0.01:   # below fingertips (tips ~ centre+0.005 at grasp)
   99     99                  continue
  100    100              oyaw = self._obj_yaw(s, o)
  101    101              oc, os_ = np.cos(oyaw), np.sin(oyaw)
```

</details>

<a id="C020"></a>
### C020 · prefer blocking obstructions with a clear aligned grasp

Commit `104631d52b516b8be2d2d5cd3635bedcb050c2d8`; parents: 9c018b1fc83045d1cc3b3a179293c071493e10f7. Recorded author date: 2026-09-30T23:01:36+02:00.

File roles (automatic): policy.

- [E0926](01_timeline.md#E0926): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_104631d_approach.py) · [Exact all-file diff](evidence/diffs/C020_104631d.diff)

[Previous saved controller snapshot](evidence/versions/C019_9c018b1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 28903fd..022df89 100644
--- a/approach.py
+++ b/approach.py
@@ -203,7 +203,16 @@ class GeneratedApproach:
  203    203                      if self._overlaps(s, o, reg, 0.004 if self.place_fail == 0 else 0.06)]
  204    204          if blocking:
  205    205              # remove the tallest (top-most) first
  206        -            o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2]
         206 +            def acc(c):
         207 +                oth = [d for d in cubes if d.name != c.name] + [tb]
         208 +                h = _he(s, c); oy = self._obj_yaw(s, c); best = -1.0
         209 +                for k in range(4):
         210 +                    rel = k * np.pi / 2
         211 +                    if abs(np.cos(rel)) * h[0] + abs(np.sin(rel)) * h[1] > 0.041:
         212 +                        continue
         213 +                    best = max(best, self._finger_clearance(s, c, oy + rel, oth))
         214 +                return best
         215 +            o = max(blocking, key=lambda c: (acc(c) > 0.002) + _pose(s, c)[2] + _he(s, c)[2]
  207    216                      - 0.05 * self.fail_count.get(c.name, 0))
  208    217              others = [c for c in cubes if c.name != o.name] + [reg, tb]
  209    218              spot = self._free_spot(s, o, others, cur)
```

</details>

<a id="C021"></a>
### C021 · restore fingertip clearance threshold

Commit `c6d49bbcd14d7d3f03a760459ed66ff0e5847fd0`; parents: 104631d52b516b8be2d2d5cd3635bedcb050c2d8. Recorded author date: 2026-09-30T23:03:09+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0948](01_timeline.md#E0948): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_c6d49bb_approach.py) · [Exact all-file diff](evidence/diffs/C021_c6d49bb.diff)

[Previous saved controller snapshot](evidence/versions/C020_104631d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 022df89..ef9df33 100644
--- a/approach.py
+++ b/approach.py
@@ -95,7 +95,7 @@ class GeneratedApproach:
   95     95          best = 1e9
   96     96          for o in others:
   97     97              op, oh = _pose(s, o), _he(s, o)
   98        -            if op[2] + oh[2] < p[2] - 0.01:   # below fingertips (tips ~ centre+0.005 at grasp)
          98 +            if op[2] + oh[2] < p[2] - 0.035:   # below fingertips
   99     99                  continue
  100    100              oyaw = self._obj_yaw(s, o)
  101    101              oc, os_ = np.cos(oyaw), np.sin(oyaw)
diff --git a/res1.txt b/res1.txt
new file mode 100644
index 0000000..8706006
--- /dev/null
+++ b/res1.txt
@@ -0,0 +1,7 @@
           1 +(15, 5, False, 1000, 13.5)
           2 +count 5 success 15 / 16 mean steps 337.75 max compute 13.5
           3 +(39, 2, True, 123, 11.0)
           4 +success 40 / 40 mean steps 83.5
           5 +(0, 6, False, 1000, 122.1)
           6 +(4, 6, False, 1000, 10.8)
           7 +count 6 success 6 / 8 mean steps 526.0 max compute 122.1
diff --git a/res2.txt b/res2.txt
new file mode 100644
index 0000000..a3d6c02
--- /dev/null
+++ b/res2.txt
@@ -0,0 +1,4 @@
           1 +(0, 6, False, 1000, 129.2)
           2 +(4, 6, False, 1000, 10.3)
           3 +count 6 success 6 / 8 mean steps 526.0 max compute 129.2
           4 +success 40 / 40 mean steps 83.5
diff --git a/res3.txt b/res3.txt
new file mode 100644
index 0000000..2c3ab26
--- /dev/null
+++ b/res3.txt
@@ -0,0 +1,5 @@
           1 +(4, 6, False, 1000, 10.7)
           2 +(11, 6, False, 1000, 9.0)
           3 +count 6 success 14 / 16 mean steps 410.8125 max compute 10.7
           4 +(11, 5, False, 1000, 8.4)
           5 +count 5 success 15 / 16 mean steps 353.625 max compute 8.4
diff --git a/show3.py b/show3.py
new file mode 100644
index 0000000..4b9a192
--- /dev/null
+++ b/show3.py
@@ -0,0 +1,13 @@
           1 +import sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]), options={"object_count":int(sys.argv[2])})
           5 +ap=GeneratedApproach(env.action_space, env.observation_space, None); ap.reset(obs,info)
           6 +for t in range(int(sys.argv[3])):
           7 +    obs,r,term,trunc,info=env.step(ap.get_action(obs))
           8 +print('queue', ap.queue[:2])
           9 +for n in sorted(obs.get_object_names()):
          10 +    o=obs.get_object_from_name(n)
          11 +    if n=='robot':
          12 +        print(n,[round(obs.get(o,f),4) for f in ['finger_state','grasp_active']]); continue
          13 +    print(n,[round(obs.get(o,f),4) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z','pose_qz','pose_qw']])
```

</details>

<a id="C022"></a>
### C022 · per-object yaw cycling; skip depth retries when descent blocked high

Commit `98402a6b6080870e69842542bd5d7d21648c1c03`; parents: c6d49bbcd14d7d3f03a760459ed66ff0e5847fd0. Recorded author date: 2026-09-30T23:08:50+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0966](01_timeline.md#E0966): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_98402a6_approach.py) · [Exact all-file diff](evidence/diffs/C022_98402a6.diff)

[Previous saved controller snapshot](evidence/versions/C021_c6d49bb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ef9df33..fceccb2 100644
--- a/approach.py
+++ b/approach.py
@@ -137,7 +137,7 @@ class GeneratedApproach:
  137    137              yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
  138    138              return _wrap(yaw)
  139    139          cands.sort(reverse=True)
  140        -        idx = self.grasp_fail % len(cands)
         140 +        idx = self.fail_count.get(obj.name, 0) % len(cands)
  141    141          return cands[idx][1]
  142    142  
  143    143      def _plan_pick_place(self, s, obj, place_xy, support_top, others, place_yaw=None):
@@ -269,6 +269,13 @@ class GeneratedApproach:
  269    269                  self.grasp_fail = 0
  270    270                  return None
  271    271              self.retries += 1
         272 +            if len(cmd) > 4 and cmd[4]:
         273 +                M = fk(base, q, TOOL)
         274 +                if M[2, 3] > cmd[2][2] + 0.035 + 0.025:
         275 +                    # descent was blocked well above the object: depth retries pointless
         276 +                    cmd = cmd[:4] + ([],)
         277 +                    self.queue[0] = cmd
         278 +                    self.retries = 3
  272    279              if self.retries > 2 and len(cmd) > 4 and cmd[4]:
  273    280                  # failed grasp: open, try another depth in place
  274    281                  self.retries = 0
diff --git a/clr.py b/clr.py
new file mode 100644
index 0000000..7e5543b
--- /dev/null
+++ b/clr.py
@@ -0,0 +1,10 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]), options={"object_count":int(sys.argv[2])})
           5 +ap=GeneratedApproach(env.action_space, env.observation_space, None); ap.reset(obs,info)
           6 +cubes=[obs.get_object_from_name(n) for n in sorted(obs.get_object_names()) if n.startswith('obs')]
           7 +tb=obs.get_object_from_name('target_block')
           8 +for c in cubes:
           9 +    oth=[d for d in cubes if d.name!=c.name]+[tb]
          10 +    print(c.name, [round(ap._finger_clearance(obs,c,k*np.pi/2,oth),4) for k in range(4)])
diff --git a/res3.txt b/res3.txt
index 2c3ab26..5026897 100644
--- a/res3.txt
+++ b/res3.txt
@@ -3,3 +3,6 @@
    3      3  count 6 success 14 / 16 mean steps 410.8125 max compute 10.7
    4      4  (11, 5, False, 1000, 8.4)
    5      5  count 5 success 15 / 16 mean steps 353.625 max compute 8.4
           6 +(58, 1, True, 55, 16.6)
           7 +(59, 2, True, 153, 21.3)
           8 +success 60 / 60 mean steps 80.05
```

</details>

<a id="C023"></a>
### C023 · dedupe grasp yaw candidates modulo pi

Commit `96188c98039031db46bf6387a822d4c8c3e727c3`; parents: 98402a6b6080870e69842542bd5d7d21648c1c03. Recorded author date: 2026-09-30T23:27:13+02:00.

File roles (automatic): policy, setup/other.

- [E1032](01_timeline.md#E1032): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C023_96188c9_approach.py) · [Exact all-file diff](evidence/diffs/C023_96188c9.diff)

[Previous saved controller snapshot](evidence/versions/C022_98402a6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fceccb2..81dc975 100644
--- a/approach.py
+++ b/approach.py
@@ -120,8 +120,10 @@ class GeneratedApproach:
  120    120          cy = np.arctan2(M[1, 0], M[0, 0])
  121    121          steps = 4 if aligned_only else 24
  122    122          cands = []
  123        -        for k in range(steps):
         123 +        for k in range(steps // 2):
  124    124              yaw = oyaw + k * (2 * np.pi / steps)
         125 +            if abs(_wrap(yaw + np.pi - cy)) < abs(_wrap(yaw - cy)):
         126 +                yaw = yaw + np.pi  # parallel gripper: yaw and yaw+pi are equivalent
  125    127              rel = yaw - oyaw
  126    128              span = abs(np.cos(rel)) * h[0] + abs(np.sin(rel)) * h[1]
  127    129              if span > 0.041:
diff --git a/res4.txt b/res4.txt
new file mode 100644
index 0000000..70a3051
--- /dev/null
+++ b/res4.txt
@@ -0,0 +1,7 @@
           1 +(58, 1, True, 55, 15.7)
           2 +(59, 2, True, 147, 22.2)
           3 +success 60 / 60 mean steps 84.76666666666667
           4 +(13, 4, False, 1000, 8.3)
           5 +count 4 success 15 / 16 mean steps 250.625 max compute 8.3
           6 +(11, 5, False, 1000, 36.5)
           7 +count 5 success 15 / 16 mean steps 349.875 max compute 36.5
```

</details>

<a id="C024"></a>
### C024 · coarse approach/lift/place moves with fine fallback on rejection

Commit `b927adaa3c5585700978d3163cdc13f66b5510bb`; parents: 96188c98039031db46bf6387a822d4c8c3e727c3. Recorded author date: 2026-09-30T23:46:33+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E1113](01_timeline.md#E1113): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C024_b927ada_approach.py) · [Exact all-file diff](evidence/diffs/C024_b927ada.diff)

[Previous saved controller snapshot](evidence/versions/C023_96188c9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 81dc975..8910876 100644
--- a/approach.py
+++ b/approach.py
@@ -155,13 +155,13 @@ class GeneratedApproach:
  155    155          return [
  156    156              ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
  157    157              ('move', np.array([p[0], p[1], gz + 0.02]), yaw, False),
  158        -            ('move', np.array([p[0], p[1], gz]), yaw, True, FINE),
         158 +            ('move', np.array([p[0], p[1], gz]), yaw, True),
  159    159              ('close', obj.name, p.copy(), yaw, [0.045, 0.03, 0.05, 0.025]),
  160        -            ('move', np.array([p[0], p[1], gz + 0.03]), yaw, False, FINE),
         160 +            ('move', np.array([p[0], p[1], gz + 0.03]), yaw, False),
  161    161              ('move', np.array([p[0], p[1], SAFE_Z]), yaw, False),
  162    162              ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
  163    163              ('place_move', place_center + np.array([0, 0, 0.02]), yaw, False),
  164        -            ('place_move', place_center, yaw, True, FINE),
         164 +            ('place_move', place_center, yaw, True),
  165    165              ('open', place_center, yaw),
  166    166              ('move_rel_up', SAFE_Z, yaw),
  167    167          ]
@@ -177,7 +177,7 @@ class GeneratedApproach:
  177    177              ('move_rel_up', SAFE_Z, yaw),
  178    178              ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
  179    179              ('place_move', place_center + np.array([0, 0, 0.02]), yaw, False),
  180        -            ('place_move', place_center, yaw, True, FINE),
         180 +            ('place_move', place_center, yaw, True),
  181    181              ('open', place_center, yaw),
  182    182              ('move_rel_up', SAFE_Z, yaw),
  183    183          ]
diff --git a/res5.txt b/res5.txt
new file mode 100644
index 0000000..f3ec86a
--- /dev/null
+++ b/res5.txt
@@ -0,0 +1,5 @@
           1 +(59, 2, True, 147, 24.3)
           2 +success 60 / 60 mean steps 84.33333333333333
           3 +count 4 success 16 / 16 mean steps 211.375 max compute 4.0
           4 +count 5 success 16 / 16 mean steps 268.8125 max compute 6.0
           5 +count 6 success 16 / 16 mean steps 321.0 max compute 8.2
diff --git a/timeit.py b/timeit.py
new file mode 100644
index 0000000..723e46b
--- /dev/null
+++ b/timeit.py
@@ -0,0 +1,13 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +env=make_env(); seed=int(sys.argv[1])
           5 +opts={"object_count":int(sys.argv[2])} if len(sys.argv)>2 else None
           6 +obs,info=env.reset(seed=seed, options=opts)
           7 +ap=GeneratedApproach(env.action_space, env.observation_space, None)
           8 +t0=time.time(); ap.reset(obs,info); tc=time.time()-t0; te=0
           9 +for t in range(1000):
          10 +    t0=time.time(); a=ap.get_action(obs); tc+=time.time()-t0
          11 +    t0=time.time(); obs,r,term,trunc,info=env.step(a); te+=time.time()-t0
          12 +    if term or trunc: break
          13 +print('steps',t+1,'term',term,'policy s',round(tc,2),'env s',round(te,2))
```

</details>

<a id="C025"></a>
### C025 · drop intermediate waypoints

Commit `1fc5850028b864e9ac5f165f06642b9f98b9acda`; parents: b927adaa3c5585700978d3163cdc13f66b5510bb. Recorded author date: 2026-09-30T23:53:26+02:00.

File roles (automatic): policy.

- [E1136](01_timeline.md#E1136): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_1fc5850_approach.py) · [Exact all-file diff](evidence/diffs/C025_1fc5850.diff)

[Previous saved controller snapshot](evidence/versions/C024_b927ada_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8910876..103e1ca 100644
--- a/approach.py
+++ b/approach.py
@@ -154,13 +154,10 @@ class GeneratedApproach:
  154    154          gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
  155    155          return [
  156    156              ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
  157        -            ('move', np.array([p[0], p[1], gz + 0.02]), yaw, False),
  158    157              ('move', np.array([p[0], p[1], gz]), yaw, True),
  159    158              ('close', obj.name, p.copy(), yaw, [0.045, 0.03, 0.05, 0.025]),
  160        -            ('move', np.array([p[0], p[1], gz + 0.03]), yaw, False),
  161    159              ('move', np.array([p[0], p[1], SAFE_Z]), yaw, False),
  162    160              ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
  163        -            ('place_move', place_center + np.array([0, 0, 0.02]), yaw, False),
  164    161              ('place_move', place_center, yaw, True),
  165    162              ('open', place_center, yaw),
  166    163              ('move_rel_up', SAFE_Z, yaw),
@@ -176,7 +173,6 @@ class GeneratedApproach:
  176    173          return [
  177    174              ('move_rel_up', SAFE_Z, yaw),
  178    175              ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
  179        -            ('place_move', place_center + np.array([0, 0, 0.02]), yaw, False),
  180    176              ('place_move', place_center, yaw, True),
  181    177              ('open', place_center, yaw),
  182    178              ('move_rel_up', SAFE_Z, yaw),
```

</details>

<a id="C026"></a>
### C026 · dynamic transit heights

Commit `73e7580acf97b5ea571fc2b90c79a9f7d1a0c8a5`; parents: 1fc5850028b864e9ac5f165f06642b9f98b9acda. Recorded author date: 2026-10-01T00:00:24+02:00.

File roles (automatic): policy.

- [E1153](01_timeline.md#E1153): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C026_73e7580_approach.py) · [Exact all-file diff](evidence/diffs/C026_73e7580.diff)

[Previous saved controller snapshot](evidence/versions/C025_1fc5850_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 103e1ca..bf0b3ca 100644
--- a/approach.py
+++ b/approach.py
@@ -142,6 +142,14 @@ class GeneratedApproach:
  142    142          idx = self.fail_count.get(obj.name, 0) % len(cands)
  143    143          return cands[idx][1]
  144    144  
         145 +    def _safe_heights(self, s, obj, others):
         146 +        tops = [TABLE_Z] + [_pose(s, o)[2] + _he(s, o)[2] for o in others if o.name != obj.name]
         147 +        top = max(tops)
         148 +        h = _he(s, obj)
         149 +        z_free = float(np.clip(top + 0.06, 0.18, SAFE_Z))
         150 +        z_held = float(np.clip(top + 0.08 + 2 * h[2], 0.18, SAFE_Z))
         151 +        return z_free, z_held
         152 +
  145    153      def _plan_pick_place(self, s, obj, place_xy, support_top, others, place_yaw=None):
  146    154          _, q, base = self._robot(s)
  147    155          p = _pose(s, obj)
@@ -152,15 +160,16 @@ class GeneratedApproach:
  152    160          self.place_yaw = place_yaw
  153    161          self.cur_obj = obj.name
  154    162          gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
         163 +        zf, zh = self._safe_heights(s, obj, others)
  155    164          return [
  156        -            ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
         165 +            ('move', np.array([p[0], p[1], max(zf, gz + 0.05)]), yaw, False),
  157    166              ('move', np.array([p[0], p[1], gz]), yaw, True),
  158    167              ('close', obj.name, p.copy(), yaw, [0.045, 0.03, 0.05, 0.025]),
  159        -            ('move', np.array([p[0], p[1], SAFE_Z]), yaw, False),
  160        -            ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
         168 +            ('move', np.array([p[0], p[1], zh]), yaw, False),
         169 +            ('place_move', place_center + np.array([0, 0, zh - place_center[2]]), yaw, False),
  161    170              ('place_move', place_center, yaw, True),
  162    171              ('open', place_center, yaw),
  163        -            ('move_rel_up', SAFE_Z, yaw),
         172 +            ('move_rel_up', zf, yaw),
  164    173          ]
  165    174  
  166    175      def _plan_place(self, s, obj, place_xy, support_top, place_yaw):
```

</details>

<a id="C027"></a>
### C027 · fine mode only for first 6 waypoints

Commit `9d0edffc76deda9336c9825378bcf8be10da0046`; parents: 73e7580acf97b5ea571fc2b90c79a9f7d1a0c8a5. Recorded author date: 2026-10-01T00:06:49+02:00.

File roles (automatic): policy.

- [E1178](01_timeline.md#E1178): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C027_9d0edff_approach.py) · [Exact all-file diff](evidence/diffs/C027_9d0edff.diff)

[Previous saved controller snapshot](evidence/versions/C026_73e7580_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bf0b3ca..8b2d645 100644
--- a/approach.py
+++ b/approach.py
@@ -385,7 +385,7 @@ class GeneratedApproach:
  385    385              return None
  386    386          # furthest waypoint reachable in one step
  387    387          k = self.pidx
  388        -        if self.fine:
         388 +        if self.fine and k < 6:
  389    389              k = min(k + 1, len(path) - 1)
  390    390          else:
  391    391              while k + 1 < len(path) and np.max(np.abs(path[k + 1] - q)) <= MAXD:
```

</details>

<a id="C028"></a>
### C028 · joint-space interpolation for high transits

Commit `f0d925adba353feb89e984d0bcfb872cf39d2b87`; parents: 9d0edffc76deda9336c9825378bcf8be10da0046. Recorded author date: 2026-10-01T00:13:46+02:00.

File roles (automatic): policy.

- [E1199](01_timeline.md#E1199): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C028_f0d925a_approach.py) · [Exact all-file diff](evidence/diffs/C028_f0d925a.diff)

[Previous saved controller snapshot](evidence/versions/C027_9d0edff_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8b2d645..30e5d36 100644
--- a/approach.py
+++ b/approach.py
@@ -162,11 +162,11 @@ class GeneratedApproach:
  162    162          gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
  163    163          zf, zh = self._safe_heights(s, obj, others)
  164    164          return [
  165        -            ('move', np.array([p[0], p[1], max(zf, gz + 0.05)]), yaw, False),
         165 +            ('move', np.array([p[0], p[1], max(zf, gz + 0.05)]), yaw, False, None, 'joint'),
  166    166              ('move', np.array([p[0], p[1], gz]), yaw, True),
  167    167              ('close', obj.name, p.copy(), yaw, [0.045, 0.03, 0.05, 0.025]),
  168    168              ('move', np.array([p[0], p[1], zh]), yaw, False),
  169        -            ('place_move', place_center + np.array([0, 0, zh - place_center[2]]), yaw, False),
         169 +            ('place_move', place_center + np.array([0, 0, zh - place_center[2]]), yaw, False, None, 'joint'),
  170    170              ('place_move', place_center, yaw, True),
  171    171              ('open', place_center, yaw),
  172    172              ('move_rel_up', zf, yaw),
@@ -181,7 +181,7 @@ class GeneratedApproach:
  181    181          place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
  182    182          return [
  183    183              ('move_rel_up', SAFE_Z, yaw),
  184        -            ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
         184 +            ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False, None, 'joint'),
  185    185              ('place_move', place_center, yaw, True),
  186    186              ('open', place_center, yaw),
  187    187              ('move_rel_up', SAFE_Z, yaw),
@@ -358,6 +358,11 @@ class GeneratedApproach:
  358    358                  qc, ok = ik(base, qc, p0 + f * (pos - p0), down_R(y0 + f * dy), tool=TOOL,
  359    359                              iters=100 if i < n else 300)
  360    360                  path.append(qc.copy())
         361 +            if len(cmd) > 5 and cmd[5] == 'joint' and path:
         362 +                # high transit: straight line in joint space (fewest steps)
         363 +                dq = path[-1] - q
         364 +                m = int(np.ceil(np.max(np.abs(dq)) / (MAXD * 0.999))) or 1
         365 +                path = [q + dq * (i / m) for i in range(1, m + 1)]
  361    366              self.qtarget = path
  362    367              self.pidx = 0
  363    368              self.last_q = None
```

</details>

<a id="C029"></a>
### C029 · test results/scripts

Commit `c30325a2d8738f93028e2d4f1812e5d43113e44c`; parents: f0d925adba353feb89e984d0bcfb872cf39d2b87. Recorded author date: 2026-10-01T00:56:28+02:00.

File roles (automatic): setup/other.

- [E1309](01_timeline.md#E1309): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C029_c30325a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res6.txt b/res6.txt
new file mode 100644
index 0000000..04bb95f
--- /dev/null
+++ b/res6.txt
@@ -0,0 +1,6 @@
           1 +(98, 1, True, 46, 18.9)
           2 +(99, 2, True, 73, 12.6)
           3 +success 100 / 100 mean steps 43.56
           4 +count 3 success 16 / 16 mean steps 83.1875 max compute 2.2
           5 +count 5 success 16 / 16 mean steps 148.125 max compute 3.9
           6 +count 6 success 16 / 16 mean steps 200.5625 max compute 8.1
diff --git a/res7.txt b/res7.txt
new file mode 100644
index 0000000..eb5f795
--- /dev/null
+++ b/res7.txt
@@ -0,0 +1,4 @@
           1 +(198, 1, True, 41, 16.2)
           2 +(199, 1, True, 41, 11.6)
           3 +success 100 / 100 mean steps 42.12
           4 +count 8 success 8 / 8 mean steps 363.75 max compute 11.6
```

</details>

