# Obstruction3D · claude-opus-5-5 · replicate 444: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `b948608` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `7c86a54` | Calibrated FK for Kinova gen3 (mount offset, tool offset), calibration scripts | calib1.py, calib2.py, calib3.py, calib4.py, calib_0_0.0_0.0_0.0_0.25.json, calib_0_1.5708_0.0_0.0_0.26.json, calib_1_0.7_0.1_0.0_0.25.json, calib_2_0.0_-0.1_0.2_0.27.json, calib_3… | [E0071](01_timeline.md#E0071) |
| [C003](#C003) · `cb6f0b4` | First full approach: clear obstructions then place block | approach.py, pp1.py, pp2.py, pp3.py, pp4.py, stats.py, test_approach.py | [E0104](01_timeline.md#E0104) |
| [C004](#C004) · `5ab379c` | Finger collision model for grasp candidates, blocked-move abort, grasp height band | approach.py, dbg1.py, dbg2.py, o1.txt, o2.txt, o3.txt, pp5.py, scan.py | [E0186](01_timeline.md#E0186) |
| [C005](#C005) · `e469cf1` | fix abort flag | approach.py | [E0194](01_timeline.md#E0194) |
| [C006](#C006) · `b36e4ca` | lateral escape before lifting held object from touching neighbours | approach.py | [E0206](01_timeline.md#E0206) |
| [C007](#C007) · `85a15bc` | 100/100 seeds 0-99; process-based test runner | dbg3.py, test_approach.py | [E0234](01_timeline.md#E0234) |
| [C008](#C008) · `8db5dca` | finer grasp offset candidates using measured grasp tolerance | approach.py, dbg3.py, test_approach.py | [E0329](01_timeline.md#E0329) |
| [C009](#C009) · `36ac886` | grasp sweep region must be free of other objects | approach.py | [E0349](01_timeline.md#E0349) |
| [C010](#C010) · `d16351b` | height-aware grasp candidates, diagonal yaws | approach.py | [E0359](01_timeline.md#E0359) |
| [C011](#C011) · `88598b5` | v2: choose symmetric yaw by full plan cost | approach_v2.py, dbg3.py, dbg4.py, gscan.py, gscan2.py, r10.txt, r4.txt, r7.txt, rd.txt, test_approach.py, timing.py | [E0498](01_timeline.md#E0498) |
| [C012](#C012) · `d07733f` | Promote v2 (lookahead pursuit, low transit, plan-cost yaw choice): 100/100, mean 32 steps | approach.py | [E0534](01_timeline.md#E0534) |
| [C013](#C013) · `872a421` | v2: choose escape direction by clearance search | approach_v2.py, r10v2.txt, r7v2.txt | [E0570](01_timeline.md#E0570) |
| [C014](#C014) · `260fcb1` | IK: clamp to joint limits | approach_v2.py, kin.py | [E0591](01_timeline.md#E0591) |
| [C015](#C015) · `32c237a` | denser cartesian waypoints | approach_v2.py, probe4.py | [E0614](01_timeline.md#E0614) |
| [C016](#C016) · `64cb9b1` | escape: search dist+dir for clearance, slow lift when tight | approach_v2.py, probe5.py | [E0630](01_timeline.md#E0630) |
| [C017](#C017) · `3fc7f32` | Promote v2 with escape/IK fixes: 100/100 mean 32.8 | approach.py, r7v2.txt, rdv2.txt | [E0675](01_timeline.md#E0675) |
| [C018](#C018) · `3a57589` | kin: analytic Jacobian for IK (faster) | kin.py, r10v2.txt, r7v2.txt | [E0707](01_timeline.md#E0707) |
| [C019](#C019) · `c5d528b` | ban failed free spots, avoid spots near robot base | approach_v2.py, prof.out, r5.txt, r9.txt, rd2.txt | [E0861](01_timeline.md#E0861) |
| [C020](#C020) · `118102d` | grasp height: fingertip offset 0.0305 measured, z_hi top+0.028 | approach_v2.py, d101.txt, d121.txt, probe6.py, probe7.py | [E0900](01_timeline.md#E0900) |
| [C021](#C021) · `3afee96` | sweep-box check uses conservative height; finger check tight | approach_v2.py, d101.txt, d113.txt, probe7.py, r7v2.txt, r9.txt, rdv2.txt | [E0964](01_timeline.md#E0964) |
| [C022](#C022) · `1fc8053` | Promote: grasp height model fixes, bad-spot banning; 9-obs 30/30 | approach.py, d101.txt, d113.txt, r10v2.txt, r7v2.txt, r9.txt | [E1025](01_timeline.md#E1025) |
| [C023](#C023) · `fd8e56a` | faster fk_jac; early-stop failing pick paths | approach_v2.py, kin.py, prof.out, r10v2.txt, r12.txt, r15.txt, rd3.txt, timing.py | [E1153](01_timeline.md#E1153) |
| [C024](#C024) · `2b3712c` | move base backward when pick/place point is too close to arm mount | approach_v2.py, basetest.py, d312.txt, reach.py | [E1198](01_timeline.md#E1198) |
| [C025](#C025) · `c09ea7f` | Promote: base backoff for near-mount objects, faster IK; 15-obs 16/16, default 100/100 | approach.py, r10v2.txt, r15.txt, r7v2.txt, rdv2.txt | [E1269](01_timeline.md#E1269) |
| [C026](#C026) · `e7d8ee4` | Test results for 12-obstruction stress batch | r12b.txt | [E1318](01_timeline.md#E1318) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `b9486084db5b5332b93d312d20346790b07976ae`; parents: none (initial snapshot). Recorded author date: 2026-09-30T20:27:47+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_b948608.diff)

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
index 0000000..7024687
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "0c4a4786fff956a467b85aee4233332b", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Calibrated FK for Kinova gen3 (mount offset, tool offset), calibration scripts

Commit `7c86a54d1d334524b83e177a079dbc99a4c8b2a4`; parents: b9486084db5b5332b93d312d20346790b07976ae. Recorded author date: 2026-09-30T20:33:10+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0071](01_timeline.md#E0071): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C002_7c86a54.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/calib1.py b/calib1.py
new file mode 100644
index 0000000..8afe51f
--- /dev/null
+++ b/calib1.py
@@ -0,0 +1,20 @@
           1 +import sys; YAW=float(sys.argv[1])
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from common import *
           5 +env = make_env()
           6 +obs, info = env.reset(seed=0)
           7 +b = objd(obs,'target_block'); print(b)
           8 +base = getbase(obs); q = getq(obs)
           9 +p = np.array([b['pose_x'], b['pose_y'], 0.40])
          10 +for z in np.arange(0.40, 0.0, -0.005):
          11 +    p[2]=z
          12 +    qt, ok = kin.ik(base, getq(obs), p, kin.topdown_R(YAW))
          13 +    obs, blocked = move_to(env, obs, qt)
          14 +    if blocked: print('blocked at', z); break
          15 +    a=np.zeros(11,dtype=np.float32); a[10]=-1
          16 +    obs,*_ = env.step(a)
          17 +    R=robot(obs)
          18 +    g=obs.get(R,'grasp_active'); fs=obs.get(R,'finger_state')
          19 +    if g or fs: print(round(z,3), 'grasp', g, fs, [round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
          20 +    a[10]=1; obs,*_=env.step(a)
diff --git a/calib2.py b/calib2.py
new file mode 100644
index 0000000..6a34cde
--- /dev/null
+++ b/calib2.py
@@ -0,0 +1,15 @@
           1 +import sys
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from common import *
           5 +env = make_env()
           6 +obs, info = env.reset(seed=0)
           7 +base = getbase(obs)
           8 +for (x,y) in [(0.2,-0.1),(0.3,-0.2),(0.15,0.0)]:
           9 +    p = np.array([x,y,0.40])
          10 +    for z in np.arange(0.40, -0.2, -0.005):
          11 +        p[2]=z
          12 +        qt, ok = kin.ik(base, getq(obs), p, kin.topdown_R(0))
          13 +        obs, blocked = move_to(env, obs, qt)
          14 +        if blocked or not ok: print(x,y,'blocked at', round(z,3), ok); break
          15 +    p[2]=0.4; qt, ok = kin.ik(base, getq(obs), p, kin.topdown_R(0)); obs,_=move_to(env,obs,qt)
diff --git a/calib3.py b/calib3.py
new file mode 100644
index 0000000..cd8ef70
--- /dev/null
+++ b/calib3.py
@@ -0,0 +1,21 @@
           1 +from env_client import make_env
           2 +import numpy as np, kin
           3 +from common import *
           4 +env = make_env()
           5 +obs, info = env.reset(seed=0)
           6 +b = objd(obs,'target_block')
           7 +base = getbase(obs)
           8 +hits=[]
           9 +for dx in np.arange(-0.08,0.081,0.02):
          10 +  for dy in np.arange(-0.08,0.081,0.02):
          11 +    for z in [0.33, 0.25]:
          12 +        qt, ok = kin.ik(base, getq(obs), np.array([b['pose_x']+dx,b['pose_y']+dy,z]), kin.topdown_R(0))
          13 +        obs, blocked = move_to(env, obs, qt)
          14 +    a=np.zeros(11,dtype=np.float32); a[10]=-1
          15 +    obs,r,t,tr,info = env.step(a)
          16 +    R=robot(obs)
          17 +    if obs.get(R,'grasp_active') or obs.get(R,'finger_state'):
          18 +        hits.append((dx,dy)); print('HIT',round(dx,2),round(dy,2),blocked,[round(obs.get(R,f),4) for f in ['finger_state','grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']], objd(obs,'target_block')['pose_z'])
          19 +    a[10]=1; obs,*_=env.step(a)
          20 +    qt, ok = kin.ik(base, getq(obs), np.array([b['pose_x']+dx,b['pose_y']+dy,0.33]), kin.topdown_R(0)); obs,_=move_to(env,obs,qt)
          21 +print(hits, tr)
diff --git a/calib4.py b/calib4.py
new file mode 100644
index 0000000..41aadc8
--- /dev/null
+++ b/calib4.py
@@ -0,0 +1,28 @@
           1 +import sys, json
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from common import *
           5 +GF=['finger_state','grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']
           6 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); bdy=float(sys.argv[3]); brot=float(sys.argv[4]); zs=float(sys.argv[5])
           7 +env = make_env()
           8 +obs, info = env.reset(seed=seed)
           9 +# move base
          10 +a=np.zeros(11,dtype=np.float32); a[1]=bdy; a[2]=brot; obs,*_=env.step(a)
          11 +b = objd(obs,'target_block')
          12 +base = getbase(obs)
          13 +data=[]
          14 +for dx in np.arange(-0.16,-0.019,0.02):
          15 +  for dy in np.arange(-0.06,0.061,0.02):
          16 +    for z in [0.35, zs]:
          17 +        qt, ok = kin.ik(base, getq(obs), np.array([b['pose_x']+dx,b['pose_y']+dy,z]), kin.topdown_R(yaw))
          18 +        obs, blocked = move_to(env, obs, qt)
          19 +    a=np.zeros(11,dtype=np.float32); a[10]=-1
          20 +    obs,r,t,tr,info = env.step(a)
          21 +    R=robot(obs)
          22 +    if obs.get(R,'grasp_active'):
          23 +        bb=objd(obs,'target_block')
          24 +        data.append(dict(base=list(getbase(obs)), q=list(getq(obs)), g=[obs.get(R,f) for f in GF], obj=[bb[k] for k in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']], dxdy=[dx,dy]))
          25 +    a[10]=1; obs,*_=env.step(a)
          26 +    qt, ok = kin.ik(base, getq(obs), np.array([b['pose_x']+dx,b['pose_y']+dy,0.35]), kin.topdown_R(yaw)); obs,_=move_to(env,obs,qt)
          27 +print(len(data), [d['dxdy'] for d in data])
          28 +json.dump(data, open(f'calib_{seed}_{yaw}_{bdy}_{brot}_{zs}.json','w'))
diff --git a/calib_0_0.0_0.0_0.0_0.25.json b/calib_0_0.0_0.0_0.0_0.25.json
new file mode 100644
index 0000000..25e16c9
--- /dev/null
+++ b/calib_0_0.0_0.0_0.0_0.25.json
@@ -0,0 +1 @@
           1 +[{"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.2870005965232849, 0.4160257577896118, -3.4516100883483887, -2.1226449012756348, 0.2103724181652069, -0.6312611699104309, 0.8280736207962036], "g": [0.41999998688697815, 2.415478229522705e-05, 0.040108442306518555, 0.02482198178768158, 0.7070975303649902, 0.7071159482002258, 9.148131539404858e-06, 2.3086780856829137e-05], "obj": [0.33598166704177856, 0.17328143119812012, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0], "dxdy": [-0.16, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.31971222162246704, 0.43703198432922363, -3.476902484893799, -2.089561939239502, 0.23226627707481384, -0.6496250629425049, 0.7591173052787781], "g": [0.019999999552965164, -0.019978255033493042, 0.04010644555091858, 0.024818137288093567, 0.707098662853241, 0.7071148157119751, 7.253324838529807e-06, 1.937559682119172e-05], "obj": [0.33598172664642334, 0.17328143119812012, 0.09999998658895493, -1.8189898372267255e-12, -2.2737371881131896e-12, -9.094949186133627e-13, 1.0], "dxdy": [-0.16, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.21772509813308716, 0.4540444314479828, -3.51363205909729, -2.067230701446533, 0.261509507894516, -0.6643514633178711, 0.8081356883049011], "g": [0.41999998688697815, 2.078711986541748e-05, 0.020108461380004883, 0.024818748235702515, 0.7070989608764648, 0.7071145176887512, 7.728209311608225e-06, 1.7548769392305985e-05], "obj": [0.33598172664642334, 0.1732814460992813, 0.09999997168779373, -4.547474376226379e-12, -4.092727025339915e-12, -5.960556848094711e-08, 1.0], "dxdy": [-0.14, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.2529091536998749, 0.4744635820388794, -3.534931182861328, -2.0352368354797363, 0.2811085283756256, -0.682933509349823, 0.743935763835907], "g": [0.019999999552965164, -0.0199815034866333, 0.020106613636016846, 0.024815142154693604, 0.7070998549461365, 0.7071136236190796, 6.415197731257649e-06, 1.4459465091931634e-05], "obj": [0.33598172664642334, 0.17328141629695892, 0.09999996423721313, -7.275958481545164e-12, -2.5011108635564216e-12, -1.6391371104873542e-07, 1.0], "dxdy": [-0.14, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.0853462815284729, 0.4141569435596466, -3.587122678756714, -1.9839249849319458, 0.252903014421463, -0.7954311370849609, 0.889722466468811], "g": [0.1599999964237213, 0.021173641085624695, -0.004429250955581665, 0.059362031519412994, 0.7087827920913696, 0.7054216265678406, -0.0003921968745999038, -0.0026794937439262867], "obj": [0.3359817564487457, 0.17328137159347534, 0.09999995678663254, -8.640199666842818e-12, -9.094947017729282e-13, -3.278264557593502e-07, 1.0], "dxdy": [-0.12000000000000002, -0.01999999999999999]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.1562475562095642, 0.4940178096294403, -3.572148561477661, -2.0101447105407715, 0.3119865357875824, -0.7005800604820251, 0.7885538339614868], "g": [0.41999998688697815, 1.7181038856506348e-05, 0.00010797381401062012, 0.02481483668088913, 0.7071003317832947, 0.7071132063865662, 6.6020284066325985e-06, 1.2558791240735445e-05], "obj": [0.3359817564487457, 0.17328138649463654, 0.09999996423721313, -1.1641532182693481e-10, 1.7462298274040222e-10, -2.3818915906304028e-07, 1.0], "dxdy": [-0.12000000000000002, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.1940302550792694, 0.5136257410049438, -3.5890376567840576, -1.9791336059570312, 0.3285779356956482, -0.71909499168396, 0.7297577857971191], "g": [0.019999999552965164, -0.01998475193977356, 0.00010630488395690918, 0.024811744689941406, 0.7071011066436768, 0.7071124315261841, 5.768853043264244e-06, 1.0171920621360186e-05], "obj": [0.3359817564487457, 0.17328138649463654, 0.09999996423721313, -1.177795638795942e-10, 1.7530510376673192e-10, -2.980232238769531e-07, 1.0], "dxdy": [-0.12000000000000002, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.035355012863874435, 0.46460652351379395, -3.641256332397461, -1.9302701950073242, 0.30493655800819397, -0.8195868134498596, 0.8654988408088684], "g": [0.07000000029802322, 0.021016180515289307, -0.024073779582977295, 0.056302741169929504, 0.7086993455886841, 0.7055062651634216, -0.0002901286934502423, -0.0024514796677976847], "obj": [0.3359817564487457, 0.17328138649463654, 0.09999996423721313, -1.1868905858136714e-10, 1.765556589816697e-10, -3.278264557593502e-07, 1.0], "dxdy": [-0.10000000000000003, -0.01999999999999999]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.1049070805311203, 0.5349417924880981, -3.6233081817626953, -1.9514681100845337, 0.3582077920436859, -0.7390907406806946, 0.7733193039894104], "g": [0.41999998688697815, 1.3723969459533691e-05, -0.01989281177520752, 0.024810791015625, 0.7071014642715454, 0.7071120142936707, 5.7779379858402535e-06, 8.415951015194878e-06], "obj": [0.3359817564487457, 0.17328138649463654, 0.09999996423721313, -3.4924596548080444e-10, 2.3283064365386963e-10, -2.83125928035588e-07, 1.0], "dxdy": [-0.10000000000000003, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.14494355022907257, 0.5535396933555603, -3.635951519012451, -1.9213180541992188, 0.3715832829475403, -0.7572370767593384, 0.7199808955192566], "g": [0.019999999552965164, -0.0199878066778183, -0.01989424228668213, 0.024808354675769806, 0.7071020007133484, 0.7071114778518677, 5.279432571114739e-06, 6.698525794490706e-06], "obj": [0.3359817564487457, 0.17328138649463654, 0.09999996423721313, -3.506102908001907e-10, 2.3345597677248975e-10, -3.725291151113197e-07, 1.0], "dxdy": [-0.10000000000000003, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.02545035257935524, 0.5584608912467957, -3.6503825187683105, -1.9178189039230347, 0.383262038230896, -0.7617750763893127, 0.8196353912353516], "g": [0.019999999552965164, 0.0200117826461792, -0.03989246487617493, 0.024808943271636963, 0.7071020007133484, 0.7071114778518677, 5.6392900660284795e-06, 6.315965038083959e-06], "obj": [0.33598172664642334, 0.17328138649463654, 0.09999997168779373, -3.515197855019636e-10, 2.332854465159073e-10, -3.5762795391747204e-07, 1.0], "dxdy": [-0.08000000000000004, -0.01999999999999999]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.0670357197523117, 0.574828028678894, -3.6610982418060303, -1.891290545463562, 0.3947380781173706, -0.77797532081604, 0.7677714228630066], "g": [0.41999998688697815, 1.0728836059570312e-05, -0.03989371657371521, 0.024807050824165344, 0.7071024775505066, 0.7071110606193542, 5.227694146014983e-06, 5.091739694762509e-06], "obj": [0.3359817564487457, 0.17328138649463654, 0.09999994933605194, -3.5288394428789616e-10, 2.333422344236169e-10, -4.023318069812376e-07, 1.0], "dxdy": [-0.08000000000000004, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.10857788473367691, 0.5923256874084473, -3.6701979637145996, -1.8618686199188232, 0.40520209074020386, -0.7955267429351807, 0.7193576097488403], "g": [0.019999999552965164, -0.01999032497406006, -0.03989478945732117, 0.024805307388305664, 0.7071028351783752, 0.7071106433868408, 4.951526534568984e-06, 3.898549493897008e-06], "obj": [0.3359817862510681, 0.17328140139579773, 0.09999994933605194, -3.531113179633394e-10, 2.332605220090045e-10, -4.321341293689329e-07, 1.0], "dxdy": [-0.08000000000000004, 0.020000000000000018]}]
\ No newline at end of file
diff --git a/calib_0_1.5708_0.0_0.0_0.26.json b/calib_0_1.5708_0.0_0.0_0.26.json
new file mode 100644
index 0000000..e8d9b0e
--- /dev/null
+++ b/calib_0_1.5708_0.0_0.0_0.26.json
@@ -0,0 +1 @@
           1 +[{"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.30286094546318054, 0.42282214760780334, -3.3019402027130127, -2.033414363861084, 0.1027507409453392, -0.692760705947876, 2.6131227016448975], "g": [0.25, -0.0001030266284942627, 0.02000613510608673, 0.0348023921251297, -4.7222365537891164e-06, 1.0, 4.578334028337849e-06, -1.5979957197487238e-06], "obj": [0.33598166704177856, 0.17328143119812012, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0], "dxdy": [-0.12000000000000002, -0.01999999999999999]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.3403034508228302, 0.43907496333122253, -3.3180696964263916, -2.005493402481079, 0.11523745954036713, -0.7062978148460388, 2.553426504135132], "g": [0.25, -0.00010231137275695801, 5.856156349182129e-06, 0.03480186313390732, -4.537549102678895e-06, 1.0, 4.157911916990997e-06, -1.773978169694601e-06], "obj": [0.33598166704177856, 0.17328143119812012, 0.09999999403953552, 0.0, 0.0, 0.0, 1.0], "dxdy": [-0.12000000000000002, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.37688058614730835, 0.4567912220954895, -3.332881450653076, -1.974661946296692, 0.12730935215950012, -0.721409261226654, 2.496816396713257], "g": [0.25, -0.00010159611701965332, -0.0199945867061615, 0.0348014160990715, -4.437789812072879e-06, 1.0, 3.777804977289634e-06, -2.0898576167383e-06], "obj": [0.33598166704177856, 0.17328143119812012, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0], "dxdy": [-0.12000000000000002, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.23802128434181213, 0.41599586606025696, -3.3613667488098145, -1.9349682331085205, 0.12533578276634216, -0.8033815026283264, 2.6131808757781982], "g": [0.18000000715255737, 0.022454291582107544, 0.01996268332004547, 0.05983595550060272, 0.0007933542365208268, 0.9999992847442627, -0.000826166826300323, -0.00045077645336277783], "obj": [0.33598166704177856, 0.1732814460992813, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0], "dxdy": [-0.10000000000000003, -0.01999999999999999]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.2788276970386505, 0.4340529441833496, -3.3718600273132324, -1.9098453521728516, 0.13513243198394775, -0.8122710585594177, 2.5584094524383545], "g": [0.14000000059604645, 0.02231648564338684, -0.00014568865299224854, 0.05885595828294754, 0.000774751475546509, 0.9999992847442627, -0.000771548948250711, -0.0004773827677126974], "obj": [0.3359817862510681, 0.1732814610004425, 0.10000000894069672, 2.9103830456733704e-11, 8.731149137020111e-11, 8.728306966077071e-11, 1.0], "dxdy": [-0.10000000000000003, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.0, 0.0], "q": [-0.318943589925766, 0.4536229968070984, -3.381120204925537, -1.8819078207015991, 0.14470423758029938, -0.8224921226501465, 2.5062527656555176], "g": [0.10999999940395355, 0.022162705659866333, -0.020247027277946472, 0.0577937513589859, 0.0007446109084412456, 0.9999994039535522, -0.0007083974196575582, -0.000490969221573323], "obj": [0.3359818160533905, 0.1732814610004425, 0.10000001639127731, 0.0, 8.731149137020111e-11, 5.8122395785176195e-11, 1.0], "dxdy": [-0.10000000000000003, 0.020000000000000018]}]
\ No newline at end of file
diff --git a/calib_1_0.7_0.1_0.0_0.25.json b/calib_1_0.7_0.1_0.0_0.25.json
new file mode 100644
index 0000000..74b3b68
--- /dev/null
+++ b/calib_1_0.7_0.1_0.0_0.25.json
@@ -0,0 +1 @@
           1 +[{"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.26773589849472046, -0.1842704862356186, -3.2494287490844727, -2.6600000858306885, -0.02166702039539814, -0.6630222201347351, 1.9119863510131836], "g": [0.6499999761581421, 0.009925533086061478, 0.047633737325668335, 0.058106616139411926, 0.42271971702575684, 0.9062543511390686, -0.0015091814566403627, -0.00297194579616189], "obj": [0.13774842023849487, 0.18313223123550415, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0], "dxdy": [-0.16, -0.039999999999999994]}, {"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.2748999297618866, -0.15184253454208374, -3.380523443222046, -2.643491506576538, -0.03345512971282005, -0.6481934785842896, 1.7810134887695312], "g": [0.2199999988079071, -0.003954589366912842, 0.03701314330101013, 0.05661475658416748, 0.4241759479045868, 0.9055454730987549, -0.005449970252811909, -0.005696948617696762], "obj": [0.13774842023849487, 0.18313224613666534, 0.09999998658895493, 0.0, -1.1641532182693481e-10, 0.0, 1.0], "dxdy": [-0.16, -0.01999999999999999]}, {"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.2838989794254303, -0.11214165389537811, -3.499363660812378, -2.620319366455078, -0.024103932082653046, -0.6315072178840637, 1.6420778036117554], "g": [0.07000000029802322, -0.01682233437895775, 0.025042816996574402, 0.05564654618501663, 0.42567771673202515, 0.9047852754592896, -0.008093939162790775, -0.00982843991369009], "obj": [0.13774843513965607, 0.18313224613666534, 0.09999999403953552, 0.0, 3.4924596548080444e-10, -3.637978807091713e-12, 1.0], "dxdy": [-0.16, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.29938510060310364, -0.06489291787147522, -3.6022469997406006, -2.593975067138672, 0.007391261402517557, -0.6136626601219177, 1.4939095973968506], "g": [0.029999999329447746, -0.02968185395002365, 0.012720495462417603, 0.05445673316717148, 0.4270249307155609, 0.9040799140930176, -0.009661913849413395, -0.013995463028550148], "obj": [0.13774842023849487, 0.18313224613666534, 0.10000000894069672, -9.313225746154785e-10, 0.0, 3.725290298461914e-08, 1.0], "dxdy": [-0.16, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.2621847987174988, -0.12064991146326065, -3.209597587585449, -2.635526418685913, -0.006739461794495583, -0.6266113519668579, 1.9450874328613281], "g": [0.14000000059604645, 0.021762201562523842, 0.034584030508995056, 0.05495080351829529, 0.4224380552768707, 0.9063894152641296, -0.001578300492838025, -0.0014078764943405986], "obj": [0.13774842023849487, 0.18313224613666534, 0.10000000149011612, -4.656613983300417e-10, -3.725291186640334e-09, -4.468893877174196e-08, 1.0], "dxdy": [-0.14, -0.039999999999999994]}, {"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.2791275978088379, -0.0924411490559578, -3.3233048915863037, -2.6185567378997803, -0.008805998601019382, -0.615100622177124, 1.8138322830200195], "g": [0.12999999523162842, 0.007963120937347412, 0.022503912448883057, 0.05383923649787903, 0.4236164391040802, 0.9058228731155396, -0.004053154494613409, -0.004187210462987423], "obj": [0.13774843513965607, 0.18313224613666534, 0.10000001639127731, -5.820767201569765e-10, -3.7543950170970675e-09, -1.1920283071731319e-07, 1.0], "dxdy": [-0.14, -0.01999999999999999]}, {"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.3496997058391571, 0.14157192409038544, -3.388460636138916, -2.564910888671875, 0.08088929206132889, -0.44061022996902466, 1.6034120321273804], "g": [0.20999999344348907, -0.002468027174472809, -0.028101667761802673, 0.024809643626213074, 0.4217688739299774, 0.9067034125328064, 6.082896106818225e-06, 6.881674380565528e-06], "obj": [0.13774843513965607, 0.18313221633434296, 0.10000000894069672, -9.313225746154785e-10, -5.704350769519806e-09, -2.607603164506145e-07, 1.0], "dxdy": [-0.10000000000000003, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.3525487780570984, 0.17075330018997192, -3.4840922355651855, -2.531353712081909, 0.1308170109987259, -0.4525947868824005, 1.4625873565673828], "g": [0.36000001430511475, -0.01776318997144699, -0.04098546504974365, 0.024815119802951813, 0.4217682480812073, 0.9067036509513855, 6.4210521486529615e-06, 9.723345101519953e-06], "obj": [0.13774845004081726, 0.18313221633434296, 0.1000000461935997, -9.313225746154785e-10, -5.705260264221579e-09, -2.756715389296005e-07, 1.0], "dxdy": [-0.10000000000000003, 0.04000000000000002]}, {"base": [-0.11999999731779099, 0.10000000149011612, 0.0], "q": [-0.19222868978977203, 0.1835925281047821, -3.5131492614746094, -2.5161232948303223, 0.15022382140159607, -0.4586346745491028, 1.5778167247772217], "g": [0.20999999344348907, 0.010417278856039047, -0.04339616000652313, 0.024816349148750305, 0.4217681288719177, 0.9067037105560303, 7.346840448008152e-06, 9.295408744947053e-06], "obj": [0.13774846494197845, 0.18313223123550415, 0.1000000461935997, -9.304130799137056e-10, -5.704123395844363e-09, -2.756715389296005e-07, 1.0], "dxdy": [-0.08000000000000004, 0.020000000000000018]}]
\ No newline at end of file
diff --git a/calib_2_0.0_-0.1_0.2_0.27.json b/calib_2_0.0_-0.1_0.2_0.27.json
new file mode 100644
index 0000000..b51e53b
--- /dev/null
+++ b/calib_2_0.0_-0.1_0.2_0.27.json
@@ -0,0 +1 @@
           1 +[{"base": [-0.11999999731779099, -0.10000000149011612, 0.20000000298023224], "q": [-1.127792239189148, -0.46623489260673523, -0.9708729982376099, -2.189910888671875, 0.5689483880996704, -0.759669303894043, 2.0331485271453857], "g": [0.09000000357627869, 0.01618063449859619, 0.022495344281196594, 0.044803187251091, 0.7071062326431274, 0.7071073055267334, 8.514832643413683e-07, 3.830258265224984e-06], "obj": [0.18906673789024353, -0.33527371287345886, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0], "dxdy": [-0.14, -0.039999999999999994]}, {"base": [-0.11999999731779099, -0.10000000149011612, 0.20000000298023224], "q": [-1.1329803466796875, -0.43124398589134216, -0.9852396845817566, -2.239452838897705, 0.5488840937614441, -0.7310950756072998, 2.0119378566741943], "g": [0.3400000035762787, -0.0038201212882995605, 0.02249811589717865, 0.04480922967195511, 0.7071055769920349, 0.7071079015731812, 3.117554342679796e-06, 3.7214308576949406e-06], "obj": [0.18906673789024353, -0.33527371287345886, 0.10000000894069672, -2.2737367544323206e-13, -2.2737367544323206e-13, 0.0, 1.0], "dxdy": [-0.14, -0.01999999999999999]}, {"base": [-0.11999999731779099, -0.10000000149011612, 0.20000000298023224], "q": [-1.1938122510910034, -0.4897584915161133, -0.9666816592216492, -2.1574606895446777, 0.5830002427101135, -0.7798084616661072, 1.973092794418335], "g": [0.09000000357627869, 0.016165107488632202, 0.002530917525291443, 0.04486469179391861, 0.7070950269699097, 0.7071185111999512, 2.57329702435527e-05, 8.808659003989305e-06], "obj": [0.18906672298908234, -0.33527371287345886, 0.10000000894069672, -6.821211889600221e-13, 7.815971719664361e-13, -1.3411047916633834e-07, 1.0], "dxdy": [-0.12000000000000002, -0.039999999999999994]}, {"base": [-0.11999999731779099, -0.10000000149011612, 0.20000000298023224], "q": [-1.2036939859390259, -0.45651760697364807, -0.9783748984336853, -2.205859899520874, 0.5652306079864502, -0.7515469789505005, 1.9473603963851929], "g": [0.3400000035762787, -0.0038190484046936035, 0.0024958401918411255, 0.044804736971855164, 0.7071059942245483, 0.7071074843406677, 1.3566327652370092e-06, 3.7349736885516904e-06], "obj": [0.18906672298908234, -0.33527371287345886, 0.10000000149011612, -5.4569682106375694e-12, 6.366462912410498e-12, -1.1920928955078125e-07, 1.0], "dxdy": [-0.12000000000000002, -0.01999999999999999]}, {"base": [-0.11999999731779099, -0.10000000149011612, 0.20000000298023224], "q": [-1.2595748901367188, -0.5130886435508728, -0.9584828019142151, -2.1221039295196533, 0.5942597389221191, -0.8000207543373108, 1.920529842376709], "g": [0.09000000357627869, 0.0161723792552948, -0.01748056709766388, 0.044843681156635284, 0.7070983648300171, 0.707115113735199, 1.8370708858128637e-05, 8.13796759757679e-06], "obj": [0.18906669318675995, -0.33527374267578125, 0.10000000149011612, -5.6843431871234085e-12, 6.1390905380098726e-12, -1.639128583974525e-07, 1.0], "dxdy": [-0.10000000000000003, -0.039999999999999994]}, {"base": [-0.11999999731779099, -0.10000000149011612, 0.20000000298023224], "q": [-1.2722864151000977, -0.4813748300075531, -0.9688690900802612, -2.1693856716156006, 0.5783095359802246, -0.7726922035217285, 1.8914519548416138], "g": [0.3400000035762787, -0.003832787275314331, -0.0174635648727417, 0.04487205296754837, 0.707093358039856, 0.7071201801300049, 2.79840733128367e-05, 1.1598692253755871e-05], "obj": [0.18906664848327637, -0.33527377247810364, 0.09999999403953552, -5.4569695116801764e-12, 1.0231817129668919e-11, -3.725291151113197e-07, 1.0], "dxdy": [-0.10000000000000003, -0.01999999999999999]}, {"base": [-0.11999999731779099, -0.10000000149011612, 0.20000000298023224], "q": [-1.2479524612426758, -0.4223668575286865, -1.0182286500930786, -2.1919007301330566, 0.5208694934844971, -0.7859079241752625, 1.8992466926574707], "g": [0.14000000059604645, -0.02065834403038025, -0.016971543431282043, 0.05861392617225647, 0.708770215511322, 0.7054359912872314, -0.0015769557794556022, -0.0015314879128709435], "obj": [0.18906664848327637, -0.33527377247810364, 0.09999999403953552, -1.0913936421275139e-11, 1.3642420526593924e-11, -3.4272852644789964e-07, 1.0], "dxdy": [-0.10000000000000003, 1.3877787807814457e-17]}]
\ No newline at end of file
diff --git a/calib_3_-0.5_0.05_-0.2_0.25.json b/calib_3_-0.5_0.05_-0.2_0.25.json
new file mode 100644
index 0000000..56b2b79
--- /dev/null
+++ b/calib_3_-0.5_0.05_-0.2_0.25.json
@@ -0,0 +1 @@
           1 +[{"base": [-0.11999999731779099, 0.05000000074505806, -0.20000000298023224], "q": [-0.12861165404319763, 0.020374825224280357, -2.6393890380859375, -2.6600000858306885, -0.024219142273068428, -0.413688600063324, 1.6664636135101318], "g": [0.41999998688697815, -0.009250231087207794, 0.024416297674179077, 0.03321433067321777, 0.859673798084259, 0.5102279186248779, 0.011140472255647182, -0.022459935396909714], "obj": [0.15941956639289856, -0.0823003500699997, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0], "dxdy": [-0.16, 0.060000000000000026]}, {"base": [-0.11999999731779099, 0.05000000074505806, -0.20000000298023224], "q": [-0.2029654085636139, 0.028011083602905273, -2.3497068881988525, -2.5068507194519043, -0.11987366527318954, -0.6379237174987793, 1.9781049489974976], "g": [0.12999999523162842, 0.01214916817843914, 0.0035438090562820435, 0.056987836956977844, 0.854278028011322, 0.5190917253494263, 0.02269342727959156, 0.015425678342580795], "obj": [0.15941958129405975, -0.08230039477348328, 0.1000000387430191, 4.190951585769653e-09, 5.587935447692871e-09, -1.0445364750921726e-07, 1.0], "dxdy": [-0.14, 1.3877787807814457e-17]}, {"base": [-0.11999999731779099, 0.05000000074505806, -0.20000000298023224], "q": [-0.21342885494232178, 0.12381333112716675, -2.3542420864105225, -2.6168885231018066, -0.20446878671646118, -0.44522395730018616, 2.0258758068084717], "g": [0.1899999976158142, 0.014121659100055695, 0.017922744154930115, 0.02486450970172882, 0.8600679636001587, 0.5101794600486755, -2.5469018510193564e-05, -7.602276127727237e-06], "obj": [0.15941961109638214, -0.08230043202638626, 0.10000007599592209, 5.587935447692871e-09, 7.916241884231567e-09, -1.1164229363203049e-07, 1.0], "dxdy": [-0.14, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.05000000074505806, -0.20000000298023224], "q": [-0.36906853318214417, 0.09666415303945541, -2.2961928844451904, -2.648653507232666, -0.1723477840423584, -0.43435952067375183, 1.9014118909835815], "g": [0.5799999833106995, -0.0034264493733644485, 0.027513056993484497, 0.0248631089925766, 0.8600675463676453, 0.5101801156997681, -2.0421144654392265e-05, -1.0278860827384051e-05], "obj": [0.15941961109638214, -0.08230043202638626, 0.10000006854534149, 5.588844942394644e-09, 7.914422894828022e-09, -1.3411070654001378e-07, 1.0], "dxdy": [-0.14, 0.04000000000000002]}, {"base": [-0.11999999731779099, 0.05000000074505806, -0.20000000298023224], "q": [-0.5239541530609131, 0.06972035020589828, -2.25636887550354, -2.6600000858306885, -0.13096974790096283, -0.4253367483615875, 1.7502824068069458], "g": [0.3400000035762787, -0.020556015893816948, 0.0279247909784317, 0.027338072657585144, 0.8598318696022034, 0.5105202198028564, 0.0034777196124196053, -0.006797380745410919], "obj": [0.15941962599754333, -0.08230042457580566, 0.10000006854534149, 5.588844942394644e-09, 7.917606126284227e-09, -6.705544564056254e-08, 1.0], "dxdy": [-0.14, 0.060000000000000026]}, {"base": [-0.11999999731779099, 0.05000000074505806, -0.20000000298023224], "q": [-0.6938022971153259, 0.33990687131881714, -1.7217671871185303, -2.583914041519165, -0.6254562735557556, -0.5979693531990051, 2.5259177684783936], "g": [0.23999999463558197, 0.0045419298112392426, 0.00036190450191497803, 0.024827465415000916, 0.8600656390190125, 0.5101833343505859, -5.978170520393178e-06, 8.053615374592482e-07], "obj": [0.15941961109638214, -0.08230041712522507, 0.10000006854534149, 7.450582373280668e-09, 9.313227522511625e-09, -6.705160160436208e-08, 1.0], "dxdy": [-0.12000000000000002, 0.020000000000000018]}, {"base": [-0.11999999731779099, 0.05000000074505806, -0.20000000298023224], "q": [-0.8137378096580505, 0.2976725399494171, -1.7094122171401978, -2.6125223636627197, -0.5756947994232178, -0.5627897381782532, 2.3849687576293945], "g": [0.07000000029802322, -0.013009211979806423, 0.009952425956726074, 0.02483207732439041, 0.860065758228302, 0.5101832747459412, -5.739118932979181e-06, -9.626014616515022e-07], "obj": [0.15941962599754333, -0.08230043202638626, 0.10000006854534149, 7.45001216273522e-09, 9.313453119830228e-09, -1.5646224937881925e-07, 1.0], "dxdy": [-0.12000000000000002, 0.04000000000000002]}, {"base": [-0.11999999731779099, 0.05000000074505806, -0.20000000298023224], "q": [-0.45305153727531433, 0.2973525822162628, -2.0360183715820312, -2.5051708221435547, -0.5151085257530212, -0.5603735446929932, 2.352200508117676], "g": [0.41999998688697815, 0.012503888458013535, -0.02677832543849945, 0.024831622838974, 0.8600662350654602, 0.5101823806762695, -1.0265322998748161e-05, 6.790176598769904e-07], "obj": [0.15941961109638214, -0.08230043202638626, 0.10000006854534149, 7.449216354871169e-09, 9.314362614532001e-09, -1.937151523634384e-07, 1.0], "dxdy": [-0.10000000000000003, 1.3877787807814457e-17]}]
\ No newline at end of file
diff --git a/common.py b/common.py
new file mode 100644
index 0000000..c78ef35
--- /dev/null
+++ b/common.py
@@ -0,0 +1,22 @@
           1 +import numpy as np, kin
           2 +JN = [f'joint_{i}' for i in range(1,8)]
           3 +def robot(obs): return obs.get_object_from_name('robot')
           4 +def getq(obs):
           5 +    R = robot(obs); return np.array([obs.get(R,f) for f in JN])
           6 +def getbase(obs):
           7 +    R = robot(obs); return np.array([obs.get(R,f) for f in ['pos_base_x','pos_base_y','pos_base_rot']])
           8 +def objd(obs, n):
           9 +    o = obs.get_object_from_name(n)
          10 +    return {f: obs.get(o,f) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z','grasp_active','pose_qx','pose_qy','pose_qz','pose_qw']}
          11 +def move_to(env, obs, qt, grip=0.0, maxd=0.2):
          12 +    """step joints toward qt; returns obs, blocked flag"""
          13 +    while True:
          14 +        q = getq(obs)
          15 +        d = np.array(qt) - q
          16 +        d = (d + np.pi) % (2*np.pi) - np.pi
          17 +        if np.max(np.abs(d)) < 1e-6: return obs, False
          18 +        s = max(1.0, np.max(np.abs(d))/maxd)
          19 +        a = np.zeros(11, dtype=np.float32); a[3:10] = d/s; a[10]=grip
          20 +        obs, r, t, tr, info = env.step(a)
          21 +        if np.max(np.abs(getq(obs)-q)) < 1e-7: return obs, True
          22 +        if t: return obs, False
diff --git a/dbg/approach.py b/dbg/approach.py
new file mode 100644
index 0000000..6d553df
--- /dev/null
+++ b/dbg/approach.py
@@ -0,0 +1,26 @@
           1 +import numpy as np
           2 +import kin
           3 +JN = [f'joint_{i}' for i in range(1,8)]
           4 +class GeneratedApproach:
           5 +    def __init__(self, action_space, observation_space, primitives): pass
           6 +    def reset(self, state, info):
           7 +        R = state.get_object_from_name('robot'); self.R=R
           8 +        b = state.get_object_from_name('target_block')
           9 +        self.base = np.array([state.get(R,f) for f in ['pos_base_x','pos_base_y','pos_base_rot']])
          10 +        q = np.array([state.get(R,f) for f in JN])
          11 +        bx, by = state.get(b,'pose_x'), state.get(b,'pose_y')
          12 +        self.targets=[]
          13 +        for z in [0.35, 0.3, 0.26, 0.235]:
          14 +            q,_ = kin.ik(self.base, q, np.array([bx,by,z]), kin.topdown_R(0)); self.targets.append(q)
          15 +        self.t=0
          16 +    def get_action(self, state):
          17 +        q = np.array([state.get(self.R,f) for f in JN])
          18 +        a = np.zeros(11, dtype=np.float32)
          19 +        while self.targets:
          20 +            d = self.targets[0]-q
          21 +            if np.max(np.abs(d))<1e-5: self.targets.pop(0); continue
          22 +            a[3:10] = np.clip(d,-0.2,0.2); return a
          23 +        self.t+=1
          24 +        a[10] = -1 if self.t<5 else 0
          25 +        if self.t>=5: a[5]=0.0; a[4]=-0.05
          26 +        return a
diff --git a/dbg/kin.py b/dbg/kin.py
new file mode 100644
index 0000000..58cb33a
--- /dev/null
+++ b/dbg/kin.py
@@ -0,0 +1,78 @@
           1 +import numpy as np
           2 +
           3 +def rpy_mat(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def tf(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = rpy_mat(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +def rotz(q):
          13 +    c, s = np.cos(q), np.sin(q)
          14 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          15 +
          16 +PI = np.pi
          17 +JOINTS = [
          18 +    tf([0, 0, 0.15643], [PI, 0, 0]),
          19 +    tf([0, 0.005375, -0.12838], [PI/2, 0, 0]),
          20 +    tf([0, -0.21038, -0.006375], [-PI/2, 0, 0]),
          21 +    tf([0, 0.006375, -0.21038], [PI/2, 0, 0]),
          22 +    tf([0, -0.20843, -0.006375], [-PI/2, 0, 0]),
          23 +    tf([0, 0.00017505, -0.10593], [PI/2, 0, 0]),
          24 +    tf([0, -0.10593, -0.00017505], [-PI/2, 0, 0]),
          25 +]
          26 +EE = tf([0, 0, -0.061525], [PI, 0, 0])
          27 +BASE_Z = 0.0
          28 +TOOL = 0.0
          29 +
          30 +def fk(base, q, tool=None, base_z=None):
          31 +    tool = TOOL if tool is None else tool
          32 +    base_z = BASE_Z if base_z is None else base_z
          33 +    T = np.eye(4)
          34 +    T[:3, :3] = rpy_mat(0, 0, base[2]); T[:3, 3] = [base[0], base[1], base_z]
          35 +    for J, qi in zip(JOINTS, q):
          36 +        T = T @ J @ rotz(qi)
          37 +    T = T @ EE
          38 +    Tt = np.eye(4); Tt[2, 3] = tool
          39 +    return T @ Tt
          40 +
          41 +def rot_err(Rc, Rt):
          42 +    Re = Rt @ Rc.T
          43 +    # axis-angle vector
          44 +    ang = np.arccos(np.clip((np.trace(Re) - 1) / 2, -1, 1))
          45 +    if ang < 1e-9:
          46 +        return np.zeros(3)
          47 +    v = np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          48 +    s = np.sin(ang)
          49 +    if s < 1e-6:
          50 +        # near pi
          51 +        w = np.sqrt(np.maximum((np.diag(Re) + 1) / 2, 0))
          52 +        return w * ang
          53 +    return v / (2 * s) * ang
          54 +
          55 +def topdown_R(yaw):
          56 +    c, s = np.cos(yaw), np.sin(yaw)
          57 +    Rz = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
          58 +    return Rz @ np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1.0]])
          59 +
          60 +def ik(base, q0, p, R, iters=200, tol=1e-4, wrot=0.5, tool=None, base_z=None):
          61 +    q = np.array(q0, dtype=float)
          62 +    for it in range(iters):
          63 +        T = fk(base, q, tool, base_z)
          64 +        e = np.concatenate([p - T[:3, 3], wrot * rot_err(T[:3, :3], R)])
          65 +        if np.linalg.norm(e) < tol:
          66 +            return q, True
          67 +        J = np.zeros((6, 7))
          68 +        for i in range(7):
          69 +            dq = q.copy(); dq[i] += 1e-5
          70 +            Td = fk(base, dq, tool, base_z)
          71 +            J[:3, i] = (Td[:3, 3] - T[:3, 3]) / 1e-5
          72 +            J[3:, i] = wrot * rot_err(T[:3, :3], Td[:3, :3]) / 1e-5
          73 +        lam = 1e-3
          74 +        dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
          75 +        n = np.linalg.norm(dq)
          76 +        if n > 0.3: dq *= 0.3 / n
          77 +        q += dq
          78 +    return q, False
diff --git a/explore1.py b/explore1.py
new file mode 100644
index 0000000..59d0671
--- /dev/null
+++ b/explore1.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +print(type(obs), info)
           6 +for n in sorted(obs.get_object_names()):
           7 +    o = obs.get_object_from_name(n)
           8 +    print(n, o.type.name if hasattr(o,'type') else '', )
           9 +for t in ['Kinematic3DCuboid','Kinematic3DRobot','Kinematic3DFixture','Kinematic3DPoint']:
          10 +    try:
          11 +        ty = env.observation_space.get_type(t)
          12 +    except Exception as e:
          13 +        print(t, e); continue
          14 +    for o in obs.get_objects(ty):
          15 +        feats = env.observation_space.type_features[ty] if hasattr(env.observation_space,'type_features') else None
          16 +        print(o.name, {f: round(float(obs.get(o,f)),4) for f in feats})
          17 +print(env.max_steps)
diff --git a/explore2.py b/explore2.py
new file mode 100644
index 0000000..c51b326
--- /dev/null
+++ b/explore2.py
@@ -0,0 +1,16 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +R = obs.get_object_from_name('robot')
           6 +F = ['pos_base_x','pos_base_y','pos_base_rot']+[f'joint_{i}' for i in range(1,8)]+['finger_state','grasp_active']
           7 +def rs(o): return np.array([o.get(R,f) for f in F])
           8 +prev = rs(obs)
           9 +for k,a in enumerate([np.eye(11)[i]*0.1 for i in range(10)] + [np.eye(11)[i]*0.3 for i in range(10)]):
          10 +    a[10]=0
          11 +    obs,r,t,tr,info = env.step(a.astype(np.float32))
          12 +    cur = rs(obs); print(k, r, t, np.round(cur-prev,4)); prev=cur
          13 +a=np.zeros(11,dtype=np.float32); a[10]=-1
          14 +obs,r,t,tr,info = env.step(a); print('close', np.round(rs(obs),3))
          15 +a[10]=1
          16 +obs,r,t,tr,info = env.step(a); print('open', np.round(rs(obs),3))
diff --git a/explore3.py b/explore3.py
new file mode 100644
index 0000000..b686729
--- /dev/null
+++ b/explore3.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +R = obs.get_object_from_name('robot')
           6 +F = ['pos_base_x','pos_base_y','pos_base_rot']+[f'joint_{i}' for i in range(1,8)]+['finger_state','grasp_active']
           7 +def rs(o): return np.round(np.array([o.get(R,f) for f in F]),3)
           8 +for g in [-1,-1,-1,0,1,1,1]:
           9 +    a=np.zeros(11,dtype=np.float32); a[10]=g
          10 +    obs,*_ = env.step(a); print(g, rs(obs)[-2:])
          11 +for dx in [-0.1,-0.1,0.05,0.05,0.05,0.05]:
          12 +    a=np.zeros(11,dtype=np.float32); a[0]=dx
          13 +    obs,*_ = env.step(a); print(dx, rs(obs)[:3])
diff --git a/fit.py b/fit.py
new file mode 100644
index 0000000..9f33ada
--- /dev/null
+++ b/fit.py
@@ -0,0 +1,30 @@
           1 +import json, glob, numpy as np, kin
           2 +from scipy.optimize import least_squares
           3 +def qmat(x,y,z,w):
           4 +    return np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],[2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],[2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]])
           5 +D=[]
           6 +for f in glob.glob('calib_*.json'): D+=json.load(open(f))
           7 +print(len(D))
           8 +def Tof(p,q):
           9 +    T=np.eye(4); T[:3,:3]=qmat(*q); T[:3,3]=p; return T
          10 +def pred(params, d, inv):
          11 +    ox,oy,oz,tx,ty,tz = params
          12 +    b=d['base']
          13 +    Tb=np.eye(4); Tb[:3,:3]=kin.rpy_mat(0,0,b[2]); Tb[:3,3]=[b[0],b[1],0]
          14 +    M=np.eye(4); M[:3,3]=[ox,oy,oz]
          15 +    T=M.copy()
          16 +    for J,qi in zip(kin.JOINTS,d['q']): T=T@J@kin.rotz(qi)
          17 +    T=T@kin.EE; Tt=np.eye(4); Tt[:3,3]=[tx,ty,tz]; T=Tb@T@Tt
          18 +    G=Tof(d['g'][1:4],d['g'][4:8])
          19 +    if inv: G=np.linalg.inv(G)
          20 +    return T@G
          21 +for inv in [False,True]:
          22 +    def res(p):
          23 +        r=[]
          24 +        for d in D:
          25 +            P=pred(p,d,inv); O=Tof(d['obj'][:3],d['obj'][3:])
          26 +            r+=list(P[:3,3]-O[:3,3]); r+=list(0.05*(P[:3,:3]-O[:3,:3]).ravel())
          27 +        return np.array(r)
          28 +    s=least_squares(res,np.zeros(6))
          29 +    r=res(s.x).reshape(len(D),-1)
          30 +    print(inv, np.round(s.x,4), 'pos rms', np.sqrt(np.mean(r[:,:3]**2)), 'rot', np.sqrt(np.mean(r[:,3:]**2))/0.05)
diff --git a/kin.py b/kin.py
new file mode 100644
index 0000000..c2d8575
--- /dev/null
+++ b/kin.py
@@ -0,0 +1,80 @@
           1 +import numpy as np
           2 +
           3 +def rpy_mat(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def tf(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = rpy_mat(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +def rotz(q):
          13 +    c, s = np.cos(q), np.sin(q)
          14 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          15 +
          16 +PI = np.pi
          17 +JOINTS = [
          18 +    tf([0, 0, 0.15643], [PI, 0, 0]),
          19 +    tf([0, 0.005375, -0.12838], [PI/2, 0, 0]),
          20 +    tf([0, -0.21038, -0.006375], [-PI/2, 0, 0]),
          21 +    tf([0, 0.006375, -0.21038], [PI/2, 0, 0]),
          22 +    tf([0, -0.20843, -0.006375], [-PI/2, 0, 0]),
          23 +    tf([0, 0.00017505, -0.10593], [PI/2, 0, 0]),
          24 +    tf([0, -0.10593, -0.00017505], [-PI/2, 0, 0]),
          25 +]
          26 +EE = tf([0, 0, -0.061525], [PI, 0, 0])
          27 +BASE_Z = -0.0052
          28 +TOOL = 0.12
          29 +MOUNT_X = 0.12
          30 +
          31 +def fk(base, q, tool=None, base_z=None):
          32 +    tool = TOOL if tool is None else tool
          33 +    base_z = BASE_Z if base_z is None else base_z
          34 +    T = np.eye(4)
          35 +    T[:3, :3] = rpy_mat(0, 0, base[2]); T[:3, 3] = [base[0], base[1], base_z]
          36 +    M = np.eye(4); M[0, 3] = MOUNT_X; T = T @ M
          37 +    for J, qi in zip(JOINTS, q):
          38 +        T = T @ J @ rotz(qi)
          39 +    T = T @ EE
          40 +    Tt = np.eye(4); Tt[2, 3] = tool
          41 +    return T @ Tt
          42 +
          43 +def rot_err(Rc, Rt):
          44 +    Re = Rt @ Rc.T
          45 +    # axis-angle vector
          46 +    ang = np.arccos(np.clip((np.trace(Re) - 1) / 2, -1, 1))
          47 +    if ang < 1e-9:
          48 +        return np.zeros(3)
          49 +    v = np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          50 +    s = np.sin(ang)
          51 +    if s < 1e-6:
          52 +        # near pi
          53 +        w = np.sqrt(np.maximum((np.diag(Re) + 1) / 2, 0))
          54 +        return w * ang
          55 +    return v / (2 * s) * ang
          56 +
          57 +def topdown_R(yaw):
          58 +    c, s = np.cos(yaw), np.sin(yaw)
          59 +    Rz = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
          60 +    return Rz @ np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1.0]])
          61 +
          62 +def ik(base, q0, p, R, iters=200, tol=1e-4, wrot=0.5, tool=None, base_z=None):
          63 +    q = np.array(q0, dtype=float)
          64 +    for it in range(iters):
          65 +        T = fk(base, q, tool, base_z)
          66 +        e = np.concatenate([p - T[:3, 3], wrot * rot_err(T[:3, :3], R)])
          67 +        if np.linalg.norm(e) < tol:
          68 +            return q, True
          69 +        J = np.zeros((6, 7))
          70 +        for i in range(7):
          71 +            dq = q.copy(); dq[i] += 1e-5
          72 +            Td = fk(base, dq, tool, base_z)
          73 +            J[:3, i] = (Td[:3, 3] - T[:3, 3]) / 1e-5
          74 +            J[3:, i] = wrot * rot_err(T[:3, :3], Td[:3, :3]) / 1e-5
          75 +        lam = 1e-3
          76 +        dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
          77 +        n = np.linalg.norm(dq)
          78 +        if n > 0.3: dq *= 0.3 / n
          79 +        q += dq
          80 +    return q, False
```

</details>

<a id="C003"></a>
### C003 · First full approach: clear obstructions then place block

Commit `cb6f0b40eff5895390fe83fdaa4722e6a05ffcf9`; parents: 7c86a54d1d334524b83e177a079dbc99a4c8b2a4. Recorded author date: 2026-09-30T20:36:03+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0104](01_timeline.md#E0104): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_cb6f0b4_approach.py) · [Exact all-file diff](evidence/diffs/C003_cb6f0b4.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..690a83c
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,363 @@
           1 +"""Obstruction3D approach: clear obstructions from target region, then place target block.
           2 +
           3 +Kinematics: Kinova Gen3 URDF chain, calibrated empirically (see kin.py):
           4 +  arm mount = base pose + 0.12 m along base x, z=-0.0052; tool point 0.12 m along flange z.
           5 +grasp_tf = object pose expressed in tool frame (T_obj = T_tool @ G).
           6 +"""
           7 +import numpy as np
           8 +import kin
           9 +
          10 +JN = [f'joint_{i}' for i in range(1, 8)]
          11 +TABLE_TOP = 0.075
          12 +Z_SAFE = 0.26          # tool z for transit
          13 +FINGER_DEPTH = 0.03    # tool point to fingertip bottom
          14 +JLIM = np.array([np.inf, 2.41, np.inf, 2.66, np.inf, 2.23, np.inf])
          15 +TABLE_X = (0.12, 0.47)
          16 +TABLE_Y = (-0.37, 0.37)
          17 +
          18 +
          19 +def quat_mat(x, y, z, w):
          20 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          21 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          22 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          23 +
          24 +
          25 +def wrap(a):
          26 +    return (a + np.pi) % (2 * np.pi) - np.pi
          27 +
          28 +
          29 +class Obj:
          30 +    def __init__(self, state, o):
          31 +        g = lambda f: float(state.get(o, f))
          32 +        self.name = o.name
          33 +        self.p = np.array([g('pose_x'), g('pose_y'), g('pose_z')])
          34 +        self.h = np.array([g('half_extent_x'), g('half_extent_y'), g('half_extent_z')])
          35 +        self.q = np.array([g('pose_qx'), g('pose_qy'), g('pose_qz'), g('pose_qw')])
          36 +        self.R = quat_mat(*self.q)
          37 +        self.yaw = np.arctan2(self.R[1, 0], self.R[0, 0])
          38 +
          39 +    def footprint(self):
          40 +        # axis aligned half extents in world (accounting for yaw)
          41 +        c, s = abs(np.cos(self.yaw)), abs(np.sin(self.yaw))
          42 +        return np.array([c * self.h[0] + s * self.h[1], s * self.h[0] + c * self.h[1]])
          43 +
          44 +
          45 +def overlap(pa, ha, pb, hb, margin=0.0):
          46 +    return (abs(pa[0] - pb[0]) < ha[0] + hb[0] + margin) and (abs(pa[1] - pb[1]) < ha[1] + hb[1] + margin)
          47 +
          48 +
          49 +class GeneratedApproach:
          50 +    def __init__(self, action_space, observation_space, primitives):
          51 +        self.action_space = action_space
          52 +        self.observation_space = observation_space
          53 +
          54 +    # ------------------------------------------------------------------ utils
          55 +    def _parse(self, state):
          56 +        self.robot = state.get_object_from_name('robot')
          57 +        objs = {}
          58 +        for n in state.get_object_names():
          59 +            if n == 'robot':
          60 +                continue
          61 +            o = state.get_object_from_name(n)
          62 +            try:
          63 +                objs[n] = Obj(state, o)
          64 +            except Exception:
          65 +                pass
          66 +        return objs
          67 +
          68 +    def _q(self, state):
          69 +        return np.array([float(state.get(self.robot, f)) for f in JN])
          70 +
          71 +    def _base(self, state):
          72 +        return np.array([float(state.get(self.robot, f)) for f in ['pos_base_x', 'pos_base_y', 'pos_base_rot']])
          73 +
          74 +    def _G(self, state):
          75 +        g = [float(state.get(self.robot, f)) for f in
          76 +             ['grasp_tf_x', 'grasp_tf_y', 'grasp_tf_z', 'grasp_tf_qx', 'grasp_tf_qy', 'grasp_tf_qz', 'grasp_tf_qw']]
          77 +        G = np.eye(4)
          78 +        G[:3, :3] = quat_mat(*g[3:])
          79 +        G[:3, 3] = g[:3]
          80 +        return G
          81 +
          82 +    def _ik(self, q0, p, R):
          83 +        best = None
          84 +        for attempt in range(3):
          85 +            qs = np.array(q0, dtype=float)
          86 +            if attempt > 0:
          87 +                qs = qs + np.random.uniform(-0.3, 0.3, 7)
          88 +            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=150, tol=1e-5)
          89 +            q = np.clip(q, -JLIM, JLIM)
          90 +            if ok:
          91 +                return q, True
          92 +            if best is None:
          93 +                best = q
          94 +        return best, False
          95 +
          96 +    def _cart_path(self, q0, p_from, p_to, R, step=0.04):
          97 +        """IK waypoints along a straight line in tool position with fixed orientation R."""
          98 +        d = np.linalg.norm(np.asarray(p_to) - np.asarray(p_from))
          99 +        n = max(1, int(np.ceil(d / step)))
         100 +        qs = []
         101 +        q = np.array(q0, float)
         102 +        for i in range(1, n + 1):
         103 +            p = p_from + (p_to - p_from) * i / n
         104 +            q, ok = self._ik(q, p, R)
         105 +            qs.append(q.copy())
         106 +        return qs, q
         107 +
         108 +    def _tool(self, q):
         109 +        return kin.fk(self.base, q)
         110 +
         111 +    # --------------------------------------------------------------- planning
         112 +    def reset(self, state, info):
         113 +        self.objs = self._parse(state)
         114 +        self.base = self._base(state)
         115 +        self.plan = []          # list of ('move', q) / ('grip', val) / ('check', kind)
         116 +        self.phase = 'init'
         117 +        self.task_queue = None
         118 +        self.blocked = 0
         119 +        self.fail_count = {}
         120 +        self.moved_spots = []
         121 +        self.steps = 0
         122 +
         123 +    def _obstacles_to_clear(self, objs):
         124 +        reg = objs['target_region']
         125 +        tb = objs['target_block']
         126 +        res = []
         127 +        for n, o in objs.items():
         128 +            if not n.startswith('obstruction'):
         129 +                continue
         130 +            # anything touching the region footprint (plus finger margin) must go
         131 +            if overlap(o.p, o.footprint(), reg.p, reg.footprint(), 0.045):
         132 +                res.append(n)
         133 +        return res
         134 +
         135 +    def _grasp_yaws(self, o, objs):
         136 +        """candidate tool yaws for grasping object o; fingers close along tool x = world (-sin, cos)."""
         137 +        cands = []
         138 +        for k in range(2):
         139 +            yaw = o.yaw + k * np.pi / 2
         140 +            # closing along world dir (-sin yaw, cos yaw); object width along that dir
         141 +            d = np.array([-np.sin(yaw), np.cos(yaw)])
         142 +            width = abs(d @ o.R[:2, 0]) * o.h[0] + abs(d @ o.R[:2, 1]) * o.h[1]
         143 +            if width > 0.041:
         144 +                continue
         145 +            # clearance: nearest other object along closing dir within finger span
         146 +            clr = 1.0
         147 +            perp = np.array([d[1], -d[0]])
         148 +            for n, b in objs.items():
         149 +                if n == o.name or n == 'target_region':
         150 +                    continue
         151 +                rel = b.p[:2] - o.p[:2]
         152 +                fp = b.footprint()
         153 +                along = abs(rel @ d) - (abs(d[0]) * fp[0] + abs(d[1]) * fp[1])
         154 +                across = abs(rel @ perp) - (abs(perp[0]) * fp[0] + abs(perp[1]) * fp[1])
         155 +                if across < 0.02 + (abs(perp @ o.R[:2, 0]) * o.h[0] + abs(perp @ o.R[:2, 1]) * o.h[1]):
         156 +                    clr = min(clr, along)
         157 +            cands.append((clr - width * 0.0, yaw, width))
         158 +        cands.sort(key=lambda c: -c[0])
         159 +        return cands
         160 +
         161 +    def _support_top(self, o, objs):
         162 +        top = TABLE_TOP
         163 +        for n, b in objs.items():
         164 +            if n == o.name:
         165 +                continue
         166 +            btop = b.p[2] + b.h[2]
         167 +            if btop <= o.p[2] - o.h[2] + 1e-3 and overlap(o.p, o.footprint(), b.p, b.footprint()):
         168 +                top = max(top, btop)
         169 +        return top
         170 +
         171 +    def _free_spot(self, o, objs, avoid_names=()):
         172 +        """find a table location for object o not overlapping anything."""
         173 +        fp = o.footprint()
         174 +        reg = objs['target_region']
         175 +        tb = objs['target_block']
         176 +        best = None
         177 +        for x in np.arange(TABLE_X[0] + fp[0], TABLE_X[1] - fp[0], 0.02):
         178 +            for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
         179 +                p = np.array([x, y])
         180 +                ok = True
         181 +                for n, b in objs.items():
         182 +                    if n == o.name:
         183 +                        continue
         184 +                    m = 0.06
         185 +                    if n == 'target_region':
         186 +                        m = 0.09
         187 +                    if overlap(p, fp, b.p, b.footprint(), m):
         188 +                        ok = False
         189 +                        break
         190 +                if not ok:
         191 +                    continue
         192 +                for sp, sh in self.moved_spots:
         193 +                    if overlap(p, fp, sp, sh, 0.06):
         194 +                        ok = False
         195 +                        break
         196 +                if not ok:
         197 +                    continue
         198 +                cost = np.linalg.norm(p - o.p[:2]) + 0.3 * abs(y - self.base[1]) * 0
         199 +                if best is None or cost < best[0]:
         200 +                    best = (cost, p)
         201 +        if best is None:
         202 +            return None
         203 +        return best[1]
         204 +
         205 +    def _plan_pick(self, state, name):
         206 +        objs = self._parse(state)
         207 +        o = objs[name]
         208 +        q = self._q(state)
         209 +        T = self._tool(q)
         210 +        cands = self._grasp_yaws(o, objs)
         211 +        nf = self.fail_count.get(name, 0)
         212 +        if not cands:
         213 +            cands = [(0, o.yaw, 0)]
         214 +        _, yaw, _ = cands[nf % len(cands)]
         215 +        # choose yaw or yaw+pi, closest to current wrist
         216 +        best = None
         217 +        for y in [yaw, yaw + np.pi]:
         218 +            R = kin.topdown_R(y)
         219 +            qa, ok = self._ik(q, np.array([o.p[0], o.p[1], Z_SAFE]), R)
         220 +            c = np.sum(np.abs(wrap(qa - q))) + (0 if ok else 100)
         221 +            if best is None or c < best[0]:
         222 +                best = (c, y, R)
         223 +        _, yaw, R = best
         224 +        sup = self._support_top(o, objs)
         225 +        zg = o.p[2] + min(max(o.h[2] - 0.004, 0.018), 0.045)
         226 +        zg = max(zg, sup + FINGER_DEPTH + 0.003)
         227 +        p0 = T[:3, 3]
         228 +        above = np.array([o.p[0], o.p[1], Z_SAFE])
         229 +        start = np.array([p0[0], p0[1], max(p0[2], Z_SAFE)])
         230 +        plan = []
         231 +        qs, qe = self._cart_path(q, p0, start, T[:3, :3] if p0[2] < Z_SAFE - 0.01 else R)
         232 +        plan += [('move', x) for x in qs]
         233 +        qs, qe = self._cart_path(qe, start, above, R, step=0.08)
         234 +        plan += [('move', x) for x in qs]
         235 +        qs, qe = self._cart_path(qe, above, np.array([o.p[0], o.p[1], zg]), R, step=0.05)
         236 +        plan += [('move', x) for x in qs]
         237 +        plan += [('grip', -1.0), ('check', 'grasp')]
         238 +        self.plan = plan
         239 +
         240 +    def _plan_place(self, state, name, xy, support_top, yaw_obj):
         241 +        objs = self._parse(state)
         242 +        o = objs[name]
         243 +        q = self._q(state)
         244 +        T = self._tool(q)
         245 +        G = self._G(state)
         246 +        Ginv = np.linalg.inv(G)
         247 +        best = None
         248 +        for yo in [yaw_obj, yaw_obj + np.pi]:
         249 +            To = np.eye(4)
         250 +            c, s = np.cos(yo), np.sin(yo)
         251 +            To[:3, :3] = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
         252 +            To[:3, 3] = [xy[0], xy[1], support_top + o.h[2] + 0.0015]
         253 +            Tt = To @ Ginv
         254 +            qa, ok = self._ik(q, Tt[:3, 3] + np.array([0, 0, Z_SAFE - Tt[2, 3]]), Tt[:3, :3])
         255 +            cst = np.sum(np.abs(wrap(qa - q))) + (0 if ok else 100)
         256 +            if best is None or cst < best[0]:
         257 +                best = (cst, Tt)
         258 +        Tt = best[1]
         259 +        R = Tt[:3, :3]
         260 +        p0 = T[:3, 3]
         261 +        # lift height: object bottom above everything
         262 +        maxtop = max([b.p[2] + b.h[2] for n, b in objs.items() if n != name] + [TABLE_TOP])
         263 +        obj_below_tool = (T @ G)[2, 3] - o.h[2]  # object bottom z
         264 +        lift_z = max(Z_SAFE, p0[2] + (maxtop + 0.03 - obj_below_tool))
         265 +        up = np.array([p0[0], p0[1], lift_z])
         266 +        above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
         267 +        plan = []
         268 +        qs, qe = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
         269 +        plan += [('move', x) for x in qs]
         270 +        qs, qe = self._cart_path(qe, up, above, R, step=0.08)
         271 +        plan += [('move', x) for x in qs]
         272 +        qs, qe = self._cart_path(qe, above, Tt[:3, 3], R, step=0.05)
         273 +        plan += [('move', x) for x in qs]
         274 +        plan += [('grip', 1.0), ('check', 'release')]
         275 +        # retreat up
         276 +        qs, qe = self._cart_path(qe, Tt[:3, 3], np.array([Tt[0, 3], Tt[1, 3], Z_SAFE]), R, step=0.06)
         277 +        plan += [('move', x) for x in qs]
         278 +        self.plan = plan
         279 +
         280 +    def _next_task(self, state):
         281 +        objs = self._parse(state)
         282 +        grasped = float(state.get(self.robot, 'grasp_active')) > 0.5
         283 +        clear = self._obstacles_to_clear(objs)
         284 +        if grasped:
         285 +            # figure out which object is held
         286 +            held = None
         287 +            for n in objs:
         288 +                o = state.get_object_from_name(n)
         289 +                try:
         290 +                    if float(state.get(o, 'grasp_active')) > 0.5:
         291 +                        held = n
         292 +                except Exception:
         293 +                    pass
         294 +            if held is None:
         295 +                held = self.current
         296 +            if held == 'target_block' and not clear:
         297 +                reg = objs['target_region']
         298 +                self._plan_place(state, held, reg.p[:2], reg.p[2] + reg.h[2], reg.yaw)
         299 +            else:
         300 +                spot = self._free_spot(objs[held], objs)
         301 +                if spot is None:
         302 +                    spot = objs[held].p[:2]
         303 +                self.moved_spots.append((spot, objs[held].footprint()))
         304 +                self._plan_place(state, held, spot, TABLE_TOP, objs[held].yaw)
         305 +            self.current = held
         306 +            return
         307 +        if clear:
         308 +            # choose obstruction with best clearance, top-most first
         309 +            def key(n):
         310 +                o = objs[n]
         311 +                c = self._grasp_yaws(o, objs)
         312 +                return (-(o.p[2] + o.h[2]) if False else 0, -(c[0][0] if c else -1) + 0.05 * self.fail_count.get(n, 0))
         313 +            clear.sort(key=key)
         314 +            self.current = clear[0]
         315 +        else:
         316 +            self.current = 'target_block'
         317 +        self._plan_pick(state, self.current)
         318 +
         319 +    # ---------------------------------------------------------------- acting
         320 +    def get_action(self, state):
         321 +        self.steps += 1
         322 +        a = np.zeros(11, dtype=np.float32)
         323 +        q = self._q(state)
         324 +        for _ in range(50):
         325 +            if not self.plan:
         326 +                self._next_task(state)
         327 +                if not self.plan:
         328 +                    return a
         329 +            kind, val = self.plan[0]
         330 +            if kind == 'move':
         331 +                d = wrap(val - q)
         332 +                if np.max(np.abs(d)) < 1e-4:
         333 +                    self.plan.pop(0)
         334 +                    self.last_q = None
         335 +                    continue
         336 +                if getattr(self, 'last_q', None) is not None and np.max(np.abs(q - self.last_q)) < 1e-7:
         337 +                    self.blocked += 1
         338 +                else:
         339 +                    self.blocked = 0
         340 +                if self.blocked >= 2:
         341 +                    # blocked: skip this waypoint
         342 +                    self.blocked = 0
         343 +                    self.plan.pop(0)
         344 +                    self.last_q = None
         345 +                    continue
         346 +                self.last_q = q.copy()
         347 +                s = max(1.0, np.max(np.abs(d)) / 0.2)
         348 +                a[3:10] = d / s
         349 +                return a
         350 +            if kind == 'grip':
         351 +                self.plan.pop(0)
         352 +                a[10] = val
         353 +                return a
         354 +            if kind == 'check':
         355 +                self.plan.pop(0)
         356 +                g = float(state.get(self.robot, 'grasp_active')) > 0.5
         357 +                if val == 'grasp' and not g:
         358 +                    self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
         359 +                    self.plan = []
         360 +                elif val == 'release' and g:
         361 +                    self.plan = []
         362 +                continue
         363 +        return a
diff --git a/pp1.py b/pp1.py
new file mode 100644
index 0000000..0803087
--- /dev/null
+++ b/pp1.py
@@ -0,0 +1,27 @@
           1 +import sys
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from common import *
           5 +seed=int(sys.argv[1])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed)
           8 +base = getbase(obs)
           9 +def goto(p, yaw=0, grip=0):
          10 +    global obs
          11 +    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
          12 +    obs, bl = move_to(env, obs, qt, grip); return bl, ok
          13 +def pr(tag):
          14 +    b=objd(obs,'target_block'); R=robot(obs)
          15 +    print(tag, 'block', np.round([b['pose_x'],b['pose_y'],b['pose_z']],4), 'q', np.round([b['pose_qx'],b['pose_qy'],b['pose_qz'],b['pose_qw']],3), 'grasp', obs.get(R,'grasp_active'), 'fs', round(obs.get(R,'finger_state'),3))
          16 +for n in obs.get_object_names():
          17 +    if n!='robot': d=objd(obs,n); print(n, np.round([d['pose_x'],d['pose_y'],d['pose_z'],d['half_extent_x'],d['half_extent_y'],d['half_extent_z']],3), np.round([d['pose_qz'],d['pose_qw']],3))
          18 +b=objd(obs,'target_block'); r=objd(obs,'target_region')
          19 +print(goto([b['pose_x'],b['pose_y'],0.25]))
          20 +print(goto([b['pose_x'],b['pose_y'],b['pose_z']]))
          21 +pr('at')
          22 +a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a); pr('closed')
          23 +print(goto([b['pose_x'],b['pose_y'],0.25]))
          24 +pr('lifted')
          25 +a=np.zeros(11,dtype=np.float32); a[10]=1; obs,rew,term,*_=env.step(a); pr('released in air')
          26 +for i in range(3):
          27 +    obs,rew,term,*_=env.step(np.zeros(11,dtype=np.float32)); pr('after')
diff --git a/pp2.py b/pp2.py
new file mode 100644
index 0000000..e307fe1
--- /dev/null
+++ b/pp2.py
@@ -0,0 +1,19 @@
           1 +import sys
           2 +exec(open('pp1.py').read().split("b=objd(obs,'target_block'); r=")[0])
           3 +b=objd(obs,'target_block'); r=objd(obs,'target_region')
           4 +print(goto([b['pose_x'],b['pose_y'],0.25]))
           5 +for z in [0.14,0.13,0.12,0.11,0.105,0.1,0.095]:
           6 +    bl,ok=goto([b['pose_x'],b['pose_y'],z]); print(z,bl)
           7 +    if bl: break
           8 +R=robot(obs); print('fk tool z', kin.fk(base,getq(obs))[2,3])
           9 +a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a); pr('closed')
          10 +print([round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
          11 +print(goto([b['pose_x'],b['pose_y'],0.25])); pr('lifted')
          12 +tx,ty=0.30,0.0
          13 +print(goto([tx,ty,0.25])); pr('moved')
          14 +for z in np.arange(0.24,0.05,-0.005):
          15 +    bl,ok=goto([tx,ty,z])
          16 +    if bl: print('blocked',z); break
          17 +pr('lowered')
          18 +a=np.zeros(11,dtype=np.float32); a[10]=1; obs,rew,term,*_=env.step(a); pr('release')
          19 +print(goto([tx,ty,0.25])); pr('up')
diff --git a/pp3.py b/pp3.py
new file mode 100644
index 0000000..9de41f1
--- /dev/null
+++ b/pp3.py
@@ -0,0 +1,11 @@
           1 +import sys
           2 +exec(open('pp1.py').read().split("b=objd(obs,'target_block'); r=")[0])
           3 +b=objd(obs,'target_block')
           4 +R=robot(obs)
           5 +for z in np.arange(0.16,0.10,-0.005):
           6 +    goto([b['pose_x'],b['pose_y'],0.25]); bl,ok=goto([b['pose_x'],b['pose_y'],z])
           7 +    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
           8 +    print(round(z,3), bl, obs.get(R,'grasp_active'), round(obs.get(R,'finger_state'),3), [round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']])
           9 +    a[10]=1; obs,*_=env.step(a); 
          10 +    if obs.get(R,'grasp_active'): print('release failed at grasp height')
          11 +    b2=objd(obs,'target_block'); print('   block after', np.round([b2['pose_x'],b2['pose_y'],b2['pose_z']],4))
diff --git a/pp4.py b/pp4.py
new file mode 100644
index 0000000..dcce4b3
--- /dev/null
+++ b/pp4.py
@@ -0,0 +1,15 @@
           1 +import sys
           2 +exec(open('pp1.py').read().split("b=objd(obs,'target_block'); r=")[0])
           3 +b=objd(obs,'target_block')
           4 +R=robot(obs)
           5 +hz=b['half_extent_z']
           6 +goto([b['pose_x'],b['pose_y'],0.25]); goto([b['pose_x'],b['pose_y'],b['pose_z']+0.03])
           7 +a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a); print('grasp',obs.get(R,'grasp_active'))
           8 +tx,ty=0.30,0.0
           9 +goto([tx,ty,0.25])
          10 +for h in [0.04,0.02,0.01,0.005,0.002,0.0,-0.002]:
          11 +    bl,ok=goto([tx,ty,0.075+hz+h+0.03]); b2=objd(obs,'target_block')
          12 +    a=np.zeros(11,dtype=np.float32); a[10]=1; obs,*_=env.step(a)
          13 +    b3=objd(obs,'target_block')
          14 +    print(h, bl, 'held at', np.round([b2['pose_x'],b2['pose_y'],b2['pose_z']],4), 'after open grasp', obs.get(R,'grasp_active'), np.round([b3['pose_x'],b3['pose_y'],b3['pose_z']],4))
          15 +    if not obs.get(R,'grasp_active'): break
diff --git a/stats.py b/stats.py
new file mode 100644
index 0000000..081e252
--- /dev/null
+++ b/stats.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +from common import *
           4 +env = make_env()
           5 +mins={}; maxs={}; counts=[]; rots=0; bases=set()
           6 +for s in range(60):
           7 +    obs,info=env.reset(seed=s)
           8 +    names=obs.get_object_names(); counts.append(len(names)-3)
           9 +    bases.add(tuple(np.round(getbase(obs),3)))
          10 +    for n in names:
          11 +        if n=='robot': continue
          12 +        d=objd(obs,n); k=n.rstrip('0123456789')
          13 +        v=np.array([d['pose_x'],d['pose_y'],d['pose_z']])
          14 +        mins[k]=np.minimum(mins.get(k,v),v); maxs[k]=np.maximum(maxs.get(k,v),v)
          15 +        if abs(d['pose_qw'])<0.9999: rots+=1
          16 +print('counts',sorted(set(counts)), np.bincount(counts)); print('rotated',rots); print('bases',bases)
          17 +for k in mins: print(k, np.round(mins[k],3), np.round(maxs[k],3))
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..ccc82d6
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,23 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +import numpy as np
           4 +from approach import GeneratedApproach
           5 +def run(seed, verbose=False):
           6 +    env = make_env()
           7 +    obs, info = env.reset(seed=seed)
           8 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +    t0=time.time(); ap.reset(obs, info)
          10 +    n = len(obs.get_object_names())-3
          11 +    for t in range(env.max_steps):
          12 +        a = ap.get_action(obs)
          13 +        obs, r, term, trunc, info = env.step(a)
          14 +        if term: env.close(); return True, t+1, n, time.time()-t0
          15 +        if trunc: break
          16 +    env.close(); return False, t+1, n, time.time()-t0
          17 +if __name__ == '__main__':
          18 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          19 +    from concurrent.futures import ThreadPoolExecutor
          20 +    with ThreadPoolExecutor(8) as ex:
          21 +        res = list(ex.map(run, seeds))
          22 +    for s, r in zip(seeds, res): print(s, r)
          23 +    print('success', sum(r[0] for r in res), '/', len(res), 'mean steps', np.mean([r[1] for r in res if r[0]]))
```

</details>

<a id="C004"></a>
### C004 · Finger collision model for grasp candidates, blocked-move abort, grasp height band

Commit `5ab379c09b70851778359a0e5888a1917be89361`; parents: cb6f0b40eff5895390fe83fdaa4722e6a05ffcf9. Recorded author date: 2026-09-30T20:51:37+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0186](01_timeline.md#E0186): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_5ab379c_approach.py) · [Exact all-file diff](evidence/diffs/C004_5ab379c.diff)

[Previous saved controller snapshot](evidence/versions/C003_cb6f0b4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 690a83c..d344e32 100644
--- a/approach.py
+++ b/approach.py
@@ -3,17 +3,18 @@
    3      3  Kinematics: Kinova Gen3 URDF chain, calibrated empirically (see kin.py):
    4      4    arm mount = base pose + 0.12 m along base x, z=-0.0052; tool point 0.12 m along flange z.
    5      5  grasp_tf = object pose expressed in tool frame (T_obj = T_tool @ G).
           6 +Grasp succeeds if tool z in [obj_bottom+0.042, obj_top+0.03] and object between fingers.
           7 +Release only succeeds when the held object's bottom is within ~5mm of a support.
    6      8  """
    7      9  import numpy as np
    8     10  import kin
    9     11  
   10     12  JN = [f'joint_{i}' for i in range(1, 8)]
   11     13  TABLE_TOP = 0.075
   12        -Z_SAFE = 0.26          # tool z for transit
   13        -FINGER_DEPTH = 0.03    # tool point to fingertip bottom
          14 +Z_SAFE = 0.25          # tool z for transit
   14     15  JLIM = np.array([np.inf, 2.41, np.inf, 2.66, np.inf, 2.23, np.inf])
   15        -TABLE_X = (0.12, 0.47)
   16        -TABLE_Y = (-0.37, 0.37)
          16 +TABLE_X = (0.13, 0.47)
          17 +TABLE_Y = (-0.36, 0.36)
   17     18  
   18     19  
   19     20  def quat_mat(x, y, z, w):
@@ -22,6 +23,11 @@ def quat_mat(x, y, z, w):
   22     23                       [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
   23     24  
   24     25  
          26 +def rotz3(a):
          27 +    c, s = np.cos(a), np.sin(a)
          28 +    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
          29 +
          30 +
   25     31  def wrap(a):
   26     32      return (a + np.pi) % (2 * np.pi) - np.pi
   27     33  
@@ -35,12 +41,23 @@ class Obj:
   35     41          self.q = np.array([g('pose_qx'), g('pose_qy'), g('pose_qz'), g('pose_qw')])
   36     42          self.R = quat_mat(*self.q)
   37     43          self.yaw = np.arctan2(self.R[1, 0], self.R[0, 0])
          44 +        try:
          45 +            self.grasped = g('grasp_active') > 0.5
          46 +        except Exception:
          47 +            self.grasped = False
   38     48  
   39     49      def footprint(self):
   40        -        # axis aligned half extents in world (accounting for yaw)
   41     50          c, s = abs(np.cos(self.yaw)), abs(np.sin(self.yaw))
   42     51          return np.array([c * self.h[0] + s * self.h[1], s * self.h[0] + c * self.h[1]])
   43     52  
          53 +    @property
          54 +    def top(self):
          55 +        return self.p[2] + self.h[2]
          56 +
          57 +    @property
          58 +    def bottom(self):
          59 +        return self.p[2] - self.h[2]
          60 +
   44     61  
   45     62  def overlap(pa, ha, pb, hb, margin=0.0):
   46     63      return (abs(pa[0] - pb[0]) < ha[0] + hb[0] + margin) and (abs(pa[1] - pb[1]) < ha[1] + hb[1] + margin)
@@ -50,6 +67,7 @@ class GeneratedApproach:
   50     67      def __init__(self, action_space, observation_space, primitives):
   51     68          self.action_space = action_space
   52     69          self.observation_space = observation_space
          70 +        self.rng = np.random.default_rng(0)
   53     71  
   54     72      # ------------------------------------------------------------------ utils
   55     73      def _parse(self, state):
@@ -84,159 +102,240 @@ class GeneratedApproach:
   84    102          for attempt in range(3):
   85    103              qs = np.array(q0, dtype=float)
   86    104              if attempt > 0:
   87        -                qs = qs + np.random.uniform(-0.3, 0.3, 7)
   88        -            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=150, tol=1e-5)
   89        -            q = np.clip(q, -JLIM, JLIM)
   90        -            if ok:
         105 +                qs = qs + self.rng.uniform(-0.4, 0.4, 7)
         106 +            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=100, tol=1e-5)
         107 +            if ok and np.all(np.abs(q) <= JLIM):
   91    108                  return q, True
   92    109              if best is None:
   93        -                best = q
         110 +                best = np.clip(q, -JLIM, JLIM)
   94    111          return best, False
   95    112  
   96    113      def _cart_path(self, q0, p_from, p_to, R, step=0.04):
   97    114          """IK waypoints along a straight line in tool position with fixed orientation R."""
   98        -        d = np.linalg.norm(np.asarray(p_to) - np.asarray(p_from))
         115 +        p_from = np.asarray(p_from, float)
         116 +        p_to = np.asarray(p_to, float)
         117 +        d = np.linalg.norm(p_to - p_from)
   99    118          n = max(1, int(np.ceil(d / step)))
  100    119          qs = []
  101    120          q = np.array(q0, float)
         121 +        allok = True
  102    122          for i in range(1, n + 1):
  103    123              p = p_from + (p_to - p_from) * i / n
  104    124              q, ok = self._ik(q, p, R)
         125 +            allok &= ok
  105    126              qs.append(q.copy())
  106        -        return qs, q
         127 +        return qs, q, allok
  107    128  
  108    129      def _tool(self, q):
  109    130          return kin.fk(self.base, q)
  110    131  
  111        -    # --------------------------------------------------------------- planning
  112        -    def reset(self, state, info):
  113        -        self.objs = self._parse(state)
  114        -        self.base = self._base(state)
  115        -        self.plan = []          # list of ('move', q) / ('grip', val) / ('check', kind)
  116        -        self.phase = 'init'
  117        -        self.task_queue = None
  118        -        self.blocked = 0
  119        -        self.fail_count = {}
  120        -        self.moved_spots = []
  121        -        self.steps = 0
         132 +    def _finger_boxes(self, x, y, yaw, inner=0.041, outer=0.068, half_across=0.017):
         133 +        d = np.array([-np.sin(yaw), np.cos(yaw)])
         134 +        a = np.array([np.cos(yaw), np.sin(yaw)])
         135 +        c = 0.5 * (inner + outer)
         136 +        hl = 0.5 * (outer - inner)
         137 +        return [(np.array([x, y]) + sgn * c * d, d, a, hl, half_across) for sgn in (1, -1)]
  122    138  
  123        -    def _obstacles_to_clear(self, objs):
  124        -        reg = objs['target_region']
  125        -        tb = objs['target_block']
  126        -        res = []
  127        -        for n, o in objs.items():
  128        -            if not n.startswith('obstruction'):
  129        -                continue
  130        -            # anything touching the region footprint (plus finger margin) must go
  131        -            if overlap(o.p, o.footprint(), reg.p, reg.footprint(), 0.045):
  132        -                res.append(n)
  133        -        return res
         139 +    @staticmethod
         140 +    def _box_hits_obj(box, b, infl=0.004):
         141 +        """SAT test: oriented finger box vs object footprint (yawed rectangle)."""
         142 +        cen, d, a, hd, ha = box
         143 +        cy, sy = np.cos(b.yaw), np.sin(b.yaw)
         144 +        bx = np.array([cy, sy]); by = np.array([-sy, cy])
         145 +        bh = (b.h[0] + infl, b.h[1] + infl)
         146 +        rel = b.p[:2] - cen
         147 +        for ax in (d, a, bx, by):
         148 +            r1 = hd * abs(ax @ d) + ha * abs(ax @ a)
         149 +            r2 = bh[0] * abs(ax @ bx) + bh[1] * abs(ax @ by)
         150 +            if abs(rel @ ax) > r1 + r2:
         151 +                return False
         152 +        return True
  134    153  
  135        -    def _grasp_yaws(self, o, objs):
  136        -        """candidate tool yaws for grasping object o; fingers close along tool x = world (-sin, cos)."""
  137        -        cands = []
         154 +    def _grasp_candidates(self, o, objs):
         155 +        """list of (score, yaw, x, y, blockers) grasp candidates for object o."""
         156 +        out = []
  138    157          for k in range(2):
  139    158              yaw = o.yaw + k * np.pi / 2
  140        -            # closing along world dir (-sin yaw, cos yaw); object width along that dir
  141    159              d = np.array([-np.sin(yaw), np.cos(yaw)])
  142        -            width = abs(d @ o.R[:2, 0]) * o.h[0] + abs(d @ o.R[:2, 1]) * o.h[1]
  143        -            if width > 0.041:
         160 +            a = np.array([np.cos(yaw), np.sin(yaw)])
         161 +            wd = abs(d @ o.R[:2, 0]) * o.h[0] + abs(d @ o.R[:2, 1]) * o.h[1]
         162 +            wa = abs(a @ o.R[:2, 0]) * o.h[0] + abs(a @ o.R[:2, 1]) * o.h[1]
         163 +            if wd > 0.041:
  144    164                  continue
  145        -            # clearance: nearest other object along closing dir within finger span
  146        -            clr = 1.0
  147        -            perp = np.array([d[1], -d[0]])
  148        -            for n, b in objs.items():
  149        -                if n == o.name or n == 'target_region':
  150        -                    continue
  151        -                rel = b.p[:2] - o.p[:2]
  152        -                fp = b.footprint()
  153        -                along = abs(rel @ d) - (abs(d[0]) * fp[0] + abs(d[1]) * fp[1])
  154        -                across = abs(rel @ perp) - (abs(perp[0]) * fp[0] + abs(perp[1]) * fp[1])
  155        -                if across < 0.02 + (abs(perp @ o.R[:2, 0]) * o.h[0] + abs(perp @ o.R[:2, 1]) * o.h[1]):
  156        -                    clr = min(clr, along)
  157        -            cands.append((clr - width * 0.0, yaw, width))
  158        -        cands.sort(key=lambda c: -c[0])
  159        -        return cands
         165 +            smax = max(0.0, 0.037 - wd)
         166 +            amax = max(0.0, wa - 0.004)
         167 +            for sd in [0.0, 0.5 * smax, -0.5 * smax, smax, -smax]:
         168 +                for sa in [0.0, 0.5 * amax, -0.5 * amax, amax, -amax]:
         169 +                    x, y = o.p[:2] + sd * d + sa * a
         170 +                    blockers = []
         171 +                    for n, b in objs.items():
         172 +                        if n == o.name or n == 'target_region':
         173 +                            continue
         174 +                        for box in self._finger_boxes(x, y, yaw):
         175 +                            if self._box_hits_obj(box, b):
         176 +                                blockers.append(n)
         177 +                                break
         178 +                    score = len(blockers) * 10 + abs(sd) + abs(sa) + 0.01 * k * (wd > wa)
         179 +                    out.append((score, yaw, x, y, blockers))
         180 +        out.sort(key=lambda c: c[0])
         181 +        return out
  160    182  
  161    183      def _support_top(self, o, objs):
  162    184          top = TABLE_TOP
  163    185          for n, b in objs.items():
  164    186              if n == o.name:
  165    187                  continue
  166        -            btop = b.p[2] + b.h[2]
  167        -            if btop <= o.p[2] - o.h[2] + 1e-3 and overlap(o.p, o.footprint(), b.p, b.footprint()):
  168        -                top = max(top, btop)
         188 +            if b.top <= o.bottom + 2e-3 and overlap(o.p, o.footprint(), b.p, b.footprint()):
         189 +                top = max(top, b.top)
  169    190          return top
  170    191  
  171        -    def _free_spot(self, o, objs, avoid_names=()):
  172        -        """find a table location for object o not overlapping anything."""
  173        -        fp = o.footprint()
         192 +    # --------------------------------------------------------------- episode
         193 +    def reset(self, state, info):
         194 +        self.objs = self._parse(state)
         195 +        self.base = self._base(state)
         196 +        self.plan = []
         197 +        self.current = None
         198 +        self.blocked = 0
         199 +        self.last_q = None
         200 +        self.fail_count = {}
         201 +        self.steps = 0
         202 +        self.plans_made = 0
         203 +
         204 +    def _block_place_candidates(self, objs):
         205 +        """candidate (tool-free) placement yaws for target block on region, with blockers."""
  174    206          reg = objs['target_region']
  175    207          tb = objs['target_block']
  176        -        best = None
  177        -        for x in np.arange(TABLE_X[0] + fp[0], TABLE_X[1] - fp[0], 0.02):
  178        -            for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
  179        -                p = np.array([x, y])
  180        -                ok = True
  181        -                for n, b in objs.items():
  182        -                    if n == o.name:
  183        -                        continue
  184        -                    m = 0.06
  185        -                    if n == 'target_region':
  186        -                        m = 0.09
  187        -                    if overlap(p, fp, b.p, b.footprint(), m):
  188        -                        ok = False
  189        -                        break
  190        -                if not ok:
         208 +        out = []
         209 +        for k in range(2):
         210 +            yaw = reg.yaw + k * np.pi / 2  # tool yaw (fingers close along (-sin, cos))
         211 +            blockers = []
         212 +            for n, b in objs.items():
         213 +                if n in ('target_region', 'target_block'):
  191    214                      continue
  192        -                for sp, sh in self.moved_spots:
  193        -                    if overlap(p, fp, sp, sh, 0.06):
  194        -                        ok = False
         215 +                for box in self._finger_boxes(reg.p[0], reg.p[1], yaw):
         216 +                    if self._box_hits_obj(box, b):
         217 +                        blockers.append(n)
  195    218                          break
  196        -                if not ok:
         219 +            out.append((len(blockers), yaw, blockers))
         220 +        return out
         221 +
         222 +    def _to_clear(self, objs):
         223 +        reg = objs['target_region']
         224 +        res = set()
         225 +        for n, o in objs.items():
         226 +            if not n.startswith('obstruction'):
         227 +                continue
         228 +            if overlap(o.p, o.footprint(), reg.p, reg.footprint(), 0.004):
         229 +                res.add(n)
         230 +        return res
         231 +
         232 +    def _pick_target(self, objs):
         233 +        """decide which object to pick next and the grasp candidate."""
         234 +        clear = self._to_clear(objs)
         235 +        tb = objs['target_block']
         236 +        if not clear:
         237 +            # placement fingers: if the block can be grasped along an axis whose placement is blocked,
         238 +            # handled at place time; ensure at least one clean placement yaw.
         239 +            pc = self._block_place_candidates(objs)
         240 +            if min(c[0] for c in pc) > 0:
         241 +                clear |= set(min(pc, key=lambda c: c[0])[2])
         242 +        if not clear:
         243 +            want = ['target_block']
         244 +        else:
         245 +            want = list(clear)
         246 +        # expand with blockers
         247 +        best = None
         248 +        seen = set()
         249 +        frontier = list(want)
         250 +        depth = 0
         251 +        while frontier and depth < 3:
         252 +            nxt = []
         253 +            for n in frontier:
         254 +                if n in seen or n not in objs:
  197    255                      continue
  198        -                cost = np.linalg.norm(p - o.p[:2]) + 0.3 * abs(y - self.base[1]) * 0
  199        -                if best is None or cost < best[0]:
  200        -                    best = (cost, p)
  201        -        if best is None:
  202        -            return None
  203        -        return best[1]
         256 +                seen.add(n)
         257 +                cands = self._grasp_candidates(objs[n], objs)
         258 +                if n == 'target_block':
         259 +                    # prefer tool yaws allowing clean placement
         260 +                    pc = {round(wrap(c[1]) % np.pi, 3): c[0] for c in self._block_place_candidates(objs)}
         261 +                    cands = sorted(cands, key=lambda c: c[0] + 5 * (pc.get(round(wrap(c[1] - objs['target_region'].yaw + objs['target_region'].yaw) % np.pi, 3), 0) > 0))
         262 +                if not cands:
         263 +                    continue
         264 +                fc = self.fail_count.get(n, 0)
         265 +                c = cands[min(fc, len(cands) - 1)] if fc < len(cands) else cands[fc % len(cands)]
         266 +                score = len(c[4]) + 0.3 * fc + 0.1 * depth
         267 +                if best is None or score < best[0]:
         268 +                    best = (score, n, c)
         269 +                for bn in c[4]:
         270 +                    if bn.startswith('obstruction') or bn == 'target_block':
         271 +                        nxt.append(bn)
         272 +            frontier = nxt
         273 +            depth += 1
         274 +        return best
  204    275  
  205        -    def _plan_pick(self, state, name):
         276 +    def _plan_pick(self, state, name, cand):
  206    277          objs = self._parse(state)
  207    278          o = objs[name]
         279 +        _, yaw, gx, gy, _ = cand
  208    280          q = self._q(state)
  209    281          T = self._tool(q)
  210        -        cands = self._grasp_yaws(o, objs)
  211        -        nf = self.fail_count.get(name, 0)
  212        -        if not cands:
  213        -            cands = [(0, o.yaw, 0)]
  214        -        _, yaw, _ = cands[nf % len(cands)]
  215        -        # choose yaw or yaw+pi, closest to current wrist
  216    282          best = None
  217    283          for y in [yaw, yaw + np.pi]:
  218    284              R = kin.topdown_R(y)
  219        -            qa, ok = self._ik(q, np.array([o.p[0], o.p[1], Z_SAFE]), R)
         285 +            qa, ok = self._ik(q, np.array([gx, gy, Z_SAFE]), R)
  220    286              c = np.sum(np.abs(wrap(qa - q))) + (0 if ok else 100)
  221    287              if best is None or c < best[0]:
  222    288                  best = (c, y, R)
  223    289          _, yaw, R = best
  224        -        sup = self._support_top(o, objs)
  225        -        zg = o.p[2] + min(max(o.h[2] - 0.004, 0.018), 0.045)
  226        -        zg = max(zg, sup + FINGER_DEPTH + 0.003)
         290 +        lo = o.bottom + 0.044
         291 +        hi = o.top + 0.028
         292 +        zg = 0.5 * (lo + hi) if hi >= lo else lo
         293 +        zg = min(zg, lo + 0.012)
  227    294          p0 = T[:3, 3]
  228        -        above = np.array([o.p[0], o.p[1], Z_SAFE])
         295 +        above = np.array([gx, gy, max(Z_SAFE, p0[2])])
  229    296          start = np.array([p0[0], p0[1], max(p0[2], Z_SAFE)])
  230    297          plan = []
  231        -        qs, qe = self._cart_path(q, p0, start, T[:3, :3] if p0[2] < Z_SAFE - 0.01 else R)
         298 +        if p0[2] < Z_SAFE - 0.005:
         299 +            qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.05)
         300 +            plan += [('move', x) for x in qs]
         301 +        qs, q, _ = self._cart_path(q, start, above, R, step=0.08)
  232    302          plan += [('move', x) for x in qs]
  233        -        qs, qe = self._cart_path(qe, start, above, R, step=0.08)
  234        -        plan += [('move', x) for x in qs]
  235        -        qs, qe = self._cart_path(qe, above, np.array([o.p[0], o.p[1], zg]), R, step=0.05)
         303 +        qs, q, _ = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.05)
  236    304          plan += [('move', x) for x in qs]
  237    305          plan += [('grip', -1.0), ('check', 'grasp')]
  238    306          self.plan = plan
  239    307  
         308 +    def _free_spot(self, o, objs, tool_yaw):
         309 +        fp = o.footprint()
         310 +        best = None
         311 +        cur = o.p[:2]
         312 +        for x in np.arange(TABLE_X[0] + fp[0], TABLE_X[1] - fp[0], 0.02):
         313 +            for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
         314 +                p = np.array([x, y])
         315 +                cost = np.linalg.norm(p - cur)
         316 +                if best is not None and cost >= best[0]:
         317 +                    continue
         318 +                ok = True
         319 +                for n, b in objs.items():
         320 +                    if n == o.name:
         321 +                        continue
         322 +                    m = 0.075 if n in ('target_region', 'target_block') else 0.02
         323 +                    if overlap(p, fp, b.p, b.footprint(), m):
         324 +                        ok = False
         325 +                        break
         326 +                if not ok:
         327 +                    continue
         328 +                for box in self._finger_boxes(x, y, tool_yaw):
         329 +                    for n, b in objs.items():
         330 +                        if n != o.name and self._box_hits_obj(box, b, 0.01):
         331 +                            ok = False
         332 +                            break
         333 +                    if not ok:
         334 +                        break
         335 +                if ok:
         336 +                    best = (cost, p)
         337 +        return None if best is None else best[1]
         338 +
  240    339      def _plan_place(self, state, name, xy, support_top, yaw_obj):
  241    340          objs = self._parse(state)
  242    341          o = objs[name]
@@ -247,8 +346,7 @@ class GeneratedApproach:
  247    346          best = None
  248    347          for yo in [yaw_obj, yaw_obj + np.pi]:
  249    348              To = np.eye(4)
  250        -            c, s = np.cos(yo), np.sin(yo)
  251        -            To[:3, :3] = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
         349 +            To[:3, :3] = rotz3(yo)
  252    350              To[:3, 3] = [xy[0], xy[1], support_top + o.h[2] + 0.0015]
  253    351              Tt = To @ Ginv
  254    352              qa, ok = self._ik(q, Tt[:3, 3] + np.array([0, 0, Z_SAFE - Tt[2, 3]]), Tt[:3, :3])
@@ -258,72 +356,76 @@ class GeneratedApproach:
  258    356          Tt = best[1]
  259    357          R = Tt[:3, :3]
  260    358          p0 = T[:3, 3]
  261        -        # lift height: object bottom above everything
  262        -        maxtop = max([b.p[2] + b.h[2] for n, b in objs.items() if n != name] + [TABLE_TOP])
  263        -        obj_below_tool = (T @ G)[2, 3] - o.h[2]  # object bottom z
  264        -        lift_z = max(Z_SAFE, p0[2] + (maxtop + 0.03 - obj_below_tool))
         359 +        maxtop = max([b.top for n, b in objs.items() if n != name] + [TABLE_TOP])
         360 +        obj_bottom = (T @ G)[2, 3] - o.h[2]
         361 +        lift_z = max(Z_SAFE, p0[2] + (maxtop + 0.025 - obj_bottom))
  265    362          up = np.array([p0[0], p0[1], lift_z])
  266    363          above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
  267    364          plan = []
  268        -        qs, qe = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
         365 +        qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
  269    366          plan += [('move', x) for x in qs]
  270        -        qs, qe = self._cart_path(qe, up, above, R, step=0.08)
         367 +        qs, q, _ = self._cart_path(q, up, above, R, step=0.08)
  271    368          plan += [('move', x) for x in qs]
  272        -        qs, qe = self._cart_path(qe, above, Tt[:3, 3], R, step=0.05)
         369 +        qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.05)
  273    370          plan += [('move', x) for x in qs]
  274    371          plan += [('grip', 1.0), ('check', 'release')]
  275        -        # retreat up
  276        -        qs, qe = self._cart_path(qe, Tt[:3, 3], np.array([Tt[0, 3], Tt[1, 3], Z_SAFE]), R, step=0.06)
  277        -        plan += [('move', x) for x in qs]
  278    372          self.plan = plan
  279    373  
         374 +    def _held(self, state, objs):
         375 +        for n, o in objs.items():
         376 +            if o.grasped:
         377 +                return n
         378 +        return self.current
         379 +
  280    380      def _next_task(self, state):
         381 +        self.plans_made += 1
  281    382          objs = self._parse(state)
  282    383          grasped = float(state.get(self.robot, 'grasp_active')) > 0.5
  283        -        clear = self._obstacles_to_clear(objs)
  284    384          if grasped:
  285        -            # figure out which object is held
  286        -            held = None
  287        -            for n in objs:
  288        -                o = state.get_object_from_name(n)
  289        -                try:
  290        -                    if float(state.get(o, 'grasp_active')) > 0.5:
  291        -                        held = n
  292        -                except Exception:
  293        -                    pass
  294        -            if held is None:
  295        -                held = self.current
  296        -            if held == 'target_block' and not clear:
  297        -                reg = objs['target_region']
  298        -                self._plan_place(state, held, reg.p[:2], reg.p[2] + reg.h[2], reg.yaw)
  299        -            else:
  300        -                spot = self._free_spot(objs[held], objs)
  301        -                if spot is None:
  302        -                    spot = objs[held].p[:2]
  303        -                self.moved_spots.append((spot, objs[held].footprint()))
  304        -                self._plan_place(state, held, spot, TABLE_TOP, objs[held].yaw)
         385 +            held = self._held(state, objs)
  305    386              self.current = held
         387 +            o = objs[held]
         388 +            clear = self._to_clear(objs)
         389 +            reg = objs['target_region']
         390 +            if held == 'target_block' and not clear:
         391 +                self._plan_place(state, held, reg.p[:2], reg.top, reg.yaw)
         392 +                return
         393 +            G = self._G(state)
         394 +            Rt = rotz3(o.yaw) @ np.linalg.inv(G)[:3, :3]
         395 +            tool_yaw = np.arctan2(Rt[1, 1], Rt[0, 1]) * 0 + np.arctan2(-Rt[0, 0], Rt[1, 0])
         396 +            spot = self._free_spot(o, objs, tool_yaw)
         397 +            if spot is None:
         398 +                spot = o.p[:2]
         399 +            self._plan_place(state, held, spot, TABLE_TOP, o.yaw)
  306    400              return
  307        -        if clear:
  308        -            # choose obstruction with best clearance, top-most first
  309        -            def key(n):
  310        -                o = objs[n]
  311        -                c = self._grasp_yaws(o, objs)
  312        -                return (-(o.p[2] + o.h[2]) if False else 0, -(c[0][0] if c else -1) + 0.05 * self.fail_count.get(n, 0))
  313        -            clear.sort(key=key)
  314        -            self.current = clear[0]
  315        -        else:
         401 +        best = self._pick_target(objs)
         402 +        if best is None:
  316    403              self.current = 'target_block'
  317        -        self._plan_pick(state, self.current)
         404 +            cands = self._grasp_candidates(objs['target_block'], objs)
         405 +            if not cands:
         406 +                return
         407 +            best = (0, 'target_block', cands[0])
         408 +        self.current = best[1]
         409 +        self._plan_pick(state, best[1], best[2])
         410 +
         411 +    def _abort(self, state):
         412 +        """blocked: retreat straight up and replan."""
         413 +        self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
         414 +        q = self._q(state)
         415 +        T = self._tool(q)
         416 +        p0 = T[:3, 3]
         417 +        qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], max(p0[2] + 0.03, Z_SAFE)]), T[:3, :3], step=0.05)
         418 +        self.plan = [('move', x) for x in qs]
  318    419  
  319    420      # ---------------------------------------------------------------- acting
  320    421      def get_action(self, state):
  321    422          self.steps += 1
  322    423          a = np.zeros(11, dtype=np.float32)
  323    424          q = self._q(state)
  324        -        for _ in range(50):
         425 +        for _ in range(20):
  325    426              if not self.plan:
  326    427                  self._next_task(state)
         428 +                self.last_q = None
  327    429                  if not self.plan:
  328    430                      return a
  329    431              kind, val = self.plan[0]
@@ -332,24 +434,30 @@ class GeneratedApproach:
  332    434                  if np.max(np.abs(d)) < 1e-4:
  333    435                      self.plan.pop(0)
  334    436                      self.last_q = None
         437 +                    self.blocked = 0
  335    438                      continue
  336        -                if getattr(self, 'last_q', None) is not None and np.max(np.abs(q - self.last_q)) < 1e-7:
         439 +                if self.last_q is not None and np.max(np.abs(q - self.last_q)) < 1e-7:
  337    440                      self.blocked += 1
  338    441                  else:
  339    442                      self.blocked = 0
  340        -                if self.blocked >= 2:
  341        -                    # blocked: skip this waypoint
         443 +                if self.blocked >= 1:
  342    444                      self.blocked = 0
  343        -                    self.plan.pop(0)
  344    445                      self.last_q = None
         446 +                    if getattr(self, 'aborting', False):
         447 +                        self.plan.pop(0)
         448 +                    else:
         449 +                        self.aborting = True
         450 +                        self._abort(state)
  345    451                      continue
  346    452                  self.last_q = q.copy()
  347    453                  s = max(1.0, np.max(np.abs(d)) / 0.2)
  348    454                  a[3:10] = d / s
  349    455                  return a
         456 +            self.aborting = False
  350    457              if kind == 'grip':
  351    458                  self.plan.pop(0)
  352    459                  a[10] = val
         460 +                self.last_q = None
  353    461                  return a
  354    462              if kind == 'check':
  355    463                  self.plan.pop(0)
@@ -358,6 +466,7 @@ class GeneratedApproach:
  358    466                      self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
  359    467                      self.plan = []
  360    468                  elif val == 'release' and g:
         469 +                    self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
  361    470                      self.plan = []
  362    471                  continue
  363    472          return a
diff --git a/dbg1.py b/dbg1.py
new file mode 100644
index 0000000..708ae4b
--- /dev/null
+++ b/dbg1.py
@@ -0,0 +1,19 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +import numpy as np
           4 +import approach
           5 +from approach import GeneratedApproach
           6 +seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 200
           7 +env = make_env()
           8 +obs, info = env.reset(seed=seed)
           9 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +ap.reset(obs, info)
          11 +for n,o in ap.objs.items(): print(n, np.round(o.p,3), np.round(o.h,3))
          12 +orig = ap._next_task
          13 +def nt(state):
          14 +    orig(state); print('step', ap.steps, 'task', ap.current, 'grasp', state.get(ap.robot,'grasp_active'), 'plan len', len(ap.plan), 'fails', ap.fail_count)
          15 +ap._next_task = nt
          16 +for t in range(N):
          17 +    a = ap.get_action(obs)
          18 +    obs, r, term, trunc, info = env.step(a)
          19 +    if term: print('SOLVED', t+1); break
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..bb148c6
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,20 @@
           1 +import sys
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +import approach
           5 +from approach import GeneratedApproach
           6 +seed=int(sys.argv[1]); N=int(sys.argv[2])
           7 +env = make_env()
           8 +obs, info = env.reset(seed=seed)
           9 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +ap.reset(obs, info)
          11 +for t in range(N):
          12 +    q0=ap._q(obs)
          13 +    head = ap.plan[0] if ap.plan else None
          14 +    a = ap.get_action(obs)
          15 +    head = ap.plan[0] if ap.plan else None
          16 +    obs, r, term, trunc, info = env.step(a)
          17 +    q1=ap._q(obs)
          18 +    T=kin.fk(ap.base,q1)
          19 +    tgt = kin.fk(ap.base, head[1])[:3,3] if head and head[0]=='move' else None
          20 +    print(t, ap.current, head[0] if head else None, 'moved', round(float(np.max(np.abs(q1-q0))),3), 'tool', np.round(T[:3,3],3), 'tgt', None if tgt is None else np.round(tgt,3), 'grip', a[10], 'g', obs.get(ap.robot,'grasp_active'))
diff --git a/o1.txt b/o1.txt
new file mode 100644
index 0000000..131f2b1
--- /dev/null
+++ b/o1.txt
@@ -0,0 +1,14 @@
           1 +{'pose_x': 0.419426292181015, 'pose_y': -0.14254437386989594, 'pose_z': 0.10106389969587326, 'half_extent_x': 0.013297317549586296, 'half_extent_y': 0.017884286120533943, 'half_extent_z': 0.01606389693915844, 'grasp_active': 0.0, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0}
           2 +0 0.024 False True 0.0 0.0
           3 +0 0.026 False True 1.0 0.5
           4 +0 0.028 False True 1.0 0.5
           5 +0 0.03 False True 1.0 0.5
           6 +0 0.032 False True 1.0 0.5
           7 +0 0.034 False True 1.0 0.5
           8 +0 0.044 False True 1.0 0.5
           9 +0 0.046 False True 1.0 0.5
          10 +0 0.048 False True 1.0 0.5
          11 +0 0.05 False True 1.0 0.5
          12 +0 0.052 False True 0.0 0.0
          13 +0 0.054 False True 0.0 0.0
          14 +0 0.056 False True 0.0 0.0
diff --git a/o2.txt b/o2.txt
new file mode 100644
index 0000000..30e3a31
--- /dev/null
+++ b/o2.txt
@@ -0,0 +1,14 @@
           1 +{'pose_x': 0.1034325584769249, 'pose_y': 0.24800321459770203, 'pose_z': 0.09505476802587509, 'half_extent_x': 0.019350724294781685, 'half_extent_y': 0.01815853640437126, 'half_extent_z': 0.010054769925773144, 'grasp_active': 0.0, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0}
           2 +0 0.024 True True 0.0 0.0
           3 +0 0.026 True True 0.0 0.0
           4 +0 0.028 True True 0.0 0.0
           5 +0 0.03 True True 0.0 0.0
           6 +0 0.032 True True 0.0 0.0
           7 +0 0.034 True True 0.0 0.0
           8 +0 0.044 True True 0.0 0.0
           9 +0 0.046 True True 0.0 0.0
          10 +0 0.048 True True 0.0 0.0
          11 +0 0.05 True True 0.0 0.0
          12 +0 0.052 False True 0.0 0.0
          13 +0 0.054 False True 0.0 0.0
          14 +0 0.056 False True 0.0 0.0
diff --git a/o3.txt b/o3.txt
new file mode 100644
index 0000000..2a1eefd
--- /dev/null
+++ b/o3.txt
@@ -0,0 +1,14 @@
           1 +{'pose_x': 0.33598166704177856, 'pose_y': 0.17328143119812012, 'pose_z': 0.10000000149011612, 'half_extent_x': 0.03128708153963089, 'half_extent_y': 0.022474881261587143, 'half_extent_z': 0.02500000037252903, 'grasp_active': 0.0, 'pose_qx': 0.0, 'pose_qy': 0.0, 'pose_qz': 0.0, 'pose_qw': 1.0}
           2 +0 0.024 False True 1.0 0.42
           3 +0 0.026 False True 1.0 0.42
           4 +0 0.028 False True 1.0 0.42
           5 +0 0.03 False True 1.0 0.42
           6 +0 0.032 False True 1.0 0.42
           7 +0 0.034 False True 1.0 0.42
           8 +0 0.044 False True 1.0 0.42
           9 +0 0.046 False True 1.0 0.42
          10 +0 0.048 False True 1.0 0.42
          11 +0 0.05 False True 1.0 0.42
          12 +0 0.052 False True 1.0 0.42
          13 +0 0.054 False True 1.0 0.42
          14 +0 0.056 False True 1.0 0.42
diff --git a/pp5.py b/pp5.py
new file mode 100644
index 0000000..e6668b5
--- /dev/null
+++ b/pp5.py
@@ -0,0 +1,19 @@
           1 +import sys
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from common import *
           5 +seed=int(sys.argv[1]); name=sys.argv[2]
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed)
           8 +base = getbase(obs)
           9 +def goto(p, yaw=0, grip=0):
          10 +    global obs
          11 +    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
          12 +    obs, bl = move_to(env, obs, qt, grip); return bl, ok
          13 +o=objd(obs,name); R=robot(obs); print(o)
          14 +for yaw in [0]:
          15 +  for dz in list(np.arange(0.024,0.034,0.002))+list(np.arange(0.044,0.056,0.002)):
          16 +    goto([o['pose_x'],o['pose_y'],0.26],yaw); bl,ok=goto([o['pose_x'],o['pose_y'],o['pose_z']+dz],yaw)
          17 +    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          18 +    print(round(yaw,2), round(dz,3), bl, ok, obs.get(R,'grasp_active'), round(obs.get(R,'finger_state'),3))
          19 +    a[10]=1; obs,*_=env.step(a)
diff --git a/scan.py b/scan.py
new file mode 100644
index 0000000..7a12216
--- /dev/null
+++ b/scan.py
@@ -0,0 +1,20 @@
           1 +import sys, json
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from common import *
           5 +dx=float(sys.argv[1]); dzt=float(sys.argv[2]); YAW=float(sys.argv[3])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=0)
           8 +base = getbase(obs)
           9 +def goto(p, yaw=None):
          10 +    yaw = YAW if yaw is None else yaw
          11 +    global obs
          12 +    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
          13 +    obs, bl = move_to(env, obs, qt); return bl
          14 +o=objd(obs,'target_block')
          15 +top=o['pose_z']+o['half_extent_z']
          16 +res=[]
          17 +for dy in np.arange(-0.10,0.1001,0.01):
          18 +    goto([o['pose_x']+dx,o['pose_y']+dy,0.26]); bl=goto([o['pose_x']+dx,o['pose_y']+dy,top+dzt])
          19 +    res.append('X' if bl else '.')
          20 +print(f"{dx:+.2f}", ''.join(res))
```

</details>

<a id="C005"></a>
### C005 · fix abort flag

Commit `e469cf1207fbd8dc11cf72ce3976f072ec08b6ec`; parents: 5ab379c09b70851778359a0e5888a1917be89361. Recorded author date: 2026-09-30T20:51:44+02:00.

File roles (automatic): policy.

- [E0194](01_timeline.md#E0194): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_e469cf1_approach.py) · [Exact all-file diff](evidence/diffs/C005_e469cf1.diff)

[Previous saved controller snapshot](evidence/versions/C004_5ab379c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d344e32..c2738f2 100644
--- a/approach.py
+++ b/approach.py
@@ -200,6 +200,7 @@ class GeneratedApproach:
  200    200          self.fail_count = {}
  201    201          self.steps = 0
  202    202          self.plans_made = 0
         203 +        self.aborting = False
  203    204  
  204    205      def _block_place_candidates(self, objs):
  205    206          """candidate (tool-free) placement yaws for target block on region, with blockers."""
@@ -392,7 +393,7 @@ class GeneratedApproach:
  392    393                  return
  393    394              G = self._G(state)
  394    395              Rt = rotz3(o.yaw) @ np.linalg.inv(G)[:3, :3]
  395        -            tool_yaw = np.arctan2(Rt[1, 1], Rt[0, 1]) * 0 + np.arctan2(-Rt[0, 0], Rt[1, 0])
         396 +            tool_yaw = np.arctan2(-Rt[0, 0], Rt[1, 0])
  396    397              spot = self._free_spot(o, objs, tool_yaw)
  397    398              if spot is None:
  398    399                  spot = o.p[:2]
@@ -424,6 +425,7 @@ class GeneratedApproach:
  424    425          q = self._q(state)
  425    426          for _ in range(20):
  426    427              if not self.plan:
         428 +                self.aborting = False
  427    429                  self._next_task(state)
  428    430                  self.last_q = None
  429    431                  if not self.plan:
```

</details>

<a id="C006"></a>
### C006 · lateral escape before lifting held object from touching neighbours

Commit `b36e4ca60b16c0571d49b957c872765e48a13096`; parents: e469cf1207fbd8dc11cf72ce3976f072ec08b6ec. Recorded author date: 2026-09-30T20:54:02+02:00.

File roles (automatic): policy.

- [E0206](01_timeline.md#E0206): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_b36e4ca_approach.py) · [Exact all-file diff](evidence/diffs/C006_b36e4ca.diff)

[Previous saved controller snapshot](evidence/versions/C005_e469cf1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c2738f2..3a56f8f 100644
--- a/approach.py
+++ b/approach.py
@@ -360,9 +360,34 @@ class GeneratedApproach:
  360    360          maxtop = max([b.top for n, b in objs.items() if n != name] + [TABLE_TOP])
  361    361          obj_bottom = (T @ G)[2, 3] - o.h[2]
  362    362          lift_z = max(Z_SAFE, p0[2] + (maxtop + 0.025 - obj_bottom))
         363 +        plan = []
         364 +        # escape laterally from touching neighbours before lifting
         365 +        e = np.zeros(2)
         366 +        Ho = o.footprint()
         367 +        for n, b in objs.items():
         368 +            if n == name or b.top <= o.bottom + 2e-3 or b.bottom >= o.top - 2e-3:
         369 +                continue
         370 +            fb = b.footprint()
         371 +            dxy = o.p[:2] - b.p[:2]
         372 +            gaps = np.abs(dxy) - (Ho + fb)
         373 +            if max(gaps) < 0.006:
         374 +                ax = int(np.argmax(gaps))
         375 +                v = np.zeros(2)
         376 +                v[ax] = np.sign(dxy[ax]) if dxy[ax] != 0 else 1.0
         377 +                e += v
         378 +        nf = self.fail_count.get(name, 0)
         379 +        if nf > 0 and np.linalg.norm(e) > 0:
         380 +            ang = [0, 0.6, -0.6, 1.2, -1.2][nf % 5]
         381 +            c_, s_ = np.cos(ang), np.sin(ang)
         382 +            e = np.array([c_ * e[0] - s_ * e[1], s_ * e[0] + c_ * e[1]])
         383 +        if np.linalg.norm(e) > 0:
         384 +            e = e / np.linalg.norm(e)
         385 +            p1 = p0 + np.array([e[0] * 0.008, e[1] * 0.008, 0.002])
         386 +            qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.01)
         387 +            plan += [('move', x) for x in qs]
         388 +            p0 = p1
  363    389          up = np.array([p0[0], p0[1], lift_z])
  364    390          above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
  365        -        plan = []
  366    391          qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
  367    392          plan += [('move', x) for x in qs]
  368    393          qs, q, _ = self._cart_path(q, up, above, R, step=0.08)
```

</details>

<a id="C007"></a>
### C007 · 100/100 seeds 0-99; process-based test runner

Commit `85a15bc8c4e80a4fdd6ab881c81c06a0d845cbc1`; parents: b36e4ca60b16c0571d49b957c872765e48a13096. Recorded author date: 2026-09-30T21:02:42+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0234](01_timeline.md#E0234): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C007_85a15bc.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..d540f4e
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,24 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from approach import GeneratedApproach
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed)
           8 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +t0=time.time()
          10 +ap.reset(obs, info)
          11 +for n,o in ap.objs.items(): print(n, np.round(o.p,3), np.round(o.h,3))
          12 +orig = ap._next_task
          13 +def nt(state):
          14 +    orig(state); T=kin.fk(ap.base, ap._q(state)); print('step', ap.steps, 'task', ap.current, 'grasp', state.get(ap.robot,'grasp_active'), 'plan', len(ap.plan), 'fails', ap.fail_count, 'tool', np.round(T[:3,3],3), 'end', np.round(kin.fk(ap.base, ap.plan[-3][1])[:3,3],3) if len(ap.plan)>3 else '')
          15 +ap._next_task = nt
          16 +oa=ap._abort
          17 +def ab(state):
          18 +    T=kin.fk(ap.base, ap._q(state)); print('ABORT step', ap.steps, 'tool', np.round(T[:3,3],3)); oa(state)
          19 +ap._abort=ab
          20 +for t in range(N):
          21 +    a = ap.get_action(obs)
          22 +    obs, r, term, trunc, info = env.step(a)
          23 +    if term: print('SOLVED', t+1); break
          24 +print('time', time.time()-t0)
diff --git a/test_approach.py b/test_approach.py
index ccc82d6..f645e61 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -16,8 +16,9 @@ def run(seed, verbose=False):
   16     16      env.close(); return False, t+1, n, time.time()-t0
   17     17  if __name__ == '__main__':
   18     18      seeds = range(int(sys.argv[1]), int(sys.argv[2]))
   19        -    from concurrent.futures import ThreadPoolExecutor
          19 +    from concurrent.futures import ProcessPoolExecutor as ThreadPoolExecutor
   20     20      with ThreadPoolExecutor(8) as ex:
   21     21          res = list(ex.map(run, seeds))
   22        -    for s, r in zip(seeds, res): print(s, r)
   23        -    print('success', sum(r[0] for r in res), '/', len(res), 'mean steps', np.mean([r[1] for r in res if r[0]]))
          22 +    for s, r in zip(seeds, res):
          23 +        if not r[0] or r[3] > 20: print(s, r)
          24 +    print('success', sum(r[0] for r in res), '/', len(res), 'mean steps', np.mean([r[1] for r in res if r[0]]), 'max time', max(r[3] for r in res))
```

</details>

<a id="C008"></a>
### C008 · finer grasp offset candidates using measured grasp tolerance

Commit `8db5dca7b59c48c6493b562ca035514f6c810439`; parents: 85a15bc8c4e80a4fdd6ab881c81c06a0d845cbc1. Recorded author date: 2026-09-30T21:25:20+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0329](01_timeline.md#E0329): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_8db5dca_approach.py) · [Exact all-file diff](evidence/diffs/C008_8db5dca.diff)

[Previous saved controller snapshot](evidence/versions/C006_b36e4ca_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3a56f8f..0a82704 100644
--- a/approach.py
+++ b/approach.py
@@ -129,7 +129,7 @@ class GeneratedApproach:
  129    129      def _tool(self, q):
  130    130          return kin.fk(self.base, q)
  131    131  
  132        -    def _finger_boxes(self, x, y, yaw, inner=0.041, outer=0.068, half_across=0.017):
         132 +    def _finger_boxes(self, x, y, yaw, inner=0.042, outer=0.067, half_across=0.015):
  133    133          d = np.array([-np.sin(yaw), np.cos(yaw)])
  134    134          a = np.array([np.cos(yaw), np.sin(yaw)])
  135    135          c = 0.5 * (inner + outer)
@@ -137,7 +137,7 @@ class GeneratedApproach:
  137    137          return [(np.array([x, y]) + sgn * c * d, d, a, hl, half_across) for sgn in (1, -1)]
  138    138  
  139    139      @staticmethod
  140        -    def _box_hits_obj(box, b, infl=0.004):
         140 +    def _box_hits_obj(box, b, infl=0.003):
  141    141          """SAT test: oriented finger box vs object footprint (yawed rectangle)."""
  142    142          cen, d, a, hd, ha = box
  143    143          cy, sy = np.cos(b.yaw), np.sin(b.yaw)
@@ -154,6 +154,8 @@ class GeneratedApproach:
  154    154      def _grasp_candidates(self, o, objs):
  155    155          """list of (score, yaw, x, y, blockers) grasp candidates for object o."""
  156    156          out = []
         157 +        near = [(n, b) for n, b in objs.items() if n != o.name and n != 'target_region'
         158 +                and np.linalg.norm(b.p[:2] - o.p[:2]) < 0.16]
  157    159          for k in range(2):
  158    160              yaw = o.yaw + k * np.pi / 2
  159    161              d = np.array([-np.sin(yaw), np.cos(yaw)])
@@ -162,15 +164,15 @@ class GeneratedApproach:
  162    164              wa = abs(a @ o.R[:2, 0]) * o.h[0] + abs(a @ o.R[:2, 1]) * o.h[1]
  163    165              if wd > 0.041:
  164    166                  continue
  165        -            smax = max(0.0, 0.037 - wd)
  166        -            amax = max(0.0, wa - 0.004)
  167        -            for sd in [0.0, 0.5 * smax, -0.5 * smax, smax, -smax]:
  168        -                for sa in [0.0, 0.5 * amax, -0.5 * amax, amax, -amax]:
         167 +            smax = max(0.0, min(0.019, 0.040 - wd))
         168 +            amax = wa + 0.003
         169 +            sds = np.linspace(-smax, smax, 7) if smax > 0 else [0.0]
         170 +            sas = np.linspace(-amax, amax, 7)
         171 +            for sd in sds:
         172 +                for sa in sas:
  169    173                      x, y = o.p[:2] + sd * d + sa * a
  170    174                      blockers = []
  171        -                    for n, b in objs.items():
  172        -                        if n == o.name or n == 'target_region':
  173        -                            continue
         175 +                    for n, b in near:
  174    176                          for box in self._finger_boxes(x, y, yaw):
  175    177                              if self._box_hits_obj(box, b):
  176    178                                  blockers.append(n)
diff --git a/dbg3.py b/dbg3.py
index d540f4e..5fa63d2 100644
--- a/dbg3.py
+++ b/dbg3.py
@@ -4,7 +4,7 @@ import numpy as np, kin
    4      4  from approach import GeneratedApproach
    5      5  seed=int(sys.argv[1]); N=int(sys.argv[2])
    6      6  env = make_env()
    7        -obs, info = env.reset(seed=seed)
           7 +obs, info = env.reset(seed=seed, options=({'object_count': int(sys.argv[3])} if len(sys.argv)>3 else None))
    8      8  ap = GeneratedApproach(env.action_space, env.observation_space, {})
    9      9  t0=time.time()
   10     10  ap.reset(obs, info)
@@ -15,9 +15,10 @@ def nt(state):
   15     15  ap._next_task = nt
   16     16  oa=ap._abort
   17     17  def ab(state):
   18        -    T=kin.fk(ap.base, ap._q(state)); print('ABORT step', ap.steps, 'tool', np.round(T[:3,3],3)); oa(state)
          18 +    T=kin.fk(ap.base, ap._q(state)); print('ABORT step', ap.steps, 'tool', np.round(T[:3,3],3), 'q', np.round(ap._q(state),3), 'target', np.round(ap.plan[0][1],3), 'tgt tool', np.round(kin.fk(ap.base, ap.plan[0][1])[:3,3],3)); oa(state)
   19     19  ap._abort=ab
   20     20  for t in range(N):
          21 +    pass
   21     22      a = ap.get_action(obs)
   22     23      obs, r, term, trunc, info = env.step(a)
   23     24      if term: print('SOLVED', t+1); break
diff --git a/test_approach.py b/test_approach.py
index f645e61..69b3499 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -2,9 +2,10 @@ import sys, time
    2      2  from env_client import make_env
    3      3  import numpy as np
    4      4  from approach import GeneratedApproach
           5 +OC=None
    5      6  def run(seed, verbose=False):
    6      7      env = make_env()
    7        -    obs, info = env.reset(seed=seed)
           8 +    obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
    8      9      ap = GeneratedApproach(env.action_space, env.observation_space, {})
    9     10      t0=time.time(); ap.reset(obs, info)
   10     11      n = len(obs.get_object_names())-3
@@ -16,6 +17,8 @@ def run(seed, verbose=False):
   16     17      env.close(); return False, t+1, n, time.time()-t0
   17     18  if __name__ == '__main__':
   18     19      seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          20 +    if len(sys.argv) > 3:
          21 +        OC = int(sys.argv[3])
   19     22      from concurrent.futures import ProcessPoolExecutor as ThreadPoolExecutor
   20     23      with ThreadPoolExecutor(8) as ex:
   21     24          res = list(ex.map(run, seeds))
```

</details>

<a id="C009"></a>
### C009 · grasp sweep region must be free of other objects

Commit `36ac886fd9821f2a9e125d74c924abc8d5f08b5d`; parents: 8db5dca7b59c48c6493b562ca035514f6c810439. Recorded author date: 2026-09-30T21:29:23+02:00.

File roles (automatic): policy.

- [E0349](01_timeline.md#E0349): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_36ac886_approach.py) · [Exact all-file diff](evidence/diffs/C009_36ac886.diff)

[Previous saved controller snapshot](evidence/versions/C008_8db5dca_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0a82704..e11fdac 100644
--- a/approach.py
+++ b/approach.py
@@ -172,8 +172,9 @@ class GeneratedApproach:
  172    172                  for sa in sas:
  173    173                      x, y = o.p[:2] + sd * d + sa * a
  174    174                      blockers = []
         175 +                    boxes = self._finger_boxes(x, y, yaw) + [(np.array([x, y]), d, a, 0.043, 0.011)]
  175    176                      for n, b in near:
  176        -                        for box in self._finger_boxes(x, y, yaw):
         177 +                        for box in boxes:
  177    178                              if self._box_hits_obj(box, b):
  178    179                                  blockers.append(n)
  179    180                                  break
```

</details>

<a id="C010"></a>
### C010 · height-aware grasp candidates, diagonal yaws

Commit `d16351b17cc62283a25bd3b7a6cf0709a40d069a`; parents: 36ac886fd9821f2a9e125d74c924abc8d5f08b5d. Recorded author date: 2026-09-30T21:31:19+02:00.

File roles (automatic): policy.

- [E0359](01_timeline.md#E0359): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_d16351b_approach.py) · [Exact all-file diff](evidence/diffs/C010_d16351b.diff)

[Previous saved controller snapshot](evidence/versions/C009_36ac886_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e11fdac..7366ff6 100644
--- a/approach.py
+++ b/approach.py
@@ -152,12 +152,19 @@ class GeneratedApproach:
  152    152          return True
  153    153  
  154    154      def _grasp_candidates(self, o, objs):
  155        -        """list of (score, yaw, x, y, blockers) grasp candidates for object o."""
         155 +        """list of (score, yaw, x, y, blockers, zg) grasp candidates for object o."""
  156    156          out = []
  157    157          near = [(n, b) for n, b in objs.items() if n != o.name and n != 'target_region'
  158    158                  and np.linalg.norm(b.p[:2] - o.p[:2]) < 0.16]
  159        -        for k in range(2):
  160        -            yaw = o.yaw + k * np.pi / 2
         159 +        z_lo = o.bottom + 0.044
         160 +        z_hi = o.top + 0.027
         161 +        if z_hi < z_lo:
         162 +            z_hi = z_lo = 0.5 * (z_lo + z_hi)
         163 +        zs = [min(0.5 * (z_lo + z_hi), z_lo + 0.012)]
         164 +        if z_hi > zs[0] + 1e-3:
         165 +            zs.append(z_hi)
         166 +        for k, yoff in enumerate([0.0, np.pi / 2, np.pi / 4, -np.pi / 4]):
         167 +            yaw = o.yaw + yoff
  161    168              d = np.array([-np.sin(yaw), np.cos(yaw)])
  162    169              a = np.array([np.cos(yaw), np.sin(yaw)])
  163    170              wd = abs(d @ o.R[:2, 0]) * o.h[0] + abs(d @ o.R[:2, 1]) * o.h[1]
@@ -165,21 +172,25 @@ class GeneratedApproach:
  165    172              if wd > 0.041:
  166    173                  continue
  167    174              smax = max(0.0, min(0.019, 0.040 - wd))
  168        -            amax = wa + 0.003
         175 +            amax = max(0.0, (wa + 0.003) if k < 2 else 0.005)
  169    176              sds = np.linspace(-smax, smax, 7) if smax > 0 else [0.0]
  170        -            sas = np.linspace(-amax, amax, 7)
  171        -            for sd in sds:
  172        -                for sa in sas:
  173        -                    x, y = o.p[:2] + sd * d + sa * a
  174        -                    blockers = []
  175        -                    boxes = self._finger_boxes(x, y, yaw) + [(np.array([x, y]), d, a, 0.043, 0.011)]
  176        -                    for n, b in near:
  177        -                        for box in boxes:
  178        -                            if self._box_hits_obj(box, b):
  179        -                                blockers.append(n)
  180        -                                break
  181        -                    score = len(blockers) * 10 + abs(sd) + abs(sa) + 0.01 * k * (wd > wa)
  182        -                    out.append((score, yaw, x, y, blockers))
         177 +            sas = np.linspace(-amax, amax, 7) if amax > 0 else [0.0]
         178 +            for zi, zg in enumerate(zs):
         179 +                tip = zg - 0.035
         180 +                rel = [(n, b) for n, b in near if b.top > tip]
         181 +                for sd in sds:
         182 +                    for sa in sas:
         183 +                        x, y = o.p[:2] + sd * d + sa * a
         184 +                        boxes = self._finger_boxes(x, y, yaw) + [(np.array([x, y]), d, a, 0.043, 0.011)]
         185 +                        blockers = []
         186 +                        for n, b in rel:
         187 +                            for box in boxes:
         188 +                                if self._box_hits_obj(box, b):
         189 +                                    blockers.append(n)
         190 +                                    break
         191 +                        score = (len(blockers) * 10 + abs(sd) + abs(sa) + 0.01 * (k == 1) * (wd > wa)
         192 +                                 + 0.05 * (k >= 2) + 0.03 * zi)
         193 +                        out.append((score, yaw, x, y, blockers, zg))
  183    194          out.sort(key=lambda c: c[0])
  184    195          return out
  185    196  
@@ -280,7 +291,7 @@ class GeneratedApproach:
  280    291      def _plan_pick(self, state, name, cand):
  281    292          objs = self._parse(state)
  282    293          o = objs[name]
  283        -        _, yaw, gx, gy, _ = cand
         294 +        _, yaw, gx, gy, _, _ = cand
  284    295          q = self._q(state)
  285    296          T = self._tool(q)
  286    297          best = None
@@ -291,10 +302,7 @@ class GeneratedApproach:
  291    302              if best is None or c < best[0]:
  292    303                  best = (c, y, R)
  293    304          _, yaw, R = best
  294        -        lo = o.bottom + 0.044
  295        -        hi = o.top + 0.028
  296        -        zg = 0.5 * (lo + hi) if hi >= lo else lo
  297        -        zg = min(zg, lo + 0.012)
         305 +        zg = cand[5]
  298    306          p0 = T[:3, 3]
  299    307          above = np.array([gx, gy, max(Z_SAFE, p0[2])])
  300    308          start = np.array([p0[0], p0[1], max(p0[2], Z_SAFE)])
```

</details>

<a id="C011"></a>
### C011 · v2: choose symmetric yaw by full plan cost

Commit `88598b5afa8748055de23e707a4e88369e96ea6c`; parents: d16351b17cc62283a25bd3b7a6cf0709a40d069a. Recorded author date: 2026-09-30T21:50:01+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0498](01_timeline.md#E0498): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C011_88598b5.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
new file mode 100644
index 0000000..4578392
--- /dev/null
+++ b/approach_v2.py
@@ -0,0 +1,576 @@
           1 +"""Obstruction3D approach: clear obstructions from target region, then place target block.
           2 +
           3 +Kinematics: Kinova Gen3 URDF chain, calibrated empirically (see kin.py):
           4 +  arm mount = base pose + 0.12 m along base x, z=-0.0052; tool point 0.12 m along flange z.
           5 +grasp_tf = object pose expressed in tool frame (T_obj = T_tool @ G).
           6 +Grasp succeeds if tool z in [obj_bottom+0.042, obj_top+0.03] and object between fingers.
           7 +Release only succeeds when the held object's bottom is within ~5mm of a support.
           8 +"""
           9 +import numpy as np
          10 +import kin
          11 +
          12 +JN = [f'joint_{i}' for i in range(1, 8)]
          13 +TABLE_TOP = 0.075
          14 +Z_SAFE = 0.25          # tool z for transit
          15 +JLIM = np.array([np.inf, 2.41, np.inf, 2.66, np.inf, 2.23, np.inf])
          16 +TABLE_X = (0.13, 0.47)
          17 +TABLE_Y = (-0.36, 0.36)
          18 +
          19 +
          20 +def quat_mat(x, y, z, w):
          21 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          22 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          23 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          24 +
          25 +
          26 +def rotz3(a):
          27 +    c, s = np.cos(a), np.sin(a)
          28 +    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
          29 +
          30 +
          31 +def expso3(w):
          32 +    th = np.linalg.norm(w)
          33 +    if th < 1e-12:
          34 +        return np.eye(3)
          35 +    k = w / th
          36 +    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
          37 +    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K
          38 +
          39 +
          40 +def wrap(a):
          41 +    return (a + np.pi) % (2 * np.pi) - np.pi
          42 +
          43 +
          44 +class Obj:
          45 +    def __init__(self, state, o):
          46 +        g = lambda f: float(state.get(o, f))
          47 +        self.name = o.name
          48 +        self.p = np.array([g('pose_x'), g('pose_y'), g('pose_z')])
          49 +        self.h = np.array([g('half_extent_x'), g('half_extent_y'), g('half_extent_z')])
          50 +        self.q = np.array([g('pose_qx'), g('pose_qy'), g('pose_qz'), g('pose_qw')])
          51 +        self.R = quat_mat(*self.q)
          52 +        self.yaw = np.arctan2(self.R[1, 0], self.R[0, 0])
          53 +        try:
          54 +            self.grasped = g('grasp_active') > 0.5
          55 +        except Exception:
          56 +            self.grasped = False
          57 +
          58 +    def footprint(self):
          59 +        c, s = abs(np.cos(self.yaw)), abs(np.sin(self.yaw))
          60 +        return np.array([c * self.h[0] + s * self.h[1], s * self.h[0] + c * self.h[1]])
          61 +
          62 +    @property
          63 +    def top(self):
          64 +        return self.p[2] + self.h[2]
          65 +
          66 +    @property
          67 +    def bottom(self):
          68 +        return self.p[2] - self.h[2]
          69 +
          70 +
          71 +def overlap(pa, ha, pb, hb, margin=0.0):
          72 +    return (abs(pa[0] - pb[0]) < ha[0] + hb[0] + margin) and (abs(pa[1] - pb[1]) < ha[1] + hb[1] + margin)
          73 +
          74 +
          75 +class GeneratedApproach:
          76 +    def __init__(self, action_space, observation_space, primitives):
          77 +        self.action_space = action_space
          78 +        self.observation_space = observation_space
          79 +        self.rng = np.random.default_rng(0)
          80 +
          81 +    # ------------------------------------------------------------------ utils
          82 +    def _parse(self, state):
          83 +        self.robot = state.get_object_from_name('robot')
          84 +        objs = {}
          85 +        for n in sorted(state.get_object_names()):
          86 +            if n == 'robot':
          87 +                continue
          88 +            o = state.get_object_from_name(n)
          89 +            try:
          90 +                objs[n] = Obj(state, o)
          91 +            except Exception:
          92 +                pass
          93 +        return objs
          94 +
          95 +    def _q(self, state):
          96 +        return np.array([float(state.get(self.robot, f)) for f in JN])
          97 +
          98 +    def _base(self, state):
          99 +        return np.array([float(state.get(self.robot, f)) for f in ['pos_base_x', 'pos_base_y', 'pos_base_rot']])
         100 +
         101 +    def _G(self, state):
         102 +        g = [float(state.get(self.robot, f)) for f in
         103 +             ['grasp_tf_x', 'grasp_tf_y', 'grasp_tf_z', 'grasp_tf_qx', 'grasp_tf_qy', 'grasp_tf_qz', 'grasp_tf_qw']]
         104 +        G = np.eye(4)
         105 +        G[:3, :3] = quat_mat(*g[3:])
         106 +        G[:3, 3] = g[:3]
         107 +        return G
         108 +
         109 +    def _ik(self, q0, p, R):
         110 +        best = None
         111 +        for attempt in range(3):
         112 +            qs = np.array(q0, dtype=float)
         113 +            if attempt > 0:
         114 +                qs = qs + self.rng.uniform(-0.4, 0.4, 7)
         115 +            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=100, tol=1e-5)
         116 +            if ok and np.all(np.abs(q) <= JLIM):
         117 +                return q, True
         118 +            if best is None:
         119 +                best = np.clip(q, -JLIM, JLIM)
         120 +        return best, False
         121 +
         122 +    def _cart_path(self, q0, p_from, p_to, R, step=0.04, R_from=None):
         123 +        """IK waypoints along a straight line in tool position; orientation interpolated
         124 +        from R_from (default: R) to R."""
         125 +        p_from = np.asarray(p_from, float)
         126 +        p_to = np.asarray(p_to, float)
         127 +        d = np.linalg.norm(p_to - p_from)
         128 +        w = np.zeros(3)
         129 +        if R_from is not None:
         130 +            w = kin.rot_err(R_from, R)
         131 +        n = max(1, int(np.ceil(d / step)), int(np.ceil(np.linalg.norm(w) / 0.35)))
         132 +        qs = []
         133 +        q = np.array(q0, float)
         134 +        allok = True
         135 +        for i in range(1, n + 1):
         136 +            p = p_from + (p_to - p_from) * i / n
         137 +            Ri = R if (R_from is None or i == n) else expso3(w * i / n) @ R_from
         138 +            q, ok = self._ik(q, p, Ri)
         139 +            allok &= ok
         140 +            qs.append(q.copy())
         141 +        return qs, q, allok
         142 +
         143 +    @staticmethod
         144 +    def _ztransit(objs, held):
         145 +        tops = [b.top for n, b in objs.items() if n != held] + [TABLE_TOP]
         146 +        return max(tops) + 0.05
         147 +
         148 +    @staticmethod
         149 +    def _seg(qs):
         150 +        if not qs:
         151 +            return []
         152 +        return [('move', x) for x in qs[:-1]] + [('move', qs[-1], 'stop')]
         153 +
         154 +    def _tool(self, q):
         155 +        return kin.fk(self.base, q)
         156 +
         157 +    def _finger_boxes(self, x, y, yaw, inner=0.042, outer=0.067, half_across=0.015):
         158 +        d = np.array([-np.sin(yaw), np.cos(yaw)])
         159 +        a = np.array([np.cos(yaw), np.sin(yaw)])
         160 +        c = 0.5 * (inner + outer)
         161 +        hl = 0.5 * (outer - inner)
         162 +        return [(np.array([x, y]) + sgn * c * d, d, a, hl, half_across) for sgn in (1, -1)]
         163 +
         164 +    @staticmethod
         165 +    def _box_hits_obj(box, b, infl=0.003):
         166 +        """SAT test: oriented finger box vs object footprint (yawed rectangle)."""
         167 +        cen, d, a, hd, ha = box
         168 +        cy, sy = np.cos(b.yaw), np.sin(b.yaw)
         169 +        bx = np.array([cy, sy]); by = np.array([-sy, cy])
         170 +        bh = (b.h[0] + infl, b.h[1] + infl)
         171 +        rel = b.p[:2] - cen
         172 +        for ax in (d, a, bx, by):
         173 +            r1 = hd * abs(ax @ d) + ha * abs(ax @ a)
         174 +            r2 = bh[0] * abs(ax @ bx) + bh[1] * abs(ax @ by)
         175 +            if abs(rel @ ax) > r1 + r2:
         176 +                return False
         177 +        return True
         178 +
         179 +    def _grasp_candidates(self, o, objs):
         180 +        """list of (score, yaw, x, y, blockers, zg) grasp candidates for object o."""
         181 +        out = []
         182 +        near = [(n, b) for n, b in objs.items() if n != o.name and n != 'target_region'
         183 +                and np.linalg.norm(b.p[:2] - o.p[:2]) < 0.16]
         184 +        z_lo = o.bottom + 0.044
         185 +        z_hi = o.top + 0.027
         186 +        if z_hi < z_lo:
         187 +            z_hi = z_lo = 0.5 * (z_lo + z_hi)
         188 +        zs = [min(0.5 * (z_lo + z_hi), z_lo + 0.012)]
         189 +        if z_hi > zs[0] + 1e-3:
         190 +            zs.append(z_hi)
         191 +        for k, yoff in enumerate([0.0, np.pi / 2, np.pi / 4, -np.pi / 4]):
         192 +            yaw = o.yaw + yoff
         193 +            d = np.array([-np.sin(yaw), np.cos(yaw)])
         194 +            a = np.array([np.cos(yaw), np.sin(yaw)])
         195 +            wd = abs(d @ o.R[:2, 0]) * o.h[0] + abs(d @ o.R[:2, 1]) * o.h[1]
         196 +            wa = abs(a @ o.R[:2, 0]) * o.h[0] + abs(a @ o.R[:2, 1]) * o.h[1]
         197 +            if wd > 0.041:
         198 +                continue
         199 +            smax = max(0.0, min(0.019, 0.040 - wd))
         200 +            amax = max(0.0, (wa + 0.003) if k < 2 else 0.005)
         201 +            sds = np.linspace(-smax, smax, 7) if smax > 0 else [0.0]
         202 +            sas = np.linspace(-amax, amax, 7) if amax > 0 else [0.0]
         203 +            for zi, zg in enumerate(zs):
         204 +                tip = zg - 0.035
         205 +                rel = [(n, b) for n, b in near if b.top > tip]
         206 +                for sd in sds:
         207 +                    for sa in sas:
         208 +                        x, y = o.p[:2] + sd * d + sa * a
         209 +                        boxes = self._finger_boxes(x, y, yaw) + [(np.array([x, y]), d, a, 0.043, 0.011)]
         210 +                        blockers = []
         211 +                        for n, b in rel:
         212 +                            for box in boxes:
         213 +                                if self._box_hits_obj(box, b):
         214 +                                    blockers.append(n)
         215 +                                    break
         216 +                        score = (len(blockers) * 10 + abs(sd) + abs(sa) + 0.01 * (k == 1) * (wd > wa)
         217 +                                 + 0.05 * (k >= 2) + 0.03 * zi)
         218 +                        out.append((score, yaw, x, y, blockers, zg))
         219 +        out.sort(key=lambda c: c[0])
         220 +        return out
         221 +
         222 +    def _support_top(self, o, objs):
         223 +        top = TABLE_TOP
         224 +        for n, b in objs.items():
         225 +            if n == o.name:
         226 +                continue
         227 +            if b.top <= o.bottom + 2e-3 and overlap(o.p, o.footprint(), b.p, b.footprint()):
         228 +                top = max(top, b.top)
         229 +        return top
         230 +
         231 +    # --------------------------------------------------------------- episode
         232 +    def reset(self, state, info):
         233 +        self.objs = self._parse(state)
         234 +        self.base = self._base(state)
         235 +        self.plan = []
         236 +        self.current = None
         237 +        self.blocked = 0
         238 +        self.last_q = None
         239 +        self.fail_count = {}
         240 +        self.steps = 0
         241 +        self.plans_made = 0
         242 +        self.aborting = False
         243 +
         244 +    def _block_place_candidates(self, objs):
         245 +        """candidate (tool-free) placement yaws for target block on region, with blockers."""
         246 +        reg = objs['target_region']
         247 +        tb = objs['target_block']
         248 +        out = []
         249 +        for k in range(2):
         250 +            yaw = reg.yaw + k * np.pi / 2  # tool yaw (fingers close along (-sin, cos))
         251 +            blockers = []
         252 +            for n, b in objs.items():
         253 +                if n in ('target_region', 'target_block'):
         254 +                    continue
         255 +                for box in self._finger_boxes(reg.p[0], reg.p[1], yaw):
         256 +                    if self._box_hits_obj(box, b):
         257 +                        blockers.append(n)
         258 +                        break
         259 +            out.append((len(blockers), yaw, blockers))
         260 +        return out
         261 +
         262 +    def _to_clear(self, objs):
         263 +        reg = objs['target_region']
         264 +        res = set()
         265 +        for n, o in objs.items():
         266 +            if not n.startswith('obstruction'):
         267 +                continue
         268 +            if overlap(o.p, o.footprint(), reg.p, reg.footprint(), 0.004):
         269 +                res.add(n)
         270 +        return res
         271 +
         272 +    def _pick_target(self, objs):
         273 +        """decide which object to pick next and the grasp candidate."""
         274 +        clear = self._to_clear(objs)
         275 +        tb = objs['target_block']
         276 +        if not clear:
         277 +            # placement fingers: if the block can be grasped along an axis whose placement is blocked,
         278 +            # handled at place time; ensure at least one clean placement yaw.
         279 +            pc = self._block_place_candidates(objs)
         280 +            if min(c[0] for c in pc) > 0:
         281 +                clear |= set(min(pc, key=lambda c: c[0])[2])
         282 +        if not clear:
         283 +            want = ['target_block']
         284 +        else:
         285 +            want = sorted(clear)
         286 +        # expand with blockers
         287 +        best = None
         288 +        seen = set()
         289 +        frontier = list(want)
         290 +        depth = 0
         291 +        while frontier and depth < 3:
         292 +            nxt = []
         293 +            for n in frontier:
         294 +                if n in seen or n not in objs:
         295 +                    continue
         296 +                seen.add(n)
         297 +                cands = self._grasp_candidates(objs[n], objs)
         298 +                if n == 'target_block':
         299 +                    # prefer tool yaws allowing clean placement
         300 +                    pc = {round(wrap(c[1]) % np.pi, 3): c[0] for c in self._block_place_candidates(objs)}
         301 +                    cands = sorted(cands, key=lambda c: c[0] + 5 * (pc.get(round(wrap(c[1] - objs['target_region'].yaw + objs['target_region'].yaw) % np.pi, 3), 0) > 0))
         302 +                if not cands:
         303 +                    continue
         304 +                fc = self.fail_count.get(n, 0)
         305 +                c = cands[min(fc, len(cands) - 1)] if fc < len(cands) else cands[fc % len(cands)]
         306 +                score = len(c[4]) + 0.3 * fc + 0.1 * depth
         307 +                if best is None or score < best[0]:
         308 +                    best = (score, n, c)
         309 +                for bn in c[4]:
         310 +                    if bn.startswith('obstruction') or bn == 'target_block':
         311 +                        nxt.append(bn)
         312 +            frontier = nxt
         313 +            depth += 1
         314 +        return best
         315 +
         316 +    @staticmethod
         317 +    def _plan_cost(q, plan):
         318 +        c = 0.0
         319 +        for item in plan:
         320 +            if item[0] == 'move':
         321 +                c += np.max(np.abs(wrap(item[1] - q)))
         322 +                q = item[1]
         323 +        return c
         324 +
         325 +    def _plan_pick(self, state, name, cand):
         326 +        objs = self._parse(state)
         327 +        o = objs[name]
         328 +        _, yaw, gx, gy, _, _ = cand
         329 +        zt = self._ztransit(objs, None)
         330 +        q0 = self._q(state)
         331 +        T = self._tool(q0)
         332 +        zg = cand[5]
         333 +        p0 = T[:3, 3]
         334 +        above = np.array([gx, gy, max(zt, p0[2])])
         335 +        start = np.array([p0[0], p0[1], max(p0[2], zt)])
         336 +        best = None
         337 +        for y in [yaw, yaw + np.pi]:
         338 +            R = kin.topdown_R(y)
         339 +            q = q0
         340 +            plan = []
         341 +            if p0[2] < zt - 0.005:
         342 +                qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.05)
         343 +                plan += self._seg(qs)
         344 +            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.08, R_from=T[:3, :3])
         345 +            plan += self._seg(qs)
         346 +            qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.05)
         347 +            plan += self._seg(qs)
         348 +            plan += [('grip', -1.0), ('check', 'grasp')]
         349 +            c = self._plan_cost(q0, plan) + (0 if (ok1 and ok2) else 100)
         350 +            if best is None or c < best[0]:
         351 +                best = (c, plan)
         352 +        self.plan = best[1]
         353 +
         354 +    def _free_spot(self, o, objs, tool_yaw):
         355 +        fp = o.footprint()
         356 +        best = None
         357 +        cur = o.p[:2]
         358 +        for x in np.arange(TABLE_X[0] + fp[0], TABLE_X[1] - fp[0], 0.02):
         359 +            for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
         360 +                p = np.array([x, y])
         361 +                cost = np.linalg.norm(p - cur)
         362 +                if best is not None and cost >= best[0]:
         363 +                    continue
         364 +                ok = True
         365 +                for n, b in objs.items():
         366 +                    if n == o.name:
         367 +                        continue
         368 +                    m = 0.075 if n in ('target_region', 'target_block') else 0.02
         369 +                    if overlap(p, fp, b.p, b.footprint(), m):
         370 +                        ok = False
         371 +                        break
         372 +                if not ok:
         373 +                    continue
         374 +                for box in self._finger_boxes(x, y, tool_yaw):
         375 +                    for n, b in objs.items():
         376 +                        if n != o.name and self._box_hits_obj(box, b, 0.01):
         377 +                            ok = False
         378 +                            break
         379 +                    if not ok:
         380 +                        break
         381 +                if ok:
         382 +                    best = (cost, p)
         383 +        return None if best is None else best[1]
         384 +
         385 +    def _plan_place(self, state, name, xy, support_top, yaw_obj):
         386 +        objs = self._parse(state)
         387 +        o = objs[name]
         388 +        q = self._q(state)
         389 +        T = self._tool(q)
         390 +        G = self._G(state)
         391 +        Ginv = np.linalg.inv(G)
         392 +        zt = self._ztransit(objs, name)
         393 +        q_init = q
         394 +        best = None
         395 +        for yo in [yaw_obj, yaw_obj + np.pi]:
         396 +            q = q_init
         397 +            p0 = T[:3, 3]
         398 +            To = np.eye(4)
         399 +            To[:3, :3] = rotz3(yo)
         400 +            To[:3, 3] = [xy[0], xy[1], support_top + o.h[2] + 0.0015]
         401 +            Tt = To @ Ginv
         402 +            R = Tt[:3, :3]
         403 +            p0 = T[:3, 3]
         404 +            maxtop = max([b.top for n, b in objs.items() if n != name] + [TABLE_TOP])
         405 +            obj_bottom = (T @ G)[2, 3] - o.h[2]
         406 +            lift_z = max(zt, p0[2] + (maxtop + 0.02 - obj_bottom))
         407 +            plan = []
         408 +            # escape laterally from touching neighbours before lifting
         409 +            e = np.zeros(2)
         410 +            Ho = o.footprint()
         411 +            for n, b in objs.items():
         412 +                if n == name or b.top <= o.bottom + 2e-3 or b.bottom >= o.top - 2e-3:
         413 +                    continue
         414 +                fb = b.footprint()
         415 +                dxy = o.p[:2] - b.p[:2]
         416 +                gaps = np.abs(dxy) - (Ho + fb)
         417 +                if max(gaps) < 0.006:
         418 +                    ax = int(np.argmax(gaps))
         419 +                    v = np.zeros(2)
         420 +                    v[ax] = np.sign(dxy[ax]) if dxy[ax] != 0 else 1.0
         421 +                    e += v
         422 +            nf = self.fail_count.get(name, 0)
         423 +            if nf > 0 and np.linalg.norm(e) > 0:
         424 +                ang = [0, 0.6, -0.6, 1.2, -1.2][nf % 5]
         425 +                c_, s_ = np.cos(ang), np.sin(ang)
         426 +                e = np.array([c_ * e[0] - s_ * e[1], s_ * e[0] + c_ * e[1]])
         427 +            if np.linalg.norm(e) > 0:
         428 +                e = e / np.linalg.norm(e)
         429 +                p1 = p0 + np.array([e[0] * 0.008, e[1] * 0.008, 0.002])
         430 +                qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.01)
         431 +                plan += self._seg(qs)
         432 +                p0 = p1
         433 +            up = np.array([p0[0], p0[1], lift_z])
         434 +            above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
         435 +            qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
         436 +            plan += self._seg(qs)
         437 +            qs, q, _ = self._cart_path(q, up, above, R, step=0.08, R_from=T[:3, :3])
         438 +            plan += self._seg(qs)
         439 +            qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.05)
         440 +            plan += self._seg(qs)
         441 +            plan += [('grip', 1.0), ('check', 'release')]
         442 +            c = self._plan_cost(q_init, plan)
         443 +            if best is None or c < best[0]:
         444 +                best = (c, plan)
         445 +        self.plan = best[1]
         446 +
         447 +    def _held(self, state, objs):
         448 +        for n, o in objs.items():
         449 +            if o.grasped:
         450 +                return n
         451 +        return self.current
         452 +
         453 +    def _next_task(self, state):
         454 +        self.plans_made += 1
         455 +        objs = self._parse(state)
         456 +        grasped = float(state.get(self.robot, 'grasp_active')) > 0.5
         457 +        if grasped:
         458 +            held = self._held(state, objs)
         459 +            self.current = held
         460 +            o = objs[held]
         461 +            clear = self._to_clear(objs)
         462 +            reg = objs['target_region']
         463 +            if held == 'target_block' and not clear:
         464 +                self._plan_place(state, held, reg.p[:2], reg.top, reg.yaw)
         465 +                return
         466 +            G = self._G(state)
         467 +            Rt = rotz3(o.yaw) @ np.linalg.inv(G)[:3, :3]
         468 +            tool_yaw = np.arctan2(-Rt[0, 0], Rt[1, 0])
         469 +            spot = self._free_spot(o, objs, tool_yaw)
         470 +            if spot is None:
         471 +                spot = o.p[:2]
         472 +            self._plan_place(state, held, spot, TABLE_TOP, o.yaw)
         473 +            return
         474 +        best = self._pick_target(objs)
         475 +        if best is None:
         476 +            self.current = 'target_block'
         477 +            cands = self._grasp_candidates(objs['target_block'], objs)
         478 +            if not cands:
         479 +                return
         480 +            best = (0, 'target_block', cands[0])
         481 +        self.current = best[1]
         482 +        self._plan_pick(state, best[1], best[2])
         483 +
         484 +    def _abort(self, state):
         485 +        """blocked: retreat straight up and replan."""
         486 +        self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
         487 +        q = self._q(state)
         488 +        T = self._tool(q)
         489 +        p0 = T[:3, 3]
         490 +        qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], max(p0[2] + 0.03, Z_SAFE)]), T[:3, :3], step=0.05)
         491 +        self.plan = self._seg(qs)
         492 +
         493 +    # ---------------------------------------------------------------- acting
         494 +    def _lookahead(self, q, budget=0.199):
         495 +        cur = q.copy()
         496 +        i = 0
         497 +        target = q.copy()
         498 +        while i < len(self.plan) and self.plan[i][0] == 'move':
         499 +            w = cur + wrap(self.plan[i][1] - cur)
         500 +            if np.max(np.abs(w - q)) <= budget:
         501 +                target = w
         502 +                cur = w
         503 +                i += 1
         504 +                if len(self.plan[i - 1]) > 2:
         505 +                    break  # hard stop
         506 +                continue
         507 +            lo, hi = 0.0, 1.0
         508 +            for _ in range(20):
         509 +                mid = 0.5 * (lo + hi)
         510 +                if np.max(np.abs(cur + mid * (w - cur) - q)) <= budget:
         511 +                    lo = mid
         512 +                else:
         513 +                    hi = mid
         514 +            target = cur + lo * (w - cur)
         515 +            # waypoints before i are passed; head becomes the segment end we are heading to
         516 +            if i > 0:
         517 +                del self.plan[:i]
         518 +            return target
         519 +        # drop fully passed waypoints except the last reached (kept so arrival is confirmed)
         520 +        if i > 1:
         521 +            del self.plan[:i - 1]
         522 +        return target
         523 +
         524 +    def get_action(self, state):
         525 +        self.steps += 1
         526 +        a = np.zeros(11, dtype=np.float32)
         527 +        q = self._q(state)
         528 +        for _ in range(20):
         529 +            if not self.plan:
         530 +                self.aborting = False
         531 +                self._next_task(state)
         532 +                self.last_q = None
         533 +                if not self.plan:
         534 +                    return a
         535 +            kind, val = self.plan[0][0], self.plan[0][1]
         536 +            if kind == 'move':
         537 +                d = wrap(val - q)
         538 +                if np.max(np.abs(d)) < 1e-4:
         539 +                    self.plan.pop(0)
         540 +                    self.last_q = None
         541 +                    self.blocked = 0
         542 +                    continue
         543 +                if self.last_q is not None and np.max(np.abs(q - self.last_q)) < 1e-7:
         544 +                    self.blocked += 1
         545 +                else:
         546 +                    self.blocked = 0
         547 +                if self.blocked >= 1:
         548 +                    self.blocked = 0
         549 +                    self.last_q = None
         550 +                    if getattr(self, 'aborting', False):
         551 +                        self.plan.pop(0)
         552 +                    else:
         553 +                        self.aborting = True
         554 +                        self._abort(state)
         555 +                    continue
         556 +                self.last_q = q.copy()
         557 +                target = self._lookahead(q)
         558 +                a[3:10] = np.clip(wrap(target - q), -0.2, 0.2)
         559 +                return a
         560 +            self.aborting = False
         561 +            if kind == 'grip':
         562 +                self.plan.pop(0)
         563 +                a[10] = val
         564 +                self.last_q = None
         565 +                return a
         566 +            if kind == 'check':
         567 +                self.plan.pop(0)
         568 +                g = float(state.get(self.robot, 'grasp_active')) > 0.5
         569 +                if val == 'grasp' and not g:
         570 +                    self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
         571 +                    self.plan = []
         572 +                elif val == 'release' and g:
         573 +                    self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
         574 +                    self.plan = []
         575 +                continue
         576 +        return a
diff --git a/dbg3.py b/dbg3.py
index 5fa63d2..f9cb543 100644
--- a/dbg3.py
+++ b/dbg3.py
@@ -1,7 +1,8 @@
    1      1  import sys, time
    2      2  from env_client import make_env
    3      3  import numpy as np, kin
    4        -from approach import GeneratedApproach
           4 +import os, importlib as _il
           5 +GeneratedApproach = _il.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
    5      6  seed=int(sys.argv[1]); N=int(sys.argv[2])
    6      7  env = make_env()
    7      8  obs, info = env.reset(seed=seed, options=({'object_count': int(sys.argv[3])} if len(sys.argv)>3 else None))
diff --git a/dbg4.py b/dbg4.py
new file mode 100644
index 0000000..bcd13e0
--- /dev/null
+++ b/dbg4.py
@@ -0,0 +1,15 @@
           1 +import sys, os, importlib
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +M = importlib.import_module(os.environ.get("APPROACH","approach"))
           5 +seed=int(sys.argv[1]); N=int(sys.argv[2]); S=int(sys.argv[3])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed)
           8 +ap = M.GeneratedApproach(env.action_space, env.observation_space, {})
           9 +ap.reset(obs, info)
          10 +for t in range(N):
          11 +    q0=ap._q(obs)
          12 +    a = ap.get_action(obs)
          13 +    obs, r, term, trunc, info = env.step(a)
          14 +    if t>=S: print(t, ap.current, len(ap.plan), ap.plan[0][0] if ap.plan else None, np.round(a[3:],3), np.round(kin.fk(ap.base, ap._q(obs))[:3,3],3))
          15 +    if term: print('SOLVED'); break
diff --git a/gscan.py b/gscan.py
new file mode 100644
index 0000000..b6f7875
--- /dev/null
+++ b/gscan.py
@@ -0,0 +1,23 @@
           1 +import sys
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from common import *
           5 +sd=float(sys.argv[1]); yaw=float(sys.argv[2])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=1)
           8 +base = getbase(obs)
           9 +def goto(p):
          10 +    global obs
          11 +    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
          12 +    obs, bl = move_to(env, obs, qt); return bl
          13 +o=objd(obs,'obstruction0'); R=robot(obs)
          14 +d=np.array([-np.sin(yaw),np.cos(yaw)]); a=np.array([np.cos(yaw),np.sin(yaw)])
          15 +bottom=o['pose_z']-o['half_extent_z']
          16 +out=''
          17 +for sa in np.arange(0,0.033,0.004):
          18 +    x,y=np.array([o['pose_x'],o['pose_y']])+sd*d+sa*a
          19 +    goto([x,y,0.24]); bl=goto([x,y,bottom+0.046])
          20 +    act=np.zeros(11,dtype=np.float32); act[10]=-1; obs,*_=env.step(act)
          21 +    g=obs.get(R,'grasp_active'); out+= 'B' if bl else ('G' if g else '.')
          22 +    act[10]=1; obs,*_=env.step(act)
          23 +print(f'{sd:.3f}', out)
diff --git a/gscan2.py b/gscan2.py
new file mode 100644
index 0000000..840e769
--- /dev/null
+++ b/gscan2.py
@@ -0,0 +1,23 @@
           1 +import sys
           2 +from env_client import make_env
           3 +import numpy as np, kin
           4 +from common import *
           5 +yaw=float(sys.argv[1]); name=sys.argv[2]; seed=int(sys.argv[3])
           6 +env = make_env()
           7 +obs, info = env.reset(seed=seed)
           8 +base = getbase(obs)
           9 +def goto(p):
          10 +    global obs
          11 +    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
          12 +    obs, bl = move_to(env, obs, qt); return bl
          13 +o=objd(obs,name); R=robot(obs)
          14 +d=np.array([-np.sin(yaw),np.cos(yaw)]); a=np.array([np.cos(yaw),np.sin(yaw)])
          15 +bottom=o['pose_z']-o['half_extent_z']
          16 +out=[]
          17 +for sa in np.arange(-0.024,0.025,0.004):
          18 +    x,y=np.array([o['pose_x'],o['pose_y']])+sa*a
          19 +    goto([x,y,0.24]); bl=goto([x,y,bottom+0.046])
          20 +    act=np.zeros(11,dtype=np.float32); act[10]=-1; obs,*_=env.step(act)
          21 +    g=obs.get(R,'grasp_active'); out.append((round(sa,3), round(y,3), 'B' if bl else ('G' if g else '.')))
          22 +    act[10]=1; obs,*_=env.step(act)
          23 +print(out)
diff --git a/r10.txt b/r10.txt
new file mode 100644
index 0000000..fa5b470
--- /dev/null
+++ b/r10.txt
@@ -0,0 +1,21 @@
           1 +0 (True, 231, 10, 162.12440013885498)
           2 +1 (True, 190, 10, 127.36271953582764)
           3 +2 (True, 141, 10, 77.27515411376953)
           4 +3 (True, 131, 10, 74.83397078514099)
           5 +4 (True, 225, 10, 147.02270007133484)
           6 +5 (True, 177, 10, 98.81404495239258)
           7 +6 (True, 205, 10, 137.08586502075195)
           8 +7 (True, 245, 10, 163.80806064605713)
           9 +8 (True, 189, 10, 132.51899981498718)
          10 +9 (True, 131, 10, 87.60487675666809)
          11 +10 (True, 197, 10, 143.36270785331726)
          12 +11 (True, 148, 10, 101.80121922492981)
          13 +12 (True, 145, 10, 99.62717819213867)
          14 +13 (True, 214, 10, 123.6604859828949)
          15 +14 (True, 153, 10, 102.9199686050415)
          16 +15 (True, 159, 10, 98.41193056106567)
          17 +16 (True, 158, 10, 95.01274347305298)
          18 +17 (True, 112, 10, 61.83763813972473)
          19 +18 (True, 166, 10, 56.4270555973053)
          20 +19 (True, 124, 10, 41.247925758361816)
          21 +success 20 / 20 mean steps 172.05 max time 163.80806064605713
diff --git a/r4.txt b/r4.txt
new file mode 100644
index 0000000..7ccfc21
--- /dev/null
+++ b/r4.txt
@@ -0,0 +1,31 @@
           1 +0 (True, 127, 4, 133.38670349121094)
           2 +1 (True, 127, 4, 141.9424479007721)
           3 +2 (True, 122, 4, 113.76478934288025)
           4 +3 (True, 76, 4, 87.19220662117004)
           5 +4 (True, 202, 4, 203.11324501037598)
           6 +5 (True, 229, 4, 248.38072085380554)
           7 +6 (True, 148, 4, 145.3385546207428)
           8 +7 (True, 143, 4, 157.67138957977295)
           9 +8 (True, 132, 4, 131.7699785232544)
          10 +9 (True, 108, 4, 116.65791201591492)
          11 +10 (True, 104, 4, 114.53326606750488)
          12 +11 (True, 107, 4, 116.04428100585938)
          13 +12 (True, 200, 4, 220.2211298942566)
          14 +13 (True, 131, 4, 133.6246621608734)
          15 +14 (True, 70, 4, 73.3166081905365)
          16 +15 (True, 104, 4, 116.75713324546814)
          17 +16 (True, 69, 4, 74.0265142917633)
          18 +17 (True, 106, 4, 113.68610405921936)
          19 +18 (True, 77, 4, 75.39678144454956)
          20 +19 (True, 110, 4, 119.23793315887451)
          21 +20 (True, 117, 4, 134.6850883960724)
          22 +21 (True, 150, 4, 160.23180389404297)
          23 +22 (True, 72, 4, 84.54903936386108)
          24 +23 (True, 144, 4, 131.63834953308105)
          25 +24 (True, 113, 4, 111.81938791275024)
          26 +25 (True, 82, 4, 74.47860360145569)
          27 +26 (True, 106, 4, 88.43458533287048)
          28 +27 (True, 122, 4, 96.3819489479065)
          29 +28 (True, 127, 4, 86.25386047363281)
          30 +29 (True, 73, 4, 47.01294493675232)
          31 +success 30 / 30 mean steps 119.93333333333334 max time 248.38072085380554
diff --git a/r7.txt b/r7.txt
new file mode 100644
index 0000000..547c484
--- /dev/null
+++ b/r7.txt
@@ -0,0 +1,31 @@
           1 +0 (True, 159, 7, 90.11010670661926)
           2 +1 (True, 156, 7, 81.40653896331787)
           3 +2 (True, 134, 7, 75.34373903274536)
           4 +3 (True, 122, 7, 47.31409311294556)
           5 +4 (False, 1000, 7, 354.9952688217163)
           6 +5 (True, 175, 7, 85.66841173171997)
           7 +6 (True, 166, 7, 78.26843357086182)
           8 +7 (True, 191, 7, 103.37379598617554)
           9 +8 (True, 153, 7, 89.49127316474915)
          10 +9 (True, 131, 7, 71.94951510429382)
          11 +10 (True, 116, 7, 70.4980719089508)
          12 +11 (True, 132, 7, 84.22071981430054)
          13 +12 (True, 140, 7, 89.88107705116272)
          14 +13 (True, 214, 7, 124.55866837501526)
          15 +14 (True, 99, 7, 60.28774404525757)
          16 +15 (True, 174, 7, 108.90700960159302)
          17 +16 (True, 91, 7, 55.18851065635681)
          18 +17 (True, 118, 7, 71.90999341011047)
          19 +18 (True, 147, 7, 84.95680856704712)
          20 +19 (True, 166, 7, 99.9144070148468)
          21 +20 (True, 151, 7, 84.72178912162781)
          22 +21 (True, 153, 7, 98.70387578010559)
          23 +22 (True, 113, 7, 67.16453814506531)
          24 +23 (True, 159, 7, 93.85213661193848)
          25 +24 (True, 139, 7, 77.53740382194519)
          26 +25 (True, 80, 7, 46.03635263442993)
          27 +26 (True, 88, 7, 49.67180347442627)
          28 +27 (True, 126, 7, 56.63281726837158)
          29 +28 (True, 173, 7, 51.654138803482056)
          30 +29 (True, 100, 7, 29.174182176589966)
          31 +success 29 / 30 mean steps 140.20689655172413 max time 354.9952688217163
diff --git a/rd.txt b/rd.txt
new file mode 100644
index 0000000..3454108
--- /dev/null
+++ b/rd.txt
@@ -0,0 +1,37 @@
           1 +100 (True, 73, 2, 82.12752795219421)
           2 +102 (True, 45, 1, 44.20385217666626)
           3 +103 (True, 46, 1, 47.17070698738098)
           4 +104 (True, 67, 2, 92.88708114624023)
           5 +106 (True, 33, 1, 27.918169021606445)
           6 +107 (True, 31, 0, 27.469348669052124)
           7 +108 (True, 43, 0, 39.38398623466492)
           8 +109 (True, 49, 1, 50.593034505844116)
           9 +110 (True, 54, 1, 63.495187282562256)
          10 +111 (True, 42, 1, 34.366554975509644)
          11 +115 (True, 52, 1, 60.340779304504395)
          12 +116 (True, 20, 0, 26.24379277229309)
          13 +117 (True, 19, 0, 27.11879873275757)
          14 +118 (True, 49, 1, 54.31369662284851)
          15 +119 (True, 78, 1, 70.72021174430847)
          16 +122 (True, 83, 2, 69.13839054107666)
          17 +124 (True, 43, 2, 37.62494659423828)
          18 +125 (True, 72, 1, 56.82122302055359)
          19 +128 (True, 85, 2, 71.07632040977478)
          20 +129 (True, 46, 1, 29.179301023483276)
          21 +130 (True, 69, 2, 53.919267892837524)
          22 +131 (True, 55, 1, 34.57645034790039)
          23 +132 (True, 59, 2, 32.218775510787964)
          24 +133 (True, 43, 1, 28.73063015937805)
          25 +134 (True, 73, 2, 57.75910019874573)
          26 +135 (True, 45, 1, 27.86125898361206)
          27 +136 (True, 54, 2, 40.94742178916931)
          28 +137 (True, 53, 1, 41.35759496688843)
          29 +138 (True, 55, 1, 40.973175048828125)
          30 +139 (True, 82, 1, 53.39430522918701)
          31 +140 (True, 50, 1, 38.59265637397766)
          32 +141 (True, 42, 1, 23.006422996520996)
          33 +143 (True, 78, 2, 38.47154355049133)
          34 +144 (True, 32, 0, 21.93236231803894)
          35 +145 (True, 48, 1, 25.947503566741943)
          36 +146 (True, 46, 2, 23.099952697753906)
          37 +success 50 / 50 mean steps 44.74 max time 92.88708114624023
diff --git a/test_approach.py b/test_approach.py
index 69b3499..76660f4 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -1,7 +1,8 @@
    1      1  import sys, time
    2      2  from env_client import make_env
    3      3  import numpy as np
    4        -from approach import GeneratedApproach
           4 +import os, importlib as _il
           5 +GeneratedApproach = _il.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
    5      6  OC=None
    6      7  def run(seed, verbose=False):
    7      8      env = make_env()
diff --git a/timing.py b/timing.py
new file mode 100644
index 0000000..75e78fb
--- /dev/null
+++ b/timing.py
@@ -0,0 +1,15 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +import numpy as np
           4 +import os, importlib as _il
           5 +GeneratedApproach = _il.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
           6 +tot=[]; 
           7 +for seed in range(int(sys.argv[1]), int(sys.argv[2])):
           8 +    env = make_env(); obs, info = env.reset(seed=seed)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0=time.time(); ap.reset(obs, info); ct=time.time()-t0; mx=0
          11 +    for t in range(1000):
          12 +        t1=time.time(); a = ap.get_action(obs); dt=time.time()-t1; ct+=dt; mx=max(mx,dt)
          13 +        obs, r, term, trunc, info = env.step(a)
          14 +        if term: break
          15 +    print(seed, term, t+1, 'compute', round(ct,2), 'max step', round(mx,2)); env.close()
```

</details>

<a id="C012"></a>
### C012 · Promote v2 (lookahead pursuit, low transit, plan-cost yaw choice): 100/100, mean 32 steps

Commit `d07733fd11b110c6d696c006c4a2c74f11951345`; parents: 88598b5afa8748055de23e707a4e88369e96ea6c. Recorded author date: 2026-09-30T21:58:55+02:00.

File roles (automatic): policy.

- [E0534](01_timeline.md#E0534): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_d07733f_approach.py) · [Exact all-file diff](evidence/diffs/C012_d07733f.diff)

[Previous saved controller snapshot](evidence/versions/C010_d16351b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7366ff6..4578392 100644
--- a/approach.py
+++ b/approach.py
@@ -28,6 +28,15 @@ def rotz3(a):
   28     28      return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
   29     29  
   30     30  
          31 +def expso3(w):
          32 +    th = np.linalg.norm(w)
          33 +    if th < 1e-12:
          34 +        return np.eye(3)
          35 +    k = w / th
          36 +    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
          37 +    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K
          38 +
          39 +
   31     40  def wrap(a):
   32     41      return (a + np.pi) % (2 * np.pi) - np.pi
   33     42  
@@ -73,7 +82,7 @@ class GeneratedApproach:
   73     82      def _parse(self, state):
   74     83          self.robot = state.get_object_from_name('robot')
   75     84          objs = {}
   76        -        for n in state.get_object_names():
          85 +        for n in sorted(state.get_object_names()):
   77     86              if n == 'robot':
   78     87                  continue
   79     88              o = state.get_object_from_name(n)
@@ -110,22 +119,38 @@ class GeneratedApproach:
  110    119                  best = np.clip(q, -JLIM, JLIM)
  111    120          return best, False
  112    121  
  113        -    def _cart_path(self, q0, p_from, p_to, R, step=0.04):
  114        -        """IK waypoints along a straight line in tool position with fixed orientation R."""
         122 +    def _cart_path(self, q0, p_from, p_to, R, step=0.04, R_from=None):
         123 +        """IK waypoints along a straight line in tool position; orientation interpolated
         124 +        from R_from (default: R) to R."""
  115    125          p_from = np.asarray(p_from, float)
  116    126          p_to = np.asarray(p_to, float)
  117    127          d = np.linalg.norm(p_to - p_from)
  118        -        n = max(1, int(np.ceil(d / step)))
         128 +        w = np.zeros(3)
         129 +        if R_from is not None:
         130 +            w = kin.rot_err(R_from, R)
         131 +        n = max(1, int(np.ceil(d / step)), int(np.ceil(np.linalg.norm(w) / 0.35)))
  119    132          qs = []
  120    133          q = np.array(q0, float)
  121    134          allok = True
  122    135          for i in range(1, n + 1):
  123    136              p = p_from + (p_to - p_from) * i / n
  124        -            q, ok = self._ik(q, p, R)
         137 +            Ri = R if (R_from is None or i == n) else expso3(w * i / n) @ R_from
         138 +            q, ok = self._ik(q, p, Ri)
  125    139              allok &= ok
  126    140              qs.append(q.copy())
  127    141          return qs, q, allok
  128    142  
         143 +    @staticmethod
         144 +    def _ztransit(objs, held):
         145 +        tops = [b.top for n, b in objs.items() if n != held] + [TABLE_TOP]
         146 +        return max(tops) + 0.05
         147 +
         148 +    @staticmethod
         149 +    def _seg(qs):
         150 +        if not qs:
         151 +            return []
         152 +        return [('move', x) for x in qs[:-1]] + [('move', qs[-1], 'stop')]
         153 +
  129    154      def _tool(self, q):
  130    155          return kin.fk(self.base, q)
  131    156  
@@ -257,7 +282,7 @@ class GeneratedApproach:
  257    282          if not clear:
  258    283              want = ['target_block']
  259    284          else:
  260        -            want = list(clear)
         285 +            want = sorted(clear)
  261    286          # expand with blockers
  262    287          best = None
  263    288          seen = set()
@@ -288,34 +313,43 @@ class GeneratedApproach:
  288    313              depth += 1
  289    314          return best
  290    315  
         316 +    @staticmethod
         317 +    def _plan_cost(q, plan):
         318 +        c = 0.0
         319 +        for item in plan:
         320 +            if item[0] == 'move':
         321 +                c += np.max(np.abs(wrap(item[1] - q)))
         322 +                q = item[1]
         323 +        return c
         324 +
  291    325      def _plan_pick(self, state, name, cand):
  292    326          objs = self._parse(state)
  293    327          o = objs[name]
  294    328          _, yaw, gx, gy, _, _ = cand
  295        -        q = self._q(state)
  296        -        T = self._tool(q)
         329 +        zt = self._ztransit(objs, None)
         330 +        q0 = self._q(state)
         331 +        T = self._tool(q0)
         332 +        zg = cand[5]
         333 +        p0 = T[:3, 3]
         334 +        above = np.array([gx, gy, max(zt, p0[2])])
         335 +        start = np.array([p0[0], p0[1], max(p0[2], zt)])
  297    336          best = None
  298    337          for y in [yaw, yaw + np.pi]:
  299    338              R = kin.topdown_R(y)
  300        -            qa, ok = self._ik(q, np.array([gx, gy, Z_SAFE]), R)
  301        -            c = np.sum(np.abs(wrap(qa - q))) + (0 if ok else 100)
         339 +            q = q0
         340 +            plan = []
         341 +            if p0[2] < zt - 0.005:
         342 +                qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.05)
         343 +                plan += self._seg(qs)
         344 +            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.08, R_from=T[:3, :3])
         345 +            plan += self._seg(qs)
         346 +            qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.05)
         347 +            plan += self._seg(qs)
         348 +            plan += [('grip', -1.0), ('check', 'grasp')]
         349 +            c = self._plan_cost(q0, plan) + (0 if (ok1 and ok2) else 100)
  302    350              if best is None or c < best[0]:
  303        -                best = (c, y, R)
  304        -        _, yaw, R = best
  305        -        zg = cand[5]
  306        -        p0 = T[:3, 3]
  307        -        above = np.array([gx, gy, max(Z_SAFE, p0[2])])
  308        -        start = np.array([p0[0], p0[1], max(p0[2], Z_SAFE)])
  309        -        plan = []
  310        -        if p0[2] < Z_SAFE - 0.005:
  311        -            qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.05)
  312        -            plan += [('move', x) for x in qs]
  313        -        qs, q, _ = self._cart_path(q, start, above, R, step=0.08)
  314        -        plan += [('move', x) for x in qs]
  315        -        qs, q, _ = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.05)
  316        -        plan += [('move', x) for x in qs]
  317        -        plan += [('grip', -1.0), ('check', 'grasp')]
  318        -        self.plan = plan
         351 +                best = (c, plan)
         352 +        self.plan = best[1]
  319    353  
  320    354      def _free_spot(self, o, objs, tool_yaw):
  321    355          fp = o.footprint()
@@ -355,58 +389,60 @@ class GeneratedApproach:
  355    389          T = self._tool(q)
  356    390          G = self._G(state)
  357    391          Ginv = np.linalg.inv(G)
         392 +        zt = self._ztransit(objs, name)
         393 +        q_init = q
  358    394          best = None
  359    395          for yo in [yaw_obj, yaw_obj + np.pi]:
         396 +            q = q_init
         397 +            p0 = T[:3, 3]
  360    398              To = np.eye(4)
  361    399              To[:3, :3] = rotz3(yo)
  362    400              To[:3, 3] = [xy[0], xy[1], support_top + o.h[2] + 0.0015]
  363    401              Tt = To @ Ginv
  364        -            qa, ok = self._ik(q, Tt[:3, 3] + np.array([0, 0, Z_SAFE - Tt[2, 3]]), Tt[:3, :3])
  365        -            cst = np.sum(np.abs(wrap(qa - q))) + (0 if ok else 100)
  366        -            if best is None or cst < best[0]:
  367        -                best = (cst, Tt)
  368        -        Tt = best[1]
  369        -        R = Tt[:3, :3]
  370        -        p0 = T[:3, 3]
  371        -        maxtop = max([b.top for n, b in objs.items() if n != name] + [TABLE_TOP])
  372        -        obj_bottom = (T @ G)[2, 3] - o.h[2]
  373        -        lift_z = max(Z_SAFE, p0[2] + (maxtop + 0.025 - obj_bottom))
  374        -        plan = []
  375        -        # escape laterally from touching neighbours before lifting
  376        -        e = np.zeros(2)
  377        -        Ho = o.footprint()
  378        -        for n, b in objs.items():
  379        -            if n == name or b.top <= o.bottom + 2e-3 or b.bottom >= o.top - 2e-3:
  380        -                continue
  381        -            fb = b.footprint()
  382        -            dxy = o.p[:2] - b.p[:2]
  383        -            gaps = np.abs(dxy) - (Ho + fb)
  384        -            if max(gaps) < 0.006:
  385        -                ax = int(np.argmax(gaps))
  386        -                v = np.zeros(2)
  387        -                v[ax] = np.sign(dxy[ax]) if dxy[ax] != 0 else 1.0
  388        -                e += v
  389        -        nf = self.fail_count.get(name, 0)
  390        -        if nf > 0 and np.linalg.norm(e) > 0:
  391        -            ang = [0, 0.6, -0.6, 1.2, -1.2][nf % 5]
  392        -            c_, s_ = np.cos(ang), np.sin(ang)
  393        -            e = np.array([c_ * e[0] - s_ * e[1], s_ * e[0] + c_ * e[1]])
  394        -        if np.linalg.norm(e) > 0:
  395        -            e = e / np.linalg.norm(e)
  396        -            p1 = p0 + np.array([e[0] * 0.008, e[1] * 0.008, 0.002])
  397        -            qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.01)
  398        -            plan += [('move', x) for x in qs]
  399        -            p0 = p1
  400        -        up = np.array([p0[0], p0[1], lift_z])
  401        -        above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
  402        -        qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
  403        -        plan += [('move', x) for x in qs]
  404        -        qs, q, _ = self._cart_path(q, up, above, R, step=0.08)
  405        -        plan += [('move', x) for x in qs]
  406        -        qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.05)
  407        -        plan += [('move', x) for x in qs]
  408        -        plan += [('grip', 1.0), ('check', 'release')]
  409        -        self.plan = plan
         402 +            R = Tt[:3, :3]
         403 +            p0 = T[:3, 3]
         404 +            maxtop = max([b.top for n, b in objs.items() if n != name] + [TABLE_TOP])
         405 +            obj_bottom = (T @ G)[2, 3] - o.h[2]
         406 +            lift_z = max(zt, p0[2] + (maxtop + 0.02 - obj_bottom))
         407 +            plan = []
         408 +            # escape laterally from touching neighbours before lifting
         409 +            e = np.zeros(2)
         410 +            Ho = o.footprint()
         411 +            for n, b in objs.items():
         412 +                if n == name or b.top <= o.bottom + 2e-3 or b.bottom >= o.top - 2e-3:
         413 +                    continue
         414 +                fb = b.footprint()
         415 +                dxy = o.p[:2] - b.p[:2]
         416 +                gaps = np.abs(dxy) - (Ho + fb)
         417 +                if max(gaps) < 0.006:
         418 +                    ax = int(np.argmax(gaps))
         419 +                    v = np.zeros(2)
         420 +                    v[ax] = np.sign(dxy[ax]) if dxy[ax] != 0 else 1.0
         421 +                    e += v
         422 +            nf = self.fail_count.get(name, 0)
         423 +            if nf > 0 and np.linalg.norm(e) > 0:
         424 +                ang = [0, 0.6, -0.6, 1.2, -1.2][nf % 5]
         425 +                c_, s_ = np.cos(ang), np.sin(ang)
         426 +                e = np.array([c_ * e[0] - s_ * e[1], s_ * e[0] + c_ * e[1]])
         427 +            if np.linalg.norm(e) > 0:
         428 +                e = e / np.linalg.norm(e)
         429 +                p1 = p0 + np.array([e[0] * 0.008, e[1] * 0.008, 0.002])
         430 +                qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.01)
         431 +                plan += self._seg(qs)
         432 +                p0 = p1
         433 +            up = np.array([p0[0], p0[1], lift_z])
         434 +            above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
         435 +            qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
         436 +            plan += self._seg(qs)
         437 +            qs, q, _ = self._cart_path(q, up, above, R, step=0.08, R_from=T[:3, :3])
         438 +            plan += self._seg(qs)
         439 +            qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.05)
         440 +            plan += self._seg(qs)
         441 +            plan += [('grip', 1.0), ('check', 'release')]
         442 +            c = self._plan_cost(q_init, plan)
         443 +            if best is None or c < best[0]:
         444 +                best = (c, plan)
         445 +        self.plan = best[1]
  410    446  
  411    447      def _held(self, state, objs):
  412    448          for n, o in objs.items():
@@ -452,9 +488,39 @@ class GeneratedApproach:
  452    488          T = self._tool(q)
  453    489          p0 = T[:3, 3]
  454    490          qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], max(p0[2] + 0.03, Z_SAFE)]), T[:3, :3], step=0.05)
  455        -        self.plan = [('move', x) for x in qs]
         491 +        self.plan = self._seg(qs)
  456    492  
  457    493      # ---------------------------------------------------------------- acting
         494 +    def _lookahead(self, q, budget=0.199):
         495 +        cur = q.copy()
         496 +        i = 0
         497 +        target = q.copy()
         498 +        while i < len(self.plan) and self.plan[i][0] == 'move':
         499 +            w = cur + wrap(self.plan[i][1] - cur)
         500 +            if np.max(np.abs(w - q)) <= budget:
         501 +                target = w
         502 +                cur = w
         503 +                i += 1
         504 +                if len(self.plan[i - 1]) > 2:
         505 +                    break  # hard stop
         506 +                continue
         507 +            lo, hi = 0.0, 1.0
         508 +            for _ in range(20):
         509 +                mid = 0.5 * (lo + hi)
         510 +                if np.max(np.abs(cur + mid * (w - cur) - q)) <= budget:
         511 +                    lo = mid
         512 +                else:
         513 +                    hi = mid
         514 +            target = cur + lo * (w - cur)
         515 +            # waypoints before i are passed; head becomes the segment end we are heading to
         516 +            if i > 0:
         517 +                del self.plan[:i]
         518 +            return target
         519 +        # drop fully passed waypoints except the last reached (kept so arrival is confirmed)
         520 +        if i > 1:
         521 +            del self.plan[:i - 1]
         522 +        return target
         523 +
  458    524      def get_action(self, state):
  459    525          self.steps += 1
  460    526          a = np.zeros(11, dtype=np.float32)
@@ -466,7 +532,7 @@ class GeneratedApproach:
  466    532                  self.last_q = None
  467    533                  if not self.plan:
  468    534                      return a
  469        -            kind, val = self.plan[0]
         535 +            kind, val = self.plan[0][0], self.plan[0][1]
  470    536              if kind == 'move':
  471    537                  d = wrap(val - q)
  472    538                  if np.max(np.abs(d)) < 1e-4:
@@ -488,8 +554,8 @@ class GeneratedApproach:
  488    554                          self._abort(state)
  489    555                      continue
  490    556                  self.last_q = q.copy()
  491        -                s = max(1.0, np.max(np.abs(d)) / 0.2)
  492        -                a[3:10] = d / s
         557 +                target = self._lookahead(q)
         558 +                a[3:10] = np.clip(wrap(target - q), -0.2, 0.2)
  493    559                  return a
  494    560              self.aborting = False
  495    561              if kind == 'grip':
```

</details>

<a id="C013"></a>
### C013 · v2: choose escape direction by clearance search

Commit `872a421dc785b10113a2b6c3e0b1fc9167491cec`; parents: d07733fd11b110c6d696c006c4a2c74f11951345. Recorded author date: 2026-09-30T22:09:22+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E0570](01_timeline.md#E0570): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C013_872a421.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index 4578392..47390c4 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -407,6 +407,7 @@ class GeneratedApproach:
  407    407              plan = []
  408    408              # escape laterally from touching neighbours before lifting
  409    409              e = np.zeros(2)
         410 +            touch = False
  410    411              Ho = o.footprint()
  411    412              for n, b in objs.items():
  412    413                  if n == name or b.top <= o.bottom + 2e-3 or b.bottom >= o.top - 2e-3:
@@ -419,11 +420,18 @@ class GeneratedApproach:
  419    420                      v = np.zeros(2)
  420    421                      v[ax] = np.sign(dxy[ax]) if dxy[ax] != 0 else 1.0
  421    422                      e += v
  422        -            nf = self.fail_count.get(name, 0)
  423        -            if nf > 0 and np.linalg.norm(e) > 0:
  424        -                ang = [0, 0.6, -0.6, 1.2, -1.2][nf % 5]
  425        -                c_, s_ = np.cos(ang), np.sin(ang)
  426        -                e = np.array([c_ * e[0] - s_ * e[1], s_ * e[0] + c_ * e[1]])
         423 +                    touch = True
         424 +            if touch:
         425 +                nbrs = [b for n, b in objs.items() if n != name and b.top > o.bottom + 2e-3 and b.bottom < o.top - 2e-3]
         426 +                opts = []
         427 +                for k in range(16):
         428 +                    ang = 2 * np.pi * k / 16
         429 +                    d = np.array([np.cos(ang), np.sin(ang)])
         430 +                    sep = min([np.max(np.abs(o.p[:2] + 0.008 * d - b.p[:2]) - (Ho + b.footprint())) for b in nbrs] + [1.0])
         431 +                    opts.append((-min(sep, 0.004) - 0.0005 * float(d @ e), k, d))
         432 +                opts.sort(key=lambda t: t[0])
         433 +                nf = self.fail_count.get(name, 0)
         434 +                e = opts[nf % len(opts)][2]
  427    435              if np.linalg.norm(e) > 0:
  428    436                  e = e / np.linalg.norm(e)
  429    437                  p1 = p0 + np.array([e[0] * 0.008, e[1] * 0.008, 0.002])
diff --git a/r10v2.txt b/r10v2.txt
new file mode 100644
index 0000000..657da7b
--- /dev/null
+++ b/r10v2.txt
@@ -0,0 +1,21 @@
           1 +0 (True, 125, 10, 92.02314901351929)
           2 +1 (True, 119, 10, 62.70379590988159)
           3 +2 (True, 93, 10, 62.281108140945435)
           4 +3 (True, 78, 10, 45.84531331062317)
           5 +4 (True, 145, 10, 90.09482216835022)
           6 +5 (True, 114, 10, 67.0106029510498)
           7 +6 (True, 108, 10, 75.81399321556091)
           8 +7 (True, 160, 10, 106.01211953163147)
           9 +8 (True, 123, 10, 85.66822290420532)
          10 +9 (True, 87, 10, 60.09585905075073)
          11 +10 (True, 100, 10, 71.18115091323853)
          12 +11 (True, 100, 10, 66.59610366821289)
          13 +12 (True, 104, 10, 72.33428025245667)
          14 +13 (True, 135, 10, 80.5737771987915)
          15 +14 (True, 110, 10, 64.405433177948)
          16 +15 (True, 135, 10, 63.66275906562805)
          17 +16 (True, 96, 10, 49.53244614601135)
          18 +17 (True, 75, 10, 35.380539655685425)
          19 +18 (True, 103, 10, 32.827847719192505)
          20 +19 (True, 88, 10, 25.02454948425293)
          21 +success 20 / 20 mean steps 109.9 max time 106.01211953163147
diff --git a/r7v2.txt b/r7v2.txt
new file mode 100644
index 0000000..68f3674
--- /dev/null
+++ b/r7v2.txt
@@ -0,0 +1,30 @@
           1 +0 (True, 98, 7, 54.41223621368408)
           2 +1 (True, 104, 7, 75.31856060028076)
           3 +2 (True, 74, 7, 49.93993282318115)
           4 +3 (True, 77, 7, 52.8530216217041)
           5 +4 (False, 1000, 7, 218.94374346733093)
           6 +5 (True, 114, 7, 86.38529539108276)
           7 +6 (True, 106, 7, 64.2974042892456)
           8 +7 (True, 122, 7, 79.57644891738892)
           9 +8 (True, 85, 7, 54.00593376159668)
          10 +9 (True, 87, 7, 56.628342151641846)
          11 +10 (True, 69, 7, 46.50450921058655)
          12 +11 (True, 76, 7, 51.43114638328552)
          13 +12 (True, 107, 7, 67.82582974433899)
          14 +13 (True, 129, 7, 91.70317268371582)
          15 +14 (True, 61, 7, 38.008939027786255)
          16 +15 (True, 119, 7, 93.79446053504944)
          17 +16 (True, 62, 7, 38.62404942512512)
          18 +17 (True, 75, 7, 46.38465428352356)
          19 +18 (True, 92, 7, 57.090057134628296)
          20 +19 (True, 88, 7, 58.803157567977905)
          21 +20 (True, 95, 7, 62.33549380302429)
          22 +21 (True, 109, 7, 74.3672263622284)
          23 +22 (True, 76, 7, 49.72415852546692)
          24 +23 (True, 107, 7, 64.89277505874634)
          25 +24 (True, 77, 7, 46.78782272338867)
          26 +25 (True, 49, 7, 36.578845500946045)
          27 +26 (True, 69, 7, 36.91229772567749)
          28 +27 (True, 71, 7, 33.56934118270874)
          29 +28 (True, 103, 7, 28.971372842788696)
          30 +success 29 / 30 mean steps 88.51724137931035 max time 218.94374346733093
```

</details>

<a id="C014"></a>
### C014 · IK: clamp to joint limits

Commit `260fcb1d0181db34d71caa2a8373b3cb408cdf45`; parents: 872a421dc785b10113a2b6c3e0b1fc9167491cec. Recorded author date: 2026-09-30T22:10:57+02:00.

File roles (automatic): support code (role needs review).

- [E0591](01_timeline.md#E0591): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C014_260fcb1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index 47390c4..a55dc27 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -112,7 +112,7 @@ class GeneratedApproach:
  112    112              qs = np.array(q0, dtype=float)
  113    113              if attempt > 0:
  114    114                  qs = qs + self.rng.uniform(-0.4, 0.4, 7)
  115        -            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=100, tol=1e-5)
         115 +            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=100, tol=1e-5, lim=JLIM - 0.02)
  116    116              if ok and np.all(np.abs(q) <= JLIM):
  117    117                  return q, True
  118    118              if best is None:
diff --git a/kin.py b/kin.py
index c2d8575..e62d77e 100644
--- a/kin.py
+++ b/kin.py
@@ -59,7 +59,7 @@ def topdown_R(yaw):
   59     59      Rz = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
   60     60      return Rz @ np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1.0]])
   61     61  
   62        -def ik(base, q0, p, R, iters=200, tol=1e-4, wrot=0.5, tool=None, base_z=None):
          62 +def ik(base, q0, p, R, iters=200, tol=1e-4, wrot=0.5, tool=None, base_z=None, lim=None):
   63     63      q = np.array(q0, dtype=float)
   64     64      for it in range(iters):
   65     65          T = fk(base, q, tool, base_z)
@@ -77,4 +77,6 @@ def ik(base, q0, p, R, iters=200, tol=1e-4, wrot=0.5, tool=None, base_z=None):
   77     77          n = np.linalg.norm(dq)
   78     78          if n > 0.3: dq *= 0.3 / n
   79     79          q += dq
          80 +        if lim is not None:
          81 +            q = np.clip(q, -lim, lim)
   80     82      return q, False
```

</details>

<a id="C015"></a>
### C015 · denser cartesian waypoints

Commit `32c237a0fed384f71b1317eb942860348974f324`; parents: 260fcb1d0181db34d71caa2a8373b3cb408cdf45. Recorded author date: 2026-09-30T22:12:12+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0614](01_timeline.md#E0614): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C015_32c237a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index a55dc27..82ba011 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -339,11 +339,11 @@ class GeneratedApproach:
  339    339              q = q0
  340    340              plan = []
  341    341              if p0[2] < zt - 0.005:
  342        -                qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.05)
         342 +                qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.015)
  343    343                  plan += self._seg(qs)
  344        -            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.08, R_from=T[:3, :3])
         344 +            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.04, R_from=T[:3, :3])
  345    345              plan += self._seg(qs)
  346        -            qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.05)
         346 +            qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.015)
  347    347              plan += self._seg(qs)
  348    348              plan += [('grip', -1.0), ('check', 'grasp')]
  349    349              c = self._plan_cost(q0, plan) + (0 if (ok1 and ok2) else 100)
@@ -440,11 +440,11 @@ class GeneratedApproach:
  440    440                  p0 = p1
  441    441              up = np.array([p0[0], p0[1], lift_z])
  442    442              above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
  443        -            qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
         443 +            qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.015)
  444    444              plan += self._seg(qs)
  445        -            qs, q, _ = self._cart_path(q, up, above, R, step=0.08, R_from=T[:3, :3])
         445 +            qs, q, _ = self._cart_path(q, up, above, R, step=0.04, R_from=T[:3, :3])
  446    446              plan += self._seg(qs)
  447        -            qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.05)
         447 +            qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.015)
  448    448              plan += self._seg(qs)
  449    449              plan += [('grip', 1.0), ('check', 'release')]
  450    450              c = self._plan_cost(q_init, plan)
@@ -495,7 +495,7 @@ class GeneratedApproach:
  495    495          q = self._q(state)
  496    496          T = self._tool(q)
  497    497          p0 = T[:3, 3]
  498        -        qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], max(p0[2] + 0.03, Z_SAFE)]), T[:3, :3], step=0.05)
         498 +        qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], max(p0[2] + 0.03, Z_SAFE)]), T[:3, :3], step=0.015)
  499    499          self.plan = self._seg(qs)
  500    500  
  501    501      # ---------------------------------------------------------------- acting
diff --git a/probe4.py b/probe4.py
new file mode 100644
index 0000000..c21b1c8
--- /dev/null
+++ b/probe4.py
@@ -0,0 +1,27 @@
           1 +import sys, numpy as np, kin, os, importlib as _il
           2 +from env_client import make_env
           3 +from common import *
           4 +GA = _il.import_module("approach_v2").GeneratedApproach
           5 +env = make_env()
           6 +obs, info = env.reset(seed=4, options={'object_count': 7})
           7 +ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +for t in range(44):
           9 +    obs, *_ = env.step(ap.get_action(obs))
          10 +print('grasp', obs.get(robot(obs),'grasp_active'))
          11 +for n in sorted(obs.get_object_names()):
          12 +    try: d=objd(obs,n); print(n, round(d['pose_x'],3), round(d['pose_y'],3), round(d['pose_z'],3), round(d['half_extent_x'],3), round(d['half_extent_y'],3), round(d['half_extent_z'],3))
          13 +    except Exception: pass
          14 +q0=getq(obs); T=kin.fk(getbase(obs), q0); print('tool', T[:3,3])
          15 +import pickle
          16 +for dv in [(0,0,0.003),(0,0,0.01),(0.003,0,0),(-0.003,0,0),(0,0.003,0),(0,-0.003,0),(0.008,0,0.002)]:
          17 +    q,ok=kin.ik(getbase(obs), q0, T[:3,3]+np.array(dv), T[:3,:3], iters=100, tol=1e-6)
          18 +    o2,bl=move_to(env, obs, q, grip=0.0)
          19 +    print(dv, 'blocked', bl, 'dq', np.round(q-q0,3))
          20 +    if not bl: obs,_=move_to(env,o2,q0)
          21 +print('--- incremental lift')
          22 +q=q0
          23 +for k in range(1,10):
          24 +    q,ok=kin.ik(getbase(obs), q, T[:3,3]+np.array([0,0,0.005*k]), T[:3,:3], iters=100, tol=1e-6)
          25 +    obs,bl=move_to(env, obs, q, grip=0.0)
          26 +    print(k, 'blocked', bl, np.round(kin.fk(getbase(obs), getq(obs))[:3,3],3), 'objz', round(objd(obs,'obstruction1')['pose_z'],3))
          27 +    if bl: break
```

</details>

<a id="C016"></a>
### C016 · escape: search dist+dir for clearance, slow lift when tight

Commit `64cb9b19f2b84f1ff1f4c7c1a6864809efbbe38b`; parents: 32c237a0fed384f71b1317eb942860348974f324. Recorded author date: 2026-09-30T22:14:47+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0630](01_timeline.md#E0630): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C016_64cb9b1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index 82ba011..50cdb85 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -427,17 +427,23 @@ class GeneratedApproach:
  427    427                  for k in range(16):
  428    428                      ang = 2 * np.pi * k / 16
  429    429                      d = np.array([np.cos(ang), np.sin(ang)])
  430        -                    sep = min([np.max(np.abs(o.p[:2] + 0.008 * d - b.p[:2]) - (Ho + b.footprint())) for b in nbrs] + [1.0])
  431        -                    opts.append((-min(sep, 0.004) - 0.0005 * float(d @ e), k, d))
         430 +                    for dist in (0.003, 0.005, 0.008, 0.012):
         431 +                        sep = min([np.max(np.abs(o.p[:2] + dist * d - b.p[:2]) - (Ho + b.footprint())) for b in nbrs] + [1.0])
         432 +                        opts.append((-min(sep, 0.005) + 0.05 * dist, k, d * dist, sep))
  432    433                  opts.sort(key=lambda t: t[0])
  433    434                  nf = self.fail_count.get(name, 0)
  434        -                e = opts[nf % len(opts)][2]
  435        -            if np.linalg.norm(e) > 0:
  436        -                e = e / np.linalg.norm(e)
  437        -                p1 = p0 + np.array([e[0] * 0.008, e[1] * 0.008, 0.002])
  438        -                qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.01)
         435 +                pick = opts[nf % len(opts)]
         436 +                ev = pick[2]
         437 +                p1 = p0 + np.array([ev[0], ev[1], 0.002])
         438 +                qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.004)
  439    439                  plan += self._seg(qs)
  440    440                  p0 = p1
         441 +                if pick[3] < 0.004 or nf > 0:
         442 +                    for k in range(3):
         443 +                        p1 = p0 + np.array([0, 0, 0.008])
         444 +                        qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.004)
         445 +                        plan += self._seg(qs)
         446 +                        p0 = p1
  441    447              up = np.array([p0[0], p0[1], lift_z])
  442    448              above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
  443    449              qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.015)
diff --git a/probe5.py b/probe5.py
new file mode 100644
index 0000000..85a4626
--- /dev/null
+++ b/probe5.py
@@ -0,0 +1,17 @@
           1 +import sys, numpy as np, kin, importlib as _il
           2 +from env_client import make_env
           3 +from common import *
           4 +GA = _il.import_module("approach_v2").GeneratedApproach
           5 +env = make_env()
           6 +obs, info = env.reset(seed=4, options={'object_count': 7})
           7 +ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +for t in range(45):
           9 +    obs, *_ = env.step(ap.get_action(obs))
          10 +q0=getq(obs); b=getbase(obs); T=kin.fk(b, q0); print('tool', T[:3,3], 'grasp', obs.get(robot(obs),'grasp_active'))
          11 +tgt=ap._lookahead(q0); print('lookahead target tool', kin.fk(b,tgt)[:3,3], 'dq', np.round(tgt-q0,3))
          12 +for dz in [0.01,0.02,0.03,0.04]:
          13 +    q=q0
          14 +    for k in range(10): q,ok=kin.ik(b, q, T[:3,3]+np.array([0,0,dz*(k+1)/10]), T[:3,:3], iters=100, tol=1e-7)
          15 +    o2,bl=move_to(env, obs, q, grip=0.0, maxd=0.2)
          16 +    print(dz,'blocked',bl, 'dqmax', np.abs(q-q0).max())
          17 +    if not bl: obs,_=move_to(env,o2,q0)
```

</details>

<a id="C017"></a>
### C017 · Promote v2 with escape/IK fixes: 100/100 mean 32.8

Commit `3fc7f32929ce6d38fc6c9c029245c48b57b00737`; parents: 64cb9b19f2b84f1ff1f4c7c1a6864809efbbe38b. Recorded author date: 2026-09-30T22:25:04+02:00.

File roles (automatic): policy, setup/other.

- [E0675](01_timeline.md#E0675): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_3fc7f32_approach.py) · [Exact all-file diff](evidence/diffs/C017_3fc7f32.diff)

[Previous saved controller snapshot](evidence/versions/C012_d07733f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4578392..50cdb85 100644
--- a/approach.py
+++ b/approach.py
@@ -112,7 +112,7 @@ class GeneratedApproach:
  112    112              qs = np.array(q0, dtype=float)
  113    113              if attempt > 0:
  114    114                  qs = qs + self.rng.uniform(-0.4, 0.4, 7)
  115        -            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=100, tol=1e-5)
         115 +            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=100, tol=1e-5, lim=JLIM - 0.02)
  116    116              if ok and np.all(np.abs(q) <= JLIM):
  117    117                  return q, True
  118    118              if best is None:
@@ -339,11 +339,11 @@ class GeneratedApproach:
  339    339              q = q0
  340    340              plan = []
  341    341              if p0[2] < zt - 0.005:
  342        -                qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.05)
         342 +                qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.015)
  343    343                  plan += self._seg(qs)
  344        -            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.08, R_from=T[:3, :3])
         344 +            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.04, R_from=T[:3, :3])
  345    345              plan += self._seg(qs)
  346        -            qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.05)
         346 +            qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.015)
  347    347              plan += self._seg(qs)
  348    348              plan += [('grip', -1.0), ('check', 'grasp')]
  349    349              c = self._plan_cost(q0, plan) + (0 if (ok1 and ok2) else 100)
@@ -407,6 +407,7 @@ class GeneratedApproach:
  407    407              plan = []
  408    408              # escape laterally from touching neighbours before lifting
  409    409              e = np.zeros(2)
         410 +            touch = False
  410    411              Ho = o.footprint()
  411    412              for n, b in objs.items():
  412    413                  if n == name or b.top <= o.bottom + 2e-3 or b.bottom >= o.top - 2e-3:
@@ -419,24 +420,37 @@ class GeneratedApproach:
  419    420                      v = np.zeros(2)
  420    421                      v[ax] = np.sign(dxy[ax]) if dxy[ax] != 0 else 1.0
  421    422                      e += v
  422        -            nf = self.fail_count.get(name, 0)
  423        -            if nf > 0 and np.linalg.norm(e) > 0:
  424        -                ang = [0, 0.6, -0.6, 1.2, -1.2][nf % 5]
  425        -                c_, s_ = np.cos(ang), np.sin(ang)
  426        -                e = np.array([c_ * e[0] - s_ * e[1], s_ * e[0] + c_ * e[1]])
  427        -            if np.linalg.norm(e) > 0:
  428        -                e = e / np.linalg.norm(e)
  429        -                p1 = p0 + np.array([e[0] * 0.008, e[1] * 0.008, 0.002])
  430        -                qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.01)
         423 +                    touch = True
         424 +            if touch:
         425 +                nbrs = [b for n, b in objs.items() if n != name and b.top > o.bottom + 2e-3 and b.bottom < o.top - 2e-3]
         426 +                opts = []
         427 +                for k in range(16):
         428 +                    ang = 2 * np.pi * k / 16
         429 +                    d = np.array([np.cos(ang), np.sin(ang)])
         430 +                    for dist in (0.003, 0.005, 0.008, 0.012):
         431 +                        sep = min([np.max(np.abs(o.p[:2] + dist * d - b.p[:2]) - (Ho + b.footprint())) for b in nbrs] + [1.0])
         432 +                        opts.append((-min(sep, 0.005) + 0.05 * dist, k, d * dist, sep))
         433 +                opts.sort(key=lambda t: t[0])
         434 +                nf = self.fail_count.get(name, 0)
         435 +                pick = opts[nf % len(opts)]
         436 +                ev = pick[2]
         437 +                p1 = p0 + np.array([ev[0], ev[1], 0.002])
         438 +                qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.004)
  431    439                  plan += self._seg(qs)
  432    440                  p0 = p1
         441 +                if pick[3] < 0.004 or nf > 0:
         442 +                    for k in range(3):
         443 +                        p1 = p0 + np.array([0, 0, 0.008])
         444 +                        qs, q, _ = self._cart_path(q, p0, p1, T[:3, :3], step=0.004)
         445 +                        plan += self._seg(qs)
         446 +                        p0 = p1
  433    447              up = np.array([p0[0], p0[1], lift_z])
  434    448              above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
  435        -            qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
         449 +            qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.015)
  436    450              plan += self._seg(qs)
  437        -            qs, q, _ = self._cart_path(q, up, above, R, step=0.08, R_from=T[:3, :3])
         451 +            qs, q, _ = self._cart_path(q, up, above, R, step=0.04, R_from=T[:3, :3])
  438    452              plan += self._seg(qs)
  439        -            qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.05)
         453 +            qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.015)
  440    454              plan += self._seg(qs)
  441    455              plan += [('grip', 1.0), ('check', 'release')]
  442    456              c = self._plan_cost(q_init, plan)
@@ -487,7 +501,7 @@ class GeneratedApproach:
  487    501          q = self._q(state)
  488    502          T = self._tool(q)
  489    503          p0 = T[:3, 3]
  490        -        qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], max(p0[2] + 0.03, Z_SAFE)]), T[:3, :3], step=0.05)
         504 +        qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], max(p0[2] + 0.03, Z_SAFE)]), T[:3, :3], step=0.015)
  491    505          self.plan = self._seg(qs)
  492    506  
  493    507      # ---------------------------------------------------------------- acting
diff --git a/r7v2.txt b/r7v2.txt
index 68f3674..e69de29 100644
--- a/r7v2.txt
+++ b/r7v2.txt
@@ -1,30 +0,0 @@
    1        -0 (True, 98, 7, 54.41223621368408)
    2        -1 (True, 104, 7, 75.31856060028076)
    3        -2 (True, 74, 7, 49.93993282318115)
    4        -3 (True, 77, 7, 52.8530216217041)
    5        -4 (False, 1000, 7, 218.94374346733093)
    6        -5 (True, 114, 7, 86.38529539108276)
    7        -6 (True, 106, 7, 64.2974042892456)
    8        -7 (True, 122, 7, 79.57644891738892)
    9        -8 (True, 85, 7, 54.00593376159668)
   10        -9 (True, 87, 7, 56.628342151641846)
   11        -10 (True, 69, 7, 46.50450921058655)
   12        -11 (True, 76, 7, 51.43114638328552)
   13        -12 (True, 107, 7, 67.82582974433899)
   14        -13 (True, 129, 7, 91.70317268371582)
   15        -14 (True, 61, 7, 38.008939027786255)
   16        -15 (True, 119, 7, 93.79446053504944)
   17        -16 (True, 62, 7, 38.62404942512512)
   18        -17 (True, 75, 7, 46.38465428352356)
   19        -18 (True, 92, 7, 57.090057134628296)
   20        -19 (True, 88, 7, 58.803157567977905)
   21        -20 (True, 95, 7, 62.33549380302429)
   22        -21 (True, 109, 7, 74.3672263622284)
   23        -22 (True, 76, 7, 49.72415852546692)
   24        -23 (True, 107, 7, 64.89277505874634)
   25        -24 (True, 77, 7, 46.78782272338867)
   26        -25 (True, 49, 7, 36.578845500946045)
   27        -26 (True, 69, 7, 36.91229772567749)
   28        -27 (True, 71, 7, 33.56934118270874)
   29        -28 (True, 103, 7, 28.971372842788696)
   30        -success 29 / 30 mean steps 88.51724137931035 max time 218.94374346733093
diff --git a/rdv2.txt b/rdv2.txt
new file mode 100644
index 0000000..2ed1bf5
--- /dev/null
+++ b/rdv2.txt
@@ -0,0 +1,72 @@
           1 +0 (True, 49, 2, 44.65753626823425)
           2 +1 (True, 38, 1, 21.186123609542847)
           3 +2 (True, 66, 2, 57.75160527229309)
           4 +4 (True, 59, 2, 50.24415946006775)
           5 +5 (True, 53, 2, 46.16478967666626)
           6 +6 (True, 37, 1, 20.326173543930054)
           7 +7 (True, 39, 2, 26.76628804206848)
           8 +8 (True, 43, 2, 43.95758414268494)
           9 +9 (True, 25, 1, 21.770167589187622)
          10 +10 (True, 28, 2, 29.55744743347168)
          11 +12 (True, 32, 1, 29.08803963661194)
          12 +13 (True, 41, 2, 39.67139220237732)
          13 +15 (True, 29, 2, 26.388429641723633)
          14 +16 (True, 27, 1, 23.87075400352478)
          15 +17 (True, 45, 2, 54.42944002151489)
          16 +18 (True, 38, 2, 37.27797603607178)
          17 +19 (True, 27, 1, 24.010403633117676)
          18 +20 (True, 55, 2, 60.94573783874512)
          19 +21 (True, 21, 0, 22.378713130950928)
          20 +22 (True, 30, 2, 32.95614266395569)
          21 +25 (True, 36, 1, 36.96371579170227)
          22 +26 (True, 33, 2, 34.67341351509094)
          23 +27 (True, 25, 0, 24.828604221343994)
          24 +28 (True, 49, 1, 51.44413161277771)
          25 +31 (True, 39, 1, 32.03095841407776)
          26 +32 (True, 47, 2, 58.34464073181152)
          27 +33 (True, 45, 2, 62.76429796218872)
          28 +36 (True, 24, 1, 29.247500896453857)
          29 +38 (True, 15, 0, 23.458435535430908)
          30 +39 (True, 45, 2, 52.62647604942322)
          31 +40 (True, 75, 1, 96.66923713684082)
          32 +41 (True, 29, 1, 28.586360931396484)
          33 +43 (True, 26, 1, 22.42523980140686)
          34 +44 (True, 30, 2, 36.01871132850647)
          35 +45 (True, 44, 2, 46.51904630661011)
          36 +46 (True, 26, 1, 31.43686842918396)
          37 +50 (True, 46, 2, 40.128849029541016)
          38 +51 (True, 29, 1, 27.790140867233276)
          39 +52 (True, 64, 2, 70.9896650314331)
          40 +53 (True, 44, 2, 46.5516517162323)
          41 +55 (True, 56, 2, 57.09167718887329)
          42 +58 (True, 21, 1, 25.080037832260132)
          43 +59 (True, 55, 2, 71.23579120635986)
          44 +61 (True, 30, 1, 30.14669418334961)
          45 +62 (True, 29, 1, 34.10112380981445)
          46 +63 (True, 27, 1, 24.44920825958252)
          47 +64 (True, 32, 1, 32.68348264694214)
          48 +65 (True, 27, 0, 26.728271961212158)
          49 +66 (True, 41, 2, 43.42152118682861)
          50 +67 (True, 48, 2, 57.42696690559387)
          51 +70 (True, 35, 1, 37.85807991027832)
          52 +71 (True, 52, 2, 56.0893611907959)
          53 +72 (True, 51, 2, 60.09363770484924)
          54 +73 (True, 37, 2, 35.012733697891235)
          55 +75 (True, 26, 1, 27.053276538848877)
          56 +76 (True, 40, 1, 40.37609887123108)
          57 +78 (True, 28, 2, 24.771350860595703)
          58 +80 (True, 39, 2, 45.06876516342163)
          59 +82 (True, 39, 2, 34.693543434143066)
          60 +83 (True, 29, 2, 30.512681484222412)
          61 +85 (True, 44, 2, 44.677146911621094)
          62 +86 (True, 45, 2, 46.307608127593994)
          63 +87 (True, 37, 1, 31.606425762176514)
          64 +88 (True, 30, 1, 23.946342706680298)
          65 +89 (True, 54, 2, 48.46833086013794)
          66 +90 (True, 27, 1, 22.381341695785522)
          67 +91 (True, 32, 2, 33.97594165802002)
          68 +92 (True, 28, 1, 22.89961051940918)
          69 +93 (True, 43, 2, 31.299214601516724)
          70 +95 (True, 33, 1, 21.54423999786377)
          71 +96 (True, 47, 2, 21.919421434402466)
          72 +success 100 / 100 mean steps 32.78 max time 96.66923713684082
```

</details>

<a id="C018"></a>
### C018 · kin: analytic Jacobian for IK (faster)

Commit `3a575890db10cac63344b8cc4fc1064bed85fb18`; parents: 3fc7f32929ce6d38fc6c9c029245c48b57b00737. Recorded author date: 2026-09-30T22:36:32+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E0707](01_timeline.md#E0707): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C018_3a57589.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/kin.py b/kin.py
index e62d77e..4de5f7f 100644
--- a/kin.py
+++ b/kin.py
@@ -40,6 +40,27 @@ def fk(base, q, tool=None, base_z=None):
   40     40      Tt = np.eye(4); Tt[2, 3] = tool
   41     41      return T @ Tt
   42     42  
          43 +def fk_jac(base, q, tool=None, base_z=None):
          44 +    tool = TOOL if tool is None else tool
          45 +    base_z = BASE_Z if base_z is None else base_z
          46 +    T = np.eye(4)
          47 +    T[:3, :3] = rpy_mat(0, 0, base[2]); T[:3, 3] = [base[0], base[1], base_z]
          48 +    M = np.eye(4); M[0, 3] = MOUNT_X; T = T @ M
          49 +    axes = []; origins = []
          50 +    for J, qi in zip(JOINTS, q):
          51 +        T = T @ J
          52 +        axes.append(T[:3, 2].copy()); origins.append(T[:3, 3].copy())
          53 +        T = T @ rotz(qi)
          54 +    T = T @ EE
          55 +    Tt = np.eye(4); Tt[2, 3] = tool
          56 +    T = T @ Tt
          57 +    p = T[:3, 3]
          58 +    Jm = np.zeros((6, 7))
          59 +    for i in range(7):
          60 +        Jm[:3, i] = np.cross(axes[i], p - origins[i])
          61 +        Jm[3:, i] = axes[i]
          62 +    return T, Jm
          63 +
   43     64  def rot_err(Rc, Rt):
   44     65      Re = Rt @ Rc.T
   45     66      # axis-angle vector
@@ -62,16 +83,11 @@ def topdown_R(yaw):
   62     83  def ik(base, q0, p, R, iters=200, tol=1e-4, wrot=0.5, tool=None, base_z=None, lim=None):
   63     84      q = np.array(q0, dtype=float)
   64     85      for it in range(iters):
   65        -        T = fk(base, q, tool, base_z)
          86 +        T, J = fk_jac(base, q, tool, base_z)
          87 +        J[3:] *= wrot
   66     88          e = np.concatenate([p - T[:3, 3], wrot * rot_err(T[:3, :3], R)])
   67     89          if np.linalg.norm(e) < tol:
   68     90              return q, True
   69        -        J = np.zeros((6, 7))
   70        -        for i in range(7):
   71        -            dq = q.copy(); dq[i] += 1e-5
   72        -            Td = fk(base, dq, tool, base_z)
   73        -            J[:3, i] = (Td[:3, 3] - T[:3, 3]) / 1e-5
   74        -            J[3:, i] = wrot * rot_err(T[:3, :3], Td[:3, :3]) / 1e-5
   75     91          lam = 1e-3
   76     92          dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
   77     93          n = np.linalg.norm(dq)
diff --git a/r10v2.txt b/r10v2.txt
index 657da7b..87b0071 100644
--- a/r10v2.txt
+++ b/r10v2.txt
@@ -1,21 +1,21 @@
    1        -0 (True, 125, 10, 92.02314901351929)
    2        -1 (True, 119, 10, 62.70379590988159)
    3        -2 (True, 93, 10, 62.281108140945435)
    4        -3 (True, 78, 10, 45.84531331062317)
    5        -4 (True, 145, 10, 90.09482216835022)
    6        -5 (True, 114, 10, 67.0106029510498)
    7        -6 (True, 108, 10, 75.81399321556091)
    8        -7 (True, 160, 10, 106.01211953163147)
    9        -8 (True, 123, 10, 85.66822290420532)
   10        -9 (True, 87, 10, 60.09585905075073)
   11        -10 (True, 100, 10, 71.18115091323853)
   12        -11 (True, 100, 10, 66.59610366821289)
   13        -12 (True, 104, 10, 72.33428025245667)
   14        -13 (True, 135, 10, 80.5737771987915)
   15        -14 (True, 110, 10, 64.405433177948)
   16        -15 (True, 135, 10, 63.66275906562805)
   17        -16 (True, 96, 10, 49.53244614601135)
   18        -17 (True, 75, 10, 35.380539655685425)
   19        -18 (True, 103, 10, 32.827847719192505)
   20        -19 (True, 88, 10, 25.02454948425293)
   21        -success 20 / 20 mean steps 109.9 max time 106.01211953163147
           1 +0 (True, 125, 10, 104.89492058753967)
           2 +1 (True, 119, 10, 77.4553337097168)
           3 +2 (True, 93, 10, 57.68733549118042)
           4 +3 (True, 78, 10, 45.96848201751709)
           5 +4 (True, 133, 10, 91.54850959777832)
           6 +5 (True, 114, 10, 61.649073362350464)
           7 +6 (True, 108, 10, 69.97951006889343)
           8 +7 (True, 161, 10, 111.96945834159851)
           9 +8 (True, 123, 10, 103.88562154769897)
          10 +9 (True, 87, 10, 74.52696228027344)
          11 +10 (True, 102, 10, 82.24074697494507)
          12 +11 (True, 96, 10, 74.87361359596252)
          13 +12 (True, 102, 10, 83.29399371147156)
          14 +13 (True, 136, 10, 93.86978816986084)
          15 +14 (True, 110, 10, 71.97742629051208)
          16 +15 (True, 132, 10, 69.7938084602356)
          17 +16 (True, 97, 10, 54.36871552467346)
          18 +17 (True, 76, 10, 31.4574453830719)
          19 +18 (True, 103, 10, 38.24239134788513)
          20 +19 (True, 84, 10, 30.301987886428833)
          21 +success 20 / 20 mean steps 108.95 max time 111.96945834159851
diff --git a/r7v2.txt b/r7v2.txt
index e69de29..f4e3098 100644
--- a/r7v2.txt
+++ b/r7v2.txt
@@ -0,0 +1,31 @@
           1 +0 (True, 94, 7, 63.02361559867859)
           2 +1 (True, 104, 7, 74.47821474075317)
           3 +2 (True, 73, 7, 35.02347707748413)
           4 +3 (True, 77, 7, 27.969908952713013)
           5 +4 (True, 132, 7, 80.5042507648468)
           6 +5 (True, 114, 7, 78.19307494163513)
           7 +6 (True, 106, 7, 63.46646475791931)
           8 +7 (True, 123, 7, 72.65765714645386)
           9 +8 (True, 85, 7, 61.07735204696655)
          10 +9 (True, 87, 7, 67.08360195159912)
          11 +10 (True, 69, 7, 52.144341707229614)
          12 +11 (True, 80, 7, 58.64270758628845)
          13 +12 (True, 104, 7, 74.42161846160889)
          14 +13 (True, 131, 7, 99.624183177948)
          15 +14 (True, 61, 7, 43.49214029312134)
          16 +15 (True, 120, 7, 94.21526288986206)
          17 +16 (True, 62, 7, 43.739404916763306)
          18 +17 (True, 76, 7, 49.73142123222351)
          19 +18 (True, 92, 7, 68.14324593544006)
          20 +19 (True, 84, 7, 53.11684465408325)
          21 +20 (True, 93, 7, 66.39607453346252)
          22 +21 (True, 107, 7, 79.70174717903137)
          23 +22 (True, 76, 7, 56.05203819274902)
          24 +23 (True, 104, 7, 67.88577699661255)
          25 +24 (True, 78, 7, 52.187477827072144)
          26 +25 (True, 49, 7, 40.90671944618225)
          27 +26 (True, 69, 7, 43.35073471069336)
          28 +27 (True, 71, 7, 40.220239877700806)
          29 +28 (True, 103, 7, 36.82794904708862)
          30 +29 (True, 65, 7, 21.46721839904785)
          31 +success 30 / 30 mean steps 89.63333333333334 max time 99.624183177948
```

</details>

<a id="C019"></a>
### C019 · ban failed free spots, avoid spots near robot base

Commit `c5d528bebc38b642d04e96097eae2bd0e05723e0`; parents: 3a575890db10cac63344b8cc4fc1064bed85fb18. Recorded author date: 2026-09-30T23:08:34+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E0861](01_timeline.md#E0861): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C019_c5d528b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index 50cdb85..b9b6ae8 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -237,6 +237,8 @@ class GeneratedApproach:
  237    237          self.blocked = 0
  238    238          self.last_q = None
  239    239          self.fail_count = {}
         240 +        self.bad_spots = []
         241 +        self.last_spot = None
  240    242          self.steps = 0
  241    243          self.plans_made = 0
  242    244          self.aborting = False
@@ -358,7 +360,9 @@ class GeneratedApproach:
  358    360          for x in np.arange(TABLE_X[0] + fp[0], TABLE_X[1] - fp[0], 0.02):
  359    361              for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
  360    362                  p = np.array([x, y])
  361        -                cost = np.linalg.norm(p - cur)
         363 +                cost = np.linalg.norm(p - cur) + 2.0 * max(0.0, 0.2 - x)
         364 +                if any(np.linalg.norm(p - bs) < 0.035 for bs in self.bad_spots):
         365 +                    continue
  362    366                  if best is not None and cost >= best[0]:
  363    367                      continue
  364    368                  ok = True
@@ -475,6 +479,7 @@ class GeneratedApproach:
  475    479              clear = self._to_clear(objs)
  476    480              reg = objs['target_region']
  477    481              if held == 'target_block' and not clear:
         482 +                self.last_spot = None
  478    483                  self._plan_place(state, held, reg.p[:2], reg.top, reg.yaw)
  479    484                  return
  480    485              G = self._G(state)
@@ -483,6 +488,7 @@ class GeneratedApproach:
  483    488              spot = self._free_spot(o, objs, tool_yaw)
  484    489              if spot is None:
  485    490                  spot = o.p[:2]
         491 +            self.last_spot = np.array(spot, float)
  486    492              self._plan_place(state, held, spot, TABLE_TOP, o.yaw)
  487    493              return
  488    494          best = self._pick_target(objs)
@@ -498,6 +504,8 @@ class GeneratedApproach:
  498    504      def _abort(self, state):
  499    505          """blocked: retreat straight up and replan."""
  500    506          self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
         507 +        if self.last_spot is not None and float(state.get(self.robot, 'grasp_active')) > 0.5:
         508 +            self.bad_spots.append(self.last_spot)
  501    509          q = self._q(state)
  502    510          T = self._tool(q)
  503    511          p0 = T[:3, 3]
diff --git a/prof.out b/prof.out
new file mode 100644
index 0000000..178365c
Binary files /dev/null and b/prof.out differ
diff --git a/r5.txt b/r5.txt
new file mode 100644
index 0000000..9347869
--- /dev/null
+++ b/r5.txt
@@ -0,0 +1,40 @@
           1 +100 (True, 83, 5, 68.87982869148254)
           2 +101 (True, 80, 5, 64.18197226524353)
           3 +102 (True, 86, 5, 55.62192964553833)
           4 +103 (True, 77, 5, 52.37706136703491)
           5 +104 (True, 107, 5, 77.28409624099731)
           6 +105 (True, 110, 5, 72.21367406845093)
           7 +106 (True, 73, 5, 35.45598363876343)
           8 +107 (True, 76, 5, 40.679455518722534)
           9 +108 (True, 83, 5, 70.51313543319702)
          10 +109 (True, 65, 5, 47.495038986206055)
          11 +110 (True, 72, 5, 55.85311222076416)
          12 +111 (True, 63, 5, 38.5626277923584)
          13 +112 (True, 82, 5, 61.37686777114868)
          14 +113 (True, 55, 5, 36.607900857925415)
          15 +114 (True, 64, 5, 50.68066644668579)
          16 +115 (True, 79, 5, 58.63892126083374)
          17 +116 (True, 41, 5, 34.451783180236816)
          18 +117 (True, 65, 5, 50.0734498500824)
          19 +118 (True, 96, 5, 70.97689318656921)
          20 +119 (True, 159, 5, 115.19384932518005)
          21 +120 (True, 73, 5, 49.841267585754395)
          22 +121 (True, 58, 5, 36.669119358062744)
          23 +122 (True, 89, 5, 61.55817675590515)
          24 +123 (True, 79, 5, 49.93154764175415)
          25 +124 (True, 70, 5, 43.622206687927246)
          26 +125 (True, 101, 5, 70.2533872127533)
          27 +126 (True, 63, 5, 43.62159967422485)
          28 +127 (True, 62, 5, 42.425272703170776)
          29 +128 (True, 79, 5, 58.76544165611267)
          30 +129 (True, 54, 5, 38.84026217460632)
          31 +130 (True, 83, 5, 54.70195508003235)
          32 +131 (True, 83, 5, 56.90645670890808)
          33 +132 (True, 58, 5, 43.307849645614624)
          34 +133 (True, 95, 5, 54.35956311225891)
          35 +134 (True, 53, 5, 38.22305607795715)
          36 +135 (True, 53, 5, 34.75531601905823)
          37 +136 (True, 39, 5, 27.096501111984253)
          38 +137 (True, 85, 5, 31.31410527229309)
          39 +138 (True, 76, 5, 22.44727325439453)
          40 +success 40 / 40 mean steps 76.25 max time 115.19384932518005
diff --git a/r9.txt b/r9.txt
new file mode 100644
index 0000000..bf5cddd
--- /dev/null
+++ b/r9.txt
@@ -0,0 +1,30 @@
           1 +100 (True, 97, 9, 72.14916110038757)
           2 +101 (False, 1000, 9, 333.80482721328735)
           3 +102 (True, 112, 9, 69.812979221344)
           4 +103 (True, 93, 9, 52.81530427932739)
           5 +104 (True, 140, 9, 87.37922263145447)
           6 +105 (True, 126, 9, 92.62624502182007)
           7 +106 (True, 91, 9, 46.40775680541992)
           8 +107 (True, 112, 9, 65.06996464729309)
           9 +108 (True, 134, 9, 91.0637879371643)
          10 +109 (True, 97, 9, 61.19999670982361)
          11 +110 (True, 120, 9, 75.0379490852356)
          12 +111 (True, 63, 9, 33.855305910110474)
          13 +112 (True, 111, 9, 62.16018080711365)
          14 +113 (True, 80, 9, 41.73160791397095)
          15 +114 (True, 92, 9, 56.17422151565552)
          16 +115 (True, 97, 9, 59.20113825798035)
          17 +116 (True, 86, 9, 54.971293687820435)
          18 +117 (True, 109, 9, 64.36724352836609)
          19 +118 (True, 136, 9, 80.83306837081909)
          20 +119 (True, 200, 9, 115.20018124580383)
          21 +120 (True, 115, 9, 54.81230664253235)
          22 +121 (False, 1000, 9, 182.53349542617798)
          23 +122 (True, 120, 9, 69.95800018310547)
          24 +123 (True, 84, 9, 38.88550424575806)
          25 +124 (True, 104, 9, 58.44248819351196)
          26 +125 (True, 100, 9, 55.21132850646973)
          27 +126 (True, 78, 9, 40.50506377220154)
          28 +127 (True, 76, 9, 38.882683753967285)
          29 +128 (True, 80, 9, 29.606189250946045)
          30 +success 28 / 30 mean steps 104.42857142857143 max time 333.80482721328735
diff --git a/rd2.txt b/rd2.txt
new file mode 100644
index 0000000..0794252
--- /dev/null
+++ b/rd2.txt
@@ -0,0 +1,135 @@
           1 +100 (True, 44, 2, 60.69733548164368)
           2 +102 (True, 27, 1, 34.21727681159973)
           3 +103 (True, 29, 1, 30.70777940750122)
           4 +104 (True, 48, 2, 63.10523986816406)
           5 +106 (True, 21, 1, 23.18472671508789)
           6 +109 (True, 33, 1, 39.35402536392212)
           7 +110 (True, 36, 1, 52.44270038604736)
           8 +111 (True, 27, 1, 43.41111135482788)
           9 +115 (True, 32, 1, 47.17558169364929)
          10 +118 (True, 36, 1, 43.52399969100952)
          11 +119 (True, 45, 1, 57.201518297195435)
          12 +122 (True, 53, 2, 60.818546772003174)
          13 +124 (True, 28, 2, 27.578972816467285)
          14 +125 (True, 35, 1, 39.412720918655396)
          15 +128 (True, 48, 2, 41.23390603065491)
          16 +129 (True, 30, 1, 22.98597478866577)
          17 +130 (True, 52, 2, 54.61865782737732)
          18 +131 (True, 38, 1, 34.704601526260376)
          19 +132 (True, 37, 2, 33.48962473869324)
          20 +134 (True, 44, 2, 44.47883081436157)
          21 +135 (True, 28, 1, 27.007402896881104)
          22 +136 (True, 35, 2, 37.70830965042114)
          23 +137 (True, 33, 1, 31.274999618530273)
          24 +138 (True, 37, 1, 37.64542102813721)
          25 +139 (True, 35, 1, 40.6359384059906)
          26 +140 (True, 34, 1, 38.6769802570343)
          27 +141 (True, 28, 1, 24.113311290740967)
          28 +143 (True, 44, 2, 44.87544059753418)
          29 +144 (True, 21, 0, 32.12799286842346)
          30 +145 (True, 28, 1, 31.925946712493896)
          31 +146 (True, 30, 2, 33.271146297454834)
          32 +151 (True, 38, 2, 39.89956760406494)
          33 +152 (True, 48, 2, 50.72694730758667)
          34 +153 (True, 41, 2, 43.44120979309082)
          35 +156 (True, 50, 2, 49.0710072517395)
          36 +159 (True, 43, 2, 35.962141275405884)
          37 +160 (True, 21, 0, 22.315553665161133)
          38 +161 (True, 32, 2, 33.05754494667053)
          39 +162 (True, 32, 1, 31.399173259735107)
          40 +163 (True, 28, 1, 29.13721251487732)
          41 +164 (True, 27, 1, 27.67407512664795)
          42 +165 (True, 31, 1, 28.843706846237183)
          43 +166 (True, 55, 2, 46.8109986782074)
          44 +167 (True, 48, 2, 43.405439615249634)
          45 +168 (True, 29, 1, 23.4277126789093)
          46 +169 (True, 42, 2, 35.74074697494507)
          47 +170 (True, 47, 2, 39.15442419052124)
          48 +171 (True, 52, 2, 42.45587873458862)
          49 +173 (True, 42, 2, 36.678534269332886)
          50 +174 (True, 36, 1, 35.68039131164551)
          51 +175 (True, 27, 2, 27.53231954574585)
          52 +177 (True, 40, 2, 39.336809396743774)
          53 +178 (True, 31, 1, 30.488246202468872)
          54 +179 (True, 47, 2, 39.503575801849365)
          55 +181 (True, 45, 2, 49.75218462944031)
          56 +182 (True, 51, 2, 57.40186309814453)
          57 +183 (True, 35, 2, 38.86477494239807)
          58 +184 (True, 33, 1, 40.17844104766846)
          59 +187 (True, 21, 1, 24.674954175949097)
          60 +188 (True, 30, 1, 41.210681676864624)
          61 +189 (True, 28, 1, 33.68290877342224)
          62 +192 (True, 34, 2, 43.184091329574585)
          63 +193 (True, 35, 1, 45.541258573532104)
          64 +194 (True, 58, 2, 70.8309223651886)
          65 +197 (True, 44, 2, 51.75822925567627)
          66 +198 (True, 33, 1, 33.830421924591064)
          67 +199 (True, 33, 1, 35.18809199333191)
          68 +204 (True, 49, 2, 59.79915142059326)
          69 +205 (True, 27, 1, 25.788176774978638)
          70 +206 (True, 29, 1, 36.98551797866821)
          71 +208 (True, 29, 2, 37.85520339012146)
          72 +209 (True, 52, 2, 60.635236978530884)
          73 +215 (True, 44, 2, 47.05663561820984)
          74 +216 (True, 27, 2, 27.25289511680603)
          75 +217 (True, 42, 2, 37.90361976623535)
          76 +218 (True, 26, 1, 26.683939218521118)
          77 +220 (True, 51, 2, 43.201497316360474)
          78 +221 (True, 28, 1, 20.959730625152588)
          79 +222 (True, 29, 1, 26.637089490890503)
          80 +223 (True, 34, 1, 29.910329341888428)
          81 +224 (True, 44, 2, 34.71137285232544)
          82 +225 (True, 51, 2, 46.584436893463135)
          83 +226 (True, 40, 2, 36.215086460113525)
          84 +227 (True, 31, 1, 27.715421199798584)
          85 +228 (True, 31, 1, 33.29912495613098)
          86 +229 (True, 27, 1, 27.890472650527954)
          87 +230 (True, 27, 1, 25.639406204223633)
          88 +232 (True, 33, 1, 31.662187099456787)
          89 +234 (True, 32, 1, 31.609704732894897)
          90 +235 (True, 31, 2, 34.06675887107849)
          91 +236 (True, 31, 1, 27.336707592010498)
          92 +237 (True, 52, 2, 47.440539598464966)
          93 +239 (True, 41, 2, 31.423362970352173)
          94 +240 (True, 26, 2, 20.58475613594055)
          95 +241 (True, 30, 1, 28.40858769416809)
          96 +242 (True, 30, 2, 21.657092809677124)
          97 +243 (True, 43, 2, 42.367554903030396)
          98 +244 (True, 38, 2, 35.25688934326172)
          99 +245 (True, 44, 2, 45.66872572898865)
         100 +246 (True, 30, 2, 23.17040252685547)
         101 +248 (True, 26, 1, 24.127030611038208)
         102 +249 (True, 60, 2, 75.24981331825256)
         103 +250 (True, 39, 1, 45.82644987106323)
         104 +251 (True, 20, 0, 20.995161294937134)
         105 +252 (True, 29, 2, 29.030064582824707)
         106 +253 (True, 28, 1, 30.458595514297485)
         107 +256 (True, 37, 1, 35.88952970504761)
         108 +257 (True, 30, 2, 29.549595832824707)
         109 +258 (True, 29, 1, 26.80653691291809)
         110 +260 (True, 54, 2, 56.287129402160645)
         111 +261 (True, 26, 1, 25.68529725074768)
         112 +262 (True, 45, 2, 43.45246434211731)
         113 +263 (True, 38, 2, 32.26543855667114)
         114 +265 (True, 36, 2, 37.71523070335388)
         115 +267 (True, 36, 1, 33.88137626647949)
         116 +268 (True, 46, 2, 46.08863711357117)
         117 +269 (True, 35, 2, 45.368892192840576)
         118 +270 (True, 34, 1, 42.98245668411255)
         119 +271 (True, 50, 2, 62.23234581947327)
         120 +274 (True, 31, 1, 35.718549966812134)
         121 +275 (True, 20, 0, 25.173145294189453)
         122 +276 (True, 34, 1, 40.41317129135132)
         123 +277 (True, 23, 0, 23.534912586212158)
         124 +278 (True, 33, 1, 35.885531425476074)
         125 +280 (True, 39, 1, 44.57630920410156)
         126 +281 (True, 31, 1, 34.681461334228516)
         127 +282 (True, 49, 2, 59.88854503631592)
         128 +283 (True, 17, 0, 20.780271291732788)
         129 +285 (True, 56, 2, 71.64363169670105)
         130 +286 (True, 16, 0, 22.44819474220276)
         131 +287 (True, 39, 2, 47.62648797035217)
         132 +289 (True, 46, 1, 52.74301719665527)
         133 +291 (True, 22, 0, 23.657796382904053)
         134 +292 (True, 38, 2, 39.1631555557251)
         135 +success 200 / 200 mean steps 29.825 max time 75.24981331825256
```

</details>

<a id="C020"></a>
### C020 · grasp height: fingertip offset 0.0305 measured, z_hi top+0.028

Commit `118102da2098c2321a43a70488f1c6a7d3532842`; parents: c5d528bebc38b642d04e96097eae2bd0e05723e0. Recorded author date: 2026-09-30T23:17:44+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0900](01_timeline.md#E0900): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C020_118102d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index b9b6ae8..5ba989b 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -182,7 +182,7 @@ class GeneratedApproach:
  182    182          near = [(n, b) for n, b in objs.items() if n != o.name and n != 'target_region'
  183    183                  and np.linalg.norm(b.p[:2] - o.p[:2]) < 0.16]
  184    184          z_lo = o.bottom + 0.044
  185        -        z_hi = o.top + 0.027
         185 +        z_hi = o.top + 0.028
  186    186          if z_hi < z_lo:
  187    187              z_hi = z_lo = 0.5 * (z_lo + z_hi)
  188    188          zs = [min(0.5 * (z_lo + z_hi), z_lo + 0.012)]
@@ -201,7 +201,7 @@ class GeneratedApproach:
  201    201              sds = np.linspace(-smax, smax, 7) if smax > 0 else [0.0]
  202    202              sas = np.linspace(-amax, amax, 7) if amax > 0 else [0.0]
  203    203              for zi, zg in enumerate(zs):
  204        -                tip = zg - 0.035
         204 +                tip = zg - 0.0305
  205    205                  rel = [(n, b) for n, b in near if b.top > tip]
  206    206                  for sd in sds:
  207    207                      for sa in sas:
diff --git a/d101.txt b/d101.txt
new file mode 100644
index 0000000..3d2b80f
--- /dev/null
+++ b/d101.txt
@@ -0,0 +1,304 @@
           1 +obstruction0 [ 0.279 -0.124  0.109] [0.012 0.018 0.024]
           2 +obstruction1 [ 0.328 -0.161  0.108] [0.014 0.014 0.023]
           3 +obstruction2 [ 0.325 -0.119  0.111] [0.013 0.018 0.026]
           4 +obstruction3 [ 0.37  -0.176  0.114] [0.012 0.016 0.029]
           5 +obstruction4 [0.407 0.126 0.088] [0.01  0.011 0.013]
           6 +obstruction5 [0.283 0.19  0.095] [0.013 0.015 0.02 ]
           7 +obstruction6 [0.338 0.067 0.105] [0.019 0.019 0.03 ]
           8 +obstruction7 [ 0.286 -0.17   0.107] [0.014 0.012 0.022]
           9 +obstruction8 [ 0.478 -0.016  0.099] [0.014 0.014 0.024]
          10 +target_block [ 0.419 -0.102  0.1  ] [0.039 0.025 0.025]
          11 +target_region [ 0.328 -0.152  0.08 ] [0.048 0.031 0.005]
          12 +step 1 task obstruction3 grasp 0.0 plan 15 fails {} tool [0.154 0.001 0.217] end [ 0.359 -0.176  0.141]
          13 +step 8 task obstruction3 grasp 1.0 plan 16 fails {} tool [ 0.359 -0.176  0.141] end [ 0.352 -0.284  0.133]
          14 +step 15 task obstruction0 grasp 0.0 plan 15 fails {} tool [ 0.352 -0.284  0.133] end [ 0.279 -0.124  0.141]
          15 +ABORT step 20 tool [ 0.279 -0.124  0.188] q [ 0.103  0.189 -2.771 -2.157 -0.094 -0.81   2.104] target [ 0.14   0.295 -2.795 -2.231 -0.167 -0.638  2.178] tgt tool [ 0.279 -0.124  0.141]
          16 +step 22 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 1} tool [ 0.279 -0.124  0.25 ] end [ 0.328 -0.161  0.141]
          17 +ABORT step 25 tool [ 0.329 -0.161  0.188] q [ 0.156  0.315 -2.757 -1.985 -0.153 -0.869  2.194] target [ 0.187  0.404 -2.785 -2.052 -0.21  -0.72   2.247] tgt tool [ 0.328 -0.161  0.141]
          18 +step 26 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 1, 'obstruction1': 1} tool [ 0.329 -0.161  0.25 ] end [ 0.325 -0.119  0.141]
          19 +ABORT step 29 tool [ 0.325 -0.119  0.19 ] q [ 0.062  0.269 -2.782 -2.04  -0.125 -0.853  2.063] target [ 0.094  0.366 -2.808 -2.112 -0.185 -0.69   2.121] tgt tool [ 0.325 -0.119  0.141]
          20 +step 31 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 1, 'obstruction1': 1, 'obstruction2': 1} tool [ 0.325 -0.119  0.25 ] end [ 0.286 -0.17   0.141]
          21 +ABORT step 34 tool [ 0.286 -0.17   0.191] q [ 0.188  0.243 -2.717 -2.077 -0.133 -0.846  2.262] target [ 0.229  0.348 -2.749 -2.153 -0.21  -0.677  2.336] tgt tool [ 0.286 -0.17   0.141]
          22 +step 35 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 1, 'obstruction1': 1, 'obstruction2': 1, 'obstruction7': 1} tool [ 0.286 -0.17   0.25 ] end [ 0.279 -0.124  0.141]
          23 +ABORT step 45 tool [ 0.28  -0.124  0.195] q [ 0.213  0.173 -2.9   -2.141 -0.056 -0.833  3.629] target [ 0.238  0.291 -2.916 -2.228 -0.108 -0.633  3.683] tgt tool [ 0.279 -0.124  0.141]
          24 +step 46 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 2, 'obstruction1': 1, 'obstruction2': 1, 'obstruction7': 1} tool [ 0.28  -0.124  0.25 ] end [ 0.323 -0.161  0.141]
          25 +ABORT step 56 tool [ 0.323 -0.161  0.188] q [ 0.141  0.306 -2.732 -2.    -0.159 -0.865  2.208] target [ 0.175  0.397 -2.762 -2.068 -0.22  -0.715  2.266] tgt tool [ 0.323 -0.161  0.141]
          26 +step 58 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 2, 'obstruction1': 2, 'obstruction2': 1, 'obstruction7': 1} tool [ 0.323 -0.161  0.25 ] end [ 0.319 -0.119  0.141]
          27 +ABORT step 61 tool [ 0.32  -0.119  0.19 ] q [ 0.045  0.259 -2.757 -2.054 -0.128 -0.851  2.074] target [ 0.081  0.359 -2.786 -2.128 -0.195 -0.685  2.138] tgt tool [ 0.319 -0.119  0.141]
          28 +step 62 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 2, 'obstruction1': 2, 'obstruction2': 2, 'obstruction7': 1} tool [ 0.32  -0.119  0.25 ] end [ 0.281 -0.17   0.141]
          29 +ABORT step 65 tool [ 0.281 -0.17   0.191] q [ 0.172  0.234 -2.689 -2.091 -0.136 -0.844  2.275] target [ 0.217  0.341 -2.723 -2.168 -0.22  -0.672  2.357] tgt tool [ 0.281 -0.17   0.141]
          30 +step 67 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 2, 'obstruction1': 2, 'obstruction2': 2, 'obstruction7': 2} tool [ 0.281 -0.17   0.25 ] end [ 0.274 -0.124  0.141]
          31 +ABORT step 70 tool [ 0.274 -0.124  0.195] q [ 0.068  0.167 -2.727 -2.159 -0.091 -0.832  2.109] target [ 0.114  0.289 -2.756 -2.246 -0.182 -0.635  2.203] tgt tool [ 0.274 -0.124  0.141]
          32 +step 71 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 3, 'obstruction1': 2, 'obstruction2': 2, 'obstruction7': 2} tool [ 0.274 -0.124  0.25 ] end [ 0.334 -0.161  0.141]
          33 +ABORT step 74 tool [ 0.334 -0.161  0.187] q [ 0.124  0.33  -2.721 -1.972 -0.174 -0.874  2.208] target [ 0.157  0.416 -2.751 -2.037 -0.232 -0.731  2.262] tgt tool [ 0.334 -0.161  0.141]
          34 +step 75 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 3, 'obstruction1': 3, 'obstruction2': 2, 'obstruction7': 2} tool [ 0.334 -0.161  0.25 ] end [ 0.33  -0.119  0.141]
          35 +ABORT step 78 tool [ 0.33  -0.119  0.189] q [ 0.028  0.282 -2.743 -2.028 -0.144 -0.857  2.078] target [ 0.063  0.378 -2.773 -2.099 -0.208 -0.699  2.139] tgt tool [ 0.33  -0.119  0.141]
          36 +step 80 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 3, 'obstruction1': 3, 'obstruction2': 3, 'obstruction7': 2} tool [ 0.33  -0.119  0.25 ] end [ 0.292 -0.17   0.141]
          37 +ABORT step 83 tool [ 0.292 -0.17   0.19 ] q [ 0.154  0.258 -2.681 -2.066 -0.151 -0.85   2.272] target [ 0.198  0.359 -2.716 -2.139 -0.231 -0.686  2.349] tgt tool [ 0.292 -0.17   0.141]
          38 +step 85 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 3, 'obstruction1': 3, 'obstruction2': 3, 'obstruction7': 3} tool [ 0.292 -0.17   0.25 ] end [ 0.285 -0.124  0.141]
          39 +ABORT step 88 tool [ 0.285 -0.124  0.193] q [ 0.049  0.19  -2.714 -2.136 -0.106 -0.835  2.112] target [ 0.095  0.307 -2.745 -2.219 -0.195 -0.647  2.202] tgt tool [ 0.285 -0.124  0.141]
          40 +step 89 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 4, 'obstruction1': 3, 'obstruction2': 3, 'obstruction7': 3} tool [ 0.285 -0.124  0.25 ] end [ 0.328 -0.167  0.141]
          41 +ABORT step 92 tool [ 0.329 -0.167  0.187] q [ 0.127  0.327 -2.697 -1.98  -0.182 -0.873  2.24 ] target [ 0.162  0.414 -2.729 -2.044 -0.244 -0.73   2.297] tgt tool [ 0.328 -0.167  0.141]
          42 +step 93 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 4, 'obstruction1': 4, 'obstruction2': 3, 'obstruction7': 3} tool [ 0.329 -0.167  0.25 ] end [ 0.325 -0.125  0.141]
          43 +ABORT step 96 tool [ 0.325 -0.125  0.189] q [ 0.029  0.278 -2.718 -2.036 -0.15  -0.856  2.109] target [ 0.067  0.375 -2.75  -2.107 -0.219 -0.698  2.174] tgt tool [ 0.325 -0.125  0.141]
          44 +step 98 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 4, 'obstruction1': 4, 'obstruction2': 4, 'obstruction7': 3} tool [ 0.325 -0.125  0.25 ] end [ 0.286 -0.176  0.141]
          45 +ABORT step 101 tool [ 0.286 -0.176  0.19 ] q [ 0.157  0.256 -2.655 -2.071 -0.159 -0.849  2.306] target [ 0.203  0.359 -2.692 -2.144 -0.243 -0.686  2.388] tgt tool [ 0.286 -0.176  0.141]
          46 +step 103 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 4, 'obstruction1': 4, 'obstruction2': 4, 'obstruction7': 4} tool [ 0.286 -0.176  0.25 ] end [ 0.279 -0.13   0.141]
          47 +ABORT step 106 tool [ 0.28  -0.13   0.194] q [ 0.05   0.187 -2.687 -2.142 -0.11  -0.835  2.143] target [ 0.099  0.305 -2.72  -2.225 -0.206 -0.647  2.24 ] tgt tool [ 0.279 -0.13   0.141]
          48 +step 107 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 5, 'obstruction1': 4, 'obstruction2': 4, 'obstruction7': 4} tool [ 0.28 -0.13  0.25] end [ 0.328 -0.154  0.141]
          49 +ABORT step 110 tool [ 0.329 -0.154  0.187] q [ 0.088  0.315 -2.69  -1.996 -0.179 -0.868  2.207] target [ 0.124  0.404 -2.723 -2.062 -0.244 -0.722  2.268] tgt tool [ 0.328 -0.154  0.141]
          50 +step 111 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 5, 'obstruction1': 5, 'obstruction2': 4, 'obstruction7': 4} tool [ 0.329 -0.154  0.25 ] end [ 0.325 -0.112  0.141]
          51 +ABORT step 114 tool [ 0.325 -0.112  0.19 ] q [-0.011  0.269 -2.713 -2.048 -0.147 -0.853  2.072] target [ 0.028  0.367 -2.746 -2.12  -0.219 -0.692  2.141] tgt tool [ 0.325 -0.112  0.141]
          52 +step 116 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 5, 'obstruction1': 5, 'obstruction2': 5, 'obstruction7': 4} tool [ 0.325 -0.112  0.25 ] end [ 0.286 -0.163  0.141]
          53 +ABORT step 119 tool [ 0.286 -0.163  0.191] q [ 0.114  0.241 -2.647 -2.088 -0.152 -0.846  2.268] target [ 0.163  0.347 -2.685 -2.164 -0.242 -0.678  2.356] tgt tool [ 0.286 -0.163  0.141]
          54 +step 120 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 5, 'obstruction1': 5, 'obstruction2': 5, 'obstruction7': 5} tool [ 0.286 -0.163  0.25 ] end [ 0.279 -0.118  0.141]
          55 +ABORT step 123 tool [ 0.28  -0.118  0.194] q [ 0.006  0.174 -2.683 -2.155 -0.104 -0.833  2.099] target [ 0.056  0.296 -2.715 -2.241 -0.203 -0.64   2.201] tgt tool [ 0.279 -0.118  0.141]
          56 +step 124 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 6, 'obstruction1': 5, 'obstruction2': 5, 'obstruction7': 5} tool [ 0.28  -0.118  0.25 ] end [ 0.328 -0.161  0.141]
          57 +ABORT step 133 tool [ 0.329 -0.161  0.185] q [-0.032  0.348 -2.506 -1.996 -0.266 -0.879  0.746] target [ 0.017  0.432 -2.553 -2.058 -0.349 -0.749  0.822] tgt tool [ 0.328 -0.161  0.141]
          58 +step 135 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 6, 'obstruction1': 6, 'obstruction2': 5, 'obstruction7': 5} tool [ 0.329 -0.161  0.25 ] end [ 0.335 -0.119  0.141]
          59 +ABORT step 144 tool [ 0.335 -0.119  0.189] q [ 0.052  0.291 -2.776 -2.013 -0.136 -0.86   2.063] target [ 0.083  0.384 -2.803 -2.083 -0.194 -0.704  2.118] tgt tool [ 0.335 -0.119  0.141]
          60 +step 145 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 6, 'obstruction1': 6, 'obstruction2': 6, 'obstruction7': 5} tool [ 0.335 -0.119  0.25 ] end [ 0.286 -0.17   0.141]
          61 +ABORT step 154 tool [ 0.286 -0.17   0.189] q [ 0.018  0.267 -2.502 -2.086 -0.211 -0.851  0.781] target [ 0.081  0.369 -2.553 -2.158 -0.317 -0.697  0.884] tgt tool [ 0.286 -0.17   0.141]
          62 +step 156 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 6, 'obstruction1': 6, 'obstruction2': 6, 'obstruction7': 6} tool [ 0.286 -0.17   0.25 ] end [ 0.286 -0.124  0.141]
          63 +ABORT step 159 tool [ 0.286 -0.124  0.192] q [-0.105  0.208 -2.53  -2.14  -0.16  -0.837  0.605] target [-0.037  0.325 -2.578 -2.22  -0.281 -0.663  0.726] tgt tool [ 0.286 -0.124  0.141]
          64 +step 160 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 7, 'obstruction1': 6, 'obstruction2': 6, 'obstruction7': 6} tool [ 0.286 -0.124  0.25 ] end [ 0.317 -0.161  0.141]
          65 +ABORT step 169 tool [ 0.317 -0.161  0.182] q [-0.148  0.361 -2.336 -2.034 -0.337 -0.88  -0.727] target [-0.084  0.443 -2.398 -2.092 -0.435 -0.762 -0.637] tgt tool [ 0.317 -0.161  0.141]
          66 +step 171 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 7, 'obstruction1': 7, 'obstruction2': 6, 'obstruction7': 6} tool [ 0.317 -0.161  0.25 ] end [ 0.319 -0.125  0.141]
          67 +ABORT step 174 tool [ 0.32  -0.125  0.184] q [-0.256  0.327 -2.338 -2.068 -0.308 -0.867 -0.846] target [-0.185  0.417 -2.403 -2.13  -0.417 -0.739 -0.745] tgt tool [ 0.319 -0.125  0.141]
          68 +step 176 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 7, 'obstruction1': 7, 'obstruction2': 7, 'obstruction7': 6} tool [ 0.32  -0.125  0.25 ] end [ 0.275 -0.17   0.141]
          69 +ABORT step 179 tool [ 0.275 -0.17   0.186] q [-0.141  0.286 -2.278 -2.123 -0.289 -0.851 -0.675] target [-0.052  0.387 -2.354 -2.191 -0.42  -0.715 -0.548] tgt tool [ 0.275 -0.17   0.141]
          70 +step 181 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 7, 'obstruction1': 7, 'obstruction2': 7, 'obstruction7': 7} tool [ 0.275 -0.17   0.25 ] end [ 0.273 -0.124  0.141]
          71 +ABORT step 190 tool [ 0.273 -0.124  0.193] q [-0.155  0.184 -2.461 -2.171 -0.156 -0.833  0.623] target [-0.074  0.311 -2.516 -2.255 -0.299 -0.654  0.768] tgt tool [ 0.273 -0.124  0.141]
          72 +step 191 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 8, 'obstruction1': 7, 'obstruction2': 7, 'obstruction7': 7} tool [ 0.273 -0.124  0.25 ] end [ 0.34  -0.161  0.141]
          73 +ABORT step 200 tool [ 0.34  -0.161  0.179] q [-0.184  0.427 -2.291 -1.98  -0.405 -0.912 -0.693] target [-0.13   0.497 -2.348 -2.031 -0.488 -0.81  -0.621] tgt tool [ 0.34  -0.161  0.141]
          74 +step 202 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 8, 'obstruction1': 8, 'obstruction2': 7, 'obstruction7': 7} tool [ 0.34  -0.161  0.25 ] end [ 0.33  -0.125  0.141]
          75 +ABORT step 205 tool [ 0.33  -0.125  0.181] q [-0.299  0.371 -2.274 -2.046 -0.366 -0.883 -0.799] target [-0.231  0.452 -2.341 -2.102 -0.467 -0.77  -0.707] tgt tool [ 0.33  -0.125  0.141]
          76 +step 207 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 8, 'obstruction1': 8, 'obstruction2': 8, 'obstruction7': 7} tool [ 0.33  -0.125  0.25 ] end [ 0.281 -0.176  0.141]
          77 +ABORT step 210 tool [ 0.281 -0.176  0.183] q [-0.163  0.327 -2.22  -2.106 -0.344 -0.863 -0.61 ] target [-0.077  0.418 -2.299 -2.168 -0.465 -0.742 -0.496] tgt tool [ 0.281 -0.176  0.141]
          78 +step 212 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 8, 'obstruction1': 8, 'obstruction2': 8, 'obstruction7': 8} tool [ 0.281 -0.176  0.25 ] end [ 0.279 -0.117  0.141]
          79 +ABORT step 221 tool [ 0.28  -0.117  0.192] q [-0.208  0.196 -2.429 -2.165 -0.173 -0.834  0.613] target [-0.124  0.321 -2.488 -2.247 -0.317 -0.662  0.759] tgt tool [ 0.279 -0.117  0.141]
          80 +step 222 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 9, 'obstruction1': 8, 'obstruction2': 8, 'obstruction7': 8} tool [ 0.28  -0.117  0.25 ] end [ 0.323 -0.167  0.141]
          81 +ABORT step 231 tool [ 0.323 -0.167  0.179] q [-0.194  0.413 -2.239 -2.018 -0.413 -0.902 -0.64 ] target [-0.133  0.485 -2.303 -2.07  -0.504 -0.8   -0.559] tgt tool [ 0.323 -0.167  0.141]
          82 +step 233 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 9, 'obstruction1': 9, 'obstruction2': 8, 'obstruction7': 8} tool [ 0.323 -0.167  0.25 ] end [ 0.319 -0.112  0.141]
          83 +ABORT step 237 tool [ 0.32  -0.112  0.182] q [-0.373  0.348 -2.223 -2.087 -0.362 -0.871 -0.817] target [-0.294  0.434 -2.299 -2.146 -0.476 -0.755 -0.712] tgt tool [ 0.319 -0.112  0.141]
          84 +step 239 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 9, 'obstruction1': 9, 'obstruction2': 9, 'obstruction7': 8} tool [ 0.32  -0.112  0.25 ] end [ 0.292 -0.176  0.141]
          85 +ABORT step 243 tool [ 0.292 -0.176  0.181] q [-0.184  0.364 -2.195 -2.083 -0.386 -0.877 -0.587] target [-0.106  0.446 -2.271 -2.14  -0.496 -0.766 -0.486] tgt tool [ 0.292 -0.176  0.141]
          86 +step 245 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 9, 'obstruction1': 9, 'obstruction2': 9, 'obstruction7': 9} tool [ 0.292 -0.176  0.25 ] end [ 0.269 -0.124  0.141]
          87 +ABORT step 249 tool [ 0.269 -0.124  0.194] q [-0.417  0.219 -2.13  -2.186 -0.247 -0.854 -0.823] target [-0.273  0.356 -2.242 -2.271 -0.442 -0.692 -0.626] tgt tool [ 0.269 -0.124  0.141]
          88 +step 250 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 10, 'obstruction1': 9, 'obstruction2': 9, 'obstruction7': 9} tool [ 0.269 -0.124  0.25 ] end [ 0.334 -0.167  0.141]
          89 +ABORT step 254 tool [ 0.334 -0.167  0.176] q [-0.227  0.458 -2.19  -1.992 -0.468 -0.926 -0.603] target [-0.172  0.521 -2.251 -2.04  -0.55  -0.835 -0.532] tgt tool [ 0.334 -0.167  0.141]
          90 +step 256 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 10, 'obstruction1': 10, 'obstruction2': 9, 'obstruction7': 9} tool [ 0.334 -0.167  0.25 ] end [ 0.33  -0.112  0.141]
          91 +ABORT step 260 tool [ 0.33  -0.112  0.179] q [-0.407  0.397 -2.167 -2.064 -0.425 -0.892 -0.764] target [-0.334  0.472 -2.241 -2.117 -0.526 -0.79  -0.673] tgt tool [ 0.33  -0.112  0.141]
          92 +step 262 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 10, 'obstruction1': 10, 'obstruction2': 10, 'obstruction7': 9} tool [ 0.33  -0.112  0.25 ] end [ 0.281 -0.163  0.141]
          93 +ABORT step 265 tool [ 0.281 -0.163  0.181] q [-0.271  0.345 -2.117 -2.131 -0.389 -0.865 -0.585] target [-0.177  0.431 -2.207 -2.189 -0.513 -0.754 -0.469] tgt tool [ 0.281 -0.163  0.141]
          94 +step 267 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 10, 'obstruction1': 10, 'obstruction2': 10, 'obstruction7': 10} tool [ 0.281 -0.163  0.25 ] end [ 0.29  -0.124  0.141]
          95 +ABORT step 270 tool [ 0.29  -0.124  0.185] q [-0.421  0.308 -2.105 -2.151 -0.352 -0.862 -0.742] target [-0.308  0.409 -2.207 -2.218 -0.497 -0.736 -0.603] tgt tool [ 0.29  -0.124  0.141]
          96 +step 271 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 11, 'obstruction1': 10, 'obstruction2': 10, 'obstruction7': 10} tool [ 0.29  -0.124  0.25 ] end [ 0.323 -0.154  0.141]
          97 +ABORT step 274 tool [ 0.323 -0.154  0.177] q [-0.287  0.431 -2.15  -2.039 -0.459 -0.909 -0.616] target [-0.221  0.499 -2.22  -2.089 -0.552 -0.815 -0.534] tgt tool [ 0.323 -0.154  0.141]
          98 +step 276 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 11, 'obstruction1': 11, 'obstruction2': 10, 'obstruction7': 10} tool [ 0.323 -0.154  0.25 ] end [ 0.325 -0.131  0.141]
          99 +ABORT step 279 tool [ 0.325 -0.131  0.178] q [-0.363  0.413 -2.142 -2.061 -0.446 -0.899 -0.685] target [-0.292  0.484 -2.215 -2.112 -0.545 -0.801 -0.597] tgt tool [ 0.325 -0.131  0.141]
         100 +step 281 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 11, 'obstruction1': 11, 'obstruction2': 11, 'obstruction7': 10} tool [ 0.325 -0.131  0.25 ] end [ 0.292 -0.163  0.141]
         101 +ABORT step 284 tool [ 0.292 -0.163  0.179] q [-0.276  0.378 -2.113 -2.106 -0.423 -0.88  -0.572] target [-0.191  0.456 -2.197 -2.16  -0.535 -0.776 -0.47 ] tgt tool [ 0.292 -0.163  0.141]
         102 +step 286 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 11, 'obstruction1': 11, 'obstruction2': 11, 'obstruction7': 11} tool [ 0.292 -0.163  0.25 ] end [ 0.274 -0.13   0.141]
         103 +ABORT step 289 tool [ 0.274 -0.13   0.195] q [-0.462  0.265 -2.033 -2.166 -0.309 -0.88  -0.738] target [-0.305  0.395 -2.167 -2.251 -0.502 -0.725 -0.55 ] tgt tool [ 0.274 -0.13   0.141]
         104 +step 290 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 12, 'obstruction1': 11, 'obstruction2': 11, 'obstruction7': 11} tool [ 0.274 -0.13   0.25 ] end [ 0.334 -0.154  0.141]
         105 +ABORT step 294 tool [ 0.334 -0.154  0.175] q [-0.301  0.47  -2.126 -2.012 -0.501 -0.931 -0.593] target [-0.244  0.531 -2.191 -2.058 -0.584 -0.845 -0.522] tgt tool [ 0.334 -0.154  0.141]
         106 +step 296 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 12, 'obstruction1': 12, 'obstruction2': 11, 'obstruction7': 11} tool [ 0.334 -0.154  0.25 ] end [ 0.325 -0.106  0.141]
         107 +ABORT step 300 tool [ 0.325 -0.106  0.177] q [-0.473  0.408 -2.093 -2.088 -0.457 -0.894 -0.733] target [-0.395  0.48  -2.173 -2.14  -0.561 -0.798 -0.641] tgt tool [ 0.325 -0.106  0.141]
         108 +step 302 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 12, 'obstruction1': 12, 'obstruction2': 12, 'obstruction7': 11} tool [ 0.325 -0.106  0.25 ] end [ 0.286 -0.182  0.141]
         109 +ABORT step 306 tool [ 0.286 -0.182  0.177] q [-0.23   0.407 -2.082 -2.094 -0.459 -0.893 -0.478] target [-0.15   0.479 -2.164 -2.146 -0.564 -0.797 -0.384] tgt tool [ 0.286 -0.182  0.141]
         110 +step 308 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 12, 'obstruction1': 12, 'obstruction2': 12, 'obstruction7': 12} tool [ 0.286 -0.182  0.25 ] end [ 0.285 -0.13   0.141]
         111 +ABORT step 312 tool [ 0.285 -0.13   0.188] q [-0.456  0.32  -2.023 -2.153 -0.377 -0.88  -0.682] target [-0.325  0.425 -2.143 -2.225 -0.534 -0.75  -0.533] tgt tool [ 0.285 -0.13   0.141]
         112 +step 313 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 13, 'obstruction1': 12, 'obstruction2': 12, 'obstruction7': 12} tool [ 0.285 -0.13   0.25 ] end [ 0.328 -0.173  0.141]
         113 +ABORT step 317 tool [ 0.329 -0.173  0.174] q [-0.254  0.489 -2.107 -2.004 -0.522 -0.942 -0.52 ] target [-0.2    0.547 -2.17  -2.048 -0.602 -0.86  -0.452] tgt tool [ 0.328 -0.173  0.141]
         114 +step 319 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 13, 'obstruction1': 13, 'obstruction2': 12, 'obstruction7': 12} tool [ 0.329 -0.173  0.25 ] end [ 0.34  -0.119  0.141]
         115 +ABORT step 322 tool [ 0.34  -0.119  0.175] q [-0.428  0.465 -2.091 -2.036 -0.508 -0.927 -0.675] target [-0.366  0.526 -2.16  -2.083 -0.595 -0.841 -0.6  ] tgt tool [ 0.34  -0.119  0.141]
         116 +step 324 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 13, 'obstruction1': 13, 'obstruction2': 13, 'obstruction7': 12} tool [ 0.34  -0.119  0.25 ] end [ 0.286 -0.157  0.141]
         117 +ABORT step 327 tool [ 0.286 -0.157  0.178] q [-0.337  0.384 -2.043 -2.131 -0.448 -0.88  -0.544] target [-0.246  0.46  -2.135 -2.185 -0.563 -0.781 -0.439] tgt tool [ 0.286 -0.157  0.141]
         118 +step 329 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 13, 'obstruction1': 13, 'obstruction2': 13, 'obstruction7': 13} tool [ 0.286 -0.157  0.25 ] end [ 0.274 -0.118  0.141]
         119 +ABORT step 333 tool [ 0.275 -0.118  0.201] q [-0.585  0.258 -1.937 -2.17  -0.309 -0.901 -0.766] target [-0.387  0.404 -2.107 -2.267 -0.53  -0.732 -0.55 ] tgt tool [ 0.274 -0.118  0.141]
         120 +step 334 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 14, 'obstruction1': 13, 'obstruction2': 13, 'obstruction7': 13} tool [ 0.275 -0.118  0.25 ] end [ 0.328 -0.148  0.141]
         121 +ABORT step 338 tool [ 0.329 -0.148  0.174] q [-0.353  0.476 -2.067 -2.038 -0.526 -0.934 -0.568] target [-0.292  0.536 -2.136 -2.083 -0.611 -0.85  -0.494] tgt tool [ 0.328 -0.148  0.141]
         122 +step 339 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 14, 'obstruction1': 14, 'obstruction2': 13, 'obstruction7': 13} tool [ 0.329 -0.148  0.25 ] end [ 0.335 -0.125  0.141]
         123 +ABORT step 342 tool [ 0.335 -0.125  0.174] q [-0.426  0.471 -2.061 -2.046 -0.523 -0.93  -0.634] target [-0.363  0.532 -2.132 -2.091 -0.611 -0.846 -0.559] tgt tool [ 0.335 -0.125  0.141]
         124 +step 344 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 14, 'obstruction1': 14, 'obstruction2': 14, 'obstruction7': 13} tool [ 0.335 -0.125  0.25 ] end [ 0.286 -0.175  0.141]
         125 +ABORT step 352 tool [ 0.286 -0.175  0.168] q [-0.422  0.666 -1.673 -2.125 -0.769 -1.084 -1.698] target [-0.37   0.705 -1.748 -2.164 -0.843 -1.024 -1.643] tgt tool [ 0.286 -0.175  0.141]
         126 +step 353 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 14, 'obstruction1': 14, 'obstruction2': 14, 'obstruction7': 14} tool [ 0.286 -0.175  0.25 ] end [ 0.285 -0.118  0.141]
         127 +ABORT step 360 tool [ 0.285 -0.118  0.192] q [-0.571  0.33  -1.92  -2.161 -0.397 -0.904 -0.684] target [-0.413  0.441 -2.07  -2.241 -0.572 -0.765 -0.52 ] tgt tool [ 0.285 -0.118  0.141]
         128 +step 362 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction1': 14, 'obstruction2': 14, 'obstruction7': 14} tool [ 0.285 -0.118  0.25 ] end [ 0.328 -0.166  0.141]
         129 +ABORT step 370 tool [ 0.329 -0.166  0.159] q [-0.43   0.759 -1.708 -2.039 -0.846 -1.147 -1.754] target [-0.405  0.786 -1.749 -2.063 -0.89  -1.11  -1.723] tgt tool [ 0.328 -0.166  0.141]
         130 +step 371 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction1': 15, 'obstruction2': 14, 'obstruction7': 14} tool [ 0.329 -0.166  0.25 ] end [ 0.335 -0.112  0.141]
         131 +ABORT step 379 tool [ 0.335 -0.112  0.174] q [-0.477  0.469 -2.04  -2.059 -0.528 -0.929 -0.658] target [-0.411  0.53  -2.114 -2.105 -0.617 -0.845 -0.581] tgt tool [ 0.335 -0.112  0.141]
         132 +step 380 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction1': 15, 'obstruction2': 15, 'obstruction7': 14} tool [ 0.335 -0.112  0.25 ] end [ 0.286 -0.165  0.141]
         133 +ABORT step 388 tool [ 0.286 -0.165  0.17 ] q [-0.464  0.666 -1.647 -2.136 -0.767 -1.092 -1.713] target [-0.407  0.707 -1.729 -2.178 -0.848 -1.026 -1.653] tgt tool [ 0.286 -0.165  0.141]
         134 +step 389 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction1': 15, 'obstruction2': 15, 'obstruction7': 15} tool [ 0.286 -0.165  0.25 ] end [ 0.279 -0.137  0.141]
         135 +ABORT step 397 tool [ 0.28  -0.137  0.188] q [-0.48   0.343 -1.947 -2.159 -0.412 -0.896 -0.61 ] target [-0.34   0.445 -2.081 -2.231 -0.571 -0.768 -0.462] tgt tool [ 0.279 -0.137  0.141]
         136 +step 399 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 16, 'obstruction1': 15, 'obstruction2': 15, 'obstruction7': 15} tool [ 0.28  -0.137  0.25 ] end [ 0.335 -0.161  0.141]
         137 +ABORT step 406 tool [ 0.335 -0.161  0.25 ] q [-0.551  0.657 -1.534 -1.874 -0.675 -1.354 -1.905] target [-0.44   0.776 -1.716 -2.035 -0.863 -1.148 -1.766] tgt tool [ 0.335 -0.161  0.155]
         138 +step 407 task obstruction2 grasp 0.0 plan 17 fails {'obstruction0': 16, 'obstruction1': 16, 'obstruction2': 15, 'obstruction7': 15} tool [ 0.335 -0.161  0.28 ] end [ 0.319 -0.131  0.141]
         139 +ABORT step 415 tool [ 0.32  -0.131  0.206] q [-0.496  0.395 -1.961 -2.03  -0.437 -1.    -0.668] target [-0.357  0.516 -2.105 -2.129 -0.612 -0.832 -0.513] tgt tool [ 0.319 -0.131  0.141]
         140 +step 416 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 16, 'obstruction1': 16, 'obstruction2': 16, 'obstruction7': 15} tool [ 0.32  -0.131  0.25 ] end [ 0.293 -0.17   0.141]
         141 +ABORT step 424 tool [ 0.293 -0.17   0.166] q [-0.439  0.698 -1.656 -2.119 -0.797 -1.108 -1.693] target [-0.395  0.734 -1.722 -2.155 -0.865 -1.054 -1.643] tgt tool [ 0.293 -0.17   0.141]
         142 +step 425 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 16, 'obstruction1': 16, 'obstruction2': 16, 'obstruction7': 16} tool [ 0.293 -0.17   0.25 ] end [ 0.279 -0.111  0.141]
         143 +ABORT step 432 tool [ 0.28  -0.111  0.202] q [-0.664  0.302 -1.841 -2.162 -0.366 -0.93  -0.721] target [-0.454  0.437 -2.036 -2.262 -0.581 -0.762 -0.516] tgt tool [ 0.279 -0.111  0.141]
         144 +step 433 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 17, 'obstruction1': 16, 'obstruction2': 16, 'obstruction7': 16} tool [ 0.28  -0.111  0.25 ] end [ 0.322 -0.161  0.141]
         145 +ABORT step 440 tool [ 0.322 -0.161  0.159] q [-0.455  0.767 -1.674 -2.064 -0.855 -1.155 -1.734] target [-0.43   0.794 -1.716 -2.089 -0.901 -1.119 -1.702] tgt tool [ 0.322 -0.161  0.141]
         146 +step 441 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 17, 'obstruction1': 17, 'obstruction2': 16, 'obstruction7': 16} tool [ 0.322 -0.161  0.25 ] end [ 0.33  -0.131  0.141]
         147 +ABORT step 449 tool [ 0.33  -0.131  0.174] q [-0.423  0.478 -2.032 -2.055 -0.538 -0.934 -0.593] target [-0.359  0.537 -2.105 -2.1   -0.625 -0.852 -0.518] tgt tool [ 0.33  -0.131  0.141]
         148 +step 450 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 17, 'obstruction1': 17, 'obstruction2': 17, 'obstruction7': 16} tool [ 0.33  -0.131  0.25 ] end [ 0.28  -0.17   0.141]
         149 +ABORT step 458 tool [ 0.28  -0.17   0.171] q [-0.452  0.676 -1.624 -2.144 -0.775 -1.103 -1.675] target [-0.394  0.717 -1.707 -2.187 -0.858 -1.037 -1.614] tgt tool [ 0.28  -0.17   0.141]
         150 +step 459 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 17, 'obstruction1': 17, 'obstruction2': 17, 'obstruction7': 17} tool [ 0.28 -0.17  0.25] end [ 0.292 -0.124  0.141]
         151 +ABORT step 462 tool [ 0.292 -0.124  0.173] q [-0.626  0.698 -1.558 -2.169 -0.789 -1.132 -1.776] target [-0.564  0.74  -1.651 -2.217 -0.879 -1.061 -1.711] tgt tool [ 0.292 -0.124  0.141]
         152 +step 463 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 18, 'obstruction1': 17, 'obstruction2': 17, 'obstruction7': 17} tool [ 0.292 -0.124  0.25 ] end [ 0.345 -0.161  0.141]
         153 +ABORT step 472 tool [ 0.345 -0.161  0.172] q [-0.297  0.518 -2.099 -1.977 -0.549 -0.961 -0.552] target [-0.248  0.572 -2.158 -2.018 -0.622 -0.884 -0.491] tgt tool [ 0.345 -0.161  0.141]
         154 +step 473 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 18, 'obstruction1': 18, 'obstruction2': 17, 'obstruction7': 17} tool [ 0.345 -0.161  0.25 ] end [ 0.319 -0.106  0.141]
         155 +ABORT step 477 tool [ 0.32  -0.106  0.176] q [-0.506  0.419 -2.039 -2.105 -0.482 -0.898 -0.695] target [-0.425  0.488 -2.124 -2.155 -0.586 -0.806 -0.603] tgt tool [ 0.319 -0.106  0.141]
         156 +step 479 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 18, 'obstruction1': 18, 'obstruction2': 18, 'obstruction7': 17} tool [ 0.32  -0.106  0.25 ] end [ 0.269 -0.17   0.141]
         157 +ABORT step 482 tool [ 0.269 -0.17   0.182] q [-0.32   0.364 -2.    -2.148 -0.432 -0.884 -0.491] target [-0.209  0.451 -2.109 -2.209 -0.566 -0.773 -0.368] tgt tool [ 0.269 -0.17   0.141]
         158 +step 483 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 18, 'obstruction1': 18, 'obstruction2': 18, 'obstruction7': 18} tool [ 0.269 -0.17   0.25 ] end [ 0.267 -0.124  0.141]
         159 +ABORT step 492 tool [ 0.267 -0.124  0.191] q [-0.376  0.21  -2.181 -2.195 -0.232 -0.838  0.731] target [-0.245  0.342 -2.279 -2.277 -0.417 -0.681  0.919] tgt tool [ 0.267 -0.124  0.141]
         160 +step 493 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 19, 'obstruction1': 18, 'obstruction2': 18, 'obstruction7': 18} tool [ 0.267 -0.124  0.25 ] end [ 0.317 -0.167  0.141]
         161 +ABORT step 501 tool [ 0.317 -0.167  0.173] q [-0.322  0.499 -2.013 -2.046 -0.562 -0.947 -0.465] target [-0.262  0.555 -2.083 -2.089 -0.645 -0.869 -0.394] tgt tool [ 0.317 -0.167  0.141]
         162 +step 502 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 19, 'obstruction1': 19, 'obstruction2': 18, 'obstruction7': 18} tool [ 0.317 -0.167  0.25 ] end [ 0.33  -0.106  0.141]
         163 +ABORT step 506 tool [ 0.33  -0.106  0.174] q [-0.529  0.478 -1.983 -2.081 -0.552 -0.934 -0.636] target [-0.459  0.537 -2.062 -2.126 -0.643 -0.852 -0.558] tgt tool [ 0.33  -0.106  0.141]
         164 +step 507 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 19, 'obstruction1': 19, 'obstruction2': 19, 'obstruction7': 18} tool [ 0.33  -0.106  0.25 ] end [ 0.275 -0.176  0.141]
         165 +ABORT step 510 tool [ 0.275 -0.176  0.176] q [-0.309  0.42  -1.971 -2.135 -0.5   -0.898 -0.415] target [-0.219  0.488 -2.066 -2.186 -0.609 -0.807 -0.318] tgt tool [ 0.275 -0.176  0.141]
         166 +step 511 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 19, 'obstruction1': 19, 'obstruction2': 19, 'obstruction7': 19} tool [ 0.275 -0.176  0.25 ] end [ 0.286 -0.117  0.141]
         167 +ABORT step 519 tool [ 0.286 -0.117  0.187] q [-0.373  0.259 -2.211 -2.163 -0.279 -0.841  0.73 ] target [-0.266  0.37  -2.299 -2.234 -0.431 -0.702  0.879] tgt tool [ 0.286 -0.117  0.141]
         168 +step 521 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 20, 'obstruction1': 19, 'obstruction2': 19, 'obstruction7': 19} tool [ 0.286 -0.117  0.25 ] end [ 0.34  -0.167  0.141]
         169 +ABORT step 529 tool [ 0.34  -0.167  0.169] q [-0.33   0.567 -1.995 -1.99  -0.624 -0.994 -0.448] target [-0.285  0.614 -2.053 -2.027 -0.692 -0.927 -0.393] tgt tool [ 0.34  -0.167  0.141]
         170 +step 530 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 20, 'obstruction1': 20, 'obstruction2': 19, 'obstruction7': 19} tool [ 0.34  -0.167  0.25 ] end [ 0.325 -0.138  0.141]
         171 +step 534 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 20, 'obstruction1': 20, 'obstruction2': 20, 'obstruction7': 19} tool [ 0.325 -0.138  0.141] end [ 0.275 -0.163  0.141]
         172 +ABORT step 537 tool [ 0.275 -0.163  0.188] q [-0.421  0.409 -1.872 -2.136 -0.49  -0.939 -0.443] target [-0.291  0.498 -2.009 -2.207 -0.636 -0.817 -0.313] tgt tool [ 0.275 -0.163  0.141]
         173 +step 538 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 20, 'obstruction1': 20, 'obstruction2': 20, 'obstruction7': 20} tool [ 0.275 -0.163  0.25 ] end [ 0.273 -0.117  0.141]
         174 +ABORT step 546 tool [ 0.273 -0.117  0.173] q [-0.663  0.773 -1.424 -2.226 -0.832 -1.208 -1.659] target [-0.605  0.812 -1.52  -2.276 -0.924 -1.14  -1.596] tgt tool [ 0.273 -0.117  0.141]
         175 +step 547 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 21, 'obstruction1': 20, 'obstruction2': 20, 'obstruction7': 20} tool [ 0.273 -0.117  0.25 ] end [ 0.317 -0.154  0.141]
         176 +ABORT step 555 tool [ 0.317 -0.154  0.172] q [-0.382  0.503 -1.974 -2.064 -0.576 -0.95  -0.474] target [-0.318  0.558 -2.048 -2.107 -0.661 -0.873 -0.402] tgt tool [ 0.317 -0.154  0.141]
         177 +step 556 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 21, 'obstruction1': 21, 'obstruction2': 20, 'obstruction7': 20} tool [ 0.317 -0.154  0.25 ] end [ 0.325 -0.1    0.141]
         178 +ABORT step 560 tool [ 0.325 -0.1    0.174] q [-0.575  0.481 -1.939 -2.101 -0.565 -0.937 -0.626] target [-0.5    0.54  -2.023 -2.148 -0.659 -0.855 -0.546] tgt tool [ 0.325 -0.1    0.141]
         179 +step 561 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 21, 'obstruction1': 21, 'obstruction2': 21, 'obstruction7': 20} tool [ 0.325 -0.1    0.25 ] end [ 0.281 -0.182  0.141]
         180 +ABORT step 565 tool [ 0.281 -0.182  0.175] q [-0.293  0.452 -1.962 -2.114 -0.533 -0.918 -0.379] target [-0.212  0.515 -2.05  -2.162 -0.633 -0.832 -0.292] tgt tool [ 0.281 -0.182  0.141]
         181 +step 566 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 21, 'obstruction1': 21, 'obstruction2': 21, 'obstruction7': 21} tool [ 0.281 -0.182  0.25 ] end [ 0.279 -0.11   0.141]
         182 +ABORT step 574 tool [ 0.28 -0.11  0.19] q [-0.431  0.235 -2.172 -2.182 -0.26  -0.842  0.701] target [-0.306  0.358 -2.271 -2.259 -0.433 -0.693  0.874] tgt tool [ 0.279 -0.11   0.141]
         183 +step 575 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 22, 'obstruction1': 21, 'obstruction2': 21, 'obstruction7': 21} tool [ 0.28 -0.11  0.25] end [ 0.34  -0.154  0.141]
         184 +ABORT step 583 tool [ 0.34  -0.154  0.17 ] q [-0.374  0.559 -1.982 -2.006 -0.621 -0.989 -0.475] target [-0.326  0.607 -2.043 -2.044 -0.692 -0.921 -0.417] tgt tool [ 0.34  -0.154  0.141]
         185 +step 584 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 22, 'obstruction1': 22, 'obstruction2': 21, 'obstruction7': 21} tool [ 0.34  -0.154  0.25 ] end [ 0.306 -0.119  0.141]
         186 +step 594 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 22, 'obstruction1': 22, 'obstruction2': 22, 'obstruction7': 21} tool [ 0.306 -0.119  0.141] end [ 0.292 -0.182  0.141]
         187 +ABORT step 602 tool [ 0.292 -0.182  0.188] q [-0.383  1.074 -1.248 -2.067 -0.986 -1.589 -2.94 ] target [-0.357  1.145 -1.337 -2.137 -1.09  -1.527 -2.893] tgt tool [ 0.292 -0.182  0.141]
         188 +step 603 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 22, 'obstruction1': 22, 'obstruction2': 22, 'obstruction7': 22} tool [ 0.292 -0.182  0.25 ] end [ 0.264 -0.124  0.141]
         189 +ABORT step 605 tool [ 0.264 -0.124  0.25 ] q [-0.593  0.994 -1.01  -2.086 -0.797 -1.69  -3.001] target [-0.531  1.126 -1.198 -2.269 -0.999 -1.546 -2.896] tgt tool [ 0.264 -0.124  0.155]
         190 +step 606 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 23, 'obstruction1': 22, 'obstruction2': 22, 'obstruction7': 22} tool [ 0.264 -0.124  0.28 ] end [ 0.323 -0.173  0.141]
         191 +ABORT step 609 tool [ 0.323 -0.173  0.175] q [-0.407  1.128 -1.286 -2.021 -1.051 -1.613 -3.022] target [-0.394  1.18  -1.345 -2.069 -1.122 -1.571 -2.992] tgt tool [ 0.323 -0.173  0.141]
         192 +step 610 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 23, 'obstruction1': 23, 'obstruction2': 22, 'obstruction7': 22} tool [ 0.323 -0.173  0.25 ] end [ 0.34  -0.125  0.141]
         193 +ABORT step 612 tool [ 0.34  -0.125  0.25 ] q [-0.56   1.056 -1.13  -1.898 -0.932 -1.766 -3.192] target [-0.529  1.222 -1.3   -2.081 -1.135 -1.624 -3.101] tgt tool [ 0.34  -0.125  0.141]
         194 +step 613 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 23, 'obstruction1': 23, 'obstruction2': 23, 'obstruction7': 22} tool [ 0.34  -0.125  0.28 ] end [ 0.281 -0.157  0.141]
         195 +ABORT step 616 tool [ 0.281 -0.157  0.181] q [-0.458  1.068 -1.223 -2.142 -0.968 -1.562 -2.94 ] target [-0.431  1.13  -1.307 -2.204 -1.065 -1.508 -2.895] tgt tool [ 0.281 -0.157  0.141]
         196 +step 617 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 23, 'obstruction1': 23, 'obstruction2': 23, 'obstruction7': 23} tool [ 0.281 -0.157  0.25 ] end [ 0.295 -0.124  0.141]
         197 +ABORT step 619 tool [ 0.295 -0.124  0.25 ] q [-0.59   1.012 -1.069 -2.015 -0.849 -1.711 -3.087] target [-0.534  1.171 -1.268 -2.21  -1.075 -1.559 -2.978] tgt tool [ 0.295 -0.124  0.141]
         198 +step 620 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 24, 'obstruction1': 23, 'obstruction2': 23, 'obstruction7': 23} tool [ 0.295 -0.124  0.28 ] end [ 0.334 -0.173  0.141]
         199 +ABORT step 623 tool [ 0.334 -0.173  0.173] q [-0.41   1.127 -1.309 -1.993 -1.061 -1.608 -3.06 ] target [-0.398  1.177 -1.364 -2.038 -1.129 -1.568 -3.032] tgt tool [ 0.334 -0.173  0.141]
         200 +step 624 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 24, 'obstruction1': 24, 'obstruction2': 23, 'obstruction7': 23} tool [ 0.334 -0.173  0.25 ] end [ 0.34  -0.112  0.141]
         201 +ABORT step 626 tool [ 0.34  -0.112  0.25 ] q [-0.601  1.05  -1.126 -1.91  -0.923 -1.758 -3.221] target [-0.568  1.215 -1.299 -2.094 -1.129 -1.615 -3.127] tgt tool [ 0.34  -0.112  0.141]
         202 +step 627 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 24, 'obstruction1': 24, 'obstruction2': 24, 'obstruction7': 23} tool [ 0.34  -0.112  0.28 ] end [ 0.292 -0.157  0.141]
         203 +ABORT step 630 tool [ 0.292 -0.157  0.18 ] q [-0.463  1.068 -1.25  -2.117 -0.982 -1.557 -2.98 ] target [-0.438  1.127 -1.328 -2.175 -1.073 -1.505 -2.937] tgt tool [ 0.292 -0.157  0.141]
         204 +step 631 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 24, 'obstruction1': 24, 'obstruction2': 24, 'obstruction7': 24} tool [ 0.292 -0.157  0.25 ] end [ 0.269 -0.13   0.141]
         205 +ABORT step 633 tool [ 0.269 -0.13   0.25 ] q [-0.59   0.965 -1.051 -2.068 -0.799 -1.658 -3.034] target [-0.524  1.094 -1.24  -2.249 -1.001 -1.507 -2.925] tgt tool [ 0.269 -0.13   0.155]
         206 +step 634 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 25, 'obstruction1': 24, 'obstruction2': 24, 'obstruction7': 24} tool [ 0.269 -0.13   0.28 ] end [ 0.323 -0.148  0.141]
         207 +ABORT step 637 tool [ 0.323 -0.148  0.176] q [-0.487  1.113 -1.272 -2.053 -1.031 -1.6   -3.068] target [-0.471  1.167 -1.337 -2.104 -1.108 -1.555 -3.035] tgt tool [ 0.323 -0.148  0.141]
         208 +step 638 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 25, 'obstruction1': 25, 'obstruction2': 24, 'obstruction7': 24} tool [ 0.323 -0.148  0.25 ] end [ 0.335 -0.131  0.141]
         209 +ABORT step 640 tool [ 0.335 -0.131  0.25 ] q [-0.556  1.026 -1.151 -1.906 -0.913 -1.73  -3.189] target [-0.518  1.188 -1.326 -2.089 -1.12  -1.581 -3.091] tgt tool [ 0.335 -0.131  0.141]
         210 +step 641 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 25, 'obstruction1': 25, 'obstruction2': 25, 'obstruction7': 24} tool [ 0.335 -0.131  0.28 ] end [ 0.286 -0.189  0.141]
         211 +ABORT step 644 tool [ 0.286 -0.189  0.178] q [-0.368  1.04  -1.305 -2.087 -0.985 -1.519 -2.936] target [-0.343  1.095 -1.378 -2.141 -1.07  -1.467 -2.894] tgt tool [ 0.286 -0.189  0.141]
         212 +step 645 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 25, 'obstruction1': 25, 'obstruction2': 25, 'obstruction7': 25} tool [ 0.286 -0.189  0.25 ] end [ 0.29  -0.13   0.141]
         213 +ABORT step 647 tool [ 0.29 -0.13  0.25] q [-0.586  0.979 -1.089 -2.021 -0.833 -1.674 -3.088] target [-0.521  1.133 -1.296 -2.216 -1.062 -1.512 -2.971] tgt tool [ 0.29  -0.13   0.141]
         214 +step 648 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 26, 'obstruction1': 25, 'obstruction2': 25, 'obstruction7': 25} tool [ 0.29 -0.13  0.28] end [ 0.334 -0.148  0.141]
         215 +ABORT step 651 tool [ 0.334 -0.148  0.175] q [-0.487  1.118 -1.292 -2.024 -1.045 -1.601 -3.102] target [-0.472  1.17  -1.352 -2.072 -1.117 -1.559 -3.071] tgt tool [ 0.334 -0.148  0.141]
         216 +step 652 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 26, 'obstruction1': 26, 'obstruction2': 25, 'obstruction7': 25} tool [ 0.334 -0.148  0.25 ] end [ 0.335 -0.106  0.141]
         217 +ABORT step 654 tool [ 0.335 -0.106  0.25 ] q [-0.631  1.034 -1.126 -1.929 -0.905 -1.738 -3.231] target [-0.591  1.196 -1.304 -2.115 -1.115 -1.591 -3.133] tgt tool [ 0.335 -0.106  0.141]
         218 +step 655 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 26, 'obstruction1': 26, 'obstruction2': 26, 'obstruction7': 25} tool [ 0.335 -0.106  0.28 ] end [ 0.286 -0.151  0.141]
         219 +ABORT step 658 tool [ 0.286 -0.151  0.181] q [-0.489  1.043 -1.249 -2.138 -0.962 -1.531 -2.989] target [-0.46   1.102 -1.333 -2.199 -1.058 -1.475 -2.942] tgt tool [ 0.286 -0.151  0.141]
         220 +step 659 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 26, 'obstruction1': 26, 'obstruction2': 26, 'obstruction7': 26} tool [ 0.286 -0.151  0.25 ] end [ 0.269 -0.118  0.141]
         221 +ABORT step 661 tool [ 0.269 -0.118  0.25 ] q [-0.641  0.957 -1.043 -2.081 -0.787 -1.648 -3.07 ] target [-0.571  1.083 -1.237 -2.264 -0.992 -1.494 -2.959] tgt tool [ 0.269 -0.118  0.155]
         222 +step 662 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 27, 'obstruction1': 26, 'obstruction2': 26, 'obstruction7': 26} tool [ 0.269 -0.118  0.28 ] end [ 0.328 -0.18   0.141]
         223 +ABORT step 666 tool [ 0.329 -0.18   0.174] q [-0.401  1.079 -1.35  -1.999 -1.035 -1.55  -3.064] target [-0.386  1.128 -1.407 -2.044 -1.104 -1.506 -3.032] tgt tool [ 0.328 -0.18   0.141]
         224 +step 667 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 27, 'obstruction1': 27, 'obstruction2': 26, 'obstruction7': 26} tool [ 0.329 -0.18   0.25 ] end [ 0.319 -0.138  0.141]
         225 +step 671 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 27, 'obstruction1': 27, 'obstruction2': 27, 'obstruction7': 26} tool [ 0.319 -0.138  0.141] end [ 0.286 -0.179  0.141]
         226 +ABORT step 680 tool [ 0.286 -0.179  0.188] q [-0.299  1.286 -1.048 -2.083 -1.047 -1.854 -4.345] target [-0.292  1.369 -1.126 -2.155 -1.147 -1.815 -4.322] tgt tool [ 0.286 -0.179  0.141]
         227 +step 681 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 27, 'obstruction1': 27, 'obstruction2': 27, 'obstruction7': 27} tool [ 0.286 -0.179  0.25 ] end [ 0.29  -0.118  0.141]
         228 +ABORT step 689 tool [ 0.29  -0.118  0.25 ] q [-0.671  0.901 -1.135 -2.034 -0.791 -1.589 -3.188] target [-0.595  1.022 -1.329 -2.211 -0.993 -1.423 -3.072] tgt tool [ 0.29  -0.118  0.155]
         229 +step 690 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 28, 'obstruction1': 27, 'obstruction2': 27, 'obstruction7': 27} tool [ 0.29  -0.118  0.28 ] end [ 0.328 -0.142  0.141]
         230 +step 694 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 28, 'obstruction1': 28, 'obstruction2': 27, 'obstruction7': 27} tool [ 0.328 -0.142  0.141] end [ 0.33  -0.138  0.141]
         231 +step 698 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 28, 'obstruction1': 28, 'obstruction2': 28, 'obstruction7': 27} tool [ 0.33  -0.138  0.141] end [ 0.286 -0.16   0.141]
         232 +ABORT step 707 tool [ 0.286 -0.16   0.188] q [-0.383  1.232 -1.078 -2.112 -1.016 -1.783 -4.407] target [-0.37   1.313 -1.161 -2.185 -1.119 -1.74  -4.376] tgt tool [ 0.286 -0.16   0.141]
         233 +step 708 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 28, 'obstruction1': 28, 'obstruction2': 28, 'obstruction7': 28} tool [ 0.286 -0.16   0.25 ] end [ 0.274 -0.137  0.141]
         234 +ABORT step 717 tool [ 0.275 -0.137  0.163] q [-0.56   0.886 -1.396 -2.216 -0.915 -1.295 -3.088] target [-0.529  0.916 -1.454 -2.249 -0.976 -1.256 -3.05 ] tgt tool [ 0.274 -0.137  0.141]
         235 +step 718 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 29, 'obstruction1': 28, 'obstruction2': 28, 'obstruction7': 28} tool [ 0.275 -0.137  0.25 ] end [ 0.328 -0.172  0.141]
         236 +ABORT step 726 tool [ 0.328 -0.172  0.168] q [-0.353  0.597 -1.911 -2.017 -0.672 -1.016 -1.932] target [-0.308  0.64  -1.971 -2.053 -0.739 -0.954 -1.879] tgt tool [ 0.328 -0.172  0.141]
         237 +step 727 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 29, 'obstruction1': 29, 'obstruction2': 28, 'obstruction7': 28} tool [ 0.328 -0.172  0.25 ] end [ 0.319 -0.1    0.141]
         238 +ABORT step 735 tool [ 0.32  -0.1    0.182] q [-0.428  0.343 -2.202 -2.099 -0.364 -0.868 -0.847] target [-0.345  0.43  -2.281 -2.158 -0.481 -0.752 -0.738] tgt tool [ 0.319 -0.1    0.141]
         239 +step 737 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 29, 'obstruction1': 29, 'obstruction2': 29, 'obstruction7': 28} tool [ 0.32 -0.1   0.25] end [ 0.293 -0.175  0.141]
         240 +ABORT step 745 tool [ 0.293 -0.175  0.173] q [-0.352  0.509 -1.897 -2.1   -0.6   -0.957 -1.917] target [-0.281  0.564 -1.98  -2.145 -0.69  -0.879 -1.841] tgt tool [ 0.293 -0.175  0.141]
         241 +step 746 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 29, 'obstruction1': 29, 'obstruction2': 29, 'obstruction7': 29} tool [ 0.293 -0.175  0.25 ] end [ 0.285 -0.137  0.141]
         242 +ABORT step 754 tool [ 0.285 -0.137  0.163] q [-0.563  0.855 -1.448 -2.19  -0.905 -1.26  -3.147] target [-0.532  0.884 -1.505 -2.222 -0.964 -1.22  -3.109] tgt tool [ 0.285 -0.137  0.141]
         243 +step 755 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 30, 'obstruction1': 29, 'obstruction2': 29, 'obstruction7': 29} tool [ 0.285 -0.137  0.25 ] end [ 0.335 -0.166  0.141]
         244 +ABORT step 763 tool [ 0.335 -0.166  0.169] q [-0.353  0.581 -1.95  -2.006 -0.649 -1.004 -1.983] target [-0.308  0.626 -2.009 -2.043 -0.717 -0.94  -1.928] tgt tool [ 0.335 -0.166  0.141]
         245 +step 764 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 30, 'obstruction1': 30, 'obstruction2': 29, 'obstruction7': 29} tool [ 0.335 -0.166  0.25 ] end [ 0.33  -0.1    0.141]
         246 +ABORT step 772 tool [ 0.33  -0.1    0.182] q [-0.388  0.354 -2.258 -2.069 -0.356 -0.875 -0.872] target [-0.314  0.438 -2.329 -2.127 -0.465 -0.758 -0.773] tgt tool [ 0.33  -0.1    0.141]
         247 +step 774 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 30, 'obstruction1': 30, 'obstruction2': 30, 'obstruction7': 29} tool [ 0.33 -0.1   0.25] end [ 0.293 -0.165  0.141]
         248 +ABORT step 782 tool [ 0.293 -0.165  0.174] q [-0.366  0.469 -1.937 -2.112 -0.555 -0.93  -1.988] target [-0.288  0.53  -2.025 -2.159 -0.652 -0.846 -1.905] tgt tool [ 0.293 -0.165  0.141]
         249 +step 783 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 30, 'obstruction1': 30, 'obstruction2': 30, 'obstruction7': 30} tool [ 0.293 -0.165  0.25 ] end [ 0.274 -0.111  0.141]
         250 +ABORT step 791 tool [ 0.274 -0.111  0.195] q [-0.471  0.218 -2.122 -2.185 -0.246 -0.856 -0.87 ] target [-0.323  0.357 -2.237 -2.272 -0.445 -0.693 -0.669] tgt tool [ 0.274 -0.111  0.141]
         251 +step 792 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 31, 'obstruction1': 30, 'obstruction2': 30, 'obstruction7': 30} tool [ 0.274 -0.111  0.25 ] end [ 0.322 -0.166  0.141]
         252 +ABORT step 800 tool [ 0.322 -0.166  0.17 ] q [-0.357  0.55  -1.945 -2.038 -0.624 -0.983 -1.979] target [-0.303  0.599 -2.012 -2.078 -0.7   -0.913 -1.918] tgt tool [ 0.322 -0.166  0.141]
         253 +step 801 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 31, 'obstruction1': 31, 'obstruction2': 30, 'obstruction7': 30} tool [ 0.322 -0.166  0.25 ] end [ 0.306 -0.126  0.141]
         254 +step 806 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 31, 'obstruction1': 31, 'obstruction2': 31, 'obstruction7': 30} tool [ 0.306 -0.126  0.141] end [ 0.28  -0.175  0.141]
         255 +ABORT step 809 tool [ 0.28  -0.175  0.188] q [-0.382  0.444 -1.869 -2.107 -0.523 -0.964 -1.963] target [-0.264  0.529 -1.997 -2.177 -0.661 -0.845 -1.843] tgt tool [ 0.28  -0.175  0.141]
         256 +step 810 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 31, 'obstruction1': 31, 'obstruction2': 31, 'obstruction7': 31} tool [ 0.28  -0.175  0.25 ] end [ 0.285 -0.111  0.141]
         257 +ABORT step 818 tool [ 0.285 -0.111  0.189] q [-0.451  0.259 -2.136 -2.169 -0.292 -0.853 -0.836] target [-0.325  0.378 -2.241 -2.245 -0.46  -0.709 -0.671] tgt tool [ 0.285 -0.111  0.141]
         258 +step 819 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 32, 'obstruction1': 31, 'obstruction2': 31, 'obstruction7': 31} tool [ 0.285 -0.111  0.25 ] end [ 0.341 -0.161  0.141]
         259 +ABORT step 827 tool [ 0.341 -0.161  0.168] q [-0.378  0.604 -1.929 -1.998 -0.674 -1.022 -1.981] target [-0.336  0.646 -1.985 -2.033 -0.738 -0.961 -1.93 ] tgt tool [ 0.341 -0.161  0.141]
         260 +step 828 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 32, 'obstruction1': 32, 'obstruction2': 31, 'obstruction7': 31} tool [ 0.341 -0.161  0.25 ] end [ 0.306 -0.111  0.141]
         261 +step 833 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 32, 'obstruction1': 32, 'obstruction2': 32, 'obstruction7': 31} tool [ 0.306 -0.111  0.141] end [ 0.28  -0.165  0.141]
         262 +ABORT step 836 tool [ 0.28  -0.165  0.188] q [-0.438  0.454 -1.821 -2.122 -0.541 -0.972 -1.96 ] target [-0.316  0.537 -1.957 -2.193 -0.68  -0.854 -1.84 ] tgt tool [ 0.28  -0.165  0.141]
         263 +step 837 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 32, 'obstruction1': 32, 'obstruction2': 32, 'obstruction7': 32} tool [ 0.28  -0.165  0.25 ] end [ 0.279 -0.143  0.141]
         264 +step 846 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 33, 'obstruction1': 32, 'obstruction2': 32, 'obstruction7': 32} tool [ 0.279 -0.143  0.141] end [ 0.316 -0.161  0.141]
         265 +ABORT step 854 tool [ 0.316 -0.161  0.188] q [-0.439  0.542 -1.833 -2.037 -0.615 -1.043 -1.971] target [-0.35   0.617 -1.944 -2.104 -0.736 -0.932 -1.873] tgt tool [ 0.316 -0.161  0.141]
         266 +step 855 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 33, 'obstruction1': 33, 'obstruction2': 32, 'obstruction7': 32} tool [ 0.316 -0.161  0.25 ] end [ 0.34  -0.131  0.141]
         267 +ABORT step 864 tool [ 0.34  -0.131  0.179] q [-0.296  0.412 -2.249 -2.014 -0.409 -0.902 -0.755] target [-0.235  0.484 -2.312 -2.066 -0.499 -0.799 -0.674] tgt tool [ 0.34  -0.131  0.141]
         268 +step 866 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 33, 'obstruction1': 33, 'obstruction2': 33, 'obstruction7': 32} tool [ 0.34  -0.131  0.25 ] end [ 0.299 -0.17   0.141]
         269 +ABORT step 874 tool [ 0.299 -0.17   0.172] q [-0.372  0.525 -1.888 -2.092 -0.616 -0.968 -1.924] target [-0.305  0.578 -1.969 -2.136 -0.703 -0.893 -1.852] tgt tool [ 0.299 -0.17   0.141]
         270 +step 875 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 33, 'obstruction1': 33, 'obstruction2': 33, 'obstruction7': 33} tool [ 0.299 -0.17   0.25 ] end [ 0.279 -0.105  0.141]
         271 +ABORT step 883 tool [ 0.28  -0.105  0.196] q [-0.528  0.232 -2.077 -2.177 -0.266 -0.869 -0.871] target [-0.369  0.372 -2.204 -2.266 -0.469 -0.705 -0.668] tgt tool [ 0.279 -0.105  0.141]
         272 +step 884 task obstruction1 grasp 0.0 plan 13 fails {'obstruction0': 34, 'obstruction1': 33, 'obstruction2': 33, 'obstruction7': 33} tool [ 0.28  -0.105  0.25 ] end [ 0.345 -0.167  0.141]
         273 +ABORT step 888 tool [ 0.345 -0.167  0.174] q [-0.241  0.494 -2.167 -1.964 -0.505 -0.948 -0.586] target [-0.193  0.552 -2.224 -2.008 -0.58  -0.864 -0.523] tgt tool [ 0.345 -0.167  0.141]
         274 +step 890 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 34, 'obstruction1': 34, 'obstruction2': 33, 'obstruction7': 33} tool [ 0.345 -0.167  0.25 ] end [ 0.34  -0.106  0.141]
         275 +ABORT step 894 tool [ 0.34  -0.106  0.177] q [-0.44   0.432 -2.138 -2.044 -0.464 -0.909 -0.753] target [-0.374  0.5   -2.209 -2.094 -0.557 -0.815 -0.671] tgt tool [ 0.34  -0.106  0.141]
         276 +step 896 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 34, 'obstruction1': 34, 'obstruction2': 34, 'obstruction7': 33} tool [ 0.34  -0.106  0.25 ] end [ 0.274 -0.17   0.141]
         277 +ABORT step 904 tool [ 0.274 -0.17   0.18 ] q [-0.442  0.533 -1.731 -2.144 -0.636 -1.006 -1.822] target [-0.345  0.594 -1.85  -2.202 -0.75  -0.91  -1.729] tgt tool [ 0.274 -0.17   0.141]
         278 +step 905 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 34, 'obstruction1': 34, 'obstruction2': 34, 'obstruction7': 34} tool [ 0.274 -0.17   0.25 ] end [ 0.298 -0.124  0.141]
         279 +step 909 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 35, 'obstruction1': 34, 'obstruction2': 34, 'obstruction7': 34} tool [ 0.298 -0.124  0.141] end [ 0.345 -0.154  0.141]
         280 +ABORT step 918 tool [ 0.345 -0.154  0.188] q [-0.501  0.948 -1.439 -1.966 -0.947 -1.444 -3.246] target [-0.469  1.014 -1.524 -2.032 -1.046 -1.37  -3.19 ] tgt tool [ 0.345 -0.154  0.141]
         281 +step 919 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 35, 'obstruction1': 35, 'obstruction2': 34, 'obstruction7': 34} tool [ 0.345 -0.154  0.25 ] end [ 0.335 -0.138  0.141]
         282 +step 923 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 35, 'obstruction1': 35, 'obstruction2': 35, 'obstruction7': 34} tool [ 0.335 -0.138  0.141] end [ 0.269 -0.176  0.141]
         283 +ABORT step 927 tool [ 0.269 -0.176  0.188] q [-0.449  0.859 -1.374 -2.132 -0.866 -1.347 -3.039] target [-0.391  0.921 -1.487 -2.204 -0.984 -1.261 -2.965] tgt tool [ 0.269 -0.176  0.141]
         284 +step 928 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 35, 'obstruction1': 35, 'obstruction2': 35, 'obstruction7': 35} tool [ 0.269 -0.176  0.25 ] end [ 0.26  -0.124  0.141]
         285 +ABORT step 936 tool [ 0.261 -0.124  0.2  ] q [-0.728  0.431 -1.578 -2.2   -0.518 -1.003 -2.009] target [-0.514  0.52  -1.818 -2.3   -0.705 -0.838 -1.851] tgt tool [ 0.26  -0.124  0.141]
         286 +step 937 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 36, 'obstruction1': 35, 'obstruction2': 35, 'obstruction7': 35} tool [ 0.261 -0.124  0.25 ] end [ 0.317 -0.173  0.141]
         287 +ABORT step 944 tool [ 0.317 -0.173  0.25 ] q [-0.493  0.845 -1.318 -1.902 -0.811 -1.532 -3.222] target [-0.412  0.987 -1.515 -2.085 -1.028 -1.338 -3.089] tgt tool [ 0.317 -0.173  0.141]
         288 +step 945 task obstruction2 grasp 0.0 plan 14 fails {'obstruction0': 36, 'obstruction1': 36, 'obstruction2': 35, 'obstruction7': 35} tool [ 0.317 -0.173  0.28 ] end [ 0.335 -0.1    0.141]
         289 +ABORT step 949 tool [ 0.335 -0.1    0.177] q [-0.662  0.998 -1.36  -2.069 -0.972 -1.466 -3.275] target [-0.636  1.05  -1.432 -2.121 -1.055 -1.412 -3.232] tgt tool [ 0.335 -0.1    0.141]
         290 +step 950 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 36, 'obstruction1': 36, 'obstruction2': 36, 'obstruction7': 35} tool [ 0.335 -0.1    0.25 ] end [ 0.269 -0.163  0.141]
         291 +ABORT step 953 tool [ 0.269 -0.163  0.25 ] q [-0.558  0.794 -1.221 -2.029 -0.738 -1.48  -3.138] target [-0.452  0.903 -1.434 -2.204 -0.945 -1.287 -3.005] tgt tool [ 0.269 -0.163  0.155]
         292 +step 954 task obstruction0 grasp 0.0 plan 17 fails {'obstruction0': 36, 'obstruction1': 36, 'obstruction2': 36, 'obstruction7': 36} tool [ 0.269 -0.163  0.28 ] end [ 0.292 -0.117  0.141]
         293 +ABORT step 962 tool [ 0.292 -0.117  0.211] q [-0.721  0.469 -1.625 -2.108 -0.54  -1.073 -2.074] target [-0.529  0.575 -1.85  -2.224 -0.737 -0.891 -1.91 ] tgt tool [ 0.292 -0.117  0.141]
         294 +step 963 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 37, 'obstruction1': 36, 'obstruction2': 36, 'obstruction7': 36} tool [ 0.292 -0.117  0.25 ] end [ 0.34  -0.173  0.141]
         295 +ABORT step 970 tool [ 0.34  -0.173  0.25 ] q [-0.48   0.858 -1.361 -1.844 -0.833 -1.546 -3.279] target [-0.412  1.003 -1.542 -2.022 -1.04  -1.357 -3.152] tgt tool [ 0.34  -0.173  0.141]
         296 +step 971 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 37, 'obstruction1': 37, 'obstruction2': 36, 'obstruction7': 36} tool [ 0.34  -0.173  0.28 ] end [ 0.325 -0.119  0.165]
         297 +step 975 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 37, 'obstruction1': 37, 'obstruction2': 37, 'obstruction7': 36} tool [ 0.325 -0.119  0.165] end [ 0.275 -0.182  0.141]
         298 +ABORT step 979 tool [ 0.275 -0.182  0.188] q [-0.426  0.868 -1.389 -2.109 -0.876 -1.357 -3.041] target [-0.372  0.931 -1.497 -2.18  -0.991 -1.273 -2.97 ] tgt tool [ 0.275 -0.182  0.141]
         299 +step 980 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 37, 'obstruction1': 37, 'obstruction2': 37, 'obstruction7': 37} tool [ 0.275 -0.182  0.25 ] end [ 0.267 -0.117  0.141]
         300 +ABORT step 988 tool [ 0.267 -0.117  0.197] q [-0.739  0.455 -1.583 -2.198 -0.545 -1.01  -2.012] target [-0.547  0.538 -1.804 -2.292 -0.721 -0.855 -1.865] tgt tool [ 0.267 -0.117  0.141]
         301 +step 989 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 38, 'obstruction1': 37, 'obstruction2': 37, 'obstruction7': 37} tool [ 0.267 -0.117  0.25 ] end [ 0.317 -0.148  0.141]
         302 +ABORT step 996 tool [ 0.317 -0.148  0.25 ] q [-0.573  0.863 -1.27  -1.934 -0.812 -1.55  -3.247] target [-0.491  1.005 -1.473 -2.12  -1.034 -1.36  -3.114] tgt tool [ 0.317 -0.148  0.141]
         303 +step 997 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 38, 'obstruction1': 38, 'obstruction2': 37, 'obstruction7': 37} tool [ 0.317 -0.148  0.28 ] end [ 0.325 -0.119  0.165]
         304 +time 96.97848534584045
diff --git a/d121.txt b/d121.txt
new file mode 100644
index 0000000..bd97f86
--- /dev/null
+++ b/d121.txt
@@ -0,0 +1,23 @@
           1 +obstruction0 [0.269 0.247 0.098] [0.01  0.018 0.023]
           2 +obstruction1 [0.342 0.058 0.107] [0.017 0.013 0.022]
           3 +obstruction2 [0.3   0.098 0.108] [0.016 0.015 0.023]
           4 +obstruction3 [0.354 0.102 0.111] [0.013 0.015 0.026]
           5 +obstruction4 [ 0.31  -0.147  0.087] [0.011 0.018 0.012]
           6 +obstruction5 [0.284 0.058 0.097] [0.013 0.018 0.012]
           7 +obstruction6 [ 0.45  -0.062  0.086] [0.014 0.017 0.011]
           8 +obstruction7 [ 0.301 -0.205  0.103] [0.019 0.016 0.028]
           9 +obstruction8 [ 0.232 -0.066  0.104] [0.012 0.017 0.029]
          10 +target_block [ 0.281 -0.085  0.1  ] [0.031 0.023 0.025]
          11 +target_region [0.326 0.069 0.08 ] [0.039 0.029 0.005]
          12 +step 1 task obstruction1 grasp 0.0 plan 12 fails {} tool [0.154 0.001 0.217] end [0.342 0.058 0.156]
          13 +step 12 task obstruction1 grasp 1.0 plan 17 fails {} tool [0.342 0.058 0.156] end [0.347 0.193 0.148]
          14 +step 19 task obstruction2 grasp 0.0 plan 14 fails {} tool [0.347 0.193 0.148] end [0.318 0.098 0.141]
          15 +step 29 task obstruction2 grasp 1.0 plan 17 fails {} tool [0.318 0.098 0.141] end [0.224 0.195 0.133]
          16 +step 37 task obstruction3 grasp 0.0 plan 14 fails {} tool [0.224 0.195 0.133] end [0.354 0.102 0.141]
          17 +step 44 task obstruction3 grasp 1.0 plan 16 fails {} tool [0.354 0.102 0.141] end [0.403 0.195 0.133]
          18 +step 51 task obstruction5 grasp 0.0 plan 15 fails {} tool [0.403 0.195 0.133] end [0.284 0.058 0.132]
          19 +step 57 task obstruction5 grasp 1.0 plan 16 fails {} tool [0.284 0.058 0.132] end [0.183 0.058 0.124]
          20 +step 64 task target_block grasp 0.0 plan 15 fails {} tool [0.183 0.058 0.124] end [ 0.27  -0.085  0.131]
          21 +step 73 task target_block grasp 1.0 plan 18 fails {} tool [ 0.27  -0.085  0.131] end [0.314 0.069 0.143]
          22 +SOLVED 80
          23 +time 4.384406089782715
diff --git a/probe6.py b/probe6.py
new file mode 100644
index 0000000..b740b4e
--- /dev/null
+++ b/probe6.py
@@ -0,0 +1,19 @@
           1 +import sys, numpy as np, kin, importlib as _il
           2 +from env_client import make_env
           3 +from common import *
           4 +GA = _il.import_module("approach_v2").GeneratedApproach
           5 +env = make_env()
           6 +obs, info = env.reset(seed=101, options={'object_count': 9})
           7 +ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +N=int(sys.argv[1])
           9 +for t in range(N):
          10 +    a=ap.get_action(obs); q0=getq(obs)
          11 +    obs, *_ = env.step(a)
          12 +    print(t, 'act', np.round(a[3:10],3), 'moved', np.abs(getq(obs)-q0).max()>1e-7, 'tool', np.round(kin.fk(getbase(obs),getq(obs))[:3,3],3))
          13 +q0=getq(obs); b=getbase(obs); T=kin.fk(b, q0); print('tool', T[:3,3])
          14 +q=q0
          15 +for k in range(1,20):
          16 +    q,ok=kin.ik(b, q, T[:3,3]-np.array([0,0,(0.024 if k>1 else 0)+0.001*k]), T[:3,:3], iters=100, tol=1e-7)
          17 +    obs,bl=move_to(env, obs, q, grip=0.0, maxd=0.2)
          18 +    print(k, 'blocked', bl, np.round(kin.fk(b, getq(obs))[:3,3],3))
          19 +    if bl: break
diff --git a/probe7.py b/probe7.py
new file mode 100644
index 0000000..f09f8db
--- /dev/null
+++ b/probe7.py
@@ -0,0 +1,11 @@
           1 +import numpy as np, kin, importlib as _il
           2 +from env_client import make_env
           3 +GA = _il.import_module("approach_v2").GeneratedApproach
           4 +env = make_env()
           5 +obs, info = env.reset(seed=101, options={'object_count': 9})
           6 +ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +for t in range(15): obs,*_=env.step(ap.get_action(obs))
           8 +objs=ap._parse(obs)
           9 +for n in ['obstruction0','obstruction1','obstruction2','obstruction7']:
          10 +    c=ap._grasp_candidates(objs[n], objs)
          11 +    print(n, [ (round(x[0],3), round(np.degrees(x[1])%360), round(x[2],3), round(x[3],3), x[4], round(x[5],3)) for x in c[:4]])
```

</details>

<a id="C021"></a>
### C021 · sweep-box check uses conservative height; finger check tight

Commit `3afee96798a374b3260180034484cbdba363f557`; parents: 118102da2098c2321a43a70488f1c6a7d3532842. Recorded author date: 2026-09-30T23:38:26+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0964](01_timeline.md#E0964): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C021_3afee96.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index 5ba989b..1d2c701 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -201,14 +201,16 @@ class GeneratedApproach:
  201    201              sds = np.linspace(-smax, smax, 7) if smax > 0 else [0.0]
  202    202              sas = np.linspace(-amax, amax, 7) if amax > 0 else [0.0]
  203    203              for zi, zg in enumerate(zs):
  204        -                tip = zg - 0.0305
  205        -                rel = [(n, b) for n, b in near if b.top > tip]
         204 +                tip = zg - 0.0315
         205 +                rel = [(n, b) for n, b in near if b.top > zg - 0.042]
  206    206                  for sd in sds:
  207    207                      for sa in sas:
  208    208                          x, y = o.p[:2] + sd * d + sa * a
  209        -                        boxes = self._finger_boxes(x, y, yaw) + [(np.array([x, y]), d, a, 0.043, 0.011)]
         209 +                        fboxes = self._finger_boxes(x, y, yaw)
         210 +                        sbox = (np.array([x, y]), d, a, 0.043, 0.011)
  210    211                          blockers = []
  211    212                          for n, b in rel:
         213 +                            boxes = ([sbox] + fboxes) if b.top > tip else [sbox]
  212    214                              for box in boxes:
  213    215                                  if self._box_hits_obj(box, b):
  214    216                                      blockers.append(n)
diff --git a/d101.txt b/d101.txt
index 3d2b80f..3595e87 100644
--- a/d101.txt
+++ b/d101.txt
@@ -9,296 +9,17 @@ obstruction7 [ 0.286 -0.17   0.107] [0.014 0.012 0.022]
    9      9  obstruction8 [ 0.478 -0.016  0.099] [0.014 0.014 0.024]
   10     10  target_block [ 0.419 -0.102  0.1  ] [0.039 0.025 0.025]
   11     11  target_region [ 0.328 -0.152  0.08 ] [0.048 0.031 0.005]
   12        -step 1 task obstruction3 grasp 0.0 plan 15 fails {} tool [0.154 0.001 0.217] end [ 0.359 -0.176  0.141]
   13        -step 8 task obstruction3 grasp 1.0 plan 16 fails {} tool [ 0.359 -0.176  0.141] end [ 0.352 -0.284  0.133]
   14        -step 15 task obstruction0 grasp 0.0 plan 15 fails {} tool [ 0.352 -0.284  0.133] end [ 0.279 -0.124  0.141]
   15        -ABORT step 20 tool [ 0.279 -0.124  0.188] q [ 0.103  0.189 -2.771 -2.157 -0.094 -0.81   2.104] target [ 0.14   0.295 -2.795 -2.231 -0.167 -0.638  2.178] tgt tool [ 0.279 -0.124  0.141]
   16        -step 22 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 1} tool [ 0.279 -0.124  0.25 ] end [ 0.328 -0.161  0.141]
   17        -ABORT step 25 tool [ 0.329 -0.161  0.188] q [ 0.156  0.315 -2.757 -1.985 -0.153 -0.869  2.194] target [ 0.187  0.404 -2.785 -2.052 -0.21  -0.72   2.247] tgt tool [ 0.328 -0.161  0.141]
   18        -step 26 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 1, 'obstruction1': 1} tool [ 0.329 -0.161  0.25 ] end [ 0.325 -0.119  0.141]
   19        -ABORT step 29 tool [ 0.325 -0.119  0.19 ] q [ 0.062  0.269 -2.782 -2.04  -0.125 -0.853  2.063] target [ 0.094  0.366 -2.808 -2.112 -0.185 -0.69   2.121] tgt tool [ 0.325 -0.119  0.141]
   20        -step 31 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 1, 'obstruction1': 1, 'obstruction2': 1} tool [ 0.325 -0.119  0.25 ] end [ 0.286 -0.17   0.141]
   21        -ABORT step 34 tool [ 0.286 -0.17   0.191] q [ 0.188  0.243 -2.717 -2.077 -0.133 -0.846  2.262] target [ 0.229  0.348 -2.749 -2.153 -0.21  -0.677  2.336] tgt tool [ 0.286 -0.17   0.141]
   22        -step 35 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 1, 'obstruction1': 1, 'obstruction2': 1, 'obstruction7': 1} tool [ 0.286 -0.17   0.25 ] end [ 0.279 -0.124  0.141]
   23        -ABORT step 45 tool [ 0.28  -0.124  0.195] q [ 0.213  0.173 -2.9   -2.141 -0.056 -0.833  3.629] target [ 0.238  0.291 -2.916 -2.228 -0.108 -0.633  3.683] tgt tool [ 0.279 -0.124  0.141]
   24        -step 46 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 2, 'obstruction1': 1, 'obstruction2': 1, 'obstruction7': 1} tool [ 0.28  -0.124  0.25 ] end [ 0.323 -0.161  0.141]
   25        -ABORT step 56 tool [ 0.323 -0.161  0.188] q [ 0.141  0.306 -2.732 -2.    -0.159 -0.865  2.208] target [ 0.175  0.397 -2.762 -2.068 -0.22  -0.715  2.266] tgt tool [ 0.323 -0.161  0.141]
   26        -step 58 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 2, 'obstruction1': 2, 'obstruction2': 1, 'obstruction7': 1} tool [ 0.323 -0.161  0.25 ] end [ 0.319 -0.119  0.141]
   27        -ABORT step 61 tool [ 0.32  -0.119  0.19 ] q [ 0.045  0.259 -2.757 -2.054 -0.128 -0.851  2.074] target [ 0.081  0.359 -2.786 -2.128 -0.195 -0.685  2.138] tgt tool [ 0.319 -0.119  0.141]
   28        -step 62 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 2, 'obstruction1': 2, 'obstruction2': 2, 'obstruction7': 1} tool [ 0.32  -0.119  0.25 ] end [ 0.281 -0.17   0.141]
   29        -ABORT step 65 tool [ 0.281 -0.17   0.191] q [ 0.172  0.234 -2.689 -2.091 -0.136 -0.844  2.275] target [ 0.217  0.341 -2.723 -2.168 -0.22  -0.672  2.357] tgt tool [ 0.281 -0.17   0.141]
   30        -step 67 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 2, 'obstruction1': 2, 'obstruction2': 2, 'obstruction7': 2} tool [ 0.281 -0.17   0.25 ] end [ 0.274 -0.124  0.141]
   31        -ABORT step 70 tool [ 0.274 -0.124  0.195] q [ 0.068  0.167 -2.727 -2.159 -0.091 -0.832  2.109] target [ 0.114  0.289 -2.756 -2.246 -0.182 -0.635  2.203] tgt tool [ 0.274 -0.124  0.141]
   32        -step 71 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 3, 'obstruction1': 2, 'obstruction2': 2, 'obstruction7': 2} tool [ 0.274 -0.124  0.25 ] end [ 0.334 -0.161  0.141]
   33        -ABORT step 74 tool [ 0.334 -0.161  0.187] q [ 0.124  0.33  -2.721 -1.972 -0.174 -0.874  2.208] target [ 0.157  0.416 -2.751 -2.037 -0.232 -0.731  2.262] tgt tool [ 0.334 -0.161  0.141]
   34        -step 75 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 3, 'obstruction1': 3, 'obstruction2': 2, 'obstruction7': 2} tool [ 0.334 -0.161  0.25 ] end [ 0.33  -0.119  0.141]
   35        -ABORT step 78 tool [ 0.33  -0.119  0.189] q [ 0.028  0.282 -2.743 -2.028 -0.144 -0.857  2.078] target [ 0.063  0.378 -2.773 -2.099 -0.208 -0.699  2.139] tgt tool [ 0.33  -0.119  0.141]
   36        -step 80 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 3, 'obstruction1': 3, 'obstruction2': 3, 'obstruction7': 2} tool [ 0.33  -0.119  0.25 ] end [ 0.292 -0.17   0.141]
   37        -ABORT step 83 tool [ 0.292 -0.17   0.19 ] q [ 0.154  0.258 -2.681 -2.066 -0.151 -0.85   2.272] target [ 0.198  0.359 -2.716 -2.139 -0.231 -0.686  2.349] tgt tool [ 0.292 -0.17   0.141]
   38        -step 85 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 3, 'obstruction1': 3, 'obstruction2': 3, 'obstruction7': 3} tool [ 0.292 -0.17   0.25 ] end [ 0.285 -0.124  0.141]
   39        -ABORT step 88 tool [ 0.285 -0.124  0.193] q [ 0.049  0.19  -2.714 -2.136 -0.106 -0.835  2.112] target [ 0.095  0.307 -2.745 -2.219 -0.195 -0.647  2.202] tgt tool [ 0.285 -0.124  0.141]
   40        -step 89 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 4, 'obstruction1': 3, 'obstruction2': 3, 'obstruction7': 3} tool [ 0.285 -0.124  0.25 ] end [ 0.328 -0.167  0.141]
   41        -ABORT step 92 tool [ 0.329 -0.167  0.187] q [ 0.127  0.327 -2.697 -1.98  -0.182 -0.873  2.24 ] target [ 0.162  0.414 -2.729 -2.044 -0.244 -0.73   2.297] tgt tool [ 0.328 -0.167  0.141]
   42        -step 93 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 4, 'obstruction1': 4, 'obstruction2': 3, 'obstruction7': 3} tool [ 0.329 -0.167  0.25 ] end [ 0.325 -0.125  0.141]
   43        -ABORT step 96 tool [ 0.325 -0.125  0.189] q [ 0.029  0.278 -2.718 -2.036 -0.15  -0.856  2.109] target [ 0.067  0.375 -2.75  -2.107 -0.219 -0.698  2.174] tgt tool [ 0.325 -0.125  0.141]
   44        -step 98 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 4, 'obstruction1': 4, 'obstruction2': 4, 'obstruction7': 3} tool [ 0.325 -0.125  0.25 ] end [ 0.286 -0.176  0.141]
   45        -ABORT step 101 tool [ 0.286 -0.176  0.19 ] q [ 0.157  0.256 -2.655 -2.071 -0.159 -0.849  2.306] target [ 0.203  0.359 -2.692 -2.144 -0.243 -0.686  2.388] tgt tool [ 0.286 -0.176  0.141]
   46        -step 103 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 4, 'obstruction1': 4, 'obstruction2': 4, 'obstruction7': 4} tool [ 0.286 -0.176  0.25 ] end [ 0.279 -0.13   0.141]
   47        -ABORT step 106 tool [ 0.28  -0.13   0.194] q [ 0.05   0.187 -2.687 -2.142 -0.11  -0.835  2.143] target [ 0.099  0.305 -2.72  -2.225 -0.206 -0.647  2.24 ] tgt tool [ 0.279 -0.13   0.141]
   48        -step 107 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 5, 'obstruction1': 4, 'obstruction2': 4, 'obstruction7': 4} tool [ 0.28 -0.13  0.25] end [ 0.328 -0.154  0.141]
   49        -ABORT step 110 tool [ 0.329 -0.154  0.187] q [ 0.088  0.315 -2.69  -1.996 -0.179 -0.868  2.207] target [ 0.124  0.404 -2.723 -2.062 -0.244 -0.722  2.268] tgt tool [ 0.328 -0.154  0.141]
   50        -step 111 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 5, 'obstruction1': 5, 'obstruction2': 4, 'obstruction7': 4} tool [ 0.329 -0.154  0.25 ] end [ 0.325 -0.112  0.141]
   51        -ABORT step 114 tool [ 0.325 -0.112  0.19 ] q [-0.011  0.269 -2.713 -2.048 -0.147 -0.853  2.072] target [ 0.028  0.367 -2.746 -2.12  -0.219 -0.692  2.141] tgt tool [ 0.325 -0.112  0.141]
   52        -step 116 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 5, 'obstruction1': 5, 'obstruction2': 5, 'obstruction7': 4} tool [ 0.325 -0.112  0.25 ] end [ 0.286 -0.163  0.141]
   53        -ABORT step 119 tool [ 0.286 -0.163  0.191] q [ 0.114  0.241 -2.647 -2.088 -0.152 -0.846  2.268] target [ 0.163  0.347 -2.685 -2.164 -0.242 -0.678  2.356] tgt tool [ 0.286 -0.163  0.141]
   54        -step 120 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 5, 'obstruction1': 5, 'obstruction2': 5, 'obstruction7': 5} tool [ 0.286 -0.163  0.25 ] end [ 0.279 -0.118  0.141]
   55        -ABORT step 123 tool [ 0.28  -0.118  0.194] q [ 0.006  0.174 -2.683 -2.155 -0.104 -0.833  2.099] target [ 0.056  0.296 -2.715 -2.241 -0.203 -0.64   2.201] tgt tool [ 0.279 -0.118  0.141]
   56        -step 124 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 6, 'obstruction1': 5, 'obstruction2': 5, 'obstruction7': 5} tool [ 0.28  -0.118  0.25 ] end [ 0.328 -0.161  0.141]
   57        -ABORT step 133 tool [ 0.329 -0.161  0.185] q [-0.032  0.348 -2.506 -1.996 -0.266 -0.879  0.746] target [ 0.017  0.432 -2.553 -2.058 -0.349 -0.749  0.822] tgt tool [ 0.328 -0.161  0.141]
   58        -step 135 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 6, 'obstruction1': 6, 'obstruction2': 5, 'obstruction7': 5} tool [ 0.329 -0.161  0.25 ] end [ 0.335 -0.119  0.141]
   59        -ABORT step 144 tool [ 0.335 -0.119  0.189] q [ 0.052  0.291 -2.776 -2.013 -0.136 -0.86   2.063] target [ 0.083  0.384 -2.803 -2.083 -0.194 -0.704  2.118] tgt tool [ 0.335 -0.119  0.141]
   60        -step 145 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 6, 'obstruction1': 6, 'obstruction2': 6, 'obstruction7': 5} tool [ 0.335 -0.119  0.25 ] end [ 0.286 -0.17   0.141]
   61        -ABORT step 154 tool [ 0.286 -0.17   0.189] q [ 0.018  0.267 -2.502 -2.086 -0.211 -0.851  0.781] target [ 0.081  0.369 -2.553 -2.158 -0.317 -0.697  0.884] tgt tool [ 0.286 -0.17   0.141]
   62        -step 156 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 6, 'obstruction1': 6, 'obstruction2': 6, 'obstruction7': 6} tool [ 0.286 -0.17   0.25 ] end [ 0.286 -0.124  0.141]
   63        -ABORT step 159 tool [ 0.286 -0.124  0.192] q [-0.105  0.208 -2.53  -2.14  -0.16  -0.837  0.605] target [-0.037  0.325 -2.578 -2.22  -0.281 -0.663  0.726] tgt tool [ 0.286 -0.124  0.141]
   64        -step 160 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 7, 'obstruction1': 6, 'obstruction2': 6, 'obstruction7': 6} tool [ 0.286 -0.124  0.25 ] end [ 0.317 -0.161  0.141]
   65        -ABORT step 169 tool [ 0.317 -0.161  0.182] q [-0.148  0.361 -2.336 -2.034 -0.337 -0.88  -0.727] target [-0.084  0.443 -2.398 -2.092 -0.435 -0.762 -0.637] tgt tool [ 0.317 -0.161  0.141]
   66        -step 171 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 7, 'obstruction1': 7, 'obstruction2': 6, 'obstruction7': 6} tool [ 0.317 -0.161  0.25 ] end [ 0.319 -0.125  0.141]
   67        -ABORT step 174 tool [ 0.32  -0.125  0.184] q [-0.256  0.327 -2.338 -2.068 -0.308 -0.867 -0.846] target [-0.185  0.417 -2.403 -2.13  -0.417 -0.739 -0.745] tgt tool [ 0.319 -0.125  0.141]
   68        -step 176 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 7, 'obstruction1': 7, 'obstruction2': 7, 'obstruction7': 6} tool [ 0.32  -0.125  0.25 ] end [ 0.275 -0.17   0.141]
   69        -ABORT step 179 tool [ 0.275 -0.17   0.186] q [-0.141  0.286 -2.278 -2.123 -0.289 -0.851 -0.675] target [-0.052  0.387 -2.354 -2.191 -0.42  -0.715 -0.548] tgt tool [ 0.275 -0.17   0.141]
   70        -step 181 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 7, 'obstruction1': 7, 'obstruction2': 7, 'obstruction7': 7} tool [ 0.275 -0.17   0.25 ] end [ 0.273 -0.124  0.141]
   71        -ABORT step 190 tool [ 0.273 -0.124  0.193] q [-0.155  0.184 -2.461 -2.171 -0.156 -0.833  0.623] target [-0.074  0.311 -2.516 -2.255 -0.299 -0.654  0.768] tgt tool [ 0.273 -0.124  0.141]
   72        -step 191 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 8, 'obstruction1': 7, 'obstruction2': 7, 'obstruction7': 7} tool [ 0.273 -0.124  0.25 ] end [ 0.34  -0.161  0.141]
   73        -ABORT step 200 tool [ 0.34  -0.161  0.179] q [-0.184  0.427 -2.291 -1.98  -0.405 -0.912 -0.693] target [-0.13   0.497 -2.348 -2.031 -0.488 -0.81  -0.621] tgt tool [ 0.34  -0.161  0.141]
   74        -step 202 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 8, 'obstruction1': 8, 'obstruction2': 7, 'obstruction7': 7} tool [ 0.34  -0.161  0.25 ] end [ 0.33  -0.125  0.141]
   75        -ABORT step 205 tool [ 0.33  -0.125  0.181] q [-0.299  0.371 -2.274 -2.046 -0.366 -0.883 -0.799] target [-0.231  0.452 -2.341 -2.102 -0.467 -0.77  -0.707] tgt tool [ 0.33  -0.125  0.141]
   76        -step 207 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 8, 'obstruction1': 8, 'obstruction2': 8, 'obstruction7': 7} tool [ 0.33  -0.125  0.25 ] end [ 0.281 -0.176  0.141]
   77        -ABORT step 210 tool [ 0.281 -0.176  0.183] q [-0.163  0.327 -2.22  -2.106 -0.344 -0.863 -0.61 ] target [-0.077  0.418 -2.299 -2.168 -0.465 -0.742 -0.496] tgt tool [ 0.281 -0.176  0.141]
   78        -step 212 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 8, 'obstruction1': 8, 'obstruction2': 8, 'obstruction7': 8} tool [ 0.281 -0.176  0.25 ] end [ 0.279 -0.117  0.141]
   79        -ABORT step 221 tool [ 0.28  -0.117  0.192] q [-0.208  0.196 -2.429 -2.165 -0.173 -0.834  0.613] target [-0.124  0.321 -2.488 -2.247 -0.317 -0.662  0.759] tgt tool [ 0.279 -0.117  0.141]
   80        -step 222 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 9, 'obstruction1': 8, 'obstruction2': 8, 'obstruction7': 8} tool [ 0.28  -0.117  0.25 ] end [ 0.323 -0.167  0.141]
   81        -ABORT step 231 tool [ 0.323 -0.167  0.179] q [-0.194  0.413 -2.239 -2.018 -0.413 -0.902 -0.64 ] target [-0.133  0.485 -2.303 -2.07  -0.504 -0.8   -0.559] tgt tool [ 0.323 -0.167  0.141]
   82        -step 233 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 9, 'obstruction1': 9, 'obstruction2': 8, 'obstruction7': 8} tool [ 0.323 -0.167  0.25 ] end [ 0.319 -0.112  0.141]
   83        -ABORT step 237 tool [ 0.32  -0.112  0.182] q [-0.373  0.348 -2.223 -2.087 -0.362 -0.871 -0.817] target [-0.294  0.434 -2.299 -2.146 -0.476 -0.755 -0.712] tgt tool [ 0.319 -0.112  0.141]
   84        -step 239 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 9, 'obstruction1': 9, 'obstruction2': 9, 'obstruction7': 8} tool [ 0.32  -0.112  0.25 ] end [ 0.292 -0.176  0.141]
   85        -ABORT step 243 tool [ 0.292 -0.176  0.181] q [-0.184  0.364 -2.195 -2.083 -0.386 -0.877 -0.587] target [-0.106  0.446 -2.271 -2.14  -0.496 -0.766 -0.486] tgt tool [ 0.292 -0.176  0.141]
   86        -step 245 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 9, 'obstruction1': 9, 'obstruction2': 9, 'obstruction7': 9} tool [ 0.292 -0.176  0.25 ] end [ 0.269 -0.124  0.141]
   87        -ABORT step 249 tool [ 0.269 -0.124  0.194] q [-0.417  0.219 -2.13  -2.186 -0.247 -0.854 -0.823] target [-0.273  0.356 -2.242 -2.271 -0.442 -0.692 -0.626] tgt tool [ 0.269 -0.124  0.141]
   88        -step 250 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 10, 'obstruction1': 9, 'obstruction2': 9, 'obstruction7': 9} tool [ 0.269 -0.124  0.25 ] end [ 0.334 -0.167  0.141]
   89        -ABORT step 254 tool [ 0.334 -0.167  0.176] q [-0.227  0.458 -2.19  -1.992 -0.468 -0.926 -0.603] target [-0.172  0.521 -2.251 -2.04  -0.55  -0.835 -0.532] tgt tool [ 0.334 -0.167  0.141]
   90        -step 256 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 10, 'obstruction1': 10, 'obstruction2': 9, 'obstruction7': 9} tool [ 0.334 -0.167  0.25 ] end [ 0.33  -0.112  0.141]
   91        -ABORT step 260 tool [ 0.33  -0.112  0.179] q [-0.407  0.397 -2.167 -2.064 -0.425 -0.892 -0.764] target [-0.334  0.472 -2.241 -2.117 -0.526 -0.79  -0.673] tgt tool [ 0.33  -0.112  0.141]
   92        -step 262 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 10, 'obstruction1': 10, 'obstruction2': 10, 'obstruction7': 9} tool [ 0.33  -0.112  0.25 ] end [ 0.281 -0.163  0.141]
   93        -ABORT step 265 tool [ 0.281 -0.163  0.181] q [-0.271  0.345 -2.117 -2.131 -0.389 -0.865 -0.585] target [-0.177  0.431 -2.207 -2.189 -0.513 -0.754 -0.469] tgt tool [ 0.281 -0.163  0.141]
   94        -step 267 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 10, 'obstruction1': 10, 'obstruction2': 10, 'obstruction7': 10} tool [ 0.281 -0.163  0.25 ] end [ 0.29  -0.124  0.141]
   95        -ABORT step 270 tool [ 0.29  -0.124  0.185] q [-0.421  0.308 -2.105 -2.151 -0.352 -0.862 -0.742] target [-0.308  0.409 -2.207 -2.218 -0.497 -0.736 -0.603] tgt tool [ 0.29  -0.124  0.141]
   96        -step 271 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 11, 'obstruction1': 10, 'obstruction2': 10, 'obstruction7': 10} tool [ 0.29  -0.124  0.25 ] end [ 0.323 -0.154  0.141]
   97        -ABORT step 274 tool [ 0.323 -0.154  0.177] q [-0.287  0.431 -2.15  -2.039 -0.459 -0.909 -0.616] target [-0.221  0.499 -2.22  -2.089 -0.552 -0.815 -0.534] tgt tool [ 0.323 -0.154  0.141]
   98        -step 276 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 11, 'obstruction1': 11, 'obstruction2': 10, 'obstruction7': 10} tool [ 0.323 -0.154  0.25 ] end [ 0.325 -0.131  0.141]
   99        -ABORT step 279 tool [ 0.325 -0.131  0.178] q [-0.363  0.413 -2.142 -2.061 -0.446 -0.899 -0.685] target [-0.292  0.484 -2.215 -2.112 -0.545 -0.801 -0.597] tgt tool [ 0.325 -0.131  0.141]
  100        -step 281 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 11, 'obstruction1': 11, 'obstruction2': 11, 'obstruction7': 10} tool [ 0.325 -0.131  0.25 ] end [ 0.292 -0.163  0.141]
  101        -ABORT step 284 tool [ 0.292 -0.163  0.179] q [-0.276  0.378 -2.113 -2.106 -0.423 -0.88  -0.572] target [-0.191  0.456 -2.197 -2.16  -0.535 -0.776 -0.47 ] tgt tool [ 0.292 -0.163  0.141]
  102        -step 286 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 11, 'obstruction1': 11, 'obstruction2': 11, 'obstruction7': 11} tool [ 0.292 -0.163  0.25 ] end [ 0.274 -0.13   0.141]
  103        -ABORT step 289 tool [ 0.274 -0.13   0.195] q [-0.462  0.265 -2.033 -2.166 -0.309 -0.88  -0.738] target [-0.305  0.395 -2.167 -2.251 -0.502 -0.725 -0.55 ] tgt tool [ 0.274 -0.13   0.141]
  104        -step 290 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 12, 'obstruction1': 11, 'obstruction2': 11, 'obstruction7': 11} tool [ 0.274 -0.13   0.25 ] end [ 0.334 -0.154  0.141]
  105        -ABORT step 294 tool [ 0.334 -0.154  0.175] q [-0.301  0.47  -2.126 -2.012 -0.501 -0.931 -0.593] target [-0.244  0.531 -2.191 -2.058 -0.584 -0.845 -0.522] tgt tool [ 0.334 -0.154  0.141]
  106        -step 296 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 12, 'obstruction1': 12, 'obstruction2': 11, 'obstruction7': 11} tool [ 0.334 -0.154  0.25 ] end [ 0.325 -0.106  0.141]
  107        -ABORT step 300 tool [ 0.325 -0.106  0.177] q [-0.473  0.408 -2.093 -2.088 -0.457 -0.894 -0.733] target [-0.395  0.48  -2.173 -2.14  -0.561 -0.798 -0.641] tgt tool [ 0.325 -0.106  0.141]
  108        -step 302 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 12, 'obstruction1': 12, 'obstruction2': 12, 'obstruction7': 11} tool [ 0.325 -0.106  0.25 ] end [ 0.286 -0.182  0.141]
  109        -ABORT step 306 tool [ 0.286 -0.182  0.177] q [-0.23   0.407 -2.082 -2.094 -0.459 -0.893 -0.478] target [-0.15   0.479 -2.164 -2.146 -0.564 -0.797 -0.384] tgt tool [ 0.286 -0.182  0.141]
  110        -step 308 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 12, 'obstruction1': 12, 'obstruction2': 12, 'obstruction7': 12} tool [ 0.286 -0.182  0.25 ] end [ 0.285 -0.13   0.141]
  111        -ABORT step 312 tool [ 0.285 -0.13   0.188] q [-0.456  0.32  -2.023 -2.153 -0.377 -0.88  -0.682] target [-0.325  0.425 -2.143 -2.225 -0.534 -0.75  -0.533] tgt tool [ 0.285 -0.13   0.141]
  112        -step 313 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 13, 'obstruction1': 12, 'obstruction2': 12, 'obstruction7': 12} tool [ 0.285 -0.13   0.25 ] end [ 0.328 -0.173  0.141]
  113        -ABORT step 317 tool [ 0.329 -0.173  0.174] q [-0.254  0.489 -2.107 -2.004 -0.522 -0.942 -0.52 ] target [-0.2    0.547 -2.17  -2.048 -0.602 -0.86  -0.452] tgt tool [ 0.328 -0.173  0.141]
  114        -step 319 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 13, 'obstruction1': 13, 'obstruction2': 12, 'obstruction7': 12} tool [ 0.329 -0.173  0.25 ] end [ 0.34  -0.119  0.141]
  115        -ABORT step 322 tool [ 0.34  -0.119  0.175] q [-0.428  0.465 -2.091 -2.036 -0.508 -0.927 -0.675] target [-0.366  0.526 -2.16  -2.083 -0.595 -0.841 -0.6  ] tgt tool [ 0.34  -0.119  0.141]
  116        -step 324 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 13, 'obstruction1': 13, 'obstruction2': 13, 'obstruction7': 12} tool [ 0.34  -0.119  0.25 ] end [ 0.286 -0.157  0.141]
  117        -ABORT step 327 tool [ 0.286 -0.157  0.178] q [-0.337  0.384 -2.043 -2.131 -0.448 -0.88  -0.544] target [-0.246  0.46  -2.135 -2.185 -0.563 -0.781 -0.439] tgt tool [ 0.286 -0.157  0.141]
  118        -step 329 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 13, 'obstruction1': 13, 'obstruction2': 13, 'obstruction7': 13} tool [ 0.286 -0.157  0.25 ] end [ 0.274 -0.118  0.141]
  119        -ABORT step 333 tool [ 0.275 -0.118  0.201] q [-0.585  0.258 -1.937 -2.17  -0.309 -0.901 -0.766] target [-0.387  0.404 -2.107 -2.267 -0.53  -0.732 -0.55 ] tgt tool [ 0.274 -0.118  0.141]
  120        -step 334 task obstruction1 grasp 0.0 plan 12 fails {'obstruction0': 14, 'obstruction1': 13, 'obstruction2': 13, 'obstruction7': 13} tool [ 0.275 -0.118  0.25 ] end [ 0.328 -0.148  0.141]
  121        -ABORT step 338 tool [ 0.329 -0.148  0.174] q [-0.353  0.476 -2.067 -2.038 -0.526 -0.934 -0.568] target [-0.292  0.536 -2.136 -2.083 -0.611 -0.85  -0.494] tgt tool [ 0.328 -0.148  0.141]
  122        -step 339 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 14, 'obstruction1': 14, 'obstruction2': 13, 'obstruction7': 13} tool [ 0.329 -0.148  0.25 ] end [ 0.335 -0.125  0.141]
  123        -ABORT step 342 tool [ 0.335 -0.125  0.174] q [-0.426  0.471 -2.061 -2.046 -0.523 -0.93  -0.634] target [-0.363  0.532 -2.132 -2.091 -0.611 -0.846 -0.559] tgt tool [ 0.335 -0.125  0.141]
  124        -step 344 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 14, 'obstruction1': 14, 'obstruction2': 14, 'obstruction7': 13} tool [ 0.335 -0.125  0.25 ] end [ 0.286 -0.175  0.141]
  125        -ABORT step 352 tool [ 0.286 -0.175  0.168] q [-0.422  0.666 -1.673 -2.125 -0.769 -1.084 -1.698] target [-0.37   0.705 -1.748 -2.164 -0.843 -1.024 -1.643] tgt tool [ 0.286 -0.175  0.141]
  126        -step 353 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 14, 'obstruction1': 14, 'obstruction2': 14, 'obstruction7': 14} tool [ 0.286 -0.175  0.25 ] end [ 0.285 -0.118  0.141]
  127        -ABORT step 360 tool [ 0.285 -0.118  0.192] q [-0.571  0.33  -1.92  -2.161 -0.397 -0.904 -0.684] target [-0.413  0.441 -2.07  -2.241 -0.572 -0.765 -0.52 ] tgt tool [ 0.285 -0.118  0.141]
  128        -step 362 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction1': 14, 'obstruction2': 14, 'obstruction7': 14} tool [ 0.285 -0.118  0.25 ] end [ 0.328 -0.166  0.141]
  129        -ABORT step 370 tool [ 0.329 -0.166  0.159] q [-0.43   0.759 -1.708 -2.039 -0.846 -1.147 -1.754] target [-0.405  0.786 -1.749 -2.063 -0.89  -1.11  -1.723] tgt tool [ 0.328 -0.166  0.141]
  130        -step 371 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction1': 15, 'obstruction2': 14, 'obstruction7': 14} tool [ 0.329 -0.166  0.25 ] end [ 0.335 -0.112  0.141]
  131        -ABORT step 379 tool [ 0.335 -0.112  0.174] q [-0.477  0.469 -2.04  -2.059 -0.528 -0.929 -0.658] target [-0.411  0.53  -2.114 -2.105 -0.617 -0.845 -0.581] tgt tool [ 0.335 -0.112  0.141]
  132        -step 380 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction1': 15, 'obstruction2': 15, 'obstruction7': 14} tool [ 0.335 -0.112  0.25 ] end [ 0.286 -0.165  0.141]
  133        -ABORT step 388 tool [ 0.286 -0.165  0.17 ] q [-0.464  0.666 -1.647 -2.136 -0.767 -1.092 -1.713] target [-0.407  0.707 -1.729 -2.178 -0.848 -1.026 -1.653] tgt tool [ 0.286 -0.165  0.141]
  134        -step 389 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction1': 15, 'obstruction2': 15, 'obstruction7': 15} tool [ 0.286 -0.165  0.25 ] end [ 0.279 -0.137  0.141]
  135        -ABORT step 397 tool [ 0.28  -0.137  0.188] q [-0.48   0.343 -1.947 -2.159 -0.412 -0.896 -0.61 ] target [-0.34   0.445 -2.081 -2.231 -0.571 -0.768 -0.462] tgt tool [ 0.279 -0.137  0.141]
  136        -step 399 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 16, 'obstruction1': 15, 'obstruction2': 15, 'obstruction7': 15} tool [ 0.28  -0.137  0.25 ] end [ 0.335 -0.161  0.141]
  137        -ABORT step 406 tool [ 0.335 -0.161  0.25 ] q [-0.551  0.657 -1.534 -1.874 -0.675 -1.354 -1.905] target [-0.44   0.776 -1.716 -2.035 -0.863 -1.148 -1.766] tgt tool [ 0.335 -0.161  0.155]
  138        -step 407 task obstruction2 grasp 0.0 plan 17 fails {'obstruction0': 16, 'obstruction1': 16, 'obstruction2': 15, 'obstruction7': 15} tool [ 0.335 -0.161  0.28 ] end [ 0.319 -0.131  0.141]
  139        -ABORT step 415 tool [ 0.32  -0.131  0.206] q [-0.496  0.395 -1.961 -2.03  -0.437 -1.    -0.668] target [-0.357  0.516 -2.105 -2.129 -0.612 -0.832 -0.513] tgt tool [ 0.319 -0.131  0.141]
  140        -step 416 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 16, 'obstruction1': 16, 'obstruction2': 16, 'obstruction7': 15} tool [ 0.32  -0.131  0.25 ] end [ 0.293 -0.17   0.141]
  141        -ABORT step 424 tool [ 0.293 -0.17   0.166] q [-0.439  0.698 -1.656 -2.119 -0.797 -1.108 -1.693] target [-0.395  0.734 -1.722 -2.155 -0.865 -1.054 -1.643] tgt tool [ 0.293 -0.17   0.141]
  142        -step 425 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 16, 'obstruction1': 16, 'obstruction2': 16, 'obstruction7': 16} tool [ 0.293 -0.17   0.25 ] end [ 0.279 -0.111  0.141]
  143        -ABORT step 432 tool [ 0.28  -0.111  0.202] q [-0.664  0.302 -1.841 -2.162 -0.366 -0.93  -0.721] target [-0.454  0.437 -2.036 -2.262 -0.581 -0.762 -0.516] tgt tool [ 0.279 -0.111  0.141]
  144        -step 433 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 17, 'obstruction1': 16, 'obstruction2': 16, 'obstruction7': 16} tool [ 0.28  -0.111  0.25 ] end [ 0.322 -0.161  0.141]
  145        -ABORT step 440 tool [ 0.322 -0.161  0.159] q [-0.455  0.767 -1.674 -2.064 -0.855 -1.155 -1.734] target [-0.43   0.794 -1.716 -2.089 -0.901 -1.119 -1.702] tgt tool [ 0.322 -0.161  0.141]
  146        -step 441 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 17, 'obstruction1': 17, 'obstruction2': 16, 'obstruction7': 16} tool [ 0.322 -0.161  0.25 ] end [ 0.33  -0.131  0.141]
  147        -ABORT step 449 tool [ 0.33  -0.131  0.174] q [-0.423  0.478 -2.032 -2.055 -0.538 -0.934 -0.593] target [-0.359  0.537 -2.105 -2.1   -0.625 -0.852 -0.518] tgt tool [ 0.33  -0.131  0.141]
  148        -step 450 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 17, 'obstruction1': 17, 'obstruction2': 17, 'obstruction7': 16} tool [ 0.33  -0.131  0.25 ] end [ 0.28  -0.17   0.141]
  149        -ABORT step 458 tool [ 0.28  -0.17   0.171] q [-0.452  0.676 -1.624 -2.144 -0.775 -1.103 -1.675] target [-0.394  0.717 -1.707 -2.187 -0.858 -1.037 -1.614] tgt tool [ 0.28  -0.17   0.141]
  150        -step 459 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 17, 'obstruction1': 17, 'obstruction2': 17, 'obstruction7': 17} tool [ 0.28 -0.17  0.25] end [ 0.292 -0.124  0.141]
  151        -ABORT step 462 tool [ 0.292 -0.124  0.173] q [-0.626  0.698 -1.558 -2.169 -0.789 -1.132 -1.776] target [-0.564  0.74  -1.651 -2.217 -0.879 -1.061 -1.711] tgt tool [ 0.292 -0.124  0.141]
  152        -step 463 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 18, 'obstruction1': 17, 'obstruction2': 17, 'obstruction7': 17} tool [ 0.292 -0.124  0.25 ] end [ 0.345 -0.161  0.141]
  153        -ABORT step 472 tool [ 0.345 -0.161  0.172] q [-0.297  0.518 -2.099 -1.977 -0.549 -0.961 -0.552] target [-0.248  0.572 -2.158 -2.018 -0.622 -0.884 -0.491] tgt tool [ 0.345 -0.161  0.141]
  154        -step 473 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 18, 'obstruction1': 18, 'obstruction2': 17, 'obstruction7': 17} tool [ 0.345 -0.161  0.25 ] end [ 0.319 -0.106  0.141]
  155        -ABORT step 477 tool [ 0.32  -0.106  0.176] q [-0.506  0.419 -2.039 -2.105 -0.482 -0.898 -0.695] target [-0.425  0.488 -2.124 -2.155 -0.586 -0.806 -0.603] tgt tool [ 0.319 -0.106  0.141]
  156        -step 479 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 18, 'obstruction1': 18, 'obstruction2': 18, 'obstruction7': 17} tool [ 0.32  -0.106  0.25 ] end [ 0.269 -0.17   0.141]
  157        -ABORT step 482 tool [ 0.269 -0.17   0.182] q [-0.32   0.364 -2.    -2.148 -0.432 -0.884 -0.491] target [-0.209  0.451 -2.109 -2.209 -0.566 -0.773 -0.368] tgt tool [ 0.269 -0.17   0.141]
  158        -step 483 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 18, 'obstruction1': 18, 'obstruction2': 18, 'obstruction7': 18} tool [ 0.269 -0.17   0.25 ] end [ 0.267 -0.124  0.141]
  159        -ABORT step 492 tool [ 0.267 -0.124  0.191] q [-0.376  0.21  -2.181 -2.195 -0.232 -0.838  0.731] target [-0.245  0.342 -2.279 -2.277 -0.417 -0.681  0.919] tgt tool [ 0.267 -0.124  0.141]
  160        -step 493 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 19, 'obstruction1': 18, 'obstruction2': 18, 'obstruction7': 18} tool [ 0.267 -0.124  0.25 ] end [ 0.317 -0.167  0.141]
  161        -ABORT step 501 tool [ 0.317 -0.167  0.173] q [-0.322  0.499 -2.013 -2.046 -0.562 -0.947 -0.465] target [-0.262  0.555 -2.083 -2.089 -0.645 -0.869 -0.394] tgt tool [ 0.317 -0.167  0.141]
  162        -step 502 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 19, 'obstruction1': 19, 'obstruction2': 18, 'obstruction7': 18} tool [ 0.317 -0.167  0.25 ] end [ 0.33  -0.106  0.141]
  163        -ABORT step 506 tool [ 0.33  -0.106  0.174] q [-0.529  0.478 -1.983 -2.081 -0.552 -0.934 -0.636] target [-0.459  0.537 -2.062 -2.126 -0.643 -0.852 -0.558] tgt tool [ 0.33  -0.106  0.141]
  164        -step 507 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 19, 'obstruction1': 19, 'obstruction2': 19, 'obstruction7': 18} tool [ 0.33  -0.106  0.25 ] end [ 0.275 -0.176  0.141]
  165        -ABORT step 510 tool [ 0.275 -0.176  0.176] q [-0.309  0.42  -1.971 -2.135 -0.5   -0.898 -0.415] target [-0.219  0.488 -2.066 -2.186 -0.609 -0.807 -0.318] tgt tool [ 0.275 -0.176  0.141]
  166        -step 511 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 19, 'obstruction1': 19, 'obstruction2': 19, 'obstruction7': 19} tool [ 0.275 -0.176  0.25 ] end [ 0.286 -0.117  0.141]
  167        -ABORT step 519 tool [ 0.286 -0.117  0.187] q [-0.373  0.259 -2.211 -2.163 -0.279 -0.841  0.73 ] target [-0.266  0.37  -2.299 -2.234 -0.431 -0.702  0.879] tgt tool [ 0.286 -0.117  0.141]
  168        -step 521 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 20, 'obstruction1': 19, 'obstruction2': 19, 'obstruction7': 19} tool [ 0.286 -0.117  0.25 ] end [ 0.34  -0.167  0.141]
  169        -ABORT step 529 tool [ 0.34  -0.167  0.169] q [-0.33   0.567 -1.995 -1.99  -0.624 -0.994 -0.448] target [-0.285  0.614 -2.053 -2.027 -0.692 -0.927 -0.393] tgt tool [ 0.34  -0.167  0.141]
  170        -step 530 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 20, 'obstruction1': 20, 'obstruction2': 19, 'obstruction7': 19} tool [ 0.34  -0.167  0.25 ] end [ 0.325 -0.138  0.141]
  171        -step 534 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 20, 'obstruction1': 20, 'obstruction2': 20, 'obstruction7': 19} tool [ 0.325 -0.138  0.141] end [ 0.275 -0.163  0.141]
  172        -ABORT step 537 tool [ 0.275 -0.163  0.188] q [-0.421  0.409 -1.872 -2.136 -0.49  -0.939 -0.443] target [-0.291  0.498 -2.009 -2.207 -0.636 -0.817 -0.313] tgt tool [ 0.275 -0.163  0.141]
  173        -step 538 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 20, 'obstruction1': 20, 'obstruction2': 20, 'obstruction7': 20} tool [ 0.275 -0.163  0.25 ] end [ 0.273 -0.117  0.141]
  174        -ABORT step 546 tool [ 0.273 -0.117  0.173] q [-0.663  0.773 -1.424 -2.226 -0.832 -1.208 -1.659] target [-0.605  0.812 -1.52  -2.276 -0.924 -1.14  -1.596] tgt tool [ 0.273 -0.117  0.141]
  175        -step 547 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 21, 'obstruction1': 20, 'obstruction2': 20, 'obstruction7': 20} tool [ 0.273 -0.117  0.25 ] end [ 0.317 -0.154  0.141]
  176        -ABORT step 555 tool [ 0.317 -0.154  0.172] q [-0.382  0.503 -1.974 -2.064 -0.576 -0.95  -0.474] target [-0.318  0.558 -2.048 -2.107 -0.661 -0.873 -0.402] tgt tool [ 0.317 -0.154  0.141]
  177        -step 556 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 21, 'obstruction1': 21, 'obstruction2': 20, 'obstruction7': 20} tool [ 0.317 -0.154  0.25 ] end [ 0.325 -0.1    0.141]
  178        -ABORT step 560 tool [ 0.325 -0.1    0.174] q [-0.575  0.481 -1.939 -2.101 -0.565 -0.937 -0.626] target [-0.5    0.54  -2.023 -2.148 -0.659 -0.855 -0.546] tgt tool [ 0.325 -0.1    0.141]
  179        -step 561 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 21, 'obstruction1': 21, 'obstruction2': 21, 'obstruction7': 20} tool [ 0.325 -0.1    0.25 ] end [ 0.281 -0.182  0.141]
  180        -ABORT step 565 tool [ 0.281 -0.182  0.175] q [-0.293  0.452 -1.962 -2.114 -0.533 -0.918 -0.379] target [-0.212  0.515 -2.05  -2.162 -0.633 -0.832 -0.292] tgt tool [ 0.281 -0.182  0.141]
  181        -step 566 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 21, 'obstruction1': 21, 'obstruction2': 21, 'obstruction7': 21} tool [ 0.281 -0.182  0.25 ] end [ 0.279 -0.11   0.141]
  182        -ABORT step 574 tool [ 0.28 -0.11  0.19] q [-0.431  0.235 -2.172 -2.182 -0.26  -0.842  0.701] target [-0.306  0.358 -2.271 -2.259 -0.433 -0.693  0.874] tgt tool [ 0.279 -0.11   0.141]
  183        -step 575 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 22, 'obstruction1': 21, 'obstruction2': 21, 'obstruction7': 21} tool [ 0.28 -0.11  0.25] end [ 0.34  -0.154  0.141]
  184        -ABORT step 583 tool [ 0.34  -0.154  0.17 ] q [-0.374  0.559 -1.982 -2.006 -0.621 -0.989 -0.475] target [-0.326  0.607 -2.043 -2.044 -0.692 -0.921 -0.417] tgt tool [ 0.34  -0.154  0.141]
  185        -step 584 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 22, 'obstruction1': 22, 'obstruction2': 21, 'obstruction7': 21} tool [ 0.34  -0.154  0.25 ] end [ 0.306 -0.119  0.141]
  186        -step 594 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 22, 'obstruction1': 22, 'obstruction2': 22, 'obstruction7': 21} tool [ 0.306 -0.119  0.141] end [ 0.292 -0.182  0.141]
  187        -ABORT step 602 tool [ 0.292 -0.182  0.188] q [-0.383  1.074 -1.248 -2.067 -0.986 -1.589 -2.94 ] target [-0.357  1.145 -1.337 -2.137 -1.09  -1.527 -2.893] tgt tool [ 0.292 -0.182  0.141]
  188        -step 603 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 22, 'obstruction1': 22, 'obstruction2': 22, 'obstruction7': 22} tool [ 0.292 -0.182  0.25 ] end [ 0.264 -0.124  0.141]
  189        -ABORT step 605 tool [ 0.264 -0.124  0.25 ] q [-0.593  0.994 -1.01  -2.086 -0.797 -1.69  -3.001] target [-0.531  1.126 -1.198 -2.269 -0.999 -1.546 -2.896] tgt tool [ 0.264 -0.124  0.155]
  190        -step 606 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 23, 'obstruction1': 22, 'obstruction2': 22, 'obstruction7': 22} tool [ 0.264 -0.124  0.28 ] end [ 0.323 -0.173  0.141]
  191        -ABORT step 609 tool [ 0.323 -0.173  0.175] q [-0.407  1.128 -1.286 -2.021 -1.051 -1.613 -3.022] target [-0.394  1.18  -1.345 -2.069 -1.122 -1.571 -2.992] tgt tool [ 0.323 -0.173  0.141]
  192        -step 610 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 23, 'obstruction1': 23, 'obstruction2': 22, 'obstruction7': 22} tool [ 0.323 -0.173  0.25 ] end [ 0.34  -0.125  0.141]
  193        -ABORT step 612 tool [ 0.34  -0.125  0.25 ] q [-0.56   1.056 -1.13  -1.898 -0.932 -1.766 -3.192] target [-0.529  1.222 -1.3   -2.081 -1.135 -1.624 -3.101] tgt tool [ 0.34  -0.125  0.141]
  194        -step 613 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 23, 'obstruction1': 23, 'obstruction2': 23, 'obstruction7': 22} tool [ 0.34  -0.125  0.28 ] end [ 0.281 -0.157  0.141]
  195        -ABORT step 616 tool [ 0.281 -0.157  0.181] q [-0.458  1.068 -1.223 -2.142 -0.968 -1.562 -2.94 ] target [-0.431  1.13  -1.307 -2.204 -1.065 -1.508 -2.895] tgt tool [ 0.281 -0.157  0.141]
  196        -step 617 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 23, 'obstruction1': 23, 'obstruction2': 23, 'obstruction7': 23} tool [ 0.281 -0.157  0.25 ] end [ 0.295 -0.124  0.141]
  197        -ABORT step 619 tool [ 0.295 -0.124  0.25 ] q [-0.59   1.012 -1.069 -2.015 -0.849 -1.711 -3.087] target [-0.534  1.171 -1.268 -2.21  -1.075 -1.559 -2.978] tgt tool [ 0.295 -0.124  0.141]
  198        -step 620 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 24, 'obstruction1': 23, 'obstruction2': 23, 'obstruction7': 23} tool [ 0.295 -0.124  0.28 ] end [ 0.334 -0.173  0.141]
  199        -ABORT step 623 tool [ 0.334 -0.173  0.173] q [-0.41   1.127 -1.309 -1.993 -1.061 -1.608 -3.06 ] target [-0.398  1.177 -1.364 -2.038 -1.129 -1.568 -3.032] tgt tool [ 0.334 -0.173  0.141]
  200        -step 624 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 24, 'obstruction1': 24, 'obstruction2': 23, 'obstruction7': 23} tool [ 0.334 -0.173  0.25 ] end [ 0.34  -0.112  0.141]
  201        -ABORT step 626 tool [ 0.34  -0.112  0.25 ] q [-0.601  1.05  -1.126 -1.91  -0.923 -1.758 -3.221] target [-0.568  1.215 -1.299 -2.094 -1.129 -1.615 -3.127] tgt tool [ 0.34  -0.112  0.141]
  202        -step 627 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 24, 'obstruction1': 24, 'obstruction2': 24, 'obstruction7': 23} tool [ 0.34  -0.112  0.28 ] end [ 0.292 -0.157  0.141]
  203        -ABORT step 630 tool [ 0.292 -0.157  0.18 ] q [-0.463  1.068 -1.25  -2.117 -0.982 -1.557 -2.98 ] target [-0.438  1.127 -1.328 -2.175 -1.073 -1.505 -2.937] tgt tool [ 0.292 -0.157  0.141]
  204        -step 631 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 24, 'obstruction1': 24, 'obstruction2': 24, 'obstruction7': 24} tool [ 0.292 -0.157  0.25 ] end [ 0.269 -0.13   0.141]
  205        -ABORT step 633 tool [ 0.269 -0.13   0.25 ] q [-0.59   0.965 -1.051 -2.068 -0.799 -1.658 -3.034] target [-0.524  1.094 -1.24  -2.249 -1.001 -1.507 -2.925] tgt tool [ 0.269 -0.13   0.155]
  206        -step 634 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 25, 'obstruction1': 24, 'obstruction2': 24, 'obstruction7': 24} tool [ 0.269 -0.13   0.28 ] end [ 0.323 -0.148  0.141]
  207        -ABORT step 637 tool [ 0.323 -0.148  0.176] q [-0.487  1.113 -1.272 -2.053 -1.031 -1.6   -3.068] target [-0.471  1.167 -1.337 -2.104 -1.108 -1.555 -3.035] tgt tool [ 0.323 -0.148  0.141]
  208        -step 638 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 25, 'obstruction1': 25, 'obstruction2': 24, 'obstruction7': 24} tool [ 0.323 -0.148  0.25 ] end [ 0.335 -0.131  0.141]
  209        -ABORT step 640 tool [ 0.335 -0.131  0.25 ] q [-0.556  1.026 -1.151 -1.906 -0.913 -1.73  -3.189] target [-0.518  1.188 -1.326 -2.089 -1.12  -1.581 -3.091] tgt tool [ 0.335 -0.131  0.141]
  210        -step 641 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 25, 'obstruction1': 25, 'obstruction2': 25, 'obstruction7': 24} tool [ 0.335 -0.131  0.28 ] end [ 0.286 -0.189  0.141]
  211        -ABORT step 644 tool [ 0.286 -0.189  0.178] q [-0.368  1.04  -1.305 -2.087 -0.985 -1.519 -2.936] target [-0.343  1.095 -1.378 -2.141 -1.07  -1.467 -2.894] tgt tool [ 0.286 -0.189  0.141]
  212        -step 645 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 25, 'obstruction1': 25, 'obstruction2': 25, 'obstruction7': 25} tool [ 0.286 -0.189  0.25 ] end [ 0.29  -0.13   0.141]
  213        -ABORT step 647 tool [ 0.29 -0.13  0.25] q [-0.586  0.979 -1.089 -2.021 -0.833 -1.674 -3.088] target [-0.521  1.133 -1.296 -2.216 -1.062 -1.512 -2.971] tgt tool [ 0.29  -0.13   0.141]
  214        -step 648 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 26, 'obstruction1': 25, 'obstruction2': 25, 'obstruction7': 25} tool [ 0.29 -0.13  0.28] end [ 0.334 -0.148  0.141]
  215        -ABORT step 651 tool [ 0.334 -0.148  0.175] q [-0.487  1.118 -1.292 -2.024 -1.045 -1.601 -3.102] target [-0.472  1.17  -1.352 -2.072 -1.117 -1.559 -3.071] tgt tool [ 0.334 -0.148  0.141]
  216        -step 652 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 26, 'obstruction1': 26, 'obstruction2': 25, 'obstruction7': 25} tool [ 0.334 -0.148  0.25 ] end [ 0.335 -0.106  0.141]
  217        -ABORT step 654 tool [ 0.335 -0.106  0.25 ] q [-0.631  1.034 -1.126 -1.929 -0.905 -1.738 -3.231] target [-0.591  1.196 -1.304 -2.115 -1.115 -1.591 -3.133] tgt tool [ 0.335 -0.106  0.141]
  218        -step 655 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 26, 'obstruction1': 26, 'obstruction2': 26, 'obstruction7': 25} tool [ 0.335 -0.106  0.28 ] end [ 0.286 -0.151  0.141]
  219        -ABORT step 658 tool [ 0.286 -0.151  0.181] q [-0.489  1.043 -1.249 -2.138 -0.962 -1.531 -2.989] target [-0.46   1.102 -1.333 -2.199 -1.058 -1.475 -2.942] tgt tool [ 0.286 -0.151  0.141]
  220        -step 659 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 26, 'obstruction1': 26, 'obstruction2': 26, 'obstruction7': 26} tool [ 0.286 -0.151  0.25 ] end [ 0.269 -0.118  0.141]
  221        -ABORT step 661 tool [ 0.269 -0.118  0.25 ] q [-0.641  0.957 -1.043 -2.081 -0.787 -1.648 -3.07 ] target [-0.571  1.083 -1.237 -2.264 -0.992 -1.494 -2.959] tgt tool [ 0.269 -0.118  0.155]
  222        -step 662 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 27, 'obstruction1': 26, 'obstruction2': 26, 'obstruction7': 26} tool [ 0.269 -0.118  0.28 ] end [ 0.328 -0.18   0.141]
  223        -ABORT step 666 tool [ 0.329 -0.18   0.174] q [-0.401  1.079 -1.35  -1.999 -1.035 -1.55  -3.064] target [-0.386  1.128 -1.407 -2.044 -1.104 -1.506 -3.032] tgt tool [ 0.328 -0.18   0.141]
  224        -step 667 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 27, 'obstruction1': 27, 'obstruction2': 26, 'obstruction7': 26} tool [ 0.329 -0.18   0.25 ] end [ 0.319 -0.138  0.141]
  225        -step 671 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 27, 'obstruction1': 27, 'obstruction2': 27, 'obstruction7': 26} tool [ 0.319 -0.138  0.141] end [ 0.286 -0.179  0.141]
  226        -ABORT step 680 tool [ 0.286 -0.179  0.188] q [-0.299  1.286 -1.048 -2.083 -1.047 -1.854 -4.345] target [-0.292  1.369 -1.126 -2.155 -1.147 -1.815 -4.322] tgt tool [ 0.286 -0.179  0.141]
  227        -step 681 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 27, 'obstruction1': 27, 'obstruction2': 27, 'obstruction7': 27} tool [ 0.286 -0.179  0.25 ] end [ 0.29  -0.118  0.141]
  228        -ABORT step 689 tool [ 0.29  -0.118  0.25 ] q [-0.671  0.901 -1.135 -2.034 -0.791 -1.589 -3.188] target [-0.595  1.022 -1.329 -2.211 -0.993 -1.423 -3.072] tgt tool [ 0.29  -0.118  0.155]
  229        -step 690 task obstruction1 grasp 0.0 plan 14 fails {'obstruction0': 28, 'obstruction1': 27, 'obstruction2': 27, 'obstruction7': 27} tool [ 0.29  -0.118  0.28 ] end [ 0.328 -0.142  0.141]
  230        -step 694 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 28, 'obstruction1': 28, 'obstruction2': 27, 'obstruction7': 27} tool [ 0.328 -0.142  0.141] end [ 0.33  -0.138  0.141]
  231        -step 698 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 28, 'obstruction1': 28, 'obstruction2': 28, 'obstruction7': 27} tool [ 0.33  -0.138  0.141] end [ 0.286 -0.16   0.141]
  232        -ABORT step 707 tool [ 0.286 -0.16   0.188] q [-0.383  1.232 -1.078 -2.112 -1.016 -1.783 -4.407] target [-0.37   1.313 -1.161 -2.185 -1.119 -1.74  -4.376] tgt tool [ 0.286 -0.16   0.141]
  233        -step 708 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 28, 'obstruction1': 28, 'obstruction2': 28, 'obstruction7': 28} tool [ 0.286 -0.16   0.25 ] end [ 0.274 -0.137  0.141]
  234        -ABORT step 717 tool [ 0.275 -0.137  0.163] q [-0.56   0.886 -1.396 -2.216 -0.915 -1.295 -3.088] target [-0.529  0.916 -1.454 -2.249 -0.976 -1.256 -3.05 ] tgt tool [ 0.274 -0.137  0.141]
  235        -step 718 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 29, 'obstruction1': 28, 'obstruction2': 28, 'obstruction7': 28} tool [ 0.275 -0.137  0.25 ] end [ 0.328 -0.172  0.141]
  236        -ABORT step 726 tool [ 0.328 -0.172  0.168] q [-0.353  0.597 -1.911 -2.017 -0.672 -1.016 -1.932] target [-0.308  0.64  -1.971 -2.053 -0.739 -0.954 -1.879] tgt tool [ 0.328 -0.172  0.141]
  237        -step 727 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 29, 'obstruction1': 29, 'obstruction2': 28, 'obstruction7': 28} tool [ 0.328 -0.172  0.25 ] end [ 0.319 -0.1    0.141]
  238        -ABORT step 735 tool [ 0.32  -0.1    0.182] q [-0.428  0.343 -2.202 -2.099 -0.364 -0.868 -0.847] target [-0.345  0.43  -2.281 -2.158 -0.481 -0.752 -0.738] tgt tool [ 0.319 -0.1    0.141]
  239        -step 737 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 29, 'obstruction1': 29, 'obstruction2': 29, 'obstruction7': 28} tool [ 0.32 -0.1   0.25] end [ 0.293 -0.175  0.141]
  240        -ABORT step 745 tool [ 0.293 -0.175  0.173] q [-0.352  0.509 -1.897 -2.1   -0.6   -0.957 -1.917] target [-0.281  0.564 -1.98  -2.145 -0.69  -0.879 -1.841] tgt tool [ 0.293 -0.175  0.141]
  241        -step 746 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 29, 'obstruction1': 29, 'obstruction2': 29, 'obstruction7': 29} tool [ 0.293 -0.175  0.25 ] end [ 0.285 -0.137  0.141]
  242        -ABORT step 754 tool [ 0.285 -0.137  0.163] q [-0.563  0.855 -1.448 -2.19  -0.905 -1.26  -3.147] target [-0.532  0.884 -1.505 -2.222 -0.964 -1.22  -3.109] tgt tool [ 0.285 -0.137  0.141]
  243        -step 755 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 30, 'obstruction1': 29, 'obstruction2': 29, 'obstruction7': 29} tool [ 0.285 -0.137  0.25 ] end [ 0.335 -0.166  0.141]
  244        -ABORT step 763 tool [ 0.335 -0.166  0.169] q [-0.353  0.581 -1.95  -2.006 -0.649 -1.004 -1.983] target [-0.308  0.626 -2.009 -2.043 -0.717 -0.94  -1.928] tgt tool [ 0.335 -0.166  0.141]
  245        -step 764 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 30, 'obstruction1': 30, 'obstruction2': 29, 'obstruction7': 29} tool [ 0.335 -0.166  0.25 ] end [ 0.33  -0.1    0.141]
  246        -ABORT step 772 tool [ 0.33  -0.1    0.182] q [-0.388  0.354 -2.258 -2.069 -0.356 -0.875 -0.872] target [-0.314  0.438 -2.329 -2.127 -0.465 -0.758 -0.773] tgt tool [ 0.33  -0.1    0.141]
  247        -step 774 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 30, 'obstruction1': 30, 'obstruction2': 30, 'obstruction7': 29} tool [ 0.33 -0.1   0.25] end [ 0.293 -0.165  0.141]
  248        -ABORT step 782 tool [ 0.293 -0.165  0.174] q [-0.366  0.469 -1.937 -2.112 -0.555 -0.93  -1.988] target [-0.288  0.53  -2.025 -2.159 -0.652 -0.846 -1.905] tgt tool [ 0.293 -0.165  0.141]
  249        -step 783 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 30, 'obstruction1': 30, 'obstruction2': 30, 'obstruction7': 30} tool [ 0.293 -0.165  0.25 ] end [ 0.274 -0.111  0.141]
  250        -ABORT step 791 tool [ 0.274 -0.111  0.195] q [-0.471  0.218 -2.122 -2.185 -0.246 -0.856 -0.87 ] target [-0.323  0.357 -2.237 -2.272 -0.445 -0.693 -0.669] tgt tool [ 0.274 -0.111  0.141]
  251        -step 792 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 31, 'obstruction1': 30, 'obstruction2': 30, 'obstruction7': 30} tool [ 0.274 -0.111  0.25 ] end [ 0.322 -0.166  0.141]
  252        -ABORT step 800 tool [ 0.322 -0.166  0.17 ] q [-0.357  0.55  -1.945 -2.038 -0.624 -0.983 -1.979] target [-0.303  0.599 -2.012 -2.078 -0.7   -0.913 -1.918] tgt tool [ 0.322 -0.166  0.141]
  253        -step 801 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 31, 'obstruction1': 31, 'obstruction2': 30, 'obstruction7': 30} tool [ 0.322 -0.166  0.25 ] end [ 0.306 -0.126  0.141]
  254        -step 806 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 31, 'obstruction1': 31, 'obstruction2': 31, 'obstruction7': 30} tool [ 0.306 -0.126  0.141] end [ 0.28  -0.175  0.141]
  255        -ABORT step 809 tool [ 0.28  -0.175  0.188] q [-0.382  0.444 -1.869 -2.107 -0.523 -0.964 -1.963] target [-0.264  0.529 -1.997 -2.177 -0.661 -0.845 -1.843] tgt tool [ 0.28  -0.175  0.141]
  256        -step 810 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 31, 'obstruction1': 31, 'obstruction2': 31, 'obstruction7': 31} tool [ 0.28  -0.175  0.25 ] end [ 0.285 -0.111  0.141]
  257        -ABORT step 818 tool [ 0.285 -0.111  0.189] q [-0.451  0.259 -2.136 -2.169 -0.292 -0.853 -0.836] target [-0.325  0.378 -2.241 -2.245 -0.46  -0.709 -0.671] tgt tool [ 0.285 -0.111  0.141]
  258        -step 819 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 32, 'obstruction1': 31, 'obstruction2': 31, 'obstruction7': 31} tool [ 0.285 -0.111  0.25 ] end [ 0.341 -0.161  0.141]
  259        -ABORT step 827 tool [ 0.341 -0.161  0.168] q [-0.378  0.604 -1.929 -1.998 -0.674 -1.022 -1.981] target [-0.336  0.646 -1.985 -2.033 -0.738 -0.961 -1.93 ] tgt tool [ 0.341 -0.161  0.141]
  260        -step 828 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 32, 'obstruction1': 32, 'obstruction2': 31, 'obstruction7': 31} tool [ 0.341 -0.161  0.25 ] end [ 0.306 -0.111  0.141]
  261        -step 833 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 32, 'obstruction1': 32, 'obstruction2': 32, 'obstruction7': 31} tool [ 0.306 -0.111  0.141] end [ 0.28  -0.165  0.141]
  262        -ABORT step 836 tool [ 0.28  -0.165  0.188] q [-0.438  0.454 -1.821 -2.122 -0.541 -0.972 -1.96 ] target [-0.316  0.537 -1.957 -2.193 -0.68  -0.854 -1.84 ] tgt tool [ 0.28  -0.165  0.141]
  263        -step 837 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 32, 'obstruction1': 32, 'obstruction2': 32, 'obstruction7': 32} tool [ 0.28  -0.165  0.25 ] end [ 0.279 -0.143  0.141]
  264        -step 846 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 33, 'obstruction1': 32, 'obstruction2': 32, 'obstruction7': 32} tool [ 0.279 -0.143  0.141] end [ 0.316 -0.161  0.141]
  265        -ABORT step 854 tool [ 0.316 -0.161  0.188] q [-0.439  0.542 -1.833 -2.037 -0.615 -1.043 -1.971] target [-0.35   0.617 -1.944 -2.104 -0.736 -0.932 -1.873] tgt tool [ 0.316 -0.161  0.141]
  266        -step 855 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 33, 'obstruction1': 33, 'obstruction2': 32, 'obstruction7': 32} tool [ 0.316 -0.161  0.25 ] end [ 0.34  -0.131  0.141]
  267        -ABORT step 864 tool [ 0.34  -0.131  0.179] q [-0.296  0.412 -2.249 -2.014 -0.409 -0.902 -0.755] target [-0.235  0.484 -2.312 -2.066 -0.499 -0.799 -0.674] tgt tool [ 0.34  -0.131  0.141]
  268        -step 866 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 33, 'obstruction1': 33, 'obstruction2': 33, 'obstruction7': 32} tool [ 0.34  -0.131  0.25 ] end [ 0.299 -0.17   0.141]
  269        -ABORT step 874 tool [ 0.299 -0.17   0.172] q [-0.372  0.525 -1.888 -2.092 -0.616 -0.968 -1.924] target [-0.305  0.578 -1.969 -2.136 -0.703 -0.893 -1.852] tgt tool [ 0.299 -0.17   0.141]
  270        -step 875 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 33, 'obstruction1': 33, 'obstruction2': 33, 'obstruction7': 33} tool [ 0.299 -0.17   0.25 ] end [ 0.279 -0.105  0.141]
  271        -ABORT step 883 tool [ 0.28  -0.105  0.196] q [-0.528  0.232 -2.077 -2.177 -0.266 -0.869 -0.871] target [-0.369  0.372 -2.204 -2.266 -0.469 -0.705 -0.668] tgt tool [ 0.279 -0.105  0.141]
  272        -step 884 task obstruction1 grasp 0.0 plan 13 fails {'obstruction0': 34, 'obstruction1': 33, 'obstruction2': 33, 'obstruction7': 33} tool [ 0.28  -0.105  0.25 ] end [ 0.345 -0.167  0.141]
  273        -ABORT step 888 tool [ 0.345 -0.167  0.174] q [-0.241  0.494 -2.167 -1.964 -0.505 -0.948 -0.586] target [-0.193  0.552 -2.224 -2.008 -0.58  -0.864 -0.523] tgt tool [ 0.345 -0.167  0.141]
  274        -step 890 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 34, 'obstruction1': 34, 'obstruction2': 33, 'obstruction7': 33} tool [ 0.345 -0.167  0.25 ] end [ 0.34  -0.106  0.141]
  275        -ABORT step 894 tool [ 0.34  -0.106  0.177] q [-0.44   0.432 -2.138 -2.044 -0.464 -0.909 -0.753] target [-0.374  0.5   -2.209 -2.094 -0.557 -0.815 -0.671] tgt tool [ 0.34  -0.106  0.141]
  276        -step 896 task obstruction7 grasp 0.0 plan 15 fails {'obstruction0': 34, 'obstruction1': 34, 'obstruction2': 34, 'obstruction7': 33} tool [ 0.34  -0.106  0.25 ] end [ 0.274 -0.17   0.141]
  277        -ABORT step 904 tool [ 0.274 -0.17   0.18 ] q [-0.442  0.533 -1.731 -2.144 -0.636 -1.006 -1.822] target [-0.345  0.594 -1.85  -2.202 -0.75  -0.91  -1.729] tgt tool [ 0.274 -0.17   0.141]
  278        -step 905 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 34, 'obstruction1': 34, 'obstruction2': 34, 'obstruction7': 34} tool [ 0.274 -0.17   0.25 ] end [ 0.298 -0.124  0.141]
  279        -step 909 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 35, 'obstruction1': 34, 'obstruction2': 34, 'obstruction7': 34} tool [ 0.298 -0.124  0.141] end [ 0.345 -0.154  0.141]
  280        -ABORT step 918 tool [ 0.345 -0.154  0.188] q [-0.501  0.948 -1.439 -1.966 -0.947 -1.444 -3.246] target [-0.469  1.014 -1.524 -2.032 -1.046 -1.37  -3.19 ] tgt tool [ 0.345 -0.154  0.141]
  281        -step 919 task obstruction2 grasp 0.0 plan 11 fails {'obstruction0': 35, 'obstruction1': 35, 'obstruction2': 34, 'obstruction7': 34} tool [ 0.345 -0.154  0.25 ] end [ 0.335 -0.138  0.141]
  282        -step 923 task obstruction7 grasp 0.0 plan 12 fails {'obstruction0': 35, 'obstruction1': 35, 'obstruction2': 35, 'obstruction7': 34} tool [ 0.335 -0.138  0.141] end [ 0.269 -0.176  0.141]
  283        -ABORT step 927 tool [ 0.269 -0.176  0.188] q [-0.449  0.859 -1.374 -2.132 -0.866 -1.347 -3.039] target [-0.391  0.921 -1.487 -2.204 -0.984 -1.261 -2.965] tgt tool [ 0.269 -0.176  0.141]
  284        -step 928 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 35, 'obstruction1': 35, 'obstruction2': 35, 'obstruction7': 35} tool [ 0.269 -0.176  0.25 ] end [ 0.26  -0.124  0.141]
  285        -ABORT step 936 tool [ 0.261 -0.124  0.2  ] q [-0.728  0.431 -1.578 -2.2   -0.518 -1.003 -2.009] target [-0.514  0.52  -1.818 -2.3   -0.705 -0.838 -1.851] tgt tool [ 0.26  -0.124  0.141]
  286        -step 937 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 36, 'obstruction1': 35, 'obstruction2': 35, 'obstruction7': 35} tool [ 0.261 -0.124  0.25 ] end [ 0.317 -0.173  0.141]
  287        -ABORT step 944 tool [ 0.317 -0.173  0.25 ] q [-0.493  0.845 -1.318 -1.902 -0.811 -1.532 -3.222] target [-0.412  0.987 -1.515 -2.085 -1.028 -1.338 -3.089] tgt tool [ 0.317 -0.173  0.141]
  288        -step 945 task obstruction2 grasp 0.0 plan 14 fails {'obstruction0': 36, 'obstruction1': 36, 'obstruction2': 35, 'obstruction7': 35} tool [ 0.317 -0.173  0.28 ] end [ 0.335 -0.1    0.141]
  289        -ABORT step 949 tool [ 0.335 -0.1    0.177] q [-0.662  0.998 -1.36  -2.069 -0.972 -1.466 -3.275] target [-0.636  1.05  -1.432 -2.121 -1.055 -1.412 -3.232] tgt tool [ 0.335 -0.1    0.141]
  290        -step 950 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 36, 'obstruction1': 36, 'obstruction2': 36, 'obstruction7': 35} tool [ 0.335 -0.1    0.25 ] end [ 0.269 -0.163  0.141]
  291        -ABORT step 953 tool [ 0.269 -0.163  0.25 ] q [-0.558  0.794 -1.221 -2.029 -0.738 -1.48  -3.138] target [-0.452  0.903 -1.434 -2.204 -0.945 -1.287 -3.005] tgt tool [ 0.269 -0.163  0.155]
  292        -step 954 task obstruction0 grasp 0.0 plan 17 fails {'obstruction0': 36, 'obstruction1': 36, 'obstruction2': 36, 'obstruction7': 36} tool [ 0.269 -0.163  0.28 ] end [ 0.292 -0.117  0.141]
  293        -ABORT step 962 tool [ 0.292 -0.117  0.211] q [-0.721  0.469 -1.625 -2.108 -0.54  -1.073 -2.074] target [-0.529  0.575 -1.85  -2.224 -0.737 -0.891 -1.91 ] tgt tool [ 0.292 -0.117  0.141]
  294        -step 963 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 37, 'obstruction1': 36, 'obstruction2': 36, 'obstruction7': 36} tool [ 0.292 -0.117  0.25 ] end [ 0.34  -0.173  0.141]
  295        -ABORT step 970 tool [ 0.34  -0.173  0.25 ] q [-0.48   0.858 -1.361 -1.844 -0.833 -1.546 -3.279] target [-0.412  1.003 -1.542 -2.022 -1.04  -1.357 -3.152] tgt tool [ 0.34  -0.173  0.141]
  296        -step 971 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 37, 'obstruction1': 37, 'obstruction2': 36, 'obstruction7': 36} tool [ 0.34  -0.173  0.28 ] end [ 0.325 -0.119  0.165]
  297        -step 975 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 37, 'obstruction1': 37, 'obstruction2': 37, 'obstruction7': 36} tool [ 0.325 -0.119  0.165] end [ 0.275 -0.182  0.141]
  298        -ABORT step 979 tool [ 0.275 -0.182  0.188] q [-0.426  0.868 -1.389 -2.109 -0.876 -1.357 -3.041] target [-0.372  0.931 -1.497 -2.18  -0.991 -1.273 -2.97 ] tgt tool [ 0.275 -0.182  0.141]
  299        -step 980 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 37, 'obstruction1': 37, 'obstruction2': 37, 'obstruction7': 37} tool [ 0.275 -0.182  0.25 ] end [ 0.267 -0.117  0.141]
  300        -ABORT step 988 tool [ 0.267 -0.117  0.197] q [-0.739  0.455 -1.583 -2.198 -0.545 -1.01  -2.012] target [-0.547  0.538 -1.804 -2.292 -0.721 -0.855 -1.865] tgt tool [ 0.267 -0.117  0.141]
  301        -step 989 task obstruction1 grasp 0.0 plan 15 fails {'obstruction0': 38, 'obstruction1': 37, 'obstruction2': 37, 'obstruction7': 37} tool [ 0.267 -0.117  0.25 ] end [ 0.317 -0.148  0.141]
  302        -ABORT step 996 tool [ 0.317 -0.148  0.25 ] q [-0.573  0.863 -1.27  -1.934 -0.812 -1.55  -3.247] target [-0.491  1.005 -1.473 -2.12  -1.034 -1.36  -3.114] tgt tool [ 0.317 -0.148  0.141]
  303        -step 997 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 38, 'obstruction1': 38, 'obstruction2': 37, 'obstruction7': 37} tool [ 0.317 -0.148  0.28 ] end [ 0.325 -0.119  0.165]
  304        -time 96.97848534584045
          12 +step 1 task obstruction0 grasp 0.0 plan 11 fails {} tool [0.154 0.001 0.217] end [ 0.279 -0.124  0.16 ]
          13 +step 7 task obstruction0 grasp 1.0 plan 17 fails {} tool [ 0.279 -0.124  0.16 ] end [ 0.282 -0.022  0.152]
          14 +step 14 task obstruction2 grasp 0.0 plan 14 fails {} tool [ 0.282 -0.022  0.152] end [ 0.306 -0.119  0.141]
          15 +step 23 task obstruction2 grasp 1.0 plan 19 fails {} tool [ 0.306 -0.119  0.141] end [ 0.303 -0.282  0.133]
          16 +step 31 task obstruction1 grasp 0.0 plan 16 fails {} tool [ 0.303 -0.282  0.133] end [ 0.328 -0.161  0.141]
          17 +step 40 task obstruction1 grasp 1.0 plan 18 fails {} tool [ 0.328 -0.161  0.141] end [ 0.384 -0.286  0.133]
          18 +step 47 task obstruction3 grasp 0.0 plan 16 fails {} tool [ 0.384 -0.286  0.133] end [ 0.376 -0.176  0.141]
          19 +step 56 task obstruction3 grasp 1.0 plan 18 fails {} tool [ 0.376 -0.176  0.141] end [ 0.369 -0.344  0.133]
          20 +step 63 task obstruction7 grasp 0.0 plan 14 fails {} tool [ 0.369 -0.344  0.133] end [ 0.286 -0.17   0.141]
          21 +step 72 task obstruction7 grasp 1.0 plan 17 fails {} tool [ 0.286 -0.17   0.141] end [ 0.264 -0.288  0.133]
          22 +step 79 task target_block grasp 0.0 plan 17 fails {} tool [ 0.264 -0.288  0.133] end [ 0.419 -0.102  0.131]
          23 +step 86 task target_block grasp 1.0 plan 17 fails {} tool [ 0.419 -0.102  0.131] end [ 0.328 -0.152  0.143]
          24 +SOLVED 93
          25 +time 6.1811769008636475
diff --git a/d113.txt b/d113.txt
new file mode 100644
index 0000000..f586687
--- /dev/null
+++ b/d113.txt
@@ -0,0 +1,119 @@
           1 +obstruction0 [ 0.321 -0.043  0.107] [0.017 0.015 0.022]
           2 +obstruction1 [ 0.43  -0.242  0.089] [0.018 0.018 0.014]
           3 +obstruction2 [ 0.321 -0.013  0.097] [0.018 0.012 0.012]
           4 +obstruction3 [ 0.477 -0.125  0.101] [0.014 0.02  0.026]
           5 +obstruction4 [0.272 0.217 0.093] [0.013 0.011 0.018]
           6 +obstruction5 [ 0.356 -0.049  0.11 ] [0.017 0.01  0.025]
           7 +obstruction6 [ 0.403 -0.013  0.091] [0.016 0.011 0.016]
           8 +obstruction7 [ 0.359 -0.018  0.113] [0.017 0.018 0.028]
           9 +obstruction8 [ 0.22  -0.148  0.087] [0.015 0.018 0.012]
          10 +target_block [ 0.299 -0.251  0.1  ] [0.018 0.02  0.025]
          11 +target_region [ 0.339 -0.03   0.08 ] [0.022 0.025 0.005]
          12 +step 1 task obstruction0 grasp 0.0 plan 13 fails {} tool [0.154 0.001 0.217] end [ 0.321 -0.043  0.141]
          13 +step 7 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 1} tool [ 0.321 -0.043  0.141] end [ 0.356 -0.053  0.162]
          14 +step 18 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 1, 'obstruction5': 1} tool [ 0.356 -0.053  0.162] end [ 0.359 -0.004  0.141]
          15 +step 22 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 1, 'obstruction5': 1, 'obstruction7': 1} tool [ 0.359 -0.004  0.141] end [ 0.321 -0.049  0.141]
          16 +step 32 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 2, 'obstruction5': 1, 'obstruction7': 1} tool [ 0.321 -0.049  0.141] end [ 0.356 -0.058  0.162]
          17 +step 42 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 2, 'obstruction5': 2, 'obstruction7': 1} tool [ 0.356 -0.058  0.162] end [ 0.365 -0.004  0.141]
          18 +step 46 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 2, 'obstruction5': 2, 'obstruction7': 2} tool [ 0.365 -0.004  0.141] end [ 0.321 -0.037  0.141]
          19 +step 55 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 3, 'obstruction5': 2, 'obstruction7': 2} tool [ 0.321 -0.037  0.141] end [ 0.363 -0.053  0.162]
          20 +step 65 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 3, 'obstruction5': 3, 'obstruction7': 2} tool [ 0.363 -0.053  0.162] end [ 0.352 -0.004  0.141]
          21 +step 69 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 3, 'obstruction5': 3, 'obstruction7': 3} tool [ 0.352 -0.004  0.141] end [ 0.314 -0.043  0.141]
          22 +step 78 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 4, 'obstruction5': 3, 'obstruction7': 3} tool [ 0.314 -0.043  0.141] end [ 0.35  -0.053  0.162]
          23 +step 88 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 4, 'obstruction5': 4, 'obstruction7': 3} tool [ 0.35  -0.053  0.162] end [0.359 0.003 0.141]
          24 +step 92 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 4, 'obstruction5': 4, 'obstruction7': 4} tool [0.359 0.003 0.141] end [ 0.314 -0.013  0.133]
          25 +ABORT step 100 tool [ 0.314 -0.013  0.191] q [-1.027  0.646 -1.526 -2.146 -0.721 -1.146 -3.765] target [-0.905  0.723 -1.7   -2.236 -0.884 -1.012 -3.645] tgt tool [ 0.314 -0.013  0.133]
          26 +step 101 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 4, 'obstruction5': 4, 'obstruction7': 4, 'obstruction2': 1} tool [ 0.314 -0.013  0.25 ] end [ 0.321 -0.03   0.141]
          27 +step 105 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 5, 'obstruction5': 4, 'obstruction7': 4, 'obstruction2': 1} tool [ 0.321 -0.03   0.141] end [ 0.356 -0.062  0.162]
          28 +step 115 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 5, 'obstruction5': 5, 'obstruction7': 4, 'obstruction2': 1} tool [ 0.356 -0.062  0.162] end [ 0.34  -0.011  0.141]
          29 +step 119 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 5, 'obstruction5': 5, 'obstruction7': 5, 'obstruction2': 1} tool [ 0.34  -0.011  0.141] end [ 0.321 -0.026  0.133]
          30 +step 129 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 5, 'obstruction5': 5, 'obstruction7': 5, 'obstruction2': 2} tool [ 0.321 -0.026  0.133] end [ 0.321 -0.056  0.141]
          31 +step 133 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 6, 'obstruction5': 5, 'obstruction7': 5, 'obstruction2': 2} tool [ 0.321 -0.056  0.141] end [ 0.363 -0.058  0.162]
          32 +step 143 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 6, 'obstruction5': 6, 'obstruction7': 5, 'obstruction2': 2} tool [ 0.363 -0.058  0.162] end [ 0.346 -0.004  0.141]
          33 +step 147 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 6, 'obstruction5': 6, 'obstruction7': 6, 'obstruction2': 2} tool [ 0.346 -0.004  0.141] end [ 0.314 -0.02   0.133]
          34 +step 157 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 6, 'obstruction5': 6, 'obstruction7': 6, 'obstruction2': 3} tool [ 0.314 -0.02   0.133] end [ 0.314 -0.049  0.141]
          35 +step 161 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 7, 'obstruction5': 6, 'obstruction7': 6, 'obstruction2': 3} tool [ 0.314 -0.049  0.141] end [ 0.35  -0.058  0.162]
          36 +step 171 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 7, 'obstruction5': 7, 'obstruction7': 6, 'obstruction2': 3} tool [ 0.35  -0.058  0.162] end [ 0.371 -0.004  0.141]
          37 +step 175 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 7, 'obstruction5': 7, 'obstruction7': 7, 'obstruction2': 3} tool [ 0.371 -0.004  0.141] end [ 0.314 -0.007  0.133]
          38 +ABORT step 184 tool [ 0.314 -0.007  0.191] q [-0.863  1.258 -1.018 -2.144 -0.992 -1.827 -6.407] target [-0.849  1.363 -1.122 -2.235 -1.122 -1.779 -6.373] tgt tool [ 0.314 -0.007  0.133]
          39 +step 185 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 7, 'obstruction5': 7, 'obstruction7': 7, 'obstruction2': 4} tool [ 0.314 -0.007  0.25 ] end [ 0.314 -0.037  0.141]
          40 +step 189 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 8, 'obstruction5': 7, 'obstruction7': 7, 'obstruction2': 4} tool [ 0.314 -0.037  0.141] end [ 0.344 -0.053  0.162]
          41 +step 199 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 8, 'obstruction5': 8, 'obstruction7': 7, 'obstruction2': 4} tool [ 0.344 -0.053  0.162] end [0.365 0.003 0.141]
          42 +step 203 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 8, 'obstruction5': 8, 'obstruction7': 8, 'obstruction2': 4} tool [0.365 0.003 0.141] end [ 0.308 -0.013  0.133]
          43 +ABORT step 212 tool [ 0.308 -0.013  0.191] q [-0.866  1.222 -1.035 -2.162 -0.972 -1.78  -6.396] target [-0.846  1.324 -1.144 -2.255 -1.106 -1.728 -6.354] tgt tool [ 0.308 -0.013  0.133]
          44 +step 213 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 8, 'obstruction5': 8, 'obstruction7': 8, 'obstruction2': 5} tool [ 0.308 -0.013  0.25 ] end [ 0.307 -0.043  0.141]
          45 +step 217 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 9, 'obstruction5': 8, 'obstruction7': 8, 'obstruction2': 5} tool [ 0.307 -0.043  0.141] end [ 0.369 -0.053  0.162]
          46 +step 227 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 9, 'obstruction5': 9, 'obstruction7': 8, 'obstruction2': 5} tool [ 0.369 -0.053  0.162] end [0.352 0.003 0.141]
          47 +step 231 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 9, 'obstruction5': 9, 'obstruction7': 9, 'obstruction2': 5} tool [0.352 0.003 0.141] end [ 0.315 -0.013  0.133]
          48 +ABORT step 234 tool [ 0.315 -0.013  0.191] q [-0.987  0.908 -1.306 -2.144 -0.88  -1.409 -5.093] target [-0.923  0.987 -1.444 -2.235 -1.028 -1.311 -5.006] tgt tool [ 0.315 -0.013  0.133]
          49 +step 235 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 9, 'obstruction5': 9, 'obstruction7': 9, 'obstruction2': 6} tool [ 0.315 -0.013  0.25 ] end [ 0.321 -0.062  0.141]
          50 +step 244 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 10, 'obstruction5': 9, 'obstruction7': 9, 'obstruction2': 6} tool [ 0.321 -0.062  0.141] end [ 0.363 -0.062  0.162]
          51 +step 254 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 10, 'obstruction5': 10, 'obstruction7': 9, 'obstruction2': 6} tool [ 0.363 -0.062  0.162] end [ 0.359 -0.018  0.169]
          52 +step 264 task obstruction2 grasp 0.0 plan 10 fails {'obstruction0': 10, 'obstruction5': 10, 'obstruction7': 10, 'obstruction2': 6} tool [ 0.359 -0.018  0.169] end [ 0.321 -0.032  0.133]
          53 +step 268 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 10, 'obstruction5': 10, 'obstruction7': 10, 'obstruction2': 7} tool [ 0.321 -0.032  0.133] end [ 0.321 -0.024  0.141]
          54 +step 272 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 11, 'obstruction5': 10, 'obstruction7': 10, 'obstruction2': 7} tool [ 0.321 -0.024  0.141] end [ 0.35  -0.062  0.162]
          55 +step 282 task obstruction7 grasp 0.0 plan 8 fails {'obstruction0': 11, 'obstruction5': 11, 'obstruction7': 10, 'obstruction2': 7} tool [ 0.35  -0.062  0.162] end [ 0.359 -0.018  0.169]
          56 +step 286 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 11, 'obstruction5': 11, 'obstruction7': 11, 'obstruction2': 7} tool [ 0.359 -0.018  0.169] end [ 0.314 -0.026  0.133]
          57 +step 296 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 11, 'obstruction5': 11, 'obstruction7': 11, 'obstruction2': 8} tool [ 0.314 -0.026  0.133] end [ 0.314 -0.03   0.141]
          58 +step 300 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 12, 'obstruction5': 11, 'obstruction7': 11, 'obstruction2': 8} tool [ 0.314 -0.03   0.141] end [ 0.369 -0.058  0.162]
          59 +step 310 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 12, 'obstruction5': 12, 'obstruction7': 11, 'obstruction2': 8} tool [ 0.369 -0.058  0.162] end [ 0.378 -0.004  0.141]
          60 +step 314 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 12, 'obstruction5': 12, 'obstruction7': 12, 'obstruction2': 8} tool [ 0.378 -0.004  0.141] end [ 0.314 -0.001  0.133]
          61 +ABORT step 323 tool [ 0.314 -0.001  0.191] q [-0.876  1.271 -1.006 -2.144 -0.994 -1.844 -6.417] target [-0.863  1.377 -1.109 -2.235 -1.124 -1.798 -6.385] tgt tool [ 0.314 -0.001  0.133]
          62 +step 324 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 12, 'obstruction5': 12, 'obstruction7': 12, 'obstruction2': 9} tool [ 0.314 -0.001  0.25 ] end [ 0.314 -0.056  0.141]
          63 +step 328 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 13, 'obstruction5': 12, 'obstruction7': 12, 'obstruction2': 9} tool [ 0.314 -0.056  0.141] end [ 0.344 -0.058  0.162]
          64 +step 338 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 13, 'obstruction5': 13, 'obstruction7': 12, 'obstruction2': 9} tool [ 0.344 -0.058  0.162] end [ 0.34  -0.004  0.141]
          65 +step 342 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 13, 'obstruction5': 13, 'obstruction7': 13, 'obstruction2': 9} tool [ 0.34  -0.004  0.141] end [ 0.308 -0.02   0.133]
          66 +step 352 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 13, 'obstruction5': 13, 'obstruction7': 13, 'obstruction2': 10} tool [ 0.308 -0.02   0.133] end [ 0.307 -0.049  0.141]
          67 +step 356 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 14, 'obstruction5': 13, 'obstruction7': 13, 'obstruction2': 10} tool [ 0.307 -0.049  0.141] end [ 0.375 -0.053  0.162]
          68 +step 366 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 14, 'obstruction5': 14, 'obstruction7': 13, 'obstruction2': 10} tool [ 0.375 -0.053  0.162] end [0.371 0.003 0.141]
          69 +step 370 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 14, 'obstruction5': 14, 'obstruction7': 14, 'obstruction2': 10} tool [0.371 0.003 0.141] end [ 0.308 -0.007  0.133]
          70 +ABORT step 379 tool [ 0.308 -0.007  0.191] q [-0.888  1.219 -1.037 -2.163 -0.971 -1.776 -6.418] target [-0.868  1.321 -1.147 -2.255 -1.105 -1.724 -6.376] tgt tool [ 0.308 -0.007  0.133]
          71 +step 380 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 14, 'obstruction5': 14, 'obstruction7': 14, 'obstruction2': 11} tool [ 0.308 -0.007  0.25 ] end [ 0.307 -0.037  0.141]
          72 +step 384 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 15, 'obstruction5': 14, 'obstruction7': 14, 'obstruction2': 11} tool [ 0.307 -0.037  0.141] end [ 0.337 -0.053  0.162]
          73 +step 394 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 15, 'obstruction5': 15, 'obstruction7': 14, 'obstruction2': 11} tool [ 0.337 -0.053  0.162] end [0.346 0.003 0.141]
          74 +step 398 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction5': 15, 'obstruction7': 15, 'obstruction2': 11} tool [0.346 0.003 0.141] end [ 0.301 -0.013  0.133]
          75 +ABORT step 407 tool [ 0.301 -0.013  0.191] q [-0.888  1.187 -1.05  -2.181 -0.953 -1.735 -6.405] target [-0.863  1.286 -1.164 -2.275 -1.09  -1.679 -6.356] tgt tool [ 0.301 -0.013  0.133]
          76 +step 408 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 15, 'obstruction5': 15, 'obstruction7': 15, 'obstruction2': 12} tool [ 0.301 -0.013  0.25 ] end [ 0.301 -0.043  0.141]
          77 +step 412 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 16, 'obstruction5': 15, 'obstruction7': 15, 'obstruction2': 12} tool [ 0.301 -0.043  0.141] end [ 0.369 -0.062  0.162]
          78 +step 422 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 16, 'obstruction5': 16, 'obstruction7': 15, 'obstruction2': 12} tool [ 0.369 -0.062  0.162] end [ 0.359 -0.024  0.169]
          79 +step 432 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 16, 'obstruction5': 16, 'obstruction7': 16, 'obstruction2': 12} tool [ 0.359 -0.024  0.169] end [ 0.315 -0.008  0.133]
          80 +ABORT step 440 tool [ 0.315 -0.008  0.191] q [-0.783  0.282 -2.139 -2.14  -0.312 -0.871 -2.736] target [-0.64   0.417 -2.265 -2.228 -0.503 -0.702 -2.552] tgt tool [ 0.315 -0.008  0.133]
          81 +step 441 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 16, 'obstruction5': 16, 'obstruction7': 16, 'obstruction2': 13} tool [ 0.315 -0.008  0.25 ] end [ 0.314 -0.062  0.141]
          82 +step 450 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 17, 'obstruction5': 16, 'obstruction7': 16, 'obstruction2': 13} tool [ 0.314 -0.062  0.141] end [ 0.344 -0.062  0.162]
          83 +step 460 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 17, 'obstruction5': 17, 'obstruction7': 16, 'obstruction2': 13} tool [ 0.344 -0.062  0.162] end [ 0.359 -0.011  0.169]
          84 +step 469 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 17, 'obstruction5': 17, 'obstruction7': 17, 'obstruction2': 13} tool [ 0.359 -0.011  0.169] end [ 0.309 -0.013  0.133]
          85 +ABORT step 477 tool [ 0.309 -0.013  0.191] q [-1.028  0.773 -1.395 -2.162 -0.804 -1.268 -5.197] target [-0.934  0.846 -1.556 -2.253 -0.962 -1.149 -5.092] tgt tool [ 0.309 -0.013  0.133]
          86 +step 478 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 17, 'obstruction5': 17, 'obstruction7': 17, 'obstruction2': 14} tool [ 0.309 -0.013  0.25 ] end [ 0.314 -0.024  0.141]
          87 +step 487 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 18, 'obstruction5': 17, 'obstruction7': 17, 'obstruction2': 14} tool [ 0.314 -0.024  0.141] end [ 0.375 -0.058  0.162]
          88 +step 497 task obstruction7 grasp 0.0 plan 8 fails {'obstruction0': 18, 'obstruction5': 18, 'obstruction7': 17, 'obstruction2': 14} tool [ 0.375 -0.058  0.162] end [ 0.365 -0.018  0.169]
          89 +step 501 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 18, 'obstruction5': 18, 'obstruction7': 18, 'obstruction2': 14} tool [ 0.365 -0.018  0.169] end [ 0.314 -0.032  0.133]
          90 +step 511 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 18, 'obstruction5': 18, 'obstruction7': 18, 'obstruction2': 15} tool [ 0.314 -0.032  0.133] end [ 0.307 -0.03   0.141]
          91 +step 515 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 19, 'obstruction5': 18, 'obstruction7': 18, 'obstruction2': 15} tool [ 0.307 -0.03   0.141] end [ 0.337 -0.058  0.162]
          92 +step 525 task obstruction7 grasp 0.0 plan 8 fails {'obstruction0': 19, 'obstruction5': 19, 'obstruction7': 18, 'obstruction2': 15} tool [ 0.337 -0.058  0.162] end [ 0.352 -0.018  0.169]
          93 +step 529 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 19, 'obstruction5': 19, 'obstruction7': 19, 'obstruction2': 15} tool [ 0.352 -0.018  0.169] end [0.314 0.006 0.133]
          94 +ABORT step 538 tool [0.314 0.006 0.191] q [-1.068  0.508 -1.673 -2.147 -0.601 -1.027 -3.986] target [-0.913  0.598 -1.861 -2.235 -0.775 -0.881 -3.844] tgt tool [0.314 0.006 0.133]
          95 +step 539 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 19, 'obstruction5': 19, 'obstruction7': 19, 'obstruction2': 16} tool [0.314 0.006 0.25 ] end [ 0.307 -0.056  0.141]
          96 +step 543 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 20, 'obstruction5': 19, 'obstruction7': 19, 'obstruction2': 16} tool [ 0.307 -0.056  0.141] end [ 0.375 -0.062  0.162]
          97 +step 553 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 20, 'obstruction5': 20, 'obstruction7': 19, 'obstruction2': 16} tool [ 0.375 -0.062  0.162] end [ 0.352 -0.018  0.169]
          98 +step 563 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 20, 'obstruction5': 20, 'obstruction7': 20, 'obstruction2': 16} tool [ 0.352 -0.018  0.169] end [ 0.315 -0.003  0.133]
          99 +ABORT step 571 tool [ 0.315 -0.003  0.191] q [-0.794  0.28  -2.146 -2.14  -0.308 -0.87  -2.756] target [-0.652  0.415 -2.271 -2.228 -0.499 -0.7   -2.573] tgt tool [ 0.315 -0.003  0.133]
         100 +step 572 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 20, 'obstruction5': 20, 'obstruction7': 20, 'obstruction2': 17} tool [ 0.315 -0.003  0.25 ] end [ 0.301 -0.049  0.141]
         101 +step 582 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 21, 'obstruction5': 20, 'obstruction7': 20, 'obstruction2': 17} tool [ 0.301 -0.049  0.141] end [ 0.337 -0.062  0.162]
         102 +step 591 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 21, 'obstruction5': 21, 'obstruction7': 20, 'obstruction2': 17} tool [ 0.337 -0.062  0.162] end [ 0.366 -0.018  0.169]
         103 +step 600 task obstruction2 grasp 0.0 plan 10 fails {'obstruction0': 21, 'obstruction5': 21, 'obstruction7': 21, 'obstruction2': 17} tool [ 0.366 -0.018  0.169] end [ 0.308 -0.026  0.133]
         104 +step 604 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 21, 'obstruction5': 21, 'obstruction7': 21, 'obstruction2': 18} tool [ 0.308 -0.026  0.133] end [ 0.301 -0.037  0.141]
         105 +step 608 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 21, 'obstruction2': 18} tool [ 0.301 -0.037  0.141] end [ 0.359 -0.025  0.169]
         106 +step 618 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 18} tool [ 0.359 -0.025  0.169] end [ 0.308 -0.001  0.133]
         107 +ABORT step 626 tool [ 0.308 -0.001  0.191] q [-1.017  0.388 -1.809 -2.165 -0.474 -0.937 -4.12 ] target [-0.834  0.501 -2.    -2.254 -0.668 -0.783 -3.947] tgt tool [ 0.308 -0.001  0.133]
         108 +step 628 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.308 -0.001  0.25 ] end [ 0.321 -0.043  0.158]
         109 +step 633 task obstruction0 grasp 1.0 plan 25 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.321 -0.043  0.158] end [ 0.207 -0.045  0.149]
         110 +step 649 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.207 -0.045  0.149] end [ 0.301 -0.026  0.133]
         111 +step 660 task obstruction2 grasp 1.0 plan 28 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.301 -0.026  0.133] end [0.307 0.079 0.124]
         112 +step 670 task obstruction5 grasp 0.0 plan 14 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [0.307 0.079 0.124] end [ 0.356 -0.053  0.162]
         113 +step 679 task obstruction5 grasp 1.0 plan 30 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.356 -0.053  0.162] end [0.427 0.086 0.154]
         114 +step 688 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [0.427 0.086 0.154] end [ 0.345 -0.018  0.141]
         115 +step 697 task obstruction7 grasp 1.0 plan 16 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.345 -0.018  0.141] end [0.254 0.098 0.133]
         116 +step 703 task target_block grasp 0.0 plan 19 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [0.254 0.098 0.133] end [ 0.299 -0.251  0.131]
         117 +step 712 task target_block grasp 1.0 plan 19 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.299 -0.251  0.131] end [ 0.339 -0.03   0.143]
         118 +SOLVED 718
         119 +time 53.90831160545349
diff --git a/probe7.py b/probe7.py
index f09f8db..0001c15 100644
--- a/probe7.py
+++ b/probe7.py
@@ -2,10 +2,10 @@ import numpy as np, kin, importlib as _il
    2      2  from env_client import make_env
    3      3  GA = _il.import_module("approach_v2").GeneratedApproach
    4      4  env = make_env()
    5        -obs, info = env.reset(seed=101, options={'object_count': 9})
           5 +obs, info = env.reset(seed=113, options={'object_count': 9})
    6      6  ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    7        -for t in range(15): obs,*_=env.step(ap.get_action(obs))
           7 +for t in range(0): obs,*_=env.step(ap.get_action(obs))
    8      8  objs=ap._parse(obs)
    9        -for n in ['obstruction0','obstruction1','obstruction2','obstruction7']:
           9 +for n in ["obstruction0","obstruction5","obstruction7","obstruction2"]:
   10     10      c=ap._grasp_candidates(objs[n], objs)
   11     11      print(n, [ (round(x[0],3), round(np.degrees(x[1])%360), round(x[2],3), round(x[3],3), x[4], round(x[5],3)) for x in c[:4]])
diff --git a/r7v2.txt b/r7v2.txt
index f4e3098..68abf2a 100644
--- a/r7v2.txt
+++ b/r7v2.txt
@@ -1,31 +1,30 @@
    1        -0 (True, 94, 7, 63.02361559867859)
    2        -1 (True, 104, 7, 74.47821474075317)
    3        -2 (True, 73, 7, 35.02347707748413)
    4        -3 (True, 77, 7, 27.969908952713013)
    5        -4 (True, 132, 7, 80.5042507648468)
    6        -5 (True, 114, 7, 78.19307494163513)
    7        -6 (True, 106, 7, 63.46646475791931)
    8        -7 (True, 123, 7, 72.65765714645386)
    9        -8 (True, 85, 7, 61.07735204696655)
   10        -9 (True, 87, 7, 67.08360195159912)
   11        -10 (True, 69, 7, 52.144341707229614)
   12        -11 (True, 80, 7, 58.64270758628845)
   13        -12 (True, 104, 7, 74.42161846160889)
   14        -13 (True, 131, 7, 99.624183177948)
   15        -14 (True, 61, 7, 43.49214029312134)
   16        -15 (True, 120, 7, 94.21526288986206)
   17        -16 (True, 62, 7, 43.739404916763306)
   18        -17 (True, 76, 7, 49.73142123222351)
   19        -18 (True, 92, 7, 68.14324593544006)
   20        -19 (True, 84, 7, 53.11684465408325)
   21        -20 (True, 93, 7, 66.39607453346252)
   22        -21 (True, 107, 7, 79.70174717903137)
   23        -22 (True, 76, 7, 56.05203819274902)
   24        -23 (True, 104, 7, 67.88577699661255)
   25        -24 (True, 78, 7, 52.187477827072144)
   26        -25 (True, 49, 7, 40.90671944618225)
   27        -26 (True, 69, 7, 43.35073471069336)
   28        -27 (True, 71, 7, 40.220239877700806)
   29        -28 (True, 103, 7, 36.82794904708862)
   30        -29 (True, 65, 7, 21.46721839904785)
   31        -success 30 / 30 mean steps 89.63333333333334 max time 99.624183177948
           1 +0 (True, 87, 7, 51.90975046157837)
           2 +1 (True, 103, 7, 64.63951778411865)
           3 +2 (True, 71, 7, 43.29448342323303)
           4 +3 (True, 78, 7, 55.36353397369385)
           5 +4 (True, 136, 7, 79.30280208587646)
           6 +5 (True, 107, 7, 65.30765151977539)
           7 +6 (True, 105, 7, 58.917471170425415)
           8 +7 (True, 143, 7, 95.11450624465942)
           9 +8 (True, 85, 7, 58.49885559082031)
          10 +9 (True, 87, 7, 66.62173414230347)
          11 +10 (True, 69, 7, 48.08510160446167)
          12 +11 (True, 77, 7, 54.44292092323303)
          13 +12 (True, 107, 7, 80.1859929561615)
          14 +13 (True, 134, 7, 101.62912821769714)
          15 +14 (True, 61, 7, 44.37665367126465)
          16 +15 (True, 111, 7, 93.56963753700256)
          17 +16 (True, 62, 7, 44.71505546569824)
          18 +17 (True, 76, 7, 50.44370412826538)
          19 +18 (True, 84, 7, 64.29676413536072)
          20 +19 (True, 77, 7, 48.525261640548706)
          21 +20 (True, 90, 7, 67.16040682792664)
          22 +21 (True, 104, 7, 78.47161626815796)
          23 +22 (True, 184, 7, 86.10974502563477)
          24 +23 (True, 103, 7, 67.44490051269531)
          25 +24 (True, 76, 7, 53.59507131576538)
          26 +25 (True, 49, 7, 35.07913136482239)
          27 +26 (True, 69, 7, 44.36275577545166)
          28 +27 (True, 71, 7, 38.36406922340393)
          29 +28 (True, 108, 7, 32.490216970443726)
          30 +success 30 / 30 mean steps 92.86666666666666 max time 101.62912821769714
diff --git a/r9.txt b/r9.txt
index bf5cddd..93bfdd5 100644
--- a/r9.txt
+++ b/r9.txt
@@ -1,30 +1,31 @@
    1        -100 (True, 97, 9, 72.14916110038757)
    2        -101 (False, 1000, 9, 333.80482721328735)
    3        -102 (True, 112, 9, 69.812979221344)
    4        -103 (True, 93, 9, 52.81530427932739)
    5        -104 (True, 140, 9, 87.37922263145447)
    6        -105 (True, 126, 9, 92.62624502182007)
    7        -106 (True, 91, 9, 46.40775680541992)
    8        -107 (True, 112, 9, 65.06996464729309)
    9        -108 (True, 134, 9, 91.0637879371643)
   10        -109 (True, 97, 9, 61.19999670982361)
   11        -110 (True, 120, 9, 75.0379490852356)
   12        -111 (True, 63, 9, 33.855305910110474)
   13        -112 (True, 111, 9, 62.16018080711365)
   14        -113 (True, 80, 9, 41.73160791397095)
   15        -114 (True, 92, 9, 56.17422151565552)
   16        -115 (True, 97, 9, 59.20113825798035)
   17        -116 (True, 86, 9, 54.971293687820435)
   18        -117 (True, 109, 9, 64.36724352836609)
   19        -118 (True, 136, 9, 80.83306837081909)
   20        -119 (True, 200, 9, 115.20018124580383)
   21        -120 (True, 115, 9, 54.81230664253235)
   22        -121 (False, 1000, 9, 182.53349542617798)
   23        -122 (True, 120, 9, 69.95800018310547)
   24        -123 (True, 84, 9, 38.88550424575806)
   25        -124 (True, 104, 9, 58.44248819351196)
   26        -125 (True, 100, 9, 55.21132850646973)
   27        -126 (True, 78, 9, 40.50506377220154)
   28        -127 (True, 76, 9, 38.882683753967285)
   29        -128 (True, 80, 9, 29.606189250946045)
   30        -success 28 / 30 mean steps 104.42857142857143 max time 333.80482721328735
           1 +100 (True, 96, 9, 52.53955030441284)
           2 +101 (True, 93, 9, 54.51079869270325)
           3 +102 (True, 112, 9, 65.34322571754456)
           4 +103 (True, 93, 9, 44.810567140579224)
           5 +104 (True, 153, 9, 93.75739359855652)
           6 +105 (True, 128, 9, 81.2679808139801)
           7 +106 (True, 93, 9, 62.40128564834595)
           8 +107 (True, 112, 9, 69.19037199020386)
           9 +108 (True, 131, 9, 91.25654864311218)
          10 +109 (True, 100, 9, 64.36337423324585)
          11 +110 (True, 121, 9, 79.18544244766235)
          12 +111 (True, 63, 9, 34.50396370887756)
          13 +112 (True, 144, 9, 99.37276291847229)
          14 +113 (True, 718, 9, 225.3370132446289)
          15 +114 (True, 82, 9, 43.92652463912964)
          16 +115 (True, 97, 9, 65.58510565757751)
          17 +116 (True, 86, 9, 52.46846628189087)
          18 +117 (True, 107, 9, 80.39322829246521)
          19 +118 (True, 137, 9, 93.61911106109619)
          20 +119 (True, 148, 9, 108.74081182479858)
          21 +120 (True, 106, 9, 68.54011392593384)
          22 +121 (True, 94, 9, 71.20775604248047)
          23 +122 (True, 121, 9, 81.89497876167297)
          24 +123 (True, 80, 9, 45.335349321365356)
          25 +124 (True, 104, 9, 61.29020118713379)
          26 +125 (True, 95, 9, 53.72698712348938)
          27 +126 (True, 78, 9, 39.93084263801575)
          28 +127 (True, 76, 9, 37.43912959098816)
          29 +128 (True, 84, 9, 34.11875557899475)
          30 +129 (True, 71, 9, 20.42490267753601)
          31 +success 30 / 30 mean steps 124.1 max time 225.3370132446289
diff --git a/rdv2.txt b/rdv2.txt
index 2ed1bf5..1eed73c 100644
--- a/rdv2.txt
+++ b/rdv2.txt
@@ -1,72 +1,75 @@
    1        -0 (True, 49, 2, 44.65753626823425)
    2        -1 (True, 38, 1, 21.186123609542847)
    3        -2 (True, 66, 2, 57.75160527229309)
    4        -4 (True, 59, 2, 50.24415946006775)
    5        -5 (True, 53, 2, 46.16478967666626)
    6        -6 (True, 37, 1, 20.326173543930054)
    7        -7 (True, 39, 2, 26.76628804206848)
    8        -8 (True, 43, 2, 43.95758414268494)
    9        -9 (True, 25, 1, 21.770167589187622)
   10        -10 (True, 28, 2, 29.55744743347168)
   11        -12 (True, 32, 1, 29.08803963661194)
   12        -13 (True, 41, 2, 39.67139220237732)
   13        -15 (True, 29, 2, 26.388429641723633)
   14        -16 (True, 27, 1, 23.87075400352478)
   15        -17 (True, 45, 2, 54.42944002151489)
   16        -18 (True, 38, 2, 37.27797603607178)
   17        -19 (True, 27, 1, 24.010403633117676)
   18        -20 (True, 55, 2, 60.94573783874512)
   19        -21 (True, 21, 0, 22.378713130950928)
   20        -22 (True, 30, 2, 32.95614266395569)
   21        -25 (True, 36, 1, 36.96371579170227)
   22        -26 (True, 33, 2, 34.67341351509094)
   23        -27 (True, 25, 0, 24.828604221343994)
   24        -28 (True, 49, 1, 51.44413161277771)
   25        -31 (True, 39, 1, 32.03095841407776)
   26        -32 (True, 47, 2, 58.34464073181152)
   27        -33 (True, 45, 2, 62.76429796218872)
   28        -36 (True, 24, 1, 29.247500896453857)
   29        -38 (True, 15, 0, 23.458435535430908)
   30        -39 (True, 45, 2, 52.62647604942322)
   31        -40 (True, 75, 1, 96.66923713684082)
   32        -41 (True, 29, 1, 28.586360931396484)
   33        -43 (True, 26, 1, 22.42523980140686)
   34        -44 (True, 30, 2, 36.01871132850647)
   35        -45 (True, 44, 2, 46.51904630661011)
   36        -46 (True, 26, 1, 31.43686842918396)
   37        -50 (True, 46, 2, 40.128849029541016)
   38        -51 (True, 29, 1, 27.790140867233276)
   39        -52 (True, 64, 2, 70.9896650314331)
   40        -53 (True, 44, 2, 46.5516517162323)
   41        -55 (True, 56, 2, 57.09167718887329)
   42        -58 (True, 21, 1, 25.080037832260132)
   43        -59 (True, 55, 2, 71.23579120635986)
   44        -61 (True, 30, 1, 30.14669418334961)
   45        -62 (True, 29, 1, 34.10112380981445)
   46        -63 (True, 27, 1, 24.44920825958252)
   47        -64 (True, 32, 1, 32.68348264694214)
   48        -65 (True, 27, 0, 26.728271961212158)
   49        -66 (True, 41, 2, 43.42152118682861)
   50        -67 (True, 48, 2, 57.42696690559387)
   51        -70 (True, 35, 1, 37.85807991027832)
   52        -71 (True, 52, 2, 56.0893611907959)
   53        -72 (True, 51, 2, 60.09363770484924)
   54        -73 (True, 37, 2, 35.012733697891235)
   55        -75 (True, 26, 1, 27.053276538848877)
   56        -76 (True, 40, 1, 40.37609887123108)
   57        -78 (True, 28, 2, 24.771350860595703)
   58        -80 (True, 39, 2, 45.06876516342163)
   59        -82 (True, 39, 2, 34.693543434143066)
   60        -83 (True, 29, 2, 30.512681484222412)
   61        -85 (True, 44, 2, 44.677146911621094)
   62        -86 (True, 45, 2, 46.307608127593994)
   63        -87 (True, 37, 1, 31.606425762176514)
   64        -88 (True, 30, 1, 23.946342706680298)
   65        -89 (True, 54, 2, 48.46833086013794)
   66        -90 (True, 27, 1, 22.381341695785522)
   67        -91 (True, 32, 2, 33.97594165802002)
   68        -92 (True, 28, 1, 22.89961051940918)
   69        -93 (True, 43, 2, 31.299214601516724)
   70        -95 (True, 33, 1, 21.54423999786377)
   71        -96 (True, 47, 2, 21.919421434402466)
   72        -success 100 / 100 mean steps 32.78 max time 96.66923713684082
           1 +0 (True, 45, 2, 38.46183633804321)
           2 +1 (True, 38, 1, 25.16204023361206)
           3 +2 (True, 62, 2, 69.66143441200256)
           4 +3 (True, 32, 2, 25.111533164978027)
           5 +4 (True, 57, 2, 47.401066064834595)
           6 +5 (True, 48, 2, 38.81461954116821)
           7 +6 (True, 37, 1, 28.365293979644775)
           8 +7 (True, 39, 2, 23.942261695861816)
           9 +8 (True, 43, 2, 48.381948947906494)
          10 +9 (True, 25, 1, 25.134716987609863)
          11 +10 (True, 28, 2, 27.94377303123474)
          12 +12 (True, 31, 1, 34.262075424194336)
          13 +13 (True, 41, 2, 47.47896194458008)
          14 +15 (True, 29, 2, 30.29609704017639)
          15 +16 (True, 27, 1, 23.91221523284912)
          16 +17 (True, 45, 2, 52.179850816726685)
          17 +18 (True, 34, 2, 38.0179545879364)
          18 +19 (True, 27, 1, 22.081477165222168)
          19 +20 (True, 52, 2, 57.48599147796631)
          20 +21 (True, 21, 0, 21.24903392791748)
          21 +22 (True, 30, 2, 37.5386917591095)
          22 +24 (True, 19, 1, 20.510115385055542)
          23 +25 (True, 36, 1, 36.27837538719177)
          24 +26 (True, 33, 2, 41.65943884849548)
          25 +27 (True, 25, 0, 30.9220449924469)
          26 +28 (True, 47, 1, 60.319626808166504)
          27 +31 (True, 39, 1, 54.2931227684021)
          28 +32 (True, 43, 2, 54.85727024078369)
          29 +33 (True, 45, 2, 56.75646710395813)
          30 +36 (True, 24, 1, 21.818586111068726)
          31 +39 (True, 45, 2, 55.257946252822876)
          32 +40 (True, 31, 1, 34.094388484954834)
          33 +41 (True, 29, 1, 28.48836350440979)
          34 +43 (True, 26, 1, 21.424931526184082)
          35 +44 (True, 30, 2, 35.7546501159668)
          36 +45 (True, 44, 2, 53.590073585510254)
          37 +46 (True, 26, 1, 32.86268901824951)
          38 +50 (True, 46, 2, 48.59174656867981)
          39 +51 (True, 29, 1, 32.24302124977112)
          40 +52 (True, 58, 2, 62.643776416778564)
          41 +53 (True, 44, 2, 45.79771566390991)
          42 +55 (True, 56, 2, 58.44292163848877)
          43 +56 (True, 28, 1, 22.507607460021973)
          44 +58 (True, 21, 1, 25.118072509765625)
          45 +59 (True, 55, 2, 57.27587962150574)
          46 +61 (True, 30, 1, 28.41112780570984)
          47 +62 (True, 29, 1, 20.521795988082886)
          48 +63 (True, 27, 1, 25.936198949813843)
          49 +64 (True, 32, 1, 29.715338230133057)
          50 +65 (True, 27, 0, 24.168847799301147)
          51 +66 (True, 41, 2, 40.606157302856445)
          52 +67 (True, 48, 2, 52.30963897705078)
          53 +70 (True, 35, 1, 30.777546167373657)
          54 +71 (True, 52, 2, 52.772658348083496)
          55 +72 (True, 51, 2, 47.925705671310425)
          56 +73 (True, 37, 2, 32.55638670921326)
          57 +76 (True, 40, 1, 39.88845419883728)
          58 +78 (True, 28, 2, 23.338553428649902)
          59 +80 (True, 39, 2, 35.555004596710205)
          60 +82 (True, 39, 2, 32.58023715019226)
          61 +83 (True, 29, 2, 26.03005838394165)
          62 +84 (True, 26, 1, 23.71669840812683)
          63 +85 (True, 44, 2, 43.41327476501465)
          64 +86 (True, 45, 2, 39.73675012588501)
          65 +87 (True, 37, 1, 27.45497751235962)
          66 +88 (True, 30, 1, 25.342838764190674)
          67 +89 (True, 50, 2, 46.96338391304016)
          68 +90 (True, 27, 1, 26.090787649154663)
          69 +91 (True, 32, 2, 35.03382110595703)
          70 +92 (True, 28, 1, 24.249154090881348)
          71 +93 (True, 42, 2, 32.150060176849365)
          72 +94 (True, 19, 0, 21.742794036865234)
          73 +95 (True, 33, 1, 20.39409828186035)
          74 +96 (True, 47, 2, 20.63382363319397)
          75 +success 100 / 100 mean steps 31.94 max time 69.66143441200256
```

</details>

<a id="C022"></a>
### C022 · Promote: grasp height model fixes, bad-spot banning; 9-obs 30/30

Commit `1fc80533cd4fade9324d12c67271240b8db6b410`; parents: 3afee96798a374b3260180034484cbdba363f557. Recorded author date: 2026-09-30T23:50:15+02:00.

File roles (automatic): policy, setup/other.

- [E1025](01_timeline.md#E1025): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_1fc8053_approach.py) · [Exact all-file diff](evidence/diffs/C022_1fc8053.diff)

[Previous saved controller snapshot](evidence/versions/C017_3fc7f32_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 50cdb85..1d2c701 100644
--- a/approach.py
+++ b/approach.py
@@ -182,7 +182,7 @@ class GeneratedApproach:
  182    182          near = [(n, b) for n, b in objs.items() if n != o.name and n != 'target_region'
  183    183                  and np.linalg.norm(b.p[:2] - o.p[:2]) < 0.16]
  184    184          z_lo = o.bottom + 0.044
  185        -        z_hi = o.top + 0.027
         185 +        z_hi = o.top + 0.028
  186    186          if z_hi < z_lo:
  187    187              z_hi = z_lo = 0.5 * (z_lo + z_hi)
  188    188          zs = [min(0.5 * (z_lo + z_hi), z_lo + 0.012)]
@@ -201,14 +201,16 @@ class GeneratedApproach:
  201    201              sds = np.linspace(-smax, smax, 7) if smax > 0 else [0.0]
  202    202              sas = np.linspace(-amax, amax, 7) if amax > 0 else [0.0]
  203    203              for zi, zg in enumerate(zs):
  204        -                tip = zg - 0.035
  205        -                rel = [(n, b) for n, b in near if b.top > tip]
         204 +                tip = zg - 0.0315
         205 +                rel = [(n, b) for n, b in near if b.top > zg - 0.042]
  206    206                  for sd in sds:
  207    207                      for sa in sas:
  208    208                          x, y = o.p[:2] + sd * d + sa * a
  209        -                        boxes = self._finger_boxes(x, y, yaw) + [(np.array([x, y]), d, a, 0.043, 0.011)]
         209 +                        fboxes = self._finger_boxes(x, y, yaw)
         210 +                        sbox = (np.array([x, y]), d, a, 0.043, 0.011)
  210    211                          blockers = []
  211    212                          for n, b in rel:
         213 +                            boxes = ([sbox] + fboxes) if b.top > tip else [sbox]
  212    214                              for box in boxes:
  213    215                                  if self._box_hits_obj(box, b):
  214    216                                      blockers.append(n)
@@ -237,6 +239,8 @@ class GeneratedApproach:
  237    239          self.blocked = 0
  238    240          self.last_q = None
  239    241          self.fail_count = {}
         242 +        self.bad_spots = []
         243 +        self.last_spot = None
  240    244          self.steps = 0
  241    245          self.plans_made = 0
  242    246          self.aborting = False
@@ -358,7 +362,9 @@ class GeneratedApproach:
  358    362          for x in np.arange(TABLE_X[0] + fp[0], TABLE_X[1] - fp[0], 0.02):
  359    363              for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
  360    364                  p = np.array([x, y])
  361        -                cost = np.linalg.norm(p - cur)
         365 +                cost = np.linalg.norm(p - cur) + 2.0 * max(0.0, 0.2 - x)
         366 +                if any(np.linalg.norm(p - bs) < 0.035 for bs in self.bad_spots):
         367 +                    continue
  362    368                  if best is not None and cost >= best[0]:
  363    369                      continue
  364    370                  ok = True
@@ -475,6 +481,7 @@ class GeneratedApproach:
  475    481              clear = self._to_clear(objs)
  476    482              reg = objs['target_region']
  477    483              if held == 'target_block' and not clear:
         484 +                self.last_spot = None
  478    485                  self._plan_place(state, held, reg.p[:2], reg.top, reg.yaw)
  479    486                  return
  480    487              G = self._G(state)
@@ -483,6 +490,7 @@ class GeneratedApproach:
  483    490              spot = self._free_spot(o, objs, tool_yaw)
  484    491              if spot is None:
  485    492                  spot = o.p[:2]
         493 +            self.last_spot = np.array(spot, float)
  486    494              self._plan_place(state, held, spot, TABLE_TOP, o.yaw)
  487    495              return
  488    496          best = self._pick_target(objs)
@@ -498,6 +506,8 @@ class GeneratedApproach:
  498    506      def _abort(self, state):
  499    507          """blocked: retreat straight up and replan."""
  500    508          self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
         509 +        if self.last_spot is not None and float(state.get(self.robot, 'grasp_active')) > 0.5:
         510 +            self.bad_spots.append(self.last_spot)
  501    511          q = self._q(state)
  502    512          T = self._tool(q)
  503    513          p0 = T[:3, 3]
diff --git a/d101.txt b/d101.txt
index 3595e87..5186adf 100644
--- a/d101.txt
+++ b/d101.txt
@@ -9,17 +9,17 @@ obstruction7 [ 0.286 -0.17   0.107] [0.014 0.012 0.022]
    9      9  obstruction8 [ 0.478 -0.016  0.099] [0.014 0.014 0.024]
   10     10  target_block [ 0.419 -0.102  0.1  ] [0.039 0.025 0.025]
   11     11  target_region [ 0.328 -0.152  0.08 ] [0.048 0.031 0.005]
   12        -step 1 task obstruction0 grasp 0.0 plan 11 fails {} tool [0.154 0.001 0.217] end [ 0.279 -0.124  0.16 ]
   13        -step 7 task obstruction0 grasp 1.0 plan 17 fails {} tool [ 0.279 -0.124  0.16 ] end [ 0.282 -0.022  0.152]
   14        -step 14 task obstruction2 grasp 0.0 plan 14 fails {} tool [ 0.282 -0.022  0.152] end [ 0.306 -0.119  0.141]
   15        -step 23 task obstruction2 grasp 1.0 plan 19 fails {} tool [ 0.306 -0.119  0.141] end [ 0.303 -0.282  0.133]
   16        -step 31 task obstruction1 grasp 0.0 plan 16 fails {} tool [ 0.303 -0.282  0.133] end [ 0.328 -0.161  0.141]
   17        -step 40 task obstruction1 grasp 1.0 plan 18 fails {} tool [ 0.328 -0.161  0.141] end [ 0.384 -0.286  0.133]
   18        -step 47 task obstruction3 grasp 0.0 plan 16 fails {} tool [ 0.384 -0.286  0.133] end [ 0.376 -0.176  0.141]
   19        -step 56 task obstruction3 grasp 1.0 plan 18 fails {} tool [ 0.376 -0.176  0.141] end [ 0.369 -0.344  0.133]
   20        -step 63 task obstruction7 grasp 0.0 plan 14 fails {} tool [ 0.369 -0.344  0.133] end [ 0.286 -0.17   0.141]
          12 +step 1 task obstruction2 grasp 0.0 plan 11 fails {} tool [0.154 0.001 0.217] end [ 0.325 -0.1    0.166]
          13 +step 6 task obstruction2 grasp 1.0 plan 17 fails {} tool [ 0.325 -0.1    0.166] end [ 0.282 -0.003  0.157]
          14 +step 13 task obstruction0 grasp 0.0 plan 14 fails {} tool [ 0.282 -0.003  0.157] end [ 0.279 -0.124  0.141]
          15 +step 22 task obstruction0 grasp 1.0 plan 17 fails {} tool [ 0.279 -0.124  0.141] end [ 0.182 -0.122  0.133]
          16 +step 29 task obstruction1 grasp 0.0 plan 16 fails {} tool [ 0.182 -0.122  0.133] end [ 0.328 -0.161  0.141]
          17 +step 40 task obstruction1 grasp 1.0 plan 18 fails {} tool [ 0.328 -0.161  0.141] end [ 0.324 -0.286  0.133]
          18 +step 47 task obstruction3 grasp 0.0 plan 16 fails {} tool [ 0.324 -0.286  0.133] end [ 0.376 -0.176  0.141]
          19 +step 56 task obstruction3 grasp 1.0 plan 17 fails {} tool [ 0.376 -0.176  0.141] end [ 0.429 -0.284  0.133]
          20 +step 62 task obstruction7 grasp 0.0 plan 14 fails {} tool [ 0.429 -0.284  0.133] end [ 0.286 -0.17   0.141]
   21     21  step 72 task obstruction7 grasp 1.0 plan 17 fails {} tool [ 0.286 -0.17   0.141] end [ 0.264 -0.288  0.133]
   22     22  step 79 task target_block grasp 0.0 plan 17 fails {} tool [ 0.264 -0.288  0.133] end [ 0.419 -0.102  0.131]
   23     23  step 86 task target_block grasp 1.0 plan 17 fails {} tool [ 0.419 -0.102  0.131] end [ 0.328 -0.152  0.143]
   24     24  SOLVED 93
   25        -time 6.1811769008636475
          25 +time 5.5087926387786865
diff --git a/d113.txt b/d113.txt
index f586687..06ff0fb 100644
--- a/d113.txt
+++ b/d113.txt
@@ -9,111 +9,15 @@ obstruction7 [ 0.359 -0.018  0.113] [0.017 0.018 0.028]
    9      9  obstruction8 [ 0.22  -0.148  0.087] [0.015 0.018 0.012]
   10     10  target_block [ 0.299 -0.251  0.1  ] [0.018 0.02  0.025]
   11     11  target_region [ 0.339 -0.03   0.08 ] [0.022 0.025 0.005]
   12        -step 1 task obstruction0 grasp 0.0 plan 13 fails {} tool [0.154 0.001 0.217] end [ 0.321 -0.043  0.141]
   13        -step 7 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 1} tool [ 0.321 -0.043  0.141] end [ 0.356 -0.053  0.162]
   14        -step 18 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 1, 'obstruction5': 1} tool [ 0.356 -0.053  0.162] end [ 0.359 -0.004  0.141]
   15        -step 22 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 1, 'obstruction5': 1, 'obstruction7': 1} tool [ 0.359 -0.004  0.141] end [ 0.321 -0.049  0.141]
   16        -step 32 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 2, 'obstruction5': 1, 'obstruction7': 1} tool [ 0.321 -0.049  0.141] end [ 0.356 -0.058  0.162]
   17        -step 42 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 2, 'obstruction5': 2, 'obstruction7': 1} tool [ 0.356 -0.058  0.162] end [ 0.365 -0.004  0.141]
   18        -step 46 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 2, 'obstruction5': 2, 'obstruction7': 2} tool [ 0.365 -0.004  0.141] end [ 0.321 -0.037  0.141]
   19        -step 55 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 3, 'obstruction5': 2, 'obstruction7': 2} tool [ 0.321 -0.037  0.141] end [ 0.363 -0.053  0.162]
   20        -step 65 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 3, 'obstruction5': 3, 'obstruction7': 2} tool [ 0.363 -0.053  0.162] end [ 0.352 -0.004  0.141]
   21        -step 69 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 3, 'obstruction5': 3, 'obstruction7': 3} tool [ 0.352 -0.004  0.141] end [ 0.314 -0.043  0.141]
   22        -step 78 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 4, 'obstruction5': 3, 'obstruction7': 3} tool [ 0.314 -0.043  0.141] end [ 0.35  -0.053  0.162]
   23        -step 88 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 4, 'obstruction5': 4, 'obstruction7': 3} tool [ 0.35  -0.053  0.162] end [0.359 0.003 0.141]
   24        -step 92 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 4, 'obstruction5': 4, 'obstruction7': 4} tool [0.359 0.003 0.141] end [ 0.314 -0.013  0.133]
   25        -ABORT step 100 tool [ 0.314 -0.013  0.191] q [-1.027  0.646 -1.526 -2.146 -0.721 -1.146 -3.765] target [-0.905  0.723 -1.7   -2.236 -0.884 -1.012 -3.645] tgt tool [ 0.314 -0.013  0.133]
   26        -step 101 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 4, 'obstruction5': 4, 'obstruction7': 4, 'obstruction2': 1} tool [ 0.314 -0.013  0.25 ] end [ 0.321 -0.03   0.141]
   27        -step 105 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 5, 'obstruction5': 4, 'obstruction7': 4, 'obstruction2': 1} tool [ 0.321 -0.03   0.141] end [ 0.356 -0.062  0.162]
   28        -step 115 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 5, 'obstruction5': 5, 'obstruction7': 4, 'obstruction2': 1} tool [ 0.356 -0.062  0.162] end [ 0.34  -0.011  0.141]
   29        -step 119 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 5, 'obstruction5': 5, 'obstruction7': 5, 'obstruction2': 1} tool [ 0.34  -0.011  0.141] end [ 0.321 -0.026  0.133]
   30        -step 129 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 5, 'obstruction5': 5, 'obstruction7': 5, 'obstruction2': 2} tool [ 0.321 -0.026  0.133] end [ 0.321 -0.056  0.141]
   31        -step 133 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 6, 'obstruction5': 5, 'obstruction7': 5, 'obstruction2': 2} tool [ 0.321 -0.056  0.141] end [ 0.363 -0.058  0.162]
   32        -step 143 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 6, 'obstruction5': 6, 'obstruction7': 5, 'obstruction2': 2} tool [ 0.363 -0.058  0.162] end [ 0.346 -0.004  0.141]
   33        -step 147 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 6, 'obstruction5': 6, 'obstruction7': 6, 'obstruction2': 2} tool [ 0.346 -0.004  0.141] end [ 0.314 -0.02   0.133]
   34        -step 157 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 6, 'obstruction5': 6, 'obstruction7': 6, 'obstruction2': 3} tool [ 0.314 -0.02   0.133] end [ 0.314 -0.049  0.141]
   35        -step 161 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 7, 'obstruction5': 6, 'obstruction7': 6, 'obstruction2': 3} tool [ 0.314 -0.049  0.141] end [ 0.35  -0.058  0.162]
   36        -step 171 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 7, 'obstruction5': 7, 'obstruction7': 6, 'obstruction2': 3} tool [ 0.35  -0.058  0.162] end [ 0.371 -0.004  0.141]
   37        -step 175 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 7, 'obstruction5': 7, 'obstruction7': 7, 'obstruction2': 3} tool [ 0.371 -0.004  0.141] end [ 0.314 -0.007  0.133]
   38        -ABORT step 184 tool [ 0.314 -0.007  0.191] q [-0.863  1.258 -1.018 -2.144 -0.992 -1.827 -6.407] target [-0.849  1.363 -1.122 -2.235 -1.122 -1.779 -6.373] tgt tool [ 0.314 -0.007  0.133]
   39        -step 185 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 7, 'obstruction5': 7, 'obstruction7': 7, 'obstruction2': 4} tool [ 0.314 -0.007  0.25 ] end [ 0.314 -0.037  0.141]
   40        -step 189 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 8, 'obstruction5': 7, 'obstruction7': 7, 'obstruction2': 4} tool [ 0.314 -0.037  0.141] end [ 0.344 -0.053  0.162]
   41        -step 199 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 8, 'obstruction5': 8, 'obstruction7': 7, 'obstruction2': 4} tool [ 0.344 -0.053  0.162] end [0.365 0.003 0.141]
   42        -step 203 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 8, 'obstruction5': 8, 'obstruction7': 8, 'obstruction2': 4} tool [0.365 0.003 0.141] end [ 0.308 -0.013  0.133]
   43        -ABORT step 212 tool [ 0.308 -0.013  0.191] q [-0.866  1.222 -1.035 -2.162 -0.972 -1.78  -6.396] target [-0.846  1.324 -1.144 -2.255 -1.106 -1.728 -6.354] tgt tool [ 0.308 -0.013  0.133]
   44        -step 213 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 8, 'obstruction5': 8, 'obstruction7': 8, 'obstruction2': 5} tool [ 0.308 -0.013  0.25 ] end [ 0.307 -0.043  0.141]
   45        -step 217 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 9, 'obstruction5': 8, 'obstruction7': 8, 'obstruction2': 5} tool [ 0.307 -0.043  0.141] end [ 0.369 -0.053  0.162]
   46        -step 227 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 9, 'obstruction5': 9, 'obstruction7': 8, 'obstruction2': 5} tool [ 0.369 -0.053  0.162] end [0.352 0.003 0.141]
   47        -step 231 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 9, 'obstruction5': 9, 'obstruction7': 9, 'obstruction2': 5} tool [0.352 0.003 0.141] end [ 0.315 -0.013  0.133]
   48        -ABORT step 234 tool [ 0.315 -0.013  0.191] q [-0.987  0.908 -1.306 -2.144 -0.88  -1.409 -5.093] target [-0.923  0.987 -1.444 -2.235 -1.028 -1.311 -5.006] tgt tool [ 0.315 -0.013  0.133]
   49        -step 235 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 9, 'obstruction5': 9, 'obstruction7': 9, 'obstruction2': 6} tool [ 0.315 -0.013  0.25 ] end [ 0.321 -0.062  0.141]
   50        -step 244 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 10, 'obstruction5': 9, 'obstruction7': 9, 'obstruction2': 6} tool [ 0.321 -0.062  0.141] end [ 0.363 -0.062  0.162]
   51        -step 254 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 10, 'obstruction5': 10, 'obstruction7': 9, 'obstruction2': 6} tool [ 0.363 -0.062  0.162] end [ 0.359 -0.018  0.169]
   52        -step 264 task obstruction2 grasp 0.0 plan 10 fails {'obstruction0': 10, 'obstruction5': 10, 'obstruction7': 10, 'obstruction2': 6} tool [ 0.359 -0.018  0.169] end [ 0.321 -0.032  0.133]
   53        -step 268 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 10, 'obstruction5': 10, 'obstruction7': 10, 'obstruction2': 7} tool [ 0.321 -0.032  0.133] end [ 0.321 -0.024  0.141]
   54        -step 272 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 11, 'obstruction5': 10, 'obstruction7': 10, 'obstruction2': 7} tool [ 0.321 -0.024  0.141] end [ 0.35  -0.062  0.162]
   55        -step 282 task obstruction7 grasp 0.0 plan 8 fails {'obstruction0': 11, 'obstruction5': 11, 'obstruction7': 10, 'obstruction2': 7} tool [ 0.35  -0.062  0.162] end [ 0.359 -0.018  0.169]
   56        -step 286 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 11, 'obstruction5': 11, 'obstruction7': 11, 'obstruction2': 7} tool [ 0.359 -0.018  0.169] end [ 0.314 -0.026  0.133]
   57        -step 296 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 11, 'obstruction5': 11, 'obstruction7': 11, 'obstruction2': 8} tool [ 0.314 -0.026  0.133] end [ 0.314 -0.03   0.141]
   58        -step 300 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 12, 'obstruction5': 11, 'obstruction7': 11, 'obstruction2': 8} tool [ 0.314 -0.03   0.141] end [ 0.369 -0.058  0.162]
   59        -step 310 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 12, 'obstruction5': 12, 'obstruction7': 11, 'obstruction2': 8} tool [ 0.369 -0.058  0.162] end [ 0.378 -0.004  0.141]
   60        -step 314 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 12, 'obstruction5': 12, 'obstruction7': 12, 'obstruction2': 8} tool [ 0.378 -0.004  0.141] end [ 0.314 -0.001  0.133]
   61        -ABORT step 323 tool [ 0.314 -0.001  0.191] q [-0.876  1.271 -1.006 -2.144 -0.994 -1.844 -6.417] target [-0.863  1.377 -1.109 -2.235 -1.124 -1.798 -6.385] tgt tool [ 0.314 -0.001  0.133]
   62        -step 324 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 12, 'obstruction5': 12, 'obstruction7': 12, 'obstruction2': 9} tool [ 0.314 -0.001  0.25 ] end [ 0.314 -0.056  0.141]
   63        -step 328 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 13, 'obstruction5': 12, 'obstruction7': 12, 'obstruction2': 9} tool [ 0.314 -0.056  0.141] end [ 0.344 -0.058  0.162]
   64        -step 338 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 13, 'obstruction5': 13, 'obstruction7': 12, 'obstruction2': 9} tool [ 0.344 -0.058  0.162] end [ 0.34  -0.004  0.141]
   65        -step 342 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 13, 'obstruction5': 13, 'obstruction7': 13, 'obstruction2': 9} tool [ 0.34  -0.004  0.141] end [ 0.308 -0.02   0.133]
   66        -step 352 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 13, 'obstruction5': 13, 'obstruction7': 13, 'obstruction2': 10} tool [ 0.308 -0.02   0.133] end [ 0.307 -0.049  0.141]
   67        -step 356 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 14, 'obstruction5': 13, 'obstruction7': 13, 'obstruction2': 10} tool [ 0.307 -0.049  0.141] end [ 0.375 -0.053  0.162]
   68        -step 366 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 14, 'obstruction5': 14, 'obstruction7': 13, 'obstruction2': 10} tool [ 0.375 -0.053  0.162] end [0.371 0.003 0.141]
   69        -step 370 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 14, 'obstruction5': 14, 'obstruction7': 14, 'obstruction2': 10} tool [0.371 0.003 0.141] end [ 0.308 -0.007  0.133]
   70        -ABORT step 379 tool [ 0.308 -0.007  0.191] q [-0.888  1.219 -1.037 -2.163 -0.971 -1.776 -6.418] target [-0.868  1.321 -1.147 -2.255 -1.105 -1.724 -6.376] tgt tool [ 0.308 -0.007  0.133]
   71        -step 380 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 14, 'obstruction5': 14, 'obstruction7': 14, 'obstruction2': 11} tool [ 0.308 -0.007  0.25 ] end [ 0.307 -0.037  0.141]
   72        -step 384 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 15, 'obstruction5': 14, 'obstruction7': 14, 'obstruction2': 11} tool [ 0.307 -0.037  0.141] end [ 0.337 -0.053  0.162]
   73        -step 394 task obstruction7 grasp 0.0 plan 10 fails {'obstruction0': 15, 'obstruction5': 15, 'obstruction7': 14, 'obstruction2': 11} tool [ 0.337 -0.053  0.162] end [0.346 0.003 0.141]
   74        -step 398 task obstruction2 grasp 0.0 plan 15 fails {'obstruction0': 15, 'obstruction5': 15, 'obstruction7': 15, 'obstruction2': 11} tool [0.346 0.003 0.141] end [ 0.301 -0.013  0.133]
   75        -ABORT step 407 tool [ 0.301 -0.013  0.191] q [-0.888  1.187 -1.05  -2.181 -0.953 -1.735 -6.405] target [-0.863  1.286 -1.164 -2.275 -1.09  -1.679 -6.356] tgt tool [ 0.301 -0.013  0.133]
   76        -step 408 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 15, 'obstruction5': 15, 'obstruction7': 15, 'obstruction2': 12} tool [ 0.301 -0.013  0.25 ] end [ 0.301 -0.043  0.141]
   77        -step 412 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 16, 'obstruction5': 15, 'obstruction7': 15, 'obstruction2': 12} tool [ 0.301 -0.043  0.141] end [ 0.369 -0.062  0.162]
   78        -step 422 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 16, 'obstruction5': 16, 'obstruction7': 15, 'obstruction2': 12} tool [ 0.369 -0.062  0.162] end [ 0.359 -0.024  0.169]
   79        -step 432 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 16, 'obstruction5': 16, 'obstruction7': 16, 'obstruction2': 12} tool [ 0.359 -0.024  0.169] end [ 0.315 -0.008  0.133]
   80        -ABORT step 440 tool [ 0.315 -0.008  0.191] q [-0.783  0.282 -2.139 -2.14  -0.312 -0.871 -2.736] target [-0.64   0.417 -2.265 -2.228 -0.503 -0.702 -2.552] tgt tool [ 0.315 -0.008  0.133]
   81        -step 441 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 16, 'obstruction5': 16, 'obstruction7': 16, 'obstruction2': 13} tool [ 0.315 -0.008  0.25 ] end [ 0.314 -0.062  0.141]
   82        -step 450 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 17, 'obstruction5': 16, 'obstruction7': 16, 'obstruction2': 13} tool [ 0.314 -0.062  0.141] end [ 0.344 -0.062  0.162]
   83        -step 460 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 17, 'obstruction5': 17, 'obstruction7': 16, 'obstruction2': 13} tool [ 0.344 -0.062  0.162] end [ 0.359 -0.011  0.169]
   84        -step 469 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 17, 'obstruction5': 17, 'obstruction7': 17, 'obstruction2': 13} tool [ 0.359 -0.011  0.169] end [ 0.309 -0.013  0.133]
   85        -ABORT step 477 tool [ 0.309 -0.013  0.191] q [-1.028  0.773 -1.395 -2.162 -0.804 -1.268 -5.197] target [-0.934  0.846 -1.556 -2.253 -0.962 -1.149 -5.092] tgt tool [ 0.309 -0.013  0.133]
   86        -step 478 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 17, 'obstruction5': 17, 'obstruction7': 17, 'obstruction2': 14} tool [ 0.309 -0.013  0.25 ] end [ 0.314 -0.024  0.141]
   87        -step 487 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 18, 'obstruction5': 17, 'obstruction7': 17, 'obstruction2': 14} tool [ 0.314 -0.024  0.141] end [ 0.375 -0.058  0.162]
   88        -step 497 task obstruction7 grasp 0.0 plan 8 fails {'obstruction0': 18, 'obstruction5': 18, 'obstruction7': 17, 'obstruction2': 14} tool [ 0.375 -0.058  0.162] end [ 0.365 -0.018  0.169]
   89        -step 501 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 18, 'obstruction5': 18, 'obstruction7': 18, 'obstruction2': 14} tool [ 0.365 -0.018  0.169] end [ 0.314 -0.032  0.133]
   90        -step 511 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 18, 'obstruction5': 18, 'obstruction7': 18, 'obstruction2': 15} tool [ 0.314 -0.032  0.133] end [ 0.307 -0.03   0.141]
   91        -step 515 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 19, 'obstruction5': 18, 'obstruction7': 18, 'obstruction2': 15} tool [ 0.307 -0.03   0.141] end [ 0.337 -0.058  0.162]
   92        -step 525 task obstruction7 grasp 0.0 plan 8 fails {'obstruction0': 19, 'obstruction5': 19, 'obstruction7': 18, 'obstruction2': 15} tool [ 0.337 -0.058  0.162] end [ 0.352 -0.018  0.169]
   93        -step 529 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 19, 'obstruction5': 19, 'obstruction7': 19, 'obstruction2': 15} tool [ 0.352 -0.018  0.169] end [0.314 0.006 0.133]
   94        -ABORT step 538 tool [0.314 0.006 0.191] q [-1.068  0.508 -1.673 -2.147 -0.601 -1.027 -3.986] target [-0.913  0.598 -1.861 -2.235 -0.775 -0.881 -3.844] tgt tool [0.314 0.006 0.133]
   95        -step 539 task obstruction0 grasp 0.0 plan 12 fails {'obstruction0': 19, 'obstruction5': 19, 'obstruction7': 19, 'obstruction2': 16} tool [0.314 0.006 0.25 ] end [ 0.307 -0.056  0.141]
   96        -step 543 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 20, 'obstruction5': 19, 'obstruction7': 19, 'obstruction2': 16} tool [ 0.307 -0.056  0.141] end [ 0.375 -0.062  0.162]
   97        -step 553 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 20, 'obstruction5': 20, 'obstruction7': 19, 'obstruction2': 16} tool [ 0.375 -0.062  0.162] end [ 0.352 -0.018  0.169]
   98        -step 563 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 20, 'obstruction5': 20, 'obstruction7': 20, 'obstruction2': 16} tool [ 0.352 -0.018  0.169] end [ 0.315 -0.003  0.133]
   99        -ABORT step 571 tool [ 0.315 -0.003  0.191] q [-0.794  0.28  -2.146 -2.14  -0.308 -0.87  -2.756] target [-0.652  0.415 -2.271 -2.228 -0.499 -0.7   -2.573] tgt tool [ 0.315 -0.003  0.133]
  100        -step 572 task obstruction0 grasp 0.0 plan 15 fails {'obstruction0': 20, 'obstruction5': 20, 'obstruction7': 20, 'obstruction2': 17} tool [ 0.315 -0.003  0.25 ] end [ 0.301 -0.049  0.141]
  101        -step 582 task obstruction5 grasp 0.0 plan 13 fails {'obstruction0': 21, 'obstruction5': 20, 'obstruction7': 20, 'obstruction2': 17} tool [ 0.301 -0.049  0.141] end [ 0.337 -0.062  0.162]
  102        -step 591 task obstruction7 grasp 0.0 plan 11 fails {'obstruction0': 21, 'obstruction5': 21, 'obstruction7': 20, 'obstruction2': 17} tool [ 0.337 -0.062  0.162] end [ 0.366 -0.018  0.169]
  103        -step 600 task obstruction2 grasp 0.0 plan 10 fails {'obstruction0': 21, 'obstruction5': 21, 'obstruction7': 21, 'obstruction2': 17} tool [ 0.366 -0.018  0.169] end [ 0.308 -0.026  0.133]
  104        -step 604 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 21, 'obstruction5': 21, 'obstruction7': 21, 'obstruction2': 18} tool [ 0.308 -0.026  0.133] end [ 0.301 -0.037  0.141]
  105        -step 608 task obstruction7 grasp 0.0 plan 13 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 21, 'obstruction2': 18} tool [ 0.301 -0.037  0.141] end [ 0.359 -0.025  0.169]
  106        -step 618 task obstruction2 grasp 0.0 plan 13 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 18} tool [ 0.359 -0.025  0.169] end [ 0.308 -0.001  0.133]
  107        -ABORT step 626 tool [ 0.308 -0.001  0.191] q [-1.017  0.388 -1.809 -2.165 -0.474 -0.937 -4.12 ] target [-0.834  0.501 -2.    -2.254 -0.668 -0.783 -3.947] tgt tool [ 0.308 -0.001  0.133]
  108        -step 628 task obstruction0 grasp 0.0 plan 11 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.308 -0.001  0.25 ] end [ 0.321 -0.043  0.158]
  109        -step 633 task obstruction0 grasp 1.0 plan 25 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.321 -0.043  0.158] end [ 0.207 -0.045  0.149]
  110        -step 649 task obstruction2 grasp 0.0 plan 12 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.207 -0.045  0.149] end [ 0.301 -0.026  0.133]
  111        -step 660 task obstruction2 grasp 1.0 plan 28 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.301 -0.026  0.133] end [0.307 0.079 0.124]
  112        -step 670 task obstruction5 grasp 0.0 plan 14 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [0.307 0.079 0.124] end [ 0.356 -0.053  0.162]
  113        -step 679 task obstruction5 grasp 1.0 plan 30 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.356 -0.053  0.162] end [0.427 0.086 0.154]
  114        -step 688 task obstruction7 grasp 0.0 plan 14 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [0.427 0.086 0.154] end [ 0.345 -0.018  0.141]
  115        -step 697 task obstruction7 grasp 1.0 plan 16 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.345 -0.018  0.141] end [0.254 0.098 0.133]
  116        -step 703 task target_block grasp 0.0 plan 19 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [0.254 0.098 0.133] end [ 0.299 -0.251  0.131]
  117        -step 712 task target_block grasp 1.0 plan 19 fails {'obstruction0': 22, 'obstruction5': 21, 'obstruction7': 22, 'obstruction2': 19} tool [ 0.299 -0.251  0.131] end [ 0.339 -0.03   0.143]
  118        -SOLVED 718
  119        -time 53.90831160545349
          12 +step 1 task obstruction0 grasp 0.0 plan 11 fails {} tool [0.154 0.001 0.217] end [ 0.321 -0.043  0.158]
          13 +step 7 task obstruction0 grasp 1.0 plan 19 fails {} tool [ 0.321 -0.043  0.158] end [ 0.207 -0.045  0.149]
          14 +step 15 task obstruction2 grasp 0.0 plan 12 fails {} tool [ 0.207 -0.045  0.149] end [ 0.314 -0.013  0.133]
          15 +step 22 task obstruction2 grasp 1.0 plan 17 fails {} tool [ 0.314 -0.013  0.133] end [0.321 0.092 0.124]
          16 +step 30 task obstruction5 grasp 0.0 plan 16 fails {} tool [0.321 0.092 0.124] end [ 0.356 -0.053  0.141]
          17 +step 39 task obstruction5 grasp 1.0 plan 18 fails {} tool [ 0.356 -0.053  0.141] end [0.427 0.086 0.133]
          18 +step 47 task obstruction7 grasp 0.0 plan 15 fails {} tool [0.427 0.086 0.133] end [ 0.359 -0.018  0.141]
          19 +step 56 task obstruction7 grasp 1.0 plan 16 fails {} tool [ 0.359 -0.018  0.141] end [0.267 0.098 0.133]
          20 +step 63 task target_block grasp 0.0 plan 19 fails {} tool [0.267 0.098 0.133] end [ 0.299 -0.251  0.131]
          21 +step 73 task target_block grasp 1.0 plan 19 fails {} tool [ 0.299 -0.251  0.131] end [ 0.339 -0.03   0.142]
          22 +SOLVED 80
          23 +time 4.28628945350647
diff --git a/r10v2.txt b/r10v2.txt
index 87b0071..e69de29 100644
--- a/r10v2.txt
+++ b/r10v2.txt
@@ -1,21 +0,0 @@
    1        -0 (True, 125, 10, 104.89492058753967)
    2        -1 (True, 119, 10, 77.4553337097168)
    3        -2 (True, 93, 10, 57.68733549118042)
    4        -3 (True, 78, 10, 45.96848201751709)
    5        -4 (True, 133, 10, 91.54850959777832)
    6        -5 (True, 114, 10, 61.649073362350464)
    7        -6 (True, 108, 10, 69.97951006889343)
    8        -7 (True, 161, 10, 111.96945834159851)
    9        -8 (True, 123, 10, 103.88562154769897)
   10        -9 (True, 87, 10, 74.52696228027344)
   11        -10 (True, 102, 10, 82.24074697494507)
   12        -11 (True, 96, 10, 74.87361359596252)
   13        -12 (True, 102, 10, 83.29399371147156)
   14        -13 (True, 136, 10, 93.86978816986084)
   15        -14 (True, 110, 10, 71.97742629051208)
   16        -15 (True, 132, 10, 69.7938084602356)
   17        -16 (True, 97, 10, 54.36871552467346)
   18        -17 (True, 76, 10, 31.4574453830719)
   19        -18 (True, 103, 10, 38.24239134788513)
   20        -19 (True, 84, 10, 30.301987886428833)
   21        -success 20 / 20 mean steps 108.95 max time 111.96945834159851
diff --git a/r7v2.txt b/r7v2.txt
index 68abf2a..8357ef0 100644
--- a/r7v2.txt
+++ b/r7v2.txt
@@ -1,30 +1,30 @@
    1        -0 (True, 87, 7, 51.90975046157837)
    2        -1 (True, 103, 7, 64.63951778411865)
    3        -2 (True, 71, 7, 43.29448342323303)
    4        -3 (True, 78, 7, 55.36353397369385)
    5        -4 (True, 136, 7, 79.30280208587646)
    6        -5 (True, 107, 7, 65.30765151977539)
    7        -6 (True, 105, 7, 58.917471170425415)
    8        -7 (True, 143, 7, 95.11450624465942)
    9        -8 (True, 85, 7, 58.49885559082031)
   10        -9 (True, 87, 7, 66.62173414230347)
   11        -10 (True, 69, 7, 48.08510160446167)
   12        -11 (True, 77, 7, 54.44292092323303)
   13        -12 (True, 107, 7, 80.1859929561615)
   14        -13 (True, 134, 7, 101.62912821769714)
   15        -14 (True, 61, 7, 44.37665367126465)
   16        -15 (True, 111, 7, 93.56963753700256)
   17        -16 (True, 62, 7, 44.71505546569824)
   18        -17 (True, 76, 7, 50.44370412826538)
   19        -18 (True, 84, 7, 64.29676413536072)
   20        -19 (True, 77, 7, 48.525261640548706)
   21        -20 (True, 90, 7, 67.16040682792664)
   22        -21 (True, 104, 7, 78.47161626815796)
   23        -22 (True, 184, 7, 86.10974502563477)
   24        -23 (True, 103, 7, 67.44490051269531)
   25        -24 (True, 76, 7, 53.59507131576538)
   26        -25 (True, 49, 7, 35.07913136482239)
   27        -26 (True, 69, 7, 44.36275577545166)
   28        -27 (True, 71, 7, 38.36406922340393)
   29        -28 (True, 108, 7, 32.490216970443726)
   30        -success 30 / 30 mean steps 92.86666666666666 max time 101.62912821769714
           1 +0 (True, 87, 7, 60.72479176521301)
           2 +1 (True, 103, 7, 83.07648015022278)
           3 +2 (True, 71, 7, 47.04066872596741)
           4 +3 (True, 78, 7, 62.394036293029785)
           5 +4 (True, 132, 7, 90.8275887966156)
           6 +5 (True, 107, 7, 78.71391916275024)
           7 +6 (True, 106, 7, 67.2218987941742)
           8 +7 (True, 131, 7, 98.29449915885925)
           9 +8 (True, 85, 7, 64.31360483169556)
          10 +9 (True, 87, 7, 65.40352606773376)
          11 +10 (True, 69, 7, 47.742194175720215)
          12 +11 (True, 77, 7, 57.84087514877319)
          13 +12 (True, 107, 7, 83.83754515647888)
          14 +13 (True, 132, 7, 102.52496147155762)
          15 +14 (True, 61, 7, 48.202779054641724)
          16 +15 (True, 111, 7, 96.96697163581848)
          17 +16 (True, 62, 7, 49.24976086616516)
          18 +17 (True, 76, 7, 57.130834341049194)
          19 +18 (True, 84, 7, 65.64731335639954)
          20 +19 (True, 82, 7, 67.95730423927307)
          21 +20 (True, 90, 7, 68.10633182525635)
          22 +21 (True, 104, 7, 76.37464356422424)
          23 +22 (True, 76, 7, 53.72096347808838)
          24 +23 (True, 103, 7, 65.23439359664917)
          25 +24 (True, 78, 7, 47.02994132041931)
          26 +25 (True, 49, 7, 36.07643413543701)
          27 +26 (True, 69, 7, 40.60338997840881)
          28 +27 (True, 71, 7, 37.73515844345093)
          29 +28 (True, 100, 7, 28.717182159423828)
          30 +success 30 / 30 mean steps 88.36666666666666 max time 102.52496147155762
diff --git a/r9.txt b/r9.txt
index 93bfdd5..fb094f8 100644
--- a/r9.txt
+++ b/r9.txt
@@ -1,31 +1,31 @@
    1        -100 (True, 96, 9, 52.53955030441284)
    2        -101 (True, 93, 9, 54.51079869270325)
    3        -102 (True, 112, 9, 65.34322571754456)
    4        -103 (True, 93, 9, 44.810567140579224)
    5        -104 (True, 153, 9, 93.75739359855652)
    6        -105 (True, 128, 9, 81.2679808139801)
    7        -106 (True, 93, 9, 62.40128564834595)
    8        -107 (True, 112, 9, 69.19037199020386)
    9        -108 (True, 131, 9, 91.25654864311218)
   10        -109 (True, 100, 9, 64.36337423324585)
   11        -110 (True, 121, 9, 79.18544244766235)
   12        -111 (True, 63, 9, 34.50396370887756)
   13        -112 (True, 144, 9, 99.37276291847229)
   14        -113 (True, 718, 9, 225.3370132446289)
   15        -114 (True, 82, 9, 43.92652463912964)
   16        -115 (True, 97, 9, 65.58510565757751)
   17        -116 (True, 86, 9, 52.46846628189087)
   18        -117 (True, 107, 9, 80.39322829246521)
   19        -118 (True, 137, 9, 93.61911106109619)
   20        -119 (True, 148, 9, 108.74081182479858)
   21        -120 (True, 106, 9, 68.54011392593384)
   22        -121 (True, 94, 9, 71.20775604248047)
   23        -122 (True, 121, 9, 81.89497876167297)
   24        -123 (True, 80, 9, 45.335349321365356)
   25        -124 (True, 104, 9, 61.29020118713379)
   26        -125 (True, 95, 9, 53.72698712348938)
   27        -126 (True, 78, 9, 39.93084263801575)
   28        -127 (True, 76, 9, 37.43912959098816)
   29        -128 (True, 84, 9, 34.11875557899475)
   30        -129 (True, 71, 9, 20.42490267753601)
   31        -success 30 / 30 mean steps 124.1 max time 225.3370132446289
           1 +100 (True, 96, 9, 67.79566717147827)
           2 +101 (True, 93, 9, 61.625250577926636)
           3 +102 (True, 98, 9, 73.67022275924683)
           4 +103 (True, 90, 9, 46.72491192817688)
           5 +104 (True, 143, 9, 96.65303158760071)
           6 +105 (True, 122, 9, 77.48038005828857)
           7 +106 (True, 93, 9, 47.51486015319824)
           8 +107 (True, 112, 9, 72.36881613731384)
           9 +108 (True, 131, 9, 110.22542905807495)
          10 +109 (True, 100, 9, 70.26443481445312)
          11 +110 (True, 121, 9, 92.87895226478577)
          12 +111 (True, 72, 9, 44.093530893325806)
          13 +112 (True, 113, 9, 81.1205563545227)
          14 +113 (True, 80, 9, 54.67210102081299)
          15 +114 (True, 82, 9, 55.89376902580261)
          16 +115 (True, 97, 9, 79.13153052330017)
          17 +116 (True, 64, 9, 51.10925650596619)
          18 +117 (True, 104, 9, 81.26630234718323)
          19 +118 (True, 125, 9, 102.77139973640442)
          20 +119 (True, 148, 9, 114.42909741401672)
          21 +120 (True, 105, 9, 74.66918158531189)
          22 +121 (True, 80, 9, 51.272884368896484)
          23 +122 (True, 113, 9, 87.74087524414062)
          24 +123 (True, 80, 9, 51.04293632507324)
          25 +124 (True, 104, 9, 71.35939741134644)
          26 +125 (True, 100, 9, 57.89858102798462)
          27 +126 (True, 78, 9, 48.48291540145874)
          28 +127 (True, 73, 9, 38.89868927001953)
          29 +128 (True, 80, 9, 32.20427870750427)
          30 +129 (True, 71, 9, 26.382763624191284)
          31 +success 30 / 30 mean steps 98.93333333333334 max time 114.42909741401672
```

</details>

<a id="C023"></a>
### C023 · faster fk_jac; early-stop failing pick paths

Commit `fd8e56ae51db44d9611ffc81e1a72597aea0f7c5`; parents: 1fc80533cd4fade9324d12c67271240b8db6b410. Recorded author date: 2026-10-01T00:41:47+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E1153](01_timeline.md#E1153): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C023_fd8e56a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index 1d2c701..8f40652 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -119,7 +119,7 @@ class GeneratedApproach:
  119    119                  best = np.clip(q, -JLIM, JLIM)
  120    120          return best, False
  121    121  
  122        -    def _cart_path(self, q0, p_from, p_to, R, step=0.04, R_from=None):
         122 +    def _cart_path(self, q0, p_from, p_to, R, step=0.04, R_from=None, stop_on_fail=False):
  123    123          """IK waypoints along a straight line in tool position; orientation interpolated
  124    124          from R_from (default: R) to R."""
  125    125          p_from = np.asarray(p_from, float)
@@ -138,6 +138,8 @@ class GeneratedApproach:
  138    138              q, ok = self._ik(q, p, Ri)
  139    139              allok &= ok
  140    140              qs.append(q.copy())
         141 +            if stop_on_fail and not ok:
         142 +                return qs, q, False
  141    143          return qs, q, allok
  142    144  
  143    145      @staticmethod
@@ -338,20 +340,24 @@ class GeneratedApproach:
  338    340          above = np.array([gx, gy, max(zt, p0[2])])
  339    341          start = np.array([p0[0], p0[1], max(p0[2], zt)])
  340    342          best = None
  341        -        for y in [yaw, yaw + np.pi]:
         343 +        for y, sof in [(yaw, True), (yaw + np.pi, True), (yaw, False)]:
         344 +            if not sof and best is not None and best[0] < 100:
         345 +                break
  342    346              R = kin.topdown_R(y)
  343    347              q = q0
  344    348              plan = []
  345    349              if p0[2] < zt - 0.005:
  346    350                  qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.015)
  347    351                  plan += self._seg(qs)
  348        -            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.04, R_from=T[:3, :3])
  349        -            plan += self._seg(qs)
  350        -            qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.015)
         352 +            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.04, R_from=T[:3, :3], stop_on_fail=sof)
  351    353              plan += self._seg(qs)
         354 +            ok2 = False
         355 +            if ok1 or not sof:
         356 +                qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.015, stop_on_fail=sof)
         357 +                plan += self._seg(qs)
  352    358              plan += [('grip', -1.0), ('check', 'grasp')]
  353    359              c = self._plan_cost(q0, plan) + (0 if (ok1 and ok2) else 100)
  354        -            if best is None or c < best[0]:
         360 +            if best is None or c < best[0] or (not sof and best[0] >= 100):
  355    361                  best = (c, plan)
  356    362          self.plan = best[1]
  357    363  
diff --git a/kin.py b/kin.py
index 4de5f7f..7740fdf 100644
--- a/kin.py
+++ b/kin.py
@@ -40,25 +40,33 @@ def fk(base, q, tool=None, base_z=None):
   40     40      Tt = np.eye(4); Tt[2, 3] = tool
   41     41      return T @ Tt
   42     42  
          43 +_JR = [J[:3, :3].copy() for J in JOINTS]
          44 +_JP = [J[:3, 3].copy() for J in JOINTS]
          45 +_EER = EE[:3, :3].copy(); _EEP = EE[:3, 3].copy()
          46 +
   43     47  def fk_jac(base, q, tool=None, base_z=None):
   44     48      tool = TOOL if tool is None else tool
   45     49      base_z = BASE_Z if base_z is None else base_z
   46        -    T = np.eye(4)
   47        -    T[:3, :3] = rpy_mat(0, 0, base[2]); T[:3, 3] = [base[0], base[1], base_z]
   48        -    M = np.eye(4); M[0, 3] = MOUNT_X; T = T @ M
   49        -    axes = []; origins = []
   50        -    for J, qi in zip(JOINTS, q):
   51        -        T = T @ J
   52        -        axes.append(T[:3, 2].copy()); origins.append(T[:3, 3].copy())
   53        -        T = T @ rotz(qi)
   54        -    T = T @ EE
   55        -    Tt = np.eye(4); Tt[2, 3] = tool
   56        -    T = T @ Tt
   57        -    p = T[:3, 3]
   58        -    Jm = np.zeros((6, 7))
          50 +    c0, s0 = np.cos(base[2]), np.sin(base[2])
          51 +    R = np.array([[c0, -s0, 0.0], [s0, c0, 0.0], [0.0, 0.0, 1.0]])
          52 +    p = np.array([base[0] + MOUNT_X * c0, base[1] + MOUNT_X * s0, base_z])
          53 +    axes = np.empty((7, 3)); origins = np.empty((7, 3))
          54 +    cq = np.cos(q); sq = np.sin(q)
   59     55      for i in range(7):
   60        -        Jm[:3, i] = np.cross(axes[i], p - origins[i])
   61        -        Jm[3:, i] = axes[i]
          56 +        p = p + R @ _JP[i]
          57 +        R = R @ _JR[i]
          58 +        axes[i] = R[:, 2]; origins[i] = p
          59 +        c, s_ = cq[i], sq[i]
          60 +        x = R[:, 0] * c + R[:, 1] * s_
          61 +        y = -R[:, 0] * s_ + R[:, 1] * c
          62 +        R = np.column_stack((x, y, R[:, 2]))
          63 +    p = p + R @ _EEP
          64 +    R = R @ _EER
          65 +    p = p + R[:, 2] * tool
          66 +    T = np.eye(4); T[:3, :3] = R; T[:3, 3] = p
          67 +    Jm = np.empty((6, 7))
          68 +    Jm[:3] = np.cross(axes, p - origins).T
          69 +    Jm[3:] = axes.T
   62     70      return T, Jm
   63     71  
   64     72  def rot_err(Rc, Rt):
diff --git a/prof.out b/prof.out
index 178365c..3689feb 100644
Binary files a/prof.out and b/prof.out differ
diff --git a/r10v2.txt b/r10v2.txt
index e69de29..bb2d5ea 100644
--- a/r10v2.txt
+++ b/r10v2.txt
@@ -0,0 +1,21 @@
           1 +0 (True, 108, 10, 67.34670829772949)
           2 +1 (True, 118, 10, 77.54825496673584)
           3 +2 (True, 93, 10, 48.29496169090271)
           4 +3 (True, 79, 10, 56.12954092025757)
           5 +4 (True, 149, 10, 113.7067198753357)
           6 +5 (True, 107, 10, 60.19983792304993)
           7 +6 (True, 107, 10, 72.70078706741333)
           8 +7 (True, 136, 10, 96.57177400588989)
           9 +8 (True, 123, 10, 100.32531452178955)
          10 +9 (True, 87, 10, 70.76278758049011)
          11 +10 (True, 96, 10, 74.97967839241028)
          12 +11 (True, 95, 10, 79.21565651893616)
          13 +12 (True, 102, 10, 85.22674655914307)
          14 +13 (True, 133, 10, 96.41449117660522)
          15 +14 (True, 104, 10, 70.36861729621887)
          16 +15 (True, 162, 10, 78.65981841087341)
          17 +16 (True, 90, 10, 49.643895626068115)
          18 +17 (True, 76, 10, 32.62133312225342)
          19 +18 (True, 98, 10, 37.19398069381714)
          20 +19 (True, 82, 10, 29.940195083618164)
          21 +success 20 / 20 mean steps 107.25 max time 113.7067198753357
diff --git a/r12.txt b/r12.txt
new file mode 100644
index 0000000..4bf8a43
--- /dev/null
+++ b/r12.txt
@@ -0,0 +1,21 @@
           1 +300 (True, 115, 12, 81.14850687980652)
           2 +301 (True, 88, 12, 64.5822856426239)
           3 +302 (True, 114, 12, 85.81254434585571)
           4 +303 (True, 81, 12, 52.839638233184814)
           5 +304 (True, 110, 12, 87.20249605178833)
           6 +305 (True, 125, 12, 95.99293088912964)
           7 +306 (True, 104, 12, 63.38118505477905)
           8 +307 (True, 126, 12, 93.74397993087769)
           9 +308 (True, 97, 12, 78.29080271720886)
          10 +309 (True, 57, 12, 49.033607959747314)
          11 +310 (True, 111, 12, 83.51215243339539)
          12 +311 (True, 92, 12, 68.35979056358337)
          13 +312 (True, 326, 12, 129.26185965538025)
          14 +313 (True, 96, 12, 67.20955419540405)
          15 +314 (True, 85, 12, 52.939067125320435)
          16 +315 (True, 122, 12, 73.23364591598511)
          17 +316 (True, 73, 12, 51.60581183433533)
          18 +317 (True, 104, 12, 50.959702491760254)
          19 +318 (True, 149, 12, 41.87000894546509)
          20 +319 (True, 102, 12, 30.127414226531982)
          21 +success 20 / 20 mean steps 113.85 max time 129.26185965538025
diff --git a/r15.txt b/r15.txt
new file mode 100644
index 0000000..8141ce4
--- /dev/null
+++ b/r15.txt
@@ -0,0 +1,17 @@
           1 +300 (True, 137, 15, 92.13922357559204)
           2 +301 (True, 88, 15, 66.16345858573914)
           3 +302 (True, 126, 15, 80.64890599250793)
           4 +303 (True, 81, 15, 41.766000270843506)
           5 +304 (True, 117, 15, 70.7319004535675)
           6 +305 (True, 147, 15, 106.49297714233398)
           7 +306 (True, 104, 15, 59.91490602493286)
           8 +307 (True, 126, 15, 91.23219919204712)
           9 +308 (True, 110, 15, 83.98466873168945)
          10 +309 (True, 64, 15, 58.519328594207764)
          11 +310 (True, 130, 15, 77.43858695030212)
          12 +311 (True, 94, 15, 59.47879433631897)
          13 +312 (True, 339, 15, 92.68320178985596)
          14 +313 (True, 96, 15, 44.86985516548157)
          15 +314 (True, 115, 15, 49.378417015075684)
          16 +315 (True, 139, 15, 44.1101233959198)
          17 +success 16 / 16 mean steps 125.8125 max time 106.49297714233398
diff --git a/rd3.txt b/rd3.txt
new file mode 100644
index 0000000..d8d6b6f
--- /dev/null
+++ b/rd3.txt
@@ -0,0 +1,71 @@
           1 +202 (True, 18, 0, 27.73287272453308)
           2 +204 (True, 49, 2, 61.287132024765015)
           3 +205 (True, 27, 1, 36.66383147239685)
           4 +206 (True, 29, 1, 47.65899419784546)
           5 +208 (True, 29, 2, 38.839773416519165)
           6 +209 (True, 51, 2, 65.3223819732666)
           7 +215 (True, 44, 2, 43.45367407798767)
           8 +216 (True, 27, 2, 25.484310150146484)
           9 +217 (True, 42, 2, 43.442408323287964)
          10 +218 (True, 26, 1, 23.96134901046753)
          11 +220 (True, 51, 2, 49.786393880844116)
          12 +221 (True, 28, 1, 23.406315565109253)
          13 +222 (True, 29, 1, 24.481075286865234)
          14 +223 (True, 34, 1, 28.300625324249268)
          15 +224 (True, 44, 2, 40.41614127159119)
          16 +225 (True, 50, 2, 54.274471282958984)
          17 +226 (True, 40, 2, 36.43033766746521)
          18 +227 (True, 31, 1, 23.912862539291382)
          19 +228 (True, 31, 1, 30.22028660774231)
          20 +229 (True, 27, 1, 29.45495843887329)
          21 +230 (True, 27, 1, 34.24670696258545)
          22 +231 (True, 17, 0, 23.85062050819397)
          23 +232 (True, 33, 1, 37.69010400772095)
          24 +234 (True, 32, 1, 29.700351238250732)
          25 +235 (True, 31, 2, 29.42720675468445)
          26 +236 (True, 31, 1, 28.88853120803833)
          27 +237 (True, 52, 2, 54.30154061317444)
          28 +239 (True, 41, 2, 32.954620361328125)
          29 +240 (True, 26, 2, 20.426220655441284)
          30 +241 (True, 30, 1, 30.38412642478943)
          31 +242 (True, 28, 2, 23.499953031539917)
          32 +243 (True, 43, 2, 48.63018822669983)
          33 +244 (True, 38, 2, 41.15494132041931)
          34 +245 (True, 44, 2, 49.27907991409302)
          35 +246 (True, 30, 2, 33.075631618499756)
          36 +248 (True, 26, 1, 28.241211891174316)
          37 +249 (True, 53, 2, 68.17695212364197)
          38 +250 (True, 39, 1, 43.90685176849365)
          39 +251 (True, 20, 0, 24.087523698806763)
          40 +252 (True, 29, 2, 28.337980031967163)
          41 +253 (True, 28, 1, 30.466415882110596)
          42 +256 (True, 37, 1, 33.45723795890808)
          43 +257 (True, 30, 2, 27.7175076007843)
          44 +258 (True, 28, 1, 33.932722330093384)
          45 +260 (True, 52, 2, 57.85380721092224)
          46 +262 (True, 45, 2, 42.90711164474487)
          47 +263 (True, 38, 2, 37.807838678359985)
          48 +265 (True, 36, 2, 38.05839800834656)
          49 +267 (True, 34, 1, 29.96534299850464)
          50 +268 (True, 46, 2, 41.60264539718628)
          51 +269 (True, 35, 2, 42.413174867630005)
          52 +270 (True, 34, 1, 44.13262891769409)
          53 +271 (True, 49, 2, 59.34237480163574)
          54 +273 (True, 19, 0, 22.78810453414917)
          55 +274 (True, 31, 1, 34.58255100250244)
          56 +275 (True, 20, 0, 24.821569442749023)
          57 +276 (True, 34, 1, 40.61282253265381)
          58 +277 (True, 23, 0, 30.57959008216858)
          59 +278 (True, 33, 1, 35.073092460632324)
          60 +280 (True, 39, 1, 47.199262380599976)
          61 +281 (True, 31, 1, 31.54364252090454)
          62 +282 (True, 49, 2, 56.83739113807678)
          63 +283 (True, 17, 0, 22.39292550086975)
          64 +285 (True, 55, 2, 68.52681922912598)
          65 +286 (True, 16, 0, 20.953136444091797)
          66 +287 (True, 39, 2, 48.93290042877197)
          67 +289 (True, 46, 1, 51.6232705116272)
          68 +291 (True, 22, 0, 21.177863836288452)
          69 +292 (True, 38, 2, 37.84365892410278)
          70 +295 (True, 18, 0, 20.1457040309906)
          71 +success 100 / 100 mean steps 29.25 max time 68.52681922912598
diff --git a/timing.py b/timing.py
index 75e78fb..2856330 100644
--- a/timing.py
+++ b/timing.py
@@ -5,7 +5,7 @@ import os, importlib as _il
    5      5  GeneratedApproach = _il.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
    6      6  tot=[]; 
    7      7  for seed in range(int(sys.argv[1]), int(sys.argv[2])):
    8        -    env = make_env(); obs, info = env.reset(seed=seed)
           8 +    env = make_env(); obs, info = env.reset(seed=seed, options=({'object_count': int(sys.argv[3])} if len(sys.argv)>3 else None))
    9      9      ap = GeneratedApproach(env.action_space, env.observation_space, {})
   10     10      t0=time.time(); ap.reset(obs, info); ct=time.time()-t0; mx=0
   11     11      for t in range(1000):
```

</details>

<a id="C024"></a>
### C024 · move base backward when pick/place point is too close to arm mount

Commit `2b3712c64154d0e000cfc91132a1598e4c141417`; parents: fd8e56ae51db44d9611ffc81e1a72597aea0f7c5. Recorded author date: 2026-10-01T00:50:29+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E1198](01_timeline.md#E1198): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C024_2b3712c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_v2.py b/approach_v2.py
index 8f40652..0333d0c 100644
--- a/approach_v2.py
+++ b/approach_v2.py
@@ -328,10 +328,45 @@ class GeneratedApproach:
  328    328                  q = item[1]
  329    329          return c
  330    330  
         331 +    def _mount(self, base=None):
         332 +        b = self.base if base is None else base
         333 +        return np.array([b[0] + kin.MOUNT_X * np.cos(b[2]), b[1] + kin.MOUNT_X * np.sin(b[2])])
         334 +
         335 +    def _base_for(self, pts, rmin=0.165):
         336 +        m = self._mount()
         337 +        need = m[0]
         338 +        for p in pts:
         339 +            dy = p[1] - m[1]
         340 +            if np.hypot(p[0] - m[0], dy) < rmin - 0.005:
         341 +                need = min(need, p[0] - np.sqrt(max(rmin ** 2 - dy ** 2, 0.0)))
         342 +        if need >= m[0] - 1e-4:
         343 +            return None
         344 +        nb = np.array(self.base, float).copy()
         345 +        nb[0] -= (m[0] - need)
         346 +        return nb
         347 +
         348 +    def _plan_base_move(self, state, objs, held, nb):
         349 +        q = self._q(state)
         350 +        T = self._tool(q)
         351 +        p0 = T[:3, 3]
         352 +        zt = self._ztransit(objs, held)
         353 +        plan = []
         354 +        if p0[2] < zt:
         355 +            qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], zt]), T[:3, :3], step=0.015)
         356 +            plan = self._seg(qs)
         357 +        self.plan = plan + [('base', nb)]
         358 +
  331    359      def _plan_pick(self, state, name, cand):
  332    360          objs = self._parse(state)
  333    361          o = objs[name]
  334    362          _, yaw, gx, gy, _, _ = cand
         363 +        pts = [(gx, gy)]
         364 +        if name == 'target_block':
         365 +            pts.append(tuple(objs['target_region'].p[:2]))
         366 +        nb = self._base_for(pts)
         367 +        if nb is not None:
         368 +            self._plan_base_move(state, objs, None, nb)
         369 +            return
  335    370          zt = self._ztransit(objs, None)
  336    371          q0 = self._q(state)
  337    372          T = self._tool(q0)
@@ -369,6 +404,8 @@ class GeneratedApproach:
  369    404              for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
  370    405                  p = np.array([x, y])
  371    406                  cost = np.linalg.norm(p - cur) + 2.0 * max(0.0, 0.2 - x)
         407 +                if np.linalg.norm(p - self._mount()) < 0.17:
         408 +                    continue
  372    409                  if any(np.linalg.norm(p - bs) < 0.035 for bs in self.bad_spots):
  373    410                      continue
  374    411                  if best is not None and cost >= best[0]:
@@ -397,6 +434,10 @@ class GeneratedApproach:
  397    434      def _plan_place(self, state, name, xy, support_top, yaw_obj):
  398    435          objs = self._parse(state)
  399    436          o = objs[name]
         437 +        nb = self._base_for([xy])
         438 +        if nb is not None:
         439 +            self._plan_base_move(state, objs, name, nb)
         440 +            return
  400    441          q = self._q(state)
  401    442          T = self._tool(q)
  402    443          G = self._G(state)
@@ -555,6 +596,7 @@ class GeneratedApproach:
  555    596          self.steps += 1
  556    597          a = np.zeros(11, dtype=np.float32)
  557    598          q = self._q(state)
         599 +        self.base = self._base(state)
  558    600          for _ in range(20):
  559    601              if not self.plan:
  560    602                  self.aborting = False
@@ -588,6 +630,18 @@ class GeneratedApproach:
  588    630                  a[3:10] = np.clip(wrap(target - q), -0.2, 0.2)
  589    631                  return a
  590    632              self.aborting = False
         633 +            if kind == 'base':
         634 +                cur = np.array(self.base, float)
         635 +                d = np.array(val, float) - cur
         636 +                d[2] = wrap(d[2])
         637 +                lb = getattr(self, 'last_base', None)
         638 +                if np.max(np.abs(d)) < 1e-4 or (lb is not None and np.max(np.abs(cur - lb)) < 1e-7):
         639 +                    self.plan.pop(0)
         640 +                    self.last_base = None
         641 +                    continue
         642 +                self.last_base = cur.copy()
         643 +                a[0:3] = np.clip(d, -0.1, 0.1)
         644 +                return a
  591    645              if kind == 'grip':
  592    646                  self.plan.pop(0)
  593    647                  a[10] = val
diff --git a/basetest.py b/basetest.py
new file mode 100644
index 0000000..fde898d
--- /dev/null
+++ b/basetest.py
@@ -0,0 +1,8 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from common import *
           4 +env=make_env(); obs,_=env.reset(seed=312, options={'object_count':15})
           5 +print(env.action_space)
           6 +for d in [(-0.05,0,0),(-0.1,0,0),(0,0.05,0)]:
           7 +    a=np.zeros(11,dtype=np.float32); a[0:3]=d
           8 +    obs,*_=env.step(a); print(d, getbase(obs))
diff --git a/d312.txt b/d312.txt
new file mode 100644
index 0000000..266fa89
--- /dev/null
+++ b/d312.txt
@@ -0,0 +1,260 @@
           1 +obstruction0 [0.126 0.034 0.111] [0.015 0.013 0.026]
           2 +obstruction1 [0.171 0.009 0.104] [0.015 0.016 0.019]
           3 +obstruction10 [ 0.192 -0.334  0.095] [0.015 0.012 0.02 ]
           4 +obstruction11 [0.258 0.103 0.09 ] [0.019 0.018 0.015]
           5 +obstruction12 [0.226 0.043 0.097] [0.014 0.019 0.022]
           6 +obstruction13 [0.131 0.059 0.098] [0.012 0.011 0.013]
           7 +obstruction14 [0.431 0.096 0.086] [0.012 0.014 0.011]
           8 +obstruction2 [0.166 0.064 0.113] [0.02  0.018 0.028]
           9 +obstruction3 [0.106 0.006 0.1  ] [0.018 0.013 0.015]
          10 +obstruction4 [0.345 0.1   0.087] [0.014 0.016 0.012]
          11 +obstruction5 [ 0.114 -0.111  0.09 ] [0.012 0.019 0.015]
          12 +obstruction6 [0.302 0.179 0.094] [0.016 0.011 0.019]
          13 +obstruction7 [ 0.387 -0.166  0.09 ] [0.017 0.014 0.015]
          14 +obstruction8 [ 0.331 -0.377  0.088] [0.017 0.011 0.013]
          15 +obstruction9 [ 0.396 -0.04   0.099] [0.017 0.013 0.024]
          16 +target_block [ 0.47  -0.266  0.1  ] [0.029 0.025 0.025]
          17 +target_region [0.143 0.038 0.08 ] [0.036 0.031 0.005]
          18 +step 1 task obstruction0 grasp 0.0 plan 8 fails {} tool [0.154 0.001 0.217] end [0.126 0.034 0.165]
          19 +step 5 task obstruction0 grasp 1.0 plan 26 fails {} tool [0.126 0.034 0.165] end [ 0.205 -0.087  0.157]
          20 +step 17 task obstruction1 grasp 0.0 plan 13 fails {} tool [ 0.205 -0.087  0.157] end [0.171 0.009 0.152]
          21 +step 27 task obstruction1 grasp 1.0 plan 17 fails {} tool [0.171 0.009 0.152] end [ 0.285 -0.004  0.143]
          22 +step 34 task obstruction2 grasp 0.0 plan 15 fails {} tool [ 0.285 -0.004  0.143] end [0.166 0.064 0.141]
          23 +step 44 task obstruction2 grasp 1.0 plan 17 fails {} tool [0.166 0.064 0.141] end [0.21  0.178 0.133]
          24 +step 52 task obstruction13 grasp 0.0 plan 15 fails {} tool [0.21  0.178 0.133] end [0.143 0.064 0.138]
          25 +step 64 task obstruction13 grasp 1.0 plan 18 fails {} tool [0.143 0.064 0.138] end [0.214 0.236 0.129]
          26 +step 72 task obstruction3 grasp 0.0 plan 17 fails {} tool [0.214 0.236 0.129] end [0.158 0.008 0.156]
          27 +step 80 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 1} tool [0.158 0.008 0.156] end [ 0.153 -0.004  0.153]
          28 +step 86 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 2} tool [ 0.153 -0.004  0.153] end [0.15  0.012 0.152]
          29 +step 91 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 3} tool [0.15  0.012 0.152] end [ 0.149 -0.     0.156]
          30 +step 97 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 4} tool [ 0.149 -0.     0.156] end [0.149 0.003 0.148]
          31 +step 102 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 5} tool [0.149 0.003 0.148] end [0.152 0.005 0.153]
          32 +ABORT step 110 tool [0.117 0.005 0.182] q [ 0.537 -0.307 -3.516 -2.594 -0.164 -0.828  3.056] target [ 0.417 -0.319 -3.445 -2.605 -0.125 -0.846  3.353] tgt tool [0.106 0.006 0.182]
          33 +step 113 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 6} tool [0.119 0.005 0.219] end [0.146 0.015 0.151]
          34 +step 122 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 7} tool [0.146 0.015 0.151] end [ 0.147 -0.018  0.152]
          35 +step 128 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 8} tool [ 0.147 -0.018  0.152] end [ 0.146 -0.014  0.156]
          36 +step 134 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 9} tool [ 0.146 -0.014  0.156] end [ 0.147 -0.009  0.148]
          37 +step 139 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 10} tool [ 0.147 -0.009  0.148] end [0.144 0.001 0.156]
          38 +step 145 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 11} tool [0.144 0.001 0.156] end [0.145 0.005 0.148]
          39 +step 150 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 12} tool [0.145 0.005 0.148] end [0.146 0.    0.145]
          40 +step 157 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 13} tool [0.146 0.    0.145] end [ 0.142 -0.012  0.16 ]
          41 +step 164 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 14} tool [ 0.142 -0.012  0.16 ] end [0.15  0.01  0.152]
          42 +ABORT step 170 tool [0.115 0.006 0.182] q [ 0.782 -0.363 -3.656 -2.598 -0.248 -0.854  3.229] target [ 0.644 -0.351 -3.611 -2.6   -0.206 -0.868  3.475] tgt tool [0.106 0.012 0.182]
          43 +step 172 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 15} tool [0.115 0.006 0.218] end [ 0.151 -0.004  0.153]
          44 +ABORT step 173 tool [0.115 0.006 0.218] q [ 0.763 -0.458 -3.569 -2.499 -0.227 -1.053  3.257] target [ 0.624 -0.433 -3.48  -2.502 -0.161 -1.056  3.537] tgt tool [0.106 0.001 0.218]
          45 +step 174 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 16} tool [0.115 0.006 0.218] end [0.151 0.004 0.149]
          46 +ABORT step 175 tool [0.115 0.006 0.218] q [ 0.763 -0.458 -3.569 -2.499 -0.227 -1.053  3.257] target [ 0.627 -0.418 -3.523 -2.492 -0.175 -1.047  3.506] tgt tool [0.113 0.006 0.218]
          47 +step 176 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 17} tool [0.115 0.006 0.218] end [0.15  0.001 0.156]
          48 +ABORT step 177 tool [0.115 0.006 0.218] q [ 0.763 -0.458 -3.569 -2.499 -0.227 -1.053  3.257] target [ 0.614 -0.461 -3.483 -2.511 -0.17  -1.075  3.529] tgt tool [0.1   0.006 0.218]
          49 +step 178 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 18} tool [0.115 0.006 0.218] end [ 0.144 -0.029  0.151]
          50 +step 186 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 19} tool [ 0.144 -0.029  0.151] end [0.142 0.017 0.151]
          51 +step 193 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 20} tool [0.142 0.017 0.151] end [0.142 0.006 0.155]
          52 +step 199 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 21} tool [0.142 0.006 0.155] end [0.144 0.011 0.148]
          53 +step 204 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 22} tool [0.144 0.011 0.148] end [ 0.138 -0.031  0.156]
          54 +step 212 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 23} tool [ 0.138 -0.031  0.156] end [ 0.141 -0.022  0.149]
          55 +step 217 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 24} tool [ 0.141 -0.022  0.149] end [ 0.143 -0.011  0.145]
          56 +step 223 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 25} tool [ 0.143 -0.011  0.145] end [0.142 0.003 0.145]
          57 +step 229 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 26} tool [0.142 0.003 0.145] end [ 0.136 -0.027  0.161]
          58 +step 236 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 27} tool [ 0.136 -0.027  0.161] end [ 0.136 -0.011  0.161]
          59 +step 242 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 28} tool [ 0.136 -0.011  0.161] end [ 0.149 -0.014  0.152]
          60 +ABORT step 247 tool [ 0.118 -0.007  0.182] q [ 1.109 -0.423 -3.763 -2.597 -0.329 -0.883  3.277] target [ 0.994 -0.391 -3.706 -2.599 -0.278 -0.878  3.476] tgt tool [ 0.112 -0.006  0.182]
          61 +step 249 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 29} tool [ 0.118 -0.007  0.25 ] end [0.148 0.015 0.151]
          62 +ABORT step 250 tool [ 0.118 -0.007  0.25 ] q [ 1.056 -0.563 -3.586 -2.405 -0.263 -1.228  3.297] target [ 0.794 -0.545 -3.57  -2.404 -0.229 -1.25   3.637] tgt tool [0.106 0.017 0.25 ]
          63 +step 251 task obstruction3 grasp 0.0 plan 15 fails {'obstruction3': 30} tool [ 0.118 -0.007  0.28 ] end [ 0.129 -0.025  0.165]
          64 +ABORT step 256 tool [0.085 0.006 0.224] q [ 1.469 -0.75  -3.619 -2.506 -0.328 -1.339  2.756] target [ 1.526 -0.691 -3.749 -2.638 -0.413 -1.135  2.788] tgt tool [0.085 0.006 0.179]
          65 +step 257 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 31} tool [0.085 0.006 0.254] end [ 0.142 -0.002  0.142]
          66 +step 263 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 32} tool [ 0.142 -0.002  0.142] end [ 0.148 -0.006  0.149]
          67 +ABORT step 269 tool [ 0.124 -0.     0.182] q [ 1.264 -0.443 -3.905 -2.571 -0.385 -0.925  3.325] target [ 1.009 -0.386 -3.767 -2.587 -0.287 -0.893  3.744] tgt tool [0.113 0.001 0.182]
          68 +step 271 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 33} tool [ 0.124 -0.     0.25 ] end [0.148 0.008 0.148]
          69 +ABORT step 272 tool [ 0.124 -0.     0.25 ] q [ 1.183 -0.573 -3.69  -2.385 -0.306 -1.263  3.34 ] target [ 0.91  -0.542 -3.61  -2.396 -0.248 -1.248  3.723] tgt tool [0.113 0.012 0.25 ]
          70 +step 273 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 34} tool [ 0.124 -0.     0.28 ] end [ 0.148 -0.01   0.156]
          71 +ABORT step 274 tool [ 0.124 -0.     0.28 ] q [ 1.166 -0.597 -3.636 -2.299 -0.281 -1.378  3.337] target [ 1.02  -0.584 -3.559 -2.313 -0.234 -1.373  3.551] tgt tool [0.112 0.    0.28 ]
          72 +step 275 task obstruction3 grasp 0.0 plan 16 fails {'obstruction3': 35} tool [ 0.124 -0.     0.31 ] end [0.147 0.005 0.155]
          73 +ABORT step 277 tool [0.112 0.006 0.31 ] q [ 1.008 -0.608 -3.537 -2.222 -0.226 -1.486  3.532] target [ 0.86  -0.613 -3.483 -2.234 -0.194 -1.495  3.734] tgt tool [0.1   0.012 0.31 ]
          74 +step 278 task obstruction3 grasp 0.0 plan 17 fails {'obstruction3': 36} tool [0.112 0.006 0.34 ] end [ 0.147 -0.005  0.159]
          75 +ABORT step 279 tool [0.112 0.006 0.34 ] q [ 1.002 -0.61  -3.509 -2.131 -0.211 -1.583  3.528] target [ 0.845 -0.621 -3.424 -2.148 -0.163 -1.596  3.751] tgt tool [0.094 0.006 0.34 ]
          76 +step 280 task obstruction3 grasp 0.0 plan 19 fails {'obstruction3': 37} tool [0.112 0.006 0.37 ] end [0.148 0.004 0.145]
          77 +ABORT step 283 tool [0.119 0.006 0.308] q [ 0.879 -0.554 -3.532 -2.218 -0.203 -1.446  3.71 ] target [ 0.897 -0.512 -3.605 -2.38  -0.234 -1.236  3.706] tgt tool [0.119 0.006 0.253]
          78 +step 284 task obstruction3 grasp 0.0 plan 21 fails {'obstruction3': 38} tool [0.119 0.006 0.338] end [ 0.133 -0.041  0.156]
          79 +step 295 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 39} tool [ 0.133 -0.041  0.156] end [ 0.138 -0.031  0.149]
          80 +step 300 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 40} tool [ 0.138 -0.031  0.149] end [0.133 0.006 0.157]
          81 +step 307 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 41} tool [0.133 0.006 0.157] end [0.137 0.013 0.149]
          82 +step 312 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 42} tool [0.137 0.013 0.149] end [ 0.147 -0.022  0.152]
          83 +ABORT step 317 tool [ 0.119 -0.001  0.182] q [ 1.253 -0.469 -3.863 -2.585 -0.387 -0.935  3.324] target [ 1.121 -0.415 -3.778 -2.592 -0.315 -0.904  3.556] tgt tool [ 0.113 -0.006  0.182]
          84 +step 319 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 43} tool [ 0.119 -0.001  0.25 ] end [0.146 0.021 0.151]
          85 +ABORT step 320 tool [ 0.119 -0.001  0.25 ] q [ 1.178 -0.594 -3.658 -2.395 -0.303 -1.27   3.33 ] target [ 0.883 -0.578 -3.615 -2.402 -0.263 -1.276  3.697] tgt tool [0.106 0.023 0.25 ]
          86 +step 321 task obstruction3 grasp 0.0 plan 15 fails {'obstruction3': 44} tool [ 0.119 -0.001  0.28 ] end [0.138 0.007 0.146]
          87 +step 329 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 45} tool [0.138 0.007 0.146] end [ 0.139 -0.021  0.146]
          88 +step 334 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 46} tool [ 0.139 -0.021  0.146] end [ 0.129 -0.007  0.161]
          89 +step 341 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 47} tool [ 0.129 -0.007  0.161] end [ 0.13  -0.038  0.161]
          90 +step 346 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 48} tool [ 0.13  -0.038  0.161] end [0.146 0.014 0.148]
          91 +ABORT step 351 tool [0.118 0.001 0.182] q [ 1.198 -0.469 -3.838 -2.59  -0.378 -0.926  3.475] target [ 1.01  -0.426 -3.834 -2.583 -0.337 -0.922  3.713] tgt tool [0.113 0.017 0.182]
          92 +step 353 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 49} tool [0.118 0.001 0.25 ] end [0.146 0.011 0.155]
          93 +ABORT step 354 tool [0.118 0.001 0.25 ] q [ 1.128 -0.595 -3.639 -2.4   -0.295 -1.262  3.482] target [ 0.912 -0.596 -3.583 -2.411 -0.252 -1.289  3.752] tgt tool [0.1   0.017 0.25 ]
          94 +step 355 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 50} tool [0.118 0.001 0.28 ] end [ 0.148 -0.012  0.149]
          95 +ABORT step 356 tool [0.118 0.001 0.28 ] q [ 1.113 -0.618 -3.59  -2.312 -0.27  -1.377  3.478] target [ 0.923 -0.545 -3.524 -2.31  -0.2   -1.348  3.778] tgt tool [ 0.113 -0.005  0.28 ]
          96 +step 357 task obstruction3 grasp 0.0 plan 16 fails {'obstruction3': 51} tool [0.118 0.001 0.31 ] end [ 0.148 -0.017  0.156]
          97 +ABORT step 358 tool [0.118 0.001 0.31 ] q [ 1.102 -0.628 -3.552 -2.223 -0.249 -1.48   3.472] target [ 0.89  -0.59  -3.445 -2.235 -0.168 -1.476  3.793] tgt tool [ 0.1   -0.005  0.31 ]
          98 +step 359 task obstruction3 grasp 0.0 plan 20 fails {'obstruction3': 52} tool [0.118 0.001 0.34 ] end [ 0.123 -0.037  0.166]
          99 +step 369 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 53} tool [ 0.123 -0.037  0.166] end [ 0.141 -0.01   0.143]
         100 +step 374 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 54} tool [ 0.141 -0.01   0.143] end [ 0.125 -0.019  0.166]
         101 +ABORT step 378 tool [0.102 0.005 0.182] q [ 1.642 -0.736 -3.826 -2.603 -0.477 -1.183  2.862] target [ 1.593 -0.765 -3.732 -2.628 -0.423 -1.218  2.868] tgt tool [0.085 0.013 0.182]
         102 +step 380 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 55} tool [0.102 0.005 0.25 ] end [0.14  0.004 0.143]
         103 +step 385 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 56} tool [0.14  0.004 0.143] end [0.146 0.008 0.145]
         104 +ABORT step 392 tool [0.122 0.011 0.182] q [ 1.205 -0.451 -3.917 -2.569 -0.389 -0.938  3.621] target [ 1.104 -0.419 -3.878 -2.573 -0.351 -0.918  3.773] tgt tool [0.119 0.012 0.182]
         105 +step 394 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 57} tool [0.122 0.011 0.25 ] end [ 0.145 -0.015  0.159]
         106 +ABORT step 395 tool [0.122 0.011 0.25 ] q [ 1.12  -0.578 -3.698 -2.383 -0.309 -1.273  3.634] target [ 0.98  -0.595 -3.527 -2.421 -0.221 -1.287  3.86 ] tgt tool [0.094 0.001 0.25 ]
         107 +step 396 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 58} tool [0.122 0.011 0.28 ] end [0.145 0.    0.159]
         108 +ABORT step 397 tool [0.122 0.011 0.28 ] q [ 1.103 -0.601 -3.644 -2.297 -0.283 -1.388  3.631] target [ 0.957 -0.64  -3.514 -2.331 -0.222 -1.421  3.829] tgt tool [0.094 0.012 0.28 ]
         109 +step 398 task obstruction3 grasp 0.0 plan 15 fails {'obstruction3': 59} tool [0.122 0.011 0.31 ] end [ 0.147 -0.004  0.145]
         110 +ABORT step 400 tool [0.119 0.001 0.31 ] q [ 0.985 -0.569 -3.547 -2.213 -0.215 -1.463  3.803] target [ 1.005 -0.527 -3.628 -2.383 -0.251 -1.244  3.8  ] tgt tool [0.119 0.001 0.252]
         111 +step 401 task obstruction3 grasp 0.0 plan 17 fails {'obstruction3': 60} tool [0.119 0.001 0.34 ] end [0.146 0.004 0.142]
         112 +ABORT step 403 tool [0.125 0.006 0.34 ] q [ 0.986 -0.569 -3.553 -2.114 -0.217 -1.559  3.777] target [ 1.001 -0.549 -3.62  -2.288 -0.249 -1.358  3.78 ] tgt tool [0.125 0.006 0.282]
         113 +step 404 task obstruction3 grasp 0.0 plan 19 fails {'obstruction3': 61} tool [0.125 0.006 0.37 ] end [ 0.143 -0.01   0.163]
         114 +ABORT step 406 tool [0.087 0.006 0.37 ] q [ 0.939 -0.646 -3.409 -2.058 -0.161 -1.71   3.843] target [ 0.951 -0.652 -3.459 -2.287 -0.191 -1.483  3.854] tgt tool [0.087 0.006 0.297]
         115 +step 407 task obstruction3 grasp 0.0 plan 25 fails {'obstruction3': 62} tool [0.087 0.006 0.4  ] end [ 0.124 -0.013  0.158]
         116 +step 418 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 63} tool [ 0.124 -0.013  0.158] end [ 0.145 -0.022  0.148]
         117 +ABORT step 423 tool [ 0.117 -0.011  0.182] q [ 1.487 -0.543 -3.893 -2.585 -0.436 -0.997  3.652] target [ 1.275 -0.438 -3.838 -2.585 -0.346 -0.931  3.981] tgt tool [ 0.113 -0.01   0.182]
         118 +step 425 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 64} tool [ 0.117 -0.011  0.25 ] end [0.143 0.017 0.148]
         119 +ABORT step 426 tool [ 0.117 -0.011  0.25 ] q [ 1.4   -0.646 -3.682 -2.396 -0.331 -1.313  3.632] target [ 1.141 -0.642 -3.695 -2.392 -0.33  -1.329  3.905] tgt tool [0.113 0.023 0.25 ]
         120 +step 427 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 65} tool [ 0.117 -0.011  0.28 ] end [ 0.144 -0.028  0.155]
         121 +ABORT step 428 tool [ 0.117 -0.011  0.28 ] q [ 1.382 -0.663 -3.629 -2.309 -0.301 -1.423  3.624] target [ 1.123 -0.61  -3.523 -2.324 -0.218 -1.397  3.985] tgt tool [ 0.1  -0.01  0.28]
         122 +step 429 task obstruction3 grasp 0.0 plan 16 fails {'obstruction3': 66} tool [ 0.117 -0.011  0.31 ] end [0.142 0.013 0.155]
         123 +ABORT step 430 tool [ 0.117 -0.011  0.31 ] q [ 1.37  -0.668 -3.589 -2.219 -0.278 -1.523  3.616] target [ 1.093 -0.692 -3.552 -2.23  -0.257 -1.562  3.914] tgt tool [0.1   0.023 0.31 ]
         124 +step 431 task obstruction3 grasp 0.0 plan 19 fails {'obstruction3': 67} tool [ 0.117 -0.011  0.34 ] end [ 0.119 -0.05   0.162]
         125 +step 439 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 68} tool [ 0.119 -0.05   0.162] end [ 0.135 -0.029  0.146]
         126 +step 444 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 69} tool [ 0.135 -0.029  0.146] end [ 0.121 -0.003  0.162]
         127 +step 450 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 70} tool [ 0.121 -0.003  0.162] end [0.135 0.014 0.146]
         128 +step 455 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 71} tool [0.135 0.014 0.146] end [0.143 0.005 0.158]
         129 +ABORT step 460 tool [0.109 0.016 0.182] q [ 1.381 -0.628 -3.874 -2.593 -0.465 -1.076  3.534] target [ 1.109 -0.542 -3.768 -2.614 -0.365 -1.012  3.896] tgt tool [0.094 0.017 0.182]
         130 +step 462 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 72} tool [0.109 0.016 0.25 ] end [ 0.147 -0.011  0.145]
         131 +ABORT step 463 tool [0.109 0.016 0.25 ] q [ 1.291 -0.706 -3.673 -2.402 -0.346 -1.371  3.492] target [ 1.078 -0.531 -3.64  -2.388 -0.259 -1.241  3.866] tgt tool [ 0.119 -0.005  0.25 ]
         132 +step 464 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 73} tool [0.109 0.016 0.28 ] end [0.145 0.014 0.145]
         133 +ABORT step 465 tool [0.109 0.016 0.28 ] q [ 1.272 -0.717 -3.621 -2.314 -0.314 -1.475  3.48 ] target [ 1.037 -0.6   -3.637 -2.299 -0.276 -1.392  3.81 ] tgt tool [0.119 0.017 0.28 ]
         134 +step 466 task obstruction3 grasp 0.0 plan 16 fails {'obstruction3': 74} tool [0.109 0.016 0.31 ] end [ 0.145 -0.022  0.159]
         135 +ABORT step 467 tool [0.109 0.016 0.31 ] q [ 1.26  -0.717 -3.582 -2.225 -0.289 -1.57   3.469] target [ 0.975 -0.621 -3.447 -2.241 -0.177 -1.5    3.878] tgt tool [ 0.094 -0.005  0.31 ]
         136 +step 468 task obstruction3 grasp 0.0 plan 19 fails {'obstruction3': 75} tool [0.109 0.016 0.34 ] end [ 0.119 -0.047  0.166]
         137 +step 477 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 76} tool [ 0.119 -0.047  0.166] end [ 0.139 -0.017  0.143]
         138 +step 482 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 77} tool [ 0.139 -0.017  0.143] end [ 0.122 -0.013  0.166]
         139 +ABORT step 486 tool [0.103 0.007 0.182] q [ 1.717 -0.79  -3.816 -2.602 -0.489 -1.237  2.949] target [ 1.654 -0.831 -3.718 -2.627 -0.433 -1.285  2.942] tgt tool [0.085 0.019 0.182]
         140 +step 488 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 78} tool [0.103 0.007 0.25 ] end [0.139 0.011 0.143]
         141 +step 493 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 79} tool [0.139 0.011 0.143] end [ 0.145 -0.004  0.142]
         142 +ABORT step 501 tool [ 0.127 -0.     0.155] q [ 1.348 -0.304 -4.123 -2.629 -0.385 -0.719  3.826] target [ 1.509 -0.2   -4.367 -2.64  -0.359 -0.563  3.74 ] tgt tool [ 0.145 -0.004  0.142]
         143 +step 504 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 80} tool [ 0.128 -0.     0.22 ] end [0.145 0.008 0.142]
         144 +ABORT step 508 tool [0.126 0.011 0.154] q [ 1.348 -0.348 -4.152 -2.63  -0.436 -0.75   3.836] target [ 1.5   -0.259 -4.378 -2.64  -0.443 -0.599  3.79 ] tgt tool [0.145 0.008 0.142]
         145 +step 511 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 81} tool [0.126 0.011 0.25 ] end [ 0.141 -0.021  0.163]
         146 +ABORT step 512 tool [0.126 0.011 0.25 ] q [ 1.151 -0.574 -3.729 -2.375 -0.319 -1.274  3.879] target [ 1.094 -0.64  -3.528 -2.428 -0.235 -1.324  3.978] tgt tool [0.087 0.001 0.25 ]
         147 +step 513 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 82} tool [0.126 0.011 0.28 ] end [ 0.141 -0.006  0.163]
         148 +ABORT step 514 tool [0.126 0.011 0.28 ] q [ 1.132 -0.597 -3.672 -2.29  -0.293 -1.389  3.876] target [ 1.071 -0.685 -3.511 -2.337 -0.232 -1.459  3.948] tgt tool [0.087 0.012 0.28 ]
         149 +step 515 task obstruction3 grasp 0.0 plan 19 fails {'obstruction3': 83} tool [0.126 0.011 0.31 ] end [ 0.123 -0.021  0.158]
         150 +step 524 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 84} tool [ 0.123 -0.021  0.158] end [ 0.123 -0.006  0.158]
         151 +step 528 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 85} tool [ 0.123 -0.006  0.158] end [ 0.12  -0.018  0.162]
         152 +step 532 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 86} tool [ 0.12  -0.018  0.162] end [ 0.128 -0.008  0.154]
         153 +step 536 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 87} tool [ 0.128 -0.008  0.154] end [ 0.142 -0.032  0.159]
         154 +ABORT step 540 tool [ 0.114 -0.009  0.182] q [ 1.603 -0.634 -3.884 -2.591 -0.477 -1.071  3.426] target [ 1.343 -0.517 -3.78  -2.609 -0.364 -0.983  3.808] tgt tool [ 0.101 -0.01   0.182]
         155 +step 542 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 88} tool [ 0.114 -0.009  0.25 ] end [0.141 0.012 0.158]
         156 +ABORT step 544 tool [0.106 0.003 0.25 ] q [ 1.336 -0.691 -3.645 -2.408 -0.324 -1.355  3.58 ] target [ 1.058 -0.671 -3.603 -2.416 -0.288 -1.353  3.892] tgt tool [0.094 0.023 0.25 ]
         157 +step 545 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 89} tool [0.106 0.003 0.28 ] end [ 0.146 -0.017  0.145]
         158 +ABORT step 546 tool [0.106 0.003 0.28 ] q [ 1.319 -0.703 -3.595 -2.32  -0.294 -1.462  3.57 ] target [ 1.103 -0.556 -3.59  -2.301 -0.237 -1.358  3.907] tgt tool [ 0.119 -0.01   0.28 ]
         159 +step 547 task obstruction3 grasp 0.0 plan 16 fails {'obstruction3': 90} tool [0.106 0.003 0.31 ] end [0.144 0.019 0.145]
         160 +ABORT step 550 tool [0.119 0.023 0.31 ] q [ 1.075 -0.637 -3.617 -2.209 -0.276 -1.517  3.839] target [ 1.105 -0.61  -3.711 -2.378 -0.326 -1.31   3.85 ] tgt tool [0.119 0.023 0.252]
         161 +step 551 task obstruction3 grasp 0.0 plan 17 fails {'obstruction3': 91} tool [0.119 0.023 0.34 ] end [0.144 0.014 0.142]
         162 +ABORT step 558 tool [0.136 0.015 0.145] q [ 1.413 -0.292 -4.305 -2.64  -0.448 -0.651  3.771] target [ 1.468 -0.263 -4.385 -2.64  -0.45  -0.601  3.756] tgt tool [0.144 0.014 0.142]
         163 +step 562 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 92} tool [0.136 0.015 0.25 ] end [0.141 0.003 0.162]
         164 +ABORT step 563 tool [0.136 0.015 0.25 ] q [ 1.121 -0.56  -3.755 -2.367 -0.332 -1.247  3.833] target [ 1.044 -0.672 -3.561 -2.425 -0.263 -1.352  3.909] tgt tool [0.087 0.017 0.25 ]
         165 +step 564 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 93} tool [0.136 0.015 0.28 ] end [ 0.146 -0.009  0.142]
         166 +ABORT step 565 tool [0.136 0.015 0.28 ] q [ 1.102 -0.584 -3.696 -2.282 -0.305 -1.363  3.831] target [ 1.103 -0.552 -3.626 -2.292 -0.253 -1.355  3.879] tgt tool [ 0.125 -0.005  0.28 ]
         167 +step 566 task obstruction3 grasp 0.0 plan 16 fails {'obstruction3': 94} tool [0.136 0.015 0.31 ] end [ 0.141 -0.027  0.163]
         168 +ABORT step 567 tool [0.136 0.015 0.31 ] q [ 1.088 -0.596 -3.651 -2.195 -0.283 -1.468  3.827] target [ 1.032 -0.647 -3.439 -2.247 -0.178 -1.521  3.943] tgt tool [ 0.087 -0.005  0.31 ]
         169 +step 568 task obstruction3 grasp 0.0 plan 17 fails {'obstruction3': 95} tool [0.136 0.015 0.34 ] end [ 0.137 -0.002  0.155]
         170 +ABORT step 570 tool [0.106 0.006 0.34 ] q [ 1.046 -0.63  -3.506 -2.135 -0.212 -1.604  3.881] target [ 1.066 -0.612 -3.585 -2.348 -0.254 -1.366  3.89 ] tgt tool [0.106 0.006 0.269]
         171 +step 571 task obstruction3 grasp 0.0 plan 23 fails {'obstruction3': 96} tool [0.106 0.006 0.37 ] end [ 0.116 -0.055  0.166]
         172 +step 582 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 97} tool [ 0.116 -0.055  0.166] end [ 0.138 -0.023  0.143]
         173 +step 587 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 98} tool [ 0.138 -0.023  0.143] end [ 0.119 -0.005  0.166]
         174 +ABORT step 591 tool [0.104 0.008 0.182] q [ 1.755 -0.818 -3.815 -2.6   -0.497 -1.265  2.99 ] target [ 1.674 -0.877 -3.706 -2.625 -0.437 -1.334  2.97 ] tgt tool [0.085 0.025 0.182]
         175 +step 593 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 99} tool [0.104 0.008 0.25 ] end [0.137 0.017 0.143]
         176 +step 597 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 100} tool [0.137 0.017 0.143] end [0.124 0.002 0.157]
         177 +step 601 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 101} tool [0.124 0.002 0.157] end [ 0.125 -0.026  0.157]
         178 +step 606 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 102} tool [ 0.125 -0.026  0.157] end [ 0.123 -0.024  0.161]
         179 +step 611 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 103} tool [ 0.123 -0.024  0.161] end [ 0.129 -0.015  0.153]
         180 +step 616 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 104} tool [ 0.129 -0.015  0.153] end [ 0.123 -0.009  0.161]
         181 +step 620 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 105} tool [ 0.123 -0.009  0.161] end [ 0.13  -0.     0.153]
         182 +step 624 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 106} tool [ 0.13  -0.     0.153] end [ 0.135 -0.001  0.149]
         183 +step 630 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 107} tool [ 0.135 -0.001  0.149] end [ 0.128 -0.015  0.164]
         184 +step 637 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 108} tool [ 0.128 -0.015  0.164] end [ 0.148 -0.014  0.143]
         185 +ABORT step 643 tool [ 0.126 -0.011  0.182] q [ 1.003 -0.326 -3.755 -2.572 -0.257 -0.841  3.452] target [ 0.913 -0.294 -3.721 -2.565 -0.215 -0.836  3.641] tgt tool [ 0.125 -0.01   0.182]
         186 +step 646 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 109} tool [ 0.128 -0.012  0.218] end [0.144 0.024 0.141]
         187 +ABORT step 650 tool [0.126 0.022 0.155] q [ 0.965 -0.221 -4.03  -2.627 -0.273 -0.673  3.445] target [ 1.087 -0.084 -4.261 -2.64  -0.155 -0.51   3.246] tgt tool [0.144 0.024 0.141]
         188 +step 653 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 110} tool [0.126 0.022 0.25 ] end [ 0.144 -0.03   0.163]
         189 +ABORT step 654 tool [0.126 0.022 0.25 ] q [ 0.84  -0.498 -3.667 -2.375 -0.256 -1.217  3.6  ] target [ 0.809 -0.559 -3.414 -2.43  -0.151 -1.257  3.764] tgt tool [ 0.087 -0.01   0.25 ]
         190 +step 655 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 111} tool [0.126 0.022 0.28 ] end [0.143 0.018 0.161]
         191 +ABORT step 656 tool [0.126 0.022 0.28 ] q [ 0.826 -0.529 -3.617 -2.289 -0.237 -1.338  3.605] target [ 0.781 -0.64  -3.488 -2.335 -0.207 -1.421  3.672] tgt tool [0.087 0.023 0.28 ]
         192 +step 657 task obstruction3 grasp 0.0 plan 15 fails {'obstruction3': 112} tool [0.126 0.022 0.31 ] end [0.139 0.008 0.155]
         193 +ABORT step 658 tool [0.126 0.022 0.31 ] q [ 0.817 -0.546 -3.578 -2.201 -0.221 -1.446  3.606] target [ 0.795 -0.583 -3.484 -2.227 -0.187 -1.472  3.666] tgt tool [0.106 0.012 0.31 ]
         194 +step 659 task obstruction3 grasp 0.0 plan 17 fails {'obstruction3': 113} tool [0.126 0.022 0.34 ] end [ 0.14  -0.005  0.156]
         195 +ABORT step 661 tool [0.106 0.001 0.34 ] q [ 0.788 -0.571 -3.429 -2.137 -0.154 -1.558  3.688] target [ 0.801 -0.541 -3.49  -2.35  -0.183 -1.309  3.688] tgt tool [0.106 0.001 0.269]
         196 +step 662 task obstruction3 grasp 0.0 plan 19 fails {'obstruction3': 114} tool [0.106 0.001 0.37 ] end [0.14  0.003 0.153]
         197 +ABORT step 664 tool [0.113 0.006 0.37 ] q [ 0.792 -0.561 -3.445 -2.035 -0.16  -1.646  3.663] target [ 0.802 -0.553 -3.497 -2.255 -0.186 -1.414  3.667] tgt tool [0.113 0.006 0.299]
         198 +step 665 task obstruction3 grasp 0.0 plan 21 fails {'obstruction3': 115} tool [0.113 0.006 0.4  ] end [ 0.138 -0.002  0.159]
         199 +ABORT step 667 tool [0.1   0.006 0.4  ] q [ 0.779 -0.58  -3.397 -1.949 -0.141 -1.755  3.679] target [ 0.785 -0.595 -3.434 -2.178 -0.162 -1.538  3.688] tgt tool [0.1   0.006 0.328]
         200 +step 668 task obstruction3 grasp 0.0 plan 27 fails {'obstruction3': 116} tool [0.1   0.006 0.43 ] end [ 0.13  -0.031  0.156]
         201 +step 680 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 117} tool [ 0.13  -0.031  0.156] end [0.128 0.013 0.156]
         202 +step 686 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 118} tool [0.128 0.013 0.156] end [0.127 0.002 0.16 ]
         203 +step 691 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 119} tool [0.127 0.002 0.16 ] end [0.132 0.009 0.152]
         204 +step 696 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 120} tool [0.132 0.009 0.152] end [ 0.129 -0.027  0.16 ]
         205 +step 701 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 121} tool [ 0.129 -0.027  0.16 ] end [ 0.133 -0.019  0.152]
         206 +step 706 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 122} tool [ 0.133 -0.019  0.152] end [ 0.145 -0.005  0.152]
         207 +step 713 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 123} tool [ 0.145 -0.005  0.152] end [ 0.13  -0.018  0.155]
         208 +step 723 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 124} tool [ 0.13  -0.018  0.155] end [ 0.135 -0.008  0.149]
         209 +step 730 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 125} tool [ 0.135 -0.008  0.149] end [0.134 0.006 0.149]
         210 +step 736 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 126} tool [0.134 0.006 0.149] end [ 0.127 -0.024  0.164]
         211 +step 742 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 127} tool [ 0.127 -0.024  0.164] end [ 0.127 -0.008  0.164]
         212 +step 747 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 128} tool [ 0.127 -0.008  0.164] end [ 0.14  -0.013  0.156]
         213 +ABORT step 752 tool [ 0.114 -0.006  0.182] q [ 1.12  -0.436 -3.763 -2.6   -0.329 -0.899  3.303] target [ 0.895 -0.371 -3.66  -2.6   -0.235 -0.882  3.699] tgt tool [ 0.106 -0.005  0.182]
         214 +step 754 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 129} tool [ 0.114 -0.006  0.25 ] end [0.138 0.015 0.155]
         215 +ABORT step 755 tool [ 0.114 -0.006  0.25 ] q [ 1.065 -0.572 -3.585 -2.407 -0.261 -1.241  3.321] target [ 0.809 -0.549 -3.575 -2.404 -0.233 -1.252  3.649] tgt tool [0.106 0.017 0.25 ]
         216 +step 756 task obstruction3 grasp 0.0 plan 15 fails {'obstruction3': 130} tool [ 0.114 -0.006  0.28 ] end [ 0.12  -0.022  0.168]
         217 +ABORT step 761 tool [0.085 0.006 0.223] q [ 1.488 -0.757 -3.62  -2.507 -0.33  -1.344  2.775] target [ 1.562 -0.682 -3.785 -2.64  -0.44  -1.095  2.817] tgt tool [ 0.093 -0.001  0.176]
         218 +step 762 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 131} tool [0.085 0.006 0.253] end [0.135 0.002 0.146]
         219 +step 768 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 132} tool [0.135 0.002 0.146] end [ 0.144 -0.009  0.153]
         220 +step 776 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 133} tool [ 0.144 -0.009  0.153] end [ 0.144 -0.005  0.151]
         221 +step 782 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 134} tool [ 0.144 -0.005  0.151] end [ 0.128 -0.018  0.156]
         222 +step 792 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 135} tool [ 0.128 -0.018  0.156] end [ 0.13  -0.019  0.154]
         223 +step 797 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 136} tool [ 0.13  -0.019  0.154] end [ 0.14  -0.004  0.153]
         224 +ABORT step 804 tool [ 0.118 -0.005  0.182] q [ 1.219 -0.448 -3.834 -2.588 -0.362 -0.918  3.286] target [ 1.089 -0.406 -3.79  -2.588 -0.315 -0.897  3.489] tgt tool [ 0.115 -0.002  0.182]
         225 +step 806 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 137} tool [ 0.118 -0.005  0.25 ] end [0.139 0.009 0.152]
         226 +ABORT step 807 tool [ 0.118 -0.005  0.25 ] q [ 1.151 -0.58  -3.637 -2.398 -0.285 -1.257  3.301] target [ 0.868 -0.532 -3.596 -2.396 -0.237 -1.24   3.689] tgt tool [0.113 0.012 0.25 ]
         227 +step 808 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 138} tool [ 0.118 -0.005  0.28 ] end [ 0.139 -0.008  0.159]
         228 +ABORT step 809 tool [ 0.118 -0.005  0.28 ] q [ 1.137 -0.604 -3.587 -2.311 -0.261 -1.373  3.298] target [ 0.985 -0.585 -3.528 -2.319 -0.219 -1.368  3.516] tgt tool [ 0.109 -0.002  0.28 ]
         229 +step 810 task obstruction3 grasp 0.0 plan 16 fails {'obstruction3': 139} tool [ 0.118 -0.005  0.31 ] end [0.138 0.006 0.159]
         230 +ABORT step 811 tool [ 0.118 -0.005  0.31 ] q [ 1.127 -0.615 -3.55  -2.221 -0.242 -1.478  3.294] target [ 0.972 -0.608 -3.508 -2.228 -0.212 -1.482  3.5  ] tgt tool [0.109 0.003 0.31 ]
         231 +step 812 task obstruction3 grasp 0.0 plan 18 fails {'obstruction3': 140} tool [ 0.118 -0.005  0.34 ] end [ 0.138 -0.003  0.162]
         232 +ABORT step 814 tool [0.107 0.    0.34 ] q [ 0.974 -0.613 -3.47  -2.139 -0.192 -1.579  3.487] target [ 0.805 -0.615 -3.415 -2.148 -0.156 -1.59   3.719] tgt tool [0.094 0.006 0.34 ]
         233 +step 815 task obstruction3 grasp 0.0 plan 20 fails {'obstruction3': 141} tool [0.107 0.    0.37 ] end [0.139 0.004 0.15 ]
         234 +ABORT step 818 tool [0.119 0.006 0.309] q [ 0.839 -0.546 -3.519 -2.218 -0.194 -1.441  3.68 ] target [ 0.86  -0.487 -3.608 -2.411 -0.23  -1.182  3.671] tgt tool [0.119 0.006 0.242]
         235 +step 819 task obstruction3 grasp 0.0 plan 19 fails {'obstruction3': 142} tool [0.119 0.006 0.339] end [ 0.144 -0.01   0.153]
         236 +step 828 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 143} tool [ 0.144 -0.01   0.153] end [ 0.145 -0.002  0.151]
         237 +step 834 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 144} tool [ 0.145 -0.002  0.151] end [ 0.128 -0.017  0.157]
         238 +step 844 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 145} tool [ 0.128 -0.017  0.157] end [ 0.131 -0.019  0.154]
         239 +step 849 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 146} tool [ 0.131 -0.019  0.154] end [ 0.145 -0.011  0.154]
         240 +step 858 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 147} tool [ 0.145 -0.011  0.154] end [0.145 0.    0.15 ]
         241 +step 864 task obstruction3 grasp 0.0 plan 14 fails {'obstruction3': 148} tool [0.145 0.    0.15 ] end [ 0.128 -0.016  0.157]
         242 +step 874 task obstruction3 grasp 0.0 plan 9 fails {'obstruction3': 149} tool [ 0.128 -0.016  0.157] end [ 0.133 -0.019  0.153]
         243 +step 879 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 150} tool [ 0.133 -0.019  0.153] end [ 0.146 -0.008  0.15 ]
         244 +step 888 task obstruction3 grasp 0.0 plan 11 fails {'obstruction3': 151} tool [ 0.146 -0.008  0.15 ] end [ 0.145 -0.001  0.154]
         245 +step 894 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 152} tool [ 0.145 -0.001  0.154] end [ 0.129 -0.025  0.157]
         246 +step 903 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 153} tool [ 0.129 -0.025  0.157] end [ 0.133 -0.01   0.152]
         247 +step 908 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 154} tool [ 0.133 -0.01   0.152] end [ 0.13  -0.033  0.159]
         248 +step 915 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 155} tool [ 0.13  -0.033  0.159] end [ 0.133 -0.025  0.152]
         249 +step 920 task obstruction3 grasp 0.0 plan 10 fails {'obstruction3': 156} tool [ 0.133 -0.025  0.152] end [0.128 0.012 0.159]
         250 +step 927 task obstruction3 grasp 0.0 plan 8 fails {'obstruction3': 157} tool [0.128 0.012 0.159] end [0.132 0.017 0.152]
         251 +step 932 task obstruction3 grasp 0.0 plan 13 fails {'obstruction3': 158} tool [0.132 0.017 0.152] end [ 0.14  -0.019  0.156]
         252 +ABORT step 937 tool [0.117 0.002 0.182] q [ 1.133 -0.431 -3.823 -2.586 -0.346 -0.911  3.191] target [ 0.995 -0.383 -3.722 -2.594 -0.273 -0.884  3.454] tgt tool [ 0.112 -0.005  0.182]
         253 +step 939 task obstruction3 grasp 0.0 plan 12 fails {'obstruction3': 159} tool [0.117 0.002 0.25 ] end [0.137 0.022 0.154]
         254 +ABORT step 940 tool [0.117 0.002 0.25 ] q [ 1.068 -0.567 -3.629 -2.397 -0.276 -1.252  3.212] target [ 0.772 -0.548 -3.582 -2.402 -0.236 -1.252  3.606] tgt tool [0.106 0.023 0.25 ]
         255 +step 941 task obstruction3 grasp 0.0 plan 15 fails {'obstruction3': 160} tool [0.117 0.002 0.28 ] end [0.133 0.012 0.149]
         256 +step 949 task obstruction3 grasp 1.0 plan 18 fails {'obstruction3': 160} tool [0.133 0.012 0.149] end [ 0.294 -0.1    0.14 ]
         257 +step 959 task target_block grasp 0.0 plan 16 fails {'obstruction3': 160} tool [ 0.294 -0.1    0.14 ] end [ 0.47  -0.266  0.131]
         258 +step 967 task target_block grasp 1.0 plan 25 fails {'obstruction3': 160} tool [ 0.47  -0.266  0.131] end [0.143 0.038 0.143]
         259 +SOLVED 980
         260 +time 117.86067271232605
diff --git a/reach.py b/reach.py
new file mode 100644
index 0000000..9727ab2
--- /dev/null
+++ b/reach.py
@@ -0,0 +1,32 @@
           1 +import numpy as np, kin
           2 +from env_client import make_env
           3 +from common import *
           4 +env=make_env(); obs,_=env.reset(seed=312, options={'object_count':15}); b=getbase(obs); q0=getq(obs)
           5 +print('base', b)
           6 +JL=np.array([np.inf,2.41,np.inf,2.66,np.inf,2.23,np.inf])-0.02
           7 +mount=b[:2]+0.12*np.array([np.cos(b[2]),np.sin(b[2])]); print('mount', mount)
           8 +for ang in [0, 0.8, 1.57, -1.57, 2.5]:
           9 +  res=[]
          10 +  for r in np.arange(0.0,0.2,0.01):
          11 +    p=np.array([mount[0]+r*np.cos(ang), mount[1]+r*np.sin(ang), 0.15])
          12 +    ok=False
          13 +    for yaw in [0,np.pi/2,np.pi/4,-np.pi/4]:
          14 +      for t in range(4):
          15 +        qs=q0+np.random.uniform(-1,1,7)*(t>0)
          16 +        q,o=kin.ik(b,qs,p,kin.topdown_R(yaw),iters=200,tol=1e-5,lim=JL)
          17 +        if o: ok=True;break
          18 +      if ok: break
          19 +    res.append(ok)
          20 +  print(ang, ''.join('1' if x else '0' for x in res))
          21 +print('per yaw, angle 0 and 0.8, z .14')
          22 +for ang in [0,0.8,-0.8]:
          23 + for yaw in np.arange(0,np.pi,np.pi/8):
          24 +  res=[]
          25 +  for r in np.arange(0.10,0.17,0.005):
          26 +    p=np.array([r*np.cos(ang), r*np.sin(ang), 0.14]); ok=False
          27 +    for t in range(4):
          28 +        qs=q0+np.random.uniform(-1,1,7)*(t>0)
          29 +        q,o=kin.ik(b,qs,p,kin.topdown_R(yaw),iters=200,tol=1e-5,lim=JL)
          30 +        if o: ok=True;break
          31 +    res.append(ok)
          32 +  print(ang, round(yaw,2), ''.join('1' if x else '0' for x in res))
```

</details>

<a id="C025"></a>
### C025 · Promote: base backoff for near-mount objects, faster IK; 15-obs 16/16, default 100/100

Commit `c09ea7fb670ff583bc80e3ca01e1e405f713935f`; parents: 2b3712c64154d0e000cfc91132a1598e4c141417. Recorded author date: 2026-10-01T01:10:44+02:00.

File roles (automatic): policy, setup/other.

- [E1269](01_timeline.md#E1269): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_c09ea7f_approach.py) · [Exact all-file diff](evidence/diffs/C025_c09ea7f.diff)

[Previous saved controller snapshot](evidence/versions/C022_1fc8053_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1d2c701..0333d0c 100644
--- a/approach.py
+++ b/approach.py
@@ -119,7 +119,7 @@ class GeneratedApproach:
  119    119                  best = np.clip(q, -JLIM, JLIM)
  120    120          return best, False
  121    121  
  122        -    def _cart_path(self, q0, p_from, p_to, R, step=0.04, R_from=None):
         122 +    def _cart_path(self, q0, p_from, p_to, R, step=0.04, R_from=None, stop_on_fail=False):
  123    123          """IK waypoints along a straight line in tool position; orientation interpolated
  124    124          from R_from (default: R) to R."""
  125    125          p_from = np.asarray(p_from, float)
@@ -138,6 +138,8 @@ class GeneratedApproach:
  138    138              q, ok = self._ik(q, p, Ri)
  139    139              allok &= ok
  140    140              qs.append(q.copy())
         141 +            if stop_on_fail and not ok:
         142 +                return qs, q, False
  141    143          return qs, q, allok
  142    144  
  143    145      @staticmethod
@@ -326,10 +328,45 @@ class GeneratedApproach:
  326    328                  q = item[1]
  327    329          return c
  328    330  
         331 +    def _mount(self, base=None):
         332 +        b = self.base if base is None else base
         333 +        return np.array([b[0] + kin.MOUNT_X * np.cos(b[2]), b[1] + kin.MOUNT_X * np.sin(b[2])])
         334 +
         335 +    def _base_for(self, pts, rmin=0.165):
         336 +        m = self._mount()
         337 +        need = m[0]
         338 +        for p in pts:
         339 +            dy = p[1] - m[1]
         340 +            if np.hypot(p[0] - m[0], dy) < rmin - 0.005:
         341 +                need = min(need, p[0] - np.sqrt(max(rmin ** 2 - dy ** 2, 0.0)))
         342 +        if need >= m[0] - 1e-4:
         343 +            return None
         344 +        nb = np.array(self.base, float).copy()
         345 +        nb[0] -= (m[0] - need)
         346 +        return nb
         347 +
         348 +    def _plan_base_move(self, state, objs, held, nb):
         349 +        q = self._q(state)
         350 +        T = self._tool(q)
         351 +        p0 = T[:3, 3]
         352 +        zt = self._ztransit(objs, held)
         353 +        plan = []
         354 +        if p0[2] < zt:
         355 +            qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], zt]), T[:3, :3], step=0.015)
         356 +            plan = self._seg(qs)
         357 +        self.plan = plan + [('base', nb)]
         358 +
  329    359      def _plan_pick(self, state, name, cand):
  330    360          objs = self._parse(state)
  331    361          o = objs[name]
  332    362          _, yaw, gx, gy, _, _ = cand
         363 +        pts = [(gx, gy)]
         364 +        if name == 'target_block':
         365 +            pts.append(tuple(objs['target_region'].p[:2]))
         366 +        nb = self._base_for(pts)
         367 +        if nb is not None:
         368 +            self._plan_base_move(state, objs, None, nb)
         369 +            return
  333    370          zt = self._ztransit(objs, None)
  334    371          q0 = self._q(state)
  335    372          T = self._tool(q0)
@@ -338,20 +375,24 @@ class GeneratedApproach:
  338    375          above = np.array([gx, gy, max(zt, p0[2])])
  339    376          start = np.array([p0[0], p0[1], max(p0[2], zt)])
  340    377          best = None
  341        -        for y in [yaw, yaw + np.pi]:
         378 +        for y, sof in [(yaw, True), (yaw + np.pi, True), (yaw, False)]:
         379 +            if not sof and best is not None and best[0] < 100:
         380 +                break
  342    381              R = kin.topdown_R(y)
  343    382              q = q0
  344    383              plan = []
  345    384              if p0[2] < zt - 0.005:
  346    385                  qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.015)
  347    386                  plan += self._seg(qs)
  348        -            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.04, R_from=T[:3, :3])
  349        -            plan += self._seg(qs)
  350        -            qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.015)
         387 +            qs, q, ok1 = self._cart_path(q, start, above, R, step=0.04, R_from=T[:3, :3], stop_on_fail=sof)
  351    388              plan += self._seg(qs)
         389 +            ok2 = False
         390 +            if ok1 or not sof:
         391 +                qs, q, ok2 = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.015, stop_on_fail=sof)
         392 +                plan += self._seg(qs)
  352    393              plan += [('grip', -1.0), ('check', 'grasp')]
  353    394              c = self._plan_cost(q0, plan) + (0 if (ok1 and ok2) else 100)
  354        -            if best is None or c < best[0]:
         395 +            if best is None or c < best[0] or (not sof and best[0] >= 100):
  355    396                  best = (c, plan)
  356    397          self.plan = best[1]
  357    398  
@@ -363,6 +404,8 @@ class GeneratedApproach:
  363    404              for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
  364    405                  p = np.array([x, y])
  365    406                  cost = np.linalg.norm(p - cur) + 2.0 * max(0.0, 0.2 - x)
         407 +                if np.linalg.norm(p - self._mount()) < 0.17:
         408 +                    continue
  366    409                  if any(np.linalg.norm(p - bs) < 0.035 for bs in self.bad_spots):
  367    410                      continue
  368    411                  if best is not None and cost >= best[0]:
@@ -391,6 +434,10 @@ class GeneratedApproach:
  391    434      def _plan_place(self, state, name, xy, support_top, yaw_obj):
  392    435          objs = self._parse(state)
  393    436          o = objs[name]
         437 +        nb = self._base_for([xy])
         438 +        if nb is not None:
         439 +            self._plan_base_move(state, objs, name, nb)
         440 +            return
  394    441          q = self._q(state)
  395    442          T = self._tool(q)
  396    443          G = self._G(state)
@@ -549,6 +596,7 @@ class GeneratedApproach:
  549    596          self.steps += 1
  550    597          a = np.zeros(11, dtype=np.float32)
  551    598          q = self._q(state)
         599 +        self.base = self._base(state)
  552    600          for _ in range(20):
  553    601              if not self.plan:
  554    602                  self.aborting = False
@@ -582,6 +630,18 @@ class GeneratedApproach:
  582    630                  a[3:10] = np.clip(wrap(target - q), -0.2, 0.2)
  583    631                  return a
  584    632              self.aborting = False
         633 +            if kind == 'base':
         634 +                cur = np.array(self.base, float)
         635 +                d = np.array(val, float) - cur
         636 +                d[2] = wrap(d[2])
         637 +                lb = getattr(self, 'last_base', None)
         638 +                if np.max(np.abs(d)) < 1e-4 or (lb is not None and np.max(np.abs(cur - lb)) < 1e-7):
         639 +                    self.plan.pop(0)
         640 +                    self.last_base = None
         641 +                    continue
         642 +                self.last_base = cur.copy()
         643 +                a[0:3] = np.clip(d, -0.1, 0.1)
         644 +                return a
  585    645              if kind == 'grip':
  586    646                  self.plan.pop(0)
  587    647                  a[10] = val
diff --git a/r10v2.txt b/r10v2.txt
index bb2d5ea..4bc3b84 100644
--- a/r10v2.txt
+++ b/r10v2.txt
@@ -1,21 +1,21 @@
    1        -0 (True, 108, 10, 67.34670829772949)
    2        -1 (True, 118, 10, 77.54825496673584)
    3        -2 (True, 93, 10, 48.29496169090271)
    4        -3 (True, 79, 10, 56.12954092025757)
    5        -4 (True, 149, 10, 113.7067198753357)
    6        -5 (True, 107, 10, 60.19983792304993)
    7        -6 (True, 107, 10, 72.70078706741333)
    8        -7 (True, 136, 10, 96.57177400588989)
    9        -8 (True, 123, 10, 100.32531452178955)
   10        -9 (True, 87, 10, 70.76278758049011)
   11        -10 (True, 96, 10, 74.97967839241028)
   12        -11 (True, 95, 10, 79.21565651893616)
   13        -12 (True, 102, 10, 85.22674655914307)
   14        -13 (True, 133, 10, 96.41449117660522)
   15        -14 (True, 104, 10, 70.36861729621887)
   16        -15 (True, 162, 10, 78.65981841087341)
   17        -16 (True, 90, 10, 49.643895626068115)
   18        -17 (True, 76, 10, 32.62133312225342)
   19        -18 (True, 98, 10, 37.19398069381714)
   20        -19 (True, 82, 10, 29.940195083618164)
   21        -success 20 / 20 mean steps 107.25 max time 113.7067198753357
           1 +0 (True, 108, 10, 76.11171078681946)
           2 +1 (True, 118, 10, 85.90705800056458)
           3 +2 (True, 91, 10, 62.046934604644775)
           4 +3 (True, 79, 10, 35.50922656059265)
           5 +4 (True, 149, 10, 100.22274112701416)
           6 +5 (True, 107, 10, 70.38754415512085)
           7 +6 (True, 107, 10, 61.11952304840088)
           8 +7 (True, 136, 10, 105.7695894241333)
           9 +8 (True, 123, 10, 105.74410653114319)
          10 +9 (True, 87, 10, 72.33307552337646)
          11 +10 (True, 97, 10, 75.5835530757904)
          12 +11 (True, 95, 10, 79.95426869392395)
          13 +12 (True, 102, 10, 79.9322943687439)
          14 +13 (True, 133, 10, 94.3127703666687)
          15 +14 (True, 104, 10, 69.52751111984253)
          16 +15 (True, 125, 10, 71.98822593688965)
          17 +16 (True, 90, 10, 47.77280592918396)
          18 +17 (True, 76, 10, 32.8667995929718)
          19 +18 (True, 98, 10, 29.852894067764282)
          20 +19 (True, 82, 10, 23.913474321365356)
          21 +success 20 / 20 mean steps 105.35 max time 105.7695894241333
diff --git a/r15.txt b/r15.txt
index 8141ce4..cd001ba 100644
--- a/r15.txt
+++ b/r15.txt
@@ -1,17 +1,17 @@
    1        -300 (True, 137, 15, 92.13922357559204)
    2        -301 (True, 88, 15, 66.16345858573914)
    3        -302 (True, 126, 15, 80.64890599250793)
    4        -303 (True, 81, 15, 41.766000270843506)
    5        -304 (True, 117, 15, 70.7319004535675)
    6        -305 (True, 147, 15, 106.49297714233398)
    7        -306 (True, 104, 15, 59.91490602493286)
    8        -307 (True, 126, 15, 91.23219919204712)
    9        -308 (True, 110, 15, 83.98466873168945)
   10        -309 (True, 64, 15, 58.519328594207764)
   11        -310 (True, 130, 15, 77.43858695030212)
   12        -311 (True, 94, 15, 59.47879433631897)
   13        -312 (True, 339, 15, 92.68320178985596)
   14        -313 (True, 96, 15, 44.86985516548157)
   15        -314 (True, 115, 15, 49.378417015075684)
   16        -315 (True, 139, 15, 44.1101233959198)
   17        -success 16 / 16 mean steps 125.8125 max time 106.49297714233398
           1 +300 (True, 137, 15, 113.22774887084961)
           2 +301 (True, 88, 15, 66.91407752037048)
           3 +302 (True, 126, 15, 101.24943614006042)
           4 +303 (True, 81, 15, 41.54556679725647)
           5 +304 (True, 117, 15, 79.97198033332825)
           6 +305 (True, 147, 15, 122.9800431728363)
           7 +306 (True, 104, 15, 68.34753918647766)
           8 +307 (True, 126, 15, 98.85335063934326)
           9 +308 (True, 110, 15, 101.27514863014221)
          10 +309 (True, 64, 15, 73.3341555595398)
          11 +310 (True, 130, 15, 95.53463292121887)
          12 +311 (True, 94, 15, 76.26246476173401)
          13 +312 (True, 109, 15, 69.15419292449951)
          14 +313 (True, 96, 15, 66.03219485282898)
          15 +314 (True, 115, 15, 71.22132897377014)
          16 +315 (True, 139, 15, 52.36058473587036)
          17 +success 16 / 16 mean steps 111.4375 max time 122.9800431728363
diff --git a/r7v2.txt b/r7v2.txt
index 8357ef0..7c5ecef 100644
--- a/r7v2.txt
+++ b/r7v2.txt
@@ -1,30 +1,30 @@
    1        -0 (True, 87, 7, 60.72479176521301)
    2        -1 (True, 103, 7, 83.07648015022278)
    3        -2 (True, 71, 7, 47.04066872596741)
    4        -3 (True, 78, 7, 62.394036293029785)
    5        -4 (True, 132, 7, 90.8275887966156)
    6        -5 (True, 107, 7, 78.71391916275024)
    7        -6 (True, 106, 7, 67.2218987941742)
    8        -7 (True, 131, 7, 98.29449915885925)
    9        -8 (True, 85, 7, 64.31360483169556)
   10        -9 (True, 87, 7, 65.40352606773376)
   11        -10 (True, 69, 7, 47.742194175720215)
   12        -11 (True, 77, 7, 57.84087514877319)
   13        -12 (True, 107, 7, 83.83754515647888)
   14        -13 (True, 132, 7, 102.52496147155762)
   15        -14 (True, 61, 7, 48.202779054641724)
   16        -15 (True, 111, 7, 96.96697163581848)
   17        -16 (True, 62, 7, 49.24976086616516)
   18        -17 (True, 76, 7, 57.130834341049194)
   19        -18 (True, 84, 7, 65.64731335639954)
   20        -19 (True, 82, 7, 67.95730423927307)
   21        -20 (True, 90, 7, 68.10633182525635)
   22        -21 (True, 104, 7, 76.37464356422424)
   23        -22 (True, 76, 7, 53.72096347808838)
   24        -23 (True, 103, 7, 65.23439359664917)
   25        -24 (True, 78, 7, 47.02994132041931)
   26        -25 (True, 49, 7, 36.07643413543701)
   27        -26 (True, 69, 7, 40.60338997840881)
   28        -27 (True, 71, 7, 37.73515844345093)
   29        -28 (True, 100, 7, 28.717182159423828)
   30        -success 30 / 30 mean steps 88.36666666666666 max time 102.52496147155762
           1 +0 (True, 87, 7, 61.46162819862366)
           2 +1 (True, 103, 7, 63.78884148597717)
           3 +2 (True, 72, 7, 38.44877886772156)
           4 +3 (True, 78, 7, 40.85119438171387)
           5 +4 (True, 132, 7, 77.33553385734558)
           6 +5 (True, 107, 7, 75.06246185302734)
           7 +6 (True, 106, 7, 58.348899841308594)
           8 +7 (True, 131, 7, 79.53805947303772)
           9 +8 (True, 85, 7, 54.80790114402771)
          10 +9 (True, 87, 7, 60.40672326087952)
          11 +10 (True, 69, 7, 48.80706310272217)
          12 +11 (True, 77, 7, 52.43125581741333)
          13 +12 (True, 107, 7, 68.49261903762817)
          14 +13 (True, 132, 7, 93.29375982284546)
          15 +14 (True, 61, 7, 39.212146043777466)
          16 +15 (True, 109, 7, 75.54428434371948)
          17 +16 (True, 62, 7, 43.17334008216858)
          18 +17 (True, 76, 7, 46.304462909698486)
          19 +18 (True, 84, 7, 50.89159870147705)
          20 +19 (True, 82, 7, 60.554113149642944)
          21 +20 (True, 90, 7, 62.22769236564636)
          22 +21 (True, 104, 7, 64.87933349609375)
          23 +22 (True, 76, 7, 52.15495562553406)
          24 +23 (True, 103, 7, 60.814656496047974)
          25 +24 (True, 78, 7, 48.38524651527405)
          26 +25 (True, 49, 7, 34.37631297111511)
          27 +26 (True, 69, 7, 39.50170922279358)
          28 +27 (True, 71, 7, 32.75030779838562)
          29 +28 (True, 100, 7, 26.861525297164917)
          30 +success 30 / 30 mean steps 88.33333333333333 max time 93.29375982284546
diff --git a/rdv2.txt b/rdv2.txt
index 1eed73c..6d35f66 100644
--- a/rdv2.txt
+++ b/rdv2.txt
@@ -1,75 +1,75 @@
    1        -0 (True, 45, 2, 38.46183633804321)
    2        -1 (True, 38, 1, 25.16204023361206)
    3        -2 (True, 62, 2, 69.66143441200256)
    4        -3 (True, 32, 2, 25.111533164978027)
    5        -4 (True, 57, 2, 47.401066064834595)
    6        -5 (True, 48, 2, 38.81461954116821)
    7        -6 (True, 37, 1, 28.365293979644775)
    8        -7 (True, 39, 2, 23.942261695861816)
    9        -8 (True, 43, 2, 48.381948947906494)
   10        -9 (True, 25, 1, 25.134716987609863)
   11        -10 (True, 28, 2, 27.94377303123474)
   12        -12 (True, 31, 1, 34.262075424194336)
   13        -13 (True, 41, 2, 47.47896194458008)
   14        -15 (True, 29, 2, 30.29609704017639)
   15        -16 (True, 27, 1, 23.91221523284912)
   16        -17 (True, 45, 2, 52.179850816726685)
   17        -18 (True, 34, 2, 38.0179545879364)
   18        -19 (True, 27, 1, 22.081477165222168)
   19        -20 (True, 52, 2, 57.48599147796631)
   20        -21 (True, 21, 0, 21.24903392791748)
   21        -22 (True, 30, 2, 37.5386917591095)
   22        -24 (True, 19, 1, 20.510115385055542)
   23        -25 (True, 36, 1, 36.27837538719177)
   24        -26 (True, 33, 2, 41.65943884849548)
   25        -27 (True, 25, 0, 30.9220449924469)
   26        -28 (True, 47, 1, 60.319626808166504)
   27        -31 (True, 39, 1, 54.2931227684021)
   28        -32 (True, 43, 2, 54.85727024078369)
   29        -33 (True, 45, 2, 56.75646710395813)
   30        -36 (True, 24, 1, 21.818586111068726)
   31        -39 (True, 45, 2, 55.257946252822876)
   32        -40 (True, 31, 1, 34.094388484954834)
   33        -41 (True, 29, 1, 28.48836350440979)
   34        -43 (True, 26, 1, 21.424931526184082)
   35        -44 (True, 30, 2, 35.7546501159668)
   36        -45 (True, 44, 2, 53.590073585510254)
   37        -46 (True, 26, 1, 32.86268901824951)
   38        -50 (True, 46, 2, 48.59174656867981)
   39        -51 (True, 29, 1, 32.24302124977112)
   40        -52 (True, 58, 2, 62.643776416778564)
   41        -53 (True, 44, 2, 45.79771566390991)
   42        -55 (True, 56, 2, 58.44292163848877)
   43        -56 (True, 28, 1, 22.507607460021973)
   44        -58 (True, 21, 1, 25.118072509765625)
   45        -59 (True, 55, 2, 57.27587962150574)
   46        -61 (True, 30, 1, 28.41112780570984)
   47        -62 (True, 29, 1, 20.521795988082886)
   48        -63 (True, 27, 1, 25.936198949813843)
   49        -64 (True, 32, 1, 29.715338230133057)
   50        -65 (True, 27, 0, 24.168847799301147)
   51        -66 (True, 41, 2, 40.606157302856445)
   52        -67 (True, 48, 2, 52.30963897705078)
   53        -70 (True, 35, 1, 30.777546167373657)
   54        -71 (True, 52, 2, 52.772658348083496)
   55        -72 (True, 51, 2, 47.925705671310425)
   56        -73 (True, 37, 2, 32.55638670921326)
   57        -76 (True, 40, 1, 39.88845419883728)
   58        -78 (True, 28, 2, 23.338553428649902)
   59        -80 (True, 39, 2, 35.555004596710205)
   60        -82 (True, 39, 2, 32.58023715019226)
   61        -83 (True, 29, 2, 26.03005838394165)
   62        -84 (True, 26, 1, 23.71669840812683)
   63        -85 (True, 44, 2, 43.41327476501465)
   64        -86 (True, 45, 2, 39.73675012588501)
   65        -87 (True, 37, 1, 27.45497751235962)
   66        -88 (True, 30, 1, 25.342838764190674)
   67        -89 (True, 50, 2, 46.96338391304016)
   68        -90 (True, 27, 1, 26.090787649154663)
   69        -91 (True, 32, 2, 35.03382110595703)
   70        -92 (True, 28, 1, 24.249154090881348)
   71        -93 (True, 42, 2, 32.150060176849365)
   72        -94 (True, 19, 0, 21.742794036865234)
   73        -95 (True, 33, 1, 20.39409828186035)
   74        -96 (True, 47, 2, 20.63382363319397)
   75        -success 100 / 100 mean steps 31.94 max time 69.66143441200256
           1 +0 (True, 45, 2, 46.85230565071106)
           2 +2 (True, 62, 2, 71.21768307685852)
           3 +4 (True, 57, 2, 57.19032168388367)
           4 +5 (True, 48, 2, 42.683635234832764)
           5 +6 (True, 37, 1, 29.496540069580078)
           6 +7 (True, 39, 2, 31.63803720474243)
           7 +8 (True, 43, 2, 51.06836748123169)
           8 +9 (True, 25, 1, 28.28107762336731)
           9 +10 (True, 28, 2, 35.01765584945679)
          10 +12 (True, 31, 1, 36.89882206916809)
          11 +13 (True, 41, 2, 51.72081279754639)
          12 +15 (True, 29, 2, 33.781227350234985)
          13 +16 (True, 27, 1, 25.88964819908142)
          14 +17 (True, 45, 2, 56.948575258255005)
          15 +18 (True, 34, 2, 33.21874785423279)
          16 +19 (True, 27, 1, 25.62008571624756)
          17 +20 (True, 52, 2, 59.69813323020935)
          18 +22 (True, 30, 2, 35.45942783355713)
          19 +23 (True, 20, 0, 22.526623725891113)
          20 +24 (True, 19, 1, 25.511611700057983)
          21 +25 (True, 36, 1, 48.046573638916016)
          22 +26 (True, 33, 2, 38.17432355880737)
          23 +27 (True, 25, 0, 24.712105989456177)
          24 +28 (True, 47, 1, 58.62340998649597)
          25 +30 (True, 20, 0, 21.140946626663208)
          26 +31 (True, 39, 1, 46.2608208656311)
          27 +32 (True, 47, 2, 59.395349979400635)
          28 +33 (True, 45, 2, 58.64613056182861)
          29 +36 (True, 24, 1, 22.5258047580719)
          30 +39 (True, 45, 2, 67.31529545783997)
          31 +40 (True, 31, 1, 36.85645651817322)
          32 +41 (True, 29, 1, 37.305859088897705)
          33 +43 (True, 26, 1, 27.750036239624023)
          34 +44 (True, 30, 2, 34.831286907196045)
          35 +45 (True, 44, 2, 58.91051411628723)
          36 +46 (True, 26, 1, 29.921911001205444)
          37 +47 (True, 14, 0, 20.188241720199585)
          38 +50 (True, 46, 2, 53.74320673942566)
          39 +51 (True, 29, 1, 30.2227623462677)
          40 +52 (True, 49, 2, 52.127910137176514)
          41 +53 (True, 44, 2, 53.82998967170715)
          42 +55 (True, 56, 2, 61.39019179344177)
          43 +58 (True, 21, 1, 23.66989302635193)
          44 +59 (True, 55, 2, 62.231321573257446)
          45 +60 (True, 17, 0, 21.428409814834595)
          46 +61 (True, 30, 1, 30.904994249343872)
          47 +62 (True, 29, 1, 28.426175117492676)
          48 +63 (True, 27, 1, 28.621488332748413)
          49 +64 (True, 32, 1, 30.79403781890869)
          50 +65 (True, 27, 0, 25.10242509841919)
          51 +66 (True, 41, 2, 39.1325249671936)
          52 +67 (True, 48, 2, 53.29757905006409)
          53 +70 (True, 35, 1, 39.00916647911072)
          54 +71 (True, 52, 2, 66.1783800125122)
          55 +72 (True, 51, 2, 60.64312982559204)
          56 +73 (True, 37, 2, 37.76424431800842)
          57 +75 (True, 26, 1, 21.290743112564087)
          58 +76 (True, 40, 1, 35.70845675468445)
          59 +78 (True, 28, 2, 36.83675217628479)
          60 +80 (True, 39, 2, 41.264421224594116)
          61 +82 (True, 39, 2, 31.366724014282227)
          62 +83 (True, 29, 2, 28.59096360206604)
          63 +84 (True, 26, 1, 22.5652437210083)
          64 +85 (True, 44, 2, 43.184794664382935)
          65 +86 (True, 45, 2, 44.032809257507324)
          66 +87 (True, 37, 1, 28.163620710372925)
          67 +88 (True, 30, 1, 24.677587747573853)
          68 +89 (True, 46, 2, 45.38135886192322)
          69 +90 (True, 27, 1, 22.142090320587158)
          70 +91 (True, 32, 2, 35.8639702796936)
          71 +92 (True, 28, 1, 22.218411207199097)
          72 +93 (True, 42, 2, 32.04357600212097)
          73 +95 (True, 33, 1, 22.84307050704956)
          74 +96 (True, 47, 2, 22.22419548034668)
          75 +success 100 / 100 mean steps 31.85 max time 71.21768307685852
```

</details>

<a id="C026"></a>
### C026 · Test results for 12-obstruction stress batch

Commit `e7d8ee408698d4ca3453b5accdd8dc3d48342f76`; parents: c09ea7fb670ff583bc80e3ca01e1e405f713935f. Recorded author date: 2026-10-01T01:38:34+02:00.

File roles (automatic): setup/other.

- [E1318](01_timeline.md#E1318): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C026_e7d8ee4.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/r12b.txt b/r12b.txt
new file mode 100644
index 0000000..7c7d88d
--- /dev/null
+++ b/r12b.txt
@@ -0,0 +1,33 @@
           1 +400 (True, 110, 12, 83.93183994293213)
           2 +401 (True, 107, 12, 84.79543662071228)
           3 +402 (True, 90, 12, 54.055529832839966)
           4 +403 (True, 89, 12, 57.647993326187134)
           5 +404 (True, 82, 12, 44.441516399383545)
           6 +405 (True, 79, 12, 36.674352169036865)
           7 +406 (True, 57, 12, 20.8955135345459)
           8 +407 (True, 75, 12, 31.98997974395752)
           9 +408 (True, 107, 12, 75.04842495918274)
          10 +409 (True, 76, 12, 51.91107392311096)
          11 +410 (True, 139, 12, 89.26716995239258)
          12 +411 (True, 89, 12, 54.25050663948059)
          13 +412 (True, 106, 12, 69.91811156272888)
          14 +413 (True, 81, 12, 52.51455640792847)
          15 +414 (True, 115, 12, 80.54345846176147)
          16 +415 (True, 151, 12, 100.14505171775818)
          17 +416 (True, 68, 12, 51.189002990722656)
          18 +417 (True, 113, 12, 88.94455933570862)
          19 +418 (True, 103, 12, 79.25154995918274)
          20 +419 (True, 166, 12, 134.1313796043396)
          21 +420 (True, 140, 12, 112.80616402626038)
          22 +421 (True, 70, 12, 55.09461498260498)
          23 +422 (True, 114, 12, 92.06537103652954)
          24 +423 (True, 103, 12, 75.68777966499329)
          25 +424 (True, 116, 12, 88.36362719535828)
          26 +425 (True, 77, 12, 64.82507276535034)
          27 +426 (True, 80, 12, 56.041191816329956)
          28 +427 (True, 115, 12, 64.81475639343262)
          29 +428 (True, 118, 12, 37.91998815536499)
          30 +429 (True, 65, 12, 24.86489248275757)
          31 +430 (True, 117, 12, 34.154709815979004)
          32 +431 (True, 96, 12, 26.69318985939026)
          33 +success 32 / 32 mean steps 100.4375 max time 134.1313796043396
```

</details>

